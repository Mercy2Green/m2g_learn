# Ollama Batch Scripts

These scripts run multi-model Ollama VLM tests for the tool-aware planning benchmark.
They activate `codex_ollama` automatically and generate a temporary models config under `outputs/<prefix>_generated_configs/` so large Ollama models can remain disabled in `config/models.yaml` by default.

## Prompt Categories

There are 18 prompt settings.

Generic clean prompts:

- `natural_free_plan`
- `efficient_safe_free_plan`

Humanoid dual-arm clean prompts:

- `natural_free_plan_humanoid_dual_arm`
- `efficient_safe_free_plan_humanoid_dual_arm`

Quadruped single-arm clean prompts:

- `natural_free_plan_quadruped_single_arm`
- `efficient_safe_free_plan_quadruped_single_arm`

Tool-prior intervention prompts:

- `tool_prior_free_plan`
- `tool_prior_free_plan_humanoid_dual_arm`
- `tool_prior_free_plan_quadruped_single_arm`

Strong decomposition intervention prompts:

- `strong_decomposition_free_plan`
- `strong_decomposition_free_plan_humanoid_dual_arm`
- `strong_decomposition_free_plan_quadruped_single_arm`

Search-explicit strong decomposition intervention prompts:

- `search_explicit_strong_decomposition_free_plan`
- `search_explicit_strong_decomposition_free_plan_humanoid_dual_arm`
- `search_explicit_strong_decomposition_free_plan_quadruped_single_arm`

Diagnostic probes:

- `structured_tool_probe`
- `structured_tool_action_chain_probe_humanoid_dual_arm`
- `structured_tool_action_chain_probe_quadruped_single_arm`

Clean prompts are the main evidence route. Tool-prior prompts are prompted helper-prior checks. Strong decomposition prompts are stronger relation-decomposition intervention baselines that keep the free-form schema. Search-explicit strong decomposition prompts additionally state that the current image is only the current view and allow short-range helper search. Diagnostic probes are for debugging action-chain behavior.

## Models Used

Each multi-model script runs these model IDs:

- `ollama_qwen3_vl_32b_instruct_q4_K_M`
- `ollama_qwen3_vl_30b_a3b_instruct_q4_K_M`
- `ollama_qwen3_5_35b`
- `ollama_minicpm_v4_5_q8_0`
- `ollama_gemma3_27b_it_q8_0`
- `ollama_llama3_2_vision_11b_instruct_q8_0`

## Output Naming

By default, output folders use:

```text
outputs/ollama_multi_YYYYMMDD_HHMMSS_<category>_<model_id>/
```

To force the same prefix across multiple script calls:

```bash
RUN_PREFIX=real_images_round01 scripts/bash/run_ollama_generic_clean.sh
RUN_PREFIX=real_images_round01 scripts/bash/run_ollama_tool_prior_intervention.sh
```

## Scripts

Run generic clean prompts:

```bash
scripts/bash/run_ollama_generic_clean.sh
```

Run humanoid dual-arm clean prompts:

```bash
scripts/bash/run_ollama_humanoid_clean.sh
```

Run quadruped single-arm clean prompts:

```bash
scripts/bash/run_ollama_quadruped_clean.sh
```

Run tool-prior intervention prompts:

```bash
scripts/bash/run_ollama_tool_prior_intervention.sh
```

Run strong decomposition intervention prompts:

```bash
scripts/bash/run_ollama_strong_decomposition_intervention.sh
```

Run diagnostic probes:

```bash
scripts/bash/run_ollama_diagnostic_probes.sh
```

Run all clean prompt categories:

```bash
scripts/bash/run_ollama_all_clean.sh
```

Run all prompt categories, including tool-prior and diagnostic probes:

```bash
scripts/bash/run_ollama_all_prompt_categories.sh
```

Run all prompt categories for one model:

```bash
scripts/bash/run_ollama_one_model_all.sh ollama_qwen3_vl_32b_instruct_q4_K_M
```

Run clean prompts for one model:

```bash
scripts/bash/run_ollama_one_model_all_clean.sh ollama_qwen3_vl_32b_instruct_q4_K_M
```

Run image-aware local VLM judge analysis and summary generation for saved benchmark outputs:

```bash
scripts/bash/run_vlm_judge_analysis.sh
```

Run Qwen-only repeated sampling with the same analysis and VLM judge pipeline:

```bash
scripts/bash/run_qwen_repeated_10_with_analysis.sh
```

This defaults to 10 repeats across `ollama_qwen3_vl_4b`, `ollama_qwen3_vl_8b`,
`ollama_qwen3_vl_30b_a3b_instruct_q4_K_M`,
`ollama_qwen3_vl_32b_instruct_q4_K_M`, and `ollama_qwen3_5_35b`. It loops by
repeat first, then model, so the same model is not run 10 times consecutively.
Override `REPEATS`, `RUN_TAG`, `OUTPUT_ROOT`, `ANALYSIS_DIR`, or
`VLM_JUDGE_DIR` as needed.

Run only `qwen3.5:35b` for 10 repeats across all tasks and all prompt settings:

```bash
scripts/bash/run_qwen35_repeated_10_with_analysis.sh
```

This uses `ollama_qwen3_5_35b` only. To reduce cross-run residency effects, it
overrides the temporary model config to `keep_alive=0`, runs each repeat in a
separate `run_batch` process, and defaults to `ollama stop qwen3.5:35b` before
and after each repeat. Set `OLLAMA_STOP_BETWEEN_REPEATS=0` to skip the explicit stop, or
override `OLLAMA_KEEP_ALIVE` if you want a different Ollama residency policy.

By default this analyzes the current round04 strong-tools merged rows:

```text
analysis_review/round04_strong_tools_v2/all_rows_merged.jsonl
```

and writes:

```text
analysis_review/round04_strong_tools_vlm_judge_qwen32_full/
```

Use different paths for another round:

```bash
scripts/bash/run_vlm_judge_analysis.sh \
  --input analysis_review/another_round/all_rows_merged.jsonl \
  --output_dir analysis_review/another_round_vlm_judge \
  --rule_case_rereview analysis_review/another_round/case_rereview.csv
```

Quick judge smoke test:

```bash
scripts/bash/run_vlm_judge_analysis.sh --limit 5 --progress_every 1
```

## Extra run_batch Arguments

Any extra arguments are passed through to `python -m src.run_batch`.

Subset tasks:

```bash
scripts/bash/run_ollama_tool_prior_intervention.sh --task_ids task_002 task_008 task_011
```

Quick smoke test:

```bash
scripts/bash/run_ollama_tool_prior_intervention.sh --task_ids task_002 --limit 1
```

If a task folder has no image, the benchmark records skipped rows for that task and continues.
