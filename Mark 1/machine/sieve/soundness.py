"""Level 3 · Formal soundness, deterministic slice (SIEVE).

Re-derives what the provenance says it derives: first- and second-order conditions, the stated
closed forms, comparative-static signs under the stated assumptions, numerical examples, whether
each proposition carries the conditions its derivation uses, and one sense per symbol and term.
For a proof (derivation kind `proof`) it checks what can be checked without judging the argument:
every step rests on something in the record, and no result rests on itself. Whether a claim carries
its proof's hypotheses is read by the resolution check; whether a prose step follows is a model
judgment and is not built (sieve/SPECIFIED.md).
"""
import re

import sympy

from ..checks.base import STANDARD, Check, Context
from ..findings import Finding
from ..pointer import Unresolvable, is_wellformed, normalize, resolve
from ..sym import ExpressionError, equal, inequality, parse, same_inequality, sign_under, symbols

DEFINITION = re.compile(r"^- \*\*(?P<term>[^*]+)\*\*(?: — `(?P<formula>[^`]+)`)?")
NEEDS_CONDITIONS = ("proposition", "comparative_static", "lemma")


def run(ctx: Context) -> list[Finding]:
    r = ctx.record
    found: list[Finding] = []

    def flag(cls: str, pointer: str, statement: str, clause: str, rationale: str = "", claim_id: str | None = None):
        found.append(Finding(level=3, check="soundness", finding_class=cls, statement=statement, record_pointer=pointer,
                             standard_pointer=f"{STANDARD}#{clause}", main=r.is_main(claim_id), rationale=rationale))

    for d in r.derivations:
        try:
            (_proof if d.get("kind") == "proof" else _derivation)(r, d, flag)
        except ExpressionError as e:
            flag("standard_departure", f"derivations:{d['id']}", f"Derivation {d['id']} cannot be read as stated.",
                 "S2", str(e))
    _conditions(r, flag)
    _senses(r, flag)
    return found


def _lead(r, d: dict) -> str | None:
    """The main claim a derivation supports, by its claim_ids or by the claims that name it."""
    named = list(d.get("claim_ids") or []) + [c["id"] for c in r.claims if c.get("derivation_id") == d["id"]]
    return next((c for c in named if r.is_main(c)), None)


def _proof(r, d: dict, flag) -> None:
    did, here = d["id"], f"derivations:{d['id']}"
    lead = _lead(r, d)
    if d.get("states"):
        try:
            resolve(r, d["states"])
        except Unresolvable as e:
            flag("standard_departure", here, f"Derivation {did} says the paper states its result at {d['states']}, "
                                             "which is not in the record.", "S8", str(e), lead)
    for n, step in enumerate(d.get("steps") or [], 1):
        for use in step.get("uses") or []:
            if use.startswith("cited:"):
                continue  # work outside the record is listed for the reader, not checked
            if not is_wellformed(use):
                flag("standard_departure", here, f"Step {n} of derivation {did} rests on {use!r}, which is neither a "
                                                 "pointer into the record nor a citation.", "S8", claim_id=lead)
                continue
            try:
                resolve(r, use)
            except Unresolvable as e:
                flag("standard_departure", here, f"Step {n} of derivation {did} rests on {use}, which is not in the "
                                                 "record.", "S8", str(e), lead)
    if cycle := _cycle(_graph(r), did):
        flag("warrant_gap", here, f"Derivation {did} rests, through what its steps use, on the result it proves.", "S8",
             " -> ".join(cycle), lead)


def _graph(r) -> dict[str, set[str]]:
    """Proof id -> the derivation ids its steps rest on.

    A location stands for a result only through the derivation that says it states the result there. Claims'
    pointers are not used: a claim may point at a passage that summarizes a result proved elsewhere, and that
    passage is often exactly what the proof rests on, which made proofs look circular.
    """
    proves: dict[str, set[str]] = {}
    for d in r.derivations:
        if d.get("states"):
            proves.setdefault(normalize(d["states"]), set()).add(d["id"])
    graph: dict[str, set[str]] = {}
    for d in r.derivations:
        if d.get("kind") == "proof":
            edges: set[str] = set()
            for u in _uses(d):
                if u.startswith("derivations:"):
                    edges.add(u.removeprefix("derivations:"))
                else:
                    edges |= proves.get(normalize(u), set())
            graph[d["id"]] = edges
    return graph


def _cycle(graph: dict[str, set[str]], start: str) -> list[str] | None:
    stack, seen = [(start, [start])], set()
    while stack:
        node, path = stack.pop()
        for nxt in sorted(graph.get(node, ())):
            if nxt == start:
                return path + [start]
            if nxt not in seen:
                seen.add(nxt)
                stack.append((nxt, path + [nxt]))
    return None


def _uses(d: dict | None) -> list[str]:
    return [u for step in (d or {}).get("steps") or [] for u in step.get("uses") or [] if not u.startswith("cited:")]



def _derivation(r, d: dict, flag) -> None:
    did, here = d["id"], f"derivations:{d['id']}"
    lead = next((c for c in d.get("claim_ids") or [] if r.is_main(c)), None)
    names = symbols(d.get("symbols") or {})
    assumptions = [inequality(a, names) for a in d.get("assumptions") or []]
    solution = {k: parse(v, names) for k, v in (d.get("solution") or {}).items()}
    at_solution = {names[k]: v for k, v in solution.items() if k in names}
    value = {**solution, **{k: parse(v, names).subs(at_solution) for k, v in (d.get("quantities") or {}).items()}}

    choice = d.get("choice_var")
    if d.get("objective") and choice in names and choice in solution:
        x, objective = names[choice], parse(d["objective"], names)
        foc = sympy.simplify(sympy.diff(objective, x).subs(at_solution))
        if foc != 0:
            flag("warrant_gap", here, f"The stated solution does not satisfy the first-order condition of derivation {did}.",
                 "S2", f"d/d{choice} of {d['objective']} at {choice} = {d['solution'][choice]} is {foc}, not 0", lead)
        else:
            goal = d.get("goal", "max")
            soc = sympy.simplify(sympy.diff(objective, x, 2).subs(at_solution))
            sign, how = sign_under(soc, assumptions)
            if sign != ("negative" if goal == "max" else "positive"):
                flag("warrant_gap", here, f"The second-order condition for a {goal}imum fails in derivation {did}.",
                     "S2", f"the second derivative is {soc}, {sign} ({how})", lead)

    for name, text in (d.get("stated") or {}).items():
        if name not in value:
            flag("standard_departure", here, f"Derivation {did} states a closed form for {name} but never defines {name}.", "S2")
        elif not equal(value[name], parse(text, names)):
            flag("warrant_gap", here, f"The stated closed form for {name} does not follow from derivation {did}.",
                 "S2", f"stated {text}; derived {sympy.simplify(value[name])}", lead)

    for cs in d.get("comparative_statics") or []:
        of, wrt, stated, cid = cs["of"], cs["wrt"], cs["stated_sign"], cs.get("claim_id")
        where = f"claims:{cid}" if r.claim(cid) else here
        if of not in value or wrt not in names:
            flag("standard_departure", where, f"Comparative static d{of}/d{wrt} names something derivation {did} "
                                              "does not define.", "S3", claim_id=cid)
            continue
        derivative = sympy.simplify(sympy.diff(value[of], names[wrt]))
        sign, how = sign_under(derivative, assumptions)
        if sign != stated:
            flag("warrant_gap", where, f"Comparative static d{of}/d{wrt} is stated {stated} but is {sign} under the "
                                       f"assumptions of derivation {did}.", "S3", f"d{of}/d{wrt} = {derivative}; {how}", cid)

    for i, ex in enumerate(d.get("examples") or [], 1):
        cid = ex.get("claim_id")
        where = f"claims:{cid}" if r.claim(cid) else here
        point = {names[k]: sympy.nsimplify(v, rational=True) for k, v in ex["params"].items() if k in names}
        for name, expected in ex["expected"].items():
            got = value[name].subs(point) if name in value else None
            try:
                got = float(got)
            except (TypeError, ValueError):
                flag("standard_departure", where, f"Numerical example {i} of derivation {did} reports {name}, which "
                                                  "does not evaluate to a number from the derivation.", "S4", claim_id=cid)
                continue
            if abs(got - expected) > 1e-9 * max(1.0, abs(expected)):
                flag("warrant_gap", where, f"Numerical example {i} of derivation {did} does not evaluate as stated: "
                                           f"{name} is {got:g}, not {expected:g}.", "S4", f"at {ex['params']}", cid)


def _conditions(r, flag) -> None:
    for claim in r.claims:
        cid = claim.get("id")
        d = r.derivation(claim.get("derivation_id"))
        if claim.get("form") not in NEEDS_CONDITIONS or not d:
            continue
        if d.get("kind") == "proof":
            # prose hypotheses are paraphrased by whoever states the claim; matching words misfired four times in
            # five on the first real paper, so whether a claim carries them is left to the resolution check
            continue
        names = symbols(d.get("symbols") or {})
        try:
            needed = [(text, inequality(text, names)) for text in d.get("assumptions") or []]
            stated = [inequality(text, names) for text in claim.get("condition") or []]
        except ExpressionError as e:
            flag("standard_departure", f"claims:{cid}", f"Claim {cid} states a condition that cannot be read.", "S1",
                 str(e), cid)
            continue
        missing = [text for text, canon in needed if not any(same_inequality(canon, s) for s in stated)]
        if missing:
            flag("standard_departure", f"claims:{cid}",
                 f"Claim {cid} is stated without the condition its derivation uses: {', '.join(missing)}.", "S1",
                 f"derivation {d['id']} assumes {', '.join(d['assumptions'])}; the claim states "
                 f"{', '.join(claim.get('condition') or []) or 'no condition'}", cid)


def _senses(r, flag) -> None:
    meanings: dict[str, tuple[str, str]] = {}
    defined: dict[str, tuple[sympy.Expr, str, dict]] = {}
    for d in r.derivations:
        names = symbols(d.get("symbols") or {})
        for name, info in (d.get("symbols") or {}).items():
            meaning = " ".join(str((info or {}).get("meaning", "")).lower().split())
            if name in meanings and meanings[name][0] != meaning:
                flag("standard_departure", f"derivations:{d['id']}",
                     f"Symbol {name} means one thing in derivation {meanings[name][1]} and another in {d['id']}.",
                     "S5", f"{meanings[name][0]!r} against {meaning!r}")
            meanings.setdefault(name, (meaning, d["id"]))
        for term, text in (d.get("quantities") or {}).items():
            try:
                expr = parse(text, names)
            except ExpressionError:
                continue
            if term in defined and not equal(defined[term][0], expr):
                flag("standard_departure", f"derivations:{d['id']}",
                     f"The term {term!r} is defined one way in derivation {defined[term][1]} and another way in {d['id']}.",
                     "S5", f"{defined[term][0]} against {expr}")
            defined.setdefault(term, (expr, d["id"], names))
    if not r.exists("ai-appendix/definitions.md"):
        return
    for n, line in enumerate(r.text("ai-appendix/definitions.md").splitlines(), 1):
        m = DEFINITION.match(line)
        term = m["term"].strip().lower() if m else None
        if not m or not m["formula"] or term not in defined:
            continue
        expr, did, names = defined[term]
        try:
            stated = parse(m["formula"], names)
        except ExpressionError:
            continue
        if not equal(stated, expr):
            flag("standard_departure", f"derivations:{did}",
                 f"Derivation {did} uses {term!r} in a sense other than its definition of record.", "S5",
                 f"ai-appendix/definitions.md line {n} defines it as {m['formula']}; {did} uses {expr}")


CHECK = Check(name="soundness", level=3, deterministic=True, run=run)
