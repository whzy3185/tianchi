# 资料盘点表

更新时间：2026-07-07

用户最新要求：不处理 `532498` 世界杯 Agent 赛道，只制作其他赛道。

## 总览

| 题目 ID | 已有文档 | 缺失文档 | 是否已有策略 | 是否已有 baseline | 是否已有数据说明 | 是否已有提交说明 |
|---|---|---|---|---|---|---|
| 532472 | background, participation_status, data_and_submission, strategy, baseline_plan, codex_task_chain | 官方数据文件未下载 | 是 | 仅脚本骨架，待数据下载后实现真实 baseline | 是 | 是 |
| 532474 | background, participation_status, data_and_submission, strategy, baseline_plan, codex_task_chain | B 榜数据文件未下载 | 是 | 仅脚本骨架，待数据下载后实现 TF-IDF baseline | 是 | 是 |
| 532479 | background, participation_status, data_and_submission, strategy, baseline_plan, codex_task_chain | 当前账号未报名，数据入口待确认 | 是 | 仅脚本骨架，待报名/数据后实现 EasyEdit2 baseline | 是 | 是 |
| 532499 | background, participation_status, data_and_submission, strategy, baseline_plan, codex_task_chain | 当前账号未报名，数据入口待确认 | 是 | 仅脚本骨架，待数据后实现图像增强 pipeline | 是 | 是 |
| 532500 | background, participation_status, data_and_submission, strategy, baseline_plan, codex_task_chain | 当前账号未报名，官方 runner 样例待确认 | 是 | 仅脚本骨架，待数据后实现 TorchScript pipeline | 是 | 是 |
| 532498 | 已排除 | 不制作 | 否 | 否 | 否 | 否 |

## 已创建统一结构

每个处理中的赛道目录均包含：

- `background.md`
- `participation_status.md`
- `data_and_submission.md`
- `strategy.md`
- `baseline_plan.md`
- `codex_task_chain.md`
- `experiments.csv`
- `src/inspect_data.py`
- `src/make_folds.py`
- `src/train_baseline.py`
- `src/predict.py`
- `src/validate_submission.py`
- `data/raw/`
- `data/processed/`
- `submissions/`
- `reports/submission_log.md`

## 阻塞项

1. 未下载官方数据集，因为下载、授权、报名和实名认证需要用户确认。
2. 未执行天池真实提交，提交前必须按 `shared/submission_policy.md` 等待用户确认。
3. Kaggle 上传未执行，需先确认赛题规则允许迁移数据且 Dataset 必须 private。
4. `gh` 未安装，GitHub 发布需使用普通 git 凭据或用户安装 GitHub CLI。
