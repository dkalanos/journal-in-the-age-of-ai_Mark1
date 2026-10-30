"""Level 3 · Re-execution under perturbation (SIEVE), formal modality, standard S9.

An anchor reproduces a value at the one point the author chose; the result it anchors is claimed wherever the
derivation's assumptions hold. So each anchor is re-run from the record at other points those assumptions admit,
and at every point the record's own procedure must agree with the derivation's formula for what it anchors.

The formula is read off the derivation, not declared: any solution, quantity, stated closed form or
comparative-static derivative that gives the anchor's value at the anchor's own point, with the derivation's
examples supplying symbols the anchor does not set. The anchor holds if one such reading agrees at every point.
An anchor that cannot be perturbed is listed with the reason, never skipped silently.
"""
import math
import random

import sympy

from ..checks.base import STANDARD, Check, Context
from ..findings import Finding
from ..sandbox import run_isolated
from ..sym import ExpressionError, inequality, parse, symbols

POINTS = 20
TRIES = 400
SPREAD = 1.0  # a perturbed value is the anchor's value times up to e^±SPREAD


def run(ctx: Context) -> list[Finding]:
    r = ctx.record
    rows, found = [], []
    for anchor in r.anchors:
        if not anchor.get("procedure") or "expected" not in anchor:
            continue  # malformed anchors are a Level 1 finding
        row = _perturb(r, anchor)
        rows.append(row)
        if row["result"] == "failed":
            found.append(Finding(level=3, check="perturbation", finding_class="warrant_gap", statement=row["statement"],
                                 record_pointer=f"anchors:{anchor['id']}", standard_pointer=f"{STANDARD}#S9",
                                 main=r.is_main(anchor.get("claim_id")), rationale=row["detail"]))
    ctx.outputs["perturbation"] = rows
    return found


def _perturb(r, anchor: dict) -> dict:
    aid, params, kind = anchor["id"], anchor.get("params") or {}, anchor.get("kind", "numeric")
    row = {"anchor": aid, "derivation": anchor.get("derivation_id"), "varied": [], "points": 0}

    def skip(why: str) -> dict:
        return {**row, "result": "not perturbed", "detail": why}

    d = r.derivation(anchor.get("derivation_id"))
    if not params:
        return skip("the anchor sets no parameter")
    if not d:
        return skip("the anchor names no derivation, so nothing in the record says what its value should be elsewhere")
    if d.get("kind") == "proof":
        return skip(f"{d['id']} is a proof; it gives no formula to re-run the anchor against")
    try:
        names = symbols(d.get("symbols") or {})
        assumptions = [inequality(a, names) for a in d.get("assumptions") or []]
        varied = [k for k in params if k in names]
        if not varied:
            return skip(f"none of its parameters ({', '.join(params)}) is a symbol of {d['id']} "
                        f"({', '.join(names)})")
        tolerance = anchor.get("tolerance") or {}
        readings = _readings(d, names, params, anchor["expected"], tolerance) if kind == "numeric" else []
    except ExpressionError as e:
        return skip(f"{d['id']} cannot be read: {e}")
    if kind == "numeric" and not readings:
        return skip(f"no formula of {d['id']} gives {anchor['expected']} at the anchor's own parameters")
    if kind not in ("numeric", "sign"):
        return skip(f"a {kind} anchor has no value to compare at other points")

    points = _points(f"{aid}|{anchor['procedure']['source']}", params, varied, names, assumptions)
    row["varied"] = varied
    if not points:
        return skip(f"no other point within e^±{SPREAD:g} of the anchor's parameters satisfies the assumptions of {d['id']}")
    result = run_isolated({"procedure": anchor["procedure"], "symbols": d.get("symbols") or {},
                           "record_root": str(r.root.resolve()), "points": [{**params, **p} for p in points]}, timeout=60)
    if not result.get("ok"):
        return skip(f"the procedure could not be re-executed: {result.get('error')}")
    ran, errors = [], []
    for point, out in zip(points, result["values"]):
        try:
            ran.append((point, float(sympy.sympify(out["value"]))))
        except (KeyError, TypeError, ValueError, sympy.SympifyError):
            errors.append(out.get("error") or f"{out.get('value')} is not a number")
    if not ran:
        return skip(f"the procedure did not run at any perturbed point: {errors[0]}")
    row = {**row, "varied": varied, "points": len(ran)}
    note = f"; it did not run at {len(errors)} further point(s): {errors[0]}" if errors else ""
    shown = ", ".join(f"{k} = {params[k]}" for k in varied)

    if kind == "sign":
        wrong = [(p, v) for p, v in ran if _sign(v) != anchor["expected"]]
        if not wrong:
            return {**row, "result": "held", "reading": f"sign {anchor['expected']}",
                    "detail": f"the sign is {anchor['expected']} at all {len(ran)} points{note}"}
        point, value = wrong[0]
        return {**row, "result": "failed",
                "statement": f"Anchor {aid} is {anchor['expected']} at {shown} but not at every value the assumptions "
                             f"of {d['id']} admit.",
                "detail": f"at {_show(point)} the record's procedure gives {value:g}, which is {_sign(value)}; "
                          f"{len(wrong)} of {len(ran)} points disagree{note}"}

    held = [rd for rd in readings if all(_close(v, _at(rd["formula"], {**rd["pins"], **params, **p}, names), tolerance)
                                         for p, v in ran)]
    if held:
        others = [rd["label"] for rd in readings if rd not in held]
        also = f". {', '.join(others)} also gave {anchor['expected']} at {shown} but does not elsewhere" if others else ""
        return {**row, "result": "held", "reading": "; ".join(_label(rd) for rd in held),
                "detail": f"agrees with {_label(held[0])} at all {len(ran)} points{also}{note}"}
    misses = []
    for rd in readings[:3]:
        point, value = next((p, v) for p, v in ran
                            if not _close(v, _at(rd["formula"], {**rd["pins"], **params, **p}, names), tolerance))
        expected = _at(rd["formula"], {**rd["pins"], **params, **point}, names)
        misses.append(f"at {_show(point)} the record's procedure gives {value:g}; {_label(rd)} gives "
                      f"{'no number' if expected is None else f'{expected:g}'}")
    return {**row, "result": "failed",
            "statement": f"Anchor {aid} reproduces {anchor['expected']} at {shown} but not at other values the "
                         f"assumptions of {d['id']} admit.",
            "detail": "; ".join(misses) + f" ({len(ran)} points){note}"}


def _readings(d: dict, names: dict, params: dict, expected, tolerance: dict) -> list[dict]:
    """The formulas of d that give the anchor's value at the anchor's own point."""
    solution = {k: parse(v, names) for k, v in (d.get("solution") or {}).items()}
    at_solution = {names[k]: v for k, v in solution.items() if k in names}
    formulas = {**solution, **{k: parse(v, names).subs(at_solution) for k, v in (d.get("quantities") or {}).items()}}
    formulas |= {f"{k}, as stated": parse(v, names) for k, v in (d.get("stated") or {}).items()}
    for cs in d.get("comparative_statics") or []:
        if cs["of"] in formulas and cs["wrt"] in names:
            formulas[f"d{cs['of']}/d{cs['wrt']}"] = sympy.diff(formulas[cs["of"]], names[cs["wrt"]])
    own = {k: v for k, v in params.items() if k in names}
    contexts = [("", {})] + [(f"example {i}", {k: v for k, v in ex["params"].items() if k in names and k not in own})
                             for i, ex in enumerate(d.get("examples") or [], 1)]
    readings, seen = [], set()
    for label, formula in formulas.items():
        for source, pins in contexts:
            key = (label, tuple(sorted(pins.items())))
            if key in seen or not formula.free_symbols <= {names[k] for k in {**pins, **own}}:
                continue
            seen.add(key)
            if _close(float(expected), _at(formula, {**pins, **own}, names), tolerance):
                readings.append({"label": label, "formula": formula, "pins": pins, "source": source})
    return readings


def _points(seed: str, params: dict, varied: list[str], names: dict, assumptions: list) -> list[dict]:
    rng = random.Random(seed)  # fixed per anchor, so a replay draws the same points
    checkable = [(e, strict) for e, strict in assumptions if {str(s) for s in e.free_symbols} <= set(params)]
    seen, points = {tuple(params[k] for k in varied)}, []
    for _ in range(TRIES):
        point = {k: _draw(params[k], names[k], rng) for k in varied}
        key = tuple(point[k] for k in varied)
        if key in seen:
            continue
        seen.add(key)
        full = {**params, **point}
        if all(_in_domain(full[k], names[k]) for k in varied) and \
                all(_holds(e, strict, full, names) for e, strict in checkable):
            points.append(point)
            if len(points) == POINTS:
                break
    return points


def _draw(value, symbol: sympy.Symbol, rng: random.Random):
    if not value:
        return (-1 if symbol.is_nonpositive else 1) * rng.uniform(0, 1)
    scaled = value * math.exp(rng.uniform(-SPREAD, SPREAD))
    return round(scaled) if isinstance(value, int) else scaled  # a count stays a count


def _in_domain(value, symbol: sympy.Symbol) -> bool:
    return not ((symbol.is_positive and value <= 0) or (symbol.is_nonnegative and value < 0)
                or (symbol.is_negative and value >= 0) or (symbol.is_nonpositive and value > 0))


def _holds(expr, strict: bool, point: dict, names: dict) -> bool:
    value = _at(expr, point, names)
    return value is not None and (value > 0 if strict else value >= 0)


def _at(formula, point: dict, names: dict) -> float | None:
    try:
        return float(formula.subs({names[k]: sympy.nsimplify(v, rational=True) for k, v in point.items() if k in names}))
    except (TypeError, ValueError):
        return None


def _close(got: float, want: float | None, tolerance: dict) -> bool:
    if want is None:
        return False
    allowed = max(tolerance.get("abs", 1e-9), tolerance.get("rel", 0) * abs(want), 1e-9 * abs(want))
    return abs(got - want) <= allowed


def _sign(value: float) -> str:
    return "zero" if abs(value) < 1e-12 else "positive" if value > 0 else "negative"


def _label(reading: dict) -> str:
    pins = ", ".join(f"{k} = {v}" for k, v in reading["pins"].items())
    return f"{reading['label']} (with {pins} from {reading['source']})" if pins else reading["label"]


def _show(point: dict) -> str:
    return ", ".join(f"{k} = {v:.4g}" if isinstance(v, float) else f"{k} = {v}" for k, v in point.items())


CHECK = Check(name="perturbation", level=3, deterministic=True, run=run)
