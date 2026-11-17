# An integral content obstruction and a two-ended divisor budget

17 November 2026. Theory subnote for the round-E resonance question. All assertions below follow by hand algebra from the banked integral box dictionary; no enumeration is used. Sources for the conventions: `collab/data/roundE/arb_REPORT.md`, sections 1–2, and `collab/data/engineC1/REPORT.md`, section 3.2.

## 1. Keep the amplitude in an integral eigenpair

Put

\[
 \Lambda=\mathbb Z[t,t^{-1}],\quad d=1-t^3,\quad
 C=(1-t)(1+t^2),\quad e=-t/(1+t^2).
\]

An actual body has integral state \((a,c)\), with channel amplitudes
\(a,b=a+dc\). The eigenpair is

\[
 A=a+Cc,\qquad B=Cc,\qquad z=B/A.
\]

Thus \(a=A-B\), \(b=A-eB\). Both eigen-coordinates are integral. In particular, the apparent denominator \(\Phi _3=1+t+t^2\) in
\(A=(ta+(1+t^2)b)/\Phi _3\) cancels on the actual integral lattice. A common framing monomial multiplies both coordinates.

The exact rules are

\[
 F_m:(A,B)\longmapsto(A,(-t)^{-m}B),
\]

up to that common unit, and

\[
 \begin{aligned}
 A_{12}&=A_1A_2-eB_1B_2,\\
 B_{12}&=A_1B_2+B_1A_2-(1+e)B_1B_2.
 \end{aligned}
\]

These expressions are integral because \(B_i\in C\Lambda\). Consequently

\[
 z_{12}={z_1+z_2-(1+e)z_1z_2\over1-ez_1z_2}.
\]

For \(Y^N\), set \(r=t^{-3N}\) and \(k=(r-1)/\Phi _3\in\Lambda\). Then

\[
 \binom{A'}{B'}=
 \begin{pmatrix}1+(1+t^2)k&tk\\(1+t^2)k&1+tk\end{pmatrix}
 \binom A B.
\]

Its determinant is \(r\), a unit. These are transformation identities, not positivity statements.

## 2. A genuine inductive obstruction: irreversible content

For an irreducible \(p\in\Lambda\), define

\[
 c_p(a,c)=\min\{\nu_p(a),\nu_p(c)\}.
\]

The banked matrices \(X,Y\) are in \(\mathrm{GL}_2(\Lambda)\), so \(c_p\) is unchanged by their powers, hence by \(F_m,Y^N\). The integral star rule is

\[
 (a_1,c_1)*(a_2,c_2)=
 (a_1a_2,\ a_1c_2+c_1a_2+dc_1c_2).
\]

Therefore

\[
 c_p(v_1*\cdots*v_n)\geq\sum_i c_p(v_i).
\]

This is an actual monotonicity theorem, valid also at primes dividing \(d\). A factor deposited in both coordinates can never be removed by subsequent star products or nesting. Every subsequent closure is divisible by it, so a unit closure requires zero content at every ancestor node.

Away from \(d\), the gain has an exact formula. Since \((a,c)\leftrightarrow(a,b)\) is invertible locally at \(p\nmid d\), put
\(r_i=\nu_p(b_i/a_i)\). Then

\[
 c_p(v_1*\cdots*v_n)=\sum_i c_p(v_i)
 +{\sum_i|r_i|-|\sum_i r_i|\over2}.
\]

Proof: write \(A_i=\nu_p(a_i)\), \(B_i=\nu_p(b_i)\); the left side is \(\min(\sum A_i,\sum B_i)\), and use
\(\min(x,y)=(x+y-|x-y|)/2\). Thus a zero of one child's channel slope and a pole of another at the same finite place deposit permanent scalar content. In a hypothetical unit-producing tree this opposite-sign configuration is forbidden at every star node, for every \(p\nmid d\). This restriction uses both channels and the amplitude; it is lost in a slope-only analysis.

It does not prove that every nontrivial tree deposits content. The primitive, sign-compatible core remains open.

## 3. The finite divisor gives an exact two-ended resonance budget

Assume \(A,B\ne0\), and write \(z=B/A\). Under a twist, the divisor of \(z\) on \(\mathbb C^*\) is unchanged. Also

\[
 \kappa(z)=\nu_0(z)+\nu_\infty(z)
\]

is unchanged: multiplication by \((-t)^{-m}\) subtracts \(m\) at zero and adds \(m\) at infinity. Neither assertion is claimed to be monotone under star or \(Y\).

Both ends can be order-zero resonant in the same \(F_m\) only if \(\kappa=0\), and then necessarily \(m=\nu_0(z)\). At this unique twist the leading constants at both ends must additionally be 1 before cancellation of \(1-(-t)^{-m}z\) at both ends is possible. Cancellation at just one end is not excluded.

Suppose these conditions hold. Let

\[
 w=(-t)^{-m}z,\quad
 \tau_0=\nu_0(1-w)>0,\quad
 \tau_\infty=\nu_\infty(1-w)>0,
\]

and let \(H_{\mathrm{fin}}(z)\) be the total pole multiplicity of \(z\) on \(\mathbb C^*\). If \(w\not\equiv1\), then

\[
 H_{\mathrm{fin}}(z)-\tau_0-\tau_\infty
 =\#\{\text{zeros of }1-w\text{ on }\mathbb C^*\},
\]

counting multiplicity. In particular the left side is nonnegative. This follows from degree zero of a rational-function divisor: \(1-w\) has the same finite poles as \(w\), no poles at either end, and the stated zeros at the ends.

A horizontal unit closure is the stronger equation

\[
 A-(-t)^{-m}B=\pm t^j.
\]

It first requires \(\gcd(A,B)\) to be a unit. After this primitive reduction, every finite zero of \(1-w\) is a zero of the closure, because it cannot also be a pole of \(w\). Thus, in the doubly resonant case, a unit closure requires the exact saturation

\[
 \boxed{H_{\mathrm{fin}}(z)=\tau_0+\tau_\infty.}
\]

Conversely, saturation and primitive \((A,B)\) make the closure a rational constant times a Laurent monomial; the integer coefficient must still be checked to be \(\pm1\). There is no residual \(\Phi _3\) budget: that factor was an artificial scaling of the eigenpair and cancels before this argument.

This is a precise global replacement for arbitrarily deep end jets in a fixed resonant state. It is not yet an inductive strict inequality. The star law can create or cancel poles, and its denominator \(1-ez_1z_2\) is exactly where the missing realizability statement would have to enter.

### Sharpening: an exact span formula and two possible twists

The parent supplied the following general version, audited independently here. Assume \((A,B)\) primitive and \(f_m=A-(-t)^{-m}B\ne0\). Set

\[
 r_0=\nu_0(z)-m,\quad r_\infty=\nu_\infty(z)+m,
 \qquad \tau_e=\max\{\nu_e(1-(-t)^{-m}z),0\}.
\]

Then

\[
 \boxed{\operatorname{span} f_m=
 H_{\mathrm{fin}}(z)+(-r_0)_++(-r_\infty)_+
 -\tau_0-\tau_\infty.}
\]

Proof: the poles of \(1-(-t)^{-m}z\) consist of the finite poles of \(z\), and additional end poles of the displayed orders. Its finite zeros are exactly those of \(f_m\), by primitivity. Count zeros and poles. The number of finite nonzero zeros of a nonzero Laurent polynomial, with multiplicity, is its span.

If \(H_{\mathrm{fin}}(z)>0\), a monomial closure consequently requires

\[
 m\in\{\nu_0(z),-\nu_\infty(z)\}.
\]

At least one of the resonant ends must have leading constant 1. Thus there are at most two possible outer twists for a fixed primitive body, even if its nesting and end cancellation depth are arbitrary. Each candidate is decided by the exact span formula (and then its scalar coefficient). If the two candidates coincide, one can still have \(\tau_0=0\) or \(\tau_\infty=0\): only the doubly-cancelling case gives the positive-contact version above. For example \(A=1+t,B=2+t\) has \(f_0=-1\), \(\tau_0=0,\tau_\infty=1\).

The case \(H_{\mathrm{fin}}=0\) is elementary and separate: \(A\) is a monomial. If \(B\) has at least three terms no twist gives a monomial difference; if it has two terms only alignment with one of their exponents can do so. Zero eigen-coordinates and monomial eigenpairs are checked directly. This is a finite fixed-body reduction, not a proof that its candidates fail on every actual nonrational body.

## 4. Cheap falsifier for an algebra-only strict inequality

Fix an integer \(\mu\ne0\), put \(u=(-t)^\mu\), and take an arbitrary Laurent polynomial \(E\). The formal integral state

\[
 (a,c)=\bigl(1+(u-1)CE,\ E\bigr)
\]

has eigenpair

\[
 (A,B)=(1+uCE,CE),\qquad A-uB=1.
\]

Both state content and eigenpair content are units. Choosing \(E\) divisible by arbitrary powers of \(t+1\), and by \(\Phi _6\Phi _{10}\), enforces any fixed required jet at \(-1\) and the corresponding finite root gates; the evaluations of \(a\) at \(1,\pm i\) are automatically 1. With the support of \(uCE\) extending on both sides of exponent zero, the resonant ratio \(uB/A\) approaches 1 at both ends and saturates the divisor budget exactly.

This is a formal skein state, not a constructed single body. It shows precisely why the content theorem, divisor budget, and finite root gates cannot alone prove non-flatness. A successful inductive theorem must exclude realization of this unit-fibre family by the permitted body operations, or force content or unsaturated divisor budget before it is reached.

Finally, N-INF proves that exact finite end-signature lists do not close. It does not rule out a finite control system with unbounded integer registers, nor a coarse finite quotient carrying a valid obstruction. The content valuations and the divisor budget are candidates for such unbounded data; no finite-state or positivity theorem for them is asserted here.
