# questions-before-priors · Ryall, *Questions Before Priors*, as a research record

The first real paper through Mark 1: a single-authored theory paper on how an actor whose causal language has
failed comes to possess a new one. Finite states and partitions, e-processes and Ville's inequality, theorems with
proofs: none of it is an optimization the toy record's checks were built around, which is why this record exists.

**Source.** `tbv_mdr_GPTedit-10.tex` and `MDR_TBV_Paper01.bib` from the repository Kalanoski dropped in
`prototype/_drop/2026_TBV_Paper-1-master/` on 2026-10-21. The repository's own notes name `-09` as the sole
authoritative manuscript (48 pages, formal architecture frozen) and `-10` as a working restructuring in which section
2, "The problem in miniature", is still to be written by the author. The record is built on `-10` because that is the
file in the drop; its section 2 is empty, as in the source. It is a demonstration input, not the author's submission.

**How it was built, and by whom.** Nothing here has yet been seen by Michael Ryall.

- `paper/` and `appendix/`: `mark1 import-tex ... --choices sec:commitments --does-not-claim
  limitations-and-the-research-program`. Headings carry the TeX labels as ids; mathematics is as written; citations
  come from the .bib; three TikZ figures are dropped with their captions kept; six TeX comment lines are dropped. Two
  in-text citations, Esponda and Pouzo (2016) and Ortoleva (2012), have no bib entry in the source and stay as plain
  text. The scope-and-choices section carries the paper's "Scope and modeling commitments" and "Limitations"
  passages verbatim.
- `materials/lab.py`: the four-state laboratory of Example 1 and appendix C as code, written by Claude Code, so the
  numbers the paper states can be re-executed. One thing it makes visible: of 15 partitions of the four states, 10
  separate the two labelled states and 4 are minimal; the paper's "eleven are ruled out" is 15 minus 4.
- `provenance/derivations.yaml`: closed-form entries for the stated numbers and `kind: proof` entries for the theorems
  (protocol formal-0.2), written by Claude Code from the proofs. A reading of the author's proofs, not the author's
  own statement of them.
- `provenance/ai-use.yaml`: drafted from the repository's `AGENTS.md`, `notes/STATUS.md` and file names; marked
  "to be confirmed by the author" throughout.
- `ai-appendix/`: produced by the published generator, from the above, when the author-side check first runs.

**Two things the machine caught while the record was being built.** A deterministic-only run made along the way,
`self-check/20261021-072206-author-c56640a/`, found that the provenance used `n` for the number of tokens in one
derivation and the number of agents in another (standard S5, one sense per symbol); the tokens became `r` before
the full run. And the first full run's three generator answers each reported, as text addressed to a model, a
sentence the converter had put at the head of the scope-and-choices section ("the generator carries them on
verbatim..."). The sentence was Mark 1's, not the author's; the converter now writes a neutral one, and that run
was discarded with its answers. The run that counts is the one after it.

**The author's run, and what it got wrong.** `self-check/20261021-074338-author-c6e282f/` is the self-check
submitted with the record: 58 findings under checks 0.2.0. Seven of its eight soundness findings are errors of Mark
1's proof check, not of the paper: three "rests on itself" loops that came from reading a result's location off the
claims' pointers, and four "hypothesis not mentioned" findings that matched the proofs' hypotheses word for word
against claims that paraphrase them (`CHANGES-from-design.md`, item 27). The check was corrected after the run and
published as checks 0.2.1. The run is kept as it was: a findings report is not edited after the fact, and it cannot
be replayed under the corrected code because it generated the AI appendix the record now carries.

**What happened next.** Submitted as round 1 with that run. The journal's run, under checks 0.2.1, returned the record
for corrections: [`3-editor/questions-before-priors/`](../../3-editor/questions-before-priors/), and the root README,
"The first real paper". Only the author can make the corrections, so nothing here has changed since. On 2026-10-22 the published
checks moved to 0.3.0 (re-execution under perturbation), and `self-check/20261022-174432-author-32a78c4/` is
the author-side re-run of the deterministic checks on the unchanged record. The round-1 view of who made each
part, `3-editor/questions-before-priors/diffs/r0-r1.md`, shows that `ai-use.yaml` declares the LaTeX
conversion and the earlier editing on `paper/paper.md` only; `appendix/appendix.md`, `record.yaml` and
`declarations.yaml` are not covered by any entry, though AI touched them. That is a correction for round 2.

**What stays behind in `_drop/`.** The GPT machine reviews, the author's planning notes, and the copyrighted PDFs in
`literature/`. They are not part of the record and are not published.
