from __future__ import annotations

from collections import Counter
from typing import Any


LEAKAGE_TERMS = {
    "useful",
    "task-relevant",
    "helper function",
    "needed helper",
    "correct helper",
    "wrong helper",
    "use this",
    "should use",
    "answer",
}


def count_specs(specs: list[dict[str, Any]]) -> dict[str, Counter[str]]:
    return {
        "view_stage": Counter(str(spec.get("view_stage")) for spec in specs),
        "spec_type": Counter(str(spec.get("spec_type")) for spec in specs),
        "task_family": Counter(str(spec.get("task_family")) for spec in specs),
    }


def expected_spec_type_counts(plan: dict[str, Any]) -> dict[str, int]:
    raw = plan["raw_scene_specs"]
    counts: dict[str, int] = {}
    counts.update(raw["o0"]["spec_types"])
    counts.update(raw["o1"]["spec_types"])
    return counts


def check_generation_plan_totals(plan: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    raw = plan.get("raw_scene_specs", {})
    o0 = raw.get("o0", {})
    o1 = raw.get("o1", {})
    o0_total = sum(o0.get("spec_types", {}).values())
    o1_total = sum(o1.get("spec_types", {}).values())
    if o0_total != o0.get("total"):
        errors.append(f"o0 total mismatch: declared {o0.get('total')} vs spec_types {o0_total}")
    if o1_total != o1.get("total"):
        errors.append(f"o1 total mismatch: declared {o1.get('total')} vs spec_types {o1_total}")
    if o0_total + o1_total != raw.get("total"):
        errors.append(f"raw total mismatch: declared {raw.get('total')} vs computed {o0_total + o1_total}")
    if raw.get("total") != 2000:
        errors.append(f"raw_scene_specs.total must be 2000, found {raw.get('total')}")

    subset = plan.get("first_image_generation_subset", {})
    subset_total = sum(subset.get("o0", {}).values()) + sum(subset.get("o1", {}).values())
    if subset_total != subset.get("total"):
        errors.append(f"first_image_generation_subset total mismatch: declared {subset.get('total')} vs computed {subset_total}")
    return errors


def check_spec_counts_against_plan(specs: list[dict[str, Any]], plan: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    counts = count_specs(specs)
    raw = plan["raw_scene_specs"]
    if counts["view_stage"].get("O0", 0) != raw["o0"]["total"]:
        errors.append(f"O0 count mismatch: {counts['view_stage'].get('O0', 0)} vs {raw['o0']['total']}")
    if counts["view_stage"].get("O1", 0) != raw["o1"]["total"]:
        errors.append(f"O1 count mismatch: {counts['view_stage'].get('O1', 0)} vs {raw['o1']['total']}")
    for spec_type, expected in expected_spec_type_counts(plan).items():
        actual = counts["spec_type"].get(spec_type, 0)
        if actual != expected:
            errors.append(f"{spec_type} count mismatch: {actual} vs {expected}")
    return errors


def check_required_fields(specs: list[dict[str, Any]], required: list[str]) -> list[str]:
    errors: list[str] = []
    for spec in specs:
        missing = [field for field in required if field not in spec]
        if missing:
            errors.append(f"{spec.get('spec_id', '<missing id>')} missing fields: {', '.join(missing)}")
    return errors


def check_duplicate_spec_id(specs: list[dict[str, Any]]) -> list[str]:
    ids = [str(spec.get("spec_id")) for spec in specs]
    duplicates = sorted(item for item, count in Counter(ids).items() if count > 1)
    return [f"duplicate spec_id: {item}" for item in duplicates]


def check_forbidden_leakage(spec: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    visual_scene = spec.get("visual_scene", {})
    if not isinstance(visual_scene, dict):
        return ["visual_scene is not a mapping"]
    text_parts: list[str] = []
    for value in visual_scene.values():
        if isinstance(value, str):
            text_parts.append(value)
        elif isinstance(value, list):
            text_parts.extend(str(item) for item in value)
    text = " ".join(text_parts).lower()
    for term in sorted(LEAKAGE_TERMS):
        if term in text:
            errors.append(f"{spec.get('spec_id')} visual_scene leaks label wording: {term}")
    return errors
