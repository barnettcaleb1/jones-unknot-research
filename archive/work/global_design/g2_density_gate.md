# Genus-two Jones image: generic and unit-circle density audit

Date: 2026-11-03. Theory audit only; no computation. Source texts checked in `/Users/calebbarnett/jones-lanes/g2-proof/zrho/read-kasahara/`. No lane or collaboration files edited.

**Verdict.** The proposed generic Zariski-density argument is valid. Kasahara's first-order image, together with its matrix commutators, suffices to prove that the Zariski closure of ρ(I₂) over Q(t) is SL₅. At a transcendental unit-circle parameter preserving a nondegenerate Hermitian form, the image is topologically dense in the corresponding SU(p,q). The separating-twist eigenvalues supply the essential nondiscreteness step. This says nothing about faithfulness.

## 1. Exact source input

[Kasahara, An expansion of the Jones representation of genus 2 and the Torelli group](https://arxiv.org/abs/math/0012216), Theorem 1.1, identifies the degree-one expansion image at t=−exp(h) with Γ_(0,2), dimension 14. Equation (4.1) gives

    End(Q⁵) = Γ_(0,2) ⊕ Γ_(2,0) ⊕ Γ_(0,0),
    dimensions 14 + 10 + 1.

The underlying five-dimensional module is Λ²H/ω, with its invariant symmetric form. Accordingly Γ_(0,2) is the traceless selfadjoint space S₀ and Γ_(2,0) is the skewadjoint space so(H). Theorem 1.3 also independently records the degree-two Γ_(2,0) image.

[Kasahara's addendum](https://arxiv.org/abs/1004.1068) proves det ρ=1 on I₂. The first paper's equation (2.2) gives the separating twist eigenvalues

    t⁶, multiplicity four;       t⁻²⁴, multiplicity one.

All matrices of I₂ specialize to I at t=−1.

## 2. Formal logarithms really belong to the Zariski Lie algebra

Let F=Q((h)), let G be any algebraic subgroup of GL_d over F, and let g∈G(F)∩(I+hM_d(Q[[h]])). Then

    X=log(g) ∈ Lie(G)(F).

**Proof.** For a polynomial P in the defining ideal of G, consider P(exp(zX)). After multiplication by a fixed power of h, this is an h-adic series whose coefficient at each power of h is a polynomial in z: X has positive h-order, so only finitely many powers of z contribute at each h-order. At every integer z=m, exp(mX)=g^m belongs to G, so every such polynomial vanishes at every integer. In characteristic zero each is identically zero. Differentiating the identity P(exp(zX))=0 at z=0 gives the tangent-space condition for X. ∎

This avoids assuming a general Lie-group logarithm theorem over the Laurent-series field. Coefficients of P may themselves depend on h; they have only finitely many negative powers, which is why the argument still applies.

## 3. Degree one is sufficient for generic SL₅

Let G be the Zariski closure of ρ(I₂) over Q(t). The substitution t↦−exp(h) is injective, so it defines a field extension Q(t)⊂F. Work inside G_F.

Choose fourteen actual group elements gᵢ∈I₂ whose first-order matrices Xᵢ form a Q-basis of S₀. The source theorem guarantees that such a finite choice exists. By Section 2,

    Yᵢ=h⁻¹ log ρ(gᵢ) ∈ Lie(G_F),       Yᵢ=Xᵢ+O(h).

The commutators [S₀,S₀] span so(H). To verify the linear-algebra assertion, extend scalars to diagonalize H and reduce it to the identity form. For i≠j, take a traceless diagonal D with unequal i,j entries and the symmetric matrix E_ij+E_ji. Their commutator is a nonzero multiple of E_ij−E_ji; these ten matrices span so₅. Surjectivity descends to Q because it is a rank statement.

Choose ten commutators of the Yᵢ whose constant terms form a basis of so(H). These ten and the original fourteen have independent constant terms in sl₅. A nonzero constant minor shows that they remain independent over F. Thus dim Lie(G_F)≥24. Since det ρ(I₂)=1, G⊂SL₅, and equality of dimensions forces G=SL₅.

No faithfulness or higher-order expansion hypothesis is used. Alternatively, Kasahara's degree-two theorem supplies ten elements of filtration two and their logarithms divided by h².

## 4. Transcendental specialization and the real form

Let t₀∈C be transcendental over Q. Evaluation gives an isomorphism Q(t)≅Q(t₀), so the specialized image is Zariski dense over Q(t₀). Extending scalars to C preserves this density: in each bounded polynomial degree, all equations vanishing on the image are the kernel of a linear system with coefficients in Q(t₀); this kernel commutes with field extension. Hence the complex Zariski closure is SL₅(C).

Suppose |t₀|=1 and the representation preserves a nondegenerate Hermitian form H₀ of signature (p,q). Determinant one gives Γ=ρ_(t₀)(I₂)⊂SU(H₀). Its real algebraic closure is all SU(H₀). Indeed, any proper real algebraic subgroup of SU(H₀) would have proper complexification inside SL₅(C), contradicting the established complex Zariski density.

The transcendence condition is important: the proof does not claim Zariski density at every non-root-of-unity algebraic specialization.

## 5. Zariski density upgrades to topological density here

Let C be the ordinary topological closure of Γ in SU(H₀), with Lie algebra c. The generic separating-twist operator satisfies the quadratic annihilating identity (ρ(T)−t⁶I)(ρ(T)−t⁻²⁴I)=0, as follows from the generic TL decomposition described in Section 6. This identity, not the eigenvalue list alone, makes its specialization diagonalizable when t₀⁶≠t₀⁻²⁴. Both eigenvalues lie on the unit circle and t₀ has infinite order. Its cyclic closure is therefore a positive-dimensional compact torus (in fact a circle). Consequently c≠0.

The space c is invariant under Ad(Γ). The stabilizer of a fixed real linear subspace under the adjoint representation is real algebraic, so real Zariski density makes c invariant under all SU(H₀). Thus c is an ideal in su(p,q). This real Lie algebra is simple for p+q=5, so c=su(p,q). The closed subgroup C therefore contains the identity component of SU(p,q), which is the whole group. Hence

    closure_topological ρ_(t₀)(I₂) = SU(p,q).

The compact cyclic subgroup is essential. Zariski-dense subgroups of noncompact groups can otherwise be discrete; Zariski density alone would not prove the claim.

## 6. The local SU(2,3) interval and the square convention

In the five-cap Temperley–Lieb realization W(6,0), label the matchings

    a=(12)(34)(56), b=(12)(36)(45), c=(14)(23)(56),
    d=(16)(23)(45), e=(16)(25)(34).

The diagrammatic Gram form is G_ij=δ^(number of loops in i∪j), δ=−A²−A⁻². Divide its universal factor δ. At δ=0, the one-loop pairs are exactly (a,d),(b,c),(b,e),(c,e), and the diagonal is zero. Thus the limiting matrix is the adjacency matrix of K₂ disjoint union K₃. Its eigenvalues are 1,−1,2,−1,−1, so it is nondegenerate of signature (2,3).

For |A|=1 the parameter δ is real, and reflection/conjugation makes the braid matrices unitary for this form. Continuity preserves its signature near A₀=exp(iπ/4). The scalar Jones normalization has modulus one, so it preserves the form as well.

The parameter convention is t⁵=A⁻⁴, with t=−1 at A=A₀. The standard TL generator has eigenvalues A (multiplicity three) and −A⁻³ (multiplicity two). Multiplication by −t⁻²/A gives −t⁻² and t³, agreeing with Kasahara's generator. Transferring between these realizations uses their generic Jones/TL module identification; agreement of eigenvalues alone is not a proof of that identification. A generic intertwiner may have a pole at the endpoint, which is harmless for density at transcendental nearby parameters.

**Separating twist correction.** Let τ be the full twist around the three-puncture side downstairs. Its TL eigenvalues are A⁻⁶ (multiplicity four) and A⁶ (multiplicity one). The separating twist upstairs corresponds to τ², not τ. Thus its eigenvalues before scalar normalization are A⁻¹² and A¹². Its determinant is A⁻³⁶. The exact determinant-one scalar branch is

    u=t⁻⁹,       u⁵=A³⁶,       u(−1)=−1.

It produces eigenvalues t⁶ and t⁻²⁴, as required. **Endpoint clarification after Claude134755:** an eigenvalue list alone does not exclude Jordan blocks, and TL₃ is not semisimple at A₀. The endpoint ρ(I₂)=I in Kasahara's lattice is source input from Section 1. To justify the same endpoint in the analytic TL lattice without a regular intertwiner, use the stronger generic identity

    (τ−A⁻⁶I)(τ−A⁶I)=0.

Indeed, over Q(A) the central full twist acts by these two scalars on the two simple TL₃ summands. TL₃ over Z[A,A⁻¹] is free on its diagram basis, so the identity holds before specialization, and hence in W(6,0) at every A. At A₀ its two roots are i and −i; the specialized identity is τ²+I=0. Therefore uτ²=I at A₀. Conjugacy of separating twists and their generation of I₂ give the trivial endpoint in this lattice. No semisimplicity at A₀ or inference from multiplicities is used.

The TL/Jones identification and its covering convention are the inputs to this last local realization; the density proof in Sections 2–5 is already complete for any nondegenerate unitary specialization.

## 7. Exact scope of the DGW barrier

Density obstructs an additivity claim only when its defect is continuous on the ambient group (or is central-invariant on a cover and descends to a continuous defect on SU(p,q)). If that defect vanished on Γ×Γ, density would force it to vanish everywhere. Therefore a known nonzero such ambient defect cannot vanish on the Torelli image.

Do not infer that every abstract homomorphism from the dense image is trivial: discontinuous homomorphisms are not excluded. Nor does density settle Kasahara's cyclic quotient Z_ρ, the factorization of d₁, Jones unknot detection, or faithfulness. No novelty assertion is made for the density deduction.
