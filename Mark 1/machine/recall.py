"""The recall test for the evidence map (appendix F.2): did retrieval reach prior work a reader knows should
be there, and what did the map make of it?"""
from pathlib import Path

from . import paths, run
from .util import load_json, write_text


def measure(paper_id: str, run_id: str, expected_dois: list[str]) -> tuple[Path, int]:
    folder = run.find(run_id)
    found = load_json(folder / "sieve" / "candidates.json")
    emap_path = folder / "sieve" / "evidence-map.json"
    emap = load_json(emap_path) if emap_path.exists() else None
    by_doi = {c["doi"]: c for c in found["candidates"] if c.get("doi")}
    on_map = {n.get("doi"): f"{n['relation']} ({claim['claim_id']}, basis: {n.get('basis', '?')})"
              for claim in (emap or {}).get("claims", []) for n in claim["nearest"]}

    rows, hits = [], 0
    for doi in expected_dois:
        doi = doi.lower().removeprefix("https://doi.org/")
        c = by_doi.get(doi)
        hits += bool(c)
        retrieved = f"yes: {'; '.join(c['found_by'])}" if c else "no"
        placed = on_map.get(doi, "not among the nearest" if emap else "map not yet produced")
        rows.append(f"| {doi} | {retrieved} | {placed} |")

    v = found.get("venues")
    lines = [f"# Recall test · {paper_id} · run `{run_id}`", "",
             "Appendix I.4: prior work a reader knows the map should reach, whether retrieval reached it, and what "
             "the map made of it. Retrieval is reported as it happened; nothing here was tuned to the answer.", "",
             f"Procedure: {found['procedure']}.", "",
             (f"Venues: {', '.join(v['lists'])}, {v['resolved']} journals resolved in OpenAlex. " if v else "")
             + f"Candidates: {len(found['candidates'])}"
             + (f", {found['hand_list']} from the hand list" if found.get("hand_list") else "") + ".", ""]
    if found["queries"]:
        lines += ["| Query | Kind | Hits |", "|---|---|---|"]
        lines += [f"| {q['q']} | {q['kind']} | {q.get('hits', 0)} |" for q in found["queries"]] + [""]
    if snow := found.get("snowball"):
        lines += [f"Snowball: {snow['distinct_references']} distinct works referenced by the {snow['seeds']} hits; "
                  f"{snow['considered']} referenced at least twice were looked up, {snow['added']} were in the venues "
                  f"and added, {snow['out_of_venue']} were not.", ""]
    lines += ["| Expected prior work | Retrieved | On the map |", "|---|---|---|"] + rows + [""]
    if emap:
        lines += ["Map: " + "; ".join(f"{c['claim_id']} → {c['newness_kind']} (agreement {c['agreement']})"
                                      for c in emap["claims"]), ""]
    out = paths.evaluation() / f"recall-{paper_id}.md"
    write_text(out, "\n".join(lines), rtf=True)
    return out, hits
