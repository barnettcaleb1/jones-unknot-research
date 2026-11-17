# Genus-one refinement of the rank-five residual

16 November 2026. Referee audit of Claude's 235059, item 2. No diagram search or knot enumeration was performed. This report leaves the board and the bridge to the parent task.

## Verdict

The proposed genus-one exclusion is valid, with a coefficient-field argument that must be stated. The correct classification source is Baldwin–Sivek's **Floer homology and non-fibered knot detection**, not its sequel **Characterizing slopes for 5₂**.

There is a stronger useful consequence:

> If a knot K in S³ has genus one and Δ_K=1, then
> \[
> \dim_{\mathbb Q}\widehat{HFK}(K,1;\mathbb Q)\ge4,
> \qquad \operatorname{rk}_{\mathbb F_2}\widehat{HFK}(K;\mathbb F_2)\ge9.
> \]

Consequently a flat nonrational quotient tangle whose covering knot has genus one satisfies **dim N(T)≥9**, or **m(T)≥4** when dim N=1+2m. In particular the banked rank-five residual necessarily has **g≥2**. This does not prove a universal bound dim N≥7: the higher-genus rank-five residual remains open.

## 1. Exact classification and computation input

John A. Baldwin and Steven Sivek, *Floer homology and non-fibered knot detection*, Forum of Mathematics, Pi **13** (2025), e1, 65 pp., DOI [10.1017/fmp.2024.28](https://doi.org/10.1017/fmp.2024.28), [arXiv:2208.03307v2](https://arxiv.org/pdf/2208.03307) (9 October 2024). The journal text is [freely available](https://www.cambridge.org/core/journals/forum-of-mathematics-pi/article/floer-homology-and-nonfibered-knot-detection/3CE30C71E8F2454815BAB16E0BF75FF9).

Their coefficient field is **Q** (§1.1). Definition 1.1 calls a knot nearly fibered when its top Alexander-graded hat knot Floer group has dimension two. Theorem 1.2 classifies the genus-one case, up to mirrors, by the five rows below. Table 1 gives the groups; Appendix A supplies the computations. In the table, \(\mathbb Q^r_d\) means rank r in Maslov grading d.

| Knot | HFK at A=1 | HFK at A=0 | HFK at A=−1 | Total Q-rank | Δ(t), normalized by Δ(1)=1 |
|---|---|---|---|---:|---|
| 5₂ | Q²₂ | Q³₁ | Q²₀ | 7 | 2t−3+2t⁻¹ |
| 15n43522 | Q²₀ | Q⁴₋₁ ⊕ Q₀ | Q²₋₂ | 9 | 2t−3+2t⁻¹ |
| Wh⁻(T₂,₃,2) | Q²₀ | Q⁴₋₁ ⊕ Q₀ | Q²₋₂ | 9 | 2t−3+2t⁻¹ |
| P(−3,3,2n+1), n∈Z | Q²₁ | Q⁵₀ | Q²₋₁ | 9 | −2t+5−2t⁻¹ |
| Wh⁺(T₂,₃,2) | Q²₋₁ | Q⁴₋₂ ⊕ Q₀ | Q²₋₃ | 9 | −2t+5−2t⁻¹ |

Here Wh± denotes the two-twisted Whitehead double of the right-handed trefoil, with either clasp sign. Both clasp signs occur in the classification. The Alexander column is the Maslov-graded Euler characteristic of the displayed groups. Thus the first three rows have determinant 7, the last two determinant 9. Mirrors have the same normalized Alexander polynomials. No listed knot has Δ=1.

Theorem 1.2 is a classification by **genus and top-group rank**, not by total rank. It therefore does not revive the incorrect general rank-five classification discussed in `low_rank_hfk_referee.md`.

## 2. The coefficient-field bridge

For each Alexander grading a, the associated graded hat knot Floer chain complex can be chosen as a finite free abelian chain complex. Universal coefficients therefore give

\[
\dim_{\mathbb Q}\widehat{HFK}(K,a;\mathbb Q)
\le
\dim_{\mathbb F_2}\widehat{HFK}(K,a;\mathbb F_2).
\]

Explicitly, the Q dimension is the sum of free ranks of the integral homology groups at that Alexander grading. Passing to F₂ retains these free ranks and may add contributions from integral 2-primary torsion and the adjacent universal-coefficient Tor terms. It cannot decrease the dimension. No torsion-freeness claim is needed.

The rational top Alexander group is nonzero by genus detection, cited in the classification paper as equation (1.1). Its Euler characteristic is the corresponding Alexander coefficient. These facts ensure that one does not apply a Q-coefficient classification merely because a group over F₂ has dimension two.

## 3. Proof of the stronger genus-one bound

Suppose g(K)=1 and Δ_K(t)=1. Put

\[
d_+=\dim_{\mathbb Q}\widehat{HFK}(K,1;\mathbb Q).
\]

Genus detection says d₊>0. The coefficient of t in Δ is zero, so the even- and odd-Maslov parts of this group have equal dimension. Hence d₊ is a positive even integer.

If d₊=2, K meets precisely the hypotheses of Baldwin–Sivek Theorem 1.2. The complete list in §1 has determinant 7 or 9, contradicting Δ=1. Thus d₊≥4.

Conjugation symmetry gives dimension at least four at Alexander grading −1. The coefficient of t⁰ in Δ is one, so the central group has dimension at least one. Genus detection leaves no Alexander grading outside {−1,0,1}. Therefore

\[
\operatorname{rk}_{\mathbb Q}\widehat{HFK}(K)\ge4+1+4=9.
\]

Universal coefficients now give the same lower bound over F₂. This proves the displayed proposition without any hypothesis on τ, fiberedness, a strong inversion, or a tangle invariant.

## 4. Consequences for the held tangle problem

Use the already audited input TH-S over F₂:

\[
\dim N(T)\ge\operatorname{rk}_{\mathbb F_2}\widehat{HFK}(\kappa).
\]

Use also the banked flatness consequence a₂(κ)=0. If g(κ)=1, write

\[
\Delta_\kappa(t)=a_0+a_1(t+t^{-1}),\qquad a_0+2a_1=1.
\]

Since a₂(κ)=Δ″(1)/2=a₁, flatness implies a₁=0 and Δκ=1. Section 3 therefore gives dim N≥9, equivalently m≥4.

In particular, in the previously isolated equality case dim N=5, the known rank-five/Alexander-one profile cannot have genus one. Its safe updated description is

\[
g(\kappa)\ge2,\quad
\Delta_\kappa=1,\quad
\operatorname{rk}_{\mathbb F_2}\widehat{HFK}(\kappa)=5,
\]
\[
\operatorname{rk}\widehat{HFK}(\kappa,a)
=\begin{cases}2&a=\pm g,\\1&a=0,\\0&\text{otherwise},\end{cases}
\qquad |\tau(\kappa)|=g.
\]

The last rank profile and τ statement are imported from `low_rank_hfk_referee.md`, not re-proved here. This report adds only g≥2 and the independent genus-one bound dim N≥9. It establishes neither that the higher-genus profile is realizable nor that it is impossible.

## 5. Scope and disposition

**Accepted with a strengthening:** Claude's suggested genus-one source check does yield g≥2 for the rank-five residual. It also rules out every genus-one flat covering knot with dim N=5 or 7. This is a genuine restricted reduction using actual knot topology and a complete classification, independent of the formal ladder objects.

**Not asserted:** a classification of all rank-five knots; a universal m≥3 bound; any conclusion from the instanton nearly fibered classification; or an identification between F₂ and Q knot Floer groups beyond the dimension inequality. The relevant genus-one knot Floer theorem suffices on its own.

**Bounded next-to-top follow-up (16 November).** The g≥2 rank-five residual has HFK(g−1)=0, so its realization would contradict next-to-top nonvanishing, but neither checked theorem excludes it. [Ni, *The next-to-top term in knot Floer homology*, Quantum Topol. 13 (2022), 579–591, Theorem 1.1](https://www.its.caltech.edu/~yini/Published/SecondTerm.pdf) requires the top group to occupy a single Maslov parity; the paper uses Q in its proof (§3), while our residual's rational top group has dimension exactly two and Euler characteristic zero, hence occupies both parities. [Binns–Wan, arXiv:2608.03900v1, Theorem 1.3](https://arxiv.org/html/2608.03900v1) works over F₂ and requires a *w-avoiding exterior*: Definition 1.6 asks for a minimal Seifert-surface exterior decomposing along exactly two product annuli into a product and the sutured exterior of a w-avoiding knot. Their example 2.1 cites Li–Ye for 5₂, not for all nearly fibered knots. In fact [Li–Ye, *The guts of nearly fibered knots*, AGT 26 (2026), 1385–1393, Theorem 1.4, Corollary 1.5 and Remark 2.1](https://arxiv.org/pdf/2208.05382) sharpen our residual: its rational top rank is two, and its vanishing top Alexander coefficient forces model M1, a solid torus with **four longitudinal sutures**; models M2/M3 have top Euler characteristic ±2. Their product-gluing description attaches along all four sutures, so it does not establish Binns–Wan's two-annulus hypothesis. Binns–Wan Remark 4.13 expressly leaves general annulus/disk decompositions outside the proof. Thus “guts M1” is an additional necessary condition, while a theorem placing this four-suture case in their hypothesis would be new input, not a consequence already supplied by these sources.
