# Baseline 计划

## 1. 最小可运行 baseline

先用 TF-IDF + LogisticRegression/LinearSVC 完成三分类检测；对预测为纯机器的样本再训练一个 TF-IDF + 线性分类器预测 family。

## 2. 数据读取脚本计划

创建：

- `src/load_data.py`：读取 JSONL。
- `src/labels.py`：维护 label/family 映射。

## 3. 数据检查脚本计划

创建 `src/check_data.py`：

- 检查 JSONL 格式。
- 统计 label/family/method 分布。
- 检查空文本、重复 id、极端长度。

## 4. 训练脚本计划

创建 `src/train_baseline.py`：

- `TfidfVectorizer`
- 检测分类器：LogisticRegression 或 LinearSVC
- 溯源分类器：仅用 `label=1` 样本训练 family 分类
- 保存模型到 `models/`

## 5. 预测脚本计划

创建 `src/predict.py`：

- 先预测 `label`
- 对 `label=1` 的样本预测 `family`
- 其他样本输出 `family=-1`

## 6. 提交校验脚本计划

创建 `src/validate_submission.py`，按 `data_and_submission.md` 的规则校验。

## 7. 第一次提交策略

优先完成完整 B 榜 `submit.jsonl` 并提交一次，获得线上反馈。不要一开始使用复杂 LLM，避免错过截止。

## 8. 后续三轮优化方向

1. 加入字符 n-gram、词 n-gram、文本长度、标点、困惑度 proxy 等特征。
2. 使用中文/英文预训练 encoder 做离线 embedding，再训练 LightGBM/线性分类器。
3. 在规则允许范围内做训练集内增强和模型集成，冻结最稳定方案用于最终提交。
