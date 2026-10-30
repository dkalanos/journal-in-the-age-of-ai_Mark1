# Defect detection · questions-before-priors

Each defected copy carries one planted error. Deterministic checks only (Levels 1, 2c, 2d stamp, soundness, perturbation, injection scan); the model-judged checks are evaluated in Stage 2 (appendix I.4).

The unaltered record has findings of its own, so each copy is judged against them: nonconformance at claims:C10; pointer_missing at claims:C10.

| Defect | Expected | Found beyond the record's own | Result |
|---|---|---|---|
| circular-proofs | warrant_gap at derivations:D7; warrant_gap at derivations:D8 | warrant_gap at derivations:D7; warrant_gap at derivations:D8 | detected as expected |
| injection | injection at paper/paper.md; injection at appendix/appendix.md; injection at ai-appendix/scope.md | injection at ai-appendix/scope.md:L9; injection at appendix/appendix.md:L555; injection at paper/paper.md:L2 | detected as expected |
| none | nothing | nothing | clean, as expected |
| pinned-to-example | warrant_gap at anchors:A2 | warrant_gap at anchors:A2 | detected as expected |
| stated-form-wrong | warrant_gap at derivations:D6 | warrant_gap at derivations:D6 | detected as expected |
| step-resting-on-nothing | standard_departure at derivations:D7 | standard_departure at derivations:D7 | detected as expected |
| two-senses | standard_departure at derivations:D23 | standard_departure at derivations:D23 | detected as expected |
| wrong-sign | warrant_gap at derivations:D1 | warrant_gap at derivations:D1 | detected as expected |
