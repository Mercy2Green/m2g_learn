# AHD VLM Image Judge Summary

- total_rows: 36
- generation_failed_count: 0
- missing_or_invalid_image_count: 0
- judge_parse_error_count: 0
- valid_images_judged_count: 36
- semantic_keep_count: 31
- semantic_reject_count: 5
- semantic_keep_rate_among_valid_images: 86.1%
- overall_keep_rate_over_total_rows: 86.1%

## Status By Spec Type

- aggregate_transport_o0_target_visible_helper_absent: total=6, generation_failed=0, missing_or_invalid_image=0, semantic_keep=6, semantic_reject=0, valid_images_judged=6, semantic_keep_rate_valid_only=100.0%
- container_helper_o1_target_absent: total=6, generation_failed=0, missing_or_invalid_image=0, semantic_keep=5, semantic_reject=1, valid_images_judged=6, semantic_keep_rate_valid_only=83.3%
- direct_is_enough_o0_single_target: total=6, generation_failed=0, missing_or_invalid_image=0, semantic_keep=4, semantic_reject=2, valid_images_judged=6, semantic_keep_rate_valid_only=66.7%
- extend_reach_o0_target_under_furniture: total=6, generation_failed=0, missing_or_invalid_image=0, semantic_keep=6, semantic_reject=0, valid_images_judged=6, semantic_keep_rate_valid_only=100.0%
- long_tool_helper_o1_target_absent: total=6, generation_failed=0, missing_or_invalid_image=0, semantic_keep=6, semantic_reject=0, valid_images_judged=6, semantic_keep_rate_valid_only=100.0%
- wrong_helper_o1_target_absent: total=6, generation_failed=0, missing_or_invalid_image=0, semantic_keep=4, semantic_reject=2, valid_images_judged=6, semantic_keep_rate_valid_only=66.7%

## A. Generation Failures

- none

## B. Missing/Invalid Image Failures

- none

## C. Semantic Rejects

- container_o1_000003 (container_helper_o1_target_absent): The image contains a visible mug and other objects (e.g., keys, possibly a remote) that are not allowed as target distractors; additionally, the tray is present but not salient enough to be considered a container helper in isolation without context. The original targets (bottles/cans/remote/small...; fix: Strengthen the negative prompt to exclude mugs, keys, remotes, and any small personal items; ensure only a salient container-like helper (e.g., tray, basket, box) is visible without any target or distractor objects.
- direct_o0_000001 (direct_is_enough_o0_single_target): A basket with wheels is visible in the scene, which violates the requirement for helper absence and constitutes forbidden object leakage.; fix: Strengthen the negative prompt to exclude baskets, trays, boxes, bags, brooms, sticks, rods, and hangers.
- direct_o0_000006 (direct_is_enough_o0_single_target): The target drink (water bottle) is not visible on the floor as required; instead, it is placed on a desk surface, making it non-reachable and inconsistent with the O0 condition of a single reachable target bottle.; fix: Place the water bottle directly on the carpeted floor in a reachable position, away from furniture.
- wrong_o1_000002 (wrong_helper_o1_target_absent): The image contains a visible water bottle under the desk, which is a target object that should be absent in an O1 scene for 'wrong_helper_o1_target_absent'. Additionally, a cup (a distractor) is present on the table, but it is not clearly salient as the intended wrong helper. The presence of the ...; fix: Strengthen the negative prompt to explicitly exclude any visible bottles or containers under furniture, ensuring only a non-target distractor like a cup remains salient.
- wrong_o1_000003 (wrong_helper_o1_target_absent): The image does not contain any visible wrong distractor object (e.g., book, cup, cloth, pillow, shoe) as required for O1 in a 'wrong_helper_o1_target_absent' scenario. The scene shows a bedroom with a bed, TV, and window — no task-relevant or irrelevant small objects are present to serve as a dis...; fix: Include a clearly visible wrong distractor object such as a pillow, book, or cup in the foreground or near the floor to satisfy the O1 condition for a wrong helper.

## D. Judge Parse Errors

- none

## Semantic Reject Reasons

- The image contains a visible mug and other objects (e.g., keys, possibly a remote) that are not allowed as target distractors; additionally, the tray is present but not salient enough to be considered a container helper in isolation without context. The original targets (bottles/cans/remote/small...: 1
- A basket with wheels is visible in the scene, which violates the requirement for helper absence and constitutes forbidden object leakage.: 1
- The target drink (water bottle) is not visible on the floor as required; instead, it is placed on a desk surface, making it non-reachable and inconsistent with the O0 condition of a single reachable target bottle.: 1
- The image contains a visible water bottle under the desk, which is a target object that should be absent in an O1 scene for 'wrong_helper_o1_target_absent'. Additionally, a cup (a distractor) is present on the table, but it is not clearly salient as the intended wrong helper. The presence of the ...: 1
- The image does not contain any visible wrong distractor object (e.g., book, cup, cloth, pillow, shoe) as required for O1 in a 'wrong_helper_o1_target_absent' scenario. The scene shows a bedroom with a bed, TV, and window — no task-relevant or irrelevant small objects are present to serve as a dis...: 1

## Semantic One Prompt Fix Frequency

- Strengthen the negative prompt to exclude mugs, keys, remotes, and any small personal items; ensure only a salient container-like helper (e.g., tray, basket, box) is visible without any target or distractor objects.: 1
- Strengthen the negative prompt to exclude baskets, trays, boxes, bags, brooms, sticks, rods, and hangers.: 1
- Place the water bottle directly on the carpeted floor in a reachable position, away from furniture.: 1
- Strengthen the negative prompt to explicitly exclude any visible bottles or containers under furniture, ensuring only a non-target distractor like a cup remains salient.: 1
- Include a clearly visible wrong distractor object such as a pillow, book, or cup in the foreground or near the floor to satisfy the O1 condition for a wrong helper.: 1
