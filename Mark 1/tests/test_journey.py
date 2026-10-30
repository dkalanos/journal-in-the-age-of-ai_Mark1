"""One paper through the whole system, model answers canned: submission to certificate and publication."""
import shutil

import pytest

from machine import generator, history, run, schemas, stats, workflow
from machine.record import Record
from machine.state import StateError, state
from machine.util import dump_yaml, load_json, load_yaml

from conftest import PAPER, answer

LIMIT = "but not creation of the analyst's ontology or a new kind of causal mechanism."


def checked(actor: str, **answers) -> run.Outcome:
    outcome = run.start(PAPER, actor)
    if outcome.pending:
        answer(outcome.folder, **answers)
        outcome = run.resume(outcome.run_id)
    assert not outcome.pending
    return outcome


@pytest.fixture
def at_intake(workspace):
    # the round-2 revision below lands in the appendix: give it a file the AI-use record never names
    ai_use = workspace / "2-author" / PAPER / "provenance" / "ai-use.yaml"
    declared = load_yaml(ai_use)
    dump_yaml({**declared, "entries": [e for e in declared["entries"]
                                       if not str(e.get("scope_pointer", "")).startswith("appendix/")]}, ai_use)
    checked("author", contribution="contribution-question.json")
    workflow.submit(PAPER)
    return checked("journal", contribution="contribution-question.json")


def test_journal_run_is_compared_with_the_author_run(at_intake):
    assert (at_intake.folder / "diff-vs-author.md").exists()
    assert all(f.absent_from_author is False for f in at_intake.report.findings)
    assert state(PAPER).name == "checked"


def test_departing_from_the_standard_action_needs_a_reason(at_intake):
    with pytest.raises(StateError, match="--reason"):
        workflow.intake(PAPER, at_intake.run_id, "Ed Itor", action="return_without_review")
    decision = workflow.intake(PAPER, at_intake.run_id, "Ed Itor", action="return_without_review", reason="testing")
    assert decision["departure"]["direction"] == "stricter"
    md, csv = stats.departures()
    assert "| Ed Itor | 1 | 1 | 100% | 1 | 0 |" in md.read_text(encoding="utf-8")


def test_issue_refuses_before_interest_and_writes_nothing(at_intake, workspace):
    workflow.intake(PAPER, at_intake.run_id, "Ed Itor")
    with pytest.raises(StateError):
        workflow.issue(PAPER, "Ed Itor")
    assert not (workspace / "5-published" / PAPER).exists()
    assert history.events(PAPER)[-1]["event"] == "issue_refused"


def test_replay_reproduces_the_journal_run(at_intake):
    _, differences = run.replay(at_intake.run_id)
    assert differences == []


def test_replay_without_the_stored_answers_says_so_and_writes_nothing(at_intake):
    shutil.rmtree(at_intake.folder / "bundles")
    with pytest.raises(FileNotFoundError, match="not in this repository"):
        run.replay(at_intake.run_id)
    assert not (at_intake.folder.parent / f"{at_intake.run_id}-replay").exists()


def test_replay_with_some_answers_missing_cannot_finish(at_intake):
    shutil.rmtree(at_intake.folder / "bundles" / "contribution")
    outcome, differences = run.replay(at_intake.run_id)
    assert outcome.pending and outcome.report is None
    assert differences == [f"{len(outcome.pending)} answer(s) missing from the stored run"]


def test_the_whole_path_to_a_certificate(at_intake, workspace, tmp_path):
    decision = workflow.intake(PAPER, at_intake.run_id, "Ed Itor")
    assert decision["action"] == "proceed_to_review" and decision["departure"] is None

    reply = tmp_path / "answer.md"
    reply.write_text("We accept the map's reading of the nearest work.", encoding="utf-8")
    workflow.answer(PAPER, reply)
    with pytest.raises(StateError, match="once"):
        workflow.answer(PAPER, reply)
    workflow.new(PAPER, "Ed Itor", kind="question")
    packet = workflow.packet(PAPER)
    assert {p.name for p in packet.iterdir()} >= {"paper", "appendix", "findings.md", "evidence-map.md", "README.md"}

    report = tmp_path / "report.md"
    report.write_text("Interesting; please say what the model leaves out across generations.", encoding="utf-8")
    with pytest.raises(StateError, match="reports"):
        workflow.revise(PAPER, "Ed Itor", "Too early: no reviewer has reported.")
    workflow.report(PAPER, "Rev One", report)
    note = workflow.revise(PAPER, "Ed Itor", "Rev One asks for one more limitation.")
    assert state(PAPER).name == "revise_requested" and "r1-rev-one.md" in note.read_text(encoding="utf-8")

    # round 2: the author revises within the existing record, the author's AI restamps, both sides re-run
    appendix = workspace / "2-author" / PAPER / "appendix" / "appendix.md"
    appendix.write_text(appendix.read_text(encoding="utf-8").replace(
        LIMIT, LIMIT + " Nor does it model learning across generations."), encoding="utf-8")
    generator.restamp(Record.load(workspace / "2-author" / PAPER))
    checked("author", contribution="contribution-question.json")
    workflow.submit(PAPER)
    assert state(PAPER).name == "submitted"  # a revision is a new submission: checked, then intake (Fig. 4, A5)
    revised = checked("journal", contribution="contribution-question.json")
    assert state(PAPER).name == "checked"
    workflow.intake(PAPER, revised.run_id, "Ed Itor")
    assert state(PAPER).name == "in_review"  # "new" was signed in round 1 and is not signed again
    round_diff = workflow.diff(PAPER, 1, 2).read_text(encoding="utf-8")
    assert "learning across generations" in round_diff
    # the revision was not declared as AI use, so the review history gives it to the author
    resubmitted = [e for e in history.events(PAPER) if e["event"] == "submitted"][-1]
    assert resubmitted["changed_by"]["appendix/appendix.md"] == "author"
    assert "| `appendix/appendix.md` | the author |" in round_diff
    assert "_No AI-use entry was added in round 2._" in round_diff
    first = workflow.diff(PAPER, 0, 1).read_text(encoding="utf-8")
    assert "## Who made it" in first and "## Files" not in first

    with pytest.raises(StateError, match="two distinct"):
        workflow.interest(PAPER, "Ed Itor", ["Rev One", "Rev One"], True, "Of interest.")
    workflow.interest(PAPER, "Ed Itor", ["Rev One", "Rev Two"], True, "Of interest to formal strategy theorists.")
    with pytest.raises(StateError, match="editor who signed"):
        workflow.issue(PAPER, "Rev One")
    cert, pub = workflow.issue(PAPER, "Ed Itor")

    certificate = load_yaml(cert / "certificate.yaml")
    assert schemas.errors("certificate", certificate) == []
    assert certificate["signed_by"] == ["Ed Itor", "Rev One", "Rev Two"]
    assert certificate["new"]["kind"] == "question"
    assert schemas.errors("publication", load_yaml(pub / "manifest.yaml")) == []
    assert state(PAPER).name == "certified"
    with pytest.raises(StateError):
        workflow.issue(PAPER, "Ed Itor")


def test_not_new_returns_the_record_with_the_map(workspace, tmp_path):
    checked("author")
    workflow.submit(PAPER)
    outcome = checked("journal")
    assert [f.finding_class for f in outcome.report.findings] == ["established_by_prior"]
    workflow.intake(PAPER, outcome.run_id, "Ed Itor")
    reply = tmp_path / "answer.md"
    reply.write_text("No answer.", encoding="utf-8")
    workflow.answer(PAPER, reply)
    with pytest.raises(StateError, match="not on the map"):
        workflow.new(PAPER, "Ed Itor", not_new_because=["gavetti-levinthal-2000"])
    workflow.new(PAPER, "Ed Itor", not_new_because=["karni-viero-2013"])
    assert state(PAPER).name == "returned"
    assert not (workspace / "5-published" / PAPER).exists()


def test_a_revision_goes_back_through_intake_and_still_owes_new(at_intake, tmp_path):
    workflow.intake(PAPER, at_intake.run_id, "Ed Itor")
    workflow.defer_new(PAPER, "Ed Itor", "Review proceeds before 'new' is signed.")
    assert state(PAPER).name == "in_review"
    workflow.packet(PAPER)
    report = tmp_path / "report.md"
    report.write_text("Revise.", encoding="utf-8")
    workflow.report(PAPER, "Rev One", report)
    workflow.revise(PAPER, "Ed Itor", "Rev One asks for revisions.")
    workflow.submit(PAPER)
    assert state(PAPER).name == "submitted"
    revised = checked("journal", contribution="contribution-question.json")
    with pytest.raises(StateError, match="latest journal run"):
        workflow.intake(PAPER, at_intake.run_id, "Ed Itor")
    workflow.intake(PAPER, revised.run_id, "Ed Itor")
    assert state(PAPER).name == "awaiting_new"  # deferred in round 1, still owed after round 2's intake


def test_signing_new_against_the_map_needs_a_reason(at_intake, tmp_path):
    """formal-0.5: the map proposes the kind on the question as the paper states it; another reading is signed with why."""
    emap = load_json(at_intake.folder / "sieve" / "evidence-map.json")
    assert emap["claims"][0]["question"]["stated_by"] == "author"
    workflow.intake(PAPER, at_intake.run_id, "Ed Itor")
    reply = tmp_path / "answer.md"
    reply.write_text("Noted.", encoding="utf-8")
    workflow.answer(PAPER, reply)
    with pytest.raises(StateError, match="reason"):
        workflow.new(PAPER, "Ed Itor", kind="answer")
    rec = workflow.new(PAPER, "Ed Itor", kind="answer", question_as_read="Where do strategic theories come from?",
                       reason="Read at the breadth of the paper's opening line, the question is one Felin and Zenger pose.")
    assert rec["map_kind"] == "question" and rec["departure"] is True
    assert load_yaml(at_intake.folder.parents[1] / "new.yaml")["departure"] is True
