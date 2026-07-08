# Scene Spec Schema

One JSONL row describes one image spec, not a paired O0/O1 sample.

## Common Fields

- `spec_id`: stable unique id.
- `version`: `ahd_v01`.
- `view_stage`: `O0` or `O1`.
- `task_family`: task family or `helper_view` for O1 helper-only images.
- `spec_type`: concrete generation type.
- `seed`: deterministic seed/id for reproducibility.
- `language`: English and Chinese task wording.
- `robot_context`: quadruped single-arm context.
- `visual_scene`: visible content, forbidden visible objects, camera, lighting, distractors.
- `generation`: generation status metadata; stage 0 always remains `not_generated`.
- `quality`: check status.

## O0 Gold

O0 specs include `gold`:

- `stage`: `search_trigger` or `direct_action`.
- `mode`: `search_helper` or `direct`.
- `needed_helper_function`: functional target memory label.
- `target_memory`: object, count, location, and task-relevant property.
- `direct_fallback_allowed`: boolean.

## O1 Gold

O1 specs include:

- `helper_candidates_gold`: visible object and its generic helper function.
- `pairing_role`: O0 spec types this O1 image can later pair with.

O1 specs intentionally do not include final helper-grounding gold. Final correctness depends on which O0 memory the O1 image is paired with.
