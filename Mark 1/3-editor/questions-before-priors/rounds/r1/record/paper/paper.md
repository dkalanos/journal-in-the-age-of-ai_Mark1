# Questions Before Priors: Causal Dissonance, Insight, and the Origin of Strategic Theories

Michael D. Ryall · July 2026 — First draft

*%
Preliminary draft; comments welcome.  This paper develops the formal core of
a research program on pre-Bayesian theory formation in strategy.*

**AI appendix.** An AI appendix in the published form (record protocol formal-0.3) accompanies this paper at `ai-appendix/` in its research record: definitions, procedure, the claims list, the authors' stance, reproduction anchors, and scope.

## Abstract {#abstract}

The theory-based view treats economic actors as theorists whose causal
understandings direct search, experimentation, and action.  Existing formal
treatments begin after the theory exists.  This paper models where strategic
theories come from.  Agents represent their environment through awareness
partitions of a state space; expressible causal theories assign elementary
mechanisms to awareness cells; theories and beliefs determine committed
policies; and the policy profile causes everyone's consequences through an
objective causal system.  Bayesian learning operates only within the current
language, and a misspecified posterior grows confident rather than alarmed,
so detecting representational failure requires a distinct faculty: causal
dissonance, the statistical rejection of every expressible theory.
Dissonance directs inquiry without determining its output; a costly, fallible
technology may produce a previously inexpressible distinction; and a bridge
prior restores Bayesian competence on the expanded language.  The value of a
question is computable before its answers are conceivable, warrant is
distinct from post-insight confidence—the insight itself is not
evidence—and an agent generally cannot measure its own overconfidence.
Because theories cause actions and actions generate evidence, inquiry dies
out almost surely, leaving every agent in a Bayesian world; the
configurations that remain can preserve false theories, heterogeneous
awareness, and permanent performance differences whenever neither strategic
variety nor environmental harshness exposes them.

**Keywords:** theory-based view; unawareness; insight; causal
learning; subjective rationality; self-confirming equilibrium

## 1. Introduction {#sec-intro}

The theory-based view of strategy holds that economic actors are theorists:
managers and entrepreneurs carry causal accounts of how value is created, and
those accounts—not merely their information or their incentives—direct
what they notice, which experiments they run, and what they do
(Felin and Zenger 2017; Felin et al. 2024).  A decade of work has
established the consequences of holding a theory.  Theories guide
experimentation and search (Camuffo et al. 2020; Chavda et al. 2024),
support the acquisition of resources and rents (Ehrig and Zenger 2024), and
discipline entrepreneurial decision-making in the field
(Camuffo et al. 2024).  What this literature has not yet formalized is the
step before all of that: where a genuinely new theory comes from.  Existing
formal treatments begin with the theory present—as a menu of candidate
theories to select among (Camuffo et al. 2024), as a given causal
conjecture that directs search (Chavda et al. 2024), or as a given
awareness advantage to be exploited competitively (Ehrig and Zenger 2024).
The origin of the theory is described verbally and documented empirically
(Ott and Hannah 2024), and the absence of formal machinery for it has been
explicitly noted as the field's open analytical problem
(Felin et al. 2024).

The difficulty is not a missing application of Bayesian reasoning; it is a
boundary of Bayesian reasoning.  A Bayesian agent updates beliefs over a
space of represented possibilities.  Conditioning reweights that space and
cannot enlarge it, so no sequence of updates makes an unrepresented causal
distinction available for belief or action.  Worse, when every represented
theory is false, the posterior does not sound an alarm: by the logic of
misspecified Bayesian learning (Berk 1966), it concentrates on the least
wrong of the available theories, and the agent grows more confident, not
less.  Within-language updating is self-sealing.  The economics of growing
awareness has developed axiomatic accounts of how beliefs should extend when
the state space expands (Karni and Vier\o 2013; Karni and Vier\o 2017; Vier\o 2021), but
in those models the expansion itself arrives exogenously; models of discovery
in games describe how play can reveal objectively available actions
(Schipper 2021) without explaining how experience generates a
substantive causal question or its answer.  What is missing, in both the
strategy literature and the economics of unawareness, is a model of the
transition: from a broken causal language, through a directed question, to a
new representation, and back to ordinary Bayesian life.

This paper models that transition, embedded in strategic interaction.  Its
organizing object is the chain

$$
\text{dissonance}
\longrightarrow
\text{inquiry}
\longrightarrow
\text{refined awareness}
\longrightarrow
\text{new models}
\longrightarrow
\text{Bayesian judgment},
$$

the process by which an agent whose causal representation has failed regains
the capacity to be a Bayesian.  The back end of the model follows the
subjective-rationality tradition (Kalai and Lehrer 1993; Ryall 2003): a finite
set of agents adopt causal theories, combine them with beliefs and
conjectures to choose committed policies, and the policy profile determines
every agent's consequences through an objective causal system that absorbs
all market and environmental detail.  The front end is new.  Agents represent
the environment through awareness partitions of a state space; the theories
they can formulate assign elementary causal mechanisms to awareness cells;
and the partition itself—the language—is endogenous.  An awareness cell
is an implicit claim that the states it pools are causally alike.  Strategic
experience can refute that claim: when the statistical record rejects every
expressible theory, the agent faces *causal dissonance*, a determinate
defect with no expressible repair.  Dissonance makes a question salient
without providing its answer.  A costly, fallible, truth-blind inquiry
technology may then produce a refinement of the partition—the formal
footprint of an insight—after which a bridge prior restores a probability
space and Bayesian judgment resumes on the expanded language.

Five sets of results give the chain its content.  First, boundary results
locate exactly where Bayesian competence stops: conditioning cannot expand
the language, and the misspecified posterior is self-sealing, so detecting
representational failure requires a faculty formally distinct from
updating.  Second, dissonance directs inquiry without determining it.  The
record restricts admissible repairs—every restorative refinement must
separate the evidence clusters that no single mechanism can accommodate—but
generally many minimal repairs remain, observationally equivalent worlds
demand different answers, and no truth-blind technology can be uniformly
correct.  Fallibility is the price of a representation that economizes on
distinctions.  Third, the value of a question is computable before its
answers are conceivable.  A leverage statistic built from retained
experience—invariant across every representation that could answer the
question—prices inquiry at exactly the moment the posterior is undefined,
and it tracks whether an answer could change action, not how much uncertainty
remains.  Questions die rationally: sustained success extinguishes them,
and defeat concentrates both the evidence and the incentive to inquire in
the losing firm.  Fourth, the return to Bayes is disciplined by a warrant
account: because any successful repair fits the experience that generated it
by construction, retrospective fit carries no information, and—when
inquiry is truth-blind—neither does the arrival of the insight itself.
Post-insight confidence therefore exceeds warrant by a computable gap, and an
agent holding a minimal repair generally cannot even formulate the comparison
that would measure its own gap.  Fifth, because theories cause actions and
actions generate the evidence, the population dynamics close the loop.
Almost surely, awareness change and inquiry die out, leaving every agent
permanently inhabiting a Bayesian world—models fit, questions are dead,
inquiry is priced below cost.  We call the configurations in which the
process rests *self-confirming unawareness equilibria*, and their
interest is epistemic rather than strategic: such a configuration can
preserve false theories, heterogeneous awareness, and permanent performance
differences, and it does so precisely when neither of the two corrective
forces—strategic variety inside an agent's categories, or an environment
harsh enough to punish misservice observably—is present.

The persistence results deserve emphasis because of what carries them.
Performance differences persist in this model not because an equilibrium
concept freezes them but because the process that would erase them has died
economically: the disadvantaged configuration generates no dissonance, or
generates no leverage, or prices its question below the cost of asking.
Strategic variety is therefore traced to its source.  Agents with identical
preferences, identical data-processing competence, and identical objective
opportunities end up with different causal languages, different theories, and
different payoffs because their experiences posed different questions, their
technologies produced different repairs, and their subsequent positions
extinguished further inquiry at different points.  This is a microfoundation
for heterogeneity that begins before probability does.

A deliberately small example runs through the paper—two firms, four
customer states, two product architectures—in which every object can be
computed exactly: the four minimal repairs of a broken language, the two that
survive a simplicity filter, the impossibility of choosing between them from
the data, the exact price of the question, the exact warrant gap, and the
knife-edge condition under which a market's shared false theory protects
itself forever.  The example is a laboratory, not the theory; each of its
results instantiates a general statement.

The paper proceeds as follows.  [Section 2](#sec-literature) locates the
contribution.  [Section 3](#sec-model) presents the model.
[Section 4](#sec-bayesian) develops the Bayesian layer and its boundary;
[section 5](#sec-dissonance) defines dissonance and exposure;
[section 6](#sec-inquiry) analyzes restoration, direction, and fallibility;
[section 7](#sec-economics) prices inquiry; [section 8](#sec-pivot) develops formulation,
warrant, and the return to Bayesian competence; and [section 9](#sec-dynamics)
closes the loop with the population dynamics.  [Section 10](#sec-discussion)
discusses implications and the research program.

## 2. Related literature {#sec-literature}

### The theory-based view {#the-theory-based-view}

The foundational claim is that theories do more than summarize evidence: they
direct attention toward causal possibilities, support counterfactual
reasoning, and guide experimentation (Felin and Zenger 2017).  The
*Strategy Science* collection on theory-based decisions substantially
developed the view (Felin et al. 2024):
Camuffo et al. (2024) formalize the choice of which theory to test and show
that the value of experimentation grows with the number and uncertainty of
candidate theories; Chavda et al. (2024) model search guided by a
given causal theory; Ehrig and Zenger (2024) translate theories into
awareness structures and show how partial disclosure secures resources and
rents; Sorenson (2024) and Adner and Levinthal (2024) probe the
mechanisms and the limits of theory-guided experimentation; and
Ott and Hannah (2024) document empirically how entrepreneurs develop a
poorly formed thesis into an articulated causal model.  A parallel empirical
program shows that training entrepreneurs to formulate and test theories
improves performance (Camuffo et al. 2020).  Related conceptual work
presses the same open question this paper addresses: Zellweger and Zenger (2023)
treat entrepreneurs as scientists generating beliefs under uncertainty, and
Felin and Holweg (2024) argue that forward-looking causal theorizing is
precisely what data-driven prediction cannot supply.  Throughout, the
formal treatments condition on the theory, the attribute list, or the
awareness advantage being present.  This paper supplies the front end those
models presuppose, and its equilibrium analysis shows when the supplied front
end matters: heterogeneous causal languages, and the performance differences
they support, persist exactly when the strategic and environmental conditions
identified below fail to erase them.

### Unawareness and growing awareness {#unawareness-and-growing-awareness}

Standard state-space models cannot represent nontrivial unawareness
(Dekel et al. 1998); generalized structures represent multiple
awareness levels and interactive beliefs
(Heifetz et al. 2006; Heifetz et al. 2013).  On belief
revision under expansion, reverse Bayesianism preserves relative odds as the
state space grows (Karni and Vier\o 2013), with extensions to awareness of
unawareness (Karni and Vier\o 2017), intertemporal settings (Vier\o 2021),
unforeseen evidence (Piermont 2021), and learning under incomplete
awareness (Grant et al. 2022).  Schipper (2021)
distinguishes learning, which discards conceived possibilities, from
discovery, which adds unconceived ones, and shows how play can move players
to richer games; Schipper (2025) shows that beliefs about novelty can be
held without representing the novel objects—a precedent for the delabeled
constructs used here.  Relative to this literature the paper endogenizes what
those models take as given: the expansion event itself.  Experience generates
the defect, the defect localizes the question, a fallible technology produces
the new distinction, and the bridge prior problem—which reverse Bayesianism
constrains but does not solve—is embedded in an explicit account of what
the generating evidence can and cannot warrant.  In strategy,
Bryan et al. (2022) bring unawareness into value capture and show
that awareness itself earns rents; the present paper models where the
awareness advantage originates, which that paper leaves open.

### Causal learning with a fixed vocabulary {#causal-learning-with-a-fixed-vocabulary}

Causal graphical models separate intervention from association
(Pearl 2009; Spirtes et al. 2000); Ryall (2009) brings this machinery to
strategy, modeling imitation as Bayesian inference over operating structures
in which passive observation narrows candidates to an
observational-equivalence class and experimentation may discriminate among
survivors.  Active-learning methods select interventions to split a
represented equivalence class (He and Geng 2008).  These models are the
benchmark for the paper's second learning tier: inference over structures
expressible in a fixed vocabulary.  The paper begins where they stop—when
no expressible structure is adequate—and its nonidentification results
extend the equivalence-class logic to the choice among vocabulary repairs:
observationally equivalent worlds can demand different distinctions, so no
truth-blind repair rule is uniformly correct.

### Subjective rationality and self-confirming equilibrium {#subjective-rationality-and-self-confirming-equilibrium}

The back end follows Kalai and Lehrer (1993) and Fudenberg and Levine (1993):
beliefs correct on the path of play need not be correct off it, and
subjectively optimal behavior against such beliefs can persist.
Ryall (2003) showed that competitive advantage can rest entirely on
rivals' self-confirming false theories.  Those models fix the hypothesis
space; convergence results in the rational-learning tradition require a grain
of truth—the truth absolutely continuous with respect to beliefs
(Kalai and Lehrer 1993).  Under unawareness the grain-of-truth condition can
fail at the level of language: the truth may be inexpressible.  This paper
supplies the missing dynamics.  Statistical dissonance is the detector of
language-level failure, awareness refinement restores the grain of truth on
the path of play, and the fixed-language models are recovered exactly as the
special case in which awareness never changes.  The paper's absorbing
configurations extend self-confirming equilibrium with two epistemic
conditions—the language survives its own evidence, and no question is worth
its price—and it is these conditions, not the strategic ones, that carry
the new results.

### Statement of contribution {#statement-of-contribution}

Existing models show how theories guide learning, how Bayesian agents
discriminate among represented causal structures, and how play can reveal
previously unavailable actions.  This paper models a different transition.
An agent's causal language pools objectively different situations;
strategic experience endogenously reveals an action-relevant failure of that
pooling and thereby creates a localized open question; costly inquiry
activates a fallible technology whose output is not measurable in the agent's
prior awareness; only after that output is formulated does the agent
construct a prior and undertake Bayesian judgment, under an explicit account
of how much confidence the generating experience licenses.  Because actions
depend on theories, play can either create the contrasts that generate
questions or suppress them—so the model also delivers the population-level
answer: when theory heterogeneity and performance differences persist, and
when the market erases them.

## 3. The model {#sec-model}

### 3.1 Agents, states, actions, and consequences {#sec-primitives}

There are $n$ agents, $N=\{1,\dots,n\}$.  Time is divided into generations
$g=1,2,\dots$, each consisting of $T$ episodes.  In each episode a state
$s\in S$, with $S$ finite, is drawn independently from a full-support
distribution $\rho\in\Delta(S)$; each agent takes an action $a_i$ from a
finite set $A_i$ through a committed policy described below; and a
consequence profile $x=(x_1,\dots,x_n)$ is realized in a finite space
$X=\prod_iX_i$.  Agent $i$'s consequence $x_i$ is everything the episode
delivers to it—profit, sales, observed reactions—and its payoff is a
function $u_i:X_i\to\mathbb R$ of that consequence.  Write $A=\prod_iA_i$ for
action profiles.

States are the analyst's descriptions of the payoff-relevant situations
agents may face: customer configurations, input conditions, competitive
circumstances.  Their status in the agents' own representations is the
subject of [section 3.3](#sec-awareness-sub).

### 3.2 Mechanisms and the objective causal system {#sec-mechanisms-sub}

#### Definition 3.1 (Elementary mechanisms and the objective system) {#def-mechanisms}

A finite set $\Theta$ of *elementary causal mechanisms* is given, each a
map $\theta:A\to\Delta(X)$.  The *objective assignment* is a function
$\tau:S\to\Theta$, and the *objective causal system* is

$$
F(\cdot\mid s,a)=\tau(s)(a)\in\Delta(X). \tag{1}
$$

Two states are *causally equivalent* if they carry the same mechanism;
$\mathcal P^{\tau}$ denotes the partition of $S$ into causal-equivalence
classes, and $\marg{i}\theta(a)$ the $X_i$-marginal of $\theta(a)$.

The causal reading of equation (1) is maintained throughout and
does real work.  $F$ is a response function, not a statistical summary: it
specifies the distribution of consequences that *would* result from
every action profile at every state, including profiles never played.
Agents' actions, together with the state, cause their consequences.  A
mechanism is the reduced form of whatever detailed model—a structural
causal model of customer behavior, a market microstructure, a production
process—underlies that relation; the paper imposes no structural-causal-model
formalism, but examples may exhibit micro-foundations explicitly, as the
running example's customer market does.  Three consequences of the causal
reading recur.  First, theories, defined next, are interventional objects:
they make predictions at unplayed profiles.  Second, on-path data constrain
$F$ only at visited state–profile pairs, so observationally equivalent
systems with different counterfactual content are generic; that is the engine
of the identification results.  Third, the on-path distribution of
consequences given an agent's category of states is a *selection*
object—it mixes mechanisms according to which states co-occur with which
play—and must never be conflated with any mechanism's own conditional.

### 3.3 Awareness, theories, and conjectures {#sec-awareness-sub}

#### Definition 3.2 (Awareness and expressible theories) {#def-awareness}

Agent $i$'s awareness partition is $\mathcal P_i\in\Pi(S)$, the set of
partitions of $S$.  Every consciously available object—theory, belief,
conjecture, policy, question—must be measurable with respect to
$\mathcal P_i$.  The *expressible theories* are the cell-constant
mechanism assignments

$$
M(\mathcal P_i)=\{m:\mathcal P_i\to\Theta\}, \tag{2}
$$

with $m$ predicting $x_i\sim\marg{i}m(C)(a)$ at cell $C$ under profile $a$.
Partition $\mathcal P$ is *sufficient* for an assignment $\tau'$ if
$\tau'$ is constant on every cell of $\mathcal P$, equivalently if $\mathcal
P$ refines $\mathcal P^{\tau'}$; the objective assignment is expressible for
agent $i$ if and only if $\mathcal P_i$ is sufficient for $\tau$.

An awareness cell is thus an implicit causal claim: the states it pools are
alike in how actions produce consequences.  An expressible theory makes the
claim explicit by naming the mechanism.  Restricting theories to
*single* mechanism assignments—rather than arbitrary conditional
distributions per cell—is substantive and deliberate.  If any distribution
were expressible, any within-cell mixture would be too, and no experience
could reject the class: coarseness alone cannot produce a detectable failure
in a saturated model space.  The mechanism vocabulary $\Theta$ is known to
all agents from the outset; what an agent may lack is the *distinction*
that separates states carrying different mechanisms.  Everything the paper
calls insight is the production of such a distinction.  Expansion of the
mechanism vocabulary itself is a deeper dimension of awareness growth
deliberately left outside this paper.

Agent $i$ holds a belief $\mu_i\in\Delta(M(\mathcal P_i))$ over expressible
theories—formally, the acting tier of a two-tier belief specified in
[section 5](#sec-dissonance)—and a conjecture
$q_i:\mathcal P_i\to\Delta(A_{-i})$ about rival play, both
$\mathcal P_i$-measurable.  Theories and conjectures are different
kinds of objects and are deliberately separated: a theory is a causal claim
about the objective system; a conjecture is a strategic claim about what
other agents will do.  The diagnostic apparatus developed below tests
theories, not conjectures.

#### Assumption 3.3 (Observation and retention) {#ass-observation}

At the end of each episode, agent $i$ observes
$(C_{\mathcal P_i}(s),a,x_i)$: its awareness cell containing the realized
state, the realized action profile, and its own consequence.  Episodes are
retained as tokens in a deliberative record $r_i$ and can be retrospectively
recoded after the agent acquires a new distinction; before acquisition,
neither belief nor action can condition on that distinction.  The
analyst-level history additionally records $s$ itself, so that a newly
produced representation can recode the tokens.

Retention without recodability-in-advance is the minimal separation between
experiencing a particular and possessing a projectible concept for it: the
agent can remember “customers like that one” without commanding a predicate
that distinguishes them, and the technology of [section 6](#sec-inquiry) operates on
exactly this material.  Observability of the full action profile keeps the
separation of causal from strategic error clean; a variant folding components
of $a$ into $x_i$ changes bookkeeping only.

#### Assumption 3.4 (Commitment and subjective optimality) {#ass-commitment}

At the start of each generation, agent $i$ commits to a policy
$\sigma_i:\mathcal P_i\to A_i$ satisfying

$$
\sigma_i(C)\in\arg\max_{a_i\in A_i}
\sum_{m\in M(\mathcal P_i)}\mu_i(m)
\sum_{a_{-i}\in A_{-i}}q_i(a_{-i}\mid C)\,
\mathbb E_{x\sim m(C)(a_i,a_{-i})}\!\left[u_i(x_i)\right], \tag{3}
$$

holds it for the generation's $T$ episodes, and revises beliefs, conjectures,
and policies only between generations.  When dissonance
([section 5](#sec-dissonance)) has made $\mu_i$ undefined and no new representation
has been produced, the previously committed policy is carried forward.
Agents evaluate one generation ahead; no discounting is imposed.

Commitment is where statistics and economics meet: a test needs a stable
data-generating configuration, and a generation of committed play supplies
exactly that.  What a deterministic model must assume as a batching device
is, in the stochastic model, the natural granularity of learning.

### 3.4 On-path conditionals {#on-path-conditionals}

Fix a generation with committed profile $\sigma=(\sigma_1,\dots,\sigma_n)$.
Each state $s$ receives the deterministic profile
$a(s)=(\sigma_j(C_{\mathcal P_j}(s)))_{j\in N}$.  Agent $i$'s *on-path
conditional* at an observation pair $(C,a)$ with
$S(C,a)=\{s\in C:a(s)=a\}\neq\emptysetset$ is

$$
p_i^{*}(\cdot\mid C,a)
=
\sum_{s\in S(C,a)}\rho\bigl(s\mid S(C,a)\bigr)\,\marg{i}\tau(s)(a). \tag{4}
$$

This is the selection object flagged above: rivals with finer partitions
condition on distinctions agent $i$ cannot see, so the within-cell state
mixture can vary with the profile.  It is precisely this
dependence—differentiated play by others inside one's own
categories—that generates the contrasts on which the diagnostic apparatus
feeds.

### 3.5 Modeling commitments {#sec-commitments}

Five disciplines govern everything that follows; they are what distinguish a
model of unawareness from a model of inattention or model selection.
(i) Agents hold no prior over the outputs of the inquiry technology and never
optimize over named future theories; pre-insight deliberation quantifies only
over represented objects.  (ii) Questions are generated by defects in the
current representation, not drawn from a primitive list.  (iii) Inquiry can
fail, and its successes can be false; nothing reveals the objective
assignment by construction.  (iv) All valuations attached to inquiry are
subjective, coarse, and possibly wrong; no objective payoff information
leaks from behind the awareness frontier.  (v) Evidence that generates a
candidate representation is separated, in the formal accounting, from
evidence that warrants it.

### 3.6 The running example {#the-running-example}

#### Example 1 (A four-state laboratory) {#ex-setup}

Two firms serve a unit market.  States are customer configurations
$S=\{s_{00},s_{01},s_{10},s_{11}\}$, displayed as a $2\times2$ array with row
coordinate $r$ and column coordinate $c$; $\rho$ is uniform.  Actions are
product architectures $A_i=\{0,1\}$.  The mechanism vocabulary is
$\Theta=\{\theta^0,\theta^1,\theta^n\}$, with a demand parameter
$\beta\in[0,1]$: under $\theta^a$ (“architecture $a$ is preferred”), if the
firms differentiate, the firm offering $a$ receives payoff $1$ and its rival
$0$; if they pool on $a$, each receives $\tfrac12$; if they pool on the other
architecture, each receives $\beta/2$, the customer withholding $1-\beta$ of
the unit value.  Under $\theta^n$ (“architecture is neutral”), each firm
receives $\tfrac12$ regardless.  A consequence $x_i$ is the pair (own payoff,
observed action profile).  The objective assignment is the *row law*
$\tau(s_{rc})=\theta^{r}$: the row coordinate is causally relevant, the
column coordinate is not.  Both firms begin with the coarse partition
$\mathcal P_i^0=\{S\}$, under which the expressible theories are the three
constant assignments; the row law is not among them, because it is not
constant on $S$.  The baseline sets $\beta=1$ (deterministic winner-take-all
with market splitting); $\beta<1$ returns in [section 9](#sec-dynamics).  All
mechanisms here are deterministic, so every test below operates in its exact,
zero-tolerance instance; nothing in the general development relies on that.

## 4. Bayesian competence and its boundary {#sec-bayesian}

Within fixed awareness, learning is ordinary.  Observations representable in
the current language update $\mu_i$ by Bayes' rule; conjectures are updated
empirically from observed play.  If no agent's awareness ever changes, the
model is a repeated interaction among subjectively rational Bayesian
learners in the sense of Kalai and Lehrer (1993) and Ryall (2003), and
its stable configurations are self-confirming equilibria
(Fudenberg and Levine 1993).  Everything new in this paper happens at the
boundary of that layer, which two results locate.

### Proposition 4.1 (No Bayesian emergence) {#prop-no-emergence}

Bayesian conditioning on any event measurable with respect to the algebra
generated by $\mathcal P_i$ yields a posterior on $\Delta(M(\mathcal P_i))$.
No sequence of such updates makes a theory outside $M(\mathcal P_i)$
expressible or a distinction finer than $\mathcal P_i$ usable in a policy.

#### Proof {#proof-prop-no-emergence}

Conditioning reweights a distribution on its domain and cannot enlarge the
domain; every element of $M(\mathcal P_i)$ is cell-constant, so every
posterior mixture, and every policy optimal against one, is
$\mathcal P_i$-measurable. ∎

### Remark 4.2 (The posterior is self-sealing) {#rem-self-sealing}

The stochastic setting yields a sharper point.  Suppose every expressible
theory is false: the agent's cell mixes mechanisms, so no cell-constant
assignment matches the on-path conditionals.  A full-support posterior does
not signal this.  By the logic of misspecified Bayesian learning
(Berk 1966), it concentrates on the expressible theories closest to the
on-path conditionals in Kullback–Leibler divergence, and the agent becomes
increasingly *confident* in a wrong theory.  Posterior mass always sums
to one; the inadequacy of the whole model class is not an event in the
agent's algebra.  Detecting that the language itself is broken therefore
requires a faculty outside the posterior—the consistency test of the next
section.  The distinction matters for how the theory-based view should treat
“updating”: ranking the answers one can express and judging whether any
expressible answer is adequate are different cognitive operations, and only
the first is Bayesian.

### Example 1 (continued) {#example-1-continued}

Under the coarse partition, firm $i$'s expressible theories are the constant
assignments $m^0$, $m^1$, $m^n$.  The row law $\tau$ is inexpressible: no
reweighting of $\{m^0,m^1,m^n\}$, on any evidence, produces it
([proposition 4.1](#prop-no-emergence)).  A firm that will later observe payoffs
irreconcilable with all three theories will find its posterior undefined, not
alarmed—the deterministic instance of [remark 4.2](#rem-self-sealing), in which
misspecification announces itself only because likelihoods hit zero exactly.
With stochastic mechanisms, no announcement would occur at all.

## 5. Causal dissonance {#sec-dissonance}

### 5.1 Tests and active sets {#tests-and-active-sets}

#### Definition 5.1 (Consistency test and active set) {#def-test}

Fix a tolerance $\eta\geq0$, a minimum count $\bar n\geq1$, and a
nonincreasing slack sequence $w(\cdot)\to0$.  Given record $r_i$ with counts
$n_i(C,a)$ and empirical conditionals $\hat p_i(\cdot\mid C,a)$, theory
$m\in M(\mathcal P_i)$ *passes* if

$$
\TV\bigl(\hat p_i(\cdot\mid C,a),\,\marg{i}m(C)(a)\bigr)
\leq
\eta+w\bigl(n_i(C,a)\bigr)
\qquad
\text{for every }(C,a)\text{ with }n_i(C,a)\geq\bar n, \tag{5}
$$

where $\TV$ is total-variation distance.  The *active set*
$\widehat M_i(\mathcal P_i,r_i)$ collects the passing theories.  Under a
committed profile, call $m$ *$\eta$-adequate* if
$\TV(p_i^{*}(\cdot\mid C,a),\marg{i}m(C)(a))\leq\eta$ at every visited pair
and *$\eta$-inadequate* if the inequality fails strictly at some visited
pair.

#### Lemma 5.2 (Test consistency) {#lem-test-consistency}

Fix a committed profile played in all generations and suppose no theory's
distance to an on-path conditional equals $\eta$ exactly.  As generations
accumulate, almost surely every $\eta$-adequate theory is eventually always
in the active set and every $\eta$-inadequate theory is eventually never in
it.

##### Proof {#proof-lem-test-consistency}

Visited pairs accumulate observations without bound almost surely under
i.i.d. full-support states, so
$\hat p_i(\cdot\mid C,a)\to p_i^{*}(\cdot\mid C,a)$ by the strong law of
large numbers.  The triangle inequality places
$\TV(\hat p_i,\marg{i}m(C)(a))$ within any $\epsilon>0$ of
$\TV(p_i^{*},\marg{i}m(C)(a))$ from some generation on; the genericity
hypothesis converts strict inequalities into eventual acceptance and
rejection, and the slack sequence absorbs finite-sample fluctuation before
that generation. ∎

The deterministic case is the degenerate instance $\eta=0$, $\bar n=1$,
$w\equiv0$: passing is exact consistency with every retained episode.

#### Judged updating {#judged-updating}

Beliefs carry two tiers.  The *reference posterior* $\bar\mu_i$ begins
at a full-support prior on $M(\mathcal P_i)$ and updates by likelihoods
alone; it is never conditioned on the test.  The *acting belief*
$\mu_i$ is the reference posterior restricted and renormalized to the
current active set, so that belief never rides on a rejected theory; when
the active set is empty, the acting belief is undefined and the
carry-forward clause of [assumption 3.4](#ass-commitment) governs.  Because restriction
always applies to the unrestricted tier, the acting belief is well defined
whenever the active set is nonempty—including when a fluctuating test
empties the set and later refills it—provided the reference posterior
gives the refilled set positive mass.  In the stochastic case we therefore
maintain that every marginal $\marg{i}\theta(a)$ has full support, which
keeps all likelihoods positive; in the deterministic case no assumption is
needed, since rejection coincides with a zero-likelihood event, refill
cannot occur, and judged updating reduces to ordinary Bayesian
conditioning.  After a refinement, both tiers restart from the full-support
bridge prior on the expanded space ([section 8](#sec-pivot)).  Judged updating is
the formal junction between the test and the posterior—between judgment
and understanding ([remark 4.2](#rem-self-sealing))—and it guarantees, in
[section 9](#sec-dynamics), that surviving acting beliefs are supported on adequate
theories.

### 5.2 Dissonance and exposure {#dissonance-and-exposure}

#### Definition 5.3 (Causal dissonance) {#def-dissonance}

Agent $i$ experiences *causal dissonance* at the end of a generation if
$\widehat M_i(\mathcal P_i,r_i)=\emptysetset$: every expressible theory is
rejected.  The expressible set does not disappear; no element of it accounts
for the record.  The immediate question has a determinate defect but not a
determinate answer: *what unrepresented difference among the pooled
states explains the heterogeneity of their consequences?*

Dissonance is the model's rendering of a question for intelligence.  It is
localized (the failing cells are identified by the test), it is directed (an
adequate repair must reconcile the record), and it is semantically open (no
expressible object names the missing distinction).  Whether dissonance ever
occurs, however, depends on whether play makes the falsity of the language
visible.

#### Definition 5.4 (Exposure and concealment) {#def-exposure}

Under a committed profile, awareness $\mathcal P_i$ is *exposed* if
every $m\in M(\mathcal P_i)$ is $\eta$-inadequate.  A committed profile is
*concealing* for agent $i$ if some expressible theory is
$\eta$-adequate under it while false as a claim about $\tau$ at some state
its cells cover.

#### Proposition 5.5 (Exposure and dissonance) {#prop-exposure}

Under a fixed committed profile, agent $i$ experiences dissonance from some
generation onward almost surely if and only if $\mathcal P_i$ is exposed.

##### Proof {#proof-prop-exposure}

Immediate from [lemma 5.2](#lem-test-consistency): exposure means every expressible
theory is eventually rejected; its failure means some theory is eventually
always accepted. ∎

Exposure has two sources, and the distinction organizes much of what
follows.  Heterogeneity inside a cell surfaces either because *other
agents play differently across the pooled states*—strategic
differentiation inside one's categories, which changes the visited profiles
and the induced mixtures—or because *the environment punishes uniform
play across causally different states in an observable way*.  Both reappear
as the corrective forces in [section 9](#sec-dynamics).

#### Example 1 (continued) {#example-1-continued-2}

Let $\beta=1$ and suppose the firms' priors over the constant theories are
heterogeneous: firm 1 considers $\theta^0$ more likely than $\theta^1$, and
firm 2 the reverse.  A direct computation shows that, against any conjecture
about the rival, offering architecture $0$ is subjectively strictly dominant
for firm 1 and architecture $1$ for firm 2 whenever
$\mu_i(m^a)>(2-\beta)\,\mu_i(m^{a'})$; at $\beta=1$ this is simple belief
asymmetry.  The firms therefore commit to differentiated constant policies.
Consider a generation in which $s_{00}$ and $s_{11}$ are served.  With
differentiated actions, the winner-take-all payoffs reveal the objectively
preferred architecture at each state: firm 1 wins at $s_{00}$ (payoffs
$1,0$) and loses at $s_{11}$ (payoffs $0,1$).  No constant assignment is
consistent with both episodes—$m^0$ fails at $s_{11}$, $m^1$ at $s_{00}$,
and $m^n$ predicts one-half at both—so each firm's active set empties:
causal dissonance, in its exact deterministic form.  Had the firms instead
pooled on the same architecture at both states, each would have received
one-half at every episode, an outcome consistent with all three constant
theories: the pooled profile is concealing, and coarse awareness would have
survived its own evidence indefinitely.  Belief heterogeneity, by inducing
differentiated play, is what made the shared language's failure visible.

## 6. Inquiry: restoration, direction, and fallibility {#sec-inquiry}

Dissonance poses a question the current language cannot answer.  This
section characterizes what a successful answer must accomplish, shows that
the requirement directs inquiry without determining its output, and
establishes that any inquiry process meeting the paper's disciplines must be
fallible.

### 6.1 Restorative refinements {#restorative-refinements}

For $\mathcal P,\mathcal P'\in\Pi(S)$, write $\mathcal P\prec\mathcal P'$
when $\mathcal P'$ strictly refines $\mathcal P$.  After a refinement, the
retained record is recoded ([assumption 3.3](#ass-observation)) and the test is
re-applied with the recoded counts.

#### Definition 6.1 (Restorative refinement) {#def-restorative}

$\mathcal P'$ is *restorative* at $(\mathcal P_i,r_i)$ if
$\mathcal P_i\prec\mathcal P'$ and
$\widehat M_i(\mathcal P',r_i)\neq\emptysetset$ under the recoded record; it
is *minimally restorative* if no restorative $\mathcal P''$ satisfies
$\mathcal P_i\prec\mathcal P''\prec\mathcal P'$.  Write
$\mathcal R(\mathcal P_i,r_i)$ for the set of minimally restorative
refinements.

#### Proposition 6.2 (Cellwise coherence) {#prop-coherence}

Call a cell of a refinement *coherent* if some single mechanism passes
the test on the cell's recoded observations.  Then
$\widehat M_i(\mathcal P',r_i)\neq\emptysetset$ if and only if every cell of
$\mathcal P'$ is coherent.

##### Proof {#proof-prop-coherence}

Theories factor across cells—$M(\mathcal P')=\Theta^{\mathcal P'}$, and the
constraints in equation (5) apply cell by cell—so a passing assignment
exists exactly when a passing mechanism can be chosen for each cell
independently. ∎

Coherence is the general form of a conflict structure.  Token sets are
*mutually incoherent* when no single mechanism accommodates their
union; every restorative refinement must separate mutually incoherent sets,
since a cell containing both would be incoherent.  In the deterministic
running example incoherence is a binary relation between labeled episodes and
restoration is a graph-coloring problem; in general, a mixture of three
mechanisms may defeat every single mechanism even though each pair of tokens
is individually accommodatable, so restoration is a hypergraph coloring.
Two further structural facts matter.  First, minimal restorations, when they
exist, are typically multiple—as the example shows vividly.  Second,
existence itself is guaranteed only in the deterministic case.

#### Remark 6.3 (Irreparable records) {#rem-irreparable}

With deterministic mechanisms, restoration is always possible: the singleton
partition recodes each token to its own state, where the generating
mechanism fits exactly.  With stochastic mechanisms this guarantee fails.
An unlucky finite sample at a single state can produce an empirical
conditional outside the tolerance of *every* mechanism, and no
partition of $S$ can separate observations generated at the same state; then
$\mathcal R(\mathcal P_i,r_i)=\emptysetset$ and the record is
*irreparable*: dissonance names a defect that no expressible refinement
can repair.  Because $\mathcal R$ is computable from the record, the agent
recognizes irreparability; the technology fails surely
([definition 6.4](#def-technology)); and the participation rule of [section 7](#sec-economics)
assigns the question no value, so no inquiry cost is wasted on it.  Under
recurring visitation, irreparability is transient—empirical conditionals
converge to the generating mechanism's, which lies within any positive
tolerance—but a record whose critical pairs stop being visited can remain
irreparable forever, a possibility the dynamics of [section 9](#sec-dynamics)
classifies within dissonant stasis.

### 6.2 The technology {#the-technology}

#### Definition 6.4 (Representation-producing technology) {#def-technology}

A representation-producing technology for agent $i$ is a possibly randomized
map $\phi_i$ from $(\mathcal P_i,r_i)$ to
$\{\mathcal P_i\}\cup\mathcal R(\mathcal P_i,r_i)$: it fails, returning the
current partition, or succeeds, producing a minimally restorative
refinement.  When $\mathcal R(\mathcal P_i,r_i)=\emptysetset$, the range is
the singleton $\{\mathcal P_i\}$ and the technology fails surely.  It is *truth-blind*: its output distribution depends only
on $(\mathcal P_i,r_i)$, never directly on $\tau$.  A complexity ordering
$\kappa$ on refinements—the analyst's model of which conceptual products
the agent's comparison capacities can generate—may restrict the range
further; $\kappa$ is a primitive of the technology, not an object of the
agent's optimization.

The technology is the paper's stated representational primitive.  No formal
model derives a semantically new concept from nothing; the contribution is to
show how experience *directs* a limited, fallible generative capacity
and why that capacity does not amount to a prior over future theories.  The
output, and even the set of possible outputs, is not a pre-insight
subjective menu: the agent cannot name a candidate refinement, assign it a
probability, or condition a policy on it before production succeeds
([section 3.5](#sec-commitments)).

### 6.3 Nonidentification and the price of robustness {#nonidentification-and-the-price-of-robustness}

#### Theorem 6.5 (Observational nonidentification) {#thm-nonidentification}

Let $\tau\neq\tau'$ be objective assignments inducing the same distribution
over agent $i$'s records under the committed profiles played.  Then any
truth-blind technology, and any truth-blind inquiry-and-formulation rule,
has the same output distribution in both worlds.  If no single theory is
$\eta$-adequate under both worlds at the visited pairs, no truth-blind rule
selects an adequate formulation with probability one in both.

##### Proof {#proof-thm-nonidentification}

The rule's input is the record, whose distribution is identical by
hypothesis, so its output distribution is identical.  If the adequate sets
are disjoint, any realized output is inadequate in at least one world with
the corresponding probability. ∎

#### Proposition 6.6 (Robust sufficiency) {#prop-robust-sufficiency}

A partition sufficient for every assignment in a candidate set $\mathcal T$
must refine $\bigvee_{\tau'\in\mathcal T}\mathcal P^{\tau'}$, the join of the
candidates' causal-equivalence partitions.  A representation guaranteed to
accommodate all observationally equivalent worlds is accordingly finer than
any single world requires; a technology that economizes on distinctions must
accept fallibility.

##### Proof {#proof-prop-robust-sufficiency}

Sufficiency for $\tau'$ is refinement of $\mathcal P^{\tau'}$
([definition 3.2](#def-awareness)); refinement of each candidate's partition is
refinement of their join. ∎

#### Example 1 (continued) {#example-1-continued-3}

After the dissonant generation, the record contains two labeled episodes:
architecture $0$ objectively preferred at $s_{00}$, architecture $1$ at
$s_{11}$.  Of the fifteen partitions of four states, exactly four are
minimally restorative—each must separate $s_{00}$ from $s_{11}$: the row
partition $\{\{s_{00},s_{01}\},\{s_{10},s_{11}\}\}$, the column partition
$\{\{s_{00},s_{10}\},\{s_{01},s_{11}\}\}$, and the two partitions isolating
one labeled state.  The record directs inquiry (eleven partitions are
excluded) without determining it (four remain).  A natural complexity
ordering counts the coordinates needed to describe a refinement: rows and
columns are one-coordinate distinctions, the isolating partitions require
two.  A factor-seeking technology thus produces the row or the column
refinement—and here direction runs out.  Define the *column world*
$\tau'(s_{rc})=\theta^{c}$: it agrees with the row world at both labeled
states, so the two worlds generate identical records
([theorem 6.5](#thm-nonidentification) in exact form).  No truth-blind rule can
formulate correctly in both, a randomized rule succeeds in the worst case
with probability at most one-half, and by [proposition 6.6](#prop-robust-sufficiency) a
partition sufficient for both worlds must be the full partition into
singletons: robustness costs every distinction the language can draw, which
is exactly what a minimal technology economizes on.  The example also
locates the failure mode of each residual candidate: whichever factor
refinement arrives, its unique consistent theory extrapolates the wrong
prediction to the two unlabeled states in one of the two worlds.

## 7. The economics of inquiry {#sec-economics}

Whether to prosecute a question must itself be a decision, and it must be
priced at exactly the moment ordinary decision theory is silent: at
dissonance the posterior is undefined ([definition 5.3](#def-dissonance)), and the
candidate answers are not represented objects ([definition 6.4](#def-technology)).  This
section shows that an honest valuation nevertheless exists: a statistic
computed entirely from retained experience that is invariant across every
representation successful inquiry could produce.

### Assumption 7.1 (Costly, elective, dissonance-triggered production) {#ass-elective}

The technology $\phi_i$ operates only when agent $i$ experiences dissonance
and elects inquiry, $\varepsilon_i=1$, at cost $\gamma_i>0$ in payoff units.
Agent $i$ holds a delabeled success weight $\lambda_i\in(0,1]$: a subjective
probability that an elected episode produces a usable refinement, defined on
the event of success alone and not on the identities of possible outputs.
On failure or abstention the committed policy is carried forward.  Awareness
is cumulative: acquired distinctions are never lost, though theories
formulated on them may later be rejected.

The success weight is awareness of unawareness in delabeled form—the agent
can believe that inquiry may yield a usable distinction without being able
to describe any candidate distinction—a construct with precedent in
beliefs about unpredictable novelty (Schipper 2025; Karni and Vier\o 2017).

### Definition 7.2 (The pinned structure) {#def-pinned}

Let $\mathcal R(\mathcal P_i,r_i)\neq\emptysetset$.  Each restorative
refinement induces, through recoding, a partition of the retained tokens,
and after production only rules constant on that partition's cells are
implementable.  The *pinned structure* $\Lambda_i(r_i)$ is the finest
common coarsening—the meet—of the induced token partitions: a token rule
is implementable *whichever repair arrives* exactly when it is
measurable with respect to $\Lambda_i(r_i)$, and the separations
$\Lambda_i$ preserves—*pinned distinctions*—are those the record
forces on every repair.  For a token $t$, let

$$
\Theta_i(t)
=
\bigl\{\,m'(C'_{\mathcal P'}(t)) :
\mathcal P'\in\mathcal R(\mathcal P_i,r_i),\
m'\in\widehat M_i(\mathcal P',r_i)\,\bigr\}
$$

collect the mechanisms that some admissible repair assigns to $t$'s
recurrence; it is nonempty because restorative active sets are nonempty.

### Definition 7.3 (Retained-record leverage) {#def-leverage}

Under the *subjective recurrence premise*—the agent values a
prospective repair over one anticipated recurrence of its retained record,
token for token—the leverage of inquiry at a dissonant record with
$\mathcal R(\mathcal P_i,r_i)\neq\emptysetset$ is

$$
B_i(r_i)
=
\max_{\psi}\;
\sum_{t\in r_i}\;
\min_{a_{-i}\in A_{-i}}\;
\min_{\theta\in\Theta_i(t)}
\Bigl(
\mathbb E_{x\sim\theta(\psi(t),\,a_{-i})}\!\bigl[u_i(x_i)\bigr]
-
\mathbb E_{x\sim\theta(\sigma_i(t),\,a_{-i})}\!\bigl[u_i(x_i)\bigr]
\Bigr), \tag{6}
$$

the maximum taken over $\Lambda_i(r_i)$-measurable rules $\psi$ from tokens
to own actions, where $\sigma_i(t)$ denotes the action the carried-forward
policy takes at $t$'s awareness cell.  Set $B_i(r_i)=0$ when there is no
dissonance or when $\mathcal R(\mathcal P_i,r_i)=\emptysetset$.

### Proposition 7.4 (Answer invariance and the participation rule) {#prop-participation}

$B_i(r_i)$ is well defined, computable from the deliberative record together
with the known structure $(\Theta,u_i)$, and invariant across the elements
of $\mathcal R(\mathcal P_i,r_i)$: every $\Lambda_i$-measurable rule is
implementable after any successful production, and the maximand of
equation (6) makes no reference to which repair arrives.  Moreover
$B_i(r_i)\geq0$.  Electing inquiry has represented value
$\lambda_iB_i(r_i)-\gamma_i$, so agent $i$ elects if and only if
$\lambda_iB_i(r_i)\geq\gamma_i$; in particular, elections occur only at
dissonant records that admit some repair.  Finally, $B_i(r_i)>0$ if and only
if some pinned rule strictly and robustly improves on the carried-forward
policy: questions whose every admissible answer supports current behavior
are worthless at any positive cost, however much model multiplicity remains.

#### Proof {#proof-prop-participation}

Each $\mathcal P'\in\mathcal R(\mathcal P_i,r_i)$ induces a partition of the
retained tokens, and a $\Lambda_i$-measurable rule is constant on the cells
of every such partition, since each induced partition refines their meet; by
[assumption 3.3](#ass-observation) the rule can therefore be implemented as a
$\mathcal P'$-measurable policy at recurrences, whichever $\mathcal P'$
arrives.  Every object in equation (6) is a function of the record,
$\Theta$, and $u_i$.  The carried-forward policy is itself
$\Lambda_i$-measurable—each induced token partition refines the partition
of tokens by current awareness cells, hence so does their meet—so taking
$\psi=\sigma_i$ shows $B_i\geq0$, and $B_i>0$ exactly when some admissible
rule achieves a strictly positive robust gain.  With probability $\lambda_i$
production succeeds and the pinned gain is secured; the extrapolated
component of any full formulation is assigned no represented value at the
election; on failure or abstention the carried-forward policy continues.
When $B_i=0$—including whenever there is no dissonance or the record is
irreparable ([remark 6.3](#rem-irreparable))—the strict cost $\gamma_i>0$ makes
abstention optimal. ∎

The participation rule is a coherent non-Bayesian criterion operating
precisely where Bayes is undefined, and its variables respect every
discipline of [section 3.5](#sec-commitments): the leverage quantifies over retained
tokens and their recorded outcomes—“situations like the episodes I lost
will recur, and whatever distinction inquiry yields would let me act on
them”—never over candidate representations.  Two comparative properties
follow immediately and organize the applications.  *Action separation,
not information*: the value of a question tracks whether its resolution
could change behavior, not how much residual uncertainty it would resolve;
a maximally uncertain agent whose every admissible repair prescribes its
current actions rationally declines to inquire.  *Rational cessation*:
an agent whose record contains no evidence against its current actions has
$B_i=0$, so sustained success extinguishes inquiry even though awareness
remains incomplete.

### Remark 7.5 (Where exactness and opacity live in the formula) {#rem-transparency}

Two features of equation (6) deserve comment.  First, normalization:
the valuation horizon is one full anticipated recurrence of the retained
record, so $B_i$ grows as evidence accumulates; any fixed-horizon
normalization—per episode, per generation—rescales $B_i$ and $\gamma_i$
together and changes nothing.  Second, the inner minimum over $\Theta_i(t)$
is where *counterfactual transparency* lives.  When consequences
identify forgone values—as in winner-take-all markets, where a lost
episode's record pins the mechanism every repair must assign it—the
minimum is over a singleton and the bound is exact; the laboratory's
leverage of one-half is this case.  When consequences conceal forgone
values, $\Theta_i(t)$ is large, the minimum drags each term toward zero, and
$B_i$ understates the objective value of repair: opaque environments
rationally suppress inquiry.  How much an environment lets agents price
their own questions is itself a dimension of its diagnosticity, alongside
exposure.

### Example 1 (continued) {#example-1-continued-4}

At the dissonant record, both firms' committed constant policies disagree
with exactly one revealed label (firm 1 lost at $s_{11}$, firm 2 at
$s_{00}$).  Every restorative refinement separates the two labeled tokens,
and implementing a token's revealed label at its recurrence gains exactly
one-half against *every* rival action: if the rival plays the winning
architecture, the switch converts a differentiated loss ($0$) into a pooled
half; if the rival switches, it converts a pooled half into a differentiated
win ($1$).  Hence $B_i=\tfrac12$ for both firms—identical leverage from
opposite experiences—and each elects inquiry if and only if
$\lambda_i/2\geq\gamma_i$.  The valuation used no conjecture about the
rival and no reference to which of the four admissible refinements might
arrive.  In the notation of equation (6): the pinned structure
separates the two labeled tokens, every repair's active theory assigns each
its revealed mechanism ($\Theta_i(t)$ is a singleton—the transparency of
winner-take-all payoffs), and the mechanism and rival minima are degenerate,
so the bound is exact.  For rational cessation and its converse, append a validation
generation in which firm 1 has acquired the row refinement (certain of the
true row assignment) while firm 2 has acquired the column refinement
(certain of the false column assignment): their policies differ at the two
off-diagonal states, firm 1 wins both, and the labels revealed there
falsify firm 2's assignment.  Firm 1's record now agrees with its policy
everywhere, so $B_1=0$: the firm holding the truth rationally never
inquires again, and its awareness remains permanently incomplete.  Firm 2's
record disagrees at two tokens, so $B_2=1$: defeat has concentrated the
evidence, the dissonance, and the incentive in the losing firm, which
elects whenever $\lambda_2\geq\gamma_2$ and, upon success, is driven
stepwise to complete awareness.

## 8. The pivot: formulation, warrant, and the return to Bayes {#sec-pivot}

Successful production yields a refinement $\mathcal P_i'$; *formulation*
selects a theory $m'\in\widehat M_i(\mathcal P_i',r_i)$ on the recoded
record; and the agent forms a full-support *bridge prior*
$\mu_i^{+}\in\Delta(M(\mathcal P_i'))$, from which ordinary updating
resumes.  Nothing in Bayesian coherence determines $\mu_i^{+}$ from the
pre-dissonance belief—the domains differ—and this nonuniqueness is not a
defect to be repaired but the boundary between insight and judgment.
Renormalizing $\mu_i^{+}$ on the active set yields what we call
*representation-relative coherence*: the confidence the new language
awards its own theories.  The question of this section is how much of that
confidence the evidence actually licenses.

### Definition 8.1 (Reflective assessment, warrant, and the gap) {#def-warrant}

A reflective assessment problem is a pair $(\mathcal T,\nu)$: a finite set
of candidate objective assignments and a full-support reflective prior.
Given the record and a successful production-and-formulation event, the
*selection-adjusted warrant* $W$ of $(\mathcal P_i',m')$ is the
$\nu$-posterior probability that $m'$ is objectively correct—that
$\tau'(s)=m'(C_{\mathcal P_i'}(s))$ for all $s$—conditional on the record
*and* on the production event.  The *warrant gap* $G$ is the
representation-relative coherence probability of $m'$ minus $W$.

### Theorem 8.2 (The insight is not evidence) {#thm-uninformative}

If the technology is truth-blind, conditioning on the production event adds
nothing to the record: $W$ equals the ordinary reflective posterior of
$m'$'s correctness given the record alone.  Post-restoration fit is
guaranteed by the restoration property, so passing the test carries no
information beyond the record either.  Among candidates in $\mathcal T$ that
induce the same record distribution, prior odds are preserved exactly.

#### Proof {#proof-thm-uninformative}

The reflective posterior on $\tau'\in\mathcal T$ is proportional to
$\nu(\tau')$, times the record's likelihood under $\tau'$, times the
probability of the production event given the record; truth blindness makes
the last factor a function of the record alone, constant across
$\mathcal T$, so it cancels.  Fit is a deterministic function of record and
output ([definition 6.1](#def-restorative)), hence has likelihood one in every world
consistent with the event.  The last claim applies the cancellation to
candidates with identical record likelihoods. ∎

The theorem locates the evidential boundary: everything evidential is in
the record; nothing evidential is in the arrival of the insight or in its
retrospective success at organizing the experience that produced it.  The
practical force is a prohibition on double counting.  The same experience
that directed representation production cannot also confirm the resulting
theory, because any restorative output fits it by construction.  Truth
blindness is the polar case; were production correlated with the objective
assignment—social transmission from an informed source—the arrival would
itself be evidence, and the adjustment could move confidence in either
direction.

### Corollary 8.3 (Self-audit requires sufficiency for the candidates) {#cor-self-audit}

The assessment $(\mathcal T,\nu)$ is expressible by agent $i$ only if
$\mathcal P_i$ is sufficient for every $\tau'\in\mathcal T$, hence only if
$\mathcal P_i$ refines the join of [proposition 6.6](#prop-robust-sufficiency).  An agent
holding a minimal restoration therefore generally cannot formulate the
comparison that measures its own warrant gap: the overconfidence is
invisible from within the representation that produces it.  Short of that
refinement, warrant must be supplied externally—by fresh evidence whose
likelihoods differ across candidates, by an assessor with broader awareness,
or by a future self.

#### Proof {#proof-cor-self-audit}

Entertaining $\tau'$ as a hypothesis requires expressing it, which is
sufficiency ([definition 3.2](#def-awareness)); sufficiency for every candidate is
refinement of the join. ∎

The pivot is now complete, and it is the paper's fulcrum.  Dissonance broke
the agent's Bayesian competence; inquiry produced a distinction; formulation
and the bridge prior rebuilt a probability space; and judgment—fresh
evidence with differential likelihoods, honestly accounted—resumes as
ordinary updating on the expanded language.  The agent has returned to the
Bayesian world carrying a warrant gap of known location and, by
[corollary 8.3](#cor-self-audit), generally unknowable (to it) size.

### Example 1 (continued) {#example-1-continued-5}

Suppose firm $i$'s technology produces the column refinement.  The recoded
record pins the unique consistent theory: architecture $0$ on the first
column, $1$ on the second.  Representation-relative coherence assigns it
probability one.  Now conduct the reflective assessment with
$\mathcal T=\{\text{row world},\text{column world}\}$ and a symmetric prior.
The two worlds generate identical records
([theorem 6.5](#thm-nonidentification)), and the technology is truth-blind, so by
[theorem 8.2](#thm-uninformative) the reflective posterior equals the prior:
$W=\tfrac12$, and the warrant gap is exactly one-half.  The same gap
afflicts the firm that acquires the *row* refinement: its coherence in
the true assignment is also probability one, and its warrant is also
one-half.  Unwarranted certainty is not a symptom of error—early
confidence outruns the evidence even when it happens to be right, and what
separates the two firms is the objective law, which neither observes.  By
[corollary 8.3](#cor-self-audit), neither firm can conduct this assessment itself:
expressing both candidate worlds requires the full partition into
singletons.  One fresh differentiated observation at an off-diagonal state
closes the gap completely—the two worlds predict opposite labels
there—while pooled observations, in any number, close nothing.  Warrant,
like leverage, is purchased with differentiated action.

## 9. Strategic dynamics: when everyone lives in a Bayesian world {#sec-dynamics}

The chain now runs inside a population.  Theories determine committed
policies; policies determine which conditionals are visited; visited
conditionals determine dissonance and leverage; and refinements feed back
into theories.  This section characterizes where the process comes to rest.
The object of interest is not a strategic equilibrium but an epistemic
condition: a configuration of the population in which *every agent
permanently inhabits a Bayesian world*—models fit, questions are dead, and
no represented calculation prices further inquiry above its cost.

### Definition 9.1 (Self-confirming unawareness equilibrium) {#def-scue}

A profile of epistemic states
$\xi_i=(\mathcal P_i,r_i,\bar\mu_i,q_i,\sigma_i)$, $i\in N$—awareness,
retained record, reference posterior, conjecture, and committed policy, with
acting beliefs $\mu_i$ derived by judged updating—is a
*self-confirming unawareness equilibrium* (SCUE) if, under the play it
induces,

- (i) each $\sigma_i$ is subjectively optimal
  (equation (3));
- (ii) each conjecture $q_i$ agrees with the play induced by $\sigma_{-i}$
  at every on-path cell;
- (iii) no dissonance occurs: each agent's active set, computed from its
  record as play accumulates, is almost surely eventually nonempty, and each
  acting belief $\mu_i$ is supported on $\eta$-adequate theories; and
- (iv) no agent elects inquiry: $\lambda_iB_i(r_i)<\gamma_i$ along the
  induced records, which holds in particular whenever $B_i=0$.

The record belongs in the state: dissonance status and leverage are
functions of retained evidence, so two histories with identical partitions,
beliefs, and policies but different records can differ in equilibrium
status.

Conditions (i)–(ii) are subjective rationality with confirmed conjectures:
the self-confirming conditions of the fixed-language tradition
(Fudenberg and Levine 1993; Kalai and Lehrer 1993).  Conditions (iii)–(iv) are the
new, epistemic ones: the language survives its own evidence, and the
question has no priced value.  A SCUE in which every partition is sufficient
for $\tau$ and beliefs concentrate near the truth is simply a
self-confirming equilibrium; the concept's interest lies entirely in the
other cases.

### Remark 9.2 (The grain of truth, restored endogenously) {#rem-grain}

Rational-learning convergence requires a grain of truth: the environment
absolutely continuous with respect to beliefs (Kalai and Lehrer 1993).
Under unawareness the condition can fail at the level of language—the
truth may be inexpressible—and statistical dissonance is precisely the
detector of that failure.  Each successful refinement restores the grain
*on the path of play*: post-restoration, some expressible theory
matches the visited conditionals within tolerance.  A SCUE is a
configuration in which the grain of truth holds on-path for every agent and
no one has a priced reason to look for the off-path remainder.

### Assumption 9.3 (Regularity) {#ass-regularity}

(i) *Generic tolerance.*  The tolerance $\eta$ lies outside the finite
set of critical values at which, for some agent, theory, partition profile,
and policy profile, the total-variation distance between an induced on-path
conditional and the theory's prediction equals $\eta$.
(ii) *Production randomness.*  The randomization in each $\phi_i$ is
independent across elections and of the state and consequence draws, and,
conditional on any election—which by [proposition 7.4](#prop-participation) occurs only
at dissonant records admitting a repair,
$\mathcal R(\mathcal P_i,r_i)\neq\emptysetset$—production succeeds with
probability at least $\underline\pi>0$.

Part (i) excludes finitely many tolerance values, since agents, theories,
partitions, and policies are all finite.  Part (ii) is substantive: it rules
out technologies that can be elected forever without ever producing
([remark 9.6](#rem-scope)).

### Theorem 9.4 (Epistemic absorption) {#thm-absorption}

Under [assumption 9.3](#ass-regularity), almost surely:

- (a) at most $n(|S|-1)$ refinements occur, and every agent's awareness
  partition is eventually constant;
- (b) only finitely many inquiry elections occur; and
- (c) there is an almost surely finite generation after which no agent's
  language changes and no agent pays an inquiry cost: every agent's
  epistemic life thereafter is judged-Bayesian updating within a fixed
  language, punctuated at most by dissonance episodes that fail the
  participation threshold.

Moreover, on the event that the committed profile is eventually constant,

- (d) every agent's active set is eventually constant, every theory it
  contains is $\eta$-adequate under the terminal play at every recurrent
  observation pair, and each agent is eventually either never
  dissonant—it lives in a Bayesian world—or in *dissonant stasis*:
  dissonance recurs while $\lambda_iB_i<\gamma_i$, in particular whenever
  $B_i=0$, as at irreparable records
  ($\mathcal R(\mathcal P_i,r_i)=\emptysetset$).

The proof is in [appendix A](../appendix/appendix.md#app-absorption).

### Proposition 9.5 (Rest points and persistence) {#prop-rest-points}

- (i) If awareness partitions, committed policies, conjectures, and acting
  beliefs are all eventually constant almost surely, then the limiting
  configuration, restricted to the agents not in dissonant stasis, is a
  self-confirming unawareness equilibrium.
- (ii) Conversely, consider a configuration whose epistemic states satisfy
  the SCUE conditions, whose play generates only records with $B_i=0$, and
  in which each agent's committed action at each cell is strictly optimal
  under every conjecture and every theory in its active set.

- (a) With deterministic mechanisms, the configuration persists:
    dissonance, elections, and policy changes never occur, and the SCUE
    conditions continue to hold, with conjectures converging empirically to
    induced play.
- (b) With stochastic mechanisms, suppose in addition that every theory
    in every active set is $\eta'$-adequate under the configuration's play
    for some $\eta'<\eta$, and that the strict optimality extends to every
    $(\eta+\varepsilon)$-adequate theory for some
    $\varepsilon\in(0,\,2(\eta-\eta')]$.  Then for every $\delta>0$ there is
    a count threshold $N(\delta)$ such that, if the configuration is reached
    with at least $N(\delta)$ observations at every recurrent pair, then
    with probability at least $1-\delta$ play never changes, dissonance and
    elections never occur, and the SCUE conditions hold in every subsequent
    generation, with conjectures converging empirically to induced play.

The proof is in [appendix A](../appendix/appendix.md#app-absorption).

### Remark 9.6 (What the theorem does and does not claim) {#rem-scope}

[Theorem 9.4](#thm-absorption) is a statement about the epistemic process—the death
of inquiry—not about the convergence of play.  Within a Bayesian world,
committed policies may in principle continue to cycle as beliefs and
conjectures chase one another; that is the classical convergence problem of
learning in games (Fudenberg and Levine 1993; Kalai and Lehrer 1993), it is
orthogonal to this paper's contribution, and the theorem deliberately does
not resolve it.  Part (d) and the rest-point characterization are
accordingly conditional on play stabilizing, which in every configuration
featured in this paper is immediate: their beliefs make one action per cell
strictly dominant.  Separately, if the success bound in
[assumption 9.3](#ass-regularity)(ii) is dropped, one further absorbing pattern becomes
possible: perpetually elected, perpetually failing inquiry—a question
worth asking that is never answered, whose economics (paying $\gamma_i$
forever for a repair that never arrives) merit separate study.

### Remark 9.7 (Rational anomaly tolerance) {#rem-anomaly}

Zero-leverage dissonant stasis is a recognizable condition, not a
pathology of the model: the agent knows its causal account is
broken—every expressible theory is rejected—yet the break disturbs no
represented action comparison, so repairing it is worth nothing.  Standing
anomalies tolerated by working scientists and managers have exactly this
structure, and the model locates them: anomaly tolerance is rational
precisely when pinned distinctions carry no robust action leverage.  A
sharper instance is the irreparable record ([remark 6.3](#rem-irreparable)): there
$\mathcal R=\emptysetset$, no expressible repair exists at any price, and
the anomaly is not merely unprofitable to fix but impossible to fix within
the current grammar.

### Proposition 9.8 (On-path adequacy, and where error lives) {#prop-adequacy}

In a SCUE, every theory in the support of every $\mu_i$ is $\eta$-adequate
at every visited pair.  All surviving falsity is confined to what the
configuration does not expose: mechanism assignments at states pooled with
causally different states whose mixture imitates a single mechanism at the
visited profiles, and counterfactual claims at unvisited profiles.

#### Proof {#proof-prop-adequacy}

Immediate from [definition 9.1](#def-scue)(iii) and [lemma 5.2](#lem-test-consistency); the
residual clause is the complement of the visited pairs' constraints. ∎

### Proposition 9.9 (Persistent performance differences) {#prop-persistence}

There exist primitives and absorbing configurations in which agents hold
different terminal partitions and theories, expected per-generation payoffs
differ strictly and permanently, and no disadvantaged agent has a priced
repair: for each such agent either $B_i=0$ or $\lambda_iB_i<\gamma_i$.

The proof is by the instances below, and the mechanism deserves emphasis.
Performance differences persist not because an equilibrium concept freezes
them but because the process that would erase them has died economically:
the disadvantaged configuration generates no dissonance, or generates no
leverage, or prices its question below the cost of asking.  Terminal
heterogeneity in awareness is path dependence in the strong sense—agents
with identical preferences and identical Bayesian competence, facing the
same objective system, end at different languages and different payoffs
because their histories posed different questions.

### Definition 9.10 (Diagnostic environments) {#def-diagnostic}

The primitives $(\Theta,\tau,\rho,u)$ are *diagnostic* if, under every
profile sustainable in a SCUE, every expressible theory that is
payoff-relevantly false—false at some state where the truth would change
its holder's optimal action—is $\eta$-inadequate.

### Proposition 9.11 (No payoff-relevant error in diagnostic environments) {#prop-diagnostic}

In a diagnostic environment, every SCUE is free of payoff-relevant error.
Payoff-relevant falsity survives only in environments that admit concealing
profiles, and it requires them to be sustained: collective error needs the
absence of *both* corrective forces, strategic variety inside agents'
categories and environmental punishment of uniform misservice.

#### Proof {#proof-prop-diagnostic}

By [definition 9.1](#def-scue)(iii), theories surviving in a SCUE are not
$\eta$-inadequate; in a diagnostic environment every payoff-relevantly false
theory is.  The second claim restates [definition 5.4](#def-exposure): a false theory
survives only under concealing profiles, and [proposition 5.5](#prop-exposure) makes
concealment necessary as well as sufficient. ∎

### Example 1 (continued) {#example-1-continued-6}

Set $\beta=1$ and suppose both firms acquired the column refinement after
the discovery generation and became certain of the false column assignment.
Each then plays the column policy; the firms pool at every state; every
payoff is one-half; and one-half is exactly what the column theory predicts
under pooled play.  The configuration is a SCUE with payoff-relevant error:
policies are subjectively optimal, conjectures confirmed, no dissonance ever
occurs (the profile is concealing), and $B_i=0$ for both firms—so the
configuration survives even a free, infallible inquiry technology.  The
warrant gap of [section 8](#sec-pivot) is permanent: unbounded experience
accumulates while each firm remains exactly half-warranted, the missing half
being the reflective weight on the world their shared language cannot
express.  Now let $\beta<1$.  In the first generation containing an
off-diagonal state, the pooled firms receive $\beta/2$ where their theory
predicts one-half: the demand side reveals the label, dissonance returns,
leverage turns positive, and the reflective posterior becomes degenerate.
Payoff-relevant self-confirmation is a knife-edge property of perfectly
forgiving demand—the $\beta<1$ environments are diagnostic—and the
destroyed value $1-\beta$ at each misserved episode is itself the corrective
signal: what demand withholds from the firms, their epistemics receives as
evidence.  Finally, persistence: with $\beta=1$, let firm 1 hold the row
refinement and the true assignment while firm 2 remains coarse with
$\gamma_2>\lambda_2B_2$.  Firm 1 wins both off-diagonal states and splits
the rest, earning three-quarters to firm 2's one-quarter, forever; firm 2
sits in dissonant stasis, its question priced below its cost.  Every route
out—strategic variety, demand harshness, cheaper inquiry—is exactly one
of the model's named forces.

## 10. Discussion {#sec-discussion}

### 10.1 Implications for the theory-based view {#implications-for-the-theory-based-view}

The model supplies the theory-based view with the object its formal
treatments presuppose and, in doing so, changes what several of the view's
claims mean.

*Strategic variety has a pre-probabilistic source.*  In the model,
agents with identical preferences, identical Bayesian competence, and
identical objective opportunities diverge because their experiences posed
different questions, their technologies produced different repairs, and
their positions extinguished inquiry at different points.  Heterogeneous
prior understanding generates heterogeneous questions; questions generate
heterogeneous languages; languages generate heterogeneous theories, plans,
and payoffs.  This sequence begins before probability does, and it is
path-dependent in the strong sense: the order of experiences shapes the
terminal language, and agents can converge to the same behavior while
retaining permanently different representations
([proposition 9.9](#prop-persistence)).

*The value of experimentation is not information.*  A question is
worth asking when some admissible answer would change action
([proposition 7.4](#prop-participation)), not when its resolution would be most
informative.  This reframes theory testing: high-entropy uncertainty with no
action leverage is rationally ignored, and narrow contrasts that straddle an
action threshold are rationally pursued.  It also explains rational
cessation—why successful firms stop asking—and the loser's advantage in
inquiry: competitive defeat concentrates the evidence, the dissonance, and
the incentive in the defeated firm.

*Early confidence outruns evidence even when correct.*  The warrant
results discipline a claim at the center of the empirical program on
scientific entrepreneurship (Camuffo et al. 2020; Zellweger and Zenger 2023).  A
founder's theory that beautifully organizes the experiences that generated
it has, by [theorem 8.2](#thm-uninformative), earned nothing by that organization:
the fit was guaranteed by construction.  Validation requires evidence whose
likelihood differs across the candidate worlds—and, by
[corollary 8.3](#cor-self-audit), the founder typically cannot even express the
comparison, which is a formal argument for outside challenge (boards,
investors, advisors with different awareness) as a warrant technology rather
than a monitoring technology.

*Markets discipline theories through two channels, and their absence
is predictable.*  Payoff-relevant collective error requires both concealment
by play and forgiveness by demand ([proposition 9.11](#prop-diagnostic)).  Industries
where customers absorb misservice—captive buyers, no substitutes, third
parties bearing the cost—can sustain shared false theories indefinitely;
industries with strong outside options discipline theories even under
consensus.  Where demand is forgiving, the only corrective is strategic
variety in beliefs, which gives belief heterogeneity a social value distinct
from its private value: the entrant with a deviant theory is the industry's
epistemic infrastructure.

*Anomaly tolerance is an equilibrium phenomenon.*  Firms that know
their causal account is broken and rationally decline to fix it
([remark 9.7](#rem-anomaly)) are not failing at learning; their standing anomalies
carry no action leverage.  The model predicts where tolerated anomalies
accumulate: in transparent-consequence environments, near decisions whose
robust optimum is insensitive to the unresolved structure.

### 10.2 The cognitional interpretation {#the-cognitional-interpretation}

The model's architecture tracks a classical account of inquiry
(Lonergan 1992; Ryall and Wilkins 2018), and the correspondence is
disciplining rather than decorative: it dictates which formal objects must
not be conflated.  Experience is the flow of episodes; the question for
intelligence is dissonance, which localizes a defect without naming its
repair; heuristic anticipation is restoration, minimality, and the
complexity ordering, which constrain an answer without supplying its
content; insight's formal footprint is the refinement; formulation is the
mechanism assignment on the new cells; reflective judgment is the
consistency test together with the warrant accounting, faculties formally
distinct from the posterior ([remark 4.2](#rem-self-sealing)); and decision is the
committed policy, which then determines what experience will teach next.
The election $\varepsilon_i$ adds the economic layer: an unrestricted desire
to know, prosecuted under restricted resources.  Nothing in the mathematics
represents the conscious act of insight itself; the model represents its
products and its price, which is what an economic theory can responsibly
claim.

### 10.3 Limitations and the research program {#limitations-and-the-research-program}

Four boundaries of the present model define the program's next steps.
First, the mechanism vocabulary $\Theta$ is fixed: agents lack distinctions,
never concepts of consequence-generation.  Expanding the vocabulary
itself—deeper unawareness—is the natural second paper in the sequence,
and the awareness-transition machinery here is built to receive it.  Second,
the model prices participation in inquiry but not its intensity or
duration, and the technology's success is exogenous; endogenizing the depth
of inquiry connects to models of costly deliberation and planning
(Ryall 2026), where cached prior conclusions govern when
reconsideration is rational—the theory-to-plan transition.  Third, agents
are individuals; the theory-bearing *firm*—how insights become shared
languages, collective intentions, and organizational commitments—is a
separate paper resting on the same primitives (Ryall and Wilkins 2018).
Fourth, the competitive consequences here run through payoffs in a fixed
game; joining the front end developed here to the cooperative back end of
value capture (Gans and Ryall 2017; Bryan et al. 2022), where awareness
itself earns rents and disclosure is strategic, completes the arc.  Within
the present model, the flagged analytical items are general conditions for
the convergence of play within Bayesian worlds ([remark 9.6](#rem-scope)),
equilibrium in the anti-coordination region that value destruction creates,
counterfactual transparency as a design variable, and Markov state
processes.

## 11. Conclusion {#sec-conclusion}

This paper models the step the theory-based view has described but not
formalized: the origin of a strategic theory.  The model draws a formal
boundary between learning within a causal language and producing a new one,
and it prices the crossing.  Bayesian updating cannot expand the language
and cannot even detect that expansion is needed; detection is statistical
dissonance, a faculty distinct from the posterior.  Dissonance directs
repair without determining it; observational equivalence makes any
economical inquiry technology fallible; and the value of a question is
computable, invariantly across its inconceivable answers, at exactly the
moment the posterior is undefined.  The return to Bayesian life is
disciplined by a warrant account whose central theorem is easily stated: the
insight is not evidence.  And because theories cause the actions that cause
the evidence, inquiry is almost surely absorbed: eventually everyone lives
in a Bayesian world—in configurations that preserve false theories,
heterogeneous languages, and permanent performance differences exactly when
neither strategic variety nor environmental harshness disturbs them.
Strategy's oldest question—why do similar firms perform differently?—here
receives an answer that begins before beliefs: because they came to
different questions, and some questions died before they were asked.

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
