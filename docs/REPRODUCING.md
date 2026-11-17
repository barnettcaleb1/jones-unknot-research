# Reproducing results

## Portable entry checks

From a clean checkout with Python 3.10 or later:

```sh
python3 tools/validate.py
python3 checks/run_portable.py
```

The first command verifies included artifact hashes, catalog consistency, and links in the new reading guide. The second runs a small fixed set of standard-library exact certificates in temporary working directories. No knot enumeration or research search is launched.

The EF check derives the fourth-order coefficient from the stated published seed and the horizontal doubling recurrence. It is not an independent reconstruction of every diagram. The maps and ladder checks concern the explicitly specified formal complexes; they do not prove those complexes are realized by tangles. Read the associated proof note before interpreting a passing assertion.

## Historical programs

Programs under `archive/` are preserved as evidence, not advertised as a unified installed package. Many use SymPy, SageMath, Regina, SnapPy, kht++, custom local modules, or absolute paths from the original machines. Some write output files or start long searches. Inspect a program and its report before running it. The reproducibility audit lists these limitations.

Source mapping:

| Historical path | Snapshot location |
|---|---|
| `work/...` | `archive/work/...` |
| `outputs/...` | `archive/outputs/...` |
| `collab/...` | `archive/collab/...` |
| `~/jones-lanes/...` | `archive/claude/...` |

## Large evidence

`data/release-assets.json` lists the downloadable supplements, file counts, sizes, and SHA-256 hashes. Their tar members already begin with `archive/`; extract a verified supplement at the repository root to restore those historical paths. `data/artifact-manifest.json` records each file's source, disposition, size, and, for distributed research artifacts, hash.

Only use the release assets attached to the corresponding snapshot. Verify their hashes before extraction. The packages contain data and historical logs; reading a stored pickle with Python executes a serialization protocol and is not part of the default checks.

Third-party papers and software environments are not included as supplements. Retrieve the identified upstream version using the bibliography or dependency report. Missing source links and unpinned dependencies are explicit tasks, not evidence that the results have been reproduced.

## What a successful check establishes

Record the command, Python and library versions, input artifact hashes, expected output, and actual output. A passing fixed certificate validates its stated algebraic instance. To certify a theorem, also inspect the proof that reduces the entire stated domain to that certificate. To certify a search, audit input coverage and every filtering step as well as the surviving outputs.
