# Carmi–Cohen universal compression package is contradicted

[Claim index](../CLAIM_INDEX.md) · [Evidence policy](../EVIDENCE_POLICY.md)

**Record type:** early handoff

**Status as recorded:**

```text
INTERNAL-PROOF / explicit classical-knot obstruction.
```

**Interpretation:** Historical status only; check later corrections. Internal review is not external specialist review.

## Statement and recorded scope

```text
EARLY-01 — Carmi–Cohen universal compression package is contradicted
Status: INTERNAL-PROOF / explicit classical-knot obstruction.
Target: Avishy Carmi and Eliahu Cohen, On trivial Jones–Vassiliev polynomials,
arXiv:2606.22410v1, submitted 21 June 2026. Do not change this identifier.
For x=t^(1/2), p=x-x^(-1), take the trefoil twist family with odd L and
V_1=x^2+x^6-x^8. Its fixed smoothing is H=-x-x^5 and
 V_L=x^4 V_(L-2)+x^2-x^4+x^6-x^8.
The unique leading monomial is -x^(2L+6). Reducing in the rank-two basis
V=A(p)+xB(p), x^2=px+1, proves deg_p V_L=2L+5 and b_(2L+5)=-1.
At L=23 this gives b_51=-1, whereas Proposition5.12 + Theorem5.6 +
Lemma5.8 as supplied predict deg_p<=3*3+11+2=22 independently of L.
The combined geometric hypotheses cannot all hold. The paired-skein
conditional algebra is not refuted with its premises intact. Changing
the fixed overhead 11 cannot repair unbounded degree. This is NOT a
counterexample to Jones detection: all these knots have V!=1.
Proof: work/jones-audit/main.tex; verifier outputs/verify_twist_obstruction.py.
Later precision: outputs/jones-preprint-local-move-audit.txt and research36
give an exact G2 fixed-clasp error. Defer detailed G2 verdict to late ledger.
Original arXiv/version/status statements are dated audit observations, not
a fresh 2 November literature check.
```

## Provenance

[Source record](../../archive/outputs/claude-handoff/RESULT_LEDGER.json). The source wording is retained; consult the chronology for later restrictions or withdrawals.

## Identified supporting artifacts

- [jones-preprint-local-move-audit.txt](../../archive/outputs/jones-preprint-local-move-audit.txt)
- [verify_twist_obstruction.py](../../archive/outputs/verify_twist_obstruction.py)
- [main.tex](../../archive/work/jones-audit/main.tex)

These links were resolved from explicit filenames, not inferred as a complete logical dependency list.
