"""M0 · The published generator: the paper, appendix and provenance in; the AI appendix out (v4 deck, Fig. 4a).

The schema-bound parts come from a model under the published prompt. The author's own words in the
appendix's scope-and-choices section become parts 4 and 6 verbatim; they are never generated.
"""
from pathlib import Path

from . import paths
from .llm import Backend, channel
from .llm.agreement import jaccard, mean_pairwise_jaccard
from .pointer import Unresolvable, normalize, resolve
from .record import AI_APPENDIX_FILES, Record
from .util import dump_yaml, load_yaml, now, sha256_file, write_text


def input_files(record: Record) -> list[str]:
    extra = [rel for rel in ("declarations.yaml", "provenance/derivations.yaml") if record.exists(rel)]
    return record.files("paper") + record.files("appendix") + extra + record.files("materials")


def input_hashes(record: Record) -> dict[str, str]:
    return {rel: sha256_file(record.path(rel)) for rel in input_files(record)}


def prompt_data(record: Record) -> str:
    return channel(record, input_files(record))


def claim_signature(claim: dict) -> tuple[str, str, bool, str]:
    return claim.get("kind", ""), claim.get("form") or "", bool(claim.get("main")), normalize(claim.get("pointer", ""))


def claim_signatures(claims: list[dict]) -> set[tuple]:
    return {claim_signature(c) for c in claims}


def generate(record: Record, backend: Backend, versions: dict, k: int, out_dir: Path, run_id: str) -> dict:
    instructions = (paths.journal() / "checks" / "prompts" / "generate.md").read_text(encoding="utf-8")
    answers = backend.ask("generate", instructions, prompt_data(record), "payload-generate", k)
    signatures = [claim_signatures(a.payload["claims"]) for a in answers]
    # the answer closest to the other k-1 becomes the AI appendix; ties go to the first
    chosen = max(range(len(answers)), key=lambda i: sum(jaccard(signatures[i], s) for s in signatures))
    write(out_dir, answers[chosen].payload, record)
    stamp = {
        "generator_version": versions["generator"],
        "run_id": run_id,
        "models": sorted({a.model for a in answers}),
        "inputs": input_hashes(record),
        "outputs": {f"ai-appendix/{name}": sha256_file(out_dir / name) for name in AI_APPENDIX_FILES},
        "agreement": round(mean_pairwise_jaccard(signatures), 3),
        "generated_at": now(),
    }
    dump_yaml(stamp, out_dir / "generated.yaml")
    return stamp


def write(out_dir: Path, payload: dict, record: Record) -> None:
    write_text(out_dir / "definitions.md", definitions_md(payload["definitions"]))
    write_text(out_dir / "procedure.md", "# Procedure\n\n"
               + "\n".join(f"{i}. {step}" for i, step in enumerate(payload["procedure"], 1)) + "\n")
    dump_yaml({"claims": payload["claims"]}, out_dir / "claims.yaml")
    dump_yaml({"anchors": payload["anchors"]}, out_dir / "anchors.yaml")
    stance, scope = carried_sections(record)
    write_text(out_dir / "stance.md", stance)
    write_text(out_dir / "scope.md", scope)


def definitions_md(definitions: list[dict]) -> str:
    lines = ["# Definitions of record", ""]
    for d in definitions:
        line = f"- **{d['term']}**"
        if d.get("formula"):
            line += f" — `{d['formula']}`."
        line += f" {d['definition'].strip()}"
        if d.get("not_to_be_confused_with"):
            line += f" Not to be confused with: {d['not_to_be_confused_with'].strip().rstrip('.')}."
        lines.append(line)
    return "\n".join(lines) + "\n"


def carried_sections(record: Record) -> tuple[str, str]:
    out = []
    for anchor, title in (("choices", "The authors' stance"), ("does-not-claim", "Scope and do-nots")):
        span = None
        for rel in record.files("appendix"):
            try:
                span = resolve(record, f"{rel}#{anchor}")
                break
            except Unresolvable:
                continue
        if span:
            body = "\n".join(span.text.splitlines()[1:]).strip()
            out.append(f"# {title}\n\nCarried verbatim from `{span.pointer}`; the generator does not write this part.\n\n{body}\n")
        else:
            out.append(f"# {title}\n\nThe appendix has no `#{anchor}` section to carry.\n")
    return out[0], out[1]


def restamp(record: Record) -> None:
    """Refresh carried sections and the stamp after an edit made on the generator's behalf (defect injection)."""
    stance, scope = carried_sections(record)
    write_text(record.ai_dir / "stance.md", stance)
    write_text(record.ai_dir / "scope.md", scope)
    stamp = load_yaml(record.ai_dir / "generated.yaml")
    stamp["inputs"] = input_hashes(record)
    stamp["outputs"] = {f"ai-appendix/{name}": sha256_file(record.ai_dir / name) for name in AI_APPENDIX_FILES}
    dump_yaml(stamp, record.ai_dir / "generated.yaml")


def record_run(record: Record, stamp: dict) -> None:
    """The author's generator run goes into the author's AI-use record."""
    path = record.path("provenance/ai-use.yaml")
    ai_use = load_yaml(path) or {}
    ai_use["generator_run"] = {"generator_version": stamp["generator_version"], "run_id": stamp["run_id"]}
    dump_yaml(ai_use, path)


def stamp_status(record: Record, versions: dict) -> dict:
    """Whether the AI appendix still matches its generator stamp: a fact on the report, never a finding (P3, formal-0.3)."""
    if not record.has_ai_appendix():
        return {"stamp": "no AI appendix", "matches": None}
    stamp = record._mapping("ai-appendix/generated.yaml")
    if not stamp:
        return {"stamp": "none", "matches": None,
                "note": "the AI appendix was written without the reference generator, or its stamp was removed"}
    current, recorded = input_hashes(record), stamp.get("inputs") or {}
    inputs_changed = sorted(rel for rel in current.keys() | recorded.keys() if current.get(rel) != recorded.get(rel))
    outputs_edited = sorted(rel for rel, sha in (stamp.get("outputs") or {}).items()
                            if not record.exists(rel) or sha256_file(record.path(rel)) != sha)
    return {"stamp": "present", "generator_version": stamp.get("generator_version"),
            "published_generator": versions["generator"], "run_id": stamp.get("run_id"),
            "matches": not inputs_changed and not outputs_edited,
            "inputs_changed_since": inputs_changed, "outputs_edited_since": outputs_edited}
