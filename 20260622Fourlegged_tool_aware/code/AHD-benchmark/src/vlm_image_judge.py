from __future__ import annotations

import base64
import csv
import json
import socket
import time
import urllib.error
import urllib.request
from pathlib import Path
from typing import Any, Iterable


JUDGE_FIELDS = [
    "keep",
    "confidence",
    "spec_id",
    "spec_type",
    "target_visible_ok",
    "helper_absent_ok",
    "helper_visible_ok",
    "target_absent_ok",
    "forbidden_object_leakage",
    "count_reasonable",
    "camera_view_ok",
    "scene_compatibility_ok",
    "main_failure_reason",
    "one_prompt_fix",
]

CSV_FIELDS = [
    "spec_id",
    "spec_type",
    "view_stage",
    "image_path",
    "keep",
    "confidence",
    "target_visible_ok",
    "helper_absent_ok",
    "helper_visible_ok",
    "target_absent_ok",
    "forbidden_object_leakage",
    "count_reasonable",
    "camera_view_ok",
    "scene_compatibility_ok",
    "main_failure_reason",
    "one_prompt_fix",
    "judge_model",
    "prompt_source",
    "enrichment_model",
    "judge_parse_error",
    "judge_raw_response_short",
]

CHOICE_FIELDS = {
    "confidence": {"high", "medium", "low"},
    "target_visible_ok": {"yes", "no", "uncertain", "not_applicable"},
    "helper_absent_ok": {"yes", "no", "uncertain", "not_applicable"},
    "helper_visible_ok": {"yes", "no", "uncertain", "not_applicable"},
    "target_absent_ok": {"yes", "no", "uncertain", "not_applicable"},
    "forbidden_object_leakage": {"yes", "no", "uncertain"},
    "count_reasonable": {"yes", "no", "uncertain", "not_applicable"},
    "camera_view_ok": {"yes", "no", "uncertain"},
    "scene_compatibility_ok": {"yes", "no", "uncertain"},
}


def image_to_base64(path: str | Path) -> str:
    return base64.b64encode(Path(path).read_bytes()).decode("ascii")


def ollama_chat(base_url: str, model: str, prompt: str, images: list[str], temperature: float) -> str:
    payload: dict[str, Any] = {
        "model": model,
        "messages": [{"role": "user", "content": prompt}],
        "stream": False,
        "options": {"temperature": temperature},
    }
    if images:
        payload["messages"][0]["images"] = images
    request = urllib.request.Request(
        f"{base_url.rstrip('/')}/api/chat",
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(request, timeout=600) as response:
            data = json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        body = exc.read().decode("utf-8", errors="replace")
        if exc.code == 404 or "not found" in body.lower() or "pull" in body.lower():
            raise RuntimeError(f"Ollama model '{model}' is not available. Run: ollama pull {model}") from exc
        raise RuntimeError(f"Ollama request failed with HTTP {exc.code}: {body}") from exc
    except (urllib.error.URLError, TimeoutError, socket.timeout) as exc:
        raise RuntimeError(f"Could not connect to Ollama at {base_url}. Run: ollama serve") from exc
    if "error" in data:
        error = str(data.get("error", ""))
        if "not found" in error.lower() or "pull" in error.lower():
            raise RuntimeError(f"Ollama model '{model}' is not available. Run: ollama pull {model}")
        raise RuntimeError(f"Ollama error: {error}")
    return str(data.get("message", {}).get("content", ""))


def extract_json(text: str) -> dict[str, Any] | None:
    stripped = text.strip()
    if stripped.startswith("```"):
        stripped = stripped.strip("`")
        if stripped.lower().startswith("json"):
            stripped = stripped[4:].strip()
    for candidate in [stripped, _between_braces(stripped)]:
        if not candidate:
            continue
        try:
            parsed = json.loads(candidate)
        except json.JSONDecodeError:
            continue
        if isinstance(parsed, dict):
            return parsed
    return None


def run_judge_with_retries(
    *,
    base_url: str,
    model: str,
    prompt: str,
    images: list[str],
    temperature: float,
    max_retries: int,
) -> tuple[dict[str, Any] | None, str, str | None]:
    last_raw = ""
    attempts = max(1, int(max_retries) + 1)
    for attempt in range(attempts):
        retry_prompt = prompt
        if attempt:
            retry_prompt += "\n\nYour previous answer was not valid JSON. Return only one valid JSON object following the exact schema."
        try:
            raw = ollama_chat(base_url, model, retry_prompt, images, temperature)
        except RuntimeError as exc:
            return None, last_raw, str(exc)
        last_raw = raw
        parsed = extract_json(raw)
        if parsed is not None:
            return parsed, raw, None
        time.sleep(0.5)
    return None, last_raw, "judge_parse_error"


def build_ahd_image_quality_prompt(result_row: dict[str, Any], manifest_row: dict[str, Any]) -> str:
    spec_type = str(result_row.get("spec_type") or manifest_row.get("spec_type") or "")
    payload = {
        "spec_id": result_row.get("spec_id") or manifest_row.get("spec_id"),
        "spec_type": spec_type,
        "view_stage": result_row.get("view_stage") or manifest_row.get("view_stage"),
        "expected_core_condition": expected_core_condition(spec_type),
        "manifest_prompt_for_context_only": manifest_row.get("prompt", ""),
        "negative_prompt_for_context_only": manifest_row.get("negative_prompt", ""),
        "prompt_source": manifest_row.get("prompt_source", ""),
        "enrichment_model": manifest_row.get("enrichment_model", ""),
        "image_path": result_row.get("output_image_path", ""),
    }
    schema = {
        "keep": True,
        "confidence": "high | medium | low",
        "spec_id": "string",
        "spec_type": "string",
        "target_visible_ok": "yes | no | uncertain | not_applicable",
        "helper_absent_ok": "yes | no | uncertain | not_applicable",
        "helper_visible_ok": "yes | no | uncertain | not_applicable",
        "target_absent_ok": "yes | no | uncertain | not_applicable",
        "forbidden_object_leakage": "yes | no | uncertain",
        "count_reasonable": "yes | no | uncertain | not_applicable",
        "camera_view_ok": "yes | no | uncertain",
        "scene_compatibility_ok": "yes | no | uncertain",
        "main_failure_reason": "string",
        "one_prompt_fix": "string",
    }
    return f"""You are judging whether the generated image satisfies the AHD image specification.

AHD = Active Helper Discovery. The benchmark tests sequential partial observation:
- O0 image: target visible, helper absent.
- O1 image: helper visible, target absent or non-salient.
- The model must later use O0 target memory to decide whether an O1 object is a task-relevant helper.

This is only image-quality and AHD-condition checking.
Do NOT judge robot action chains.
Do NOT judge whether a model plan is correct.
Do NOT change or recommend changing gold labels.
The manifest prompt is not ground truth. If the image contradicts the prompt, judge the image.
Return only one JSON object. No markdown. No code fences.

Rubric by spec_type:

A. aggregate_transport_o0_target_visible_helper_absent
- This is O0.
- Target drinks/bottles/cans should be visible.
- Count >= 3 is acceptable.
- Exact count mismatch is only a warning, not automatic reject.
- Container/helper objects such as basket, tray, box, bag, tote bag, carrying container should be absent.
- target_absent_ok = not_applicable.
- helper_visible_ok = not_applicable.
- keep=true only if target_visible_ok=yes, helper_absent_ok=yes, forbidden_object_leakage=no, and count_reasonable is yes or uncertain.

B. direct_is_enough_o0_single_target
- This is O0.
- One single reachable target bottle/drink should be visible.
- No helper/container/long tool should be visible.
- keep=true only if target_visible_ok=yes, helper_absent_ok=yes, forbidden_object_leakage=no, and count_reasonable=yes.

C. extend_reach_o0_target_under_furniture
- This is O0.
- Target object should be partly visible under compatible furniture.
- Target should look hard to directly grasp.
- Long helper/tool should be absent.
- Furniture/environment compatibility matters.
- Bed in kitchen is suspicious.
- keep=true only if target_visible_ok=yes, helper_absent_ok=yes, forbidden_object_leakage=no, and scene_compatibility_ok is yes or uncertain.

D. container_helper_o1_target_absent
- This is O1.
- Container-like helper must be visible and salient.
- Examples: basket, tray, open box, tote bag.
- Original target objects such as bottles/cans/remote/small ball should be absent or non-salient.
- Long tools should not be visible.
- keep=true only if helper_visible_ok=yes, target_absent_ok=yes, and forbidden_object_leakage=no.

E. long_tool_helper_o1_target_absent
- This is O1.
- Long rigid helper should be visible and clearly usable.
- Good examples: broom, long stick, clear rod.
- Hanger is weak/ambiguous; mark keep=false or confidence=low unless it clearly appears as a rigid reach-extension helper.
- Original target objects should be absent or non-salient.
- Containers should not be visible.
- keep=true only if helper_visible_ok=yes, target_absent_ok=yes, and forbidden_object_leakage=no.

F. wrong_helper_o1_target_absent
- This is O1.
- A wrong object/distractor should be visible.
- Original target and correct helpers should be absent.
- Good wrong objects: book, cup, cloth, pillow, shoe.
- Short pencil is acceptable only if clearly short and not useful as a long rigid reach tool.
- keep=true only if target_absent_ok=yes, helper_absent_ok=yes, and forbidden_object_leakage=no.

Prompt-fix rules:
- If keep=false, one_prompt_fix must contain exactly one actionable sentence.
- If keep=true, one_prompt_fix must be "".
- Do not return multiple fixes.
- Do not return vague fixes like "make it better."
- Do not recommend changing gold labels.

Example one_prompt_fix values:
- "Remove task/action wording and describe only the visible scene."
- "Use 'several visible drink bottles' instead of an exact count."
- "Constrain this scene to a bedroom or dorm room when furniture is a bed."
- "Use broom, long stick, or clearly visible rod instead of hanger for long-tool O1."
- "Strengthen the negative prompt to exclude baskets, trays, boxes, and bags."

Input:
{json.dumps(payload, ensure_ascii=False, indent=2)}

Output JSON schema:
{json.dumps(schema, ensure_ascii=False, indent=2)}
"""


def normalize_judge_output(
    parsed: dict[str, Any] | None,
    result_row: dict[str, Any],
    manifest_row: dict[str, Any],
    raw_response: str,
    judge_model: str,
    *,
    parse_error: str | None = None,
    image_path: str | Path | None = None,
) -> dict[str, Any]:
    spec_id = str(result_row.get("spec_id") or manifest_row.get("spec_id") or "")
    spec_type = str(result_row.get("spec_type") or manifest_row.get("spec_type") or "")
    base = {
        "keep": False,
        "confidence": "low",
        "spec_id": spec_id,
        "spec_type": spec_type,
        "view_stage": str(result_row.get("view_stage") or manifest_row.get("view_stage") or ""),
        "image_path": str(image_path or result_row.get("output_image_path", "")),
        "target_visible_ok": "uncertain",
        "helper_absent_ok": "uncertain",
        "helper_visible_ok": "uncertain",
        "target_absent_ok": "uncertain",
        "forbidden_object_leakage": "uncertain",
        "count_reasonable": "uncertain",
        "camera_view_ok": "uncertain",
        "scene_compatibility_ok": "uncertain",
        "main_failure_reason": "judge_parse_error" if parse_error else "",
        "one_prompt_fix": "Rerun the local VLM judge or inspect this image manually." if parse_error else "",
        "judge_model": judge_model,
        "prompt_source": manifest_row.get("prompt_source"),
        "enrichment_model": manifest_row.get("enrichment_model"),
        "judge_parse_error": parse_error or "",
        "judge_raw_response_short": compact_text(raw_response, 500),
    }
    if parsed is None:
        return base

    base["keep"] = bool(parsed.get("keep", False))
    for field, allowed in CHOICE_FIELDS.items():
        base[field] = _choice_value(parsed.get(field), allowed, str(base[field]))
    base["spec_id"] = spec_id
    base["spec_type"] = spec_type
    base["main_failure_reason"] = compact_text(str(parsed.get("main_failure_reason", "")), 300)
    fix = str(parsed.get("one_prompt_fix", "")).strip()
    if base["keep"]:
        fix = ""
    elif not fix:
        fix = "Revise the prompt to make the required AHD visual condition more explicit."
    base["one_prompt_fix"] = one_sentence(fix)
    return base


def expected_core_condition(spec_type: str) -> str:
    if spec_type == "aggregate_transport_o0_target_visible_helper_absent":
        return "O0: multiple target drinks visible; count >= 3 acceptable; container/helper absent"
    if spec_type == "extend_reach_o0_target_under_furniture":
        return "O0: target partly visible under compatible furniture; long helper absent"
    if spec_type == "direct_is_enough_o0_single_target":
        return "O0: one reachable target drink visible; helper absent"
    if spec_type == "container_helper_o1_target_absent":
        return "O1: container-like helper visible and salient; original target absent or non-salient"
    if spec_type == "long_tool_helper_o1_target_absent":
        return "O1: long rigid helper visible and usable; original target absent or non-salient"
    if spec_type == "wrong_helper_o1_target_absent":
        return "O1: wrong distractor visible; original target and correct helpers absent"
    return "Manual AHD image-quality check required"


def resolve_image_path(result_row: dict[str, Any], ahd_root: str | Path) -> Path:
    value = Path(str(result_row.get("output_image_path") or result_row.get("image_path") or ""))
    return value if value.is_absolute() else Path(ahd_root) / value


def probe_image(path: str | Path) -> dict[str, Any]:
    file_path = Path(path)
    result: dict[str, Any] = {"exists": file_path.exists(), "valid_image": False, "width": None, "height": None, "error": None}
    if not file_path.exists():
        result["error"] = "missing_file"
        return result
    data = file_path.read_bytes()
    if data.startswith(b"\x89PNG\r\n\x1a\n") and len(data) >= 24:
        result.update({
            "valid_image": True,
            "width": int.from_bytes(data[16:20], "big"),
            "height": int.from_bytes(data[20:24], "big"),
        })
        return result
    if data.startswith(b"\xff\xd8"):
        size = _jpeg_size(data)
        if size is not None:
            result.update({"valid_image": True, "width": size[0], "height": size[1]})
            return result
    result["error"] = "invalid_or_unsupported_image"
    return result


def write_jsonl(path: str | Path, rows: Iterable[dict[str, Any]]) -> None:
    file_path = Path(path)
    file_path.parent.mkdir(parents=True, exist_ok=True)
    with file_path.open("w", encoding="utf-8") as handle:
        for row in rows:
            handle.write(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n")


def write_csv(path: str | Path, rows: Iterable[dict[str, Any]], fieldnames: list[str] | None = None) -> None:
    file_path = Path(path)
    file_path.parent.mkdir(parents=True, exist_ok=True)
    fields = fieldnames or CSV_FIELDS
    with file_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        for row in rows:
            writer.writerow({field: row.get(field, "") for field in fields})


def compact_text(text: str, limit: int) -> str:
    normalized = " ".join(str(text).split())
    if len(normalized) <= limit:
        return normalized
    return normalized[: max(0, limit - 3)] + "..."


def one_sentence(text: str) -> str:
    normalized = compact_text(text, 240)
    for delimiter in [". ", "! ", "? ", "\n"]:
        if delimiter in normalized:
            first = normalized.split(delimiter, 1)[0].strip()
            return first + ("." if delimiter.startswith(".") else "")
    return normalized


def _between_braces(text: str) -> str:
    start = text.find("{")
    end = text.rfind("}")
    if start == -1 or end == -1 or end <= start:
        return ""
    return text[start : end + 1]


def _choice_value(value: Any, allowed: set[str], default: str) -> str:
    normalized = str(value).strip().lower()
    return normalized if normalized in allowed else default


def _jpeg_size(data: bytes) -> tuple[int, int] | None:
    index = 2
    while index + 9 < len(data):
        if data[index] != 0xFF:
            index += 1
            continue
        marker = data[index + 1]
        index += 2
        if marker in {0xD8, 0xD9}:
            continue
        if index + 2 > len(data):
            break
        segment_length = int.from_bytes(data[index : index + 2], "big")
        if segment_length < 2 or index + segment_length > len(data):
            break
        if marker in {0xC0, 0xC1, 0xC2, 0xC3, 0xC5, 0xC6, 0xC7, 0xC9, 0xCA, 0xCB, 0xCD, 0xCE, 0xCF}:
            height = int.from_bytes(data[index + 3 : index + 5], "big")
            width = int.from_bytes(data[index + 5 : index + 7], "big")
            return width, height
        index += segment_length
    return None
