# 1-journal/corpus/ · what the evidence map is allowed to see

The corpus is the journal's own object, published in advance (appendix C.6: "the corpus is the journal's"). It has
two parts, and the map states its coverage as exactly what was searched, never as "the literature".

## The venues: `venues.yaml`

The journal lists on which the map searches, each journal with its ISSNs and the lists it belongs to:
UT Dallas 24, Financial Times 50, and the Chartered ABS Academic Journal Guide grades 4* and 4. `search` says
which lists are switched on; `hand_list` says whether the hand list below is also shown. `mark1 corpus`
resolves every ISSN to an OpenAlex source once and caches it in `sources.json`; journals that do not resolve
are named in every coverage statement.

For each paper, SIEVE's contribution module (`machine/retrieval.py`) searches those venues through OpenAlex:

1. Keyword queries built from each contribution claim and the paper's title: the claim whole, the words the
   claim shares with the title, and those again against titles only, where a short old note can still win.
2. The works most cited among the hits, and among what the paper itself cites, kept when they are in the
   venues. This is the step that reaches older antecedents, which often have no abstract in OpenAlex and rank
   low on keyword relevance.

Up to 60 candidates, with the queries and what found each one, are kept in the run's `sieve/candidates.json`,
so a miss can be traced and the run replays offline. Candidates without an abstract are shown to the model by
title, venue and year only; a placement that rests on one carries `basis: title_and_known_work` and the editor
sees it. Membership of the three lists was compiled from public sources on the dates in the file and needs a
coauthor's check before use on a real paper.

## The hand list: `corpus.yaml`

A hand-named list of papers, enriched from OpenAlex into `openalex/<id>.json` (title, authors, year, venue,
abstract, topics). It is what the Stage-1 demonstration ran on before the venues existed, and it remains useful
for work the venues do not reach: a journal can name a book or a working paper here. Where OpenAlex has no
abstract, the `summary` written in `corpus.yaml` is shown instead; those summaries were written by Claude Code
for the demonstration and need a coauthor's check.

The enrichment also checks the list: a wrong DOI comes back as a different paper. One did, during the build,
and was corrected.

## OpenAlex access

OpenAlex gives every network a small free daily budget, shared by everyone behind the same address, and a
free key with its own budget to anyone who registers an email. Set `MARK1_OPENALEX_KEY` to use a key, or
`MARK1_OPENALEX_MAILTO` for the polite pool. Nothing in Mark 1 sends an address on its own.
