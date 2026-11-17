# Exact obstruction for all twisted satellites of Ren's original pattern

31 October 2026. This is a proved exclusion of an infinite construction family, not a resolution of the Jones unknot problem.

Let \(P\) be the annular knot in [Ren, arXiv:2609.11084v2](https://arxiv.org/html/2609.11084v2), with the framing used in the published planar diagram. Let \(P_n\) be its meridional twist by \(n\in\mathbb Z\), with the convention that the annular color-two basis element acquires the factor \(A^{8n}\). Let \(C\) be any zero-framed companion knot.

**Proposition.** For every knot \(C\) and integer \(n\),

\[
\det(P_n(C))=|100n-11|\ne1.
\]

Consequently no satellite in this entire family has Jones polynomial one. Reversing the convention for positive twists replaces \(n\) by \(-n\) and gives the same exclusion.

## Proof

Write \(\delta=-A^2-A^{-2}\), \(S_2=z^2-1\), and \(\Delta_2=S_2(\delta)=A^4+1+A^{-4}\). The exact annular state sum computed from the published PD gives

\[
\langle P\rangle=a(A)z^2+b(A)=a(A)S_2+(a(A)+b(A)),
\]

where

\[
\begin{aligned}
a(A)={}&-A^{12}+2A^8-5A^4+9-11A^{-4}+11A^{-8}\\
&-7A^{-12}+3A^{-16}-A^{-20}.
\end{aligned}
\]

The pattern has winding number zero, checked directly as its linking number with the axis. Its diagram framing is two. Under meridional twisting the framing of an oriented pattern changes by \(n\,w(P)^2\), so in this case it remains two. The eigenvalues of the meridional twist on \(1,S_2\) are \(1,A^8\). Therefore

\[
V_{P_n(U)}(A)=V_{P(U)}(A)
 +(A^{8n}-1)\frac{a(A)\Delta_2}{A^6\delta}.
\]

Here \(V\) is normalized by \(V_U=1\) and its usual Jones variable is \(t=A^{-4}\). Exact independent ordinary-Jones computation gives

\[
V_{P(U)}=A^4-1+2A^{-4}-2A^{-8}+2A^{-12}-2A^{-16}+A^{-20}.
\]

Set \(x=A^4\). Then \(A^6\delta=-x(x+1)\), \(\Delta_2=x+1+x^{-1}\), and

\[
V_{P(U)}\big|_{x=-1}=-11,\qquad
a\big|_{x=-1}=50,\qquad \Delta_2\big|_{x=-1}=-1.
\]

It is essential to remove the apparent pole before evaluating. For every integer \(n\), including negative \(n\),

\[
\left.\frac{x^{2n}-1}{x+1}\right|_{x=-1}=-2n.
\]

Thus the twist correction at \(x=-1\) is \(100n\), and

\[
V_{P_n(U)}(-1)=100n-11.
\]

The Alexander satellite formula gives

\[
\Delta_{P_n(C)}(t)=\Delta_{P_n(U)}(t)\Delta_C(t^{w(P_n)}).
\]

Since \(w(P_n)=0\) and normalized \(\Delta_C(1)=1\), the Alexander polynomial, hence determinant, is independent of \(C\). Finally \(100n-11=\pm1\) has no integral solution. This proves the proposition.

For the satellite formula see [Livingston–Melvin, *Abelian invariants of satellite knots*](https://pmelvin.blogs.brynmawr.edu/files/2021/09/1985LivingstonMelvin.pdf). The exact checks, including the winding number and polynomial division of the twist correction for \(n=-3,\ldots,3\), are reproducible in `homology_ren_satellite.py`, with results in `homology_ren_satellite.json`.

## Independent obstruction using Laurent integrality

For an arbitrary companion \(C\), let \(J_2(C)=\langle S_2(C)\rangle\) denote the zero-framed, unreduced color-three Jones polynomial; in particular \(J_2(U)=\Delta_2\). The satellite formula at the skein level is

\[
V_{P_n(C)}=\frac{A^{8n}aJ_2(C)+(a+b)}{A^6\delta}.
\]

Jones polynomial one would require

\[
a\mid A^6\delta-(a+b)
\quad\text{in }\mathbb Z[A^{\pm1}],
\]

independently of \(n\), because \(A^{8n}\) is a Laurent unit. Exact division disproves this condition even over \(\mathbb Q[A^{\pm1}]\). In \(x=A^4\), shifting the dividend and divisor separately so their smallest exponents are zero gives the nonzero ordinary polynomial remainder

\[
-3x^7+4x^6-2x^5+3x^3-3x^2+2x-1.
\]

This supplies a separate algebraic proof of the exclusion for all companions and all twists.

# What composition can and cannot do

A solid-torus embedding around a framed pattern \(Q\) induces a **linear skein map**. It sends \(z^r\) to the actual framed \(r\)-parallel cable of \(Q\). It need not preserve the annular stacking product, and it does not act by substituting \(\langle Q\rangle\) into an ordinary polynomial.

In particular,

\[
\langle P\circ Q\rangle=a\langle Q^{(2)}\rangle+b.
\]

For Ren's pattern the two-cable has annular degree eight, although the original has degree two. Thus \(P\circ P\) and \(P\circ\bar P\) have degree eight, not zero. A separate exact module computation in the braid-agent work verifies the degree-eight coefficient. Ordinary annular multiplication with the mirror also cannot cancel its highest degree: its coefficient is \(a(A)a(A^{-1})\ne0\).

The failure here is concrete: cabling remembers information that the uncolored annular bracket has lost.

# Exact conversion criterion for an unknot-closing pattern

Suppose a winding-zero pattern \(Q\) has annular bracket

\[
\langle Q\rangle=aS_2+d,\qquad a\ne0,
\]

and its closure \(Q(U)\) is the unknot. Let \(f=(-A^3)^{\operatorname{fr}(Q)}\) be its framing factor. Then \(a\Delta_2+d=f\delta\), and for every zero-framed companion,

\[
V_{Q(C)}-1=\frac{a}{f\delta}\bigl(J_2(C)-\Delta_2\bigr).
\]

Since Laurent polynomials form an integral domain,

\[
V_{Q(C)}=1\quad\Longleftrightarrow\quad J_2(C)=J_2(U).
\]

The tangle agent's modified Ren pattern with top twists \((-1,1)\) is such a degree-two, unknot-closing pattern. It therefore gives a geometric converter for a companion with trivial color-three Jones polynomial. It does not itself supply such a nontrivial companion.

Finally, a genuinely essential winding-zero pattern with **zero-framed annular bracket exactly \(\delta\)** would suffice: every companion satellite would have Jones polynomial one, and a nontrivial companion would give an essential companion torus and hence a nontrivial knot. Merely having annular degree zero is weaker; its constant could be \(\delta\) times a nontrivial ordinary Jones polynomial. The missing constructive condition is the exact constant \(\delta\), together with geometric essentiality.
