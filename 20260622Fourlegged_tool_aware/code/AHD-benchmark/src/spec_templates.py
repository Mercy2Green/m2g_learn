from __future__ import annotations

from typing import Any


VERSION = "ahd_v01"


def _base_spec(
    *,
    spec_id: str,
    view_stage: str,
    task_family: str,
    spec_type: str,
    seed: int,
    instruction_en: str,
    instruction_zh: str,
    visual_scene: dict[str, Any],
) -> dict[str, Any]:
    return {
        "spec_id": spec_id,
        "version": VERSION,
        "view_stage": view_stage,
        "task_family": task_family,
        "spec_type": spec_type,
        "split_candidate": "train",
        "seed": seed,
        "language": {
            "instruction_en": instruction_en,
            "instruction_zh": instruction_zh,
        },
        "robot_context": {
            "robot_type": "quadruped_single_arm",
            "capability": "can grasp one object at a time",
            "constraint": "must choose efficient high-level behavior from partial observations",
        },
        "visual_scene": visual_scene,
        "generation": {
            "image_generator": "cosmos3_t2i",
            "status": "not_generated",
        },
        "quality": {
            "checked": False,
            "status": "unchecked",
            "notes": [],
        },
    }


def make_aggregate_o0_spec(
    *,
    spec_id: str,
    seed: int,
    environment: str,
    surface: str,
    target_object: str,
    target_count: int,
    distractors: list[str],
    camera: str,
    lighting: str,
) -> dict[str, Any]:
    target_description = f"{target_count} visible {target_object}"
    spec = _base_spec(
        spec_id=spec_id,
        view_stage="O0",
        task_family="aggregate_transport",
        spec_type="aggregate_transport_o0_target_visible_helper_absent",
        seed=seed,
        instruction_en=f"Bring all visible {target_object} to the bedroom efficiently.",
        instruction_zh="卧室里几个同学有点渴，请尽快把这些饮料送到卧室。",
        visual_scene={
            "camera": camera,
            "environment": environment,
            "surface": surface,
            "lighting": lighting,
            "target_description": target_description,
            "target_type": target_object,
            "target_count": target_count,
            "must_include": [target_description, surface],
            "must_exclude": ["basket", "tray", "box", "bag", "shopping bag", "carrying container"],
            "distractors": distractors,
            "avoid": ["people", "hands", "text", "watermark", "cartoon", "advertisement"],
        },
    )
    spec["gold"] = {
        "stage": "search_trigger",
        "mode": "search_helper",
        "needed_helper_function": "container_for_multiple_objects",
        "target_memory": {
            "target_objects": [f"multiple {target_object}"],
            "target_count_range": [max(2, target_count - 1), target_count + 1],
            "target_location": surface,
            "task_relevant_property": "multiple loose objects",
        },
        "direct_fallback_allowed": False,
    }
    return spec


def make_extend_reach_o0_spec(
    *,
    spec_id: str,
    seed: int,
    environment: str,
    surface: str,
    furniture: str,
    target_object: str,
    distractors: list[str],
    camera: str,
    lighting: str,
) -> dict[str, Any]:
    target_description = f"{target_object} partly visible under {furniture}"
    spec = _base_spec(
        spec_id=spec_id,
        view_stage="O0",
        task_family="extend_reach",
        spec_type="extend_reach_o0_target_under_furniture",
        seed=seed,
        instruction_en=f"Retrieve the {target_object} from under the {furniture}.",
        instruction_zh=f"请把{furniture}下面的{target_object}取出来。",
        visual_scene={
            "camera": camera,
            "environment": environment,
            "surface": surface,
            "furniture": furniture,
            "lighting": lighting,
            "target_description": target_description,
            "target_type": target_object,
            "target_count": 1,
            "must_include": [target_description, furniture],
            "must_exclude": ["broom", "stick", "long stick", "rod", "hanger", "long tool"],
            "distractors": distractors,
            "avoid": ["people", "hands", "text", "watermark", "cartoon", "advertisement"],
        },
    )
    spec["gold"] = {
        "stage": "search_trigger",
        "mode": "search_helper",
        "needed_helper_function": "long_rigid_reach_extension",
        "target_memory": {
            "target_objects": [target_object],
            "target_count_range": [1, 1],
            "target_location": f"under {furniture}",
            "task_relevant_property": "under furniture and beyond direct grasp",
        },
        "direct_fallback_allowed": False,
    }
    return spec


def make_direct_o0_spec(
    *,
    spec_id: str,
    seed: int,
    environment: str,
    surface: str,
    target_object: str,
    distractors: list[str],
    camera: str,
    lighting: str,
) -> dict[str, Any]:
    target_description = f"single reachable {target_object}"
    spec = _base_spec(
        spec_id=spec_id,
        view_stage="O0",
        task_family="direct_is_enough",
        spec_type="direct_is_enough_o0_single_target",
        seed=seed,
        instruction_en=f"Pick up the visible {target_object}.",
        instruction_zh=f"请拿起可直接够到的{target_object}。",
        visual_scene={
            "camera": camera,
            "environment": environment,
            "surface": surface,
            "lighting": lighting,
            "target_description": target_description,
            "target_type": target_object,
            "target_count": 1,
            "must_include": [target_description, surface],
            "must_exclude": ["basket", "tray", "box", "bag", "broom", "stick", "rod", "hanger"],
            "distractors": distractors,
            "avoid": ["people", "hands", "text", "watermark", "cartoon", "advertisement"],
        },
    )
    spec["gold"] = {
        "stage": "direct_action",
        "mode": "direct",
        "needed_helper_function": "none",
        "target_memory": {
            "target_objects": [target_object],
            "target_count_range": [1, 1],
            "target_location": surface,
            "task_relevant_property": "single reachable object",
        },
        "direct_fallback_allowed": True,
    }
    return spec


def _make_o1_spec(
    *,
    spec_id: str,
    seed: int,
    spec_type: str,
    helper_name: str,
    helper_function: str,
    environment: str,
    surface: str,
    distractors: list[str],
    camera: str,
    lighting: str,
    must_exclude: list[str],
) -> dict[str, Any]:
    spec = _base_spec(
        spec_id=spec_id,
        view_stage="O1",
        task_family="helper_view",
        spec_type=spec_type,
        seed=seed,
        instruction_en="Inspect the current view for objects.",
        instruction_zh="观察当前视野中的物体。",
        visual_scene={
            "camera": camera,
            "environment": environment,
            "surface": surface,
            "lighting": lighting,
            "helper_description": f"empty {helper_name}" if helper_function == "container_for_multiple_objects" else helper_name,
            "helper_type": helper_name,
            "must_include": [helper_name],
            "must_exclude": must_exclude,
            "distractors": distractors,
            "avoid": ["people", "hands", "text", "watermark", "cartoon", "advertisement"],
        },
    )
    spec["helper_candidates_gold"] = [{"name": helper_name, "helper_function": helper_function}]
    spec["pairing_role"] = {
        "can_pair_with": [
            "aggregate_transport_o0_target_visible_helper_absent",
            "extend_reach_o0_target_under_furniture",
            "direct_is_enough_o0_single_target",
        ],
        "same_o1_group_eligible": True,
    }
    return spec


def make_container_o1_spec(**kwargs: Any) -> dict[str, Any]:
    return _make_o1_spec(
        spec_type="container_helper_o1_target_absent",
        helper_function="container_for_multiple_objects",
        must_exclude=["water bottle", "drink can", "remote control", "small ball", "broom", "stick", "rod", "hanger"],
        **kwargs,
    )


def make_long_tool_o1_spec(**kwargs: Any) -> dict[str, Any]:
    return _make_o1_spec(
        spec_type="long_tool_helper_o1_target_absent",
        helper_function="long_rigid_reach_extension",
        must_exclude=["water bottle", "drink can", "remote control", "small ball", "basket", "tray", "box", "bag"],
        **kwargs,
    )


def make_wrong_helper_o1_spec(**kwargs: Any) -> dict[str, Any]:
    return _make_o1_spec(
        spec_type="wrong_helper_o1_target_absent",
        helper_function="none",
        must_exclude=["water bottle", "drink can", "remote control", "small ball"],
        **kwargs,
    )
