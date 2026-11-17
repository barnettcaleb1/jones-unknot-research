# Completeness of this snapshot

This is an inventory of the available research record, not a claim that every proposed proof has been verified or that every conversation ever held was recoverable. The source scope is the workspace `collab/`, `work/`, `outputs/` and the separate `jones-lanes/` research tree. Live chat transcripts outside the saved letters and reports are not fabricated.

| Category | Files | Bytes |
|---|---:|---:|
| excluded | 10,910 | 851,007,438 |
| git | 14,662 | 164,308,666 |
| asset | 11,126 | 2,175,771,151 |

The catalog contains 345 claim records and 270 letters. Claims may overlap or supersede one another; these are not counts of theorems.

## What is preserved

- Original research notes, correspondence, proof drafts, programs, and compact evidence in Git.
- Large generated evidence and historical logs in hash-indexed release supplements, restored at their original archive-relative paths.
- A disposition for every inventoried file, with a reason for exclusion.
- Original wording, including mistakes and unfinished reviews, with a separate current reading guide.

## What is excluded

Downloaded human papers and source bundles are cited rather than republished. Vendored dependencies, interpreter environments, compiled executables, and transient state are omitted. Legacy ZIP/tar bundles are inventoried as bundled copies rather than added again; extraction contents are reviewed separately for any unique research documents. These decisions are visible in [artifact-manifest.json](../data/artifact-manifest.json).

The [source audit](REPRODUCIBILITY_AUDIT.md) describes dependency and provenance limitations. Hash coverage is for the distributed original research files; it does not certify their mathematical correctness. The export program is included so the selection policy is inspectable.

## Review still needed

The bibliography is a curated primary-source map, not a fresh verification of every citation in every archived document. Historical bare paths may require the mapping in [Reproducing](REPRODUCING.md). Full manuscript specialist review, complete dependency pinning, and replay of all large certificate collections are not claimed. The contribution tasks make these gaps explicit.

## Additional handoff and recovered bundles

The [Claude completeness request](CLAUDE_HANDOFF.md) is tracked separately; a pending response is not confirmation of exhaustiveness. Twenty-five unique original files were recovered from legacy evidence ZIPs after byte-level comparison with the other exported artifacts. Their ZIP/member provenance is in [legacy-members.json](../data/legacy-members.json). Third-party members remain excluded and identified.

A [harvested source-link index](../data/source-links.json) makes citations scattered through the historical record discoverable. It is not a claim that every link or historical use has been independently verified; the curated [References](REFERENCES.md) states its review levels.
