from __future__ import annotations

import argparse
from collections import Counter
import json
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.enrichment_schema import check_forbidden_label_leakage, validate_enrichment_row


def _prompt_length(row: dict[str, Any]) -> int:
    return len(str(row.get("cosmos_prompt_variant", "")))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("enrichment_jsonl", help="Path to an enrichment preview JSONL file.")
    args = parser.parse_args()

    input_path = Path(args.enrichment_jsonl)
    if not input_path.is_absolute():
        input_path = ROOT / input_path
    if not input_path.exists():
        raise SystemExit(f"Enrichment file not found: {input_path}")

    total_rows = 0
    parse_failures = 0
    schema_failures = 0
    leakage_failures = 0
    prompt_lengths: list[int] = []
    note_counts: Counter[str] = Counter()
    examples: list[str] = []

    with input_path.open("r", encoding="utf-8") as handle:
        for line_no, line in enumerate(handle, start=1):
            stripped = line.strip()
            if not stripped:
                continue
            total_rows += 1
            try:
                row = json.loads(stripped)
            except json.JSONDecodeError as exc:
                parse_failures += 1
                examples.append(f"line {line_no}: JSON parse failure: {exc}")
                continue
            if not isinstance(row, dict):
                parse_failures += 1
                examples.append(f"line {line_no}: row is not an object")
                continue
            notes = row.get("notes", [])
            row_schema_note_failure = False
            row_leakage_note_failure = False
            if isinstance(notes, list):
                for note in notes:
                    note_text = str(note)
                    if "parse_error" in note_text:
                        parse_failures += 1
                    if note_text.startswith("schema_error:"):
                        row_schema_note_failure = True
                    if note_text.startswith("leakage_error:"):
                        row_leakage_note_failure = True
                    note_counts[note_text.split(":", 1)[0]] += 1

            schema_errors = validate_enrichment_row(row)
            leakage_errors = check_forbidden_label_leakage(row)
            if schema_errors or row_schema_note_failure:
                schema_failures += 1
                examples.extend(f"{row.get('spec_id', f'line {line_no}')}: {error}" for error in schema_errors[:3])
            if leakage_errors or row_leakage_note_failure:
                leakage_failures += 1
                examples.extend(f"{row.get('spec_id', f'line {line_no}')}: {error}" for error in leakage_errors[:3])
            prompt_lengths.append(_prompt_length(row))

    average_prompt_length = sum(prompt_lengths) / len(prompt_lengths) if prompt_lengths else 0.0
    report_lines = [
        "# LLM Enrichment Check Report",
        "",
        f"- Input file: `{input_path.relative_to(ROOT) if input_path.is_relative_to(ROOT) else input_path}`",
        f"- Total rows: {total_rows}",
        f"- JSON parse failures: {parse_failures}",
        f"- Schema failures: {schema_failures}",
        f"- Leakage failures: {leakage_failures}",
        f"- Average prompt length: {average_prompt_length:.1f}",
        "",
        "## Note Summary",
        "",
    ]
    if note_counts:
        report_lines.extend(f"- {key}: {value}" for key, value in sorted(note_counts.items()))
    else:
        report_lines.append("- none")
    report_lines.extend(["", "## Examples", ""])
    report_lines.extend(f"- {item}" for item in examples[:50]) if examples else report_lines.append("- none")

    report_path = input_path.with_name(f"{input_path.stem}_report.md")
    report_path.write_text("\n".join(report_lines) + "\n", encoding="utf-8")
    print("\n".join(report_lines))
    print(f"Saved {report_path.relative_to(ROOT) if report_path.is_relative_to(ROOT) else report_path}")


if __name__ == "__main__":
    main()
