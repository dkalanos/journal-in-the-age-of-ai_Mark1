# questions-before-priors · Ryall, *Questions Before Priors*, as a research record

The first real paper through Mark 1, on its real history (Ryall, 2026-10-24). Round 1 is the draft of 2026-07-23 that
two machine reviews read, `tbv_mdr_Paper01-v02.tex`; round 2 is the resubmission of 2026-08-15, `tbv_mdr_GPTedit-10.tex`.
A single-authored theory paper on how an actor whose causal language has failed comes to possess a new one: finite
states and partitions, theorems with proofs; none of it an optimization the closed-form checks were first built around,
which is why this record exists.

**Source.** `demo-paper/` at the root of this repository, a frozen copy of the author's repository taken on 2026-10-24: the two drafts with
their bibliographies, the two machine reviews, and the 29 commits between the rounds. Nothing else of the working
repository is used, and nothing here has been licensed from anyone else.

**This folder is the author's record as the author keeps it.** It now holds round 2. The journal's snapshot of each
submission, the findings reports, the decisions and the review history are under
[`3-editor/questions-before-priors/`](../../3-editor/questions-before-priors/); round 1 is `rounds/r1/` there.

**Round 1** (the draft of 2026-07-23, built 2026-10-27 by Kalanoski with Claude Code): imported with `mark1 import-tex`,
derivations read from that draft's proofs, the running example as code to its Definition 7.3, an AI-use record of what
AI did before July 23 in the author's statement of 2026-10-28, and an AI appendix from the reference generator in the
author's first self-check, kept as the author's working run. Its report was the work list: the claims list was
corrected twice before submission (2026-10-28), from that report and from the next. Then submission, the journal's run,
intake (departing from return for corrections to proceed to review, with sixteen supporting-claim findings named),
"new" deferred, the two machine reviews of July 2026 filed, revise and resubmit; all signed by Dimitrija Kalanoski.

**Round 2** (the draft of 2026-08-15, `tbv_mdr_GPTedit-10.tex`):

- `paper/`, `appendix/`, `provenance/derivations.yaml`, `materials/lab.py` and `ai-appendix/`: as built on 2026-10-21
  from this draft (import, derivations and code by Claude Code; the AI appendix from the reference generator in that
  day's author run). The front notice is added at the head of the paper and the record declares protocol formal-0.3.
  The AI appendix is not regenerated: it is the author's, and its stamp reports, as facts, that the paper changed
  after generation and that the claims list was edited after it. The claims list was corrected before submission
  (2026-10-28), with the author's own check report on the uncorrected list as the work list and then the report on
  the first correction: each statement the reports found missing added with its evidence pointer, each partly
  supported claim aimed at the passage that carries it, and C10's evidence pointer rewritten in the protocol's form.
- `provenance/ai-use.yaml`: round 1's entries first; one entry per AI pass between the rounds as the commit messages of
  `demo-paper/history/commits.md` name them (Claude Code on July 23 to 25 and August 15; Codex, model GPT-6-Astra, for
  the GPTedit passes of August 12 to 14), confirmed in the author's statement of 2026-10-28; and the record-keeping
  done on this draft, including the claims-list correction.

**What building round 1 made visible** (the record keeper's notes, not the author's statements; each is a candidate
finding, left for the checks):

- Round 1's `materials/lab.py` evaluates Definition 7.3 (retained-record leverage) in full and reproduces every number
  appendix B states except one: in the persistence instance appendix B says firm 2 sits in dissonance with $B_2 > 0$,
  while the definition on firm 2's full retained record gives $B_2 = 0$.
- Round 1's Proposition 5.5 is proved "immediate from Lemma 5.2", whose genericity hypothesis the proposition does not
  state; the checks found the same in claim C5.

**What the first record was.** Before 2026-10-27 this folder held the `-10` draft as a first submission, checked under
protocol formal-0.2 and returned for corrections. That history is superseded by the real one and is kept outside the
repository.
