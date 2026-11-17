# Cycle-2 audit and file triage: braid-route, Carmi-Cohen and special-class literature; cable and scalar-sum algebra audits; braid-route skeptic

- Workflow: wf_6f2d5e26-ef1 (jones-cycle2-audit-and-file-triage-wf_6f2d5e26-ef1.js)
- Session: bridge session (Claude-Codex integrator)
- Launched (script written): 2026-11-02 23:15 local; journal last written: 2026-11-02 23:59 local
- Agents started: audit:cable-algebra, lit:braid-route, lit:carmi-cohen, lit:special-classes, audit:cable-geometry, audit:scalar-sums-algebra, skeptic:braid-route, skeptic:carmi-cohen, skeptic:special-classes
- Results extracted here: lit:braid-route, lit:carmi-cohen, audit:cable-algebra, audit:scalar-sums-algebra, lit:special-classes, skeptic:braid-route
- Started but returned no result: audit:cable-geometry, skeptic:carmi-cohen, skeptic:special-classes
- Context: Launched 2 Nov 23:15 (first night of the bridge). Six of nine agents returned (audit:cable-geometry, skeptic:carmi-cohen and skeptic:special-classes did not). No report files were written; results were used in letters of 2-3 Nov but are not saved anywhere else in full.
- Provenance: contemporaneous agent outputs recorded in the workflow journal (runtime state, not copied). Text below is verbatim except formatting (JSON fields rendered as markdown), em dashes replaced by ' - ', email addresses redacted, and home-directory paths shortened to ~ (session scratchpad roots to <scratch>). These are internal AI agent outputs, not external review; statuses are as the agent stated them at the time and may be superseded by later board entries.


## Agent: lit:braid-route


### items

  -
    - source_id: S009
    - citation: V. Bharathram, J. S. Birman, T. E. Brendle, The Burau representation of the braid group is faithful for n = 4, arXiv:2607.05283 [math.GT; math.GR], MSC 57M07, 57M10, 20F65. v1 Mon 6 Jul 2026 16:28:02 UTC (3,164 KB; 26 pp, 28 figures); v2 Mon 14 Sep 2026 15:55:28 UTC (3,746 KB; 28 pp, 32 figures). No journal reference on the listing. The PDF title omits the words 'of the braid group'.
    - exact_statement: Main Theorem (verbatim, the only verbatim quote in this output): "The Burau representation ρ4 of B4 is faithful." Here ρ_n: B_n -> GL_n(Z[t,t^-1]) is the UNREDUCED Burau representation, defined in Sec. 2 as the action of B_n on H_1(D~_n, {p~*}), a free Z[t^{±1}]-module of rank n. D~_n is the Z-cover of the n-punctured disk for the exponent-sum map, and p* is a boundary basepoint. The paper notes that Burau's original representation is the reduced one into GL_{n-1}(Z[t,t^-1]). Both have the same kernel. My check: over Q(t) the fixed vector (1,...,1) and the fixed covector (1,t,...,t^{n-1}) pair to 1+t+...+t^{n-1} ≠ 0, so unreduced = reduced ⊕ trivial. The theorem therefore covers the reduced Burau representation too. Corollary 1.1 (paraphrase): the Jones (Hecke-algebra) representation of B_4 is faithful. This is immediate because that representation contains reduced Burau as a summand; the paper cites Jones 1987 and Kasahara 2008, Remark 5.6. Proof chain (paraphrase): (1) Prop 1.2 uses Long 1986, Thm 2.2 to reduce the problem to faithfulness on the Brunnian subgroup Brun_4. (2) Theorem 6.9 (v2; Theorem 6.6 in v1) says ρ4 is faithful on Brun_4. (3) The proof uses Moody's obstruction (Thm 2.3: if M_{Φ·Γ} ≠ M_Γ for some Γ, then Φ ∉ ker ρ_n), a parity condition on disk sequences that rules out cancellation (Lemma 4.2), and a correcting push-map in K_5 < B_5 (Prop 6.7 and Cor 6.8 in v2; Prop 6.4 and Cor 6.5 in v1).
    - status: Claimed in an unrefereed preprint. Latest version is v2 (14 Sep 2026). As of 2026-11-02 the v3 URL returns 'not found' and there is no withdrawal notice. I did NOT audit the proof (UNCHECKED). The abstract is word-identical in v1 and v2.
    - latest_version: v2, 14 Sep 2026 (arXiv stamp); the PDF title page is dated 15 Sep 2026
    - url: https://arxiv.org/abs/2607.05283
    - read_primary: True
    - relevance_to_scaffold: If correct, this closes the B4-kernel sub-route only. There is no nontrivial β in B4 acting trivially under Burau, Temperley-Lieb (TL) or Jones/Hecke at generic parameter, so Ito-style knots closure(αβ) with β in the kernel cannot exist on 4 strands. It proves nothing about trace collisions, B_n for n>=5, or Lemma Q.
    - category: audit_target
  -
    - source_id: S009
    - citation: Same paper, v1 vs v2 comparison. Sentence-level diff of pdftotext output: <scratch>/7610ac96-4d03-4d32-b526-8a5647837809/scratchpad/wf-c2audit/s008-s010-verify/diff_2607_v1_v2.txt
    - exact_statement: These statements are word-identical in v1 and v2: Main Theorem, Corollary 1.1, Prop 1.2, Prop 6.4 (=6.7), Cor 6.5 (=6.8), Thm 6.6 (=6.9). The v2 comment field calls the changes minor corrections plus improved exposition, but the proof of the key step changed. (i) Sec. 5 adds a new class of bigon-forming configurations, generalized bigons/trigons/rectangles 'with basepoint' (new Fig. 5.5), used in Prop 5.1's proof. (ii) Sec. 6.3 adds three lemmas. Lemma 6.4: pushing along a loop 'disjoint from β modulo 4-disks' replaces each 4-disk by a sign-changing 5-disk. Lemma 6.5: such loops are 'alternating modulo 4-disks'. Lemma 6.6: a loop that is 'properly simple modulo 4-disks' satisfies the parity condition. (iii) v1's justification for the correcting loop Γ ('otherwise we could have made a different choice of γ1') is replaced by an appeal to Lemma 6.6. (iv) Khalid Bou-Rabee is added to the acknowledgments. (v) Several results are renumbered. Both versions say AI was used to proofread a draft, and both thank Dan Margalit for extensive feedback. My reading of the v2 text is not an audit, but it found two possible soft spots. (a) The proof of Prop 6.7 explicitly checks only conditions (1) and (2) of 'properly simple modulo 4-disks'; condition (3), that Γ_I misses β*_3, is not mentioned, and condition (1) is asserted to hold by construction. (b) The modified loop Γ' (Cases 1 and 2) is justified only by the ordering and intersection-number properties. No explicit parity check for Γ' was added, which is the point an automated review raised for v1.
    - status: The revision is confirmed from the primary arXiv listing; the secondary index's '14 Sep revision' is correct. The claim did not change. The proof of the central proposition was substantively reworked. Whether soft spots (a) and (b) are real gaps is UNCHECKED.
    - latest_version: v2 (14 Sep 2026)
    - url: https://arxiv.org/abs/2607.05283v2
    - read_primary: True
    - relevance_to_scaffold: Anyone relying on S009 should audit v2's Prop 6.7 (Lemmas 6.4-6.6 and the Γ' modification). This is the load-bearing step for Brun_4.
    - category: audit_target
  -
    - source_id: S009
    - citation: Reception. Scientific American, L. Chiou, How a 99-year-old mathematician unraveled a century-old braid mystery, 2026-07-24. Columbia Math Dept announcement, added 2026-08-03. English Wikipedia: Burau representation (last edited 2026-09-27), Joan Birman (2026-09-26), Tara E. Brendle (2026-09-26). pith.science/paper/2607.05283. alphaXiv abs page. NYT, G. Barber, 2026-09-06 (cited by Wikipedia; not read).
    - exact_statement: Positive but informal. Yang-Hui He (London Institute for Mathematical Sciences) is quoted in SciAm calling it a major advance and saying the authors did solve the problem; there is no indication that he refereed it. Columbia's department page says the result was proved. Cautionary. All three Wikipedia pages describe it as a claim not yet verified by the mathematical community and cite the NYT article. The NYT returned HTTP 403, so its text is UNCHECKED. The cited NYT title says '92-Year-Old', while SciAm gives Birman's age as 99; this mismatch is unresolved. Automated, not a specialist. pith.science shows an 'AI referee (glm-5.2)' review of v1 dated 2026-07-07 with verdict CONDITIONAL. It flags the parity verification in Prop 6.4 (v1), the γ1 disk-type claim, and Prop 5.1 rigor. Its 'Authors' replies are not attested as genuine, and no v2 review exists. Pre-posting feedback is acknowledged from Margalit, Bou-Rabee (v2), Dougherty, Farb and Ken Birman; this is not independent verification. Not found in searches on 2026-11-02: any MathOverflow thread, alphaXiv comments (the v2 page shows none), published rebuttal, erratum, independent reproof, or journal acceptance.
    - status: Not withdrawn, not formally challenged, not independently verified. The specialist reaction found is thin and informal. Absence of a challenge in searches does not prove there is none.
    - url: https://www.scientificamerican.com/article/how-a-99-year-old-mathematician-unraveled-a-century-old-braid-mystery/
    - read_primary: True
    - relevance_to_scaffold: Treat S009 as a strong but unrefereed claim. Do not use it as an established barrier without that caveat.
    - category: context
  -
    - source_id: S008
    - citation: T. Ito, A kernel of a braid group representation yields a knot with trivial knot polynomials, arXiv:1402.2028. The only version is v1, Mon 10 Feb 2014. Published Math. Z. 280 (2015), no. 1-2, 347-353, DOI 10.1007/s00209-015-1426-7 (Crossref: online 2015-01-09).
    - exact_statement: Statements below are precise restatements; the verbatim text is on pp. 1-2 of arXiv v1. Theorem 1 (labelled [Big, Conj. 3.2]): Let H be a nontrivial, non-central normal subgroup of B_n, and let α in B_n have the unknot as closure. Then for every N>0 there exists β in H such that the closure of αβ is a hyperbolic knot of genus >= N and braid index n. The arXiv text misprints this as 'β ∈ K'. Corollary 1: if a quantum representation ρ_V: B_n -> GL(V^{⊗n}) (V a finite-dimensional U_q(g)-module) is non-faithful for some n, then every knot K shares Q_V with infinitely many mutually distinct hyperbolic knots. Corollary 2: the same holds simultaneously for finitely many such representations, all non-faithful on B_n. This uses Long's lemma that two nontrivial non-central normal subgroups intersect nontrivially. Corollary 3: IF the Burau representation of B_4 is NOT faithful, THEN the Jones polynomial fails to detect the unknot. The direction is one-way; the converse (Burau(B4) faithful implies Jones detects the unknot) is neither claimed nor implied. Corollary 3 comes from Theorem 1 'as explained in [Big]': take H = kernel of the TL/Jones representation of B4 and α = σ1σ2σ3. This yields nontrivial (hyperbolic) knots with V=1 (also HOMFLY-trivial), of braid index 4 and unbounded genus. The proof of Theorem 1 combines two results. Theorem 3: nontrivial normal subgroups of B_n are unbounded in the Dehornoy order, and pseudo-Anosov elements can be chosen if the subgroup is non-central. Theorem 2 (Ito's earlier work): β >_D Δ^{2N} implies genus >= N; β >_D Δ^{2r(n)} implies braid index n; β >_D Δ^4 and pseudo-Anosov implies hyperbolic.
    - status: Published and proved. The arXiv text was read in full. The journal wording and numbering are UNCHECKED: the Springer page served a bot challenge, which I did not bypass.
    - latest_version: arXiv v1 (2014-02-10); journal 2015
    - url: https://arxiv.org/abs/1402.2028
    - read_primary: True
    - relevance_to_scaffold: This is the exact theorem behind the kernel route, and it only produces counterexamples. If S009 is correct, Corollary 3 has a false hypothesis and says nothing either way. Theorem 1 still applies to any nontrivial kernel of a quantum representation of B_n for n>=5. It gives no control over unknotting number.
    - category: route
  -
    - source_id: S007
    - citation: S. Bigelow, Does the Jones polynomial detect the unknot?, arXiv:math/0012086 v1 (12 Dec 2000); J. Knot Theory Ramifications 11 (2002) 493-505. Read only for the B4 equivalence that Ito's Corollary 3 depends on.
    - exact_statement: Prop 1.5 (restated): for B4, the Jones representation, the TL representation and the Burau representation are all faithful or all unfaithful. Proof: TL_4 = V(4) ⊕ V(3,1) ⊕ V(2,2), where V(3,1) is Burau and V(2,2) is Burau_3 composed with B4->B3 (σ3 -> σ1). The Jones representation adds V(2,1,1), which has the same kernel as Burau, and V(1,1,1,1). The unfaithful direction uses the commutator [(σ1σ2)^3, β]. Bigelow omits the proof that this commutator is nontrivial. Conjecture 3.2, the knot-producing step, was later proved by Ito (S008, Thm 1). Bigelow also remarks that a positive answer (faithfulness) would have no comparably dramatic consequence.
    - status: Published. One step of Prop 1.5 is omitted in the source. S009 instead cites Kasahara 2008, Remark 5.6 for the equivalence, which I did not read (UNCHECKED). The direction S009 needs (Burau faithful implies Jones/TL faithful) is immediate.
    - url: https://arxiv.org/abs/math/0012086
    - read_primary: True
    - relevance_to_scaffold: Explains why Burau(B4) faithfulness is equivalent to TL(B4) faithfulness. This is the hinge between S009 and the Jones polynomial.
    - category: context
  -
    - source_id: S010
    - citation: D. Korzun, E. Lanina, A. Sleptsov, Closed 4-braids and the Jones unknot conjecture, arXiv:2402.02553: v1 Sun 4 Feb 2024 (22 pp); v2 Thu 18 Apr 2024 (23 pp, latest). PUBLISHED: Ann. Inst. H. Poincaré D Comb. Phys. Interact. 13 (2026), no. 4, 711-746, DOI 10.4171/AIHPD/213, CC BY 4.0. Received 13 Jun 2024, revised 17 Jul 2024, communicated by L. Chekhov; Crossref record dated 2025-08-11. The inventory record lacks this publication.
    - exact_statement: Restatements. An 'n-strand knot' is the closure of an n-braid. H is HOMFLY-PT normalized so that H(unknot)=1; Jones = H at A=q^2 and Alexander = H at A=1. Prop 3.1: no nontrivial closed 2-braid knot has V=1. Prop 3.3: no nontrivial closed 3-braid knot has V=1 and H≠1; Prop 3.4 cites Stoimenow for V=1 on 3 strands in general. THEOREM 3.1: no nontrivial closed 4-braid knot has V=1, Δ=1 and H≠1. Equivalently, V=Δ=1 forces H=1 on 4 strands. THEOREM 3.2: every closed 4-braid knot K with V_K=1 and H_K≠1 satisfies, for SOME integer m>=0, H_K = 1 + (A²-q²)(A²-q⁴)(A²-q⁻²)(A²-q⁻⁴)·F. Here either F = F^{K_m} = -Σ_{j=0}^{m} [2j+4]_q[j+3]_q[j+1]_q/([3]_q[4]_q)·A^{-2j-8}, or F is the mirror version F̄^{K̄_m}, the same sum with A^{2j}. The theorem's wording 'arbitrary m' means each such K has some m. It does not mean that every m occurs. Sec. 4.1 (not a numbered theorem): matching the 4-strand character expansion forces the braid writhe W = 2m+5 (mirror: -(2m+5)). So W is odd with |W|>=5, and H is determined by W. All coefficients are fixed except one, a[2,2]. It equals the [2,1]-trace of the 3-braid obtained by replacing σ3 with σ1; that 3-braid's closure is a 2-component link with the same W. Remark 3.1: such K is chiral. Sec. 4.2: the order-2 and order-3 Vassiliev invariants vanish. Sec. 4.3 is a numerical unitarity-of-eigenvalues test. It covers 3-braids (c1,b1;c2,b2) with entries in [-7,7] and W=2m+5 for m=0..5, sampled at k from 0.1 to 150 in steps of 0.1. Only six braids pass, all with W=5. This is heuristic: a finite family and floating-point samples. Sec. 4.4: the related knots β·Δ^{2n} and β^{2k+1} add no constraints. Sec. 4.5 proposes a finite enumeration for W=5 via positive braids with 5+12k crossings. Theorems 3.3/3.4 (added in v2) give analogues for b strands under stronger hypotheses. The paper says that, since no converse to Bigelow's construction is known, Burau(B4) faithfulness would not close the Jones problem. The abstract credits Bigelow (2000) with 'Burau(B4) unfaithful implies infinitely many HOMFLY-trivial nontrivial knots'. Bigelow only conjectured the knot step; Ito (S008) proved it.
    - status: Peer-reviewed and published. Theorems 3.1 and 3.2 have short complete proofs using Morton-Franks-Williams (MFW) and the differential expansion. I re-checked their algebra with exact pure-Python arithmetic. The scripts are kls_check.py and kls_thm31_check.py in <scratch>/7610ac96-4d03-4d32-b526-8a5647837809/scratchpad/wf-c2audit/s008-s010-verify/scripts/. (1) The coefficients equal h_j(q^{±2},q^{±4}) for j<=8. (2) For m=0..6, H_{K_m} has A-exponents exactly {-2m-8,...,-2m-2}. This window has span 6, consistent with MFW, and centres on W=2m+5. Jones is trivial and Alexander is nontrivial. (3) Example (4.4) equals the m=0 member. (4) Every Alexander-and-Jones-trivial candidate spans 5 powers of A², which MFW forbids. No existence or realizability of any family member is shown. The Sec. 4.3 numerics were not re-run.
    - latest_version: arXiv v2 (2024-04-18); journal version AIHPD 13 (2026) 711-746
    - url: https://arxiv.org/abs/2402.02553
    - read_primary: True
    - relevance_to_scaffold: Gives exact necessary conditions for any Jones-trivial closed 4-braid knot. This is precisely the trace-collision regime, which S009 does not touch: kernel-derived knots are HOMFLY-trivial, so the H≠1 family cannot come from kernels. Usable as a rejection filter. It does not certify existence.
    - category: tool
  -
    - source_id: DERIVED-4braid-filter
    - citation: Derived here from S010 Thm 3.1/3.2 and Sec. 4.1, plus MFW; the H=1 clause and the parity remark are mine, not in S010.
    - exact_statement: Let K be a nontrivial knot with V_K=1 that is the closure of β in B4 with exponent sum W. (i) W is odd, because a 4-cycle permutation is odd. (ii) Either H_K=1, in which case MFW puts A-degree 0 in [-W-3,-W+3], so |W|<=3 and W is in {±1,±3}. Or H_K≠1, in which case Δ_K≠1, |W| = 2m+5 >= 5, and H_K is the unique KLS member H_{K_m} (W>0) or its mirror (W<0). (iii) If S009 holds, no such K arises as closure(αβ') with closure(α) the unknot and β' a nontrivial kernel element.
    - status: Derived; clause (ii) for H=1 uses the standard MFW bound and was not taken from any source.
    - read_primary: False
    - relevance_to_scaffold: A cheap rejection test for any explicit candidate of braid index <=4, including any u=1 candidate the project generates.
    - category: tool
  -
    - source_id: IMPL-kernel-searches
    - citation: Synthesis of S009, S008, S007 and S010
    - exact_statement: If S009 is correct, every search for a nontrivial element of ker Burau(B4), ker TL(B4) or ker Jones/Hecke(B4) at generic parameter is searching an empty set. Bigelow's computer-search program in B4 and Ito's Corollary 3 route are therefore dead. Not killed: (a) kernel searches for TL/Jones/RT representations of B_n with n>=5. Burau's unfaithfulness there does not transfer, and per S010 (2024) faithfulness of Jones/RT representations is open in general; I did not search for 2025-26 updates (UNCHECKED). (b) Non-kernel (trace-collision) searches among closed 4-braids. (c) Non-braid routes.
    - status: Conditional on S009's unaudited proof.
    - read_primary: False
    - relevance_to_scaffold: Do not invest in B4-kernel searches unless S009 is refuted. The route is closed only conditionally on an unrefereed preprint.
    - category: barrier
  -
    - source_id: IMPL-trace-collisions
    - citation: Synthesis of S009, S010 (eq. 2.30) and S007
    - exact_statement: S009 says nothing about trace collisions. Faithfulness is injectivity of β -> ρ4(β). The Jones polynomial of a closed 4-braid depends only on W, the trace of reduced Burau_4(β), and the trace of Burau_3 of β's image under B4->B3 (TL_4 = V(4) ⊕ V(3,1) ⊕ V(2,2)). Injectivity of the matrix map constrains none of these trace values. S009 itself says the kernel and image remain wide open and makes no trace statements. If S009 holds, any Jones-trivial nontrivial closed 4-braid knot must be a trace collision. Both the HOMFLY-trivial non-kernel type and the KLS H≠1 family remain open.
    - status: Logical consequence; no source claims otherwise.
    - read_primary: False
    - relevance_to_scaffold: This is the remaining 4-strand counterexample route, and KLS gives its exact HOMFLY shape. Barrier B1 shows Jones-trivial nontrivial links exist, so trace collisions are not absurd in principle.
    - category: context
  -
    - source_id: IMPL-LemmaQ
    - citation: Synthesis vs. the project scaffold (unknotting-number-one slice)
    - exact_statement: No direct bearing on Lemma Q. Lemma Q concerns u(K)=1 knots and 2-string tangles with a rational Kauffman bracket. S008-S010 constrain braid closures and kernel constructions only, and none of them controls unknotting number. Ito's knots have unbounded genus and no control on u. S009, if correct, only says a u=1 counterexample of braid index 4 could not come from a B4 kernel element. S010 and the derived filter give necessary conditions for any u=1 candidate of braid index <=4. None of this touches the hyperbolic crux or the Khovanov-to-Jones gap (B5).
    - status: Assessment
    - read_primary: False
    - relevance_to_scaffold: Use these results only as filters on explicit candidates. They neither prove nor threaten Lemma Q.
    - category: none

### key_claims

  - arXiv:2607.05283, checked 2026-11-02: v1 Mon 6 Jul 2026 16:28:02 UTC and v2 Mon 14 Sep 2026 15:55:28 UTC; the v3 URL returns 'not found'; no withdrawal notice and no journal reference. The Main Theorem (unreduced Burau ρ4: B4 -> GL4(Z[t,t^-1]) is faithful), Cor 1.1 (the Jones representation of B4 is faithful), Prop 1.2 and Thm 6.6/6.9 are word-identical in v1 and v2.
  - The v2 comment calls the changes minor, but v2 materially reworks the proof of the key parity step. It adds Lemmas 6.4-6.6 and new 'with basepoint' configurations in Sec. 5. On my non-audit reading, the modified loop Γ' in Prop 6.7 still has no explicit parity check, and condition (3) of 'properly simple modulo 4-disks' is not addressed. No independent human verification or refutation was found. Wikipedia calls the claim unverified, citing an NYT article I could not read.
  - Ito (arXiv:1402.2028, only v1; Math. Z. 280 (2015) 347-353), Corollary 3, is strictly one-way: Burau(B4) non-faithful implies the Jones polynomial fails to detect the unknot. It is derived from Theorem 1 together with Bigelow's Prop 1.5. Theorem 1: H a nontrivial non-central normal subgroup of B_n and α a braid with unknot closure imply that for every N there is β in H with closure(αβ) hyperbolic, genus >= N, braid index n. The converse is not claimed. If S009 is correct, Corollary 3's hypothesis is false and it yields nothing.
  - Korzun-Lanina-Sleptsov (arXiv:2402.02553 v2; published Ann. Inst. H. Poincaré D 13 (2026) 711-746, DOI 10.4171/AIHPD/213). Thm 3.1: a nontrivial closed 4-braid knot with V=1 and Δ=1 must have H=1. Thm 3.2 with Sec. 4.1: one with V=1 and H≠1 has H = 1 + P4·F for one explicit F per m>=0 (or its mirror), braid writhe W = ±(2m+5) (odd, |W|>=5), nontrivial Δ, and is chiral. The Sec. 4.3 restriction to six W=5 three-braids is a numerical heuristic over a finite family.
  - If S009 is correct, B4 kernel searches (Burau, TL or Jones at generic q) target an empty set. Jones-trivial closed 4-braids via trace collisions (the KLS H≠1 family and HOMFLY-trivial non-kernel braids) remain fully open, as do TL/Jones kernel searches for n>=5. None of S008-S010 constrains unknotting number, so none bears on Lemma Q beyond serving as a braid-index-<=4 filter.
  - The public reaction to S009 is informal. Yang-Hui He (LIMS) endorsed it in Scientific American (2026-07-24), and Columbia's department announced it (2026-08-03). The authors acknowledge pre-posting feedback from Margalit, Bou-Rabee, Dougherty and Farb. The only critique found is an automated AI review (pith.science, v1, verdict CONDITIONAL) flagging the Prop 6.4 parity step.

### summary

I read the inventory records and checked all three items against the primary arXiv pages, PDFs and journal metadata on 2026-11-02.

S009, arXiv:2607.05283, has two versions. v1 is dated 6 Jul 2026 and v2 is dated 14 Sep 2026, which confirms the reported September 14 revision. There is no v3, no withdrawal and no journal reference. The Main Theorem says the unreduced Burau representation ρ4: B4 -> GL4(Z[t,t^-1]) is faithful. It is defined as the action on H_1 of the Z-cover of the 4-punctured disk relative to the preimage of a boundary basepoint. Reduced and unreduced Burau have the same kernel, so the claim covers reduced Burau too. Corollary 1.1 says the Jones representation of B4 is faithful.

The statements are identical in v1 and v2, but v2 substantively reworks the proof of the key parity step. It adds new Lemmas 6.4-6.6 and new 'with basepoint' configurations in Sec. 5. On my reading, which is not an audit, the modified loop Γ' in Prop 6.7 still lacks an explicit parity check. I found no independent verification, rebuttal, erratum, MathOverflow thread or alphaXiv comment. The reaction found is informal and positive: Yang-Hui He in Scientific American and a Columbia department announcement. Wikipedia calls the claim unverified, citing an NYT article that returned HTTP 403, so it is UNCHECKED. An automated AI review of v1 rated it CONDITIONAL.

S008 (Ito, arXiv v1 only; Math. Z. 280 (2015) 347-353) proves Theorem 1. If H is a nontrivial non-central normal subgroup of B_n and α has unknot closure, then for every N there is β in H with closure(αβ) hyperbolic, genus >= N and braid index n. Corollary 3 is strictly one-way: Burau(B4) non-faithful implies the Jones polynomial fails to detect the unknot. It is obtained from Theorem 1 and Bigelow's Prop 1.5. The journal wording is UNCHECKED because the Springer page served a bot challenge.

S010 (Korzun-Lanina-Sleptsov) is now published: Ann. Inst. H. Poincaré D 13 (2026) 711-746, DOI 10.4171/AIHPD/213. The inventory record lacks this. Its main theorems are proved; I re-checked their algebra exactly in pure Python.
- **Thm 3.1:** if a nontrivial closed 4-braid knot has V=Δ=1, then H=1.
- **Thm 3.2 and Sec. 4.1:** if it has V=1 and H≠1, then H is one explicit polynomial determined by the braid writhe W = ±(2m+5), which is odd with |W|>=5. In that case Δ≠1 and the knot is chiral.
- **The rest:** Sec. 4.3's numerics and the proposed search are heuristic.

Implications for the project:
- **B4 kernel searches:** if S009 is correct, they are dead. Burau, TL and Jones of B4 are then all faithful, so Ito's Corollary 3 has a false hypothesis. Kernel searches for n>=5 are not addressed.
- **Trace collisions:** S009 says nothing about them. The Jones polynomial of a closed 4-braid depends only on W and two trace values, and injectivity of the matrix map does not constrain those values. Every remaining 4-strand counterexample would be a trace collision, and the S010 family describes exactly that regime.
- **Lemma Q:** none of this bears on it directly, because no result here controls unknotting number. S010, plus my derived MFW filter (V=1 closed 4-braid knots have odd W, and H=1 forces |W|<=3), can serve as a filter on explicit candidates of braid index <=4.

Files are in <scratch>/7610ac96-4d03-4d32-b526-8a5647837809/scratchpad/wf-c2audit/s008-s010-verify/. That folder holds the extracted texts (txt_2607_v1.txt, txt_2607_v2.txt, txt_ito.txt, txt_bigelow.txt, txt_kls_v1.txt, txt_kls_v2.txt, txt_kls_journal.txt), diff_2607_v1_v2.txt, and scripts/kls_check.py and scripts/kls_thm31_check.py.


## Agent: lit:carmi-cohen


### summary

Status of Carmi-Cohen arXiv:2606.22410 as of 2026-11-02, and verdict on the Oct 31 objection.

1. Version status. The arXiv abstract page, fetched raw on 2026-11-02, lists only v1: Sun 21 Jun 2026 09:56:10 UTC, 3,960 KB, from Avishy Carmi. It is in math.GM with no cross-lists, and has no journal-ref, no MSC field, no trackbacks and no withdrawal notice. The pages /abs/2606.22410v2 and v3 return HTTP 404. The comments field says: main text 54 pp, auxiliary lemmas and proofs 7 pp, 17 figure panels, comments welcome. The arXiv author search for Carmi lists no later knot-theory paper or correction. The alphaXiv page showed no comments when fetched. Standard and extended web searches found no rebuttal. The arXiv API and Semantic Scholar both rate-limited me (HTTP 429), so citing works are UNCHECKED. Not finding a rebuttal does not prove none exists. The local W/work/carmi-cohen.pdf is byte-identical to the arXiv v1 PDF (SHA-256 ba379268b5ca1f614d6cc1ba7cfa1dc3ff588892d7a1e793356ac9c36302e30f). W/work/carmi-cohen.txt is exactly the output of pdftotext -layout on that PDF. Since v1 is the only version, the main claim and Section 5 (Thm 5.6, Lemma 5.8, Prop 5.12) are unchanged.

2. Algebra. I wrote my own pure-Python code; it does not reuse the audit's script. For every odd L from 1 to 101 it checks:
- the recurrence, and the closed form V_L = 1 + D*sum_{j<(L+1)/2} x^{4j} with D = x^2+x^6-x^8-1;
- the reduction V_L = A_L(p) + x B_L(p), done two independent ways (Fibonacci-polynomial formula and greedy elimination);
- exact reconstruction of V_L by substituting p = x - 1/x;
- deg_p = 2L+5, with b_{2L+5} = -1 and a_{2L+5} = 0;
- V(1) = 1, |V(-1)| = 2L+1, and x-span 2L+4.
At L = 23: deg_p = 51, b_51 = -1, deg A = 50. The trefoil expansion matches the paper's own Remark 3.8.
I then built the diagram family from PD codes. The host is the trefoil written as the closure of the 2-braid sigma^3. One crossing is replaced by a horizontal anti-parallel twist of L copies of that crossing. These diagrams are all-positive, alternating, with L+2 crossings. I computed their Jones polynomials three ways: an exhaustive bracket state sum for L <= 11, my own frontier contraction, and Regina 7.4.1 from pip. All three equal the recurrence for every odd L <= 101. The smoothing H = -x - x^5 (the positive Hopf link) is confirmed. Knot Atlas gives the same Jones polynomials (mirror convention q = 1/t) for 5_2 [32] det 7, 7_2 [52] det 11 and 9_2 [72] det 15. So K_1, K_3, K_5, K_7 are 3_1, 5_2, 7_2, 9_2.

3. What the paper asserts. B_host = 3n+l-1, the Cor 3.7 cap for the host shadow with the seed crossing counted. kappa_mach = 11 and B^ = B_host + 11.
- Thm 5.6: given (C1)-(C3), every signed machine state has f_q = 0 for q > B^, for every L.
- Lemma 5.8: given (C1)-(C4), every residual-twist state has f_r = 0 for r > B^+2. It needs no anchor and no Jones-trivial host.
- Prop 5.12: (C1)-(C4) hold for a machine planted at any seed crossing of any host with odd L > 1. (G4) says the residual face is the ordinary anti-parallel twist planted in place of the seed.
The trefoil host is the Section 5 opening figure (twist1.png, a 3-crossing trefoil with one crossing circled; I viewed it). It has n=3, l=1, so B_host = 9, B^ = 20, and Lemma 5.8 gives deg_p <= 22 on the residual twist for every odd L >= 3. The family meets these hypotheses as the paper states them. The bound fails for every odd L >= 9 (L=9 gives 23; L=23 gives 51 with b_51 = -1). A separate check needs no recurrence: the reduced alternating diagram has x-span 2L+4, which exceeds 45 for L >= 21.

4. Direct machine computation (new, beyond the audit). I rebuilt the machine on the trefoil host from the paper's schematics G1_2.png and G2_2.png. With the loop orientation for which (G3) holds:
- (C4), the paired identity (29), (C1c) (non-locked states have deg <= 9, under the limit of 14), (G0) and (G3) all hold on the states I tested. D(rho;alpha) equals K_L, including L=23 with b_51 = -1.
- A full scan up to Reidemeister-II equivalence (16 clasp states x all net twists, L = 3..11) shows the cube's maximum degree is 2L+11. It is reached only at the exceptional state Xi+ = ([++;++]; alpha), with coefficient b = -1. So (C2) and the conclusion of Thm 5.6 fail directly for every L >= 5 (L=5 gives 21 > 20; L=23 gives 57).
- The isotopy claimed in (G2) is false: V(Xi+-) at length L differs from V(Xi+-) at length L-2. Instead V(Xi+- at L) = x^{+-12} times V(the state with all four clasps switched, at L-2), for L = 3..13. This matches the Nov 1 local-move audit's account.
- With the other loop orientation, (G3) fails, and the maximum degree is still unbounded at Xi+.

Verdict: the Oct 31 objection is VALID against v1, the only version. Thm 6.8 and Thm 6.9 rest on Thm 5.11, which rests on Lemma 5.8 and Thm 5.10, which rest on Thm 5.6, which needs (C2) from Prop 5.12 (G2). (C2) fails, so the proof as written does not establish Jones unknot detection. Every knot in the family has nontrivial Jones polynomial, so this is not a counterexample to the conjecture. A version restricted to hosts that are minimal diagrams of nontrivial Jones-trivial knots would need a new proof: (G2) is a local claim relative to the disk boundary and it fails for the trefoil host.

UNCHECKED:
- the local-move audit's reading of figures omega_1 to omega_5;
- the orientation-repair audit's span argument (read, not re-derived);
- Semantic Scholar and arXiv-API citation data;
- alphaXiv comments that may load dynamically.

All files are under <scratch>/7610ac96-4d03-4d32-b526-8a5647837809/scratchpad/wf-c2audit/carmi-cohen-status/:
- scripts: twist_algebra.py, twist_pd_jones.py, regina_check.py (venv/), g2_bracket_check.py, machine_check.py, machine_check2.py, machine_check3.py, machine_check4.py, extra_checks.py;
- full output: RUNLOG.txt;
- downloads: dl-arxiv-abs/, dl-arxiv-pdf/, dl-arxiv-search/;
- source figures: src-extract/;
- v1 text extraction: local-extract/.

### key_claims

  - As of 2026-11-02, arXiv:2606.22410 has only v1. It was submitted Sun 21 Jun 2026 09:56:10 UTC (3,960 KB), is listed only in math.GM, and has no journal-ref or withdrawal notice. The v2 and v3 abstract URLs return 404, and I found no public rebuttal (citation databases UNCHECKED). The local carmi-cohen.pdf is byte-identical to arXiv v1 (SHA-256 ba3792...302e30f), so Section 5 is unchanged.
  - The v1 bounds hold for any host and any L. Thm 5.6 says every signed machine state has f_q = 0 for q > B_host+11. Lemma 5.8 says every residual-twist state has f_r = 0 for r > B_host+13, with no anchor or Jones-trivial hypothesis. Prop 5.12 asserts (C1)-(C4) for any planted machine, with kappa_mach = 11. For the paper's own 3-crossing trefoil host (B_host = 9), the residual twist must have deg_p <= 22 for every odd L >= 3.
  - The paper's (G4) and (H1) identify the residual face with the host diagram whose seed crossing is replaced by an anti-parallel L-twist. So the all-positive residual state is the twist knot K_L: 3_1, 5_2, 7_2, 9_2, and so on. Its Jones polynomial equals the audit's recurrence for every odd L <= 101. This was confirmed three ways: exhaustive bracket state sum, frontier contraction, and Regina 7.4.1, with Knot Atlas matches for 5_2, 7_2 and 9_2.
  - deg_p V_L = 2L+5, with b_{2L+5} = -1 and a_{2L+5} = 0, for all odd L <= 101, checked by two independent reduction methods plus exact reconstruction. L=23 gives degree 51 with b_51 = -1. Lemma 5.8's bound of 22 already fails at L=9 (degree 23). A recurrence-free check also works: the alternating x-span 2L+4 exceeds 45 for L >= 21.
  - In my reconstruction of the machine on the trefoil host, the identification (C4), the paired identity (29), (C1c), (G0) and (G3) hold on the states I tested. The cube's maximum degree is 2L+11, reached only at the exceptional state Xi+ = ([++;++]; alpha) with b = -1. So (C2) and Thm 5.6 fail for every L >= 5, and the (G2) isotopy is false: V(Xi+-) at length L equals x^{+-12} times V(the clasp-switched state at length L-2), not V(Xi+-) at L-2. This assumes my reading of the G1_2 and G2_2 schematics.
  - Verdict: the Oct 31 audit's objection is valid against v1. Thm 6.8 and Thm 6.9 depend, through Thm 5.11, Lemma 5.8 and Thm 5.6, on Prop 5.12 (G2)/(C2), which is false. The proof is invalid as written, but this is not a counterexample to the Jones unknot conjecture.

### items

  -
    - source_id: S005
    - citation: A. Carmi and E. Cohen, On trivial Jones--Vassiliev polynomials, arXiv:2606.22410 [math.GM], v1 21 Jun 2026
    - exact_statement: (Paraphrase of v1.) Thm 6.8: if K is a nontrivial knot whose JVP coefficients f_q = (a_q, b_q) vanish for 1 <= q < N, then N <= 3c(K). Equivalently, every nontrivial knot has a nonzero f_q with 2 <= q <= 3c(K). Thm 6.9: V_K = 1 implies K is the unknot. Cor 6.10 claims Vassiliev-Goussarov unknot detection. JVP conventions: x = t^{1/2} = A^{-2}, p = x - x^{-1}, V = sum_q (a_q + b_q x) p^q, skein x^{-2}V+ - x^2V- = pV0.
    - status: Only v1 exists; not withdrawn; no journal-ref; no public rebuttal located (citation databases UNCHECKED). The proof is invalid as written because the Section 5 compression package is false (see S005-SEC5). The main claim and Section 5 have not changed, since no later version exists.
    - read_primary: True
    - relevance_to_scaffold: If it were valid, it would settle the full conjecture and make Lemma Q unnecessary. It is not, so the unknotting-number-one route stays necessary. Its own 'initialization problem' (lengthening a twist raises the degree cap) is a concrete case of B4 hardness, and the paper does not overcome it.
    - category: audit_target
    - latest_version: v1, Sun 21 Jun 2026 09:56:10 UTC, 3,960 KB. Comments field: main text 54 pp, auxiliary lemmas and proofs 7 pp, 17 figure panels, comments welcome. No v2 (404 on /abs/2606.22410v2). Checked 2026-11-02.
    - url: https://arxiv.org/abs/2606.22410
  -
    - source_id: S005-SEC5
    - citation: Carmi-Cohen v1, Section 5 (paraphrased): Def 5.4, Sec 5.1.1, Thm 5.6 (printed p.30), Lemma 5.8 (pp.31-33), Prop 5.12 (pp.38-48)
    - exact_statement: (Paraphrase.) B_host = 3n+l-1 is the Cor 3.7 cap of the pre-planting host shadow, with the seed crossing counted; kappa_mach = 11; B^ = B_host + 11. Thm 5.6: if (C1)-(C3) hold uniformly over the exterior host family, then f_q = 0 on every signed machine state for all q > B^, independent of L. Lemma 5.8: if (C1)-(C4) hold, then f_r = 0 on every state of the residual face Q_rho for r > B^+2. Proof: the paired identity V-+ + V+- = x^-4 V++ + x^4 V-- - p^2 V00, then a degree shift. Prop 5.12: for a machine planted at any seed crossing with odd L > 1, (G0)-(G8) hold relative to the disk boundary. (G2) says ([s,s;s,s]; s^L) is isotopic to ([s,s;s,s]; s^{L-2}), hence to a non-exceptional state, which gives (C2). (G4) says Q_rho = {y0=0, y0'=-, y_{L+1}=0, y'_{L+1}=+} x Q_Z is the ordinary anti-parallel twist planted in place of the seed crossing. Trefoil host: B_host = 9, B^ = 20, Lemma 5.8 bound deg_p <= 22.
    - status: FALSE for the 3-crossing trefoil host, which meets every stated hypothesis. Lemma 5.8 fails for every odd L >= 9 (residual all-positive state K_L has deg_p = 2L+5; L=23 gives 51, b_51 = -1). Thm 5.6 fails for every L >= 5 (Xi+ has deg_p = 2L+11). The failing hypothesis is (C2)/(G2). Lemma 5.8's algebra is correct, and the x^{+-4} reductions match my computation.
    - read_primary: True
    - relevance_to_scaffold: Regression test: any route that claims degree compression independent of twist length must control the exceptional locked state, whose degree carries the full twist length.
    - category: audit_target
    - latest_version: v1 (unchanged; only version)
    - url: https://arxiv.org/pdf/2606.22410v1
  -
    - source_id: S005-FIG
    - citation: Carmi-Cohen v1 arXiv source figures: twist1.png, twist2_white_bg.png (Sec 5 opening illustration), G1_2.png (machine), G2_2.png ((G4) residual). Extracted from the local W/work/carmi-cohen-source.tar into my scratch dir.
    - exact_statement: twist1.png shows a 3-crossing oriented trefoil diagram with one crossing circled. twist2_white_bg.png shows that crossing replaced by a planted twist. G1_2.png shows two upward strands, each clasped twice (y0, y0' on the left; y_{L+1}, y'_{L+1} on the right) by the ends of a closed loop that carries the anti-parallel twist Z. G2_2.png shows the double smoothing as an ordinary anti-parallel twist joining the four endpoints.
    - status: Viewed. These figures confirm that the audit's family is the Section 5 host and residual twist. My machine reconstruction relies on this reading of the shadow. omega_1..5.png (the (G2) movie) were NOT viewed: UNCHECKED.
    - read_primary: True
    - relevance_to_scaffold: Pins the geometric identification that a skeptic must accept for the objection.
    - category: context
    - url: https://arxiv.org/abs/2606.22410
  -
    - source_id: S006
    - citation: Jones unknot detection: a concrete obstruction to the Carmi-Cohen proof (project audit prepared with Codex, 31 Oct 2026), W/outputs/jones-unknot-proof-audit.pdf with verify_twist_obstruction.py; summarized in CLAUDE_JONES_RESEARCH.md S006 and section 7
    - exact_statement: (Paraphrase.) For the trefoil-host odd twist family: V_1 = x^2+x^6-x^8 and V_L = x^4 V_{L-2} + x^2-x^4+x^6-x^8. The unique top monomial is -x^{2L+6}, so deg_p V_L = 2L+5 and b_{2L+5} = -1; L=23 gives b_51 = -1. The paper's package (Prop 5.12, Thm 5.6, Lemma 5.8) implies deg_p <= 9+11+2 = 22 for every L. The audit also gives an alternating-span check (span 50 vs at most 45 at L=23). It does not claim to identify which geometric step fails.
    - status: VERIFIED. The recurrence, closed form and deg/coefficient claims hold for every odd L <= 101 by two reduction methods. The diagram identification is confirmed by my own bracket state sum, frontier contraction and Regina 7.4.1. The paper's statements apply to this host as written. The objection is valid against v1. The gap it left open (which step fails) is now closed by my machine computation: (C2)/(G2).
    - read_primary: True
    - relevance_to_scaffold: Confirms Carmi-Cohen gives no shortcut. The algebra replay is now matched by a geometric replay (task T001 in the inventory).
    - category: audit_target
    - url: file://~/Documents/Codex/2026-10-31/it-is-an-open-problem-whether-4/outputs/jones-unknot-proof-audit.pdf
  -
    - source_id: AUD-LOCALMOVE
    - citation: Jones unknot detection: a concrete failure in the claimed proof (project audit, checked 31 Oct 2026), W/outputs/jones-preprint-local-move-audit.txt
    - exact_statement: (Paraphrase.) The relative-boundary isotopy in Prop 5.12(G2) does not preserve the four clasp crossings. The pictured endpoint switches all four and reverses the loop's arrows. A 7-crossing bracket certificate gives the initial closure span 20, the claimed endpoint span 4, and the actual endpoint A^6 times the initial bracket. The corrected relation carries a factor x^{12s}, which mixes JVP levels.
    - status: Bracket arithmetic reproduced exactly from its three PD codes (spans 20, 4, 20; actual endpoint = A^6 times initial). Its account is independently corroborated by my machine reconstruction: V(Xi+- at L) = x^{+-12} V(all-clasps-switched state at L-2) for L = 3..13, and V(Xi+- at L) != V(Xi+- at L-2). Its reading of omega_1..5.png was NOT re-done (UNCHECKED).
    - read_primary: True
    - relevance_to_scaffold: Locates the specific false step, (G2), behind the twist-family contradiction.
    - category: audit_target
    - url: file://~/Documents/Codex/2026-10-31/it-is-an-open-problem-whether-4/outputs/jones-preprint-local-move-audit.txt
  -
    - source_id: AUD-ORIENT
    - citation: Jones unknot detection: a concrete repair attempt and its limit (project audit, 1 Nov 2026), W/outputs/jones-orientation-repair-audit.txt
    - exact_statement: (Paraphrase.) Normalizing by self-writhe only, F = x^{-3 lk} V, and squaring to H = F^2 removes the orientation defect and keeps finite-type order. However, any family T_m = A + B x^{dm} with both A and B nonzero has span dm + O(1). The locked clasp state on the unknot host has this form with d = 4, so no fixed JVP degree bound holds after the repair.
    - status: Read; arguments NOT independently re-derived (UNCHECKED). It is consistent with my finding that the exceptional-state degree grows like 2L+11.
    - read_primary: True
    - relevance_to_scaffold: Shows that a natural repair of the compression step also fails, which supports the hardness diagnosis.
    - category: context
    - url: file://~/Documents/Codex/2026-10-31/it-is-an-open-problem-whether-4/outputs/jones-orientation-repair-audit.txt
  -
    - source_id: TOOL-REGINA
    - citation: Regina 7.4.1 (PyPI wheel), Link.fromPD and Link.jones(); installed in scratch venv
    - exact_statement: Link.jones() returns a Laurent polynomial in sqrt(t), which is the paper's x. On KnotTheory's Knot[3,1] PD it returns x^-2 + x^-6 - x^-8. That is the left-handed trefoil, consistent with the paper's x^2 + x^6 - x^8 for the positive trefoil.
    - status: Used as a third backend. It equals the recurrence and my bracket code for all odd L in 1..101 on the same PD codes (writhe L+2, all crossings positive).
    - read_primary: True
    - relevance_to_scaffold: An independent exact Jones backend, usable for future replays.
    - category: tool
    - url: https://pypi.org/project/regina/
  -
    - source_id: CTX-KNOTATLAS
    - citation: The Knot Atlas pages 5_2, 7_2, 9_2 (fetched 2026-11-02)
    - exact_statement: 5_2: Conway [32], det 7. 7_2: Conway [52], det 11. 9_2: Conway [72], det 15. Their Jones polynomials in q equal V_3, V_5, V_7 from the recurrence under q = 1/t, the mirror convention.
    - status: Matches. This identifies K_L (L = 3, 5, 7) as the twist knots with L half-twists, by Jones polynomial plus construction.
    - read_primary: True
    - relevance_to_scaffold: External check that the family is the ordinary twist-knot family.
    - category: context
    - url: https://katlas.org/wiki/7_2
  -
    - source_id: CTX-SEARCH
    - citation: arXiv author search 'Carmi, Avishy' and topic search 'Jones polynomial unknot' (2026-11-02); alphaXiv abs/2606.22410; WebSearch (standard and extended); Semantic Scholar API; arXiv export API
    - exact_statement: The author search returned 26 results, with 2606.22410 the only Jones/knot-detection paper and no later correction. The topic search showed no post-June-2026 rebuttal. alphaXiv rendered v1 only, with no discussion entries. Web searches found no rebuttal or erratum. Semantic Scholar and the arXiv API returned HTTP 429.
    - status: No public rebuttal, revision or withdrawal located. Citing papers UNCHECKED because of rate limits. alphaXiv comments that load via JavaScript may be invisible to WebFetch (UNCHECKED). Not finding a rebuttal does not prove none exists.
    - read_primary: True
    - relevance_to_scaffold: Version and correction ledger for S005 (inventory task T002).
    - category: context
    - url: https://www.alphaxiv.org/abs/2606.22410


## Agent: audit:cable-algebra


### summary

I re-derived all of section (e) independently with exact pure-Python Laurent arithmetic in Z[A,A^-1] and Z[zeta8]. I did not run or import any archive script. I read cable_models.py only after my results existed, to interpret the archive's output file.

Every claim e1 to e5 holds exactly as written under the convention I_1 = A^-1*Q0 + A*Qinf and Q_(1/2) = R(I_-2) = (1-A^-4)*Q0 + A^2*Qinf. This I_1 is the convention cables.txt states; the message itself does not fix it. With the other choice, I_1 = A*Q0 + A^-1*Qinf (and Q_(1/2) = R(I_-2) = (1-A^4)*Q0 + A^-2*Qinf), the formulas for u_q, d_q, r_q, the recurrence and x_q'(1) hold only after A <-> A^-1, so the derivative sign flips to -4(q-s). The mirror-invariant facts hold in both conventions: divisibility, r_q(1), d_q(zeta)=4 and x_q(zeta)=0. If Q_(1/2) is taken as R(I_2) relative to the chosen I_1, the meridian eigen-row property f_inf M = u f_inf fails for every q, so (e1) itself pins Q_(1/2).

I checked all 22 odd q in [-21,21] exactly and also proved every statement for all odd q. M_q factors exactly as L(I_1)^(-2q) N L(I_1)^m, where N = S L_-1 L_Q S L_-2 S is a fixed block. Exact computation gives:
- f_inf N = -A^-3 f_inf
- normalized N = [[1,0],[A^-6 - A^-2, A^-8(1-A^4)(1+A^8)]]
- f_inf(I_1) = -A^3, with normalized twist data x_1 = -A^-2 and d_1 = -A^-4

These give closed forms for u_q, d_q and r_q = (-1)^m A^(2-12m)(A^(16m)-1)/(1-A^16) + A^2(1-(-A^4)^m)/(1+A^4). Both terms are Laurent polynomials for every integer m. I machine-checked x_q = d_q r_q and the recurrence as identities in two variables (A, Y = A^(4m)) for both parities of m. The s in the recurrence is s_q = (-1)^((q-1)/2), the sign for q; with s_(q+2) the recurrence fails at every q.

The a_2 identity follows symbolically from the cabling formula. An independent reduced-Burau computation on explicit (2,q)-cable braids confirms both the formula and the identity: 6 companions times 10 values of q, 60 cases.

The final step of (e) contains no algebraic step I could not reproduce, including w_J(1)=0 for type-0 tangles. The only inputs I did not check are geometric or come from outside (e), and are recorded as UNCHECKED in the e6 entry.

Archive comparison found no discrepancy in any normalized quantity. One side observation on section (a): under the same convention, (a)'s cap constant C(A) belongs to the mirror of (e)'s Q_(1/2). This is a chirality-label mismatch only and changes no conclusion.

### conventions_used

R=Z[A,A^-1], delta=-A^2-A^-2. Brackets are column vectors (a,b) for a*Q0+b*Qinf. Horizontal addition is the commutative product (a,b)*(c,d)=(ac, ad+bc+delta*bd), so Q0 is the identity and Qinf^2=delta*Qinf. L_B=[[a,0],[b,a+delta*b]] is multiplication by B and is multiplicative: L_(BC)=L_B L_C. f_inf=(1,delta) and f_0=(delta,1) are row vectors. The quarter turn R acts as the swap S. Basis change uses P=[[1,-delta],[0,1]] with columns Q0 and Qinf-delta*Q0. Normalized matrices are P^-1 M P / u in column-vector convention: [[1,0],[x,d]] means Q0 maps to Q0 + x*(Qinf-delta*Q0). Here x=-w, d=det(M)/u^2, and x_B=b/f_inf(B), d_B=a/f_inf(B) for a tangle B.

Working convention (the formulas hold as written): I_1 = A^-1*Q0 + A*Qinf (the archive's stated TL2 convention). Then I_-1 = A*Q0 + A^-1*Qinf, I_2 = A^-2*Q0 + (1-A^4)*Qinf and I_-2 = A^2*Q0 + (1-A^-4)*Qinf. Q_(1/2) = R(I_-2) = (1-A^-4)*Q0 + A^2*Qinf, with f_inf(Q_(1/2)) = -A^4-A^-4 and f_0(Q_(1/2)) = A^-6. With the fraction F = -i*b/a at A = zeta = exp(pi*i/4), this convention gives F(I_n)=n, F(R T)=-1/F(T), F(Q_(1/2))=1/2 and F(R(I_-3))=1/3.

Other choice: I_1 = A*Q0 + A^-1*Qinf (with Q_(1/2) = R(I_-2) = (1-A^4)*Q0 + A^-2*Qinf). The formulas then hold only up to the mirror A <-> A^-1.

Other conventions: the Jones variable is t=A^-4 with V=(-A^3)^-w <D>. s = s_q = (-1)^((q-1)/2) and m = (q-1)/2; Python floor division gives exact m for negative q. Exact Z[zeta8] arithmetic uses zeta^4=-1.

### claims

  -
    - id: e1
    - claim: f_inf M_q = u_q f_inf with u_q = (-1)^((q+1)/2) A^(-9(q+1)/2), where M_q = L_(I_-2q) S L_(I_-1) L_(Q_1/2) S L_(I_-2) S L_(I_m), for odd q in [-21,21].
    - verdict: CONFIRMED
    - method: Built M_q exactly as a 2x2 matrix over Z[A,A^-1] for all 22 odd q in [-21,21] and computed the row f_inf M_q. Checked that its second entry equals delta times its first, that the first entry is a unit, and that it equals the formula. Repeated for both I_1 choices and both candidate brackets of Q_(1/2). All-q proof: L is multiplicative, so M_q = L(I_1)^(-2q) N L(I_1)^m exactly (also checked as matrices for every q in range). Exact computation gives f_inf N = nu f_inf with nu = -A^-3, so u_q = nu * f_inf(I_1)^(m-2q) = -A^-3 (-A^3)^(-3m-2) = (-1)^(m+1) A^(-9(m+1)).
    - evidence: Working convention (I_1 = A^-1 Q0 + A Qinf, Q = R(I_-2) = (1-A^-4)Q0 + A^2 Qinf): the eigen-row holds and u_q matches the formula for all 22 q. Values: u_1=-A^-9, u_3=A^-18, u_5=-A^-27, u_15=A^-72, u_17=-A^-81, u_-1=1, u_-3=-A^9. f_inf N = (-A^-3, A^-5+A^-1) = -A^-3 (1,delta). Other choice (I_1 = A Q0 + A^-1 Qinf, Q = (1-A^4)Q0 + A^-2 Qinf): the eigen-row holds, but u_q equals the formula only after A -> A^-1. Q_(1/2) = R(I_2) relative to either I_1: the eigen-row property fails for all 22 q, so (e1) pins Q_(1/2) = R(I_-2), fraction +1/2 under z -> -1/z. Output file: <scratch>/7610ac96-4d03-4d32-b526-8a5647837809/scratchpad/wf-c2audit/e-algebra/e_check_output.txt
  -
    - id: e2
    - claim: In the basis (Q0, Qinf - delta Q0), M_q/u_q = [[1,0],[x_q,d_q]] with d_q = s A^(6(q-1)) (1-A^4)(1+A^8), and x_q is the preferred T(2,q) defect.
    - verdict: CONFIRMED
    - method: Computed P^-1 M_q P exactly. Checked that the top row is (u_q, 0), set x_q = entry21/u_q and d_q = entry22/u_q, and compared d_q with the formula and with det(M_q)/u_q^2. All-q proof: d_q = d_N * d_1^(-3m-2) with d_N = A^-8(1-A^4)(1+A^8) (computed from N) and d_1 = -A^-4, which gives (-1)^m A^(12m)(1-A^4)(1+A^8). Checked that the longitude is preferred: x_q(zeta) = 0 exactly in Z[zeta8] for every q in range, and for all q from the closed form (r_q(zeta) = zeta^2 m (1 - s*zeta^(-12m)) = 0). Integer twists shift this by |x_(I_n)(zeta)| = |n| (checked for |n| <= 12), so -2q is the unique integral adjustment that gives a determinant-zero longitude closure.
    - evidence: The top row is exactly (u,0) and d_q = formula = det(M_q)/u_q^2 for all 22 q. Factored forms: d_q = +-A^(6(q-1)) Phi_1 Phi_2 Phi_4 Phi_16. x_3 = A^2 Phi_1 Phi_2 Phi_4 Phi_8 Phi_16 Phi_24 = -A^2(1-A^4)(1+A^8)(1+A^12) = -A^2 F, matching section (c). The bracket of C_3(Q0) equals that of the archived trefoil quotient R(I_-1+Q_1/2+Q_1/3)+I_-6. F divides x_q for all 22 q, consistent with (a). x_q(1)=0 for all q. The (Q0,Qinf) form in cables.txt, [[1-delta x, delta(1-d) - delta^2 x],[x, d + delta x]], also matches. The geometric claim that the Q0 filling is the T(2,q) exterior is only reasoned: a Montesinos (-1, 1/2, m/q) piece with unknotted meridian closure, det |2m - q| = 1. That part, and its chirality, is not algebraically verified.
  -
    - id: e3
    - claim: r_q = x_q/d_q is a Laurent polynomial; r_1 = 0, r_-1 = 0, r_3 = A^-10(1+A^12); r_(q+2) = -A^4 r_q + A^2 + s A^(-6q-4); r_q(1) = (1-sq)/2.
    - verdict: CONFIRMED
    - method: For each q, exact Laurent long division (zero remainder, integer quotient, re-multiplied as a check). Tested the recurrence with s = s_q and with s = s_(q+2). All-q proof: the closed form r_q = (-1)^m A^(2-12m)(A^(16m)-1)/(1-A^16) + A^2(1-(-A^4)^m)/(1+A^4) matches all 22 cases. The identity x_q = d_q r_q and the recurrence were machine-verified as identities in two variables (A, Y = A^(4m)) for sigma = +-1. Also re-derived the message's own route by hand and by computation. The tangle identity C_q(I_n) = C_(q+2n)(Q0) + I_(4n) holds exactly at the bracket level for n in {+-1,+-2,+-3}. With the normalized twist action x_(I_k) = (1-(-A^-4)^k)/delta and d_(I_k) = (-A^-4)^k, this gives r_(q+2) = -A^4 r_q - A^4 x_(I_1) - x_(I_4)/(d_(I_4) d_(q+2)) = -A^4 r_q + A^2 + s_q A^(-6q-4). At A=1 the closed form gives -s*m + (1-s)/2 = (1-sq)/2.
    - evidence: Division is exact for all 22 q. r_1 = 0, r_-1 = 0, r_3 = A^-10 + A^2, r_-3 = A^-2 + A^10, r_5 = -A^-22 - A^-6 + A^2 - A^6. r_15 = A^-82+A^-66+A^-50+A^-34+A^-18+A^-2+A^2-A^6+A^10+A^18-A^22+A^26. r_17 = -A^-94-A^-78-A^-62-A^-46-A^-30-A^-14-A^6+A^10-A^14-A^22+A^26-A^30. The recurrence holds for every q in [-21,19] with s = s_q = (-1)^((q-1)/2), the sign for q, equivalently -s_(q+2). With s = s_(q+2) it fails at every q. The two-variable check is ALL-Q IDENTITIES OK. r_q(1) = (1-sq)/2 for all 22 q, e.g. r_-21(1)=-10 and r_21(1)=-10. Mirror symmetry r_(-q)(A) = r_q(A^-1), and likewise for x and d. Output file: <scratch>/7610ac96-4d03-4d32-b526-8a5647837809/scratchpad/wf-c2audit/e-algebra/allq_output.txt
  -
    - id: e4
    - claim: Table: required w_J(1) = r_q(1) = 0, 2, -2, 8, -8 for q = 1, 3, 5, 15, 17, with divisibility 'yes' and required a_2(J) = 0, -1/4, -3/4, -7, -9. Identity a_2(C_(2,q)(J)) = 4 a_2(J) + (q^2-1)/8, and a_2 = 0 implies q = +-1 mod 16.
    - verdict: CONFIRMED
    - method: r_q(1) was read off the exact r_q. The required a_2(J) = -(q^2-1)/32 was computed with Fractions. a_2 calculus: for symmetric f with f(1)=1, a_2 = f''(1)/2 = (sum of k^2 c_k)/2; a_2(fg) = a_2(f) + a_2(g); a_2(f(t^p)) = p^2 a_2(f). a_2(T(2,q)) = (q^2-1)/8 was checked exactly for odd |q| <= 41. As an independent check of the cabling formula itself, I computed Alexander polynomials with a reduced Burau representation (braid relations verified) for explicit (2,q)-cable braids. Each braid is the blackboard 2-parallel plus sigma_1^(q - 2*writhe). Companions: unknot, both trefoils, 4_1, T(2,5) and 5_2. Values of q: +-1, +-3, +-5, +-15, +-17.
    - evidence: r_q(1) = 0, 2, -2, 8, -8 and divisibility holds for q = 1, 3, 5, 15, 17. Required a_2(J) = 0, -1/4, -3/4, -7, -9. In all 60 Burau cases, Delta_C = Delta_J(t^2) Delta_T(2,q)(t) and a_2(C) = 4 a_2(J) + (q^2-1)/8. Examples: J=4_1, q=15 gives a_2(C)=24; J=5_2, q=17 gives 44. Odd q with 32 | q^2-1 have residues {1,15,17,31} mod 32, i.e. q = +-1 mod 16. The premise that a_2 = 0 is necessary for a flat preferred quotient comes from outside (e) and is UNCHECKED here. Output file: <scratch>/7610ac96-4d03-4d32-b526-8a5647837809/scratchpad/wf-c2audit/e-algebra/alex_output.txt
  -
    - id: e5
    - claim: |d_q(zeta)| = 4 at zeta = exp(pi*i/4), and x_q'(1) = 4(q-s) (d/dA at A=1).
    - verdict: CONFIRMED
    - method: Exact evaluation in Z[zeta8] (zeta^4 = -1), with |z|^2 computed as z * conj(z). Derivative at A=1 computed as the sum of e*c over the terms of x_q. All-q proof: d_q(zeta) = 4 s zeta^(12m) = 4 s^2 = 4. x_q'(1) = d_q'(1) r_q(1) + d_q(1) r_q'(1) = (-8s)(1-sq)/2 = 4(q-s), using d_q(1) = 0 and d_q'(1) = -8s, both checked. The supporting relation x'(1) = -4 lk(L) follows from f_0(T_hat) = delta + (1-delta^2)x, V_L'(1) = -3 lk, and f_0(T_hat) = V_L(A^-4) when the closures are oriented compatibly (w_L = w_U). It was checked on T = I_2: x = A^-6 - A^-2, x'(1) = -4, f_0(T_hat) = -A^-2 - A^-10 = V(positive Hopf)(A^-4).
    - evidence: d_q(zeta) = Z8(4,0,0,0) exactly, i.e. the value is 4 and not merely of modulus 4, with |.|^2 = 16 for all 22 q. x_q'(1) = 4(q-s) for all 22 q: 0, 16, 16, 64, 64 for q = 1, 3, 5, 15, 17; -16 for q = -3; 80 for q = 21. Under the other I_1 convention the value is -4(q-s). lk = s - q is always 0 mod 4, consistent with det(L) = 0 (det = 2 lk mod 8). Since d_q(1) = x_J(1) = 0, the output satisfies x_out'(1) = x_q'(1) for every input J.
  -
    - id: e6
    - claim: Final step: cancellation needs w_J = r_q, but every actual preferred quotient has w_J(1) = 0, so a flat output is impossible unless q = s, i.e. q = +-1.
    - verdict: CONFIRMED
    - method: Algebra: by the normalized matrix, x_out = x_q + d_q x_J. R is a domain and d_q != 0, so flatness holds iff x_J = -r_q, i.e. w_J = r_q. Evaluating at A=1 gives w_J(1) = (1-sq)/2. Lemma: for any 2-string tangle diagram with n crossings, k closed loops and connectivity type tau, <T>(A=1) = (-1)^n (-2)^k e_tau, where e_0 = Q0, e_inf = Qinf and e_1 = -(Q0+Qinf). This follows from V(1) = (-2)^(c-1) and writhe = crossing count mod 2; the two closures determine the bracket because det [[1,-2],[-2,1]] = -3 != 0. Hence any type-0 tangle has b(1) = 0 and x_J(1) = b(1)/f_inf(1) = 0. The lemma was checked on 4000 random algebraic tangles, 193 of them with closed loops, with connectivity tracked combinatorially. Finally, (1-sq)/2 = 0 iff q = s iff q in {1,-1}.
    - evidence: I reproduced every algebraic step; none failed. The lemma check returned True; types seen were 0: 885, inf: 926, 1: 2189. For q = +-1, x_q = 0 and d_q != 0, so x_out = 0 iff x_J = 0. The obstruction is symmetric under q -> -q, because r_q(1) is even in q and r_(-q)(A) = r_q(A^-1). UNCHECKED, because they are not algebra: (i) that C_q is the inherited (2,q)-cable operator on actual quotients (the Seifert-cover identification); (ii) that the input is an actual preferred quotient, i.e. a type-0 2-string tangle with unknotted meridian closure.
  -
    - id: e7
    - claim: Comparison with work/defect-calculus/cable-check-output.txt and cables.txt.
    - verdict: CONFIRMED
    - method: Compared my values item by item with both files.
    - evidence: No discrepancy in any normalized quantity. DIRECT SHELL lines: u, dprime(1), xprime(1) and target x(1) match mine for q = 1, 3, 5, 15, 17, -1, -3. The d lines and droot {0:4} match. The 'x0/d' polynomials are identical to my r_q for all 7 values of q. The archive's 'meridian' lines (-A^-3, A^-18, A^-30, A^-90, A^-102, 1, -A^9) differ from u_q at q = 1, 5, 15, 17 by the units A^6, -A^-3, A^-18 and -A^-21. These are meridian brackets of the continued-fraction presentation R(I_-1+Q_1/2+Q_((q-1)/(2q)))+I_-2q. I reproduced all 7 values exactly with my own code (archive_meridian_output.txt), and the normalized x agrees, so these are framing-curl units only. All formulas in cables.txt agree with mine: I_1, a_n, b_n, det L_n = (-A^2)^n, det L_Q = A^-8(1-A^4)(1+A^8), the Mhat (Q0,Qinf) form, x(T+I_k), the recurrence with s = (-1)^((q-1)/2), the table including a_2(T(2,q)) = 0, 1, 3, 28, 36, r_5, V_L = delta + (1-delta^2)x, x'(1) = -4 lk, and lk = s - q. Note: cable_models.py checks only the 7 sample values of q. The all-q claim in cables.txt rests on a hand derivation, which my N-factorization and two-variable identity now machine-verify.
  -
    - id: x1
    - claim: Side observation (outside (e)): under the convention that makes (e) hold, section (a)'s exact cap constant C(A) = A^-10(A^4-1)(A^8+A^4+1) is produced by the cap R(I_2) (fraction -1/2), the mirror of (e)'s Q_(1/2).
    - verdict: CONFIRMED
    - method: Computed V_B(A^-4) = f_0(L_cap T_hat)/f_0(cap) exactly on the q=3 output for both caps, with T_hat the meridian-normalized output bracket. Compared each capped knot's bracket, up to a unit and mirror, with Montesinos knots M(e; 1/2, b/3, c/k) built in the same algebra (homology-sphere condition imposed).
    - evidence: Cap (1-A^4)Q0 + A^-2 Qinf = R(I_2): V_B - 1 = C(A) x exactly. With (e)'s Q_(1/2) as the cap, the coefficient is -A^8 C(A). On the q=3 output, (a)'s cap gives the bracket of M(-1; 1/2, 1/3, 2/13), exceptional fibers (2,3,13); (e)'s Q_(1/2) gives M(-1; 1/2, 1/3, 2/11), fibers (2,3,11). +1/2 surgery on the RH trefoil has order 11 and on the LH trefoil order 13. So (a)'s '+1/2' label and (e)'s T(2,3)/Q_(1/2) labels use opposite slope-sign conventions, unless T(2,3) there means the LH trefoil. This is harmless: C changes by a unit, det(B) = 1 either way, and (e) is mirror-symmetric. The 'minus_half'/'plus_half' line in cable-check-output.txt was not traced (UNCHECKED). Output files: <scratch>/7610ac96-4d03-4d32-b526-8a5647837809/scratchpad/wf-c2audit/e-algebra/cap_output.txt and <scratch>/7610ac96-4d03-4d32-b526-8a5647837809/scratchpad/wf-c2audit/e-algebra/cap_montesinos_output.txt

### discrepancies_with_codex_artifacts

None in any normalized quantity: u_q from DIRECT SHELL, d_q, d_q(zeta)=4, d_q'(1), x_q'(1), the targets, and the r_q polynomials for q = 1, 3, 5, 15, 17, -1, -3 all match.

Three notes. (1) The 'meridian' column of cable-check-output.txt is not u_q. It is the meridian bracket of the continued-fraction torus quotient, which differs from the shell output by framing-curl units at q = 1, 5, 15, 17. My own construction reproduces it exactly, and normalized x agrees. (2) cable_models.py checks only 7 sample values of q. The all-q assertion in cables.txt rests on a hand derivation, which I independently re-derived and machine-checked through the factorization M_q = L(I_1)^(-2q) N L(I_1)^m and a two-variable identity. (3) Side issue outside (e): under the archive's I_1 convention, section (a)'s C(A) belongs to the mirror of (e)'s Q_(1/2). The two differ by the unit -A^8, so this is a slope-sign or chirality label mismatch only; no conclusion changes.

### scripts_written

  - <scratch>/7610ac96-4d03-4d32-b526-8a5647837809/scratchpad/wf-c2audit/e-algebra/lp.py
  - <scratch>/7610ac96-4d03-4d32-b526-8a5647837809/scratchpad/wf-c2audit/e-algebra/e_check.py
  - <scratch>/7610ac96-4d03-4d32-b526-8a5647837809/scratchpad/wf-c2audit/e-algebra/allq_check.py
  - <scratch>/7610ac96-4d03-4d32-b526-8a5647837809/scratchpad/wf-c2audit/e-algebra/alex_check.py
  - <scratch>/7610ac96-4d03-4d32-b526-8a5647837809/scratchpad/wf-c2audit/e-algebra/extra_check.py
  - <scratch>/7610ac96-4d03-4d32-b526-8a5647837809/scratchpad/wf-c2audit/e-algebra/archive_meridian_explain.py
  - <scratch>/7610ac96-4d03-4d32-b526-8a5647837809/scratchpad/wf-c2audit/e-algebra/cap_chirality_check.py
  - <scratch>/7610ac96-4d03-4d32-b526-8a5647837809/scratchpad/wf-c2audit/e-algebra/cap_montesinos_check.py


## Agent: audit:scalar-sums-algebra


### claims

  -
    - id: a1
    - claim: f_0(T_hat) = delta + (delta^2 - 1) w, so w is recovered by exact division.
    - verdict: CONFIRMED
    - method: Own exact Laurent arithmetic (dict exponent->int, Fraction long division) in the module R*Q0 + R*Qinf. Checked symbolically, on 200 random exact T_hat, and on the trefoil quotient.
    - evidence: f_inf(v)=0 and f_0(v)=delta^2-1=A^-4+1+A^4. ker f_inf=R*v is free of rank 1 because a+delta*b=0 iff (a,b)=-b*(delta,-1). So T_hat-Q0 lies in ker f_inf, and w is minus the Qinf-coefficient of T_hat. This gives f_0(T_hat)=delta+(delta^2-1)w identically. On 200 random T_hat, exact division of f_0(T_hat)-delta by delta^2-1 had zero remainder, integral quotient, and returned w. For the trefoil quotient it returned A^2 F. Also confirmed the message's side remark: f_0(Q0-delta*Qinf)=0, so the kernel of the numerator functional is spanned by Q0-delta*Qinf.
  -
    - id: a2
    - claim: With t=A^-4: G(A^-4) is a Laurent unit times C(A)F(A), so G | (V_B-1) together with V_B(A^-4)-1=C(A)x gives F | x. List the zeros of F as values of t.
    - verdict: CONFIRMED
    - method: Exact substitution t=A^-4 and unit_ratio test. Numerical root checks for the zero list (24 A-roots, simplicity via F'(a)!=0).
    - evidence: G(t)=1-t+t^2-t^3-t^6+t^7-t^8+t^9. The exact identity is G(A^-4) = -A^-26 * C(A) * F(A), with C(A)=A^2-A^-10. If P(t)=G(t)Q(t) with Q in Z[t^+-1], then x=(V_B(A^-4)-1)/C = -A^-26 F(A) Q(A^-4), which lies in F*R. This uses only that R is a domain and C is nonzero. Factor map from F to t: (1-A^4) gives t=1; (1+A^8) gives t=+-i; (1+A^12) gives t=-1 and t=exp(+-i pi/3). The zero set of F in t is exactly {1, i, -i, -1, exp(i pi/3), exp(-i pi/3)}. F has 24 simple roots in A (deg F=24 = 6 t-values x 4 preimages), and the three factors have disjoint roots. C vanishes at t in {1, exp(+-2 pi i/3)}, so after cancelling C, F keeps one (t-1) and no Phi_3.
  -
    - id: a3
    - claim: Cap identity: for the closure by the '+1/2 cap', V_B(A^-4)-1 = C(A)x with C=A^-10(A^4-1)(A^8+A^4+1), as an identity affine in w; report the exact units.
    - verdict: CONFIRMED_WITH_CONVENTION_FIX
    - method: (i) Symbolic closure functionals in the module R^2. (ii) Independent explicit-diagram engine: planar crossings in ccw order, full Kauffman state sum, orientation traversal, writhe. Kauffman A-smoothing rule checked by kink invariance and by positive-braid anchors (RHT t+t^3-t^4, T(3,4), T(3,5)). Applied to the 12-crossing trefoil quotient and to 60 random pairing-type-0 tangles whose D-closure is a knot.
    - evidence: The closure is B=N(T+R), where R is the two-crossing vertical twist with bracket (1-A^4)Q0+A^-2Qinf. In the archive crossing convention (<1>=A^-1Q0+A*Qinf) this R is two vertically stacked <-1> crossings, equal to rot(<2>), with tangle fraction -1/2 under z->-1/z. The archive code builds it as cap_tangle=integer_tangle(2)[::-1]. Its closure functional is (1-A^4)f_0 + A^-2 f_inf, with f_R(Q0)=A^6, f_R(Qinf)=-A^4-A^-4 and f_R(v)=A^-4-A^8. R has the meridional pairing, so B is a knot and T's arcs get the same orientation in B as in D(T). The writhe difference writhe(B)-writhe(D(T)) was exactly +2 for every tested T (trefoil: -4 vs -6; 60 random tangles: always +2). Units needed: divide by f_inf(T)=(-A^3)^{writhe D(T)} (for the trefoil, A^-18), then apply (-A^3)^-2=A^-6. Result: V_B(A^-4) = A^-6(A^6 + w(A^-4-A^8)) = 1 + (A^-10-A^2)w = 1 + C(A)x exactly. There is no further unit and no additive monomial. The general identity V_B*f_inf(T) = (-A^3)^-2*f_R(T)*V_{D(T)} held on all 60 random tangles. Trefoil instance from the explicit 14-crossing diagram: V_B(t) = t^2-t+2-t^-1-t^-4+t^-5-t^-6+t^-7 = 1 + t^-7 G(t), equal to 1+Cx with x=-A^2F. Opposite half-cap (bracket (1-A^-4)Q0+A^2Qinf, cap writhe -2): V_B(A^-4)-1 = -A^8 C(A) x = -A^-2(A^4-1)(A^8+A^4+1)x, matching the archive's 'opposite choice' prefactor. Trefoil instance: V_B-1 = -t^-9 G. Mirroring both gives t^-2 G and -G, as in the archive's Regina line.
  -
    - id: a3.slope
    - claim: Which surgery the C-exact half-cap realizes ('+1/2' label).
    - verdict: CONFIRMED
    - method: Calibrated with integer caps on the trefoil quotient (explicit diagrams). Uses standard facts: Sigma_2(positive T(3,5)) = Sigma(2,3,5) as a singularity link (bounds -E8; Casson lambda=-1); Sigma(2,3,5)=S^3_{-1}(LHT); S^3_{-1}(RHT)=Sigma(2,3,7); Casson formula lambda(S^3_{1/n}(K)) = n*a2(K); linearity of the Montesinos slope map.
    - evidence: N(T+<1>) has V=t^4+t^6-t^10, which is V(T(3,5)) for the positive torus knot (checked against the closure of (s1 s2)^5). N(T+<-1>) has V=t^5+t^7-t^11+t^12-t^13 (det 1). N(T+<3>) has V=t^3+t^5-t^8, which is T(3,4). This forces: a closing tangle of fraction s gives Sigma_2 = S^3_{-s}(kappa), and the archived trefoil quotient is a quotient of the LEFT-handed trefoil exterior. The C-exact cap (fraction -1/2) therefore realizes S^3_{+1/2}(kappa), so the '+1/2' label is correct as a surgery slope. This matches the archive's Q_s indexing by surgery slope (Q_{1/2}=rotate(Q_{-2})=<-1/2>), and it is the opposite sign from the <n> tangle-fraction indexing. The F-divisibility proof does not depend on this, because both half-caps give det(B)=1 and C up to a unit. Caveat: the calibration rests on the standard orientation facts listed under method.
  -
    - id: a4
    - claim: Classical facts in the F-divisibility proof: V(1)=1, V'(1)=0, V(e^{2pi i/3})=1; det=1 => V(-1)=1 (mod-4 argument) and Arf=0 so V(+-i)=1; at e^{pi i/3} trivial H_1(Sigma_2;Z/3) gives +-1 and the sign is forced to +1 via Phi_6 | (V-eps) at t=-1.
    - verdict: CONFIRMED
    - method: Checked each logical step by hand and with exact arithmetic. Read the primary sources: Lickorish-Millett scanned PDF (pages rendered and read, pp.349-350) and Stoimenow MRL text (pdftotext, p.759).
    - evidence: Step 1: Lickorish-Millett, Comment. Math. Helv. 61 (1986) 349-359, p.349, lists V_L(1)=(-2)^{c(L)-1}, P_L(l,-(l+l^-1)) = 1 = V_L(e^{-2pi i/3}), and V_L(-1)=Delta_L(-1)=Det(L). Stoimenow, MRL 11 (2004) 755-769, Prop 3.2 p.759 (attributed to Jones, Ann. of Math 126 (1987) Sec 12): 'V = 1 mod (t-1)(t^3-1)', which gives V(1)=1, V'(1)=0 and V(omega)=1. Step 2: V(-1)=1-2*S_odd and V'(1)=0 gives S_odd even, so V(-1)=1 mod 4; with |V(-1)|=det=1 this forces V(-1)=+1. Logic correct. Step 3: det 1 gives Delta(-1)=+-1, which is +-1 mod 8, so Arf=0 (Levine/Murasugi). Equivalently, scalar.txt's argument (Delta(-1)=1-4a2 mod 8, so a2 is even) is correct. LM Theorem 1 (H. Murakami): V_L(i)=(-sqrt2)^{c-1}(-1)^{Arf}, so V(i)=1, and V(-i)=conj V(i)=1. Stoimenow Prop 3.2 also gives V(i)=(-1)^{V''(1)/6}. Step 4: LM Theorem 3: V_L(e^{i pi/3}) = +-i^{c-1}(i sqrt3)^{dim H_1(D_L;Z_3)}, which is +-1 here. Phi_6=t^2-t+1 is monic and is the minimal polynomial of e^{i pi/3}, so Phi_6 | V-eps in Z[t^+-1]. Since Phi_6(-1)=3, 1-eps=0 mod 3, so eps=+1. Stoimenow Prop 3.2's form 'V = +-3^k(2t-1)^d mod t^2-t+1, k=d=0 if 3 does not divide V(-1)' agrees. The factors (t-1)^2, Phi_3, Phi_4, Phi_2, Phi_6 are pairwise coprime and monic, so G | P over Z. Lickorish's book (GTM 175, 1997): Chapter 3 is 'The Jones Polynomial' and Chapter 10 is 'The Arf Invariant and the Jones Polynomial'. V_L(i) is reportedly Theorem 10.6 per a secondary citation in arXiv:2303.04233; the theorem numbers in the book itself are UNCHECKED.
  -
    - id: c1
    - claim: Archived trefoil quotient R(<-1>+<1/2>+<1/3>)+<-6> has w=A^2 F (x=-A^2 F); fix the bracket of <1> by testing both mirror conventions.
    - verdict: CONFIRMED_WITH_CONVENTION_FIX
    - method: Computed in both conventions with my module code. Rebuilt the 12-crossing diagram explicitly and recomputed its bracket by state sum.
    - evidence: The working convention is <1> = A^-1*Q0 + A*Qinf: the A-smoothing is Qinf and the over-strand runs NE-SW. Here <n> is n horizontal <+-1> crossings, <1/n> is n vertically stacked <sign n> crossings, and rotation swaps Q0 and Qinf. This gives f_inf(T)=A^-18, f_0(T)/f_inf(T)=-A^2+A^6-A^22-A^30 and w=A^2 F exactly, all matching wh_gate.txt and the archive certificate (whose integer_tangle uses the same crossing). The other convention, <1>=A*Q0+A^-1*Qinf, gives f_inf=A^18 and w=-A^-26 F=A^-2 F(A^-1), the mirror. On the explicit diagram, D(T) is a knot with Jones polynomial 1, writhe -6 and bracket A^-18. N(T) has 2 components and its bracket vanishes at zeta (det 0). The diagram bracket equals the module bracket. Probe defects: x(<1>)=-A^-2 and x(<-1>)=-A^2.
  -
    - id: c1.Wh
    - claim: Mhat_Wh = [[1, delta(1-d)],[0,d]] with d a unit times F (only if wh_gate.txt gives the shell explicitly).
    - verdict: UNCHECKED
    - method: wh_gate.txt and quotient17/whitehead_pattern_audit.txt give no explicit shell (the latter says 'No explicit polynomial d was computed'). I checked the algebra that is present.
    - evidence: Algebra CONFIRMED. The two stated properties, Mhat(Q0)=Q0 and f_inf*Mhat=f_inf, force the matrix [[1, delta(1-d)],[0,d]] (column action on (Q0,Qinf) coordinates). Then Mhat v=d v, det Mhat=d, and w_out=d*w_in. For raw M=u*Mhat: det M=u^2 d, the raw eigenvalue on v is u*d=det(M)/u, and the normalized multiplier is d=det(M)/u^2 (100 random checks). Exact divisions give x_trefoil/x(<-1>)=F and x_trefoil/x(<1>)=A^4 F, both a unit times F. F(A^-1)=-A^-24 F(A), and x_mirror=A^-26 F is also a unit times F. That the shell sends a Q+-1 probe to exactly this marked trefoil quotient is geometric input I did not check.
  -
    - id: d1
    - claim: Horizontal algebra e^2=delta e, v=delta-e: v^2=delta v; w_(1#2)=w1+w2+delta w1 w2; H=1+delta w is multiplicative.
    - verdict: CONFIRMED
    - method: Exact algebra plus 200 random instances. Explicit-diagram check that diagram horizontal and vertical sums equal the module products (40 random pairs). Trefoil sums recomputed independently.
    - evidence: v*v = delta*v exactly. f_inf is multiplicative, (1+w1 v)(1+w2 v) = 1+(w1+w2+delta w1 w2)v, and H_(1#2)=H1*H2. All held on 200 random cases. So m=1+delta*w_kappa and c0=-delta in Claude's m=1-c0*w. Archive x-sign: x_(1#2)=x1+x2-delta x1 x2 and H=1-delta x. Reproduced sums.txt exactly: x(3_1#3_1) = -A^2+A^6-A^10+A^14-A^18+A^22-2A^30+3A^34-3A^38+A^42+A^46-A^50+A^54, and x(3_1#mirror) = -A^-14+2A^-10-2A^-6+A^-2+A^2-2A^6+2A^10-A^14, with x_mirror=A^-26 F. For the T+T diagram (24 crossings), D-closure is 1 component, N-closure is 2 components, f_inf=A^-36, and w(T+T) equals the formula. The geometric identification of directed equivariant sums with horizontal composition was not checked.
  -
    - id: d2
    - claim: H1*H2=1 in R forces each H_i=eps*A^k; with w(zeta)=0=delta(zeta) at zeta=exp(pi i/4), H(zeta)=1 and H'(zeta)=0 force k=0, eps=1; w(zeta)=0 holds for every actual preferred quotient (via F|w).
    - verdict: CONFIRMED
    - method: Exact and numerical evaluation at zeta. Unit scan eps*A^k for |k|<=5. 100 random w divisible by A^4+1. Trefoil instance.
    - evidence: Units of Z[A^+-1] are exactly +-A^k. delta(zeta)=0 and delta(zeta)^2-1=-1. Since H'=delta'*w+delta*w', w(zeta)=0 gives H(zeta)=1 and H'(zeta)=0. Among eps*A^k, only (eps,k)=(1,0) satisfies both. Then H=1, so delta*w=0, so w=0 (R is a domain). For the trefoil: w(zeta)=0, H(zeta)=1, H'(zeta)=0. w(zeta)=0 for every actual preferred quotient follows either from F|w or directly from det(N(T))=0: |f_0(T_hat)(zeta)|=det=0, so w(zeta)=0/(-1)=0. Only Phi_8(A)=A^4+1 is needed, as the message says.
  -
    - id: d2.reason
    - claim: Parenthetical in the task: 'since 1+A^8 vanishes at zeta'.
    - verdict: REFUTED
    - method: Direct evaluation and exact divisibility.
    - evidence: At zeta=exp(i pi/4), zeta^8=1, so 1+A^8 evaluates to 2 (also 1-A^4 evaluates to 2). The vanishing factor of F is 1+A^12 (zeta^12=-1), and 1+A^12=(1+A^4)(1-A^4+A^8). So Phi_8(A)=A^4+1 divides 1+A^12 but not 1+A^8; 1+A^8 is Phi_16(A). The conclusion w(zeta)=0 still holds. The codex message and sums.txt state it correctly (Phi8=A^4+1).
  -
    - id: d3
    - claim: Figure-eight: the self-sum has defect z(2-delta z) and the second factor equals 2 at zeta.
    - verdict: CONFIRMED
    - method: Exact algebra plus 100 random z, evaluated at zeta.
    - evidence: In the archive x-sign, x_(K#K)=2z-delta z^2=z(2-delta z). In the w-sign it is z(2+delta z). In both, the second factor is exactly 2 at zeta because delta(zeta)=0, so it is a nonzero Laurent polynomial. Since R is a domain, the product is nonzero whenever z is nonzero.
  -
    - id: d3.nonzero
    - claim: z != 0 for the chosen 4_1 inversion because a2(4_1)=-1.
    - verdict: UNCHECKED
    - method: Not re-derived. The archived longitude/Casson lemma (flat => a2=0) was not audited.
    - evidence: a2(4_1)=-1 is correct (Conway 1-z^2). A plausible proof of 'w=0 => a2(kappa)=0': w=0 gives V(B_n)=1 for all 1/n-cap knots. Casson's formula gives lambda(S^3_{1/n})=n*a2. Mullins' formula gives lambda=sigma(B_n)/8 when V=1. B_{n+1} and B_{n-1} differ by one crossing change, so |delta sigma|<=2, which forces a2=0. Mullins' constants were not verified against the source.

### summary

The exact algebra in sections (c), (a) and (d) of 20261102-230141-codex.md checks out. I rebuilt everything independently: a Laurent/TL2 module implementation, plus a separate explicit-diagram engine (planar crossings, full state sum, writhe from orientation) calibrated on kinks and on positive-braid closures RHT, T(3,4) and T(3,5).

- **c1: crossing convention.** The archive's convention is <1> = A^-1 Q0 + A Qinf. In it the trefoil quotient has f_inf=A^-18, f_0/f_inf=-A^2+A^6-A^22-A^30 and w=A^2 F. The other convention gives the mirror, -A^-26 F.
- **a3: cap identity.** It holds exactly, with no extra unit, for the half-cap with bracket (1-A^4)Q0+A^-2Qinf, closed as N(T+cap). That cap is two vertically stacked <-1> crossings: tangle fraction -1/2, and calibrated surgery +1/2, so the '+1/2' label is right as a surgery slope. The unit factors are 1/f_inf(T) and (-A^3)^-2. The writhe difference of +2 was verified on the trefoil diagram and on 60 random tangles. The other half-cap gives -A^8 C(A) x.
- **a1, a2.** a1 confirmed. a2 holds with G(A^-4) = -A^-26 C F. The zeros of F in t are {1, ±i, -1, e^{±iπ/3}}, all simple.
- **a4.** Each step's logic is correct, checked against Lickorish-Millett pp.349-350 (Theorems 1 and 3) and Stoimenow MRL 2004, Prop 3.2 on p.759.
- **d1-d3.** d1 confirmed; the sums.txt trefoil numbers reproduce exactly. d2 and d3 confirmed.
- **Correction.** zeta=e^{iπ/4} is a root of F through 1+A^12 (which contains A^4+1), not through 1+A^8, which equals 2 at zeta.

Not checked:
- the geometry of the explicit Whitehead shell (no shell is given in the files);
- the nonvanishing of z for 4_1, which rests on an archived Casson lemma;
- theorem numbers in Lickorish's book.

Side finding: under standard orientation conventions the archived trefoil quotient is a quotient of the left-handed trefoil.

### conventions_used

R=Z[A,A^-1], delta=-A^2-A^-2, normalization <O>=1. Q0='=' (arcs NW-NE, SW-SE), Qinf=')(' (arcs NW-SW, NE-SE). Horizontal sum: Q0 is the identity and Qinf^2=delta*Qinf. Vertical sum: Qinf is the identity and Q0^2=delta*Q0. Rotation swaps the coordinates (Q0 <-> Qinf). f_inf=(1,delta) is the D-closure (meridian); f_0=(delta,1) is the N-closure (longitude). v=delta*Q0-Qinf, T_hat=[T]/f_inf(T)=Q0+w*v, x=-w. Crossing convention (archive, fixed by the trefoil test): <1>=A^-1*Q0+A*Qinf, i.e. over-strand NE-SW, A-smoothing gives Qinf. <-1> is its mirror; <n> is n horizontal <sign n> crossings; <1/n> is n vertically stacked <sign n> crossings. Jones: V(A^-4) = (-A^3)^{-writhe} <D>, with t=A^-4 and the standard crossing sign (positive braid closures give RHT t+t^3-t^4, T(3,4), T(3,5)). Kauffman A-smoothing on a crossing with ccw edges (S,E,N,W), under-strand S-N: A pairs (S,E),(N,W). Slope calibration: closing tangle fraction s gives Sigma_2 = S^3_{-s}(kappa) in this convention, so the archive's Q_s indexes surgery slope (Q_s = <-s>).

### discrepancies_with_codex_artifacts

1. Cap naming. transmission18/whitehead_factor_and_clasp_audit.txt and whitehead_factor_check.py call the C-exact cap 'rotate(Q_-2)' / 'Q_(1/2)', with coefficients (1-A^4, A^-2). exact_factor_certificate.py builds it as integer_tangle(2)[::-1], i.e. rot(<+2>) = <-1/2> in the <n> convention, which is also the convention of the trefoil formula. In that convention rot(<-2>) = (1-A^-4, A^2), the opposite cap. Both are consistent only if Q_s is indexed by surgery slope and <n> by tangle fraction (s = -fraction). The labels are not wrong mathematically, but the two notations have opposite signs. This matters for any audit of (e), where C_q mixes I_n and Q_(1/2).
2. The archive's Regina results 'V-1 = t^-2 F_0 and -F_0' are the mirrors of the standard-convention values t^-7 G and -t^-9 G. This is consistent with the archive's own note that Regina uses the mirror Jones variable.
3. The task text's '1+A^8 vanishes at zeta' is false; the vanishing factor is 1+A^12, which contains A^4+1. The codex message and sums.txt correctly cite Phi8=A^4+1.
4. The archive says the trefoil quotient is a trefoil exterior 'up to chirality'. Calibration indicates the left-handed trefoil under standard conventions. This is no conflict.
5. wh_gate.txt does not give the Whitehead shell explicitly, so only its algebraic consequences were checkable.
No numerical disagreement was found with scalar.txt, wh_gate.txt, sums.txt, sums_check.py's expected values, or the certificate's stored constants.

### scripts_written

  - <scratch>/7610ac96-4d03-4d32-b526-8a5647837809/scratchpad/wf-c2audit/claude-audit/lp.py
  - <scratch>/7610ac96-4d03-4d32-b526-8a5647837809/scratchpad/wf-c2audit/claude-audit/tl2.py
  - <scratch>/7610ac96-4d03-4d32-b526-8a5647837809/scratchpad/wf-c2audit/claude-audit/diag.py
  - <scratch>/7610ac96-4d03-4d32-b526-8a5647837809/scratchpad/wf-c2audit/claude-audit/t0_anchors.py
  - <scratch>/7610ac96-4d03-4d32-b526-8a5647837809/scratchpad/wf-c2audit/claude-audit/t1_trefoil_quotient.py
  - <scratch>/7610ac96-4d03-4d32-b526-8a5647837809/scratchpad/wf-c2audit/claude-audit/t2_cap.py
  - <scratch>/7610ac96-4d03-4d32-b526-8a5647837809/scratchpad/wf-c2audit/claude-audit/t3_diagrams.py
  - <scratch>/7610ac96-4d03-4d32-b526-8a5647837809/scratchpad/wf-c2audit/claude-audit/t4_slope_calibration.py
  - <scratch>/7610ac96-4d03-4d32-b526-8a5647837809/scratchpad/wf-c2audit/claude-audit/t5_algebra.py
  - <scratch>/7610ac96-4d03-4d32-b526-8a5647837809/scratchpad/wf-c2audit/claude-audit/t6_braid_anchor.py
  - <scratch>/7610ac96-4d03-4d32-b526-8a5647837809/scratchpad/wf-c2audit/claude-audit/t7_G_divides.py


## Agent: lit:special-classes


### items

  -
    - source_id: S014
    - citation: G. Pagel, On the modular Jones polynomial, C. R. Math. Acad. Sci. Paris 358 (2020), no. 8, 901-908, DOI 10.5802/crmath.106; arXiv:2008.00716 v1 (2020-08-03), the only arXiv version.
    - exact_statement: Definition (verbatim): 'We say that a nontrivial knot K is n-trivial if its Jones polynomial V(K) satisfy V(K)≡1[n].' Theorem 1.1 (verbatim): 'If there exists an n-trivial knot for some n≥2, then for all k≥1 there exists an n^k-trivial knot.' The proof is a construction: if V(K)=1+nP, then #(K,n^{k-1}) is n^k-trivial. Corollary (verbatim): 'For all integers k≥2 there exist 3^k-trivial and 2^k-trivial non-prime knots.' The seed is γ=12n659 with V=1-3t+6t^2-9t^3+12t^4-12t^5+12t^6-9t^7+6t^8-3t^9. Further results: for p prime, if a p-trivial knot exists then a p-trivial prime knot exists; and a connected sum of m_i-trivial knots is trivial only modulo gcd(m_i^{k_i}), so no new composite modulus arises this way. The introduction says 'Essentially nothing else is known, except that there are no 5-trivial knots up to 16 crossings', and also states that the knots of Eliahou-Fromentin are prime (EF's own text does not claim this). Open questions (Further work): a 6-trivial knot; other moduli; the minimal crossing number of n-trivial knots, and whether minimal ones are prime when n is composite.
    - status: Published 2020. OpenAlex cited_by_count is 0 (checked 2026-11-02). Reproduced here: V(γ)≡1 mod 3; V(γ)^3≡1 mod 9 but not mod 27 (V(γ)^3 runs -27t^27+162t^26-567t^25 ... +45t^2-9t+1). Still open: n-trivial knots for any n that is not a power of 2 or 3.
    - read_primary: True
    - relevance_to_scaffold: As stated, Pagel's barrier lies outside the slice: the 3^k-trivial knots with k≥2 are composite, so u≥2 by Scharlemann (u=1 knots are prime; not re-read here), and the seed 12n659 itself has u=2 (KnotInfo). DERIVED-1 brings the modular barrier inside the slice for n=2^r. Any proof of Lemma Q therefore has to use integral data, such as V'(-1)=0, which gives a2(κ)=0.
    - category: barrier
    - url: https://arxiv.org/abs/2008.00716
    - latest_version: arXiv v1 (2020-08-03); C. R. Math. 358(8) (2020) 901-908
  -
    - source_id: S014-ref-EF2017
    - citation: S. Eliahou, J. Fromentin, A remarkable 20-crossing tangle, J. Knot Theory Ramifications 26(14) (2017) 1750091, DOI 10.1142/S0218216517500912; arXiv:1610.05560 v2 (2017-01-18).
    - exact_statement: Theorem (verbatim): 'For all r≥1, there exist infinitely many pairwise distinct knots with trivial Jones polynomial modulo 2^r.' Construction: T_{8,21}=(((1/2)+1)*2)+(-3), T_10=T_{8,21}*2, T_20=T_10+(-T_10), M_1=T_20, M_r=M_{r-1}+M_{r-1}, and K_r=den(1*M_r). Proposition: K_r has at most 1+2^{r-1}·20 crossings. Proposition: br_{2^r}(M_r)=[1;0]. The leading term of χ(K_r) is (2t^28)^{2^{r-1}}. Census of knots with V≡1 mod m, for ≤11/12/13/14/15/16 crossings: m=2: 0/4/9/35/140/582; m=3: 0/1/0/1/2/26; m=4: one knot at 15 crossings; m=5: none. Closing questions (verbatim): 'given an integer m ≥ 3, does there exist a tangle, analogous to T_20, whose Kauffman bracket polynomial pair would be trivial mod m?' and 'does there exist a tangle whose Kauffman bracket polynomial pair is trivial over Z? The existence of such a tangle would probably imply the existence of a nontrivial knot with trivial Jones polynomial.'
    - status: Published 2017. Reproduced exactly here with two independent implementations (the bracket-pair calculus and explicit PD Kauffman state sums): br(2), br(3), br(1/2), br(T_{8,21}), br(T_10), br_2(T_20)=[1;0], br(M_r)≡[1;0] mod 2^r for r=1..4, and the leading terms. SnapPy identifies num(T_{8,21}) as 8_21 and simplifies den(T_10) and den(M_1) to 0 crossings. Both closing questions appear open. OpenAlex lists 4 citing records (Pagel, ABF 2023, arXiv:2002.06672); none resolves them.
    - read_primary: True
    - relevance_to_scaffold: EF's question about a tangle whose bracket pair is trivial over Z asks for an integral version of the object that Lemma Q rules out when one closure is the unknot; EF's mod-2^r tangle M_r is the engine of DERIVED-1. M_r is algebraic (arborescent), so every construction of EF type has a graph-manifold double branched cover and lands in the graph-κ case, never in the hyperbolic crux.
    - category: barrier
    - url: https://arxiv.org/abs/1610.05560
    - latest_version: arXiv v2 (2017-01-18); JKTR 26(14) (2017) 1750091
  -
    - source_id: DERIVED-1
    - citation: Derived in this audit from EF2017's M_r; not a literature source. Files: <scratch>/7610ac96-4d03-4d32-b526-8a5647837809/scratchpad/wf-c2audit/modular-detection-audit/scripts/verify_all.py with output in verify_all_output.txt; scripts/kpp_general_r.py for r≤5; scripts/casson_readout.py; PD codes in pd_codes.json under keys Kpp_1, Kpp_1_switched, Kpp_2, Kpp_2_switched.
    - exact_statement: Let K''_r=den((1*1)*M_r), i.e. EF's knot with its single crossing 1 replaced by the clasp 1*1=1/2. (i) In EF pair coordinates, <den((1*1)*M)> = t^6 f_M - (t^4+t^-4) g_M. Hence χ(K''_r) = f(M_r) - (t^-2+t^-10) g(M_r) ≡ 1 mod 2^r. (ii) Switching one clasp crossing gives (1*(-1))*M_r = ∞*M_r, and its den closure is den(M_r), a connected sum of copies of den(T_10)#den(-T_10). That is the unknot, because SnapPy simplifies den(T_10) to 0 crossings; so u(K''_r)≤1 for every r. (iii) V(K''_r)≠1. For r=1 the diagram has 22 crossings, writhe 2, and V = 2t^-7-8t^-6+18t^-5-32t^-4+44t^-3-48t^-2+42t^-1-23+24t^2-42t^3+48t^4-44t^5+32t^6-18t^7+8t^8-2t^9, which is ≡1 mod 2 but not mod 4. For r=2 the diagram has 42 crossings and V is ≡1 mod 4 but not mod 8. For r=1..5, V ≡1 mod 2^r, V is not ≡1 mod 2^{r+1}, and the extreme coefficient is 2^{2^{r-1}}. Hence K''_r is nontrivial, u(K''_r)=1, and K''_r is prime (Scharlemann). (iv) Let X_r=1*M_r be the complementary tangle. Then br(X_r) ≡ -t^3·[1;0] mod 2^r, X_r∪(-1) is the unknot, and X_r is not rational: otherwise K''_r would be 2-bridge, hence alternating, and no nontrivial alternating knot is n-trivial (Thistlethwaite's extreme coefficients). (v) det=1, V'(1)=0, a2(K''_r)=0, V(i)=1, V(-1)=1, and V'(-1) = -1536·2^{r-1} for r=1..5, which gives |a2(κ_r)| = 64·2^{r-1} by DERIVED-2.
    - status: DERIVED here; not peer reviewed; novelty UNCHECKED (no literature hit on u=1 n-trivial knots). The pair calculus and the explicit PD state sums agree exactly for r=1,2; r=3..5 use the pair calculus only. The switched diagrams have V=1 exactly, and SnapPy simplifies them to 0 crossings for r=1,2; for all r, the unknot follows from the connected-sum structure. Numerical hyperbolic volumes are K''_1≈29.2397 and K''_2≈58.468 (not rigorously verified), so K itself is apparently hyperbolic. κ_r is presumed to be a nontrivial graph knot. Reason: X_r is algebraic, so its double branched cover, which is the exterior of κ_r, is a graph manifold. That is the standard Montesinos/Bonahon-Siebenmann fact, not re-verified here. It is consistent with a2(κ_r)≠0 and with SnapPy's degenerate solutions on the (1,0)-filled double covers (H1=0).
    - read_primary: False
    - relevance_to_scaffold: This is a new modular barrier inside the u=1 slice. For every r tested, the mod-2^r shadow of Lemma Q is false: X_r is non-rational, its bracket is ≡ that of a rational tangle mod 2^r, and it has an unknot closure. So no proof of Lemma Q can rely only on V, or on <X>, mod 2^r. These witnesses are still eliminated by the scaffold's integral a2 step, since κ_r is presumed graph with a2(κ_r)≠0. The sharper open target is a mod-p witness with V'(-1)=0. Such a witness would need a non-algebraic X, so it would sit in the hyperbolic crux.
    - category: barrier
  -
    - source_id: DERIVED-2
    - citation: Derived in this audit by combining Mullins' formula (Topology 32 (1993) 419-438; recalled, not re-read) with Casson's surgery formula. Calibration script: <scratch>/7610ac96-4d03-4d32-b526-8a5647837809/scratchpad/wf-c2audit/modular-detection-audit/scripts/casson_readout.py
    - exact_statement: Let K be a knot with u(K)=1 and det(K)=1. Then σ(K)=0, because det≡1 mod 4 forces σ≡0 mod 4 and |σ|≤2u. Also V(-1)=Δ(-1)=1, and Σ2(K)=S^3_{±1/2}(κ). Combine three formulas: Mullins, λ_W(Σ2(L)) = -(1/6)·V'_L(-1)/V_L(-1) + σ(L)/4; Casson, λ_C(S^3_{1/n}(κ)) = n·a2(κ); and λ_W = 2λ_C. The result is a2(κ) = ±V'_K(-1)/24. The normalization was checked here against Walker's lens-space values |λ_W(L(p,q))| = |s(q,p)|: the formula gives 1/18 for 3_1, 1/5 for 5_1 and 0 for 4_1, all matching.
    - status: DERIVED here. The sign convention is not fixed (only |a2| is used). For V=1 it reproduces the scaffold's a2(κ)=0. For K''_r it gives |a2(κ_r)| = 64, 128, 256, 512, 1024 for r=1..5.
    - read_primary: False
    - relevance_to_scaffold: This is a computational tool. It reads a2(κ) off V'_K(-1) without constructing κ, so it screens any candidate X in one line: for det 1, a2(κ)=0 if and only if V'(-1)=0. It also locates the scaffold's graph-knot exclusion on the exact integer V'(-1), which no mod-p argument can detect.
    - category: tool
  -
    - source_id: S014-ref-ABF2023
    - citation: N. Aiello, S. Baader, L. Ferretti, On the Jones polynomial modulo primes, Glasgow Math. J. 65(3) (2023) 730-734, DOI 10.1017/S0017089523000253; arXiv:2204.12259 v1 (2022-04-26).
    - exact_statement: Theorem 1 (verbatim): 'For all a,b ∈ Z with b-a ≥ 7, the set of Laurent polynomials with coefficients in F_p=Z/pZ within the degree range from a to b, that are realised as Jones polynomials of knots, has density at most 4/p^7.' Theorem 2: let h(t)=(t^3-1)(t-1)(t^2+1) and f(t)=(t^2-t+1)h(t). For every knot K there is a unique p(t) in Z[t] of degree at most 7, from one of four families (the first is 1+n·h(t)), such that f divides V_K - p. Remark: V_{12n237} ≡ t^12 mod 2, so 12n237 # mirror is 2-trivial. Question (verbatim): 'Let p be an odd prime. Is there a knot K ⊂ S^3 with V̄_K(t)=t^{12p} (mod p)?'
    - status: Published 2023. OpenAlex cited_by_count is 0. The KnotInfo data confirm 12n_237 ≡ t^12 mod 2 and 12n_510 ≡ t^-12 mod 2; both have u=2 and Turaev genus 1. The odd-p question appears open.
    - read_primary: True
    - relevance_to_scaffold: A yes answer for odd p would give p-trivial knots K#mirror(K) for every prime p. Those are composite, so u≥2, and the barrier would reach the u=1 slice only through a separate u=1 construction like DERIVED-1. The divisor f(t) in Theorem 2 encodes the root-of-unity constraints that any candidate V must satisfy: useful as a sanity filter, but it gives no mechanism for hyperbolic κ.
    - category: context
    - url: https://arxiv.org/abs/2204.12259
    - latest_version: arXiv v1 (2022-04-26); Glasgow Math. J. 65(3) (2023)
  -
    - source_id: KNOTINFO-SCAN
    - citation: Scan run in this audit on the KnotInfo database (C. Livingston, A. H. Moore, knotinfo.org), read as data only from the database_knotinfo 2026.11.2 wheel (csv_data/knotinfo_data_complete.csv). Crossing-change test: <scratch>/7610ac96-4d03-4d32-b526-8a5647837809/scratchpad/wf-c2audit/modular-detection-audit/scripts/identify_changes.py
    - exact_statement: Among prime knots with at most 12 crossings, the knots with V≡1 mod 2 are exactly: 12n_557 (u in [2,3], Turaev genus 1), 12n_643 (u=2, Turaev genus 1), 12n_706 (u=2, Turaev genus 2) and 12n_730 (u in [1,2], Turaev genus in [1,2]). V≡1 mod 3 holds only for 12n_659 (u=2, Turaev genus 1, hyperbolic). No knot is n-trivial for n=4..9. No nontrivial knot has V=1. For each of the 12 single crossing changes in KnotInfo's minimal diagram of 12n_730, SnapPy identifies the result as a nontrivial knot (numerical): 10_140, 8_16, 8_7, 11n132, 7_6, 11n95, 7_3, 10_151, 10_151, 10_130, 7_3, 7_6. The analogous changes in 12n_643 and 12n_659 also leave knotted diagrams.
    - status: Computed 2026-11-02. The 12-crossing counts (4 knots for m=2, 1 for m=3) agree with EF's table. u(12n_730) is still open: only one diagram was tested.
    - read_primary: True
    - relevance_to_scaffold: No knot with at most 12 crossings is a u=1 n-trivial knot unless u(12n_730)=1. In that case 12n_730 would be a 12-crossing mod-2 witness, far smaller than DERIVED-1's 22 crossings, which makes u(12n_730) the cheapest open audit target. The Turaev-genus-one n-trivial knots (12n_557, 12n_643, 12n_659) show that the Lowrance-Spyropoulos mechanism is integral.
    - category: audit_target
  -
    - source_id: S013
    - citation: A. M. Lowrance, D. Spyropoulos, The Jones polynomial of an almost alternating link, New York J. Math. 23 (2017) 1611-1639 (published 2017-11-06); arXiv:1707.05443 v2 (2017-12-14).
    - exact_statement: Theorem 1.1 (verbatim): 'Let L be an ℓ-component almost alternating link or a link of Turaev genus one where ℓ≥1, and let V_L(t) be the Jones polynomial of L. Then V_L(t)≠t^k(-t^{1/2}-t^{-1/2})^{ℓ-1} for any k∈Z. In particular, the Jones polynomial of L is different from the Jones polynomial of the ℓ-component unlink.' Theorem 1.2: if L is a non-split almost alternating link or a link of Turaev genus one with V_L = a_0 t^k + ... + a_n t^{k+n}, then either |a_0|=1 and a_0a_1≤0, or |a_n|=1 and a_{n-1}a_n≤0. The Turaev genus one case reduces to the almost alternating case via Armond-Lowrance (every Turaev genus one link is a mutant of an almost alternating link) and mutation invariance of V. Stated consequence: the EKT links with unlink Jones polynomial are not almost alternating and have Turaev genus at least 2.
    - status: Published. NYJM abstract confirmed: 'Using these formulas, we show that the Jones polynomial of an almost alternating link is nontrivial.' My inference: V detects the unknot among all knots of Turaev genus at most 1 (alternating knots by Kauffman-Murasugi-Thistlethwaite, plus Theorem 1.1). Whether all Montesinos knots fall in this class was recalled but UNCHECKED.
    - read_primary: True
    - relevance_to_scaffold: Usable as a filter: a u=1 counterexample K must have Turaev genus at least 2 and cannot be almost alternating. The extreme-coefficient mechanism is integral (it fails mod 2 on 12n_557 and 12n_643, and mod 3 on 12n_659) and constrains K's diagram rather than κ, so it gives no mechanism for the hyperbolic case.
    - category: tool
    - url: https://arxiv.org/abs/1707.05443
    - latest_version: arXiv v2 (2017-12-14); NYJM 23 (2017) 1611-1639
  -
    - source_id: S053
    - citation: O. T. Dasbach, A. M. Lowrance, Invariants for Turaev genus one links, Comm. Anal. Geom. 26(5) (2018) 1103-1126, DOI 10.4310/CAG.2018.v26.n5.a4; arXiv:1604.03501 v2 (2016-09-30).
    - exact_statement: arXiv v2 Theorem 1.3 (verbatim): 'Let L be an almost alternating link or a link of Turaev genus one with Jones polynomial V_L(t) = a_m t^m + a_{m+1} t^{m+1} + ... + a_{M-1} t^{M-1} + a_M t^M, where a_m and a_M are nonzero. Either |a_m| = 1 or |a_M|=1 (or both).' Theorem 1.1: if K has a diagram D whose Turaev surface has genus one, then σ(K) = s_A(D) - c_+(D) ± 1 and σ(K) ≡ det(K) - 1 mod 4. Proposition: a prime knot of Turaev genus one is either hyperbolic or a torus pretzel knot (T_{3,4}, T_{3,5} and their mirrors). The arXiv comment notes that Theorem 1.3 of v1 became Equation 3.2 in v2, so theorem numbers differ between versions.
    - status: Published 2018. For unknot detection it is superseded by S013: V=1 satisfies the |a|=1 condition, so Theorem 1.3 alone detects nothing.
    - read_primary: True
    - relevance_to_scaffold: Context only. This is the obstruction that S013 sharpened into detection. The hyperbolic-or-torus proposition concerns K and says nothing about κ in Σ2(K)=S^3_{±1/2}(κ).
    - category: context
    - url: https://arxiv.org/abs/1604.03501
    - latest_version: arXiv v2 (2016-09-30); CAG 26(5) (2018)
  -
    - source_id: S011
    - citation: R. E. Tuzun, A. S. Sikora, Verification of the Jones unknot conjecture up to 24 crossings, J. Knot Theory Ramifications 30(3) (2021) 2150020, DOI 10.1142/S0218216521500206; arXiv:2003.06724 v2 (2021-03-23). Predecessors: TS22, JKTR 27(3) (2018) 1840009, arXiv:1606.06671 v7 (2020-04-04); a 2-page 23-crossing note, arXiv:1809.02285 v1.
    - exact_statement: Main theorem (verbatim): 'The Jones polynomial distinguishes all non-trivial knots with diagrams up to 24 crossings from the unknot.' Scale: 59,361,435,729,041 non-algebraic plus 185,317,928,640 algebraic knot diagrams, 59,546,753,657,681 in total; 41.8 core-years. Method: Conway polyhedra filled with algebraic tangles, pruned by requiring subtangles to be algebraically trivializable (their bracket coefficients generate the unit ideal of Z[A^{±1}]; TS22 shows that every subtangle of a diagram of a V=1 knot has this property). Unknot checks use SnapPy and Dynnikov's algorithm. TS22 covered 22 crossings with 2,274,000,383,051 diagrams.
    - status: Published 2021. As of 2026-11-02 no extension beyond 24 crossings was found. Sources checked: the 3 OpenAlex citers of TS24 (Big data approaches to knot theory, JKTR 2022; Sikora's Tangle equations, the Jones conjecture..., CJM; a 2023 book chapter), the 14 citers of TS22 (through a 2025 AIF paper), and two web searches. The search was not exhaustive, so 'no extension exists' is UNCHECKED.
    - read_primary: True
    - relevance_to_scaffold: Useful as a tool: algebraic trivializability is an integral form of the bracket-pair condition behind Lemma Q. Combined with Gordon-Luecke and the solid-torus criterion, TS24 gives Lemma Q for every X with a diagram of at most 23 crossings (my derivation). TS's algebraic/non-algebraic split matches the scaffold: hyperbolic κ forces X to be non-algebraic, which is the class TS enumerated in bulk. EF-type mod-p tangles are algebraic and would never be pruned by a mod-p version of the filter.
    - category: tool
    - url: https://arxiv.org/abs/2003.06724
    - latest_version: arXiv v2 (2021-03-23); JKTR 30(3) (2021) 2150020
  -
    - source_id: S054
    - citation: M. Hedden, Khovanov homology of the 2-cable detects the unknot, Math. Res. Lett. 16(6) (2009) 991-994, DOI 10.4310/MRL.2009.v16.n6.a6; arXiv:0805.4418 v1 (2008-05-28), the only version.
    - exact_statement: Theorem (verbatim): 'Let K be a knot, and let K^2 denote its 2-cable. Then rk Kh(K^2)=4 if and only if K is the unknot. Here, Kh denotes the Khovanov homology (with coefficients in Z/2Z).' The cable uses the Seifert framing. Corollary (verbatim): 'Khovanov's categorification of the 2-colored Jones polynomial detects the unknot.' Proof: the Ozsváth-Szabó spectral sequence from reduced Kh of the mirror to HF^(Σ(L)); Σ(K^2) ≅ S^3_0(K#K); Floer homology detects the Thurston norm, so rk HF^(S^3_0(K#K)) ≥ 6 for nontrivial K.
    - status: Published 2009. Established; later strengthened by Kronheimer-Mrowka's theorem that Kh detects the unknot (2011; not re-read here).
    - read_primary: True
    - relevance_to_scaffold: Context for barrier B5: detection comes from Floer-homology rank on the far side of a spectral sequence, which V cannot see because V is only χ(Kh). In the slice the same mechanism gives rk Kh~(K) ≥ rk HF^(S^3_{±1/2}(κ)) > 1 for nontrivial κ (S^3_{±1/2}(κ) is an L-space only when κ is the unknot; my derivation from the L-space surgery bound), but nothing carries this over to V.
    - category: context
    - url: https://arxiv.org/abs/0805.4418
    - latest_version: arXiv v1 (2008-05-28); MRL 16(6) (2009)
  -
    - source_id: S055
    - citation: J. E. Grigsby, S. M. Wehrli, On the colored Jones polynomial, sutured Floer homology, and knot Floer homology, Adv. Math. 223(6) (2010) 2114-2165, DOI 10.1016/j.aim.2009.11.002; arXiv:0807.1432 v3 (2008-10-13).
    - exact_statement: Theorem 1.1 (verbatim core): 'Let K ⊂ S^3 be an oriented knot, K̄ ⊂ S^3 its mirror, and K^r its orientation reverse. For each n ∈ Z_{>0}, there is a spectral sequence, whose E^2 term is Kh~_n(K̄) and whose E^∞ term is HF_n(K)'. Here HF_n(K) is HF^(Σ(S^3,K)) if n=1, HFK^(Σ(S^3,K),K~) if n>1 is odd, and HFK^(S^3,K#K^r) if n is even, with grading shifts and Z_2 coefficients. Corollary 1.2 (verbatim): 'Kh~_n(K) detects the unknot for all n>1.' The proof uses that HFK^ has rank greater than 1 for knots of positive genus.
    - status: Published 2010. The case n=1 (ordinary reduced Kh) is not covered by this paper; it was settled by Kronheimer-Mrowka (2011; not re-read here).
    - read_primary: True
    - relevance_to_scaffold: Context for B5: Kh~_n detects the unknot for n>1, but its Euler characteristic is a colored Jones polynomial, not V. The n=1 E^∞ term HF^(Σ2(K)) is exactly the scaffold's S^3_{±1/2}(κ): Floer theory sees κ there and V does not.
    - category: context
    - url: https://arxiv.org/abs/0807.1432
    - latest_version: arXiv v3 (2008-10-13); Adv. Math. 223(6) (2010)
  -
    - source_id: S002
    - citation: J. Halverson, F. Ruehle, Learning Topological Invariance, arXiv:2504.12390 v1 (2025-04-16), Section 3.5.
    - exact_statement: Section 3.5 (verbatim): 'We generated 400k knots with the sampling methods outlined in Section 2.3, but did not find a counterexample.' Setup: a training set of inequivalent length-30 braid words on up to 5 strands, with Jones polynomials computed in SageMath, and an encoder-decoder Transformer trained to map a Jones polynomial to a braid word. They generated 100k knots per sampling method plus a 100k random-braid baseline. Conclusion (verbatim): 'none of them have trivial Jones Polynomial.'
    - status: arXiv v1 only; no other version on arXiv as checked 2026-11-02. A negative computational result, not independently reproduced.
    - read_primary: True
    - relevance_to_scaffold: Nothing for the scaffold. This is an unstructured negative search on short braids, weaker evidence than TS24's exhaustive enumeration, and it supplies no mechanism or barrier.
    - category: none
    - url: https://arxiv.org/abs/2504.12390
    - latest_version: arXiv v1 (2025-04-16)
  -
    - source_id: S004
    - citation: Samaritan Research, FrontierMath Open Problems, 'The Jones Unknot Conjecture', https://samaritan-research.org/frontiermath/open-problems/jones-unknot (read 2026-11-02).
    - exact_statement: The page shows the status as Unsolved. A counterexample must be a PD code in the SnapPy/Spherogram convention (each label used twice, planar, one component; trefoil example [[5,2,0,3],[3,0,4,1],[1,4,2,5]]). It may have at most 100 crossings and must be reduced: 'Link(pd).simplify(mode='basic') must return False'. Its normalized Jones polynomial must be exactly 1, and knot Floer homology must show positive Seifert genus. The verifier allows 900 seconds for any single computation and 1800 seconds in total.
    - status: Live page; status Unsolved on 2026-11-02. The page also contains a prompt addressed to solvers, which was treated as data only.
    - read_primary: True
    - relevance_to_scaffold: Tool and target format: any u=1 counterexample has to be delivered as a reduced PD code of at most 100 crossings, with exact V=1 and an HFK genus certificate. Searches on the hyperbolic crux should therefore aim at small, low-width diagrams.
    - category: tool
    - url: https://samaritan-research.org/frontiermath/open-problems/jones-unknot

### key_claims

  - DERIVED-1: K''_r = den((1*1)*M_r), built from Eliahou-Fromentin's M_r, has u=1 and V ≡ 1 mod 2^r with V ≠ 1. This was checked exactly for r=1..5 with the pair calculus and cross-checked for r=1,2 (22 and 42 crossings) by explicit PD state sums. The switched diagram is den(M_r), a connected sum of copies of den(±T_10), and SnapPy simplifies it to the unknot. Consequence: the mod-2^r shadow of Lemma Q is false. Novelty is UNCHECKED. To re-check, run an independent Jones and unknot routine on pd_codes.json (keys Kpp_1, Kpp_1_switched, Kpp_2, Kpp_2_switched).
  - For these witnesses V(-1)=1 and V'(-1) = -1536·2^{r-1}. Via Mullins plus Casson, a2(κ) = ±V'_K(-1)/24 for det-1, u=1 knots, which gives |a2(κ_r)| = 64·2^{r-1} ≠ 0. X_r=1*M_r is algebraic, so κ_r should be a graph knot (standard fact, not re-verified). The witnesses therefore fall to the scaffold's integral a2 step and do not reach the hyperbolic crux; a hyperbolic-κ witness would need a non-algebraic X.
  - Pagel's Theorem 1.1 is a connected-sum construction, so his 3^k-trivial knots for k≥2 are composite and have u≥2 (Scharlemann), and the seed 12n659 has u=2. No n-trivial knot is known for any n other than a power of 2 or 3: EF found no 5-trivial knot up to 16 crossings, and this KnotInfo scan found none for n=4..9 up to 12 crossings.
  - Lowrance-Spyropoulos Theorem 1.1 covers both almost alternating links and Turaev genus one links, with any number of components, and gives unknot detection. Dasbach-Lowrance arXiv-v2 Theorem 1.3 only gives |a_m|=1 or |a_M|=1, which V=1 satisfies. Turaev-genus-one knots that are n-trivial exist (12n_557 and 12n_643 mod 2, 12n_659 mod 3), so the extreme-coefficient mechanism cannot work mod p.
  - Tuzun-Sikora 24 states detection for 'non-trivial knots with diagrams up to 24 crossings' (59,546,753,657,681 diagrams). As of 2026-11-02 no extension beyond 24 crossings was found; the search covered OpenAlex citers and web search and was not exhaustive.
  - Hedden: rk Kh(K^2; Z/2) = 4 if and only if K is the unknot (2-cable with Seifert framing). Grigsby-Wehrli Corollary 1.2: Kh~_n detects the unknot only for n>1; the case n=1 is outside that paper.

### summary

All eight assigned sources were read in primary form: arXiv TeX or HTML, plus the live NYJM and Samaritan pages. Their key statements were re-checked verbatim on 2026-11-02.

Modular picture:
- n-trivial knots (V ≡ 1 mod n with V ≠ 1) are known only for n = 2^k (Eliahou-Fromentin 2017; Pagel and ABF assert EF's knots are prime) and n = 3^k (Pagel 2020; composite for k≥2).
- Nothing is known for 5, 6, 7 or other moduli.
- ABF's question whether t^{12p} is realised mod p for odd p is open.
- KnotInfo up to 12 crossings: 2-trivial knots are 12n_557, 12n_643, 12n_706 and 12n_730; the only 3-trivial knot is 12n_659 (u=2); none for n=4..9.

New in this audit:
- Replacing EF's single crossing with a clasp gives K''_r = den((1*1)*M_r), a u=1 knot with V ≡ 1 mod 2^r and V ≠ 1 (checked for r ≤ 5). Its non-rational complementary tangle has bracket ≡ rational mod 2^r. So Lemma Q cannot be proved from V or the bracket pair mod 2^r alone. This is a modular barrier; its novelty is UNCHECKED.
- These witnesses have κ_r a presumed graph knot with |a2(κ_r)| = 64·2^{r-1}, computed from the derived readout a2(κ) = ±V'(-1)/24 for det-1, u=1 knots. So the scaffold's integral a2 step eliminates them, and they say nothing about hyperbolic κ, which requires a non-algebraic X.
- The sharper open target is a mod-p witness with V'(-1)=0.
- The cheapest open audit target is u(12n_730): if it is 1, 12n_730 is a 12-crossing mod-2 witness.

The other sources:
- Lowrance-Spyropoulos gives detection for Turaev genus at most 1 via an integral extreme-coefficient argument; it provably fails mod 2 and mod 3 on 12-crossing knots.
- Dasbach-Lowrance alone detects nothing.
- Tuzun-Sikora stands at 24 crossings with no extension found. Their algebraic/non-algebraic split matches the scaffold's graph/hyperbolic split for κ.
- Hedden and Grigsby-Wehrli are context for B5: detection comes from Floer-side rank, which the Euler characteristic V does not see.
- S002 is a negative ML search with no mechanism.
- S004 fixes the counterexample format: a reduced PD code of at most 100 crossings, V exactly 1, and HFK genus > 0.

Scratch files are in <scratch>/7610ac96-4d03-4d32-b526-8a5647837809/scratchpad/wf-c2audit/modular-detection-audit/. Nothing was written under W or Downloads.


## Agent: skeptic:braid-route


### checks

  -
    - claim: S009 version history (arXiv:2607.05283): v1 Mon 6 Jul 2026 16:28:02 UTC (3,164 KB; 26 pp, 28 figs); v2 Mon 14 Sep 2026 15:55:28 UTC (3,746 KB; 28 pp, 32 figs); the v3 URL is not found; no withdrawal and no journal-ref; MSC 57M07, 57M10, 20F65; the PDF title omits 'of the braid group'; the v2 title page is dated 15 Sep 2026.
    - verdict: UPHELD
    - evidence: I fetched the arXiv abs pages on 2026-11-02. The submission history matches exactly. The v1 comment is '26 pages, 28 figures'. The v2 comment is '28 pages, 32 figures. Minor corrections and improved exposition'. The listing has no Journal-ref field. /abs/2607.05283v3 returns HTTP 404 'Article 2607.05283v3 not found'. The PDF title pages (v1 and v2) read 'The Burau representation is faithful for n = 4' and are dated 'July 7, 2026' (v1) and 'September 15, 2026' (v2). The alphaXiv embedded data shows maxVersionOrder 2. PDFs are under <scratch>/7610ac96-4d03-4d32-b526-8a5647837809/scratchpad/wf-c2audit/skeptic-braid-route/dl/pdf_2607v1/ and dl/pdf_2607v2/.
  -
    - claim: S009 statements: Main Theorem verbatim 'The Burau representation ρ4 of B4 is faithful.'; ρn is the UNREDUCED rep, the action on H1(D̃n,{p̃*}), free of rank n; Cor 1.1 says the Jones rep of B4 is faithful (citing Jones 1987 and Kasahara 2008 Rem 5.6). The Main Thm, Cor 1.1, Prop 1.2, Prop 6.4=6.7, Cor 6.5=6.8 and Thm 6.6=6.9 are word-identical in v1 and v2.
    - verdict: UPHELD
    - evidence: My script <scratch>/7610ac96-4d03-4d32-b526-8a5647837809/scratchpad/wf-c2audit/skeptic-braid-route/scripts/cmp_statements.py compared the pdftotext output of both versions. All listed statements are identical, and so are Thm 2.3 (Moody), Cor 2.4, Lemma 4.2, Prop 5.1 and Lemmas 6.1-6.3. Sec. 2 defines ρn as stated ('free of rank n; this action is the unreduced Burau representation'). Cor 1.1 reads 'The Jones representation of Bn is faithful for n = 4.' Prop 1.2 relies on '[Lon86, Theorem 2.2]'. I did not read Long's paper, so its theorem numbering is UNCHECKED. Ito cites the related intersection fact as [Lon, Lemma 2.1].
  -
    - claim: Reduced and unreduced Burau have the same kernel: over Q(t) the fixed vector (1,...,1) and the fixed covector (1,t,...,t^{n-1}) pair to 1+...+t^{n-1} ≠ 0, so unreduced = reduced ⊕ trivial.
    - verdict: UPHELD
    - evidence: I checked this with exact arithmetic in <scratch>/7610ac96-4d03-4d32-b526-8a5647837809/scratchpad/wf-c2audit/skeptic-braid-route/scripts/burau_split.py, using σi -> I ⊕ [[1-t,t],[1,0]] ⊕ I acting on columns. For n=3,4,5, (1,..,1)^T is fixed, the row (1,t,..,t^{n-1}) is fixed, and the pairing is 1+t+...+t^{n-1}. The conclusion does not depend on the matrix convention. Note: the paper itself never says 'same kernel'. That sentence is the finder's (standard) addition, and the finder's own check is correct.
  -
    - claim: v2 materially reworks the proof of the key parity step while calling the changes minor. It adds 'with basepoint' generalized bigons/trigons/rectangles (new Fig 5.5) and Lemmas 6.4-6.6, replaces v1's 'otherwise we could have made a different choice of γ1' with an appeal to Lemma 6.6, adds Bou-Rabee to the acknowledgments and renumbers. Soft spot (a): Prop 6.7 checks only conditions (1) and (2) of 'properly simple mod 4-disks', with (1) said to hold 'by construction'. Soft spot (b): there is no explicit parity check for Γ'.
    - verdict: UPHELD
    - evidence: I made my own sentence diff: <scratch>/7610ac96-4d03-4d32-b526-8a5647837809/scratchpad/wf-c2audit/skeptic-braid-route/notes/diff_v1_v2_mine.txt. v2 adds item '4. Generalized bigons/trigons/rectangles with basepoint'. Its proof of Prop 5.1 says only that 'the proof goes through when adding in each case with basepoint', so those cases are asserted, not worked out. Prop 6.7's proof reads 'condition (1) is immediately satisfied by the constriction [sic], and condition (2) is satisfied...'. Condition (3) (ΓI misses β*3) is never mentioned. The Γ' paragraphs are unchanged except for figure numbers: only properties 1 and 2 are verified, and nothing establishes parity or properly-simple for Γ'. Whether (a) and (b) are real gaps is UNCHECKED. Minor paraphrase error: Lemma 6.5's hypothesis is 'properly simple modulo 4-disks', not 'disjoint from β modulo 4-disks' as the finding's 'such loops' implies. Its conclusion is that the signs of Γ∩β*3 alternate modulo 4-disks.
  -
    - claim: (relevance) The load-bearing S009 step to audit is v2 Prop 6.7 (Lemmas 6.4-6.6 and the Γ' modification).
    - verdict: UNCERTAIN
    - evidence: Prop 6.7 is load-bearing, but my non-audit reading finds other unaddressed points the findings omit. (c) Thm 6.9 (=6.6 v1, identical text): the conjugation paragraph shows that Φ·Γ1 is a proper product, then concludes 'Φ = Φ'·Γ1' is a proper product. Applying Cor 6.8 to Φ·Γ1 would only give Φ·Γ1 ∉ ker ρ4, which says nothing about Φ. A natural repair exists but is not written: conjugate by Γ1, since Γ1^{-1}ΦΓ1 = (Γ1^{-1}Φ)·Γ1. (d) Thm 6.9's sentence that with Γ1 'the only possible bigon-forming polygons ... are β-to-α trigons and rectangles' was not updated for the new 'with basepoint' class. (e) Prop 6.7 never checks that Γ = γ2∘γ1 (or Γ') is 'simple modulo 4-disks', which properly-simple presupposes. It also never argues its stated claim that f(Φ)·Γ is a proper product in B5; Cor 6.8 may not need that claim. (f) In Case 2, Γ' passes through q twice, on the boundary of a disk that is not a 4-disk, so simplicity modulo 4-disks is unclear. All of these are UNCHECKED as genuine gaps.
  -
    - claim: Reception: SciAm (L. Chiou, 2026-07-24) quotes Yang-Hui He (LIMS) calling it a major advance and saying the authors had solved it. Columbia's page (added 2026-08-03) says it was proved. Three Wikipedia pages (last edited 2026-09-27, 09-26, 09-26) call it unverified, citing NYT (G. Barber, 2026-09-06). The NYT is unreadable (403). pith.science has an AI referee (glm-5.2) review of v1 dated 2026-07-07, verdict CONDITIONAL, and no v2 review.
    - verdict: UPHELD
    - evidence: SciAm: JSON-LD gives datePublished 2026-07-24, modified 2026-07-28, author Lyndie Chiou. He says the authors 'claimed that they had solved the problem... And they had' and calls it 'one of the major advances'. Nothing indicates he checked the proof. Columbia: 'Added on August 03, 2026 ... proved'. The Wikipedia API gives last revisions 2026-09-27T23:48:53Z, 2026-09-26T15:43:34Z and 2026-09-26T04:19:34Z, all with 'not (yet) verified' wording citing the NYT. The NYT returned 403 with a captcha to me as well, so its text is UNCHECKED. pith: 'An AI referee (glm-5.2) read the paper on July 7, 2026'; 'arXiv v2 is newer than reviewed v1'; 'CONDITIONAL verdict and MODERATE confidence'. Nuance 1: the replies are explicitly labelled 'Simulated authors' rebuttal'. Nuance 2: there are 4 major objections, and the omitted 4th asks whether the conjugate stays in Brun4. That one is answered by Brun4 being normal in B4, which the paper states.
  -
    - claim: The NYT title '92-Year-Old' vs SciAm's age 99 for Birman is an unresolved mismatch.
    - verdict: UNCERTAIN
    - evidence: Mostly resolvable. Columbia's announcement (2026-09-08) confirms the NYT ran a profile of Birman titled 'The 92-Year-Old Mathematician and the Teenage Apprentice' on Sept 6, 2026. Wikipedia gives her birth date as 30 May 1927, so she was 99 in July 2026 and 92 in 2019. The paper dates the project's inception to 'seven years ago', i.e. 2019. A search-engine snippet of a reprint likewise mentions her being 92 in summer 2019. The title plausibly refers to her age at the 2019 start of the project. I could not read the NYT or the reprint (fetch denied), so this is UNCHECKED at the source.
  -
    - claim: No independent verification, rebuttal, erratum, MathOverflow thread, alphaXiv comment or journal acceptance for S009 was found as of 2026-11-02.
    - verdict: UPHELD
    - evidence: alphaXiv embedded metrics show commentsCount:0. The StackExchange API on MathOverflow has no hits for '2607.05283' or 'Bharathram', and the newest 'Burau' question is from 2026-04-13. An arXiv search for 'Burau' sorted by date, through 27 Oct 2026, shows no rebuttal or verification preprint. Web searches found none either. Absence of evidence is not proof. Bou-Rabee is thanked only in v2, for comments 'on earlier drafts', so 'pre-posting' feedback from him is not established; it may concern v1.
  -
    - claim: S008 Ito: arXiv:1402.2028 has only v1 (10 Feb 2014); published Math. Z. 280 (2015) no. 1-2, 347-353, DOI 10.1007/s00209-015-1426-7, online 2015-01-09. Thm 1: for H a nontrivial non-central normal subgroup of Bn and α with unknot closure, for every N there is β in H with closure(αβ) hyperbolic, genus >= N and braid index n (the text misprints 'β ∈ K'). Cors 1 and 2 hold (Cor 2 uses Long's intersection lemma). Thm 2 (1)-(3) and Thm 3 are as stated.
    - verdict: UPHELD
    - evidence: The arXiv listing shows v1 only, Mon 10 Feb 2014 03:47:49 UTC, 13 KB. Crossref: Math. Z. vol 280, issue 1-2, pp 347-353, published online 2015-01-09, print 2015-06. zbMATH: Zbl 1323.57009; review text is unavailable. I read the full text in <scratch>/7610ac96-4d03-4d32-b526-8a5647837809/scratchpad/wf-c2audit/skeptic-braid-route/notes/ito.txt. The statements match, including 'there exists β ∈ K' and Cor 2 citing [Lon, Lemma 2.1]. The proof also uses Papadopoulos to make αβ pseudo-Anosov. Springer served a bot challenge, which I did not bypass, so the journal wording is UNCHECKED.
  -
    - claim: Ito Cor 3 is strictly one-way: Burau(B4) not faithful => Jones fails to detect the unknot. The converse is not claimed. If S009 holds, Cor 3 has a false hypothesis and yields nothing.
    - verdict: UPHELD
    - evidence: Ito p.2: 'Corollary 3. If the Burau representation of the 4-strand braid group B4 is not faithful, then the Jones polynomial fails to detect the unknot', 'as is explained in [Big]'. No converse appears. Bigelow p.2 says a positive answer 'would have no such dramatic consequences'. KLS (v2 Sec 2.3; journal) says the inverse theorem is not known, 'so the faithfulness of the Burau representation for B4 does not mean that the Jones problem is closed'. The finding's choice of H = ker TL/Jones(B4) and α = σ1σ2σ3 is its own (correct) reconstruction, not Ito's text.
  -
    - claim: S007 Bigelow, JKTR 11 (2002) 493-505: Prop 1.5 says the Jones, TL and Burau reps of B4 are all faithful or all unfaithful, via TL4 = V(4)⊕V(3,1)⊕V(2,2) plus V(2,1,1) and V(1111). The nontriviality of the commutator [(σ1σ2)^3,β] is omitted. Conj 3.2 was later proved by Ito.
    - verdict: UPHELD
    - evidence: The arXiv listing shows v1 only (12 Dec 2000). Crossref: JKTR 11(04) 493-505, June 2002, DOI 10.1142/S0218216502001779. Text (<scratch>/7610ac96-4d03-4d32-b526-8a5647837809/scratchpad/wf-c2audit/skeptic-braid-route/notes/bigelow.txt): Prop 1.5 is as stated. The proof says 'It remains to show that [(σ1σ2)^3, β] must be non-trivial... We therefore omit this part'. The V(2,1,1) kernel equality is cited from [11]. Nuance: Bigelow's Conj 3.2 is stated for any nontrivial normal subgroup, with no non-central hypothesis. Ito proves '(a version of)' it, 'in a slightly stronger form', for non-central H.
  -
    - claim: (previously UNCHECKED) Kasahara 2008 Remark 5.6 explains the Burau/Jones faithfulness equivalence for n=4, as S009 cites it.
    - verdict: UPHELD
    - evidence: I read arXiv:0803.0304v1 (3 Mar 2008). Remark 5.6 argues that π[2²,1] restricted to B4 = π[2,1²] ⊕ π[2,2] is faithful iff reduced Burau(B4) is faithful. It uses Long's result that such a direct sum is faithful iff one summand is, and π[2,1²] ≅ sgn ⊗ reduced Burau. This is the template argument rather than a literal statement about the full Jones representation of B4, so S009's citation is loose but fair. The direction S009 needs (Burau faithful => Jones faithful, Burau being a summand) is immediate anyway.
  -
    - claim: S010 KLS bibliography: arXiv v1 Sun 4 Feb 2024 (22 pp), v2 Thu 18 Apr 2024 (23 pp, latest). Published in Ann. Inst. H. Poincaré D 13 (2026) no. 4, 711-746, DOI 10.4171/AIHPD/213, CC BY 4.0. Received 13 Jun 2024, revised 17 Jul 2024, communicated by L. Chekhov; Crossref record 2025-08-11. The inventory record lacks the publication.
    - verdict: UPHELD
    - evidence: arXiv history: v1 15:54:47 UTC ('22 pages'), v2 17:56:58 UTC ('23 pages'); v3 returns 404. The EMS page gives 13 (2026), no. 4, pp. 711-746, License CC-BY-4.0, Submitted 13 June 2024, Accepted 12 June 2025, Published 11 August 2025. The journal PDF has 'Communicated by Leonid Chekhov' and 'Received 13 June 2024; revised 17 July 2024'. Crossref has 2025-08-11. The journal revision postdates arXiv v2, but Thms 3.1-3.4, the numbering and the converse remark match. Inventory: W/collab/lit/raw/lit-sweep-partial.json lists the source only as 'arXiv:2402.02553v2'. W/work/pass3/literature_notes.md does link the ems.press version.
  -
    - claim: KLS Thm 3.1: a nontrivial closed 4-braid knot with V=Δ=1 has H=1. Thm 3.2 + Sec 4.1: if V=1 and H≠1, then H = 1 + P4·F with F = -Σ_{j≤m}[2j+4][j+3][j+1]/([3][4]) A^{-2j-8} (or its mirror) for some m>=0, W = ±(2m+5), Δ≠1, chiral. Example (4.4) is m=0. Existence is not shown.
    - verdict: UPHELD
    - evidence: Independent exact check: <scratch>/7610ac96-4d03-4d32-b526-8a5647837809/scratchpad/wf-c2audit/skeptic-braid-route/scripts/kls_audit.py.
- The coefficients equal h_j(q^{±2},q^{±4}) for j<=30.
- For m=0..12, H_{K_m} has A-support exactly {-2m-8,...,-2m-2}, with H(A=q²)=1, H(A=1)≠1, q-inversion symmetry and a consistent mirror.
- (4.4) = H_{K_0}.

General proof for all m (stronger than the finder's m<=6 check): H-1 is divisible by P4, so H(x)=1 at x=A² ∈ {q^{±2},q^{±4}}.
- If the MFW window of 4 consecutive A²-powers contains 0, then H=1.
- Otherwise H is the unique interpolant, whose extreme coefficients are nonzero divided differences of a power of x. So the support is the full window and W is determined.
- With the extra node x=1 (Δ=1) the system is inconsistent unless the window contains 0, which gives Thm 3.1.

I verified this exactly for odd W in [-25,25] at q ∈ {2, 3/2, -5/3}.
  -
    - claim: KLS details: Sec 4.1 leaves a[2,2] free (it is the [2,1]-trace of the 3-braid σ3->σ1, a 2-component link with the same W). Sec 4.2: Vassiliev invariants of orders 2 and 3 vanish. Sec 4.3: 3-braids (c1,b1;c2,b2) in [-7,7], W=2m+5 with m=0..5, k from 0.1 to 150 in steps of 0.1, six survivors, all W=5 (heuristic). Sec 4.4: the related knots give no new constraints. Sec 4.5: positive braids with 5+12k crossings. Thms 3.3/3.4 added in v2. The abstract credits Bigelow with what Ito proved.
    - verdict: UPHELD
    - evidence: Every item matches the v2 text (<scratch>/7610ac96-4d03-4d32-b526-8a5647837809/scratchpad/wf-c2audit/skeptic-braid-route/notes/kls_v2.txt) and the journal version. The six braids listed are (-5,2;6,2), (-2,-1;1,7), (-2,-1;3,5), (-2,2;3,2), (-1,1;2,3), (-2,2;1,4). Thms 3.3/3.4 are absent from v1. The v1, v2 and journal abstracts all say 'S. Bigelow showed in 2000...', while the KLS intro separately credits Ito. Nuance: the Sec 4.5 search is finite for each k (3^{5+12k} braids) but unbounded over k, so it is a semi-decision procedure. The Sec 4.3 numerics were not re-run (UNCHECKED).
  -
    - claim: DERIVED 4-braid filter: for a nontrivial knot K with V=1 that is the closure of β in B4 with writhe W: (i) W is odd; (ii) either H=1 and |W|<=3 (W in {±1,±3}), or H≠1, Δ≠1, |W|=2m+5>=5 and H equals the unique KLS member (W>0) or its mirror (W<0); (iii) if S009 holds, K is not kernel-derived.
    - verdict: UPHELD
    - evidence: (i) The permutation is a 4-cycle, which is odd, and W ≡ parity mod 2. (ii) In KLS's convention (A H+ - A^{-1} H- = zH0; positive trefoil 2A^{-2}-A^{-4}+A^{-2}z²), MFW puts the A-degrees in [-W-3,-W+3]. The dichotomy H=1 <=> 0 in the window <=> |W|<=3 is exact by the interpolation argument above and the exact checks in kls_audit.py. The W>0 <-> K_m sign is confirmed by KLS (4.2), a[4]=q^{2m+5}. (iii) This is trivially true given a trivial kernel.
  -
    - claim: IMPL-kernel-searches: if S009 is correct, searches for nontrivial elements of ker Burau/TL/Jones-Hecke(B4) at generic parameter target an empty set, and the Bigelow and Ito Cor 3 routes on B4 are dead. Kernel searches for n>=5 (Burau's unfaithfulness does not transfer; Jones/RT faithfulness is open per KLS 2024) and trace-collision and non-braid routes remain.
    - verdict: UPHELD
    - evidence: The logic is correct. TL4 and Hecke contain reduced Burau as a summand up to a character twist, so a faithful Burau implies faithful TL and Jones. For n>=5, an unfaithful summand does not make a direct sum unfaithful. KLS v2 says faithfulness of the RT and Jones representations is 'also open'. On 2025-26 status for n>=5: my arXiv searches ('faithful Jones representation braid', 'Temperley-Lieb representation faithful') found no new result besides S009. This is not exhaustive, so it remains partly UNCHECKED. Everything here is conditional on S009, whose proof is unaudited.
  -
    - claim: IMPL-trace-collisions: the Jones polynomial of a closed 4-braid depends only on W and the traces of reduced Burau4(β) and of Burau3 of β's image in B3; S009 constrains none of these; 'S009 itself says the kernel and image remain wide open'.
    - verdict: REFUTED
    - evidence: The substance is UPHELD. At A=q², the quantum dimensions S*_[2,1,1] and S*_[1,1,1,1] vanish (a box with content -2), so KLS (4.1) reduces Jones to q^W, a[3,1] and a[2,2]. Those are traces of blocks equivalent to (scaled) reduced Burau4(β) and Burau3(π(β)). Faithfulness says nothing about trace values. The paraphrase of S009 is wrong as worded, though. The paper says 'The questions of giving both a useful characterization of its kernel and of its image remain wide open in general', meaning a useful characterization for general n. Read literally for n=4, the finding's wording contradicts S009's own Main Theorem. The defect is minor (wording only).
  -
    - claim: IMPL-LemmaQ: S008-S010 do not control unknotting number and bear on Lemma Q only as filters for candidates of braid index <=4.
    - verdict: UPHELD
    - evidence: Ito's Thm 1 controls only genus (>=N), braid index n and hyperbolicity. KLS constrains HOMFLY, W and character data of closed 4-braids. S009 is a faithfulness statement. None of the three primary texts mentions unknotting number.
  -
    - claim: (status framing) 'Treat S009 as a strong but unrefereed claim.'
    - verdict: UNCERTAIN
    - evidence: 'Unrefereed' is correct. Nothing found supports 'strong'. The only technical assessment is an automated v1 review with verdict CONDITIONAL. v2 rewrote the key step without changing any statement. My reading finds further unaddressed points (Thm 6.9 conjugation, the Γ1 bigon sentence, the basepoint cases, simplicity of Γ/Γ'). The specialist praise (He) is informal, and he is not reported to have checked the proof. A neutral label would be 'unrefereed claim by established experts with identified unverified steps'.

### summary

I checked every key claim against primary sources on 2026-11-02: arXiv abstract pages and PDFs of both S009 versions, KLS v1, v2 and the journal PDF, Ito, Bigelow, Kasahara, Crossref, the EMS Press page, zbMATH, SciAm, Columbia, the Wikipedia API, pith.science, alphaXiv and the MathOverflow API.

**What holds up**
- **Bibliography:** the versions, timestamps, sizes, page counts, comments and MSC for 2607.05283 are confirmed. v3 returns 404 and there is no journal-ref.
- **S009 statements:** all key statements are word-identical in v1 and v2, and the v2 changes the finder described are accurate.
- **Ito:** arXiv v1 only, Math. Z. 280 (2015) 347-353. Thm 1 and Cors 1-3 are as stated, and Cor 3 is strictly one-way.
- **Bigelow:** Prop 1.5 is as stated, with the omitted commutator step.
- **KLS:** v1/v2 dates are confirmed. The paper is published in AIHPD 13 (2026) no. 4, 711-746 (received 13 Jun 2024, revised 17 Jul 2024, accepted 12 Jun 2025, published 11 Aug 2025, CC BY 4.0, Chekhov).
- **My own exact checks:** the KLS coefficient identity holds for j<=30. The family's A-window, Jones=1 and Alexander≠1 hold for m<=12, and (4.4) is the m=0 member. A general interpolation argument proves the family shape and W=±(2m+5) for all m. The derived 4-braid filter is correct: H=1 exactly when |W|<=3. The unreduced/reduced Burau splitting check is correct.
- **Reception:** the facts are confirmed. alphaXiv shows commentsCount 0, and I found no MathOverflow thread or arXiv rebuttal.

**Corrections and additions**
1. Lemma 6.5's hypothesis is 'properly simple modulo 4-disks', not 'disjoint from β modulo 4-disks'.
2. 'S009 says the kernel and image remain wide open' misquotes the paper. It says 'useful characterization ... in general'.
3. Prop 6.7 is not the only weak spot. On my reading, which is not an audit:
   - Thm 6.9's conjugation paragraph shows Φ·Γ1 is a proper product but then asserts Φ = Φ'·Γ1. A repair (conjugating by Γ1) is plausible but unwritten.
   - The sentence about which bigon-forming polygons can occur with Γ1 was not updated for the new 'with basepoint' class.
   - Prop 5.1 asserts the basepoint cases without working them out.
   - 'Simple modulo 4-disks' for Γ and Γ' is never checked, and neither is the claim that f(Φ)·Γ is a proper product.
   - Whether any of these are real gaps is UNCHECKED.
4. pith.science labels its rebuttal 'Simulated authors' rebuttal'. It lists 4 major objections; the 4th, about staying in Brun4, is answered by Brun4 being normal in B4.
5. The '92 vs 99' mismatch is plausibly resolved. Columbia confirms the NYT profile is about Birman, and she was born 30 May 1927, so she was 92 at the project's 2019 start. The NYT text itself is still UNCHECKED: 403/captcha, and my fetch of the reprint was denied.
6. Kasahara Remark 5.6 is now read. It gives the Long direct-sum argument for π[2²,1] restricted to B4 versus reduced Burau, which is a loose but fair citation.
7. The 'strong claim' framing is unsupported; 'unrefereed' is correct.
8. Bou-Rabee is thanked only in v2, so 'pre-posting' feedback from him is not established.
9. Nothing here bears on unknotting number or Lemma Q.

**Remaining UNCHECKED items:** the proof of S009 itself, Long's theorem numbering, the Springer wording of Ito, the KLS Sec 4.3 numerics, and n>=5 Jones/TL faithfulness developments in 2025-26 (my limited search found none).

All files are in <scratch>/7610ac96-4d03-4d32-b526-8a5647837809/scratchpad/wf-c2audit/skeptic-braid-route/:
- notes/b4_v1.txt and notes/b4_v2.txt: S009 v1 and v2 text
- notes/diff_v1_v2_mine.txt: my sentence-level v1/v2 diff
- notes/kls_v1.txt, notes/kls_v2.txt, notes/kls_journal.txt: KLS texts
- notes/ito.txt, notes/bigelow.txt, notes/kasahara.txt, notes/sciam_paras.txt: other source texts
- scripts/kls_audit.py, scripts/burau_split.py, scripts/cmp_statements.py, scripts/sentdiff.py, scripts/lp.py: my check scripts
- dl/: raw downloads
