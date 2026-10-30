"""Derivations of kind `proof` (protocol formal-0.2, standard S8): what the soundness slice checks without judging the
argument, on the sixteen proofs of Questions Before Priors."""
from machine import schemas
from machine.checks.base import Context
from machine.record import Record
from machine.sieve import soundness
from machine.util import dump_yaml, load_yaml

from conftest import PAPER


def _findings(workspace, edit=None):
    path = workspace / "2-author" / PAPER / "provenance" / "derivations.yaml"
    if edit:
        data = load_yaml(path)
        edit({d["id"]: d for d in data["derivations"]})
        dump_yaml(data, path)
    ctx = Context(record=Record.load(path.parents[1]), actor="author", run_dir=workspace / "run", versions={},
                  tolerance={"k": 3, "quorum": 2, "checks": {}})
    return [(f.finding_class, f.record_pointer, f.standard_pointer.rsplit("#", 1)[1]) for f in soundness.run(ctx)]


def test_the_papers_proofs_are_clean(workspace):
    # the regression for the check's first real run: claims point at summaries of results their proofs use, and
    # they paraphrase the proofs' prose hypotheses; neither is a finding (CHANGES-from-design.md, item 27)
    assert _findings(workspace) == []


def test_a_step_resting_on_nothing_in_the_record_is_a_departure(workspace):
    def unmoor(d):
        d["D7"]["steps"][0]["uses"] = ["appendix/appendix.md#a-lemma-nobody-wrote"]
    assert _findings(workspace, unmoor) == [("standard_departure", "derivations:D7", "S8")]


def test_a_citation_outside_the_record_is_listed_not_checked(workspace):
    def cite(d):
        d["D7"]["steps"][0]["uses"] = ["cited: a textbook on conditional expectation"]
    assert _findings(workspace, cite) == []


def test_proofs_resting_on_each_other_are_a_warrant_gap(workspace):
    def tie(d):
        d["D7"]["steps"][0]["uses"] = [d["D8"]["states"]]
        d["D8"]["steps"][0]["uses"] = [d["D7"]["states"]]
    assert _findings(workspace, tie) == [("warrant_gap", "derivations:D7", "S8"), ("warrant_gap", "derivations:D8", "S8")]


def test_the_schema_asks_a_proof_for_its_steps_and_hypotheses(workspace):
    proof = next(d for d in load_yaml(workspace / "2-author" / PAPER / "provenance" / "derivations.yaml")["derivations"]
                 if d["id"] == "D7")
    assert schemas.errors("derivations", {"derivations": [proof]}) == []
    assert any("steps" in e for e in schemas.errors("derivations", {"derivations": [{**proof, "steps": []}]}))
    bare = {k: v for k, v in proof.items() if k not in ("hypotheses", "conclusion")}
    assert any("hypotheses" in e for e in schemas.errors("derivations", {"derivations": [bare]}))
    assert schemas.errors("derivations", {"derivations": [{"id": "D9", "symbols": {}}]}) == []
