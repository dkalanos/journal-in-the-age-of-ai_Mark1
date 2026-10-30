"""Level 1 · Form: does the record conform to the published protocol for its modality? (appendix C.2)"""
import re

import yaml

from .. import schemas
from ..findings import Finding
from ..pointer import file_of, is_wellformed, sections
from ..record import AI_APPENDIX_FILES
from ..util import load_json
from .base import PROTOCOL, Check, Context

REQUIRED_PARTS = ("paper", "appendix", "materials", "provenance", "declarations")
TABLES = (  # file, schema, protocol clause, required
    ("record.yaml", "record", "P1", True),
    ("declarations.yaml", "declarations", "P7", True),
    ("ai-appendix/claims.yaml", "claims", "P4", True),
    ("ai-appendix/anchors.yaml", "anchors", "P5", True),
    ("provenance/derivations.yaml", "derivations", "P6", True),
    ("provenance/ai-use.yaml", "ai-use", "P7", True),
    ("ai-appendix/generated.yaml", "generated", "P3", False),
)
SCOPE_SECTIONS = ("scope-and-choices", "choices", "does-not-claim")
FRONT_NOTICE = re.compile(r"^\s*>?\s*\*\*AI appendix[.:]?\*\*.*ai-appendix", re.IGNORECASE)  # P2, formal-0.3
NEEDS_DERIVATION = ("proposition", "comparative_static", "lemma")


def run(ctx: Context) -> list[Finding]:
    r = ctx.record
    found: list[Finding] = []

    def flag(pointer: str, statement: str, clause: str, rationale: str = "") -> None:
        found.append(Finding(level=1, check="form", finding_class="nonconformance", statement=statement,
                             record_pointer=pointer, standard_pointer=f"{PROTOCOL}#{clause}", rationale=rationale))

    parts = r.manifest.get("parts") or {}
    for part in REQUIRED_PARTS:
        rel = str(parts.get(part, part)).rstrip("/")
        if not r.exists(rel):
            flag("record.yaml", f"The record has no {part} part ({rel}).", "P1")

    for rel, schema, clause, required in TABLES:
        if not r.exists(rel):
            if required:
                flag(rel, f"{rel} is missing.", clause)
            continue
        try:
            data = r.table(rel)
        except yaml.YAMLError as e:
            flag(rel, f"{rel} is not valid YAML.", clause, str(e).splitlines()[0])
            continue
        if problems := schemas.errors(schema, data):
            flag(rel, f"{rel} does not conform to the {schema} schema.", clause, "; ".join(problems[:3]))

    for name in AI_APPENDIX_FILES:
        if name.endswith(".md") and not r.exists(f"ai-appendix/{name}"):
            flag(f"ai-appendix/{name}", f"The AI appendix lacks {name}.", "P3")

    appendix = [f for f in r.files("appendix") if f.endswith(".md")]
    missing = [s for s in SCOPE_SECTIONS if s not in sections("\n".join(r.text(f) for f in appendix))]
    if appendix and missing:
        flag(appendix[0], "The appendix has no scope-and-choices section in the protocol's form.", "P2",
             f"missing sections: {', '.join('#' + s for s in missing)}")

    _front_notice(r, flag)
    _claims(r, flag)
    _anchors(r, flag)
    _ai_use(ctx, flag)
    if ctx.actor == "journal":
        _submission(ctx, flag)
    return found


def _front_notice(r, flag) -> None:
    """P2: before its first section, the paper says that an AI appendix exists and where it is."""
    papers = [f for f in r.files("paper") if f.endswith(".md")]
    if not papers:
        return
    paper = "paper/paper.md" if "paper/paper.md" in papers else papers[0]
    head = []
    for line in r.text(paper).splitlines():
        if line.startswith("## "):
            break
        head.append(line)
    if not any(FRONT_NOTICE.match(line) for line in head):
        flag(paper, "The paper has no front notice saying that an AI appendix exists and where it is.", "P2",
             "expected before the first section: a paragraph beginning **AI appendix.** that names ai-appendix/")


def _claims(r, flag) -> None:
    claims = r.claims
    ids = [c.get("id") for c in claims]
    for dup in sorted({i for i in ids if ids.count(i) > 1}):
        flag(f"claims:{dup}", f"Claim id {dup} is used more than once.", "P4")
    if claims and not any(c.get("kind") == "contribution" for c in claims):
        flag("ai-appendix/claims.yaml", "The claims list has no contribution claim.", "P4")
    if claims and not any(c.get("main") for c in claims):
        flag("ai-appendix/claims.yaml", "No claim in the claims list is flagged main.", "P4")
    for c in claims:
        cid = c.get("id", "?")
        for key in ("pointer", "evidence_pointer", "question_pointer"):
            if c.get(key) and not is_wellformed(c[key]):
                flag(f"claims:{cid}", f"Claim {cid} has a malformed {key.replace('_', ' ')}: {c[key]!r}.", "P9")
        if c.get("kind") == "contribution" and not (c.get("question") and c.get("question_pointer")):
            flag(f"claims:{cid}", f"Contribution claim {cid} does not state the question it answers, or where the "
                                  "paper states it.", "P4")
        if c.get("derivation_id") and not r.derivation(c["derivation_id"]):
            flag(f"claims:{cid}", f"Claim {cid} names derivation {c['derivation_id']}, which the provenance "
                                  "does not contain.", "P6")
        if c.get("form") in NEEDS_DERIVATION and not c.get("derivation_id"):
            flag(f"claims:{cid}", f"Claim {cid} is a {c['form'].replace('_', ' ')} with no derivation in the "
                                  "provenance.", "P6")


def _anchors(r, flag) -> None:
    for a in r.anchors:
        aid = a.get("id", "?")
        if a.get("pointer") and not is_wellformed(a["pointer"]):
            flag(f"anchors:{aid}", f"Anchor {aid} has a malformed pointer: {a['pointer']!r}.", "P9")
        if a.get("claim_id") and not r.claim(a["claim_id"]):
            flag(f"anchors:{aid}", f"Anchor {aid} names claim {a['claim_id']}, which the claims list lacks.", "P5")
        if a.get("derivation_id") and not r.derivation(a["derivation_id"]):
            flag(f"anchors:{aid}", f"Anchor {aid} names derivation {a['derivation_id']}, which the provenance "
                                   "lacks.", "P5")
        procedure = a.get("procedure") or {}
        if procedure.get("language") == "python":
            file = procedure.get("source", "").partition(":")[0]
            if not file.startswith("materials/") or not r.path(file).is_file():
                flag(f"anchors:{aid}", f"Anchor {aid} runs {file or 'nothing'}, which is not a file in the "
                                       "materials.", "P5")


def _ai_use(ctx: Context, flag) -> None:
    r = ctx.record
    ai_use = r._mapping("provenance/ai-use.yaml")
    entries = [e for e in ai_use.get("entries") or [] if isinstance(e, dict)]
    recorded = {e.get("tool") for e in entries}
    declared = set((r.declarations.get("ai_use_summary") or {}).get("tools") or [])
    for tool in sorted(declared - recorded):
        flag("declarations.yaml", f"The declarations name AI tool {tool!r}, which the AI-use record does not "
                                  "account for.", "P7")
    for e in entries:
        pointer = e.get("scope_pointer", "")
        if pointer and (not is_wellformed(pointer) or not r.exists(file_of(pointer))):
            flag("provenance/ai-use.yaml", f"An AI-use entry points at {pointer!r}, which is not in the record.", "P7")
    stamp = r._mapping("ai-appendix/generated.yaml")
    run = ai_use.get("generator_run")
    if stamp and not ctx.generated_here:
        if not run:
            flag("provenance/ai-use.yaml", "The AI-use record does not record the generator run that produced "
                                           "the AI appendix.", "P7")
        elif (run.get("run_id"), run.get("generator_version")) != (stamp.get("run_id"), stamp.get("generator_version")):
            flag("provenance/ai-use.yaml", "The generator run in the AI-use record does not match the AI "
                                           "appendix stamp.", "P7",
                 f"AI-use record: {run.get('run_id')}; stamp: {stamp.get('run_id')}")
    history = r.manifest.get("working_history")
    if r.declarations.get("working_history_submitted") and not (history and r.exists(history)):
        flag("declarations.yaml", "The working history is declared as submitted but is not in the record.", "P7")


def _submission(ctx: Context, flag) -> None:
    sub, folder = ctx.submission, ctx.submission_dir
    report = folder / "author-report" / "findings.json" if folder else None
    if not sub or not report or not report.exists():
        flag("submission.yaml", "The submission carries no author findings report.", "P8")
        return
    try:
        author = load_json(report)
    except ValueError:
        author = {}
    if author.get("versions") != ctx.versions:
        flag("submission.yaml", "The author's findings report was produced with versions other than the "
                                "published ones.", "P8", f"author ran {author.get('versions')}")
    if author.get("record_sha") != sub.get("record_sha"):
        flag("submission.yaml", "The author's findings report was run on a different version of the record.", "P8")


CHECK = Check(name="form", level=1, deterministic=True, run=run)
