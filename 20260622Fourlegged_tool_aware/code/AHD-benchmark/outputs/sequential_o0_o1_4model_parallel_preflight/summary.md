# Sequential O0/O1 Evaluation Summary

- evaluated rows: 4
- ok evaluations: 4
- generation budget exhausted: 0
- schema echoes: 0
- non-empty parse errors: 0
- provider errors: 0
- clean protocols do not explicitly name task-specific helper types.
- generation/provider failures are not counted as task-capability failures.

## Response Execution Status

| response_status | count |
| --- | ---: |
| ok_eval | 4 |

## By Model

| model | pass | fail | needs_review | parse_error | not_evaluated |
| --- | ---: | ---: | ---: | ---: | ---: |
| ollama_qwen3_5_35b | 1 | 0 | 0 | 0 | 0 |
| ollama_qwen3_vl_30b_a3b_instruct_q4_K_M | 0 | 1 | 0 | 0 | 0 |
| ollama_qwen3_vl_32b_instruct_q4_K_M | 0 | 1 | 0 | 0 | 0 |
| ollama_qwen3_vl_8b | 0 | 1 | 0 | 0 | 0 |

## By Protocol

| protocol | pass | fail | needs_review | parse_error | not_evaluated |
| --- | ---: | ---: | ---: | ---: | ---: |
| single_turn_multi_image | 1 | 3 | 0 | 0 | 0 |

## By Sample Type

| sample_type | pass | fail | needs_review | parse_error | not_evaluated |
| --- | ---: | ---: | ---: | ---: | ---: |
| positive_aggregate | 1 | 3 | 0 | 0 | 0 |

## Same O1 Different O0 Consistency

| model | prompt | group | consistency |
| --- | --- | --- | --- |
| - | - | - | not_available |
