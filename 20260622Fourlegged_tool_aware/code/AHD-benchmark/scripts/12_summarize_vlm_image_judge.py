from __future__ import annotations

import argparse
import csv
from collections import Counter, defaultdict
from pathlib import Path
import sys
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.jsonl_utils import read_jsonl  # noqa: E402


def main() -> None:
    args = parse_args()
    input_dir = _resolve_path(args.input_dir)
    rows = read_jsonl(input_dir / "vlm_image_judge.jsonl")
    if not rows:
        raise SystemExit(f"Judge results not found or empty: {input_dir / 'vlm_image_judge.jsonl'}")
    write_summary(input_dir / "vlm_image_judge_summary.md", rows)
    write_spec_type_summary(input_dir / "vlm_image_judge_spec_type_summary.csv", rows)
    print(f"Wrote summary: {input_dir / 'vlm_image_judge_summary.md'}")
    print(f"Wrote spec type CSV: {input_dir / 'vlm_image_judge_spec_type_summary.csv'}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Summarize AHD VLM image judge outputs.")
    parser.add_argument("--input_dir", default="data/judges/ahd_cosmos3_smoke12_qwen32")
    return parser.parse_args()


def write_summary(path: Path, rows: list[dict[str, Any]]) -> None:
    stats = _status_counts(rows)
    by_type: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in rows:
        by_type[str(row.get("spec_type", ""))].append(row)
    generation_failures = _rows_with_status(rows, "generation_failed")
    missing_invalid = _rows_with_status(rows, "missing_or_invalid_image")
    semantic_rejects = _rows_with_status(rows, "semantic_reject")
    parse_errors = _rows_with_status(rows, "judge_parse_error")
    semantic_reasons = Counter(str(row.get("main_failure_reason", "")) for row in semantic_rejects)
    semantic_fixes = Counter(str(row.get("one_prompt_fix", "")) for row in semantic_rejects)

    lines = [
        "# AHD VLM Image Judge Summary",
        "",
        f"- total_rows: {stats['total_rows']}",
        f"- generation_failed_count: {stats['generation_failed_count']}",
        f"- missing_or_invalid_image_count: {stats['missing_or_invalid_image_count']}",
        f"- judge_parse_error_count: {stats['judge_parse_error_count']}",
        f"- valid_images_judged_count: {stats['valid_images_judged_count']}",
        f"- semantic_keep_count: {stats['semantic_keep_count']}",
        f"- semantic_reject_count: {stats['semantic_reject_count']}",
        f"- semantic_keep_rate_among_valid_images: {stats['semantic_keep_rate_among_valid_images']:.1f}%",
        f"- overall_keep_rate_over_total_rows: {stats['overall_keep_rate_over_total_rows']:.1f}%",
        "",
        "## Status By Spec Type",
        "",
    ]
    for spec_type in sorted(by_type):
        group_stats = _status_counts(by_type[spec_type])
        lines.append(
            f"- {spec_type}: total={group_stats['total_rows']}, "
            f"generation_failed={group_stats['generation_failed_count']}, "
            f"missing_or_invalid_image={group_stats['missing_or_invalid_image_count']}, "
            f"semantic_keep={group_stats['semantic_keep_count']}, "
            f"semantic_reject={group_stats['semantic_reject_count']}, "
            f"valid_images_judged={group_stats['valid_images_judged_count']}, "
            f"semantic_keep_rate_valid_only={group_stats['semantic_keep_rate_among_valid_images']:.1f}%"
        )

    lines.extend(["", "## A. Generation Failures", ""])
    if generation_failures:
        for row in generation_failures:
            lines.append(f"- {row.get('spec_id')}: {row.get('generation_error_short') or row.get('main_failure_reason')}")
    else:
        lines.append("- none")

    lines.extend(["", "## B. Missing/Invalid Image Failures", ""])
    if missing_invalid:
        for row in missing_invalid:
            lines.append(f"- {row.get('spec_id')}: {row.get('main_failure_reason')}")
    else:
        lines.append("- none")

    lines.extend(["", "## C. Semantic Rejects", ""])
    if semantic_rejects:
        for row in semantic_rejects:
            lines.append(
                f"- {row.get('spec_id')} ({row.get('spec_type')}): "
                f"{row.get('main_failure_reason')}; fix: {row.get('one_prompt_fix')}"
            )
    else:
        lines.append("- none")

    lines.extend(["", "## D. Judge Parse Errors", ""])
    if parse_errors:
        for row in parse_errors:
            lines.append(f"- {row.get('spec_id')}: {row.get('judge_parse_error')}")
    else:
        lines.append("- none")

    lines.extend(["", "## Semantic Reject Reasons", ""])
    if semantic_reasons:
        for reason, count in semantic_reasons.most_common():
            lines.append(f"- {reason or '(empty)'}: {count}")
    else:
        lines.append("- none")

    lines.extend(["", "## Semantic One Prompt Fix Frequency", ""])
    if semantic_fixes:
        for fix, count in semantic_fixes.most_common():
            lines.append(f"- {fix or '(empty)'}: {count}")
    else:
        lines.append("- none")

    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_spec_type_summary(path: Path, rows: list[dict[str, Any]]) -> None:
    by_type: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in rows:
        by_type[str(row.get("spec_type", ""))].append(row)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=[
            "spec_type",
            "total",
            "generation_failed",
            "missing_or_invalid_image",
            "semantic_keep",
            "semantic_reject",
            "valid_images_judged",
            "semantic_keep_rate_valid_only",
        ])
        writer.writeheader()
        for spec_type in sorted(by_type):
            stats = _status_counts(by_type[spec_type])
            writer.writerow({
                "spec_type": spec_type,
                "total": stats["total_rows"],
                "generation_failed": stats["generation_failed_count"],
                "missing_or_invalid_image": stats["missing_or_invalid_image_count"],
                "semantic_keep": stats["semantic_keep_count"],
                "semantic_reject": stats["semantic_reject_count"],
                "valid_images_judged": stats["valid_images_judged_count"],
                "semantic_keep_rate_valid_only": f"{stats['semantic_keep_rate_among_valid_images']:.1f}",
            })


def _status_counts(rows: list[dict[str, Any]]) -> dict[str, float]:
    total = len(rows)
    generation_failed = len(_rows_with_status(rows, "generation_failed"))
    missing_invalid = len(_rows_with_status(rows, "missing_or_invalid_image"))
    parse_errors = len(_rows_with_status(rows, "judge_parse_error"))
    semantic_keep = len(_rows_with_status(rows, "semantic_keep"))
    semantic_reject = len(_rows_with_status(rows, "semantic_reject"))
    valid_judged = semantic_keep + semantic_reject
    return {
        "total_rows": total,
        "generation_failed_count": generation_failed,
        "missing_or_invalid_image_count": missing_invalid,
        "judge_parse_error_count": parse_errors,
        "valid_images_judged_count": valid_judged,
        "semantic_keep_count": semantic_keep,
        "semantic_reject_count": semantic_reject,
        "semantic_keep_rate_among_valid_images": (semantic_keep / valid_judged * 100) if valid_judged else 0.0,
        "overall_keep_rate_over_total_rows": (semantic_keep / total * 100) if total else 0.0,
    }


def _rows_with_status(rows: list[dict[str, Any]], status: str) -> list[dict[str, Any]]:
    return [row for row in rows if row.get("image_judge_status") == status]


def _resolve_path(path_text: str) -> Path:
    path = Path(path_text)
    return path if path.is_absolute() else ROOT / path


if __name__ == "__main__":
    main()
