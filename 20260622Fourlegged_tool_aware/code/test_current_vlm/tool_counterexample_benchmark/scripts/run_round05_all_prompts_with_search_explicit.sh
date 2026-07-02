#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")/.."

RUN_TAG="${RUN_TAG:-round05_all_prompts_with_search_explicit}"
OUTPUT_DIR="${OUTPUT_DIR:-outputs/${RUN_TAG}}"
ANALYSIS_DIR="${ANALYSIS_DIR:-analysis_review/${RUN_TAG}}"
VLM_JUDGE_DIR="${VLM_JUDGE_DIR:-analysis_review/${RUN_TAG}_vlm_judge_qwen32}"
JUDGE_MODEL="${JUDGE_MODEL:-qwen3-vl:32b-instruct-q4_K_M}"
OLLAMA_URL="${OLLAMA_URL:-http://localhost:11434}"
PROGRESS_EVERY="${PROGRESS_EVERY:-1}"

MODEL_IDS=(
  ollama_gemma3_27b_it_q8_0
  ollama_llama3_2_vision_11b_instruct_q8_0
  ollama_minicpm_v4_5_q8_0
  ollama_qwen3_5_35b
  ollama_qwen3_vl_30b_a3b_instruct_q4_K_M
  ollama_qwen3_vl_32b_instruct_q4_K_M
)

PROMPT_IDS=(
  natural_free_plan
  efficient_safe_free_plan
  tool_prior_free_plan
  strong_decomposition_free_plan
  search_explicit_strong_decomposition_free_plan
  structured_tool_probe
  natural_free_plan_humanoid_dual_arm
  efficient_safe_free_plan_humanoid_dual_arm
  tool_prior_free_plan_humanoid_dual_arm
  strong_decomposition_free_plan_humanoid_dual_arm
  search_explicit_strong_decomposition_free_plan_humanoid_dual_arm
  structured_tool_action_chain_probe_humanoid_dual_arm
  natural_free_plan_quadruped_single_arm
  efficient_safe_free_plan_quadruped_single_arm
  tool_prior_free_plan_quadruped_single_arm
  strong_decomposition_free_plan_quadruped_single_arm
  search_explicit_strong_decomposition_free_plan_quadruped_single_arm
  structured_tool_action_chain_probe_quadruped_single_arm
)

TASK_ARGS=()

# shellcheck source=scripts/_round05_pipeline_common.sh
source scripts/_round05_pipeline_common.sh

run_round05_pipeline
