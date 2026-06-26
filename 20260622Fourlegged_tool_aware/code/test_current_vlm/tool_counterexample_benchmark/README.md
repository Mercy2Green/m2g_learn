# Tool-Aware Planning Counterexample Benchmark

## Purpose

This framework batch-tests whether current strong VLM / VLA / multimodal APIs can spontaneously produce tool-aware high-level plans in natural mobile manipulation scenes.

The target failure mode is not low-level robot control. The target is planning failure: for example, a model sees several bottles that should be moved quickly but plans to carry them one by one instead of using a tray, bag, box, basket, broom, rod, or other helper object.

## Current task focus

- Test natural household, office, kitchen, bedroom, and lab-like mobile manipulation scenes.
- Use robot first-person or near robot first-person images.
- Do not test cross-embodiment differences such as robot height, arm length, or gripper type.
- Do not run low-level control, WBC, VLA action execution, training, or fine-tuning.
- Do not explicitly prompt the model to use tools.
- Focus on aggregation, containers, short-range search, efficiency, physical stability, and high-level decomposition.

## Install

```bash
cd tool_counterexample_benchmark
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

For a dry run, only `PyYAML` is required. Real API runs need the provider SDKs listed in `requirements.txt`.

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

Each task folder has a `README.md` with the scene, expected human-level plan, and failure types.

## Configure APIs

Copy `.env.example` to `.env` and fill only the providers you want to run:

```bash
cp .env.example .env
```

Default environment variables:

```bash
QWEN_API_KEY=
QWEN_BASE_URL=https://dashscope.aliyuncs.com/compatible-mode/v1
QWEN_MODEL=qwen-vl-plus

OPENAI_API_KEY=
OPENAI_MODEL=gpt-4o

GEMINI_API_KEY=
GEMINI_MODEL=gemini-2.5-pro
```

Enable or disable models in `config/models.yaml`. Do not commit real API keys.

## How to run

Dry run without API keys or images:

```bash
python -m src.run_batch --dry_run --limit 2 --overwrite
```

Full run:

```bash
python -m src.run_batch \
  --tasks config/tasks.yaml \
  --models config/models.yaml \
  --prompts config/prompt_sets.yaml \
  --output_dir outputs/run_001 \
  --overwrite
```

Filter tasks, models, or prompts:

```bash
python -m src.run_batch \
  --task_ids task_001 task_002 \
  --model_ids qwen_default openai_default \
  --prompt_ids natural efficient_safe \
  --output_dir outputs/run_subset
```

## Outputs

Each run creates:

```text
outputs/run_001/
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

Raw responses are always saved, including provider errors and parse failures.

## How to judge counterexamples

The evaluator is an automatic first pass, not a substitute for manual review.

Strong:
Qwen plus at least one closed strong model both fail on the same task/image/prompt.

Medium:
Qwen consistently fails, but a closed strong model succeeds.

Weak:
Only a smaller or single model fails.

Invalid:
The image is unclear, the scene is too artificial, the prompt leaks the answer, or a small wording change completely solves it.

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

- Do not write "please use tools" in prompts.
- Do not write the answer into the prompt.
- Do not use pure text puzzles.
- Do not add cross-embodiment tasks as the current main line.
- Do not treat one model failure as a paper-level conclusion.
- Confirm candidates across multiple images, models, and prompt settings.

## Notes on prompt leakage

The benchmark checks task/user prompt text against `invalid_prompt_leakage_terms`. It does not count the required JSON field names as leakage, because fields such as `uses_tool_or_container` are needed for batch evaluation.
