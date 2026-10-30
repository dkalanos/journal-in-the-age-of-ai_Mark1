"""The steps people take (Fig. 4b), each signed by a named person and appended to the review history.

A4 submit · H1/D2/H2 intake decision · the author's one answer to the map · H5 new · the reviewers'
packet and reports · the diff between rounds · H3 interest · D3 issue the certificate and publication.
"""
import difflib
import shutil
from pathlib import Path

from . import attribution, history, mapping, paths, render, rtf, schemas, versions
from .findings import FindingsReport
from .pointer import slug
from .record import HASHED_PARTS, Record
from .state import StateError, require
from .util import dump_yaml, load_json, load_yaml, now, sha256_file, write_text

KINDS = ("answer", "question", "reading", "evidence")
RETURNS = ("return_for_corrections", "return_without_review")
TEXT_SUFFIXES = (".md", ".yaml", ".yml", ".py", ".txt", ".csv", ".json", ".tex")


def sign(name: str, role: str, *files: Path) -> dict:
    # a named, timestamped statement of exactly which files were signed; not a cryptographic signature
    return {"name": name, "role": role, "at": now(), "signs": {paths.relative(f): sha256_file(f) for f in files}}


def submit(paper_id: str, author_run: str | None = None) -> Path:
    root = paths.record_dir(paper_id)
    s = require(paper_id, "draft", "returned_for_corrections", "returned", "closed", "in_review", "revise_requested")
    finished = sorted(p for p in (root / "self-check").glob("*-author-*")
                      if (p / "findings.json").exists() and not load_json(p / "run.json")["deterministic_only"])
    run = root / "self-check" / author_run if author_run else (finished[-1] if finished else None)
    if not run or not (run / "findings.json").exists():
        raise StateError("no finished author run to attach: run `mark1 check <paper>` and answer its bundles first")
    sha = Record.load(root).sha()
    if load_json(run / "findings.json")["record_sha"] != sha:
        raise StateError(f"author run {run.name} checked an earlier version of the record; run the checks again")
    n = s.round + 1
    snapshot = history.folder(paper_id) / "rounds" / f"r{n}"
    shutil.copytree(root, snapshot / "record", ignore=shutil.ignore_patterns("self-check", "submission.yaml", "__pycache__"))
    shutil.copytree(run, snapshot / "author-report")
    submission = {"paper_id": paper_id, "round": n, "record_sha": sha, "author_run": run.name, "submitted_at": now()}
    schemas.validate("submission", submission)
    dump_yaml(submission, snapshot / "submission.yaml")
    dump_yaml(submission, root / "submission.yaml")
    previous = history.folder(paper_id) / "rounds" / f"r{n - 1}" if n > 1 else None
    found = attribution.attribute(Record.load(previous / "record") if previous else None, Record.load(snapshot / "record"),
                                  load_yaml(previous / "submission.yaml")["submitted_at"] if previous else None)
    dump_yaml(found, snapshot / "changed-by.yaml")
    history.append(paper_id, "submitted", round=n, record_sha=sha, author_run=run.name,
                   changed_by={c["file"]: c["by"] for c in found["changes"]}, declared=len(found["declared"]),
                   declared_late=len(found["declared_late"]))
    return snapshot


def intake(paper_id: str, run_id: str, signed_by: str, action: str | None = None, reason: str | None = None,
           specialist: str | None = None) -> dict:
    s = require(paper_id, "checked", "referred")
    if s.name == "referred" and signed_by != s.specialist:
        raise StateError(f"the paper was referred to {s.specialist}; only they apply the mapping now")
    if run_id != s.last_run:
        raise StateError(f"decide on the latest journal run, {s.last_run}")
    folder = paths.intake(paper_id) / run_id
    report_path = folder / "findings.json"
    rules = mapping.load()
    findings = FindingsReport.load(report_path).findings
    standard = mapping.standard_action(findings, s.passes_used, rules)
    # a finding the author's own report already lists was acknowledged at submission: the author saw it and
    # submitted; it travels with the paper (appendix D.2, mapping 0.3)
    acknowledged = sorted(f.id for f in findings if f.absent_from_author is False)
    for r in standard.fired:
        r["acknowledged"] = r["finding"] in acknowledged
    chosen = action or standard.action
    if chosen != standard.action and not reason:
        raise StateError(f"departing from the standard action ({standard.action}) needs --reason")
    if chosen == "refer_to_specialist" and not specialist:
        raise StateError("a referral names the specialist: --specialist NAME")
    departure = {"direction": mapping.direction(standard.action, chosen, rules), "reason": reason} \
        if chosen != standard.action else None
    decision = {
        "kind": "intake", "paper_id": paper_id, "run_id": run_id, "report_sha": sha256_file(report_path),
        "standard_action": standard.action, "fired_rules": standard.fired, "passes_used": s.passes_used,
        "action": chosen, "departure": departure,
        "acknowledged": acknowledged, "findings_total": len(findings),
        "specialist": specialist if chosen == "refer_to_specialist" else None,
        "signature": sign(signed_by, "specialist editor" if s.name == "referred" else "editor", report_path),
    }
    schemas.validate("decision", decision)
    earlier = len(list(folder.glob("decision*.yaml")))
    name = f"decision-{earlier + 1}" if earlier else "decision"
    dump_yaml(decision, folder / f"{name}.yaml")
    write_text(folder / f"{name}.md", render.decision(decision), rtf=True)
    history.append(paper_id, "decided", run_id=run_id, action=chosen, standard_action=standard.action,
                   departure=departure, signed_by=signed_by, specialist=decision["specialist"],
                   acknowledged=len(acknowledged), findings_total=len(findings),
                   classes=sorted({r["class"] for r in standard.fired}))
    if chosen in RETURNS:
        fired = [r for r in standard.fired if r["action"] != "proceed_to_review"]
        write_text(history.folder(paper_id) / "returns" / f"r{s.round}-{chosen}.md",
                   render.return_note(paper_id, chosen, fired, paths.relative(report_path), signed_by, departure), rtf=True)
    return decision


def defer_new(paper_id: str, signed_by: str, reason: str) -> dict:
    """The editor lets review proceed before "new" is signed, with the reason recorded (a departure from Fig. 4b,
    CHANGES item 38). "new" stays owed: it is signed later, on the evidence map, after the author's one answer."""
    s = require(paper_id, "awaiting_new")
    if not reason.strip():
        raise StateError("deferring \"new\" needs a reason, recorded in the review history")
    emap = paths.intake(paper_id) / s.last_run / "sieve" / "evidence-map.json"
    signature = sign(signed_by, "editor", *([emap] if emap.exists() else []))
    history.append(paper_id, "new_deferred", round=s.round, reason=reason, signature=signature)
    return {"paper_id": paper_id, "round": s.round, "reason": reason, "signature": signature}


def answer(paper_id: str, file: Path) -> Path:
    s = require(paper_id, "awaiting_new", "in_review")
    if s.name == "in_review" and not s.new_deferred:
        raise StateError("the author answers the map before \"new\" is signed, and \"new\" is already signed")
    if s.answered:
        raise StateError("the author answers the evidence map once, and already has")
    dest = history.folder(paper_id) / "author-answer.md"
    shutil.copyfile(file, dest)
    history.append(paper_id, "answered", sha=sha256_file(dest))
    return dest


def new(paper_id: str, signed_by: str, kind: str | None = None, not_new_because: list[str] = (),
        question_as_read: str | None = None, reason: str | None = None) -> dict:
    s = require(paper_id, "awaiting_new", "in_review")
    if s.name == "in_review" and not s.new_deferred:
        raise StateError("\"new\" is already signed for this paper")
    if not s.answered:
        raise StateError("the author answers the evidence map once before 'new' is signed (`mark1 answer`)")
    if bool(kind) == bool(not_new_because):
        raise StateError("sign either --kind or --not-new with the prior work that establishes it")
    if kind and kind not in KINDS:
        raise StateError(f"the kinds of newness are {', '.join(KINDS)}")
    emap_path = paths.intake(paper_id) / s.last_run / "sieve" / "evidence-map.json"
    if not emap_path.exists():
        raise StateError("the latest journal run has no evidence map")
    emap = load_json(emap_path)
    on_map = {n["corpus_id"] for c in emap["claims"] for n in c["nearest"]}
    if stray := [p for p in not_new_because if p not in on_map]:
        raise StateError(f"'not new' rests on prior work the map shows; not on the map: {', '.join(stray)}")
    # the map proposes the kind on the question as the paper states it; an editor who signs another kind, or reads
    # the question otherwise, says why, and the departure is counted (standard S6, formal-0.5)
    map_kind = next((c["newness_kind"] for c in emap["claims"]), None)
    departure = bool(question_as_read) or (kind or "none") != map_kind
    if departure and not reason:
        raise StateError("signing a kind other than the map's, or reading the question otherwise than the paper states "
                         "it, needs --reason")
    folder = history.folder(paper_id)
    record = {"paper_id": paper_id, "new": bool(kind), "kind": kind, "not_new_because": list(not_new_because),
              "map_kind": map_kind, "question_as_read": question_as_read, "reason": reason, "departure": departure,
              "signature": sign(signed_by, "editor", emap_path, folder / "author-answer.md")}
    schemas.validate("new", record)
    dump_yaml(record, folder / "new.yaml")
    history.append(paper_id, "new_signed", new=bool(kind), kind=kind, map_kind=map_kind, departure=departure,
                   question_as_read=question_as_read, reason=reason, signed_by=signed_by)
    if not kind:
        write_text(folder / "returns" / f"r{s.round}-not-new.md",
                   render.not_new_note(paper_id, not_new_because, paths.relative(emap_path), signed_by), rtf=True)
    return record


def packet(paper_id: str) -> Path:
    s = require(paper_id, "in_review", "awaiting_certificate")
    run = paths.intake(paper_id) / s.last_run
    out = paths.reviewers(paper_id) / "packet"
    if out.exists():
        shutil.rmtree(out)
    record = history.latest_submission(paper_id) / "record"
    shutil.copytree(record / "paper", out / "paper")
    shutil.copytree(record / "appendix", out / "appendix")
    for md in (*out.glob("paper/*.md"), *out.glob("appendix/*.md")):
        rtf.twin(md)
    for name in ("findings.md", "findings.json"):
        shutil.copyfile(run / name, out / name)
    for name in ("evidence-map.md", "evidence-map.json"):
        if (run / "sieve" / name).exists():
            shutil.copyfile(run / "sieve" / name, out / name)
    shutil.copyfile(paths.journal() / "interest-criteria.md", out / "interest-criteria.md")
    write_text(out / "README.md", render.packet_readme(paper_id, s.round, s.last_run), rtf=True)
    history.append(paper_id, "packet_built", run_id=s.last_run, round=s.round)
    return out


def report(paper_id: str, reviewer: str, file: Path) -> Path:
    s = require(paper_id, "in_review")
    dest = paths.reviewers(paper_id) / "reports" / f"r{s.round}-{slug(reviewer)}.md"
    dest.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(file, dest)
    history.append(paper_id, "review_report", round=s.round, reviewer=reviewer, sha=sha256_file(dest))
    return dest


def revise(paper_id: str, signed_by: str, reason: str) -> Path:
    """A5/T1 after review: revise and resubmit. The record goes back with this round's reports; the next submission
    is a new round against the same review history, not a new paper."""
    s = require(paper_id, "in_review")
    reports = sorted((paths.reviewers(paper_id) / "reports").glob(f"r{s.round}-*.md"))
    if not reports:
        raise StateError(f"revise and resubmit rests on the reviewers' reports; round {s.round} has none yet")
    signature = sign(signed_by, "editor", *reports)
    note = history.folder(paper_id) / "returns" / f"r{s.round}-revise_and_resubmit.md"
    write_text(note, render.revise_note(paper_id, s.round, [paths.relative(r) for r in reports], reason, signed_by),
               rtf=True)
    history.append(paper_id, "revise_requested", round=s.round, reason=reason, signature=signature)
    return note


def diff(paper_id: str, a: int, b: int) -> Path:
    """a = 0 reads what round b brought: every file is new, so only who made it is shown."""
    rounds = history.folder(paper_id) / "rounds"
    for n in filter(None, (a, b)):
        if not (rounds / f"r{n}" / "record").exists():
            raise FileNotFoundError(f"{paper_id} has no round {n}")
    new_ = Record.load(rounds / f"r{b}" / "record")
    out = history.folder(paper_id) / "diffs" / f"r{a}-r{b}.md"
    if not a:
        write_text(out, render.round_diff(paper_id, a, b, [], [], attribution.attribute(None, new_)), rtf=True)
        history.append(paper_id, "diffed", rounds=[a, b])
        return out
    old = Record.load(rounds / f"r{a}" / "record")
    files = sorted(set(_texts(old)) | set(_texts(new_)))
    changes = []
    for rel in files:
        before = old.text(rel).splitlines() if old.path(rel).exists() else []
        after = new_.text(rel).splitlines() if new_.path(rel).exists() else []
        if before != after:
            changes.append((rel, list(difflib.unified_diff(before, after, f"r{a}/{rel}", f"r{b}/{rel}", lineterm=""))))
    since = load_yaml(rounds / f"r{a}" / "submission.yaml")["submitted_at"]
    who = attribution.attribute(old, new_, since)
    write_text(out, render.round_diff(paper_id, a, b, _claim_changes(old, new_), changes, who), rtf=True)
    history.append(paper_id, "diffed", rounds=[a, b])
    return out


def interest(paper_id: str, editor: str, reviewers: list[str], interesting: bool, statement: str) -> dict:
    require(paper_id, "in_review")
    if len(set(reviewers)) != 2 or len(reviewers) != 2 or editor in reviewers:
        raise StateError("interest is signed by the editor and two distinct named reviewers")
    folder = history.folder(paper_id)
    signed = (paths.journal() / "interest-criteria.md", folder / "new.yaml")
    record = {
        "paper_id": paper_id, "interesting": interesting,
        "criteria_version": versions.published()["interest_criteria"], "statement": statement,
        "signatures": [sign(editor, "editor", *signed)] + [sign(r, "reviewer", *signed) for r in reviewers],
    }
    schemas.validate("interest", record)
    dump_yaml(record, folder / "interest.yaml")
    history.append(paper_id, "interest_signed", interesting=interesting, editor=editor, reviewers=reviewers)
    return record


def issue(paper_id: str, by: str) -> tuple[Path, Path]:
    try:
        return _issue(paper_id, by)
    except (StateError, FileNotFoundError, ValueError) as e:
        history.append(paper_id, "issue_refused", by=by, reason=str(e))
        raise


def _issue(paper_id: str, by: str) -> tuple[Path, Path]:
    s = require(paper_id, "awaiting_certificate")
    folder = history.folder(paper_id)
    new_rec, interest_rec = load_yaml(folder / "new.yaml"), load_yaml(folder / "interest.yaml")
    editor, *reviewers = [sig["name"] for sig in interest_rec["signatures"]]
    if by != editor:
        raise StateError(f"the certificate is issued by the editor who signed interest, {editor}")
    submission = history.latest_submission(paper_id)
    sub = load_yaml(submission / "submission.yaml")
    run = paths.intake(paper_id) / s.last_run
    report_ = load_json(run / "findings.json")
    if report_.get("round") != sub["round"]:
        raise StateError(f"the latest journal run checked round {report_.get('round')}, not the submitted round {sub['round']}")
    out = paths.published(paper_id)
    if out.exists():
        raise StateError("already issued: one certificate per record")
    cert_dir, pub_dir = out / "certificate", out / "publication"

    record = Record.load(submission / "record")
    decl = record.declarations
    summary = decl.get("ai_use_summary") or {}
    doi = f"10.5555/mark1.{paper_id}"
    certificate = {
        "paper_id": paper_id,
        "title": record.manifest.get("title", paper_id),
        "record_sha": sub["record_sha"],
        "versions": report_["versions"],
        "journal_run": {"run_id": s.last_run, "models": [m["model"] for m in report_["models_used"]],
                        "machine_sha": report_["machine_sha"]},
        "data": {"materials_tier": decl.get("materials_tier"),
                 "verification": "not_applicable" if decl.get("modality") == "formal" else "as_declared"},
        "new": {"kind": new_rec["kind"], "signed_by": new_rec["signature"]["name"],
                "evidence_map": paths.relative(cert_dir / "evidence-map.json")},
        "interest": {"criteria_version": interest_rec["criteria_version"], "editor": editor, "reviewers": reviewers,
                     "statement": interest_rec["statement"]},
        "ai_use": {"summary": f"tools: {', '.join(summary.get('tools', [])) or 'none'}; "
                              f"used for: {', '.join(summary.get('roles', [])) or 'nothing'}",
                   "working_history_submitted": bool(decl.get("working_history_submitted"))},
        "signed_by": [editor, *reviewers],
        "publication": {"doi": doi, "minted": False},
        "issued_at": now(),
    }
    schemas.validate("certificate", certificate)

    staging = paths.root() / f".issuing-{paper_id}"
    shutil.rmtree(staging, ignore_errors=True)
    try:
        cert_tmp, pub_tmp = staging / "certificate", staging / "publication"
        dump_yaml(certificate, cert_tmp / "certificate.yaml")
        write_text(cert_tmp / "certificate.md", render.certificate(certificate), rtf=True)
        for name in ("evidence-map.json", "evidence-map.md"):
            shutil.copyfile(run / "sieve" / name, cert_tmp / name)
        for part in ("paper", "appendix"):
            shutil.copytree(record.root / part, pub_tmp / part)
        manifest = {
            "paper_id": paper_id, "doi": doi, "minted": False, "record_sha": sub["record_sha"],
            "files": sorted(p.relative_to(pub_tmp).as_posix() for p in pub_tmp.rglob("*") if p.is_file()),
            "certificate": paths.relative(cert_dir / "certificate.yaml"),
            "record_link": {"path": paths.relative(submission / "record"), "tier": decl.get("materials_tier")},
        }
        schemas.validate("publication", manifest)
        dump_yaml(manifest, pub_tmp / "manifest.yaml")
        out.parent.mkdir(parents=True, exist_ok=True)
        staging.rename(out)  # one rename: the certificate and the publication appear together or not at all
    finally:
        shutil.rmtree(staging, ignore_errors=True)
    history.append(paper_id, "issued", by=by, doi=doi, certificate=paths.relative(cert_dir))
    return cert_dir, pub_dir


def _texts(record: Record) -> list[str]:
    return [rel for part in HASHED_PARTS for rel in record.files(part) if rel.endswith(TEXT_SUFFIXES)]


def _claim_changes(old: Record, new_: Record) -> list[str]:
    before, after = {c["id"]: c for c in old.claims}, {c["id"]: c for c in new_.claims}
    changes = [f"{cid} added: {after[cid]['text']}" for cid in sorted(after.keys() - before.keys())]
    changes += [f"{cid} removed: {before[cid]['text']}" for cid in sorted(before.keys() - after.keys())]
    for cid in sorted(before.keys() & after.keys()):
        for key in ("text", "condition", "main", "evidence_pointer"):
            if before[cid].get(key) != after[cid].get(key):
                changes.append(f"{cid} {key.replace('_', ' ')}: {before[cid].get(key)!r} → {after[cid].get(key)!r}")
    anchors_before, anchors_after = {a["id"]: a for a in old.anchors}, {a["id"]: a for a in new_.anchors}
    for aid in sorted(anchors_before.keys() | anchors_after.keys()):
        a, b = anchors_before.get(aid), anchors_after.get(aid)
        if a != b:
            changes.append(f"anchor {aid}: {'added' if not a else 'removed' if not b else 'changed'}")
    return changes
