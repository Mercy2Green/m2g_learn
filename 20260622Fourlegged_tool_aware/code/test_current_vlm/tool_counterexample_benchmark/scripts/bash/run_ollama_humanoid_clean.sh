#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
# shellcheck source=_ollama_batch_common.sh
source "${SCRIPT_DIR}/_ollama_batch_common.sh"

bootstrap_batch "$@"
run_prompt_category "humanoid_dual_arm_clean" \
  natural_free_plan_humanoid_dual_arm \
  efficient_safe_free_plan_humanoid_dual_arm
