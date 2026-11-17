# Moment hierarchy: precise scope and logical corrections

This is an algebraic audit of Claude's 20261103-045944 proposal, using the saved anchored formula and existing records only. No new geometry or braid scan was performed. It does not assert a nonvanishing theorem.

## 1. Inner moments and matching moments are different objects

For a fixed matching and parked incidence, retain the actual anchored inner polynomial

\[
S_{m,y}(q,u)=\sum_x\tau_x q^{A_x}u^{W_m(x;y)},\qquad
\mu_{k,m,y}=\partial_u^k S_{m,y}(q,1).
\]

Let \(p_m=b_m\bmod 2\), \(\kappa_m=(b_m-p_m)/2\), and \(c_{m,y}=\kappa_m+w_{0,m}(y)\). The parity aggregate, after extracting \(t^{p_m}\), is

\[
F_m(q,u)=r_mq^{a_m}\sum_y\tau_yq^{A_y}u^{c_{m,y}}S_{m,y}(q,u).
\]

Consequently

\[
F_m^{(k)}(q,1)=r_mq^{a_m}\sum_y\tau_yq^{A_y}
\sum_{j=0}^{k}{k\choose j}(c_{m,y})_{k-j}\mu_{j,m,y}(q).
\]

The anchor factors mix moments by Leibniz's rule, and the outer sum can cancel across parked positions. Therefore Bigelow's aggregate order two and Long–Paton's aggregate order one do **not** give the lowest nonzero index of each inner sum. Even when every inner \(\mu_0\) vanishes, an aggregate order-two zero can arise from cancellation of nonzero first inner moments. An identically zero matching aggregate likewise does not force all its inners to vanish.

The archived kernel computations establish their stated aggregate orders exactly. They do not contain completed per-position kernel geometry; aggregate information must not be labeled per-position measurements.

## 2. Equal q-degree is equal total winding only

Here \(A_x=\sum_{p=1}^{6}\operatorname{wind}_p(L_x)\). Equality of two values of \(A_x\) says only that these sums agree, not that the six winding numbers agree separately. For example, the integer vectors \((1,0,\ldots)\) and \((0,1,0,\ldots)\) have the same sum. Thus “two points of a cancelling family wind equally around every real puncture” does not follow from equal q-exponents. Unequal coloring can distinguish information already lost by summing the real-puncture windings.

## 3. Polynomial order is invariant under a unit; record sign coherence is not

For a change of local-system lift \(S'=\epsilon q^r u^c S\),

\[
\mu'_k=\epsilon q^r\sum_{j=0}^{k}{k\choose j}(c)_{k-j}\mu_j.
\]

If \(k\) is the first nonzero moment index, then \(\mu'_k=\epsilon q^r\mu_k\). Hence the order and first nonzero polynomial, up to the displayed unit, are unchanged. But individual contributions have weights \(\tau_x(W_x+c)_k\), so their signs and counts need not be unchanged.

The algebraic example \(S=u-1\) has \(\mu_0=0,\mu_1=1\), represented by one positive nonzero first-moment contribution. Multiplying by \(u\) gives \(u^2-u\), with the same first moment represented by \(+2-1\). More generally, when \(k>0\) is first, \(\mu_0=0\) makes the raw signs balance at every q-degree. A sufficiently positive shift makes every falling-factorial weight positive, exposing mixed signs at any contributing degree.

This is a warning about a proposed invariant, not a geometric counterexample to the conjecture. The existing definition uses closed loops based at chosen reference incidences and thus fixes a convention; arbitrary lift shifts need not preserve that convention. Conjecture M must explicitly fix those anchors or provide a sign criterion invariant under their permitted changes. Moments of individual parked sums are not automatically cap-slide-invariant tangle invariants.

If “single-sign extremal q-term” means the coefficient **after all equal-degree records have been aggregated**, the assertion is tautological: any nonzero Laurent polynomial has one nonzero coefficient at its highest degree. The nontrivial version concerns the signs of all nonzero-weight records contributing to that degree. For \(k>0\) these are signs of \(\tau_x(W_x)_k\), not merely \(\tau_x\); zero weights must be excluded. Record counts are also not coefficient magnitudes.

## 4. Taylor expansion is formal; finite support provides the exact substitute

For negative winding, \(u^W\) has an infinite Taylor series at \(u=1\). The displayed moment expansion is valid in \(\mathbb Q[q^{\pm1}][[u-1]]\), but this does not authorize substituting \(u=q^{-2}\) into that infinite series without a specified completion or convergence argument. Evaluate the finite Laurent polynomial \(S\) directly instead.

If its distinct winding support is \(W_1,\ldots,W_d\), the first \(d\) moments determine all aggregated coefficient polynomials: the matrix \(((W_i)_k)_{0\leq k<d,1\leq i\leq d}\) has the nonzero Vandermonde determinant. Thus a nonzero \(S\) has order at most \(d-1\) at \(u=1\). Three vanishing moments alone prove \(S=0\) only when the known support has at most three distinct winding values, or when the full coefficient table independently proves it. The full witness's saved winding support lies in \(\{-1,0,1\}\), so that bound applies there.

## 5. What the proposed tests can and cannot establish

Conjecture M is existential in the matching and parked position and assumes a slide-reduced nonsplit representative. P1, phrased for all “surviving parked positions” of a control, is stronger. A P1 failure at one position does not refute the existential claim; failure at every position in an unminimized representative still does not refute its slide-reduced version. “Surviving” should be defined explicitly, for example \(S_{m,y}(q,q^{-2})\ne0\), rather than conflating inner survival with survival after the outer sum.

The completed full-witness summary has 1,585 parked positions and **no** vanishing zeroth inner moment. P2's antecedent is therefore never met in that saved representative: it passes vacuously and supplies no evidence about higher moments of Burau-zero inners. Every lowest moment there is already \(\mu_0\). For example, one extremal coefficient \(+1\) aggregates 93 positive and 92 negative records.

Finally, a nonzero first moment with a coherent extremum need not survive substitution \(u=q^{-2}\), and surviving inner specializations can still cancel in the outer sum. These are separate remaining gaps. The exact parked decomposition is a useful identity; the moment expansion alone does not close either gap.

## Sources within this workspace

- `work/width6_parked/formula_note.md`: exact anchored formula and its record-level verification.
- `work/width6_parked/kernel_note.md`: exact aggregate kernel orders and limits of available geometry.
- `work/width6_moments/tables_witness_full_summary.json`: completed full-witness counts cited above.
