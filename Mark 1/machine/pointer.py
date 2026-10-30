"""Pointer grammar (protocol/formal.md#P9):

    paper/paper.md                 a whole file
    paper/paper.md#prop-1          a section, by explicit {#id} or heading slug
    paper/paper.md:L12-L14         a line range
    claims:C1  anchors:A2  derivations:D1   an entry in a record table
"""
import re
from dataclasses import dataclass

import yaml

from .record import Record

TABLES = {
    "claims": ("ai-appendix/claims.yaml", "claims"),
    "anchors": ("ai-appendix/anchors.yaml", "anchors"),
    "derivations": ("provenance/derivations.yaml", "derivations"),
}
TABLE_POINTER = re.compile(r"^(?P<table>claims|anchors|derivations):(?P<id>[\w-]+)$")
FILE_POINTER = re.compile(r"^(?P<file>[\w./-]+?)(?:#(?P<anchor>[\w.-]+)|:L(?P<start>\d+)(?:-L(?P<end>\d+))?)?$")
HEADING = re.compile(r"^(?P<hashes>#{1,6})\s+(?P<title>.*?)\s*(?:\{#(?P<id>[\w.-]+)\})?\s*$")
ENTRY_START = re.compile(r"^\s*-\s+id:")


class Unresolvable(ValueError):
    pass


@dataclass(frozen=True)
class Span:
    pointer: str
    file: str
    start: int
    end: int
    text: str

    def overlaps(self, other: "Span") -> bool:
        return self.file == other.file and self.start <= other.end and other.start <= self.end


def normalize(pointer: str) -> str:
    return pointer.strip().replace("\\", "/").removeprefix("./")


def is_wellformed(pointer: str) -> bool:
    p = normalize(pointer)
    return ".." not in p and bool(TABLE_POINTER.match(p) or FILE_POINTER.match(p))


def file_of(pointer: str) -> str:
    p = normalize(pointer)
    if m := TABLE_POINTER.match(p):
        return TABLES[m["table"]][0]
    return re.split(r"[#:]", p, maxsplit=1)[0]


def slug(title: str) -> str:
    return re.sub(r"[\s-]+", "-", re.sub(r"[^\w\s-]", "", title.lower())).strip("-")


def sections(text: str) -> set[str]:
    found = set()
    for line in text.splitlines():
        if m := HEADING.match(line):
            found |= {slug(m["title"])} | ({m["id"]} if m["id"] else set())
    return found


def resolve(record: Record, pointer: str) -> Span:
    p = normalize(pointer)
    if m := TABLE_POINTER.match(p):
        return _table_entry(record, p, m["table"], m["id"])
    m = FILE_POINTER.match(p)
    if not m or ".." in p:
        raise Unresolvable(f"malformed pointer {pointer!r}")
    rel = m["file"]
    if not record.path(rel).is_file():
        raise Unresolvable(f"{rel} is not in the record")
    lines = record.text(rel).splitlines()
    if m["anchor"]:
        start, end = _section(lines, m["anchor"], rel)
    elif m["start"]:
        start, end = int(m["start"]), int(m["end"] or m["start"])
        if not 1 <= start <= end <= len(lines):
            raise Unresolvable(f"{p}: {rel} has {len(lines)} lines")
    else:
        start, end = 1, len(lines)
    return Span(p, rel, start, end, "\n".join(lines[start - 1:end]))


def _section(lines: list[str], anchor: str, rel: str) -> tuple[int, int]:
    for i, line in enumerate(lines):
        m = HEADING.match(line)
        if m and anchor in (m["id"], slug(m["title"])):
            level = len(m["hashes"])
            end = next(
                (j for j in range(i + 1, len(lines)) if (h := HEADING.match(lines[j])) and len(h["hashes"]) <= level),
                len(lines),
            )
            return i + 1, end
    raise Unresolvable(f"no section #{anchor} in {rel}")


def _table_entry(record: Record, pointer: str, table: str, entry_id: str) -> Span:
    rel, key = TABLES[table]
    entry = next((e for e in record._entries(rel, key) if e.get("id") == entry_id), None)
    if entry is None:
        raise Unresolvable(f"no entry {entry_id} in {rel}")
    lines = record.text(rel).splitlines()
    id_line = re.compile(r"^\s*-?\s*id:\s*[\"']?" + re.escape(entry_id) + r"[\"']?\s*$")
    start = next((i for i, line in enumerate(lines, 1) if id_line.match(line)), 1)
    end = next((i - 1 for i, line in enumerate(lines[start:], start + 1) if ENTRY_START.match(line)), len(lines))
    return Span(pointer, rel, start, end, yaml.safe_dump(entry, sort_keys=False, allow_unicode=True).strip())
