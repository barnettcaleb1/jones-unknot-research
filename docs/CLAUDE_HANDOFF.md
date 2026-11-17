# Claude's completeness handoff

The additional handoff requested by Caleb was received on 17 November 2026 and incorporated after privacy and provenance review. It adds material from the separate adversarial-pass directory, the bridge scratchpad, and one earlier literature-crawl inventory. Research stayed paused: importing a saved check is not rerunning it.

The [original request](../archive/collab/msgs/20261117-140421-codex.md), [machine-readable receipt](../data/claude-handoff-status.json), [per-file provenance](../data/handoff-artifacts.json), and [known-gap register](../data/handoff-known-gaps.json) describe the scope. The public guide to conversation-only results is [Recovered history and corrections](HISTORY_RECOVERED.md).

## What arrived

| Material | Artifacts | Provenance |
|---|---:|---|
| Saved notes, scripts, outputs and reviews | 403 | Copied from the identified source roots; ten were privacy-redacted before delivery, with both original and received hashes recorded |
| Recovered files | 5 | Exact text recovered from original file-creation tool inputs; not recreated from remembered mathematics |
| Workflow-journal result extracts | 8 | Contemporaneous research results extracted from journals, excluding the private runtime containers |

All 416 manifest-covered received hashes matched. An additional recovery-method note is indexed separately, for 417 added archive records. Eleven received records needed editorial preparation; other normalized paths are recorded separately. The published manifest states which files received further editorial redaction or home-path normalization and gives the final published hashes. This distinction prevents a redacted copy from being described as byte-identical to its private source. The [540-entry source disposition inventory](../data/handoff-source-dispositions.json) also records duplicates, third-party exclusions and private withheld artifacts using generic aliases.

[Browse the added archive](archive/handoff-copied.md), including [recoveries](archive/handoff-recovered.md) and [journal extracts](archive/handoff-journal-results.md). The claim index now also includes explicit supplementary records for results omitted from the original scaffold narrative; these retain their actual review levels.

## Reading the additions

Start with the [V3 branch-knot corollary and E6 scope](RESEARCH_MAP.md), the [new short proof](SMALL_RESULTS.md), and the [human-work correction guide](HUMAN_WORK_AND_CORRECTIONS.md). The latter separates source criticism from the project's own misreadings and credits existing results used in the investigation.

The recovered scripts are historical evidence. In particular, two BBB construction scripts import a missing patched helper and are not a runnable reconstruction of the full construction. Its verdict remains **UNDECIDED**. The recovered first `phi0.py` is not a replacement for the later authoritative recheck. The Sikora bracket-check script is preserved, but was not rerun during this publication update.

The BBB analysis describes what **appears to be a gap in the proof** of the specified version; **the theorem is not refuted**. The checks are **AI-only**, and incomplete geometric verification is stated explicitly. No authors have been contacted. The maintainer confirmed that no correspondence was sent; private drafts remain excluded from the archive.

## Deliberate exclusions and limits

Eight private artifacts remain withheld: correspondence drafts, contact/package READMEs, and an old PDF carrying private author/contact material. Their mathematical content is represented by the redacted notes and certificates. Some internal review reports also discussed draft correspondence; those passages were removed with visible redaction markers and transformation records.

The internal handoff instructions, private memory log and raw runtime journals are not published wholesale. Their identified mathematical content is carried by the artifact archive, the recovered-history guide, the attribution guide and the status supplements. Third-party papers and software retain their own terms and are cited rather than relicensed as original project material.

The gap register includes missing traces and patched scripts, unfinished checks, the incomplete literature-crawl bundle, and the limits of the underlying reads. In particular, **d2fix2 was not rerun and is not claimed**. The collaborators report no further *known* missing research artifacts outside those gaps. This is a bounded inventory conclusion, not a guarantee that every historic conversation or unsaved computation was recoverable.

## Reimport and verification

`tools/import_handoff.py` imports only the paths and hashes admitted by the public handoff manifest. It requires separately reviewed copies for editorially redacted records and has no raw fallback. `tools/export_sources.py` excludes the private handoff staging directory from automatic export and preserves these separately reviewed imports.

`python3 tools/validate.py` checks the distributed source hashes and guide links. It does not run historical programs, validate every quotation, confer external referee approval, or settle a mathematical claim.
