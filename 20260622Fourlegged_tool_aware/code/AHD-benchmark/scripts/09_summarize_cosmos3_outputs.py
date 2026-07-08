from __future__ import annotations

import argparse
from collections import Counter
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.cosmos3_manifest import load_manifest  # noqa: E402


def main() -> None:
    parser = argparse.ArgumentParser(description="Summarize Cosmos3 batch result JSONL.")
    parser.add_argument("--results", required=True)
    parser.add_argument("--output", default=None)
    args = parser.parse_args()

    results_path = _resolve_path(args.results)
    rows = load_manifest(results_path)
    total = len(rows)
    success = sum(1 for row in rows if row.get("status") == "success")
    failed = total - success
    rate = (success / total * 100.0) if total else 0.0
    by_type = Counter(str(row.get("spec_type", "")) for row in rows)
    by_type_success = Counter(str(row.get("spec_type", "")) for row in rows if row.get("status") == "success")
    by_size = Counter(
        f"{row.get('width')}x{row.get('height')}"
        for row in rows
        if row.get("width") is not None and row.get("height") is not None
    )

    lines = [
        f"# Cosmos3 Run Summary: {results_path.stem}",
        "",
        f"- total: {total}",
        f"- success: {success}",
        f"- failed: {failed}",
        f"- success_rate: {rate:.1f}%",
        "",
        "## Width/Height Distribution",
        "",
    ]
    if by_size:
        lines.extend(f"- {size}: {count}" for size, count in sorted(by_size.items()))
    else:
        lines.append("- No valid image dimensions recorded.")

    lines.extend(["", "## Counts By Spec Type", ""])
    for spec_type in sorted(by_type):
        lines.append(f"- {spec_type}: {by_type_success[spec_type]}/{by_type[spec_type]} success")

    failures = [row for row in rows if row.get("status") != "success"]
    if failures:
        lines.extend(["", "## Failures", ""])
        for row in failures:
            lines.append(f"- {row.get('spec_id')}: {row.get('error')}")

    output_path = _resolve_path(args.output) if args.output else results_path.with_name(results_path.name.replace("_results.jsonl", "_summary.md"))
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Wrote summary: {output_path}")


def _resolve_path(path_text: str) -> Path:
    path = Path(path_text)
    return path if path.is_absolute() else ROOT / path


if __name__ == "__main__":
    main()
