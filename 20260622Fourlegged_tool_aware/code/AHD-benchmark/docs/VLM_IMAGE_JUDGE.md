# VLM Image Judge

This local judge triages generated Cosmos3 images for AHD-Benchmark image-pool construction.
It is an image-quality and AHD-condition checker, not ground truth.

Default judge:

```text
qwen3-vl:32b-instruct-q4_K_M
```

The judge uses local Ollama only. It should not modify labels, gold logic, prompts, or generated images.
For rejected images, it suggests exactly one prompt/spec adjustment in `one_prompt_fix`.

The judge is image-level triage, not pair construction. It does not delete raw generated images, does not delete O0/O1 together as a pair, and does not decide final pair validity. Pair filtering belongs to the later paired dataset export stage. This matters because one O1 image may later be reused with multiple O0 memories, especially for same-O1-different-O0 variants.

Judge rows use `image_judge_status` to separate engineering failures from semantic image-quality decisions:

- `generation_failed`: Cosmos3 did not produce a successful row. This is not a semantic reject.
- `missing_or_invalid_image`: the final image path is missing or unreadable. This is not a prompt-quality failure.
- `judge_parse_error`: the local VLM did not return valid JSON.
- `semantic_keep`: a valid image was judged usable for the AHD condition.
- `semantic_reject`: a valid image was judged unusable for the AHD condition.

Prompt-fix frequencies should be aggregated only from `semantic_reject` rows. Semantic keep rate should be computed only over valid images actually judged by the VLM.

After judging, materialize accepted candidates into a curated pool. The curated pool copies or symlinks only `semantic_keep` images:

```text
data/generated_runs/<run_name>/ = raw run outputs, including rejects
data/curated_pools/<pool_name>/ = semantic_keep image pool
data/paired_datasets/ = later paired exports
```

`data/images/` is no longer the canonical generated-image location. Historical judge inputs may still reference it through old result files, but new curated candidates should come from `data/curated_pools/`.

Run the judge on smoke12:

```bash
python scripts/11_vlm_judge_generated_images.py \
  --results data/generated_runs/ahd_cosmos3_smoke12/results.jsonl \
  --manifest prompts/manifests/cosmos3_smoke12_manifest.jsonl \
  --output_dir data/judges/ahd_cosmos3_smoke12_qwen32 \
  --judge_model qwen3-vl:32b-instruct-q4_K_M \
  --overwrite \
  --progress_every 1

python scripts/12_summarize_vlm_image_judge.py \
  --input_dir data/judges/ahd_cosmos3_smoke12_qwen32

python scripts/13_materialize_curated_pool.py \
  --results data/generated_runs/ahd_cosmos3_smoke12/results.jsonl \
  --judge_dir data/judges/ahd_cosmos3_smoke12_qwen32 \
  --pool_name ahd_cosmos3_smoke12_qwen32 \
  --overwrite
```

Accepted examples still need human audit before inclusion in test or counterfactual subsets.
Do not scale to `mini36` or larger until the VLM judge and human audit show that generated images satisfy AHD O0/O1 semantics.
