# A DGW route to Morita's homomorphism: the exact descent gate

2026-11-03. Bounded mechanism check. No lane files or collaboration board were edited. This is not a faithfulness investigation.

## Inputs and verdict

**Follow-up in this same pass:** `g2_density_gate.md` verifies the representation-specific hypotheses left conditional below. The normalized W(6,0) Gram form gives an SU(2,3) interval starting at the trivial Torelli specialization; Kasahara's first-order image gives generic SL5 Zariski density, and infinite-order elliptic twists give topological density at nearby transcendental parameters. Thus the parameter-path lift of Section 3 kills the generic kernel, but the additivity obstruction of Section 5 actually applies to this Jones family. The direct rotation-as-d_hat mechanism is closed on that interval.

Use the conventions in `/Users/calebbarnett/jones-lanes/g2-proof/zrho/read-casson/casson.md`: Gamma=M_2, I=I_2, N=ker(rho) intersect I, and d_hat:I->Z is Gamma-invariant with d_hat(T_c)=1 on a separating twist. The desired conclusion is d_hat(N)=0, equivalently Z_rho is infinite.

**Verdict:** a representation-derived homogeneous quasimorphism could provide an exact test, but the usual DGW construction does not itself give descent or additivity on I. These are separate requirements. The central winding number is exactly the information lost when a lifted matrix becomes the identity downstairs. Vanishing of a cocycle on a subgroup proves additivity there; it does not prove that the resulting homomorphism vanishes on the representation kernel.

The relevant primary facts are in [Funar–Pitsch, arXiv:1209.0302v2](https://arxiv.org/html/1209.0302v2): Definition 4.1 and Proposition 4.2 place the real DGW invariant on a universal covering group, while Proposition 4.5 recovers only its value modulo Z from the matrix. Lemma 5.3 and Proposition 5.4 explicitly use nonzero invariant homomorphisms on representation kernels. Their central-extension and genus hypotheses must not be silently transferred to generic Jones rho in genus two.

## 1. Exact central-winding lemma

Let r:I->G be a representation into a connected Hermitian Lie group with central covering

    1 -> <z> ~= Z -> G_tilde -> G -> 1.

Let Phi:G_tilde->R be a homogeneous DGW quasimorphism normalized by Phi(z)=1. Suppose a homomorphic lift r_tilde:I->G_tilde has been specified. Put Q=Phi o r_tilde.

For x in ker(r), write r_tilde(x)=z^(omega(x)). Then omega is an integer-valued homomorphism on ker(r), invariant under any conjugations for which the lift is equivariant, and

    Q(x)=omega(x).                                       (1)

Moreover,

    Q descends to r(I)  iff  omega is identically zero.   (2)

**Proof.** Kernel images lie in the central covering subgroup, so their integer exponents add. A homogeneous quasimorphism is exactly additive on commuting pairs: apply the bounded defect to powers and divide by the power. Thus Q(yx)=Q(y)+omega(x) for x in ker(r). This proves both directions of (2).

If r starts only projectively, resolving that projective ambiguity is an additional source central extension. A function on that extension must first vanish on its source center to descend to I, and then satisfy (2) to descend to the matrix image. These steps cannot be conflated.

In extension language, a lift killing ker(r) is precisely a splitting over the discrete image r(I) of the pulled-back covering extension. A lift on I alone is insufficient. Indeed I is free, so lifts of r|I exist without solving the image-descent problem; two such lifts differ by a homomorphism I->Z. An arbitrary separating-twist calibration can therefore encode a chosen character rather than recover information from rho. For the trivial representation on I, the lift x->z^(d_hat(x)) gives Q=d_hat although every matrix is the identity. This is a countermodel to the claimed implication from a lifted formula to downstairs factorization, not a statement about a lift of all M_2.

## 2. Exact additivity criterion after descent

Suppose Q is a Gamma-invariant homogeneous quasimorphism on I that already kills N. Then it is a function of the generic Jones image. Let delta Q be its bounded defect cocycle.

**Lemma.** The following are equivalent:

    [delta Q]=0 in H_b^2(I;R);
    Q is a homomorphism on I.

If they hold and Q(T_c)!=0, then

    Q=Q(T_c) d_hat,

so d_hat kills N and Z_rho is infinite.

**Proof.** Vanishing in bounded cohomology supplies a bounded function b with delta Q=delta b. Hence Q-b is a homomorphism H. For each x and positive integer k,

    |k(Q(x)-H(x))|=|Q(x^k)-H(x^k)|<=sup|b|.

Divide by k to obtain Q=H exactly. Gamma-invariance and the fact that separating twists generate I and form one Gamma-conjugacy class then give the stated multiple of d_hat. The converse is immediate.

This lemma identifies a missing theorem; it does not prove the required bounded-cohomology vanishing. Ordinary cohomological triviality is much weaker, particularly because I is free. Nor does matching Q on separating twists prove additivity on their products. A single nonzero defect Q(xy)-Q(x)-Q(y) for x,y in I kills the claim that this particular homogeneous Q equals a nonzero multiple of d_hat.

The classical Meyer cocycle vanishes on Torelli because its symplectic representation is trivial there. A generic Jones representation is not trivial on Torelli. Therefore this vanishing cannot simply be transferred to its pulled-back DGW cocycle.

## 3. A conditional repair for the GENERIC kernel

There is one concrete way to solve the central-winding problem for the generic kernel, without solving it for a fixed root-of-unity image.

**Parameter-lift lemma.** Suppose a connected parameter interval supports representations r_t:I->G into one fixed Lie group G, continuously in t, with r_0(I)=1. Suppose they are specializations of generic rho, so rho(x)=1 implies r_t(x)=1 throughout the interval. Then the paths

    s |-> r_(s t)(x),       0<=s<=1,

define a homomorphic lift r_t_tilde:I->G_tilde. Every element of N has the constant identity path, hence maps to the identity in G_tilde. Consequently Q_t=Phi o r_t_tilde kills N exactly.

If the family extends equivariantly to Gamma, conjugation invariance of Phi gives Gamma-invariance of Q_t. The lemma then leaves exactly the additivity/nonzero-value gate of Section 2.

This statement requires an actual continuous family into a fixed group, including a valid trivial endpoint on I. A degenerating invariant Hermitian form or a singular change of basis cannot be ignored. Those hypotheses were not verified here for the Jones family. At a transcendental parameter, equality of rational-function matrices may identify the specialized kernel with the generic one; at a root of unity it generally does not.

Thus this is a precise possible mechanism, not a factorization result already obtained. Even with the parameter lift, the DGW pullback is initially only a quasimorphism. No argument here turns its bounded defect class into zero.

## 4. A cheap fixed-specialization kill criterion

If a specialization r_zeta sends a separating twist T_c to an element of finite order m, no homogeneous real-valued quasimorphism on the **matrix image** can pull back to c d_hat with c!=0. Homogeneity forces its value at r_zeta(T_c) to be zero, whereas d_hat(T_c)=1.

Equivalently, T_c^m is in the specialized kernel and has d_hat=m. A nonzero lifted DGW value on this element records central winding and therefore fails descent to that specialized matrix image. This is consistent with Funar–Pitsch's use of kernel homomorphisms; it is not an objection to their construction.

The test does not kill the parameter-lift route for the generic representation: a root-of-unity identity need not be a generic identity. It does kill an argument that substitutes one finite-order specialization for generic rho and treats a real rotation lift as a matrix-only invariant.

## 5. A conditional density criterion that kills exact additivity

**Lemma.** Let G=SU(p,q), p,q>0, and let r:I->G have real-Zariski-dense image. Suppose r(I) contains an elliptic element of infinite order, so its powers have infinite compact closure. Then r(I) is topologically dense in G. For every homomorphic lift r_tilde:I->G_tilde, the pullback of a nonzero continuous homogeneous DGW quasimorphism Phi is **not** a homomorphism on I.

An irrational eigenangle suffices here only with the ellipticity/precompact-powers condition. The lemma does not infer compact powers from an irrational angle on one eigenvalue of an otherwise hyperbolic matrix.

**Proof of base density.** Let C be the topological closure of r(I). The infinite compact cyclic closure contains a positive-dimensional torus, so the Lie algebra c of C is nonzero. It is invariant under Ad(r(I)). The stabilizer of a linear subspace in the adjoint representation is real algebraic, so Zariski density makes c invariant under Ad(G). The Lie algebra su(p,q) is real simple; hence c=su(p,q). Since G is connected, C=G.

**Proof that the lifted image is dense.** Put C_tilde=closure(r_tilde(I)) and let Z be the central kernel of G_tilde->G. Its dense projection implies C_tilde Z is dense in G_tilde. The closed subgroup C_tilde is normal in C_tilde Z, because Z is central. Its normalizer is closed, so C_tilde is normal in G_tilde. Simplicity of the Lie algebra makes its Lie algebra either zero or all of g. In the zero case C_tilde is a discrete normal subgroup of the connected group G_tilde, hence central; its projection lies in the finite center of G and cannot be dense. Thus C_tilde=G_tilde.

**Proof of the obstruction.** If Phi o r_tilde were additive on I, the continuous defect

    Phi(xy)-Phi(x)-Phi(y)

would vanish on the dense subset r_tilde(I) x r_tilde(I), hence everywhere on G_tilde x G_tilde. Phi would be a continuous homomorphism G_tilde->R. Such a homomorphism is zero because the Lie algebra is semisimple and the group is connected. This contradicts Phi(z)=1. QED.

Therefore, whenever these density and ellipticity hypotheses are verified for a proposed Jones specialization, the bounded defect class in Section 2 is necessarily nonzero. It rules out this fixed DGW pullback as a nonzero multiple of d_hat, including a parameter-path lift that already solves the generic-kernel descent issue. The needed generic-density and elliptic-twist inputs were **not** checked in this pass; this is a conditional kill criterion, not a claim about the lane's representation.

## Stop condition

The density verification in `g2_density_gate.md` rules out exact additivity for this fixed-parameter DGW pullback, even after the parameter lift repairs generic-kernel descent. Therefore do not continue trying to identify that pullback with a nonzero multiple of d_hat. A different construction, such as a justified combination with cancelling defects or a discontinuous arithmetic character, would be a new route requiring its own mechanism. Neither d_hat factorization nor Z_rho=infinity is established here.
