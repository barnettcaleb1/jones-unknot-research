# Failure atlas

[Start here](START_HERE.md) · [Research map](RESEARCH_MAP.md) · [Small results](SMALL_RESULTS.md) · [Open problems](OPEN_PROBLEMS.md)

A failed direction is useful only if the failed statement, evidence, surviving scope and possible repair are distinguishable. The entries below select recurring mechanisms. The [full dead-end ledger](../archive/collab/DEAD_ENDS.md) and [early result ledger](../archive/outputs/claude-handoff/RESULT_LEDGER.json) retain additional failures, individual candidates and their exact provenance.

**Important distinction:** an actual knot refutes a knot-level claim; a formal skein vector refutes only an inference based on the properties that vector satisfies. A finite experiment can refute a universal conjecture with one certified example, but a run with no examples does not prove the universal conjecture.

## F01. “One actual unknot closure determines the entire twist family”

**Failure.** The anchored skein recurrence retains a second smoothing channel. Knowing the initial closure is an unknot does not make that channel equal to the unlink channel. Exact anchored families can start at the unknot and have nonunit Jones polynomials after twisting.

**What survives.** A fixed two-channel recurrence gives an exact flat/nonflat dichotomy and finite certificates for its parameter locus. It does not determine which initial channel values occur geometrically.

**Possible repair.** Supply an independent geometric or skein identity for the second channel, with the same marking and normalization. [Early ledger, EARLY-02](../archive/work/handoff/early-ledger.txt); [full uniform twist obstruction](../archive/outputs/jones-uniform-band-twist-obstruction.txt).

## F02. “A fixed real Jones value is a positive norm”

**Failure.** An explicit sequence of nontrivial ribbon knots has $V(1)=V(-1)=1$ and, for every other fixed nonzero real parameter, eventually negative Jones value tending to minus infinity.

**What survives.** Unitary or reflection-positive constructions with different observables may still be useful. The obstruction is to identifying the normalized ordinary scalar itself with a universally nonnegative quantity at one such parameter.

**Possible repair.** Name a new positive observable and prove that ordinary Jones equality determines its extremal value. Changing the normalization without proving this implication does not repair the route. [Exact family and proof](../archive/outputs/jones-real-positivity-obstruction.txt).

## F03. “The unknot's plat amplitude saturates Cauchy–Schwarz”

**Failure.** The plat normalization includes a quantum-dimension factor. For a $2m$-strand plat the unknot value corresponds to an interior overlap when $m>1$, not a unit overlap. Saturation instead corresponds to the appropriate unlink value.

**What survives.** The positive TQFT endpoint is legitimate on its own hypotheses.

**Possible repair.** Derive a different positive-defect identity genuinely forced to vanish by $V_K=1$. Density of quantum braid images does not supply that equality case. [Normalization and source comparison](../archive/work/global_design/crossfield_physics.md).

## F04. “Finite roots, initial jets or formal color constraints force exact triviality”

**Failure.** Actual nontrivial knots can evade specified finite probes; later marked two-bridge commutators give arbitrarily deep initial vanishing of $J$ at minus one. Formal higher-color sequences also satisfy extensive algebraic packages while retaining invisible higher information.

**What survives.** Particular finite tests exclude particular classes, and bounds depending on geometric complexity are not refuted.

**Possible repair.** A global nonvanishing mechanism, a proved complexity-dependent cutoff, or a knot-specific realization theorem. Merely adding another fixed number of moments is not a class-free repair. [Early ledger, EARLY-05/19/24](../archive/work/handoff/early-ledger.txt); [formal color countermodel](../archive/work/global_design/colored_propagation.md); [finite-depth discussion](../archive/work/theory_restart/ft_nonvanishing_referee.md).

## F05. “Two actual unframed closure equalities force a rational tangle”

**Failure.** The recorded Ernst–Sumners calibration has a nonrational tangle and a rational tangle with two matching actual closures. Their determinant functionals are $|6p-q|$ and $|4p+q|$; their squared difference is $20p(p-q)$.

**What survives.** A third determinant separates this ambiguity. Under the candidate surgery-rigidity argument, it yields the three-probe theorem. A distance divisibility test can sometimes eliminate the alternative already at two probes.

**Possible repair.** Keep the third probe or the explicit arithmetic condition; do not assert a general two-probe unframed theorem. [Calibration, proof and prior-work references](../archive/work/big_reductions/surgery.md).

## F06. “A link banding to the unknot has unknotted components”

**Failure.** The two zero-framed parallels of a trefoil bound an annulus. Cutting the annulus along a spanning band gives a disk, so the banded link is the unknot although its components are knotted. The split-link hypothesis in the attempted band-sum theorem import was missing.

**What survives.** Results with a split starting link retain their hypotheses. The example does not have a claimed unlink Jones polynomial.

**Possible repair.** Prove a separate component restriction using the full Jones hypothesis, or restrict the geometry to a split-link situation. [Exact correction and source](../archive/work/global_design/ekt_unknot_components_gate.md).

## F07. “Changing Kanenobu's seed determinant repairs its unit line”

**Failure.** In the unchanged unlink-resolution mechanism the family has
$V_{p,q}=1+(V_{\mathrm{seed}}-1)A^{8(p+q)}$.
A nonunit seed cannot become unit by choosing parameters. Determinant one is insufficient.

**What survives.** The general two-site constant-sum problem is not excluded.

**Possible repair.** Change the actual marked turnback data and prove the new full unit equation. [Design gate](../archive/work/global_design/c1_candidate_gate.md).

## F08. “The H2 fused EKT family contains a determinant-one candidate”

**Failure.** Its exact determinant is $|13+26m-18n-88mn|$. The equations for either unit sign factor into products $588$ or $764$, with one factor required to be $70$ modulo $88$. No signed divisor satisfies that condition.

**What survives.** The corner formula is valid and this family passes a weaker coloring test. The rejection is the sharper integral obstruction.

**Possible repair.** A different marked template with a different determinant polynomial. More parameters from the same family cannot help. [Recorded full verdict](../archive/collab/msgs/20261103-181201-claude.md).

## F09. “The parity/unequal-count package establishes Burau₄ faithfulness”

**Failure.** In the audited version of Bharathram–Birman–Brendle, parity implies $|M(-1)|$ equals the intersection count. A specified nontrivial Brunnian braid acts trivially under Burau at $t=-1$, so two parity-satisfying configurations related by it cannot have unequal counts. The combined preparation/parity/unequal-count package is incompatible with that input.

**What survives.** This does **not** refute Burau₄ faithfulness, prove a kernel, or isolate a counterexample to a conditional proposition whose antecedents were not constructed. Equal counts can still accompany different exponent multisets.

**Possible repair.** A corrected preparation theorem or an argument using exponent information beyond the count. [Version-specific proof and exact scope](../archive/work/global_design/bbb_parity_obstruction.md); [Bharathram–Birman–Brendle v2](https://arxiv.org/html/2607.05283v2).

## F10. “All quotient-tangle extrema are Euler-visible”

**Failure.** An actual symmetric half-diagram gives a quotient tangle with an unknot closure and top quantum generators at $(h,q)=(4,8),(5,8)$. Their Euler contributions cancel. Its $J$ is nonunit, so this is a counterexample to the proposed mechanism, not to Lemma Q. The compatible sum with its mirror cancels at both ends.

**What survives.** Conditional implications from endpoint visibility and the tensor-product theorem remain valid. The original large datasets remain observations, superseded as evidence for a universal law.

**Possible repair.** A genuinely restricted class theorem or information beyond endpoint support. Weakening “both ends” to “at least one end” does not repair the universal statement. [Actual example and replay](../archive/work/theory_restart/ce1_endpoint_referee.md).

## F11. “Every special curve is short; every component is a unit square”

**Failure.** Longer special curves and larger rectangles occur beyond the initial tables, including the recorded torus-knot controls. Some earlier shape laws quantified only over unit arrows; that restricted hypothesis must not be dropped.

**What survives.** The intrinsic augmented count and tensor law do not require every special to have the same length. A theorem specifically about unit-arrow components is a different statement.

**Possible repair.** Work with the full curve types or prove the unit-arrow hypothesis on a named class. [Shape audit](../archive/work/theory_restart/unreduced_shape_referee.md); [later correction record](../archive/collab/msgs/20261116-120708-claude.md).

## F12. “Replacement maps or additive collapse sequences exclude every invisible summand”

**Failure.** Central actions on the specified special summands are null-homotopic, so shifts alone do not violate the replacement-map relations. A correctly graded formal ladder has identity-block higher differentials cancelling its extra pieces naturally at every additive closure.

**What survives.** A bare two-row defect is excluded by the plane-Floer matching constraint. The ladder is a formal object, not a constructed tangle.

**Possible repair.** Specify an actual geometric map package whose compatibility fails on the ladder. Another rank bound or an abstract additive functor is not enough. [Map audit](../archive/work/theory_restart/maps_report_referee.md); [ladder](../archive/work/theory_restart/surgery_ladder_referee.md); [characteristic-zero control](../archive/work/theory_restart/characteristic_zero_ladder_referee.md).

## F13. “The noncompact arc is determined by the two numerical labels k,j”

**Failure.** The second inversion of $9_{46}$ has the same proposed numerical labels as a standard class but a different quantum character. Agreement at one and agreement of a count do not determine the graded polynomial.

**What survives.** The count identities surviving that test remain separate from a classification of arc shapes.

**Possible repair.** Add a defined intrinsic invariant and prove that it contains the missing information. Do not infer the arc is trivial from $k=j=0$ alone. [Read and explicit polynomial difference](../archive/work/theory_restart/arc_law_read.md).

## F14. “Finite-index pattern symmetry must be rational gluing”

**Failure and repair.** The initial statement omitted an outer normalizer coset. The explicit matrix
$E=\left(\begin{smallmatrix}\delta&1\\-1&-\delta\end{smallmatrix}\right)$
normalizes the projective modular group and is not in it.

The repaired algebraic theorem includes that coset; an additional actual-diagram constraint excludes it for the specified pattern tensors. Even the repaired conclusion classifies the tensor, not the geometry of its realizing pattern. [Corrected theorem and referee amendments](../archive/work/theory_restart/finite_index_pattern_rigidity.md).

## F15. “A joint constant twist line means one site is individually scalar”

**Failure.** A marked width-two example is constant along the diagonal $(1,-1)$ even though neither individual site is scalar on the relevant boundary states and either site alone is nonflat. A joint cap/annulus stabilizer explains the cancellation.

A search implementation had skipped exactly the one-slope groups representing constant lines. Its initial “only coordinate lines” census was false and was recomputed.

**What survives.** The seven-sector calculation and fixed-template algebra remain valid. Recorded families later received geometric or group certificates.

**Possible repair.** Classify joint geometric stabilizers, including annulus mechanisms. Do not assume geometric covector injectivity either: actual covector coincidences were found. [Unit-line referee](../archive/work/theory_restart/width2_unit_line_referee.md); [certification and census record](../archive/collab/msgs/20261117-065336-claude.md).

## F16. “Finite lists of end jets finish all arborescent boxes”

**Failure.** The recorded N-INF family produces infinitely many distinct leading coefficients through resonance. A finite list of exact signatures cannot encompass the general class. A proposed positive potential also failed on nested examples.

**What survives.** Exact automata and Farkas certificates for their specified rational or listed signature classes remain useful. Finite tests did not prove an all-depth theorem.

**Possible repair.** An inductive invariant retaining the relevant two-ended resonance and integral data. The coordinate ideal is one surviving necessary invariant, not the whole solution. [Round E theorem and limits](../archive/collab/msgs/20261117-072948-claude.md); [resonance note](../archive/work/theory_restart/arborescent_resonance_divisor.md).

## F17. “The best span deficit is superadditive under star product”

**Failure.** Two actual rational states are unimodular, each with minimum horizontal span four, while their unimodular product has minimum span seven: $4+4\to7$. The loss is an interaction effect, not discarded scalar content.

**What survives.** The two-candidate rule and pair-ideal criterion remain exact.

**Possible repair.** An invariant with an explicit interaction correction, or a genuinely different quantity whose transformation under nesting is proved. [Displayed states and complete hand calculation](../archive/work/theory_restart/arborescent_pair_and_deficit.md).

## F18. “Modular closeness is perturbative depth”

**Failure.** The published Eliahou–Fromentin knots satisfy increasingly strong coefficientwise congruences but always have Taylor order exactly four at one.

**What survives.** The uniform Jones-jet bound is consistent because their displayed diagrams grow exponentially. No primality or minimal crossing number is inferred.

**Possible repair.** A construction that separately proves increasing Taylor order with polynomial size. [Source-checked calculation](../archive/work/theory_restart/eliahou_fromentin_bridge_audit.md).

## F19. “A formal product of differences is already one exact link gadget”

**Failure.** Multilinearity realizes the product as a signed sum of diagrams. An actual background-plus-product gate must also kill every nonempty proper mixed corner. Bare actual smoothing defects cannot do this. Serial two-state carriers fail at arity three; the simplest projector accumulator instead creates at least one component per input.

**Status:** the exact-gadget restrictions were TRUSTED, with independent referees stopped at the pause.

**Possible repair.** A larger-boundary, parameter-dependent or noninvertible compiler, with a marked open tensor, its reusable composition law, polynomial size and exactly two final components. Matching scalar closures alone is insufficient. [Proof and scopes](../archive/work/theory_restart/jt2_difference_algebra.md).

## F20. “Generic constant braid gates automatically give universal exact computation”

**Failure under specified hypotheses.** On one common invariant code with constant projective matrices in one basis, pure-braid specialization and regular unitarity force a finite projective group factoring the permutation group. A rational Hadamard restriction has a separate valuation obstruction.

**Status:** TRUSTED; formal independent referee unfinished.

**What survives.** Parameter-dependent gates, noninvertible tangles, projection, larger interfaces and general scalar zero tests are not excluded.

**Possible repair.** Identify exactly which hypothesis the construction escapes and prove its exact tensor identity. Approximate root-of-unity universality is not an exact generic compiler. [Full note](../archive/work/theory_restart/jt2_clause_gate_scope.md).

## Corrections to other researchers' work require a separate standard

This atlas includes both our own failures and version-specific audits of external work; those must not be conflated.

For example, the Carmi–Cohen note gives an explicit twist recurrence whose Jones–Vassiliev degree grows beyond the claimed uniform residual cap. Its conclusion is that the audited proof package does not establish the main theorem as written. It is **not** a counterexample to that main theorem or to the Jones unknot conjecture. See the [manuscript](../archive/work/paper/carmi-cohen-obstruction/main.tex), [portable recurrence check](../archive/outputs/verify_twist_obstruction.py), and the source-version record in [LATE-03/04](../archive/work/handoff/late-ledger.txt).

Other external-paper observations—including the Sikora proposition issue, the Snape framing discrepancy and the proposed grading obstruction concerning Grigsby–Wehrli—have different levels of verification and different dependencies. Their dedicated records must accompany any public claim. In particular, a computation-dependent grading observation requiring a separate cable reconstruction must not be described as an externally established refutation.

## How to revive a route

A useful revival names the exact failed hypothesis it replaces and gives new information not already satisfied by its counterexample. Examples are a new geometric compatibility map, an explicit tangle realizing a formal tensor, or a restriction to a class excluding the actual endpoint counterexample. Renaming the target, changing the number of sampled examples, or citing a stronger-looking invariant without a proved bridge does not revive a route.

