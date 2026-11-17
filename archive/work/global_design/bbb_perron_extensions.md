# Limits of the Perron argument and an exact cone-certificate target

2026-11-03. Supporting the Burau_4 target underlying BBB-MULTISET. The two counterexamples and cyclic matrix identities have independent internal reads. UPDATE173602: the finite full-dimensional semialgebraic implementation of the conditional certificate below is impossible at every rational t>2; see bbb_cone_obstruction.md. The abstract sufficient inclusions remain valid. No novelty claim.

## 1. Positive re-entry does not produce a positive-fraction normal form

Use x=A_14,y=A_24,z=A_34 and the v_i coordinates of BBB-PERRON. Put delta=xyz. Direct multiplication gives

    rho(delta)=t I+t(t-1)(t²,t,1)^T(1,1,1).

The matrix rho(delta y^-1) is strictly positive for every real t>1. Its only potentially problematic row, the second, simplifies to

    ((t-1)²,  t-1+t^-1,  (t-1)²(t²+1)/t).

The other rows are positive directly from the displayed rank-one formula and

    (1,1,1) R_y^-1=(1/t, t^-2, (t²-t+1)/t²).

For example at t=3 it is exactly

    [21    6      42   ]
    [ 4    7/3    40/3 ]
    [ 2    2/3    23/3 ].

Consequently w=(xyz y^-1)^2 has a strictly positive matrix. This actual free word is cyclically reduced and has four cyclic sign runs. It is neither P Q^-1 nor Q^-1 P with P,Q positive, since reduction of either such expression leaves at most two cyclic sign runs. Nevertheless it takes the ENTIRE nonnegative cone minus zero into the strictly positive cone.

This is not Brunnian. It refutes the proposed unrestricted inference from re-entry to a two-run normal form; it does not refute any Brunnian-specific restriction or BBB-MULTISET.

## 2. Four sign runs do not bound the genus of Brunnian words

For n>=1 let

    B_n=(xy)^n (yx)^-n (zyx)^n (zxy)^-n.

This is a cyclically reduced word of length 10n with exactly four cyclic sign runs. It is Brunnian in the canonical point-pushing group: deleting x or y cancels the first two and last two factors separately; deleting z cancels the middle factors followed by the outer factors. Deleting strand4 kills the whole word.

Define a counting function on reduced free words by

    q(w)=number of xyz subwords minus number of z^-1 y^-1 x^-1 subwords,

counting overlaps. It is antisymmetric under inversion and has defect at most 6. To prove the bound, write a=a_0 c and b=c^-1 b_0 with maximal cancellation. At each of the three seams a_0|c, c^-1|b_0, and a_0|b_0, at most two length-three windows cross the seam. The c contributions cancel, so |q(ab)-q(a)-q(b)|<=6.

It follows that a single commutator has |q|<=18, by multiplying its four factors and using three defect bounds. A product of r>=1 commutators has |q|<=18r+6(r-1)=24r-6.

For B_n, neither positive block contains xyz. Only its last negative block, (y^-1 x^-1 z^-1)^n, contributes, giving q(B_n)=-(n-1). Therefore

    cl(B_n)>=ceil((n+5)/24).

In particular B_20 is not a single commutator, nor a conjugate or inverse of one, inside the free group K. Thus the proposed reduction of every four-run Brunnian word to [g,H], with H positive and g a positive fraction, is false even without either positivity restriction on the commutator factors. All commutator lengths and conjugacies in this section are in K; no claim about arbitrary B_4 commutator factorizations is made. The argument is a basic counting-quasimorphism argument and claims no novelty for that technique.

No assertion B_n in BI_4 is made. A further hypothesis rho(B_n)(-1)=I has not been imposed or checked. The counterexample kills the attempted Brunnian-only classification, not a classification using that extra condition.

## 3. Cyclic symmetry reduces the three matrices to an explicit free-product question

Set

    C=[0 0 t^-1; 1 0 0; 0 1 0],
    R=R_1=[t² t-1 t-1; 0 1 0; 0 0 1].

Then, exactly,

    C³=t^-1 I,   C R_i C^-1=R_(i+1 mod3),
    RC=[t-1 t-1 t; 1 0 0; 0 1 0],
    char_C(s)=s³-t^-1,
    char_(RC)(s)=(s-t)(s²+s+1).

Thus R,C define a projective representation of G=Z*C_3. Its index-three subgroup F=ker(G -> C_3), killing the infinite cyclic generator, is free on a,cac^-1,c²ac^-2. These map to the three canonical R_i.

Projective injectivity on F is equivalent to projective injectivity on G. For the nontrivial direction, any kernel element has cube in F, so injectivity on F makes that cube trivial. A nontrivial torsion element of a free product is conjugate to c or c², and neither is killed by C.

For the GENERIC representation, projective and ordinary kernels on F agree. If a word W(t)=lambda(t)I, differentiate at t=1. Since R_i(1)=I, every off-diagonal entry in row i of W'(1) is the exponent sum e_i of the corresponding free generator. Scalarity makes all e_i zero. Then det W=t^(2 sum e_i)=1 gives lambda³=1, hence lambda=1 in Q(t). The unreduced invariant vector alone would not establish this assertion about scalars on the reduced summand.

Consequently a proof of this explicit projective free-product representation's generic injectivity proves injectivity on K. The banked Long/Brunnian reduction then proves generic Burau_4 faithfulness. This is not a proof of Jones unknot detection; Burau_4 faithfulness is only a necessary rung in that problem.

## 4. A finite sufficient certificate

Fix one rational t_0>2. In RP² seek nonempty domains X_+,X_-, put X=X_+ union X_- and Y=CX union C²X, and prove

    X intersect Y is empty,
    RY subset X_+,       RX_+ subset X_+,
    R^-1Y subset X_-,    R^-1X_- subset X_-.

These imply R^nY subset X for every nonzero integer n, and C^jX subset Y for j=1,2. Free-product ping-pong gives projective injectivity of G at t_0. A generic kernel word would also be killed at t_0, so this single certificate would settle generic Burau_4 faithfulness via section3.

If the domains were finite unions of projectivized rational polyhedral cones, a sufficient certificate would consist of finitely many exact ray-containment and cone-disjointness checks, assigning each image cone to one destination cone. UPDATE173602: bbb_cone_obstruction.md proves that no nonempty open semialgebraic X_- can meet these inclusions at any rational t>2. This includes finite unions of full-dimensional polyhedral cones and does not require individual image-cone assignments. The general domain-existence question remains open here, but this proposed finite implementation is closed.

C and RC are companion matrices whose difference has rank one. This places the explicit matrices in the hypergeometric-monodromy framework. The Burau/hypergeometric connection is established prior art, for example [Venkataramana, Image of the Burau representation at d-th roots of unity](https://annals.math.princeton.edu/2014/179-3/p04). Related finite cone constructions for a different three-dimensional hypergeometric group appear in [Frieden–Gélinas–Soucy, Cones and ping-pong in three dimensions](https://arxiv.org/abs/2111.14692). Neither result supplies the domains above or proves their existence.

## Scope

BBB-PERRON remains valid. The two proposed automatic extensions are ruled out at their stated scopes. The finite-domain implementation is also ruled out by the subsequent theorem; the conditional free-product criterion is not a new faithfulness theorem. BBB-MULTISET remains held and OPEN, and Claude's geometric push construction has not been duplicated.
