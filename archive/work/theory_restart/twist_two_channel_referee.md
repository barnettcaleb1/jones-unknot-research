# Referee: the fixed two-channel family and finite flat twist fibers

16 November 2026. Inputs: Claude120708 item3, Claude192557 item1, and the
subsequent written derivation in
`/Users/calebbarnett/jones-lanes/theory-restart/mont/nest/REPORT.md`, section3.
No search was run. Three exact bracket initial values and the two algebraic
tie values were checked; the all-parameter conclusion uses the skein proof.

## Verdict

The family really has two contributing channels, after a local cap slide
identifies its twist as the special-region twist of a fixed box. The displayed
polynomial in the letter is in an **unpreferred framing**. In the preferred
normalization it must be multiplied by `t^(2n-6)`. This is already repaired
in the newer NEST report. It changes degrees but not span or monomiality.

The all-integer nonflatness conclusion is correct. It has a short exact
piecewise span proof; no interval scan is needed. The general finite-flat
twist lemma is also correct when phrased in terms of monomiality and distinct
colored eigenvalue degrees. Its scope does not imply that the homological
outline has bounded overshoot: the observed top-N formula remains a separate
categorified assertion.

## 1. The actual marked site has two channels

The halfword is

```
T_n = s.r1.x2.(y1)^n.y0.r2.y0.y1.y0.y1.x2.u3.u1,
```

using x1 for negative exponents. In a half-diagram, slide the cap past its
adjacent crossing:

```
r1.x2  ->  r2.y1.
```

This is the cup/crossing naturality move: the right leg passing over the
adjacent strand becomes the left leg passing over it from the other side.
The crossing letter changes from x2 to y1, not to x1. The reflected half
undergoes the same move, so the isotopy is equivariant. Interchange the two
disjoint terminal cups (u3.u1 -> u1.u1 in the reindexed diagram). The result is

```
T_n  ~  s.r2.(y1)^(n+1).B.u1,
B = y0.r2.y0.y1.y0.y1.x2.u1.
```

This is a single fixed box, not an assumption that the whole quotient is
rational. The boundary of the box has two axis points of color1 and two arc
points of color2. The state space can be written

\[
\operatorname{Hom}(V_1\otimes V_1,V_2\otimes V_2)
\cong\operatorname{Hom}(V_1,V_1\otimes V_2\otimes V_2).
\]

The two common fusion channels are 0 and2:
`V1 tensor V1=V0+V2`, whereas `V2 tensor V2=V0+V2+V4`.
There is no color4 contribution in this **particular closed frame**. This is
stronger than a fit of an order-three recurrence with one zero coefficient.
An arbitrary other arc-pair twist site may have all three channels.

In the TH-2BR convention the y1 special-region crossing acts as X^-1. Its
eigenvalues on this space are 1 and `(-t)^-1`. The crossing/cabling convention
used by the unframed quotient bracket instead packages the same two channel
contributions with eigenvalues `t^2` and `-t`. Their ratio is the same `-t`;
the difference is the common ribbon-framing factor and the one-crossing
offset m=n+1. This distinction is essential when quoting exact degrees.

Equivalently, the raw two-colored crossing has the three possible eigenvalues
`t^2,-t,t^-1` in channels0,2,4, respectively, with t=A^4 in the direct-bracket
implementation. The above admissibility kills the third channel. Global
framing normalization changes them by a common monomial only.

## 2. Exact formula and the preferred unit

Put

\[
\begin{aligned}
\alpha&=t^{-5}(t^2-t+1),\\
\beta&=t^2(t^4-t^3-1)+t^{-6}(t^2-t+1),\\
F_n&=\alpha t^{2n}+\beta(-t)^n.
\end{aligned}
\]

The all-n skein expansion proves that the raw scalar has this form with
fixed coefficients; two independent initial values determine those
coefficients. For extra calibration, the exact bracket implementation
`flat_search.bracket_vector` was used on the fixed inputs n=0,1,2. In its
unframed quotient convention the other closure scalar is u=1 at each input,
and the three first coefficients are exactly

\[
\begin{aligned}
F_0&=t^{-6}+t^{-3}-t^2-t^5+t^6,\\
F_1&=-t^{-5}+t^{-4}-t^{-2}+t^{-1}+t^3+t^6-t^7,\\
F_2&=t^{-4}-t^{-3}+t^{-2}+t^{-1}-1+t-t^4-t^7+t^8.
\end{aligned}
\]

These checks are retained in
`referee_checks/twist_two_channel.py` and its JSON. They are fixed tests, not
a word enumeration. The calculation uses the existing integer TL evaluator;
it is independent of Khovanov homology, not a new implementation of TL.

The claim "u=1" is insufficient to say that the preferred longitude framing
has been used. In fact

\[
F_n(-1)=1,\qquad F_n'(-1)=2n-6.
\]

Preferred J satisfies `J=1 mod(t+1)^2`. Multiplying by a unit `s t^k`, its
value and derivative at−1 force s=1 and k=2n−6. Thus

\[
\boxed{\ J(T_n)=t^{2n-6}F_n\ }.
\]

At n=1 this is

\[
-t^{-9}+t^{-8}-t^{-6}+t^{-5}+t^{-1}+t^2-t^3,
\]

exactly the previously certified endpoint-counterexample value. The
unshifted formula in120708 has endpoints−5 and7, not−9 and3.

In the box notation of the newer report,

\[
\begin{aligned}
P_B&=t^{-15}(t^2-t+1),\\
Q_B&=(t^{-7}+t^{-4}-t^{-3})-P_B,\\
J(T_n)&=t^{4n+4}P_B+(-1)^{n+1}t^{3n+3}Q_B.
\end{aligned}
\]

The identities `alpha=t^10 P_B` and `beta=-t^9 Q_B` make this identical to
the corrected formula. In particular the two recurrences are

\[
\begin{aligned}
F_{n+2}&=(t^2-t)F_{n+1}+t^3F_n,\\
J_{n+2}&=(t^4-t^3)J_{n+1}+t^7J_n.
\end{aligned}
\]

The coefficients on J's right side are the preferred-frame eigenvalues
`t^4,-t^3`. An exact recurrence and its normalization should always be
stated together.

## 3. No member is flat: exact span for every integer

The alpha block has support interval `[2n-5,2n-3]`; the beta block has support
interval `[n-6,n+6]`. Their four endpoint coefficients are nonzero. There are
only two possible endpoint ties: the lower one at n=−1 and the upper one at
n=9.

For n≤−2 the alpha block uniquely supplies the bottom and beta the top.
For 0≤n≤8 beta uniquely supplies both endpoints. For n≥10 beta uniquely
supplies the bottom and alpha the top. At the two tie values direct expansion
gives

\[
F_{-1}=t+t^4-t^5,\qquad
F_9=t^{13}+t^{11}-t^5+t^4-t^3.
\]

Therefore, without any remaining finite search,

\[
\operatorname{span}J(T_n)=\operatorname{span}F_n=
\begin{cases}
11-n,&n\le -2,\\
4,&n=-1,\\
12,&0\le n\le8,\\
10,&n=9,\\
n+3,&n\ge10.
\end{cases}
\]

Every span is positive. This proves the all-integer nonflatness result for
this family, regardless of the extra homology hidden beyond the polynomial
support. It is a concrete instance of controlled endpoint ties, not a
universal no-cancellation theorem.

## 4. General finite-flat twist lemma

At a fixed arc–arc crossing site, generic colored skein theory gives

\[
G_n=\sum_{c\in\{0,2,4\}}\alpha_c(A)\,
          (\epsilon_c A^{d_c})^n,
\]

up to the chosen overall framing unit. The d_c are pairwise distinct;
depending on handedness they are 8,4,−4 or their negatives, with the middle
channel carrying a minus sign. The alpha_c lie in Q(A), are independent of
n, and may vanish for the actual outside tangle. Only nonzero channels
should be retained. Fix endpoint connectivity and orientation, or split
into parity subfamilies when necessary. A preferred-framing correction
does not affect whether G_n is a Laurent unit.

If exactly one channel survives, G_n is a monomial multiple of the fixed
coefficient, hence all members are units or none are. The coefficient need
not itself be a unit. If at least two channels survive, **only finitely many
parameters can give a Laurent unit**.

Here is an explicit elementary bound. Choose a common nonzero Laurent
denominator D, write p_c=D alpha_c, and let [L,U] contain the exponents in D
and all p_c. Put W=U−L and Delta=min_{c!=c'}|d_c−d_c'|. If

\[
|n|\,\Delta>2W,
\]

the translated support intervals of the distinct nonzero channels are
disjoint. Their outermost terms cannot cancel, and

\[
\operatorname{span}(D G_n)
\ge |n|(d_{\max}-d_{\min})-W>W\ge\operatorname{span}D.
\]

But a Laurent-unit G_n would make D G_n just a shifted signed copy of D,
with equal span. Contradiction. Thus the finite candidate interval

\[
|n|\le\left\lfloor2W/\Delta\right\rfloor
\]

is rigorous (usually very nonoptimal). Signs epsilon_c and negative n cause
no issue once the support intervals are separated. This proof is about
monomiality, so it also covers changing normalizing units; it does not
mistake a fixed-value recurrence for a normalized-Jones statement.

The finite-fiber conclusion is compatible with the banked twist theory.
It does not rule out exceptional flat parameters inside the finite interval,
and does not reduce arbitrary knots to a twist family with controlled fixed
coefficients. The specific family above is stronger because both collision
parameters are handled exactly.

## 5. What the outline data do not yet prove

Reported top-N values and gaps must be expressed in the **same variable and
framing** as the chosen polynomial. If the raw exponent of t is p=q/2, a gap
of nine t-slices means eighteen units of the usual quantum grading q. A
preferred-framing shift moves both endpoints and leaves the gap unchanged.
The phrase "top quantum degree 2n+6" should not be combined with the
preferred J degrees above without explicitly giving those conversions.

The bracket formula determines J for every n. It does not establish the
reported all-n formula for the maximal quantum degree of N, or the linear
rank law dim N=18n+15. Values n=7,9,10,11 are useful checks of those laws,
not a proof. In particular the proposed eventual overshoot of nine is still
conditional on the homological top-degree formula. The no-flatness theorem
needs none of it.
