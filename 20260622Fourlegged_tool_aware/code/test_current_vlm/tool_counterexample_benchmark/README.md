# Tool-Aware Planning Counterexample Benchmark

## Purpose

This framework batch-tests whether current strong VLM / VLA / multimodal APIs can spontaneously produce tool-aware high-level plans in natural mobile manipulation scenes.

The goal is to find clean counterexamples: for example, a model sees several bottles that should be moved quickly but plans to carry them one by one instead of naturally using a tray, bag, box, basket, broom, rod, or other helper object. This is not a training system and not a robot control stack.

## Current task focus

- Test natural household, office, kitchen, bedroom, and lab-like mobile manipulation scenes.
- Use robot first-person or near robot first-person images.
- Do not test cross-embodiment differences such as robot height, arm length, or gripper type.
- Do not run low-level control, WBC, VLA action execution, training, or fine-tuning.
- Do not explicitly prompt the model to use tools.
- Focus on aggregation, containers, short-range search, efficiency, physical stability, and high-level decomposition.

## Prompt settings

Primary clean prompts:

- `natural_free_plan`
- `efficient_safe_free_plan`

These prompts do not include `tool`, `container`, `uses_tool_or_container`, or similar output fields. They are the only prompt settings used for clean counterexample strength.

Diagnostic prompt:

- `structured_tool_probe`

`structured_tool_probe` is useful for debugging because its schema asks for tool/container fields, but it is not clean main counterexample evidence.

## Install

```bash
cd 20260622Fourlegged_tool_aware/code/test_current_vlm/tool_counterexample_benchmark
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

For a dry run, the repo includes a limited YAML fallback. Real API runs should install `requirements.txt`.

## How to add images

Each task has one folder under `images/`:

```text
images/task_001_multi_bottles_visible_container/
```

Each task folder can contain multiple images:

```text
image_01.jpg
image_02.jpg
image_03.jpg
```

Images should be real or realistic robot-view scenes. Do not write the answer on the image. Do not stage a puzzle-like scene. For tasks where no helper object is currently visible, keep trays, bags, boxes, and similar helpers out of the image.

`scene_note` in `config/tasks.yaml` is for human bookkeeping and optional diagnostic prompts. It is not used by the primary clean prompts.

## Configure Alibaba Cloud Bailian

The recommended main provider is Alibaba Cloud Bailian / DashScope OpenAI-compatible API through `openai_compatible`.

Copy `.env.example` to `.env`:

```bash
cp .env.example .env
```

Fill:

```bash
BAILIAN_API_KEY=
BAILIAN_BASE_URL=https://{WorkspaceId}.cn-beijing.maas.aliyuncs.com/compatible-mode/v1
```

Use the WorkspaceId, region, and model names shown in the Bailian console. Model names in `config/models.yaml` are examples and may need to be changed to models enabled in your workspace.

Optional legacy DashScope-compatible variables:

```bash
DASHSCOPE_API_KEY=
DASHSCOPE_BASE_URL=https://dashscope.aliyuncs.com/compatible-mode/v1
```

Do not commit real API keys.

## Config check without API call

This checks enabled model configuration and image folders. It does not call any model API.

```bash
python scripts/smoke_bailian_config_check.py
```

Warnings about empty image folders are expected before you add images.

## How to run

Dry run without API keys or images:

```bash
python -m src.run_batch --dry_run --limit 2 --overwrite
```

Single real smoke test after adding at least one image and filling `.env`:

```bash
python -m src.run_batch \
  --models config/models.yaml \
  --prompts config/prompt_sets.yaml \
  --tasks config/tasks.yaml \
  --output_dir outputs/bailian_smoke \
  --task_ids task_001 \
  --model_ids bailian_qwen_vl_plus \
  --prompt_ids natural_free_plan \
  --limit 1 \
  --overwrite
```

Full batch example:

```bash
python -m src.run_batch \
  --tasks config/tasks.yaml \
  --models config/models.yaml \
  --prompts config/prompt_sets.yaml \
  --output_dir outputs/run_full \
  --overwrite
```

## Outputs

Each run creates:

```text
outputs/<run_name>/
  raw_responses.jsonl
  parsed_results.jsonl
  evaluation.csv
  summary.md
  failed_cases.md
  config_snapshot/
    tasks.yaml
    models.yaml
    prompt_sets.yaml
```

Raw responses are always saved, including provider errors and parse failures. API keys are not saved.

## How to judge counterexamples

The evaluator is an automatic first pass, not a substitute for manual review. For primary clean prompts, it infers helper use from the free-form plan text with bilingual keyword heuristics.

Strong:
`qwen_main` failed and at least one other non-mock model failed on the same task/image/primary prompt.

Medium:
`qwen_main` failed, but another stronger or non-Qwen non-mock model passed.

Weak:
Only one non-mock model failed.

Invalid or unclear:
Parse error, skipped, needs review, mock-only evidence, non-primary prompt, unclear image, artificial scene, or prompt leakage.

## Failure taxonomy

F1_aggregation_failure:
Multi-object transport does not use a tray, bag, box, basket, or similar aggregation aid.

F2_tool_search_failure:
When no helper is visible, the model does not propose a short-range search for one.

F3_efficiency_blind_planning:
The model only plans for task completion and ignores trips, time, or route cost.

F4_container_affordance_miss:
A visible container or carrying aid is not used for transport.

F5_wrong_tool_or_container_choice:
The selected helper is too small, unstable, inappropriate, or mismatched.

F6_tool_necessity_miss:
The task needs a helper to be efficient or feasible, but the model still directly operates.

F7_over_tool_use:
A helper is available but unnecessary, and the model uses it anyway.

F8_physical_stability_miss:
The model ignores stacking, liquids, fragile objects, tipping, or stability.

F9_long_horizon_decomposition_miss:
The plan lacks a sequence such as first get helper, load or operate, then transport or finish.

F10_search_or_fallback_miss:
When a helper is unavailable or unsuitable, the model gives no fallback.

## What not to do

- Do not write "please use tools" in primary prompts.
- Do not write the answer into the prompt.
- Do not use pure text puzzles.
- Do not add cross-embodiment tasks as the current main line.
- Do not run training or fine-tuning here.
- Do not treat `structured_tool_probe` as clean counterexample evidence.
- Do not treat one model failure as a paper-level conclusion.
- Confirm candidates across multiple images, models, and primary prompt settings.

## Current limitations

- Bailian model names and vision input support must be confirmed in the Bailian console.
- `image_transport: data_url` is implemented; some OpenAI-compatible providers may require a different image transport.
- The heuristic evaluator can miss implicit helper use or over-detect keyword mentions. Review `failed_cases.md` and raw outputs manually.
