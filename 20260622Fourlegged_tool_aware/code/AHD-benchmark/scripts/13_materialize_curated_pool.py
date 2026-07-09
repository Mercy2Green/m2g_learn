from __future__ import annotations

import argparse
import shutil
from collections import Counter
from pathlib import Path
import sys
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.jsonl_utils import read_jsonl, write_jsonl  # noqa: E402
from src.load_config import load_yaml  # noqa: E402
from src.storage_layout import (  # noqa: E402
    curated_pool_dir,
    curated_pool_image_path,
    relative_to_root,
    storage_config,
    view_stage_dir,
)


def main() -> None:
    args = parse_args()
    config = load_yaml(ROOT / "configs" / "cosmos3_batch_generation.yaml")
    copy_mode = args.copy_mode or str(storage_config(config)["curated_copy_mode"])
    if copy_mode not in {"copy", "symlink"}:
        raise SystemExit(f"Unsupported --copy_mode: {copy_mode}")

    results_path = resolve_path(args.results)
    judge_dir = resolve_path(args.judge_dir)
    judge_path = judge_dir / "vlm_image_judge.jsonl"
    pool_dir = curated_pool_dir(args.pool_name, config, ROOT)
    index_path = pool_dir / "curated_index.jsonl"
    summary_path = pool_dir / "curated_summary.md"

    if pool_dir.exists() and not args.overwrite and not args.dry_run:
        raise SystemExit(f"Curated pool already exists: {pool_dir}. Use --overwrite to replace files.")

    result_rows = read_jsonl(results_path)
    judge_rows = read_jsonl(judge_path)
    if not result_rows:
        raise SystemExit(f"Results file not found or empty: {results_path}")
    if not judge_rows:
        raise SystemExit(f"Judge file not found or empty: {judge_path}")

    results_by_spec_id = {str(row.get("spec_id")): row for row in result_rows}
    keep_rows = [
        row for row in judge_rows
        if row.get("image_judge_status") == "semantic_keep" and row.get("keep") is True
    ]
    source_run_name = infer_source_run_name(results_path)

    curated_rows: list[dict[str, Any]] = []
    missing_sources: list[str] = []
    for judge_row in keep_rows:
        spec_id = str(judge_row.get("spec_id", ""))
        result_row = results_by_spec_id.get(spec_id)
        if result_row is None:
            missing_sources.append(f"{spec_id}: missing_result_row")
            continue

        view_stage = str(judge_row.get("view_stage") or result_row.get("view_stage") or "")
        source_image = resolve_source_image(result_row, judge_row)
        if not source_image.is_file():
            missing_sources.append(f"{spec_id}: missing_image:{source_image}")
            continue

        target = curated_pool_image_path(args.pool_name, spec_id, view_stage, config, ROOT)
        curated_rows.append({
            "spec_id": spec_id,
            "spec_type": judge_row.get("spec_type") or result_row.get("spec_type"),
            "view_stage": view_stage,
            "source_run_name": source_run_name,
            "source_results_path": relative_to_root(results_path, ROOT),
            "source_image_path": relative_to_root(source_image, ROOT),
            "curated_image_path": relative_to_root(target, ROOT),
            "judge_model": judge_row.get("judge_model"),
            "image_judge_status": judge_row.get("image_judge_status"),
            "keep": judge_row.get("keep"),
            "prompt_source": judge_row.get("prompt_source") or result_row.get("prompt_source"),
            "enrichment_model": judge_row.get("enrichment_model") or result_row.get("enrichment_model"),
        })

        if not args.dry_run:
            materialize_one(source_image, target, copy_mode, overwrite=args.overwrite)

    if missing_sources:
        raise SystemExit("Cannot materialize all semantic_keep rows:\n" + "\n".join(missing_sources))

    if not args.dry_run:
        write_jsonl(index_path, curated_rows)
        summary_path.write_text(
            build_summary(
                curated_rows,
                pool_name=args.pool_name,
                source_run_name=source_run_name,
                judge_dir=judge_dir,
                copy_mode=copy_mode,
            ),
            encoding="utf-8",
        )

    print(f"semantic_keep rows: {len(keep_rows)}")
    print(f"materialized rows: {len(curated_rows)}")
    print(f"copy_mode: {copy_mode}")
    print(f"curated_pool: {pool_dir}")
    if args.dry_run:
        print("dry_run: no files written")
    else:
        print(f"Wrote index: {index_path}")
        print(f"Wrote summary: {summary_path}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Materialize semantic_keep AHD images into a curated pool.")
    parser.add_argument("--results", required=True)
    parser.add_argument("--judge_dir", required=True)
    parser.add_argument("--pool_name", required=True)
    parser.add_argument("--copy_mode", choices=["copy", "symlink"], default=None)
    parser.add_argument("--overwrite", action="store_true")
    parser.add_argument("--dry_run", action="store_true")
    return parser.parse_args()


def resolve_path(path_text: str) -> Path:
    path = Path(path_text)
    return path if path.is_absolute() else ROOT / path


def infer_source_run_name(results_path: Path) -> str:
    if results_path.name == "results.jsonl":
        return results_path.parent.name
    if results_path.name.endswith("_results.jsonl"):
        return results_path.name.removesuffix("_results.jsonl")
    return results_path.stem


def resolve_source_image(result_row: dict[str, Any], judge_row: dict[str, Any]) -> Path:
    value = result_row.get("output_image_path") or judge_row.get("image_path") or ""
    path = Path(str(value))
    return path if path.is_absolute() else ROOT / path


def materialize_one(source: Path, target: Path, copy_mode: str, *, overwrite: bool) -> None:
    target.parent.mkdir(parents=True, exist_ok=True)
    if target.exists() or target.is_symlink():
        if not overwrite:
            raise SystemExit(f"Curated image exists: {target}. Use --overwrite to replace it.")
        target.unlink()
    if copy_mode == "symlink":
        target.symlink_to(source.resolve())
    else:
        shutil.copy2(source, target)


def build_summary(
    rows: list[dict[str, Any]],
    *,
    pool_name: str,
    source_run_name: str,
    judge_dir: Path,
    copy_mode: str,
) -> str:
    by_type = Counter(str(row.get("spec_type", "")) for row in rows)
    by_stage = Counter(view_stage_dir(str(row.get("view_stage", ""))) for row in rows)
    lines = [
        f"# Curated Pool Summary: {pool_name}",
        "",
        f"- source run name: {source_run_name}",
        f"- source judge dir: {relative_to_root(judge_dir, ROOT)}",
        f"- copy mode: {copy_mode}",
        f"- total semantic_keep copied: {len(rows)}",
        f"- o0 count: {by_stage['o0']}",
        f"- o1 count: {by_stage['o1']}",
        "",
        "## Counts By Spec Type",
        "",
    ]
    if by_type:
        lines.extend(f"- {spec_type}: {count}" for spec_type, count in sorted(by_type.items()))
    else:
        lines.append("- none")
    return "\n".join(lines) + "\n"


if __name__ == "__main__":
    main()
