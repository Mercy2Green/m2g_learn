from __future__ import annotations
import argparse, csv, hashlib, json, os, sys
from collections import Counter
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]; sys.path.insert(0, str(ROOT))
from src.load_config import load_dotenv  # noqa: E402
from src.providers.ollama_provider import OllamaProvider  # noqa: E402
from src.response_parser import parse_model_response  # noqa: E402

VERSION = "task_image_audit_v2"
FIELDS = ["image_path","image_sha256","image_role","visible_objects","target_category","target_count_estimate","candidate_helper_present","candidate_helper_type","candidate_helper_visibility","candidate_helper_function","wrong_object_present","image_quality","audit_confidence","audit_overridden","audit_override_reason"]
DEFAULT_OVERRIDE = {"match_basename":"container_o1_000001.jpg","candidate_helper_present":"yes","candidate_helper_type":"baking_tray","candidate_helper_visibility":"clear","candidate_helper_function":"container_for_multiple_objects","audit_confidence":"high","audit_override_reason":"Authoritative manual fact: clear baking tray / tray suitable for container_for_multiple_objects."}

def resolve(value: str) -> Path:
    p=Path(value); return p.resolve() if p.is_absolute() else (ROOT/p).resolve()
def sha(path: Path) -> str:
    h=hashlib.sha256()
    with path.open("rb") as f:
        for b in iter(lambda:f.read(1024*1024), b""): h.update(b)
    return h.hexdigest()
def read_jsonl(path: Path) -> list[dict[str,Any]]:
    return [json.loads(x) for x in path.read_text(encoding="utf-8").splitlines() if x.strip()]
def unique_images(rows: list[dict[str,Any]]) -> list[dict[str,str]]:
    found={}
    for row in rows:
        for role,key in (("o0","o0_image_path"),("o1","o1_image_path")):
            path=resolve(str(row[key])); ident=(str(path),sha(path)); rec={"image_path":str(row[key]),"resolved_image_path":str(path),"image_sha256":ident[1],"image_role":role}
            if ident in found and found[ident]["image_role"] != role: raise ValueError(f"Image has conflicting roles: {path}")
            found[ident]=rec
    return [found[k] for k in sorted(found)]
def defaults(rec: dict[str,str]) -> dict[str,Any]:
    return {"audit_version":VERSION,**rec,"audit_status":"error","audit_error":"","audit_raw_response":"","visible_objects":[],"target_category":"unclear","target_count_estimate":"unclear","candidate_helper_present":"unclear","candidate_helper_type":"unclear","candidate_helper_visibility":"ambiguous","candidate_helper_function":"unclear","wrong_object_present":"unclear","image_quality":"ambiguous","audit_confidence":"low","audit_overridden":False,"audit_override_reason":""}
def apply_override(row: dict[str,Any], overrides: list[dict[str,Any]]) -> None:
    ov=next((x for x in overrides if x.get("match_basename")==Path(row["image_path"]).name),None)
    if ov:
        row.update({k:v for k,v in ov.items() if k!="match_basename"}); row["audit_overridden"]=True
def audit_one(provider: Any, rec: dict[str,str], prompt: str, overrides: list[dict[str,Any]]) -> dict[str,Any]:
    row=defaults(rec)
    try:
        result=provider.run_chat_with_retry([{"role":"system","content":prompt},{"role":"user","content":json.dumps({"image_role":rec["image_role"],"image_path":rec["image_path"]},ensure_ascii=False),"images":[rec["resolved_image_path"]]}])
        row["audit_raw_response"]=str(result.get("raw_response","")); parsed=parse_model_response(row["audit_raw_response"])
        if parsed["parse_status"]!="ok": raise ValueError(parsed["parse_error"])
        for key in FIELDS[3:13]:
            if key in parsed["parsed"]: row[key]=parsed["parsed"][key]
        if not isinstance(row["visible_objects"],list): raise ValueError("visible_objects must be a list")
        row["audit_status"]="ok"
    except Exception as exc: row["audit_error"]=str(exc)
    apply_override(row,overrides); return row
def write_jsonl(path:Path,rows:list[dict[str,Any]]) -> None:
    with path.open("w",encoding="utf-8") as f:
        for r in rows:f.write(json.dumps(r,ensure_ascii=False,sort_keys=True)+"\n")
def main() -> None:
    p=argparse.ArgumentParser();p.add_argument("--input_dir",required=True);p.add_argument("--output_dir");p.add_argument("--audit_model",default="qwen3-vl:32b-instruct-q4_K_M");p.add_argument("--limit",type=int);p.add_argument("--overwrite",action="store_true");p.add_argument("--dry_run",action="store_true");a=p.parse_args()
    load_dotenv(ROOT/".env"); inp=Path(a.input_dir).resolve();out=Path(a.output_dir).resolve() if a.output_dir else inp/"task_image_audit_v2"
    if out.exists() and not a.overwrite: raise SystemExit(f"Output exists: {out}")
    out.mkdir(parents=True,exist_ok=True); override_path=out/"manual_image_fact_overrides.jsonl"; overrides=read_jsonl(override_path) if override_path.exists() else []
    by={x.get("match_basename"):x for x in overrides};by.setdefault(DEFAULT_OVERRIDE["match_basename"],DEFAULT_OVERRIDE);overrides=list(by.values());write_jsonl(override_path,overrides)
    images=unique_images(read_jsonl(inp/"raw_responses.jsonl"));images=images[:a.limit] if a.limit else images
    provider=None if a.dry_run else OllamaProvider({"model_id":"task_image_audit_v2","model_name":a.audit_model,"provider_label":"ollama_task_image_audit_v2","base_url":os.environ.get("OLLAMA_BASE_URL","http://localhost:11434"),"temperature":0.0,"max_tokens":768,"num_ctx":8192,"timeout_seconds":420,"retries":1,"format_json":True,"keep_alive":"10m"})
    prompt=(ROOT/"sequential_o0_o1/prompts/image_audit_v2.txt").read_text(encoding="utf-8")
    rows=[]
    for i,rec in enumerate(images,1):
        row=defaults(rec) if a.dry_run else audit_one(provider,rec,prompt,overrides);apply_override(row,overrides);rows.append(row);print(f"audit {i}/{len(images)} {Path(rec['image_path']).name} {row['audit_status']}",flush=True)
    write_jsonl(out/"image_fact_catalog.jsonl",rows)
    with (out/"image_fact_catalog.csv").open("w",encoding="utf-8",newline="") as f:
        w=csv.DictWriter(f,fieldnames=FIELDS,extrasaction="ignore");w.writeheader();w.writerows(rows)
    c=Counter(r["audit_status"] for r in rows);(out/"image_audit_summary.md").write_text(f"# Image Fact Audit V2\n\n- unique images: {len(rows)}\n- ok: {c['ok']}\n- errors: {c['error']}\n- overrides: {sum(bool(r['audit_overridden']) for r in rows)}\n\nEach call receives one image; no candidate response or cross-image reasoning is used.\n",encoding="utf-8")
    low=[r for r in rows if r["audit_confidence"]=="low" or r["image_quality"] in {"ambiguous","bad"}];(out/"low_confidence_images.md").write_text("# Low-confidence images\n\n"+"\n".join(f"- {r['image_path']}: {r['audit_error'] or r['image_quality']}" for r in low)+"\n",encoding="utf-8")
if __name__=="__main__":main()
