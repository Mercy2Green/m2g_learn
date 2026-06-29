#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
# shellcheck source=_ollama_batch_common.sh
source "${SCRIPT_DIR}/_ollama_batch_common.sh"

bootstrap_batch "$@"
run_prompt_category "quadruped_single_arm_clean" \
  natural_free_plan_quadruped_single_arm \
  efficient_safe_free_plan_quadruped_single_arm
