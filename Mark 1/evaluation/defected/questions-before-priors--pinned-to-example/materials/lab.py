"""The four-state laboratory of Example 1, computed rather than narrated.

Two firms, states s_rc on a 2x2 array, architectures 0 and 1, mechanisms theta^0, theta^1, theta^n, demand parameter
beta, and the row law tau(s_rc) = theta^r. The functions below reproduce the numbers the paper and appendix C state:
dominance thresholds, the count of repairs, deliberative leverage at the discovery and validation records, the trap
and persistence payoffs, and the two bounds. Exact arithmetic throughout; the anchor-facing functions return floats.
"""
from fractions import Fraction
from math import exp

STATES = ("s00", "s01", "s10", "s11")
ROW = {s: int(s[1]) for s in STATES}
COL = {s: int(s[2]) for s in STATES}
HALF = Fraction(1, 2)
ONE = Fraction(1)


def payoff(theta, own: int, rival: int, beta=ONE) -> Fraction:
    """One firm's payoff under mechanism theta in {0, 1, "n"} when it plays `own` and its rival plays `rival`."""
    if theta == "n":
        return HALF
    if own != rival:
        return ONE if own == theta else Fraction(0)
    return HALF if own == theta else Fraction(beta) / 2


def row_law(state: str) -> int:
    return ROW[state]


def average_payoffs(policy1, policy2, beta=ONE, law=row_law) -> tuple[Fraction, Fraction]:
    """Expected per-period payoffs under uniform rho when firm 1 plays policy1 and firm 2 plays policy2."""
    n = len(STATES)
    return (sum(payoff(law(s), policy1(s), policy2(s), beta) for s in STATES) / n,
            sum(payoff(law(s), policy2(s), policy1(s), beta) for s in STATES) / n)


def pinned(own: int, rival: int, pay: Fraction, beta=ONE) -> list:
    """The mechanisms one token (own action, rival action, payoff) leaves open."""
    return [theta for theta in (0, 1, "n") if payoff(theta, own, rival, beta) == pay]


def leverage(tokens: list[tuple], cells: dict, T: int, beta=ONE) -> dict:
    """Deliberative leverage (Definition 8.3) with each token its own group, as under pointwise transparency.

    tokens: (state, own action, rival action, payoff); cells: state -> current awareness cell.
    Returns L_fine, L_cur, J and B = (T / |r|) J, exactly as appendix C computes them.
    """
    def gain(token, a):  # robust gain of action a over the standing action, worst case over the mechanisms left open
        _, own, rival, pay = token
        return min(payoff(theta, a, rival, beta) - pay for theta in pinned(own, rival, pay, beta))

    fine = sum(max(gain(t, a) for a in (0, 1)) for t in tokens)
    cur = sum(max(sum(gain(t, a) for t in tokens if cells[t[0]] == cell) for a in (0, 1)) for cell in set(cells.values()))
    return {"L_fine": fine, "L_cur": cur, "J": fine - cur, "B": Fraction(T, len(tokens)) * (fine - cur)}


def play(policy1, policy2, states, beta=ONE) -> tuple[list[tuple], list[tuple]]:
    """The tokens each firm retains from serving `states` under the row law."""
    one, two = [], []
    for s in states:
        a1, a2 = policy1(s), policy2(s)
        one.append((s, a1, a2, payoff(row_law(s), a1, a2, beta)))
        two.append((s, a2, a1, payoff(row_law(s), a2, a1, beta)))
    return one, two


def partitions(items):
    """Every set partition of `items`."""
    items = list(items)
    if not items:
        yield []
        return
    first, rest = items[0], items[1:]
    for smaller in partitions(rest):
        for i, cell in enumerate(smaller):
            yield smaller[:i] + [[first] + cell] + smaller[i + 1:]
        yield [[first]] + smaller


def repairs(labeled=("s00", "s11")) -> dict:
    """Of all partitions of the four states, how many separate the two labelled states, and how many are minimal.

    The discovery record labels s00 (theta^0) and s11 (theta^1); a restorative refinement keeps them apart; a minimal one
    is a coarsest such refinement, which here means two cells. The paper's "eleven ruled out" is 15 - 4.
    """
    every = list(partitions(STATES))
    apart = [p for p in every if not any(set(labeled) <= set(cell) for cell in p)]
    return {"partitions": len(every), "restorative": len(apart), "minimal": sum(1 for p in apart if len(p) == 2),
            "excluded": len(every) - sum(1 for p in apart if len(p) == 2)}


# ----- the numbers the paper states, as anchors can call them --------------------------------------------------------

def dominance_threshold(p0: float, p1: float, beta: float = 1) -> float:
    """Positive exactly when architecture 0 is strictly dominant at label beliefs p0, p1: p0 > (2 - beta) p1."""
    return p0 - (2 - beta) * p1


def count_partitions(n: int = 4) -> float:
    return float(sum(1 for _ in partitions(range(n))))


def minimal_repairs() -> float:
    return float(repairs()["minimal"])


def discovery_leverage(T: int = 2, firm: int = 1) -> float:
    """Both firms differentiate (firm 1 plays 0, firm 2 plays 1) and the market serves the diagonal states: B = 1/2."""
    one, two = play(lambda s: 0, lambda s: 1, ("s00", "s11"))
    return float(leverage(one if firm == 1 else two, {s: 0 for s in STATES}, T)["B"]) * T / 2


def validation_leverage(firm: int = 2, T: int = 2) -> float:
    """Firm 1 holds the row law, firm 2 the column law; the four states are served: B_1 = 0, B_2 = 1/2."""
    one, two = play(row_law, lambda s: COL[s], STATES)
    tokens, cells = (one, ROW) if firm == 1 else (two, COL)
    return float(leverage(tokens, cells, T)["B"])


def persistence_payoff(firm: int = 1, beta: float = 0.5, c: int = 0) -> float:
    """Firm 1 on the row law against firm 2 constant on architecture c, uniform rho: 3/4 and 1/4, for any beta."""
    return float(average_payoffs(row_law, lambda s: c, Fraction(beta))[firm - 1])


def persistence_leverage(beta: float = 0.5, T: int = 2, c: int = 0) -> float:
    """The coarse firm's leverage on the balanced four-token record of the persistence configuration: 1/2."""
    _, two = play(row_law, lambda s: c, STATES, Fraction(beta))
    return float(leverage(two, {s: 0 for s in STATES}, T, Fraction(beta))["B"])


def trap_payoff(beta: float = 1, state: str = "s01") -> float:
    """Both firms pool on the column law. At beta = 1 every payoff is 1/2; at an off-diagonal state it is beta/2."""
    return float(payoff(row_law(state), COL[state], COL[state], Fraction(beta)))


def warrant_gap(coherence: float = 1, warrant: float = 0.5) -> float:
    return coherence - warrant


def false_alarm_bound(b: float) -> float:
    """Ville's inequality: a theory adequate from initialization is rejected with probability at most e^{-b}."""
    return exp(-b)


def refinement_bound(n: int = 2, states: int = 4) -> float:
    """At most n(|S| - 1) successful refinements can ever occur (Theorem 10.4(a))."""
    return float(n * (states - 1))


if __name__ == "__main__":
    print("repairs", repairs())
    print("discovery leverage", discovery_leverage(), "validation", validation_leverage(1), validation_leverage(2))
    print("persistence payoffs", persistence_payoff(1), persistence_payoff(2), "leverage", persistence_leverage())
    print("trap payoff at beta 0.8", trap_payoff(0.8), "dominance threshold", dominance_threshold(0.6, 0.4))
