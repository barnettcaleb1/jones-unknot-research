# Order-three geometric identification: two decisive exclusions

16 November 2026. This is a bounded identification audit, not a search or a claimed classification of equivariant finite-type invariants.

## Verdict

There is not yet a proved geometric identification of the residual invariant

\[
\iota(K,h)=\frac{M_3(K,h)/36-7v_3(K)}5.
\]

Two proposed identifications can now be rejected exactly:

1. No fixed rational linear combination of the ordinary order-three Jones invariants of the covering knot and its two theta constituents equals \(M_3/36\) universally.
2. Neither \(M_3\) nor \(\iota\) is determined by the underlying knot together with the **entire Sakuma eta polynomial**. The obstruction persists after adding the invariant \(j\).

The second conclusion uses a published named pair with equal eta, not a regression against a list of low-order eta coefficients. It leaves open genuinely mixed equivariant invariants, combinations involving further inversion data, and a symbol identification followed by a separately proved lower-order correction.

## Conventions and certificate method

The ordinary Jones polynomials use the inverse-fourth-power bracket variable.
The quotient invariant here is \(J=J_{\mathrm{lp}}\), which uses \(t=A^{+4}\)
for its own quotient bracket. These are the mixed conventions in the saved
scripts and numerical tables. With those conventions,

\[
v_3(K)=-\frac{V_K'''(1)+3V_K''(1)}{36},\qquad
M_3=\sum_eJ_e(-1)^e e^3,\qquad
j=-\frac{J'(1)}8.
\]

The preferred invariant \(J\) is evaluated from the quotient bracket, while \(V_K\) is evaluated independently from the full symmetric covering diagram. Constituent polynomials come from the two actual constituent diagrams of the quotient theta graph. All calculations are exact Laurent-polynomial arithmetic. No numerical differentiation or fitted identity is used.

The scripts read the existing implementations `mont/lp.py`, `tools/kauffman.py`, and `mont/ft/core/c1_constituents.py` in Claude's lane. Their JSON outputs retain the full Laurent polynomials, so every derivative and moment below can be rechecked without running the diagram evaluator.

## 1. Covering and constituent order-three invariants do not suffice linearly

For the following four fixed published strong inversions, the values are:

| inversion | \(M_3/36\) | \(v_3(K)\) | \(v_3(C_{\rm in})\) | \(v_3(C_{\rm out})\) |
|---|---:|---:|---:|---:|
| \(3_1\) | 7 | 1 | -1 | 0 |
| first inversion of \(4_1\) | -5 | 0 | -5 | 0 |
| first inversion of \(5_2\) | 26 | 3 | -14 | 0 |
| second inversion of \(5_2\) | 16 | 3 | 3 | 0 |

The exact marked halfwords are respectively

```text
s.l1.y0.y0.y1.u2
s.l1.y0.y0.x1.u2
s.l1.y0.y0.y0.y0.y1.u2
s.r1.y0.y0.y1.y1.u2
```

Suppose \(M_3/36=a v_3(K)+b v_3(C_{\rm in})+c v_3(C_{\rm out})\) universally. The figure-eight example forces \(b=1\). The trefoil then forces \(a=8\). The first \(5_2\) inversion would give \(8\cdot3-14=10\), but its value is 26. Thus no choice of \(a,b,c\in\mathbb Q\) works. In particular the tentative formula with coefficients \((6,1,1)\) is false. Since \(\iota\) differs from \(M_3/36\) by a fixed covering-knot multiple, the same exclusion applies to a pure linear constituent/cover formula for \(\iota\).

For the first three diagrams, the constituent identification has a direct geometric calibration: doubling the axis crossings gives the indicated two-strand torus constituent (three, five, or seven crossings), and deleting them gives the other, unknotted constituent. This checks the chirality conventions used in the table. The ordinary Laurent polynomials of those nontrivial constituents are

\[
\begin{aligned}
&-t^{-4}+t^{-3}+t^{-1},\\
&-t^{-7}+t^{-6}-t^{-5}+t^{-4}+t^{-2},\\
&-t^{-10}+t^{-9}-t^{-8}+t^{-7}-t^{-6}+t^{-5}+t^{-3}.
\end{aligned}
\]

Certificate: `referee_checks/degree3_constituent_gate.py` and `.json`. This excludes only the stated linear formula. It does not exclude correction terms of order at most two, products of lower-order invariants, or other invariants of the inversion.

## 2. A complete Sakuma-eta obstruction to identification

Watson's *Khovanov homology and the symmetry group of a knot*, [arXiv:1311.1085v4](https://arxiv.org/abs/1311.1085v4), subsection **Distinguishing strong inversions**, explicitly discusses the two inversions of \(9_9\). The caption for the figure depicting this pair attributes to Sakuma the equality

\[
\eta(9_9,h_1)=\eta(9_9,h_2)=-2t^{-2}+4-2t^2.
\]

The following marked halfwords are the two inversions in the saved KWZ table:

```text
9_9^1: s.r1.y0.y0.y1.y0.y0.y1.y1.y0.y0.y1.u2
9_9^2: s.l1.y0.y0.y1.y0.y0.y0.y0.y1.y0.y0.y1.u2
```

Their full covering-knot Jones polynomials agree exactly, and direct differentiation gives \(v_3(9_9)=22\). Their preferred quotient calculations give

| inversion | \(M_3\) | \(M_3/36\) | \(j\) | \(\iota\) |
|---|---:|---:|---:|---:|
| \(9_9^1\) | 4824 | 134 | 2 | -4 |
| \(9_9^2\) | 6264 | 174 | 2 | 4 |

Consequently any proposed function

\[
M_3=F(K,\eta(K,h),j(K,h))
\]

fails on this pair, regardless of the complexity or nonlinearity of \(F\). The same is true with \(\iota\) in place of \(M_3\). In particular no choice of eta coefficient, derivative, collection of moments, or nonlinear operation on the complete eta polynomial repairs an identification that uses only these inputs.

Certificate: `referee_checks/degree3_eta_gate.py` and `.json`. Source checkpoint: the saved primary TeX is `/Users/calebbarnett/jones-lanes/theory-restart/lit/kwz-inversions/src/watson/involutions.tex`, lines 941–951; the eta equality is at line 945. We use Watson's explicit report of Sakuma's calculation; we have not independently recomputed the equivariant linking polynomial.

**Notation warning.** Some local KWZ metadata and scripts call a bracket-defect character `eta`. That object is not Sakuma's equivariant linking polynomial. Equality or disagreement of that character cannot be substituted for the source equality above.

## 3. What is still needed after a principal-symbol match

If a proposed geometric invariant \(I\) has the same order-three symbol as \(M_3\), their difference has order at most two (with respect to exactly the allowed equivariant moves). This implication alone does not identify the difference. No classification of the relevant equivariant order-at-most-two space has been supplied in this audit. An ordinary knot finite-type classification cannot silently be substituted: an on-axis move is a full twist versus its inverse, and the quotient has a marked axis and vertex data.

There is a precise bounded way to check a residual on any fixed move cube. Let \(R=M_3-I\), and let \(S\subset\{1,\ldots,m\}\) specify the changed sites of one diagram. If \(R\) is known to have order at most two, Boolean interpolation gives

\[
R(S)=R(\varnothing)+\sum_{i\in S}[R(\{i\})-R(\varnothing)]
+\sum_{\{i,j\}\subset S}[R(\{i,j\})-R(\{i\})-R(\{j\})+R(\varnothing)].
\]

Thus the base value, all first differences, and all second differences determine the residual on that cube. A global identity still requires a proved normal form or spanning result for the marked singular configurations and their degree-zero sectors. Checking an arbitrary sample of knots, even after a symbol calculation, does not provide that missing theorem.

The banked exact identity

\[
M_3=36\bigl(2H'(-1)-7a_2(K)\bigr),\qquad
H=\frac{J-1}{(t^4-1)(t^3+1)},
\]

already includes the preferred-framing correction and lower-order terms. It is a useful calibration, but \(H\) is defined from \(J\), so this is not an independent geometric identification. The principal-symbol comparison should therefore be retained as a symbol result until its own lower-order residual is determined.

## 4. Deliverable status

The fixed tests eliminate two natural identification routes and exhibit order-three inversion information not contained in the cover and Sakuma eta. They do not establish a new universal formula for \(\iota\), prove its observed integrality, or settle the modulo-five congruence. Those statements remain separate tasks.


## Later completion in this turn

The complete annular covering comparison is now written in `degree3_cyclotomic_comparison.md` and recorded TRUSTED pending Claude's read in reply20261116-221023-codex. Its final internal audits include `degree3_cyclotomic_referee.md`, `degree3_annular_closure_audit.md` and `degree3_coefficient_framing_audit.md`. It supplies the full preferred Phi10 congruence and hence the modulo-five third-moment identity, including the lower-order residual. Earlier pending statements in this report describe the intermediate stage. The independent geometric identification of iota remains open, and the exact exclusions in this report, where present, stand.
