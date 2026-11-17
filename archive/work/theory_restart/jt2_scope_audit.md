# JT2: exact language, jet tractability, and the conditional depth restriction

17 November 2026. Bounded audit of Claude131014, `L2_complexity.md`, and STRESS P4. No enumeration. The statements below are elementary deductions, not a claim of literature novelty or a hardness theorem.

## 1. Fix the input and target

Input is an explicitly encoded, oriented classical link diagram with exactly two components; invalid encodings and other component counts can be rejected in polynomial time. Write

\[
 P_L(q)=V_L(q^2)\in\mathbb Z[q,q^{-1}],\qquad
 \Delta_L(q)=P_L(q)+q+q^{-1}.
\]

The normalization is the ambient-isotopy Jones polynomial with unknot value 1. The two-component unlink has value \(-q-q^{-1}\). Thus

\[
 \mathrm{JT}_2=\{L:\Delta_L(q)=0\}.
\]

Using q removes the half-integer exponents of the t-variable two-component Jones polynomial. This is exact equality with the target, not equality up to a Laurent unit. Orientations and writhe are part of the normalization. A claim about unoriented inputs needs its own convention; nothing below needs that extension.

There is an immediate many-one reduction KJT to JT2: send a knot K to the split union K with an unknot. Then

\[
 V_{K\sqcup U}(q^2)=-(q+q^{-1})V_K(q^2),
\]

so equality to the two-component unlink is equivalent to \(V_K=1\), since the Laurent ring is a domain. Consequently JT2 is not disconnected from the knot problem, but hardness of its nonsplit portion would not by itself imply hardness of KJT or a failure of JC.

## 2. JT2 belongs to C_=P

Expand the normalized bracket in the A-variable. Every coefficient is a signed count of polynomial-size witnesses: choose a smoothing at every crossing, then choose one of the two monomials in each factor of \(\delta=-A^2-A^{-2}\). The loop count, writhe shift, monomial exponent and sign are computable from the witness in polynomial time. Hence every coefficient is GapP. The relevant exponent interval has length O(n+1) for n crossings and two components.

Subtract the fixed unlink target after the same normalization. If the coefficient differences are \(g_e(D)\), the signed-count function

\[
 G(D)=\sum_e g_e(D)^2
\]

is GapP: products use pairs of signed witnesses, and sums add a polynomial-size choice of exponent. Since the coefficients are integers, G is zero exactly when every difference is zero. Invalid inputs can be assigned G=1 by polynomial-time branching. This proves JT2 in C_=P without computing the Jones polynomial in polynomial time.

Membership in this upper class does not establish C_=P-hardness. Generic evaluation hardness and approximate root-of-unity hardness have different targets and reductions.

## 3. Fixed jets of two-component links are computable in polynomial time

**Lemma.** For each fixed r, the Taylor coefficients through order r of \(\Delta_L(e^h)\) are exactly computable in time polynomial in the diagram size.

**Direct proof.** Use the descending-diagram recursion from `depth_uniform_audit.md`. At each node, changing at most n crossings to a descending unlink gives one unlink term and at most n smoothing branches. Every smoothing branch contains a factor \(z=t^{1/2}-t^{-1/2}\), of order one in h at t=exp(h). Thus a branch at smoothing depth s>r contributes nothing modulo \(h^{r+1}\). Only O(1+n+...+n^r) nodes need be retained. At depth r, the constant term of the remaining link is determined by its component count; no deeper expansion is necessary.

The diagrams, the descending crossing sequence and the accumulated integer monomial exponents are handled in polynomial time per node. The unlink factors and exponential monomials have explicit truncated Taylor series; for fixed r their rational denominators and bit lengths cause no difficulty. Replacing h by 2h gives the q-variable series used here. This proves the claim for links directly, without importing a Gauss-diagram theorem or taking the skeptic's LWPP detour.

**Corollary.** Suppose a family of two-component diagrams has the promise that every nonzero \(\Delta_L\) has \(\operatorname{ord}_{q=1}\Delta_L\le r_0\), for a fixed constant r0. Its JT2 membership test is in P: compute that fixed jet and check whether it vanishes.

The promise is about the family; this does not decide whether an arbitrary input belongs to such a family. For a polynomial-time reduction R, its output family automatically supplies the promise if the asserted bound holds for all its nonunit outputs.

## 4. Correct the “necessary unbounded depth on NO instances” claim

Let R be a deterministic polynomial-time many-one reduction from a coNP-hard language to JT2. If there is a fixed r0 such that every NO-output R(x) has nonzero defect of order at most r0, the preceding algorithm decides the source language in P. Therefore P=NP=coNP follows.

The sound conclusion is:

> Assuming P differs from NP, the orders of the nonzero defects in the NO-image set of any such hardness reduction must be unbounded.

This is not an unconditional restriction on arbitrary reductions, and it does not say the order tends to infinity along every sequence of NO instances. Many NO instances could remain shallow; the supremum over the image must be unbounded. Nor does it supply an Omega(m/log m) rate for an arbitrary zero-preserving reduction.

In particular, it is too strong to say simply that “any many-one reduction must have unbounded depth.” A reduction from an easy language can use two fixed diagrams, and a hypothetical complexity collapse also removes the hardness-based obstruction.

## 5. Uniform two-component estimate and integral count encodings

The quantitative knot estimate has a direct two-component version.

**Lemma.** If L is a two-component diagram with n>=1 crossings, then, for every r>=0,

\[
 \left|[h^r]\Delta_L(e^h)\right|\le8(32n)^r.
\]

**Proof.** In the knot proof, a smoothing-depth-s terminal unlink has at most s+1 components. Starting with two components changes this to s+2, so the previous bound acquires at most one extra factor \(2e^{R/2}\). Consequently, for the t-variable and \(|u|\le R=1/(16n)\),

\[
 |V_L(e^u)|<4e^{R/2}.
\]

Put u=2h. On \(|h|\le1/(32n)\), the target satisfies

\[
 |e^h+e^{-h}|\le2e^{1/(32n)}.
\]

The triangle inequality therefore gives

\[
 |\Delta_L(e^h)|<6e^{1/(32n)}<8.
\]

Cauchy's estimate proves the claim. The crossing-free case is the unlink and has zero defect, so does not enter the nonzero factorization below.

Now assume an exact encoding

\[
 \Delta_{L_x}(q)=N(x)D_x(q)\ne0,
 \quad N(x)\in\mathbb Z,
 \quad D_x(q)\in\mathbb Z[q,q^{-1}].
\]

If r is the order at q=1, write \(D_x=(q-1)^rE_x\). The first h-coefficient is the nonzero integer \(N(x)E_x(1)\), so

\[
 |N(x)|\le8(32n)^r,
 \qquad
 r\ge\frac{\log(|N(x)|/8)}{\log(32n)}.
\]

For polynomial diagram size and exponentially large outputs, r is Omega(m/log m), unconditionally. As before, uncontrolled denominators in D invalidate the integrality step, and an upper bound on N is not an exponential lower bound. This is a quantitative restriction on value-preserving integral encodings, not a theorem about all zero-test reductions.

## 6. The skeptic does not subsume the amplitude obstruction

STRESS P4 calls the growth obstruction a weak corollary of fixed-jet tractability. The two results have different logical force:

- Fixed-jet tractability rules out a hardness reduction only under a complexity separation assumption; otherwise its conclusion is a collapse.
- A polynomial-size integral encoding of an exponential count with a fixed nonzero factor is impossible from coefficient growth, without assuming P differs from NP or FP differs from #P.

Thus the first is more general in the allowed encoding shape, while the second is an unconditional numerical obstruction in a narrower shape. Neither should be described as simply subsuming the other. The new uniform bound quantifies the second when the factor varies with the input.

## 7. Literature scope and a concrete next obligation

A bounded search located no primary theorem establishing coNP-hardness or C_=P-completeness of this exact two-component unlink fibre. That is a search result, not a proof that the problem is open or new.

Primary statements checked:

- Hass–Lagarias–Pippenger, *The Computational Complexity of Knot and Link Problems*, introduction, attributes to Welsh the observation that JC would give a P^#P unknot-recognition algorithm. This is prior art for that conditional upper-bound observation, not a result about the exact JT2 fibre. [Author-hosted PDF](https://www.math.ucdavis.edu/~hass/Research/Papers/Complexity/hlp.pdf).
- Kuperberg, *How Hard Is It to Approximate the Jones Polynomial?*, Theory of Computing 11(6) (2015), Theorem 1.2, proves Cook–Turing #P-hardness for distinguishing two promised magnitude ranges at a principal non-lattice root, even for knots. It does not state a many-one hardness theorem for equality of the whole Laurent polynomial to the unlink polynomial. [Primary PDF](https://theoryofcomputing.org/articles/v011a006/v011a006.pdf).

The task “construct a JT2 hardness reduction” therefore still requires an exact symbolic gadget mechanism, a complete normalization and a proof that the final diagrams have exactly two components. Approximate synthesis is insufficient for exact zero preservation. The family must escape the fixed-jet tractability promise if the usual complexity separation is maintained, but a value-preserving count factorization is not obligatory. A first useful deliverable would specify the gate algebra and prove its exact zero-fibre simulation before any diagram search.

No new global hardness, detection, or novelty conclusion is asserted here.
