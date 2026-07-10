from __future__ import annotations

import argparse
from collections import Counter
from pathlib import Path
import sys
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.jsonl_utils import read_jsonl  # noqa: E402
from src.pair_construction import (  # noqa: E402
    DATASET_VERSION,
    HELPER_FUNCTIONS,
    O0_SPEC_TYPES,
    SPLITS,
    STAGE1_MODES,
    STAGE2_MODES,
    STAGE2_RELATIONS,
    derive_stage2_gold,
    index_by_spec_id,
    o1_helper,
    resolve_root_path,
    stage2_case,
)


DEFAULT_POOL = "ahd_cosmos3_raw240_qwen32"


def main() -> None:
    args = parse_args()
    dataset_dir = ROOT / "data" / "paired_datasets" / args.dataset_name
    pool_dir = ROOT / "data" / "curated_pools" / args.pool_name
    report_path = dataset_dir / "check_report.md"

    errors: list[str] = []
    checks: Counter[str] = Counter()
    try:
        stage1 = load_required(dataset_dir / "stage1_search_trigger.jsonl")
        stage2 = load_required(dataset_dir / "stage2_helper_grounding.jsonl")
        same_o1 = load_required(dataset_dir / "evaluation" / "same_o1_different_o0.jsonl")
        wrong_helper = load_required(dataset_dir / "evaluation" / "wrong_helper.jsonl")
        no_tool = load_required(dataset_dir / "evaluation" / "no_tool_control.jsonl")
        curated = load_required(pool_dir / "curated_index.jsonl")
        specs = load_required(resolve_path(args.specs))
        reject_rows = read_jsonl(resolve_path(args.reject_list))

        curated_by_id = index_by_spec_id(curated, source="curated index")
        specs_by_id = index_by_spec_id(specs, source="checked specs")
        curated_by_image = {
            str(row.get("curated_image_path", "")): row for row in curated
        }
        reject_ids = {str(row.get("spec_id", "")) for row in reject_rows}

        check_curated_index(curated, specs_by_id, reject_ids, errors, checks)
        check_stage1(stage1, curated_by_id, curated_by_image, specs_by_id, errors, checks)
        check_stage2(stage2, curated_by_id, curated_by_image, specs_by_id, errors, checks)
        check_evaluation(same_o1, wrong_helper, no_tool, stage2, errors, checks)
        check_leakage(stage2, errors, checks)
        check_unique_ids(stage1, stage2, errors, checks)
    except (OSError, ValueError, KeyError, TypeError) as exc:
        errors.append(f"fatal validation error: {exc}")
        stage1 = locals().get("stage1", [])
        stage2 = locals().get("stage2", [])

    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(build_report(errors, checks, stage1, stage2), encoding="utf-8")
    print(f"validation errors: {len(errors)}")
    print(f"checks performed: {sum(checks.values())}")
    print(f"Wrote check report: {report_path}")
    if errors:
        for error in errors[:20]:
            print(f"ERROR: {error}")
        raise SystemExit(1)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate AHD-Benchmark v0.1 paired dataset exports.")
    parser.add_argument("--pool_name", default=DEFAULT_POOL)
    parser.add_argument("--dataset_name", default=DATASET_VERSION)
    parser.add_argument("--specs", default="specs/scene_specs_checked.jsonl")
    parser.add_argument(
        "--reject_list",
        default="data/judges/ahd_cosmos3_raw240_qwen32/vlm_image_judge_reject_list.jsonl",
    )
    return parser.parse_args()


def resolve_path(value: str) -> Path:
    path = Path(value)
    return path if path.is_absolute() else ROOT / path


def load_required(path: Path) -> list[dict[str, Any]]:
    rows = read_jsonl(path)
    if not rows:
        raise ValueError(f"required JSONL is missing or empty: {path}")
    return rows


def check_curated_index(
    curated: list[dict[str, Any]],
    specs_by_id: dict[str, dict[str, Any]],
    reject_ids: set[str],
    errors: list[str],
    checks: Counter[str],
) -> None:
    seen_images: set[str] = set()
    for row in curated:
        spec_id = str(row.get("spec_id", ""))
        image = str(row.get("curated_image_path", ""))
        checks["curated rows"] += 1
        if row.get("image_judge_status") != "semantic_keep" or row.get("keep") is not True:
            errors.append(f"curated {spec_id}: not semantic_keep/keep=true")
        if spec_id in reject_ids:
            errors.append(f"curated {spec_id}: also appears in reject list")
        if spec_id not in specs_by_id:
            errors.append(f"curated {spec_id}: missing checked spec")
        if not image or image in seen_images:
            errors.append(f"curated {spec_id}: missing or duplicate curated image path")
        seen_images.add(image)
        if image and not resolve_root_path(ROOT, image).is_file():
            errors.append(f"curated {spec_id}: image does not exist: {image}")


def check_stage1(
    rows: list[dict[str, Any]],
    curated_by_id: dict[str, dict[str, Any]],
    curated_by_image: dict[str, dict[str, Any]],
    specs_by_id: dict[str, dict[str, Any]],
    errors: list[str],
    checks: Counter[str],
) -> None:
    required = {
        "sample_id", "stage", "split", "spec_id", "spec_type", "task_family",
        "instruction", "robot_context", "image", "gold",
    }
    for row in rows:
        sample_id = str(row.get("sample_id", "<missing>"))
        checks["Stage1 rows"] += 1
        missing = required - set(row)
        if missing:
            errors.append(f"{sample_id}: Stage1 missing fields: {sorted(missing)}")
            continue
        if row["stage"] != "search_trigger" or row["split"] not in SPLITS:
            errors.append(f"{sample_id}: invalid Stage1 stage or split")
        spec_id = str(row["spec_id"])
        spec = specs_by_id.get(spec_id)
        curated = curated_by_id.get(spec_id)
        gold = row.get("gold")
        if spec is None or curated is None or not isinstance(gold, dict):
            errors.append(f"{sample_id}: missing source spec/curated row or invalid gold")
            continue
        expected = O0_SPEC_TYPES.get(str(spec.get("spec_type", "")))
        if expected is None:
            errors.append(f"{sample_id}: unsupported O0 spec type")
            continue
        family, mode, helper_function = expected
        expected_gold = {
            "mode": mode,
            "needed_helper_function": helper_function,
            "target_memory": spec["gold"]["target_memory"],
        }
        if gold != expected_gold:
            errors.append(f"{sample_id}: Stage1 gold differs from checked spec adapter")
        if gold.get("mode") not in STAGE1_MODES:
            errors.append(f"{sample_id}: invalid Stage1 mode")
        if gold.get("needed_helper_function") not in HELPER_FUNCTIONS:
            errors.append(f"{sample_id}: invalid Stage1 helper function")
        if row["task_family"] != family or row["spec_type"] != spec["spec_type"]:
            errors.append(f"{sample_id}: Stage1 source metadata mismatch")
        check_dataset_image(sample_id, str(row["image"]), spec_id, curated_by_image, errors)


def check_stage2(
    rows: list[dict[str, Any]],
    curated_by_id: dict[str, dict[str, Any]],
    curated_by_image: dict[str, dict[str, Any]],
    specs_by_id: dict[str, dict[str, Any]],
    errors: list[str],
    checks: Counter[str],
) -> None:
    required = {
        "sample_id", "stage", "split", "task_family", "o0_spec_id", "o1_spec_id",
        "o1_spec_type", "instruction", "target_memory", "needed_helper_function", "image", "gold",
    }
    for row in rows:
        sample_id = str(row.get("sample_id", "<missing>"))
        checks["Stage2 rows"] += 1
        missing = required - set(row)
        if missing:
            errors.append(f"{sample_id}: Stage2 missing fields: {sorted(missing)}")
            continue
        if row["stage"] != "helper_grounding" or row["split"] not in SPLITS:
            errors.append(f"{sample_id}: invalid Stage2 stage or split")
        o0_id = str(row["o0_spec_id"])
        o1_id = str(row["o1_spec_id"])
        o0_spec = specs_by_id.get(o0_id)
        o1_spec = specs_by_id.get(o1_id)
        curated = curated_by_id.get(o1_id)
        gold = row.get("gold")
        if o0_spec is None or o1_spec is None or curated is None or not isinstance(gold, dict):
            errors.append(f"{sample_id}: missing source metadata or invalid gold")
            continue
        try:
            helper_name, helper_function = o1_helper(o1_spec)
        except ValueError as exc:
            errors.append(f"{sample_id}: {exc}")
            continue
        expected_gold = derive_stage2_gold(
            task_family=str(o0_spec["task_family"]),
            needed_helper_function=str(o0_spec["gold"]["needed_helper_function"]),
            helper_name=helper_name,
            helper_function=helper_function,
        )
        if gold != expected_gold:
            errors.append(f"{sample_id}: Stage2 gold is not derivable from O0/O1 specs")
        if gold.get("mode") not in STAGE2_MODES:
            errors.append(f"{sample_id}: invalid Stage2 mode")
        if gold.get("helper_target_relation") not in STAGE2_RELATIONS:
            errors.append(f"{sample_id}: invalid Stage2 relation")
        if not isinstance(gold.get("continue_search"), bool):
            errors.append(f"{sample_id}: continue_search must be boolean")
        if row["target_memory"] != o0_spec["gold"]["target_memory"]:
            errors.append(f"{sample_id}: target memory differs from checked O0 spec")
        if row["needed_helper_function"] != o0_spec["gold"]["needed_helper_function"]:
            errors.append(f"{sample_id}: needed helper differs from checked O0 spec")
        if row["task_family"] != o0_spec["task_family"] or row["o1_spec_type"] != o1_spec["spec_type"]:
            errors.append(f"{sample_id}: Stage2 source metadata mismatch")
        check_dataset_image(sample_id, str(row["image"]), o1_id, curated_by_image, errors)


def check_dataset_image(
    sample_id: str,
    image: str,
    expected_spec_id: str,
    curated_by_image: dict[str, dict[str, Any]],
    errors: list[str],
) -> None:
    curated = curated_by_image.get(image)
    if curated is None:
        errors.append(f"{sample_id}: image is not from the curated pool: {image}")
        return
    if str(curated.get("spec_id")) != expected_spec_id:
        errors.append(f"{sample_id}: image/spec provenance mismatch")
    if not resolve_root_path(ROOT, image).is_file():
        errors.append(f"{sample_id}: image path does not exist: {image}")


def check_evaluation(
    same_o1: list[dict[str, Any]],
    wrong_helper: list[dict[str, Any]],
    no_tool: list[dict[str, Any]],
    stage2: list[dict[str, Any]],
    errors: list[str],
    checks: Counter[str],
) -> None:
    master = {str(row["sample_id"]): row for row in stage2}
    test_rows = [row for row in stage2 if row["split"] == "test"]
    expected_wrong = {row["sample_id"] for row in test_rows if row["gold"]["mode"] == "continue_search"}
    expected_no_tool = {row["sample_id"] for row in test_rows if row["gold"]["mode"] == "direct_is_enough"}

    seen_groups: set[str] = set()
    seen_o1: set[str] = set()
    for group in same_o1:
        checks["same-O1 evaluation groups"] += 1
        required = {"group_id", "split", "o1_spec_id", "shared_o1_image", "cases"}
        if required - set(group):
            errors.append(f"same-O1 group missing fields: {group.get('group_id')}")
            continue
        group_id = str(group["group_id"])
        o1_id = str(group["o1_spec_id"])
        if group_id in seen_groups or o1_id in seen_o1:
            errors.append(f"duplicate same-O1 group or O1 id: {group_id}")
        seen_groups.add(group_id)
        seen_o1.add(o1_id)
        cases = group["cases"]
        if group["split"] != "test" or not isinstance(cases, list) or len(cases) != 3:
            errors.append(f"{group_id}: expected exactly three test cases")
            continue
        families = {case.get("task_family") for case in cases if isinstance(case, dict)}
        modes = {case.get("gold", {}).get("mode") for case in cases if isinstance(case, dict)}
        if families != {"aggregate_transport", "extend_reach", "direct_is_enough"}:
            errors.append(f"{group_id}: incomplete task-family contrast")
        if "direct_is_enough" not in modes:
            errors.append(f"{group_id}: missing direct control")
        for case in cases:
            if not isinstance(case, dict):
                errors.append(f"{group_id}: case is not an object")
                continue
            source = master.get(str(case.get("case_id", "")))
            if source is None or source["o1_spec_id"] != o1_id:
                errors.append(f"{group_id}: case is absent from matching master group")
                continue
            if group["shared_o1_image"] != source["image"]:
                errors.append(f"{group_id}: shared image differs from master row")
            if case != stage2_case(source):
                errors.append(f"{group_id}: case fields differ from the master Stage2 row")

    actual_wrong = {str(row.get("sample_id", "")) for row in wrong_helper}
    actual_no_tool = {str(row.get("sample_id", "")) for row in no_tool}
    checks["wrong-helper evaluation rows"] += len(wrong_helper)
    checks["no-tool-control evaluation rows"] += len(no_tool)
    if actual_wrong != expected_wrong:
        errors.append("wrong_helper evaluation is not the exact test continue_search subset")
    if actual_no_tool != expected_no_tool:
        errors.append("no_tool_control evaluation is not the exact test direct_is_enough subset")
    for name, rows in (("wrong_helper", wrong_helper), ("no_tool_control", no_tool)):
        for row in rows:
            source = master.get(str(row.get("sample_id", "")))
            if source is not None and row != source:
                errors.append(f"{name} row differs from master Stage2 row: {row.get('sample_id')}")


def check_leakage(
    stage2: list[dict[str, Any]], errors: list[str], checks: Counter[str]
) -> None:
    o1_by_split = {
        split: {str(row["o1_spec_id"]) for row in stage2 if row["split"] == split}
        for split in SPLITS
    }
    for left, right in (("train", "val"), ("train", "test"), ("val", "test")):
        checks["O1 split intersections"] += 1
        overlap = o1_by_split[left] & o1_by_split[right]
        if overlap:
            errors.append(f"same-O1 leakage between {left}/{right}: {sorted(overlap)}")


def check_unique_ids(
    stage1: list[dict[str, Any]],
    stage2: list[dict[str, Any]],
    errors: list[str],
    checks: Counter[str],
) -> None:
    for name, rows in (("Stage1", stage1), ("Stage2", stage2)):
        ids = [str(row.get("sample_id", "")) for row in rows]
        checks["sample id uniqueness"] += 1
        if not all(ids) or len(ids) != len(set(ids)):
            errors.append(f"{name} sample_id values are missing or duplicated")


def build_report(
    errors: list[str],
    checks: Counter[str],
    stage1: list[dict[str, Any]],
    stage2: list[dict[str, Any]],
) -> str:
    lines = [
        "# AHD v0.1 Pair Check Report",
        "",
        f"- result: {'PASS' if not errors else 'FAIL'}",
        f"- Stage1 rows: {len(stage1)}",
        f"- Stage2 rows: {len(stage2)}",
        f"- validation errors: {len(errors)}",
        "",
        "## Checks",
        "",
    ]
    lines.extend(f"- {name}: {count}" for name, count in sorted(checks.items()))
    lines.extend(["", "## Errors", ""])
    if errors:
        lines.extend(f"- {error}" for error in errors)
    else:
        lines.append("- none")
    return "\n".join(lines) + "\n"


if __name__ == "__main__":
    main()
