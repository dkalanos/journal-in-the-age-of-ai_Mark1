"""Level 2 (c) · Anchors: the reproduction anchors reproduce when re-executed from the record. Deterministic."""
from ..findings import Finding
from ..sandbox import run_isolated
from .base import PROTOCOL, Check, Context


def run(ctx: Context) -> list[Finding]:
    r = ctx.record
    found = []
    for anchor in r.anchors:
        procedure = anchor.get("procedure")
        if not procedure or "expected" not in anchor:
            continue  # malformed anchors are a Level 1 finding
        derivation = r.derivation(anchor.get("derivation_id")) or {}
        result = run_isolated({
            "procedure": procedure,
            "params": anchor.get("params") or {},
            "kind": anchor.get("kind", "numeric"),
            "expected": anchor["expected"],
            "tolerance": anchor.get("tolerance") or {},
            "symbols": derivation.get("symbols") or {},
            "record_root": str(r.root),
        })
        if result.get("ok") and result.get("passed"):
            continue
        if result.get("ok"):
            got = result.get("sign", result["value"])
            statement = (f"Anchor {anchor['id']} does not reproduce: re-executed from the record it gives {got}; "
                         f"the AI appendix states {anchor['expected']}.")
            rationale = f"{procedure['language']} {procedure['source']} with {anchor.get('params') or {}}"
        else:
            statement = f"Anchor {anchor['id']} could not be re-executed from the record."
            rationale = result.get("error", "")
        found.append(Finding(level=2, check="anchors", finding_class="anchor_failed", statement=statement,
                             record_pointer=f"anchors:{anchor['id']}", standard_pointer=f"{PROTOCOL}#P10",
                             main=r.is_main(anchor.get("claim_id")), rationale=rationale))
    return found


CHECK = Check(name="anchors", level=2, deterministic=True, run=run)
