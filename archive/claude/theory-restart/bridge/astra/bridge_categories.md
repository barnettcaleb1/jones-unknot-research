# Categorical bridge: realization through deformation, not a new Euler characteristic

17 November 2026. Theory-only audit for the cross-field pivot. No computations or scans. The strongest useful outcome is a precise test for whether a proposed categorical enhancement contains new information; ordinary stability positivity fails that test already.

## 1. Translation and existing bridge

Let C(T) be the bigraded Bar–Natan/Khovanov tangle object, and A the rational comparison object in the same boundary marking. The bracket is a graded Grothendieck-class pairing. In the unknot-filling fibre, Lemma Q asks whether the appropriate rational bracket class forces the actual tangle to be rational. **It does not assert that every formal object with that class is A.** The formal objects A ⊕ Q ⊕ Q[1], and the banked four-summand ladders, disprove that unrestricted assertion.

This is already connected to symplectic geometry: [Kotelskiy–Watson–Zibrowius, arXiv:2004.01619](https://arxiv.org/abs/2004.01619) identify two constructions of the relevant Fukaya-category tangle invariants. [KWZ, arXiv:1910.14584](https://arxiv.org/abs/1910.14584) give immersed curves with local systems and the closure pairing. The component classification over arbitrary fields is supplied by [KWZ, arXiv:2602.23442](https://arxiv.org/abs/2602.23442). Merely replacing a complex by its curve picture is therefore a known translation, not new leverage.

The relevant distinction is **objects of the category versus objects produced by an actual planar tangle construction**. A promising bridge must exploit this distinction explicitly.

## 2. Why stability conditions alone do not give positivity

Bridgeland's central charge is a homomorphism from K0; hence every central charge kills [Q]+[Q[1]]. Stability mass does not: for a stability condition sigma and a nonzero Q,

    m_sigma(Q ⊕ Q[1]) = 2 m_sigma(Q) > 0.

Consequently, equality of the bracket class with a rational class gives no mass bound. Adding arbitrarily many opposite-shift pairs keeps every charge fixed and increases mass without bound. This is an elementary deduction from the definitions, not a new theorem about tangles. Sources: [Bridgeland, Stability conditions on triangulated categories](https://arxiv.org/abs/math/0212237), and [Haiden–Katzarkov–Kontsevich, Flat surfaces and stability structures](https://arxiv.org/abs/1409.8611), especially Theorem 5.1 identifying the surface category's K0 with relative homology with local coefficients.

A heart cannot contain both a nonzero object Q and Q[1]: the t-structure axioms exclude this. Nor can a single semistable object have both as direct summands, since their phases differ by one. Thus an assertion that every actual quotient invariant is semistable, or lies in one common heart after a global shift, is too strong under the recorded realization data. The saved invariant examined in `maps_report_referee.md`, §5, contains precisely an equal-quantum Q ⊕ Q[1] pair, together with other summands. Its labelled strong-inversion identification was not independently reconstructed from a diagram in that audit; subject to that identification it is a direct inexpensive falsifier, independent of the later counterexamples to endpoint laws.

A phase restriction only on the Jones-unit locus could evade this example, but without a separate geometric argument it is essentially the desired noncancellation statement recast in stability language. It is not presently a reduction.

## 3. The better bridge: derived deformation obstructions

There is a concrete precedent for realization constraints gaining information beyond K0. [KWZ, Khovanov multicurves are linear, Theorem 4.4](https://arxiv.org/pdf/2202.01460) prove that actual tangle type-D structures extend from B to the A-infinity deformation B*[U]. Their proof of Theorem 4.1 uses an uncancellable U² term from a higher product to exclude certain curves. Theorem 4.25 relates the deformation to a matrix-factorization model. This is a genuine import from homological mirror symmetry and deformation theory, not a positivity assumption.

Precisely, Theorem 4.4 covers both the Bar–Natan objects Д(DT), Д^c(T) and the H-cone/reduced-Khovanov objects Д_1(DT), Д^c_1(T). The paper's §2 defines Д_1 as the suitably shifted cone of H on Д. Our ladder Q is a compact **BN** block, so the proposed test concerns Q itself over B, not an unidentified Khovanov special. A test on Cone(H:Q→Q) is a separate Kh-level test; it must not be substituted for the BN lift.

The next candidate is therefore **a relative, coherent extension obstruction for the actual tangle diagram and its filling maps**, rather than a new homology group with the same Euler polynomial. A prospective construction must specify which higher operations or geometric maps it retains. For a module deformation, at each order the equation for the next correction is linear up to a known obstruction cocycle in its endomorphism complex. A nonzero obstruction class is a finite certificate that the proposed formal module cannot realize that enhancement.

The information could be useful because the bracket and the separate closure groups forget higher extension data. It is not yet a theorem about our ladders: no nonzero obstruction for a ladder has been established. Moreover, the 2022 paper's Remarks 4.13 and 4.26 distinguish extension existence from invariance of a selected enhanced multifactorization. One must not silently promote that construction to a fully functorial new tangle invariant.

## 4. First lemma and decisive test

**Block-extension lemma (elementary).** For a fixed uncurved or curved A-infinity algebra deformation, the class of modules admitting extensions is closed under finite direct sums and grading shifts. Indeed, take block-diagonal structure maps on the direct sum. Each A-infinity equation restricts to its original summand; no mixed composable sequence occurs. The usual shifted signs handle homological shifts. The same argument works to any specified finite deformation order.

Therefore, if A and the single compact building block Q separately extend, then every banked ladder made from A and shifted copies of Q extends. **No mere existence-of-extension test over that deformation can exclude those ladders.** This is a rigorous exclusion of a mechanism, conditional only on checking the single-block lifts, not on classifying all tangles. It also explains why adding still more separately satisfiable deformation equations may be empty work.

The first bounded task should be: take the exact Q already used in TH-LADDER, write the KWZ higher operations, and determine whether Q alone extends over B*[U] (or identify its first obstruction). This is one object and one explicitly stated extension problem. If it extends, the entire “use the existing U-extension to eliminate ladders” route closes immediately. If it does not, test the whole ladder: an extension of a whole object need not preserve its undeformed summand decomposition, so nonextension of Q alone does not prove nonextension of the ladder.

Only after this test should one develop a stronger structure: e.g. a specified simultaneous system of filling/cobordism maps with coherence under movie moves. The present central-map no-go result covers existence of isolated pairs of maps, not such a geometric system. A successful new theory must name a relation that its formal identity-block ladder cannot satisfy.

## 5. Verdict and novelty scope

Rank below a bridge that already supplies a nontrivial consequence. The existing Fukaya/mirror-symmetry connection is established literature; central-charge blindness and the block-extension lemma are standard formal deductions. I found no source establishing the proposed coherent obstruction on our realization fibre, and no novelty is claimed for the general method.

What survives is a precise research filter: **compute a realization obstruction, or specify a nonadditive geometric compatibility that fails on the ladder.** “Categorify J,” “put the curves in a stability condition,” and “lift the module to a deformation” are insufficient on their own. The one-block extension test is a cheap falsifier before investing in a new homology theory.
