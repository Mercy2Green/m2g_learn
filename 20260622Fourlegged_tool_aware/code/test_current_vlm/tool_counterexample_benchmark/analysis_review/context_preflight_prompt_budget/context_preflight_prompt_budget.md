# Context Preflight Prompt Budget

This is a text-only preflight estimate. It does not include image tokens, so actual VLM context use may be higher.

## Risk Counts

- high: 0
- medium: 0
- low: 1188
- unknown: 0

## Highest Estimated Usage

| Model | Prompt | Task | Approx input | Max tokens | Num ctx | Estimated total | Headroom | Risk |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| ollama_qwen3_vl_32b_instruct_q4_K_M | search_explicit_strong_decomposition_free_plan_quadruped_single_arm | task_001 | 571 | 1536 | 8192 | 2107 | 6085 | low |
| ollama_qwen3_vl_32b_instruct_q4_K_M | search_explicit_strong_decomposition_free_plan_quadruped_single_arm | task_002 | 571 | 1536 | 8192 | 2107 | 6085 | low |
| ollama_qwen3_vl_30b_a3b_instruct_q4_K_M | search_explicit_strong_decomposition_free_plan_quadruped_single_arm | task_001 | 571 | 1536 | 8192 | 2107 | 6085 | low |
| ollama_qwen3_vl_30b_a3b_instruct_q4_K_M | search_explicit_strong_decomposition_free_plan_quadruped_single_arm | task_002 | 571 | 1536 | 8192 | 2107 | 6085 | low |
| ollama_qwen3_5_35b | search_explicit_strong_decomposition_free_plan_quadruped_single_arm | task_001 | 571 | 1536 | 8192 | 2107 | 6085 | low |
| ollama_qwen3_5_35b | search_explicit_strong_decomposition_free_plan_quadruped_single_arm | task_002 | 571 | 1536 | 8192 | 2107 | 6085 | low |
| ollama_minicpm_v4_5_q8_0 | search_explicit_strong_decomposition_free_plan_quadruped_single_arm | task_001 | 571 | 1536 | 4096 | 2107 | 1989 | low |
| ollama_minicpm_v4_5_q8_0 | search_explicit_strong_decomposition_free_plan_quadruped_single_arm | task_002 | 571 | 1536 | 4096 | 2107 | 1989 | low |
| ollama_gemma3_27b_it_q8_0 | search_explicit_strong_decomposition_free_plan_quadruped_single_arm | task_001 | 571 | 1536 | 8192 | 2107 | 6085 | low |
| ollama_gemma3_27b_it_q8_0 | search_explicit_strong_decomposition_free_plan_quadruped_single_arm | task_002 | 571 | 1536 | 8192 | 2107 | 6085 | low |
| ollama_llama3_2_vision_11b_instruct_q8_0 | search_explicit_strong_decomposition_free_plan_quadruped_single_arm | task_001 | 571 | 1536 | 4096 | 2107 | 1989 | low |
| ollama_llama3_2_vision_11b_instruct_q8_0 | search_explicit_strong_decomposition_free_plan_quadruped_single_arm | task_002 | 571 | 1536 | 4096 | 2107 | 1989 | low |
| ollama_qwen3_vl_32b_instruct_q4_K_M | search_explicit_strong_decomposition_free_plan_quadruped_single_arm | task_003 | 568 | 1536 | 8192 | 2104 | 6088 | low |
| ollama_qwen3_vl_32b_instruct_q4_K_M | search_explicit_strong_decomposition_free_plan_quadruped_single_arm | task_004 | 568 | 1536 | 8192 | 2104 | 6088 | low |
| ollama_qwen3_vl_30b_a3b_instruct_q4_K_M | search_explicit_strong_decomposition_free_plan_quadruped_single_arm | task_003 | 568 | 1536 | 8192 | 2104 | 6088 | low |
| ollama_qwen3_vl_30b_a3b_instruct_q4_K_M | search_explicit_strong_decomposition_free_plan_quadruped_single_arm | task_004 | 568 | 1536 | 8192 | 2104 | 6088 | low |
| ollama_qwen3_5_35b | search_explicit_strong_decomposition_free_plan_quadruped_single_arm | task_003 | 568 | 1536 | 8192 | 2104 | 6088 | low |
| ollama_qwen3_5_35b | search_explicit_strong_decomposition_free_plan_quadruped_single_arm | task_004 | 568 | 1536 | 8192 | 2104 | 6088 | low |
| ollama_minicpm_v4_5_q8_0 | search_explicit_strong_decomposition_free_plan_quadruped_single_arm | task_003 | 568 | 1536 | 4096 | 2104 | 1992 | low |
| ollama_minicpm_v4_5_q8_0 | search_explicit_strong_decomposition_free_plan_quadruped_single_arm | task_004 | 568 | 1536 | 4096 | 2104 | 1992 | low |

## By Model

| Name | Rows | Avg approx input | Max approx input | High | Medium | Low | Unknown |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| ollama_gemma3_27b_it_q8_0 | 198 | 389.81 | 571 | 0 | 0 | 198 | 0 |
| ollama_llama3_2_vision_11b_instruct_q8_0 | 198 | 389.81 | 571 | 0 | 0 | 198 | 0 |
| ollama_minicpm_v4_5_q8_0 | 198 | 389.81 | 571 | 0 | 0 | 198 | 0 |
| ollama_qwen3_5_35b | 198 | 389.81 | 571 | 0 | 0 | 198 | 0 |
| ollama_qwen3_vl_30b_a3b_instruct_q4_K_M | 198 | 389.81 | 571 | 0 | 0 | 198 | 0 |
| ollama_qwen3_vl_32b_instruct_q4_K_M | 198 | 389.81 | 571 | 0 | 0 | 198 | 0 |

## By Prompt

| Name | Rows | Avg approx input | Max approx input | High | Medium | Low | Unknown |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| efficient_safe_free_plan | 66 | 226.18 | 232 | 0 | 0 | 66 | 0 |
| efficient_safe_free_plan_humanoid_dual_arm | 66 | 281.73 | 287 | 0 | 0 | 66 | 0 |
| efficient_safe_free_plan_quadruped_single_arm | 66 | 295.18 | 301 | 0 | 0 | 66 | 0 |
| natural_free_plan | 66 | 220.73 | 226 | 0 | 0 | 66 | 0 |
| natural_free_plan_humanoid_dual_arm | 66 | 273.73 | 279 | 0 | 0 | 66 | 0 |
| natural_free_plan_quadruped_single_arm | 66 | 287.18 | 293 | 0 | 0 | 66 | 0 |
| search_explicit_strong_decomposition_free_plan | 66 | 497.18 | 503 | 0 | 0 | 66 | 0 |
| search_explicit_strong_decomposition_free_plan_humanoid_dual_arm | 66 | 551.18 | 557 | 0 | 0 | 66 | 0 |
| search_explicit_strong_decomposition_free_plan_quadruped_single_arm | 66 | 565.73 | 571 | 0 | 0 | 66 | 0 |
| strong_decomposition_free_plan | 66 | 403.18 | 409 | 0 | 0 | 66 | 0 |
| strong_decomposition_free_plan_humanoid_dual_arm | 66 | 457.18 | 463 | 0 | 0 | 66 | 0 |
| strong_decomposition_free_plan_quadruped_single_arm | 66 | 471.73 | 477 | 0 | 0 | 66 | 0 |
| structured_tool_action_chain_probe_humanoid_dual_arm | 66 | 519.18 | 525 | 0 | 0 | 66 | 0 |
| structured_tool_action_chain_probe_quadruped_single_arm | 66 | 532.73 | 538 | 0 | 0 | 66 | 0 |
| structured_tool_probe | 66 | 466.18 | 472 | 0 | 0 | 66 | 0 |
| tool_prior_free_plan | 66 | 280.73 | 286 | 0 | 0 | 66 | 0 |
| tool_prior_free_plan_humanoid_dual_arm | 66 | 336.18 | 342 | 0 | 0 | 66 | 0 |
| tool_prior_free_plan_quadruped_single_arm | 66 | 350.73 | 356 | 0 | 0 | 66 | 0 |

## Recommendations

- If a row is already medium/high in this text-only preflight, actual VLM calls are riskier because image tokens are not counted here.
- For the six-model round05 run, prefer `num_ctx >= 8192` where the model supports it.
- Pay particular attention to `ollama_minicpm_v4_5_q8_0` and `ollama_llama3_2_vision_11b_instruct_q8_0` when they use `num_ctx=4096` and `max_tokens=1536`.
- If context risk appears in real run metadata, consider raising `num_ctx`, lowering `max_tokens` to 1024, or both.
