# Bounded attack: anti-parallel twists and Jones-trivial links

Research notes, 31 October 2026. No solution of the general problem is claimed.

## 1. Exact algebraic reduction

Use x = t^(1/2), p = x - x^(-1), and delta = -(x+x^(-1)). Let K_n be an anti-parallel full-twist family with a fixed oriented smoothing L. Choose the index/sign convention so that a crossing change gives K_(n-1) and oriented skein gives

    V_n = x^4 V_(n-1) + p x^2 H,     H = V_L.

The oriented smoothing is independent of n: the remaining twists become removable curls. The normalization is the usual one with V_unknot = 1 and V_unlink2 = delta.

Define S_n = (x^(4n)-1)/(x^4-1). For n>=1 this is sum_(j=0)^(n-1) x^(4j); for n<=-1 it is -sum_(j=n)^(-1) x^(4j); S_0=0. Direct induction, in both directions, gives

    V_n - 1 = x^(4n)(V_0-1) + p x^2 (H-delta) S_n.

This is an identity of Laurent polynomials. If K_0 is the unknot, then for every n != 0,

    V_n = 1  iff  H = delta,

because Z[x,x^(-1)] is an integral domain and p*x^2*S_n != 0. Thus an arbitrary long twist cannot force Jones vanishing: either the smoothing already has the unlink Jones polynomial, in which case every twist has Jones 1, or every nonzero twist has nontrivial Jones polynomial.

More generally, if V_n=V_m=1 for any n != m then H=delta and all V_j=1. This follows by shifting the base index to m. The same assertion does not say that a family with H=delta has V=1 unless a seed value is 1.

This is a standard skein reduction, not a novelty claim. Hedden–Watson, On the geography and botany of knot Floer homology, arXiv:1404.6913, §3 equation (9), explicitly gives the H=delta specialization for band sums of the two-component unlink and notes the hypothetical infinite Jones-trivial family consequence.

Source: https://arxiv.org/pdf/1404.6913

## 2. Topological meaning and limitation

To construct a counterexample by this route it would suffice to find a nonnugatory crossing c in an unknot diagram whose oriented smoothing L satisfies V_L=delta. The known cosmetic-crossing theorem for the unknot rules out the possibility that changing this crossing merely produces another unknot. Thus the n=-1 member is a nontrivial Jones-trivial knot. It would have unknotting number one.

Conversely, a Jones-trivial nontrivial knot of unknotting number one gives such a skein triple with the unknot. Therefore this restricted construction problem is equivalent to unknot detection within unknotting-number-one knots. It is not established here to be equivalent to the full conjecture.

If the smoothed link L is the actual two-component unlink, the band-sum unknot theorem rules the construction out: a band sum of a split link that yields the unknot is a trivial connected sum. Here one needs a nontrivial Jones-trivial two-component link together with a very special band to the unknot; the polynomial equality alone supplies no such band.

Primary modern discussion of cosmetic crossing theorem, plus precise tangle formulation: Artem Kotelskiy, Tye Lidman, Allison H. Moore, Liam Watson, and Claudius Zibrowius, Cosmetic operations and Khovanov multicurves, Theorem 1.2 (a Conway tangle with an unknot closure has no two distinct isotopic rational fillings unless it is rational). The paper cites Scharlemann–Thompson, Link genus and the Conway moves (1989), for the unknot case.

Source: https://pmc.ncbi.nlm.nih.gov/articles/PMC11139753/

## 3. Rigorous homology obstruction to any band-to-unknot

**Lemma.** If a two-component link L has V_L(t)=-(t^(1/2)+t^(-1/2)) and an embedded band surgery takes L to the unknot, then

    H_1(Sigma_2(L); Z) = Z.

In particular any torsion, or free rank other than one, obstructs every such band.

**Proof.** Reverse the band surgery. The double branched cover of the unknot is S^3. The lift of the band's core is a knot J in S^3. The Montesinos trick says that banding corresponds to integral Dehn surgery: the two local rational tangle slopes have distance one. Consequently Sigma_2(L) = S^3_r(J) for some integer r. The abelianization is Z/rZ, where r=0 means Z. The link determinant |V_L(-1)| is zero, and the determinant equals the order of H_1 of the double branched cover when finite (zero when infinite). Therefore H_1 is infinite, r=0, and H_1=Z. QED.

No assumption of a diagrammatically simple band is used. Thus a Smith normal form of any valid integral Goeritz presentation gives a complete cheap necessary test for this route. Passing the test is only necessary, not sufficient.

Primary source for the specific band/integral-surgery correspondence: Kenneth L. Baker, The Poincaré homology sphere, lens space surgeries, and some knots with tunnel number two, Pacific J. Math. 305 (2020), §3, journal p.7, paragraph beginning “If M is the double branched cover...” The published text explicitly describes a band along an arc and its lift as the dual knot of integral surgery.

Source (article): https://msp.org/pjm/2020/305-1/pjm-v305-n1-p01-s.pdf

Original Montesinos: Surgery on links and double branched covers of S^3, https://webhomes.maths.ed.ac.uk/~v1ranick/papers/neuwir3.pdf

## 4. What the known Jones-trivial links supply

Eliahou–Kauffman–Thistlethwaite (2003), Theorem 4.1, constructs LL2(n)=H(T_n,-T_n). For even n the oriented Jones polynomial is exactly delta; for odd n it is t^(+/-6)*delta, not delta. Even n also gives boundary links with zero Alexander polynomial. Section 4.2 supplies another family LL1(m,n). Thus merely comparing determinant or one-variable Alexander polynomial will not eliminate every example.

Source: https://homepages.math.uic.edu/~kauffman/ekt.pdf

I did not find a published homology computation of the double branched cover of LL2(2) in this bounded search. No particular torsion group is claimed here. A direct Goeritz/Fox-coloring/branched-cover computation remains to be done.

Liam Watson's thesis, §8.3 around pp.157–158, discusses branched covers of these Hopf-satellite examples and proves Khovanov homology distinguishes the LL2 family from the unlink. It does not in the retrieved passage provide the H_1 Smith form needed above.

Source: https://www.collectionscanada.gc.ca/obj/thesescanada/vol2/QMUQ/TC-QMUQ-2310.pdf

## 5. Concrete next test

For a verified diagram of a Jones-trivial two-component EKT link, compute the integral Goeritz matrix and its Smith form. If it is not diag(1,...,1,0), stop: no band from that link can produce the unknot. If it is, search bands only after preserving a combinatorial diagram certificate and check resulting knot nontriviality independently. A local fusion that yields a diagram within the established 24-crossing range cannot give a counterexample; bands adding substantial diagram complexity would be required.
