# Jones power moments: what the whole orbit determines

2026-11-03. Theory pass, no computation. The algebraic lemmas below are elementary deductions, with no novelty claim. They distinguish one closure from a full braid-power family.

## 1. Exact normalization and recurrence

Work over F=Q(A), with delta=-A^2-A^{-2}. Let rho:B_n -> TL_n(delta) be the bracket representation, using rho(sigma_i)=A 1+A^{-1} e_i, and let tau be the normalized Markov trace, tau(1)=1. For beta of writhe w define

\[
B=(-A^3)^{-w}\rho(\beta),\qquad m_k=\tau(B^k).
\]

For the oriented trace closure, including link closures,

\[
V_{\widehat{\beta^k}}(A^{-4})=\delta^{n-1}m_k.
\tag{1}
\]

This absorbs the writhe correction exactly because w(beta^k)=kw. The representation/trace conventions and unitary path models can be checked in [Aharonov–Jones–Landau, Sections 2.6–2.13](https://arxiv.org/html/quant-ph/0511096v2).

Generic TL_n is split semisimple, with blocks labeled by j=n,n-2,...,epsilon. Let B_j be its cell-module matrices and

\[
\Delta_0=1,\quad\Delta_1=\delta,\quad
\Delta_{j+1}=\delta\Delta_j-\Delta_{j-1}.
\]

The unnormalized closure trace is

\[
s_k:=\delta^n m_k=\sum_j\Delta_j(\delta)\operatorname{Tr}(B_j^k).
\tag{2}
\]

Thus, over an algebraic closure of F,

\[
s_k=\sum_{\lambda\in\Lambda}c_\lambda\lambda^k,
\qquad c_\lambda=\sum_j m_{j,\lambda}\Delta_j(\delta),
\tag{3}
\]

where m_{j,lambda} is the algebraic multiplicity. There are no k-polynomial factors in (3): ordinary traces kill the nilpotent portions of Jordan blocks. Every eigenvalue is nonzero because B is invertible. Cayley–Hamilton yields a linear recurrence; the generating function is sum c_lambda/(1-lambda z).

The quantum-dimension expansion in (2) follows equally from closing the minimal matrix idempotents: the trace of each primitive idempotent in the j block is Delta_j. Its positivity at real delta>2 is also visible directly from the recurrence Delta_j=U_j(delta/2).

## 2. Strongest generic lemma: no spectral mode is invisible

**Lemma A.** For any invertible generic TL element B, the power-trace Hankel rank equals the number D of distinct eigenvalues across its blocks. The full sequence (s_k) determines the characteristic polynomial of B in every individual TL block.

**Proof.** Each c_lambda in (3) is a nonzero polynomial: its coefficients in the Delta_j basis are nonnegative integers, not all zero, and all Delta_j are positive at delta>2. For the D by D Hankel matrix H=(s_{a+b}) with a,b=0,...,D-1,

\[
\det H=\left(\prod_\lambda c_\lambda\right)
\left(\prod_{\lambda<\mu}(\lambda-\mu)\right)^2\ne0.
\]

The entire Hankel matrix has rank at most D by (3), hence exactly D. Its recurrence identifies the distinct eigenvalues and a Vandermonde system identifies each c_lambda. Since the Delta_j are monic of distinct degrees, they are linearly independent over Q. Expanding c_lambda uniquely in this basis recovers every integer m_{j,lambda}. This proves the blockwise characteristic-polynomial claim. QED.

In particular, two generic TL elements having identical power traces have identical characteristic polynomials in each block. This is stronger than equality of weighted spectral measures at one specialization. It still does not give equality of elements: conjugate elements have identical power traces, and traces alone do not determine Jordan structure for arbitrary TL elements.

If M is the sum of the cell-module dimensions, equality of moments k=0,...,2M-1 already suffices to compare two such elements: their difference sequence has at most 2M distinct exponential modes, and the corresponding Vandermonde system is invertible. This is an exact finite verification statement, not an efficiency claim.

## 3. Skolem–Mahler–Lech: the precise progression statement

For a fixed target C in F, the zero set of s_k-C is a finite union of arithmetic progressions and a finite set, by the characteristic-zero [Skolem–Mahler–Lech theorem (Lech, 1953)](https://archive.ymsc.tsinghua.edu.cn/pacm_paperurl/20170108203416870878892). This applies over Q(A), not just after numerical specialization. It does not by itself provide an effective bound on the exceptional set.

For a specified progression k=a+bh, group eigenvalues by mu=lambda^b. Then

\[
s_{a+bh}=\sum_\mu d_\mu\mu^h,
\qquad
d_\mu=\sum_{\lambda^b=\mu}c_\lambda\lambda^a.
\]

The exact condition for s_{a+bh}=C for all h>=0 is

\[
d_\mu=0\quad(\mu\ne1),\qquad d_1=C.
\tag{4}
\]

The same condition follows if equality holds for all sufficiently large h, since all mu are nonzero. Infinite equality therefore concerns root-of-unity RATIOS and cancellation within classes; it does not force every lambda to be a root of unity.

**Counterexample even with unitary positivity.** Take normalized trace on M_3(C) and U=diag(1,z,-z), where |z|=1 and z is not a root of unity. Then

\[
\tau(U^{2h+1})=1/3
\]

for every h. The two nonperiodic eigenvalues cancel. The version diag(1,2,-2) shows the same failure for a positive trace and a self-adjoint nonunitary matrix. These are matrix counterexamples to the proposed inference, not asserted braid realizations.

Positive Markov weights at delta>2 prevent cancellation of a single eigenvalue coefficient c_lambda in the FULL sequence, as Lemma A uses. They do not prevent the offset phases lambda^a in (4) from canceling on a progression.

## 4. Toeplitz positivity: the rigidity it really gives

Let U be unitary in a finite-dimensional C*-algebra with a faithful positive normalized trace tau. Put m_k=tau(U^k), including m_{-k}=conjugate(m_k). Then

\[
T_d=(m_{j-i})_{0\le i,j\le d}\succeq0,
\qquad
\bar p^T T_d p=\tau(P(U)^*P(U)).
\tag{5}
\]

Consequently a null vector of T_d is exactly an annihilating polynomial P(U)=0. All moments determine the positive weighted spectral measure. If they match a reference unitary W, they determine its spectral support and weights, not its placement of eigenspaces or its operator identity.

There are useful precise special cases:

- If tau(U)=z with |z|=1, then tau((U-z)^*(U-z))=0, hence U=zI. One saturated moment suffices.
- If tau(U^b)=1, then U^b=I. A constant progression through the identity value is much stronger than an interior-value progression.
- If W has distinct eigenvalues z_1,...,z_d and the moments of U and W agree for |k|<=d, take P(z)=product(z-z_i). Equation (5) gives P(U)=0. The remaining moments recover the weights on that support.
- At a single real delta>2, positivity of the trace alone does not make arbitrary B unitary or normal. Even all identities tau(B^k)=1 permit B=I+N with nonzero nilpotent N. That limitation is absent for unitary U, not for general B.

## 5. Generic braid-image saturation and its normalization trap

For fixed n, specialize A_r=i exp(pi i/(2r)) with r>n+1. Then delta_r=2cos(pi/r), the TL_n Markov trace is positive and faithful, and braid images (including their writhe phases) are unitary. All generic cell blocks survive at these levels. The path model gives these properties; the Chebyshev trace weights are strictly positive because j+1<r.

**Lemma B.** If B is the writhe-corrected generic image of a braid and tau(B)=1 identically as a rational function of A, then B=I in generic TL_n.

**Proof.** At every sufficiently large r, the first bullet above gives B(A_r)=I. Each coefficient of B-I in the finite diagram basis is a Laurent polynomial (or a rational function after a change of basis) vanishing at infinitely many distinct A_r. It is therefore identically zero. QED.

This does not require all power moments. But its Jones hypothesis is

\[
V_{\widehat\beta}=\delta^{n-1},
\]

the n-component unlink value at that braid width. For a Jones-trivial K represented on n>1 strands, the actual input is

\[
\tau(B)=\delta^{1-n},
\]

an interior trace value at large unitary levels. It supplies neither saturation nor any of the higher moments. Identity of the TL image would in any case leave the braid-kernel/topology question; no general faithfulness assumption is being inserted.

## 6. What would make this a route to the unknot conjecture?

The useful positive result is Lemma A: the generic entire power family is spectrally complete, block by block. The useful unitary result is (5): moment-kernel relations become exact operator relations. Neither is supplied by V_K=1 for one closure.

A revival requires a geometric theorem converting that SINGLE Jones equality into a specific annihilating moment relation, or into equality of sufficiently many power/mixed closures with a reference. Powering a braid is not such a theorem. The closures change, and their component counts depend on the permutation powers; one may not assume every member remains a knot. A mixed trace such as tau(U V*)=1 would force U=V, but it is additional closure data, not a consequence of their separate Jones values.

Thus dynamics offers a rigorous observable-orbit dictionary and a strong finite moment lemma. The missing step is geometric propagation from one ordinary Jones polynomial to the extra moments, not a spectral or positivity argument after those moments are available.

## 7. Finiteness theorem for the unknot Jones fiber along every fixed braid-power orbit

**Theorem C (root's proposed corollary, independently checked).** Fix n>1 and beta in B_n. Then

\[
\{k\in\mathbb Z_{>0}:V_{\widehat{\beta^k}}=1\}
\]

is finite. No hypothesis of faithfulness, positivity, pseudo-Anosov behavior, or nontriviality of beta is required. The same conclusion holds for nonzero integer powers by applying the positive-power result to beta^{-1}.

**Proof.** Retain B and s_k from (1)–(3), so the flat Jones condition is s_k=delta. The one-dimensional top block j=n has e_i=0 and therefore has eigenvalue

\[
\lambda_* =(-A^3)^{-w}A^w=(-1)^w A^{-2w}.
\tag{7}
\]

Suppose there are infinitely many flat powers. Skolem–Mahler–Lech supplies an infinite progression k=a+bh (b>0) on which s_k=delta. Group the exponential terms by lambda^b, as in (4), and consider the group mu_*=lambda_*^b. Every lambda in this group is lambda=zeta lambda_* for a b-th root of unity zeta. Such zeta lies in the algebraic constants Qbar, even though lambda lives in an algebraic extension of Q(A). The group's coefficient is

\[
d_{\mu_*}=\lambda_*^a
\sum_j\Delta_j(\delta)
\sum_{\lambda^b=\lambda_*^b}m_{j,\lambda}\zeta_\lambda^a.
\tag{8}
\]

In the inner polynomial combination the coefficient of Delta_n is exactly 1: the top block has dimension one, its sole eigenvalue is lambda_*, and its zeta is 1. All other terms have j<n. Since the Delta_j have distinct degrees in the transcendental delta, they remain linearly independent over Qbar. Thus (8) is nonzero.

The target sequence is constant. Independence of distinct exponential sequences mu^h now forces mu_*=1. Equation (7) and transcendence of A imply w=0, hence lambda_*=1.

The mu=1 group must therefore equal the constant target delta. Every eigenvalue in this group is a root of unity and hence an algebraic constant. Its coefficient is a Qbar-linear combination of Delta_j with coefficient 1 on Delta_n. It has degree n in delta. It cannot equal delta, of degree 1, because n>1. Contradiction. QED.

**What the theorem does and does not say.** Every fixed braid has a last positive Jones-trivial power. This proof gives no effective value for that threshold, no uniform bound over beta, and no test that the first power is nontrivial. It excludes an infinite constant-power route to counterexamples; it does not detect the unknot for a single arbitrary closure. The n=1 exception is necessary: its sole braid has unknot closure at every power.

**Narrow prior-art check.** The nearest direct primary result found is [Berceanu–Nizami, *Recurrence relation for Jones polynomials*, Theorem 1.7](https://arxiv.org/pdf/1002.3735): varying one generator exponent in a fixed braid word gives at most two Jones-trivial closures, and their exponents differ by two. Their family is alpha sigma_i^e gamma, not an arbitrary whole-braid orbit beta^k. Their Proposition 1.5 separately treats powers of the three-strand Garside braid. The narrow check did not locate Theorem C in this generality; this is not a novelty certification.
