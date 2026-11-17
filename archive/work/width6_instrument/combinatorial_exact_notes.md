# Exact cut and monodromy component

Status: a finite geometric instrument with exact arithmetic, not a theorem about tight representatives or tangle splitness.

## Inputs and conventions

The input is a pair of disjoint rational polygonal source arcs and a pair of disjoint figure-eight target loops. `transport_pl.py` constructs each source as the actual image of its standard arc under a composition of piecewise-affine half twists, splitting every segment at every affine cell edge. `transport_exact_intersections.py` gives exact transverse intersections, retaining repeated geometric positions when their parameters differ.

The braiding convention is fixed independently by based-meridian words. If `w` is the chronological **geometric** word, the upward-cut meridians have images

    reverse_each_word( Artin( reverse( negate(w) ) ) ).

The reversal of each image converts the based-word convention; the sign reversal converts the oriented half twist. All ten signed generators and six noncommuting words passed. Matrix words in the pairing are transported by chronological `negate(matrix_word)`.

An open arc's cut word does not itself supply the configuration-space exchange exponent. The geometric representatives and the two-point paths are retained explicitly.

## Exact integer exponents

Puncture cuts are the parallel upward rays `(j+epsilon*y,y)`, `y>=0`, with rational `epsilon`. For each point path, count right-to-left crossings positively and left-to-right negatively. Summing over both point paths and all six punctures gives the puncture exponent `a`. This is ordinary winding, with no trigonometric computation. The cap-cut record includes the unreduced event word, each segment parameter, exact crossing position, and the prefix exponent before and after the event.

For exchange, let `r=z1-z2`. A closed unordered configuration path has `r_final=+r_initial` or `-r_initial`. The projective line of `r` is therefore a closed loop in `RP^1`. Its signed crossings of the full line `x-epsilon*y=0` count its degree, which equals the change of relative argument divided by pi. A crossing of a rational straight segment has sign `sign(det(r_start,r_end))`. This integer is `b`. A collision at an endpoint or in a relative straight segment is rejected; the parity of `b` is checked against the permutation of the two target assignments.

Both exponents use half-open crossing conventions. Prefix constants at puncture endpoints of a source arc are arbitrary and cancel, because the actual configuration paths start and end at interior intersections. Partial-segment queries are exact rational interpolation. The cache changes performance only: it stores the same signed crossings that direct path concatenation would count.

The geometric loop follows the target product from a fixed base intersection to the selected intersection, then returns along the source product. Moving one point at a time gives four path contributions to `b`. The full-line count is invariant under replacing every relative vector by its negative, so the same centered-curve primitive works when the second point moves and when the target assignments swap.

## Files

- `combinatorial_winding.py`: primitive ray/full-line crossings, unreduced cut events, reduced free words, direct configuration-loop monodromy.
- `combinatorial_validate.py`, `.json`: independent Artin and monodromy controls.
- `combinatorial_exact_pairing.py`: cached exact pairing for the rational geometry model; each configuration retains its two actual intersection references, `(a,b)`, and sign.
- `combinatorial_exact_witness14.npz`: compact exact integer records for all 340,350 witness pairs. The six columns are `matching,index0,index1,a,b,sign`.
- `combinatorial_exact_witness14_summary.json`: exact rational one-point records and metadata for that array.
- `combinatorial_exact_basis81.json`: incremental/final exact geometric Gram calibration; consult its status field.
- `combinatorial_original_basis81.json`: direct check against the original nine cap lifts, separate from the effective-seed calculation.

## Completed witness checks

The 14-letter witness required 17.488 seconds for exact geometry and all 340,350 exact exponent pairs. It gives

    -q^-3 + q^-2 - q^-2*t + q^-1*t
    = q^-3 (q-1)(1+qt).

Every `(matching,a,b,sign)` agrees with the independently computed floating-angle layer on the same exact geometric intersections; there were zero mismatches. Recomputing all 340,350 exponent pairs with cut slope `2/103` in place of `1/101` gives exactly the same records. This confirms cut independence in this finite example; no angle rounding is used in the exact result.

The torus target and mixed square/torus normalization still matter: this geometric polynomial is the calibrated mixed pairing Phi up to its documented deck unit. It should not be labeled the raw Budney pairing or the Jones polynomial without applying the specified normalizations.

## Limits

These are unaggregated geometric intersection data. They do not certify that the diagram minimizes intersections over cap slides. Cancellation packets can be inspected on the actual pairs, but a polynomial factor or an arbitrary pairing of opposite contributions is not by itself a disk-induced geometric involution. The instrument establishes no hard implication from a zero Jones coefficient to a split tangle.

Primary definitions: Bigelow, *Braid groups are linear*, JAMS 14 (2001), sections 1.2–2, https://www.maths.ed.ac.uk/~v1ranick/papers/bigelow2.pdf .
