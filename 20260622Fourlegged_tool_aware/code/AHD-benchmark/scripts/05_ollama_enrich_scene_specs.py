from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.enrichment_schema import FORBIDDEN_FIELDS, REQUIRED_FIELDS, check_forbidden_label_leakage, validate_enrichment_row
from src.jsonl_utils import write_jsonl
from src.load_config import load_dotenv, load_yaml
from src.ollama_client import OllamaClient, OllamaClientError


FORBIDDEN_OUTPUT_FIELDS = [
    "gold",
    "mode",
    "needed_helper_function",
    "helper_found",
    "selected_helper",
    "helper_target_relation",
    "continue_search",
    "direct_fallback_allowed",
    "target_memory",
    "helper_candidates_gold",
    "pairing_role",
]


def _model_id_for_path(model: str) -> str:
    return model.replace(":", "_").replace("/", "_")


def _public_spec(spec: dict[str, Any]) -> dict[str, Any]:
    return {
        "spec_id": spec.get("spec_id"),
        "view_stage": spec.get("view_stage"),
        "task_family": spec.get("task_family"),
        "spec_type": spec.get("spec_type"),
        "language": spec.get("language", {}),
        "robot_context": spec.get("robot_context", {}),
        "visual_scene": spec.get("visual_scene", {}),
    }


def _build_messages(spec: dict[str, Any], model_id: str) -> list[dict[str, str]]:
    output_schema = {
        "spec_id": spec["spec_id"],
        "model_id": model_id,
        "instruction_en_variant": "",
        "instruction_zh_variant": "",
        "cosmos_prompt_variant": "",
        "negative_prompt_variant": "",
        "notes": [],
    }
    user_prompt = {
        "task": "Rewrite visual and task wording for an image-generation dataset.",
        "rules": [
            "Do not infer labels.",
            "Do not include answer labels.",
            "Do not mention helper correctness.",
            "Preserve all required visible objects and forbidden visible objects.",
            "Use only visual wording and natural task wording.",
            "Return only valid JSON with exactly the requested fields.",
            f"Never output these fields: {', '.join(FORBIDDEN_OUTPUT_FIELDS)}.",
        ],
        "requested_output_schema": output_schema,
        "source_spec_without_gold": _public_spec(spec),
    }
    return [
        {
            "role": "system",
            "content": "You produce strict JSON only. You never add labels or hidden decisions.",
        },
        {
            "role": "user",
            "content": json.dumps(user_prompt, ensure_ascii=False, sort_keys=True),
        },
    ]


def _parse_response(raw_text: str, spec_id: str, model_id: str) -> dict[str, Any]:
    try:
        value = json.loads(raw_text)
    except json.JSONDecodeError as exc:
        return _error_row(spec_id, model_id, f"parse_error: {exc}")
    if not isinstance(value, dict):
        return _error_row(spec_id, model_id, "parse_error: response root is not an object")
    return _normalize_response_row(value, spec_id, model_id)


def _normalize_response_row(value: dict[str, Any], spec_id: str, model_id: str) -> dict[str, Any]:
    notes = _notes(value)
    extra_fields = set(value) - REQUIRED_FIELDS
    forbidden_fields = set(value) & FORBIDDEN_FIELDS
    if extra_fields:
        notes.append("schema_error: unexpected_output_fields")
    if forbidden_fields:
        notes.append("schema_error: forbidden_output_fields")
    if value.get("spec_id") != spec_id:
        notes.append("schema_warning: source_ids_restored")
    if value.get("model_id") != model_id:
        notes.append("schema_warning: source_ids_restored")

    row: dict[str, Any] = {
        "spec_id": spec_id,
        "model_id": model_id,
        "instruction_en_variant": _string_field(value, "instruction_en_variant", notes),
        "instruction_zh_variant": _string_field(value, "instruction_zh_variant", notes),
        "cosmos_prompt_variant": _string_field(value, "cosmos_prompt_variant", notes),
        "negative_prompt_variant": _string_field(value, "negative_prompt_variant", notes),
        "notes": notes,
    }
    return row


def _string_field(value: dict[str, Any], field: str, notes: list[str]) -> str:
    item = value.get(field, "")
    if isinstance(item, str):
        return item
    notes.append("schema_error: non_string_output_field")
    return ""


def _notes(row: dict[str, Any]) -> list[str]:
    notes = row.get("notes", [])
    if isinstance(notes, list):
        return [str(item) for item in notes]
    return [str(notes)]


def _error_row(spec_id: str, model_id: str, note: str) -> dict[str, Any]:
    return {
        "spec_id": spec_id,
        "model_id": model_id,
        "instruction_en_variant": "",
        "instruction_zh_variant": "",
        "cosmos_prompt_variant": "",
        "negative_prompt_variant": "",
        "notes": [note],
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", default=None)
    parser.add_argument("--max_specs", type=int, default=None)
    args = parser.parse_args()

    load_dotenv(ROOT / ".env")
    config = load_yaml(ROOT / "configs" / "ollama_text_enrichment.yaml")
    model_id = args.model or str(config["default_model"])
    max_specs = args.max_specs if args.max_specs is not None else int(config["max_specs"])
    input_path = ROOT / str(config["input_specs_path"])
    if not input_path.exists():
        raise SystemExit(
            f"Checked scene specs not found: {input_path}\n"
            "Run scripts/01_generate_scene_specs.py, scripts/02_check_scene_specs.py, "
            "and scripts/03_expand_cosmos_prompts.py first."
        )

    specs = []
    with input_path.open("r", encoding="utf-8") as handle:
        for line in handle:
            stripped = line.strip()
            if stripped:
                specs.append(json.loads(stripped))
            if len(specs) >= max_specs:
                break

    client = OllamaClient(
        base_url=str(config["ollama_base_url"]),
        timeout_seconds=int(config["timeout_seconds"]),
    )
    options = {
        "temperature": float(config["temperature"]),
        "num_ctx": int(config["num_ctx"]),
    }
    rows: list[dict[str, Any]] = []
    for spec in specs:
        spec_id = str(spec["spec_id"])
        try:
            raw_text = client.chat(model=model_id, messages=_build_messages(spec, model_id), options=options)
            row = _parse_response(raw_text, spec_id, model_id)
        except (OllamaClientError, json.JSONDecodeError) as exc:
            row = _error_row(spec_id, model_id, f"request_error: {exc}")

        schema_errors = validate_enrichment_row(row)
        leakage_errors = check_forbidden_label_leakage(row)
        if schema_errors or leakage_errors:
            notes = _notes(row)
            if schema_errors:
                notes.append("schema_error: normalized_row_failed_validation")
            if leakage_errors:
                notes.append("leakage_error: output_text_contains_forbidden_label_wording")
            row["notes"] = notes
            for field in REQUIRED_FIELDS - set(row):
                row[field] = [] if field == "notes" else ""
        rows.append(row)

    output_rel = str(config["output_path_template"]).format(model_id=_model_id_for_path(model_id))
    output_path = ROOT / output_rel
    write_jsonl(output_path, rows)
    print(f"Wrote {len(rows)} enrichment preview rows to {output_rel}")
    print("No source specs were modified.")


if __name__ == "__main__":
    main()
