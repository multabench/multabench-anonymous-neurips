import subprocess
from typing import Dict


def get_current_commit_hash() -> str:
    try:
        commit_hash = subprocess.check_output(["git", "rev-parse", "HEAD"]).decode("utf-8").strip()
        return commit_hash[:7]
    except subprocess.CalledProcessError:
        return ""


def wandb_run(exp_name: str, project: str) -> None:
    pass


def wandb_finish(d_summary: Dict):
    print(d_summary)
