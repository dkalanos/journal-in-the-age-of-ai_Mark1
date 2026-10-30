"""Retrieval for the evidence map with OpenAlex faked: queries, the venue filter, the snowball, assembly;
and bundles answered under an earlier check version."""
import pytest
import yaml

from machine import retrieval
from machine.llm import Pending, RecordChanged
from machine.llm.bundle import BundleBackend
from machine.util import dump_json

from test_bundles import respond

TITLE = "Cost pass-through under linear demand: a worked note"
CLAIM = {"id": "C4", "text": "For demand q = a - p with a > c >= 0, the note gives the pass-through of marginal "
                             "cost to price in closed form: exactly one half, whatever the demand intercept a."}


def work(wid, title, source="S1", refs=(), year=2000, abstract=True):
    return {"id": f"https://openalex.org/{wid}", "doi": f"https://doi.org/10.1/{wid}", "title": title,
            "publication_year": year, "authorships": [{"author": {"display_name": "Ann Author"}}],
            "primary_location": {"source": {"id": f"https://openalex.org/{source}", "display_name": source}},
            "abstract_inverted_index": {"word": [0]} if abstract else None, "topics": [], "cited_by_count": 5,
            "referenced_works": [f"https://openalex.org/{r}" for r in refs], "relevance_score": 1.0}


OLD_NOTE = work("W9", "A Note on the Effect of Cost Changes on Prices", year=1983, abstract=False)
OUTSIDE = work("W8", "Also cited, but published outside the venues", source="S99")


def fake_get(url, params):
    flt = params.get("filter", "")
    if "openalex:" in flt:
        wanted = flt.split("openalex:")[1].split(",")[0].split("|")
        return {"results": [w for w in (OLD_NOTE, OUTSIDE) if w["id"].rsplit("/", 1)[-1] in wanted]}
    if "doi:" in flt:
        return {"results": []}
    return {"results": [work("W1", "Pass-through as an economic tool", refs=("W9", "W8")),
                        work("W2", "Multiproduct cost pass-through", refs=("W9", "W8"))]}


@pytest.fixture
def venues(workspace):
    folder = workspace / "1-journal" / "corpus"
    cfg = {"version": "test", "search": ["test"], "hand_list": False, "lists": {"test": {"name": "Test list"}},
           "journals": [{"name": "Journal One", "issn": ["1111-1111"], "lists": ["test"]},
                        {"name": "Unresolved Journal", "issn": ["2222-2222"], "lists": ["test"]}]}
    (folder / "venues.yaml").write_text(yaml.safe_dump(cfg), encoding="utf-8")
    dump_json({"1111-1111": {"id": "S1", "name": "Journal One", "type": "journal"}, "2222-2222": None},
              folder / "sources.json")
    return folder


def test_queries_come_from_the_claim_and_the_title():
    qs = retrieval.queries(TITLE, [CLAIM])
    assert {q["kind"] for q in qs} == {"search", "title"}
    assert any(q["q"] == "demand pass-through cost" for q in qs)  # the words the claim shares with the title
    assert all("exactly" not in q["q"] for q in qs)


def test_snowball_reaches_the_antecedent_the_hits_cite_when_it_is_in_the_venues(venues):
    found = retrieval.search(TITLE, [CLAIM], set(), get=fake_get)
    ids = [c["id"] for c in found["candidates"]]
    assert ids[0] == "W9" and "W8" not in ids
    note = found["candidates"][0]
    assert note["found_by"] == ["cited by 2 of the retrieved works"] and note["abstract"] is None
    assert found["snowball"]["out_of_venue"] == 1
    assert found["venues"] == {"lists": ["test"], "journals": 2, "resolved": 1, "unresolved": ["Unresolved Journal"]}
    assert all(q["hits"] == 2 for q in found["queries"])


def test_search_refuses_without_a_resolved_venue(venues):
    dump_json({"1111-1111": None, "2222-2222": None}, venues / "sources.json")
    with pytest.raises(retrieval.Unavailable, match="mark1 corpus"):
        retrieval.search(TITLE, [CLAIM], set(), get=fake_get)


def test_bundles_from_an_earlier_check_version_are_read_as_they_are(workspace, tmp_path):
    folder = tmp_path / "bundles" / "completeness"
    with pytest.raises(Pending):
        BundleBackend(tmp_path, "0.1.0").ask("completeness", "old instructions", "old data", "payload-completeness", 2)
    respond(folder, 1)
    with pytest.raises(RecordChanged, match="incomplete"):
        BundleBackend(tmp_path, "0.2.0").ask("completeness", "new instructions", "new data", "payload-completeness", 2)
    respond(folder, 2)
    answers = BundleBackend(tmp_path, "0.2.0").ask("completeness", "new instructions", "new data", "payload-completeness", 2)
    assert [a.k for a in answers] == [1, 2]
