# 数据和提交说明

## 1. 数据下载入口

- 天池页面：`赛题与数据` 标签
- HuggingFace：https://huggingface.co/datasets/xingxingzhihuo2333/PersonUKE-dataset
- ModelScope：https://www.modelscope.cn/datasets/youngerobert2333/PersonUKE-dataset

## 2. 数据文件名

已本地归档：

- `data/raw/PersonUKE-dataset.json`

## 3. 文件大小

已确认：

- `PersonUKE-dataset.json`：1,044,836 bytes，679 条 JSON 样本

## 4. 训练集说明

PersonUKE 数据已确认字段：

- `prompt`
- `rephrase`
- `target_old`
- `target_new`
- `portability`
- `locality`

官方限制：仅允许使用 edit/train prompt 和 `target_new` 字段进行训练；其他字段仅用于评估或结构校验。

## 5. 测试集说明

初赛提供测试数据集，参赛队伍提交编辑结果参与排名。复赛阶段会提供复赛测试数据集。

## 6. 样例提交文件说明

官方示例结构包含 `case_id`、`requested_rewrite`、`pre`、`post`、`score` 和多项指标字段。最终提交以提交页样例为准。

## 7. 提交文件格式

JSON 文件，文件名格式：

```text
参赛队伍名称_result.json
```

## 8. 提交字段

待以官方样例严格确认。当前已知字段包括：

- `case_id`
- `requested_rewrite.prompt`
- `requested_rewrite.target_new`
- `pre`
- `post`
- `pred` 或生成结果字段

## 9. 是否需要 zip

常规线上提交为单个 JSON 文件；Top3 复现审核需提交代码和模型权重，是否打包 zip 待官方通知。

## 10. 是否有代码提交环境

常规提交不显示代码提交环境。Top3 需要离线复现审核。

## 11. 本地校验规则

1. JSON 必须能被 `json.load` 读取。
2. 样本数必须与测试集一致。
3. 每个 `case_id` 必须唯一。
4. 不得使用测试集标签或测试集相似构造数据训练。
5. 提交前保存 `submissions/submit_YYYYMMDD_HHMM.json`，并记录到 `experiments.csv`。
