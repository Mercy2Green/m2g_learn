from __future__ import annotations

import argparse
import json
import sys
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any, Callable

if __package__ is None or __package__ == "":
    sys.path.insert(0, str(Path(__file__).resolve().parent))

from common import normalize_list_field, read_jsonl, write_csv_dicts  # noqa: E402


PROMPT_PAIRS = {
    "natural_free_plan": "tool_prior_free_plan",
    "natural_free_plan_humanoid_dual_arm": "tool_prior_free_plan_humanoid_dual_arm",
    "natural_free_plan_quadruped_single_arm": "tool_prior_free_plan_quadruped_single_arm",
}
EFFICIENT_PROMPT_PAIRS = {
    "efficient_safe_free_plan": "tool_prior_free_plan",
    "efficient_safe_free_plan_humanoid_dual_arm": "tool_prior_free_plan_humanoid_dual_arm",
    "efficient_safe_free_plan_quadruped_single_arm": "tool_prior_free_plan_quadruped_single_arm",
}


def main() -> None:
    args = parse_args()
    input_path = Path(args.input)
    output_dir = Path(args.output_dir) if args.output_dir else input_path.parent
    output_dir.mkdir(parents=True, exist_ok=True)
    rows = read_jsonl(input_path)

    write_aggregate_findings(output_dir / "aggregate_findings.md", rows)
    write_csv_dicts(output_dir / "task_family_summary.csv", summarize_by(rows, "task_id"), summary_fieldnames("task_id"))
    write_csv_dicts(output_dir / "model_prompt_matrix.csv", summarize_model_prompt(rows), model_prompt_fieldnames())
    write_prompt_delta(output_dir / "prompt_intervention_delta.md", rows)
    write_candidates(output_dir / "counterexample_candidates_ranked.md", rows)
    write_handoff(output_dir / "README_FOR_CHATGPT.md", rows)

    print(json.dumps({"output_dir": str(output_dir), "rows": len(rows)}, ensure_ascii=False))


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Summarize rereviewed benchmark rows.")
    parser.add_argument("--input", default="analysis_review/round02_full_important_outputs/case_rereview.jsonl")
    parser.add_argument("--output_dir", default=None)
    return parser.parse_args()


def metric_row(name: str, rows: list[dict[str, Any]]) -> dict[str, Any]:
    labels = Counter(str(row.get("rereview_label", "")) for row in rows)
    reviewed_valid = labels.get("true_pass", 0) + labels.get("true_fail", 0) + labels.get("uncertain", 0)
    failure_modes = Counter()
    valid_helper = 0
    visual = 0
    for row in rows:
        if row.get("valid_helper_action_chain") == "yes":
            valid_helper += 1
        if row.get("needs_visual_check") == "yes":
            visual += 1
        failure_modes.update(mode for mode in normalize_list_field(row.get("rereview_failure_modes")) if mode)
    return {
        "name": name,
        "total_rows": len(rows),
        "true_pass": labels.get("true_pass", 0),
        "true_fail": labels.get("true_fail", 0),
        "uncertain": labels.get("uncertain", 0),
        "parse_error": labels.get("parse_error", 0),
        "skipped": labels.get("skipped", 0),
        "reviewed_valid_rows": reviewed_valid,
        "true_fail_rate": round(labels.get("true_fail", 0) / reviewed_valid, 4) if reviewed_valid else 0,
        "valid_helper_action_chain_rate": round(valid_helper / reviewed_valid, 4) if reviewed_valid else 0,
        "needs_visual_check_count": visual,
        "top_failure_modes": "; ".join(f"{mode}:{count}" for mode, count in failure_modes.most_common(5)),
    }


def summarize_by(rows: list[dict[str, Any]], key: str) -> list[dict[str, Any]]:
    grouped: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in rows:
        grouped[str(row.get(key, ""))].append(row)
    return [metric_row(group_key or "-", group_rows) for group_key, group_rows in sorted(grouped.items())]


def summarize_model_prompt(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    grouped: dict[tuple[str, str], list[dict[str, Any]]] = defaultdict(list)
    for row in rows:
        grouped[(str(row.get("model_id", "")), str(row.get("prompt_id", "")))].append(row)
    output: list[dict[str, Any]] = []
    for (model_id, prompt_id), group_rows in sorted(grouped.items()):
        summary = metric_row(f"{model_id} / {prompt_id}", group_rows)
        summary["model_id"] = model_id
        summary["prompt_id"] = prompt_id
        summary["prompt_category"] = group_rows[0].get("prompt_category", "") if group_rows else ""
        summary["embodiment_profile"] = group_rows[0].get("embodiment_profile", "") if group_rows else ""
        output.append(summary)
    return output


def summary_fieldnames(name_field: str) -> list[str]:
    return [
        "name",
        "total_rows",
        "true_pass",
        "true_fail",
        "uncertain",
        "parse_error",
        "skipped",
        "reviewed_valid_rows",
        "true_fail_rate",
        "valid_helper_action_chain_rate",
        "needs_visual_check_count",
        "top_failure_modes",
    ]


def model_prompt_fieldnames() -> list[str]:
    return ["model_id", "prompt_id", "prompt_category", "embodiment_profile"] + summary_fieldnames("name")


def write_aggregate_findings(path: Path, rows: list[dict[str, Any]]) -> None:
    lines = ["# Aggregate Findings", "", "Text-based rereview summary. This is not final paper evidence.", ""]
    for title, key in [
        ("By prompt category", "prompt_category"),
        ("By prompt ID", "prompt_id"),
        ("By model", "model_id"),
        ("By task", "task_id"),
        ("By embodiment", "embodiment_profile"),
    ]:
        lines.extend([f"## {title}", "", metric_table(summarize_by(rows, key)), ""])
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def metric_table(metric_rows: list[dict[str, Any]]) -> str:
    lines = [
        "| Name | Rows | Pass | Fail | Uncertain | Parse | Skipped | Fail rate | Helper-chain rate | Visual checks | Top failure modes |",
        "| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |",
    ]
    for row in metric_rows:
        lines.append(
            f"| {row['name']} | {row['total_rows']} | {row['true_pass']} | {row['true_fail']} | {row['uncertain']} | "
            f"{row['parse_error']} | {row['skipped']} | {row['true_fail_rate']} | {row['valid_helper_action_chain_rate']} | "
            f"{row['needs_visual_check_count']} | {row['top_failure_modes'] or '-'} |"
        )
    return "\n".join(lines)


def write_prompt_delta(path: Path, rows: list[dict[str, Any]]) -> None:
    deltas = compute_prompt_deltas(rows, PROMPT_PAIRS, "natural_vs_tool_prior")
    efficient_deltas = compute_prompt_deltas(rows, EFFICIENT_PROMPT_PAIRS, "efficient_vs_tool_prior")
    lines = ["# Prompt Intervention Delta", "", "Tool-prior prompts are intervention checks, not clean evidence.", ""]
    lines.extend(["## Natural clean vs tool-prior", "", delta_tables(deltas), ""])
    lines.extend(["## Efficient/safe clean vs tool-prior", "", delta_tables(efficient_deltas), ""])
    for title, predicate in [
        ("Examples of prompted improvement", lambda d: d["delta_type"] == "prompted_improvement"),
        ("Examples where tool-prior still fails", lambda d: d["delta_type"] == "robust_failure"),
        ("Examples where tool-prior degrades", lambda d: d["delta_type"] == "tool_prior_degradation"),
    ]:
        lines.extend([f"## {title}", ""])
        subset = [delta for delta in deltas + efficient_deltas if predicate(delta)]
        if not subset:
            lines.append("- None found.")
        for delta in subset[:30]:
            lines.append(
                f"- {delta['task_id']} / {delta['image_name']} / {delta['model_id']} / {delta['embodiment_profile']}: "
                f"{delta['clean_prompt']}={delta['clean_label']} -> {delta['tool_prior_prompt']}={delta['tool_prior_label']}. "
                f"Evidence: {delta['tool_prior_evidence']}"
            )
        lines.append("")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def compute_prompt_deltas(rows: list[dict[str, Any]], pairs: dict[str, str], comparison: str) -> list[dict[str, Any]]:
    by_key: dict[tuple[str, str, str, str, str], dict[str, Any]] = {}
    for row in rows:
        key = (
            str(row.get("task_id", "")),
            str(row.get("image_name", "")),
            str(row.get("model_id", "")),
            str(row.get("embodiment_profile", "")),
            str(row.get("prompt_id", "")),
        )
        by_key[key] = row
    deltas: list[dict[str, Any]] = []
    for clean_prompt, tool_prompt in pairs.items():
        for row in rows:
            if row.get("prompt_id") != clean_prompt:
                continue
            clean_key = (
                str(row.get("task_id", "")),
                str(row.get("image_name", "")),
                str(row.get("model_id", "")),
                str(row.get("embodiment_profile", "")),
                clean_prompt,
            )
            tool_key = clean_key[:-1] + (tool_prompt,)
            tool_row = by_key.get(tool_key)
            if not tool_row:
                continue
            deltas.append(
                {
                    "comparison": comparison,
                    "task_id": row.get("task_id", ""),
                    "image_name": row.get("image_name", ""),
                    "model_id": row.get("model_id", ""),
                    "embodiment_profile": row.get("embodiment_profile", ""),
                    "clean_prompt": clean_prompt,
                    "tool_prior_prompt": tool_prompt,
                    "clean_label": row.get("rereview_label", ""),
                    "tool_prior_label": tool_row.get("rereview_label", ""),
                    "delta_type": classify_delta(str(row.get("rereview_label", "")), str(tool_row.get("rereview_label", ""))),
                    "tool_prior_evidence": tool_row.get("evidence_quote", ""),
                }
            )
    return deltas


def classify_delta(clean_label: str, tool_label: str) -> str:
    if clean_label == "true_fail" and tool_label == "true_pass":
        return "prompted_improvement"
    if clean_label == "true_fail" and tool_label == "true_fail":
        return "robust_failure"
    if clean_label == "true_pass" and tool_label == "true_pass":
        return "stable_success"
    if clean_label == "true_pass" and tool_label == "true_fail":
        return "tool_prior_degradation"
    return "uncertain_or_parse"


def delta_tables(deltas: list[dict[str, Any]]) -> str:
    by_model = Counter(delta["delta_type"] for delta in deltas)
    lines = ["### Overall", "", "| Delta type | Count |", "| --- | ---: |"]
    for key, count in by_model.most_common():
        lines.append(f"| {key} | {count} |")
    lines.extend(["", "### Per-model", "", "| Model | Prompted improvement | Robust failure | Stable success | Degradation | Other |", "| --- | ---: | ---: | ---: | ---: | ---: |"])
    grouped: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for delta in deltas:
        grouped[str(delta["model_id"])].append(delta)
    for model_id, group in sorted(grouped.items()):
        counter = Counter(delta["delta_type"] for delta in group)
        lines.append(
            f"| {model_id} | {counter.get('prompted_improvement', 0)} | {counter.get('robust_failure', 0)} | "
            f"{counter.get('stable_success', 0)} | {counter.get('tool_prior_degradation', 0)} | {counter.get('uncertain_or_parse', 0)} |"
        )
    lines.extend(["", "### Per-task", "", "| Task | Prompted improvement | Robust failure | Stable success | Degradation | Other |", "| --- | ---: | ---: | ---: | ---: | ---: |"])
    grouped_task: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for delta in deltas:
        grouped_task[str(delta["task_id"])].append(delta)
    for task_id, group in sorted(grouped_task.items()):
        counter = Counter(delta["delta_type"] for delta in group)
        lines.append(
            f"| {task_id} | {counter.get('prompted_improvement', 0)} | {counter.get('robust_failure', 0)} | "
            f"{counter.get('stable_success', 0)} | {counter.get('tool_prior_degradation', 0)} | {counter.get('uncertain_or_parse', 0)} |"
        )
    return "\n".join(lines)


def write_candidates(path: Path, rows: list[dict[str, Any]]) -> None:
    primary_failures = [
        row for row in rows
        if _is_true(row.get("primary_for_counterexample"))
        and row.get("rereview_label") == "true_fail"
        and row.get("rereview_confidence") in {"high", "medium"}
        and row.get("prompt_category") != "tool_prior_intervention"
        and row.get("prompt_category") != "diagnostic_probe"
    ]
    grouped: dict[tuple[str, str, str], list[dict[str, Any]]] = defaultdict(list)
    for row in primary_failures:
        grouped[(str(row.get("task_id", "")), str(row.get("image_name", "")), str(row.get("prompt_id", "")))].append(row)
    ranked = sorted(grouped.items(), key=lambda item: (len({r.get("model_id") for r in item[1]}), len(item[1])), reverse=True)
    lines = ["# Counterexample Candidates Ranked", "", "Only primary clean prompts are ranked here. Tool-prior and diagnostic rows are excluded.", ""]
    if not ranked:
        lines.append("No clean candidates found.")
    for rank, ((task_id, image_name, prompt_id), group) in enumerate(ranked[:80], start=1):
        models = sorted({str(row.get("model_id", "")) for row in group})
        modes = Counter()
        visual_count = 0
        for row in group:
            modes.update(mode for mode in normalize_list_field(row.get("rereview_failure_modes")) if mode)
            if row.get("needs_visual_check") == "yes":
                visual_count += 1
        best = group[0]
        caveat = "needs image verification" if visual_count else "text-only evidence; still verify image before claims"
        lines.extend(
            [
                f"## {rank}. {task_id} / {image_name} / {prompt_id}",
                "",
                f"- Models failed: {', '.join(models)}",
                f"- Failure modes: {', '.join(mode for mode, _ in modes.most_common()) or '-'}",
                f"- Evidence quote: {best.get('evidence_quote', '')}",
                f"- Why it is a counterexample: primary clean prompt failed under text rereview with {len(models)} model(s).",
                f"- Caveat: {caveat}",
                "",
            ]
        )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_handoff(path: Path, rows: list[dict[str, Any]]) -> None:
    labels = Counter(row.get("rereview_label", "") for row in rows)
    prompt_categories = Counter(row.get("prompt_category", "") for row in rows)
    models = sorted({str(row.get("model_id", "")) for row in rows})
    tasks = sorted({str(row.get("task_id", "")) for row in rows})
    top_failures = Counter()
    for row in rows:
        top_failures.update(mode for mode in normalize_list_field(row.get("rereview_failure_modes")) if mode)
    candidates = [
        row for row in rows
        if _is_true(row.get("primary_for_counterexample"))
        and row.get("rereview_label") == "true_fail"
        and row.get("rereview_confidence") in {"high", "medium"}
    ][:10]
    deltas = compute_prompt_deltas(rows, PROMPT_PAIRS, "natural_vs_tool_prior")
    improvements = [delta for delta in deltas if delta["delta_type"] == "prompted_improvement"][:10]
    robust = [delta for delta in deltas if delta["delta_type"] == "robust_failure"][:10]
    lines = [
        "# README For ChatGPT",
        "",
        "This is an automatic text-based rereview handoff. It suggests analysis directions but is not final paper evidence.",
        "",
        "## Data Scope",
        f"- Rows: {len(rows)}",
        f"- Models: {len(models)} ({', '.join(models[:12])}{'...' if len(models) > 12 else ''})",
        f"- Tasks: {len(tasks)} ({', '.join(tasks)})",
        f"- Prompt categories: {dict(prompt_categories)}",
        f"- Rereview labels: {dict(labels)}",
        "",
        "## Rereview Rubric Summary",
        "- Valid helper use requires a committed action chain, not just helper mention.",
        "- Conditional helper-only plans are not counted as valid helper use.",
        "- Tool-prior prompts are intervention checks, not clean evidence.",
        "- Visual uncertainty remains unresolved until image-level review.",
        "",
        "## Top 10 Findings",
    ]
    for mode, count in top_failures.most_common(10):
        lines.append(f"- {mode}: {count} text-based labels")
    lines.extend(["", "## Top Clean Counterexample Candidates"])
    for row in candidates:
        lines.append(f"- {row.get('task_id')} / {row.get('image_name')} / {row.get('model_id')} / {row.get('prompt_id')}: {row.get('rereview_failure_modes')} | {row.get('evidence_quote')}")
    lines.extend(["", "## Top Prompted Improvement Cases"])
    if not improvements:
        lines.append("- None in the summarized rows.")
    for delta in improvements:
        lines.append(f"- {delta['task_id']} / {delta['image_name']} / {delta['model_id']}: {delta['clean_prompt']} fail -> {delta['tool_prior_prompt']} pass")
    lines.extend(["", "## Top Robust Failures Across Clean/Tool-Prior"])
    if not robust:
        lines.append("- None in the summarized rows.")
    for delta in robust:
        lines.append(f"- {delta['task_id']} / {delta['image_name']} / {delta['model_id']}: clean and tool-prior both true_fail")
    lines.extend(
        [
            "",
            "## Main Uncertainty Sources",
            "- Image visibility of helpers/targets was not checked.",
            "- Parse-recoverable outputs need manual interpretation.",
            "- Some helper mentions may be background or conditional rather than committed use.",
            "",
            "## Generated Files",
            "- `aggregate_findings.md`: aggregate text-rereview metrics.",
            "- `task_family_summary.csv`: per-task metrics.",
            "- `model_prompt_matrix.csv`: per-model/prompt matrix.",
            "- `prompt_intervention_delta.md`: clean vs tool-prior comparisons.",
            "- `counterexample_candidates_ranked.md`: ranked clean failure candidates.",
            "",
            "## Warning",
            "Automatic text rereview is not final paper evidence. Selected claims require image-level human review.",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def _is_true(value: Any) -> bool:
    if isinstance(value, bool):
        return value
    return str(value).lower() in {"true", "1", "yes"}


if __name__ == "__main__":
    main()
