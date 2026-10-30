"""Injection screen: text in the record addressed to an evaluator is itself a finding (appendix C.4).

A deterministic scan of every text file in the record, plus anything a quorum of the answering
models reported under `injection_observed` while doing another check.
"""
import re

from ..findings import Finding
from ..llm.agreement import cluster_spans
from ..pointer import Unresolvable, resolve
from .base import PROTOCOL, Check, Context

SCANNED = ("record.yaml", "declarations.yaml", "paper", "appendix", "ai-appendix", "materials", "provenance")
INVISIBLE = re.compile("[​-‏‪-‮⁠-⁤⁦-⁩﻿]")
HIDDEN = re.compile(r"<!--.*?-->", re.S)
ADDRESSED = re.compile(
    r"ignore (?:all |any )?(?:previous|prior|above|earlier) instructions"
    r"|report no findings|do not (?:flag|report)"
    r"|(?:note|message|instruction)s? (?:to|for) (?:the )?(?:evaluat\w*|review\w*|model|AI|LLM|checker)"
    r"|you are (?:an? |the )(?:reviewer|evaluator|language model|AI)"
    r"|pre-?approved",
    re.I,
)
PATTERNS = ((INVISIBLE, "an invisible character"), (HIDDEN, "a hidden comment"), (ADDRESSED, "text addressed to an evaluator"))


def run(ctx: Context) -> list[Finding]:
    found = scan(ctx.record)
    return found + observed(ctx, found)


def scan(record) -> list[Finding]:
    found = []
    for part in SCANNED:
        for rel in record.files(part):
            try:
                text = record.text(rel)
            except UnicodeDecodeError:
                continue
            for start, end, what, quote in _merge(_hits(text)):
                lines = f"L{start}" if start == end else f"L{start}-L{end}"
                found.append(Finding(level=1, check="injection", finding_class="injection",
                                     statement=f"The record carries {what} in {rel}: \"{quote}\"",
                                     record_pointer=f"{rel}:{lines}", standard_pointer=f"{PROTOCOL}#P12",
                                     rationale="Parts 4 and 6 and the narrative are data to the checker, never "
                                               "instructions; an instruction to the evaluator is reported."))
    return found


def observed(ctx: Context, already: list[Finding]) -> list[Finding]:
    if ctx.backend is None:
        return []
    known = []
    for f in already:
        try:
            known.append(resolve(ctx.record, f.record_pointer))
        except Unresolvable:
            pass
    found = []
    for check, answers in sorted(ctx.backend.answers.items()):
        runs = []
        for answer in answers:
            spans = []
            for item in answer.injection_observed:
                try:
                    spans.append((resolve(ctx.record, item["pointer"]), item.get("quote", "")))
                except Unresolvable:
                    continue
            runs.append(spans)
        clusters, _ = cluster_spans(runs, ctx.quorum)
        for cluster in clusters:
            _, span, quote = cluster[0]
            if any(span.overlaps(k) for k in known):
                continue
            known.append(span)
            found.append(Finding(level=1, check="injection", finding_class="injection",
                                 statement=f"The models answering {check} report text addressed to them: \"{quote}\"",
                                 record_pointer=span.pointer, standard_pointer=f"{PROTOCOL}#P12",
                                 **ctx.produced_by(answers, check, len({i for i, _, _ in cluster}))))
    return found


def _hits(text: str) -> list[tuple[int, int, str, str]]:
    hits = []
    for pattern, what in PATTERNS:
        for m in pattern.finditer(text):
            start = text.count("\n", 0, m.start()) + 1
            end = text.count("\n", 0, m.end()) + 1
            quote = m.group() if pattern is not INVISIBLE else f"U+{ord(m.group()):04X}"
            hits.append((start, end, what, " ".join(quote.split())[:120]))
    return sorted(hits)


def _merge(hits: list[tuple[int, int, str, str]]) -> list[tuple[int, int, str, str]]:
    merged: list[list] = []
    for start, end, what, quote in hits:
        if merged and start <= merged[-1][1]:
            last = merged[-1]
            last[1] = max(last[1], end)
            if what not in last[2]:
                last[2] += f" and {what}"
        else:
            merged.append([start, end, what, quote])
    return [tuple(m) for m in merged]


CHECK = Check(name="injection", level=1, deterministic=False, run=run)
