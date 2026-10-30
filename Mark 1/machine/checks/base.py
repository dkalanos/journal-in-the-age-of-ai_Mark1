from collections.abc import Callable
from dataclasses import dataclass, field
from pathlib import Path

from .. import paths
from ..findings import Finding
from ..llm import Answer, Backend
from ..record import Record

PROTOCOL = "protocol/formal.md"
STANDARD = "standard/formal.md"


class NotRun(Exception):
    """A check that could not run on this record; the reason goes into the findings report."""


@dataclass(frozen=True)
class Check:
    name: str
    level: int
    deterministic: bool
    run: Callable[["Context"], list[Finding]]


@dataclass
class Context:
    record: Record
    actor: str
    run_dir: Path
    versions: dict
    tolerance: dict
    backend: Backend | None = None
    generated_here: bool = False
    submission: dict | None = None
    submission_dir: Path | None = None
    agreement: dict[str, dict] = field(default_factory=dict)
    outputs: dict = field(default_factory=dict)

    @property
    def k(self) -> int:
        return self.tolerance["k"]

    @property
    def quorum(self) -> int:
        return self.tolerance["quorum"]

    def ask(self, check: str, data: str, prompt: str | None = None) -> list[Answer]:
        prompt = prompt or check
        instructions = (paths.journal() / "checks" / "prompts" / f"{prompt}.md").read_text(encoding="utf-8")
        return self.backend.ask(check, instructions, data, f"payload-{prompt}", self.k)

    def note_agreement(self, check: str, value: float) -> None:
        minimum = self.tolerance["checks"][check]["min"]
        self.agreement[check] = {"value": round(value, 3), "min": minimum, "met": value >= minimum}

    def produced_by(self, answers: list[Answer], prompt: str, agreeing: int) -> dict:
        return {
            "model": ", ".join(sorted({a.model for a in answers})),
            "model_version": ", ".join(sorted({a.model_version for a in answers})),
            "prompt_id": f"{prompt}@{self.versions['checks']}",
            "agreement": f"{agreeing}/{len(answers)}",
        }
