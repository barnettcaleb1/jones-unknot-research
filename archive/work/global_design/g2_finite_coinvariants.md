# Genus-two Torelli coinvariants at every finite expansion order

2026-11-03. Source audit and completed proof of the theorem proposed in the coordinated lane's `zrho/build-infinite/infinite.md`. Codex supplied the integral extension-class normalization and an elementary congruence proof, with an independent internal check of the latter. Status: TRUSTED, written proof; main collaborator review and novelty check pending. No claim of Jones unknot detection or of generic faithfulness.

## Statement

Write M = Mod(Σ₂), I = I₂, and D = [M,I]. Normalize the generator of I/D ≅ Z by sending a separating Dehn twist T to 1. For a homomorphism σ defined on M, put

    Z_σ = σ(I)/σ(D).

Let ρ be Jones's integral genus-two representation, and let ρ_k be its reduction modulo (t+1)^(k+1). Equivalently, use Kasahara's expansion t = −exp(h) through degree k.

**Theorem.**

1. For every homomorphism π from M into a finite group, Z_π is cyclic of order dividing 10.
2. For every integer k ≥ 1,

       Z_{ρ_k} ≅ Z/10.

Consequently, if F_{k+1} = I ∩ ker ρ_k and d̂:I→Z is the normalized coinvariant homomorphism, then

    d̂(F_{k+1}) = 10Z     for every k ≥ 1.

The second assertion extends the two finite-order values recorded in Kasahara's Remark 6.3. It does not determine Z_ρ for the untruncated representation.

## 1. Published inputs and exact normalizations

- [Kasahara, AGT 1 (2001), Section 6 and Remark 6.3](https://arxiv.org/pdf/math/0012216): I/D ≅ Z, with a separating twist as generator; Z_{ρ_1} ≅ Z/10. The representation is integral Laurent-polynomial valued, and ρ(I)|_{t=−1}=1. We use the published first-order value for the lower bound; no new lattice computation or Casson sign convention is needed.
- [Endo, Math. Ann. 316 (2000), Proposition 3.1 and Lemma 3.5](https://webhomes.maths.ed.ac.uk/~v1ranick/papers/endo2.pdf): a class function φ:M→(1/5)Z satisfies δφ = τ, where τ is the pulled-back symplectic Meyer cocycle. For a separating twist in Endo's convention, φ(T)=−4/5. Reversing the twist convention changes a sign only. His Section 2(1) records [τ]=4c₁.
- [Turaev, Functional Analysis and Its Applications 18 (1984), Section 1 and Theorem 1](https://webhomes.maths.ed.ac.uk/~v1ranick/papers/turaev2.pdf): c₁ is the class of the pullback of the universal cover of Sp(4,R), and the signature cocycle represents four times that class. This fixes the normalization relative to the actual infinite cyclic covering kernel, not an unspecified generator of rational cohomology.
- [Deligne, C. R. Acad. Sci. Paris 287 (1978), p.203](https://publications.ias.edu/sites/default/files/35_ExtensionsCentrales.pdf): every finite-index subgroup of the pullback of the universal cover of Sp(2g,R) to Sp(2g,Z), g≥2, contains twice its infinite cyclic covering kernel. The genus-two case is explicitly included.

All four source statements were checked in this pass. No assertion about a universal central extension of the nonperfect group Sp(4,Z) is needed.

## 2. The extension class: an integral identity

Set E=M/D. There is a central extension

    1 → ⟨T⟩ ≅ Z → E → S=Sp(4,Z) → 1.

Let ε∈H²(S;Z) be its class, and c the universal-cover class from Section 1. We prove

    4ε = 20c,

up to the harmless simultaneous sign choice for T or the covering generator. This is stronger than an unspecified equality modulo torsion and removes the factor-of-two uncertainty in the draft.

Because τ is inflated from S and vanishes when an argument is the identity, φ restricts to a homomorphism on I. Its conjugation invariance makes it vanish on D, so it descends to E. Also φ(T^n x)=n c₀+φ(x), where c₀=−4/5.

Choose a set-theoretic section s:S→E and write

    s(a)s(b)=T^{e(a,b)}s(ab),       f(a)=φ(s(a)).

Here e is an integral cocycle representing ε. The coboundary equation for φ gives

    δf(a,b)=τ(a,b)+c₀ e(a,b).

Since 5f is integer valued,

    δ(5f)=5τ−4e.

Thus 4ε=5[τ]=20c in integral cohomology. This argument uses neither the rank of H²(S;Z) nor a choice of a primitive Hodge generator.

## 3. Transporting Deligne's bound

Push E out along multiplication by 4 on its central Z. Denote the resulting extension by E₄ and its central generator by w. The natural map E→E₄ is injective, has finite-index image, and sends T to w⁴.

Its extension class is 4ε=20c. Therefore E₄ is isomorphic, as an extension of S, to the pushout of the restricted universal cover S̃ along multiplication by 20. The corresponding injection S̃→E₄ sends its central generator z to w²⁰=T⁵. A sign change would give T⁻⁵ and does not affect the conclusion.

Let V≤E have finite index. Viewed in E₄ it still has finite index, so V∩S̃ has finite index in S̃. Deligne gives z²∈V∩S̃. Hence

    T¹⁰ ∈ V.

This holds for every finite-index subgroup of E.

Now let π:M→F with F finite. The image V=(ker π)D/D in E has finite index. The natural map I/D→π(I)/π(D) has kernel ⟨T⟩∩V. Therefore Z_π is a quotient of Z/10, proving assertion 1.

## 4. Elementary congruence lemma for integral unipotent groups

**Lemma.** If P≤UT_d(Z) and H≤P has finite index, there is an integer m>0 such that

    {p∈P : p≡1 mod m} ⊆ H.

**Proof.** Let U_r≤UT_d(Z) consist of matrices whose first r−1 superdiagonals vanish, and set P_r=P∩U_r. The r-th superdiagonal embeds P_r/P_{r+1} as a subgroup L_r of Z^(d−r). Choose a lattice basis of each L_r and lifts g_{r,j}∈P_r. Extracting the superdiagonals successively gives a unique ordered expression

    p = ∏_{r,j} g_{r,j}^{n_{r,j}},       n_{r,j}∈Z.

There are finitely many lifts, so this also proves finite generation of P. Every coordinate n_{r,j} is a rational polynomial in the entries of p−1 with zero constant term. To see this inductively, a rational left inverse to the lattice-basis matrix extracts each layer. Removing previously extracted factors remains polynomial, using the finite nilpotent identity

    g^n = Σ_{ℓ=0}^{d−1} binom(n,ℓ)(g−1)^ℓ

for all integers n, including negative n.

Clear all coordinate-polynomial denominators with a common positive integer D₀. Choose e>0 such that every g_{r,j}^e lies in H, for instance e=[P:H]!. If p≡1 mod D₀e, each integral polynomial D₀ n_{r,j}(p) is divisible by D₀e. Thus every n_{r,j}(p) is divisible by e, and the ordered product belongs to H. Take m=D₀e. ∎

This proves precisely the congruence fact needed below, without assuming that P is a preselected arithmetic lattice or citing a general congruence-subgroup theorem.

## 5. All finite expansion orders

Put R_k=Z[s]/s^(k+1), with t=−1+s. Since t is a unit in R_k, ρ_k is an integral representation of M on the free abelian group R_k⁵ of rank 5(k+1). After ordering its basis by powers of s, the image

    P_k=ρ_k(I)

is unitriangular: every element is identity modulo s. Reversing basis order if needed puts it in UT_{5(k+1)}(Z). Set C_k=ρ_k(D). Then P_k/C_k is cyclic, because it is a quotient of I/D.

We first prove it is finite, rather than presuming this in applying the congruence lemma. If P_k/C_k≅Z, let H be the inverse image of 11Z. The lemma supplies m such that the matrix congruence kernel inside P_k lies in H. Reduce the representation of the **whole group M** modulo m to obtain a finite quotient π. The cyclic group Z_π then surjects onto P_k/H≅Z/11, contradicting assertion 1.

Now C_k has finite index in P_k. Apply the lemma with H=C_k. For the resulting finite reduction π, its kernel on P_k is contained in C_k; hence

    Z_π ≅ P_k/C_k.

Assertion 1 gives |P_k/C_k| dividing 10. For k≥1 there is a natural surjection P_k/C_k→Z_{ρ_1}≅Z/10, using Kasahara's recorded first-order calculation. Thus |P_k/C_k| is also divisible by 10 and assertion 2 follows.

Finally, substitution s=1−exp(h) is an isomorphism of the truncated rational power-series algebras, with nonzero linear term. The inclusion of R_k in its rationalization is injective. Thus the integer s-truncation and Kasahara's h-truncation have the same kernel on M and the same coinvariant quotient.

## 6. Exact limitation and research decision

This result fixes every finite-stage number in Kasahara's suggested truncation test. It forbids proving that Z_ρ is infinite by showing these orders grow: they do not grow.

It does **not** show d̂(ker ρ∩I)=10Z. One cannot exchange d̂ with the infinite intersection:

    d̂(⋂_{k≥1}F_{k+1})  need not equal  ⋂_{k≥1}d̂(F_{k+1})=10Z.

For each k there exists an element x_k with d̂(x_k)=10 and ρ(x_k)=1 to order k. This does not produce one element with that property at every order. Nor does it rule out a genuinely global argument using the complete representation and additional geometry.

The generic question remains: does some x∈ker ρ∩I have d̂(x)≠0? The coordinated Casson–Mullins identity would turn such an actual element into a Jones-trivial knot of nonzero signature. Neither the theorem here nor the completed branch notes provide that element.

Research disposition: bank the finite-stage theorem; stop attempts to obtain unbounded coinvariant orders by deeper expansion. Do not substitute repeated finite calculations for a mechanism controlling the intersection.
