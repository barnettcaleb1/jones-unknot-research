# Research map: what was built, and where it stops

[Start here](START_HERE.md) · [Small results](SMALL_RESULTS.md) · [Failures](FAILURES.md) · [Open problems](OPEN_PROBLEMS.md)

The project repeatedly changed scale. It began with concrete proof audits and knot constructions, moved to tangle and surgery reductions, then to representation theory and categorification, and finally to exact counting gadgets. The persistent issue was **realization**: algebraic data that look like the unknot need not provide the topological information required to recognize it.

This map records the final scope of each route. The original chronological accounts are retained in the [early handoff](../archive/outputs/claude-handoff/CLAUDE_JONES_HANDOFF.txt) and [later theory log](../archive/collab/THEORY-width-ladder.md).

## 1. The first rounds: make proposed mechanisms exact

**Period:** 31 October–2 November. **Entry points:** [early ledger](../archive/work/handoff/early-ledger.txt), [middle ledger](../archive/work/handoff/middle-ledger.txt), [late ledger](../archive/work/handoff/late-ledger.txt).

The first rounds tested several ways one might turn a unit Jones polynomial into trivial topology: twist compression, band fusion of Jones-trivial links, positivity, braid kernels, finite root tests, satellite operators, and control of homological rank or exterior volume. Most results in these ledgers are small deductions or exclusions of a precisely specified construction.

Three distinctions emerged.

* **Finite invariant data are not complete data.** Actual knots can evade a prescribed finite collection of roots or finite Taylor jets. Formal higher-color sequences can pass many algebraic checks without being knot invariants.
* **A scalar is not an operator.** A single closure value does not recover the braid operator, a second closure, higher colors, or the knot exterior. The relevant “promotion” step remained open even when the proposed endpoint theorem was correct.
* **A linear skein construction is not a diagram construction.** Projectors, subtraction, division by the loop value and signed sums are legitimate algebraic operations. Their realization by actual uncolored tangles is a separate question.

The early ledger contains exact family exclusions, not just negative impressions. Examples include one- and two-band recurrences, a classification of units in the two-strand skein algebra, fixed-template twist loci, restrictions on EKT band fusions, and explicit Jones collisions separating higher colors. The [small-results guide](SMALL_RESULTS.md) develops several of the reusable deductions; the ledger preserves the remaining statements and their individual proof paths.

## 2. Rational tangle equations and the missing second topological probe

**Main nodes:** LATE-41, RB-HOM3, RB-3PROBE, RB-ARITH. **Sources:** [audited framed proof](../archive/outputs/rational-tangle-uniqueness-audited-proof.txt), [audit](../archive/collab/audits/LATE-41-audit.md), [unframed extension](../archive/work/big_reductions/surgery.md).

Sikora's conjecture concerns uniqueness of a rational solution to two actual framed tangle equations. The candidate argument in this project passes to branched double covers, matches signed filling coefficients, uses Casson–Walker surgery and Floer-simple torsion, and concludes that the cover is a solid torus. The orientation and framing comparison is an essential step, not a removable convention.

The elementary part of the unframed extension is especially transparent: three homology-order measurements determine an integral peripheral linear functional up to sign. This leads, conditional on the audited surgery-rigidity argument, to two actual closure equalities plus one additional determinant equality. Two unframed closures alone are insufficient; the Ernst–Sumners example supplies the calibration.

**Where the Jones route stops:** polynomial equality supplies scalar information, but not the second actual lens-space filling. The paper cannot be used to replace “isotopic closures” by “closures with equal Jones polynomials.” The manuscript remains an internally audited candidate, with external review and priority unresolved.

## 3. Lemma Q, strong inversions and the November 3 global-design round

**Entry points:** [scaffold](../archive/collab/SCAFFOLD.md), [global routes](../archive/work/global_design/routes.md), [theory log, morning of November 3](../archive/collab/THEORY-width-ladder.md).

An actual unknot closure identifies the other tangle filling problem with surgery on a strongly invertible covering knot. “Flatness” means the relevant bracket coefficient vanishes, making a specified twist family Jones-unit. The project sought a theorem forcing a flat tangle with an unknot closure to be rational or nugatory.

Here is the scalar used in the later notes. In the fixed boundary basis write $[T]=y b+x c$, with loop value $\delta=-A^2-A^{-2}$. The actual unknot cap gives $u=y+\delta x$, a signed framing monomial. In the preferred longitude marking,

$$J=y/u=1-\delta x/u.$$

Thus $J=1$ is precisely flatness in this marking. A raw diagram must first undergo the common framing normalization in the [skein dictionary, Sections 2–3](../archive/work/theory_restart/skein_dictionary_arbitrary_boxes.md); one cannot normalize several closures independently and retain their vector relations. The saved quotient variable is $t=A^4$, so comparisons with an ordinary Jones convention must retain the dictionary's chirality rule.

Equivalent or closely related marked formulations used crossing-circle links, Sakuma links, Brunnian theta-curves, annular patterns and pants surfaces. These reformulations clarify the geometry but do not independently solve the realization problem. A necessary condition such as $a_2=0$, determinant one, or a finite-field fifth-root value is a gate, not a mechanism for producing or excluding every candidate.

The broader rational-tangle reformulation is due to [Sikora, arXiv v2 Theorem 24 / journal Theorem 9.2](REFERENCES.md#sikora24): the Jones unknot conjecture is equivalent to rational-tangle detection by the bracket. Lemma Q restricts that question to tangles with an actual unknot rational closure. A converse from this restricted Lemma Q alone to the full Jones conjecture is not established here.

The same day explored genus-two Jones representations, Burau pairings, two-twist subgroups, recurrence and AJ ideas, positivity, and finite-order approximations. Restricted orbit theorems survived; global claims did not follow from them. The [failure atlas](FAILURES.md) records the missing imports and the countermodels.

## 4. Designed counterexamples: four routes, no surviving candidate

**Period:** November 3 evening. **Main record:** [counterexample design section of the scaffold](../archive/collab/SCAFFOLD.md), [global-design proof notes](../archive/work/global_design/).

The target changed from proving detection to constructing a nontrivial knot with unit Jones polynomial. Designs were required to come with a reason and an exact decisive calculation.

| Design | Intended mechanism | Outcome and surviving question |
|---|---|---|
| Constant-sum twist templates | Make two twist variables invisible along a diagonal | The unchanged Kanenobu resolution mechanism cannot turn a nonunit seed into a unit. New turnback geometry would be required. |
| H2 fused EKT shell | Use two interacting sites to repair a Jones-trivial link into a knot | The determinant equation has no integer unit solutions. That entire marked family is excluded. |
| Sakuma pilot links | Pass (a_2) and fifth-root gates, then test exact unlink Jones value | Six specified pilots were rejected. The gates were necessary but weak. |
| Genus-two kernel / invariant tensor | Find a topologically nontrivial object in a unit skein fiber | Restricted orbit and signed-square results constrain the design; no actual kernel or counterexample was obtained. |
| EKT fusion and clasp variants | Retain link cancellation while changing component structure | Single-fusion defects and the signed-square corner identity excluded the proposed shells. General seam-changing operations remain a distinct problem. |

There is no “best surviving counterexample” from this round. The correct output is the list of exact exclusions and the residual realization conditions.

## 5. Categorification and the geography of cancellation

**Period:** November 15–16. **Entry points:** [bullet-sum proof](../archive/work/theory_restart/sum_functor_referee.md), [sutured-sequence audit](../archive/work/theory_restart/sutured_sequence_referee.md), [ladder countermodel](../archive/work/theory_restart/surgery_ladder_referee.md).

The invariant $N(T)$ is obtained from the Bar–Natan tangle complex by an augmentation that keeps one crossingless matching. Its graded Euler characteristic recovers the selected scalar information, while its graded dimensions expose cancellation hidden from that scalar. Compatible tangle sums tensor these augmented homologies. This gives genuine factor reductions.

The proposed geographic laws—TILT, OVERHANG, J-TILT, NP, END and a parallelogram bound—tried to force a nonzero Euler coefficient at an extreme grading. Several fitted large datasets. Later actual examples refuted the universal endpoint strategy, and longer special curves invalidated an over-narrow shape model.

There were also useful negative theorems. A bare opposite-parity pair fails the admissible matching condition arising from Daemi's plane-Floer sequence. A suitably shifted two-rung ladder, however, admits a natural higher differential cancelling its extra summands after every additive closure. Changing coefficients to characteristic zero does not eliminate the correctly signed formal ladder. Thus a successful categorical bridge must supply additional **geometric compatibility**, not just ranks, grading shifts or the existence of additive spectral sequences.

The identification of the sutured target and its gradings was corrected during the process. In particular, no general bound $\operatorname{rank}\widehat{HFK}\ge 2g+1$ is retained. These corrections are substantive and remain visible in the ledger.

Some mechanism-round notes were never given separate scaffold nodes. They belong in the record, with their different review levels preserved:

| Note | Exact surviving scope | Review state at the pause |
|---|---|---|
| [Extreme states](../archive/claude/theory-restart/mech2/states/REPORT.md), Theorems 2.3–2.4 | A suitable adequate extreme state away from the unit grading detects non-flatness; a one-sign half-diagram detects it unless the covering knot is the unknot. | Claude-side proof and [independent internal referee](../archive/claude/theory-restart/mech2/verify/positivity-proof.md), using the cited minimal-genus theorem for homogeneous diagrams. The first two criteria cover **71**, not 72, of the 138 table entries; the 72nd uses a third criterion. No separate Codex proof audit was found. |
| [Pointed link splitting](../archive/claude/theory-restart/mech2/colored/REPORT.md) | Proposed sequence from $N(T)$ to $\widetilde{Kh}(K_u)\otimes\widetilde{Kh}(K_l)$ and the resulting product rank bound. | **Partial referee only.** The [referee notes](../archive/claude/theory-restart/mech2/verify/splitting-proof.md) identify the extra chain-level marked-point equivariance required beyond [Batson–Seed](https://arxiv.org/abs/1303.6240); its proof step (5) was not completed. The adequate-double END/NP claim also remains unrefereed. |
| [Unit-arrow shape](../archive/claude/theory-restart/mech2/annular/REPORT.md), Section 2 | Over $\mathbb F_2$, the specified unit $D$-arrows and $P_2$-runs force each component **containing a bullet generator** to have the stated square or staircase shape. The corollary also assumes one arc and an odd bullet count. | [Internal referee with tail cases and scope repairs](../archive/claude/theory-restart/mech2/verify/shape-proof.md), using [KWZ, Theorem 4.4](https://arxiv.org/abs/2202.01460). This is not the withdrawn unrestricted shape law, nor a proof that every undeformed summand lifts separately. |

The annular report also gives a scoped negative argument for constructions that are additive and grading-shift equivariant on the tangle complex: such a package cannot by itself exclude the formal opposite-parity blocks. This leaves open extra geometric data or maps not determined by that additive object. For adequate doubles, ordinary Jones non-triviality already has a published source in [Stoimenow, Proposition 4.3](https://arxiv.org/abs/math/0606255); the proposed homological refinements must not be credited as the first detection result for that class.

## 6. Exact transfer systems: two-bridge, necklaces and arborescent boxes

**Period:** November 16–17. **Entry points:** [arbitrary-box skein dictionary](../archive/work/theory_restart/skein_dictionary_arbitrary_boxes.md), [necklace analysis](../archive/work/theory_restart/necklace_extremes_referee.md), [resonance and ideals](../archive/work/theory_restart/arborescent_resonance_divisor.md).

The two-bridge work replaced unsupported pictures by a marked two-dimensional representation and a closed degree-state calculation. Its scope is the specified side-preserving strong inversions; side-exchanging inversions were not silently included. The necklace formula then decomposed a more general marked assembly into two fusion channels, with one common normalization.

This produced restricted non-flatness theorems for horizontal Montesinos-type inversions and vertical arborescent constructions. Exact finite-state and Farkas certificates extended certain listed classes. These are infinite-family theorems within their hypotheses, but not a proof for all arborescent inversions. The list of allowed vectors, root slopes and eligible signatures is part of each statement.

**The knot-level consequence matters.** For a V3-class marked strong inversion with $a_2(K)=0$, the branch knots $L_n=T(1/n)$ have $V(L_n)\ne1$ for **every nonzero integer $n$**. V3 here means the stated vertical word with any integral part, non-integral rational boxes, odd vertical exponent $a$, and at least one box if $|a|\ge3$ or at least two if $a=\pm1$. Without $a_2(K)=0$, every nonzero even parameter is excluded, while at most one odd parameter can escape: it must satisfy $j=n a_2(K)$ in the fixed orientation convention. Non-flatness alone does not erase that exception. [Statement and short proof](SMALL_RESULTS.md#21-from-v3-non-flatness-to-knot-level-jones-detection); [V3 internal referee](../archive/collab/data/roundD/refV3_REPORT.md); [odd-closure repair](../archive/work/theory_restart/roots_odd_referee.md).

The saved **E6** example has $a=-3$, integral part $N=-2$, and box slopes $1/9,5/13,-4/13$. The internal record gives $a_2(K)=0$ and, for $n\ge1$, Jones span $n+28$ with both extreme coefficients of modulus two. These coefficients put those members outside the semi-adequate and Turaev-genus-one detection classes, and the span puts their crossing numbers above 24. The record also reports hyperbolicity of the covering knot $K$ and of $\Sigma_2(L_n)$ for $|n|\ge9$; small-slope numerical observations are not a theorem. This is an explicit infinite family illustrating the result, not a substitute for its uniform proof over all permitted boxes. [Parameters and saved polynomials](../archive/claude/theory-restart/mont/cx/roundD/lit/examples_E6.json); [construction code](../archive/claude/theory-restart/mont/cx/roundD/lit/bk.py); [internal geometry and literature report](../archive/collab/data/roundD/LIT_RESULT.md).

**Credit and verification boundary.** The V3 algebra, its marked skein dictionary and the odd-closure repair have internal proof/referee records; the E6 computations and literature comparison have not received external specialist review. The comparison is **PARTLY_KNOWN**, not an established priority claim: existing detection results include [semi-adequate links](https://arxiv.org/abs/math/0606255), [Turaev-genus-one links](https://arxiv.org/abs/1604.03501), and [the computational range through 24 crossings](https://arxiv.org/abs/2003.06724). The [Khovanov result of Hedden–Watson](https://arxiv.org/abs/0805.4423) is a categorified antecedent, not a Jones theorem. The literature report's unqualified sentence about **all** V3 closures is superseded by the $a_2=0$/odd-exception scope above. Neither the report's “no known theorem” wording nor its novelty verdict is an exhaustive literature certification.

An eventual obstruction to finite class lists led to a more structural invariant: the ideal generated by a box's two integral coordinates. Twists preserve it, and products cannot repair a proper ideal. Pairwise compatibility detects when a product of unimodular states remains unimodular. For the remainder, an exact resonance budget reduces each fixed body's horizontal unit search to at most two twist candidates.

**Where this route stops:** a primitive state can pass the scalar gates and still have the formal unit behavior. The missing theorem is geometric realization in this primitive fiber. A naive superadditive deficit was refuted by an explicit unimodular pair with deficits $4+4\to7$.

## 7. Finite-type theory, the osp symbol and cyclotomic comparison

**Entry points:** [integral finite-type audit](../archive/work/theory_restart/ft_integral_referee.md), [osp Casimir calculation](../archive/work/theory_restart/osp_casimir_exact.md), [third-moment audit](../archive/work/theory_restart/degree3_geometric_identity.md).

Expanding $J$ at $t=-1$ gives an equivariant finite-type series. The integral local model resolves singular-projector concerns, and its straight chord symbol agrees with an $\mathfrak{osp}(1|2)$ Casimir normalization. A separate cyclotomic argument compares the quotient invariant with a fifth-root evaluation of the covering knot's ordinary Jones polynomial.

These are structural results and useful necessary conditions. They are not nonvanishing theorems. Explicit commutator families have arbitrarily large first nonzero moment order while remaining non-flat. Consequently no fixed initial jet of this series can decide the whole problem. The order-three invariant also retains equivariant information not captured by the initially proposed combinations of classical knot invariants.

There is also a useful calibration of difficulty: for the standard summand-swapping inversion with summand $L$, the preferred identity is $J_{\mathrm{LP}}(t)=J_3(L;t^{-1})$, where $J_3$ is the spin-one colored Jones polynomial in the standard Jones variable. Consequently Lemma Q for these swap inversions contains the assertion that $J_3$ detects the unknot. The [dictionary, Section 8.1](../archive/work/theory_restart/skein_dictionary_arbitrary_boxes.md), supplies the marked swap-sphere argument; this is not an assertion that colored Jones detection is already proved. The [odd-closure audit, Section 5](../archive/work/theory_restart/roots_odd_referee.md), separately explains why Lemma Q for all strong inversions would imply ordinary Jones detection among unknotting-number-one knots.

## 8. Width two and certified construction searches

**Entry points:** [width-two root/marking note](../archive/work/theory_restart/width2_root_resonance_answer.md), [joint unit-line certificate](../archive/work/theory_restart/width2_unit_line_certificate.py), [theory log, X.27–X.34](../archive/collab/THEORY-width-ladder.md).

The nine-dimensional mixed braid module becomes a block endomorphism algebra after bending the boundary strands. Fusion rules explain its seven possible joint twist sectors and two absent sectors. This supports finite-window and line certificates for fixed double-twist templates.

A crucial correction was that joint cancellation need not come from either site acting scalarly on its boundary state. An actual diagonal unit line is stabilized by a joint cap/annulus mechanism. A search implementation had discarded precisely these constant lines, so its census had to be repaired. Covectors were also found not to be geometrically injective; mutation is a proposed explanation, not a completed classification.

The collaboration reports later audited unknot certificates for its recorded search queues. These are finite certified regions and specified all-parameter families. They do not establish emptiness for all width-two knots, all plats of a given crossing number, or an unrestricted higher-dimensional slice.

## 9. Cross-field theory and exact link complexity

**Period:** November 17. **Entry points:** [complexity scope](../archive/work/theory_restart/jt2_scope_audit.md), [uniform depth proof](../archive/work/theory_restart/depth_uniform_audit.md), [exact gadget algebra](../archive/work/theory_restart/jt2_difference_algebra.md).

A broad survey found that many attractive “bridges” were restatements, known twist-polynomial technology, or claims requiring extra realization input. The selected new target was JT₂, exact equality to the two-component unlink polynomial.

In particular, [Champanerkar–Kofman](REFERENCES.md#ck06) already supply the twist-bracket framework and its links to Mahler measure and resonant directions. The project's fixed-template algorithm must be read in that setting. Fixed-order jet computability belongs to the classical finite-type framework of [Bar-Natan](REFERENCES.md#barnatan95); the uniform-in-order constants below require the separate direct skein estimate. The conditional complexity observation linking a hypothetical Jones unknot detector to exact evaluation has a [Welsh antecedent recorded by Hass–Lagarias–Pippenger](REFERENCES.md#welsh93). These prior observations are not presented as new project results.

The banked restrictions are concrete:

* JT₂ is in $\mathrm C_{=}\mathrm P$, by a sum of squares of signed-count coefficient differences.
* Fixed Taylor jets can be computed in polynomial time. Under $\mathrm P\ne\mathrm{NP}$, a hardness reduction cannot keep all its nonzero output defects at uniformly bounded depth.
* A uniform analytic estimate gives an unconditional lower bound on depth for **integral value-preserving count encodings**. This is a narrower but quantitatively stronger statement than the conditional hardness restriction.
* One fixed twist template remains tractable even when twist exponents are written in binary.
* Formal differences multiply in the skein category, but that does not compile them into one actual two-component diagram. Bare smoothing carriers and the simplest serial projector construction meet exact obstructions.

The generic constant-braid and projector-carrier restrictions remain **TRUSTED**, with their independent referee workflow stopped at the pause. No exact clause-gadget construction or JT₂ hardness theorem has been obtained.

The wider survey also produced the following **unrefereed proposals**, retained as directions rather than promoted results:

| Source | Proposal and unresolved obligation |
|---|---|
| [Categorification lens](../archive/claude/theory-restart/bridge/L1_categorification.md) | Multicurve congruences and reverse constraints on Watson's invariant; a realization obstruction still needs additional geometric information. |
| [Quantum-representation lens](../archive/claude/theory-restart/bridge/L3_quantum_reps.md) | A BHMV curve-operator detection statement and its off-diagonal limitation; verify its exact surface, operator and positivity hypotheses. |
| [Arithmetic lens](../archive/claude/theory-restart/bridge/L4_arithmetic.md) | A Jones-specific Lehmer-gap proposal and related arithmetic statements; Mahler measure alone fails on known knots. |
| [Gauge-geometry lens](../archive/claude/theory-restart/bridge/L5_gauge_geometry.md) | Equivariant instanton and traceless-character-count proposals; the lens's erroneous Euler-characteristic barrier was withdrawn. |
| [Combinatorial lens](../archive/claude/theory-restart/bridge/L6_combinatorics.md) | An “Even Jones” conjecture for signed chord diagrams and a Z-equivalence formulation; finite chord checks do not prove either assertion. |
| [Physics lens](../archive/claude/theory-restart/bridge/L7_physics.md) | A branched-cover/genon interpretation at selected roots; source and normalization checks remain open. An identity at a root does not explain a double cyclotomic zero, nor establish that a proposed list of levels is exhaustive. |

For these notes read the [skeptical review](../archive/claude/theory-restart/bridge/STRESS.md), the [Codex map](../archive/work/theory_restart/cross_field_bridge_map.md), and the [final scope correction](../archive/collab/msgs/20261117-131440-codex.md) alongside the [survey synthesis](../archive/claude/theory-restart/bridge/THEORY-MAP.md). Those corrections take precedence over stronger headlines in the synthesis or the lens drafts. See [the bounded review queue](OPEN_PROBLEMS.md#o13-referee-one-cross-field-proposal-without-inheriting-its-headline).

## The current dependency picture

```mermaid
flowchart TD
  JC["Jones unknot conjecture: unresolved"]
  Q["Marked flat-tangle realization / Lemma Q"]
  R["Candidate rational-equation rigidity"]
  P["Missing actual topological probe"]
  C["Categorified realization restrictions"]
  A["Primitive arborescent unit fiber"]
  W["Width-two unit matrix coefficient"]
  L["JT₂ exact link complexity"]
  G["Actual exact gadget compiler"]
  R --> P
  P --> Q
  C --> Q
  A --> Q
  W --> Q
  Q -. "restricted detection route" .-> JC
  G --> L
  JC -. "split-union reduction from knot Jones-triviality" .-> L
```

Arrows name research dependencies or reductions, not equivalences unless the linked note proves one. The ledger is valuable precisely because it leaves these gaps visible.
