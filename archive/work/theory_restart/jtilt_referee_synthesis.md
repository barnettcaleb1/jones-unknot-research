# J-TILT and the endpoint visibility reduction

15 November 2026. Codex referee synthesis, prepared at Caleb's request without contacting Claude. The original sum and maps reports are preserved unchanged. Their claims are superseded, where necessary, by the scoped conclusions below.

**Verdict.** J-TILT gives a genuine conditional reduction of Lemma Q, but the reports do not prove the required restriction on actual tangles. We can make the reduction both more general and weaker: use an intrinsic graded vector space, allow every special-curve length, and ask only that its two extreme quantum degrees survive the signed Euler count. The sum report supplies a theorem about this vector space and a reduction to compatible sum-indecomposable factors. The maps report shows why individual central-composite map equations do not prove the missing restriction.

This addresses Lemma Q, the actual-unknot-closure/strong-inversion problem. It does not reduce the full Jones unknot conjecture to this problem.

## 1. The intrinsic invariant and a rank theorem

Work over \(\mathbb F_2\), while taking dimensions and Euler characteristics in the integers. Fix a marked quotient tangle \(T\) with \(T(\infty)=U\), using its Seifert longitude. Let \(C(T)\) be the Bar-Natan complex over the two-object algebra. Write \(b\) for the crossingless matching which is the unit of horizontal sum, and \(c\) for the other matching.

There is an augmentation functor \(F_b\) sending \(b\) to \(\mathbb F_2\), \(c\) to zero, and every nonidentity algebra path to zero. Define
\[
N(T)=H(F_bC(T)).
\]
This is a homotopy invariant. In a reduced model its differential is zero, so it is precisely the bigraded vector space of \(b\)-generators. Its graded Euler characteristic is the selected bracket coordinate. With the actual cap framing,
\[
\chi_qN(T)=u(T)J(T),
\]
where \(u(T)\) is a signed monomial and \(J=1\) is the previously established flatness condition. No empirical formula for the grading shift in terms of \(k,j\) is required.

**Rank theorem.** If \(\widetilde{\mathrm{Kh}}(T)\) has \(m(T)\) special components, counted with multiplicity, then
\[
\dim N(T)=1+2m(T).
\tag{1}
\]
In particular, \(\dim N(T)=1\) if and only if \(T\) is rational.

Here is the proof, including the previously missing long-curve case. The unknot-cap structure theorem gives one rational component \(r_1(k)\), with integer \(k\), and special components at slope infinity. The rational component has two \(b\)-generators. In the explicit normal form for a special \(s_\ell(\infty)\), there are four \(b\)-generators, independently of its length; the additional generators of longer components lie in the other idempotent. Actual Khovanov components have the specified rank-one local systems. Applying \(F_b\) to the \(H\)-cone doubles \(\dim N(T)\), because \(F_b(H)=0\). Thus
\[
2\dim N(T)=2+4m(T).
\]
If \(m=0\), the published rational-tangle detection theorem applies. Conversely a rational tangle has no specials. In the preferred Seifert framing the rational tangle in this locus is \(Q_0\).

The sources are the proof of Theorem 1.2 in [Kotelskiy–Lidman–Moore–Watson–Zibrowius](https://arxiv.org/abs/2109.14049), and Definition 3.12, Theorems 3.17 and 3.19 in [Kotelskiy–Watson–Zibrowius](https://arxiv.org/abs/2602.23442). The local primary texts were inspected. The formula (1) was independently checked in two referee reads.

This count concerns generators in one idempotent, **not** the dimension of pairing a special with a filling arc. The latter grows with length. Expanding a long special into short blocks for a pairing calculation does not decompose its contribution to \(N(T)\) into that many short pairs.

## 2. The weaker sufficient condition

For a finite bigraded vector space \(N\), put
\[
q_-=\min\{q:N^{*,q}\ne0\},\qquad
q_+=\max\{q:N^{*,q}\ne0\}.
\]
Call its endpoints visible, or **END**, when both integers
\[
e_\pm(N)=\sum_h(-1)^h\dim N^{h,q_\pm}
\]
are nonzero. The implications are
\[
\text{J-TILT}\ \Longrightarrow\
\text{pure parity at both endpoints (EXT)}\
\Longrightarrow\ \text{END}.
\tag{2}
\]
For J-TILT, strict decrease of the quantum extrema along the diagonal levels places each global quantum extreme on one level, hence in one homological degree. The consecutiveness requirement in J-TILT is unnecessary for this particular implication.

**Endpoint reduction.** If every nonrational actual tangle with an unknot cap satisfies END for \(N(T)\), then Lemma Q holds.

To prove this, a special of length \(\ell\) has four \(b\)-generator quantum degrees
\[
c-\ell-1,\ c-\ell+1,\ c+\ell-1,\ c+\ell+1.
\]
Thus the unsigned quantum breadth of the augmented Khovanov complex is at least \(2\ell+2\). The \(H\)-cone makes its unsigned character \((q+q^{-1})\) times that of \(N(T)\), after forgetting homological degrees. Positivity of unsigned multiplicities gives
\[
\operatorname{breadth}N(T)\ge 2\max_i\ell_i>0
\quad\text{if }T\text{ is nonrational}.
\tag{3}
\]
Under END both endpoints survive in \(\chi_qN(T)\). That polynomial has positive breadth, so cannot be the monomial required by \(J=1\).

A conservative proof using EXT needs only (1), without the length-dependent quantum formula: a monomial Euler characteristic and EXT force a single quantum degree, all generators have one sign, and a unit coefficient forces rank one. Rationality follows from (1).

END is strictly weaker than pure endpoint parity: two even generators and one odd generator can have a nonzero endpoint coefficient. It is also stronger than the desired conclusion. A non-flat tangle could have cancellation at an outer endpoint while retaining a nonconstant interior polynomial. Consequently END is a falsifiable geography conjecture, not an equivalence obtained by renaming Lemma Q.

## 3. What the sum theorem proves

The sum report's Theorem A survives:
\[
N(T_1+T_2)\cong N(T_1)\otimes_{\mathbb F_2}N(T_2).
\tag{4}
\]
Before reduction, only a pair \((b,b)\) produces \(b\); delooping affects only \(c\)-terms. On \(b\)-pairs, the augmented differential is the ordinary tensor differential. Künneth gives (4), and subsequent cancellation cannot change augmented homology. This is a consequence of the planar functoriality in [Bar-Natan, Theorem 2](https://arxiv.org/html/math/0410495v2) and the two-object category in [KWZ, Definition 4.19 and Theorem 4.21](https://arxiv.org/abs/1910.14584v2).

Three consequences are unconditional within this compatible sum operation:

1. The grading multiset is a Minkowski sum. J-TILT is preserved.
2. END holds for a product if and only if it holds for both factors: the two endpoint Euler coefficients multiply as integers. The same factor equivalence holds for EXT.
3. Combining (1) and (4) gives
   \[
   1+2m(T_1+T_2)=(1+2m(T_1))(1+2m(T_2)).
   \tag{5}
   \]
   This component-count formula needs no short-special hypothesis. If \(1+2m(T)\) is prime, \(T\) cannot decompose into two nonrational compatible factors.

The last statement is an obstruction to a specified equivariant decomposition, not a test of whether the underlying knot is prime. Inversions which exchange summands are not covered by the sum rule.

There is also a quantitative formulation. Write \(\chi=\chi_qN\ne0\), and define
\[
\lambda_+(N)=q_+-\max\operatorname{supp}\chi,\qquad
\lambda_-(N)=\min\operatorname{supp}\chi-q_-.
\]
These nonnegative endpoint losses add under (4). END is exactly \(\lambda_+=\lambda_-=0\). A hypothetical flat nonrational tangle would satisfy
\[
\lambda_++\lambda_-=\operatorname{breadth}N(T)>0.
\]
This measures the cancellation that must be ruled out; it does not rule it out.

Thus the sufficient conjecture can be restricted to factors admitting no nontrivial compatible equivariant sum. The composite examples cease to be independent evidence once (4) is proved. No claim is made that every quotient tangle admits a useful such decomposition.

## 4. What the maps report actually rules out

The three explicit null-homotopies on the displayed twelve-generator short special \(S\) were independently reimplemented and checked:
\[
dK_b+K_bd=D_b\,\mathrm{id},\quad
dK_c+K_cd=D_c\,\mathrm{id},\quad
dK_s+K_sd=S^2\,\mathrm{id}.
\]
Hence every central augmentation element acts null-homotopically on \(S\). It follows that a homogeneous pair of maps with prescribed central composites can be extended by zero when shifted copies of \(S\) are added to its source and target.

The formal object
\[
B=a(0)\oplus S\oplus hS
\]
therefore satisfies these individual central-composite existence conditions while retaining the unknot-cap Euler data and failing endpoint visibility. It is not an actual tangle. This proves that those equations alone cannot establish END or J-TILT.

It does **not** prove that every geometric replacement map is zero there, that compatible systems of maps and homotopies contain no further information, that arbitrary deletion of summands preserves the constraints, or that integral refinements are powerless.

The independently verified noncentral morphism window also permits an equal-quantum pair on adjacent levels. It supplies neither a forced connecting map nor the strict negative shift required by J-TILT. Moreover, the saved invariant of \(b(35,26)\)'s specified inversion contains such a pair, alongside additional components. A rule forbidding the pair locally is contradicted by the very archive supporting the geography conjecture. A useful restriction must concern the whole support or additional geometric structure.

The maps report's all-twist closure-range formulas and finer orientation dictionary are not fully proved as written; their finite checks do not supply the omitted uniform arguments. They are unnecessary for the scoped conclusion above. The field-valued map-invariant interpretation was checked against [Lewark–Marino–Zibrowius, Proposition 5.20](https://arxiv.org/abs/2409.05743v2).

## 5. Corrections and scope decisions

| Claim | Referee disposition |
|---|---|
| Augmented invariant is monoidal | Verified, including reduction and delooping. |
| J-TILT implies Lemma Q universally | Verified as a conditional implication; long curves handled by intrinsic \(N(T)\). |
| Every actual unknot-cap tangle satisfies J-TILT | OPEN; the reports provide data, not a proof. |
| Component-number sum formula requires short specials | Restriction removed by (1). |
| Detailed graded short-special tensor formula | Separate calculation remains; not used in this reduction. |
| \(J=1\) alone fixes a singleton's homological degree to zero | Incorrect algebraic inference; it fixes even parity. Use rationality and cap normalization afterwards. |
| Failure of EXT in \(B\otimes T\) proves failure of old special-only TILT | Unsupported; it proves failure of EXT and J-TILT. |
| Central map identities exclude every possible map-level mechanism | Unsupported; only individual central-composite existence constraints are covered. |
| A surviving extreme coefficient by itself excludes the unknot | Requires a nonzero normalized degree, or two distinct surviving degrees. END plus (3) supplies the latter. |

## 6. Research decision

Retain the intrinsic invariant, its monoidality, the universal rank count and the endpoint reduction. Keep J-TILT OPEN as a stronger possible mechanism. The economical target is END for actual nonrational quotient tangles indecomposable under the compatible sum.

This is real progress in stating the problem: it removes the all-short-special assumption, virtual-string bookkeeping, empirical absolute-centering formula and OVERHANG from the deduction, and proves exact decomposition restrictions. It is not yet progress past the central realizability obstruction. Neither report provides a theorem explaining why an actual sum-indecomposable tangle cannot realize the extreme cancellation of \(B\).

The next proof input would have to use actual tangle geometry that the formal direct-sum object does not retain—for example, a specified system of cube/cobordism maps and its compatibility, rather than the mere existence of isolated map pairs. No such mechanism is asserted here. The cheap falsifier of END is one actual unknot-cap tangle whose unsigned extreme has zero integer Euler count. A failure of J-TILT alone would not falsify END; a failure of END would not falsify Lemma Q.

## Referee records

- [Sum functor and count theorem](sum_functor_referee.md).
- [J-TILT implication and endpoint refinement](jtilt_implication_referee.md).
- [Maps report and scope corrections](maps_report_referee.md).
- Independent finite verification: [maps_exact.py](referee_checks/maps_exact.py), run successfully in this session.

No new knot enumeration was performed. No message was sent to Claude. No external specialist review or priority claim is asserted.
