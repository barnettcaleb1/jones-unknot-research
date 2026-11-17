# Rational color corrections preserve nontrivial difference factors

2026-11-03. Algebraic theory pass; no sequence computation or geometric AJ claim. The primitive-specialization argument below was checked independently within the project. No novelty claim.

## Setup

Let K=Q(q,M), let sigma fix q and send M to qM, and let

    R=K[E;sigma],       E a=sigma(a) E.

For a sequence J_N, M acts by q^N and E shifts N to N+1. Work modulo finitely many initial values, so rational coefficients and the shift are well-defined wherever needed. Let J be q-holonomic and let g be a rational function in K. Set

    F_N=J_N-g(q,q^N).

Use minimal left annihilator generators P_J,P_F in R: every annihilator of J is a left multiple of P_J, and similarly for F. They are unique up to multiplication on the left by K^times. For the zero sequence use the generator 1.

The rational sequence g has first-order annihilator

    T_g=E-sigma(g)/g

when g is nonzero. Its rank-one difference module is isomorphic to the trivial rational module K, even though this displayed scalar operator need not be E-1 in its chosen cyclic generator.

## 1. Exact statement about composition factors

Let M_J and M_F be the finite-dimensional K-spans of all shifts of J and F, with their semilinear E actions. Inside the ambient sequence space put

    V=M_J+K=M_F+K,
    W=V/K.

Both cyclic modules surject onto W. Their kernels are M_J intersect K and M_F intersect K, respectively. Since K is one-dimensional over itself, each kernel is either zero or the trivial rank-one module K. Hence there are exact sequences

    0 -> epsilon_J K -> M_J -> W -> 0,
    0 -> epsilon_F K -> M_F -> W -> 0,
    epsilon_J,epsilon_F in {0,1}.

**Conclusion.** M_J and M_F have identical Jordan-Hoelder multiplicities for every simple difference module other than the trivial rank-one module. The multiplicity of the trivial module can differ by at most one. In particular their ranks, equivalently the orders of their minimal scalar recurrences, differ by at most one.

This is a comparison through a common quotient, not a claim that either module splits as a direct sum with K.

## 2. Primitive classical symbols: no monic-regularity assumption is needed

Put h=q-1. The h-adic valuation nu on K has residue field k=Q(M). Its valuation ring O consists of the rational functions regular at q=1 over that residue field. The automorphism sigma preserves nu, fixes h, and induces the identity on k.

For a nonzero Ore polynomial P=sum_i p_i E^i, define

    nu(P)=min_i nu(p_i).

Multiply P by a K-unit so nu(P)=0. Call this an h-primitive normalization, and let bar(P) in k[L] be its nonzero coefficientwise reduction at q=1. The resulting symbol is well-defined up to multiplication by k^times. Its L-degree can be smaller than the order of P; no degree-preservation hypothesis is being made.

**Gauss lemma.** For nonzero Ore polynomials P,Q,

    nu(PQ)=nu(P)+nu(Q).

Indeed, scale by powers of the central element h so both valuations are zero. Their nonzero reductions multiply in k[L], because sigma reduces to the identity. That product is nonzero since k[L] is a domain. This proves the assertion, including for nonintegral original factors.

**Theorem.** Let P_J,P_F be h-primitive minimal annihilator generators. Their primitive classical symbols satisfy

    bar(P_F) divides (L-1) bar(P_J),
    bar(P_J) divides (L-1) bar(P_F)                    (1)

in k[L]. Consequently every irreducible factor other than L-1 occurs with exactly the same multiplicity in the two symbols. The multiplicities of L-1 differ by at most one. Equivalently, up to a k-unit, their ratio is (L-1)^epsilon with epsilon in {-1,0,1}.

**Proof.** Apply P_J to the rational function g using its Ore action:

    r=P_J g=sum_i p_i sigma^i(g) in K.

Since P_J J=0, we have P_J F=-r. If r=0, P_J already annihilates F. Otherwise

    Q=(E-sigma(r)/r)P_J

annihilates F. Write r=h^v u with nu(u)=0. Since sigma(h)=h and sigma acts identically on the residue field,

    sigma(r)/r=sigma(u)/u is in O^times,
    (sigma(r)/r) mod h=1.

Thus the first-order factor is h-integral and has reduction L-1. Its valuation is zero, so the Gauss lemma gives nu(Q)=0 and

    bar(Q)=(L-1)bar(P_J).

Minimality means Q=R_F P_F for some Ore polynomial R_F over K. Since nu(Q)=nu(P_F)=0, multiplicativity forces nu(R_F)=0. We may therefore reduce this factorization to obtain

    (L-1)bar(P_J)=bar(R_F)bar(P_F).

If r=0, the same argument yields the stronger direct divisibility bar(P_F) divides bar(P_J). Repeating the argument from J=F+g gives the reverse divisibility in (1). Unique factorization in k[L] gives the stated multiplicity comparison. QED.

The sign of the correction is irrelevant. Zeros or poles of r at q=1 cause no problem, because they cancel from sigma(r)/r.

## 3. Regular scalar recurrences and interpretation

If P_J can be chosen monic with all coefficients in O, then the same is true of P_F. Indeed P_F can be taken as a monic right factor of the monic h-integral annihilator Q above. Both monic factors have Gauss valuation at most zero, while their product has valuation zero, so each factor has valuation zero and is h-integral. In this case both classical symbols retain their recurrence orders, and the multiplicity comparison also describes the ordinary companion-module characteristic polynomials at q=1.

The stronger primitive-symbol theorem does not require this regular cyclic basis. It avoids replacing a nonzero primitive specialization by an identically zero specialization caused by an avoidable common h factor.

Factors depending only on M are units over Q(M), so the theorem does not compare their chosen polynomial normalizations. If working with Laurent L, monomial L factors are also units. Geometric uses should make those conventions explicit.

## 4. Application to removing one Habiro coefficient

In the symmetric Habiro convention, the first kernel is

    C_(N,1)=q^N+q^-N-q-q^-1.

Thus subtracting

    g(q,M)=H_1(q)(M+M^-1-q-q^-1)

removes the first cyclotomic coefficient. For an actual reduced colored Jones sequence this gives F_1=F_2=1 and retains the higher Habiro coefficients. The correction is rational, indeed Laurent when H_1 is Laurent, so the theorem applies: it cannot erase any non-L-1 factor of the original h-primitive minimal recurrence symbol.

This supplies an exact limitation of a formal propagation argument: preserving an AJ-type classical symbol away from L=1 does not, by itself, force the fundamental-color sequence to be nontrivial. The modified sequence need not be the colored Jones sequence of any knot. Its MMR/Alexander realizability, diagrammatic realization and other constraints must be checked separately; this Ore argument does not supply them.

More generally, for any fixed r, subtracting sum_(k=1)^r H_k(q) C_(N,k) is a rational color correction: each C_(N,k) is a Laurent polynomial in q and M=q^N. The resulting formal sequence has F_N=1 for every 1<=N<=r+1, retains all H_k for k>r, and has exactly the same primitive classical factors away from L-1. Thus even an arbitrarily long finite initial segment of unit colors can coexist formally with the original non-L-1 recurrence factors. This extension does not assert preservation of the MMR diagonal or any actual-knot realization condition.

If an external AJ theorem or hypothesis identifies the original primitive symbol with a geometric A-polynomial up to the customary factors, then the modified formal sequence retains those nonabelian polynomial factors. It does not acquire a knot exterior, peripheral representation variety or geometric AJ interpretation merely by retaining that algebraic shadow.
