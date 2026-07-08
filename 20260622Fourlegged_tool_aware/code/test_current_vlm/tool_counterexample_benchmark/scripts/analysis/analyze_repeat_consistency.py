from __future__ import annotations

import argparse
import csv
import hashlib
import json
import math
import re
from collections import Counter, defaultdict
from pathlib import Path
from statistics import pstdev
from typing import Any, Iterable


GROUP_KEY = ("model_id", "task_id", "image_name", "prompt_id")
CONSISTENCY_TYPES = [
    "stable_all_pass",
    "stable_all_fail",
    "stable_all_parse",
    "stable_nonparse_pass_with_parse",
    "stable_nonparse_fail_with_parse",
    "mixed_pass_fail_no_parse",
    "mixed_pass_fail_with_parse",
    "uncertain_or_other",
]
IMPORTANT_FAILURE_TASKS = {"task_002", "task_008", "task_001", "task_005"}
IMPORTANT_SUCCESS_TASKS = {"task_006", "task_007", "task_011", "task_003"}


def main() -> None:
    args = parse_args()
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    vlm_rows = read_table(Path(args.vlm_case_csv))
    warnings: list[str] = []
    group_rows = build_group_rows(vlm_rows, args.expected_repeats, warnings)
    write_csv(output_dir / "repeat_consistency_by_task_prompt.csv", group_rows, task_prompt_fields())

    task_rows = summarize_by_task(group_rows)
    write_csv(output_dir / "repeat_consistency_by_task.csv", task_rows, task_summary_fields())

    prompt_rows = summarize_by_prompt(group_rows)
    write_csv(output_dir / "repeat_consistency_by_prompt.csv", prompt_rows, prompt_summary_fields())

    write_summary(output_dir / "repeat_consistency_summary.md", group_rows, task_rows, prompt_rows, len(vlm_rows), args.expected_repeats, warnings)
    write_top_unstable(output_dir / "top_unstable_task_prompt_groups.md", group_rows)
    write_stable_groups(output_dir / "stable_failure_groups.md", group_rows, success=False)
    write_stable_groups(output_dir / "stable_success_groups.md", group_rows, success=True)
    write_task002(output_dir / "task002_repeat_consistency.md", vlm_rows, group_rows, args.expected_repeats)
    write_task005(output_dir / "task005_repeat_consistency.md", vlm_rows, group_rows, args.expected_repeats)

    if args.merged_rows and Path(args.merged_rows).exists():
        audit_rows = build_input_integrity_rows(read_table(Path(args.merged_rows)), args.expected_repeats, warnings)
        write_csv(output_dir / "repeat_input_integrity_audit.csv", audit_rows, input_audit_fields())
        write_input_integrity_md(output_dir / "repeat_input_integrity_audit.md", audit_rows)
        append_input_integrity_to_summary(output_dir / "repeat_consistency_summary.md", audit_rows)
    else:
        warnings.append(f"merged rows not found, skipped input integrity audit: {args.merged_rows}")

    if args.text_case and Path(args.text_case).exists():
        text_rows = read_table(Path(args.text_case))
        comparison_rows = build_vlm_text_comparison(group_rows, text_rows, args.expected_repeats, warnings)
        write_csv(output_dir / "repeat_consistency_vlm_vs_text_comparison.csv", comparison_rows, vlm_text_fields())
        write_vlm_text_md(output_dir / "repeat_consistency_vlm_vs_text_comparison.md", comparison_rows)
    else:
        warnings.append(f"text rereview not found, skipped VLM/text comparison: {args.text_case}")

    if warnings:
        (output_dir / "repeat_consistency_warnings.md").write_text(
            "# Repeat Consistency Warnings\n\n" + "\n".join(f"- {item}" for item in warnings) + "\n",
            encoding="utf-8",
        )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Analyze repeat consistency for repeated benchmark judge outputs.")
    parser.add_argument("--vlm_case_csv", required=True)
    parser.add_argument("--text_case", default="")
    parser.add_argument("--merged_rows", default="")
    parser.add_argument("--output_dir", required=True)
    parser.add_argument("--expected_repeats", type=int, default=10)
    return parser.parse_args()


def read_table(path: Path) -> list[dict[str, Any]]:
    if not path.exists():
        raise SystemExit(f"Input not found: {path}")
    if path.suffix == ".jsonl":
        rows: list[dict[str, Any]] = []
        with path.open(encoding="utf-8") as handle:
            for line in handle:
                stripped = line.strip()
                if stripped:
                    rows.append(json.loads(stripped))
        return rows
    with path.open(encoding="utf-8", newline="") as handle:
        return [dict(row) for row in csv.DictReader(handle)]


def write_csv(path: Path, rows: list[dict[str, Any]], fieldnames: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        for row in rows:
            writer.writerow({field: csv_value(row.get(field, "")) for field in fieldnames})


def csv_value(value: Any) -> str:
    if value is None:
        return ""
    if isinstance(value, (list, dict, tuple, bool)):
        return json.dumps(value, ensure_ascii=False)
    if isinstance(value, float):
        return f"{value:.6f}".rstrip("0").rstrip(".")
    return str(value)


def group_key(row: dict[str, Any]) -> tuple[str, str, str, str]:
    return tuple(str(row.get(field, "")) for field in GROUP_KEY)  # type: ignore[return-value]


def repeat_id_from_run(run_id: str, warnings: list[str]) -> str:
    match = re.match(r"^(repeat_\d+)(?:_|$)", run_id)
    if match:
        return match.group(1)
    warnings.append(f"Unexpected run_id format: {run_id}")
    return run_id or "missing_run_id"


def expected_repeat_ids(expected_repeats: int) -> list[str]:
    return [f"repeat_{index:02d}" for index in range(1, expected_repeats + 1)]


def normalize_label(row: dict[str, Any], label_field: str = "vlm_rereview_label") -> str:
    if str(row.get("judge_parse_error", "") or "").strip():
        return "judge_parse_error"
    label = str(row.get(label_field, "") or "").strip().lower()
    if label in {"true_pass", "pass"}:
        return "true_pass"
    if label in {"true_fail", "fail"}:
        return "true_fail"
    if label in {"parse_error", "tested_model_parse_error"}:
        return "parse_error"
    if label in {"uncertain", "needs_visual_check", "needs_review"}:
        return "uncertain"
    return "uncertain"


def helper_value(row: dict[str, Any]) -> str:
    value = str(row.get("valid_helper_action_chain", "") or "").strip().lower()
    if value in {"yes", "true", "1"}:
        return "yes"
    if value in {"no", "false", "0"}:
        return "no"
    return "uncertain"


def build_group_rows(rows: list[dict[str, Any]], expected_repeats: int, warnings: list[str]) -> list[dict[str, Any]]:
    grouped: dict[tuple[str, str, str, str], list[dict[str, Any]]] = defaultdict(list)
    for row in rows:
        grouped[group_key(row)].append(row)

    output: list[dict[str, Any]] = []
    expected_ids = expected_repeat_ids(expected_repeats)
    for key in sorted(grouped):
        items = grouped[key]
        repeat_pairs = [(repeat_id_from_run(str(row.get("run_id", "")), warnings), row) for row in items]
        repeat_counter = Counter(repeat_id for repeat_id, _ in repeat_pairs)
        ordered_pairs = sorted(repeat_pairs, key=lambda pair: repeat_sort_key(pair[0]))
        labels = [normalize_label(row) for _, row in ordered_pairs]
        helper_values = [helper_value(row) for _, row in ordered_pairs]
        label_counter = Counter(labels)
        helper_counter = Counter(helper_values)
        n_rows = len(items)
        true_pass = label_counter["true_pass"]
        true_fail = label_counter["true_fail"]
        parse_error = label_counter["parse_error"]
        judge_parse_error = label_counter["judge_parse_error"]
        uncertain = label_counter["uncertain"]
        non_parse = true_pass + true_fail + uncertain
        helper_yes_nonparse = sum(1 for (_, row), label in zip(ordered_pairs, labels) if label not in {"parse_error", "judge_parse_error"} and helper_value(row) == "yes")
        missing = [repeat_id for repeat_id in expected_ids if repeat_counter[repeat_id] == 0]
        duplicates = [repeat_id for repeat_id, count in sorted(repeat_counter.items()) if count > 1]

        row0 = ordered_pairs[0][1]
        consistency_type = classify_consistency(n_rows, expected_repeats, true_pass, true_fail, parse_error, judge_parse_error, uncertain)
        majority_label, majority_count = majority(labels)
        output.append(
            {
                "model_id": key[0],
                "task_id": key[1],
                "task_name": row0.get("task_name", ""),
                "image_name": key[2],
                "prompt_id": key[3],
                "prompt_category": row0.get("prompt_category", ""),
                "embodiment_profile": row0.get("embodiment_profile", ""),
                "n_rows": n_rows,
                "expected_repeats": expected_repeats,
                "observed_repeat_ids": " | ".join(repeat_id for repeat_id, _ in ordered_pairs),
                "missing_repeat_ids": " | ".join(missing),
                "duplicate_repeat_ids": " | ".join(duplicates),
                "data_integrity_status": data_integrity_status(n_rows, expected_repeats, missing, duplicates),
                "vlm_true_pass_count": true_pass,
                "vlm_true_fail_count": true_fail,
                "vlm_uncertain_count": uncertain,
                "tested_model_parse_error_count": parse_error,
                "judge_parse_error_count": judge_parse_error,
                "parse_error_count": parse_error + judge_parse_error,
                "non_parse_count": non_parse,
                "pass_rate_all": ratio(true_pass, n_rows),
                "fail_rate_all": ratio(true_fail, n_rows),
                "parse_rate_all": ratio(parse_error + judge_parse_error, n_rows),
                "pass_rate_non_parse": ratio(true_pass, non_parse),
                "fail_rate_non_parse": ratio(true_fail, non_parse),
                "helper_chain_yes_count": helper_counter["yes"],
                "helper_chain_no_count": helper_counter["no"],
                "helper_chain_uncertain_count": helper_counter["uncertain"],
                "helper_chain_yes_rate_all": ratio(helper_counter["yes"], n_rows),
                "helper_chain_yes_rate_non_parse": ratio(helper_yes_nonparse, non_parse),
                "label_sequence_by_repeat": " | ".join(f"{repeat_id}:{label}" for (repeat_id, _), label in zip(ordered_pairs, labels)),
                "helper_chain_sequence_by_repeat": " | ".join(f"{repeat_id}:{value}" for (repeat_id, _), value in zip(ordered_pairs, helper_values)),
                "evidence_quote_sequence_short": " | ".join(f"{repeat_id}:{short(row.get('evidence_quote', ''), 120)}" for repeat_id, row in ordered_pairs),
                "plan_sequence_short": " | ".join(f"{repeat_id}:{short(row.get('parsed_plan', ''), 160)}" for repeat_id, row in ordered_pairs),
                "consistency_type": consistency_type,
                "unique_label_count": len(set(labels)),
                "majority_label": majority_label,
                "majority_label_count": majority_count,
                "majority_label_rate": ratio(majority_count, n_rows),
                "volatility_score": 1 - ratio(majority_count, n_rows),
                "label_entropy": entropy(labels),
                "nonparse_flip": true_pass > 0 and true_fail > 0,
                "helper_chain_flip": helper_counter["yes"] > 0 and helper_counter["no"] > 0,
                "failure_modes_top": top_failure_modes(items),
            }
        )
    return output


def repeat_sort_key(repeat_id: str) -> tuple[int, str]:
    match = re.match(r"repeat_(\d+)$", repeat_id)
    if match:
        return int(match.group(1)), repeat_id
    return 9999, repeat_id


def data_integrity_status(n_rows: int, expected_repeats: int, missing: list[str], duplicates: list[str]) -> str:
    if duplicates:
        return "duplicate_repeats"
    if missing:
        return "missing_repeats"
    if n_rows != expected_repeats:
        return "unexpected_count"
    return "complete"


def classify_consistency(
    n_rows: int,
    expected_repeats: int,
    true_pass: int,
    true_fail: int,
    parse_error: int,
    judge_parse_error: int,
    uncertain: int,
) -> str:
    parse_total = parse_error + judge_parse_error
    if n_rows == expected_repeats and true_pass == expected_repeats:
        return "stable_all_pass"
    if n_rows == expected_repeats and true_fail == expected_repeats:
        return "stable_all_fail"
    if n_rows == expected_repeats and parse_error == expected_repeats:
        return "stable_all_parse"
    if true_fail == 0 and true_pass > 0 and parse_total > 0 and uncertain == 0:
        return "stable_nonparse_pass_with_parse"
    if true_pass == 0 and true_fail > 0 and parse_total > 0 and uncertain == 0:
        return "stable_nonparse_fail_with_parse"
    if true_pass > 0 and true_fail > 0 and parse_total == 0:
        return "mixed_pass_fail_no_parse"
    if true_pass > 0 and true_fail > 0 and parse_total > 0:
        return "mixed_pass_fail_with_parse"
    return "uncertain_or_other"


def ratio(num: int | float, den: int | float) -> float:
    if not den:
        return 0.0
    return float(num) / float(den)


def entropy(labels: list[str]) -> float:
    if not labels:
        return 0.0
    total = len(labels)
    value = 0.0
    for count in Counter(labels).values():
        p = count / total
        value -= p * math.log2(p)
    return value


def majority(labels: list[str]) -> tuple[str, int]:
    if not labels:
        return "", 0
    label, count = Counter(labels).most_common(1)[0]
    return label, count


def parse_jsonish_list(value: Any) -> list[str]:
    if value is None or value == "":
        return []
    if isinstance(value, list):
        return [str(item) for item in value]
    text = str(value).strip()
    if not text:
        return []
    try:
        parsed = json.loads(text)
        if isinstance(parsed, list):
            return [str(item) for item in parsed]
    except json.JSONDecodeError:
        pass
    if ";" in text:
        return [part.strip() for part in text.split(";") if part.strip()]
    if "," in text and not text.startswith("["):
        return [part.strip() for part in text.split(",") if part.strip()]
    return [text]


def top_failure_modes(rows: list[dict[str, Any]], limit: int = 5) -> str:
    counter: Counter[str] = Counter()
    for row in rows:
        counter.update(parse_jsonish_list(row.get("failure_modes", row.get("rereview_failure_modes", ""))))
    return " | ".join(f"{mode}:{count}" for mode, count in counter.most_common(limit))


def short(value: Any, max_chars: int) -> str:
    text = re.sub(r"\s+", " ", "" if value is None else str(value)).strip()
    if len(text) <= max_chars:
        return text
    return text[: max_chars - 3].rstrip() + "..."


def summarize_by_task(group_rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    by_task: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in group_rows:
        by_task[str(row["task_id"])].append(row)
    output = []
    for task_id in sorted(by_task):
        rows = by_task[task_id]
        output.append(summary_row(task_id, rows, "task"))
    return output


def summarize_by_prompt(group_rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    by_prompt: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in group_rows:
        by_prompt[str(row["prompt_id"])].append(row)
    output = []
    for prompt_id in sorted(by_prompt):
        rows = by_prompt[prompt_id]
        base = summary_row(prompt_id, rows, "prompt")
        base["prompt_category"] = rows[0].get("prompt_category", "")
        base["embodiment_profile"] = rows[0].get("embodiment_profile", "")
        output.append(base)
    return output


def summary_row(identifier: str, rows: list[dict[str, Any]], kind: str) -> dict[str, Any]:
    mixed_rows = [row for row in rows if boolish(row.get("nonparse_flip"))]
    parse_rows = [row for row in rows if intish(row.get("parse_error_count")) > 0]
    unstable_ids = [str(row["prompt_id" if kind == "task" else "task_id"]) for row in sorted(rows, key=unstable_sort_key)[:8] if is_unstable(row)]
    return {
        "task_id" if kind == "task" else "prompt_id": identifier,
        "total_prompt_groups" if kind == "task" else "total_task_groups": len(rows),
        "stable_all_pass_groups": count_type(rows, "stable_all_pass"),
        "stable_all_fail_groups": count_type(rows, "stable_all_fail"),
        "stable_all_parse_groups": count_type(rows, "stable_all_parse"),
        "mixed_pass_fail_groups": len(mixed_rows),
        "helper_chain_flip_groups": sum(1 for row in rows if boolish(row.get("helper_chain_flip"))),
        "groups_with_parse_error": len(parse_rows),
        "avg_pass_rate_non_parse": avg(row.get("pass_rate_non_parse") for row in rows),
        "avg_helper_chain_yes_rate_non_parse": avg(row.get("helper_chain_yes_rate_non_parse") for row in rows),
        "avg_volatility_score": avg(row.get("volatility_score") for row in rows),
        "max_volatility_score": max((floatish(row.get("volatility_score")) for row in rows), default=0.0),
        "representative_unstable_prompt_ids" if kind == "task" else "representative_unstable_task_ids": " | ".join(unstable_ids),
    }


def count_type(rows: list[dict[str, Any]], consistency_type: str) -> int:
    return sum(1 for row in rows if row.get("consistency_type") == consistency_type)


def avg(values: Iterable[Any]) -> float:
    nums = [floatish(value) for value in values]
    return sum(nums) / len(nums) if nums else 0.0


def floatish(value: Any) -> float:
    try:
        return float(value)
    except (TypeError, ValueError):
        return 0.0


def intish(value: Any) -> int:
    try:
        return int(value)
    except (TypeError, ValueError):
        return 0


def boolish(value: Any) -> bool:
    if isinstance(value, bool):
        return value
    return str(value).strip().lower() in {"true", "yes", "1"}


def is_unstable(row: dict[str, Any]) -> bool:
    return boolish(row.get("nonparse_flip")) or boolish(row.get("helper_chain_flip")) or floatish(row.get("volatility_score")) > 0


def unstable_sort_key(row: dict[str, Any]) -> tuple[int, int, float, float, str, str]:
    return (
        0 if boolish(row.get("nonparse_flip")) else 1,
        0 if boolish(row.get("helper_chain_flip")) else 1,
        -floatish(row.get("volatility_score")),
        -floatish(row.get("label_entropy")),
        str(row.get("task_id", "")),
        str(row.get("prompt_id", "")),
    )


def write_summary(
    path: Path,
    group_rows: list[dict[str, Any]],
    task_rows: list[dict[str, Any]],
    prompt_rows: list[dict[str, Any]],
    total_rows: int,
    expected_repeats: int,
    warnings: list[str],
) -> None:
    total_groups = len(group_rows)
    expected_groups = 11 * 18
    expected_rows = expected_groups * expected_repeats
    type_counts = Counter(str(row["consistency_type"]) for row in group_rows)
    complete_stable = type_counts["stable_all_pass"] + type_counts["stable_all_fail"] + type_counts["stable_all_parse"]
    pass_fail_flip = sum(1 for row in group_rows if boolish(row.get("nonparse_flip")))
    helper_flip = sum(1 for row in group_rows if boolish(row.get("helper_chain_flip")))
    parse_instability = sum(1 for row in group_rows if 0 < intish(row.get("parse_error_count")) < intish(row.get("n_rows")))
    integrity_counts = Counter(str(row["data_integrity_status"]) for row in group_rows)

    lines = [
        "# Repeat Consistency Summary",
        "",
        "## Data Scope",
        "",
        f"- Total groups: {total_groups}",
        f"- Expected groups: {expected_groups} (11 tasks x 18 prompts)",
        f"- Total rows: {total_rows}",
        f"- Expected rows: {expected_rows}",
        f"- Missing/duplicate repeat groups: {integrity_counts.get('missing_repeats', 0) + integrity_counts.get('duplicate_repeats', 0)}",
        "",
        "## Overall Consistency",
        "",
        "| consistency_type | groups | percent |",
        "| --- | ---: | ---: |",
    ]
    for item in CONSISTENCY_TYPES:
        count = type_counts[item]
        lines.append(f"| {item} | {count} | {ratio(count, total_groups):.1%} |")
    lines.extend(
        [
            "",
            "## Key Judgments",
            "",
            f"- Completely stable groups: {complete_stable}",
            f"- Groups with pass/fail flip: {pass_fail_flip}",
            f"- Groups with helper-chain yes/no flip: {helper_flip}",
            f"- Groups with parse instability: {parse_instability}",
            "",
            "## By Task",
            "",
            markdown_table(task_rows, task_summary_fields()),
            "",
            "## By Prompt",
            "",
            markdown_table(prompt_rows, prompt_summary_fields()),
        ]
    )
    if warnings:
        lines.extend(["", "## Warnings", "", *[f"- {item}" for item in warnings[:50]]])
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def markdown_table(rows: list[dict[str, Any]], fields: list[str], limit: int | None = None) -> str:
    selected = rows[:limit] if limit is not None else rows
    if not selected:
        return "_No rows._"
    lines = [
        "| " + " | ".join(fields) + " |",
        "| " + " | ".join("---" for _ in fields) + " |",
    ]
    for row in selected:
        lines.append("| " + " | ".join(escape_md(csv_value(row.get(field, ""))) for field in fields) + " |")
    return "\n".join(lines)


def escape_md(value: str) -> str:
    return value.replace("|", "\\|").replace("\n", " ")


def write_top_unstable(path: Path, group_rows: list[dict[str, Any]]) -> None:
    fields = [
        "task_id",
        "prompt_id",
        "prompt_category",
        "vlm_true_pass_count",
        "vlm_true_fail_count",
        "parse_error_count",
        "pass_rate_non_parse",
        "helper_chain_yes_rate_non_parse",
        "label_sequence_by_repeat",
        "helper_chain_sequence_by_repeat",
        "plan_sequence_short",
        "evidence_quote_sequence_short",
    ]
    rows = sorted(group_rows, key=unstable_sort_key)[:30]
    path.write_text("# Top Unstable Task/Prompt Groups\n\n" + markdown_table(rows, fields) + "\n", encoding="utf-8")


def write_stable_groups(path: Path, group_rows: list[dict[str, Any]], success: bool) -> None:
    if success:
        allowed = {"stable_all_pass", "stable_nonparse_pass_with_parse"}
        important = IMPORTANT_SUCCESS_TASKS
        title = "Stable Success Groups"
    else:
        allowed = {"stable_all_fail", "stable_nonparse_fail_with_parse"}
        important = IMPORTANT_FAILURE_TASKS
        title = "Stable Failure Groups"
    rows = [row for row in group_rows if row.get("consistency_type") in allowed]
    rows.sort(key=lambda row: (0 if row.get("task_id") in important else 1, str(row.get("task_id")), str(row.get("prompt_id"))))
    fields = [
        "task_id",
        "prompt_id",
        "consistency_type",
        "vlm_true_pass_count",
        "vlm_true_fail_count",
        "parse_error_count",
        "failure_modes_top",
        "evidence_quote_sequence_short",
    ]
    path.write_text(f"# {title}\n\n" + markdown_table(rows, fields) + "\n", encoding="utf-8")


def write_task002(path: Path, rows: list[dict[str, Any]], group_rows: list[dict[str, Any]], expected_repeats: int) -> None:
    task_groups = [row for row in group_rows if row.get("task_id") == "task_002"]
    task_rows = [row for row in rows if row.get("task_id") == "task_002"]
    never_pass = [row for row in task_groups if intish(row.get("vlm_true_pass_count")) == 0]
    occasional_pass = [row for row in task_groups if 0 < intish(row.get("vlm_true_pass_count")) < expected_repeats]
    true_pass_rows = [row for row in sorted(task_rows, key=lambda r: repeat_sort_key(repeat_id_from_run(str(r.get("run_id", "")), []))) if normalize_label(row) == "true_pass"]
    flip_groups = [row for row in task_groups if boolish(row.get("nonparse_flip"))]
    search_groups = [row for row in task_groups if "search_explicit" in str(row.get("prompt_id", ""))]
    search_stable_pass = [row for row in search_groups if row.get("consistency_type") == "stable_all_pass"]
    search_stable_fail = [row for row in search_groups if row.get("consistency_type") == "stable_all_fail"]

    lines = [
        "# task_002 Repeat Consistency",
        "",
        f"- Prompts that never pass: {len(never_pass)} / 18",
        f"- Prompts with occasional pass: {len(occasional_pass)} / 18",
        f"- VLM true_pass rows: {len(true_pass_rows)}",
        f"- Groups with pass/fail flip: {len(flip_groups)}",
        f"- Search-explicit prompts stable pass: {len(search_stable_pass)} / {len(search_groups)}",
        f"- Search-explicit prompts stable fail: {len(search_stable_fail)} / {len(search_groups)}",
        "",
        "## True Pass Rows",
        "",
    ]
    pass_fields = ["run_id", "prompt_id", "parsed_plan", "evidence_quote", "rationale"]
    lines.append(markdown_table([{field: short(row.get(field, ""), 500) for field in pass_fields} for row in true_pass_rows], pass_fields))
    lines.extend(["", "## Prompt Groups", "", markdown_table(task_groups, ["prompt_id", "consistency_type", "vlm_true_pass_count", "vlm_true_fail_count", "parse_error_count", "label_sequence_by_repeat"])])
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_task005(path: Path, rows: list[dict[str, Any]], group_rows: list[dict[str, Any]], expected_repeats: int) -> None:
    task_groups = [row for row in group_rows if row.get("task_id") == "task_005"]
    task_rows = [row for row in rows if row.get("task_id") == "task_005"]
    stable_pass = [row for row in task_groups if row.get("consistency_type") in {"stable_all_pass", "stable_nonparse_pass_with_parse"}]
    stable_fail = [row for row in task_groups if row.get("consistency_type") in {"stable_all_fail", "stable_nonparse_fail_with_parse"}]
    flips = [row for row in task_groups if boolish(row.get("nonparse_flip"))]
    success_rows = [row for row in task_rows if normalize_label(row) == "true_pass"]
    fail_rows = [row for row in task_rows if normalize_label(row) == "true_fail"]
    success_helper_terms = ["tray", "basin", "basket", "托盘", "盆", "篮", "筐"]
    success_uses_visible_container = sum(1 for row in success_rows if contains_any(row.get("selected_helper", ""), success_helper_terms) or contains_any(row.get("evidence_quote", ""), success_helper_terms))
    fail_modes = Counter()
    for row in fail_rows:
        fail_modes.update(parse_jsonish_list(row.get("failure_modes", "")))

    examples = []
    for row in sorted(success_rows, key=lambda r: (str(r.get("prompt_id", "")), str(r.get("run_id", ""))))[:5]:
        examples.append({"label": "success", "run_id": row.get("run_id", ""), "prompt_id": row.get("prompt_id", ""), "quote": short(row.get("evidence_quote", ""), 240)})
    for row in sorted(fail_rows, key=lambda r: (str(r.get("prompt_id", "")), str(r.get("run_id", ""))))[:5]:
        examples.append({"label": "failure", "run_id": row.get("run_id", ""), "prompt_id": row.get("prompt_id", ""), "quote": short(row.get("evidence_quote", ""), 240)})

    lines = [
        "# task_005 Repeat Consistency",
        "",
        f"- Stable pass prompts: {len(stable_pass)} / 18",
        f"- Stable fail prompts: {len(stable_fail)} / 18",
        f"- Pass/fail flip prompts: {len(flips)} / 18",
        f"- Successful rows mentioning visible tray/basin/basket-like helper: {success_uses_visible_container} / {len(success_rows)}",
        f"- Failure modes top: {' | '.join(f'{mode}:{count}' for mode, count in fail_modes.most_common(8))}",
        "",
        "## Stable Pass Prompts",
        "",
        markdown_table(stable_pass, ["prompt_id", "consistency_type", "vlm_true_pass_count", "parse_error_count", "helper_chain_yes_count"]),
        "",
        "## Stable Fail Prompts",
        "",
        markdown_table(stable_fail, ["prompt_id", "consistency_type", "vlm_true_fail_count", "parse_error_count", "failure_modes_top"]),
        "",
        "## Pass/Fail Flip Prompts",
        "",
        markdown_table(flips, ["prompt_id", "vlm_true_pass_count", "vlm_true_fail_count", "label_sequence_by_repeat", "helper_chain_sequence_by_repeat"]),
        "",
        "## Success/Failure Short Examples",
        "",
        markdown_table(examples, ["label", "run_id", "prompt_id", "quote"]),
    ]
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def contains_any(value: Any, terms: list[str]) -> bool:
    text = str(value).lower()
    return any(term.lower() in text for term in terms)


def build_input_integrity_rows(rows: list[dict[str, Any]], expected_repeats: int, warnings: list[str]) -> list[dict[str, Any]]:
    grouped: dict[tuple[str, str, str, str], list[dict[str, Any]]] = defaultdict(list)
    for row in rows:
        grouped[group_key(row)].append(row)
    output = []
    expected_ids = expected_repeat_ids(expected_repeats)
    for key in sorted(grouped):
        items = grouped[key]
        repeat_ids = [repeat_id_from_run(str(row.get("run_id", "")), warnings) for row in items]
        prompt_counts = [floatish(row.get("prompt_eval_count")) for row in items if str(row.get("prompt_eval_count", "")) != ""]
        total_chars = [floatish(row.get("total_prompt_chars")) for row in items if str(row.get("total_prompt_chars", "")) != ""]
        raw_chars = [floatish(row.get("raw_response_chars")) for row in items if str(row.get("raw_response_chars", "")) != ""]
        system_hashes = sorted({sha1(row.get("system_prompt", "")) for row in items if str(row.get("system_prompt", ""))})
        user_hashes = sorted({sha1(row.get("user_prompt", "")) for row in items if str(row.get("user_prompt", ""))})
        image_names = sorted({str(row.get("image_name", "")) for row in items})
        task_hashes = sorted({sha1(row.get("task_instruction", "")) for row in items if str(row.get("task_instruction", ""))})
        repeat_counter = Counter(repeat_ids)
        input_identical = (
            len(system_hashes) == 1
            and len(user_hashes) == 1
            and len(image_names) == 1
            and len(task_hashes) == 1
            and len(items) == expected_repeats
            and all(repeat_counter[item] == 1 for item in expected_ids)
        )
        output.append(
            {
                "model_id": key[0],
                "task_id": key[1],
                "image_name": key[2],
                "prompt_id": key[3],
                "n_rows": len(items),
                "observed_repeat_ids": " | ".join(sorted(repeat_ids, key=repeat_sort_key)),
                "system_prompt_sha1_set": " | ".join(system_hashes),
                "user_prompt_sha1_set": " | ".join(user_hashes),
                "image_name_set": " | ".join(image_names),
                "task_instruction_set": " | ".join(task_hashes),
                "input_identical_across_repeats": "yes" if input_identical else "no",
                "prompt_eval_count_min": min(prompt_counts) if prompt_counts else "",
                "prompt_eval_count_max": max(prompt_counts) if prompt_counts else "",
                "prompt_eval_count_range": (max(prompt_counts) - min(prompt_counts)) if prompt_counts else "",
                "prompt_eval_count_std": pstdev(prompt_counts) if len(prompt_counts) > 1 else 0.0,
                "total_prompt_chars_min": min(total_chars) if total_chars else "",
                "total_prompt_chars_max": max(total_chars) if total_chars else "",
                "raw_response_chars_min": min(raw_chars) if raw_chars else "",
                "raw_response_chars_max": max(raw_chars) if raw_chars else "",
            }
        )
    return output


def sha1(value: Any) -> str:
    return hashlib.sha1(str(value).encode("utf-8")).hexdigest()


def write_input_integrity_md(path: Path, rows: list[dict[str, Any]]) -> None:
    bad = [row for row in rows if row.get("input_identical_across_repeats") != "yes"]
    fields = ["task_id", "prompt_id", "n_rows", "input_identical_across_repeats", "prompt_eval_count_min", "prompt_eval_count_max", "prompt_eval_count_std"]
    lines = [
        "# Repeat Input Integrity Audit",
        "",
        f"- Total groups audited: {len(rows)}",
        f"- Groups with non-identical inputs or repeat-count issues: {len(bad)}",
        "",
        "## Problem Groups",
        "",
        markdown_table(bad, input_audit_fields(), limit=50),
        "",
        "## Prompt Eval Count Overview",
        "",
        markdown_table(rows, fields, limit=50),
    ]
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def append_input_integrity_to_summary(path: Path, audit_rows: list[dict[str, Any]]) -> None:
    bad = [row for row in audit_rows if row.get("input_identical_across_repeats") != "yes"]
    prompt_changed = [
        row
        for row in audit_rows
        if len(str(row.get("system_prompt_sha1_set", "")).split(" | ")) > 1
        or len(str(row.get("user_prompt_sha1_set", "")).split(" | ")) > 1
        or len(str(row.get("image_name_set", "")).split(" | ")) > 1
        or len(str(row.get("task_instruction_set", "")).split(" | ")) > 1
    ]
    lines = [
        "",
        "## Input Integrity Audit",
        "",
        f"- Groups audited: {len(audit_rows)}",
        f"- Groups with non-identical inputs or repeat-count issues: {len(bad)}",
        f"- Groups with changed system/user/image/task fields: {len(prompt_changed)}",
    ]
    if prompt_changed:
        lines.extend(["", "### Severe Input Mismatches", "", markdown_table(prompt_changed, input_audit_fields(), limit=30)])
    with path.open("a", encoding="utf-8") as handle:
        handle.write("\n".join(lines) + "\n")


def build_vlm_text_comparison(
    vlm_group_rows: list[dict[str, Any]], text_rows: list[dict[str, Any]], expected_repeats: int, warnings: list[str]
) -> list[dict[str, Any]]:
    text_group_rows = build_text_group_rows(text_rows, expected_repeats, warnings)
    text_by_key = {(row["model_id"], row["task_id"], row["image_name"], row["prompt_id"]): row for row in text_group_rows}
    output = []
    for vlm in vlm_group_rows:
        key = (vlm["model_id"], vlm["task_id"], vlm["image_name"], vlm["prompt_id"])
        text = text_by_key.get(key, {})
        output.append(
            {
                "model_id": vlm["model_id"],
                "task_id": vlm["task_id"],
                "image_name": vlm["image_name"],
                "prompt_id": vlm["prompt_id"],
                "vlm_true_pass_count": vlm["vlm_true_pass_count"],
                "vlm_true_fail_count": vlm["vlm_true_fail_count"],
                "vlm_parse_error_count": vlm["parse_error_count"],
                "text_true_pass_count": text.get("vlm_true_pass_count", ""),
                "text_true_fail_count": text.get("vlm_true_fail_count", ""),
                "text_parse_error_count": text.get("parse_error_count", ""),
                "vlm_consistency_type": vlm["consistency_type"],
                "text_consistency_type": text.get("consistency_type", "missing_text_group"),
                "whether_consistency_type_agrees": vlm["consistency_type"] == text.get("consistency_type"),
                "vlm_nonparse_flip": vlm["nonparse_flip"],
                "text_nonparse_flip": text.get("nonparse_flip", ""),
                "vlm_helper_chain_flip": vlm["helper_chain_flip"],
                "text_helper_chain_flip": text.get("helper_chain_flip", ""),
            }
        )
    return output


def build_text_group_rows(rows: list[dict[str, Any]], expected_repeats: int, warnings: list[str]) -> list[dict[str, Any]]:
    adapted = []
    for row in rows:
        new_row = dict(row)
        new_row["vlm_rereview_label"] = row.get("rereview_label", "")
        new_row["failure_modes"] = row.get("rereview_failure_modes", "")
        adapted.append(new_row)
    return build_group_rows(adapted, expected_repeats, warnings)


def write_vlm_text_md(path: Path, rows: list[dict[str, Any]]) -> None:
    agree = sum(1 for row in rows if boolish(row.get("whether_consistency_type_agrees")))
    text_flip_only = [row for row in rows if boolish(row.get("text_nonparse_flip")) and not boolish(row.get("vlm_nonparse_flip"))]
    vlm_flip_only = [row for row in rows if boolish(row.get("vlm_nonparse_flip")) and not boolish(row.get("text_nonparse_flip"))]
    fields = ["task_id", "prompt_id", "vlm_consistency_type", "text_consistency_type", "vlm_nonparse_flip", "text_nonparse_flip"]
    lines = [
        "# VLM vs Text Repeat Consistency Comparison",
        "",
        f"- Groups compared: {len(rows)}",
        f"- Consistency type agreements: {agree}",
        f"- Text-only pass/fail flip groups: {len(text_flip_only)}",
        f"- VLM-only pass/fail flip groups: {len(vlm_flip_only)}",
        "",
        "## Text-Only Flip Groups",
        "",
        markdown_table(text_flip_only, fields, limit=50),
        "",
        "## VLM-Only Flip Groups",
        "",
        markdown_table(vlm_flip_only, fields, limit=50),
    ]
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def task_prompt_fields() -> list[str]:
    return [
        "model_id",
        "task_id",
        "task_name",
        "image_name",
        "prompt_id",
        "prompt_category",
        "embodiment_profile",
        "n_rows",
        "expected_repeats",
        "observed_repeat_ids",
        "missing_repeat_ids",
        "duplicate_repeat_ids",
        "data_integrity_status",
        "vlm_true_pass_count",
        "vlm_true_fail_count",
        "vlm_uncertain_count",
        "tested_model_parse_error_count",
        "judge_parse_error_count",
        "parse_error_count",
        "non_parse_count",
        "pass_rate_all",
        "fail_rate_all",
        "parse_rate_all",
        "pass_rate_non_parse",
        "fail_rate_non_parse",
        "helper_chain_yes_count",
        "helper_chain_no_count",
        "helper_chain_uncertain_count",
        "helper_chain_yes_rate_all",
        "helper_chain_yes_rate_non_parse",
        "label_sequence_by_repeat",
        "helper_chain_sequence_by_repeat",
        "evidence_quote_sequence_short",
        "plan_sequence_short",
        "consistency_type",
        "unique_label_count",
        "majority_label",
        "majority_label_count",
        "majority_label_rate",
        "volatility_score",
        "label_entropy",
        "nonparse_flip",
        "helper_chain_flip",
        "failure_modes_top",
    ]


def task_summary_fields() -> list[str]:
    return [
        "task_id",
        "total_prompt_groups",
        "stable_all_pass_groups",
        "stable_all_fail_groups",
        "stable_all_parse_groups",
        "mixed_pass_fail_groups",
        "helper_chain_flip_groups",
        "groups_with_parse_error",
        "avg_pass_rate_non_parse",
        "avg_helper_chain_yes_rate_non_parse",
        "avg_volatility_score",
        "max_volatility_score",
        "representative_unstable_prompt_ids",
    ]


def prompt_summary_fields() -> list[str]:
    return [
        "prompt_id",
        "prompt_category",
        "embodiment_profile",
        "total_task_groups",
        "stable_all_pass_groups",
        "stable_all_fail_groups",
        "stable_all_parse_groups",
        "mixed_pass_fail_groups",
        "helper_chain_flip_groups",
        "groups_with_parse_error",
        "avg_pass_rate_non_parse",
        "avg_helper_chain_yes_rate_non_parse",
        "avg_volatility_score",
        "max_volatility_score",
        "representative_unstable_task_ids",
    ]


def input_audit_fields() -> list[str]:
    return [
        "model_id",
        "task_id",
        "image_name",
        "prompt_id",
        "n_rows",
        "observed_repeat_ids",
        "system_prompt_sha1_set",
        "user_prompt_sha1_set",
        "image_name_set",
        "task_instruction_set",
        "input_identical_across_repeats",
        "prompt_eval_count_min",
        "prompt_eval_count_max",
        "prompt_eval_count_range",
        "prompt_eval_count_std",
        "total_prompt_chars_min",
        "total_prompt_chars_max",
        "raw_response_chars_min",
        "raw_response_chars_max",
    ]


def vlm_text_fields() -> list[str]:
    return [
        "model_id",
        "task_id",
        "image_name",
        "prompt_id",
        "vlm_true_pass_count",
        "vlm_true_fail_count",
        "vlm_parse_error_count",
        "text_true_pass_count",
        "text_true_fail_count",
        "text_parse_error_count",
        "vlm_consistency_type",
        "text_consistency_type",
        "whether_consistency_type_agrees",
        "vlm_nonparse_flip",
        "text_nonparse_flip",
        "vlm_helper_chain_flip",
        "text_helper_chain_flip",
    ]


if __name__ == "__main__":
    main()
