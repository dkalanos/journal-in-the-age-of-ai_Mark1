# 3-editor/ · what the editor gets, and signs

One folder per paper: the journal's file on it, from the first submission to the certificate or the return. It
stays with the journal and travels to another journal only at the author's request (appendix D.7).
`statistics/` sits beside the papers.

## The journal's runs: `<paper>/intake/<run-id>/`

Where the machine's work (M0 to M6) meets the named editor (H1, D2, H2). Run with
`mark1 check <paper> --actor journal`; decide with `mark1 intake <paper> <run-id> --signed-by NAME`. Read in
this order:

| File | What it is |
|---|---|
| `findings.md`, `findings.json` | The findings report (M5): findings only, each with a pointer into the record and into the standard, the versions and the models. Findings the author's own run lacks are marked. |
| `sieve/` | The SIEVE analysis: `evidence-map.md` and `.json` (M6), and `warrant.md`, the Level 3 findings on their own. |
| `diff-vs-author.md` | The journal's run against the author's, in both directions (appendix D.2). |
| `decision.yaml`, `decision.md` | The intake decision: the standard action under the published mapping, the rules that fired, the action taken, any departure with its reason, and the editor's signature. |
| `bundles/` | Every model-judged question as it was asked and answered: prompt, answer, reasoning, for each of the k repetitions. The audit trail; not needed to decide. |
| `ai-appendix/` | Present only when the submission had none and the journal generated it (M0). |
| `run.json` | How the run was started, so it can be resumed or replayed. |

## The rest of the file: `<paper>/`

| Path | What it is |
|---|---|
| `history.jsonl` | J2. Append-only log of every event: submitted, checked, decided, answered, new signed, packet built, reports, interest signed, issued or refused. Where a paper stands is derived from it (`mark1 status <paper>`). |
| `rounds/r<n>/` | Each submission as the journal received it: the record, the author's findings report, and `submission.yaml`. `changed-by.yaml`: every file changed since the last round (in round 1, every file) and who changed it, author or AI, with the basis for saying so, and the AI-use entries the round declares; the `submitted` event in `history.jsonl` carries the same, file by file. |
| `diffs/r<a>-r<b>.md` | What changed between two rounds, who changed it, and the AI-use entries declared, claims first, so no one re-reads what did not change. `r0-r1.md` is what round 1 brought and who made each part (`mark1 diff <paper> 0 1`). |
| `returns/` | Return notes to the author (A5, T1): for corrections at intake, or revise and resubmit after review with the round's reports (`mark1 revise`). Private communications, never public objects. |
| `author-answer.md` | The author's one answer to the evidence map, before "new" is signed. |
| `new.yaml` | H5: one editor's signed judgment of what is new, on the evidence map. |
| `interest.yaml` | H3: the editor's and two named reviewers' signed judgment of interest. |

What reviewers see is in `../4-reviewers/`; what the journal issues is in `../5-published/`.

## `statistics/`

Departure statistics by editor (`mark1 departures`): how often each departs from the standard action, and
which way.
