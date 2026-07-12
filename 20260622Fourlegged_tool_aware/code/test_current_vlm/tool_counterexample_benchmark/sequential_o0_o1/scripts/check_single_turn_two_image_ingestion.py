from __future__ import annotations

import argparse
import csv
import hashlib
import json
import shutil
import struct
from collections import Counter, defaultdict
from pathlib import Path
import sys
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
AHD_ROOT = ROOT.parents[1] / "AHD-benchmark"
sys.path.insert(0, str(ROOT))

from sequential_o0_o1.scripts.run_sequential_eval import apply_model_overrides  # noqa: E402
from src.load_config import load_dotenv, load_yaml  # noqa: E402
from src.providers.factory import create_provider  # noqa: E402
from src.response_parser import parse_model_response  # noqa: E402


DEFAULT_SAMPLE_IDS = [
    "positive_aggregate_001", "no_tool_control_001", "same_o1_aggregate_001",
    "same_o1_direct_001", "wrong_helper_negative_aggregate_001",
]
TEST_CASES = ["O0_O1", "O1_O0", "O0_only", "O1_only", "O0_O0"]
SYSTEM_PROMPT = """You are a vision-language model diagnostic checker.
This is not a robot planning task.
Your only job is to inspect the provided image inputs and report what you can see.
Do not solve the robot task.
Do not infer hidden scene state.
Do not assume there are two images unless you can inspect two image inputs.
Return only one valid JSON object."""
USER_PROMPT = """You are given image input(s).
Please answer only the following diagnostic questions.

1. How many images do you perceive?
2. Describe image_1.
3. Describe image_2 if present.
4. Are image_1 and image_2 visually different?
5. Which image contains the original task target, if any?
6. Which image contains a potential helper object, if any?
7. Can you distinguish first image from second image by visual content?

Return JSON with exactly this schema:
{
  "perceived_image_count": "0/1/2/more/unclear",
  "image_1_description": "string",
  "image_2_description": "string or none",
  "image_1_key_objects": ["string"],
  "image_2_key_objects": ["string"],
  "images_visually_different": "yes/no/unclear/not_applicable",
  "image_1_contains_task_target": "yes/no/unclear/not_applicable",
  "image_2_contains_task_target": "yes/no/unclear/not_applicable",
  "image_1_contains_potential_helper": "yes/no/unclear/not_applicable",
  "image_2_contains_potential_helper": "yes/no/unclear/not_applicable",
  "can_distinguish_image_order": "yes/no/unclear",
  "evidence": "brief visual evidence"
}

Important:
* Do not mention helper-chain.
* Do not plan actions.
* Do not use the original task instruction.
* This is only an image ingestion diagnostic."""

O0_TERMS = ["bottle", "bottles", "water", "drink", "drinks", "水瓶", "瓶子", "饮料", "水"]
CONTAINER_TERMS = ["tray", "baking tray", "metal tray", "pan", "container", "托盘", "烤盘", "盘"]
WRONG_TERMS = ["pencil", "pen", "desk item", "writing", "铅笔", "笔", "文具"]


def main() -> None:
    args = parse_args()
    load_dotenv(ROOT / ".env")
    samples_path = resolve_samples(args.samples)
    output_dir = resolve_path(args.output_dir)
    existing_raw = read_jsonl(output_dir / "diagnostic_raw_responses.jsonl") if args.reuse_raw else []
    if not args.reuse_raw:
        prepare_output(output_dir, args.overwrite)

    all_samples = read_jsonl(samples_path)
    by_id = {str(row.get("sample_id", "")): row for row in all_samples}
    missing = sorted(set(args.sample_ids) - set(by_id))
    if missing:
        raise ValueError(f"Missing diagnostic sample IDs: {missing}")
    samples = [by_id[sample_id] for sample_id in args.sample_ids]
    if args.limit is not None:
        samples = samples[: args.limit]
    validate_no_reach(samples)

    models = select_models(args.models, args.model_overrides, args.model_ids)
    cases = build_cases(samples, models)
    manifests = [build_manifest(case) for case in cases]
    write_jsonl(output_dir / "payload_manifest.jsonl", manifests)
    (output_dir / "payload_manifest_summary.md").write_text(
        build_manifest_summary(manifests, samples_path), encoding="utf-8"
    )

    if args.reuse_raw:
        raw_rows = existing_raw
        expected_keys = {(case["sample_id"], case["model_id"], case["test_case_id"]) for case in cases}
        actual_keys = {(row["sample_id"], row["model_id"], row["test_case_id"]) for row in raw_rows}
        if expected_keys != actual_keys:
            raise ValueError("Existing raw response keys do not match the selected diagnostic cases.")
    else:
        providers = {str(model["model_id"]): create_provider(model) for model in models}
        raw_rows = []
        for index, case in enumerate(cases, start=1):
            raw = run_case(case, providers[str(case["model_id"])])
            raw_rows.append(raw)
            print(f"diagnostic {index}/{len(cases)}: {case['sample_id']} / {case['model_id']} / {case['test_case_id']} error={bool(raw['error'])}", flush=True)
        write_jsonl(output_dir / "diagnostic_raw_responses.jsonl", raw_rows)

    scored = [score_row(row) for row in raw_rows]
    write_csv(output_dir / "diagnostic_scored.csv", scored, SCORE_FIELDS)
    (output_dir / "diagnostic_summary.md").write_text(
        build_diagnostic_summary(manifests, scored, samples_path), encoding="utf-8"
    )
    (output_dir / "diagnostic_manual_review.md").write_text(
        build_manual_review(raw_rows, scored), encoding="utf-8"
    )
    print(f"Wrote diagnostic outputs: {output_dir}", flush=True)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Sanity-check single-turn two-image ingestion and image order perception.")
    parser.add_argument("--samples", default="sequential_o0_o1/data/sequential_core_clean_samples_v2.jsonl")
    parser.add_argument("--models", default="config/models.yaml")
    parser.add_argument("--model_overrides", default="sequential_o0_o1/config/sequential_model_overrides.yaml")
    parser.add_argument("--model_ids", nargs="+", default=["ollama_qwen3_5_35b"])
    parser.add_argument("--sample_ids", nargs="+", default=DEFAULT_SAMPLE_IDS)
    parser.add_argument("--output_dir", default=str(AHD_ROOT / "outputs/sanity_check_single_turn_two_images"))
    parser.add_argument("--limit", type=int)
    parser.add_argument("--overwrite", action="store_true")
    parser.add_argument("--reuse_raw", action="store_true", help="Rescore the existing raw responses without model calls.")
    return parser.parse_args()


def resolve_samples(value: str) -> Path:
    requested = resolve_path(value)
    if requested.is_file():
        return requested
    canonical = ROOT / "sequential_o0_o1/data/sequential_core_eval_samples.jsonl"
    if Path(value).name == "sequential_core_clean_samples_v2.jsonl" and canonical.is_file():
        return canonical
    raise FileNotFoundError(f"Samples file not found: {requested}")


def select_models(models_path: str, overrides_path: str, selected: list[str]) -> list[dict[str, Any]]:
    models = load_yaml(resolve_path(models_path)).get("models", [])
    overrides = load_yaml(resolve_path(overrides_path)).get("model_overrides", [])
    merged = apply_model_overrides(models, overrides)
    by_id = {str(row.get("model_id", "")): row for row in merged}
    missing = sorted(set(selected) - set(by_id))
    if missing:
        raise ValueError(f"Unknown model IDs: {missing}")
    output = [dict(by_id[model_id]) for model_id in selected]
    for row in output:
        if not row.get("supports_vision", False):
            raise ValueError(f"Selected model does not declare vision support: {row['model_id']}")
        if row.get("provider") == "ollama":
            row["think"] = False
    return output


def build_cases(samples: list[dict[str, Any]], models: list[dict[str, Any]]) -> list[dict[str, Any]]:
    output: list[dict[str, Any]] = []
    for model in models:
        for sample in samples:
            o0, o1 = resolve_path(sample["o0_image_path"]), resolve_path(sample["o1_image_path"])
            orders = {
                "O0_O1": [o0, o1], "O1_O0": [o1, o0], "O0_only": [o0], "O1_only": [o1], "O0_O0": [o0, o0],
            }
            for test_case_id in TEST_CASES:
                output.append({
                    "sample": sample, "sample_id": sample["sample_id"], "sample_type": sample["sample_type"],
                    "model": model, "model_id": model["model_id"], "test_case_id": test_case_id,
                    "image_order": test_case_id, "o0_image_path": o0, "o1_image_path": o1,
                    "sent_image_paths": orders[test_case_id],
                })
    return output


def build_manifest(case: dict[str, Any]) -> dict[str, Any]:
    paths = case["sent_image_paths"]
    provider = str(case["model"].get("provider", ""))
    return {
        "sample_id": case["sample_id"], "model_id": case["model_id"], "test_case_id": case["test_case_id"],
        "image_order": case["image_order"], "message_count": 2, "user_message_count": 1,
        "images_per_user_message": [len(paths)], "image_count_total": len(paths),
        "o0_image_path": str(case["o0_image_path"]), "o1_image_path": str(case["o1_image_path"]),
        "sent_image_paths": [str(path) for path in paths], "sent_image_basenames": [path.name for path in paths],
        "sent_image_sha256": [sha256(path) for path in paths],
        "sent_image_file_size_bytes": [path.stat().st_size for path in paths],
        "sent_image_dimensions": [list(image_dimensions(path)) for path in paths], "provider": provider,
        "expected_provider_transport": "ollama_images_base64" if provider == "ollama" else "openai_image_url_data_url",
    }


def run_case(case: dict[str, Any], provider: Any) -> dict[str, Any]:
    base = {
        "sample_id": case["sample_id"], "sample_type": case["sample_type"], "model_id": case["model_id"],
        "test_case_id": case["test_case_id"], "image_order": case["image_order"],
        "sent_image_paths": [str(path) for path in case["sent_image_paths"]],
        "sent_image_basenames": [path.name for path in case["sent_image_paths"]],
        "system_prompt": SYSTEM_PROMPT, "user_prompt": USER_PROMPT, "raw_response": "", "metadata": {}, "error": "",
    }
    try:
        result = provider.run_chat_with_retry([
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": USER_PROMPT, "images": base["sent_image_paths"]},
        ])
        base["raw_response"] = str(result.get("raw_response", ""))
        base["metadata"] = result.get("metadata", {})
    except Exception as exc:  # noqa: BLE001
        base["error"] = str(exc)
    return base


SCORE_FIELDS = [
    "sample_id", "sample_type", "model_id", "test_case_id", "sent_image_count",
    "model_perceived_two_images", "model_distinguishes_order", "image_1_mentions_o0_expected_content",
    "image_2_mentions_o1_expected_content", "single_turn_two_image_ingestion_pass", "failure_reason",
]


def score_row(row: dict[str, Any]) -> dict[str, Any]:
    base = {key: row.get(key, "") for key in ("sample_id", "sample_type", "model_id", "test_case_id")}
    base["sent_image_count"] = len(row["sent_image_paths"])
    if row["error"]:
        return {**base, **unknown_score("provider_error")}
    if not row["raw_response"].strip():
        return {**base, **unknown_score("empty_response")}
    parsed_result = parse_model_response(row["raw_response"])
    if parsed_result["parse_status"] != "ok":
        return {**base, **unknown_score("unclear")}
    parsed = parsed_result["parsed"]
    perceived = str(parsed.get("perceived_image_count", "unclear")).lower()
    perceived_two: bool | str = True if perceived == "2" else False if perceived in {"0", "1"} else "unclear"
    distinguish_value = str(parsed.get("can_distinguish_image_order", "unclear")).lower()
    if perceived_two is True:
        distinguishes: bool | str = True if distinguish_value == "yes" else False if distinguish_value == "no" else "unclear"
    else:
        distinguishes = False if perceived_two is False else "unclear"
    desc1 = image_text(parsed, 1)
    desc2 = image_text(parsed, 2)
    o1_terms = WRONG_TERMS if row["sample_type"] == "wrong_helper_negative" else CONTAINER_TERMS
    image1_o0 = mentions(desc1, O0_TERMS)
    image2_o1 = mentions(desc2, o1_terms)
    test_case = row["test_case_id"]
    passed: bool | str = "unclear"
    reason = "unclear"
    if test_case == "O0_O1":
        passed, reason = two_image_result(perceived_two, image1_o0, image2_o1, parsed, normal_order=True)
    elif test_case == "O1_O0":
        passed, reason = two_image_result(perceived_two, mentions(desc2, O0_TERMS), mentions(desc1, o1_terms), parsed, normal_order=False)
    elif test_case in {"O0_only", "O1_only"}:
        no_second = perceived == "1" or not meaningful_second_image(desc2)
        passed = no_second
        reason = "" if passed else "did_not_perceive_two_images"
    elif test_case == "O0_O0":
        visually_different = str(parsed.get("images_visually_different", "unclear")).lower()
        both_o0 = mentions(desc1, O0_TERMS) and mentions(desc2, O0_TERMS)
        invented_helper = mentions(desc2, CONTAINER_TERMS + WRONG_TERMS)
        passed = perceived_two is True and not invented_helper and (visually_different == "no" or both_o0)
        reason = "" if passed else "both_images_described_same" if visually_different == "yes" else "order_confused"
    return {
        **base, "sent_image_count": len(row["sent_image_paths"]), "model_perceived_two_images": perceived_two,
        "model_distinguishes_order": distinguishes, "image_1_mentions_o0_expected_content": image1_o0,
        "image_2_mentions_o1_expected_content": image2_o1, "single_turn_two_image_ingestion_pass": passed,
        "failure_reason": reason,
    }


def two_image_result(
    perceived_two: bool | str, first_expected: bool, second_expected: bool,
    parsed: dict[str, Any], *, normal_order: bool,
) -> tuple[bool | str, str]:
    if perceived_two is not True:
        return False if perceived_two is False else "unclear", "did_not_perceive_two_images"
    if not meaningful_second_image(image_text(parsed, 2)):
        return False, "did_not_describe_second_image"
    if not first_expected or not second_expected:
        return False, "order_confused"
    if str(parsed.get("images_visually_different", "unclear")).lower() == "no":
        return False, "both_images_described_same"
    return True, ""


def unknown_score(reason: str) -> dict[str, Any]:
    return {
        "model_perceived_two_images": "unclear", "model_distinguishes_order": "unclear",
        "image_1_mentions_o0_expected_content": "unclear", "image_2_mentions_o1_expected_content": "unclear",
        "single_turn_two_image_ingestion_pass": "unclear", "failure_reason": reason,
    }


def build_manifest_summary(rows: list[dict[str, Any]], samples_path: Path) -> str:
    dual = [row for row in rows if row["test_case_id"] in {"O0_O1", "O1_O0", "O0_O0"}]
    single = [row for row in rows if row["test_case_id"] in {"O0_only", "O1_only"}]
    unexpected_duplicates = sum(
        row["test_case_id"] in {"O0_O1", "O1_O0"} and len(set(row["sent_image_sha256"])) != 2 for row in rows
    )
    bad_o0o0 = sum(row["test_case_id"] == "O0_O0" and len(set(row["sent_image_sha256"])) != 1 for row in rows)
    return "\n".join([
        "# Static Two-Image Payload Audit", "", f"- samples source: `{samples_path}`", f"- total test cases: {len(rows)}",
        f"- image_count_total values: {dict(sorted(Counter(row['image_count_total'] for row in rows).items()))}",
        f"- expected two-image cases with image_count_total=2: {sum(row['image_count_total'] == 2 for row in dual)}/{len(dual)}",
        f"- expected one-image cases with image_count_total=1: {sum(row['image_count_total'] == 1 for row in single)}/{len(single)}",
        "- missing files: 0", f"- unexpected O0/O1 duplicate SHA patterns: {unexpected_duplicates}",
        f"- mismatched O0/O0 SHA patterns: {bad_o0o0}", "",
        "No base64 or data URL payload content is stored in this manifest.",
    ]) + "\n"


def build_diagnostic_summary(manifests: list[dict[str, Any]], rows: list[dict[str, Any]], samples_path: Path) -> str:
    lines = ["# Single-Turn Two-Image Ingestion Diagnostic", "", *build_manifest_summary(manifests, samples_path).splitlines()[2:], ""]
    for title, key in (("By Model", "model_id"), ("By Sample", "sample_id")):
        lines.extend([f"## {title}", "", *score_table(rows, key), ""])
    lines.extend([
        "This diagnostic only tests image ingestion and image-order perception.",
        "It does not rerun or replace the helper-chain benchmark and does not strengthen the original task prompt.",
    ])
    return "\n".join(lines) + "\n"


def score_table(rows: list[dict[str, Any]], key: str) -> list[str]:
    grouped: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in rows:
        grouped[str(row[key])].append(row)
    header = f"| {key} | O0_O1 | O1_O0 | O0_only | O1_only | O0_O0 | two-image perceived | order distinguish |"
    lines = [header, "| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |"]
    for name, subset in sorted(grouped.items()):
        rates = [case_rate(subset, test_case) for test_case in TEST_CASES]
        two_rows = [row for row in subset if row["test_case_id"] in {"O0_O1", "O1_O0", "O0_O0"}]
        lines.append(
            f"| {name} | {' | '.join(rates)} | {bool_rate(two_rows, 'model_perceived_two_images')} | "
            f"{bool_rate(two_rows, 'model_distinguishes_order')} |"
        )
    return lines


def build_manual_review(raw_rows: list[dict[str, Any]], scored_rows: list[dict[str, Any]]) -> str:
    raw_by_key = {(row["sample_id"], row["model_id"], row["test_case_id"]): row for row in raw_rows}
    selected: list[tuple[dict[str, Any], dict[str, Any], str]] = []
    for score in scored_rows:
        if score["single_turn_two_image_ingestion_pass"] is not True:
            selected.append((score, raw_by_key[(score["sample_id"], score["model_id"], score["test_case_id"])], "failure_or_unclear"))
    for test_case in TEST_CASES:
        successes = [row for row in scored_rows if row["test_case_id"] == test_case and row["single_turn_two_image_ingestion_pass"] is True][:2]
        for score in successes:
            selected.append((score, raw_by_key[(score["sample_id"], score["model_id"], score["test_case_id"])], "success_example"))
    lines = ["# Diagnostic Manual Review", "", "All failures/unclear rows plus up to two successes per test case.", ""]
    for score, raw, category in selected:
        lines.extend([
            f"## {raw['sample_id']} | {raw['model_id']} | {raw['test_case_id']}", "",
            f"- category: {category}", f"- sent images: {raw['sent_image_basenames']}",
            f"- pass: {score['single_turn_two_image_ingestion_pass']}", f"- failure reason: {score['failure_reason']}",
            f"- provider error: {raw['error']}", "", "Raw response:", "", "```json", raw["raw_response"] or "(empty)", "```", "",
        ])
    return "\n".join(lines) + "\n"


def image_text(parsed: dict[str, Any], index: int) -> str:
    description = str(parsed.get(f"image_{index}_description", ""))
    objects = parsed.get(f"image_{index}_key_objects", [])
    if not isinstance(objects, list):
        objects = [str(objects)]
    return " ".join([description, *(str(value) for value in objects)]).lower()


def meaningful_second_image(text: str) -> bool:
    normalized = text.strip().lower()
    return normalized not in {"", "none", "not applicable", "n/a", "no second image", "not present"}


def mentions(text: str, terms: list[str]) -> bool:
    return any(term in text for term in terms)


def case_rate(rows: list[dict[str, Any]], test_case: str) -> str:
    subset = [row for row in rows if row["test_case_id"] == test_case]
    return ratio(sum(row["single_turn_two_image_ingestion_pass"] is True for row in subset), len(subset))


def bool_rate(rows: list[dict[str, Any]], field: str) -> str:
    return ratio(sum(row[field] is True for row in rows), len(rows))


def ratio(numerator: int, denominator: int) -> str:
    return f"{numerator}/{denominator} ({numerator / denominator:.1%})" if denominator else "n/a"


def sha256(path: Path) -> str:
    if not path.is_file():
        raise FileNotFoundError(path)
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def image_dimensions(path: Path) -> tuple[int, int]:
    with path.open("rb") as handle:
        signature = handle.read(24)
        if signature.startswith(b"\x89PNG\r\n\x1a\n"):
            return struct.unpack(">II", signature[16:24])
        if not signature.startswith(b"\xff\xd8"):
            raise ValueError(f"Unsupported image format for dimensions: {path}")
        handle.seek(2)
        while True:
            marker_start = handle.read(1)
            if not marker_start:
                break
            if marker_start != b"\xff":
                continue
            marker = handle.read(1)
            while marker == b"\xff":
                marker = handle.read(1)
            if marker in {b"\xd8", b"\xd9"}:
                continue
            length_bytes = handle.read(2)
            if len(length_bytes) != 2:
                break
            segment_length = struct.unpack(">H", length_bytes)[0]
            if marker and marker[0] in {
                0xC0, 0xC1, 0xC2, 0xC3, 0xC5, 0xC6, 0xC7, 0xC9, 0xCA, 0xCB, 0xCD, 0xCE, 0xCF,
            }:
                payload = handle.read(5)
                if len(payload) != 5:
                    break
                height, width = struct.unpack(">HH", payload[1:5])
                return width, height
            handle.seek(segment_length - 2, 1)
    raise ValueError(f"Could not read image dimensions: {path}")


def validate_no_reach(samples: list[dict[str, Any]]) -> None:
    forbidden = [row["sample_id"] for row in samples if "reach" in str(row["sample_id"])]
    if forbidden:
        raise ValueError(f"Reach samples are excluded from this diagnostic: {forbidden}")


def prepare_output(path: Path, overwrite: bool) -> None:
    if path.name != "sanity_check_single_turn_two_images":
        raise SystemExit(f"Refusing unexpected output directory: {path}")
    if path.exists():
        if not overwrite:
            raise SystemExit(f"Output exists: {path}. Use --overwrite.")
        shutil.rmtree(path)
    path.mkdir(parents=True)


def resolve_path(value: str | Path) -> Path:
    path = Path(value)
    return path.resolve() if path.is_absolute() else (ROOT / path).resolve()


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
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


if __name__ == "__main__":
    main()
