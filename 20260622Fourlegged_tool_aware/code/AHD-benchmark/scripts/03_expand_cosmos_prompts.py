from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.jsonl_utils import read_jsonl, write_jsonl
from src.load_config import load_yaml
from src.prompt_builder import build_prompt_from_spec


def main() -> None:
    specs = read_jsonl(ROOT / "specs" / "scene_specs_checked.jsonl")
    templates = load_yaml(ROOT / "configs" / "prompt_templates.yaml")
    entries = []
    for spec in specs:
        prompt, negative_prompt = build_prompt_from_spec(spec, templates)
        stage_dir = "o0" if spec["view_stage"] == "O0" else "o1"
        entries.append({
            "spec_id": spec["spec_id"],
            "view_stage": spec["view_stage"],
            "spec_type": spec["spec_type"],
            "seed": spec["seed"],
            "prompt": prompt,
            "negative_prompt": negative_prompt,
            "output_image_path": f"data/images/{stage_dir}/{spec['spec_id']}.png",
            "output_image_path_is_placeholder": True,
            "runtime_output_layout": "data/generated_runs/<run_name>/images/<o0_or_o1>/<spec_id>.jpg",
            "source_spec": spec,
        })
    write_jsonl(ROOT / "prompts" / "cosmos3_prompts_raw.jsonl", entries)
    print(f"Wrote {len(entries)} Cosmos3 prompt entries. No image API calls were made.")


if __name__ == "__main__":
    main()
