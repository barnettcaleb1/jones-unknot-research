# EXACT TWO-BAND INTEGER-LOCUS CERTIFICATES (pass37)

[Claim index](../CLAIM_INDEX.md) · [Evidence policy](../EVIDENCE_POLICY.md)

**Record type:** early handoff

**Status as recorded:**

```text
IP
```

**Interpretation:** Historical status only; check later corrections. Internal review is not external specialist review.

## Statement and recorded scope

```text
LATE-06 [IP] EXACT TWO-BAND INTEGER-LOCUS CERTIFICATES (pass37)
Actual two-site unknot anchor, partial oriented Jones S1,S2, double cut delta^2;
D_i=S_i-delta, z=x^-4:
  delta(V_mn-1)=z^n(1-z^m)D1+z^m(1-z^n)D2.
If both D_i are nonzero and ord_1 D1 != ord_1 D2, the ONLY Jones-one integer
pair is (0,0), because the two nonzero terms have unequal vanishing orders.
Additional rank-one matrix B=d vv^T, v1*v2!=0: put a=v2^2,b=v1^2.
Signed determinant forces b m+a n=0, i.e. (m,n)=(a k,-b k). For k!=0,
V=1 iff R=D1/D2=z^(ak)(z^(bk)-1)/(z^(ak)-1), hence necessarily
  k*= -[x R'/R]_(x=i)/(2(a+b)).
At most ONE non-anchor point exists. If k* not a nonzero integer, reject all;
otherwise verify full Laurent identity, not just derivative integrality.
With c_i=D_i(i)/i,e_i=(xD_i')(i)/i, k*=-(e1/c1-e2/c2)/(2(a+b)).
If one v_i=0, retain the separate coordinate family: it is constant iff the
corresponding S_i=delta. Actual coherent fission geometry makes diagonal B_ii
even, hence d even; do not invent independent partial-link reorientations.
Proof: research37/isolated_twist_algebra.txt, topology_audit.txt;
verify_isolated_twist_algebra.py/.json, topology_arithmetic_audit.json.
```

## Provenance

[Source record](../../archive/outputs/claude-handoff/RESULT_LEDGER.json). The source wording is retained; consult the chronology for later restrictions or withdrawals.

## Identified supporting artifacts

- [isolated_twist_algebra.txt](../../archive/work/research37/isolated_twist_algebra.txt)
- [topology_arithmetic_audit.json](../../archive/work/research37/topology_arithmetic_audit.json)
- [topology_audit.txt](../../archive/work/research37/topology_audit.txt)

These links were resolved from explicit filenames, not inferred as a complete logical dependency list.
