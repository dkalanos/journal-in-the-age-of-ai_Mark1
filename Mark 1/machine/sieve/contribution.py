"""Level 3 · Contribution warrant (SIEVE): does the contribution claim survive comparison with the
nearest prior work? Produces the evidence map (appendix C.6). A model judgment on a retrieved candidate set."""
from collections import Counter

import yaml

from .. import corpus, retrieval
from ..checks.base import STANDARD, Check, Context, NotRun
from ..findings import Finding
from ..llm import channel
from ..llm.agreement import quorum_items, quorum_value
from ..pointer import Unresolvable, resolve


def run(ctx: Context) -> list[Finding]:
    r = ctx.record
    claims = [c for c in r.claims if c.get("kind") == "contribution"]
    if ctx.backend is None:
        return []
    if not claims:
        raise NotRun("the claims list has no contribution claim to place")
    references = _references(r)
    try:
        found = corpus.candidates(ctx, claims, corpus.dois_in(references))
    except retrieval.Unavailable as e:
        raise NotRun(f"retrieval failed: {e}") from None
    items = found["candidates"]
    if not items:
        raise NotRun("nothing to place the claim against: no venue switched on and no hand list")

    context = [c for c in r.claims if c.get("main") and c.get("kind") != "contribution"]
    data = channel(r, [], extras=[
        ("claims to place", _dump([_to_place(r, c) for c in claims])),
        ("main results of the paper, for context", _dump([{"id": c["id"], "text": c["text"]} for c in context])),
        ("references cited by the paper", references or "(none found)"),
        ("candidate set: the prior work this map may cite", corpus.prompt_text(items)),
    ])
    answers = ctx.ask("contribution", data)

    by_id = {i["id"]: i for i in items}
    placements: dict[str, list[dict]] = {c["id"]: [] for c in claims}
    for answer in answers:
        for p in answer.payload["claims"]:
            if p["claim_id"] in placements:
                # the map cites the candidate set and nothing else
                placements[p["claim_id"]].append({**p, "nearest": [n for n in p["nearest"] if n["corpus_id"] in by_id]})

    kinds = {cid: quorum_value([p["newness_kind"] for p in ps], ctx.quorum) for cid, ps in placements.items()}
    ctx.note_agreement("contribution", sum(k is not None for k in kinds.values()) / len(kinds))

    found_, mapped = [], []
    for claim in claims:
        ps, kind = placements[claim["id"]], kinds[claim["id"]] or "no_consensus"
        nearest = _nearest(ps, by_id, ctx.quorum)
        agreeing = sum(p["newness_kind"] == kind for p in ps)
        rationale = next((p["rationale"] for p in ps if p["newness_kind"] == kind), ps[0]["rationale"] if ps else "")
        mapped.append({"claim_id": claim["id"], "text": claim["text"], "newness_kind": kind, "nearest": nearest,
                       "rationale": rationale, "agreement": f"{agreeing}/{len(answers)}",
                       "question": _question(claim, ps)})
        if kind == "none":
            prior = [_cite(n) for n in nearest if n["relation"] == "anticipates"] or [_cite(n) for n in nearest]
            found_.append(_finding(ctx, answers, claim, "established_by_prior", "S6", agreeing, rationale,
                                   f"The evidence map finds contribution claim {claim['id']} established by prior "
                                   f"work: {'; '.join(prior)}."))
        elif kind == "uncovered":
            found_.append(_finding(ctx, answers, claim, "uncovered", "S7", agreeing, rationale,
                                   f"The candidate set does not reach the area of contribution claim {claim['id']} "
                                   "well enough to place it."))

    ctx.outputs["evidence_map"] = {
        "paper_id": r.paper_id,
        "run_id": ctx.run_dir.name,
        "corpus": {"version": corpus.version(), "items": len(items), "procedure": found["procedure"]},
        "claims": mapped,
        "coverage": corpus.coverage(found, corpus.dois_in(references)),
    }
    return found_


def _nearest(placements: list[dict], by_id: dict, quorum: int) -> list[dict]:
    agreed = quorum_items([{n["corpus_id"] for n in p["nearest"]} for p in placements], quorum)
    counts = Counter(n["corpus_id"] for p in placements for n in p["nearest"])
    first, rank = {}, {}
    for p in placements:
        for i, n in enumerate(p["nearest"]):
            first.setdefault(n["corpus_id"], n)
            rank[n["corpus_id"]] = min(rank.get(n["corpus_id"], i), i)
    order = sorted(agreed, key=lambda cid: (-counts[cid], rank[cid], cid))
    return [{**first[cid], **_answers(placements, cid), "citation": corpus.citation(by_id[cid]),
             "doi": by_id[cid].get("doi"),
             "venue": by_id[cid].get("venue"), "year": by_id[cid].get("year"),
             "retrieved_by": by_id[cid].get("found_by"), "found_by": f"{counts[cid]}/{len(placements)}"}
            for cid in order]


def _answers(placements: list[dict], cid: str) -> dict:
    """The two answers on one nearest work, by majority of the answers that listed it: does it pose the question the
    claim answers, does it state the claim. The other fields come from the first answer that listed the work."""
    out = {}
    for field in ("poses_question", "states_claim"):
        votes = [n[field] for p in placements for n in p["nearest"] if n["corpus_id"] == cid and field in n]
        if votes:
            yes = sum(bool(v) for v in votes)
            out[field] = 2 * yes > len(votes)
            out[f"{field}_votes"] = f"{yes}/{len(votes)} yes"
    return out


def _to_place(record, claim: dict) -> dict:
    """The claim with the question it answers as the paper states it, passage included (protocol P4, formal-0.4)."""
    out = {"id": claim["id"], "text": claim["text"]}
    if claim.get("question"):
        out["question"] = claim["question"]
        out["question_stated_at"] = claim.get("question_pointer")
        try:
            out["question_passage"] = resolve(record, claim["question_pointer"]).text.strip()
        except (Unresolvable, TypeError):
            pass  # the form check reports the pointer; the map still places the claim on the question as stated
    return out


def _question(claim: dict, placements: list[dict]) -> dict:
    """The question the claim was placed on: the paper's, when the claims list states it; otherwise the model's."""
    read = list(dict.fromkeys(p["question_as_read"] for p in placements if p.get("question_as_read")))
    if claim.get("question"):
        return {"text": claim["question"], "pointer": claim.get("question_pointer"), "stated_by": "author",
                "read_differently": read}
    return {"text": " / ".join(read) or None, "pointer": None, "stated_by": "model" if read else "none",
            "read_differently": []}


def _cite(n: dict) -> str:
    return n["citation"] + (" (seen by title only)" if n.get("basis") == "title_and_known_work" else "")


def _references(record) -> str:
    for rel in record.files("paper"):
        try:
            return resolve(record, f"{rel}#references").text
        except Unresolvable:
            continue
    return ""


def _finding(ctx, answers, claim, cls, clause, agreeing, rationale, statement) -> Finding:
    return Finding(level=3, check="contribution", finding_class=cls, statement=statement,
                   record_pointer=f"claims:{claim['id']}", standard_pointer=f"{STANDARD}#{clause}",
                   main=bool(claim.get("main")), rationale=rationale,
                   **ctx.produced_by(answers, "contribution", agreeing))


def _dump(rows: list[dict]) -> str:
    return yaml.safe_dump(rows, sort_keys=False, allow_unicode=True, width=110)


CHECK = Check(name="contribution", level=3, deterministic=False, run=run)
