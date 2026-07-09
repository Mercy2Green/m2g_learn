# VLM Image Judge

This local judge triages generated Cosmos3 images for AHD-Benchmark image-pool construction.
It is an image-quality and AHD-condition checker, not ground truth.

Default judge:

```text
qwen3-vl:32b-instruct-q4_K_M
```

The judge uses local Ollama only. It should not modify labels, gold logic, prompts, or generated images.
For rejected images, it suggests exactly one prompt/spec adjustment in `one_prompt_fix`.

Judge rows use `image_judge_status` to separate engineering failures from semantic image-quality decisions:

- `generation_failed`: Cosmos3 did not produce a successful row. This is not a semantic reject.
- `missing_or_invalid_image`: the final image path is missing or unreadable. This is not a prompt-quality failure.
- `judge_parse_error`: the local VLM did not return valid JSON.
- `semantic_keep`: a valid image was judged usable for the AHD condition.
- `semantic_reject`: a valid image was judged unusable for the AHD condition.

Prompt-fix frequencies should be aggregated only from `semantic_reject` rows. Semantic keep rate should be computed only over valid images actually judged by the VLM.

Run the judge on smoke12:

```bash
python scripts/11_vlm_judge_generated_images.py \
  --results data/runs/ahd_cosmos3_smoke12_results.jsonl \
  --manifest prompts/manifests/cosmos3_smoke12_manifest.jsonl \
  --output_dir data/judges/ahd_cosmos3_smoke12_qwen32 \
  --judge_model qwen3-vl:32b-instruct-q4_K_M \
  --overwrite \
  --progress_every 1

python scripts/12_summarize_vlm_image_judge.py \
  --input_dir data/judges/ahd_cosmos3_smoke12_qwen32
```

Accepted examples still need human audit before inclusion in test or counterfactual subsets.
Do not scale to `mini36` or larger until the VLM judge and human audit show that generated images satisfy AHD O0/O1 semantics.
