# Fixed twist templates: an elementary lattice-locus statement

Independent audit, 31 October 2026. This is an elementary algebraic observation; no novelty claim is intended.

**Statement.** Fix a link-diagram template with k disjoint two-strand twist boxes. Let m_i in Z denote the number of signed half-twists in box i, and fix a parity vector r in (Z/2Z)^k for which the closures are knots. Then

    { m in r + 2 Z^k : V_(K_m)(t) = 1 }

is an effectively computable finite union of affine integer lattices. Here an affine integer lattice means a set m_0 + L with L a subgroup of Z^k; its rank may be less than k or zero. The empty union is allowed.

The same conclusion holds after imposing fixed affine integer relations between the parameters, including repeated parameters. It includes negative twist powers. If one additionally restricts parameters to be nonnegative, bounded, or in another domain, the resulting set is the intersection of this union with that domain; it need not itself be a union of full affine lattices.

## Proof

Use the Kauffman variable A and delta = -A^2 - A^-2. The two-strand Temperley–Lieb algebra over Q(A) has basis I,e with e^2 = delta e. Its positive braid generator is

    R = A I + A^-1 e.

The idempotents P_1=e/delta and P_0=I-e/delta are independent of the twist exponent, mutually orthogonal, and sum to I. Consequently

    R = A P_0 + (-A^-3) P_1,
    R^m = A^m P_0 + (-A^-3)^m P_1       for every m in Z.

The negative-power formula is valid because both eigenvalues are nonzero in Q(A). A reversed convention or mirrored twist box merely changes the sign of the corresponding exponent.

Write m=r+2n, where n ranges over Z^k. Expanding each twist box into its two projector terms and using multilinearity of the bracket gives a sum of at most 2^k expressions

    C_sigma(A) A^[u_sigma + v_sigma dot n],

with fixed rational functions C_sigma and fixed integer exponents u_sigma,v_sigma. The factors (-1)^(m_i) have become constants on the parity class. The coefficients include the evaluation of the fixed outside diagram with the chosen projectors inserted.

A parity class fixes all endpoint pairings and hence the number of closure components. Choose a consistent orientation of these knot closures. Adding two twists preserves the oriented endpoint data. Therefore each twist site has a fixed oriented crossing sign per signed half-twist, the crossing signs outside the boxes remain fixed, and the writhe is affine in n. Multiplication by the Jones normalizing factor (-A^3)^(-w(n)) only alters the fixed coefficients and affine exponent functions. Its sign is constant on the parity class. Equality V_(K_m)=1 is equivalent to equality of this normalized bracket to one.

Subtract one, clear a fixed nonzero Laurent-polynomial denominator, and expand the resulting fixed coefficient polynomials. This produces a finite expression

    F_n(A) = sum_(nu=1)^N c_nu A^[a_nu + b_nu dot n],

where all c_nu are fixed nonzero integers, a_nu are integers and b_nu lie in Z^k. The cleared denominator is independent of n, so F_n=0 is equivalent to the original Jones identity in Q(A). No specialization at a root of that denominator is being used.

For any fixed n, a Laurent polynomial is zero exactly when the coefficients at each exponent sum to zero. Equivalently, the finite index set {1,...,N} admits a partition into blocks B such that

    sum_(nu in B) c_nu = 0,

and, within each block,

    a_nu + b_nu dot n = a_mu + b_mu dot n.

Necessity follows by partitioning indices according to their actual exponent values. Sufficiency follows by summing the zero contribution of each block. **No inequalities between different blocks are needed:** different zero-sum blocks may have the same exponent, because their combined contribution remains zero.

There are finitely many set partitions. Discard partitions containing a block with nonzero coefficient sum. For each remaining partition, equality of the exponents gives an explicit integer linear system M n=d. Its integer solution set is either empty or

    n_0 + ker_Z(M).

Integer solvability, a particular solution and a basis for the integer kernel are effectively computable, for example by Smith normal form. Mapping back by m=r+2n yields an affine integer lattice contained in the chosen parity class. Taking the finite union over partitions proves the statement. If N=0, the locus is the whole parity class.

Affine parameter identifications and additional affine integer constraints simply substitute into, or append equations to, these integer linear systems. This proves the extension claimed above.

## What this does and does not provide

This converts the unbounded twist-exponent problem for a fixed template into finite algebraic data. The computation can be large: there are already 2^k projector choices, denominator expansion creates more terms, and enumeration of all partitions grows according to the Bell numbers. “Effectively computable” is not a claim of practical polynomial complexity.

Each surviving lattice is a certified family with Jones polynomial one. Establishing that every knot in that lattice is an unknot is a separate topological problem; checking a few lattice points does not establish that conclusion. Conversely, any independently certified nontrivial point would be a counterexample. The argument supplies neither a universal bound on templates nor an automatic topological classification of their surviving lattices.

## A conditional geometric way to use a surviving lattice

There is a concrete sufficient condition for turning an infinite surviving lattice into counterexamples. Form the augmented link by retaining the fixed parity crossings and placing one crossing circle around each twist site. Suppose its complement is hyperbolic. Suppose a surviving lattice contains a line n(t)=n_0+t v with every v_i nonzero. Filling crossing circle i with the appropriate slope 1/n_i(t) realizes the full twists, and all these slopes tend to infinity in length as |t| tends to infinity. Hyperbolic Dehn filling then makes the remaining knot complement hyperbolic for all sufficiently large |t|. Those knots are nontrivial, while the lattice certificate makes their Jones polynomial one.

This is a conditional deduction, not an assertion that such a lattice or hyperbolic augmented template has been found. The geometric theorem is the standard hyperbolic Dehn filling theorem; see the original quantitative treatment by [Hodgson–Kerckhoff](https://annals.math.princeton.edu/2005/162-1/p06). This shows precisely how an algebraic lattice search could acquire topological force. If some coordinates stay constant, those cusps would first need to be filled and hyperbolicity of the resulting parent manifold established separately.
