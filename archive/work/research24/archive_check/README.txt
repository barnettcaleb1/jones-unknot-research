JONES UNKNOT DETECTION: PASS 24 EVIDENCE
31 October 2026 America/Chicago / 1 November 2026 UTC

No proof of Jones unknot detection and no nontrivial Jones-one knot have
been obtained. These are research deductions and conditional scaffolds,
with no claim of novelty. The named published results are used as inputs;
the small verifiers do not independently prove those results.

START HERE
  jones-full-proof-scaffolds.md
    Living report, complete conditional chains, remaining gates, and
    falsified approaches. Sections 6 and 7 contain pass-24 additions.
  work/research24/homology_strategy.txt
  work/research24/braid_strategy.txt
  work/research24/geometric_strategy.txt
    Independent strategic reviews requested before further local work.

MATHEMATICAL NOTES
  spanning_tree_mechanism.txt
    All-diagram tree-count lower bound and actual-homology countertests.
  intersection_geometry.txt
    Geometric cancellation failures, specialization obstruction, and a
    sufficient extreme-face certificate with an unproved coverage gate.
  braid_kernel_route.txt
    Ito endpoint, four-moment criterion, separate topology requirement,
    and all-integer anchor-family exclusions.
  spectral_realizability_obstruction.txt
    Rational eigenvalues of actual pure-commutator TL matrices are one;
    complete splitting forces an identity matrix. Not braid faithfulness.
  split_spectrum_audit.txt and split_spectrum_second_audit.txt
    Two independent audits of that proof.

PORTABLE VERIFICATION
Extract the archive, preserve the directory layout, and run these from
its root with Python 3. No third-party packages or network are required:

  python3 work/research24/verify_homology_examples.py
  python3 work/research24/verify_intersection_examples.py
  python3 work/research24/verify_spectral_jets.py
  python3 work/research24/braid_moment_filter.py

The last two use the four included earlier modules under work/pass2,
work/pass3, and work/attack_search. Only the explicitly listed entry
points were rerun as part of this archive's portable verification.

The homology verifier checks arithmetic against the retained KnotInfo
10_132 record and the stated torus-knot formula. It is not an independent
Khovanov homology computation. The source table record was extracted
without changing its fields from work/proof10/homology/polys.json.
KnotInfo vector conventions:
https://knotinfo.org/descriptions/khovanov_reduced_rational_vector.html

The intersection verifier checks polynomial specializations and examples,
not existence of isotopies. The spectral verifier checks all 10 pure
generator first derivatives, the known kernel seed's two jets, and all
42 TL5 basis traces; the general spectral theorem uses the written proof.
The moment verifier uses exact finite-field polynomial gcd to exclude
all integer twists in four specified anchor families. It does not exclude
other seeds, more general anchors, or isolated power closures.

SHA256SUMS.txt lists checksums of every other packaged file. The archive
was extracted into a separate directory and all four verifiers rerun.
See the separate pass-23 archive for ribbon candidates and quantum norm
tests; those data are not duplicated here.
