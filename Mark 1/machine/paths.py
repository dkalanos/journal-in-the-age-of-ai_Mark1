import os
from pathlib import Path

PACKAGE_ROOT = Path(__file__).resolve().parents[1]


def root() -> Path:
    return Path(os.environ.get("MARK1_ROOT", PACKAGE_ROOT))


# One folder per party, numbered in the order the paper travels; see README.md.

def journal() -> Path:
    return root() / "1-journal"


def corpus() -> Path:
    return journal() / "corpus"


def records() -> Path:
    return root() / "2-author"


def editor() -> Path:
    return root() / "3-editor"


def intake(paper_id: str) -> Path:
    return editor() / paper_id / "intake"


def reviewers(paper_id: str) -> Path:
    return root() / "4-reviewers" / paper_id


def published(paper_id: str) -> Path:
    return root() / "5-published" / paper_id


def evaluation() -> Path:
    return root() / "evaluation"


def record_dir(arg: str | Path) -> Path:
    """A paper id under 2-author/, or a path to any record folder (e.g. a defected copy)."""
    candidate = Path(arg)
    if (candidate / "record.yaml").exists():
        return candidate.resolve()
    by_id = records() / str(arg)
    if (by_id / "record.yaml").exists():
        return by_id
    raise FileNotFoundError(f"no record at {arg!s} or 2-author/{arg!s}")


def relative(path: Path) -> str:
    try:
        return path.resolve().relative_to(root().resolve()).as_posix()
    except ValueError:
        return path.as_posix()
