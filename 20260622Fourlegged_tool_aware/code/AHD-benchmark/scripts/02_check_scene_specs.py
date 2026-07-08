from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.jsonl_utils import read_jsonl, write_jsonl
from src.load_config import load_yaml
from src.schema import validate_scene_spec
from src.spec_checks import (
    check_duplicate_spec_id,
    check_forbidden_leakage,
    check_generation_plan_totals,
    check_spec_counts_against_plan,
    count_specs,
)


def _format_counts(title: str, counts: dict[str, int]) -> list[str]:
    lines = [f"## {title}", ""]
    for key, value in sorted(counts.items()):
        lines.append(f"- {key}: {value}")
    lines.append("")
    return lines


def main() -> None:
    plan = load_yaml(ROOT / "configs" / "generation_plan_v01.yaml")
    specs = read_jsonl(ROOT / "specs" / "scene_specs_raw.jsonl")
    errors: list[str] = []
    errors.extend(check_generation_plan_totals(plan))
    errors.extend(check_spec_counts_against_plan(specs, plan))
    errors.extend(check_duplicate_spec_id(specs))

    valid_specs: list[dict] = []
    for spec in specs:
        spec_errors = validate_scene_spec(spec) + check_forbidden_leakage(spec)
        if spec_errors:
            errors.extend(f"{spec.get('spec_id', '<missing id>')}: {error}" for error in spec_errors)
        else:
            spec["quality"] = {
                "checked": True,
                "status": "checked",
                "notes": [],
            }
            valid_specs.append(spec)

    counts = count_specs(valid_specs)
    report_lines = [
        "# AHD Scene Spec Check Report",
        "",
        f"- Input specs: {len(specs)}",
        f"- Valid specs: {len(valid_specs)}",
        f"- Errors: {len(errors)}",
        "",
    ]
    report_lines.extend(_format_counts("Counts By View Stage", dict(counts["view_stage"])))
    report_lines.extend(_format_counts("Counts By Spec Type", dict(counts["spec_type"])))
    report_lines.extend(_format_counts("Counts By Task Family", dict(counts["task_family"])))
    if errors:
        report_lines.append("## Errors")
        report_lines.append("")
        report_lines.extend(f"- {error}" for error in errors[:200])
        if len(errors) > 200:
            report_lines.append(f"- ... truncated {len(errors) - 200} additional errors")

    (ROOT / "specs" / "scene_specs_check_report.md").write_text("\n".join(report_lines) + "\n", encoding="utf-8")

    if errors:
        raise SystemExit(f"Scene spec check failed with {len(errors)} errors. See specs/scene_specs_check_report.md")

    o0_specs = [spec for spec in valid_specs if spec["view_stage"] == "O0"]
    o1_specs = [spec for spec in valid_specs if spec["view_stage"] == "O1"]
    write_jsonl(ROOT / "specs" / "scene_specs_checked.jsonl", valid_specs)
    write_jsonl(ROOT / "specs" / "o0_scene_specs_checked.jsonl", o0_specs)
    write_jsonl(ROOT / "specs" / "o1_scene_specs_checked.jsonl", o1_specs)
    print(f"Checked {len(valid_specs)} specs. Report: specs/scene_specs_check_report.md")


if __name__ == "__main__":
    main()
