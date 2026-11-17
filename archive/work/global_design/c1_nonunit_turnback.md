# C1: an actual unknot anchor with a nonunit EKT turnback

Date: 2026-11-03. **REJECTED as a counterexample design. Its entire Jones-unit
locus is the actual unknot anchor `(m,n)=(0,0)`.** The explicit construction
and anchor are valid, but the torsion of the turnback link obstructs every
nonzero n. This was caught in the root's final homology check before a Jones
corner computation was requested. No Jones polynomial was computationally
evaluated in this pass.

Executable source: `work/global_design/c1_nonunit_turnback.py`.
Original PD codes and the anchor simplification record:
`work/global_design/c1_nonunit_turnback_anchor.json`.

## 1. A Jones-flat link family outside the old unknot-seed obstruction

Let

\[
S_n=\sigma_1^{-2n}\,R(25,-9),\qquad
T_n=\omega(S_n),\qquad U=-3,
\]

where the braid box is immediately above the fixed rational tangle and
`omega(T)=((T+IntegerTangle(2))*IntegerTangle(1))+IntegerTangle(2)` is the
literal EKT operation. The fractions are

\[
S_n=\frac{25}{-9+50n},\qquad
T_n=\frac{3+400n}{-2+150n}.
\tag{1}
\]

The numerator of `S_n` is the same actual two-bridge knot
`J=N(R(25,-9))` for every integer `n`: the inserted full twists are adjacent
to its numerator cap and remove as curls. In particular `det J=25`, so
`V_J` is nonunit. This is a **non-unknot seed**, unlike the LL1/LL2
unknot-seed families excluded in `work/band_obstructions.md`.

Set `L_n=H(T_n,-3)` using the existing Hopf builder. EKT's opposite-omega
identity compares this with the split union `N(S_n) disjoint-union U`.
Thus their normalized Jones polynomials differ at most by a monomial.
Here the first companion pattern has winding zero: the denominator of `T_n`
is even. Hence `lk(L_n)=0`, as for the split comparison link. The Jones
derivative at 1 determines the linking number and eliminates that monomial
ambiguity. Consequently

\[
V_{L_n}=\delta V_J
\tag{2}
\]

for compatible orientations, with `delta=-A^2-A^-2` and Jones variable
`t=A^-4`. Equivalently, the marked n-twist is Jones-cosmetic for these
two-component links. It is a single crossing disk: it is the image of the
specified top braid box under the fixed tangle operations and outside gluing.
No changing standard continued-fraction diagram is used to define the site.

The archived integral Fox presentation gives directly

\[
H_1(\Sigma_2L_n)=\mathbb Z\oplus
 \mathbb Z/|1+1800n|.
\tag{3}
\]

Indeed the numerator/denominator data of `T_n` are
`p=3+400n`, `q=-2+150n`, and the other tangle is `-3`; the finite order is
`|-3p-4q|`. In particular `L_0=H(-3/2,-3)` has torsion-free double-cover
homology. Only the fractions are simplified in this description; the executable
construction retains the literal framed omega diagram and its marked site.

Source for the EKT operation and split-link comparison: Eliahou--Kauffman--
Thistlethwaite, Sections 2--3, especially Theorem 3.2 and the construction in
Theorem 3.3, https://homepages.math.uic.edu/~kauffman/ekt.pdf .
The homology formula is the archived calculation in `work/band_obstructions.md`.

## 2. Exact seam band and second twist site

Write

\[
A_n=I_2\mathbin{|}\operatorname{rot}_{90}(T_n),\qquad
B=\operatorname{rot}_{90}(-3)\mathbin{|}I_2,\qquad
h=\sigma_2^{-1}\sigma_3^{-1}\sigma_1^{-1}\sigma_2^{-1}.
\]

The link `L_n` is the braid closure of `A_n h h B`. At the seam between the
two `h` blocks, replace the vertical strands in positions 2 and 3 by a horizontal
cap and cup, leaving positions 1 and 4 vertical. This is one exactly located
band fusion, with no band-position search. Twist that band by setting

\[
C_m=I_1\mathbin{|}\operatorname{rot}_{90}(\sigma_1^{2m})\mathbin{|}I_1,
\qquad
K(m,n)=\operatorname{cl}_{\mathrm{braid}}(A_n h C_m h B).
\tag{4}
\]

At `m=0`, the central two-strand piece is `ZeroTangle`. Rotation is essential:
composing that turnback with a vertical braid would merely add curls.

The actual boundary matching, in the library's order of bottom endpoints
followed by top endpoints, is

    [5, 3, 4, 1, 2, 0, 7, 6].

Its braid closure is one component. Both local parameter changes are full
twists and preserve their local endpoint pairings, so **every K(m,n) is a
knot**.

Orientation tracing gives

\[
w(K(m,n))=-2m+2n.
\tag{5}
\]

Both sites are antiparallel. The m-box uses a positive full twist in its
rotated local coordinates and has normalized eigenvalues `1,A^(8m)`.
The n-box uses a negative full twist and has eigenvalues `1,A^(-8n)`.
Thus set `X=A^(8m)`, `Y=A^(-8n)`; the candidate constant-product line is
`m=n`, not `m+n=0` in these literal parameter conventions.

Only endpoint/component/writhe bookkeeping was checked at `(0,0),(1,0),(0,1)`;
no Jones evaluation was performed at any parameter. These three checks give
writhes `0,-2,+2` and the same displayed boundary matching.

## 3. The anchor is an actual unknot

The literal `K(0,0)` has 24 crossings, one component, and writhe zero.
Spherogram's global simplifier, using isotopy moves, reduces it to zero
crossings with `unlinked_unknot_components=1`.
The separate list of components containing crossings is empty after this
reduction; it must not be mistaken for the empty link. The executable script
asserts the retained crossing-free component explicitly.

Regina's local simplifier reduced the same PD only to 17 crossings. This is
not an independent unknot certificate and is recorded only for transparency.
The original PD and both outputs are retained in the JSON record.

Thus the reduced Jones value at the anchor is 1 and its **absolute raw**
bracket is `delta`, since its displayed writhe is zero. No polynomial
computation was needed to establish this anchor.

## 4. Four actual corners and the proposed equation

Use the **absolute** bracket: `bracket(empty)=1`, `bracket(U)=delta`.
Do not substitute separately normalized corner Jones polynomials.
The code's `corner(epsilon,eta)` produces exactly these closures:

| Local state | m-site at the seam, in global vertical coordinates | n-site above R(25,-9) |
|---|---|---|
| 0 = through in that site's local coordinates | `ZeroTangle()` | `IdentityBraid(2)` |
| 1 = turnback in that site's local coordinates | `IdentityBraid(2)` | `ZeroTangle()` |

Let their raw brackets be `B00,B10,B01,B11`. Then

\[
B_{00}=\delta,\qquad B_{10}=\delta^2V_J,
\qquad B_{11}=\delta B_{10}.
\tag{6}
\]

The first equality is the actual unknot anchor. The second is (2) at `n=0`,
whose inherited displayed writhe is zero. The third is exactly the framed
Jones-flatness statement for `L_n`: the negative full twist has raw eigenvalues
`A^(6n),A^(-2n)`, while `w(L_n)=2n`, so its surviving channel is the turnback
channel. These identities do **not** determine `B01`, the fused link after
turning back the n-site.

Define the prospective defect Laurent polynomial

\[
E(A)=\delta B_{01}-B_{11}.
\tag{7}
\]

The C1 four-corner expansion, now with `X=A^(8m),Y=A^(-8n)` and `w0=0`, gives

\[
\begin{aligned}
a&=V_J,\qquad b=E/\delta^3,\qquad c=0,\qquad d=1-a-b,\\
V_{K(m,n)}&=a+bX+(1-a-b)XY.
\end{aligned}
\tag{8}
\]

In particular

\[
V_{K(m,m)}=1+\frac{E(A)}{\delta^3}\bigl(A^{8m}-1\bigr).
\tag{9}
\]

Had `E` vanished, the whole diagonal would have had Jones polynomial one.
The homology argument below instead proves **E is nonzero without computing
it**. There is no outstanding corner-certification request for this rejected
family. The corner construction is retained to make the exact design and
its failed condition reproducible.

## 5. Decisive rejection: turnback torsion divides every fusion determinant

Let a two-component link L be obtained from a knot K by a single band surgery.
The covers of the two links are fillings of one torus-boundary manifold M.
Since `Sigma_2(K)` has finite homology, `b1(M)=1`. Write

    H1(M)=Z direct-sum T.

If `b1(Sigma_2(L))=1`, its filling slope has free coordinate zero, so

    Tor H1(Sigma_2(L)) = T / <t_lambda>.

For the knot filling slope alpha, the free coordinate `ell(alpha)` is nonzero,
and the elementary filling-order formula gives

    det K = |T| * |ell(alpha)|.

Consequently

\[
|\operatorname{Tor}H_1(\Sigma_2L)|\ \mid\ \det K.
\tag{10}
\]

This applies to every `K(m,n)`: the seam tangle in (4) is the same band with
different integer framing. Its turnback is always `L_n`. By (3),

\[
|1+1800n|\ \mid\ \det K(m,n).
\tag{11}
\]

For every nonzero integer n the divisor exceeds 1. Therefore no such parameter
can have Jones polynomial one, irrespective of m.

At n=0, substitute `Y=1` in (8). The unknown mixed coefficient cancels, giving

\[
V_{K(m,0)}=V_J+(1-V_J)A^{8m}.
\tag{12}
\]

Since `det J=25`, `V_J != 1`. The Laurent-polynomial ring is a domain, so
`V_K(m,0)=1` holds exactly at m=0. Together with the actual unknot anchor,
this proves that the whole unit locus is exactly `(0,0)`.

It also proves `E != 0`: otherwise (9) would give a Jones-unit knot at `(1,1)`,
contradicting (11). Thus the second desired Jones-only turnback identity
cannot hold for this marked template.

**Design lesson with precise scope:** a torsion-free turnback at the anchor
is insufficient. In a proposed constant-unit diagonal of band fusions, every
turnback encountered along that diagonal must have torsion-free branched-cover
homology. The nonunit seed avoids the old anchor obstruction, but its EKT
Jones-flat twist family immediately reintroduces torsion away from the anchor.

## 6. General rational-seed boundary-twist obstruction

The preceding rejection is not special to the numbers25 and-9. Take any
primitive rational seed `S_n=p/(q+2pn)`, with p an odd nonzero integer, and
retain the same fixed omega operation and second input -3. The numerator
closure stays the same knot, while the integral boundary calculation gives

    T_n=(3p+8q+16pn)/(p+3q+6pn),
    H1(Sigma_2 H(T_n,-3))=Z plus Z/|13p+36q+72pn|.

The integer inside the absolute value is odd, so it never vanishes. Every
Jones-unit band fusion must therefore satisfy

    |13p+36q+72pn|=1.

There is at most ONE integer n satisfying this condition. Two distinct
solutions would differ by `2/(72p)`, which is not an integer. Thus no
infinite Jones-unit diagonal varying n can arise from this particular
cap-twist deformation, for ANY rational seed. At a parameter admitting an
actual unknot band-fusion anchor, if the fixed numerator knot has nonunit
Jones polynomial, the one-band twist recurrence above leaves only the
anchor framing m as well.

This is scoped to the specified boundary-twist deformation and fixed
outside EKT geometry. It does not exclude internal deformations of a
nonrational seed with unchanged boundary homology, or a different outside
construction. It identifies why replacing the old unknot seed by a
nonunit seed fixes the obstruction at one parameter but cannot fix the
entire proposed unit line.
