CREATIVE JONES RESEARCH PASS, 31 OCTOBER 2026
Start with outputs/jones-creative-pass.txt.
No knot counterexample or general detection proof is claimed.
The rank bounds use a December 2025 instanton preprint; see the source audit.
The isolating-Maslov deduction passed an independent local-diagram and gluing audit.
It is a restricted research deduction, with no novelty or general-resolution claim.

Run from any directory after extracting, using Python 3:
  python3 work/creative6/cyclotomic_formal_model.py
  python3 work/creative6/homology_formal_certificate.py
  python3 work/creative6/quantum_two_copy_test.py
These use the standard library. The last can take longer (exact rational matrices).
Sibling dependency files for the last script are included.

The graph experiments require Spherogram and Regina (not bundled):
  python3 work/creative6/statmech_bridge.py
  python3 work/creative6/activity_moments.py
They were run in the task environment with Spherogram 2.4.1 and Regina 7.4.1.
The tree helper also recognizes the original workspace's package directory,
but ordinary installed packages work. JSON certificates contain the results.

MANIFEST.json lists SHA256 for every evidence file. Source PDFs and screenshots
are not redistributed; primary-source links are provided in the notes.

Verification: all three standard-library scripts above were rerun successfully
from a clean extracted archive. Computed JSON outputs matched the originals.
