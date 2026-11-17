# Positive geometry for the Jones coefficient norm: two decisive calibrations

Date: 2026-11-03. Independent bounded theory pass. No enumeration.

## Verdict

I did not find a new positive geometric mechanism proving Jones detection. The most natural concrete attempt—Morse-reducing the quantum-zero reflection-double complex to positive critical generators—fails because that complex can have genuine odd homology. A separate torus-knot calculation shows that the coefficient norm cannot bound the usual geometric or Floer complexity measures. These are useful design constraints, not progress on the missing positivity theorem.

## 1. The norm is already minimal above one on arbitrarily complicated torus knots

Let E(K)=sum_j a_j^2 for V_K(t)=sum_j a_j t^j, and D(K)=(E(K)-1)/2.

The standard torus formula gives, for EVERY integer q>1 coprime to 3,

    V_{T(3,q)}(t)
      = t^(q-1) (1-t^4-t^(q+1)+t^(q+3))/(1-t^2)
      = t^(q-1) (1+t^2-t^(q+1)).

The three exponents are distinct, so

    E(T(3,q))=3,        D(T(3,q))=1.

No odd-q restriction is needed. A primary exposition of the torus formula is [Vaughan Jones, The Jones polynomial for dummies](https://abel.math.harvard.edu/~ctm/home/text/class/harvard/101/22/html/home/pdf/for_dummies.pdf), final calculation of Section 7, page 45.

Meanwhile their Seifert genus is q-1 and their slice genus and unknotting number are q-1; for the latter equalities see [Rasmussen, Khovanov homology and the slice genus](https://arxiv.org/abs/math/0402131), the Milnor-conjecture corollary. Thus D cannot assign a uniformly positive cost to each essential handle, each unknotting move, or each ordinary geometric intersection needed to represent the knot.

There is an equally explicit Floer-rank calibration. Up to a Laurent shift,

    Delta_{T(3,q)}(t)=(1+t^q+t^(2q))/(1+t+t^2).

For q=3n+1 its coefficient l1 norm is 4n+1; for q=3n+2 it is 4n+3. To check this without computation, expand

    1/(1+t+t^2) = (1-t)/(1-t^3).

Before degree q the coefficient pattern is 1,-1,0. From degree q through 2q-2 it is the sum of that pattern and its q-shift. Counting the nonzero entries gives the two displayed formulas; every nonzero coefficient is +/-1. Therefore any homology whose graded Euler characteristic is Delta has unbounded total rank on this E=3 family. In particular this applies to knot Floer homology and to KHI: [Kronheimer--Mrowka, Instanton Floer homology and the Alexander polynomial](https://arxiv.org/abs/0907.4639) identifies the Alexander coefficients with graded Euler characteristics of KHI.

Consequently, an inequality such as E>=dim KHI, or an identity equating D to the count of all nontrivial instanton/Floer generators with positive multiplicities, is false. This does not rule out a new coarse invariant with one positive contribution for an entire essential geometric structure. But no such structure or count has been identified here.

## 2. A precise candidate Morse lemma, and its falsification

The plausible candidate was:

> The quantum-degree-zero part of the reduced Khovanov complex of K#mirror(K) has a Reidemeister-compatible algebraic Morse matching whose unmatched generators are all even, with one distinguished identity generator. Its remaining positive generators would realize E(K)-1.

This would turn the reflection norm into an actual nonnegative chain count before taking Euler characteristic. The motivation is concrete: over a field, the reflection-double complex is C tensor C-dual, so its quantum-zero sector is the endomorphism complex of C preserving quantum grading.

However, let R=Kh_red(K) over a field. The homology of this endomorphism complex is

    H^r(End_{q=0}(C))
      = direct_sum_{i,j} Hom(R^{i,j}, R^{i+r,j}).

This is standard linear algebra over a field: split C into its homology plus contractible summands. Hence any nonzero adjacent homological groups R^{i,j} and R^{i+1,j} give nonzero H^1 of the quantum-zero endomorphism complex. No chain-homotopy equivalence, and therefore no valid algebraic Morse matching, can remove this odd homology and leave only even critical generators.

Such classical knots exist. The n=1 case of [Gonzalez-Meneses--Manchon--Silvero, Theorem 13](https://arxiv.org/html/1511.05845) has a lowest quantum row with two free rank-one groups in adjacent homological degrees. The reduction-over-F2 and reflection conventions were checked in the project's `work/global_design/n2.md`; over F2 the unreduced/reduced splitting transfers that row to reduced homology. Thus this is an actual classical knot obstruction, not a hypothetical complex.

Numerically, if one fixed quantum row has even dimension a and odd dimension b, its contribution to E is (a-b)^2, while its endomorphism homology has even dimension a^2+b^2 and odd dimension 2ab. Reflection has made the Euler number a square; it has not killed the odd geometric information.

An arbitrary sign-reversing involution on the state-pair sum could cancel these classes at the level of Euler characteristics. It would then no longer be a Morse reduction of Khovanov's complex. One would need new geometric moves and an independent argument that zero remaining defects yields a spanning disk. I have no such move or argument.

## 3. What remains open after these checks

Restricting the candidate to the Jones-unit locus avoids the known odd-homology examples unless one already has a Jones counterexample. But the restriction supplies no reason the odd groups should disappear; it restores the same Euler-to-object gap under a new name.

Likewise, a supersymmetric index equal to one does not imply one ground state: even and odd states can remain, and the endomorphism calculation exhibits exactly how they survive reflection. Classical one-component topology has not supplied a rule forbidding them.

The next worthwhile positivity proposal should specify an actual geometric complex or count distinct from the standard reflection endomorphism complex, explain why its contributions are nonnegative, and identify how its zero set produces a disk in S^3. It must also accommodate D=1 for all T(3,q), so it cannot count ordinary complexity with uniform positive weights. Without those additional ingredients, I recommend parking this positivity route rather than promoting another conjectural purity statement.
