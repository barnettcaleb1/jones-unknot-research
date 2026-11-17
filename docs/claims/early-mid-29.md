# Rank-one fusion projectors and residual-faithfulness equivalence

[Claim index](../CLAIM_INDEX.md) · [Evidence policy](../EVIDENCE_POLICY.md)

**Record type:** early handoff

**Status as recorded:**

```text
D/N/C
```

**Interpretation:** Historical status only; check later corrections. Internal review is not external specialist review.

## Statement and recorded scope

```text
MID-29  D/N/C  Rank-one fusion projectors and residual-faithfulness equivalence
------------------------------------------------------------------------
For a three-puncture curve a in the five-punctured disk, residual TL5[3,2]
 rho(D_a)=A^-6 I+(A^6-A^-6)P_a, rank P_a=1.
At A=1, tr(P_a P_b)=1 if enclosed subsets agree and1/9 otherwise (edge-function
S5 model). Therefore nonzero powers of two such twists commute in the generic
representation iff P_a=P_b; different subsets are excluded, regardless of
winding. For any fixed different-subset pair, sufficiently high powers of their
matrices freely generate by real projective ping-pong.
Same-subset exclusion: if g is a product of nonzero even powers on one or two
DISJOINT cross-partition arcs, P_g(a)=P_a forces all exponents0. Joint spectral
weights at A1 are1/3,2/3 for one, and1/6,1/6,1/6,1/2 for two, so every channel
is present and equal monomial eigenvalues force zero exponents.
Pass30 equivalence: nonfaithfulness of residual rho <=> collision of projectors
for distinct three-puncture curves <=> collision with any fixed curve and same
subset <=> a strictly larger quantum than geometric stabilizer. Kernel of the
action on all such curves is the braid center; rho is faithful on its center.
Therefore this collision gate is NOT an easier proven intermediate problem.
A collision would yield a nontrivial exponent-zero residual kernel; Long with
Burau plus Ito would give Jones counterexamples. No collision exists in our data.
Universal skein positivity cannot prove fixed-color faithfulness: a nonzero
multicurve element (a-mu1)(a-mu3) is killed by the fixed-color representation.
Its positive square is likewise killed; this is not a simple-curve collision.
Proofs: work/research28/braid_structure.txt, verify_rank_one_twists.py;
work/research29/curve_projector.txt, verify_joint_support.py;
work/research30/braid_global.txt.

------------------------------------------------------------------------
```

## Provenance

[Source record](../../archive/outputs/claude-handoff/RESULT_LEDGER.json). The source wording is retained; consult the chronology for later restrictions or withdrawals.

## Identified supporting artifacts

- [braid_structure.txt](../../archive/work/research28/braid_structure.txt)
- [verify_rank_one_twists.py](../../archive/work/research28/verify_rank_one_twists.py)
- [curve_projector.txt](../../archive/work/research29/curve_projector.txt)
- [braid_global.txt](../../archive/work/research30/braid_global.txt)

These links identify recorded evidence; they are not a claim that the logical dependency list is complete.
