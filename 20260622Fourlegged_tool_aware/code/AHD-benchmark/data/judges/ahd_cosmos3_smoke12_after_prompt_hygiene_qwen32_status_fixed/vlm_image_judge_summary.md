# AHD VLM Image Judge Summary

- total_rows: 12
- generation_failed_count: 5
- missing_or_invalid_image_count: 0
- judge_parse_error_count: 0
- valid_images_judged_count: 7
- semantic_keep_count: 6
- semantic_reject_count: 1
- semantic_keep_rate_among_valid_images: 85.7%
- overall_keep_rate_over_total_rows: 50.0%

## Status By Spec Type

- aggregate_transport_o0_target_visible_helper_absent: total=2, generation_failed=2, missing_or_invalid_image=0, semantic_keep=0, semantic_reject=0, valid_images_judged=0, semantic_keep_rate_valid_only=0.0%
- container_helper_o1_target_absent: total=2, generation_failed=2, missing_or_invalid_image=0, semantic_keep=0, semantic_reject=0, valid_images_judged=0, semantic_keep_rate_valid_only=0.0%
- direct_is_enough_o0_single_target: total=2, generation_failed=1, missing_or_invalid_image=0, semantic_keep=1, semantic_reject=0, valid_images_judged=1, semantic_keep_rate_valid_only=100.0%
- extend_reach_o0_target_under_furniture: total=2, generation_failed=0, missing_or_invalid_image=0, semantic_keep=2, semantic_reject=0, valid_images_judged=2, semantic_keep_rate_valid_only=100.0%
- long_tool_helper_o1_target_absent: total=2, generation_failed=0, missing_or_invalid_image=0, semantic_keep=2, semantic_reject=0, valid_images_judged=2, semantic_keep_rate_valid_only=100.0%
- wrong_helper_o1_target_absent: total=2, generation_failed=0, missing_or_invalid_image=0, semantic_keep=1, semantic_reject=1, valid_images_judged=2, semantic_keep_rate_valid_only=50.0%

## A. Generation Failures

- agg_o0_000001: OutOfMemoryError('CUDA out of memory. Tried to allocate 96.00 MiB. GPU 0 has a total capacity of 47.41 GiB of which 8.38 MiB is free. Process 375949 has 20.04 GiB memory in use. Including non-PyTorch memory, this process has 27.34 GiB memory in use. Of the allocated memory 27.02 GiB is allocated ...
- agg_o0_000002: OutOfMemoryError('CUDA out of memory. Tried to allocate 96.00 MiB. GPU 0 has a total capacity of 47.41 GiB of which 8.38 MiB is free. Process 375949 has 20.04 GiB memory in use. Including non-PyTorch memory, this process has 27.34 GiB memory in use. Of the allocated memory 27.02 GiB is allocated ...
- container_o1_000001: OutOfMemoryError('CUDA out of memory. Tried to allocate 96.00 MiB. GPU 0 has a total capacity of 47.41 GiB of which 8.38 MiB is free. Process 375949 has 20.04 GiB memory in use. Including non-PyTorch memory, this process has 27.34 GiB memory in use. Of the allocated memory 27.02 GiB is allocated ...
- container_o1_000002: OutOfMemoryError('CUDA out of memory. Tried to allocate 96.00 MiB. GPU 0 has a total capacity of 47.41 GiB of which 8.38 MiB is free. Process 375949 has 20.04 GiB memory in use. Including non-PyTorch memory, this process has 27.34 GiB memory in use. Of the allocated memory 27.02 GiB is allocated ...
- direct_o0_000001: OutOfMemoryError('CUDA out of memory. Tried to allocate 96.00 MiB. GPU 0 has a total capacity of 47.41 GiB of which 8.38 MiB is free. Process 375949 has 20.04 GiB memory in use. Including non-PyTorch memory, this process has 27.34 GiB memory in use. Of the allocated memory 27.02 GiB is allocated ...

## B. Missing/Invalid Image Failures

- none

## C. Semantic Rejects

- wrong_o1_000002 (wrong_helper_o1_target_absent): The image contains a visible water bottle under the desk, which is a target object that should be absent in an O1 scene for this spec. Additionally, a cup (which may be considered a distractor) is present on the table, but it's not clearly a wrong helper as defined; however, the presence of the w...; fix: Strengthen the negative prompt to strictly exclude any visible water bottles or drink containers in O1 scenes.

## D. Judge Parse Errors

- none

## Semantic Reject Reasons

- The image contains a visible water bottle under the desk, which is a target object that should be absent in an O1 scene for this spec. Additionally, a cup (which may be considered a distractor) is present on the table, but it's not clearly a wrong helper as defined; however, the presence of the w...: 1

## Semantic One Prompt Fix Frequency

- Strengthen the negative prompt to strictly exclude any visible water bottles or drink containers in O1 scenes.: 1
