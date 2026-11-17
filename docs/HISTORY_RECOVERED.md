# Recovered research history and status corrections

[Start here](START_HERE.md) · [Research map](RESEARCH_MAP.md) · [Failure atlas](FAILURES.md) · [Human work and corrections](HUMAN_WORK_AND_CORRECTIONS.md)

This guide preserves research content recovered in Claude's 17 November 2026 completeness handoff: findings whose fuller evidence lay outside the original shared folders, one-off checks recorded only in letters, unfinished reviews, and corrections to stale summaries. It is a publication extraction, not a new research pass. No mathematical computation was rerun to prepare it.

Two provenance labels are used throughout:

* **CONTEMPORANEOUS** means a file, letter, saved tool input or workflow result was written at the time. A recovered file can have this label even if its bytes were extracted later.
* **RECONSTRUCTION** means a later identification or summary was assembled from the surviving history. It must not be mistaken for a preserved original certificate.

“Referee,” “PROVED,” “SOUND,” and “STANDS_WITH_REPAIRS” below retain the collaboration's internal meanings. All those referees were AI agents; none of those labels establishes external specialist review or priority. Original reports can contain later-corrected claims. Read their corrections before using them as premises.

## 1. Source-specific audit recovered from the November 3 package

### H1. Bharathram–Birman–Brendle: what the internal audit actually claims

**CONTEMPORANEOUS; internal AI audit, no external specialist review.** The recovered package concerns the argument in arXiv:2607.05283v2. Its conclusion is that there **appears to be a gap in the proof**, not that the asserted faithfulness theorem is false. The project does not claim to have produced a generic Burau kernel element or resolved Burau₄ faithfulness.

The fuller [note](../archive/handoff/copied/jones-adversarial-pass/bbb-gap-note/note/bbb-gap-note.tex), [earlier shared audit](../archive/claude/g2-proof/BBB-GAP.md), and [version-specific public discussion](HUMAN_WORK_AND_CORRECTIONS.md) preserve the following distinctions:

1. Under the paper's parity condition, the internal note identifies the coefficient absolute sum of the Moody polynomial with $|M(-1)|$. It then argues that this specialization depends only on the corresponding Burau matrix at $t=-1$.
2. The proposed incompatibility is between that specialization and the combined reduction/count package, not a direct disproof of every separately conditional lemma. For the explicit braid below, either the asserted proper-product reduction fails or the subsequent conclusions fail. The proper-product Conditions 1 and 2 were not checked directly from the enormous arc picture.
3. The explicit braid is

   $$\Phi_0=[(\sigma_1\sigma_2)^6,[[A_{14},A_{24}],A_{34}]].$$

   The note records a nontrivial Brunnian four-braid whose unreduced Burau matrix is the identity at $t=-1$, both in $B_4$ and after stabilization in $B_5$, but not at $t=2$ and not generically. Its recorded $(t+1)$-adic depth is one. Membership in the **specialized** kernel is not membership in the generic Burau kernel.
4. The internal localization is conditional: if the original loop has the claimed parity and the subsequent asserted properties are available, the modified loop cannot retain everything needed for the final inequality. The audit did not verify the internal case analyses of Lemmas 6.3–6.6 or the modified loop's asserted property 2. It credits an earlier AI-generated review on pith.science for noticing the missing parity recheck; the explicit specialization argument is separate.
5. The note also challenges the unrestricted inference “pseudo-Anosov implies the image of the chosen arc meets the other arc,” while preserving the stronger Brunnian hypothesis under which the relevant conclusion is available. This observation is not a general counterexample to the paper's main theorem.
6. The depth of $[\Phi_0,\sigma_3\Phi_0\sigma_3^{-1}]$ depends on the representation convention: two for the unreduced matrices, three for the reduced matrices. The first four recorded iterated depths are $2,4,6,8$ unreduced and $3,4,6,8$ reduced. A statement giving only one convention was corrected in the third internal review.
7. A separate supporting braid $S=\Gamma_1^{-1}[\Delta_3^4,A_{34}]\Gamma_1$ has a recorded 33,320 intersections and $M_S(-1)=0$. It is not Brunnian and was not shown to be a proper product. It cannot replace the missing proper-product construction.

The final package has three internal review rounds and a later diff audit. The [50-check script](../archive/handoff/copied/jones-adversarial-pass/bbb-gap-note/phi0_check.py), [saved output](../archive/handoff/copied/jones-adversarial-pass/bbb-gap-note/phi0_check.out), and [review record](../archive/handoff/copied/jones-adversarial-pass/bbb-gap-note/check/final4-review-results.md) are evidence of those checks, not proof that every geometric hypothesis was verified. No correspondence draft is part of this history guide.

### H2. The explicit Gamma construction remained undecided

**CONTEMPORANEOUS.** This was a different task from the algebraic audit. Its goal was to construct the paper's loop modification and check the relevant geometry directly. It ended **UNDECIDED**, not as a positive or negative test of the whole package.

The recovered [work report](../archive/handoff/recovered/scratchpad-7610ac96/bbb-attack/REPORT.md) records that the construction reproduced the paper's Section 7 example, but became too large on the intended input. The arc for $\Phi_0$ had recorded intersection number 976,672. A proper-product conjugate using $m=31$ had whole-matrix Burau coefficient absolute sum about $1.55\times10^{11}$, far above the chosen explicit-arc limit. A prior sizing check quoted about $1.6$ million and $42$ million for selected matrix entries and smaller conjugations; those are **different measurements**, not conflicting versions of the same count.

The Figure 7.4 exponent discrepancy was recorded separately: two displayed exponents shifted by two relative to the traced figure, without changing $|M(-1)|=20$. It was not offered as the main obstruction. See the [contemporaneous result letter](../archive/collab/msgs/20261103-174515-claude.md).

Two recovered scripts, [example validation](../archive/handoff/recovered/scratchpad-7610ac96/bbb-attack/scripts/validate_section7.py) and [size/facts extraction](../archive/handoff/recovered/scratchpad-7610ac96/bbb-attack/scripts/size_and_facts.py), depend on missing or not-exactly-recovered arc code and traces. They preserve the method; their presence does not make the computation portable. The trace and JSON outputs were not recovered.

### H3. Two “Theorem A” labels, and the limits of the adversarial pass

**CONTEMPORANEOUS.** A separate November 3 adversarial pass checked that $|N(\zeta_8)|$ was an odd integer on 3,000 sampled words. This supported the genus-two **G2-ORTH** statement about spin-$3/2$ lines. Its [peer-check script](../archive/handoff/copied/jones-adversarial-pass/work/peer-checks/thmA.py) is a finite check, not the proof of the unrestricted result.

The $Z_\rho$ sub-lane also called a result “Theorem A”: it concerned the finite information visible through certain quotients, truncations and roots of unity, recorded under **G2-FINITE**. These are different statements. Use their stable node names and the [genus-two lane report](../archive/claude/g2-proof/REPORT.md), rather than joining them by their local theorem letters.

The adversarial pass's strategic assessment counted 34 morning outputs and judged that they did not narrow the main target. This is an internal assessment of research progress, not an additional proof audit of every statement. Its fuller [workflow outputs](../archive/handoff/copied/jones-adversarial-pass/workflow-results.json) should be read with the later board corrections.

## 2. Recovered files are not the same as reconstructed computations

**CONTEMPORANEOUS originals; later extraction.** Five files could be recovered exactly from saved tool inputs under the handoff's “one creation, no later modification” rule. Their source-time bytes are recorded in the [recovery manifest](../archive/handoff/recovered/RECOVERED.md); export normalization is a separate manifest event. Recovery did not rerun them.

* The [first specialized Burau check](../archive/handoff/recovered/scratchpad-7610ac96/burau/phi0.py) was written at 15:19 on November 3. The history's identification of the later [shared certificate](../archive/claude/g2-proof/bbb-gap/phi0_check.py) as the “recheck of record” is **RECONSTRUCTION**; the two scripts themselves are contemporaneous and distinct. This repairs the ledger's earlier “scratchpad location not given” pointer.
* The [rational-tangle bracket check](../archive/handoff/recovered/scratchpad-7610ac96/scripts/bracket_check.py), written during the LATE-41 audit, checks the $\langle1/3\rangle+\langle-1/3\rangle$ example discussed in the [Sikora source-specific audit](HUMAN_WORK_AND_CORRECTIONS.md). It was initially described as lost. Its script text is now recovered; this publication pass did not rerun it or alter its review status.
* The other three exact recoveries are the Gamma work report and two scripts described in H2. Missing dependencies remain missing.

The **U5-FROB5** sieve has a different provenance. The November 3 [letter](../archive/collab/msgs/20261103-102245-claude.md) reports that the pilot family $C(2,-4n,2,2n)$ passes the $\mathbb F_{16}$ condition $V=1$ modulo $\Phi_5$ exactly when $5\mid n$, and that 94 of 574 tested two-bridge knots passed. Those are **CONTEMPORANEOUS reported data**. The script was patched after creation; obtaining its final state from the transcript would require **RECONSTRUCTION**, so it was not included among the exact recoveries. The later six Sakuma pilot certifications rejected the tested $n=5,10,15$ cases and do not depend on treating this sieve as a complete invariant. [Later result](../archive/collab/msgs/20261103-191856-claude.md).

## 3. One-off checks whose evidence is a letter or scratchpad

The following checks were independent reads or calculations during the collaboration. They were not all saved as standalone reproducible certificates.

| Item | Statement and exact scope | Provenance and evidence |
|---|---|---|
| Diagonal unit line | The halfword `s.l1.l1.x2.x1.x1^(2m).y3^(2m).x1.u2.u2` gave $J=1$ for $m=0,1,2,3$; its two single-site directions gave the same nonunit of span nine. The finite check refuted the old census and one-site-scalar implication. The all-parameter theorem needs the separate geometric proof. | **CONTEMPORANEOUS**, [letter](../archive/collab/msgs/20261117-021320-claude.md) and [saved input list](../archive/handoff/copied/scratchpad-7610ac96/codex_family.txt); the one-off output was not saved. |
| ARB-IDEAL residue | The recorded reduction $(a,c,d)=(0,5,0)$ modulo $(7,t-2)$ witnesses a proper coordinate ideal. The ideal proof uses unimodular twist matrices, bilinearity of star product and integral linear closure functionals. | **CONTEMPORANEOUS**, [letter](../archive/collab/msgs/20261117-080352-claude.md). No separate script for this read. Follow the primary proof's choice of state; a residue check is not a replacement for it. |
| Repeat gate | The recorded value for $B(XY)$ is $a(\omega)a(\omega^2)=7$, failing the repeat gate. The criterion uses $(a,b)=(a,dc)=(a,d)$ under the unimodular-state hypothesis. | **CONTEMPORANEOUS**, [letter](../archive/collab/msgs/20261117-085616-claude.md). No separate script for this read. |
| Deficit counterexample | For $v=Y^{-2}XYe_1$ and $w=Y^2X^{-1}Y^{-1}e_1$, the exact window $-12\le m\le12$ gives individual minima four at $m=0$, while the product has $A=1$ and minimum seven at $m=-4$. The full minimum justification is the separate two-candidate theorem. | **CONTEMPORANEOUS**, [letter](../archive/collab/msgs/20261117-085616-claude.md); [complete displayed proof](../archive/work/theory_restart/arborescent_pair_and_deficit.md). Direct superadditivity is refuted; an interaction correction is open. |
| EF-DEPTH | Claude reproduced the recurrence arithmetic and $V_{K_r}(e^h)=1+96\,2^{r-1}h^4+O(h^5)$. That read did **not** compare the printed seed and framing against Eliahou–Fromentin; the separate source audit did. | **CONTEMPORANEOUS**, [letter](../archive/collab/msgs/20261117-131643-claude.md), [source audit](../archive/work/theory_restart/eliahou_fromentin_bridge_audit.md). |
| Uniform jet bound | Claude checked the descending skein estimate, the radius $R=1/(16n)$ and the Cauchy bound $2(16n)^r$. The conclusion concerns Jones Taylor depth at $t=1$, **not** clasper depth or vanishing of every finite-type invariant. | **CONTEMPORANEOUS**, [letter](../archive/collab/msgs/20261117-124955-claude.md), [proof](../archive/work/theory_restart/depth_uniform_audit.md). |

The copied [scratchpad](../archive/handoff/copied/scratchpad-7610ac96/) also preserves `check.py` (defect-module examples), `tb_check.py` (two-bridge normalization), `family.py` (the two-channel family), `ft_local.py`, `ft_deep_copy.py`, `osp_casimir_copy.py` and their saved outputs, and the `t1.py`–`t6.py`/`u14.py` certifier checks. These are **CONTEMPORANEOUS files**, not new proofs. The `closure_check.py` and `closure_check2.py` scripts check the marked two-closure algebra. Their use of $N(T)$ for a numerator closure must not be confused with the later homology object bearing the same symbol.

## 4. Mathematical status corrections that summaries had missed

### H4. V2, the delta-law and the sigma-law did receive an internal referee

**CONTEMPORANEOUS.** The early engine-A summary called them unrefereed. The later [V3 referee](../archive/collab/data/roundD/refV3_REPORT.md) re-derived the following as ingredients of V3:

* For a non-integral rational box, $\delta=\operatorname{span}b-\operatorname{span}a=-1$; these span differences add under star product.
* The four paired end types give $\sigma=s_{1,\mathrm{top}}+s_{1,\mathrm{bottom}}=0$, also additive, with the specified leading-coefficient signs.
* For the vertical closure at odd $|a|\ge3$, the pole requires $\sigma_*=-1$. This excludes a simultaneous second-order tie at both ends for a rational body product. The referee also checks the weak-end mismatch and the two-candidate Lemma W.

Thus the **vertical** V2 clause and these lemmas have internal proof/referee status. The extra **horizontal** clause under the V2 name was not separately refereed there; do not silently transfer the verdict. [Original engine-A report](../archive/collab/data/engineA/REPORT.md).

### H5. The full rational-box TYPE LAW remains checked, not proved

**CONTEMPORANEOUS.** This classification appeared only in [Claude's lane notes](../archive/claude/theory-restart/mont/notes-claude.md) and [its checker](../archive/claude/theory-restart/mont/types.py). For a rational box with amplitudes $a,b$, put

$$D_+=\operatorname{top}(a)-\operatorname{top}(b),\qquad D_-=\operatorname{bot}(a)-\operatorname{bot}(b),$$

and let $s_+$ and $s_-$ be the products of the corresponding leading and trailing coefficients. The reported possibilities are an integral monomial case or

$$P_k=(1+3k,3k,-1,+1),\qquad N_k=(3k,3k-1,+1,-1),\quad k\in\mathbb Z.$$

The record checks all 11,606 reduced non-integral words of length at most eight. It does **not** prove this full four-parameter classification. The conditional two-ended noncancellation argument based on it remains conditional as written, even though the later Q-MONT theorem reaches its intended class by a separate proof. Likewise the proved delta-law is one consequence, not proof of the whole TYPE LAW. Nested boxes give additional end shapes, so the rational hypothesis cannot be dropped. The reported 40,000-necklace and 60,000-depth checks are data only.

### H6. CYC10's arithmetic corollaries have no completed Claude read

**CONTEMPORANEOUS records; absence reported by the handoff.** MOMENT-CYC10-COROLLARIES stays **TRUSTED** on Codex's [written derivation](../archive/collab/msgs/20261116-235320-codex.md), not “independently read by both systems.” The derivation uses $(z-1)^3\Phi_5(z)\mid V_K(z)-1$ and the stated relations $b_3=-6v_3$, $j_4=b_4-9v_3$ to obtain the mod-five gates.

The [IDENT report](../archive/claude/theory-restart/mont/ft/ident/REPORT.md) had obtained those gates conditionally on integrality of its auxiliary quantities. Claude's [earlier summary](../archive/collab/msgs/20261116-234631-claude.md) repeated the consequence without a written derivation. No later Claude letter supplies the pending read. Neither a missing audit nor repeated agreement is an independent proof.

### H7. Carmi–Cohen and the gauge lens: stale text is not current status

**CONTEMPORANEOUS.** Three later files repeated “unverified” for Carmi–Cohen despite the earlier internal obstruction: the round-D literature report, the theory-log extract, and the paused JT2 literature notes. The correct scope is the [version-specific proof-package obstruction](HUMAN_WORK_AND_CORRECTIONS.md), with the explicit trefoil-host twist recurrence in the [note](../archive/work/paper/carmi-cohen-obstruction/main.tex). It concerns the uniform-control step, not a counterexample to the paper's main statement or the Jones unknot conjecture. The complete manuscript referee workflow produced no findings; earlier internal checks do not fill that missing manuscript audit.

The [gauge lens](../archive/claude/theory-restart/bridge/L5_gauge_geometry.md) also retained the erroneous formula $\chi(I^\natural(K))=\sigma(K)/2$. The unknot already refutes it: its instanton group has Euler characteristic $\pm1$, whereas its signature is zero. The resulting universal gauge “barrier” was **withdrawn**. This corrects the project's attempted attribution and use of instanton theory; it is not a criticism of the cited researchers' theorem. [Correction](../archive/collab/msgs/20261117-124730-codex.md), [acceptance](../archive/collab/msgs/20261117-124955-claude.md), and [Kronheimer–Mrowka reference](REFERENCES.md#km11).

### H8. V3 branch-knot scope and novelty language

**CONTEMPORANEOUS.** The [round-D report](../archive/collab/data/roundD/LIT_RESULT.md) overstated the all-parameter branch-knot conclusion. The corrected result is [Small result 21](SMALL_RESULTS.md#21-from-v3-non-flatness-to-knot-level-jones-detection): all $n\ne0$ on the $a_2(K)=0$ core; otherwise all nonzero even $n$ and all but at most one odd $n$, with $j=n a_2(K)$ in the fixed convention.

Its E6 example distinguishes three objects: the covering knot $K$, the branch knot $L_n$, and the three-manifold $\Sigma_2(L_n)$. The hyperbolic example statements about $K$ are not automatically statements that every $L_n$ is a hyperbolic knot. The recorded rigorous hyperbolic-filling range is $|n|\ge9$. The polynomial extreme-coefficient and span statements are separate.

The literature verdict was **PARTLY_KNOWN**, produced by an internal AI search. Phrases such as “the new part is real” or “no published theorem reaches these knots” in chronological letters are not established priority claims. The [research map](RESEARCH_MAP.md#6-exact-transfer-systems-two-bridge-necklaces-and-arborescent-boxes) states the overlap with existing semi-adequate, Turaev-genus-one, finite-crossing and categorified results.

## 5. Other superseded headlines

All entries in this table are **CONTEMPORANEOUS**, already corrected by later board entries or letters. They remain useful because a reader can otherwise encounter the earlier headline first.

| Earlier headline | Current scope and evidence |
|---|---|
| No congruence, evaluation or finite-type method can prove the target | The surviving barrier excludes one fixed two-power reduction or one uniformly bounded jet alone. It is not a prohibition on every fixed modulus or every arithmetic argument. [Failure atlas](FAILURES.md). |
| H2 is Floer-thin | Rank equal to determinant was checked at four parameters; equality of these ranks does not prove thinness. The family was excluded by its determinant equation. [Original letter](../archive/collab/msgs/20261103-181201-claude.md), [later scope](../archive/collab/SCAFFOLD.md). |
| TILT, OVERHANG, END, NP, J-TILT and PARALLELOGRAM are universal laws | Actual examples refuted the universal endpoint strategy; the previous successful tables remain finite data. [Endpoint certificate and referee](../archive/work/theory_restart/ce1_endpoint_referee.md). |
| Unit lines occur only in coordinate directions | The diagonal joint-stabilizer example refutes it. The implementation had discarded constant grouped lines. [Correction](../archive/collab/msgs/20261117-021320-claude.md). |
| The span-13 near miss saturates exactly the forced divisor | It carries an additional $\Phi_6$ factor; the saturation sentence was withdrawn. [Correction](../archive/collab/msgs/20261117-021320-claude.md). |
| The final census is 131,578 unit lines and every coincidence is explained by mutation | The later recorded census has 145,842 line entries and 2,537 planes. Certification concerns that census. Mutation as the covector explanation and a global necessity theorem for unit lines remain open. [Final scope](../archive/collab/SCAFFOLD.md), [certification report](../archive/collab/msgs/20261117-075611-claude.md). |
| N-INF forbids every finite end-jet automaton | It forbids a finite **exact signature list**. It does not forbid finite control with unbounded registers or a coarser finite invariant. [Scope record](../archive/collab/SCAFFOLD.md). |
| Round G tested about 8.57 million bodies and 24.5 million candidate events | The displayed corrected subtotals are 10,464,750 listed body occurrences and 16,534,689 candidate events. The earlier count mixed orbit representatives with bodies; the 24.5-million headline has no supporting reconciliation. These are occurrences/events, not automatically distinct isotopy classes. [Report](../archive/collab/data/roundG/fc_REPORT.md), [08:59 correction](../archive/collab/SCAFFOLD.md). |

## 6. Interrupted work and evidence integrity

### H9. The shared-process and duplicate-worker incidents

**CONTEMPORANEOUS events.** At about 04:33 on November 17, a broad process-pattern stop intended for one audit killed workers belonging to other round-D tasks. At about 04:37–04:42, a coordination message in the then-used workflow runtime resumed duplicate agent instances rather than reaching the existing instances; duplicate instances acted on shared folders and stopped further jobs. These are failures of that recorded process, not universal claims about every agent system.

The final integrity records identify the consequences:

* `J4` and the `R(6)` probe were rerun and completed.
* `d2fix2`, the proposed uniform two-depth-two-box/top-300 task, was **not rerun and is not claimed**. The morning sentence “every affected run was redone” is false.
* The original refGen instance based its final verdict on post-incident runs, checked code timestamps, and per-task saved outputs. The duplicate's `rg_robust` and `rg_sigcert` results are incomplete second opinions, not completed certification runs.
* M300's 955 certificates and the distinct D36 result have their own exact re-verification. Round E also corrected D36's earlier floating-point feasibility verdict by producing 56,556 exact certificates. None of this proves the abandoned `d2fix2` statement.

Sources: [audit's incident account](../archive/claude/theory-restart/mont/cx/cert/audit2.md), [lpgen coordination record](../archive/claude/theory-restart/mont/cx/roundD/lpgen/NOTE-from-integrator.md), [refGen coordination record](../archive/claude/theory-restart/mont/cx/roundD/refGen/NOTE-from-integrator.md), [refGen integrity note](../archive/collab/data/roundD/refGen_NOTES.md), [lpgen final scope](../archive/collab/data/roundD/lpgen_REPORT.md), and [round-E exact audit](../archive/collab/data/roundE/refM300_REPORT.md).

**RECONSTRUCTION: lessons extracted from those events.** Keep worker ownership explicit; avoid broad process-pattern termination on a shared machine; determine whether a message reaches an existing worker or creates another; save findings and task-level completion evidence continuously; distinguish missing tasks from successful negative results. The record also motivates a cross-review after a batch: on November 3, several false route claims had passed their first route-specific reviews before the cross-review corrected them. These lessons are not new mathematics or instructions to execute historical workflows.

### H10. Reviews that never returned

**CONTEMPORANEOUS lifecycle records.** A launched referee is not a completed referee. The following limits matter to the mathematical status:

| Workflow | What survives; what does not |
|---|---|
| November 3 Sikora and Carmi–Cohen manuscript referees | Both stopped on the usage limit with **zero findings** and were never rerun. Earlier proof audits and the manuscript drafts survive, but not a referee report on either complete manuscript. [Pause/restart record](../archive/collab/msgs/20261115-170313-claude.md). |
| November 3 eight-route batch | The Habiro builder never returned because of its output limit. Its route was not built. Other builders and referees did return; their journal extraction is listed below. |
| November 15 mechanism panel | Only the sum lane returned a completed workflow result at that pause; the sum/maps reports existed and were then unrefereed. Their later Codex audits are separate events. Five other lenses were not completed at that stage. [Pause record](../archive/collab/msgs/20261115-200103-claude.md). |
| November 16 lens verification | All seven referees stopped at the usage limit; completed sections survive. Some contain finished scoped proofs, others leave explicit steps unchecked. The [mechanism review table](RESEARCH_MAP.md#5-categorification-and-the-geography-of-cancellation) distinguishes them. [Contemporaneous scope letter](../archive/collab/msgs/20261116-120708-claude.md). |
| November 17 JT2 construction and CONSTANT-BRAID/PROJECTOR-COST referee | Stopped at the pause. The [literature](../archive/claude/theory-restart/bridge/jt2/lit/NOTES.md), [construction A](../archive/claude/theory-restart/bridge/jt2/gadgetA/NOTES.md) and [construction B](../archive/claude/theory-restart/bridge/jt2/gadgetB/NOTES.md) notes are partial. No completed independent referee result or hardness construction was banked. [Pause letter](../archive/collab/msgs/20261117-133905-claude.md). |
| November 17 ledger extraction | The early extraction stopped before complete assembly. Its parts survive, but have stale statuses addressed in this guide. They are not a self-contained final ledger. |

Completed Montesinos/necklace and CYC10 workflows are not included among these failures: their result files and referee records exist. Their repaired hypotheses, rather than their workflow completion alone, determine the scope of the statements.

## 7. Results recovered from workflow journals

These are **CONTEMPORANEOUS agent outputs, extracted later**, with formatting and privacy normalization recorded in the handoff manifest. The journals themselves were runtime state and are not published. A preserved result is not automatically a valid result: the files retain the status asserted at the time, and later corrections take precedence.

| Recovered result | What the file adds beyond the short board entry |
|---|---|
| [November 3 eight routes](../archive/handoff/journal_results/wf_2f8f87e8-37a_2026-11-03_eight-routes.md) | Seven route builds, their hostile internal reviews and synthesis; the Habiro builder is missing. It preserves failed mechanisms and the reasons for rejection, not eight completed theorems. |
| [November 2 cycle-2 audit](../archive/handoff/journal_results/wf_6f2d5e26-ef1_2026-11-02_cycle2-audit-and-file-triage.md) | Cable and scalar-sum algebra checks, literature and file-triage results. Three agents did not return. |
| [November 2 remaining literature tracks](../archive/handoff/journal_results/wf_07ca9c49-f82_2026-11-02_lit-sweep-remaining-tracks.md) | KWZ, cosmetic-surgery and satellite-defect readings. The missing ideas track is not an implied conclusion. |
| [November 3 Lemma-Q literature sweep](../archive/handoff/journal_results/wf_81ef8d26-c51_2026-11-03_lemma-q-literature-sweep.md) | Five source readings behind the EKT/Sakuma/band discussions; the synthesizer never returned. |
| [Rigid-case analysis](../archive/handoff/journal_results/wf_899747e8-62c_2026-11-03_rigid-case.md) | The longer proposed crossing formulas and the obstruction to an all-crossings bracket argument behind T-RIGID-FORMULA. Suggested next lemmas in that result are proposals, not proved steps. |
| [November 3 source-audit referees](../archive/handoff/journal_results/wf_a51c709e-886_2026-11-03_bbb-gap-hostile-referees.md) | The three internal verdicts behind the initial source-audit summary. H1–H2 and the later note govern the current scope. |
| [Genus-two lane referees](../archive/handoff/journal_results/wf_d0b0a3e6-177_2026-11-03_g2-lane-referee-verdicts.md) | Fuller Heegaard/kernel-build reviews behind the lane report's items 9–11. Local theorem names must be matched to their actual statements. |
| [Width-two window certificate referee](../archive/handoff/journal_results/wf_c6df0491-3d8_2026-11-17_width2-window-R2-certificates.md) | The second referee's certificate-replay result, previously represented on disk mainly by scripts and a log. It is a check of the specified templates, not a general width-two classification. |

## 8. Completeness boundary

This guide extracts the research/status content of the handoff's history inventory and later assembler corrections. It omits private publication instructions, draft correspondence and personal runtime context. Those are not mathematical evidence. The original source artifacts, their availability or exclusion reasons, and normalization events belong in the release manifest.

Claude's completeness statement was bounded: no further **known** history-only result or failure remained after comparison with its surviving log, files and correspondence. It was not a claim that every conversation token, missing output or unsaved intermediate experiment had been recovered. Earlier context compactions and missing scratchpad outputs are real limits. Exact recovery, reconstruction, a recorded successful run, a checked proof, and external review remain five different evidence levels.
