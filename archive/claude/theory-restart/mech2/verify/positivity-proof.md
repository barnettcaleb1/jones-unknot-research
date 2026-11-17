# REFEREE NOTES: positivity-proof

Target: /Users/calebbarnett/jones-lanes/theory-restart/mech2/states/REPORT.md, sections 0, 1, 2
(type-b cube C_b; Lemma 1.1, Lemma 1.2, Prop 1.3, Cor 1.4, Thm 2.1, Cor 2.2, UNIT POSITION, Thm 2.3, Thm 2.4).
Role: independent proof referee. Notes are appended as I go; the file ends with a VERDICT section when finished.
Scripts and kht++ working folders: /Users/calebbarnett/jones-lanes/theory-restart/mech2/verify/positivity-proof/

Status log
- [start] Read BRIEF2.md and report sections 0-2. Nothing verified yet.

## A. Conventions re-read in the kht++ source (my own reading, not the report's word)

File lit/kht/src/khtpp/sources/modules/Tangles.cpp.
- CobComplex (lines ~687-712): x is called positive iff the two strands point in OPPOSITE vertical directions, y positive iff they
  point in the SAME direction; x: 0-smoothing "=" (turnback e), 1-smoothing ")(" (id); y: 0 = id, 1 = e. So in both cases
  positive crossing <=> 0-smoothing is the oriented (Seifert) smoothing, negative <=> 1-smoothing is the Seifert smoothing.
  Report section 0, first bullet: CONFIRMED.
- Tangle::quotient (lines 967-1040): prefix "r1.r2." (or l1.l2.), off-axis crossing at i -> same letter at 2i, 2i-1, 2i+1, 2i;
  axis crossing -> same letter at 0,1,1,0; caps l/r at i -> 2i-1, 2i; cup at i -> 2i, 2i-1; then "u0"; then |w| copies of "x1.x1."
  if w = writhe() > 0, of "y1.y1." otherwise. Report section 0, second bullet: CONFIRMED (band = positions 2i-1, 2i; the extra
  band is created by the doubled cap; twists act on the last two bottom ends).
- Tangle::writhe (1195-1215) with the symmetric cut rule (line ~62: an axis crossing flips the orientation flag of strand 1):
  off-axis crossing: +1 iff (y and parallel) or (x and antiparallel), i.e. the usual sign; axis crossing: y0 -> -1, x0 -> +1 always.
  This is the true sign of the crossing in the symmetric diagram: at an axis crossing the strand and its image under the
  inversion are antiparallel in the vertical direction (the inversion reverses the orientation of K), so x0 is positive, y0 negative.
  Tangle::complete_symmetry (1042-1096) gives the mirror crossing the same letter and the two mirror strands opposite
  orientation flags, so each off-axis crossing of the half-diagram gives two crossings of the same sign upstairs.
  CONSEQUENCE (asked in the task): "all crossings of H have the same sign, wr = -c (resp. +c)" <=> the symmetric diagram
  D_sym (2 c_o + c_axis crossings) is a negative (resp. positive) diagram. CONFIRMED by reading; numerical check below (section D).

## B. Independent implementation and sweep over the 138 half-diagrams (referee code, no import of the report's scripts)

Code: verify/positivity-proof/ref.py (parser; orientation tracing of the half-diagram with a flip at every axis crossing; the
twist-free band diagram D built from my reading of Tangle::quotient; state evaluation; transfer matrices over planar matchings
for (a) chi_q of the type-b and type-c parts, (b) max/min of |s| +- k(s) over type-b states with the number of maximisers;
an independent half-plane model: union-find on strand sides ("ribbon edges"), gaps (regions) and arcs of Gamma_1 / Gamma_0).
Sweep: sweep.py -> sweep.log, sweep.json (1.4 s). Every item below holds for ALL 138 words, at both ends where applicable:
 1. s_1 and s_0 are of type b (Lemma 1.2).
 2. max over type-b states of |s|+k(s) equals 4c + k(s_1); min of |s|-k(s) equals -k(s_0) (Lemma 1.1 + 1.2).
 3. Single flips of s_1 (s_0): each either splits off a circle, or merges with a circle, or changes the type; the circle-splitting
    ("loop") chords come in pairs, exactly the twin places the report names (pass-by hook: the two letters at position 0;
    band block with id-smoothing: places 1 and 4; with e-smoothing: places 2 and 3); cut hooks have none (CHORDS paragraph).
 4. The set of blocks with loop chords computed in D equals the set of BAD blocks computed from the half-plane criteria (i), (ii).
 5. k(s_1) = (number of cut hooks) + (number of boundary curves of the regions) - 2; alpha and beta are the two curves the
    report says (HALF-PLANE PICTURE); regions = arcs + loops + 1, curves = arcs + 2 loops + 1.
 6. Number of maximisers |E| = 4^(number of bad blocks) (Proposition 1.3) -- by transfer-matrix count, not by enumeration.
 7. chi_b + (q+1/q) chi_c = q^(2c) exactly: the unknot diagram D(infinity) of the twist-free diagram sits at cube quantum
    degree 2c with sign +, i.e. n_+ = n_- = 2c (UNIT POSITION, twist-free part).
 8. With d_0 = 2c - 4wr (wr from my own orientation tracing): J := q^(-d_0) chi_b satisfies J(i) = 1 and J'(i) = 0, i.e.
    J = 1 mod (q+1/q)^2.  This test is sharp: replacing d_0 by d_0 + 4k changes J'(i) by -4k i.  (See section E for why this
    congruence is equivalent to "the tangle with |wr| twist pairs is Seifert framed".)  wr ranges over -12..11 in the sample.
 9. Counts of section 2 [DATA] re-derived: b-adequate at both ends 7 (the same seven names), 1-end only 23, 0-end only 13,
    neither 95; Theorem 2.3 applies to 43, never with the unit at an adequate corner; |wr| = c for 39; for these
    k = 2c_axis + 2l, |d_0 - (corner)| = 2(c_o - l), and c_o - l equals the genus I remember for each knot (3_1:1, 5_1:2, 5_2:1,
    7_1:3, 7_2:1, 7_3:2, 7_4:1, 7_5:2, 8_15:2, 8_19:3, 9_1:4, 9_2:1, 9_3:3, 9_4:2, 9_5:1, 9_6:3, 9_7:2, 9_9:3, 9_10:2, 9_13:2,
    9_16:3, 9_18:2, 9_23:2, 9_35:1).
 CORRECTION (minor, data): "Together: 72 of the 138 are non-flat" is not the union of Theorems 2.3 and 2.4. That union has
    43 + 39 - 11 = 71 elements (67 remain). The 72nd is 9_38 (s.l2.y1.y1.x0.x1.y0.y1.y1.u2, c = 7, wr = -5): there d_0 = M = 34,
    the unit sits exactly at the top corner of the cube, and the case is settled only by Corollary 1.4 (two bad blocks, so the
    top degree is acyclic and chi vanishes there; indeed chi_b has top degree 30). This third criterion (criterion "B" of
    py/criteria.py) should be stated as such in the text; with it the count 72 / 66 is right (I get A|B|C = 72 as well).

## C. Symmetric diagram, signs, genus (independent tracer: symm.py)

For all 138 words: D_sym built from my reading of Tangle::complete_symmetry is a knot diagram; its crossing signs, computed by
tracing the closed diagram, equal the signs I computed in the half-diagram (each off-axis letter twice, each axis letter
once): so wr(H) = -c <=> D_sym negative, wr(H) = +c <=> D_sym positive. For the 39 homogeneous words the number of Seifert
circles of D_sym is c_axis + 1 + 2l and (n_sym - s + 1)/2 = c_o - l. So "c_o - l = genus of the canonical Seifert surface of
D_sym" is CONFIRMED (proof: each of the c_axis + 1 arcs of the Seifert smoothing of H closes up with its mirror image to ONE
symmetric Seifert circle, each loop gives two; 2g = (2c_o + c_axis) - (c_axis + 1 + 2l) + 1).

## D. Random half-diagrams (randtest.py, randtest2.py; hidden cases)

Random shapes (caps anywhere, cups anywhere, crossings anywhere, widths up to 7, up to 10 crossings), letters chosen to make
the word all-negative, all-positive, or random. 400 + 3 x 1500 words kept (plus several thousand further genus-0 words that
were checked and not counted). Zero failures of: items 1-8 of section B; D_sym is a knot; and for homogeneous words:
k = 2c_axis + 2l, canonical genus of D_sym (from its own Seifert circles) = c_o - l, the support of chi_b lies on the far side
of d_0 -+ 2(c_o - l), "c_o = l => chi_b = q^(d_0) exactly and no bad block at the Seifert end", "c_o > l => chi_b != q^(d_0)".
Among the counted words: 1320 homogeneous with c_o - l > 0 (up to 7), 936 of them with loops (l > 0), 323 b-adequate at the
Seifert end; 408 + many uncounted homogeneous words with c_o = l (unknots, with nugatory kinks, zigzag cap-cup pairs etc.);
2772 non-homogeneous words (general claims only, including the unit position via J = 1 mod (q+1/q)^2).
So the hidden cases named in the task (extra cap-cup pairs, nugatory crossings, the unknot presented by a one-signed
half-diagram) produce no counterexample; see section G for why the unknot case is consistent.

