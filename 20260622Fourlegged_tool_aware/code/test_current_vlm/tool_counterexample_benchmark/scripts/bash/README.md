# Ollama Batch Scripts

These scripts run multi-model Ollama VLM tests for the tool-aware planning benchmark.
They activate `codex_ollama` automatically and generate a temporary models config under `outputs/<prefix>_generated_configs/` so the large Ollama models can remain disabled in `config/models.yaml` by default.

## Current Prompt Sets

There are 9 prompt settings.

Generic clean prompts:

- `natural_free_plan`
- `efficient_safe_free_plan`

Humanoid dual-arm clean prompts:

- `natural_free_plan_humanoid_dual_arm`
- `efficient_safe_free_plan_humanoid_dual_arm`

Quadruped single-arm clean prompts:

- `natural_free_plan_quadruped_single_arm`
- `efficient_safe_free_plan_quadruped_single_arm`

Diagnostic probes:

- `structured_tool_probe`
- `structured_tool_action_chain_probe_humanoid_dual_arm`
- `structured_tool_action_chain_probe_quadruped_single_arm`

Clean prompts are the main evidence route. Diagnostic probes are for debugging action-chain behavior and should be analyzed separately.

## Models Used

Each multi-model script runs these model IDs:

- `ollama_qwen3_vl_32b_instruct_q4_K_M`
- `ollama_qwen3_vl_30b_a3b_instruct_q4_K_M`
- `ollama_qwen3_5_35b`
- `ollama_minicpm_v4_5_q8_0`
- `ollama_gemma3_27b_it_q8_0`
- `ollama_llama3_2_vision_11b_instruct_q8_0`

They correspond to these Ollama model names:

- `qwen3-vl:32b-instruct-q4_K_M`
- `qwen3-vl:30b-a3b-instruct-q4_K_M`
- `qwen3.5:35b`
- `minicpm-v4.5:q8_0`
- `gemma3:27b-it-q8_0`
- `llama3.2-vision:11b-instruct-q8_0`

## Output Naming

By default, output folders use:

```text
outputs/ollama_multi_YYYYMMDD_HHMMSS_<category>_<model_id>/
```

To force the same prefix across multiple script calls:

```bash
RUN_PREFIX=real_images_round01 scripts/bash/run_ollama_generic_clean.sh
RUN_PREFIX=real_images_round01 scripts/bash/run_ollama_quadruped_clean.sh
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

Run all clean prompt categories:

```bash
scripts/bash/run_ollama_all_clean.sh
```

Run diagnostic probes only:

```bash
scripts/bash/run_ollama_diagnostic_probes.sh
```

Run clean prompts for one model:

```bash
scripts/bash/run_ollama_one_model_all_clean.sh ollama_qwen3_vl_32b_instruct_q4_K_M
```

Run all categories, including diagnostic probes:

```bash
scripts/bash/run_ollama_all_prompt_categories.sh
```

## Extra run_batch Arguments

Any extra arguments are passed through to `python -m src.run_batch`.

Subset tasks:

```bash
scripts/bash/run_ollama_generic_clean.sh --task_ids task_001 task_002 task_008
```

Limit quick smoke tests:

```bash
scripts/bash/run_ollama_generic_clean.sh --task_ids task_001 --limit 1
```

If a task folder has no image, the benchmark records skipped rows for that task and continues.


# 中文版

• 已在 scripts/bash/ 下加好批量测试脚本，并验证了 dry run 可以跑通。

  目前共有 9 种 prompt：

  Generic clean：

  - natural_free_plan
  - efficient_safe_free_plan

  Humanoid dual-arm clean：

  - natural_free_plan_humanoid_dual_arm
  - efficient_safe_free_plan_humanoid_dual_arm

  Quadruped single-arm clean：

  - natural_free_plan_quadruped_single_arm
  - efficient_safe_free_plan_quadruped_single_arm

  Diagnostic probes：

  - structured_tool_probe
  - structured_tool_action_chain_probe_humanoid_dual_arm
  - structured_tool_action_chain_probe_quadruped_single_arm

  新增脚本：

  - scripts/bash/run_ollama_generic_clean.sh
  - scripts/bash/run_ollama_humanoid_clean.sh
  - scripts/bash/run_ollama_quadruped_clean.sh
  - scripts/bash/run_ollama_diagnostic_probes.sh
  - scripts/bash/run_ollama_all_clean.sh
  - scripts/bash/run_ollama_all_prompt_categories.sh
  - scripts/bash/run_ollama_one_model_all_clean.sh
  - scripts/bash/_ollama_batch_common.sh
  - scripts/bash/README.md

  默认跑这 6 个模型：

  - qwen3-vl:32b-instruct-q4_K_M
  - qwen3-vl:30b-a3b-instruct-q4_K_M
  - qwen3.5:35b
  - minicpm-v4.5:q8_0
  - gemma3:27b-it-q8_0
  - llama3.2-vision:11b-instruct-q8_0

  常用命令：

  cd 20260622Fourlegged_tool_aware/code/test_current_vlm/tool_counterexample_benchmark

  scripts/bash/run_ollama_generic_clean.sh
  scripts/bash/run_ollama_quadruped_clean.sh
  scripts/bash/run_ollama_humanoid_clean.sh

  跑所有 clean prompt：

  scripts/bash/run_ollama_all_clean.sh

  只跑某些 task：

  scripts/bash/run_ollama_all_clean.sh --task_ids task_001 task_002 task_008

  设置统一输出前缀：

  RUN_PREFIX=real_images_round01 scripts/bash/run_ollama_all_clean.sh --task_ids task_001 task_002

  输出目录格式类似：

  outputs/real_images_round01_generic_clean_ollama_qwen3_vl_32b_instruct_q4_K_M/

  脚本会自动 conda activate codex_ollama，并临时生成一个启用这些大模型的 models config，不会修改主
  config/models.yaml。有图片的 task 会测，没有图片的 task 会按现有逻辑 skipped。

  我已运行：

  bash -n scripts/bash/*.sh
  RUN_PREFIX=script_dryrun_check scripts/bash/run_ollama_generic_clean.sh --dry_run --limit 1

  都通过。