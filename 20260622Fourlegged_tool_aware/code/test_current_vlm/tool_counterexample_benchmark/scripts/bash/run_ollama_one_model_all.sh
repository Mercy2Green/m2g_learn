#!/usr/bin/env bash
set -euo pipefail

if [[ $# -lt 1 ]]; then
  echo "Usage: $0 <model_id> [extra run_batch args...]" >&2
  echo "Example: $0 ollama_qwen3_vl_32b_instruct_q4_K_M --task_ids task_001 task_002" >&2
  exit 1
fi

MODEL_ID="$1"
shift

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
# shellcheck source=_ollama_batch_common.sh
source "${SCRIPT_DIR}/_ollama_batch_common.sh"

bootstrap_batch "$@"
run_prompt_category_for_models "generic_clean" "${MODEL_ID}" \
  natural_free_plan \
  efficient_safe_free_plan
run_prompt_category_for_models "humanoid_dual_arm_clean" "${MODEL_ID}" \
  natural_free_plan_humanoid_dual_arm \
  efficient_safe_free_plan_humanoid_dual_arm
run_prompt_category_for_models "quadruped_single_arm_clean" "${MODEL_ID}" \
  natural_free_plan_quadruped_single_arm \
  efficient_safe_free_plan_quadruped_single_arm
run_prompt_category_for_models "tool_prior_intervention" "${MODEL_ID}" \
  tool_prior_free_plan \
  tool_prior_free_plan_humanoid_dual_arm \
  tool_prior_free_plan_quadruped_single_arm
run_prompt_category_for_models "diagnostic_probes" "${MODEL_ID}" \
  structured_tool_probe \
  structured_tool_action_chain_probe_humanoid_dual_arm \
  structured_tool_action_chain_probe_quadruped_single_arm
