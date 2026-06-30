# Human Visual Review Pack

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
