# 1-journal/ · J1, what the journal publishes before any paper arrives

The five published objects (appendix D.1), each versioned in `checks/versions.yaml`, and the corpus the evidence
map searches. Every findings report and certificate carries these versions.

| Object | Where | Version |
|---|---|---|
| 1. Record protocol, formal theory | `protocol/formal.md`, schemas in `protocol/schemas/` | formal-0.1 |
| The other modalities, specified | `protocol/modalities.md` | |
| 2. The checks | the instructions in `checks/prompts/`, the code in `../machine/`, repeatability in `tolerance.yaml` | 0.1.0 |
| 3. The standard, formal theory | `standard/formal.md` | formal-0.1 |
| 4. The mapping from findings to standard actions | `mapping.yaml` | 0.3 |
| 5. The interest criteria | `interest-criteria.md` | 0.1 |
| The corpus behind the evidence map | `corpus/venues.yaml` (UTD24, FT50, CABS 4*/4, searched through OpenAlex) and `corpus/corpus.yaml` (a hand list); README there | hash of their contents |

The protocol belongs to the field and is shared across journals. Objects 2 to 5 and the corpus are this
journal's own; that is where journals differ, and should. The standard and the interest criteria here are
demonstration text.
