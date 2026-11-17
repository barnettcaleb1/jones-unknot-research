# C4: a marked persistent-coloring gate for several replacement sites

Date: 2026-11-03. Elementary local proof; no CX-H2 corner, Jones, or coloring computation performed. This is a necessary design condition, not a sufficient determinant-one criterion or a new counterexample.

## Exact assumptions

Fix a classical link diagram D and r disjoint marked balls, each meeting D in the identity two-string tangle, with no closed component in a ball. The outside diagram and its four marked endpoints per ball remain fixed. Replace these tangles by arbitrary diagrams of two-string tangles, with no extra closed components if the output is to be a knot. Twists, half-twists, full twists and rational tangles are included. No isotopy of the marked outside is needed.

Let p be a prime. Fox p-colorings satisfy 2 times the over-arc color = the sum of the two under-arc colors. Let

    V_p(D)=Col_p(D)/(global constant colorings),
    nu=dim_Fp V_p(D).

At site i the two identity strands have colors a_i,b_i. The functional

    d_i([c])=a_i-b_i

is well-defined on V_p(D), because adding a global constant does not change the difference. Let d=(d_1,...,d_r):V_p(D)->Fp^r.

## Persistent-coloring lemma

For EVERY simultaneous choice of replacement tangles, there is an injective linear map

    ker d -> V_p(D_replaced).

Proof: if d_i=0, both identity strands at site i have one common color c_i. Therefore all four boundary endpoints of that site have color c_i. Color every arc of the replacement tangle c_i. Every crossing then satisfies the Fox equation, and its boundary colors agree with the unchanged outside coloring. Apply this at every site.

This extension is linear and respects global constants. It is injective modulo constants: if the extended coloring is globally constant, all unchanged outside pieces have that color. Each original identity strand has endpoints on those pieces and consequently has the same color. Thus the original coloring was constant as well. In particular, a nonconstant class cannot disappear when the identity boxes are replaced.

It follows that

    dim V_p(D_replaced) >= nu-rank(d) >= nu-r.

The proof does not require rationality of the replacement. Equality of ALL FOUR endpoint colors supports the constant coloring on any classical two-string tangle. In contrast, equality of just two selected endpoints of an arbitrary NONidentity baseline tangle is not enough. Such a baseline can carry internal colorings invisible at its boundary. For that generalization one must work with the actual outside-restriction space and retain nonconstancy outside, rather than use the full baseline coloring dimension without checking injectivity.

## Homological interpretation and EKT specialization

Reduced Fox p-colorings identify with Hom(H_1(Sigma_2(L);Z),Fp). Hence if

    H_1(Sigma_2(L);Z)=Z^beta direct-sum T,

then nu=beta plus the number of invariant factors of T divisible by p. A knot K has a nonconstant p-coloring exactly when p divides det(K)=|H_1(Sigma_2(K);Z)|.

For the stated baseline H(3,-3), assuming the banked integral calculation

    H_1(Sigma_2)=Z direct-sum Z/13,

we have nu_13=2. With two identity sites, determinant-one feasibility therefore requires

    rank_F13(d_1,d_2)=2.

If the two difference functionals are dependent, their joint kernel contains a nonzero reduced coloring. That SAME outside coloring survives every half/full twist and every rational replacement at both sites. Every knot member then has determinant divisible by 13 and cannot be Jones-unit.

For implementation, choose two reduced baseline coloring representatives f_1,f_2 by fixing one outside arc to color zero. Form the 2-by-2 matrix with entry d_i(f_j). Its determinant must be nonzero modulo 13. Changing basis or reversing either site's strand order does not affect this rank condition. No entries of this matrix have been computed here.

With r sites the necessary condition is that d be injective; in particular r>=nu. If r>nu, it is full column rank that is necessary, not independence of every row. Passing this test merely removes the persistent-coloring obstruction. It does not establish determinant one, nontriviality, Jones equality, or geometric independence of the sites.

## Relation to the existing one-site obstruction

For one site and nu_13=2, rank d<=1 automatically leaves a nonzero kernel. This recovers the MOD-13 CONTENT of the banked one-site torsion obstruction. It is a marked, computable refinement for several sites, not a new mechanism for defeating the integral homology obstruction. It does not replace stronger integral divisibility information.

Equivalently, in the double branched cover, replacing a rational two-string tangle changes a solid-torus filling. One new filling slope can remove at most one mod-p homology dimension. The difference functionals identify a subspace of baseline classes that survives every filling choice at the marked sites. Their joint rank is the useful placement-sensitive datum.

Primary source for the standard coloring/cover identification: Jozef H. Przytycki, *3-coloring and other elementary invariants of knots*, arXiv:math/0608172, Theorem 3.3 and Corollary 3.12 (printed pp.15 and 19). His elementary boundary-monochromatic subspace argument appears on printed p.5; the marked r-site extension above follows directly from the same Fox crossing equation.

https://arxiv.org/pdf/math/0608172

## Placement existence in a connected projection

Assume the entire underlying projection graph is connected, including any crossing-free circle components. For each crossing c, choose one incident over-strand half-edge and an ADJACENT incident under-strand half-edge. The two chosen half-edges lie on one side of a sufficiently small crossing neighborhood. A still smaller ball, away from the crossing itself, contains short pieces of just these two strands. Its diagram has no crossings and can be straightened to the identity two-string tangle, with its ports marked accordingly. This is a geometric choice of adjacent half-edges; it does not require an orientation or an intrinsic notion of incoming strands. Starting with disjoint crossing neighborhoods makes all the resulting boxes disjoint.

Define d_c to be the over color minus the color of that chosen under half-edge. If d_c=0, the Fox relation 2o=u_1+u_2 forces the OTHER under color also to equal o. Thus all four incident half-edge colors agree at that crossing. Vanishing of every d_c consequently makes the coloring constant on the connected projection graph. Hence the common kernel of the d_c on V_p(D) is zero, and these functionals span V_p(D)^*.

It follows that nu=dim V_p(D) independent marked sites can always be selected at distinct crossings. If a specified crossing c_0 has d_(c_0) nonzero, its functional can be extended to such a basis using other crossings.

For a TWO-component baseline, suppose c_0 is a mixed crossing and d_(c_0) is nonzero. The two arcs in its identity box lie on different baseline components. Replacing I by one half-twist means replacing the endpoint pairing by the two-strand braid transposition; this reconnects those two components into a single component. This endpoint-permutation change is essential: merely changing which strand passes over at an existing crossing would not change component number. Keeping that fixed odd half-twist and adding arbitrary full twists at the selected sites preserves the resulting one-component endpoint pairing. Therefore every parameter member of that family is a knot.

In particular, when nu_13=2, a mixed crossing with nonzero difference can be selected together with one other independent crossing difference. The marked persistent-coloring obstruction is then removed for the two-site family after a fixed odd half-twist at the mixed site. This does NOT prove determinant-one feasibility or any Jones identity. It also does not assert that every connected two-component projection has a mixed crossing whose difference functional is nonzero; that additional condition remains to be checked for the actual diagram.
