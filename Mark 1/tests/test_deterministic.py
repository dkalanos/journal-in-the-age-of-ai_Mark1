from machine import inject, run
from machine.sandbox import run_isolated
from machine.util import dump_yaml, load_yaml

from conftest import PAPER


def test_clean_record_has_no_deterministic_findings(workspace):
    outcome = run.start(PAPER, "author", deterministic_only=True)
    assert outcome.report.findings == []
    assert {c["check"] for c in outcome.report.header["checks_not_run"]} >= {"completeness", "contribution"}


def test_every_planted_defect_is_found_and_nothing_else(workspace):
    inject.inject(PAPER)
    report, passed = inject.evaluate(PAPER)
    assert passed, report.read_text(encoding="utf-8")


def test_anchor_reexecution_is_killed_on_timeout(tmp_path):
    (tmp_path / "materials").mkdir()
    (tmp_path / "materials" / "spin.py").write_text("def spin():\n    while True:\n        pass\n", encoding="utf-8")
    result = run_isolated({"procedure": {"language": "python", "source": "materials/spin.py:spin"}, "kind": "numeric",
                           "expected": 0, "record_root": str(tmp_path)}, timeout=2)
    assert not result["ok"] and "timed out" in result["error"]


def test_hand_edited_ai_appendix_is_a_fact_on_the_report_not_a_finding(workspace):
    """formal-0.3: the AI appendix is the author's; the generator stamp is reported, never flagged (P3)."""
    claims = workspace / "2-author" / PAPER / "ai-appendix" / "claims.yaml"
    data = load_yaml(claims)
    data["claims"][1]["text"] += " (for every agent)"
    dump_yaml(data, claims)
    report = run.start(PAPER, "author", deterministic_only=True).report
    assert report.findings == []
    stamp = report.header["ai_appendix_stamp"]
    assert stamp["matches"] is False and stamp["outputs_edited_since"] == ["ai-appendix/claims.yaml"]


def test_paper_without_front_notice_is_a_form_finding(workspace):
    """formal-0.3, P2: the front notice is a required element of the paper, checked at Level 1."""
    paper = workspace / "2-author" / PAPER / "paper" / "paper.md"
    kept = [line for line in paper.read_text(encoding="utf-8").splitlines() if not line.startswith("**AI appendix.**")]
    paper.write_text("\n".join(kept) + "\n", encoding="utf-8")
    report = run.start(PAPER, "author", deterministic_only=True).report
    assert [(f.finding_class, f.record_pointer) for f in report.findings] == [("nonconformance", "paper/paper.md")]
    assert report.findings[0].standard_pointer.endswith("#P2")


def test_contribution_claim_without_its_question_is_a_form_finding(workspace):
    """formal-0.4, P4: the contribution claim states the question it answers and where the paper states it."""
    claims = workspace / "2-author" / PAPER / "ai-appendix" / "claims.yaml"
    data = load_yaml(claims)
    c1 = next(c for c in data["claims"] if c["kind"] == "contribution")
    del c1["question"], c1["question_pointer"]
    dump_yaml(data, claims)
    report = run.start(PAPER, "author", deterministic_only=True).report
    assert [(f.finding_class, f.record_pointer) for f in report.findings] == [("nonconformance", "claims:C1")]
    assert report.findings[0].standard_pointer.endswith("#P4")
