# 数据和提交说明

## 1. 数据下载入口

- 天池页面：`赛题与数据` 标签
- SteerEval 文档：https://github.com/zjunlp/EasyEdit/blob/main/examples/SteerEval.md
- 训练集：https://huggingface.co/datasets/zjunlp/SteerEval/blob/main/personality/train.json
- 验证集：https://huggingface.co/datasets/zjunlp/SteerEval/blob/main/personality/valid.json

## 2. 数据文件名

已知：

- `personality/train.json`
- `personality/valid.json`

天池数据包内文件名待报名后确认。

## 3. 文件大小

待确认。

## 4. 训练集说明

仅可使用 SteerEval Personality 领域 train split 训练。每条数据包含：

- `domain`
- `domain_description`
- `concept`
- `concept_id`
- `question`
- `matching`
- `not_matching`

## 5. 测试集说明

官方说明初赛在 Personality validation split 上评估。严禁使用 validation split 训练。复赛数据与初赛保持一致的表述需要报名后进一步确认。

## 6. 样例提交文件说明

单个 sample 示例结构：

```json
{
  "concept_id": "L1_1",
  "concept_name": "概念名称",
  "concept_description": "概念描述",
  "generation_prompt": null,
  "generated_results": [
    {
      "input": "问题 prompt1",
      "orig_pred": [],
      "pred": ["steer 后模型对 prompt 的回答"],
      "reference_response": null,
      "complete_output": ["完整的回答"]
    }
  ]
}
```

## 7. 提交文件格式

JSON 文件，文件名：

```text
参赛队伍名称_result.json
```

## 8. 提交字段

- `concept_id`
- `concept_name`
- `concept_description`
- `generation_prompt`
- `generated_results`
- `generated_results[].input`
- `generated_results[].orig_pred`
- `generated_results[].pred`
- `generated_results[].reference_response`
- `generated_results[].complete_output`

## 9. 是否需要 zip

常规线上提交为单个 JSON 文件。复现审核材料是否 zip 待官方通知。

## 10. 是否有代码提交环境

常规提交不显示代码环境。优胜队伍需要提交完整可运行代码供人工复现验证。

## 11. 本地校验规则

1. JSON 文件必须可被 `json.load` 读取。
2. `concept_id` 覆盖评估集概念。
3. 每个 `generated_results` 中 `pred` 不为空。
4. 不得使用 validation split 训练。
5. 提交前记录模型、Steering 层、向量生成方法和随机种子。
