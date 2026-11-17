# Raw spanning-tree minimization still bounds crossing number

[Claim index](../CLAIM_INDEX.md) · [Evidence policy](../EVIDENCE_POLICY.md)

**Record type:** early handoff

**Status as recorded:**

```text
D/N
```

**Interpretation:** Historical status only; check later corrections. Internal review is not external specialist review.

## Statement and recorded scope

```text
MID-19  D/N  Raw spanning-tree minimization still bounds crossing number
------------------------------------------------------------------------
For a connected loopless bridgeless multigraph with an edge, tau(G)>=e(G).
Proof uses ear addition tau(H+ear_l)=l*tau(H)+F_uv(H) and multiplication over
blocks. Remove nugatory crossings from any knot diagram without changing
its Tait-tree count. Hence tau_min(K)>=c(K). Thus infinite Kanenobu exact
Jones fibers have unbounded MINIMIZED raw tree count, not merely bad chosen
diagrams. Counting all quasi-trees does not evade the generator bijection.
This kills raw-state compactness as an all-fiber rank proof, not actual Kh
rank boundedness after differential cancellations. Any proposed cancellation
algorithm must retain the invisible T(3,4) column and 10_132 spill above.
Proof/check: work/research24/spanning_tree_mechanism.txt,
verify_homology_examples.py, spanning_tree_checks.json.

------------------------------------------------------------------------
```

## Provenance

[Source record](../../archive/outputs/claude-handoff/RESULT_LEDGER.json). The source wording is retained; consult the chronology for later restrictions or withdrawals.

## Identified supporting artifacts

- [spanning_tree_mechanism.txt](../../archive/work/research24/spanning_tree_mechanism.txt)

These links identify recorded evidence; they are not a claim that the logical dependency list is complete.
