# LLM Enrichment Check Report

- Input file: `specs/enrichment/llm_enriched_qwen3.5_35b_preview.jsonl`
- Total rows: 20
- JSON parse failures: 0
- Schema failures: 0
- Leakage failures: 1
- Average prompt length: 175.7

## Note Summary

- Camera view must be robot first-person.: 1
- Enforced target count of seven bottles on low table.: 1
- Ensure 4 drink cans are clearly visible on the wooden desk surface.: 1
- Ensure exactly 3 sports drink bottles are visible on the shelf edge.: 1
- Ensure exactly six drink cans are visible.: 1
- Ensures six drink cans and shelf edge are visible.: 1
- Exclude all forbidden objects including people and containers in visual scene.: 1
- Exclude all human interaction and carrying tools.: 1
- Exclude all specified forbidden objects and containers.: 1
- Excluded all human elements and auxiliary containers.: 1
- Excludes all forbidden objects like people and containers.: 1
- Maintain low quadruped camera perspective.: 1
- Quadruped robot with single arm capability.: 1
- Scene must include exactly three drink cans on a wooden desk.: 1
- Target count is exactly six.: 1
- View stage O0: 1
- leakage_error: 1
- request_error: 3

## Examples

- agg_o0_000009: instruction_en_variant contains forbidden label term: direct
