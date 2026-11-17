# C2 scope referee: mirror frequencies, resonance, and certification

Date: 17 November 2026. Source: `collab/data/engineC2/REPORT.md`, especially Sections 2, 5–9, 11–12. Bounded independent mathematical read; no computations, scans, or review of V3. This note audits deductions and scope; it does not independently certify the geometric models or their matrix entries.

## Verdict

The Hermitian frequency mechanism in M2 is sound for the listed local twist spectra, with two essential qualifications: combine equal frequencies before testing nonvanishing, and retain the constant-unit branch. Its version for arbitrary signed monomial spectra must be stated separately on the two parity classes. The S1 finite-frequency fit can be promoted to an identity by interpolation once the marked spectral decomposition proves its frequency support.

Two stronger conclusions in the report are unsupported: a monomial channel ratio does not prove that a box is topologically local, and a unit sister invariant together with an unknotted constituent does not certify a trivial theta-curve. The finite-order hypothesis and the distinction between a universal mirror identity and a symmetry of a particular input must also be preserved.

## 1. M2 with grouped frequencies

Assume one fixed marked gluing form satisfies `bar(G)^T = G`, and that the repeated local operator is semisimple over the rational-function field with eigenvalues

\[
\lambda_i=\epsilon_i t^{e_i},\qquad \epsilon_i\in\{1,-1\}.
\]

For its spectral components, set

\[
C_{ij}=v_i^TG\bar v_j,
\qquad C_{ji}=\overline{C_{ij}}.
\]

The stated expansion is then exact:

\[
F_k=\sum_{i,j} C_{ij}(\epsilon_i\epsilon_j)^k
t^{(e_i-e_j)k}.
\]

Define the *aggregate* coefficient

\[
A_{d,\epsilon}=\sum_{e_i-e_j=d,\ \epsilon_i\epsilon_j=\epsilon}C_{ij}.
\]

It satisfies `A_{-d,epsilon} = bar(A_{d,epsilon})`. For a fixed parity `a in {0,1}`, write `k=a+2r` and put

\[
B_d^{(a)}=t^{ad}\sum_{\epsilon=\pm1}\epsilon^a A_{d,\epsilon}.
\]

Then

\[
F_{a+2r}=\sum_d B_d^{(a)}t^{2dr},
\qquad B_{-d}^{(a)}=\overline{B_d^{(a)}}.
\]

After clearing one common denominator, distinct translated supports separate when `|r|` is sufficiently large. Consequently, on each parity class:

* If all coefficients with `d != 0` vanish, the family is constant on that parity class.
* Otherwise let `d_max > 0` be the largest surviving difference. The maximal degree grows as `2 d_max |r| + O(1)` in both directions. By reciprocity the minimal degree decreases correspondingly. Unit values occur in a finite window on this parity class.

This proves the corrected statement. The maximum rate must be taken over surviving aggregate coefficients, not individual nonzero `C_ij`. Without parity separation, opposite signs at one exponent difference can cancel on just one parity, while signed zero-rate terms can make a bounded family periodic instead of constant.

For the spectra actually listed in M2, `1,-t,t^3`, `1,t^-3`, and the two-channel nested-box operator up to a common scalar, the nonzero exponent differences are unique. Their diagonal terms have positive sign. Thus the simpler constant-or-growth conclusion follows for these local sites; the general qualification does not invalidate those cases.

### The constant-unit branch

The report's consequence (iii), “units only in an explicit finite window”, needs the hypothesis that a nonconstant aggregate survives. If the family is identically a unit, it has infinitely many unit parameters. Section 7 itself reports an identically unit example. Such branches require a separate geometric certification; the frequency argument does not identify their topology.

### Preferred normalization

The expansion must use one marked framing throughout. If the Hermitian evaluation `F_k` and the preferred invariant `J_k` are both reciprocal, and `J_k=epsilon_k t^{n_k} F_k` with `F_k != 0`, reciprocity forces `n_k=0`. A sign can remain and cannot affect span. This is a way to justify the passage to preferred normalization; independent arbitrary monomial recentring at each parameter is not a substitute. If only raw reciprocity is established, the invariant conclusion that survives an arbitrary monomial factor is the span-growth statement.

## 2. Exact finite interpolation can repair the S1 fit

Sections 8–9 currently describe the frequency identity as checked and Theorem F as proved modulo that fit. There is a clean certificate once the marked gluing and local spectral decomposition have been established.

For even `m=2r`, the allowed frequencies from the local spectrum `1,-t,t^3` are exactly a subset of

\[
t^{2fr},\qquad -3\le f\le3.
\]

Over `Q(t)` these seven bases are distinct. Therefore seven exact consecutive values of each matrix entry, in the same framing, uniquely determine its seven coefficients by an invertible Vandermonde matrix. If the proposed coefficients match those values and the seven-frequency support is already proved, the formula holds for every integer `r`, positive and negative. Extra fitted values are then validation rather than the missing theorem.

This observation does not itself verify the reported coefficients, the geometric marking, the Newton polygon, or its edge equations. It says precisely how a finite exact certificate becomes an all-parameter proof, without further enumeration.

## 3. A monomial channel ratio is not a locality theorem

Section 11 makes the inference

\[
b=\pm t^j a
\quad\Longrightarrow\quad
\text{trivial box or a local knot tied into the arc}.
\]

The left side is a statement about two skein channel amplitudes. It says that, after a suitable integral twist when permitted, the box acts by a scalar in this two-channel representation. It does not identify the embedded box. Distinct tangles can have the same skein vector; establishing that this particular scalar fibre consists only of local constructions is an additional realization or detection theorem. No such theorem is proved in C2.

The root constraints can narrow the algebraic exception but do not supply topology. In the preferred integral normalization with `a(1)=1`, `a(omega)` cannot vanish at a primitive cube root: otherwise `Phi_3` divides `a` in the Laurent polynomial ring, and evaluation at 1 would give `3 | a(1)`. Thus `a=b mod (1-t^3)` really gives `q(omega)=1`, rather than an undefined `0/0`. If `q=epsilon t^j`, this implies `epsilon=1` and `3 | j`. A suitable `Y` shift then makes the two amplitudes equal. The result is still only a scalar skein state.

Accordingly, the rectangular resonances in Section 11 cannot be removed by the equivariant-primality condition N3 without a geometric certificate or a separately proved scalar-fibre theorem. The uniform finite-window conclusion for those cases remains open under the supplied argument. This is an identified proof gap, not an exhibited counterexample to the desired conclusion.

## 4. Unit sister invariants are not unknot certificates

Sections 5–6 and 12 call the unit survivors presumed trivial after checking an unknotted constituent and a unit sister invariant. The parenthetical claim that a nontrivial Brunnian theta-curve would necessarily have a nonunit sister is a detection statement, not a consequence of those calculations.

These tests provide additional necessary invariant conditions. They do not certify that the theta-curve is trivial, that its covering knot is the unknot, or that it is an excluded equivariant sum. Until a topological certificate is supplied, the entries should be recorded as **unit-invariant survivors with triviality unresolved**, and the region should not be called certified empty. The same correction applies to the bounded periodic examples described as “certified-trivial” if their only certification is this test.

## 5. Geometry: preserve hypotheses and avoid a universal-to-pointwise inference

Section 2 explicitly assumes a **finite-order** orientation-reversing symmetry preserving the marked arc. Its summary should retain that hypothesis. A mirror equivalence or orientation-reversing self-homeomorphism of an arbitrary marked theta-curve does not, merely by its definition, provide the finite-order representative needed for the interval and fixed-set arguments. This referee note does not verify a realization theorem extending that hypothesis to every nonhyperbolic or satellite case.

There is also a separate logical gap in Section 2(b). Nonproportional closure covectors prove that two closure rules are not universally identical for arbitrary input states. They do not rule out equal evaluations on a particular input, and a fortiori do not rule out an accidental geometric symmetry of that particular marked box configuration. Thus the nonproportionality argument alone cannot establish that every standard necklace with nonzero special twist, or every vertical odd closure, is non-amphicheiral. A geometric proof for the specified grammar would be needed for that stronger assertion.

The explicitly symmetric construction and its Hermitian gluing identity do not depend on that overclaim: they remain valid subjects of M2 under their stated marked-model assumptions.

## Recommended status corrections

* **M2:** retain as a conditional marked spectral theorem, with aggregate coefficients, parity where needed, and a separate constant-unit branch.
* **F (S1):** the finite-frequency support plus a seven-value exact certificate can remove the “checked fit” qualification; this note has not executed that certificate.
* **F′ rectangular cases:** retain the scalar-channel resonance as an open residual case, not an N3 exclusion.
* **S2/E4 unit survivors:** topological triviality unresolved unless certified by additional methods.
* **Geometry P2:** preserve the finite-order hypothesis and remove the inference from nonproportional universal closure rules to absence of symmetry on every individual input.
