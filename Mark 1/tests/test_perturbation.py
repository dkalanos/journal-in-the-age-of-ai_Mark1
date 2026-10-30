"""Re-execution under perturbation (standard S9): anchors re-run at other points the assumptions admit."""
from machine import generator, run
from machine.record import Record
from machine.sieve.perturbation import _perturb

from conftest import PAPER


def _rows(workspace) -> dict[str, dict]:
    r = Record.load(workspace / "2-author" / PAPER)
    return {a["id"]: _perturb(r, a) for a in r.anchors}


def test_every_anchor_that_can_be_perturbed_holds_and_the_others_say_why(workspace):
    rows = _rows(workspace)
    assert {k: row["result"] for k, row in rows.items()} == {
        "A1": "not perturbed", "A2": "held", "A3": "held", "A4": "not perturbed", "A5": "held"}
    assert rows["A1"]["detail"] == "the anchor sets no parameter"
    assert "(coherence, warrant) is a symbol of D3 (Coh, W)" in rows["A4"]["detail"]
    assert rows["A2"]["varied"] == ["T"] and rows["A2"]["points"] == 4  # the horizon is a count: 1, 3, 4, 5


def test_a_value_two_formulas_give_at_the_point_is_settled_by_the_other_points(workspace):
    # at beta = 1/2 the coarse firm's payoff 1/4 and the pooled payoff beta/2 coincide; the lab's code is the former
    row = _rows(workspace)["A5"]
    assert row["reading"].startswith("pi_coarse_firm") and row["points"] == 20
    assert "pooled_on_wrong_architecture also gave 0.25 at beta = 0.5 but does not elsewhere" in row["detail"]


def test_code_right_only_at_the_anchors_horizon_is_a_warrant_gap(workspace):
    lab = workspace / "2-author" / PAPER / "materials" / "lab.py"
    old = 'return float(leverage(one if firm == 1 else two, {s: 0 for s in STATES}, T)["B"])'
    lab.write_text(lab.read_text(encoding="utf-8").replace(old, old + " * T / 2"), encoding="utf-8")
    generator.restamp(Record.load(lab.parents[1]))  # as if the author regenerated after the edit
    outcome = run.start(PAPER, "author", deterministic_only=True)
    assert [(f.check, f.finding_class, f.record_pointer) for f in outcome.report.findings] == [
        ("perturbation", "warrant_gap", "anchors:A2")]
    assert "the record's procedure gives" in outcome.report.findings[0].rationale
    assert "| A2 | D2 | T | 4 | failed |" in (outcome.folder / "sieve" / "perturbation.md").read_text(encoding="utf-8")
