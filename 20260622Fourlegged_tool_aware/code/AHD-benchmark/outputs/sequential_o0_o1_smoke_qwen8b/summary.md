# Sequential O0/O1 Evaluation Summary

- evaluated rows: 8
- parse success: 2
- parse errors: 6
- clean protocols do not explicitly name task-specific helper types.

## By Protocol

| protocol | pass | fail | needs_review | parse_error |
| --- | ---: | ---: | ---: | ---: |
| single_turn_multi_image | 0 | 0 | 1 | 3 |
| two_turn_sequential | 1 | 0 | 0 | 3 |

## By Sample Type

| sample_type | pass | fail | needs_review | parse_error |
| --- | ---: | ---: | ---: | ---: |
| no_tool_control | 1 | 0 | 1 | 0 |
| positive_aggregate | 0 | 0 | 0 | 2 |
| positive_reach | 0 | 0 | 0 | 2 |
| wrong_helper_negative | 0 | 0 | 0 | 2 |

## Same O1 Different O0 Consistency

| model | prompt | group | consistency |
| --- | --- | --- | --- |
| - | - | - | not_available |
