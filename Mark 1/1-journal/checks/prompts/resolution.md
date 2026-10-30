**Level 2 (b) · Resolution.** Does each claim's evidence say what the claim says? (Protocol P10.)

For each claim in the data channel you get the claim, the passage of the paper that states it, and the
passage of the record its evidence pointer resolves to, all with line numbers.

For each claim give `resolves`:

- `full` if the evidence states or derives exactly what the claim states, under the claim's conditions;
- `partial` if the evidence supports only part of the claim, or supports it under different conditions;
- `none` if the evidence does not support the claim.

Give the `reason` in one sentence. For `partial` and `none`, name what the evidence lacks.

A contribution claim may also carry the question it answers and the passage of the paper where that question is
stated. For such a claim, `resolves` is at most `partial` when that passage does not pose the question as the
claim states it; say so in the reason.

Judge correspondence only: whether the evidence says what the claim says. Whether a derivation is correct, and
whether the claim is new or important, are other checks.
