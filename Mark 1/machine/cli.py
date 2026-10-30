import argparse
import sys
from collections import Counter
from pathlib import Path

from . import corpus, history, inject, paths, recall, rtf, run, stats, texmd, workflow
from .llm import InvalidResponse, RecordChanged
from .modality import NotBuilt
from .schemas import SchemaError
from .state import StateError, state

KNOWN_ERRORS = (StateError, FileNotFoundError, InvalidResponse, RecordChanged, NotBuilt, SchemaError)
ACTIONS = ("proceed_to_review", "return_for_corrections", "return_without_review", "refer_to_specialist")


def main(argv: list[str] | None = None) -> int:
    # the Windows console defaults to cp1252 and chokes on the typography in titles and abstracts
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8", errors="replace")
    args = parser().parse_args(argv)
    try:
        return args.func(args) or 0
    except KNOWN_ERRORS as e:
        print(f"mark1: {e}", file=sys.stderr)
        return 2


def check(args) -> int:
    if args.resume:
        outcome = run.resume(args.resume)
    elif args.target:
        outcome = run.start(args.target, args.actor, args.deterministic_only, args.only)
    else:
        raise StateError("name a paper (or a record folder), or --resume RUN_ID")
    if outcome.pending:
        print(f"{len(outcome.pending)} bundle(s) waiting for an answer: {paths.relative(outcome.folder / 'PENDING.md')}")
        print(f"answer them, then: mark1 check --resume {outcome.run_id}")
        return 3
    _summary(outcome)
    return 0


def _summary(outcome: run.Outcome) -> None:
    report = outcome.report
    by_level = Counter(f.level for f in report.findings)
    print(f"run {outcome.run_id}: {len(report.findings)} finding(s) "
          f"(level 1: {by_level[1]}, level 2: {by_level[2]}, level 3: {by_level[3]})"
          + (f", {len(report.below_tolerance)} below tolerance" if report.below_tolerance else ""))
    for f in report.findings:
        print(f"  {f.id}  {f.finding_class:<20} {f.record_pointer}")
    print(f"report: {paths.relative(outcome.folder / 'findings.md')}")


def bundles(args) -> int:
    waiting = sorted(p for p in paths.root().rglob("bundles/*/k*/prompt.md") if not (p.parent / "response.json").exists())
    for p in waiting:
        print(paths.relative(p))
    print(f"{len(waiting)} bundle(s) waiting" if waiting else "no bundles waiting")
    return 0


def replay(args) -> int:
    outcome, differences = run.replay(args.run_id)
    if outcome.pending:
        print(f"replay of {args.run_id} could not finish: {len(outcome.pending)} of its answers are not stored with "
              f"the run, so the findings were not compared (the waiting prompts: "
              f"{paths.relative(outcome.folder / 'PENDING.md')})")
        return 3
    if differences:
        print(f"replay of {args.run_id} differs from the original in {len(differences)} field(s):")
        for d in differences:
            print(f"  {d}")
        return 1
    print(f"replay of {args.run_id} reproduces the original findings report exactly "
          f"({paths.relative(outcome.folder / 'findings.json')})")
    return 0


def submit(args) -> int:
    snapshot = workflow.submit(args.paper, args.author_run)
    print(f"submitted {args.paper} as {paths.relative(snapshot)}")


def intake(args) -> int:
    d = workflow.intake(args.paper, args.run_id, args.signed_by, args.action, args.reason, args.specialist)
    note = f" (departs from the standard action, {d['standard_action']})" if d["departure"] else ""
    print(f"{d['action']}{note}, signed by {args.signed_by}")


def defer_new(args) -> int:
    d = workflow.defer_new(args.paper, args.signed_by, args.reason)
    print(f"'new' deferred in round {d['round']}, signed by {args.signed_by}; review proceeds")


def answer(args) -> int:
    print(f"the author's answer to the map: {paths.relative(workflow.answer(args.paper, Path(args.file)))}")


def new(args) -> int:
    rec = workflow.new(args.paper, args.signed_by, args.kind, args.not_new or [], args.question_as_read, args.reason)
    note = f" (departs from the map, which proposed {rec['map_kind']})" if rec["departure"] else ""
    print(f"new, as {rec['kind']}" if rec["new"] else "not new; returned with the map", f"(signed by {args.signed_by}){note}")


def packet(args) -> int:
    print(f"reviewer packet: {paths.relative(workflow.packet(args.paper))}")


def report(args) -> int:
    print(f"reviewer report filed: {paths.relative(workflow.report(args.paper, args.reviewer, Path(args.file)))}")


def revise(args) -> int:
    note = workflow.revise(args.paper, args.signed_by, args.reason)
    print(f"revise and resubmit, signed by {args.signed_by}: {paths.relative(note)}")


def diff(args) -> int:
    print(f"diff: {paths.relative(workflow.diff(args.paper, args.a, args.b))}")


def interest(args) -> int:
    rec = workflow.interest(args.paper, args.signed_by, args.reviewer, args.interesting == "yes", args.statement)
    print(("of interest" if rec["interesting"] else "not of interest; no public object") +
          f", signed by {args.signed_by}, {args.reviewer[0]}, {args.reviewer[1]}")


def issue(args) -> int:
    cert, pub = workflow.issue(args.paper, args.by)
    print(f"certificate: {paths.relative(cert)}\npublication: {paths.relative(pub)}")


def status(args) -> int:
    s = state(args.paper)
    print(f"{args.paper}: {s.name.replace('_', ' ')}, round {s.round}, latest journal run {s.last_run or '-'}, "
          f"correction passes used {s.passes_used}")
    print(f"next: {s.next}")
    for e in history.events(args.paper)[-5:]:
        print(f"  {e['at']}  {e['event']}")


def departures(args) -> int:
    md, _ = stats.departures()
    print(md.read_text(encoding="utf-8"))


def build_corpus(args) -> int:
    result = corpus.build(offline=args.offline)
    for key in ("fetched", "cached", "skipped", "failed"):
        if result[key]:
            print(f"{key}: {', '.join(result[key])}")
    print(f"venues resolved in OpenAlex: {result['venues_resolved']}"
          + (f"; not resolved: {', '.join(result['venues_unresolved'])}" if result["venues_unresolved"] else ""))


def recall_test(args) -> int:
    path, hits = recall.measure(args.paper, args.run_id, args.expect)
    print(f"{hits} of {len(args.expect)} expected prior works retrieved: {paths.relative(path)}")
    return 0 if hits == len(args.expect) else 1


def rtf_docs(args) -> int:
    print(f"{len(rtf.twins(paths.root()))} .rtf twin(s) written beside their .md")


def import_tex(args) -> int:
    record = Path(args.record) if "/" in args.record or "\\" in args.record else paths.records() / args.record
    result = texmd.import_tex(Path(args.tex), record, Path(args.bib) if args.bib else None, args.choices or [],
                              args.does_not_claim or [], args.force)
    print(f"paper and appendix written under {paths.relative(record)}: {len(result.labels)} labelled headings, "
          f"figures, tables and equations; {len(result.log)} note(s)")
    for line in result.log:
        print(f"  {line}")
    return 0


def defects(args) -> int:
    for path in inject.inject(args.paper, args.defect):
        print(paths.relative(path))


def evaluate(args) -> int:
    report_path, passed = inject.evaluate(args.paper)
    print(f"{'all defects detected as expected' if passed else 'some defects were not detected as expected'}: "
          f"{paths.relative(report_path)}")
    return 0 if passed else 1


def parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="mark1", description="Mark 1: the journal after AI, on one formal paper.")
    sub = p.add_subparsers(required=True, metavar="command")

    def command(name: str, func, help_: str) -> argparse.ArgumentParser:
        c = sub.add_parser(name, help=help_)
        c.set_defaults(func=func)
        return c

    c = command("check", check, "run the checks (A3 author self-check, or M0-M6 journal intake)")
    c.add_argument("target", nargs="?", help="paper id under 2-author/, or a record folder")
    c.add_argument("--actor", choices=("author", "journal"), default="author")
    c.add_argument("--deterministic-only", action="store_true", help="skip the model-judged checks")
    c.add_argument("--only", nargs="+", metavar="CHECK", help="run only these checks")
    c.add_argument("--resume", metavar="RUN_ID", help="finish a run once its bundles are answered")

    command("bundles", bundles, "list prompt bundles waiting for an answer")
    command("replay", replay, "re-run a finished run from its stored answers").add_argument("run_id")

    c = command("submit", submit, "A4: submit the record with the author's findings report")
    c.add_argument("paper")
    c.add_argument("--author-run", help="which author run to attach (default: the latest finished)")

    c = command("intake", intake, "H1/D2/H2: a named editor applies the mapping")
    c.add_argument("paper")
    c.add_argument("run_id")
    c.add_argument("--signed-by", required=True)
    c.add_argument("--action", choices=ACTIONS, help="depart from the standard action (needs --reason)")
    c.add_argument("--reason")
    c.add_argument("--specialist")

    c = command("defer-new", defer_new, "H5 deferred: review proceeds before 'new' is signed, with the reason")
    c.add_argument("paper")
    c.add_argument("--signed-by", required=True, help="the editor")
    c.add_argument("--reason", required=True)

    c = command("answer", answer, "the author's one answer to the evidence map")
    c.add_argument("paper")
    c.add_argument("file")

    c = command("new", new, "H5: one editor signs what is new, on the evidence map")
    c.add_argument("paper")
    c.add_argument("--signed-by", required=True)
    group = c.add_mutually_exclusive_group(required=True)
    group.add_argument("--kind", choices=workflow.KINDS)
    group.add_argument("--not-new", nargs="+", metavar="CORPUS_ID")
    c.add_argument("--question-as-read", help="the question as the editor read it, when not as the paper states it")
    c.add_argument("--reason", help="required when the kind signed is not the map's, or the question is read otherwise")

    command("packet", packet, "build what reviewers receive").add_argument("paper")

    c = command("report", report, "file a reviewer's report in the review history")
    c.add_argument("paper")
    c.add_argument("--reviewer", required=True)
    c.add_argument("file")

    c = command("revise", revise, "A5/T1 after review: revise and resubmit, with the round's reports")
    c.add_argument("paper")
    c.add_argument("--signed-by", required=True, help="the editor")
    c.add_argument("--reason", required=True)

    c = command("diff", diff, "what changed between two submitted rounds")
    c.add_argument("paper")
    c.add_argument("a", type=int, help="the earlier round, or 0 for what round b brought and who made it")
    c.add_argument("b", type=int)

    c = command("interest", interest, "H3: the editor and two named reviewers sign interest")
    c.add_argument("paper")
    c.add_argument("--signed-by", required=True, help="the editor")
    c.add_argument("--reviewer", action="append", required=True, help="give exactly two")
    c.add_argument("--interesting", choices=("yes", "no"), required=True)
    c.add_argument("--statement", required=True)

    c = command("issue", issue, "D3: issue the certificate and the publication together, or nothing")
    c.add_argument("paper")
    c.add_argument("--by", required=True)

    command("status", status, "where a paper stands and what comes next").add_argument("paper")
    command("departures", departures, "departure statistics by editor")
    c = command("corpus", build_corpus, "resolve the venues and enrich the hand list from OpenAlex (1-journal/corpus/)")
    c.add_argument("--offline", action="store_true")

    c = command("recall", recall_test, "I.4: did the map reach the prior work it should have? writes evaluation/recall-<paper>.md")
    c.add_argument("paper")
    c.add_argument("run_id")
    c.add_argument("--expect", action="append", required=True, metavar="DOI", help="a DOI the map should reach; repeat")

    command("rtf", rtf_docs, "write an .rtf twin (Times New Roman 12) beside every document, for Word readers")

    c = command("import-tex", import_tex, "author's helper: a LaTeX paper into paper/ and appendix/ in the protocol's Markdown")
    c.add_argument("tex", help="the .tex file")
    c.add_argument("record", help="paper id under 2-author/, or a record folder")
    c.add_argument("--bib", help="the .bib file (default: the one \\bibliography names, beside the .tex)")
    c.add_argument("--choices", nargs="+", metavar="REF", help="labels or headings to carry into #choices")
    c.add_argument("--does-not-claim", nargs="+", metavar="REF", help="labels or headings to carry into #does-not-claim")
    c.add_argument("--force", action="store_true", help="overwrite an existing paper/ and appendix/")

    c = command("inject", defects, "make defected copies of a record for the evaluation")
    c.add_argument("paper")
    c.add_argument("--defect", nargs="+", choices=sorted(inject.DEFECTS))

    command("evaluate", evaluate, "check every defected copy and compare with what each should produce").add_argument("paper")
    return p


if __name__ == "__main__":
    sys.exit(main())
