# Two special sectors: the protected-endpoint case and its limitation

This is a targeted continuation of EARLY-36, not a new general categorification route. The generic invisible-pair construction duplicates EARLY-39/LATE-30/LATE-50 and is not counted as progress. No actual knot/tangle counterexample is constructed below.

## 1. A precise restricted spectral-sequence theorem

Let an E1 page be the direct sum of:

- a rational unlink sector U with two generators in homological degree zero, quantum degrees -1 and 1;
- two copies A and B of the same delta-thin special-sector shape E_n, n>=1, with identical quantum support, but homological shifts differing by an odd integer d.

Here E_n is the published KWZ s_(4n) pairing shape used in EARLY-36: its quantum span is 8n+2, its homological span is 4n+1, and each homological endpoint has a gap of two to the next class of that sector. Each extreme is one-dimensional. The identical quantum support condition permits one common arbitrary quantum shift.

There is no spectral sequence with differentials of degree (1,2r), r>=1, from this E1 page to a rank-two vector space entirely in homological degree zero.

### Proof

Interchange A and B so that B is shifted upward by d>0. Let H be B's top homological degree, and L be A's bottom homological degree. Then H-L=4n+1+d>=6.

The top class at H has no outgoing differential to either special sector. It cannot receive a differential within B because of the top gap. From A an incoming source in degree H-1 can exist only if d=1; it is then A's top class, with the **same** quantum degree, so the required positive quantum shift excludes it. Thus only U can kill this top class: an incoming differential is possible when H=1, and an outgoing differential to U is possible when H=-1. If H is outside {-1,0,1}, it is a permanent cycle outside the allowed limiting degree.

Dually, the bottom class at L has no incoming differential from a special sector. Its own sector has no h=L+1 class, and the only possible B source/target at that next degree occurs for d=1 with the same quantum degree. Thus only U can kill it: an outgoing differential is possible when L=-1, and an incoming differential from U is possible when L=1. If L is outside {-1,0,1}, it is a permanent cycle outside the allowed limiting degree.

Avoiding both contradictions would require H and L both in {-1,0,1}, hence H-L<=2, contrary to H-L>=6. The exclusions persist through all pages because pages are bigraded subquotients of E1. QED.

This is genuinely stronger than applying the one-special theorem to each component separately: it handles the Euler-cancelling pair without needing either copy to have nonzero standalone defect.

## 2. Scoped application to the slope-zero two-special model

Suppose a tangle's preferred zero-filling Kh is the rational unlink sector **with the grading normalization specified above**, plus exactly two multiplicity-one rank-one-local-system s_(4n), s_(4m) sectors. If its Euler polynomial is the unlink polynomial, the two special Euler polynomials must cancel exactly.

Their widths are 8n+2 and 8m+2, so cancellation forces n=m. Their extreme quantum degrees then force equal quantum shifts, and their opposite Euler signs force odd difference of homological shifts. The preceding theorem excludes the required Bar-Natan limit when the zero-filling has linking number zero.

**Calibration gate:** to turn this into a tangle theorem stated only with "rational slope 0 and an actual unknot meridional closure", the rational sector's absolute grading must be checked via the gluing convention. The meridional closure sees only the rational component, so its graded rank-one unknot homology should fix that component's shift; however this note does not silently substitute that statement for an explicit grading calculation. The theorem above includes the normalized rational-sector hypothesis. Its abstract proof is complete within that scope.

## 3. The broader two-special support argument already has a countermodel

For nonzero rational slope, the root's Euler interval-path reduction admits the monotone split k=8=4+4. The following explicit E1 vector space has the unlink Euler polynomial and two special sectors, yet admits a valid abstract Bar-Natan spectral sequence. It disproves a broad claim based solely on those supports and the rank-two h=0 limit.

Rational sector R8:

    (h,q) = (j,2j+1), j=0,...,6, together with (8,17).

First special E1:

    (2,-1), (4,3), (5,5), (7,9).

Second special E2:

    (0,7), (2,11), (3,13), (5,17).

The Euler polynomial is Q+Q^-1: all other coefficients cancel directly. On page one, pair

    R(1,3) -> R(2,5),
    E2(2,11) -> E2(3,13).

On page four, pair

    E1(2,-1) -> R(3,7),
    E1(4,3) -> R(5,11),
    E1(5,5) -> R(6,13),
    E1(7,9) -> R(8,17),
    R(4,9) -> E2(5,17).

The first two arrows have degree (1,2), and the remaining five have degree (1,8). They are disjoint pairs, so all differentials square to zero and can be realized by a direct sum of filtered two-term complexes. The survivors are R(0,1) and E2(0,7), both in h=0. Equivalently, the formal deformed complex has two free generators, two bars of length one, and five bars of length four.

No actual Bar-Natan tangle object or classical link realizes this model as part of this note. It is a spectral-sequence support countermodel only. It is sufficient to stop a proposed universal two-special proof that sees no more than these support and limit conditions.

## 4. A relevant published constraint, without the invalid shortcut

[Alishahi, *Unknotting number and Khovanov homology*, Pacific J. Math. 301 (2019), Theorem 1.2](https://msp.org/pjm/2019/301-1/pjm-v301-n1-p.pdf), proves that maximal h-torsion order in unreduced F2[h] Bar-Natan homology is bounded by the unknotting number. Thus the actual crossing filling K1 in the Lemma-Q setup has torsion order at most one.

This does **not** directly constrain the zero-filling L above: L is a two-component link one band move from U, not an unknotting-number-one knot. Also K+, K-, and L are not simply the three terms of the ordinary resolution triangle. Both crossing complexes involve a second smoothing. A crossing-change cone can introduce multiplication-by-h cones, which can hide the original torsion lengths. One must compute or prove the relevant filling compatibility before using the knot bound to reject this link model.

Potential next gate, not completed here: determine whether every realization of the two-special Euler interval pattern forces torsion order greater than one in the actual slope-1/2 knot filling. This would use the actual unknot anchor in a way the standalone zero-filling support test does not. Reduced/unreduced conventions and the full Bar-Natan pairing must be retained. The existing four-special formal model has length-one bars and is an immediate barrier against extrapolating this idea to all components.
