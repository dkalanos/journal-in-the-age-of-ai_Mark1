"""Retrieval for the evidence map: the journal's venues, searched through OpenAlex (appendix C.6).

The venues and the procedure are published in advance (1-journal/corpus/venues.yaml); what each run retrieved
is kept in its sieve/candidates.json, so a miss can be traced to a query. Keyword search favours work with an
abstract or full text; the second step, the works most cited among the first step's hits, is what reaches the
older antecedents, which often have neither.
"""
import os
import re
import time
from collections import Counter

import requests

from . import paths
from .util import dump_json, load_json, load_yaml

API = "https://api.openalex.org"
FIELDS = ("id,doi,title,publication_year,authorships,primary_location,abstract_inverted_index,topics,"
          "referenced_works,cited_by_count")
PER_QUERY = 25
SNOWBALL = 20
CAP = 60
CHUNK = 40  # OR-ed values per filter; keeps each request small and within OpenAlex's limits
STOPWORDS = set("""a an the and or of to in on for with by from at as is are be was were been being this that
these those it its into under over than then so such not no nor but if when where which who whom whose what why
how all any each other some more most very can could may might shall should will would do does did done has have
had having we our us they their them he she his her i my you your one two three first second new note paper
article study show shows shown give gives given result results exactly whatever whether also between among
within without via per""".split())


class Unavailable(Exception):
    """OpenAlex could not be reached or refused the request; the check reports itself not run."""


def venues() -> dict:
    path = paths.corpus() / "venues.yaml"
    return load_yaml(path) if path.exists() else {"search": [], "hand_list": True, "lists": {}, "journals": []}


def active(cfg: dict) -> list[dict]:
    on = set(cfg.get("search") or [])
    return [j for j in cfg.get("journals", []) if on & set(j.get("lists", []))]


def resolve(get=None) -> dict:
    """Map every ISSN in venues.yaml to its OpenAlex source; cached in sources.json, unknown ISSNs as null."""
    get = get or fetch
    path = paths.corpus() / "sources.json"
    cache = load_json(path) if path.exists() else {}
    issns = sorted({i for j in venues().get("journals", []) for i in j.get("issn", []) if i not in cache})
    for start in range(0, len(issns), CHUNK):
        batch = issns[start:start + CHUNK]
        found = get(f"{API}/sources", {"filter": "issn:" + "|".join(batch), "per-page": 100,
                                       "select": "id,display_name,issn,type"})["results"]
        for s in found:
            for i in s.get("issn") or []:
                if i in batch:
                    cache[i] = {"id": _tail(s["id"]), "name": s["display_name"], "type": s["type"]}
        for i in batch:
            cache.setdefault(i, None)
    dump_json(cache, path)
    return cache


def sources(cfg: dict | None = None) -> tuple[dict[str, str], list[str]]:
    """({OpenAlex source id: journal} for the journals switched on, journals that did not resolve)."""
    cfg = cfg or venues()
    path = paths.corpus() / "sources.json"
    cache = load_json(path) if path.exists() else {}
    ids, missing = {}, []
    for j in active(cfg):
        hit = next((cache[i] for i in j.get("issn", []) if cache.get(i)), None)
        if hit:
            ids[hit["id"]] = j["name"]
        else:
            missing.append(j["name"])
    return ids, missing


def words(text: str) -> list[str]:
    seen, out = set(), []
    for w in re.findall(r"[a-z][a-z-]+", text.lower()):
        if len(w) > 2 and w not in STOPWORDS and w not in seen:
            seen.add(w)
            out.append(w)
    return out


def queries(title: str, claims: list[dict]) -> list[dict]:
    """Per claim: the claim whole; the words it shares with the title, which tend to be the subject terms; and
    those again against titles only, where a short old note can still win. Plus the title itself."""
    title_words = words(title)
    out = [{"id": "title", "claim_id": None, "kind": "title", "q": " ".join(title_words[:6])}]
    for c in claims:
        claim_words = words(c["text"])
        key = [w for w in claim_words if w in title_words] or title_words[:4]
        out += [{"id": f"{c['id']}-claim", "claim_id": c["id"], "kind": "search", "q": " ".join(claim_words)},
                {"id": f"{c['id']}-key", "claim_id": c["id"], "kind": "search", "q": " ".join(key)},
                {"id": f"{c['id']}-key-title", "claim_id": c["id"], "kind": "title", "q": " ".join(key)}]
    unique, seen = [], set()
    for q in out:
        if q["q"] and (q["kind"], q["q"]) not in seen:
            seen.add((q["kind"], q["q"]))
            unique.append(q)
    return unique


def search(title: str, claims: list[dict], cited_dois: set[str], get=None) -> dict:
    """Keyword search of the venues, then the works most cited among the hits; the content of candidates.json."""
    get = get or fetch
    cfg = venues()
    ids, missing = sources(cfg)
    if not ids:
        raise Unavailable("no venue is resolved in OpenAlex; run `mark1 corpus` first")
    qs = queries(title, claims)
    hits: dict[str, dict] = {}
    for q in qs:
        results = []
        for chunk in _chunks(sorted(ids)):
            venue = f"primary_location.source.id:{'|'.join(chunk)}"
            if q["kind"] == "title":
                params = {"filter": f"title.search:{q['q']},{venue}", "sort": "cited_by_count:desc", "select": FIELDS}
            else:
                params = {"search": q["q"], "filter": venue, "sort": "relevance_score:desc",
                          "select": FIELDS + ",relevance_score"}
            results += get(f"{API}/works", {**params, "per-page": PER_QUERY})["results"]
        score = "relevance_score" if q["kind"] == "search" else "cited_by_count"
        results.sort(key=lambda w: -(w.get(score) or 0))
        q["hits"] = len(results[:PER_QUERY])
        for rank, work in enumerate(results[:PER_QUERY], 1):
            entry = hits.setdefault(_tail(work["id"]), {**slim(work), "found_by": [], "best_rank": rank,
                                                         "refs": work.get("referenced_works") or []})
            entry["found_by"].append(f"{q['id']} #{rank}")
            entry["best_rank"] = min(entry["best_rank"], rank)

    refs = Counter(_tail(r) for h in hits.values() for r in h.pop("refs"))
    if cited_dois:
        # what the paper cites seeds the count too, so the antecedents of its own references are reached
        for work in _batched(get, "doi", sorted(cited_dois)):
            refs.update(_tail(r) for r in work.get("referenced_works") or [])
    wanted = [w for w, n in refs.most_common(3 * SNOWBALL) if n >= 2 and w not in hits]
    snow, out_of_venue = [], 0
    for work in _batched(get, "openalex", wanted):
        if _source(work) in ids:
            n = refs[_tail(work["id"])]
            snow.append({**slim(work), "found_by": [f"cited by {n} of the retrieved works"], "cited_among_hits": n})
        else:
            out_of_venue += 1
    snow.sort(key=lambda w: -w["cited_among_hits"])
    snow = snow[:SNOWBALL]
    keyword = sorted(hits.values(), key=lambda h: (h["best_rank"], -len(h["found_by"])))
    return {
        "procedure": ("keyword search of the venues switched on in venues.yaml, through OpenAlex, then the works most "
                      "cited among the hits and among what the paper cites, kept when they are in those venues"),
        "venues": {"lists": cfg.get("search"), "journals": len(active(cfg)), "resolved": len(ids), "unresolved": missing},
        "queries": qs,
        "snowball": {"seeds": len(hits), "distinct_references": len(refs), "considered": len(wanted),
                     "added": len(snow), "out_of_venue": out_of_venue},
        "candidates": snow + keyword[:max(0, CAP - len(snow))],
    }


def fetch(url: str, params: dict) -> dict:
    auth = {k: v for k, v in (("api_key", os.environ.get("MARK1_OPENALEX_KEY")),
                              ("mailto", os.environ.get("MARK1_OPENALEX_MAILTO"))) if v}
    for attempt in range(3):
        try:
            resp = requests.get(url, params={**params, **auth}, timeout=30)
        except requests.RequestException as e:
            raise Unavailable(f"OpenAlex unreachable: {e}") from None
        if resp.ok:
            return resp.json()
        # a short Retry-After is rate limiting, worth a pause; a long one is an exhausted daily budget
        if resp.status_code == 429 and attempt < 2 and int(resp.headers.get("Retry-After") or 0) < 10:
            time.sleep(2 * (attempt + 1))
            continue
        try:
            detail = resp.json().get("message", resp.text)
        except ValueError:
            detail = resp.text
        raise Unavailable(f"OpenAlex answered {resp.status_code}: {detail[:300]}")
    raise Unavailable("OpenAlex kept rate limiting")


def slim(work: dict) -> dict:
    doi = (work.get("doi") or "").removeprefix("https://doi.org/").lower()
    return {
        "id": _tail(work.get("id") or ""),
        "openalex_id": _tail(work.get("id") or ""),
        "doi": doi or None,
        "title": work.get("title"),
        "year": work.get("publication_year"),
        "authors": [a["author"]["display_name"] for a in work.get("authorships", [])],
        "venue": ((work.get("primary_location") or {}).get("source") or {}).get("display_name"),
        "abstract": _abstract(work.get("abstract_inverted_index")),
        "topics": [t["display_name"] for t in (work.get("topics") or [])[:5]],
        "cited_by_count": work.get("cited_by_count"),
    }


def _batched(get, field: str, values: list[str]):
    for chunk in _chunks(values):
        yield from get(f"{API}/works", {"filter": f"{field}:{'|'.join(chunk)}", "per-page": len(chunk),
                                        "select": FIELDS})["results"]


def _chunks(values: list[str]):
    for start in range(0, len(values), CHUNK):
        yield values[start:start + CHUNK]


def _source(work: dict) -> str:
    return _tail(((work.get("primary_location") or {}).get("source") or {}).get("id") or "")


def _tail(openalex_url: str) -> str:
    return openalex_url.rsplit("/", 1)[-1]


def _abstract(index: dict | None) -> str | None:
    if not index:
        return None
    return " ".join(word for _, word in sorted((pos, word) for word, positions in index.items() for pos in positions))
