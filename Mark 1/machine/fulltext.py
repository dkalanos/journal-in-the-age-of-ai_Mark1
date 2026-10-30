"""Introductions for the evidence map: where the journal holds a copy of a candidate, the model reads its introduction.

An abstract compresses a paper's contribution; the introduction states it and the gap it fills, which is what
placing a claim needs. A copy is the journal's own licensed one (a folder named in venues.yaml) or an open-access
copy OpenAlex knows of; its text is cut at the "Introduction" heading (or, without one, from the opening pages)
and capped. Without licensed copies most candidates in the journal's venues keep their abstract, since most are
paywalled; the coverage statement says how many were read each way.

The excerpts are other people's text. A run keeps them in sieve/introductions.json and in its prompt bundles,
which replay needs; neither belongs in anything published (machine/README.md).
"""
import io
import logging
import re
import unicodedata
from pathlib import Path

import requests

from . import retrieval
from .util import sha256_text

WORDS = 1200
MIN_WORDS = 150
MAX_BYTES = 20_000_000
PAGES = 10
HEADING = re.compile(r"(?:^|\n)\s*(?:1\.?|I\.?)?\s*introduction\s*\n", re.I)
NEXT = re.compile(r"\n\s*(?:2\.?|II\.?)\s+[A-Z][^\n]{2,80}\n")
logging.getLogger("pypdf").setLevel(logging.ERROR)  # font and xref warnings on stderr, one per page


def introductions(items: list[dict], limit: int, get=None, download=None,
                  licensed: Path | None = None) -> dict[str, dict]:
    """{candidate id: {text, source, via, from, words, sha}}: up to `limit` excerpts.

    licensed: a folder of the journal's own copies, named by OpenAlex id or DOI. Those are read first, down the
    whole candidate list; open-access copies fill what remains of the limit."""
    get, download = get or retrieval.fetch, download or _download
    shelf = {_key(p.stem): p for p in licensed.glob("*.pdf")} if licensed and licensed.is_dir() else {}
    found: dict[str, dict] = {}

    def take(item: dict, copies) -> None:
        for source, via, read in copies:
            text = read()
            if not text or not is_the_paper(text, item.get("title") or ""):
                continue  # repositories, and people, sometimes file a different document under the work
            excerpt, where = cut(text)
            if excerpt:
                found[item["id"]] = {"text": excerpt, "source": source, "via": via, "from": where,
                                     "words": len(excerpt.split()), "sha": sha256_text(excerpt)}
                return

    for item in items:
        if len(found) == limit:
            return found
        held = {shelf.get(_key(k)) for k in (item.get("id"), item.get("doi")) if k} - {None}
        take(item, [(f"licensed copy {p.name}", "licensed", lambda p=p: _pdf_text(p.read_bytes())) for p in held])
    for item in items:
        if len(found) == limit:
            break
        if item["id"] not in found and item.get("openalex_id"):
            take(item, [(url, "open access", lambda url=url: download(url)) for url in _open_copies(get, item)])
    return found


def _open_copies(get, item: dict) -> list[str]:
    try:
        return _pdf_urls(get(f"{retrieval.API}/works/{item['openalex_id']}", {"select": "best_oa_location,locations"}))
    except retrieval.Unavailable:
        return []


def _key(name: str) -> str:
    # "10.1016 j jet.2005.02.007", "10.1016j.jet.2005.02.007" and the DOI itself all match: '/' is not a file character
    return re.sub(r"[^a-z0-9]", "", name.lower())


def is_the_paper(text: str, title: str) -> bool:
    head = _plain(text[:4000])
    words = [w for w in re.findall(r"[a-z]+", _plain(title)) if len(w) > 3][:8]
    return bool(words) and sum(w in head for w in words) >= 0.75 * len(words)


def cut(text: str) -> tuple[str | None, str | None]:
    text = re.sub(r"-\n(?=[a-z])", "", unicodedata.normalize("NFKC", text))  # ligatures; words broken across lines
    if m := HEADING.search(text):
        body, where = text[m.end():], "introduction heading"
        # a numbered footnote looks like the next section; a real one comes after some introduction
        if end := next((e for e in NEXT.finditer(body) if len(body[:e.start()].split()) >= MIN_WORDS), None):
            body = body[:end.start()]
    else:
        body, where = text, "opening pages"
    words = body.split()
    if len(words) < MIN_WORDS:  # a scanned page or a cover sheet, not an introduction
        return None, None
    return " ".join(words[:WORDS]), where


def _plain(text: str) -> str:
    return re.sub(r"\s+", " ", unicodedata.normalize("NFKC", text).lower().replace("-\n", ""))


def _pdf_urls(work: dict) -> list[str]:
    urls = [(work.get("best_oa_location") or {}).get("pdf_url")]
    urls += [loc.get("pdf_url") for loc in work.get("locations") or [] if loc.get("is_oa")]
    return list(dict.fromkeys(u for u in urls if u))


def _download(url: str) -> str | None:
    try:
        resp = requests.get(url, timeout=30, headers={"User-Agent": "mark1-evidence-map"})
    except requests.RequestException:
        return None
    if not resp.ok or len(resp.content) > MAX_BYTES:
        return None
    return _pdf_text(resp.content)


def _pdf_text(data: bytes) -> str | None:
    from pypdf import PdfReader

    if not data.startswith(b"%PDF"):
        return None  # publishers often answer an open-access link with a landing page
    try:
        reader = PdfReader(io.BytesIO(data))
        return "\n".join(page.extract_text() or "" for page in reader.pages[:PAGES])
    except Exception:  # pypdf raises a wide variety on malformed files; any of them means no text
        return None
