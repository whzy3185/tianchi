# Baseline 计划

## 1. 最小可运行 baseline

使用官方 EasyEdit2 / SteerEval 示例，在 Qwen3-4B-Instruct-2507 上为每个 concept 训练或估计 Steering 向量，再对 validation prompts 生成结果。

## 2. 数据读取脚本计划

创建：

- `src/load_steereval.py`
- `src/schema.py`

## 3. 数据检查脚本计划

创建 `src/check_data.py`：

- 检查 train/valid 分割。
- 统计 domain、concept、concept_id。
- 确认训练阶段不读取 valid。

## 4. 训练脚本计划

创建 `src/train_steering.py`：

- 读取 train split。
- 按 concept 生成 Steering 向量。
- 保存每个 concept 的向量和配置。

## 5. 预测脚本计划

创建 `src/generate_submission.py`：

- 加载 Qwen3-4B-Instruct-2507。
- 对 validation/test prompts 应用对应 concept 的 Steering 向量。
- 生成 `参赛队伍名称_result.json`。

## 6. 提交校验脚本计划

创建 `src/validate_submission.py`，校验 JSON 结构、concept 覆盖率和 pred 非空。

## 7. 第一次提交策略

使用官方 EasyEdit2 默认 Steering 方法跑通全流程，先提交可用结果，再优化干预层、强度和生成参数。

## 8. 后续三轮优化方向

1. 搜索 Steering 层、向量归一化和干预强度，平衡 CS/IS/FS。
2. 针对不同 concept 粒度做分组超参数。
3. 生成后做轻量格式清洗，避免空答案、跑题和重复输出。
