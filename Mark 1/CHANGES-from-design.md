# Where Mark 1 departs from the design

Each line says what the code does, what the design text says, and why. The design texts are
`proposal/stage1/appendix-draft.md` (cited by section), `notebook/vision/system-design.md` (cited by Q), and the
v4dk deck. Items marked **v4** followed Kalanoski's 2026-10-20 proposals; Ryall answered them on 2026-10-24
(A1–A5), and each says how it was resolved. Items 35–37 carry the changes, as protocol formal-0.3.

## The paper and the AI appendix

1. **v4. Three layers, and the AI appendix is generated.** The paper, the appendix and a generated AI appendix
   (protocol P1–P3). The appendix C.2 and Q4 have two layers. To undo: submit hand-written AI appendices and drop
   check (d) from `machine/modality.py`. **Resolved 2026-10-24:** three layers accepted (A1); the AI appendix is
   the author's, in the published form, not generated (A2); see 35.
2. **v4. The AI appendix has six parts, not seven.** Declarations live once, in `declarations.yaml` (C.2 lists
   them as part 7). Avoids two copies of the same facts drifting apart. **Stands** under A2.
3. **v4. Generator M0 is built**, with a generate-if-absent fallback on the journal side (I.3 does not list it).
   Parts 4 and 6 are carried verbatim from the appendix's scope-and-choices section, never generated. Of k
   generations, the one closest to the others becomes the AI appendix; their agreement goes on the stamp. **Resolved:** the generator stays, as the reference
   implementation of P3 and the journal's fallback (A2).
4. **v4. Level 2 has a fourth check, (d) derivation**, with a new finding class `derivation` (D.5 lists nine
   classes; Mark 1 has ten). It has a deterministic half (the AI appendix against its generator stamp, by
   hash) and a model half (regenerate k times and compare claim sets). D.1 names two deterministic operations;
   the stamp comparison is a third. **Resolved:** withdrawn in formal-0.3 (A4); see 36.

## Findings

5. **Four fields added to the D.5 finding:** `rationale`, `prompt_id`, `agreement` and `absent_from_author`.
   The editor in the red team noted that a warrant finding could be located but not audited as reasoning; the
   rationale and the prompt id answer that.
6. **Deterministic findings carry `model: deterministic`** and the hash of the check code as `model_version`
   (D.5 requires both fields on every finding).
7. **Injection findings are class `injection`**, as D.5, C.4 and Q5 say, not `nonconformance` as red-team fix
   #8 proposed. They are reported at level 1, since the class is cross-level and the schema needs a level.
8. **Resolution (2b) is partly deterministic.** A pointer that does not resolve is found without a model; D.3
   calls the whole of resolution a model judgment.
9. **Below-tolerance findings are reported separately**, not dropped: a check whose agreement falls below its
   minimum is "not published as a check" (D.1), and its findings move to `below_tolerance` in the report.
10. **No pointer, no flag is enforced on model answers:** a model finding whose pointer does not resolve in the
    record is discarded before the report is written.

## The mapping

11. **Two rows added to F.1.** `derivation` is treated like the other Level 2 classes (return for corrections;
    counts toward the two passes; that row went with check (d) in mapping 0.2). `established_by_prior` proceeds at intake, because the "new" judgment on
    the map belongs to H5, not to intake.
12. **When several rows fire, the most severe action wins**, in the order written in `1-journal/mapping.yaml`.
    F.1 does not say. Every fired rule is recorded on the decision.
13. **A pass is a prior "return for corrections" on the same paper**, counted from the review history.

## The steps people take

14. **Review history, "new", interest, the certificate and the publication are built** (I.3 and I.5 list them
    as specified, and the diff between rounds as a stretch goal). The deck's fill is left as Ryall drew it.
15. **v4. The journal issues a publication and a certificate together, or nothing** (G.1 issues the
    certificate alone). The two are staged and moved into place together; if the second move fails the first
    is undone. To undo: have `workflow.issue` write the certificate only. **Resolved:** accepted (A5).
16. **Reviewers receive the paper and the appendix**, as the v4 deck says, with the findings report and the
    map. F.3 says the narrative.
17. **Submissions are snapshot copies** under `3-editor/<paper>/rounds/r<n>/`, and the diff between rounds is
    computed from them. The plan used git tags; copies need no git and keep the journal's witness separate
    from the author's working history.
18. **Signatures are a name, a time and the hashes of what was signed.** They record what was signed; they are
    not cryptographic.

## Level 3

19. **The formal soundness module is built as a deterministic slice** (I.5 lists modality soundness as not
    built). Whether a prose step follows stays specified.
20. **The evidence map places contribution claims only**, with the main results given to the model as
    context. D.6 speaks of "the paper's contribution claim".
21. **`uncovered` is chosen by the model as a newness kind** and becomes a finding of that class.
22. **The corpus is the journal's venues, searched per paper through OpenAlex, plus an optional hand list.**
    D.6 says "the corpus the journal has access to"; I.3 planned a small named corpus for Stage 1, and the first
    demonstration ran on one. Kalanoski asked (2026-10-21) for a realistic test, so `1-journal/corpus/venues.yaml`
    names UTD24, FT50 and CABS 4*/4, and retrieval is keyword search of those venues followed by the works most
    cited among the hits (`machine/retrieval.py`). Coverage is stated as what was searched, with the queries and
    candidates kept per run. The check set is version 0.2.0; runs made under 0.1.0 replay against the hand list
    their answers cite. The hand list stays for work the venues do not reach; its summaries were written by Claude
    Code and need a coauthor's check.
23. **Placements can rest on a title alone, and say so.** Older antecedents often have no abstract anywhere
    (Bulow and Pfleiderer 1983 has none in OpenAlex, Semantic Scholar or Crossref). Each nearest entry carries a
    `basis`: `abstract`, `summary`, or `title_and_known_work`, the last meaning the model relied on the title and
    what it knows of the work. The editor sees the basis; the coverage statement counts abstract-less candidates.
    D.6 did not foresee this; the alternative was a map that could never say "not new" of a result older than the
    abstracting services.

## Not built

24. **The repository conforming to its own protocol** (I.3). It needs a decision about what the project
    repository's record is; running Level 1 on a manifest for this folder would be cheap once that is decided.
25. **Formal certificates say data verification "not applicable"**; the as-declared and externally-verified
    lines of G.1 belong to the empirical modality.
26. **The publication's DOI is a placeholder**, `10.5555/mark1.<paper>`, flagged `minted: false`.

## Protocol formal-0.2 (2026-10-21, for the first real paper)

27. **Provenance has a second shape, the proof.** P6 and the synthetic record were built for closed-form derivations:
    objective, solution, comparative statics, examples, all re-derived in sympy. Ryall's *Questions Before Priors*
    is a theorem-proof paper on finite partitions and e-processes; none of its results is an optimization the
    machine can re-solve. A derivation of `kind: proof` states hypotheses, steps and what each step rests on; the
    soundness slice checks that every pointer resolves and that no result rests on itself (standard S8). Whether a
    step follows stays a model judgment, not built. Records written under formal-0.1 validate unchanged.
    The first run on the paper (2026-10-21) produced eight soundness findings, and on reading them seven were the
    check's own errors. Three "rests on itself" findings came from reading a result's location off the claims'
    pointers: the generator pointed some claims at the paper's summary of an appendix result, which is what the
    proof rests on. Locations now come only from each derivation's `states`. Five "hypothesis not mentioned"
    findings came from matching the proof's hypotheses word for word against claims that paraphrase them; four
    were wrong. That reading now belongs to the resolution check, whose three answers had already flagged the one
    real case (Proposition D.5 stated without two of its hypotheses) with reasons. The corrected check is published
    as checks 0.2.1, so a report made under 0.2.0 says which check made it.
28. **`mark1 import-tex` turns a LaTeX paper into the protocol's Markdown.** Headings, theorem environments,
    labelled paragraphs and proofs become headings with ids; mathematics is kept as written; citations come from
    the .bib; drawings are dropped with their captions kept; the scope-and-choices section is assembled from
    passages the author names. It is an author's helper, outside the published objects; the author reads and
    edits what it writes.

## Review history (2026-10-21)

29. **The review history says who changed what as the record declares it, not as it happened.** Box J2 promises
    that the journal records "what changed and who changed it, author or AI". Mark 1 attributes each file changed
    between rounds from the two sources the record has: AI-use entries added that round and the files they touch,
    and the generator stamp. Each attribution names its basis. A file AI drafted in an earlier round but changed
    now with nothing declared is marked "not declared this round" rather than given to the author. A declaration
    that appears for the first time dated before the previous submission is flagged as declared late. The
    alternative, attributing from the working history's commits, needs a working history the author chose to
    submit; it is not built. Kalanoski asked for this on 2026-10-21.
30. **Each round lists the AI-use entries it declares, and round 1 is attributed too** (2026-10-22, at
    Kalanoski's request). The diff between rounds names every entry first made in the later round, and
    `mark1 diff <paper> 0 1` reads the first submission against nothing: who made each file. Submission writes
    `changed-by.yaml` for every round, round 1 included.

## Level 3 · re-execution under perturbation (2026-10-22)

31. **Re-execution under perturbation is built for the formal modality, as standard S9** (formal-0.3,
    checks 0.3.0). The deck draws it as the third leg of Level 3, "the robustness checks the standard
    names", and no Mark 1 standard named any. For a formal paper S9 names one: each reproduction anchor is
    re-run at other points the derivation's assumptions admit. The formula an anchor stands for is read off
    the derivation (any solution, quantity, stated closed form or comparative-static derivative that gives
    its value at its own point, with symbols it does not set taken from the derivation's examples), so the
    protocol and the generator are unchanged. Points are drawn within e^±1 of the anchor's values, integers
    kept integral, from a seed fixed per anchor so a replay draws the same ones. Results without an anchor
    are not perturbed; that is stated, not hidden. Kalanoski asked for this on 2026-10-21.
32. **The evidence map reads introductions where the journal holds a copy** (checks 0.4.0, 2026-10-22). An
    abstract compresses a contribution; the introduction states it and its gap. Up to 20 candidates are read from
    their introduction: first from the journal's own licensed copies (`licensed_copies` in venues.yaml), then
    from open-access copies OpenAlex knows of; a copy whose opening does not carry the work's title is refused
    (one repository filed a Colombian journal issue under Barney 1991). On Questions Before Priors the verdict
    did not move, but every placement came to rest on the prior work's own statement of its contribution, and the
    formal unawareness literature the first map missed came in. Open-access copies alone reached only weak
    candidates. The excerpts are other people's text: they stay in each run's `sieve/introductions.json` and
    `bundles/`, which replay needs and nothing published may carry. Kalanoski asked for this on 2026-10-22 and
    supplied 14 licensed copies for the demonstration. At Kalanoski's request every map in Mark 1 now rests on
    introductions: the live record's maps, made from abstracts on 2026-10-21, were remade from introductions on
    the same text and candidates, and the abstract-based ones moved to `_drop/`.
33. **Revise and resubmit after review is a signed step** (`mark1 revise`, 2026-10-22). The deck's A5/T1 sends a
    reviewed paper back for revision, each round a new submission against the same review history; Mark 1 could
    return a paper only at intake, and interest "no" closes it, which is a rejection. The simulation of
    Questions Before Priors found the gap: both reviewers said REVISE. The editor now signs revise and resubmit
    on the round's reports, the return note carries them, and the next submission is reviewed as round n + 1.
34. **The demonstration runs on one real paper; the synthetic record is gone** (2026-10-22, at Kalanoski's
    request). The tests run on a copy of Questions Before Priors with its one Level 1 finding corrected, with
    canned answers taken where possible from the paper's own stored answers. The planted defects are written
    against its text, and each copy is judged against the findings the unaltered record already has (a real
    record is rarely clean), measured on the unaltered copy. The recall test now asks for the seven works on
    awareness the paper cites in the venues searched: 3 of 7 came back.

## Protocol formal-0.3 (2026-10-27, to Ryall's answers of 2026-10-24)

35. **The AI appendix is the author's.** P3 now says what the author says to the machine, in the published form,
    with the generator as the reference implementation of that form and the journal's fallback when none arrives
    (A2). The code is unchanged: the generator, the fallback and the stamp stay as built; what changed is what the
    stamp means. P1 and P7 are reworded to match.
36. **Check (d) is withdrawn; the stamp is a fact on the report.** `checks/derivation.py` is gone, with the finding
    class `derivation`, its mapping row (mapping 0.2) and its tolerance. `generator.stamp_status` puts on every
    findings report whether the AI appendix still matches its stamp, which inputs changed and which outputs were
    edited since; it produces no finding (A4). Reports made under checks 0.4.0 and earlier carry derivation findings
    and say so by their version. Nothing demonstrated is lost: on the first paper the check's thirteen findings all
    came from one field the generator does not settle.
37. **The paper opens with a front notice** (A3): before its first section, a paragraph beginning `**AI appendix.**`
    that says an AI appendix exists and where it is. Level 1 flags its absence as `nonconformance` against P2
    (checks 0.5.0). `machine/notice.py` writes it. Its first wording described the AI appendix as "for the reader
    that evaluates"; on round 1's first self-check all three completeness answers reported that line as text
    addressed to them, the injection screen made it a finding, and the mapping would have returned the paper
    without review over a sentence Mark 1 wrote. The notice now states facts only, P2 says so, and that run is
    kept outside the repository (`_drop/discarded-2026-10-27/`) as the record of the catch. The existing record received it on 2026-10-27 and now declares
    protocol formal-0.3, which moved its abstract two lines down and changed its hash; the runs made before that
    date are of the record as it was, and the record's pointers, which name sections, were unaffected.
38. **"New" can be deferred past a review round** (`mark1 defer-new`). Fig. 4b and the design sign "new" after intake
    and before any review round; Mark 1 enforced that order. Ryall's demonstration (task sheet A6, B4) runs the paper's
    real history, in which round 1 went to two reviewers and back for revision with nothing signed as "new", and leaves
    "new" to the labelled simulation after round 2. The editor may now let review proceed with "new" still owed and the
    reason recorded in the review history; "new" is signed later, after the author's one answer to the map. The real
    history uses this once. Whether the figure changes or the real history is the exception is for the authors.
39. **A revision goes back through intake** (resolved 2026-10-27, toward the design). Figs. 4 and 4b (v5dk, box A5)
    send each revise-and-resubmit round through the journal's checks and the editor's signed intake decision; Mark 1
    had sent a revision straight back to review. Now a revised round stops at "checked" until an editor signs intake.
    "New" is signed once per paper: a later round that proceeds goes to review, or to "new" if it is still owed
    (item 38). Ryall's B5 ("submit, check, decide") asked for this decision; round 2 of *Questions Before Priors* has it.

## The four kinds of newness (2026-10-28, to Ryall's decision of that day)

40. **The kinds are answer, question, reading, evidence** (checks 0.6.0, standard formal-0.4). The kinds of
    October 17, gap, insight, stream and evidence, were a proposal never decided, and did not partition anything.
    The contribution check now answers two questions on each nearest work, `poses_question` (does it pose the
    question the claim answers) and `states_claim` (does it state the claim), and proposes the kind from them: an
    *answer* is a new claim on a question already posed; a *question* is a question not posed before, with its
    first answer; a *reading* is a question not posed before that results already in hand are shown to answer;
    *evidence* is new support for, or a new test of, a claim already stated. A claim already stated with no new
    support is `none`, not new. `uncovered` and `no_consensus` stay as values of the map only. The map keeps each
    work's two answers by majority of the answers that listed it, with the vote beside them. The editor signs the
    kind (`mark1 new --kind`); the map proposes it. The mapping is unchanged: it reads finding classes, not kinds.

## The question the contribution answers (2026-10-29, Kalanoski, after Ryall's reading of the first maps)

41. **The contribution claim carries the question it answers, as the paper states it** (protocol formal-0.4 P4,
    checks 0.7.0, generator 0.2.0, standard formal-0.5). Under checks 0.6.0 the prompt asked whether each nearest work
    "poses the question the claim answers" without saying what that question was, so the model stated it, and stated
    it broadly: every paper answers some question, and stated broadly enough someone has always asked it. The claims
    list now carries `question` and `question_pointer` on the contribution claim, in the paper's words and pointing at
    where the paper states them; a contribution claim without them is a Level 1 finding (P4). The map places the claim
    on that question, shows it with its pointer, and shows any answer that read it otherwise (`question_as_read`);
    where a record states none, the map says the model read it. Resolution reads the passage at the question pointer
    with the claim. The generator writes both fields. The editor who signs "new" on another kind than the map's, or on
    a broader or narrower reading of the question, gives the reading and the reason (`mark1 new --question-as-read
    --reason`); `new.yaml` records the map's kind and the departure, and `mark1 departures` counts them. Whether the
    question is stated at an honest breadth stays a judgment; it is now a signed one, on the author's words.
42. **The answering brief asks for a work log, not reasoning** (checks 0.7.0). Two answering sessions of 2026-10-28
    stopped on "write your reasoning to `transcript.md`", reading it as a request for their private reasoning; the
    brief and `HOW-TO-ANSWER.md` now ask for a short work log of what was done.

43. **Evidence that carries part of a claim proceeds to review** (mapping 0.3, inside checks 0.7.0). Under mapping
    0.2 any `pointer_missing` returned the paper for corrections, so a resolution verdict of "only in part" on one
    supporting claim out of eighty sent the whole paper back, and both intakes of the demonstration were signed
    departures. Kalanoski's reading (2026-10-29): a partial is the record saying where the support is and the claim
    being broader than that span; when the author submits with it visible on their own report, they stand behind the
    claim as written, and that is for reviewers to weigh, not a defect to fix. Resolution now reports a partial as
    class `evidence_partial`; rule R9 sends it to review with the finding carried; `pointer_missing` stays for a
    pointer that does not resolve or evidence that says nothing, and still returns under R3. The intake decision says
    which findings the author's own report already lists ("acknowledged at submission") and how many. This is the
    two-weights sentence Ryall asked for in §3, applied: findings against the standard bar publication; findings
    against the package's correspondence with itself travel with the paper. Ryall's reading (2026-10-29): not the
    two weights applied but a third path, and §3 says so; the row is in appendix D.3, the mapping table.

## After Ryall's clean-clone test (2026-10-29, to his answers of that day)

44. **A file of the AI appendix that is off its stamp is attributed from the AI-use record** (`machine/attribution.py`).
    Both rounds' `changed-by.yaml` said of `ai-appendix/claims.yaml` "does not match the stamp of generator run …;
    nothing in the record says who edited it", while each round's AI-use record carries the entry for the correction
    (scope `ai-appendix/claims.yaml`, role editing). Attribution read the generator stamp for files of the AI appendix
    and stopped there. It now goes on to the AI-use entries as for every other file: an entry added this round that
    covers the file makes the change "AI, declared", with the stamp mismatch and the declaration both in the basis;
    cover only by an earlier round's entry is "not declared this round"; "edited after generation" is left for a
    file that nothing declares. The two submitted `changed-by.yaml` files and the round diff stand as written
    (Ryall, 2026-10-29): they are what the journal recorded at submission, and appendix E.5 reports the gap as
    something the run found.
45. **Replay says when the answers are not there** (`machine/run.py`, `machine/cli.py`). From a clone, `mark1 replay`
    on a run of the demonstration printed "differs from the original in 1 field(s): 9 answer(s) missing from the
    stored run" (Ryall's clean-clone test, 2026-10-29). A run whose `bundles/` folder holds no answer now stops before
    anything is copied, saying that the stored answers are not in this repository, why, and that the test suite's run
    is what replays from a clone; a run with some answers missing reports that it could not finish and where the
    waiting prompts are, and the findings are not compared. Deterministic-only runs replay as before. The early stop
    also keeps a clone without `sieve/candidates.json` from building the map's candidate list anew, which would have
    gone to the network before the missing answers were noticed.

## After the figure check (2026-10-30)

46. **Replay reports a change of the check code apart from the findings** (`machine/run.py`, `machine/cli.py`). Every
    report carries the hash of the code that produced it, and a replay's copy carries the hash of the code that
    replayed it. After the corrections of 2026-10-29 (items 44 and 45) the replay of round 2's two runs reported
    "differs from the original in 1 field(s): machine_sha", with every finding reproduced. The code hash, and the
    version a deterministic finding carries, which is the same hash, are now left out of the comparison; when they
    differ, replay says so beside the result and gives both hashes. Round 2's two runs again reproduce exactly, with
    the note. One test added (106).
47. **Section numbers follow the appendix of 2026-10-30.** The cross-references in the code's docstrings and in the
    journal's documents named sections of an earlier draft of the appendix (the five published objects as "H", the
    planted defects as "I.4"); they now name the sections as the appendix numbers them. The teaching-note pilot the
    evaluation folder was waiting for is not in the current appendix, and its README says so.
