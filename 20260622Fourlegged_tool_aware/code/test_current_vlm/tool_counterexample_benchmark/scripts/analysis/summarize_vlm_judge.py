from __future__ import annotations

import argparse
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

if __package__ is None or __package__ == "":
    import sys

    sys.path.insert(0, str(Path(__file__).resolve().parent))

from common import normalize_list_field, read_csv_dicts, write_csv_dicts  # noqa: E402

ALLOWED_FAILURE_MODES = {
    "aggregation_failure",
    "container_affordance_miss",
    "helper_search_failure",
    "helper_mention_without_use",
    "tool_necessity_miss",
    "target_as_helper",
    "wrong_helper_type",
    "over_tool_use",
    "direct_operation_without_helper",
    "conditional_helper_only",
    "visual_uncertainty",
    "physical_capacity_hallucination",
    "parse_failure",
    "tested_model_parse_error",
    "judge_parse_error",
}


def main() -> None:
    args = parse_args()
    input_dir = Path(args.input_dir)
    rows = read_csv_dicts(input_dir / "vlm_case_rereview.csv")
    rule_rows = read_csv_dicts(args.rule_case_rereview) if args.rule_case_rereview else []

    write_aggregate(input_dir / "vlm_aggregate_findings.md", rows)
    write_csv_dicts(input_dir / "vlm_task_family_summary.csv", summarize_by(rows, "task_id"), metric_fieldnames("task_id"))
    write_csv_dicts(input_dir / "vlm_model_prompt_matrix.csv", summarize_model_prompt(rows), model_prompt_fieldnames())
    write_rule_comparison(input_dir / "vlm_rule_comparison.csv", rows)
    write_rule_disagreements(input_dir / "vlm_rule_disagreements.md", rows)
    write_handoff(input_dir / "README_FOR_CHATGPT.md", rows, rule_rows)
    print({"input_dir": str(input_dir), "rows": len(rows)})


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Summarize local VLM judge rereview outputs.")
    parser.add_argument("--input_dir", default="analysis_review/round04_strong_tools_vlm_judge_qwen32_smoke")
    parser.add_argument("--rule_case_rereview", default="")
    return parser.parse_args()


def metric_row(name: str, rows: list[dict[str, Any]]) -> dict[str, Any]:
    labels = Counter(row.get("vlm_rereview_label", "") for row in rows)
    non_parse = [row for row in rows if row.get("vlm_rereview_label") not in {"parse_error", "judge_parse_error"}]
    judged = [row for row in non_parse if row.get("vlm_rereview_label") in {"true_pass", "true_fail", "uncertain"}]
    helper_yes = sum(1 for row in judged if row.get("valid_helper_action_chain") == "yes")
    failure_modes = Counter()
    for row in rows:
        failure_modes.update(mode for mode in normalized_failure_modes(row) if mode)
    return {
        "name": name,
        "total_rows": len(rows),
        "true_pass": labels.get("true_pass", 0),
        "true_fail": labels.get("true_fail", 0),
        "uncertain": labels.get("uncertain", 0),
        "tested_model_parse_error": labels.get("parse_error", 0),
        "judge_parse_error": labels.get("judge_parse_error", 0),
        "image_used": sum(1 for row in rows if row.get("image_used") == "yes"),
        "image_missing": sum(1 for row in rows if row.get("image_missing") == "yes"),
        "needs_visual_check": sum(1 for row in rows if row.get("needs_visual_check") == "yes"),
        "judged_non_parse_rows": len(judged),
        "fail_rate": round(labels.get("true_fail", 0) / len(judged), 4) if judged else 0,
        "helper_chain_rate": round(helper_yes / len(judged), 4) if judged else 0,
        "top_failure_modes": "; ".join(f"{mode}:{count}" for mode, count in failure_modes.most_common(6)),
    }


def normalized_failure_modes(row: dict[str, Any]) -> list[str]:
    output: list[str] = []
    raw_modes = normalize_list_field(row.get("failure_modes"))
    for mode in raw_modes:
        label = failure_mode_to_allowed(str(mode))
        if label and label not in output:
            output.append(label)
    if raw_modes and not output:
        output.append("visual_uncertainty")
    return output


def failure_mode_to_allowed(mode: str) -> str:
    normalized = mode.strip().lower().replace(" ", "_").replace("-", "_")
    if normalized in ALLOWED_FAILURE_MODES:
        return normalized
    text = mode.lower()
    checks = [
        ("tested_model_parse_error", ["tested model parse", "model parse", "tested_model_parse", "parse_status"]),
        ("judge_parse_error", ["judge parse", "judge json", "judge error"]),
        ("parse_failure", ["parse", "json", "format"]),
        ("target_as_helper", ["target as helper", "selected helper is target", "target object", "目标物", "目标当作"]),
        ("wrong_helper_type", ["wrong helper", "inappropriate helper", "wrong tool", "不合适", "错误工具"]),
        ("over_tool_use", ["over tool", "unnecessary", "single bottle", "多余", "不必要"]),
        ("conditional_helper_only", ["conditional", "if available", "if needed", "consider", "optional", "如果", "若有", "可考虑", "必要时"]),
        ("helper_search_failure", ["search", "no helper visible", "no container visible", "does not search", "寻找", "搜索", "没有看到", "未搜索"]),
        ("helper_mention_without_use", ["mention", "mentioned", "not used", "without use", "只提到", "提到但", "没有使用"]),
        ("container_affordance_miss", ["visible basket", "visible tray", "visible container", "affordance", "可见", "收纳篮", "托盘", "容器"]),
        ("physical_capacity_hallucination", ["capacity", "carry all", "all loose", "physically", "一次拿", "全部拿", "承载"]),
        ("direct_operation_without_helper", ["direct", "one by one", "by hand", "hand carrying", "direct hand", "直接", "逐个", "一件一件", "一瓶一瓶"]),
        ("tool_necessity_miss", ["tool needed", "helper needed", "necessity", "需要工具", "需要辅助"]),
        ("aggregation_failure", ["aggregation", "aggregate", "batch", "no aggregation", "container before transport", "聚合", "分批"]),
        ("visual_uncertainty", ["visual", "image", "visible", "unclear", "uncertain", "看不清", "图像", "不确定"]),
    ]
    for label, keywords in checks:
        if any(keyword in text for keyword in keywords):
            return label
    return ""


def summarize_by(rows: list[dict[str, Any]], key: str) -> list[dict[str, Any]]:
    grouped: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in rows:
        grouped[str(row.get(key, ""))].append(row)
    return [metric_row(group_key or "-", group_rows) for group_key, group_rows in sorted(grouped.items())]


def summarize_model_prompt(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    grouped: dict[tuple[str, str], list[dict[str, Any]]] = defaultdict(list)
    for row in rows:
        grouped[(str(row.get("model_id", "")), str(row.get("prompt_id", "")))].append(row)
    output = []
    for (model_id, prompt_id), group in sorted(grouped.items()):
        item = metric_row(f"{model_id} / {prompt_id}", group)
        item["model_id"] = model_id
        item["prompt_id"] = prompt_id
        item["prompt_category"] = group[0].get("prompt_category", "") if group else ""
        item["embodiment_profile"] = group[0].get("embodiment_profile", "") if group else ""
        output.append(item)
    return output


def metric_fieldnames(name: str) -> list[str]:
    return [
        "name",
        "total_rows",
        "true_pass",
        "true_fail",
        "uncertain",
        "tested_model_parse_error",
        "judge_parse_error",
        "image_used",
        "image_missing",
        "needs_visual_check",
        "judged_non_parse_rows",
        "fail_rate",
        "helper_chain_rate",
        "top_failure_modes",
    ]


def model_prompt_fieldnames() -> list[str]:
    return ["model_id", "prompt_id", "prompt_category", "embodiment_profile"] + metric_fieldnames("name")


def write_aggregate(path: Path, rows: list[dict[str, Any]]) -> None:
    lines = [
        "# VLM Judge Aggregate Findings",
        "",
        "Image-aware local VLM judge summary. This is still not final paper evidence.",
        "",
        "## Overall",
        "",
        metric_table([metric_row("overall", rows)]),
        "",
    ]
    for title, key in [
        ("By task", "task_id"),
        ("By model", "model_id"),
        ("By prompt", "prompt_id"),
        ("By task family", "task_family"),
    ]:
        lines.extend([f"## {title}", "", metric_table(summarize_by(rows, key)), ""])
    path.write_text("\n".join(lines), encoding="utf-8")


def metric_table(items: list[dict[str, Any]]) -> str:
    lines = [
        "| Name | Rows | Pass | Fail | Uncertain | Tested parse | Judge parse | Image used | Image missing | Visual check | Fail rate | Helper-chain rate | Top failure modes |",
        "| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |",
    ]
    for row in items:
        lines.append(
            f"| {row['name']} | {row['total_rows']} | {row['true_pass']} | {row['true_fail']} | {row['uncertain']} | "
            f"{row['tested_model_parse_error']} | {row['judge_parse_error']} | {row['image_used']} | {row['image_missing']} | "
            f"{row['needs_visual_check']} | {row['fail_rate']} | {row['helper_chain_rate']} | {row['top_failure_modes'] or '-'} |"
        )
    return "\n".join(lines)


def write_rule_comparison(path: Path, rows: list[dict[str, Any]]) -> None:
    fieldnames = [
        "task_id",
        "image_name",
        "model_id",
        "prompt_id",
        "rule_rereview_label",
        "vlm_rereview_label",
        "comparison_type",
        "selected_helper_is_target",
        "conditional_helper_only",
        "committed_helper_use",
        "search_failure_when_helper_not_visible",
        "evidence_quote",
        "rationale",
    ]
    write_csv_dicts(path, [{**{field: row.get(field, "") for field in fieldnames}, "comparison_type": comparison_type(row)} for row in rows], fieldnames)


def write_rule_disagreements(path: Path, rows: list[dict[str, Any]]) -> None:
    selected = [row for row in rows if comparison_type(row) not in {"consistent_or_other", "task002_search_agreement"}]
    lines = ["# VLM Judge vs Rule Disagreements", ""]
    if not selected:
        lines.append("No high-signal disagreements found.")
    for row in selected:
        lines.append(
            f"- {row.get('task_id')} / {row.get('model_id')} / {row.get('prompt_id')}: "
            f"rule={row.get('rule_rereview_label')} vlm={row.get('vlm_rereview_label')} type={comparison_type(row)}. "
            f"Evidence: {row.get('evidence_quote')} Rationale: {row.get('rationale')}"
        )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def comparison_type(row: dict[str, Any]) -> str:
    rule = str(row.get("rule_rereview_label", ""))
    vlm = str(row.get("vlm_rereview_label", ""))
    if rule == "true_pass" and vlm == "true_fail":
        return "rule_true_pass_vlm_true_fail"
    if rule == "true_fail" and vlm == "true_pass":
        return "rule_true_fail_vlm_true_pass"
    if rule == "uncertain" and vlm in {"true_pass", "true_fail"}:
        return "rule_uncertain_vlm_resolved"
    if rule == "true_pass" and row.get("selected_helper_is_target") == "yes":
        return "rule_pass_vlm_selected_helper_is_target"
    if rule == "true_pass" and row.get("conditional_helper_only") == "yes":
        return "rule_pass_vlm_conditional_helper_only"
    if rule == "true_fail" and row.get("committed_helper_use") == "yes":
        return "rule_fail_vlm_committed_helper_use"
    if row.get("task_id") == "task_002":
        return "task002_search_agreement" if row.get("search_failure_when_helper_not_visible") in {"yes", "no"} else "task002_search_review"
    return "consistent_or_other"


def write_handoff(path: Path, rows: list[dict[str, Any]], rule_rows: list[dict[str, Any]]) -> None:
    labels = Counter(row.get("vlm_rereview_label", "") for row in rows)
    comparisons = Counter(comparison_type(row) for row in rows)
    models = sorted({row.get("model_id", "") for row in rows})
    tasks = sorted({row.get("task_id", "") for row in rows})
    lines = [
        "# README For ChatGPT",
        "",
        "This is a local image-aware VLM judge rereview handoff. It is not final paper evidence.",
        "",
        "## Scope",
        f"- Rows judged: {len(rows)}",
        f"- Tested models: {', '.join(models)}",
        f"- Tasks: {', '.join(tasks)}",
        f"- VLM labels: {dict(labels)}",
        f"- Rule comparison types: {dict(comparisons)}",
        "",
        "## How To Read",
        "- `vlm_case_rereview.csv/jsonl` contains row-level judge decisions.",
        "- `vlm_rule_disagreements.md` highlights where VLM judge and rule rereview disagree.",
        "- Image-aware judge output can still be wrong and requires human review for claims.",
        "",
        "## Key Warnings",
        "- Judge is another VLM, not ground truth.",
        "- Image visibility and physical feasibility should still be human verified.",
        "- Parse failures of tested models and judge parse failures are separate from planning failures.",
        "- This workflow is intended to reduce keyword-rule mistakes, not replace final manual review.",
    ]
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
