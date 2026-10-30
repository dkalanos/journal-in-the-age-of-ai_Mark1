# Findings report · questions-before-priors

Findings only: no verdict, score, ranking, or recommendation. Every finding points into the record and into the standard it was checked against.

| | |
|---|---|
| Run | `20261028-232034-author-047023d` |
| Run by | author |
| Record | `sha256:047023dde1714548` |
| Versions | protocol formal-0.3 · checks 0.6.0 · generator 0.1.0 · standard formal-0.4 |
| Check code | `9567e947c9c5` |
| Models | claude-opus-5-5 (bundle, 9 answers) |
| AI appendix | submitted with the record |
| Generator stamp | generator 0.1.0, run `20261027-040052-author-cfeeaca`; inputs changed since generation: declarations.yaml, paper/paper.md; edited after generation: ai-appendix/claims.yaml (a fact, not a finding) |
| Bundles answered | 9 |

| Model-judged check | Agreement | Minimum | Published as a check |
|---|---|---|---|
| completeness | 0.38 | 0.50 | no, below tolerance |
| resolution | 0.97 | 0.80 | yes |
| contribution | 1.00 | 0.67 | yes |

## Level 1 · Form

_No findings._

## Level 2 · Correspondence

### F-2-resolution-01 · `pointer_missing`

**The evidence for claim C24 does not say what the claim says (only in part).**

- Record: `claims:C24`
- Standard: `protocol/formal.md#P10`
- Why: Proposition 4.1 and Remark 4.2 support that updating cannot expand the language and that a misspecified posterior grows confident, so a faculty outside the posterior is needed; but the evidence names that faculty only as 'the consistency test of the next section' and never identifies it as causal dissonance, the statistical rejection of every expressible theory. / Proposition 4.1 and Remark 4.2 support that conditioning cannot expand the language and that detection needs a faculty outside the posterior (the consistency test), but the evidence establishes the confident-not-alarmed posterior only in the stochastic full-support setting, whereas the claim states it unconditionally. / Proposition 4.1 and Remark 4.2 support that updating cannot expand the language and that a misspecified posterior grows confident, but only in the stochastic full-support setting (the deterministic case, where likelihoods hit zero, is not covered), and the evidence names the faculty only as the next section's consistency test without identifying it as causal dissonance, the rejection of every expressible theory.
- Produced by: claude-opus-5-5 via prompt `resolution@0.6.0`, agreement 3/3

### F-2-resolution-02 · `pointer_missing`

**The evidence for claim C29 does not say what the claim says (only in part).**

- Record: `claims:C29`
- Standard: `protocol/formal.md#P10`
- Why: The evidence supports a.s. death of refinement and inquiry and the existence of rest points that preserve false theories, heterogeneity and payoff gaps; it lacks the claim's 'precisely/exactly when' biconditional, since Proposition 9.11 gives only that payoff-relevant collective error requires absence of both forces, and Theorem 9.4(d) lets agents end in dissonant stasis rather than a Bayesian world where models fit. / Theorem 9.4 supports the death of awareness change and inquiry, but it allows agents to end in dissonant stasis rather than a Bayesian world where models fit; Proposition 9.11 gives only the necessity of both forces' absence for payoff-relevant error; and the persistence instance keeps performance differences under differentiated play because inquiry is priced below cost, so the evidence does not support 'precisely when'. / Theorem 9.4 and the examples support the death of inquiry and the existence of rest points with false theories, heterogeneous awareness and persistent payoff gaps, but the evidence lacks the claimed 'precisely when' link for heterogeneity and performance differences: Proposition 9.11 gives only necessity, and only for payoff-relevant error, the persistence instance turns on inquiry cost while differentiated play is present, and Theorem 9.4(d) also allows dissonant stasis, not every agent in a Bayesian world.
- Produced by: claude-opus-5-5 via prompt `resolution@0.6.0`, agreement 3/3

### F-2-resolution-03 · `pointer_missing`

**The evidence for claim C30 does not say what the claim says (only in part).**

- Record: `claims:C30`
- Standard: `protocol/formal.md#P10`
- Why: The evidence states that agents with identical preferences and Bayesian competence facing the same system end at different languages and payoffs because their histories posed different questions, with processes dying economically; it does not state the role of technologies producing different repairs or the microfoundation 'beginning before probability' and questions dying before they are asked. / The span states that agents with identical preferences and competence end at different languages and payoffs because their histories posed different questions, and that the eroding process dies economically, but it shows no channel through different repairs (the instance has one firm refined and one coarse) and does not state the before-probability microfoundation. / Proposition 9.9's discussion supports that agents with identical preferences and Bayesian competence end with different languages and payoffs because their histories posed different questions, but the evidence does not show the further mechanisms the claim names (different technology repairs, inquiry extinguished at different points) in this instance, where firm 2 simply stays coarse, nor that heterogeneity begins before probability.
- Produced by: claude-opus-5-5 via prompt `resolution@0.6.0`, agreement 3/3

### F-2-resolution-04 · `pointer_missing`

**The evidence for claim C32 does not say what the claim says (only in part).**

- Record: `claims:C32`
- Standard: `protocol/formal.md#P10`
- Why: Remark 9.2 states the language-level grain-of-truth failure, dissonance as detector, and on-path restoration after each refinement, but the evidence does not state that fixed-language models are recovered as the special case in which awareness never changes; it only says a SCUE with sufficient partitions and beliefs near the truth is a self-confirming equilibrium. / Remark 9.2 states that dissonance detects language-level grain-of-truth failure and that each refinement restores the grain on-path, but the span recovers the fixed-language case only as a SCUE with partitions sufficient for tau, not as the special case in which awareness never changes. / Remark 9.2 states that grain-of-truth failure can be linguistic, that dissonance detects it, and that each refinement restores the grain on-path, but the evidence does not state that the fixed-language models are recovered as the special case in which awareness never changes; Definition 9.1 gives instead the reduction to self-confirming equilibrium when partitions are sufficient and beliefs are near the truth.
- Produced by: claude-opus-5-5 via prompt `resolution@0.6.0`, agreement 3/3

### F-2-resolution-05 · `pointer_missing`

**The evidence for claim C33 does not say what the claim says (only in part).**

- Record: `claims:C33`
- Standard: `protocol/formal.md#P10`
- Why: Theorem 6.5 and the example show that observationally equivalent assignments defeat identification and construct one instance, but the evidence does not state that on-path data constrain F only at visited state-profile pairs or that such equivalent systems are generic. / Theorem 6.5 and the row/column example show that observationally equivalent worlds with different counterfactual content exist and drive nonidentification, but the evidence does not show that such systems are generic or state that on-path data constrain F only at visited pairs. / The evidence shows observational equivalence driving Theorem 6.5 and exhibits one such pair of worlds that agree at the labeled states, but it does not state that on-path data constrain F only at visited state-profile pairs, nor that such equivalent systems are generic.
- Produced by: claude-opus-5-5 via prompt `resolution@0.6.0`, agreement 3/3

### F-2-resolution-06 · `pointer_missing`

**The evidence for claim C36 does not say what the claim says (only in part).**

- Record: `claims:C36`
- Standard: `protocol/formal.md#P10`
- Why: The SCUE definition identifies conditions (i)-(ii) as the self-confirming conditions of the fixed-language tradition and says a SCUE with sufficient partitions and beliefs near the truth is a self-confirming equilibrium, but it does not state that with awareness never changing the model is a repeated interaction of subjectively rational Bayesian learners (Kalai-Lehrer, Ryall) whose stable configurations are self-confirming equilibria. / Definition 9.1 notes that conditions (i)-(ii) are the self-confirming conditions of the fixed-language tradition and that a SCUE with partitions sufficient for tau is an SCE, but it does not establish that with never-changing awareness the model reduces to Kalai-Lehrer/Ryall Bayesian learners whose stable configurations are SCE. / Definition 9.1 identifies conditions (i)-(ii) with the fixed-language self-confirming conditions and gives a reduction to self-confirming equilibrium when partitions are sufficient and beliefs near the truth, but it does not state that with awareness never changing the model is a repeated game among subjectively rational Bayesian learners whose stable configurations are self-confirming equilibria.
- Produced by: claude-opus-5-5 via prompt `resolution@0.6.0`, agreement 3/3

### F-2-resolution-07 · `pointer_missing`

**The evidence for claim C44 does not say what the claim says (only in part).**

- Record: `claims:C44`
- Standard: `protocol/formal.md#P10`
- Why: The evidence shows B_i is computed from retained tokens and their outcomes, priced where the posterior is undefined and invariant to which repair arrives, but it does not lay out the disciplines of section 3.5 so that respect for 'every' one can be read off, and Theta_i(t) is itself defined by quantifying over admissible repairs. / The span shows the rule operating at dissonance where the posterior is undefined and computable from record, Theta and u_i, but section 3.5's disciplines are not in it, and Definitions 7.2-7.3 build Lambda_i and Theta_i(t) by quantifying over the restorative refinements R(P_i, r_i), so the evidence does not show the leverage never quantifies over candidate representations. / The evidence supports that the rule prices inquiry where the posterior is undefined and that equation (6) sums over retained tokens, but it does not state the section 3.5 disciplines or that leverage never quantifies over candidate representations; Theta_i(t) is in fact built from the set of restorative refinements R(P_i, r_i).
- Produced by: claude-opus-5-5 via prompt `resolution@0.6.0`, agreement 3/3

### F-2-resolution-08 · `pointer_missing`

**The evidence for claim C52 does not say what the claim says (only in part).**

- Record: `claims:C52`
- Standard: `protocol/formal.md#P10`
- Why: The appendix shows part (d) and Proposition 9.5(i) conditioned on eventually constant play, and the dominance computation shows certainty or belief asymmetry makes one action strictly dominant; but nothing in the evidence states that dropping the success bound of Assumption 9.3(ii) allows a perpetually elected, perpetually failing inquiry pattern. / The appendix proofs condition part (d) and Proposition 9.5 on an eventually constant profile, and Appendix B shows strict dominance in the opening and trap configurations, but nothing in the span shows that dropping the success bound makes perpetually elected, perpetually failing inquiry an absorbing pattern (part (b) merely relies on the bound). / The appendix shows that part (d) and the Proposition 9.5(i) proof condition on eventually constant play, and the dominance computation shows certainty makes one action per cell strictly dominant in the featured configurations, but nothing in the evidence states that dropping the success bound allows perpetually elected, perpetually failing inquiry; it only shows the bound is used in part (b).
- Produced by: claude-opus-5-5 via prompt `resolution@0.6.0`, agreement 3/3

### F-2-resolution-09 · `pointer_missing`

**The evidence for claim C53 does not say what the claim says (only in part).**

- Record: `claims:C53`
- Standard: `protocol/formal.md#P10`
- Why: Proposition 7.4 and its proof show that B_i = 0 (including irreparable records) makes abstention optimal at any positive cost; the evidence does not show the agent recognizes the condition, that irreparability means no repair exists at any price, or the 'precisely when' characterization, since its rule also makes tolerance rational whenever lambda_i B_i < gamma_i with positive leverage. / Proposition 7.4 supports that B_i = 0 (including irreparable records) makes repair worthless and abstention optimal at any positive cost, but the same evidence makes abstention rational whenever lambda_i B_i < gamma_i, so it does not support tolerance being rational 'precisely when' pinned distinctions carry no leverage. / Proposition 7.4 and its proof support that zero leverage, including irreparable records, makes repair worthless and abstention optimal, and that B_i > 0 iff some pinned rule robustly improves, but the evidence does not state that the stasis agent knows every expressible theory is rejected, or that an irreparable anomaly cannot be fixed at any price within the current grammar.
- Produced by: claude-opus-5-5 via prompt `resolution@0.6.0`, agreement 3/3

### F-2-resolution-10 · `pointer_missing`

**The evidence for claim C54 does not say what the claim says (only in part).**

- Record: `claims:C54`
- Standard: `protocol/formal.md#P10`
- Why: The evidence supports path-dependent divergence of languages and payoffs among otherwise identical agents because their histories posed different questions, but it does not state the role of different repairs, the before-probability chain from prior understanding to questions to languages, or that agents can converge to the same behavior with different representations (its instances have different behavior and payoffs). / The span (Proposition 9.9 and the Example 1 instances) shows different languages and payoffs from different histories, but no instance has agents converging to the same behavior with different representations (the persistence instance has different behavior), and neither the different-repairs channel nor order-of-experience dependence is exhibited. / Proposition 9.9's discussion supports path dependence: identical agents end with different languages and payoffs because their histories posed different questions, but the evidence does not show agents converging to the same behavior while keeping different representations (the persistence instance has different behavior), nor the claimed chain from heterogeneous prior understanding through questions to languages and the role of different technology repairs.
- Produced by: claude-opus-5-5 via prompt `resolution@0.6.0`, agreement 3/3

### F-2-resolution-11 · `pointer_missing`

**The evidence for claim C58 does not say what the claim says (only in part).**

- Record: `claims:C58`
- Standard: `protocol/formal.md#P10`
- Why: Theorem 9.4(d) and Remark 9.7 support that zero-leverage dissonant stasis is absorbing and rational for agents who know their account is broken, but the evidence does not state the prediction that tolerated anomalies accumulate in transparent-consequence environments near decisions whose robust optimum is insensitive to the unresolved structure. / Theorem 9.4(d) and Remark 9.7 support that agents can rest in dissonant stasis, knowingly broken and rationally not repairing, but the span gives no support for the prediction that tolerated anomalies accumulate in transparent-consequence environments, and Proposition 9.5(i) excludes agents in dissonant stasis from the SCUE. / Theorem 9.4(d) and Remark 9.7 support zero-leverage dissonant stasis as an absorbing, rationally tolerated condition, but the evidence does not contain the prediction that tolerated anomalies accumulate in transparent-consequence environments near decisions insensitive to the unresolved structure, and Proposition 9.5(i) excludes stasis agents from the SCUE, so 'equilibrium' holds only in the absorbing sense.
- Produced by: claude-opus-5-5 via prompt `resolution@0.6.0`, agreement 3/3

### F-2-resolution-12 · `pointer_missing`

**The evidence for claim C60 does not say what the claim says (only in part).**

- Record: `claims:C60`
- Standard: `protocol/formal.md#P10`
- Why: The SCUE definition states that conditions (iii)-(iv) are new epistemic conditions added to the self-confirming ones (the language survives its evidence, the question has no priced value), but it does not state that these conditions rather than the strategic ones carry the paper's new results. / Definition 9.1 shows the SCUE extends the self-confirming conditions with two epistemic conditions (the language survives its own evidence; no priced question), but the span does not show that these conditions rather than the strategic ones carry the new results. / Definition 9.1's commentary states that conditions (iii)-(iv) are the new epistemic ones extending the self-confirming conditions (the language survives its evidence, no question is priced), but it does not state that these conditions, rather than the strategic ones, carry the new results.
- Produced by: claude-opus-5-5 via prompt `resolution@0.6.0`, agreement 3/3

## Level 3 · Warrant (SIEVE)

_No findings._

## Below tolerance

These came from a check whose agreement across runs fell below its published minimum. They are reported, not published as findings.

### F-2-completeness-01 · `claim_unresolved`

**The paper states something the contribution rests on that the claims list lacks: "The record belongs in the state: dissonance status and leverage are functions of retained evidence, so two histories with identical partitions, beliefs, and policies but different records can differ in equilibrium status."**

- Record: `paper/paper.md:L1148-L1151`
- Standard: `protocol/formal.md#P10`
- Why: A claim that appears only in the narrative is one the machine cannot check (appendix C.3).
- Produced by: claude-opus-5-5 via prompt `completeness@0.6.0`, agreement 2/3

### F-2-completeness-02 · `claim_unresolved`

**The paper states something the contribution rests on that the claims list lacks: "Nothing in the mathematics represents the conscious act of insight itself; the model represents its products and its price, which is what an economic theory can responsibly claim."**

- Record: `paper/paper.md:L1434-L1437`
- Standard: `protocol/formal.md#P10`
- Why: A claim that appears only in the narrative is one the machine cannot check (appendix C.3).
- Produced by: claude-opus-5-5 via prompt `completeness@0.6.0`, agreement 2/3

### F-2-completeness-03 · `claim_unresolved`

**The paper states something the contribution rests on that the claims list lacks: "a variant folding components of $a$ into $x_i$ changes bookkeeping only."**

- Record: `paper/paper.md:L405-L406`
- Standard: `protocol/formal.md#P10`
- Why: A claim that appears only in the narrative is one the machine cannot check (appendix C.3).
- Produced by: claude-opus-5-5 via prompt `completeness@0.6.0`, agreement 2/3
