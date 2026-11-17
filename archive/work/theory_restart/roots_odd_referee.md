# Referee: ROOTS and the repaired odd-closure consequence

Referee: Codex subagent roots_odd_referee, 16 November 2026.
Scope: Claude210856, items 2 and 4. Verdict: both conclusions hold, with a useful simplification of the signature argument and an orientation convention that must be made explicit.

## 1. Fixed conventions and inputs

Write L_n=T(1/n), n an integer, with L_0=U. The preferred invariant is J in Z[t,t^{-1}], J=1 modulo (t+1)^2. Put G=(J-1)/(t+1)^2 and Phi_3=1+t+t^2. The corrected dictionary's closure formula is

    V(L_n)=t^{12j epsilon_n} [1+(1-(-t)^{-n}) Phi_3 G],
    epsilon_n=0 for n even, 1 for n odd.

The oriented branched cover is the appropriate orientation of 1/n surgery on the covering knot K; in the convention of this displayed formula and J''(-1)=-24a_2(K), its Casson invariant is -n a_2(K). Reversing the chosen identification of the cover changes this sign. One must not simultaneously state this closure formula, Mullins's formula below, and lambda=+n a_2 without inserting the orientation reversal. All zero and uniqueness assertions here are independent of that choice.

Use Casson normalization (half the doubled Casson-Walker normalization):

    lambda(Sigma_2 L)=-V_L'(-1)/(12 V_L(-1))+sigma(L)/8.

This is Mullins, Topology 32 (1993), Theorem 5.1. A primary extension/source check is S. Garoufalidis, *Signatures of links and finite type invariants of cyclic branched covers*, Theorem 1.1 and Remark 1.2, arXiv:math/9811021:
https://people.mpim-bonn.mpg.de/stavros/publications/printed/signatures_of_links_and_finite_type_invariants_of_cyclic_branched_covers.pdf
Its invariant normalization and signature convention must be translated consistently; the report's numerical denominator is the ordinary integral-homology-sphere Casson normalization.

## 2. The signatures are constant on each parity class

Every L_n has determinant one, since its branched double cover is integral homology sphere surgery. A symmetrized Seifert matrix for L_n is therefore an even unimodular integral form. Its signature is divisible by eight. This is a direct lattice-theoretic explanation; no Arf-to-signature implication is being assumed.

L_{n+2} and L_n differ by a single crossing change: change one crossing in the two-extra-crossing twist box and cancel the resulting Reidemeister-II pair. Therefore their signatures differ by at most two (the Seifert-form rank-one crossing-change calculation). Both signatures lie in 8Z, so they are equal. Thus sigma(L_n) is constant on each parity class. The even value is zero because L_0=U.

This supplies a short missing justification in the dictionary's original derivation of the second moment. No genus bound for L_n and no extrapolation from an unknotting-number-one example is needed.

For completeness, differentiate the displayed closure formula. Since

    (1-(-t)^{-n})' at t=-1 = -n,

one obtains

    V'(L_n)(-1)=-12j epsilon_n-nG(-1).

For nonzero even n, Mullins and Casson surgery, with sigma=0, give G(-1)=-12a_2(K). Thus J''(-1)=2G(-1)=-24a_2(K), independently of ROOTS. Substitution for odd n gives sigma(L_n)=-8j. In particular j is an integer: the signature is divisible by eight. This also justifies the integrality of j needed when evaluating the framing prefactor at i and at the sixth root.

## 3. ROOTS is correct

Only the preferred integrality of G, the closure formula, integer j, and the usual knot evaluations are needed.

At t=1, the n=1 formula gives

    1=V(L_1)(1)=1+6G(1),

hence G(1)=0.

At t=i, the prefactors are one, and

    V(L_1)(i)=1+(1+i)G(i),
    V(L_2)(i)=1+2iG(i).

The knot value V(i) is plus or minus one. Consequently G(i) belongs both to {0,-1+i} and to {0,i}, so G(i)=0. In fact determinant-one knots have Arf invariant zero, so one could use the stronger value +1, but the two-probe proof avoids that extra fact.

At zeta=exp(i pi/3), again the prefactor is one. Since Phi_3(zeta)=2zeta,

    V(L_1)(zeta)=1+(3+i sqrt(3))G(zeta).

The double cover has H_1(-;Z/3)=0, so the Lickorish-Millett value is plus or minus one. If it is minus one, then G(zeta)=-2/(3+i sqrt(3)). This element of Q(sqrt(-3)) has norm 1/3, whereas the norm of an algebraic integer in that quadratic field is an integer. Since G is integral Laurent and zeta a unit algebraic integer, this is impossible. Thus G(zeta)=0.

Primary source for the special evaluations: W. B. R. Lickorish and K. C. Millett, *Some evaluations of link polynomials*, Comment. Math. Helv. 61 (1986), 349-359, Theorems 1 and 3:
https://web.math.ucsb.edu/~millett/Papers/1986Millett6LickorishCommMathHelv.pdf
Theorem 1 is the Arf evaluation at i; Theorem 3 gives the sixth-root value in terms of H_1 of the double cover over Z/3. Here there is one link component and that homology group is zero.

Since all factors are distinct monic irreducibles over Q, Gauss's lemma now gives

    (t+1)^2 (t-1)(t^2+1)(t^2-t+1) divides J-1

in Z[t,t^{-1}]. Pairwise comaximality over Z is not needed. This product is minus (1-t^4)(1+t^3), so ROOTS proves exactly the factor used earlier in the dictionary, without importing it from data. If a_2=0, the second-derivative identity raises the (t+1) multiplicity to at least three. It does not, by itself, force j=0.

## 4. Odd closures: the repaired corollary and a sharper form

Suppose V(L_n)=1, n nonzero. Mullins gives lambda=sigma/8. For odd n, the constant signature is -8j, while Casson is -n a_2 in our consistent convention. Thus necessarily

    j=n a_2(K).

A simultaneous convention reversal changes the corresponding sign, never the zero or uniqueness conclusions.

If a_2=0, a Jones-unit odd closure forces j=0. The closure formula then has no prefactor; its nonzero Laurent coefficient (1-(-t)^{-n})Phi_3 implies J=1. The even case has the same implication without any signature input. Conversely J=1 forces j=0: for example differentiate the n=1 formula at t=1, using V'_K(1)=0, to obtain J'(1)=-8j. Thus in the a_2=0 regime, for every nonzero n,

    V(L_n)=1 if and only if J=1.

When a_2 is nonzero, no even n is Jones-unit because J is nonflat by its second derivative. An odd Jones-unit n, if one exists, is the single parameter determined by j=n a_2. This is stronger than merely comparing signatures with a linear crossing-change bound: signatures are exactly constant on odd parameters. It also gives the arithmetic gate a_2 divides j, with odd nonzero quotient, in the chosen convention. If that gate fails, all nonzero closures are detected already.

Accordingly the repaired corollary is accepted: nonflatness detects every nonzero closure except possibly one odd parameter in the a_2-nonzero case. No actual exceptional example or realizability assertion is supplied by the formal J_* from the previous letter.

## 5. Unknotting-number-one consequence

The stated implication from Lemma Q for all strong inversions is valid, with the determinant-one hypothesis inserted at the right place. Given a hypothetical nontrivial Jones-unit knot L of unknotting number one, perform the unknotting crossing change. Montesinos's trick presents Sigma_2(L) as p/2 surgery on a strongly invertible knot K in S^3, since the two rational fillings are at distance two. Jones-unitness gives det L=1, so |p|=1. Hence L is one of the even-parameter closures L_{+2},L_{-2} after marking/sign choice. If K is nontrivial, Lemma Q and the even closure formula exclude V(L)=1. If K is the unknot, the quotient tangle is rational and the determinant-one two-bridge branch knot is the unknot. This completes the implication. The assertion does not say arbitrary unknotting-one knots arise as 1/2 surgery; the numerator-one conclusion uses determinant one.

## Final scope

ROOTS and the signature repair are genuine identities and arithmetic refinements, not a new separation mechanism on the a_2=0 core. On that core the all-n knot-closure problem is exactly the nonflatness problem J!=1. No finite root test can by itself establish it.
