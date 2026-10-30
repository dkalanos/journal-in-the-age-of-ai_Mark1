# figures · the figures of the technical appendix

| File | Figure |
|---|---|
| `legend.png`, `legend.pdf` | the legend shared by the figures |
| `fig1.*` | Fig. 1, the journal today and the journal in the age of AI, side by side |
| `fig2.*` | Fig. 2, the research package and the AI appendix |
| `fig3.*` | Fig. 3, the three levels of checks, the kinds of newness, and what each level's findings lead to |
| `fig4.*` | Fig. 4, one paper's path through the process |
| `fig4a.*`, `fig4b.*` | Fig. 4a and 4b, the path in two halves: to intake, and from intake to a certificate |

All of them are slides of one PowerPoint deck, `system_diagrams v6dk.pptx`, exported one slide per figure at 2667
by 1500 pixels (PNG) and as single-page PDFs. The deck is the source; the figures are not drawn by hand.

**Rebuilding.** `figures_v6.py` builds v6dk from a fresh copy of the previous deck, `system_diagrams v5dk.pptx`,
changing the two boxes of Fig. 3 it names in its docstring; it needs Python with `python-pptx` and imports
`set_text` from `figures_v3.py`, the module that drew the deck's text boxes in the first place. `export_figures.ps1`
exports every slide of the deck into this folder through PowerPoint (Windows, COM). Neither is needed to read the
figures or to run Mark 1.
