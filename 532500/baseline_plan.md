# Baseline 计划

## 1. 最小可运行 baseline

报名并下载数据后，先实现可提交工程骨架：读取测试图、输出同名 jpg、导出一个可运行 TorchScript 模型、实现 `runner.py` 并打包 zip。若官方提供样例，优先完全复刻样例接口。

## 2. 数据读取脚本计划

创建：

- `src/list_images.py`
- `src/load_images.py`

## 3. 数据检查脚本计划

创建 `src/check_data.py`：

- 检查 evaluation/test 图片数量。
- 检查分辨率、通道、文件名。
- 检查是否能裁剪或缩放到 512x512 用于测速。

## 4. 训练脚本计划

创建 `src/train_light_diffusion.py`：

- 若采用开源轻量 Diffusion，记录模型来源、许可证、修改点。
- 如需微调，仅用规则允许的数据。
- 输出可导出的 PyTorch 模型。

## 5. 预测脚本计划

创建 `src/enhance.py`：

- 对 4K test 图像做 tile/patch 推理。
- 输出同名 jpg 到 `work/output_dir/`。

创建 `src/export_torchscript.py`：

- 导出 `work/model_dir/your_model.pt`。

创建 `work/model_dir/runner.py`：

- 按官方样例加载模型并执行 512x512 推理。

## 6. 提交校验脚本计划

创建 `src/validate_package.py`：

- 校验 `output_dir` 图片。
- 校验 `model_dir` 内容。
- 运行 `runner.py` smoke test。
- 校验 zip 大小。

## 7. 第一次提交策略

先提交格式完全正确且 `runner.py` 可运行的轻量模型包，验证提交链路；随后优化模型质量和速度。

## 8. 后续三轮优化方向

1. 降低采样步数、蒸馏或使用 latent/tile 策略提升速度。
2. 优化 512x512 推理路径，减少显存和延迟。
3. 平衡感知质量与速度，建立本地 latency/quality 记录并冻结最稳版本。
