"""The corpus behind the evidence map: the prior work the map is allowed to cite (appendix D.6).

Two sources, both published in advance under 1-journal/corpus/: the journal's venues, searched per paper
through OpenAlex (venues.yaml; the procedure is retrieval.py), and a hand-named list (corpus.yaml) enriched
from OpenAlex and cached under openalex/. Coverage is stated as exactly what was searched, never as
"the literature".
"""
import re
from pathlib import Path

import yaml

from . import fulltext, paths, retrieval
from .util import dump_json, load_json, load_yaml, sha256_files

DOI = re.compile(r"10\.\d{4,9}/[^\s\"<>]+", re.I)
INTRODUCTIONS = "introductions.json"  # other people's text: kept in the run for replay, never published
NOT_COVERED = ("work outside the venues searched", "books", "work without an abstract, beyond its title",
               "non-English work", "grey literature")


def entries() -> list[dict]:
    path = paths.corpus() / "corpus.yaml"
    return (load_yaml(path) or {}).get("items", []) if path.exists() else []


def cache_path(item_id: str) -> Path:
    return paths.corpus() / "openalex" / f"{item_id}.json"


def build(offline: bool = False) -> dict:
    """Enrich the hand list and resolve the venues, both cached, so runs replay offline."""
    report = {"fetched": [], "cached": [], "skipped": [], "failed": []}
    for item in entries():
        if cache_path(item["id"]).exists():
            report["cached"].append(item["id"])
        elif offline or not item.get("doi"):
            report["skipped"].append(item["id"])
        else:
            try:
                work = retrieval.fetch(f"{retrieval.API}/works/doi:{item['doi']}", {})
            except retrieval.Unavailable as e:
                report["failed"].append(f"{item['id']}: {e}")
                continue
            dump_json(retrieval.slim(work), cache_path(item["id"]))
            report["fetched"].append(item["id"])
    if not offline:
        try:
            retrieval.resolve()
        except retrieval.Unavailable as e:
            report["failed"].append(f"venues: {e}")
    ids, missing = retrieval.sources()
    return {**report, "venues_resolved": len(ids), "venues_unresolved": missing}


def load() -> list[dict]:
    items = []
    for item in entries():
        path = cache_path(item["id"])
        enriched = load_json(path) if path.exists() else {}
        items.append({**item, **{k: v for k, v in enriched.items() if v and k != "id"}, "enriched": bool(enriched)})
    return items


def candidates(ctx, claims: list[dict], cited: set[str]) -> dict:
    """What this run's map may cite, kept in the run (sieve/candidates.json) so resume and replay see the same set."""
    path = ctx.run_dir / "sieve" / "candidates.json"
    if path.exists():
        return _with_introductions(load_json(path), ctx.run_dir)
    request = ctx.run_dir / "bundles" / "contribution" / "request.json"
    if request.exists() and load_json(request)["check_version"] != ctx.versions["checks"]:
        # bundles written under checks 0.1.0 saw the hand list alone; their answers are read against it
        return {"procedure": "the hand list alone (checks 0.1.0)", "venues": None, "queries": [],
                "hand_list": len(load()), "candidates": load()}
    cfg = retrieval.venues()
    found = {"procedure": "the hand list alone; no venue switched on", "venues": None, "queries": [], "candidates": []}
    if cfg.get("search"):
        found = retrieval.search(ctx.record.manifest.get("title", ctx.record.paper_id), claims, cited)
        if limit := cfg.get("introductions"):
            shelf = paths.root() / cfg["licensed_copies"] if cfg.get("licensed_copies") else None
            texts = fulltext.introductions(found["candidates"], limit, licensed=shelf)
            dump_json(texts, ctx.run_dir / "sieve" / INTRODUCTIONS)
            for item in found["candidates"]:
                if item["id"] in texts:  # the text itself stays in introductions.json
                    item["introduction"] = {k: v for k, v in texts[item["id"]].items() if k != "text"}
    hand = [{**i, "found_by": ["hand list"]} for i in load()] if cfg.get("hand_list", True) else []
    found["hand_list"] = len(hand)
    found["candidates"] += hand
    dump_json(found, path)
    return _with_introductions(found, ctx.run_dir)


def _with_introductions(found: dict, run_dir: Path) -> dict:
    path = run_dir / "sieve" / INTRODUCTIONS
    texts = load_json(path) if path.exists() else {}
    for item in found["candidates"]:
        if item["id"] in texts:
            item["introduction_text"] = texts[item["id"]]["text"]
    return found


def version() -> str:
    files = [(name, paths.corpus() / name) for name in ("corpus.yaml", "venues.yaml", "sources.json")]
    files += [(p.name, p) for p in sorted((paths.corpus() / "openalex").glob("*.json"))]
    return sha256_files((name, p) for name, p in files if p.exists())


def citation(item: dict) -> str:
    surnames = [a.split()[-1] for a in item.get("authors") or []]
    if len(surnames) > 2:
        who = f"{surnames[0]} et al."
    else:
        who = " & ".join(surnames) or "Unknown"
    return f"{who} ({item.get('year', 'n.d.')}). {item.get('title', item['id'])}"


def prompt_text(items: list[dict]) -> str:
    rows = []
    for i in items:
        row = {"id": i["id"], "citation": citation(i), "venue": i.get("venue"), "year": i.get("year"), "doi": i.get("doi")}
        if i.get("abstract"):
            row["abstract"] = i["abstract"]
        elif i.get("summary"):
            row["summary"] = i["summary"]
        else:
            row["abstract"] = "(none available: title, venue and year only)"
        if i.get("introduction_text"):
            row["introduction"] = i["introduction_text"]
        rows.append(row)
    return yaml.safe_dump(rows, sort_keys=False, allow_unicode=True, width=110)


def dois_in(text: str) -> set[str]:
    return {m.rstrip(".,;)").lower() for m in DOI.findall(text)}


def coverage(found: dict, cited: set[str]) -> dict:
    items = found["candidates"]
    dois = {i.get("doi") for i in items if i.get("doi")}
    without = sum(1 for i in items if not (i.get("abstract") or i.get("summary")))
    if v := found.get("venues"):
        snow = found.get("snowball", {})
        unresolved = f"; {len(v['unresolved'])} not resolved in OpenAlex" if v["unresolved"] else ""
        head = (f"Venues searched: {', '.join(v['lists'])} ({v['journals']} journals, {v['resolved']} resolved in "
                f"OpenAlex{unresolved}). {len(found['queries'])} queries from the contribution claim and the title "
                f"returned {sum(q.get('hits', 0) for q in found['queries'])} hits; {snow.get('added', 0)} works were "
                f"added as the most cited among them ({snow.get('out_of_venue', 0)} such works lay outside the venues "
                "and were dropped). ")
    else:
        head = f"Procedure: {found['procedure']}. "
    hand = f"Hand list: {found['hand_list']} items. " if found.get("hand_list") else ""
    read = sum(1 for i in items if i.get("introduction"))
    licensed = sum(1 for i in items if (i.get("introduction") or {}).get("via") == "licensed")
    intros = (f"{read} were also read from their introduction ({licensed} from the journal's licensed copies, "
              f"{read - licensed} from open-access copies); the rest have no copy the journal holds or could "
              "fetch. ") if read else ""
    return {
        "items": len(items),
        "without_abstract": without,
        "with_introduction": read,
        "statement": (head + hand + f"Candidates shown to the model: {len(items)}, of which {without} have no "
                      f"abstract and were seen by title, venue and year only. {intros}"
                      f"Not covered: {', '.join(NOT_COVERED)}."),
        "cited_but_not_retrieved": sorted(d for d in cited if d not in dois),
        "unresolved": sorted(i["id"] for i in items if "enriched" in i and not i["enriched"]),
    }
