# Referee notes: positivity-compute (independent computation)

Target: mech2/states/REPORT.md, section 2: UNIT POSITION formula, Theorem 2.4 (one-sign half-diagram => unit degree
outside the support => T not flat), census claim (72 of 138 non-flat by diagram counts).
Role: independent computation. None of the lens's scripts (mech2/states/py) were read or run. All scripts of this
referee are in mech2/verify/positivity-compute/ . Notes are appended as the work proceeds (2026-11-16).

## 0. What is being tested, and how the unit is located without the report's formula

- Read: BRIEF2.md, mech/BRIEF.md, lit/kht/REPORT.md, REPORT.md sections 0-2, kht++ source Tangles.cpp
  (constructor, quotient(), complete_symmetry(), writhe(), CobComplex()).
- Conventions confirmed in the source (Tangles.cpp 644-735, 1195-1215): x is positive iff the two strands point in
  opposite vertical directions, y is positive iff they point the same way; 0-smoothing of x = turnback, of y = vertical;
  an axis crossing y0 is always negative and x0 always positive (writhe() uses the orientation flip of strand 1 at
  position 0). kht++'s writhe of a half-diagram counts each crossing of the half-diagram once (an off-axis crossing
  stands for a mirror pair of equal sign).
- INDEPENDENT LOCATION OF THE UNIT (my own argument, used for every test below). Write the bracket vector of T as
  alpha [Q_0] + beta [Q_inf]. chi_q N(T) = alpha up to a unit. T(inf) = unknot gives alpha + delta beta = unit, and the other
  closure T(0) is a link with determinant 0 or, for another even framing, alpha only changes by a unit (a twist pair
  multiplies alpha by a unit). Hence chi_q N(T) = +-q^d J with J = 1 mod (q + 1/q)^2. In Z[q,1/q]/((q^2+1)^2) the
  elements +-q^d are pairwise different (q^(2m) = (-1)^m (1 - m eps), eps = q^2+1, eps^2 = 0; odd powers are odd).
  So the pair (sign, d) is DETERMINED by the Euler characteristic alone:  d = the unique integer with
  chi_q N(T) = +-q^d mod (q^2+1)^2.  This needs neither the report's formula U = (2c - 2wr, 2c - 4wr) nor the
  brief's 24j. Both are then compared with it.

## 1. The 138 saved half-diagrams (script positivity-compute/part1.py, log part1.log, data part1_rows.json)

Own code (sidiag.py): symmetric diagram from the half-diagram word (written from Tangle::complete_symmetry), traced as an
unoriented planar diagram, sign of every crossing from the direction vectors (over x under > 0 = positive), Seifert
circles, Alexander polynomial (Fox calculus, exact integer determinants + interpolation); band diagram of the quotient
(written from Tangle::quotient); state sum over planar matchings giving, for the twist-free band diagram D, the number
of type-b states with given (|s|, k). Own reader for kht++ chain files (khtio.py).

Sanity of inputs (all 138, no exception):
- my symmetric word and total writhe agree with tools/alex.py; mirror pairs have equal signs; y0 is negative, x0 positive;
- the Alexander polynomial computed from each file equals the Rolfsen-table polynomial of the knot named in the file
  (table typed from memory; it reproduced all 138, including the mislabelled comment lines of 8_15-2, 8_18-2, 8_21-*);
- the unsimplified quotient word stored by kht++ in <name>-q.svg equals my band word with |wr| twist pairs
  (y1.y1 for wr < 0, x1.x1 for wr > 0), wr = my signed count. So "kht++ Tangle::writhe" = geometric signed count of
  the crossings of the half-diagram, in all 138 files.
- k138.jsonl has NO kht++ output for 6 names (9_10-2, 9_17-2, 9_31-2, 9_39, 9_40-1, 9_41: 'timeout'); none is one-sign.
  For the other 132: the b-generators from tools/gtilde.py jset equal the b-generators read from the chain file
  cxBNr-c2-qs by my parser (all 132 chain files exist; identical multisets of (h,q)).

UNIT POSITION, tested without using the formula:
- kht++ coordinates (132 cases): chi_q N = +q^(24j) mod (q^2+1)^2 in every case (j from the rational component as in
  the brief). So the unit degree is 24j, sign +.
- cube coordinates of the twist-free band diagram (all 138, my state sum, no kht++): chi_q(C_b(D)) = +q^(2c-4wr)
  mod (q^2+1)^2 in every case. This is the report's d_0 = 2c - 4wr, with the sign (+) that h_0 = 2c - 2wr even requires.
- J computed from the kht++ generators and J computed from my state sum agree in all 132 cases.
  [So the report's UNIT POSITION formula holds on the table, q-coordinate and parity of h. The h-coordinate itself is
  tested below only through the adequate cases.]

THEOREM 2.4 on the table: 39 half-diagrams have all crossings of one sign (26 negative, 13 positive) - the report's 39.
For each of the 39 (table in part1.log):
- genus: diagram genus (Seifert circles of the symmetric diagram) = half the span of the Alexander polynomial = table
  genus. So g(K) is certified here without Cromwell's theorem.
- chain level (my count): max of |s| + k over type-b states (negative case; min of |s| - k in the positive case) is
  exactly d_0 - 2g (resp. d_0 + 2g); k(s_1) = 2 c_axis + 2 l and c_off - l = g with l from the Seifert circle count. OK 39/39.
- homology (kht++): no b-generator in the unit degree, coefficient of J there 0, all generators on the predicted side. OK 39/39.
- DISTANCE: the distance from the unit degree to the nearest generator of N is 2g(K) in ONLY 11 of the 39
  (5_2-2, 7_2-2, 7_4-1, 8_15-1, 8_15-2, 9_16-2, 9_18-2, 9_2-2, 9_35-1, 9_5-1, 9_5-2). These are exactly the 11 whose
  Seifert end has a unique extreme type-b state (b-adequate end), and there N is one-dimensional at exactly
  (h,q) = (8j, 24j -+ 2g), i.e. at U -+ (0, 2g): the last sentence of Theorem 2.4 is confirmed, including the
  homological degree. In the other 28 the nearest generator is FURTHER away: distance 2g + 4b with 4^b = number of
  extreme states (b = 1..4), except 8_19 (2g + 10 with 64 extreme states). E.g. 3_1: 6, 5_1: 12, 7_1: 18, 9_1: 24.
  So "distance = 2g" is a statement about the complex C_b (its top degree), not about N; for N it is ">= 2g, with
  equality iff the end is b-adequate" on this table. The theorem as written says exactly this; the phrase in my task
  ("the distance ... is 2g(K)") is true for the complex and false for N in 28 cases.

CENSUS (all 138, my extreme-state counts; identical to the numbers in the lens's survey.jsonl where it has them):
- unique extreme state at both ends: 7 (8_5-2, 8_15-2, 8_18-1, 8_18-2, 9_34, 9_35-1, 9_37-1); top only 23; bottom only 13;
  neither 95. = report. The number of extreme states is a power of 4 in all 276 ends. In the 132 cases with kht++ output:
  N is non-zero at the cube corner iff the extreme state is unique, and then it is one-dimensional. = report.
- at least one adequate end: 43, and in all 43 the unit degree differs from the adequate corner. = report.
- one-sign: 39. = report.
- OVERLAP of the two families: 11 (the list above). So the union is 43 + 39 - 11 = 71, NOT 72; 67 remain, not 66.
  CORRECTION 1: "72 of the 138" should read "71 of the 138" ("66 remain" -> "67 remain"). The same 11 come out of the
  lens's own survey.jsonl (top_nE == 1 or bot_nE == 1 among the one-sign names), so this is an arithmetic slip.
