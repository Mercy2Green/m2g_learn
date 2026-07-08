# LLM Enrichment Plan

Stage 0.5 is an optional local Ollama smoke test for text enrichment only.

The deterministic Stage 0 scene specs remain the source of truth. The local model may rewrite natural task wording and image-generation prompt wording, but it must not decide or modify labels.

## Scope

Allowed:

- Rewrite `instruction_en_variant`.
- Rewrite `instruction_zh_variant`.
- Rewrite `cosmos_prompt_variant`.
- Rewrite `negative_prompt_variant`.
- Add non-label notes.

Forbidden:

- Changing source scene specs.
- Adding or modifying gold labels.
- Deciding helper correctness.
- Calling Cosmos3.
- Generating images.
- Running VLM filtering, training, or evaluation.

## Workflow

Run only after Stage 0 generated and checked local specs:

```bash
python scripts/05_ollama_enrich_scene_specs.py --model qwen3-vl:32b-instruct-q4_K_M --max_specs 50
python scripts/06_check_llm_enrichment.py specs/enrichment/llm_enriched_qwen3-vl_32b-instruct-q4_K_M_preview.jsonl
```

Outputs are local generated artifacts under `specs/enrichment/` and are gitignored.

## Output Contract

Each enrichment row must contain exactly:

```json
{
  "spec_id": "...",
  "model_id": "...",
  "instruction_en_variant": "...",
  "instruction_zh_variant": "...",
  "cosmos_prompt_variant": "...",
  "negative_prompt_variant": "...",
  "notes": []
}
```

Rows must not contain label fields such as `gold`, `mode`, `needed_helper_function`, `target_memory`, `helper_candidates_gold`, or `pairing_role`.
