GLOBAL HYPOTHESIS TESTS — 31 OCTOBER 2026 LOCAL DATE

STATUS
No proof of Jones unknot detection and no counterexample has been found.
The full goal remains open. These are bounded tests of the central
assumptions in jones-full-proof-scaffolds.md, not substitutes for a proof.
No novelty claim is made for the derived implications.

MAIN REPORT
jones-full-proof-scaffolds.md is a snapshot of the updated main report.

GEOMETRIC AND QUANTUM TESTS
global_fiber_test.txt derives a restricted theorem from Wang's results:
a Jones-constant non-nugatory band-twist orbit has only finitely many
Euler-efficient members; with split smoothing it has none. No generic
reduction from a hypothetical Jones-one knot is supplied.

markov_global_constraints.txt proves the exact obstruction to treating
Markov-related presentations as independent quantum measurements.

ribbon_global_geometry.txt records a complete conditional axis-extension
route, its still-unproved bridge from ordinary Jones, and the explicit
failure of the arbitrary cyclic-disk-complement shortcut.

satellite_same_genus_appendix.txt checks that equal Seifert genus is NOT
an obstruction to ribbon concordance. Standard Whitehead satellite
examples already give distinct prime genus-one pairs. They are not
claimed to have the same Jones polynomial.

FINITE CANDIDATE SCREEN
candidate_filter_audit.txt gives definitions, counts, coefficient fields,
data limitations, and the independently checked screening argument.
The 12,965 cached KnotInfo polynomial records give 460 directed pairs
with equal Jones and strict rational reduced-Kh dominance. Necessary
conditions initially reduce these to 54, or 27 simultaneous-mirror orbits.
The stronger relative Lee-bar obstruction below reduces them further to
48, or 24 mirror orbits. No ribbon concordance is certified for any pair.

one_band_relative_rank.txt derives the relative graded Lee-bar constraint
from Sarkar's operator identities and graded PID decomposition. The
independent topology audit checks its module-to-complex step. With d
births and saddles, only additional bars X^a with 1<=a<=d are possible.
For d=1 the reduced rational rank difference must be divisible by four.
This does NOT establish the general rank-mod-four concordance conjecture.

ribbon_relative_bar_filter.json and its accompanying audit test the
positive-bar decomposition. Six directed pairs fail at every positive
bar length, so are excluded for ANY ribbon concordance, subject to the
table's homology values. Among the 48 remaining pairs, 42 pass the
one-band test and six need at least two births/saddles. These tests give
necessary conditions only.

verify_relative_bar_certificates.py is a standalone certificate checker:
run it with Python 3 beside the archived JSON files. It uses only the
included 47-row subset and the Python standard library. It independently
reconstructs all 54 defects, verifies all matching/minimum-cut certificates,
checks isolated-grade obstructions for the six failures, and reconstructs
the 42 nonnegative one-band quotients. All checks passed.
ribbon_bar_survivors.json separately retains the final 48 pairs, involving
42 underlying table knots; the earlier 54-pair file is preserved.

audit_candidate_filter.py and audit_integral_torsion.py reproduce the
whole-table audit in the existing workspace. They use the large cached
KnotInfo data under work/proof10/homology; those entire downloads are not
duplicated here. candidate_source_subset.json retains all 47 endpoint
records, their small metadata records, and hashes of the full inputs.
The independent audit JSON retains signature and tau values as well.
Primary source: https://knotinfo.org/ . Documentation links are in the
audit text. Homology values are table data, not fresh homology runs.

verify_candidate_polynomials.py independently recomputes Jones from the
47 endpoint PDs using the retained frontier bracket evaluator; its
machine-readable output records chirality conventions. The evaluator is
included as independent_pd_bracket.py for inspection, although the script
paths are laid out for the existing workspace.

small_band_screen.py screened one retained diagram for each of 25 target
names, with shortest dual paths, length at most2 (at most3 for two targets),
and at most2 half-twists. Across 5,732 bands, the simplifier recognized no
split unknot to remove. This is NOT a proof that any candidate lacks a
ribbon concordance, a split smoothing, or a longer-band presentation.
The trefoil#stevedore positive control finds the expected trefoil endpoints.

The Dunfield-Gong public concordance dataset was located in the literature
but was NOT downloaded or tested: the author's linked archive returned
404, and the public metadata endpoint returned403. The finite screen here
uses the already retained KnotInfo records and actual band generation,
not an implied comparison with that unavailable graph.

PROVENANCE
MANIFEST.sha256 lists the archived files. Primary-source URLs and the
distinction between established results, derived consequences, unproved
assumptions, and finite computations are retained in the individual notes.
