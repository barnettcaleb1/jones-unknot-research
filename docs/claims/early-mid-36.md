# All-slope two-band algebra and one complete family exclusion

[Claim index](../CLAIM_INDEX.md) · [Evidence policy](../EVIDENCE_POLICY.md)

**Record type:** early handoff

**Status as recorded:**

```text
D/F
```

**Interpretation:** Historical status only; check later corrections. Internal review is not external specialist review.

## Statement and recorded scope

```text
MID-36  D/F  All-slope two-band algebra and one complete family exclusion
------------------------------------------------------------------------
For an actual oriented Jones-one anchor with two DISJOINT antiparallel
full-twist sites, induced smoothings S1,S2, double smoothing S12=delta^2,
put z=A^8=t^-2, u=S1/delta-1, v=S2/delta-1. Then for all m,n in Z,
 V_mn-1=u*z^n(1-z^m)+v*z^m(1-z^n).
Jones-one on an entire line(m,n)=(ak,bk) iff:
 a=b=0: automatic; a!=0,b=0:u=0; a=0,b!=0:v=0;
 a=b!=0:u+v=0; a,b nonzero unequal:u=v=0.
One exact K11 check certifies the whole diagonal; one nonzero axis point
certifies its axis; two k=1,2 points certify any fixed nonzero unequal slope.
These are complete polynomials, not numerical evaluations. Equal-and-opposite
u,v is a genuine FORMAL possibility; no realized nontrivial family supplied.
For the marked LLL(1) family based on prior hit5, exact determinant value
 V_mn(-1)=1-288(m+n)
forces n=-m. Its cut-link defects have unequal spans22,24 in x=sqrt(t),
so they cannot be Laurent monomial translates; every nonzero antidiagonal
point fails. Exactly (0,0) has V=1, and it is the actual unknot.
Independent audit checked five saved corners and the all-integer inference.
Later pass37 generalizes/certifies16 marked families and should supersede
older claims about how many records have established geometry.
Proofs: work/research34/twist_formula.txt, all_integer_audit.txt,
two_band_family.py/.json, verify_all_integer_formula.py. The tempting common-
phase surgery shortcut was NOT proved and was unnecessary.

------------------------------------------------------------------------
SECONDARY EXACT RESTRICTIONS AND SCOPE WARNINGS
------------------------------------------------------------------------
* Classical diagram/fork intersection: equal monomial exponents with opposite
  signs need not form removable empty bigons; specialization can erase an
  unspecialized faithful pairing. A sufficient unique/extreme-face sign
  certificate exists, but no generic coverage. work/research24/intersection_geometry.txt.
* Ribbon movie topology does not bound Kh complexity: fixed-genus/critical-
  point constructions can carry arbitrarily complex companions; distinguish
  relative Lee length from rank. work/research25/homology_global_mechanism.txt.
* Canonical connected-sum Smith inequalities in periodic Kh are automatic from
  dimension/Hopf facts and do not eliminate invisible states. Equivariant
  cobordism and Steenrod suggestions remained conditional.
  work/research27/homology_global.txt.
* Important source correction: 'unreduced integral Kh has no2-torsion => U'
  is NOT an established universal endpoint. It is Shumakovitch's conjecture.
  Gujral--Wang prove that a no2-torsion knot has reduced rational rank no
  greater than any one-proper-rational-tangle-replacement neighbor; this implies every
  nontrivial u=1 knot has2-torsion. One cannot iterate it through arbitrary
  crossing changes because the no-torsion hypothesis need not persist.
  Jones1 has not been proved to eliminate torsion even in the restricted case.
  See work/research27/homology_global.txt, section3.
* Exact Jones equality does not imply primeness, symmetric-union partial-knot
  equality, rational closure topology, or actual knot equivalence. Preserve
  source hypotheses instead of inferring geometry from matching polynomials.
* No literature search proving absence of fixed-Jones unbounded rank/bridge
  families was performed. The notes report bounded failures to locate them.
* Old notes say 'goal active'; this is HISTORICAL. The current standing goal
  is paused, and the present request is a handoff only.

------------------------------------------------------------------------
ARCHIVE INVENTORY AND REPRODUCIBILITY
------------------------------------------------------------------------
Include our .txt/.md reports, .py verifiers, small JSON exact certificates,
and saved PDs from the nineteen named directories. Source references are
embedded in those notes. Existing evidence ZIPs already organize many portable
subsets. Preserve relative directory layout because several verifiers import
earlier engines in work/attack_search, work/pass2 and work/proof12.

Exclude complete downloaded papers/cache texts, specifically:
 work/research21/watson_identical.txt
 work/research26/piwocki_traczyk_source_cache.json
as well as PDFs, figures, binary site-packages, __pycache__, and huge redundant
raw tables. Retain small primary-table excerpts only as documented necessary
data with their original source metadata; distinguish those from freshly
computed homology (we did not recompute all KnotInfo homology).

Important portable entry points (standard library unless noted):
 work/cancellation19/homology_k3_bracket_audit.py
 work/cancellation19/stoimenow_factor.py
 work/research22/verify_relative_bar_certificates.py
 work/research23/verify_fibered_filter.py
 work/research23/verify_fusion_variance.py
 work/research24/verify_homology_examples.py
 work/research24/verify_spectral_jets.py
 work/research24/braid_moment_filter.py
 work/research26/verify_watson_independent.py
 work/research26/verify_satellite_certificate.py
 work/research27/verify_bing_formula.py
 work/research28/verify_promotion_jet.py
 work/research28/verify_rank_one_twists.py
 work/research29/verify_colored_family.py
 work/research31/verify_torus_countertest.py
 work/research32/verify_twist_specializations.py
 work/research34/verify_all_integer_formula.py

Full diagram regeneration needs compatible Spherogram/Regina (historically
Spherogram2.4.1, Regina7.4/7.4.1, Python3.13). Do not ship local cp313 binary
wheels as universally portable. Some scripts overwrite adjacent deterministic
JSON reports; run in a copied extraction. Previous archives record successful
replays, but this handoff compilation did not rerun every computation.

Coverage: this ledger compresses repeated scaffolds and repeats of known
published inputs into shared records. It is a substantive result inventory,
not a claim every scratch paragraph or every computational candidate received
a fresh independent correctness audit on 2 November. For any claim chosen for
new work, read its named proof plus the latest audit/STOPPED notes first.
```

## Provenance

[Source record](../../archive/outputs/claude-handoff/RESULT_LEDGER.json). The source wording is retained; consult the chronology for later restrictions or withdrawals.

## Identified supporting artifacts

- [homology_k3_bracket_audit.py](../../archive/work/cancellation19/homology_k3_bracket_audit.py)
- [stoimenow_factor.py](../../archive/work/cancellation19/stoimenow_factor.py)
- [verify_relative_bar_certificates.py](../../archive/work/research22/verify_relative_bar_certificates.py)
- [verify_fibered_filter.py](../../archive/work/research23/verify_fibered_filter.py)
- [verify_fusion_variance.py](../../archive/work/research23/verify_fusion_variance.py)
- [braid_moment_filter.py](../../archive/work/research24/braid_moment_filter.py)
- [intersection_geometry.txt](../../archive/work/research24/intersection_geometry.txt)
- [verify_homology_examples.py](../../archive/work/research24/verify_homology_examples.py)
- [verify_spectral_jets.py](../../archive/work/research24/verify_spectral_jets.py)
- [homology_global_mechanism.txt](../../archive/work/research25/homology_global_mechanism.txt)
- [verify_satellite_certificate.py](../../archive/work/research26/verify_satellite_certificate.py)
- [verify_watson_independent.py](../../archive/work/research26/verify_watson_independent.py)
- [homology_global.txt](../../archive/work/research27/homology_global.txt)
- [verify_bing_formula.py](../../archive/work/research27/verify_bing_formula.py)
- [verify_promotion_jet.py](../../archive/work/research28/verify_promotion_jet.py)
- [verify_rank_one_twists.py](../../archive/work/research28/verify_rank_one_twists.py)
- [verify_colored_family.py](../../archive/work/research29/verify_colored_family.py)
- [verify_torus_countertest.py](../../archive/work/research31/verify_torus_countertest.py)
- [verify_twist_specializations.py](../../archive/work/research32/verify_twist_specializations.py)
- [all_integer_audit.txt](../../archive/work/research34/all_integer_audit.txt)
- [twist_formula.txt](../../archive/work/research34/twist_formula.txt)
- [verify_all_integer_formula.py](../../archive/work/research34/verify_all_integer_formula.py)

These links were resolved from explicit filenames, not inferred as a complete logical dependency list.
