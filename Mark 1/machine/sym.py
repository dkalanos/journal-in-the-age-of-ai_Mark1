import io
import random
import tokenize

import sympy
from sympy.parsing.sympy_parser import convert_xor, parse_expr, standard_transformations

FUNCTIONS = {
    "diff": sympy.diff, "sqrt": sympy.sqrt, "exp": sympy.exp, "log": sympy.log,
    "Abs": sympy.Abs, "Min": sympy.Min, "Max": sympy.Max, "Rational": sympy.Rational,
}
OPERATORS = {"+", "-", "*", "/", "**", "^", "(", ")", ",", "<", ">", "<=", ">=", "=="}
DOMAINS = {
    "real": {"real": True},
    "positive": {"positive": True},
    "nonnegative": {"nonnegative": True},
    "negative": {"negative": True},
    "nonpositive": {"nonpositive": True},
}
ALLOWED_TOKENS = {tokenize.NAME, tokenize.OP, tokenize.NUMBER, tokenize.NEWLINE, tokenize.NL, tokenize.ENDMARKER}
TRANSFORMS = standard_transformations + (convert_xor,)


class ExpressionError(ValueError):
    pass


def symbols(spec: dict[str, dict]) -> dict[str, sympy.Symbol]:
    return {name: sympy.Symbol(name, **DOMAINS.get((info or {}).get("domain", "real"), DOMAINS["real"]))
            for name, info in spec.items()}


def parse(source: str, names: dict[str, sympy.Symbol], evaluate: bool = True):
    # Author-supplied text goes through eval inside parse_expr, so whitelist tokens first:
    # declared symbols, a few functions, numbers, arithmetic. No dots, quotes, brackets or builtins.
    source = str(source).strip()
    try:
        tokens = list(tokenize.generate_tokens(io.StringIO(source).readline))
    except (tokenize.TokenError, SyntaxError) as e:
        raise ExpressionError(f"cannot read {source!r}: {e}") from None
    for tok in tokens:
        if tok.type not in ALLOWED_TOKENS:
            raise ExpressionError(f"unexpected {tok.string!r} in {source!r}")
        if tok.type == tokenize.NAME and tok.string not in names and tok.string not in FUNCTIONS:
            raise ExpressionError(f"unknown name {tok.string!r} in {source!r}")
        if tok.type == tokenize.OP and tok.string not in OPERATORS:
            raise ExpressionError(f"operator {tok.string!r} not allowed in {source!r}")
    # constructors parse_expr itself emits; user text can't name them, the token check above already ran
    emitted = ("Integer", "Float", "Rational", "Symbol", "Add", "Mul", "Pow", "Gt", "Ge", "Lt", "Le", "Eq", "Ne")
    globals_ = {"__builtins__": {}, **{name: getattr(sympy, name) for name in emitted}}
    try:
        return parse_expr(source, local_dict={**FUNCTIONS, **names}, global_dict=globals_,
                          transformations=TRANSFORMS, evaluate=evaluate)
    except Exception as e:
        raise ExpressionError(f"cannot parse {source!r}: {e}") from None


def inequality(source: str, names: dict[str, sympy.Symbol]) -> tuple[sympy.Expr, bool]:
    """Canonical form of an inequality: `a > c` and `c < a` both become (a - c, strict=True)."""
    rel = parse(source, names, evaluate=False)
    if isinstance(rel, (sympy.StrictGreaterThan, sympy.GreaterThan)):
        expr = rel.lhs - rel.rhs
    elif isinstance(rel, (sympy.StrictLessThan, sympy.LessThan)):
        expr = rel.rhs - rel.lhs
    else:
        raise ExpressionError(f"{source!r} is not an inequality")
    return sympy.simplify(expr), isinstance(rel, (sympy.StrictGreaterThan, sympy.StrictLessThan))


def same_inequality(a: tuple[sympy.Expr, bool], b: tuple[sympy.Expr, bool]) -> bool:
    return a[1] == b[1] and sympy.simplify(a[0] - b[0]) == 0


def equal(a, b) -> bool:
    return sympy.simplify(a - b) == 0


def sign_under(expr, assumptions: list[tuple[sympy.Expr, bool]], samples: int = 300, seed: int = 7) -> tuple[str, str]:
    e = sympy.simplify(expr)
    if e.is_zero:
        return "zero", "symbolic"
    if e.is_positive:
        return "positive", "symbolic"
    if e.is_negative:
        return "negative", "symbolic"
    free = sorted(e.free_symbols | {s for a, _ in assumptions for s in a.free_symbols}, key=str)
    rng = random.Random(seed)
    seen, accepted = set(), 0
    for _ in range(samples * 20):
        point = {s: _draw(s, rng) for s in free}
        if not all(_holds(a, strict, point) for a, strict in assumptions):
            continue
        value = float(e.subs(point))
        seen.add("zero" if abs(value) < 1e-12 else "positive" if value > 0 else "negative")
        accepted += 1
        if accepted == samples:
            break
    if not accepted:
        return "undetermined", "no sampled point satisfies the assumptions"
    if len(seen) == 1:
        return seen.pop(), f"sampled at {accepted} points satisfying the assumptions"
    return "mixed", f"sign changes across {accepted} sampled points satisfying the assumptions"


def _draw(symbol: sympy.Symbol, rng: random.Random) -> float:
    if symbol.is_positive:
        return rng.uniform(0.01, 100)
    if symbol.is_nonnegative:
        return rng.uniform(0, 100)
    if symbol.is_negative:
        return -rng.uniform(0.01, 100)
    if symbol.is_nonpositive:
        return -rng.uniform(0, 100)
    return rng.uniform(-100, 100)


def _holds(expr: sympy.Expr, strict: bool, point: dict) -> bool:
    value = float(expr.subs(point))
    return value > 0 if strict else value >= 0
