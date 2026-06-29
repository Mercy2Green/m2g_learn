from __future__ import annotations

import argparse
import json
import tempfile
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
COMMONS_API = "https://commons.wikimedia.org/w/api.php"
OPENVERSE_API = "https://api.openverse.org/v1/images/"
USER_AGENT = "m2g-learn-research-image-collection/0.1 (internal academic smoke-test image collection)"
SUPPORTED_MIME = {"image/jpeg", "image/png", "image/webp"}
MAX_LONG_SIDE = 1280
MIN_SIDE = 300

import sys

sys.path.insert(0, str(ROOT))
from src.load_config import load_yaml  # noqa: E402

try:
    from PIL import Image
except ImportError as exc:  # pragma: no cover
    raise RuntimeError("Pillow is required. Install with: pip install -r requirements.txt") from exc


def main() -> int:
    args = parse_args()
    query_config = load_yaml(ROOT / args.query_config)
    manual_config = load_optional_yaml(ROOT / args.manual_urls)
    tasks = filter_tasks(query_config.get("tasks", []), args.task_ids)
    if not tasks:
        print("No tasks selected.")
        return 1

    metadata_dir = ROOT / "image_metadata"
    metadata_dir.mkdir(parents=True, exist_ok=True)
    metadata_path = metadata_dir / "web_images.jsonl"

    records: list[dict[str, Any]] = []
    if args.dry_run:
        for task in tasks:
            print(f"DRY RUN {task['task_id']}: target={min(args.max_per_task, int(task.get('target_num_images', args.max_per_task)))}")
            for query in task.get("queries", []):
                print(f"  query: {query}")
        write_reports(metadata_dir, records, tasks)
        return 0

    for task in tasks:
        records.extend(collect_for_task(task, manual_config, args))

    with metadata_path.open("w", encoding="utf-8") as handle:
        for record in records:
            handle.write(json.dumps(record, ensure_ascii=False) + "\n")
    write_reports(metadata_dir, records, tasks)
    print(f"Wrote metadata: {metadata_path}")
    print(f"Wrote summary: {metadata_dir / 'web_images_summary.md'}")
    print(f"Wrote checklist: {metadata_dir / 'manual_review_checklist.md'}")
    return 0


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Collect temporary web images for internal smoke tests.")
    parser.add_argument("--query_config", default="config/web_image_queries.yaml")
    parser.add_argument("--manual_urls", default="config/manual_image_urls.yaml")
    parser.add_argument("--max_per_task", type=int, default=3)
    parser.add_argument("--task_ids", nargs="*", default=None)
    parser.add_argument("--overwrite", action="store_true")
    parser.add_argument("--dry_run", action="store_true")
    parser.add_argument("--search_limit", type=int, default=12)
    parser.add_argument("--request_sleep", type=float, default=0.5)
    return parser.parse_args()


def filter_tasks(tasks: list[dict[str, Any]], task_ids: list[str] | None) -> list[dict[str, Any]]:
    if not task_ids:
        return tasks
    selected = set(task_ids)
    return [task for task in tasks if task.get("task_id") in selected]


def load_optional_yaml(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {"tasks": []}
    return load_yaml(path)


def collect_for_task(task: dict[str, Any], manual_config: dict[str, Any], args: argparse.Namespace) -> list[dict[str, Any]]:
    task_id = str(task["task_id"])
    task_name = str(task.get("task_name", ""))
    folder = ROOT / str(task["folder"])
    folder.mkdir(parents=True, exist_ok=True)
    target = min(args.max_per_task, int(task.get("target_num_images", args.max_per_task)))
    existing = sorted(folder.glob("image_*.jpg"))
    if existing and not args.overwrite:
        remaining = max(target - len(existing), 0)
    else:
        remaining = target
    records: list[dict[str, Any]] = []
    if remaining <= 0:
        records.append(base_record(task, "", "", "", "", "", "skipped", "Target already satisfied; use --overwrite to replace."))
        return records

    next_index = 1 if args.overwrite else next_image_index(folder)
    downloaded = 0
    seen_urls: set[str] = set()

    for manual in manual_entries_for_task(manual_config, task_id):
        if downloaded >= remaining:
            break
        record, ok = try_download_candidate(
            task=task,
            candidate=manual_candidate(manual),
            local_path=folder / f"image_{next_index:02d}.jpg",
            search_query=str(manual.get("search_query", "manual_url")),
            why_selected=str(manual.get("why_selected", task.get("desired_scene", ""))),
            overwrite=args.overwrite,
        )
        records.append(record)
        if ok:
            downloaded += 1
            next_index += 1
            seen_urls.add(str(manual.get("source_url", "")))

    for query in task.get("queries", []):
        if downloaded >= remaining:
            break
        candidates: list[dict[str, Any]] = []
        try:
            candidates.extend(search_commons(str(query), args.search_limit))
        except Exception as exc:  # noqa: BLE001
            records.append(base_record(task, "", "", "", "", str(query), "error", f"Wikimedia Commons search failed: {exc}"))
        time.sleep(args.request_sleep)
        try:
            candidates.extend(search_openverse(str(query), args.search_limit))
        except Exception as exc:  # noqa: BLE001
            records.append(base_record(task, "", "", "", "", str(query), "error", f"Openverse search failed: {exc}"))
        if not candidates:
            continue
        for candidate in candidates:
            if downloaded >= remaining:
                break
            source_url = str(candidate.get("source_url", ""))
            if not source_url or source_url in seen_urls:
                continue
            seen_urls.add(source_url)
            record, ok = try_download_candidate(
                task=task,
                candidate=candidate,
                local_path=folder / f"image_{next_index:02d}.jpg",
                search_query=str(query),
                why_selected=str(task.get("desired_scene", "")),
                overwrite=args.overwrite,
            )
            records.append(record)
            if ok:
                downloaded += 1
                next_index += 1

    if downloaded < remaining:
        records.append(base_record(task, "", "", "", "", "", "skipped", f"Only downloaded {downloaded}/{remaining} requested images."))
    print(f"{task_id}: downloaded {downloaded}/{remaining}")
    return records


def search_commons(query: str, limit: int) -> list[dict[str, Any]]:
    params = {
        "action": "query",
        "format": "json",
        "generator": "search",
        "gsrsearch": query,
        "gsrnamespace": "6",
        "gsrlimit": str(limit),
        "prop": "imageinfo",
        "iiprop": "url|mime|size|extmetadata",
        "iiurlwidth": "1280",
        "origin": "*",
    }
    payload = fetch_json(f"{COMMONS_API}?{urllib.parse.urlencode(params)}")
    pages = payload.get("query", {}).get("pages", {})
    candidates: list[dict[str, Any]] = []
    for page in pages.values():
        infos = page.get("imageinfo") or []
        if not infos:
            continue
        info = infos[0]
        mime = info.get("mime", "")
        if mime not in SUPPORTED_MIME:
            continue
        ext = info.get("extmetadata", {}) or {}
        candidates.append(
            {
                "source_url": info.get("thumburl") or info.get("url", ""),
                "page_url": info.get("descriptionurl", ""),
                "license": ext_value(ext, "LicenseShortName") or ext_value(ext, "UsageTerms"),
                "author": strip_html(ext_value(ext, "Artist") or ext_value(ext, "Credit")),
                "original_filename": page.get("title", "").replace("File:", ""),
                "mime": mime,
                "width": info.get("width"),
                "height": info.get("height"),
            }
        )
    return candidates


def search_openverse(query: str, limit: int) -> list[dict[str, Any]]:
    params = {
        "q": query,
        "page_size": str(limit),
    }
    payload = fetch_json(f"{OPENVERSE_API}?{urllib.parse.urlencode(params)}")
    candidates: list[dict[str, Any]] = []
    for item in payload.get("results", []):
        source_url = item.get("url", "")
        if not source_url:
            continue
        candidates.append(
            {
                "source_url": source_url,
                "page_url": item.get("foreign_landing_url") or item.get("url", ""),
                "license": item.get("license") or "",
                "author": item.get("creator") or "",
                "original_filename": item.get("title") or Path(urllib.parse.urlparse(source_url).path).name,
                "mime": "",
                "width": item.get("width"),
                "height": item.get("height"),
            }
        )
    return candidates


def fetch_json(url: str) -> dict[str, Any]:
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(request, timeout=20) as response:
        return json.loads(response.read().decode("utf-8"))


def try_download_candidate(
    task: dict[str, Any],
    candidate: dict[str, Any],
    local_path: Path,
    search_query: str,
    why_selected: str,
    overwrite: bool,
) -> tuple[dict[str, Any], bool]:
    if local_path.exists() and not overwrite:
        return (
            metadata_record(task, local_path, candidate, search_query, why_selected, "skipped", "Local file exists; use --overwrite."),
            False,
        )
    try:
        with tempfile.NamedTemporaryFile(suffix=".img", delete=True) as tmp:
            download_file(str(candidate["source_url"]), Path(tmp.name))
            process_image(Path(tmp.name), local_path)
        return metadata_record(task, local_path, candidate, search_query, why_selected, "downloaded", "Temporary web image for internal smoke test; manual review required."), True
    except Exception as exc:  # noqa: BLE001
        return metadata_record(task, local_path, candidate, search_query, why_selected, "error", str(exc)), False


def download_file(url: str, output_path: Path) -> None:
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            content_type = response.headers.get("Content-Type", "").split(";")[0].strip().lower()
            if content_type and content_type not in SUPPORTED_MIME:
                raise ValueError(f"Unsupported content type: {content_type}")
            output_path.write_bytes(response.read())
    except urllib.error.HTTPError as exc:
        raise ValueError(f"Download failed with HTTP {exc.code}") from exc


def process_image(input_path: Path, output_path: Path) -> None:
    with Image.open(input_path) as image:
        width, height = image.size
        if width < MIN_SIDE or height < MIN_SIDE:
            raise ValueError(f"Image too small: {width}x{height}")
        image = image.convert("RGB")
        longest = max(width, height)
        if longest > MAX_LONG_SIDE:
            scale = MAX_LONG_SIDE / float(longest)
            new_size = (int(width * scale), int(height * scale))
            image = image.resize(new_size, Image.Resampling.LANCZOS)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        image.save(output_path, format="JPEG", quality=88, optimize=True)


def next_image_index(folder: Path) -> int:
    indices: list[int] = []
    for path in folder.glob("image_*.jpg"):
        try:
            indices.append(int(path.stem.split("_")[-1]))
        except ValueError:
            continue
    return max(indices, default=0) + 1


def manual_entries_for_task(config: dict[str, Any], task_id: str) -> list[dict[str, Any]]:
    entries: list[dict[str, Any]] = []
    for task in config.get("tasks", []):
        if task.get("task_id") == task_id:
            entries.extend(task.get("urls", []))
    return entries


def manual_candidate(entry: dict[str, Any]) -> dict[str, Any]:
    return {
        "source_url": entry.get("source_url", ""),
        "page_url": entry.get("page_url", entry.get("source_url", "")),
        "license": entry.get("license", ""),
        "author": entry.get("author", ""),
        "original_filename": entry.get("original_filename", Path(str(entry.get("source_url", ""))).name),
        "mime": "",
        "width": "",
        "height": "",
    }


def metadata_record(
    task: dict[str, Any],
    local_path: Path,
    candidate: dict[str, Any],
    search_query: str,
    why_selected: str,
    status: str,
    notes: str,
) -> dict[str, Any]:
    return {
        "task_id": task.get("task_id", ""),
        "task_name": task.get("task_name", ""),
        "local_path": str(local_path.relative_to(ROOT)) if str(local_path) else "",
        "source_url": candidate.get("source_url", ""),
        "page_url": candidate.get("page_url", ""),
        "license": candidate.get("license", ""),
        "author": candidate.get("author", ""),
        "original_filename": candidate.get("original_filename", ""),
        "download_time": now_iso(),
        "search_query": search_query,
        "why_selected": why_selected,
        "status": status,
        "notes": notes,
    }


def base_record(
    task: dict[str, Any],
    local_path: str,
    source_url: str,
    page_url: str,
    license_name: str,
    search_query: str,
    status: str,
    notes: str,
) -> dict[str, Any]:
    return {
        "task_id": task.get("task_id", ""),
        "task_name": task.get("task_name", ""),
        "local_path": local_path,
        "source_url": source_url,
        "page_url": page_url,
        "license": license_name,
        "author": "",
        "original_filename": "",
        "download_time": now_iso(),
        "search_query": search_query,
        "why_selected": task.get("desired_scene", ""),
        "status": status,
        "notes": notes,
    }


def write_reports(metadata_dir: Path, records: list[dict[str, Any]], tasks: list[dict[str, Any]]) -> None:
    by_task: dict[str, list[dict[str, Any]]] = {}
    for record in records:
        by_task.setdefault(str(record.get("task_id", "")), []).append(record)

    summary_lines = [
        "# Web Image Collection Summary",
        "",
        "Temporary web images are for internal smoke tests only. Do not treat them as final benchmark data without manual license and quality review.",
        "",
        "| Task | Downloaded | Skipped | Errors |",
        "| --- | ---: | ---: | ---: |",
    ]
    checklist_lines = [
        "# Manual Review Checklist",
        "",
        "Downloaded images are temporary smoke-test assets. Check every item before using it in any report, paper, or public release.",
        "",
    ]
    for task in tasks:
        task_id = str(task.get("task_id", ""))
        rows = by_task.get(task_id, [])
        summary_lines.append(
            f"| {task_id} | {count_status(rows, 'downloaded')} | {count_status(rows, 'skipped')} | {count_status(rows, 'error')} |"
        )
        checklist_lines.append(f"## {task_id}_{task.get('task_name', '')}")
        downloaded = [row for row in rows if row.get("status") == "downloaded"]
        if not downloaded:
            checklist_lines.append("- [ ] No downloaded images yet; user may need to add real robot-view photos or manual URLs.")
        for row in downloaded:
            checklist_lines.extend(
                [
                    f"- [ ] {Path(str(row.get('local_path', ''))).name}",
                    f"  - Source: {row.get('page_url') or row.get('source_url')}",
                    f"  - License: {row.get('license') or 'unknown'}",
                    f"  - Author: {row.get('author') or 'unknown'}",
                    "  - Check: realistic robot-view? no face? no watermark? no large text/logo? task-relevant objects visible?",
                ]
            )
        checklist_lines.append("")
    (metadata_dir / "web_images_summary.md").write_text("\n".join(summary_lines) + "\n", encoding="utf-8")
    (metadata_dir / "manual_review_checklist.md").write_text("\n".join(checklist_lines) + "\n", encoding="utf-8")


def count_status(rows: list[dict[str, Any]], status: str) -> int:
    return sum(1 for row in rows if row.get("status") == status)


def ext_value(ext: dict[str, Any], key: str) -> str:
    value = ext.get(key, {})
    if isinstance(value, dict):
        return str(value.get("value", ""))
    return str(value or "")


def strip_html(text: str) -> str:
    output = []
    in_tag = False
    for char in text:
        if char == "<":
            in_tag = True
            continue
        if char == ">":
            in_tag = False
            continue
        if not in_tag:
            output.append(char)
    return " ".join("".join(output).split())


def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


if __name__ == "__main__":
    raise SystemExit(main())
