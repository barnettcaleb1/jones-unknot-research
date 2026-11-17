# C4: a fully marked two-site modification of the smallest EKT orbit

Status: **DESIGN ONLY. The Jones polynomial, determinant feasibility, unit locus,
and nontriviality of the candidate family have not been tested.** No counterexample
or successful sieve passage is claimed. The only computation performed here was
endpoint tracing and the component/crossing/writhe check of the base diagram.

This specimen uses the existing `work/ekt_model/check_links.py` Hopf builder. It
is not a new choice of band faces from a picture, and it is not the archived
three-component `LLL(1)` two-band family.

## 1. Exact diagram and sites

Use the literal framed tangles

\[
T=\operatorname{IntegerTangle}(3),\qquad
U=\operatorname{IntegerTangle}(-3),
\]

the first nonzero EKT `LL2` orbit, and set

\[
A_0=I_2\mathbin{|}\operatorname{rot}_{90}(T),\qquad
B_0=\operatorname{rot}_{90}(U)\mathbin{|}I_2,
\qquad h=\sigma_2^{-1}\sigma_3^{-1}\sigma_1^{-1}\sigma_2^{-1}.
\]

All multiplication below is top to bottom, as in Spherogram's tangle product.
The archived Hopf diagram is the braid closure of `A0 * h * h * B0`.
Define

\[
K(m,n)=\operatorname{cl}_{\mathrm{braid}}
 \bigl(A_0\,h\,\sigma_2\,\sigma_2^{2m}\,h\,
       \sigma_2^{2n}\,B_0\bigr),\qquad(m,n)\in\mathbb Z^2.
\tag{1}
\]

The first variable box lies immediately after a **fixed positive** `sigma_2`
between the two copies of `h`. The second variable box lies immediately after
the second `h` and before `B0`. In each box, positions 2 and 3 are the marked
strands; positions 1 and 4 pass straight through. Thus both sites and the fixed
fusion crossing are specified before any simplification or diagram rendering.

Executable builder (run from the repository root):

```python
from pathlib import Path
import sys

sys.path.insert(0, str(Path('work/braid_classification/packages').resolve()))
from spherogram.links.tangles import (
    IdentityBraid, BraidTangle, IntegerTangle, ZeroTangle,
)

def sigma2_power(k):
    assert isinstance(k, int)
    return BraidTangle([2 if k > 0 else -2] * abs(k), 4)

def fixed_pieces():
    T = IntegerTangle(3)
    U = IntegerTangle(-3)
    A0 = IdentityBraid(2) | T.rotate(1)
    B0 = U.rotate(1) | IdentityBraid(2)
    h = BraidTangle([-2, -3, -1, -2], 4)
    return A0, h, B0

def candidate(m, n):
    A0, h, B0 = fixed_pieces()
    return (A0 * h * sigma2_power(1) * sigma2_power(2*m)
            * h * sigma2_power(2*n) * B0).braid_closure()

def corner(epsilon, eta):
    assert epsilon in (0, 1) and eta in (0, 1)
    A0, h, B0 = fixed_pieces()
    G = [IdentityBraid(4),
         IdentityBraid(1) | ZeroTangle() | IdentityBraid(1)]
    return (A0 * h * sigma2_power(1) * G[epsilon]
            * h * G[eta] * B0).braid_closure()

# Exact PD inputs for the FOUR corner evaluations:
# corners = {(e, f): corner(e, f).PD_code()
#            for e in (0, 1) for f in (0, 1)}
# No parameter scan is needed.
```

The tangle `G[1]` is explicitly the Temperley--Lieb turnback `e_2`: an upper
cap joining positions 2--3, a lower cup joining positions 2--3, and vertical
strands in positions 1 and 4. The fixed `sigma_2` remains in **all four** corners.

## 2. Endpoint and orientation check

The local library numbers bottom endpoints first, then top endpoints, both
left to right. Tracing actual `Crossing` opposite half-edges and `Strand`
connections, rather than assuming the rotated rational tangles are braids,
gave the following complete boundary involutions (zero-based):

| Piece | Boundary mates |
|---|---|
| `IntegerTangle(3).rotate(1)` | `[3, 2, 1, 0]` |
| `IntegerTangle(-3).rotate(1)` | `[3, 2, 1, 0]` |
| `h` | `[6, 7, 4, 5, 2, 3, 0, 1]` |
| `A0*h*h*B0` | `[5, 4, 7, 6, 1, 0, 3, 2]` |
| `A0*h*sigma2*h*B0` | `[5, 6, 7, 4, 3, 0, 1, 2]` |

Thus the baseline closure has permutation `(12)(34)`, whereas the fixed odd
crossing changes it to a four-cycle (top-to-bottom convention `(1 4 3 2)`).
Both variable powers are even, hence have identity endpoint permutation.
Consequently **every `K(m,n)` is a knot**.

Rotation of the literal integer-tangle diagrams turns their horizontal crossing
chains into vertical crossing chains: `T.rotate(1)` is the positive three-crossing
two-braid and `U.rotate(1)` the negative one in the library's convention. They
admit the common downward braid orientation, which is preserved throughout
(1). In particular the two variable sites are **coherently oriented**, with
algebraic winding number 2. They are not the antiparallel, winding-zero sites
of a Kanenobu-type constant-sum template.

Their initial writhes cancel, the two copies of `h` contribute `-8`, and the
fixed crossing contributes `+1`. Therefore

\[
w(K(m,n))=-7+2m+2n.
\tag{2}
\]

Direct construction of `K(0,0)` confirmed one component, 15 crossings in this
diagram, and writhe `-7`. These checks do not evaluate any knot invariant.

## 3. The exact four-corner certificate

Use the raw reduced Kauffman bracket with

\[
\langle U\rangle=1,\quad
\delta=-A^2-A^{-2},\quad
\sigma_i=A I+A^{-1}e_i,\quad
e_i^2=\delta e_i,
\]

and Jones normalization `V=(-A^3)^{-w}<D>`. If an evaluation implementation
uses the mirrored `A` convention, invert `A` consistently in the entire table
and the normalization; do not normalize corners independently.
If Claude's evaluator instead uses the absolute convention `bracket(empty)=1`
and `bracket(U)=delta`, divide each of the four nonempty closure brackets by
`delta` to obtain the `F_epsilon,eta` used here. That exact common division is
performed before the determinant specialization.

Let `F_epsilon,eta(A)` be the **raw reduced bracket** of `corner(epsilon,eta)`
from the executable builder. The writhe and component counts of these four
closures need not agree, so their separately normalized Jones polynomials are
not the four entries to substitute below.

Put `X=A^(8m)` and `Y=A^(8n)`. The exact identity

\[
\sigma_2^{2m}
 =A^{-6m}\left(XI+\frac{1-X}{\delta}e_2\right)
\]

gives the bilinear corner expression

\[
\begin{aligned}
P(A;X,Y)={}&XYF_{00}
 +\frac{(1-X)Y}{\delta}F_{10}
 +\frac{X(1-Y)}{\delta}F_{01}
 +\frac{(1-X)(1-Y)}{\delta^2}F_{11},\\
V_{K(m,n)}(A^{-4})={}&(-A^3)^7 A^{-12(m+n)}
 P(A;A^{8m},A^{8n}).
\end{aligned}
\tag{3}
\]

In particular, the eigenvalue exponents at each normalized coherent-twist site
are **-12 and -4**, not 0 and 8. The factor `A^(-12(m+n))` must be retained.
The exact unit equation to solve is

\[
P(A;A^{8m},A^{8n})=(-A^3)^{-7}A^{12(m+n)}.
\tag{4}
\]

Multiplying by `delta^2` makes (4) a finite Laurent-exponent identity with a
fixed denominator removed. The archived affine-exponent partition method can
then solve its entire integer parameter locus from this single corner table,
without enumerating `(m,n)`.

## 4. First kill check: determinant feasibility

Before solving the full Laurent identity, specialize the same four-corner
identity at a primitive eighth root `zeta` with `zeta^4=-1`. Work with the
removable limits in (3), or directly use

\[
\left.\sigma_2^{2m}\right|_{A=\zeta}
 =\zeta^{2m}\bigl(I+2m\zeta^{-2}e_2\bigr),
\tag{5}
\]

which follows because `e_2^2=0` at `delta=0`.
Thus, up to the known unit phase, the determinant of `K(m,n)` is the absolute
value of a polynomial of degree at most one in each variable, obtained from
`F00, F10, F01, F11` and the fixed normalizing phase. Extract this integer
bilinear polynomial and test whether its absolute value can be 1 for integers
`m,n`. If there are no solutions, reject the template immediately. **Neither
its coefficients nor this feasibility question have been computed here.**

Do not substitute `delta=0` into un-cancelled fractions in (3).

## 5. Why two sites, and the limits of the proposal

The archived base `H(3,-3)` has
`H1(Sigma_2)=Z direct-sum Z/13`. When `n=0`, the whole modification is contained
in the first marked ball: replace the original two parallel strands between
the copies of `h` by `sigma_2^(2m+1)`. This is a single rational-tangle
replacement, so the archived one-site torsion obstruction rules out
`det K(m,0)=1` for every integer `m`.

For `n != 0`, (1) changes the second, separately marked rational-tangle ball as
well. Our fixed one-site obstruction no longer applies directly. This does
**not** prove essential independence of the sites: separation by `h` does not
exclude a larger ball containing both modifications whose net effect is a
single rational replacement. This is the sole reason to test this specimen:
it is the smallest literal EKT orbit with a deterministic knot-making crossing
and one additional explicitly located modification. The EKT bracket
cancellation is a source of structure, not evidence that (4) has a solution.

No claim is made that the family avoids all existing Jones-detection classes,
that determinant-one parameters exist, that any member has trivial Jones
polynomial, or that any Jones-unit member would be nontrivial. Those are the
successive exact certification tasks, beginning with the four corners above.
