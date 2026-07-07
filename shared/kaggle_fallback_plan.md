# Kaggle 备用方案

更新时间：2026-07-07

## 启用条件

任一赛道满足以下条件之一时，启用 Kaggle 备用方案：

1. 单个数据文件超过 5GB。
2. 单赛道数据总量超过 20GB。
3. 本地磁盘不足。
4. 本地训练时间过长。
5. 需要 GPU，且本机运行成本高。

## 前置检查

```powershell
kaggle --version
```

如果未登录，需要用户配置：

```text
C:\Users\<用户名>\.kaggle\kaggle.json
```

不得把 `kaggle.json`、token、cookie、账号信息写入仓库、文档或 Kaggle Dataset。

## Dataset 命名

每个大数据赛道创建私有 Dataset：

```text
tianchi-题目ID-dataset
```

上传前生成 `dataset-metadata.json`，并设置为 private。

## Notebook 命名

每个大数据赛道创建 Notebook：

```text
tianchi-题目ID-baseline
```

Notebook 必须包含：

1. 数据读取。
2. EDA。
3. baseline 训练。
4. 推理。
5. 生成提交文件。
6. 输出提交文件到 Notebook output。

## 数据合规边界

- 不上传任何账号密钥、cookie、token、个人身份信息。
- 不公开上传天池受限数据，Kaggle Dataset 必须为 private。
- 如果赛题规则禁止迁移数据到 Kaggle，停止 Kaggle 方案，改为本地或天池官方环境。
- 如果规则未明确允许外部平台保存数据，必须先让用户确认。

## 当前赛道初判

| 赛道 | 是否可能需要 Kaggle | 原因 |
|---|---|---|
| 532472 | 可能 | LLM 知识编辑需要 GPU 和模型权重 |
| 532474 | 暂不需要 | JSONL 文本分类，传统 baseline 可本地跑 |
| 532479 | 可能 | Qwen3-4B-Instruct-2507 和 Steering 需要 GPU |
| 532499 | 可能 | 100 张 4K 图像，Diffusion 推理重 |
| 532500 | 可能 | 4K 图像、轻量 Diffusion、TorchScript 和测速 |
