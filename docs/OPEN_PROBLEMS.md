# Open obligations and contribution packets

[Start here](START_HERE.md) · [Research map](RESEARCH_MAP.md) · [Failure atlas](FAILURES.md)

The research was paused on 17 November 2026. These are unresolved mathematical and verification obligations, **not running assignments or authorization to start archived searches**. The last selected research direction was JT₂ exact link complexity; other lanes were parked. A contributor can propose a bounded packet without reopening the whole program.

A useful contribution has a statement, exact conventions, dependency list, proof or certificate, scope limitations and a failure test. Returning “promising” numerical behavior is not a substitute for the missing statement.

## O1. Referee the generic constant-braid restriction

**Question.** On a fixed generic Temperley–Lieb braid module, does a subgroup preserving one common invariant code and acting there by scalar functions times constant matrices necessarily have finite projective image factoring its permutation image?

**Starting point:** [JT2 clause-gate note](../archive/work/theory_restart/jt2_clause_gate_scope.md), CONSTANT-BRAID and RATIONAL-HADAMARD.

**Present status:** written argument and first read; independent adversarial referee stopped before reporting. TRUSTED, not promoted.

**Bounded deliverable.** Check the eigenvalue specialization at $A=1$, possible singular code bases, a regular positive unitary specialization, and the diagonalizability step. For Hadamard, check the invariant-code lattice and valuation argument separately. Return a counterexample with all hypotheses satisfied, or a line-by-line proof audit with exact source statements.

**What would not resolve it:** an approximate universal gate result at one root of unity, or a parameter-dependent code/gate example outside the common-constant-code hypotheses.

## O2. Build one actual reusable exact product or clause gadget

**Question.** Can a polynomial-size marked tangle network isolate an all-variable product while retaining an open output state suitable for composition and exactly two final components?

**Starting point:** [difference/carrier note](../archive/work/theory_restart/jt2_difference_algebra.md), especially the mixed-corner criterion; [root restrictions](../archive/work/theory_restart/jt2_root_gates.md).

**Present status:** the elementary scalar interpolation works formally; bare smoothing, serial invertible TL₂ and the literal projector accumulator meet scoped obstructions. No actual compiler is known here.

**First deliverable.** Give one marked gadget with:
1. its actual endpoint matching and any closed components;
2. the complete open tensor in a fixed basis;
3. a common framing convention;
4. an exact reusable composition identity, including every proper-subset mixed term;
5. a proof of size and final component count.

It is legitimate to escape an obstruction by using extra boundary legs, parameter-dependent states or noninvertible operations. State the escape explicitly.

**Cheap falsifiers:** specialization at $A=1$ contradicts the asserted matching; a proper mixed corner survives; the output only has the desired value after a closure that destroys reusability; nonunit loop factors were removed as though they were framing units.

## O3. Establish the exact complexity status of JT₂

**Question.** Is equality to the two-component unlink's whole Jones polynomial coNP-hard or $\mathrm C_{=}\mathrm P$-hard under polynomial-time many-one reductions? Alternatively, is there a structural tractability theorem for a broader exact gadget class?

**Starting point:** [exact language and quantifier audit](../archive/work/theory_restart/jt2_scope_audit.md), [fixed-template theorem](../archive/work/theory_restart/fixed_twist_bridge_audit.md).

**Present status:** membership in $\mathrm C_{=}\mathrm P$ and several restrictions are recorded. A bounded literature search found no exact hardness theorem of the required kind; this is not a certification of novelty or open status.

**Bounded first packet.** Either identify a published theorem with exactly this target and reduction type, or state and prove a reduction for an explicitly defined intermediate exact tensor language. Preserve normalization and two-component connectivity.

**Failure tests:** approximate versus exact equality; Turing versus many-one reductions; fixed-root evaluation versus the entire Laurent polynomial; unrestricted links versus exactly two components; a fixed twist template hidden inside the encoding.

The quantitative depth bound applies to integral value-preserving count factorizations. A general zero-preserving reduction need not have that form. Conversely, fixed-depth hardness restrictions require the usual complexity-separation assumption.

## O4. Complete the manuscript-level audit of rational-solution uniqueness

**Question.** Does the candidate framed theorem, with the stated arbitrary tangle and balanced-framing hypotheses, follow from the cited surgery and Floer results exactly as written? Do the unframed extension and arithmetic corollaries retain those hypotheses?

**Starting point:** [audited proof](../archive/outputs/rational-tangle-uniqueness-audited-proof.txt), [prior audit](../archive/collab/audits/LATE-41-audit.md), [manuscript](../archive/work/paper/sikora-uniqueness/main.tex), [unframed note](../archive/work/big_reductions/surgery.md).

**Present status:** candidate proof with several internal audits; the later complete manuscript referee workflow did not return. External specialist review and priority remain unestablished.

**Divide the audit into independent obligations:**
- exact comparison with Sikora's conjecture and balanced-isotopy definitions;
- peripheral marking, deck involution, orientation and signed surgery coefficients;
- irreducibility, longitudinal versus nonlongitudinal branches, and every Rasmussen–Rasmussen hypothesis;
- Casson–Walker normalization and the alternating Alexander form;
- prior work, especially the method overlap with Gainullin and the known unknot-product special case.

A returned audit should cite the exact source version and proposition, not just the paper title. A discovery that a theorem is already known is valuable and should change the credit, not be concealed.

**Non-goal:** deriving Jones unknot detection by replacing actual closure equalities with polynomial equalities.

## O5. Identify a geometric structure that excludes the formal ladder

**Question.** What extra geometric compatibility distinguishes actual unknot-closure quotient tangles from the formal zero-Euler ladder?

**Starting point:** [ladder](../archive/work/theory_restart/surgery_ladder_referee.md), [signed integral version](../archive/work/theory_restart/characteristic_zero_ladder_referee.md), [Lipshitz–Sarkar map audit](../archive/work/theory_restart/lipshitz_sarkar_bridge_audit.md).

**Present status:** a named candidate input exists—the upstairs inversion action and axis-moving map—but no dictionary proving a realization obstruction has been completed. Bare equivariance, additive pairings and rank constraints are insufficient.

**First deliverable.** Identify whether the axis-moving map $f^+$ is a natural transformation of the relevant additive closure functors, with the precise marking and unreduced $\mathbb F_2$ conventions. If it needs additional coherence, state that extra structure and evaluate the formal ladder against it.

**Failure tests:** replacing a map cone by the direct sum of its two objects; identifying its target with $N(T)$ without proof; claiming non-additivity solely because a chosen matrix has off-diagonal entries; using universal endpoint visibility after the actual counterexample.

## O6. Decide the isolated-block extension question

**Question.** Does the particular compact Bar–Natan block used in the countermodel admit the required KWZ deformation/extension in isolation?

**Starting point:** [map audit](../archive/work/theory_restart/maps_report_referee.md), [unreduced shape audit](../archive/work/theory_restart/unreduced_shape_referee.md), [cross-field scope correction](../archive/work/theory_restart/lipshitz_sarkar_bridge_audit.md).

**Present status:** OPEN. A whole object having a deformation does not imply that each undeformed summand lifts separately; deformation maps may mix summands. Conversely, independently lifted summands do produce a lifted direct sum.

**Bounded deliverable.** Supply the isolated block, its gradings, coefficient ring, the exact deformation equations and a lift or obstruction. Keep a Bar–Natan compact component separate from a Khovanov special curve.

**Non-goal:** inferring actual tangle realization merely from the existence of a formal extension.

## O7. Control the primitive arborescent unit fiber

**Question.** Which geometrically realizable unimodular box states can exhaust the resonance budget and admit a unit closure?

**Starting point:** [integral ideal and resonance proof](../archive/work/theory_restart/arborescent_resonance_divisor.md), [pair compatibility and deficit counterexample](../archive/work/theory_restart/arborescent_pair_and_deficit.md), [marked dictionary](../archive/work/theory_restart/skein_dictionary_arbitrary_boxes.md).

**Present status:** proper ideals are permanent obstructions; each fixed nondegenerate body has at most two horizontal candidates. The general primitive remainder is open. Finite exact lists do not encompass all nested signatures.

**First deliverable.** Propose a quantity or geometric normal form preserved by the permitted operations and prove one induction step. It must allow the explicit $4+4\to7$ deficit loss and the known resonant examples. If the quantity is only defined on a restricted class, specify the class and show closure under the operations used.

**Failure tests:** replacing an ideal by its polynomial gcd; dropping radicals in the pair criterion; assuming two end-jet laws remain invariant under nesting; reporting a numerical floor without an induction theorem.

## O8. Classify unit lines in the marked width-two system

**Question.** Are the observed constant unit lines always explained by a geometric stabilizer, and what is the correct statement after allowing joint cap/annulus mechanisms and covector coincidences?

**Starting point:** [joint line referee](../archive/work/theory_restart/width2_unit_line_referee.md), [root-resonance scope](../archive/work/theory_restart/width2_root_resonance_answer.md), [certification report letter](../archive/collab/msgs/20261117-065336-claude.md).

**Present status:** finite regions and specified families were certified; a global necessity theorem is open. Individual-site scalarity and covector injectivity are false as proposed.

**Bounded deliverable.** An all-parameter proof for one new exact template, or a structural normal form that explains an entire class and explicitly includes the diagonal joint stabilizer.

**Failure tests:** treating a kernel of one scalar contraction as a representation kernel; identifying equal covectors with isotopic tangles; excluding constant lines in an implementation; calling a Jones/Alexander-unit output an unknot without a topological certificate.

## O9. Finish source-specific audits before making external claims

This is a set of independent tasks, not one generic “check the citations” request.

- **Carmi–Cohen:** verify that the explicit growing twist degree contradicts the exact uniform-control package asserted in the audited version; retain the distinction between failure of that proof and falsity of its main theorem. [Note](../archive/work/paper/carmi-cohen-obstruction/main.tex).
- **Bharathram–Birman–Brendle:** locate precisely which joint hypotheses in the audited preparation/parity/unequal-count package fail; do not claim that a conditional proposition or Burau₄ faithfulness itself has been refuted. [Scope note](../archive/work/global_design/bbb_parity_obstruction.md).
- **Grigsby–Wehrli grading observation:** independently reconstruct the saved cable and gradings before promoting the computation-dependent concern about a conjectural terminal grading. The ungraded theorem and unrelated gradings are not refuted. [Endpoint/referee scope](../archive/work/theory_restart/ce1_endpoint_referee.md).
- **Snape framing observation:** reproduce the particular marked link and preferred framing before attributing a discrepancy to an example rather than a convention. [Recorded report](../archive/collab/msgs/20261103-191856-claude.md).

A good result may be “our interpretation was wrong.” Corrections to this repository's own claim are as important as corrections to a source.

## O10. Make one evidence packet independently portable

**Question.** Can a new machine reproduce one positive result and one failed-route certificate using only the public package?

**Starting point:** [EF exact certificate](../archive/work/theory_restart/referee_checks/ef_depth.py), [endpoint certificate](../archive/work/theory_restart/referee_checks/endpoint_counterexample.py), and their linked proof notes.

**Present status:** some small certificates use only standard-library arithmetic; many historical computations depend on external environments, source trees or saved files. A historical successful run is not a portable environment guarantee.

**Deliverable.** A declared input, tool versions, exact command, expected output, independent invariant checks, and a certificate linked to the precise ledger claim. Report unavailable inputs rather than reconstructing them silently from an output polynomial. Work in a copy: historical scripts may write results beside themselves.

**Failure tests:** importing an unarchived private path; verifying only a cached output against itself; changing normalization to fit the expected result; treating checksum agreement as mathematical verification.

## O11. Complete one unfinished mechanism-round proof audit

These are different obligations; agreement with the saved numerical examples does not settle them.

* **Pointed link splitting.** Check step (5) of the proposed sequence $N(T)\Rightarrow\widetilde{Kh}(K_u)\otimes\widetilde{Kh}(K_l)$: the chain maps and homotopies for Reidemeister moves must preserve the marked-point subcomplex, not merely its ambient homology module. The [partial referee](../archive/claude/theory-restart/mech2/verify/splitting-proof.md) explains the gap between this requirement and [Batson–Seed's published construction](https://arxiv.org/abs/1303.6240). The [compute referee](../archive/claude/theory-restart/mech2/verify/splitting-compute.md) is corroborating data, not that missing proof.
* **One-sign and extreme-state criteria.** Independently audit the [states report](../archive/claude/theory-restart/mech2/states/REPORT.md) with its [existing internal referee](../archive/claude/theory-restart/mech2/verify/positivity-proof.md), including the imported homogeneous-diagram minimal-genus result. Preserve the 71-versus-72 count correction and the unknot exception. This already has a Claude-side internal proof/referee record; the task is not to silently label it externally verified.
* **Restricted shape.** Audit the repaired $\mathbb F_2$ unit-arrow theorem using [KWZ's extension theorem](https://arxiv.org/abs/2202.01460) and the [tail-case referee](../archive/claude/theory-restart/mech2/verify/shape-proof.md). Retain the bullet-containing-component condition and the two extra hypotheses of the staircase-plus-squares corollary. This does not settle O6 or recover the false universal shape law.

The adequate-double END/NP refinement remains an unrefereed proposal in the [colored report](../archive/claude/theory-restart/mech2/colored/REPORT.md). A proof must distinguish that homological refinement from the already published ordinary Jones detection for such doubles.

## O12. Make the V3 branch-knot consequence independently reviewable

**Target.** Audit the complete chain from a marked V3 word to $V(T(1/n))\ne1$ on the $a_2=0$ core, with its odd-parameter exception outside that core. [Readable corollary](SMALL_RESULTS.md#21-from-v3-non-flatness-to-knot-level-jones-detection).

**Present status.** V3 and the arbitrary-box dictionary have internal referee records; the surgery/signature translation is internally checked. E6's exact polynomial data and geometry/literature conclusions are reported separately. No external specialist review or comprehensive novelty determination is recorded.

**Bounded packet.** Check one of the following: the marked V3-to-cover identification; the common framing in the dictionary; the Casson/Mullins orientation comparison; or E6's saved halfword, $a_2=0$, two-channel polynomial and claimed geometric certificates. Start from the [V3 audit](../archive/collab/data/roundD/refV3_REPORT.md), [dictionary](../archive/work/theory_restart/skein_dictionary_arbitrary_boxes.md), [odd-closure audit](../archive/work/theory_restart/roots_odd_referee.md), and [E6 data](../archive/claude/theory-restart/mont/cx/roundD/lit/examples_E6.json).

**Failure tests.** Replacing non-flatness by an all-odd-closures conclusion without checking $j=n a_2$; proving a statement about the ordinary Jones polynomial of the covering knot $K$ instead of the branch knot $L_n$; calling a small-slope numerical hyperbolicity check a proof; confusing a reported literature search with established priority.

## O13. Referee one cross-field proposal without inheriting its headline

The explanatory proposals listed in [Research map, Section 9](RESEARCH_MAP.md#9-cross-field-theory-and-exact-link-complexity) remain **unrefereed**. Select one concrete identity or implication, pin its conventions and source theorem, and test it against the recorded countermodels before doing a broader survey.

Examples are the BHMV curve-operator statement, the branched-cover/genon evaluation, the “Even Jones”/Z-equivalence reformulation, or a specific arithmetic congruence for multicurves. For a root-of-unity identity, separate equality at the root from divisibility with multiplicity, and a finite set of verified levels from a classification of every level. For a categorified proposal, specify the extra geometric map that is not already determined by the additive complex.

Use the [skeptical review](../archive/claude/theory-restart/bridge/STRESS.md) and [final scope letter](../archive/collab/msgs/20261117-131440-codex.md) as corrections to the [survey synthesis](../archive/claude/theory-restart/bridge/THEORY-MAP.md). A useful outcome may be a known theorem, a counterexample, or a precise missing hypothesis. None of these directions is an active assignment or authorization to restart a search.

## Suggested handoff format

Each contribution can fit into a small packet:

| Field | Required content |
|---|---|
| Claim | A single precise statement or exact question |
| Scope | Category, coefficients, markings, normalization and input model |
| Dependencies | Ledger IDs, proof files and exact external statements |
| Method | Proof, exact computation, or counterexample construction |
| Evidence | Reproducible files and expected outputs where applicable |
| Verdict | Proved within the packet, conditional, refuted, or unresolved |
| Limits | What the result does not establish |
| Next obligation | One concrete missing step, if any |

This makes work distributable across people and machines without equating repeated agreement with independent proof.

