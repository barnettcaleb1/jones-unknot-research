Jones investigation: EKT band-fusion obstruction and completed braid classification
31 October 2026

The accompanying four-page proof establishes a restricted obstruction, not the
Jones unknot-detection conjecture. For any EKT two-component opposite-omega
orbit from a tangle with unknot numerator, every nonzero iterate has nonzero
branched-cover homology torsion. No band fusion of these links can yield a
Jones-trivial knot. The unlink seed is the excluded zero iterate.

The separate previous search is now completely classified: all 93 exact
Jones-one hits are unknots. The previous_search folder retains the original
91 braid certificates and historical report; its two formerly unresolved
entries are settled by the new braid_certificates folder. Those historical
unresolved labels are superseded by this supplement.

Checks:
  python3 homology/fox_braid.py
    Standard library only: independently verifies the published LL2(1) braid.
  python3 previous_search/bounded-jones-search/replay.py
    Standard library only: repeats the 93 exact polynomial checks and 91
    original braid certificates.
  python3 braid_certificates/replay_reidemeister.py
    Requires Regina; verifies the remaining two unknot certificates by moves.
  python3 homology/replay_homology.py
    Requires Regina; recomputes full-diagram Fox Smith forms from saved PDs.

For diagram reconstruction scripts in homology/, also install Spherogram.
Versions used: regina Python wheel 7.4.1, spherogram 2.4.1.
The platform-specific dependencies are not bundled. A local package directory
can be supplied through PYTHONPATH; the Reidemeister replay also accepts it
as its first command-line argument.

The scripts check finite examples and exact certificate steps. The arbitrary-
parameter proof, including the Mayer-Vietoris reduction for nonrational seeds,
is in the accompanying PDF and proof_source/main.tex. No novelty claim is made.
