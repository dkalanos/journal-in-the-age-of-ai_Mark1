# 4-reviewers/ · what reviewers see, and send back

One folder per paper, written only after the editor has signed "new" (H5) and the paper is in review.

| Path | What it is |
|---|---|
| `packet/` | What reviewers receive (`mark1 packet`): the paper and the appendix as submitted, the findings report, the evidence map, the interest criteria, and a README saying what they are asked. The AI appendix, the materials, the author's answer, the comparison with the author's run and the decision stay with the editor. |
| `reports/r<n>-<reviewer>.md` | Reviewers' reports, by round (`mark1 report`). |

Reviewers are asked whether the work is of interest under the published criteria; whether its claims are
warranted was checked before they read, and the findings report tells them where it was not. Their signed
judgment goes, with the editor's, to `../3-editor/<paper>/interest.yaml` (H3).

`questions-before-priors/` holds round 1's review: the packet, and the two machine reviews of the July 23 draft
filed as the reports of two reviewers. Both say revise, and the editor signed revise and resubmit (`mark1
revise`). Round 2 stops at intake, where the paper's real history ends; the test suite takes a copy of the
record through review to a certificate (`tests/test_journey.py`).
