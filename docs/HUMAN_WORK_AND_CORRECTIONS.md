# Human work, attribution, and corrections

This project builds on published mathematics. It does not claim to have proved Jones unknot detection, and its internal label **PROVED** is not a substitute for external specialist review. This page is the public reading guide to claims involving other researchers: what they established, what this collaboration used, what it challenged, and what remains unverified.

The archive preserves chronological research notes, including statements later withdrawn. Read the qualification here and the linked proof note before quoting an older letter. Numbered results below are pinned to the specified source version. No author is alleged to have acted improperly; the issues are mathematical hypotheses, calculations, and scope. The bibliography is in [References](REFERENCES.md).

## 1. Sikora's rational-solution conjecture: a candidate manuscript, not a completed public theorem

**Source.** Adam S. Sikora, *Tangle equations, the Jones conjecture, slopes of surfaces in tangle complements, and q-deformed rationals*, [arXiv:2005.08162v2](https://arxiv.org/pdf/2005.08162v2); published in *Canadian Journal of Mathematics* 76 (2024), 707–727. In v2, Proposition 1 proves uniqueness among rational framed solutions, Conjecture 2 asks uniqueness among all solutions, and Theorem 3 derives the conjecture from Jones unknot detection. The journal numbers differ.

**Project contribution and status.** The collaboration prepared a [complete manuscript draft](../archive/work/paper/sikora-uniqueness/main.tex) with an [audited underlying proof](../archive/outputs/rational-tangle-uniqueness-audited-proof.txt), a [corrective audit](../archive/outputs/rational-tangle-uniqueness-audit.txt), and an [independent internal audit](../archive/collab/audits/LATE-41-audit.md). It proposes the framed theorem and an unframed three-probe extension. The final full-manuscript referee round did not finish before the research program moved on. Present it as a **candidate proof with internal audits**, not as an externally verified solution or an established priority claim. The draft's assertive title is historical authoring text, not a stronger review status.

The method owes substantial credit to Gainullin's surgery–Alexander strategy, Rasmussen–Rasmussen's Floer-simple machinery, the Casson–Walker surgery formula, Lickorish's rational-tangle/solid-torus criterion, and the classical unknot-surgery results of Kronheimer–Mrowka–Ozsváth–Szabó. The manuscript's detailed [source hierarchy](../archive/work/paper/sikora-uniqueness/README.md) controls conflicts between drafts. Proving the uniqueness statement would not prove the converse of Sikora's implication and would not solve Jones unknot detection.

### The separate Proposition 10(1) issue

V2, p. 5, Proposition 10(1), asserts uniqueness of a two-string solution to a single unlink-closure equation. The project's explicit objection is the two-string tangle

\[
T_g=\langle 1/g\rangle+\langle-1/g\rangle,\qquad g>1\text{ odd}.
\]

Its numerator closure is the two-component unlink, whereas its denominator closure is the connected sum of the opposite \((2,g)\)-torus knots and has determinant \(g^2\). The branched cover has presentation \(gx+h=0,\;gy-h=0\), hence first homology \(\mathbb Z\oplus\mathbb Z/g\); it is not a solid torus. Thus the proposed uniqueness cannot be used as a shortcut in our proof. The [manuscript stress test](../archive/work/paper/sikora-uniqueness/main.tex) and [audit](../archive/collab/audits/LATE-41-audit.md) supply the convention-sensitive argument. This objection is to that one statement in v2, not to Sikora's other theorems or the whole paper.

### Attribution repairs made while drafting

| Earlier project wording | Corrected treatment |
|---|---|
| A stronger component-count divisibility claim attributed to Stoimenow Proposition 6.5 | The manuscript uses only the odd-determinant/knot consequence checked there. |
| The two-probe example treated as new or credited to Ernst–Sumners 1990 | It is a mirror/reparametrization of **Ernst–Sumners 1999, Example 3**. |
| Original Boyer–Lines theorem numbering asserted without a source check | The exact surgery formula is cited through **Ni–Wu, Proposition 3.1**. |
| Unframed two-closure uniqueness assumed without qualification | Actual two-probe counterexamples remain; the third determinant is an added hypothesis. |
| Sikora's talk abstract used as a priority certificate | An abstract records its wording at that time; it cannot establish absence of another proof. |

## 2. Carmi–Cohen: an obstruction to a universal intermediate package

**Source.** Avishy Carmi and Eliahu Cohen, *On trivial Jones–Vassiliev polynomials*, [arXiv:2606.22410v1](https://arxiv.org/pdf/2606.22410v1), 21 June 2026. The relevant package is Proposition 5.12, Theorem 5.6, and Lemma 5.8. It claims a residual-degree cap determined by the pre-planting host, independently of an arbitrarily long residual twist. Theorem 6.8 and Theorem 6.9 are later conclusions.

**Project finding.** On the specified antiparallel seed of a minimal three-crossing trefoil host, the odd residual family satisfies

\[
V_1=x^2+x^6-x^8,
\qquad V_L=x^4V_{L-2}+x^2-x^4+x^6-x^8.
\]

Writing \(p=x-x^{-1}\) and \(V=A(p)+xB(p)\), its degree is \(2L+5\), with \(b_{2L+5}=-1\). At \(L=23\), \(b_{51}=-1\) conflicts with the package's cap \(3\cdot3+11+2=22\).

This is an explicit objection to the **combined universal construction and cap**, not an assertion that the conditional skein identity or Theorem 5.6 with independently verified hypotheses is false. The project has not isolated a unique defective geometric submove. The example's Jones polynomial is nonconstant: it is not a counterexample to the paper's main theorem or to Jones unknot detection. The ordinary bound using the residual diagram's \(L+2\) crossings remains compatible with the calculation.

Read the [claim-by-claim source review](../archive/work/paper/carmi-cohen-obstruction/claim-review.md), [draft note](../archive/work/paper/carmi-cohen-obstruction/main.tex), [exact arithmetic certificate](../archive/work/paper/carmi-cohen-obstruction/verify.py), and [actual-diagram check notes](../archive/work/paper/carmi-cohen-obstruction/diagram-check-notes.md). The manuscript remains an internal-review draft. Reproduction of its exact calculation is different from independent specialist acceptance of the geometric reading of the source package.

## 3. Bharathram–Birman–Brendle: a parity/count incompatibility, not nonfaithfulness

**Source.** Vasudha Bharathram, Joan S. Birman, and Tara E. Brendle, *The Burau representation is faithful for n = 4*, [arXiv:2607.05283v2](https://arxiv.org/pdf/2607.05283v2), September 2026. The project inspected the preparation and unequal-count argument involving Proposition 6.7 and Theorem 6.9.

**Project finding.** If an unsimplified Moody pairing is \(M(t)=\sum_{i=1}^m\epsilon_i t^{k_i}\) and satisfies the stated parity relation, then every \(\epsilon_i(-1)^{k_i}\) is equal, so \(|M(-1)|=m\). A braid in the Burau kernel specialized at \(t=-1\) preserves the absolute specialized pairing. Therefore two parity-satisfying configurations related by that braid must have equal counts. The note supplies an explicit nontrivial Brunnian braid in the specialized kernel.

The consequence is an incompatibility of the **combined preparation, simultaneous parity, and unequal-count claims**. It is not an isolated counterexample to Proposition 6.7 under all its conditional geometric hypotheses; the required huge proper-product construction was not completed. It is not a kernel element for generic Burau, a nonfaithfulness theorem, or a Jones counterexample. Equal counts also do not imply equal polynomials: exponent information can survive.

See the [complete scoped obstruction](../archive/work/global_design/bbb_parity_obstruction.md), [obstacle report](../archive/collab/msgs/20261103-174515-claude.md), and [separate cone-domain failure](../archive/work/global_design/bbb_cone_obstruction.md). The Figure 7.4 exponent discrepancy reported in the obstacle letter is a separate computational observation, not the proof of the package incompatibility. Any public claim about a later version requires a new version-specific check.

## 4. Grigsby–Wehrli: a conditional grading objection; the spectral sequence stands

**Source.** J. Elisenda Grigsby and Stephan Wehrli, *On the Colored Jones Polynomial, Sutured Floer Homology, and Knot Floer Homology*, [arXiv:0807.1432v3](https://arxiv.org/pdf/0807.1432v3), especially Proposition 5.20, Proposition 6.9, and Conjecture 7.1. The project uses their spectral sequence and credits it as a published input.

**Qualified project observation.** A saved doubled-figure-eight chain has source delta multiplicities \((2,6,9,6,2)\), total rank 25. The specified target has an 11-dimensional group in one relative Maslov/Spin-c sector. Under the recorded input identification, rank equality forces collapse and a lift as proposed in Conjecture 7.1 cannot place that sector in a source grading of dimension at most 9.

The [grading audit](../archive/work/theory_restart/gw_delta_referee.md) independently parses a saved chain but does **not** independently reconstruct and recompute the cable input. Its public status is therefore **conditional computational objection, reconstruction pending**. It does not refute the ungraded spectral sequence or all possible grading relations. The [sutured-sequence audit](../archive/work/theory_restart/sutured_sequence_referee.md) also explains the mirror and coefficient conventions.

Two mistakes were ours, not theirs: total knot-Floer rank need not be at least \(2g+1\) (\(T(3,4)\) is a counterexample), and rank five does not classify a knot as figure-eight or cinquefoil. Also, the converse of the cutting statement removed between versions of [0907.4375](https://arxiv.org/abs/0907.4375v2) must not be imported from v1.

## 5. Snape, Watson, and KWZ: credit the existing detecting invariants

Michael Snape's [2018 thesis](https://theses.gla.ac.uk/39015/) already formulates the relevant strongly-invertible-unknot Jones question; the project's Sakuma and annular reformulations are not new detection theorems. Liam Watson's [invariant \(\kappa\)](https://arxiv.org/abs/1311.1085v4) detects the trivial strongly invertible knot at the homological level. This does not imply that its Euler characteristic detects it. Kotelskiy–Watson–Zibrowius and Kotelskiy–Lidman–Moore–Watson–Zibrowius supply the curve models, gluing, and geography used throughout the homology lane; they did not establish our proposed endpoint laws.

The [Sakuma recipe report](../archive/collab/msgs/20261103-191856-claude.md) reports a discrepancy with Snape Example 3.2.6: its figure-eight value matched a different framing in the implementation. **This remains a reported convention-dependent discrepancy**, not a publication-ready independent erratum. Before strengthening it, reproduce the thesis diagram and the preferred framing from the archived construction data.

Several corrections concerned our use of the literature:

- Linear-component classification was incorrectly applied to the entire Bar–Natan invariant; the reduced Khovanov and Bar–Natan curve objects must be distinguished.
- Longer special components were already noted in [KWZ 2104.13592](https://arxiv.org/abs/2104.13592); absence in an initial table was not a theorem.
- Extension of an entire actual object under [KWZ 2202.01460, Theorem 4.4](https://arxiv.org/abs/2202.01460) does not imply independent extension of every direct summand. The isolated-block question remains open in this project.
- A map-level interpretation of [Lipshitz–Sarkar 2203.13895](https://arxiv.org/abs/2203.13895) remains open. Its target is not simply the project's bullet invariant \(N(T)\).

See [the curve-referee synthesis](../archive/work/theory_restart/jtilt_referee_synthesis.md), [replacement-map audit](../archive/work/theory_restart/maps_report_referee.md), and [Lipshitz–Sarkar scope audit](../archive/work/theory_restart/lipshitz_sarkar_bridge_audit.md). The universal endpoint/TILT proposals were later refuted by an actual quotient tangle; that failure belongs to this project.

## 6. Existing constructions and complexity: avoid false novelty

| Human work | What the project should credit | What it must not infer |
|---|---|---|
| Eliahou–Kauffman–Thistlethwaite, *Topology* 42 (2003), 155–169 | Actual nontrivial links with unlink Jones polynomial; the Hopf-shell mechanism | Such a link is automatically a knot counterexample after fusion. LL2(1)'s shifted polynomial is not exact JT2 membership. |
| Eliahou–Fromentin, [1610.05560v2](https://arxiv.org/abs/1610.05560v2) | Nontrivial distinct knots with coefficientwise congruence modulo \(2^r\) | Primality, minimum crossing number, or increasing Taylor depth. Our [deduction](../archive/work/theory_restart/eliahou_fromentin_bridge_audit.md) gives exact depth four; it is internally checked, with novelty unassessed. |
| Champanerkar–Kofman, [math/0605631v3](https://arxiv.org/abs/math/0605631v3) | Multivariable twist-bracket expansion and the fixed-template setting | The whole fixed-twist framework is new to this project. Our [binary-input algorithmic deduction](../archive/work/theory_restart/fixed_twist_bridge_audit.md) has explicitly fixed-template scope. |
| Kuperberg, [*How Hard Is It to Approximate the Jones Polynomial?*](https://theoryofcomputing.org/articles/v011a006/) | Approximation/value-distinguishing hardness at specified roots | Many-one hardness of exact equality of the whole Laurent polynomial to the unlink polynomial. |
| Hass–Lagarias–Pippenger; Lackenby | NP certificates for unknot recognition and knottedness, respectively | Jones-triviality equals unknot recognition without assuming Jones detection. |
| Lickorish–Millett (including Murakami's theorem) | Classical special-root evaluations | Arbitrary arithmetic gates for the project's quotient invariant without normalization and component hypotheses. |

The [JT2 scope note](../archive/work/theory_restart/jt2_scope_audit.md) records the exact decision language and quantifiers. Failure to locate a theorem in a bounded literature search is not proof of novelty. The latest exact-gadget restrictions were only TRUSTED when the independent referee workflow was paused.

## 7. Rules for future corrections and citations

Each correction record should contain the exact version, theorem/page, original hypotheses, explicit witness or proof, reproduction dependencies, and the strongest conclusion justified. Separate four cases: **our misreading**, **our independently derived extension**, **a conditional computational discrepancy**, and **an objection to a source statement**. Record later repairs and author responses without deleting the original record. Cite the source for its contribution as well as for the claim being discussed.

The source text and arithmetic behind several statements above were checked for this publication guide on 17 November 2026. That check did not rerun every geometric computation, re-referee either full manuscript, or establish priority. No external endorsement is represented here.
