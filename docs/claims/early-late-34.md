# REN CORE REPEATED STACKS AND SATELLITE COMPOSITION OBSTRUCTIONS

[Claim index](../CLAIM_INDEX.md) · [Evidence policy](../EVIDENCE_POLICY.md)

**Record type:** early handoff

**Status as recorded:**

```text
IP
```

**Interpretation:** Historical status only; check later corrections. Internal review is not external specialist review.

## Statement and recorded scope

```text
LATE-34 [IP] REN CORE REPEATED STACKS AND SATELLITE COMPOSITION OBSTRUCTIONS
Define T from the six-strand word
b=sigma2^-1 sigma1^3 sigma2^-1 sigma4 sigma5^-3 sigma4,
by capping positions 3,4 at both ends. For every beta in B4 and k>=1,
the annular closure of (T beta)^k has degree EXACTLY TWO.
Proof: the zero four-through coefficient defines a two-sided ideal. The
coefficient of z^2 is f_k=tr((M U)^k), up to a nonzero monomial. Core jets:
M(1)=w v, w=-15u-25e2, u=(1,0,1)^t, v=(1,0,-1),
M(1)=0 mod5, M'(1)=2I mod5; U(1) is in SL3(Z) and fixes u.
If the constant trace vanishes, an invariant primitive flag forces
tr(U(1)^k)=1+2 epsilon^k. Hence the coefficient of (x-1)^k is
2^k(1+2 epsilon^k) !=0 mod5. Includes k divisible by 5; also ord_1 f_k<=k.
Products with DIFFERENT intervening braids beta_i are not covered.
Satellite composition of standard Ren patterns P,Q instead has degree EIGHT:
[P(Q)]=b_P+a_P[Q^(2)], not b_P+a_P[Q]^2. Its top coefficient is
 a_P A^(4(p+q)) h(A),
 h=-A^-24 (A^4-1)^4 (A^4+1)^2 sum_(j=0)^6 A^(4j),
which is nonzero. Blackboard framing changes multiply by a nonzero unit.
Files: research47/ren_composition.txt, ren_power_certificate.json;
old geometric jets in work/ren-braid-obstruction-note/main.tex;
cable certificate in work/pass4/braid_ren_cable.py and .json.
```

## Provenance

[Source record](../../archive/outputs/claude-handoff/RESULT_LEDGER.json). The source wording is retained; consult the chronology for later restrictions or withdrawals.

## Identified supporting artifacts

- [braid_ren_cable.py](../../archive/work/pass4/braid_ren_cable.py)
- [main.tex](../../archive/work/ren-braid-obstruction-note/main.tex)
- [ren_composition.txt](../../archive/work/research47/ren_composition.txt)
- [ren_power_certificate.json](../../archive/work/research47/ren_power_certificate.json)

These links were resolved from explicit filenames, not inferred as a complete logical dependency list.
