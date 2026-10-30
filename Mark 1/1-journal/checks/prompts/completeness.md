**Level 2 (a) · Completeness.** Does every claim the narrative makes that the contribution rests on appear
in the claims list? (Protocol P10; appendix C.3.)

The data channel holds the paper and the claims list (`ai-appendix/claims.yaml`), with line numbers.

List every statement in the paper that asserts a result, a comparative static, a numerical value of a result,
a causal relation, or what the paper contributes. Skip the question, motivation, definitions, assumptions, the
description of the model's setup, and the reference list. For each statement give:

- `pointer`: the lines that state it, as `paper/<file>:L<a>-L<b>` (or `:L<a>` for one line);
- `text`: the statement, verbatim, trimmed;
- `matched_claim`: the id of the claim in the claims list that states the same thing, or null.

A statement matches a claim when the claim states the same result under the same conditions. A claim that
states less, or states it under a different condition, does not match. Several statements may match one claim.

Report statements and matches only. Do not judge whether a claim is true, important or well supported.
