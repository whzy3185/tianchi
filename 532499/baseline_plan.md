# Baseline 计划

## 1. 最小可运行 baseline

报名并下载数据后，先实现一个可复现的图像处理 pipeline：读取测试图、保持分辨率、输出同名 jpg、打包 zip。若官方提供样例或 baseline，优先使用官方 baseline；否则选择许可证清晰的开源 Diffusion 图像增强/复原模型作为初版。

## 2. 数据读取脚本计划

创建：

- `src/list_images.py`
- `src/load_images.py`

## 3. 数据检查脚本计划

创建 `src/check_data.py`：

- 检查 evaluation/test 图片数量。
- 检查分辨率、通道、文件名。
- 统计五类挑战场景目录或命名模式。

## 4. 训练脚本计划

若使用官方或开源模型微调，创建 `src/train.py`；若不训练，则记录模型来源、许可证和推理配置。

## 5. 预测脚本计划

创建 `src/enhance.py`：

- 逐张读取 test 图像。
- 使用 Diffusion 增强或基础增强 pipeline。
- 输出到 `work/output_dir/`。
- 保持原始分辨率和文件名。

## 6. 提交校验脚本计划

创建 `src/validate_package.py`：

- 校验 `output_dir`。
- 校验图片数量、文件名、分辨率、扩展名。
- 校验 zip 大小。

## 7. 第一次提交策略

先提交一个格式完全正确的轻量结果包，验证线上流程。随后再投入重模型增强。

## 8. 后续三轮优化方向

1. 对五类挑战场景分别调参，降低过度增强和伪影。
2. 尝试 patch/tile 推理以处理 4K 图像，并做边界融合。
3. 集成无参考质量指标和人眼抽检，冻结最自然稳定的结果。
