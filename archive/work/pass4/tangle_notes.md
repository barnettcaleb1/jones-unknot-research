# Fourth pass: complete two-site Ren twist calculation

No general solution of Jones unknot detection is claimed. This pass gives an exact all-parameter result for a specified infinite family, rather than another bounded parameter scan.

## Actual family and identification

Start with the six-strand braid

    B = (sigma2^-1 sigma1^3 sigma2^-1)(sigma4 sigma5^-3 sigma4).

Cap positions 3 and 4 at both top and bottom, retaining positions 1,2,5,6 as the four strands crossing an annular seam. At the top insert sigma1^p sigma5^q before taking the annular closure. This is the two-site extension of Figure 1 of [Ren, arXiv:2609.11084v2](https://arxiv.org/abs/2609.11084v2); p=q=1 recovers its knot. Odd p,q keep the one-component connectivity. The oriented writhe is p+q: the ten-crossing base contributes zero, and the two twist sites have positive signs in the displayed convention. Full twists do not change the connectivity or those local orientations.

In the paper's published 20-crossing planar-diagram code, the variable sites are zero-based crossing 8, tuple (31,27,32,26), and crossing 5, tuple (17,13,18,12), respectively. All four resolved annular bracket polynomials at these sites were matched exactly against the TL6 model using the independent 4,096-state data from the previous pass. Thus the model identification does not rely only on matching the original knot's polynomial.

## Full exact bracket

Write delta=-A²-A⁻². For an integer twist,

    sigma^p = A^p I + g_p e,
    g_p = ((-A^-3)^p - A^p)/delta.

The formula is valid for positive, zero, and negative p. Compute the four annular bracket blocks B00,B10,B01,B11 by inserting I or e at the two sites. Then

    <K(p,q)> = A^(p+q)B00 + g_p A^q B10
               + A^p g_q B01 + g_p g_q B11.

All four blocks have annular degree at most two, and B11 has degree zero. Their complete integer Laurent coefficients are in `tangle_ren_twists.json`. The computation uses all 132 crossingless TL6 basis diagrams, with an explicit annular closure operation.

## No degree-zero member for any integers p,q

Let a(p,q) be the coefficient of z². Put y=A⁴ and

    P(y)=1-y+2y²-y³-y⁴-2y⁶-y⁸+y⁹,
    Q(y)=1-y-2y³-y⁵-y⁶+2y⁷-y⁸+y⁹,
    R(y)=1-2y+3y²-4y³-4y⁶+3y⁷-2y⁸+y⁹.

The exact four-block calculation reduces a(p,q)=0 to

    (-1)^p P(y)y^(-p) + (-1)^q Q(y)y^(2-q) = -yR(y).

All three polynomials have degree 9 and constant and leading coefficients 1. Set r=-p and s=2-q. If r differs from s, the left side has Laurent breadth 9+|r-s|, because its extreme terms cannot cancel. The right side has breadth 9. Therefore r=s. But then p,q have the same parity, so the extreme coefficients of the left side add to either +2 or -2; the right side has extreme coefficients -1. Equality is again impossible.

Consequently the annular bracket has **degree exactly two for every pair of integers p,q**. There are no degree-zero cases whose topology remains to be checked.

## Determinant with an additional meridional twist

For odd p,q, let n be the meridional-twist parameter, with convention that the spin-two channel gains A^(8n). The exact specialization is

    V_{p,q,n}(-1) = (-1)^((p+q)/2)
        [36+30p-30q-25pq-50(p+q)n].

This follows without numerical approximation. At A⁴=-1, the four a-block values, written as A^r times an integer, are (r,value)=(2,0),(0,25),(0,25),(0,0). After dividing each constant block by delta, its corresponding root values are (0,36),(2,30),(2,-30),(0,25). Since e²=0 at this root, sigma^p=A^p(1+pA^-2 e). These data give the displayed formula, including the limiting contribution from meridional twisting.

The bracket expression has a removable zero/pole at delta=0; setting A^(8n)-1 to zero before taking that limit would incorrectly discard the n-term.

Because the expression inside square brackets is 1 modulo 5, determinant one requires

    (5p+10n+6)(5q+10n-6)=100n²-1.

For n=0 this has the sole integral solution p=-1,q=1. For general n it has other solutions, so determinant alone must not be described as excluding the entire three-parameter family. Since these patterns have winding zero, the determinant is unchanged by inserting a companion knot; this necessary obstruction therefore also applies to satellites.

## Complete Jones-one locus and independent audit

The root agent's `ren_jones_locus.py` uses the full four-block polynomial, not merely the determinant. Write

    Fa = delta² A^(-p-q) a,   Fb = delta² A^(-p-q) b,
    Delta2 = delta²-1.

For odd p,q and writhe p+q, the exact Jones-one equation is

    (A^(8n) Delta2+1)Fa + Fb - delta³ A^(2(p+q)) = 0.

I independently checked this normalization, the odd-power signs, the affine exponent conversion p=1+2m,q=1+2l, and the branch algorithm's completeness. Every nonzero group of coincident monomials at a true solution must meet a group with opposite coefficient sign. The solver branches over every possible such equality. Grouping after rational row reduction removes identities already imposed; every remaining equality between distinct slopes strictly increases the constraint rank. There are three integer parameters, so depth at most three is exhaustive. Rowwise divisibility pruning supplies necessary conditions and cannot discard an integral solution. The resulting sole leaf has full rank, so no residual lattice-integrality issue remains.

Its sole all-integer solution is

    (m,l,n)=(-1,0,0), equivalently (p,q,n)=(-1,1,0).

The actual diagram for p=-1,q=1 was independently reconstructed. Regina and Spherogram both reduce it to zero crossings and one component. Thus the unique Jones-one member is an actual unknot. Original planar-diagram data and both simplification results are saved in `tangle_ren_geometry.json`.

This classifies ordinary closures with the unknot as companion. It does not classify arbitrary companion knots, whose satellite Jones evaluation includes a colored companion invariant. In particular, the special p=-1,q=1 pattern is an unknot in S³ while remaining geometrically essential relative to its axis; the braid agent's separate cable computation certifies wrapping number four throughout this family.

## Reproducible files

- `tangle_ren_twists.py/.json`: four exact blocks, P/Q/R identity, root specializations, determinant formula.
- `tangle_ren_site_map.py/.json`: exact identification of the two published-PD sites.
- `tangle_ren_geometry.py/.json`: independent actual diagrams, writhe and determinant checks, and the unique unknot's simplification.
- `ren_jones_locus.py/.json`: root agent's complete unbounded integer-parameter cancellation certificate, independently audited here.
