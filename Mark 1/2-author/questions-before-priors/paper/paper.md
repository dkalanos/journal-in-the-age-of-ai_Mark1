# Questions Before Priors: Causal Dissonance, Insight, and the Origin of Strategic Theories

Michael D. Ryall · July 2026 — First draft

*%
Preliminary draft; comments welcome.  This paper develops the formal core of
a research program on pre-Bayesian theory formation in strategy.*

**AI appendix.** An AI appendix in the published form (record protocol formal-0.3) accompanies this paper at `ai-appendix/` in its research record: definitions, procedure, the claims list, the authors' stance, reproduction anchors, and scope.

## Abstract {#abstract}

 Where do strategic theories come from?
The theory-based view shows how causal theories direct managers' search, experimentation, and action, but its formal treatments begin after a theory—or at least a hypothesis space—exists.
This paper models the step before: how an actor whose causal language has failed comes to possess a new one.
Bayesian updating can rank the theories a manager can already express; it cannot produce a distinction never yet drawn, and confidence can grow even as every expressible theory fails.
I model a separate, fallible faculty—causal dissonance—that detects when the represented class has broken, and a costly, elective inquiry process that may repair it.
Four results follow.
Experience directs repair without determining it, so insight is necessarily fallible.
A firm can rationally value a question before it can state any answer—and an unresolved action margin, not success, is what sustains that value.
The evidence that generates a theory cannot also validate it, which gives boards and investors a precise epistemic role.
And because inquiry can die economically, firms facing identical environments can end with permanently different theories and payoffs: strategic heterogeneity can originate before priors.

**Keywords:** theory-based view; unawareness; insight; causal learning; subjective rationality; self-confirming equilibrium

## 1. Introduction {#sec-intro}

Where do strategic theories come from?
Consider a firm that has just lost a market it was certain it understood.
Its theory of demand did not merely mispredict; every account the firm knows how to state has now failed, and the distinction that would explain the defeat is one it cannot yet draw.
The firm's problem is not to update a belief.
It is to acquire a language in which the right belief could be expressed.
This paper is about that problem.

The theory-based view of strategy holds that economic actors are theorists: managers and entrepreneurs carry causal accounts of value creation, and those accounts—not merely information or incentives—direct what they notice, test, and do (Felin and Zenger 2017; Felin et al. 2024).
The view now has a substantial formal and empirical apparatus.
Theories guide experimentation and search (Camuffo et al. 2020; Chavda et al. 2024), support the acquisition of resources and rents (Ehrig and Zenger 2024), and discipline entrepreneurial decisions in the field (Camuffo et al. 2024; Ott and Hannah 2024).
But the formal treatments begin downstream: with a menu of theories to test, a causal conjecture to search under, or an awareness advantage to exploit.
Felin et al. (2024) explicitly flag the upstream step—where a genuinely new theory comes from—as the open analytical problem of the program.
This paper models that step.

The step is hard for a precise reason: it sits at a boundary of Bayesian rationality.
Bayesian updating ranks the theories an actor can already express.
It cannot produce a distinction never yet drawn, because conditioning reweights a space of possibilities and no reweighting enlarges the space.
Nor does updating sound an alarm when the space itself is broken: posterior mass always sums to one, so a manager whose every expressible theory is false can grow steadily more confident in the least false among them.[^1]
Discovering that one's causal language has failed, and repairing it, are therefore different cognitive operations from ranking the answers the language allows—and only the ranking is Bayesian.

The model supplies the missing transition as a complete loop, displayed in figure 1.
Agents hold theories on a coarse causal language, judge them by Bayes' rule, act through standing policies, and experience the consequences; this back end is standard subjective rationality (Kalai and Lehrer 1993; Ryall 2003).
The front end makes the language itself answerable to experience.
Causal dissonance is a separate, statistically fallible diagnosis that every theory the agent can state has failed its own evidence.
Dissonance poses a question the current language cannot answer; the agent may then elect inquiry, a costly and fallible process that operates on remembered particulars and may deliver a distinction the agent could not previously draw.
Formulation assigns causal content to the refined language, a bridge prior—a fresh prior on the expanded language—restores a probability space, and Bayesian judgment resumes.
The creative act itself, how a mind produces a new predicate, is treated as a primitive technology; the model explains when insight is demanded, what constrains it, what it is worth, and what its output warrants.
Throughout, a two-firm, four-state market example serves as laboratory: each firm chooses one of two product architectures, customer configurations determine which architecture wins, and neither firm initially perceives the distinction that governs demand.

> **Figure 1.** The organizing chain.
> A theory supports Bayesian judgment and action; experience can defeat every expressible theory, producing causal dissonance; costly inquiry may refine awareness; formulation on the refined language yields new models and a new theory, and Bayesian judgment resumes.
>
> *(The figure is a TikZ drawing in the TeX source and is not carried into the record.)*

The first finding is that experience directs repair without determining it.
When the example's firms differentiate and the market delivers a win at one customer configuration and a loss at another, the record tells each firm exactly what any new theory must explain: those two experiences can no longer be treated as alike.
That requirement has teeth—of the fifteen ways to partition the example's four states, eleven are ruled out.
But four repairs remain, and the two simplest, organizing the market by row or by column, fit the record equally well and cannot both be right.
Worlds that agree on everything the firms have ever seen can require different repairs, so no procedure that reads only the record—the model calls such procedures truth-blind—can be reliably correct; in the example, the best any truth-blind technology can guarantee is a coin flip.
Insight is necessarily fallible, and the fallibility is not a defect of the inquirer but the price of a representation that economizes on distinctions.

The second finding is that a firm can rationally pay for a distinction it cannot yet name.
At dissonance the firm cannot compute an expected value over candidate answers, because the candidates are not representable objects.
It can, however, read its own record: situations like the ones it lost will recur, and a distinction that sorted them would let it act on them.
Deliberative leverage—the value of a question—prices exactly this: the robust gain from letting action vary across remembered experiences, over and above the best the firm could do by adjusting one action within its current categories.
In the example that value is exactly one half, for both firms, at the moment their shared language collapses.
Leverage prices action separation, not uncertainty reduction, and the difference shows in who inquires: after a later stretch of play, the firm holding the true theory faces no unresolved action margin and values its question at zero, while its defeated rival values the same question at one half.
Success, not ignorance, is what extinguishes the demand for new theories.

The third finding is that generating a theory and validating it are different achievements, and the evidence for the first cannot double as evidence for the second.
A successful repair fits the record that provoked it—by construction, since fitting the record is the entry requirement for a repair.
Retrospective fit therefore carries no evidential weight of its own: conditional on the record and the inquiry history, the output of a truth-blind technology is independent of which world is actual.
In the example, a firm that adopts the unique theory consistent with its refined language holds it with subjective confidence one, while a reflective assessor who has seen the same record assigns it probability one half: the gap between confidence and warranted confidence is exactly plus one half, and it is the same whether the adopted theory happens to be true or false.
The firm cannot close this gap by itself, because computing it requires representing rival worlds its language cannot express.
Validation must come from new evidence that discriminates—which gives boards, investors, and other broader-awareness outsiders a precise epistemic role that retrospective coherence cannot play.

The fourth finding is that strategic heterogeneity can originate before priors.
Inquiry is an economic process, and it can die in every way an economic process dies: the question is answered, it is priced below its cost, it is abandoned after repeated failure, or it was never answerable.
The example displays the resulting endings.
Under perfectly forgiving demand the two firms can settle permanently on the same false theory, each earning one half forever, because their pooled play conceals the error; the market never generates the contrast that would expose it.
Under even slightly punishing demand that trap becomes a knife edge, and an asymmetric ending appears instead: one firm holds the truth and earns three quarters while its rival earns one quarter, permanently.
The disadvantaged firm sits in dissonant stasis—aware that its account has failed, yet rationally unwilling to pay for a question priced below its cost.
A third ending requires no ignorance at all: a firm can acquire the true theory and still hold its old policy, because the switch it now knows to be an improvement does not clear its switching cost—enlightened inertia.
Identical firms facing identical environments can thus end with different languages, different theories, and permanently different payoffs, for reasons that precede any prior.

The contribution is therefore upstream of the existing formal apparatus of the theory-based view.
Models of theory testing, theory-guided search, and awareness advantage each begin with a representational achievement in hand; this paper supplies the passage that produces it—from the failure of a causal language, through a priced question and a fallible repair, back to Bayesian judgment—and shows that the passage itself generates competitively consequential heterogeneity.
Two boundaries should be stated plainly.
The model treats the semantic act of insight as a primitive: it explains the conditions, direction, price, and warrant of representational change, not the conscious creative operation itself.
And the vocabulary of elementary causal mechanisms is fixed throughout, so insight here means discovering which differences matter, with expansion of the vocabulary itself reserved for companion work in this research program.

[Section 2](#sec-miniature) tells the whole story in miniature: the running example carried from confident differentiation through dissonance, priced questions, and unwarranted confidence to its divergent endings, with no formal apparatus.
[Section 3](#sec-literature) positions the contribution; [section 4](#sec-model) presents the model; [section 5](#sec-bayesian), [section 6](#sec-dissonance), [section 7](#sec-inquiry), [section 8](#sec-economics) and [section 9](#sec-pivot) develop the boundary, the diagnosis, the repair, the price, and the warrant; [section 10](#sec-dynamics) closes the dynamics; and [section 11](#sec-discussion) draws the implications for strategy.

## 2. The problem in miniature {#sec-miniature}

## 3. Related literature {#sec-literature}

### The theory-based view {#the-theory-based-view}

Theories direct attention, counterfactual reasoning, and experimentation rather than merely summarizing evidence (Felin and Zenger 2017).
Work on theory-based decisions formalizes which represented theory to test (Camuffo et al. 2024), search under a given causal conjecture (Chavda et al. 2024), and competitive use of an awareness advantage (Ehrig and Zenger 2024), while related contributions examine the mechanisms and limits of theory-guided experimentation (Felin et al. 2024; Sorenson 2024; Adner and Levinthal 2024).
Empirical studies document thesis development and performance gains from disciplined theory testing (Ott and Hannah 2024; Camuffo et al. 2020), and conceptual work emphasizes entrepreneurial belief generation and the limits of data-driven prediction (Zellweger and Zenger 2023; Felin and Holweg 2024).
These accounts begin with theories, search directions, attributes, or awareness advantages available.
This paper supplies their upstream transition: how experience poses a question, constrains representation change, and can produce heterogeneous causal languages before priors over new theories exist.
It thereby changes the location of strategic heterogeneity in the causal sequence.
Instead of treating different theories only as inputs into search, experimentation, or resource acquisition, the model makes their representational origins and stopping conditions objects of analysis.
The existence claim is limited: different question histories can support different terminal languages and payoffs, not that all durable advantage arises this way.

### Unawareness and growing awareness {#unawareness-and-growing-awareness}

Standard state spaces cannot represent nontrivial unawareness (Dekel et al. 1998), whereas generalized structures represent multiple awareness levels and interactive beliefs (Heifetz et al. 2006; Heifetz et al. 2013).
Reverse Bayesianism constrains belief revision under expansion (Karni and Vier\o 2013), with extensions to awareness of unawareness, intertemporal choice, unforeseen evidence, and incomplete-awareness learning (Karni and Vier\o 2017; Vier\o 2021; Piermont 2021; Grant et al. 2022).
Discovery adds unconceived possibilities rather than discarding conceived ones (Schipper 2021), and beliefs about novelty need not represent the novel objects (Schipper 2025).
This paper supplies an endogenous trigger, economic demand, and record-dependent constraints for awareness expansion while retaining semantic production as a primitive operation.
It connects the defect that generates a question to a fallible refinement and then to bridge-prior formation and warrant.
Where unawareness has been linked to value capture (Bryan et al. 2022), the present model explains a possible origin of the awareness advantage.
The contribution is thus neither an endogenous derivation of semantic creativity nor another rule for updating on an enlarged space.
It identifies when the old space fails, what the retained record requires of a repair, why the agent may pay for an unnamed distinction, and what the generating evidence warrants after that distinction arrives.

### Causal learning with a fixed vocabulary {#causal-learning-with-a-fixed-vocabulary}

Causal graphical models distinguish intervention from association (Pearl 2009; Spirtes et al. 2000); in strategy, Bayesian inference over represented operating structures narrows candidates to an observational-equivalence class that experimentation may split (Ryall 2009), and active learning selects interventions within such a class (He and Geng 2008).
These methods begin after the causal vocabulary is fixed.
This paper studies failure and repair of that vocabulary: when no expressible structure remains adequate, experience constrains but need not identify the new distinction, and observationally equivalent worlds can require different repairs.
Once refinement and formulation create a new represented class, conventional interventions and Bayesian discrimination can again operate among its members.

### Subjective rationality and self-confirming equilibrium {#subjective-rationality-and-self-confirming-equilibrium}

Subjective rationality permits on-path-correct beliefs and subjectively optimal behavior to persist despite off-path error (Kalai and Lehrer 1993; Fudenberg and Levine 1993), and competitive advantage can rest on rivals' self-confirming false theories (Ryall 2003).
These models fix the hypothesis space, while rational-learning convergence requires a grain of truth in represented beliefs (Kalai and Lehrer 1993).
When truth is inexpressible, this paper supplies a process for diagnosing failure and restoring a viable represented class.
Its terminal analysis adds two epistemic possibilities: self-confirming unawareness equilibrium requires a surviving represented class and no worthwhile question, while dissonant stasis permits rational cessation outside a Bayesian world.
Enlightened inertia adds a policy condition rather than a third theory of learning: even after an improved policy becomes representable, its finite-horizon gain may not clear the switching hurdle.
Together these conditions show how restoration of a viable represented class, termination of inquiry, and continuation of play can diverge.

### Statement of contribution {#statement-of-contribution}

Existing work explains learning and action once theories, vocabularies, or awareness advantages exist; this paper supplies the pre-Bayesian passage from represented-class failure to a question, a fallible new representation, formulation, and renewed Bayesian judgment.
Its distinctive economic and epistemic results are that an agent can value a finer actionable distinction before representing its answers, and that evidence generating a truth-blind representation cannot be counted again as independent validation.

Embedding that passage in strategic interaction provides a mechanism by which play exposes or conceals coarse languages and establishes the existence of absorbing configurations with heterogeneous terminal languages and payoffs.
The contribution is therefore upstream: question histories and rational stopping points can generate strategic heterogeneity before priors over the resulting theories are available.
The four conversations meet there: theory-based strategy assumes a theory, unawareness research an expansion, causal learning a vocabulary, and subjective rationality a hypothesis space.
This paper endogenizes the strategically consequential transition into a new hypothesis space while leaving the semantic act that produces it primitive.

## 4. The model {#sec-model}

### 4.1 Agents, states, actions, and consequences {#sec-primitives}

There are $n\ge 2$ *agents*, $N=\{1,\dots,n\}$.
Time is a sequence of *periods* $t=1,2,\dots$.
In each period one state is drawn, every agent acts through a *standing policy* carried over from the previous period, and consequences are realized.
Agents update beliefs every period.
If evidence mounts that their model of the world is in conflict with reality, they may engage in a process of costly inquiry which may then lead to refined awareness, changes to their held model, and potential revisions of their business strategy.

In each period a *state* $s\in S$, with $S$ finite, is drawn independently from a full-support distribution $\rho\in\Delta(S)$.
States describe the strategically-relevant features of the environment that evolve or change over time: customer configurations, input conditions, competitive circumstances, available production technologies, and so on.
(Their status in the agents' own representations is the subject of [section 4.3](#sec-awareness-sub).)

Contingent upon agent $i$'s awareness of the consequence-relevant features of his present state, he chooses an *action* $a_i$ from a finite set $A_i$ through the standing policy described below.
An *action profile* is a list of each agent's action choice, $a=(a_1,\ldots,a_n)$ where $A=\prod_iA_i$ is the set of all action profiles.
Write $A_{-i}=\prod_{j\neq i}A_j$.

Finally, $X=\prod_iX_i$ is the finite set of performance-related *consequences* with typical element $x=(x_1,\dots,x_n)$.
Agent $i$'s consequence $x_i$ is everything a period delivers to it—profit, sales, rival behavior, and any other observed events.
Then, agent $i$'s *payoff function* $\pi_i:X_i\to\mathbb R$ maps his consequences to payoffs.

### 4.2 The objective causal system {#sec-mechanisms-sub}

Causality is modeled in a general, high-level fashion.
Each period, the state $s$, together with the agents' actions $a$, determines the consequences $x$.

#### Definition 4.1 (Elementary mechanisms and the objective system) {#def-mechanisms}

A finite set $\Theta$ of *elementary causal mechanisms* is given, each element of which is a map $\theta:A\to\Delta(X)$.[^2]
The *objective assignment* is a function $\tau:S\to\Theta$.
Both $\Theta$ and $\tau$ are primitives of the model.
The *objective causal system* is $\tau(s)(a)\in\Delta(X)$, a distribution over consequences determined by the state and action profile associated with a period.
Two states $s$ and $s^\prime$ are *causally equivalent* if $\tau(s)=\tau(s^\prime)$.
Let $\mathcal P^{\tau}$ denote the partition of $S$ into causal-equivalence classes.
Finally, $\marg{i}\theta(a)$ denotes the $X_i$-marginal of $\theta(a)$.

Thus, $\tau$ implies a distribution of consequences for every action profile at every state, including profiles never played and states never occurring.
Agents' actions, together with the state, cause their consequences.
A mechanism is the reduced form of whatever detailed model—a structural causal model of customer behavior, a market microstructure, a production process—underlies that relation; the paper imposes no structural-causal-model formalism, but examples may exhibit micro-foundations explicitly, as the running example's customer market does.

Three consequences of the causal reading recur.
First, theories, defined next, are interventional objects: they make predictions at unplayed profiles.
Second, on-path data constrain $\tau(s)(a)$ only at visited state–profile pairs, so observationally equivalent systems with different counterfactual content are generic; that is the engine of the identification results.
Third, the on-path distribution of consequences given an agent's category of states is a *selection* object—it mixes mechanisms according to which states co-occur with which play—and must never be conflated with any mechanism's own conditional.

#### The Calibration Convention {#conv-calibration}

Throughout, the *exact calibration* means deterministic mechanisms with adequacy tolerance $\eta=0$ and finite-sample slack $w\equiv0$ (the test calibration of [definition 6.1](#def-test)), in which tests reject at the first impossible observation and false alarms are zero; the running example uses it.
All definitions are stated once for the general stochastic case; the exact calibration is the special case, and I flag the two places where it changes a conclusion: every dissonant record is repairable under the exact calibration but not in general ([remark D.3](../appendix/appendix.md#rem-irreparable)), and the dissonance capacity $b_i$ affects neither detection nor false alarms under the exact calibration ([proposition D.7](../appendix/appendix.md#prop-capacity)).

### 4.3 Awareness, theories, and conjectures {#sec-awareness-sub}

#### Definition 4.2 (Awareness and expressible theories) {#def-awareness}

Agent $i$'s awareness partition is $\mathcal P_i\in\Pi(S)$, the set of partitions of $S$.
The agent's represented causal and decision objects are restricted by $\mathcal P_i$: theories and policies are defined on its cells, conjectures condition only on its cells, and beliefs range only over theories expressible on it.
The *expressible theories* are the cell-constant mechanism assignments

$$
M(\mathcal P_i)=\{m:\mathcal P_i\to\Theta\}, \tag{1}
$$

with $m$ predicting $x_i\sim\marg{i}m(C)(a)$ at cell $C$ under profile $a$.
Partition $\mathcal P$ is *sufficient* for an assignment $\tau'$ if $\tau'$ is constant on every cell of $\mathcal P$, equivalently if $\mathcal P$ refines $\mathcal P^{\tau'}$; the objective assignment is expressible for agent $i$ if and only if $\mathcal P_i$ is sufficient for $\tau$.

An awareness cell is thus an implicit causal claim: the states it pools are alike in how actions produce consequences.
An expressible theory makes the claim explicit by naming the mechanism.
Restricting theories to *single* mechanism assignments—rather than arbitrary conditional distributions per cell—is substantive and deliberate.
If any distribution were expressible, any within-cell mixture would be too, and no experience could reject the class: coarseness alone cannot produce a detectable failure in a saturated model space.

Agent $i$ holds a belief $\mu_i\in\Delta(M(\mathcal P_i))$ over $M(\mathcal P_i)$—formally, the acting tier of a two-tier belief specified in [section 6](#sec-dissonance)—and a conjecture $q_i:\mathcal P_i\to\Delta(A_{-i})$ about rival play that conditions on $\mathcal P_i$-cells.
Theories and conjectures are different kinds of objects and are deliberately separated: a theory is a causal claim about the objective system; a conjecture is a strategic claim about what other agents will do.
The diagnostic apparatus developed below tests theories, not conjectures.

#### Assumption 4.3 (Observation, retention, and the two records) {#ass-observation}

At the start of each period agent $i$ perceives its current awareness cell $C_{\mathcal P_i}(s)$, the cell of $\mathcal P_i$ containing $s$; at the end it additionally observes the realized action profile $a$ and its own consequence $x_i$.
Each period is retained as a token.
Two records are distinguished throughout.
The *deliberative record* $r_i$ is the multiset of tokens $(C_{\mathcal P_i}(s),a,x_i)$; it is the only record on which the agent's beliefs, tests, and decisions may depend.
The *analyst record* $\bar r_i$ additionally carries the underlying state $s$ of each token.
No object used in the agent's deliberation may depend on the underlying state labels carried only by $\bar r_i$.
Analyst-level constructions that require those labels—in particular the restorative correspondence and the warrant accounting of [section 9](#sec-pivot)—are so marked.
The non-deliberative representation-producing technology is specified separately in [definition 7.2](#def-technology).

*Recodability.*
When the agent acquires a new distinction—a refinement $\mathcal P'$ of its partition—it also acquires the capacity to classify each retained token under $\mathcal P'$, producing a recoded deliberative record.
Before acquisition neither belief nor action can condition on that distinction.
This capacity is a modeling idealization: it treats the retained particular as re-describable under any predicate the agent comes to possess, while denying the agent any pre-insight access to the predicate itself.

#### Assumption 4.4 (Standing policy, subjective optimality, and costly switching) {#ass-commitment}

Agent $i$ carries a *standing policy* $\sigma_i:\mathcal P_i\to A_i$ from one period to the next.
Given its current acting belief $\mu_i$ and conjecture $q_i$, the *belief-optimal* policy $\sigma_i^{\star}$ plays at each cell $C$

$$
\sigma_i^{\star}(C)\in\arg\max_{a_i\in A_i}
\sum_{m\in M(\mathcal P_i)}\mu_i(m)
\sum_{a_{-i}\in A_{-i}}q_i(a_{-i}\mid C)\,
\mathbb E_{x\sim m(C)(a_i,a_{-i})}\!\left[\pi_i(x_i)\right]. \tag{2}
$$

The associated subjective per-period value is

$$
U_i(\sigma\mid\mu_i,q_i)=\sum_{C\in\mathcal P_i}\rho(C)\sum_{m\in M(\mathcal P_i)}\mu_i(m)\sum_{a_{-i}\in A_{-i}}q_i(a_{-i}\mid C)\,\mathbb E_{x\sim m(C)(\sigma(C),a_{-i})}\!\left[\pi_i(x_i)\right], \tag{3}
$$

where $\rho(C)=\sum_{s\in C}\rho(s)$.
Agent $i$ values a lumpy, one-time cost against the gain it produces over a fixed *valuation horizon* of $T$ periods, common across agents, without discounting—the planning horizon over which a one-time cost is amortized, a bounded-rationality stand-in for discounting.
Revising the standing policy is costly: agent $i$ replaces $\sigma_i$ by $\sigma_i^{\star}$ if and only if the horizon-$T$ gain clears a one-time *switching hurdle* $\kappa_i\ge0$,

$$
T\bigl(U_i(\sigma_i^{\star}\mid\mu_i,q_i)-U_i(\sigma_i\mid\mu_i,q_i)\bigr)>\kappa_i,
$$

and otherwise carries $\sigma_i$ unchanged.
The inaction band $T\,[\,U_i(\sigma_i^{\star})-U_i(\sigma_i)\,]\le\kappa_i$ is the source of policy inertia: beliefs may drift and the belief-optimal action may move, yet the standing policy holds until the gain from switching clears the hurdle.
When dissonance ([section 6](#sec-dissonance)) leaves $\mu_i$ undefined, $\sigma_i^{\star}$ is undefined and the standing policy is carried forward unchanged.

Policy inertia is thus an outcome, not an assumption: a standing policy persists until the belief-optimal action moves far enough to clear the switching hurdle $\kappa_i$, or until the language itself breaks down and must be repaired ([section 6](#sec-dissonance)).
How long play stays fixed is therefore governed by agent-level parameters—the switching hurdle here, and the tolerance for misfit introduced with the test of [section 6](#sec-dissonance)—rather than fixed by assumption.
Figure 2 displays the period timeline.

> **Figure 2.** The period timeline.
> Solid steps occur every period: the agent perceives its current awareness cell, acts through its standing policy, observes the realized action profile and its own consequence, and updates its beliefs and sequential test ([assumption 4.3](#ass-observation), [assumption 4.4](#ass-commitment) and [definition 6.1](#def-test)).
> Dashed steps are contingent: dissonance occurs only if the active set empties ([definition 6.3](#def-dissonance)); a dissonant agent elects inquiry only if $\lambda_i^{(k_i)}\widehat B_i\ge\gamma_i$ ([proposition 8.4](#prop-participation)); a successful election refines awareness, and formulation with a bridge prior restores judgment ([section 9](#sec-pivot)); a policy switch occurs only when the horizon-$T$ gain clears the hurdle $\kappa_i$ ([assumption 4.4](#ass-commitment)).
>
> *(The figure is a TikZ drawing in the TeX source and is not carried into the record.)*

### 4.4 What agents know and don't know {#sec-epistemics}

The start-of-period perception of the current cell is what lets a cell-contingent policy be implemented; the state $s$ itself is never perceived.
Observability of the full action profile keeps the separation of causal from strategic error clean; a variant folding components of $a$ into $x_i$ changes bookkeeping only.
Retention without recodability-in-advance is the minimal separation between experiencing a particular and possessing a projectible concept for it: the agent can remember “customers like that one” without commanding a predicate that distinguishes them, and the technology of [section 7](#sec-inquiry) operates on exactly this material.
The idealization has a cost worth naming: recoding is treated as total and infallible once the predicate is held, whereas real reclassification of remembered particulars is partial and error-prone; [section 9](#sec-pivot) isolates where this matters.
The mechanism vocabulary $\Theta$ is known to all agents from the outset; what an agent may lack is the *distinction* that separates states carrying different mechanisms.
Everything the paper formalizes as the representational product of insight is the production of such a distinction.
For every cell $C$ of its current awareness partition, agent $i$ knows the induced cell probability $\rho(C)$.
When a refinement is acquired, the probabilities of the newly representable cells become available with that refinement.
This does not give the agent access to the decomposition of a current cell into states or distinctions it does not yet represent.
Table 1 collects the epistemic specification in one place; the defining statements are referenced in its final column.

**Table 1.** The epistemic ledger: what agent $i$ knows, observes, and never accesses.

| Object | Agent $i$'s access | Reference |
|---|---|---|
| State $s$ | never perceived, at the time or in retrospect | [assumption 4.3](#ass-observation) |
| Own awareness cell $C_{\mathcal P_i}(s)$ | perceived at the start of each period | [assumption 4.3](#ass-observation) |
| Realized action profile $a$ | observed at the end of each period, including rivals' actions | [assumption 4.3](#ass-observation) |
| Own consequence $x_i$ | observed at the end of each period | [assumption 4.3](#ass-observation) |
| Rivals' consequences $x_{-i}$ | never observed | [assumption 4.3](#ass-observation) |
| Mechanism vocabulary $\Theta$ | known to all agents from the outset | [definition 4.1](#def-mechanisms) |
| Objective assignment $\tau$ | never accessed; theories are cell-constant conjectures about it | [definition 4.1](#def-mechanisms) and [definition 4.2](#def-awareness) |
| Cell probabilities $\rho(C)$ | known on current cells; the within-cell decomposition is not represented | equation (3) |
| Deliberative record $r_i$ | retained; the only record deliberation may use | [assumption 4.3](#ass-observation) |
| Analyst record $\bar r_i$ (state labels) | never accessed by deliberation; consumed only by the technology | [assumption 4.3](#ass-observation) and [definition 7.2](#def-technology) |
| Recoding under a refinement | total and infallible once the refinement is acquired; unavailable before | [assumption 4.3](#ass-observation) |
| Test calibration $(\eta,w,\bar n)$, capacity $b_i$ | the agent's own; operated by the agent | [definition 6.1](#def-test) |
| Rivals' partitions, beliefs, policies | never accessed; rival play enters only through the empirical conjecture $q_i$ | [section 4.3](#sec-awareness-sub) |

### 4.5 On-path conditionals {#on-path-conditionals}

Fix a stable stretch over which the standing profile $\sigma=(\sigma_1,\dots,\sigma_n)$ is constant.
Each state $s$ receives the deterministic profile $a(s)=(\sigma_j(C_{\mathcal P_j}(s)))_{j\in N}$.
Agent $i$'s *on-path conditional* at an observation pair $(C,a)$ with $S(C,a)=\{s\in C:a(s)=a\}\neq\emptysetset$ is

$$
p_i^{*}(\cdot\mid C,a)
=
\sum_{s\in S(C,a)}\rho\bigl(s\mid S(C,a)\bigr)\,\marg{i}\tau(s)(a). \tag{4}
$$

This is the selection object flagged above: rivals with finer partitions condition on distinctions agent $i$ cannot see, so the within-cell state mixture can vary with the profile.
It is precisely this dependence—differentiated play by others inside one's own categories—that generates the contrasts on which the diagnostic apparatus feeds.

### 4.6 Scope and modeling commitments {#sec-commitments}

Five disciplines govern everything that follows; they are what distinguish a model of unawareness from a model of inattention or model selection.
(i) Agents hold no prior over the outputs of the inquiry technology and never optimize over named future theories; pre-insight deliberation quantifies only over represented objects.
(ii) The questions modeled here are generated by defects in the current representation, not drawn from a primitive list.
(iii) Inquiry can fail, and its successes can be false; nothing reveals the objective assignment by construction.
(iv) All valuations attached to inquiry are subjective, coarse, and possibly wrong; no objective payoff information leaks from behind the awareness frontier.
(v) Evidence that generates a candidate representation is separated, in the formal accounting, from evidence that warrants it.

Expansion of the mechanism vocabulary itself is a deeper dimension of awareness growth deliberately left outside this paper.

### 4.7 The running example {#the-running-example}

#### Example 1 (A four-state laboratory) {#ex-setup}

Two firms serve a unit market.
States are customer configurations $S=\{s_{00},s_{01},s_{10},s_{11}\}$, displayed as a $2\times2$ array with row coordinate $r$ and column coordinate $c$ (figure 3); $\rho$ is uniform.
Actions are product architectures $A_i=\{0,1\}$.
The mechanism vocabulary is $\Theta=\{\theta^0,\theta^1,\theta^n\}$, with a demand parameter $\beta\in[0,1]$: under $\theta^a$ (“architecture $a$ is preferred”), if the firms differentiate, the firm offering $a$ receives payoff $1$ and its rival $0$; if they pool on $a$, each receives $\tfrac12$; if they pool on the other architecture, each receives $\beta/2$, the customer withholding $1-\beta$ of the unit value.
Under $\theta^n$ (“architecture is neutral”), each firm receives $\tfrac12$ regardless.
A consequence $x_i$ is the pair (own payoff, observed action profile).
The objective assignment is the *row law* $\tau(s_{rc})=\theta^{r}$: the row coordinate is causally relevant, the column coordinate is not.
Both firms begin with the coarse partition $\mathcal P_i^0=\{S\}$, under which the expressible theories are the three constant assignments; the row law is not among them, because it is not constant on $S$.
The baseline sets $\beta=1$ (deterministic winner-take-all with market splitting); $\beta<1$ returns in [section 10](#sec-dynamics).
All mechanisms here are deterministic, so the example runs in the exact calibration of the Calibration Convention ([“The Calibration Convention”](#conv-calibration)); nothing in the general development relies on that.

> **Figure 3.** The four-state laboratory.
> Left: states $s_{rc}$ with the row law $\tau(s_{rc})=\theta^{r}$—the row coordinate is causally relevant, the column coordinate is not ([example 1](#ex-setup)).
> Right: once the discovery record labels $s_{00}$ and $s_{11}$, exactly four minimal repairs separate them (thick boundaries): the row partition, the column partition, and the two partitions isolating one labeled state ([section 7](#sec-inquiry)).
>
> *(The figure is a TikZ drawing in the TeX source and is not carried into the record.)*

## 5. Bayesian competence and its boundary {#sec-bayesian}

Within fixed awareness, learning is ordinary: the Bayesian belief tier updates by Bayes' rule, while conjectures are updated empirically from observed play.
[Section 6](#sec-dissonance) distinguishes the reference posterior from the acting belief once test-based exclusions are introduced.
If no agent's awareness ever changes, the model is a repeated interaction among subjectively rational Bayesian learners in the sense of Kalai and Lehrer (1993) and Ryall (2003), and its stable configurations are self-confirming equilibria (Fudenberg and Levine 1993).
Everything new in this paper happens at the boundary of that layer, which two results locate.

### Proposition 5.1 (No Bayesian emergence) {#prop-no-emergence}

Any well-defined judged or ordinary conditioning of a prior $\mu\in\Delta(M(\mathcal P_i))$ on an observation in the agent's observation algebra yields a posterior $\mu'\in\Delta(M(\mathcal P_i))$.
No sequence of such updates makes a theory outside $M(\mathcal P_i)$ expressible or a distinction finer than $\mathcal P_i$ usable in a policy.

#### Proof {#proof-prop-no-emergence}

Conditioning reweights a distribution on its domain and cannot enlarge the domain; every element of $M(\mathcal P_i)$ is cell-constant, so every posterior mixture, and every policy optimal against one, is $\mathcal P_i$-measurable. ∎

### The posterior is self-sealing {#rem-self-sealing}

The stochastic setting yields a sharper point.
Suppose the on-path data-generating conditionals lie outside the expressible model class, so every expressible theory is misspecified on path.
A full-support posterior does not signal this.
By the logic of misspecified Bayesian learning (Berk 1966), it concentrates on the expressible theories closest to the on-path conditionals in Kullback–Leibler divergence, and the agent becomes increasingly *confident* in one of the least-misspecified expressible theories.
Posterior mass always sums to one; the inadequacy of the whole represented model class is not an event in the agent's algebra.
Diagnosing that no expressible theory is adequate to the observed on-path conditionals therefore requires a faculty outside the posterior—the consistency test of the next section.
The distinction matters for how the theory-based view should treat “updating”: ranking the answers one can express and judging whether any expressible answer is adequate are different cognitive operations, and only the first is Bayesian.

### Example 1 (continued) {#example-1-continued}

Under the coarse partition, firm $i$'s expressible theories are the constant assignments $m^0$, $m^1$, $m^n$.
The row law $\tau$ is inexpressible: no reweighting of $\{m^0,m^1,m^n\}$, on any evidence, produces it ([proposition 5.1](#prop-no-emergence)).
After successive deterministic observations eliminate the expressible theories one by one, the observation that eliminates the last theory with positive posterior mass produces a zero Bayesian normalizer, so ordinary conditioning itself is undefined—the deterministic instance of [“The posterior is self-sealing”](#rem-self-sealing), in which misspecification announces itself only because likelihoods hit zero exactly.
With stochastic full-support mechanisms, the Bayesian normalizer remains positive and no such announcement occurs.

## 6. Causal dissonance {#sec-dissonance}

### 6.1 Tests and active sets {#tests-and-active-sets}

#### Definition 6.1 (Sequential adequacy test, dissonance capacity, and active set) {#def-test}

Fix an adequacy tolerance $\eta\ge0$.
Theory $m$ is *adequate* at a visited pair $(C,a)$ when $\TV\!\left(p_i^{*}(\cdot\mid C,a),\marg{i}m(C)(a)\right)\le\eta$, where $\TV$ is total-variation distance; under a standing profile call $m$ *$\eta$-adequate* if it is adequate at every visited pair and *$\eta$-inadequate* if it is inadequate at some visited pair.
The agent monitors adequacy *sequentially*, period by period.
For each theory admitted when the current language is initialized, it maintains a nonnegative *evidence process* $E_i^{m}$, initialized at $1$ with that language; under adequacy, $E_i^{m}$ is a nonnegative supermartingale, while at a recurrent pair where $m$ is strictly inadequate the construction in [appendix A](../appendix/appendix.md#app-eprocess) contains a fixed betting component with strictly positive expected log-growth.
Because the total evidence process assigns that component positive weight, $E_i^{m}$ diverges almost surely under recurrent strict inadequacy.
Agent $i$ carries a *dissonance capacity* $b_i>0$ and *rejects* $m$, permanently, at the first period in which $\log E_i^{m}\ge b_i$.
The *active set* $\widehat M_i(\mathcal P_i,r_i)$ contains the theories admitted when the current language was initialized that have not subsequently been rejected by the sequential test.
On the initial language all theories in $M(\mathcal P_i)$ are admitted and each begins with $E_i^m=1$; after a refinement, admission is determined by the initial repair screen described in the judged-updating paragraph below.
Capacity is the agent's evidence threshold for abandoning a theory: for a theory adequate from initialization, Ville's inequality gives $\Pr(\sup_t E_i^m(t)\ge e^{b_i})\le e^{-b_i}$, so a high-capacity agent tolerates apparent misfit and rarely rejects on noise, while a low-capacity agent rejects on slight evidence and suffers more false alarms.
Retrospective fits to a *fixed* record score a candidate against evidence already in hand rather than a stream, using the record's counts $n_i(C,a)$ and empirical conditionals $\hat p_i(\cdot\mid C,a)$ and a nonnegative, nonincreasing slack $w(\cdot)\to0$: theory $m$ *fits* at a pair $(C,a)$ when

$$
\TV\bigl(\hat p_i(\cdot\mid C,a),\,\marg{i}m(C)(a)\bigr)
\le
\eta+w\bigl(n_i(C,a)\bigr). \tag{5}
$$

The repair test of [section 7](#sec-inquiry) imposes this at every pair with $n_i(C,a)>0$; the grouping test of [section 8](#sec-economics) imposes it wherever $n_i(C,a)\ge\bar n$, a minimum count $\bar n\ge1$.

Sequential testing is consistent: a theory strictly inadequate at a recurrent pair is almost surely rejected, an adequate theory is falsely rejected with conditional probability at most $E_i^m(t_0)e^{-b_i}$, and the active set is monotone and eventually constant; the formal statement and proof are [lemma D.1](../appendix/appendix.md#lem-test-consistency) in [appendix D](../appendix/appendix.md#app-deferred).

The inherited-value term matters: a theory adequate under the current profile may carry evidence from an earlier regime, so the active set and its future false-rejection bound track the whole retained process, not current play alone.
Under the exact calibration the separate zero-likelihood detector of [appendix A](../appendix/appendix.md#app-eprocess) applies and capacity $b_i$ plays no role ([“The Calibration Convention”](#conv-calibration)).

#### Assumption 6.2 (Full-support marginals, stochastic case) {#ass-full-support}

In the stochastic case every mechanism marginal $\marg{i}\theta(a)$ has full support on $X_i$.
(The deterministic case, including the running example, is exempt and needs no such assumption.)

The likelihood of a token $(C,a,x_i)$ under theory $m$ is $\marg{i}m(C)(a)(x_i)$: the agent's subjective model treats the $(C,a)$-occurrence probability as theory-independent, so it cancels in Bayes' rule and updating requires neither $\rho$ nor the within-cell state mixture.
That this occurrence probability is objectively theory-informative—rivals' finer play correlates $a_{-i}$ with the within-cell mechanism—is exactly the misspecification that feeds dissonance ([“The posterior is self-sealing”](#rem-self-sealing)); the agent does not model it.

#### Judged updating {#judged-updating}

Beliefs carry two tiers.
The *reference posterior* $\bar\mu_i$ begins at a full-support prior on $M(\mathcal P_i)$ and updates by the token likelihoods above; it is never conditioned on the test.
The *acting belief* $\mu_i$ is the reference posterior restricted and renormalized to the current active set, so that belief never rides on a rejected theory; when the active set is empty, the acting belief is undefined and the carry-forward clause of [assumption 4.4](#ass-commitment) governs.
Because the active set only shrinks after the current language is initialized, the acting belief is well defined at every period until—if ever—the last active theory is rejected; [assumption 6.2](#ass-full-support) keeps every reference likelihood positive, so restriction to any nonempty active set is always to a positive-mass set.
In the deterministic case judged updating coincides with ordinary Bayesian conditioning while the Bayesian normalizer is positive; a zero-likelihood contradiction can instead make ordinary conditioning itself undefined.
After a refinement to $\mathcal P_i'$, the recoded record supplies an initial repair screen: the new-language active set is initialized as $\widehat M_i^{\,R}(\mathcal P_i',\bar r_i)$, which the agent can compute from its recoded deliberative record, and excluded theories begin inactive without replaying the historical record through the sequential evidence process.
Each admitted theory begins with $E_i^m=1$; the reference posterior begins at the full-support bridge prior $\mu_i^+\in\Delta(M(\mathcal P_i'))$, and the acting belief is its restriction, renormalized on $\widehat M_i^{\,R}(\mathcal P_i',\bar r_i)$.
Thereafter the reference posterior and sequential evidence processes update from newly arriving tokens, permanent sequential rejection further shrinks the active set, and the acting belief is the reference posterior restricted and renormalized to the current active set.
Judged updating is the formal junction between the test and the acting belief—between judgment and understanding ([“The posterior is self-sealing”](#rem-self-sealing))—and it guarantees, in [section 10](#sec-dynamics), that surviving acting beliefs are supported on adequate theories.

### 6.2 Dissonance and exposure {#dissonance-and-exposure}

#### Definition 6.3 (Causal dissonance) {#def-dissonance}

Agent $i$ experiences *causal dissonance* at any period at which $\widehat M_i(\mathcal P_i,r_i)=\emptysetset$: no theory admitted on the current language remains unrejected.
The expressible set does not disappear; every element is either excluded by the current language's initialization screen or subsequently rejected by the sequential test.
The diagnostic event is determinate—no theory admitted on the current language remains—but its cause and repair need not be.
The modeled question is: *is there an unrepresented distinction among the pooled states that can reconcile the record, and if so what is it?*

Within the model, dissonance is the endogenous trigger and localization of an anomaly-driven question for intelligence.
It is localized by the cells and observation pairs at which admitted theories fail, directed because any successful repair must reconcile the retained record, and semantically open because no expressible object names the candidate distinction.
Under exact deterministic testing, dissonance implies that the current partition is insufficient for the objective assignment: an expressible true deterministic theory could not be rejected.
In the stochastic model, false rejection and irreparable finite records mean that dissonance is an operational diagnosis, not by itself proof of objective representational insufficiency ([lemma D.1](../appendix/appendix.md#lem-test-consistency) and [remark D.3](../appendix/appendix.md#rem-irreparable)).
Whether dissonance occurs depends on whether play exposes inadequacy of the represented class; objective falsity can remain concealed.

#### Definition 6.4 (Exposure and concealment) {#def-exposure}

Under a standing profile, awareness $\mathcal P_i$ is *exposed* if every $m\in M(\mathcal P_i)$ is $\eta$-inadequate.
A standing profile is *concealing* for agent $i$ if some expressible theory is $\eta$-adequate under it while false as a claim about $\tau$ at some state its cells cover.

#### Proposition 6.5 (Exposure and dissonance) {#prop-exposure}

Fix a standing profile and suppose no theory sits exactly at the adequacy boundary ([lemma D.1](../appendix/appendix.md#lem-test-consistency)).
If every theory that is $\eta$-adequate under the fixed profile remains active when that profile begins at $t_0$, then $\mathcal P_i$ is exposed if and only if eventual dissonance occurs almost surely.
If the profile is not exposed and $m$ is an active $\eta$-adequate theory at entry, then, conditional on the entry history, dissonance is avoided forever with probability at least $1-E_i^m(t_0)e^{-b_i}$; if some such $m$ satisfies $E_i^m(t_0)\le1$, this bound is at least $1-e^{-b_i}$.

##### Proof {#proof-prop-exposure}

By [lemma D.1](../appendix/appendix.md#lem-test-consistency), every entry-active theory strictly inadequate at a recurrent pair is eventually rejected almost surely, while every theory inactive at $t_0$ remains absent.
If all profile-adequate theories are active at $t_0$, the eventual active set is therefore empty almost surely exactly when there is no $\eta$-adequate theory—that is, exactly when the profile is exposed.
For a non-exposed profile, conditional Ville's inequality bounds the future rejection probability of any entry-active adequate theory $m$ by $E_i^m(t_0)e^{-b_i}$, so the stated survival and no-dissonance bounds follow. ∎

The activity proviso is not cosmetic: the dynamics of [section 10](#sec-dynamics) generate records whose early periods were played under coarser partitions and different profiles, so a terminally adequate theory may already be absent because it was excluded when the current language was initialized or was subsequently rejected, while an active theory may inherit an evidence value above one.

Two recurring mechanisms generate exposure, and the distinction organizes much of what follows.
Heterogeneity inside a cell surfaces either because *other agents play differently across the pooled states*—strategic differentiation inside one's categories, which changes the visited profiles and the induced mixtures—or because *the environment punishes uniform play across causally different states in an observable way*.
Both reappear as the corrective forces in [section 10](#sec-dynamics).

#### Example 1 (continued) {#example-1-continued-2}

Let $\beta=1$ and suppose the firms' priors over the constant theories are heterogeneous: firm 1 considers $\theta^0$ more likely than $\theta^1$, and firm 2 the reverse.
A direct computation shows that, against any conjecture about the rival, offering architecture $0$ is subjectively strictly dominant for firm 1 and architecture $1$ for firm 2 whenever $\mu_i(m^a)>(2-\beta)\,\mu_i(m^{a'})$; at $\beta=1$ this is simple belief asymmetry.
The firms therefore adopt differentiated constant policies.
Take the valuation horizon $T=2$ and condition on two periods that serve the diagonal states $s_{00}$ and $s_{11}$ under differentiated play—a positive-probability event under uniform $\rho$; the appendix records how the leverage below scales with the realized composition.
With differentiated actions, the winner-take-all payoffs reveal the objectively preferred architecture at each state: firm 1 wins at $s_{00}$ (payoffs $1,0$) and loses at $s_{11}$ (payoffs $0,1$).
No constant assignment is consistent with both observations—$m^0$ fails at $s_{11}$, $m^1$ at $s_{00}$, and $m^n$ predicts one-half at both—so each firm's active set empties: causal dissonance, in its exact deterministic form.
Had the firms instead pooled on the same architecture at both states, each would have received one-half at every period, an outcome consistent with all three constant theories: the pooled profile is concealing, and coarse awareness would have survived its own evidence indefinitely.
Belief heterogeneity, by inducing differentiated play, is what made the shared language's failure visible.

## 7. Inquiry: restoration, direction, and fallibility {#sec-inquiry}

Within the model, dissonance poses an anomaly-driven question the current language cannot answer.
This section characterizes what a successful answer must accomplish, shows that the requirement directs inquiry without determining its output, and establishes that any inquiry process meeting the paper's disciplines must be fallible.

### 7.1 Restorative refinements {#restorative-refinements}

For $\mathcal P,\mathcal P'\in\Pi(S)$, write $\mathcal P\prec\mathcal P'$ when $\mathcal P'$ strictly refines $\mathcal P$.
The restorative correspondence is an *analyst-level* object: deciding whether a candidate refinement $\mathcal P'$ restores expressibility requires recoding tokens to $\mathcal P'$-cells, which uses the analyst record $\bar r_i$ of [assumption 4.3](#ass-observation).
It is defined here for the analysis of what a successful answer must accomplish; [section 8](#sec-economics) builds the agent's own deliberative valuation separately.

#### Definition 7.1 (Restorative refinement) {#def-restorative}

Fix a candidate refinement $\mathcal P_i\prec\mathcal P'$ and recode the analyst record $\bar r_i$ to the deliberative record $r_i^{\mathcal P'}$ on $\mathcal P'$.
Define the *repair-consistent active set*

$$
\widehat M_i^{\,R}(\mathcal P',\bar r_i)
=
\left\{
m'\in M(\mathcal P'):
m'\text{ satisfies \cref{eq:repair-test}}
\right\},
$$

where the *repair test* is

$$
\TV\!\left(
\hat p_i(\cdot\mid C',a),
\marg{i}m'(C')(a)
\right)
\leq
\eta+w\!\left(n_i(C',a)\right)
\quad
\text{for every $(C',a)$ with }n_i(C',a)>0. \tag{6}
$$

Here the counts and empirical conditionals are computed from $r_i^{\mathcal P'}$.
The refinement $\mathcal P'$ is *restorative* at $(\mathcal P_i,\bar r_i)$ if $\widehat M_i^{\,R}(\mathcal P',\bar r_i)\neq\emptysetset$.
It is *minimally restorative* if no restorative $\mathcal P''$ satisfies $\mathcal P_i\prec\mathcal P''\prec\mathcal P'$.
Write $\mathcal R(\mathcal P_i,\bar r_i)$ for the set of minimally restorative refinements.

The repair test deliberately applies to every nonempty recoded cell–profile pair.
The count floor $\bar n$ is not part of the repair test; it applies only to the deliberative grouping test of [section 8](#sec-economics).
Every nonempty recoded fragment remains subject to equation (6), while the larger finite-sample slack $w(n)$ at small $n$ preserves the intended caution about sparse evidence.
Refinement can therefore reconcile observations but cannot delete their constraints.
Under the exact calibration the repair test is exact consistency at every observed pair ([“The Calibration Convention”](#conv-calibration)).

Restoration factorizes cell by cell, so finding a repair is a coloring problem; the formal statement and proof are [proposition D.2](../appendix/appendix.md#prop-coherence) in [appendix D](../appendix/appendix.md#app-deferred).

Coherence is the general form of a conflict structure.
Token sets are *mutually incoherent* when no single mechanism accommodates their union; every restorative refinement must separate mutually incoherent sets, since a cell containing both would be incoherent.
In the deterministic running example incoherence is a binary relation between labeled periods and restoration is a graph-coloring problem; in general, a mixture of three mechanisms may defeat every single mechanism even though each pair of tokens is individually accommodatable, so restoration is a hypergraph coloring.
Two further structural facts matter.
First, minimal restorations, when they exist, are typically multiple—as the example shows vividly.
Second, existence itself is guaranteed only in the deterministic case.

With deterministic mechanisms every dissonant record is repairable, and finiteness of $\Pi(S)$ ensures a minimally restorative refinement exists ([remark D.3](../appendix/appendix.md#rem-irreparable), [appendix D](../appendix/appendix.md#app-deferred)).
With stochastic mechanisms this guarantee fails.
Multiple observations at a single state may yield empirical conditionals for which no one mechanism satisfies equation (6) across the observed profiles.
Because no refinement can split a state, such a record has $\mathcal R(\mathcal P_i,\bar r_i)=\emptysetset$ and is *irreparable*: dissonance names a defect that no expressible refinement can repair.
Irreparability is an analyst-level property: it is a fact about $\bar r_i$, and the agent, lacking the state labels, cannot in general tell an irreparable record from a repairable one—this is precisely the agent's inability to distinguish causal heterogeneity from mechanism noise, developed in [section 8](#sec-economics).
When the record is irreparable the technology fails surely ([definition 7.2](#def-technology)); the resulting behavior is governed by the deliberative valuation and failure-discouragement of [section 8](#sec-economics).
If the deliberative record still admits a positive-leverage coherent grouping, the agent may elect a doomed inquiry until its achievability weight decays; if no coherent grouping prices the question, it declines immediately.
Neither response requires the agent to recognize analyst-level irreparability.
Under recurring visitation irreparability is typically transient, but a record whose critical pairs stop being visited can remain irreparable forever, a possibility [section 10](#sec-dynamics) classifies within dissonant stasis.

### 7.2 The technology {#the-technology}

#### Definition 7.2 (Representation-producing technology) {#def-technology}

A representation-producing technology for agent $i$ is a possibly randomized map $\phi_i$ from the analyst record $(\mathcal P_i,\bar r_i)$ to $\{\mathcal P_i\}\cup\mathcal R(\mathcal P_i,\bar r_i)$: it fails, returning the current partition, or succeeds, producing a minimally restorative refinement.
When $\mathcal R(\mathcal P_i,\bar r_i)=\emptysetset$, the range is the singleton $\{\mathcal P_i\}$ and the technology fails surely.
It is *truth-blind*: its output distribution depends only on $(\mathcal P_i,\bar r_i)$, never directly on $\tau$.
The technology consumes the analyst record because producing a distinction operates on retained particulars in their full concreteness; what the agent lacks pre-insight is not the particulars but the predicate that organizes them, and truth-blindness records that even this concrete operation cannot read off the objective law.
A complexity ordering on refinements—the analyst's model of which conceptual products the agent's comparison capacities can generate—may restrict the range further, provided it leaves the admissible subset of $\mathcal R$ nonempty whenever $\mathcal R$ is; it is a primitive of the technology, not an object of the agent's optimization.

#### Definition 7.3 (Truth-blind formulation rule) {#def-formulation-rule}

After successful production of $\mathcal P_i'$, let $r_i^{\mathcal P_i'}$ denote the deliberative record recoded to that partition.
At this point the agent can compute from $r_i^{\mathcal P_i'}$ the same repair-consistent active set that the analyst writes as $\widehat M_i^{\,R}(\mathcal P_i',\bar r_i)$.
A *formulation rule* is a possibly randomized kernel

$$
\psi_i\!\left(
\cdot\mid\mathcal P_i',r_i^{\mathcal P_i'}
\right)
\in
\Delta\!\left(
\widehat M_i^{\,R}(\mathcal P_i',\bar r_i)
\right).
$$

It is *record-measurable and truth-blind* if its conditional distribution depends only on the displayed arguments and on internal randomness independent of the objective assignment, state draws, consequence draws, and production randomness.
A *truth-blind inquiry-and-formulation rule* is a pair $(\phi_i,\psi_i)$ satisfying these restrictions.
Any randomized post-refinement prior-selection rule is subject to the same record-measurability and truth-blindness requirement.

The technology is the paper's stated representational primitive.
This model does not derive the semantic act that produces a new predicate; it treats that act as a representational technology and shows how experience directs, constrains, prices, and disciplines its output.
The model endogenizes the demand for representational production, the record-dependent constraints on successful products, their unavoidable fallibility, and their strategic consequences, while leaving the internal creative operation primitive.
The output, and even the set of possible outputs, is not a pre-insight subjective menu: the agent cannot name a candidate refinement, assign it a probability, or condition a policy on it before production succeeds ([section 4.6](#sec-commitments)).

### 7.3 Nonidentification and the price of robustness {#nonidentification-and-the-price-of-robustness}

#### Theorem 7.4 (Observational nonidentification) {#thm-nonidentification}

Fix common initial epistemic states, common record-measurable behavioral and tie-breaking rules, common truth-blind inquiry-and-formulation rules, and a finite horizon of $H$ periods.
Let $\tau\neq\tau'$ be objective assignments whose *joint* consequence laws agree at every state–profile pair reachable through $H$ under either world from those initial conditions:

$$
\tau(s)(a)=\tau'(s)(a)\in\Delta(X)
\qquad
\text{at every such $(s,a)$.}
$$

The two worlds admit a coupling under which, through $H$, their state draws, full consequence profiles, analyst and deliberative records, partition paths, beliefs, conjectures, standing policies, and production-and-formulation outputs coincide pathwise.
If the equality holds at every pair reachable at any finite horizon, the coupling extends to the entire process.

Consequently, no truth-blind inquiry-and-formulation rule can produce an objectively correct formulation with probability one in both worlds.
More generally, the same conclusion holds for any success criterion whose sets of realizable outputs are disjoint across the two worlds.

##### Proof {#proof-thm-nonidentification}

Use common state draws, common independent random seeds for production, formulation, bridge-prior selection, and tie-breaking, and an identity coupling of the joint consequence draws at every reachable pair.
Proceed by induction over periods.
Identical histories imply identical current partitions and standing policies, hence the same action profile at the common state.
The pair is reachable, so the two objective assignments give it the same joint consequence distribution and the coupled consequence profiles coincide.
Both analyst and deliberative records therefore remain identical.
Record-measurability and truth-blindness then give identical belief updates, conjectures, policies, refinements, and formulations, closing the induction through $H$; the all-horizons claim follows by countability.

Thus every truth-blind rule has the same output distribution in the two worlds.
Because $\tau\neq\tau'$, their sets of objectively correct formulations are disjoint, so that common distribution cannot assign probability one to both sets.
The same argument applies to any other disjoint pair of success sets. ∎

#### Proposition 7.5 (Robust sufficiency) {#prop-robust-sufficiency}

A partition sufficient for every assignment in a candidate set $\mathcal T$ must refine $\bigvee_{\tau'\in\mathcal T}\mathcal P^{\tau'}$, where $\bigvee$ denotes the coarsest partition that refines every candidate causal-equivalence partition.
A representation guaranteed to accommodate all observationally equivalent worlds is accordingly finer than any single world requires; a technology that economizes on distinctions must accept fallibility.

##### Proof {#proof-prop-robust-sufficiency}

Sufficiency for $\tau'$ is refinement of $\mathcal P^{\tau'}$ ([definition 4.2](#def-awareness)); refinement of each candidate's partition is refinement of their join. ∎

#### Example 1 (continued) {#example-1-continued-3}

After discovery, the record contains two labeled observations: architecture $0$ objectively preferred at $s_{00}$, architecture $1$ at $s_{11}$.
Of the fifteen partitions of four states, exactly four are minimally restorative—each must separate $s_{00}$ from $s_{11}$: the row partition $\{\{s_{00},s_{01}\},\{s_{10},s_{11}\}\}$, the column partition $\{\{s_{00},s_{10}\},\{s_{01},s_{11}\}\}$, and the two partitions isolating one labeled state (figure 3).
The record directs inquiry (eleven partitions are excluded) without determining it (four remain).
A natural complexity ordering counts the coordinates needed to describe a refinement: rows and columns are one-coordinate distinctions, the isolating partitions require two.
A factor-seeking technology thus produces the row or the column refinement—and here direction runs out.
Define the *column world* $\tau'(s_{rc})=\theta^{c}$.
Through the discovery horizon and conditional on the diagonal-state event, it agrees with the row world on the full joint mechanism at both visited states, so the two worlds generate the discovery record and every truth-blind production-and-formulation output with the same probability by the same coupling argument, conditional on the diagonal-state event.
No truth-blind rule can formulate correctly in both, a randomized rule succeeds in the worst case with probability at most one-half, and by [proposition 7.5](#prop-robust-sufficiency) a partition sufficient for both worlds must be the full partition into singletons: robustness costs every distinction the language can draw, which is exactly what a minimal technology economizes on.
The example also locates the failure mode of each residual candidate: whichever factor refinement arrives, its unique consistent theory extrapolates the wrong prediction to the two unlabeled states in one of the two worlds.

## 8. The economics of inquiry {#sec-economics}

Whether to prosecute a question must itself be a decision, and it must be priced at exactly the moment the action-guiding Bayesian calculation is disabled: at dissonance the acting belief is undefined ([definition 6.3](#def-dissonance)), and the candidate answers are not represented objects ([definition 7.2](#def-technology)).
This section builds the valuation from what the agent actually has—its deliberative record—and prices the rest through the success weight.
The resulting statistic is a genuine estimate, not a guarantee: the agent guesses at the worth of a distinction it cannot yet name, and the model keeps that epistemic honesty rather than smuggling in the analyst's restorative correspondence.

### Assumption 8.1 (Costly, elective, dissonance-triggered production) {#ass-elective}

The technology $\phi_i$ operates only when agent $i$ experiences dissonance and elects inquiry, at cost $\gamma_i>0$ in payoff units.
Let $k_i$ count agent $i$'s consecutive failed elections, reset to zero on any success.
Agent $i$ holds a *delabeled achievability weight* $\lambda_i^{(k)}\in(0,1]$, nonincreasing in $k$ with $\lambda_i^{(k)}\to0$: a subjective probability that an election produces a refinement *delivering the estimated value below*, defined on that event alone and not on the identities of possible outputs.
On failure or abstention the standing policy is carried forward.
Awareness is cumulative: acquired distinctions are never lost, though theories formulated on them may later be rejected.

The weight is awareness of unawareness in delabeled form—the agent can believe that inquiry may yield a usable distinction, and grow less hopeful as attempts fail, without ever describing a candidate distinction—a construct with precedent in beliefs about unpredictable novelty (Schipper 2025; Karni and Vier\o 2017).
Its decay is the answerability meta-prior doing formal work: repeated failure is evidence that the question may be unanswerable (the record irreparable, the repertoire inadequate), and a rational inquirer eventually abandons it.
That the weight prices *achievability*—not mere success—absorbs the gap between the agent's estimate and what an arriving refinement can actually deliver, a gap that is zero under the pointwise-transparency condition below and may be positive otherwise.

### Definition 8.2 (Deliberative groupings and coherent classes) {#def-pinned}

A *deliberative grouping* $G$ of the record $r_i$ is a partition of its tokens.
For a group $g\in G$ and observed profile $a$, let

$$
n_g(a)=\bigl|\{t\in g:a(t)=a\}\bigr|
$$

and, when $n_g(a)>0$, let $\hat p_g(\cdot\mid a)$ be the empirical distribution of the consequences $x_i(t)$ among those tokens.
Define

$$
\Theta_i(g)
=
\left\{
\theta\in\Theta:
\TV\!\left(
\hat p_g(\cdot\mid a),\marg{i}\theta(a)
\right)
\leq
\eta+w\!\left(n_g(a)\right)
\ \text{for every }a\text{ with }n_g(a)\geq\bar n
\right\}.
$$

The group $g$ is *coherent* if $\Theta_i(g)\neq\emptysetset$, and the grouping $G$ is coherent if every one of its groups is coherent.
Write $\mathcal G_i(r_i)$ for the finite family of coherent groupings of $r_i$.

Coherence, $\Theta_i(g)$, and $\mathcal G_i(r_i)$ depend only on the deliberative record—on observed actions and own consequences—together with the known mechanism vocabulary.
They never use state labels or candidate refinements.
The family $\mathcal G_i(r_i)$ may be empty under stochastic sampling: full support guarantees positive likelihood, not finite-sample passage of the consistency test.
An empty family means only that the retained record supplies no coherent action-contingent decomposition the agent can price; it does not tell the agent whether an analyst-level restorative refinement exists.
A coherent grouping is the agent's hypothesis about which remembered particulars share a mechanism.
It is not a partition of $S$, and the agent cannot verify before insight that any refinement of its awareness would realize it.

### Definition 8.3 (Deliberative leverage) {#def-leverage}

Given a coherent grouping $G$, let $g(t)$ be the group of token $t$, let $C_i(t)$ denote token $t$'s cell under the current partition, and set $\sigma_i(t):=\sigma_i(C_i(t))$.
The *per-token robust gain* of proposing action $a_i$ for a group is

$$
\Delta_i^G(t,a_i)
=
\min_{a_{-i}\in A_{-i}}\;
\min_{\theta\in\Theta_i(g(t))}
\Bigl(
\mathbb E_{x\sim\theta(a_i,a_{-i})}\!\bigl[\pi_i(x_i)\bigr]
-
\mathbb E_{x\sim\theta(\sigma_i(t),a_{-i})}\!\bigl[\pi_i(x_i)\bigr]
\Bigr),
$$

the worst case over rival responses and over the mechanisms the group's record leaves open.
For $G\in\mathcal G_i(r_i)$, define the current-cell/group intersection

$$
r_i(C,g)
=
\{t\in r_i:C_i(t)=C,\ g(t)=g\},
\qquad C\in\mathcal P_i,\quad g\in G,
$$

where empty intersections contribute zero.
Define the robust fine-contingent value

$$
L_i^{\mathrm{fine}}(G;r_i)
=
\sum_{C\in\mathcal P_i}
\sum_{g\in G}
\max_{a_i\in A_i}
\sum_{t\in r_i(C,g)}
\Delta_i^G(t,a_i),
$$

which lets action vary by each nonempty current-cell/group intersection, and define the current-language benchmark

$$
L_i^{\mathrm{cur}}(G;r_i)
=
\sum_{C\in\mathcal P_i}
\max_{a_i\in A_i}
\sum_{g\in G}
\sum_{t\in r_i(C,g)}
\Delta_i^G(t,a_i),
$$

which requires one action for every token in a current awareness cell, although the coherent grouping is used to evaluate that action.
The grouping may span more than one current awareness cell, since any future awareness partition refines rather than erases current awareness.
The *gross representational increment* under grouping $G$ is

$$
J_i(G;r_i)
=
L_i^{\mathrm{fine}}(G;r_i)-L_i^{\mathrm{cur}}(G;r_i).
$$

The *deliberative leverage* is

$$
\widehat B_i(r_i)
=
\begin{cases}
\displaystyle
\frac{T}{\lvert r_i\rvert}
\max\!\left(
\{0\}\cup
\{J_i(G;r_i):G\in\mathcal G_i(r_i)\}
\right),
&
\widehat M_i(\mathcal P_i,r_i)=\emptysetset,
\\[1.1em]
0,
&
\widehat M_i(\mathcal P_i,r_i)\neq\emptysetset.
\end{cases} \tag{7}
$$

The premise is that the empirical token *distribution* recurs, so the horizon-$T$ estimate is $T$ times the average per-token gross representational increment.
The outside option $0$ represents declining to attribute actionable value to any available grouping; it also makes leverage zero when $\mathcal G_i(r_i)=\emptysetset$.
The current-language term is a counterfactual valuation benchmark, not a new dissonant policy-switching rule: at dissonance the standing policy continues to be carried forward under [assumption 4.4](#ass-commitment) unless inquiry succeeds.
Thus $\widehat B_i$ prices the incremental gross action value of making a coherent grouping actionable beyond what one action per current awareness cell can already obtain, not a complete net expected-payoff value after switching costs.

### Proposition 8.4 (Participation) {#prop-participation}

$\widehat B_i(r_i)$ is well defined, nonnegative, bounded by $T(\max \pi_i-\min \pi_i)$, and computable from the deliberative record, the standing policy, and the agent-known model primitives and test calibration.
At a dissonant record, electing inquiry has represented value $\lambda_i^{(k_i)}\widehat B_i(r_i)-\gamma_i$, so agent $i$ elects if and only if

$$
\lambda_i^{(k_i)}\widehat B_i(r_i)\geq\gamma_i.
$$

Moreover, at a dissonant record, $\widehat B_i(r_i)>0$ if and only if some coherent grouping has positive representational increment:

$$
J_i(G;r_i)>0
\qquad\text{for some }G\in\mathcal G_i(r_i).
$$

Thus a question is priced positively only when some coherent reading of the record supports action variation within at least one current awareness cell that robustly outperforms the best action kept uniform on that cell under the same coherent reading.

#### Proof {#proof-prop-participation}

The record is finite, so it has finitely many groupings.
For every coherent group, $\Theta_i(g)$ is a nonempty finite set, and all action and consequence spaces are finite.
Hence every max–min expression and every $L_i^{\mathrm{fine}}(G;r_i)$, $L_i^{\mathrm{cur}}(G;r_i)$, and $J_i(G;r_i)$ is well defined.
The set whose maximum appears in equation (7) always contains $0$, including when $\mathcal G_i(r_i)=\emptysetset$, proving existence and nonnegativity.
For fixed $C$ and $G$, put $f_{C,g}(a_i)=\sum_{t\in r_i(C,g)}\Delta_i^G(t,a_i)$.
Then

$$
\sum_{g\in G}\max_{a_i}f_{C,g}(a_i)
\geq
\max_{a_i}\sum_{g\in G}f_{C,g}(a_i),
$$

because the left side permits a separate maximizing action for every intersection while the right side restricts them to a common action.
Summing across current cells gives $L_i^{\mathrm{fine}}(G;r_i)\geq L_i^{\mathrm{cur}}(G;r_i)$ and hence $J_i(G;r_i)\geq0$.
Writing $\Delta \pi_i=\max \pi_i-\min \pi_i$, each $\Delta_i^G(t,a_i)\leq\Delta \pi_i$, so $L_i^{\mathrm{fine}}(G;r_i)\leq\lvert r_i\rvert\Delta \pi_i$.
For each current cell $C$, selecting its standing action $a_i=\sigma_i(C)$ gives zero gain for every token in that cell, so $L_i^{\mathrm{cur}}(G;r_i)\geq0$.
Therefore $0\leq J_i(G;r_i)\leq\lvert r_i\rvert\Delta \pi_i$, which gives $\widehat B_i(r_i)\leq T\Delta \pi_i$.
Computability follows by finite enumeration using only the deliberative record, the standing policy, and the agent-known model primitives and test calibration.
The election rule is the achievability-weighted represented gain net of the inquiry cost.
Finally, because every $J_i(G;r_i)$ is nonnegative and the outside option is zero, the maximum in equation (7) is strictly positive exactly when some coherent grouping has strictly positive representational increment. ∎

The participation rule is a coherent non-Bayesian criterion operating precisely where the acting belief is undefined, and it respects every discipline of [section 4.6](#sec-commitments): $\widehat B_i$ quantifies over the agent's own remembered tokens and the groupings it can articulate—“situations like the ones I lost will recur, and a distinction that sorted them would let me act on them”—never over named future representations.
For each coherent reading, the current-language benchmark first values the best action already expressible uniformly on each current awareness cell; gross representational leverage is only the additional robust gain from conditioning action on the finer grouping.
The estimate can be wrong, and honestly so: the agent does not know whether a distinction realizing its best grouping exists, which is why $\lambda_i^{(k)}$ prices achievability.
Two comparative properties organize the applications.
*Action separation, not information*: the value of a question tracks whether a finer distinction could improve action beyond the best current-cell-uniform response, not how much residual uncertainty remains; an agent for whom no coherent grouping yields positive representational increment declines to inquire.
*Rational cessation*: an agent for whose record no coherent grouping yields positive representational increment has $\widehat B_i=0$, so sustained success can extinguish inquiry even though awareness stays incomplete; and, by the decay of $\lambda_i^{(k)}$, so can sustained failure—a true, valuable, repairable question can be rationally abandoned.

### Enlightened inertia {#rem-stickiness}

The model deliberately treats acquiring a distinction and acting on it as sequential decisions.
Pre-insight the agent uses $\widehat B_i$ as a gross estimate of representational leverage, while the known switching hurdle $\kappa_i$ is applied only after a concrete refinement, belief, conjecture, and policy make the realized horizon gain well defined ([assumption 4.4](#ass-commitment) and [proposition 8.4](#prop-participation)).
This timing is a bounded-rationality modeling convention, not a logical implication of unawareness.
Once inquiry delivers a concrete refinement, the realized gain may fail to clear $\kappa_i$, so the agent carries its old policy forward despite knowing that its earlier causal account was incomplete.
Away from pointwise transparency, that enlightened inertia can be unanticipated because pre-insight leverage is only an estimate and the realized refinement may deliver a different gain.
Under pointwise transparency, by contrast, exact and repair-invariant leverage can make later enlightened inertia foreseeable; the model nevertheless preserves the two-stage timing as a deliberate simplification.
Enlightened inertia remains a second source of persistence, distinct from an unpriced question, whether or not mechanisms are deterministic, and it feeds the performance differences of [section 10](#sec-dynamics).

Determinism certifies that two tokens sharing an observed pair but differing in consequence are distinct states, and under the stronger record-level condition of pointwise transparency the deliberative leverage estimate becomes exact and repair-invariant; the full statement is [remark D.4](../appendix/appendix.md#rem-certification) in [appendix D](../appendix/appendix.md#app-deferred).

### Example 1 (continued) {#example-1-continued-4}

At the discovery record ($T=2$, diagonal states served), each firm holds two tokens sharing the profile $(0,1)$ but differing in payoff: firm 1 won at $s_{00}$ and lost at $s_{11}$, firm 2 the reverse.
Because mechanisms are deterministic, the conflicting payoffs *certify* the two tokens as distinct states ([remark D.4](../appendix/appendix.md#rem-certification)), and the agent's best coherent grouping splits them: on the winning token the fine optimal gain is zero, while on the losing token switching to the pinned architecture gains $\tfrac12$ against every rival action—a differentiated loss becomes a pooled half, or a pooled half a differentiated win.
Thus $L_i^{\mathrm{fine}}=\tfrac12$.
Under the coarse one-cell current language, keeping the standing action gives aggregate gain zero, while switching uniformly gains $\tfrac12$ on the losing token and loses $\tfrac12$ on the winning token, so $L_i^{\mathrm{cur}}=0$ and $J_i=\tfrac12$.
Consequently $\widehat B_i=(2/2)(\tfrac12)=\tfrac12$ for both firms—identical gross representational leverage from opposite experiences—so each elects iff $\lambda_i^{(0)}\widehat B_i\geq\gamma_i$, i.e. $\lambda_i^{(0)}/2\geq\gamma_i$.
The positive value is genuinely representational because no uniform current-language action improves on the standing policy.
Acting on the row refinement, once acquired, means re-differentiating by row at the switching hurdle $\kappa_i$; the post-refinement horizon gain remains exactly $\tfrac12$, so the firm re-differentiates when $\kappa_i<\tfrac12$ and—knowing the row law yet finding the change not worth its cost—holds its old policy when $\kappa_i\geq\tfrac12$, the deterministic face of enlightened inertia ([“Enlightened inertia”](#rem-stickiness)).
Under the model's two-stage timing it may still elect inquiry when the participation condition holds; in this transparent case, a hurdle at or above the exact gain makes later enlightened inertia foreseeable, a consequence of the deliberate timing convention rather than of unawareness.
The valuation used no conjecture about the rival and no reference to which refinement might arrive; transparency (winner-take-all) makes each $\Theta_i(g)$ a singleton, so the deliberative estimate is exact.
For rational cessation and its converse, consider a later stretch that serves the two off-diagonal states, by which point firm 1 has acquired the row refinement (certain of the true assignment) while firm 2 has acquired the column refinement (certain of the false one): their policies differ at those states, firm 1 wins both, and the labels revealed there falsify firm 2's column theory.
For firm 1, both the fine and current-language values are zero, so $L_1^{\mathrm{fine}}=L_1^{\mathrm{cur}}=J_1=\widehat B_1=0$: the firm holding the truth rationally never inquires again, and its awareness stays permanently incomplete.
For firm 2, two tokens disagree with its column policy and contribute $\tfrac12$ each under fine contingency, while two agree and contribute zero, so $L_2^{\mathrm{fine}}=1$.
Within either current column, reversing the action gains $\tfrac12$ on one token and loses $\tfrac12$ on the other, so $L_2^{\mathrm{cur}}=0$, $J_2=1$, and $\widehat B_2=(2/4)1=\tfrac12$.
Defeat thus concentrates the evidence, dissonance, and incentive in the losing firm in this example, which elects whenever $\lambda_2^{(k_2)}\widehat B_2\geq\gamma_2$ and, upon success, reaches complete awareness in one step (both column cells must split).
The winner/loser asymmetry—$\widehat B_1=0<\widehat B_2$—is the durable point; the appendix records the exact value of $\widehat B_2$.

## 9. The pivot: formulation, warrant, and the return to Bayes {#sec-pivot}

Successful production yields a refinement $\mathcal P_i'$; the truth-blind formulation rule selects $m'\in\widehat M_i^{\,R}(\mathcal P_i',\bar r_i)$ from the repair-consistent theories on the recoded record; and the agent forms a full-support *bridge prior* $\mu_i^{+}\in\Delta(M(\mathcal P_i'))$, from which ordinary updating resumes.
Nothing in Bayesian coherence determines $\mu_i^{+}$ from the pre-dissonance belief—the domains differ—and this nonuniqueness is not a defect to be repaired but the boundary between insight and judgment.
Write the complete realized post-insight output as $O_i=(\mathcal P_i',m',\mu_i^+)$, treating deterministic bridge-prior selection as a degenerate truth-blind selection rule.
Restricting and renormalizing $\mu_i^{+}$ on $\widehat M_i^{\,R}(\mathcal P_i',\bar r_i)$ yields the initial acting belief on the refined language, whose probability assigned to the formulated theory is its *representation-relative coherence*:

$$
\operatorname{Coh}_i(O_i)
=
\frac{\mu_i^+(m')}
{\displaystyle\sum_{\widetilde m\in\widehat M_i^{\,R}(\mathcal P_i',\bar r_i)}\mu_i^+(\widetilde m)}.
$$

Formulation alone does not determine this probability: it depends jointly on the bridge prior and the repair-consistent active set, but is agent-computable once the refinement, recoded record, and bridge prior exist.
The question of this section is how much of that confidence the evidence actually licenses.

The conjecture on the refined partition is initialized from the recoded empirical frequencies of observed rival actions wherever the record contains observations, with a fixed default on previously unvisited cells, and is updated empirically thereafter.
Thus both inputs needed for the next standing policy—the bridge belief and the strategic conjecture—are defined on the expanded language only after the refinement has arrived.

### Definition 9.1 (Reflective assessment, warrant, and signed gap) {#def-warrant}

A reflective assessment problem is a pair $(\mathcal T,\nu)$: a finite set of candidate objective assignments and a full-support reflective prior.
It is an *analyst-level* construct: conditioning on the events below uses the analyst record and the inquiry history.
Let $h_i$ denote the complete pre-production inquiry history, including prior elections, prior failures, prior successful production-and-formulation outputs, and the current partition generated by that history; in particular, the current pre-production partition $\mathcal P_i$ is $h_i$-measurable.
For a realized complete post-insight output $o=(\mathcal P',m_o,\mu^+)$, define its objective-correctness event by

$$
A_o
=
\left\{
\tau'\in\mathcal T:
\tau'(s)=m_o(C_{\mathcal P'}(s))
\text{ for every }s
\right\}.
$$

Its *selection-adjusted warrant*, relative to the specified assessment problem $(\mathcal T,\nu)$, is

$$
W(o)
=
\nu(A_o\mid\bar r_i,h_i,O_i=o).
$$

The *signed warrant gap* at $o$ is $\operatorname{Coh}_i(o)-W(o)$, whose sign is unrestricted in general.

### Theorem 9.2 (No additional evidence beyond the generating record) {#thm-uninformative}

Conditional on the analyst record $\bar r_i$ and the pre-production inquiry history $h_i$, a record-measurable, truth-blind production, formulation, and bridge-prior-selection rule makes the complete output $O_i=(\mathcal P_i',m',\mu_i^+)$ conditionally independent of the candidate objective assignment.
Consequently, under the reflective joint law, for $K_i(\,\cdot\mid\bar r_i,h_i)$-almost every realized output $o$ and every $\tau'\in\mathcal T$,

$$
\nu(\tau'\mid\bar r_i,h_i,O_i=o)
=
\nu(\tau'\mid\bar r_i,h_i)
$$

and therefore

$$
W(o)
=
\nu(A_o\mid\bar r_i,h_i).
$$

Passing the repair test adds no information beyond the record because post-restoration fit is guaranteed by the successful-output construction.
If candidates assign equal likelihood to $(\bar r_i,h_i)$, their posterior odds remain their reflective prior odds.

#### Proof {#proof-thm-uninformative}

Let $Z_i=(\bar r_i,h_i)$.
Because $\mathcal P_i$ is $h_i$-measurable and the complete output rule is record-measurable and truth-blind, its regular conditional output kernel $K_i(\,\cdot\mid Z_i)$ is candidate-independent.
Thus, for every $\tau'\in\mathcal T$ and every measurable output set $B$, the conditional joint law factors as

$$
\Pr(\tau',O_i\in B\mid Z_i)
=
\nu(\tau'\mid Z_i)K_i(B\mid Z_i).
$$

Election is determined by the deliberative record and failure history; production and formulation are truth-blind; and randomized bridge-prior selection is record-measurable and truth-blind.
The factorization establishes $O_i\perp\!\!\!\perp\tau'\mid Z_i$ and hence the displayed posterior equality for $K_i(\,\cdot\mid Z_i)$-almost every realized output $o$ and every candidate.
Summing that equality over the fixed event $A_o$ gives $W(o)=\nu(A_o\mid\bar r_i,h_i)$.
Passing the repair test is a deterministic implication of the record and realized output and therefore contributes no additional likelihood factor.
If the record-and-history likelihoods are also equal across two candidates, their posterior odds equal their prior odds. ∎

In this precise conditional sense, the insight itself is not evidence: once the complete analyst record and inquiry history are held fixed, a truth-blind output adds no evidential content of its own.
An agent or outside observer who does not possess the complete analyst record may genuinely learn from the output because it conveys information about the hidden particulars on which production operated.
The theorem prohibits treating that information as independent confirmation after the complete generating record has already entered the assessment; its practical force is a prohibition on double counting.
Truth blindness is the polar case; if production, formulation, or bridge-prior selection remains correlated with the objective assignment after conditioning on the record and history—as with transmission from an informed source—the output can supply a genuine Bayes factor, and the adjustment can move warrant in either direction.

### Corollary 9.3 (Self-audit requires sufficiency for the candidates) {#cor-self-audit}

The assessment $(\mathcal T,\nu)$ is expressible by agent $i$ only if its current post-refinement partition $\mathcal P_i'$ is sufficient for every $\tau'\in\mathcal T$, hence only if $\mathcal P_i'$ refines the join of [proposition 7.5](#prop-robust-sufficiency).
This is necessary but not sufficient for complete computation of warrant, which also requires a candidate set, a reflective prior, candidate likelihoods for the generating record and inquiry history, and the relevant selection rule.
An agent holding a minimal restoration therefore generally cannot formulate the cross-representation comparison required to determine the sign or magnitude of its signed warrant gap.
A broader-awareness assessor may be able to formulate the comparison; fresh evidence changes reflective warrant only when its likelihood differs across the represented candidate worlds, and otherwise further awareness expansion may be required before the agent can use the evidence for that comparison.

#### Proof {#proof-cor-self-audit}

Entertaining $\tau'$ as a hypothesis requires expressing it, which is sufficiency ([definition 4.2](#def-awareness)); sufficiency for every candidate is refinement of the join. ∎

The pivot is now complete, and it is the paper's fulcrum.
Dissonance broke the agent's Bayesian competence; inquiry produced a distinction; formulation and the bridge prior rebuilt a probability space; and judgment—fresh evidence with differential likelihoods, honestly accounted—resumes as ordinary updating on the expanded language.
The agent has returned to the Bayesian world carrying an analyst-defined signed warrant gap whose sign and magnitude it generally cannot compute.

### Example 1 (continued) {#example-1-continued-5}

Suppose firm $i$'s technology produces the column refinement.
The recoded record pins the unique consistent theory: architecture $0$ on the first column, $1$ on the second.
Representation-relative coherence assigns it probability one.
Now conduct the reflective assessment with $\mathcal T=\{\text{row world},\text{column world}\}$ and a symmetric prior.
The two worlds assign the realized diagonal-only record equal probability by the same coupling argument conditional on the diagonal-state event, and the technology is truth-blind, so by [theorem 9.2](#thm-uninformative) the reflective posterior equals the prior: $W(O_i)=\tfrac12$, and the signed warrant gap is $1-\tfrac12=+\tfrac12$.
The same example-specific gap applies to a firm that acquires the *row* refinement: its representation-relative coherence is also one, its warrant is also one-half, and confidence exceeds warrant even when the formulated theory happens to be objectively correct.
By [corollary 9.3](#cor-self-audit), neither firm can conduct this assessment itself: expressing both candidate worlds requires the full partition into singletons.
One fresh differentiated observation at an off-diagonal state resolves the row/column identification problem completely because the two worlds predict opposite labels there: if the formulated theory is correct, $W(O_i)$ rises to one and the positive signed gap closes; if it is false, it is rejected, the singleton active set empties, and the acting belief becomes undefined.
At $\beta=1$ under pooled play, any number of pooled observations remains nondiagnostic between the row and column worlds.
In this four-state laboratory at $\beta=1$, differentiated play purchases the evidence that separates the row and column worlds; pooled play does not.

## 10. Strategic dynamics: when everyone lives in a Bayesian world {#sec-dynamics}

The chain now runs inside a population.
Theories determine standing policies; policies determine which conditionals are visited; visited conditionals determine dissonance and leverage; and refinements feed back into theories.
This section characterizes where the process comes to rest.
The object of interest is not a strategic equilibrium but an epistemic condition: a configuration of the population in which *every agent permanently inhabits a Bayesian world*—models fit, questions are dead, and no represented calculation prices further inquiry above its cost.

### Definition 10.1 (Self-confirming unawareness equilibrium) {#def-scue}

A profile of epistemic states $\xi_i=(\mathcal P_i,r_i,\bar\mu_i,q_i,\sigma_i,k_i)$, $i\in N$—awareness, retained record, reference posterior, conjecture, standing policy, and failure counter, with acting beliefs $\mu_i$ derived by judged updating—is a *self-confirming unawareness equilibrium* (SCUE) if, under the play it induces,

- (i) each standing policy is stationary under the switching rule of [assumption 4.4](#ass-commitment): no switch clears the hurdle, $T\,[\,U_i(\sigma_i^{\star}\mid\mu_i,q_i)-U_i(\sigma_i\mid\mu_i,q_i)\,]\le\kappa_i$, which is subjective optimality itself when $\kappa_i=0$;
- (ii) each conjecture $q_i$ agrees, in the limit of its empirical frequencies, with the play induced by $\sigma_{-i}$ at every on-path cell;
- (iii) no dissonance survives: each agent's active set, computed from its record as play accumulates, is almost surely eventually nonempty, and the acting-belief mass on any $\eta$-inadequate theory vanishes almost surely; and
- (iv) no agent elects inquiry: $\lambda_i^{(k_i)}\widehat B_i(r_i)<\gamma_i$ along the induced records, which holds in particular whenever $\widehat B_i=0$.

The record and failure counter belong in the state: dissonance status, leverage, and the achievability weight are functions of retained evidence and inquiry history, so two histories with identical partitions, beliefs, and policies but different records can differ in equilibrium status.
Conditions (ii)–(iii) are stated asymptotically because empirical conjectures and stochastic tests fluctuate at finite samples.
Deterministic consequence mechanisms make a contradictory test observation irreversible, but they do not eliminate sampling variation in states or in rivals' actions within an agent's awareness cell; empirical conjectures therefore generally still converge only asymptotically.

Conditions (i)–(ii) are subjective rationality with confirmed conjectures: the self-confirming conditions of the fixed-language tradition (Fudenberg and Levine 1993; Kalai and Lehrer 1993).
Conditions (iii)–(iv) are the new, epistemic ones: the language survives its own evidence, and the question has no priced value.
A SCUE in which every partition is sufficient for $\tau$ and beliefs concentrate near the truth is simply a self-confirming equilibrium; the concept's interest lies entirely in the other cases.

### Definition 10.2 (Dissonant stasis) {#def-stasis}

Agent $i$ is in *dissonant stasis* from some period on if dissonance recurs while it never both elects and succeeds—because $\lambda_i^{(k_i)}\widehat B_i(r_i)<\gamma_i$ (no priced repair: zero leverage, or an abandoned question after the achievability weight has decayed, possibly at an irreparable record), or because elected production fails at every subsequent attempt.
Its standing policy is carried forward with a standing anomaly.
A population profile is *absorbing* if every agent is, from some period on, either in a SCUE role (never dissonant) or in dissonant stasis.

Table 2 collects the taxonomy of terminal conditions developed in this section, including the enlightened inertia of [“Enlightened inertia”](#rem-stickiness).

**Table 2.** Taxonomy of terminal conditions: how questions die.

| Terminal condition | What survives | Why inquiry died | Payoff consequence | Example instance |
|---|---|---|---|---|
| SCUE ([definition 10.1](#def-scue)) | a represented model class adequate on path, with acting beliefs on it | answered, or never priced: $\lambda_i^{(k_i)}\widehat B_i<\gamma_i$, in particular $\widehat B_i=0$ | can be first-best, or carry concealed payoff-relevant error | the $\beta=1$ trap: both firms certain of the false column law, each earning $\tfrac12$ forever |
| Dissonant stasis ([definition 10.2](#def-stasis)) | no admitted theory; the standing policy carries a standing anomaly | unpriced ($\widehat B_i=0$), abandoned ($\lambda_i^{(k)}$ decayed), or unanswerable (irreparable record) | permanent disadvantage possible | at $\beta<1$: the coarse firm earns $\tfrac14$ against its refined rival's $\tfrac34$, permanently |
| Enlightened inertia ([“Enlightened inertia”](#rem-stickiness)) | a refined language and an improved model, learned but not acted on | answered, but the recommended switch is unpriced: horizon-$T$ gain $\le\kappa_i$ | the agent forgoes the improvement its rival captures | $\kappa_i\ge\tfrac12$ after acquiring the row law: the firm knows it and holds its old policy |

### A represented model class, restored endogenously {#rem-grain}

Rational-learning convergence traditionally requires a grain of truth: the environment is absolutely continuous with respect to beliefs (Kalai and Lehrer 1993).
Under unawareness the objective assignment may be inexpressible on the current language.
Causal dissonance is the model's operational signal that no admitted theory survives the current evidence; in the stochastic setting it is not by itself proof that the objective truth is inexpressible.
Successful refinement restores a nonempty represented model class consistent with the retained record.
It does not by itself establish objective correctness or future on-path adequacy; subsequent experience determines whether the restored language survives.
A SCUE is a configuration in which an admitted represented model class continues to survive on path and no agent has a priced reason to seek a finer one.

### Assumption 10.3 (Regularity) {#ass-regularity}

(i) *Strict adequacy.*
At each visited pair every theory is either $\eta$-adequate or strictly inadequate—none sits exactly at the adequacy boundary—so [lemma D.1](../appendix/appendix.md#lem-test-consistency) applies for every agent, theory, partition profile, and policy profile.
(ii) *Production randomness.*
The randomization in each $\phi_i$ is independent across elections and of the state and consequence draws, and, conditional on an election at a *repairable* record ($\mathcal R(\mathcal P_i,\bar r_i)\neq\emptysetset$), production succeeds with probability at least $\underline\pi>0$.
At an irreparable record production fails surely ([definition 7.2](#def-technology)).

Part (i) is the genericity that makes each theory's evidence process settle cleanly relative to the capacity threshold ([lemma D.1](../appendix/appendix.md#lem-test-consistency)); it rules out only a boundary knife-edge and holds automatically under the exact calibration ([“The Calibration Convention”](#conv-calibration)).
Part (ii) gives every elected repairable question a real chance of resolution; finiteness of elections comes instead from the decay of the achievability weight, so no separate never-produce exclusion is needed.
The agent, unable to tell a repairable record from an irreparable one, may elect either; the two are distinguished only in their success probabilities, not in the agent's decision.

### Theorem 10.4 (Epistemic absorption) {#thm-absorption}

Under [assumption 10.3](#ass-regularity), almost surely:

- (a) at most $n(|S|-1)$ refinements occur, and every agent's awareness partition is eventually constant;
- (b) only finitely many inquiry elections occur—each agent stops electing once its achievability weight has decayed enough that $\lambda_i^{(k)}\,T(\max \pi_i-\min \pi_i)<\gamma_i$, and this happens after finitely many consecutive failures because $\widehat B_i$ is bounded and $\gamma_i>0$; and
- (c) there is an almost surely finite period after which no agent's language changes and no agent pays an inquiry cost: every agent's epistemic life thereafter is judged-Bayesian updating within a fixed language, punctuated at most by belief-driven policy switches under [assumption 4.4](#ass-commitment) and by dissonance events that fail the participation threshold.

Moreover, on the event that the standing profile is eventually constant,

- (d) every agent's active set is eventually constant; every theory retained in that eventual active set is $\eta$-adequate at every recurrent pair under terminal play, every theory $\eta$-inadequate at a recurrent pair under terminal play is eventually absent, and each agent is eventually either never dissonant—it lives in a Bayesian world—or in dissonant stasis ([definition 10.2](#def-stasis)).

The proof is in [appendix B](../appendix/appendix.md#app-absorption).

Converging non-stasis configurations limit to a partial SCUE, and a SCUE configuration with strict optimality margins and zero leverage persists—exactly with deterministic mechanisms, and with probability at least $1-\sum_i e^{-b_i}$ in the stochastic case, so capacity governs the robustness of a rest point; the formal statement is [proposition D.5](../appendix/appendix.md#prop-rest-points) in [appendix D](../appendix/appendix.md#app-deferred), with proof in [appendix B](../appendix/appendix.md#app-absorption).

### What the theorem does and does not claim {#rem-scope}

[Theorem 10.4](#thm-absorption) is a statement about the epistemic process—the death of inquiry—not about the convergence of play.
Within a Bayesian world, standing policies may in principle continue to cycle as beliefs and conjectures chase one another; that is the classical convergence problem of learning in games (Fudenberg and Levine 1993; Kalai and Lehrer 1993), it is orthogonal to this paper's contribution, and the theorem deliberately does not resolve it.
Part (d) and the rest-point characterization are accordingly conditional on play stabilizing, which in every configuration featured in this paper is immediate: their beliefs make one action per cell strictly dominant.
Switching costs temper the cycling: the inaction band absorbs belief fluctuations too small to be worth acting on, so only swings whose horizon-$T$ gain exceeds $\kappa_i$ move play—a stabilizing force, though not one that rules out large-amplitude cycles.
The decay of $\lambda_i^{(k)}$ is what makes inquiry die out even when the question is genuine: an agent facing a true, valuable, but hard-to-repair defect abandons it once repeated failure has eroded its hope.
Abandoned questions are thus a substantive absorbing outcome, not an artifact—inquiry ceases because it is answered, because it is unpriced, or because it is given up.
Were $\lambda_i^{(k)}$ held fixed instead of decaying, an agent could elect a doomed inquiry forever, paying $\gamma_i$ each period for a repair that never arrives; the decay rules this out and is the model's account of when a rational inquirer stops.

### Rational anomaly tolerance {#rem-anomaly}

Zero-leverage dissonant stasis is a recognizable condition, not a pathology of the model: the agent registers that no admitted theory survives its test—yet its deliberative valuation finds no coherent grouping with positive representational increment, so repairing the account is worth nothing to it.
Standing anomalies tolerated by working scientists and managers have exactly this structure, and the model locates them: anomaly tolerance is rational precisely when the agent's coherent groupings carry no gross representational leverage.
Two sharper instances complete the taxonomy.
At an irreparable record ([remark D.3](../appendix/appendix.md#rem-irreparable)) no expressible repair exists at any price—the anomaly is not merely unprofitable but impossible to fix within the current grammar—though the agent, unable to certify irreparability under noise, may keep electing while its deliberative record supports positive leverage and until the achievability weight decays.
And an *abandoned question* is a repairable, positively-valued defect the agent stops pursuing because repeated failure has driven $\lambda_i^{(k)}\widehat B_i$ below cost: rational surrender, not indifference.

In a SCUE, surviving error lives only in what play never exposes: acting-belief mass on every $\eta$-inadequate theory vanishes, and all retained falsity is confined to pooled mechanism assignments within tolerance at visited profiles and to counterfactual claims at unvisited profiles ([proposition D.6](../appendix/appendix.md#prop-adequacy), [appendix D](../appendix/appendix.md#app-deferred)).

In stochastic environments capacity is a single cognitive-style dial—expected detection time under an exposed profile is $O(b_i/D_i)$ while spurious dissonance at a non-exposed rest point has probability at most $e^{-b_i}$—and it plays no role in the exact deterministic case; the formal statement and proof are [proposition D.7](../appendix/appendix.md#prop-capacity) in [appendix D](../appendix/appendix.md#app-deferred).

### Proposition 10.5 (Persistent performance differences) {#prop-persistence}

There exist primitives and absorbing configurations in which agents hold different terminal partitions and theories, and expected per-period payoffs differ strictly and permanently, with no disadvantaged agent closing the gap—because for each the corrective process has died economically at one of its two stages: either its question is unpriced (*dissonant stasis*, $\lambda_i^{(k_i)}\widehat B_i(r_i)<\gamma_i$ from some period on), or, having asked and refined, the policy change its new model recommends is priced below the switching hurdle (*enlightened inertia*, $T$-horizon gain $\le\kappa_i$, [“Enlightened inertia”](#rem-stickiness)).

The stasis channel is established by the instance below; the enlightened-inertia channel is the deterministic possibility of [“Enlightened inertia”](#rem-stickiness) (a firm that acquires the true distinction yet, facing $\kappa_i$ above the gain, forgoes the improvement its rival captures). The mechanism deserves emphasis.
Performance differences persist not because an equilibrium concept freezes them but because the process that would erase them has died economically: the disadvantaged agent's question is priced below the cost of asking—through zero leverage, an eroded achievability weight, or an irreparable record—or, having asked and learned, it finds the switch its new model recommends priced below the hurdle and holds its old policy ([“Enlightened inertia”](#rem-stickiness)).
Terminal heterogeneity in awareness is path dependence in the strong sense—agents with identical preferences and identical Bayesian competence, facing the same objective system, end at different languages and different payoffs because their histories posed different questions.

### Two sources of heterogeneity {#rem-two-sources}

Terminal heterogeneity has two independent origins here.
Agents identical in preferences, competence, capacity, and cost can still end at different languages and payoffs, because their histories posed different questions and their truth-blind technologies produced different repairs—path dependence that begins before probability.
Agents identical in *everything* but their dissonance capacity $b_i$ and switching hurdle $\kappa_i$ also diverge: in stochastic environments capacity affects detection speed and the robustness of rest points ([proposition D.7](../appendix/appendix.md#prop-capacity)), while the hurdle sets the propensity to enlightened inertia ([“Enlightened inertia”](#rem-stickiness)); the capacity channel disappears under exact deterministic contradiction.
The first is the awareness-path microfoundation; the second a parametric cognitive-style one—and neither is available in the fixed-language tradition.

In environments whose primitives are *diagnostic*—payoff-relevant policy errors always expose the erring agent's awareness under confirmed stationary play—no SCUE contains a payoff-relevant policy error; the formal apparatus is [definition D.8](../appendix/appendix.md#def-diagnostic) and [proposition D.9](../appendix/appendix.md#prop-diagnostic) in [appendix D](../appendix/appendix.md#app-deferred).

### Concealment is necessary, not sufficient {#concealment-is-necessary-not-sufficient}

By [proposition D.6](../appendix/appendix.md#prop-adequacy), an objectively false theory that retains nonvanishing acting-belief mass in a stable SCUE must be $\eta$-adequate on path; the induced profile is therefore concealing for that theory in the sense of [definition 6.4](#def-exposure).
Concealment alone does not guarantee survival.
The theory must also be admitted when the language is initialized, avoid prior and subsequent rejection, retain nonvanishing acting-belief mass, support a stationary standing policy, coexist with confirmed conjectures, and leave no profitable inquiry election.
In stochastic environments even an active $\eta$-adequate theory remains subject to the conditional false-rejection bound of [lemma D.1](../appendix/appendix.md#lem-test-consistency); under the exact calibration false rejection is impossible ([“The Calibration Convention”](#conv-calibration)), but the remaining SCUE conditions are still required.

Strictly punishing primitives—those whose on-path conditionals at every payoff-relevant policy error separate from every expressible prediction by more than $\eta$—are diagnostic, as [proposition D.10](../appendix/appendix.md#prop-punishing) in [appendix D](../appendix/appendix.md#app-deferred) records.

Strict payoff and separation margins at a fixed profile survive small perturbations of the primitives, though this is a local stability property rather than openness of global diagnosticity; see [remark D.11](../appendix/appendix.md#rem-local-robustness) in [appendix D](../appendix/appendix.md#app-deferred).

### Example 1 (continued) {#example-1-continued-6}

*The trap.*
Set $\beta=1$ and suppose both firms acquired the column refinement after discovery and became certain of the false column assignment.
Each plays the column policy; the firms pool at every state; every payoff is one-half; and one-half is exactly what the column theory predicts under pooled play.
The configuration is a SCUE with payoff-relevant error: policies are subjectively optimal, conjectures confirmed, and no dissonance ever occurs because the profile is concealing—so the technology never triggers, whatever its cost or reliability.
The positive signed warrant gap of the running example is permanent: unbounded pooled experience accumulates while each firm remains exactly half-warranted, the missing half being the reflective weight on the world their shared language cannot express.

*The knife edge.*
Now let $\beta<1$.
In the first period serving an off-diagonal state, the pooled firms receive $\beta/2$ where their theory predicts one-half: the demand side reveals the label, dissonance returns, $\widehat B$ turns positive, and the reflective posterior becomes degenerate.
Payoff-relevant self-confirmation is a knife-edge property of perfectly forgiving demand, and the destroyed value $1-\beta$ at each misserved period is itself the corrective signal: what demand withholds from the firms, their epistemics receives as evidence.

*Persistence.*
Run the asymmetric configuration at $\beta<1$: firm 1 holds the row refinement and the true assignment, while firm 2 remains coarse and is dissonant from an entry period $t_0$ onward.
To make its stasis permanent, suppose

$$
\gamma_2
>
\lambda_2^{(k_{2,t_0})}
\widehat B_2(r_{2,t})
\qquad
\text{for every subsequent record \(r_{2,t}\) generated by this profile.}
$$

A simple record-uniform sufficient condition is

$$
\gamma_2
>
\lambda_2^{(k_{2,t_0})}
T\bigl(\max\pi_2-\min\pi_2\bigr),
$$

using the bound in [proposition 8.4](#prop-participation).
Under either condition firm 2 never elects after $t_0$, its failure count remains unchanged, and it is in dissonant stasis.
Here firm 2's coarse record genuinely rejects all three constant theories—its differentiated losses defeat the constant theory matching its own action, its pooled payoff of one-half defeats the opposite theory's $\beta/2$ prediction, and neutrality fails at the differentiated losses—so it is dissonant rather than merely mistaken, and it stays put because its question is priced below cost.
With constant action $c$, the two correctly served tokens contribute zero and the two misserved tokens contribute $\tfrac12$ each under fine contingency, so $L_2^{\mathrm{fine}}=1$.
A uniform current-language reversal has aggregate robust gain $\beta-1<0$, while retaining the standing action gives zero, so $L_2^{\mathrm{cur}}=0$, $J_2=1$, and, for this balanced four-token record with $T=2$, $\widehat B_2=\tfrac12$.
For other realized record compositions the gross representational leverage remains positive when some coherent grouping supplies a positive increment and is bounded as in [proposition 8.4](#prop-participation).
Firm 1 offers the preferred architecture in the row its rival misserves, winning both those states and splitting the rest, so under uniform $\rho$ the firms earn three-quarters and one-quarter, permanently.
At $\beta=1$, the same initial constant-$c$ record leaves the opposite constant theory as firm 2's only active theory.
If the reversal that theory recommends clears the switching hurdle, firm 2 switches once from $c$ to $1-c$.
Under the reversed policy, a subsequent visit to a state in the true row $c$ produces a diagnostic contradiction and rejects that last active theory.
Because the constant-$c$ and neutral theories were already permanently rejected and theories do not re-enter, the active set then becomes empty and firm 2 enters dissonance rather than oscillating.
If the switching hurdle blocks the initial reversal, firm 2 may instead remain in policy inertia under [assumption 4.4](#ass-commitment).
Thus the $\beta=1$ continuation is either a one-switch path into renewed dissonance or a stable policy-inertia path, depending on the switching hurdle; it is not an indefinite oscillation.
The example illustrates several routes out: strategic variety, demand harshness, and cheaper or more hopeful inquiry.

## 11. Discussion {#sec-discussion}

### 11.1 Implications for the theory-based view {#implications-for-the-theory-based-view}

The model supplies the theory-based view with an upstream source of strategic heterogeneity: question histories.
Experiences can pose different questions, truth-blind technologies can produce different repairs, and inquiry can stop at different points, leaving agents with different languages, theories, and payoffs ([proposition 10.5](#prop-persistence)).
The order of experience matters because it changes which defects become visible and which refinements become available before Bayesian judgment resumes.
This channel does not require heterogeneity to begin with different priors; the model also permits cognitive-style differences in detection capacity and switching hurdles, but question-dependent representation change is the distinctive source.
It therefore complements rather than replaces familiar explanations based on heterogeneous resources, incentives, beliefs, or capabilities.
Two firms facing the same opportunity may not disagree over common theories at all: one may possess an actionable distinction the other has never formulated, so comparing priors starts too late.

Inquiry creates value through *action separation*, not uncertainty reduction.
Deliberative leverage asks whether a coherent reading of retained experience supports a finer contingent policy whose robust value exceeds the best policy already expressible on each current cell ([proposition 8.4](#prop-participation)).
High uncertainty without such an increment is economically irrelevant, whereas a narrow contrast crossing an action threshold can be worth pursuing.
The same logic integrates anomaly tolerance and cessation: a firm may rationally leave a question unasked when leverage is zero, stop after its achievability weight decays, or abandon a record no admissible refinement can repair ([“Rational anomaly tolerance”](#rem-anomaly)).
In the running example, competitive defeat concentrates diagnostic evidence and produces a winner/loser inquiry asymmetry; the example exhibits this mechanism without implying that losers generally have greater inquiry incentives.
Success can remove action-separating leverage, repeated production failure can reduce the assessed chance of resolution, and a genuine anomaly can remain economically dormant when no feasible refinement changes robust action.
Questions can therefore die through success, discouragement, or irreparability even though the underlying causal structure remains unresolved.

Warrant depends on *independent discrimination*, not retrospective fit.
The result disciplines interpretations of scientific entrepreneurship (Camuffo et al. 2020; Zellweger and Zenger 2023): once the complete generating record and inquiry history are conditioned upon, a record-measurable truth-blind output earns no additional warrant merely by organizing that record.
Validation requires evidence whose likelihood differs across relevant candidate worlds, yet the agent may lack the awareness needed to formulate that comparison ([corollary 9.3](#cor-self-audit)).
A broader-awareness board, investor, advisor, or other outsider can serve as a warrant assessor if it represents the alternatives and has an appropriate assessment model; outside challenge can therefore play a warrant role under those conditions.
The relevant contribution is diagnostic variation separating worlds the focal agent cannot jointly represent, so governance is epistemically useful only when the outsider's broader language and evidence support that discrimination.

Strategic interaction and market conditions govern *exposure and concealment*.
Shared false theories can remain viable when play pools states that a coarse language treats alike, but concealment does not guarantee survival.
Strategic differentiation can supply diagnostic contrasts, and observable environmental punishment can reveal misservice even under common play ([proposition D.9](../appendix/appendix.md#prop-diagnostic)).
These are recurring exposure mechanisms rather than an exhaustive classification.
Accordingly, a strategically deviant actor functions as epistemic infrastructure only when its variation exposes the coarse language; strong customer outside options can instead discipline a consensus, while forgiving demand can protect it.
A false theory may predict well along the path it induces because its policy suppresses the contrast that would refute it, yet the same theory can fail after a rival differentiates or customers visibly punish misservice.
Concealment is only protection: changes in play or subsequent inquiry can still unsettle the represented class.

### 11.2 The cognitional interpretation {#the-cognitional-interpretation}

The architecture also tracks a cognitional account of inquiry (Lonergan 1992; Ryall and Wilkins 2018).
Experience supplies the record; dissonance poses and localizes a question; coherent groupings provide heuristic anticipation without semantic content; and refinement is insight's formal footprint.
Formulation assigns mechanisms to new cells, judgment tests the adequacy of the represented class, and decision appears as the standing policy that shapes subsequent experience.
The cross-representation warrant assessment remains an analyst-level comparison the agent may be unable to perform ([corollary 9.3](#cor-self-audit)).
The mathematics represents the products and price of insight rather than the conscious semantic act itself.
The mapping keeps experience, question, insight, formulation, judgment, and decision analytically separate.

### 11.3 Limitations and the research program {#limitations-and-the-research-program}

The principal ontological boundary combines three restrictions: the elementary mechanism vocabulary is fixed, the analyst's state space is finite and fixed, and semantic production is a primitive operation.
Novelty is therefore agent-relative: refinement makes an analyst-represented distinction available to the agent but does not create objective states or elementary mechanisms.
The model can explain why a new representation is demanded and constrained, but not creation of the analyst's ontology or a new kind of causal mechanism.

Three extensions follow.
First, inquiry intensity, duration, and technological success can become endogenous, connecting question valuation to costly deliberation and planning (Ryall 2026).
Second, replacing individual agents with theory-bearing organizations would study how insights become shared languages, collective intentions, and commitments (Ryall and Wilkins 2018).
Third, connecting this pre-Bayesian front end to cooperative value capture would allow awareness rents, disclosure, and bargaining over newly represented opportunities (Gans and Ryall 2017; Bryan et al. 2022).
These extensions can enrich how long inquiry lasts, who bears a theory inside an organization, and how the resulting awareness advantage is appropriated.

## 12. Conclusion {#sec-conclusion}

This paper supplies the upstream step that the theory-based view has lacked: where theories come from relative to an actor's prior causal language.
Bayesian learning ranks possibilities inside such a language; producing a new one begins when causal dissonance separately diagnoses that the represented class has failed.

Three insights organize the transition back to Bayes.
Experience directs repair without selecting its answer, so economical representation change is necessarily fallible.
An agent can value a question before representing candidate answers because leverage isolates the value of finer actionable contingency from corrections already available in the current language.
And generating a representation is not warranting it: conditional on the complete generating record and inquiry history, a record-measurable truth-blind output adds no evidence of its own, and retrospective fit is not independent validation.

These results matter for strategy because theories shape the actions that generate subsequent evidence.
The paper establishes the existence of absorbing configurations in which heterogeneous question histories and stopping points sustain different terminal languages and payoffs.
It does not claim that every performance difference has this origin; it identifies a pre-prior mechanism by which otherwise similar firms can diverge.
They can come to different theories because they came to different questions, and because some questions died or were abandoned before resolution.
The contribution is an origin result: enduring variety can begin with different histories of which questions became thinkable and worth pursuing.

## References {#references}

- Adner, Ron, Levinthal, Daniel (2024). Strategy Experiments in Nonexperimental Settings: Challenges of Theory, Inference, and Persuasion. *Strategy Science*, 9(4), 311–321.
- Berk, Robert H. (1966). Limiting Behavior of Posterior Distributions when the Model is Incorrect. *Annals of Mathematical Statistics*, 37(1), 51–58.
- Bryan, Kevin A., Ryall, Michael D., Schipper, Burkhard C. (2022). Value Capture in the Face of Known and Unknown Unknowns. *Strategy Science*, 7(3), 157–189. https://doi.org/10.1287/stsc.2021.0126
- Camuffo, Arnaldo, Cordova, Alessandro, Gambardella, Alfonso, Spina, Chiara (2020). A Scientific Approach to Entrepreneurial Decision Making: Evidence from a Randomized Control Trial. *Management Science*, 66(2), 564–586. https://doi.org/10.1287/mnsc.2018.3249
- Camuffo, Arnaldo, Gambardella, Alfonso, Pignataro, Andrea (2024). Theory-Driven Strategic Management Decisions. *Strategy Science*, 9(4), 382–396. https://doi.org/10.1287/stsc.2024.0173
- Chavda, Ankur, Gans, Joshua S., Stern, Scott (2024). Theory-Based Entrepreneurial Search. *Strategy Science*, 9(4), 397–415. https://doi.org/10.1287/stsc.2024.0166
- Dekel, Eddie, Lipman, Barton L., Rustichini, Aldo (1998). Standard State-Space Models Preclude Unawareness. *Econometrica*, 66(1), 159–173.
- Ehrig, Timo, Zenger, Todd (2024). Competing with Theories: Using Awareness and Confidence to Secure Resources and Rents. *Strategy Science*, 9(4), 416–432. https://doi.org/10.1287/stsc.2024.0177
- Felin, Teppo, Holweg, Matthias (2024). Theory Is All You Need: AI, Human Cognition, and Causal Reasoning. *Strategy Science*, 9(4), 346–371. https://doi.org/10.1287/stsc.2024.0189
- Felin, Teppo, Zenger, Todd R. (2017). The Theory-Based View: Economic Actors as Theorists. *Strategy Science*, 2(4), 258–271. https://doi.org/10.1287/stsc.2017.0048
- Felin, Teppo, Gambardella, Alfonso, Zenger, Todd (2024). Theory-Based Decisions: Foundations and Introduction. *Strategy Science*, 9(4), 297–310. https://doi.org/10.1287/stsc.2024.intro.v9.n4
- Fudenberg, Drew, Levine, David K. (1993). Self-Confirming Equilibrium. *Econometrica*, 61(3), 523–545.
- Gans, Joshua, Ryall, Michael D. (2017). Value Capture Theory: A Strategic Management Review. *Strategic Management Journal*, 38(1), 17–41. https://doi.org/10.1002/smj.2592
- Grant, Simon, Meneghel, Idione, Tourky, Rabee (2022). Learning Under Unawareness. *Economic Theory*, 74, 447–475. https://doi.org/10.1007/s00199-021-01408-y
- He, Yang-Bo, Geng, Zhi (2008). Active Learning of Causal Networks with Intervention Experiments and Optimal Designs. *Journal of Machine Learning Research*, 9, 2523–2547.
- Heifetz, Aviad, Meier, Martin, Schipper, Burkhard C. (2006). Interactive Unawareness. *Journal of Economic Theory*, 130(1), 78–94.
- Heifetz, Aviad, Meier, Martin, Schipper, Burkhard C. (2013). Dynamic Unawareness and Rationalizable Behavior. *Games and Economic Behavior*, 81, 50–68.
- Kalai, Ehud, Lehrer, Ehud (1993). Rational Learning Leads to Nash Equilibrium. *Econometrica*, 61(5), 1019–1045.
- Kalai, Ehud, Lehrer, Ehud (1993). Subjective Equilibrium in Repeated Games. *Econometrica*, 61(5), 1231–1240.
- Karni, Edi, Vier\o, Marie-Louise (2013). ``Reverse Bayesianism'': A Choice-Based Theory of Growing Awareness. *American Economic Review*, 103(7), 2790–2810. https://doi.org/10.1257/aer.103.7.2790
- Karni, Edi, Vier\o, Marie-Louise (2017). Awareness of Unawareness: A Theory of Decision Making in the Face of Ignorance. *Journal of Economic Theory*, 168, 301–328. https://doi.org/10.1016/j.jet.2016.12.011
- Lonergan, Bernard J. F. (1992). *Insight: A Study of Human Understanding*. University of Toronto Press.
- Ott, Timothy E., Hannah, Douglas P. (2024). On the Origin of Entrepreneurial Theories: How Entrepreneurs Craft Complex Causal Models with Theorizing and Data. *Strategy Science*, 9(4), 461–482. https://doi.org/10.1287/stsc.2024.0178
- Pearl, Judea (2009). *Causality: Models, Reasoning, and Inference*. Cambridge University Press.
- Piermont, Evan (2021). Unforeseen Evidence. *Journal of Economic Theory*, 193, 105235. https://doi.org/10.1016/j.jet.2021.105235
- Ryall, Michael D. (2003). Subjective Rationality, Self-Confirming Equilibrium, and Corporate Strategy. *Management Science*, 49(7), 936–949. https://doi.org/10.1287/mnsc.49.7.936.16383
- Ryall, Michael D. (2009). Causal Ambiguity, Complexity, and Capability-Based Advantage. *Management Science*, 55(3), 389–403. https://doi.org/10.1287/mnsc.1080.0938
- Ryall, Michael D. (2026). Mathematical Analysis of Agents $C$, $C^+$, and $C^\mathrmPlan$. Unpublished action-theory manuscript, Appendix A.
- Ryall, Michael D., Wilkins, Jeremy (2018). Insight and Social Being. Unpublished manuscript.
- Schipper, Burkhard C. (2021). Discovery and Equilibrium in Games with Unawareness. *Journal of Economic Theory*, 198, 105365. https://doi.org/10.1016/j.jet.2021.105365
- Schipper, Burkhard C. (2025). Predicting the Unpredictable Under Subjective Expected Utility. Working paper, University of California, Davis. arXiv:2403.01421.
- Sorenson, Olav (2024). Theory, Search, and Learning. *Strategy Science*, 9(4), 372–381. https://doi.org/10.1287/stsc.2024.0179
- Spirtes, Peter, Glymour, Clark, Scheines, Richard (2000). *Causation, Prediction, and Search*. MIT Press.
- Vier\o, Marie-Louise (2021). An Intertemporal Model of Growing Awareness. *Journal of Economic Theory*, 197, 105351. https://doi.org/10.1016/j.jet.2021.105351
- Zellweger, Thomas, Zenger, Todd (2023). Entrepreneurs as Scientists: A Pragmatist Approach to Producing Value Out of Uncertainty. *Academy of Management Review*, 48(3), 379–408. https://doi.org/10.5465/amr.2020.0503

[^1]: Under misspecification the posterior concentrates on the expressible theories closest to the data-generating process (Berk 1966); Esponda and Pouzo (2016) develop the equilibrium counterpart. Ortoleva (2012) models paradigm shifts in which a surprised agent switches priors, but his agent switches among alternatives represented ex ante; here the replacement is inexpressible before insight.
[^2]: Here $\Delta(X)$ denotes the set of probability distributions on $X$. Deterministic causal effects are a special case.
