# Findings report · questions-before-priors

Findings only: no verdict, score, ranking, or recommendation. Every finding points into the record and into the standard it was checked against.

| | |
|---|---|
| Run | `20261028-233241-journal-047023d` |
| Run by | journal, round 1 |
| Record | `sha256:047023dde1714548` |
| Versions | protocol formal-0.3 · checks 0.6.0 · generator 0.1.0 · standard formal-0.4 |
| Check code | `9567e947c9c5` |
| Models | claude-opus-5-5 (bundle, 9 answers) |
| AI appendix | submitted with the record |
| Generator stamp | generator 0.1.0, run `20261027-040052-author-cfeeaca`; inputs changed since generation: declarations.yaml, paper/paper.md; edited after generation: ai-appendix/claims.yaml (a fact, not a finding) |
| Bundles answered | 9 |

| Model-judged check | Agreement | Minimum | Published as a check |
|---|---|---|---|
| completeness | 0.00 | 0.50 | no, below tolerance |
| resolution | 0.82 | 0.80 | yes |
| contribution | 1.00 | 0.67 | yes |

## Level 1 · Form

_No findings._

## Level 2 · Correspondence

### F-2-resolution-01 · `pointer_missing`

**The evidence for claim C24 does not say what the claim says (only in part).**

- Record: `claims:C24`
- Standard: `protocol/formal.md#P10`
- Why: Proposition 4.1 and Remark 4.2 establish that updating cannot expand the language and that the posterior does not signal failure, but only in the stochastic full-support case (in the deterministic case the posterior becomes undefined), and the span names the detector as 'the consistency test of the next section' rather than establishing it as causal dissonance. / Proposition 4.1 and Remark 4.2 support that updating cannot expand the language and that a faculty outside the posterior (the consistency test) is needed, but the confident-not-alarmed result is established only for the stochastic full-support setting, whereas the claim states it without that condition. / Proposition 4.1 and Remark 4.2 establish that updating cannot expand the language and that a full-support misspecified posterior grows confident in the stochastic case, but the span names the needed faculty only as 'the consistency test of the next section' and does not identify it as causal dissonance, the statistical rejection of every expressible theory, nor cover the deterministic case where the posterior becomes undefined rather than confident.
- Produced by: claude-opus-5-5 via prompt `resolution@0.6.0`, agreement 3/3

### F-2-resolution-02 · `pointer_missing`

**The evidence for claim C29 does not say what the claim says (only in part).**

- Record: `claims:C29`
- Standard: `protocol/formal.md#P10`
- Why: Theorem 9.4 and the examples support the death of inquiry and SCUEs preserving false theories, heterogeneity and payoff gaps, but the evidence also allows permanent dissonant stasis (not every agent with fitting models), gives only a necessity condition (for payoff-relevant collective error) rather than 'precisely when', and its persistence instance keeps differences despite strategic variety, because inquiry is priced below cost. / Theorem 9.4 supports the almost-sure death of awareness change and inquiry, but under Assumption 9.3, with part (d) conditional on play stabilizing and dissonant stasis left open (so not every agent ends in a world where models fit), and the range shows no iff characterization that persistence occurs exactly when both corrective forces are absent; its persistence instance turns on inquiry cost. / Theorem 9.4 and Propositions 9.9 and 9.11 support the absorption result and SCUEs preserving false theories, heterogeneous awareness and performance differences, but the evidence allows agents to end in dissonant stasis rather than all in a Bayesian world, gives only necessity of absent corrective forces for payoff-relevant error, and its persistence instance relies on inquiry priced above leverage even with differentiated play, so the 'precisely when' biconditional is not supported.
- Produced by: claude-opus-5-5 via prompt `resolution@0.6.0`, agreement 3/3

### F-2-resolution-03 · `pointer_missing`

**The evidence for claim C30 does not say what the claim says (only in part).**

- Record: `claims:C30`
- Standard: `protocol/formal.md#P10`
- Why: Proposition 9.9 and the example show configurations with different terminal languages and payoffs, and the text asserts path dependence, but the instance is stipulated (firm 1 given the row refinement, firm 2 left coarse), so the evidence does not derive that differences arise because experiences posed different questions, nor the 'microfoundation before probability' and 'questions died before asked' conclusions. / The span states path dependence for agents with identical preferences and Bayesian competence whose histories posed different questions, but its instances posit the firms' terminal refinements rather than deriving them from different experiences, repairs and extinction points, and it does not state the 'begins before probability' microfoundation or that some questions died before being asked.
- Produced by: claude-opus-5-5 via prompt `resolution@0.6.0`, agreement 2/3

### F-2-resolution-04 · `pointer_missing`

**The evidence for claim C31 does not say what the claim says (only in part).**

- Record: `claims:C31`
- Standard: `protocol/formal.md#P10`
- Why: The cited paragraph supports the paper's own contribution (endogenizing the expansion event), but its only statement about what Bryan et al. (2022) show and leave open is the claim's own sentence, with no independent support for that characterization. / The surrounding passage supports that the paper endogenizes the awareness-expansion event, but nothing beyond the claim's own sentence supports what Bryan et al. (2022) show or leave open.
- Produced by: claude-opus-5-5 via prompt `resolution@0.6.0`, agreement 2/3
- Not in the author's own findings report

### F-2-resolution-05 · `pointer_missing`

**The evidence for claim C32 does not say what the claim says (only in part).**

- Record: `claims:C32`
- Standard: `protocol/formal.md#P10`
- Why: Remark 9.2 supports dissonance as the detector and on-path restoration of the grain of truth after each refinement, but the span does not show that the fixed-language models are recovered as the special case in which awareness never changes; it says only that a SCUE with sufficient partitions and near-true beliefs is an SCE. / Remark 9.2 supports the language-level failure of the grain of truth, dissonance as its detector, and on-path restoration after each successful refinement, but the evidence recovers self-confirming equilibrium only when partitions are sufficient for tau and beliefs concentrate near the truth, not as the case in which awareness never changes. / Remark 9.2 states the language-level failure of the grain of truth, dissonance as its detector, and on-path restoration after refinement, but the span does not state that fixed-language models are recovered as the special case in which awareness never changes; it instead gives SCE as the case of sufficient partitions with beliefs near the truth.
- Produced by: claude-opus-5-5 via prompt `resolution@0.6.0`, agreement 3/3

### F-2-resolution-06 · `pointer_missing`

**The evidence for claim C33 does not say what the claim says (only in part).**

- Record: `claims:C33`
- Standard: `protocol/formal.md#P10`
- Why: Theorem 6.5 and the example show that observationally equivalent worlds with different off-record content drive nonidentification, but they give one constructed instance and do not establish that such equivalent systems are generic. / Theorem 6.5 and the row/column example show that observationally equivalent worlds defeat truth-blind rules, but the evidence neither states that on-path data constrain F only at visited pairs nor shows that such equivalent systems are generic rather than merely possible. / Theorem 6.5 and the row/column example show observationally equivalent worlds driving nonidentification, but the span does not state that on-path data constrain F only at visited state-profile pairs or that such equivalent systems are generic.
- Produced by: claude-opus-5-5 via prompt `resolution@0.6.0`, agreement 3/3

### F-2-resolution-07 · `pointer_missing`

**The evidence for claim C35 does not say what the claim says (only in part).**

- Record: `claims:C35`
- Standard: `protocol/formal.md#P10`
- Why: Equation (4) shows that the within-cell mixture depends on the profile through S(C,a), which rivals' finer partitions shape, but the span does not establish that this dependence is precisely what generates the diagnostic contrasts (the paper later names environmental punishment as a second source). / Equation (4) shows the on-path conditional is a within-cell mixture over S(C,a), which depends on rivals' policies, but the evidence does not show that this profile dependence is precisely what generates the contrasts the diagnostic apparatus uses.
- Produced by: claude-opus-5-5 via prompt `resolution@0.6.0`, agreement 2/3
- Not in the author's own findings report

### F-2-resolution-08 · `pointer_missing`

**The evidence for claim C36 does not say what the claim says (only in part).**

- Record: `claims:C36`
- Standard: `protocol/formal.md#P10`
- Why: Definition 9.1 identifies conditions (i)-(ii) with fixed-language self-confirming conditions and says that a SCUE with sufficient partitions and near-true beliefs is an SCE, but it does not state that with awareness fixed the model is a Kalai-Lehrer/Ryall interaction whose stable configurations are SCE. / Definition 9.1 identifies conditions (i)-(ii) with the fixed-language self-confirming conditions and recovers SCE when partitions are sufficient for tau, but it does not show that the stable configurations are self-confirming equilibria whenever awareness never changes, nor the correspondence to the Kalai-Lehrer and Ryall learners. / Definition 9.1 relates SCUE conditions (i)-(ii) to the self-confirming conditions of the fixed-language tradition and calls a SCUE with sufficient partitions and near-true beliefs a self-confirming equilibrium, but it does not state that with awareness never changing the model reduces to Kalai-Lehrer/Ryall Bayesian learners whose stable configurations are self-confirming equilibria.
- Produced by: claude-opus-5-5 via prompt `resolution@0.6.0`, agreement 3/3

### F-2-resolution-09 · `pointer_missing`

**The evidence for claim C39 does not say what the claim says (only in part).**

- Record: `claims:C39`
- Standard: `protocol/formal.md#P10`
- Why: Proposition 5.5 links exposure to dissonance but does not establish the two-source decomposition (strategic differentiation versus observable environmental punishment), which appears only as the claim's own assertion, and the section-9 role is a forward reference outside the span. / Proposition 5.5 and its proof link exposure to dissonance but say nothing about the sources of exposure; outside the claim's own sentence, nothing in the evidence establishes the two sources or their return as the section-9 corrective forces.
- Produced by: claude-opus-5-5 via prompt `resolution@0.6.0`, agreement 2/3
- Not in the author's own findings report

### F-2-resolution-10 · `pointer_missing`

**The evidence for claim C42 does not say what the claim says (only in part).**

- Record: `claims:C42`
- Standard: `protocol/formal.md#P10`
- Why: Remark 6.3 in the span establishes that existence is guaranteed only with deterministic mechanisms, but the 'typically multiple' minimal restorations rest on the example, which lies outside the cited lines and is not otherwise shown. / Remark 6.3 supports that existence of a restoration is guaranteed only in the deterministic case, but the example that is supposed to show minimal restorations are typically multiple lies outside the cited range, and nothing in the range establishes that multiplicity.
- Produced by: claude-opus-5-5 via prompt `resolution@0.6.0`, agreement 2/3
- Not in the author's own findings report

### F-2-resolution-11 · `pointer_missing`

**The evidence for claim C44 does not say what the claim says (only in part).**

- Record: `claims:C44`
- Standard: `protocol/formal.md#P10`
- Why: The section shows that the rule is defined at dissonance, where the posterior is undefined, and that it is computed from the record, but Definitions 7.2-7.3 build Lambda_i and Theta_i(t) by quantifying over the restorative refinements in R(P_i,r_i), and the section-3.5 disciplines are not in the span, so 'never over candidate representations' and 'respects every discipline' are not shown. / The section supports that the rule operates where the posterior is undefined and that B_i is computable from the record and invariant across repairs, but equation (6) through Theta_i(t) and Lambda_i explicitly ranges over R(P_i, r_i), the restorative refinements, so the evidence does not bear out 'never over candidate representations', and the section 3.5 disciplines are not in the range. / The section shows the leverage statistic is computed from retained tokens at the point where the posterior is undefined, but the span does not show the rule respects the disciplines of section 3.5, and its definitions of Lambda_i and Theta_i(t) range over the admissible repairs in R rather than never referring to candidate representations.
- Produced by: claude-opus-5-5 via prompt `resolution@0.6.0`, agreement 3/3

### F-2-resolution-12 · `pointer_missing`

**The evidence for claim C52 does not say what the claim says (only in part).**

- Record: `claims:C52`
- Standard: `protocol/formal.md#P10`
- Why: The appendix shows that part (d) and Proposition 9.5(i) condition on an eventually constant profile, that the dominance thresholds make one action per cell strictly dominant in the featured configurations, and that part (b) relies on the success bound, but it does not show that dropping the bound makes perpetually elected, perpetually failing inquiry an absorbing pattern. / The appendix proofs condition part (d) and Proposition 9.5(i) on eventually constant play, and the dominance-threshold computation shows strict dominance in the featured configurations, but the evidence only shows that part (b) relies on the success bound; it does not exhibit the perpetually elected, perpetually failing pattern as possible without it. / The appendix shows Theorem 9.4(d) and Proposition 9.5 condition on an eventually constant profile and that certainty in a label makes the labeled action strictly dominant in the trap and opening configurations, but it does not state that dropping the success bound permits a perpetually elected, perpetually failing inquiry pattern; it only uses the bound to rule out infinitely many elections.
- Produced by: claude-opus-5-5 via prompt `resolution@0.6.0`, agreement 3/3

### F-2-resolution-13 · `pointer_missing`

**The evidence for claim C54 does not say what the claim says (only in part).**

- Record: `claims:C54`
- Standard: `protocol/formal.md#P10`
- Why: Proposition 9.9's instances show divergent terminal languages and payoffs, but they are stipulated configurations, and the span shows neither that the order of experiences shapes the terminal language nor that agents converge to the same behavior while keeping different representations (the persistence instance has different behavior). / The Proposition 9.9 discussion supports identical agents ending with different languages and payoffs through histories that posed different questions, but the range does not show that the order of experiences shapes the terminal language, nor any instance in which agents converge to the same behavior while keeping permanently different representations. / The span states path dependence from different questions for agents with identical preferences and Bayesian competence, but it does not show that technologies' different repairs or the order of experiences shape terminal languages, and it does not show agents converging to the same behavior with different representations; its persistence instance has different behavior and payoffs.
- Produced by: claude-opus-5-5 via prompt `resolution@0.6.0`, agreement 3/3

### F-2-resolution-14 · `pointer_missing`

**The evidence for claim C58 does not say what the claim says (only in part).**

- Record: `claims:C58`
- Standard: `protocol/formal.md#P10`
- Why: Theorem 9.4(d) and Remark 9.7 support zero-leverage dissonant stasis as a rational absorbing outcome, but the span does not derive the prediction that tolerated anomalies accumulate in transparent-consequence environments near decisions with insensitive robust optima, and Proposition 9.5(i) excludes agents in dissonant stasis from the SCUE. / Theorem 9.4(d) and Remark 9.7 support rational zero-leverage dissonant stasis, but they allow stasis with positive leverage priced below cost, the absorbing stasis lies outside the SCUE definition rather than being an equilibrium in the paper's sense, and nothing in the range derives the prediction that tolerated anomalies accumulate in transparent-consequence environments. / Theorem 9.4(d) and Remark 9.7 support that zero-leverage dissonant stasis is an absorbing, rational anomaly tolerance, but the span does not support the prediction that tolerated anomalies accumulate in transparent-consequence environments near action-insensitive decisions, and Proposition 9.5(i) excludes dissonant-stasis agents from the equilibrium characterization.
- Produced by: claude-opus-5-5 via prompt `resolution@0.6.0`, agreement 3/3

### F-2-resolution-15 · `pointer_missing`

**The evidence for claim C60 does not say what the claim says (only in part).**

- Record: `claims:C60`
- Standard: `protocol/formal.md#P10`
- Why: Definition 9.1 shows that the SCUE adds two epistemic conditions to the self-confirming ones (the language survives its evidence, the question has no priced value), but the span does not show that these conditions rather than the strategic ones carry the new results. / Definition 9.1 shows SCUE adds two epistemic conditions to the self-confirming ones (the language survives its evidence, no question has priced value), but nothing in the evidence shows that these conditions, rather than the strategic ones, carry the paper's new results.
- Produced by: claude-opus-5-5 via prompt `resolution@0.6.0`, agreement 2/3

### F-2-resolution-16 · `pointer_missing`

**The evidence for claim C62 does not say what the claim says (only in part).**

- Record: `claims:C62`
- Standard: `protocol/formal.md#P10`
- Why: Proposition 6.2 supports the cellwise-coherence framing (graph coloring follows when deterministic labels pin mechanisms pairwise), but the span gives no instance or argument that a three-mechanism mixture can defeat every single mechanism while each pair is accommodatable, so the hypergraph case is only asserted. / Proposition 6.2 supports restoration as the separation of incoherent sets, but the evidence neither shows that incoherence is pairwise in the deterministic example nor exhibits a three-mechanism mixture that defeats every single mechanism while each pair is accommodatable.
- Produced by: claude-opus-5-5 via prompt `resolution@0.6.0`, agreement 2/3
- Not in the author's own findings report

## Level 3 · Warrant (SIEVE)

_No findings._
