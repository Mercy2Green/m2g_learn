# VLM Judge Aggregate Findings

Image-aware local VLM judge summary. This is still not final paper evidence.

## Overall

| Name | Rows | Pass | Fail | Uncertain | Tested parse | Judge parse | Image used | Image missing | Visual check | Fail rate | Helper-chain rate | Top failure modes |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| overall | 198 | 83 | 69 | 0 | 46 | 0 | 152 | 0 | 0 | 0.4539 | 0.4474 | direct_operation_without_helper:65; tested_model_parse_error:46; helper_search_failure:15; helper_mention_without_use:8; container_affordance_miss:6; conditional_helper_only:5 |

## By task

| Name | Rows | Pass | Fail | Uncertain | Tested parse | Judge parse | Image used | Image missing | Visual check | Fail rate | Helper-chain rate | Top failure modes |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| task_001 | 18 | 5 | 10 | 0 | 3 | 0 | 15 | 0 | 0 | 0.6667 | 0.3333 | direct_operation_without_helper:10; aggregation_failure:3; tested_model_parse_error:3; conditional_helper_only:1 |
| task_002 | 18 | 0 | 15 | 0 | 3 | 0 | 15 | 0 | 0 | 1.0 | 0.0 | helper_search_failure:15; direct_operation_without_helper:15; tested_model_parse_error:3; helper_mention_without_use:1 |
| task_003 | 18 | 11 | 2 | 0 | 5 | 0 | 13 | 0 | 0 | 0.1538 | 0.8462 | tested_model_parse_error:5; direct_operation_without_helper:2; helper_mention_without_use:1 |
| task_004 | 18 | 5 | 9 | 0 | 4 | 0 | 14 | 0 | 0 | 0.6429 | 0.3571 | direct_operation_without_helper:8; tested_model_parse_error:4; helper_mention_without_use:2; conditional_helper_only:1 |
| task_005 | 18 | 5 | 8 | 0 | 5 | 0 | 13 | 0 | 0 | 0.6154 | 0.3846 | direct_operation_without_helper:8; tested_model_parse_error:5; conditional_helper_only:1 |
| task_006 | 18 | 9 | 5 | 0 | 4 | 0 | 14 | 0 | 0 | 0.3571 | 0.6429 | container_affordance_miss:5; tested_model_parse_error:4; direct_operation_without_helper:3 |
| task_007 | 18 | 10 | 5 | 0 | 3 | 0 | 15 | 0 | 0 | 0.3333 | 0.6667 | direct_operation_without_helper:5; tested_model_parse_error:3 |
| task_008 | 18 | 8 | 5 | 0 | 5 | 0 | 13 | 0 | 0 | 0.3846 | 0.6154 | tested_model_parse_error:5; direct_operation_without_helper:5; physical_capacity_hallucination:1; conditional_helper_only:1 |
| task_009 | 18 | 9 | 4 | 0 | 5 | 0 | 13 | 0 | 0 | 0.3077 | 0.6923 | tested_model_parse_error:5; direct_operation_without_helper:4 |
| task_010 | 18 | 6 | 6 | 0 | 6 | 0 | 12 | 0 | 0 | 0.5 | 0.5 | tested_model_parse_error:6; direct_operation_without_helper:5; helper_mention_without_use:4; aggregation_failure:1; container_affordance_miss:1; conditional_helper_only:1 |
| task_011 | 18 | 15 | 0 | 0 | 3 | 0 | 15 | 0 | 0 | 0.0 | 0.0 | tested_model_parse_error:3 |

## By model

| Name | Rows | Pass | Fail | Uncertain | Tested parse | Judge parse | Image used | Image missing | Visual check | Fail rate | Helper-chain rate | Top failure modes |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| ollama_gemma3_27b_it_q8_0 | 33 | 10 | 23 | 0 | 0 | 0 | 33 | 0 | 0 | 0.697 | 0.2121 | direct_operation_without_helper:21; helper_mention_without_use:4; container_affordance_miss:4; aggregation_failure:3; helper_search_failure:3; conditional_helper_only:1 |
| ollama_llama3_2_vision_11b_instruct_q8_0 | 33 | 0 | 0 | 0 | 33 | 0 | 0 | 0 | 0 | 0 | 0 | tested_model_parse_error:33 |
| ollama_minicpm_v4_5_q8_0 | 33 | 14 | 19 | 0 | 0 | 0 | 33 | 0 | 0 | 0.5758 | 0.3333 | direct_operation_without_helper:19; conditional_helper_only:3; helper_search_failure:3; helper_mention_without_use:1; physical_capacity_hallucination:1 |
| ollama_qwen3_5_35b | 33 | 17 | 3 | 0 | 13 | 0 | 20 | 0 | 0 | 0.15 | 0.7 | tested_model_parse_error:13; helper_search_failure:3; direct_operation_without_helper:3 |
| ollama_qwen3_vl_30b_a3b_instruct_q4_K_M | 33 | 19 | 14 | 0 | 0 | 0 | 33 | 0 | 0 | 0.4242 | 0.4848 | direct_operation_without_helper:12; helper_search_failure:3; container_affordance_miss:2; helper_mention_without_use:2 |
| ollama_qwen3_vl_32b_instruct_q4_K_M | 33 | 23 | 10 | 0 | 0 | 0 | 33 | 0 | 0 | 0.303 | 0.6061 | direct_operation_without_helper:10; helper_search_failure:3; aggregation_failure:1; helper_mention_without_use:1; conditional_helper_only:1 |

## By prompt

| Name | Rows | Pass | Fail | Uncertain | Tested parse | Judge parse | Image used | Image missing | Visual check | Fail rate | Helper-chain rate | Top failure modes |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| strong_decomposition_free_plan | 66 | 29 | 22 | 0 | 15 | 0 | 51 | 0 | 0 | 0.4314 | 0.4706 | direct_operation_without_helper:19; tested_model_parse_error:15; helper_search_failure:5; container_affordance_miss:3; aggregation_failure:2; helper_mention_without_use:2 |
| strong_decomposition_free_plan_humanoid_dual_arm | 66 | 30 | 21 | 0 | 15 | 0 | 51 | 0 | 0 | 0.4118 | 0.4902 | direct_operation_without_helper:21; tested_model_parse_error:15; helper_search_failure:5; helper_mention_without_use:2; container_affordance_miss:1; conditional_helper_only:1 |
| strong_decomposition_free_plan_quadruped_single_arm | 66 | 24 | 26 | 0 | 16 | 0 | 50 | 0 | 0 | 0.52 | 0.38 | direct_operation_without_helper:25; tested_model_parse_error:16; helper_search_failure:5; helper_mention_without_use:4; aggregation_failure:2; container_affordance_miss:2 |

## By task family

| Name | Rows | Pass | Fail | Uncertain | Tested parse | Judge parse | Image used | Image missing | Visual check | Fail rate | Helper-chain rate | Top failure modes |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| aggregation_transport | 90 | 31 | 38 | 0 | 21 | 0 | 69 | 0 | 0 | 0.5507 | 0.4493 | direct_operation_without_helper:36; tested_model_parse_error:21; helper_mention_without_use:6; aggregation_failure:4; conditional_helper_only:4; container_affordance_miss:1 |
| cleanup_collection | 36 | 18 | 9 | 0 | 9 | 0 | 27 | 0 | 0 | 0.3333 | 0.6667 | tested_model_parse_error:9; direct_operation_without_helper:7; container_affordance_miss:5 |
| control_no_tool | 18 | 15 | 0 | 0 | 3 | 0 | 15 | 0 | 0 | 0.0 | 0.0 | tested_model_parse_error:3 |
| helper_search | 18 | 0 | 15 | 0 | 3 | 0 | 15 | 0 | 0 | 1.0 | 0.0 | helper_search_failure:15; direct_operation_without_helper:15; tested_model_parse_error:3; helper_mention_without_use:1 |
| other | 18 | 11 | 2 | 0 | 5 | 0 | 13 | 0 | 0 | 0.1538 | 0.8462 | tested_model_parse_error:5; direct_operation_without_helper:2; helper_mention_without_use:1 |
| reach_extension | 18 | 8 | 5 | 0 | 5 | 0 | 13 | 0 | 0 | 0.3846 | 0.6154 | tested_model_parse_error:5; direct_operation_without_helper:5; physical_capacity_hallucination:1; conditional_helper_only:1 |
