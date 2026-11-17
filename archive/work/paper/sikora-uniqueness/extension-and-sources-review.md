# Extension and source review for paper 1

Review date: 3 November 2026. Scope: source verification, attribution, and an independent check of the unframed statements in `work/big_reductions/surgery.md`. This review does not audit the main Jones conjecture, certify priority, or replace external specialist review. Main manuscript and scaffold were not edited.

## Assessment

The three-probe and arithmetic statements follow from the audited nonlongitudinal surgery lemma, with the qualifications below. I found no mathematical obstruction in the homology interpolation, reflected-functional calculation, or stated calibration. The proof should state its orientation and boundary conventions explicitly and choose its auxiliary meridian away from both given probes. The extra assumption of an existing rational-homology-sphere filling in the interpolation lemma can be dropped because the three matching orders already imply it.

No prior proof of the exact framed theorem or exact three-probe formulation was located in this bounded review. This is not a novelty or priority conclusion. The recent talk abstract is evidence of what that abstract says, not evidence that all subsequent literature or the complete talk has been checked.

Two bibliographic corrections are necessary: Buck–Mauricio changed the title between preprint and journal publication; the explicit rational/nonrational two-probe ambiguity is in Ernst–Sumners **1999**, Example 3, not their 1990 calculus paper.

## 1. Precise proposed theorem statements

Fix an oriented 3-ball with four marked boundary points. A two-string tangle here has exactly two interval components and no closed components. Equivalence of tangles fixes the marked boundary. Write `C_s(T)` for closure by the rational exterior tangle whose meridian lifts to the slope `s` on the common boundary torus. Slopes are primitive homology classes modulo sign. The common boundary identification preserves orientation; oriented link components are not required. Link equivalence below is ambient isotopy in the oriented 3-sphere, so its branched-cover lift preserves orientation. The determinant is nonnegative and is zero when the double branched cover has infinite first homology.

**Framed rational-solution uniqueness.** Let `P` and `Q` be rational tangles with distinct underlying unframed slopes, and let `R` be a rational tangle. Give these tangles balanced framings in Sikora's sense. If a balanced-framed two-string tangle `X` satisfies

`N(X+P) ≃ N(R+P)` and `N(X+Q) ≃ N(R+Q)`

as balanced-framed links, then `X ≃ R` as balanced-framed marked tangles.

If the manuscript intends to include additional circle components in its definition of two-tangle, say so separately, retain the determinant-one exclusion, and establish that the bracket argument covers that enlarged class. With the usual exactly-two-arcs definition, that exclusion is unnecessary but harmless as an extension remark.

**Two unframed closures and one determinant.** Let `R` be rational and `X` a two-string tangle in the same marked ball. Let `α,β,γ` be pairwise distinct rational closure slopes. Suppose

`det C_α(R)>0`, `det C_β(R)>0`,

`C_α(X) ≃ C_α(R)`, `C_β(X) ≃ C_β(R)`

by unframed ambient isotopy, and

`det C_γ(X)=det C_γ(R)`.

Then `X ≃ R` as unframed marked tangles. No positivity assumption is needed at `γ`.

**Three-closure corollary.** If the three closures of `X` at pairwise distinct slopes are ambient isotopic to the corresponding closures of rational `R`, then `X ≃ R` unframed. At most one of the three slopes is the disk slope of the solid-torus cover of `R`, so two have nonzero determinant.

**Diagnostic corollary.** If `X` is not equivalent to rational `R`, but the two nonlongitudinal closures at `α,β` are ambient isotopic to those of `R`, then

`det C_γ(X) ≠ det C_γ(R)` for every `γ ∉ {α,β}`.

This quantifies over every third slope, and allows `X` itself to be rational. Do not narrow it unnecessarily to nonrational `X`.

**Arithmetic two-probe criterion.** Under the two actual nonlongitudinal closure hypotheses above, set `d=Δ(α,β)>0`. If

`d ∤ 2 det C_α(R)`,

then `X ≃ R` unframed. The divisibility condition is unchanged if `β` replaces `α`. Failure of the condition does not assert existence of a rival.

These statements should use distinct *slopes*, not just different framed representatives of the same rational tangle. Allowing mirror equivalence or arbitrary orientation-reversing homeomorphisms in place of ambient isotopy would not justify the signed Casson–Walker comparison used by this proof.

## 2. Independent homology and surgery check

### Homology interpolation

Here is a slightly cleaner general statement:

Let `M` be a compact connected oriented 3-manifold whose entire boundary is one torus. Identify its boundary with that of a solid torus `V`. Put `h(Y)=|H_1(Y;Z)|` when finite, and `h(Y)=0` otherwise. If

`h(M(s_i))=h(V(s_i))` for three pairwise distinct slopes `s_1,s_2,s_3`,

then `H_1(M;Z)≅Z`, the boundary-to-homology map is onto, and its kernel is generated by the disk slope of `V`.

Proof check: at least two of the right-hand orders are positive. One finite filling, together with the usual half-lives–half-dies/Euler-characteristic argument, gives `b_1(M)=1`. Write `H_1(M)=Z⊕T`; let `e:H_1(∂M)→Z` be inclusion followed by projection. It need not yet be primitive. Mayer–Vietoris gives `H_1(M(s))=H_1(M)/⟨i(s)⟩`. Therefore

`h(M(s))=|T| |e(s)|`.

For `e(s)=0`, both sides are zero under the adopted convention; otherwise the quotient has order `|T| |e(s)|`, regardless of the torsion coordinate of `i(s)`. Let `m=|T|e` and let `l` be the primitive solid-torus functional. The degree-two homogeneous polynomial `(m-l)(m+l)` vanishes on three projective directions and hence identically. Over the polynomial domain this means `m=l` or `m=-l`. Primitivity of `l` forces `|T|=1` and `e` primitive. This proves all assertions, without irreducibility or framing.

The qualification “entire boundary is one torus” matters: an unspecified torus boundary component in a manifold with further boundary components is not the intended setting. The original lemma's QHS-filling assumption is redundant, not false.

### Matched-filling lemma

Use the following precise surgery lemma:

Let `M` be compact, connected, oriented, with boundary one torus and `H_1(M)=Z`. Suppose the boundary map is onto and an orientation-preserving boundary marking to a solid torus `V` identifies the homological longitude of `M` with the disk slope of `V`. If, for two distinct nonlongitudinal slopes `α,β`, the fillings `M(α),M(β)` are orientation-preservingly homeomorphic to `V(α),V(β)`, respectively, then `M` is a solid torus with that disk slope.

Details to include in its proof:

1. Choose the auxiliary primitive slope `μ` dual to the common longitude `λ` **and distinct from `α,β`**. There are infinitely many such dual slopes. Then `Y=M(μ)` is an integral homology sphere, and both input slopes have expressions `p_i μ+q_i λ` with `p_i≠0` and `q_i≠0`. This avoids applying a finite-surgery statement to the meridian slope.
2. The fixed oriented marking supplies the identical signed pair `(p_i,q_i)` on the comparison solid torus; do not identify coefficients merely from lens-space homeomorphism types. Simultaneously changing both signs does not change `q_i/p_i`.
3. Casson–Walker gives `0=λ_CW(Y)+(q_i/(2p_i))Δ_K''(1)`. Distinct slopes make the two ratios different. Subtraction yields `Δ_K''(1)=0`.
4. The two actual fillings are L-spaces. The Rasmussen–Rasmussen facts verified below give Floer simplicity, the alternating Alexander form, and then `Δ_K=1` by the elementary paired-square positivity argument.
5. Explain irreducibility using an **actual prime lens-space filling**, not the L-space condition alone. In a sphere decomposition of `M`, the closed summand is an integral homology sphere; its persistence under filling contradicts primeness unless it is `S^3`. Nonseparating spheres are excluded by `H_2(M)=0`.
6. Boundary incompressibility would force norm `deg(Δ)-1=-1`. Thus the boundary compresses, and irreducibility implies `M` is a solid torus. The disk slope is its homological longitude.

For the unframed theorem, determinant/order equality calibrates homology before this lemma is applied. The solid-torus branched-cover criterion then proves rationality, and rational-tangle classification with the marked disk slope proves equality. A solid-torus cover alone does not identify the rational slope; the calibration does that work.

### Arithmetic reflection

Take oriented coordinates `α=(1,0)`, `β=(a,d)`, with `gcd(a,d)=1`, and write `l=(u,v)` so `l(α)=u` and `l(β)=au+dv`. Both values are nonzero. After a single global sign choice `m(α)=u`, the second absolute-value equation gives exactly

`m=l` or `m=m*=(u,-v-2au/d)`.

The second candidate is integral only if `d|2au`, equivalently `d|2u`. Since `l(β)=au+dv` and `a` is invertible modulo `d`, also `d|2l(β)` iff `d|2u`. If the alternative is impossible, `m=l` gives the calibrated surgery lemma. If `X≠R`, the first candidate is impossible, so `m*` prescribes all residual determinants.

In particular, `content(m*)=|Tor H_1(M)|·[Z:e(H_1(∂M))]`; it determines that product, not the two factors separately. Its primitive kernel gives the rational longitude. These claims are independent of whether the integral candidate is geometrically realizable.

## 3. Calibration and its antecedent

For the project's rational-tangle convention, take

`X=⟨-1⟩+⟨1/2⟩+⟨1/3⟩`, `R=⟨1/4⟩`.

The local actual-diagram audits recorded in `work/try8/tangle/processive_proof.txt` identify the closures at add-ons `0,1` as the unknot and `T(2,-5)`, respectively, for both tangles. The cover of `X` is Seifert over a disk with exceptional orders `2,3`; its group surjects onto the nonabelian group `C_2*C_3`, so it is not a solid torus. These are topology claims; the determinant calculation by itself would not establish the actual closure types.

Independent determinant calculation for primitive `(p,q)` gives

`det N(X+⟨p/q⟩)=|6p-q|`,

`det N(R+⟨p/q⟩)=|4p+q|`.

Their squared difference is exactly `20p(p-q)`. Thus equality occurs only at projective slopes `0` and `1`. At `∞` the values are `6,4`, either by the same homology functionals or denominator closures. This verifies the asserted sharpness calibration and the absence of any hidden third determinant match. State the handedness convention or use the displayed diagrams; the torus-knot sign changes on mirroring.

The antecedent is Ernst–Sumners 1999, Example 3, pp. 33–34. Their first two listed solutions have the **same** reaction tangle `-1`: the nonrational outside tangle `(1/2,2/3,-1)` and rational outside tangle `-1/4`. Mirroring, followed by the usual integer transfers in the Montesinos presentation, gives `(-1,1/2,1/3)` and `1/4`, with reaction `+1`. Therefore the present calibration is a reformulation of a published example, not a new counterexample. Their example also allows other reaction tangles, but those are not needed here.

Primary publisher metadata: [Ernst–Sumners 1999](https://doi.org/10.1017/S0305004198002989). The article's Example 3 text was inspected through the [full article reproduction](https://www.researchgate.net/publication/231762263_Solving_tangle_equations_arising_in_a_DNA_recombination_model); the publisher abstract independently verifies the article identity and its four-equation scope. The reproduction is a copy of the primary article, not an independent secondary result.

## 4. Source register and attribution

### Sikora: exact target, weaker theorem, stronger equivalent

Adam S. Sikora, *Tangle equations, the Jones conjecture, slopes of surfaces in tangle complements, and q-deformed rationals*, Canadian Journal of Mathematics **76**(2) (2024), 707–727, DOI [10.4153/S0008414X23000755](https://doi.org/10.4153/S0008414X23000755). [arXiv:2005.08162v2](https://arxiv.org/html/2005.08162v2), 5 August 2023. The first version is dated 17 May 2020.

| Meaning | Journal | arXiv v2 |
|---|---|---|
| Uniqueness among rational framed solutions | Proposition 1.1 | Proposition 1 |
| Rational solution unique among all solutions | Conjecture 1.2 | Conjecture 2 |
| Jones unknot conjecture implies that conjecture | Theorem 1.3 | Theorem 3 |
| Framed rational tangles distinguished by bracket | Corollary 7.2 | Corollary 20 |
| Bracket vector fixed by two closure equations | Theorem 8.1 | Theorem 21 |
| Rational tangle detected among arbitrary tangles by bracket alone; Jones-equivalent | Theorem 9.2(c) | Theorem 24(c) |

This proof addresses actual balanced-framed closure isotopies. It does not establish bracket-only detection. The unframed three-probe result uses an additional datum; it is not an unframed restatement of the two-probe conjecture. The [2024 erratum](https://doi.org/10.4153/S0008414X24000208), p. 728, corrects only the author's printed surname.

### Gainullin: direct methodological antecedent

Fyodor Gainullin, *Heegaard Floer homology and knots determined by their complements*, Algebraic & Geometric Topology **18**(1) (2018), 69–109, DOI [10.2140/agt.2018.18.69](https://doi.org/10.2140/agt.2018.18.69), [arXiv:1504.06180](https://arxiv.org/abs/1504.06180).

[Theorem 8.2 and its proof, pp. 104–105](https://msp.org/agt/2018/18-1/agt-v18-n1-p03-p.pdf), concern a null-homologous knot in an L-space `Y`, with surgery Floer homology matching that of `Y#L(p,q)` (the grading information is essential). The proof combines Casson–Walker, `Δ''(1)=0`, the alternating coefficient structure, and genus detection. Credit this sequence explicitly.

The current auxiliary homology sphere is not established to be an L-space, and its comparison surgery is `L(p,q)`, not `Y#L(p,q)`. Choosing an actual lens filling as the ambient space instead generally makes the filling core homologically essential. Therefore the displayed theorem is not an immediate application of Gainullin 8.2 as stated. This is a hypothesis comparison, not a claim that nobody has made a related deduction elsewhere. Avoid quoting Gainullin's displayed statement without the surrounding nontrivial-surgery convention: meridional surgery would be tautological.

### Rasmussen–Rasmussen and Casson–Walker

Jacob Rasmussen and Sarah Dean Rasmussen, *Floer simple manifolds and L-space intervals*, Advances in Mathematics **322** (2017), 738–805, DOI [10.1016/j.aim.2017.10.014](https://doi.org/10.1016/j.aim.2017.10.014), [arXiv:1508.05900](https://arxiv.org/html/1508.05900). Proposition 1.3 supplies Floer simplicity from two L-space slopes. The paragraph preceding Proposition 1.4 gives the torsion normalization and eventual coefficient `1`; Proposition 1.4 supplies coefficients in `{0,1}`. Section 2.1 and Proposition 2.2 also record the eventual behavior. Corollary 2.3 gives the boundary-incompressible norm formula. Do not attribute the whole normalization to Proposition 1.4 alone. Proposition 7.8 is relevant only to the longitudinal branch of the framed proof, not to the unframed extension's nonlongitudinal lemma.

Yi Ni and Zhongtao Wu, *Cosmetic surgeries on knots in S^3*, Journal für die reine und angewandte Mathematik **706** (2015), 1–17, DOI [10.1515/crelle-2013-0067](https://doi.org/10.1515/crelle-2013-0067), [arXiv:1009.4720](https://arxiv.org/abs/1009.4720). Their [published Proposition 3.1, p. 9](https://www.its.caltech.edu/~yini/Published/Cosmetic.pdf) states the required signed `q/(2p)` formula for null-homologous knots in rational homology spheres, with symmetric Alexander polynomial normalized to value `1`. It attributes the general formula to Boyer–Lines, Theorem 2.8. Cite this verified restatement if the original is not independently inspected.

### Solid-torus cover and the Buck–Mauricio title change

Dorothy Buck and Mauro Mauricio, *Connect sum of lens spaces surgeries: application to Hin recombination*, Mathematical Proceedings of the Cambridge Philosophical Society **150**(3) (2011), 505–525, DOI [10.1017/S0305004111000090](https://doi.org/10.1017/S0305004111000090). The journal title and metadata were verified on the publisher's page.

The preprint is [arXiv:1007.0948](https://arxiv.org/abs/1007.0948). Its metadata title is *Tangle solutions for composite knots: applications to Hin recombination*; the [preprint body](https://arxiv.org/html/1007.0948) instead uses singular *application*. **Theorem 3.5(2) in that inspected preprint** states that a tangle is rational exactly when its double branched cover is a solid torus, crediting Lickorish. Do not silently assert this is the journal theorem number without checking the journal PDF. The displayed autogenerated HTML date is not the preprint's publication date.

W. B. R. Lickorish, *Prime knots and tangles*, Transactions of the American Mathematical Society **267**(1) (1981), 321–332, DOI [10.1090/S0002-9947-1981-0621991-2](https://doi.org/10.1090/S0002-9947-1981-0621991-2). The original AMS PDF returned 403 in this review; the solid-torus criterion was verified through Buck–Mauricio's explicit primary-paper restatement. Attribute to Lickorish while making the checked source clear. Buck–Mauricio's theorem about rational-to-composite products is nearby prior work, not the present marked uniqueness statement.

### Ernst–Sumners and Baker–Buck: precise nearby scope

Claus Ernst and De Witt Sumners, *A calculus for rational tangles: applications to DNA recombination*, Mathematical Proceedings of the Cambridge Philosophical Society **108**(3) (1990), 489–515, DOI [10.1017/S0305004100069383](https://doi.org/10.1017/S0305004100069383). Foundational tangle calculus; the publisher issue confirms this page range. Some later bibliographies print an incorrect starting page, so do not copy those entries.

C. Ernst and D. W. Sumners, *Solving tangle equations arising in a DNA recombination model*, Mathematical Proceedings of the Cambridge Philosophical Society **126**(1) (1999), 23–36, DOI [10.1017/S0305004198002989](https://doi.org/10.1017/S0305004198002989). Besides the calibration, this paper studies four processive equations `N(O+iR)=K_i`, `0≤i≤3`, with varying unknown reaction tangle `R`. Its uniqueness theorem under its stated product hypotheses is not the present three fixed probes against one specified rational comparator. Its examples with three equations and multiple pairs `(O,R)` likewise do not contradict the proposed theorem, which fixes the closure probes.

Kenneth L. Baker and Dorothy Buck, *The classification of rational subtangle replacements between rational tangles*, Algebraic & Geometric Topology **13**(3) (2013), 1413–1463, DOI [10.2140/agt.2013.13.1413](https://doi.org/10.2140/agt.2013.13.1413), [arXiv:1304.7669](https://arxiv.org/abs/1304.7669). The [publisher PDF](https://msp.org/agt/2013/13-3/agt-v13-n3-p05-p.pdf) verifies publication on 30 April 2013. Theorems 3.1/5.1 classify rational subtangle replacements and their sites between rational tangles. Theorem 5.2, p. 1440, classifies distance-at-least-two replacements between 2-bridge links and their sites, building on Darcy–Sumners. The latter is particularly relevant to the distance-at-least-three unknot corollary. It is not safe to advertise that special corollary as new without a complete comparison to those classifications. Conversely, these statements do not on their face state the general marked three-probe theorem.

Kronheimer–Mrowka–Ozsváth–Szabó, *Monopoles and lens space surgeries*, Annals of Mathematics **165** (2007), 457–546, [Theorem 1.1](https://annals.math.princeton.edu/2007/165-2/p03), [arXiv:math/0310164](https://arxiv.org/abs/math/0310164). Once the common longitude/peripheral data are fixed, an actual unknot closure gives ambient `S^3` and their surgery characterization covers the remaining finite surgery comparison. Determinant one alone only gives a homology sphere and cannot replace the actual unknot hypothesis.

### Recent status evidence

The primary [MathInstitutes record](https://www.mathinstitutes.org/videos/25091) dates Adam Sikora's IPAM talk *Tangle Equations, the Jones Unknot Conjecture, and Lens Space Surgeries* to **15 October 2026**. Its abstract explicitly labels rational-solution uniqueness in framed systems a conjecture and describes the implication from its failure to a failure of Jones unknot detection. This supports reporting the abstract's status as of that event. The full recording was not reviewed, and the abstract does not establish exhaustive current open status.

## 5. Local-source corrections that matter to the manuscript

- Follow `collab/audits/LATE-41-audit.md` over the older audited proof where they conflict. In particular, Stoimenow Proposition 6.5 establishes **odd determinant iff knot**, not the stronger `2^(c-1)` divisibility claim attributed to it in an older file. The former is sufficient for the determinant-one no-circle argument.
- The determinant/branched-cover homology identity, including determinant zero, needs a correct Goeritz-presentation reference or proof. The later audit flags the older Dasbach–Futer–Kalfagianni–Lin–Stoltzfus Section 3 citation as insufficient for the entire asserted generality.
- Do not use Sikora arXiv Proposition 10(1), journal Proposition 2.1(1), as a shortcut. The local audit rejects it. The surgery proof is independent of it; discussing the source error is optional and should not distract from the theorem unless the counterexample is fully presented and independently checked.
- Replace the Claude-note wording that a converse is “neither claimed nor true as far as anyone knows” with “no converse is claimed or established here.” Do not assert a converse is false merely because it is unknown.
- Replace broad claims that “no polynomial argument bridges” the gap with the specific statement that the present proof requires actual closure isotopies. The argument does not rule out other possible approaches.

## 6. Bounded search record and permissible priority wording

In addition to the local November 1 novelty audit, this pass checked the primary journal/preprint sources above and ran searches including:

- `Sikora "uniqueness" "rational solutions" tangle proof`
- `"three" "rational closures" tangle uniqueness`
- `"three" "solid torus" "same" "fillings" rigidity`
- `"tangle equations" "determinant" "three" uniqueness`
- `"Tangle solutions for composite knots" Cambridge 505 525`
- `"Buck" "Mauricio" "505" "525"`
- `"Heegaard Floer homology and knots determined" Gainullin arxiv`
- `"classification of rational subtangle replacements" arxiv`
- `"Solving tangle equations" "Example 3"`

Search results did not identify an exact earlier proof. This search was not exhaustive; it did not inspect every citing paper, unpublished manuscript, or the full October talk. Appropriate review wording is: “No prior proof of this exact formulation was located in the sources checked.” In the paper itself, prefer direct theorem statements and explicit attribution rather than declarations of priority.

Suggested attribution sentence: “The surgery argument follows the Casson–Walker and Alexander-polynomial strategy used by Gainullin, combined here with the Floer-simple-manifold results of Rasmussen and Rasmussen; the use of two matched fillings avoids assuming that the auxiliary homology sphere is an L-space.” This identifies the substantive overlap without asserting priority of the remaining deduction.

## 7. Check of the first compiled manuscript

The first `main.tex` was inspected after the report above was drafted. Line numbers below refer to that first compiled version and will move as the parent revises it.

- Line 125 cites Sikora Theorem 4 for Jones implying framed uniqueness. Change to arXiv v2 Theorem 3, or explicitly journal Theorem 1.3.
- Lines 1579–1582 combine Buck–Mauricio's preprint title with the journal reference. Use the journal title above and add a sentence identifying the preprint title and the fact that the cited Theorems 3.5(2) and 3.6 refer to the inspected preprint.
- Lines 1041–1046 cite only the 1990 Ernst–Sumners entry for the calibration, and describe its displayed convention as that “used there.” Add the 1999 entry and identify the displayed pair as the mirrored, integer-transferred version of Example 3(i),(ii). The project's handedness convention should not be silently attributed to the original article.
- The first manuscript already chooses `μ` away from both original probes. Adding `q_i≠0` at line 607 makes that consequence visible at the surgery application.
- Gainullin's arXiv identifier `1504.06180` and Baker–Buck's page range `1413–1463` are correct.
- Dasbach–Futer–Kalfagianni–Lin–Stoltzfus, *Alternating sum formulae for the determinant and other link invariants*, Journal of Knot Theory and Its Ramifications **19**(6) (2010), 765–782, is correctly identified by [arXiv:math/0611025v2](https://arxiv.org/abs/math/0611025v2), DOI [10.1142/S021821651000811X](https://doi.org/10.1142/S021821651000811X). Section 3 does record the standard determinant/order assertion, but its wording is informal (including an imprecise reference to a branched cover of the link complement), and does not explicitly state the infinite-order-as-zero convention or the disconnected Goeritz augmentation. Thus the citation identity is correct while the scope problem at lines 384–388 remains: provide the precise Goeritz justification or narrow what is attributed to that source.
- If the bibliography labels an arXiv version explicitly, link to that exact version (`.../abs/1508.05900v2`, `.../abs/2005.08162v2`, and `.../abs/1009.4720v2`) rather than the mutable unversioned URL. This is especially useful with a source/version-map appendix.

The source/version table in Section 4 is suitable for a concise manuscript appendix. A useful appendix can also identify the specific Rasmussen–Rasmussen inputs, the verified Ni–Wu restatement, and Buck–Mauricio's title change; it should not pad the page count with search history or repeat a novelty claim.
