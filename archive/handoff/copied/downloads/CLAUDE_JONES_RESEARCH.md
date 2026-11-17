# Historical Jones and knot-theory source inventory — public edition

> **Provenance and status (17 November 2026):** This is an edited historical inventory from a separate AI assistant thread's 2 November 2026 crawl, later handed to Claude. It is **not Claude-authored original research**, an independently checked bibliography, or current specialist review. Source summaries, reported inspections, versions and classifications below are preserved as historical assertions and may be incomplete or wrong. The public ledger's current references, corrections and claim-status pages supersede them. No literature verification or new mathematical computation was performed in preparing this edition.
>
> Raw operating instructions and private context have been removed with explicit markers. All 56 source records and 25 inherited paper records remain. Proposed tasks and next checks are historical recommendations, not instructions executed for this release. Only this inventory file was recovered from its former bundle; references to companion JSONL, source, PDF or replay files describe that historical bundle and do not assert that those artifacts are included here.

## 0. Start here: scope, provenance and evidence boundary

**Target question:** for a classical one-component knot K in S³, with the ordinary Jones polynomial normalized by V_U(t)=1, does V_K(t)=1 imply that K is the unknot?

This inventory records the **2 November 2026 crawl**, not a fresh literature search or a validation of its claims. It retains **all 56 source records S001–S056**, the **25 inherited paper records P001–P025**, and historical proposed follow-up actions. Source inspection statements, publication dates, titles, numerical totals and version claims below are inherited from that crawl. They have **not been rechecked for this public edition**. Recommendations remain unperformed in this editorial pass.

The 56 records include historical literature, proof attempts, research-process archives, code, datasets, indexes, aliases and uncertain leads. They are **not 56 independent results**. The 25 paper records are **not a complete knot-theory bibliography**; some known manuscripts or association leads remain only in source records. A site's source type and classification confidence describe publishing function, not mathematical correctness or novelty. AI involvement is separately recorded; many relevant historical or computational sources are not known to be AI-assisted.

The inherited catalogue has 12 P0 sources, 14 P1 sources, 24 P2 sources and 6 P3 sources. P0 means directly relevant to the current project, not correct or independently verified. P1 means strong supporting material; P2 means adjacent/backfill; P3 means duplicate, uncertain or audit-only.

**Historical bundle:** the received document described original crawl files in `original_crawl/`, JSONL exports with 29 source fields and 14 paper fields, and `_handoff` metadata. Those companion files were not recovered with this Markdown inventory. Empty inherited fields mean “not recorded,” not “none exists.” Local P001–P025 IDs are navigation keys; canonical DOI/arXiv keys remain the intended deduplication keys.

**Catalogue limitation:** the earlier crawl did not recover its cumulative catalogue or authoritative taxonomy. The functional classifications below are therefore provisional. [Redacted: private catalogue location and operational merge instructions.]

**Source availability:** this public edition contains the historical inventory text. It does not bundle the old project-audit PDF or replay package, third-party papers, repository trees, formal developments, raw logs, model weights or hard-unknot datasets. URLs and local paths below are historical locators, not guarantees of availability.

[Redacted: instructions for processing the incoming handoff.]

## 1. Removed operating instructions

[Redacted: raw operating prompt for a receiving AI instance. The source records, historical task proposals and evidentiary limitations are retained below.]

## 2. Inventory map

The following thematic groups cover each of the 56 source records exactly once. These are navigation groups, not new taxonomy assignments.

| Group | Records | Count | Focus |
|---|---|---:|---|
| G01 | S001, S002, S003, S004, S005, S006 | 6 | Direct Jones proof/search programmes and current audit |
| G02 | S007, S008, S009, S010 | 4 | Braid representations and closed-four-braid routes |
| G03 | S011, S012, S013, S014, S015, S053, S054, S055 | 8 | Established boundaries, structural classes and stronger invariants |
| G04 | S016, S017, S018, S019, S020, S021, S022, S023 | 8 | Computational certificates, reinforcement learning and datasets |
| G05 | S024, S025, S026, S027, S028, S029, S039, S040, S041, S042, S043 | 11 | Exact computation, tables, quantum/colored algorithms and uncertain tools |
| G06 | S030, S031, S032, S033, S034, S035, S036, S037, S056 | 9 | Adjacent knot-geometry, formal, volume and slice-ribbon research |
| G07 | S038, S044, S045, S046, S049, S051, S052 | 7 | Indexes, bibliographies, mirrors and announcements |
| G08 | S047, S048, S050 | 3 | Broader AI/topology research and follow-up manuscripts |

### Complete priority index

| ID | Priority | Function | Title |
|---|---|---|---|
| [S001](#s001) | P0 | research_process_archive | ProofAtlas: Jones Unknot Conjecture |
| [S002](#s002) | P0 | original_results | Learning Topological Invariance |
| [S003](#s003) | P0 | original_results | The Unknotting Number, Hard Unknot Diagrams, and Reinforcement Learning |
| [S004](#s004) | P0 | problem_incubator | Samaritan Jones-unknot open-problem contract |
| [S005](#s005) | P0 | original_results | On trivial Jones--Vassiliev polynomials |
| [S006](#s006) | P0 | research_process_archive | User audit: concrete obstruction to Carmi–Cohen proof |
| [S008](#s008) | P0 | original_results | A kernel of a braid group representation yields a knot with trivial knot polynomials |
| [S009](#s009) | P0 | original_results | The Burau representation of the braid group is faithful for n = 4 |
| [S011](#s011) | P0 | original_results | Verification of the Jones unknot conjecture up to 24 crossings |
| [S014](#s014) | P0 | original_results | On the modular Jones polynomial |
| [S024](#s024) | P0 | research_infrastructure | Regina Link engine documentation |
| [S025](#s025) | P0 | research_infrastructure | SnapPy / Spherogram documentation |
| [S007](#s007) | P1 | original_results | Does the Jones polynomial detect the unknot? |
| [S010](#s010) | P1 | original_results | Closed 4-braids and the Jones unknot conjecture |
| [S012](#s012) | P1 | original_results | Khovanov homology is an unknot-detector |
| [S013](#s013) | P1 | original_results | The Jones polynomial of an almost alternating link |
| [S016](#s016) | P1 | original_results | Machine learning methods and unknotting numbers: repository |
| [S017](#s017) | P1 | original_results | Unknotting numbers via Tait graphs |
| [S018](#s018) | P1 | original_results | RL unknotter, hard unknots and unknotting number |
| [S019](#s019) | P1 | research_infrastructure | untangling-number |
| [S020](#s020) | P1 | research_process_archive | RL unknotter notebooks |
| [S021](#s021) | P1 | research_infrastructure | Unknotting upper-bounds workflow |
| [S022](#s022) | P1 | original_results | Computations of the slice genus and the unknotting number of links via machine learning |
| [S023](#s023) | P1 | original_results | slice-genus-unknotting-rl: v1.0-preprint release |
| [S026](#s026) | P1 | research_index | KnotInfo |
| [S030](#s030) | P1 | original_results | Certified upper bound for the distortion of the trefoil knot |
| [S015](#s015) | P2 | research_index | From knots to four-manifolds |
| [S027](#s027) | P2 | research_infrastructure | ParallelJones |
| [S028](#s028) | P2 | research_infrastructure | Quantinuum Jones-polynomial quantum algorithms |
| [S031](#s031) | P2 | original_results | Gluons and Knots |
| [S032](#s032) | P2 | formal_mathematics | Gluon-knot Lean development |
| [S033](#s033) | P2 | original_results | Rogers–Ramanujan identities from the geometry of X^a=Y^b |
| [S034](#s034) | P2 | research_process_archive | ProofAtlas volume conjecture: boundary states |
| [S035](#s035) | P2 | research_process_archive | ProofAtlas volume conjecture: root-regular transport |
| [S036](#s036) | P2 | research_process_archive | ProofAtlas slice-ribbon: R-link / trisection |
| [S037](#s037) | P2 | research_process_archive | ProofAtlas slice-ribbon: Morse concordance |
| [S039](#s039) | P2 | research_infrastructure | Colored Jones from walks: repository lead |
| [S040](#s040) | P2 | research_infrastructure | Yui knot-homology engine lead |
| [S044](#s044) | P2 | problem_incubator | MathDB AJ conjecture page |
| [S045](#s045) | P2 | problem_incubator | MathDB complexified volume conjecture page |
| [S046](#s046) | P2 | research_index | Awesome AI for Math index |
| [S047](#s047) | P2 | original_results | Advancing mathematics by guiding human intuition with AI |
| [S048](#s048) | P2 | original_results | Variational autoencoders understand knot topology |
| [S049](#s049) | P2 | research_index | Fabian Ruehle publication list |
| [S050](#s050) | P2 | original_results | Learning Topological Features of Z-hat Invariants |
| [S051](#s051) | P2 | mixed_other | University of Sydney braid seminar announcement |
| [S053](#s053) | P2 | original_results | Invariants for Turaev genus one links |
| [S054](#s054) | P2 | original_results | Khovanov homology of the 2-cable detects the unknot |
| [S055](#s055) | P2 | original_results | On the Colored Jones Polynomial, Sutured Floer homology, and Knot Floer homology |
| [S056](#s056) | P2 | original_results | Trefoil distortion lower-bound Zenodo lead |
| [S029](#s029) | P3 | mirror_or_duplicate | CQCL Jones repository alias |
| [S038](#s038) | P3 | mirror_or_duplicate | Hugging Face page for Learning Topological Invariance |
| [S041](#s041) | P3 | mixed_other | QLF knot formalization lead |
| [S042](#s042) | P3 | mixed_other | topoKEMP lead |
| [S043](#s043) | P3 | mixed_other | Mini representation / Lie theory repository lead |
| [S052](#s052) | P3 | mixed_other | George Washington Jones hypothesis speculative talk |

## 3. Historical proposed cross-source work queue

Every task below was **proposed**, not completed in the earlier reformat or in this public-edition pass. These records preserve how the project planned follow-up work; they are not active workflow instructions. Source-specific proposed checks also appear in the full records.

### T001 · P0 · Independent geometric replay of the current twist obstruction

**Sources:** S005, S006, S024, S025

**Action:** Create signed PD/braid encodings for selected odd L including 1, 3 and 23; independently derive the smoothing link and compute Jones polynomials; check every hypothesis of the audited compression statement.

**Expected output:** A diagram manifest with exact encodings and checksums, two-backend normalization table where genuinely independent, and a hypothesis-by-hypothesis geometric audit.

**Boundary:** Do not use the recurrence as both definition and independent validation of the diagram; no claim about a counterexample to the conjecture follows.

### T002 · P0 · Current-version and correction audit of the general proof claim

**Sources:** S005, S006

**Action:** Read the primary version history and locate dated specialist responses or corrections; compare affected Section 5 statements.

**Expected output:** A versioned claim/dependency and correction ledger with primary links and unresolved questions.

**Boundary:** The included Codex-assisted audit is not external specialist review; absence of a located response is not proof that none exists.

### T003 · P0 · ProofAtlas underlying-archive and reduction audit

**Sources:** S001

**Action:** Retrieve original retained investigations rather than only the public route map; inspect embedded topology, residual strata, rigid-kernel and smoothing-link steps.

**Expected output:** An explicit dependency graph separating proved restricted lemmas, computational checks, missing global reductions and failed routes.

**Boundary:** Do not treat self-reported line counts or agent reviews as validation or completeness.

### T004 · P0 · Hard-unknot controls and counterexample acceptance harness

**Sources:** S003, S004, S024, S025

**Action:** Fetch a small pinned hard-unknot sample; build exact-polynomial and independent-nontriviality gates with explicit error/completion states.

**Expected output:** A reproducible regression corpus and decision log separating valid input, exact V=1, nontriviality proof, simplification certificate and unresolved cases.

**Boundary:** A failed simplifier is not a positive nontriviality label. Do not assume randomized/approximate geometry is a rigorous certificate.

### T005 · P0 · Braid-route validity and literature audit

**Sources:** S007, S008, S009, S010

**Action:** Extract Ito’s exact directional theorem, audit current four-strand faithfulness claims, and record realizability conditions for candidate polynomial data.

**Expected output:** A strategy memo with precise implications, current primary versions and explicit unsupported converses.

**Boundary:** Representation faithfulness is not trace injectivity or Jones detection; a compatible polynomial need not be realized by a knot.

### T006 · P0 · Independent exact-invariant convention tests

**Sources:** S024, S025, S011, S014

**Action:** Pin implementations and test variable scaling, chirality, writhe normalization, component count, cancellation/error signals and modular traps.

**Expected output:** Versioned exact coefficient-vector tests for an unknot, both trefoil chiralities, audit-family examples and modular adversarial cases.

**Boundary:** Distinct wrappers around the same implementation are not independent checks; modular or sampled numeric agreement is not exact equality.

### T007 · P1 · Direct AI braid-search reproduction

**Sources:** S002, S038, S049

**Action:** Locate primary code and data associated with the paper; reproduce a bounded pilot with the exact acceptance harness.

**Expected output:** Environment and source manifest, candidate-generation parameters, complete outcome logs and per-candidate certification status.

**Boundary:** A negative finite search does not prove detection; do not infer authorship of cited generic tools.

### T008 · P1 · Replay the October 2026 link-invariant release

**Sources:** S022, S023

**Action:** Retrieve the exact tagged release, verify checksums and replay selected band paths; record link and invariant definitions and lower-bound inputs.

**Expected output:** Artifact manifest, execution log and claim-to-certificate table with pinned versions.

**Boundary:** The companion paper and code are one research programme, not independent confirmations; link genus/unknotting bounds are not Jones detection.

### T009 · P1 · Corrected certificate and KnotInfo baseline audit

**Sources:** S016, S017, S026

**Action:** Inspect errata, establish dated baseline tables, and replay representative lower/upper-bound certificates.

**Expected output:** A corrected-value table separating newly claimed values, already-official values, conditional statements and minimal-diagram results.

**Boundary:** Source-reported totals must not be treated as independently reproduced totals or new Jones results.

### T010 · P1 · Reusable legal-move and RL workflow audit

**Sources:** S018, S019, S020, S021

**Action:** Inventory external inputs and models, then replay successful move sequences and inspect polynomial-export conventions.

**Expected output:** A dependency manifest and a collection of independently replayed legal paths with exact input/output encodings.

**Boundary:** Exhausted searches do not prove lower bounds; mirror/shift matching for lookup is not a normalization certificate.

### T011 · P1 · Established theorem boundary extraction

**Sources:** S011, S012, S013, S014, S015, S053, S054, S055

**Action:** Read exact statements and hypotheses in the primary literature; identify which structural classes can be excluded and which stronger invariants certify nontriviality.

**Expected output:** A lemma table with quantifiers, coefficient fields, diagram/class restrictions, citations and permissible uses.

**Boundary:** Do not replace categorified invariants by Jones polynomials or extend finite/special-class theorems without proof.

### T012 · P2 · Formal artifacts and version-transition audit

**Sources:** S031, S032, S033, S041

**Action:** Obtain pinned formal artifacts, inspect exact theorem statements and admitted assumptions, and compare recorded versions.

**Expected output:** A theorem-to-informal-claim mapping, axiom report, compilation log if run and correction history.

**Boundary:** Preserve the reported S032 Hypothesis R and S033 v2 changes while independently checking them; compilation is not novelty assessment.

### T013 · P2 · Explicit knot-geometry certificate audit

**Sources:** S030, S056

**Action:** Verify source-package and Zenodo metadata; inspect polygon knot type and distortion certificate mechanisms separately.

**Expected output:** Creator/version/DOI records only when verified, input hashes, verifier logs and an exact scope statement.

**Boundary:** Shared construction inputs limit independence; trefoil-distortion bounds are not a Jones theorem.

### T014 · P2 · Infrastructure and uncertain-lead triage

**Sources:** S027, S028, S029, S039, S040, S041, S042, S043

**Action:** Check repository identity, definitions, arithmetic, assumptions, paper associations and claims; classify unsafe or irrelevant leads without deleting them.

**Expected output:** A tool capability/limitation matrix and retained alias/irrelevance flags.

**Boundary:** Do not use approximate quantum evaluations, heuristic recognition or unreviewed Lean names as exact certification.

### T015 · P2 · Adjacent research and author-bibliography backfill

**Sources:** S034, S035, S036, S037, S044, S045, S046, S047, S048, S049, S050, S051, S052

**Action:** Follow primary outbound papers, off-arXiv manuscripts, author pages, corrections and data releases; keep adjacent topics separate from direct Jones claims.

**Expected output:** Dated additional source/paper records with credited authors, association evidence, exact scope and pending bibliography gaps.

**Boundary:** An index entry, seminar announcement, paper mirror or common author is a discovery lead, not theorem validation.

### T016 · P2 · Recover catalogue and finish uncompleted watch-source coverage

**Sources:** Original COVERAGE.md; persistent catalogue recovery

**Action:** Recover the latest persistent catalogue and authoritative taxonomy before merging; revisit failed or incomplete owner/site scans described in COVERAGE.md.

**Expected output:** A non-destructive merge plan, version-protected catalogue updates only when access succeeds, and a coverage ledger for remaining sources.

**Boundary:** This handoff is not the original cumulative catalogue. Never replace an inaccessible catalogue with these 56 records or treat an incomplete negative search as proof of absence.


## 4. Full source inventory — every original record

The received document attributes the original values below to `original_crawl/sources.json`, which is not present in this recovered bundle. “Next check” denotes a historical proposed action, not reported execution. Blank values remain `[not recorded in original crawl]`.

<a id="s001"></a>

### S001 — ProofAtlas: Jones Unknot Conjecture

**Priority:** P0

**Primary type:** research_process_archive

**Secondary type/tags:** problem_incubator; argument_map; failed_routes

**Classification basis:** Publishing function of the inspected source; provisional until authoritative taxonomy is recovered

**Type-assignment confidence:** high

**Platform:** website

**Format / publishing role:** research page

**Navigation group:** G01 — Direct Jones proof/search programmes and current audit

**Canonical source URL / original locator:** https://www.proofatlas.ai/collaboration/jones-unknot-conjecture/

**Canonical GitHub repository:** [not recorded in original crawl]

**Direct manuscript / proof / data URLs:** [not recorded in original crawl]

**Scholarly authors as recorded:** pending

**Maintainer / operator / publisher:** ProofAtlas

**AI contribution:** AI-oriented collaboration; authorship of individual retained claims unresolved

**Artifact kinds:** claim map; partial reductions; failure records; finite computations

**Publication / source date:** 2026-08-15 (source/status record)

**Version:** [not recorded in original crawl]

**Identifiers:** [not recorded in original crawl]

**Claim or resource as recorded:** Restricted weighted-triangular-prism investigation. Site reports 4,344 retained lines; selected route map and outstanding topology/coverage obligations are public.

**Evidence status:** source inspected; not independently reproduced

**Inspection depth reported by prior crawl:** primary page or abstract inspected

**External specialist review:** not established in this crawl

**Limitations and correction history:** Full underlying line-by-line archive was not obtained. Global rigid-kernel and smoothing-link reductions remain open. Counts and finite computations are self-reported, not independent validation.

**Potential mathematical utility:** Audit algebra-to-diagram bridges; compare restricted reductions with the current twist-family objection.

**Recommended next check — not yet performed:** Retrieve the raw weighted-prism investigation if publicly available; enumerate every residual-stratum, embedding and smoothing-link obligation. Treat the visible route map as a pointer, not the missing proof.

**Related source IDs:** [not recorded in original crawl]

**Relationship as recorded:** standalone source

**Associated inherited paper records:** Not indexed in the inherited 25 paper rows; inspect source-specific leads and backlog.

**Author-bibliography status:** pending; not exhaustive

**Prior crawl last-checked date:** 2026-11-02

---

<a id="s002"></a>

### S002 — Learning Topological Invariance

**Priority:** P0

**Primary type:** original_results

**Secondary type/tags:** [not recorded in original crawl]

**Classification basis:** Publishing function of the inspected source; provisional until authoritative taxonomy is recovered

**Type-assignment confidence:** high

**Platform:** arXiv

**Format / publishing role:** original manuscript

**Navigation group:** G01 — Direct Jones proof/search programmes and current audit

**Canonical source URL / original locator:** https://arxiv.org/abs/2504.12390

**Canonical GitHub repository:** [not recorded in original crawl]

**Direct manuscript / proof / data URLs:** https://arxiv.org/html/2504.12390v1

**Scholarly authors as recorded:** James Halverson; Fabian Ruehle

**Maintainer / operator / publisher:** pending

**AI contribution:** machine-learning-guided candidate generation

**Artifact kinds:** text

**Publication / source date:** 2025-04-16

**Version:** v1 inspected

**Identifiers:** arXiv:2504.12390

**Claim or resource as recorded:** Transformer-based polynomial-to-braid generation and latent-space exploration. Section 3.5 reports several hundred thousand generated knots without finding a nontrivial knot having Jones polynomial one.

**Evidence status:** source inspected; not independently reproduced

**Inspection depth reported by prior crawl:** primary page or abstract inspected

**External specialist review:** not established in this crawl

**Limitations and correction history:** Negative finite search, not proof of detection. Author-released code association remains pending; generic cited software must not be assigned to these authors.

**Potential mathematical utility:** Directly relevant Jones-trivial braid-search design; reproducibility follow-up needed.

**Recommended next check — not yet performed:** Read Section 3.5 in the exact cited version; locate author-released code and data through release pages and author links. Reproduce a small candidate-generation run with exact Jones and independent nontriviality checks.

**Related source IDs:** [not recorded in original crawl]

**Relationship as recorded:** standalone source

**Associated inherited paper records:** P001

**Author-bibliography status:** pending; not exhaustive

**Prior crawl last-checked date:** 2026-11-02

---

<a id="s003"></a>

### S003 — The Unknotting Number, Hard Unknot Diagrams, and Reinforcement Learning

**Priority:** P0

**Primary type:** original_results

**Secondary type/tags:** [not recorded in original crawl]

**Classification basis:** Publishing function of the inspected source; provisional until authoritative taxonomy is recovered

**Type-assignment confidence:** high

**Platform:** journal

**Format / publishing role:** published research manuscript

**Navigation group:** G01 — Direct Jones proof/search programmes and current audit

**Canonical source URL / original locator:** https://www.tandfonline.com/doi/full/10.1080/10586458.2025.2542174

**Canonical GitHub repository:** [not recorded in original crawl]

**Direct manuscript / proof / data URLs:** https://arxiv.org/abs/2409.09032 | gs://gdm-unknotting

**Scholarly authors as recorded:** Taylor Applebaum; Sam Blackwell; Alex Davies; Thomas Edlich; András Juhász; Marc Lackenby; Nenad Tomašev; Daniel Zheng

**Maintainer / operator / publisher:** DeepMind / Oxford research collaboration; Taylor & Francis publisher

**AI contribution:** reinforcement learning and computational searches

**Artifact kinds:** text

**Publication / source date:** 2025-08-18 (publication); 2024-09-13 (initial preprint)

**Version:** [not recorded in original crawl]

**Identifiers:** arXiv:2409.09032; DOI:10.1080/10586458.2025.2542174

**Claim or resource as recorded:** Published ML knot study; data availability lists 2,464,461 hard unknot diagrams and 382 really hard unknot diagrams, plus random and quasipositive knot datasets.

**Evidence status:** source inspected; not independently reproduced

**Inspection depth reported by prior crawl:** primary page or abstract inspected

**External specialist review:** published in Experimental Mathematics; this crawl did not rerun certificates

**Limitations and correction history:** Failure of simplification is not a nontriviality certificate. Some separate unknotting-number values in this work are conditional on additivity. Indexed publisher text was available; direct publisher open returned 403. Bucket files were not downloaded.

**Potential mathematical utility:** Adversarial negative controls for Jones-trivial candidate classifiers and simplification pipelines.

**Recommended next check — not yet performed:** Retrieve the actual gs://gdm-unknotting file manifest, licensing and checksums; select a small pinned sample of known hard unknots and independently validate labels before using them as negative controls.

**Related source IDs:** [not recorded in original crawl]

**Relationship as recorded:** standalone source

**Associated inherited paper records:** P002

**Author-bibliography status:** pending; not exhaustive

**Prior crawl last-checked date:** 2026-11-02

---

<a id="s004"></a>

### S004 — Samaritan Jones-unknot open-problem contract

**Priority:** P0

**Primary type:** problem_incubator

**Secondary type/tags:** benchmark; validation_contract

**Classification basis:** Publishing function of the inspected source; provisional until authoritative taxonomy is recovered

**Type-assignment confidence:** high

**Platform:** website

**Format / publishing role:** research page

**Navigation group:** G01 — Direct Jones proof/search programmes and current audit

**Canonical source URL / original locator:** https://samaritan-research.org/frontiermath/open-problems/jones-unknot

**Canonical GitHub repository:** [not recorded in original crawl]

**Direct manuscript / proof / data URLs:** [not recorded in original crawl]

**Scholarly authors as recorded:** pending

**Maintainer / operator / publisher:** Samaritan Research

**AI contribution:** AI research challenge

**Artifact kinds:** problem statement; verification requirements

**Publication / source date:** [not recorded in original crawl]

**Version:** [not recorded in original crawl]

**Identifiers:** [not recorded in original crawl]

**Claim or resource as recorded:** Public counterexample submission target: classical one-component PD code, exact Jones polynomial one, and positive genus from knot Floer homology. Submission restrictions include a 100-crossing cap.

**Evidence status:** source inspected; not independently reproduced

**Inspection depth reported by prior crawl:** primary page or abstract inspected

**External specialist review:** not established in this crawl

**Limitations and correction history:** Problem/validation specification, not a found counterexample or a published proof. Verification code was not independently executed.

**Potential mathematical utility:** Template for separating exact polynomial equality from independent topological nontriviality.

**Recommended next check — not yet performed:** Fetch the current validation specification and any published code; separate benchmark crossing/runtime restrictions from mathematical hypotheses. Check the meaning and implementation of the proposed positive-genus certificate.

**Related source IDs:** [not recorded in original crawl]

**Relationship as recorded:** standalone source

**Associated inherited paper records:** Not indexed in the inherited 25 paper rows; inspect source-specific leads and backlog.

**Author-bibliography status:** pending; not exhaustive

**Prior crawl last-checked date:** 2026-11-02

---

<a id="s005"></a>

### S005 — On trivial Jones--Vassiliev polynomials

**Priority:** P0

**Primary type:** original_results

**Secondary type/tags:** [not recorded in original crawl]

**Classification basis:** Publishing function of the inspected source; provisional until authoritative taxonomy is recovered

**Type-assignment confidence:** high

**Platform:** arXiv

**Format / publishing role:** claimed proof manuscript

**Navigation group:** G01 — Direct Jones proof/search programmes and current audit

**Canonical source URL / original locator:** https://arxiv.org/abs/2606.22410

**Canonical GitHub repository:** [not recorded in original crawl]

**Direct manuscript / proof / data URLs:** [not recorded in original crawl]

**Scholarly authors as recorded:** Avishy Carmi; Eliahu Cohen

**Maintainer / operator / publisher:** pending

**AI contribution:** not established

**Artifact kinds:** text

**Publication / source date:** 2026-06-21

**Version:** June 21 manuscript inspected; later version status pending

**Identifiers:** arXiv:2606.22410

**Claim or resource as recorded:** Claims general ordinary Jones unknot detection through finite-type coefficient and geometric compression arguments.

**Evidence status:** general proof claim; substantive objection in user audit

**Inspection depth reported by prior crawl:** primary page or abstract inspected

**External specialist review:** not established in this crawl

**Limitations and correction history:** The user’s October 31 audit challenges the Section 5 uniform compression package with an explicit twist family. No independent validation of the general claim was located. Latest version/correction status not fully resolved.

**Potential mathematical utility:** Exact audit target; isolate false uniform bounds and retain correct conditional algebra.

**Recommended next check — not yet performed:** Retrieve the latest primary version and revision history; compare Proposition 5.12, Theorem 5.6 and Lemma 5.8 against the October 31 audit. Extract exact diagram hypotheses and any correction, withdrawal or external specialist response.

**Related source IDs:** S006

**Relationship as recorded:** standalone source

**Associated inherited paper records:** P003

**Author-bibliography status:** pending; not exhaustive

**Prior crawl last-checked date:** 2026-11-02

---

<a id="s006"></a>

### S006 — User audit: concrete obstruction to Carmi–Cohen proof

**Priority:** P0

**Primary type:** research_process_archive

**Secondary type/tags:** [not recorded in original crawl]

**Classification basis:** Publishing function of the inspected source; provisional until authoritative taxonomy is recovered

**Type-assignment confidence:** high

**Platform:** user Library / local copy

**Format / publishing role:** existing project audit

**Navigation group:** G01 — Direct Jones proof/search programmes and current audit

**Canonical source URL / original locator:** context/jones-unknot-proof-audit.pdf

**Canonical GitHub repository:** [not recorded in original crawl]

**Direct manuscript / proof / data URLs:** [not recorded in original crawl]

**Local audit in this package:** `original_crawl/context/jones-unknot-proof-audit.pdf`.

**Scholarly authors as recorded:** Not individually credited in the document

**Maintainer / operator / publisher:** User project; document says prepared with Codex

**AI contribution:** substantial audit assistance, as credited

**Artifact kinds:** audit; exact recurrence; proof objection

**Publication / source date:** 2026-10-31

**Version:** [not recorded in original crawl]

**Identifiers:** [not recorded in original crawl]

**Claim or resource as recorded:** For the stated trefoil-based odd twist family, V_L=x^4 V_(L-2)+x^2-x^4+x^6-x^8 and deg_p(V_L)=2L+5; L=23 gives b_51=-1 versus claimed uniform bound 22.

**Evidence status:** full existing audit read; recurrence independently replayed algebraically

**Inspection depth reported by prior crawl:** primary page or abstract inspected

**External specialist review:** not established in this crawl

**Limitations and correction history:** User-provided Codex-assisted mathematical audit, not external specialist review. An algebra-only replay is supplied in checks/; the diagram identification is not newly verified here. This is not a counterexample to Jones detection.

**Potential mathematical utility:** Regression test against alleged twist-length-independent compression arguments.

**Recommended next check — not yet performed:** Read the included audit; independently construct signed PD or braid encodings for its odd-twist family and derive the smoothing recurrence. Recompute with a separate exact backend. The supplied replay only tests algebra conditional on the recurrence.

**Related source IDs:** S005

**Relationship as recorded:** standalone source

**Associated inherited paper records:** Not indexed in the inherited 25 paper rows; inspect source-specific leads and backlog.

**Author-bibliography status:** pending; not exhaustive

**Prior crawl last-checked date:** 2026-11-02

---

<a id="s007"></a>

### S007 — Does the Jones polynomial detect the unknot?

**Priority:** P1

**Primary type:** original_results

**Secondary type/tags:** [not recorded in original crawl]

**Classification basis:** Publishing function of the inspected source; provisional until authoritative taxonomy is recovered

**Type-assignment confidence:** high

**Platform:** arXiv / journal

**Format / publishing role:** research manuscript

**Navigation group:** G02 — Braid representations and closed-four-braid routes

**Canonical source URL / original locator:** https://arxiv.org/abs/math/0012086

**Canonical GitHub repository:** [not recorded in original crawl]

**Direct manuscript / proof / data URLs:** [not recorded in original crawl]

**Scholarly authors as recorded:** Stephen Bigelow

**Maintainer / operator / publisher:** pending

**AI contribution:** not established

**Artifact kinds:** text

**Publication / source date:** 2000-12-12 (preprint); 2002 (journal)

**Version:** [not recorded in original crawl]

**Identifiers:** arXiv:math/0012086; DOI:10.1142/S0218216502001779

**Claim or resource as recorded:** Braid-representation approach to Jones unknot detection and candidate-search mechanisms.

**Evidence status:** source inspected; not independently reproduced

**Inspection depth reported by prior crawl:** primary page or abstract inspected

**External specialist review:** not established in this crawl

**Limitations and correction history:** Historical program; do not treat its conjectural implications as stronger than later proved statements. Compare Ito’s precise result.

**Potential mathematical utility:** Conceptual starting point for braid-kernel and trace-collision search.

**Recommended next check — not yet performed:** Extract the precise braid-representation and closure constructions, distinguishing conjectural suggestions from proved statements; compare the later directional theorem in S008.

**Related source IDs:** S008;S009;S010

**Relationship as recorded:** standalone source

**Associated inherited paper records:** P004

**Author-bibliography status:** pending; not exhaustive

**Prior crawl last-checked date:** 2026-11-02

---

<a id="s008"></a>

### S008 — A kernel of a braid group representation yields a knot with trivial knot polynomials

**Priority:** P0

**Primary type:** original_results

**Secondary type/tags:** [not recorded in original crawl]

**Classification basis:** Publishing function of the inspected source; provisional until authoritative taxonomy is recovered

**Type-assignment confidence:** high

**Platform:** arXiv / journal

**Format / publishing role:** research theorem manuscript

**Navigation group:** G02 — Braid representations and closed-four-braid routes

**Canonical source URL / original locator:** https://arxiv.org/abs/1402.2028

**Canonical GitHub repository:** [not recorded in original crawl]

**Direct manuscript / proof / data URLs:** [not recorded in original crawl]

**Scholarly authors as recorded:** Tetsuya Ito

**Maintainer / operator / publisher:** pending

**AI contribution:** not established

**Artifact kinds:** text

**Publication / source date:** 2014-02-10 (preprint); 2015 (journal)

**Version:** [not recorded in original crawl]

**Identifiers:** arXiv:1402.2028; DOI:10.1007/s00209-015-1426-7

**Claim or resource as recorded:** Corollary 3: nonfaithfulness of the Burau representation of B_4 implies that Jones fails to detect the unknot. More general results produce infinitely many hyperbolic knots sharing quantum invariants under representation hypotheses.

**Evidence status:** source inspected; not independently reproduced

**Inspection depth reported by prior crawl:** full text and exact corollary inspected

**External specialist review:** not established in this crawl

**Limitations and correction history:** The implication is one-way. Faithfulness is not a proof that a trace-valued closure invariant detects the unknot.

**Potential mathematical utility:** Exact theorem governing the Burau-kernel route.

**Recommended next check — not yet performed:** Read Corollary 3 and its hypotheses directly; maintain the direction nonfaithful Burau(B_4) implies Jones nondetection. Identify exactly which construction produces a classical nontrivial knot.

**Related source IDs:** S007;S009

**Relationship as recorded:** standalone source

**Associated inherited paper records:** P005

**Author-bibliography status:** pending; not exhaustive

**Prior crawl last-checked date:** 2026-11-02

---

<a id="s009"></a>

### S009 — The Burau representation of the braid group is faithful for n = 4

**Priority:** P0

**Primary type:** original_results

**Secondary type/tags:** [not recorded in original crawl]

**Classification basis:** Publishing function of the inspected source; provisional until authoritative taxonomy is recovered

**Type-assignment confidence:** high

**Platform:** arXiv

**Format / publishing role:** claimed theorem preprint

**Navigation group:** G02 — Braid representations and closed-four-braid routes

**Canonical source URL / original locator:** https://arxiv.org/abs/2607.05283

**Canonical GitHub repository:** [not recorded in original crawl]

**Direct manuscript / proof / data URLs:** [not recorded in original crawl]

**Scholarly authors as recorded:** Vasudha Bharathram; Joan S. Birman; Tara E. Brendle

**Maintainer / operator / publisher:** pending

**AI contribution:** not established

**Artifact kinds:** text

**Publication / source date:** 2026-07-06 (initial submission)

**Version:** retrieved July manuscript; revision history pending

**Identifiers:** arXiv:2607.05283

**Claim or resource as recorded:** 2026 preprint claims faithfulness for the four-strand Burau representation.

**Evidence status:** source inspected; not independently reproduced

**Inspection depth reported by prior crawl:** primary page or abstract inspected

**External specialist review:** not established in this crawl

**Limitations and correction history:** Independent specialist acceptance and latest revision status were not established. Even if correct, this blocks one kernel strategy, not all Jones counterexamples and not trace collisions.

**Potential mathematical utility:** Audit before investing in B_4 kernel searches; do not mark Jones conjecture solved.

**Recommended next check — not yet performed:** Check the latest arXiv version, correction history and named specialist assessments before relying on four-strand faithfulness. Do not convert faithfulness into injectivity of trace or Jones unknot detection.

**Related source IDs:** S008;S010

**Relationship as recorded:** standalone source

**Associated inherited paper records:** P006

**Author-bibliography status:** pending; not exhaustive

**Prior crawl last-checked date:** 2026-11-02

---

<a id="s010"></a>

### S010 — Closed 4-braids and the Jones unknot conjecture

**Priority:** P1

**Primary type:** original_results

**Secondary type/tags:** [not recorded in original crawl]

**Classification basis:** Publishing function of the inspected source; provisional until authoritative taxonomy is recovered

**Type-assignment confidence:** high

**Platform:** arXiv

**Format / publishing role:** research manuscript

**Navigation group:** G02 — Braid representations and closed-four-braid routes

**Canonical source URL / original locator:** https://arxiv.org/abs/2402.02553

**Canonical GitHub repository:** [not recorded in original crawl]

**Direct manuscript / proof / data URLs:** [not recorded in original crawl]

**Scholarly authors as recorded:** Dmitriy Korzun; Elena Lanina; Alexey Sleptsov

**Maintainer / operator / publisher:** pending

**AI contribution:** not established

**Artifact kinds:** text

**Publication / source date:** 2024

**Version:** v2, 2024-04-18

**Identifiers:** arXiv:2402.02553

**Claim or resource as recorded:** Necessary polynomial constraints for hypothetical Jones-trivial closed four-braid knots, including a writhe-parameterized HOMFLY family.

**Evidence status:** source inspected; not independently reproduced

**Inspection depth reported by prior crawl:** primary page or abstract inspected

**External specialist review:** not established in this crawl

**Limitations and correction history:** A compatible formal polynomial is not an actual realizable nontrivial knot. Abstract-level triage, not full theorem audit.

**Potential mathematical utility:** Constraints and rejection tests for bounded-braid searches.

**Recommended next check — not yet performed:** Extract the necessary polynomial restrictions and their quantifiers; determine whether any candidate data are realized by an actual braid. Use them as filters, not existence certificates.

**Related source IDs:** S007;S008;S009

**Relationship as recorded:** standalone source

**Associated inherited paper records:** P007

**Author-bibliography status:** pending; not exhaustive

**Prior crawl last-checked date:** 2026-11-02

---

<a id="s011"></a>

### S011 — Verification of the Jones unknot conjecture up to 24 crossings

**Priority:** P0

**Primary type:** original_results

**Secondary type/tags:** [not recorded in original crawl]

**Classification basis:** Publishing function of the inspected source; provisional until authoritative taxonomy is recovered

**Type-assignment confidence:** high

**Platform:** arXiv / journal

**Format / publishing role:** computational theorem manuscript

**Navigation group:** G03 — Established boundaries, structural classes and stronger invariants

**Canonical source URL / original locator:** https://arxiv.org/abs/2003.06724

**Canonical GitHub repository:** [not recorded in original crawl]

**Direct manuscript / proof / data URLs:** [not recorded in original crawl]

**Scholarly authors as recorded:** Robert E. Tuzun; Adam S. Sikora

**Maintainer / operator / publisher:** pending

**AI contribution:** not established

**Artifact kinds:** finite exhaustive verification; theorem

**Publication / source date:** 2020-03-15 (initial); 2021 (journal)

**Version:** v2, 2021-03-23

**Identifiers:** arXiv:2003.06724; DOI:10.1142/S0218216521500206

**Claim or resource as recorded:** Verifies ordinary Jones unknot detection for all knots with crossing number at most 24.

**Evidence status:** source inspected; not independently reproduced

**Inspection depth reported by prior crawl:** primary page or abstract inspected

**External specialist review:** published in Journal of Knot Theory and Its Ramifications

**Limitations and correction history:** Finite crossing range, not all knots. Enumeration and implementation were not rerun in this crawl.

**Potential mathematical utility:** Known finite-range baseline and sanity check for any proposed small counterexample.

**Recommended next check — not yet performed:** Locate enumeration code, input coverage and proof of completeness for the stated crossing range; record versions. Distinguish the finite theorem from unrestricted detection and diagram crossing count from minimal crossing number.

**Related source IDs:** [not recorded in original crawl]

**Relationship as recorded:** standalone source

**Associated inherited paper records:** P008

**Author-bibliography status:** pending; not exhaustive

**Prior crawl last-checked date:** 2026-11-02

---

<a id="s012"></a>

### S012 — Khovanov homology is an unknot-detector

**Priority:** P1

**Primary type:** original_results

**Secondary type/tags:** [not recorded in original crawl]

**Classification basis:** Publishing function of the inspected source; provisional until authoritative taxonomy is recovered

**Type-assignment confidence:** high

**Platform:** arXiv / journal

**Format / publishing role:** theorem manuscript

**Navigation group:** G03 — Established boundaries, structural classes and stronger invariants

**Canonical source URL / original locator:** https://arxiv.org/abs/1005.4346

**Canonical GitHub repository:** [not recorded in original crawl]

**Direct manuscript / proof / data URLs:** [not recorded in original crawl]

**Scholarly authors as recorded:** P. B. Kronheimer; T. S. Mrowka

**Maintainer / operator / publisher:** pending

**AI contribution:** not established

**Artifact kinds:** text

**Publication / source date:** 2010 (preprint); 2011 (journal)

**Version:** [not recorded in original crawl]

**Identifiers:** arXiv:1005.4346

**Claim or resource as recorded:** Khovanov-homological unknot detection.

**Evidence status:** source inspected; not independently reproduced

**Inspection depth reported by prior crawl:** primary page or abstract inspected

**External specialist review:** not established in this crawl

**Limitations and correction history:** Cannot be replaced by the statement that its graded Euler characteristic, the Jones polynomial, detects the unknot. Homological information may cancel.

**Potential mathematical utility:** Stronger invariant for independently testing candidate nontriviality.

**Recommended next check — not yet performed:** Extract the exact reduced/unreduced and coefficient hypotheses of the detection theorem; use the homological invariant only under those hypotheses, without replacing it by its Euler characteristic.

**Related source IDs:** [not recorded in original crawl]

**Relationship as recorded:** standalone source

**Associated inherited paper records:** P009

**Author-bibliography status:** pending; not exhaustive

**Prior crawl last-checked date:** 2026-11-02

---

<a id="s013"></a>

### S013 — The Jones polynomial of an almost alternating link

**Priority:** P1

**Primary type:** original_results

**Secondary type/tags:** [not recorded in original crawl]

**Classification basis:** Publishing function of the inspected source; provisional until authoritative taxonomy is recovered

**Type-assignment confidence:** high

**Platform:** journal

**Format / publishing role:** published theorem manuscript

**Navigation group:** G03 — Established boundaries, structural classes and stronger invariants

**Canonical source URL / original locator:** https://nyjm.albany.edu/j/2017/23-71.html

**Canonical GitHub repository:** [not recorded in original crawl]

**Direct manuscript / proof / data URLs:** [not recorded in original crawl]

**Scholarly authors as recorded:** Adam M. Lowrance; Dean Spyropoulos

**Maintainer / operator / publisher:** pending

**AI contribution:** not established

**Artifact kinds:** text

**Publication / source date:** 2017-11-06

**Version:** [not recorded in original crawl]

**Identifiers:** NYJM 23 (2017), 1611–1639

**Claim or resource as recorded:** Almost alternating links have nontrivial Jones polynomial; develops endpoint-coefficient information.

**Evidence status:** source inspected; not independently reproduced

**Inspection depth reported by prior crawl:** primary page or abstract inspected

**External specialist review:** published in New York Journal of Mathematics

**Limitations and correction history:** Restricted class, not a theorem for arbitrary diagrams or all knots. Do not silently broaden to other Turaev-genus classes.

**Potential mathematical utility:** Exclude structural classes and test coefficient arguments.

**Recommended next check — not yet performed:** Read the full almost-alternating theorem and definitions, record precise exceptions and diagram hypotheses, and add a complete manuscript record when merging. Do not broaden the theorem by analogy.

**Related source IDs:** [not recorded in original crawl]

**Relationship as recorded:** standalone source

**Associated inherited paper records:** Not indexed in the inherited 25 paper rows; inspect source-specific leads and backlog.

**Author-bibliography status:** pending; not exhaustive

**Prior crawl last-checked date:** 2026-11-02

---

<a id="s014"></a>

### S014 — On the modular Jones polynomial

**Priority:** P0

**Primary type:** original_results

**Secondary type/tags:** [not recorded in original crawl]

**Classification basis:** Publishing function of the inspected source; provisional until authoritative taxonomy is recovered

**Type-assignment confidence:** high

**Platform:** arXiv / journal

**Format / publishing role:** research theorem manuscript

**Navigation group:** G03 — Established boundaries, structural classes and stronger invariants

**Canonical source URL / original locator:** https://arxiv.org/abs/2008.00716

**Canonical GitHub repository:** [not recorded in original crawl]

**Direct manuscript / proof / data URLs:** [not recorded in original crawl]

**Scholarly authors as recorded:** Guillaume Pagel

**Maintainer / operator / publisher:** pending

**AI contribution:** not established

**Artifact kinds:** text

**Publication / source date:** 2020

**Version:** [not recorded in original crawl]

**Identifiers:** arXiv:2008.00716; DOI:10.5802/crmath.106

**Claim or resource as recorded:** Constructs nontrivial knots with Jones polynomial congruent to one modulo arbitrarily high powers of three; includes related modular constructions.

**Evidence status:** source inspected; not independently reproduced

**Inspection depth reported by prior crawl:** full primary text inspected

**External specialist review:** not established in this crawl

**Limitations and correction history:** Congruence modulo an integer is not equality over Z[t,t^-1]. Do not assume a bounded list of modular tests settles exact triviality.

**Potential mathematical utility:** Adversarial tests for modular sieves; prevent false exact certificates.

**Recommended next check — not yet performed:** Extract an explicit modular-Jones construction and use it as an adversarial modular-sieve test; derive any coefficient bound needed before promoting modular agreement to exact equality.

**Related source IDs:** [not recorded in original crawl]

**Relationship as recorded:** standalone source

**Associated inherited paper records:** P010

**Author-bibliography status:** pending; not exhaustive

**Prior crawl last-checked date:** 2026-11-02

---

<a id="s015"></a>

### S015 — From knots to four-manifolds

**Priority:** P2

**Primary type:** research_index

**Secondary type/tags:** [not recorded in original crawl]

**Classification basis:** Publishing function of the inspected source; provisional until authoritative taxonomy is recovered

**Type-assignment confidence:** high

**Platform:** arXiv

**Format / publishing role:** expert survey

**Navigation group:** G03 — Established boundaries, structural classes and stronger invariants

**Canonical source URL / original locator:** https://arxiv.org/abs/2601.05425

**Canonical GitHub repository:** [not recorded in original crawl]

**Direct manuscript / proof / data URLs:** [not recorded in original crawl]

**Scholarly authors as recorded:** Ciprian Manolescu

**Maintainer / operator / publisher:** pending

**AI contribution:** not established

**Artifact kinds:** text

**Publication / source date:** 2026

**Version:** v2, 2026-03-29

**Identifiers:** arXiv:2601.05425

**Claim or resource as recorded:** Expert survey of knot and four-manifold topology, useful for status and context.

**Evidence status:** source inspected; not independently reproduced

**Inspection depth reported by prior crawl:** primary page or abstract inspected

**External specialist review:** not established in this crawl

**Limitations and correction history:** Survey is not an original Jones proof and its composition date need not postdate later claims.

**Potential mathematical utility:** Terminology, theorem boundaries, and citation discovery.

**Recommended next check — not yet performed:** Use the survey for primary references and terminology, while separating manuscript composition and publication dates. Do not treat it as a direct review of a later proof claim.

**Related source IDs:** [not recorded in original crawl]

**Relationship as recorded:** standalone source

**Associated inherited paper records:** P011

**Author-bibliography status:** pending; not exhaustive

**Prior crawl last-checked date:** 2026-11-02

---

<a id="s016"></a>

### S016 — Machine learning methods and unknotting numbers: repository

**Priority:** P1

**Primary type:** original_results

**Secondary type/tags:** research_process_archive; research_infrastructure

**Classification basis:** Publishing function of the inspected source; provisional until authoritative taxonomy is recovered

**Type-assignment confidence:** high

**Platform:** GitHub

**Format / publishing role:** original-result and verification archive

**Navigation group:** G04 — Computational certificates, reinforcement learning and datasets

**Canonical source URL / original locator:** https://github.com/dtubbenhauer/unknot

**Canonical GitHub repository:** dtubbenhauer/unknot

**Direct manuscript / proof / data URLs:** [not recorded in original crawl]

**Scholarly authors as recorded:** Anne Dranowski; Zhen Guo; Yura Kabkov; Daniel Tubbenhauer

**Maintainer / operator / publisher:** dtubbenhauer / Daniel Tubbenhauer

**AI contribution:** machine learning; precise LLM role pending

**Artifact kinds:** certificates; code; datasets; correction log

**Publication / source date:** [not recorded in original crawl]

**Version:** [not recorded in original crawl]

**Identifiers:** Associated paper identifier pending

**Claim or resource as recorded:** Repository reports 1,943 lower-bound improvements relative to its frozen KnotInfo baseline, including 1,677 exact values, with scripts, checksums, status notes and an erratum.

**Evidence status:** source inspected; not independently reproduced

**Inspection depth reported by prior crawl:** README and correction/status descriptions inspected; code not executed

**External specialist review:** not established in this crawl

**Limitations and correction history:** Counts are source-reported and not rerun. A correction concerns an orientation convention in an Owens obstruction. Minimal-diagram unknotting numbers are not ordinary unknotting numbers.

**Potential mathematical utility:** Reusable lower-bound certificate architecture and examples of corrected claims.

**Recommended next check — not yet performed:** Resolve the associated paper identifier from CITATION.cff, releases and author pages; pin the corrected repository version, read the erratum, and replay one claimed certificate with the frozen KnotInfo baseline.

**Related source IDs:** [not recorded in original crawl]

**Relationship as recorded:** standalone source

**Associated inherited paper records:** Not indexed in the inherited 25 paper rows; inspect source-specific leads and backlog.

**Author-bibliography status:** pending; not exhaustive

**Prior crawl last-checked date:** 2026-11-02

---

<a id="s017"></a>

### S017 — Unknotting numbers via Tait graphs

**Priority:** P1

**Primary type:** original_results

**Secondary type/tags:** [not recorded in original crawl]

**Classification basis:** Publishing function of the inspected source; provisional until authoritative taxonomy is recovered

**Type-assignment confidence:** high

**Platform:** GitHub

**Format / publishing role:** original computational research archive

**Navigation group:** G04 — Computational certificates, reinforcement learning and datasets

**Canonical source URL / original locator:** https://github.com/Pinocchio315/unknotting-tait-graphs

**Canonical GitHub repository:** pinocchio315/unknotting-tait-graphs

**Direct manuscript / proof / data URLs:** https://arxiv.org/abs/2609.09861 | https://github.com/Pinocchio315/unknotting-tait-graphs/blob/main/results/extensions_2026-09-10/lower/README.md

**Scholarly authors as recorded:** Seong-Jin Lee

**Maintainer / operator / publisher:** Pinocchio315; association supported by paper/repository

**AI contribution:** not established

**Artifact kinds:** PD data; crossing-change witnesses; lower-bound scripts

**Publication / source date:** 2026-09-09 (v1); 2026-09-11 (v2)

**Version:** v2, 2026-09-11; arXiv submission history checked

**Identifiers:** arXiv:2609.09861

**Claim or resource as recorded:** Tait-graph crossing-change witnesses and lower-bound verification materials; associated paper reports 2,540 newly exact values relative to its dated KnotInfo baseline.

**Evidence status:** source inspected; not independently reproduced

**Inspection depth reported by prior crawl:** primary page or abstract inspected

**External specialist review:** not established in this crawl

**Limitations and correction history:** Not Jones detection. Archived total 2,734 exact values includes 194 already official; do not count all as new. Certificate replay was not run.

**Potential mathematical utility:** Reproducible knot certification patterns; not proof from a failed simplifier.

**Recommended next check — not yet performed:** Pin the v2 manuscript and relevant certificate directories; replay a small lower/upper-bound certificate pair. Separate the 2,540 claimed new values from the 194 previously official entries in the archived total.

**Related source IDs:** [not recorded in original crawl]

**Relationship as recorded:** standalone source

**Associated inherited paper records:** P012

**Author-bibliography status:** pending; not exhaustive

**Prior crawl last-checked date:** 2026-11-02

---

<a id="s018"></a>

### S018 — RL unknotter, hard unknots and unknotting number

**Priority:** P1

**Primary type:** original_results

**Secondary type/tags:** [not recorded in original crawl]

**Classification basis:** Publishing function of the inspected source; provisional until authoritative taxonomy is recovered

**Type-assignment confidence:** high

**Platform:** website

**Format / publishing role:** author research page with original manuscript and code associations

**Navigation group:** G04 — Computational certificates, reinforcement learning and datasets

**Canonical source URL / original locator:** https://www.dtubbenhauer.com/unknotter.html

**Canonical GitHub repository:** [not recorded in original crawl]

**Direct manuscript / proof / data URLs:** https://arxiv.org/abs/2603.07955

**Scholarly authors as recorded:** Anne Dranowski; Yura Kabkov; Daniel Tubbenhauer

**Maintainer / operator / publisher:** Daniel Tubbenhauer author site

**AI contribution:** reinforcement learning

**Artifact kinds:** text

**Publication / source date:** 2026-03 (initial preprint)

**Version:** [not recorded in original crawl]

**Identifiers:** arXiv:2603.07955

**Claim or resource as recorded:** RL legal-move proposal and diagram-inflation research; recovers a three-crossing-change upper bound for 4_1#9_10 and describes a systematic upper-bound improver.

**Evidence status:** source inspected; not independently reproduced

**Inspection depth reported by prior crawl:** primary page or abstract inspected

**External specialist review:** not established in this crawl

**Limitations and correction history:** Upper bounds require replayable successful moves; unsuccessful search is not a lower bound. Manuscript is a preprint.

**Potential mathematical utility:** Hard-unknot simplification and candidate rejection pipeline.

**Recommended next check — not yet performed:** Read the paper and author-linked companion descriptions together; map each claimed bound to a successful explicit move path and separate search exhaustion from proof.

**Related source IDs:** S019;S020;S021

**Relationship as recorded:** standalone source

**Associated inherited paper records:** P013

**Author-bibliography status:** pending; not exhaustive

**Prior crawl last-checked date:** 2026-11-02

---

<a id="s019"></a>

### S019 — untangling-number

**Priority:** P1

**Primary type:** research_infrastructure

**Secondary type/tags:** [not recorded in original crawl]

**Classification basis:** Publishing function of the inspected source; provisional until authoritative taxonomy is recovered

**Type-assignment confidence:** high

**Platform:** GitHub

**Format / publishing role:** companion code and experiments

**Navigation group:** G04 — Computational certificates, reinforcement learning and datasets

**Canonical source URL / original locator:** https://github.com/annedranowski/untangling-number

**Canonical GitHub repository:** annedranowski/untangling-number

**Direct manuscript / proof / data URLs:** [not recorded in original crawl]

**Scholarly authors as recorded:** Paper: Anne Dranowski; Yura Kabkov; Daniel Tubbenhauer

**Maintainer / operator / publisher:** annedranowski / Anne Dranowski

**AI contribution:** reinforcement-learning workflow

**Artifact kinds:** Python; notebooks; PD generation

**Publication / source date:** [not recorded in original crawl]

**Version:** [not recorded in original crawl]

**Identifiers:** [not recorded in original crawl]

**Claim or resource as recorded:** RL crossing-reduction workflow, variant sweeps, PD pools and notebooks associated by the author site with arXiv:2603.07955.

**Evidence status:** source inspected; not independently reproduced

**Inspection depth reported by prior crawl:** primary page or abstract inspected

**External specialist review:** not established in this crawl

**Limitations and correction history:** Large artifacts are intentionally git-ignored; repository alone is not a complete dataset. Not a Jones theorem.

**Potential mathematical utility:** Reproducible candidate sweeps; audit missing external inputs.

**Recommended next check — not yet performed:** Inventory omitted or git-ignored data and model artifacts; locate their authoritative releases. Reproduce one small workflow only after versions, input conventions and dependencies are pinned.

**Related source IDs:** S018

**Relationship as recorded:** companion implementation; do not count paper twice

**Associated inherited paper records:** P013

**Author-bibliography status:** pending; not exhaustive

**Prior crawl last-checked date:** 2026-11-02

---

<a id="s020"></a>

### S020 — RL unknotter notebooks

**Priority:** P1

**Primary type:** research_process_archive

**Secondary type/tags:** [not recorded in original crawl]

**Classification basis:** Publishing function of the inspected source; provisional until authoritative taxonomy is recovered

**Type-assignment confidence:** high

**Platform:** GitHub

**Format / publishing role:** companion experiment notebooks

**Navigation group:** G04 — Computational certificates, reinforcement learning and datasets

**Canonical source URL / original locator:** https://github.com/dtubbenhauer/unknotter

**Canonical GitHub repository:** dtubbenhauer/unknotter

**Direct manuscript / proof / data URLs:** [not recorded in original crawl]

**Scholarly authors as recorded:** Paper: Anne Dranowski; Yura Kabkov; Daniel Tubbenhauer

**Maintainer / operator / publisher:** Daniel Tubbenhauer

**AI contribution:** reinforcement-learning notebooks

**Artifact kinds:** notebooks; training/evaluation procedures

**Publication / source date:** [not recorded in original crawl]

**Version:** [not recorded in original crawl]

**Identifiers:** [not recorded in original crawl]

**Claim or resource as recorded:** Notebooks for hard-unknot simplification and KnotInfo-compatible Jones-vector export, including mirror/shift matching.

**Evidence status:** source inspected; not independently reproduced

**Inspection depth reported by prior crawl:** primary page or abstract inspected

**External specialist review:** not established in this crawl

**Limitations and correction history:** Mirror or shift matching used for table lookup must not replace normalized exact V=1 testing. External input files and models may be required.

**Potential mathematical utility:** Useful hard-unknot experiments; normalize the actual invariant independently.

**Recommended next check — not yet performed:** Inspect the Jones-vector export and mirror/shift conventions; check normalized exact polynomials independently. Replay one notebook with all external data explicitly identified.

**Related source IDs:** S018

**Relationship as recorded:** companion notebook archive

**Associated inherited paper records:** P013

**Author-bibliography status:** pending; not exhaustive

**Prior crawl last-checked date:** 2026-11-02

---

<a id="s021"></a>

### S021 — Unknotting upper-bounds workflow

**Priority:** P1

**Primary type:** research_infrastructure

**Secondary type/tags:** [not recorded in original crawl]

**Classification basis:** Publishing function of the inspected source; provisional until authoritative taxonomy is recovered

**Type-assignment confidence:** high

**Platform:** GitHub

**Format / publishing role:** companion code

**Navigation group:** G04 — Computational certificates, reinforcement learning and datasets

**Canonical source URL / original locator:** https://github.com/dtubbenhauer/upperbounds

**Canonical GitHub repository:** dtubbenhauer/upperbounds

**Direct manuscript / proof / data URLs:** [not recorded in original crawl]

**Scholarly authors as recorded:** Paper: Anne Dranowski; Yura Kabkov; Daniel Tubbenhauer

**Maintainer / operator / publisher:** Daniel Tubbenhauer

**AI contribution:** RL-assisted upper-bound search

**Artifact kinds:** text

**Publication / source date:** [not recorded in original crawl]

**Version:** [not recorded in original crawl]

**Identifiers:** [not recorded in original crawl]

**Claim or resource as recorded:** Companion code for the RL unknotter paper, explicitly linked by its author research page.

**Evidence status:** source inspected; not independently reproduced

**Inspection depth reported by prior crawl:** primary page or abstract inspected

**External specialist review:** not established in this crawl

**Limitations and correction history:** Repository page inspected, not all certificates or workbook-driven runs. Not an independent Jones result.

**Potential mathematical utility:** Extend upper-bound searches with explicit move certificates.

**Recommended next check — not yet performed:** Locate actual output certificates and all workbook/input dependencies; replay a successful crossing-change path and identify the corresponding lower bound before calling a value exact.

**Related source IDs:** S018

**Relationship as recorded:** companion implementation

**Associated inherited paper records:** P013

**Author-bibliography status:** pending; not exhaustive

**Prior crawl last-checked date:** 2026-11-02

---

<a id="s022"></a>

### S022 — Computations of the slice genus and the unknotting number of links via machine learning

**Priority:** P1

**Primary type:** original_results

**Secondary type/tags:** [not recorded in original crawl]

**Classification basis:** Publishing function of the inspected source; provisional until authoritative taxonomy is recovered

**Type-assignment confidence:** high

**Platform:** arXiv

**Format / publishing role:** original research preprint

**Navigation group:** G04 — Computational certificates, reinforcement learning and datasets

**Canonical source URL / original locator:** https://arxiv.org/abs/2610.10206

**Canonical GitHub repository:** [not recorded in original crawl]

**Direct manuscript / proof / data URLs:** [not recorded in original crawl]

**Scholarly authors as recorded:** Yutong Dai; Oliver Hayman; András Juhász; Ludovico Morellato

**Maintainer / operator / publisher:** pending

**AI contribution:** reinforcement learning; Bayesian optimization; disclosed LLM proofreading and some coding assistance

**Artifact kinds:** manuscript; upper-bound paths; datasets; models

**Publication / source date:** 2026-10-07

**Version:** initial preprint inspected

**Identifiers:** arXiv:2610.10206

**Claim or resource as recorded:** RL and Bayesian-optimization constructions give upper bounds for link invariants, combined with separately justified lower bounds. The paper gives explicit PD-coded move sequences.

**Evidence status:** source inspected; not independently reproduced

**Inspection depth reported by prior crawl:** primary page or abstract inspected

**External specialist review:** not established in this crawl

**Limitations and correction history:** Link, slice-genus and unknotting-number results are not ordinary Jones detection. No independent execution in this crawl.

**Potential mathematical utility:** Recent reproducible move-generation and verification system.

**Recommended next check — not yet performed:** Read the exact invariant definitions and assumptions; pair the manuscript claims with release S023 and identify which bounds are constructive and which use independent lower-bound inputs.

**Related source IDs:** S023

**Relationship as recorded:** standalone source

**Associated inherited paper records:** P014

**Author-bibliography status:** pending; not exhaustive

**Prior crawl last-checked date:** 2026-11-02

---

<a id="s023"></a>

### S023 — slice-genus-unknotting-rl: v1.0-preprint release

**Priority:** P1

**Primary type:** original_results

**Secondary type/tags:** [not recorded in original crawl]

**Classification basis:** Publishing function of the inspected source; provisional until authoritative taxonomy is recovered

**Type-assignment confidence:** high

**Platform:** GitHub

**Format / publishing role:** versioned original-result and reproducibility release

**Navigation group:** G04 — Computational certificates, reinforcement learning and datasets

**Canonical source URL / original locator:** https://github.com/andras-juhasz/slice-genus-unknotting-rl

**Canonical GitHub repository:** andras-juhasz/slice-genus-unknotting-rl

**Direct manuscript / proof / data URLs:** https://github.com/andras-juhasz/slice-genus-unknotting-rl/releases/tag/v1.0-preprint

**Scholarly authors as recorded:** Yutong Dai; Oliver Hayman; András Juhász; Ludovico Morellato

**Maintainer / operator / publisher:** andras-juhasz; release posted by ludomorellato

**AI contribution:** companion implementation for S022

**Artifact kinds:** code; models; evaluation data; certificates

**Publication / source date:** 2026-10-06 (release)

**Version:** v1.0-preprint; commit shown 2e8e255

**Identifiers:** [not recorded in original crawl]

**Claim or resource as recorded:** Versioned code and data release contains five trained models, dataset splits, evaluation outputs, bound tables, certifying band paths, replay scripts and checksums.

**Evidence status:** source inspected; not independently reproduced

**Inspection depth reported by prior crawl:** primary page or abstract inspected

**External specialist review:** not established in this crawl

**Limitations and correction history:** Release page verified; release ZIPs were not downloaded or replayed. The code repository and manuscript are one research project, not independent confirmations.

**Potential mathematical utility:** One of the strongest recent turnkey archives for independent replay.

**Recommended next check — not yet performed:** Download the pinned v1.0-preprint release, verify published checksums, inspect environments, and replay selected certifying band paths before adopting model heuristics. Record the full commit hash rather than relying on the short prefix.

**Related source IDs:** S022

**Relationship as recorded:** code/data for manuscript S022

**Associated inherited paper records:** P014

**Author-bibliography status:** pending; not exhaustive

**Prior crawl last-checked date:** 2026-11-02

---

<a id="s024"></a>

### S024 — Regina Link engine documentation

**Priority:** P0

**Primary type:** research_infrastructure

**Secondary type/tags:** [not recorded in original crawl]

**Classification basis:** Publishing function of the inspected source; provisional until authoritative taxonomy is recovered

**Type-assignment confidence:** high

**Platform:** website

**Format / publishing role:** official software API documentation

**Navigation group:** G05 — Exact computation, tables, quantum/colored algorithms and uncertain tools

**Canonical source URL / original locator:** https://regina-normal.github.io/engine-docs/classregina_1_1Link.html

**Canonical GitHub repository:** [not recorded in original crawl]

**Direct manuscript / proof / data URLs:** [not recorded in original crawl]

**Scholarly authors as recorded:** pending

**Maintainer / operator / publisher:** Regina project

**AI contribution:** not established

**Artifact kinds:** exact invariant engine; diagram algorithms

**Publication / source date:** [not recorded in original crawl]

**Version:** [not recorded in original crawl]

**Identifiers:** [not recorded in original crawl]

**Claim or resource as recorded:** Exact integer Laurent Jones-polynomial backend and link-diagram methods. Jones exponents use sqrt(t), so returned exponents are doubled relative to t.

**Evidence status:** source inspected; not independently reproduced

**Inspection depth reported by prior crawl:** primary page or abstract inspected

**External specialist review:** not established in this crawl

**Limitations and correction history:** Handedness conventions can invert exponents. A cancelled Jones computation can return a zero polynomial; check completion status. Tool output alone is not novelty assessment.

**Potential mathematical utility:** Independent exact Jones backend and normalization regression tests.

**Recommended next check — not yet performed:** Pin a Regina version; test unknot normalization, both trefoil chiralities, doubled exponents, and cancelled-computation status. Record coefficient ring and whether outputs represent completed exact computations.

**Related source IDs:** [not recorded in original crawl]

**Relationship as recorded:** standalone source

**Associated inherited paper records:** Not indexed in the inherited 25 paper rows; inspect source-specific leads and backlog.

**Author-bibliography status:** pending; not exhaustive

**Prior crawl last-checked date:** 2026-11-02

---

<a id="s025"></a>

### S025 — SnapPy / Spherogram documentation

**Priority:** P0

**Primary type:** research_infrastructure

**Secondary type/tags:** [not recorded in original crawl]

**Classification basis:** Publishing function of the inspected source; provisional until authoritative taxonomy is recovered

**Type-assignment confidence:** high

**Platform:** website

**Format / publishing role:** official documentation

**Navigation group:** G05 — Exact computation, tables, quantum/colored algorithms and uncertain tools

**Canonical source URL / original locator:** https://snappy.computop.org/spherogram.html

**Canonical GitHub repository:** [not recorded in original crawl]

**Direct manuscript / proof / data URLs:** [not recorded in original crawl]

**Scholarly authors as recorded:** pending

**Maintainer / operator / publisher:** SnapPy / Spherogram maintainers

**AI contribution:** not established

**Artifact kinds:** software; PD diagrams; invariants

**Publication / source date:** [not recorded in original crawl]

**Version:** [not recorded in original crawl]

**Identifiers:** [not recorded in original crawl]

**Claim or resource as recorded:** PD-coded link manipulation, simplification and invariant interfaces.

**Evidence status:** source inspected; not independently reproduced

**Inspection depth reported by prior crawl:** primary page or abstract inspected

**External specialist review:** not established in this crawl

**Limitations and correction history:** Failure to simplify does not establish nontriviality. Versions, diagram conventions and optional external backends must be pinned.

**Potential mathematical utility:** Complementary diagram backend; use independent nontriviality certificates.

**Recommended next check — not yet performed:** Pin Spherogram and optional backends; validate signed PD conventions, component count and invariants on the same regression set as Regina. Determine whether two apparent backends share the same implementation.

**Related source IDs:** [not recorded in original crawl]

**Relationship as recorded:** standalone source

**Associated inherited paper records:** Not indexed in the inherited 25 paper rows; inspect source-specific leads and backlog.

**Author-bibliography status:** pending; not exhaustive

**Prior crawl last-checked date:** 2026-11-02

---

<a id="s026"></a>

### S026 — KnotInfo

**Priority:** P1

**Primary type:** research_index

**Secondary type/tags:** [not recorded in original crawl]

**Classification basis:** Publishing function of the inspected source; provisional until authoritative taxonomy is recovered

**Type-assignment confidence:** high

**Platform:** website

**Format / publishing role:** curated invariant database

**Navigation group:** G05 — Exact computation, tables, quantum/colored algorithms and uncertain tools

**Canonical source URL / original locator:** https://knotinfo.math.indiana.edu/

**Canonical GitHub repository:** [not recorded in original crawl]

**Direct manuscript / proof / data URLs:** [not recorded in original crawl]

**Scholarly authors as recorded:** pending

**Maintainer / operator / publisher:** KnotInfo project; individual editors pending

**AI contribution:** not established

**Artifact kinds:** text

**Publication / source date:** [not recorded in original crawl]

**Version:** [not recorded in original crawl]

**Identifiers:** [not recorded in original crawl]

**Claim or resource as recorded:** Curated knot-invariant table, used as a dated baseline by several computational repositories.

**Evidence status:** discovery/reference pointer; direct access failed

**Inspection depth reported by prior crawl:** referenced by inspected primary archives

**External specialist review:** not established in this crawl

**Limitations and correction history:** Direct homepage access failed in this crawl. Freeze a dated table before claiming new invariant values; companion repositories can include results already accepted by the table.

**Potential mathematical utility:** Baseline comparison and small-knot regression data.

**Recommended next check — not yet performed:** Retrieve a dated KnotInfo snapshot and its licensing/provenance; compare baseline dates used by S016 and S017 before counting improvements. Failed homepage access is not absence of data.

**Related source IDs:** [not recorded in original crawl]

**Relationship as recorded:** standalone source

**Associated inherited paper records:** Not indexed in the inherited 25 paper rows; inspect source-specific leads and backlog.

**Author-bibliography status:** pending; not exhaustive

**Prior crawl last-checked date:** 2026-11-02

---

<a id="s027"></a>

### S027 — ParallelJones

**Priority:** P2

**Primary type:** research_infrastructure

**Secondary type/tags:** [not recorded in original crawl]

**Classification basis:** Publishing function of the inspected source; provisional until authoritative taxonomy is recovered

**Type-assignment confidence:** high

**Platform:** GitHub

**Format / publishing role:** paper implementation

**Navigation group:** G05 — Exact computation, tables, quantum/colored algorithms and uncertain tools

**Canonical source URL / original locator:** https://github.com/Parallel-Jones-Polynomial/ParallelJones

**Canonical GitHub repository:** parallel-jones-polynomial/paralleljones

**Direct manuscript / proof / data URLs:** https://arxiv.org/abs/2505.23101

**Scholarly authors as recorded:** Kasturi Barkataki; Eleni Panagiotou

**Maintainer / operator / publisher:** Parallel-Jones-Polynomial organization

**AI contribution:** not established

**Artifact kinds:** text

**Publication / source date:** 2025-05-29 (preprint); 2026-04-21 (journal)

**Version:** [not recorded in original crawl]

**Identifiers:** arXiv:2505.23101; DOI:10.1073/pnas.2520332123

**Claim or resource as recorded:** Parallel Jones-polynomial methods for closed and open curves, with associated paper and code.

**Evidence status:** source inspected; not independently reproduced

**Inspection depth reported by prior crawl:** primary page or abstract inspected

**External specialist review:** not established in this crawl

**Limitations and correction history:** Open-curve functional is not the classical knot invariant. Example numeric coefficients require checking before treating output as an exact integer certificate; no algorithm rerun.

**Potential mathematical utility:** Performance/geometry ideas, with strict exact-arithmetic validation.

**Recommended next check — not yet performed:** Inspect the closed-curve versus open-curve definitions, input geometry, arithmetic and normalization. Determine whether the relevant code yields an exact classical Jones polynomial or a different/approximate quantity.

**Related source IDs:** [not recorded in original crawl]

**Relationship as recorded:** standalone source

**Associated inherited paper records:** P015

**Author-bibliography status:** pending; not exhaustive

**Prior crawl last-checked date:** 2026-11-02

---

<a id="s028"></a>

### S028 — Quantinuum Jones-polynomial quantum algorithms

**Priority:** P2

**Primary type:** research_infrastructure

**Secondary type/tags:** [not recorded in original crawl]

**Classification basis:** Publishing function of the inspected source; provisional until authoritative taxonomy is recovered

**Type-assignment confidence:** high

**Platform:** GitHub

**Format / publishing role:** research implementation

**Navigation group:** G05 — Exact computation, tables, quantum/colored algorithms and uncertain tools

**Canonical source URL / original locator:** https://github.com/Quantinuum/jones-polynomial

**Canonical GitHub repository:** quantinuum/jones-polynomial

**Direct manuscript / proof / data URLs:** https://arxiv.org/abs/2503.05625

**Scholarly authors as recorded:** Tuomas Laakkonen; Enrico Rinaldi; Chris N. Self; Eli Chertkov; Matthew DeCross; David Hayes; Brian Neyenhuis; Marcello Benedetti; Konstantinos Meichanetzidis

**Maintainer / operator / publisher:** Quantinuum

**AI contribution:** not established

**Artifact kinds:** text

**Publication / source date:** 2025

**Version:** [not recorded in original crawl]

**Identifiers:** arXiv:2503.05625

**Claim or resource as recorded:** Code and data for Less Quantum, More Advantage: An End-to-End Quantum Algorithm for the Jones Polynomial.

**Evidence status:** source inspected; not independently reproduced

**Inspection depth reported by prior crawl:** primary page or abstract inspected

**External specialist review:** not established in this crawl

**Limitations and correction history:** Approximate evaluations and quantum resource analysis do not certify equality of an entire integer Laurent polynomial. CQCL/jones-polynomial redirects here and is not a separate result.

**Potential mathematical utility:** Evaluation methods, not exact counterexample certification.

**Recommended next check — not yet performed:** Identify what each algorithm approximates and its error guarantee. Keep evaluation/resource results distinct from full exact Laurent-polynomial identity certificates.

**Related source IDs:** S029

**Relationship as recorded:** standalone source

**Associated inherited paper records:** P016

**Author-bibliography status:** pending; not exhaustive

**Prior crawl last-checked date:** 2026-11-02

---

<a id="s029"></a>

### S029 — CQCL Jones repository alias

**Priority:** P3

**Primary type:** mirror_or_duplicate

**Secondary type/tags:** [not recorded in original crawl]

**Classification basis:** Publishing function of the inspected source; provisional until authoritative taxonomy is recovered

**Type-assignment confidence:** high

**Platform:** GitHub

**Format / publishing role:** redirect

**Navigation group:** G05 — Exact computation, tables, quantum/colored algorithms and uncertain tools

**Canonical source URL / original locator:** https://github.com/CQCL/jones-polynomial

**Canonical GitHub repository:** cqcl/jones-polynomial

**Direct manuscript / proof / data URLs:** [not recorded in original crawl]

**Scholarly authors as recorded:** pending

**Maintainer / operator / publisher:** Former CQCL owner path

**AI contribution:** not established

**Artifact kinds:** text

**Publication / source date:** [not recorded in original crawl]

**Version:** [not recorded in original crawl]

**Identifiers:** [not recorded in original crawl]

**Claim or resource as recorded:** Old owner alias redirects to Quantinuum/jones-polynomial.

**Evidence status:** redirect observed

**Inspection depth reported by prior crawl:** primary page or abstract inspected

**External specialist review:** not established in this crawl

**Limitations and correction history:** Deduplicate with S028; do not count as a second archive or mathematical result.

**Potential mathematical utility:** Preserve historic citations.

**Recommended next check — not yet performed:** Verify the redirect and retain the historical alias to S028; do not process it as an independent research result or count it twice.

**Related source IDs:** S028

**Relationship as recorded:** alias_of S028

**Associated inherited paper records:** Not indexed in the inherited 25 paper rows; inspect source-specific leads and backlog.

**Author-bibliography status:** pending; not exhaustive

**Prior crawl last-checked date:** 2026-11-02

---

<a id="s030"></a>

### S030 — Certified upper bound for the distortion of the trefoil knot

**Priority:** P1

**Primary type:** original_results

**Secondary type/tags:** [not recorded in original crawl]

**Classification basis:** Publishing function of the inspected source; provisional until authoritative taxonomy is recovered

**Type-assignment confidence:** high

**Platform:** Hexagon

**Format / publishing role:** original off-arXiv manuscript

**Navigation group:** G06 — Adjacent knot-geometry, formal, volume and slice-ribbon research

**Canonical source URL / original locator:** https://hexagonmath.org/2611.00012v1

**Canonical GitHub repository:** [not recorded in original crawl]

**Direct manuscript / proof / data URLs:** https://hexagonmath.org/pdf/2611.00012v1 | https://hexagonmath.org/src/2611.00012v1/files

**Scholarly authors as recorded:** David Niedbala Giraudin

**Maintainer / operator / publisher:** Hexagon publisher; author credited in PDF

**AI contribution:** Claude technical assistance credited in manuscript

**Artifact kinds:** PDF; TeX; rational polygon data; Python verifiers

**Publication / source date:** 2026-11-01 (v1/history); 2026-11-02 (listing)

**Version:** v1

**Identifiers:** Hexagon:2611.00012v1 (NOT an arXiv ID)

**Claim or resource as recorded:** Claims a 192-vertex polygonal trefoil with distortion at most 6.92, accompanied by exact/rational and interval-assisted certificate checking material.

**Evidence status:** source inspected; not independently reproduced

**Inspection depth reported by prior crawl:** manuscript inspected with page screenshots; code listing inspected, not executed

**External specialist review:** not established in this crawl

**Limitations and correction history:** No specialist validation was established. Two verifier implementations share construction input and are not fully independent evidence. No claim about Jones unknot detection.

**Potential mathematical utility:** Recent certificate-architecture example for explicit knot geometry.

**Recommended next check — not yet performed:** Retrieve the exact v1 source package and credited authorship/AI statement; validate polygon input, trefoil identification and distortion bound separately. Replay each verifier and identify their shared inputs or assumptions.

**Related source IDs:** [not recorded in original crawl]

**Relationship as recorded:** standalone source

**Associated inherited paper records:** P017

**Author-bibliography status:** pending; not exhaustive

**Prior crawl last-checked date:** 2026-11-02

---

<a id="s031"></a>

### S031 — Gluons and Knots

**Priority:** P2

**Primary type:** original_results

**Secondary type/tags:** [not recorded in original crawl]

**Classification basis:** Publishing function of the inspected source; provisional until authoritative taxonomy is recovered

**Type-assignment confidence:** high

**Platform:** arXiv

**Format / publishing role:** research preprint

**Navigation group:** G06 — Adjacent knot-geometry, formal, volume and slice-ribbon research

**Canonical source URL / original locator:** https://arxiv.org/abs/2610.10673

**Canonical GitHub repository:** [not recorded in original crawl]

**Direct manuscript / proof / data URLs:** https://arxiv.org/html/2610.10673v1

**Scholarly authors as recorded:** Alfredo Guevara

**Maintainer / operator / publisher:** pending

**AI contribution:** not established

**Artifact kinds:** text

**Publication / source date:** 2026-10-07

**Version:** [not recorded in original crawl]

**Identifiers:** arXiv:2610.10673

**Claim or resource as recorded:** Relates a HOMFLY-derived corner-state sum to a single-minus gluon amplitude and supplies a Lean companion.

**Evidence status:** source inspected; not independently reproduced

**Inspection depth reported by prior crawl:** primary page or abstract inspected

**External specialist review:** not established in this crawl

**Limitations and correction history:** Not an ordinary Jones unknot-detection theorem. Formal treatment includes imported literature/contact inputs; compilation alone is not full semantic or independent mathematical validation.

**Potential mathematical utility:** Local-state-sum and Reidemeister-bridge design ideas; audit hypotheses.

**Recommended next check — not yet performed:** Extract the exact HOMFLY/amplitude statement and literature dependencies; distinguish the paper theorem from the scope of the Lean companion S032.

**Related source IDs:** S032

**Relationship as recorded:** standalone source

**Associated inherited paper records:** P018

**Author-bibliography status:** pending; not exhaustive

**Prior crawl last-checked date:** 2026-11-02

---

<a id="s032"></a>

### S032 — Gluon-knot Lean development

**Priority:** P2

**Primary type:** formal_mathematics

**Secondary type/tags:** [not recorded in original crawl]

**Classification basis:** Publishing function of the inspected source; provisional until authoritative taxonomy is recovered

**Type-assignment confidence:** high

**Platform:** GitHub

**Format / publishing role:** formal companion proof artifacts

**Navigation group:** G06 — Adjacent knot-geometry, formal, volume and slice-ribbon research

**Canonical source URL / original locator:** https://github.com/aguevara22/gluon-knot-lean

**Canonical GitHub repository:** aguevara22/gluon-knot-lean

**Direct manuscript / proof / data URLs:** [not recorded in original crawl]

**Scholarly authors as recorded:** Associated manuscript: Alfredo Guevara

**Maintainer / operator / publisher:** aguevara22

**AI contribution:** not established

**Artifact kinds:** Lean; dependency map; imported axioms

**Publication / source date:** [not recorded in original crawl]

**Version:** [not recorded in original crawl]

**Identifiers:** [not recorded in original crawl]

**Claim or resource as recorded:** Lean companion with theorem/dependency inventory; README says its Hypothesis R bridge is proved.

**Evidence status:** source inspected; not independently reproduced

**Inspection depth reported by prior crawl:** primary page or abstract inspected

**External specialist review:** not established in this crawl

**Limitations and correction history:** Do not incorrectly leave Hypothesis R marked open based on older descriptions. Admitted literature inputs including SM.lit_homfly remain. No Jones-detection proof follows.

**Potential mathematical utility:** Inspect the exact algebra-to-Reidemeister bridge and axiom boundary.

**Recommended next check — not yet performed:** Pin the formal source and toolchain, inspect theorem statements and all axioms/admitted inputs, and verify the claimed Hypothesis R change. A successful build is not an independent audit of the topology model.

**Related source IDs:** S031

**Relationship as recorded:** formal companion; not independent confirmation

**Associated inherited paper records:** P018

**Author-bibliography status:** pending; not exhaustive

**Prior crawl last-checked date:** 2026-11-02

---

<a id="s033"></a>

### S033 — Rogers–Ramanujan identities from the geometry of X^a=Y^b

**Priority:** P2

**Primary type:** original_results

**Secondary type/tags:** [not recorded in original crawl]

**Classification basis:** Publishing function of the inspected source; provisional until authoritative taxonomy is recovered

**Type-assignment confidence:** high

**Platform:** arXiv

**Format / publishing role:** research manuscript

**Navigation group:** G06 — Adjacent knot-geometry, formal, volume and slice-ribbon research

**Canonical source URL / original locator:** https://arxiv.org/abs/2609.20567

**Canonical GitHub repository:** [not recorded in original crawl]

**Direct manuscript / proof / data URLs:** https://axiommath.ai/research/publications/

**Scholarly authors as recorded:** Yifeng Huang; Kenny Lau; Ken Ono

**Maintainer / operator / publisher:** pending

**AI contribution:** AxiomProver formal verification assistance

**Artifact kinds:** text

**Publication / source date:** 2026-09-17 (v1); 2026-10-07 (v2)

**Version:** v2, 2026-10-07; supersedes v1 conditional-formalization description

**Identifiers:** arXiv:2609.20567

**Claim or resource as recorded:** Torus-knot singularity and generating-function identities, with AI-assisted formal verification reported by Axiom.

**Evidence status:** v2 primary metadata checked; formalization is author-reported, not rerun

**Inspection depth reported by prior crawl:** primary page or abstract inspected

**External specialist review:** not established in this crawl

**Limitations and correction history:** Version history matters: v1 depended on two literature inputs; the October 7 v2 says these prerequisites have now been formalized and reports an unconditional Lean formalization. Neither the code nor independent specialist assessment was audited here. Not ordinary Jones detection; repository association remains pending.

**Potential mathematical utility:** Adjacent exact q-series and singularity techniques.

**Recommended next check — not yet performed:** Compare v1 and v2 and locate the exact formal repository/release from primary author links. Audit whether the two previously imported prerequisites are discharged in the pinned artifact, not just in the abstract description.

**Related source IDs:** [not recorded in original crawl]

**Relationship as recorded:** standalone source

**Associated inherited paper records:** P019

**Author-bibliography status:** pending; not exhaustive

**Prior crawl last-checked date:** 2026-11-02

---

<a id="s034"></a>

### S034 — ProofAtlas volume conjecture: boundary states

**Priority:** P2

**Primary type:** research_process_archive

**Secondary type/tags:** [not recorded in original crawl]

**Classification basis:** Publishing function of the inspected source; provisional until authoritative taxonomy is recovered

**Type-assignment confidence:** high

**Platform:** website

**Format / publishing role:** research route map

**Navigation group:** G06 — Adjacent knot-geometry, formal, volume and slice-ribbon research

**Canonical source URL / original locator:** https://proofatlas.ai/collaboration/kashaev-murakami-murakami-volume-conjecture-boundary-state/

**Canonical GitHub repository:** [not recorded in original crawl]

**Direct manuscript / proof / data URLs:** [not recorded in original crawl]

**Scholarly authors as recorded:** pending

**Maintainer / operator / publisher:** ProofAtlas

**AI contribution:** AI-oriented research workspace; individual roles unresolved

**Artifact kinds:** text

**Publication / source date:** [not recorded in original crawl]

**Version:** [not recorded in original crawl]

**Identifiers:** [not recorded in original crawl]

**Claim or resource as recorded:** Public route map for volume-conjecture boundary-state methods.

**Evidence status:** source inspected; not independently reproduced

**Inspection depth reported by prior crawl:** discovery page triage

**External specialist review:** not established in this crawl

**Limitations and correction history:** Adjacent colored/volume problem, not ordinary Jones detection. No complete source log or end-to-end proof obtained.

**Potential mathematical utility:** Boundary-state and asymptotic failure records.

**Recommended next check — not yet performed:** Inspect the actual boundary-state proof dependencies and failed routes; record colored-Jones/volume hypotheses and do not import an ordinary-Jones conclusion.

**Related source IDs:** [not recorded in original crawl]

**Relationship as recorded:** standalone source

**Associated inherited paper records:** Not indexed in the inherited 25 paper rows; inspect source-specific leads and backlog.

**Author-bibliography status:** pending; not exhaustive

**Prior crawl last-checked date:** 2026-11-02

---

<a id="s035"></a>

### S035 — ProofAtlas volume conjecture: root-regular transport

**Priority:** P2

**Primary type:** research_process_archive

**Secondary type/tags:** [not recorded in original crawl]

**Classification basis:** Publishing function of the inspected source; provisional until authoritative taxonomy is recovered

**Type-assignment confidence:** high

**Platform:** website

**Format / publishing role:** research route map

**Navigation group:** G06 — Adjacent knot-geometry, formal, volume and slice-ribbon research

**Canonical source URL / original locator:** https://proofatlas.ai/collaboration/kashaev-murakami-murakami-volume-conjecture-root-regular-transport/

**Canonical GitHub repository:** [not recorded in original crawl]

**Direct manuscript / proof / data URLs:** [not recorded in original crawl]

**Scholarly authors as recorded:** pending

**Maintainer / operator / publisher:** ProofAtlas

**AI contribution:** not established

**Artifact kinds:** text

**Publication / source date:** [not recorded in original crawl]

**Version:** [not recorded in original crawl]

**Identifiers:** [not recorded in original crawl]

**Claim or resource as recorded:** Public route map for root-regular transport in a volume-conjecture program.

**Evidence status:** source inspected; not independently reproduced

**Inspection depth reported by prior crawl:** discovery page triage

**External specialist review:** not established in this crawl

**Limitations and correction history:** Outstanding global asymptotic bridges; no ordinary Jones conclusion.

**Potential mathematical utility:** Track local-to-global and root-of-unity limitations.

**Recommended next check — not yet performed:** Identify the unresolved root-regular and global-asymptotic bridges; obtain underlying calculations if public. Keep adjacent asymptotic claims distinct from exact ordinary-Jones detection.

**Related source IDs:** [not recorded in original crawl]

**Relationship as recorded:** standalone source

**Associated inherited paper records:** Not indexed in the inherited 25 paper rows; inspect source-specific leads and backlog.

**Author-bibliography status:** pending; not exhaustive

**Prior crawl last-checked date:** 2026-11-02

---

<a id="s036"></a>

### S036 — ProofAtlas slice-ribbon: R-link / trisection

**Priority:** P2

**Primary type:** research_process_archive

**Secondary type/tags:** [not recorded in original crawl]

**Classification basis:** Publishing function of the inspected source; provisional until authoritative taxonomy is recovered

**Type-assignment confidence:** high

**Platform:** website

**Format / publishing role:** research route map

**Navigation group:** G06 — Adjacent knot-geometry, formal, volume and slice-ribbon research

**Canonical source URL / original locator:** https://proofatlas.ai/collaboration/slice-ribbon-conjecture-r-link-trisection/

**Canonical GitHub repository:** [not recorded in original crawl]

**Direct manuscript / proof / data URLs:** [not recorded in original crawl]

**Scholarly authors as recorded:** pending

**Maintainer / operator / publisher:** ProofAtlas

**AI contribution:** not established

**Artifact kinds:** text

**Publication / source date:** [not recorded in original crawl]

**Version:** [not recorded in original crawl]

**Identifiers:** [not recorded in original crawl]

**Claim or resource as recorded:** Workspace for a slice-ribbon route involving R-links and trisections.

**Evidence status:** source inspected; not independently reproduced

**Inspection depth reported by prior crawl:** discovery page triage

**External specialist review:** not established in this crawl

**Limitations and correction history:** Unresolved general reductions; adjacent knot theory only.

**Potential mathematical utility:** Recorded topological proof obligations.

**Recommended next check — not yet performed:** Obtain the underlying R-link/trisection argument and list its unresolved global reductions; do not infer a general slice-ribbon theorem from a workspace title.

**Related source IDs:** [not recorded in original crawl]

**Relationship as recorded:** standalone source

**Associated inherited paper records:** Not indexed in the inherited 25 paper rows; inspect source-specific leads and backlog.

**Author-bibliography status:** pending; not exhaustive

**Prior crawl last-checked date:** 2026-11-02

---

<a id="s037"></a>

### S037 — ProofAtlas slice-ribbon: Morse concordance

**Priority:** P2

**Primary type:** research_process_archive

**Secondary type/tags:** [not recorded in original crawl]

**Classification basis:** Publishing function of the inspected source; provisional until authoritative taxonomy is recovered

**Type-assignment confidence:** high

**Platform:** website

**Format / publishing role:** research route map

**Navigation group:** G06 — Adjacent knot-geometry, formal, volume and slice-ribbon research

**Canonical source URL / original locator:** https://proofatlas.ai/collaboration/slice-ribbon-conjecture-morse-concordance/

**Canonical GitHub repository:** [not recorded in original crawl]

**Direct manuscript / proof / data URLs:** [not recorded in original crawl]

**Scholarly authors as recorded:** pending

**Maintainer / operator / publisher:** ProofAtlas

**AI contribution:** not established

**Artifact kinds:** text

**Publication / source date:** [not recorded in original crawl]

**Version:** [not recorded in original crawl]

**Identifiers:** [not recorded in original crawl]

**Claim or resource as recorded:** Morse-concordance research route for slice-ribbon questions.

**Evidence status:** source inspected; not independently reproduced

**Inspection depth reported by prior crawl:** discovery page triage

**External specialist review:** not established in this crawl

**Limitations and correction history:** Does not supply an arbitrary slice-disk reduction or Jones detector.

**Potential mathematical utility:** Adjacent geometric proof-process archive.

**Recommended next check — not yet performed:** Obtain actual Morse-concordance notes and track geometric hypotheses at every reduction. Retain as adjacent work unless a concrete Jones connection is established.

**Related source IDs:** [not recorded in original crawl]

**Relationship as recorded:** standalone source

**Associated inherited paper records:** Not indexed in the inherited 25 paper rows; inspect source-specific leads and backlog.

**Author-bibliography status:** pending; not exhaustive

**Prior crawl last-checked date:** 2026-11-02

---

<a id="s038"></a>

### S038 — Hugging Face page for Learning Topological Invariance

**Priority:** P3

**Primary type:** mirror_or_duplicate

**Secondary type/tags:** [not recorded in original crawl]

**Classification basis:** Publishing function of the inspected source; provisional until authoritative taxonomy is recovered

**Type-assignment confidence:** high

**Platform:** Hugging Face

**Format / publishing role:** paper index mirror

**Navigation group:** G07 — Indexes, bibliographies, mirrors and announcements

**Canonical source URL / original locator:** https://huggingface.co/papers/2504.12390

**Canonical GitHub repository:** [not recorded in original crawl]

**Direct manuscript / proof / data URLs:** [not recorded in original crawl]

**Scholarly authors as recorded:** James Halverson; Fabian Ruehle

**Maintainer / operator / publisher:** pending

**AI contribution:** not established

**Artifact kinds:** text

**Publication / source date:** [not recorded in original crawl]

**Version:** [not recorded in original crawl]

**Identifiers:** arXiv:2504.12390

**Claim or resource as recorded:** Paper discovery mirror for S002.

**Evidence status:** source inspected; not independently reproduced

**Inspection depth reported by prior crawl:** primary page or abstract inspected

**External specialist review:** not established in this crawl

**Limitations and correction history:** Not a separate original manuscript or code archive.

**Potential mathematical utility:** Discovery pointer only.

**Recommended next check — not yet performed:** Use only to discover outbound code or author links for S002. Preserve the mirror relationship and do not count a second paper.

**Related source IDs:** S002

**Relationship as recorded:** indexes S002

**Associated inherited paper records:** P001

**Author-bibliography status:** pending; not exhaustive

**Prior crawl last-checked date:** 2026-11-02

---

<a id="s039"></a>

### S039 — Colored Jones from walks: repository lead

**Priority:** P2

**Primary type:** research_infrastructure

**Secondary type/tags:** [not recorded in original crawl]

**Classification basis:** Publishing function of the inspected source; provisional until authoritative taxonomy is recovered

**Type-assignment confidence:** medium

**Platform:** GitHub

**Format / publishing role:** software lead

**Navigation group:** G05 — Exact computation, tables, quantum/colored algorithms and uncertain tools

**Canonical source URL / original locator:** https://github.com/jsflevitt/color-Jones-from-walks

**Canonical GitHub repository:** jsflevitt/color-jones-from-walks

**Direct manuscript / proof / data URLs:** [not recorded in original crawl]

**Scholarly authors as recorded:** Hajij / Levitt association pending primary verification

**Maintainer / operator / publisher:** pending

**AI contribution:** not established

**Artifact kinds:** text

**Publication / source date:** [not recorded in original crawl]

**Version:** [not recorded in original crawl]

**Identifiers:** [not recorded in original crawl]

**Claim or resource as recorded:** Lead for colored-Jones computation by walks; associated literature pointer arXiv:1804.07910.

**Evidence status:** unreviewed discovery lead

**Inspection depth reported by prior crawl:** search/index discovery only

**External specialist review:** not established in this crawl

**Limitations and correction history:** Primary repository and precise author association not fully inspected; pending, not verified.

**Potential mathematical utility:** Possible independent colored-Jones computation.

**Recommended next check — not yet performed:** Confirm repository existence, exact maintainers, manuscript association and the arXiv:1804.07910 lead using primary metadata. Inspect arithmetic, color conventions and examples before running code.

**Related source IDs:** [not recorded in original crawl]

**Relationship as recorded:** standalone source

**Associated inherited paper records:** Not indexed in the inherited 25 paper rows; inspect source-specific leads and backlog.

**Author-bibliography status:** pending; not exhaustive

**Prior crawl last-checked date:** 2026-11-02

---

<a id="s040"></a>

### S040 — Yui knot-homology engine lead

**Priority:** P2

**Primary type:** research_infrastructure

**Secondary type/tags:** [not recorded in original crawl]

**Classification basis:** Publishing function of the inspected source; provisional until authoritative taxonomy is recovered

**Type-assignment confidence:** medium

**Platform:** GitHub

**Format / publishing role:** software lead

**Navigation group:** G05 — Exact computation, tables, quantum/colored algorithms and uncertain tools

**Canonical source URL / original locator:** https://github.com/taketo1024/yui

**Canonical GitHub repository:** taketo1024/yui

**Direct manuscript / proof / data URLs:** https://github.com/taketo1024/yui/blob/main/CLAUDE.md

**Scholarly authors as recorded:** pending

**Maintainer / operator / publisher:** taketo1024

**AI contribution:** not established

**Artifact kinds:** text

**Publication / source date:** [not recorded in original crawl]

**Version:** [not recorded in original crawl]

**Identifiers:** [not recorded in original crawl]

**Claim or resource as recorded:** Rust knot-homology engine with a surfaced CLAUDE.md file.

**Evidence status:** unreviewed discovery lead

**Inspection depth reported by prior crawl:** search discovery

**External specialist review:** not established in this crawl

**Limitations and correction history:** A CLAUDE.md file does not establish AI authorship of a theorem. Code, assertions and mathematical scope remain unreviewed.

**Potential mathematical utility:** Potential homological backend after audit.

**Recommended next check — not yet performed:** Read the implemented knot-homology scope, tests, input conventions and any exactness claims. A CLAUDE.md file alone is not evidence of AI discovery or formal correctness.

**Related source IDs:** [not recorded in original crawl]

**Relationship as recorded:** standalone source

**Associated inherited paper records:** Not indexed in the inherited 25 paper rows; inspect source-specific leads and backlog.

**Author-bibliography status:** pending; not exhaustive

**Prior crawl last-checked date:** 2026-11-02

---

<a id="s041"></a>

### S041 — QLF knot formalization lead

**Priority:** P3

**Primary type:** mixed_other

**Secondary type/tags:** formal_mathematics_candidate

**Classification basis:** Publishing function of the inspected source; provisional until authoritative taxonomy is recovered

**Type-assignment confidence:** low

**Platform:** GitHub

**Format / publishing role:** mixed formalization lead

**Navigation group:** G05 — Exact computation, tables, quantum/colored algorithms and uncertain tools

**Canonical source URL / original locator:** https://github.com/rhovision-org/quantum-logical-framework

**Canonical GitHub repository:** rhovision-org/quantum-logical-framework

**Direct manuscript / proof / data URLs:** https://github.com/rhovision-org/quantum-logical-framework/blob/main/Knot_Theory_QLF.md

**Scholarly authors as recorded:** pending

**Maintainer / operator / publisher:** rhovision-org

**AI contribution:** not established

**Artifact kinds:** text

**Publication / source date:** [not recorded in original crawl]

**Version:** [not recorded in original crawl]

**Identifiers:** [not recorded in original crawl]

**Claim or resource as recorded:** Surfaced knot-theory notes and Kauffman-bracket / knot-invariant Lean file names.

**Evidence status:** unreviewed; scope uncertain

**Inspection depth reported by prior crawl:** search discovery

**External specialist review:** not established in this crawl

**Limitations and correction history:** Unreviewed formalization claim. Need exact theorem, axiom and topological-model inspection; not a certified Jones-detection result.

**Potential mathematical utility:** Retain for axiom audit, not mathematical reliance.

**Recommended next check — not yet performed:** Inspect actual Lean theorem statements, admitted assumptions and the knot model; distinguish formal algebra from ambient-isotopy claims. Retain as uncertain until a relevant theorem is identified.

**Related source IDs:** [not recorded in original crawl]

**Relationship as recorded:** standalone source

**Associated inherited paper records:** Not indexed in the inherited 25 paper rows; inspect source-specific leads and backlog.

**Author-bibliography status:** pending; not exhaustive

**Prior crawl last-checked date:** 2026-11-02

---

<a id="s042"></a>

### S042 — topoKEMP lead

**Priority:** P3

**Primary type:** mixed_other

**Secondary type/tags:** [not recorded in original crawl]

**Classification basis:** Publishing function of the inspected source; provisional until authoritative taxonomy is recovered

**Type-assignment confidence:** low

**Platform:** GitHub

**Format / publishing role:** unreviewed software

**Navigation group:** G05 — Exact computation, tables, quantum/colored algorithms and uncertain tools

**Canonical source URL / original locator:** https://github.com/arccoxx/topoKEMP

**Canonical GitHub repository:** arccoxx/topokemp

**Direct manuscript / proof / data URLs:** [not recorded in original crawl]

**Scholarly authors as recorded:** pending

**Maintainer / operator / publisher:** arccoxx

**AI contribution:** not established

**Artifact kinds:** text

**Publication / source date:** [not recorded in original crawl]

**Version:** [not recorded in original crawl]

**Identifiers:** [not recorded in original crawl]

**Claim or resource as recorded:** Knot recognition / invariant code surfaced during discovery.

**Evidence status:** unreviewed; unsafe certification inference risk

**Inspection depth reported by prior crawl:** search discovery

**External specialist review:** not established in this crawl

**Limitations and correction history:** Surfaced heuristic combines polynomial/volume tests; this must not be accepted as a general unknot certificate. Full code remains unreviewed.

**Potential mathematical utility:** Retained for audit, not recommended as a validator.

**Recommended next check — not yet performed:** Audit every recognition decision and look for heuristic polynomial/volume shortcuts. Do not use this project as a general nontriviality or unknot validator without a justified certificate mechanism.

**Related source IDs:** [not recorded in original crawl]

**Relationship as recorded:** standalone source

**Associated inherited paper records:** Not indexed in the inherited 25 paper rows; inspect source-specific leads and backlog.

**Author-bibliography status:** pending; not exhaustive

**Prior crawl last-checked date:** 2026-11-02

---

<a id="s043"></a>

### S043 — Mini representation / Lie theory repository lead

**Priority:** P3

**Primary type:** mixed_other

**Secondary type/tags:** [not recorded in original crawl]

**Classification basis:** Publishing function of the inspected source; provisional until authoritative taxonomy is recovered

**Type-assignment confidence:** low

**Platform:** GitHub

**Format / publishing role:** unreviewed repository

**Navigation group:** G05 — Exact computation, tables, quantum/colored algorithms and uncertain tools

**Canonical source URL / original locator:** https://github.com/rootkiller6788/mini-representation-lie-theory

**Canonical GitHub repository:** rootkiller6788/mini-representation-lie-theory

**Direct manuscript / proof / data URLs:** [not recorded in original crawl]

**Scholarly authors as recorded:** pending

**Maintainer / operator / publisher:** rootkiller6788

**AI contribution:** not established

**Artifact kinds:** text

**Publication / source date:** [not recorded in original crawl]

**Version:** [not recorded in original crawl]

**Identifiers:** [not recorded in original crawl]

**Claim or resource as recorded:** Broad formal-algebra keyword hit during knot/Jones searches.

**Evidence status:** unreviewed; possible irrelevant hit

**Inspection depth reported by prior crawl:** search discovery

**External specialist review:** not established in this crawl

**Limitations and correction history:** No original Jones or knot theorem established from the retrieved material. Relevance uncertain.

**Potential mathematical utility:** Retain without promoting to a result.

**Recommended next check — not yet performed:** Check whether any genuinely relevant knot/Jones content exists; preserve the record even if it proves irrelevant. Do not infer relevance from formal-algebra keywords.

**Related source IDs:** [not recorded in original crawl]

**Relationship as recorded:** standalone source

**Associated inherited paper records:** Not indexed in the inherited 25 paper rows; inspect source-specific leads and backlog.

**Author-bibliography status:** pending; not exhaustive

**Prior crawl last-checked date:** 2026-11-02

---

<a id="s044"></a>

### S044 — MathDB AJ conjecture page

**Priority:** P2

**Primary type:** problem_incubator

**Secondary type/tags:** [not recorded in original crawl]

**Classification basis:** Publishing function of the inspected source; provisional until authoritative taxonomy is recovered

**Type-assignment confidence:** high

**Platform:** MathDB

**Format / publishing role:** problem page

**Navigation group:** G07 — Indexes, bibliographies, mirrors and announcements

**Canonical source URL / original locator:** https://mathdb.com/p/377946/the-aj-conjecture-for-knots

**Canonical GitHub repository:** [not recorded in original crawl]

**Direct manuscript / proof / data URLs:** [not recorded in original crawl]

**Scholarly authors as recorded:** pending

**Maintainer / operator / publisher:** MathDB

**AI contribution:** not established

**Artifact kinds:** text

**Publication / source date:** [not recorded in original crawl]

**Version:** [not recorded in original crawl]

**Identifiers:** [not recorded in original crawl]

**Claim or resource as recorded:** Problem page for the AJ conjecture.

**Evidence status:** discovery pointer; no proof audited

**Inspection depth reported by prior crawl:** search discovery

**External specialist review:** not established in this crawl

**Limitations and correction history:** Index/problem listing, not verification of a theorem; colored-Jones context differs from the ordinary unknot question.

**Potential mathematical utility:** Outbound bibliography and related problem discovery.

**Recommended next check — not yet performed:** Follow the problem page to original AJ-conjecture papers or attempts; preserve distinctions between the entire colored sequence and the ordinary Jones polynomial.

**Related source IDs:** [not recorded in original crawl]

**Relationship as recorded:** standalone source

**Associated inherited paper records:** Not indexed in the inherited 25 paper rows; inspect source-specific leads and backlog.

**Author-bibliography status:** pending; not exhaustive

**Prior crawl last-checked date:** 2026-11-02

---

<a id="s045"></a>

### S045 — MathDB complexified volume conjecture page

**Priority:** P2

**Primary type:** problem_incubator

**Secondary type/tags:** [not recorded in original crawl]

**Classification basis:** Publishing function of the inspected source; provisional until authoritative taxonomy is recovered

**Type-assignment confidence:** high

**Platform:** MathDB

**Format / publishing role:** problem page

**Navigation group:** G07 — Indexes, bibliographies, mirrors and announcements

**Canonical source URL / original locator:** https://mathdb.com/p/345378/complexified-volume-conjecture-for-hyperbolic-knots

**Canonical GitHub repository:** [not recorded in original crawl]

**Direct manuscript / proof / data URLs:** [not recorded in original crawl]

**Scholarly authors as recorded:** pending

**Maintainer / operator / publisher:** MathDB

**AI contribution:** not established

**Artifact kinds:** text

**Publication / source date:** [not recorded in original crawl]

**Version:** [not recorded in original crawl]

**Identifiers:** [not recorded in original crawl]

**Claim or resource as recorded:** Problem page for a complexified volume conjecture.

**Evidence status:** discovery pointer; no proof audited

**Inspection depth reported by prior crawl:** search discovery

**External specialist review:** not established in this crawl

**Limitations and correction history:** No Jones unknot theorem follows from an index entry.

**Potential mathematical utility:** Related asymptotic invariant bibliography.

**Recommended next check — not yet performed:** Follow primary references and verify exact complexified-volume hypotheses; treat the page as a discovery pointer rather than theorem evidence.

**Related source IDs:** [not recorded in original crawl]

**Relationship as recorded:** standalone source

**Associated inherited paper records:** Not indexed in the inherited 25 paper rows; inspect source-specific leads and backlog.

**Author-bibliography status:** pending; not exhaustive

**Prior crawl last-checked date:** 2026-11-02

---

<a id="s046"></a>

### S046 — Awesome AI for Math index

**Priority:** P2

**Primary type:** research_index

**Secondary type/tags:** [not recorded in original crawl]

**Classification basis:** Publishing function of the inspected source; provisional until authoritative taxonomy is recovered

**Type-assignment confidence:** high

**Platform:** GitHub

**Format / publishing role:** curated index

**Navigation group:** G07 — Indexes, bibliographies, mirrors and announcements

**Canonical source URL / original locator:** https://github.com/seewoo5/awesome-ai-for-math

**Canonical GitHub repository:** seewoo5/awesome-ai-for-math

**Direct manuscript / proof / data URLs:** [not recorded in original crawl]

**Scholarly authors as recorded:** pending

**Maintainer / operator / publisher:** seewoo5

**AI contribution:** not established

**Artifact kinds:** text

**Publication / source date:** [not recorded in original crawl]

**Version:** [not recorded in original crawl]

**Identifiers:** [not recorded in original crawl]

**Claim or resource as recorded:** Community AI/mathematics index with knot-related literature pointers.

**Evidence status:** index inspected at discovery level

**Inspection depth reported by prior crawl:** search/index triage

**External specialist review:** not established in this crawl

**Limitations and correction history:** Compilation, not an original proof. Outbound knot bibliography only partially followed.

**Potential mathematical utility:** Additional backfill across older ML knot papers.

**Recommended next check — not yet performed:** Extract knot-related outbound links, canonicalize them and inspect each primary source before adding claims. Do not cite the compilation as proof.

**Related source IDs:** [not recorded in original crawl]

**Relationship as recorded:** standalone source

**Associated inherited paper records:** Not indexed in the inherited 25 paper rows; inspect source-specific leads and backlog.

**Author-bibliography status:** pending; not exhaustive

**Prior crawl last-checked date:** 2026-11-02

---

<a id="s047"></a>

### S047 — Advancing mathematics by guiding human intuition with AI

**Priority:** P2

**Primary type:** original_results

**Secondary type/tags:** [not recorded in original crawl]

**Classification basis:** Publishing function of the inspected source; provisional until authoritative taxonomy is recovered

**Type-assignment confidence:** high

**Platform:** journal

**Format / publishing role:** published research article

**Navigation group:** G08 — Broader AI/topology research and follow-up manuscripts

**Canonical source URL / original locator:** https://www.nature.com/articles/s41586-021-04086-x

**Canonical GitHub repository:** [not recorded in original crawl]

**Direct manuscript / proof / data URLs:** [not recorded in original crawl]

**Scholarly authors as recorded:** Alex Davies et al.; complete credited list in primary paper

**Maintainer / operator / publisher:** pending

**AI contribution:** AI-guided conjecture discovery; human mathematical work

**Artifact kinds:** text

**Publication / source date:** 2021

**Version:** [not recorded in original crawl]

**Identifiers:** DOI:10.1038/s41586-021-04086-x

**Claim or resource as recorded:** AI-guided mathematics paper includes a knot-theory relationship between signature and hyperbolic geometric data, followed by mathematical analysis.

**Evidence status:** source inspected; not independently reproduced

**Inspection depth reported by prior crawl:** primary article search text; not full proof audit

**External specialist review:** published in Nature

**Limitations and correction history:** Historical 2021 work, not a new Jones-detection result. Exact theorem and complete bibliography should be checked before reuse.

**Potential mathematical utility:** Model for converting learned structure into an explicit theorem.

**Recommended next check — not yet performed:** Retrieve the complete credited author list and exact knot-theory theorem; separate learned conjecture generation from the mathematical proof and check reusable geometric/signature ingredients.

**Related source IDs:** [not recorded in original crawl]

**Relationship as recorded:** standalone source

**Associated inherited paper records:** P020

**Author-bibliography status:** pending; not exhaustive

**Prior crawl last-checked date:** 2026-11-02

---

<a id="s048"></a>

### S048 — Variational autoencoders understand knot topology

**Priority:** P2

**Primary type:** original_results

**Secondary type/tags:** [not recorded in original crawl]

**Classification basis:** Publishing function of the inspected source; provisional until authoritative taxonomy is recovered

**Type-assignment confidence:** high

**Platform:** arXiv / journal

**Format / publishing role:** research manuscript

**Navigation group:** G08 — Broader AI/topology research and follow-up manuscripts

**Canonical source URL / original locator:** https://arxiv.org/abs/2504.04179

**Canonical GitHub repository:** [not recorded in original crawl]

**Direct manuscript / proof / data URLs:** [not recorded in original crawl]

**Scholarly authors as recorded:** Anna Braghetto; Sumanta Kundu; Marco Baiesi; Enzo Orlandini

**Maintainer / operator / publisher:** pending

**AI contribution:** variational autoencoders

**Artifact kinds:** text

**Publication / source date:** 2025

**Version:** [not recorded in original crawl]

**Identifiers:** arXiv:2504.04179; DOI:10.1103/mdpw-lvcy

**Claim or resource as recorded:** Machine-learning representation/classification research for knot topology.

**Evidence status:** source inspected; not independently reproduced

**Inspection depth reported by prior crawl:** primary metadata/abstract discovery

**External specialist review:** not established in this crawl

**Limitations and correction history:** Not an exact topological certificate or Jones-detection theorem. Discovery-level review.

**Potential mathematical utility:** Potential candidate-space exploration, with separate certification.

**Recommended next check — not yet performed:** Verify full primary metadata and DOI association, retrieve code/data if author-linked, and distinguish learned topology classification from exact mathematical certification.

**Related source IDs:** [not recorded in original crawl]

**Relationship as recorded:** standalone source

**Associated inherited paper records:** P021

**Author-bibliography status:** pending; not exhaustive

**Prior crawl last-checked date:** 2026-11-02

---

<a id="s049"></a>

### S049 — Fabian Ruehle publication list

**Priority:** P2

**Primary type:** research_index

**Secondary type/tags:** [not recorded in original crawl]

**Classification basis:** Publishing function of the inspected source; provisional until authoritative taxonomy is recovered

**Type-assignment confidence:** high

**Platform:** website

**Format / publishing role:** author bibliography

**Navigation group:** G07 — Indexes, bibliographies, mirrors and announcements

**Canonical source URL / original locator:** https://ruehlef.github.io/research.html

**Canonical GitHub repository:** [not recorded in original crawl]

**Direct manuscript / proof / data URLs:** [not recorded in original crawl]

**Scholarly authors as recorded:** Fabian Ruehle (author site)

**Maintainer / operator / publisher:** Fabian Ruehle

**AI contribution:** not established

**Artifact kinds:** text

**Publication / source date:** [not recorded in original crawl]

**Version:** [not recorded in original crawl]

**Identifiers:** [not recorded in original crawl]

**Claim or resource as recorded:** Author bibliography links Learning Topological Invariance and a later Z-hat-invariant paper.

**Evidence status:** source inspected; not independently reproduced

**Inspection depth reported by prior crawl:** primary page or abstract inspected

**External specialist review:** not established in this crawl

**Limitations and correction history:** Follow-up bibliography incomplete; later manuscript not deeply inspected. Do not infer all outputs are Jones-related.

**Potential mathematical utility:** Author-associated outputs beyond the original repository search.

**Recommended next check — not yet performed:** Check the complete author bibliography and official code links for S002 and S050; preserve pending status for unsearched outputs and do not infer coauthors from site ownership.

**Related source IDs:** S002;S050

**Relationship as recorded:** standalone source

**Associated inherited paper records:** Not indexed in the inherited 25 paper rows; inspect source-specific leads and backlog.

**Author-bibliography status:** pending; not exhaustive

**Prior crawl last-checked date:** 2026-11-02

---

<a id="s050"></a>

### S050 — Learning Topological Features of Z-hat Invariants

**Priority:** P2

**Primary type:** original_results

**Secondary type/tags:** [not recorded in original crawl]

**Classification basis:** Publishing function of the inspected source; provisional until authoritative taxonomy is recovered

**Type-assignment confidence:** medium

**Platform:** arXiv

**Format / publishing role:** manuscript lead

**Navigation group:** G08 — Broader AI/topology research and follow-up manuscripts

**Canonical source URL / original locator:** https://arxiv.org/abs/2608.18570

**Canonical GitHub repository:** [not recorded in original crawl]

**Direct manuscript / proof / data URLs:** [not recorded in original crawl]

**Scholarly authors as recorded:** Pending primary metadata verification; linked from Fabian Ruehle bibliography

**Maintainer / operator / publisher:** pending

**AI contribution:** ML according to bibliography lead

**Artifact kinds:** text

**Publication / source date:** 2026-08

**Version:** [not recorded in original crawl]

**Identifiers:** arXiv:2608.18570

**Claim or resource as recorded:** Author-bibliography lead for ML and plumbed-three-manifold invariants.

**Evidence status:** unreviewed author-associated manuscript lead

**Inspection depth reported by prior crawl:** author bibliography discovery

**External specialist review:** not established in this crawl

**Limitations and correction history:** Full author list, exact theorems, data and code association pending. Adjacent three-manifold work, not ordinary Jones detection.

**Potential mathematical utility:** Backfill lead for broader quantum-topology learning.

**Recommended next check — not yet performed:** Resolve complete primary author metadata, exact claims, version and any code/data link. Classify relevance only after reviewing the plumbed-three-manifold setting.

**Related source IDs:** S049

**Relationship as recorded:** standalone source

**Associated inherited paper records:** P022

**Author-bibliography status:** pending; not exhaustive

**Prior crawl last-checked date:** 2026-11-02

---

<a id="s051"></a>

### S051 — University of Sydney braid seminar announcement

**Priority:** P2

**Primary type:** mixed_other

**Secondary type/tags:** [not recorded in original crawl]

**Classification basis:** Publishing function of the inspected source; provisional until authoritative taxonomy is recovered

**Type-assignment confidence:** high

**Platform:** website

**Format / publishing role:** seminar announcement

**Navigation group:** G07 — Indexes, bibliographies, mirrors and announcements

**Canonical source URL / original locator:** https://www.maths.usyd.edu.au/s/scnitm/cmeister-InformalFridaySeminar-Wil

**Canonical GitHub repository:** [not recorded in original crawl]

**Direct manuscript / proof / data URLs:** [not recorded in original crawl]

**Scholarly authors as recorded:** Speaker: Geordie Williamson; paper authorship not inferred

**Maintainer / operator / publisher:** University of Sydney

**AI contribution:** not established

**Artifact kinds:** text

**Publication / source date:** 2026-03-06

**Version:** [not recorded in original crawl]

**Identifiers:** [not recorded in original crawl]

**Claim or resource as recorded:** Official March 2026 seminar announcement involving braid/representation research.

**Evidence status:** primary announcement only

**Inspection depth reported by prior crawl:** primary page or abstract inspected

**External specialist review:** not established in this crawl

**Limitations and correction history:** Announcement only; associated proof archive and exact claims not established. Do not promote a talk abstract to a theorem.

**Potential mathematical utility:** Expert-route discovery and bibliography follow-up.

**Recommended next check — not yet performed:** Follow the official announcement to an actual paper or notes with explicit authorship; do not infer a theorem from a seminar abstract or speaker identity.

**Related source IDs:** [not recorded in original crawl]

**Relationship as recorded:** standalone source

**Associated inherited paper records:** Not indexed in the inherited 25 paper rows; inspect source-specific leads and backlog.

**Author-bibliography status:** pending; not exhaustive

**Prior crawl last-checked date:** 2026-11-02

---

<a id="s052"></a>

### S052 — George Washington Jones hypothesis speculative talk

**Priority:** P3

**Primary type:** mixed_other

**Secondary type/tags:** [not recorded in original crawl]

**Classification basis:** Publishing function of the inspected source; provisional until authoritative taxonomy is recovered

**Type-assignment confidence:** high

**Platform:** website

**Format / publishing role:** seminar announcement

**Navigation group:** G07 — Indexes, bibliographies, mirrors and announcements

**Canonical source URL / original locator:** https://math.columbian.gwu.edu/distinguished-speculative-first-april-talk-and-university-seminar-speculations-jones-hypothesis

**Canonical GitHub repository:** [not recorded in original crawl]

**Direct manuscript / proof / data URLs:** [not recorded in original crawl]

**Scholarly authors as recorded:** Speaker: Anzor Beridze; paper authorship not inferred

**Maintainer / operator / publisher:** George Washington University

**AI contribution:** not established

**Artifact kinds:** text

**Publication / source date:** 2026-04-01

**Version:** [not recorded in original crawl]

**Identifiers:** [not recorded in original crawl]

**Claim or resource as recorded:** Official speculative seminar announcement on the Jones hypothesis.

**Evidence status:** primary announcement only

**Inspection depth reported by prior crawl:** primary page or abstract inspected

**External specialist review:** not established in this crawl

**Limitations and correction history:** No proof or independent assessment inferred from announcement.

**Potential mathematical utility:** Low-priority route/bibliography lead.

**Recommended next check — not yet performed:** Look for an actual manuscript and mathematical argument, with its stated speculative status preserved. Do not promote the April 1 seminar announcement to a proof.

**Related source IDs:** [not recorded in original crawl]

**Relationship as recorded:** standalone source

**Associated inherited paper records:** Not indexed in the inherited 25 paper rows; inspect source-specific leads and backlog.

**Author-bibliography status:** pending; not exhaustive

**Prior crawl last-checked date:** 2026-11-02

---

<a id="s053"></a>

### S053 — Invariants for Turaev genus one links

**Priority:** P2

**Primary type:** original_results

**Secondary type/tags:** [not recorded in original crawl]

**Classification basis:** Publishing function of the inspected source; provisional until authoritative taxonomy is recovered

**Type-assignment confidence:** high

**Platform:** arXiv

**Format / publishing role:** research manuscript

**Navigation group:** G03 — Established boundaries, structural classes and stronger invariants

**Canonical source URL / original locator:** https://arxiv.org/abs/1604.03501

**Canonical GitHub repository:** [not recorded in original crawl]

**Direct manuscript / proof / data URLs:** [not recorded in original crawl]

**Scholarly authors as recorded:** Oliver T. Dasbach; Adam M. Lowrance

**Maintainer / operator / publisher:** pending

**AI contribution:** not established

**Artifact kinds:** text

**Publication / source date:** 2016

**Version:** [not recorded in original crawl]

**Identifiers:** arXiv:1604.03501

**Claim or resource as recorded:** Invariants and coefficient restrictions for a low-Turaev-genus class.

**Evidence status:** source inspected; not independently reproduced

**Inspection depth reported by prior crawl:** primary abstract discovery

**External specialist review:** not established in this crawl

**Limitations and correction history:** A leading or trailing coefficient of absolute value one alone does not imply a nonconstant polynomial. Exact scope needs full-text review before reuse.

**Potential mathematical utility:** Structural classes and coefficient restrictions.

**Recommended next check — not yet performed:** Read the full theorem and hypotheses; determine exactly what endpoint-coefficient restrictions imply. A coefficient of absolute value one alone does not imply a nonconstant polynomial.

**Related source IDs:** [not recorded in original crawl]

**Relationship as recorded:** standalone source

**Associated inherited paper records:** P023

**Author-bibliography status:** pending; not exhaustive

**Prior crawl last-checked date:** 2026-11-02

---

<a id="s054"></a>

### S054 — Khovanov homology of the 2-cable detects the unknot

**Priority:** P2

**Primary type:** original_results

**Secondary type/tags:** [not recorded in original crawl]

**Classification basis:** Publishing function of the inspected source; provisional until authoritative taxonomy is recovered

**Type-assignment confidence:** high

**Platform:** arXiv

**Format / publishing role:** research theorem manuscript

**Navigation group:** G03 — Established boundaries, structural classes and stronger invariants

**Canonical source URL / original locator:** https://arxiv.org/abs/0805.4418

**Canonical GitHub repository:** [not recorded in original crawl]

**Direct manuscript / proof / data URLs:** [not recorded in original crawl]

**Scholarly authors as recorded:** Matthew Hedden

**Maintainer / operator / publisher:** pending

**AI contribution:** not established

**Artifact kinds:** text

**Publication / source date:** 2008

**Version:** [not recorded in original crawl]

**Identifiers:** arXiv:0805.4418

**Claim or resource as recorded:** Homological unknot-detection result for a cable.

**Evidence status:** source inspected; not independently reproduced

**Inspection depth reported by prior crawl:** primary abstract discovery

**External specialist review:** not established in this crawl

**Limitations and correction history:** The result concerns Khovanov homology, not the ordinary or colored Jones polynomial alone.

**Potential mathematical utility:** Additional independent homological detection route.

**Recommended next check — not yet performed:** Extract the exact cable, coefficient and homology hypotheses; do not replace the detecting homology by the ordinary or colored polynomial.

**Related source IDs:** [not recorded in original crawl]

**Relationship as recorded:** standalone source

**Associated inherited paper records:** P024

**Author-bibliography status:** pending; not exhaustive

**Prior crawl last-checked date:** 2026-11-02

---

<a id="s055"></a>

### S055 — On the Colored Jones Polynomial, Sutured Floer homology, and Knot Floer homology

**Priority:** P2

**Primary type:** original_results

**Secondary type/tags:** [not recorded in original crawl]

**Classification basis:** Publishing function of the inspected source; provisional until authoritative taxonomy is recovered

**Type-assignment confidence:** high

**Platform:** arXiv

**Format / publishing role:** research theorem manuscript

**Navigation group:** G03 — Established boundaries, structural classes and stronger invariants

**Canonical source URL / original locator:** https://arxiv.org/abs/0807.1432

**Canonical GitHub repository:** [not recorded in original crawl]

**Direct manuscript / proof / data URLs:** [not recorded in original crawl]

**Scholarly authors as recorded:** J. Elisenda Grigsby; Stephan Wehrli

**Maintainer / operator / publisher:** pending

**AI contribution:** not established

**Artifact kinds:** text

**Publication / source date:** 2008-07-09

**Version:** [not recorded in original crawl]

**Identifiers:** arXiv:0807.1432

**Claim or resource as recorded:** Unknot detection by a colored-Jones categorification under the paper’s color hypotheses.

**Evidence status:** source inspected; not independently reproduced

**Inspection depth reported by prior crawl:** primary abstract discovery

**External specialist review:** not established in this crawl

**Limitations and correction history:** Do not replace categorification by the polynomial itself; exact coefficients and conventions require full-text review.

**Potential mathematical utility:** Stronger-invariant comparison; guards against conflation.

**Recommended next check — not yet performed:** Read the categorification theorem and its color/coefficient restrictions; distinguish the categorical invariant from its polynomial Euler characteristic.

**Related source IDs:** [not recorded in original crawl]

**Relationship as recorded:** standalone source

**Associated inherited paper records:** P025

**Author-bibliography status:** pending; not exhaustive

**Prior crawl last-checked date:** 2026-11-02

---

<a id="s056"></a>

### S056 — Trefoil distortion lower-bound Zenodo lead

**Priority:** P2

**Primary type:** original_results

**Secondary type/tags:** [not recorded in original crawl]

**Classification basis:** Publishing function of the inspected source; provisional until authoritative taxonomy is recovered

**Type-assignment confidence:** medium

**Platform:** Zenodo

**Format / publishing role:** manuscript lead

**Navigation group:** G06 — Adjacent knot-geometry, formal, volume and slice-ribbon research

**Canonical source URL / original locator:** https://zenodo.org/records/22759451

**Canonical GitHub repository:** [not recorded in original crawl]

**Direct manuscript / proof / data URLs:** [not recorded in original crawl]

**Scholarly authors as recorded:** A. Schoen as cited; primary creator metadata pending

**Maintainer / operator / publisher:** pending

**AI contribution:** not established

**Artifact kinds:** text

**Publication / source date:** 2026-09-14 (v2 date as cited, unverified)

**Version:** [not recorded in original crawl]

**Identifiers:** Zenodo record:22759451; DOI not independently verified

**Claim or resource as recorded:** Lower-bound manuscript cited by the Hexagon trefoil distortion note.

**Evidence status:** unreviewed cited manuscript

**Inspection depth reported by prior crawl:** citation in S030 only

**External specialist review:** not established in this crawl

**Limitations and correction history:** Citation-following lead only; creator name, version, exact lower bound and independent review remain pending. Do not treat the cited claim as checked.

**Potential mathematical utility:** Related explicit knot-geometry certificate research.

**Recommended next check — not yet performed:** Open the cited Zenodo record and check creator metadata, version history, DOI, files and exact lower bound. Do not manufacture a DOI from the record number or silently upgrade a citation-only lead.

**Related source IDs:** S030

**Relationship as recorded:** standalone source

**Associated inherited paper records:** Not indexed in the inherited 25 paper rows; inspect source-specific leads and backlog.

**Author-bibliography status:** pending; not exhaustive

**Prior crawl last-checked date:** 2026-11-02

---


## 5. Full paper inventory — all 25 inherited identifier records

The received document attributes these rows to `original_crawl/papers.csv`, which is not present in this recovered bundle. The local P IDs are navigation keys. Paper/repository/mirror associations do not establish independent confirmation.

### P001 — Learning Topological Invariance

**canonical_paper_key:** arxiv:2504.12390

**title:** Learning Topological Invariance

**identifiers:** arXiv:2504.12390

**scholarly_authors:** James Halverson; Fabian Ruehle

**maintainer_or_publisher:** pending

**date:** 2025-04-16

**version:** v1 inspected

**canonical_url:** https://arxiv.org/abs/2504.12390

**direct_manuscript_or_data_urls:** https://arxiv.org/html/2504.12390v1

**associated_source_ids:** S002;S038

**association_evidence:** standalone source; primary page or abstract inspected

**evidence_status:** source inspected; not independently reproduced

**limitations:** Negative finite search, not proof of detection. Author-released code association remains pending; generic cited software must not be assigned to these authors.

**author_bibliography_status:** pending; not exhaustive

---

### P002 — The Unknotting Number, Hard Unknot Diagrams, and Reinforcement Learning

**canonical_paper_key:** arxiv:2409.09032

**title:** The Unknotting Number, Hard Unknot Diagrams, and Reinforcement Learning

**identifiers:** arXiv:2409.09032; DOI:10.1080/10586458.2025.2542174

**scholarly_authors:** Taylor Applebaum; Sam Blackwell; Alex Davies; Thomas Edlich; András Juhász; Marc Lackenby; Nenad Tomašev; Daniel Zheng

**maintainer_or_publisher:** DeepMind / Oxford research collaboration; Taylor & Francis publisher

**date:** 2025-08-18 (publication); 2024-09-13 (initial preprint)

**version:** [not recorded in original crawl]

**canonical_url:** https://arxiv.org/abs/2409.09032

**direct_manuscript_or_data_urls:** https://arxiv.org/abs/2409.09032 | gs://gdm-unknotting

**associated_source_ids:** S003

**association_evidence:** standalone source; primary page or abstract inspected

**evidence_status:** source inspected; not independently reproduced

**limitations:** Failure of simplification is not a nontriviality certificate. Some separate unknotting-number values in this work are conditional on additivity. Indexed publisher text was available; direct publisher open returned 403. Bucket files were not downloaded.

**author_bibliography_status:** pending; not exhaustive

---

### P003 — On trivial Jones--Vassiliev polynomials

**canonical_paper_key:** arxiv:2606.22410

**title:** On trivial Jones--Vassiliev polynomials

**identifiers:** arXiv:2606.22410

**scholarly_authors:** Avishy Carmi; Eliahu Cohen

**maintainer_or_publisher:** pending

**date:** 2026-06-21

**version:** June 21 manuscript inspected; later version status pending

**canonical_url:** https://arxiv.org/abs/2606.22410

**direct_manuscript_or_data_urls:** [not recorded in original crawl]

**associated_source_ids:** S005

**association_evidence:** standalone source; primary page or abstract inspected

**evidence_status:** general proof claim; substantive objection in user audit

**limitations:** The user’s October 31 audit challenges the Section 5 uniform compression package with an explicit twist family. No independent validation of the general claim was located. Latest version/correction status not fully resolved.

**author_bibliography_status:** pending; not exhaustive

---

### P004 — Does the Jones polynomial detect the unknot?

**canonical_paper_key:** arxiv:math/0012086

**title:** Does the Jones polynomial detect the unknot?

**identifiers:** arXiv:math/0012086; DOI:10.1142/S0218216502001779

**scholarly_authors:** Stephen Bigelow

**maintainer_or_publisher:** pending

**date:** 2000-12-12 (preprint); 2002 (journal)

**version:** [not recorded in original crawl]

**canonical_url:** https://arxiv.org/abs/math/0012086

**direct_manuscript_or_data_urls:** [not recorded in original crawl]

**associated_source_ids:** S007

**association_evidence:** standalone source; primary page or abstract inspected

**evidence_status:** source inspected; not independently reproduced

**limitations:** Historical program; do not treat its conjectural implications as stronger than later proved statements. Compare Ito’s precise result.

**author_bibliography_status:** pending; not exhaustive

---

### P005 — A kernel of a braid group representation yields a knot with trivial knot polynomials

**canonical_paper_key:** arxiv:1402.2028

**title:** A kernel of a braid group representation yields a knot with trivial knot polynomials

**identifiers:** arXiv:1402.2028; DOI:10.1007/s00209-015-1426-7

**scholarly_authors:** Tetsuya Ito

**maintainer_or_publisher:** pending

**date:** 2014-02-10 (preprint); 2015 (journal)

**version:** [not recorded in original crawl]

**canonical_url:** https://arxiv.org/abs/1402.2028

**direct_manuscript_or_data_urls:** [not recorded in original crawl]

**associated_source_ids:** S008

**association_evidence:** standalone source; full text and exact corollary inspected

**evidence_status:** source inspected; not independently reproduced

**limitations:** The implication is one-way. Faithfulness is not a proof that a trace-valued closure invariant detects the unknot.

**author_bibliography_status:** pending; not exhaustive

---

### P006 — The Burau representation of the braid group is faithful for n = 4

**canonical_paper_key:** arxiv:2607.05283

**title:** The Burau representation of the braid group is faithful for n = 4

**identifiers:** arXiv:2607.05283

**scholarly_authors:** Vasudha Bharathram; Joan S. Birman; Tara E. Brendle

**maintainer_or_publisher:** pending

**date:** 2026-07-06 (initial submission)

**version:** retrieved July manuscript; revision history pending

**canonical_url:** https://arxiv.org/abs/2607.05283

**direct_manuscript_or_data_urls:** [not recorded in original crawl]

**associated_source_ids:** S009

**association_evidence:** standalone source; primary page or abstract inspected

**evidence_status:** source inspected; not independently reproduced

**limitations:** Independent specialist acceptance and latest revision status were not established. Even if correct, this blocks one kernel strategy, not all Jones counterexamples and not trace collisions.

**author_bibliography_status:** pending; not exhaustive

---

### P007 — Closed 4-braids and the Jones unknot conjecture

**canonical_paper_key:** arxiv:2402.02553

**title:** Closed 4-braids and the Jones unknot conjecture

**identifiers:** arXiv:2402.02553

**scholarly_authors:** Dmitriy Korzun; Elena Lanina; Alexey Sleptsov

**maintainer_or_publisher:** pending

**date:** 2024

**version:** v2, 2024-04-18

**canonical_url:** https://arxiv.org/abs/2402.02553

**direct_manuscript_or_data_urls:** [not recorded in original crawl]

**associated_source_ids:** S010

**association_evidence:** standalone source; primary page or abstract inspected

**evidence_status:** source inspected; not independently reproduced

**limitations:** A compatible formal polynomial is not an actual realizable nontrivial knot. Abstract-level triage, not full theorem audit.

**author_bibliography_status:** pending; not exhaustive

---

### P008 — Verification of the Jones unknot conjecture up to 24 crossings

**canonical_paper_key:** arxiv:2003.06724

**title:** Verification of the Jones unknot conjecture up to 24 crossings

**identifiers:** arXiv:2003.06724; DOI:10.1142/S0218216521500206

**scholarly_authors:** Robert E. Tuzun; Adam S. Sikora

**maintainer_or_publisher:** pending

**date:** 2020-03-15 (initial); 2021 (journal)

**version:** v2, 2021-03-23

**canonical_url:** https://arxiv.org/abs/2003.06724

**direct_manuscript_or_data_urls:** [not recorded in original crawl]

**associated_source_ids:** S011

**association_evidence:** standalone source; primary page or abstract inspected

**evidence_status:** source inspected; not independently reproduced

**limitations:** Finite crossing range, not all knots. Enumeration and implementation were not rerun in this crawl.

**author_bibliography_status:** pending; not exhaustive

---

### P009 — Khovanov homology is an unknot-detector

**canonical_paper_key:** arxiv:1005.4346

**title:** Khovanov homology is an unknot-detector

**identifiers:** arXiv:1005.4346

**scholarly_authors:** P. B. Kronheimer; T. S. Mrowka

**maintainer_or_publisher:** pending

**date:** 2010 (preprint); 2011 (journal)

**version:** [not recorded in original crawl]

**canonical_url:** https://arxiv.org/abs/1005.4346

**direct_manuscript_or_data_urls:** [not recorded in original crawl]

**associated_source_ids:** S012

**association_evidence:** standalone source; primary page or abstract inspected

**evidence_status:** source inspected; not independently reproduced

**limitations:** Cannot be replaced by the statement that its graded Euler characteristic, the Jones polynomial, detects the unknot. Homological information may cancel.

**author_bibliography_status:** pending; not exhaustive

---

### P010 — On the modular Jones polynomial

**canonical_paper_key:** arxiv:2008.00716

**title:** On the modular Jones polynomial

**identifiers:** arXiv:2008.00716; DOI:10.5802/crmath.106

**scholarly_authors:** Guillaume Pagel

**maintainer_or_publisher:** pending

**date:** 2020

**version:** [not recorded in original crawl]

**canonical_url:** https://arxiv.org/abs/2008.00716

**direct_manuscript_or_data_urls:** [not recorded in original crawl]

**associated_source_ids:** S014

**association_evidence:** standalone source; full primary text inspected

**evidence_status:** source inspected; not independently reproduced

**limitations:** Congruence modulo an integer is not equality over Z[t,t^-1]. Do not assume a bounded list of modular tests settles exact triviality.

**author_bibliography_status:** pending; not exhaustive

---

### P011 — From knots to four-manifolds

**canonical_paper_key:** arxiv:2601.05425

**title:** From knots to four-manifolds

**identifiers:** arXiv:2601.05425

**scholarly_authors:** Ciprian Manolescu

**maintainer_or_publisher:** pending

**date:** 2026

**version:** v2, 2026-03-29

**canonical_url:** https://arxiv.org/abs/2601.05425

**direct_manuscript_or_data_urls:** [not recorded in original crawl]

**associated_source_ids:** S015

**association_evidence:** standalone source; primary page or abstract inspected

**evidence_status:** source inspected; not independently reproduced

**limitations:** Survey is not an original Jones proof and its composition date need not postdate later claims.

**author_bibliography_status:** pending; not exhaustive

---

### P012 — Computation of unknotting numbers: which knot breaks the Bernhard-Jablan Conjecture

**canonical_paper_key:** arxiv:2609.09861

**title:** Computation of unknotting numbers: which knot breaks the Bernhard-Jablan Conjecture

**identifiers:** arXiv:2609.09861

**scholarly_authors:** Seong-Jin Lee

**maintainer_or_publisher:** Pinocchio315; association supported by paper/repository

**date:** 2026-09-09 (v1); 2026-09-11 (v2)

**version:** v2, 2026-09-11; arXiv submission history checked

**canonical_url:** https://arxiv.org/abs/2609.09861

**direct_manuscript_or_data_urls:** https://arxiv.org/abs/2609.09861 | https://github.com/Pinocchio315/unknotting-tait-graphs/blob/main/results/extensions_2026-09-10/lower/README.md

**associated_source_ids:** S017

**association_evidence:** standalone source; primary page or abstract inspected

**evidence_status:** source inspected; not independently reproduced

**limitations:** Not Jones detection. Archived total 2,734 exact values includes 194 already official; do not count all as new. Certificate replay was not run.

**author_bibliography_status:** pending; not exhaustive

---

### P013 — RL unknotter, hard unknots and unknotting number

**canonical_paper_key:** arxiv:2603.07955

**title:** RL unknotter, hard unknots and unknotting number

**identifiers:** arXiv:2603.07955

**scholarly_authors:** Anne Dranowski; Yura Kabkov; Daniel Tubbenhauer

**maintainer_or_publisher:** Daniel Tubbenhauer author site

**date:** 2026-03 (initial preprint)

**version:** [not recorded in original crawl]

**canonical_url:** https://arxiv.org/abs/2603.07955

**direct_manuscript_or_data_urls:** https://arxiv.org/abs/2603.07955

**associated_source_ids:** S018;S019;S020;S021

**association_evidence:** standalone source; primary page or abstract inspected

**evidence_status:** source inspected; not independently reproduced

**limitations:** Upper bounds require replayable successful moves; unsuccessful search is not a lower bound. Manuscript is a preprint.

**author_bibliography_status:** pending; not exhaustive

---

### P014 — Computations of the slice genus and the unknotting number of links via machine learning

**canonical_paper_key:** arxiv:2610.10206

**title:** Computations of the slice genus and the unknotting number of links via machine learning

**identifiers:** arXiv:2610.10206

**scholarly_authors:** Yutong Dai; Oliver Hayman; András Juhász; Ludovico Morellato

**maintainer_or_publisher:** pending

**date:** 2026-10-07

**version:** initial preprint inspected

**canonical_url:** https://arxiv.org/abs/2610.10206

**direct_manuscript_or_data_urls:** [not recorded in original crawl]

**associated_source_ids:** S022;S023

**association_evidence:** standalone source; primary page or abstract inspected

**evidence_status:** source inspected; not independently reproduced

**limitations:** Link, slice-genus and unknotting-number results are not ordinary Jones detection. No independent execution in this crawl.

**author_bibliography_status:** pending; not exhaustive

---

### P015 — A parallel algorithm for the computation of the Jones polynomial

**canonical_paper_key:** arxiv:2505.23101

**title:** A parallel algorithm for the computation of the Jones polynomial

**identifiers:** arXiv:2505.23101; DOI:10.1073/pnas.2520332123

**scholarly_authors:** Kasturi Barkataki; Eleni Panagiotou

**maintainer_or_publisher:** Parallel-Jones-Polynomial organization

**date:** 2025-05-29 (preprint); 2026-04-21 (journal)

**version:** [not recorded in original crawl]

**canonical_url:** https://arxiv.org/abs/2505.23101

**direct_manuscript_or_data_urls:** https://arxiv.org/abs/2505.23101

**associated_source_ids:** S027

**association_evidence:** standalone source; primary page or abstract inspected

**evidence_status:** source inspected; not independently reproduced

**limitations:** Open-curve functional is not the classical knot invariant. Example numeric coefficients require checking before treating output as an exact integer certificate; no algorithm rerun.

**author_bibliography_status:** pending; not exhaustive

---

### P016 — Less Quantum, More Advantage: An End-to-End Quantum Algorithm for the Jones Polynomial

**canonical_paper_key:** arxiv:2503.05625

**title:** Less Quantum, More Advantage: An End-to-End Quantum Algorithm for the Jones Polynomial

**identifiers:** arXiv:2503.05625

**scholarly_authors:** Tuomas Laakkonen; Enrico Rinaldi; Chris N. Self; Eli Chertkov; Matthew DeCross; David Hayes; Brian Neyenhuis; Marcello Benedetti; Konstantinos Meichanetzidis

**maintainer_or_publisher:** Quantinuum

**date:** 2025

**version:** [not recorded in original crawl]

**canonical_url:** https://arxiv.org/abs/2503.05625

**direct_manuscript_or_data_urls:** https://arxiv.org/abs/2503.05625

**associated_source_ids:** S028

**association_evidence:** standalone source; primary page or abstract inspected

**evidence_status:** source inspected; not independently reproduced

**limitations:** Approximate evaluations and quantum resource analysis do not certify equality of an entire integer Laurent polynomial. CQCL/jones-polynomial redirects here and is not a separate result.

**author_bibliography_status:** pending; not exhaustive

---

### P017 — Certified upper bound for the distortion of the trefoil knot

**canonical_paper_key:** Hexagon:2611.00012v1 (NOT an arXiv ID)

**title:** Certified upper bound for the distortion of the trefoil knot

**identifiers:** Hexagon:2611.00012v1 (NOT an arXiv ID)

**scholarly_authors:** David Niedbala Giraudin

**maintainer_or_publisher:** Hexagon publisher; author credited in PDF

**date:** 2026-11-01 (v1/history); 2026-11-02 (listing)

**version:** v1

**canonical_url:** https://hexagonmath.org/2611.00012v1

**direct_manuscript_or_data_urls:** https://hexagonmath.org/pdf/2611.00012v1 | https://hexagonmath.org/src/2611.00012v1/files

**associated_source_ids:** S030

**association_evidence:** standalone source; manuscript inspected with page screenshots; code listing inspected, not executed

**evidence_status:** source inspected; not independently reproduced

**limitations:** No specialist validation was established. Two verifier implementations share construction input and are not fully independent evidence. No claim about Jones unknot detection.

**author_bibliography_status:** pending; not exhaustive

---

### P018 — Gluons and Knots

**canonical_paper_key:** arxiv:2610.10673

**title:** Gluons and Knots

**identifiers:** arXiv:2610.10673

**scholarly_authors:** Alfredo Guevara

**maintainer_or_publisher:** pending

**date:** 2026-10-07

**version:** [not recorded in original crawl]

**canonical_url:** https://arxiv.org/abs/2610.10673

**direct_manuscript_or_data_urls:** https://arxiv.org/html/2610.10673v1

**associated_source_ids:** S031;S032

**association_evidence:** standalone source; primary page or abstract inspected

**evidence_status:** source inspected; not independently reproduced

**limitations:** Not an ordinary Jones unknot-detection theorem. Formal treatment includes imported literature/contact inputs; compilation alone is not full semantic or independent mathematical validation.

**author_bibliography_status:** pending; not exhaustive

---

### P019 — Rogers–Ramanujan identities from the geometry of X^a=Y^b

**canonical_paper_key:** arxiv:2609.20567

**title:** Rogers–Ramanujan identities from the geometry of X^a=Y^b

**identifiers:** arXiv:2609.20567

**scholarly_authors:** Yifeng Huang; Kenny Lau; Ken Ono

**maintainer_or_publisher:** pending

**date:** 2026-09-17 (v1); 2026-10-07 (v2)

**version:** v2, 2026-10-07; supersedes v1 conditional-formalization description

**canonical_url:** https://arxiv.org/abs/2609.20567

**direct_manuscript_or_data_urls:** https://axiommath.ai/research/publications/

**associated_source_ids:** S033

**association_evidence:** standalone source; primary page or abstract inspected

**evidence_status:** v2 primary metadata checked; formalization is author-reported, not rerun

**limitations:** Version history matters: v1 depended on two literature inputs; the October 7 v2 says these prerequisites have now been formalized and reports an unconditional Lean formalization. Neither the code nor independent specialist assessment was audited here. Not ordinary Jones detection; repository association remains pending.

**author_bibliography_status:** pending; not exhaustive

---

### P020 — Advancing mathematics by guiding human intuition with AI

**canonical_paper_key:** doi:10.1038/s41586-021-04086-x

**title:** Advancing mathematics by guiding human intuition with AI

**identifiers:** DOI:10.1038/s41586-021-04086-x

**scholarly_authors:** Alex Davies et al.; complete credited list in primary paper

**maintainer_or_publisher:** pending

**date:** 2021

**version:** [not recorded in original crawl]

**canonical_url:** https://www.nature.com/articles/s41586-021-04086-x

**direct_manuscript_or_data_urls:** [not recorded in original crawl]

**associated_source_ids:** S047

**association_evidence:** standalone source; primary article search text; not full proof audit

**evidence_status:** source inspected; not independently reproduced

**limitations:** Historical 2021 work, not a new Jones-detection result. Exact theorem and complete bibliography should be checked before reuse.

**author_bibliography_status:** pending; not exhaustive

---

### P021 — Variational autoencoders understand knot topology

**canonical_paper_key:** arxiv:2504.04179

**title:** Variational autoencoders understand knot topology

**identifiers:** arXiv:2504.04179; DOI:10.1103/mdpw-lvcy

**scholarly_authors:** Anna Braghetto; Sumanta Kundu; Marco Baiesi; Enzo Orlandini

**maintainer_or_publisher:** pending

**date:** 2025

**version:** [not recorded in original crawl]

**canonical_url:** https://arxiv.org/abs/2504.04179

**direct_manuscript_or_data_urls:** [not recorded in original crawl]

**associated_source_ids:** S048

**association_evidence:** standalone source; primary metadata/abstract discovery

**evidence_status:** source inspected; not independently reproduced

**limitations:** Not an exact topological certificate or Jones-detection theorem. Discovery-level review.

**author_bibliography_status:** pending; not exhaustive

---

### P022 — Learning Topological Features of Z-hat Invariants

**canonical_paper_key:** arxiv:2608.18570

**title:** Learning Topological Features of Z-hat Invariants

**identifiers:** arXiv:2608.18570

**scholarly_authors:** Pending primary metadata verification; linked from Fabian Ruehle bibliography

**maintainer_or_publisher:** pending

**date:** 2026-08

**version:** [not recorded in original crawl]

**canonical_url:** https://arxiv.org/abs/2608.18570

**direct_manuscript_or_data_urls:** [not recorded in original crawl]

**associated_source_ids:** S050

**association_evidence:** standalone source; author bibliography discovery

**evidence_status:** unreviewed author-associated manuscript lead

**limitations:** Full author list, exact theorems, data and code association pending. Adjacent three-manifold work, not ordinary Jones detection.

**author_bibliography_status:** pending; not exhaustive

---

### P023 — Invariants for Turaev genus one links

**canonical_paper_key:** arxiv:1604.03501

**title:** Invariants for Turaev genus one links

**identifiers:** arXiv:1604.03501

**scholarly_authors:** Oliver T. Dasbach; Adam M. Lowrance

**maintainer_or_publisher:** pending

**date:** 2016

**version:** [not recorded in original crawl]

**canonical_url:** https://arxiv.org/abs/1604.03501

**direct_manuscript_or_data_urls:** [not recorded in original crawl]

**associated_source_ids:** S053

**association_evidence:** standalone source; primary abstract discovery

**evidence_status:** source inspected; not independently reproduced

**limitations:** A leading or trailing coefficient of absolute value one alone does not imply a nonconstant polynomial. Exact scope needs full-text review before reuse.

**author_bibliography_status:** pending; not exhaustive

---

### P024 — Khovanov homology of the 2-cable detects the unknot

**canonical_paper_key:** arxiv:0805.4418

**title:** Khovanov homology of the 2-cable detects the unknot

**identifiers:** arXiv:0805.4418

**scholarly_authors:** Matthew Hedden

**maintainer_or_publisher:** pending

**date:** 2008

**version:** [not recorded in original crawl]

**canonical_url:** https://arxiv.org/abs/0805.4418

**direct_manuscript_or_data_urls:** [not recorded in original crawl]

**associated_source_ids:** S054

**association_evidence:** standalone source; primary abstract discovery

**evidence_status:** source inspected; not independently reproduced

**limitations:** The result concerns Khovanov homology, not the ordinary or colored Jones polynomial alone.

**author_bibliography_status:** pending; not exhaustive

---

### P025 — On the Colored Jones Polynomial, Sutured Floer homology, and Knot Floer homology

**canonical_paper_key:** arxiv:0807.1432

**title:** On the Colored Jones Polynomial, Sutured Floer homology, and Knot Floer homology

**identifiers:** arXiv:0807.1432

**scholarly_authors:** J. Elisenda Grigsby; Stephan Wehrli

**maintainer_or_publisher:** pending

**date:** 2008-07-09

**version:** [not recorded in original crawl]

**canonical_url:** https://arxiv.org/abs/0807.1432

**direct_manuscript_or_data_urls:** [not recorded in original crawl]

**associated_source_ids:** S055

**association_evidence:** standalone source; primary abstract discovery

**evidence_status:** source inspected; not independently reproduced

**limitations:** Do not replace categorification by the polynomial itself; exact coefficients and conventions require full-text review.

**author_bibliography_status:** pending; not exhaustive

---


### Manuscript and association gaps outside the 25 inherited paper rows

**S006:** Historical project audit, not then identified as a public publication. The received inventory said its PDF was included in the old bundle; that PDF was not recovered with this Markdown file. The present public ledger provides the later provenance and status of the Carmi–Cohen work.

**S013:** Original manuscript is retained in sources with NYJM citation, but is absent from the inherited 25 identifier-keyed paper records. Next: Use the exact NYJM article URL and establish any persistent identifier before adding a deduplicated paper record.

**S016:** Associated manuscript identifier remains pending. Next: Read CITATION.cff, releases and scholarly author publication pages.

**S039:** arXiv:1804.07910 is only an unverified association lead in the source claim text, not a confirmed paper record. Next: Verify primary metadata and repository-paper association; do not turn the cited ID into established authorship.

**S056:** Zenodo record 22759451 is citation-only; exact DOI/creator/version not verified. Next: Read the actual record metadata and publication files; preserve reserved/unpublished status if applicable.


## 6. Mathematical claim boundaries and preserved corrections

The following is retained from the original crawl; version descriptions are as recorded at that snapshot, not newly verified current status.

### Claim and verification boundaries

| Statement or observation | What it does establish | What it does not establish |
|---|---|---|
| V_K(t)=1 exactly over integer Laurent polynomials | The candidate passes the polynomial condition | That K is trivial or nontrivial |
| Simplifier did not unknot the diagram | This search failed within its resources | Nontriviality, crossing number, or a lower bound for unknotting number |
| Explicit legal Reidemeister path to a circle | An unknot certificate once each move and encoding is checked | A theorem about all Jones-trivial diagrams |
| Positive Seifert genus from a justified exact knot-Floer calculation | Nontriviality of the encoded knot | Jones polynomial equality |
| V_K≡1 modulo m | A modular congruence | V_K=1 over the integers without additional bounds and reconstruction |
| Approximate evaluations at roots of unity agree | Numerical agreement at sampled points | Equality of Laurent polynomials |
| Khovanov homology detects the unknot | A stronger invariant can recognize the unknot | Its graded Euler characteristic alone does so |
| Verification through 24 crossings | A finite universal crossing range | The unrestricted statement |
| Ordinary unknotting number u(K) | Minimum over all diagrams and sequences | The same minimum restricted to crossing changes in minimal diagrams |
| Faithfulness of a braid representation | No nontrivial element maps to the identity matrix | Injectivity of trace, or unknot detection by a closure polynomial |
| Necessary hypothetical HOMFLY/Jones data | A candidate passes an algebraic restriction | Existence of a knot realizing those data |
| A formal proof compiles | The formal theorem follows from the formal definitions and admitted assumptions | Correct translation of the informal claim, novelty, or independent specialist review |
| A graph/tangle identity holds algebraically | An identity in the stated algebra | A legal embedded diagram move with all topology hypotheses preserved |
| An archive contains many lines or lemmas | Substantial recorded activity | Proximity to a completed proof |

Primary references are indexed in SOURCE_REGISTER.md: S003–S004, S008, S011–S014, S016, S024, S028 and S031–S033. The conditional algebra replay S006 intentionally does not claim a topological verification.

#### Version/correction register

- S005: existing October 31 user audit challenges Carmi–Cohen's June manuscript. No newly confirmed repair or withdrawal was found; latest version status remains pending.
- S009: July 2026 Burau faithfulness claim retrieved. A secondary index points to a September 14 revision, but the primary version history was not resolved. Do not treat the initial snapshot as guaranteed current.
- S016: repository exposes an erratum concerning an orientation convention in an Owens obstruction; preserve its corrected scope and distinguish minimal-diagram results.
- S032: current README says Hypothesis R is proved; literature/contact inputs still need audit. Do not propagate a stale statement that Hypothesis R remains open.
- S033: arXiv v1 had two external literature prerequisites in the formalization; October 7 v2 explicitly reports that those have now been formalized. Mark the current formalization as author-reported unconditional, while leaving independent reproduction pending.


## 7. Historical project-audit and replay record

The received inventory identifies `original_crawl/context/jones-unknot-proof-audit.pdf` as the 31 October 2026 Codex-assisted project audit. That PDF is not included with this recovered inventory, and the recorded audit was not independently published specialist review. The equations below preserve the earlier record; later ledger notes govern their reviewed scope.

The recorded algebraic setup is:

```text
Classical target: V_U(t) = 1; x = sqrt(t); p = x - x^(-1).
V_1 = x^2 + x^6 - x^8.
V_L = x^4 V_(L-2) + x^2 - x^4 + x^6 - x^8, for odd L >= 3.
V_L = A_L(p) + x B_L(p), using x^2 = p*x + 1.
Recorded algebraic conclusion: deg_p(V_L) = 2L + 5,
with leading coefficient of B_L equal to -1.
At L = 23: degree 51 and b_51 = -1.
Audit comparison: the geometric package is alleged to imply a uniform bound 22.
```

This is an objection to a particular proof package, not an example of a nontrivial knot with Jones polynomial one. For it to refute that package, the encoded geometric family must actually satisfy the package's hypotheses. The replay checks reduction and reconstruction conditional on the supplied recurrence; it does not establish the diagrammatic identification or the applicability of the paper's hypotheses.

The received inventory says that `checks/results.json` recorded 51 passing odd lengths from 1 through 101, using `original_crawl/checks/replay_twist_algebra.py`. Neither file was recovered with this inventory, and that execution was not repeated for this edition.

[Redacted: run command and workflow instructions for the unavailable historical replay package.]

No third-party repository certificate, Lean build, training run, large enumeration or independent diagram calculation was performed for this public edition.


## 8. Coverage, failed retrievals and uncrawled material

The following preserves the earlier crawl’s actual coverage, not a claim of new or exhaustive coverage. Negative searches and failed access do not establish that relevant content is absent.

### Coverage and unresolved retrieval

#### Scope

This is a targeted public-source crawl seeded from the user's AI mathematics watch, expanded into knot/Jones literature and author-linked computational archives. It is not a file-by-file mirror of all sources. The 56 retained records include pointers and uncertain cases; the 25 paper records are identifier-deduplicated, not a complete bibliography.

#### Historical context availability

[Redacted: private catalogue/session handoff details and personal-context retrieval instructions.]

The earlier inventory records that an October 31 project-audit PDF was consulted, but the underlying bundle was not recovered with this file. No additional manuscript or repository coverage is inferred from private conversation history.

#### Priority sources

| Source | Action / result | Limit |
|---|---|---|
| github.com/ipitchford | Repository listing and indexed Jones/knot code searches | Not every repository file, release, issue or author bibliography was inspected; negative indexed searches are not absence proof |
| github.com/cyclemath | Indexed knot code and repository/README queries | No relevant hit in returned results; not a complete source-content crawl |
| evidencepress.org/api/papers.json | Direct attempt | Response exceeded web tool size limit; not parsed completely |
| ipitchford/evidence-press-site/PUBLISHED.json | GitHub connector retrieved source publication ledger; searched for knot and Jones | No matching ledger text; slug/URL metadata is not full manuscript content |
| ProofAtlas | Jones workspace inspected in detail; four adjacent route pages retained | Full raw 4,344-line source archive not obtained |
| Hexagon | Trefoil paper page, PDF pages and source-file index inspected | Code not executed; broader site not exhaustively crawled |
| MathDB | Paper/index and knot-problem searches | Relevant problem pointers retained; no complete dynamic catalogue export |
| VibeMathed | Homepage and targeted search | Not all internal pages crawled |
| Hugging Face | Targeted Jones/knot searches | Paper mirrors and unrelated benchmark/OCR datasets predominated; no complete host crawl |
| GitLab | Targeted public searches | No substantive new primary Jones archive identified in returned results; not proof of absence |
| Zenodo | Citation and keyword search | Cited trefoil lower-bound deposit remains unreviewed; unrelated keyword hits not promoted |
| MAIS and teorth/optimizationproblems | Remain watch seeds | No complete knot-specific deep/backfill pass in this run |
| Dugongue/MathProofs | Public root retrieval attempted | Failed access; no deep full-text audit completed |

#### Personal-site seed pass

The following pages were reached or searched at entry-page level without locating a directly relevant primary Jones proof in the retrieved material. This is NOT a conclusion that their full archives contain none:

- https://nitromannitol.github.io/ai-mathematics.html
- https://stepsunbounded.com
- https://maidenhead.solutions
- https://harjassand.github.io
- https://hypnosmath.org
- https://yoshito-ishiki-math.github.io/ai-research-reports.html

Access/search limitations remained for https://paatai.github.io/ai-proofs, https://barnettcaleb1.github.io/mathematics and https://aleckriebel.github.io/Math. No full scan of Hypnos notebooks or unindexed PDFs was performed.

#### Outbound accounts followed

The crawl followed paper/author links to dtubbenhauer, annedranowski, Pinocchio315, andras-juhasz, aguevara22, Quantinuum (with CQCL alias), and Parallel-Jones-Polynomial. Some additional repository leads are retained as unreviewed, rather than asserted as mathematical results. Individual contributors' complete publication lists remain pending.

#### Reproducibility and access gaps

- Third-party certificates, Lean builds, model training and large enumerations were not run.
- The public hard-unknot bucket is named by the paper, but the storage root could not be opened and individual files were not downloaded.
- Several publishers returned access errors even where indexed primary abstract/full-text excerpts were available.
- The precise current primary version history of the Carmi–Cohen and Burau claims remains incompletely resolved. Automated summaries were not accepted as validation.
- Paper associations for the `dtubbenhauer/unknot` manuscript, the colored-Jones-walks repository, and the HJO formal repository remain pending.
- Source timestamps, search crawl dates, publication dates and version dates are kept conceptually separate; a recently crawled historical paper is not a new result.

#### Historical outstanding backfill

The earlier inventory proposed checking full source trees and releases, exact hard-unknot data manifests, the raw ProofAtlas archive, author-associated manuscripts and formal repositories, colored-Jones and modular primary citations, and specialist corrections when located. These were proposed follow-ups, not work performed for this edition. [Redacted: private cumulative-catalogue recovery instruction.]


## 9. Historical package manifest — companion files not recovered

The following table describes the former bundle as recorded in the received inventory. It is not the manifest of this public directory. Only `CLAUDE_JONES_RESEARCH.md` was recovered here; companion files listed below are historical references.

| File | Purpose |
|---|---|
| `CLAUDE_JONES_RESEARCH.md` | This complete standalone readable inventory, including all sources, paper rows, boundaries and coverage. |
| `CLAUDE.md` | Short operating brief for a folder-based Claude session. |
| `source_inventory.jsonl` | 56 JSON objects, one per source, retaining every original field plus `_handoff` metadata. |
| `paper_inventory.jsonl` | 25 JSON objects, one per inherited paper record, retaining every original field plus `_handoff` metadata. |
| `reading_queue.json` | Every source exactly once, ordered by original priority and source ID, with a specific next check. |
| `research_tasks.json` | 16 proposed cross-source tasks with deliverables and guardrails. |
| `source_groups.json` | Thematic navigation groups; every source appears in exactly one group. |
| `relationships.jsonl` | Original source relationships and paper associations; not an independence or correctness graph. |
| `link_inventory.jsonl` | Deduplicated recorded external locators with source/paper references. |
| `source_links.txt` | The same recorded locators as plain UTF-8 text, one per line. |
| `paper_association_backlog.json` | Missing or unresolved paper-index associations preserved explicitly. |
| `SCHEMA.md` | Field and provenance conventions; examples of safe JSONL ingestion. |
| `validate_package.py` | Local integrity/count/preservation checks; does not validate external mathematics. |
| `VALIDATION_REPORT.json` | Results of package-level preservation and structure checks. |
| `MANIFEST.json`, `SHA256SUMS.txt` | File sizes and integrity hashes. |
| `original_crawl/` | All original crawl files retained byte-for-byte, including the audit PDF, Python replay and historical results. |

[Redacted: machine-ingestion and artifact-fetch instructions for the unavailable historical bundle.]

The inventory's duplicate, alias and mirror records remain deliberate historical entries; they do not count as independent mathematical results. Original qualifiers such as `pending`, `not established` and `unreviewed` are retained in the records above.
