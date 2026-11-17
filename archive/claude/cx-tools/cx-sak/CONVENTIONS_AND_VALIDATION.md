# cx-sak: conventions, construction, validation (detailed companion to REPORT.md)

Directory: /private/tmp/claude-501/-Users-calebbarnett/7610ac96-4d03-4d32-b526-8a5647837809/scratchpad/cx-sak/

## Code
* `kb.py` – own exact Kauffman bracket by planar contraction (states = perfect matchings of the
  open edges, Laurent polynomials in A as dicts).  PD convention: `[a,b,c,d]` counterclockwise from
  the incoming under-edge; A-smoothing joins (a,b),(c,d); `<O>=1`, `delta=-A^2-A^-2`;
  `V(t)=(-A^3)^(-w)<D>`, `t^(1/2)=A^(-2)`; crossing sign +1 iff the over strand runs d->b.
  Jones polynomials are stored as `{k: coeff}` meaning `sum coeff*t^(k/2)`.
  Snape/Khovanov normalisation: `J(q) = V(t)` at `t^(1/2) = -q` (Snape Def. 3.2.2 and his remark).
* `validate_kb.py` → `out/validate_kb_output.txt`: all 12 Knot Atlas entries in cx-tools/katlas_reference.json
  (3_1, 4_1, 5_1, 5_2, 6_1, 7_2, 7_4, 8_1, 8_19, 10_132, K11n42, L2a1) reproduced exactly (chirality
  included); geometric Hopf links of both signs (lk = ±1 → V = -t^(±1/2) - t^(±5/2)), a geometric
  2-component unlink diagram (V = -t^(1/2) - t^(-1/2)) and a geometric (2,3) torus knot.
* `geom.py` – centripetal Catmull-Rom sampling, grid segment-intersection finder, PD extraction from a
  generic rotated projection (returns PD, crossing signs, components, linking matrix), τ-symmetric lift,
  anti-equivariant normal field with framing correction, quotient map, Gauss integral (sanity only).
* `templates.py` – Snape Fig. 1.10 template I_1(α_1..α_m; c_1..c_m), m = 1, 2, with the port wiring
  1–6 of `work/next_theory/sakuma_template.md` / recipe §1 (axis = y-axis; central α boxes vertical on
  the axis; side boxes labelled −c_j horizontal; connectors crossing-free; exterior arcs straight through
  the two fixed points).  Glyph: positive label → NW–SE strand over (Snape p.21).  For the horizontal
  side boxes the glyph is ROTATED with the box (positive → NE–SW over); see calibration below.
* `pipeline.py` – the full construction and all checks; `run_*.py` drivers; `fig22_model.py` – explicit
  space-curve model of the link drawn in Snape's Figure 2.2.

## Construction (recipe §2–3, implemented literally)
1. Planar symmetric diagram from the template (mirror-symmetric waypoint list, traversed along the knot),
   sampled at arclength spacing 0.005.  Lift: z = +h on the over strand and −h on the under strand at
   every crossing (C² bumps of half-width 0.6, h = 0.4).  τ(x,y,z) = (−x,y,−z); the lift is verified to
   satisfy τK = K exactly (mirror index map, max error < 1e-6) and the found planar crossings are
   matched one-to-one with the template's crossing markers (count and over-strand direction).
2. Writhe x of the symmetric diagram from the PD of the z-projection; Jones polynomial and det(K)
   from the same PD.
3. Normal field v = normalize(e_z − (e_z·T)T) (framing = x).  Correction: rotate v right-handedly
   about T by θ = 2π(−x)·S(u) on the τ-symmetric straight run of the top exterior arc through the top
   fixed point, with S(1−u) = 1−S(u) (plateau profile: twisting kept in |x_coord| ∈ [1.5, 8]·… away from
   the fixed point).  This is anti-equivariant for every integer −x (odd included), checked numerically.
   λ_+ = K + εv' (ε = 0.1), λ_- = τλ_+ = K − εv'.
4. Cover checks (generic projection, exact crossing counts): lk(K,λ_+) = lk(K,λ_-) = lk(λ_+,λ_-) = 0
   in every run (also for framed variants with the requested lk).  Gauss integral as a rough sanity
   check (it is coarse for the tight correction helices of the pilots; the crossing count is exact).
5. Quotient p(x,y,z) = (x²−z², y, 2xz).  U = B = y-axis (closed by a far rectangle on the left, oriented
   upward), c = L = p(λ_+).  PD of B ∪ L from a generic rotation (two different rotations, must agree).
   Checks: 2 components, lk(B,L) = 0, Jones(L alone) = 1.
6. Exact Jones polynomial of S = B ∪ L via kb.py; verdict = equality with −t^(1/2) − t^(−1/2).

## Calibration results (exact)
* Glyph convention: with the upright glyph in the side boxes I_1(2;1) is a trefoil (V = t+t³−t⁴); with
  the rotated glyph it is the figure-eight (V = t⁻²−t⁻¹+1−t+t², det 5).  Rotated is used throughout.
  With it: I_1(2;−1), I_1(1;1) are trefoils, I_1(2;2) is 6_1, I_1(±1;∓1), I_1(k;0) are unknots, and the
  pilot templates give K with det 32n²−1 and the Jones polynomial of spherogram's
  RationalTangle(32n²−1, 16n²+2n−… ) closure (both inversions give the same knot; chirality matches
  the K(p/(p−q)) convention of spherogram).
* Strongly invertible unknot: I_1(0;0) (round circle, x=0), I_1(1;0) (x=1), I_1(−1;0) (x=−1),
  I_1(2;0) (x=2, two coils), I_1(1;−1), I_1(−1;1) (3-crossing unknot diagrams): S = 2-component unlink
  in every case (V_S = −t^(1/2) − t^(−1/2)).
* Figure-eight I_1(2;1) (x = 0):
  V_S = −t^(−5/2) + 2t^(−3/2) − 3t^(−1/2) + t^(1/2) − t^(3/2) + t^(7/2) − 2t^(9/2) + 2t^(11/2) − 2t^(13/2) + t^(15/2),
  i.e. J_S(q) = q⁻⁵ − 2q⁻³ + 3q⁻¹ − q + q³ − q⁷ + 2q⁹ − 2q¹¹ + 2q¹³ − q¹⁵.  I_1(−2;−1) gives the mirror.
  25 crossings raw (snappy simplify: 16), both components unknots, lk = 0, hyperbolic volume 9.2718866842.
  Stable under ε ∈ {0.05, 0.1, 0.12}, h ∈ {0.3, 0.4, 0.5}, spacing ∈ {0.0025, 0.005}, two projections.
* Snape Example 3.2.6 states J(4_1,h_1) = q⁻⁹ − 3q⁻⁷ + 4q⁻⁵ − 3q⁻³ + 3q⁻¹ − q + 2q⁵ − 2q⁷ + 2q⁹ − q¹¹.
  This is reproduced EXACTLY by the framed Sakuma link with lk(K,l) = +2 (run_framed.py), not by the
  preferred-framing link; framings −3..3 were computed, only +2 matches (h_2 = mirror ↔ −2).
* Trefoil: I_1(1;1) (3 crossings, x = 3, one coil) and I_1(2;−1) (4 crossings, x = 4, two coils) give the
  same V_S = −t^(−3/2) + t^(−1/2) − 3t^(1/2) + 2t^(3/2) − t^(5/2) + t^(9/2) − 2t^(11/2) + 2t^(13/2) − 2t^(15/2) + t^(17/2)
  (J_S(q) = q⁻³ − q⁻¹ + 3q − 2q³ + q⁵ − q⁹ + 2q¹¹ − 2q¹³ + 2q¹⁵ − q¹⁷); the mirror diagrams give the mirror.
  snappy: volume 8.9973519436, identified as L14n10047 for both diagrams.
* Snape's Figure 2.2 (trefoil, drawn with his clasp/coil/twist rules and Lemma 2.1.2: two opposite clasps,
  one coil, four NE–SW-over twists) modelled as an explicit space curve (fig22_model.py, 17–18 crossings,
  lk = 0, L unknot) has Jones polynomial equal to the MIRROR of the above (chirality of the drawn trefoil),
  i.e. Snape's own drawing conventions agree with this construction at preferred framing.  Only the
  Example 3.2.6 numbers disagree (they are the ±2-framed links).

## Files per run (out/)
`<tag>_knot.json` (PD of the symmetric diagram, writhe, Jones, det, cover linking numbers),
`<tag>_sakuma_proj0.json`, `<tag>_sakuma_proj1.json` (PD of S = B ∪ L with crossing signs, component edge
lists, linking matrix, Jones polynomial in both normalisations), `<tag>_log.txt`.

## Pilot facts (n = 5), both inversions
* Symmetric diagrams: 34 crossings, writhe 14, det 799, same Jones polynomial for both inversions,
  equal to spherogram's RationalTangle(799, 389).numerator_closure() (the mirror convention of
  K(799/410)); so the two templates are strong inversions of the same knot, as Prop. 1.2.11 states.
* Correction: −14 turns (plateau profile) on the top run; cover lk(K,λ±) = lk(λ+,λ−) = 0 exactly.
* I_1(2,2;−10,5): S has 181 raw crossings (B–L 20 = 2 clasps×2 + 4 coils×4; snappy-simplified 75),
  lk = 0, both components unknotted (snappy sublinks simplify to 0 crossings; Jones(c) = 1),
  bracket cutwidth 14 (greedy), two projections agree.  V_S ≠ unlink.
* I_1(−10,20;−1,−1): S has 187 raw crossings (B–L 124 = 2×2 + 30 coils×4; snappy-simplified 159),
  lk = 0, both components unknotted, bracket cutwidth 12 (sweep 105° / greedy), two projections agree.
  V_S ≠ unlink (span t^(−57/2)..t^(125/2)).
* The Gauss-integral sanity values printed in the logs (−0.06, −1.26) are artefacts of subsampling
  the tight 14-turn helices; the exact crossing counts are the certification.

## Pilot facts (n = 10), both inversions
* Symmetric diagrams: 64 crossings, writhe 24, det 3199 = 32·100−1, same Jones polynomial for both
  inversions, equal to spherogram's RationalTangle(3199, 3199−1620).numerator_closure().
* Cover lk(K,λ±) = lk(λ+,λ−) = 0 exactly (−24 turns of correction).
* I_1(2,2;−20,10): S has 489 raw crossings (B–L 20; snappy-simplified 150), lk = 0, both components
  unknotted (Jones(c) = 1; snappy sublinks 0 crossings), two projections agree (489 vs 555 crossings),
  cutwidth 14.  V_S ≠ unlink.
* I_1(−20,40;−1,−1): S has 347 raw crossings (B–L 244 = 2×2 + 60 coils×4; snappy-simplified 321),
  lk = 0, both components unknotted, two projections agree, cutwidth 12.  V_S ≠ unlink.

## Pilot facts (n = 15), both inversions
* Symmetric diagrams: 94 crossings, writhe 34, det 7199 = 32·225−1, same Jones polynomial for both
  inversions, equal to spherogram's RationalTangle(7199, 7199−3630).numerator_closure().
* Cover lk(K,λ±) = lk(λ+,λ−) = 0 exactly (−34 turns of correction).
* I_1(2,2;−30,15): S has 895 raw crossings (snappy-simplified 221), lk = 0, both components unknotted,
  two projections agree (895 vs 999 crossings), cutwidth 14, 30 s.  V_S ≠ unlink.
* I_1(−30,60;−1,−1): S has 507 raw crossings (B–L 364 = 2×2 + 90 coils×4; snappy-simplified 482),
  lk = 0, both components unknotted, two projections agree, cutwidth 12, 22 s.  V_S ≠ unlink.

Full polynomials for all six pilot links: out/RESULTS.md (and the *_sakuma_proj0.json files).
