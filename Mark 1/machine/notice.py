"""The front notice (protocol P2, formal-0.3): before its first section, the paper says that an AI appendix exists
and where it is. `insert` is an author's helper, like `import-tex`; the author edits what it writes."""
from pathlib import Path

MARK = "**AI appendix.**"


def text(protocol_version: str, where: str = "`ai-appendix/` in its research record") -> str:
    # Facts only, addressed to no one: the injection screen (P12) reports text addressed to an evaluator, and
    # "for the reader that evaluates" was reported by all three completeness answers on 2026-10-27.
    return (f"{MARK} An AI appendix in the published form (record protocol {protocol_version}) accompanies this "
            f"paper at {where}: definitions, procedure, the claims list, the authors' stance, reproduction anchors, "
            "and scope.")


def insert(paper_md: Path, protocol_version: str) -> int:
    """Put the notice before the paper's first section. Returns the number of lines inserted, 0 if one is there."""
    raw = paper_md.read_text(encoding="utf-8")
    nl = "\r\n" if "\r\n" in raw else "\n"
    lines = raw.splitlines()
    for i, line in enumerate(lines):
        if line.lstrip("> ").startswith(MARK):
            if line == text(protocol_version):
                return 0
            lines[i] = text(protocol_version)  # an earlier wording is replaced in place, on the same line
            paper_md.write_text(nl.join(lines) + nl, encoding="utf-8")
            return 0
    at = next((i for i, line in enumerate(lines) if line.startswith("## ")), len(lines))
    block = [text(protocol_version), ""]
    lines[at:at] = block
    paper_md.write_text(nl.join(lines) + nl, encoding="utf-8")
    return len(block)
