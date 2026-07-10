from __future__ import annotations

import argparse
import hashlib
from collections import defaultdict
from pathlib import Path
import sys
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.jsonl_utils import read_jsonl, write_jsonl  # noqa: E402
from src.pair_construction import (  # noqa: E402
    DATASET_VERSION,
    O0_SPEC_TYPES,
    SPLITS,
    build_split_report,
    build_summary,
    index_by_spec_id,
    join_curated_specs,
    make_stage1_row,
    make_stage2_row,
    stage2_case,
    stratified_group_split,
)


DEFAULT_POOL = "ahd_cosmos3_raw240_qwen32"


def main() -> None:
    args = parse_args()
    pool_dir = ROOT / "data" / "curated_pools" / args.pool_name
    output_dir = ROOT / "data" / "paired_datasets" / args.dataset_name
    curated_path = pool_dir / "curated_index.jsonl"
    specs_path = resolve_path(args.specs)

    curated_rows = read_jsonl(curated_path)
    spec_rows = read_jsonl(specs_path)
    if not curated_rows:
        raise SystemExit(f"Curated index not found or empty: {curated_path}")
    if not spec_rows:
        raise SystemExit(f"Checked specs not found or empty: {specs_path}")

    specs_by_id = index_by_spec_id(spec_rows, source=str(specs_path))
    joined = join_curated_specs(curated_rows, specs_by_id)
    o0_items = [item for item in joined if item["spec"]["view_stage"] == "O0"]
    o1_items = [item for item in joined if item["spec"]["view_stage"] == "O1"]
    if not o0_items or not o1_items:
        raise SystemExit("Curated pool must contain both O0 and O1 images")

    o0_assignments = stratified_group_split(
        [
            {
                "spec_id": item["spec"]["spec_id"],
                "task_family": item["spec"]["task_family"],
            }
            for item in o0_items
        ],
        id_key="spec_id",
        stratum_key="task_family",
        seed=args.seed,
    )
    o1_assignments = stratified_group_split(
        [
            {
                "spec_id": item["spec"]["spec_id"],
                "spec_type": item["spec"]["spec_type"],
            }
            for item in o1_items
        ],
        id_key="spec_id",
        stratum_key="spec_type",
        seed=args.seed,
    )

    stage1 = sorted(
        (
            make_stage1_row(item, o0_assignments[str(item["spec"]["spec_id"])])
            for item in o0_items
        ),
        key=lambda row: row["sample_id"],
    )
    stage2 = build_stage2(o0_items, o1_items, o0_assignments, o1_assignments, args.seed)
    evaluation = build_evaluation(stage2)

    assert_group_isolation(stage2)
    output_dir.mkdir(parents=True, exist_ok=True)
    evaluation_dir = output_dir / "evaluation"
    evaluation_dir.mkdir(parents=True, exist_ok=True)
    write_jsonl(output_dir / "stage1_search_trigger.jsonl", stage1)
    write_jsonl(output_dir / "stage2_helper_grounding.jsonl", stage2)
    write_jsonl(evaluation_dir / "same_o1_different_o0.jsonl", evaluation["same_o1"])
    write_jsonl(evaluation_dir / "wrong_helper.jsonl", evaluation["wrong_helper"])
    write_jsonl(evaluation_dir / "no_tool_control.jsonl", evaluation["no_tool_control"])
    (output_dir / "dataset_summary.md").write_text(
        build_summary(stage1, stage2, args.pool_name), encoding="utf-8"
    )
    (output_dir / "split_report.md").write_text(
        build_split_report(stage1, stage2), encoding="utf-8"
    )

    print(f"source curated pool: {pool_dir}")
    print(f"Stage1 rows: {len(stage1)}")
    print(f"Stage2 rows: {len(stage2)}")
    print(f"same-O1 test groups: {len(evaluation['same_o1'])}")
    print(f"wrong-helper test rows: {len(evaluation['wrong_helper'])}")
    print(f"no-tool-control test rows: {len(evaluation['no_tool_control'])}")
    print(f"Wrote paired dataset: {output_dir}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build AHD-Benchmark v0.1 pairs from a curated image pool.")
    parser.add_argument("--pool_name", default=DEFAULT_POOL)
    parser.add_argument("--dataset_name", default=DATASET_VERSION)
    parser.add_argument("--specs", default="specs/scene_specs_checked.jsonl")
    parser.add_argument("--seed", type=int, default=42)
    return parser.parse_args()


def resolve_path(value: str) -> Path:
    path = Path(value)
    return path if path.is_absolute() else ROOT / path


def build_stage2(
    o0_items: list[dict[str, Any]],
    o1_items: list[dict[str, Any]],
    o0_assignments: dict[str, str],
    o1_assignments: dict[str, str],
    seed: int,
) -> list[dict[str, Any]]:
    o0_by_family_split: dict[tuple[str, str], list[dict[str, Any]]] = defaultdict(list)
    for item in o0_items:
        spec = item["spec"]
        family = str(spec["task_family"])
        if str(spec["spec_type"]) not in O0_SPEC_TYPES:
            raise ValueError(f"unsupported O0 spec_type: {spec['spec_type']}")
        split = o0_assignments[str(spec["spec_id"])]
        o0_by_family_split[(family, split)].append(item)
    for pool in o0_by_family_split.values():
        pool.sort(key=lambda item: str(item["spec"]["spec_id"]))

    rows: list[dict[str, Any]] = []
    families = ("aggregate_transport", "extend_reach", "direct_is_enough")
    for o1_item in sorted(o1_items, key=lambda item: str(item["spec"]["spec_id"])):
        o1_id = str(o1_item["spec"]["spec_id"])
        split = o1_assignments[o1_id]
        for family in families:
            candidates = o0_by_family_split.get((family, split), [])
            if not candidates:
                raise ValueError(f"no curated O0 candidates for family={family}, split={split}")
            digest = hashlib.sha256(f"{seed}:{o1_id}:{family}".encode("utf-8")).digest()
            index = int.from_bytes(digest[:8], "big") % len(candidates)
            rows.append(make_stage2_row(candidates[index], o1_item, split))
    return sorted(rows, key=lambda row: row["sample_id"])


def build_evaluation(stage2: list[dict[str, Any]]) -> dict[str, list[dict[str, Any]]]:
    test_rows = [row for row in stage2 if row["split"] == "test"]
    by_o1: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in test_rows:
        by_o1[str(row["o1_spec_id"])].append(row)

    same_o1: list[dict[str, Any]] = []
    for o1_id, rows in sorted(by_o1.items()):
        images = {str(row["image"]) for row in rows}
        if len(images) != 1 or len(rows) != 3:
            raise ValueError(f"{o1_id}: expected one shared image and three cases")
        same_o1.append(
            {
                "group_id": f"same_o1_{o1_id}",
                "split": "test",
                "o1_spec_id": o1_id,
                "shared_o1_image": next(iter(images)),
                "cases": [stage2_case(row) for row in sorted(rows, key=lambda row: row["task_family"])],
            }
        )

    wrong_helper = [
        row for row in test_rows if row["gold"]["mode"] == "continue_search"
    ]
    no_tool_control = [
        row for row in test_rows if row["gold"]["mode"] == "direct_is_enough"
    ]
    return {
        "same_o1": same_o1,
        "wrong_helper": wrong_helper,
        "no_tool_control": no_tool_control,
    }


def assert_group_isolation(stage2: list[dict[str, Any]]) -> None:
    o1_ids = {
        split: {row["o1_spec_id"] for row in stage2 if row["split"] == split}
        for split in SPLITS
    }
    assert o1_ids["train"].isdisjoint(o1_ids["test"]), "train/test O1 leakage"
    assert o1_ids["train"].isdisjoint(o1_ids["val"]), "train/val O1 leakage"
    assert o1_ids["val"].isdisjoint(o1_ids["test"]), "val/test O1 leakage"


if __name__ == "__main__":
    main()
