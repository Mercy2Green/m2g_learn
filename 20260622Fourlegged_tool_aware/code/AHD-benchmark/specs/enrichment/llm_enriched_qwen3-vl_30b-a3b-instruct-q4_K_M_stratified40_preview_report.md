# LLM Enrichment Check Report

- Input file: `specs/enrichment/llm_enriched_qwen3-vl_30b-a3b-instruct-q4_K_M_stratified40_preview.jsonl`
- Total rows: 240
- JSON parse failures: 0
- Schema failures: 0
- Leakage failures: 50
- Average prompt length: 275.8

## Note Summary

- leakage_error: 50
- schema_warning: 241

## Examples

- agg_o0_000008: cosmos_prompt_variant contains forbidden action/task term: bedroom
- agg_o0_000013: cosmos_prompt_variant contains forbidden action/task term: bedroom
- agg_o0_000014: cosmos_prompt_variant contains forbidden action/task term: bedroom
- agg_o0_000016: cosmos_prompt_variant contains forbidden action/task term: bedroom
- agg_o0_000017: cosmos_prompt_variant contains forbidden action/task term: transport
- agg_o0_000023: cosmos_prompt_variant contains forbidden action/task term: bedroom
- agg_o0_000025: cosmos_prompt_variant contains forbidden action/task term: bedroom
- agg_o0_000029: cosmos_prompt_variant contains forbidden action/task term: bedroom
- agg_o0_000040: cosmos_prompt_variant contains forbidden action/task term: bedroom
- container_o1_000003: cosmos_prompt_variant contains forbidden action/task term: bedroom
- container_o1_000010: cosmos_prompt_variant contains forbidden action/task term: bedroom
- container_o1_000012: cosmos_prompt_variant contains forbidden action/task term: bedroom
- container_o1_000013: cosmos_prompt_variant contains forbidden action/task term: bedroom
- container_o1_000019: cosmos_prompt_variant contains forbidden action/task term: bedroom
- container_o1_000021: cosmos_prompt_variant contains forbidden action/task term: bedroom
- container_o1_000022: cosmos_prompt_variant contains forbidden action/task term: bedroom
- container_o1_000026: cosmos_prompt_variant contains forbidden action/task term: bedroom
- container_o1_000029: cosmos_prompt_variant contains forbidden action/task term: bedroom
- container_o1_000030: cosmos_prompt_variant contains forbidden action/task term: bedroom
- container_o1_000034: cosmos_prompt_variant contains forbidden action/task term: bedroom
- container_o1_000035: cosmos_prompt_variant contains forbidden action/task term: bedroom
- container_o1_000038: cosmos_prompt_variant contains forbidden action/task term: bedroom
- direct_o0_000010: cosmos_prompt_variant contains forbidden action/task term: bedroom
- direct_o0_000018: cosmos_prompt_variant contains forbidden action/task term: bedroom
- direct_o0_000021: cosmos_prompt_variant contains forbidden action/task term: bedroom
- direct_o0_000022: cosmos_prompt_variant contains forbidden action/task term: bedroom
- direct_o0_000028: cosmos_prompt_variant contains forbidden action/task term: bedroom
- direct_o0_000033: cosmos_prompt_variant contains forbidden action/task term: bedroom
- direct_o0_000040: cosmos_prompt_variant contains forbidden action/task term: bedroom
- reach_o0_000002: cosmos_prompt_variant contains forbidden action/task term: bedroom
- reach_o0_000012: cosmos_prompt_variant contains forbidden action/task term: bedroom
- reach_o0_000020: cosmos_prompt_variant contains forbidden action/task term: bedroom
- reach_o0_000034: cosmos_prompt_variant contains forbidden action/task term: bedroom
- longtool_o1_000010: cosmos_prompt_variant contains forbidden action/task term: bedroom
- longtool_o1_000011: cosmos_prompt_variant contains forbidden action/task term: bedroom
- longtool_o1_000021: cosmos_prompt_variant contains forbidden action/task term: bedroom
- longtool_o1_000024: cosmos_prompt_variant contains forbidden action/task term: bedroom
- longtool_o1_000031: cosmos_prompt_variant contains forbidden action/task term: bedroom
- longtool_o1_000032: cosmos_prompt_variant contains forbidden action/task term: bedroom
- longtool_o1_000033: cosmos_prompt_variant contains forbidden action/task term: bedroom
- longtool_o1_000039: cosmos_prompt_variant contains forbidden action/task term: bedroom
- wrong_o1_000013: cosmos_prompt_variant contains forbidden action/task term: bedroom
- wrong_o1_000015: cosmos_prompt_variant contains forbidden action/task term: bedroom
- wrong_o1_000016: cosmos_prompt_variant contains forbidden action/task term: bedroom
- wrong_o1_000017: cosmos_prompt_variant contains forbidden action/task term: bedroom
- wrong_o1_000023: cosmos_prompt_variant contains forbidden action/task term: bedroom
- wrong_o1_000028: cosmos_prompt_variant contains forbidden action/task term: bedroom
- wrong_o1_000032: cosmos_prompt_variant contains forbidden action/task term: bedroom
- wrong_o1_000037: cosmos_prompt_variant contains forbidden action/task term: bedroom
- wrong_o1_000039: cosmos_prompt_variant contains forbidden action/task term: bedroom
