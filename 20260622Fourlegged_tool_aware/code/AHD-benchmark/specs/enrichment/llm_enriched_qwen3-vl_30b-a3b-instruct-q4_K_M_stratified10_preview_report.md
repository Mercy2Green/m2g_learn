# LLM Enrichment Check Report

- Input file: `specs/enrichment/llm_enriched_qwen3-vl_30b-a3b-instruct-q4_K_M_stratified10_preview.jsonl`
- Total rows: 60
- JSON parse failures: 0
- Schema failures: 0
- Leakage failures: 6
- Average prompt length: 282.1

## Note Summary

- leakage_error: 6
- schema_warning: 60

## Examples

- agg_o0_000008: cosmos_prompt_variant contains forbidden action/task term: bedroom
- container_o1_000003: cosmos_prompt_variant contains forbidden action/task term: bedroom
- container_o1_000010: cosmos_prompt_variant contains forbidden action/task term: bedroom
- direct_o0_000010: cosmos_prompt_variant contains forbidden action/task term: bedroom
- reach_o0_000002: cosmos_prompt_variant contains forbidden action/task term: bedroom
- longtool_o1_000010: cosmos_prompt_variant contains forbidden action/task term: bedroom
