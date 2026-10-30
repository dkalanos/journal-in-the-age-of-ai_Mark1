"""The four-state laboratory of Example 1 in *Questions Before Priors* (round-1 draft, 2026-07-23), computed, not narrated.

Two firms, states s_rc on a 2x2 array, architectures {0, 1}, mechanisms theta^0, theta^1, theta^n, demand parameter
beta in [0, 1], the row law tau(s_rc) = theta^r, and the exact (eta = 0) instance of every test. The record is built
generation by generation, as the paper tells it: a discovery generation in which the coarse firms differentiate (firm 1
on architecture 0, firm 2 on 1) and s00 and s11 are served; then one of three continuations, each played on top of the
retained record (assumption 3.3): validation (firm 1 row-refined on the row law, firm 2 column-refined on the column
law), the trap (both column-refined, pooled on the column law) and persistence (firm 1 on the row law, firm 2 still
coarse and constant). Exact arithmetic throughout; the anchor-facing functions take keyword parameters named by the
paper's symbols, default to the paper's values, and return floats.

Leverage here is the retained-record leverage of Definition 7.3 (paper.md#def-leverage), which round 1 states: a sum
over retained tokens of the robust gain, over the carried-forward policy, of the best rule measurable with respect to
the pinned structure, with no horizon normalisation. `leverage` computes that definition literally: the minimally
restorative refinements of Definition 6.1, the mechanisms they can assign each token (Definition 7.2), the pinned
structure as the finest common coarsening of the induced token partitions, and the maximum over measurable rules. The
later draft's deliberative leverage over coherent groupings is not round 1's and is not here.

Which sentence each anchor-facing function reproduces (ids are headings of paper/paper.md and appendix/appendix.md):

  dominance_gain             appendix#dominance-thresholds: against a rival playing 0 the subjective expected-payoff
                             difference between own actions 0 and 1 is p0/2 - (1 - beta/2) p1; against a rival
                             playing 1 it is (1 - beta/2) p0 - p1/2.
  dominance_threshold        appendix#dominance-thresholds, paper#example-1-continued-2: action 0 is strictly dominant
                             iff p0 > (2 - beta) p1; at beta = 1 simple belief asymmetry; certainty in a label keeps
                             the labeled action dominant for every beta.
  discovery_payoff           paper#example-1-continued-2: firm 1 wins at s00 (payoffs 1, 0) and loses at s11
                             (payoffs 0, 1); pooled, each would have received one-half at every episode.
  discovery_active_theories  paper#example-1-continued-2: no constant assignment is consistent with both episodes
                             (the active set empties: 0); the pooled profile is consistent with all three (3).
  count_partitions           paper#example-1-continued-3: the fifteen partitions of four states.
  minimal_repairs            paper#example-1-continued-3: exactly four are minimally restorative.
  excluded_partitions        paper#example-1-continued-3: eleven partitions are excluded.
  worst_case_success         paper#example-1-continued-3: a randomized rule succeeds in the worst case with
                             probability at most one-half.
  robust_partition_cells     paper#example-1-continued-3: a partition sufficient for both worlds must be the full
                             partition into singletons (four cells; Proposition 6.6).
  extrapolation_errors       paper#example-1-continued-3: whichever factor refinement arrives, its unique consistent
                             theory extrapolates the wrong prediction to the two unlabeled states in one of the worlds.
  unit_gain                  appendix#unit-leverage, paper#example-1-continued-4: implementing the revealed label a*
                             gains exactly one-half against every rival action (0 -> 1/2 if the rival plays a*;
                             1/2 -> 1 if the rival plays a).
  discovery_leverage         paper#example-1-continued-4, appendix#unit-leverage: B_i = 1/2 for both firms.
  validation_leverage        paper#example-1-continued-4, appendix#unit-leverage: B_1 = 0 and B_2 = 1.
  election_value             paper#prop-participation, paper#example-1-continued-4: the represented value
                             lambda_i B_i - gamma_i; a firm elects iff it is >= 0 (lambda_i/2 >= gamma_i after
                             discovery, lambda_2 >= gamma_2 after validation).
  coherence                  paper#example-1-continued-5: the recoded record pins a unique consistent theory and
                             representation-relative coherence assigns it probability one (row or column refinement).
  warrant                    paper#example-1-continued-5: W = 1/2 under a symmetric prior over the row and column
                             worlds; one differentiated off-diagonal observation closes the gap and pooled observations
                             close nothing. paper#example-1-continued-6: half-warranted forever at beta = 1; the
                             reflective posterior becomes degenerate for beta < 1.
  warrant_gap                paper#example-1-continued-5: the warrant gap is exactly one-half.
  trap_payoff                paper#example-1-continued-6, appendix#the-trap-and-its-knife-edge: every payoff is
                             one-half at beta = 1; beta/2 at an off-diagonal state for beta < 1.
  trap_prediction            the same: one-half is exactly what the column theory predicts under pooled play.
  trap_prediction_error      the knife edge: realized payoff short of the prediction by (1 - beta)/2 at an
                             off-diagonal state, zero exactly at beta = 1.
  destroyed_value            paper#example-1-continued-6: the destroyed value 1 - beta at each misserved episode.
  active_theories            appendix#the-trap-and-its-knife-edge: active sets never empty at beta = 1 and the active
                             set empties for beta < 1; appendix#persistence-payoffs: firm 2's record rejects all three
                             constant theories; paper#example-1-continued-4: firm 1's record agrees with its policy.
  trap_leverage              paper#example-1-continued-6, appendix#the-trap-and-its-knife-edge: B_i = 0 at beta = 1;
                             leverage turns positive for beta < 1.
  persistence_payoff         paper#example-1-continued-6, appendix#persistence-payoffs: three-quarters and one-quarter
                             under uniform rho.
  persistence_leverage       appendix#persistence-payoffs: "dissonance with B_2 > 0". Definition 7.3 on the full
                             retained record gives 0; see that function's docstring for why and for the two readings
                             under which it is positive.
  refinement_bound           paper#thm-absorption (a): at most n(|S| - 1) refinements occur.

The functions read no files, print nothing outside `__main__`, and use no randomness; run the module to print each
value beside the number the text states.
"""
from collections import namedtuple
from fractions import Fraction
from itertools import product

STATES = ("s00", "s01", "s10", "s11")
ROW = {s: int(s[1]) for s in STATES}
COL = {s: int(s[2]) for s in STATES}
MECHANISMS = (0, 1, "n")  # theta^0, theta^1, theta^n
HALF = Fraction(1, 2)
ONE = Fraction(1)
ZERO = Fraction(0)
DISCOVERY_STATES = ("s00", "s11")

Token = namedtuple("Token", "state own rival pay")  # one retained episode: the state (analyst level), own action, the
#                                                      rival's action and the own payoff (assumption 3.3)


def partition(*cells) -> frozenset:
    return frozenset(frozenset(cell) for cell in cells)


COARSE = partition(STATES)
ROWS = partition(("s00", "s01"), ("s10", "s11"))
COLUMNS = partition(("s00", "s10"), ("s01", "s11"))
REFINEMENTS = {"row": ROWS, "column": COLUMNS}


# ----- primitives ---------------------------------------------------------------------------------------------------

def payoff(theta, own: int, rival: int, beta=ONE) -> Fraction:
    """One firm's payoff under mechanism theta in {0, 1, "n"} when it plays `own` and its rival plays `rival`
    (Example 1, paper#ex-setup): differentiated, the firm offering the preferred architecture gets 1 and its rival 0;
    pooled on the preferred architecture, 1/2 each; pooled on the other, beta/2 each; under theta^n, 1/2 regardless."""
    if theta == "n":
        return HALF
    if own != rival:
        return ONE if own == theta else ZERO
    return HALF if own == theta else Fraction(beta) / 2


def row_law(state: str) -> int:
    """tau(s_rc) = theta^r, the objective assignment; also firm 1's row policy, which plays the row's label."""
    return ROW[state]


def column_law(state: str) -> int:
    """tau'(s_rc) = theta^c, the column world; also the column policy, which plays the column's label."""
    return COL[state]


def constant(a: int):
    """The constant policy, the only kind a coarse firm can commit to."""
    return lambda state: a


WORLDS = {"row": row_law, "column": column_law}


def play(policy1, policy2, states, beta=ONE, world=row_law) -> tuple[list, list]:
    """The tokens each firm retains from serving `states` under `world` (the row law unless said otherwise)."""
    one, two = [], []
    for s in states:
        a1, a2 = policy1(s), policy2(s)
        one.append(Token(s, a1, a2, payoff(world(s), a1, a2, beta)))
        two.append(Token(s, a2, a1, payoff(world(s), a2, a1, beta)))
    return one, two


def average_payoffs(policy1, policy2, beta=ONE) -> tuple[Fraction, Fraction]:
    """Expected per-episode payoffs under uniform rho."""
    one, two = play(policy1, policy2, STATES, beta)
    return sum(t.pay for t in one) / len(STATES), sum(t.pay for t in two) / len(STATES)


# ----- the test, active sets and restorative refinements (Definitions 5.1, 6.1, Proposition 6.2) --------------------

def coherent(cell, record, beta=ONE) -> list:
    """The mechanisms that fit every retained token of `cell` exactly: the eta = 0 test of Definition 5.1 on one cell."""
    return [th for th in MECHANISMS if all(payoff(th, t.own, t.rival, beta) == t.pay for t in record if t.state in cell)]


def active_set(P, record, beta=ONE) -> list:
    """The expressible theories on partition P consistent with the recoded record: one coherent mechanism per cell
    (Proposition 6.2). Each theory is a dict cell -> mechanism; the list is empty exactly under dissonance."""
    cells = sorted(P, key=sorted)
    return [dict(zip(cells, choice)) for choice in product(*(coherent(c, record, beta) for c in cells))]


def cell_of(P, state: str):
    return next(cell for cell in P if state in cell)


def partitions(items):
    """Every set partition of `items`, as lists of lists."""
    items = list(items)
    if not items:
        yield []
        return
    first, rest = items[0], items[1:]
    for smaller in partitions(rest):
        for i, cell in enumerate(smaller):
            yield smaller[:i] + [[first] + cell] + smaller[i + 1:]
        yield [[first]] + smaller


def all_partitions() -> list:
    return [partition(*p) for p in partitions(STATES)]


def refines(fine, coarse) -> bool:
    return all(any(cell <= big for big in coarse) for cell in fine)


def strictly_refines(fine, coarse) -> bool:
    return fine != coarse and refines(fine, coarse)


def restorative(P, record, beta=ONE) -> list:
    """The strict refinements of P whose recoded active set is nonempty (Definition 6.1)."""
    return [Q for Q in all_partitions() if strictly_refines(Q, P) and active_set(Q, record, beta)]


def minimal_restorative(P, record, beta=ONE) -> list:
    """R(P, r): the restorative refinements with no restorative partition strictly between P and them."""
    R = restorative(P, record, beta)
    return [Q for Q in R if not any(strictly_refines(Q, M) for M in R)]


# ----- retained-record leverage (Definitions 7.2 and 7.3) -----------------------------------------------------------

def leverage(record, P, policy, beta=ONE, repairs=None) -> Fraction:
    """B_i(r_i) of equation (6): the maximum, over rules psi measurable with respect to the pinned structure, of the sum
    over retained tokens of the worst-case gain of psi(t) over the carried-forward action sigma(t), the worst case taken
    over the rival's actions and over the mechanisms some admissible repair assigns the token. Zero when there is no
    dissonance (the active set on P is nonempty) or when no repair exists.

    `repairs` restricts the admissible repairs to a given set (the technology's range); by default they are the
    minimally restorative refinements R(P, r) of Definition 6.1, as Definition 7.2 says.
    """
    if not record or active_set(P, record, beta):
        return ZERO
    if repairs is None:
        R = minimal_restorative(P, record, beta)
    else:
        R = [Q for Q in repairs if strictly_refines(Q, P) and active_set(Q, record, beta)]
    if not R:
        return ZERO
    index = range(len(record))
    # Theta_i(t): the mechanisms some repair's active theory assigns to the token's recurrence
    allowed = {i: {th for Q in R for th in coherent(cell_of(Q, record[i].state), record, beta)} for i in index}
    # Lambda_i(r_i): tokens that share a cell under some repair must share a rule; the finest common coarsening
    group = {i: i for i in index}

    def root(i):
        while group[i] != i:
            i = group[i]
        return i

    for Q in R:
        for cell in Q:
            members = [i for i in index if record[i].state in cell]
            for i in members[1:]:
                group[root(i)] = root(members[0])
    pinned = {}
    for i in index:
        pinned.setdefault(root(i), []).append(i)

    def gain(i, a):
        t = record[i]
        sigma = policy(t.state)
        return min(payoff(th, a, rival, beta) - payoff(th, sigma, rival, beta)
                   for rival in (0, 1) for th in allowed[i])

    return sum(max(sum(gain(i, a) for i in members) for a in (0, 1)) for members in pinned.values())


# ----- the generations of the example ---------------------------------------------------------------------------------

STAGES = {  # stage -> ((awareness of firm 1, of firm 2), c -> (policy of firm 1, of firm 2))
    "discovery": ((COARSE, COARSE), lambda c: (constant(0), constant(1))),
    "validation": ((ROWS, COLUMNS), lambda c: (row_law, column_law)),
    "trap": ((COLUMNS, COLUMNS), lambda c: (column_law, column_law)),
    "persistence": ((ROWS, COARSE), lambda c: (row_law, constant(c))),
}


def discovery(beta=ONE, a1: int = 0, a2: int = 1, states=DISCOVERY_STATES) -> tuple[list, list]:
    """The discovery generation: coarse firms on constant policies a1 and a2; s00 and s11 served."""
    return play(constant(a1), constant(a2), states, beta)


def epistemic_states(stage: str = "discovery", beta=ONE, c: int = 1, states=None, retain: bool = True) -> list:
    """(record, awareness, carried-forward policy) of each firm after `stage`. A continuation's record is the discovery
    record followed by one generation of the continuation's play over `states` (all four by default); `retain=False`
    drops the discovery tokens. In persistence, firm 2 plays architecture c; c = 1 is the policy it committed to in the
    opening generation and carries forward under dissonance (assumption 3.4)."""
    awareness, make = STAGES[stage]
    policies = make(c)
    if stage == "discovery":
        records = discovery(beta, states=states or DISCOVERY_STATES)
    else:
        earlier = discovery(beta) if retain else ([], [])
        now = play(*policies, states or STATES, beta)
        records = (earlier[0] + now[0], earlier[1] + now[1])
    return [(records[i], awareness[i], policies[i]) for i in (0, 1)]


def repairs(beta=ONE) -> dict:
    """Of the 15 partitions of the four states at firm 1's discovery record: how many are restorative, how many minimally
    so, and how many the paper counts as excluded (15 minus the minimal ones)."""
    record = discovery(beta)[0]
    every = all_partitions()
    minimal = minimal_restorative(COARSE, record, beta)
    return {"partitions": len(every), "restorative": len(restorative(COARSE, record, beta)), "minimal": len(minimal),
            "excluded": len(every) - len(minimal)}


def _leverage_at(stage, firm, beta, c=1, states=None, retain=True, repairs=None) -> Fraction:
    record, P, sigma = epistemic_states(stage, Fraction(beta), c, states, retain)[firm - 1]
    return leverage(record, P, sigma, Fraction(beta), repairs)


# ----- the numbers the paper states, as anchors call them -----------------------------------------------------------

def dominance_gain(p0: float = 0.6, p1: float = 0.4, beta: float = 1, rival: int = 0) -> float:
    """Subjective expected-payoff difference between own actions 0 and 1 against a rival playing `rival`, with belief
    mass p0 on theories assigning theta^0 and p1 on theta^1 at the cell (theta^n pays 1/2 either way and drops out):
    p0/2 - (1 - beta/2) p1 against 0, (1 - beta/2) p0 - p1/2 against 1. The paper states no belief numbers; the
    defaults are a belief asymmetry favouring 0."""
    return float(sum(Fraction(p) * (payoff(a, 0, rival, Fraction(beta)) - payoff(a, 1, rival, Fraction(beta)))
                     for a, p in ((0, p0), (1, p1))))


def dominance_threshold(p0: float = 0.6, p1: float = 0.4, beta: float = 1) -> float:
    """p0 - (2 - beta) p1: positive exactly when architecture 0 is strictly dominant on the cell. It is twice the gain
    against a rival playing 0, the binding one of the two; at beta = 1 it is p0 - p1, simple belief asymmetry."""
    return float(Fraction(p0) - (2 - Fraction(beta)) * Fraction(p1))


def discovery_payoff(firm: int = 1, state: str = "s00", beta: float = 1, a1: int = 0, a2: int = 1) -> float:
    """The payoff to `firm` at `state` in the discovery generation when firm 1 plays a1 and firm 2 plays a2 under the
    row law: differentiated (0, 1), firm 1 gets 1 at s00 and 0 at s11; pooled (a1 = a2), 1/2 each at beta = 1."""
    own, rival = ((a1, a2), (a2, a1))[firm - 1]
    return float(payoff(row_law(state), own, rival, Fraction(beta)))


def discovery_active_theories(a1: int = 0, a2: int = 1, beta: float = 1, firm: int = 1) -> float:
    """How many of the three constant theories survive the discovery record (s00 and s11 served) under the coarse
    partition: none under differentiated play, all three under pooled play."""
    return float(len(active_set(COARSE, discovery(Fraction(beta), a1, a2)[firm - 1], Fraction(beta))))


def count_partitions(n: int = 4) -> float:
    return float(sum(1 for _ in partitions(range(n))))


def minimal_repairs() -> float:
    return float(repairs()["minimal"])


def excluded_partitions() -> float:
    return float(repairs()["excluded"])


def worst_case_success(q: float = 0.5) -> float:
    """A truth-blind rule that formulates the row refinement with probability q and the column refinement otherwise
    succeeds with probability q in the row world and 1 - q in the column world; its worst case min(q, 1 - q) is at most
    one-half, attained at q = 1/2."""
    return float(min(Fraction(q), 1 - Fraction(q)))


def robust_partition_cells(worlds=("row", "column")) -> float:
    """Cells of the coarsest partition sufficient for every named world, the join of their causal-equivalence partitions
    (Proposition 6.6): for the row and column worlds, the four singletons."""
    return float(len({tuple(WORLDS[w](s) for w in worlds) for s in STATES}))


def extrapolation_errors(refinement: str = "column", world: str = "row") -> float:
    """States at which the unique theory consistent with firm 1's discovery record on `refinement` mispredicts the
    mechanism of `world`: the two unlabeled states when refinement and world cross, none when they agree."""
    P, law = REFINEMENTS[refinement], WORLDS[world]
    theories = active_set(P, discovery()[0])
    if len(theories) != 1:
        raise ValueError(f"the {refinement} refinement leaves {len(theories)} consistent theories, not one")
    return float(sum(1 for s in STATES if theories[0][cell_of(P, s)] != law(s)))


def unit_gain(rival: int = 0, a_star: int = 0, beta: float = 1) -> float:
    """At a retained episode labelled a* where the committed policy prescribes a != a*, the gain of implementing a* at
    its recurrence when the rival plays `rival`: 1/2 - 0 if the rival plays a*, 1 - beta/2 if the rival plays a; both
    exactly one-half at beta = 1."""
    a = 1 - a_star
    return float(payoff(a_star, a_star, rival, Fraction(beta)) - payoff(a_star, a, rival, Fraction(beta)))


def discovery_leverage(firm: int = 1, beta: float = 1) -> float:
    """Definition 7.3 at the dissonant discovery record: B_i = 1/2 for both firms."""
    return float(_leverage_at("discovery", firm, beta))


def validation_leverage(firm: int = 2, beta: float = 1) -> float:
    """After the validation generation on the retained record: B_1 = 0 (no dissonance) and B_2 = 1 (two disagreeing
    tokens, each worth one-half)."""
    return float(_leverage_at("validation", firm, beta))


def election_value(lam: float = 1, B: float = 0.5, gamma: float = 0.25) -> float:
    """lambda_i B_i - gamma_i, the represented value of electing inquiry (Proposition 7.4); the firm elects iff it is
    nonnegative. The paper states no numbers for lambda or gamma."""
    return float(Fraction(lam) * Fraction(B) - Fraction(gamma))


def coherence(refinement: str = "column", firm: int = 1, beta: float = 1, stage: str = "discovery") -> float:
    """Representation-relative coherence of the formulated theory: the acting-belief mass a uniform bridge prior leaves
    on it after judged updating on the recoded record, 1/|active set|; one when the record pins a unique theory, zero
    under dissonance."""
    record = epistemic_states(stage, Fraction(beta))[firm - 1][0]
    n = len(active_set(REFINEMENTS[refinement], record, Fraction(beta)))
    return float(Fraction(1, n)) if n else 0.0


def warrant(world: str = "column", stage: str = "discovery", firm: int = 1, beta: float = 1, nu: float = 0.5) -> float:
    """Selection-adjusted warrant W of `world` (Definition 8.1): the posterior, from a prior putting nu on `world` and
    1 - nu on the other, that it is the objective assignment given the firm's record at `stage`. Mechanisms are
    deterministic, so a world's likelihood is one if it reproduces every retained payoff and zero otherwise; the
    production event adds nothing because the technology is truth-blind (Theorem 8.2)."""
    record = epistemic_states(stage, Fraction(beta))[firm - 1][0]
    other = next(w for w in WORLDS if w != world)
    like = {w: ONE if all(payoff(law(t.state), t.own, t.rival, Fraction(beta)) == t.pay for t in record) else ZERO
            for w, law in WORLDS.items()}
    weighted = Fraction(nu) * like[world]
    return float(weighted / (weighted + (1 - Fraction(nu)) * like[other]))


def warrant_gap(coherence: float = 1, W: float = 0.5) -> float:
    """Coherence minus warrant: exactly one-half for the firm that formulated on the discovery record."""
    return float(Fraction(coherence) - Fraction(W))


def trap_payoff(beta: float = 1, state: str = "s01") -> float:
    """Both firms pooled on the column policy under the row law: 1/2 everywhere at beta = 1; beta/2 at an off-diagonal
    state, where the pooled architecture is the wrong one, for beta < 1."""
    return float(payoff(row_law(state), column_law(state), column_law(state), Fraction(beta)))


def trap_prediction(state: str = "s01", beta: float = 1) -> float:
    """What the column theory predicts under pooled column play: one-half at every state, for every beta."""
    return float(payoff(column_law(state), column_law(state), column_law(state), Fraction(beta)))


def trap_prediction_error(beta: float = 0.8, state: str = "s01") -> float:
    """Prediction minus realized payoff under the trap: (1 - beta)/2 at an off-diagonal state, zero on the diagonal and
    zero everywhere exactly at beta = 1, the knife edge on which the trap is a SCUE."""
    return trap_prediction(state, beta) - trap_payoff(beta, state)


def destroyed_value(beta: float = 0.8) -> float:
    """The unit value the customer withholds at a misserved episode, 1 - beta."""
    return float(1 - Fraction(beta))


def active_theories(stage: str = "trap", firm: int = 1, beta: float = 1, c: int = 1, retain: bool = True) -> float:
    """The number of expressible theories consistent with the firm's retained record under its awareness at `stage`:
    positive means no dissonance, zero means the active set has emptied."""
    record, P, _ = epistemic_states(stage, Fraction(beta), c, None, retain)[firm - 1]
    return float(len(active_set(P, record, Fraction(beta))))


def trap_leverage(beta: float = 1, firm: int = 1, states=STATES) -> float:
    """Definition 7.3 after a trap generation serving `states`: 0 at beta = 1 (no episode is labeled); positive for
    beta < 1 once an off-diagonal state is served, one-half per off-diagonal token."""
    return float(_leverage_at("trap", firm, beta, states=states))


def persistence_payoff(firm: int = 1, beta: float = 1, c: int = 1) -> float:
    """Firm 1 on the row law against firm 2 constant on architecture c, uniform rho: 3/4 and 1/4, for any beta and c."""
    return float(average_payoffs(row_law, constant(c), Fraction(beta))[firm - 1])


def persistence_leverage(beta: float = 1, c: int = 1, factor_seeking: bool = False, states=STATES,
                         retain: bool = True) -> float:
    """Firm 2's leverage in the persistence configuration. Appendix B states B_2 > 0; Definition 7.3 on the full retained
    record gives 0 at beta = 1, and this function returns what the definition gives.

    Why: the record pins theta^0 at the two states firm 2 lost and theta^1 at s11, but the fourth state is served pooled
    on the preferred architecture, pays 1/2, and so fits every mechanism. The two minimally restorative refinements of
    the coarse partition place that state on opposite sides, their finest common coarsening is the trivial partition,
    and the only pinned-structure-measurable rules are the constants: switching gains one-half at each lost token and
    loses one-half at each token on the other side, for a total of zero. Two readings make it positive: restrict the
    admissible repairs to the factor refinements the example's technology produces (`factor_seeking=True`, giving 3/2),
    or let the persistence generation serve only the differentiated states (`states=("s00", "s01")` for c = 1, also
    3/2). Without the retained discovery tokens (`retain=False`) one constant theory survives at beta = 1 and there is
    no dissonance at all."""
    repairs_ = [ROWS, COLUMNS] if factor_seeking else None
    return float(_leverage_at("persistence", 2, beta, c, states, retain, repairs_))


def refinement_bound(n: int = 2, states: int = 4) -> float:
    """At most n(|S| - 1) refinements ever occur (Theorem 9.4(a))."""
    return float(n * (states - 1))


# ----- validation: each value beside the number the text states --------------------------------------------------------

if __name__ == "__main__":
    S01, S00 = "s01", "s00"
    rows = [
        # (what, computed, stated: a number, or "positive" / "zero" for a sign the text states)
        ("dominance gain vs rival 0, (p0, p1, beta) = (0.6, 0.4, 1) = p0/2 - (1 - beta/2) p1", dominance_gain(0.6, 0.4, 1, 0), 0.1),
        ("dominance gain vs rival 1, (0.6, 0.4, 1) = (1 - beta/2) p0 - p1/2", dominance_gain(0.6, 0.4, 1, 1), 0.1),
        ("dominance gain vs rival 0, (0.7, 0.3, 0.5)", dominance_gain(0.7, 0.3, 0.5, 0), 0.35 - 0.75 * 0.3),
        ("dominance gain vs rival 1, (0.7, 0.3, 0.5)", dominance_gain(0.7, 0.3, 0.5, 1), 0.75 * 0.7 - 0.15),
        ("dominance threshold (0.6, 0.4, 1) = p0 - (2 - beta) p1 = 2 x gain vs rival 0", dominance_threshold(0.6, 0.4, 1), 2 * dominance_gain(0.6, 0.4, 1, 0)),
        ("dominance threshold at beta = 1 is belief asymmetry p0 - p1", dominance_threshold(0.6, 0.4, 1), 0.2),
        ("dominance threshold under certainty (1, 0, beta = 0) is positive", dominance_threshold(1, 0, 0), "positive"),
        ("discovery: firm 1 at s00 wins 1", discovery_payoff(1, "s00"), 1),
        ("discovery: firm 2 at s00 gets 0", discovery_payoff(2, "s00"), 0),
        ("discovery: firm 1 at s11 gets 0", discovery_payoff(1, "s11"), 0),
        ("discovery: firm 2 at s11 wins 1", discovery_payoff(2, "s11"), 1),
        ("discovery pooled on 0 at s00: one-half", discovery_payoff(1, "s00", a1=0, a2=0), 0.5),
        ("discovery pooled on 0 at s11: one-half at beta = 1", discovery_payoff(1, "s11", a1=0, a2=0), 0.5),
        ("discovery, differentiated: constant theories surviving (active set empties)", discovery_active_theories(0, 1), 0),
        ("discovery, pooled: consistent with all three constant theories", discovery_active_theories(0, 0), 3),
        ("fifteen partitions of four states", count_partitions(), 15),
        ("exactly four minimally restorative", minimal_repairs(), 4),
        ("eleven partitions excluded", excluded_partitions(), 11),
        ("randomized rule, worst case at q = 1/2: one-half", worst_case_success(0.5), 0.5),
        ("randomized rule, worst case over q in {0, .1, ..., 1} at most one-half", max(worst_case_success(k / 10) for k in range(11)), 0.5),
        ("partition sufficient for both worlds: singletons, four cells", robust_partition_cells(), 4),
        ("column refinement extrapolates wrongly at two states of the row world", extrapolation_errors("column", "row"), 2),
        ("row refinement extrapolates wrongly at two states of the column world", extrapolation_errors("row", "column"), 2),
        ("row refinement is right everywhere in the row world", extrapolation_errors("row", "row"), 0),
        ("unit gain, rival plays a*: 0 -> 1/2", unit_gain(rival=0, a_star=0), 0.5),
        ("unit gain, rival plays a: 1/2 -> 1", unit_gain(rival=1, a_star=0), 0.5),
        ("B_1 after discovery", discovery_leverage(1), 0.5),
        ("B_2 after discovery", discovery_leverage(2), 0.5),
        ("B_1 after validation", validation_leverage(1), 0),
        ("B_2 after validation", validation_leverage(2), 1),
        ("election value lambda B - gamma at (1, 1/2, 1/2): the boundary lambda/2 = gamma", election_value(1, 0.5, 0.5), 0),
        ("coherence of the column formulation: probability one", coherence("column"), 1),
        ("coherence of the row formulation: probability one", coherence("row"), 1),
        ("warrant of the column world after discovery, symmetric prior", warrant("column", "discovery"), 0.5),
        ("warrant of the row world after discovery", warrant("row", "discovery"), 0.5),
        ("warrant gap: coherence 1 minus W 1/2", warrant_gap(1, 0.5), 0.5),
        ("warrant of the column world after one off-diagonal differentiated observation", warrant("column", "validation"), 0),
        ("warrant of the row world after it", warrant("row", "validation"), 1),
        ("warrant of the column world after pooled observations at beta = 1 (trap): still one-half", warrant("column", "trap", beta=1), 0.5),
        ("warrant of the column world after the trap at beta = 0.8: degenerate", warrant("column", "trap", beta=0.8), 0),
        ("trap payoff at s01, beta = 1", trap_payoff(1, S01), 0.5),
        ("trap payoff at s00, beta = 1", trap_payoff(1, S00), 0.5),
        ("trap payoff at s01, beta = 0.8: beta/2", trap_payoff(0.8, S01), 0.4),
        ("trap payoff at s00, beta = 0.8: still one-half", trap_payoff(0.8, S00), 0.5),
        ("column theory's prediction under pooled play", trap_prediction(S01), 0.5),
        ("knife edge: prediction error at s01, beta = 1", trap_prediction_error(1, S01), 0),
        ("knife edge: prediction error at s01, beta = 0.8 = (1 - beta)/2", trap_prediction_error(0.8, S01), 0.1),
        ("destroyed value at beta = 0.8", destroyed_value(0.8), 0.2),
        ("trap, beta = 1: active set never empties (one column theory survives)", active_theories("trap", 1, 1), 1),
        ("trap, beta = 0.8: active set empties", active_theories("trap", 1, 0.8), 0),
        ("validation: firm 1's record agrees with its policy (one theory survives)", active_theories("validation", 1), 1),
        ("validation: firm 2's assignment falsified", active_theories("validation", 2), 0),
        ("persistence: firm 2's record rejects all three constant theories", active_theories("persistence", 2), 0),
        ("B_i in the trap at beta = 1", trap_leverage(1), 0),
        ("B_i in the trap at beta = 0.8: positive (both off-diagonal states served)", trap_leverage(0.8), "positive"),
        ("B_i in the trap at beta = 0.8, first generation with one off-diagonal state", trap_leverage(0.8, states=("s00", "s01", "s11")), "positive"),
        ("persistence payoff, firm 1: three-quarters", persistence_payoff(1), 0.75),
        ("persistence payoff, firm 2: one-quarter", persistence_payoff(2), 0.25),
        ("persistence payoffs for c = 0 and beta = 0.5", persistence_payoff(1, 0.5, 0) - persistence_payoff(2, 0.5, 0), 0.5),
        ("B_2 in persistence: appendix states positive; Definition 7.3 on the full record", persistence_leverage(), "positive"),
        ("B_2 in persistence, repairs restricted to the factor refinements", persistence_leverage(factor_seeking=True), "positive"),
        ("B_2 in persistence, only the differentiated states served", persistence_leverage(states=("s00", "s01")), "positive"),
        ("at most n(|S| - 1) = 6 refinements", refinement_bound(), 6),
    ]
    width = max(len(r[0]) for r in rows)
    agreed = 0
    for what, got, stated in rows:
        if isinstance(stated, str):
            ok = {"positive": got > 0, "zero": got == 0, "negative": got < 0}[stated]
            shown = stated
        else:
            ok = abs(got - stated) <= 1e-12
            shown = f"{stated:g}"
        agreed += ok
        print(f"{'agrees ' if ok else 'DIFFERS'}  {what:<{width}}  computed {got:g}  stated {shown}")
    print(f"\n{agreed} of {len(rows)} agree with the text;", repairs())
