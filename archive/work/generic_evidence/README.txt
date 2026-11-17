Generic Jones unknot-detection bounded pass, 31 October 2026.

No generic proof or counterexample was obtained. No novelty claim is made.

Run these standard-library checks from this folder:
  python3 verify_jets.py
  python3 tangle_unit_check.py
  python3 commutator_nontrivial.py

The first replays all 8 exact Jones polynomials, confirms every closure is a knot,
and checks Taylor vanishing and the even leading coefficient.
The second checks 2,754 unit/inverse examples and the cap-absorption identity.
The third verifies exact Burau determinant recurrences through order 10.
Unbounded statements rely on the accompanying proofs, not finite checks.

Optional diagram check (requires Regina and Spherogram):
  python3 smoothing_homology.py
It recalculates all 44 resolutions of KT and Conway and their full H1.

main.tex is the four-page research-note source. Working notes contain fuller
arguments and source links. tl_exact.py is the exact TL engine used previously.

The tangle numerator certificate is replayed with Regina alone:
  python3 tangle_diagram_check.py
Use --regenerate to rebuild the tangle with Spherogram as well.
The JSON records the PD and every Reidemeister move, reducing 6 crossings to 0.

Diagram checks were verified with Python 3.13, Regina 7.4.1, and Spherogram 2.4.1.
Use versions compatible with your Python runtime.
