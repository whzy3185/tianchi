# Codex 总控任务链提示词

将下面整段复制给 Codex 执行：

```text
你现在接管 E:\tianchi 下的天池赛道准备工作。当前处理赛道是：

1. E:\tianchi\532472
   链接：https://tianchi.aliyun.com/competition/entrance/532472
   赛题：CCKS2026-任务三：大模型知识编辑评测

2. E:\tianchi\532474
   链接：https://tianchi.aliyun.com/competition/entrance/532474
   赛题：CCKS2026-任务六：大模型生成文本检测及溯源

3. E:\tianchi\532479
   链接：https://tianchi.aliyun.com/competition/entrance/532479/information
   赛题：CCKS2026-任务七：大模型行为调控评测

4. E:\tianchi\532499
   链接：https://tianchi.aliyun.com/competition/entrance/532499
   赛题：CSIG图像图形技术挑战赛-赛道一：生成式图像增强可控性挑战

5. E:\tianchi\532500
   链接：https://tianchi.aliyun.com/competition/entrance/532500
   赛题：CSIG图像图形技术挑战赛-赛道二：生成式图像增强轻量模型设计挑战

不要处理 532498。

总要求：

1. 先阅读 E:\tianchi\README.md、E:\tianchi\shared\platform_status.md、E:\tianchi\shared\login_checklist.md、E:\tianchi\shared\environment_setup.md。
2. 再阅读每个赛道的 background.md、participation_status.md、data_and_submission.md、baseline_plan.md、codex_task_chain.md。
3. 使用 Chrome 中已登录的天池账号核验报名、实名认证、数据下载和提交状态。遇到登录、授权、实名认证、在线学生认证、签署协议、加入队伍等页面时暂停，让用户操作完成后继续。
4. 按优先级选择赛道：
   - 532474 已报名且 B 榜截止最近，最高优先级。
   - 532472 已报名且初赛截止较近，高优先级。
   - 532479 当前显示立即报名，报名成功后高优先级。
   - 532499/532500 截止较晚，但需要 CV 算力和资格审核，中高优先级。
5. 每个赛道先跑通最小可运行 baseline，再做优化。
6. 每次提交前必须执行本地格式校验，不允许直接提交未经校验的文件。
7. 每次提交后必须记录提交时间、文件路径、线上分数、备注。
8. 不删除历史提交、日志、配置和模型；新版本使用递增编号。
9. 每个赛道维护 experiments.csv，字段至少包括：run_id、time、code_version、data_version、config_path、model_path、submission_path、local_metric、online_score、notes。
10. 每个模型版本都要能复现：保留代码、配置、依赖版本、随机种子、数据处理脚本、训练命令和预测命令。
11. B 榜或最终提交前冻结最稳定方案，复制到 final/ 目录，并写 README_final.md 说明复现步骤。

建议执行顺序：

1. 对 532474 执行 E:\tianchi\532474\codex_task_chain.md。
2. 对 532472 执行 E:\tianchi\532472\codex_task_chain.md。
3. 若用户完成 532479 报名，对 532479 执行 E:\tianchi\532479\codex_task_chain.md。
4. 若用户完成 532499/532500 报名和学生认证，按算力情况选择其中一个 CV 赛道执行。
```
