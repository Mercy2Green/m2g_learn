# AHD VLM Image Judge Summary

- total: 12
- keep_count: 6
- reject_count: 6
- keep_rate: 50.0%

## Keep/Reject By Spec Type

- aggregate_transport_o0_target_visible_helper_absent: keep=0, reject=2, total=2
- container_helper_o1_target_absent: keep=0, reject=2, total=2
- direct_is_enough_o0_single_target: keep=1, reject=1, total=2
- extend_reach_o0_target_under_furniture: keep=2, reject=0, total=2
- long_tool_helper_o1_target_absent: keep=2, reject=0, total=2
- wrong_helper_o1_target_absent: keep=1, reject=1, total=2

## Reject Reasons

- missing_file: 5
- The image contains a visible water bottle under the desk, which is a target object that should be absent in an O1 scene for this spec. Additionally, a cup (which may be considered a distractor) is present on the table, but it's not clearly a wrong helper as defined; however, the presence of the w...: 1

## One Prompt Fix Frequency

- Regenerate this image after confirming the expected output path exists.: 5
- Strengthen the negative prompt to strictly exclude any visible water bottles or drink containers in O1 scenes.: 1

## Rejected Spec IDs

- agg_o0_000001 (aggregate_transport_o0_target_visible_helper_absent): missing_file; fix: Regenerate this image after confirming the expected output path exists.
- agg_o0_000002 (aggregate_transport_o0_target_visible_helper_absent): missing_file; fix: Regenerate this image after confirming the expected output path exists.
- container_o1_000001 (container_helper_o1_target_absent): missing_file; fix: Regenerate this image after confirming the expected output path exists.
- container_o1_000002 (container_helper_o1_target_absent): missing_file; fix: Regenerate this image after confirming the expected output path exists.
- direct_o0_000001 (direct_is_enough_o0_single_target): missing_file; fix: Regenerate this image after confirming the expected output path exists.
- wrong_o1_000002 (wrong_helper_o1_target_absent): The image contains a visible water bottle under the desk, which is a target object that should be absent in an O1 scene for this spec. Additionally, a cup (which may be considered a distractor) is present on the table, but it's not clearly a wrong helper as defined; however, the presence of the w...; fix: Strengthen the negative prompt to strictly exclude any visible water bottles or drink containers in O1 scenes.

## Judge Parse Errors

- none
