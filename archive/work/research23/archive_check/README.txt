Jones unknot detection: global geometry and quantum tests
Research pass 23, 1 November 2026 UTC (31 October local time).

STATUS
No proof of Jones unknot detection, no counterexample, and no certified
ribbon concordance among the seven surviving candidate classes.
No novelty or publication-readiness claim is made.

The report snapshot gives the complete conditional proof scaffolds and
identifies every missing global premise. The individual notes distinguish
published inputs, our deductions, finite calculations, and unproved targets.

MAIN RESULTS
1. Fibered-target/equal-genus rigidity reduces the previous 48 directed
   ribbon-E candidates to 14, or seven simultaneous-mirror classes.
2. One-band ribbon concordances cannot connect any of these distinct
   equal-genus endpoints. Every possible movie needs interacting bands
   and a regular level with at least three components. The prior local
   one-band search was unnecessary. An independent topology audit and
   a sharp two-birth Whitehead example are included.
3. The actual torus family T(3,3k+1) has three Jones coefficients of
   magnitudes 1,1,1 and reduced rational Khovanov rank 4k+1. This rules
   out amplitude-only rank bounds, not fixed-whole-polynomial bounds.
4. The trefoil ribbon double gives variance -24 for the proposed fusion
   moment functional at level four. Ribbonness alone does not give
   positivity of that functional. The Jones-one-restricted positivity
   conjecture and the separate AJ premise remain unproved.
5. Quantum braid Floer homology offers a conditional connected-sum
   argument through a presentation-minimized rank bound. That bound is
   unproved. Exact calculations show that its invariant polynomial
   quotient contains exactly the Alexander/Jones pair, while actual
   unknot presentations already have rank lower bounds 3,5,9.

PORTABLE CHECKS (Python standard library; run in this extracted folder)
python3 verify_fibered_filter.py
python3 verify_torus_norm_obstruction.py
python3 verify_quantum_floer_polynomials.py
python3 verify_fusion_variance.py

The first uses the small table subset and previous 48-pair certificate.
It independently recomputes the HFK top-rank criterion and checks every
new exclusion and surviving mirror class. The mathematical criterion
does not depend on the spreadsheet's separate fibered metadata field.
The original fibered_target_filter.py is retained as provenance for the
additional full-spreadsheet cross-check; unlike the portable verifier,
it requires the original large workspace database and xlrd installation.

The other three scripts check the stated exact arithmetic and finite
polynomial records. The torus-family all-k statement comes from the
published block formula and the symbolic telescoping proof in the note;
checking 20 examples alone is not a proof for all k. The scripts do not
prove the published topology or Floer theorems, recompute table homology,
or certify the existence of any ribbon movie among the candidate pairs.

INPUT PROVENANCE
candidate_source_subset.json and ribbon_bar_survivors.json come from the
preceding pass. The subset includes source hashes and retained KnotInfo
records. The preceding full relative-bar audit, proof, and certificate
verifier are in outputs/jones-global-hypothesis-tests.zip, delivered with
the previous pass. No large spreadsheet or source-paper PDF is bundled.
Primary-source links and precise theorem locators are in the notes.

MANIFEST.sha256 lists every other archived file. All four portable
checks were run successfully from a fresh extraction, and archive CRCs
and manifest hashes were checked.
