# EKT band-fusion obstruction, including arbitrary unknot seeds

[Claim index](../CLAIM_INDEX.md) · [Evidence policy](../EVIDENCE_POLICY.md)

**Record type:** early handoff

**Status as recorded:**

```text
INTERNAL-PROOF; exact family theorem; novelty unverified.
```

**Interpretation:** Historical status only; check later corrections. Internal review is not external specialist review.

## Statement and recorded scope

```text
EARLY-03 — EKT band-fusion obstruction, including arbitrary unknot seeds
Status: INTERNAL-PROOF; exact family theorem; novelty unverified.
For a two-component link L of determinant zero, a band to a determinant-one
knot would make Sigma2(L) zero surgery on a knot in an integral homology
sphere; hence H1(Sigma2(L)) must be Z. Nonzero finite torsion blocks every
such band, not merely a band to U.
For EKT H(T,U) with primitive Fox boundary pairs (pT,qT),(pU,qU),
 H1(Sigma2 H(T,U)) = Z direct-sum coker[[pU,-2qT],[-2qU,pT]].
This applies to nonrational tangles whose numerator is U: the cover is a
knot exterior in S3, giving a free integral module; fractions alone would
not justify it for arbitrary nonrational tangles.
LL2: (p_n,q_n)=Omega^n(1,0), Omega=[[3,8],[1,3]], p_n^2-8q_n^2=1;
 H1=Z direct-sum Z/(1+12q_n^2). Orders n=1..4:13,433,14701,499393.
LL1(m,n): H1=Z direct-sum Z/|12*4^m(3n+2)-1|, never torsion-free.
Strongest form: for ANY two-tangle S with N(S)=U, start with
H(S,infinity+2) and apply opposite omega iterates j to its two slots.
Normalize S's boundary pair to (1,d), let Omega^j=[[a,8b],[b,a]]. Then
 H1=Z direct-sum Z/|1+12b(b+ad)|.
This order is 1 exactly at j=0; modulo12 and Pell's equation show it is
>1 for every nonzero j. j=0 is the actual two-component unlink.
Thus all nonzero members are excluded from band-fusion to Jones-one knots.
LL1 omega iterates have exactly the pre-omega unlink exception (k=-1
when indexing from the displayed LL1 diagram).
Checks: full PD/Fox Smith forms, 28 LL1 seeds, 35 orbit cases; Watson's
published braid for LL2(1) independently gives Smith diag(1,13,0,0).
Sources: work/band_obstructions.md, work/ekt_homology_notes.md,
work/ekt_model/{ll1_scan,ll1_orbit}.py/.json and band_evidence.
Correction: repeated EKT (1 dot 1/2)^m means the left-associated FACTOR
LIST, not repeated multiplication by the compound rational tangle.
An old LL1/LL2 indexing concern was avoided by actual-diagram calibration.
```

## Provenance

[Source record](../../archive/outputs/claude-handoff/RESULT_LEDGER.json). The source wording is retained; consult the chronology for later restrictions or withdrawals.

## Identified supporting artifacts

- [band_obstructions.md](../../archive/work/band_obstructions.md)
- [ekt_homology_notes.md](../../archive/work/ekt_homology_notes.md)

These links identify recorded evidence; they are not a claim that the logical dependency list is complete.
