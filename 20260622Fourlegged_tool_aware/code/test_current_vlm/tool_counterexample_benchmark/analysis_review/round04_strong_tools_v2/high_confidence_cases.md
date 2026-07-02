# High Confidence Cases

## Clean counterexample candidates

- None in this subset.

## Tool-prior intervention successes

- None in this subset.

## Structured diagnostic cases

- None in this subset.

## Robust failures

- task_001 / Weixin Image_20260629231738_395_27.jpg / ollama_gemma3_27b_it_q8_0 / strong_decomposition_free_plan_quadruped_single_arm: true_fail [aggregation_failure;container_affordance_miss]. Expected helper use, but no valid helper action chain is evident.
- task_006 / Weixin Image_20260629231745_400_27.jpg / ollama_gemma3_27b_it_q8_0 / strong_decomposition_free_plan: true_fail [aggregation_failure;container_affordance_miss;tool_necessity_miss]. Plan directly operates on the target although helper use is expected. Expected helper use, but no valid helper action chain is evident.
- task_009 / Weixin Image_20260629231751_404_27.jpg / ollama_gemma3_27b_it_q8_0 / strong_decomposition_free_plan_quadruped_single_arm: true_fail [aggregation_failure;container_affordance_miss;tool_necessity_miss]. Plan directly operates on the target although helper use is expected. Expected helper use, but no valid helper action chain is evident.
- task_001 / Weixin Image_20260629231738_395_27.jpg / ollama_minicpm_v4_5_q8_0 / strong_decomposition_free_plan: true_fail [aggregation_failure;container_affordance_miss;tool_necessity_miss]. Plan directly operates on the target although helper use is expected. Expected helper use, but no valid helper action chain is evident.
- task_011 / Weixin Image_20260629231748_402_27.jpg / ollama_minicpm_v4_5_q8_0 / strong_decomposition_free_plan_humanoid_dual_arm: true_fail [helper_mention_without_use]. Helper use is only conditional or optional, with no committed helper action chain.
- task_011 / Weixin Image_20260629231748_402_27.jpg / ollama_qwen3_5_35b / strong_decomposition_free_plan_humanoid_dual_arm: true_fail [helper_mention_without_use]. Helper use is only conditional or optional, with no committed helper action chain.

