> Public archival edition, prepared 17 November 2026. Historical AI-generated research/review record; not external specialist review. Private instructions and correspondence discussion have been removed with markers, and local paths anonymized. Mathematical claims and verdicts remain historical and may be superseded by the current ledger. No research or computation was rerun for this edition.



######## LENS: quotes

## verdict
"holds_with_fixes"
## findings (20)

### F1 [major] Claim (line 9) and §4 Conclusion (line 71)
- **claim**: An explicit nontrivial Brunnian 4-braid that is trivial at t = -1 'meets every hypothesis of Prop. 6.7 and Cor. 6.8'. §4 adds that Φ 'therefore meets every hypothesis of Lemma 6.3, Prop. 6.7 and Cor. 6.8'.
- **problem**: All three results assume that Φ = Φ′·Γ_1 is a proper product. The note gets this hypothesis only from the criterion asserted in the proof of Thm 6.9. The note itself says it could not check that criterion (line 69), and §5 (line 76) lists it as a possible false statement. So the headline states as fact something that is conditional. The 'Corrections folded in' list (line 105) says the conditional status of the shortcut was folded in, but the Claim and the Conclusion do not reflect it.
- **evidence**: Each statement assumes the proper product Φ′·Γ_1: Lemma 6.3 (p.17, layout 832), Prop 6.7 (p.20, layout 1031), Cor 6.8 (p.24, layout 1192). For the note's Φ, properness comes only from the Thm 6.9 proof: the simple-loop sentence (p.24, layout 1228-1230) and the assertion that a freely reduced juxtaposition makes the second condition immediate (layout 1231-1234). Note line 69 admits that Conditions 1 and 2 were not checked.
- **fix**: State the shortcut-free dichotomy. Either no B_4-conjugate of Φ0 is a proper product Φ′·Γ_1, and then the conjugation step of Thm 6.9 (p.25, layout 1239-1240) fails for Φ0. Or some conjugate is, and then Prop 6.7 fails for it. If the paper's free-reduction criterion is valid, the explicit Φ = Γ_1^{-1}y1^mΦ0y1^{-m}·Γ_1 falls in the second case. Wherever the unconditional form appears, write 'meets every hypothesis, provided the criterion stated in the proof of Thm 6.9 is valid'.

### F2 [major] §3, line 39
- **claim**: Quoted as: "By Proposition 6.7 we can assume that ι ≠ ι. The result follows."
- **problem**: This is a misquotation. Text inside quotation marks was altered with no ellipsis: both arguments of ι were deleted. The result reads like the tautology 'ι ≠ ι', which the authors never wrote. In a note addressed to the authors this looks careless or mocking.
- **evidence**: Paper p.24, layout 1214, confirmed on the page image: "By Proposition 6.7 we can assume that ι(α, (β^3_*)(f(Φ)·Γ)) ≠ ι(α, (β^3_*)Γ). The result follows."
- **fix**: Quote the sentence in full as above, or paraphrase it without quotation marks.

### F3 [major] §5, line 79 (second sentence)
- **claim**: "If the parity lemmas hold, the 'Furthermore' clause of Prop. 6.7 is what fails."
- **problem**: The sentence drops the first alternative of the disjunction stated at line 76, namely the shortcut criterion. If the shortcut fails, Φ′·Γ_1 need not be a proper product, Prop 6.7 need not apply to Φ, and its Furthermore clause may be true. The localization is overstated.
- **evidence**: Note lines 75-77 give two alternatives; line 79 concludes as if there were one. In the paper, the Furthermore part of the proof (pp.21-23, layout 1092-1176) builds Γ′ = γ1 ∪ γ2′ and checks only the two listed properties of γ2′ (layout 1101-1105, 1122-1123). Parity is proved only for the unmodified Γ (layout 1085-1091, via Lemmas 6.4 and 6.6). Lemma 6.6 needs Γ to be properly simple modulo 4-disks (layout 944-949, 987), and this is never re-checked for Γ′.
- **fix**: Write: 'If the shortcut criterion and the parity lemmas both hold, the Furthermore clause fails.' Optionally sharpen it: the proof of the Furthermore clause never re-establishes the hypotheses of Lemmas 6.4 and 6.6 for the modified loop Γ′. For the note's Φ, Lemmas 1-2 show that Γ′ and f(Φ)·Γ′ cannot both satisfy parity, so that is the place to look.

### F4 [major] Status (line 11); §4 line 50; §6 line 91; Verification section (lines 93-111)
- **claim**: 'Three independent hostile referees ... found no refutation'; 'A separate chat independently recomputed Φ0'; 'suggested by the breakthrough chat'; script paths bbb-gap/phi0_check.py, bbb-gap/check-parity/sec7.py, bbb-gap/check-tminus1/chk.py.
- **problem**: This is an attribution problem in a note meant for the authors. They will take 'independent referees' to mean independent human experts, which misdescribes internal checks, and 'chat' will be unintelligible to them. The paths cannot be accessed and do not match where the scripts actually are (source/scripts/). The referee lenses also leave out §3, the logical core, and §6.
- **evidence**: Note lines 11, 50, 91 and 95-111. The scripts are in <HOME>/jones-adversarial-pass/bbb-gap-note/source/scripts/.
- **fix**: Delete the Status line, the Verification section and the phrase 'suggested by the breakthrough chat'. Replace them with a neutral 'Computations' paragraph that states the conventions and attaches the code or the matrices.

### F5 [minor] §3, line 39
- **claim**: The proof of Cor. 6.8 'deduces M_{f(Φ)Γ} ≠ M_Γ from the inequality of the coefficient sums alone'.
- **problem**: The paper's sums are sums of absolute values of the coefficients (ℓ¹ norms). 'Coefficient sums' suggests Σ a_j = M(1). The authors may also object that the proof introduces the extreme exponents; the note should say how they are used.
- **evidence**: p.24, layout 1204 and 1209: |a_{M−}| + ... + |a_{M+}| = ι(α, (β^3_*)(f(Φ)·Γ)) and |b_{M′−}| + ... + |b_{M′+}| = ι(α, (β^3_*)Γ). The lowest and highest exponents M±, M′± (layout 1198-1200) appear only as summation limits. The conclusion (layout 1214) uses only the ι inequality.
- **fix**: Write 'from the inequality of the sums of absolute values of the coefficients alone; the extreme exponents M±, M′± that the proof introduces serve only as summation limits'.

### F6 [minor] §3 (line 39) and §1
- **claim**: The note uses M_{f(Φ)Γ} and 'Let Γ be as in Prop. 6.7' without comment.
- **problem**: Prop 6.7's Furthermore clause literally compares Φ·Γ, not f(Φ)·Γ, and the proof of Cor 6.8 also says that Φ·Γ satisfies parity. The note silently adopts two readings: f(Φ)·Γ for Φ·Γ, and a single Γ with all properties. Both readings are right, but they should be stated.
- **evidence**: Furthermore clause: ι(β^3_*·(Φ·Γ), α) ≠ ι(β^3_*·Γ, α) (p.20, layout 1033). Eq. (2): ι(α, (β^3_*)·Γ) ≠ ι(α, (β^3_*)(Φ·Γ)) (p.22, layout 1094). Cor 6.8's proof asserts parity for Γ and Φ·Γ (layout 1196) and writes f(Φ)·Γ only from layout 1204 on. The proof of 6.7 itself sets β = (β^3_*)f(Φ) (layout 1052), writes (β)Γ = (β^3_*)(Φ·Γ) (layout 1085) and concludes that f(Φ)·Γ satisfies parity (layout 1087).
- **fix**: Add one sentence: 'We read Φ·Γ in Prop. 6.7 as f(Φ)·Γ, as its proof and the proof of Cor. 6.8 do. As in that proof, we take one Γ with all the asserted properties.'

### F7 [minor] §4, line 65
- **claim**: 'The proof of Thm. 6.9 asserts a shortcut for Γ_1, without proof'.
- **problem**: The paper gives a brief justification for each condition, so 'without proof' will read as unfair. What is genuinely missing is an argument that free reduction yields the geometric Condition 2.
- **evidence**: Condition 1, p.24 layout 1228-1230: only β-to-α trigons and rectangles can occur; trigons are removed by isotopy; rectangles are excluded because α∩Γ_1 alternates in sign. Condition 2, layout 1234-1240: the remark that the reduced word of Γ_1 begins with y2^{-1}, followed by the conjugation remark.
- **fix**: Write 'asserts, with a short sketch that does not explain why free reduction yields Condition 2'.

### F8 [minor] §4, line 69
- **claim**: 'We could not check Conditions 1 and 2 directly, because the figures are not in our text.'
- **problem**: Figures 6.3 and 6.13 are in the paper. To the authors, the stated reason will read as 'we did not look at the figures'.
- **evidence**: Fig 6.3 is on p.16 and Fig 6.13 on p.25 (page images).
- **fix**: Write 'We have not verified Conditions 1 and 2 directly for Φ′·Γ_1; that would require drawing (β^3_*)Φ′.'

### F9 [minor] §5, line 79 (first sentence)
- **claim**: 'Prop. 5.1 is not a suspect, because Lemma 1 gives minimal position from parity alone.'
- **problem**: The paper's proof of Cor 6.8 never cites Prop 5.1. Prop 5.1's explicit use is in the proof of Lemma 6.2, which is one of the listed suspects. The sentence implies a role for Prop 5.1 that the paper does not state.
- **evidence**: The proof of Cor 6.8 (p.24, layout 1195-1214) does not mention Prop 5.1. The proof of Lemma 6.2 (p.16, layout 798-799) invokes Prop 5.1 to get minimal position of (β′)Γ.
- **fix**: Write: 'Prop. 5.1 is not needed for the contradiction: Lemma 1 supplies the minimal position used tacitly in Cor. 6.8. Prop. 5.1 enters the suspects only through Lemma 6.2.'

### F10 [minor] §5, line 77
- **claim**: 'Prop. 6.7, through its parity claims (Lemmas 6.2 to 6.6)'.
- **problem**: Lemma 6.1 also feeds the parity claims: it supplies the sign lists used in Lemma 6.3 and the fact that 4-disks are sign-changing, used in Lemma 6.4. Prop 5.1 enters through Lemma 6.2.
- **evidence**: p.15, layout 738: n = 4 is used particularly in Lemmas 6.1 and 6.3. Lemma 6.4: p.18, layout 916-918 and 935.
- **fix**: Write 'Lemmas 6.1 to 6.6 (and Prop. 5.1 via Lemma 6.2)'.

### F11 [minor] Notation, line 5 (with 'Notation follows the paper', line 3)
- **claim**: 'f : B_4 → B_5 is the stabilization'.
- **problem**: The paper never uses the word 'stabilization', which in braid theory usually means Markov stabilization. It calls f the inclusion map for the standard embedding (Obs 2.1) and the induced injection (§6.3). §6.3 also describes its embedding differently from Obs 2.1's standard one, as adding p5 'in the interior of the disk D4'. The note's ρ_5 computation uses σ_i ↦ σ_i.
- **evidence**: p.3, layout 140; p.17, layout 876-877. A grep of the paper text finds no 'stabiliz'.
- **fix**: Write 'the inclusion f : B_4 ↪ B_5 (Obs. 2.1, §6.3)'. Add one sentence: for any such embedding, f(Φ) is conjugate in B_5 to the standard image, so ρ_5(f(Φ)) is conjugate to ρ_4(Φ) ⊕ 1.

### F12 [minor] Notation, line 7; Lemma 2 proof, line 35
- **claim**: 'M_Φ ... defined up to a unit ±t^k'; 'The ± comes from normalising M only up to ±t^k.'
- **problem**: This misstates the paper's convention. The paper defines M only up to a power of t (the orientations fix the sign) and normalizes the first crossing to ±t^0.
- **evidence**: p.4, layout 174-176.
- **fix**: Write 'defined up to a power of t (the paper normalizes the first crossing to ±t^0); at t = −1 this ambiguity becomes a sign, since (−1)^k = ±1', and adjust line 35 to match.

### F13 [minor] Claim, line 9 (last sentence)
- **claim**: 'It shows that the question is open again.'
- **problem**: The tone and strength exceed what is shown. The note itself leaves the failing statement as a disjunction, and it is addressed to the authors.
- **evidence**: Note §5, lines 75-79.
- **fix**: Write 'It shows that the proof, as written, does not settle the question.'

### F14 [minor] §5, line 83
- **claim**: 'the definition and Prop. 5.1 require the first factor to lie in K_5, and f(Φ) does not.'
- **problem**: This is correct, but the authors may cite the remark in their §5 that its results hold with K_n replaced by any point-pushing subgroup K_j. The note should pre-empt this. Also, the proof of Prop 6.7 never checks that f(Φ)·Γ is a proper product at all.
- **evidence**: The K_j remark is on p.9, layout 428-429. The definition (p.11, layout 563-570) has Φ ∈ K_n and Γ based at p_n. The proof of 6.7 (layout 1040-1176) contains no check that f(Φ)·Γ is proper.
- **fix**: Add: 'f(Φ) lies in the point-pushing subgroup of p4 in B_5, but Γ is based at p5, so the remark on p.9 does not apply; and the proof of Prop. 6.7 does not address whether f(Φ)·Γ is proper.'

### F15 [minor] §3-§4 (omission)
- **claim**: Φ meets every hypothesis of Prop 6.7.
- **problem**: The proof of Prop 6.7 treats only braids that do not satisfy parity. An author could reply that the parity case is handled separately. The note can close this off in one line.
- **evidence**: p.20, layout 1040: the proof opens by assuming that Φ does not satisfy parity. Apply Lemmas 1-2 with X = 1; here M_1 = 0, since α and β^3_* are disjoint (Fig 2.2). Then a braid that is trivial at t = −1 and has ι > 0 cannot satisfy parity.
- **fix**: Add one sentence saying that Φ does not satisfy parity, so it falls in the case the proof treats.

### F16 [wording] §4, line 49
- **claim**: 'Deleting strand i ≤ 3 kills A_{i4}, and with it the inner commutator.'
- **problem**: For i = 3 the innermost commutator [A14, A24] survives. What dies is b, because A34 ↦ 1.
- **evidence**: Artin-action check (check/quotes/brunn_check.py): after deleting strand 3, [A14, A24] is nontrivial and b is trivial.
- **fix**: Write 'kills A_{i4}, and hence b'.

### F17 [wording] §4, lines 45 and 50
- **claim**: 'standard pure braid generators'; ρ_4(Φ0) = I at t = −1.
- **problem**: Conventions for A_{ij} and for the Burau matrices vary, and the note gives neither, so its computation is hard to reproduce.
- **evidence**: The computation used A14 = σ3σ2σ1²σ2^{-1}σ3^{-1}, A24 = σ3σ2²σ3^{-1}, A34 = σ3², and σ_i ↦ I ⊕ [[1−t, t],[1, 0]] ⊕ I. The word length of Φ0 is 112 (check/quotes/phi0_laurent.py).
- **fix**: State these conventions explicitly in the note.

### F18 [wording] Throughout (e.g. line 7)
- **claim**: '(β*_3)Φ'.
- **problem**: The paper typesets the arc as β^3_*, with subscript * and superscript 3. In plain text, 'β*_3' reads as subscript 3.
- **evidence**: p.5, layout 227 (page image).
- **fix**: Write β^3_* (or β_*^3).

### F19 [wording] §5, line 82
- **claim**: 'that proof shows only that Φ·Γ_1 is reduced and then asserts Φ = Φ′·Γ_1'.
- **problem**: The paper does not prove that Φ·Γ_1 is reduced; it arranges this by conjugating Φ.
- **evidence**: p.25, layout 1238-1240. The intended step is stated in the introduction (p.2, layout 78-79): every braid in K4 is to be conjugated to one realized as a proper product.
- **fix**: Write 'arranges, by conjugation, that Φ·Γ_1 is freely reduced, and then concludes Φ = Φ′·Γ_1', and cite the introduction's statement of intent.

### F20 [wording] §6, line 91
- **claim**: 'nontrivial Brunnian braids occur at every depth'.
- **problem**: The argument needs only arbitrarily large depth, which iterated commutators provide. Exact depth d for every d is not shown.
- **evidence**: Depth is at least additive under commutators; exact depths were not computed.
- **fix**: Write 'of arbitrarily large depth'.
## confirmed
[
 "Title and authors. The note's title matches the arXiv metadata: the PDF Info Title field is 'The Burau representation of the braid group is faithful for n = 4'. The title printed on p.1 omits 'of the braid group'; either is acceptable. The authors and arXiv:2607.05283v2 are correct (p.1 stamp).",
 "ρ_n is the unreduced Burau representation, acting on the free rank-n Z[t^{±1}]-module H_1(D̃_n, {p̃*}) (p.1, layout 22-24; p.3).",
 "K_i ≅ π_1(D_{n-1}, p_i) is the point-pushing subgroup (p.8, layout 404). The note writes = where the paper writes ≅; this is harmless.",
 "M_Φ = M(α, (β^3_*)Φ) (p.5, layout 227). M_Φ is well defined on the homology class in H_1(D̃_n, {p̃*}), and the boundary of a regular neighbourhood of the arc gives a loop around p3 (p.5, layout 229-231). The proof of Thm 2.3 uses this (layout 245-256).",
 "W_i = +k or −k for the k-punctured disk bounded by α_i ∪ β_i (p.6, layout 270-274), so |W_i| = |P(Δ_i)|, with P(Δ) as defined on p.7. Lemma 3.1 gives W_i = k_{i+1} − k_i, which is eq. (1) (p.6, layout 295-299).",
 "Parity condition: a disk is sign-changing exactly when |P(Δ)| is odd (p.7, layout 352-357). 'Admits no cancellations' means there is no pair with k_i = k_j and ε_i = −ε_j, and Lemma 4.2 holds for φ ∈ B_n (p.8, layout 371-375). In §4, m = ι(α, β) is part of the paper's set-up (layout 370).",
 "Obs 2.1 is stated for the standard embedding (p.3, layout 140-141). Thm 2.3: if M_{Φ·Γ} ≠ M_Γ for some Γ ∈ B_n, then Φ ∉ ker ρ_n (p.5, layout 245). The chain Prop 6.7 → Cor 6.8 → Thm 2.3 is the one in the proof of Thm 6.9 (p.25, layout 1250-1252).",
 "Prop 6.7, checked on the page image (p.20, layout 1031-1033). Hypothesis: Φ ∈ B_4 (not K_4), written as a proper product Φ′·Γ_1. Conclusion: some Γ ∈ K_5 such that f(Φ)·Γ is a proper product in B_5, and both f(Φ)·Γ and Γ satisfy parity. Furthermore clause: ι(β^3_*·(Φ·Γ), α) ≠ ι(β^3_*·Γ, α), comparing Φ·Γ (not f(Φ)·Γ) with Γ, both applied to the arc β^3_*.",
 "Cor 6.8 (p.24, layout 1192-1193). Hypothesis: Φ ∈ K_4, Φ = Φ′·Γ_1 a proper product, and ι(α, (β^3_*)Φ) > 0. Conclusion: some Γ ∈ K_5 with M_{f(Φ)·Γ} ≠ M_Γ. Its proof (layout 1194-1214) uses only three things: Lemma 4.2 (no cancellation), the identities Σ|coefficients| = ι, and the ι inequality from Prop 6.7. The extreme exponents M± and M′± appear only as summation limits. So the note's 'alone' is correct.",
 "Thm 6.9 proof, checked on the page images of pp.24-25. (1) For a simple loop such as Γ_1, only trigons and rectangles can occur; trigons are removed by isotopy, and rectangles are excluded because the signs alternate along α (layout 1228-1230). (2) A freely reduced juxtaposition gives 'the second condition' (layout 1231-1234). (3) The reduced word of Γ_1 begins with y2^{-1} (layout 1238). (4) The conjugation remark, then the conclusion Φ = Φ′·Γ_1 with Φ′ ∈ K_4 (layout 1238-1240). The note's paraphrases are accurate apart from 'without proof' and 'shows'.",
 "Proper product definition (p.11, layout 563-575): Φ ∈ K_n, Γ a loop based at p_n, Γ in minimal position with α and β. Condition 1: no bigon-forming polygons. Condition 2: (a) Γ_I ∩ β′ ≠ ∅, or (b) Γ_I ∩ β′ = ∅ and Γ_F ∩ β′ = ∅. Prop 5.1 requires Φ ∈ K_n (p.12, layout 599-600). f(Φ) ∉ K_5 for Φ ≠ 1, since forgetting p5 returns Φ.",
 "Brun_n is normal in B_n (p.2). Whittlesey: nontrivial Brunnian braids are pseudo-Anosov (p.2, layout 83). The image of β^3_* under a pseudo-Anosov map meets α (p.24).",
 "Section 7 data, checked with my own script check/quotes/sec7_check.py on polynomials transcribed from the page images of pp.26-27. M_Φ (not parity): 8 terms, M(−1) = 2. M_{Φ·Γ} (parity): 8 terms, M(−1) = 8. M_Γ (parity): 20 terms, M(−1) = −20. All three simplified forms match the paper. Both parity sequences satisfy 'the sign changes iff |k_{i+1} − k_i| is odd', and ε_i(−1)^{k_i} is constant along each. M_Φ violates parity at the step with W = −4. Fig 3.1(b) gives 6 terms and M(−1) = 6, also consistent with Lemma 1.",
 "The paper never mentions t = −1, a double or branched cover, the Torelli group or BI_n, hyperelliptic or symplectic representations, Putman, or Brendle-Margalit-Putman: grep finds no hits. 'Cover' refers only to the Z-cover D̃_n, and 'Margalit' appears only in [Mar19], [FM12] and the acknowledgements. The note itself makes no claim of this kind, so nothing needs fixing; if such a claim is added, it is accurate.",
 "Φ0 facts, recomputed independently with exact Laurent-polynomial arithmetic (check/quotes/phi0_laurent.py). The word length is 112. ρ_4(Φ0) = I at t = −1, but ρ_4(Φ0) ≠ I as a Laurent matrix and at t = 2 and t = 3. The same holds for ρ_5 under σ_i ↦ σ_i. The (t+1)-adic order of ρ(Φ0) − I is exactly 1. (σ1σ2)^6 is I at t = −1.",
 "Φ0 is nontrivial, pure and Brunnian, checked with the Artin action (check/quotes/brunn_check.py). δ = Δ_3^{-2}Δ_4² is pure and lies in K_4, Δ_4² is central, and Φ0 = [δ^{-2}, b] (check/quotes/delta_check.py, by composing block automorphisms).",
 "The free-reduction claims at both junctions of Φ′·Γ_1 are correct, checked by hand, given the paper's claim about the first letter of Γ_1 and m > |Φ0|.",
 "Logical core, checked by hand. Under parity, ε_i(−1)^{k_i} is constant (from eq. (1) and the parity definition). Hence |M(−1)| = m = Σ|coefficients| = ι. If ρ(Y) = I at t = −1, the class contributions for YX and X differ by (t+1)H. So for any Φ trivial at t = −1, no Γ can have both parity properties and the ι inequality."
]
## not_checked
[
 "Conditions 1 and 2 of a proper product for Φ′·Γ_1, checked directly from Figs 6.3 and 6.13. I did not compute Γ_1's reduced word in the y-basis.",
 "Whether Γ_1's reduced word really begins with y2^{-1}. This is taken from the paper's text (layout 1238).",
 "The figure-driven case analyses of Lemmas 6.2 to 6.6 and of Prop 6.7 (Figs 6.4-6.12).",
 "The moment and span discussion in the note's §6, beyond the derivative identity M^{(j)}(−1) = ±(−1)^j p^{(j)}(1), which I checked by hand. I did not analyse the effect of the t^k shift ambiguity on moment comparisons.",
 "The full sesquilinearity argument of Lemma 2 and the reduced and transposed Burau conventions. These belong to the t = −1 lens; the logic reads correctly.",
 "The arXiv abstract page, since I made no network access. The title was checked against the PDF metadata and against p.1."
]
## summary
"Lens: quotations and attributions. I checked every statement the note makes about the paper against the page images (re-rendered at 200-220 dpi, crops in <HOME>/jones-adversarial-pass/bbb-gap-note/check/quotes/hires/) and the layout text, and recomputed the numerical claims with my own scripts in <HOME>/jones-adversarial-pass/bbb-gap-note/check/quotes/ (sec7_check.py, phi0_laurent.py, brunn_check.py, delta_check.py).\n\nThe note represents the paper accurately on every point the task singled out:\n- **(a) Prop 6.7** assumes Φ ∈ B_4, not K_4. Its Furthermore clause compares ι(β^3_*·(Φ·Γ), α) with ι(β^3_*·Γ, α): Φ·Γ, not f(Φ)·Γ, applied to the fixed arc β^3_*.\n- **(b) The proof of Cor 6.8** uses only Lemma 4.2, the identities Σ|coefficients| = ι, and the ι inequality. The extreme exponents M± serve only as summation limits.\n- **(c) The proof of Thm 6.9** contains the simple-loop sentence about trigons and rectangles, the claim that a reduced juxtaposition gives 'the second condition', the remark that Γ_1's reduced word begins with y2^{-1}, and the conjugation step.\n- **(d) Section 7:** M(−1) = 8 (8 terms) and −20 (20 terms) for the two parity polynomials, and 2 (8 terms) for the non-parity one.\n- **Φ0:** trivial at t = −1, nontrivial as a Laurent matrix and at t = 2 and 3, (t+1)-adic depth 1, Brunnian, and equal to [δ^{-2}, b] with δ ∈ K_4.\n- **What the paper never mentions:** t = −1, double covers, BI_n and BMP. The note makes no such claim.\n- **Title:** the note's title is the arXiv metadata title; the title printed on p.1 omits 'of the braid group'.\n\nFour major problems need fixing before the note is finalized:\n1. The Claim and the §4 Conclusion say, without qualification, that the braid 'meets every hypothesis' of Prop 6.7 and Cor 6.8. That rests on the shortcut in the proof of Thm 6.9, which the note admits it did not check.\n2. The quotation of the proof of Cor 6.8 is cut to 'ι ≠ ι' inside quotation marks.\n3. The §5 sentence that puts the failure in the Furthermore clause drops the shortcut alternative.\n4. [Redacted: private correspondence or workflow instructions.]\n\nThe minor items are paraphrases to tighten:\n- 'coefficient sums' should be 'sums of absolute values';\n- the reading of Φ·Γ as f(Φ)·Γ, and of a single Γ, should be stated explicitly;\n- 'without proof' should acknowledge the paper's brief sketch;\n- 'the figures are not in our text' should go;\n- the role of Prop 5.1 is in Lemma 6.2, not Cor 6.8;\n- Lemma 6.1 should be added to the suspects;\n- 'stabilization' is not the paper's term; it calls f an inclusion;\n- M is defined up to t^k, not ±t^k;\n- pre-empt the paper's p.9 remark on K_j;\n- note that Φ cannot satisfy parity, so it falls in the case the proof of Prop 6.7 treats.\n\nA useful sharpening, verifiable from the text: the proof of the Furthermore clause (pp.21-23) modifies Γ to Γ′ and checks only two properties of γ2′. It never re-establishes for Γ′ the hypotheses that Lemmas 6.4 and 6.6 need for parity.\n\nThe orchestrator asked for a markdown copy at check/quotes/report.md, but the harness blocks subagents from writing report files, so it was not saved; this output is the full report.\n\nSide remarks on the paper, not errors in the note:\n- p.26 says the last three exponents increase by 1; they actually decrease.\n- The proof of Lemma 4.2 writes Σ|P(Δ)| = 0 where the signed winding sum is meant.\n- The proof of Prop 6.7 never checks condition (3) of 'properly simple', nor that f(Φ)·Γ is a proper product."
## cleanest_statement
"Let Φ0 = [(σ1σ2)^6, [[A14, A24], A34]] ∈ B_4, where A_{i4} = σ3···σ_{i+1}σ_i²σ_{i+1}^{-1}···σ3^{-1}. Exact computation shows that Φ0 is a nontrivial pure Brunnian braid with ρ_4(Φ0) = I at t = −1 and ρ_4(Φ0) ≠ I at t = 2. Lemma 1 follows from Bigelow's Lemma 3.1 and the paper's definition of parity: if a transverse representative of (β^3_*)X with m intersection points satisfies the parity condition, then |M_X(−1)| = m = Σ|coefficients| = ι(α, (β^3_*)X). Lemma 2: if ρ_n(Y) = I at t = −1, then M_{Y·X}(−1) = ±M_X(−1) for every X. Hence, for every B_4-conjugate Φ of Φ0 and every Γ ∈ K_5 such that f(Φ)·Γ and Γ both satisfy parity, ι(α, (β^3_*)(f(Φ)·Γ)) = ι(α, (β^3_*)Γ). So no Γ has all the properties that Prop. 6.7 asserts, reading Φ·Γ as f(Φ)·Γ as its proof and the proof of Cor. 6.8 do. Consequently there are two cases. Either no conjugate of Φ0 can be written as a proper product Φ′·Γ_1, and then the conjugation step in the proof of Thm. 6.9 fails for Φ0. Or some conjugate can, and then Prop. 6.7 is false for it. In either case the proof of Thm. 6.9 does not cover the nontrivial Brunnian braid Φ0. If the criterion stated in that proof is valid (a freely reduced juxtaposition with Γ_1 is a proper product), the explicit conjugate Γ_1^{-1}y1^mΦ0y1^{-m}·Γ_1, with m larger than the length of Φ0, is in the second case. This does not show that ρ_4 is unfaithful."

## VERIFY
{
 "verdicts": [
  {
   "claim": "Finding 1 (Claim, line 9; §4 Conclusion, line 71). The note says the explicit Brunnian braid meets every hypothesis of Lemma 6.3, Prop 6.7 and Cor 6.8. But the proper product Φ = Φ′·Γ1 that all three results assume comes only from the unverified criterion in the proof of Thm 6.9. So the headline states as fact something that is conditional.",
   "verdict": "REAL",
   "evidence": "Paper:\n- Lemma 6.3 (p.17, layout 832-833) assumes Φ = Ψ·Γ1 is a proper product.\n- Prop 6.7 (p.20, layout 1031) assumes only Φ ∈ B4 and a proper product Φ′·Γ1.\n- Cor 6.8 (p.24, layout 1192) assumes the proper product and ι > 0.\n- For the note's Φ, properness comes only from the two assertions in the proof of Thm 6.9 (p.24, layout 1228-1234).\n\nNote:\n- Line 65 calls that shortcut unproved, line 69 says Conditions 1 and 2 were not checked, and line 76 lists it as possibly false.\n- Line 105 says the conditional status was 'folded in', yet lines 9 and 71 carry no condition.\n\nI re-checked the §4 free reductions:\n- Φ0 is a nontrivial element of [K4,K4], so its reduced word is y1^a w y1^b with w nonempty and not beginning or ending in y1^{±1}.\n- Hence y1^m Φ0 y1^{-m} reduces to y1^{m+a} w y1^{b-m}.\n- Γ1 begins with y2^{-1} (layout 1234-1238), so both junctions are reduced.\n- So the criterion's hypothesis holds; only the criterion itself is unverified.\n\nThe referee's dichotomy is valid. Every B4-conjugate of Φ0 is nontrivial, Brunnian, and trivial at t=-1 under ρ4 and under ρ5∘f.\n- If some conjugate is a proper product Φ′·Γ1: Prop 6.7, which needs nothing else, asserts a Γ such that Γ and f(Φ)·Γ both satisfy parity and their ι differ. The note's Lemmas 1-2 forbid this.\n- If none is: the reduction step fails for Φ0. That step is at p.25, layout 1238-1240, and is announced on p.2, layout 78-79.\n- Since the explicit Φ meets the criterion's hypothesis, the second case implies that the criterion is false. So the §5 disjunction (lines 75-77) is already correct; only lines 9 and 71 overstate.\n- The dichotomy needs only Prop 6.7. So it also avoids the paper's claim that ι > 0 for nontrivial Brunnian braids (p.5, layout 259-260), which only Cor 6.8 needs.\n- 'Explicit' then refers to Φ0, which is fully explicit.",
   "required_change": "Rewrite the third sentence of line 9 as the dichotomy: 'Either no conjugate of Φ0 can be written as a proper product Φ′·Γ1, and then the reduction step in the proof of Thm 6.9 (p.25) fails for Φ0. Or some conjugate can, and then Prop 6.7 fails for it. By the criterion asserted in the proof of Thm 6.9, the explicit conjugate Φ of §4 is such a proper product.'\n\nAt line 71, add 'provided the criterion asserted in the proof of Thm 6.9 is valid'.\n\nAt line 69, delete 'because the figures are not in our text'. The paper has the figures, so the reason will puzzle the authors. Say only that Conditions 1 and 2 were not verified directly."
  },
  {
   "claim": "Finding 2 (§3, line 39). The quoted sentence from the proof of Cor 6.8, 'By Proposition 6.7 we can assume that ι ≠ ι. The result follows.', is a misquotation: both arguments of ι were deleted inside quotation marks with no ellipsis.",
   "verdict": "REAL",
   "evidence": "The paper's sentence is at p.24, layout 1214. I confirmed it on the page image and in my 300 dpi crop (<HOME>/jones-adversarial-pass/bbb-gap-note/check/verify-quotes/p24quote-24.png). It reads \"By Proposition 6.7 we can assume that\" and then states ι(α, (β^3_*)(f(Φ)·Γ)) ≠ ι(α, (β^3_*)Γ), before a short sentence saying the result follows.\n\nI checked the raw bytes of note line 39. They contain exactly 'ι ≠ ι', so no markup was stripped in rendering. The quotation has been altered, and it reads as a tautology the authors never wrote.",
   "required_change": "Quote the sentence with both arguments of ι, in the paper's notation β^3_* (superscript 3, subscript *), citing p.24, end of the proof of Cor 6.8. Alternatively, paraphrase it without quotation marks.\n\nIn the same line, change 'coefficient sums' to 'sums of the absolute values of the coefficients'. The display in that proof (layout 1202-1209) sums |a_j|, and that sum is what Lemma 1 identifies with |M(-1)|.\n\nOptional: the note writes β*_3 throughout (for example line 7), which reverses the paper's β^3_*, although line 3 says the notation follows the paper."
  },
  {
   "claim": "Finding 3 (§5, line 79, second sentence). 'If the parity lemmas hold, the Furthermore clause of Prop 6.7 is what fails' drops the shortcut alternative from line 76, so the localization is overstated. Optional sharpening: the Furthermore proof never re-establishes the hypotheses of Lemmas 6.4 and 6.6 for Γ′.",
   "verdict": "REAL",
   "evidence": "The core point is correct. If the shortcut criterion fails, the explicit Φ need not be a proper product, Prop 6.7 need not apply, and nothing in it is contradicted. The severity is moderate rather than major, because lines 75-77 state the disjunction correctly.\n\nPaper check:\n- The Furthermore part is on pp.22-23 (layout 1092-1176). The referee's 'pp.21-23' is a page slip; p.21 is the construction of γ1 and γ2.\n- The proof says it suffices to find γ2′ with two properties (layout 1100-1107). That claim concerns inequality (2) only.\n- It never returns to three requirements of Prop 6.7: parity of Γ′, parity of f(Φ)·Γ′, and properness of f(Φ)·Γ′.\n- Parity is shown only for the unmodified Γ (layout 1085-1091).\n- Property 2 is asserted without argument (layout 1122-1123).\n\nTwo tightenings of the referee's text:\n(a) 'The parity lemmas hold' is still slightly loose. Placing the failure in the Furthermore clause also needs the constructed Γ = γ2∘γ1 to meet the lemmas' hypotheses. Layout 1088-1090 justifies only conditions (1) and (2) of 'properly simple modulo 4-disks', not condition (3) or simplicity modulo 4-disks.\n(b) For Γ′ = γ1∪γ′∪γ″∪γ2, the hypothesis of Lemma 6.4 holds by construction: γ1, γ′ and γ″ avoid β, and γ2 is reused after the last crossing with α (property 1). So f(Φ)·Γ′ keeps parity. For the note's Φ:\n- property 1 gives ι(f(Φ)Γ′) = ι(f(Φ)Γ);\n- Lemmas 1-2 give ι(f(Φ)Γ) = ι(Γ);\n- property 2 gives ι(Γ) < ι(Γ′);\n- hence |M_{Γ′}(-1)| < ι(Γ′), so Γ′ itself violates parity. If Lemma 6.6 holds, Γ′ is then not properly simple modulo 4-disks. This is unless property 2 fails.",
   "required_change": "Replace the second sentence of line 79 with: 'If the shortcut criterion holds and the loop Γ = γ2∘γ1 built in the proof of Prop. 6.7 does give the parity condition for Γ and f(Φ)·Γ, as that proof claims via Lemmas 6.4 and 6.6, then it is the Furthermore clause that fails.'\n\nOptional addition: 'The modified loop Γ′ (p.22) still meets the hypothesis of Lemma 6.4, so f(Φ)·Γ′ keeps the parity condition. If property 2 there holds, Lemmas 1-2 then show that Γ′ itself cannot satisfy it. The proof checks only properties 1-2 of γ2′, gives no argument for property 2, and does not show that Γ′ is properly simple modulo 4-disks.'\n\nIf the dichotomy of finding 1 is adopted, phrase this as 'for any conjugate of Φ0 that is a proper product Φ′·Γ1', and the shortcut condition drops out."
  },
  {
   "claim": "Finding 4 (Status line 11; line 50; line 91; Verification section, lines 93-111). 'Three independent hostile referees', 'a separate chat' and 'the breakthrough chat' misdescribe internal checks to the authors. The script paths are inaccessible and do not match where the scripts are (source/scripts/). The lenses also leave out §3 and §6.",
   "verdict": "REAL",
   "evidence": "The substance is right.\n- Lines 11, 91 and 95-111 present internal review passes as independent referees, which the authors will read as human refereeing, and refer to 'chats' that mean nothing to them.\n- The section is also inaccurate: line 105 claims the shortcut's conditional status was folded in, and finding 1 shows it was not.\n- The local paths at lines 50, 96 and 97 are useless to the authors.\n\nTwo sub-points of the referee are wrong:\n- The paths are not mismatched. They resolve under <HOME>/jones-lanes/g2-proof/bbb-gap/, and cmp shows the five files there are byte-identical to source/scripts/.\n- §3 was partly covered: line 96 lists Cor 6.8 among the parity pass's checks, and line 109 says the separate pass agreed with §3's logic. Only §6 has no stated check.\n\nI re-ran phi0_check.py, chk.py and brunn.py (python3 -I). They reproduce every stated fact:\n- ρ4(Φ0) and ρ5(f(Φ0)) are I at t=-1, and are not I at t = 2, 3 or 1/3;\n- the same holds in unreduced and reduced Burau and in their transposes;\n- Φ0 has length 112, is pure and nontrivial, and every strand deletion is trivial under the Artin action.\n\nNo script backed the 'depth exactly 1' claim (lines 91 and 109). My <HOME>/jones-adversarial-pass/bbb-gap-note/check/verify-quotes/depth_check.py uses exact Laurent polynomials and confirms that ρ(Φ0) − I is divisible by (t+1) but not by (t+1)^2, in unreduced B4, in reduced B4, and for f(Φ0) in B5.",
   "required_change": "Delete the Status line (11), the Verification section (93-111), the phrase 'suggested by the breakthrough chat' (91), and the paths in line 50.\n\nAdd a neutral 'Computations' paragraph with the code attached. It should state:\n- the conventions: σ_i ↦ I_{i-1} ⊕ [[1-t, t],[1, 0]] ⊕ I_{n-i-1}, words multiplied left to right, A14 = σ3σ2σ1²σ2⁻¹σ3⁻¹, A24 = σ3σ2²σ3⁻¹, A34 = σ3², [x,y] = xyx⁻¹y⁻¹, and Φ0 of length 112;\n- the evaluations at t = -1, 2 and 3, and that they agree in reduced Burau and in the transposes;\n- the depth-1 result, which should be backed by attached code (for example depth_check.py);\n- the Brunnian check.\n\nKeep in the main text the honest limitations now on line 111: Conditions 1 and 2 not checked from the figures, and the case analyses of Lemmas 6.3 and 6.6 not checked.\n\nHow to acknowledge machine assistance is the sender's decision. The checks must not be called independent referees."
  }
 ],
 "summary": "All four major findings hold up, and the note must change for each of them. None comes from a misreading of the paper or the note. The note's thesis survives once it is restated as a dichotomy (finding 1).\n\nFindings:\n1. **Finding 1 (REAL).** Lines 9 and 71 state, without condition, that the explicit braid meets the proper-product hypothesis. The note itself admits it rests on the unverified criterion in the proof of Thm 6.9.\n   - The referee's dichotomy is valid and needs only Prop 6.7. Either no conjugate of Φ0 is a proper product Φ′·Γ1, and the reduction step at p.25 fails. Or one is, and Prop 6.7 fails for it.\n   - It also avoids the paper's ι > 0 claim.\n   - Because the explicit Φ meets the criterion's hypothesis, the §5 disjunction is already correct.\n2. **Finding 2 (REAL).** Line 39 quotes the p.24 sentence (layout 1214, confirmed on a 300 dpi render) with both arguments of ι removed, so it reads 'ι ≠ ι'. Requote it in full or paraphrase. Also change 'coefficient sums' to 'sums of absolute values of the coefficients'.\n3. **Finding 3 (REAL, moderate severity).** Line 79 needs the shortcut condition. The referee's page range should be pp.22-23, not pp.21-23.\n   - The referee's replacement wording is still slightly loose. Placing the failure in the Furthermore clause also needs the constructed Γ to meet the lemmas' hypotheses, and the paper justifies only conditions (1) and (2).\n   - The optional sharpening can be made exact: the modified loop Γ′ still satisfies Lemma 6.4's hypothesis, so f(Φ)·Γ′ keeps parity. Lemmas 1-2 then force Γ′ itself to violate parity, unless the paper's unargued property 2 fails.\n4. **Finding 4 (REAL).** The internal 'referees' and 'chat' language and the local paths must go before finalization.\n   - Two of the referee's sub-points are wrong. The paths do exist under <HOME>/jones-lanes/g2-proof/bbb-gap/ and are byte-identical to the copies in source/scripts/. And §3 was partly covered.\n   - Keep the 'not checked' limitations in the main text.\n\nComputations:\n- I re-ran the existing scripts. They reproduce all the stated Burau and Brunnian facts.\n- The 'depth exactly 1' claim had no script behind it. My new <HOME>/jones-adversarial-pass/bbb-gap-note/check/verify-quotes/depth_check.py confirms it in unreduced and reduced Burau, and for f(Φ0).\n\nMinor items (not among the findings):\n- The note's β*_3 reverses the paper's β^3_*.\n- Line 65's 'without proof' is too strong for Condition 1.\n- Line 69's reason 'the figures are not in our text' should be dropped.\n\nFiles: <HOME>/jones-adversarial-pass/bbb-gap-note/check/verify-quotes/depth_check.py, p24quote-24.png and p20prop67-20.png in the same folder.\n\nThe requested report.md was not saved: the harness blocks subagents from writing report files. The full content is in this structured output instead."
}


######## LENS: defence

## verdict
"holds_with_fixes"
## summary
"Verdict: the note's conclusion stands; no authors' defence succeeds; the wording and the localization need fixes before finalization.\n\nI could not save report.md: the harness blocks subagents from writing report files, so the full report is in this output. Scripts and outputs are in <HOME>/jones-adversarial-pass/bbb-gap-note/check/defence/.\n\nThe five assigned defences:\n(1) A hypothesis fails for the note's Φ. FAILS.\n- Prop. 6.7 needs only that Φ is a proper product Φ′·Γ1 (p.20, l.1031). Kernel membership is never used: the proof of Thm 6.9 is a direct proof.\n- The non-parity case in which Prop. 6.7's proof starts is forced here: Lemma 2 gives M_Φ(−1) = 0 while ι > 0.\n- Γ1 begins with y2⁻¹. Reading Fig 6.3 in the basis of Fig 6.13 gives Γ1 = y2⁻¹y1⁻¹y2²y3⁻¹y2⁻¹y1y2.\n- Criterion-free version: by Lemmas 1–2, every conjugate of Φ0 of the form Φ′·Γ1 contradicts Prop 6.7. So either the conjugation step of Thm 6.9 or Prop 6.7 fails for Φ0.\n\n(2) Cor 6.8 or Thm 6.9 uses more than coefficient sums. FAILS. Cor 6.8 (p.24, l.1195–1214) uses M−, M+ only as summation limits. In any case the contradiction is with Prop 6.7's own conclusion.\n\n(3) Lemma 2 fails for the paper's conventions. FAILS. The argument works in either composition order, since (t+1)H is preserved on either side. Planar computation: |M_X(−1)| = |M_YX(−1)| = |M_XY(−1)| for 60 random X with Y = [Δ3⁴, A34], while ι changes (for example 12 → 1004).\n\n(4) Parity does not force |M(−1)| = m under the paper's definitions. FAILS.\n- The disks of the disk sequence are exactly the disks of Lemma 3.1 (p.6). Only parities matter.\n- On 6412 disks, k_{i+1} − k_i = W_i always and Lemma 1 never fails.\n- My model reproduces Lemma 6.1 exactly.\n- The Section 7 values are 2 (non-parity), 8 and −20.\n\n(5) The Main Theorem does not route kernel elements through Prop 6.7/Cor 6.8. FAILS. Every nontrivial Brunnian Φ is conjugated, then sent through Cor 6.8 and Thm 2.3 (p.24–25).\n\nExtra defences: also fail. These were \"f differs because of where p5 sits\", \"Γ is a different object\", and \"Φ0's conjugates are never proper\".\n\nNew computational evidence:\n- Lemma 6.3's disk list and the {p1,p2,p3} 3-disk claim hold for all 400 products Φ′·Γ1 that meet the paper's word criterion. Random K4 elements violate the list 25% of the time, so the test is not vacuous.\n- The small proper product S = Γ1⁻¹[Δ3⁴, A34]Γ1 is trivial at t = −1 but not Brunnian. It has m = 33320, 312 4-disks, every other disk is in the Lemma 6.3 list, and M(−1) = 0.\n- So for S the inputs that the D5 part of Prop 6.7's proof takes from the hypothesis hold, and that D5 part must fail.\n- The proof of the \"Furthermore\" clause (p.22, l.1100–1107) checks only the ι inequality. It never checks that the modified Γ′ keeps parity, which Cor 6.8 needs. By Lemmas 1–2, Γ′ must lose parity whenever the earlier parity claims hold.\n\nAll of the note's Φ0 facts are confirmed independently, in both matrix conventions: pure, Brunnian, ρ_4 and ρ_5 trivial at t = −1, depth exactly 1, Φ0 = [δ⁻², b].\n\nFixes needed:\n- Major:\n  - The headline \"meets every hypothesis\" rests on the paper's unproved criterion; state the dichotomy instead.\n  - Remove the \"independent hostile referees\", \"chat\" and local-path wording.\n  - Fix the §5 localization: what fails is parity of Γ′, not the inequality.\n- Minor:\n  - §3 \"never reaches a kernel element\" is vacuous; say the chain proves a false stronger statement.\n  - Restrict Lemma 2's scope and separate its two justifications.\n  - Replace the Torelli heuristic with ρ(Δ3⁴) − I = (1+t³)(ρ(Δ3²) − I).\n  - Correct the strand-3 deletion sentence.\n  - Prop 5.1 is used in Lemma 6.2's proof.\n  - The §6 \"finitely many moments\" sentence is false; add the depth tower.\n  - The f(Φ)·Γ remark should cite the paper's \"any K_j\" sentence.\n- Wording: the misquote \"ι ≠ ι\"; \"stabilization\"; \"±t^k\"; \"open again\"."
## findings (13)

### F1 [major] Claim paragraph (line 9) and §4 'Conclusion' (line 71)
- **claim**: An explicit nontrivial Brunnian 4-braid that is trivial at t = -1 meets every hypothesis of Prop. 6.7 and Cor. 6.8, so the argument fails on it.
- **problem**: This is stated without condition. That Φ′·Γ1 is a proper product rests only on the word criterion asserted without proof in the proof of Thm 6.9, and the note's own §4 admits that Conditions 1 and 2 were not checked. An author can reply that the note has not shown its Φ meets the hypotheses.
- **evidence**: Paper p.24, l.1231–1234: 'if the juxtaposition of the two words (yielding the product Φ·Γ1) is also a freely reduced word with respect to this free basis, then the second condition for Φ·Γ1 to be a proper product is immediately satisfied' (asserted, not proved). Note line 69: 'We could not check Conditions 1 and 2 directly'. My computations support the criterion but do not prove it: Lemma 6.3's conclusion holds for 400 products that meet it (lemma63.out).
- **fix**: Lead with the criterion-free dichotomy. By Lemmas 1–2, every conjugate of Φ0 that is a proper product Φ′·Γ1 contradicts Prop 6.7. So either no such conjugate exists, contradicting the conjugation step (p.2, l.78–79; p.25, l.1239–1240), or Prop 6.7 fails. Then present gΦ0g⁻¹ as the conjugate that the paper's own criterion certifies.

### F2 [major] 'Status' (line 11), 'Verification' (lines 93–111), §6 (line 91), §4 (lines 50, 69)
- **claim**: 'Three independent hostile referees ... found no refutation'; 'A separate chat independently recomputed Φ0'; 'suggested by the breakthrough chat'; 'bbb-gap/phi0_check.py'; 'because the figures are not in our text'.
- **problem**: In a public account, this would present internal automated review passes as independent refereeing and cites chats and files the authors cannot see. The figures excuse is odd, since the figures are in the PDF. This is an embarrassment and credibility risk, not a math error.
- **evidence**: Note lines 11, 50, 69, 91, 95–111.
- **fix**: Delete these passages. Say once, plainly, how the computations were done, and attach the code or give the braid words and matrices. Replace the figures excuse with 'We have not verified Conditions 1 and 2 directly.'

### F3 [major] §5 'Where the failure can be' (lines 75–79)
- **claim**: At least one of the following is false: the shortcut criterion, or Prop. 6.7 through its parity claims (Lemmas 6.2 to 6.6) or its 'Furthermore' inequality. If the parity lemmas hold, the 'Furthermore' clause is what fails.
- **problem**: 1. This reads as if the inequality itself cannot be achieved. It can: the proof makes ι(α,(β*_3)Γ′) larger. What fails is keeping parity for the same loop.
2. The note misses the explicit textual gap: the proof of the Furthermore clause never re-checks that Γ′ satisfies parity or is properly simple modulo 4-disks, or that f(Φ)·Γ′ satisfies parity or is proper.
3. Also never verified in Prop 6.7's proof: that f(Φ)·Γ is proper, condition (3) of 'properly simple', and the existence of a γ2 that avoids all other disks.
- **evidence**: p.22, l.1100–1101: 'We note that it is sufficient to find such an arc γ2′ satisfying the following two properties' (an ι inequality, and the β-crossings come after the α-crossings). Cor 6.8, p.24, l.1196: 'By Proposition 6.7, both Γ and Φ · Γ satisfy the parity condition', which is needed for the same Γ as the ι inequality. Computation (phi0_arc.out): for S = Γ1⁻¹[Δ3⁴,A34]Γ1, which is trivial at t = −1, the Lemma 6.3 list and the 3-disk hold. So the D5 part must fail.
- **fix**: State it as follows. For Φ trivial at t = −1: if the unmodified Γ satisfies parity (Lemmas 6.4, 6.6), then ι(Γ) = ι(f(Φ)Γ). The modified Γ′ then has |M_Γ′(−1)| = ι(f(Φ)Γ′) < ι(Γ′), so it violates parity, which the proof never checks. Otherwise the failure is already in Lemma 6.4 or 6.6, or in the existence of γ1, γ2. Optionally add that Lemma 6.3 and the 3-disk claim survive direct computation.

### F4 [minor] §3 (line 41)
- **claim**: The chain Prop. 6.7 → Cor. 6.8 → Thm. 2.3 therefore never reaches a kernel element.
- **problem**: If the theorem were true this would be vacuous, and it invites the reply 'there are none'. The real point is that the chain proves a strictly stronger statement, and that statement is false.
- **evidence**: The proof of Thm 6.9 is a direct proof (p.24, l.1223; p.25, l.1250–1251).
- **fix**: 'If valid, the chain proves that every nontrivial Φ ∈ Brun4 has ρ_4(Φ) ≠ I at t = −1. Φ0 refutes this.'

### F5 [minor] §2 Lemma 2 (lines 27–35)
- **claim**: 'If ρ_n(Y) = I at t = −1, then M_YX(−1) = ±M_X(−1) for every X ∈ B_n' and 'This holds in either composition convention, because the hypothesis is invariant under transpose, inverse and t ↦ 1/t.'
- **problem**: (a) The paper's M(α,β) is defined only when β avoids the endpoints of α, so 'every X' is too broad. (b) The justification mixes two points. The composition order is handled because (t+1)H is preserved on either side. Invariance under transpose, inverse and t ↦ 1/t only makes the hypothesis independent of the matrix convention.
- **evidence**: p.4, l.172–173: 'we will always choose our arcs so that the endpoints of α are disjoint from those of β'. The lemma itself is confirmed in the planar model: for 60 random pure X with Y = [Δ3⁴,A34], |M_X(−1)| = |M_YX(−1)| = |M_XY(−1)| (test_curves.out).
- **fix**: State it for Y pure and X fixing p3, which covers Y = f(Φ) and X = Γ. Give the two reasons separately.

### F6 [minor] §4 'Why it holds' (line 51)
- **claim**: 'By the 2-chain relation it lifts to a Dehn twist about a separating curve in the double branched cover. So it lies in the braid Torelli group'.
- **problem**: This heuristic explains why the reduced (symplectic) action is trivial. It does not explain triviality of the unreduced ρ_4, which Lemma 2 uses.
- **evidence**: Exact identity ρ(Δ3⁴) − I = (1 + t³)(ρ(Δ3²) − I), checked in the standard and homological conventions for n = 3, 4 (identity_D34.out).
- **fix**: Replace the heuristic with this identity. Since Φ0 = [Δ3⁴, b], it gives ρ_4(Φ0) ≡ I mod (t+1) (even mod 1 + t³) in one line.

### F7 [minor] §4 'Pure and Brunnian' (line 49)
- **claim**: 'Deleting strand i ≤ 3 kills A_{i4}, and with it the inner commutator.'
- **problem**: Wrong for i = 3. Deleting strand 3 kills A34, so the outer commutator collapses, while the inner commutator [A14,A24] survives.
- **evidence**: b = [[A14,A24],A34]. That Φ0 is Brunnian is confirmed: each deleted word has Burau_3 = I, and Burau_3 is faithful (phi0_facts.out).
- **fix**: 'For i = 1, 2 the inner commutator dies; for i = 3, A34 dies; either way b ↦ 1.'

### F8 [minor] §5 (line 79)
- **claim**: 'Prop. 5.1 is not a suspect, because Lemma 1 gives minimal position from parity alone.'
- **problem**: Overstated. Lemma 1 removes Prop 5.1 only from Cor 6.8. Prop 5.1 is also used in the proof of Lemma 6.2, which feeds Lemma 6.3.
- **evidence**: p.16, l.798–800: 'By Proposition 5.1, we may choose a representative of β′ so that (β′)Γ is in minimal position with respect to α.'
- **fix**: Write 'Cor 6.8 does not need Prop 5.1', and optionally add that Lemma 6.3's conclusion survives direct computation.

### F9 [minor] §6 (lines 87–91)
- **claim**: 'A repair needs a statistic that finitely many moments at t = −1 do not determine' and 'nontrivial Brunnian braids occur at every depth'.
- **problem**: 1. False as written: a multiset of size m is determined by its first m power sums.
2. Moments are meaningful only up to translation, because M is normalized only up to a power of t.
3. 'm' is reused for the depth.
4. The every-depth claim is asserted without proof.
- **evidence**: Newton's identities. depth_tower.out: Φ_k = [Δ3⁴, Φ_{k−1}] is pure, Brunnian, nontrivial, with (t+1)-adic depth exactly k for k = 1..4.
- **fix**: Say 'not controlled by congruences mod (t+1)^k for any fixed k', use central moments, rename the depth variable, and add the tower Φ_k.

### F10 [minor] §5 second remark (line 83)
- **claim**: 'the definition and Prop. 5.1 require the first factor to lie in K_5, and f(Φ) does not.'
- **problem**: Fair, but it ignores the paper's sentence allowing any K_j. The mismatch remains: f(Φ) lies in the p4-push subgroup of B5, while Γ is based at p5. The proof of Prop 6.7 also never verifies that f(Φ)·Γ is proper.
- **evidence**: p.9, l.428–429: 'The results in this section hold if we replace Kn with any other point-pushing subgroup Kj where j ≥ 4.'
- **fix**: Add one clause acknowledging that sentence and noting that properness of f(Φ)·Γ is never argued.

### F11 [wording] §3 (line 39)
- **claim**: Quoted as: "By Proposition 6.7 we can assume that ι ≠ ι. The result follows."
- **problem**: This misquotes the paper by dropping the arguments of ι inside quotation marks.
- **evidence**: p.24, l.1214: 'By Proposition 6.7 we can assume that ι(α, (β∗3)(f(Φ)·Γ)) ≠ ι(α, (β∗3)Γ).'
- **fix**: Quote the sentence exactly, or paraphrase without quotation marks.

### F12 [wording] Notation block (lines 5, 7)
- **claim**: 'f : B_4 → B_5 is the stabilization'; 'M_Φ ... defined up to a unit ±t^k'.
- **problem**: 'Stabilization' suggests Markov stabilization. The paper's M is defined up to a power of t, not ±t^k.
- **evidence**: p.3, l.140: 'the inclusion map corresponding to the standard embedding of Dn into Dn+1'. p.4, l.173–174: 'only well defined up to multiplication by a power of t'.
- **fix**: Use 'inclusion' and 'up to a power of t (that is, up to sign at t = −1)'. Note that any embedding D4 ⊂ D5 gives an f conjugate to the standard one, so ρ_5(f(Φ)) ≡ I mod (t+1) is unaffected.

### F13 [wording] Claim paragraph (line 9)
- **claim**: 'It shows that the question is open again.'
- **problem**: Stronger than what is shown.
- **evidence**: The note proves a gap in the proof, not a counterexample to the theorem.
- **fix**: 'It shows that the proof, as written, does not establish the Main Theorem.'
## confirmed
[
 "Note Lemma 1 (parity makes ε_i(−1)^{k_i} constant, so |M(−1)| = m = ι). Checked against p.6, l.271–273 (W_i = ±k for the k-punctured disk Δ_i), Lemma 3.1 (l.295–299) and the parity definition (p.7, l.353–357). Re-derived from the covering space. On 6412 disks of random pure 4-braids: k_{i+1} − k_i = W_i every time, every disk is simple, zero Lemma 1 failures (check/defence/test_curves.out).",
 "Note Lemma 2. Consistent with p.3, l.131–138 (free Z[t^±1]-module), p.4, l.152–170 (equivariant intersection count) and p.5, l.229–231 (M well defined on the homology class). Pairing of the boundary-loop class with the lift of α = (1 − t^±1)M on 400 arcs. Planar test: Y = [Δ3⁴, A34] with 60 random pure X, in both orders, leaves |M(−1)| unchanged while ι changes, e.g. 12 → 1004 (test_curves.out).",
 "Cor 6.8 deduces M_f(Φ)Γ ≠ M_Γ from the coefficient sums alone; M−, M+ appear only as summation limits (p.24, l.1195–1214).",
 "Thm 6.9 sends every nontrivial Φ ∈ Brun4 through conjugation, Cor 6.8 and Thm 2.3, with no use of kernel membership (p.24–25, l.1223–1252). The Main Theorem follows via Prop 1.2 and Long's theorem (p.2, l.63–67).",
 "Φ0 facts (phi0_facts.out), in both the standard unreduced and the homological (Fox) conventions: pure; Brunnian (each strand deletion gives a word whose Burau_3 image is I, and Burau_3 is faithful); ρ_4(Φ0) and ρ_5(f(Φ0)) equal I at t = −1 but not at t = 2 or 3; (t+1)-adic depth exactly 1.",
 "Φ0 = [δ⁻², b] with δ = Δ3⁻²Δ4² = A14A24A34 ∈ K4; conjugation by Δ3² equals conjugation by δ⁻¹ on K4 (phi0_facts.out).",
 "Γ1 begins with y2⁻¹: reading Fig 6.3 in the basis of Fig 6.13 gives the reduced word y2⁻¹y1⁻¹y2²y3⁻¹y2⁻¹y1y2. Its 5 crossings with α alternate in sign along α (p.24, l.1229–1230). This reading reproduces Lemma 6.3's five disk types exactly.",
 "The free reductions in note §4 (lines 58–61) are correct. Moreover Φ0's reduced y-word (length 30) begins and ends with y3⁻¹, so Γ1⁻¹Φ0Γ1 already meets the paper's criterion (phi0_arc.out).",
 "Section 7 values: M(−1) = 2 for the non-parity polynomial (8 terms); 8 and −20 for the parity polynomials (8 and 20 terms). The simplified polynomials match p.26–27 (sec7_check.out).",
 "Lemma 6.1 is reproduced exactly on 6412 disks, which validates the curve model (test_curves.out).",
 "Lemma 6.3's disk list and the 3-disk claim (p.22, l.1089–1090) hold for all 400 products Φ′·Γ1 meeting the word criterion. Random K4 elements violate the list 25% of the time (lemma63.out, k4_types.out).",
 "Example S = Γ1⁻¹[y3⁻², y1]Γ1, which equals Γ1⁻¹[Δ3⁴, A34]Γ1, meets the criterion and has ρ_4 ≡ I mod (t+1). Its arc has m = 33320 and 312 4-disks; every other disk is in the Lemma 6.3 list; a 3-disk is present; M(−1) = 0; c_i flips exactly at the 4-disks (phi0_arc.out).",
 "Prop 6.7's proof assumes Φ fails parity (p.20, l.1040). This case is forced for any Φ trivial at t = −1, since then M_Φ(−1) = 0 while ι > 0.",
 "The proof of the 'Furthermore' clause checks only two properties of Γ′ and never re-checks parity (p.22, l.1100–1107).",
 "Identity ρ(Δ3⁴) − I = (1 + t³)(ρ(Δ3²) − I) holds exactly (identity_D34.out).",
 "The tower Φ_k = [Δ3⁴, Φ_{k−1}] consists of nontrivial Brunnian braids of depth exactly k for k = 1..4 (depth_tower.out)."
]
## not_checked
[
 "Conditions 1 and 2 of 'proper product', checked directly on the geometry, for Φ0's conjugate or for S. Only the paper's word criterion and Lemma 6.3's conclusion were checked.",
 "The D5 construction in Prop 6.7 (q, γ1, γ2, γ′, γ″) and Lemmas 6.4–6.6. So I cannot say which D5 step fails first: Lemma 6.4, Lemma 6.6, the existence of Γ, or only the 'Furthermore' step.",
 "Lemma 6.3 on the Brunnian conjugate Γ1⁻¹Φ0Γ1 itself. Its y-word has length 46 and the arc was too large for pure Python, so the run was aborted.",
 "Nesting of 4-disks (a claim of the paper).",
 "Whittlesey and Lee–Song (the pseudo-Anosov input, ι > 0); for S, ι > 0 was computed directly.",
 "Long's theorem and Prop 1.2.",
 "Whether the span idea in note §6 is viable.",
 "report.md was not saved: the harness blocks subagents from writing report files, so the full report is in this structured output."
]
## cleanest_statement
"Let ρ_n be the unreduced Burau representation, let Δ3² = (σ1σ2)³, and let Φ0 = [Δ3⁴, [[A14, A24], A34]] ∈ B4. Then Φ0 is a nontrivial Brunnian braid and ρ_4(Φ0) ≡ I mod (t+1), because ρ_4(Δ3⁴) − I = (1 + t³)(ρ_4(Δ3²) − I). Two elementary facts hold for the paper's Moody polynomial M_X = M(α, (β*_3)X). (A) If X satisfies the parity condition, then by Lemma 3.1 and |W_i| = |P(Δ_i)| the sign ε_i(−1)^{k_i} is constant, so |M_X(−1)| = m = ι(α, (β*_3)X). (B) (1 − t^{±1})M_X is the Z[t^{±1}]-linear equivariant pairing of the class of (β*_3)X in H_1(D̃_n, {p̃*}) with the lift of α; so if Y is pure with ρ_n(Y) ≡ I mod (t+1), then M_YX(−1) = ±M_X(−1) for every X fixing p3. Consequently, for every Φ ∈ B4 with ρ_4(Φ) ≡ I mod (t+1), no Γ ∈ B5 makes both f(Φ)·Γ and Γ satisfy the parity condition with ι(α, (β*_3)f(Φ)Γ) ≠ ι(α, (β*_3)Γ). So the conclusion of Prop. 6.7, in the form Cor. 6.8 uses it, fails for every such Φ that meets its hypothesis. The proof of Thm. 6.9 applies Prop. 6.7 to a conjugate Φ = Φ′·Γ1 of each nontrivial Φ ∈ Brun4. Hence for Φ0 either no such conjugate exists, contrary to the conjugation step of that proof, or Prop. 6.7 fails for it. The paper's own free-reduction criterion supplies such a conjugate (gΦ0g⁻¹ with g = Γ1⁻¹y1^m), which places Φ0 in the second case. Either way the proof of Thm. 6.9, and with it the proof of the Main Theorem, is incomplete as written. Inside the proof of Prop. 6.7, the 'Furthermore' step replaces Γ by a modified loop Γ′ and checks only the ι inequality. It never checks that Γ′ still satisfies the parity condition, which Cor. 6.8 needs, and by (A) and (B) this must fail when ρ_4(Φ) ≡ I mod (t+1) and the other parity claims hold. None of this shows that ρ_4 is unfaithful."

## VERIFY
{
 "verdicts": [
  {
   "claim": "Finding 1 (Claim l.9, Conclusion l.71): the note says without condition that its explicit Brunnian braid meets every hypothesis of Prop 6.7 and Cor 6.8. But the proper-product property rests only on the word criterion that the paper asserts without proof in Thm 6.9, and the note admits it did not check Conditions 1 and 2.",
   "verdict": "REAL",
   "evidence": "**Note.** l.9 says the braid \"meets every hypothesis of Prop. 6.7 and Cor. 6.8\". l.71 says \"It therefore meets every hypothesis\". Yet l.69 rests this only on the criterion (\"By that criterion Φ = Φ′·Γ1 is a proper product. We could not check Conditions 1 and 2 directly\"), and §5 (l.76) concedes the criterion may fail.\n\n**Paper.** p.24 l.1231-1234 asserts the criterion: \"then the second condition for Φ · Γ1 to be a proper product is immediately satisfied\". The only support is the remark that Γ1 begins with y2^-1 (p.25 l.1238), which does not touch the geometric content of Condition 2.\n\n**The referee's dichotomy holds.** Every B4-conjugate Ψ of Φ0 is trivial at t=-1.\n- If some Ψ = Φ′·Γ1 is proper, Prop 6.7 plus Lemma 1 give |M_{f(Ψ)Γ}(-1)| = ι(f(Ψ)Γ) ≠ ι(Γ) = |M_Γ(-1)|, against Lemma 2.\n- If none is proper, the conjugation step fails for Φ0: p.25 l.1238-1240 (\"Thus we may assume that Φ has been conjugated so that it can be written as a proper product Φ = Φ′ · Γ1\") and p.2 l.78-79.\n\n**Free reduction.** I re-verified the note's free reductions; see extra_checks.out (b).\n\n**One overstatement by the referee.** The 400-product Lemma 6.3 test does not 'support' the criterion. The Lemma 6.3 list also holds when the criterion fails: defence lemma63_discriminate.out, and my extra_checks.out (c), with 0 violations in 36 products that fail the criterion.",
   "required_change": "Replace the unconditional sentence at l.9 and l.71 with the criterion-free dichotomy:\n\n> \"Every conjugate of Φ0 is trivial at t = -1, so by Lemmas 1-2 none can satisfy the conclusion of Prop. 6.7. Either no conjugate is a proper product Φ′·Γ1, and the conjugation step of Thm 6.9 (p.25) fails for Φ0, or one is, and Prop. 6.7 fails for it. The paper's own criterion (p.24) certifies gΦ0g^-1 as such a conjugate.\"\n\nOptionally add the criterion-free example S from finding 3. Do not cite the Lemma 6.3 test as evidence for the criterion."
  },
  {
   "claim": "Finding 2 (l.11, l.50, l.69, l.91, l.93-111): the note presents internal automated passes as 'three independent hostile referees', cites chats and bbb-gap/ file paths the authors cannot see, and gives an odd 'figures are not in our text' excuse.",
   "verdict": "REAL",
   "evidence": "All the passages are present:\n- l.11: \"Three independent hostile referees ...\"\n- l.50: \"bbb-gap/phi0_check.py\"\n- l.69: \"because the figures are not in our text\"\n- l.91: \"suggested by the breakthrough chat\"\n- l.95-97: the referee lenses and script paths\n- l.109: \"A separate chat independently recomputed Φ0\"\n\n**Figures.** The figures are in the PDF: Fig 6.3 on p.16 and Fig 6.13 on p.25 (page images; imgs/fig6-3.png and imgs/fig6-13.png). The construction lens of this check used them (check/construction/gamma1_annotated.png, fig613_full.png). The real obstacle to checking Conditions 1-2 is size, not missing figures: S alone has ι = 33,320, and gΦ0g^-1 is far longer.\n\n**Credibility.** The authors cannot see or evaluate these internal passes or chats. Calling these AI passes independent human referees would misrepresent them. This is a credibility risk, not a math error.",
   "required_change": "- Delete the Status paragraph (l.11), the referee and chat narrative in Verification (l.93-109), and \"suggested by the breakthrough chat\" (l.91).\n- Replace the bbb-gap/... paths (l.50, l.96-97) with attached code, or with the braid words and matrices in an appendix.\n- Replace l.69's excuse with \"We have not verified Conditions 1 and 2 directly.\"\n- Keep one honest line saying what was not checked: Conditions 1-2 directly, and the case analyses of Lemmas 6.3 and 6.6.\n- If AI assistance is mentioned at all, describe it plainly, not as refereeing."
  },
  {
   "claim": "Finding 3 (§5, l.75-79): the note's suspect list misplaces the failure. The 'Furthermore' inequality itself is achievable; what fails is keeping parity for the same loop. The proof never re-checks parity or properly-simple for Γ′, and also leaves unverified that f(Φ)·Γ is proper, condition (3), and the existence of γ2.",
   "verdict": "REAL",
   "evidence": "**The textual gap.**\n- p.22 l.1092: \"It remains to show that we can always choose Γ to ensure the following statement holds\".\n- l.1100-1101: \"We note that it is sufficient to find such an arc γ2′ satisfying the following two properties\". The two properties give only the ι inequality.\n- Neither Case 1 (p.22 l.1122-1123) nor Case 2 (p.23 l.1174-1176) re-establishes parity or 'properly simple modulo 4-disks' for Γ′.\n- Cor 6.8 needs both for the same loop: p.24 l.1196 \"By Proposition 6.7, both Γ and Φ · Γ satisfy the parity condition\", and the inequality at l.1214.\n- For the unmodified Γ, only conditions (1) and (2) are checked (p.22 l.1088-1090). Condition (3) and 'simple mod 4-disks' are not.\n- The existence of q and γ2 (p.21-22) is asserted without argument.\n\n**Sharper logic, which I verified.** Let Φ be trivial at t=-1 with a disk sequence on the Lemma 6.3 list. Take any loop Λ disjoint from β modulo 4-disks; both Γ and Γ′ qualify, since γ1, γ′, γ″ avoid β and property 1 puts every β-crossing last.\n- Lemmas 6.3 and 6.4, then Lemmas 1 and 2, give |M_Λ(-1)| = ι(f(Φ)Λ).\n- So Λ satisfies parity only if ι(Λ) = ι(f(Φ)Λ), and parity and the inequality are incompatible.\n\n**Independent computation.** I reran the defence's S with a fresh implementation (different cut system, my own Artin action, validated by a multivariable Fox identity and by Lemma 6.1 on every disk).\n- S is trivial at t=-1 (homological and standard Burau) and not trivial at t=2 or t=3.\n- ι = 33,320, with 312 4-disks.\n- No disk is off the Lemma 6.3 list, and a {p1,p2,p3}-disk is present.\n- M_S(-1) = 0.\n\nThe D5 part uses properness only through these facts. So it fails on S, regardless of the shortcut criterion or the reading of Fig 6.3.\n\n**Errors in the referee's version.**\n- 'f(Φ)·Γ′ parity' is not a real gap: Lemma 6.4 applies to Γ′.\n- 'f(Φ)·Γ proper' is already in the note (l.83) and is not needed for the contradiction.\n- The outward part of γ2 follows from the band structure, since α lies in the closure of every 4-disk. Only its start at q is unargued.\n- '=' should be '≤', unless Lemma 6.4 is invoked for Γ′.\n- The 'Otherwise' list omits Lemma 6.3, Lemma 6.5 and the unverified hypotheses.",
   "required_change": "Replace l.75-79 with the following.\n\n> Let Φ = Φ′·Γ1 be a proper product with ρ4(Φ) = I at t = -1. Let Λ ∈ K5 be any loop that is disjoint from β modulo 4-disks. This includes Γ = γ2∘γ1 and the modified Γ′. By Lemmas 6.3 and 6.4, f(Φ)·Λ satisfies parity, so |M_Λ(-1)| = ι(f(Φ)Λ) by Lemmas 1 and 2. Hence Λ satisfies parity only if ι(Λ) = ι(f(Φ)Λ).\n>\n> If Γ satisfies parity (Lemma 6.6), the equality holds, so the proof passes to Γ′. Properties 1 and 2 (p.22) then give |M_Γ′(-1)| = ι(f(Φ)Γ) = ι(Γ) < ι(Γ′), so Γ′ violates parity. The proof never re-checks this, and Cor. 6.8 needs parity and the inequality for one loop.\n>\n> Otherwise the failure is earlier: in Lemma 6.3, 6.4, 6.5 or 6.6; in the unverified hypotheses (simple mod 4-disks, condition (3), condition (1) 'by construction'); or in the existence of q, γ1, γ2.\n\nThen:\n- Add S = Γ1^-1[Δ3^4, A34]Γ1, with its code, as a criterion-free example on which the D5 part fails.\n- Delete \"If the parity lemmas hold, the 'Furthermore' clause of Prop. 6.7 is what fails.\""
  }
 ],
 "summary": "All three of the defence referee's findings are REAL. None of them threatens the note's mathematical core (Lemmas 1-2 and the §3 logic). Each needs a specific change before the note is finalized.\n\n**1. Unconditional headline (REAL).** The Claim (l.9) and the Conclusion (l.71) are unconditional, but the proper-product status of Φ = Φ′·Γ1 rests only on the paper's unproved word criterion (p.24 l.1231-1234), which the note itself concedes (l.69, l.76).\n- The referee's criterion-free dichotomy is valid. Either no B4-conjugate of Φ0 is a proper product, and the conjugation step fails (p.25 l.1238-1240; p.2 l.78-79), or one is, and Prop 6.7 fails for it.\n- One overstatement by the referee: the 400-product Lemma 6.3 test does not support the criterion. The Lemma 6.3 list also holds for products that fail it (their own discriminate run; my check: 0 violations in 36 such products).\n\n**2. Internal references (REAL).** The note calls internal passes \"independent hostile referees\", cites \"chats\" and bbb-gap/ file paths, and says Conditions 1-2 were unchecked \"because the figures are not in our text\". The figures are in the PDF (Fig 6.3 on p.16, Fig 6.13 on p.25), and this check's construction lens used them.\n- Delete these passages.\n- Attach the code, or give the braid words and matrices.\n- Say plainly: \"We have not verified Conditions 1 and 2 directly.\"\n\n**3. §5 misplaces the failure (REAL, with corrections).** The paper says two properties of γ2′ are \"sufficient\" (p.22 l.1100-1101), but they give only the ι inequality. Parity, and 'properly simple modulo 4-disks', are never re-checked for Γ′ (p.22-23). Cor 6.8 needs parity and the inequality for the same loop (p.24 l.1196, l.1214).\n- **Sharper version.** For Φ trivial at t=-1 with a disk sequence on the Lemma 6.3 list, every loop Λ disjoint from β modulo 4-disks (both Γ and Γ′ are) satisfies |M_Λ(-1)| = ι(f(Φ)Λ), by Lemmas 6.4, 1 and 2. So parity of Λ forces ι(Λ) = ι(f(Φ)Λ), and the two requirements are incompatible.\n- **Corrections to the referee's fix:**\n  - f(Φ)·Γ′ parity is not a real gap.\n  - 'f(Φ)·Γ proper' is already in the note.\n  - The outward part of γ2 follows from the band structure.\n  - '=' should be '≤', unless Lemma 6.4 is invoked for Γ′.\n  - The 'Otherwise' list must add Lemma 6.3, Lemma 6.5 and the unverified hypotheses.\n\n**Independent computation.** I reproduced the referee's S = Γ1^-1[Δ3^4, A34]Γ1 exactly, with a separate implementation (different cut system, my own Artin action, validated by a multivariable Fox identity and by Lemma 6.1 on every disk).\n- S is trivial at t=-1 and not at t=2 or t=3.\n- ι = 33,320, with 312 4-disks.\n- No disk is off the Lemma 6.3 list, and a {p1,p2,p3}-disk is present.\n- M_S(-1) = 0.\n\nSo the D5 part of Prop 6.7's proof fails on S, independent of the shortcut criterion and of the reading of Fig 6.3. I recommend adding S to the note as a criterion-free example.\n\n**Further checks.**\n- Lemma 2 planar test: 0 mismatches in 40 cases.\n- Φ0's y-word equals the note's σ-word as a mapping class.\n- The note's free reductions hold.\n\n**Files.** Scripts and outputs are in <HOME>/jones-adversarial-pass/bbb-gap-note/check/verify-defence/: arcs_indep.py, arcs_indep.out, extra_checks.py and extra_checks.out. The harness refused the write of report.md (\"Subagents should return findings as text\"), so the full report is in this structured output instead.\n\n**Minor points.**\n- Note l.65's \"without proof\" is better put as \"with only a one-line justification\".\n- l.77 mislabels Lemmas 6.2-6.3 as parity claims."
}


######## LENS: lemmas

## verdict
"holds_with_fixes"
## findings (14)

### F1 [minor] §1, Lemma 1 statement (line 15)
- **claim**: Let φ satisfy the parity condition. Write M_φ = Σ ε_i t^{k_i} over the intersection points of α with a transverse representative of β ... Then ε_i(-1)^{k_i} does not depend on i. Hence |M_φ(-1)| = m.
- **problem**: The conclusion holds only for the representative whose disk sequence satisfies parity. For an arbitrary transverse representative of a parity braid it is false: a finger move adds two consecutive points with the same exponent and opposite signs. The paper's parity condition belongs to a disk sequence, and the paper takes that sequence from a minimal representative.
- **evidence**: Paper p. 8, line 370: "where m = ι(α, β)". lemma1_sec6.py: the Fig. 3.1(b) arc (parity, m = 6, M(-1) = 6) after one finger move has m = 8 and M(-1) = 6, with two empty sign-changing disks (W = 0).
- **fix**: Write: "Let β be a transverse representative of (β*_3)φ whose disk sequence satisfies the parity condition, with intersection points q_1, ..., q_m in order along β." The minimal-position remark then stands. It also has a one-line direct proof: an innermost bigon is a disk Δ_i with P(Δ_i) empty, and such a disk is sign-changing, which parity forbids.

### F2 [minor] §3, first paragraph (line 39)
- **claim**: Quoted as "By Proposition 6.7 we can assume that ι ≠ ι. The result follows."
- **problem**: This is a misquotation. The arguments of ι were dropped inside quotation marks, and "ι ≠ ι" reads as a typo or as a jibe in a note sent to the authors.
- **evidence**: Paper p. 24, line 1214: "By Proposition 6.7 we can assume that ι(α, (β∗3)(f(Φ)·Γ)) ≠ ι(α, (β∗3)Γ)."
- **fix**: Quote the sentence in full with its arguments, or paraphrase it without quotation marks.

### F3 [minor] §3, last paragraph (line 41)
- **claim**: The chain Prop. 6.7 → Cor. 6.8 → Thm. 2.3 therefore never reaches a kernel element. Any braid that meets its hypotheses and is trivial at t = -1 is a counterexample to it.
- **problem**: A proof by contradiction is meant never to reach a kernel element, so the first sentence is no objection on its own. The real defect is that Prop. 6.7, with Lemmas 1 and 2, implies the stronger statement ρ_4(Φ) ≢ I mod (t+1), and that statement is false. "A counterexample to it" names the whole chain. The chain includes Thm. 2.3, which is Moody's criterion and is correct, and the statement of Cor. 6.8, which a braid trivial at t = -1 does not contradict. Only Prop. 6.7's conclusion (parity for both braids together with the ι inequality) is contradicted.
- **evidence**: Logic of the note's §3 together with paper p. 24 (proof of Cor. 6.8) and p. 25, lines 1250-1251 (Thm. 6.9 cites Cor. 6.8, then Thm. 2.3).
- **fix**: Suggested text: "So wherever Prop. 6.7 applies, it implies ρ_4(Φ) ≢ I mod (t+1). Thm. 6.9 does not need this, and it is false for some nontrivial Brunnian braids (§4). Any Φ that meets the hypotheses of Prop. 6.7 and is trivial at t = -1 is a counterexample to Prop. 6.7."

### F4 [minor] Claim paragraph (line 9), as it feeds the §3 deduction
- **claim**: An explicit nontrivial Brunnian 4-braid that is trivial at t = -1 meets every hypothesis of Prop. 6.7 and Cor. 6.8, so the argument fails on it.
- **problem**: The note establishes the proper-product hypothesis only through the unproved criterion in the proof of Thm. 6.9, so the headline claims more than the body. The conclusion "the argument fails on it" is still right, because that criterion is part of the paper's argument, but the hypothesis claim is conditional.
- **evidence**: The note's own §4: "We could not check Conditions 1 and 2 directly." The note's §5 states the dichotomy correctly.
- **fix**: Write: "... meets every hypothesis of Prop. 6.7 and Cor. 6.8 by the proper-product criterion used in the proof of Thm. 6.9, so either that criterion or Prop. 6.7 fails on it."

### F5 [minor] §6, lines 89 and 91 (moment comparison and p'(1))
- **claim**: Since M^{(j)}(-1) = ±(-1)^j p^{(j)}(1), comparing the first m factorial moments p^{(j)}(1), j < m, cannot separate braids with ρ ≡ I mod (t+1)^m. ... the first moment p'(1) may already separate f(Φ0)Γ from Γ.
- **problem**: The identity is correct, but a moment comparison means something only at fixed lifts. The paper normalises the first crossing to ±t^0, and under that normalisation the exponents of f(Φ)Γ and of Γ carry unrelated shifts. Raw factorial moments can then differ even for a kernel element, and a difference in them certifies nothing. At order 1, only p'(1) mod p(1) is invariant under translation.
- **evidence**: Paper p. 4, line 175: "choose our lifts so that the first point at which β crosses α is assigned the monomial ±t^0". lemma1_sec6.py: shifting the exponents by d changes p'(1) by d·ι and leaves p'(1) mod p(1) fixed. lemma2_deep.py: for Y of depth 2, 3 and 4 and random pure X, the class-level arc data of YX, XY and X agree mod (t+1)^d and not to higher order. Dividing by 1 - t loses no (t+1)-adic order, because the two are coprime primes of Z[t^±1].
- **fix**: Fix α̃ and the lift of β from p̃* once and for all (the class-level normalisation that the proof of Thm. 2.3 uses). Then state: ρ_5(f(Φ)) ≡ I mod (t+1)^d implies M̂_{f(Φ)Γ} ≡ M̂_Γ mod (t+1)^d, so their factorial moments of order < d agree. With the paper's normalisation, say this holds up to a translation of the exponents. Change "p'(1) may already separate" to "p'(1), at fixed lifts, may already separate".

### F6 [minor] §6, line 91 ("every depth")
- **claim**: Elements of ker ρ_4 have infinite depth, though, and nontrivial Brunnian braids occur at every depth. So no comparison of moments of bounded order can work.
- **problem**: Depth is never defined, and the existence claim comes without an argument. The conclusion needs only arbitrarily large depth, which has a short proof. Exact depth d for every d is not proved.
- **evidence**: depth([A,B]) ≥ depth(A) + depth(B), since ρ(A)ρ(B) - ρ(B)ρ(A) = (t+1)^{a+b}(XY - YX). Brun_4 is free and normal in B_4. Φ0 and σ3Φ0σ3^{-1} do not commute (their commutator is not I at t = 2). So the left-normed commutators [Φ0,[Φ0,...,[Φ0,σ3Φ0σ3^{-1}]]] are nontrivial and have depth ≥ k+1. depth.py: Φ_1..Φ_4 have depths 2, 4, 6, 8 and are not I at t = 2 or t = 3. odd_depth2.py: nontrivial Brunnian braids of every exact depth 1 to 10 were found; exact_depth_xcheck.py rechecks depths 1 to 5 in exact Laurent arithmetic.
- **fix**: Define depth(Φ) = max{d : ρ_4(Φ) ≡ I mod (t+1)^d}. Write "nontrivial Brunnian braids of arbitrarily large finite depth exist" and add the two-line commutator argument.

### F7 [minor] §6, line 91 ("finitely many moments")
- **claim**: A repair needs a statistic that finitely many moments at t = -1 do not determine.
- **problem**: Taken literally this is false. A multiset of ι integers is determined by its first ι power sums (Newton's identities), so every statistic of the exponent multiset, the span included, is determined by finitely many moments. The depth argument only rules out an order bound that is uniform in Φ.
- **evidence**: lemma1_sec6.py: for d = 1 to 4 it exhibits pairs of multisets with equal power sums up to order d but spans d+2 and d+1.
- **fix**: Write: "A repair needs a statistic not determined by the moments up to any order fixed in advance, independent of Φ, such as the span."

### F8 [minor] §5, line 79 (uses the §1 minimal-position remark)
- **claim**: Prop. 5.1 is not a suspect, because Lemma 1 gives minimal position from parity alone.
- **problem**: Lemma 1 takes Prop. 5.1 out of the count step of Cor. 6.8 only. Prop. 5.1 is still used inside the proof of Lemma 6.2, and its terminology appears in Lemma 6.6. The proof of Lemma 6.1 also assumes minimal position. So a failure of Prop. 5.1 could still be what breaks the parity claims of Prop. 6.7.
- **evidence**: Paper p. 16, lines 798-799: "By Proposition 5.1, we may choose a representative of β′ so that (β′)Γ is in minimal position". p. 20, line 1005 (Lemma 6.6). p. 15, line 754 (Lemma 6.1).
- **fix**: Write: "Prop. 5.1 is not needed for the step from parity to 'coefficient sum = ι' in Cor. 6.8, since Lemma 1 gives minimal position from parity. It enters only through the proofs of Lemmas 6.2 to 6.6."

### F9 [minor] §2, Lemma 2 statement (line 27)
- **claim**: M_{YX}(-1) = ±M_X(-1) for every X ∈ B_n.
- **problem**: The paper sets up M only for arcs whose endpoints avoid those of α. The identity "noose pairing = (1 - t^{±1}) × arc polynomial" fails when X(p_3) ∈ {p_1, p_2}, because the noose's small circle then crosses α. This is harmless for the application, where X = Γ ∈ K_5 is pure.
- **evidence**: Paper p. 4, line 173: "we will always choose our arcs so that the endpoints of α are disjoint from those of β".
- **fix**: Write "for every X ∈ B_n with X(p_3) = p_3 (in particular every pure X)".

### F10 [wording] §2, Lemma 2 last paragraph (line 35)
- **claim**: This holds in either composition convention, because the hypothesis is invariant under transpose, inverse and t ↦ 1/t.
- **problem**: That invariance shows the hypothesis does not depend on the matrix convention. It says nothing about composition order. Order is already handled by the preceding paragraph: the class difference is (ρ(Y) - I) applied either before or after ρ(X), and in both cases it lies in (t+1)H.
- **evidence**: depth.py and lemma2_deep.py check both X·Y and Y·X against X.
- **fix**: Split this into two sentences. One says the argument works in both composition orders because the difference is (ρ(Y) - I) applied before or after ρ(X). The other says the hypothesis does not depend on the matrix convention, since it is invariant under transpose, inverse, change of basis and t ↦ 1/t.

### F11 [wording] Notation (line 7) and Lemma 2 proof (line 35)
- **claim**: M_Φ ... defined up to a unit ±t^k; "The ± comes from normalising M only up to ±t^k."
- **problem**: The paper defines M only up to a power of t. The orientations fix the sign. The ± in Lemma 2 is the factor t^k evaluated at t = -1.
- **evidence**: Paper p. 4, line 174: "only well defined up to multiplication by a power of t".
- **fix**: Write "up to a power of t", and "The ± is the factor t^k, which equals ±1 at t = -1."

### F12 [wording] §2, Lemma 2 proof, first two paragraphs (lines 29-31)
- **claim**: By the proof of Thm. 2.3, M_X is determined by a class ... Its pairing is (1 - t^{±1}) times the arc polynomial.
- **problem**: The fact that M depends only on the class is the remark on p. 5, which the proof of Thm. 2.3 uses. The pairing description and the factor 1 - t^{±1} are the note's own derivation. That derivation is correct, but the paper does not contain it, and the note gives no argument for it.
- **evidence**: Paper p. 5, lines 229-231: "MΦ is well defined on the homology class of a lift of [(β∗3)Φ]". My derivation: each point q_i gives two points of the noose on α, of opposite sign, on sheets that differ by t^{±1}. Fox-calculus form: the noose class is (1-t)·∂w + t^{e(w)}e_3. The matrix model agrees (entries (3,1) and (3,2) are divisible by 1 - t; σ2^{2k} gives a k-term single-sign series).
- **fix**: Cite the p. 5 remark. Add the one-line two-sheets derivation so the authors can check it.

### F13 [wording] §6 (lines 89-91)
- **claim**: "the first m factorial moments", "ρ ≡ I mod (t+1)^m"
- **problem**: The letter m is overloaded. In §1 it is the number of intersection points, and in §6 it is the depth bound.
- **evidence**: §1, line 15 versus §6, line 89.
- **fix**: Use d for the depth bound in §6.

### F14 [wording] Lines 11, 50, 91, 95-97, 109
- **claim**: "suggested by the breakthrough chat", "A separate chat independently recomputed", "Three independent hostile referees", local paths such as bbb-gap/phi0_check.py
- **problem**: These are internal references the authors cannot see or use, and "chat" and "hostile referees" read oddly in a note sent to them.
- **evidence**: Note text.
- **fix**: Remove these references, or attach the scripts and write "we checked".
## confirmed
[
 "|W_i| = |P(Δ_i)|: W_i = ±k for the k-punctured disk Δ_i (paper p. 6, lines 271-273), and P(Δ) is the set of interior marked points (p. 7). This also holds for a non-minimal representative, since α_i ∪ β_i is always a simple closed curve.",
 "Lemma 3.1 (p. 6, eq. (1)), W_i = k_{i+1} - k_i, agrees with Fig. 3.1(b): W = 1,1,-1,-2,1 gives the exponents 0,1,2,1,-1,0 of 2 - 2t + t^2 - t^{-1} (lemma1_sec6.py).",
 "Lemma 1's sign argument is correct: under parity, ε_i(-1)^{k_i} is constant, so |M(-1)| = m = Σ|coeff| and m = ι. Only 'ε_i ≠ ε_{i+1}' is used, so the sign convention is irrelevant. Checked on Fig. 3.1(a), Fig. 3.1(b) and both §7 parity polynomials (lemma1_sec6.py).",
 "The paper's set-up assumes a minimal representative: p. 8, line 370 (\"where m = ι(α, β)\") and p. 7, line 327 (proof of Thm. 4.1). The note's remark that a parity representative is automatically minimal is right, both via m = |M(-1)| ≤ ι ≤ m and directly: an innermost bigon is a Δ_i with no punctures, which is sign-changing.",
 "§7 values match the paper (pp. 26-27). M_Φ(-1) = 2 with 8 unsimplified terms and L1 = 6; its only parity-violating disk is the 4-disk, W = -4. M_ΦΓ(-1) = 8 with 8 terms. M_Γ(-1) = -20 with 20 terms. The simplified forms are as printed (lemma1_sec6.py).",
 "Lemma 2 structure is correct. The noose pairing with α̃ is sesquilinear with no denominators and equals (1 - t^{±1})·M, a factor of 2 at t = -1. The class difference lies in (t+1)H for both composition orders. Matrix model (depth.py): entries (3,1) and (3,2) of ρ(X) are divisible by 1 - t for 40 random pure X; σ2^{2k} gives 1 + t^2 + ... + t^{2k-2} (ι = k, one sign); quotients at t = -1 agree for X, Φ0·X and X·Φ0.",
 "Generalised Lemma 2 (lemma2_deep.py): if ρ(Y) ≡ I mod (t+1)^d, then the class-level arc data of YX and XY agree with those of X mod (t+1)^d, and only to that order, for d = 2, 3, 4.",
 "§3 deduction: Prop. 6.7 with Lemmas 1 and 2 forces ρ_5(f(Φ)) ≠ I at t = -1. The proof of Cor. 6.8 uses only the coefficient L1 norms (p. 24, lines 1194-1214). Thm. 6.9 goes through Cor. 6.8, then Thm. 2.3, then Obs. 2.1 (p. 25, lines 1250-1251).",
 "Obs. 2.1 (p. 3, lines 140-141) gives f(ker ρ_4) ⊂ ker ρ_5, and ρ_5(f(Φ0)) = ρ_4(Φ0) ⊕ 1 was checked in depth.py. The paper places p5 'in the interior of the disk D4' (p. 17, line 876). Any embedding-induced stabilisation is conjugate in B_5 to the standard one, up to conjugating Φ in B_4, so triviality at t = -1 and depth carry over.",
 "Φ0 (depth.py): ρ_4(Φ0) ≡ I mod (t+1), and ρ_4(Φ0) ≠ I at t = 2 and t = 3. Its (t+1)-adic depth is exactly 1 in unreduced Burau, with transposed generators, under t ↦ 1/t, for the inverse braid, for ρ_5∘f, and in reduced Burau. The factor (σ1σ2)^6 has depth 1; b has depth 0.",
 "The identity M^{(j)}(-1) = c(-1)^j p^{(j)}(1) for M(t) = c·p(-t) holds (300 random multisets, j < 6; lemma1_sec6.py).",
 "Elements of ker ρ_4 have infinite depth (trivially).",
 "Arbitrarily large depth occurs among nontrivial Brunnian braids. depth([A,B]) ≥ depth(A) + depth(B), and iterated commutators in the free group Brun_4 are nontrivial. Computed: Φ_1..Φ_4 have depths 2, 4, 6, 8 for three different conjugators (depth.py). Exact depths 1 to 10 all occur (odd_depth2.py); 1 to 5 were rechecked in exact Laurent arithmetic (exact_depth_xcheck.py).",
 "'BBB compare only p(1) = ι' is accurate: the proof of Cor. 6.8 names the extreme exponents M_- and M_+ but uses only the L1 norm (p. 24).",
 "Side consequence of the note's lemmas: Lemma 2 with X = 1 gives M_Y(-1) = 0 whenever ρ(Y) ≡ I mod (t+1), so no braid in the t = -1 kernel with ι > 0 satisfies parity. This is consistent with the paper's need for the push into B_5.",
 "Φ0 is Brunnian, by reasoning only: the word is pure, strand deletion is a homomorphism on PB_4, and each deletion kills b = [[A14,A24],A34]."
]
## not_checked
[
 "The §4 construction: free reductions in K_4, Conditions 1 and 2 of a proper product, the shortcut criterion in the proof of Thm. 6.9, and Figs. 6.3 and 6.13 (outside this lens).",
 "The internal case analyses of Lemmas 6.2-6.6 and the Γ' modification in the proof of Prop. 6.7 (Figs. 6.9-6.12).",
 "The Brunnian property of Φ0 and the 2-chain / separating-twist explanation of (σ1σ2)^6 were reasoned through, not recomputed; brunn.py was not rerun.",
 "Whether every exact depth d is realised; only d ≤ 10 was found computationally.",
 "The exact monomials ⟨x̃_1, α̃⟩ and ⟨x̃_2, α̃⟩ in the matrix model, and any comparison with a planar Moody computation beyond the σ2^{2k} family.",
 "The LaTeX version in note/bbb-gap-note.tex was not compared with BBB-GAP.md.",
 "The note's Verification and Status sections, and §5 beyond the Prop. 5.1 remark.",
 "report.md was not saved. The harness blocked writing report files from this subagent ('Subagents should return findings as text'), so the full report is this structured output. The scripts and their .out files are in <HOME>/jones-adversarial-pass/bbb-gap-note/check/lemmas/."
]
## summary
"Within this lens (Lemma 1, Lemma 2, the §3 deduction and the §6 remarks) the mathematics is correct and the gap argument stands. Parity forces ε_i(-1)^{k_i} to be constant, so |M(-1)| = ι and a parity representative is minimal. M_X is, up to t^k and the factor 1 - t^{±1} (2 at t = -1), a no-denominator pairing of ρ_n(X) applied to the noose class with α̃, so ρ(Y) ≡ I mod (t+1) gives |M_{YX}(-1)| = |M_X(-1)| in both composition orders. Hence Prop. 6.7 cannot hold for any braid that meets its hypotheses and is trivial at t = -1.\n\nExact computation confirms Φ0 is trivial at t = -1, not trivial at t = 2 or 3, and has depth exactly 1 in six conventions. It confirms the §7 numbers and the moment identity. It also finds nontrivial Brunnian braids of every exact depth from 1 to 10.\n\nNo fatal or major problems. Fixes needed:\n- State Lemma 1 for the parity representative; for an arbitrary transverse representative it is false.\n- Repair the garbled §3 quotation (\"ι ≠ ι\").\n- Reframe §3 so the target is Prop. 6.7 proving too much, not the whole chain, and make the headline conditional on the paper's proper-product criterion.\n- In §6, fix the lift normalisation before comparing moments, define depth and prove arbitrarily large depth, and rewrite the literally false \"statistic that finitely many moments do not determine\".\n- Soften \"Prop. 5.1 is not a suspect\".\n- Restrict Lemma 2 to X fixing p_3 and correct its composition-order justification.\n- Use \"power of t\" rather than \"±t^k\", and remove internal references.\n\nOptional courtesy typos in the paper: the Lemma 4.2 proof writes Σ|P(Δ)| = 0 for ΣW = 0 (p. 8), and §7 says \"increase\" where the exponents decrease (p. 26). report.md could not be written because the harness blocks report files from subagents; scripts and outputs are in <HOME>/jones-adversarial-pass/bbb-gap-note/check/lemmas/."
## cleanest_statement
"Let Φ ∈ K_4 meet the hypotheses of Prop. 6.7 and Cor. 6.8, and suppose ρ_4(Φ) ≡ I mod (t+1). Let Γ ∈ K_5 be as asserted in Prop. 6.7. Then f(Φ)·Γ and Γ satisfy the parity condition, so by Lemma 1, applied to their parity representatives, |M_{f(Φ)Γ}(-1)| = ι(α, (β*_3)f(Φ)Γ) and |M_Γ(-1)| = ι(α, (β*_3)Γ). Since ρ_5(f(Φ)) is conjugate to ρ_4(Φ) ⊕ 1 and so is ≡ I mod (t+1), and since M_X is, up to t^k and the factor 1 - t^{±1} (equal to 2 at t = -1), the equivariant pairing of ρ_5(X) applied to the noose class of β*_3 with α̃, Lemma 2 gives |M_{f(Φ)Γ}(-1)| = |M_Γ(-1)|. So the two intersection numbers are equal, contradicting the 'Furthermore' clause. Hence Prop. 6.7 fails for every braid that meets its hypotheses and is trivial under Burau at t = -1. Nontrivial Brunnian braids trivial at t = -1 exist, for example Φ0 = [(σ1σ2)^6, [[A14,A24],A34]], whose (t+1)-adic depth is exactly 1. A conjugate of Φ0 meets the hypotheses of Prop. 6.7 provided the proper-product criterion stated in the proof of Thm. 6.9 is valid. So either that criterion or Prop. 6.7 is false, and the proof of Thm. 6.9 as written has a gap. This says nothing about whether ρ_4 is faithful."

## VERIFY
null


######## LENS: construction

## verdict
"holds_with_fixes"
## findings (14)

### F1 [major] Claim paragraph (note l. 9) and §4 Conclusion (l. 71)
- **claim**: "An explicit nontrivial Brunnian 4-braid that is trivial at t = -1 meets every hypothesis of Prop. 6.7 and Cor. 6.8"; "It therefore meets every hypothesis of Lemma 6.3, Prop. 6.7 and Cor. 6.8"
- **problem**: The headline states unconditionally something the note never establishes. Properness of Φ′·Γ_1 rests only on the paper's sketched criterion in the proof of Thm 6.9. The note itself calls that criterion unproved (l. 65), says it was not checked (l. 69) and lists it as a possible point of failure (l. 76). So the headline asserts as fact what §5 correctly treats as one side of a dichotomy.
- **evidence**: Note l. 69: "By that criterion Φ = Φ′·Γ_1 is a proper product. We could not check Conditions 1 and 2 directly". Paper p. 24, l. 1231-1234: the reduced-juxtaposition criterion is stated inside the proof of Thm 6.9 with a one-line justification.
- **fix**: Lead with the dichotomy, which does not depend on the criterion. Take Φ0, or any Brunnian braid trivial at t = -1. Either no conjugate of it is a proper product Φ′·Γ_1, and then the reduction step of Thm 6.9 fails for it. Or some conjugate is such a product, and then Prop 6.7 fails for that conjugate, by §3. Then add that, by the paper's own criterion, the explicit Φ is such a conjugate.

### F2 [minor] §4 Conclusion (l. 71)
- **claim**: "So it is a nontrivial Brunnian braid in K_4, hence pseudo-Anosov with ι(α, (β*_3)Φ) > 0"
- **problem**: The note borrows the paper's inference that a pseudo-Anosov braid sends β*_3 to an arc meeting α. That inference is false for general pseudo-Anosov braids. The conclusion ι > 0 is true for Φ, but it needs a different reason.
- **evidence**: The paper's claim is at p. 5, l. 258-260 and p. 24, l. 1226-1227. Counterexample:
- c12 encloses p1,p2; c34 encloses p3,p4; e encloses p2,p4 and passes above p3, so it misses β*_3.
- Checking each puncture type shows every essential curve in S_{0,5} meets c12 ∪ c34 ∪ e. So by Penner's construction T_{c12}·T_e^{-1}·T_{c34} is pseudo-Anosov.
- Yet it sends β*_3 to (β*_3)T_{c34}, which misses α.

A valid argument for Φ uses only Φ ∈ K_1 ∩ K_3:
1. Suppose (β*_3)Φ missed α. Forgetting p1 makes it isotopic to β*_3 rel p2,p3,p4.
2. Both arcs avoid a disk N containing α. Retracting D−p2 onto D−N turns that isotopy into a homotopy, hence an isotopy, in D_4. So Φ fixes β*_3.
3. A nontrivial push of p3 moves β*_3, since arcs from p* to p3 form a π_1-torsor. So Φ ∈ K_3 gives Φ = 1, a contradiction.
- **fix**: Replace "hence pseudo-Anosov with ι > 0" by the K_1 ∩ K_3 argument. If pseudo-Anosov is wanted, cite Whittlesey, or Kra: a nontrivial Brunnian loop fills D_3 = S_{0,4}. Optionally tell the authors about this small additional slip.

### F3 [minor] §4 'Proper product' (l. 63-69) and Remark 1 (l. 82)
- **claim**: "The proof of Thm. 6.9 asserts a shortcut for Γ_1 ... A freely reduced juxtaposition gives Condition 2."
- **problem**: In the paper, the Condition-2 criterion is phrased with the Φ of the proof, which is a nontrivial Brunnian braid. The note applies it to Φ′, which is never Brunnian. Without comment, the authors can object that the criterion was only claimed for Brunnian first factors.
- **evidence**: - Paper p. 24, l. 1223 and l. 1231-1234: Φ is Brunnian there.
- My trace of Fig 6.3: Γ_1 winds −1, 0, 0 around p1, p2, p3, and its cyclic core is y2 y3^{-1} = x1^{-1}. So Γ_1 is a twist about a curve around p1 and p4. It survives forgetting p2, and Φ′ = ΦΓ_1^{-1} is not in Brun_4.
- The paper's own conclusion Φ = Φ′·Γ_1 (p. 25, l. 1239-1240) needs the criterion for exactly such a Φ′.
- The justification of the criterion uses only the first letter of Γ_1.
- **fix**: Add one sentence. The justification uses only the first letter of Γ_1, and the proof of Thm 6.9 needs the criterion for the non-Brunnian first factor Φ′ = ΦΓ_1^{-1}. The note uses it in that form.

### F4 [minor] §5 (l. 79)
- **claim**: "Prop. 5.1 is not a suspect, because Lemma 1 gives minimal position from parity alone."
- **problem**: Too strong. The proof of Lemma 6.2 uses Prop 5.1 to put (β′)Γ in minimal position, before any parity is known. So Prop 5.1 feeds Lemmas 6.2 and 6.3, which the note itself lists as suspects. Lemma 1 removes Prop 5.1 only from the last step of Cor 6.8.
- **evidence**: Paper p. 16, l. 798-800: the proof of Lemma 6.2 invokes Prop 5.1 to choose β′ with (β′)Γ in minimal position with α.
- **fix**: Write: "Prop. 5.1 is not needed in the last step of Cor. 6.8, where Lemma 1 supplies minimal position; it enters only through Lemma 6.2."

### F5 [minor] §4 first bullet (l. 49)
- **claim**: "Deleting strand i ≤ 3 kills A_{i4}, and with it the inner commutator."
- **problem**: False for i = 3. Deleting strand 3 kills A_34, and hence b = [[A14, A24], A34]. But the inner commutator [A14, A24] survives.
- **evidence**: Strand deletion is a homomorphism on P_4. Deleting strand 3 sends A_34 to 1 and A_14, A_24 to free generators in P_3. Re-running brunn.py confirms that all four deletions of Φ0 are trivial.
- **fix**: Write "kills A_{i4}, and with it b".

### F6 [minor] §4 Conclusion (l. 71)
- **claim**: "It therefore meets every hypothesis of Lemma 6.3, Prop. 6.7 and Cor. 6.8"
- **problem**: Prop 6.7 is stated for Φ ∈ B_4, but its proof needs more. It uses Lemma 6.3, which requires Φ ∈ K_4. It also treats only braids Φ that fail parity. The note does not say that Φ is in this case, which invites the objection that Φ falls outside the proof.
- **evidence**: - Paper p. 20, l. 1031: Φ ∈ B_4. Line 1040: the proof opens by assuming Φ fails parity.
- For the note's Φ, Lemma 2 with X = 1 gives M_Φ(−1) = ±M_1(−1) = 0, because β*_3 misses α.
- If Φ satisfied parity, Lemma 1 together with ι > 0 would give |M_Φ(−1)| = ι > 0, a contradiction.
- So Φ fails parity, and if Lemma 6.3 holds, its disk sequence contains a 4-disk.
- **fix**: Add: "Φ ∈ K_4, and Φ violates parity (Lemma 2 with X = 1, then Lemma 1), so the proof of Prop. 6.7 applies to Φ in its main case."

### F7 [minor] Claim (l. 9) and §4 Conclusion (l. 71)
- **claim**: "meets every hypothesis of Prop. 6.7 and Cor. 6.8, so the argument fails on it"
- **problem**: This can be read as saying that the conclusion of Cor 6.8 fails for Φ. What is actually contradicted is Prop 6.7: two-sided parity together with unequal ι. That is the input to the proof of Cor 6.8. Since Φ0 is not in ker ρ_4, the conclusion of Cor 6.8 (some Γ with M_{f(Φ)Γ} ≠ M_Γ) may well hold.
- **evidence**: Re-running phi0_check: ρ_4(Φ0) ≠ I at t = 2 and t = 3. The argument in §3 of the note uses only the parity and inequality clauses of Prop 6.7.
- **fix**: Say explicitly that what fails is Prop 6.7, and with it the proof of Cor 6.8, not necessarily its conclusion.

### F8 [wording] §4 'Proper product' (l. 65)
- **claim**: "The proof of Thm. 6.9 asserts a shortcut for Γ_1, without proof"
- **problem**: Inaccurate. The paper gives a one-line reason for each part. For Condition 1: trigons are removed by isotopy, and rectangles are excluded by the alternation of signs. For Condition 2: the first letter of Γ_1. The note's own next bullet repeats the Condition-1 reason.
- **evidence**: Paper p. 24, l. 1228-1230 and l. 1234-1238.
- **fix**: Write "with only a one-line justification".

### F9 [wording] §4 'Proper product' (l. 69)
- **claim**: "We could not check Conditions 1 and 2 directly, because the figures are not in our text."
- **problem**: The figures are in the paper, so the authors will find this sentence odd. It also undersells what has been checked.
- **evidence**: Figs 6.3 and 6.13 are embedded rasters (PDF objects 246 and 266). Read off them:
- Γ_1 is simple.
- Its crossings with α alternate along α: down, up, down, up, down.
- Its reduced word is y2^{-1}y1^{-1}y2^2y3^{-1}y2^{-1}y1y2.
- **fix**: Write: "We have not verified Conditions 1 and 2 directly, since β′ = (β*_3)Φ′ is too long to draw. The parts of the criterion that can be read off the figures hold." Then give the word of Γ_1.

### F10 [wording] §4 (l. 54, l. 59)
- **claim**: "Take m larger than the length of the reduced word of Φ0"; "Φ0 is nontrivial with exponent sum zero"
- **problem**: No basis is named. For a general element, the total exponent sum depends on the basis. Both statements are fine here because Φ0 ∈ [K_4, K_4], but the text should say so.
- **evidence**: In the convention A_{i4} = x_i, Φ0 = [y3^{-2}, b] has y-length 30 and y-exponent sums (0, 0, 0). In that convention m = 1 already works, and m = 31 gives a reduced Φ of length 108 (freewords.py).
- **fix**: Write "reduced word in y1, y2, y3". Write "Φ0 ∈ [K_4, K_4] is nontrivial, so its y1-exponent sum is 0 and it is not a power of y1".

### F11 [wording] §4 (l. 45, l. 50)
- **claim**: "standard pure braid generators"; "This is exact rational arithmetic in bbb-gap/phi0_check.py"
[Redacted: private correspondence or workflow instructions.] Conventions for the "standard" generators A_{ij} also vary between authors.
- **evidence**: The scripts use A_{i4} = σ3…σ_{i+1}σ_i²σ_{i+1}^{-1}…σ3^{-1} and the Burau matrices σ_i ↦ I ⊕ [[1−t, t],[1, 0]] ⊕ I.
- **fix**: State both conventions in the note, and attach the short script or put it in an appendix.

### F12 [wording] Remark 2 (l. 83)
- **claim**: "That is a misapplication inside Prop. 6.7, not a separate failure."
- **problem**: The remark is accurate. The label "misapplication" can be heard as a stronger charge than intended, and two facts that support the remark are missing.
- **evidence**: - The definition (p. 11, l. 564) and Prop 5.1 (p. 12, l. 599) take the first factor in K_n.
- Prop 6.7 (p. 20, l. 1032) applies the notion to f(Φ)·Γ, and f(Φ) is not in K_5, since forgetting p5 returns Φ ≠ 1.
- With f(Φ) as first factor the definition reads verbatim with β′ = ∅: no α-β disk contains p5, which lies outside D_4. So Condition 2 is vacuous.
- The proof of Prop 6.7 never verifies that f(Φ)Γ is proper.
- **fix**: Call it a scope mismatch, and add the two facts: the definition is vacuous here with β′ = ∅, and the proof never checks properness.

### F13 [wording] Status (l. 11), §6 (l. 91), Verification (l. 95-111); outside my lens
- **claim**: "Three independent hostile referees ... found no refutation"; "suggested by the breakthrough chat"; "A separate chat independently recomputed Φ0"
- **problem**: Internal-process language. To the authors it will read either as independent human experts or as references to private context.
- **evidence**: Note text.
- **fix**: Remove these phrases, or describe them plainly as internal checks.

### F14 [wording] §3 (l. 39); outside my lens
- **claim**: "By Proposition 6.7 we can assume that ι ≠ ι. The result follows."
- **problem**: Misquote. The arguments of ι were dropped, so the line reads as if the paper contained a typo.
- **evidence**: Paper p. 24, l. 1214 compares ι(α, (β*_3)(f(Φ)·Γ)) with ι(α, (β*_3)Γ).
- **fix**: Restore the arguments.
## confirmed
[
 "The paper says Γ_1's reduced word begins with y2^{-1}: p. 25 top, l. 1234-1238, \"as a freely reduced word in this basis, Γ1 begins with y2^{-1}\". I confirmed this independently by tracing the Fig 6.3 raster against the cut system dual to Fig 6.13: Γ_1 = y2^{-1} y1^{-1} y2^2 y3^{-1} y2^{-1} y1 y2, freely reduced, length 8 (trace_gamma1.py). The word also ends with y2, so the claim does not depend on how Γ_1 is oriented or on whether Push is read as a homomorphism or an anti-homomorphism.",
 "Fig 6.13 basis (p. 25): y1 encloses p3, y2 encloses p2 and p3, y3 encloses p1, p2 and p3. All three are counterclockwise; the arrowheads point right along the bottom, checked at pixel level. In terms of the standard loops x_i: y1 = x3, y2 = x2x3, y3 = x1x2x3. In the convention A_{i4} = x_i: A34 = y1, A24 = y2y1^{-1}, A14 = y3y2^{-1}, δ = y3, and Φ0 = [y3^{-2}, b] with reduced y-length 30 (freewords.py). The note's argument uses only Φ0 ∈ [K_4,K_4] \\ {1}, so it does not depend on this relation.",
 "Γ_1 is simple: the gold pixels minus a disk at p4 form one arc. It is in minimal position with α: 5 crossings and 5 y2-letters. Its crossings with α alternate in sign along α (down, up, down, up, down), as the paper's Condition-1 argument asserts at p. 24, l. 1229-1230 (trace_check.py).",
 "Γ_1 winds −1, 0, 0 around p1, p2, p3, and its cyclic core is y2 y3^{-1} = x1^{-1}. So Γ_1 is a Dehn twist about a curve enclosing p1 and p4, and it is not Brunnian.",
 "The free reductions are right. They hold for any m larger than the y-length of Φ0. The junctions are y2|y1 and y1^{-1}|y2^{-1}, and Φ = gΦ0g^{-1} with g = Γ_1^{-1}y1^m. An explicit run with m = 31 gives a reduced word of length 108 (freewords.py). The construction needs only that the first letter of Γ_1 is not y1^{±1}.",
 "Φ0 is pure, Brunnian and nontrivial (re-ran brunn.py, Artin action). ρ_4(Φ0) = I and ρ_5(f(Φ0)) = I at t = −1, and ρ_4(Φ0) ≠ I at t = 2 and t = 3 (re-ran phi0_check.py).",
 "Φ0 = [δ^{-2}, b] with δ = Δ_3^{-2}Δ_4² = A14A24A34 ∈ K_4. The δ identity is exact via the Artin action, and the commutator identity checks via Burau at t = 2 and t = 3/2 (identity_check.py). Hence Φ0 ∈ [K_4,K_4], and its exponent sums vanish in every basis.",
 "Brun_4 ⊂ [K_4,K_4], because strand deletions kill every A_{i4} exponent sum. So Remark 1's repair covers every nontrivial Brunnian braid.",
 "Φ is a nontrivial Brunnian braid in K_4, since Brun_4 is normal in B_4. It is pseudo-Anosov, by Whittlesey or by Kra (a nontrivial Brunnian loop fills D_3 = S_{0,4}). ι(α,(β*_3)Φ) > 0 by the K_1 ∩ K_3 argument. ρ_5(f(Φ)) = I at t = −1 by conjugation invariance.",
 "Φ necessarily violates parity, by Lemma 2 with X = 1 together with Lemma 1 and ι > 0. So the proof of Prop 6.7, which opens by assuming parity fails (p. 20, l. 1040), applies to Φ in its main case.",
 "Hypothesis lists, all met given the paper's criterion: Lemma 6.3 (p. 17, l. 832-834); Prop 6.7 (p. 20, l. 1031-1033, plus the implicit requirement Φ ∈ K_4); Cor 6.8 (p. 24, l. 1192-1193).",
 "Scope of the criterion. The Condition-1 part is stated for simple loops like Γ_1 and any β (p. 24, l. 1228-1230). The Condition-2 part is phrased for the Brunnian Φ of the proof (l. 1223, 1231-1234), and its justification uses only the first letter of Γ_1. The proof itself needs the criterion for the non-Brunnian first factor Φ′.",
 "Remark 1 is accurate: the proof arranges that Φ·Γ_1 is reduced and then asserts Φ = Φ′·Γ_1 (p. 25, l. 1238-1240).",
 "Remark 2 is accurate: the definition (p. 11, l. 564) and Prop 5.1 (p. 12, l. 599) require a first factor in K_n, while Prop 6.7 (p. 20, l. 1032) uses f(Φ)·Γ, and f(Φ) is not in K_5."
]
## not_checked
[
 "Conditions 1 and 2 of a proper product for Φ′·Γ_1, verified directly. β′ = (β*_3)Φ′ is far too long to draw.",
 "Whether the paper's criterion (a reduced juxtaposition with Γ_1 gives a proper product) is valid in general.",
 "Lemmas 6.2-6.6 and the case analysis of Prop 6.7, including whether the modified Γ′ keeps both parities. These belong to other lenses.",
 "§§1-3 and §6 of the note in depth. I re-derived Lemmas 1 and 2 only as far as the cleanest statement needs them.",
 "The y-word of Φ0 under the paper's own identification of A_{ij} with loops, which the paper does not state. I computed it in one natural convention only.",
 "Whether the conclusion of Cor 6.8 holds for Φ.",
 "report.md was not written. The harness blocks this subagent from writing report files, so the full report is in this output. Scripts and images are in <HOME>/jones-adversarial-pass/bbb-gap-note/check/construction/."
]
## summary
"The construction in §§4-5 holds up, but the note needs fixes before finalization.\n\nReading Fig 6.3 against the cut system dual to Fig 6.13 gives Γ_1 = y2^{-1} y1^{-1} y2^2 y3^{-1} y2^{-1} y1 y2. This confirms the paper's claim that the word begins with y2^{-1}. It also confirms the paper's claim that Γ_1's crossings with α alternate in sign. Two facts are new: Γ_1 is a twist about a curve around p1 and p4, and it is not Brunnian.\n\nWhat checks out:\n- The free reductions are correct, and they do not depend on how the y-basis relates to the A_{i4}: they need only Φ0 ∈ [K_4,K_4] \\ {1}.\n- Φ is a nontrivial Brunnian, pseudo-Anosov braid in K_4, with ι > 0 and trivial at t = −1.\n- Φ necessarily violates parity, so the proof of Prop 6.7 applies to it in its main case.\n- Both further remarks describe the paper accurately.\n\nWhat needs fixing:\n- **Major:** the headline says Φ \\\"meets every hypothesis\\\" of Prop 6.7 and Cor 6.8. Properness of Φ′·Γ_1 rests only on the paper's unproved criterion. Lead instead with the dichotomy, which holds without the criterion: either no conjugate of Φ0 is a proper product Φ′·Γ_1, or Prop 6.7 fails for one that is.\n- **Minor:** the ι > 0 step relies on the paper's claim that a pseudo-Anosov braid always moves β*_3 onto α. That claim is false; a Penner example pseudo-Anosov keeps β*_3 off α. Replace it with an argument that uses only Φ ∈ K_1 ∩ K_3.\n- **Minor:** the note should state that the criterion is used for the non-Brunnian first factor Φ′.\n- **Minor:** \\\"Prop 5.1 is not a suspect\\\" is too strong, because Lemma 6.2 uses Prop 5.1.\n- **Minor:** in the strand-deletion bullet, the phrase \\\"the inner commutator\\\" is wrong for i = 3.\n- **Wording:** \\\"without proof\\\", \\\"the figures are not in our text\\\", the internal file paths, the language about referees and chats, and the garbled ι ≠ ι quote all need changing.\n\nThe harness blocked writing report.md, so the full report is in this output. The scripts (trace_gamma1.py, trace_check.py, freewords.py, identity_check.py) and gamma1_annotated.png are in <HOME>/jones-adversarial-pass/bbb-gap-note/check/construction/."
## cleanest_statement
"Let Φ0 = [(σ1σ2)^6, [[A14, A24], A34]], where A_{i4} = σ3…σ_{i+1}σ_i²σ_{i+1}^{-1}…σ3^{-1}. Then Φ0 is a nontrivial Brunnian 4-braid, and ρ_4(Φ0) = I at t = −1 but ρ_4(Φ0) ≠ I at t = 2.\n\nLet Φ be any conjugate of Φ0 that is a proper product Φ′·Γ_1. Then:\n- Φ ∈ K_4;\n- ι(α, (β*_3)Φ) > 0, because Φ ∈ K_1 ∩ K_3;\n- Φ violates parity;\n- ρ_5(f(Φ)) = I at t = −1.\n\nTake any Γ ∈ K_5 for which f(Φ)·Γ and Γ both satisfy parity. Lemma 1 gives ι = |M(−1)| for both arcs, and Lemma 2 gives M_{f(Φ)Γ}(−1) = ±M_Γ(−1). So the two values of ι are equal, and Prop 6.7 is false for Φ.\n\nIf no conjugate of Φ0 is such a proper product, then the reduction step of Thm 6.9 fails for Φ0. Either way, the proof of Thm 6.9 does not cover Φ0.\n\nThe paper's own criterion asks only that the juxtaposition with Γ_1 be freely reduced. Γ_1's reduced word in the basis of Fig 6.13 is y2^{-1}y1^{-1}y2^2y3^{-1}y2^{-1}y1y2, which begins with y2^{-1}. So by that criterion, (Γ_1^{-1}y1^m)Φ0(Γ_1^{-1}y1^m)^{-1} is such a proper product for every m larger than the y-length of Φ0. On the paper's own terms, then, Prop 6.7 fails.\n\nThis does not show that ρ_4 is unfaithful, because Φ0 is not in ker ρ_4."

## VERIFY
{
 "verdicts": [
  {
   "claim": "Headline overstates properness. Note l. 9 says the explicit nontrivial Brunnian 4-braid 'meets every hypothesis of Prop. 6.7 and Cor. 6.8'. §4 Conclusion l. 71 says 'It therefore meets every hypothesis of Lemma 6.3, Prop. 6.7 and Cor. 6.8'. Both are stated without condition, although properness of Φ′·Γ_1 rests only on the paper's sketched criterion. The note itself calls that criterion unproved (l. 65), says it was not checked (l. 69), and lists it as a possible point of failure (l. 76).",
   "verdict": "REAL",
   "evidence": "(1) The note's own text. l. 9 and l. 71 are unconditional. l. 69 says properness holds only 'By that criterion' and that the note 'could not check Conditions 1 and 2 directly'. l. 75-76 list the criterion among the things that may be false. The referee's line numbers and quotes from the note are exact.\n\n(2) The paper. The proper-product definition is geometric (p. 11, bbb-layout.txt l. 564-581). The Γ_1 shortcut appears only inside the proof of Thm 6.9:\n- Condition 1 gets a two-sentence argument (p. 24, l. 1228-1230: only trigons and rectangles; trigons removed by isotopy; rectangles excluded by sign alternation along α). It does not explicitly address the type-4 'with basepoint' polygons of p. 11.\n- Condition 2 gets the reduced-juxtaposition criterion (p. 24, l. 1231-1234) with a one-line hint (p. 25, l. 1238).\nThe referee's citation of p. 24, l. 1231-1234 is accurate.\n\n(3) Hypothesis lists. Lemma 6.3 (p. 17, l. 832-833), Prop. 6.7 (p. 20, l. 1031-1033) and Cor. 6.8 (p. 24, l. 1192-1193; also needs ι > 0). Properness is the only one the note takes on trust.\n\n(4) The construction, given the criterion, is correct.\n- I read Fig. 6.3 and Fig. 6.13 myself. The dual cuts are (p2,p3) for y1, α for y2, and the ray left of p1 for y3; each y_i crosses its cut once, downward.\n- Γ_1 leaves p4 on the arrowed outer bottom strand. Its first cut crossing goes upward through α at about x = 300 px.\n- So Γ_1 begins with y2^{-1}, as the paper states.\n- The free reductions at l. 58-61 hold: a randomised test found 0 failures in 19,889 trials. They need only that the first letter of Γ_1 is not y1.\n\n(5) The referee's dichotomy is valid and does not use the criterion.\n- Case A: no B_4-conjugate of Φ0 can be written as a proper product Φ′·Γ_1. Then the reduction step (p. 25, l. 1238-1240) is false for Φ0. The criterion is then false as well, since the explicit Φ has a freely reduced juxtaposition.\n- Case B: some conjugate Φ is such a product. Brun_4 is normal in B_4 (p. 2), so Φ is Brunnian and lies in K_4, and ρ_5(f(Φ)) = ρ_4(Φ)⊕1 = I at t = -1. Prop. 6.7 plus Lemma 1 give |M_{f(Φ)Γ}(-1)| ≠ |M_Γ(-1)|, which Lemma 2 forbids. So Prop. 6.7 fails for Φ.\n- Case B does not even need ι > 0. The dichotomy depends only on §3 (Lemmas 1 and 2) and on the facts about Φ0.\n\n(6) ι > 0 is not a second conditional ingredient. It has an elementary proof for every nontrivial Brunnian 4-braid. Suppose (β*_3)Φ misses α. Deleting strand 1 makes it isotopic to β*_3 in D_{2,3,4}. Since D_4 minus α equals D_{2,3,4} minus α, and that space is homeomorphic to D_{2,3,4} by a map supported near α, Φ fixes β*_3. Deleting strand 3 is injective on Stab(β*_3). So Φ = 1.\n\n(7) Facts about Φ0, recomputed with conventions independent of the earlier scripts (left Artin action, transposed Burau):\n- Φ0 is nontrivial and pure, and deleting each strand gives the trivial braid.\n- ρ_4(Φ0) and ρ_5(f(Φ0)) are I at t = -1, and not I as Laurent matrices or at t = 2 or t = 3.\n- The (t+1)-depth is 1.\n- Φ0 = [δ^{-2}, b] exactly, with δ and b in K_4.\n\nConclusion: the referee is right on every point. The mathematics of §§3-5 is unaffected, because §5 already states a valid dichotomy. The problem is confined to the framing at l. 9 and l. 71, plus two phrases at l. 65 and l. 69, but it must be fixed before finalizing the note.",
   "required_change": "1. l. 9 (Claim). Replace the sentence 'An explicit nontrivial Brunnian 4-braid that is trivial at t = -1 meets every hypothesis of Prop. 6.7 and Cor. 6.8, so the argument fails on it.' with:\n\n'Take any nontrivial Brunnian 4-braid that is trivial at t = -1; §4 gives an explicit one, Φ0. If no conjugate of it can be written as a proper product Φ′·Γ_1, the reduction step at the end of the proof of Thm. 6.9 fails for it. If some conjugate can, that conjugate meets every hypothesis of Prop. 6.7 and Cor. 6.8, and by §3 Prop. 6.7 fails for it. Either way the proof of Thm. 6.9 does not go through. By the criterion for proper products stated in that proof, the conjugate Φ of §4 is such a product, so if the criterion holds, Prop. 6.7 is where the argument fails.'\n\n2. l. 71 (Conclusion). Replace 'It therefore meets every hypothesis of Lemma 6.3, Prop. 6.7 and Cor. 6.8, and by §3 no Γ can have all the properties Prop. 6.7 asserts for it.' with:\n\n'If Φ′·Γ_1 is a proper product, as that criterion says, then Φ meets every hypothesis of Lemma 6.3, Prop. 6.7 and Cor. 6.8, and by §3 no Γ can have all the properties Prop. 6.7 asserts for it. If it is not, the criterion fails for Φ′.'\n\n3. l. 65. 'without proof' is unfair, because the paper gives short reasons for both conditions (p. 24, l. 1228-1238). Change it to 'with only a short justification'.\n\n4. l. 69. Drop 'because the figures are not in our text'. The figures are in the paper, and they have now been read and confirm that Γ_1 begins with y2^{-1}. Write instead: 'We have not checked Conditions 1 and 2 for Φ′·Γ_1 directly from the definition in Section 5.'\n\n5. Optional. For ι > 0 at l. 71, cite the two-line Brunnian argument in place of the route through pseudo-Anosov maps.\n\nA direct planar check that Φ′·Γ_1 is a proper product was not done and is not needed with this wording. It is needed only to make the stronger claim unconditional."
  }
 ],
 "summary": "Verdict: REAL. The construction referee is right that note l. 9 (Claim) and l. 71 (§4 Conclusion) state without condition that the explicit braid meets every hypothesis of Lemma 6.3, Prop. 6.7 and Cor. 6.8. Properness of Φ′·Γ_1 rests only on the criterion sketched inside the proof of Thm 6.9 (p. 24, layout l. 1228-1234; p. 25, l. 1238-1240). The note itself treats that criterion as unchecked (l. 69) and as possibly false (l. 76).\n\nThe referee's fix is logically sound and independent of the criterion. Either no B_4-conjugate of Φ0 is a proper product Φ′·Γ_1, in which case the reduction step of Thm 6.9 is false (and so is the criterion). Or some conjugate is, in which case Prop. 6.7 fails for it by §3; that case needs neither the criterion nor ι > 0.\n\nThe rest of the construction holds, granting the criterion:\n- Reading Fig. 6.3 and Fig. 6.13 directly, Γ_1 begins with y2^{-1}, as the paper states.\n- The free reductions hold (randomised test, 0 failures in 19,889 trials).\n- Recomputed with independent conventions, Φ0 is nontrivial, pure and Brunnian. ρ_4(Φ0) and ρ_5(f(Φ0)) are I at t = -1 and not I as Laurent matrices or at t = 2 or 3; the (t+1)-depth is 1; Φ0 = [δ^{-2}, b] with δ and b in K_4.\n- ι > 0 holds for every nontrivial Brunnian 4-braid by an elementary argument (delete strand 1, then strand 3). So properness is the only conditional ingredient.\n\nThe mathematics of §§3-5 stands, since §5 already states a valid dichotomy. The fix is to lead with the dichotomy at l. 9, make l. 71 conditional on the criterion, change 'without proof' at l. 65 to 'with only a short justification', and drop 'because the figures are not in our text' at l. 69. Exact replacement wording is in required_change.\n\nNot done: a direct planar check of Conditions 1 and 2 for Φ′·Γ_1. It is not needed with the proposed wording.\n\nThe markdown copy at <HOME>/jones-adversarial-pass/bbb-gap-note/check/verify-construction/report.md could not be saved: the harness blocks subagents from writing report files. Its full content is in this output.\n\nFiles saved:\n- <HOME>/jones-adversarial-pass/bbb-gap-note/check/verify-construction/phi0_independent.py and phi0_independent.out\n- <HOME>/jones-adversarial-pass/bbb-gap-note/check/verify-construction/freered_test.py and freered_test.out\n- <HOME>/jones-adversarial-pass/bbb-gap-note/check/verify-construction/zoom_left_bottom.png and zoom_right_bottom.png (the first crossing of Γ_1 in Fig. 6.3)"
}


######## LENS: compute

## conventions
"Everything is in pure Python with exact integer and Fraction arithmetic, written from scratch before I looked at source/scripts/.\n\nBraid words are lists of nonzero integers (k = s_k, -k = s_k^-1), multiplied left to right.\n\nArtin action is a right action, x.(uv) = (x.u).v, with images freely reduced:\n- s_i: x_i -> x_i x_{i+1} x_i^-1, x_{i+1} -> x_i.\n- s_i^-1: x_i -> x_{i+1}, x_{i+1} -> x_{i+1}^-1 x_i x_{i+1}.\n- A left-action variant gave the same verdicts.\n\nStrand deletion tracks the permutation and drops each crossing that involves the deleted strand, reindexing the rest. A deleted braid is trivial if its word freely reduces to empty, or if it acts trivially on F_3.\n\nBurau over Z[t, 1/t], with Laurent polynomials stored as dicts:\n- U: s_i -> I with block [[1-t, t], [1, 0]] in rows/columns i, i+1.\n- UT: the transpose of each generator.\n- R: reduced, row i replaced by (t, -t, 1) in columns i-1, i, i+1.\n- RT: its transpose.\n- Mirror variants (s_i -> generator inverse) were also run.\n\nSelf-tests (selftest.py, 220 PASS):\n- Braid relations hold in all four conventions, and each generator times its inverse is I.\n- The Fox Jacobian of the Artin action equals the U product on 30 random words.\n- trace U = 1 + trace R on 25 random words.\n- Deletion is a homomorphism on pure words and is well defined on equal braids.\n\nDepth is the minimum multiplicity of the root t = -1 over the entries of M - I. Stabilisation f is s_i -> s_i (new strand 5 on the right, as in the paper's Fig. 6.10); s_i -> s_{i+1} was also checked."
## checks
[
 {
  "id": "0",
  "claim": "A14 = s3 s2 s1 s1 s2^-1 s3^-1, A24 = s3 s2 s2 s3^-1, A34 = s3 s3 are the standard pure braid generators",
  "result": "PASS",
  "detail": "They equal Artin/Birman's A_ij = s_{j-1}..s_{i+1} s_i^2 s_{i+1}^-1..s_{j-1}^-1. Each is pure with linking matrix {(i,4): 1}, is trivial after deleting strand 4 (so lies in K_4), and deleting a third strand gives the matching A_{i'j'} in B_3. With the other common convention (s_i..s_{j-2} s_{j-1}^2 ..), all key properties of Phi0 still hold; only the word length and the formula delta = A14 A24 A34 change."
 },
 {
  "id": "1",
  "claim": "Phi0 is pure",
  "result": "PASS",
  "detail": "The permutation of Phi0 is the identity."
 },
 {
  "id": "2",
  "claim": "Phi0 is nontrivial (Artin action)",
  "result": "PASS",
  "detail": "The reduced Artin images of x1..x4 have lengths 6774875, 9487773, 5064573, 2359041, none equal to x_j (about 37 s; the left action agrees). The fast certificate in phi0_check.py: X and b do not commute under the Artin action. Burau(Phi0) != I also proves it."
 },
 {
  "id": "3",
  "claim": "Deleting strand 4 gives the trivial braid (Phi0 in K_4), and deleting each of strands 1, 2, 3 does too (Brunnian)",
  "result": "PASS",
  "detail": "For each of the four strands, the deleted word (80, 64, 56 and 24 letters) freely reduces to the empty word, and acts trivially on F_3. b itself is also Brunnian and nontrivial."
 },
 {
  "id": "4",
  "claim": "The freely reduced length of the word Phi0 is 112 letters",
  "result": "FAIL",
  "detail": "112 is the unreduced concatenation (X 12 + b 44 + X^-1 12 + b^-1 44). The freely reduced word has 76 letters (c = [A14,A24] reduces to 12 letters and b to 26). In the free basis A_14, A_24, A_34 of K_4 it has 28 letters; in the Fig. 6.13 basis it has 30, under the convention-dependent identification y1 = A34, y2 = A24 A34, y3 = A14 A24 A34. BBB-GAP.md never states 112. The figure comes from ref-transfer.md line 20 ('has a 112-letter word') and from the old script output 'word length of Phi0: 112'. The note needs no specific number: 'm larger than the length' works for any m > 30."
 },
 {
  "id": "5",
  "claim": "Burau(Phi0) = I at t = -1 in every convention, in B_4 and for the stabilisation in B_5",
  "result": "PASS",
  "detail": "Holds in U, UT, R, RT and their mirror variants, in B_4, and in B_5 for both s_i -> s_i (the paper's f) and s_i -> s_{i+1}. Also holds for 16 sampled conjugates g Phi0 g^-1."
 },
 {
  "id": "6",
  "claim": "Burau(Phi0) is not I as a Laurent matrix, nor at t = 2 or t = 3",
  "result": "PASS",
  "detail": "In all four conventions, in B_4 and B_5. chk.py independently gives not-I at t = 2 and t = 1/3."
 },
 {
  "id": "7",
  "claim": "The (t+1)-adic depth of Burau(Phi0) is exactly 1",
  "result": "PASS",
  "detail": "Depth 1 in U, UT, R, RT, their mirrors, in B_4 and B_5, and for all sampled conjugates (depth is a conjugacy invariant). Mutation Phi0 -> [X, [X, b]] gives depth 2, so the depth routine discriminates."
 },
 {
  "id": "8",
  "claim": "X = (s1 s2)^6 equals Delta_3^4 and is I at t = -1",
  "result": "PASS",
  "detail": "(s1 s2)^6 = (s1 s2 s1)^4 and (s1 s2)^3 = (s1 s2 s1)^2 by the Artin action. Burau(X) = I at -1 in all four conventions, with depth exactly 1."
 },
 {
  "id": "9",
  "claim": "Phi0 = [delta^-2, b] with delta = Delta_3^-2 Delta_4^2",
  "result": "PASS",
  "detail": "Checked directly by the Artin action, and in the script via the equivalent statement that delta^2 X commutes with b. Also: Delta_4^2 is central; Delta_3^2 x Delta_3^-2 = delta^-1 x delta for x = A14, A24, A34; delta = A14 A24 A34 lies in K_4."
 },
 {
  "id": "10",
  "claim": "Phi0 lies in [K_4, K_4]",
  "result": "PASS",
  "detail": "delta and b both lie in K_4 (pure and trivial after deleting strand 4), so Phi0 = [delta^-2, b] lies in [K_4, K_4]. As a word in the free basis A_i4 it is reduced of length 28 with exponent sums (0, 0, 0). Direct argument: K_4 is normal in P_4 and [K_4, K_4] is characteristic, so X b X^-1 lies in [K_4, K_4]. In fact Phi0 lies in gamma_4(K_4)."
 },
 {
  "id": "E1",
  "claim": "iota(alpha, (beta*_3)Phi0) > 0, and Phi0 cannot satisfy parity",
  "result": "PASS",
  "detail": "For pure braids, B31 - t B32 = (1 - t)(W1 - t W2) exactly, with W_j the Fox derivatives of the conjugator in x3.Phi0. This confirms the note's (1 - t^{+-1}) boundary-loop factor. M_Phi0 is nonzero with M(-1) = 0 (sum of |coefficients| 330962), and the same holds for rev, mirror and rev-mirror. Sixteen conjugates (g = A34^m for m up to 31, and random K_4 and B_4 elements) also give M != 0 with M(-1) = 0. This is evidence for iota > 0 on the note's Phi, not a proof, since Gamma_1 is not available as a word."
 },
 {
  "id": "E2",
  "claim": "Lemma 2 (if rho(Y) = I at -1 then M_YX(-1) = +-M_X(-1)) holds",
  "result": "PASS",
  "detail": "With Y = f(Phi0) and 12 random pure G in B_5, M_YG(-1) = M_GY(-1) = M_G(-1) every time. Also M_YG != M_G as polynomials every time, so Moody's criterion separates f(Phi0) from the kernel for generic G. Only Cor. 6.8's iota-only comparison fails."
 },
 {
  "id": "E3",
  "claim": "Nontrivial Brunnian braids occur at every (t+1)-adic depth (note Section 6)",
  "result": "PASS",
  "detail": "Phi_1 = Phi0 and Phi_k = [X, Phi_{k-1}] have depth exactly k, checked directly for k = 1..4 in U and UT. For all k: the leading coefficient is ad_C^{k-1}(N_1), where C = C_X(-1) is diagonalisable with eigenvalues 0, 0, -6, -6 and ad_C(N_1) != 0, so it never vanishes (also computed up to k = 11). These braids are Brunnian because Brun_4 is normal. The note states this without justification."
 },
 {
  "id": "T1",
  "claim": "Note Section 4: 'Deleting strand i <= 3 kills A_{i4}, and with it the inner commutator.'",
  "result": "FAIL",
  "detail": "False for i = 3. Deleting strand 3 sends [A14, A24] to [A13, A23], which is nontrivial in B_3 (computed); it is the outer commutator that dies because A34 -> 1. The conclusion that Phi0 is Brunnian is still correct."
 },
 {
  "id": "T2",
  "claim": "Note Section 3 quotes Cor. 6.8's proof as \"By Proposition 6.7 we can assume that ι ≠ ι. The result follows.\"",
  "result": "FAIL",
  "detail": "Misquote. The paper (p. 24, layout line 1214) has 'ι(α, (β∗3)(f(Φ)·Γ)) ̸= ι(α, (β∗3)Γ)'. Abbreviated inside quotation marks it reads as a tautology the authors never wrote."
 },
 {
  "id": "T3",
  "claim": "Claim paragraph: the explicit braid 'meets every hypothesis of Prop. 6.7 and Cor. 6.8'",
  "result": "FAIL",
  "detail": "Stated more strongly than the note supports. It depends on (a) the unproven proper-product shortcut in the proof of Thm. 6.9, which the note admits it could not check, and (b) the paper's claim (p. 24) that a pseudo-Anosov image of beta*_3 'necessarily intersects the arc α nontrivially', which gives iota > 0. Section 5's 'at least one of the following is false' is the accurate form. Better: either the shortcut, Prop. 6.7 or the pA iota > 0 claim fails, so the proof of Thm. 6.9 has a gap whichever it is."
 }
]
## script_path
"<HOME>/jones-adversarial-pass/bbb-gap-note/check/compute/phi0_check.py"
## output_path
"<HOME>/jones-adversarial-pass/bbb-gap-note/check/compute/phi0_check.out"
## disagreements_with_existing_scripts
[
 "No disagreement in any computed value. brunn.py (rerun, 74 s) gives Artin image lengths 6774875, 9487773, 5064573, 2359041, identical to mine, and finds Phi0 nontrivial, pure and Brunnian. Its deletion method (killing x_i in the images) differs from mine (deleting letters from the braid word), so the agreement is an independent confirmation.",
 "chk.py agrees with me in all four conventions in B_4 and B_5: I at t = -1, not I at t = 2 or t = 1/3, and b not I at -1. The old phi0_check.py reproduces its stored output (U only, t = -1, 2, 3) and agrees with mine.",
 "sec7.py's data match the paper's Section 7 and Fig. 3.1b polynomials. M(-1) = 6, 2, 8, -20, as the note says; I also checked these by hand.",
 "Presentational: the old source/scripts/phi0_check.py, which is the script the note cites, says on line 1 'Phi0 = [(s1 s2)^6, [[y1,y2],y3]], y_i = A_{i4}'. This clashes with the note's and the paper's y1, y2, y3 (Fig. 6.13: y1 is the loop around p3, roughly A34^{+-1}, not A14). Do not send it as is.",
 "Presentational: the old script prints 'word length of Phi0: 112' and ref-transfer.md says 'a 112-letter word'. Both are the unreduced length; the freely reduced word has 76 letters.",
 "Background only: ref-transfer.md says Burau is not I 'at t = 2 or t = 3/2', but no script evaluates t = 3/2. The scripts use 2, 3 and 1/3; the note correctly says 2 and 3.",
 "The old scripts check numerical values only. None checks the Laurent-matrix identity, the depth, the identity [delta^-2, b], membership in [K_4, K_4], or the free reduction to 76 letters. The new script covers all of these."
]
## summary
"Verdict: every computational fact the note uses about Phi0 is correct. I checked them from scratch, in several conventions, and no computation contradicts the note. The problems are in the wording, not the numbers.\n\n**What I computed.**\n- Phi0 is pure, nontrivial and Brunnian, and lies in [K_4, K_4], indeed in gamma_4(K_4).\n- Its Burau matrix is I at t = -1 in U, UT, R, RT and their mirrors, in B_4, and in B_5 under both stabilisations.\n- It is not I as a Laurent matrix, at t = 2 or at t = 3, and its (t+1)-adic depth is exactly 1 everywhere.\n- X = (s1 s2)^6 = Delta_3^4, and Phi0 = [delta^-2, b] with delta = A14 A24 A34.\n\n**Extra computations.**\n- M_Phi0 is nonzero with M(-1) = 0, and the same holds for 16 conjugates. That gives iota(alpha, (beta*_3)Phi0) > 0 and rules out parity for Phi0. It is evidence, not proof, for the note's specific conjugate Phi.\n- Lemma 2 holds on 12 random samples in B_5. M_{f(Phi0)G} != M_G for every sample, so only the iota-only comparison in Cor. 6.8 fails.\n- The iterated commutators [X, ..., [X, b]] have depth exactly k for every k. That rigorously supports the note's unjustified claim that nontrivial Brunnian braids occur at every depth.\n\n**Problems in the note, most serious first.**\n1. Section 3 quotes the paper as \"we can assume that ι ≠ ι\". The paper (p. 24, line 1214) states the full inequality; abbreviated inside quotation marks it reads as a tautology the authors never wrote.\n2. The Brunnian bullet \"kills A_{i4}, and with it the inner commutator\" is false for i = 3: [A13, A23] survives, and the outer commutator is what dies. The conclusion still holds.\n3. The headline claim that the braid \"meets every hypothesis of Prop. 6.7 and Cor. 6.8\" overstates. It depends on the unproven proper-product shortcut and on the paper's own claim that pseudo-Anosov implies iota > 0. The robust form: either the shortcut, Prop. 6.7 or the pA claim fails, so the proof of Thm. 6.9 has a gap whichever it is.\n4. \"Is a counterexample to it\" in Section 3 should say Prop. 6.7, not Cor. 6.8. Cor. 6.8's conclusion is probably true for Phi0 with some other Gamma.\n5. Internal references the authors cannot follow: \"breakthrough chat\", \"separate chat\", \"hostile referees\", paths like bbb-gap/..., and \"the figures are not in our text\" (the figures are in the paper).\n6. The cited old script calls A_{i4} \"y_i\", which clashes with the paper's Fig. 6.13 basis.\n\n**The 112-letter figure.** It is not in the note; it comes from ref-transfer.md and the old script's output. It is the unreduced length; the freely reduced word has 76 letters.\n\n**Deliverable.** phi0_check.py is 149 lines of pure Python 3 with no dependencies, runs in about 0.8 s, and prints 42 PASS lines and 0 FAIL. Mutation tests confirm that each check fails when its property is broken. Output is in phi0_check.out. Supporting files are in <HOME>/jones-adversarial-pass/bbb-gap-note/check/compute/: braidlib.py, selftest.py and selftest.out (220 PASS), explore.py and explore.out (full Artin run), extra.py and extra.out, mut/, brunn_rerun.out.\n\n**Comparison with source/scripts/.** All earlier scripts agree with my values. The only disagreements are presentational: the y_i notation, the unreduced 112, and t = 3/2 in ref-transfer.md, which no script computes.\n\n**report.md was not saved.** The harness refused to let a subagent write report files, so the full report is this structured output."

## VERIFY
{
 "verdicts": [
  {
   "claim": "Finding 1 (location 4): the freely reduced length of the word Phi0 is 112 letters.",
   "verdict": "NOT_REAL",
   "evidence": "The note never states 112 or any other length. A search of BBB-GAP.md for '112', 'length' and 'letters' finds only line 54: 'Take m larger than the length of the reduced word of Φ0'. 112 appears only in background files, ref-transfer.md line 20 and scripts/phi0_check.out. There it is the length of the unreduced sigma-word that was actually evaluated (12 + 44 + 12 + 44), which is accurate for that word. My own code agrees with all of the referee's numbers. Freely reduced sigma-words: c = [A14, A24] has 12 letters, b has 26, Phi0 has 76. In the free basis A14, A24, A34 of K_4, Phi0 = [delta^-2, b] with delta = A14 A24 A34 = Delta_3^-2 Delta_4^2 (checked in the Artin action), and has 28 letters. In the Fig. 6.13 basis it has 30 letters with y1 = A34, y2 = A24 A34, y3 = A14 A24 A34, but 36 with y2 = A34 A24, y3 = A34 A24 A14 (mixed identifications give 30 to 44). So any y-length is convention-dependent. The exponent sums are 0, and y1^m Phi0 y1^-m already begins with y1 and ends with y1^-1 for m >= 1 (or m >= 2 in the second convention). The note's rule 'm larger than the length' is therefore sufficient in every convention.",
   "required_change": "None. Optional: write 'the reduced word of Φ0 in y1, y2, y3'. If phi0_check.out is ever attached, label its first line as the length of the unreduced sigma-word."
  },
  {
   "claim": "T1, note Section 4 line 49: 'Deleting strand i <= 3 kills A_{i4}, and with it the inner commutator.'",
   "verdict": "REAL",
   "evidence": "I computed this two ways, diagrammatic strand deletion and the Artin-quotient method, and they agree. Deleting strand 3 sends A14 to A13, A24 to A23 and A34 to 1. So [A14, A24] goes to [A13, A23], which is nontrivial in B_3 (A13 and A23 generate a free group). What dies is the outer commutator b, because A34 goes to 1. Deleting strand 1 or 2 kills the inner commutator c, and deleting strand 4 kills both c and b. Deleting any single strand kills Phi0. So Phi0 is Brunnian, but the stated reason is false for i = 3. Severity is minor because the conclusion stands, but the sentence is false and must change.",
   "required_change": "Replace the sentence with something like: 'Deleting strand 1 or 2 kills A_{14} or A_{24}, and with it the inner commutator. Deleting strand 3 kills A_{34}, and with it b. So b, and hence Φ0, dies in every case.'"
  },
  {
   "claim": "T2, note Section 3 line 39 quotes the proof of Cor. 6.8 as 'By Proposition 6.7 we can assume that ι ≠ ι. The result follows.'",
   "verdict": "REAL",
   "evidence": "The page image of p. 24 (layout line 1214) reads: 'By Proposition 6.7 we can assume that ι(α, (β^3_*)(f(Φ)·Γ)) ≠ ι(α, (β^3_*)Γ).' The note drops the arguments but keeps the quotation marks, so it presents as verbatim a sentence the authors did not write. One small correction to the referee: 'ι ≠ ι' reads as a contradiction, not a tautology. The point stands either way.",
   "required_change": "Quote the sentence in full, or paraphrase it without quotation marks. In the same sentence, change 'the inequality of the coefficient sums' to 'the inequality of the sums of the absolute values of the coefficients'. The paper's display is |a_{M-}| + ... + |a_{M+}| = ι. 'Coefficient sums' can be read as M(1), which would make the next sentence's '|M(-1)|' wrong."
  },
  {
   "claim": "T3, Claim paragraph (line 9), with the same wording in the Section 4 Conclusion (line 71): the explicit braid 'meets every hypothesis of Prop. 6.7 and Cor. 6.8'.",
   "verdict": "REAL",
   "evidence": "Part (a) is exactly right. The only hypothesis of Prop. 6.7 is that 'Φ can be written as a proper product Φ = Φ′ · Γ1' (p. 20, layout line 1031). The note gets this only from the criterion asserted in the proof of Thm. 6.9 (pp. 24-25), and it says itself that it 'could not check Conditions 1 and 2 directly' (line 69). Section 5 correctly says 'At least one of the following is false'. So the Claim and the Section 4 Conclusion state as unconditional what the note's own argument makes conditional, an inconsistency in the headline claim. Part (b) is right that the note's justification is unsound, but the conclusion it supports is true. Cor. 6.8 (not Prop. 6.7) needs ι(α, (β^3_*)Φ) > 0 (p. 24, line 1192). The note supports it with 'hence pseudo-Anosov', repeating the paper's inference (p. 24, line 1226; p. 5, line 259). That inference fails for pseudo-Anosov maps in general. Penner's construction gives a counterexample. Take a, the curve around p2 and p4 passing above p3; d0, the curve around p1, p2 and p4 bounding a neighbourhood of ∂D ∪ β^3_*; and b, the round curve around p3 and p4. Then a and d0 miss β^3_*, b misses α, and a ∪ d0 ∪ b fills (I checked by enumeration that every essential puncture set crosses one of the three). So T_a T_{d0} T_b^-1 is a pure pseudo-Anosov braid, and it sends β^3_* to (β^3_*)T_b^-1, which is disjoint from α. Still, every nontrivial Φ that dies under forgetting strand 1 and under forgetting strand 3 has ι > 0, and this covers every nontrivial Brunnian 4-braid. The argument: if (β^3_*)Φ missed α, the loop (β^3_*)Φ·(β^3_*)^-1 would lie in D minus (α ∪ p4). It is null in D minus {p2, p4} because forgetting p1 kills Φ. The inclusion of D minus (α ∪ p4) into D minus {p2, p4} is a homotopy equivalence, so (β^3_*)Φ is isotopic to β^3_*. A push of p3 that fixes β^3_* is trivial. Moreover, the note's contradiction in Section 3 uses only Prop. 6.7, which has no ι hypothesis. So the referee's proposed third disjunct ('or the pA iota > 0 claim fails') is unnecessary.",
   "required_change": "(1) Make the Claim conditional, in line with Section 5. Suggested text: 'An explicit nontrivial Brunnian 4-braid Φ that is trivial at t = -1 is certified as a proper product Φ′·Γ_1 by the criterion used in the proof of Thm. 6.9. If it is one, Φ meets every hypothesis of Prop. 6.7 and Cor. 6.8, and Prop. 6.7 fails on it. If it is not, that criterion fails. Either way the proof of Thm. 6.9 does not go through.' (2) Rewrite the Section 4 Conclusion the same way ('if Φ′·Γ_1 is a proper product, Φ meets ...'). (3) Replace 'hence pseudo-Anosov with ι(α, (β*_3)Φ) > 0' with 'ι(α, (β^3_*)Φ) > 0, as the paper asserts for every nontrivial Brunnian braid (p. 5); Prop. 6.7 does not need this', or with the short forgetting-strands argument above. (4) Do not add the pseudo-Anosov ι > 0 claim as a third disjunct. Optional, for tone: line 65 says the shortcut is asserted 'without proof', but the paper gives a one-line justification, so 'with only a brief justification' is fairer. Line 69 says 'because the figures are not in our text', which is out of date now that the figures are available; better: 'We have not verified Conditions 1 and 2 directly from the figures.'"
  }
 ],
 "summary": "I checked all four of the compute referee's 'major' findings against the paper's page images and layout text, and recomputed them with new code. Three are real and one is not.\n\n- **Finding 1 (112 letters): NOT_REAL.** The note never states a length. 112 is the unreduced sigma-word length, and it appears only in background files. The referee's numbers are right (76 reduced sigma-letters, 28 in the A_i4 basis, 30 in the Fig. 6.13 basis under one convention and 36 under the other). The note's rule 'm larger than the length' is sufficient in any convention.\n- **T1 (strand-3 deletion): REAL, minor.** Deleting strand 3 turns the inner commutator into [A13, A23], which is nontrivial. It is the outer commutator that dies. Phi0 is still Brunnian (verified two independent ways), so only the sentence needs fixing.\n- **T2 (quote of the proof of Cor. 6.8): REAL.** The note shortens the paper's ι-inequality to 'ι ≠ ι' but keeps the quotation marks. It should quote the sentence in full and say 'sums of the absolute values of the coefficients'.\n- **T3 ('meets every hypothesis'): REAL.** The Claim paragraph and the Section 4 Conclusion must become conditional on the proper-product criterion in the proof of Thm. 6.9, matching Section 5. The referee's second ground needs correcting:\n  - The paper's inference 'pseudo-Anosov implies ι > 0' is false in general. Penner's construction gives a pure pseudo-Anosov braid with ι = 0.\n  - But ι > 0 does hold for every nontrivial Brunnian 4-braid, by a short forgetting-strands argument.\n  - Prop. 6.7 has no ι hypothesis anyway.\n  \n  So the note should drop 'hence pseudo-Anosov' and should not add a third disjunct.\n\n**Other notes:**\n- The paper writes β^3_* (superscript 3, subscript *), and the note's 'β*_3' reads the other way round.\n- Rechecked and consistent with the note: Burau of Phi0 is I at t = -1 in B_4 and B_5, not I at t = 2 or 3, not I as a Laurent matrix, with (t+1)-depth exactly 1. Phi0 = [delta^-2, b] lies in [K_4, K_4].\n\nThe requested report.md was not saved, because the harness blocked report-file writes from subagents. Its full content is in these verdicts. Scripts and output are in <HOME>/jones-adversarial-pass/bbb-gap-note/check/verify-compute/: braidcore.py, check_findings.py and check_findings.out (run with python3 -I, about 0.1 s)."
}


######## LENS: status

## versions
[
 "v1: submitted Mon 6 Jul 2026 16:28:02 UTC, 3,164 KB, from Tara E. Brendle's account. Comments field: '26 pages, 28 figures'. Source: https://arxiv.org/abs/2607.05283v1",
 "v2 (current): submitted Mon 14 Sep 2026 15:55:28 UTC, 3,746 KB, from Tara E. Brendle's account. Comments field: '28 pages, 32 figures. Minor corrections and improved exposition'. Sources: https://arxiv.org/abs/2607.05283 and https://export.arxiv.org/api/query?id_list=2607.05283 (updated 2026-09-14T15:55:28Z, published 2026-07-06T16:28:02Z)",
 "v3: does not exist. https://arxiv.org/abs/2607.05283v3 returns HTTP 404. There is no erratum, no withdrawal notice, no journal-ref and no related DOI. arXiv records no trackbacks: https://arxiv.org/tb/2607.05283"
]
## current_version
"v2, submitted 14 Sep 2026 15:55:28 UTC, still current on 3 Nov 2026. Its statement numbers (Lemmas 6.1-6.6, Prop. 6.7, Cor. 6.8, Thm. 6.9) differ from v1 (Lemmas 6.1-6.3, Prop. 6.4, Cor. 6.5, Thm. 6.6); Lemmas 6.4-6.6 are new in v2."
## comments_field
"v2 (current): \"28 pages, 32 figures. Minor corrections and improved exposition\". v1: \"26 pages, 28 figures\". The arXiv metadata title is \"The Burau representation of the braid group is faithful for n = 4\"; the PDF and HTML of both versions print \"The Burau representation is faithful for n = 4\". Subjects: math.GT (primary), math.GR. No journal-ref. arXiv DOI: 10.48550/arXiv.2607.05283. The printed date lines come from the compile date: the v2 PDF prints 15 Sep 2026 next to an arXiv stamp of 14 Sep, and the v1 HTML prints 24 Aug 2026 although v1 was submitted on 6 Jul."
## public_reports_of_error
[
 {
  "url": "https://pith.science/paper/2607.05283",
  "summary": "The only public report of a specific gap I found. It is an AI-generated review by the model 'glm-5.2', which 'read the paper on July 7, 2026'. It covers v1 only (the page says v2 is newer) and says no human expert has reviewed the paper. It judges the strategy sound but says v1 Prop. 6.4 needs careful verification. Its main point is that the proof never checks that the modified push map satisfies the parity condition, which it calls 'the load-bearing gap'. Smaller points: the first-stage disk types, Case 2, normality of Brun_4 in v1 Thm 6.6, and the connectivity claims in Prop. 5.1. A section headed 'Simulated authors' rebuttal' is machine text, not a reply from the authors. The page never mentions t = -1, Torelli or specialization. v2 later added Lemmas 6.4-6.6 on the parity of loops in D_5, which covers this ground; whether that was a response to Pith is unknown."
 },
 {
  "url": "https://www.nytimes.com/2026/09/06/science/92-year-old-mathematician-apprentice.html",
  "summary": "General caution only, with no specific error. Read through the mirror https://dnyuz.com/2026/09/06/the-92-year-old-mathematician-and-the-teenage-apprentice/ and secondary sources, because the NYT itself could not be fetched. It says the ideas had not yet been through rigorous peer review, experts would need months to digest them, and errors could still surface."
 },
 {
  "url": "https://en.wikipedia.org/wiki/Burau_representation",
  "summary": "Last edited 27 Sep 2026. Citing the NYT, it says the claim 'has not yet been verified by the mathematical community' and that refereeing may uncover errors. The word 'disputed' does not appear, and the article names no specific error."
 },
 {
  "url": "https://en.wikipedia.org/wiki/Joan_Birman",
  "summary": "Last edited 26 Sep 2026. Same caution: the claim is not yet verified by the mathematics community and errors may be uncovered in refereeing. No specific error."
 },
 {
  "url": "https://en.wikipedia.org/wiki/Tara_E._Brendle",
  "summary": "Last edited 26 Sep 2026. It says the claim 'has not been verified by the mathematical community', citing the NYT, Scientific American and arXiv. No specific error."
 }
]
## publication_status
"Preprint only. I found no record of acceptance, 'to appear' status or publication. Specifically:\n- arXiv has no journal-ref.\n- OpenAlex lists it as a preprint with no venue: https://api.openalex.org/works/doi:10.48550/arXiv.2607.05283\n- Brendle's Glasgow staff profile and personal papers page do not list it.\n- The NYT (6 Sep 2026) says it had not yet been through rigorous peer review.\n- The Breakthrough Questions Substack (22 Sep 2026) says 'under peer review' but gives no source or journal: https://breakthroughquestions.substack.com/p/how-people-work-on-a-breakthrough\n- It is already cited as an established result: Shimizu-Yaguchi, arXiv:2608.29147v2, footnote 1, writes 'Very recently, Bharathram, Birman, and Brendle proved that it is faithful for m=4'.\nNot checked: Semantic Scholar returned HTTP 429 and zbMATH returned HTTP 403."
[Redacted: private correspondence or workflow instructions.]
[Redacted: private correspondence or workflow instructions.]

## coverage
[
 {
  "url": "https://www.scientificamerican.com/article/how-a-99-year-old-mathematician-unraveled-a-century-old-braid-mystery/",
  "summary": "Scientific American, 24 Jul 2026, by Lyndie Chiou (edited by Clara Moskowitz). The main early piece. Quotes Yang-Hui He (LIMS), Birman, Brendle and Bharathram, and gives their affiliations as Columbia, Glasgow and Princeton. Says nothing about peer review. Reports that a group around Breuillard and Kosyak spent six months trying AI chatbots on the problem."
 },
 {
  "url": "https://www.nytimes.com/2026/09/06/science/92-year-old-mathematician-apprentice.html",
  "summary": "New York Times, 6 Sep 2026, Gregory Barber, 'The 92-Year-Old Mathematician and the Teenage Apprentice'. A profile of the Birman-Bharathram collaboration. Quotes Dan Margalit (skeptical early on, now understands the result) and Emmanuel Breuillard (calls the paper remarkable). Says it has not yet been through rigorous peer review. Not fetchable directly; read through the mirror https://dnyuz.com/2026/09/06/the-92-year-old-mathematician-and-the-teenage-apprentice/ and secondary sources."
 },
 {
  "url": "https://www.math.columbia.edu/2026/08/03/professor-joan-birman-and-collaborators-resolved-the-last-remaining-open-case-for-the-burau-representation-of-the-classical-braid-group/",
  "summary": "Columbia Mathematics department news, 3 Aug 2026. Announces that the last open case has been resolved and links Scientific American. The body could not be fetched (TLS error); the content here comes from search snippets."
 },
 {
  "url": "https://as.vanderbilt.edu/math/2026/09/06/prof-margalit-quoted-in-new-york-times/",
  "summary": "Vanderbilt Mathematics news, 6 Sep 2026. Notes that Margalit is quoted in the NYT and that Brendle announced the result in a talk at the July 2026 ICM satellite conference at Vanderbilt."
 },
 {
  "url": "https://margalit.droppages.net/vcs26/abstracts.html",
  "summary": "Vanderbilt Colloquium Series (ICM satellite), 13-17 Jul 2026. Plenary talk by Brendle titled 'The Burau representation': a new proof for n = 3, and how to adapt it to n = 4."
 },
 {
  "url": "https://www.buffalo.edu/cas/math/news-events/calendar.html",
  "summary": "University at Buffalo Topology and Geometry Seminar, Fri 18 Sep 2026: Bharathram (Princeton), 'The Burau representation of B4 is faithful'."
 },
 {
  "url": "https://www.spektrum.de/news/99-jaehrige-mathematikerin-loest-jahrhundertealtes-raetsel/2336315",
  "summary": "Spektrum der Wissenschaft, 4 Aug 2026. An exclusive German translation of the Scientific American article by Lyndie Chiou; paywalled."
 },
 {
  "url": "https://www.yahoo.com/news/science/articles/99-old-mathematician-unraveled-century-111500867.html",
  "summary": "Yahoo News syndication of the Scientific American article."
 },
 {
  "url": "https://www.derstandard.at/story/3000000333054/99-jaehrige-mathematikerin-loeste-problem-an-dem-generationen-scheiterten",
  "summary": "Der Standard (Austria), around 27 Jul 2026 (date inferred from the page). A human-interest piece with no peer-review caveat."
 },
 {
  "url": "https://nazology.kusuguru.co.jp/archives/198071",
  "summary": "Nazology (Japan), 28 Jul 2026. Describes the result as a preprint and raises no doubts."
 },
 {
  "url": "https://www.math.columbia.edu/~woit/wordpress/?p=15770",
  "summary": "Peter Woit, Not Even Wrong, 'Various and Sundry', 15 Jul 2026. Early mention of the result; no reader comments about it."
 },
 {
  "url": "https://www.math.columbia.edu/~woit/wordpress/?p=15846",
  "summary": "Peter Woit, 7 Sep 2026. Points readers to the NYT piece. Three comments, none about correctness."
 },
 {
  "url": "https://aperiodical.com/2026/08/aperiodical-news-roundup-july-2026/",
  "summary": "Aperiodical news roundup for July 2026. Links Scientific American and Greg Egan's post; raises no doubts."
 },
 {
  "url": "https://breakthroughquestions.substack.com/p/how-people-work-on-a-breakthrough",
  "summary": "Breakthrough Questions (Stephen Rappaport), 22 Sep 2026. Describes how the collaboration worked and says the paper is 'under peer review' (unsourced)."
 },
 {
  "url": "https://news.ycombinator.com/item?id=49077209",
  "summary": "Hacker News thread on the arXiv link, 27 Jul 2026: 53 points, 18 comments, none about correctness."
 },
 {
  "url": "https://news.ycombinator.com/item?id=49586038",
  "summary": "Hacker News thread on the NYT piece: 13 points, 2 comments, none about correctness."
 },
 {
  "url": "https://mathstodon.xyz/@gregeganSF/116990320867526554",
  "summary": "Greg Egan on Mathstodon, 27 Jul 2026 (also on X: https://x.com/gregeganSF/status/2081617044471214199). 10 replies. Ian Agol points to Bharathram's separate claim about the Gassner representation (arXiv:2208.12378); no reply discusses whether BBB is correct."
 },
 {
  "url": "https://x.com/lyndie_chiou/status/2080703210705281339",
  "summary": "Lyndie Chiou on X, 24 Jul 2026, promoting the Scientific American piece and framing the team as having beaten an AI effort."
 }
]
## summary
"Verdict for the public-status lens, checked 3 Nov 2026\n\nThe note's status framing holds. arXiv:2607.05283 v2 (14 Sep 2026) is still current. There is no v3 (the URL returns 404), no erratum, no withdrawal, no journal-ref and no trackback, and I found no acceptance or publication anywhere.\n\nI found no public statement that the Section 6 argument sees only t = -1 or the braid Torelli group. As far as the public record shows, the note's objection is new; private reports to the authors cannot be checked. Places searched with no hit:\n- MathOverflow's own search: 0 results for '2607.05283'.\n- arXiv trackbacks and alphaXiv.\n- Hacker News, Peter Woit's blog and the Mathstodon threads.\n- Scientific American, NYT, Columbia, Vanderbilt, Spektrum, Der Standard, Nazology, Aperiodical and Substack coverage.\n- Targeted web searches on t = -1, Torelli, Moody polynomial, Prop. 6.7 and Cor. 6.8, with gap, error and counterexample.\n\nThe only public report of a specific gap is an AI-generated Pith review of v1 (7 Jul 2026). It is about the parity condition for the modified push map in v1 Prop. 6.4, which is a different point, and v2 added Lemmas 6.4-6.6 covering that ground. Beyond that, the NYT and three Wikipedia articles say only that the claim is not yet verified and that refereeing may uncover errors; none says 'disputed'. One later arXiv paper (Shimizu-Yaguchi, 2608.29147v2) already cites BBB as proved.\n\nPoints for the note from this lens:\n1. **Pin the version in the first line:** 'arXiv:2607.05283v2 (14 Sep 2026)'.\n   - v1 numbers differ: v1 Prop. 6.4, Cor. 6.5 and Thm. 6.6 are v2 Prop. 6.7, Cor. 6.8 and Thm. 6.9, and Lemmas 6.4-6.6 do not exist in v1.\n   - Cite arXiv submission dates rather than the printed date lines, which are compile dates.\n   - There are two titles: the arXiv metadata title, which the note uses, and the printed title 'The Burau representation is faithful for n = 4'.\n2. **Word the novelty claim carefully.** Write 'we have not seen this raised publicly', not 'no one has raised it'.\n3. **Cite Brendle's own paper.** Brendle co-authored Brendle-Margalit-Putman, Invent. Math. 200 (2015) 263-310, on the kernel of Burau at t = -1; it is on her Glasgow page, and Margalit, thanked in the paper, is a co-author. Citing it for the claim in §4 that (sigma1 sigma2)^6 lies in the braid Torelli group puts the objection in the authors' own framework. I checked only the abstract, which identifies the hyperelliptic Torelli group with that kernel; I did not check its braid generating set.\n4. **Internal references will be opaque to the authors:** 'bbb-gap/phi0_check.py', 'the breakthrough chat', 'a separate chat' and 'three independent hostile referees'.\n   - If the referees were AI passes, calling them 'independent referees' overstates the verification.\n   - The public framing is sensitive to AI. Scientific American reports a rival group's six futile months with AI chatbots, Chiou's X post frames the team as beating an AI effort, the paper says AI proofread a draft, and the Pith page contains a 'Simulated authors' rebuttal'.\n   - State how the checks were done and attach the script with its output.\n5. **A misquote in note §3 (outside this lens).** The note puts 'we can assume that ι ≠ ι' inside quotation marks. The paper's sentence (p. 24, text line 1214) reads 'By Proposition 6.7 we can assume that ι(α, (β*_3)(f(Φ)·Γ)) ≠ ι(α, (β*_3)Γ).' Quote it in full or drop the quotation marks.\n6. **An inconsistency in v2 itself (outside this lens).** v2 is inconsistent about the scope of Thm. 6.9:\n   - the opening of §6 (lines 723-724) says 'the point-pushing group K4';\n   - the theorem itself (line 1221) says Brun4;\n   - the introduction (line 109) says 'point-pushing group Brun4'.\n\n[Redacted: private correspondence or workflow instructions.] Limits:\n- The NYT could not be fetched; I read it through the dnyuz mirror and secondary sources.\n- math.columbia.edu failed TLS in WebFetch. I read Woit's blog and Birman's homepage through the r.jina.ai reader. The body of the Columbia news post could not be retrieved, so its content comes from search snippets.\n- MathOverflow is not reachable by the search tool, so I used its own search through the reader.\n- X and LinkedIn were mostly unreadable. Semantic Scholar returned HTTP 429 and zbMATH HTTP 403.\n- I opened no PDFs, including Glasgow's Summer 2026 newsletter, and found no official Glasgow announcement.\n\nThe markdown copy was not saved. The harness refused the write to <HOME>/jones-adversarial-pass/bbb-gap-note/check/status/report.md because subagents may not write report files, so this structured output is the report. The folder <HOME>/jones-adversarial-pass/bbb-gap-note/check/status/ exists and is empty."

## VERIFY
null
