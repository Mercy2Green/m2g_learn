# Offline Result Analysis

These scripts build a row-level index from existing benchmark outputs and run a stricter text-based rereview pass. They do not call Ollama, cloud APIs, or any VLM.

## Why This Exists

`evaluation.csv` is an automatic first-pass heuristic. It is useful for filtering, but it is not ground truth. The analysis scripts use:

- `raw_responses.jsonl`
- `parsed_results.jsonl`
- `evaluation.csv`
- `config_snapshot/`

`summary.md` and `failed_cases.md` are only navigation aids.

## build_result_index.py

`build_result_index.py` merges each output directory into one unified row-level table.

It joins rows using:

```text
task_id, image_path, model_id, prompt_id
```

It enriches rows with task expected behavior, prompt metadata, model metadata, raw response metadata, compact text fields, and full parsed/raw objects in JSONL.

Default small-subset run:

```bash
python scripts/analysis/build_result_index.py \
  --output_dir analysis_review/round01_small_subset
```

Generated files:

- `all_runs_manifest.csv`
- `all_rows_merged.csv`
- `all_rows_merged.jsonl`
- `data_integrity_report.md`

## rereview_results.py

`rereview_results.py` rereviews every merged row, including automatic pass/fail/review, parse errors, and skipped rows.

It is text-based only. It does not inspect images, so image-dependent cases are marked with `needs_visual_check=yes` or `uncertain` when needed.

Self-test:

```bash
python scripts/analysis/rereview_results.py --self_test
```

Run rereview:

```bash
python scripts/analysis/rereview_results.py \
  --input analysis_review/round01_small_subset/all_rows_merged.jsonl \
  --output_dir analysis_review/round01_small_subset
```

Generated files:

- `case_rereview.csv`
- `case_rereview.jsonl`
- `rereview_disagreements.md`
- `high_confidence_cases.md`
- `uncertain_cases_for_human.md`

## How To Expand Later

Scan all completed runs under an outputs root:

```bash
python scripts/analysis/build_result_index.py \
  --outputs_root outputs/20260630_important_all_test \
  --output_dir analysis_review/round02_full_important_outputs
```

Pass explicit output directories:

```bash
python scripts/analysis/build_result_index.py \
  --output_dirs outputs/run_a outputs/run_b outputs/run_c \
  --output_dir analysis_review/round02_selected_runs
```

For full-output aggregation, first decide which output directories are valid and whether old runs used compatible prompt schemas. Do not mix exploratory/debug runs into paper-facing summaries without marking them.

## summarize_rereview.py

After rereview, generate aggregate analysis documents:

```bash
python scripts/analysis/summarize_rereview.py \
  --input analysis_review/round02_full_important_outputs/case_rereview.jsonl \
  --output_dir analysis_review/round02_full_important_outputs
```

Generated files:

- `aggregate_findings.md`
- `task_family_summary.csv`
- `model_prompt_matrix.csv`
- `prompt_intervention_delta.md`
- `counterexample_candidates_ranked.md`
- `README_FOR_CHATGPT.md`

## Limitations

- Text rereview cannot verify image contents.
- It cannot prove a helper was actually visible.
- It can miss implicit helper use.
- It should not be used for final paper claims without manual image-level review.
- Tool-prior intervention rows are prompted upper-bound checks, not clean counterexample evidence.
