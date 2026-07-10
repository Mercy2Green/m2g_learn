# AHD-Benchmark

AHD = Active Helper Discovery. This benchmark tests sequential partial observation for helper-target grounding:

- O0 image: target visible, helper absent.
- O1 image: helper visible, target absent or non-salient.
- The model must use O0 target memory to decide whether the O1 object is a task-relevant helper.

## v0.1 Scope

Stage 0 creates a deterministic candidate pool only. It does not generate images, call Cosmos3, run VLM filtering, train models, or evaluate models.

This stage generates:

- 2,000 image-level scene spec candidates.
- Schema, count, duplicate-id, and simple leakage checks.
- Cosmos3 T2I prompt entries for later image generation.
- Distribution preview docs.

The 2,000 specs are candidates. Later stages should select about 600-800 image specs for Cosmos3 generation, then filter into paired samples.

Running scripts `01` through `04` creates local generated artifacts under `specs/`, `prompts/`, and `docs/DATA_DISTRIBUTION_PREVIEW.md`. These outputs are gitignored and should not be committed in the Stage 0 repository state. Keep source code, configs, docs, and `.gitkeep` placeholders in version control.

## Task Families

- `aggregate_transport`: multiple bottles or drinks are visible; a container-like helper is absent in O0.
- `extend_reach`: a small object is under furniture; a long rigid helper is absent in O0.
- `direct_is_enough`: a single reachable bottle should be handled directly without helper search.

## Stage 0.5 Optional Ollama Enrichment

Stage 0.5 can run local Ollama text enrichment after scripts `01` through `03` have created checked specs locally. The deterministic Stage 0 specs remain the source of truth; the local model may rewrite visual/task wording, but it must not modify gold labels or decide helper correctness.

Recommended first local model:

```text
qwen3-vl:32b-instruct-q4_K_M
```

Generated enrichment previews and reports are written under `specs/enrichment/` and are gitignored.

## Commands

```bash
cd 20260622Fourlegged_tool_aware/code/AHD-benchmark
conda activate codex_ollama
pip install -r requirements.txt
python scripts/00_smoke_config_check.py
python scripts/01_generate_scene_specs.py
python scripts/02_check_scene_specs.py
python scripts/03_expand_cosmos_prompts.py
python scripts/04_preview_distribution.py
# Optional local text enrichment only, after checked specs exist:
python scripts/05_ollama_enrich_scene_specs.py --model qwen3-vl:32b-instruct-q4_K_M --max_specs 50
python scripts/06_check_llm_enrichment.py specs/enrichment/llm_enriched_qwen3-vl_32b-instruct-q4_K_M_preview.jsonl

python scripts/05_ollama_enrich_scene_specs.py \
  --model qwen3-vl:30b-a3b-instruct-q4_K_M \
  --stratified_per_type 10
python scripts/06_check_llm_enrichment.py \
  specs/enrichment/llm_enriched_qwen3-vl_30b-a3b-instruct-q4_K_M_stratified10_preview.jsonl
```

## Outputs

```text
specs/scene_specs_raw.jsonl
specs/o0_scene_specs_raw.jsonl
specs/o1_scene_specs_raw.jsonl
specs/scene_specs_checked.jsonl
specs/o0_scene_specs_checked.jsonl
specs/o1_scene_specs_checked.jsonl
specs/scene_specs_check_report.md
prompts/cosmos3_prompts_raw.jsonl
docs/DATA_DISTRIBUTION_PREVIEW.md
specs/enrichment/llm_enriched_<model_id>_preview.jsonl
specs/enrichment/llm_enriched_<model_id>_preview_report.md
```

Stage 0 scripts do not make model API calls.
The optional Stage 0.5 enrichment script calls only a local Ollama endpoint when explicitly run.

## Stage 1: Cosmos3 Smoke Generation Bridge

Stage 1 builds small deterministic manifests that connect AHD prompt artifacts to the local Cosmos3-Nano setup under `../cosmos3`. It is intentionally lightweight: build manifests, dry-run commands, then manually launch small batches after inspection.

Generated images now follow a three-layer lifecycle:

- `data/generated_runs/<run_name>/`: raw run outputs, including all generated successes before semantic filtering.
- `data/curated_pools/<pool_name>/`: materialized image pool containing only `semantic_keep` images from a judge run.
- `data/paired_datasets/`: reserved for later paired exports; pair construction is not part of image judging.

`data/images/` is no longer the canonical raw generation directory. Historical results may still point there, but new generation runs should write under `data/generated_runs/`, and curated candidates should be read from `data/curated_pools/`.

Manifest rows keep `output_image_path` for backward compatibility with older prompt artifacts. For new runs this path is a placeholder marked by `output_image_path_is_placeholder: true`; `scripts/08_run_cosmos3_batch.py` overrides it at runtime and writes the actual raw image to `data/generated_runs/<run_name>/images/<o0_or_o1>/<spec_id>.jpg`.

Build a `smoke12` manifest with the recommended enrichment source:

```bash
python scripts/07_build_cosmos3_manifest.py \
  --plan smoke12 \
  --use_enrichment true \
  --enrichment_file specs/enrichment/<your_file>.jsonl
```

Manifest building prints enrichment coverage and writes a sidecar report next to the manifest. Review deterministic fallback rows before generation.

Dry-run the Cosmos3 commands without generating images:

```bash
python scripts/08_run_cosmos3_batch.py \
  --manifest prompts/manifests/cosmos3_smoke12_manifest.jsonl \
  --dry_run
```

First actual test must be one image:

```bash
python scripts/08_run_cosmos3_batch.py \
  --manifest prompts/manifests/cosmos3_smoke12_manifest.jsonl \
  --limit 1 \
  --run_name ahd_cosmos3_one_image_test \
  --yes
```

Summarize the one-image test:

```bash
python scripts/09_summarize_cosmos3_outputs.py \
  --results data/generated_runs/ahd_cosmos3_one_image_test/results.jsonl
```

AHD `target_output_size` is the desired final image size. Cosmos3 `cosmos_input.resolution` is an internal preset/bucket, not the final pixel width or height. The current verified mapping is:

```text
target_output_size: 960x960
cosmos_input.resolution: "720"
cosmos_input.aspect_ratio: "1,1"
observed output: 960x960
```

Only after one-image success and manual inspection should you run the full `smoke12` manifest. See `docs/COSMOS3_INTEGRATION.md` for details.

Smoke generation success is only an engineering check. Before scaling past `smoke12`, run a manual semantic audit:

```bash
python scripts/10_create_visual_audit_sheet.py \
  --results data/generated_runs/ahd_cosmos3_smoke12/results.jsonl
```

For `aggregate_transport` O0 images, exact object count mismatch is a warning, not an automatic failure. The formal visual filter should require a reasonable group of target drinks with count `>= 3`, target visibility, and container/helper absence.

## Stage 1.5: Local VLM Image Judge

Use the local Ollama VLM judge as a triage tool before scaling generated images. It checks image quality and AHD O0/O1 semantics; it is not ground truth and must not modify labels.

The judge separates `generation_failed` and `missing_or_invalid_image` from true `semantic_reject` rows. Missing files and CUDA/OOM generation failures are engineering issues, not prompt-quality failures. Prompt fixes and semantic keep rate should be read from valid images that were actually judged. The image judge is image-level triage only: it does not delete an O0/O1 pair together, does not infer pair validity, and does not remove raw images. Pair filtering happens later during paired dataset export, where one O1 image may be reused across multiple O0 memories.

```bash
python scripts/11_vlm_judge_generated_images.py \
  --results data/generated_runs/ahd_cosmos3_smoke12/results.jsonl \
  --manifest prompts/manifests/cosmos3_smoke12_manifest.jsonl \
  --output_dir data/judges/ahd_cosmos3_smoke12_qwen32 \
  --judge_model qwen3-vl:32b-instruct-q4_K_M \
  --overwrite \
  --progress_every 1

python scripts/12_summarize_vlm_image_judge.py \
  --input_dir data/judges/ahd_cosmos3_smoke12_qwen32

python scripts/13_materialize_curated_pool.py \
  --results data/generated_runs/ahd_cosmos3_smoke12/results.jsonl \
  --judge_dir data/judges/ahd_cosmos3_smoke12_qwen32 \
  --pool_name ahd_cosmos3_smoke12_qwen32 \
  --overwrite
```

Do not scale to `mini36` or larger until VLM judge plus human audit show that generated images satisfy AHD O0/O1 semantics.

## Sequential O0/O1 Baseline Evaluation

The isolated sequential baseline lives under `../test_current_vlm/tool_counterexample_benchmark/sequential_o0_o1/`.
It evaluates curated O0/O1 pairs without changing the old single-image tasks, prompts, or runner. This is evaluation only;
it does not train or fine-tune a model.

Run the controlled 8-row core set with 12 clean sequential prompts and four local models, including `qwen3.5:35b`:

```bash
scripts/bash/prepare_sequential_eval.sh
scripts/bash/run_sequential_core_eval.sh
```

`prepare_sequential_eval.sh` is lightweight: it regenerates and validates the prompt/data artifacts, compiles the
extension, and performs the complete 384-row dry-run without model inference. Run it before starting the long job.

The core script regenerates the 18-to-36 prompt mapping and core dataset, then runs `qwen3-vl:8b`, Qwen3-VL 32B,
Qwen3-VL 30B-A3B, and Qwen3.5 35B. By default it also runs the response-level Qwen3-VL 32B judge on rows
that reached `response_status=ok_eval`. Disable the secondary judge with `RUN_JUDGE=0`. The script defaults to
four concurrent model streams when Ollama has enough GPU capacity; set `PARALLEL_MODELS=1` for serial execution.

Run all 36 sequential prompts on the five critical prompt-sensitivity cases:

```bash
scripts/bash/run_sequential_prompt_sensitivity.sh
```

The sensitivity script defaults to Qwen3-VL 32B, Qwen3-VL 30B-A3B, and Qwen3.5 35B because this run is
substantially larger. Include Qwen3-VL 8B with `INCLUDE_QWEN8=1`. Override output locations with `OUTPUT_DIR=...`.
Generated results remain under the old benchmark's `outputs/` directory and do not overwrite single-image runs.

Rerun only the secondary response judge after a completed core run:

```bash
scripts/bash/run_sequential_response_judge.sh
```

Use `INPUT_DIR=...`, `OUTPUT_DIR=...`, or `JUDGE_MODEL=...` to select another completed run or judge. Extra command-line
arguments such as `--limit 5 --progress_every 1` are passed to the judge script.
