"""The .rtf twins: Times New Roman 12, the Markdown constructs Mark 1 writes, and where twins are and are not made."""
import re

from machine import rtf, stats

SAMPLE = """# Findings report · a paper {#top}

Findings only: **no verdict**, each with a *pointer*; see `claims:C1` and [the standard](../standard/formal.md#S1)
and [OpenAlex](https://openalex.org).

- first item, with p* = (a+c)/2 and pi* = (a-c)^2/4 left alone
  continued on the next line
- second {braces} and a dash – here
1. numbered

| Box | State |
|---|---|
| J1 | built |

> a quote

```
code {here}
```
"""


def test_conversion_covers_the_constructs_in_times_new_roman_12():
    out = rtf.convert(SAMPLE)
    assert out.startswith(r"{\rtf1") and out.endswith("}") and out.isascii()
    assert "Times New Roman" in out and r"\f0\fs24" in out
    assert r"\keepn\b Findings report" in out and "{#top}" not in out
    unescaped = re.sub(r"\\[{}]", "", out)
    assert unescaped.count("{") == unescaped.count("}")
    assert r"{\b no verdict}" in out and r"{\i pointer}" in out and r"{\f1 claims:C1}" in out
    assert r"the standard" in out and "formal.md" not in out  # relative links keep their text only
    assert r"OpenAlex ({\f1 https://openalex.org})" in out
    assert r"\'95\tab first item, with p* = (a+c)/2 and pi* = (a-c)^2/4 left alone continued" in out
    assert r"\{braces\}" in out and "\\u" "8211?" in out  # the en dash as an RTF unicode escape
    assert r"1.\tab numbered" in out
    assert r"\trowd" in out and r"\sa0\b Box\cell" in out and r" built\cell" in out and r"\row" in out
    assert r"\li720\ri720\sa160\i a quote" in out
    assert r"{\pard\f1\fs20\sa0 code \{here\}\par}" in out
    assert "**" not in out and "```" not in out


def test_machine_documents_get_a_twin(workspace):
    md, _ = stats.departures()
    assert md.with_suffix(".rtf").exists()


def test_twins_skip_record_parts_and_code_facing_files(workspace):
    (workspace / "PENDING.md").write_text("# waiting\n", encoding="utf-8")
    made = rtf.twins(workspace)
    names = {p.relative_to(workspace).as_posix() for p in made}
    assert "1-journal/README.md".replace(".md", ".rtf") in names
    assert not any("2-author/questions-before-priors/paper" in n or "appendix" in n for n in names)
    assert "PENDING.rtf" not in names
