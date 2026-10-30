import pytest
import sympy

from machine.sym import ExpressionError, inequality, parse, same_inequality, sign_under, symbols

NAMES = symbols({"a": {"domain": "positive"}, "c": {"domain": "nonnegative"}, "p": {"domain": "nonnegative"}})


@pytest.mark.parametrize("source", [
    "__import__('os')",
    "a.__class__",
    "open('x')",
    "[a, c]",
    "lambda: 1",
    "q + a",
])
def test_author_text_cannot_reach_beyond_arithmetic(source):
    with pytest.raises(ExpressionError):
        parse(source, NAMES)


def test_parses_ascii_math():
    assert parse("(a - c)^2/4", NAMES) == (NAMES["a"] - NAMES["c"]) ** 2 / 4
    assert sympy.diff(parse("(p - c)*(a - p)", NAMES), NAMES["p"]) == NAMES["a"] + NAMES["c"] - 2 * NAMES["p"]


def test_inequalities_compare_in_canonical_form():
    assert same_inequality(inequality("a > c", NAMES), inequality("c < a", NAMES))
    assert not same_inequality(inequality("a > c", NAMES), inequality("a >= c", NAMES))


def test_sign_under_assumptions():
    a, c = NAMES["a"], NAMES["c"]
    assert sign_under(sympy.Rational(1, 2), [])[0] == "positive"
    assumptions = [inequality("a > c", NAMES)]
    assert sign_under(-(a - c) / 2, assumptions)[0] == "negative"
    assert sign_under(a - 2 * c, assumptions)[0] == "mixed"
