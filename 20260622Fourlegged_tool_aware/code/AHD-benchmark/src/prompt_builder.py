from __future__ import annotations

from typing import Any


def _join(value: Any) -> str:
    if isinstance(value, list):
        return ", ".join(str(item) for item in value)
    return str(value)


def build_prompt_from_spec(spec: dict[str, Any], prompt_templates: dict[str, Any]) -> tuple[str, str]:
    templates = prompt_templates.get("templates", prompt_templates)
    spec_type = spec["spec_type"]
    if spec_type not in templates:
        raise KeyError(f"No prompt template configured for spec_type: {spec_type}")

    visual = spec.get("visual_scene", {})
    fields = {key: _join(value) for key, value in visual.items()}
    fields.setdefault("furniture", "")
    fields.setdefault("helper_description", "")
    fields.setdefault("target_description", "")
    fields.setdefault("must_exclude", "")
    fields.setdefault("avoid", "")
    fields.setdefault("distractors", "")

    template = templates[spec_type]
    prompt = template["positive_prompt_template"].format(**fields)
    negative_prompt = template["negative_prompt_template"].format(**fields)
    return prompt, negative_prompt
