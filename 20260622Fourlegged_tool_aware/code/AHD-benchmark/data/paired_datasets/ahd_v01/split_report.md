# AHD v0.1 Split Report

Split unit: O1 image group. Ratios are applied deterministically within each O1 spec type.

## Counts

| split | Stage1 rows | Stage2 rows | O1 groups |
| --- | ---: | ---: | ---: |
| train | 71 | 207 | 69 |
| val | 10 | 27 | 9 |
| test | 20 | 63 | 21 |

## Stage2 Task Family Distribution

| category | train | val | test |
| --- | ---: | ---: | ---: |
| aggregate_transport | 69 | 9 | 21 |
| direct_is_enough | 69 | 9 | 21 |
| extend_reach | 69 | 9 | 21 |

## O1 Spec Type Distribution

| category | train | val | test |
| --- | ---: | ---: | ---: |
| container_helper_o1_target_absent | 24 | 3 | 7 |
| long_tool_helper_o1_target_absent | 22 | 3 | 7 |
| wrong_helper_o1_target_absent | 23 | 3 | 7 |

## Same O1 Leakage Check

- train O1 ids intersect val O1 ids: 0
- train O1 ids intersect test O1 ids: 0
- val O1 ids intersect test O1 ids: 0
- result: PASS
