# Pair Construction Design Review

## 当前可复用字段

- `data/curated_pools/ahd_cosmos3_raw240_qwen32/curated_index.jsonl` 为每张保留图提供 `spec_id`、`spec_type`、`view_stage`、`curated_image_path`、`image_judge_status`、`keep` 和 raw run/judge 追溯信息。
- `specs/scene_specs_checked.jsonl` 可通过 `spec_id` 连接 curated row。O0 spec 提供 `task_family`、双语 instruction、robot context，以及确定性的 `gold.mode`、`gold.needed_helper_function` 和 `gold.target_memory`。
- O1 spec 提供 `helper_candidates_gold`（helper name/function）和 `pairing_role`；O1 本身刻意没有最终 pair gold，因为其正确性取决于 O0 memory。
- judge 输出明确区分 `semantic_keep` 与 `semantic_reject`。curated pool 当前包含 200 个 `semantic_keep` row：101 个 O0、99 个 O1。
- enrichment metadata 只改写文本和图像 prompt，不含 gold。pair construction 不需要用 enrichment 恢复标签。

## 缺失字段

- curated index 不直接包含 `task_family`、instruction、target memory、helper name/function 或最终 pair label。
- scene spec 的 direct O0 mode 为 `direct`，而 AHD pair export v0.1 要求 `direct_is_enough`。
- 现有数据没有 pair id、O1 group split 或 pair-level relation。
- curated 文件名包含 spec type 前缀，若模型能看到原始路径字符串会造成标签线索；图像内容本身不受此阶段修改。

以上字段通过只读 adapter 从 checked spec 恢复和规范化，不修改 curated index 或 scene spec 格式。

## Pair Construction 设计

- Stage1 对每个 curated O0 导出一个 `search_trigger` 样本。gold 直接来自 scene spec，仅把 `direct` 规范化为导出枚举 `direct_is_enough`。
- Stage2 以 curated O1 image 为 group。每个 O1 确定性配三个 O0 memory（aggregate、extend-reach、direct），得到约 300 个样本，并覆盖 helper-found、function mismatch/continue-search 和 no-tool control。
- Pair gold 由两个只读事实决定：O0 所需 helper function 与 O1 candidate helper function。function 相同则 `helper_found`；direct O0 始终 `direct_is_enough`；其余为 `continue_search`。
- O1 按 spec type 做确定性的分层 70/10/20 group split。O0 也按 task family 分层，Stage2 只在相同 split 内选 memory。builder assert train/val/test 的 O1 id 两两不相交。
- `same_o1_different_o0`、`wrong_helper` 和 `no_tool_control` 只导出 test O1 groups。主 Stage2 JSONL 保留 `split`、`o0_spec_id` 和 `o1_spec_id`，便于审计。
- 输出只引用 curated image path，不复制、重命名或修改图像，也不更改 raw run、judge 或 curated pool lifecycle。

## 风险

- VLM judge 是自动 triage；`semantic_keep` 不等同于人工确认的 benchmark gold，仍可能有视觉语义误判。
- 原始 curated 路径中的 `agg_o0`、`container_o1` 等名称可能对读取路径文本的模型产生 label leakage。评测接口应只向模型传图像字节，不暴露文件名。
- 同一个有限 O0 memory 会在同一 split 内被多个 O1 group 复用；统计分析应按 O1 group bootstrap，并报告复用。
- wrong-helper 是基于 spec helper function 的组合标签，不是对每张图片重新做视觉 affordance 标注；模糊物体仍可能具有意外用途。
- 当前数据规模只支持 v0.1 construction/validation，不应据此宣称跨场景泛化。
