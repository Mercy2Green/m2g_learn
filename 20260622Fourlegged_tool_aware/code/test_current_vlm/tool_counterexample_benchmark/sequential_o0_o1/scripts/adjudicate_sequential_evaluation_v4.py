from __future__ import annotations
import argparse,csv,json,sys
from collections import defaultdict
from pathlib import Path
from typing import Any
ROOT=Path(__file__).resolve().parents[2];sys.path.insert(0,str(ROOT))
def read(path:Path)->list[dict[str,Any]]:return [json.loads(x) for x in path.read_text(encoding="utf-8").splitlines() if x.strip()]
def key(r:dict[str,Any])->tuple[str,str,str]:return(str(r.get("sample_id","")),str(r.get("prompt_id","")),str(r.get("model_id","")))
def adjudicate(text:dict[str,Any],vlm:dict[str,Any]|None)->dict[str,Any]:
    validity=str(text.get("evaluation_validity","requires_ingestion_diagnostic"));base={k:text.get(k,"") for k in("sample_id","sample_type","group_id","model_id","protocol","prompt_id","prompt_category","old_task_id_source","task_state_update","action_mode_pred","parse_status")};base.update(evaluation_validity=validity,judge_missing=False)
    if validity in {"invalid_multi_image_ingestion","excluded_untrusted_image","requires_ingestion_diagnostic"}:return{**base,"final_status":"excluded","final_pass_fail":"excluded","final_failure_type":validity,"text_vlm_agreement":"not_applicable","requires_manual_review":False}
    t=str(text.get("pass_fail","needs_review"));v=str((vlm or{}).get("judge_decision","needs_review"));vok=bool(vlm)and vlm.get("judge_status")=="ok"
    if not vok:
        high=t in{"pass","fail"} and text.get("parse_status")=="ok" and text.get("action_mode_pred")!="unclear"
        return{**base,"final_status":"adjudicated" if high else "needs_review","final_pass_fail":t if high else "needs_review","final_failure_type":text.get("failure_type","") if high else "judge_missing","text_vlm_agreement":"judge_missing","requires_manual_review":not high,"judge_missing":True}
    if t==v and t in{"pass","fail"}:return{**base,"final_status":"adjudicated","final_pass_fail":t,"final_failure_type":text.get("failure_type","") or vlm.get("failure_type",""),"text_vlm_agreement":"agree","requires_manual_review":False}
    return{**base,"final_status":"needs_review","final_pass_fail":"needs_review","final_failure_type":"text_vlm_disagreement","text_vlm_agreement":"disagree","requires_manual_review":True}
def metric(sub:list[dict[str,Any]])->dict[str,Any]:
    valid=[r for r in sub if r["evaluation_validity"]=="valid"];attempted=[r for r in sub if r["evaluation_validity"]!="excluded_untrusted_image"];dec=[r for r in valid if r["final_pass_fail"] in{"pass","fail"}];helper=[r for r in valid if r["sample_type"]=="positive_aggregate" or(r["sample_type"]=="same_o1_different_o0"and r["old_task_id_source"]=="task_002")];direct=[r for r in valid if r["sample_type"]=="no_tool_control"or(r["sample_type"]=="same_o1_different_o0"and r["old_task_id_source"]=="task_011")];wrong=[r for r in valid if r["sample_type"]=="wrong_helper_negative"]
    rate=lambda n,d: n/d if d else ""
    pairs=defaultdict(dict)
    for r in valid:
        if r["sample_type"]=="same_o1_different_o0":pairs[(r["model_id"],r["prompt_id"],r["group_id"])][r["old_task_id_source"]]=r
    consistent=sum(x.get("task_002",{}).get("action_mode_pred")=="physical_o1_helper_chain" and x.get("task_011",{}).get("action_mode_pred")=="direct_single" and x.get("task_002",{}).get("final_pass_fail")=="pass" and x.get("task_011",{}).get("final_pass_fail")=="pass" for x in pairs.values())
    return{"rows":len(sub),"semantic_success_rate_over_valid_rows":rate(sum(r["final_pass_fail"]=="pass" for r in dec),len(dec)),"end_to_end_success_rate_over_attempted_rows":rate(sum(r["final_pass_fail"]=="pass" for r in attempted),len(attempted)),"invalid_ingestion_rate":rate(sum(r["evaluation_validity"]=="invalid_multi_image_ingestion" for r in sub),len(sub)),"helper_chain_rate_on_helper_required_rows":rate(sum(r["final_pass_fail"]=="pass" for r in helper),len(helper)),"direct_control_accuracy":rate(sum(r["final_pass_fail"]=="pass" for r in direct),len(direct)),"wrong_helper_rejection_rate":rate(sum(r["final_pass_fail"]=="pass" for r in wrong),len(wrong)),"task_state_preservation_rate":rate(sum(r["task_state_update"]=="preserved" for r in valid),len(valid)),"o1_target_overwrite_rate":rate(sum(r["task_state_update"]=="overwritten" for r in valid),len(valid)),"target_set_contamination_rate":rate(sum(r["task_state_update"]=="contaminated" for r in valid),len(valid)),"same_o1_aggregate_direct_consistency":rate(consistent,len(pairs)),"same_o1_reach_consistency":"excluded_untrusted_image","parse_success_rate":rate(sum(r["parse_status"]=="ok" for r in sub),len(sub)),"needs_review_rate":rate(sum(r["requires_manual_review"] for r in sub),len(sub))}
def main()->None:
    p=argparse.ArgumentParser();p.add_argument("--text",required=True);p.add_argument("--vlm",required=True);p.add_argument("--image_audit",required=True);p.add_argument("--validity_config",required=True);p.add_argument("--output_dir",required=True);a=p.parse_args();texts=read(Path(a.text));vlms={key(r):r for r in read(Path(a.vlm))};rows=[adjudicate(t,vlms.get(key(t))) for t in texts];out=Path(a.output_dir);out.mkdir(parents=True,exist_ok=True)
    with(out/"final_evaluation_v4.jsonl").open("w",encoding="utf-8")as f:
        for r in rows:f.write(json.dumps(r,ensure_ascii=False,sort_keys=True)+"\n")
    dimensions=[(),("model_id",),("sample_type",),("protocol",),("prompt_id",),("prompt_category",),("model_id","sample_type","protocol"),("model_id","sample_type","protocol","prompt_category")];metrics=[]
    for dims in dimensions:
        groups=defaultdict(list)
        for r in rows:groups[tuple(str(r.get(d,""))for d in dims)].append(r)
        for vals,sub in groups.items():metrics.append({"group_by":" × ".join(dims)or"overall","group":" × ".join(vals)or"all",**metric(sub)})
    fields=list(metrics[0]);
    with(out/"metrics_v4.csv").open("w",encoding="utf-8",newline="")as f:w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows(metrics)
    review=[r for r in rows if r["requires_manual_review"]];(out/"adjudication_summary.md").write_text(f"# Sequential Adjudication V4\n\n- rows: {len(rows)}\n- needs review: {len(review)}\n- excluded: {sum(r['final_status']=='excluded' for r in rows)}\n\nReach consistency remains unavailable/excluded until its image is trusted.\n",encoding="utf-8")
if __name__=="__main__":main()
