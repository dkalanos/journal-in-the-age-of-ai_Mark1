# Findings report · questions-before-priors

Findings only: no verdict, score, ranking, or recommendation. Every finding points into the record and into the standard it was checked against.

| | |
|---|---|
| Run | `20261029-043822-journal-4909a9e` |
| Run by | journal, round 2 |
| Record | `sha256:4909a9e7e9a126ec` |
| Versions | protocol formal-0.4 · checks 0.7.0 · generator 0.2.0 · standard formal-0.5 |
| Check code | `0f0dc2eff865` |
| Models | claude-opus-5-5 (bundle, 9 answers) |
| AI appendix | submitted with the record |
| Generator stamp | generator 0.1.0, run `20261021-074338-author-c6e282f`; inputs changed since generation: declarations.yaml, paper/paper.md; edited after generation: ai-appendix/claims.yaml (a fact, not a finding) |
| Bundles answered | 9 |

| Model-judged check | Agreement | Minimum | Published as a check |
|---|---|---|---|
| completeness | 0.43 | 0.50 | no, below tolerance |
| resolution | 0.93 | 0.80 | yes |
| contribution | 1.00 | 0.67 | yes |

## Level 1 · Form

_No findings._

## Level 2 · Correspondence

### F-2-resolution-01 · `evidence_partial` · main claim

**The evidence for claim C1 does not say what the claim says (only in part).**

- Record: `claims:C1`
- Standard: `protocol/formal.md#P10`
- Why: The evidence (section 11.1) supports question histories as an upstream source of heterogeneity, action-separation value, the independent-discrimination limit on warrant, and exposure/concealment, but it lacks the comparison with existing work, any statement that the semantic act producing the new hypothesis space is left primitive, and it only cites rather than states the existence of absorbing configurations; the question passage (L14-15) does pose the question as the claim states it. / The question passage (L14-15) poses the question as the claim states it, but the Section 11.1 evidence supports only parts of the contribution (question histories as an upstream source of heterogeneity, action-separating value of a finer policy, no extra warrant from a truth-blind output, exposure and concealment) and mostly by citation; it lacks the comparison with existing work, the full pre-Bayesian passage from failure through question, representation and formulation to renewed judgment, a demonstration of the existence of absorbing configurations, and the statement that the semantic act is left primitive. / The cited Section 11.1 restates the question-history source of heterogeneity, action separation, independent discrimination and exposure/concealment, and the question passage (L14-L15) poses the question as the claim states it, but the evidence does not lay out the pre-Bayesian passage itself, does not establish the existence of absorbing configurations (it only cites Proposition 10.5 for different languages and payoffs), and does not state that the transition is endogenized while the semantic act stays primitive.
- Produced by: claude-opus-5-5 via prompt `resolution@0.7.0`, agreement 3/3

### F-2-resolution-02 · `evidence_partial`

**The evidence for claim C23 does not say what the claim says (only in part).**

- Record: `claims:C23`
- Standard: `protocol/formal.md#P10`
- Why: The appendix evidence derives the trap's SCUE conditions, the beta/2 knife edge with degenerate reflective posterior, the persistence leverage values and the 3/4 and 1/4 payoffs, the stasis conditions, and the beta = 1 non-oscillation, but says nothing about the permanent positive signed warrant gap or each firm remaining exactly half-warranted. / The appendix evidence supports the trap (pooled 1/2 payoffs, SCUE conditions), the beta<1 revelation with dissonance and a degenerate reflective posterior, the persistence computations and 3/4-1/4 payoffs, and the beta=1 no-oscillation continuation, but it lacks the statements that the trap carries payoff-relevant error, that each firm remains permanently half-warranted, and that self-confirmation is a knife-edge property of forgiving demand. / The appendix evidence supports the trap's SCUE conditions, the beta/2 knife edge with degenerate reflective posterior, the stasis condition and its sufficient bound, the leverage values, the 3/4 and 1/4 payoffs and the beta = 1 no-oscillation continuation, but it does not state that the trap's error is payoff-relevant or that the positive signed warrant gap is permanent with each firm half-warranted.
- Produced by: claude-opus-5-5 via prompt `resolution@0.7.0`, agreement 3/3

### F-2-resolution-03 · `evidence_partial`

**The evidence for claim C24 does not say what the claim says (only in part).**

- Record: `claims:C24`
- Standard: `protocol/formal.md#P10`
- Why: The self-sealing remark supports growing confidence in the least-misspecified theory and posterior mass summing to one, but only in the stochastic full-support setting with every expressible theory misspecified on path, a narrower condition than the claim's 'every expressible theory is false' (in the deterministic case the posterior becomes undefined instead). / The self-sealing remark supports growing confidence in the least-misspecified theory only in the stochastic full-support setting where every expressible theory is misspecified on path; it lacks support for the claim under the broader condition that every expressible theory is false (the deterministic case instead yields a zero normalizer).
- Produced by: claude-opus-5-5 via prompt `resolution@0.7.0`, agreement 2/3

### F-2-resolution-04 · `evidence_partial`

**The evidence for claim C34 does not say what the claim says (only in part).**

- Record: `claims:C34`
- Standard: `protocol/formal.md#P10`
- Why: Definition 10.1 identifies conditions (i)-(ii) with the self-confirming conditions of Fudenberg-Levine and Kalai-Lehrer and notes a SCUE with sufficient partitions is a self-confirming equilibrium, but it does not state that fixed awareness reduces the model to a repeated game among subjectively rational Bayesian learners, nor cite Ryall (2003). / Definition 10.1 identifies SCUE conditions (i)-(ii) with the self-confirming conditions of the fixed-language tradition and notes that a SCUE with sufficient partitions and near-true beliefs is a self-confirming equilibrium, but it lacks a statement that with fixed awareness the model reduces to Kalai-Lehrer/Ryall Bayesian learners and that its stable configurations are then self-confirming equilibria. / The SCUE definition says conditions (i)-(ii) are the self-confirming conditions of the fixed-language tradition (Fudenberg and Levine; Kalai and Lehrer) and that a SCUE with sufficient partitions and near-true beliefs is a self-confirming equilibrium, but it does not state that with unchanging awareness the model reduces to a repeated interaction of subjectively rational Bayesian learners in the sense of Kalai-Lehrer and Ryall (2003), nor that all stable configurations are then self-confirming equilibria.
- Produced by: claude-opus-5-5 via prompt `resolution@0.7.0`, agreement 3/3

### F-2-resolution-05 · `evidence_partial`

**The evidence for claim C37 does not say what the claim says (only in part).**

- Record: `claims:C37`
- Standard: `protocol/formal.md#P10`
- Why: Proposition D.2 implies incoherent token sets must be separated, and Remark D.4's certified pairwise conflicts support the deterministic graph-coloring case, but the evidence says nothing about three-mechanism mixtures defeating every single mechanism or restoration as hypergraph coloring. / Proposition D.2 implies that a restorative refinement cannot contain an incoherent cell and Remark D.4 that certified pairwise conflicts must be separated, but the evidence lacks the graph-coloring characterization of the running example and the three-mechanism case in which pairwise accommodation fails jointly, making restoration a hypergraph coloring. / Proposition D.2 implies that a cell containing mutually incoherent tokens cannot be repair-coherent, and Remark D.4 gives the pairwise certified-conflict separation behind graph coloring in the deterministic case, but the evidence does not show the general case where three-mechanism mixtures defeat every single mechanism while each pair is accommodatable, so the hypergraph-coloring claim is unsupported.
- Produced by: claude-opus-5-5 via prompt `resolution@0.7.0`, agreement 3/3

### F-2-resolution-06 · `evidence_partial`

**The evidence for claim C38 does not say what the claim says (only in part).**

- Record: `claims:C38`
- Standard: `protocol/formal.md#P10`
- Why: The example shows four minimal restorations in one case, illustrating multiplicity, but does not support the general claim that minimal restorations are typically multiple. / The example exhibits four minimal restorations, but the evidence supports only this instance and not the general claim that minimal restorations are typically multiple. / The example exhibits four distinct minimal restorations, but the evidence offers nothing beyond this one instance for the general claim that minimal restorations are typically multiple.
- Produced by: claude-opus-5-5 via prompt `resolution@0.7.0`, agreement 3/3

### F-2-resolution-07 · `evidence_partial`

**The evidence for claim C57 does not say what the claim says (only in part).**

- Record: `claims:C57`
- Standard: `protocol/formal.md#P10`
- Why: Proposition 8.4 shows that zero leverage (no coherent grouping with positive increment) prices repair at zero, so the agent does not elect, but it does not support 'precisely when': by the election rule an agent also tolerates the anomaly when B_hat > 0 but lambda_i^(k_i) B_hat < gamma_i. / Proposition 8.4 shows that zero representational increment gives B_hat_i=0 and hence no election, supporting zero-leverage stasis, but its election rule (elect iff lambda_i^(k) B_hat_i >= gamma_i) also makes non-election rational with positive leverage, so the evidence does not support anomaly tolerance being rational precisely when leverage is zero. / Proposition 8.4 supports the zero-leverage case (no positively incremented coherent grouping gives B_hat_i = 0 and hence no election), but its election rule makes non-election rational whenever lambda_i^(k_i) B_hat_i < gamma_i, so the evidence does not support the claim that anomaly tolerance is rational precisely (only) when leverage is zero.
- Produced by: claude-opus-5-5 via prompt `resolution@0.7.0`, agreement 3/3

### F-2-resolution-08 · `evidence_partial`

**The evidence for claim C67 does not say what the claim says (only in part).**

- Record: `claims:C67`
- Standard: `protocol/formal.md#P10`
- Why: The evidence shows that the play profile (differentiated versus pooled) determines whether a language's defect becomes visible and that records carry earlier regimes, but it does not show that the order of experience changes which refinements become available. / The evidence shows that the profile being played (differentiated versus pooled) decides whether the coarse language's failure becomes visible, and that records carry earlier regimes, but it lacks any treatment of the order of experience or of which refinements become available. / The evidence shows that the play profile under which experience arrives decides whether a coarse language's failure becomes visible, and that earlier history shapes which theories are active, but it does not show that the order of experience changes which refinements become available before Bayesian judgment resumes.
- Produced by: claude-opus-5-5 via prompt `resolution@0.7.0`, agreement 3/3

### F-2-resolution-09 · `evidence_partial`

**The evidence for claim C73 does not say what the claim says (only in part).**

- Record: `claims:C73`
- Standard: `protocol/formal.md#P10`
- Why: The example shows forgiving demand (beta = 1) protecting a shared false theory, harsher demand (beta < 1) exposing it, and a differentiating rival exposing a coarse firm, but it neither establishes the 'only when' condition for deviant actors nor mentions customer outside options. / The example shows forgiving demand (beta=1) protecting a pooled false consensus, harsher demand (beta<1) exposing it, and a differentiating rival exposing a coarse firm, but it does not establish that a deviant actor works as epistemic infrastructure only when its variation exposes the language, nor link beta to customer outside options. / The example shows forgiving demand (beta = 1) protecting the pooled false consensus and harsher demand (beta < 1) exposing it, but the evidence does not tie beta to customer outside options and does not show the only-when condition, that a deviant actor serves as epistemic infrastructure only when its variation exposes the coarse language.
- Produced by: claude-opus-5-5 via prompt `resolution@0.7.0`, agreement 3/3

### F-2-resolution-10 · `evidence_partial`

**The evidence for claim C75 does not say what the claim says (only in part).**

- Record: `claims:C75`
- Standard: `protocol/formal.md#P10`
- Why: The section 9 passage shows ordinary Bayesian updating resuming from the bridge prior on the refined language, but says nothing about conventional interventions operating among the new class's members. / The evidence supports ordinary Bayesian updating resuming on the new language from the bridge prior after refinement and formulation, but it lacks any mention of conventional interventions operating among the new class's members. / Section 9 states that ordinary updating resumes from the bridge prior on the refined language and that conjectures and policies are then defined there, which supports renewed Bayesian discrimination, but it says nothing about conventional interventions operating among the new class's members.
- Produced by: claude-opus-5-5 via prompt `resolution@0.7.0`, agreement 3/3

### F-2-resolution-11 · `evidence_partial`

**The evidence for claim C84 does not say what the claim says (only in part).**

- Record: `claims:C84`
- Standard: `protocol/formal.md#P10`
- Why: The dominance-thresholds evidence shows that certainty makes the labeled action strictly dominant in the trap and that belief asymmetry differentiates the opening policies, but it neither states that Part (d) and the rest-point characterization are conditional on play stabilizing nor covers every featured configuration. / The dominance-threshold evidence shows that certainty makes the labeled action strictly dominant in the trap and that belief asymmetry fixes the opening policies, but it lacks the statement that part (d) and the rest-point results are conditional on play stabilizing and does not cover every featured configuration. / The dominance-threshold passage shows that certainty makes the labeled action strictly dominant (sustaining the trap) and that belief asymmetry differentiates the opening policies, but it does not state that Theorem 10.4(d) and the rest-point results are conditional on play stabilizing, and it does not cover every featured configuration, such as the dissonant coarse firm in the persistence case, whose acting belief is undefined.
- Produced by: claude-opus-5-5 via prompt `resolution@0.7.0`, agreement 3/3

## Level 3 · Warrant (SIEVE)

_No findings._

## Below tolerance

These came from a check whose agreement across runs fell below its published minimum. They are reported, not published as findings.

### F-2-completeness-01 · `claim_unresolved`

**The paper states something the contribution rests on that the claims list lacks: "Deterministic consequence mechanisms make a contradictory test observation irreversible, but they do not eliminate sampling variation in states or in rivals' actions within an agent's awareness cell; empirical conjectures therefore generally still converge only asymptotically."**

- Record: `paper/paper.md:L1010`
- Standard: `protocol/formal.md#P10`
- Why: A claim that appears only in the narrative is one the machine cannot check (appendix C.3).
- Produced by: claude-opus-5-5 via prompt `completeness@0.7.0`, agreement 2/3

### F-2-completeness-02 · `claim_unresolved`

**The paper states something the contribution rests on that the claims list lacks: "The model can explain why a new representation is demanded and constrained, but not creation of the analyst's ontology or a new kind of causal mechanism."**

- Record: `paper/paper.md:L1215`
- Standard: `protocol/formal.md#P10`
- Why: A claim that appears only in the narrative is one the machine cannot check (appendix C.3).
- Produced by: claude-opus-5-5 via prompt `completeness@0.7.0`, agreement 2/3

### F-2-completeness-03 · `claim_unresolved`

**The paper states something the contribution rests on that the claims list lacks: "on-path data constrain $\tau(s)(a)$ only at visited state–profile pairs, so observationally equivalent systems with different counterfactual content are generic"**

- Record: `paper/paper.md:L197`
- Standard: `protocol/formal.md#P10`
- Why: A claim that appears only in the narrative is one the machine cannot check (appendix C.3).
- Produced by: claude-opus-5-5 via prompt `completeness@0.7.0`, agreement 3/3

### F-2-completeness-04 · `claim_unresolved`

**The paper states something the contribution rests on that the claims list lacks: "If any distribution were expressible, any within-cell mixture would be too, and no experience could reject the class: coarseness alone cannot produce a detectable failure in a saturated model space."**

- Record: `paper/paper.md:L223`
- Standard: `protocol/formal.md#P10`
- Why: A claim that appears only in the narrative is one the machine cannot check (appendix C.3).
- Produced by: claude-opus-5-5 via prompt `completeness@0.7.0`, agreement 3/3

### F-2-completeness-05 · `claim_unresolved`

**The paper states something the contribution rests on that the claims list lacks: "Policy inertia is thus an outcome, not an assumption: a standing policy persists until the belief-optimal action moves far enough to clear the switching hurdle $\kappa_i$, or until the language itself breaks down and must be repaired ([section 6](#sec-dissonance))."**

- Record: `paper/paper.md:L275`
- Standard: `protocol/formal.md#P10`
- Why: A claim that appears only in the narrative is one the machine cannot check (appendix C.3).
- Produced by: claude-opus-5-5 via prompt `completeness@0.7.0`, agreement 2/3

### F-2-completeness-06 · `claim_unresolved`

**The paper states something the contribution rests on that the claims list lacks: "Because the total evidence process assigns that component positive weight, $E_i^{m}$ diverges almost surely under recurrent strict inadequacy."**

- Record: `paper/paper.md:L406`
- Standard: `protocol/formal.md#P10`
- Why: A claim that appears only in the narrative is one the machine cannot check (appendix C.3).
- Produced by: claude-opus-5-5 via prompt `completeness@0.7.0`, agreement 2/3

### F-2-completeness-07 · `claim_unresolved`

**The paper states something the contribution rests on that the claims list lacks: "The inherited-value term matters: a theory adequate under the current profile may carry evidence from an earlier regime, so the active set and its future false-rejection bound track the whole retained process, not current play alone."**

- Record: `paper/paper.md:L423`
- Standard: `protocol/formal.md#P10`
- Why: A claim that appears only in the narrative is one the machine cannot check (appendix C.3).
- Produced by: claude-opus-5-5 via prompt `completeness@0.7.0`, agreement 3/3

### F-2-completeness-08 · `claim_unresolved`

**The paper states something the contribution rests on that the claims list lacks: "That this occurrence probability is objectively theory-informative—rivals' finer play correlates $a_{-i}$ with the within-cell mechanism—is exactly the misspecification that feeds dissonance ([“The posterior is self-sealing”](#rem-self-sealing)); the agent does not model it."**

- Record: `paper/paper.md:L432`
- Standard: `protocol/formal.md#P10`
- Why: A claim that appears only in the narrative is one the machine cannot check (appendix C.3).
- Produced by: claude-opus-5-5 via prompt `completeness@0.7.0`, agreement 3/3

### F-2-completeness-09 · `claim_unresolved`

**The paper states something the contribution rests on that the claims list lacks: "the acting belief is well defined at every period until—if ever—the last active theory is rejected"**

- Record: `paper/paper.md:L439`
- Standard: `protocol/formal.md#P10`
- Why: A claim that appears only in the narrative is one the machine cannot check (appendix C.3).
- Produced by: claude-opus-5-5 via prompt `completeness@0.7.0`, agreement 3/3

### F-2-completeness-10 · `claim_unresolved`

**The paper states something the contribution rests on that the claims list lacks: "The diagnostic event is determinate—no theory admitted on the current language remains—but its cause and repair need not be."**

- Record: `paper/paper.md:L452`
- Standard: `protocol/formal.md#P10`
- Why: A claim that appears only in the narrative is one the machine cannot check (appendix C.3).
- Produced by: claude-opus-5-5 via prompt `completeness@0.7.0`, agreement 2/3

### F-2-completeness-11 · `claim_unresolved`

**The paper states something the contribution rests on that the claims list lacks: "The activity proviso is not cosmetic: the dynamics of [section 10](#sec-dynamics) generate records whose early periods were played under coarser partitions and different profiles, so a terminally adequate theory may already be absent because it was excluded when the current language was initialized or was subsequently rejected, while an active theory may inherit an evidence value above one."**

- Record: `paper/paper.md:L478`
- Standard: `protocol/formal.md#P10`
- Why: A claim that appears only in the narrative is one the machine cannot check (appendix C.3).
- Produced by: claude-opus-5-5 via prompt `completeness@0.7.0`, agreement 3/3

### F-2-completeness-12 · `claim_unresolved`

**The paper states something the contribution rests on that the claims list lacks: "An empty family means only that the retained record supplies no coherent action-contingent decomposition the agent can price; it does not tell the agent whether an analyst-level restorative refinement exists."**

- Record: `paper/paper.md:L701`
- Standard: `protocol/formal.md#P10`
- Why: A claim that appears only in the narrative is one the machine cannot check (appendix C.3).
- Produced by: claude-opus-5-5 via prompt `completeness@0.7.0`, agreement 3/3

### F-2-completeness-13 · `claim_unresolved`

**The paper states something the contribution rests on that the claims list lacks: "Formulation alone does not determine this probability: it depends jointly on the bridge prior and the repair-consistent active set, but is agent-computable once the refinement, recoded record, and bridge prior exist."**

- Record: `paper/paper.md:L886`
- Standard: `protocol/formal.md#P10`
- Why: A claim that appears only in the narrative is one the machine cannot check (appendix C.3).
- Produced by: claude-opus-5-5 via prompt `completeness@0.7.0`, agreement 2/3
