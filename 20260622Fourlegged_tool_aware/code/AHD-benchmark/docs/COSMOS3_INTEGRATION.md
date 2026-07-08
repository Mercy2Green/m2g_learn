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

## Workflow

Build a smoke manifest:

```bash
python scripts/07_build_cosmos3_manifest.py \
  --plan smoke12 \
  --use_enrichment true \
  --enrichment_file specs/enrichment/llm_enriched_qwen3-vl_30b-a3b-instruct-q4_K_M_stratified10_preview.jsonl
```

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
  --results data/runs/ahd_cosmos3_one_image_test_results.jsonl
```

Only after the one-image output is successful and manually inspected should you run the full `smoke12` manifest:

```bash
python scripts/08_run_cosmos3_batch.py \
  --manifest prompts/manifests/cosmos3_smoke12_manifest.jsonl \
  --run_name ahd_cosmos3_smoke12 \
  --yes
```

## Notes

- Early outputs should be manually inspected before any larger generation run.
- Actual generation refuses batches larger than 12 images unless `--yes` is provided.
- The runner wraps the local Cosmos3 workflow documented in `../cosmos3/README.md`.
- `default_resolution: 960x960` is converted to the local Cosmos image tier `resolution=720` with `aspect_ratio=1,1`, which produces a 960x960 image in the verified local framework.
- It uses local Cosmos3-Nano by default:
  - env: `/data0/yurunze/conda_envs/codex_cosmos`
  - checkpoint: `/data0/yurunze/models/Cosmos3-Nano`
  - HF auxiliary cache: `/data0/yurunze/models/hf-cache`
- Generated manifests, run plans, result logs, and images are local artifacts and are gitignored.
