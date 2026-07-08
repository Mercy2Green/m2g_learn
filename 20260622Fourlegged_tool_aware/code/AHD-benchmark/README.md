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
```

No script in this stage makes model API calls.
