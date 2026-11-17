# Exterior reduction: a single commutator certificate and a local skein obstruction

Date: 2026-11-03. Author: Codex subagent `skein_exterior_reduction`.
Status: elementary deductions below are **TRUSTED after root's independent check**. The cited inputs are published; Claude review remains pending under the collaboration protocol. No novelty claim is made. No Jones-to-exterior comparison has been proved.

## Outcome

There is a concrete endpoint smaller than controlling an entire peripheral character variety: **annihilate one explicit commutator defect in the traceless-meridian classical skein fiber**. For a two-generator knot group this is a single quadratic trace relation. More generally one finite sum of commutator defects suffices.

A second deduction isolates an obstruction to a rank-one exterior-module route: a nontrivial knot with meridional generic skein rank one must retain a defect at the two-dimensional base point `(A+1, m)`. Finite local rank one plus reflexivity excludes that defect and forces the unknot. Generic rank one alone, or even flatness in A alone, does not.

These are endpoints and obstruction lemmas, not a newly completed route from the Jones polynomial. The ordinary rational tangle bracket has not supplied either certificate.

## 1. Setting and the published input

Let κ be a knot in S³, M its exterior, and μ a meridian. Put

\[
R=\mathbb C[A^{\pm1}],\qquad B=R[m],\qquad
S=\mathcal S_R(M),\qquad \mathfrak p=(A+1,m).
\]

Here m acts on S by adding a boundary-parallel meridian. Define the vector space

\[
F_\mu(M)=S/\big((A+1)S+mS\big).
\]

At A=-1 the skein module has its usual commutative algebra structure, and an SL₂(C) representation ρ gives an evaluation

\[
[L_1\cup\cdots\cup L_k]\longmapsto
\prod_j -\operatorname{tr}\rho(L_j).
\]

The trace identity verifies the skein relation. If tr ρ(μ)=0, this factors through Fμ. Thus Fμ is the whole **base fiber at meridional trace zero**, retaining every character over that trace. It is NOT a localization at the abelian character; the latter would discard other characters and would not work.

The essential published input is Kronheimer–Mrowka, *Knots, sutures and excision*, Corollary 7.17: a nontrivial knot in S³ has an irreducible SU(2) representation with traceless meridian. [Primary paper](https://arxiv.org/abs/0807.4891), §7.6, Corollary 7.17 (PDF p.63).

The fuller identification of classical skeins with character functions, with the appropriate scheme/reduction qualification, is due to Bullock and Przytycki–Sikora. The arguments below need only the explicit trace evaluations, so they do not require a reducedness or flatness assumption. [Bullock](https://arxiv.org/abs/q-alg/9604014), [Przytycki–Sikora](https://arxiv.org/abs/q-alg/9705011).

In Lemma Q, the actual unknot filling identifies the cover M with the actual exterior E(κ) of a strongly invertible knot in S³. That is exactly the S³ input needed here; there is no unresolved closed-summand ambiguity.

## 2. A single commutator-defect certificate

Choose finite generators g₁,…,gᵣ of π₁(M). For each i<j choose an embedded loop γᵢⱼ representing the conjugacy class of [gᵢ,gⱼ]. Its framing and representative do not affect its classical character evaluation. Define

\[
\mathcal D_G=\sum_{i<j}\big([\gamma_{ij}]+2[\varnothing]\big)
\quad\text{in }F_\mu(M).
\]

**Theorem E1.** The following are equivalent:

1. κ is the unknot;
2. D_G=0;
3. D_G is nilpotent in Fμ(M).

**Proof.** For an SU(2) representation ρ,

\[
\operatorname{ev}_\rho(\mathcal D_G)
=\sum_{i<j}\big(2-\operatorname{tr}[\rho(g_i),\rho(g_j)]\big).
\]

Every summand is real and nonnegative. A matrix in SU(2) has trace 2 exactly when it is the identity. Consequently this sum vanishes exactly when all generator images commute, equivalently when the representation has abelian image. A meridian-traceless irreducible representation supplied by Corollary 7.17 therefore evaluates D_G to a strictly positive real number. Such an element is neither zero nor nilpotent. This proves (3)⇒(1), and (2)⇒(3) is immediate. For the unknot, M is a solid torus, S=R[z] with m=z, and Fμ=C. All commutators are trivial, so every summand is zero. ∎

For r=2, there is just **one loop** and one relation. For arbitrary r, the positivity applies to this specific trace function; it is not an assertion of positivity for Jones state sums or Chern–Simons integration.

This is reminiscent of the elementary Wilson action in lattice gauge theory: a sum of commutator-holonomy penalties vanishes exactly at commuting configurations. Here gauge theory supplies the existence of a noncommuting traceless configuration. The useful mathematical content is the exact nonnilpotence certificate, not the analogy.

### A two-generator algebra certificate

Suppose π₁(M)=⟨a,b | relations⟩. Set

\[
x=\operatorname{tr}(a),\quad y=\operatorname{tr}(b),\quad
z=\operatorname{tr}(ab).
\]

The Fricke identity gives

\[
\operatorname{tr}[a,b]-2=x^2+y^2+z^2-xyz-4=:f.
\]

Let I be the actual character ideal of this presentation and let τμ(x,y,z) be the meridian trace polynomial. The sufficient certificate is

\[
f\in\sqrt{I+(\tau_\mu)}.
\]

It forces the commutator trace to be 2 on every traceless character, and hence κ=U by the preceding SU(2) argument. If a is a meridian, it is simply

\[
y^2+z^2-4\in\sqrt{I+(x)}.
\]

One can certify radical membership by a finite polynomial identity fᴺ∈I+(τμ). This is a concrete target for an exterior with a genus-two handlebody presentation. It does not require recovering its full A-polynomial. A tunnel-number-one knot need not have two MERIDIONAL generators; if μ is a word, its actual τμ must be retained. Nor does the width-six zero-surgery presentation by itself certify tunnel number one.

For calibration, the trefoil two-meridian character fiber at x=y=0 includes z=-2 (abelian) and z=1 (irreducible). At z=1 the polynomial f is -3, so the proposed certificate correctly fails. This is an illustrative hand calculation, not a census computation.

**Important limitation:** the one relation f=0 is in the exterior character/skein object. It is not implied by an equality of two coefficients in the bracket skein module of a ball. Supplying a derivation of that relation from the rational quotient bracket is OPEN.

## 3. The traceless-meridian fiber has at least two dimensions

**Theorem E2.** If κ is nontrivial, then

\[
\dim_{\mathbb C} F_\mu(E(\kappa))\ge 2.
\]

No finite-generation assumption is required; the dimension may be infinite.

**Proof.** There is a unique abelian traceless character: send the generator of H₁(M)=Z to diag(i,-i). It evaluates the empty skein to 1 and D_G to 0. An irreducible traceless SU(2) character evaluates the empty skein to 1 and D_G to a positive number. Thus the empty skein and D_G are linearly independent. ∎

Consequently, the extremely small certificate dim Fμ≤1 forces κ=U. The unknot attains dimension exactly 1.

For a finite B-module presentation Bᵖ→Bⁿ→S→0, this becomes a finite Fitting-ideal obstruction:

\[
\kappa\ne U\quad\Longrightarrow\quad
\operatorname{Fitt}_1(S)\subseteq(A+1,m).
\]

Indeed the presentation matrix at this point must have cokernel dimension at least two. Equivalently, **one (n−1)×(n−1) minor nonzero at A=-1,m=0 is enough to certify the unknot**, provided the displayed presentation really presents the entire exterior module. A presentation of the cyclic span of the empty skein is insufficient.

## 4. A local rank-one/reflexivity reduction

**Theorem E3.** Suppose the localized B-module Sₚ is finite, rank one, and reflexive over Bₚ. Then κ is the unknot.

Reflexivity includes torsion-freeness here. Equivalently one may list finite, torsion-free rank one, and the isomorphism Sₚ→Sₚ** separately.

**Proof.** Bₚ is a two-dimensional regular local UFD. A finite rank-one reflexive module over it is free of rank one: it is a rank-one divisorial fractional ideal, and every such ideal in a UFD is principal. Its residue fiber consequently has dimension one. Localizing at the base maximal ideal does not change that residue fiber, so dim Fμ=1. Theorem E2 forces κ=U. The abelian evaluation also shows the empty link is nonzero in the residue fiber; hence by Nakayama it is a basis of Sₚ. ∎

**Contrapositive.** If a nontrivial knot has a finite torsion-free meridional module of generic rank one, then its localization at (A+1,m) is not reflexive. Any attempt to promote generic rank one to unknothood must encounter this particular lattice defect.

If Sₚ is finite torsion-free rank one, the quotient Sₚ**/Sₚ is supported in codimension two and has finite length. The theorem says that it cannot vanish for a nontrivial κ. This is a precise obstruction living at a specified base point, rather than an unspecified failure of specialization.

### Why the hypotheses cannot be silently weakened

Let a=A+1. Over the regular local ring C[a,m]_(a,m), the ideal (a,m) is finite torsion-free of rank one but has a two-dimensional residue fiber. It is not reflexive: its double dual is the ring itself. It is torsion-free, and hence flat, over the one-variable PID C[a]. Thus **even A-flatness does not repair generic meridional rank one**.

An even simpler finite algebra countermodel is B×(B/ₚ), with B acting diagonally. It has generic rank one and two distinct reduced points in its exceptional residue fiber. Nilpotents are not needed for the specialization problem.

These are commutative-algebra countermodels, not asserted skein modules of knots. Their role is to falsify the invalid formal implications.

## 5. Exact open gates and relation to the archived routes

For a Lemma-Q tangle X, the following is an end-to-end conditional scaffold:

1. X has rational bracket and an actual unknot closure. **Given.**
2. Its branched cover is E(κ) for κ⊂S³. **Established topological input.**
3. The exterior meridional skein module localized at (A+1,m) is finite of rank one. **OPEN GATE 1.**
4. That module is reflexive, so no codimension-two defect survives. **OPEN GATE 2, independent of Gate 1.**
5. E3 makes κ the unknot. **Deduction above.**
6. X is rational. **Usual equivariant solid-torus classification in the Lemma-Q setup.**

Alternatively replace steps 3–4 by the single exterior relation of E1, or the explicit two-generator radical certificate. That replacement is a smaller algebraic target, but deriving it from the bracket is still OPEN. It is not evidence that the target follows.

The known calculation of skein modules over meridian polynomial rings for two-bridge and torus knots shows that this type of module is a real computational object. General finite generation over the meridian is itself a substantial issue; it must not be assumed in Gate 1. See Detcherry, *Infinite families of hyperbolic 3-manifolds with finite-dimensional skein modules*, especially the meridional finiteness discussion and conjectures. [Primary article](https://doi.org/10.1112/jlms.12410).

What differs from archived LATE-10 is the use of an **entire single peripheral trace fiber of an actual knot exterior**, rather than a closed-manifold generic skein dimension plus global tameness. What remains unchanged from LATE-26/LATE-33 is the fundamental information barrier: drilling is not skein-linear, and a ball-bracket scalar cannot simply be promoted to an exterior module relation. LATE-45's closed summand is excluded here by the actual S³ filling before gauge theory is invoked.

Barrier accounting: the one-component and classical S³ hypotheses enter the traceless irreducible representation theorem and the unique abelian trace fiber; virtual tangles do not supply this S³ exterior. The argument explicitly uses information beyond the Euler characteristic. Signed Jones cancellation has not been prohibited or explained away. The positivity in E1 belongs to SU(2) character evaluations of a newly defined exterior defect, not to the Jones polynomial.

## 6. Recommendation and stop point

Bank E1–E3 as conditional endpoints/obstruction lemmas, with no claim that they are new to the literature. The best concrete target for a future geometric argument is the **single commutator relation in a two-generator exterior**, because it avoids proving full meridional finiteness or reflexivity. Any proposed way to obtain it must explicitly retain exterior relations before taking the ordinary Jones counit.

No construction producing that relation from rational quotient bracket emerged in this pass. Do not launch a generic character-variety or AJ computation under the label of solving this gap. The construction is parked until there is a geometric comparison map or a genuinely new relation to test.
