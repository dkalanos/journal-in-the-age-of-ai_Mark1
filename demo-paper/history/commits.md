# Commits from round 1 to round 2

Source repository: 2026_TBV_Paper-1, commits `18b3ebd` (2026-07-23, which added the reviews and the v03 repair pass) through `0a18f80` (2026-08-15, GPTedit-10). Oldest first. Full messages; file statistics for every path the commit touched.

## 18b3ebd · 2026-07-23 · MDR Git

Consolidate to single-file paper; add talk deck; v03 repair pass

Paper structure:
- Collapse modular main.tex + sections/ into single tbv_mdr_Paper01-vNN.tex
  (v01 first draft, v02 GPT-reviewed baseline, v03 current)

v03 — repair of GPT machine review #2 + four internal audits (A1+B1+C1):
- Two typed records (deliberative r_i / analyst r̄_i); agent decisions depend
  only on r_i, restorative/warrant objects on r̄_i
- Deliberative leverage B̂ (recurrence-rate, per-token robust gain over
  coherent groupings) replaces agent-infeasible meet-based B; determinism-
  certifies-separability remark harmonizes example and general model
- Achievability weight λ^{(k)} decays on repeated failure: finite elections,
  "abandoned questions"; failure counter enters SCUE state
- Proof gaps closed: aggregated-count restoration (dilution), absorption(d)
  auxiliary coupling, frozen-prefix test consistency, marginal-equality
  nonidentification, entry-count rest-points, analyst-record warrant
- Persistence instance moved to beta<1 (stable stasis); dissonant stasis now
  a standalone definition; SCUE conditions made asymptotic
- Headline hedged: inquiry dies out to a Bayesian world OR rationally
  tolerated dissonance
- 36 pp, compiles clean, 0 undefined refs; repair plan in notes/

Also: MARP talk deck (talks/2026_Questions_Before_Priors.{md,pdf}) and
machine review PDFs (Machine_Reviews/).

Co-Authored-By: Claude Fable 5 <noreply@anthropic.com>


 Machine_Reviews/Draft01-GPTReview.pdf       |  Bin 0 -> 59997 bytes
 Machine_Reviews/Draft01-GPTReview02.pdf     |  Bin 0 -> 73275 bytes
 README.md                                   |    2 +-
 notes/v03_repair_plan.md                    |  112 ++++
 paper/main.pdf                              |  Bin 253758 -> 0 bytes
 paper/main.tex                              |  123 -----
 paper/sections/appendix.tex                 |  169 ------
 paper/sections/bayesian.tex                 |   55 --
 paper/sections/discussion.tex               |  129 -----
 paper/sections/dissonance.tex               |  134 -----
 paper/sections/dynamics.tex                 |  229 --------
 paper/sections/economics.tex                |  125 -----
 paper/sections/inquiry.tex                  |  140 -----
 paper/sections/intro.tex                    |  140 -----
 paper/sections/literature.tex               |  104 ----
 paper/sections/model.tex                    |  205 -------
 paper/sections/pivot.tex                    |  108 ----
 paper/{refs.bib => tbv_mdr_Paper01-v01.bib} |    0
 paper/tbv_mdr_Paper01-v01.pdf               |  Bin 0 -> 265891 bytes
 paper/tbv_mdr_Paper01-v01.tex               | 1786 +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
 paper/tbv_mdr_Paper01-v02.pdf               |  Bin 0 -> 265891 bytes
 paper/tbv_mdr_Paper01-v02.tex               | 1786 +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
 paper/tbv_mdr_Paper01-v03.bib               |  429 +++++++++++++++
 paper/tbv_mdr_Paper01-v03.pdf               |  Bin 0 -> 285379 bytes
 paper/tbv_mdr_Paper01-v03.tex               | 2017 +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
 talks/2026_Questions_Before_Priors.md       |  894 ++++++++++++++++++++++++++++++
 talks/2026_Questions_Before_Priors.pdf      |  Bin 0 -> 178568 bytes
 talks/MARP_Theme_Template.md                |  576 +++++++++++++++++++
 28 files changed, 7601 insertions(+), 1662 deletions(-)
## 978ebe5 · 2026-07-24 · MDR Git

Add v04 as source of truth: one sentence per line

Reformat the paper so each sentence sits on its own line, with
no content changes. Verified that collapsing all whitespace yields
text byte-identical to the wrapped version, so only line breaks
changed; display math, environments, and the preamble are untouched.
This makes git diffs and Meld comparisons land on the changed
sentence rather than reflowing whole paragraphs.

Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>


 paper/tbv_mdr_Paper01-v04.tex | 1352 +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
 1 file changed, 1352 insertions(+)
## 8f11b71 · 2026-07-24 · MDR Git

Prune old paper versions; adopt version-agnostic bib; fix v04 citations

- Delete superseded drafts v01/v02/v03 (.tex/.pdf/.bib), recoverable
  from git history if ever needed; v04 is the sole source of truth.
- Rename the bibliography to a version-agnostic MDR_TBV_Paper01.bib
  (git mv from the identical v03 bib) so all revisions share one name.
- Point v04's \bibliography at MDR_TBV_Paper01; this fixes the broken
  citations (v04 referenced a nonexistent tbv_mdr_Paper01-v04.bib, so
  bibtex found no database and every \cite came up empty). Compiles
  clean with zero undefined citations.
- Include current v04.tex edits and compiled PDF.

Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>


 paper/{tbv_mdr_Paper01-v01.bib => MDR_TBV_Paper01.bib} |    0
 paper/tbv_mdr_Paper01-v01.pdf                          |  Bin 265891 -> 0 bytes
 paper/tbv_mdr_Paper01-v01.tex                          | 1786 -------------------------------------------------
 paper/tbv_mdr_Paper01-v02.pdf                          |  Bin 265891 -> 0 bytes
 paper/tbv_mdr_Paper01-v02.tex                          | 1786 -------------------------------------------------
 paper/tbv_mdr_Paper01-v03.bib                          |  429 ------------
 paper/tbv_mdr_Paper01-v03.pdf                          |  Bin 285379 -> 0 bytes
 paper/tbv_mdr_Paper01-v03.tex                          | 2017 --------------------------------------------------------
 paper/tbv_mdr_Paper01-v04.pdf                          |  Bin 0 -> 299568 bytes
 paper/tbv_mdr_Paper01-v04.tex                          |   33 +-
 10 files changed, 21 insertions(+), 6030 deletions(-)
## 6cab9ea · 2026-07-24 · MDR Git

Notation simplification pass + single-clock redesign note (checkpoint)

Pre-overhaul checkpoint. Notation economy:
- Drop redundant F(\cdot\mid s,a); use \tau(s)(a) throughout.
- Fix u_i -> \pi_i straggler; remove unused symbols (warrant-gap letter G,
  complexity ordering \kappa, election indicator \varepsilon_i, unused \ind macro).
- Motivate the two-clock timing at first appearance (about to be replaced).

Add notes/single-clock-redesign.md: full spec + claim-by-claim change map for
the single-clock / dissonance-capacity / switching-cost overhaul.

Also carries in-progress manual edits to v04.tex.

Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>


 notes/single-clock-redesign.md | 265 +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
 paper/tbv_mdr_Paper01-v04.pdf  | Bin 299568 -> 299829 bytes
 paper/tbv_mdr_Paper01-v04.tex  |  76 ++++++++++++-----------
 3 files changed, 305 insertions(+), 36 deletions(-)
## 97aae3c · 2026-07-24 · MDR Git

Single-clock overhaul T1 (front end): timing, standing policy, sequential detector

- One clock (periods); drop generations/episodes in the front end.
- ass:commitment -> standing policy + (S,s) switching rule: belief-optimal
  sigma*_i (eq:subjective-optimality retained), new value U_i, switch iff
  per-period gain clears the switching hurdle kappa_i; inertia now emergent.
- def:test -> sequential e-process adequacy detector with dissonance capacity
  b_i: reject (permanently) when log E^m >= b_i; Ville gives false-alarm
  <= e^{-b_i}; deterministic eta=0 recovers the exact test. eta/w/nbar kept as
  the fixed-sample retrospective criterion for the repair/grouping tests.
- lem:test-consistency, def:dissonance, def:exposure, prop:exposure recast in
  periods; permanent rejection makes the active set monotone (refill clause dropped).

Compiles, 40pp. Remaining: T2 (economics) and T3 (dynamics/appendix/example).

Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>


 paper/tbv_mdr_Paper01-v04.pdf | Bin 299829 -> 304232 bytes
 paper/tbv_mdr_Paper01-v04.tex | 123 +++++++++++++++++++++++++++++++++++++++++++++++-----------------------------------
 2 files changed, 70 insertions(+), 53 deletions(-)
## ab6bf72 · 2026-07-24 · MDR Git

Single-clock overhaul T2 (economics): valuation horizon, net-of-switching participation, decoupling

- Reinterpret T as a common valuation horizon (periods): ass:commitment switch
  rule becomes T*(U_i(sigma*)-U_i(sigma)) > kappa_i with kappa_i a one-time cost.
- def:leverage premise reworded to horizon-T; ass:elective -> standing policy.
- prop:participation now nets the switching hurdle: elect iff
  lambda_i (B_i - kappa_i)_+ >= gamma_i (don't inquire for a distinction you won't act on).
- New rem:stickiness (Enlightened inertia): model updates but policy doesn't when
  the realized switch gain falls below kappa_i -- a second persistence channel;
  an opacity phenomenon (collapses under pointwise transparency, rem:certification).

Compiles, 41pp. Remaining: T3 (dynamics/appendix/running example).

Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>


 paper/tbv_mdr_Paper01-v04.pdf | Bin 304232 -> 306004 bytes
 paper/tbv_mdr_Paper01-v04.tex |  31 ++++++++++++++++++++-----------
 2 files changed, 20 insertions(+), 11 deletions(-)
## 30c5de8 · 2026-07-25 · MDR Git

T2 fix: do not net the switching cost into the inquiry decision

Per author: netting kappa into participation is inconsistent with unawareness --
kappa prices a switch to a policy on the refined partition, which is unrepresentable
pre-insight, so the agent cannot price it when deciding to inquire.

- Participation reverted to lambda_i * B_i >= gamma_i (prices the question, not the
  answer). kappa now enters only the post-insight (S,s) switch (ass:commitment).
- rem:stickiness rewritten: enlightened-inertia decoupling is structural (price the
  question now, decide the switch later), holds deterministically, not opacity-only;
  the agent cannot anticipate declining to act because it cannot anticipate what it
  will learn.
- Design note 4.4 and memory updated with the general principle: pre-insight
  deliberation quantifies only over currently-represented objects.

Compiles, 41pp.

Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>


 notes/single-clock-redesign.md |  23 ++++++++++++++---------
 paper/tbv_mdr_Paper01-v04.pdf  | Bin 306004 -> 305912 bytes
 paper/tbv_mdr_Paper01-v04.tex  |  17 +++++++++--------
 3 files changed, 23 insertions(+), 17 deletions(-)
## 3696e24 · 2026-07-25 · MDR Git

Single-clock overhaul T3a: dynamics section recast to periods + standing policy

- def:scue(i): standing policy stationary under the switching rule (no switch clears
  kappa_i; = subjective optimality when kappa_i=0). State lists the standing policy.
- ass:regularity(i): generic-tolerance -> strict-adequacy (no theory at the boundary),
  matching the sequential detector; deterministic case automatic.
- thm:absorption / prop:rest-points / prop:adequacy: period + standing-policy wording;
  rest point = standing policy strictly inside the inaction band.
- rem:scope: switching costs temper cycling (inaction band absorbs small swings).
- prop:persistence: add the enlightened-inertia channel (rem:stickiness) alongside
  unpriced repair.

Compiles, 41pp. Remaining: T3b (appendix (g,t)->t reindex) and T3c (running example).

Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>


 paper/tbv_mdr_Paper01-v04.pdf | Bin 305912 -> 306886 bytes
 paper/tbv_mdr_Paper01-v04.tex |  85 +++++++++++++++++++++++++++++++++++++++++-----------------------------------------
 2 files changed, 43 insertions(+), 42 deletions(-)
## 1484df3 · 2026-07-25 · MDR Git

Single-clock overhaul T3b: appendix reindexed (g,t) -> single period t

- Probability framework: {s_t},{U_t},{V_{i,t}} over periods; F_t; standing policy
  and election indicator F_{t-1}-measurable.
- Absorption proof parts (c),(d) and rest-points proofs: generation -> period,
  g_0 -> t_0; part (d) now invokes lem:test-consistency (e-process) with the
  e^{-b_i} false-rejection accounted in A_i^*.
- rest-points(i) proof reconciled to the inaction band (no switch near the limit).

Compiles, 41pp. Remaining: T3c (running-example recalibration + kappa).

Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>


 paper/tbv_mdr_Paper01-v04.pdf | Bin 306886 -> 306893 bytes
 paper/tbv_mdr_Paper01-v04.tex |  32 ++++++++++++++++----------------
 2 files changed, 16 insertions(+), 16 deletions(-)
## 4e25239 · 2026-07-25 · MDR Git

Single-clock overhaul T3c: running example recast to periods + switching-cost illustration

- Example fully period-based: valuation horizon T=2 preserves the leverage numbers
  (B_hat=1/2); "discovery generation" -> two periods serving the diagonal states;
  "validation generation" -> a later stretch; episodes -> observations/periods.
- Added the kappa illustration: acting on the row refinement costs kappa_i; with
  kappa_i<1/2 the firm re-differentiates, with kappa_i>1/2 it holds its old policy
  despite knowing the row law -- the deterministic face of enlightened inertia.

Overhaul complete: zero generation/episode references remain. Compiles, 41pp.

Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>


 paper/tbv_mdr_Paper01-v04.pdf | Bin 306893 -> 307528 bytes
 paper/tbv_mdr_Paper01-v04.tex |  17 +++++++++--------
 2 files changed, 9 insertions(+), 8 deletions(-)
## b28f3c9 · 2026-07-25 · MDR Git

Audit fixes: minors + def:test repair-threshold + rest-points(i) kappa=0 clause

From the three-way stress-test (all non-statement-changing except the two noted):
- def:test: define \hat p_i / n_i at first use; state the repair test as the n>0
  variant and the grouping test as the \bar n variant (they genuinely differ) [#3, m4].
- lem:test-consistency proof: phrase the divergence step as a domination argument [m3].
- rest-points(i): add the \kappa_i=0 companion clause (strict-argmax no-switch) so the
  hypothesis is satisfiable in the case def:scue(i) foregrounds [#2].
- Rename nonidentification horizon G -> H (de-collide with grouping G) [m5].
- Stale lexis (commit->adopt, "committed one"->carried-forward); appendix (d) prefix
  wording; state F_{t-1} timing convention; note T is common across agents [m6/4/5/7].

Compiles, 41pp. Still open (need author sign-off): rest-points(ii-b) recast [#1] and
prop:persistence scope [#4].

Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>


 paper/tbv_mdr_Paper01-v04.pdf | Bin 307528 -> 308832 bytes
 paper/tbv_mdr_Paper01-v04.tex |  34 ++++++++++++++++------------------
 2 files changed, 16 insertions(+), 18 deletions(-)
## 93e3a58 · 2026-07-25 · MDR Git

Formal-core Phase 1: recast rest-points(ii-b) on the e-process; broaden persistence

- rest-points(ii-b) [#1]: replace the retired fixed-sample/Hoeffding proof with the
  correct sequential-detector argument. Ville on each entry-active eta-adequate
  theory's evidence process => an agent goes dissonant w.p. <= e^{-b_i}; union =>
  persistence w.p. >= 1 - sum_i e^{-b_i}. Drops the N(delta)/eps/eta' apparatus and
  yields a result: CAPACITY GOVERNS REST-POINT ROBUSTNESS (deterministic case: sure).
- prop:persistence [#4]: broaden to two channels -- dissonant stasis (unpriced
  question) OR enlightened inertia (learned, but the recommended switch is priced
  below kappa_i); proof prose attributes the stasis channel to the instance and the
  inertia channel to rem:stickiness.
- Add notes/formal-core-plan.md (5-phase plan; capacity = modest-core per author).

Compiles, 41pp.

Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>


 notes/formal-core-plan.md     | 140 ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
 paper/tbv_mdr_Paper01-v04.pdf | Bin 308832 -> 306193 bytes
 paper/tbv_mdr_Paper01-v04.tex | 103 ++++++++++--------------------------------------------------
 3 files changed, 156 insertions(+), 87 deletions(-)
## 1e15cbf · 2026-07-25 · MDR Git

Formal-core Phase 3 (modest-core capacity): prop:capacity + rem:two-sources

- prop:capacity: capacity as a single cognitive-style dial. (i) Detection: under an
  exposed profile, expected periods to dissonance = O(b_i/D_i) (linear in capacity,
  inverse in detectability), via Wald on the dominating evidence component. (ii)
  Robustness: false-alarm <= e^{-b_i} (from rest-points ii-b). Higher b_i => longer
  stable stretches + harder rest points, slower detection of genuine breakage.
- rem:two-sources: separates the two heterogeneity origins -- awareness-path
  (identical agents, different experiences) vs cognitive-style (different b_i/kappa_i)
  -- resolving the "identical agents" tension inside the formalism.

Compiles, 41pp.

Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>


 paper/tbv_mdr_Paper01-v04.pdf | Bin 306193 -> 309884 bytes
 paper/tbv_mdr_Paper01-v04.tex |  22 ++++++++++++++++++++++
 2 files changed, 22 insertions(+)
## cef4415 · 2026-07-25 · MDR Git

Formal-core Phase 2: interpret the valuation horizon T

T = the planning horizon over which a one-time cost is amortized, a
bounded-rationality stand-in for discounting.

Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>


 paper/tbv_mdr_Paper01-v04.pdf | Bin 309884 -> 309956 bytes
 paper/tbv_mdr_Paper01-v04.tex |   2 +-
 2 files changed, 1 insertion(+), 1 deletion(-)
## 85c9ad5 · 2026-07-25 · MDR Git

Formal-core: explicit e-process construction (app:eprocess)

Add appendix section giving the mixture e-value construction underlying def:test:
per-pair betting supermartingales for the TV-ball adequacy null, mixed over
subsets/sign/betting-fraction, combined across pairs by a weighted sum. Yields the
Ville false-alarm bound e^{-b_i}, the dominating-component property used in
lem:test-consistency and prop:capacity, and the deterministic likelihood-ratio
reduction. def:test now points to it instead of "a standard mixture construction."

Compiles, 42pp.

Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>


 paper/tbv_mdr_Paper01-v04.pdf | Bin 309956 -> 313819 bytes
 paper/tbv_mdr_Paper01-v04.tex |  22 +++++++++++++++++++++-
 2 files changed, 21 insertions(+), 1 deletion(-)
## b070314 · 2026-07-25 · MDR Git

Formal-core Phase 3: strengthen prop:diagnostic with a genericity result

Add prop:punishing: since the consequence carries the realized payoff, a
payoff-relevantly false theory is exposed the moment its prescribed (objectively
suboptimal) action is played, unless the realized consequence exactly matches the
prediction. "Strictly punishing" primitives (an OPEN condition on Theta,tau,pi) are
diagnostic => every SCUE free of payoff-relevant error; diagnosticity is generic,
concealment the knife-edge (beta=1 in the example). Turns the near-tautological
diagnostic result into a substantive primitive-condition/genericity statement.

Compiles, 42pp.

Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>


 paper/tbv_mdr_Paper01-v04.pdf | Bin 313819 -> 315398 bytes
 paper/tbv_mdr_Paper01-v04.tex |  13 +++++++++++++
 2 files changed, 13 insertions(+)
## be4b0f9 · 2026-07-25 · MDR Git

Apply verification findings on the new formal-core material

Independent adversarial check of the new math (rest-points ii-b recast,
prop:capacity, app:eprocess, prop:punishing): no blockers; fixes applied:
- prop:punishing [MAJOR]: "generic/knife-edge" was an eta=0 claim; for eta>0 the
  concealing region is open too. Recast as "Diagnosticity is robust" (openness =>
  robustness; knife-edge only as eta->0). Also quantify strict punishment over every
  ACTIVE THEORY at the on-path conditional (not "a theory prescribes"), fixing the
  >=3-action/mixed-belief looseness.
- prop:capacity proof: dominate by a fixed-fraction bet with i.i.d. log-increments
  (the mixture itself isn't one); rename w_{j*} -> v_{j*}.
- app:eprocess: state lambda_max <= 1/(1+eta) for nonnegativity (eta=0 exception).
- def:test / lem / prop:capacity: growth rate is the "betting exponent," not KL.

rest-points(ii-b), prop:capacity(ii), app:eprocess core, rem:two-sources verified
sound as-is. Compiles, 42pp.

Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>


 paper/tbv_mdr_Paper01-v04.pdf | Bin 315398 -> 315709 bytes
 paper/tbv_mdr_Paper01-v04.tex |  26 ++++++++++++++------------
 2 files changed, 14 insertions(+), 12 deletions(-)
## 97057a0 · 2026-07-25 · MDR Git

Add notes/STATUS.md: orientation note (where we are, what's next)

Human-readable summary for picking the work back up: current model/setup, the new
propositions, locked decisions, and the outstanding tasks (front-matter sync deferred).

Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>


 notes/STATUS.md | 70 ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
 1 file changed, 70 insertions(+)
## f36ac71 · 2026-08-12 · MDR Git

Establish GPTedit-01 as authoritative manuscript



 paper/tbv_mdr_GPTedit-01.pdf                              | Bin 0 -> 318225 bytes
 paper/{tbv_mdr_Paper01-v04.tex => tbv_mdr_GPTedit-01.tex} |  46 ++++++++++++++++++++++++++++++----------------
 paper/tbv_mdr_Paper01-v04.pdf                             | Bin 315709 -> 0 bytes
 3 files changed, 30 insertions(+), 16 deletions(-)
## b1e13b9 · 2026-08-12 · MDR Git

Add shared AI editing controls and redraft plan



 AGENTS.md             | 111 ++++++++++++++++++++++++++++++++++++++++++++++++
 README.md             |  16 +++++--
 notes/REDRAFT_PLAN.md | 206 ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
 notes/STATUS.md       |  13 ++++--
 4 files changed, 339 insertions(+), 7 deletions(-)
## ebb306c · 2026-08-12 · MDR Git

Complete B1 evidence-process audit and promote GPTedit-02



 AGENTS.md                                                |   6 ++--
 README.md                                                |   4 +--
 notes/REDRAFT_PLAN.md                                    |   7 ++--
 notes/STATUS.md                                          |  13 ++++---
 paper/{tbv_mdr_GPTedit-01.pdf => tbv_mdr_GPTedit-02.pdf} | Bin 318225 -> 322225 bytes
 paper/{tbv_mdr_GPTedit-01.tex => tbv_mdr_GPTedit-02.tex} | 108 ++++++++++++++++++++++++++++++++++++-------------------
 6 files changed, 90 insertions(+), 48 deletions(-)
## 0babced · 2026-08-13 · MDR Git

Complete B2 formal-hygiene audit and promote GPTedit-03



 AGENTS.md                                                |   6 +--
 README.md                                                |   4 +-
 notes/REDRAFT_PLAN.md                                    |  11 +++++-
 notes/STATUS.md                                          |  16 +++++---
 paper/tbv_mdr_GPTedit-02.pdf                             | Bin 322225 -> 0 bytes
 paper/tbv_mdr_GPTedit-03.pdf                             | Bin 0 -> 324078 bytes
 paper/{tbv_mdr_GPTedit-02.tex => tbv_mdr_GPTedit-03.tex} | 111 ++++++++++++++++++++++++++++++-------------------------
 7 files changed, 84 insertions(+), 64 deletions(-)
## 18ad0b9 · 2026-08-13 · MDR Git

Complete B3 and promote GPTedit-04



 AGENTS.md                                                |   6 +-
 README.md                                                |   4 +-
 notes/REDRAFT_PLAN.md                                    |   7 ++-
 notes/STATUS.md                                          |  15 +++--
 paper/{tbv_mdr_GPTedit-03.pdf => tbv_mdr_GPTedit-04.pdf} | Bin 324078 -> 330417 bytes
 paper/{tbv_mdr_GPTedit-03.tex => tbv_mdr_GPTedit-04.tex} | 170 +++++++++++++++++++++++++++++++++++++++++--------------
 6 files changed, 145 insertions(+), 57 deletions(-)
## afc0202 · 2026-08-13 · MDR Git

Complete B4 and promote GPTedit-05



 AGENTS.md                                                |   6 +--
 README.md                                                |   4 +-
 notes/REDRAFT_PLAN.md                                    |   9 ++--
 notes/STATUS.md                                          |  12 +++---
 paper/tbv_mdr_GPTedit-04.pdf                             | Bin 330417 -> 0 bytes
 paper/tbv_mdr_GPTedit-05.pdf                             | Bin 0 -> 334422 bytes
 paper/{tbv_mdr_GPTedit-04.tex => tbv_mdr_GPTedit-05.tex} | 123 +++++++++++++++++++++++++++++++++----------------------
 7 files changed, 92 insertions(+), 62 deletions(-)
## a019dd3 · 2026-08-14 · MDR Git

Complete B5 and promote GPTedit-06



 AGENTS.md                                                |   6 ++--
 README.md                                                |   4 +--
 notes/REDRAFT_PLAN.md                                    |   9 +++--
 notes/STATUS.md                                          |  11 +++---
 paper/tbv_mdr_GPTedit-05.pdf                             | Bin 334422 -> 0 bytes
 paper/tbv_mdr_GPTedit-06.pdf                             | Bin 0 -> 336608 bytes
 paper/{tbv_mdr_GPTedit-05.tex => tbv_mdr_GPTedit-06.tex} | 106 ++++++++++++++++++++++++++++++++-----------------------
 7 files changed, 79 insertions(+), 57 deletions(-)
## 7646420 · 2026-08-14 · MDR Git

Complete B6 and promote GPTedit-07



 AGENTS.md                                                |   6 +-
 README.md                                                |   4 +-
 notes/REDRAFT_PLAN.md                                    |   9 ++-
 notes/STATUS.md                                          |  11 ++--
 paper/{tbv_mdr_GPTedit-06.pdf => tbv_mdr_GPTedit-07.pdf} | Bin 336608 -> 343389 bytes
 paper/{tbv_mdr_GPTedit-06.tex => tbv_mdr_GPTedit-07.tex} | 174 ++++++++++++++++++++++++++++++++++++++++++++++++-------
 6 files changed, 169 insertions(+), 35 deletions(-)
## 6ba14cb · 2026-08-14 · MDR Git

Complete B7 and promote GPTedit-08



 AGENTS.md                                                |   6 +-
 README.md                                                |   4 +-
 notes/REDRAFT_PLAN.md                                    |   7 +-
 notes/STATUS.md                                          |  27 +++--
 paper/tbv_mdr_GPTedit-07.pdf                             | Bin 343389 -> 0 bytes
 paper/tbv_mdr_GPTedit-08.pdf                             | Bin 0 -> 339669 bytes
 paper/{tbv_mdr_GPTedit-07.tex => tbv_mdr_GPTedit-08.tex} | 307 +++++++++++++++++++++++++++++--------------------------
 7 files changed, 182 insertions(+), 169 deletions(-)
## 48c0c14 · 2026-08-14 · MDR Git

Complete B8 and promote GPTedit-09



 AGENTS.md                                                |   6 +++---
 README.md                                                |   8 +++++---
 notes/REDRAFT_PLAN.md                                    |  15 +++++++++++++--
 notes/STATUS.md                                          |  24 +++++++++++-------------
 paper/{tbv_mdr_GPTedit-08.pdf => tbv_mdr_GPTedit-09.pdf} | Bin 339669 -> 339669 bytes
 paper/{tbv_mdr_GPTedit-08.tex => tbv_mdr_GPTedit-09.tex} |   2 +-
 6 files changed, 33 insertions(+), 22 deletions(-)
## 0a18f80 · 2026-08-15 · MDR Git

v10 session 0: baseline + mechanical demotions

Open the GPTedit-10 expository revision (plan + runbook committed as
authorization). Governance blocks appended to AGENTS.md and STATUS.md.
Phase 0: working copy tbv_mdr_GPTedit-10.tex (non-authoritative header),
baseline build, METRICS.md baseline. Phase 1: ten items demoted verbatim
to new Appendix D with pointers; six remarks converted to prose in place.
GPTedit-09 untouched and remains authoritative.

Co-Authored-By: Claude Fable 5 <noreply@anthropic.com>


 AGENTS.md                     |   13 +
 notes/REVISION_PLAN_v10.md    |  257 ++++++++++++
 notes/REVISION_RUNBOOK_v10.md |  171 ++++++++
 notes/STATUS.md               |    5 +
 notes/revision_v10/METRICS.md |   79 ++++
 paper/tbv_mdr_GPTedit-10.pdf  |  Bin 0 -> 347094 bytes
 paper/tbv_mdr_GPTedit-10.tex  | 1758 +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
 7 files changed, 2283 insertions(+)
