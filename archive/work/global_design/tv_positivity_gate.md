# Turaev–Viro positivity gate: exact normalization and its obstruction

Date: 2026-11-03. Bounded theory/literature pass; no scans or new computations. Status: the standard constructions do not supply an ordinary-Jones-only local positivity mechanism. This is a scoped obstruction, not a theorem excluding every possible positive model.

## 1. The unitary boundary norm includes all colors

Fix r >= 3 and set

\[
A=e^{\pi i/(2r)},\qquad q_{\rm TV}=A^2=e^{\pi i/r},\qquad
t=A^4=e^{2\pi i/r},\qquad d=2\cos(\pi/r).
\]

Use unreduced colored Jones polynomials J_{K,n}, with J_{U,n}=[n]=sin(n pi/r)/sin(pi/r), and normalized ordinary Jones V_K=J_{K,2}/[2]. Theorem 1.1(1) of [Detcherry–Kalfagianni–Yang](https://arxiv.org/html/1701.07818v3#S1.SS1) gives

\[
TV_r(EK,q_{\rm TV})=\eta_r^2\sum_{n=1}^{r-1}|J_{K,n}(t)|^2,
\qquad \eta_r=\sqrt{2/r}\sin(\pi/r).
\tag{1}
\]

This is the standard unitary SU(2) point. Their odd-r Theorem 1.1(2), with A=e^{pi i/r}, instead has q_TV=e^{2pi i/r}, t=e^{4pi i/r}, a different range of colors and normalization; it must not be substituted into a unitary argument without further justification.

Our consequences: TV_r(EU)=1 by the sine-square sum. The fundamental term in (1) is eta_r^2 d^2 |V_K(t)|^2. Therefore V_K=1 fixes only one coordinate of this positive boundary norm. It does not fix the remaining colored amplitudes, and gives no equality TV_r(EK)=TV_r(EU). Moreover, (1) is a sum of squares of completed amplitudes, not a sum of nonnegative independent tetrahedron weights before those amplitudes are evaluated.

## 2. An ordinary-only decorated observable exists

[Balsam's extended TV/RT equivalence](https://arxiv.org/html/1012.0560v1) identifies TV_C with RT_{Z(C)}, including boundary state spaces. For modular unitary C, Z(C) is C tensor C^rev. Consequently a knot labeled by the paired fundamental object X tensor X has chiral and conjugate factors. Dividing by the equally decorated unknot gives

\[
\frac{TV_C(S^3,K_{X\boxtimes X})}
     {TV_C(S^3,U_{X\boxtimes X})}
=|V_K(t)|^2.
\tag{2}
\]

Here X is self-dual. This is a center-labeled line defect; it is not the same observable as fixing a fundamental triangulation-edge spin in the original state sum.

There is a concrete obstruction to interpreting (2) by independent positive local choices. For r >= 4, write X tensor X=1 direct-sum Y. Then

\[
(X\boxtimes X)^{\otimes2}
=(1\boxtimes1)\oplus(1\boxtimes Y)
 \oplus(Y\boxtimes1)\oplus(Y\boxtimes Y).
\tag{3}
\]

Thus diagonal labels are not fusion closed. The off-diagonal bra/ket channels are part of the genuine doubled theory. Keeping only matching channels in order to replace amplitudes by local absolute squares changes the theory. Globally |sum amplitudes|^2 contains cross terms; it is not sum |amplitudes|^2.

In standard unitary recoupling gauge this is already visible in the four-fundamental matrix

\[
F=\frac1d\begin{pmatrix}1&\sqrt{d^2-1}\\
\sqrt{d^2-1}&-1\end{pmatrix}.
\]

A nonnegative unitary matrix must be a permutation matrix, by orthogonality of its rows. Since this F genuinely mixes channels, no basis-phase gauge makes every entry nonnegative. This statement concerns standard local recoupling, not an arbitrary alternative positive representation.

## 3. Exact chain-mail transform: the ordinary row has both signs

[Barrett–García-Islas–Faria Martins](https://arxiv.org/html/math/0411281v2), Theorem 4 and Section 4.4, identify fixed-spin TV observables with squared bracket observables through a Fourier transform. Use their unvertexed-circle normalization, including the subdivision factors in Definition 4. Put

\[
p_j(K)=Z(S^3,K(j))/Z(S^3),\qquad
j=0,\tfrac12,\ldots,\tfrac{r-2}{2}.
\]

Their matrix and signed dimensions are

\[
H_{jk}=(-1)^{2j+2k}
\frac{\sin((2j+1)(2k+1)\pi/r)}{\sin(\pi/r)},\qquad
d_j=(-1)^{2j}\frac{\sin((2j+1)\pi/r)}{\sin(\pi/r)}.
\]

For a circle there are no vertex theta denominators. Hence their theorem says

\[
\sum_j p_j(K)\,\frac{H_{jk}}{d_j}=|\langle K(k)\rangle|^2.
\tag{4}
\]

They also give H^2=N I, N=sum_j d_j^2, so the transform is invertible.

**Deduction (exact fundamental row).** Substituting k=1/2 in (4), dividing by the squared fundamental unknot value d^2, and using sin(2x)/sin(x)=2cos(x), gives

\[
\boxed{\quad
|V_K(t)|^2=\frac1{d^2}
\sum_{j=0,1/2,\ldots,(r-2)/2}
\left[-2\cos\!\left(\frac{(2j+1)\pi}{r}\right)\right]p_j(K).
\quad}
\tag{5}
\]

The inverse Jones-variable convention t=A^{-4} gives the same modulus. Bracket framing phases disappear in (5).

The coefficient is -d at j=0 and +d at j=(r-2)/2. These are genuinely opposite signs at every r >= 3. They are not an unspecified convention-dependent global sign.

**Scoped no-go.** On the full vector space of fixed-spin coordinates, no nonnegative coefficient row can agree with this fundamental functional: evaluating on coordinate basis vectors already fixes its coefficients. Invertibility places it inside the exact Fourier dictionary. No positivity of the p_j themselves is asserted or needed for this conclusion.

**Essential scope caveat.** This does not establish that actual knot vectors (p_j(K)) span that coordinate space. A different positive formula valid only on actual knot vectors could use further identities. We have neither proved such identities nor excluded them. The no-go is for replacing the standard transform by a positive row on its whole coordinate space, not for every conceivable Jones positivity argument.

## 4. Even the normalized ordinary observable is below the unknot at a unitary level

The explicit figure-eight polynomial is

\[
V_{4_1}(t)=t^2-t+1-t^{-1}+t^{-2}=t^{-2}\Phi_{10}(t).
\]

At the genuine unitary level r=10, t=e^{2pi i/10}, its value is zero. Thus the normalized decorated invariant (2) is 0 for 4_1 and 1 for U. In particular,

\[
|V_{4_1}(t)|^2-1=-1.
\]

So a level-by-level proposal expressing |V_K(t)|^2-1 as a sum of nonnegative local defects is false. This does not rule out a different defect or an integrated identity.

## 5. Coefficient energy does not follow by averaging these unitary levels

For V=sum_j a_j t^j and any integer m greater than its exponent span, discrete Parseval gives

\[
E(K)=\sum_j a_j^2=\frac1m\sum_{\ell=0}^{m-1}
|V_K(e^{2\pi i\ell/m})|^2.
\tag{6}
\]

This formula is exact and positive, but not a new geometric state sum. The standard unitary SU(2) points t=e^{plus-or-minus 2pi i/r} do not supply the full-circle grids in (6). The other Galois specializations are not generally unitary. For example, at r=5 the conjugate specialization t=e^{4pi i/5} has fundamental quantum dimension 2cos(2pi/5)<1. This cannot be the positive dimension of that noninvertible fundamental in a unitary fusion category: X tensor X* contains 1, forcing dim(X)>=1.

Thus applying Parseval does not transfer the available unitary boundary positivity into a nonnegative geometric decomposition of E-1. It leaves the coefficient energy identity and its unknot-detection question unchanged.

## Verdict and explicit revival condition

The standard theories give either an all-color positive norm (1), or an ordinary-only observable (2)/(5) whose local/transform presentation retains signed interference and mandatory off-diagonal fusion channels. The formulas do not supply a zero-defect disk criterion.

A viable revival must add a geometric identity special to classical knot-realizable states, producing a nonnegative decomposition without deleting the off-diagonal channels, together with a proof that its zero terms force a spanning disk in S^3. Alternatively it must construct a genuinely different positive model of E-1 with that zero criterion. Merely squaring the ordinary amplitude, fixing an edge spin, or replacing recoupling matrices by entrywise absolute squares does not accomplish this.
