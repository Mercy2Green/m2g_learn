# VLM Judge Aggregate Findings

Image-aware local VLM judge summary. This is still not final paper evidence.

## Overall

| Name | Rows | Pass | Fail | Uncertain | Tested parse | Judge parse | Image used | Image missing | Visual check | Fail rate | Helper-chain rate | Top failure modes |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| overall | 5 | 0 | 5 | 0 | 0 | 0 | 5 | 0 | 0 | 1.0 | 0.0 | Plan involves carrying each bottle individually, which violates the requirement to use a helper object for aggregation and transport.:1; No commitment to using any visible container (e.g., orange bag) as a helper despite its suitability.:1; Direct hand carrying of bottles without using a helper object (bag, tray, box, basket) as required by task_001.:1; Plan does not mention or use any non-target container to aggregate and transport the water bottles.:1; Direct hand carrying of bottles one by one without using a helper object (bag, tray, box, basket) as required for task_001.:1; Plan does not mention or commit to using any visible non-target container to aggregate and transport the water bottles.:1 |

## By task

| Name | Rows | Pass | Fail | Uncertain | Tested parse | Judge parse | Image used | Image missing | Visual check | Fail rate | Helper-chain rate | Top failure modes |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| task_001 | 3 | 0 | 3 | 0 | 0 | 0 | 3 | 0 | 0 | 1.0 | 0.0 | Plan involves carrying each bottle individually, which violates the requirement to use a helper object for aggregation and transport.:1; No commitment to using any visible container (e.g., orange bag) as a helper despite its suitability.:1; Direct hand carrying of bottles without using a helper object (bag, tray, box, basket) as required by task_001.:1; Plan does not mention or use any non-target container to aggregate and transport the water bottles.:1; Direct hand carrying of bottles one by one without using a helper object (bag, tray, box, basket) as required for task_001.:1; Plan does not mention or commit to using any visible non-target container to aggregate and transport the water bottles.:1 |
| task_002 | 2 | 0 | 2 | 0 | 0 | 0 | 2 | 0 | 0 | 1.0 | 0.0 | Plan does not search for or use any helper container as required by task; instead, it proposes direct hand-carrying of bottles one at a time.:1; No mention of searching for tray/bag/box/basket/container despite none being visible in the image.:1; Direct operation (hand-carrying) is invalid when helper is explicitly required and not available.:1; Direct hand carrying of bottles without using a helper container:1; No search for or use of tray/bag/box/basket as required by task:1; Plan does not mention any helper object, even conditionally:1 |

## By model

| Name | Rows | Pass | Fail | Uncertain | Tested parse | Judge parse | Image used | Image missing | Visual check | Fail rate | Helper-chain rate | Top failure modes |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| ollama_gemma3_27b_it_q8_0 | 5 | 0 | 5 | 0 | 0 | 0 | 5 | 0 | 0 | 1.0 | 0.0 | Plan involves carrying each bottle individually, which violates the requirement to use a helper object for aggregation and transport.:1; No commitment to using any visible container (e.g., orange bag) as a helper despite its suitability.:1; Direct hand carrying of bottles without using a helper object (bag, tray, box, basket) as required by task_001.:1; Plan does not mention or use any non-target container to aggregate and transport the water bottles.:1; Direct hand carrying of bottles one by one without using a helper object (bag, tray, box, basket) as required for task_001.:1; Plan does not mention or commit to using any visible non-target container to aggregate and transport the water bottles.:1 |

## By prompt

| Name | Rows | Pass | Fail | Uncertain | Tested parse | Judge parse | Image used | Image missing | Visual check | Fail rate | Helper-chain rate | Top failure modes |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| strong_decomposition_free_plan | 2 | 0 | 2 | 0 | 0 | 0 | 2 | 0 | 0 | 1.0 | 0.0 | Plan involves carrying each bottle individually, which violates the requirement to use a helper object for aggregation and transport.:1; No commitment to using any visible container (e.g., orange bag) as a helper despite its suitability.:1; Plan does not search for or use any helper container as required by task; instead, it proposes direct hand-carrying of bottles one at a time.:1; No mention of searching for tray/bag/box/basket/container despite none being visible in the image.:1; Direct operation (hand-carrying) is invalid when helper is explicitly required and not available.:1 |
| strong_decomposition_free_plan_humanoid_dual_arm | 2 | 0 | 2 | 0 | 0 | 0 | 2 | 0 | 0 | 1.0 | 0.0 | Direct hand carrying of bottles without using a helper object (bag, tray, box, basket) as required by task_001.:1; Plan does not mention or use any non-target container to aggregate and transport the water bottles.:1; Direct hand carrying of bottles without using a helper container:1; No search for or use of tray/bag/box/basket as required by task:1; Plan does not mention any helper object, even conditionally:1 |
| strong_decomposition_free_plan_quadruped_single_arm | 1 | 0 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 1.0 | 0.0 | Direct hand carrying of bottles one by one without using a helper object (bag, tray, box, basket) as required for task_001.:1; Plan does not mention or commit to using any visible non-target container to aggregate and transport the water bottles.:1 |

## By task family

| Name | Rows | Pass | Fail | Uncertain | Tested parse | Judge parse | Image used | Image missing | Visual check | Fail rate | Helper-chain rate | Top failure modes |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| aggregation_transport | 3 | 0 | 3 | 0 | 0 | 0 | 3 | 0 | 0 | 1.0 | 0.0 | Plan involves carrying each bottle individually, which violates the requirement to use a helper object for aggregation and transport.:1; No commitment to using any visible container (e.g., orange bag) as a helper despite its suitability.:1; Direct hand carrying of bottles without using a helper object (bag, tray, box, basket) as required by task_001.:1; Plan does not mention or use any non-target container to aggregate and transport the water bottles.:1; Direct hand carrying of bottles one by one without using a helper object (bag, tray, box, basket) as required for task_001.:1; Plan does not mention or commit to using any visible non-target container to aggregate and transport the water bottles.:1 |
| helper_search | 2 | 0 | 2 | 0 | 0 | 0 | 2 | 0 | 0 | 1.0 | 0.0 | Plan does not search for or use any helper container as required by task; instead, it proposes direct hand-carrying of bottles one at a time.:1; No mention of searching for tray/bag/box/basket/container despite none being visible in the image.:1; Direct operation (hand-carrying) is invalid when helper is explicitly required and not available.:1; Direct hand carrying of bottles without using a helper container:1; No search for or use of tray/bag/box/basket as required by task:1; Plan does not mention any helper object, even conditionally:1 |
