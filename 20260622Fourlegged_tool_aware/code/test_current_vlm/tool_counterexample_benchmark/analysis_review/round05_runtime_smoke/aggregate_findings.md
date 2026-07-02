# Aggregate Findings

Text-based rereview summary. This is not final paper evidence.

Warnings:
- This is text-based rereview; image-visible helper verification is not performed.
- Strong decomposition prompt may have label noise; see `label_inconsistency_audit.md` when available.
- Parse failures are separate from planning failures.

## Context usage warnings

- High risk rows: 0
- Medium risk rows: 0
- Unknown risk rows: 0
- Rows with negative prompt+generation headroom: 0

### Highest context usage ratio top 10

| Task | Model | Prompt | Usage ratio | Prompt eval | Num ctx | Headroom after prompt+generation | Risk |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- |
| task_002 | ollama_qwen3_vl_32b_instruct_q4_K_M | search_explicit_strong_decomposition_free_plan | 0.321289 | 2632 | 8192 | 4024 | low |

### Prompt eval count by model

| Name | Rows with prompt eval | Avg prompt eval | Max prompt eval |
| --- | ---: | ---: | ---: |
| ollama_qwen3_vl_32b_instruct_q4_K_M | 1 | 2632.0 | 2632 |

### Prompt eval count by prompt

| Name | Rows with prompt eval | Avg prompt eval | Max prompt eval |
| --- | ---: | ---: | ---: |
| search_explicit_strong_decomposition_free_plan | 1 | 2632.0 | 2632 |

## By prompt category

| Name | Rows | Pass | Fail | Uncertain | Parse | Skipped | Fail rate | Helper-chain rate | Visual checks | Top failure modes |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| search_explicit_strong_decomposition_intervention | 1 | 1 | 0 | 0 | 0 | 0 | 0.0 | 1.0 | 0 | - |

## By prompt ID

| Name | Rows | Pass | Fail | Uncertain | Parse | Skipped | Fail rate | Helper-chain rate | Visual checks | Top failure modes |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| search_explicit_strong_decomposition_free_plan | 1 | 1 | 0 | 0 | 0 | 0 | 0.0 | 1.0 | 0 | - |

## By model

| Name | Rows | Pass | Fail | Uncertain | Parse | Skipped | Fail rate | Helper-chain rate | Visual checks | Top failure modes |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| ollama_qwen3_vl_32b_instruct_q4_K_M | 1 | 1 | 0 | 0 | 0 | 0 | 0.0 | 1.0 | 0 | - |

## By task

| Name | Rows | Pass | Fail | Uncertain | Parse | Skipped | Fail rate | Helper-chain rate | Visual checks | Top failure modes |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| task_002 | 1 | 1 | 0 | 0 | 0 | 0 | 0.0 | 1.0 | 0 | - |

## By embodiment

| Name | Rows | Pass | Fail | Uncertain | Parse | Skipped | Fail rate | Helper-chain rate | Visual checks | Top failure modes |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| generic | 1 | 1 | 0 | 0 | 0 | 0 | 0.0 | 1.0 | 0 | - |

