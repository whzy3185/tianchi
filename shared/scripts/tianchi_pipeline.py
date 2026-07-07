import argparse
import csv
import json
import logging
import shutil
import sys
import time
import zipfile
from pathlib import Path


SEED = 20260707


def contest_root() -> Path:
    path = Path(__file__).resolve()
    # E:/tianchi/shared/scripts/tianchi_pipeline.py
    return path.parents[2]


def current_contest_dir() -> Path:
    script = Path(sys.argv[0]).resolve()
    if script.parent.name == "src":
        return script.parents[1]
    return Path.cwd()


def setup_logging(contest_dir: Path, name: str) -> Path:
    logs = contest_dir / "logs"
    logs.mkdir(parents=True, exist_ok=True)
    log_path = logs / f"{name}_{time.strftime('%Y%m%d_%H%M%S')}.log"
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(message)s",
        handlers=[logging.FileHandler(log_path, encoding="utf-8"), logging.StreamHandler(sys.stdout)],
    )
    return log_path


def append_experiment(contest_dir: Path, row: dict) -> None:
    path = contest_dir / "experiments.csv"
    fields = [
        "run_id",
        "time",
        "stage",
        "code_version",
        "data_version",
        "config_path",
        "model_path",
        "submission_path",
        "local_metric",
        "online_score",
        "status",
        "notes",
    ]
    exists = path.exists()
    with path.open("a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        if not exists:
            writer.writeheader()
        writer.writerow({k: row.get(k, "") for k in fields})


def summarize_file(path: Path) -> dict:
    item = {"path": str(path), "name": path.name, "bytes": path.stat().st_size, "suffix": path.suffix.lower()}
    try:
        if path.suffix.lower() == ".csv":
            with path.open("r", encoding="utf-8-sig", newline="") as f:
                reader = csv.reader(f)
                header = next(reader, [])
                rows = sum(1 for _ in reader)
            item.update({"rows": rows, "columns": header})
        elif path.suffix.lower() == ".jsonl":
            rows = 0
            keys = set()
            with path.open("r", encoding="utf-8") as f:
                for line in f:
                    if not line.strip():
                        continue
                    rows += 1
                    if rows <= 100:
                        obj = json.loads(line)
                        if isinstance(obj, dict):
                            keys.update(obj.keys())
            item.update({"rows": rows, "columns": sorted(keys)})
        elif path.suffix.lower() == ".json":
            with path.open("r", encoding="utf-8") as f:
                obj = json.load(f)
            if isinstance(obj, list):
                keys = sorted(set().union(*(x.keys() for x in obj[:100] if isinstance(x, dict))))
                item.update({"rows": len(obj), "columns": keys})
            elif isinstance(obj, dict):
                item.update({"rows": 1, "columns": sorted(obj.keys())})
        elif path.suffix.lower() == ".zip":
            with zipfile.ZipFile(path) as zf:
                item.update({"zip_entries": len(zf.namelist()), "zip_sample": zf.namelist()[:20]})
    except Exception as exc:
        item["error"] = str(exc)
    return item


def cmd_inspect(args: argparse.Namespace) -> int:
    contest_dir = current_contest_dir()
    setup_logging(contest_dir, "inspect_data")
    input_dir = Path(args.input) if args.input else contest_dir / "data" / "raw"
    output = Path(args.output) if args.output else contest_dir / "reports" / "data_inventory.json"
    output.parent.mkdir(parents=True, exist_ok=True)
    files = [p for p in input_dir.rglob("*") if p.is_file()] if input_dir.exists() else []
    report = {
        "contest_dir": str(contest_dir),
        "input": str(input_dir),
        "file_count": len(files),
        "files": [summarize_file(p) for p in files],
    }
    output.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    logging.info("wrote %s", output)
    append_experiment(contest_dir, {
        "run_id": time.strftime("inspect_%Y%m%d_%H%M%S"),
        "time": time.strftime("%Y-%m-%d %H:%M:%S"),
        "stage": "inspect",
        "status": "ok" if files else "no_data",
        "notes": f"files={len(files)}",
    })
    return 0


def cmd_make_folds(args: argparse.Namespace) -> int:
    contest_dir = current_contest_dir()
    setup_logging(contest_dir, "make_folds")
    output = Path(args.output) if args.output else contest_dir / "data" / "processed" / "folds.csv"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text("id,fold\n", encoding="utf-8")
    logging.info("created placeholder folds at %s; replace after data download", output)
    append_experiment(contest_dir, {
        "run_id": time.strftime("folds_%Y%m%d_%H%M%S"),
        "time": time.strftime("%Y-%m-%d %H:%M:%S"),
        "stage": "make_folds",
        "status": "placeholder",
        "notes": "waiting for official data",
    })
    return 0


def cmd_train(args: argparse.Namespace) -> int:
    contest_dir = current_contest_dir()
    setup_logging(contest_dir, "train_baseline")
    report = contest_dir / "reports" / "baseline_blocked.md"
    report.write_text(
        "# Baseline blocked\n\nOfficial data is not available locally yet. Download data first, then replace this placeholder training step.\n",
        encoding="utf-8",
    )
    append_experiment(contest_dir, {
        "run_id": time.strftime("train_%Y%m%d_%H%M%S"),
        "time": time.strftime("%Y-%m-%d %H:%M:%S"),
        "stage": "train",
        "status": "blocked",
        "notes": "official data missing",
    })
    logging.info("baseline blocked until data is available")
    return 0


def cmd_predict(args: argparse.Namespace) -> int:
    contest_dir = current_contest_dir()
    setup_logging(contest_dir, "predict")
    out_dir = contest_dir / "submissions"
    out_dir.mkdir(parents=True, exist_ok=True)
    contest_id = contest_dir.name
    output = Path(args.output) if args.output else out_dir / f"sub_{contest_id}_sample_v001_{time.strftime('%Y%m%d_%H%M%S')}.csv"
    if args.sample and Path(args.sample).exists():
        shutil.copyfile(args.sample, output)
        status = "sample_copy"
    else:
        output.write_text("placeholder\n", encoding="utf-8")
        status = "placeholder"
    append_experiment(contest_dir, {
        "run_id": time.strftime("predict_%Y%m%d_%H%M%S"),
        "time": time.strftime("%Y-%m-%d %H:%M:%S"),
        "stage": "predict",
        "submission_path": str(output),
        "status": status,
        "notes": "not for real Tianchi submission until validated",
    })
    logging.info("wrote %s", output)
    return 0


def validate_jsonl(path: Path) -> list[str]:
    errors = []
    with path.open("r", encoding="utf-8") as f:
        for i, line in enumerate(f, 1):
            if not line.strip():
                continue
            try:
                json.loads(line)
            except Exception as exc:
                errors.append(f"line {i}: {exc}")
                if len(errors) >= 20:
                    break
    return errors


def cmd_validate(args: argparse.Namespace) -> int:
    contest_dir = current_contest_dir()
    setup_logging(contest_dir, "validate_submission")
    path = Path(args.file)
    errors = []
    if not path.exists():
        errors.append(f"missing file: {path}")
    elif path.suffix.lower() == ".jsonl":
        errors.extend(validate_jsonl(path))
    elif path.suffix.lower() == ".json":
        try:
            json.loads(path.read_text(encoding="utf-8"))
        except Exception as exc:
            errors.append(str(exc))
    elif path.suffix.lower() == ".zip":
        try:
            with zipfile.ZipFile(path) as zf:
                bad = zf.testzip()
                if bad:
                    errors.append(f"bad zip entry: {bad}")
        except Exception as exc:
            errors.append(str(exc))
    elif path.suffix.lower() == ".csv":
        try:
            with path.open("r", encoding="utf-8-sig", newline="") as f:
                next(csv.reader(f), None)
        except Exception as exc:
            errors.append(str(exc))
    report = contest_dir / "reports" / f"validation_{time.strftime('%Y%m%d_%H%M%S')}.json"
    report.write_text(json.dumps({"file": str(path), "errors": errors}, ensure_ascii=False, indent=2), encoding="utf-8")
    append_experiment(contest_dir, {
        "run_id": time.strftime("validate_%Y%m%d_%H%M%S"),
        "time": time.strftime("%Y-%m-%d %H:%M:%S"),
        "stage": "validate",
        "submission_path": str(path),
        "status": "failed" if errors else "ok",
        "notes": "; ".join(errors[:3]),
    })
    if errors:
        for error in errors:
            logging.error(error)
        return 1
    logging.info("validation ok: %s", path)
    return 0


def build_parser() -> argparse.ArgumentParser:
    script = Path(sys.argv[0]).stem
    parser = argparse.ArgumentParser()
    parser.add_argument("--input")
    parser.add_argument("--output")
    parser.add_argument("--sample")
    parser.add_argument("--file", default="")
    parser.add_argument("--target")
    parser.add_argument("--id-col", default="id")
    parser.add_argument("--seed", type=int, default=SEED)
    parser.set_defaults(script=script)
    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    script = args.script
    if script == "inspect_data":
        code = cmd_inspect(args)
    elif script == "make_folds":
        code = cmd_make_folds(args)
    elif script == "train_baseline":
        code = cmd_train(args)
    elif script == "predict":
        code = cmd_predict(args)
    elif script == "validate_submission":
        if not args.file:
            parser.error("--file is required for validate_submission")
        code = cmd_validate(args)
    else:
        parser.error(f"unknown script name: {script}")
        code = 2
    raise SystemExit(code)


if __name__ == "__main__":
    main()
