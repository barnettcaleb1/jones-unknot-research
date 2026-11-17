JONES UNKNOT DETECTION: FINITE-ORDER REALIZABILITY AND GLOBAL GEOMETRY
Research pass 28, 1 November 2026 UTC

STATUS
No full proof or counterexample. These are mathematical research deductions
with exact algebra checks and independent internal audits; no novelty or
external peer-review claim. The original goal remains unresolved.

RESULTS AND LIMITS
1. Habiro's actual clasper inverses produce, for every N>=5, actual knots
   R_N with ordinary Jones 1+O(h^(N+1)) and reduced color-three Jones
   1+320h^5+O(h^6), in the convention q=e^h. Their whole ordinary Jones
   polynomials are provably nonunit, have at least N+1 terms, and cannot
   be mistaken for counterexamples. Connected sums imply that every
   realizable finite ordinary-Jones Taylor jet has unbounded bridge
   number and reduced rational Khovanov rank.

2. The particular completed ratio Z(5_1)/Z(10_132), with chirality fixed
   by explicit braids, is NOT an exact-realization candidate: its color-
   three value fails Laurent polynomiality by an exponent-span argument.
   Actual realization to every finite order does not supply one finite knot.

3. Finitely many unmarked Dehn-filling parents for double branched covers
   in one whole Jones fiber would prove detection by Grushko and Smith.
   No theorem deriving this premise from Jones data was found. A family
   of actual ribbon knots shows that determinant, signature, Casson-Walker,
   correction term, simplicial volume and HF-hat rank together do not
   supply the required cover-group bound.

4. In the residual five-dimensional B5 Jones block, three-puncture full
   twists are scalar plus rank-one projectors. Different enclosed subsets
   have classical projector overlap1/9, so their images cannot commute,
   even for arbitrary nonzero powers and geometric winding. Equal generic
   projectors for distinct same-subset curves would finish a counterexample
   route via Long/Ito. No such equality was found.

FILES
The main notes and audit records are in work/research28/.
Older exact arithmetic engines are included only as verifier dependencies:
  work/attack_search/search.py
  work/pass2/braid_kernel.py
  work/pass2/tl5_block.py
The exact ordinary/color-three input is recomputed by
  work/proof12/braid/all_color_collision_check.py
Explicit braid words fix chirality; table names alone are not used to
choose signs or normalization.

REPRODUCIBILITY
From the extracted archive root, with standard Python only:
  python3 work/research28/verify_promotion_jet.py
  python3 work/research28/verify_rank_one_twists.py
  python3 work/proof12/braid/all_color_collision_check.py

These check the finite Laurent arithmetic, projector formulas and input
braid calculations. They do not verify Habiro's theorem, Smith's theorem,
topological realization of inverse representatives, or any missing global
assumption. General conclusions have separate mathematical arguments in
the notes. No explicit diagrams of the arbitrary-order inverse knots are
claimed. Some scripts rewrite their adjacent deterministic JSON reports.

The archive manifest records SHA-256 hashes of all other members.
Primary sources are linked in the notes; complete papers are not bundled.
The living synthesis is outputs/jones-full-proof-scaffolds.md.
