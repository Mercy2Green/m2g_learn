from __future__ import annotations

from typing import Any


COMMON_REQUIRED = [
    "spec_id",
    "version",
    "view_stage",
    "task_family",
    "spec_type",
    "seed",
    "language",
    "robot_context",
    "visual_scene",
    "quality",
]

O0_GOLD_REQUIRED = [
    "stage",
    "mode",
    "needed_helper_function",
    "target_memory",
    "direct_fallback_allowed",
]


def _missing(mapping: dict[str, Any], keys: list[str]) -> list[str]:
    return [key for key in keys if key not in mapping]


def _expect_dict(spec: dict[str, Any], key: str, errors: list[str]) -> dict[str, Any]:
    value = spec.get(key)
    if not isinstance(value, dict):
        errors.append(f"{key} must be a mapping")
        return {}
    return value


def validate_scene_spec(spec: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    for key in _missing(spec, COMMON_REQUIRED):
        errors.append(f"missing required field: {key}")

    if spec.get("version") != "ahd_v01":
        errors.append("version must be ahd_v01")
    if spec.get("view_stage") not in {"O0", "O1"}:
        errors.append("view_stage must be O0 or O1")
    if not isinstance(spec.get("spec_id"), str) or not spec.get("spec_id"):
        errors.append("spec_id must be a non-empty string")
    if not isinstance(spec.get("seed"), int):
        errors.append("seed must be an integer")

    _expect_dict(spec, "language", errors)
    _expect_dict(spec, "robot_context", errors)
    visual_scene = _expect_dict(spec, "visual_scene", errors)
    _expect_dict(spec, "quality", errors)

    for list_key in ("must_include", "must_exclude", "distractors", "avoid"):
        if visual_scene and not isinstance(visual_scene.get(list_key), list):
            errors.append(f"visual_scene.{list_key} must be a list")

    if spec.get("view_stage") == "O0":
        errors.extend(validate_o0_spec(spec))
    elif spec.get("view_stage") == "O1":
        errors.extend(validate_o1_spec(spec))
    return errors


def validate_o0_spec(spec: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    gold = _expect_dict(spec, "gold", errors)
    for key in _missing(gold, O0_GOLD_REQUIRED):
        errors.append(f"gold missing required field: {key}")
    if gold.get("mode") not in {"search_helper", "direct"}:
        errors.append("gold.mode must be search_helper or direct")
    if gold.get("stage") not in {"search_trigger", "direct_action"}:
        errors.append("gold.stage must be search_trigger or direct_action")
    if not isinstance(gold.get("target_memory"), dict):
        errors.append("gold.target_memory must be a mapping")
    if not isinstance(gold.get("direct_fallback_allowed"), bool):
        errors.append("gold.direct_fallback_allowed must be a boolean")
    if "helper_candidates_gold" in spec:
        errors.append("O0 spec must not include helper_candidates_gold")
    return errors


def validate_o1_spec(spec: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    helpers = spec.get("helper_candidates_gold")
    if not isinstance(helpers, list) or not helpers:
        errors.append("helper_candidates_gold must be a non-empty list")
    else:
        for index, helper in enumerate(helpers):
            if not isinstance(helper, dict):
                errors.append(f"helper_candidates_gold[{index}] must be a mapping")
                continue
            if not helper.get("name"):
                errors.append(f"helper_candidates_gold[{index}].name is required")
            if "helper_function" not in helper:
                errors.append(f"helper_candidates_gold[{index}].helper_function is required")
    pairing_role = spec.get("pairing_role")
    if not isinstance(pairing_role, dict):
        errors.append("pairing_role must be a mapping")
    elif not isinstance(pairing_role.get("can_pair_with"), list):
        errors.append("pairing_role.can_pair_with must be a list")
    if "gold" in spec:
        errors.append("O1 spec must not include final gold; final helper grounding depends on pairing")
    return errors
