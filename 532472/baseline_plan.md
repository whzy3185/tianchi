# Baseline 计划

## 1. 最小可运行 baseline

使用官方 EasyEdit 跑通 PersonUKE 示例流程。若 GPU 不足，先用最小子集验证数据读取、结果生成和提交格式。

## 2. 数据读取脚本计划

创建：

- `src/load_data.py`：读取 train/test JSON。
- `src/schema.py`：定义样本字段和提交字段。

## 3. 数据检查脚本计划

创建 `src/check_data.py`：

- 检查字段完整性。
- 检查只使用允许的训练字段。
- 输出概念/关系/实体分布。

## 4. 训练脚本计划

创建 `src/train_edit.py`：

- 封装 EasyEdit 方法。
- 保存配置、随机种子、模型路径。
- 对少量样本先完成 smoke test。

## 5. 预测脚本计划

创建 `src/predict.py`：

- 加载编辑配置和模型。
- 对测试集生成编辑后输出。
- 输出中间预测文件。

## 6. 提交校验脚本计划

创建 `src/validate_submission.py`：

- 校验 JSON 格式。
- 校验样本数、字段、`case_id` 唯一性。
- 校验文件名符合 `参赛队伍名称_result.json`。

## 7. 第一次提交策略

先使用官方 baseline 或最小 EasyEdit 配置生成完整提交，目标是跑通线上评分，不追求高分。

## 8. 后续三轮优化方向

1. 调整知识编辑方法和超参数，优化 Edit_Success 与 Locality 平衡。
2. 加入更强的 prompt 模板和生成后处理，但不得违反字段限制。
3. 复赛前固定环境、模型权重和配置，准备复现材料。
