# Data Generation Plan

Stage 0 generates 2,000 raw scene spec candidates:

- O0 total: 1,000
- O1 total: 1,000

O0 distribution:

- `aggregate_transport_o0_target_visible_helper_absent`: 400
- `extend_reach_o0_target_under_furniture`: 400
- `direct_is_enough_o0_single_target`: 200

O1 distribution:

- `container_helper_o1_target_absent`: 350
- `long_tool_helper_o1_target_absent`: 350
- `wrong_helper_o1_target_absent`: 300

First image generation subset target:

- Total: 700 image specs.
- O0: 150 aggregate, 150 extend reach, 80 direct.
- O1: 120 container helper, 120 long tool helper, 80 wrong helper.

Later stages should run image generation and filtering only after schema, balance, leakage, and prompt checks pass.
