Evidence for the 31 October 2026 continuation

Read outputs/jones-positivity-and-boundaries.txt first. No general Jones
unknot theorem or counterexample is claimed, and novelty is unassessed.

Proofs: tangle/findings.txt, tangle/unit_box_classification_audit.txt,
finite_certificate.txt, homology/result.txt, and
quantum/root_reflection_obstruction.txt under work/proof10/.

Standard-library reproduction commands, from the extracted root:
 python3 work/proof10/mixed_unit_independent.py
 python3 work/proof10/tangle/odd_pretzel.py
 python3 work/proof10/tangle/mixed_moments.py
 python3 work/proof10/homology/check_extremes.py
 python3 work/proof10/homology/composite_counterexample.py
 python3 work/proof10/quantum/root_reflection_check.py

Actual diagram cross-checks additionally require Spherogram and Regina:
 python3 work/proof10/tangle/odd_pretzel.py --diagrams
 python3 work/proof10/tangle/mixed_counterexample.py
Third-party packages are not bundled. The scripts also look for an optional
work/braid_classification/packages directory before the standard environment.

The KnotInfo polys.json input is a lossless projection to the three fields
used by these checkers: name, rational reduced Kh, integral unreduced Kh.
The complete metadata and saved result files are included. Official original
spreadsheet links and mathematical sources are recorded in homology/result.txt.
The very large original spreadsheets are not duplicated in this archive.

SHA256SUMS checks the exact archived contents, including the projected input.
