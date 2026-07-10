# Pair Construction Final Review

## Completed

- 完成 `curated pool -> AHD paired dataset`：唯一输入 image pool 为 `data/curated_pools/ahd_cosmos3_raw240_qwen32`。
- Stage1 导出 101 个 curated O0 search-trigger 样本：38 aggregate transport、32 extend reach、31 direct-is-enough。
- Stage2 以 99 个 curated O1 image 为 group，每个 O1 配三个 O0 task-family memory，共 297 个 helper-grounding 样本。
- Stage2 gold 分布为 66 `helper_found`、132 `continue_search`、99 `direct_is_enough`。wrong-helper 由 O0 needed function 与 O1 helper function 不匹配得到；direct O0 不因 O1 出现物体而改变。
- test evaluation 包含 21 个 same-O1/different-O0 groups、28 个 wrong-helper cases 和 21 个 no-tool controls。
- O1 按 spec type 做确定性 group split：69 train / 9 val / 21 test groups，对应 207 / 27 / 63 个 Stage2 rows。train、val、test 的 O1 id 两两交集均为零。
- checker 验证 JSON 结构、标签推导、relation、路径存在、curated provenance、reject contamination、evaluation/master 一致性和 same-O1 leakage。
- scene spec gold 未修改。direct 的源 mode `direct` 仅在 pair adapter 输出时规范化为 `direct_is_enough`。
- raw run、VLM judge、curated pool 三层目录与生命周期未修改；没有运行 Cosmos3、VLM judge、训练或推理。

## Remaining Issues

- 无阻塞实现问题。当前 paired dataset 是本地生成 artifact，需随输入 curated pool 和构造脚本一起进行版本冻结或记录校验和，才能保证后续实验完全可复现。
- `semantic_keep` 来自自动 VLM triage；在正式论文评测前仍需要对 test evaluation 做人工视觉复核，但不应在复核时改写 scene spec gold。

## Potential Research Risks

- curated 文件名包含 `container_o1`、`longtool_o1`、`agg_o0` 等语义前缀。评测程序若向模型暴露路径文本会产生 label leakage；只应传图像内容和规定字段。
- 同 split 内会复用 O0 target memory。置信区间和显著性分析应按 O1 image group 处理，而不是把 297 rows 假设为完全独立样本。
- wrong-helper label 基于预定义 helper function。视觉上含糊或具有替代 affordance 的物体可能使组合标签与人类判断不一致。
- same-O1 groups 中 wrong-helper O1 没有 `helper_found` case，但仍包含两个 `continue_search` case 和一个 direct control。分析时应按 O1 spec type 分层报告。
- instruction 和 target memory 本身揭示任务需求，这是 benchmark 输入设计的一部分；不得额外暴露 `o0_spec_id`、`o1_spec_type`、文件名或 gold 字段给被测模型。

## Recommended Next Step

冻结 `ahd_v01` 的构造配置和文件校验和，对 test 的 21 张共享 O1 图像及其 63 个 case 做盲法人工审计，重点标记视觉 affordance 歧义和路径/metadata 暴露。审计通过后再实现只传规定模型输入字段的 evaluation loader；本阶段不进入训练。
