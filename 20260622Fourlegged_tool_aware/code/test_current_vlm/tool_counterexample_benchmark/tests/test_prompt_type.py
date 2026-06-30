from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.run_batch import prompt_type_for  # noqa: E402


def test_prompt_type_for_primary() -> None:
    assert prompt_type_for({"primary_for_counterexample": True}) == "primary_clean"


def test_prompt_type_for_diagnostic_probe() -> None:
    assert prompt_type_for({"primary_for_counterexample": False, "prompt_category": "diagnostic_probe"}) == "structured_probe"


def test_prompt_type_for_tool_prior_intervention() -> None:
    assert (
        prompt_type_for({"primary_for_counterexample": False, "prompt_category": "tool_prior_intervention"})
        == "tool_prior_intervention"
    )


def test_prompt_type_for_unknown_non_primary() -> None:
    assert prompt_type_for({"primary_for_counterexample": False}) == "non_primary"
    assert prompt_type_for({"primary_for_counterexample": False, "prompt_category": "custom_category"}) == "custom_category"


if __name__ == "__main__":
    test_prompt_type_for_primary()
    test_prompt_type_for_diagnostic_probe()
    test_prompt_type_for_tool_prior_intervention()
    test_prompt_type_for_unknown_non_primary()
    print("prompt_type tests passed")
