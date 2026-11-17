# Reversible finite classical positivity cannot model Jones

[Claim index](../CLAIM_INDEX.md) · [Evidence policy](../EVIDENCE_POLICY.md)

**Record type:** early handoff

**Status as recorded:**

```text
D/N
```

**Interpretation:** Historical status only; check later corrections. Internal review is not external specialist review.

## Statement and recorded scope

```text
MID-01  D/N  Reversible finite classical positivity cannot model Jones
------------------------------------------------------------------------
At A=i*r, r>1, q=r^-4, d=r^2+r^-2, write B_i=rI-r^-1 e_i.
Its eigenvalues are r and -r^-3; B_i^-1 has dominant eigenvalue -r^3.
Perron--Frobenius for a proper cone rules out a scalar gauge making both
directions preserve one proper cone on the ordinary two-channel module.

Stronger finite-state theorem: if a three-strand model has finite entrywise
nonnegative invertible crossing matrices whose inverses are nonnegative,
and a fixed closure depending otherwise only on strand count and writhe,
it cannot recover Jones on all knot closures. Such matrices are monomial.
For a common even permutation period m, their powers commute, but the knots
 beta_+=sigma1^m sigma2^m sigma1 sigma2,
 beta_-=sigma2^m sigma1^m sigma1 sigma2
have equal writhe and model matrix while their actual Jones difference is
 -q^(m+2)(1+q+q^2)(sum_(j=0)^(m-1)(-q)^j)^2 !=0 for q>0, q!=1.
The same argument covers a positive finite retract with a pointed polyhedral
physical cone: cone automorphisms permute finitely many extreme rays.
It does not cover arbitrary nonpolyhedral density-operator models, nonpositive
projections, or infinitely many states; those retain separate information gaps.
Control calculation gives |V(q)|<=q^((p-3b-n+1)/2)(1+q)^(n-1) for an n-braid
with p positive and b negative crossings. V=1 implies p-3b<=n-1 and its mirror
inequality. For positive braid knots this gives the known unknot detector.
Proof/data: work/fanout16/physics.txt; physics_check.json.

------------------------------------------------------------------------
```

## Provenance

[Source record](../../archive/outputs/claude-handoff/RESULT_LEDGER.json). The source wording is retained; consult the chronology for later restrictions or withdrawals.

## Identified supporting artifacts

- [physics.txt](../../archive/work/fanout16/physics.txt)
- [physics_check.json](../../archive/work/fanout16/physics_check.json)

These links identify recorded evidence; they are not a claim that the logical dependency list is complete.
