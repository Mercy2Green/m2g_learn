from __future__ import annotations

import argparse
import json
import sys
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

if __package__ is None or __package__ == "":
    sys.path.insert(0, str(Path(__file__).resolve().parent))

from common import (  # noqa: E402
    compact_text,
    contains_any,
    extract_evidence_quote,
    extract_plan_text,
    normalize_list_field,
    read_jsonl,
    write_csv_dicts,
    write_jsonl,
)


GENERAL_HELPER_KEYWORDS = [
    "helper",
    "tool",
    "工具",
    "辅助物",
    "tray",
    "托盘",
    "bag",
    "袋子",
    "box",
    "盒子",
    "箱子",
    "basket",
    "篮子",
    "basin",
    "container",
    "storage bin",
    "bin",
    "backpack",
    "背包",
    "容器",
    "收纳篮",
    "盆",
    "框",
    "筐",
    "broom",
    "扫把",
    "dustpan",
    "簸箕",
    "rod",
    "stick",
    "杆",
    "长杆",
    "cloth",
    "抹布",
    "tissue",
    "纸巾",
]
HELPER_ACTION_KEYWORDS = [
    "place",
    "place in",
    "place into",
    "put",
    "put in",
    "put into",
    "load",
    "load into",
    "carry",
    "transport",
    "deliver",
    "collect",
    "gather",
    "push",
    "pull",
    "hook",
    "sweep",
    "wipe",
    "clean",
    "use",
    "放入",
    "放进",
    "放到",
    "放置到",
    "装入",
    "装进",
    "收集到",
    "集中放置",
    "暂存到",
    "搬运",
    "运送",
    "收集",
    "使用",
    "用",
    "拨",
    "拉",
    "推",
    "勾",
    "扫",
    "擦",
    "清理",
]
HELPER_ACQUISITION_KEYWORDS = [
    "find",
    "locate",
    "get",
    "pick up",
    "take",
    "select",
    "obtain",
    "寻找",
    "找到",
    "拿",
    "取",
    "选择",
    "获取",
]
HELPER_REFERENCE_TERMS = [
    "it",
    "them",
    "this helper",
    "that helper",
    "the helper",
    "the tool",
    "the container",
    "the tray",
    "the basket",
    "the box",
    "the bag",
    "它",
    "它们",
    "其",
    "将其",
    "把它",
    "这个辅助物",
    "该辅助物",
    "该工具",
    "该容器",
    "托盘",
    "篮子",
    "箱子",
    "袋子",
]
CONDITIONAL_HELPER_PATTERNS = [
    "or use",
    "or find",
    "if possible",
    "if available",
    "consider using",
    "try to use",
    "optionally",
    "if needed",
    "或使用",
    "或寻找",
    "如果有",
    "如果可用",
    "若有",
    "可考虑",
    "考虑使用",
    "尝试使用",
    "必要时",
    "有的话",
]
SEARCH_KEYWORDS = ["寻找", "查找", "检查附近", "查看附近", "搜索附近", "look for", "search nearby", "check nearby"]
NEGATION_KEYWORDS = ["avoid", "避开", "不要碰", "not use", "不用", "不使用", "ignore", "忽略"]
DIRECT_OPERATION_KEYWORDS = [
    "directly grasp",
    "grasp directly",
    "grasp the remote directly",
    "pick up directly",
    "directly pick",
    "use the gripper to pick",
    "直接抓取",
    "直接拿",
    "直接夹取",
    "直接拾取",
]
DIRECT_CAPACITY_KEYWORDS = [
    "grab all",
    "carry all",
    "pick up all",
    "carry them all",
    "hold all",
    "all four",
    "all bottles",
    "拿起所有",
    "抓起所有",
    "直接拿所有",
    "一次拿完",
    "全部直接拿",
]
HELPER_GROUPS = {
    "aggregation": [
        "tray",
        "bag",
        "box",
        "basket",
        "basin",
        "container",
        "storage bin",
        "bin",
        "backpack",
        "托盘",
        "袋子",
        "箱子",
        "盒子",
        "篮子",
        "收纳篮",
        "容器",
        "盆",
        "框",
        "筐",
        "背包",
    ],
    "reach": ["rod", "stick", "broom", "杆", "长杆", "扫把"],
    "cleaning": ["dustpan", "broom", "cloth", "tissue", "簸箕", "扫把", "抹布", "纸巾"],
}
CONTAINER_TERMS = HELPER_GROUPS["aggregation"]
CONTAINER_COLLECTION_ACTIONS = [
    "put into",
    "place into",
    "place in",
    "put in",
    "load into",
    "collect into",
    "gather into",
    "deposit into",
    "place objects in",
    "put items into",
    "load bottles onto",
    "放入",
    "放进",
    "放到",
    "放置到",
    "装入",
    "装进",
    "收集到",
    "集中放置",
    "暂存到",
]
TRANSPORT_ACTIONS = ["carry", "transport", "deliver", "bring", "move", "端起", "搬", "搬运", "运送", "送到", "带到", "提起", "拿到"]
REACH_USE_ACTIONS = ["use", "push", "pull", "hook", "retrieve", "reach", "拨", "拉", "推", "勾", "取出", "够到", "用"]

CSV_FIELDNAMES = [
    "run_id",
    "task_id",
    "task_name",
    "image_name",
    "model_id",
    "prompt_id",
    "prompt_category",
    "prompt_type",
    "embodiment_profile",
    "primary_for_counterexample",
    "auto_pass_fail",
    "rereview_label",
    "rereview_confidence",
    "disagreement_type",
    "helper_mentioned",
    "valid_helper_action_chain",
    "helper_only_mentioned_not_used",
    "target_as_helper",
    "wrong_helper_type",
    "direct_capacity_risk",
    "direct_operation_when_tool_needed",
    "search_failure_when_helper_not_visible",
    "over_tool_use",
    "field_plan_inconsistency",
    "conditional_helper_only",
    "committed_helper_use",
    "needs_visual_check",
    "rereview_failure_modes",
    "rereview_caveats",
    "evidence_quote",
    "rereview_reason",
    "auto_failure_types",
    "auto_notes",
    "parsed_plan",
    "parsed_reason",
    "raw_response_short",
]


def main() -> None:
    args = parse_args()
    if args.self_test:
        run_self_test()
        print("rereview self-test passed")
        return

    input_path = Path(args.input)
    output_dir = Path(args.output_dir) if args.output_dir else input_path.parent
    output_dir.mkdir(parents=True, exist_ok=True)

    rows = read_jsonl(input_path)
    reviewed = [rereview_row(row) for row in rows]
    write_csv_dicts(output_dir / "case_rereview.csv", reviewed, CSV_FIELDNAMES)
    write_jsonl(output_dir / "case_rereview.jsonl", reviewed)
    write_disagreements(output_dir / "rereview_disagreements.md", reviewed)
    write_high_confidence_cases(output_dir / "high_confidence_cases.md", reviewed)
    write_uncertain_cases(output_dir / "uncertain_cases_for_human.md", reviewed)

    counts = Counter(row["rereview_label"] for row in reviewed)
    disagreements = sum(1 for row in reviewed if row["disagreement_type"] not in {"consistent", "auto_parse_or_skip"})
    print(json.dumps({"output_dir": str(output_dir), "rows": len(reviewed), "labels": counts, "disagreements": disagreements}, ensure_ascii=False))


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Strict text-based rereview of merged benchmark rows.")
    parser.add_argument("--input", default="analysis_review/round01_small_subset/all_rows_merged.jsonl")
    parser.add_argument("--output_dir", default=None)
    parser.add_argument("--self_test", action="store_true")
    return parser.parse_args()


def rereview_row(row: dict[str, Any]) -> dict[str, Any]:
    base = base_review_row(row)
    auto_status = str(row.get("auto_pass_fail", ""))
    parse_status = str(row.get("parse_status", ""))
    if auto_status == "skipped":
        base.update(label("skipped", "high", ["skipped_missing_image"], "Row was skipped, likely because no image files were found."))
        return finalize_review(base, row)
    if parse_status != "ok":
        raw_text = str(row.get("raw_response", ""))
        if _looks_parse_recoverable(raw_text):
            base["parse_recoverable"] = "yes"
            base.update(label("uncertain", "low", ["parse_failure"], "Parse failed, but raw response may contain a recoverable plan."))
        else:
            base["parse_recoverable"] = "no"
            base.update(label("parse_error", "high", ["parse_failure"], "Parsed record is not valid JSON."))
        return finalize_review(base, row)

    parsed = row.get("parsed", {}) if isinstance(row.get("parsed", {}), dict) else {}
    plan_steps = normalize_list_field(parsed.get("plan") or row.get("parsed_plan"))
    chain_steps = normalize_list_field(parsed.get("tool_use_action_chain") or row.get("parsed_tool_use_action_chain"))
    text = extract_plan_text(row)
    expected_helper = _bool_value(row.get("expected_should_use_tool_or_container"))
    expected_search = _bool_value(row.get("expected_should_search_for_tool_if_not_visible"))
    avoid_over_tool = _bool_value(row.get("expected_should_avoid_over_tool_use"))
    expected_helpers = normalize_list_field(row.get("expected_tool_or_container_types"))
    target_terms = normalize_list_field(row.get("target_object_terms"))
    selected_helper = str(parsed.get("selected_helper") or parsed.get("tool_or_container") or row.get("parsed_selected_helper") or "")
    helper_terms = _helper_terms(expected_helpers, selected_helper)
    task_family = task_family_for(row)

    helper_mentioned = contains_any(text, helper_terms)
    target_as_helper = bool(selected_helper) and _matches_any(selected_helper, target_terms)
    valid_chain = _has_valid_helper_action_chain(
        plan_steps,
        chain_steps,
        helper_terms,
        target_as_helper,
        expected_helpers,
        str(row.get("task_id", "")),
        task_family,
        text,
    )
    conditional_helper_only = _conditional_helper_only(plan_steps, chain_steps, text, helper_terms, valid_chain)
    committed_helper_use = valid_chain and not conditional_helper_only
    if conditional_helper_only:
        valid_chain = False
        committed_helper_use = False
    helper_only_mentioned = helper_mentioned and not valid_chain
    direct_capacity = contains_any(text, DIRECT_CAPACITY_KEYWORDS) and not valid_chain
    direct_operation = contains_any(text, DIRECT_OPERATION_KEYWORDS)
    search_failure = expected_search and not contains_any(text, SEARCH_KEYWORDS) and not valid_chain
    wrong_helper_type = _wrong_helper_type(text, expected_helpers, valid_chain)
    field_plan_inconsistency = _field_plan_inconsistency(parsed, valid_chain, selected_helper)
    over_tool_use = avoid_over_tool and valid_chain
    needs_visual_check = _needs_visual_check(row, helper_mentioned, valid_chain)

    base.update(
        {
            "helper_mentioned": tri(helper_mentioned),
            "valid_helper_action_chain": "yes" if valid_chain else "no",
            "helper_only_mentioned_not_used": tri(helper_only_mentioned),
            "target_as_helper": tri(target_as_helper),
            "wrong_helper_type": tri(wrong_helper_type),
            "direct_capacity_risk": tri(direct_capacity),
            "direct_operation_when_tool_needed": tri(expected_helper and direct_operation and not valid_chain),
            "search_failure_when_helper_not_visible": "yes" if search_failure else ("not_applicable" if not expected_search else "no"),
            "over_tool_use": tri(over_tool_use),
            "field_plan_inconsistency": tri(field_plan_inconsistency),
            "conditional_helper_only": tri(conditional_helper_only),
            "committed_helper_use": tri(committed_helper_use),
            "needs_visual_check": tri(needs_visual_check),
            "evidence_quote": extract_evidence_quote(text),
        }
    )

    failure_modes: list[str] = []
    caveats: list[str] = []
    reasons: list[str] = []
    if target_as_helper:
        failure_modes.append("target_as_helper")
        reasons.append("Selected helper appears to be a target object.")
    if field_plan_inconsistency:
        failure_modes.append("field_plan_inconsistency")
        reasons.append("Helper fields claim or imply helper use, but plan/action chain does not support it.")
    if wrong_helper_type:
        failure_modes.append("wrong_helper_type")
        reasons.append("The apparent helper type does not match the task's expected helper function.")
    if direct_capacity:
        failure_modes.append("physical_capacity_hallucination")
        reasons.append("Plan directly carries many loose objects without a valid helper.")
    if search_failure:
        failure_modes.append("helper_search_failure")
        reasons.append("Task expects helper search/fallback, but plan does not search.")
    if conditional_helper_only:
        failure_modes.append("helper_mention_without_use")
        reasons.append("Helper use is only conditional or optional, with no committed helper action chain.")
    elif helper_only_mentioned and expected_helper:
        failure_modes.append("helper_mention_without_use")
        reasons.append("A helper is mentioned but no valid helper action chain is present.")
    elif helper_only_mentioned:
        caveats.append("Helper is mentioned but not used; direct handling may be acceptable for this task.")
    if expected_helper and direct_operation and not valid_chain:
        failure_modes.append("tool_necessity_miss")
        reasons.append("Plan directly operates on the target although helper use is expected.")
    if expected_helper and not valid_chain and not helper_mentioned:
        failure_modes.extend(["aggregation_failure", "container_affordance_miss"])
        reasons.append("Expected helper use, but no valid helper action chain is evident.")
    if over_tool_use:
        failure_modes.append("over_tool_use")
        reasons.append("Task expects direct handling, but plan uses a helper.")
    if needs_visual_check:
        failure_modes.append("visual_uncertainty")
        reasons.append("Correctness depends on image-visible helper/target details not verified by text.")

    failure_modes = sorted(set(failure_modes))
    if over_tool_use or target_as_helper or direct_capacity or search_failure or wrong_helper_type or (expected_helper and (direct_operation or not valid_chain)):
        base.update(label("true_fail", "high" if not needs_visual_check else "medium", failure_modes, " ".join(reasons), caveats))
    elif expected_helper and helper_only_mentioned:
        base.update(label("uncertain", "medium", failure_modes, " ".join(reasons), caveats))
    elif needs_visual_check:
        base.update(label("uncertain", "medium", failure_modes, " ".join(reasons), caveats))
    else:
        base.update(label("true_pass", "high", [], "Valid helper use or acceptable direct handling is supported by the text.", caveats))
    return finalize_review(base, row)


def base_review_row(row: dict[str, Any]) -> dict[str, Any]:
    return {
        "run_id": row.get("run_id", ""),
        "task_id": row.get("task_id", ""),
        "task_name": row.get("task_name", ""),
        "image_name": row.get("image_name", ""),
        "model_id": row.get("model_id", ""),
        "prompt_id": row.get("prompt_id", ""),
        "prompt_category": row.get("prompt_category", ""),
        "prompt_type": row.get("prompt_type", ""),
        "embodiment_profile": row.get("embodiment_profile", ""),
        "primary_for_counterexample": row.get("primary_for_counterexample", ""),
        "auto_pass_fail": row.get("auto_pass_fail", ""),
        "rereview_label": "uncertain",
        "rereview_confidence": "low",
        "disagreement_type": "uncertain",
        "helper_mentioned": "no",
        "valid_helper_action_chain": "unclear",
        "helper_only_mentioned_not_used": "unclear",
        "target_as_helper": "unclear",
        "wrong_helper_type": "unclear",
        "direct_capacity_risk": "unclear",
        "direct_operation_when_tool_needed": "unclear",
        "search_failure_when_helper_not_visible": "unclear",
        "over_tool_use": "unclear",
        "field_plan_inconsistency": "unclear",
        "conditional_helper_only": "unclear",
        "committed_helper_use": "unclear",
        "needs_visual_check": "no",
        "rereview_failure_modes": "",
        "rereview_caveats": "",
        "evidence_quote": extract_evidence_quote(extract_plan_text(row)),
        "rereview_reason": "",
        "auto_failure_types": row.get("auto_failure_types", ""),
        "auto_notes": row.get("auto_notes", ""),
        "parsed_plan": row.get("parsed_plan", ""),
        "parsed_reason": row.get("parsed_reason", ""),
        "raw_response_short": row.get("raw_response_short", ""),
        "raw_response": row.get("raw_response", ""),
        "parsed": row.get("parsed", {}),
        "parse_recoverable": "no",
    }


def label(
    rereview_label: str,
    confidence: str,
    failure_modes: list[str],
    reason: str,
    caveats: list[str] | None = None,
) -> dict[str, str]:
    return {
        "rereview_label": rereview_label,
        "rereview_confidence": confidence,
        "rereview_failure_modes": ";".join(sorted(set(failure_modes))),
        "rereview_caveats": ";".join(sorted(set(caveats or []))),
        "rereview_reason": compact_text(reason, 700),
    }


def finalize_review(review: dict[str, Any], original: dict[str, Any]) -> dict[str, Any]:
    review["disagreement_type"] = disagreement_type(str(original.get("auto_pass_fail", "")), str(review.get("rereview_label", "")))
    return review


def disagreement_type(auto_label: str, review_label: str) -> str:
    if auto_label in {"parse_error", "skipped"} or review_label in {"parse_error", "skipped"}:
        return "auto_parse_or_skip"
    if review_label == "uncertain":
        return "uncertain"
    if auto_label == "pass" and review_label == "true_fail":
        return "auto_pass_but_review_fail"
    if auto_label == "fail" and review_label == "true_pass":
        return "auto_fail_but_review_pass"
    if auto_label == "needs_review" and review_label == "true_pass":
        return "auto_review_resolved_pass"
    if auto_label == "needs_review" and review_label == "true_fail":
        return "auto_review_resolved_fail"
    if (auto_label == "pass" and review_label == "true_pass") or (auto_label == "fail" and review_label == "true_fail"):
        return "consistent"
    return "uncertain"


def _helper_terms(expected_helpers: list[str], selected_helper: str) -> list[str]:
    terms = list(GENERAL_HELPER_KEYWORDS)
    for helper in expected_helpers:
        terms.append(helper)
    if selected_helper and selected_helper.lower() not in {"none", "null", "无", "没有"}:
        terms.append(selected_helper)
    return sorted({term.lower() for term in terms if term}, key=len, reverse=True)


def _has_valid_helper_action_chain(
    plan_steps: list[str],
    chain_steps: list[str],
    helper_terms: list[str],
    target_as_helper: bool,
    expected_helpers: list[str],
    task_id: str,
    task_family: str,
    text: str,
) -> bool:
    if target_as_helper:
        return False
    steps = [str(item).lower() for item in chain_steps + plan_steps]
    if _has_container_collection_chain(plan_steps, chain_steps, text, expected_helpers, task_id, task_family):
        return True
    if task_family == "reach_extension":
        return _has_reach_extension_chain(steps, helper_terms)
    helper_acquired = False
    for step in steps:
        if contains_any(step, NEGATION_KEYWORDS) or _is_conditional_helper_step(step):
            continue
        if contains_any(step, helper_terms) and contains_any(step, HELPER_ACTION_KEYWORDS):
            return True
        if contains_any(step, helper_terms) and contains_any(step, HELPER_ACQUISITION_KEYWORDS):
            helper_acquired = True
            continue
        if helper_acquired and contains_any(step, HELPER_ACTION_KEYWORDS) and contains_any(step, HELPER_REFERENCE_TERMS):
            return True
    return False


def task_family_for(row: dict[str, Any]) -> str:
    task_id = str(row.get("task_id", ""))
    if task_id in {"task_001", "task_002", "task_004", "task_005", "task_007", "task_010"}:
        return "aggregation_transport"
    if task_id in {"task_006", "task_009"}:
        return "cleanup_collection"
    if task_id == "task_008":
        return "reach_extension"
    if task_id == "task_011":
        return "control_no_tool"
    return "generic"


def _has_container_collection_chain(
    plan_steps: list[str],
    chain_steps: list[str],
    text: str,
    expected_helpers: list[str],
    task_id: str,
    task_family: str,
) -> bool:
    if task_family not in {"aggregation_transport", "cleanup_collection"}:
        return False
    expected_text = " ".join(expected_helpers).lower()
    if expected_helpers and not contains_any(expected_text, CONTAINER_TERMS) and task_id not in {"task_006", "task_009"}:
        return False

    steps = [str(item).lower() for item in chain_steps + plan_steps]
    active_steps = [step for step in steps if not contains_any(step, NEGATION_KEYWORDS) and not _is_conditional_helper_step(step)]
    if not active_steps:
        return False

    load_step_found = any(_step_has_container_collection_action(step) for step in active_steps)
    if not load_step_found:
        return False

    if task_family == "cleanup_collection":
        return True

    return any(contains_any(step, CONTAINER_TERMS) and contains_any(step, TRANSPORT_ACTIONS) for step in active_steps)


def _step_has_container_collection_action(step: str) -> bool:
    if not contains_any(step, CONTAINER_TERMS):
        return False
    return contains_any(step, CONTAINER_COLLECTION_ACTIONS)


def _has_reach_extension_chain(steps: list[str], helper_terms: list[str]) -> bool:
    reach_terms = sorted({term.lower() for term in helper_terms + HELPER_GROUPS["reach"] if term}, key=len, reverse=True)
    helper_acquired = False
    for step in steps:
        if contains_any(step, NEGATION_KEYWORDS) or _is_conditional_helper_step(step):
            continue
        if contains_any(step, reach_terms) and contains_any(step, REACH_USE_ACTIONS):
            return True
        if contains_any(step, reach_terms) and contains_any(step, HELPER_ACQUISITION_KEYWORDS):
            helper_acquired = True
            continue
        if helper_acquired and contains_any(step, REACH_USE_ACTIONS) and contains_any(step, HELPER_REFERENCE_TERMS):
            return True
    return False


def _field_plan_inconsistency(parsed: dict[str, Any], valid_chain: bool, selected_helper: str) -> bool:
    helper_needed = str(parsed.get("helper_needed", "")).lower()
    field_claims_helper = helper_needed == "yes" or bool(selected_helper and selected_helper.lower() not in {"none", "null", "无", "没有"})
    return field_claims_helper and not valid_chain


def _conditional_helper_only(
    plan_steps: list[str],
    chain_steps: list[str],
    text: str,
    helper_terms: list[str],
    valid_chain: bool,
) -> bool:
    if valid_chain:
        return False
    steps = [str(item).lower() for item in chain_steps + plan_steps]
    if any(_is_conditional_helper_step(step) and contains_any(step, helper_terms) for step in steps):
        return True
    lowered = text.lower()
    return contains_any(lowered, CONDITIONAL_HELPER_PATTERNS) and contains_any(lowered, helper_terms)


def _is_conditional_helper_step(step: str) -> bool:
    return contains_any(step, CONDITIONAL_HELPER_PATTERNS)


def _wrong_helper_type(text: str, expected_helpers: list[str], valid_chain: bool) -> bool:
    if not valid_chain or not expected_helpers:
        return False
    lowered_expected = {helper.lower() for helper in expected_helpers}
    if lowered_expected.intersection({term.lower() for term in HELPER_GROUPS["aggregation"]}):
        return False
    if lowered_expected.intersection({"broom", "stick", "rod"}):
        return contains_any(text, HELPER_GROUPS["aggregation"]) and not contains_any(text, HELPER_GROUPS["reach"])
    if lowered_expected.intersection({"tissue", "cloth", "dustpan"}):
        return contains_any(text, HELPER_GROUPS["aggregation"]) and not contains_any(text, HELPER_GROUPS["cleaning"])
    return False


def _needs_visual_check(row: dict[str, Any], helper_mentioned: bool, valid_chain: bool) -> bool:
    if str(row.get("parse_status", "")) != "ok":
        return False
    if str(row.get("prompt_category", "")) == "diagnostic_probe":
        return False
    expected_helper = _bool_value(row.get("expected_should_use_tool_or_container"))
    if expected_helper and helper_mentioned and not valid_chain:
        return True
    return False


def _bool_value(value: Any) -> bool:
    if isinstance(value, bool):
        return value
    return str(value).strip().lower() in {"true", "1", "yes", "y", "是"}


def _matches_any(value: str, terms: list[str]) -> bool:
    lowered = value.lower()
    return any(term and (term.lower() == lowered or term.lower() in lowered or lowered in term.lower()) for term in terms)


def _looks_parse_recoverable(raw_text: str) -> bool:
    text = raw_text.lower()
    if not raw_text.strip():
        return False
    return contains_any(text, ["plan", "step", "步骤", "计划", "抓取", "移动", "使用", "carry", "move"])


def tri(value: bool) -> str:
    return "yes" if value else "no"


def write_disagreements(path: Path, rows: list[dict[str, Any]]) -> None:
    selected = [row for row in rows if row["disagreement_type"] not in {"consistent", "auto_parse_or_skip"}]
    grouped: dict[tuple[str, str], list[dict[str, Any]]] = defaultdict(list)
    for row in selected:
        grouped[(str(row["task_id"]), str(row["prompt_category"]))].append(row)
    lines = ["# Rereview Disagreements", ""]
    if not selected:
        lines.append("No non-parse disagreements found.")
    for (task_id, category), group in sorted(grouped.items()):
        lines.extend([f"## {task_id} / {category}", ""])
        for row in group:
            lines.append(
                f"- {row['model_id']} / {row['prompt_id']}: auto={row['auto_pass_fail']} "
                f"review={row['rereview_label']} ({row['disagreement_type']}). "
                f"Evidence: {row['evidence_quote']} Reason: {row['rereview_reason']}"
            )
        lines.append("")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_high_confidence_cases(path: Path, rows: list[dict[str, Any]]) -> None:
    lines = ["# High Confidence Cases", ""]
    sections = [
        ("Clean counterexample candidates", lambda row: row["primary_for_counterexample"] in {True, "True", "true"} and row["rereview_label"] == "true_fail"),
        ("Tool-prior intervention successes", lambda row: row["prompt_category"] == "tool_prior_intervention" and row["rereview_label"] == "true_pass"),
        ("Structured diagnostic cases", lambda row: row["prompt_category"] == "diagnostic_probe" and row["rereview_confidence"] == "high"),
        ("Robust failures", lambda row: row["rereview_label"] == "true_fail" and row["rereview_confidence"] == "high"),
    ]
    for title, predicate in sections:
        lines.extend([f"## {title}", ""])
        subset = [row for row in rows if predicate(row) and row["rereview_confidence"] == "high"]
        if not subset:
            lines.append("- None in this subset.")
        for row in subset[:80]:
            lines.append(
                f"- {row['task_id']} / {row['image_name']} / {row['model_id']} / {row['prompt_id']}: "
                f"{row['rereview_label']} [{row['rereview_failure_modes']}]. {row['rereview_reason']}"
            )
        lines.append("")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_uncertain_cases(path: Path, rows: list[dict[str, Any]]) -> None:
    selected = [
        row for row in rows
        if row["rereview_label"] == "uncertain"
        or row["needs_visual_check"] == "yes"
        or row["rereview_confidence"] == "low"
        or row.get("parse_recoverable") == "yes"
        or row["field_plan_inconsistency"] == "yes"
    ]
    lines = ["# Uncertain Cases For Human Review", ""]
    if not selected:
        lines.append("No uncertain cases in this subset.")
    for row in selected[:150]:
        lines.append(
            f"- {row['task_id']} / {row['image_name']} / {row['model_id']} / {row['prompt_id']}: "
            f"label={row['rereview_label']} confidence={row['rereview_confidence']} "
            f"visual={row['needs_visual_check']} parse_recoverable={row.get('parse_recoverable', 'no')}. "
            f"Reason: {row['rereview_reason']} Evidence: {row['evidence_quote']}"
        )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def run_self_test() -> None:
    tests = [
        ("direct carry all", synthetic_row("grab all four bottles directly and carry them in one trip"), "true_fail"),
        ("selected helper no use", synthetic_row("carry the water bottles to the bedroom", selected_helper="tray"), "true_fail"),
        ("avoid rod", synthetic_remote_row("avoid the white rod-like object; grasp the remote directly"), "true_fail"),
        ("valid tray", synthetic_row("find a tray; place bottles on the tray; carry the tray to bedroom"), "true_pass"),
        ("conditional direct tray", synthetic_row("carry bottles directly, or find a tray if available"), "true_fail"),
        ("valid pronoun tray", synthetic_row("find a tray; place the bottles on it; carry it to bedroom"), "true_pass"),
        ("try tray only", synthetic_row("try to use a tray if available"), "true_fail"),
        ("chinese cleanup basket", synthetic_cleanup_row("逐个拾取地上的小物品，并将其放置到白色收纳篮内。"), "true_pass"),
        ("chinese tray transport", synthetic_row("找到托盘；把水瓶放到托盘上；端起托盘送到卧室。"), "true_pass"),
        ("chinese conditional tray", synthetic_row("逐个搬运水瓶，必要时可以考虑寻找托盘。"), "true_fail"),
        ("valid reach rod", synthetic_remote_row("找到长杆；用长杆把沙发下的遥控器拨出来；再用夹爪抓取遥控器。"), "true_pass"),
        ("direct reach fail", synthetic_remote_row("直接把机械臂伸进沙发下抓取遥控器。"), "true_fail"),
        ("single bottle direct pass", synthetic_single_bottle_row("直接拿起桌上的单个水瓶并递给用户。"), "true_pass"),
        ("over tool use", synthetic_single_bottle_row("find a tray; place the bottle on the tray; carry the tray to user"), "true_fail"),
        ("parse error", {**synthetic_row("", parse_status="parse_error"), "raw_response": ""}, "parse_error"),
        ("skipped", {**synthetic_row(""), "auto_pass_fail": "skipped"}, "skipped"),
    ]
    failures: list[str] = []
    for name, row, expected in tests:
        reviewed = rereview_row(row)
        if reviewed["rereview_label"] != expected:
            failures.append(f"{name}: expected {expected}, got {reviewed['rereview_label']} ({reviewed['rereview_reason']})")
    if failures:
        raise SystemExit("\n".join(failures))


def synthetic_row(plan: str, selected_helper: str = "", parse_status: str = "ok") -> dict[str, Any]:
    parsed = {"plan": [plan], "selected_helper": selected_helper, "estimated_number_of_trips": "single"}
    return {
        "run_id": "self_test",
        "task_id": "task_001",
        "task_name": "water",
        "image_name": "image.jpg",
        "model_id": "model",
        "prompt_id": "prompt",
        "prompt_category": "generic_clean",
        "prompt_type": "primary_clean",
        "embodiment_profile": "generic",
        "primary_for_counterexample": True,
        "auto_pass_fail": "pass",
        "parse_status": parse_status,
        "parsed": parsed if parse_status == "ok" else {},
        "parsed_plan": plan,
        "parsed_selected_helper": selected_helper,
        "raw_response": plan,
        "raw_response_short": plan,
        "expected_should_use_tool_or_container": True,
        "expected_tool_or_container_types": ["tray", "bag", "box", "basket"],
        "expected_should_search_for_tool_if_not_visible": False,
        "expected_should_avoid_over_tool_use": False,
        "target_object_terms": ["water", "bottle", "bottles"],
    }


def synthetic_remote_row(plan: str) -> dict[str, Any]:
    row = synthetic_row(plan)
    row.update(
        {
            "task_id": "task_008",
            "expected_tool_or_container_types": ["broom", "stick", "rod"],
            "target_object_terms": ["remote", "remote control"],
        }
    )
    return row


def synthetic_cleanup_row(plan: str) -> dict[str, Any]:
    row = synthetic_row(plan)
    row.update(
        {
            "task_id": "task_006",
            "task_name": "small objects",
            "expected_tool_or_container_types": ["box", "basket", "dustpan", "container", "盒子", "收纳篮"],
            "target_object_terms": ["small objects", "小物品", "objects"],
        }
    )
    return row


def synthetic_single_bottle_row(plan: str) -> dict[str, Any]:
    row = synthetic_row(plan)
    row.update(
        {
            "task_id": "task_011",
            "expected_should_use_tool_or_container": False,
            "expected_tool_or_container_types": [],
            "expected_should_avoid_over_tool_use": True,
            "target_object_terms": ["water", "bottle"],
        }
    )
    return row


if __name__ == "__main__":
    main()
