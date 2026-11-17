# Satellite gate: universal Jones preservation cannot manufacture unknotting number one

2026-11-03. Bounded theory pass; no enumeration. Status: direct deductions from standard satellite topology and the cited theorems, offered for independent review. No novelty claim.

## 1. The strongest short obstruction needs only a2

**Proposition.** Let P be a fixed oriented knot pattern in a solid torus, with P(U)=U. Suppose V(P(K))=V(K) for every knot K. Then its algebraic winding number is w(P)=+1 or -1. If P is not isotopic to the core, then for every nontrivial K,

    u(P(K)) >= 2.

Consequently no such noncore pattern turns a hypothetical nontrivial Jones-trivial knot into an unknotting-number-one knot. The core pattern returns K, up to orientation, and supplies no reduction either.

**Proof.** With normalized Jones convention V(U)=1, one has V''(1)=-6 a2, where a2 is the z^2 Conway coefficient. Thus Jones equality implies a2 equality. The satellite Alexander identity

    Delta_(P(K))(t) = Delta_(P(U))(t) Delta_K(t^w)

gives, by expanding at t=1,

    a2(P(K)) = a2(P(U)) + w^2 a2(K).

Apply this only to K=trefoil, for which a2=1. The hypotheses give w^2=1. In fact preservation of Jones on just U and the trefoil suffices for this winding conclusion.

For nontrivial K, let T=boundary N(K) be the companion torus of P(K). On the outside, T is incompressible because K is nontrivial. On the pattern side, a compression would provide a meridian disk of the solid torus missing P, impossible when w is nonzero. Thus T is incompressible. If T were parallel to the boundary of the satellite exterior, the intervening pattern exterior would be T^2 x I, making P a core. Hence noncore P gives an essential companion torus. Scharlemann--Thompson, Corollary 3.3, excludes unknotting number one for a satellite of nonzero winding. This proves the claim.

The Scharlemann--Thompson input is precisely the nonzero-winding statement, not a statement that all satellite knots have unknotting number at least two. Winding-zero Whitehead patterns are the familiar exception to that broader false claim.

Primary references: [Scharlemann--Thompson, *Unknotting number, genus, and companion tori*, Math. Ann. 280 (1988), 191--205, DOI 10.1007/BF01456051](https://doi.org/10.1007/BF01456051); its exact Corollary 3.3 is explicitly restated in the introduction of [Hom--Lidman--Park, *Unknotting number and cabling*](https://preprint.press.jhu.edu/ajm/sites/default/files/AJM-hom-lidman-park.pdf). The original paper's [Corollary 4.5](https://gdz.sub.uni-goettingen.de/fulltext/PPN235181684_0280/00000207?_format=xml) also states the extension to attaching an integer-twisted band and identifies one twist with Corollary 3.3. The original 3.3 page itself was not recovered in this bounded pass; the exact citation and statement were checked in the primary modern paper.

## 2. A skein version needs no universal preservation hypothesis

The solid-torus Kauffman bracket skein module R[z], R=Z[A^{+/-1}], is graded by H1(solid torus; Z/2). Each smoothing preserves this mod-2 homology class. The core z=e1 is odd.

Therefore, if the actual annular bracket of a knot pattern is a nonzero scalar times e1, its winding is odd and in particular nonzero. If the pattern is noncore, the same topological proof gives u(P(K))>=2 for every nontrivial K. This version works even when one has only the scalar-core skein certificate, not a statement about all normalized Jones polynomials. A framing unit does not change the grading.

Conversely, winding-zero unknotting patterns necessarily live in the even part of the annular skein. This explains structurally why Whitehead-style reductions read even colors, starting with e0 and e2, rather than copying the ordinary e1 Jones invariant.

## 3. Universal Jones preservation also forces scalar-core skein (root's strengthening)

Here use zero-framed companions and the pattern framing induced from P(U); P(U)=U fixes its normalization. Expand the annular skein class in the integral Chebyshev basis:

    [P] = sum_n p_n(A) e_n.

On a zero-framed companion K, its bracket evaluation is

    sum_n p_n(A) Delta_n(A) J_(n+1)(K),

where J_N is reduced colored Jones, J_N(U)=1, and Delta_n is nonzero. If this functional equals the core functional on every K, set K_r to the connected sum of r trefoils. Multiplicativity gives J_N(K_r)=lambda_N^r, where lambda_N=J_N(trefoil). These lambda_N are pairwise distinct: their expansions at q=e^h have quadratic coefficients proportional to N^2-1, with nonzero proportionality constant because a2(trefoil)=1. Equivalently, the k=1 Habiro term starts with (N^2-1)h^2, while terms k>=2 start at order at least four.

For the finite set of colors appearing in [P] together with e1, the equations at r=0,...,d-1 form a Vandermonde system over Q(A). Its determinant is nonzero, so all coefficients other than that of e1 vanish and the e1 coefficient is 1. A fixed framing unit on the functional gives the same unit times e1. Thus scalar-core is not an extra assumption for a fixed universally Jones-preserving framed pattern.

This separation argument uses finitely many colors for each fixed P, not a claim that a fixed finite set of Jones evaluations detects every knot. It is stronger algebraically than Section 1, but unnecessary for the unknotting-number obstruction.

## 4. A fixed nonzero-winding pattern cannot force strong inversion universally

There is a separate JSJ obstruction, already at ordinary invertibility.

**Lemma.** Suppose P has nonzero winding, K is hyperbolic and noninvertible, and E(K) is not homeomorphic to any hyperbolic JSJ piece of the fixed pattern exterior. Then P(K) is not invertible. If P is a core, this conclusion is immediate; otherwise the companion torus is essential as above.

**Reason.** The hyperbolic piece E(K) remains a JSJ piece after gluing, and its homeomorphism type occurs uniquely. Any orientation-preserving symmetry of the satellite can therefore be isotoped to preserve E(K), its boundary, and the complementary solid torus V. If that symmetry reverses the satellite knot, then in H1(V)=Z the equation [P]=w[core], w!=0, forces the generator to be reversed. The induced map of V preserves the meridian slope and reverses the core orientation; after an isotopy of V it carries the core to itself. Gluing it to the map of E(K) produces an orientation-preserving homeomorphism of S3 reversing K, a contradiction.

A fixed pattern has finitely many hyperbolic JSJ pieces. There are infinitely many pairwise distinct asymmetric hyperbolic knots in S3, so one can choose K as in the lemma. Published constructions are in [Baker--Luecke, *Asymmetric L-space knots*, Geometry & Topology 24 (2020), 2287--2359](https://msp.org/gt/2020/24-5/gt-v24-n5-p02-p.pdf); an explicit infinite family is also [Baker--Teragaito, Theorem 1.1](https://arxiv.org/abs/2510.07618). Thus a fixed nonzero-winding pattern cannot send all knots to invertible, and hence cannot send all knots to strongly invertible, knots.

The symmetry-gate sibling independently read this proof and agreed, with the uniqueness and peripheral-extension hypotheses kept explicit. Its equivalent homological check is that inclusion sends mu_K to w mu_sat in H1 of the satellite exterior; reversal of mu_sat and w!=0 forces reversal of mu_K.

Scope: this does NOT show that a fixed pattern fails on the hypothetical V=1 fiber specifically. Its asymmetric companions above need not have V=1. The unknotting-number obstruction in Section 1 is stronger in this respect: it applies to every nontrivial input, including that hypothetical fiber.

## 5. Consequence for the project

There is no universal fixed-pattern Jones-preserving satellite shortcut from the general unknot conjecture to its unknotting-number-one slice. It fails for a topological reason before the full polynomial matters. A proposed construction must relinquish universal Jones preservation, fixed-pattern satelliting, or the u=1 target.

The known universal strong-inversion construction K#K^r is different: the inversion exchanges two separate summands. The archived last section of work/defect-calculus/sums.txt says its quotient flatness is H3(K)=1, whereas its ordinary Jones polynomial is V(K)^2. Hence Jones-trivial input makes its ordinary polynomial trivial, but does not supply the color-three identity needed to invoke Lemma Q. This precise gap remains; the present obstruction does not close it.

No claim is made that every operation preserving only the V=1 fiber has scalar-core skein or winding +/-1. Universal preservation on all companions was essential in Sections 1 and 3.
