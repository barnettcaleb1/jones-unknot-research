# Human work, attribution, and corrections

This project builds on published mathematics. It does not claim to have proved Jones unknot detection, and its internal label **PROVED** is not a substitute for external specialist review. This page is the public reading guide to claims involving other researchers: what they established, what this collaboration used, what it challenged, and what remains unverified.

The archive preserves chronological research notes, including statements later withdrawn. Read the qualification here and the linked proof note before quoting an older letter. Numbered results below are pinned to the specified source version. No author is alleged to have acted improperly; the issues are mathematical hypotheses, calculations, and scope. The bibliography is in [References](REFERENCES.md).

## 1. Sikora's rational-solution conjecture: a candidate manuscript, not a completed public theorem

**Source.** Adam S. Sikora, *Tangle equations, the Jones conjecture, slopes of surfaces in tangle complements, and q-deformed rationals*, [arXiv:2005.08162v2](https://arxiv.org/pdf/2005.08162v2); published in *Canadian Journal of Mathematics* 76 (2024), 707–727, [DOI 10.4153/S0008414X23000755](https://doi.org/10.4153/S0008414X23000755). In v2, Proposition 1 proves uniqueness among rational framed solutions, Conjecture 2 asks uniqueness among all solutions, and Theorem 3 derives the conjecture from Jones unknot detection.

The checked numbering concordance is:

| arXiv v2 | Journal |
|---|---|
| Proposition 1 | Proposition 1.1 |
| Theorem 7 | Theorem 1.7 |
| Proposition 10 | Proposition 2.1 |
| Corollaries 19 and 20 | Corollaries 7.1 and 7.2 |
| Theorem 21 | Theorem 8.1 |
| Theorem 24 | Theorem 9.2 |

**Project contribution and status.** The collaboration prepared a [complete manuscript draft](../archive/work/paper/sikora-uniqueness/main.tex) with an [audited underlying proof](../archive/outputs/rational-tangle-uniqueness-audited-proof.txt), a [corrective audit](../archive/outputs/rational-tangle-uniqueness-audit.txt), and an [independent internal audit](../archive/collab/audits/LATE-41-audit.md). It proposes the framed theorem and an unframed three-probe extension. The final full-manuscript referee round did not finish before the research program moved on. Present it as a **candidate proof with internal audits**, not as an externally verified solution or an established priority claim. The draft's assertive title is historical authoring text, not a stronger review status.

The method owes substantial credit to Gainullin's surgery–Alexander strategy, Rasmussen–Rasmussen's Floer-simple machinery, the Casson–Walker surgery formula, Lickorish's rational-tangle/solid-torus criterion, and the classical unknot-surgery results of Kronheimer–Mrowka–Ozsváth–Szabó. The manuscript's detailed [source hierarchy](../archive/work/paper/sikora-uniqueness/README.md) controls conflicts between drafts. Proving the uniqueness statement would not prove the converse of Sikora's implication and would not solve Jones unknot detection.

The internal completeness audit's positive assessment was qualified: the original Lickorish and Boyer–Lines sources were not independently checked there, and a Floer specialist should check the distance hypothesis in the use of Rasmussen–Rasmussen Proposition 7.8 in the longitudinal-probe case. No completed final-manuscript referee report or external specialist approval is on record.

### The existing rational-tangle equivalence

Sikora's **v2 Theorem 24 / journal Theorem 9.2** already identifies Jones unknot detection with bracket detection of rational tangles. It gives equivalent trivial-tangle formulations with bracket vector \((1,0)\) in the framed setting and \((rA^n,0)\) in the unframed setting. The reverse implication uses a locally knotted trivial tangle. Lemma Q in this ledger restricts the domain to tangles having an actual unknot rational closure; **a converse from Lemma Q to Jones unknot detection has not been established here**. This is a restricted problem within Sikora's existing framework, not a newly discovered equivalence. V2 Proposition 25 also gives a bounded-crossing version; combined with the Tuzun–Sikora 24-crossing verification, it covers comparisons where each tangle has at most 11 crossings. Sikora's introduction announces further work on strong inversions; a bounded search that did not locate a follow-up does not establish that none exists.

### The separate Proposition 10(1) issue

V2, p. 5, **Proposition 10(1) / journal Proposition 2.1(1)** asserts uniqueness of a two-string solution to a single unlink-closure equation. The statement as printed is contradicted by the two-string tangle

\[
T_g=\langle 1/g\rangle+\langle-1/g\rangle,\qquad g>1\text{ odd}.
\]

Its numerator closure is the two-component unlink, whereas its denominator closure is the connected sum of the opposite \((2,g)\)-torus knots and has determinant \(g^2\). The branched cover has presentation \(gx+h=0,\;gy-h=0\), hence first homology \(\mathbb Z\oplus\mathbb Z/g\); it is not a solid torus. For \(g=3\), the denominator is the square knot, with determinant 9, whereas the trivial tangle is another solution to the same numerator equation. The printed proof exhibits that trivial solution without establishing uniqueness. The extension remark about framed equations in Section 4 fails for part (1) for the same reason. The [manuscript stress test](../archive/work/paper/sikora-uniqueness/main.tex) and [audit](../archive/collab/audits/LATE-41-audit.md) supply the convention-sensitive argument. This is a hand-verifiable objection to the statement as printed, with AI-only internal checks, not a claim of a new external referee assessment. Proposition 10(2), Theorems 3, 21 and 24, and the candidate manuscript's argument are not challenged by this example; none of the manuscript's steps uses Proposition 10.

### Attribution repairs made while drafting

The [original bracket-check script](../archive/handoff/recovered/scratchpad-7610ac96/scripts/bracket_check.py) was subsequently recovered from its file-creation input. It is now available as historical evidence; this publication update did not rerun it.

| Earlier project wording | Corrected treatment |
|---|---|
| A stronger component-count divisibility claim attributed to Stoimenow Proposition 6.5 | The manuscript uses only the odd-determinant/knot consequence checked there. |
| The two-probe example treated as new or credited to Ernst–Sumners 1990 | It is a mirror/reparametrization of **Ernst–Sumners 1999, Example 3**. |
| Original Boyer–Lines theorem numbering asserted without a source check | The exact surgery formula is cited through **Ni–Wu, Proposition 3.1**. |
| Unframed two-closure uniqueness assumed without qualification | Actual two-probe counterexamples remain; the third determinant is an added hypothesis. |
| Sikora's talk abstract used as a priority certificate | An abstract records its wording at that time; it cannot establish absence of another proof. |

## 2. Carmi–Cohen: an obstruction to a universal intermediate package

**Source.** Avishy Carmi and Eliahu Cohen, *On trivial Jones–Vassiliev polynomials*, [arXiv:2606.22410v1](https://arxiv.org/pdf/2606.22410v1), 21 June 2026. The relevant package is Proposition 5.12 (pp. 39–40), Theorem 5.6 (pp. 30–31), and Lemma 5.8 (pp. 31–33). It claims a residual-degree cap determined by the pre-planting host, independently of an arbitrarily long residual twist.

**Project finding.** On the specified antiparallel seed of a minimal three-crossing trefoil host, the odd residual family satisfies

\[
V_1=x^2+x^6-x^8,
\qquad V_L=x^4V_{L-2}+x^2-x^4+x^6-x^8.
\]

Writing \(p=x-x^{-1}\) and \(V=A(p)+xB(p)\), its degree is \(2L+5\), with \(b_{2L+5}=-1\). At \(L=23\), \(b_{51}=-1\) conflicts with the package's cap \(3\cdot3+11+2=22\).

This is an explicit objection to the **combined universal construction and cap**, not an assertion that the conditional skein identity or Theorem 5.6 with independently verified hypotheses is false. The project has not isolated a unique defective geometric submove. The example's Jones polynomial is nonconstant: it is not a counterexample to the paper's main theorem or to Jones unknot detection. The ordinary bound using the residual diagram's \(L+2\) crossings remains compatible with the calculation.

The source's Theorem 6.8 (pp. 50–53) asserts the order bound \(N\leq3c(K)\) for its nontrivial \(J_N\)-trivial knots; Theorem 6.9 (p. 53) asserts Jones unknot detection. The proof of Theorem 6.8 uses the two-machine descent of Theorem 5.11, which uses Lemma 5.8's initialization. **If the recorded objection to that universal package is accepted, the v1 argument does not establish its main theorems.** This is a proof-gap conclusion, not a disproof of those statements. Archived shorthand saying the paper was “refuted” refers only to the intermediate package; a later literature helper's “unverified” entry was written without awareness of this earlier audit.

Read the [claim-by-claim source review](../archive/work/paper/carmi-cohen-obstruction/claim-review.md), [draft note](../archive/work/paper/carmi-cohen-obstruction/main.tex), [exact arithmetic certificate](../archive/work/paper/carmi-cohen-obstruction/verify.py), and [actual-diagram check notes](../archive/work/paper/carmi-cohen-obstruction/diagram-check-notes.md). The manuscript remains an internal-review draft. Reproduction of its exact calculation is different from independent specialist acceptance of the geometric reading of the source package.

## 3. Bharathram–Birman–Brendle: a parity/count incompatibility, not nonfaithfulness

**Source.** Vasudha Bharathram, Joan S. Birman, and Tara E. Brendle, *The Burau representation is faithful for n = 4*, [arXiv:2607.05283v2](https://arxiv.org/pdf/2607.05283v2), posted 14 September 2026 (paper dated 15 September). The project inspected the preparation and unequal-count argument involving Proposition 6.7, Corollary 6.8 and Theorem 6.9.

**Status of the main theorem: not refuted.** On the project's reading, there **appears to be a gap in the proof** in v2: the Section 6 preparation/count route can only certify braids whose stabilization is nontrivial under Burau at \(t=-1\), whereas an element of the generic Burau kernel is trivial at that specialization. If this reading is correct, the route through Proposition 6.7, Corollary 6.8 and Theorem 2.3 does not establish faithfulness for \(n=4\), or its Jones-representation consequence in Corollary 1.1. It does not show either statement false. These are **AI-only checks**, without external specialist review.

**Project finding.** If an unsimplified Moody pairing is \(M(t)=\sum_{i=1}^m\epsilon_i t^{k_i}\) and satisfies the stated parity relation, then every \(\epsilon_i(-1)^{k_i}\) is equal, so \(|M(-1)|=m\). A braid in the Burau kernel specialized at \(t=-1\) preserves the absolute specialized pairing. Therefore two parity-satisfying configurations related by that braid must have equal counts. The note supplies an explicit nontrivial Brunnian braid in the specialized kernel.

The consequence is an incompatibility of the **combined preparation, simultaneous parity, and unequal-count claims**. The parity calculation uses Section 3, equation (1), and Lemma 3.1; stabilization uses Observation 2.1 and the proof of Theorem 2.3. The localization is a dichotomy involving the shortcut criterion in the proof of Theorem 6.9 and the parity/“Furthermore” package of Proposition 6.7; it does not accuse Proposition 5.1. The note also flags the first-factor hypothesis in the use of “proper product” in \(B_5\). It is not an isolated counterexample to Proposition 6.7 under all its conditional geometric hypotheses: the required huge proper-product construction was not completed, conditions (1) and (2) were not checked from the figures, and the internal cases of Lemmas 6.3 and 6.6 were not fully checked. It is not a kernel element for generic Burau, a nonfaithfulness theorem, or a Jones counterexample. Equal counts also do not imply equal polynomials: exponent information can survive.

**Prior critique.** The missing parity re-check for the modified loop \(\Gamma'\), in the corresponding v1 step, was already flagged by an [AI-generated pith.science review](https://pith.science/paper/2607.05283), recorded in the project's source notes as posted on 7 July 2026. Credit for that observation is not claimed here. The \(t=-1\) incompatibility and explicit specialized-kernel witness are the project's additions; priority beyond the sources located is unassessed. The more specific \(\Gamma'\) localization remains conditional on the source's asserted property (2): either parity fails or that property fails. The earlier review could not be reopened during this handoff edit; its date and characterization are taken from the archived audit.

See the [complete scoped obstruction](../archive/work/global_design/bbb_parity_obstruction.md), [later redacted note](../archive/handoff/copied/jones-adversarial-pass/bbb-gap-note/note/bbb-gap-note.tex), [saved certificate and output](../archive/handoff/copied/jones-adversarial-pass/bbb-gap-note/phi0_check.out), [obstacle report](../archive/collab/msgs/20261103-174515-claude.md), and [separate cone-domain failure](../archive/work/global_design/bbb_cone_obstruction.md). The Figure 7.4 exponent discrepancy reported in the obstacle letter is a separate computational observation, not the proof of the package incompatibility. Any public claim about a later version requires a new version-specific check.

## 4. Grigsby–Wehrli: a conditional grading objection; the spectral sequence stands

**Source.** J. Elisenda Grigsby and Stephan Wehrli, *On the Colored Jones Polynomial, Sutured Floer Homology, and Knot Floer Homology*, [arXiv:0807.1432v3](https://arxiv.org/pdf/0807.1432v3), especially Proposition 5.20, Proposition 6.9, and Conjecture 7.1. The project uses their spectral sequence and credits it as a published input.

**Qualified project observation.** A saved doubled-figure-eight chain has source delta multiplicities \((2,6,9,6,2)\), total rank 25. The specified target has an 11-dimensional group in one relative Maslov/Spin-c sector. Under the recorded input identification, rank equality forces collapse and a lift as proposed in Conjecture 7.1 cannot place that sector in a source grading of dimension at most 9.

The [grading audit](../archive/work/theory_restart/gw_delta_referee.md) independently parses a saved chain but does **not** independently reconstruct and recompute the cable input. Its public status is therefore **conditional computational objection, reconstruction pending**. It does not refute the ungraded spectral sequence or all possible grading relations. The [sutured-sequence audit](../archive/work/theory_restart/sutured_sequence_referee.md) also explains the mirror and coefficient conventions.

Two mistakes were ours, not theirs: total knot-Floer rank need not be at least \(2g+1\) (\(T(3,4)\) is a counterexample), and rank five does not classify a knot as figure-eight or cinquefoil. The latter was incorrectly attributed to Farber–Reinoso–Wang: their [Theorem A](https://arxiv.org/pdf/2203.01402v2) detects \(T(2,5)\) from its **bigraded** knot-Floer homology over \(\mathbb Q\), not its total rank. The rank-three trefoil input used in the corrected low-rank argument is [Hedden–Watson, Corollary 8](https://arxiv.org/pdf/1404.6913v3), also [Baldwin–Vela-Vick, Corollary 1.5](https://msp.org/agt/2018/18-6/agt-v18-n6-p14-p.pdf), with \(\mathbb F_2\) coefficients. Also, the converse of the cutting statement removed between versions of [0907.4375](https://arxiv.org/abs/0907.4375v2) must not be imported from v1.

## 5. Snape, Watson, and KWZ: credit the existing detecting invariants

Michael Snape's [2018 thesis](https://theses.gla.ac.uk/39015/) already formulates the relevant strongly-invertible-unknot Jones question (the unnumbered question after Example 3.2.6, p. 67). Theorems 0.1.1–0.1.3 establish Khovanov versions; Propositions 2.1.7–2.1.8 supply the framed Sakuma-link characterization. The project's Sakuma and annular reformulations are not new detection theorems. Liam Watson's [invariant \(\kappa\)](https://arxiv.org/abs/1311.1085v4) detects the trivial strongly invertible knot at the homological level. This does not imply that its Euler characteristic detects it. [Hedden–Watson 2010, Theorem 1](https://arxiv.org/abs/0805.4423) already proves reduced-Khovanov detection for knots of tangle unknotting number one; it does not prove the corresponding Jones statement. Kotelskiy–Watson–Zibrowius and Kotelskiy–Lidman–Moore–Watson–Zibrowius supply the curve models, gluing, and geography used throughout the homology lane; they did not establish our proposed endpoint laws.

The [Sakuma recipe report](../archive/collab/msgs/20261103-191856-claude.md) reports a discrepancy with Snape Example 3.2.6: its figure-eight value matched the implementation's linking-number-\(+2\) framing, rather than the preferred framing, among the framings tested from \(-3\) to \(3\). The general preferred-framing recipe passed its other controls. **This remains a reported convention-dependent discrepancy**, not a publication-ready independent erratum. Before strengthening it, reproduce the thesis diagram and the preferred framing from the archived construction data.

Several corrections concerned our use of the literature:

- Linear-component classification was incorrectly applied to the entire Bar–Natan invariant; the reduced Khovanov and Bar–Natan curve objects must be distinguished.
- Longer special components were already noted in [KWZ 2104.13592](https://arxiv.org/abs/2104.13592); absence in an initial table was not a theorem.
- Extension of an entire actual object under [KWZ 2202.01460, Theorem 4.4](https://arxiv.org/abs/2202.01460) does not imply independent extension of every direct summand. The isolated-block question remains open in this project.
- Conversely, independent summand lifts do give a lift of their direct sum. The earlier lens assertion that a single special block must lift was not established. KWZ Theorems 1.2, 5.1 and 5.4 also replace older conjectural geography language over \(\mathbb F_2\); the project's residual concern about even-length rational components at infinite slope is separate.
- [Lipshitz–Sarkar 2203.13895, Theorem 1.1 and Section 3](https://arxiv.org/abs/2203.13895v1) use an intravergent diagram and **unreduced** homology over \(\mathbb F_2\). Their first page is \(Kh(K)\otimes\mathbb F_2[\theta,\theta^{-1}]\), with differential \(\theta(1+\tau_*)\). The target is the homology of the axis-moving cone \(\operatorname{Cone}(f^+)\) for annular versions of a chosen quotient knot. It is not the tangle multicurve, the two theta constituents, or \(N(T)\). Proposition 4.4 gives geometric fixed-point data; the introduction leaves full spectral-sequence invariance and a reduced analogue unproved. The project has not established that this input is non-additive relative to the KWZ decomposition.
- An archived gauge-theory lens attributed \(\chi(I^\natural(K))=\sigma(K)/2\) to Daemi–Scaduto and inferred a barrier. That formula fails for the unknot: [Kronheimer–Mrowka, Section 1.1, Propositions 1.2 and 1.4](https://arxiv.org/pdf/1005.4346v1) give \(I^\natural(U)=\mathbb Z\). The attribution and barrier were withdrawn. This is our mistake; no criticism of a Daemi–Scaduto theorem is intended.

See [the curve-referee synthesis](../archive/work/theory_restart/jtilt_referee_synthesis.md), [replacement-map audit](../archive/work/theory_restart/maps_report_referee.md), and [Lipshitz–Sarkar scope audit](../archive/work/theory_restart/lipshitz_sarkar_bridge_audit.md). The universal endpoint/TILT proposals were later refuted by an actual quotient tangle; that failure belongs to this project.

## 6. Existing constructions and complexity: avoid false novelty

| Human work | What the project should credit | What it must not infer |
|---|---|---|
| Thistlethwaite 2001; Eliahou–Kauffman–Thistlethwaite, *Topology* 42 (2003), 155–169 | Thistlethwaite's first Jones-trivial link examples; EKT's infinite families and Hopf-shell mechanism | Such a link is automatically a knot counterexample after fusion. LL2(1)'s shifted polynomial is not exact JT2 membership. |
| Eliahou–Fromentin, [1610.05560v2](https://arxiv.org/abs/1610.05560v2) | Nontrivial distinct knots with coefficientwise congruence modulo \(2^r\) | Primality, minimum crossing number, or increasing Taylor depth. Our [deduction](../archive/work/theory_restart/eliahou_fromentin_bridge_audit.md) gives exact depth four; it is internally checked, with novelty unassessed. |
| Champanerkar–Kofman, [2005](https://arxiv.org/abs/math/0404236v3) and [2006](https://arxiv.org/abs/math/0605631v3), distinct papers | The 2005 Mahler-measure limits under twisting; the 2006 twist-bracket expansion, Kanenobu invisible directions, and resonant-hyperplane method | The whole fixed-twist framework is new to this project. Our [binary-input algorithmic deduction](../archive/work/theory_restart/fixed_twist_bridge_audit.md) has explicitly fixed-template scope. |
| Jones 1985; Champanerkar–Kofman 2006, Proposition 2.2, equation (3) | The classical specialization \(V_L(1)=(-2)^{\mu-1}\) detects component count | The component-count input in our boundary-matching lemma is new. The project applies that input to common closing tangles. |
| Kanenobu 1986, two papers listed in the bibliography | Polynomial-preserving knot/link families, including the constant-sum mechanism | A new family is nontrivial or Jones-unit merely because it resembles that mechanism. |
| Jaeger–Vertigan–Welsh 1990 | Classical exact Jones/Tutte evaluation hardness | Hardness of exact whole-polynomial equality to one specified unlink value. |
| Welsh 1993, as quoted by Hass–Lagarias–Pippenger, Section 1, p. 6 of arXiv v1 | The observation that an affirmative Jones conjecture yields a \(P^{\#P}\) unknot-recognition algorithm | Priority for the project's routine conditional complexity refinements. |
| Bar–Natan 1995, Theorems 1–2 | Polynomial-time evaluation and polynomial magnitude bounds for **one fixed finite-type invariant** | Control of constants as the order grows. Remark 1.1 announces link/tangle extensions without proving them; our link estimate uses a direct proof. |
| Kuperberg, [*How Hard Is It to Approximate the Jones Polynomial?*](https://theoryofcomputing.org/articles/v011a006/) | Approximation/value-distinguishing hardness at specified roots | Many-one hardness of exact equality of the whole Laurent polynomial to the unlink polynomial. |
| Hass–Lagarias–Pippenger; Lackenby | NP certificates for unknot recognition and splitting (HLP Theorems 1.1–1.2), and for knottedness (Lackenby); together they supply the conditional \(NP\cap coNP\) observation | Jones-triviality equals unknot recognition without assuming Jones detection. |
| Lickorish–Millett (including Murakami's theorem) | Classical special-root evaluations | Arbitrary arithmetic gates for the project's quotient invariant without normalization and component hypotheses. |

The [JT2 scope note](../archive/work/theory_restart/jt2_scope_audit.md) records the exact decision language and quantifiers. Failure to locate a theorem in a bounded literature search is not proof of novelty. The latest exact-gadget restrictions were only TRUSTED when the independent referee workflow was paused.

For the twist sources, the detailed prior locators are Champanerkar–Kofman 2005 Proposition 3.3, and 2006 Definition 1/Proposition 2.1, Examples 4–5, Lemmas 3.1–3.4/Example 6, Proposition 3.5 and Proposition 4.1. The project's explicit coset certificates and fixed-template algorithm should be read against that framework. Its [uniform Jones-jet estimate](../archive/work/theory_restart/depth_uniform_audit.md), \(2(16n)^r\) for knots and \(8(32n)^r\) for two-component links, has a separate descending-skein argument. An earlier attempt to obtain a growing-order rate from Bar–Natan's fixed-order constant was withdrawn; fixed-jet computability itself is classical.

### Known Jones-detection classes and the branch-knot claim

[Lickorish–Thistlethwaite 1988](https://www.e-periodica.ch/cntmng?pid=com-001%3A1988%3A63%3A%3A32) introduced adequacy and proved nontriviality for adequate links, with an extreme-coefficient constraint for semiadequate links and partial Montesinos results. Credit for the broader semiadequate nontriviality used here belongs to **Stoimenow**: in [arXiv:math/0606255v1](https://arxiv.org/pdf/math/0606255v1), Theorem 4.1, Corollary 4.1, Proposition 4.3 and Corollary 6.3 cover the relevant semiadequate, Montesinos, Whitehead-double and 3-braid statements. A single extreme coefficient of modulus one does not by itself exclude \(V=1\). The v2 title differs from v1; the bibliography pins the locators to v1.

[Tuzun–Sikora](https://arxiv.org/abs/2003.06724v2) verified Jones unknot detection through **24 crossings**, following their 22- and 23-crossing work. [Dasbach–Lowrance](https://arxiv.org/abs/1604.03501v2) give the extreme-coefficient restriction for Turaev-genus-one and almost-alternating links. These are relevant controls when evaluating the V3 branch-knot claims in [Research map](RESEARCH_MAP.md). The \(a_2\ne0\) shortcut uses classical Mullins and Casson-surgery inputs; its signs depend on a consistent orientation and normalization, as recorded in the [odd-closure audit](../archive/work/theory_restart/roots_odd_referee.md). The proposed contribution is the uniform Jones-level assertion on the \(a_2=0\) core, including the specific E6 family—not a new detection theorem for all Montesinos knots or a new Khovanov detection theorem. The bounded prior-art search found no theorem covering that whole assertion; **novelty and the full geometric claim still need external review**.

## 7. Rules for future corrections and citations

Each correction record should contain the exact version, theorem/page, original hypotheses, explicit witness or proof, reproduction dependencies, and the strongest conclusion justified. Separate four cases: **our misreading**, **our independently derived extension**, **a conditional computational discrepancy**, and **an objection to a source statement**. Record later repairs and author responses without deleting the original record. Cite the source for its contribution as well as for the claim being discussed.

The source text and arithmetic behind several statements above were checked for this publication guide on 17 November 2026. The subsequent handoff edit incorporated earlier source audits and reopened selected primary statements and bibliographic records; a metadata check is not a new full referee pass. These checks did not rerun every geometric computation, re-referee either full manuscript, or establish priority. No external endorsement is represented here.
