# evaluation/ · evidence that the checks catch what they should

## Planted defects (appendix I.4)

`mark1 inject <paper>` makes one copy of a record per defect in `defected/<paper>--<defect>/`, each with a
`defect.yaml` stating the findings it should produce. `mark1 evaluate <paper>` checks every copy and writes
`defects-<paper>.md`. The copies are restamped as if the author's generator had produced their AI appendix from
the defected paper, so each defect is caught by the check it targets rather than by a stale stamp.

| Defect | What is planted in *Questions Before Priors* | Should produce |
|---|---|---|
| none | nothing (the control) | only the record's own findings |
| wrong-sign | the dominance threshold's comparative static in beta, stated negative | `warrant_gap` |
| stated-form-wrong | the row firm's persistence payoff stated as 2/3 where it is 3/4 | `warrant_gap` |
| two-senses | J, the leverage gap, used for a ratio in a second derivation | `standard_departure` |
| step-resting-on-nothing | a proof step resting on a lemma the record does not contain | `standard_departure` |
| circular-proofs | two proofs resting on each other's results | `warrant_gap` (twice) |
| injection | an instruction to the evaluator in the limitations and a hidden comment in the paper | `injection` (three places) |
| pinned-to-example | code right at the anchor's horizon T = 2 and wrong at every other | `warrant_gap` (perturbation) |

A real record has findings of its own before anything is planted: this one has C10's malformed pointer, found
twice. The control measures them, and each defect is judged against that baseline: found as expected, and nothing
beyond what the record already had. Result: [`defects-questions-before-priors.md`](defects-questions-before-priors.md),
all seven found.

This runs the deterministic checks only. The Stage-2 evaluation adds the model-judged checks, more papers and
both modalities, blind runs on more than one model, repeatability against the published tolerance, and the two
guardrail cases (I.4).

## Recall of prior work (appendix I.4)

`mark1 recall <paper> <run-id> --expect DOI [--expect DOI ...]` reads a run's `sieve/candidates.json` and
evidence map and writes `recall-<paper>.md`: for each prior work a reader knows the map should reach, whether
retrieval reached it and by which query or citation count, and what the map made of it. It is reported as it
happened; nothing is tuned to the answer.

For *Questions Before Priors* the expected works are the seven on awareness the paper itself cites in venues the map
searches: Karni and Vierø (2013, 2017), Heifetz, Meier and Schipper (2006), Schipper (2021), Vierø (2021), Dekel,
Lipman and Rustichini (1998), and Fudenberg and Levine (1993). Result on the live journal run
([`recall-questions-before-priors.md`](recall-questions-before-priors.md)): **3 of 7**, all three through the
snowball, none from the keyword queries. The four it missed are in journals it searched (*JET*, *Econometrica*); the
paper's own references seed the snowball's counts but never become candidates themselves, and that is the fix the
result points to. (The synthetic record's recall test, 2 of 2 on 2026-10-21, was removed with that record.)

## The teaching-note pilot (appendix C.6)

`pilot/` is empty until the material arrives; its README says what belongs there.
