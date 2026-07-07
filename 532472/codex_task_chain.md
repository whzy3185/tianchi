# Codex 后续任务链

```text
你现在处理 E:\tianchi\532472。

赛题链接：https://tianchi.aliyun.com/competition/entrance/532472
赛题名称：CCKS2026-任务三：大模型知识编辑评测
当前状态：Chrome 登录态已确认“已报名”，页面显示“提交剩 08 日 10 时”，有“赛题与数据/我的团队/提交结果/我的成绩/排行榜/论坛”。

任务要求：

1. 先阅读：
   - E:\tianchi\532472\background.md
   - E:\tianchi\532472\participation_status.md
   - E:\tianchi\532472\data_and_submission.md
   - E:\tianchi\532472\baseline_plan.md
   - E:\tianchi\shared\environment_setup.md
2. 使用 Chrome 打开赛题页面和“赛题与数据”页，确认数据下载入口、文件名、文件大小、提交样例和当日剩余提交次数。遇到登录、授权、实名认证、签署协议时暂停，让用户操作完成后继续。
3. 在 E:\tianchi\532472 下创建代码结构：
   - src\load_data.py
   - src\schema.py
   - src\check_data.py
   - src\train_edit.py
   - src\predict.py
   - src\validate_submission.py
   - configs\baseline.yaml
   - submissions\
   - runs\
   - logs\
   - experiments.csv
4. 下载或登记 PersonUKE 数据：
   - HuggingFace：https://huggingface.co/datasets/xingxingzhihuo2333/PersonUKE-dataset
   - ModelScope：https://www.modelscope.cn/datasets/youngerobert2333/PersonUKE-dataset
5. 安装并记录 EasyEdit 版本：https://github.com/zjunlp/EasyEdit
6. 先做 smoke test：只跑 2-5 条样本，验证数据读取、编辑、预测、提交文件生成。
7. 跑通完整 baseline，生成 `submissions/参赛队伍名称_result.json`。
8. 提交前运行 `python src/validate_submission.py --file <提交文件>`。
9. 提交后记录 experiments.csv：run_id、时间、配置、提交文件、线上 score、Edit_Success、Generalization、Portability、Locality、fluency。
10. 不删除历史提交。每次提交新建递增版本。
```
