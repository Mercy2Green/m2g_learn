# Sequential Core Evaluation Dataset Report

- total samples: 8
- images copied: 0
- curated paths referenced: PASS

## Sample Type Counts

- no_tool_control: 1
- positive_aggregate: 1
- positive_reach: 1
- same_o1_different_o0: 3
- wrong_helper_negative: 2

## Same O1 Group

- group id: same_o1_container_000001
- shared O1: container_o1_000001 (../../AHD-benchmark/data/curated_pools/ahd_cosmos3_raw240_qwen32/images/o1/container_o1_000001.jpg)
- same_o1_aggregate_001: task_002 -> helper_found / aggregate_transport
- same_o1_direct_001: task_011 -> direct_is_enough / none
- same_o1_reach_001: task_008 -> continue_search / none

## First Rows

- positive_aggregate_001: O0=../../AHD-benchmark/data/curated_pools/ahd_cosmos3_raw240_qwen32/images/o0/agg_o0_000001.jpg; O1=../../AHD-benchmark/data/curated_pools/ahd_cosmos3_raw240_qwen32/images/o1/container_o1_000001.jpg
- positive_reach_001: O0=../../AHD-benchmark/data/curated_pools/ahd_cosmos3_raw240_qwen32/images/o0/reach_o0_000001.jpg; O1=../../AHD-benchmark/data/curated_pools/ahd_cosmos3_raw240_qwen32/images/o1/longtool_o1_000001.jpg
- wrong_helper_negative_aggregate_001: O0=../../AHD-benchmark/data/curated_pools/ahd_cosmos3_raw240_qwen32/images/o0/agg_o0_000002.jpg; O1=../../AHD-benchmark/data/curated_pools/ahd_cosmos3_raw240_qwen32/images/o1/wrong_o1_000001.jpg
- wrong_helper_negative_reach_001: O0=../../AHD-benchmark/data/curated_pools/ahd_cosmos3_raw240_qwen32/images/o0/reach_o0_000002.jpg; O1=../../AHD-benchmark/data/curated_pools/ahd_cosmos3_raw240_qwen32/images/o1/wrong_o1_000004.jpg
- no_tool_control_001: O0=../../AHD-benchmark/data/curated_pools/ahd_cosmos3_raw240_qwen32/images/o0/direct_o0_000002.jpg; O1=../../AHD-benchmark/data/curated_pools/ahd_cosmos3_raw240_qwen32/images/o1/container_o1_000001.jpg

The standalone no-tool control and same-O1 direct row intentionally reuse the same direct O0/container O1 pair.
