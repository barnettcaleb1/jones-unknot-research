# Geometry of affine Jones fibers in a fixed multitwist template

2026-11-03. Bounded theory/referee pass, no computation. The balanced-partition statement below is the parent's algebraic deduction; this note checks its consequences and the geometric step that does not follow. No novelty claim.

## 1. The algebraic statement really gives whole integer lines

Fix finitely many disjoint disk-twist sites and use full-twist integer parameters n in Z^k. After clearing a nonzero denominator depending only on A and including the exact writhe correction, equality with a fixed Jones polynomial is of the form

    sum_{s in S} c_s A^(a_s + b_s dot n) = 0,

where S is finite, c_s are nonzero integers, a_s are integers, and b_s lie in Z^k.

For every partition of S whose blocks have coefficient sum zero, impose equality of the affine exponents within each block. Its solution set is an integer affine flat, possibly empty. The union over these finitely many balanced partitions is exactly the Jones fiber. Indeed, an actual zero partitions its terms by equal exponent, and conversely balanced blocks cancel even if two blocks also collide. Thus no inequations or exclusions of coincident blocks are needed.

A nonempty flat is n_0 + ker_Z(B) for an integer matrix B. If the total fiber is infinite, at least one flat has positive rank and contains n_0 + m v for every m in Z, with v a nonzero integer vector. **This is a nonconstant parameter line, not necessarily a family of distinct knot types.** Nugatory twists and redundant coordinates remain possible.

For half-twist conventions one first fixes the parity classes: signs and possibly connectivity can depend on them. Full disk twists avoid this issue. Without that restriction, the correct formulation allows affine sublattice cosets rather than only saturated affine flats.

This is a particularly elementary function-field instance of the structure studied in [Laurent, *Équations exponentielles polynômes et suites récurrentes linéaires* (1987)](https://www.numdam.org/item/AST_1987__147-148__121_0.pdf). The direct proof is stronger for the present purpose than invoking a general exponential-equation theorem: the formal monomials A^e are linearly independent, and the finite partitions explicitly describe every solution locus. It requires no arithmetic specialization, ineffective finiteness theorem, or general Mordell–Lang machinery.

## 2. What is already in the twist-bracket literature

[Champanerkar–Kofman, *On links with cyclotomic Jones polynomials* (2006), Proposition 2.1](https://www.math.csi.cuny.edu/~abhijit/papers/cjp_AGT.pdf), defines the multivariable twist-bracket and gives

    delta^k <L_n> = A^(sum n_i) P(A,(-A^-4)^n_1,...,(-A^-4)^n_k).

The general finite-disk spectral expansion is also in their earlier 2005 twisting paper. Thus the finite-support input is established prior art; the present balanced-partition deduction should not be advertised as discovering the multivariable description.

Examples 4–5 of the 2006 paper explicitly calculate Kanenobu templates:

    P(A,x,y) = delta^2 (<8_9>-1+xy),
    P(A,x_1,...,x_k) = delta^k (<L_0>-1+product x_i).

With their writhe convention, fixed sum of twist parameters gives a constant Jones polynomial. These are explicit affine hyperplanes of equal values, not evidence that every constant fiber has that particular topology or that its constant value can be 1. The paper does not state the general balanced-partition classification in the portions checked. Priority for that elementary deduction remains unassessed.

## 3. Why one integer parameter is not one disk twist

Along a line n=n_0+m v, the operation is simultaneous twisting by v_i m at each active site. In the tensor-product spectral expansion, its slope on a color tuple j is

    E_j(v) = sum_i v_i [j_i(j_i+2)-3w_i^2].

Many different color tuples can have the same slope. In particular, for two equal local winding numbers and v=(1,-1), every diagonal pair j_1=j_2 has slope zero. Consequently a constant family need not reduce to one surviving color, and the one-disk divisibility argument at A=-1 no longer isolates a single quantum dimension. Opposite compensation is a real escape from D-TWIST-FIBER, not a contradiction to it.

There is also a direct geometric obstruction to collapsing the operation. Suppose a marked realization places the twist supports on a common punctured disk with pairwise disjoint, nonisotopic essential curves c_1,...,c_s. If at least two v_i are nonzero, then

    f = product_i T_(c_i)^(v_i)

is not a power of a single Dehn twist, nor conjugate to one.

**Proof.** If f=T_d^a with a nonzero, then f fixes every c_i. A nonzero twist about d fixes c_i only if their geometric intersection is zero. Hence d is disjoint from the entire multicurve. Dehn twists about distinct disjoint essential curves generate a free abelian group, so equality forces d to be one c_i and all other v_i to vanish. Conjugacy merely changes d. The free-abelian statement is recalled and used in [Birman–Lubotzky–McCarthy (1983)](https://www.math.columbia.edu/~jb/abelian-solvable.pdf). QED.

This is an obstruction in the marked surface/tangle category. It does not exclude arbitrary Kirby moves, stabilization, or an accidental alternative single-disk presentation of the resulting *closed knots*. Those would require additional geometric arguments. Not every arbitrary collection of three-dimensional twisting disks has the common-surface realization used in this lemma.

## 4. Annulus twists are a separate geometric operation

Two 0-framed disk-twist circles forming an unlink can be joined by an embedded annulus in S^3. Opposite equal-magnitude surgeries can then be packaged as an annulus twist. This packaging does not make the annulus a disk, does not make it disjoint from K, and does not supply the extra band-presentation hypotheses used to preserve a specified surgery on K.

General annulus twists are broader still: their boundary components can be linked or knotted. The annulus and its induced boundary framings are geometric input, not a consequence of an affine relation among Laurent exponents. [Abe–Jong–Luecke–Osoinach, arXiv:1409.4851v2, Section 2](https://arxiv.org/html/1409.4851v2) defines this operation and exhibits opposite-slope surgery families with a common integer surgery. It supplies no general ordinary-Jones preservation theorem.

A useful distinction persists even after forgetting the marked tangle:

**Lemma.** Every fixed finite disk-twist template has a uniform upper bound on the bridge numbers of all its knots.

**Proof.** Place each fixed twisting ball in a height coordinate in which its strands are vertical. A full twist is inserted as a braid and introduces no maxima or minima. Arrange the fixed outside arcs in Morse position. Their finite number of maxima bounds the bridge number for every parameter choice. QED.

By contrast, Theorem 2.2(1) of Abe–Jong–Luecke–Osoinach gives annulus-twist families whose bridge number tends to infinity when their fixed auxiliary surgery parameter is nonzero. Such a family cannot be represented by **any** fixed finite disk-twist template, much less a single disk, even if one asks only for equality of knot types. This prevents using “annulus twist” and “compensating disk twists” interchangeably. It does not forbid a particular bounded-bridge annulus family from having a disk-template description.

## 5. The concrete geometric consequence worth retaining

Let n_0+m v be an integer line of Jones-unit values. Fill the coordinates with v_i=0 at their fixed slopes, and leave the active twisting circles unfilled. Denote the resulting augmented-link exterior by M_v. Its boundary includes the knot cusp and the active twisting-circle cusps.

**Proposition.** If M_v is finite-volume hyperbolic, then all but finitely many knots on the line are hyperbolic Jones-trivial knots. Infinitely many of these knots are distinct.

**Proof.** Every active slope is -1/(n_0i+m v_i), in the chosen disk convention, and has length tending to infinity as |m| tends to infinity. The hyperbolic Dehn filling theorem therefore gives hyperbolic knot exteriors for all sufficiently large |m|. Their volumes tend to Vol(M_v), strictly from below. They cannot comprise finitely many isometry types, since a finite set of strictly smaller volumes cannot converge to Vol(M_v). Jones-unit equality holds on the entire line by construction. QED.

The same hyperbolic-filling mechanism is used explicitly in the proof of Theorem 2.2(2) of the above annulus-twist paper; the present deduction is the direct multicusp version.

For a positive-dimensional affine flat, one can choose an integer direction nonzero in every coordinate that is nonconstant on that flat. The coordinates constant on the whole flat are filled first. Thus the active-augmentation test applies to the full geometric variation of the flat, not merely a poorly chosen direction with unnecessary zero entries.

This gives a precise next geometric question: **does a balanced Jones-unit flat force its active augmented exterior to be nonhyperbolic?** A positive answer would exclude infinite unit fibers with hyperbolic augmentation. A counterexample to that statement would immediately produce actual counterexamples to Jones unknot detection by the proposition. Nothing in the exponent partition supplies that topology. Also, excluding positive-dimensional unit flats would still leave isolated integer parameters; it would not prove the full conjecture.

## Assessment

Keep the affine-line extraction and the conditional hyperbolic-filling proposition. Do not collapse an affine direction to one disk merely because it has one integer parameter. The marked multitwist obstruction and the bridge-number distinction show why that reduction needs substantive geometry. The unresolved content is the topology of the active augmentation on a Jones-unit flat; no general reduction by annulus or band surgery was established here.
