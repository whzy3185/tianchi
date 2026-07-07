# Codex 后续任务链

```text
你现在处理 E:\tianchi\532474。

赛题链接：https://tianchi.aliyun.com/competition/entrance/532474
赛题名称：CCKS2026-任务六：大模型生成文本检测及溯源
当前状态：Chrome 登录态已确认“已报名”，页面显示“提交剩 03 日 10 时”，有“赛题与数据/我的团队/提交结果/我的成绩/排行榜/论坛”。

任务要求：

1. 先阅读：
   - E:\tianchi\532474\background.md
   - E:\tianchi\532474\participation_status.md
   - E:\tianchi\532474\data_and_submission.md
   - E:\tianchi\532474\baseline_plan.md
   - E:\tianchi\shared\environment_setup.md
2. 使用 Chrome 打开赛题页面和“赛题与数据”页，确认 B 榜数据下载入口、文件名、文件大小、提交页剩余次数。遇到登录、授权、实名认证、签署协议时暂停，让用户操作完成后继续。
3. 在 E:\tianchi\532474 下创建代码结构：
   - src\load_data.py
   - src\labels.py
   - src\check_data.py
   - src\train_baseline.py
   - src\predict.py
   - src\validate_submission.py
   - configs\baseline.yaml
   - models\
   - submissions\
   - runs\
   - logs\
   - experiments.csv
4. 下载并放置数据到 data\raw\，不得使用外部标注数据、在线闭源模型 API、互联网搜索服务或人工交互。
5. 先实现 TF-IDF + LogisticRegression/LinearSVC baseline：
   - 检测三分类 label：0/1/2
   - 对 label=1 样本预测 family：0..7
   - label=0/2 时 family=-1
6. 生成 submit.jsonl。
7. 提交前运行：
   python src\validate_submission.py --test data\raw\test.jsonl --submit submissions\submit.jsonl
8. 提交后记录 experiments.csv：run_id、时间、配置、提交文件、线上 FinalScore、F1_detect、F1_source、备注。
9. 不删除历史提交。B 榜截止前冻结最稳定版本到 final\。
```
