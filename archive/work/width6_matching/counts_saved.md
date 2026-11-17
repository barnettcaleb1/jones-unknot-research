# Five fixed archived zero examples: matching counts

Computed from `c3_samples.json` for the five labels selected before computation. Each exact `(word,i,j)` was located in `probe_candidates.json` and `topology_results.json`; all have two arcs, e-type connectivity, no closed components, and zero id-coefficient. The JSON records the archive index and saved split certificate classification.

These are **unsimplified canonical geometric representatives obtained from the stored cap-braid lifts** and the exact PL instrument, not a recovery of planar coordinates from the original knot-diagram archive (which saved braid/cap data). No cap slides or source-curve simplification were performed. Target figure-eight return connectors retrace; the counts are geometric intersection incidences/preimages of parametrized cycles.

| saved example | one-point count matrix | matching 0 product | matching 1 product | sum |
|---|---|---:|---:|---:|
| identity, i=0,j=6 | [[4,1],[18,11]] | 44 | 18 | 62 |
| sigma1^-3, i=0,j=6 | [[28,1],[48,11]] | 308 | 48 | 356 |
| Ren standard, i=1,j=7 | [[182,214],[705,811]] | 147,602 | 150,870 | 298,472 |
| arc commutator, i=0,j=7 | [[1683,757],[3992,1610]] | 2,709,630 | 3,021,944 | 5,731,574 |
| product of conjugates, i=0,j=7 | [[127,121],[106,260]] | 33,020 | 12,826 | 45,846 |

All counts are exact rational segment intersection counts with transverse-intersection guards passing. No exponent enumeration was needed. The five runs took approximately 0.25, 0.47, 4.97, 12.02, and 1.21 seconds.

All five chosen representatives have nonempty configuration intersection sets despite their archived splitness and Jones-zero pairing. This does **not** show cap slides are required to make the matching count zero: previous instrument work already reduced the arc-commutator example using ordinary arc isotopies alone to one-point matrix [[1,1],[0,0]], hence zero pairs. That saved evidence is `../width6_instrument/prior_zero_arc_commutator_simplified.json`. The present counts give no minimum and do not establish Conjecture N or the proposed split criterion.

Reproduce with `python3 work/width6_matching/counts_saved.py`. Data: `counts_saved.json`.
