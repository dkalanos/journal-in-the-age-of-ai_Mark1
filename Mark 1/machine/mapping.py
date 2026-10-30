"""Object 4 · The published mapping from findings to the standard action at intake (appendix D.3)."""
from dataclasses import dataclass

from . import paths
from .findings import Finding
from .util import load_yaml


@dataclass
class StandardAction:
    action: str
    fired: list[dict]


def load() -> dict:
    return load_yaml(paths.journal() / "mapping.yaml")


def standard_action(findings: list[Finding], passes_used: int, mapping: dict | None = None) -> StandardAction:
    mapping = mapping or load()
    exhausted = passes_used >= mapping["two_pass_bound"]
    fired = []
    for f in findings:
        rule = next((r for r in mapping["rules"] if _matches(r["when"], f, exhausted)), None)
        fired.append({"rule": rule["id"] if rule else "unmatched", "finding": f.id, "class": f.finding_class,
                      "action": rule["action"] if rule else mapping["unmatched"]})
    if not fired:
        return StandardAction(mapping["no_findings"], [])
    return StandardAction(min((x["action"] for x in fired), key=mapping["severity"].index), fired)


def direction(standard: str, chosen: str, mapping: dict) -> str:
    return "stricter" if mapping["severity"].index(chosen) < mapping["severity"].index(standard) else "more_lenient"


def _matches(when: dict, f: Finding, exhausted: bool) -> bool:
    if "class" in when and f.finding_class not in when["class"]:
        return False
    if "main" in when and f.main != when["main"]:
        return False
    return "passes_exhausted" not in when or exhausted == when["passes_exhausted"]
