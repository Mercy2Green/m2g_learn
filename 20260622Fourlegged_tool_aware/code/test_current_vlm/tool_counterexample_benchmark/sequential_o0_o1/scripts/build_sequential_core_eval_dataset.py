from __future__ import annotations

import argparse
import json
from collections import Counter, defaultdict
from pathlib import Path
import sys
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from sequential_o0_o1.scripts.build_sequential_smoke_dataset import (  # noqa: E402
    SPEC_TYPES,
    gold,
    read_jsonl,
    resolve_curated_image,
    sample_row,
)
from src.load_config import load_yaml  # noqa: E402


def main() -> None:
    args = parse_args()
    curated_path = root_path(args.curated_index)
    output_path = root_path(args.output)
    report_path = output_path.with_name(f"{output_path.stem}_report.md")
    if not curated_path.is_file():
        raise SystemExit(f"Curated index does not exist: {curated_path}")
    if (output_path.exists() or report_path.exists()) and not args.overwrite:
        raise SystemExit(f"Output exists. Use --overwrite: {output_path}")

    task_by_id = {
        str(row["task_id"]): row for row in load_yaml(ROOT / "config" / "tasks.yaml").get("tasks", [])
    }
    by_type = load_curated_by_type(curated_path)
    samples = build_samples(by_type, task_by_id)
    validate_samples(samples)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", encoding="utf-8") as handle:
        for row in samples:
            handle.write(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n")
    report_path.write_text(build_report(samples), encoding="utf-8")
    print(f"core eval samples: {len(samples)}")
    for name, count in sorted(Counter(row["sample_type"] for row in samples).items()):
        print(f"{name}: {count}")
    print(f"Wrote: {output_path}")
    print(f"Wrote: {report_path}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build the controlled sequential O0/O1 core evaluation set.")
    parser.add_argument(
        "--curated_index",
        default="../../AHD-benchmark/data/curated_pools/ahd_cosmos3_raw240_qwen32/curated_index.jsonl",
    )
    parser.add_argument("--output", default="sequential_o0_o1/data/sequential_core_eval_samples.jsonl")
    parser.add_argument("--overwrite", action="store_true")
    return parser.parse_args()


def root_path(value: str | Path) -> Path:
    path = Path(value)
    return path if path.is_absolute() else (ROOT / path).resolve()


def load_curated_by_type(path: Path) -> dict[str, list[dict[str, Any]]]:
    ahd_root = path.parents[3]
    by_type: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for source in read_jsonl(path):
        if source.get("image_judge_status") != "semantic_keep" or source.get("keep") is not True:
            raise ValueError(f"Non-curated row in curated index: {source.get('spec_id')}")
        row = dict(source)
        row["resolved_image_path"] = resolve_curated_image(row, ahd_root)
        by_type[str(row["spec_type"])].append(row)
    for rows in by_type.values():
        rows.sort(key=lambda row: str(row["spec_id"]))
    for name, spec_type in SPEC_TYPES.items():
        if not by_type.get(spec_type):
            raise ValueError(f"Missing required curated type {name}: {spec_type}")
    if len(by_type[SPEC_TYPES["wrong"]]) < 2:
        raise ValueError("Core eval requires two wrong-helper O1 images")
    return by_type


def build_samples(
    by_type: dict[str, list[dict[str, Any]]], tasks: dict[str, dict[str, Any]]
) -> list[dict[str, Any]]:
    aggregate = by_type[SPEC_TYPES["aggregate"]]
    reach = by_type[SPEC_TYPES["reach"]]
    direct = by_type[SPEC_TYPES["direct"]]
    container = by_type[SPEC_TYPES["container"]]
    long_tool = by_type[SPEC_TYPES["long_tool"]]
    wrong = by_type[SPEC_TYPES["wrong"]]
    task002 = str(tasks["task_002"]["instruction"])
    task008 = str(tasks["task_008"]["instruction"])
    task011 = str(tasks["task_011"]["instruction"])
    shared_group = "same_o1_container_000001"
    shared_o1 = container[0]

    return [
        sample_row(
            sample_id="positive_aggregate_001", sample_type="positive_aggregate", group_id="",
            instruction=task002, o0=aggregate[0], o1=container[0], old_task_id="task_002",
            gold=gold("helper_found", "container_for_multiple_objects", "aggregate_transport", True, False, False),
            notes="Core positive aggregate pair; first curated aggregate O0 and container O1.",
        ),
        sample_row(
            sample_id="positive_reach_001", sample_type="positive_reach", group_id="",
            instruction=task008, o0=reach[0], o1=long_tool[0], old_task_id="task_008",
            gold=gold("helper_found", "long_rigid_reach_extension", "reach_extension", True, False, False),
            notes="Core positive reach pair; first curated reach O0 and long-tool O1.",
        ),
        sample_row(
            sample_id="wrong_helper_negative_aggregate_001", sample_type="wrong_helper_negative", group_id="",
            instruction=task002, o0=aggregate[1], o1=wrong[0], old_task_id="task_002",
            gold=gold("continue_search", "container_for_multiple_objects", "none", False, True, False),
            notes="Wrong-helper negative for aggregate target memory.",
        ),
        sample_row(
            sample_id="wrong_helper_negative_reach_001", sample_type="wrong_helper_negative", group_id="",
            instruction=task008, o0=reach[1], o1=wrong[1], old_task_id="task_008",
            gold=gold("continue_search", "long_rigid_reach_extension", "none", False, True, False),
            notes="Wrong-helper negative for reach target memory.",
        ),
        sample_row(
            sample_id="no_tool_control_001", sample_type="no_tool_control", group_id="",
            instruction=task011, o0=direct[0], o1=container[0], old_task_id="task_011",
            gold=gold("direct_is_enough", "none", "none", False, False, True),
            notes="Standalone direct-execution control; pair is intentionally also represented in the shared-O1 group.",
        ),
        sample_row(
            sample_id="same_o1_aggregate_001", sample_type="same_o1_different_o0", group_id=shared_group,
            instruction=task002, o0=aggregate[0], o1=shared_o1, old_task_id="task_002",
            gold=gold("helper_found", "container_for_multiple_objects", "aggregate_transport", True, False, False),
            notes="Shared container O1 with aggregate O0 memory.",
        ),
        sample_row(
            sample_id="same_o1_direct_001", sample_type="same_o1_different_o0", group_id=shared_group,
            instruction=task011, o0=direct[0], o1=shared_o1, old_task_id="task_011",
            gold=gold("direct_is_enough", "none", "none", False, False, True),
            notes="Shared container O1 with direct O0 memory; duplicates the standalone control pair intentionally.",
        ),
        sample_row(
            sample_id="same_o1_reach_001", sample_type="same_o1_different_o0", group_id=shared_group,
            instruction=task008, o0=reach[0], o1=shared_o1, old_task_id="task_008",
            gold=gold("continue_search", "long_rigid_reach_extension", "none", False, True, False),
            notes="Shared container O1 with reach O0 memory.",
        ),
    ]


def validate_samples(samples: list[dict[str, Any]]) -> None:
    if len(samples) != 8 or len({row["sample_id"] for row in samples}) != 8:
        raise ValueError("Core eval must contain exactly eight uniquely identified rows")
    for row in samples:
        for key in ("o0_image_path", "o1_image_path"):
            if not root_path(str(row[key])).is_file():
                raise ValueError(f"Missing curated image for {row['sample_id']}: {row[key]}")
    shared = [row for row in samples if row["group_id"] == "same_o1_container_000001"]
    if len(shared) != 3 or len({row["o1_spec_id"] for row in shared}) != 1:
        raise ValueError("same-O1 group must contain three rows sharing one O1 spec")
    expected = {"helper_found", "direct_is_enough", "continue_search"}
    if {row["gold"]["expected_decision"] for row in shared} != expected:
        raise ValueError("same-O1 group must cover all three expected decisions")


def build_report(samples: list[dict[str, Any]]) -> str:
    counts = Counter(row["sample_type"] for row in samples)
    shared = [row for row in samples if row.get("group_id")]
    lines = [
        "# Sequential Core Evaluation Dataset Report", "",
        f"- total samples: {len(samples)}", "- images copied: 0", "- curated paths referenced: PASS", "",
        "## Sample Type Counts", "",
    ]
    lines.extend(f"- {key}: {value}" for key, value in sorted(counts.items()))
    lines.extend([
        "", "## Same O1 Group", "", f"- group id: {shared[0]['group_id']}",
        f"- shared O1: {shared[0]['o1_spec_id']} ({shared[0]['o1_image_path']})",
    ])
    lines.extend(
        f"- {row['sample_id']}: {row['old_task_id_source']} -> {row['gold']['expected_decision']} / "
        f"{row['gold']['helper_target_relation']}"
        for row in shared
    )
    lines.extend(["", "## First Rows", ""])
    lines.extend(
        f"- {row['sample_id']}: O0={row['o0_image_path']}; O1={row['o1_image_path']}"
        for row in samples[:5]
    )
    lines.extend([
        "", "The standalone no-tool control and same-O1 direct row intentionally reuse the same direct O0/container O1 pair.",
    ])
    return "\n".join(lines) + "\n"


if __name__ == "__main__":
    main()
