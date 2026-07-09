# AHD VLM Image Judge Failures

- agg_o0_000001 (aggregate_transport_o0_target_visible_helper_absent): missing_file. Fix: Regenerate this image after confirming the expected output path exists.
- agg_o0_000002 (aggregate_transport_o0_target_visible_helper_absent): missing_file. Fix: Regenerate this image after confirming the expected output path exists.
- container_o1_000001 (container_helper_o1_target_absent): missing_file. Fix: Regenerate this image after confirming the expected output path exists.
- container_o1_000002 (container_helper_o1_target_absent): missing_file. Fix: Regenerate this image after confirming the expected output path exists.
- direct_o0_000001 (direct_is_enough_o0_single_target): missing_file. Fix: Regenerate this image after confirming the expected output path exists.
- wrong_o1_000002 (wrong_helper_o1_target_absent): The image contains a visible water bottle under the desk, which is a target object that should be absent in an O1 scene for this spec. Additionally, a cup (which may be considered a distractor) is present on the table, but it's not clearly a wrong helper as defined; however, the presence of the w.... Fix: Strengthen the negative prompt to strictly exclude any visible water bottles or drink containers in O1 scenes.
