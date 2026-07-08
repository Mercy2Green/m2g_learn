from __future__ import annotations

import argparse
import csv
from pathlib import Path
import sys
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.jsonl_utils import read_jsonl  # noqa: E402


AUDIT_COLUMNS = [
    "spec_id",
    "spec_type",
    "view_stage",
    "image_path",
    "expected_core_condition",
    "target_visible_ok",
    "helper_absent_ok",
    "helper_visible_ok",
    "forbidden_object_leakage",
    "count_reasonable",
    "camera_view_ok",
    "overall_usable",
    "notes",
]


def main() -> None:
    parser = argparse.ArgumentParser(description="Create a manual visual audit sheet from Cosmos3 result JSONL.")
    parser.add_argument("--results", required=True)
    parser.add_argument("--output_stem", default=None)
    args = parser.parse_args()

    results_path = _resolve_path(args.results)
    rows = read_jsonl(results_path)
    if not rows:
        raise SystemExit(f"Results file not found or empty: {results_path}")

    output_dir = ROOT / "data" / "audits"
    output_dir.mkdir(parents=True, exist_ok=True)
    stem = args.output_stem or results_path.stem.replace("_results", "")
    audit_rows = [_audit_row(row) for row in rows]

    csv_path = output_dir / f"{stem}_visual_audit.csv"
    md_path = output_dir / f"{stem}_visual_audit.md"
    _write_csv(csv_path, audit_rows)
    _write_markdown(md_path, audit_rows)
    print(f"Wrote CSV audit sheet: {csv_path}")
    print(f"Wrote Markdown audit sheet: {md_path}")


def _audit_row(row: dict[str, Any]) -> dict[str, str]:
    spec_type = str(row.get("spec_type", ""))
    return {
        "spec_id": str(row.get("spec_id", "")),
        "spec_type": spec_type,
        "view_stage": str(row.get("view_stage", "")),
        "image_path": str(row.get("output_image_path") or row.get("image_path") or ""),
        "expected_core_condition": _expected_core_condition(spec_type),
        "target_visible_ok": "",
        "helper_absent_ok": "",
        "helper_visible_ok": "",
        "forbidden_object_leakage": "",
        "count_reasonable": "",
        "camera_view_ok": "",
        "overall_usable": "",
        "notes": "",
    }


def _expected_core_condition(spec_type: str) -> str:
    if spec_type == "aggregate_transport_o0_target_visible_helper_absent":
        return "O0: multiple target drinks visible; count >= 3 is acceptable; container/helper absent"
    if spec_type == "extend_reach_o0_target_under_furniture":
        return "O0: target partly visible under compatible furniture; long tool/helper absent"
    if spec_type == "direct_is_enough_o0_single_target":
        return "O0: single reachable target visible; helper absent"
    if spec_type == "container_helper_o1_target_absent":
        return "O1: container-like helper visible; original target absent or non-salient"
    if spec_type == "long_tool_helper_o1_target_absent":
        return "O1: long rigid helper visible; original target absent or non-salient"
    if spec_type == "wrong_helper_o1_target_absent":
        return "O1: wrong helper/distractor visible; original target and correct helper absent"
    return "Manual check required"


def _write_csv(path: Path, rows: list[dict[str, str]]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=AUDIT_COLUMNS)
        writer.writeheader()
        writer.writerows(rows)


def _write_markdown(path: Path, rows: list[dict[str, str]]) -> None:
    lines = [
        f"# Visual Audit Sheet: {path.stem.removesuffix('_visual_audit')}",
        "",
        "| " + " | ".join(AUDIT_COLUMNS) + " |",
        "| " + " | ".join("---" for _ in AUDIT_COLUMNS) + " |",
    ]
    for row in rows:
        values = [_escape_markdown_table(row[column]) for column in AUDIT_COLUMNS]
        lines.append("| " + " | ".join(values) + " |")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def _escape_markdown_table(value: str) -> str:
    return value.replace("|", "\\|").replace("\n", " ")


def _resolve_path(path_text: str) -> Path:
    path = Path(path_text)
    return path if path.is_absolute() else ROOT / path


if __name__ == "__main__":
    main()
