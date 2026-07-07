# Codex 后续任务链

```text
你现在处理 E:\tianchi\532479。

赛题链接：https://tianchi.aliyun.com/competition/entrance/532479/information
赛题名称：CCKS2026-任务七：大模型行为调控评测
当前状态：Chrome 登录态显示“立即报名”“报名剩 09 日 00 时”，当前账号尚未报名。

任务要求：

1. 先阅读：
   - E:\tianchi\532479\background.md
   - E:\tianchi\532479\participation_status.md
   - E:\tianchi\532479\data_and_submission.md
   - E:\tianchi\532479\baseline_plan.md
   - E:\tianchi\shared\environment_setup.md
2. 使用 Chrome 打开赛题页面，先确认是否仍显示“立即报名”。如果需要报名、协议、实名认证、组队或授权，暂停让用户操作，完成后继续。
3. 报名后确认数据下载入口、提交入口、当日提交次数和提交样例。
4. 在 E:\tianchi\532479 下创建代码结构：
   - src\load_steereval.py
   - src\schema.py
   - src\check_data.py
   - src\train_steering.py
   - src\generate_submission.py
   - src\validate_submission.py
   - configs\baseline.yaml
   - vectors\
   - submissions\
   - runs\
   - logs\
   - experiments.csv
5. 下载 SteerEval Personality train/valid。严格禁止用 valid 训练。
6. 安装 EasyEdit/EasyEdit2，并记录 commit 与依赖版本。
7. 下载或配置 Qwen3-4B-Instruct-2507。
8. 先跑 1 个 concept 的 smoke test，再跑完整 baseline。
9. 生成 `参赛队伍名称_result.json`，提交前运行 `python src\validate_submission.py --file <提交文件>`。
10. 提交后记录 experiments.csv：run_id、时间、Steering 方法、层号、强度、生成参数、线上分数、备注。
11. 不删除历史提交。复赛/最终前冻结最稳定方案到 final\。
```
