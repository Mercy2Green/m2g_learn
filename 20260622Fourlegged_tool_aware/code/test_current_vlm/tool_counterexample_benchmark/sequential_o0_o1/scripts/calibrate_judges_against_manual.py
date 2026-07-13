from __future__ import annotations
import argparse,csv,json
from collections import defaultdict
from pathlib import Path
from typing import Any
def load(path:Path)->list[dict[str,Any]]:
    if path.suffix==".jsonl":return[json.loads(x)for x in path.read_text(encoding="utf-8").splitlines()if x.strip()]
    with path.open(encoding="utf-8-sig",newline="")as f:return list(csv.DictReader(f))
def key(r:dict[str,Any])->tuple[str,str,str]:return(str(r.get("sample_id","")),str(r.get("prompt_id","")),str(r.get("model_id","ollama_qwen3_5_35b")))
def manual_label(r:dict[str,Any])->str:
    for k in("manual_pass_fail","pass_fail_manual","manual_judge_decision","manual_label","pass_fail","judge_decision"):
        v=str(r.get(k,"")).strip().lower()
        if v in{"pass","fail","needs_review","excluded"}:return v
    return ""
def compare(manual:list[dict[str,Any]],pred:list[dict[str,Any]],field:str)->list[dict[str,Any]]:
    p={key(r):r for r in pred};out=[]
    for m in manual:
        q=p.get(key(m),{});ml=manual_label(m);pl=str(q.get(field,""));out.append({**{k:m.get(k,"")for k in("sample_id","sample_type","protocol","prompt_id","prompt_family","model_id")},"manual":ml,"predicted":pl,"agreement":ml==pl,"false_positive":ml=="fail"and pl=="pass","false_negative":ml=="pass"and pl=="fail"})
    return out
def write(path:Path,rows:list[dict[str,Any]])->None:
    fields=list(rows[0])if rows else["sample_id","manual","predicted","agreement"]
    with path.open("w",encoding="utf-8",newline="")as f:w=csv.DictWriter(f,fieldnames=fields,extrasaction="ignore");w.writeheader();w.writerows(rows)
def main()->None:
    p=argparse.ArgumentParser();p.add_argument("--manual");p.add_argument("--text",required=True);p.add_argument("--vlm",required=True);p.add_argument("--final",required=True);p.add_argument("--output_dir",required=True);a=p.parse_args();out=Path(a.output_dir);out.mkdir(parents=True,exist_ok=True)
    manual=Path(a.manual)if a.manual else next(Path.cwd().rglob("qwen35_all_204_prompt_level_manual_review.csv"),None)
    if not manual or not manual.is_file():
        for name in ("text_v3_vs_manual.csv","vlm_v4_vs_manual.csv","final_v4_vs_manual.csv","per_task_protocol_metrics.csv"):
            (out/name).write_text("sample_id,manual,predicted,agreement\n",encoding="utf-8")
        for name,title in (("false_positive_cases.md","False positives"),("false_negative_cases.md","False negatives"),("disagreement_review_pack.md","Disagreement review pack")):
            (out/name).write_text(f"# {title}\n\nUnavailable: manual CSV was not found.\n",encoding="utf-8")
        (out/"calibration_summary.md").write_text("# Judge Calibration\n\nCalibration stopped: `qwen35_all_204_prompt_level_manual_review.csv` was not found. No manual labels were fabricated.\n",encoding="utf-8");print("manual calibration CSV not found");return
    m=load(manual);sets=[("text_v3_vs_manual.csv",compare(m,load(Path(a.text)),"pass_fail")),("vlm_v4_vs_manual.csv",compare(m,load(Path(a.vlm)),"judge_decision")),("final_v4_vs_manual.csv",compare(m,load(Path(a.final)),"final_pass_fail"))]
    for name,rows in sets:write(out/name,rows)
    final=sets[-1][1];valid=[r for r in final if r["manual"]in{"pass","fail"}and r["predicted"]in{"pass","fail"}];agreement=sum(r["agreement"]for r in valid)/len(valid)if valid else 0
    fps=[r for _,rs in sets for r in rs if r["false_positive"]];fns=[r for _,rs in sets for r in rs if r["false_negative"]]
    (out/"false_positive_cases.md").write_text("# False positives\n\n"+"\n".join(f"- {r['sample_id']} {r['prompt_id']}"for r in fps)+"\n",encoding="utf-8");(out/"false_negative_cases.md").write_text("# False negatives\n\n"+"\n".join(f"- {r['sample_id']} {r['prompt_id']}"for r in fns)+"\n",encoding="utf-8");(out/"disagreement_review_pack.md").write_text("# Disagreements\n\n"+"\n".join(f"- {r['sample_id']} {r['manual']} vs {r['predicted']}"for r in final if not r["agreement"])+"\n",encoding="utf-8")
    groups=defaultdict(list)
    for r in final:groups[(r["sample_type"],r["protocol"])].append(r)
    per=[]
    for(k1,k2),rs in groups.items():per.append({"task":k1,"protocol":k2,"rows":len(rs),"agreement":sum(x["agreement"]for x in rs)/len(rs)})
    write(out/"per_task_protocol_metrics.csv",per);(out/"calibration_summary.md").write_text(f"# Judge Calibration\n\n- manual rows: {len(m)}\n- final comparable rows: {len(valid)}\n- final agreement: {agreement:.3%}\n- final false positives: {sum(r['false_positive']for r in final)}\n- final false negatives: {sum(r['false_negative']for r in final)}\n",encoding="utf-8")
if __name__=="__main__":main()
