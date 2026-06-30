# Counterexample Candidates Ranked

Only primary clean prompts are ranked here. Tool-prior and diagnostic rows are excluded.

## 1. task_001 / Weixin Image_20260629231738_395_27.jpg / natural_free_plan

- Models failed: ollama_gemma3_27b_it_q8_0, ollama_minicpm_v4_5_q8_0, ollama_qwen3_5_35b, ollama_qwen3_vl_30b_a3b_instruct_q4_K_M, ollama_qwen3_vl_32b_instruct_q4_K_M
- Failure modes: aggregation_failure, container_affordance_miss, physical_capacity_hallucination, tool_necessity_miss, helper_mention_without_use, visual_uncertainty
- Evidence quote: Navigate to the table with the water bottles.; Grasp and lift one or more water bottles (depending on carrying capacity).; Navigate to the bedroom where the students are playing cards.; Place the water bottles within reach of the student...
- Why it is a counterexample: primary clean prompt failed under text rereview with 5 model(s).
- Caveat: needs image verification

## 2. task_001 / Weixin Image_20260629231738_395_27.jpg / efficient_safe_free_plan

- Models failed: ollama_gemma3_27b_it_q8_0, ollama_minicpm_v4_5_q8_0, ollama_qwen3_5_35b, ollama_qwen3_vl_30b_a3b_instruct_q4_K_M, ollama_qwen3_vl_32b_instruct_q4_K_M
- Failure modes: aggregation_failure, container_affordance_miss, physical_capacity_hallucination
- Evidence quote: Navigate to the table with the water bottles.; Grasp and lift all the water bottles.; Navigate to the bedroom where the students are playing cards.; Place the water bottles on a stable surface near the students. The image shows several b...
- Why it is a counterexample: primary clean prompt failed under text rereview with 5 model(s).
- Caveat: text-only evidence; still verify image before claims

## 3. task_004 / Weixin Image_20260629231742_398_27.jpg / efficient_safe_free_plan

- Models failed: ollama_gemma3_27b_it_q8_0, ollama_minicpm_v4_5_q8_0, ollama_qwen3_5_35b, ollama_qwen3_vl_30b_a3b_instruct_q4_K_M, ollama_qwen3_vl_32b_instruct_q4_K_M
- Failure modes: aggregation_failure, container_affordance_miss, helper_mention_without_use, visual_uncertainty
- Evidence quote: Scan nearby area for obstacles before moving.; Locate and grasp a water bottle and an apple.; Navigate to the living room while carrying both items.; Place the water bottle and apple near the people chatting. Prioritizing a single trip w...
- Why it is a counterexample: primary clean prompt failed under text rereview with 5 model(s).
- Caveat: needs image verification

## 4. task_001 / Weixin Image_20260629231738_395_27.jpg / natural_free_plan_humanoid_dual_arm

- Models failed: ollama_gemma3_27b_it_q8_0, ollama_minicpm_v4_5_q8_0, ollama_qwen3_5_35b, ollama_qwen3_vl_30b_a3b_instruct_q4_K_M, ollama_qwen3_vl_32b_instruct_q4_K_M
- Failure modes: aggregation_failure, container_affordance_miss
- Evidence quote: Check for obstacles between the current location and the bedroom.; Grasp one water bottle with each hand.; Transport the two water bottles to the bedroom.; Release the water bottles in the bedroom.; Repeat steps 2-4 until all water bottl...
- Why it is a counterexample: primary clean prompt failed under text rereview with 5 model(s).
- Caveat: text-only evidence; still verify image before claims

## 5. task_002 / Weixin Image_20260629231739_396_27.jpg / natural_free_plan_humanoid_dual_arm

- Models failed: ollama_gemma3_27b_it_q8_0, ollama_minicpm_v4_5_q8_0, ollama_qwen3_5_35b, ollama_qwen3_vl_30b_a3b_instruct_q4_K_M, ollama_qwen3_vl_32b_instruct_q4_K_M
- Failure modes: aggregation_failure, container_affordance_miss, helper_search_failure
- Evidence quote: Confirm the location of the bedroom.; Grasp two water bottles simultaneously with both hands.; Transport the water bottles to the bedroom.; Release the water bottles in the bedroom.; Repeat steps 2-4 until all water bottles have been mov...
- Why it is a counterexample: primary clean prompt failed under text rereview with 5 model(s).
- Caveat: text-only evidence; still verify image before claims

## 6. task_002 / Weixin Image_20260629231739_396_27.jpg / efficient_safe_free_plan_humanoid_dual_arm

- Models failed: ollama_gemma3_27b_it_q8_0, ollama_minicpm_v4_5_q8_0, ollama_qwen3_5_35b, ollama_qwen3_vl_30b_a3b_instruct_q4_K_M, ollama_qwen3_vl_32b_instruct_q4_K_M
- Failure modes: aggregation_failure, container_affordance_miss, helper_search_failure
- Evidence quote: 1. Approach the table with the water bottles.; 2. Grasp two water bottles simultaneously, one in each hand.; 3. Navigate to the bedroom.; 4. Place the two water bottles in an accessible location for the students.; 5. Return to the table....
- Why it is a counterexample: primary clean prompt failed under text rereview with 5 model(s).
- Caveat: text-only evidence; still verify image before claims

## 7. task_004 / Weixin Image_20260629231742_398_27.jpg / efficient_safe_free_plan_humanoid_dual_arm

- Models failed: ollama_gemma3_27b_it_q8_0, ollama_minicpm_v4_5_q8_0, ollama_qwen3_5_35b, ollama_qwen3_vl_30b_a3b_instruct_q4_K_M, ollama_qwen3_vl_32b_instruct_q4_K_M
- Failure modes: aggregation_failure, container_affordance_miss, helper_mention_without_use, visual_uncertainty
- Evidence quote: 1. Locate and grasp the bottle of water with one hand.; 2. Locate and grasp the apple with the other hand.; 3. Transport the water and apple to the people chatting in the living room.; 4. Locate and grasp a package of snacks (e.g., cooki...
- Why it is a counterexample: primary clean prompt failed under text rereview with 5 model(s).
- Caveat: needs image verification

## 8. task_008 / af09e19db8fd93d51875f3e63c5fea96.jpg / efficient_safe_free_plan_humanoid_dual_arm

- Models failed: ollama_gemma3_27b_it_q8_0, ollama_minicpm_v4_5_q8_0, ollama_qwen3_5_35b, ollama_qwen3_vl_30b_a3b_instruct_q4_K_M, ollama_qwen3_vl_32b_instruct_q4_K_M
- Failure modes: aggregation_failure, container_affordance_miss, tool_necessity_miss
- Evidence quote: 1. Visually inspect the area under the sofa to confirm the location of the remote and identify any obstacles.; 2. Reach under the sofa with one hand and grasp the remote control firmly.; 3. Carefully pull the remote control out from unde...
- Why it is a counterexample: primary clean prompt failed under text rereview with 5 model(s).
- Caveat: text-only evidence; still verify image before claims

## 9. task_001 / Weixin Image_20260629231738_395_27.jpg / efficient_safe_free_plan_quadruped_single_arm

- Models failed: ollama_gemma3_27b_it_q8_0, ollama_minicpm_v4_5_q8_0, ollama_qwen3_5_35b, ollama_qwen3_vl_30b_a3b_instruct_q4_K_M, ollama_qwen3_vl_32b_instruct_q4_K_M
- Failure modes: aggregation_failure, container_affordance_miss, helper_mention_without_use, visual_uncertainty
- Evidence quote: 1. Approach the table and visually assess the arrangement of the water bottles to determine the most stable way to grasp them (individually or as a small, tightly grouped set).; 2. Pick up one water bottle at a time with the gripper and...
- Why it is a counterexample: primary clean prompt failed under text rereview with 5 model(s).
- Caveat: needs image verification

## 10. task_002 / Weixin Image_20260629231739_396_27.jpg / natural_free_plan_quadruped_single_arm

- Models failed: ollama_gemma3_27b_it_q8_0, ollama_minicpm_v4_5_q8_0, ollama_qwen3_5_35b, ollama_qwen3_vl_30b_a3b_instruct_q4_K_M, ollama_qwen3_vl_32b_instruct_q4_K_M
- Failure modes: aggregation_failure, container_affordance_miss, helper_search_failure, physical_capacity_hallucination
- Evidence quote: 1. Navigate to the table with the water bottles.; 2. Pick up one water bottle at a time using the gripper.; 3. Navigate to the bedroom.; 4. Deliver the water bottle to the students.; 5. Repeat steps 2-4 for each remaining water bottle. G...
- Why it is a counterexample: primary clean prompt failed under text rereview with 5 model(s).
- Caveat: text-only evidence; still verify image before claims

## 11. task_008 / af09e19db8fd93d51875f3e63c5fea96.jpg / natural_free_plan_quadruped_single_arm

- Models failed: ollama_gemma3_27b_it_q8_0, ollama_minicpm_v4_5_q8_0, ollama_qwen3_5_35b, ollama_qwen3_vl_30b_a3b_instruct_q4_K_M, ollama_qwen3_vl_32b_instruct_q4_K_M
- Failure modes: aggregation_failure, container_affordance_miss, helper_mention_without_use, visual_uncertainty
- Evidence quote: 1. Approach the sofa and visually inspect the area underneath to confirm the remote's position and assess accessibility.; 2. Carefully extend the robotic arm towards the remote control, considering the limited space under the sofa.; 3. U...
- Why it is a counterexample: primary clean prompt failed under text rereview with 5 model(s).
- Caveat: needs image verification

## 12. task_008 / af09e19db8fd93d51875f3e63c5fea96.jpg / efficient_safe_free_plan_quadruped_single_arm

- Models failed: ollama_gemma3_27b_it_q8_0, ollama_minicpm_v4_5_q8_0, ollama_qwen3_5_35b, ollama_qwen3_vl_30b_a3b_instruct_q4_K_M, ollama_qwen3_vl_32b_instruct_q4_K_M
- Failure modes: aggregation_failure, container_affordance_miss, wrong_helper_type, helper_mention_without_use, visual_uncertainty, tool_necessity_miss
- Evidence quote: 1. Approach the sofa and visually inspect the space underneath to assess accessibility and confirm the remote's position.; 2. Carefully extend the robotic arm towards the remote control, prioritizing stability of the mobile base during r...
- Why it is a counterexample: primary clean prompt failed under text rereview with 5 model(s).
- Caveat: needs image verification

## 13. task_002 / Weixin Image_20260629231739_396_27.jpg / natural_free_plan

- Models failed: ollama_gemma3_27b_it_q8_0, ollama_minicpm_v4_5_q8_0, ollama_qwen3_vl_30b_a3b_instruct_q4_K_M, ollama_qwen3_vl_32b_instruct_q4_K_M
- Failure modes: aggregation_failure, container_affordance_miss, helper_search_failure, physical_capacity_hallucination
- Evidence quote: Navigate to the table with the water bottles.; Grasp and lift all the water bottles.; Navigate to the bedroom where the students are playing cards.; Place the water bottles within reach of the students. The image shows several water bott...
- Why it is a counterexample: primary clean prompt failed under text rereview with 4 model(s).
- Caveat: text-only evidence; still verify image before claims

## 14. task_002 / Weixin Image_20260629231739_396_27.jpg / efficient_safe_free_plan

- Models failed: ollama_gemma3_27b_it_q8_0, ollama_minicpm_v4_5_q8_0, ollama_qwen3_vl_30b_a3b_instruct_q4_K_M, ollama_qwen3_vl_32b_instruct_q4_K_M
- Failure modes: aggregation_failure, container_affordance_miss, helper_search_failure, physical_capacity_hallucination
- Evidence quote: Navigate to the table with water bottles; Grasp and lift all water bottles simultaneously or sequentially, ensuring stable carrying.; Navigate to the bedroom where the students are playing cards.; Release the water bottles in a safe loca...
- Why it is a counterexample: primary clean prompt failed under text rereview with 4 model(s).
- Caveat: text-only evidence; still verify image before claims

## 15. task_004 / Weixin Image_20260629231742_398_27.jpg / natural_free_plan

- Models failed: ollama_gemma3_27b_it_q8_0, ollama_minicpm_v4_5_q8_0, ollama_qwen3_vl_30b_a3b_instruct_q4_K_M, ollama_qwen3_vl_32b_instruct_q4_K_M
- Failure modes: aggregation_failure, container_affordance_miss
- Evidence quote: Locate drink options (water bottle, potentially others not visible).; Locate snack options (variety of packaged snacks and an apple).; Select a reasonable quantity of both drinks and snacks considering the number of people chatting (assu...
- Why it is a counterexample: primary clean prompt failed under text rereview with 4 model(s).
- Caveat: text-only evidence; still verify image before claims

## 16. task_005 / Weixin Image_20260629231743_399_27.jpg / natural_free_plan

- Models failed: ollama_gemma3_27b_it_q8_0, ollama_minicpm_v4_5_q8_0, ollama_qwen3_vl_30b_a3b_instruct_q4_K_M, ollama_qwen3_vl_32b_instruct_q4_K_M
- Failure modes: aggregation_failure, container_affordance_miss, helper_mention_without_use, visual_uncertainty
- Evidence quote: Locate all used cups and dishes on the table.; Pick up each cup/dish one by one.; Transport each item to the kitchen.; Repeat until all items are moved. The task requires moving multiple objects from one location (the table) to another (...
- Why it is a counterexample: primary clean prompt failed under text rereview with 4 model(s).
- Caveat: needs image verification

## 17. task_007 / Weixin Image_20260629231746_401_27.jpg / natural_free_plan

- Models failed: ollama_gemma3_27b_it_q8_0, ollama_minicpm_v4_5_q8_0, ollama_qwen3_vl_30b_a3b_instruct_q4_K_M, ollama_qwen3_vl_32b_instruct_q4_K_M
- Failure modes: helper_mention_without_use, visual_uncertainty, aggregation_failure, container_affordance_miss, physical_capacity_hallucination
- Evidence quote: Locate and grasp the green striped shirt.; Transport the green striped shirt to the laundry area.; Locate and grasp the blue hoodie.; Transport the blue hoodie to the laundry area.; Locate and grasp the black t-shirt.; Transport the blac...
- Why it is a counterexample: primary clean prompt failed under text rereview with 4 model(s).
- Caveat: needs image verification

## 18. task_007 / Weixin Image_20260629231746_401_27.jpg / efficient_safe_free_plan

- Models failed: ollama_gemma3_27b_it_q8_0, ollama_minicpm_v4_5_q8_0, ollama_qwen3_vl_30b_a3b_instruct_q4_K_M, ollama_qwen3_vl_32b_instruct_q4_K_M
- Failure modes: helper_mention_without_use, visual_uncertainty, aggregation_failure, container_affordance_miss
- Evidence quote: 1. Navigate to the pile of clothes.; 2. Grasp and lift the green striped shirt.; 3. Transport the green striped shirt to the laundry area and deposit it.; 4. Return to the remaining clothes.; 5. Grasp and lift the blue hoodie.; 6. Transp...
- Why it is a counterexample: primary clean prompt failed under text rereview with 4 model(s).
- Caveat: needs image verification

## 19. task_008 / af09e19db8fd93d51875f3e63c5fea96.jpg / natural_free_plan

- Models failed: ollama_gemma3_27b_it_q8_0, ollama_qwen3_5_35b, ollama_qwen3_vl_30b_a3b_instruct_q4_K_M, ollama_qwen3_vl_32b_instruct_q4_K_M
- Failure modes: aggregation_failure, container_affordance_miss, helper_mention_without_use, visual_uncertainty
- Evidence quote: Approach the sofa.; Check for obstacles around the sofa legs.; Reach under the sofa to grasp the remote control.; Withdraw the remote control from under the sofa.; Present the remote control. The task requires navigating to the sofa, ide...
- Why it is a counterexample: primary clean prompt failed under text rereview with 4 model(s).
- Caveat: needs image verification

## 20. task_001 / Weixin Image_20260629231738_395_27.jpg / efficient_safe_free_plan_humanoid_dual_arm

- Models failed: ollama_gemma3_27b_it_q8_0, ollama_minicpm_v4_5_q8_0, ollama_qwen3_vl_30b_a3b_instruct_q4_K_M, ollama_qwen3_vl_32b_instruct_q4_K_M
- Failure modes: aggregation_failure, container_affordance_miss
- Evidence quote: 1. Visually confirm clear path to the bedroom, noting any obstacles.; 2. Grasp two water bottles simultaneously with both hands.; 3. Transport the two water bottles to the bedroom.; 4. Return to the original location.; 5. Repeat steps 2-...
- Why it is a counterexample: primary clean prompt failed under text rereview with 4 model(s).
- Caveat: text-only evidence; still verify image before claims

## 21. task_005 / Weixin Image_20260629231743_399_27.jpg / natural_free_plan_humanoid_dual_arm

- Models failed: ollama_gemma3_27b_it_q8_0, ollama_minicpm_v4_5_q8_0, ollama_qwen3_vl_30b_a3b_instruct_q4_K_M, ollama_qwen3_vl_32b_instruct_q4_K_M
- Failure modes: aggregation_failure, container_affordance_miss, physical_capacity_hallucination, helper_mention_without_use, visual_uncertainty
- Evidence quote: Scan the table to identify all cups and plates.; Pick up one cup/plate with each hand, prioritizing stable grasps.; Transport the items to the kitchen.; Place the items in the designated dirty dish area in the kitchen.; Repeat steps 2-4...
- Why it is a counterexample: primary clean prompt failed under text rereview with 4 model(s).
- Caveat: needs image verification

## 22. task_007 / Weixin Image_20260629231746_401_27.jpg / natural_free_plan_humanoid_dual_arm

- Models failed: ollama_gemma3_27b_it_q8_0, ollama_minicpm_v4_5_q8_0, ollama_qwen3_vl_30b_a3b_instruct_q4_K_M, ollama_qwen3_vl_32b_instruct_q4_K_M
- Failure modes: helper_mention_without_use, visual_uncertainty, aggregation_failure, container_affordance_miss
- Evidence quote: 1. Approach the pile of clothes.; 2. Pick up the green striped shirt with one hand.; 3. Pick up the blue hoodie with the other hand.; 4. Transport both items to the laundry area.; 5. Return to the remaining clothing item.; 6. Pick up the...
- Why it is a counterexample: primary clean prompt failed under text rereview with 4 model(s).
- Caveat: needs image verification

## 23. task_007 / Weixin Image_20260629231746_401_27.jpg / efficient_safe_free_plan_humanoid_dual_arm

- Models failed: ollama_gemma3_27b_it_q8_0, ollama_minicpm_v4_5_q8_0, ollama_qwen3_vl_30b_a3b_instruct_q4_K_M, ollama_qwen3_vl_32b_instruct_q4_K_M
- Failure modes: helper_mention_without_use, visual_uncertainty, aggregation_failure, container_affordance_miss
- Evidence quote: 1. Approach the striped shorts and pick them up with one hand.; 2. Approach the blue hoodie and pick it up with the other hand.; 3. Transport both the striped shorts and blue hoodie to the laundry area.; 4. Return to the original locatio...
- Why it is a counterexample: primary clean prompt failed under text rereview with 4 model(s).
- Caveat: needs image verification

## 24. task_008 / af09e19db8fd93d51875f3e63c5fea96.jpg / natural_free_plan_humanoid_dual_arm

- Models failed: ollama_gemma3_27b_it_q8_0, ollama_minicpm_v4_5_q8_0, ollama_qwen3_vl_30b_a3b_instruct_q4_K_M, ollama_qwen3_vl_32b_instruct_q4_K_M
- Failure modes: aggregation_failure, container_affordance_miss, helper_mention_without_use, visual_uncertainty
- Evidence quote: Check if I can directly reach under the sofa with either arm and hand.; If not, check for obstacles preventing access from the side or front of the sofa.; Reach under the sofa and grasp the remote control with one hand.; Carefully pull t...
- Why it is a counterexample: primary clean prompt failed under text rereview with 4 model(s).
- Caveat: needs image verification

## 25. task_001 / Weixin Image_20260629231738_395_27.jpg / natural_free_plan_quadruped_single_arm

- Models failed: ollama_gemma3_27b_it_q8_0, ollama_minicpm_v4_5_q8_0, ollama_qwen3_vl_30b_a3b_instruct_q4_K_M, ollama_qwen3_vl_32b_instruct_q4_K_M
- Failure modes: aggregation_failure, container_affordance_miss
- Evidence quote: Navigate to the table with the water bottles.; Inspect the arrangement of the water bottles to determine if any can be safely carried as a stable group. If not, plan for individual trips.; Pick up one (or a small, stable group) of the wa...
- Why it is a counterexample: primary clean prompt failed under text rereview with 4 model(s).
- Caveat: text-only evidence; still verify image before claims

## 26. task_002 / Weixin Image_20260629231739_396_27.jpg / efficient_safe_free_plan_quadruped_single_arm

- Models failed: ollama_gemma3_27b_it_q8_0, ollama_minicpm_v4_5_q8_0, ollama_qwen3_vl_30b_a3b_instruct_q4_K_M, ollama_qwen3_vl_32b_instruct_q4_K_M
- Failure modes: aggregation_failure, container_affordance_miss, helper_search_failure
- Evidence quote: 1. Approach the table with the water bottles.; 2. Pick up one water bottle at a time using the gripper.; 3. Navigate to the bedroom, maintaining balance during movement.; 4. Deliver the water bottle to the students.; 5. Repeat steps 2-4...
- Why it is a counterexample: primary clean prompt failed under text rereview with 4 model(s).
- Caveat: text-only evidence; still verify image before claims

## 27. task_004 / Weixin Image_20260629231742_398_27.jpg / natural_free_plan_quadruped_single_arm

- Models failed: ollama_gemma3_27b_it_q8_0, ollama_minicpm_v4_5_q8_0, ollama_qwen3_vl_30b_a3b_instruct_q4_K_M, ollama_qwen3_vl_32b_instruct_q4_K_M
- Failure modes: aggregation_failure, container_affordance_miss
- Evidence quote: Locate the water bottle and apple on the table.; Pick up the water bottle and transport it to the living room.; Return to the table.; Pick up the apple and transport it to the living room.; Return to the table.; Assess the snack packets;...
- Why it is a counterexample: primary clean prompt failed under text rereview with 4 model(s).
- Caveat: text-only evidence; still verify image before claims

## 28. task_004 / Weixin Image_20260629231742_398_27.jpg / efficient_safe_free_plan_quadruped_single_arm

- Models failed: ollama_gemma3_27b_it_q8_0, ollama_minicpm_v4_5_q8_0, ollama_qwen3_vl_30b_a3b_instruct_q4_K_M, ollama_qwen3_vl_32b_instruct_q4_K_M
- Failure modes: aggregation_failure, container_affordance_miss, helper_mention_without_use, visual_uncertainty
- Evidence quote: 1. Approach the table.; 2. Scan the table for suitable items (drinks and individually packaged snacks).; 3. Pick up the water bottle.; 4. Deliver the water bottle to the living room.; 5. Return to the table.; 6. Pick up a stack of snack...
- Why it is a counterexample: primary clean prompt failed under text rereview with 4 model(s).
- Caveat: needs image verification

## 29. task_007 / Weixin Image_20260629231746_401_27.jpg / efficient_safe_free_plan_quadruped_single_arm

- Models failed: ollama_gemma3_27b_it_q8_0, ollama_minicpm_v4_5_q8_0, ollama_qwen3_vl_30b_a3b_instruct_q4_K_M, ollama_qwen3_vl_32b_instruct_q4_K_M
- Failure modes: aggregation_failure, container_affordance_miss, helper_mention_without_use, visual_uncertainty
- Evidence quote: 1. Navigate to the striped shorts and pick them up.; 2. Transport the striped shorts to the laundry area and deposit them.; 3. Navigate to the blue hoodie and pick it up.; 4. Transport the blue hoodie to the laundry area and deposit it.;...
- Why it is a counterexample: primary clean prompt failed under text rereview with 4 model(s).
- Caveat: needs image verification

## 30. task_005 / Weixin Image_20260629231743_399_27.jpg / efficient_safe_free_plan

- Models failed: ollama_gemma3_27b_it_q8_0, ollama_qwen3_vl_30b_a3b_instruct_q4_K_M, ollama_qwen3_vl_32b_instruct_q4_K_M
- Failure modes: aggregation_failure, container_affordance_miss, physical_capacity_hallucination, helper_mention_without_use, visual_uncertainty
- Evidence quote: 1. Scan the table to confirm the locations of all dirty dishes (cups, bowls).; 2. Grasp and lift each dish individually.; 3. Transport all grasped dishes to the kitchen.; 4. Release the dishes in the designated area within the kitchen. M...
- Why it is a counterexample: primary clean prompt failed under text rereview with 3 model(s).
- Caveat: needs image verification

## 31. task_008 / af09e19db8fd93d51875f3e63c5fea96.jpg / efficient_safe_free_plan

- Models failed: ollama_gemma3_27b_it_q8_0, ollama_qwen3_vl_30b_a3b_instruct_q4_K_M, ollama_qwen3_vl_32b_instruct_q4_K_M
- Failure modes: aggregation_failure, container_affordance_miss, helper_mention_without_use, tool_necessity_miss, visual_uncertainty
- Evidence quote: Approach the sofa from a clear angle.; Extend arm/manipulator to reach under the sofa and grasp the remote control.; Retract arm/manipulator with the remote control.; Present the remote control. A single, direct approach with a careful e...
- Why it is a counterexample: primary clean prompt failed under text rereview with 3 model(s).
- Caveat: needs image verification

## 32. task_004 / Weixin Image_20260629231742_398_27.jpg / natural_free_plan_humanoid_dual_arm

- Models failed: ollama_gemma3_27b_it_q8_0, ollama_minicpm_v4_5_q8_0, ollama_qwen3_vl_32b_instruct_q4_K_M
- Failure modes: aggregation_failure, container_affordance_miss
- Evidence quote: Scan the table to identify suitable drink and snack items.; Pick up the water bottle with one hand and the apple with the other.; Transport the water bottle and apple to the location where people are chatting.; Return to the table.; Pick...
- Why it is a counterexample: primary clean prompt failed under text rereview with 3 model(s).
- Caveat: text-only evidence; still verify image before claims

## 33. task_009 / Weixin Image_20260629231751_404_27.jpg / natural_free_plan_humanoid_dual_arm

- Models failed: ollama_gemma3_27b_it_q8_0, ollama_minicpm_v4_5_q8_0, ollama_qwen3_5_35b
- Failure modes: aggregation_failure, container_affordance_miss, wrong_helper_type, helper_mention_without_use, visual_uncertainty
- Evidence quote: Scan the area to confirm the location of all paper balls and identify any obstacles.; Pick up one paper ball with each hand, if possible. Otherwise, pick them up one at a time.; Transport the collected paper balls to the trash can.; Repe...
- Why it is a counterexample: primary clean prompt failed under text rereview with 3 model(s).
- Caveat: needs image verification

## 34. task_005 / Weixin Image_20260629231743_399_27.jpg / natural_free_plan_quadruped_single_arm

- Models failed: ollama_gemma3_27b_it_q8_0, ollama_minicpm_v4_5_q8_0, ollama_qwen3_vl_32b_instruct_q4_K_M
- Failure modes: aggregation_failure, container_affordance_miss, helper_mention_without_use, visual_uncertainty
- Evidence quote: 1. Visually scan the table to identify all used cups and plates.; 2. Approach the first cup/plate, grasp it with the gripper, and ensure a stable hold during lifting.; 3. Navigate to the kitchen while maintaining balance.; 4. Place the c...
- Why it is a counterexample: primary clean prompt failed under text rereview with 3 model(s).
- Caveat: needs image verification

## 35. task_005 / Weixin Image_20260629231743_399_27.jpg / efficient_safe_free_plan_quadruped_single_arm

- Models failed: ollama_gemma3_27b_it_q8_0, ollama_minicpm_v4_5_q8_0, ollama_qwen3_vl_32b_instruct_q4_K_M
- Failure modes: aggregation_failure, container_affordance_miss
- Evidence quote: 1. Approach the table and visually scan for all cups and plates.; 2. Pick up one cup or plate at a time with the gripper, ensuring a stable grasp.; 3. Navigate to the kitchen while maintaining balance.; 4. Place the cup/plate in the desi...
- Why it is a counterexample: primary clean prompt failed under text rereview with 3 model(s).
- Caveat: text-only evidence; still verify image before claims

## 36. task_009 / Weixin Image_20260629231751_404_27.jpg / natural_free_plan_quadruped_single_arm

- Models failed: ollama_gemma3_27b_it_q8_0, ollama_minicpm_v4_5_q8_0, ollama_qwen3_5_35b
- Failure modes: aggregation_failure, container_affordance_miss, helper_mention_without_use, visual_uncertainty
- Evidence quote: 1. Scan the area to identify all crumpled papers and their locations.; 2. Navigate to the first crumpled paper.; 3. Use the mechanical arm and gripper to pick up the crumpled paper.; 4. Navigate to the trash can (visible in the image).;...
- Why it is a counterexample: primary clean prompt failed under text rereview with 3 model(s).
- Caveat: needs image verification

## 37. task_009 / Weixin Image_20260629231751_404_27.jpg / efficient_safe_free_plan_quadruped_single_arm

- Models failed: ollama_gemma3_27b_it_q8_0, ollama_minicpm_v4_5_q8_0, ollama_qwen3_vl_32b_instruct_q4_K_M
- Failure modes: aggregation_failure, container_affordance_miss, helper_mention_without_use, visual_uncertainty, wrong_helper_type
- Evidence quote: 1. Navigate to the first visible crumpled paper object.; 2. Use the mechanical arm and gripper to pick up the crumpled paper.; 3. Navigate to the trash can (visible in the image).; 4. Open the lid of the trash can (if necessary, assess i...
- Why it is a counterexample: primary clean prompt failed under text rereview with 3 model(s).
- Caveat: needs image verification

## 38. task_010 / Weixin Image_20260629231750_403_27.jpg / efficient_safe_free_plan

- Models failed: ollama_minicpm_v4_5_q8_0, ollama_qwen3_vl_30b_a3b_instruct_q4_K_M
- Failure modes: helper_mention_without_use, visual_uncertainty, aggregation_failure, container_affordance_miss
- Evidence quote: 检查餐桌位置和周围环境以确保路径畅通，避免碰撞。; 逐一拾取桌面上的鸡蛋并放入蛋托中，防止掉落或破损。; 拾取其他可移动物品（如盒子），注意轻拿轻放，保持平衡。; 将所有物品安全搬运至餐桌上。 尽量减少往返次数并确保一次完成任务。 避免碰撞和掉落，特别是处理易碎的鸡蛋时要小心。 未明确餐桌的具体位置及周围障碍物情况。 { "task_understanding": "将桌面上的物品（鸡蛋、盒子等）安全地拿到餐桌上。", "plan": [ "检查餐桌位置和周围环境以确保...
- Why it is a counterexample: primary clean prompt failed under text rereview with 2 model(s).
- Caveat: needs image verification

## 39. task_009 / Weixin Image_20260629231751_404_27.jpg / efficient_safe_free_plan_humanoid_dual_arm

- Models failed: ollama_gemma3_27b_it_q8_0, ollama_qwen3_vl_32b_instruct_q4_K_M
- Failure modes: aggregation_failure, container_affordance_miss, wrong_helper_type
- Evidence quote: 1. Visually scan the entire area to identify all pieces of crumpled paper and their approximate locations.; 2. Navigate to the first piece of crumpled paper.; 3. Pick up the crumpled paper with one hand.; 4. Navigate to the trash can (vi...
- Why it is a counterexample: primary clean prompt failed under text rereview with 2 model(s).
- Caveat: text-only evidence; still verify image before claims

## 40. task_010 / Weixin Image_20260629231750_403_27.jpg / natural_free_plan_humanoid_dual_arm

- Models failed: ollama_minicpm_v4_5_q8_0, ollama_qwen3_5_35b
- Failure modes: helper_mention_without_use, visual_uncertainty
- Evidence quote: 检查桌面所有物品的位置和状态，确认哪些是需要搬运的目标。; 使用双手分别抓取鸡蛋和其他小件物品，确保每只手稳定拿住一个物体或稳定的组合。; 将抓取的物品有序放置在餐桌上，避免碰撞或掉落。 尽量减少搬运次数和路径长度，提高效率。 确保每只手拿住的物品稳定，防止滑落；注意鸡蛋易碎，避免碰撞。 桌面物品的具体数量、摆放位置及餐桌的位置信息未明确说明。 { "task_understanding": "将桌面上的物品（包括鸡蛋、盒子等）安全地搬运到餐桌。", "plan": [...
- Why it is a counterexample: primary clean prompt failed under text rereview with 2 model(s).
- Caveat: needs image verification

## 41. task_006 / Weixin Image_20260629231745_400_27.jpg / natural_free_plan_quadruped_single_arm

- Models failed: ollama_gemma3_27b_it_q8_0, ollama_minicpm_v4_5_q8_0
- Failure modes: aggregation_failure, container_affordance_miss, helper_mention_without_use, visual_uncertainty
- Evidence quote: 1. Approach the first object (e.g., the red pen).; 2. Pick up the object with the gripper.; 3. Navigate to the trash can while maintaining balance.; 4. Deposit the object into the trash can.; 5. Repeat steps 1-4 for each remaining object...
- Why it is a counterexample: primary clean prompt failed under text rereview with 2 model(s).
- Caveat: needs image verification

## 42. task_007 / Weixin Image_20260629231746_401_27.jpg / natural_free_plan_quadruped_single_arm

- Models failed: ollama_minicpm_v4_5_q8_0, ollama_qwen3_vl_32b_instruct_q4_K_M
- Failure modes: aggregation_failure, container_affordance_miss
- Evidence quote: 检查椅子下方是否有隐藏的衣物，如果有则先取出并加入收集物中。; 使用机械臂逐一拾取椅子上悬挂或放置的衣物（例如绿色条纹衫、深蓝色T恤等）放入洗衣篮。注意保持平衡和稳定。; 拾取地面上的衣物，并将其放入洗衣篮。确保每次只携带一件，避免夹爪过载导致不稳定。; 将所有收集到的衣物全部移入洗衣篮中，完成任务。 任务目标是将所有衣物收起来并拿到洗衣区。通过分步计划可以系统地完成物品的收集和搬运，同时考虑平衡、稳定性和安全性。 尽量一次性拾取并移动尽可能多的衣物以减少往返次数，但需...
- Why it is a counterexample: primary clean prompt failed under text rereview with 2 model(s).
- Caveat: text-only evidence; still verify image before claims

## 43. task_006 / Weixin Image_20260629231745_400_27.jpg / natural_free_plan

- Models failed: ollama_gemma3_27b_it_q8_0
- Failure modes: aggregation_failure, container_affordance_miss
- Evidence quote: Scan the area to identify all individual objects.; Pick up each object one by one.; Place each object into the trash can.; Verify that no objects remain on the floor. The image shows several small objects scattered on the floor. The task...
- Why it is a counterexample: primary clean prompt failed under text rereview with 1 model(s).
- Caveat: text-only evidence; still verify image before claims

## 44. task_006 / Weixin Image_20260629231745_400_27.jpg / efficient_safe_free_plan

- Models failed: ollama_gemma3_27b_it_q8_0
- Failure modes: aggregation_failure, container_affordance_miss
- Evidence quote: Scan the area for obstacles and identify all target objects (small items).; Prioritize collection based on fragility/size - start with non-fragile, larger items first. Collect items in a clockwise or counterclockwise manner to minimize t...
- Why it is a counterexample: primary clean prompt failed under text rereview with 1 model(s).
- Caveat: text-only evidence; still verify image before claims

## 45. task_009 / Weixin Image_20260629231751_404_27.jpg / natural_free_plan

- Models failed: ollama_gemma3_27b_it_q8_0
- Failure modes: aggregation_failure, container_affordance_miss
- Evidence quote: Scan the area to confirm all debris locations and identify any obstacles.; Navigate to each piece of crumpled paper.; Pick up each piece of crumpled paper.; Navigate to the trash can (visible in the image).; Deposit the crumpled paper in...
- Why it is a counterexample: primary clean prompt failed under text rereview with 1 model(s).
- Caveat: text-only evidence; still verify image before claims

## 46. task_009 / Weixin Image_20260629231751_404_27.jpg / efficient_safe_free_plan

- Models failed: ollama_gemma3_27b_it_q8_0
- Failure modes: aggregation_failure, container_affordance_miss
- Evidence quote: 1. Scan the area for any obstacles or hazards before starting cleaning.; 2. Navigate to the location of the crumpled papers.; 3. Collect all visible crumpled papers and store them in the trash can (located near the toilet).; 4. Re-scan t...
- Why it is a counterexample: primary clean prompt failed under text rereview with 1 model(s).
- Caveat: text-only evidence; still verify image before claims

## 47. task_003 / 372f92c1ce9c87231d199c1102dcf7b4.jpg / efficient_safe_free_plan

- Models failed: ollama_minicpm_v4_5_q8_0
- Failure modes: helper_mention_without_use, visual_uncertainty
- Evidence quote: 识别桌面区域内的所有待收拾物品：左侧报纸、中间笔记本电脑及其配件（如鼠标）、右侧背包以及可能散落的小物件。; 将左侧的报纸和文件叠放整齐，并检查是否还有其他纸张需要收纳，确保不遗漏。; 关闭并整理好笔记本电脑屏幕及周边线缆，确认所有电子设备处于待机或关机状态。 一次性完成桌面物品的识别与整理，避免多次往返于不同区域。 确保笔记本电脑和屏幕在移动过程中不会倾倒或损坏，注意轻拿轻放。 未明确哪些物品是需要携带的，需根据用户指示确认具体打包内容。 { "task_unders...
- Why it is a counterexample: primary clean prompt failed under text rereview with 1 model(s).
- Caveat: needs image verification

## 48. task_010 / Weixin Image_20260629231750_403_27.jpg / natural_free_plan

- Models failed: ollama_qwen3_vl_30b_a3b_instruct_q4_K_M
- Failure modes: helper_mention_without_use, visual_uncertainty
- Evidence quote: 检查周围环境，确认餐桌位置和路径无障碍物。; 逐一拾取鸡蛋，并小心放置在餐桌上。; 将塑料蛋托拿起并放在餐桌上。; 拿起金属碗并移动到餐桌上。; 将遥控器、JBL音箱和纸巾盒依次搬到餐桌上。; 整理桌面上的物品，确保摆放整齐且安全。 为了确保所有物品安全、有序地转移到餐桌上，同时减少不必要的移动次数以提高效率。 优先搬运易碎品（如鸡蛋），减少移动次数以提高效率。 搬运过程中避免碰撞或掉落，特别是鸡蛋和金属碗等易碎物品。 未明确餐桌的具体位置和大小，需根据实际情况调整搬运...
- Why it is a counterexample: primary clean prompt failed under text rereview with 1 model(s).
- Caveat: needs image verification

## 49. task_006 / Weixin Image_20260629231745_400_27.jpg / natural_free_plan_humanoid_dual_arm

- Models failed: ollama_gemma3_27b_it_q8_0
- Failure modes: helper_mention_without_use, visual_uncertainty
- Evidence quote: Scan the area to identify all individual objects needing collection.; Pick up one object at a time with either hand, prioritizing smaller/lighter items first.; Transport the object to the trash can and deposit it inside.; Repeat steps 2-...
- Why it is a counterexample: primary clean prompt failed under text rereview with 1 model(s).
- Caveat: needs image verification

## 50. task_010 / Weixin Image_20260629231750_403_27.jpg / efficient_safe_free_plan_humanoid_dual_arm

- Models failed: ollama_gemma3_27b_it_q8_0
- Failure modes: helper_mention_without_use, visual_uncertainty
- Evidence quote: 1. Scan the area around the objects to confirm no obstructions or fragile items nearby that could be disturbed during transport.; 2. Pick up the cardboard box with both hands and move it to the dining table.; 3. Return to the original lo...
- Why it is a counterexample: primary clean prompt failed under text rereview with 1 model(s).
- Caveat: needs image verification

## 51. task_006 / Weixin Image_20260629231745_400_27.jpg / efficient_safe_free_plan_humanoid_dual_arm

- Models failed: ollama_minicpm_v4_5_q8_0
- Failure modes: -
- Evidence quote: 检查所有可见区域，确认没有遗漏任何物品。; 使用一只手拿起一个物品，并将其放入篮子。如果需要，另一只手可以辅助稳定或拿取其他物品。; 重复上述动作，直到所有物品都被收集到篮子里。 通过先检查区域确保不遗漏，再分批收集并利用双手提高效率。 尽量减少往返次数和移动路径长度，通过同时使用两只手提高效率。 确保每件物品在放入篮子前都稳定抓取，避免掉落。注意笔等细长物体的稳定性。 未明确指定目标位置是否为白色塑料篮子内部还是外部；需要确认所有物品都能被直接拿取（无遮挡、无障碍）。...
- Why it is a counterexample: primary clean prompt failed under text rereview with 1 model(s).
- Caveat: text-only evidence; still verify image before claims

## 52. task_003 / 372f92c1ce9c87231d199c1102dcf7b4.jpg / natural_free_plan_humanoid_dual_arm

- Models failed: ollama_qwen3_5_35b
- Failure modes: helper_mention_without_use, visual_uncertainty
- Evidence quote: 1. 检查桌面状态：确认笔记本电脑、黑色电脑包以及左侧散乱纸张的具体位置。; 2. 腾挪空间与清理杂物：左手将左侧的报纸/文件推至桌边或收纳盒中，右手拿起玻璃水杯移至安全区域（若需带走则放入包内）。; 3. 打包核心物品：合上笔记本电脑屏幕并将其平稳放入黑色电脑包内，确认拉链拉好。 利用双臂协同操作，左手处理非关键杂物（纸张），右手处理易碎品和水杯，最后集中打包电脑，减少重复移动手臂的次数。 笔记本电脑较重且屏幕脆弱，拿取时需保持水平；玻璃水杯需稳固抓取以防破碎；避免在...
- Why it is a counterexample: primary clean prompt failed under text rereview with 1 model(s).
- Caveat: needs image verification

## 53. task_005 / Weixin Image_20260629231743_399_27.jpg / efficient_safe_free_plan_humanoid_dual_arm

- Models failed: ollama_qwen3_vl_32b_instruct_q4_K_M
- Failure modes: aggregation_failure, container_affordance_miss
- Evidence quote: 检查桌面所有餐具，确认需要收回的物品：两个白色瓷碗、一个不锈钢碗、一个小白杯（含勺子）、一个金属保温杯。; 使用左手拿起小白杯和勺子组合，右手同时拿起其中一个白色瓷碗。; 将左手的小白杯放置于右手瓷碗上方形成稳定叠放结构，保持在右手中；左手再拿起不锈钢碗。; 移动至厨房区域，将右手的叠放餐具（小白杯+瓷碗）放入水槽或指定收纳处，然后放下左手的不锈钢碗。; 返回桌面，用左手拿起另一个白色瓷碗，右手拿起金属保温杯。; 再次前往厨房，将剩余两个物品放置于水槽或指定位置。 通过...
- Why it is a counterexample: primary clean prompt failed under text rereview with 1 model(s).
- Caveat: text-only evidence; still verify image before claims

