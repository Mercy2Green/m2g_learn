from __future__ import annotations

import hashlib
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any, Iterable


DATASET_VERSION = "ahd_v01"
ROBOT_CONTEXT = "A quadruped robot with one arm. It can grasp one object at a time."
SPLITS = ("train", "val", "test")
SPLIT_RATIOS = {"train": 0.70, "val": 0.10, "test": 0.20}

O0_SPEC_TYPES = {
    "aggregate_transport_o0_target_visible_helper_absent": (
        "aggregate_transport",
        "search_helper",
        "container_for_multiple_objects",
    ),
    "extend_reach_o0_target_under_furniture": (
        "extend_reach",
        "search_helper",
        "long_rigid_reach_extension",
    ),
    "direct_is_enough_o0_single_target": (
        "direct_is_enough",
        "direct_is_enough",
        "none",
    ),
}

O1_SPEC_TYPES = {
    "container_helper_o1_target_absent": "container_for_multiple_objects",
    "long_tool_helper_o1_target_absent": "long_rigid_reach_extension",
    "wrong_helper_o1_target_absent": "none",
}

STAGE1_MODES = {"search_helper", "direct_is_enough"}
HELPER_FUNCTIONS = {
    "container_for_multiple_objects",
    "long_rigid_reach_extension",
    "none",
}
STAGE2_MODES = {"helper_found", "continue_search", "direct_is_enough"}
STAGE2_RELATIONS = {"aggregate_transport", "extend_reach", "none"}


def index_by_spec_id(rows: Iterable[dict[str, Any]], *, source: str) -> dict[str, dict[str, Any]]:
    indexed: dict[str, dict[str, Any]] = {}
    for row in rows:
        spec_id = str(row.get("spec_id", ""))
        if not spec_id:
            raise ValueError(f"{source} contains a row without spec_id")
        if spec_id in indexed:
            raise ValueError(f"{source} contains duplicate spec_id: {spec_id}")
        indexed[spec_id] = row
    return indexed


def join_curated_specs(
    curated_rows: Iterable[dict[str, Any]],
    specs_by_id: dict[str, dict[str, Any]],
) -> list[dict[str, Any]]:
    joined: list[dict[str, Any]] = []
    for curated in curated_rows:
        spec_id = str(curated.get("spec_id", ""))
        spec = specs_by_id.get(spec_id)
        if spec is None:
            raise ValueError(f"curated spec_id is missing from checked specs: {spec_id}")
        for field in ("spec_type", "view_stage"):
            if curated.get(field) != spec.get(field):
                raise ValueError(
                    f"{spec_id}: curated {field}={curated.get(field)!r} "
                    f"does not match spec {field}={spec.get(field)!r}"
                )
        if curated.get("image_judge_status") != "semantic_keep" or curated.get("keep") is not True:
            raise ValueError(f"{spec_id}: curated row is not semantic_keep/keep=true")
        joined.append({"curated": curated, "spec": spec})
    return joined


def stratified_group_split(
    items: Iterable[dict[str, Any]],
    *,
    id_key: str,
    stratum_key: str,
    seed: int = 42,
) -> dict[str, str]:
    strata: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for item in items:
        strata[str(item[stratum_key])].append(item)

    assignments: dict[str, str] = {}
    for stratum, members in sorted(strata.items()):
        ordered = sorted(
            members,
            key=lambda row: (
                hashlib.sha256(f"{seed}:{stratum}:{row[id_key]}".encode("utf-8")).hexdigest(),
                str(row[id_key]),
            ),
        )
        counts = split_counts(len(ordered))
        cursor = 0
        for split in SPLITS:
            for row in ordered[cursor : cursor + counts[split]]:
                item_id = str(row[id_key])
                if item_id in assignments:
                    raise ValueError(f"duplicate split group id: {item_id}")
                assignments[item_id] = split
            cursor += counts[split]
    return assignments


def split_counts(total: int) -> dict[str, int]:
    if total < 0:
        raise ValueError("split total cannot be negative")
    train = int(total * SPLIT_RATIOS["train"] + 0.5)
    val = int(total * SPLIT_RATIOS["val"] + 0.5)
    if train + val > total:
        val = max(0, total - train)
    return {"train": train, "val": val, "test": total - train - val}


def make_stage1_row(item: dict[str, Any], split: str) -> dict[str, Any]:
    spec = item["spec"]
    curated = item["curated"]
    spec_type = str(spec.get("spec_type", ""))
    expected = O0_SPEC_TYPES.get(spec_type)
    if expected is None:
        raise ValueError(f"unsupported O0 spec_type: {spec_type}")
    task_family, export_mode, needed_function = expected
    gold = spec.get("gold")
    language = spec.get("language")
    if not isinstance(gold, dict) or not isinstance(language, dict):
        raise ValueError(f"{spec['spec_id']}: invalid gold or language mapping")
    if spec.get("task_family") != task_family:
        raise ValueError(f"{spec['spec_id']}: task_family does not match spec_type")
    source_mode = gold.get("mode")
    expected_source_mode = "direct" if export_mode == "direct_is_enough" else export_mode
    if source_mode != expected_source_mode or gold.get("needed_helper_function") != needed_function:
        raise ValueError(f"{spec['spec_id']}: scene spec gold conflicts with deterministic spec_type mapping")
    target_memory = gold.get("target_memory")
    if not isinstance(target_memory, dict):
        raise ValueError(f"{spec['spec_id']}: gold.target_memory must be a mapping")
    return {
        "sample_id": f"stage1_{spec['spec_id']}",
        "stage": "search_trigger",
        "split": split,
        "spec_id": spec["spec_id"],
        "spec_type": spec_type,
        "task_family": task_family,
        "instruction": str(language.get("instruction_en", "")),
        "robot_context": ROBOT_CONTEXT,
        "image": str(curated["curated_image_path"]),
        "gold": {
            "mode": export_mode,
            "needed_helper_function": needed_function,
            "target_memory": target_memory,
        },
    }


def make_stage2_row(o0_item: dict[str, Any], o1_item: dict[str, Any], split: str) -> dict[str, Any]:
    o0_spec = o0_item["spec"]
    o1_spec = o1_item["spec"]
    o0_gold = o0_spec.get("gold")
    language = o0_spec.get("language")
    if not isinstance(o0_gold, dict) or not isinstance(language, dict):
        raise ValueError(f"{o0_spec['spec_id']}: invalid O0 metadata")

    needed = str(o0_gold.get("needed_helper_function", ""))
    target_memory = o0_gold.get("target_memory")
    helper_name, helper_function = o1_helper(o1_spec)
    task_family = str(o0_spec.get("task_family", ""))
    gold = derive_stage2_gold(
        task_family=task_family,
        needed_helper_function=needed,
        helper_name=helper_name,
        helper_function=helper_function,
    )
    return {
        "sample_id": f"stage2_{o1_spec['spec_id']}_{o0_spec['spec_id']}",
        "stage": "helper_grounding",
        "split": split,
        "task_family": task_family,
        "o0_spec_id": o0_spec["spec_id"],
        "o1_spec_id": o1_spec["spec_id"],
        "o1_spec_type": o1_spec["spec_type"],
        "instruction": str(language.get("instruction_en", "")),
        "target_memory": target_memory,
        "needed_helper_function": needed,
        "image": str(o1_item["curated"]["curated_image_path"]),
        "gold": gold,
    }


def o1_helper(spec: dict[str, Any]) -> tuple[str, str]:
    spec_type = str(spec.get("spec_type", ""))
    expected_function = O1_SPEC_TYPES.get(spec_type)
    helpers = spec.get("helper_candidates_gold")
    if expected_function is None or not isinstance(helpers, list) or len(helpers) != 1:
        raise ValueError(f"{spec.get('spec_id')}: unsupported or ambiguous O1 helper metadata")
    helper = helpers[0]
    if not isinstance(helper, dict):
        raise ValueError(f"{spec.get('spec_id')}: helper candidate must be a mapping")
    name = str(helper.get("name", ""))
    function = str(helper.get("helper_function", ""))
    if not name or function != expected_function:
        raise ValueError(f"{spec.get('spec_id')}: helper candidate conflicts with spec_type")
    return name, function


def derive_stage2_gold(
    *,
    task_family: str,
    needed_helper_function: str,
    helper_name: str,
    helper_function: str,
) -> dict[str, Any]:
    if task_family == "direct_is_enough":
        return {
            "mode": "direct_is_enough",
            "selected_helper": "none",
            "helper_target_relation": "none",
            "continue_search": False,
        }
    if needed_helper_function == helper_function and helper_function != "none":
        return {
            "mode": "helper_found",
            "selected_helper": helper_name,
            "helper_target_relation": task_family,
            "continue_search": False,
        }
    return {
        "mode": "continue_search",
        "selected_helper": "none",
        "helper_target_relation": "none",
        "continue_search": True,
    }


def stage2_case(row: dict[str, Any]) -> dict[str, Any]:
    return {
        "case_id": row["sample_id"],
        "o0_spec_id": row["o0_spec_id"],
        "task_family": row["task_family"],
        "instruction": row["instruction"],
        "target_memory": row["target_memory"],
        "needed_helper_function": row["needed_helper_function"],
        "gold": row["gold"],
    }


def build_summary(stage1: list[dict[str, Any]], stage2: list[dict[str, Any]], pool_name: str) -> str:
    s1_family = Counter(row["task_family"] for row in stage1)
    s2_mode = Counter(row["gold"]["mode"] for row in stage2)
    s2_split = Counter(row["split"] for row in stage2)
    lines = [
        f"# AHD Paired Dataset Summary: {DATASET_VERSION}",
        "",
        f"- source curated pool: data/curated_pools/{pool_name}",
        f"- Stage1 samples: {len(stage1)}",
        f"- Stage2 samples: {len(stage2)}",
        f"- unique Stage2 O1 groups: {len({row['o1_spec_id'] for row in stage2})}",
        "- construction: one curated O1 paired with one O0 memory from each task family",
        "",
        "## Stage1 Task Families",
        "",
    ]
    lines.extend(f"- {name}: {count}" for name, count in sorted(s1_family.items()))
    lines.extend(["", "## Stage2 Gold Modes", ""])
    lines.extend(f"- {name}: {count}" for name, count in sorted(s2_mode.items()))
    lines.extend(["", "## Stage2 Split Counts", ""])
    lines.extend(f"- {split}: {s2_split[split]}" for split in SPLITS)
    return "\n".join(lines) + "\n"


def build_split_report(stage1: list[dict[str, Any]], stage2: list[dict[str, Any]]) -> str:
    o1_by_split = {
        split: {row["o1_spec_id"] for row in stage2 if row["split"] == split}
        for split in SPLITS
    }
    assert o1_by_split["train"].isdisjoint(o1_by_split["test"])
    assert o1_by_split["train"].isdisjoint(o1_by_split["val"])
    assert o1_by_split["val"].isdisjoint(o1_by_split["test"])

    lines = [
        "# AHD v0.1 Split Report",
        "",
        "Split unit: O1 image group. Ratios are applied deterministically within each O1 spec type.",
        "",
        "## Counts",
        "",
        "| split | Stage1 rows | Stage2 rows | O1 groups |",
        "| --- | ---: | ---: | ---: |",
    ]
    for split in SPLITS:
        lines.append(
            f"| {split} | {sum(row['split'] == split for row in stage1)} | "
            f"{sum(row['split'] == split for row in stage2)} | {len(o1_by_split[split])} |"
        )
    lines.extend(["", "## Stage2 Task Family Distribution", ""])
    lines.extend(_distribution_table(stage2, "task_family"))
    lines.extend(["", "## O1 Spec Type Distribution", ""])
    lines.extend(_distribution_table(stage2, "o1_spec_type", unique_group=True))
    lines.extend(
        [
            "",
            "## Same O1 Leakage Check",
            "",
            f"- train O1 ids intersect val O1 ids: {len(o1_by_split['train'] & o1_by_split['val'])}",
            f"- train O1 ids intersect test O1 ids: {len(o1_by_split['train'] & o1_by_split['test'])}",
            f"- val O1 ids intersect test O1 ids: {len(o1_by_split['val'] & o1_by_split['test'])}",
            "- result: PASS",
        ]
    )
    return "\n".join(lines) + "\n"


def _distribution_table(
    rows: list[dict[str, Any]], key: str, *, unique_group: bool = False
) -> list[str]:
    names = sorted({str(row[key]) for row in rows})
    result = ["| category | train | val | test |", "| --- | ---: | ---: | ---: |"]
    for name in names:
        counts = []
        for split in SPLITS:
            matched = [row for row in rows if row["split"] == split and row[key] == name]
            count = len({row["o1_spec_id"] for row in matched}) if unique_group else len(matched)
            counts.append(count)
        result.append(f"| {name} | {counts[0]} | {counts[1]} | {counts[2]} |")
    return result


def resolve_root_path(root: Path, value: str) -> Path:
    path = Path(value)
    return path if path.is_absolute() else root / path
