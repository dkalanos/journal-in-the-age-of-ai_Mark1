# Findings report · questions-before-priors

Findings only: no verdict, score, ranking, or recommendation. Every finding points into the record and into the standard it was checked against.

| | |
|---|---|
| Run | `20261022-202641-author-ce91955` |
| Run by | author |
| Record | `sha256:ce9195528a269977` |
| Versions | protocol formal-0.2 · checks 0.4.0 · generator 0.1.0 · standard formal-0.3 |
| Check code | `c2e0745f3318` |
| Models | deterministic checks only |
| AI appendix | submitted with the record |
| Bundles answered | 0 |

## Level 1 · Form

### F-1-form-01 · `nonconformance`

**Claim C10 has a malformed evidence pointer: 'materials/lab.py:repairs'.**

- Record: `claims:C10`
- Standard: `protocol/formal.md#P9`
- Produced by: deterministic check `form` 0.4.0, code `c2e0745f3318`

## Level 2 · Correspondence

### F-2-resolution-01 · `pointer_missing`

**Claim C10: its evidence pointer does not resolve in the record.**

- Record: `claims:C10`
- Standard: `protocol/formal.md#P10`
- Why: malformed pointer 'materials/lab.py:repairs'
- Produced by: deterministic check `resolution` 0.4.0, code `c2e0745f3318`

## Level 3 · Warrant (SIEVE)

### F-3-perturbation-01 · `warrant_gap`

**Anchor A2 reproduces 0.5 at T = 2 but not at other values the assumptions of D2 admit.**

- Record: `anchors:A2`
- Standard: `standard/formal.md#S9`
- Why: at T = 1 the record's procedure gives 0.125; J (with r = 2, Lfine = 0.5, Lcur = 0 from example 1) gives 0.5; at T = 1 the record's procedure gives 0.125; B (with r = 2, Lfine = 0.5, Lcur = 0 from example 1) gives 0.25; at T = 1 the record's procedure gives 0.125; B (with r = 4, Lfine = 1, Lcur = 0 from example 2) gives 0.25 (4 points)
- Produced by: deterministic check `perturbation` 0.4.0, code `c2e0745f3318`

## Checks not run

- **completeness**: deterministic-only run: the model-judged part was not run
- **resolution**: deterministic-only run: the model-judged part was not run
- **derivation**: deterministic-only run: the model-judged part was not run
- **contribution**: deterministic-only run: the model-judged part was not run
- **injection**: deterministic-only run: the model-judged part was not run
