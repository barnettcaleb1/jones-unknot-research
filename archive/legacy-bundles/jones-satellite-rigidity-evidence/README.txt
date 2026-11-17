JONES SATELLITE RIGIDITY — REPRODUCIBLE EVIDENCE
31 October 2026

Start with outputs/jones-satellite-rigidity.txt. The general Jones unknot
problem is not solved by these notes. No novelty claim is made.

After extracting, these checks use only Python 3 standard library:
  python3 work/proof11/torus_source_audit.py
  python3 work/proof11/braid/satellite_frequency_check.py
  python3 work/proof11/braid/markov_moment_check.py
  python3 work/proof11/homology/verify_obstructions.py
  python3 work/proof11/tangle/coupled_determinant.py
  python3 work/proof11/tangle/coupled_sampling.py

The last command recomputes Jones polynomials and replaces its JSON with
fresh results. Its optional --diagrams mode additionally needs Spherogram
and Regina, which are not bundled. The supplied JSON retains the actual
PD codes and Regina results from that independent check.

The KnotInfo input is restricted to two rows and four relevant columns;
this is enough to reproduce the mirror-norm calculation. Original source:
https://raw.githubusercontent.com/knotinfo-org/assets/main/knot_polys.xlsx.zip
https://knotinfo.org/homelinks/database_download.php

The infinite statements are proved in the notes. Finite arithmetic checks
confirm conventions and examples, not universality. Prior proof10 source
files referenced for background are not included unless listed in SHA256SUMS.
