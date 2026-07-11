# Strict VLM Judge V3 Image-Audit-Aware Summary

## Overall

- judge model: qwen3-vl:32b-instruct-q4_K_M
- source rows: 384
- eligible rows: 338
- selected rows: 5
- judged rows: 5
- judge errors: 0
- pass/fail/needs_review: 0/0/5
- physical_o1_helper_chain: 0 (0.000)
- embodiment_batching: 0 (0.000)
- direct_multi_trip: 0 (0.000)
- hallucinated_helper: 0 (0.000)
- visual_conflict: 5 (1.000)
- image_audit_overridden rows: 5

## By Model

| model_id | judged | pass | fail | review | physical chain | physical rate | embodiment | embodiment rate | multi-trip | multi-trip rate | hallucinated | hallucinated rate | visual conflict | conflict rate | overridden |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| ollama_qwen3_vl_32b_instruct_q4_K_M | 3 | 0 | 0 | 3 | 0 | 0.000 | 0 | 0.000 | 0 | 0.000 | 0 | 0.000 | 3 | 1.000 | 3 |
| ollama_qwen3_vl_8b | 2 | 0 | 0 | 2 | 0 | 0.000 | 0 | 0.000 | 0 | 0.000 | 0 | 0.000 | 2 | 1.000 | 2 |

## By Protocol

| protocol | judged | pass | fail | review | physical chain | physical rate | embodiment | embodiment rate | multi-trip | multi-trip rate | hallucinated | hallucinated rate | visual conflict | conflict rate | overridden |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| single_turn_multi_image | 3 | 0 | 0 | 3 | 0 | 0.000 | 0 | 0.000 | 0 | 0.000 | 0 | 0.000 | 3 | 1.000 | 3 |
| two_turn_sequential | 2 | 0 | 0 | 2 | 0 | 0.000 | 0 | 0.000 | 0 | 0.000 | 0 | 0.000 | 2 | 1.000 | 2 |

## By Sample Type

| sample_type | judged | pass | fail | review | physical chain | physical rate | embodiment | embodiment rate | multi-trip | multi-trip rate | hallucinated | hallucinated rate | visual conflict | conflict rate | overridden |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| positive_aggregate | 5 | 0 | 0 | 5 | 0 | 0.000 | 0 | 0.000 | 0 | 0.000 | 0 | 0.000 | 5 | 1.000 | 5 |

## Critical Strict V2 vs Strict V3

| group by | value | comparable | physical v2 | physical v3 | hallucinated v2 | hallucinated v3 | review v2 | review v3 | same-O1 pass v2 | same-O1 pass v3 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| overall | all | 5 | 0 | 0 | 1 | 0 | 0 | 5 | 0 | 0 |
| model_id | ollama_qwen3_vl_32b_instruct_q4_K_M | 3 | 0 | 0 | 1 | 0 | 0 | 3 | 0 | 0 |
| model_id | ollama_qwen3_vl_8b | 2 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 0 |
| protocol | single_turn_multi_image | 3 | 0 | 0 | 0 | 0 | 0 | 3 | 0 | 0 |
| protocol | two_turn_sequential | 2 | 0 | 0 | 1 | 0 | 0 | 2 | 0 | 0 |
| sample_type | positive_aggregate | 5 | 0 | 0 | 1 | 0 | 0 | 5 | 0 | 0 |

## Same-O1 Consistency V3

- groups evaluated: 0
- consistency pass: 0
- consistency fail: 0
- not available: 0
- consistency pass rate: n/a

| model | prompt | group | consistency |
| --- | --- | --- | --- |
