# Classification of the two remaining Jones-one braid closures

The two previously unclassified words, entries 82 and 86 of the saved 40,000-word
search, are both unknots. This supplements the 91 existing braid certificates,
so all 93 exact Jones-one hits in that sample are now classified as unknots.
It does not establish the Jones unknot-detection conjecture or provide a new
exhaustive census.

| Entry | Initial crossings | Primitive Reidemeister moves | Breakdown |
|---|---:|---:|---|
| 82 | 35 | 70 | 16 RII deletions, 51 RIII, 3 RI deletions |
| 86 | 39 | 38 | 20 RII deletions, 15 RIII, 2 RI additions, 1 RI deletion |

Each move preserves the knot type. Each replay ends at a diagram with zero
crossings and exactly one component. Therefore each replay is an unknot
certificate, independently of the Jones and Alexander polynomials.

`reidemeister_certificates.json` gives the original braid words, initial planar
diagram codes, primitive moves, and exact diagrams before and after each move.
Crossing indices are zero-based and refer to the diagram at that step. Moves
are Regina's `Link.r1`, `Link.r2`, and `Link.r3` with their documented argument
conventions. An `r1add` operation gives the crossing index, strand number,
side, and crossing sign.

`replay_reidemeister.py` independently reconstructs each braid by tracking its
strands and building a signed Gauss encoding, checks that the resulting diagram
agrees with the saved planar diagram up to relabelling, checks each move's
applicability, and verifies each saved before/after diagram. It uses exact
combinatorial operations in Regina, with no numerical tolerances and no
polynomial-as-unknot criterion.

The independent braid encoder applies an ordinary three-dimensional rotation
to match the diagram convention used when producing the saved planar diagram.
The subsequent signature comparison allows relabelling only: reflection,
reversal, and further rotation are disabled.

The certificates were generated using Regina's Python wheel 7.4.1
(`regina.versionString()` reports 7.4), and the initial PD codes were generated
using Spherogram 2.4.1. Spherogram is not needed to replay them.

Install Regina, then run:

```
python3 replay_reidemeister.py
```

Alternatively, pass a directory containing the locally installed Regina package
as the script's first argument. In the research workspace this was:

```
python3 work/braid_classification/deliverable/replay_reidemeister.py work/braid_classification/packages
```

Regina's documented operations:
https://regina-normal.github.io/engine-docs/classregina_1_1Link.html

The second certificate adds a crossing when the diagram has 11 crossings and
again when it has 10 crossings. These temporary increases escape the local
minima encountered by the initial simplifier. The complete process never
exceeds the original 39 crossings. This explains the previous failure as a
limitation of that bounded search, not evidence of knot-theoretic novelty.
