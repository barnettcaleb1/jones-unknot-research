# Quantum information and reflection positivity: a focused audit

Outcome: no generic unknot-detection proof or counterexample. This pass produced a precise no-go statement for using only the fundamental long-knot operator, a conditional detection theorem using all cable trace closures, and two explicit checks showing why the missing information cannot simply be assumed.

## 1. The unknot value is an interior quantum amplitude

Fix a unitary root with d=-A^2-A^-2>1 and let Omega be the normalized state made from m disjoint cups. A 2m-strand plat braid beta gives a unitary U_beta, and, up to a framing phase,

    V(plat(beta)) = d^(m-1) <Omega,U_beta Omega>.

This follows directly by closing the cup state, whose unnormalized squared norm is d^m. It is the path-model quantum computation of the Jones polynomial in [Aharonov--Jones--Landau](https://arxiv.org/html/quant-ph/0511096).

Consequently V=1 gives overlap magnitude d^(1-m), not1. Cauchy--Schwarz only implies U_beta Omega is proportional to Omega when the magnitude is1. The same issue appears for an n-strand trace closure, where the normalized Markov trace is d^(1-n) when V=1. Increasing the number of roots does not change this normalization at any one root.

## 2. Two actual unknot diagrams already defeat the proposed reflection saturation

Take four-strand plats beta_+=sigma_2 and beta_-=sigma_2^-1. Each plat is the actual unknot. In the convention U_+=A I+A^-1 e_2 and U_-=A^-1 I+A e_2, the normalized cup state satisfies

    <Omega,e_2 Omega>=1/d,
    <Omega,U_+ Omega>=-A^3/d,
    <Omega,U_- Omega>=-A^-3/d.

After correcting their framing phases, both amplitudes are1/d. However, their state overlap, before an irrelevant unit phase, is

    <U_+ Omega,U_- Omega>
      = <Omega,U_-^2 Omega>
      = A^-2+(1-A^4)/d
      = -(A^4+A^-4)/d.

At A=i exp(-pi i/10), d=phi=(1+sqrt(5))/2 and the overlap has magnitude phi^-2<1. The two-state reflection Gram determinant is1-phi^-4>0. Thus even two genuine unknot presentations with identical Jones polynomial at every parameter need not give the same normalized cap state or saturate a reflection inequality against each other. The reflected relative closure carries additional information about the presentations.

One also cannot assume |V_K|>=1 at unitary roots as a shortcut to a sum-of-squares argument. Exact TL calculation for the figure-eight braid sigma_1 sigma_2^-1 sigma_1 sigma_2^-1 gives

    V_4_1(t)=t^-2-t^-1+1-t+t^2=Phi_10(t)/t^2,

which is zero at a primitive tenth root. Thus |V|^2-1 need not be nonnegative.

## 3. A black-box no-go lemma

Cut a zero-framed knot K at one small unknotted arc and regard the remainder as a long knot T_K. In the fundamental SU(2) skein category, the single-strand endomorphism space is one-dimensional. Equivalently, Schur's lemma for the fundamental simple object gives

    RT(T_K)=V_K I.

Any network assembled from fixed braids, cups, caps and individual uses of this fundamental long-knot operator therefore depends on K only through V_K (and V_K with inverted variable if reflected copies are allowed). Multiple independent uses, tensoring, interference, and reflection do not recover information that this scalar operator has already discarded. In particular, if V_K=1 then such networks already see T_K as the identity in the skein quotient. Positivity is faithful on that quotient, not on the set of geometric tangles before quotienting.

The geometric zero-framed two-parallel of K is a different operation. It cables every crossing and can access the three-dimensional representation in the fusion rule2 tensor2=1 direct-sum3. It is not the same as two independent insertions T_K tensor T_K. Cabling is not determined by the one-strand skein class.

## 4. Exact knot example: full ordinary Jones equality, different two-copy data

The certificate `quantum_two_copy_test.py` uses the explicit table braid presentations

    5_1:    [-1,-1,-1,-1,-1],
    10_132: [-1,2,-3,-2,3,-4,3,-2,1,-3,2,-3,4,-3,-3,-2].

The names are not needed for the algebraic claim: these explicit braids both have connected closures. Their full ordinary Jones polynomials, computed by the exact Temperley--Lieb engine, agree:

    V(A)=A^8+A^16-A^20+A^24-A^28.

For the normalized spin-one/three-dimensional colored invariant, the [Jackson--Kerler R-matrix](https://arxiv.org/html/0912.2114), equation23 with s=q^2, gives at the quantum-group parameter q=2:

    H_3(5_1)=208357048576,
    H_3(10_132)=12565016366179/4.

The computation uses exact rational arithmetic and a quantum trace over the full tensor power, separated only into invariant weight spaces for efficiency. The normalization factor is [3] q^(2w), with [3]=q^2+1+q^-2. Tests include both signs of Markov stabilization, including stabilization of the actual nontrivial five-strand example. The q here is the square root of the ordinary Jones variable, up to mirroring; the same convention is used for both knots.

This explicitly disproves any universal inference from the entire ordinary Jones polynomial to the first colored/cable invariant. It does not disprove a special rigidity theorem restricted to the fiber V=1.

## 5. A correct conditional theorem: all cabled maximal traces do detect braid identity

[Freedman--Walker--Wang, Theorem5.1](https://arxiv.org/html/math/0209150) proves that every nonidentity braid has some cabling on which the SU(2) Jones representation is nontrivial. Combining it with positive-trace extremality gives:

**Conditional theorem.** Let h be an unframed braid. Suppose that for every blackboard braid cabling c(h) on N strands, as in the cited theorem and without added internal twists, the ordinary Jones polynomial of its trace closure is exactly d^(N-1), the N-component unlink value. Then h is the identity braid.

Proof: Fix a cabling. For A in a sufficiently small unitary arc near i, the fixed finite TL_N trace tau is faithful and positive. For the writhe-corrected unitary operator R, the hypothesis gives tau(R)=1, hence

    tau((R-I)^*(R-I))=2-2 Re tau(R)=0.

Thus R=I on the arc and hence as a generic Laurent identity. Applying the one-dimensional character e_i->0 to R gives (-1)^w A^-2w=1 identically, forcing w=0. Therefore the uncorrected Jones operator of this cabling is also identity. This holds for every cabling, contradicting the cited theorem unless h=1.

This concerns trace closures with as many unlink components as braid strands. It says nothing contradictory about known Jones-trivial links whose braid index is larger than their component count. It also does not identify knots from an arbitrary chosen relative braid: different braids can present the same unknot, as Section2 shows.

The homology agent independently checked this corollary against Theorem5.1, including its unframed convention and separate treatment of central full twists.

## 6. Best remaining direction and its first falsifiable target

The useful connection is not a direct Cauchy--Schwarz proof. It is a **closure-to-cabling rigidity problem**: can the special hypothesis V_K=1 force any additional colored or reflected data that general Jones equality does not determine?

An exact first target is the next Habiro coefficient. In the integral cyclotomic expansion H_N=1+sum_{j>=1} C_j times the standard N-dependent factors, V_K=H_2=1 forces C_1=0. At color3 the remaining defect is a nonzero known factor times C_2. Therefore proving that an actual knot with C_1=0 must have C_2=0 would establish V_K=1 implies H_3(K)=1. Formal cyclotomic integrality alone does not do this: C_1=0,C_2=1 is algebraically consistent with the expansion but is not asserted to be realized by a knot.

The first test for any proposed positivity or reflection mechanism is therefore to express C_2 as a genuinely positive geometric quantity under C_1=0, without assuming the unobserved two-parallel data. It must survive both explicit countertests above: different unknot plat states and equal-Jones knots with different H_3. Even a successful first bridge would not itself prove unknot detection; it would supply genuinely new information that the scalar quantum oracle lacks.
