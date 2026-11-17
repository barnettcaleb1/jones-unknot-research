# Exact unit loci of the two supplied width-two templates

17 November 2026. Input: the **two fixed** seven-sector tables in
`collab/data/engineB/exact_sectors.json`. This is a classification over all
integer twist parameters, not a parameter scan.

**Conclusion.** In the table's parameter convention:

- Template 1 has precisely one unit point, `(m,n)=(-2,-1)`.
- Template 2 has no unit point.

At the first point the raw evaluation is exactly `t^-8`, and the preferred
evaluation is `J=1`. Its covering knot type is **not certified here**. The
isolated point has a short body word, given in Section 4; it must be identified
geometrically before any nontriviality conclusion is drawn.

**Subsequent geometry check, same round:** `width2_fixed_unit_geometry.md`
identifies that point as an unknot via a local two-bridge determinant1
certificate. The independent script `width2_source_geometry_check.py`
also reconstructs every supplied sector coefficient from the raw matrix
JSON and checks the local Alexander minor. Both templates therefore
contain no nontrivial flat inversion. The moment/degree computation alone
does not supply this topological conclusion.

The symbolic certificate is `width2_fixed_template_gate.py`; its exact output
is `width2_fixed_template_gate.json`, including the SHA-256 of the input. It
uses only the two supplied tables, symbolic derivatives, positivity of explicit
quadratic polynomials on two rays, and the two remaining parameters of the
first conic. All assertions passed.

## 1. Parameter and normalization conventions

Write `e_0=0, e_2=1, e_4=3` and

    F(m,n;t) = sum_(a,b) c_ab(t) t^(2e_a m+2e_b n).

The chronological body word is `V . x1^(2m) . x3^(2n) . U`; negative powers
use the inverse y letter. The seven terms are indexed by
`00,02,20,22,24,42,44`. This is the table's raw invariant; braid-generator
normalizations differing by framing units do not affect its preferred
second logarithmic moment.

Let D=t d/dt and define `F_i=(D^i F)(-1)`. In both templates `F_0=1`.
All exponents `2e_a m+2e_b n` are even, so for `q_ab=2e_a m+2e_b n`,

    F_1 = sum (D c_ab + q_ab c_ab)(-1),
    F_2 = sum (D^2 c_ab + 2q_ab D c_ab + q_ab^2 c_ab)(-1).

The first moment is removed by the preferred framing. Hence

    M_2 = F_2 - F_1^2,          a_2 = -M_2/24.             (1)

The latter identity is the banked second-moment theorem. Here `F_1` is always
a multiple of 8, so the preferred value is exactly `t^(-F_1)F`; no extra sign
occurs at -1. Equivalently, if F is a Laurent unit, its value and logarithmic
derivative at -1 force it to equal `t^(F_1)`.

## 2. The two moment gates

Template 1 has

    V = x0.y2.y2.x1.x1,
    U = x1.x1.y0.x1.

In the sector order above, the triples `(c,Dc,D^2c)(-1)` are

    00: (-3,-6,10)       02: (0,0,48)       20: (4,18,102)
    22: (0,0,-72)        24: (0,-4,-24)
    42: (0,0,12)         44: (0,0,-12).

It follows exactly that

    F_1 = 8m+8,
    F_2 = 16m^2+56m-48n+64,
    a_2(m,n) = 2m^2+3m+2n.                               (2)

Thus an integer unit parameter must satisfy

    m=2k,        n=-4k^2-3k,        k in Z.              (3)

Indeed (2) modulo 2 makes m even, and substitution then determines n.

Template 2 has

    V = y0.y2.y1.x0.x3.y2,
    U = y3.x2.x2.y3.x0.x1.

Its derivative triples are

    00: (9,72,-12)       02: (-12,-54,118)   20: (-12,-54,118)
    22: (16,36,-188)     24: (0,0,12)
    42: (0,0,12)         44: (0,0,-60).

Consequently

    F_1 = 8m+8n,
    F_2 = 16m^2+128mn-72m+16n^2-72n,
    a_2(m,n) = 2m^2+3m+2n^2+3n.                         (4)

The zero locus of (4) is

    (4m+3)^2+(4n+3)^2=18.

The only nonnegative squares summing to 18 are 9 and 9, and the only signed
square root of 9 congruent to 3 modulo 4 is +3. Therefore `(m,n)=(0,0)` is
the only integer solution. At this point the preferred value satisfies

    J(0,0)-1 = (t-1)^2(t+1)^3(t^2+1)(t^2-t+1)Phi_10(t)/t^11,

which is nonzero. This rejects **the entire second template**.

## 3. All parameters on the first template's conic

For Template 1 clear the common denominator

    d(t) = t^8(t^2+1)(t^2+t+1),       p_ab=d c_ab in Z[t].

It has degree 12. On the conic (3), a unit would require

    sum p_ab t^(4e_a k+2e_b(-4k^2-3k)) = d(t)t^(16k+8).  (5)

The right-hand side has top degree `16k+20`. The exact polynomial data on
the left are:

| Sector | min deg p | max deg p | bottom coefficient | top coefficient | shifted top on (3) |
|---|---:|---:|---:|---:|---|
| 00 | 0 | 14 | 1 | -1 | 14 |
| 02 | 0 | 14 | -1 | 1 | -8k^2-6k+14 |
| 20 | 4 | 18 | -1 | 1 | 4k+18 |
| 22 | 4 | 20 | 1 | 1 | -8k^2-2k+20 |
| 24 | 7 | 20 | -1 | -1 | -24k^2-14k+20 |
| 42 | 15 | 28 | -1 | -1 | -8k^2+6k+28 |
| 44 | 15 | 28 | 1 | 1 | -24k^2-6k+28 |

For `k>=1` the target degree exceeds every row of this table. The seven
differences, in order, are

    16k+6, 8k^2+22k+6, 12k+2, 8k^2+18k,
    24k^2+30k, 8k^2+10k-8, 24k^2+22k-8.

Each is strictly positive on `k>=1`: on substituting `k=j+1` it has a
positive constant and nonnegative remaining coefficients. Cancellation can
only lower the left side's degree, so (5) is impossible there.

For `k<=-2`, the 00 sector uniquely has the largest top degree, namely 14,
with coefficient -1. The differences between its degree and the six other
degrees are

    8k^2+6k, -4k-4, 8k^2+2k-6, 24k^2+14k-6,
    8k^2-6k-14, 24k^2+6k-14.

Substituting `k=-j-2` again gives a positive constant and nonnegative other
coefficients. Meanwhile `16k+20<=-12`, so the target degree cannot equal 14.
This excludes that entire ray.

Only `k=-1,0` remain. Exact substitution gives

    k=-1: (m,n)=(-2,-1),   F=t^-8,        J=1;
    k= 0: (m,n)=(0,0),
       J-1 = -(t-1)(t+1)^3(t^2+1)(t^2-t+1)^2 Phi_10(t)/t^14 != 0.

This proves the claimed unique unit point, without a finite box search.

## 4. The isolated point has a short braid representative

The body at `(-2,-1)` is

    x0.y2.y2.x1.x1.y1.y1.y1.y1.y3.y3.x1.x1.y0.x1.

Using commutation of x1 with y3, the middle x1/y1 factors cancel. Next x0
commutes with y2 and y3, so x0 and y0 cancel. The result is

    y2.y2.y3.y3.x1.

Thus the same marked plat is represented by

    s.l1.l1.y2.y2.y3.y3.x1.u2.u2.

This is a braid-word identity. It is not, by itself, an isotopy to the
unknot or a nontriviality certificate. The construction lane can identify
this one fixed short object independently. There is no claim of a Jones
counterexample in this report.

## 5. What the reduction contributes

The two supplied near-miss templates cannot yield further isolated unit
points hidden at large twist parameters. The first has one explicit short
unit object; the second has none. The method uses the preferred second
moment **before** a two-ended positivity conjecture: it cuts the parameter
plane to a conic, after which ordinary exact sector-degree comparisons
decide all but two points. It does not establish a positivity theorem for
arbitrary width-two templates.

## 6. Independent referee closure (Claude030114)

Status: PROVED under the collaboration protocol. R2 rebuilt the sector
coefficients from rho2_matrices.json, checked literal halfword evaluations
against the quotient bracket, re-derived both moment conics and the
complete degree argument, and checked the local rational-knot certificate
including its crossing sign. R1 separately accepted the broader support
theorem. Reports: ~/jones-lanes/theory-restart/mont/referee/width2-window/.
The all-integer conclusion uses the proof, not the referee's finite
samples. No broader width-two detection claim is made.
