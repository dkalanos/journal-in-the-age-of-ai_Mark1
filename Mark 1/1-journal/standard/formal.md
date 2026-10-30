# Standard · formal theory · version formal-0.5

Published object 3 (appendix D.1). What the Level 3 checks judge a formal paper against. It is the journal's
own, versioned, and cited by findings as `standard/formal.md#S<n>`. Demonstration text: a journal writes its
own standard.

## S1. A proposition states the conditions its derivation uses {#S1}

Every condition the derivation assumes appears in the claim as stated. A proposition stated without a
condition it needs claims more than its evidence supports. Class `standard_departure`.

## S2. The derivation follows {#S2}

The stated solution satisfies the first-order condition of the stated objective, the second-order condition
holds for the stated goal under the assumptions, and every closed form the paper states follows from the
derivation. A step that does not follow is class `warrant_gap`; a derivation that cannot be read as stated is
class `standard_departure`.

## S3. Comparative statics are signed correctly under the assumptions {#S3}

The sign of each stated comparative static is the sign of the derivative under the stated assumptions,
checked symbolically or, where that is inconclusive, at sampled points satisfying the assumptions. Class
`warrant_gap`.

## S4. Numerical examples evaluate as stated {#S4}

Each numerical example evaluates, from the derivation, to the values stated. Class `warrant_gap`.

## S5. One sense per term {#S5}

A symbol means one thing across the paper's derivations, and a term defined in the definitions of record is
used in that sense throughout. Class `standard_departure`.

## S6. The contribution claim is placed against the nearest prior work {#S6}

The contribution claim is compared with the nearest prior work in the corpus, not only with the substream the
paper cites, and placed in one of four kinds of newness, from two questions asked of each nearest work: does it
pose the question the claim answers, and does it state the claim. A new claim on a question already posed is an
*answer*; a question not posed before, with its first answer, is a *question*; a question not posed before that
results already in hand are shown to answer is a *reading*; new support for, or a new test of, a claim already
stated is *evidence*. A claim already stated with no new support is not new. The question the claim answers is the
one the paper states, carried in the claims list with a pointer to where the paper states it (protocol P4); the map
places the claim on that question, and an editor who signs on another reading of it, broader or narrower, records
the reading and the reason with the signature. When the corpus shows the claim already
established, the finding is class `established_by_prior`. This class runs high on false positives; the author
answers the map once before an editor signs "not new".

## S7. Coverage is stated {#S7}

The evidence map states what the corpus covers. When the corpus does not cover a claim's area well enough to
place it, the finding is class `uncovered`, and a specialist applies the mapping.

## S8. A proof names what it rests on {#S8}

For a result proved rather than solved (derivation kind `proof`), the provenance states the hypotheses, the
steps, and for each step what it rests on: a pointer into the record (a definition, an assumption, an earlier
result, another derivation) or a citation of work outside it. Every pointer resolves, and no result rests,
through the steps of other proofs, on itself; a location stands for a result only where a derivation says it
states the result there. A step that rests on something not in the record is class `standard_departure`; a
circular dependence is class `warrant_gap`. Whether a claim carries the hypotheses its proof lists is read by
the resolution check (protocol P10 (b)), since claims paraphrase; whether a step follows is not judged here.

## S9. Results survive re-execution under perturbation {#S9}

The robustness check this standard names for a formal paper. A reproduction anchor shows a value at one point;
the result it anchors is claimed wherever the derivation's assumptions hold. Each anchor is therefore re-run from
the record at other points those assumptions admit: its parameters that are symbols of its derivation are varied
(a count stays a count), the rest held, and at every point the record's procedure must agree with a formula of
the derivation that gives the anchor's value at the anchor's own point; a sign anchor must keep its sign. An
anchor that agrees only at the point it was written for is class `warrant_gap`. An anchor that cannot be
perturbed (no parameters, no derivation, a proof, parameters not named as the derivation's symbols) is listed
with the reason; that is coverage, not a finding.

## What this standard does not cover yet

Whether a prose derivation or proof step follows (a model judgment), proof validity beyond what S8 checks,
perturbation of results that have no anchor, and the modules for statistical-conclusion, internal, construct and
external validity. See `machine/sieve/SPECIFIED.md`. Version formal-0.5 places the claim on the question as the paper states it (S6); formal-0.4 names the four kinds of newness in S6; formal-0.3 added S9; formal-0.2 added S8; formal-0.1
covered closed-form derivations only.
