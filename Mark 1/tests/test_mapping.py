import pytest

from machine import mapping
from machine.findings import Finding


def finding(cls: str, main: bool = False, level: int = 2) -> Finding:
    return Finding(level=level, check="x", finding_class=cls, statement="s", record_pointer="claims:C1",
                   standard_pointer="p", main=main, id=f"F-{cls}")


@pytest.mark.parametrize("findings, passes, action", [
    ([], 0, "proceed_to_review"),
    ([finding("nonconformance", level=1)], 0, "return_for_corrections"),
    ([finding("anchor_failed")], 2, "return_without_review"),
    ([finding("warrant_gap", main=False, level=3)], 0, "proceed_to_review"),
    ([finding("warrant_gap", main=True, level=3)], 0, "return_for_corrections"),
    ([finding("warrant_gap", main=True, level=3)], 2, "return_without_review"),
    ([finding("established_by_prior", main=True, level=3)], 0, "proceed_to_review"),
    ([finding("uncovered", level=3)], 0, "refer_to_specialist"),
    ([finding("injection", level=1), finding("established_by_prior", level=3)], 0, "return_without_review"),
    ([finding("pointer_missing"), finding("uncovered", level=3)], 0, "refer_to_specialist"),
    ([finding("evidence_partial"), finding("evidence_partial", main=True)], 0, "proceed_to_review"),
    ([finding("evidence_partial"), finding("pointer_missing")], 0, "return_for_corrections"),
])
def test_published_mapping(workspace, findings, passes, action):
    assert mapping.standard_action(findings, passes).action == action


def test_every_finding_is_accounted_for(workspace):
    result = mapping.standard_action([finding("anchor_failed"), finding("warrant_gap", level=3)], 0)
    assert [(r["finding"], r["rule"]) for r in result.fired] == [("F-anchor_failed", "R3"), ("F-warrant_gap", "R6")]


def test_departure_direction(workspace):
    rules = mapping.load()
    assert mapping.direction("proceed_to_review", "return_without_review", rules) == "stricter"
    assert mapping.direction("return_for_corrections", "proceed_to_review", rules) == "more_lenient"
