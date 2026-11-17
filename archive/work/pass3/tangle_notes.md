# Third bounded pass: adversarial audit and a new annular construction

Pass window: 2026-10-31, 17:42–18:02 UTC. No solution of Jones unknot detection is claimed.

## Main new concrete test: Ren's annular cancellation

The primary preprint [Qiuyu Ren, A counterexample to the wrapping number conjecture, arXiv:2609.11084v2](https://arxiv.org/abs/2609.11084v2), revised September 14, 2026, gives a knot in a solid torus with wrapping number four but annular bracket degree at most two. Its proof uses an explicit cancellation related to a six-strand Burau-kernel construction. Thus actual geometry can cancel the highest annular channel; this is more than a formal skein combination. It does not establish degree zero or a Jones-one knot.

I independently computed the complete annular bracket from the paper's published planar-diagram code. The code includes the knot K and an unknotted annular axis U. It has 12 self-crossings of K and eight K–U crossings. The state sum resolves all 4,096 choices at the 12 self-crossings; linking with U classifies each resulting state circle as essential or contractible. This uses the annular projection represented by this diagram: its smoothed circles lie in the annulus and have winding zero or absolute winding one. It is not a claim that linking number detects geometric essentiality for arbitrary knots in a solid torus. A separate Hopf-pairing calculation using Regina's exact ordinary Jones polynomials agrees.

With delta=-A²-A⁻² and the published blackboard framing (writhe 2),

    <K>_annular = a(A) z² + b(A),

    a = -A¹² + 2A⁸ - 5A⁴ + 9 - 11A⁻⁴ + 11A⁻⁸
        - 7A⁻¹² + 3A⁻¹⁶ - A⁻²⁰,

    b = A¹⁶ - A¹² + 2A⁸ - 2A⁴ - 2 + 2A⁻⁴ - 4A⁻⁸
        + A⁻¹² + A⁻¹⁶ - A⁻²⁰ + A⁻²⁴.

In particular, the annular degree is exactly two. The ordinary knot has

    V_K(x) = x¹⁰ - 2x⁸ + 2x⁶ - 2x⁴ + 2x² - 1 + x⁻²,

where x=sqrt(t), and simplifies to a six-crossing diagram. It is not an unknot anchor.

### Every meridional twist is excluded

For a winding-zero annular knot with annular bracket a z²+b, use the colored basis S₂=z²−1 and S₀=1. A normalized meridional twist multiplies these two channels by A⁸ and 1. Hence, with one choice of twist sign,

    V_n = V_0 + (A^(8n)-1) C₂,
    C₂ = a(delta²−1) / (delta A⁶).

The opposite sign convention replaces n by −n and does not change the conclusion. Here deg_A(C₂)=8, while deg_A(1−V_0)=4. If V_n=1, then

    A^(8n) = 1 + (1−V_0)/C₂.

The rational function on the right has degree zero at infinity. Thus n=0, but V_0 is not one. Consequently **no integer meridional twist of this example has Jones polynomial one**. This is an all-integer argument, not a finite twist scan.

The Hopf-pairing check uses Delta₂=delta²−1 and lambda₂=−A⁶−A⁻⁶. The bracket of K together with its axis is

    a Delta₂ lambda₂ + (a+b) delta.

It exactly matches the independently computed two-component-link Jones polynomial after restoring framing and the unreduced unknot factor.

### Exhaustive crossing-sign test

We then retained Ren's annular projection and tested **all 2¹²=4,096 choices of crossing signs** at the twelve self-crossings. State-circle data remain fixed. For sign mask h, the bracket is

    sum_s A^(12−2 popcount(s XOR h)) delta^c(s) z^e(s).

Two modular Walsh–Hadamard convolutions screen the coefficients of z² and z⁴ simultaneously. Every survivor is then checked using exact integer Laurent polynomials, so the modular screen introduces no accepted false positives. A true zero cannot be discarded by either modular screen.

Exactly **234** sign choices have annular degree zero. All 234 have ordinary Jones polynomial one. Their entire K-union-axis diagrams were reconstructed and each simplified to a crossing-free **two-component unlink**. Thus every degree-zero case in this fixed projection is geometrically local; there is no surviving essential annular pattern in this complete sign-choice test.

To check the XOR-mask/actual-diagram correspondence independently, masks 1, 1375, and 4095 were each rebuilt as changed planar diagrams. Both their ordinary Jones polynomial and their Jones polynomial together with the axis agree exactly with the corresponding annular-state evaluation and colored Hopf pairing. These three checks are recorded in the sign-screen JSON.

Reproducibility:

- `tangle_ren_check.py` and `.json`: original PD, all-state calculation, exact annular coefficients, ordinary and axis Jones checks, all-twist exclusion.
- `tangle_ren_signscreen.py` and `.json`: exhaustive 4,096-sign screen, 234 exact hits, and all 234 actual unlink simplification results.
- `ren_source/`: original public TeX source, including explicit diagram construction.

This test does not classify other projections, extra crossings, or other ways of changing the residual degree-two channel.

## Stronger obstruction for proposed EKT replacements

The earlier EKT examples have double-cover homology Z direct-sum a nonzero finite cyclic group. This blocks **any single rational-tangle replacement** to a determinant-one knot, not merely an embedded band.

Proof: suppose the target is a determinant-one knot, with double branched cover Y an integral homology sphere. The common tangle exterior is the exterior of a knot in Y. Its first homology is Z generated by a meridian, and its preferred longitude is zero in homology. Filling slope p*meridian+q*longitude therefore gives Z/p, interpreted as Z when p=0. It never gives Z plus nonzero torsion. The Montesinos rational-tangle/filling correspondence now gives the contradiction. There is no restriction on the distance between the two rational slopes.

More generally, m simultaneous rational-tangle replacements from a determinant-one knot give a cover obtainable by surgery on an m-component link in an integral homology sphere. Its homology has a presentation on m meridians. Therefore m is at least the minimal number of generators of the original cover's homology. For Z plus nonzero cyclic torsion, at least two sites are required. This does not obstruct arbitrary two-site constructions.

## Formal TL₃ unit: stronger nonrealizability conclusion

The previous formal unit

    u = 1 + delta e₁e₂ − e₁

is not just outside the braid image: **it cannot be the bracket of any single actual tangle**.

At A=i, delta=2, and crossing reversal multiplies the bracket by −1. Crossing changes reduce any tangle to a standard connectivity matching and its separated closed components; framing changes add only Gaussian-unit phases. Use the integral spin representation on (Z[i]²) tensor n with E_i=I−P_i, where P_i swaps adjacent tensor factors. It satisfies the Temperley–Lieb relations at delta=2.

If a matching has an arc joining two endpoints on the same boundary side, its spin operator is singular. If all strands pass through, its operator is a phase times a tensor permutation. Each closed component contributes a scalar 2. A bracket that is a unit over Z[A,A⁻¹] specializes to a unit over Z[i], so its spin determinant must be a Gaussian unit. Thus an actual tangle with a unit bracket has no same-side arcs and no closed components; its spin operator at A=i is a phase times a permutation and is unitary.

For the displayed u, put N=2E₁E₂−E₁. Exact integer matrices show N²=0, so I−N is its inverse. But the squared column norms of I+N are

    [1, 9, 5, 1, 1, 5, 9, 1].

It is not unitary and therefore cannot be an actual tangle bracket. The standard-library verification is `tangle_unit_obstruction.py` and `.json`.

This necessary specialization condition does not show that every realizable unit bracket is geometrically a braid. Even the one-strand case includes the original Jones unknot problem.

## Audit of the previous general reductions

The finite-affine-locus method remains valid for a fixed finite template of two-strand integer twist sites. After fixing parity and orientation and clearing fixed denominators, Jones minus one is a finite sum of fixed integer coefficients times monomials whose exponents are affine integer functions of the twist parameters. Partitioning the terms into zero-sum coefficient blocks, and equating exponents inside each block, produces finitely many affine integer solution lattices. Different blocks need not be kept distinct: if they collide, their sums remain zero.

This is not a theorem for arbitrary varying braid words, variable-length continued fractions, or an unbounded collection of templates. It classifies the exact polynomial condition in each fixed template, not the topology of the resulting knots.

No fatal gap was found in the earlier simple-tangle Watson collapse. Its crucial input remains an actual two-component-unlink band resolution, verified by the nested-cap cancellation. The new Ren construction escapes that particular hypothesis, but its surviving annular channel blocks the direct all-twist route, and every degree-zero sign variant of its present projection is an actual unlink pattern.
