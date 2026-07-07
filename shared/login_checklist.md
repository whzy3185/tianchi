# 登录与人工确认清单

浏览器要求：使用已登录天池账号的 Chrome。

## 账号状态

1. 打开 https://tianchi.aliyun.com/ 并确认右上角为已登录状态。
2. 确认个人中心的实名认证状态。Chrome 页面中账号区域出现“去认证”字样，需要人工确认是否已经满足各赛道要求。
3. 如提示支付宝实名认证、在线学生认证、授权或手机号验证，完成后返回比赛页面。
4. 对需要组队的赛道，记录队伍名、队长、队员人数和队伍状态。

## 每个赛道逐项确认

对以下链接分别确认：

- https://tianchi.aliyun.com/competition/entrance/532472
- https://tianchi.aliyun.com/competition/entrance/532474
- https://tianchi.aliyun.com/competition/entrance/532479/information
- https://tianchi.aliyun.com/competition/entrance/532499
- https://tianchi.aliyun.com/competition/entrance/532500

需要记录到对应 `participation_status.md`：

1. 页面显示“立即报名”“已报名”还是“报名已结束”。
2. 是否提示实名认证、在线学生认证、授权、签署协议、加入队伍。
3. 是否能进入数据下载页。
4. 数据文件是否可下载，文件名和大小是多少。
5. 是否能进入提交页。
6. 当前赛季是否允许提交。
7. 当日剩余提交次数或总剩余提交次数。
8. 是否有提交模板、官方 baseline、公告、论坛置顶帖或钉钉群更新。

## 赛道特别事项

- 532472：已经报名；重点确认初赛数据下载、提交页当日剩余次数、PersonUKE 数据版本、官方评测脚本或 baseline notebook。
- 532474：已经报名；重点确认 B 榜数据是否已下载、B 榜提交入口是否可用、剩余提交次数。
- 532479：未报名；先完成报名/实名认证/组队，再确认 SteerEval 数据与提交入口。
- 532499：未报名；先确认是否满足国内高校/科研院所在读学生资格、在线学生认证、报名表不可修改风险，再下载数据。
- 532500：未报名；同 532499，另需确认官方样例 `runner.py` 与 TorchScript 模型要求。

## 已排除赛道

- 532498：用户要求不看该比赛，后续不打开、不整理、不执行。
