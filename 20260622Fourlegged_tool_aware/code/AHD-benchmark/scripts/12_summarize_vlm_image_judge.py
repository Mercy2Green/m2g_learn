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
    total = len(rows)
    keep_count = sum(1 for row in rows if row.get("keep") is True)
    reject_count = total - keep_count
    keep_rate = keep_count / total * 100 if total else 0.0
    by_type: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in rows:
        by_type[str(row.get("spec_type", ""))].append(row)
    reject_reasons = Counter(str(row.get("main_failure_reason", "")) for row in rows if row.get("keep") is False)
    fixes = Counter(str(row.get("one_prompt_fix", "")) for row in rows if row.get("keep") is False)
    parse_errors = [row for row in rows if row.get("judge_parse_error")]

    lines = [
        "# AHD VLM Image Judge Summary",
        "",
        f"- total: {total}",
        f"- keep_count: {keep_count}",
        f"- reject_count: {reject_count}",
        f"- keep_rate: {keep_rate:.1f}%",
        "",
        "## Keep/Reject By Spec Type",
        "",
    ]
    for spec_type in sorted(by_type):
        group = by_type[spec_type]
        group_keep = sum(1 for row in group if row.get("keep") is True)
        group_reject = len(group) - group_keep
        lines.append(f"- {spec_type}: keep={group_keep}, reject={group_reject}, total={len(group)}")

    lines.extend(["", "## Reject Reasons", ""])
    if reject_reasons:
        for reason, count in reject_reasons.most_common():
            lines.append(f"- {reason or '(empty)'}: {count}")
    else:
        lines.append("- none")

    lines.extend(["", "## One Prompt Fix Frequency", ""])
    if fixes:
        for fix, count in fixes.most_common():
            lines.append(f"- {fix or '(empty)'}: {count}")
    else:
        lines.append("- none")

    lines.extend(["", "## Rejected Spec IDs", ""])
    rejected = [row for row in rows if row.get("keep") is False]
    if rejected:
        for row in rejected:
            lines.append(
                f"- {row.get('spec_id')} ({row.get('spec_type')}): "
                f"{row.get('main_failure_reason')}; fix: {row.get('one_prompt_fix')}"
            )
    else:
        lines.append("- none")

    lines.extend(["", "## Judge Parse Errors", ""])
    if parse_errors:
        for row in parse_errors:
            lines.append(f"- {row.get('spec_id')}: {row.get('judge_parse_error')}")
    else:
        lines.append("- none")

    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_spec_type_summary(path: Path, rows: list[dict[str, Any]]) -> None:
    by_type: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in rows:
        by_type[str(row.get("spec_type", ""))].append(row)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=["spec_type", "total", "keep", "reject", "keep_rate"])
        writer.writeheader()
        for spec_type in sorted(by_type):
            group = by_type[spec_type]
            keep = sum(1 for row in group if row.get("keep") is True)
            total = len(group)
            writer.writerow({
                "spec_type": spec_type,
                "total": total,
                "keep": keep,
                "reject": total - keep,
                "keep_rate": f"{(keep / total * 100 if total else 0):.1f}",
            })


def _resolve_path(path_text: str) -> Path:
    path = Path(path_text)
    return path if path.is_absolute() else ROOT / path


if __name__ == "__main__":
    main()
