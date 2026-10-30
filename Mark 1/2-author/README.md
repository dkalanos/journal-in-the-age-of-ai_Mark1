# 2-author/ · A2 to A4, what the author sends

One folder per paper: the research record, kept by the author (and the author's AI) as the work proceeds. The
layout is the protocol's (`../1-journal/protocol/formal.md#P1`):

    record.yaml          manifest
    declarations.yaml    modality, standard version, access tier, AI use
    paper/               for people
    appendix/            for the reader who checks; ends with the scope-and-choices section
    ai-appendix/         generated: definitions, procedure, claims, stance, anchors, scope, and the stamp
    materials/           code that reproduces reported values
    provenance/          derivations.yaml (the derivation behind each proposition) and ai-use.yaml
    self-check/<run>/    A3: the author's own runs of the published checks
    submission.yaml      A4: written by `mark1 submit`

The author sends the record itself, nothing else. `mark1 submit` copies it as received to
`../3-editor/<paper>/rounds/r<n>/`, and the journal works on that copy from then on; the author keeps working
here.

A synthetic record, `toy-monopoly/`, lived here until 2026-10-22; it was removed at Kalanoski's request. A
labelled simulation of the later steps, `questions-before-priors-simulation/`, was removed on 2026-10-28: the
demonstration stops at round 2's intake, and the tests take a copy of the record the rest of the way.

A real paper is added as a new folder. Source material stays outside the repository; the paper and
its appendix are extracted into a record here, and anything confidential stays behind. For a paper that exists
as LaTeX, `mark1 import-tex <file.tex> <paper-id> --choices <label> --does-not-claim <label>` writes `paper/`
and `appendix/` in the protocol's form; the author then adds `record.yaml`, `declarations.yaml`, `materials/`
and `provenance/`, and reads what the converter wrote.

`questions-before-priors/` is the first real paper: Ryall's *Questions Before Priors*, a theorem-proof paper
built from the repository dropped on 2026-10-21. Its `README.md` says what came from the source, what Claude
Code wrote, and what the author has not yet seen. It brought protocol formal-0.2 with it: derivations of kind
`proof`, because none of its results is a closed form the machine can re-solve.
