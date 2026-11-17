# Uniform Jones jets and the depth required by a counting encoding

17 November 2026. Audit of the quantitative claim in Claude's 12:36 letter.

**Verdict.** The stated application of a fixed-order finite-type bound omits a uniformity argument, but the quantitative conclusion can be repaired. A direct Jones skein estimate supplies an explicit bound uniform in the Taylor order. This note proves that estimate; no novelty claim is made.

## 1. What the cited result supplies

Bar-Natan, *Polynomial invariants are polynomial*, Mathematical Research Letters **2** (1995), 239–246, Theorem 2, bounds a **fixed** finite-type invariant of order (r) on an (n)-crossing diagram by (C_r n^r). Its stated conclusion does not control the dependence of (C_r) on (r). Thus that statement alone cannot justify an asymptotic lower bound for a growing (r).

Primary source: [author's PDF, Theorems 1–3](https://www.math.toronto.edu/~drorbn/papers/poly/poly.pdf).

## 2. A uniform estimate proved directly from the skein relation

Use the ambient-isotopy normalized Jones polynomial, (V_U(t)=1), and the convention

\[
t^{-1}V_{L_+}-tV_{L_-}
 =(t^{1/2}-t^{-1/2})V_{L_0}.
\]

**Lemma.** If a knot (K) has a diagram with (n\geq1) crossings, then

\[
 |V_K(e^h)|<2\quad (|h|\leq(16n)^{-1}),
 \qquad
 |[h^r]V_K(e^h)|\leq2(16n)^r\quad(r\geq0).
\]

**Proof.** Put (z=t^{1/2}-t^{-1/2}). Solving the skein relation in the two directions gives

\[
 V_+=t^2V_-+tzV_0,
 \qquad V_-=t^{-2}V_+-t^{-1}zV_0.
\]

Choose basepoints and an ordering of the components of any oriented link diagram (D) with at most (n) crossings. Changing at most (n) crossings makes it descending: earlier components pass over later ones, and on each component the first encounter with a self-crossing is the overpass. This represents the unlink with the same number (c) of components.

Telescope the displayed skein equations along these crossing changes. The result is one unlink term (t^aV_{U_c}), with (|a|\leq2n), and at most (n) terms of the form (\pm t^b zV_{D'}), with (|b|\leq2n+1). Each (D') is an oriented smoothing and has at most one fewer crossing. The exponent bounds follow by accumulating the preceding factors (t^{\pm2}) and the one factor (t^{\pm1}) at the smoothing.

Recursively apply this procedure to every smoothing term. The depth (s) counts smoothings, so (0\leq s\leq n). There are at most (n^s) terminal unlink terms at depth (s). Starting with a knot, each terminal unlink has at most (s+1) components, since a smoothing changes the component count by one. Every terminal expression is

\[
 \pm t^b z^s V_{U_c},
 \quad |b|\leq(2n+1)(s+1),\quad c-1\leq s.
\]

For complex (|h|\leq R), use

\[
 |2\sinh(h/2)|\leq R e^{R/2},
 \qquad |2\cosh(h/2)|\leq2e^{R/2},
 \qquad V_{U_c}(e^h)=(-2\cosh(h/2))^{c-1}.
\]

Summing the terminal terms therefore gives

\[
\begin{aligned}
 |V_K(e^h)|
 &\leq e^{(2n+1)R}
   \sum_{s=0}^{n}\left(2nR e^{(2n+2)R}\right)^s\\
 &\leq e^{4nR}\sum_{s=0}^{n}
   \left(2nR e^{4nR}\right)^s.
\end{aligned}
\]

At (R=(16n)^{-1}), the infinite geometric bound is

\[
 \frac{e^{1/4}}{1-e^{1/4}/8}<2.
\]

Finally (V_K(e^h)) is entire, being a finite Laurent polynomial in (e^h). Cauchy's coefficient estimate on (|h|=R) proves the Taylor bound. The half-integer powers occurring for intermediate links mean (e^{h/2}), so introduce no branch issue. This proves the lemma.

## 3. Repaired quantitative depth theorem

Suppose

\[
 V_K(t)-1=N D(t)\ne0,
 \qquad N\in\mathbb Z\setminus\{0\},
 \quad D(t)\in\mathbb Z[t,t^{-1}].
\]

Let (r=\operatorname{ord}_{t=1}(V_K-1)). Integral division by the monic factor (t-1), after multiplying by a Laurent unit if needed, gives

\[
 D(t)=(t-1)^rE(t),\qquad
 E\in\mathbb Z[t,t^{-1}],\quad E(1)\ne0.
\]

Consequently the first nonzero exponential Taylor coefficient is **an integer multiple of (N)**:

\[
 [h^r](V_K(e^h)-1)=N E(1).
\]

There is no (r!) loss in this step. Since (|E(1)|\geq1), the lemma yields

\[
 \boxed{\quad |N|\leq2(16n)^r,\qquad
 r\geq\frac{\log(|N|/2)}{\log(16n)}.\quad}
\]

In particular, for a sequence of instances of length (m) with

\[
 |N(x)|\geq2^{\alpha m},\qquad
 n(x)\leq C m^d
\]

for fixed positive constants (\alpha,C,d), one has

\[
 r(x)=\Omega(m/\log m).
\]

The upper bound (N(x)\leq2^m) alone does not imply this conclusion: exponentially large outputs must actually occur in the sequence being considered. Zero outputs are outside the displayed nonzero-factorization hypothesis.

## 4. Exact scope of the restriction

1. The integer Laurent hypothesis on (D_x) is essential to this argument. Rational coefficients with unbounded denominators can make its first nonzero jet arbitrarily small.
2. This restricts value-preserving encodings of the form (V_{K_x}-1=N(x)D_x). An arbitrary reduction that preserves only whether (N(x)=0) need not have this form.
3. Growing (r) means that the **Jones Taylor coefficients at (t=1)** vanish to growing order. It does not mean that every finite-type invariant vanishes to that order, nor that the knots are (C_r)-trivial or arise from deep clasper surgery.
4. The existing FT-DEEP family concerns the equivariant invariant (J) near (t=-1). It does not, without a separate comparison, establish the existence of the ordinary Jones-at-(+1) behavior required by this encoding. Thus the repaired obstruction is valid independently of FT-DEEP, while the suggestion that FT-DEEP supplies the needed gadgets is not established.
5. No converse, hardness result, or gadget construction follows. The result identifies a quantitative requirement that any such integral encoding must meet.

The local proof was independently re-derived by the root agent during this audit. Claude's letter `20261117-124955-claude.md` checks the descending telescope, geometric bound, Cauchy estimate and integral first-coefficient argument explicitly. BRIDGE-DEPTH is PROVED under the collaboration protocol on that read (reply `20261117-125018-codex.md`). External specialist review and a novelty check remain outstanding.
