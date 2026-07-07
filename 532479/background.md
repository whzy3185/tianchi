# 背景文档

## 1. 赛题名称

CCKS2026-任务七：大模型行为调控评测

## 2. 赛题链接

https://tianchi.aliyun.com/competition/entrance/532479/information

## 3. 赛事背景

大模型在推理过程中表现出复杂的知识表达与行为属性。Steering（行为引导调控）是在不修改模型权重的情况下，对模型内部表示或激活进行即时调控，使模型输出符合指定目标行为。相比微调，Steering 更轻量、实时、即插即用，适用于人格调控、情感控制、语言风格调整等场景。

## 4. 任务目标

根据给定目标行为概念 `concept`，使用 Steering 方法控制大模型生成内容，使模型回答相关问题时输出符合目标行为的答案。

## 5. 输入数据说明

初赛使用 SteerEval 数据集中的 Personality 子数据集：

- 训练集：Personality `train` split
- 评估集：Personality `validation` split

数据为 paired preference 格式，字段包括：

- `domain`
- `domain_description`
- `concept`
- `concept_id`
- `question`
- `matching`
- `not_matching`

## 6. 输出结果说明

最终提交一个 JSON 文件，命名为：

```text
参赛队伍名称_result.json
```

每个 sample 包含 `concept_id`、`concept_name`、`concept_description`、`generation_prompt`、`generated_results` 等字段。

## 7. 评测指标

开放式生成评测，三个维度每项 0-4 分：

- Concept Score, CS：概念准确性
- Instruction Score, IS：指令遵循度
- Fluency Score, FS：流畅性

最终得分使用每条数据三个维度的调和平均 Harmonic Mean，最终排名基于所有领域和粒度层级每条数据的平均 HM 分数。

## 8. 参赛限制

- 每队 2-3 人。
- 每位选手只能加入一支队伍。
- 报名、组队变更、实名认证截止：2026-07-15 23:59:59。
- 复赛前 3 名需提交完整可运行代码和模型/干预向量等复现材料。
- 禁止使用 validation split 训练。
- 禁止使用基于 Prompt 的方法，如 0-shot Prompt、Few-shot Prompt。
- 参赛方法必须对模型内部激活进行调控，如激活干预、Steering 向量。

## 9. 是否允许外部数据

官方规则允许使用公开可获得的预训练数据，但严禁标注测试集或构造测试集相似数据。训练阶段仅可使用指定训练 split。

## 10. 是否允许预训练模型

允许使用官方指定模型与基线框架。比赛使用的大模型：

- Qwen3-4B-Instruct-2507：https://huggingface.co/Qwen/Qwen3-4B-Instruct-2507

## 11. 是否允许在线 API

不建议也不应使用在线 API。赛题要求对模型内部激活进行调控，在线闭源 API 通常无法满足该要求；最终以官方公告为准。

## 12. 是否需要提交代码、模型、报告

- 常规提交：`参赛队伍名称_result.json`
- 复现审核：需提交完整可运行代码
- 论文/报告：评测论文时间为 2026-09-01，具体要求待 CCKS 通知

## 13. 官方 baseline 或 starter notebook 链接

- EasyEdit2 README：https://github.com/zjunlp/EasyEdit/blob/main/README_2.md
- SteerEval 文档：https://github.com/zjunlp/EasyEdit/blob/main/examples/SteerEval.md
- SteerEval train：https://huggingface.co/datasets/zjunlp/SteerEval/blob/main/personality/train.json
- SteerEval valid：https://huggingface.co/datasets/zjunlp/SteerEval/blob/main/personality/valid.json

## 14. 官方公告、论坛、钉钉群信息

- 官方钉钉群：84640002889
- 论坛入口：登录后页面导航中的“论坛”
- 公告/补充规则：待报名后继续确认
