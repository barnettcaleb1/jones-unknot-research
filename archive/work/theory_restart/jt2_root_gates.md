# Classical-root gates for an exact two-component counting encoding

17 November 2026. Bounded algebraic audit of the proposed variable factor
`(1-t)^m`. No diagrams were generated or searched. The results constrain the
prefactor of an encoding; they do not construct a realizable signature or a
hardness reduction. New deductions below are TRUSTED pending independent read.

## 1. Integral normalization

For an oriented two-component link, put

\[
 F_L(t)=t^{-1/2}V_L(t)+1+t^{-1}\in\mathbb Z[t,t^{-1}].
\]

The parity of Jones exponents is the standard consequence of the oriented
skein relation: for a c-component link they lie in `(c-1)/2 + Z`.
Thus `F_L=0` is exactly the two-component unlink Jones target. This uses the
ambient normalization and a fixed orientation convention, not equality up to
an instance-dependent unit. It is the same defect as
`Delta_L(q)=V_L(q^2)+q+q^-1`, divided by q, with t=q².

Use the skein convention

\[
 t^{-1}V_+-tV_-=(t^{1/2}-t^{-1/2})V_0.
\]

Assume an exact nonzero encoding `F_L=N D`, with integer N and integral
Laurent D. The following gates are independent of the uniform Taylor bound.

## 2. Universal third-root gate

For every oriented two-component link,

\[
 (t^3-1)\mid F_L(t).
\]

At t=1 the assertion is `V_L(1)=-2`. At `t=exp(2pi i/3)`, take the explicit
square root `q=exp(pi i/3)`. The assignment
`V_L(t)=(-1)^(c(L)-1)` satisfies the specialized skein relation: the smoothing
changes component parity, and `t^-1-t=-(q-q^-1)`. It has the correct unknot
value, so skein induction proves the assignment. Both the two-component link
and the unlink have value −1 at this branch, whence `F_L(t)=0`. The conjugate
root follows by integral coefficients. The three factors are monic and
coprime over Q, so Gauss's lemma gives the asserted product divisibility.

Consequently every nonzero integral factorization `F_L=N D` has

\[
 (t-1)\Phi_3(t)\mid D(t).
\]

In particular, the bare prescription `F_L=N(1-t)^m` cannot hold for any
nonzero N. A fixed additional Phi3 factor repairs this elementary arithmetic
objection; it is not a prohibition on the proposed general mechanism.

## 3. A large-count Arf gate

Lickorish–Millett, *Some evaluations of link polynomials*, Comment. Math.
Helv. 61 (1986), Theorem 1, gives, for two components and the root
`q=exp(pi i/4)`,

\[
 V_L(i)\in\{-\sqrt2,0,+\sqrt2\}.
\]

The negative value is a proper link with Arf invariant zero, the positive
value is proper with Arf invariant one, and zero is the nonproper case.
For two components, properness means that their linking number is even.
Since the unlink has value −sqrt2, this yields

\[
 F_L(i)\in\{0,1-i,2(1-i)\}.
\]

If `F_L=N D`, then `D(i)` belongs to Z[i]. Comparing the two integer
coordinates shows that N divides the coefficient k in `k(1-i)`,
`k in {0,1,2}`. Therefore

\[
 |N|>2\quad\Longrightarrow\quad D(i)=0,
 \qquad \Phi_4(t)\mid D(t).
\]

For these outputs the realized link must be proper with Arf invariant zero.
This does not follow merely from multiplying by a power of `(1-t)`, since
that factor is nonzero at i.

Primary source, Theorem 1 and the definition of properness in §2:
[Lickorish–Millett PDF](https://web.math.ucsb.edu/~millett/Papers/1986Millett6LickorishCommMathHelv.pdf).

## 4. Sixth-root gate for a common prefactor

At `zeta=exp(pi i/3)`, Theorem 3 of the same primary source states

\[
 V_L(\zeta)=\pm i\,(i\sqrt3)^d,
 \qquad d=\dim_{\mathbb F_3}H_1(\Sigma_2 L;\mathbb F_3)\ge0.
\]

Unlike the Arf values, this set is unbounded even when the link has two
components. It does not give a uniform large-N argument for arbitrary
instance-dependent D. But its arithmetic shape gives a sharp gate when the
same prefactor must realize the counts 1, 2 and 3.

**Lemma.** Suppose a fixed integral Laurent D occurs in exact encodings
`F_(L_j)=j D` for three actual two-component links, j=1,2,3. Then
`Phi6(t)` divides D.

**Proof.** Put `q=exp(pi i/6)`, so `q²=zeta`, and `C=q D(zeta)`. The three
Jones values are

\[
 v_j=-\sqrt3+jC.
\]

The evaluation theorem puts each in one of the two sets

\[
 \{\pm\sqrt3\,3^a:a\ge0\}\quad\hbox{or}\quad
 \{\pm i\,3^a:a\ge0\}.
\]

If either v1 or v2 is real, C is real. They cannot both be imaginary:
their real parts would require simultaneously `Re C=sqrt3` and
`2 Re C=sqrt3`. Hence C is real, and all three values use the real set.
Write c=C/sqrt3. Since `v1/sqrt3=-1+c` is an odd integer, c is an even
integer. If c<0, then `-1+c=-3^a` with a>=1, whereas
`-1+2c=1-2*3^a` has absolute value 2 mod3 and greater than one; it cannot
be a power of three. If c>0, then `-1+c=3^a` and
`-1+2c=2*3^a+1=3^b`. Reduction mod3 forces a=0, and then c=2. But the
third value is `-1+3c=5`, again not a signed power of three. Thus c=0,
so D(zeta)=0. Integral divisibility follows. QED.

This applies, for example, to a proposed fixed-variable-count encoding with
prefactor D_m independent of the formula, whenever formulas with counts
1,2,3 occur at that size. It does **not** apply when D_phi changes arbitrarily
with the formula. Nor does agreement at these three counts validate an
encoding: it only forces one root of its common prefactor.

Combining the universal gate and the j=3 Arf gate gives

\[
 (t-1)\Phi_3(t)\Phi_4(t)\Phi_6(t)\mid D_m(t).
\]

Thus if `D_m=(1-t)^m C(t)`, the fixed seed factor C must include
`Phi3 Phi4 Phi6`. These fixed factors do not interfere with the intended
growing Taylor order. They remove a cheaply falsifiable defect in a proposed
design, without providing any geometry.

## 5. Linking and the limits of root tests

Differentiating the skein relation at t=1 shows

\[
 V_L'(1)=-3\operatorname{lk}(L_1,L_2),\qquad
 F_L'(1)=V_L'(1)
\]

in the convention fixed above. For a mixed crossing change, the derivative
difference is −3 and the linking-number difference is +1; for a self-crossing
change both derivative difference and linking-number difference are zero.
Reduction to the unlink proves the formula. Hence Taylor depth at least two
forces linking number zero. A proposed `(1-t)^m` construction with m>=2
must meet that geometric requirement on every nonzero-count output.

The determinant evaluation at t=−1 is not bounded for fixed component count,
and the sixth-root homology exponent d is likewise unbounded. No argument
here forces a factor `(t+1)` or applies the knot-specific ROOTS theorem for J
to arbitrary two-component link defects. In particular, satisfying the
displayed factors is not equivalent to satisfying every link realization
constraint.

A formal polynomial

\[
 F_{m,N}(t)=N(t-1)^m\Phi_3(t)\Phi_4(t)\Phi_6(t),\qquad m\ge2,
\]

passes all the root-value and linking-derivative checks in this note. Whether
the associated expression for V comes from an actual two-component link is
entirely unresolved. That is precisely the distinction the gadget program
must retain.
