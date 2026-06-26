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
        "prompt_id",
        "pass_fail",
        "failure_types_detected",
        "counterexample_strength_hint",
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
    counts = Counter(row.get("pass_fail", "") for row in evaluations)
    failure_counts = Counter()
    strength_counts = Counter(row.get("counterexample_strength_hint", "") for row in evaluations)
    for row in evaluations:
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
        "",
        "## Overall pass/fail summary",
        "| Status | Count |",
        "| --- | ---: |",
    ]
    for status in ["pass", "fail", "needs_review", "parse_error", "skipped"]:
        lines.append(f"| {status} | {counts.get(status, 0)} |")

    lines.extend(["", "## Counterexample strength hints", "| Hint | Count |", "| --- | ---: |"])
    for hint in ["strong_candidate", "medium_candidate", "weak_candidate", "invalid_or_unclear"]:
        lines.append(f"| {hint} | {strength_counts.get(hint, 0)} |")

    lines.extend(["", "## Failure type counts", "| Failure type | Count | Description |", "| --- | ---: | --- |"])
    for failure, count in failure_counts.most_common():
        lines.append(f"| {failure} | {count} | {FAILURE_TAXONOMY.get(failure, '')} |")

    for title, hint in [
        ("Strong candidate counterexamples", "strong_candidate"),
        ("Medium candidate counterexamples", "medium_candidate"),
        ("Cases needing manual review", "invalid_or_unclear"),
    ]:
        lines.extend(["", f"## {title}", "| Task | Image | Model | Prompt | Status | Failures | Notes |", "| --- | --- | --- | --- | --- | --- | --- |"])
        subset = [row for row in evaluations if row.get("counterexample_strength_hint") == hint]
        if title == "Cases needing manual review":
            subset = [row for row in evaluations if row.get("pass_fail") in {"needs_review", "parse_error", "skipped"}]
        if not subset:
            lines.append("| - | - | - | - | - | - | - |")
        for row in subset[:50]:
            lines.append(_eval_table_row(row))

    lines.extend(["", "## Per-task table", "| Task | Pass | Fail | Review | Parse error | Skipped |", "| --- | ---: | ---: | ---: | ---: | ---: |"])
    for task_id, rows in _group_by(evaluations, "task_id").items():
        counter = Counter(row.get("pass_fail", "") for row in rows)
        lines.append(
            f"| {task_id} | {counter.get('pass', 0)} | {counter.get('fail', 0)} | "
            f"{counter.get('needs_review', 0)} | {counter.get('parse_error', 0)} | {counter.get('skipped', 0)} |"
        )

    lines.extend(["", "## Per-model table", "| Model | Provider | Pass | Fail | Review | Parse error | Skipped |", "| --- | --- | ---: | ---: | ---: | ---: | ---: |"])
    for model_id, rows in _group_by(evaluations, "model_id").items():
        counter = Counter(row.get("pass_fail", "") for row in rows)
        provider = rows[0].get("provider", "") if rows else ""
        lines.append(
            f"| {model_id} | {provider} | {counter.get('pass', 0)} | {counter.get('fail', 0)} | "
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
    lines = ["# Failed and Review Cases", ""]
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
                f"- {row.get('model_id')} / {row.get('prompt_id')}: {row.get('pass_fail').upper()} "
                f"- {failures}. {row.get('notes', '')} Plan: {plan}"
            )
        lines.extend(["", "### Failure types", ", ".join(sorted({f for row in rows for f in row.get("failure_types_detected", [])})) or "-", ""])
    Path(path).write_text("\n".join(lines) + "\n", encoding="utf-8")


def _eval_table_row(row: dict[str, Any]) -> str:
    failures = ", ".join(row.get("failure_types_detected", [])) or "-"
    notes = str(row.get("notes", "")).replace("|", "\\|")
    return (
        f"| {row.get('task_id')} | {Path(str(row.get('image_path', ''))).name} | {row.get('model_id')} | "
        f"{row.get('prompt_id')} | {row.get('pass_fail')} | {failures} | {notes} |"
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
