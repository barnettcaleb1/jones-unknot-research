# Referee report: J-TILT, endpoint cancellation, and the rationality reduction

15 November 2026. Independent Codex subagent read for the resumed theory session.
Scope: §§1, 3.3, 4.3–4.8 and 5 of `mech/sum/REPORT.md`; no new knot search. The monoidality of the augmentation functor is being audited separately. Statements about sums below assume that functorial assertion, rather than treating the computed composite examples as its proof.

## Verdict

The conditional implication **J-TILT ⇒ Lemma Q is repairable and genuinely independent of the short-special observation**. The missing universal rank argument is available directly from the published curve normal forms. In fact a weaker endpoint condition suffices, and it is preferable to make that the research target.

This is a reduction, not a proof of the needed geography. It replaces the old package “all short specials + TILT + OVERHANG + empirical centering” by one intrinsic noncancellation assertion for a finite bigraded vector space. No result in the report proves that assertion for an arbitrary actual quotient tangle. The formal object B remains an explicit obstruction to deriving it from the abstract monoidal category alone.

## 1. Use the intrinsic vector space, not the empirical centering

Work over F₂. Let C(T) be the Bar-Natan type D invariant over the two-idempotent algebra B. Write b for the idempotent represented by Q₀, the unit for the chosen horizontal sum. Let ε_b kill the other idempotent and every positive-length algebra path, and set

    N_b(T) = H(ε_b C(T)).

All statements here concern the ordinary integer dimensions and integer graded Euler characteristic of this F₂-vector space. Choose the actual absolute grading induced by the unknot cap; alternatively allow an overall bigrading shift and keep track of the corresponding monomial. In a minimal/reduced model the differential has no identity coefficient, so ε_b C(T) has zero differential and its basis is precisely the b-generators. This definition avoids both the empirical shift (24j,4j) and the assumption k ∈ 4Z.

Its Euler characteristic is the b-coordinate of the tangle bracket. Dividing by the actual unknot-cap unit gives J. For the reduction, only the following consequence is needed:

    J(T)=1  ⇒  χ_q N_b(T) is a signed monomial.

The standard H-cone formula is

    C₁(T) = Cone(H : q⁻¹h⁻¹ C(T) → q C(T)).

Since ε_b(H)=0, applying ε_b gives two shifted copies. Consequently

    dim ε_b C₁(T) = 2 dim N_b(T).

This can be expressed at the homology level without making a uniqueness assertion about a chosen minimal model. In the explicit reduced curve model, all nonidentity paths again die under ε_b, so generator counts compute this dimension.

## 2. The universal component-count lemma

Suppose T(∞)=U, with the meridian and Seifert longitude marked as in the quotient-tangle convention. The published structure theorem gives

    Kh~(T) = r₁(k) ⊔ s_{ℓ₁}(∞) ⊔ … ⊔ s_{ℓ_m}(∞),

where k is an even integer and every ℓ_i is a positive even integer in the current notation. The local systems are one-dimensional. Neither ℓ_i=4 nor 4|k is required.

The b-generator counts in this marking are:

    r₁(k): 2;
    s_ℓ(∞): 4, for every allowed positive length ℓ.

Here is the direct count, which is easy to confuse with an arc-pairing dimension. In Kotelskiy–Watson–Zibrowius (2026), Definition 3.12, the displayed complex for s_{2n}(0) has FOUR circle-idempotent endpoint generators, while its two growing interior strings contain 4n bullet-idempotent generators. Lemma 3.9 and Proposition 3.10 identify the rotation ρ with the grading-preserving algebra automorphism interchanging the idempotents; it takes slope 0 to ∞. Thus the slope-∞ special has FOUR b-generators, independent of n; increasing its length increases the *other* idempotent's count. Equivalently this is visible in the older 2021 Figure 7: the four endpoint generators have the desired idempotent, while the caption counts 8n generators of the opposite idempotent. The older s_{2n} has current length 4n.

For r₁(k), use the same paper's §3.2 rather than assume the count from data. The matrix of τ_b is [[1,0],[-1,1]], and therefore τ_b⁻ᵏ sends slope 0 to k. The paragraph defining the grading action immediately after the replacement table states that τ_b establishes a one-to-one correspondence of the bullet vertices. Thus every r₁(k) has the same TWO b-generators as r₁(0), displayed in Definition 3.12 and Remark 3.13. Equivalently a(k) has one b-generator and its H-cone has two. This works for every integer k, not only multiples of four.

It follows that

    2 dim N_b(T) = 2 + 4m,
    dim N_b(T) = 1 + 2m.                                      (R)

Thus **dim N_b(T)=1 iff T is rational** on the unknot-cap locus. The only-if direction uses the published rational-tangle detection theorem once m=0. In the preferred Seifert framing that rational tangle is Q₀, since the disk slope is the marked longitude.

This repairs the open parenthesis in report §4.7. Longer specials do not create a gap here. It also upgrades the *number-of-special-components* sum formula, conditional on monoidality, to arbitrary allowed special lengths. It does not upgrade the report's separate rank-growth formula involving the length-weighted quantity D.

## 3. The weakest useful endpoint reduction supplied by this argument

For any nonzero finite bigraded vector space N define its unsigned quantum support endpoints

    q₋ = min{q : N^{*,q} ≠ 0},  q₊ = max{q : N^{*,q} ≠ 0}.

Define **END** to mean that both integer Euler characteristics

    Σ_h (-1)^h dim N^{h,q₋},   Σ_h (-1)^h dim N^{h,q₊}

are nonzero. Define **EXT** as in the report: each of these two quantum slices is supported in a single homological parity. Then

    J-TILT ⇒ EXT ⇒ END.

The first implication uses δ=q/2−h: strict decrease of the maximum q across successive δ-levels puts the global maximum on a unique level, hence at one homological degree. The same argument applies to the minimum. Consecutiveness of the levels is stronger than needed for this implication.

**Conditional theorem.** If every nonrational actual T with an unknot cap satisfies END for N_b(T), then Lemma Q holds.

Proof. A special component of length ℓ has b-generator quantum degrees c−ℓ−1, c−ℓ+1, c+ℓ−1, c+ℓ+1 in the symmetric convention (uniform grading shifts do not matter). Thus the unsigned quantum breadth of ε_b C₁(T) is at least 2ℓ+2. On the other hand, the H-cone identity says that its unsigned character is (q+q⁻¹) times that of N_b(T), after forgetting homological degrees. Nonnegative coefficients give the exact breadth identity

    breadth(ε_b C₁(T)) = breadth(N_b(T)) + 2.

Hence m>0 implies breadth(N_b(T)) ≥ 2 max_i ℓ_i ≥ 4. Under END both support endpoints survive in χ_q N_b(T), which therefore is not a monomial. This contradicts J=1. ∎

Alternatively, without using the length-dependent quantum formula, EXT alone suffices with (R): if χ_q N is a monomial, both support endpoints survive, so q₋=q₊. EXT then makes every generator have the same Euler sign, and the monomial coefficient ±1 forces dim N=1; (R) gives rationality. This is the most conservative repaired version of report §4.7.

The quantum formula is the same endpoint count as the preceding paragraph, not the “expanded support” obtained from pairing a long special with the horizontal filling arc. **Those are different vector spaces.** A long special contributes two length-separated points to the intrinsic J-set, not n copies of the short-special J-pair. The published decomposition of HF(a(0),s_{2n}(∞)) into n shifted blocks does not assert such a decomposition of N_b.

END is strictly weaker than EXT: an endpoint with even dimension 2 and odd dimension 1 has nonzero Euler coefficient but mixed parity. Neither END nor EXT is equivalent to Lemma Q: a non-flat tangle could have cancelled outermost support and a surviving nonconstant interior polynomial. Thus these are sufficient geography conjectures, not tautological rephrasings of the desired conclusion.

## 4. What the sum argument really establishes

Assuming the separately audited monoidal identity

    N_b(T₁+T₂) ≅ N_b(T₁) ⊗ N_b(T₂),

the following assertions are rigorous:

1. J-TILT is closed under compatible equivariant sums. For maxima, take a maximizing pair at level d+1; lower a non-bottom factor one level to get a strictly larger value at d. For minima, take a minimizing pair at d and raise a non-top factor one level to get a strictly smaller value at d+1. The occupied sum levels form an interval.
2. EXT holds for a tensor product iff it holds for both nonzero factors. Its top quantum slice is exactly the tensor product of their top slices, and likewise at the bottom. Positivity of dimensions prevents mixed parity in a factor from disappearing in the product.
3. END likewise holds for a tensor product iff it holds for both factors: the endpoint Euler coefficients multiply in Z.
4. Formula (R) gives, with no short-special hypothesis,

       1+2m₁₂ = (1+2m₁)(1+2m₂).

5. Let χ=χ_qN be nonzero and define the nonnegative endpoint losses

       λ₊(N)=max supp_q N − max supp χ,
       λ₋(N)=min supp χ − min supp_q N.

   Both losses add under tensor products, because unsigned support endpoints add and the highest/lowest nonzero coefficients of a product of integer Laurent polynomials cannot cancel. Thus END is exactly λ₊=λ₋=0, and the quantitative cancellation defect is additive. For a hypothetical flat nonrational T,

       λ₊(T)+λ₋(T)=breadth N_b(T) ≥ 2 max_i ℓ_i.

   This measures what an actual realization theorem must prohibit; it is not itself such a prohibition.
6. If dim N_b(T)=1+2m is prime, T cannot be a compatible equivariant sum of two nonrational quotient tangles: each factor would have odd rank at least three, contradicting multiplicativity. More generally, the number of nonrational factors in any such factorization is at most Ω(dim N_b(T)), the total number of prime factors counted with multiplicity. This is a concrete decomposition obstruction, not a statement that the underlying knot is prime and not a uniqueness theorem for equivariant decompositions.

These facts permit restriction of a minimal failure to **equivariantly sum-indecomposable factors**. They do not imply that the underlying knot is prime: an inversion that permutes summands need not be such a sum. They do not prove an equivariant prime-decomposition theorem or supply new information for the indecomposable factors.

The composite calculations give checks of conventions and implementation; once the tensor theorem is proved, they are not independent evidence for the geography conjecture.

## 5. Corrections to the report

- In §4.7, Euler algebra only proves that the unique generator has quantum degree 0 and **even** homological degree after χN=1 normalization. It does not by itself prove h=0 or δ=0. One should first conclude dim N=1, use (R) and rationality, and only then use the actual cap normalization to identify the absolute bigrading.
- The unqualified displayed formula `J-set={(2k,0)} ⊔ (S+E)` is a short-special formula in the report's empirically centered convention. The intrinsic definition by N_b is the universal one. Long-special endpoint pairs have length-dependent separation.
- The statement in §5 that B⊗T violates “EXT, J-TILT and TILT, because EXT is co-closed” overstates its proof. It gives failure of EXT and consequently J-TILT. Original special-set TILT does not imply EXT without further hypotheses; §4.2 already distinguishes these conditions. A separate argument or the reported explicit example is needed to claim original TILT fails in a particular product.
- “A minimal failure is sum-prime” must retain the compatible equivariant sum qualification.
- The component-number formula extends, but the full shape formula for special sets and the length-weighted rank-growth formula remain at their stated scope unless separately proved.

## 6. Does this give a real reduction?

**Yes, in the limited but useful sense of eliminating auxiliary hypotheses and identifying a single intrinsic realization question.** We now have an invariant defined directly from the tangle chain object, a rank-one detection theorem on the actual unknot-cap locus, and a precise endpoint noncancellation condition that implies Lemma Q. The report's older all-short, virtual-string, absolute-centering and OVERHANG assumptions are unnecessary for this reduction.

**No new topological mechanism has yet been supplied.** A formal object can have a nontrivial N_b with trivial Euler characteristic; B is exactly such an object. The tensor identity and rank calculations also hold for formal objects and cannot distinguish them from actual tangles. Proving END, EXT, or J-TILT on actual sum-indecomposable quotient tangles remains the hard realization theorem, and no cited theorem in this report establishes it.

The most economical next target is END on actual sum-indecomposable quotient tangles, with J-TILT as a stronger testable hypothesis that might provide a proof mechanism. A single actual failure of J-TILT would refute that stronger conjecture but would leave END and Lemma Q open. A single actual failure of END would refute this endpoint route, again without refuting Lemma Q. Neither needs an indiscriminate knot search to be understood logically.

## 7. Sources inspected

- Kotelskiy–Lidman–Moore–Watson–Zibrowius, *Cosmetic operations and Khovanov multicurves*, [arXiv:2109.14049](https://arxiv.org/abs/2109.14049), §2 Theorems 2.6–2.7 and the beginning of §4 (proof of Theorem 1.2). Primary local TeX inspected: `lit/kwz-thin/src/cosmetic/tex/sections/Background.tex`, `ecsc.tex`. This supplies the unknot-cap structure and rationality detection, with no assumption of short specials.
- Kotelskiy–Watson–Zibrowius, *On mutation invariance in Khovanov homology*, [arXiv:2602.23442](https://arxiv.org/abs/2602.23442), Definition 3.12, Theorems 3.17 and 3.19. Primary local TeX inspected: `lit/kwz-linear/src/mut2026/tex/sections/KhNew.tex`; numbering checked in `mut.txt`. This supplies the explicit normal forms, their generator counts, rationality detection and one-dimensional local systems over every field. The present referee argument is restricted to F₂.
- Kotelskiy–Watson–Zibrowius, *Khovanov homology and strong inversions*, [arXiv:2104.13592v1](https://arxiv.org/html/2104.13592v1), Lemma 2.3 and Figure 7. The long-special pairing decomposition and the type-D endpoint count are distinct; both were checked against the primary TeX and HTML.
- The H-cone and curve-generator conventions were cross-checked in the primary TeX of [arXiv:1910.14584](https://arxiv.org/abs/1910.14584), §§5–6, and in the cosmetic-operations paper §2.

No external specialist review or novelty claim is asserted. No new geometric examples were computed in this referee pass.
