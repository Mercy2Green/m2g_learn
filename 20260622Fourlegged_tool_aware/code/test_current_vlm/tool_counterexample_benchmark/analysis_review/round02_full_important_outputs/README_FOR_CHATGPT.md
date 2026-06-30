# README For ChatGPT

This is an automatic text-based rereview handoff. It suggests analysis directions but is not final paper evidence.

## Data Scope
- Rows: 792
- Models: 6 (ollama_gemma3_27b_it_q8_0, ollama_llama3_2_vision_11b_instruct_q8_0, ollama_minicpm_v4_5_q8_0, ollama_qwen3_5_35b, ollama_qwen3_vl_30b_a3b_instruct_q4_K_M, ollama_qwen3_vl_32b_instruct_q4_K_M)
- Tasks: 11 (task_001, task_002, task_003, task_004, task_005, task_006, task_007, task_008, task_009, task_010, task_011)
- Prompt categories: {'generic_clean': 132, 'embodiment_clean': 264, 'diagnostic_probe': 198, 'tool_prior_intervention': 198}
- Rereview labels: {'true_fail': 338, 'true_pass': 261, 'parse_error': 191, 'uncertain': 2}

## Rereview Rubric Summary
- Valid helper use requires a committed action chain, not just helper mention.
- Conditional helper-only plans are not counted as valid helper use.
- Tool-prior prompts are intervention checks, not clean evidence.
- Visual uncertainty remains unresolved until image-level review.

## Top 10 Findings
- parse_failure: 193 text-based labels
- helper_mention_without_use: 173 text-based labels
- aggregation_failure: 143 text-based labels
- container_affordance_miss: 143 text-based labels
- visual_uncertainty: 97 text-based labels
- helper_search_failure: 50 text-based labels
- tool_necessity_miss: 21 text-based labels
- physical_capacity_hallucination: 16 text-based labels
- field_plan_inconsistency: 7 text-based labels
- wrong_helper_type: 5 text-based labels

## Top Clean Counterexample Candidates
- task_001 / Weixin Image_20260629231738_395_27.jpg / ollama_gemma3_27b_it_q8_0 / natural_free_plan: aggregation_failure;container_affordance_miss;physical_capacity_hallucination | Navigate to the table with the water bottles.; Grasp and lift one or more water bottles (depending on carrying capacity).; Navigate to the bedroom where the students are playing cards.; Place the water bottles within reach of the student...
- task_001 / Weixin Image_20260629231738_395_27.jpg / ollama_gemma3_27b_it_q8_0 / efficient_safe_free_plan: aggregation_failure;container_affordance_miss;physical_capacity_hallucination | Navigate to the table with the water bottles.; Grasp and lift all the water bottles.; Navigate to the bedroom where the students are playing cards.; Place the water bottles on a stable surface near the students. The image shows several b...
- task_002 / Weixin Image_20260629231739_396_27.jpg / ollama_gemma3_27b_it_q8_0 / natural_free_plan: aggregation_failure;container_affordance_miss;helper_search_failure;physical_capacity_hallucination | Navigate to the table with the water bottles.; Grasp and lift all the water bottles.; Navigate to the bedroom where the students are playing cards.; Place the water bottles within reach of the students. The image shows several water bott...
- task_002 / Weixin Image_20260629231739_396_27.jpg / ollama_gemma3_27b_it_q8_0 / efficient_safe_free_plan: aggregation_failure;container_affordance_miss;helper_search_failure;physical_capacity_hallucination | Navigate to the table with water bottles; Grasp and lift all water bottles simultaneously or sequentially, ensuring stable carrying.; Navigate to the bedroom where the students are playing cards.; Release the water bottles in a safe loca...
- task_004 / Weixin Image_20260629231742_398_27.jpg / ollama_gemma3_27b_it_q8_0 / natural_free_plan: aggregation_failure;container_affordance_miss | Locate drink options (water bottle, potentially others not visible).; Locate snack options (variety of packaged snacks and an apple).; Select a reasonable quantity of both drinks and snacks considering the number of people chatting (assu...
- task_004 / Weixin Image_20260629231742_398_27.jpg / ollama_gemma3_27b_it_q8_0 / efficient_safe_free_plan: helper_mention_without_use;visual_uncertainty | Scan nearby area for obstacles before moving.; Locate and grasp a water bottle and an apple.; Navigate to the living room while carrying both items.; Place the water bottle and apple near the people chatting. Prioritizing a single trip w...
- task_005 / Weixin Image_20260629231743_399_27.jpg / ollama_gemma3_27b_it_q8_0 / natural_free_plan: aggregation_failure;container_affordance_miss | Locate all used cups and dishes on the table.; Pick up each cup/dish one by one.; Transport each item to the kitchen.; Repeat until all items are moved. The task requires moving multiple objects from one location (the table) to another (...
- task_005 / Weixin Image_20260629231743_399_27.jpg / ollama_gemma3_27b_it_q8_0 / efficient_safe_free_plan: aggregation_failure;container_affordance_miss | 1. Scan the table to confirm the locations of all dirty dishes (cups, bowls).; 2. Grasp and lift each dish individually.; 3. Transport all grasped dishes to the kitchen.; 4. Release the dishes in the designated area within the kitchen. M...
- task_006 / Weixin Image_20260629231745_400_27.jpg / ollama_gemma3_27b_it_q8_0 / natural_free_plan: aggregation_failure;container_affordance_miss | Scan the area to identify all individual objects.; Pick up each object one by one.; Place each object into the trash can.; Verify that no objects remain on the floor. The image shows several small objects scattered on the floor. The task...
- task_006 / Weixin Image_20260629231745_400_27.jpg / ollama_gemma3_27b_it_q8_0 / efficient_safe_free_plan: aggregation_failure;container_affordance_miss | Scan the area for obstacles and identify all target objects (small items).; Prioritize collection based on fragility/size - start with non-fragile, larger items first. Collect items in a clockwise or counterclockwise manner to minimize t...

## Top Prompted Improvement Cases
- task_007 / Weixin Image_20260629231746_401_27.jpg / ollama_gemma3_27b_it_q8_0: natural_free_plan fail -> tool_prior_free_plan pass
- task_008 / af09e19db8fd93d51875f3e63c5fea96.jpg / ollama_gemma3_27b_it_q8_0: natural_free_plan fail -> tool_prior_free_plan pass
- task_005 / Weixin Image_20260629231743_399_27.jpg / ollama_minicpm_v4_5_q8_0: natural_free_plan fail -> tool_prior_free_plan pass
- task_001 / Weixin Image_20260629231738_395_27.jpg / ollama_qwen3_vl_32b_instruct_q4_K_M: natural_free_plan fail -> tool_prior_free_plan pass
- task_008 / af09e19db8fd93d51875f3e63c5fea96.jpg / ollama_qwen3_vl_32b_instruct_q4_K_M: natural_free_plan fail -> tool_prior_free_plan pass
- task_006 / Weixin Image_20260629231745_400_27.jpg / ollama_gemma3_27b_it_q8_0: natural_free_plan_humanoid_dual_arm fail -> tool_prior_free_plan_humanoid_dual_arm pass
- task_008 / af09e19db8fd93d51875f3e63c5fea96.jpg / ollama_gemma3_27b_it_q8_0: natural_free_plan_humanoid_dual_arm fail -> tool_prior_free_plan_humanoid_dual_arm pass
- task_005 / Weixin Image_20260629231743_399_27.jpg / ollama_minicpm_v4_5_q8_0: natural_free_plan_humanoid_dual_arm fail -> tool_prior_free_plan_humanoid_dual_arm pass
- task_009 / Weixin Image_20260629231751_404_27.jpg / ollama_minicpm_v4_5_q8_0: natural_free_plan_humanoid_dual_arm fail -> tool_prior_free_plan_humanoid_dual_arm pass
- task_003 / 372f92c1ce9c87231d199c1102dcf7b4.jpg / ollama_qwen3_5_35b: natural_free_plan_humanoid_dual_arm fail -> tool_prior_free_plan_humanoid_dual_arm pass

## Top Robust Failures Across Clean/Tool-Prior
- task_001 / Weixin Image_20260629231738_395_27.jpg / ollama_gemma3_27b_it_q8_0: clean and tool-prior both true_fail
- task_002 / Weixin Image_20260629231739_396_27.jpg / ollama_gemma3_27b_it_q8_0: clean and tool-prior both true_fail
- task_004 / Weixin Image_20260629231742_398_27.jpg / ollama_gemma3_27b_it_q8_0: clean and tool-prior both true_fail
- task_005 / Weixin Image_20260629231743_399_27.jpg / ollama_gemma3_27b_it_q8_0: clean and tool-prior both true_fail
- task_006 / Weixin Image_20260629231745_400_27.jpg / ollama_gemma3_27b_it_q8_0: clean and tool-prior both true_fail
- task_009 / Weixin Image_20260629231751_404_27.jpg / ollama_gemma3_27b_it_q8_0: clean and tool-prior both true_fail
- task_001 / Weixin Image_20260629231738_395_27.jpg / ollama_minicpm_v4_5_q8_0: clean and tool-prior both true_fail
- task_002 / Weixin Image_20260629231739_396_27.jpg / ollama_minicpm_v4_5_q8_0: clean and tool-prior both true_fail
- task_004 / Weixin Image_20260629231742_398_27.jpg / ollama_minicpm_v4_5_q8_0: clean and tool-prior both true_fail
- task_007 / Weixin Image_20260629231746_401_27.jpg / ollama_minicpm_v4_5_q8_0: clean and tool-prior both true_fail

## Main Uncertainty Sources
- Image visibility of helpers/targets was not checked.
- Parse-recoverable outputs need manual interpretation.
- Some helper mentions may be background or conditional rather than committed use.

## Generated Files
- `aggregate_findings.md`: aggregate text-rereview metrics.
- `task_family_summary.csv`: per-task metrics.
- `model_prompt_matrix.csv`: per-model/prompt matrix.
- `prompt_intervention_delta.md`: clean vs tool-prior comparisons.
- `counterexample_candidates_ranked.md`: ranked clean failure candidates.

## Warning
Automatic text rereview is not final paper evidence. Selected claims require image-level human review.
