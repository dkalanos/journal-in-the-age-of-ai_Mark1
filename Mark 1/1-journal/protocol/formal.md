# Record protocol · formal theory · version formal-0.4

Published object 1 (appendix H). What a research record in the formal-theory modality contains, how its
parts point at each other, and what the Level 2 checks mean for it. The protocol is a field specification:
it belongs to the field, not to one journal. Findings cite its clauses as `protocol/formal.md#P<n>`.

## P1. The record's parts {#P1}

A record is a folder with a manifest, `record.yaml` (schema `schemas/record.schema.yaml`), and these parts:

| Part | Path | For |
|---|---|---|
| Paper | `paper/` | people: the question, what was done, what it means. Any length. Opens with the front notice (P2). |
| Appendix | `appendix/` | the reader who checks: derivations, procedures, the scope-and-choices section (P2). |
| AI appendix | `ai-appendix/` | the reader that evaluates: the author's statement to the machine, in the published form (P3). |
| Materials | `materials/` | code that reproduces reported values, in a declared access tier (P11). |
| Provenance | `provenance/` | the derivation behind each proposition (P6) and the AI-use record (P7). |
| Declarations | `declarations.yaml` | modality, standard version, access tier, AI use (P7). |

## P2. The two human layers {#P2}

The paper and the appendix are written by the authors, with whatever help they choose. Headings that a claim
points at carry an explicit id, `### Proposition 1 {#prop-1}`. The appendix ends with a section
`## Scope and choices {#scope-and-choices}` holding two subsections:

- `### Choices {#choices}`: the choices made and why; what was tried and set aside.
- `### Does not claim {#does-not-claim}`: what the paper does not claim; which frameworks are not to be imported.

These are the authors' own words; the AI appendix carries them as parts 4 and 6 (P3).

The paper opens with a front notice (added in formal-0.3). Before its first section, after the title and
byline, a paragraph beginning `**AI appendix.**` says that an AI appendix in this protocol's form accompanies
the paper and where it is: `ai-appendix/` in the record, and the published location once the paper is
published. Level 1 checks that the notice is there; its wording beyond those two facts is the authors'. The
notice states facts and addresses no reader: like any text in the record, a sentence addressed to an evaluator
is reported under P12.

## P3. The AI appendix {#P3}

The author's statement to the machine: how the paper is to be read by the reader that evaluates. Its content
is the author's alone; the journal publishes the form and requires conformance to it at submission. Six parts:

1. `definitions.md`: definitions of record, every term used in a non-default sense.
2. `procedure.md`: the solution method, step by step.
3. `claims.yaml`: the claims list (P4).
4. `stance.md`: the authors' stance, the words of `#choices`.
5. `anchors.yaml`: reproduction anchors (P5).
6. `scope.md`: scope and do-nots, the words of `#does-not-claim`.

Declarations live once, in `declarations.yaml`, rather than as a seventh part. The author may write the AI
appendix with any tool, or by hand, and may edit it. The journal's generator (M0) is the reference
implementation of this form, offered to authors as a convenience; a submission that arrives without an AI
appendix receives one from it on intake, and the report says so. An AI appendix the generator wrote carries a
stamp, `generated.yaml`: the generator version, the run that produced it, and the hash of every input and output
(schema `schemas/generated.schema.yaml`). Whether the AI appendix still matches its stamp is recorded on the
findings report as a fact; it is not a finding (formal-0.3; formal-0.2 had check (d)). What the AI appendix says
is held to the paper, the appendix and the record by the Level 2 checks (P10): understatement by completeness,
overstatement by resolution.

## P4. The claims list {#P4}

Every claim the contribution rests on, schema `schemas/claims.schema.yaml`. Each claim has an id (`C1`, ...),
a kind (`result`, `causal`, `contribution`), a form for formal results (`proposition`, `comparative_static`,
`lemma`, `example`), a `main` flag, the text, the conditions it is stated under, a pointer to where the paper
states it, a pointer to the evidence in the record, and the derivation that supports it. The list contains at
least one contribution claim and at least one main claim. The contribution claim also carries the question it
answers, in the paper's words, and a pointer to where the paper states it (formal-0.4): the evidence map places
the claim on that question, not on a reading of the machine's own.

## P5. Reproduction anchors {#P5}

Three to five results a reader must reproduce before proceeding, schema `schemas/anchors.schema.yaml`. An
anchor re-runs a function in `materials/` with stated arguments, or evaluates an ASCII expression in the
symbols of a named derivation, and compares the result with the stated value: a number within a tolerance,
a sign, or an identity.

## P6. Provenance: the derivation behind each proposition {#P6}

For formal work, provenance means the derivation behind each proposition, stated checkably in
`provenance/derivations.yaml` (schema `schemas/derivations.schema.yaml`): the symbols and their domains and
meanings, the assumptions, the objective and the choice variable, the stated solution, the derived
quantities, the closed forms stated in the paper, the comparative statics with their stated signs, and the
numerical examples. Every proposition, comparative static and lemma in the claims list names a derivation.
Expressions are ASCII arithmetic in declared symbols; nothing else is read.

A result that is proved rather than solved, a theorem with a proof, is a derivation of kind `proof` (added in
formal-0.2): the hypotheses as the paper states them, the steps of the argument, and for each step what it rests
on, as pointers into the record (P9) or as `cited: ...` for work outside it, and the conclusion. The machine
checks that the pointers resolve and that nothing rests on itself; it does not judge whether a step follows.
Numerical facts a theorem-paper states, worked examples and thresholds, go in closed-form derivations beside it.

## P7. Declarations and the AI-use record {#P7}

`declarations.yaml` states the modality, the version of the standard followed, the access tier of the
materials, how AI was used (tools and roles), and whether the working history is submitted.
`provenance/ai-use.yaml` is the AI-use record: one entry per use, with the tool, the role, what it touched
(a pointer into the record), the date, and the human direction behind it. Every tool the declarations name
has an entry. When the generator produced the AI appendix, the record names that run, and it must match the
stamp's run; whether the files still match the stamp is a fact on the report (P3). The record cannot prove human direction; like an authorship statement, it rests on good
faith and reputation (appendix E.5).

## P8. Submission {#P8}

The author submits the record together with their own findings report from the published checks, run on
this exact version of the record with the published versions. The report is a declaration of participation
and the baseline the journal's run is compared with; it is not proof of a pass.

## P9. Pointer grammar {#P9}

| Pointer | Names |
|---|---|
| `paper/paper.md` | a whole file |
| `paper/paper.md#prop-1` | a section, by its `{#id}` or by the slug of its heading |
| `paper/paper.md:L12-L14` | a line range (`:L12` for one line) |
| `claims:C1`, `anchors:A2`, `derivations:D1` | an entry in a record table |

A finding whose record pointer does not resolve is not emitted: no pointer, no flag.

## P10. Level 2 for formal theory {#P10}

A claim is a proposition or a comparative static. A pointer names the derivation. An anchor holds when the
derivation's steps re-check and a stated numerical example evaluates as stated.

- (a) Completeness: every statement in the paper that the contribution rests on is in the claims list.
- (b) Resolution: each claim's pointers resolve, and the evidence says what the claim says.
- (c) Anchors: each reproduction anchor reproduces. Deterministic.

formal-0.2 had a fourth check, (d) derivation, which held the AI appendix to the generator's output. It is
withdrawn in formal-0.3: the AI appendix is the author's (P3), and whether it matches its stamp is a fact on
the report, not a finding.

## P11. Access tiers {#P11}

Materials are `public`, `restricted` (available under stated conditions), or `described_only`. Level 2 checks
them to the extent the tier admits. For formal work the materials are usually public code; the data
verification line on the certificate reads "not applicable".

## P12. Text addressed to the evaluator {#P12}

The checks receive the published instructions as instructions and the whole record, parts 4 and 6 included,
as data in a fenced channel. Parts 4 and 6 are reported, never executed. Text anywhere in the record that
addresses an evaluator, reviewer or model, and invisible characters or hidden comments, are findings in class
`injection`.
