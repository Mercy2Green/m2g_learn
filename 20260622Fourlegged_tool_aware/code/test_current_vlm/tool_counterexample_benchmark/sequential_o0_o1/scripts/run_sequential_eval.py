from __future__ import annotations

import argparse
from concurrent.futures import ThreadPoolExecutor
import json
import shutil
import threading
from pathlib import Path
import sys
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from sequential_o0_o1.sequential_evaluator import summarize_raw_file  # noqa: E402
from src.load_config import load_dotenv, load_yaml, snapshot_configs  # noqa: E402
from src.providers.factory import create_provider  # noqa: E402


CLEAN_FORBIDDEN_TERMS = [
    "工具", "容器", "托盘", "篮子", "箱子", "盒子", "袋子", "扫把", "长杆", "杆子",
    "tool", "helper", "container", "tray", "basket", "box", "broom", "stick", "rod",
]


def main() -> None:
    args = parse_args()
    load_dotenv(ROOT / ".env")
    samples_path = root_path(args.samples)
    models_path = root_path(args.models)
    prompts_path = root_path(args.sequential_prompts)
    overrides_path = root_path(args.model_overrides)
    output_dir = root_path(args.output_dir)
    prepare_output(output_dir, args.overwrite)

    samples = select_items(read_jsonl(samples_path), "sample_id", args.sample_ids, enabled_only=False)
    model_config = load_yaml(models_path)
    override_config = load_yaml(overrides_path)
    prompt_config = load_yaml(prompts_path)
    old_prompt_config = load_yaml(ROOT / "config" / "prompt_sets.yaml")
    model_rows = apply_model_overrides(
        model_config.get("models", []), override_config.get("model_overrides", [])
    )
    models = select_items(model_rows, "model_id", args.model_ids, enabled_only=not bool(args.model_ids))
    prompts = select_items(prompt_config.get("prompts", []), "prompt_id", args.prompt_ids, enabled_only=False)
    if not samples or not models or not prompts:
        raise SystemExit("Samples, selected models, and selected prompts must all be non-empty.")
    validate_prompt_inheritance(prompts, old_prompt_config.get("prompts", []))
    validate_clean_prompts(prompts)
    validate_sample_images(samples)

    providers: dict[str, Any] = {}
    provider_errors: dict[str, str] = {}
    if not args.dry_run:
        for model in models:
            model_id = str(model["model_id"])
            try:
                providers[model_id] = create_provider(model)
            except Exception as exc:  # noqa: BLE001
                provider_errors[model_id] = str(exc)

    raw_path = output_dir / "raw_responses.jsonl"
    processed = 0
    with raw_path.open("w", encoding="utf-8") as handle:
        if args.parallel_models > 1:
            if args.limit is not None:
                raise ValueError("--parallel_models > 1 cannot be combined with --limit")
            write_lock = threading.Lock()
            progress = {"count": 0}

            def run_model(model: dict[str, Any]) -> None:
                for sample in samples:
                    for prompt in prompts:
                        raw = run_one(sample, prompt, model, providers, provider_errors, args.dry_run)
                        with write_lock:
                            progress["count"] += 1
                            handle.write(json.dumps(raw, ensure_ascii=False, sort_keys=True) + "\n")
                            handle.flush()
                            print(
                                f"[{progress['count']}] {sample['sample_id']} / {prompt['prompt_id']} / "
                                f"{model['model_id']} error={bool(raw['error'])}"
                            )

            with ThreadPoolExecutor(max_workers=min(args.parallel_models, len(models))) as executor:
                futures = [executor.submit(run_model, model) for model in models]
                for future in futures:
                    future.result()
            processed = progress["count"]
        else:
            for model in models:
                for sample in samples:
                    for prompt in prompts:
                        if args.limit is not None and processed >= args.limit:
                            break
                        processed += 1
                        raw = run_one(sample, prompt, model, providers, provider_errors, args.dry_run)
                        handle.write(json.dumps(raw, ensure_ascii=False, sort_keys=True) + "\n")
                        handle.flush()
                        print(
                            f"[{processed}] {sample['sample_id']} / {prompt['prompt_id']} / "
                            f"{model['model_id']} error={bool(raw['error'])}"
                        )
                    if args.limit is not None and processed >= args.limit:
                        break
                if args.limit is not None and processed >= args.limit:
                    break

    snapshot_configs(
        [
            models_path,
            prompts_path,
            samples_path,
            ROOT / "sequential_o0_o1" / "config" / "sequential_eval_config.yaml",
            overrides_path,
            ROOT / "config" / "prompt_sets.yaml",
        ],
        output_dir,
    )
    result = summarize_raw_file(output_dir)
    print(json.dumps({"output_dir": str(output_dir), **result}, ensure_ascii=False))


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run isolated sequential O0/O1 VLM evaluation.")
    parser.add_argument("--samples", default="sequential_o0_o1/data/sequential_smoke_samples.jsonl")
    parser.add_argument("--models", default="config/models.yaml")
    parser.add_argument("--sequential_prompts", default="sequential_o0_o1/prompts/sequential_prompt_sets.yaml")
    parser.add_argument(
        "--model_overrides",
        default="sequential_o0_o1/config/sequential_model_overrides.yaml",
    )
    parser.add_argument("--output_dir", default="outputs/sequential_o0_o1_smoke")
    parser.add_argument("--model_ids", nargs="*", default=None)
    parser.add_argument("--prompt_ids", nargs="*", default=None)
    parser.add_argument("--sample_ids", nargs="*", default=None)
    parser.add_argument("--limit", type=int, default=None)
    parser.add_argument("--parallel_models", type=int, default=1)
    parser.add_argument("--overwrite", action="store_true")
    parser.add_argument("--dry_run", action="store_true")
    return parser.parse_args()


def root_path(value: str | Path) -> Path:
    path = Path(value)
    return path if path.is_absolute() else (ROOT / path).resolve()


def prepare_output(path: Path, overwrite: bool) -> None:
    if path == ROOT or ROOT not in path.parents:
        raise SystemExit(f"Output directory must be below benchmark root: {path}")
    if path.exists():
        if not overwrite:
            raise SystemExit(f"Output directory exists: {path}. Use --overwrite to replace it.")
        shutil.rmtree(path)
    path.mkdir(parents=True, exist_ok=True)


def read_jsonl(path: Path) -> list[dict[str, Any]]:
    if not path.is_file():
        raise FileNotFoundError(f"JSONL file not found: {path}")
    rows: list[dict[str, Any]] = []
    with path.open("r", encoding="utf-8") as handle:
        for line_no, line in enumerate(handle, start=1):
            if not line.strip():
                continue
            value = json.loads(line)
            if not isinstance(value, dict):
                raise ValueError(f"JSONL row {line_no} is not an object: {path}")
            rows.append(value)
    return rows


def select_items(
    items: Any, key: str, selected: list[str] | None, *, enabled_only: bool
) -> list[dict[str, Any]]:
    if not isinstance(items, list):
        raise ValueError(f"Config key for {key} entries must be a list.")
    available = {str(item.get(key, "")): item for item in items if isinstance(item, dict)}
    if selected:
        missing = sorted(set(selected) - set(available))
        if missing:
            raise ValueError(f"Unknown {key} values: {missing}")
        result = [available[item_id] for item_id in selected]
    else:
        result = list(available.values())
    if enabled_only:
        result = [item for item in result if item.get("enabled", True)]
    return result


def apply_model_overrides(models: Any, overrides: Any) -> list[dict[str, Any]]:
    if not isinstance(models, list) or not isinstance(overrides, list):
        raise ValueError("models and model_overrides must be lists")
    allowed = {"max_tokens", "num_ctx", "format_json", "timeout_seconds", "retries"}
    override_by_id: dict[str, dict[str, Any]] = {}
    for row in overrides:
        if not isinstance(row, dict) or not row.get("model_id"):
            raise ValueError("Each sequential model override must have model_id")
        unexpected = set(row) - allowed - {"model_id", "reason"}
        if unexpected:
            raise ValueError(f"Unsupported sequential override fields for {row['model_id']}: {sorted(unexpected)}")
        override_by_id[str(row["model_id"])] = {key: row[key] for key in allowed if key in row}

    known_ids = {str(row.get("model_id", "")) for row in models if isinstance(row, dict)}
    unknown = sorted(set(override_by_id) - known_ids)
    if unknown:
        raise ValueError(f"Sequential overrides reference unknown models: {unknown}")

    output: list[dict[str, Any]] = []
    for model in models:
        copied = dict(model)
        override = override_by_id.get(str(copied.get("model_id", "")), {})
        copied.update(override)
        copied["sequential_model_override"] = override
        output.append(copied)
    return output


def validate_prompt_inheritance(
    prompts: list[dict[str, Any]], old_prompts: list[dict[str, Any]]
) -> None:
    old_by_id = {str(prompt.get("prompt_id", "")): prompt for prompt in old_prompts}
    for prompt in prompts:
        base_id = str(prompt.get("base_prompt_id") or prompt.get("turn1_base_prompt_id") or "")
        base = old_by_id.get(base_id)
        if base is None:
            raise ValueError(f"Sequential prompt has unknown base prompt: {base_id}")
        if prompt.get("system_prompt") != base.get("system_prompt"):
            raise ValueError(f"{prompt['prompt_id']}: system_prompt differs from old {base_id}")
        if prompt.get("response_schema_text") != base.get("response_schema_text"):
            raise ValueError(f"{prompt['prompt_id']}: response schema differs from old {base_id}")
        if prompt.get("protocol") == "two_turn_sequential":
            if prompt.get("turn1_user_prompt_template") != base.get("user_prompt_template"):
                raise ValueError(f"{prompt['prompt_id']}: turn1 user template differs from old {base_id}")


def validate_clean_prompts(prompts: list[dict[str, Any]]) -> None:
    for prompt in prompts:
        category = str(prompt.get("prompt_category", ""))
        if category != "sequential_clean" and not category.endswith("_clean"):
            continue
        user_text = " ".join(
            str(prompt.get(key, ""))
            for key in ("user_prompt_template", "turn1_user_prompt_template", "turn2_user_prompt")
        ).lower()
        leaked = sorted(term for term in CLEAN_FORBIDDEN_TERMS if term.lower() in user_text)
        if leaked:
            raise ValueError(f"{prompt['prompt_id']}: clean prompt leaks helper terms: {leaked}")


def validate_sample_images(samples: list[dict[str, Any]]) -> None:
    for sample in samples:
        for key in ("o0_image_path", "o1_image_path"):
            path = root_path(str(sample.get(key, "")))
            if not path.is_file():
                raise FileNotFoundError(f"{sample.get('sample_id')}: missing {key}: {path}")


def run_one(
    sample: dict[str, Any],
    prompt: dict[str, Any],
    model: dict[str, Any],
    providers: dict[str, Any],
    provider_errors: dict[str, str],
    dry_run: bool,
) -> dict[str, Any]:
    protocol = str(prompt["protocol"])
    system_prompt = with_schema(prompt)
    instruction = str(sample["instruction"])
    o0_path = str(root_path(str(sample["o0_image_path"])))
    o1_path = str(root_path(str(sample["o1_image_path"])))
    user_prompt_turn1 = ""
    user_prompt_turn2 = ""

    if protocol == "single_turn_multi_image":
        user_prompt_turn1 = str(prompt["user_prompt_template"]).format(instruction=instruction).strip()
    elif protocol == "two_turn_sequential":
        user_prompt_turn1 = str(prompt["turn1_user_prompt_template"]).format(instruction=instruction).strip()
        user_prompt_turn2 = str(prompt["turn2_user_prompt"]).strip()
    else:
        raise ValueError(f"Unsupported sequential protocol: {protocol}")

    raw = {
        **{key: sample.get(key, "") for key in (
            "sample_id", "sample_type", "group_id", "instruction", "o0_image_path", "o1_image_path",
            "o0_spec_id", "o1_spec_id", "o0_spec_type", "o1_spec_type", "old_task_id_source", "gold", "notes",
        )},
        "protocol": protocol,
        "prompt_id": prompt["prompt_id"],
        "prompt_category": prompt.get("prompt_category", ""),
        "primary_for_sequential": bool(prompt.get("primary_for_sequential", False)),
        "model_id": model["model_id"],
        "provider": model.get("provider", ""),
        "provider_label": model.get("provider_label", model.get("provider", "")),
        "model_name": model.get("model_name", ""),
        "configured_max_tokens": model.get("max_tokens", ""),
        "configured_num_ctx": model.get("num_ctx", ""),
        "configured_format_json": model.get("format_json", ""),
        "sequential_model_override": model.get("sequential_model_override", {}),
        "system_prompt": system_prompt,
        "user_prompt_turn1": user_prompt_turn1,
        "user_prompt_turn2": user_prompt_turn2,
        "raw_response_turn1": "",
        "raw_response_final": "",
        "metadata_turn1": {},
        "metadata_final": {},
        "error": "",
        "dry_run": dry_run,
    }
    if dry_run:
        return raw

    model_id = str(model["model_id"])
    if model_id in provider_errors:
        raw["error"] = provider_errors[model_id]
        return raw
    provider = providers.get(model_id)
    if provider is None:
        raw["error"] = "Provider was not initialized."
        return raw

    try:
        if protocol == "single_turn_multi_image":
            messages = [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt_turn1, "images": [o0_path, o1_path]},
            ]
            result = provider.run_chat_with_retry(messages)
            raw["raw_response_final"] = result.get("raw_response", "")
            raw["metadata_final"] = result.get("metadata", {})
        else:
            turn1_messages = [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt_turn1, "images": [o0_path]},
            ]
            turn1 = provider.run_chat_with_retry(turn1_messages)
            raw["raw_response_turn1"] = turn1.get("raw_response", "")
            raw["metadata_turn1"] = turn1.get("metadata", {})
            turn2_messages = [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt_turn1, "images": [o0_path]},
                {"role": "assistant", "content": raw["raw_response_turn1"]},
                {"role": "user", "content": user_prompt_turn2, "images": [o1_path]},
            ]
            final = provider.run_chat_with_retry(turn2_messages)
            raw["raw_response_final"] = final.get("raw_response", "")
            raw["metadata_final"] = final.get("metadata", {})
    except Exception as exc:  # noqa: BLE001
        raw["error"] = str(exc)
    return raw


def with_schema(prompt: dict[str, Any]) -> str:
    system = str(prompt["system_prompt"]).strip()
    schema = str(prompt.get("response_schema_text", "")).strip()
    return f"{system}\n\n{schema}" if schema else system


if __name__ == "__main__":
    main()
