# Quantum braid Floer quotient adds no mixed polynomial data

[Claim index](../CLAIM_INDEX.md) · [Evidence policy](../EVIDENCE_POLICY.md)

**Record type:** early handoff

**Status as recorded:**

```text
D/N/C
```

**Interpretation:** Historical status only; check later corrections. Internal review is not external specialist review.

## Statement and recorded scope

```text
MID-21  D/N/C  Quantum braid Floer quotient adds no mixed polynomial data
------------------------------------------------------------------------
For S=Z[x^±1], R=S[d^±1], the quotient R/((d-1)(xd+1)) injects into
S x S by the two specializations, with image {(A,J): A-J divisible by x+1}.
It is exactly the Alexander/Jones pair, not an extra independent invariant.
Constructive inverse representative: F=A+x(d-1)(A-J)/(x+1).
The unknot braid sigma1 has Omega^q=xd^2-xd+d and therefore qHFB rank>=3;
other unknot representatives give lower bounds5,9. Jones1 does not force
rank1 for every presentation. Defining bq(K) as minimum rank over all braid
presentations yields HFK-rank<=bq(K); an unproved whole-fiber bound would
combine with HFK connected sums/genus detection to prove Jones detection.
No qHFB connected-sum formula or Markov invariance is assumed.
Proof/source-scope audit: work/research23/quantum_floer_bridge_audit.txt,
quantum_floer_route.txt; verify_quantum_floer_polynomials.py.

------------------------------------------------------------------------
```

## Provenance

[Source record](../../archive/outputs/claude-handoff/RESULT_LEDGER.json). The source wording is retained; consult the chronology for later restrictions or withdrawals.

## Identified supporting artifacts

- [quantum_floer_bridge_audit.txt](../../archive/work/research23/quantum_floer_bridge_audit.txt)

These links identify recorded evidence; they are not a claim that the logical dependency list is complete.
