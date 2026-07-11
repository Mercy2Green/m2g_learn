from __future__ import annotations

import argparse
import csv
import json
import os
import shutil
from collections import Counter
from pathlib import Path
import sys
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from src.load_config import load_dotenv  # noqa: E402
from src.providers.ollama_provider import OllamaProvider  # noqa: E402
from src.response_parser import parse_model_response  # noqa: E402


AUDIT_VERSION = "task_image_audit_v1"
ALLOWED = {
    "audit_version": {AUDIT_VERSION},
    "o0_target_visible": {"yes", "no", "unclear"},
    "o0_target_category": {"multiple_bottles", "remote", "single_object", "none", "unclear"},
    "o1_contains_original_target": {"yes", "no", "unclear"},
    "o1_contains_candidate_helper": {"yes", "no", "unclear"},
    "o1_helper_type": {
        "tray", "baking_tray", "basket", "box", "bag", "pan", "long_rigid", "pencil", "lamp",
        "wrong_object", "none", "unclear",
    },
    "o1_helper_visibility": {"clear", "partial", "ambiguous", "not_visible"},
    "o1_helper_affordance": {
        "container_for_multiple_objects", "long_rigid_reach_extension", "not_suitable", "none", "unclear",
    },
    "o1_wrong_helper_visible": {"yes", "no", "unclear"},
    "image_quality": {"good", "usable", "ambiguous", "bad"},
    "audit_confidence": {"high", "medium", "low"},
}
TEXT_FIELDS = ["o0_target_count_estimate", "o1_helper_description", "visual_notes"]
DEFAULT_OVERRIDE = {
    "match_o1_basename": "container_o1_000001.jpg",
    "override_reason": "User manually confirmed this O1 image contains a clear baking tray / tray.",
    "o1_contains_candidate_helper": "yes",
    "o1_helper_type": "baking_tray",
    "o1_helper_description": "Clear baking tray / tray confirmed by the user.",
    "o1_helper_visibility": "clear",
    "o1_helper_affordance": "container_for_multiple_objects",
    "audit_confidence": "high",
}

SYSTEM_PROMPT = """You are auditing task images only. Do not judge any model response.
The two images are O0 then O1.
O0 usually contains the original task target or scene.
O1 is a later observation and may contain a helper object.
Do not require O1 to contain the original target.
Your job is only to describe what is visible and what affordance it has.

For aggregate transport:
* tray, baking tray, metal tray, pan, basket, box, bag, container can be helper.
* pencil, lamp, phone, remote, book are not container helpers.

For reach extension:
* broom, stick, rod, pole, hanger, mop, long rigid object can be helper.
* short object, soft cloth, bottle, pillow, pencil are usually not valid reach-extension helpers unless clearly long-rigid.

Return strict JSON only.

Required JSON schema:
{
  "audit_version": "task_image_audit_v1",
  "o0_target_visible": "yes/no/unclear",
  "o0_target_category": "multiple_bottles/remote/single_object/none/unclear",
  "o0_target_count_estimate": "string",
  "o1_contains_original_target": "yes/no/unclear",
  "o1_contains_candidate_helper": "yes/no/unclear",
  "o1_helper_type": "tray/baking_tray/basket/box/bag/pan/long_rigid/pencil/lamp/wrong_object/none/unclear",
  "o1_helper_description": "string",
  "o1_helper_visibility": "clear/partial/ambiguous/not_visible",
  "o1_helper_affordance": "container_for_multiple_objects/long_rigid_reach_extension/not_suitable/none/unclear",
  "o1_wrong_helper_visible": "yes/no/unclear",
  "image_quality": "good/usable/ambiguous/bad",
  "audit_confidence": "high/medium/low",
  "visual_notes": "string"
}"""


def main() -> None:
    args = parse_args()
    load_dotenv(ROOT / ".env")
    input_dir = resolve_path(args.input_dir)
    output_dir = resolve_path(args.output_dir) if args.output_dir else input_dir / "task_image_audit_qwen32"
    raw_rows = read_jsonl(input_dir / "raw_responses.jsonl")
    pairs = unique_pairs(raw_rows)
    if args.limit is not None:
        pairs = pairs[: args.limit]

    preserved = read_jsonl(output_dir / "manual_image_audit_overrides.jsonl") if (
        output_dir / "manual_image_audit_overrides.jsonl"
    ).is_file() else []
    prepare_output(output_dir, args.overwrite)
    overrides = merge_overrides(preserved)
    write_jsonl(output_dir / "manual_image_audit_overrides.jsonl", overrides)

    provider = OllamaProvider({
        "model_id": f"task_image_audit_{safe_name(args.audit_model)}", "model_name": args.audit_model,
        "provider_label": "ollama_task_image_audit", "base_url": os.environ.get("OLLAMA_BASE_URL", "http://localhost:11434"),
        "temperature": 0.0, "max_tokens": args.max_tokens, "num_ctx": args.num_ctx,
        "timeout_seconds": args.timeout_seconds, "retries": 1, "format_json": True, "keep_alive": "10m",
    })
    audited: list[dict[str, Any]] = []
    for index, pair in enumerate(pairs, start=1):
        row = audit_one(provider, pair, overrides, args.audit_model)
        audited.append(row)
        print(f"audited {index}/{len(pairs)}: {pair['sample_id']} status={row['audit_status']}", flush=True)

    write_jsonl(output_dir / "image_pair_audit.jsonl", audited)
    write_by_sample(output_dir / "image_pair_audit_by_sample.csv", audited)
    write_manifest(output_dir / "image_audit_manifest.csv", audited)
    (output_dir / "image_pair_audit_summary.md").write_text(build_summary(audited, len(unique_pairs(raw_rows))), encoding="utf-8")
    (output_dir / "image_pair_audit_disagreements.md").write_text(build_disagreements(audited), encoding="utf-8")
    print(f"Wrote task image audit: {output_dir}", flush=True)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Audit unique O0/O1 task image pairs without judging model responses.")
    parser.add_argument("--input_dir", required=True)
    parser.add_argument("--output_dir")
    parser.add_argument("--audit_model", default="qwen3-vl:32b-instruct-q4_K_M")
    parser.add_argument("--limit", type=int)
    parser.add_argument("--max_tokens", type=int, default=1024)
    parser.add_argument("--num_ctx", type=int, default=8192)
    parser.add_argument("--timeout_seconds", type=int, default=420)
    parser.add_argument("--overwrite", action="store_true")
    return parser.parse_args()


def unique_pairs(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    unique: dict[tuple[str, str, str], dict[str, Any]] = {}
    for row in rows:
        key = (str(row.get("sample_id", "")), str(row.get("o0_image_path", "")), str(row.get("o1_image_path", "")))
        record = {
            "sample_id": row.get("sample_id", ""), "sample_type": row.get("sample_type", ""),
            "group_id": row.get("group_id", ""), "instruction": row.get("instruction", ""),
            "gold_expectation": row.get("gold", {}), "o0_image_path": row.get("o0_image_path", ""),
            "o1_image_path": row.get("o1_image_path", ""),
        }
        if key in unique and unique[key] != record:
            raise ValueError(f"Conflicting metadata for image pair: {key}")
        unique[key] = record
    return [unique[key] for key in sorted(unique)]


def audit_one(provider: OllamaProvider, pair: dict[str, Any], overrides: list[dict[str, Any]], model: str) -> dict[str, Any]:
    base = {
        "audit_version": AUDIT_VERSION, "audit_model": model, **pair, "audit_status": "error", "audit_error": "",
        "audit_raw_response": "", **audit_defaults(), "audit_overridden": False, "audit_override_reason": "",
    }
    try:
        payload = {key: pair[key] for key in ("sample_id", "sample_type", "group_id", "instruction", "gold_expectation")}
        result = provider.run_chat_with_retry([
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": "Audit these ordered O0 and O1 task images:\n" + json.dumps(payload, ensure_ascii=False, indent=2),
             "images": [str(resolve_path(pair["o0_image_path"])), str(resolve_path(pair["o1_image_path"]))]},
        ])
        base["audit_raw_response"] = str(result.get("raw_response", ""))
        parsed = parse_model_response(base["audit_raw_response"])
        if parsed["parse_status"] != "ok":
            raise ValueError(parsed["parse_error"])
        base.update(validate_audit(parsed["parsed"]))
        base["audit_status"] = "ok"
    except Exception as exc:  # noqa: BLE001
        base["audit_error"] = str(exc)
    override = find_override(pair, overrides)
    if override:
        for key, value in override.items():
            if key not in {"match_o1_basename", "override_reason"}:
                base[key] = value
        base["audit_overridden"] = True
        base["audit_override_reason"] = str(override.get("override_reason", ""))
    return base


def audit_defaults() -> dict[str, str]:
    return {
        "o0_target_visible": "unclear", "o0_target_category": "unclear", "o0_target_count_estimate": "unclear",
        "o1_contains_original_target": "unclear", "o1_contains_candidate_helper": "unclear",
        "o1_helper_type": "unclear", "o1_helper_description": "unclear", "o1_helper_visibility": "ambiguous",
        "o1_helper_affordance": "unclear", "o1_wrong_helper_visible": "unclear", "image_quality": "ambiguous",
        "audit_confidence": "low", "visual_notes": "Audit unavailable.",
    }


def validate_audit(parsed: dict[str, Any]) -> dict[str, str]:
    output: dict[str, str] = {}
    for key, allowed in ALLOWED.items():
        value = str(parsed.get(key, "")).strip().lower()
        if value not in allowed:
            raise ValueError(f"Invalid audit field {key}={value!r}")
        output[key] = value
    for key in TEXT_FIELDS:
        value = str(parsed.get(key, "")).strip()
        if key == "o1_helper_description" and not value and output.get("o1_helper_type") == "none":
            value = "none visible"
        if not value:
            raise ValueError(f"Audit field {key} is empty")
        output[key] = value
    return output


def merge_overrides(existing: list[dict[str, Any]]) -> list[dict[str, Any]]:
    merged = {str(row.get("match_o1_basename", "")): row for row in existing if row.get("match_o1_basename")}
    key = DEFAULT_OVERRIDE["match_o1_basename"]
    merged[key] = {**DEFAULT_OVERRIDE, **merged.get(key, {})}
    return [merged[key] for key in sorted(merged)]


def find_override(pair: dict[str, Any], overrides: list[dict[str, Any]]) -> dict[str, Any] | None:
    basename = Path(str(pair["o1_image_path"])).name
    return next((row for row in overrides if row.get("match_o1_basename") == basename), None)


def write_by_sample(path: Path, rows: list[dict[str, Any]]) -> None:
    fields = [
        "sample_id", "sample_type", "group_id", "o0_image_path", "o1_image_path", "audit_status",
        "o0_target_visible", "o0_target_category", "o1_contains_candidate_helper", "o1_helper_type",
        "o1_helper_visibility", "o1_helper_affordance", "image_quality", "audit_confidence",
        "audit_overridden", "audit_override_reason",
    ]
    write_csv(path, rows, fields)


def write_manifest(path: Path, rows: list[dict[str, Any]]) -> None:
    fields = ["sample_id", "o0_basename", "o1_basename", "o0_image_path", "o1_image_path", "audit_status", "audit_overridden"]
    manifest = [{
        "sample_id": row["sample_id"], "o0_basename": Path(row["o0_image_path"]).name,
        "o1_basename": Path(row["o1_image_path"]).name, "o0_image_path": row["o0_image_path"],
        "o1_image_path": row["o1_image_path"], "audit_status": row["audit_status"],
        "audit_overridden": row["audit_overridden"],
    } for row in rows]
    write_csv(path, manifest, fields)


def build_summary(rows: list[dict[str, Any]], available: int) -> str:
    status = Counter(row["audit_status"] for row in rows)
    helper = Counter(row["o1_contains_candidate_helper"] for row in rows)
    quality = Counter(row["image_quality"] for row in rows)
    return "\n".join([
        "# Task Image Audit Summary", "", f"- audit version: {AUDIT_VERSION}", f"- unique pairs available: {available}",
        f"- pairs selected: {len(rows)}", f"- audit ok: {status['ok']}", f"- audit errors: {status['error']}",
        f"- manual override rows: {sum(bool(row['audit_overridden']) for row in rows)}",
        f"- O1 candidate helper yes/no/unclear: {helper['yes']}/{helper['no']}/{helper['unclear']}",
        f"- image quality good/usable/ambiguous/bad: {quality['good']}/{quality['usable']}/{quality['ambiguous']}/{quality['bad']}", "",
        "This audit describes task images only and does not judge candidate model responses.",
    ]) + "\n"


def build_disagreements(rows: list[dict[str, Any]]) -> str:
    selected = [row for row in rows if row["audit_overridden"] or row["audit_status"] != "ok" or row["image_quality"] in {"ambiguous", "bad"}]
    lines = ["# Task Image Audit Disagreements and Review", "", "Overrides and uncertain image audits are listed here.", ""]
    for row in selected:
        lines.append(
            f"- {row['sample_id']} / {Path(row['o1_image_path']).name}: helper={row['o1_helper_type']} "
            f"visibility={row['o1_helper_visibility']} quality={row['image_quality']} overridden={row['audit_overridden']} "
            f"reason={row['audit_override_reason'] or row['audit_error'] or row['visual_notes']}"
        )
    return "\n".join(lines) + "\n"


def resolve_path(value: str | Path) -> Path:
    path = Path(value)
    return path.resolve() if path.is_absolute() else (ROOT / path).resolve()


def prepare_output(path: Path, overwrite: bool) -> None:
    if not path.name.startswith("task_image_audit_"):
        raise SystemExit(f"Refusing non-audit output directory: {path}")
    if path.exists():
        if not overwrite:
            raise SystemExit(f"Output exists: {path}. Use --overwrite.")
        shutil.rmtree(path)
    path.mkdir(parents=True, exist_ok=True)


def read_jsonl(path: Path) -> list[dict[str, Any]]:
    if not path.is_file():
        raise FileNotFoundError(path)
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def write_jsonl(path: Path, rows: list[dict[str, Any]]) -> None:
    with path.open("w", encoding="utf-8") as handle:
        for row in rows:
            handle.write(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n")


def write_csv(path: Path, rows: list[dict[str, Any]], fields: list[str]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def safe_name(value: str) -> str:
    return "".join(char if char.isalnum() else "_" for char in value)


if __name__ == "__main__":
    main()
