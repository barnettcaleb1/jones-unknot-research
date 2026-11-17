# Positive surface skeins: a compression obstruction

Status: bounded theory pass, 2026-11-03. The proposition below is an elementary deduction, not a novelty claim. It rules out a specific use of established positivity; it does not rule out a new knot-specific positive invariant.

## 1. The strongest safe positivity input

Let S be an oriented punctured surface with negative Euler characteristic, and use the full Kauffman bracket skein algebra over R = Z[A,A^{-1}]. Our conventions are

    [contractible circle] = delta · 1,   delta = -A^2 - A^{-2}.

For an essential nonperipheral simple closed curve c at constant elevation with vertical framing, Cho–Kim–Kim–Oh, Theorem 1.3, proves that its Bonahon–Wong quantum trace has nonnegative Laurent coefficients in every ideal triangulation. The parameters satisfy A = omega^{-2}; coefficients lie in Z_{≥0}[omega,omega^{-1}], with square-root quantum edge variables. This is already enough for the obstruction below. Their integral-lamination theorem supplies a larger positive class. [Primary source, Theorems 1.1–1.3](https://arxiv.org/pdf/1710.06217).

Two related results should be kept distinct. Thurston's bracelet-basis theorem gives positive multiplication constants at the classical skein parameter 1, and positivity for diagrams without nullhomotopic components or nugatory crossings. It is not a theorem about arbitrary generic-parameter knot diagrams. [Thurston, Theorems 1–2](https://arxiv.org/pdf/1310.1959). Mandel–Qin identify bracelet and theta bases, including quantum results in their specified surface settings; this strengthens the available surface positivity but does not address filling into S^3. [Mandel–Qin](https://arxiv.org/pdf/2301.11101).

## 2. Proposition: S^3 filling has a nonzero positive kernel element

Embed a once-punctured torus S in S^3 as a standard unknotted torus with one point removed. Let c be a meridian, and choose the puncture away from c. Give c its surface framing. Let

    E : S_A(S) -> R

be the R-linear map induced by including a thickening of S into S^3 and evaluating its framed bracket. Define

    D = [c] + (A^2 + A^{-2}) · 1.

Then:

1. D is nonzero in the surface skein.
2. D is a positive combination of the simple-curve bracelet element [c] and the unit.
3. After A = omega^{-2}, its quantum trace is a nonzero Laurent-positive element in every ideal triangulation.
4. E(D) = 0.

Proof. The essential-curve multicurve basis makes [c] and 1 linearly independent, proving (1). Statement (2) is immediate and does not need a theorem about multiplication constants. The cited quantum-trace theorem applies to c; adding the positive scalar omega^{-4}+omega^4 proves (3), including nonvanishing. In S^3, c bounds a meridian disk, and its surface framing is zero. Therefore E([c]) = delta and E(D) = delta + A^2 + A^{-2} = 0. This proves (4).

The example is more relevant than an arbitrary formal positive sum. If u is a small contractible circle in S, then

    D = [c] - [u].

Both c and u are zero-framed unknots in S^3. Thus the kernel element is an actual knot-minus-unknot difference. Its positivity is entirely genuine in the established surface domain, and its disappearance comes from compression in the ambient three-manifold.

The map E is only asserted to be linear. No claim is made that it is an algebra homomorphism, or that its kernel is an ideal: stacking links on S and evaluating in S^3 need not turn multiplication into scalar multiplication.

## 3. What this forbids

The proposed chain

    positive surface lift -> no cancellation -> nonzero Jones defect

fails at the second implication, even before one introduces a crossing. Positivity controls the algebra of a marked surface. Classical knot isotopy is permitted to move across compressing disks of that surface, and those additional identifications have positive kernel elements.

For the specific zero-framed knots in the proposition, dividing the evaluated difference by delta gives their normalized Jones difference, which is zero. Writhe normalization therefore does not rescue this example.

There is also a marking problem. The meridian and longitude of the standard unknotted torus are distinct simple-curve skein basis elements, but both are zero-framed unknots in S^3. A raw surface lift consequently carries information not determined by ordinary Jones. Making it independent of the chosen surface presentation requires quotienting out genuine topological information, precisely where the positive-kernel obstruction occurs.

This does not prove that a specially chosen set of positive knot defects must intersect the kernel. A knot-specific construction might avoid this element. It would need an additional theorem doing that work; the existing positivity theorems do not supply it.

## 4. Why projection and normalization do not fill the gap

For an arbitrary projection into S, the bracket smoothing coefficients A and A^{-1} are positive monomials, but contractible state circles contribute -A^2-A^{-2}. A framing change contributes -A^{±3}. Surface quantum-trace positivity is not a license to discard these signs. Writhe normalization is an operation on a specified oriented diagram, not a single positivity-preserving linear operation on every term of a skein expansion.

One can alter sign conventions or choose a spin-dependent identification of skein algebras, but then the positive cone changes. The proposition concerns the standard bracelet/Bonahon–Wong cone with the conventions explicitly stated above; it is not a theorem about every conceivable re-signed cone.

There is nevertheless a stronger, precisely scoped obstruction to one common repair.

**Homological sign-gauge lemma (parent's extension, checked here).** Let S be the boundary of a standard genus-two handlebody in S^3, with one point removed. For any character

    epsilon : H_1(S; F_2) -> {+1,-1},

re-sign each essential simple-curve generator by [c] -> epsilon([c]) [c]. The filling map cannot send all these re-signed generators to coefficientwise nonnegative Laurent polynomials.

Proof. Choose the two standard meridian disks D1,D2 and their boundary band sum D12, using a band avoiding the puncture. Their boundaries mu1,mu2,mu12 are essential nonperipheral simple curves, each zero-framed and unknotted in S^3. Their nonzero homology classes satisfy [mu12]=[mu1]+[mu2] over F_2. Positive evaluation of each re-signed curve would require epsilon([mui])=-1, since every original curve evaluates to delta. But epsilon([mu12])=epsilon([mu1])epsilon([mu2]), so those three signs cannot all be -1. At least one of the three still evaluates to delta, with negative coefficients.

There is an even shorter proof if separating curves are allowed: an essential separating meridian on the genus-two handlebody has homology class zero, so every character leaves its sign unchanged. The three-disk argument shows that excluding separating curves does not repair the problem.

This rules out sign characters of homology as a universal positivity repair. It does not classify quadratic spin conventions, conventions changing A to -A, or component-dependent re-signings.

There is no justified assertion here that a positive surface lift forces an adequate planar diagram. Essential simple curves on surfaces have positive quantum traces for reasons independent of planar adequacy. Conversely, surface positivity alone cannot imply planar noncancellation, as the compression example shows.

## 5. The only honest construction target left by this pass

A usable route would have to construct, for each classical knot K, a surface and a distinguished element D_K with three independently justified properties:

- E(D_K) is determined by V_K, and vanishes whenever V_K = 1.
- D_K lies in a proved positive cone and is nonzero whenever K is nontrivial.
- The selected family {D_K} avoids the positive kernel of filling.

The third item is the actual new geometric theorem. A condition expressed merely as crossing-free projection, membership in the bracelet cone, or Laurent positivity in every triangulation is insufficient: D above has all of them in the applicable sense. A fruitful refinement would have to control compression or disk geometry while being invariant under changes of surface presentation. No such refinement was proved or found in this pass.

Conclusion: the cross-field input is real and strong, but the direct positivity-to-Jones argument is blocked by an explicit positive compression relation. This is a reason to stop that generic route, not a new partial proof of unknot detection.
