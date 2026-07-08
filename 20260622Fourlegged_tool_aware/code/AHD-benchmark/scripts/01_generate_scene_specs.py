from __future__ import annotations

import argparse
import random
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.jsonl_utils import write_jsonl
from src.load_config import load_yaml
from src.spec_checks import check_generation_plan_totals
from src.spec_templates import (
    make_aggregate_o0_spec,
    make_container_o1_spec,
    make_direct_o0_spec,
    make_extend_reach_o0_spec,
    make_long_tool_o1_spec,
    make_wrong_helper_o1_spec,
)


ENVIRONMENTS = [
    "realistic home kitchen",
    "small apartment living room",
    "student dorm room",
    "office kitchenette",
    "robotics lab lounge",
    "bedroom corner",
]
SURFACES = ["kitchen counter", "low table", "wooden desk", "tile floor", "carpeted floor", "shelf edge"]
FURNITURE = ["sofa", "bed", "cabinet", "low couch"]
CAMERAS = ["robot first-person view", "low quadruped camera view", "near floor mobile robot view", "slightly wide robot view"]
LIGHTING = ["soft daylight", "warm indoor lighting", "even overhead lighting", "mixed window and ceiling light"]
DISTRACTORS = ["cup", "book", "cloth", "phone charger", "notebook", "small towel", "empty mug", "toy block"]


def _sample_distractors(rng: random.Random) -> list[str]:
    return rng.sample(DISTRACTORS, k=rng.randint(2, 4))


def _choice(rng: random.Random, values: list[str]) -> str:
    return rng.choice(values)


def _common_kwargs(rng: random.Random) -> dict[str, Any]:
    return {
        "environment": _choice(rng, ENVIRONMENTS),
        "surface": _choice(rng, SURFACES),
        "distractors": _sample_distractors(rng),
        "camera": _choice(rng, CAMERAS),
        "lighting": _choice(rng, LIGHTING),
    }


def generate_specs(plan: dict[str, Any], seed: int) -> list[dict[str, Any]]:
    rng = random.Random(seed)
    specs: list[dict[str, Any]] = []
    counts = plan["raw_scene_specs"]["o0"]["spec_types"] | plan["raw_scene_specs"]["o1"]["spec_types"]

    for index in range(counts["aggregate_transport_o0_target_visible_helper_absent"]):
        target = _choice(rng, ["water bottles", "drink cans", "sports drink bottles"])
        specs.append(make_aggregate_o0_spec(
            spec_id=f"agg_o0_{index + 1:06d}",
            seed=100000 + index,
            target_object=target,
            target_count=rng.randint(3, 7),
            **_common_kwargs(rng),
        ))

    for index in range(counts["extend_reach_o0_target_under_furniture"]):
        target = _choice(rng, ["remote control", "small ball", "dropped key ring", "small toy"])
        specs.append(make_extend_reach_o0_spec(
            spec_id=f"reach_o0_{index + 1:06d}",
            seed=120000 + index,
            furniture=_choice(rng, FURNITURE),
            target_object=target,
            **_common_kwargs(rng),
        ))

    for index in range(counts["direct_is_enough_o0_single_target"]):
        target = _choice(rng, ["water bottle", "drink can", "sports drink bottle"])
        specs.append(make_direct_o0_spec(
            spec_id=f"direct_o0_{index + 1:06d}",
            seed=140000 + index,
            target_object=target,
            **_common_kwargs(rng),
        ))

    for index in range(counts["container_helper_o1_target_absent"]):
        specs.append(make_container_o1_spec(
            spec_id=f"container_o1_{index + 1:06d}",
            seed=200000 + index,
            helper_name=_choice(rng, ["basket", "tray", "open box", "tote bag"]),
            **_common_kwargs(rng),
        ))

    for index in range(counts["long_tool_helper_o1_target_absent"]):
        specs.append(make_long_tool_o1_spec(
            spec_id=f"longtool_o1_{index + 1:06d}",
            seed=220000 + index,
            helper_name=_choice(rng, ["broom", "long stick", "rod", "hanger"]),
            **_common_kwargs(rng),
        ))

    for index in range(counts["wrong_helper_o1_target_absent"]):
        specs.append(make_wrong_helper_o1_spec(
            spec_id=f"wrong_o1_{index + 1:06d}",
            seed=240000 + index,
            helper_name=_choice(rng, ["cloth", "book", "short pencil", "soft pillow", "empty cup", "shoe"]),
            **_common_kwargs(rng),
        ))

    return specs


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--seed", type=int, default=None)
    args = parser.parse_args()

    plan = load_yaml(ROOT / "configs" / "generation_plan_v01.yaml")
    errors = check_generation_plan_totals(plan)
    if errors:
        raise SystemExit("\n".join(errors))
    seed = args.seed if args.seed is not None else int(plan.get("random_seed", 42))
    specs = generate_specs(plan, seed)
    o0_specs = [spec for spec in specs if spec["view_stage"] == "O0"]
    o1_specs = [spec for spec in specs if spec["view_stage"] == "O1"]

    write_jsonl(ROOT / "specs" / "scene_specs_raw.jsonl", specs)
    write_jsonl(ROOT / "specs" / "o0_scene_specs_raw.jsonl", o0_specs)
    write_jsonl(ROOT / "specs" / "o1_scene_specs_raw.jsonl", o1_specs)
    print(f"Wrote {len(specs)} raw specs ({len(o0_specs)} O0, {len(o1_specs)} O1).")


if __name__ == "__main__":
    main()
