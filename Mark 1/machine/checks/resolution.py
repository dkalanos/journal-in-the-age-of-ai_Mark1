"""Level 2 (b) · Resolution: does each claim's evidence say what the claim says?

A pointer that does not resolve is found deterministically. Whether resolved evidence says what
the claim says is a model judgment, repeated k times.
"""
from collections import Counter

import yaml

from ..findings import Finding
from ..llm import excerpt
from ..pointer import Span, Unresolvable, resolve
from .base import PROTOCOL, Check, Context


def run(ctx: Context) -> list[Finding]:
    found, resolved = _resolve_pointers(ctx)
    if ctx.backend is None or not resolved:
        return found
    data = "\n\n".join(_block(*item) for item in resolved)
    answers = ctx.ask("resolution", data)
    verdicts: dict[str, list[tuple[str, str]]] = {item[0]["id"]: [] for item in resolved}
    for answer in answers:
        for v in answer.payload["verdicts"]:
            if v["claim_id"] in verdicts:
                verdicts[v["claim_id"]].append((v["resolves"], v["reason"]))
    unanimous = sum(1 for vs in verdicts.values() if len(vs) == len(answers) and len({r for r, _ in vs}) == 1)
    ctx.note_agreement("resolution", unanimous / len(verdicts))
    for claim, *_ in resolved:
        failing = [(r, why) for r, why in verdicts[claim["id"]] if r != "full"]
        if len(failing) < ctx.quorum:
            continue
        how = Counter(r for r, _ in failing).most_common(1)[0][0]
        found.append(Finding(
            level=2, check="resolution", finding_class="evidence_partial" if how == "partial" else "pointer_missing",
            statement=f"The evidence for claim {claim['id']} does not say what the claim says "
                      f"({'only in part' if how == 'partial' else 'not at all'}).",
            record_pointer=f"claims:{claim['id']}", standard_pointer=f"{PROTOCOL}#P10", main=bool(claim.get("main")),
            rationale=" / ".join(dict.fromkeys(why for _, why in failing)),
            **ctx.produced_by(answers, "resolution", len(failing)),
        ))
    return found


def _resolve_pointers(ctx: Context) -> tuple[list[Finding], list[tuple[dict, Span, Span, Span | None]]]:
    found, resolved = [], []
    for claim in ctx.record.claims:
        cid = claim.get("id", "?")
        spans = {}
        keys = ("pointer", "evidence_pointer") + (("question_pointer",) if claim.get("question_pointer") else ())
        for key in keys:
            try:
                spans[key] = resolve(ctx.record, claim.get(key, ""))
            except Unresolvable as e:
                found.append(Finding(level=2, check="resolution", finding_class="pointer_missing",
                                     statement=f"Claim {cid}: its {key.replace('_', ' ')} does not resolve in the record.",
                                     record_pointer=f"claims:{cid}", standard_pointer=f"{PROTOCOL}#P10",
                                     main=bool(claim.get("main")), rationale=str(e)))
        if "pointer" in spans and "evidence_pointer" in spans:
            resolved.append((claim, spans["pointer"], spans["evidence_pointer"], spans.get("question_pointer")))
    return found, resolved


def _block(claim: dict, states: Span, evidence: Span, question: Span | None = None) -> str:
    entry = {k: claim[k] for k in ("id", "kind", "form", "main", "text", "condition", "question") if k in claim}
    lines = [
        f"=== claim {claim['id']} ===",
        yaml.safe_dump(entry, sort_keys=False, allow_unicode=True).strip(),
        f"--- where the paper states it: {states.pointer} ---",
        excerpt(states),
        f"--- the evidence it points to: {evidence.pointer} ---",
        excerpt(evidence),
    ]
    if question is not None:
        lines += [f"--- the question it answers, where the paper states it: {question.pointer} ---", excerpt(question)]
    return "\n".join(lines)


CHECK = Check(name="resolution", level=2, deterministic=False, run=run)
