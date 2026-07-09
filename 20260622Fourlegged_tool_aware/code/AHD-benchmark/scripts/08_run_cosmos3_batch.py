from __future__ import annotations

import argparse
from datetime import datetime
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.cosmos3_manifest import load_manifest, save_manifest  # noqa: E402
from src.cosmos3_runner import (  # noqa: E402
    Cosmos3Runtime,
    build_cosmos3_command,
    command_preview,
    resolve_cuda_visible_devices,
    run_cosmos3_one,
)
from src.load_config import load_yaml  # noqa: E402


def main() -> None:
    parser = argparse.ArgumentParser(description="Run or dry-run Cosmos3 generation from an AHD manifest.")
    parser.add_argument("--manifest", required=True)
    parser.add_argument("--dry_run", action="store_true")
    parser.add_argument("--limit", type=int, default=None)
    parser.add_argument("--start_index", type=int, default=0)
    parser.add_argument("--print_commands_only", action="store_true")
    parser.add_argument("--run_name", default=None)
    parser.add_argument("--timeout_seconds", type=int, default=None)
    parser.add_argument("--yes", action="store_true", help="Confirm actual generation, required for batches larger than 12.")
    args = parser.parse_args()

    config = load_yaml(ROOT / "configs" / "cosmos3_batch_generation.yaml")
    manifest_path = _resolve_path(args.manifest)
    rows = load_manifest(manifest_path)
    selected = rows[args.start_index:]
    if args.limit is not None:
        selected = selected[: args.limit]
    is_dry_mode = bool(args.dry_run or args.print_commands_only)
    if not is_dry_mode:
        image_count = len(selected)
        print(f"WARNING: Actual Cosmos3 generation will run {image_count} images. Use --limit 1 first for smoke testing.")
        if image_count > 12 and not args.yes:
            raise SystemExit("Refusing to run more than 12 images without --yes.")

    run_name = args.run_name or f"{manifest_path.stem}_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
    run_log_dir = ROOT / str(config["run_log_dir"])
    run_log_dir.mkdir(parents=True, exist_ok=True)
    work_dir = run_log_dir / f"{run_name}_work"
    cosmos_input = config["cosmos_input"]
    runtime = Cosmos3Runtime(
        ahd_root=ROOT,
        cosmos_root=(ROOT / str(config["cosmos_root"])).resolve(),
        cuda_visible_devices=resolve_cuda_visible_devices(str(config.get("cuda_visible_devices", "1"))),
        target_output_size=str(config["target_output_size"]),
        cosmos_resolution=str(cosmos_input["resolution"]),
        cosmos_aspect_ratio=str(cosmos_input["aspect_ratio"]),
        expected_width=int(cosmos_input["expected_width"]),
        expected_height=int(cosmos_input["expected_height"]),
        num_steps=int(config["default_num_steps"]),
        guidance_scale=float(config["default_guidance_scale"]),
    )

    plan_rows = []
    for index, row in enumerate(selected, start=args.start_index):
        command, input_path, output_dir = build_cosmos3_command(row, runtime, work_dir=work_dir)
        plan = {
            "index": index,
            "spec_id": row["spec_id"],
            "spec_type": row["spec_type"],
            "output_image_path": row["output_image_path"],
            "seed": row["seed"],
            "generator": str(config["generator_name"]),
            "dry_run": is_dry_mode,
            "cosmos_input_path": str(input_path),
            "cosmos_output_dir": str(output_dir),
            "target_output_size": runtime.target_output_size,
            "cosmos_resolution": runtime.cosmos_resolution,
            "cosmos_aspect_ratio": runtime.cosmos_aspect_ratio,
            "expected_width": runtime.expected_width,
            "expected_height": runtime.expected_height,
            "cuda_visible_devices": runtime.cuda_visible_devices,
            "expected_primary_generated_path": str(output_dir / "t2i" / "vision.jpg"),
            "final_output_image_path": row["output_image_path"],
            "command": command_preview(command, runtime),
        }
        plan_rows.append(plan)
        print(f"[{index}] {row['spec_id']} -> {row['output_image_path']}")
        print(plan["command"])

    if is_dry_mode:
        plan_path = run_log_dir / f"{run_name}_plan.jsonl"
        save_manifest(plan_path, plan_rows)
        print(f"Wrote dry-run plan: {plan_path}")
        return

    results = []
    for index, row in enumerate(selected, start=args.start_index):
        print(f"Running [{index}] {row['spec_id']}")
        result = run_cosmos3_one(row, runtime, work_dir=work_dir, timeout_seconds=args.timeout_seconds)
        result["index"] = index
        results.append(result)
        print(f"  {result['status']}: {result['output_image_path']}")

    results_path = run_log_dir / f"{run_name}_results.jsonl"
    save_manifest(results_path, results)
    print(f"Wrote results: {results_path}")


def _resolve_path(path_text: str) -> Path:
    path = Path(path_text)
    return path if path.is_absolute() else ROOT / path


if __name__ == "__main__":
    main()
