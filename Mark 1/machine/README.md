# machine/ · M0 to M6

The checks and the steps around them, as a Python package with one command, `mark1`. Everything it reads
and writes is a file in this repository; there is no server and no database.

## How a run works

`mark1 check <paper>` (the author's self-check, A3) or `mark1 check <paper> --actor journal` (the journal's
intake run) does this:

1. Loads the record: `2-author/<paper>/` for the author, the submitted snapshot in
   `3-editor/<paper>/rounds/r<n>/record/` for the journal.
2. Routes on the declared modality (`modality.py`, M2). Only formal theory is built.
3. If the record has no AI appendix, runs the published generator (`generator.py`, M0).
4. Runs the checks in `checks/` and `sieve/` (M1, M3, M4) and writes the findings report (`findings.py`, M5)
   and the evidence map (`sieve/contribution.py`, M6).
5. On the journal side, marks every finding the author's own report lacks (`compare.py`).

| Module | Box | What it does |
|---|---|---|
| `checks/form.py` | M1 | Level 1: parts present, tables valid against `1-journal/protocol/schemas/`, pointers well formed, the paper's front notice present (P2), the AI-use record consistent with the declarations and the generator stamp. Deterministic. |
| `checks/completeness.py` | M3 (a) | Every claim the paper rests on is in the claims list. Model judgment. |
| `checks/resolution.py` | M3 (b) | Each claim's pointers resolve (deterministic) and its evidence says what it says (model judgment). |
| `checks/anchors.py` | M3 (c) | Re-executes each reproduction anchor in a fresh interpreter (`sandbox.py`, `anchor_runner.py`). Deterministic. |
| `generator.py` (`stamp_status`) | M0 | Whether the AI appendix still matches its generator stamp, by hash: a fact on every report's header, never a finding (protocol P3, formal-0.3). |
| `sieve/contribution.py` | M4, M6 | SIEVE contribution warrant: places the contribution claim against a candidate set retrieved from the journal's venues (`retrieval.py`), plus any hand list, and writes the evidence map. Model judgment. |
| `sieve/soundness.py` | M4 | SIEVE formal soundness, deterministic slice: first- and second-order conditions, closed forms, comparative-static signs, examples, conditions carried into claims, one sense per term; for a proof (derivation kind `proof`), that every step rests on something in the record and nothing rests on itself. |
| `sieve/perturbation.py` | M4 | SIEVE re-execution under perturbation (standard S9): each anchor re-run in one sandboxed interpreter at up to 20 other points its derivation's assumptions admit, against the derivation's formula for what it anchors; anchors that cannot be perturbed are listed with the reason. Writes `sieve/perturbation.md`. Deterministic. |
| `checks/injection.py` | all levels | Text addressed to the evaluator, hidden comments, invisible characters, plus anything a quorum of answering models reported. |
| `mapping.py` | H1 | The published mapping from findings to the standard action. |
| `workflow.py` | A4, H1/D2/H2, A5/T1, H5, H3, D3 | The signed human steps, each appended to the review history, revise and resubmit after review among them. |
| `history.py`, `state.py` | J2 | The review history and where a paper stands. |
| `attribution.py` | J2 | Who changed each file between two rounds, author or AI, read from the AI-use record and the generator stamp, with the basis named: the published generator, AI as declared, not declared this round, or the author. Lists the AI-use entries each round declares, reads a first submission against nothing (who made each file), and flags an AI-use entry that appears for the first time dated before the previous submission. It reads the declarations; it cannot verify them. |
| `stats.py` | F.4 | Departure statistics by editor. |
| `corpus.py`, `retrieval.py` | | The corpus: the venues in `1-journal/corpus/venues.yaml` searched through OpenAlex (keyword queries from the claim and the title, then the works most cited among the hits), and the hand list; sources and enrichment cached, and each run keeps its candidates, so runs resume and replay offline. |
| `fulltext.py` | M6 | Introductions for the evidence map: the journal's licensed copies first, then open-access copies, each checked against the work's title and cut at its introduction. The excerpts are other people's text: kept in the run (`sieve/introductions.json`, `bundles/`), never published. |
| `recall.py` | I.4 | The recall test: did retrieval reach the prior work a reader knows it should have, and what did the map make of it? |
| `rtf.py` | | Writes the .rtf twin (Times New Roman 12) of every document the machine produces; `mark1 rtf` does the same for the hand-written ones. The .md is the source. |
| `inject.py` | I.4 | Defected copies of a record and the evaluation that checks each defect is found, against the findings the unaltered record already has. |
| `texmd.py` | A1 | The author's helper, `mark1 import-tex`: a LaTeX paper into `paper/` and `appendix/` in the protocol's Markdown. Sections, theorem environments, labelled paragraphs and proofs become headings with ids; mathematics stays as written; citations come from the .bib; drawings are dropped with their captions kept; `--choices` and `--does-not-claim` name the passages carried into the scope-and-choices section. Not a published object; the author reads and edits what it writes. |

## The model-judged checks, answered from a chat session

A model-judged check does not call a model. It writes a prompt bundle per repetition:

    <run>/bundles/<check>/request.json      nonce, k, hashes of the instructions and the data
    <run>/bundles/<check>/k1/prompt.md      published instructions + response contract + the record, fenced
    <run>/bundles/<check>/k1/response.json  written by whoever answers
    <run>/bundles/<check>/k1/transcript.md  their reasoning

The instructions come verbatim from `1-journal/checks/prompts/<check>.md`. The record goes inside a fence
marked with a random nonce, labelled as data. The run stops with "N bundles waiting"; once they are
answered, `mark1 check --resume <run-id>` validates every answer against `1-journal/protocol/schemas/`,
checks the nonce, drops any finding whose pointer does not resolve, computes agreement across the k answers
against `1-journal/tolerance.yaml`, and finishes the report. `machine/llm/HOW-TO-ANSWER.md` is the brief for
the answering session. A changed record invalidates the bundles: the hashes no longer match.

`mark1 replay <run-id>` re-runs a finished run from its stored answers and reports any difference. Zero
differences is the repeatability demonstration for everything but the model's own sampling.

Nothing in Mark 1 calls a model service, and nothing here offers one as a way to run it. If a journal asks for
it in Stage 2, a connection would sit behind the same interface (`llm/__init__.py: Backend.ask`) and write the
same three files, so replay and the tests would not change.

## Limits stated plainly

- `sandbox.py` runs each anchor in a fresh interpreter with an empty working directory, a scrubbed
  environment and a ten-second timeout. That isolates crashes and hangs. It is not a jail: on Windows it
  does not stop network or filesystem access by the code under test.
- Author-supplied expressions are parsed only after a token whitelist (`sym.py`): declared symbols, a few
  functions, numbers and arithmetic. No attribute access, strings, brackets or builtins reach `eval`.
- A signature in this repository is a name, a time and the hashes of the files signed. It records what was
  signed; it is not cryptographic.
- The bundle backend does not see token counts, so cost is reported as the number of answers.
