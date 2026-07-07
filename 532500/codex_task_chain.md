# Codex 后续任务链

```text
你现在处理 E:\tianchi\532500。

赛题链接：https://tianchi.aliyun.com/competition/entrance/532500
赛题名称：CSIG图像图形技术挑战赛-赛道二：生成式图像增强轻量模型设计挑战
当前状态：Chrome 登录态显示“立即报名”“报名剩 71 日 00 时”，当前账号尚未报名。

任务要求：

1. 先阅读：
   - E:\tianchi\532500\background.md
   - E:\tianchi\532500\participation_status.md
   - E:\tianchi\532500\data_and_submission.md
   - E:\tianchi\532500\baseline_plan.md
   - E:\tianchi\shared\environment_setup.md
2. 使用 Chrome 打开赛题页面。如果需要报名、报名表、在线学生认证、实名认证、资格审核、协议或组队，暂停让用户操作，完成后继续。
3. 报名后确认数据下载入口、文件名、文件大小、提交入口、官方样例 `runner.py`、TorchScript 模型要求和提交次数。
4. 在 E:\tianchi\532500 下创建代码结构：
   - src\list_images.py
   - src\load_images.py
   - src\check_data.py
   - src\train_light_diffusion.py
   - src\enhance.py
   - src\export_torchscript.py
   - src\validate_package.py
   - configs\baseline.yaml
   - data\
   - work\output_dir\
   - work\model_dir\
   - submissions\
   - runs\
   - logs\
   - experiments.csv
5. 严格遵守规则：不得使用商用图像处理软件或商用 AI 产品处理结果。
6. 先跑通最小提交骨架：
   - 100 张同名 jpg 输出到 output_dir
   - TorchScript 模型输出到 model_dir
   - runner.py 可执行 512x512 输入输出 smoke test
   - zip 包结构正确
7. 若官方有 baseline 或 runner.py 样例，优先完全兼容官方接口。
8. 提交前运行 `python src\validate_package.py --zip <提交zip> --test-dir <测试图目录>`。
9. 提交后记录 experiments.csv：run_id、时间、模型结构、TorchScript 路径、runner.py 路径、本地测速、线上分数、备注。
10. 不删除历史提交。最终前冻结最佳结果到 final\。
```
