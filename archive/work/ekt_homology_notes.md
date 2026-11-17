# Branched-cover homology obstruction for the EKT LL2 family

Research calculation, 31 October 2026. The Fox-coloring derivation below is independently calibrated against a published braid for LL2(1). The parent investigation independently constructed full planar diagrams for n=1,2,3,4, computed their Jones polynomials in Regina, and obtained the same integral homology groups from their full Fox matrices.

## Sources and exact normalization

Eliahou–Kauffman–Thistlethwaite, *Infinite families of links with trivial Jones polynomial*, Topology 42 (2003), 155–169, §4.1:
https://homepages.math.uic.edu/~kauffman/ekt.pdf

They define LL2(n)=H(T_n,-T_n), with T_0=infinity−2, T_1=3, T_2=5·1·2, T_3=5·1·4·1·2, etc. The rational tangle product T·k reflects T across the NW–SE diagonal and adds the integer k, so its fraction changes r→1/r+k. The omega operation changes r→(3r+8)/(r+3). Therefore, after forgetting framing, T_0 has fraction infinity and

    (p_0,q_0)=(1,0),
    (p_(n+1),q_(n+1))=(3p_n+8q_n,p_n+3q_n).

The first fractions are 3/1, 17/6, 99/35, 577/204. The matrix of this recurrence has determinant 1, so gcd(p_n,q_n)=1; p_n is always odd. Directly, p_n^2−8q_n^2=1.

Watson, *Involutions on 3-manifolds and Khovanov homology*, PhD thesis (2009), §8.5, printed p.157:
https://personal.math.ubc.ca/~liam/files/doctoral.pdf

Watson explicitly gives the linked trefoil/mirror example (LL2(1)) as the closure of

    sigma_3^3 (sigma_2^−1 sigma_3^−1 sigma_1^−1 sigma_2^−1)^2 sigma_1^−3.

This supplies an independently published braid realization of the common doubled Hopf clasp.

## Fox presentation

The universal abelian Fox coloring group (generators are arcs, and crossings impose the Fox relations) is Z plus H_1 of the two-fold branched cover. This is the universal presented group, not merely its group of integer-valued solutions, which would lose torsion. See Przytycki, *3-coloring and other elementary invariants of knots*, Theorem 3.3: https://arxiv.org/pdf/math/0608172 . At a crossing, 2 times the over-arc color equals the sum of the two under-arc colors. For a positive braid generator we use the color transfer (a,b)→(2a−b,a); its inverse is (a,b)→(b,2b−a).

Let

    C=(sigma_2^−1 sigma_3^−1 sigma_1^−1 sigma_2^−1)^2.

Its transfer matrix on four colors is

    [ 1  0 -2  2 ]
    [ 0  1 -2  2 ]
    [-2  2  1  0 ]
    [-2  2  0  1 ].

A rational tangle p/q placed vertically has a two-generator integral color group. In a compatible endpoint convention, its top colors can be parameterized by (s,s−qz), and its bottom colors by (s+pz,s+(p−q)z). This is the usual rational-tangle fraction/color relation: the endpoint differences are qz and pz. See Kauffman–Lambropoulou, *On the classification of rational tangles*, the integral-coloring proof: https://arxiv.org/abs/math/0311499 ; also the explicit p,q boundary formulas in https://indico.ictp.it/event/a08157/session/33/contribution/18/material/0/0.pdf , p.17. The generator z is integral because p and q are coprime. For an integer tangle n/1, this is exactly the transfer of sigma^n. The infinity tangle has p=1,q=0.

Put U=p_U/q_U in the left pair and T=p_T/q_T in the right pair, followed by C, and close. Write u,t for the respective difference generators. The closure equations reduce to

    p_U u−2q_T t=0,
    p_T t−2q_U u=0.

The two offsets s_U,s_T are unconstrained. Removing the single common constant coloring gives

    H_1(Sigma_2(H(T,U));Z) = Z ⊕ coker A,
    A = [[p_U,−2q_T], [−2q_U,p_T]].

Conventions that transpose A or negate its rows/columns produce the same Smith invariants. Four calibration cases:

* H(infinity,infinity) is the two-component unlink, and A is unimodular: H_1=Z.
* H(0,infinity) is the three-component unlink: H_1=Z^2.
* H(0,0) is the two-parallel of the Hopf link: the formula gives Z⊕Z/2⊕Z/2.
* H(T,infinity) is the split union of T^N and an unknot: the formula gives Z⊕Z/p_T, the expected group for a rational numerator.

## LL2 specialization

For U=−T, choose p_U=−p and q_U=q. Then

    A=[[-p,−2q],[-2q,p]],
    det A=−(p^2+4q^2).

If p is odd and coprime to q, the gcd of all entries is 1, so

    H_1(Sigma_2(LL2(n));Z) = Z ⊕ Z/(p_n^2+4q_n^2)
                              = Z ⊕ Z/(1+12q_n^2).

In particular:

    n=0: Z
    n=1: Z ⊕ Z/13
    n=2: Z ⊕ Z/433
    n=3: Z ⊕ Z/14701
    n=4: Z ⊕ Z/499393.

For every n>0, q_n>0 and the torsion is nonzero. The even-n subfamily has exactly the unlink Jones polynomial by EKT Theorem 4.1.

## Independent braid verification at n=1

The exact script work/attack/fox_braid.py computes the transfer matrix for Watson's published braid and its Smith invariants via gcds of all minors, without third-party packages. The matrix M−I has rows

    (-3,3,−2,2),
    (-3,3,−2,2),
    (−2,2,3,−3),
    (−2,2,3,−3).

Its Smith form is diag(1,13,0,0). Removing a global color gives H_1=Z⊕Z/13, confirming the general specialization at n=1.

## Consequence for banding

If any embedded band takes a two-component link with determinant zero to the unknot, the Montesinos trick expresses its branched cover as integral surgery on a knot in S^3. Determinant zero makes the surgery coefficient zero. Hence its H_1 must be Z, with no torsion. The homology calculation therefore obstructs every band from LL2(n) to the unknot for n>0, in particular every Jones-trivial LL2(2m), m>=1.

This rules out the entire LL2 family as a source for the proposed unknot-smoothing counterexample route. It does not prove Jones unknot detection, nor rule out other Jones-trivial links.

## Limits and caution on LL1

The rational-tangle calculation must not be naively applied to the full LL1(m,n) family: its factors include 1/2 in horizontal sums, and sums of two rational tangles need not be rational. A numerical fraction does not determine its integral coloring module. Also, EKT p.167 writes LL1(0,−1)=LL2(0), but the displayed definitions instead seem to give the linked-trefoil member LL2(1); this possible indexing discrepancy needs a separate diagram check and is not used above.

## Extension: the entire EKT orbit from an unknot numerator

The rationality hypothesis can be replaced by the following sufficient topological hypothesis: the numerator T^N is the unknot, followed by any reparametrization of the four-punctured tangle boundary. Indeed, X=Sigma_2(B^3,T) has a Dehn filling S^3 and is therefore the exterior of the filling-core knot. Hence H_1(X)=Z, and the map from boundary homology is surjective. Its universal Fox module is free of rank two, and its primitive difference data can be taken as (p,q)=(1,k), k an integer. The numerator filling has homology order |p|=1. The local boundary braid omega acts on (p,q) by the same matrix M as for rational tangles. Thus the Fox calculation above continues to hold; merely having a numerical tangle fraction without this free-module argument would not suffice.

Let U=infinity+2, so its primitive data are (1,0), and let

    L_n=H(T^(omega^n), U^(omega^(−n))).

Write

    M^n=[[a,8b],[b,a]],    a^2−8b^2=1.

The tangle data after applying the opposite transformations are

    (p_T,q_T)=(a+8bk,b+ak),
    (p_U,q_U)=(a,−b).

Therefore the finite part of H_1(Sigma_2(L_n)) has order

    |D|,    D=p_T p_U−4q_T q_U
             =1+12b(b+ak).

For n≠0, one has a>|b|>0. Therefore b+ak cannot vanish for any integer k. Thus D≠1. Also D≡1 (mod 12), so D≠−1 and D≠0. Consequently |D|>1 for every n≠0. The matrix may have two nontrivial invariant factors in general; only its determinant/order is used.

**Proposition.** Every nonzero opposite-omega iterate of an EKT diagram H(T,infinity+2), with T^N the unknot, has nontrivial torsion in the integral first homology of its double branched cover. Consequently no embedded band takes it to the unknot.

This covers LL2 as well as all LL1(m,n), since EKT Proposition 4.2 establishes that the LL1 seed numerators are unknots. For LL1(m,n), direct fraction/difference arithmetic gives the torsion order

    |12*4^m*(3n+2)−1|,

which is always greater than 1. The parent team independently checked the full planar diagrams for 0<=m<=3 and −3<=n<=3 (see work/ekt_model/ll1_scan.py and .json).

**Stronger immediate consequence.** No embedded band from one of these links can produce *any determinant-one knot*. If it did, the double branched cover of the resulting knot would be an integral homology sphere Y. The Montesinos trick would describe Sigma_2(L_n) as integral surgery on a knot in Y. Because its first homology is infinite, the surgery coefficient must be zero, giving H_1=Z, a contradiction. Thus this EKT band-fusion route cannot yield a Jones-trivial knot even if an unknot anchor is not demanded.

These are deductions from established elementary tools and the EKT construction. No claim of novelty is made.
