python scripts/08_run_cosmos3_batch.py \
  --manifest prompts/manifests/cosmos3_smoke12_manifest.jsonl \
  --run_name ahd_cosmos3_smoke12 \
  --timeout_seconds 900 \
  --yes

python scripts/09_summarize_cosmos3_outputs.py \
  --results data/runs/ahd_cosmos3_smoke12_results.jsonl