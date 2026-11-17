EVIDENCE FOR THE BRUNNIAN REDUCTION AND EXACT SEED TEST
31 October 2026

Read outputs/jones-brunnian-reduction-and-exact-test.txt first.

Principal mathematical notes:
  work/cancellation19/adjacency_amplification.txt
  work/cancellation19/adjacency_amplification_braid_audit.txt
  work/cancellation19/brunnian_reduction.txt
  work/cancellation19/homology_brunnian_audit.txt
  work/cancellation19/algebra.txt
  work/cancellation19/geometry.txt

These give conditional reductions, exact algebra, and restricted geometric
obstructions. They do not establish the existence of a Jones counterexample
or a generic unknot-detection theorem. No claim of literature priority is made.

The short adjacency proof uses the chosen source knot's known nontriviality
and the knot-complement theorem. The more general CGLS argument elsewhere
in these notes is optional; it is not needed for that short proof.

Exact concrete certificate:
  work/cancellation19/stoimenow_exact_seed.txt
  work/cancellation19/stoimenow_k3.json
  work/cancellation19/stoimenow_k3.py
  work/cancellation19/stoimenow_versions.json
  work/cancellation19/stoimenow_factor.py/.json
  work/cancellation19/homology_k3_bracket_audit.py/.json

From the extracted archive root, these checks require only Python 3's
standard library:

  python3 work/cancellation19/homology_k3_bracket_audit.py
  python3 work/cancellation19/stoimenow_factor.py

The first independently contracts the original eight 38-crossing PD
diagrams, without Regina, Spherogram, or diagram simplification, and compares
every Laurent coefficient. The second checks the complete factorization.
Both were rerun successfully by the parent agent.

To reconstruct the diagrams and repeat the actual geometric simplifications,
stoimenow_k3.py additionally requires Spherogram and Regina. Tested versions
are recorded in stoimenow_versions.json. Its optional local package path can
be ignored when these packages are installed normally. The script writes
its eight results to work/cancellation19/stoimenow_k3.json.

The exact polynomial is nonconstant. Each of the seven nonempty marked-
crossing changes was separately simplified to a crossing-free unknot; those
topological claims do not rely on inferring unknot type from Jones=1.

The archive contains our derivations, data, and computational checks. It does
not include downloaded papers or copies of their figures. Primary references
are linked in the report and proof notes.

Foundational cap and unknotting-one details from the preceding pass:
  work/transmission18/unknotting_one_reduction_audit.txt
  work/transmission18/whitehead_factor_check.py
  work/quotient17/sato_levine_skein_injectivity.txt

The prior Whitehead-clasp converse failed. The present Brunnian construction
repairs the existence reduction by a different geometric operation; it does
not validate the failed clasp argument.
