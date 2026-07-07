# 统一环境准备方案

建议 Python 版本：3.10 或 3.11。

虚拟环境路径：`E:\tianchi\.venv`

## PowerShell 初始化命令

```powershell
cd E:\tianchi
py -3.11 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip setuptools wheel
pip install pandas numpy scikit-learn matplotlib seaborn tqdm jupyter lightgbm xgboost catboost
```

如果本机没有 Python 3.11，可改用：

```powershell
py -3.10 -m venv .venv
```

## NLP/LLM 赛题补充依赖

适用于 `532472`、`532474`、`532479`：

```powershell
pip install torch transformers datasets sentence-transformers accelerate peft
```

532472 和 532479 可按官方 EasyEdit/EasyEdit2 仓库安装：

```powershell
cd E:\tianchi
mkdir external
git clone https://github.com/zjunlp/EasyEdit.git external\EasyEdit
cd external\EasyEdit
pip install -e .
```

## CV/图像增强赛题补充依赖

适用于 `532499`、`532500`：

```powershell
pip install opencv-python pillow torchvision timm einops safetensors
pip install diffusers accelerate transformers
pip install lpips piq
```

如果使用官方或开源扩散图像增强仓库，按仓库 README 单独安装依赖并记录 commit。

## 推荐、排序或传统建模补充依赖

适用于 `532474` 的传统文本基线：

```powershell
pip install scipy
```

## 版本记录

每个赛道第一次运行前保存依赖快照：

```powershell
cd E:\tianchi
.\.venv\Scripts\Activate.ps1
pip freeze > shared\requirements.lock.txt
```

每个赛道应维护：

- `experiments.csv`
- `README_run.md`
- `configs/`
- `data/`
- `submissions/`
- `runs/`
- `logs/`
- `final/`
