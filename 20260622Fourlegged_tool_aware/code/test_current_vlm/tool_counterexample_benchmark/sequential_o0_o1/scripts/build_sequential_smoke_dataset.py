from __future__ import annotations

import argparse
import json
import os
from collections import Counter, defaultdict
from pathlib import Path
import sys
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from src.load_config import load_yaml  # noqa: E402


SPEC_TYPES = {
    "aggregate": "aggregate_transport_o0_target_visible_helper_absent",
    "container": "container_helper_o1_target_absent",
    "direct": "direct_is_enough_o0_single_target",
    "reach": "extend_reach_o0_target_under_furniture",
    "long_tool": "long_tool_helper_o1_target_absent",
    "wrong": "wrong_helper_o1_target_absent",
}


def main() -> None:
    args = parse_args()
    config_path = root_path(args.config)
    output_path = root_path(args.output)
    if output_path.exists() and not args.overwrite:
        raise SystemExit(f"Output exists: {output_path}. Use --overwrite to replace it.")

    config = load_yaml(config_path)
    curated_path = root_path(str(config["curated_index_path"]))
    if not curated_path.is_file():
        raise SystemExit(f"Curated index does not exist: {curated_path}")
    tasks_path = root_path(str(config["old_tasks_path"]))
    task_by_id = {str(row["task_id"]): row for row in load_yaml(tasks_path).get("tasks", [])}
    for task_id in ("task_002", "task_008", "task_011"):
        if task_id not in task_by_id:
            raise SystemExit(f"Required old task is missing: {task_id}")

    curated_rows = read_jsonl(curated_path)
    by_type: dict[str, list[dict[str, Any]]] = defaultdict(list)
    seen_ids: set[str] = set()
    ahd_root = curated_path.parents[3]
    for row in curated_rows:
        spec_id = str(row.get("spec_id", ""))
        if not spec_id or spec_id in seen_ids:
            raise SystemExit(f"Missing or duplicate curated spec_id: {spec_id!r}")
        seen_ids.add(spec_id)
        if row.get("image_judge_status") != "semantic_keep" or row.get("keep") is not True:
            raise SystemExit(f"Curated row is not semantic_keep: {spec_id}")
        row = dict(row)
        row["resolved_image_path"] = resolve_curated_image(row, ahd_root)
        by_type[str(row.get("spec_type", ""))].append(row)
    for rows in by_type.values():
        rows.sort(key=lambda row: str(row["spec_id"]))
    for name, spec_type in SPEC_TYPES.items():
        if not by_type.get(spec_type):
            raise SystemExit(f"Curated pool has no rows for {name}: {spec_type}")

    counts = dict(config.get("smoke_sample_counts") or {})
    samples_by_type: dict[str, list[dict[str, Any]]] = {
        "positive_aggregate": build_positive_aggregate(
            by_type, task_by_id["task_002"], int(counts.get("positive_aggregate", 0))
        ),
        "positive_reach": build_positive_reach(
            by_type, task_by_id["task_008"], int(counts.get("positive_reach", 0))
        ),
        "wrong_helper_negative": build_wrong_helper(
            by_type, task_by_id, int(counts.get("wrong_helper_negative", 0))
        ),
        "no_tool_control": build_no_tool(
            by_type, task_by_id["task_011"], int(counts.get("no_tool_control", 0))
        ),
    }
    samples = round_robin(samples_by_type)
    group_count = int(counts.get("same_o1_different_o0_groups", 0))
    samples.extend(build_same_o1_groups(by_type, task_by_id, group_count))
    validate_samples(samples)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", encoding="utf-8") as handle:
        for row in samples:
            handle.write(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n")

    sample_counts = Counter(row["sample_type"] for row in samples)
    print(f"curated index: {curated_path}")
    print(f"built samples: {len(samples)}")
    for sample_type, count in sorted(sample_counts.items()):
        print(f"{sample_type}: {count}")
    print(f"Wrote: {output_path}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build the isolated O0/O1 sequential smoke dataset.")
    parser.add_argument("--config", default="sequential_o0_o1/config/sequential_eval_config.yaml")
    parser.add_argument("--output", default="sequential_o0_o1/data/sequential_smoke_samples.jsonl")
    parser.add_argument("--overwrite", action="store_true")
    return parser.parse_args()


def root_path(value: str) -> Path:
    path = Path(value)
    return path if path.is_absolute() else (ROOT / path).resolve()


def read_jsonl(path: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    with path.open("r", encoding="utf-8") as handle:
        for line_no, line in enumerate(handle, start=1):
            if not line.strip():
                continue
            value = json.loads(line)
            if not isinstance(value, dict):
                raise ValueError(f"JSONL row {line_no} is not an object: {path}")
            rows.append(value)
    return rows


def resolve_curated_image(row: dict[str, Any], ahd_root: Path) -> str:
    value = Path(str(row.get("curated_image_path", "")))
    absolute = value if value.is_absolute() else ahd_root / value
    if not absolute.is_file():
        raise SystemExit(f"Curated image does not exist: {absolute}")
    return Path(os.path.relpath(absolute, ROOT)).as_posix()


def build_positive_aggregate(
    by_type: dict[str, list[dict[str, Any]]], task: dict[str, Any], count: int
) -> list[dict[str, Any]]:
    o0s = require_count(by_type[SPEC_TYPES["aggregate"]], count, "aggregate O0")
    o1s = require_count(by_type[SPEC_TYPES["container"]], count, "container O1")
    return [
        sample_row(
            sample_id=f"seq_positive_aggregate_{index + 1:03d}",
            sample_type="positive_aggregate",
            group_id="",
            instruction=str(task["instruction"]),
            o0=o0s[index],
            o1=o1s[index],
            old_task_id="task_002",
            gold=gold("helper_found", "container_for_multiple_objects", "aggregate_transport", True, False, False),
            notes="Positive aggregate transport pair from curated O0/O1 images.",
        )
        for index in range(count)
    ]


def build_positive_reach(
    by_type: dict[str, list[dict[str, Any]]], task: dict[str, Any], count: int
) -> list[dict[str, Any]]:
    o0s = require_count(by_type[SPEC_TYPES["reach"]], count, "reach O0")
    o1s = require_count(by_type[SPEC_TYPES["long_tool"]], count, "long-tool O1")
    return [
        sample_row(
            sample_id=f"seq_positive_reach_{index + 1:03d}",
            sample_type="positive_reach",
            group_id="",
            instruction=str(task["instruction"]),
            o0=o0s[index],
            o1=o1s[index],
            old_task_id="task_008",
            gold=gold("helper_found", "long_rigid_reach_extension", "reach_extension", True, False, False),
            notes="Positive reach-extension pair from curated O0/O1 images.",
        )
        for index in range(count)
    ]


def build_wrong_helper(
    by_type: dict[str, list[dict[str, Any]]], tasks: dict[str, dict[str, Any]], count: int
) -> list[dict[str, Any]]:
    wrong_o1s = require_count(by_type[SPEC_TYPES["wrong"]], count, "wrong-helper O1")
    rows: list[dict[str, Any]] = []
    for index in range(count):
        use_aggregate = index % 2 == 0
        o0_type = SPEC_TYPES["aggregate"] if use_aggregate else SPEC_TYPES["reach"]
        task_id = "task_002" if use_aggregate else "task_008"
        needed = "container_for_multiple_objects" if use_aggregate else "long_rigid_reach_extension"
        rows.append(
            sample_row(
                sample_id=f"seq_wrong_helper_negative_{index + 1:03d}",
                sample_type="wrong_helper_negative",
                group_id="",
                instruction=str(tasks[task_id]["instruction"]),
                o0=by_type[o0_type][index // 2],
                o1=wrong_o1s[index],
                old_task_id=task_id,
                gold=gold("continue_search", needed, "none", False, True, False),
                notes="Negative pair: current O1 object is not suitable for the remembered O0 task.",
            )
        )
    return rows


def build_no_tool(
    by_type: dict[str, list[dict[str, Any]]], task: dict[str, Any], count: int
) -> list[dict[str, Any]]:
    o0s = require_count(by_type[SPEC_TYPES["direct"]], count, "direct O0")
    o1_pools = (by_type[SPEC_TYPES["container"]], by_type[SPEC_TYPES["long_tool"]])
    return [
        sample_row(
            sample_id=f"seq_no_tool_control_{index + 1:03d}",
            sample_type="no_tool_control",
            group_id="",
            instruction=str(task["instruction"]),
            o0=o0s[index],
            o1=o1_pools[index % 2][index // 2],
            old_task_id="task_011",
            gold=gold("direct_is_enough", "none", "none", False, False, True),
            notes="Control pair: the original single reachable target should be handled directly.",
        )
        for index in range(count)
    ]


def build_same_o1_groups(
    by_type: dict[str, list[dict[str, Any]]], tasks: dict[str, dict[str, Any]], count: int
) -> list[dict[str, Any]]:
    containers = require_count(by_type[SPEC_TYPES["container"]], count, "shared container O1")
    rows: list[dict[str, Any]] = []
    for index in range(count):
        group_id = f"same_o1_container_{index + 1:06d}"
        shared_o1 = containers[index]
        variants = [
            (
                "aggregate", "task_002", "helper_found", "container_for_multiple_objects",
                "aggregate_transport", True, False, False,
            ),
            ("direct", "task_011", "direct_is_enough", "none", "none", False, False, True),
            (
                "reach", "task_008", "continue_search", "long_rigid_reach_extension",
                "none", False, True, False,
            ),
        ]
        for variant, task_id, decision, needed, relation, use, search, direct in variants:
            rows.append(
                sample_row(
                    sample_id=f"seq_{group_id}_{variant}",
                    sample_type="same_o1_different_o0",
                    group_id=group_id,
                    instruction=str(tasks[task_id]["instruction"]),
                    o0=by_type[SPEC_TYPES[variant]][index],
                    o1=shared_o1,
                    old_task_id=task_id,
                    gold=gold(decision, needed, relation, use, search, direct),
                    notes=f"Shared-O1 control case with {variant} O0 memory.",
                )
            )
    return rows


def sample_row(
    *,
    sample_id: str,
    sample_type: str,
    group_id: str,
    instruction: str,
    o0: dict[str, Any],
    o1: dict[str, Any],
    old_task_id: str,
    gold: dict[str, Any],
    notes: str,
) -> dict[str, Any]:
    return {
        "sample_id": sample_id,
        "sample_type": sample_type,
        "group_id": group_id,
        "instruction": instruction,
        "o0_image_path": o0["resolved_image_path"],
        "o1_image_path": o1["resolved_image_path"],
        "o0_spec_id": o0["spec_id"],
        "o1_spec_id": o1["spec_id"],
        "o0_spec_type": o0["spec_type"],
        "o1_spec_type": o1["spec_type"],
        "old_task_id_source": old_task_id,
        "gold": gold,
        "notes": notes,
    }


def gold(
    decision: str,
    needed: str,
    relation: str,
    use_helper: bool,
    continue_search: bool,
    direct_execute: bool,
) -> dict[str, Any]:
    return {
        "expected_decision": decision,
        "needed_helper_function": needed,
        "helper_target_relation": relation,
        "should_use_helper": use_helper,
        "should_continue_search": continue_search,
        "should_direct_execute": direct_execute,
    }


def require_count(rows: list[dict[str, Any]], count: int, label: str) -> list[dict[str, Any]]:
    if count < 0 or len(rows) < count:
        raise SystemExit(f"Need {count} {label} rows, found {len(rows)}")
    return rows[:count]


def round_robin(groups: dict[str, list[dict[str, Any]]]) -> list[dict[str, Any]]:
    ordered_names = ("positive_aggregate", "positive_reach", "wrong_helper_negative", "no_tool_control")
    output: list[dict[str, Any]] = []
    max_size = max((len(groups[name]) for name in ordered_names), default=0)
    for index in range(max_size):
        for name in ordered_names:
            if index < len(groups[name]):
                output.append(groups[name][index])
    return output


def validate_samples(samples: list[dict[str, Any]]) -> None:
    required = {
        "sample_id", "sample_type", "group_id", "instruction", "o0_image_path", "o1_image_path",
        "o0_spec_id", "o1_spec_id", "o0_spec_type", "o1_spec_type", "old_task_id_source", "gold", "notes",
    }
    ids: set[str] = set()
    for row in samples:
        if set(row) != required:
            raise ValueError(f"Invalid sample schema: {row.get('sample_id')}")
        if row["sample_id"] in ids:
            raise ValueError(f"Duplicate sample_id: {row['sample_id']}")
        ids.add(str(row["sample_id"]))
        for key in ("o0_image_path", "o1_image_path"):
            if not root_path(str(row[key])).is_file():
                raise ValueError(f"Missing sample image: {row[key]}")


if __name__ == "__main__":
    main()
