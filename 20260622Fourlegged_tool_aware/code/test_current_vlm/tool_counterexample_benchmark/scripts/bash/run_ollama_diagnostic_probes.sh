#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
# shellcheck source=_ollama_batch_common.sh
source "${SCRIPT_DIR}/_ollama_batch_common.sh"

bootstrap_batch "$@"
run_prompt_category "diagnostic_probes" \
  structured_tool_probe \
  structured_tool_action_chain_probe_humanoid_dual_arm \
  structured_tool_action_chain_probe_quadruped_single_arm
