# The social science journal in the age of AI

Dimitrija Kalanoski, Michael D. Ryall, and Yannick Thams

This repository supports our Stage 1 proposal for the *Organization Science* special issue on AI-enabled frontiers.

Our main argument is that academic journals have traditionally been built around written manuscripts, but AI now
makes it possible to rethink how research is submitted, reviewed and published.

In the technical appendix, we explain our proposed approach in detail, while the repository demonstrates how it works
in practice. It includes a working prototype called Mark 1 and shows how we used it to process two versions of a real
research paper.

## The main idea

Instead of submitting only a manuscript, authors submit a complete research package. This includes the paper, its
appendix, supporting materials, a record of how AI was used in making it, and a short machine-readable list of what
the paper claims and the evidence supporting each claim.

The journal clearly explains its checks, its standards and its decision rules in advance. The checks are then run on
the submitted materials. Most of these checks are ordinary software, and some of them use an AI model. None of them
makes the publication decision. A human editor reviews the findings, applies the journal's rules, and makes the final
decision. If the editor chooses not to follow the standard rule, the reason must be documented.

Authors can run the same checks and correct any issues before submitting their work. Some findings may remain, for
example when the evidence supports only part of a claim. If the author has seen these findings and decides to submit
anyway, they are shared with the reviewers together with the paper. Other findings are treated differently. If a
claim points to evidence that cannot be found, the paper is returned to the author for correction. If a finding goes
against the journal's standard, the paper cannot be published. If the paper is accepted, the journal publishes both
the paper and a certificate explaining what was checked.

The main goal is to make the publication process more transparent, consistent, and accountable. Every step is
documented, and the records are available in this repository.

## Testing the system with a real paper

We tested Mark 1 using *Questions Before Priors*, a formal theory paper written by Michael D. Ryall.

The paper went through two rounds of review in 2026. The first draft was reviewed by two machine reviewers in
July, and the author revised it over 29 commits into a second draft in August. We processed both versions through
Mark 1 in the same order.

During this test, Dimitrija Kalanoski acted as the journal editor and also handled corrections to the structured
claims list on behalf of the author.

### Round 1: July 2026

The author's initial check identified 55 problems with the automatically generated list of claims: 44 statements
made in the paper that the list did not include, and 11 claims whose cited evidence supported only part of what
they said. These were corrected before submission, and the list grew from 23 to 66 claims.

The journal's check then identified 16 findings. In each case, the evidence supported only part of a claim. None of
these findings involved the paper's main results.

Under the journal's rules at that time, the paper should have been returned for corrections. However, the editor
decided to move it forward to review and documented the reason for making an exception. The two machine reviews
from July were included as the reviewers' reports, and the editor signed revise and resubmit.

### Round 2: August 2026

The revised paper was submitted with a declaration of each use of AI in the 29 commits between the drafts, and with
the list of claims expanded to 86. The list now also stated, in the paper's own words, the question that the paper's
main contribution answers. The author's own check found 13 findings. The journal's check identified 11, all of which
had already been identified in the author's own report, and every numerical result that could be re-run at other
parameter values held.

The journal's rules had also been updated based on what we learned in round 1. Under the revised rules, the paper
could proceed to review without an exception. The editor approved that decision.

The system also examined how the paper's contribution is related to existing research. It was asked three times,
independently, and each time it concluded that the paper answers a question raised by Felin and Zenger in 2009.
However, the author interprets that question more narrowly. In our process, it is the editor who decides which
interpretation to accept and documents the reason. This shows why human judgement is still important, especially when
deciding whether a paper makes a new contribution.

This is where the test ends, matching the point reached in the paper's actual review history.

## Lessons learned and what still needs work

Our tests also point to three aspects of Mark 1 worth clarifying. First, the system's completeness check, which looks
for results mentioned in the paper but missing from the list of claims, did not produce sufficiently consistent
results to report its findings in this demonstration. Second, the evidence map was based on 45 papers from the venues
searched, rather than the broader literature; the paper's home field, *Strategy Science*, is on none of the three
journal lists the map uses. Third, the two machine reviewers spent their effort on verifying the theorems, which our
design assigns to the checks, and they found problems in the proofs that the checks did not flag. This is the present
measure of how much of a reviewer's work the checks take over, and Stage 2 is designed to measure whether it moves.
All three points are documented in the appendix to clarify the current scope of the system, rather than to raise
concerns about the paper used in these tests.

Two further tests are in the repository. Seven copies of the package each carry one planted defect, and each was
found by the check that targets it and by nothing else. Of seven prior works the paper cites in journals the map
searches, the map reached three.

## Ten minutes with it

If you want to see the results directly, these are the files to open, in this order. They are Markdown files, and
each has an `.rtf` twin beside it for anyone who prefers to read in Word.

1. [The journal's findings report on round 2](Mark%201/3-editor/questions-before-priors/intake/20261029-043822-journal-4909a9e/findings.md):
   what the checks found, with the level, class and location of each finding, and how far the three independent
   answers behind each model-judged finding agreed.
2. [The evidence map](Mark%201/3-editor/questions-before-priors/intake/20261029-043822-journal-4909a9e/sieve/evidence-map.md):
   the prior works the map found closest to the paper, whether each of them poses the paper's question and states
   its claim, and the kind of newness the map proposes.
3. [The editor's decision](Mark%201/3-editor/questions-before-priors/intake/20261029-043822-journal-4909a9e/decision.md):
   the rule applied, the action taken, and which findings the author had already acknowledged at submission.
4. [What changed between the rounds](Mark%201/3-editor/questions-before-priors/diffs/r1-r2.md): each changed file,
   and who changed it, the author or an AI tool, as the record declares it.
5. [The research package itself](Mark%201/2-author/questions-before-priors/), with the claims list in
   `ai-appendix/claims.yaml` and the AI-use record in `provenance/ai-use.yaml`.

## Run it yourself

There are three ways to run Mark 1, in the order an editor would try them. The first two need no model, no key and no
account, and after the one-time install they need no network. You need Python 3.12 or later.

1. **Replay.** `mark1 replay <run-id>` rebuilds a run's findings report, evidence map and decision from the model
   answers stored with it, and reports every difference from the original. The answers behind the two rounds are not
   included in this repository, because the prompts contain text from other people's papers. On a clone, replay says
   so and stops. What can be replayed from a clone is the test suite's own run:
   `python -m pytest -q tests/test_journey.py -k replay`.
2. **The deterministic checks, live.** `mark1 check questions-before-priors --deterministic-only` runs the code-only
   checks on the package: form and pointers, the package's code re-executed against its stated results and under
   perturbation, and the soundness of its stated derivations. It prints the path of the report it writes. The whole
   test suite runs the same way on a copy of the package: `python -m pytest -q`, 105 tests, about a quarter of an
   hour.
3. **The model-judged checks, from your own chat session.** `mark1 check questions-before-priors` writes one prompt
   per judgment, three per check, and stops. Answer each one in a new chat of your own, following
   [the brief](Mark%201/machine/llm/HOW-TO-ANSWER.md), save the answer beside the prompt, and run
   `mark1 check --resume <run-id>` to finish the run. An answer that fails its schema or carries the wrong nonce is
   refused, with the reason. This is how the two rounds were produced. It costs whatever your subscription costs; we
   ship no key.

**Set up once**, in a terminal at the root of a clone. Windows (PowerShell):

```
cd "Mark 1"
py -3.12 -m venv .venv
.venv\Scripts\python -m pip install -e ".[test]"
.venv\Scripts\Activate.ps1
```

If PowerShell refuses to run `Activate.ps1`, use `cmd` instead and run `.venv\Scripts\activate.bat`. macOS and Linux:

```
cd "Mark 1"
python3 -m venv .venv
.venv/bin/python -m pip install -e ".[test]"
source .venv/bin/activate
```

After that the commands are the same everywhere, run from the `Mark 1` folder. `mark1 status questions-before-priors`
says where the paper stands and what comes next. The details of each way are in
[`Mark 1/README.md`](Mark%201/README.md), under "Run it".

## What is here

| Folder | What it holds |
|---|---|
| [`Mark 1/`](Mark%201/) | the prototype. What the journal publishes before any paper arrives (protocol, checks, standard, mapping, interest criteria) in `1-journal/`; the code in `machine/`, one Python package and one command, `mark1`; the research package of *Questions Before Priors* with both rounds; the journal's runs and signed decisions; the reviewers' reports; the diff between rounds; the unit tests; and the planted-defect and recall evaluations |
| [`demo-paper/`](demo-paper/) | the source material: the round-1 draft of July 23, 2026, the two machine reviews of it, the commit log and patches between the drafts, and the round-2 draft of August 15 |
| [`figures/`](figures/) | the figures of the appendix (legend, Figs. 1 to 4b, PNG and PDF), the deck they are exported from, and the scripts that build and export it |

[`Mark 1/README.md`](Mark%201/README.md) is the full account: the system box by box against the figures, what the
demonstration shows, and the three ways to run it. [`Mark 1/CHANGES-from-design.md`](Mark%201/CHANGES-from-design.md)
lists every place where the build departs from the appendix or the design, with the reason.

## What is not here

The repository contains no working notes, no correspondence, no stored model answers, and no material licensed from
anyone else. The answers behind the two rounds, the introductions the evidence map read, and the candidates' abstracts
are left out because they contain text from other people's papers, and `.gitignore` keeps them out of any clone. The
package is Ryall's own paper, and the round-1 reports are the machine reviews from his repository. There is no simulation
after round 2. The demonstration stops where the paper's actual history stops, and the test suite takes a copy of the
package through the remaining steps: "new", interest, and the certificate issued together with the publication.

## The demonstration, step by step

For the reader who wants every file. Paths are under `Mark 1/`; `P` stands for `questions-before-priors`.

| Step | Command | What it wrote |
|---|---|---|
| **Round 1, the July 23 draft** | | |
| The author's self-check on the corrected package | `mark1 check P`, the nine prompts answered, `mark1 check --resume <run>` | `2-author/P/self-check/20261028-232034-author-047023d/findings.md` (12 findings); the earlier run `20261027-114802-author-28648dd` is the author's working run on the uncorrected list (55) |
| Submission | `mark1 submit P` | `3-editor/P/rounds/r1/`: the package, the author's report, `changed-by.yaml`, `submission.yaml` |
| The journal's check | `mark1 check P --actor journal`, answered, resumed | `3-editor/P/intake/20261028-233241-journal-047023d/`: `findings.md` (16), `diff-vs-author.md`, `sieve/evidence-map.md`, `sieve/warrant.md`, `sieve/perturbation.md` |
| Intake | `mark1 intake P <run> --signed-by <editor> --action proceed_to_review --reason <text>` | `.../20261028-233241-journal-047023d/decision.md`: standard action return for corrections (mapping 0.2, rule R3); a signed departure to proceed |
| "New" deferred | `mark1 defer-new P --signed-by <editor> --reason <text>` | an event in `3-editor/P/history.jsonl`; review proceeds with "new" still owed |
| The reviewers' packet | `mark1 packet P` | `4-reviewers/P/packet/` |
| The reports | `mark1 report P --reviewer <name> <file>`, twice | `4-reviewers/P/reports/r1-machine-reviewer-1-chatgpt-july-2026.md` and `...-2-...md`, the two machine reviews of July 2026 |
| Revise and resubmit | `mark1 revise P --signed-by <editor> --reason <text>` | `3-editor/P/returns/r1-revise_and_resubmit.md` |
| **Round 2, the August 15 draft** | | |
| The author's self-check on the corrected package | `mark1 check P`, answered, resumed | `2-author/P/self-check/20261029-041808-author-4909a9e/findings.md` (13); `20261028-234924-author-466a39e` is the author's first run, before the contribution claim stated its question |
| Submission | `mark1 submit P` | `3-editor/P/rounds/r2/` |
| The journal's check | `mark1 check P --actor journal`, answered, resumed | `3-editor/P/intake/20261029-043822-journal-4909a9e/`: `findings.md` (11, every one in the author's report), `diff-vs-author.md`, `sieve/evidence-map.md` |
| Intake | `mark1 intake P <run> --signed-by <editor>` | `.../20261029-043822-journal-4909a9e/decision.md`: standard action proceed to review (mapping 0.3, rule R9), no departure |
| The diff between rounds | `mark1 diff P 1 2` | `3-editor/P/diffs/r1-r2.md` |
| Departure statistics | `mark1 departures` | `3-editor/statistics/departures.md` |
| Where the paper stands | `mark1 status P` | awaiting "new", round 2 |

The two rounds ran under different published versions, and every report names the ones it ran under: round 1 under
protocol formal-0.3, checks 0.6.0 and mapping 0.2; round 2 under formal-0.4, checks 0.7.0 and mapping 0.3, the
changes round 1 forced (`Mark 1/CHANGES-from-design.md`, items 41 to 43).
