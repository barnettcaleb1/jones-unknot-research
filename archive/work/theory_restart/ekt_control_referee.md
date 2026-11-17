# EKT two-row control: referee and normalization correction

16 November 2026. Bounded read of Claude000711. No new knot invariant computation or scan: the finite check below uses only the supplied 26-generator graded table and the banked integral cover homology.

## Verdict

The control is valid as a demonstration that a large two-row Euler-cancelling profile occurs for an actual link and can survive entirely in plane Floer homology. Two scope corrections are needed:

1. LL2(1) has the unlink Jones polynomial **up to a nontrivial monomial**, not exactly. Its raw bracket is the unlink's bracket in EKT's diagram convention.
2. Cyclic-cover target rank forces all *excess dimension* to disappear; it does not identify a canonical invisible summand whose named generators must all die.

## 1. Primary-source normalization

Eliahou–Kauffman–Thistlethwaite, *Infinite families of links with trivial Jones polynomial*, Topology 42 (2003), 155–169, §4.1, Theorem 4.1 (printed p.165):

    V_LL2(n)=u for even n,
    V_LL2(n)=t^(+/-6)u for odd n,

where u=−t^(-1/2)−t^(1/2), with the sign in the exponent depending on component orientations. The preceding paragraph gives writhe zero for even n and +/-8 for odd n, although every diagram's bracket is delta. [Primary PDF](https://homepages.math.uic.edu/~kauffman/ekt.pdf).

This is also explicitly recorded in `work/ekt_homology_notes.md`: its exact unlink-Jones claim is only for even n. Thus LL2(1), the supplied linked trefoil/mirror control, is not an exactly Jones-unlink link in the normalized invariant. The displayed graded Euler polynomial

    q^11+q^13=q^12(q^-1+q)

is consistent with the odd-n monomial shift, under the corresponding Jones/Khovanov convention. No choice between the two mirror/orientation conventions is needed for the rank or matching argument.

## 2. The supplied grading table checks internally

Adding (-1)^h q^q across the 26 generators gives q^11+q^13 exactly. Remove one generator at (h,q)=(4,11) from the lower delta row and one at (4,13) from the upper row. The remaining upper row has multiplicities

    1,1,2,2,2,2,1,1

at q=5,7,9,11,13,15,17,19 and has rank12. The remaining lower row is exactly its h-shift. Thus the precise graded decomposition is

    Kh_red(LL2(1)) = h^4 q^12 Kh_red(U2) + X + hX,
    dim X=12.

This is an isomorphism of bigraded vector spaces; it does not pick geometric chain subcomplexes or an invariant splitting. The common q multiplicity reaches two after the two exceptional generators are removed, while the complete rows have multiplicities up to three.

Allowed post-E2 matching edges go from the upper delta row to a strictly larger q in the lower row. Greedy increasing matching gives ten pairs. A Hall obstruction proves optimality: the upper tail q>=13 has seven generators (3+2+1+1), while the lower targets q>13 number four (2+1+1). Its deficiency is three, so at most thirteen-minus-three=ten pairs are possible. The greedy matching attains ten, leaving six generators.

## 3. Actual collapse and formal matching are different

The banked Fox presentation proves

    H1(Sigma2(LL2(1));Z)=Z + Z/13.

Daemi's plane Floer target therefore has dimension 2*13=26. The source also has dimension26, so every actual higher differential is zero and the sequence collapses at E2. This follows just from finite-dimensional rank bookkeeping; no map formula is needed.

The maximum admissible matching of ten pairs is a *possible abstract differential*, not a prediction of the actual Daemi differential. Its residual six is a lower bound on a formal abutment rank. The actual target26 is consistent because the geometric maps all vanish here. This example is therefore a useful calibration of precisely what maximum matching does and does not determine.

The general inequality

    dim_F2 Kh_red(L)>=2^b1(Sigma2L) |Tor H1(Sigma2L;Z)|

is the direct spectral-sequence rank inequality (base extend to Daemi's characteristic-two Novikov field). It is sharp on this control. Its source ledger is already audited in `surgery_collapse_sources_referee.md`.

## 4. Scope of the quotient-tangle interpretation

For the quotient closures with cover S3_(p/q)(kappa), the target rank is |p| if p is nonzero; at the longitude p=0, H1=Z and the target rank is two. Unlike the EKT control, there is no additional finite torsion multiplying the target rank. Accordingly any source dimension beyond these targets must be cancelled.

One should not strengthen that dimension statement to a canonical claim that every generator assigned to X dies and every generator assigned to the rational part survives. Later maps can mix these chosen summands, and even the rational component of the curve invariant need not itself have the target rank. Likewise for a Jones-unit knot the target has rank one, but its representative need not be the initially chosen 'pawn'.

The valid conclusion is the same strategic one as the letter: the two-row bare-B profile is ruled out for the indicated knot closures by its Hall obstruction, whereas multilevel ladders have enough admissible cancellation. This EKT example demonstrates the link control after accounting for its monomial normalization and torsion-rich target; it supplies no new proof of NP/END and no realization of a ladder as a quotient tangle.

## 5. Exact two-row classification for a Jones-unit knot profile

Root's corollary, independently checked by the referee. Let V be a finite
bigraded vector space supported on two adjacent delta levels, with even
quantum gradings and integer graded Euler polynomial one. Set p=q/2.
The two row signs at each p are opposite. Consequently the rows have a
common multiset M of p positions and a single additional generator at
p=0 (the pawn), in the row whose sign gives the positive constant term.

The allowable post-E2 edges are upper p -> lower p' with p'>p. Their
maximum-matching residual is one if and only if:

- with the pawn in the upper row, M has no repeated position and every
  position is strictly positive;
- with the pawn in the lower row, M has no repeated position and every
  position is strictly negative.

The empty multiset is included. For necessity in the first case all lower
vertices must match. At a lower prefix ending at p the available upper
sources are at most |M_{<p}|+1, so multiplicity at p is at most one. At the
minimum, the sole possible smaller source is the pawn, forcing p_min>0.
The second case follows by reversing the order and exchanging the rows.
For sufficiency, write 0<p1<...<pm and match upper0 to lowerp1, upperp1
to lowerp2, and so on. Only upperpm survives. The other case is symmetric.

Thus the initial pawn may die even in the simplest complete admissible
matching. For an actual Jones-unit knot Daemi supplies residual one, so
this is a necessary restriction if its reduced homology has two delta
rows. It is sufficient only for an abstract matching, not for a geometric
spectral sequence or for realization by a knot. It does not classify
profiles with three or more rows or prove NP/END.

## 6. The exact-unlink members need no new computation for a rank bound

The already proved family homology in work/ekt_homology_notes.md is

    H1(Sigma2 LL2(n))=Z + Z/(1+12q_n^2),
    (p_(n+1),q_(n+1))=(3p_n+8q_n,p_n+3q_n), (p_0,q_0)=(1,0).

Daemi therefore gives dim Kh_red(LL2(n);F2)>=2(1+12q_n^2). For n=2,
where the normalized Jones polynomial is exactly the unlink's, q_2=6
and the bound is866. This is an immediate corollary of banked homology,
not a fresh Khovanov calculation; no equality, two-row profile or collapse
is asserted for n=2. The n=1 computed equality26 remains the particular
collapse control.
