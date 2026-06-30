from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

if __package__ is None or __package__ == "":
    sys.path.insert(0, str(Path(__file__).resolve().parent))

from common import (  # noqa: E402
    compact_text,
    flatten_parsed_fields,
    infer_model_from_dirname,
    infer_run_category_from_dirname,
    join_key,
    normalize_list_field,
    output_dir_to_run_id,
    read_csv_dicts,
    read_jsonl,
    safe_load_yaml,
    write_csv_dicts,
    write_jsonl,
)


DEFAULT_OUTPUT_DIRS = [
    "outputs/ollama_multi_20260629_232329_generic_clean_ollama_qwen3_5_35b",
    "outputs/ollama_multi_20260629_232329_generic_clean_ollama_qwen3_vl_32b_instruct_q4_K_M",
    "outputs/ollama_multi_20260630_105118_tool_prior_intervention_ollama_qwen3_vl_30b_a3b_instruct_q4_K_M",
    "outputs/ollama_multi_20260630_082623_diagnostic_probes_ollama_minicpm_v4_5_q8_0",
]

CSV_FIELDNAMES = [
    "run_id",
    "output_dir",
    "inferred_run_category",
    "inferred_model_id",
    "task_id",
    "task_name",
    "image_path",
    "image_name",
    "model_id",
    "model_name",
    "provider",
    "provider_label",
    "strength_role",
    "supports_vision",
    "prompt_id",
    "prompt_category",
    "prompt_type",
    "embodiment_profile",
    "primary_for_counterexample",
    "auto_pass_fail",
    "auto_failure_types",
    "auto_counterexample_strength_hint",
    "auto_notes",
    "auto_plan_summary",
    "parsed_plan",
    "parsed_reason",
    "parsed_efficiency_consideration",
    "parsed_safety_or_stability_consideration",
    "parsed_uncertainty_or_missing_information",
    "parsed_selected_helper",
    "parsed_tool_use_action_chain",
    "parse_status",
    "parse_error",
    "expected_should_use_tool_or_container",
    "expected_tool_or_container_types",
    "expected_should_search_for_tool_if_not_visible",
    "expected_should_avoid_over_tool_use",
    "expected_trip_pattern",
    "target_object_terms",
    "prompt_eval_count",
    "eval_count",
    "num_ctx",
    "system_prompt_chars",
    "user_prompt_chars",
    "raw_response_chars",
    "parsed_plan_chars",
    "raw_response_short",
]


def main() -> None:
    args = parse_args()
    root_dir = Path(__file__).resolve().parents[2]
    output_dirs = [Path(item) for item in (args.output_dirs or DEFAULT_OUTPUT_DIRS)]
    output_dir = Path(args.output_dir)
    if not output_dir.is_absolute():
        output_dir = root_dir / output_dir
    output_dir.mkdir(parents=True, exist_ok=True)

    all_rows: list[dict[str, Any]] = []
    manifest: list[dict[str, Any]] = []
    integrity_lines = ["# Data Integrity Report", ""]

    for raw_output_dir in output_dirs:
        run_dir = raw_output_dir if raw_output_dir.is_absolute() else root_dir / raw_output_dir
        run_result = process_run_dir(run_dir, root_dir)
        manifest.append(run_result["manifest"])
        integrity_lines.extend(run_result["integrity_lines"])
        all_rows.extend(run_result["rows"])

    if not all_rows and not args.allow_missing:
        integrity_lines.append("")
        integrity_lines.append("No rows were loaded from the selected output directories.")
        (output_dir / "data_integrity_report.md").write_text("\n".join(integrity_lines) + "\n", encoding="utf-8")
        raise SystemExit("No rows loaded. Use --allow_missing to ignore missing directories.")

    write_csv_dicts(output_dir / "all_runs_manifest.csv", manifest, manifest_fieldnames())
    write_csv_dicts(output_dir / "all_rows_merged.csv", all_rows, CSV_FIELDNAMES)
    write_jsonl(output_dir / "all_rows_merged.jsonl", all_rows)
    (output_dir / "data_integrity_report.md").write_text("\n".join(integrity_lines) + "\n", encoding="utf-8")

    print(json.dumps({"output_dir": str(output_dir), "runs": len(manifest), "rows": len(all_rows)}, ensure_ascii=False))


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build unified row-level index from benchmark output directories.")
    parser.add_argument("--output_dirs", nargs="*", default=None)
    parser.add_argument("--output_dir", default="analysis_review/round01_small_subset")
    parser.add_argument("--allow_missing", action="store_true")
    return parser.parse_args()


def process_run_dir(run_dir: Path, root_dir: Path) -> dict[str, Any]:
    run_id = output_dir_to_run_id(run_dir)
    inferred_category = infer_run_category_from_dirname(run_dir.name)
    inferred_model_id = infer_model_from_dirname(run_dir.name)
    required_files = ["evaluation.csv", "parsed_results.jsonl", "raw_responses.jsonl"]
    issues: list[str] = []
    integrity_lines = [f"## {run_id}", "", f"- Path: `{run_dir}`"]

    if not run_dir.exists():
        issues.append("output directory missing")
    else:
        for filename in required_files:
            if not (run_dir / filename).exists():
                issues.append(f"missing {filename}")
        if not (run_dir / "config_snapshot").exists():
            issues.append("missing config_snapshot/")

    if issues:
        integrity_lines.append(f"- Status: incomplete ({'; '.join(issues)})")
        integrity_lines.append("")
        return {
            "manifest": manifest_row(run_dir, run_id, inferred_category, inferred_model_id, "incomplete", issues, 0, 0, 0, 0),
            "integrity_lines": integrity_lines,
            "rows": [],
        }

    eval_rows = read_csv_dicts(run_dir / "evaluation.csv")
    parsed_rows = read_jsonl(run_dir / "parsed_results.jsonl")
    raw_rows = read_jsonl(run_dir / "raw_responses.jsonl")
    parsed_by_key = {join_key(row): row for row in parsed_rows}
    raw_by_key = {join_key(row): row for row in raw_rows}
    snapshot = load_config_snapshot(run_dir / "config_snapshot")

    merged_rows = []
    missing_parsed = 0
    missing_raw = 0
    for eval_row in eval_rows:
        key = join_key(eval_row)
        parsed_record = parsed_by_key.get(key, {})
        raw_record = raw_by_key.get(key, {})
        if not parsed_record:
            missing_parsed += 1
        if not raw_record:
            missing_raw += 1
        merged_rows.append(
            merge_row(
                run_dir=run_dir,
                root_dir=root_dir,
                run_id=run_id,
                inferred_category=inferred_category,
                inferred_model_id=inferred_model_id,
                eval_row=eval_row,
                parsed_record=parsed_record,
                raw_record=raw_record,
                snapshot=snapshot,
            )
        )

    status = "ok"
    if missing_parsed or missing_raw:
        status = "partial_join"
        issues.append(f"missing parsed join rows: {missing_parsed}")
        issues.append(f"missing raw join rows: {missing_raw}")

    integrity_lines.extend(
        [
            f"- Status: {status}",
            f"- evaluation.csv rows: {len(eval_rows)}",
            f"- parsed_results.jsonl rows: {len(parsed_rows)}",
            f"- raw_responses.jsonl rows: {len(raw_rows)}",
            f"- merged rows: {len(merged_rows)}",
            f"- missing parsed joins: {missing_parsed}",
            f"- missing raw joins: {missing_raw}",
            f"- snapshot tasks: {len(snapshot['tasks'])}",
            f"- snapshot prompts: {len(snapshot['prompts'])}",
            f"- snapshot models: {len(snapshot['models'])}",
            "",
        ]
    )
    return {
        "manifest": manifest_row(
            run_dir, run_id, inferred_category, inferred_model_id, status, issues, len(eval_rows), len(parsed_rows), len(raw_rows), len(merged_rows)
        ),
        "integrity_lines": integrity_lines,
        "rows": merged_rows,
    }


def load_config_snapshot(snapshot_dir: Path) -> dict[str, dict[str, dict[str, Any]]]:
    tasks: dict[str, dict[str, Any]] = {}
    prompts: dict[str, dict[str, Any]] = {}
    models: dict[str, dict[str, Any]] = {}
    for path in snapshot_dir.rglob("*.yaml"):
        data = safe_load_yaml(path)
        if "tasks" in data:
            tasks.update({str(item.get("task_id", "")): item for item in data.get("tasks", []) if item.get("task_id")})
        if "prompts" in data:
            prompts.update({str(item.get("prompt_id", "")): item for item in data.get("prompts", []) if item.get("prompt_id")})
        if "models" in data:
            models.update({str(item.get("model_id", "")): item for item in data.get("models", []) if item.get("model_id")})
    return {"tasks": tasks, "prompts": prompts, "models": models}


def merge_row(
    run_dir: Path,
    root_dir: Path,
    run_id: str,
    inferred_category: str,
    inferred_model_id: str,
    eval_row: dict[str, Any],
    parsed_record: dict[str, Any],
    raw_record: dict[str, Any],
    snapshot: dict[str, dict[str, dict[str, Any]]],
) -> dict[str, Any]:
    task = snapshot["tasks"].get(str(eval_row.get("task_id", "")), {})
    prompt = snapshot["prompts"].get(str(eval_row.get("prompt_id", "")), {})
    model = snapshot["models"].get(str(eval_row.get("model_id", "")), {})
    expected = task.get("expected_behavior", {}) if isinstance(task.get("expected_behavior", {}), dict) else {}
    parsed = parsed_record.get("parsed", {}) if isinstance(parsed_record.get("parsed", {}), dict) else {}
    raw_metadata = raw_record.get("metadata", {}) if isinstance(raw_record.get("metadata", {}), dict) else {}
    parsed_flat = flatten_parsed_fields(parsed)
    raw_response = str(raw_record.get("raw_response", parsed_record.get("raw_response", "")) or "")
    system_prompt = str(raw_record.get("system_prompt", prompt.get("system_prompt", "")) or "")
    user_prompt = str(raw_record.get("user_prompt", "") or "")
    image_path = str(eval_row.get("image_path", "") or parsed_record.get("image_path", "") or raw_record.get("image_path", ""))

    merged: dict[str, Any] = {
        "run_id": run_id,
        "output_dir": str(run_dir.relative_to(root_dir) if run_dir.is_relative_to(root_dir) else run_dir),
        "inferred_run_category": inferred_category,
        "inferred_model_id": inferred_model_id,
        "task_id": eval_row.get("task_id", ""),
        "task_name": eval_row.get("task_name") or task.get("name", ""),
        "task_instruction": task.get("instruction", ""),
        "image_path": image_path,
        "image_name": Path(image_path).name if image_path else "",
        "model_id": eval_row.get("model_id", ""),
        "model_name": eval_row.get("model_name") or model.get("model_name", ""),
        "provider": eval_row.get("provider") or model.get("provider", ""),
        "provider_label": eval_row.get("provider_label") or model.get("provider_label", ""),
        "strength_role": eval_row.get("strength_role") or model.get("strength_role", ""),
        "supports_vision": eval_row.get("supports_vision") or model.get("supports_vision", ""),
        "prompt_id": eval_row.get("prompt_id", ""),
        "prompt_category": eval_row.get("prompt_category") or prompt.get("prompt_category", ""),
        "prompt_type": eval_row.get("prompt_type") or raw_record.get("prompt_type", ""),
        "embodiment_profile": eval_row.get("embodiment_profile") or prompt.get("embodiment_profile", ""),
        "primary_for_counterexample": eval_row.get("primary_for_counterexample") or prompt.get("primary_for_counterexample", ""),
        "auto_pass_fail": eval_row.get("pass_fail", ""),
        "auto_failure_types": eval_row.get("failure_types_detected", ""),
        "auto_counterexample_strength_hint": eval_row.get("counterexample_strength_hint", ""),
        "auto_notes": eval_row.get("notes", ""),
        "auto_plan_summary": eval_row.get("plan_summary", ""),
        "parse_status": parsed_record.get("parse_status", ""),
        "parse_error": parsed_record.get("parse_error", ""),
        "expected_behavior": expected,
        "expected_should_use_tool_or_container": expected.get("should_use_tool_or_container", ""),
        "expected_tool_or_container_types": normalize_list_field(expected.get("expected_tool_or_container_types")),
        "expected_should_search_for_tool_if_not_visible": expected.get("should_search_for_tool_if_not_visible", ""),
        "expected_should_avoid_over_tool_use": expected.get("should_avoid_over_tool_use", ""),
        "expected_trip_pattern": expected.get("expected_trip_pattern", ""),
        "target_object_terms": normalize_list_field(expected.get("target_object_terms")),
        "system_prompt": system_prompt,
        "user_prompt": user_prompt,
        "prompt_eval_count": raw_metadata.get("prompt_eval_count", ""),
        "eval_count": raw_metadata.get("eval_count", ""),
        "num_ctx": raw_metadata.get("num_ctx", ""),
        "ollama_done": raw_metadata.get("ollama_done", ""),
        "provider_metadata": raw_metadata,
        "system_prompt_chars": len(system_prompt),
        "user_prompt_chars": len(user_prompt),
        "raw_response": raw_response,
        "raw_response_chars": len(raw_response),
        "raw_response_short": compact_text(raw_response, 500),
        "parsed": parsed,
    }
    merged.update(parsed_flat)
    merged["parsed_plan_chars"] = len(str(merged.get("parsed_plan", "")))
    return merged


def manifest_row(
    run_dir: Path,
    run_id: str,
    inferred_category: str,
    inferred_model_id: str,
    status: str,
    issues: list[str],
    evaluation_rows: int,
    parsed_rows: int,
    raw_rows: int,
    merged_rows: int,
) -> dict[str, Any]:
    return {
        "run_id": run_id,
        "output_dir": str(run_dir),
        "inferred_run_category": inferred_category,
        "inferred_model_id": inferred_model_id,
        "status": status,
        "issues": "; ".join(issues),
        "evaluation_rows": evaluation_rows,
        "parsed_rows": parsed_rows,
        "raw_rows": raw_rows,
        "merged_rows": merged_rows,
    }


def manifest_fieldnames() -> list[str]:
    return [
        "run_id",
        "output_dir",
        "inferred_run_category",
        "inferred_model_id",
        "status",
        "issues",
        "evaluation_rows",
        "parsed_rows",
        "raw_rows",
        "merged_rows",
    ]


if __name__ == "__main__":
    main()
