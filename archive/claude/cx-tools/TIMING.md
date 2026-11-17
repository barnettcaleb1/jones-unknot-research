# TIMING.md -- bracket.py speed on large diagrams (subprocess per case, timeout 100s)

| family | diagram | crossings | greedy width | max states | seconds | status |
|---|---|---|---|---|---|---|
| braid | random 4-strand braid closure, 60 cr. | 60 | 8 | 14 | 0.07 | ok |
| braid | random 6-strand braid closure, 60 cr. | 60 | 10 | 41 | 0.07 | ok |
| braid | random 8-strand braid closure, 80 cr. | 80 | 10 | 42 | 0.18 | ok |
| braid | random 10-strand braid closure, 100 cr. | 100 | 14 | 243 | 0.40 | ok |
| braid | random 10-strand braid closure, 200 cr. | 200 | 20 | 16795 | 61.65 | ok |
| braid | random 12-strand braid closure, 60 cr. | 60 | 8 | 14 | 0.07 | ok |
| braid | random 12-strand braid closure, 120 cr. | 120 | 12 | 131 | 0.62 | ok |
| braid | random 14-strand braid closure, 60 cr. | 60 | 6 | 6 | 0.07 | ok |
| braid | random 16-strand braid closure, 40 cr. | 40 | 6 | 5 | 0.02 | ok |
| random-map | random planar knot diagram (asked 40, got 40 cr.) | 40 | 10 | 26 | 0.02 | ok |
| random-map | random planar knot diagram (asked 60, got 60 cr.) | 60 | 12 | 132 | 0.10 | ok |
| random-map | random planar knot diagram (asked 80, got 80 cr.) | 80 | 16 | 562 | 0.21 | ok |
| random-map | random planar knot diagram (asked 100, got 100 cr.) | 100 | 16 | 590 | 0.40 | ok |
| random-map | random planar knot diagram (asked 120, got 82 cr.) | 82 | 16 | 1100 | 0.31 | ok |
| random-map | random planar knot diagram (asked 150, got 150 cr.) | 150 | 20 | 10713 | 6.83 | ok |
| random-map | random planar knot diagram (asked 200, got 200 cr.) | 200 | 20 | 10472 | 10.03 | ok |
| twist | clasp unknot + 25 full twists (52 cr.) | 52 | 4 | 2 | 0.04 | ok |
| twist | clasp unknot + 50 full twists (102 cr.) | 102 | 4 | 2 | 0.31 | ok |
| twist | clasp unknot + 100 full twists (202 cr.) | 202 | 4 | 2 | 2.36 | ok |

Largest crossing number finished in under 60 s: **202** (clasp unknot + 100 full twists (202 cr.), 2.4 s, width 4, 2 states).
- braid: 120 crossings in 0.6 s (random 12-strand braid closure, 120 cr.).
- random-map: 200 crossings in 10.0 s (random planar knot diagram (asked 200, got 200 cr.)).
- twist: 202 crossings in 2.4 s (clasp unknot + 100 full twists (202 cr.)).
