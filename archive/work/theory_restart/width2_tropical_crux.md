# Width-two disjoint-pair cancellations

17 November 2026. Bounded THEORY subtask. This is a written generic-skein
deduction and one finite seven-point combinatorial certificate, not a knot
search. The generic fusion rules are the same Masbaum–Vogel rules already
used in `twobridge_geometry_referee.md` and `necklace_skein_referee.md`.

## 1. The seven sectors, not nine scalar states

Let

    H2 = Hom(V1, V1 tensor V2 tensor V2 tensor V2 tensor V2).

Fuse the first and second arc legs to a, and the third and fourth to b,
where a,b belong to {0,2,4}. Write E_ab for the resulting simultaneous
projector. To couple with the axis V1 and finish at V1, V_a tensor V_b
must have total color0 or2. The complete table is

| (a,b) | (0,0) | (0,2) | (2,0) | (2,2) | (2,4) | (4,2) | (4,4) |
|---|---:|---:|---:|---:|---:|---:|---:|
| rank E_ab | 1 | 1 | 1 | 2 | 1 | 1 | 2 |

The omitted sectors E_04 and E_40 vanish identically. The listed projectors
are mutually orthogonal and sum to I_H2. Their ranks sum to9.

Proof of the ranks: the Clebsch–Gordan interval for V_a tensor V_b contains
color0 precisely when a=b, and color2 precisely when |a-b|<=2<=a+b. Each
occurs once. Count these two possibilities. This proves the table without
constructing a nine-by-nine matrix.

Consequently one arc-pair crossing has eigenspace dimensions (2,4,3) in
channels0,2,4. An axis–arc full twist has dimensions (4,5) in channels1,3:
V2^3 has multiplicities (1,3,2,1) in colors0,2,4,6, so the two dimensions
are1+3 and3+2. This is the multiplicity obstruction to treating width two
as a scalar extension of the width-one ratio automaton.

## 2. Exact opposite-twist spectral degrees

Use the normalization in which an arc-pair half twist X has eigenvalues

    lambda_0=1, lambda_2=-t, lambda_4=t^3.

This agrees with the width-one eigenvalues1,-t; the remaining generic
color4 eigenvalue is obtained from the same half-twist formula. Reversing
all handedness replaces t by t^-1.

For m,n positive, the two disjoint arc-pair twists satisfy

    X1^m X3^(-n)
      = E00 + (-1)^n t^-n E02 + (-1)^m t^m E20
        + (-1)^(m+n) t^(m-n) E22
        + (-1)^m t^(m-3n) E24
        + (-1)^n t^(3m-n) E42 + t^(3m-3n) E44.

In the simultaneous pair-fusion basis, the exact highest and lowest matrix
degrees are

    top = max(m,3m-n),       bottom = min(-n,m-3n).

The fictitious sectors40 and04 would have given top3m and bottom-3n.
Thus their universal absence causes degree losses

    top loss=min(n,2m),      bottom loss=min(m,2n).

This loss is forced by fusion, not a cancellation between nonzero paths.
At n=2m the top operator is

    t^m [(-1)^m E20 + E42],

and at m=2n the bottom operator is

    t^-n [(-1)^n E02 + E24].

Neither bracketed operator vanishes: its summands act on disjoint nonzero
subspaces. A scalar marked closure can nevertheless cancel their images.

These are exact degrees in the simultaneous fusion basis. A t-dependent
change to a TL/link-state basis introduces fixed degree offsets. Therefore
the homogeneous walls alone are not the walls of an arbitrary scalar
coefficient.

## 3. The exact scalar wall test, with outside offsets

Fix arbitrary outside braids/tangles U,V and the actual marked boundary
vectors. Set

    c_ab(t)=phi rho(U) E_ab rho(V)v.

No claim is made that these seven rational functions can be chosen
independently. Choose a common nonzero Laurent denominator D and put
p_ab=D c_ab. Write u_ab=deg p_ab and l_ab=minexp p_ab for nonzero p_ab.
Let [L,U] contain the supports of all nonzero p_ab and put W=U-L.

Assume p20,p42,p02,p24 are all nonzero, and m,n>W. Then only20 and42 can
supply the top degree of D times the scalar coefficient; only02 and24 can
supply its bottom degree. For example, relative to the larger of m and
3m-n, every other sector loses at least min(m,n) before coefficient offsets.
The same calculation applies at the bottom.

The upper equality wall is

    n-2m = u42-u20.

On it, cancellation of the top coefficient occurs exactly when

    (-1)^m lc(p20) + (-1)^n lc(p42) = 0.

The lower equality wall is

    m-2n = l02-l24.

On it, cancellation of the bottom coefficient occurs exactly when

    (-1)^n bc(p02) + (-1)^m bc(p24) = 0.

Away from its corresponding wall that endpoint cannot cancel. If one of
the assumed four coefficients vanishes, remove that sector and recompute
the support envelope; do not apply this four-sector statement unchanged.
Clearing D does not decide flatness by itself: a unit scalar has numerator
equal to a shifted signed copy of D, not necessarily one monomial.

## 4. Infinite unit lines of two full twists

Full twists remove parity signs. Put u=t². After fixed framing units are
removed, the two-parameter coefficient has the form

    F(m,n)=sum_(i,j in S) c_ij(t) u^(i m+j n),
    S={(0,0),(0,1),(1,0),(1,1),(1,3),(3,1),(3,3)}.

Here i=0,1,3 corresponds to fusion color0,2,4. For a line
(m,n)=(m0,n0)+k(p,q), aggregate the terms having equal slope ip+jq.
On a fixed marked knot template, full twists preserve endpoint orientations,
so the preferred normalization differs by a monomial character
`±t^(a+bm+cn)`; it preserves this unit-fiber classification.
Every aggregate is one rational function independent of k. If infinitely
many integer k give a Laurent unit, all but one aggregate must vanish,
and the surviving aggregate must be a Laurent unit (up to the fixed
normalization). Proof: after clearing one common denominator, distinct
nonzero slope groups have disjoint translated supports for |k| large.
Two surviving groups force span to grow without bound, whereas a unit
times the fixed denominator has constant span. This also proves that an
infinite unit subsequence on a fixed line forces the entire line to be
unit-valued in the stated raw normalization.

The complete nonaxis collision directions, up to nonzero scaling and
overall sign, are

    (1,-3), (1,-2), (1,-1), (1,1),
    (2,-3), (2,-1), (3,-2), (3,-1).

At (1,1) there are two pairs and three singletons; at (1,-1) there is one
triple and four singletons. Each other direction in the list has exactly
one pair and five singletons. A nonaxis direction outside the list has
seven distinct slopes. The classification is a finite consequence of the
21 pair differences in S, verified by the exact certificate below.

Hence an infinite line with both parameters varying can have at most
five nonzero c_ij. At least four active sectors restrict its direction to
one of the two diagonals; at least five restrict it to (1,1); six active
sectors exclude every such line. These are necessary support conditions,
not sufficient realization conditions. Axis-parallel lines are excluded
from these statements and must be treated by the one-site channel test.

The two diagonal identities expose exactly which cancellations matter.
For n=m+r the five slope groups are

    c00;
    c10 + u^r c01;
    u^r c11;
    u^(3r)c13 + u^r c31;
    u^(3r)c33.

Their slopes are0,1,2,4,6. For n=-m+r the groups are

    c00 + u^r c11 + u^(3r)c33;   [slope0]
    u^r c01, c10, u^(3r)c13, u^r c31;   [slopes-1,+1,-2,+2].

All but one group must vanish; the remaining group must be a unit.
In fusion-color labels this gives two practical design requirements:

- Opposite-sum flat lines require at least three of c02,c20,c24,c42 to be
  identically zero. If one survives, the central triple c00+u^r c22+
  u^(3r)c44 must cancel. If none survives, that triple itself must be a unit.
- Same-sign flat lines require at least two of c00,c22,c44 to vanish. If a
  diagonal singleton survives, both off-diagonal pair sums must cancel.
  If an off-diagonal group survives, all three diagonal singletons vanish.

These exact zero/identity conditions, rather than a large observed span
deficit, are concrete targets for the outside-tangle construction lane.
They apply to a fixed two-site template. They do not exclude isolated
unit parameters or establish Lemma Q for arbitrary width-two words.

Combining this with the banked D-MULTITWIST finite-union-of-affine-flats
theorem: if at least six sectors are active, every positive-dimensional
piece of the preferred Jones-unit locus is axis-parallel. If the two
one-site flat alternatives are separately excluded, the entire
two-parameter unit locus is finite. This conclusion still allows isolated
unit parameters and does not identify them as nontrivial knots.

## 5. Finite certificate used

One exact enumeration of the pair differences of the seven fixed points
was run; no braid or knot words were enumerated. The primitive normal
directions and their nonsingleton groups were:

    (0,1):  {00,10}, {01,11,31}, {13,33}
    (1,-3): {00,31}
    (1,-2): {10,31}
    (1,-1): {00,11,33}
    (1,0):  {00,01}, {10,11,13}, {31,33}
    (1,1):  {01,10}, {13,31}
    (2,-3): {01,33}
    (2,-1): {01,13}
    (3,-2): {10,33}
    (3,-1): {00,13}.

Each pair of equal projections must appear on this list, because its
direction is perpendicular to one of those 21 point differences. This is
also a direct hand-checkable certificate of completeness.

Independent internal audit: `width2_marking_fusion` accepted the ranks,
spectral envelope, offset walls/signs, seven-point direction list, active
thresholds, and diagonal formulas. Its marking report supplies the actual
canonical template `s.l1.l3.W.u2.u2`, W using indices0..3 with spectator5
fixed. Arbitrary words using index4 are not covered by that canonical
marking. No connectivity or nontriviality assertion is inferred from the
algebra alone.

## 6. Seven-probe sector tomography

The seven coefficients of this fixed marked two-site template can be
recovered from exactly seven raw evaluations, without first constructing
the full nine-dimensional module. Take

    F(m,n),  m=0,1,2 and n=0,1,
    together with F(0,2).

Use u=t² as above and

    V = [[1,1,1], [1,u,u³], [1,u²,u⁶]].

Its determinant is `(u-1)(u³-1)(u³-u)`, nonzero over Q(t). For each n=0,1,
solve

    (r0(n),r1(n),r3(n))^T
      = V^-1 (F(0,n),F(1,n),F(2,n))^T.

The forbidden sectors give

    r0(n)=c00+c01 u^n,
    r1(n)=c10+c11 u^n+c13 u^(3n),
    r3(n)=c31 u^n+c33 u^(3n).

Hence the first and third rows are already determined:

    c01=(r0(1)-r0(0))/(u-1),
    c00=(u r0(0)-r0(1))/(u-1),
    c33=(r3(1)-u r3(0))/(u³-u),
    c31=(u³ r3(0)-r3(1))/(u³-u).

Equivalently their next values are

    r0(2)=(1+u)r0(1)-u r0(0),
    r3(2)=(u+u³)r3(1)-u⁴ r3(0).

The seventh probe supplies

    r1(2)=F(0,2)-r0(2)-r3(2).

One last V-inversion of `(r1(0),r1(1),r1(2))` gives `(c10,c11,c13)`.
This proves uniqueness of the seven-probe recovery. It also predicts the
two omitted corners of the three-by-three sample grid:

    F(1,2)=r0(2)+u r1(2)+u³ r3(2),
    F(2,2)=r0(2)+u² r1(2)+u⁶ r3(2).

These are useful independent calibration checks of the marked template,
not extra data needed to fit its seven coefficients. Recovery is over the
generic rational-function field; do not invert V directly at roots where
its determinant vanishes.

All seven evaluations must use one consistent raw framing, after the
same known generator normalization to eigenvalues1,u,u³. A single common
outside unit only rescales all recovered coefficients. Independently
preferred-normalizing each probe destroys the linear system unless its
known affine framing character is undone first. The argument proves
tomography of a template already known to have this seven-sector form;
seven fitted values alone do not establish that geometric premise.
