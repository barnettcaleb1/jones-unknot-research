# Classification of Jones-one satellites in the entire odd two-top-twist Ren family

This is an exact theorem about the specified template, with no bound on its integer parameters or on the companion knot. It does not settle the generic Jones unknot problem.

Let \(P_{p,q}\) be the partial annular closure of

\[
\sigma_2^{-1}\sigma_1^3\sigma_2^{-1}
\sigma_4\sigma_5^{-3}\sigma_4
\]

with the two top twist sites \(\sigma_1^p,\sigma_5^q\), as encoded in `tangle_ren_twists.py`. The cap joins endpoints 3 and 4 at both ends, and the remaining four strands close annularly. Assume \(p,q\) odd, so the pattern is a knot. Let \(P_{p,q,n}\) be its meridional twist by \(n\in\mathbb Z\), with eigenvalue \(A^{8n}\) on \(S_2=z^2-1\).

**Theorem.** For every knot \(C\), with its zero framing,

\[
V_{P_{p,q,n}(C)}=1
\quad\Longleftrightarrow\quad
(p,q,n)=(-1,1,0)\ \text{and}\ H_3(C)=1,
\]

where \(H_3\) is the reduced color-three Jones polynomial, normalized to one on the unknot.

The exceptional pattern closes to an actual unknot when the companion is the unknot, but is geometrically essential in the solid torus. Thus the theorem identifies the remaining colored-Jones condition rather than proving that no nontrivial companion satisfies it.

## Conventions and satellite equation

Set \(S=p+q\), \(D=p-q\), \(y=A^4\), \(\delta=-A^2-A^{-2}\), and \(\Delta_2=y+1+y^{-1}\). The patterns have winding zero and diagram framing \(S\). The former is preserved when the odd twist parameters vary, since adding two crossings at a site does not change the oriented strand connectivity. The two top crossings have the orientations for which their writhe contributions are \(p,q\); the base braid contributes zero. Meridional twisting changes the framing by the square of the winding number times \(n\), hence by zero here.

The exact annular bracket has the form

\[
\langle P_{p,q}\rangle=a_{p,q}z^2+b_{p,q}
=a_{p,q}S_2+(a_{p,q}+b_{p,q}).
\]

Write

\[
F_a=\delta^2 A^{-S}a_{p,q},\qquad
F_b=\delta^2 A^{-S}b_{p,q}.
\]

The satellite Jones-one equation is exactly

\[
G_C=A^{-2}\left[(A^{8n}\Delta_2H_3(C)+1)F_a+F_b-\delta^3A^{2S}\right]=0.
\]

For odd \(p,q\), this lies in \(\mathbb Z[y^{\pm1}]\). The factor \(A^{-2}\) is just the common grading shift. Denote the same expression with \(H_3=1\) by \(G_U\). The state-sum coefficients and its 48 affine monomials are recorded by `ren_jones_locus.py/.json`.

## Low-order companion constraints

For every zero-framed knot, \(H_3\in\mathbb Z[y^{\pm1}]\), \(H_3(1)=1\), and its first derivative at one is zero. These follow, for example, from [Habiro, §3.3 and Theorem 3.1](https://msp.org/gtm/2002/04/gtm-2002-04-005p.pdf): the reduced invariant is integral, and every nonconstant cyclotomic term has at least two factors vanishing at one. No formula identifying the second derivative with another knot invariant is needed.

Put \(y=e^h\) and let

\[
h_2=\left.\frac{d^2}{dh^2}H_3(C;e^h)\right|_{h=0}\in\mathbb Z.
\]

Integrality follows directly by writing \(H_3=\sum c_jy^j\), so \(h_2=\sum j^2c_j\). Exact differentiation of the state sum gives

\[
F_a(1)=0,\qquad \left.\frac{dF_a}{dh}\right|_0=-2S.
\]

Thus the companion correction begins at order three, and

\[
G_C''(0)=G_U''(0),\qquad
G_C'''(0)=G_U'''(0)-18S h_2.
\]

In particular, second-order vanishing is independent of the companion. The exact second derivative is

\[
G_U''(0)=6\bigl[p^2+q^2-4p+4q-10-4n(p+q)\bigr].
\]

## Determinant and second derivative reduce the infinite parameter space

Because the pattern has winding zero, its satellite determinant is independent of the companion. The exact determinant formula is

\[
\det(P_{p,q,n}(C))=
\left|36+30p-30q-25pq-50(p+q)n\right|.
\]

Jones polynomial one requires this to equal one. Let the expression inside the absolute value be \(F\). The condition \(G_U''(0)=0\) becomes

\[
S^2+D^2-8D-20-8nS=0.
\]

Using this relation to eliminate \(nS\) in \(F\) yields

\[
F=161+80D-\tfrac{25}{2}S^2.
\]

Write \(S=2s,D=2d\). The case \(F=-1\) would give
\(25s^2-80d=81\), impossible modulo five. The case \(F=1\) gives

\[
5s^2-16d=16.
\]

Hence \(s=4k\) and \(d=5k^2-1\). Since \(p,q\) are odd, \(k\) is even; write \(k=2j\). If \(S\ne0\), the second-derivative equation now gives

\[
n=\frac{j(50j^2-7)}4.
\]

The factor \(50j^2-7\) is odd, so integrality of \(n\) forces \(j=4r\). Therefore every remaining solution with \(S\ne0\) has the form

\[
\boxed{
p=320r^2+32r-1,\quad
q=-320r^2+32r+1,\quad
n=800r^3-7r,\quad r\in\mathbb Z\setminus\{0\}.
}
\]

If \(S=0\), the second derivative gives \(D=10\) or \(D=-2\). The first has determinant 961. Thus the only determinant-one possibility is \(p=-1,q=1\), at this point with arbitrary \(n\).

## Third-order integrality eliminates every nonzero parameter

Independent differentiation of the affine monomial expression, followed by substitution of the displayed parameterization, gives

\[
G_U'''(0)=2496r+2370048r^3-169574400r^5+2949120000r^7.
\]

Since \(S=64r\), the necessary equation \(G_C'''(0)=0\) would force

\[
h_2=\frac{G_U'''(0)}{18S}
=\frac{13+12344r^2-883200r^4+15360000r^6}{6}.
\]

The numerator is odd for every integer \(r\), whereas \(h_2\) must be an integer. This is impossible. All \(S\ne0\) cases are excluded.

At \(p=-1,q=1\), direct differentiation gives \(G_U'''(0)=-576n\). Because \(S=0\), the companion correction at this order vanishes. Therefore \(n=0\).

Finally the remaining pattern has \(V_{P_{-1,1}(U)}=1\) and nonzero \(a_{-1,1}\). The exact satellite equation reduces to a nonzero Laurent factor times \(H_3(C)-1\), so it vanishes if and only if \(H_3(C)=1\). This proves both implications of the theorem.

## Independent computational audit

`homology_full_family.py/.json` independently differentiates the 48 affine monomials using integer arithmetic, checks the first moment of \(F_a\), the vanishing second moment on the parameterized family, its determinant value, the complete third-moment polynomial, the odd-numerator obstruction, and the \(S=0\) third moment. It performs polynomial identities, not finite parameter sampling. The only external theorem needed for the companion step is the integral, zero-framed colored-Jones normalization and its vanishing first derivative, cited above.
