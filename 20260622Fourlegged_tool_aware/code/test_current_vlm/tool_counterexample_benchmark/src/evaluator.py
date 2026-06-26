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


def evaluate_response(
    task: dict[str, Any],
    parsed_record: dict[str, Any],
    model: dict[str, Any],
    prompt: dict[str, Any],
    image_path: str,
) -> dict[str, Any]:
    base = {
        "task_id": task.get("task_id", ""),
        "task_name": task.get("name", ""),
        "image_path": image_path,
        "model_id": model.get("model_id", ""),
        "provider": model.get("provider", ""),
        "prompt_id": prompt.get("prompt_id", ""),
        "pass_fail": "needs_review",
        "failure_types_detected": [],
        "counterexample_strength_hint": "invalid_or_unclear",
        "notes": "",
    }

    if parsed_record.get("parse_status") != "ok":
        base.update(
            {
                "pass_fail": "parse_error",
                "failure_types_detected": [],
                "counterexample_strength_hint": "invalid_or_unclear",
                "notes": parsed_record.get("parse_error", "parse_error"),
            }
        )
        return base

    parsed = parsed_record.get("parsed", {})
    expected = task.get("expected_behavior", {})
    failures: list[str] = []
    notes: list[str] = []

    uses_tool = parsed.get("uses_tool_or_container", "unknown")
    searches = parsed.get("will_search_for_tool_if_not_visible", "unknown")
    trips = parsed.get("estimated_number_of_trips", "unknown")
    plan_text = " ".join(parsed.get("plan", [])).lower()

    if expected.get("should_use_tool_or_container") is True:
        if uses_tool == "no":
            failures.extend(_task_failures(task, ["F1_aggregation_failure", "F4_container_affordance_miss", "F6_tool_necessity_miss"]))
            notes.append("Expected tool/container use, but model said no.")
        elif uses_tool == "unknown":
            notes.append("Tool/container use is unclear.")

    if expected.get("should_search_for_tool_if_not_visible") is True:
        if searches == "no":
            failures.extend(_task_failures(task, ["F2_tool_search_failure", "F10_search_or_fallback_miss"]))
            notes.append("Expected short-range search when helper is not visible, but model said no.")
        elif searches == "unknown":
            notes.append("Search behavior is unclear.")

    if expected.get("expected_trip_pattern") == "single_or_few_trips":
        if trips == "multiple" or _looks_like_one_by_one(plan_text):
            failures.extend(_task_failures(task, ["F1_aggregation_failure", "F3_efficiency_blind_planning"]))
            notes.append("Expected single/few trips, but model indicates multiple or one-by-one handling.")
        elif trips == "unknown":
            notes.append("Trip count is unclear.")

    if expected.get("should_avoid_over_tool_use") is True and uses_tool == "yes":
        failures.append("F7_over_tool_use")
        notes.append("Expected direct action, but model used a tool/container.")

    failures = sorted(set(failures))
    if failures:
        base["pass_fail"] = "fail"
        base["counterexample_strength_hint"] = "weak_candidate"
    elif notes:
        base["pass_fail"] = "needs_review"
    else:
        base["pass_fail"] = "pass"

    base["failure_types_detected"] = failures
    base["notes"] = " ".join(notes) if notes else "Heuristic check passed."
    return base


def assign_counterexample_strength(evaluations: list[dict[str, Any]]) -> list[dict[str, Any]]:
    grouped: dict[tuple[str, str, str], list[dict[str, Any]]] = defaultdict(list)
    for row in evaluations:
        key = (row.get("task_id", ""), row.get("image_path", ""), row.get("prompt_id", ""))
        grouped[key].append(row)

    for rows in grouped.values():
        qwen_failed = any(row.get("provider") == "qwen" and row.get("pass_fail") == "fail" for row in rows)
        closed_failed = any(row.get("provider") in {"openai", "gemini"} and row.get("pass_fail") == "fail" for row in rows)
        closed_passed = any(row.get("provider") in {"openai", "gemini"} and row.get("pass_fail") == "pass" for row in rows)
        any_failed = any(row.get("pass_fail") == "fail" for row in rows)
        for row in rows:
            if row.get("pass_fail") != "fail":
                row["counterexample_strength_hint"] = "invalid_or_unclear"
            elif qwen_failed and closed_failed:
                row["counterexample_strength_hint"] = "strong_candidate"
            elif qwen_failed and closed_passed:
                row["counterexample_strength_hint"] = "medium_candidate"
            elif any_failed:
                row["counterexample_strength_hint"] = "weak_candidate"
            else:
                row["counterexample_strength_hint"] = "invalid_or_unclear"
    return evaluations


def _task_failures(task: dict[str, Any], candidates: list[str]) -> list[str]:
    configured = set(task.get("failure_types", []))
    return [failure for failure in candidates if failure in configured] or candidates[:1]


def _looks_like_one_by_one(plan_text: str) -> bool:
    markers = ["逐个", "一个个", "一瓶一瓶", "一件一件", "one by one", "one-by-one", "each item"]
    return any(marker in plan_text for marker in markers)
