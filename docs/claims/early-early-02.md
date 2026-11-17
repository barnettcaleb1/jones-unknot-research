# Exact anchored-twist dichotomy and failed propagation

[Claim index](../CLAIM_INDEX.md) · [Evidence policy](../EVIDENCE_POLICY.md)

**Record type:** early handoff

**Status as recorded:**

```text
INTERNAL-PROOF, elementary skein deduction; novelty not claimed.
```

**Interpretation:** Historical status only; check later corrections. Internal review is not external specialist review.

## Statement and recorded scope

```text
EARLY-02 — Exact anchored-twist dichotomy and failed propagation
Status: INTERNAL-PROOF, elementary skein deduction; novelty not claimed.
For an antiparallel full-twist family with fixed oriented smoothing H,
 V_(m+1)=x^4 V_m+px^2H.
If V_0=1, D=px^2(H+x+x^(-1)) and
 V_m=1+D*(x^(4m)-1)/(x^4-1), for all integer m.
Either H=-(x+x^(-1)) and every V_m=1, or only m=0 has V=1 and degree is
unbounded. Thus uniform compression at a Jones-one anchor is equivalent
to the missing smoothing assertion, not a consequence of that anchor.
An ACTUAL unknot host obtained by switching the trefoil unknotting crossing
has H=-x-x^5 and deg_p V_m=4m+3 for m>=1. It refutes an unrestricted
anchor-only repair; its diagram is nonminimal, so a newly restricted
minimal-diagram theorem is not disproved but remains unproved.
The order-two coefficient c2=a2+b2=-3 Conway_a2. In this example c2=-3m;
on an odd residual crossing cube c2(epsilon)=-(3/2)(sum epsilon_i+1).
It vanishes on the entire anchor layer but not the cube. For interlacing
crossings the mixed difference of c2 is -3, so four Jones-one face vertices
are impossible; the trefoil shadow has three actual-U vertices and one
trefoil. The endpoint contradiction is valid, propagation to it is absent.
Proof/check: work/anchor_twist_attack.md, work/anchor_twist_attack.py.
```

## Provenance

[Source record](../../archive/outputs/claude-handoff/RESULT_LEDGER.json). The source wording is retained; consult the chronology for later restrictions or withdrawals.

## Identified supporting artifacts

- [anchor_twist_attack.md](../../archive/work/anchor_twist_attack.md)
- [anchor_twist_attack.py](../../archive/work/anchor_twist_attack.py)

These links were resolved from explicit filenames, not inferred as a complete logical dependency list.
