# Exact Whitehead factor and actual deep-jet u=1 knot family

[Claim index](../CLAIM_INDEX.md) · [Evidence policy](../EVIDENCE_POLICY.md)

**Record type:** early handoff

**Status as recorded:**

```text
D
```

**Interpretation:** Historical status only; check later corrections. Internal review is not external specialist review.

## Statement and recorded scope

```text
MID-06  D  Exact Whitehead factor and actual deep-jet u=1 knot family
------------------------------------------------------------------------
For the standard inherited untwisted Whitehead shell,
 d_Wh(A)=unit*(1-A^4)(1+A^8)(1+A^12).
An explicit trefoil-exterior quotient T=rotation(<-1>+<1/2>+<1/3>)+<-6>
has f_inf(T)=A^-18 and x(T)=A^2(A^4-1)(1+A^8)(1+A^12).
Preferred half-integral closure gives
 V_B(A^-4)-1=A^-10(A^4-1)(A^8+A^4+1)x(T)
(opposite choice has factor -A^-2(A^4-1)(A^8+A^4+1)).
After r Whitehead layers and +/-1/2 filling, actual knots B_r satisfy
 V_Br(t)-1=epsilon_r t^k_r (t-1)^(r+2)(t^2+t+1)
                         *(t^2+1)^(r+1)(t^3+1)^(r+1).
Therefore u(B_r)=1, they are nontrivial and pairwise distinct, orders at
1 and -1 are r+2 and r+1, and the first Taylor coefficient at 1 has
absolute value 12*4^r. This is not vanishing of EVERY finite-type invariant.
Proof: outputs/jones-exact-knot-family-and-zero-factor-target.txt;
work/transmission18/whitehead_factor_and_clasp_audit.txt,
whitehead_factor_check.py, exact_factor_certificate.py,
trefoil_actual_PD_checks.json. All-r scope follows the shell identity.

------------------------------------------------------------------------
```

## Provenance

[Source record](../../archive/outputs/claude-handoff/RESULT_LEDGER.json). The source wording is retained; consult the chronology for later restrictions or withdrawals.

## Identified supporting artifacts

- [jones-exact-knot-family-and-zero-factor-target.txt](../../archive/outputs/jones-exact-knot-family-and-zero-factor-target.txt)
- [exact_factor_certificate.py](../../archive/work/transmission18/exact_factor_certificate.py)
- [trefoil_actual_PD_checks.json](../../archive/work/transmission18/trefoil_actual_PD_checks.json)
- [whitehead_factor_and_clasp_audit.txt](../../archive/work/transmission18/whitehead_factor_and_clasp_audit.txt)
- [whitehead_factor_check.py](../../archive/work/transmission18/whitehead_factor_check.py)

These links were resolved from explicit filenames, not inferred as a complete logical dependency list.
