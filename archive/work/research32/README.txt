PASS 32 — EXTERIOR VOLUME AND FINITE JONES PROBES
1 November 2026 UTC

Main problem remains unresolved: there is no proof or counterexample to
ordinary Jones unknot detection in this archive. The persistent goal remains
active. The preceding goal turn made progress by producing and auditing the
projective crossing identity and closing its proposed span-bound route.

Current results:
1. A bound on TOTAL hyperbolic JSJ volume of knot exteriors in any ONE
   nonempty whole Jones fiber would prove detection. Every nontrivial graph
   knot has a2>0, whereas Jones-one implies a2=0; thus a hypothetical
   counterexample has positive exterior volume, amplified by connected sums.
   The required bound itself remains unproved.
2. For every finite Taylor order, finite set of ordinary root-of-unity
   evaluations, and volume threshold, there is a hyperbolic knot exceeding
   that threshold and matching the unknot at ALL those probes, with Delta=1.
   This is derived from published Brunnian-link and adjacency constructions.
   It does not assert an entire Jones polynomial equal to one.
3. New spectral and dyadic-representation frameworks were tested. Signed
   spectral observables retain only Jones Euler data; the dyadic algebra
   creates no automatic extra kernel beyond the finite braid kernels.

READING ORDER
geometric_mechanism.txt — complete exterior-volume conditional proof,
  source links, missing premise and research decisions.
exterior_volume_audit.txt — independent proof audit.
finite_probe_volume_obstruction.txt — simultaneous finite-probe construction.
finite_probe_independent_audit.txt — independent audit, including a separate
  unreduced all-color strengthening and its normalization limitation.
homology_mechanism.txt — exact signed-spectral obstruction.
actual_collision_check.json — actual same-Jones knot homology data.
quantum_mechanism.txt — dyadic kernel and normalization audit.
verify_twist_specializations.py — portable exact local arithmetic check.
twist_specialization_result.json — expected output.

Run the verifier with Python3; no external packages are required. It tests
48 primitive root orders and explicitly detects the order-eight exception.
The general theorem has a separate algebraic and geometric proof; those
48 cases do not prove a universal statement by themselves.

All new deductions received internal review only. No publication acceptance,
external review, or novelty claim is made. The complete current strategy is
recorded in outputs/jones-full-proof-scaffolds.md, Section15.
MANIFEST.json records SHA-256 and size of every other archive member.
