# 策略文档

## 1. 题目理解

大模型 Steering 行为调控任务。不是 prompt-only 任务，必须通过内部激活干预或 Steering 向量控制模型输出目标行为。

## 2. 数据类型判断

LLM paired preference 数据，包含 concept、question、matching、not_matching。

## 3. 评测指标解释

三维评分：Concept Score、Instruction Score、Fluency Score，每条取调和平均，再对样本求平均。短板会被明显惩罚。

## 4. 最小 baseline

使用 EasyEdit2 / SteerEval 示例，为每个 concept 生成 Steering 向量，在 Qwen3-4B-Instruct-2507 上生成结果。

## 5. 进阶方案

- 搜索干预层和强度。
- 按 concept 粒度分组设置超参数。
- 对输出做轻量格式清洗，避免空答和重复。

## 6. 特征工程方向

重点不是传统特征，而是 concept 分组、matching/not_matching 表示差异、层选择、向量归一化、解码参数。

## 7. 模型选择

优先官方指定 Qwen3-4B-Instruct-2507。GPU 不足时先用小规模 smoke test 验证流程。

## 8. 验证方案

严格只用 train split 训练，valid split 只评估。记录每个 concept 的输出样例。

## 9. 后处理方案

清除无意义重复、空输出和明显格式错误；不使用 prompt-only 技巧替代 Steering。

## 10. 融合方案

可按 concept 选择不同层/强度，不建议复杂模型集成，避免复现困难。

## 11. 提交计划

1. 用户先完成报名。
2. 下载 SteerEval 数据和官方样例。
3. 跑 1 个 concept smoke test。
4. 生成完整 JSON 并校验。

## 12. 风险点

未报名；需要 GPU；禁止 validation 训练；禁止 prompt-only 方法。

## 13. 时间优先级

高，但应先处理已报名的 532474 和 532472。

## 14. 是否建议深做

建议报名后深做，和 532472 技术栈可复用。
