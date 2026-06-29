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
- `natural_free_plan_humanoid_dual_arm`
- `efficient_safe_free_plan_humanoid_dual_arm`
- `natural_free_plan_quadruped_single_arm`
- `efficient_safe_free_plan_quadruped_single_arm`

The generic prompts remain generic baselines. The humanoid/quadruped prompts add only robot capability constraints such as hand count, gripper capacity, balance, and reach limits. They do not name task-specific helper answers. These primary prompts do not include `tool`, `container`, `uses_tool_or_container`, or similar output fields.

Diagnostic prompts:

- `structured_tool_probe`
- `structured_tool_action_chain_probe_humanoid_dual_arm`
- `structured_tool_action_chain_probe_quadruped_single_arm`

Diagnostic probes ask for helper/action-chain fields and are useful for debugging, but they are not clean main counterexample evidence.

## Install

```bash
cd 20260622Fourlegged_tool_aware/code/test_current_vlm/tool_counterexample_benchmark
conda activate codex_ollama
pip install -r requirements.txt
```

For a dry run, the repo includes a limited YAML fallback. Real API runs should install `requirements.txt`.

The shared local environment for Ollama-linked runs is:

```bash
conda activate codex_ollama
```

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

## Collect temporary web images for smoke tests

This script collects temporary web images for internal smoke tests only. These images are not a final dataset and should not be used in a paper or released publicly unless their licenses are manually verified.

The default route searches Wikimedia Commons first, then Openverse as a fallback. It downloads traceable image files, resizes them to a modest size, and writes metadata for manual review. Downloaded images and generated metadata are gitignored by default.

Run:

```bash
python scripts/collect_web_images.py --max_per_task 3
```

For a subset:

```bash
python scripts/collect_web_images.py --task_ids task_001 task_002 --max_per_task 3
```

Dry run:

```bash
python scripts/collect_web_images.py --dry_run
```

After collection, manually inspect:

```text
image_metadata/manual_review_checklist.md
```

Do not treat downloaded images as clean benchmark data without manual review. Final counterexamples should preferably use your own robot-view photos or explicitly licensed images that have been checked one by one.

If web search is blocked or returns poor matches, add traceable direct image URLs to `config/manual_image_urls.yaml` and rerun the script. Manual URLs still get metadata entries and resize processing.

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

## Local Ollama pre-screening

Ollama is used as a cheap local pre-screening route. It is not a replacement for stronger paid/cloud verification models.

Recommended workflow:

1. Use Ollama local VLMs to scan many candidate images/tasks.
2. Keep only stable failure cases.
3. Verify the strongest 5-10 cases with Bailian or another stronger cloud VLM.

Recommended local models:

- `qwen3-vl:8b`: main local Qwen VLM pre-screening baseline.
- `qwen3-vl:4b`: small weak baseline.
- `gemma3:12b`: cross-model-family local sanity check.
- `qwen3-vl:32b-instruct-q4_K_M` and `qwen3-vl:30b-a3b-instruct-q4_K_M`: optional stronger Qwen local checks if GPU memory allows.
- `gemma3:27b-it-q8_0` and `llama3.2-vision:11b-instruct-q8_0`: optional cross-family local checks.
- `minicpm-v4.5:q8_0`: optional local open VLM candidate; verify image support first.
- `qwen3.5:35b`: disabled by default and should not be treated as VLM evidence unless an image smoke test confirms vision support.

Start Ollama:

```bash
ollama serve
```

Pull candidate models:

```bash
ollama pull qwen3-vl:8b
ollama pull qwen3-vl:4b
ollama pull gemma3:12b
```

Check local Ollama config without inference:

```bash
python scripts/smoke_ollama_config_check.py
```

Run a local smoke test after adding at least one image:

```bash
python -m src.run_batch \
  --models config/models.yaml \
  --prompts config/prompt_sets.yaml \
  --tasks config/tasks.yaml \
  --output_dir outputs/ollama_smoke \
  --task_ids task_001 \
  --model_ids ollama_qwen3_vl_8b ollama_qwen3_vl_4b \
  --prompt_ids natural_free_plan \
  --limit 1 \
  --overwrite
```

Important:

- Ollama failure alone is not final paper evidence.
- Stronger cloud verification is still needed.
- Use `--model_ids` to avoid unintentionally running both local and cloud models.
- Ollama uses native `/api/chat` with `images: [base64]`, while Bailian/OpenAI-compatible providers use `image_url` data URLs. These are intentionally separate providers.

Run generic clean prompts on selected strong local models:

```bash
python -m src.run_batch \
  --models config/models.yaml \
  --prompts config/prompt_sets.yaml \
  --tasks config/tasks.yaml \
  --output_dir outputs/ollama_generic_clean_strong \
  --model_ids ollama_qwen3_vl_32b_instruct_q4_K_M ollama_qwen3_vl_30b_a3b_instruct_q4_K_M ollama_gemma3_27b_it_q8_0 ollama_llama3_2_vision_11b_instruct_q8_0 \
  --prompt_ids natural_free_plan efficient_safe_free_plan \
  --overwrite
```

Run quadruped single-arm constrained prompts:

```bash
python -m src.run_batch \
  --models config/models.yaml \
  --prompts config/prompt_sets.yaml \
  --tasks config/tasks.yaml \
  --output_dir outputs/ollama_quadruped_single_arm \
  --model_ids ollama_qwen3_vl_32b_instruct_q4_K_M ollama_llama3_2_vision_11b_instruct_q8_0 \
  --prompt_ids natural_free_plan_quadruped_single_arm efficient_safe_free_plan_quadruped_single_arm structured_tool_action_chain_probe_quadruped_single_arm \
  --overwrite
```

Run humanoid dual-arm constrained prompts:

```bash
python -m src.run_batch \
  --models config/models.yaml \
  --prompts config/prompt_sets.yaml \
  --tasks config/tasks.yaml \
  --output_dir outputs/ollama_humanoid_dual_arm \
  --model_ids ollama_qwen3_vl_32b_instruct_q4_K_M ollama_llama3_2_vision_11b_instruct_q8_0 \
  --prompt_ids natural_free_plan_humanoid_dual_arm efficient_safe_free_plan_humanoid_dual_arm structured_tool_action_chain_probe_humanoid_dual_arm \
  --overwrite
```

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
- Ollama must be installed and running separately; the Python environment only contains benchmark dependencies.
- Some Ollama models may not support image input even if text inference works. Confirm with a small local smoke test.
- 27B/30B local models may exceed available GPU memory.
- `supports_vision: false/unknown` models should not be used as VLM evidence until image input is confirmed.
- The heuristic evaluator can miss implicit helper use or over-detect keyword mentions. Review `failed_cases.md` and raw outputs manually.
