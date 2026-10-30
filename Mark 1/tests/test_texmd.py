import pytest

from machine import texmd
from machine.pointer import sections

TEX = r"""
\documentclass{article}
\newtheorem{proposition}{Proposition}[section]
\newtheorem{definition}[proposition]{Definition}
\newtheorem*{excont}{Example~1 (continued)}
\title{A \textbf{Title}\thanks{Thanks.}}
\author{A. Author}
\date{June 2026\\[0.4em] --- Draft ---}
\begin{document}
\maketitle
\begin{abstract}
Short.
\end{abstract}
\section{Introduction}
\label{sec:intro}
See \cref{prop:main} and \cref{sec:model}; also \citep{Doe2020,Roe2019} and \citet{Doe2020}.\footnote{A note with $x^2$.}
% a comment to drop
\section{Model}
\label{sec:model}
\begin{equation}
y = a - p
\label{eq:demand}
\end{equation}
Prices---and costs--matter, see \cref{eq:demand} and \Cref{fig:one}.
\begin{proposition}[Main]
\label{prop:main}
If $a > c$ then $p^* = (a+c)/2$.
\end{proposition}
\begin{proof}
Differentiate \[ \pi = (p-c)(a-p). \]
\end{proof}
\begin{excont}
Still the same example.
\end{excont}
\paragraph{Scope.}
\label{rem:scope}
We assume linear demand (\cref{rem:scope}).
\begin{enumerate}[label=(\roman*)]
\item first
\item second
\end{enumerate}
\begin{enumerate}[label=(\alph*),start=4]
\item fourth
\end{enumerate}
\begin{table}[t]
\caption{A ledger.}
\label{tab:one}
\begin{tabularx}{\textwidth}{lX}
\toprule
Object & Access\\
\midrule
State $s$ & never & \cref{prop:main}\\
\bottomrule
\end{tabularx}
\end{table}
\bibliographystyle{plainnat}
\bibliography{refs}
\appendix
\section{Proofs}
\label{app:proofs}
\begin{figure}
\begin{tikzpicture}\node {x};\end{tikzpicture}
\caption{A drawing.}
\label{fig:one}
\end{figure}
\Cref{fig:one}, \cref{prop:main} and \cref{tab:one}.
\end{document}
"""
BIB = r"""
@article{Doe2020, author = {Doe, Jane and Roe, Richard}, title = {On Things}, journal = {J. Stuff},
  year = {2020}, volume = {1}, number = {2}, pages = {3--4}, doi = {10.1/x}}
@book{Roe2019, author = {Roe, Richard}, title = {A Book}, publisher = {Press}, year = {2019}}
"""


@pytest.fixture(scope="module")
def result():
    return texmd.convert(TEX, BIB, choices=["rem:scope"], does_not_claim=["sec:intro"])


def test_headings_carry_labels_as_ids(result):
    paper = result.paper
    assert "# A Title\n\nA. Author · June 2026 — Draft\n\n*Thanks.*" in paper
    assert "## 2. Model {#sec-model}" in paper
    assert "### Proposition 2.1 (Main) {#prop-main}" in paper
    assert "#### Proof {#proof-prop-main}" in paper and "(a-p).\n$$\n ∎" in paper
    assert "### Example 1 (continued) {#example-1-continued}" in paper
    assert "### Scope {#rem-scope}" in paper
    assert {"sec-model", "prop-main", "proof-prop-main", "rem-scope", "references", "abstract"} <= sections(paper)


def test_cross_references_link_and_read_naturally(result):
    assert "See [proposition 2.1](#prop-main) and [section 2](#sec-model)" in result.paper
    assert "see equation (1) and Figure 1." in result.paper
    assert "([“Scope”](#rem-scope))" in result.paper
    assert "Figure 1, [proposition 2.1](../paper/paper.md#prop-main) and table 1." in result.appendix


def test_citations_and_references_come_from_the_bib(result):
    assert "(Doe and Roe 2020; Roe 2019) and Doe and Roe (2020)" in result.paper
    assert "- Doe, Jane, Roe, Richard (2020). On Things. *J. Stuff*, 1(2), 3–4. https://doi.org/10.1/x" in result.paper
    assert "- Roe, Richard (2019). *A Book*. Press." in result.paper


def test_math_footnotes_lists_tables_and_typography(result):
    paper = result.paper
    assert "$$\ny = a - p \\tag{1}\n$$" in paper
    assert "Prices—and costs–matter" in paper
    assert "(2020).[^1]" in paper and paper.rstrip().endswith("[^1]: A note with $x^2$.")
    assert "- (i) first\n- (ii) second\n\n- (d) fourth" in paper
    assert "**Table 1.** A ledger.\n\n| Object | Access |  |\n|---|---|---|\n| State $s$ | never | [proposition 2.1](#prop-main) |" in paper


def test_scope_and_choices_carry_the_named_sections_verbatim(result):
    appendix = result.appendix
    assert "## Scope and choices {#scope-and-choices}" in appendix
    assert "### Choices {#choices}\n\nFrom [Scope](../paper/paper.md#rem-scope) of the paper:\n\nWe assume linear demand" in appendix
    assert "### Does not claim {#does-not-claim}\n\nFrom [1. Introduction](../paper/paper.md#sec-intro) of the paper:" in appendix
    assert "> **Figure 1.** A drawing." in appendix


def test_the_log_says_what_was_dropped(result):
    assert any("TikZ drawing dropped" in line for line in result.log)
    assert any("comment line" in line for line in result.log)


def test_import_writes_both_parts_and_refuses_to_overwrite(tmp_path):
    tex = tmp_path / "paper.tex"
    tex.write_text(TEX, encoding="utf-8")
    (tmp_path / "refs.bib").write_text(BIB, encoding="utf-8")
    record = tmp_path / "record"
    result = texmd.import_tex(tex, record, choices=["rem:scope"])
    assert (record / "paper" / "paper.md").read_text(encoding="utf-8") == result.paper
    assert "### Does not claim {#does-not-claim}\n\n*(The author has not yet named" in (record / "appendix" / "appendix.md").read_text(encoding="utf-8")
    with pytest.raises(FileExistsError):
        texmd.import_tex(tex, record)
