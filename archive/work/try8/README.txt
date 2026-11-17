REPRODUCIBLE EVIDENCE: CONCRETE JONES EXPERIMENTS, 2026-10-31

Read outputs/jones-concrete-experiments.txt for scope and conclusions.
No proof of Jones unknot detection or Jones-one nontrivial knot is claimed.

Extract the archive into an empty directory and run from its root.
The exact algebra and quiver computations require Python 3 and, for the
enumerator, a C++ compiler. The geometric checks additionally require
Spherogram and Regina in the Python environment. External packages and
compiled binaries are not bundled. Some scripts also check the original
workspace's local package directory; ordinary installed packages work.

Algebraic proof covering all integer twists (standard library only):
  python3 work/try8/tangle/processive_certificate.py

Regenerate its geometric checks:
  python3 work/try8/tangle/processive_certificate.py --diagrams

Verify the mirror repair produces U and 10_153:
  python3 work/try8/tangle/mirror_geometry.py

Quiver orbit partition, exhaustive enumeration, and independent audit:
  python3 work/try8/quiver/prepare.py
  c++ -O3 -std=c++17 work/try8/quiver/search.cpp -o work/try8/quiver/search
  work/try8/quiver/search
  python3 work/try8/quiver/audit.py

Expected enumeration counts:
assignments=29106000, row_square_zero=141944,
third_derivative_zero=455, fourth_derivative_correct=2,
fifth_derivative_correct=0, full_H4_Habiro=0.
Confirm assignments equals total; a timing cutoff in the enumerator must
not be mistaken for a completed search. The recorded run was complete.

The JSON files contain original and reduced planar diagrams, normalized
Jones polynomials, exact Laurent coefficients, and the last two quiver
matrices with their failed divisibility checks. Independent audit notes
explain the conventions and exhaustive reductions. Earlier algebra
helpers used as dependencies are included under work/generic and work/bio7.
