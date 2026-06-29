from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.evaluator import evaluate_response  # noqa: E402


MODEL = {"model_id": "unit_model", "provider": "mock", "strength_role": "local_open_vlm"}
PRIMARY_PROMPT = {"prompt_id": "natural_free_plan", "primary_for_counterexample": True, "embodiment_profile": "generic"}
STRUCTURED_PROMPT = {"prompt_id": "structured_tool_probe", "primary_for_counterexample": False, "embodiment_profile": "generic"}


def water_task() -> dict:
    return {
        "task_id": "task_001",
        "name": "multi_bottles_visible_container",
        "expected_behavior": {
            "should_use_tool_or_container": True,
            "expected_tool_or_container_types": ["tray", "bag", "box", "basket"],
            "target_object_terms": ["water", "bottle", "bottles", "水", "水瓶"],
            "expected_trip_pattern": "single_or_few_trips",
            "should_search_for_tool_if_not_visible": False,
            "should_avoid_over_tool_use": False,
        },
        "failure_types": ["F1_aggregation_failure", "F3_efficiency_blind_planning", "F4_container_affordance_miss"],
    }


def remote_task() -> dict:
    return {
        "task_id": "task_008",
        "name": "remote_under_sofa",
        "expected_behavior": {
            "should_use_tool_or_container": True,
            "expected_tool_or_container_types": ["broom", "stick", "rod"],
            "target_object_terms": ["remote", "remote control", "遥控器"],
            "expected_trip_pattern": "single_or_few_trips",
            "should_search_for_tool_if_not_visible": False,
            "should_avoid_over_tool_use": False,
        },
        "failure_types": ["F4_container_affordance_miss", "F6_tool_necessity_miss", "F9_long_horizon_decomposition_miss"],
    }


def single_bottle_task() -> dict:
    return {
        "task_id": "task_011",
        "name": "single_bottle_tool_unnecessary",
        "expected_behavior": {
            "should_use_tool_or_container": False,
            "expected_tool_or_container_types": [],
            "target_object_terms": ["water", "bottle", "水", "水瓶"],
            "expected_trip_pattern": "single",
            "should_search_for_tool_if_not_visible": False,
            "should_avoid_over_tool_use": True,
        },
        "failure_types": ["F7_over_tool_use"],
    }


def parsed(payload: dict) -> dict:
    return {"parse_status": "ok", "parsed": payload}


def test_target_as_helper() -> None:
    row = evaluate_response(
        water_task(),
        parsed({"plan": ["carry the water bottles"], "selected_helper": "water bottles", "estimated_number_of_trips": "single"}),
        MODEL,
        STRUCTURED_PROMPT,
        "image.jpg",
    )
    assert row["pass_fail"] == "fail"
    assert row["inferred_target_as_helper"] == "yes"


def test_mention_as_use() -> None:
    row = evaluate_response(
        remote_task(),
        parsed({"plan": ["avoid the white rod-like object", "grasp the remote directly"], "estimated_number_of_trips": "single"}),
        MODEL,
        PRIMARY_PROMPT,
        "image.jpg",
    )
    assert row["pass_fail"] in {"fail", "needs_review"}
    assert row["pass_fail"] != "pass"
    assert "F6_tool_necessity_miss" in row["failure_types_detected"]


def test_valid_container_action_chain() -> None:
    row = evaluate_response(
        water_task(),
        parsed({"plan": ["find a tray", "place bottles on the tray", "carry tray to bedroom"], "estimated_number_of_trips": "single"}),
        MODEL,
        PRIMARY_PROMPT,
        "image.jpg",
    )
    assert row["pass_fail"] == "pass"
    assert row["inferred_valid_helper_action_chain"] == "yes"


def test_selected_helper_without_action_chain_is_not_valid() -> None:
    row = evaluate_response(
        water_task(),
        parsed(
            {
                "plan": ["carry the water bottles to the bedroom"],
                "selected_helper": "tray",
                "tool_use_action_chain": [],
                "estimated_number_of_trips": "single",
            }
        ),
        MODEL,
        STRUCTURED_PROMPT,
        "image.jpg",
    )
    assert row["inferred_valid_helper_action_chain"] == "no"
    assert row["pass_fail"] in {"fail", "needs_review"}
    assert row["pass_fail"] != "pass"


def test_structured_selected_helper_with_real_action_chain_is_valid() -> None:
    row = evaluate_response(
        water_task(),
        parsed(
            {
                "plan": ["find a tray", "place bottles on the tray", "carry the tray to the bedroom"],
                "selected_helper": "tray",
                "tool_use_action_chain": ["find a tray", "place bottles on the tray", "carry the tray to the bedroom"],
                "estimated_number_of_trips": "single",
            }
        ),
        MODEL,
        STRUCTURED_PROMPT,
        "image.jpg",
    )
    assert row["pass_fail"] == "pass"
    assert row["inferred_valid_helper_action_chain"] == "yes"


def test_direct_capacity_hallucination() -> None:
    row = evaluate_response(
        water_task(),
        parsed({"plan": ["grab all four bottles directly and carry them in one trip"], "estimated_number_of_trips": "single"}),
        MODEL,
        PRIMARY_PROMPT,
        "image.jpg",
    )
    assert row["pass_fail"] == "fail"
    assert row["inferred_direct_carry_capacity_risk"] == "yes"


def test_over_tool_use() -> None:
    row = evaluate_response(
        single_bottle_task(),
        parsed({"plan": ["find a tray", "place the bottle on the tray", "carry the tray to the user"], "estimated_number_of_trips": "single"}),
        MODEL,
        PRIMARY_PROMPT,
        "image.jpg",
    )
    assert row["pass_fail"] == "fail"
    assert "F7_over_tool_use" in row["failure_types_detected"]


if __name__ == "__main__":
    test_target_as_helper()
    test_mention_as_use()
    test_valid_container_action_chain()
    test_selected_helper_without_action_chain_is_not_valid()
    test_structured_selected_helper_with_real_action_chain_is_valid()
    test_direct_capacity_hallucination()
    test_over_tool_use()
    print("evaluator synthetic tests passed")
