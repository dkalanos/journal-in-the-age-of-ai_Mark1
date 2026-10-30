"""Level 2 (a) · Completeness: is every claim the narrative rests on in the claims list? A model judgment."""
from ..findings import Finding
from ..llm import channel
from ..llm.agreement import cluster_spans
from ..pointer import Unresolvable, resolve
from .base import PROTOCOL, Check, Context


def run(ctx: Context) -> list[Finding]:
    r = ctx.record
    if ctx.backend is None:
        return []
    answers = ctx.ask("completeness", channel(r, r.files("paper") + ["ai-appendix/claims.yaml"]))
    known = {c.get("id") for c in r.claims}
    runs = []
    for answer in answers:
        unmatched = []
        for s in answer.payload["statements"]:
            if s["matched_claim"] in known:
                continue
            try:
                span = resolve(r, s["pointer"])
            except Unresolvable:
                continue  # no pointer, no flag
            if span.file.startswith("paper/"):
                unmatched.append((span, s["text"]))
        runs.append(unmatched)
    clusters, agreement = cluster_spans(runs, ctx.quorum)
    ctx.note_agreement("completeness", agreement)
    found = []
    for cluster in clusters:
        _, span, text = min(cluster, key=lambda item: (item[1].end - item[1].start, item[1].start))
        found.append(Finding(
            level=2, check="completeness", finding_class="claim_unresolved",
            statement=f'The paper states something the contribution rests on that the claims list lacks: "{text.strip()}"',
            record_pointer=span.pointer, standard_pointer=f"{PROTOCOL}#P10",
            rationale="A claim that appears only in the narrative is one the machine cannot check (appendix C.3).",
            **ctx.produced_by(answers, "completeness", len({i for i, _, _ in cluster})),
        ))
    return found


CHECK = Check(name="completeness", level=2, deterministic=False, run=run)
