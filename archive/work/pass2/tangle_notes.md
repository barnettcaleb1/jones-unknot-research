# Second bounded pass: actual tangle constructions

Prepared 2026-10-31, within the 16:57–17:27 UTC pass.

## Outcome

No counterexample and no general proof. Every actual Jones-one knot produced in these tests was certified to be an unknot by diagram simplification. More substantially, the generalized Kanenobu/Watson construction used here has an actual unlink band smoothing. Lobb's theorem and Khovanov unknot detection therefore exclude whole infinite twist families once an unknot anchor is established. This is a deduction from existing theorems, not a claimed new theorem of knot theory.

The obstruction is topological: the constructions that make the Jones cancellation automatic also provide band resolutions strong enough for Khovanov theory. Merely replacing an integer tangle by a nonrational tangle with an unknot denominator did not evade that obstruction.

## Exact conventions and cap cancellation

Write `L_alpha(T,U)` for the actual six-strand construction in `watson_model.py`. Its middle braid is

    beta = j(alpha) s(alpha),
    j(sigma_i) = sigma_i,
    s(sigma_i) = sigma_(6-i)^(-1),   i=1,2.

The two homomorphisms have disjoint strand supports. The top and bottom endcaps consist of a four-endpoint tangle plus an outer cap.

Let C be the six-strand cap with nested pairings (1,6), (2,5), (3,4). Replacing the top tangle by infinity gives exactly C. A crossing can slide around a cap, yielding the actual tangle isotopy

    C sigma_i = C sigma_(6-i),   i=1,2.

Consequently C sigma_i sigma_(6-i)^(-1) = C, with the same identity for inverse generators. Because the left and right braid blocks commute, the letters in j(alpha)s(alpha) can be interleaved into such cancelling pairs. Therefore

    C j(alpha)s(alpha) = C

as tangles, for every braid alpha, without evaluating an invariant. After cancellation, the opposite endcap leaves a split outer circle together with the denominator closure D(U):

    L_alpha(infinity,U) is isotopic to O disjoint-union D(U).

The reflected bottom-cap argument gives L_alpha(T,infinity) = O disjoint-union D(T). These are isotopies, not just bracket identities.

A tangle is called simple here when T+infinity is isotopic relative endpoints to infinity. For two-arc tangles, D(T)=O implies this: capping the two right endpoints leaves a proper arc whose closure by a boundary arc is the unknot, hence that proper arc is unknotted; the other arc of T+infinity is trivial. Integer additions preserve this property by Reidemeister I moves at the cap.

For simple T,U, consider

    K(p,q) = L_alpha(T+<p>, U+<q>).

Band surgery at either twist site replaces the integer twist block by infinity. Simplicity and the preceding cap cancellation turn the resulting link into the actual two-component unlink, uniformly in alpha,p,q. Thus every knot in this family has a presentation as a one-band ribbon knot at each of the two sites. Full twists preserve endpoint connectivity, so a parity class containing a knot consists of knots.

## Infinite-family exclusion from known homology results

[Lobb, The Kanenobu knots and Khovanov–Rozansky homology, Theorem 1.4](https://maths.dur.ac.uk/users/andrew.lobb/kbu.pdf) applies to a knot presented by one ribbon band on the actual two-component unlink. Its reduced sl(2) homology is the unknot summand plus a complement, and adding a full twist shifts the complement's gradings. In particular, reduced Khovanov dimension is unchanged. The theorem requires the geometric unlink band resolution, not a Jones-polynomial equality.

Apply it first at the p-site and then at the q-site. If K(p0,q0) is an actual unknot, every knot K(p0+2a,q0+2b) has reduced Khovanov dimension one, for all integers a,b. [Kronheimer–Mrowka, Khovanov homology is an unknot-detector](https://arxiv.org/abs/1005.4346) then makes every such knot an unknot. This proves an entire parity lattice is unknotted; no assertion about Jones detection is used.

For opposite twists K(n,-n), certified anchors at n=0 and n=1 therefore exclude **every integer n**. All 72 integer-tangle seeds tested below have both anchors. For each certified nonrational-tangle seed below, at least its full-twist parity lattice is excluded. We did not certify every other parity class for those nonrational seeds and do not claim that extension.

[Watson, Knots with identical Khovanov homology, Lemma 4.2](https://arxiv.org/abs/math/0606630) gives a separate half-twist invariance result for compatible simple tangles, but in that section restricts the central three-braid to sigma_1^(-1) sigma_2 sigma_1^(-2m). It should not be quoted as a theorem about every arbitrary alpha in our sample. The Lobb argument above is the appropriate full-twist argument for our general mirrored-braid template.

## Nonrational building block

In the convention delta=-A^2-A^(-2), positive integer crossing b=A^(-1)+A e, and e^2=delta e, put

    T = <-1> + <1/2> + <1/3>,   Q = rotate(T).

For T the two bracket coefficients are

    f = A^2 - 2A^(-2) + 2A^(-6) - A^(-10),
    g = A^4 + A^(-8) - A^(-12),
    delta*f + g = 1.

T has an actual unknot numerator, certified in the first pass by five checked Reidemeister moves; hence Q has an actual unknot denominator and is simple. T is nonrational: its classical fraction is -1/6, whereas the rational tangle of that fraction has a monomial infinity coefficient up to framing, and g has three terms. Rotation preserves nonrationality.

Algebraically e[Q]=e. Geometrically eQ=e as well, because Q is simple. This is therefore not a nontrivial kernel element. The same distinction rules out treating cap absorption itself as a new candidate construction.

## Reproducible experiments

All Jones evaluations here are exact full Laurent polynomials, not numerical specializations or Taylor jets. Simplification success to a crossing-free one-component diagram certifies an unknot. Initial failure of a simplifier is not evidence of nontriviality.

1. **Compositions of the nonrational seed.** `tangle_search.py` sampled 20,000 expressions, each containing 2–6 copies of T, Q, or their mirrors, with intervening integer additions and rotations. Both closures were evaluated: 40,000 evaluations. There were 112 monomial-bracket hits, all with two seed copies. `tangle_search_diagrams.py` reconstructed all 112 as actual diagrams; all simplified to the unknot. Their diagrams initially had 12–16 crossings. Data: `tangle_search_hits.json`.

2. **Generalized Watson opposite twists.** `watson_search.py` sampled 1,000 freely reduced three-braid words of lengths 10,14,18,22,26, using random seed 20261102. It retained 72 words whose K(0,0) was certified unknotted. For each it tested n=-5,-2,-1,1,2,5: 432 actual knots, all Jones polynomial one. Regina's first simplification pass reduced 380; Spherogram's global simplification reduced the remaining 52. All ended with zero crossings and one component. There are **no unresolved candidates**. Data: `watson_search.json`; follow-up: `watson_classify.py`. The preceding theorem excludes the complete integer n-family for each of these 72 seeds.

3. **Actual nonrational substitutions.** `watson_q_search.py` used the same 72 braid seeds and four pairs (Q,-Q), (Q,Q), (Q+<2>,-Q+<-2>), and (Q+Q,-Q). All 288 actual knots had Jones polynomial one and simplified to the unknot. Data and original planar-diagram codes: `watson_q_search.json`. Every one of these inputs is simple at both sites, so its certified unknot seed also excludes a complete full-twist parity lattice.

The model was calibrated against the figure-eight and 5_2 instances in [Watson's original generalized construction](https://personal.math.ubc.ca/~liam/files/preprint.pdf): exact polynomials agree across opposite twists. These finite samples are not an exhaustive census of braid words or tangles.

## What this changes about the search

An unknot-seeded two-band construction with actual unlink smoothings is a dead end for finding a Jones counterexample by full-twist insertion: Khovanov theory already excludes it. The next construction would have to preserve Jones cancellation while avoiding that geometric unlink-smoothing hypothesis, or start with an actual nontrivial Jones-one anchor, which is the original problem. We did not find such a construction in this pass.

For a fixed template of two-strand twist sites, one can separately classify possible Jones-one parameters by writing the bracket as a finite sum of monomials with affine integer exponents, after fixing parities and clearing fixed denominators. Cancellation partitions impose affine integer equations. This can reduce the parameter search to finitely many affine integer loci, but the knot types on those loci still require topology. No general classification of those loci or topology was established here.
