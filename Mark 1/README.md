# Mark 1 · the journal after AI, on one formal paper

The system in the v7dk deck ([`../figures/`](../figures/): the deck and the figures exported from it), built for
the formal-theory modality and run end to end, with the authors standing in for the journal. A paper arrives as a
research
record; the machine emits findings and never a verdict; named people take every decision and sign it; the
journal issues a certificate and a publication together, or nothing.

Everything is a file you can open. Documents are Markdown, and each has an `.rtf` twin in Times New Roman 12
for anyone who reads in Word; the `.md` is the source, and `mark1 rtf` regenerates the twins. The folders
follow the paper's path, one per party:

```
1-journal/     what the journal publishes before any paper arrives: protocol, checks, standard,
               mapping, interest criteria, and the corpus the evidence map searches
2-author/      what the author sends: one research record per paper, with its self-check and submission
3-editor/      what the editor gets and signs: each journal run (findings report, SIEVE analysis,
               comparison with the author's run, decision), the review history, rounds, returns,
               "new", interest; statistics/ across papers
4-reviewers/   what reviewers see (the packet) and send back (reports)
5-published/   the certificate and the publication, issued together or not at all
machine/       the code: one Python package, one command, `mark1`
tests/         106 tests; model answers canned in tests/answers/
evaluation/    planted defects in copies of the record and their detection; pilot/ for the teaching-note pilot
```

## The figure, box by box

| Box | In the deck | Where it lives | State |
|---|---|---|---|
| J1 | Publishes in advance: protocol, checks, standard, mapping, interest criteria | [`1-journal/`](1-journal/) | built (formal); other modalities specified |
| A1 | The author works however they like | — (`mark1 import-tex` helps a LaTeX paper into the record's form) | |
| A2 | The research record | [`2-author/<paper>/`](2-author/) | built |
| A3 | Self-check: the author runs the same generator and checks first | `2-author/<paper>/self-check/<run>/` | built |
| A4 | Submission, every round | `mark1 submit` → `3-editor/<paper>/rounds/r<n>/` | built |
| M0 | The reference generator: an AI appendix for a submission that arrives without one | [`machine/generator.py`](machine/generator.py) | built; the AI appendix is the author's (A2, formal-0.3) |
| M1 | Level 1 · Form, the paper's front notice included | [`machine/checks/form.py`](machine/checks/form.py) | built |
| M2 | Checks differ by modality | [`machine/modality.py`](machine/modality.py) | built; formal only |
| M3 | Level 2 · Correspondence: (a) completeness, (b) resolution, (c) anchors | [`machine/checks/`](machine/checks/) | built; (d) derivation withdrawn in formal-0.3 (A4) |
| M4 | Level 3 · Warrant (SIEVE) | [`machine/sieve/`](machine/sieve/) | contribution, formal soundness and re-execution under perturbation built; four modules specified |
| M5 | Findings report | `3-editor/<paper>/intake/<run>/findings.md` | built |
| M6 | Evidence map | `3-editor/<paper>/intake/<run>/sieve/evidence-map.md`; the corpus it searches is [`1-journal/corpus/`](1-journal/corpus/) | built; venues (UTD24, FT50, CABS 4*/4) searched through OpenAlex |
| H1 / D2 / H2 | Editor applies the mapping; departs or not; standard action signed, every round (A5) | `mark1 intake` → `3-editor/<paper>/intake/<run>/decision.md` | built |
| A5 / T1 | Back to the author: corrections at intake, or revise and resubmit after review | `3-editor/<paper>/returns/`; `mark1 revise` | built |
| H5 | New, signed, after the author answers the map once | `mark1 answer`, `mark1 new` → `3-editor/<paper>/new.yaml`; a kind other than the map's, or another reading of the paper's question, is signed with a reason (item 41); `mark1 defer-new` lets review proceed with "new" still owed (item 38) | built |
| — | Review rounds; what reviewers get; the diff between rounds | `mark1 packet`, `mark1 report` → [`4-reviewers/<paper>/`](4-reviewers/); `mark1 diff` → `3-editor/<paper>/diffs/` | built |
| H3 | Interest, signed by the editor and two named reviewers | `mark1 interest` → `3-editor/<paper>/interest.yaml` | built |
| D3 | Publish and certify: both, or nothing | `mark1 issue` | built |
| J3 | Certificate | [`5-published/<paper>/certificate/`](5-published/) | built, issued with J4 |
| J4 | Publication | [`5-published/<paper>/publication/`](5-published/) | built |
| J2 | Review history: what changed, and who changed it, author or AI | `3-editor/<paper>/history.jsonl`; each submission records who made or changed each file, and the AI-use entries it declares, as the record declares it ([`machine/attribution.py`](machine/attribution.py)) | built |

Every place the build departs from the appendix draft or the system design is listed in
[`CHANGES-from-design.md`](CHANGES-from-design.md), with the items Ryall's answers of 2026-10-24 and 2026-10-26
settled marked resolved.

## What the demonstration shows

The paper is Ryall's *Questions Before Priors*, replayed through Mark 1 along its real history (Ryall, 2026-10-24):
the July 23 draft was reviewed by two machine reviewers and came back for revision; 29 commits later, the August 15
draft is the revision. The sources are in [`../demo-paper/`](../demo-paper/). Every human step is signed by
Dimitrija Kalanoski, standing in for the journal and, where the author corrects the AI appendix, for the author. The
root README of this repository lists the steps in order, with the command behind each and the file it wrote.

Each round follows the design: the author runs the checks, corrects the AI appendix, and submits; the journal then
runs the same checks on what was submitted. The AI appendix was first produced with the reference generator, and its
claims list carried 23 claims in each round. The author's first run on round 1
([`20261027-114802-author-28648dd`](2-author/questions-before-priors/self-check/20261027-114802-author-28648dd/findings.md),
kept as the author's working run) found 55 things to correct: 44 statements of the paper the list did not carry and
11 claims whose evidence said only part of what they said. Those are the author's corrections to make before
submitting, and in both rounds they were made before the journal ran. The generator's stamp is left as it was, so
every report says, as a fact and not as a finding, that `ai-appendix/claims.yaml` was edited after generation.

Two published objects changed between the rounds, and every report carries its versions. Round 1 ran under protocol
formal-0.3, checks 0.6.0 and mapping 0.2. Round 2 ran under protocol formal-0.4, checks 0.7.0 and mapping 0.3
(CHANGES items 41 and 43): the contribution claim states the question it answers, in the paper's words, and the map
places the claim on that question; and evidence that carries only part of a claim travels to review with the finding,
instead of returning the paper.

### Round 1: the July 23 draft

- **The record** ([`rounds/r1/record/`](3-editor/questions-before-priors/rounds/r1/record/)), imported from
  `tbv_mdr_Paper01-v02.tex`, with its derivations, its laboratory as code, and an AI-use record confirmed by the
  author on 2026-10-28.
- **The author's correction**: the claims list grew from 23 to 66 claims: 43 added, one per statement the list did
  not carry, and 15 evidence pointers narrowed or widened to the spans that carry the claims.
- **The author's run on the corrected record**
  ([`20261028-232034-author-047023d`](2-author/questions-before-priors/self-check/20261028-232034-author-047023d/findings.md)):
  12 findings, all claims whose evidence carries only part of what they say. Completeness published nothing: its
  three answers agreed too little (0.38 against a minimum of 0.50), and the three statements two of them named are
  reported below tolerance.
- **The journal's check** ([`20261028-233241-journal-047023d`](3-editor/questions-before-priors/intake/20261028-233241-journal-047023d/findings.md)):
  16 findings, all on supporting claims, none on a main claim; no statement was named by two of the three
  completeness answers. Eleven of the 16 are the author's; five are the journal's alone, and one of the author's is
  not among them ([`diff-vs-author.md`](3-editor/questions-before-priors/intake/20261028-233241-journal-047023d/diff-vs-author.md)).
- **Intake**: the mapping says return for corrections whenever a claim's evidence is incomplete (R3); the editor
  departed to proceed to review, with the reason recorded
  ([`decision.md`](3-editor/questions-before-priors/intake/20261028-233241-journal-047023d/decision.md)). "New" was
  deferred, because round 1 was really reviewed with nothing signed as new (CHANGES item 38).
- **Review**: the two machine reviews of July 2026 are filed as the reports of two reviewers
  ([`4-reviewers/questions-before-priors/reports/`](4-reviewers/questions-before-priors/reports/)); both say revise,
  and the editor signed revise and resubmit
  ([`returns/r1-revise_and_resubmit.md`](3-editor/questions-before-priors/returns/r1-revise_and_resubmit.md)).

### Round 2: the August 15 draft

- **The record** ([`2-author/questions-before-priors/`](2-author/questions-before-priors/)), from
  `tbv_mdr_GPTedit-10.tex`; its AI-use record names one entry per AI pass in the 29 commits between the rounds, as
  the author confirmed them on 2026-10-28.
- **The author's correction**: the claims list grew from 23 to 86 claims, 63 added; claim C10's evidence pointer, which the
  generator had written malformed, now points at the paper's section on nonidentification; and the contribution
  claim C1 states the question it answers, in the paper's words and with a pointer to the lines that state it
  (`paper/paper.md:L14-L15`): how an actor whose causal language has failed comes to possess a new one, the step
  before a theory, or at least a hypothesis space, exists.
- **The author's runs**: the first, under checks 0.6.0 and before the question was stated
  ([`20261028-234924-author-466a39e`](2-author/questions-before-priors/self-check/20261028-234924-author-466a39e/findings.md)),
  published nothing: both model-judged checks fell below their agreement minimums. The run the author submitted on
  ([`20261029-041808-author-4909a9e`](2-author/questions-before-priors/self-check/20261029-041808-author-4909a9e/findings.md)):
  13 claims whose evidence carries only part of what they say, the contribution claim C1 among them. Completeness
  again published nothing (0.28); five statements are reported below tolerance.
- **The journal's check** ([`20261029-043822-journal-4909a9e`](3-editor/questions-before-priors/intake/20261029-043822-journal-4909a9e/findings.md)):
  11 findings, all claims whose evidence carries part of what they say: C1 and ten supporting claims. Every one of
  them is in the author's own report; two of the author's are not in the journal's
  ([`diff-vs-author.md`](3-editor/questions-before-priors/intake/20261029-043822-journal-4909a9e/diff-vs-author.md)).
  Completeness published nothing (0.43); 13 statements are reported below tolerance. No answering session reported
  injection.
- **The diff between rounds** ([`diffs/r1-r2.md`](3-editor/questions-before-priors/diffs/r1-r2.md)) attributes each
  changed file as the record declares it. Its 32 entries "declared late" are dated before round 1 was submitted to
  Mark 1, on 2026-10-28: the replay runs on today's clock.
- **Intake**: under mapping 0.3 the standard action is proceed to review (rule R9 on all eleven); the editor signed it
  with no departure, and the decision records that all eleven findings were in the author's report, acknowledged at
  submission ([`decision.md`](3-editor/questions-before-priors/intake/20261029-043822-journal-4909a9e/decision.md)).
  A revision goes back through intake, as Figs. 4 and 4b show (CHANGES item 39).

The paper stands at **awaiting "new", round 2**, where its real history ends. The demonstration stops here; the test
suite takes a copy of the record through "new", interest and issue (below).

What the runs say about the system rather than the paper:

- **The author's step carries most of the work.** Uncorrected, the generator's claims list gave the journal 57
  findings in round 1 and 70 in round 2; corrected by the author, 16 and 11. What remains is evidence spread over
  several sections, which no single evidence span carries: one evidence pointer per claim is the limit, not the paper,
  and for the contribution claim, whose evidence is the whole paper, it is a limit by construction.
- **A partial is the author's to stand behind.** Under mapping 0.2, rule R3 returned the paper for any claim whose
  evidence carried only part of it, so round 1's intake was a signed departure. Mapping 0.3 reports such evidence as
  its own class, `evidence_partial`, and sends it to review with the finding carried, marked when the author's own
  report already lists it: the author saw it and submitted. Round 2's intake was the standard action. Return stays
  for a pointer that does not resolve or evidence that says nothing.
- **The map proposes "answer" on the author's own question.** Round 1's map read the question for itself and placed
  the paper as an answer on a question Felin and Zenger (2009) pose. Round 2's map judged on the question as the
  paper states it and placed it the same way, 3 of 3, on Felin and Zenger alone; each answer named the reading that
  would make it a question, one that starts from a failed causal language. That reading is the editor's to sign,
  with a reason, when "new" is signed (`mark1 new --question-as-read`), and the departure is counted.
- **Completeness is the least stable check.** On lists of 66 and 86 claims, its three answers named different
  statements, and it fell below its minimum in every run (0.38, 0.00, 0.28, 0.43). Its findings are reported, not
  published; how it is asked is a question for the next version of the checks.
- **The front notice was first read as an injection.** Its first wording, addressed to "the reader that evaluates",
  was reported by all three completeness answers; the notice now states facts and addresses no one (CHANGES item 37).
  The runs made with the old wording were discarded and are kept outside Mark 1.

### The evidence map reads introductions

Each evidence map rests on the prior work's introductions where the journal holds or can fetch a copy (checks 0.4.0,
CHANGES item 32). Since checks 0.6.0 each nearest work is asked two questions, does it pose the question the
contribution claim answers and does it state the claim (item 40), and since checks 0.7.0 the question is the one the
paper states, carried in the claims list with its pointer and shown on the map (item 41). In round 2's journal run
([`evidence-map.md`](3-editor/questions-before-priors/intake/20261029-043822-journal-4909a9e/sieve/evidence-map.md)),
45 candidates were shown to the model; 20 were also read from their introduction, 14 from the journal's licensed
copies and 6 from open-access copies. All three answers place the contribution as an answer, a new claim on a
question already posed: Felin and Zenger (2009) pose the question as the paper states it (3 of 3); Karni and Vierø
(2013 and 2017), Ehrig and Schmidt (2022), Gavetti and Levinthal (2000) and Ryall (2003) do not; none of the six
states the claim. Round 1's map, which read the question for itself, placed the paper the same way, with Ehrig and
Schmidt posing the question in two answers of three.

The map's coverage statement names its limit: sixteen works the paper cites are not among the candidates, among them
the dynamic-unawareness papers in *Journal of Economic Theory* and *Economic Theory* that may be nearer than anything
on the map, and several *Strategy Science* papers, a venue outside the 150 searched. "An answer" holds against the
candidates, not against the literature. The licensed copies stay outside this repository; the
excerpts stay in each run's `sieve/introductions.json` and `bundles/`, and neither is published.

### Planted defects

[`evaluation/defects-questions-before-priors.md`](evaluation/defects-questions-before-priors.md) plants seven defects in
copies of the record: a wrong comparative-static sign, a stated closed form that does not follow, one term in two
senses, a proof step resting on nothing, two proofs resting on each other, text addressed to the evaluating model, and
code right only at the anchor's horizon, which only perturbation can see. Each is judged against the record's own
findings (C10's pointer, twice), and each is found by the check it targets, with nothing else.

### The tests

The test suite runs on a copy of this record, with C10's pointer corrected so that the deterministic checks start
clean, and model answers canned in `tests/answers/`: the author's real generator answer, a real completeness answer
with its unmatched statements removed, and short synthetic answers for resolution and the map. It takes the copy along
the whole path: intake, "new", review, revise and resubmit, a second round back through intake with its diff,
interest signed by three named people, and the certificate and publication issued together; and a second path in
which "new" is deferred in round 1 and still owed after round 2's intake (`tests/test_journey.py`). No real paper has
gone that far.

## Run it

Three ways, in the order an editor would try them. Each needs Python 3.12 or later: no account and no key, and after
the one-time install no network for the first two.

**Set up once**, from this folder (`Mark 1`), in a terminal:

Windows (PowerShell):

```
py -3.12 -m venv .venv
.venv\Scripts\python -m pip install -e ".[test]"
.venv\Scripts\Activate.ps1
```

If PowerShell refuses to run `Activate.ps1`, use `cmd` instead and run `.venv\Scripts\activate.bat`.

macOS and Linux:

```
python3 -m venv .venv
.venv/bin/python -m pip install -e ".[test]"
source .venv/bin/activate
```

After that the commands are the same everywhere. `mark1 status questions-before-priors` says where the paper
stands and what comes next.

### 1. Replay, no key

Re-runs a finished run from the model answers stored with it, calls no AI, and reports every difference from the
original run; zero differences means the report is reproduced. If the check code changed after the run, replay says
so and gives both hashes; that is not a difference in the findings:

```
mark1 replay 20261029-043822-journal-4909a9e
```

Replay writes its copy beside the original, as `<run-id>-replay`. **From a fresh clone it says the answers are not
here and stops.** The stored answers live in each run's `bundles/` folder and the introduction excerpts in
`sieve/introductions.json`, and neither is in the repository, because the evidence map's prompts carry other
people's text; the submission copy leaves the map's candidate list (`sieve/candidates.json`) out with them. On the
machine where the runs were answered, round 2's author and journal runs reproduce exactly (2026-10-29, and again
on 2026-10-30 under the corrected code, with the code change noted); with only the completeness and resolution
answers, replay stops at the evidence map and names the three prompts whose answers are missing; without the
excerpts the map's stored answers are refused, because the prompt they answer has changed;
and round 1's runs, made under checks 0.6.0, replay to a report that differs in its versions and class names. From a
clone, what replays is the test suite's own run (`tests/test_journey.py`, part of `python -m pytest -q`).

### 2. Deterministic only, no key

Runs the code-only checks live on the record: form and pointers, the record's code re-executed against its anchors
and under perturbation, and the soundness of its stated derivations:

```
mark1 check questions-before-priors --deterministic-only
```

The findings report is written to `2-author/questions-before-priors/self-check/<run-id>/findings.md`; the command
prints the path. The tests run the same way, on a copy of the record (about 13 minutes):

```
python -m pytest -q
```

### 3. The model-judged checks, answered from your own chat subscription

A full run stops at each model-judged check and writes a prompt for it, three repetitions per check:

```
mark1 check questions-before-priors
```

It prints the run id and the path to `PENDING.md`, which lists every `prompt.md` waiting; `mark1 bundles` lists them
again at any time. For each one, open a **new** chat (any model; one chat per prompt, so the three repetitions stay
independent), attach or paste the whole `prompt.md`, and save the JSON object the model returns as `response.json`
in the same folder as that `prompt.md`. The brief every answer follows, and what to tell the model, is
[`machine/llm/HOW-TO-ANSWER.md`](machine/llm/HOW-TO-ANSWER.md). When every prompt has its answer:

```
mark1 check --resume <run-id>
```

An answer that fails its schema, carries the wrong nonce or names the wrong check is refused with the reason, and the
run waits until it is fixed. The journal's run is the same with `--actor journal`, after `mark1 submit`.

### What is not here

Every run's `bundles/` and `sieve/introductions.json` carry other people's text, and every run's
`sieve/candidates.json` carries publishers' abstracts; none of the three is in this repository, and `.gitignore`
keeps them out. The record is Ryall's own paper, and the round-1 reports are the machine reviews from his
repository ([`../demo-paper/`](../demo-paper/)). There is no simulation after round 2: the demonstration stops at
round 2's intake, and the tests take a copy of the record the rest of the way.
