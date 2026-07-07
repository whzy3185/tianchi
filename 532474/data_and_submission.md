# 数据和提交说明

## 1. 数据下载入口

天池页面 `赛题与数据` 标签。B 榜数据发布时间为 2026-07-03。

## 2. 数据文件名

待确认。已知官方说明包含 `train.jsonl`、`test.jsonl`、`submit.jsonl`。

## 3. 文件大小

待确认。

## 4. 训练集说明

`train.jsonl` 每行一个 JSON：

```json
{
  "id": "样本ID",
  "text": "文本内容",
  "label": 1,
  "model": "模型名",
  "family": 0
}
```

`label` 含义：

- `0`：纯人类文本
- `1`：纯机器生成文本
- `2`：人机协作文本

当 `label=2` 时，`method` 可为：

- `machine-modify-human`
- `machine-continue-human`
- `human-mix-machine`

## 5. 测试集说明

`test.jsonl` 每行一个 JSON，包含：

- `id`
- `text`

## 6. 样例提交文件说明

`submit.jsonl` 每行一个 JSON：

```json
{"id":"样本ID","label":1,"family":0}
```

## 7. 提交文件格式

JSON Lines，文件名建议为：

```text
submit.jsonl
```

## 8. 提交字段

- `id`
- `label`
- `family`

模型家族标签：

- `0`：OpenAI/GPT
- `1`：Alibaba/Qwen
- `2`：DeepSeek
- `3`：ByteDance/Doubao
- `4`：Moonshot/Kimi
- `5`：Google/Gemini
- `6`：Anthropic/Claude
- `7`：xAI/Grok

## 9. 是否需要 zip

常规榜单提交为 `submit.jsonl`。B 榜前 10 需要最终压缩包，包含：

- `submit.jsonl`
- 全部系统代码
- `README.md` 或 `README.pdf`

邮件提交地址：`CCKS2026taskAIGC@163.com`

邮件主题格式：

```text
CCKS-评测任务AIGC-最终提交文件-参赛队名称
```

## 10. 是否有代码提交环境

线上常规提交不要求代码环境。B 榜前 10 需要离线代码复现。

## 11. 本地校验规则

1. `submit.jsonl` 每行必须为合法 JSON。
2. 每行必须包含 `id`、`label`、`family`。
3. `label` 只能取 `0/1/2`。
4. 当 `label=0/2`，`family` 必须为 `-1`。
5. 当 `label=1`，`family` 必须在 `0..7`。
6. `id` 必须覆盖测试集且不重复。
