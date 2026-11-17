REPRODUCIBLE EVIDENCE — 31 October 2026

No generic Jones unknot-detection proof or counterexample is claimed.
Read jones-finite-tests-and-cancellation.txt first. Novelty is unestablished.
The exact algebra verifiers listed below use Python3 standard-library arithmetic.
Extract this archive, retain its directory layout, and run from its root:

 python3 work/proof12/braid/all_color_collision_check.py
 python3 work/proof12/braid/finite_probe_determinant_check.py
 python3 work/proof12/homology/verify_one_special.py
 python3 work/proof12/tangle/kt_partial_filter.py
 python3 work/proof12/kt_twist_algebra_audit.py
 python3 work/proof12/tangle/kt_leading_verify.py

The first imports the included work/attack_search/search.py. Verifiers write
JSON outputs beside themselves. The archive also includes a prior torus
formula audit and the earlier all-odd-pretzel proof used for the KT bridge
restriction. Primary literature is linked in the research notes, not bundled.

The optional geometry reconstruction scripts in tangle/ require Spherogram
and Regina. These dependencies are not bundled. The stored initial/simplified
planar diagrams and cut-link polynomials are included. Algebra-only checks
can run without these external libraries; they do not independently recompute
the geometric cut-link polynomials.

The mathematical proofs cover all colors, all wrapping bounds, or all n in
their stated hypotheses. Finite exact checks are independent error checks,
not claims of exhaustive verification of the generic unknot problem.
