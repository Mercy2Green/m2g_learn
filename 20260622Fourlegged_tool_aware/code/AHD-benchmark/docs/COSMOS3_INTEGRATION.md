# Cosmos3 Integration

This bridge connects AHD-Benchmark prompt artifacts to local Cosmos3-Nano image generation.
It does not train models, run VLM filtering, or launch large generation jobs by default.

## Purpose

The AHD pipeline already creates checked scene specs, deterministic Cosmos3 prompts, and optional local Ollama enrichment. The Cosmos3 bridge adds:

- deterministic manifest selection for small generation plans
- a dry-run command planner
- one-image-at-a-time Cosmos3 execution for manual batches
- simple result summaries

## Plans

- `smoke12`: 12 images total, 2 per key spec type.
- `mini36`: 36 images total, 6 per spec type.

The recommended enrichment source for early runs is:

```text
qwen3-vl:30b-a3b-instruct-q4_K_M
```

## Storage Lifecycle

Cosmos3 generation, image judging, and final paired export use separate directories:

```text
data/generated_runs/<run_name>/
  images/o0/
  images/o1/
  results.jsonl
  summary.md
  manifest_snapshot.jsonl

data/curated_pools/<pool_name>/
  images/o0/
  images/o1/
  curated_index.jsonl
  curated_summary.md

data/paired_datasets/
```

`data/generated_runs/<run_name>/` is the raw experiment record and may contain images that later receive `semantic_reject`. `data/curated_pools/<pool_name>/` contains only images materialized from `semantic_keep` judge rows. `data/paired_datasets/` is reserved for later pair construction/export.

`data/images/` is deprecated as the canonical generated-image location. Some historical manifests or result files may still reference it for compatibility, but new Cosmos3 batch runs should write raw images under `data/generated_runs/<run_name>/images/`.

Manifest rows may still contain `output_image_path` values under `data/images/` because older tools and artifacts expect that field. New manifests mark this as `output_image_path_is_placeholder: true` and include `runtime_output_layout`. During dry-run or generation, `scripts/08_run_cosmos3_batch.py` rewrites `output_image_path` to the actual by-run path, sets `output_image_path_is_placeholder: false`, and keeps the original value in `legacy_output_image_path`.

## Workflow

Build a smoke manifest:

```bash
python scripts/07_build_cosmos3_manifest.py \
  --plan smoke12 \
  --use_enrichment true \
  --enrichment_file specs/enrichment/llm_enriched_qwen3-vl_30b-a3b-instruct-q4_K_M_stratified10_preview.jsonl
```

Review the printed enrichment coverage and the sidecar manifest report before generation. Deterministic fallback rows are allowed for traceability, but they should not be silent.

Dry-run the manifest and inspect commands:

```bash
python scripts/08_run_cosmos3_batch.py \
  --manifest prompts/manifests/cosmos3_smoke12_manifest.jsonl \
  --dry_run
```

First actual one-image test, only after inspecting the dry-run plan:

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

Only after the one-image output is successful and manually inspected should you run the full `smoke12` manifest:

```bash
python scripts/08_run_cosmos3_batch.py \
  --manifest prompts/manifests/cosmos3_smoke12_manifest.jsonl \
  --run_name ahd_cosmos3_smoke12 \
  --yes
```

Create a manual audit sheet before deciding whether to scale beyond `smoke12`:

```bash
python scripts/10_create_visual_audit_sheet.py \
  --results data/generated_runs/ahd_cosmos3_smoke12/results.jsonl
```

## Notes

- Early outputs should be manually inspected before any larger generation run.
- A 12/12 `smoke12` engineering success only proves the local generation pipeline works; it does not prove semantic AHD usability.
- For `aggregate_transport` O0, exact count mismatch is a warning rather than an automatic failure. The formal visual filter should use count `>= 3`, target visibility, and container/helper absence.
- Actual generation refuses batches larger than 12 images unless `--yes` is provided.
- New actual generation runs write raw images and results under `data/generated_runs/<run_name>/`; dry-run plans are written as `data/generated_runs/<run_name>/plan.jsonl`.
- `configs/cosmos3_batch_generation.yaml` uses `cuda_visible_devices: auto` by default. The batch runner selects the least-used GPU from `nvidia-smi` before generation; set a specific GPU id to override this.
- The runner wraps the local Cosmos3 workflow documented in `../cosmos3/README.md`.
- AHD `target_output_size` is the desired final image size.
- Cosmos3 `cosmos_input.resolution` is an internal preset/bucket, not the final pixel width or height.
- Current verified mapping:
  - `target_output_size: 960x960`
  - `cosmos_input.resolution: "720"`
  - `cosmos_input.aspect_ratio: "1,1"`
  - observed output: `960x960`
- It uses local Cosmos3-Nano by default:
  - env: `/data0/yurunze/conda_envs/codex_cosmos`
  - checkpoint: `/data0/yurunze/models/Cosmos3-Nano`
  - HF auxiliary cache: `/data0/yurunze/models/hf-cache`
- Generated manifests, run plans, result logs, raw images, curated pools, and future paired datasets are local artifacts and are gitignored.
