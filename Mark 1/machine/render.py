"""Markdown views of the machine-readable outputs. The JSON/YAML files are the record; these are for people."""
from . import attribution

LEVELS = {1: "Level 1 · Form", 2: "Level 2 · Correspondence", 3: "Level 3 · Warrant (SIEVE)"}
ACTIONS = {
    "proceed_to_review": "proceed to review",
    "return_for_corrections": "return for corrections",
    "return_without_review": "return without review",
    "refer_to_specialist": "refer to a specialist",
}
KINDS = {
    "answer": "an answer: a new claim on a question already posed",
    "question": "a question: not posed before, with its first answer",
    "reading": "a reading: a question not posed before, answered by results in hand",
    "evidence": "evidence: new support for, or a new test of, a claim already stated",
    "none": "not new: established by prior work in the corpus",
    "uncovered": "the corpus does not cover the claim's area",
    "no_consensus": "no consensus across runs",
}


def findings(report) -> str:
    h = report.header
    v = h["versions"]
    models = ", ".join(_model(m) for m in h["models_used"]) or "deterministic checks only"
    out = [
        f"# Findings report · {h['paper_id']}",
        "",
        "Findings only: no verdict, score, ranking, or recommendation. Every finding points into the record "
        "and into the standard it was checked against.",
        "",
        "| | |",
        "|---|---|",
        f"| Run | `{h['run_id']}` |",
        f"| Run by | {h['actor']}" + (f", round {h['round']}" if h.get("round") else "") + " |",
        f"| Record | `sha256:{h['record_sha'][:16]}` |",
        f"| Versions | protocol {v['protocol']} · checks {v['checks']} · generator {v['generator']} · standard {v['standard']} |",
        f"| Check code | `{h['machine_sha']}` |",
        f"| Models | {models} |",
        f"| AI appendix | {h.get('ai_appendix', 'submitted')} |",
        f"| Generator stamp | {stamp_line(h.get('ai_appendix_stamp'))} |",
        f"| Bundles answered | {h['cost'].get('bundles', 0)} |",
        "",
    ]
    if h["agreement"]:
        out += ["| Model-judged check | Agreement | Minimum | Published as a check |", "|---|---|---|---|"]
        for check, a in h["agreement"].items():
            out.append(f"| {check} | {a['value']:.2f} | {a['min']:.2f} | {'yes' if a['met'] else 'no, below tolerance'} |")
        out.append("")
    for level, title in LEVELS.items():
        out += [f"## {title}", ""]
        rows = [f for f in report.findings if f.level == level]
        out += [block for f in rows for block in _finding(f)] or ["_No findings._", ""]
    if report.below_tolerance:
        out += ["## Below tolerance", "",
                "These came from a check whose agreement across runs fell below its published minimum. "
                "They are reported, not published as findings.", ""]
        out += [block for f in report.below_tolerance for block in _finding(f)]
    if h["checks_not_run"]:
        out += ["## Checks not run", ""] + [f"- **{c['check']}**: {c['reason']}" for c in h["checks_not_run"]] + [""]
    return "\n".join(out)


def _model(m: dict) -> str:
    return f"{m['model']} ({m['backend']}, {m['answers']} answers)"


def _finding(f) -> list[str]:
    tags = [f"`{f.finding_class}`"] + (["main claim"] if f.main else [])
    produced = (f"deterministic check `{f.check}` {f.check_version}, code `{f.model_version}`"
                if f.model == "deterministic"
                else f"{f.model} via prompt `{f.prompt_id}`, agreement {f.agreement}")
    lines = [f"### {f.id} · " + " · ".join(tags), "", f"**{f.statement}**", "",
             f"- Record: `{f.record_pointer}`", f"- Standard: `{f.standard_pointer}`"]
    if f.rationale:
        lines.append(f"- Why: {f.rationale}")
    lines.append(f"- Produced by: {produced}")
    if f.absent_from_author:
        lines.append("- Not in the author's own findings report")
    return lines + [""]


def perturbation(paper_id: str, rows: list[dict]) -> str:
    out = [f"# SIEVE · re-execution under perturbation · {paper_id}", "",
           "Each reproduction anchor re-run from the record at other points its derivation's assumptions admit "
           "(standard S9). An anchor holds when the record's procedure agrees, at every point, with a formula of the "
           "derivation that gives the anchor's value at the anchor's own point. Integer parameters stay integers.", "",
           "| Anchor | Derivation | Varied | Points | Result |", "|---|---|---|---|---|"]
    for row in rows:
        result = f"held, as {row['reading']}" if row["result"] == "held" else row["result"]
        out.append(f"| {row['anchor']} | {row['derivation'] or '—'} | {', '.join(row['varied']) or '—'} | "
                   f"{row['points'] or '—'} | {result.replace('|', '/')} |")
    out += ["", "## Notes", ""]
    out += [f"- **{row['anchor']}**: {row['detail']}." for row in rows]
    return "\n".join(out) + "\n"


def evidence_map(emap: dict) -> str:
    cov, corp = emap["coverage"], emap["corpus"]
    out = [
        f"# Evidence map · {emap['paper_id']}",
        "",
        "The contribution claim placed against the prior work the corpus reaches. The map informs the "
        "editor's signed judgment of what is new; it does not make it.",
        "",
        f"Run `{emap['run_id']}` · corpus `{corp['version'][:12]}` · {corp['items']} candidates"
        + (f" · {corp['procedure']}" if corp.get("procedure") else ""),
        "",
    ]
    for claim in emap["claims"]:
        out += [f"## {claim['claim_id']} · {KINDS.get(claim['newness_kind'], claim['newness_kind'])}", "",
                f"> {claim['text']}", ""]
        out += _question_lines(claim)
        out += [claim["rationale"], "", f"Agreement: {claim['agreement']}", ""]
        if claim["nearest"]:
            out += ["| Prior work | Relation | Basis | Poses the question | States the claim | What it establishes |",
                    "|---|---|---|---|---|---|"]
            out += [f"| {_cite(n)} | {n['relation']} | {n.get('basis', 'abstract or summary')} | "
                    f"{_yes_no(n, 'poses_question')} | {_yes_no(n, 'states_claim')} | {n['establishes']} |"
                    for n in claim["nearest"]]
            out.append("")
    out += ["## Coverage", "", cov["statement"], ""]
    if cited := cov.get("cited_but_not_retrieved") or cov.get("cited_but_not_in_corpus"):
        out += ["Cited by the paper, not among the candidates:", ""] + [f"- {c}" for c in cited] + [""]
    if cov.get("unresolved"):
        out += ["Hand-list entries that could not be enriched:", ""] + [f"- {c}" for c in cov["unresolved"]] + [""]
    return "\n".join(out)


def _question_lines(claim: dict) -> list[str]:
    """The question the claim was placed on, and whose statement of it that was (maps before checks 0.7.0 have none)."""
    q = claim.get("question")
    if not q:
        return []
    if q["stated_by"] == "author":
        lines = [f"The question it answers, as the paper states it (`{q['pointer']}`): {q['text']}"]
        if q.get("read_differently"):
            lines += ["", "Read otherwise in the answers: " + " / ".join(q["read_differently"])]
    elif q["stated_by"] == "model":
        lines = [f"The question it answers, as the model read it (the claims list states none): {q['text']}"]
    else:
        lines = ["The claims list states no question for this claim, and the answers named none."]
    return lines + [""]


def _cite(n: dict) -> str:
    return n["citation"] + (f" · [doi](https://doi.org/{n['doi']})" if n.get("doi") else "")


def _yes_no(n: dict, field: str) -> str:
    if field not in n:
        return "not asked"
    votes = n.get(f"{field}_votes")
    return ("yes" if n[field] else "no") + (f" ({votes})" if votes else "")


def comparison(paper_id: str, journal_run: str, author_run: str, absent: list, author_only: list) -> str:
    out = [f"# Journal run against the author's run · {paper_id}", "",
           f"Journal run `{journal_run}` · author run `{author_run}`", ""]
    out += ["## In the journal's report, not in the author's", ""]
    out += [f"- {f.id} `{f.finding_class}` at `{f.record_pointer}`: {f.statement}" for f in absent] or ["_None._"]
    out += ["", "## In the author's report, not in the journal's", ""]
    out += [f"- `{f.finding_class}` at `{f.record_pointer}`: {f.statement}" for f in author_only] or ["_None._"]
    return "\n".join(out + [""])


def decision(d: dict) -> str:
    out = [f"# Intake decision · {d['paper_id']}", "",
           f"**{ACTIONS[d['action']]}**, signed by {d['signature']['name']} at {d['signature']['at']}.", "",
           f"Standard action under the published mapping: {ACTIONS[d['standard_action']]}"
           f" (passes used: {d['passes_used']}).", ""]
    if d["fired_rules"]:
        out += ["| Rule | Finding | Class | Action | In the author's report |", "|---|---|---|---|---|"]
        out += [f"| {r['rule']} | {r['finding']} | {r['class']} | {ACTIONS[r['action']]} | "
                f"{'yes' if r.get('acknowledged') else 'no'} |" for r in d["fired_rules"]]
        out.append("")
    if d.get("findings_total"):
        n, total = len(d.get("acknowledged") or []), d["findings_total"]
        out += [(f"{n} of the {total} findings are in the author's own report, submitted with the package: "
                 "acknowledged at submission, they travel with the paper to review.") if n else
                f"None of the {total} findings is in the author's own report.", ""]
    if d["departure"]:
        out += [f"Departure ({d['departure']['direction'].replace('_', ' ')}): {d['departure']['reason']}", ""]
    if d.get("specialist"):
        out += [f"Referred to {d['specialist']}, who applies the mapping and returns the decision to this step.", ""]
    return "\n".join(out)


def return_note(paper_id: str, action: str, fired: list, report_path: str, signed_by: str,
                departure: dict | None = None) -> str:
    what = ("Correct the record and resubmit. This is not new work: fix the narrative to match the record, "
            "or the record if the record is wrong, then run the checks again."
            if action == "return_for_corrections"
            else "The record goes back unchanged. Strengthen the evidence or weaken the claims; a new submission "
                 "is new work.")
    out = [f"# Returned: {ACTIONS[action]} · {paper_id}", "", what, "",
           f"The findings behind this return are in `{report_path}`."]
    if fired:
        out += ["The rules that fired:", ""] + [f"- {r['rule']}: {r['finding']} (`{r['class']}`)" for r in fired]
    if departure:
        out += ["", f"The editor departed from the standard action ({departure['direction'].replace('_', ' ')}): "
                    f"{departure['reason']}"]
    return "\n".join(out + ["", f"Signed: {signed_by}. This note is a private communication to the author.", ""])


def revise_note(paper_id: str, round_: int, reports: list[str], reason: str, signed_by: str) -> str:
    return "\n".join([
        f"# Returned after review: revise and resubmit · {paper_id}", "",
        f"The reviewers of round {round_} ask for revisions. Revise the record, run the checks again, and resubmit: "
        f"the next submission is round {round_ + 1} of the same paper, checked and decided at intake again against the "
        "same review history, and "
        "the diff between rounds will show what changed and who changed it.", "",
        f"The editor's reason: {reason}", "",
        "The reviewers' reports:", "",
        *[f"- `{r}`" for r in reports], "",
        f"Signed: {signed_by}. This note is a private communication to the author.", ""])


def not_new_note(paper_id: str, prior: list[str], map_path: str, signed_by: str) -> str:
    return "\n".join([
        f"# Returned: not new · {paper_id}", "",
        f"The evidence map (`{map_path}`) shows this prior work establishing the contribution claim: "
        f"{', '.join(prior)}.", "",
        "The record goes back with the map. This produces no public object.", "",
        f"Signed: {signed_by}, after the author's answer to the map.", "",
    ])


def packet_readme(paper_id: str, round_: int, run_id: str) -> str:
    return "\n".join([
        f"# Reviewer packet · {paper_id}, round {round_}", "",
        "You are asked one question: is what this paper adds of interest to the community this journal serves, "
        "under `interest-criteria.md`?", "",
        "- `paper/` is the paper, written for people; `appendix/` is the appendix, for the reader who checks.",
        f"- `findings.md` is the machine's findings report from journal run `{run_id}`: form, correspondence and "
        "warrant, each finding with a pointer into the record and the standard.",
        "- `evidence-map.md` places the contribution claim against the corpus. An editor has already signed what "
        "is new, on this map.", "",
        "You are not asked to redo Levels 1 to 3. A review round is a question the author can answer within the "
        "existing record: a clarification, a reframed claim, an analysis on materials already there. A request "
        "that needs new materials is new work and a new submission.", "",
        "If you sign that the paper is of interest, your name goes on the certificate. A judgment that it is not "
        "produces no public object.", "",
    ])


def _declaration(e: dict) -> str:
    model = f" ({e['model_version']})" if e.get("model_version") else ""
    return f"- {e['tool']}{model}, {e['role']}, {e['date']}, on `{e['scope_pointer']}`: {e['human_direction']}"


def round_diff(paper_id: str, a: int, b: int, claim_changes: list[str], files: list[tuple[str, list[str]]],
               who: dict | None = None) -> str:
    first = not a
    out = [f"# What round {b} brought · {paper_id}" if first else
           f"# What changed between round {a} and round {b} · {paper_id}", "",
           f"Every file is new in round {b}; the record itself is in `rounds/r{b}/record/`. This page says who made "
           "each part." if first else "Read this instead of re-reading what did not change.", ""]
    if who:
        out += ["## Who made it" if first else "## Who changed it", "",
                "As the record declares it: the AI-use record names each use of AI and what it touched, and the "
                "generator stamp fingerprints what the published generator wrote. The record cannot prove who wrote "
                "what (appendix B.6); this table reads it, it does not verify it.", "",
                f"| File | {'Made' if first else 'Changed'} by | On what basis |", "|---|---|---|"]
        out += [f"| `{c['file']}` | {attribution.LABELS[c['by']]} | {c['basis'].replace('|', '/')} |"
                for c in who["changes"]] or ["| _no file changed_ | | |"]
        out += ["", f"**Declared in round {b}.** The AI-use entries that first appear in this round:", ""]
        out += [_declaration(e) for e in who.get("declared", [])] or [f"_No AI-use entry was added in round {b}._"]
        if who["declared_late"]:
            out += ["", f"**Declared late.** {len(who['declared_late'])} AI-use entr"
                        f"{'y' if len(who['declared_late']) == 1 else 'ies'} appear for the first time in round {b} "
                        f"but are dated before round {a} was submitted:", ""]
            out += [f"- {e['tool']}, {e['role']}, dated {e['date']}, on `{e['scope_pointer']}`" for e in who["declared_late"]]
        out.append("")
    if first:
        return "\n".join(out) + "\n"
    out += ["## Claims and anchors", ""]
    out += [f"- {c}" for c in claim_changes] or ["_No claim or anchor changed._"]
    out += ["", "## Files", ""]
    if not files:
        out.append("_No file changed._")
    for rel, lines in files:
        out += [f"### {rel}", "", "```diff", *lines, "```", ""]
    return "\n".join(out) + "\n"


def certificate(c: dict) -> str:
    v = c["versions"]
    return "\n".join([
        f"# Certificate · {c['title']}",
        "",
        f"The research record `{c['paper_id']}` (`sha256:{c['record_sha'][:16]}`) meets standard "
        f"{v['standard']} under protocol {v['protocol']}, checked by checks {v['checks']} and generator "
        f"{v['generator']} in journal run `{c['journal_run']['run_id']}` "
        f"({', '.join(c['journal_run']['models']) or 'deterministic'}).",
        "",
        f"**New**, as {KINDS[c['new']['kind']]}, signed by {c['new']['signed_by']} on the evidence map "
        f"(`{c['new']['evidence_map']}`).",
        "",
        f"**Of interest** to this community under criteria {c['interest']['criteria_version']}, signed by "
        f"{c['interest']['editor']} (editor), {c['interest']['reviewers'][0]} and {c['interest']['reviewers'][1]} (reviewers).",
        "",
        f"Data: materials {c['data']['materials_tier']}, verification {c['data']['verification'].replace('_', ' ')}.",
        "",
        f"AI use, as declared: {c['ai_use']['summary']}",
        "",
        f"Publication: {c['publication']['doi']}" + ("" if c["publication"]["minted"] else " (placeholder, not minted)"),
        "",
        f"Issued {c['issued_at']}. One certificate or nothing: there is no partial certificate.",
        "",
    ])


def stamp_line(s: dict | None) -> str:
    """The generator stamp as a fact (protocol P3): whether the AI appendix still matches it."""
    if not s or s.get("stamp") == "no AI appendix":
        return "no AI appendix"
    if s.get("stamp") == "none":
        return "none: the AI appendix was written without the reference generator, or its stamp was removed"
    head = f"generator {s.get('generator_version')}, run `{s.get('run_id')}`"
    if s.get("matches"):
        return f"matches: {head}"
    parts = []
    if s.get("inputs_changed_since"):
        parts.append("inputs changed since generation: " + ", ".join(s["inputs_changed_since"]))
    if s.get("outputs_edited_since"):
        parts.append("edited after generation: " + ", ".join(s["outputs_edited_since"]))
    return f"{head}; " + "; ".join(parts) + " (a fact, not a finding)"
