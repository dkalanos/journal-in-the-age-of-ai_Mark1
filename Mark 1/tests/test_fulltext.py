"""Introductions for the evidence map, with the network stubbed: what is cut, what is kept, what is said."""
from machine import corpus, fulltext

BODY = " ".join(f"word{i}" for i in range(2000))
PDF_TEXT = f"A Title\nAbstract. Short.\n1. Introduction\n{BODY}\n2. The Model\nAssume a firm."


def _get(work_url, params):
    return {"best_oa_location": {"pdf_url": "https://example.org/a.pdf"}, "locations": []}


def test_the_excerpt_starts_at_the_introduction_and_is_capped():
    excerpt, where = fulltext.cut(PDF_TEXT)
    assert where == "introduction heading"
    assert excerpt.split()[0] == "word0" and len(excerpt.split()) == fulltext.WORDS


def test_the_excerpt_stops_at_the_next_section():
    excerpt, _ = fulltext.cut(f"1 Introduction\n{' '.join(['gap'] * 300)}\n2 Related Work\nNot this.")
    assert "Related" not in excerpt and len(excerpt.split()) == 300


def test_a_page_with_too_little_text_is_no_introduction():
    assert fulltext.cut("Cover page\nDownloaded from somewhere") == (None, None)


def test_only_candidates_with_a_fetchable_copy_get_one_and_only_up_to_the_limit():
    items = [{"id": "W1", "openalex_id": "W1", "title": "A Title"}, {"id": "W2", "openalex_id": "W2", "title": "A Title"},
             {"id": "hand", "doi": None}]
    texts = fulltext.introductions(items, 20, get=_get, download=lambda url: PDF_TEXT)
    assert set(texts) == {"W1", "W2"}  # the hand-listed item has no OpenAlex record to find a copy through
    assert texts["W1"]["source"] == "https://example.org/a.pdf" and texts["W1"]["words"] == fulltext.WORDS
    assert set(fulltext.introductions(items, 1, get=_get, download=lambda url: PDF_TEXT)) == {"W1"}
    assert fulltext.introductions(items, 20, get=_get, download=lambda url: None) == {}  # a landing page, not a PDF


def test_the_model_sees_the_introduction_and_coverage_counts_it():
    items = [{"id": "W1", "title": "T", "abstract": "A.", "introduction": {"words": 5}, "introduction_text": "Intro."},
             {"id": "W2", "title": "U", "abstract": "B."}]
    assert "introduction: Intro." in corpus.prompt_text(items)
    cov = corpus.coverage({"candidates": items, "procedure": "test", "hand_list": 0}, set())
    assert cov["with_introduction"] == 1 and "1 were also read from their introduction (0 from" in cov["statement"]


def test_a_copy_that_is_not_the_paper_is_not_used():
    items = [{"id": "W1", "openalex_id": "W1", "title": "Firm Resources and Sustained Competitive Advantage"}]
    issue = "Revista Innova, Enero - Junio 2021\n1. Introduction\n" + BODY
    assert fulltext.introductions(items, 20, get=_get, download=lambda url: issue) == {}


def test_a_licensed_copy_named_by_doi_is_read_before_any_open_access_copy(tmp_path, monkeypatch):
    shelf = tmp_path / "licensed"
    shelf.mkdir()
    (shelf / "10.1016 j jet.2005.02.007.pdf").write_bytes(b"%PDF stub")
    monkeypatch.setattr(fulltext, "_pdf_text", lambda data: PDF_TEXT)
    items = [{"id": "W9", "openalex_id": "W9", "doi": "10.1016/j.jet.2005.02.007", "title": "A Title"}]
    texts = fulltext.introductions(items, 20, get=_get, download=lambda url: None, licensed=shelf)
    assert texts["W9"]["via"] == "licensed" and texts["W9"]["source"].endswith("jet.2005.02.007.pdf")


def test_a_numbered_footnote_on_the_first_page_does_not_end_the_introduction():
    text = f"1. Introduction\nIt is hard to argue.\n2 Financial support is acknowledged.\n{BODY}\n2. The Model\nX."
    excerpt, _ = fulltext.cut(text)
    assert "Financial support" in excerpt and len(excerpt.split()) == fulltext.WORDS


def test_licensed_copies_take_the_limit_before_open_access_ones(tmp_path, monkeypatch):
    shelf = tmp_path / "licensed"
    shelf.mkdir()
    (shelf / "W3.pdf").write_bytes(b"%PDF stub")
    monkeypatch.setattr(fulltext, "_pdf_text", lambda data: PDF_TEXT)
    items = [{"id": f"W{n}", "openalex_id": f"W{n}", "title": "A Title"} for n in (1, 2, 3)]
    texts = fulltext.introductions(items, 2, get=_get, download=lambda url: PDF_TEXT, licensed=shelf)
    assert {k: v["via"] for k, v in texts.items()} == {"W3": "licensed", "W1": "open access"}
