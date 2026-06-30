from __future__ import annotations

import argparse
import json
import shutil
from pathlib import Path
from typing import Any
from urllib.parse import urlparse

from .evaluator import assign_counterexample_strength, evaluate_response
from .image_utils import PLACEHOLDER_IMAGE, is_placeholder_image, list_images
from .load_config import enabled_items, load_dotenv, load_yaml, snapshot_configs
from .prompt_builder import build_prompt
from .providers.factory import create_provider
from .report_writer import append_jsonl, write_evaluation_csv, write_reports
from .response_parser import parse_model_response


def main() -> None:
    args = parse_args()
    root_dir = Path(__file__).resolve().parents[1]
    load_dotenv(root_dir / ".env")

    output_dir = Path(args.output_dir)
    if not output_dir.is_absolute():
        output_dir = root_dir / output_dir
    if output_dir.exists() and args.overwrite:
        shutil.rmtree(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    raw_path = output_dir / "raw_responses.jsonl"
    parsed_path = output_dir / "parsed_results.jsonl"
    for path in [raw_path, parsed_path]:
        if path.exists():
            path.unlink()

    tasks_config = load_yaml(root_dir / args.tasks if not Path(args.tasks).is_absolute() else args.tasks)
    models_config = load_yaml(root_dir / args.models if not Path(args.models).is_absolute() else args.models)
    prompts_config = load_yaml(root_dir / args.prompts if not Path(args.prompts).is_absolute() else args.prompts)

    tasks = filter_by_ids(tasks_config.get("tasks", []), "task_id", args.task_ids)
    models = filter_by_ids(enabled_items(models_config, "models"), "model_id", args.model_ids)
    prompts = filter_by_ids(prompts_config.get("prompts", []), "prompt_id", args.prompt_ids)

    if args.dry_run:
        models = dry_run_models(models)

    if not tasks:
        raise ValueError("No tasks selected.")
    if not models:
        raise ValueError("No models selected.")
    if not prompts:
        raise ValueError("No prompt sets selected.")

    snapshot_configs(
        [
            root_dir / args.tasks if not Path(args.tasks).is_absolute() else args.tasks,
            root_dir / args.models if not Path(args.models).is_absolute() else args.models,
            root_dir / args.prompts if not Path(args.prompts).is_absolute() else args.prompts,
        ],
        output_dir,
    )

    providers = build_providers(models, args.dry_run)
    evaluations: list[dict[str, Any]] = []
    parsed_records: list[dict[str, Any]] = []
    processed = 0

    for task in tasks:
        images = list_images(task.get("image_dir", ""), root_dir, allow_placeholder=args.dry_run)
        if not images:
            for model in models:
                for prompt in prompts:
                    evaluations.append(skipped_record(task, model, prompt, "No image files found for task."))
            continue

        for image_path in images:
            for prompt in prompts:
                system_prompt, user_prompt, leakage_terms = build_prompt(task, prompt)
                for model in models:
                    if args.limit is not None and processed >= args.limit:
                        return finalize(output_dir, raw_path, parsed_path, tasks, models, prompts, evaluations, parsed_records)
                    processed += 1

                    model_id = model.get("model_id", "")
                    provider = providers.get(model_id)
                    if provider is None:
                        raw_record = base_record(task, model, prompt, image_path, system_prompt, user_prompt)
                        raw_record.update({"error": "Provider was not initialized.", "raw_response": ""})
                        append_jsonl(raw_path, raw_record)
                        parsed_record = parsed_output_record(raw_record, {"parse_status": "parse_error", "parsed": {}, "parse_error": "Provider was not initialized."})
                        append_jsonl(parsed_path, parsed_record)
                        parsed_records.append(parsed_record)
                        evaluations.append(evaluate_response(task, parsed_record, model, prompt, str(image_path)))
                        continue

                    raw_record = base_record(task, model, prompt, image_path, system_prompt, user_prompt)
                    raw_record["prompt_leakage_terms"] = leakage_terms
                    try:
                        if is_placeholder_image(image_path) and not args.dry_run:
                            raise FileNotFoundError("Placeholder image is only allowed in dry_run.")
                        result = provider.run_with_retry(str(image_path), system_prompt, user_prompt)
                        raw_record.update(result)
                        raw_record["error"] = ""
                    except Exception as exc:  # noqa: BLE001
                        raw_record.update(
                            {
                                "provider": model.get("provider", ""),
                                "model_name": model.get("model_name", ""),
                                "raw_response": "",
                                "metadata": {},
                                "error": str(exc),
                            }
                        )
                    append_jsonl(raw_path, raw_record)

                    if raw_record.get("error"):
                        parsed = {"parse_status": "parse_error", "parsed": {}, "parse_error": raw_record["error"]}
                    else:
                        parsed = parse_model_response(str(raw_record.get("raw_response", "")))
                    parsed_record = parsed_output_record(raw_record, parsed)
                    append_jsonl(parsed_path, parsed_record)
                    parsed_records.append(parsed_record)
                    evaluations.append(evaluate_response(task, parsed_record, model, prompt, str(image_path)))

    finalize(output_dir, raw_path, parsed_path, tasks, models, prompts, evaluations, parsed_records)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run tool-aware planning counterexample benchmark.")
    parser.add_argument("--tasks", default="config/tasks.yaml")
    parser.add_argument("--models", default="config/models.yaml")
    parser.add_argument("--prompts", default="config/prompt_sets.yaml")
    parser.add_argument("--output_dir", default="outputs/run_001")
    parser.add_argument("--task_ids", nargs="*", default=None)
    parser.add_argument("--model_ids", nargs="*", default=None)
    parser.add_argument("--prompt_ids", nargs="*", default=None)
    parser.add_argument("--dry_run", action="store_true")
    parser.add_argument("--limit", type=int, default=None)
    parser.add_argument("--overwrite", action="store_true")
    return parser.parse_args()


def filter_by_ids(items: list[dict[str, Any]], id_key: str, selected_ids: list[str] | None) -> list[dict[str, Any]]:
    if not selected_ids:
        return items
    selected = set(selected_ids)
    return [item for item in items if item.get(id_key) in selected]


def prompt_type_for(prompt: dict[str, Any]) -> str:
    if prompt.get("primary_for_counterexample", False):
        return "primary_clean"
    category = str(prompt.get("prompt_category", ""))
    if category == "diagnostic_probe":
        return "structured_probe"
    if category == "tool_prior_intervention":
        return "tool_prior_intervention"
    return category or "non_primary"


def dry_run_models(models: list[dict[str, Any]]) -> list[dict[str, Any]]:
    selected_mock = [model for model in models if model.get("provider") == "mock"]
    if selected_mock:
        return selected_mock
    return [
        {
            "model_id": "mock",
            "provider": "mock",
            "provider_label": "mock",
            "enabled": True,
            "model_name": "mock",
            "strength_role": "mock",
            "temperature": 0.0,
            "max_tokens": 1024,
            "timeout_seconds": 5,
            "retries": 0,
        }
    ]


def build_providers(models: list[dict[str, Any]], dry_run: bool) -> dict[str, Any]:
    providers: dict[str, Any] = {}
    for model in models:
        model_id = str(model.get("model_id", ""))
        try:
            providers[model_id] = create_provider(model)
        except Exception as exc:  # noqa: BLE001
            if dry_run:
                raise
            print(f"[WARN] Could not initialize provider for {model_id}: {exc}")
    return providers


def base_record(
    task: dict[str, Any],
    model: dict[str, Any],
    prompt: dict[str, Any],
    image_path: str | Path,
    system_prompt: str,
    user_prompt: str,
) -> dict[str, Any]:
    image_value = str(image_path) if str(image_path) != PLACEHOLDER_IMAGE else PLACEHOLDER_IMAGE
    return {
        "task_id": task.get("task_id", ""),
        "task_name": task.get("name", ""),
        "image_path": image_value,
        "model_id": model.get("model_id", ""),
        "provider": model.get("provider", ""),
        "provider_label": model.get("provider_label", model.get("provider", "")),
        "model_name": model.get("model_name", ""),
        "strength_role": model.get("strength_role", ""),
        "supports_vision": model.get("supports_vision", ""),
        "base_url_host": urlparse(str(model.get("base_url", ""))).netloc,
        "prompt_id": prompt.get("prompt_id", ""),
        "embodiment_profile": prompt.get("embodiment_profile", "generic"),
        "prompt_category": prompt.get("prompt_category", ""),
        "diagnostic_type": prompt.get("diagnostic_type", ""),
        "primary_for_counterexample": bool(prompt.get("primary_for_counterexample", False)),
        "prompt_type": prompt_type_for(prompt),
        "system_prompt": system_prompt,
        "user_prompt": user_prompt,
    }


def parsed_output_record(raw_record: dict[str, Any], parsed: dict[str, Any]) -> dict[str, Any]:
    return {
        "task_id": raw_record.get("task_id", ""),
        "task_name": raw_record.get("task_name", ""),
        "image_path": raw_record.get("image_path", ""),
        "model_id": raw_record.get("model_id", ""),
        "provider": raw_record.get("provider", ""),
        "provider_label": raw_record.get("provider_label", ""),
        "model_name": raw_record.get("model_name", ""),
        "strength_role": raw_record.get("strength_role", ""),
        "supports_vision": raw_record.get("supports_vision", ""),
        "prompt_id": raw_record.get("prompt_id", ""),
        "embodiment_profile": raw_record.get("embodiment_profile", "generic"),
        "prompt_category": raw_record.get("prompt_category", ""),
        "diagnostic_type": raw_record.get("diagnostic_type", ""),
        "primary_for_counterexample": raw_record.get("primary_for_counterexample", False),
        "prompt_type": raw_record.get("prompt_type", ""),
        "parse_status": parsed.get("parse_status", ""),
        "parse_error": parsed.get("parse_error", ""),
        "parsed": parsed.get("parsed", {}),
        "raw_response": raw_record.get("raw_response", ""),
        "error": raw_record.get("error", ""),
        "prompt_leakage_terms": raw_record.get("prompt_leakage_terms", []),
    }


def skipped_record(task: dict[str, Any], model: dict[str, Any], prompt: dict[str, Any], reason: str) -> dict[str, Any]:
    return {
        "task_id": task.get("task_id", ""),
        "task_name": task.get("name", ""),
        "image_path": "",
        "model_id": model.get("model_id", ""),
        "provider": model.get("provider", ""),
        "provider_label": model.get("provider_label", model.get("provider", "")),
        "model_name": model.get("model_name", ""),
        "strength_role": model.get("strength_role", ""),
        "supports_vision": model.get("supports_vision", ""),
        "prompt_id": prompt.get("prompt_id", ""),
        "embodiment_profile": prompt.get("embodiment_profile", "generic"),
        "prompt_category": prompt.get("prompt_category", ""),
        "diagnostic_type": prompt.get("diagnostic_type", ""),
        "prompt_type": prompt_type_for(prompt),
        "primary_for_counterexample": bool(prompt.get("primary_for_counterexample", False)),
        "pass_fail": "skipped",
        "failure_types_detected": [],
        "counterexample_strength_hint": "invalid_or_unclear",
        "notes": reason,
    }


def finalize(
    output_dir: Path,
    raw_path: Path,
    parsed_path: Path,
    tasks: list[dict[str, Any]],
    models: list[dict[str, Any]],
    prompts: list[dict[str, Any]],
    evaluations: list[dict[str, Any]],
    parsed_records: list[dict[str, Any]],
) -> None:
    evaluations = assign_counterexample_strength(evaluations)
    write_evaluation_csv(output_dir / "evaluation.csv", evaluations)
    write_reports(
        output_dir,
        tasks,
        models,
        prompts,
        evaluations,
        parsed_records,
        raw_path.name,
        parsed_path.name,
    )
    print(json.dumps({"output_dir": str(output_dir), "evaluated_rows": len(evaluations)}, ensure_ascii=False))


if __name__ == "__main__":
    main()
