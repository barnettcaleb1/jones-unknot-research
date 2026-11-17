# Characteristic-zero instanton audit

16 November 2026. Audit of item 4 of `20261115-235059-claude`.
Scope: the proposed characteristic-zero analogue of TH-S, its target and
its possible quantitative use. No enumeration or new experimental data.

## Verdict

There is a genuine characteristic-zero spectral sequence

\[
N_{\mathbb C}(\overline T)\Longrightarrow THI(T).
\]

Its target is the **singular instanton invariant of the original tangle**.
It is not the ordinary sutured instanton invariant of the double branched
cover, and the cited results do not give a sequence to `KHI(kappa)`.
In fact the doubled-trefoil calibration below disproves that identification
of targets. This does not disprove the existence of some additional,
different sequence to `KHI(kappa)`; it says that Xie's sequence is not one.

The sequence gives rank constraints and braid detection. Its stated grading
properties do not give END, NP, or a restriction on the two quantum endpoints.
Low-rank classifications for `KHI(kappa)` therefore cannot be applied to
this target.

## 1. Exact source ledger

The following statements use the numbering of [Xie, arXiv:1809.01568v2](https://arxiv.org/pdf/1809.01568).

| Location | Content used |
|---|---|
| Theorem 5.16 | For each annular grading `i`, `AKh(mirror L,i; C)` is `E2` of a sequence converging to `AHI(L,i)`.
| Equation (4.3), Theorem 6.1 (= introductory Corollary 1.2) | For a balanced admissible tangle with `m` top endpoints, `TKh(T)=AKh(hat T,m)` and `THI(T)=AHI(hat T,m)`; hence `TKh(mirror T; C) => THI(T)`.
| Definition 3.7 | Close `(I x D,T)` using two auxiliary product strands to obtain `(S1 x S2,hat T union K2,u)`; take the distinguished sphere eigenspace.
| Proposition 4.10; Corollary 4.11 | `THI(T)` has odd dimension precisely for vertical tangles; dimension one precisely for braids.
| Theorem 6.3, proof | For the `n`-parallel of a cut-open knot, `THI(T^n(K)) = I^natural(K; C)`.

The sequence preserves the integer **annular** grading. No endpoint-monotonicity
rule in the Khovanov quantum grading is asserted here. The ambient instanton
grading is mod four, descending to mod two on a sphere eigenspace.

The general terminology is [Xie--Zhang, arXiv:1907.00547v2](https://arxiv.org/pdf/1907.00547),
Definition 7.6 and Proposition 7.7: `SHI(M,gamma,T)` retains the singular
tangle in a sutured closure and is independent of closure choices.
Remark 7.8 recovers ordinary `SHI(M,gamma)` when `T` is empty.

## 2. Application to the bullet complex

Use the horizontal direction in which the `b` matching is the identity.
The cylinder has two endpoints on each end disk; its side annulus is the
sutured annulus, with core `gamma`. The quotient tangle is admissible and
balanced. Verticality is not needed for the spectral sequence itself.

The previously checked chain calculation in
[`annular_colored_referee.md`](annular_colored_referee.md), Section 1, works
over `C` as well: a `b` resolution produces two essential circles, and the
annular-weight-two summand labels both by `v_+`. A backtracking resolution
has no weight-two state. Dots on essential circles and saddles leaving
this matching disappear in the annular associated graded. Contractible
circles retain their ordinary two-dimensional label spaces.

Consequently the relevant group is the top weight of **ordinary unreduced
annular Khovanov homology**, not an independently reduced annular theory.
It is `N_C(T)` with the overall grading convention already fixed there:
in the unnormalized convention it is `q^2 N_C(T)`; in adjusted quantum
degree `j-k` that shift disappears. Apply this to the mirror to obtain
the displayed sequence. There is no extra two-dimensional factor.
The auxiliary strands are part of the target's closure construction,
not a tensor factor added to this top-weight summand.

Two different sutured constructions must remain separate:

\[
\begin{array}{ll}
\text{instanton here:}&(I\times D,\gamma,T),\quad\text{singular tangle retained};\\
\text{TH-S upstairs:}&(\Sigma_2(I\times D,T),\widetilde\gamma),\quad
\text{branched cover, no singular tangle}.
\end{array}
\]

For our marking the second manifold is `E(kappa)` with meridional sutures.
That fact identifies the Heegaard Floer target in TH-S. It does not turn
the first construction into the second one.

## 3. A concrete obstruction to identifying the targets

Let `K` be a trefoil, and take its zero-framed doubled tangle `T_K`.
This is `T^2(K)` in the parallel-tangle construction. Its branched cover
is `E(K#K)` by Lewark--Zibrowius, Definition 3.9 and Remark 3.10, as
checked in [`annular_colored_referee.md`](annular_colored_referee.md), Section 4.
Thus the knot called `kappa` is `K#K`.

The source ledger identifies the instanton target with `I^natural(K)`.
Using the one-parallel case of the same sequence, its dimension is at
most the reduced Khovanov rank of the trefoil, namely three:

\[
\dim THI(T_K)=\dim I^\natural(K;\mathbb C)\leq 3.
\]

By contrast, Kronheimer--Mrowka's Alexander categorification,
[Theorem 1.1, *Instanton Floer homology and the Alexander polynomial*](https://msp.org/agt/2010/10-3/agt-v10-n3-p16-s.pdf),
gives `dim KHI(J) >= ||Delta_J||_1` for every knot `J`. Here

\[
\Delta_{K\#K}(t)=(t-1+t^{-1})^2
=t^2-2t+3-2t^{-1}+t^{-2},
\qquad \|\Delta_{K\#K}\|_1=9.
\]

Therefore `THI(T_K)` and `KHI(kappa)` cannot be isomorphic. This argument
requires neither a connected-sum theorem for instanton homology nor a
classification of its rank-three or rank-five knots.

## 4. What can safely be banked

The surviving rank inequality is

\[
\dim_{\mathbb C}N_{\mathbb C}(\overline T)
\geq \dim_{\mathbb C}THI(T).
\]

For a vertical two-string tangle, the right side is odd. If the left side
is one, the target is one-dimensional and the tangle is a two-strand
braid, hence rational. A nonrational vertical tangle therefore has
`dim N_C >= 3`. This is a braid-detection bound, not a low-rank bound
for `KHI(kappa)`.

A characteristic-zero formulation still matters for distinguishing genuine
adjacent-degree classes from universal-coefficient copies. It does not
alone rule out the cancelling ladder: independent classes over `C` can
have zero graded Euler characteristic. To extract an endpoint restriction
one needs additional information about the actual instanton filtered
complex or its maps; total rank, braid detection and annular weight alone
provide none. In particular, do not replace the target by `KHI(kappa)`
and import an Alexander-polynomial-one or low-rank classification.

## Bibliographic data

* Yi Xie, *Instantons and annular Khovanov homology*, Advances in Mathematics
  **388** (2021), 107864; arXiv:1809.01568v2.
* Yi Xie and Boyu Zhang, *Instanton Floer homology for sutured manifolds with
  tangles*, Journal of the European Mathematical Society **27** (2025),
  333--394; numbered statements above checked in arXiv:1907.00547v2.
* Peter Kronheimer and Tomasz Mrowka, *Instanton Floer homology and the
  Alexander polynomial*, Algebraic & Geometric Topology **10** (2010),
  1715--1738; arXiv:0907.4639.
* Lukas Lewark and Claudius Zibrowius, *Rasmussen invariants of Whitehead
  doubles and other satellites*, Journal für die reine und angewandte
  Mathematik **816** (2024), 241--296; arXiv:2208.13612v2.
