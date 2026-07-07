# 天池比赛资料整理与参赛准备

更新时间：2026-07-07（Asia/Shanghai）

本目录用于整理阿里云天池赛道的官方资料、当前参赛状态、数据与提交要求、baseline 计划和后续 Codex 任务链。当前处理赛道为 `532472`、`532474`、`532479`、`532499`、`532500`。

用户已明确要求停止处理 `532498` 世界杯 Agent 赛道，后续不再查看、整理或执行该赛道。

## 核验来源

- 天池比赛页面：Chrome 已登录状态下读取页面可见按钮、导航与状态文案。
- 天池官方详情接口：`https://tianchi.aliyun.com/v3/proxy/competition/api/race/getDetail?raceId=<ID>`
- 当前账号页面状态：Chrome 页面显示已登录；页面右上角能看到“退出登录”。

## 总览

| 赛道 | 赛题名称 | Chrome 登录态状态 | 当前窗口判断 | 是否仍可参与 | 建议优先级 |
|---|---|---|---|---|---|
| 532472 | CCKS2026-任务三：大模型知识编辑评测 | 已报名；显示“提交剩 08 日 10 时”；有“赛题与数据/我的团队/提交结果/我的成绩/排行榜/论坛” | 初赛/报名至 2026-07-15 23:59:59，复赛至 2026-08-15 17:59:59 | 是 | 高 |
| 532474 | CCKS2026-任务六：大模型生成文本检测及溯源 | 已报名；显示“提交剩 03 日 10 时”；有“提交结果/我的成绩/排行榜/论坛” | B 榜至 2026-07-10 23:59:59 | 是，需尽快处理 | 最高 |
| 532479 | CCKS2026-任务七：大模型行为调控评测 | 显示“立即报名”“报名剩 09 日 00 时”；有“赛题与数据/排行榜/论坛” | 初赛/报名至 2026-07-15 23:59:59 | 可报名，报名后参与 | 高 |
| 532499 | CSIG图像图形技术挑战赛-赛道一：生成式图像增强可控性挑战 | 显示“立即报名”“报名剩 70 日 18 时”；有“赛题与数据/算力支持/排行榜/论坛” | 报名至 2026-09-15 17:59:59，提交至 2026-09-15 17:59:59 | 可报名，报名后参与 | 中高 |
| 532500 | CSIG图像图形技术挑战赛-赛道二：生成式图像增强轻量模型设计挑战 | 显示“立即报名”“报名剩 71 日 00 时”；有“赛题与数据/算力支持/排行榜/论坛” | 报名/提交至 2026-09-15 23:59:59 | 可报名，报名后参与 | 中高 |

## 推荐执行顺序

1. 优先处理 `532474/codex_task_chain.md`：已经报名，B 榜截止最近。
2. 第二优先处理 `532472/codex_task_chain.md`：已经报名，初赛截止较近，数据与 baseline 明确。
3. 第三优先处理 `532479/codex_task_chain.md`：需要先报名，但截止较近，任务与 532472 技术栈接近。
4. 再处理 `532499/codex_task_chain.md` 和 `532500/codex_task_chain.md`：截止较晚，但需要 CV/扩散模型与算力准备。

## 目录结构

```text
E:\tianchi
├─ README.md
├─ shared
│  ├─ platform_status.md
│  ├─ environment_setup.md
│  ├─ kaggle_fallback_plan.md
│  ├─ submission_policy.md
│  ├─ material_inventory.md
│  ├─ login_checklist.md
│  └─ codex_master_task_chain.md
├─ 532472
│  ├─ background.md
│  ├─ participation_status.md
│  ├─ data_and_submission.md
│  ├─ strategy.md
│  ├─ baseline_plan.md
│  ├─ codex_task_chain.md
│  ├─ experiments.csv
│  ├─ src
│  ├─ data
│  ├─ submissions
│  └─ reports
├─ 532474
│  ├─ background.md
│  ├─ participation_status.md
│  ├─ data_and_submission.md
│  ├─ strategy.md
│  ├─ baseline_plan.md
│  ├─ codex_task_chain.md
│  ├─ experiments.csv
│  ├─ src
│  ├─ data
│  ├─ submissions
│  └─ reports
├─ 532479
│  ├─ background.md
│  ├─ participation_status.md
│  ├─ data_and_submission.md
│  ├─ strategy.md
│  ├─ baseline_plan.md
│  ├─ codex_task_chain.md
│  ├─ experiments.csv
│  ├─ src
│  ├─ data
│  ├─ submissions
│  └─ reports
├─ 532499
│  ├─ background.md
│  ├─ participation_status.md
│  ├─ data_and_submission.md
│  ├─ strategy.md
│  ├─ baseline_plan.md
│  ├─ codex_task_chain.md
│  ├─ experiments.csv
│  ├─ src
│  ├─ data
│  ├─ submissions
│  └─ reports
├─ 532500
│  ├─ background.md
│  ├─ participation_status.md
│  ├─ data_and_submission.md
│  ├─ strategy.md
│  ├─ baseline_plan.md
│  ├─ codex_task_chain.md
│  ├─ experiments.csv
│  ├─ src
│  ├─ data
│  ├─ submissions
│  └─ reports
```
