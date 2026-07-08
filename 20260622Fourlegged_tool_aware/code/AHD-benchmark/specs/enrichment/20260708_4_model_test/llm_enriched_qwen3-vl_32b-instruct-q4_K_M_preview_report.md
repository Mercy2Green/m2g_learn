# LLM Enrichment Check Report

- Input file: `specs/enrichment/llm_enriched_qwen3-vl_32b-instruct-q4_K_M_preview.jsonl`
- Total rows: 20
- JSON parse failures: 0
- Schema failures: 0
- Leakage failures: 1
- Average prompt length: 477.2

## Note Summary

- All five drink cans must be visible and placed on the low table.: 1
- All four drink cans must be clearly visible on the wooden desk.: 1
- All six sports drink bottles are visible in the initial view.: 1
- All six sports drink bottles must be transported to the bedroom.: 1
- All six sports drink bottles must be visible and clearly distinguishable on the kitchen counter.: 1
- All three sports drink bottles are visible on the shelf edge in the initial view.: 1
- Avoid any visual elements that could imply human interaction or containment structures.: 1
- Distractors are present but not to be interacted with.: 2
- Distractors like phone charger and book should appear naturally in the environment without obstructing target visibility.: 1
- Distractors must be present but not interfere with target visibility.: 1
- Distractors should be present but not interfere with task focus.: 1
- Distractors such as phone charger, small towel, cloth, and cup are allowed but not to be interacted with.: 1
- Efficiency requires high-level planning from partial observations.: 1
- Efficiency requires prioritizing direct paths and minimizing redundant movements.: 1
- Efficiency requires selecting high-level behavior based on partial observations.: 1
- Ensure all 3 drink cans are clearly visible and placed on the wooden desk.: 1
- Ensure all 3 sports drink bottles are clearly visible and placed on the shelf edge.: 1
- Ensure all four water bottles are clearly visible and distinguishable.: 1
- Exclude all forbidden objects including containers and human elements.: 1
- Exclude any containers or human elements.: 1
- Maintain even overhead lighting and tile floor as key environmental features.: 1
- No containers or assistance from other agents are allowed.: 1
- No containers or assistive tools are allowed for carrying multiple items at once.: 1
- No containers or assistive tools may appear in the scene.: 2
- Only the five sports drink bottles are target objects; all others are distractors or forbidden items.: 1
- Preserve all 4 visible water bottles and tile floor as required.: 1
- Preserve all 5 visible sports drink bottles and carpeted floor.: 1
- Robot is quadruped_single_arm and can grasp only one object at a time.: 1
- Robot's first-person view must be maintained for consistency.: 1
- Scene is captured from a quadruped single-arm robot's first-person view with even overhead lighting.: 1
- Scene must include exactly six visible drink cans on a shelf edge.: 1
- The robot can grasp only one object at a time.: 1
- The robot must grasp one object at a time.: 1
- The robot must operate under partial observation and choose efficient high-level behavior.: 2
- The robot's first-person view should imply readiness to grasp one object at a time.: 1
- The robot's first-person view should show only the living room environment with no occlusions from other objects.: 1
- The scene must be rendered from a low quadruped camera perspective.: 1
- The scene must be rendered from a robot's first-person perspective.: 1
- Use natural task wording with visual context.: 1
- Use natural task wording without labels or inference.: 1
- leakage_error: 1

## Examples

- agg_o0_000018: notes contains forbidden label term: direct
