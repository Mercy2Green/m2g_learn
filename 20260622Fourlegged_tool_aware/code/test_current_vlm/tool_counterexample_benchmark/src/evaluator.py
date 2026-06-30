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
    "工具", "辅助物", "容器", "托盘", "袋子", "箱子", "盒子", "篮子", "背包", "洗衣篮", "收纳箱",
    "扫把", "簸箕", "抹布", "纸巾", "长杆", "杆子", "tool", "helper", "container", "tray", "bag",
    "box", "basket", "backpack", "broom", "dustpan", "cloth", "tissue", "rod", "stick",
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
DIRECT_ONLY_KEYWORDS = [
    "直接抓取",
    "直接拿",
    "直接夹取",
    "直接用夹爪",
    "直接拾取",
    "directly grasp",
    "grasp directly",
    "grasp the remote directly",
    "pick up directly",
    "directly pick",
    "use the gripper to pick",
]
DIRECT_CARRY_ALL_KEYWORDS = [
    "拿起所有", "抓起所有", "直接拿所有", "一次拿完", "一次性直接拿", "直接搬运所有", "全部直接拿",
    "grab all", "carry all", "pick up all", "carry them all", "hold all", "all four", "all bottles",
]
VALID_HELPER_ACTION_KEYWORDS = [
    "放入", "放进", "装入", "装进", "装载", "承载", "托着", "端起", "搬运", "运送", "收集", "盛放",
    "拨出", "拨出来", "拉出", "推出来", "勾出", "扫出", "擦拭", "清理", "清扫", "使用", "用",
    "place", "put", "load", "carry", "transport", "deliver", "collect", "gather", "push", "pull",
    "hook", "sweep", "wipe", "clean", "use",
]
NEGATED_MENTION_PATTERNS = ["avoid", "避开", "不要碰", "not use", "不用", "不使用", "ignore", "忽略"]


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
        "supports_vision": model.get("supports_vision", ""),
        "prompt_id": prompt.get("prompt_id", ""),
        "embodiment_profile": prompt.get("embodiment_profile", "generic"),
        "prompt_category": prompt.get("prompt_category", ""),
        "prompt_type": _prompt_type_for(prompt),
        "primary_for_counterexample": primary,
        "pass_fail": "needs_review",
        "failure_types_detected": [],
        "counterexample_strength_hint": "invalid_or_unclear",
        "inferred_uses_helper": "unknown",
        "inferred_searches_helper": "unknown",
        "inferred_one_by_one": "no",
        "inferred_helper_mentioned": "no",
        "inferred_valid_helper_action_chain": "no",
        "inferred_target_as_helper": "no",
        "inferred_selected_helper": "",
        "inferred_direct_carry_capacity_risk": "no",
        "inferred_physical_feasibility_risk": "",
        "plan_summary": "",
        "notes": "",
    }

    if parsed_record.get("parse_status") != "ok":
        base.update({"pass_fail": "parse_error", "notes": parsed_record.get("parse_error", "parse_error")})
        return base

    parsed = parsed_record.get("parsed", {})
    expected = task.get("expected_behavior", {})
    failures: list[str] = []
    notes: list[str] = []
    inference = infer_helper_use_from_plan(parsed, task)
    base.update(inference)
    base["plan_summary"] = "; ".join(parsed.get("plan", []))[:500]

    searches_helper = inference["inferred_searches_helper"]
    one_by_one = inference["inferred_one_by_one"] == "yes"
    valid_chain = inference["inferred_valid_helper_action_chain"] == "yes"
    helper_mentioned = inference["inferred_helper_mentioned"] == "yes"
    target_as_helper = inference["inferred_target_as_helper"] == "yes"
    direct_capacity_risk = inference["inferred_direct_carry_capacity_risk"] == "yes"
    direct_operation = inference.get("inferred_direct_operation", "no") == "yes"
    trips = parsed.get("estimated_number_of_trips", "unknown")

    if not primary:
        category = str(prompt.get("prompt_category", ""))
        if category == "diagnostic_probe":
            notes.append("Structured/action-chain probe: diagnostic only, not clean counterexample evidence.")
        elif category == "tool_prior_intervention":
            notes.append(
                "Tool-prior intervention prompt: not clean counterexample evidence; use for prompted helper-awareness analysis."
            )
        else:
            notes.append("Non-primary prompt: not clean counterexample evidence.")

    if expected.get("should_use_tool_or_container") is True:
        if target_as_helper:
            failures.extend(_task_failures(task, ["F1_aggregation_failure", "F4_container_affordance_miss"]))
            notes.append("Selected helper appears to be a target object, not a valid helper.")
        elif valid_chain:
            pass
        elif direct_capacity_risk:
            failures.extend(_task_failures(task, ["F1_aggregation_failure", "F3_efficiency_blind_planning", "F8_physical_stability_miss"]))
            notes.append("Plan appears to directly carry many loose objects without a valid helper/action chain.")
        elif helper_mentioned and direct_operation:
            failures.extend(_task_failures(task, ["F6_tool_necessity_miss", "F4_container_affordance_miss"]))
            notes.append("Helper is only mentioned, but the plan directly operates on the target without a valid helper action chain.")
        elif helper_mentioned:
            notes.append("Helper is mentioned, but no valid helper action chain is evident; manual review needed.")
        else:
            failures.extend(_task_failures(task, ["F1_aggregation_failure", "F4_container_affordance_miss", "F6_tool_necessity_miss"]))
            notes.append("Expected helper use, but no valid helper action chain is evident.")

    if expected.get("should_search_for_tool_if_not_visible") is True:
        if searches_helper == "no" and not valid_chain:
            failures.extend(_task_failures(task, ["F2_tool_search_failure", "F10_search_or_fallback_miss"]))
            notes.append("Expected nearby search when no helper is visible, but plan does not indicate search.")
        elif searches_helper == "unknown":
            notes.append("Search behavior is unclear from plan text.")

    if expected.get("expected_trip_pattern") == "single_or_few_trips":
        if trips == "multiple" or one_by_one:
            failures.extend(_task_failures(task, ["F1_aggregation_failure", "F3_efficiency_blind_planning"]))
            notes.append("Expected single/few trips, but plan indicates multiple or one-by-one handling.")
        elif trips == "single" and direct_capacity_risk:
            failures.extend(_task_failures(task, ["F1_aggregation_failure", "F3_efficiency_blind_planning", "F8_physical_stability_miss"]))
            notes.append("Single-trip claim has physical capacity risk without valid helper action chain.")
        elif trips == "unknown":
            notes.append("Trip count is unclear.")

    if expected.get("should_avoid_over_tool_use") is True and valid_chain:
        failures.append("F7_over_tool_use")
        notes.append("Expected direct action, but plan has a valid helper action chain.")

    failures = sorted(set(failures))
    if failures:
        base["pass_fail"] = "fail"
        base["counterexample_strength_hint"] = "weak_candidate" if primary else "invalid_or_unclear"
    elif notes and any("unclear" in note.lower() or "manual review" in note.lower() for note in notes):
        base["pass_fail"] = "needs_review"
    else:
        base["pass_fail"] = "pass"

    base["failure_types_detected"] = failures
    base["notes"] = " ".join(notes) if notes else "Automatic first-pass check passed."
    return base


def infer_helper_use_from_plan(parsed: dict[str, Any], task: dict[str, Any]) -> dict[str, str]:
    text = _combined_plan_text(parsed)
    helper_keywords = _helper_keywords_for_task(task)
    selected_helper = _selected_helper(parsed)
    target_terms = _target_terms_for_task(task)

    helper_mentioned = any(keyword.lower() in text for keyword in helper_keywords) or bool(selected_helper)
    target_as_helper = bool(selected_helper) and _matches_any(selected_helper, target_terms)
    search = any(keyword.lower() in text for keyword in SEARCH_KEYWORDS)
    one_by_one = any(keyword.lower() in text for keyword in ONE_BY_ONE_KEYWORDS)
    direct_operation = any(keyword.lower() in text for keyword in DIRECT_ONLY_KEYWORDS)
    direct_capacity_risk = _has_direct_capacity_risk(text)
    valid_chain = _has_valid_helper_action_chain(parsed, helper_keywords, selected_helper, target_as_helper)

    if target_as_helper:
        uses_helper = "no"
    elif valid_chain:
        uses_helper = "yes"
    elif direct_capacity_risk or direct_operation or one_by_one:
        uses_helper = "no"
    elif helper_mentioned:
        uses_helper = "unknown"
    else:
        uses_helper = "unknown"

    return {
        "inferred_uses_helper": uses_helper,
        "inferred_searches_helper": "yes" if search else "no",
        "inferred_one_by_one": "yes" if one_by_one else "no",
        "inferred_helper_mentioned": "yes" if helper_mentioned else "no",
        "inferred_valid_helper_action_chain": "yes" if valid_chain else "no",
        "inferred_target_as_helper": "yes" if target_as_helper else "no",
        "inferred_selected_helper": selected_helper,
        "inferred_direct_carry_capacity_risk": "yes" if direct_capacity_risk else "no",
        "inferred_physical_feasibility_risk": "direct_carry_capacity_risk" if direct_capacity_risk else str(parsed.get("physical_feasibility_risk", "")),
        "inferred_direct_operation": "yes" if direct_operation else "no",
    }


def _prompt_type_for(prompt: dict[str, Any]) -> str:
    if prompt.get("primary_for_counterexample", False):
        return "primary_clean"
    category = str(prompt.get("prompt_category", ""))
    if category == "diagnostic_probe":
        return "structured_probe"
    if category == "tool_prior_intervention":
        return "tool_prior_intervention"
    return category or "non_primary"


def assign_counterexample_strength(evaluations: list[dict[str, Any]]) -> list[dict[str, Any]]:
    grouped: dict[tuple[str, str, str], list[dict[str, Any]]] = defaultdict(list)
    for row in evaluations:
        key = (row.get("task_id", ""), row.get("image_path", ""), row.get("prompt_id", ""))
        grouped[key].append(row)

    for rows in grouped.values():
        evidence_rows = [
            row for row in rows
            if row.get("primary_for_counterexample") is True
            and row.get("strength_role") != "mock"
            and row.get("pass_fail") in {"pass", "fail"}
        ]
        qwen_failed = any(row.get("strength_role") == "qwen_main" and row.get("pass_fail") == "fail" for row in evidence_rows)
        other_non_mock_failed = any(
            row.get("strength_role") not in {"qwen_main", "mock"} and row.get("pass_fail") == "fail" for row in evidence_rows
        )
        other_non_qwen_passed = any(
            row.get("strength_role") not in {"qwen_main", "mock"} and row.get("pass_fail") == "pass" for row in evidence_rows
        )
        failed_count = sum(1 for row in evidence_rows if row.get("pass_fail") == "fail")

        for row in rows:
            if row.get("pass_fail") != "fail" or row.get("primary_for_counterexample") is not True or row.get("strength_role") == "mock":
                row["counterexample_strength_hint"] = "invalid_or_unclear"
            elif qwen_failed and other_non_mock_failed:
                row["counterexample_strength_hint"] = "strong_candidate"
            elif qwen_failed and other_non_qwen_passed:
                row["counterexample_strength_hint"] = "medium_candidate"
            elif failed_count == 1:
                row["counterexample_strength_hint"] = "weak_candidate"
            else:
                row["counterexample_strength_hint"] = "invalid_or_unclear"
    return evaluations


def _combined_plan_text(parsed: dict[str, Any]) -> str:
    pieces: list[str] = []
    for key in ["plan", "target_objects", "visible_helper_objects", "tool_use_action_chain"]:
        pieces.extend(parsed.get(key, []))
    for key in [
        "task_understanding", "tool_or_container", "selected_helper", "helper_purpose", "efficiency_consideration",
        "safety_or_stability_consideration", "physical_feasibility_risk", "uncertainty_or_missing_information",
        "reason", "failure_risk",
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


def _target_terms_for_task(task: dict[str, Any]) -> list[str]:
    return [str(term).lower() for term in task.get("expected_behavior", {}).get("target_object_terms", []) if term]


def _selected_helper(parsed: dict[str, Any]) -> str:
    selected = str(parsed.get("selected_helper") or parsed.get("tool_or_container") or "").strip()
    if selected.lower() in {"none", "null", "无", "没有", "string or none"}:
        return ""
    return selected


def _matches_any(value: str, terms: list[str]) -> bool:
    lowered = value.lower()
    return any(term and (term == lowered or term in lowered or lowered in term) for term in terms)


def _has_direct_capacity_risk(text: str) -> bool:
    return any(keyword.lower() in text for keyword in DIRECT_CARRY_ALL_KEYWORDS)


def _has_valid_helper_action_chain(
    parsed: dict[str, Any],
    helper_keywords: list[str],
    selected_helper: str,
    target_as_helper: bool,
) -> bool:
    if target_as_helper:
        return False
    helper_terms = [term for term in helper_keywords if term]
    if selected_helper:
        helper_terms.append(selected_helper)
    helper_terms = sorted({term.lower() for term in helper_terms if term}, key=len, reverse=True)
    if not helper_terms:
        return False

    chain_steps = _normalized_steps(parsed.get("tool_use_action_chain", []))
    plan_steps = _normalized_steps(parsed.get("plan", []))

    for step in chain_steps:
        if _step_has_helper_and_action(step, helper_terms) and not _has_negated_helper_mention(step):
            return True

    for step in plan_steps:
        if _step_has_helper_and_action(step, helper_terms) and not _has_negated_helper_mention(step):
            return True

    return _has_conservative_helper_sequence(chain_steps + plan_steps, helper_terms)


def _normalized_steps(value: Any) -> list[str]:
    if isinstance(value, list):
        return [str(item).lower() for item in value if str(item).strip()]
    if value:
        return [str(value).lower()]
    return []


def _step_has_helper_and_action(step: str, helper_terms: list[str]) -> bool:
    if not step or _has_negated_helper_mention(step):
        return False
    has_helper = any(term and term in step for term in helper_terms)
    has_action = any(keyword.lower() in step for keyword in VALID_HELPER_ACTION_KEYWORDS)
    return has_helper and has_action


def _has_negated_helper_mention(step: str) -> bool:
    lowered = step.lower()
    return any(pattern.lower() in lowered for pattern in NEGATED_MENTION_PATTERNS)


def _has_conservative_helper_sequence(steps: list[str], helper_terms: list[str]) -> bool:
    helper_seen = False
    for step in steps:
        if _has_negated_helper_mention(step):
            continue
        step_has_helper = any(term and term in step for term in helper_terms)
        step_has_action = any(keyword.lower() in step for keyword in VALID_HELPER_ACTION_KEYWORDS)
        if step_has_helper:
            helper_seen = True
        if helper_seen and step_has_helper and step_has_action:
            return True
        if helper_seen and step_has_action and _refers_to_seen_helper(step):
            return True
    return False


def _refers_to_seen_helper(step: str) -> bool:
    reference_terms = [
        "it",
        "that helper",
        "the helper",
        "the selected item",
        "它",
        "其",
        "将其",
        "把它",
        "其中",
        "该辅助物",
        "该物品",
        "这个辅助物",
    ]
    return any(term in step for term in reference_terms)


def _task_failures(task: dict[str, Any], candidates: list[str]) -> list[str]:
    configured = set(task.get("failure_types", []))
    matched = [failure for failure in candidates if failure in configured]
    if matched:
        return matched
    return candidates[:1]
