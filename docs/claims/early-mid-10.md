# Exact no-cancellation restrictions for anchored quotient circuits

[Claim index](../CLAIM_INDEX.md) · [Evidence policy](../EVIDENCE_POLICY.md)

**Record type:** early handoff

**Status as recorded:**

```text
D/N
```

**Interpretation:** Historical status only; check later corrections. Internal review is not external specialist review.

## Statement and recorded scope

```text
MID-10  D/N  Exact no-cancellation restrictions for anchored quotient circuits
------------------------------------------------------------------------
For normalized preferred quotients T=1+xv, v=e-delta, v^2=-delta v,
horizontal equivariant connected sum obeys x12=x1+x2-delta*x1*x2 and
y12=y1*y2, y=1-delta*x. Actual longitude determinant zero implies
y in 1+(A^4+1)^2 Z[A,A^-1]. Its only Laurent unit is 1. Hence any finite
equivariant connected sum is flat iff every summand was flat.
Duplicating an input into shells gives
x_out=[1-product_i(1-delta*d_i*x)]/delta;
its nonzero highest-degree term prevents treating this as a linear shell.
Fixed-width serial invertible operations preserve full rank.
An integral affine controller sum_i a_i diag(1,u_i*d0), with sum a_i=1
and Laurent units u_i, cannot cancel d0!=0: reduction mod (2,A-1) gives
1=0. Rational divisions such as 1/2 are not supplied by ordinary skein moves.
The first overlapping TL3 two-gate cup/cap circuit has exact knot formula
V=1+(1-delta^2)ab, so at least one input must already be flat to get V=1.
For the standard flipping inversion on K#K^r, x=(1-H3(K))/delta and y=H3(K).
The global decomposition of all strongly invertible composites via Sakuma was
NOT fully primary-source checked in this period; do not promote this local
block calculation into that unverified classification claim.
Proof: work/cancellation19/algebra.txt (sections1--8).

------------------------------------------------------------------------
```

## Provenance

[Source record](../../archive/outputs/claude-handoff/RESULT_LEDGER.json). The source wording is retained; consult the chronology for later restrictions or withdrawals.

## Identified supporting artifacts

- [algebra.txt](../../archive/work/cancellation19/algebra.txt)

These links were resolved from explicit filenames, not inferred as a complete logical dependency list.
