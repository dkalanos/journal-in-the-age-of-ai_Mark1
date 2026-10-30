"""One run of the checks on one record: the author's self-check (A3) or the journal's intake run (M0-M6).

With the bundle backend a run has two phases. The first writes a prompt bundle for every model-judged
question and stops; once the bundles are answered, `resume` finishes the report from the same folder.
"""
import shutil
from dataclasses import dataclass, field
from pathlib import Path

from . import generator, history, paths, render, versions
from .checks import REGISTRY, Context, NotRun
from .compare import mark_absent
from .findings import Finding, FindingsReport, assign_ids
from .llm import Pending
from .llm.bundle import BundleBackend
from .modality import route
from .record import Record
from .util import dump_json, load_json, load_yaml, now, stamp, write_text


@dataclass
class Outcome:
    run_id: str
    folder: Path
    pending: list[Path] = field(default_factory=list)
    report: FindingsReport | None = None
    code_changed: tuple[str, str] | None = None  # replay: the original's check-code hash and the replay's, if they differ


def start(target: str, actor: str = "author", deterministic_only: bool = False, only: list[str] | None = None) -> Outcome:
    if actor == "journal":
        submission = history.latest_submission(target)
        record, base = Record.load(submission / "record"), paths.intake(target)
    else:
        submission, record = None, Record.load(paths.record_dir(target))
        base = record.root / "self-check"
    run_id = f"{stamp()}-{actor}-{record.sha()[:7]}"
    folder = base / run_id
    dump_json({
        "run_id": run_id,
        "actor": actor,
        "record": paths.relative(record.root),
        "record_sha": record.sha(),
        "submission": paths.relative(submission) if submission else None,
        "deterministic_only": deterministic_only,
        "only": only,
        "started": now(),
    }, folder / "run.json")
    return execute(folder)


def resume(run_id: str) -> Outcome:
    return execute(find(run_id))


VOLATILE = {"run_id", "started", "finished"}


def replay(run_id: str) -> tuple[Outcome, list[str]]:
    """Re-run a finished run from its stored answers and report every difference from the original. A change of the
    check code since the run is reported apart from the differences, as Outcome.code_changed."""
    original = find(run_id)
    meta = load_json(original / "run.json")
    if not (original / "findings.json").exists():
        raise FileNotFoundError(f"run {run_id} never finished; resume it before replaying it")
    if Record.load(paths.root() / meta["record"]).sha() != meta["record_sha"]:
        raise FileNotFoundError(f"the record changed after run {run_id} (for instance, that run generated its AI "
                                "appendix); replay a later run")
    stored = sorted((original / "bundles").glob("*/k*/response.json")) if (original / "bundles").exists() else []
    if not meta["deterministic_only"] and not stored:
        raise FileNotFoundError(
            f"the stored answers of run {run_id} are not in this repository (its bundles/ folder holds none). The "
            "demonstration's answers do not ship, because the evidence map's prompts carry other people's text; see "
            "'Replay, no key' in the README. Nothing was replayed. From a clone, the test suite replays a run of its "
            "own: python -m pytest -q tests/test_journey.py")
    copy = original.parent / f"{run_id}-replay"
    shutil.rmtree(copy, ignore_errors=True)
    if (original / "bundles").exists():
        shutil.copytree(original / "bundles", copy / "bundles")
    if (original / "sieve" / "candidates.json").exists():
        (copy / "sieve").mkdir(parents=True)
        for name in ("candidates.json", "introductions.json"):
            if (original / "sieve" / name).exists():
                shutil.copyfile(original / "sieve" / name, copy / "sieve" / name)
    dump_json({**meta, "run_id": copy.name, "replay_of": run_id}, copy / "run.json")
    outcome = execute(copy)
    if outcome.pending:
        return outcome, [f"{len(outcome.pending)} answer(s) missing from the stored run"]
    before, after = load_json(original / "findings.json"), load_json(copy / "findings.json")
    if before.get("machine_sha") != after.get("machine_sha"):
        outcome.code_changed = (before.get("machine_sha"), after.get("machine_sha"))
    return outcome, _differences(before, after)


def _differences(a: dict, b: dict) -> list[str]:
    # the hash of the check code names what ran, the original's code or the replay's; a change there is reported
    # beside the result (Outcome.code_changed), not counted as a difference in the findings
    def strip(report: dict) -> dict:
        clean = {k: v for k, v in report.items() if k not in VOLATILE and k != "machine_sha"}
        for key in ("findings", "below_tolerance"):
            clean[key] = [{k: v for k, v in f.items()
                           if k != "run_id" and not (k == "model_version" and f.get("model") == "deterministic")}
                          for f in report.get(key, [])]
        return clean
    a, b = strip(a), strip(b)
    return [f"{key}: {a.get(key)!r} -> {b.get(key)!r}" for key in sorted(a.keys() | b.keys()) if a.get(key) != b.get(key)]


def find(run_id: str) -> Path:
    places = (paths.records().glob(f"*/self-check/{run_id}"), paths.editor().glob(f"*/intake/{run_id}"),
              paths.evaluation().glob(f"defected/*/self-check/{run_id}"))
    for hits in places:
        if found := sorted(hits):
            return found[0]
    raise FileNotFoundError(f"no run {run_id}")


def execute(folder: Path) -> Outcome:
    meta = load_json(folder / "run.json")
    record = Record.load(paths.root() / meta["record"])
    published = versions.published()
    tolerance = load_yaml(paths.journal() / "tolerance.yaml")
    backend = None if meta["deterministic_only"] else BundleBackend(folder, published["checks"])
    ctx = Context(record=record, actor=meta["actor"], run_dir=folder, versions=published, tolerance=tolerance,
                  backend=backend)
    if meta["submission"]:
        ctx.submission_dir = paths.root() / meta["submission"]
        ctx.submission = load_yaml(ctx.submission_dir / "submission.yaml")
    modality = route(record)
    not_run: list[dict] = []
    ai_appendix = "submitted with the record"
    overlay = folder / "ai-appendix"

    if not meta.get("generated") and not record.has_ai_appendix():
        if backend is None:
            not_run.append({"check": "generate", "reason": "the record has no AI appendix and this run is deterministic-only"})
        else:
            target = overlay if ctx.actor == "journal" else record.ai_dir
            try:
                stamp_ = generator.generate(record, backend, published, ctx.k, target, run_id=meta["run_id"])
            except Pending as p:
                return _pending(meta, folder, p.prompts)
            if ctx.actor == "author":
                generator.record_run(record, stamp_)
            meta["generated"] = {"agreement": stamp_["agreement"], "label":
                                 "absent at submission; generated by the journal in this run (M0)" if ctx.actor == "journal"
                                 else "generated by the author's run of the published generator in this run"}
            dump_json(meta, folder / "run.json")
    if meta.get("generated"):
        # check (d) has nothing to compare against an appendix this run wrote itself
        ctx.generated_here = True
        ctx.note_agreement("generate", meta["generated"]["agreement"])
        ai_appendix = meta["generated"]["label"]
        if ctx.actor == "journal":
            ctx.record = record = Record.load(record.root, ai_dir=overlay)

    findings: list[Finding] = []
    pending: list[Path] = []
    for check in REGISTRY:
        if check.name not in modality.checks or (meta["only"] and check.name not in meta["only"]):
            continue
        try:
            findings += check.run(ctx)
        except Pending as p:
            pending += p.prompts
            continue
        except NotRun as e:
            not_run.append({"check": check.name, "reason": str(e)})
            continue
        if backend is None and not check.deterministic:
            not_run.append({"check": check.name, "reason": "deterministic-only run: the model-judged part was not run"})
    if pending:
        return _pending(meta, folder, pending)
    return _finish(meta, folder, ctx, findings, not_run, ai_appendix)


def _pending(meta: dict, folder: Path, prompts: list[Path]) -> Outcome:
    lines = [f"# {len(prompts)} bundle(s) waiting for an answer", "",
             "Answer each prompt by writing `response.json` (and `transcript.md`) next to it, then run:", "",
             f"    mark1 check --resume {meta['run_id']}", ""]
    lines += [f"- `{paths.relative(p)}`" for p in prompts]
    write_text(folder / "PENDING.md", "\n".join(lines) + "\n")
    return Outcome(meta["run_id"], folder, pending=prompts)


def _finish(meta, folder, ctx: Context, findings: list[Finding], not_run: list[dict], ai_appendix: str) -> Outcome:
    (folder / "PENDING.md").unlink(missing_ok=True)
    machine_sha = versions.machine_sha()
    for f in findings:
        f.run_id, f.check_version = meta["run_id"], ctx.versions["checks"]
        f.standard_version = ctx.versions["standard"] if f.level == 3 else None
        if f.model == "deterministic":
            f.model_version = machine_sha
    below = [f for f in findings if f.model != "deterministic" and not ctx.agreement.get(f.check, {}).get("met", True)]
    published = [f for f in findings if f not in below]
    assign_ids(published)
    assign_ids(below)

    answers = [a for batch in (ctx.backend.answers.values() if ctx.backend else []) for a in batch]
    models = sorted({a.model for a in answers})
    report = FindingsReport(header={
        "run_id": meta["run_id"],
        "actor": meta["actor"],
        "paper_id": ctx.record.paper_id,
        "record_sha": ctx.record.sha(),
        "round": (ctx.submission or {}).get("round"),
        "versions": ctx.versions,
        "machine_sha": machine_sha,
        "models_used": [{"model": m, "backend": ctx.backend.name, "answers": sum(a.model == m for a in answers)}
                        for m in models],
        "started": meta["started"],
        "finished": now(),
        "cost": {"bundles": len(answers), "input_tokens": None, "output_tokens": None, "usd": None,
                 "note": "the answers come from chat sessions, which report no token counts"},
        "agreement": ctx.agreement,
        "ai_appendix": ai_appendix,
        "ai_appendix_stamp": generator.stamp_status(ctx.record, ctx.versions),  # a fact, P3
        "checks_run": [c.name for c in REGISTRY if c.name not in {n["check"] for n in not_run}],
        "checks_not_run": not_run,
    }, findings=published, below_tolerance=below)

    if ctx.actor == "journal":
        author = FindingsReport.load(ctx.submission_dir / "author-report" / "findings.json") \
            if (ctx.submission_dir / "author-report" / "findings.json").exists() else FindingsReport(header={})
        absent, author_only = mark_absent(report, author)
        write_text(folder / "diff-vs-author.md",
                   render.comparison(report.header["paper_id"], meta["run_id"], ctx.submission.get("author_run", "?"),
                                     absent, author_only), rtf=True)
    report.write(folder)
    _write_sieve(folder, report, ctx)
    if ctx.actor == "journal" and not meta.get("replay_of"):
        history.append(report.header["paper_id"], "checked", run_id=meta["run_id"], round=report.header["round"],
                       record_sha=report.header["record_sha"], findings=len(published))
    return Outcome(meta["run_id"], folder, report=report)


def _write_sieve(folder: Path, report: FindingsReport, ctx: Context) -> None:
    sieve = folder / "sieve"
    # candidates.json is the check's input; it stays
    for name in ("warrant.md", "evidence-map.json", "evidence-map.md", "perturbation.md"):
        (sieve / name).unlink(missing_ok=True)
    warrant = FindingsReport(header=report.header, findings=[f for f in report.findings if f.level == 3],
                             below_tolerance=[f for f in report.below_tolerance if f.level == 3])
    write_text(sieve / "warrant.md", render.findings(warrant).replace("# Findings report", "# SIEVE · warrant findings", 1), rtf=True)
    if emap := ctx.outputs.get("evidence_map"):
        from . import schemas
        schemas.validate("evidence-map", emap)
        dump_json(emap, sieve / "evidence-map.json")
        write_text(sieve / "evidence-map.md", render.evidence_map(emap), rtf=True)
    if rows := ctx.outputs.get("perturbation"):
        write_text(sieve / "perturbation.md", render.perturbation(report.header["paper_id"], rows), rtf=True)
