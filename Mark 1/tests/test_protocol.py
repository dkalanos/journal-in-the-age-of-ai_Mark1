import pytest

from machine import schemas
from machine.pointer import Unresolvable, resolve, slug
from machine.record import Record

from conftest import PAPER

TABLES = [
    ("record.yaml", "record"),
    ("declarations.yaml", "declarations"),
    ("ai-appendix/claims.yaml", "claims"),
    ("ai-appendix/anchors.yaml", "anchors"),
    ("ai-appendix/generated.yaml", "generated"),
    ("provenance/derivations.yaml", "derivations"),
    ("provenance/ai-use.yaml", "ai-use"),
]


@pytest.fixture
def record(workspace):
    return Record.load(workspace / "2-author" / PAPER)


@pytest.mark.parametrize("rel, name", TABLES)
def test_fixture_tables_conform(record, rel, name):
    assert schemas.errors(name, record.table(rel)) == []


def test_a_missing_required_field_is_caught(record):
    claims = record.table("ai-appendix/claims.yaml")
    del claims["claims"][0]["evidence_pointer"]
    assert any("evidence_pointer" in e for e in schemas.errors("claims", claims))


def test_section_pointer_resolves_to_the_whole_section(record):
    span = resolve(record, "paper/paper.md#prop-no-emergence")
    assert span.text.startswith("### Proposition 5.1 (No Bayesian emergence)")
    assert "#### Proof" in span.text  # a subsection belongs to its section
    assert "self-sealing" not in span.text


def test_line_and_table_pointers(record):
    assert "No sequence of such updates" in resolve(record, "paper/paper.md:L373").text
    span = resolve(record, "claims:C19")
    assert span.file == "ai-appendix/claims.yaml" and "comparative_static" in span.text


@pytest.mark.parametrize("pointer", ["paper/paper.md#nowhere", "claims:C99", "paper/paper.md:L99999", "../secret.md", "nope.md"])
def test_unresolvable_pointers_raise(record, pointer):
    with pytest.raises(Unresolvable):
        resolve(record, pointer)


def test_slug_matches_heading_text():
    assert slug("A.1 Derivation of Proposition 1") == "a1-derivation-of-proposition-1"
