import json
from pathlib import Path
import sys
import unittest
ROOT=Path(__file__).resolve().parents[2];sys.path.insert(0,str(ROOT))
from src.load_config import load_yaml
from sequential_o0_o1.text_evaluator_v3 import evaluate_raw
from sequential_o0_o1.scripts.audit_task_images_v2 import apply_override,DEFAULT_OVERRIDE
from sequential_o0_o1.scripts.adjudicate_sequential_evaluation_v4 import adjudicate
CFG=load_yaml(ROOT/"sequential_o0_o1/configs/evaluator_v3.yaml");VALID=load_yaml(ROOT/"sequential_o0_o1/configs/model_protocol_validity.yaml")
AUDIT={"candidate_helper_present":"yes","candidate_helper_function":"container_for_multiple_objects"}
def raw(plan,sample="positive_aggregate",source="task_002",model="ollama_qwen3_5_35b",protocol="two_turn_sequential"):
    response={"task_understanding":"搬运原先看到的多瓶水","plan":plan,"tool_use_action_chain":plan,"selected_helper":"托盘" if "托盘" in "".join(plan) else "","helper_needed":"yes","uncertainty_or_missing_information":"","reason":""}
    return{"sample_id":"x","sample_type":sample,"old_task_id_source":source,"model_id":model,"protocol":protocol,"prompt_id":"p","raw_response_final":json.dumps(response,ensure_ascii=False)}
def ev(plan,**kw):return evaluate_raw(raw(plan,**kw),CFG,VALID,AUDIT)
class Rules(unittest.TestCase):
    def test_01_explicit_chain(self):self.assertEqual(ev(["把多瓶水放入托盘","用托盘把这些水运送到卧室"])["pass_fail"],"pass")
    def test_02_helper_multiple_trips(self):self.assertEqual(ev(["分两次把水瓶放入托盘","每次用托盘运送所装水瓶"])["action_mode_pred"],"physical_o1_helper_chain")
    def test_03_conditional(self):self.assertEqual(ev(["如果托盘可用，将水放入托盘并用它运送"])["action_mode_pred"],"conditional_helper_only")
    def test_04_mention_only(self):self.assertEqual(ev(["看到托盘，继续规划搬运"])["action_mode_pred"],"helper_mention_without_chain")
    def test_05_dual_arm(self):self.assertEqual(ev(["用双臂一次拿多瓶水送到卧室"])["action_mode_pred"],"embodiment_batching")
    def test_06_direct_trips(self):self.assertEqual(ev(["逐个拿水瓶，多次往返送到卧室"])["action_mode_pred"],"direct_multi_trip")
    def test_07_search_seen_target(self):self.assertEqual(ev(["在新区域寻找水瓶"],sample="no_tool_control",source="task_011")["task_state_update"],"overwritten")
    def test_08_premature(self):self.assertEqual(ev(["任务已经完成"],sample="no_tool_control",source="task_011")["action_mode_pred"],"premature_task_completion")
    def test_09_wrong_ignored(self):self.assertEqual(ev(["返回原处直接拿水瓶"],sample="wrong_helper_negative")["pass_fail"],"pass")
    def test_10_wrong_used(self):self.assertEqual(ev(["把水放到台灯上，用台灯搬运水瓶"],sample="wrong_helper_negative")["action_mode_pred"],"wrong_helper_use")
    def test_11_pencil_bookkeeping(self):self.assertEqual(ev(["直接搬水，每完成一批移动铅笔作计数标记"],sample="wrong_helper_negative")["helper_role"],"incidental_bookkeeping")
    def test_12_phone_contamination(self):self.assertEqual(ev(["把手机也加入目标物，与水瓶一起送走"],sample="wrong_helper_negative")["action_mode_pred"],"target_set_contamination")
    def test_13_empty(self):self.assertEqual(evaluate_raw({**raw([]),"raw_response_final":""},CFG,VALID,AUDIT)["failure_type"],"empty_or_error_response")
    def test_14_manual_override(self):
        row={"image_path":"x/container_o1_000001.jpg","candidate_helper_present":"no","audit_overridden":False};apply_override(row,[DEFAULT_OVERRIDE]);self.assertTrue(row["audit_overridden"]);self.assertEqual(row["candidate_helper_visibility"],"clear")
    def test_15_invalid_ingestion(self):
        text=evaluate_raw(raw([],protocol="single_turn_multi_image"),CFG,VALID,AUDIT);self.assertEqual(text["pass_fail"],"excluded");self.assertEqual(adjudicate(text,None)["final_status"],"excluded")
if __name__=="__main__":unittest.main()
