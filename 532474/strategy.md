# 策略文档

## 1. 题目理解

文本检测与溯源联合任务。先判断文本是纯人类、纯机器或人机协作；若为纯机器，再判断模型家族。

## 2. 数据类型判断

JSONL 文本分类任务，训练集有 label/family/method，测试集只有 id/text。

## 3. 评测指标解释

`FinalScore = 0.8 * F1_detect + 0.2 * F1_source`。检测三分类更重要，溯源只对真实纯机器样本计算。

## 4. 最小 baseline

TF-IDF word/char n-gram + LogisticRegression 或 LinearSVC：

- 模型 1：预测 label 0/1/2。
- 模型 2：只用 label=1 样本预测 family 0..7。

## 5. 进阶方案

- 字符 n-gram 和词 n-gram 融合。
- 文本长度、标点比例、重复度、数字比例等统计特征。
- 离线开源 encoder embedding + 线性/LightGBM 分类器。

## 6. 特征工程方向

长度、平均句长、标点密度、换行密度、词汇多样性、重复片段、字符 n-gram、subword n-gram。

## 7. 模型选择

先用 TF-IDF + LinearSVC/LogisticRegression。时间允许再用开源小模型 embedding，避免在线闭源 API。

## 8. 验证方案

从训练集 stratified split 出验证集，同时分开监控 Macro-F1 detect 和 family Macro-F1。

## 9. 后处理方案

若 label 为 0/2，强制 family=-1；若 label=1，family 必须为 0..7。可按检测置信度调整 label=1 阈值。

## 10. 融合方案

线性模型、char 模型、word 模型投票或概率平均。优先保持简单可复现。

## 11. 提交计划

1. 确认 B 榜数据 `test_b.jsonl`。
2. 先生成合法 `submit.jsonl`。
3. 尽快提交一次 B 榜获取反馈。
4. 仅在确认前列出提交信息，等待用户确认后提交。

## 12. 风险点

B 榜截止近；禁止在线闭源 API；外部数据限制严格；前 10 要代码复现。

## 13. 时间优先级

最高。已报名且 B 榜截止最近。

## 14. 是否建议深做

建议立即做，先追求可提交 baseline，再小步优化。
