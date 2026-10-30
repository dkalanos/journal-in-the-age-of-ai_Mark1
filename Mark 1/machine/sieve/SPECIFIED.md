# SIEVE modules · built and specified

SIEVE (Kalanoski 2026) is the Level 3 warrant audit: it reports whether the claims match the evidence offered,
never whether the paper is worth publishing. No pointer, no flag. The modules follow the validity typology the
field already uses, and the modality router selects which apply.

| Module | State in Mark 1 | What it checks |
|---|---|---|
| Contribution warrant | built (`contribution.py`) | The contribution claim against the nearest prior work retrieved from the journal's venues through OpenAlex, plus any hand list; writes the evidence map with its coverage. Model judgment. |
| Modality soundness, formal, deterministic slice | built (`soundness.py`) | First- and second-order conditions, closed forms, comparative-static signs under the assumptions, numerical examples, conditions carried into claims, one sense per term. For a proof (formal-0.2): every step rests on something in the record, and nothing rests on itself. |
| Re-execution under perturbation, formal | built (`perturbation.py`) | Each reproduction anchor re-run at other points its derivation's assumptions admit, against the derivation's formula (standard S9). Results without an anchor are not perturbed. |
| Modality soundness, formal, prose steps | specified | Whether each prose step in the appendix's derivation follows from the one before. A model judgment under tolerance, with the deterministic slice as its anchor. |
| Modality soundness, simulation | specified | Verification and validation: seeds, parameter ranges, the runs behind each reported pattern. |
| Statistical-conclusion validity | specified | Test statistics consistent with reported values; power; multiple comparisons. |
| Internal validity | specified | Causal language matched to what the design licenses. |
| Construct validity | specified | Measures matched to the constructs the claims name. |
| External validity | specified | Claims generalized no further than the sample and setting support. |

The specified modules apply to the empirical modality, which is Stage 2 (appendix H).
