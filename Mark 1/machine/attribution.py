"""J2 · Who changed what between two submitted rounds, as far as the record says.

The record cannot prove who wrote what (appendix E.5). What it does say, it says in two places: the AI-use record
declares each use of AI and the part of the record it touched, and the generator stamp fingerprints every file the
published generator wrote. Each changed file is attributed from those two, and every attribution names its basis,
so a reader can tell a declaration from an inference. A file of the AI appendix that no longer matches its
stamp is then read against the AI-use record like any other file; "edited after generation" is what is left
when nothing declares the edit.
"""
from .pointer import file_of, is_wellformed
from .record import HASHED_PARTS, Record
from .util import sha256_file

LABELS = {
    "generator": "the published generator",
    "edited_after_generation": "edited after generation",
    "ai": "AI, declared",
    "undeclared": "not declared this round",
    "author": "the author",
    "ai_use_record": "the AI-use record itself",
}


def attribute(old: Record | None, new: Record, since: str | None = None) -> dict:
    """old: the previous round's record, or None for a first submission, where every file is new.
    since: when the earlier round was submitted; a declaration first made now but dated before it is backdated."""
    before = _entries(old)
    added = [e for e in _entries(new) if e not in before]
    stamp = new._mapping("ai-appendix/generated.yaml")
    rerun = _generator_run(old) != _generator_run(new)
    changes = [{"file": rel, **_who(rel, new, added, before, stamp, rerun)} for rel in changed_files(old, new)]
    late = [e for e in added if since and _dated_before(str(e.get("date", "")), since)]
    return {"changes": changes, "declared": [_entry(e) for e in added], "declared_late": [_entry(e) for e in late]}


def changed_files(old: Record | None, new: Record) -> list[str]:
    files = {rel for rec in (old, new) if rec for part in HASHED_PARTS for rel in rec.files(part)}
    return sorted(rel for rel in files if _sha(old, rel) != _sha(new, rel))


def _who(rel: str, new: Record, added: list[dict], before: list[dict], stamp: dict, rerun: bool) -> dict:
    if rel == "provenance/ai-use.yaml":
        what = [f"{len(added)} entr{'y' if len(added) == 1 else 'ies'} added or revised"] if added else []
        if rerun:
            what.append(f"the generator run it records is now {_generator_run(new) or 'none'}")
        return {"by": "ai_use_record", "basis": "; ".join(what or ["reworded"]) + "; the declarations are the author's"}
    off_stamp = ""  # for a file of the AI appendix: what the generator stamp says, before the AI-use record is read
    if rel.startswith("ai-appendix/"):
        run = stamp.get("run_id", "?")
        if rel == "ai-appendix/generated.yaml":
            return {"by": "generator", "basis": f"the stamp written by generator run {run}"}
        if (stamp.get("outputs") or {}).get(rel) == _sha(new, rel):
            return {"by": "generator", "basis": f"matches the stamp of generator run {run}"}
        off_stamp = f"does not match the stamp of generator run {run}; "
    if declared := [e for e in added if _covers(e, rel)]:
        return {"by": "ai", "basis": off_stamp + "; ".join(_describe(e) for e in declared)}
    if earlier := [e for e in before if _covers(e, rel)]:
        named = ", ".join(sorted({f"{e.get('tool')} ({e.get('role')})" for e in earlier}))
        return {"by": "undeclared", "basis": f"{off_stamp}no AI use is declared for this round; earlier rounds declare "
                                             f"{named} on this file"}
    if off_stamp:
        return {"by": "edited_after_generation", "basis": off_stamp + "nothing in the record says who edited it"}
    return {"by": "author", "basis": "no AI use is declared for this file"}


def _covers(entry: dict, rel: str) -> bool:
    scope = str(entry.get("scope_pointer", ""))
    target = file_of(scope) if is_wellformed(scope) else scope
    return rel == target or rel.startswith(target.rstrip("/") + "/")


def _entry(e: dict) -> dict:
    return {"tool": e.get("tool"), "model_version": e.get("model_version"), "role": e.get("role"),
            "scope_pointer": e.get("scope_pointer"), "date": str(e.get("date")),
            "human_direction": str(e.get("human_direction") or "").strip()}


def _describe(entry: dict) -> str:
    model = f" ({entry['model_version']})" if entry.get("model_version") else ""
    return f"{entry.get('tool')}{model}, {entry.get('role')}, {entry.get('date')}: {entry.get('human_direction', '').strip()}"


def _dated_before(date: str, since: str) -> bool:
    # a declared date may be a month ("2026-08") or a day; compare at the precision it was given
    return bool(date) and date < since[:len(date)]


def _generator_run(record: Record | None) -> str | None:
    if not record:
        return None
    return (record._mapping("provenance/ai-use.yaml").get("generator_run") or {}).get("run_id")


def _entries(record: Record | None) -> list[dict]:
    if not record:
        return []
    return [e for e in record._mapping("provenance/ai-use.yaml").get("entries") or [] if isinstance(e, dict)]


def _sha(record: Record | None, rel: str) -> str | None:
    path = record.path(rel) if record else None
    return sha256_file(path) if path and path.is_file() else None
