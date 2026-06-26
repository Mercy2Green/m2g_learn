from __future__ import annotations

import csv
import json
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path
from typing import Any

from .evaluator import FAILURE_TAXONOMY


def append_jsonl(path: str | Path, record: dict[str, Any]) -> None:
    with Path(path).open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(record, ensure_ascii=False) + "\n")


def write_evaluation_csv(path: str | Path, evaluations: list[dict[str, Any]]) -> None:
    fieldnames = [
        "task_id",
        "task_name",
        "image_path",
        "model_id",
        "provider",
        "provider_label",
        "model_name",
        "strength_role",
        "prompt_id",
        "prompt_type",
        "primary_for_counterexample",
        "pass_fail",
        "failure_types_detected",
        "counterexample_strength_hint",
        "inferred_uses_helper",
        "inferred_searches_helper",
        "inferred_one_by_one",
        "plan_summary",
        "notes",
    ]
    with Path(path).open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        for row in evaluations:
            output = dict(row)
            output["failure_types_detected"] = ";".join(output.get("failure_types_detected", []))
            writer.writerow({key: output.get(key, "") for key in fieldnames})


def write_reports(
    output_dir: str | Path,
    tasks: list[dict[str, Any]],
    models: list[dict[str, Any]],
    prompts: list[dict[str, Any]],
    evaluations: list[dict[str, Any]],
    parsed_records: list[dict[str, Any]],
    raw_path: str,
    parsed_path: str,
) -> None:
    output = Path(output_dir)
    write_summary(output / "summary.md", tasks, models, prompts, evaluations, raw_path, parsed_path)
    write_failed_cases(output / "failed_cases.md", tasks, evaluations, parsed_records)


def write_summary(
    path: str | Path,
    tasks: list[dict[str, Any]],
    models: list[dict[str, Any]],
    prompts: list[dict[str, Any]],
    evaluations: list[dict[str, Any]],
    raw_path: str,
    parsed_path: str,
) -> None:
    primary_rows = [row for row in evaluations if row.get("primary_for_counterexample") is True]
    probe_rows = [row for row in evaluations if row.get("primary_for_counterexample") is not True]
    counts = Counter(row.get("pass_fail", "") for row in evaluations)
    primary_counts = Counter(row.get("pass_fail", "") for row in primary_rows)
    probe_counts = Counter(row.get("pass_fail", "") for row in probe_rows)
    strength_counts = Counter(row.get("counterexample_strength_hint", "") for row in primary_rows)
    failure_counts = Counter()
    for row in primary_rows:
        failure_counts.update(row.get("failure_types_detected", []))

    lines: list[str] = [
        "# Tool-Aware Planning Counterexample Benchmark Summary",
        "",
        "## Run metadata",
        f"- Generated at: {datetime.now().isoformat(timespec='seconds')}",
        f"- Tasks configured: {len(tasks)}",
        f"- Models tested: {', '.join(model.get('model_id', '') for model in models)}",
        f"- Prompt settings: {', '.join(prompt.get('prompt_id', '') for prompt in prompts)}",
        f"- Total evaluated rows: {len(evaluations)}",
        "- Structured probe is diagnostic only and is not clean main counterexample evidence.",
        "",
        "## Provider and model information",
        "| Model | Provider | Provider label | Model name | Strength role |",
        "| --- | --- | --- | --- | --- |",
    ]
    for model in models:
        lines.append(
            f"| {model.get('model_id', '')} | {model.get('provider', '')} | {model.get('provider_label', '')} | "
            f"{model.get('model_name', '')} | {model.get('strength_role', '')} |"
        )

    lines.extend(["", "## Prompt type", "| Prompt | Type | Primary | Description |", "| --- | --- | --- | --- |"])
    for prompt in prompts:
        prompt_type = "primary clean prompt" if prompt.get("primary_for_counterexample") else "structured probe"
        description = str(prompt.get("description", "")).replace("|", "\\|")
        lines.append(f"| {prompt.get('prompt_id', '')} | {prompt_type} | {prompt.get('primary_for_counterexample', False)} | {description} |")

    lines.extend(["", "## Overall pass/fail summary", "| Scope | Pass | Fail | Review | Parse error | Skipped |", "| --- | ---: | ---: | ---: | ---: | ---: |"])
    lines.append(_status_row("all", counts))
    lines.append(_status_row("primary_clean", primary_counts))
    lines.append(_status_row("structured_probe", probe_counts))

    lines.extend(["", "## Clean counterexample strength hints", "| Hint | Count |", "| --- | ---: |"])
    for hint in ["strong_candidate", "medium_candidate", "weak_candidate", "invalid_or_unclear"]:
        lines.append(f"| {hint} | {strength_counts.get(hint, 0)} |")

    lines.extend(["", "## Primary clean failure type counts", "| Failure type | Count | Description |", "| --- | ---: | --- |"])
    if failure_counts:
        for failure, count in failure_counts.most_common():
            lines.append(f"| {failure} | {count} | {FAILURE_TAXONOMY.get(failure, '')} |")
    else:
        lines.append("| - | 0 | - |")

    for title, hint in [
        ("Strong clean candidate counterexamples", "strong_candidate"),
        ("Medium clean candidate counterexamples", "medium_candidate"),
        ("Weak clean candidate counterexamples", "weak_candidate"),
    ]:
        lines.extend(["", f"## {title}", "| Task | Image | Model | Prompt | Status | Failures | Plan summary | Notes |", "| --- | --- | --- | --- | --- | --- | --- | --- |"])
        subset = [row for row in primary_rows if row.get("counterexample_strength_hint") == hint]
        if not subset:
            lines.append("| - | - | - | - | - | - | - | - |")
        for row in subset[:50]:
            lines.append(_eval_table_row(row))

    lines.extend(["", "## Cases needing manual review", "| Task | Image | Model | Prompt | Type | Status | Notes |", "| --- | --- | --- | --- | --- | --- | --- |"])
    review_rows = [row for row in evaluations if row.get("pass_fail") in {"needs_review", "parse_error", "skipped"}]
    if not review_rows:
        lines.append("| - | - | - | - | - | - | - |")
    for row in review_rows[:80]:
        notes = str(row.get("notes", "")).replace("|", "\\|")
        lines.append(
            f"| {row.get('task_id')} | {Path(str(row.get('image_path', ''))).name} | {row.get('model_id')} | "
            f"{row.get('prompt_id')} | {row.get('prompt_type')} | {row.get('pass_fail')} | {notes} |"
        )

    lines.extend(["", "## Structured probe results", "| Task | Image | Model | Prompt | Status | Failures | Plan summary | Notes |", "| --- | --- | --- | --- | --- | --- | --- | --- |"])
    if not probe_rows:
        lines.append("| - | - | - | - | - | - | - | - |")
    for row in probe_rows[:80]:
        lines.append(_eval_table_row(row))

    lines.extend(["", "## Per-task table", "| Task | Pass | Fail | Review | Parse error | Skipped |", "| --- | ---: | ---: | ---: | ---: | ---: |"])
    for task_id, rows in _group_by(evaluations, "task_id").items():
        lines.append(_status_row(task_id, Counter(row.get("pass_fail", "") for row in rows)))

    lines.extend(["", "## Per-model table", "| Model | Provider label | Strength role | Pass | Fail | Review | Parse error | Skipped |", "| --- | --- | --- | ---: | ---: | ---: | ---: | ---: |"])
    for model_id, rows in _group_by(evaluations, "model_id").items():
        counter = Counter(row.get("pass_fail", "") for row in rows)
        provider_label = rows[0].get("provider_label", "") if rows else ""
        strength_role = rows[0].get("strength_role", "") if rows else ""
        lines.append(
            f"| {model_id} | {provider_label} | {strength_role} | {counter.get('pass', 0)} | {counter.get('fail', 0)} | "
            f"{counter.get('needs_review', 0)} | {counter.get('parse_error', 0)} | {counter.get('skipped', 0)} |"
        )

    lines.extend(
        [
            "",
            "## Raw output files",
            f"- Raw responses JSONL: `{raw_path}`",
            f"- Parsed results JSONL: `{parsed_path}`",
            "- Evaluation CSV: `evaluation.csv`",
            "- Failed cases: `failed_cases.md`",
        ]
    )
    Path(path).write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_failed_cases(
    path: str | Path,
    tasks: list[dict[str, Any]],
    evaluations: list[dict[str, Any]],
    parsed_records: list[dict[str, Any]],
) -> None:
    task_map = {task.get("task_id", ""): task for task in tasks}
    parsed_by_key = {
        (record.get("task_id"), record.get("image_path"), record.get("model_id"), record.get("prompt_id")): record
        for record in parsed_records
    }
    failed = [row for row in evaluations if row.get("pass_fail") in {"fail", "needs_review", "parse_error", "skipped"}]
    grouped = _group_by(failed, "task_id")
    lines = ["# Failed and Review Cases", "", "Heuristic labels are an automatic first pass. Review raw plans before using a case as paper evidence.", ""]
    if not grouped:
        lines.append("No failed or review cases.")
    for task_id, rows in grouped.items():
        task = task_map.get(task_id, {})
        lines.extend(
            [
                f"## {task_id}_{task.get('name', '')}",
                "",
                "### Expected",
                _expected_summary(task),
                "",
                "### Model outputs",
            ]
        )
        for row in rows:
            key = (row.get("task_id"), row.get("image_path"), row.get("model_id"), row.get("prompt_id"))
            parsed = parsed_by_key.get(key, {}).get("parsed", {})
            plan = "; ".join(parsed.get("plan", [])) if parsed else row.get("notes", "")
            failures = ", ".join(row.get("failure_types_detected", [])) or "-"
            lines.append(
                f"- {row.get('model_id')} / {row.get('prompt_id')} / {row.get('prompt_type')}: "
                f"{row.get('pass_fail').upper()} - {failures}. {row.get('notes', '')} "
                f"Inference: helper={row.get('inferred_uses_helper')}, search={row.get('inferred_searches_helper')}, "
                f"one_by_one={row.get('inferred_one_by_one')}. Plan: {plan}"
            )
        lines.extend(["", "### Failure types", ", ".join(sorted({f for row in rows for f in row.get("failure_types_detected", [])})) or "-", ""])
    Path(path).write_text("\n".join(lines) + "\n", encoding="utf-8")


def _status_row(scope: str, counter: Counter[str]) -> str:
    return (
        f"| {scope} | {counter.get('pass', 0)} | {counter.get('fail', 0)} | "
        f"{counter.get('needs_review', 0)} | {counter.get('parse_error', 0)} | {counter.get('skipped', 0)} |"
    )


def _eval_table_row(row: dict[str, Any]) -> str:
    failures = ", ".join(row.get("failure_types_detected", [])) or "-"
    notes = str(row.get("notes", "")).replace("|", "\\|")
    plan = str(row.get("plan_summary", "")).replace("|", "\\|")
    return (
        f"| {row.get('task_id')} | {Path(str(row.get('image_path', ''))).name} | {row.get('model_id')} | "
        f"{row.get('prompt_id')} | {row.get('pass_fail')} | {failures} | {plan} | {notes} |"
    )


def _group_by(rows: list[dict[str, Any]], key: str) -> dict[str, list[dict[str, Any]]]:
    grouped: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in rows:
        grouped[str(row.get(key, ""))].append(row)
    return dict(grouped)


def _expected_summary(task: dict[str, Any]) -> str:
    expected = task.get("expected_behavior", {})
    return (
        f"- should_use_tool_or_container: {expected.get('should_use_tool_or_container')}\n"
        f"- expected_tool_or_container_types: {expected.get('expected_tool_or_container_types')}\n"
        f"- should_search_for_tool_if_not_visible: {expected.get('should_search_for_tool_if_not_visible')}\n"
        f"- expected_trip_pattern: {expected.get('expected_trip_pattern')}"
    )
