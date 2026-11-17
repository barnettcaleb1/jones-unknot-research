Jones unknot detection: second bounded pass, 31 October 2026

Outcome: no general proof and no counterexample.

1. Main exact certificate (Python standard library only):
   python3 braid_certificate/verify.py
   It checks all 144 infinite families using the unique-leading-term proof.
   An optional extra all-integer root audit is available; see its README.

2. Proofs and limits are in notes/. The general fixed-template lattice proof
   is elementary and makes no novelty claim. The tangle exclusion uses actual
   unlink band smoothings and Lobb plus Khovanov unknot detection.

3. The original research computations and saved records are in computations/.
   Python files there may overwrite their adjacent result JSON when run.
   The braid/categorical calculations use only the Python standard library.
   Tangle diagram reconstruction additionally requires Regina 7.4.1 and
   Spherogram 2.4.1 (tested with Python 3.13); packages are not bundled.
   The nonexistent optional local-package path in those scripts is harmless
   when both packages are installed in the active Python environment.
   Reproduce the 20,000-expression search by passing 20000 to tangle_search.py;
   then run tangle_search_diagrams.py. Smaller default runs overwrite results.
   Watson search records include the follow-up simplifier outcomes; an initial
   simplifier failure is not a nontriviality certificate.

4. independent_checks.py exercises the root solver on 1,505 synthetic cases,
   compares 940,625 points, and replays all 144 saved root certificates.
   These bounded regressions check implementation, not the unbounded proof.

No primary-source PDFs or external Python packages are bundled.
