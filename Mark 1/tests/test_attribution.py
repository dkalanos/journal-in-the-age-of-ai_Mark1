"""J2: who changed what between two rounds, read from the AI-use record and the generator stamp."""
import shutil

import pytest

from machine import attribution
from machine.record import Record
from machine.util import dump_yaml, load_yaml

from conftest import PAPER

ROUND_1_SUBMITTED = "2026-10-20T23:16:00Z"
LIMIT = "but not creation of the analyst's ontology or a new kind of causal mechanism."


@pytest.fixture
def rounds(workspace, tmp_path):
    source = workspace / "2-author" / PAPER
    old, new = tmp_path / "r1", tmp_path / "r2"
    for target in (old, new):
        shutil.copytree(source, target, ignore=shutil.ignore_patterns("self-check", "__pycache__", "*.rtf"))
        ai_use = load_yaml(target / "provenance" / "ai-use.yaml")  # each test declares the history it needs,
        dump_yaml({**ai_use, "entries": []}, target / "provenance" / "ai-use.yaml")  # not the live record's
    return old, new


def _edit(path, old_text, new_text):
    path.write_text(path.read_text(encoding="utf-8").replace(old_text, new_text), encoding="utf-8")


def _declare(root, **entry):
    ai_use = load_yaml(root / "provenance" / "ai-use.yaml")
    ai_use["entries"].append({"tool": "Claude Code", "model_version": "claude-opus-5-5", "role": "editing",
                              "date": "2026-10-22", "human_direction": "Tighten the contribution statement.", **entry})
    dump_yaml(ai_use, root / "provenance" / "ai-use.yaml")


def _who(old, new):
    found = attribution.attribute(Record.load(old), Record.load(new), ROUND_1_SUBMITTED)
    return {c["file"]: c["by"] for c in found["changes"]}, found


def test_unchanged_rounds_attribute_nothing(rounds):
    assert _who(*rounds)[0] == {}


def test_a_change_declared_as_ai_use_is_the_ais(rounds):
    old, new = rounds
    _edit(new / "appendix" / "appendix.md", LIMIT, LIMIT + " Nor does it model learning across generations.")
    _declare(new, scope_pointer="appendix/appendix.md#does-not-claim")
    who, found = _who(old, new)
    assert who == {"appendix/appendix.md": "ai", "provenance/ai-use.yaml": "ai_use_record"}
    assert "Tighten the contribution statement." in found["changes"][0]["basis"]


def test_an_undeclared_change_to_a_file_with_no_ai_history_is_the_authors(rounds):
    old, new = rounds
    _edit(new / "appendix" / "appendix.md", LIMIT, LIMIT + " Nor does it model learning across generations.")
    assert _who(old, new)[0] == {"appendix/appendix.md": "author"}


def test_an_undeclared_change_to_a_file_ai_drafted_before_says_so(rounds):
    old, new = rounds
    for root in (old, new):
        _declare(root, role="record_keeping", scope_pointer="paper/paper.md", date="2026-10-21")
    _edit(new / "paper" / "paper.md", "No sequence of such updates makes", "No sequence of such updates ever makes")
    who, found = _who(old, new)
    assert who == {"paper/paper.md": "undeclared"}
    assert "Claude Code (record_keeping)" in found["changes"][0]["basis"]


def test_an_ai_appendix_file_off_its_stamp_was_edited_after_generation(rounds):
    old, new = rounds
    _edit(new / "ai-appendix" / "claims.yaml", "Existing work explains", "Prior work explains")
    assert _who(old, new)[0] == {"ai-appendix/claims.yaml": "edited_after_generation"}


def test_an_ai_appendix_file_off_its_stamp_with_a_declaration_is_the_ais(rounds):
    old, new = rounds
    _edit(new / "ai-appendix" / "claims.yaml", "Existing work explains", "Prior work explains")
    _declare(new, scope_pointer="ai-appendix/claims.yaml", human_direction="Correct the claims list before submission.")
    who, found = _who(old, new)
    assert who["ai-appendix/claims.yaml"] == "ai"
    basis = next(c["basis"] for c in found["changes"] if c["file"] == "ai-appendix/claims.yaml")
    assert "does not match the stamp of generator run" in basis
    assert "Correct the claims list before submission." in basis


def test_an_ai_appendix_file_off_its_stamp_declared_only_in_an_earlier_round_says_so(rounds):
    old, new = rounds
    for root in (old, new):
        _declare(root, scope_pointer="ai-appendix/claims.yaml", date="2026-10-19")
    _edit(new / "ai-appendix" / "claims.yaml", "Existing work explains", "Prior work explains")
    who, found = _who(old, new)
    assert who == {"ai-appendix/claims.yaml": "undeclared"}
    assert "does not match the stamp of generator run" in found["changes"][0]["basis"]


def test_a_declaration_dated_before_the_last_submission_is_flagged(rounds):
    old, new = rounds
    _declare(new, scope_pointer="paper/paper.md", date="2026-10-19")
    _declare(new, scope_pointer="paper/", date="2026-08")
    found = _who(old, new)[1]
    assert [e["date"] for e in found["declared_late"]] == ["2026-10-19", "2026-08"]


def test_a_declaration_dated_after_the_last_submission_is_not(rounds):
    old, new = rounds
    _declare(new, scope_pointer="paper/paper.md", date="2026-10-21")
    _declare(new, scope_pointer="paper/paper.md", date="2026-10")  # same month: cannot tell, so not flagged
    assert _who(old, new)[1]["declared_late"] == []


def test_each_round_lists_the_declarations_it_adds(rounds):
    old, new = rounds
    assert _who(old, new)[1]["declared"] == []
    _declare(new, scope_pointer="appendix/appendix.md#does-not-claim")
    declared = _who(old, new)[1]["declared"]
    assert [(e["tool"], e["scope_pointer"]) for e in declared] == [("Claude Code", "appendix/appendix.md#does-not-claim")]


def test_a_first_submission_says_who_made_every_file(rounds):
    _, record = rounds
    found = attribution.attribute(None, Record.load(record))
    who = {c["file"]: c["by"] for c in found["changes"]}
    assert set(who) == set(attribution.changed_files(None, Record.load(record)))
    assert who["provenance/ai-use.yaml"] == "ai_use_record"
    assert who["ai-appendix/claims.yaml"] == "generator"
    assert len(found["declared"]) == len(load_yaml(record / "provenance" / "ai-use.yaml")["entries"])
    assert "undeclared" not in who.values()
