# Exterior-volume endpoint and simultaneous finite-probe evasion

[Claim index](../CLAIM_INDEX.md) · [Evidence policy](../EVIDENCE_POLICY.md)

**Record type:** early handoff

**Status as recorded:**

```text
C/D/N
```

**Interpretation:** Historical status only; check later corrections. Internal review is not external specialist review.

## Statement and recorded scope

```text
MID-33  C/D/N  Exterior-volume endpoint and simultaneous finite-probe evasion
------------------------------------------------------------------------
Define v(K)=sum of hyperbolic JSJ piece volumes of E(K), not branched-cover
volume. It is additive under connected sum; v=0 exactly for graph knots.
For winding-p cables,
 a2(cable_(p,q)(K))=p^2 a2(K)+(p^2-1)(q^2-1)/24.
Graph knots arise from torus knots by cabling/sums, so a2=0 among graph knots
forces U. V''(1)=-6a2, hence a nontrivial Jones-one K has v(K)>0. Therefore
bounding v throughout ANY ONE nonempty whole Jones fiber would prove detection
by J#K^m. The bound is unproved and equivalent in existential form to detection.
Actual finite-probe theorem: for any finite ordinary Taylor order d, finite
set Omega of roots of unity, and B>0, there is a hyperbolic K with Delta=1,
V(e^h)=1+O(h^(d+1)), V(zeta)=1 for every zeta in Omega, and volume>B.
Derived from Kalfagianni hyperbolic Brunnian crossing-circle parents, high
adjacency, and arbitrarily long twists divisible by finite root periods.
At t=-1 do NOT apply the semisimple twist identity: Delta=1 plus V(-1)=1 mod4
gives the exact value1 separately. General bounded finite-type invariants can
also match U. This existence construction supplies no finite explicit diagram
or whole-polynomial identity. Parent cusp count must grow for unbounded volume.
Proofs: work/research32/geometric_mechanism.txt, exterior_volume_audit.txt,
finite_probe_volume_obstruction.txt, finite_probe_independent_audit.txt;
verify_twist_specializations.py checks convention cases, not the theorem alone.

------------------------------------------------------------------------
```

## Provenance

[Source record](../../archive/outputs/claude-handoff/RESULT_LEDGER.json). The source wording is retained; consult the chronology for later restrictions or withdrawals.

## Identified supporting artifacts

- [exterior_volume_audit.txt](../../archive/work/research32/exterior_volume_audit.txt)
- [finite_probe_independent_audit.txt](../../archive/work/research32/finite_probe_independent_audit.txt)
- [finite_probe_volume_obstruction.txt](../../archive/work/research32/finite_probe_volume_obstruction.txt)
- [geometric_mechanism.txt](../../archive/work/research32/geometric_mechanism.txt)
- [verify_twist_specializations.py](../../archive/work/research32/verify_twist_specializations.py)

These links were resolved from explicit filenames, not inferred as a complete logical dependency list.
