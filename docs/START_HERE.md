# Start here

This is a research record about the **Jones unknot conjecture**:

> If a classical knot $K\subset S^3$ has normalized Jones polynomial $V_K(t)=1$, must $K$ be the unknot?

The project has **neither proved the conjecture nor produced a certified counterexample**. Its useful outputs are narrower theorems and reductions, explicit obstructions to proposed methods, exact computational certificates, and a history of corrections. A substantial part of the record explains why plausible arguments do not establish what they initially appeared to establish.

Caleb Barnett directed the collaboration with Codex and Claude. Historical references to “Astra” mean Codex. The archive preserves the collaborators' original terminology and status labels; these labels describe an internal process, not journal acceptance or independent specialist review. Mathematical priority has not been certified.

## Choose a route through the material

| Reader's aim | Start with | Then follow |
|---|---|---|
| Understand what was attempted and what remains | [Research map](RESEARCH_MAP.md) | [Open problems](OPEN_PROBLEMS.md) |
| Read mathematics without reading the correspondence | [Small results, with proofs](SMALL_RESULTS.md) | The linked full proof notes |
| Avoid repeating failed work | [Failure atlas](FAILURES.md) | The exact counterexample or scope correction linked from each entry |
| Inspect the early ledger exhaustively | [Early/middle/late result ledger](../archive/outputs/claude-handoff/RESULT_LEDGER.json) | [Human handoff](../archive/outputs/claude-handoff/CLAUDE_JONES_HANDOFF.txt) |
| Inspect the later chronology | [Theory log](../archive/collab/THEORY-width-ladder.md) | The dated letters and named proof notes |
| Check the project's status discipline | [Original protocol](../archive/collab/PROTOCOL.md) | [Recorded scaffold](../archive/collab/SCAFFOLD.md) |

The short proofs here are an entry point, not a replacement for the full ledger. The archive retains many additional small results, finite computations, corrections and abandoned designs. The historical theory log is chronological: it contains conjectures subsequently refuted in later entries, and some section numbers repeat. **Do not treat the first occurrence of a claim as its final status.**

## What the main objects mean

**Actual diagram versus skein element.** A tangle is a collection of embedded strands in a marked ball. Its Kauffman bracket is a vector in a linear space. A formal linear combination of bracket vectors need not be the bracket of any actual tangle. Much of the research concerns this gap between linear algebra and geometric realization.

**Closure equality versus polynomial equality.** Two closures being isotopic is much stronger than their Jones polynomials agreeing. The proposed rational-tangle uniqueness theorem uses actual closure equalities. Substituting polynomial equalities into its hypotheses would assume the missing detection result.

**Lemma Q.** This is the project's name for the remaining flat-tangle realization problem in the unknot-closure setting. Roughly, a tangle with a specified actual unknot closure has the bracket behavior of a trivial tangle; must it itself be trivial in the required marked sense? The full formulation and framing belong to the [scaffold's u=1 route](../archive/collab/SCAFFOLD.md). It is a reduction and a research target, not a theorem proved here.

**The invariant $J$.** Later notes use a normalized scalar attached to a strongly invertible knot and its marked quotient tangle. It is not the ordinary Jones polynomial of the covering knot. Conventions matter: several historical computations use $t=A^4$, whereas the ordinary Jones convention uses $t=A^{-4}$. The [skein dictionary](../archive/work/theory_restart/skein_dictionary_arbitrary_boxes.md) fixes the correspondence. Never transfer an identity between these conventions without the documented inversion or framing correction.

**JT₂.** The last research direction asks about the computational complexity of recognizing two-component links with exactly the Jones polynomial of the two-component unlink. Known links with that polynomial need not be unlinks. This is a different decision problem from unknot recognition, and no hardness theorem for it is proved here.

## How to read a status

| Historical label | Safe public interpretation |
|---|---|
| PROVED | A written proof was checked within the collaboration, or the claim was imported from a cited published theorem. Inspect which of these applies. |
| TRUSTED / INTERNAL-PROOF | A written argument is present and used internally; its specified review remains incomplete. |
| CHECKED / DATA / EXACT-COMPUTATION | A finite computation or reported certificate, with the stated range and inputs. It does not automatically imply an infinite-family theorem. |
| FORMAL | A result or countermodel in an algebraic/category model; actual knot or tangle realization is not asserted. |
| OPEN / CONDITIONAL | A missing proof, a proposed reduction, or a theorem whose explicit extra input is unresolved. |
| REFUTED / WITHDRAWN | The particular statement or inference failed. Read what the counterexample does and does not refute. |

An internal proof, a reproducible computation, external specialist review, and a novelty claim are four different things. A hash verifies which file was used, not whether its mathematics is correct. A large search with no hit is evidence about its certified search region, not about all knots.

## The strongest cautions are mathematical

1. The **Sikora manuscript is an internally audited candidate proof** of a separate rational-solution uniqueness conjecture, with an unframed extension. Its complete manuscript referee rounds did not finish before the research resumed. It is not a proof of Jones unknot detection. See the [audited proof](../archive/outputs/rational-tangle-uniqueness-audited-proof.txt), [audit](../archive/collab/audits/LATE-41-audit.md), and [manuscript source](../archive/work/paper/sikora-uniqueness/main.tex).
2. Obstructions to a proof in another paper must be read with the exact version, numbered assertion, normalization and counterexample. They do not automatically disprove that paper's main theorem. This distinction is especially important for the [Carmi–Cohen note](../archive/work/paper/carmi-cohen-obstruction/main.tex).
3. Endpoint-positivity conjectures that initially fit hundreds of examples were later refuted by actual tangles. The current map therefore does not present TILT, NP, END or the parallelogram law as universal theorems.
4. Earlier search summaries included provisional “unknot” classifications. Later certification repaired specified sets. The [certification chronology](../archive/collab/THEORY-width-ladder.md) and exact scope are part of the evidence, not optional footnotes.

## A useful contribution has a bounded target

The research was paused on 17 November 2026. Publication of this ledger does not reactivate archived tasks. To contribute, choose one [open obligation](OPEN_PROBLEMS.md), state the conventions and dependencies you are using, and return either a proof, an exact counterexample, or a precise obstruction. A proof note should say which formal countermodels it excludes. A computational contribution should specify its finite domain, include a replayable certificate, and keep “no certified hit” separate from “every candidate certified trivial.”

The intended benefit of distributing this record is that another person or agent can begin at a genuine unresolved step without rediscovering an old failure or relying on an obsolete claim.
