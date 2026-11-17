# Categorical design round: purity is a possible bridge, but no mechanism survived

Scope: T-ROUTES, design only, 2026-11-03. No computation, no scaffold edits. Recommendation: do not promote this to an active proof route yet.

## The strongest precise candidate I can formulate

Use a stability condition or a positive heart on a category containing the link's Floer/trace object. Its central charge would be the full graded Jones character evaluated at a suitable parameter, rather than an ungraded intersection number. In an abelian heart with a faithful positive character, equality with the character of a simple unit object forces the absence of extra composition factors. Thus a geometrically constructed positive heart containing the reduced knot object when V=1 could turn its Jones character into actual rank one; Khovanov unknot detection would finish.

The genuinely geometric missing lemma would be:

> For the Lagrangian pair arising from a classical one-component plat, a Jones-unit character admits a Markov-compatible geometric deformation into a specified positive heart, without changing its Floer object.

“Specified” matters: defining the heart by the desired conclusion merely renames the conjecture. A plausible proof would have to produce a geometric move, filtration, or holomorphic-disc exclusion from the character equality itself. I have found no such move or exclusion. One-component and classical-S3 hypotheses are not yet used by the proposed mechanism, so the barriers are not passed.

## What the known symplectic results actually supply

[Abouzaid–Smith, The symplectic arc algebra is formal](https://arxiv.org/abs/1311.5535), proves formality over characteristic zero using a noncommutative vector field. Their [Khovanov homology from Floer cohomology](https://arxiv.org/abs/1504.01230) identifies symplectic and combinatorial Khovanov homology in characteristic zero. [Cheng, Bigrading the symplectic Khovanov cohomology](https://arxiv.org/abs/2111.07792), refines the grading comparison: the additional weight grading recovers the Jones grading up to shift. Cheng's introduction also distinguishes that comparison from a purely symplectic proof of weight-grading invariance.

These are meaningful geometric structures, but they do not identify the Jones weight with the cohomological degree in a way that prevents cancellation. In particular, “pure noncommutative vector field” in the formality theorem must not be silently replaced by “pure Hodge structure that makes every fixed-Jones-degree Euler coefficient positive.” The former is a statement about higher operations on an algebra; the latter would be an extra statement about the particular morphism/trace object after applying a braid and closing it.

## Cheap obstruction to the naive bridge

Even in the formal derived category of graded vector spaces,

    Q{j} direct-sum Q{j}[1]

is nonzero and has zero graded Euler character. There are no hidden higher products or differentials to blame. It also fits into the usual duality framework after adding its dual. Formality, finite-dimensionality, and duality therefore cannot be the proposed positivity theorem.

This obstruction occurs in actual classical knot homology, not only in an abstract derived category: the GMS Theorem 13, n=1 construction used in work/global_design/n2.md has adjacent homological groups in its lowest quantum row with zero Euler characteristic. Consequently an unconditional positive-heart statement for all classical knot objects is already too strong. Restricting it to Jones-unit objects avoids that example but currently supplies no independent reason it should hold.

A stability-condition version has the same missing implication in a useful numerical form. The central charge is additive; the mass is a sum of absolute central charges of semistable factors. The triangle inequality gives mass >= absolute central charge. Knowing Jones=1 determines the central charge, but gives no reason for equality in that inequality. Mass minimality is the missing theorem, not a consequence of the numerical equality.

## Verdict and revival criterion

This is a well-defined shape a proof could take, but presently it is a reformulation of the Euler-to-object gap. I do not recommend a page asserting new purity or nearby-Lagrangian rigidity. Nearby-Lagrangian statements would require hypotheses such as a suitable projection/homotopy condition on a single exact Lagrangian; a prescribed graded intersection number with another Lagrangian does not supply them.

Revive only after finding an independently motivated geometric filtration or disc-count identity whose positive summands can be read from the full Jones polynomial, and which is demonstrably sensitive to one-component classical topology. Another equivalence of models, or another grading dictionary, does not meet that criterion.
