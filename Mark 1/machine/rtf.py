"""Markdown to RTF, for readers who open things in Word: Times New Roman 12 throughout, Courier New for code.

Covers the Markdown Mark 1 writes: headings, paragraphs, bullet and numbered lists, tables, fenced and indented
code, quotes, bold, italic, inline code and links. The .md stays the source; the .rtf is its twin.
"""
import re
from pathlib import Path

HEADER = (r"{\rtf1\ansi\ansicpg1252\deff0{\fonttbl{\f0\froman\fcharset0 Times New Roman;}"
          r"{\f1\fmodern\fcharset0 Courier New;}}\f0\fs24")
PAGE_TWIPS = 9360  # 6.5 inches of text between one-inch margins
CELL_BORDER = r"\clbrdrt\brdrs\brdrw10\clbrdrl\brdrs\brdrw10\clbrdrb\brdrs\brdrw10\clbrdrr\brdrs\brdrw10"
PARTS = {"paper", "appendix", "ai-appendix", "materials", "provenance"}
SKIP_DIRS = {".venv", ".git", ".pytest_cache", "tests", "bundles", "__pycache__"}
SKIP_FILES = {"CLAUDE.md", "PENDING.md", "prompt.md", "transcript.md"}


def twin(md_path: Path) -> Path:
    out = md_path.with_suffix(".rtf")
    out.write_text(convert(md_path.read_text(encoding="utf-8")), encoding="ascii")
    return out


def twins(root: Path) -> list[Path]:
    """An .rtf beside every .md document under root, except code-facing files and the parts of research records,
    whose hashes must not change."""
    made = []
    for md in sorted(root.rglob("*.md")):
        rel = md.relative_to(root).parts
        if SKIP_DIRS & set(rel) or md.name in SKIP_FILES or _in_record_part(md):
            continue
        made.append(twin(md))
    return made


def _in_record_part(md: Path) -> bool:
    for parent in md.parents:
        if (parent / "record.yaml").exists():
            return md.relative_to(parent).parts[0] in PARTS
    return False


def convert(markdown: str) -> str:
    out = [HEADER]
    lines = markdown.replace("\r\n", "\n").split("\n")
    i = 0
    while i < len(lines):
        line = lines[i]
        if line.startswith("```"):
            i += 1
            while i < len(lines) and not lines[i].startswith("```"):
                out.append(_code_line(lines[i]))
                i += 1
            i += 1
            out.append(r"{\pard\sa160\par}")
        elif line.startswith("    ") and not _list_item(line):
            while i < len(lines) and (lines[i].startswith("    ") or not lines[i].strip()):
                if lines[i].strip():
                    out.append(_code_line(lines[i][4:]))
                i += 1
            out.append(r"{\pard\sa160\par}")
        elif line.lstrip().startswith("|"):
            rows = []
            while i < len(lines) and lines[i].lstrip().startswith("|"):
                rows.append(lines[i])
                i += 1
            out.append(_table(rows))
        elif heading := re.match(r"^(#{1,6})\s+(.*?)\s*(\{#[^}]*\})?\s*$", line):
            depth = len(heading.group(1))
            style = r"\b" if depth < 3 else r"\b\i"
            out.append(rf"{{\pard\sb{360 if depth == 1 else 240}\sa120\keepn{style} {_inline(heading.group(2))}\par}}")
            i += 1
        elif item := _list_item(line):
            indent, marker, text = item
            body, i = _continuation(lines, i + 1, text)
            label = r"\'95" if marker == "-" else marker
            out.append(rf"{{\pard\li{360 + 360 * indent}\fi-360\sa60 {label}\tab {_inline(body)}\par}}")
        elif line.startswith(">"):
            body, i = _continuation(lines, i + 1, line.lstrip("> "), quote=True)
            out.append(rf"{{\pard\li720\ri720\sa160\i {_inline(body)}\par}}")
        elif re.match(r"^\s*(-{3,}|\*{3,}|_{3,})\s*$", line) or not line.strip():
            i += 1
        else:
            body, i = _continuation(lines, i + 1, line.strip())
            out.append(rf"{{\pard\sa160 {_inline(body)}\par}}")
    out.append("}")
    return "\n".join(out)


def _list_item(line: str):
    m = re.match(r"^(\s*)(-|\*|\d+\.)\s+(.*)$", line)
    if not m or m.group(2) == "*" and not line.lstrip().startswith("* "):
        return None
    return len(m.group(1)) // 2, m.group(2).replace("*", "-"), m.group(3)


def _continuation(lines: list[str], i: int, first: str, quote: bool = False) -> tuple[str, int]:
    """Join the wrapped lines of one paragraph, list item or quote; stop at a blank line or a new block."""
    parts = [first]
    while i < len(lines):
        line = lines[i]
        if not line.strip() or _list_item(line) or line.lstrip().startswith(("|", "#", "```")) or \
                (quote != line.startswith(">")):
            break
        parts.append(line.lstrip("> ").strip())
        i += 1
    return " ".join(parts), i


def _table(rows: list[str]) -> str:
    cells = [[c.strip() for c in r.strip().strip("|").split("|")] for r in rows
             if not re.match(r"^\s*\|?\s*:?-{3,}", r)]
    if not cells:
        return ""
    ncols = max(len(r) for r in cells)
    width = PAGE_TWIPS // ncols
    edges = "".join(rf"{CELL_BORDER}\cellx{width * (n + 1)}" for n in range(ncols))
    out = []
    for n, row in enumerate(cells):
        row += [""] * (ncols - len(row))
        style = r"\b" if n == 0 else ""
        body = "".join(rf"{{\pard\intbl\sa0{style} {_inline(c)}\cell}}" for c in row)
        out.append(rf"\trowd\trgaph108{edges}{body}\row")
    return "\n".join(out) + r"{\pard\sa160\par}"


def _code_line(text: str) -> str:
    return rf"{{\pard\f1\fs20\sa0 {_escape(text)}\par}}"


def _inline(text: str) -> str:
    spans = []

    def hold(m):
        spans.append(m.group(1))
        return f"\x00{len(spans) - 1}\x00"

    text = re.sub(r"`([^`]+)`", hold, text)
    text = _escape(text)
    text = re.sub(r"\*\*(?=\S)(.+?)(?<=\S)\*\*", r"{\\b \1}", text)
    # a lone * opens italics only at a word boundary, so p* and pi* in formulas are left alone
    text = re.sub(r"(?<![\w*\\])\*(?=\S)([^*]+?)(?<=\S)\*(?![\w*])", r"{\\i \1}", text)
    text = re.sub(r"(?<!\w)_(?=\S)([^_]+?)(?<=\S)_(?!\w)", r"{\\i \1}", text)
    text = re.sub(r"\[([^\]]+)\]\((https?://[^)\s]+)\)", r"\1 ({\\f1 \2})", text)
    text = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", text)
    return re.sub("\x00(\\d+)\x00", lambda m: rf"{{\f1 {_escape(spans[int(m.group(1))])}}}", text)


def _escape(text: str) -> str:
    out = []
    for ch in text:
        if ch in "\\{}":
            out.append("\\" + ch)
        elif ord(ch) < 128:
            out.append(ch)
        elif ord(ch) <= 0xFFFF:
            code = ord(ch)
            out.append(rf"\u{code if code < 0x8000 else code - 0x10000}?")
        else:
            hi, lo = divmod(ord(ch) - 0x10000, 0x400)
            out.append(rf"\u{0xD800 + hi - 0x10000}?\u{0xDC00 + lo - 0x10000}?")
    return "".join(out)
