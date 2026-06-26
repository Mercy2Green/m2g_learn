from __future__ import annotations

from collections import defaultdict
from typing import Any


FAILURE_TAXONOMY: dict[str, str] = {
    "F1_aggregation_failure": "多物体搬运时不会使用托盘、袋子、箱子、篮子等聚合工具。",
    "F2_tool_search_failure": "当前视野没有容器/工具时，不会主动提出短程搜索附近是否有可用辅助物。",
    "F3_efficiency_blind_planning": "只要能完成就行，不考虑往返次数、时间、路线成本。",
    "F4_container_affordance_miss": "图像中存在明显容器/托盘/袋子/箱子，但模型不把它用于搬运。",
    "F5_wrong_tool_or_container_choice": "选择太小、不稳、不合适或与任务不匹配的工具/容器。",
    "F6_tool_necessity_miss": "需要工具/容器才高效或可行时，仍直接操作。",
    "F7_over_tool_use": "工具存在但任务很简单，直接操作更合理时，仍多余使用工具。",
    "F8_physical_stability_miss": "没考虑多物体堆放、液体、易碎、倾倒风险。",
    "F9_long_horizon_decomposition_miss": "缺少'先拿容器/工具，再装载/操作，再运送/完成'的任务分解。",
    "F10_search_or_fallback_miss": "工具不可见、不可用或不合适时，不提出替代方案。",
}


GENERAL_HELPER_KEYWORDS = [
    "工具",
    "辅助物",
    "容器",
    "托盘",
    "盘子",
    "袋子",
    "箱子",
    "盒子",
    "篮子",
    "背包",
    "洗衣篮",
    "收纳箱",
    "扫把",
    "簸箕",
    "抹布",
    "纸巾",
    "长杆",
    "杆子",
    "tool",
    "helper",
    "container",
    "tray",
    "bag",
    "box",
    "basket",
    "backpack",
    "broom",
    "dustpan",
    "cloth",
    "tissue",
    "rod",
    "stick",
]
HELPER_TYPE_SYNONYMS = {
    "tray": ["托盘", "tray"],
    "bag": ["袋子", "包", "bag"],
    "box": ["箱子", "盒子", "box"],
    "basket": ["篮子", "basket"],
    "backpack": ["背包", "backpack"],
    "basin": ["盆", "basin"],
    "dustpan": ["簸箕", "dustpan"],
    "broom": ["扫把", "broom"],
    "laundry basket": ["洗衣篮", "laundry basket"],
    "storage box": ["收纳箱", "storage box"],
    "stick": ["长杆", "杆子", "stick"],
    "rod": ["长杆", "杆子", "rod"],
    "tissue": ["纸巾", "tissue"],
    "cloth": ["抹布", "cloth"],
    "padded box": ["软垫", "padded box"],
}
SEARCH_KEYWORDS = ["寻找", "查找", "检查附近", "查看附近", "搜索附近", "附近是否", "look for", "search nearby", "check nearby"]
ONE_BY_ONE_KEYWORDS = ["逐个", "一个个", "一瓶一瓶", "一件一件", "每次一个", "one by one", "one-by-one", "each item"]
DIRECT_ONLY_KEYWORDS = ["直接抓取", "直接拿", "逐个抓取", "直接夹取", "directly grasp", "pick up directly"]


def evaluate_response(
    task: dict[str, Any],
    parsed_record: dict[str, Any],
    model: dict[str, Any],
    prompt: dict[str, Any],
    image_path: str,
) -> dict[str, Any]:
    primary = bool(prompt.get("primary_for_counterexample", False))
    base = {
        "task_id": task.get("task_id", ""),
        "task_name": task.get("name", ""),
        "image_path": image_path,
        "model_id": model.get("model_id", ""),
        "provider": model.get("provider", ""),
        "provider_label": model.get("provider_label", model.get("provider", "")),
        "model_name": model.get("model_name", ""),
        "strength_role": model.get("strength_role", ""),
        "prompt_id": prompt.get("prompt_id", ""),
        "prompt_type": "primary_clean" if primary else "structured_probe",
        "primary_for_counterexample": primary,
        "pass_fail": "needs_review",
        "failure_types_detected": [],
        "counterexample_strength_hint": "invalid_or_unclear",
        "inferred_uses_helper": "unknown",
        "inferred_searches_helper": "unknown",
        "inferred_one_by_one": "no",
        "plan_summary": "",
        "notes": "",
    }

    if parsed_record.get("parse_status") != "ok":
        base.update(
            {
                "pass_fail": "parse_error",
                "notes": parsed_record.get("parse_error", "parse_error"),
            }
        )
        return base

    parsed = parsed_record.get("parsed", {})
    expected = task.get("expected_behavior", {})
    failures: list[str] = []
    notes: list[str] = []
    inference = infer_helper_use_from_plan(parsed, task)
    base.update(inference)
    base["plan_summary"] = "; ".join(parsed.get("plan", []))[:500]

    if primary:
        uses_helper = inference["inferred_uses_helper"]
        searches_helper = inference["inferred_searches_helper"]
        one_by_one = inference["inferred_one_by_one"] == "yes"
    else:
        uses_helper = parsed.get("uses_tool_or_container", "unknown")
        searches_helper = parsed.get("will_search_for_tool_if_not_visible", "unknown")
        one_by_one = inference["inferred_one_by_one"] == "yes"
        notes.append("Structured probe: diagnostic only, not clean counterexample evidence.")

    trips = parsed.get("estimated_number_of_trips", "unknown")

    if expected.get("should_use_tool_or_container") is True:
        if uses_helper == "no":
            failures.extend(_task_failures(task, ["F1_aggregation_failure", "F4_container_affordance_miss", "F6_tool_necessity_miss"]))
            notes.append("Expected helper use, but plan does not indicate one.")
        elif uses_helper == "unknown":
            notes.append("Helper use is unclear from plan text.")

    if expected.get("should_search_for_tool_if_not_visible") is True:
        if searches_helper == "no":
            failures.extend(_task_failures(task, ["F2_tool_search_failure", "F10_search_or_fallback_miss"]))
            notes.append("Expected nearby search when no helper is visible, but plan does not indicate search.")
        elif searches_helper == "unknown":
            notes.append("Search behavior is unclear from plan text.")

    if expected.get("expected_trip_pattern") == "single_or_few_trips":
        if trips == "multiple" or one_by_one:
            failures.extend(_task_failures(task, ["F1_aggregation_failure", "F3_efficiency_blind_planning"]))
            notes.append("Expected single/few trips, but plan indicates multiple or one-by-one handling.")
        elif trips == "unknown":
            notes.append("Trip count is unclear.")

    if expected.get("should_avoid_over_tool_use") is True and uses_helper == "yes":
        failures.append("F7_over_tool_use")
        notes.append("Expected direct action, but plan indicates unnecessary helper use.")

    failures = sorted(set(failures))
    if failures:
        base["pass_fail"] = "fail"
        base["counterexample_strength_hint"] = "weak_candidate" if primary else "invalid_or_unclear"
    elif notes and any("unclear" in note.lower() or "不清楚" in note for note in notes):
        base["pass_fail"] = "needs_review"
    else:
        base["pass_fail"] = "pass"

    base["failure_types_detected"] = failures
    base["notes"] = " ".join(notes) if notes else "Automatic first-pass check passed."
    return base


def infer_helper_use_from_plan(parsed: dict[str, Any], task: dict[str, Any]) -> dict[str, str]:
    text = _combined_plan_text(parsed)
    helper_keywords = _helper_keywords_for_task(task)
    has_helper = any(keyword.lower() in text for keyword in helper_keywords)
    has_search = any(keyword.lower() in text for keyword in SEARCH_KEYWORDS)
    one_by_one = any(keyword.lower() in text for keyword in ONE_BY_ONE_KEYWORDS)
    direct_only = any(keyword.lower() in text for keyword in DIRECT_ONLY_KEYWORDS)

    if has_helper:
        inferred_uses_helper = "yes"
    elif one_by_one or direct_only:
        inferred_uses_helper = "no"
    else:
        inferred_uses_helper = "unknown"

    return {
        "inferred_uses_helper": inferred_uses_helper,
        "inferred_searches_helper": "yes" if has_search else "no",
        "inferred_one_by_one": "yes" if one_by_one else "no",
    }


def assign_counterexample_strength(evaluations: list[dict[str, Any]]) -> list[dict[str, Any]]:
    grouped: dict[tuple[str, str, str], list[dict[str, Any]]] = defaultdict(list)
    for row in evaluations:
        key = (row.get("task_id", ""), row.get("image_path", ""), row.get("prompt_id", ""))
        grouped[key].append(row)

    for rows in grouped.values():
        primary_rows = [row for row in rows if row.get("primary_for_counterexample") is True]
        non_mock_rows = [row for row in primary_rows if row.get("strength_role") != "mock"]
        qwen_failed = any(row.get("strength_role") == "qwen_main" and row.get("pass_fail") == "fail" for row in non_mock_rows)
        other_non_mock_failed = any(
            row.get("strength_role") not in {"qwen_main", "mock"} and row.get("pass_fail") == "fail" for row in non_mock_rows
        )
        other_non_qwen_passed = any(
            row.get("strength_role") not in {"qwen_main", "mock"} and row.get("pass_fail") == "pass" for row in non_mock_rows
        )
        failed_non_mock_count = sum(1 for row in non_mock_rows if row.get("pass_fail") == "fail")

        for row in rows:
            if row.get("pass_fail") != "fail" or row.get("primary_for_counterexample") is not True or row.get("strength_role") == "mock":
                row["counterexample_strength_hint"] = "invalid_or_unclear"
            elif qwen_failed and other_non_mock_failed:
                row["counterexample_strength_hint"] = "strong_candidate"
            elif qwen_failed and other_non_qwen_passed:
                row["counterexample_strength_hint"] = "medium_candidate"
            elif failed_non_mock_count == 1:
                row["counterexample_strength_hint"] = "weak_candidate"
            else:
                row["counterexample_strength_hint"] = "invalid_or_unclear"
    return evaluations


def _combined_plan_text(parsed: dict[str, Any]) -> str:
    pieces: list[str] = []
    pieces.extend(parsed.get("plan", []))
    for key in [
        "task_understanding",
        "tool_or_container",
        "efficiency_consideration",
        "safety_or_stability_consideration",
        "uncertainty_or_missing_information",
        "reason",
        "failure_risk",
    ]:
        value = parsed.get(key)
        if value:
            pieces.append(str(value))
    return " ".join(pieces).lower()


def _helper_keywords_for_task(task: dict[str, Any]) -> list[str]:
    expected_types = task.get("expected_behavior", {}).get("expected_tool_or_container_types", []) or []
    keywords = list(GENERAL_HELPER_KEYWORDS)
    for helper_type in expected_types:
        helper_text = str(helper_type)
        keywords.append(helper_text)
        keywords.extend(HELPER_TYPE_SYNONYMS.get(helper_text, []))
    return sorted({keyword for keyword in keywords if keyword})


def _task_failures(task: dict[str, Any], candidates: list[str]) -> list[str]:
    configured = set(task.get("failure_types", []))
    return [failure for failure in candidates if failure in configured] or candidates[:1]
