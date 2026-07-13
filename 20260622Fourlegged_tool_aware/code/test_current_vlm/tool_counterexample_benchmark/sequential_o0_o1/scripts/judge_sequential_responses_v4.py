from __future__ import annotations
import argparse,csv,json,os,sys
from collections import Counter
from pathlib import Path
from typing import Any
ROOT=Path(__file__).resolve().parents[2];sys.path.insert(0,str(ROOT))
from sequential_o0_o1.text_evaluator_v3 import protocol_validity  # noqa:E402
from src.load_config import load_dotenv,load_yaml  # noqa:E402
from src.providers.ollama_provider import OllamaProvider  # noqa:E402
from src.response_parser import parse_model_response  # noqa:E402
VERSION="strict_v4_task_state"
ENUM={"task_state_update":{"preserved","overwritten","contaminated","premature_complete","unclear"},"helper_commitment":{"committed","conditional","mentioned_only","none"},"helper_role":{"task_helper","incidental_bookkeeping","obstacle","irrelevant","none"},"action_mode_pred":{"physical_o1_helper_chain","conditional_helper_only","helper_mention_without_chain","embodiment_batching","direct_multi_trip","direct_single","continue_search","wrong_helper_use","target_set_contamination","o1_target_overwrite","premature_task_completion","unclear"},"links_o1_helper_to_o0_target":{"yes","no","unclear"},"target_set_preserved":{"yes","no","unclear"},"decision_pred":{"helper_found","direct_is_enough","continue_search","unclear"},"relation_pred":{"aggregate_transport","reach_extension","none","unclear"},"judge_decision":{"pass","fail","needs_review","excluded"},"judge_confidence":{"high","medium","low"}}
def read(path:Path)->list[dict[str,Any]]:return [json.loads(x) for x in path.read_text(encoding="utf-8").splitlines() if x.strip()]
def key(r:dict[str,Any])->tuple[str,str,str]:return(str(r.get("sample_id","")),str(r.get("prompt_id","")),str(r.get("model_id","")))
def stratified(rows:list[dict[str,Any]],limit:int|None)->list[dict[str,Any]]:
    if not limit:return rows
    groups={}
    for r in rows:groups.setdefault((str(r.get("sample_type")),str(r.get("protocol"))),[]).append(r)
    chosen=[]
    while len(chosen)<limit and any(groups.values()):
        for k in sorted(groups):
            if groups[k] and len(chosen)<limit:chosen.append(groups[k].pop(0))
    return chosen
def validate(x:dict[str,Any])->dict[str,Any]:
    if x.get("judge_version")!=VERSION:raise ValueError("wrong judge_version")
    for k,vals in ENUM.items():
        if str(x.get(k,"")) not in vals:raise ValueError(f"invalid {k}={x.get(k)!r}")
    for k in ("selected_helper","failure_type","evidence_quote","reason"):
        x[k]=str(x.get(k,""))
    return x
def excluded(raw:dict[str,Any],validity:dict[str,Any])->str:
    v=protocol_validity(str(raw.get("model_id","")),str(raw.get("protocol","")),validity).get("validity","requires_ingestion_diagnostic")
    if raw.get("sample_type")=="positive_reach" or(raw.get("sample_type")=="same_o1_different_o0" and raw.get("old_task_id_source")=="task_008"):return "excluded_untrusted_image"
    return str(v)
def main()->None:
    p=argparse.ArgumentParser();p.add_argument("--input_dir",required=True);p.add_argument("--output_dir");p.add_argument("--image_audit_path",required=True);p.add_argument("--judge_model",default="qwen3-vl:32b-instruct-q4_K_M");p.add_argument("--limit",type=int);p.add_argument("--overwrite",action="store_true");a=p.parse_args();load_dotenv(ROOT/".env")
    inp=Path(a.input_dir).resolve();out=Path(a.output_dir).resolve() if a.output_dir else inp/"response_judge_qwen32_strict_v4_task_state"
    if out.exists() and not a.overwrite:raise SystemExit(f"Output exists: {out}")
    out.mkdir(parents=True,exist_ok=True);rows=stratified(read(inp/"raw_responses.jsonl"),a.limit);audits=read(Path(a.image_audit_path));audit_by_path={str(x.get("image_path")):x for x in audits};audit_by_name={Path(str(x.get("image_path"))).name:x for x in audits}
    validity=load_yaml(ROOT/"sequential_o0_o1/configs/model_protocol_validity.yaml");prompt=(ROOT/"sequential_o0_o1/prompts/vlm_response_judge_v4.txt").read_text(encoding="utf-8")
    provider=OllamaProvider({"model_id":"response_judge_v4","model_name":a.judge_model,"provider_label":"ollama_response_judge_v4","base_url":os.environ.get("OLLAMA_BASE_URL","http://localhost:11434"),"temperature":0.0,"max_tokens":1200,"num_ctx":12288,"timeout_seconds":420,"retries":1,"format_json":True,"keep_alive":"10m"});output=[]
    for i,raw in enumerate(rows,1):
        v=excluded(raw,validity);audit=audit_by_path.get(str(raw.get("o1_image_path"))) or audit_by_name.get(Path(str(raw.get("o1_image_path"))).name);base={k:raw.get(k,"") for k in("sample_id","sample_type","group_id","protocol","prompt_id","prompt_category","model_id","old_task_id_source","o1_image_path")};base.update(judge_version=VERSION,evaluation_validity=v,judge_status="excluded" if v!="valid" else "error",judge_error="")
        if v!="valid":base.update(task_state_update="unclear",helper_commitment="none",helper_role="none",action_mode_pred="unclear",selected_helper="",links_o1_helper_to_o0_target="unclear",target_set_preserved="unclear",decision_pred="unclear",relation_pred="unclear",judge_decision="excluded",failure_type=v,evidence_quote="",judge_confidence="high",reason="Excluded deterministically by protocol/image validity.")
        elif not audit:base.update(judge_decision="needs_review",judge_status="error",judge_error="Missing authoritative O1 audit")
        else:
            payload={"candidate_response":raw.get("raw_response_final",""),"instruction":raw.get("instruction",""),"gold_expectation":raw.get("gold",{}),"o0_target_memory":{"instruction":raw.get("instruction",""),"o0_spec_id":raw.get("o0_spec_id","")},"authoritative_o1_image_audit_facts":{k:audit.get(k) for k in ("image_path","image_sha256","visible_objects","target_category","target_count_estimate","candidate_helper_present","candidate_helper_type","candidate_helper_visibility","candidate_helper_function","wrong_object_present","image_quality","audit_confidence","audit_overridden","audit_override_reason")},"protocol_validity":protocol_validity(str(raw.get("model_id","")),str(raw.get("protocol","")),validity)}
            try:
                res=provider.run_chat_with_retry([{"role":"system","content":prompt},{"role":"user","content":json.dumps(payload,ensure_ascii=False,indent=2),"images":[str((ROOT/str(raw["o1_image_path"])).resolve())]}]);parsed=parse_model_response(str(res.get("raw_response","")))
                if parsed["parse_status"]!="ok":raise ValueError(parsed["parse_error"])
                base.update(validate(parsed["parsed"]));base["evaluation_validity"]="valid";base["judge_status"]="ok"
            except Exception as exc:base["judge_error"]=str(exc);base.setdefault("judge_decision","needs_review")
        output.append(base);print(f"judge {i}/{len(rows)} {base['sample_id']} {base['judge_status']}",flush=True)
    with(out/"response_vlm_judge_strict_v4_task_state.jsonl").open("w",encoding="utf-8")as f:
        for r in output:f.write(json.dumps(r,ensure_ascii=False,sort_keys=True)+"\n")
    fields=sorted({k for r in output for k in r});
    with(out/"response_vlm_judge_strict_v4_task_state.csv").open("w",encoding="utf-8",newline="")as f:w=csv.DictWriter(f,fieldnames=fields,extrasaction="ignore");w.writeheader();w.writerows(output)
    c=Counter(r.get("judge_decision") for r in output);(out/"response_vlm_judge_summary_strict_v4_task_state.md").write_text(f"# Strict V4 Task-State Judge\n\n- rows: {len(output)}\n- pass/fail/review/excluded: {c['pass']}/{c['fail']}/{c['needs_review']}/{c['excluded']}\n",encoding="utf-8")
if __name__=="__main__":main()
