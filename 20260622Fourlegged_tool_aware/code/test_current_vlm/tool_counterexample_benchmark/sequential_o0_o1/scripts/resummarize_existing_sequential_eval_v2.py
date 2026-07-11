from __future__ import annotations

import argparse
import json
import shutil
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from sequential_o0_o1.sequential_evaluator import summarize_raw_file_v2  # noqa: E402


def main() -> None:
    args = parse_args()
    input_dir = resolve_path(args.input_dir)
    output_dir = resolve_path(args.output_dir) if args.output_dir else input_dir / "analysis_v2"
    review_images_dir = resolve_path(args.review_images_dir) if args.review_images_dir else None

    if not (input_dir / "raw_responses.jsonl").is_file():
        raise SystemExit(f"Missing raw responses: {input_dir / 'raw_responses.jsonl'}")
    prepare_output(output_dir, args.overwrite)
    result = summarize_raw_file_v2(
        input_dir,
        output_dir,
        review_images_dir=review_images_dir,
        experiment_name=args.experiment_name or input_dir.name,
    )
    print(json.dumps({"input_dir": str(input_dir), "output_dir": str(output_dir), **result}, ensure_ascii=False))


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Offline v2 reanalysis of existing sequential raw responses.")
    parser.add_argument("--input_dir", required=True)
    parser.add_argument("--output_dir")
    parser.add_argument("--review_images_dir")
    parser.add_argument("--experiment_name")
    parser.add_argument("--overwrite", action="store_true")
    return parser.parse_args()


def resolve_path(value: str | Path) -> Path:
    path = Path(value)
    return path.resolve() if path.is_absolute() else (ROOT / path).resolve()


def prepare_output(path: Path, overwrite: bool) -> None:
    if path.exists():
        if not overwrite:
            raise SystemExit(f"Output exists: {path}. Use --overwrite.")
        shutil.rmtree(path)
    path.mkdir(parents=True, exist_ok=True)


if __name__ == "__main__":
    main()
