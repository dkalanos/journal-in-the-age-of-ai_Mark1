# questions-before-priors · Ryall, *Questions Before Priors*, as a research record

The first real paper through Mark 1, on its real history (Ryall, 2026-10-24). Round 1 is the draft of 2026-07-23 that
two machine reviews read, `tbv_mdr_Paper01-v02.tex`; round 2 is the resubmission of 2026-08-15, `tbv_mdr_GPTedit-10.tex`.
A single-authored theory paper on how an actor whose causal language has failed comes to possess a new one: finite
states and partitions, theorems with proofs; none of it an optimization the closed-form checks were first built around,
which is why this record exists.

**Source.** `demo-paper/` at the root of this repository, a frozen copy of the author's repository taken on 2026-10-24: the two drafts with
their bibliographies, the two machine reviews, and the 29 commits between the rounds. Nothing else of the working
repository is used, and nothing here has been licensed from anyone else.

**This folder is the author's record as the author keeps it.** The journal's snapshot of each submission, the findings
reports, the decisions and the review history are under [`3-editor/questions-before-priors/`](../../3-editor/questions-before-priors/).
The folder holds round 1 until round 2 is submitted; the snapshots keep each round as it was.

**How round 1 was built, and by whom** (2026-10-27, Kalanoski with Claude Code; the AI appendix corrected and the
AI-use record completed on 2026-10-28, as below):

- `paper/` and `appendix/`: `mark1 import-tex ../demo-paper/round-1/tbv_mdr_Paper01-v02.tex questions-before-priors
  --bib ../demo-paper/round-1/tbv_mdr_Paper01-v01.bib --choices sec:commitments --does-not-claim rem:scope
  "Limitations and the research program"`. Sixty labelled headings carry the TeX labels as ids; mathematics is as
  written; citations come from the .bib; drawings are dropped with their captions kept. The scope-and-choices section
  carries the paper's "Modeling commitments", Remark 9.6 and "Limitations and the research program" unchanged. The
  front notice at the head of the paper (protocol P2, formal-0.3) is written by `machine/notice.py`.
- `materials/lab.py`: the four-state laboratory of the running example as code, to this draft's definitions
  (retained-record leverage, Definition 7.3), so that the numbers appendix B states can be re-executed.
- `provenance/derivations.yaml`: closed forms for the stated numbers and `kind: proof` entries for the theorems, read
  from this draft's proofs. A reading of the author's proofs, not the author's own statement of them.
- `provenance/ai-use.yaml`: what AI did before 2026-07-23, in the author's own statement (Ryall, 2026-10-28): Codex,
  model GPT-6-Astra, for an outline and initial drafts of the text, exploration of propositions, initial drafts of
  proofs, and red-teaming before submission; ChatGPT for the two machine reviews. The entries dated 2026-10-27 and
  2026-10-28 are the record-keeping above and below.
- `ai-appendix/`: the author's statement to the machine (protocol P3), produced with the reference generator in the
  author's first self-check run (`self-check/20261027-114802-author-28648dd`, kept as the author's working run). That
  run's report was then the work list: the claims list was corrected before submission (2026-10-28), each statement the
  report found missing added with its evidence pointer and each partly supported claim given a wider pointer. The
  stamp now says the list was edited after generation, which is the ownership rule working.

**What the first record was.** Before 2026-10-27 this folder held the `-10` draft as a first submission, checked under
protocol formal-0.2 and checks 0.4.0 and returned for corrections. That history is superseded by the real one and is
kept outside the repository; `CHANGES-from-design.md` items 35–37 say what changed in the protocol in between.

**What building round 1 made visible** (the record keeper's notes, not the author's statements; each is a candidate
finding, left for the checks):

- `materials/lab.py` evaluates Definition 7.3 (retained-record leverage) in full, with the pinned structure, and
  reproduces every number appendix B and the Example 1 continuations state except one: in the persistence instance
  appendix B says firm 2 sits in dissonance with $B_2 > 0$, while the definition evaluated on firm 2's full retained
  record gives $B_2 = 0$, because the two minimally restorative repairs put the free state on opposite sides and the
  pinned structure collapses to the trivial partition. The function returns what the definition gives and exposes the
  two readings under which the sign is positive as parameters; the main text's condition $\gamma_2 > \lambda_2 B_2$ holds
  either way.
- `provenance/derivations.yaml` states Proposition 5.5's proof as "immediate from Lemma 5.2", whose genericity
  hypothesis the proposition does not state; and Proposition 9.9's proof is by one instance, where the text says
  "instances".
