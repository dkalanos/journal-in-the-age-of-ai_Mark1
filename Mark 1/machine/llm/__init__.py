from dataclasses import dataclass
from pathlib import Path
from typing import Protocol

from ..pointer import Span
from ..record import Record


@dataclass(frozen=True)
class Answer:
    k: int
    payload: dict
    model: str
    model_version: str
    answered_by: str
    injection_observed: list[dict]


class Pending(Exception):
    def __init__(self, prompts: list[Path]):
        self.prompts = prompts
        super().__init__(f"{len(prompts)} bundle(s) waiting for an answer")


class InvalidResponse(ValueError):
    pass


class RecordChanged(RuntimeError):
    pass


class Backend(Protocol):
    name: str
    answers: dict[str, list[Answer]]

    def ask(self, check: str, instructions: str, data: str, payload_schema: str, k: int) -> list[Answer]: ...


def channel(record: Record, files: list[str], extras: list[tuple[str, str]] = ()) -> str:
    """The data half of every prompt: record files with line numbers, so answers can point at lines."""
    blocks = [_numbered(rel, record.text(rel)) for rel in files]
    blocks += [f"=== {title} ===\n{body.strip()}" for title, body in extras]
    return "\n\n".join(blocks)


def excerpt(span: Span) -> str:
    lines = span.text.splitlines()
    width = len(str(span.start + len(lines)))
    return "\n".join(f"{n:>{width}} | {line}" for n, line in enumerate(lines, span.start))


def _numbered(rel: str, text: str) -> str:
    lines = text.splitlines()
    width = len(str(len(lines)))
    return f"=== {rel} ===\n" + "\n".join(f"{n:>{width}} | {line}" for n, line in enumerate(lines, 1))
