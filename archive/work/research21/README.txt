GLOBAL SCAFFOLD AUDIT — 31 OCTOBER 2026 (LOCAL DATE)

This archive records a bounded research pass toward Jones unknot detection.
It contains conditional proof architectures, derived restricted results,
countertests to proposed methods, and independent internal audits.
It is not a proof of Jones unknot detection and makes no novelty claim.

START WITH
  jones-full-proof-scaffolds.md
The main report separates established implications from unproved premises.

DERIVED RESTRICTED RESULTS
  geometric_bridge.txt
  watson_topology_audit.txt
    For the precise mirrored-three-braid Watson shell, determinant one
    forces the two-bridge base to be the unknot. A marked geometric
    reduction then identifies the output with the connected sum of its
    input denominator closures. This rules out that shell as a first
    generic-to-unknotting-number-one converter.

  watson_homology.txt
  watson_rank_audit.txt
    A fixed Watson compensating-twist orbit has a fixed finite Khovanov
    bigrading support window, including nonsimple input tangles. This
    does not bound ranks inside the window or across arbitrary templates.
    The formal mapping-cone example is not asserted to be a knot complex.

FULL CONDITIONAL ARCHITECTURES
  global_homology_bridge.txt
    Sublinear support or geometric-complexity targets would close a proof;
    their required global geometric constructions remain missing.
    Factor-by-factor skein moves provably cannot supply the sublinear
    quantum-support target for a knot of positive homological spread.

  ribbon_euler_audit.txt
    A ribbon-concordance complement with zero Euler polynomial is the
    proposed rigidity target. Assuming it vanishes, the K#mirror(K)
    construction gives a complete generic proof. The premise is unproved.
    Wang's split-band theorem provides a specific test and sharply
    distinguishes fixed-Jones rank bounds from support bounds.
    The appendix proves conditionally that H-rank and H-spread together
    would make every Jones-preserving crossing change nugatory. This
    calibrates the strength of the proposed global hypotheses.

  ribbon_norm_architecture.txt
  ribbon_euler_faithfulness_audit.txt
    Reflection does not upgrade a single ordinary Jones scalar to a
    full-state norm. The Khovanov Frobenius algebra is not positive under
    movie reversal. Concrete knot examples also defeat proposed sign
    and extreme-parity shortcuts.

LITERATURE AND CONVENTION CHECKS
  fiber_bound_audit.txt
    Bounded primary-source search; not an exhaustive literature claim.

  watson_degenerate_check.py
  watson_degenerate_check.json
    Eight small diagram checks support convention choices. The universal
    topological argument does not infer its conclusion from these checks.

Any later additions are identified by their descriptive filenames.
All files are listed with SHA-256 hashes in MANIFEST.sha256.
Primary-source URLs appear in the individual notes.
