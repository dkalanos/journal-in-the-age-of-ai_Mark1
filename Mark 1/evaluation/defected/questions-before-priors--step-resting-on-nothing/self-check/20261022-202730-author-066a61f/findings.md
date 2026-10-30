# Findings report · questions-before-priors

Findings only: no verdict, score, ranking, or recommendation. Every finding points into the record and into the standard it was checked against.

| | |
|---|---|
| Run | `20261022-202730-author-066a61f` |
| Run by | author |
| Record | `sha256:066a61fe6cbc874e` |
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

### F-3-soundness-01 · `standard_departure` · main claim

**Step 1 of derivation D7 rests on appendix/appendix.md#a-lemma-nobody-wrote, which is not in the record.**

- Record: `derivations:D7`
- Standard: `standard/formal.md#S8`
- Why: no section #a-lemma-nobody-wrote in appendix/appendix.md
- Produced by: deterministic check `soundness` 0.4.0, code `c2e0745f3318`

## Checks not run

- **completeness**: deterministic-only run: the model-judged part was not run
- **resolution**: deterministic-only run: the model-judged part was not run
- **derivation**: deterministic-only run: the model-judged part was not run
- **contribution**: deterministic-only run: the model-judged part was not run
- **injection**: deterministic-only run: the model-judged part was not run
