from collections import Counter
from dataclasses import dataclass, field, fields
from pathlib import Path

from . import render, schemas
from .pointer import normalize
from .util import dump_json, load_json, write_text

CLASSES = (
    "nonconformance", "claim_unresolved", "pointer_missing", "evidence_partial", "anchor_failed",
    "warrant_gap", "standard_departure", "established_by_prior", "uncovered", "injection",
)


@dataclass
class Finding:
    level: int
    check: str
    finding_class: str
    statement: str
    record_pointer: str
    standard_pointer: str
    main: bool = False
    rationale: str = ""
    model: str = "deterministic"
    model_version: str = ""
    prompt_id: str | None = None
    agreement: str | None = None
    check_version: str = ""
    standard_version: str | None = None
    run_id: str = ""
    id: str = ""
    absent_from_author: bool | None = None

    @property
    def key(self) -> tuple[str, str, str]:
        return self.check, self.finding_class, normalize(self.record_pointer)

    def to_dict(self) -> dict:
        data = {
            "id": self.id, "level": self.level, "check": self.check, "check_version": self.check_version,
            "standard_version": self.standard_version, "record_pointer": self.record_pointer,
            "standard_pointer": self.standard_pointer, "statement": self.statement, "class": self.finding_class,
            "main": self.main, "rationale": self.rationale, "model": self.model, "model_version": self.model_version,
            "prompt_id": self.prompt_id, "agreement": self.agreement, "run_id": self.run_id,
        }
        if self.absent_from_author is not None:
            data["absent_from_author"] = self.absent_from_author
        return data

    @classmethod
    def from_dict(cls, data: dict) -> "Finding":
        data = {**data, "finding_class": data["class"]}
        names = {f.name for f in fields(cls)}
        return cls(**{k: v for k, v in data.items() if k in names})


@dataclass
class FindingsReport:
    header: dict
    findings: list[Finding] = field(default_factory=list)
    below_tolerance: list[Finding] = field(default_factory=list)

    def to_dict(self) -> dict:
        return {
            **self.header,
            "below_tolerance": [f.to_dict() for f in self.below_tolerance],
            "findings": [f.to_dict() for f in self.findings],
        }

    def write(self, folder: Path) -> Path:
        data = self.to_dict()
        schemas.validate("findings-report", data)
        dump_json(data, folder / "findings.json")
        write_text(folder / "findings.md", render.findings(self), rtf=True)
        return folder / "findings.json"

    @classmethod
    def load(cls, path: Path) -> "FindingsReport":
        data = load_json(path)
        findings = [Finding.from_dict(f) for f in data.pop("findings")]
        below = [Finding.from_dict(f) for f in data.pop("below_tolerance", [])]
        return cls(header=data, findings=findings, below_tolerance=below)


def assign_ids(findings: list[Finding]) -> None:
    findings.sort(key=lambda f: (f.level, f.check, normalize(f.record_pointer), f.finding_class, f.statement))
    seen = Counter()
    for f in findings:
        seen[f.level, f.check] += 1
        f.id = f"F-{f.level}-{f.check}-{seen[f.level, f.check]:02d}"
