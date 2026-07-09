#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")/../.."

ENRICHMENT_FILE="specs/enrichment/llm_enriched_qwen3-vl_30b-a3b-instruct-q4_K_M_stratified40_preview.jsonl"
MANIFEST="prompts/manifests/cosmos3_raw240_manifest.jsonl"
RUN_NAME="ahd_cosmos3_raw240"
DRY_RUN_NAME="ahd_cosmos3_raw240_dryrun"
RESULTS="data/generated_runs/${RUN_NAME}/results.jsonl"
MANIFEST_SNAPSHOT="data/generated_runs/${RUN_NAME}/manifest_snapshot.jsonl"
JUDGE_DIR="data/judges/ahd_cosmos3_raw240_qwen32"
POOL_NAME="ahd_cosmos3_raw240_qwen32"

echo "[1/9] py_compile"
python -m py_compile \
  src/enrichment_schema.py \
  src/storage_layout.py \
  src/cosmos3_runner.py \
  scripts/03_expand_cosmos_prompts.py \
  scripts/05_ollama_enrich_scene_specs.py \
  scripts/06_check_llm_enrichment.py \
  scripts/07_build_cosmos3_manifest.py \
  scripts/08_run_cosmos3_batch.py \
  scripts/09_summarize_cosmos3_outputs.py \
  scripts/11_vlm_judge_generated_images.py \
  scripts/12_summarize_vlm_image_judge.py \
  scripts/13_materialize_curated_pool.py

echo "[2/9] check existing stratified40 enrichment"
if [[ ! -f "${ENRICHMENT_FILE}" ]]; then
  echo "Missing ${ENRICHMENT_FILE}" >&2
  echo "Generate it first with:" >&2
  echo "python scripts/05_ollama_enrich_scene_specs.py --model qwen3-vl:30b-a3b-instruct-q4_K_M --stratified_per_type 40" >&2
  exit 1
fi
python scripts/06_check_llm_enrichment.py "${ENRICHMENT_FILE}"
python - <<'PY'
from pathlib import Path
report = Path("specs/enrichment/llm_enriched_qwen3-vl_30b-a3b-instruct-q4_K_M_stratified40_preview_report.md")
text = report.read_text(encoding="utf-8")
required = [
    "- JSON parse failures: 0",
    "- Schema failures: 0",
    "- Leakage failures: 0",
]
missing = [item for item in required if item not in text]
if missing:
    raise SystemExit("Enrichment check did not pass: " + ", ".join(missing))
PY

echo "[3/9] build raw240 manifest"
python scripts/07_build_cosmos3_manifest.py \
  --plan raw240 \
  --use_enrichment true \
  --enrichment_file "${ENRICHMENT_FILE}"

echo "[4/9] dry-run raw240"
python scripts/08_run_cosmos3_batch.py \
  --manifest "${MANIFEST}" \
  --dry_run \
  --run_name "${DRY_RUN_NAME}"

echo "[5/9] actual raw240 generation"
python scripts/08_run_cosmos3_batch.py \
  --manifest "${MANIFEST}" \
  --run_name "${RUN_NAME}" \
  --yes

echo "[6/9] summarize generation"
python scripts/09_summarize_cosmos3_outputs.py \
  --results "${RESULTS}"

echo "[7/9] VLM judge"
python scripts/11_vlm_judge_generated_images.py \
  --results "${RESULTS}" \
  --manifest "${MANIFEST_SNAPSHOT}" \
  --output_dir "${JUDGE_DIR}" \
  --judge_model qwen3-vl:32b-instruct-q4_K_M \
  --overwrite \
  --progress_every 5

echo "[8/9] summarize VLM judge"
python scripts/12_summarize_vlm_image_judge.py \
  --input_dir "${JUDGE_DIR}"

echo "[9/9] materialize curated pool"
python scripts/13_materialize_curated_pool.py \
  --results "${RESULTS}" \
  --judge_dir "${JUDGE_DIR}" \
  --pool_name "${POOL_NAME}" \
  --overwrite

echo "Done."
echo "Generation summary: data/generated_runs/${RUN_NAME}/summary.md"
echo "Judge summary: ${JUDGE_DIR}/vlm_image_judge_summary.md"
echo "Curated summary: data/curated_pools/${POOL_NAME}/curated_summary.md"
