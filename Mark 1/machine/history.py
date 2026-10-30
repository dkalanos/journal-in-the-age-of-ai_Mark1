"""J2 · The review history: the journal's own record of its process on one submission. Append-only."""
import json
from pathlib import Path

from . import paths
from .util import now


def folder(paper_id: str) -> Path:
    return paths.editor() / paper_id


def append(paper_id: str, event: str, **data) -> dict:
    entry = {"at": now(), "event": event, **data}
    path = folder(paper_id) / "history.jsonl"
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as f:
        f.write(json.dumps(entry, ensure_ascii=False) + "\n")
    return entry


def events(paper_id: str) -> list[dict]:
    path = folder(paper_id) / "history.jsonl"
    if not path.exists():
        return []
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def rounds(paper_id: str) -> list[Path]:
    return sorted(folder(paper_id).glob("rounds/r*"), key=lambda p: int(p.name[1:]))


def latest_submission(paper_id: str) -> Path:
    if found := rounds(paper_id):
        return found[-1]
    raise FileNotFoundError(f"{paper_id} has not been submitted; run `mark1 submit {paper_id}` first")
