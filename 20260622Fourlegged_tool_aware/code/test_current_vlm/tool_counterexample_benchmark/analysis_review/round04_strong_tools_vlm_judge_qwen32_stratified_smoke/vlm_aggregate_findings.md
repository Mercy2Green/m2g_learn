# VLM Judge Aggregate Findings

Image-aware local VLM judge summary. This is still not final paper evidence.

## Overall

| Name | Rows | Pass | Fail | Uncertain | Tested parse | Judge parse | Image used | Image missing | Visual check | Fail rate | Helper-chain rate | Top failure modes |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| overall | 24 | 7 | 5 | 0 | 12 | 0 | 12 | 0 | 0 | 0.4167 | 0.3333 | tested_model_parse_error:12; Direct hand carrying of clothes without using the visible laundry basket:2; No aggregation into helper container before transport:2; Plan specifies direct individual pickup and transport of each item without using any helper object, violating the task requirement for aggregation_transport with a non-target container.:1; No committed use of a tray, basin, or basket to collect and carry multiple dishes together.:1; Plan involves direct individual pickup of each dish without using any helper object for aggregation and transport.:1 |

## By task

| Name | Rows | Pass | Fail | Uncertain | Tested parse | Judge parse | Image used | Image missing | Visual check | Fail rate | Helper-chain rate | Top failure modes |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| task_005 | 6 | 1 | 2 | 0 | 3 | 0 | 3 | 0 | 0 | 0.6667 | 0.3333 | tested_model_parse_error:3; Plan specifies direct individual pickup and transport of each item without using any helper object, violating the task requirement for aggregation_transport with a non-target container.:1; No committed use of a tray, basin, or basket to collect and carry multiple dishes together.:1; Plan involves direct individual pickup of each dish without using any helper object for aggregation and transport.:1; No commitment to use a tray, basin, or basket as specified in expected tool types.:1; Multiple trips are planned instead of aggregating items into a container for single transport.:1 |
| task_007 | 6 | 0 | 3 | 0 | 3 | 0 | 3 | 0 | 0 | 1.0 | 0.0 | tested_model_parse_error:3; Direct hand carrying of clothes without using the visible laundry basket:2; No aggregation into helper container before transport:2; Plan does not use the visible laundry basket to aggregate and transport clothes.:1; Direct hand carrying of clothes is invalid for task_007 as per rubric.:1; Plan does not commit to using the available laundry basket:1 |
| task_008 | 6 | 3 | 0 | 0 | 3 | 0 | 3 | 0 | 0 | 0.0 | 1.0 | tested_model_parse_error:3 |
| task_011 | 6 | 3 | 0 | 0 | 3 | 0 | 3 | 0 | 0 | 0.0 | 0.0 | tested_model_parse_error:3 |

## By model

| Name | Rows | Pass | Fail | Uncertain | Tested parse | Judge parse | Image used | Image missing | Visual check | Fail rate | Helper-chain rate | Top failure modes |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| ollama_gemma3_27b_it_q8_0 | 12 | 7 | 5 | 0 | 0 | 0 | 12 | 0 | 0 | 0.4167 | 0.3333 | Direct hand carrying of clothes without using the visible laundry basket:2; No aggregation into helper container before transport:2; Plan specifies direct individual pickup and transport of each item without using any helper object, violating the task requirement for aggregation_transport with a non-target container.:1; No committed use of a tray, basin, or basket to collect and carry multiple dishes together.:1; Plan involves direct individual pickup of each dish without using any helper object for aggregation and transport.:1; No commitment to use a tray, basin, or basket as specified in expected tool types.:1 |
| ollama_llama3_2_vision_11b_instruct_q8_0 | 12 | 0 | 0 | 0 | 12 | 0 | 0 | 0 | 0 | 0 | 0 | tested_model_parse_error:12 |

## By prompt

| Name | Rows | Pass | Fail | Uncertain | Tested parse | Judge parse | Image used | Image missing | Visual check | Fail rate | Helper-chain rate | Top failure modes |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| strong_decomposition_free_plan | 8 | 2 | 2 | 0 | 4 | 0 | 4 | 0 | 0 | 0.5 | 0.25 | tested_model_parse_error:4; Plan specifies direct individual pickup and transport of each item without using any helper object, violating the task requirement for aggregation_transport with a non-target container.:1; No committed use of a tray, basin, or basket to collect and carry multiple dishes together.:1; Plan does not use the visible laundry basket to aggregate and transport clothes.:1; Direct hand carrying of clothes is invalid for task_007 as per rubric.:1 |
| strong_decomposition_free_plan_humanoid_dual_arm | 8 | 3 | 1 | 0 | 4 | 0 | 4 | 0 | 0 | 0.25 | 0.5 | tested_model_parse_error:4; Direct hand carrying of clothes without using the visible laundry basket:1; No aggregation into helper container before transport:1; Plan does not commit to using the available laundry basket:1 |
| strong_decomposition_free_plan_quadruped_single_arm | 8 | 2 | 2 | 0 | 4 | 0 | 4 | 0 | 0 | 0.5 | 0.25 | tested_model_parse_error:4; Plan involves direct individual pickup of each dish without using any helper object for aggregation and transport.:1; No commitment to use a tray, basin, or basket as specified in expected tool types.:1; Multiple trips are planned instead of aggregating items into a container for single transport.:1; Direct hand carrying of clothes without using the visible laundry basket:1; No aggregation into helper container before transport:1 |

## By task family

| Name | Rows | Pass | Fail | Uncertain | Tested parse | Judge parse | Image used | Image missing | Visual check | Fail rate | Helper-chain rate | Top failure modes |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| aggregation_transport | 12 | 1 | 5 | 0 | 6 | 0 | 6 | 0 | 0 | 0.8333 | 0.1667 | tested_model_parse_error:6; Direct hand carrying of clothes without using the visible laundry basket:2; No aggregation into helper container before transport:2; Plan specifies direct individual pickup and transport of each item without using any helper object, violating the task requirement for aggregation_transport with a non-target container.:1; No committed use of a tray, basin, or basket to collect and carry multiple dishes together.:1; Plan involves direct individual pickup of each dish without using any helper object for aggregation and transport.:1 |
| control_no_tool | 6 | 3 | 0 | 0 | 3 | 0 | 3 | 0 | 0 | 0.0 | 0.0 | tested_model_parse_error:3 |
| reach_extension | 6 | 3 | 0 | 0 | 3 | 0 | 3 | 0 | 0 | 0.0 | 1.0 | tested_model_parse_error:3 |
