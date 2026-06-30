from __future__ import annotations

import argparse
import json
import shutil
import sys
import tempfile
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

if __package__ is None or __package__ == "":
    sys.path.insert(0, str(Path(__file__).resolve().parent))

from common import compact_text, normalize_list_field, read_jsonl, write_csv_dicts  # noqa: E402


DEFAULT_REREVIEW = "analysis_review/round02_full_important_outputs/case_rereview.jsonl"
DEFAULT_MERGED = "analysis_review/round02_full_important_outputs/all_rows_merged.jsonl"
DEFAULT_OUTPUT_DIR = "analysis_review/round03_human_visual_review_pack"

PROMPT_PAIRS = {
    "natural_free_plan": "tool_prior_free_plan",
    "natural_free_plan_humanoid_dual_arm": "tool_prior_free_plan_humanoid_dual_arm",
    "natural_free_plan_quadruped_single_arm": "tool_prior_free_plan_quadruped_single_arm",
}

RECOMMENDED_TASKS = {
    "task_001",
    "task_002",
    "task_004",
    "task_005",
    "task_006",
    "task_008",
}

OPTIONAL_TASKS = {"task_007", "task_009", "task_010"}

HIGH_VALUE_FAILURES = {
    "aggregation_failure",
    "container_affordance_miss",
    "helper_search_failure",
    "physical_capacity_hallucination",
    "wrong_helper_type",
    "tool_necessity_miss",
}

REVIEWER_FIELDS = [
    "reviewer_image_target_visible",
    "reviewer_helper_visible",
    "reviewer_helper_needed_by_task",
    "reviewer_expected_helper_reasonable",
    "reviewer_model_plan_physically_feasible",
    "reviewer_model_failure_confirmed",
    "reviewer_claim_safe_to_use",
    "reviewer_notes",
]

CSV_FIELDS = [
    "review_case_id",
    "case_tier",
    "failure_family",
    "task_id",
    "task_name",
    "image_name",
    "image_path",
    "copied_image_path",
    "model_id",
    "prompt_id",
    "prompt_category",
    "prompt_type",
    "embodiment_profile",
    "rereview_label",
    "rereview_confidence",
    "rereview_failure_modes",
    "evidence_quote",
    "model_plan_short",
    "expected_should_use_tool_or_container",
    "expected_tool_or_container_types",
    "expected_should_search_for_tool_if_not_visible",
    "expected_should_avoid_over_tool_use",
    "expected_trip_pattern",
    "target_object_terms",
    "task_instruction",
] + REVIEWER_FIELDS


def main() -> None:
    args = parse_args()
    if args.self_test:
        run_self_test()
        return

    rereview_rows = read_jsonl(args.rereview_jsonl)
    merged_rows = read_jsonl(args.merged_jsonl)
    enriched = enrich_rows(rereview_rows, merged_rows)
    selected = select_cases(
        enriched,
        max_cases=args.max_cases,
        include_prompted_improvements=args.include_prompted_improvements,
        include_uncertain=args.include_uncertain,
    )
    output_dir = Path(args.output_dir)
    write_pack(selected, output_dir, copy_images=args.copy_images)
    summary = summarize_selection(selected)
    print(json.dumps({"output_dir": str(output_dir), **summary}, ensure_ascii=False))


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Create a human visual review pack from rereviewed benchmark rows.")
    parser.add_argument("--rereview_jsonl", default=DEFAULT_REREVIEW)
    parser.add_argument("--merged_jsonl", default=DEFAULT_MERGED)
    parser.add_argument("--output_dir", default=DEFAULT_OUTPUT_DIR)
    parser.add_argument("--max_cases", type=int, default=40)
    parser.add_argument("--include_prompted_improvements", action="store_true")
    parser.add_argument("--include_uncertain", action="store_true")
    parser.add_argument("--copy_images", action="store_true")
    parser.add_argument("--self_test", action="store_true")
    return parser.parse_args()


def enrich_rows(rereview_rows: list[dict[str, Any]], merged_rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    merged_index: dict[tuple[str, str, str, str, str], dict[str, Any]] = {}
    for row in merged_rows:
        key = row_key(row)
        merged_index[key] = row

    enriched: list[dict[str, Any]] = []
    for row in rereview_rows:
        merged = merged_index.get(row_key(row), {})
        combined = dict(merged)
        combined.update(row)
        if not combined.get("image_path"):
            combined["image_path"] = merged.get("image_path", "")
        if not combined.get("task_instruction"):
            combined["task_instruction"] = merged.get("task_instruction", "")
        enriched.append(combined)
    return enriched


def row_key(row: dict[str, Any]) -> tuple[str, str, str, str, str]:
    image_name = str(row.get("image_name") or Path(str(row.get("image_path", ""))).name)
    return (
        str(row.get("run_id", "")),
        str(row.get("task_id", "")),
        image_name,
        str(row.get("model_id", "")),
        str(row.get("prompt_id", "")),
    )


def select_cases(
    rows: list[dict[str, Any]],
    max_cases: int,
    include_prompted_improvements: bool,
    include_uncertain: bool,
) -> list[dict[str, Any]]:
    clean_fail_rows = [row for row in rows if is_clean_candidate(row)]
    reproduction = clean_reproduction_counts(clean_fail_rows)

    candidates: list[dict[str, Any]] = []
    for row in clean_fail_rows:
        candidates.append(make_candidate(row, "clean_counterexample", reproduction))

    candidates.extend(make_robust_failure_candidates(rows, reproduction))
    if include_prompted_improvements:
        candidates.extend(make_prompted_improvement_candidates(rows, reproduction))
    if include_uncertain:
        candidates.extend(make_uncertain_candidates(rows, reproduction))

    candidates = deduplicate_candidates(candidates)
    candidates.sort(key=candidate_sort_key, reverse=True)
    selected = enforce_group_limits(candidates, max_cases=max_cases, per_group_limit=3)
    for idx, row in enumerate(selected, start=1):
        row["review_case_id"] = f"VR{idx:03d}"
        for field in REVIEWER_FIELDS:
            row[field] = ""
    return selected


def is_clean_candidate(row: dict[str, Any]) -> bool:
    if not truthy(row.get("primary_for_counterexample")):
        return False
    if row.get("rereview_label") != "true_fail":
        return False
    if row.get("rereview_confidence") not in {"high", "medium"}:
        return False
    if row.get("rereview_label") in {"parse_error", "skipped"}:
        return False
    modes = set(normalize_list_field(row.get("rereview_failure_modes")))
    return row.get("task_id") in RECOMMENDED_TASKS or bool(modes & HIGH_VALUE_FAILURES)


def clean_reproduction_counts(rows: list[dict[str, Any]]) -> Counter[tuple[str, str, str]]:
    grouped: dict[tuple[str, str, str], set[str]] = defaultdict(set)
    for row in rows:
        family = failure_family(row)
        grouped[(str(row.get("task_id", "")), image_name(row), family)].add(str(row.get("model_id", "")))
    return Counter({key: len(models) for key, models in grouped.items()})


def make_robust_failure_candidates(rows: list[dict[str, Any]], reproduction: Counter[tuple[str, str, str]]) -> list[dict[str, Any]]:
    by_key = comparison_index(rows)
    output: list[dict[str, Any]] = []
    for clean_prompt, tool_prompt in PROMPT_PAIRS.items():
        for row in rows:
            if row.get("prompt_id") != clean_prompt or row.get("rereview_label") != "true_fail":
                continue
            tool_row = by_key.get(comparison_key(row, tool_prompt))
            if not tool_row or tool_row.get("rereview_label") != "true_fail":
                continue
            if row.get("rereview_confidence") not in {"high", "medium"}:
                continue
            candidate = make_candidate(row, "robust_failure", reproduction)
            candidate["tier_note"] = f"Matching {tool_prompt} also failed for the same task/image/model/embodiment."
            output.append(candidate)
    return output


def make_prompted_improvement_candidates(rows: list[dict[str, Any]], reproduction: Counter[tuple[str, str, str]]) -> list[dict[str, Any]]:
    by_key = comparison_index(rows)
    output: list[dict[str, Any]] = []
    for clean_prompt, tool_prompt in PROMPT_PAIRS.items():
        for clean_row in rows:
            if clean_row.get("prompt_id") != clean_prompt or clean_row.get("rereview_label") != "true_fail":
                continue
            tool_row = by_key.get(comparison_key(clean_row, tool_prompt))
            if not tool_row or tool_row.get("rereview_label") != "true_pass":
                continue
            candidate = make_candidate(tool_row, "prompted_improvement", reproduction)
            candidate["tier_note"] = f"{clean_prompt} failed but {tool_prompt} passed; not clean evidence."
            output.append(candidate)
    return output


def make_uncertain_candidates(rows: list[dict[str, Any]], reproduction: Counter[tuple[str, str, str]]) -> list[dict[str, Any]]:
    output: list[dict[str, Any]] = []
    for row in rows:
        modes = set(normalize_list_field(row.get("rereview_failure_modes")))
        if row.get("rereview_label") == "parse_error" or row.get("rereview_label") == "skipped":
            continue
        if row.get("rereview_label") == "uncertain" or row.get("needs_visual_check") == "yes" or "visual_uncertainty" in modes:
            candidate = make_candidate(row, "uncertain_visual", reproduction)
            candidate["tier_note"] = "Text-only review needs image-level confirmation."
            output.append(candidate)
    return output


def comparison_index(rows: list[dict[str, Any]]) -> dict[tuple[str, str, str, str, str], dict[str, Any]]:
    return {comparison_key(row, str(row.get("prompt_id", ""))): row for row in rows}


def comparison_key(row: dict[str, Any], prompt_id: str) -> tuple[str, str, str, str, str]:
    return (
        str(row.get("task_id", "")),
        image_name(row),
        str(row.get("model_id", "")),
        str(row.get("embodiment_profile", "")),
        prompt_id,
    )


def make_candidate(row: dict[str, Any], case_tier: str, reproduction: Counter[tuple[str, str, str]]) -> dict[str, Any]:
    family = failure_family(row)
    reproduced = reproduction.get((str(row.get("task_id", "")), image_name(row), family), 0)
    output = dict(row)
    output["case_tier"] = case_tier
    output["failure_family"] = family
    output["reproduced_model_count"] = reproduced
    output["model_plan_short"] = compact_text(
        row.get("parsed_plan") or row.get("evidence_quote") or row.get("raw_response_short") or "",
        max_chars=500,
    )
    output["evidence_quote"] = compact_text(row.get("evidence_quote") or output["model_plan_short"], max_chars=500)
    output["image_name"] = image_name(row)
    output["copied_image_path"] = ""
    return output


def failure_family(row: dict[str, Any]) -> str:
    modes = set(normalize_list_field(row.get("rereview_failure_modes")))
    task_id = str(row.get("task_id", ""))
    if "over_tool_use" in modes or row.get("over_tool_use") == "yes" or task_id == "task_011":
        return "over_tool_use_control"
    if "helper_search_failure" in modes:
        return "helper_search"
    if "wrong_helper_type" in modes:
        return "wrong_helper_type"
    if "physical_capacity_hallucination" in modes:
        return "physical_capacity"
    if "tool_necessity_miss" in modes or task_id == "task_008":
        return "reach_extension"
    if "helper_mention_without_use" in modes or row.get("helper_only_mentioned_not_used") == "yes":
        return "helper_mention_without_use"
    if modes & {"aggregation_failure", "container_affordance_miss"}:
        return "aggregation_container"
    if "parse_failure" in modes:
        return "parse_or_format"
    return "other"


def deduplicate_candidates(candidates: list[dict[str, Any]]) -> list[dict[str, Any]]:
    seen: set[tuple[str, str, str, str, str, str]] = set()
    unique: list[dict[str, Any]] = []
    for row in candidates:
        key = (
            str(row.get("case_tier", "")),
            str(row.get("task_id", "")),
            image_name(row),
            str(row.get("model_id", "")),
            str(row.get("prompt_id", "")),
            str(row.get("failure_family", "")),
        )
        if key in seen:
            continue
        seen.add(key)
        unique.append(row)
    return unique


def candidate_sort_key(row: dict[str, Any]) -> tuple[int, int, int, int, int, int, int]:
    tier_score = {
        "clean_counterexample": 4000,
        "robust_failure": 3000,
        "prompted_improvement": 2000,
        "uncertain_visual": 1000,
        "control": 500,
    }.get(str(row.get("case_tier", "")), 0)
    confidence_score = {"high": 2, "medium": 1, "low": 0}.get(str(row.get("rereview_confidence", "")), 0)
    task_score = 2 if row.get("task_id") in RECOMMENDED_TASKS else 1 if row.get("task_id") in OPTIONAL_TASKS else 0
    visual_score = 1 if row.get("needs_visual_check") == "yes" else 0
    reproduced = int(row.get("reproduced_model_count") or 0)
    evidence_short = 1 if len(str(row.get("evidence_quote", ""))) < 280 else 0
    prompt_score = 2 if row.get("prompt_type") == "primary_clean" else 1 if row.get("prompt_category") == "tool_prior_intervention" else 0
    return (tier_score, reproduced, confidence_score, task_score, visual_score, prompt_score, evidence_short)


def enforce_group_limits(candidates: list[dict[str, Any]], max_cases: int, per_group_limit: int) -> list[dict[str, Any]]:
    selected: list[dict[str, Any]] = []
    group_counts: Counter[tuple[str, str, str]] = Counter()
    selected_ids: set[tuple[str, str, str, str, str, str]] = set()

    tier_candidates: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in candidates:
        tier_candidates[str(row.get("case_tier", ""))].append(row)

    quotas = tier_quotas(tier_candidates, max_cases)
    for tier in ["clean_counterexample", "robust_failure", "prompted_improvement", "uncertain_visual", "control"]:
        quota = quotas.get(tier, 0)
        for row in tier_candidates.get(tier, []):
            if quota <= 0 or len(selected) >= max_cases:
                break
            if add_candidate(row, selected, selected_ids, group_counts, per_group_limit):
                quota -= 1

    for row in candidates:
        if len(selected) >= max_cases:
            break
        add_candidate(row, selected, selected_ids, group_counts, per_group_limit)
    return selected


def tier_quotas(tier_candidates: dict[str, list[dict[str, Any]]], max_cases: int) -> dict[str, int]:
    if max_cases <= 0:
        return {}
    robust = min(len(tier_candidates.get("robust_failure", [])), max(1, max_cases // 7))
    prompted = min(len(tier_candidates.get("prompted_improvement", [])), max(1, max_cases // 10))
    uncertain = min(len(tier_candidates.get("uncertain_visual", [])), max(1, max_cases // 10))
    clean = max_cases - robust - prompted - uncertain
    if clean < max_cases // 2:
        clean = max_cases // 2
    return {
        "clean_counterexample": clean,
        "robust_failure": robust,
        "prompted_improvement": prompted,
        "uncertain_visual": uncertain,
        "control": 0,
    }


def add_candidate(
    row: dict[str, Any],
    selected: list[dict[str, Any]],
    selected_ids: set[tuple[str, str, str, str, str, str]],
    group_counts: Counter[tuple[str, str, str]],
    per_group_limit: int,
) -> bool:
    row_id = (
        str(row.get("case_tier", "")),
        str(row.get("task_id", "")),
        image_name(row),
        str(row.get("model_id", "")),
        str(row.get("prompt_id", "")),
        str(row.get("failure_family", "")),
    )
    if row_id in selected_ids:
        return False
    group_key = (str(row.get("task_id", "")), image_name(row), str(row.get("failure_family", "")))
    if group_counts[group_key] >= per_group_limit:
        return False
    selected.append(row)
    selected_ids.add(row_id)
    group_counts[group_key] += 1
    return True


def write_pack(rows: list[dict[str, Any]], output_dir: Path, copy_images: bool) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    if copy_images:
        copy_selected_images(rows, output_dir / "images")
    write_csv_dicts(output_dir / "visual_review_sheet.csv", rows, CSV_FIELDS)
    write_visual_cases(output_dir / "visual_review_cases.md", rows)
    write_summary(output_dir / "visual_review_summary.md", rows)
    write_readme(output_dir / "README.md")


def copy_selected_images(rows: list[dict[str, Any]], image_dir: Path) -> None:
    image_dir.mkdir(parents=True, exist_ok=True)
    used_names: set[str] = set()
    for row in rows:
        source = Path(str(row.get("image_path", "")))
        if not source.exists():
            row["copied_image_path"] = ""
            continue
        target_name = source.name
        if target_name in used_names:
            target_name = f"{row.get('review_case_id', 'case')}_{target_name}"
        used_names.add(target_name)
        target = image_dir / target_name
        shutil.copy2(source, target)
        row["copied_image_path"] = str(target)


def write_visual_cases(path: Path, rows: list[dict[str, Any]]) -> None:
    grouped: dict[tuple[str, str], list[dict[str, Any]]] = defaultdict(list)
    for row in rows:
        grouped[(str(row.get("task_id", "")), str(row.get("failure_family", "")))].append(row)
    lines = [
        "# Visual Review Cases",
        "",
        "These cases are selected for human image-level verification. Text rereview is not final evidence.",
        "",
    ]
    for (task_id, family), group_rows in sorted(grouped.items()):
        lines.extend([f"## {task_id} / {family}", ""])
        for row in group_rows:
            lines.extend(
                [
                    f"### {row.get('review_case_id')} - {row.get('case_tier')}",
                    "",
                    f"- Task instruction: {row.get('task_instruction', '')}",
                    f"- Image path: {row.get('image_path', '')}",
                    f"- Expected helper/tool behavior: use={row.get('expected_should_use_tool_or_container', '')}; "
                    f"types={row.get('expected_tool_or_container_types', '')}; "
                    f"search={row.get('expected_should_search_for_tool_if_not_visible', '')}",
                    f"- Model/prompt: {row.get('model_id', '')} / {row.get('prompt_id', '')} / {row.get('embodiment_profile', '')}",
                    f"- Model output excerpt: {row.get('evidence_quote', '')}",
                    f"- Rereview judgment: {row.get('rereview_label', '')} ({row.get('rereview_confidence', '')}); "
                    f"modes={row.get('rereview_failure_modes', '')}",
                    "",
                    "Human checks:",
                    "- [ ] Is the target object visible?",
                    "- [ ] Is the expected helper visible?",
                    "- [ ] If helper is not visible, is searching for one reasonable?",
                    "- [ ] Is the expected helper/tool type reasonable for this task?",
                    "- [ ] Is the model plan physically feasible for the stated embodiment?",
                    "- [ ] Is the failure truly about helper/tool awareness, rather than image ambiguity?",
                    "- [ ] Can this case be safely used as paper evidence?",
                    "",
                ]
            )
    path.write_text("\n".join(lines), encoding="utf-8")


def write_summary(path: Path, rows: list[dict[str, Any]]) -> None:
    missing_images = sum(1 for row in rows if not Path(str(row.get("image_path", ""))).exists())
    lines = [
        "# Visual Review Summary",
        "",
        f"- Selected cases: {len(rows)}",
        f"- Missing image files: {missing_images}",
        "",
        "Reviewer fields in `visual_review_sheet.csv` are blank and must be filled manually.",
        "",
        "## By Case Tier",
        "",
        count_table(Counter(str(row.get("case_tier", "")) for row in rows), "Case tier"),
        "",
        "## By Task",
        "",
        count_table(Counter(str(row.get("task_id", "")) for row in rows), "Task"),
        "",
        "## By Failure Family",
        "",
        count_table(Counter(str(row.get("failure_family", "")) for row in rows), "Failure family"),
        "",
        "## Top Tasks Selected",
        "",
    ]
    for task_id, count in Counter(str(row.get("task_id", "")) for row in rows).most_common(10):
        lines.append(f"- {task_id}: {count}")
    lines.extend(["", "This pack prepares human review only; it does not validate final benchmark claims.", ""])
    path.write_text("\n".join(lines), encoding="utf-8")


def count_table(counter: Counter[str], label: str) -> str:
    lines = [f"| {label} | Count |", "| --- | ---: |"]
    for key, count in counter.most_common():
        lines.append(f"| {key or '-'} | {count} |")
    return "\n".join(lines)


def write_readme(path: Path) -> None:
    path.write_text(
        """# Human Visual Review Pack

This directory contains a structured pack for human image-level verification of selected benchmark cases.

The source rereview is text-only. It cannot verify whether the target objects, helper objects, occlusions, or physical layout are actually visible in the image. Do not treat this pack as final paper evidence until the reviewer fields are manually completed.

## How Cases Were Selected

Cases are selected from `case_rereview.jsonl` and joined with `all_rows_merged.jsonl`.

Priority order:

1. Clean counterexample candidates from primary clean prompts.
2. Robust failures where clean and matching tool-prior prompts both fail.
3. Prompted improvements where clean fails but tool-prior passes.
4. Uncertain or visually ambiguous cases.

Rows with parse errors or skipped images are excluded from this visual review pack.

## How To Fill `visual_review_sheet.csv`

Fill the blank `reviewer_*` columns manually:

- `reviewer_image_target_visible`: whether the target object is visible.
- `reviewer_helper_visible`: whether the expected helper/tool is visible.
- `reviewer_helper_needed_by_task`: whether helper/tool use is actually needed.
- `reviewer_expected_helper_reasonable`: whether the expected helper type is physically reasonable.
- `reviewer_model_plan_physically_feasible`: whether the model plan can plausibly work.
- `reviewer_model_failure_confirmed`: whether the text-rereview failure is confirmed by the image.
- `reviewer_claim_safe_to_use`: whether the case is safe to use as evidence after license/source checks.
- `reviewer_notes`: free-form notes.

`reviewer_claim_safe_to_use=yes` should require clear image evidence, no major ambiguity, and suitable image provenance for the intended use.

## Limitations

- No VLM inference is run here.
- No image content is automatically inspected.
- Text rereview can be wrong when the image contradicts or clarifies the model output.
- Prompted-improvement cases are intervention examples, not clean counterexample evidence.
""",
        encoding="utf-8",
    )


def summarize_selection(rows: list[dict[str, Any]]) -> dict[str, Any]:
    return {
        "selected_cases": len(rows),
        "case_tier": dict(Counter(str(row.get("case_tier", "")) for row in rows)),
        "task_id": dict(Counter(str(row.get("task_id", "")) for row in rows)),
        "failure_family": dict(Counter(str(row.get("failure_family", "")) for row in rows)),
        "missing_image_files": sum(1 for row in rows if not Path(str(row.get("image_path", ""))).exists()),
    }


def image_name(row: dict[str, Any]) -> str:
    return str(row.get("image_name") or Path(str(row.get("image_path", ""))).name)


def truthy(value: Any) -> bool:
    if isinstance(value, bool):
        return value
    return str(value).strip().lower() in {"true", "1", "yes"}


def run_self_test() -> None:
    merged = [
        synthetic_merged("run1", "task_001", "image_01.jpg", "model_a", "natural_free_plan"),
        synthetic_merged("run2", "task_001", "image_01.jpg", "model_a", "tool_prior_free_plan"),
        synthetic_merged("run3", "task_002", "image_02.jpg", "model_a", "natural_free_plan"),
        synthetic_merged("run4", "task_002", "image_02.jpg", "model_a", "tool_prior_free_plan"),
        synthetic_merged("run5", "task_003", "image_03.jpg", "model_a", "natural_free_plan"),
        synthetic_merged("run6", "task_004", "image_04.jpg", "model_a", "natural_free_plan"),
        synthetic_merged("run7", "task_004", "image_04.jpg", "model_b", "natural_free_plan"),
        synthetic_merged("run8", "task_004", "image_04.jpg", "model_c", "natural_free_plan"),
        synthetic_merged("run9", "task_004", "image_04.jpg", "model_d", "natural_free_plan"),
    ]
    rereview = [
        synthetic_review(merged[0], "true_fail", "high", "aggregation_failure"),
        synthetic_review(merged[1], "true_fail", "high", "aggregation_failure"),
        synthetic_review(merged[2], "true_fail", "high", "aggregation_failure"),
        synthetic_review(merged[3], "true_pass", "high", ""),
        synthetic_review(merged[4], "parse_error", "low", "parse_failure"),
        synthetic_review(merged[5], "true_fail", "high", "aggregation_failure"),
        synthetic_review(merged[6], "true_fail", "high", "aggregation_failure"),
        synthetic_review(merged[7], "true_fail", "high", "aggregation_failure"),
        synthetic_review(merged[8], "true_fail", "high", "aggregation_failure"),
    ]
    rows = enrich_rows(rereview, merged)
    selected = select_cases(rows, max_cases=20, include_prompted_improvements=True, include_uncertain=False)
    assert any(row["case_tier"] == "clean_counterexample" for row in selected), "clean fail should be selected"
    assert all(row["rereview_label"] != "parse_error" for row in selected), "parse_error rows must be excluded"
    assert any(row["case_tier"] == "prompted_improvement" for row in selected), "prompted improvement should be selected"
    group_count = sum(1 for row in selected if row["task_id"] == "task_004" and row["image_name"] == "image_04.jpg")
    assert group_count <= 3, "deduplication should cap repeated task/image/family rows"

    with tempfile.TemporaryDirectory() as tmp:
        output_dir = Path(tmp) / "pack"
        write_pack(selected, output_dir, copy_images=False)
        sheet = (output_dir / "visual_review_sheet.csv").read_text(encoding="utf-8")
        assert ",,,,,,,," in sheet or "reviewer_notes" in sheet, "reviewer fields should be present"
        for field in REVIEWER_FIELDS:
            assert field in sheet, f"{field} missing from sheet"
        cases_md = (output_dir / "visual_review_cases.md").read_text(encoding="utf-8")
        assert "VR001" in cases_md and "image_01.jpg" in cases_md, "cases markdown should include IDs and image paths"
    print(json.dumps({"self_test": "passed"}, ensure_ascii=False))


def synthetic_merged(run_id: str, task_id: str, image_name_value: str, model_id: str, prompt_id: str) -> dict[str, Any]:
    prompt_category = "tool_prior_intervention" if "tool_prior" in prompt_id else "generic_clean"
    return {
        "run_id": run_id,
        "task_id": task_id,
        "task_name": f"{task_id}_name",
        "image_name": image_name_value,
        "image_path": f"/tmp/{image_name_value}",
        "model_id": model_id,
        "prompt_id": prompt_id,
        "prompt_category": prompt_category,
        "prompt_type": "tool_prior_intervention" if "tool_prior" in prompt_id else "primary_clean",
        "embodiment_profile": "generic",
        "primary_for_counterexample": "False" if "tool_prior" in prompt_id else "True",
        "task_instruction": "Move the target objects.",
        "expected_should_use_tool_or_container": "True",
        "expected_tool_or_container_types": "tray; bag; box",
        "expected_should_search_for_tool_if_not_visible": "False",
        "expected_should_avoid_over_tool_use": "False",
        "expected_trip_pattern": "single_or_few_trips",
        "target_object_terms": "water; bottles",
    }


def synthetic_review(row: dict[str, Any], label: str, confidence: str, modes: str) -> dict[str, Any]:
    output = dict(row)
    output.update(
        {
            "rereview_label": label,
            "rereview_confidence": confidence,
            "rereview_failure_modes": modes,
            "evidence_quote": "find a tray; place bottles on it; carry it to bedroom" if label == "true_pass" else "carry bottles directly",
            "parsed_plan": "carry bottles directly",
            "raw_response_short": "raw",
            "needs_visual_check": "yes" if modes else "no",
        }
    )
    return output


if __name__ == "__main__":
    main()
