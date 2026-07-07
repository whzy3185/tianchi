# 数据和提交说明

## 1. 数据下载入口

天池页面 `赛题与数据` 标签。当前未报名，具体下载按钮、官方样例 `runner.py` 和模型提交要求需报名后确认。

## 2. 数据文件名

待确认。

## 3. 文件大小

待确认。测试集为 100 张 4K 图像，预计体积较大。

## 4. 训练集说明

官方页面未明确提供训练集。已知有 evaluation 验证集 3 组输入图像和 Ground Truth，可用于验证算法效果。

## 5. 测试集说明

测试集 test 包含 100 组低质量图像，Ground Truth 不公开，覆盖建筑、绿植、夜景等真实场景，分辨率均为 4K。

## 6. 样例提交文件说明

提交 zip 内部目录结构：

```text
my_work.zip
├── output_dir
│   ├── case1.jpg
│   ├── case2.jpg
│   ├── case3.jpg
│   ├── case4.jpg
│   └── ...
└── model_dir
    ├── your_model.pt
    └── runner.py
```

## 7. 提交文件格式

`.zip` 压缩包，大小 <= 10GB。

作品命名规范：

```text
技术领域+作品名称+团队/个人名称+联系方式
```

示例：

```text
赛题二_xxx作品_xx队_13000000000.zip
```

## 8. 提交字段

无表格字段。提交内容为：

- `output_dir`：100 张增强 jpg。
- `model_dir/your_model.pt`：TorchScript 可执行模型。
- `model_dir/runner.py`：推理代码。

## 9. 是否需要 zip

需要。压缩包必须包含 `output_dir` 和 `model_dir`。

## 10. 是否有代码提交环境

需要提交 `runner.py` 和 TorchScript 模型用于测速。具体执行接口以官方样例为准。

## 11. 本地校验规则

1. zip 根目录下必须有 `output_dir` 和 `model_dir`。
2. `output_dir` 中必须包含 100 张 jpg。
3. 图片文件名必须与测试输入图一一对应，不得包含中文符号。
4. 图片分辨率必须与输入一致。
5. `model_dir` 中必须包含 `.pt` 模型和 `runner.py`。
6. 本地必须能执行 `runner.py` 并完成 512x512 输入输出测速。
7. zip 大小 <= 10GB。
8. 生成过程不得使用官方禁止的商用图像处理软件或商用 AI 产品。
