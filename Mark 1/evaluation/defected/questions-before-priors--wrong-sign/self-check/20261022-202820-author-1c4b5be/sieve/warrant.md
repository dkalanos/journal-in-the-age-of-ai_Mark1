# SIEVE · warrant findings · questions-before-priors

Findings only: no verdict, score, ranking, or recommendation. Every finding points into the record and into the standard it was checked against.

| | |
|---|---|
| Run | `20261022-202820-author-1c4b5be` |
| Run by | author |
| Record | `sha256:1c4b5be14c49b88e` |
| Versions | protocol formal-0.2 · checks 0.4.0 · generator 0.1.0 · standard formal-0.3 |
| Check code | `c2e0745f3318` |
| Models | deterministic checks only |
| AI appendix | submitted with the record |
| Bundles answered | 0 |

## Level 1 · Form

_No findings._

## Level 2 · Correspondence

_No findings._

## Level 3 · Warrant (SIEVE)

### F-3-soundness-01 · `warrant_gap`

**Comparative static dthreshold/dbeta is stated negative but is positive under the assumptions of derivation D1.**

- Record: `derivations:D1`
- Standard: `standard/formal.md#S3`
- Why: dthreshold/dbeta = p1; sampled at 54 points satisfying the assumptions
- Produced by: deterministic check `soundness` 0.4.0, code `c2e0745f3318`

## Checks not run

- **completeness**: deterministic-only run: the model-judged part was not run
- **resolution**: deterministic-only run: the model-judged part was not run
- **derivation**: deterministic-only run: the model-judged part was not run
- **contribution**: deterministic-only run: the model-judged part was not run
- **injection**: deterministic-only run: the model-judged part was not run
