# What this archive can reproduce

This is a publication audit of the available files, dated 17 November 2026. It is not a fresh verification of every mathematical claim or every reported search. The distinction matters: a proof note, a program, a saved output, and an independently replayed certificate provide different kinds of evidence.

The machine-readable companion is [source-audit.json](../data/source-audit.json). It records the source inventory, recommended exclusions, dependency problems, and the two fixed checks replayed during preparation.

## Coverage of the available source material

The initial inventory found the following files before publication filtering. Counts include duplicate exports, downloaded papers, caches, and third-party software; they are not counts of original mathematical results.

| Source collection | Files | Approximate size | Public archive location |
|---|---:|---:|---|
| Collaboration letters, boards and selected reports | 329 | 3.8 MB | `archive/collab/` |
| Codex working notes, code and data | 3,694 | 966 MB | `archive/work/` |
| Earlier handoffs and deliverables | 95 | 13.4 MB | `archive/outputs/` |
| Claude's separate research directories | 32,557 | 2.21 GB | `archive/claude/` |

No symbolic links were found in the three workspace collections. Claude's source directories were available locally for this audit. Most of the later engine code and detailed certificates live there; copying only `collab/data/` would preserve summaries but omit essential supporting material.

“Complete” should therefore mean an indexed record of every available research artifact, its disposition and its relationship to a claim. It should not mean that every byte belongs in the main Git repository, or that every archived sentence is currently endorsed. The export manifest is the authority on which objects are actually included, excluded, or distributed separately. An external file named in a report is not reproduced merely because the report is reproduced.

## Two checks replayed during preparation

These checks ran from the existing source, without any new diagram search. The Carmi–Cohen verifier was copied to a temporary directory because it writes its result beside itself; the working research files were left unchanged.

| Check | Dependency profile | Observed result | What it establishes |
|---|---|---|---|
| [EF depth certificate](../archive/work/theory_restart/referee_checks/ef_depth.py) | Python 3 standard library | Passed | The transcribed seed has the displayed fourth-order jet, and the doubling identity doubles that coefficient. The proof note supplies the all-parameter induction and the primary-source check. |
| [Carmi–Cohen recurrence certificate](../archive/work/paper/carmi-cohen-obstruction/verify.py) | Python 3 standard library | Passed; regenerated JSON agrees with the archived result | The displayed recurrence, binomial change of basis, and leading coefficient agree at the stated fixed values, including the obstruction at `L=23`. It does not refute the paper's main mathematical statement. |

For the first check, from the repository root:

```sh
python3 -I archive/work/theory_restart/referee_checks/ef_depth.py
```

For the second, copy the verifier into a temporary directory before running it, or use the repository's portable reproduction harness if supplied. Do not run an entire archived search directory merely to check this fixed certificate.

The preparation environment did not have SymPy in its default Python installation. Symbolic matrix certificates depending on SymPy were inspected but not replayed in this audit. No claim is made here that the large knot-certification censuses, Khovanov computations, or Farkas-certificate collections were rerun.

## What still prevents one-command reproduction

### Absolute paths and dependency closure

Several archived scripts import from machine-specific paths. For example, the width-two module imports `lp`, which imports `flat_search` and `alex`; these in turn depend on the original helper files. The mathematical matrices are also saved as JSON, but the JSON alone does not reproduce the diagram-to-matrix identification.

Keep the archived sources unchanged where possible. A portable launcher can add the corresponding repository directories to Python's import path; any source patch should be recorded as a patch, with the original hash and a regression result. A successful import is not a verification of the intended normalization or marking.

### Environments

There was no common dependency lock covering the whole project. Different experiments use standard Python, SymPy, kht++, Regina, SnapPy, and other mathematical software. Vendored virtual environments and platform-specific wheels are unsuitable as the portable specification.

Each runnable package should state:

1. The claim or certificate it checks, including conventions and input files.
2. The interpreter and dependency versions actually used.
3. A command, expected output, approximate resource requirement, and whether it writes files.
4. Whether the check is exact arithmetic, a numerical diagnostic, or a finite sample.
5. Which part of the proof remains mathematical rather than executable.

### Large data and certificates

The largest files include generated transport tables of roughly 129 MB and 169 MB, and an external arborescent cache of roughly 700 MB. Some smaller compressed files contain replayable knot-group certificates rather than disposable search caches. Size alone must not decide whether evidence is discarded.

For data outside the main repository, preserve its original logical path, size, hash, producing command or report, and public download location. Mark a missing asset as missing. A report saying that all certificates passed is different from making those certificates and both checkers available.

Pickle files are executable serialization formats. They should not be loaded automatically by the website, indexer, or verification harness. Prefer a safe export format for public certificate exchange; otherwise make use opt-in and document the producer and checksum.

## Publication filtering

The recommended rules are explicit in the JSON audit. They distinguish material by provenance, not merely by filename extension.

- Include original proof notes, reports, correspondence, scripts, exact certificates, and small result data, with source mapping and hashes.
- Retain failed and superseded work as historical material. Link it to the correction or current status; do not silently rewrite the original argument into something it never claimed.
- Exclude installed packages, virtual environments, wheels, bytecode, and regenerable typesetting files from the research archive. Record dependencies instead.
- Do not redistribute downloaded human papers, their full-text conversions or source archives under this project's license. Cite the primary source and preserve the bibliographic pointer.
- Do not apply a blanket `src/` exclusion. Claude's `lit/*/src/` trees contain downloaded sources, whereas `mont/cx/roundE/refM300/src/` and `roundD/refV3/src/` contain original certificate code needed for this project.
- Treat third-party knot tables and databases separately from original computed data. Their presence in an experiment does not make them original project material.

The original manuscripts and expository PDFs are distinct from third-party PDFs. They may be included as drafts with their actual review status, alongside their source and corrections.

## Privacy and credential check

A bounded pattern check covered 10,310 text-like files of at most 4 MB, excluding installed packages and runtime caches. It found no confirmed GitHub tokens, OpenAI-style secret tokens, or private-key headers. Four apparent matches were parts of LaTeX lemma labels in downloaded human source.

This was not a complete security audit of arbitrary binaries, larger files, or every possible secret format. Absolute home-directory paths and machine-specific locations occur frequently and should be rewritten in the public presentation or represented by stable source aliases. Preserve the scientific provenance without treating a private machine path as a public dependency.

## A contribution standard for independent machines

### Later handoff integration

The [additional Claude handoff](CLAUDE_HANDOFF.md) contributes 416 manifest-covered research artifacts and one recovery explanation. Received hashes were checked before import; the [handoff manifest](../data/handoff-artifacts.json) records source, received and published hashes separately wherever redaction or path normalization changes the bytes. The [known-gap register](../data/handoff-known-gaps.json) includes missing patched helpers, lost outputs and unfinished runs. None of these additional historical programs was rerun during integration. The first-snapshot portable checks and their recorded outcomes above are unchanged.

### Returning a check

A useful contribution should arrive as a small claim package, not merely a transcript asserting success. It should name the question, its prerequisites, the exact statement or counterexample, the proof or executable certificate, and the scope of verification. A separate reviewer should be able to reject it without rerunning an unrelated search.

Failed packages are valuable when they retain the proposed statement, the decisive witness, the reason the failure applies, and the hypotheses under which the idea might still work. This archive's strongest starting point is that evidence can be attached to stable claim identifiers while preserving the original research history. Making every historical computation turnkey is a further engineering task, not something implied by uploading its files.
