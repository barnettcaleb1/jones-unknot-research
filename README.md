# Jones unknot conjecture: a research ledger

**A research record directed by Caleb Barnett, with Codex and Claude. Snapshot: 17 November 2026.**

This repository records an investigation of the Jones unknot conjecture: does a knot with Jones polynomial 1 have to be the unknot? **The investigation has neither proved the conjecture nor produced a verified counterexample.** Its output includes reductions, small lemmas, exact calculations, candidate arguments, failed approaches, and corrections to earlier claims.

The record is intended for mathematicians and independent agents who want to inspect a proof, reproduce a calculation, find an unresolved step, or avoid repeating a failed route. The historical archive is evidence of what was attempted. It is not a collection of endorsed theorems.

## Read the mathematics

| Start with | What it contains |
|---|---|
| [Start here](docs/START_HERE.md) | The problem, conventions, and a suggested reading route |
| [Research map](docs/RESEARCH_MAP.md) | How the approaches connect and where they stop |
| [Small results and proof sketches](docs/SMALL_RESULTS.md) | Readable statements, arguments, scope, and links to full notes |
| [Complete claim index](docs/CLAIM_INDEX.md) | Historical ledger entries and the latest scaffold records, with provenance |
| [Failure directions](docs/FAILURES.md) | Refutations, failed mechanisms, and what would be needed to reopen them |
| [Human work and corrections](docs/HUMAN_WORK_AND_CORRECTIONS.md) | Prior work, exact criticism, retractions, and source qualifications |
| [References](docs/REFERENCES.md) | Bibliography and primary-source links |
| [Open problems](docs/OPEN_PROBLEMS.md) | Scoped questions that remain unresolved |

## Inspect the record

[Download the evidence supplements](https://github.com/barnettcaleb1/jones-unknot-research/releases/tag/snapshot-2026-11-17). The release includes the large saved computations and their checksums.

- [Evidence and status policy](docs/EVIDENCE_POLICY.md): what historical `PROVED`, `TRUSTED`, and `REFUTED` labels mean.
- [Chronology](docs/CHRONOLOGY.md): dated correspondence with subjects and links.
- [Archive index](docs/ARCHIVE_INDEX.md): the original notes, reports, code, manuscripts, and evidence.
- [Completeness and exclusions](docs/COMPLETENESS.md): the precise boundary of this snapshot; nothing omitted is silently treated as verified.
- [Reproducibility audit](docs/REPRODUCIBILITY_AUDIT.md): portable checks and dependencies still needing repair.
- [Machine-readable records](data/): claims, correspondence, artifact hashes, references, and downloadable evidence inventories.

The source archive preserves the available research files from both working areas. Large generated evidence is distributed as release supplements, indexed by hash, rather than added to every Git clone. Third-party papers, vendored software, machine environments, and duplicate legacy bundles are not relicensed or republished wholesale. The manifest records those exclusions.

## Reproduce a bounded check

With Python 3.10 or later, from the repository root:

```sh
python3 tools/validate.py
python3 checks/run_portable.py
```

These commands check the package and run selected fixed exact certificates. They do **not** establish all archived theorems or replay every search. Read [reproduction instructions](docs/REPRODUCING.md) before running historical programs, whose paths and dependencies are often specific to the original machines.

## Contribute from another machine

Read [CONTRIBUTING.md](CONTRIBUTING.md) and [AGENTS.md](AGENTS.md). Choose one bounded task from [the task board](docs/TASKS.md), pin a commit, state your assumptions, and return a proof or a replayable counterexample. An independent read should report what it checked, not simply agree with a previous agent.

The mathematical program was paused at this snapshot. Its last selected direction was the exact complexity of two-component links with the unlink's Jones polynomial, called **JT₂** here. Publication of the record does not turn pending referee work into completed work.

## Authorship and review

Caleb Barnett directed the investigation. Much of the prose, mathematics, and code was developed through an AI collaboration using Codex and Claude. Independent AI reads are internal checks, not external specialist peer review. Historical model labels are retained where they occur; they are not guarantees of the reliability of an argument. Authored manuscripts and claims of priority remain subject to review. See [authorship and reuse](docs/AUTHORSHIP_AND_REUSE.md).

Project contact: [Caleb Barnett](https://barnettcaleb1.github.io).
