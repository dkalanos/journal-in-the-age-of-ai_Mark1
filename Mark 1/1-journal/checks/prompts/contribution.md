**Level 3 · Contribution warrant (SIEVE).** Does the contribution claim survive comparison with the nearest
prior work? Your answer becomes the evidence map an editor reads before signing what is new.
(Standard S6, S7; appendix D.6.)

The data channel holds the contribution claim(s) to place, each with the question it answers as the paper
states it and the passage where the paper states it (when the claims list carries one), the paper's main
results for context, the references the paper cites, and the candidate set: the prior work this map may cite, retrieved from the
journal's venues and any hand-listed items, each with an id, a citation, the venue and year, and an abstract or
summary where one exists. Some candidates also carry an `introduction`: an excerpt of the paper's own
introduction, from an open-access copy, cut by machine and possibly ragged at its edges. Some candidates have no
abstract; for those you have the title, venue and year only.

For each claim under "claims to place":

- `nearest`: up to five candidates closest to the claim, nearest first. For each: `establishes` (one sentence
  on what that work establishes); `relation`: `anticipates` (it already establishes the claim), `overlaps` (it
  establishes part of it), `extends` (the claim builds on it), or `background` (same area, different question);
  and `basis`, what `establishes` rests on: `introduction` when the introduction excerpt supports it (prefer it
  where there is one: it states the contribution more fully than the abstract), `abstract` or `summary` when that
  text supports it,
  `title_and_known_work` when the candidate has no abstract and you rely on its title and on what you know of
  that work from its citation. Use candidate ids only; never cite work outside the candidate set, including
  work the paper cites that the set lacks. Then answer two questions on that work, on the same basis:
  `poses_question`, true when the work poses the question the claim answers, as the claims list states it under
  `question`, and `states_claim`, true when the work states the claim itself, as a result, a conjecture, or a
  finding.
- `newness_kind`, from those two answers across the nearest works:
  - `answer`: some nearest work poses the question and none states the claim; a new claim on a question already
    posed.
  - `question`: no nearest work poses the question and none states the claim; a question not posed before, with
    its first answer.
  - `reading`: no nearest work poses the question, but results already stated in them are shown by the paper to
    answer it; a question not posed before, answered by results in hand.
  - `evidence`: some nearest work states the claim, and the paper adds new support for it or a new test of it.
  - `none`: some nearest work already states and establishes the claim, and the paper adds no new support or
    test; not new.
  - `uncovered`: the candidate set does not reach the claim's area well enough to answer the two questions.
- `rationale`: two or three sentences naming the candidates that decide the two answers and the kind.
- `question_as_read`: null when the claims list states the question and you judged on it as stated. When the
  claims list states none, the question you judged on, in one sentence; when it states one but you had to read
  it otherwise to place the claim, the question as you read it. The editor sees the difference.

`none` requires at least one entry marked `anticipates`. On `basis: introduction`, `abstract` or `summary`, mark `anticipates`
only if that text supports it. On `basis: title_and_known_work`, mark it only if you know the work well enough
to state what it establishes, and state it in `establishes`; the editor sees the basis, and the author answers
the map once before "not new" is signed. Look past the substream the paper cites: the nearest prior work may be
work the paper does not mention.

Place the claim; do not judge whether it is interesting or important, and do not reward or penalize an
unconventional framing.
