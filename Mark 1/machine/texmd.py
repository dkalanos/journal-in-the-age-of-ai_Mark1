"""TeX in, the protocol's Markdown out (protocol/formal.md#P2), for a paper that exists as LaTeX.

Sections, theorem-like environments, labelled paragraphs and proofs become headings with explicit ids, so claims
can point at them. Mathematics is kept as written. Citations are resolved from the .bib and listed under
`#references`. What cannot be carried, a TikZ drawing, is said in place. The result is a starting point for the
author to read and edit, not a submission; `mark1 import-tex` prints what it dropped and what it could not resolve.
"""
import re
from dataclasses import dataclass, field
from pathlib import Path

from .pointer import slug

MATH = re.compile(r"\$\$.*?\$\$|\\\[.*?\\\]|\\\(.*?\\\)"
                  r"|\\begin\{(equation\*?|align\*?|gather\*?|multline\*?)\}.*?\\end\{\1\}|(?<!\\)\$[^$]+?\$", re.S)
BS = "\x00BS\x00"  # a TeX line break, taken out before math is found so that `\\$x$` and `\\[1em]` read correctly
STRUCT = re.compile(r"\\(?P<edge>begin|end)\{(?P<env>[A-Za-z*]+)\}"
                    r"|\\(?P<sec>section|subsection|subsubsection|paragraph)\*?\s*\{"
                    r"|\\(?P<cmd>appendix|maketitle|item|bibliography|bibliographystyle)\b")
INLINE = re.compile(r"\\(?P<cmd>[A-Za-z]+\*?)|(?P<tilde>~)|(?P<dash>---|--)|(?P<quote>``|'')")
FIELD = re.compile(r"\s*(\w+)\s*=\s*")
ESCAPES = {"&": "&", "%": "%", "_": "_", "#": "#", "{": "{", "}": "}", "$": "$", ",": " ", ";": " ", " ": " "}
TEXT = {"emph": "*", "textit": "*", "textbf": "**", "texttt": "`", "text": ""}
DROP = {"noindent", "medskip", "smallskip", "bigskip", "newpage", "clearpage", "centering", "raggedright",
        "arraybackslash", "small", "footnotesize", "scriptsize", "normalsize", "leavevmode", "hfill", "indent",
        "par", "protect", "onehalfspacing", "singlespacing", "relax", "qedhere"}
SKIP_ARG = {"caption", "thanks", "vspace", "hspace", "setlength", "input", "include", "usetikzlibrary", "label"}
SYMBOLS = {"ldots": "…", "dots": "…", "textendash": "–", "textemdash": "—", "qed": "∎", "square": "∎"}
SECTION_LEVEL = {"section": 2, "subsection": 3, "subsubsection": 4}
LISTS = ("enumerate", "itemize", "description")
QUIET_ENVS = ("center", "quote", "quotation", "flushleft", "flushright", "minipage")
PH = "\x00{}{}\x00"  # placeholders survive every text transform and are restored last


@dataclass
class Theorem:
    title: str
    counter: str | None  # None: unnumbered
    reset: str | None


@dataclass
class Label:
    text: str  # how a cross-reference reads: "Proposition 4.2", "Figure 1", or a paragraph's title
    id: str | None  # heading id it links to; None for equations, figures and tables
    file: str  # paper or appendix
    quoted: bool = False  # paragraph titles read as “…” and keep their case


@dataclass
class Result:
    paper: str
    appendix: str
    labels: dict[str, Label]
    log: list[str] = field(default_factory=list)


def convert(tex: str, bib: str = "", choices: list[str] = (), does_not_claim: list[str] = ()) -> Result:
    return Converter(tex, bib).run(list(choices), list(does_not_claim))


class Converter:
    def __init__(self, tex: str, bib: str):
        self.src = tex
        self.bib = parse_bib(bib)
        self.theorems = theorem_kinds(tex)
        self.math: list[str] = []
        self.refs: list[tuple[str, str]] = []  # (label, how) per cross-reference placeholder
        self.labels: dict[str, Label] = {}
        self.equations = 0
        self.counters: dict[str, int] = {}
        self.figures = self.tables = 0
        self.section_no: int | str = 0
        self.subsection_no = 0
        self.in_appendix = False
        self.level = 1  # heading level of the innermost open section
        self.stack: list[dict] = []  # open environments
        self.last_theorem: tuple[str, int] | None = None
        self.lstrip_next = False
        self.last_list_n = 0
        self.ids: set[str] = set()
        self.cited: set[str] = set()
        self.notes: dict[str, list[str]] = {"paper": [], "appendix": []}
        self.out: dict[str, list[str]] = {"paper": [], "appendix": []}
        self.log: list[str] = []
        self.unknown: dict[str, int] = {}

    # ----- driver -------------------------------------------------------------------------------------------

    @property
    def here(self) -> str:
        return "appendix" if self.in_appendix else "paper"

    def emit(self, text: str) -> None:
        self.out[self.here].append(text)

    def trim(self) -> None:
        buf = self.out[self.here]
        while buf and not buf[-1].strip():
            buf.pop()
        if buf:
            buf[-1] = buf[-1].rstrip()

    def run(self, choices: list[str], does_not_claim: list[str]) -> Result:
        body = self.src[self.src.index(r"\begin{document}") + len(r"\begin{document}"):]
        body = body[:body.index(r"\end{document}")] if r"\end{document}" in body else body
        comments = len(re.findall(r"(?m)^\s*%.*$", body))
        body = re.sub(r"(?<!\\)%.*", "", body)
        body = re.sub(r"\\hfill\s*\$\\square\$", " ∎", body)
        self.walk(self.protect_math(body))
        if comments:
            self.log.append(f"{comments} comment line(s) dropped; comments are not part of the paper")
        paper = self.assemble("paper")
        self.in_appendix = True
        self.scope_section(paper, choices, does_not_claim)
        appendix = self.assemble("appendix")
        for name, n in sorted(self.unknown.items()):
            self.log.append(f"\\{name} left as written ({n})")
        return Result(self.restore(paper, "paper"), self.restore(appendix, "appendix"), self.labels, self.log)

    def walk(self, text: str) -> None:
        pos = 0
        while m := STRUCT.search(text, pos):
            self.prose(text[pos:m.start()])
            pos = m.end()
            if m["sec"]:
                title, pos = arg(text, pos - 1)
                label, pos = label_after(text, pos)
                self.heading_command(m["sec"], title, label)
            elif m["cmd"] == "item":
                marker, pos = opt(text, pos)
                self.item(marker)
            elif m["cmd"] == "maketitle":
                self.title_block()
            elif m["cmd"] == "appendix":
                self.in_appendix, self.section_no = True, 0
            elif m["cmd"] == "bibliography":
                _, pos = arg(text, pos)
                self.references()
            elif m["cmd"] == "bibliographystyle":
                _, pos = arg(text, pos)
            elif m["edge"] == "begin":
                pos = self.begin(m["env"], text, pos)
            else:
                self.end(m["env"])
        self.prose(text[pos:])

    # ----- structure ----------------------------------------------------------------------------------------

    def heading(self, level: int, shown: str, hid: str | None = None, label: str | None = None,
                ref_text: str | None = None, quoted: bool = False) -> str:
        shown = " ".join(shown.split())
        hid = self.unique(hid or slug(plain(shown)))
        self.emit(f"\n\n{'#' * min(level, 6)} {shown} {{#{hid}}}\n\n")
        if label:
            self.labels[label] = Label(ref_text or plain(shown), hid, self.here, quoted)
        return hid

    def unique(self, hid: str) -> str:
        candidate, n = hid or "section", 2
        while candidate in self.ids:
            candidate, n = f"{hid}-{n}", n + 1
        self.ids.add(candidate)
        return candidate

    def heading_command(self, kind: str, title: str, label: str | None) -> None:
        text = self.inline(title).strip()
        hid = label.replace(":", "-") if label else slug(plain(text))
        if kind == "paragraph":
            text = text.rstrip(".")
            self.heading(self.level + 1, text, hid, label, plain(text), quoted=True)
            return
        level = SECTION_LEVEL[kind]
        if level == 2:
            self.section_no = self.next_section()
            self.subsection_no = 0
            for kind_ in self.theorems.values():
                if kind_.reset == "section":
                    self.counters[kind_.counter] = 0
            number = f"{self.section_no}"
        elif level == 3:
            self.subsection_no += 1
            number = f"{self.section_no}.{self.subsection_no}"
        else:
            number = ""
        self.level = level
        shown = f"{number}. {text}" if level == 2 else f"{number} {text}" if number else text
        word = "Appendix" if self.in_appendix and level == 2 else "Section"
        self.heading(level, shown, hid, label, f"{word} {number}" if number else plain(text))

    def next_section(self) -> int | str:
        if self.in_appendix:
            return "A" if not isinstance(self.section_no, str) else chr(ord(self.section_no) + 1)
        return int(self.section_no) + 1

    def begin(self, env: str, text: str, pos: int) -> int:
        if env in self.theorems:
            title, pos = opt(text, pos)
            label, pos = label_after(text, pos)
            kind = self.theorems[env]
            name = f"{kind.title} {self.number(kind)}".strip()
            shown = f"{name} ({self.inline(title).strip()})" if title else name
            level = self.level + 1
            hid = self.heading(level, shown, label.replace(":", "-") if label else None, label, name)
            self.stack.append({"env": env, "level": level, "id": hid})
        elif env == "proof":
            title, pos = opt(text, pos)
            level = self.last_theorem[1] + 1 if self.last_theorem else self.level + 1
            shown = self.inline(title).strip().rstrip(".") if title else "Proof"
            hid = f"proof-{self.last_theorem[0]}" if self.last_theorem and not title else None
            self.heading(level, shown, hid)
            self.stack.append({"env": "proof"})
        elif env in LISTS:
            opts, pos = opt(text, pos)
            style = "alph" if r"\alph*" in opts else "roman" if r"\roman*" in opts else "arabic"
            start = re.search(r"start\s*=\s*(\d+)", opts)
            n = int(start[1]) - 1 if start else self.last_list_n if "resume" in opts else 0
            self.stack.append({"env": env, "style": style, "n": n, "first": True})
            self.emit("\n")
        elif env == "abstract":
            self.heading(2, "Abstract")
        elif env in ("figure", "figure*", "table", "table*"):
            end = text.index(f"\\end{{{env}}}", pos)
            (self.figure if env.startswith("figure") else self.table)(text[pos:end])
            return end + len(f"\\end{{{env}}}")
        elif env == "tikzpicture":
            end = text.index(r"\end{tikzpicture}", pos)
            self.emit("\n*(A TikZ drawing stands here in the TeX source; it is not carried into the record.)*\n")
            self.log.append("a TikZ drawing outside any figure was dropped")
            return end + len(r"\end{tikzpicture}")
        else:
            if env not in QUIET_ENVS:
                self.unknown[f"begin{{{env}}}"] = self.unknown.get(f"begin{{{env}}}", 0) + 1
            self.stack.append({"env": env})
        return pos

    def end(self, env: str) -> None:
        open_ = self.stack.pop() if self.stack and self.stack[-1]["env"] == env else None
        if env in self.theorems and open_:
            self.last_theorem = (open_["id"], open_["level"])
            self.emit("\n\n")
        elif env == "proof":
            self.trim()
            self.emit(" ∎\n\n")
        elif env in LISTS:
            self.last_list_n = open_["n"] if open_ else 0
            self.trim()
            self.emit("\n\n")

    def item(self, marker: str) -> None:
        lst = next((s for s in reversed(self.stack) if s["env"] in LISTS), None)
        if not lst:
            self.emit("\n- ")
            return
        lst["n"] += 1
        n = lst["n"]
        if marker:
            shown = f"- **{self.inline(marker).strip()}**"
        elif lst["env"] != "enumerate":
            shown = "-"
        elif lst["style"] == "roman":
            shown = f"- ({roman(n)})"
        elif lst["style"] == "alph":
            shown = f"- ({chr(96 + n)})"
        else:
            shown = f"{n}."
        self.trim()
        self.emit(f"{chr(10) * (2 if lst['first'] else 1)}{shown} ")
        lst["first"] = self.lstrip_next = False
        self.lstrip_next = True

    def number(self, kind: Theorem) -> str:
        if not kind.counter:
            return ""
        self.counters[kind.counter] = self.counters.get(kind.counter, 0) + 1
        n = self.counters[kind.counter]
        return f"{self.section_no}.{n}" if kind.reset == "section" else str(n)

    def title_block(self) -> None:
        title, author, date = (preamble_arg(self.src, name) for name in ("title", "author", "date"))
        thanks = ""
        if m := re.search(r"\\thanks\s*\{", title):
            thanks, end = arg(title, m.end() - 1)
            title = title[:m.start()] + title[end:]
        title = plain(self.inline(self.protect_math(title)).replace("**", ""))
        date = self.inline(re.sub(r"\\\\(\[[^]]*\])?", " ", date))
        date = re.sub(r"\s*[—–-]+\s*", " — ", date).strip(" —")
        self.emit(f"# {' '.join(title.split())}\n\n{' · '.join(filter(None, [self.inline(author).strip(), date]))}\n\n")
        if thanks:
            self.emit(f"*{self.inline(thanks).strip()}*\n\n")

    def figure(self, block: str) -> None:
        self.figures += 1
        caption, label = caption_and_label(block)
        if label:
            self.labels[label] = Label(f"Figure {self.figures}", None, self.here)
        drawn = "a TikZ drawing" if r"\begin{tikzpicture}" in block else "an included graphic"
        self.emit(f"\n> **Figure {self.figures}.** {self.inline(caption).strip().replace(chr(10), chr(10) + '> ')}\n>\n"
                  f"> *(The figure is {drawn} in the TeX source and is not carried into the record.)*\n\n")
        self.log.append(f"figure {self.figures}: {drawn} dropped, caption kept")

    def table(self, block: str) -> None:
        self.tables += 1
        caption, label = caption_and_label(block)
        if label:
            self.labels[label] = Label(f"Table {self.tables}", None, self.here)
        rows: list[list[str]] = []
        if m := re.search(r"\\begin\{(tabular[xy]?)\}", block):
            pos = m.end()
            for _ in range(2 if m[1] != "tabular" else 1):
                _, pos = arg(block, pos)
            end = block.index(f"\\end{{{m[1]}}}", pos)
            inner = re.sub(r"\\(toprule|midrule|bottomrule|addlinespace|hline|cline\{[^}]*\})", "", block[pos:end])
            for raw in re.split(re.escape(BS) + r"|\\\\", inner):
                cells = [" ".join(self.inline(c).split()).replace("|", "\\|") for c in raw.split("&")]
                if any(cells):
                    rows.append(cells)
        self.emit(f"\n**Table {self.tables}.** {self.inline(caption).strip()}\n\n")
        if not rows:
            self.log.append(f"table {self.tables}: no tabular found, caption kept")
            return
        width = max(len(r) for r in rows)
        rows = [r + [""] * (width - len(r)) for r in rows]
        self.emit("| " + " | ".join(rows[0]) + " |\n|" + "---|" * width + "\n")
        self.emit("".join("| " + " | ".join(r) + " |\n" for r in rows[1:]) + "\n")

    def references(self) -> None:
        self.heading(2, "References")
        for key in sorted(k for k in self.cited if k not in self.bib):
            self.log.append(f"cited key {key} is not in the bibliography")
        entries = sorted((self.bib[k] for k in self.cited if k in self.bib),
                         key=lambda e: (e["label"], e.get("year", ""), e["key"]))
        self.emit("\n".join(f"- {reference(e)}" for e in entries) + "\n\n")

    def scope_section(self, paper: str, choices: list[str], does_not_claim: list[str]) -> None:
        # says nothing about the machine: text in a record that speaks to the evaluator is an injection finding
        self.emit("\n\n## Scope and choices {#scope-and-choices}\n\n"
                  "The two subsections below repeat, unchanged, passages of the paper in which the authors state their "
                  "modeling commitments and what the paper does not claim.\n")
        for title, hid, refs in (("Choices", "choices", choices), ("Does not claim", "does-not-claim", does_not_claim)):
            self.emit(f"\n### {title} {{#{hid}}}\n\n")
            if not refs:
                self.emit("*(The author has not yet named the passages to carry here.)*\n")
                self.log.append(f"#{hid} is empty: pass --{hid} with a label or heading to fill it")
            for ref in refs:
                found = section_body(paper, self.target_id(ref))
                if found is None:
                    self.emit(f"*(No section {ref!r} in the paper to carry.)*\n\n")
                    self.log.append(f"--{hid} {ref}: no such section in the paper")
                    continue
                heading, body = found
                self.emit(f"From {heading} of the paper:\n\n{body}\n\n")

    def target_id(self, ref: str) -> str:
        if ref in self.labels and self.labels[ref].id:
            return self.labels[ref].id
        return ref.replace(":", "-") if ":" in ref else slug(ref)

    # ----- text -----------------------------------------------------------------------------------------------

    def prose(self, text: str) -> None:
        if self.lstrip_next and text.strip():
            text, self.lstrip_next = text.lstrip(), False
        if text.strip():
            self.emit(self.inline(text))
        elif "\n\n" in text:
            self.emit("\n\n")
        elif text:
            self.emit(" ")

    def inline(self, text: str) -> str:
        text = re.sub(r"\\([&%_#{}$,; ])", lambda m: ESCAPES[m[1]], text.replace(BS, "\n"))
        out, pos = [], 0
        while m := INLINE.search(text, pos):
            out.append(text[pos:m.start()])
            pos = m.end()
            if m["tilde"]:
                out.append(" ")
            elif m["dash"]:
                out.append("—" if m["dash"] == "---" else "–")
            elif m["quote"]:
                out.append("“" if m["quote"] == "``" else "”")
            else:
                piece, pos = self.command(m["cmd"], text, pos)
                out.append(piece)
        out.append(text[pos:])
        return "".join(out)

    def command(self, cmd: str, text: str, pos: int) -> tuple[str, int]:
        if cmd in TEXT:
            inner, pos = arg(text, pos)
            mark = TEXT[cmd]
            return f"{mark}{self.inline(inner).strip()}{mark}", pos
        if cmd == "footnote":
            inner, pos = arg(text, pos)
            notes = self.notes[self.here]
            notes.append(" ".join(self.inline(inner).split()))
            return f"[^{len(notes)}]", pos
        if cmd in ("cref", "Cref", "ref", "eqref", "autoref"):
            inner, pos = arg(text, pos)
            return self.crossref(cmd, inner), pos
        if cmd.startswith("cite"):
            _, pos = opt(text, pos)
            _, pos = opt(text, pos)
            inner, pos = arg(text, pos)
            return self.citation(cmd, inner), pos
        if cmd in SKIP_ARG:
            _, pos = arg(text, pos)
            return "", pos
        if cmd in DROP:
            return "", pos
        if cmd in SYMBOLS:
            return SYMBOLS[cmd], pos
        self.unknown[cmd] = self.unknown.get(cmd, 0) + 1
        return f"\\{cmd}", pos

    def crossref(self, cmd: str, labels: str) -> str:
        how = {"cref": "lower", "Cref": "upper", "ref": "number", "eqref": "eq", "autoref": "upper"}[cmd]
        parts = []
        for label in filter(None, (l.strip() for l in labels.split(","))):
            self.refs.append((label, how))
            parts.append(PH.format("REF", len(self.refs) - 1))
        return join_natural(parts)

    def citation(self, cmd: str, keys: str) -> str:
        names = []
        for key in filter(None, (k.strip() for k in keys.split(","))):
            self.cited.add(key)
            e = self.bib.get(key)
            names.append((e["label"], e.get("year", "n.d.")) if e else (f"[{key}?]", ""))
        if cmd in ("citet", "citet*"):
            return join_natural([f"{n} ({y})" if y else n for n, y in names])
        if cmd == "citeauthor":
            return join_natural([n for n, _ in names])
        if cmd == "citeyear":
            return ", ".join(y for _, y in names)
        inner = "; ".join(f"{n} {y}".strip() for n, y in names)
        return inner if cmd == "citealp" else f"({inner})"

    # ----- placeholders -------------------------------------------------------------------------------------

    def protect_math(self, text: str) -> str:
        text = text.replace("\\\\", BS)

        def keep(m: re.Match) -> str:
            raw = m[0].replace(BS, "\\\\")
            if raw.startswith("\\["):
                shown = f"\n$$\n{raw[2:-2].strip()}\n$$\n"
            elif raw.startswith("\\("):
                shown = f"${raw[2:-2].strip()}$"
            elif raw.startswith("\\begin{equation"):
                body = re.sub(r"^\\begin\{equation\*?\}|\\end\{equation\*?\}$", "", raw).strip()
                tag = ""
                if lab := re.search(r"\\label\{([^}]*)\}", body):
                    self.equations += 1
                    self.labels[lab[1]] = Label(f"equation ({self.equations})", None, self.here)
                    body = body.replace(lab[0], "").strip()
                    tag = f" \\tag{{{self.equations}}}"
                shown = f"\n$$\n{body}{tag}\n$$\n"
            else:
                shown = raw
            self.math.append(shown)
            return PH.format("MATH", len(self.math) - 1)
        return MATH.sub(keep, text)

    def assemble(self, which: str) -> str:
        text = "".join(self.out[which])
        text = re.sub(r"[ \t]+\n", "\n", text)
        text = re.sub(r"\n{3,}", "\n\n", text).strip() + "\n"
        if self.notes[which]:
            text += "\n" + "\n".join(f"[^{i}]: {note}" for i, note in enumerate(self.notes[which], 1)) + "\n"
        return text

    def restore(self, text: str, here: str) -> str:
        def ref(m: re.Match) -> str:
            label, how = self.refs[int(m[1])]
            target = self.labels.get(label)
            if not target:
                self.log.append(f"reference to unknown label {label}")
                return f"[?{label}]"
            shown = target.text
            if how in ("number", "eq"):
                shown = shown.rsplit(" ", 1)[-1]
            elif target.quoted:
                shown = f"“{shown}”"
            elif how == "lower":
                shown = shown[0].lower() + shown[1:]
            if not target.id:
                return shown
            link = f"#{target.id}" if target.file == here else f"../{target.file}/{target.file}.md#{target.id}"
            return f"[{shown}]({link})"

        text = re.sub("\x00REF(\\d+)\x00", ref, text)
        text = re.sub("\x00MATH(\\d+)\x00", lambda m: self.math[int(m[1])], text)
        return re.sub(r"\n{3,}", "\n\n", text)


# ----- helpers ---------------------------------------------------------------------------------------------------

def arg(text: str, pos: int) -> tuple[str, int]:
    """The brace-delimited argument at or after pos; ('', pos) when there is none."""
    while pos < len(text) and text[pos] in " \t\n":
        pos += 1
    if pos >= len(text) or text[pos] != "{":
        return "", pos
    depth, i = 0, pos
    while i < len(text):
        c = text[i]
        if c == "\\":
            i += 2
            continue
        depth += (c == "{") - (c == "}")
        if depth == 0:
            return text[pos + 1:i], i + 1
        i += 1
    return text[pos + 1:], len(text)


def opt(text: str, pos: int) -> tuple[str, int]:
    """An optional [..] argument at pos, nested braces allowed inside; ('', pos) when there is none."""
    start = pos
    while pos < len(text) and text[pos] in " \t":
        pos += 1
    if pos >= len(text) or text[pos] != "[":
        return "", start
    depth, i = 0, pos
    while i < len(text):
        c = text[i]
        if c == "\\":
            i += 2
            continue
        depth += (c in "[{") - (c in "]}")
        if depth == 0:
            return text[pos + 1:i], i + 1
        i += 1
    return "", start


def label_after(text: str, pos: int) -> tuple[str | None, int]:
    if m := re.compile(r"\s*\\label\s*\{([^}]*)\}").match(text, pos):
        return m[1].strip(), m.end()
    return None, pos


def caption_and_label(block: str) -> tuple[str, str | None]:
    caption = ""
    if m := re.search(r"\\caption\s*(\[[^]]*\])?\s*\{", block):
        caption, _ = arg(block, m.end() - 1)
    label = re.search(r"\\label\{([^}]*)\}", block)
    return caption, label[1] if label else None


def preamble_arg(src: str, name: str) -> str:
    if m := re.search(rf"\\{name}\s*\{{", src):
        return arg(src, m.end() - 1)[0]
    return ""


def theorem_kinds(src: str) -> dict[str, Theorem]:
    kinds: dict[str, Theorem] = {}
    for m in re.finditer(r"\\newtheorem(\*?)\{(\w+)\}(?:\[(\w+)\])?\{([^}]*)\}(?:\[(\w+)\])?", src):
        starred, name, shared, title, reset = m.groups()
        title = title.replace("~", " ")
        if starred:
            kinds[name] = Theorem(title, None, None)
        elif shared:
            base = kinds.get(shared) or Theorem(shared, shared, None)
            kinds[name] = Theorem(title, base.counter, base.reset)
        else:
            kinds[name] = Theorem(title, name, reset)
    return kinds


def section_body(markdown: str, hid: str) -> tuple[str, str] | None:
    """A section of converted Markdown by heading id: (its heading as a link into the paper, its body)."""
    lines = markdown.splitlines()
    head = re.compile(r"^(#{1,6})\s+(.*?)\s*\{#([\w.-]+)\}\s*$")
    for i, line in enumerate(lines):
        m = head.match(line)
        if m and m[3] == hid:
            level = len(m[1])
            end = next((j for j in range(i + 1, len(lines)) if (h := head.match(lines[j])) and len(h[1]) <= level),
                       len(lines))
            return f"[{plain(m[2])}](../paper/paper.md#{hid})", "\n".join(lines[i + 1:end]).strip()
    return None


def plain(text: str) -> str:
    """Markdown and placeholders out of a heading, for its slug or a reference's display text."""
    text = re.sub("\x00(?:REF|MATH)\\d+\x00", "", text)
    text = re.sub(r"\[([^]]*)\]\([^)]*\)", r"\1", text)
    return " ".join(text.replace("*", "").replace("`", "").split())


def join_natural(parts: list[str]) -> str:
    if len(parts) <= 1:
        return "".join(parts)
    return ", ".join(parts[:-1]) + " and " + parts[-1]


def roman(n: int) -> str:
    out = ""
    for value, numeral in ((10, "x"), (9, "ix"), (5, "v"), (4, "iv"), (1, "i")):
        while n >= value:
            out, n = out + numeral, n - value
    return out


# ----- bibliography ----------------------------------------------------------------------------------------------

def parse_bib(bib: str) -> dict[str, dict]:
    entries = {}
    for m in re.finditer(r"@(\w+)\s*\{\s*([^,\s]+)\s*,", bib):
        kind, key = m[1].lower(), m[2]
        if kind in ("comment", "string", "preamble"):
            continue
        fields, pos = {}, m.end()
        while f := FIELD.match(bib, pos):
            name, pos = f[1].lower(), f.end()
            if bib[pos] == "{":
                value, pos = arg(bib, pos)
            elif bib[pos] == '"':
                end = bib.index('"', pos + 1)
                value, pos = bib[pos + 1:end], end + 1
            else:
                v = re.compile(r"[^,}\s]+").match(bib, pos)
                value, pos = v[0], v.end()
            fields[name] = " ".join(value.split())
            if not (comma := re.compile(r"\s*,").match(bib, pos)):
                break
            pos = comma.end()
        authors = [a for a in re.split(r"\s+and\s+", fields.get("author", "")) if a]
        last = [surname(a) for a in authors] or [surname(fields.get("editor", "")) or key]
        label = last[0] if len(last) == 1 else f"{last[0]} and {last[1]}" if len(last) == 2 else f"{last[0]} et al."
        entries[key] = {"key": key, "kind": kind, "authors": authors, "label": label, **fields}
    return entries


def surname(author: str) -> str:
    author = debrace(author).strip()
    if not author:
        return ""
    return (author.split(",")[0] if "," in author else author.split()[-1]).strip()


def debrace(text: str) -> str:
    text = re.sub(r"\\['`\"^~=.uvHtcdb]\{?(\w)\}?", r"\1", text)
    return text.replace("{", "").replace("}", "").replace("~", " ")


def reference(e: dict) -> str:
    names = ", ".join(debrace(a) for a in e["authors"]) or e["label"]
    year = e.get("year", "n.d.")
    title = debrace(e.get("title", "")).rstrip(".")
    if e["kind"] == "book":
        where = f"*{title}*. {debrace(e.get('publisher', ''))}".rstrip(". ") + "."
    elif e["kind"] == "article":
        issue = f"({e['number']})" if e.get("number") else ""
        pages = e.get("pages", "").replace("--", "–")
        where = (f"{title}. *{debrace(e.get('journal', ''))}*" + (f", {e['volume']}{issue}" if e.get("volume") else "")
                 + (f", {pages}" if pages else "") + ".")
    else:
        note = debrace(e.get("note") or e.get("howpublished") or e.get("booktitle") or e["kind"].capitalize())
        where = f"{title}. {note}".rstrip(".") + "."
    doi = f" https://doi.org/{e['doi']}" if e.get("doi") else f" {e['url']}" if e.get("url") else ""
    return f"{names} ({year}). {where}{doi}"


def import_tex(tex_path: Path, record_dir: Path, bib_path: Path | None = None, choices: list[str] = (),
               does_not_claim: list[str] = (), force: bool = False) -> Result:
    tex = tex_path.read_text(encoding="utf-8")
    if bib_path is None and (m := re.search(r"\\bibliography\{([^}]*)\}", tex)):
        bib_path = (tex_path.parent / m[1].split(",")[0]).with_suffix(".bib")
    bib = bib_path.read_text(encoding="utf-8") if bib_path and bib_path.exists() else ""
    result = convert(tex, bib, choices, does_not_claim)
    targets = {record_dir / "paper" / "paper.md": result.paper, record_dir / "appendix" / "appendix.md": result.appendix}
    if not force and (taken := [p for p in targets if p.exists()]):
        raise FileExistsError(f"{taken[0]} exists; pass --force to overwrite")
    for path, text in targets.items():
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8", newline="\n")
    if not bib:
        result.log.append("no bibliography found: citations show their keys")
    return result
