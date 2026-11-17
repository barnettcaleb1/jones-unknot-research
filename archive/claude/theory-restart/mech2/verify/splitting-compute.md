# REFEREE NOTES: splitting inequality, independent computation

Referee role: independent computation (no reuse of the lenses' scripts in colored/py or twobridge/scripts).
Target: colored/REPORT.md section 2 (Theorem A, consequences (i), (ii)); twobridge/REPORT.md 1.4 and 6.4
(dim N(T) >= dim Kh~(K_u) dim Kh~(K_l); l-graded refinement; data claim dim N = max(rank HFK^(K), rank Kh~(K_u) rank Kh~(K_l))).
Working folder (scripts, kht++ runs): verify/splitting-compute/ .  Notes are appended as work proceeds (started 2026-11-16).

Marks used below: [RUN] = computed by me in this session; [READ] = read in the target reports / source; [RECALLED] = from memory, not recomputed.

## 0. What is being tested, and how (plan)
- N(T): b-generators of BN~(T) with (h,q), read by my own parser from the stored chain files
  lit/kht/out/k138/examples/si/<name>/cxBNr-c2-qs, cross-checked against tools/gtilde.py jset on k138.jsonl (h = q/2 - delta).
- Components of T(0): from the simplified 1-3 tangle word in the .kht header, append u0, trace strands with my own
  Morse-word tracer, extract the sub-diagram of each component, run kht++ on each (1-1 tangle), and independently
  compute the Jones polynomial of each component with my own Kauffman-bracket code as a check on kht++'s output.
- Tests: (i) dim N >= dim Kh~(K_u) dim Kh~(K_l); (ii) exists c with P_N(x) - x^c W_u(x) W_l(x) = (1+x) R(x), R >= 0
  (l = h - q); (iii) dim N = max(rank HFK^(K), product).

## 1. N(T) from the data  [RUN]
- k138.jsonl has 138 records; 6 are {"error": "timeout"} or have no chain file (9_10-2, 9_17-2, 9_31-2, 9_39, 9_40-1, 9_41).
  So "the table of 138" is really 132 computed inversions (this agrees with "132" in twobridge 1.4/6.4; the task's "138" is the
  number of input files, not of data points).
- I wrote my own parser of the chain files (splitting-compute/chain.py) and read the b-generators (symbol ⬮) with (h,q) from
  cxBNr-c2-qs for all 132.  Result: for all 132 the multiset of (h,q) equals tools/gtilde.py jset (q, delta) with h = q/2 - delta.
  (script check_N.py; output N_from_chains.json).  dim N ranges over 3..75, all odd.
  So N(T) as a bigraded vector space is the same whether read from the Kh~ labels (gtilde) or from BN~ directly.

## 2. The tangle words and the components of T(0)  [RUN]
- All 138 headers carry a simplified word; each is a 1-3 tangle (1 top end, 3 bottom ends) in which the top strand ends at the
  bottom position b3 and the other strand joins b1 to b2 (connectivity b), so T.u0 is a 2-component link: one open component
  (through the special end) and one closed component.  (words.py)
- Independent check that the header word really is the tangle behind the stored BN~ (check_chi.py), all 132:
  (a) my own Kauffman bracket of the word (sweep over non-crossing matchings): T.u1 = T(infinity) has unit bracket (unknot-consistent);
  (b) the graded Euler characteristic of the stored b-generators equals +-q^s times the Q_0-coefficient of my bracket (q = -A^-2).
  0 failures.  This also fixes the chirality convention of my reader against kht++ (x/y swapped would fail (b)).
  (c) Rerunning kht++ directly on the header word as a plain 1-3 tangle (no -q), 8 cases (3_1, 4_1-1, 4_1-2, 8_19, 9_42, 9_46-1,
  9_46-2, 7_4-2), reproduces the stored cxBNr file including absolute gradings (examples/rerun/).  So the stored gradings are those
  of the header word with kht++'s orientation rule: top end up, cap letters l/r as written.
- Components (split.py): I trace the monotone strands of T.u0 (crossing = swap, cap = two new strands, cup = join), take the two
  union-find classes, and write the sub-diagram of each class alone as a 1-1 tangle (closed component: cut open at its top cap).
  Self/mixed crossing counts, writhes and the mixed linking number are recorded in split_info.json.
- Kh~ of every component over F_2 with kht++ (276 runs, each < 2 s; examples/comp/).  Check: the Euler characteristic of each
  kht++ output equals the Jones polynomial I get from my own bracket code on the same sub-word (all 276).

## 3. Results on the table  [RUN]  (analyse.py, lkcheck.py; output analysis.json)
All 132 inversions with data were tested (not only 25).  Notation: (o, c) = (open component, closed component) of T(0).
- INEQUALITY dim N(T) >= rk Kh~(o) rk Kh~(c): holds in 132/132.  Equality in 130.  Strict in exactly two:
      8_19:  dim N = 5 > 1*3   (components: unknot, trefoil)
      9_42:  dim N = 9 > 7*1   (components: Jones polynomial of 5_2, unknot)
- l-GRADED REFINEMENT: for each of the 132 there is EXACTLY ONE shift c with P_N(x) - x^c W_o(x) W_c(x) = (1+x) R(x), R >= 0
  (many other c give divisibility by 1+x but an R with a negative coefficient).  R = 0 in the 130 equality cases;
  R = x^7 for 8_19 and R = x^-1 for 9_42 (one cancelling pair each, and in both cases N contains a pair of generators at the
  two l-levels whose (h,q)-difference is (-1,-2) = the claimed bidegree of d_1).
- ABSOLUTE SHIFT (stronger than what the report states as (ii)): with the orientation kht++ uses for the gradings (top end up, cap
  letters of the header word) the unique admissible shift is c = -2 lk(L_1, L_2) in 132/132 (2 lk = sum of the signs of the mixed
  crossings of T.u0; values -24..32).  So  dim N^l = dim (Kh~ (x) Kh~)^(l + 2 lk) + (cancelling pairs), which is the shift
  t = 2 lk of Batson-Seed's rank inequality.  The form c = -2 lk is also the only one compatible with reversing one component
  (N shifts by l -> l + 4 lk, lk changes sign).  The report's Theorem A says "l shifted by 2 lk" without a sign; the data fix it.

## 4. Doubled tangles  [RUN]  (doubles.py, analyse_dbl.py, analyse_dbl2.py)
- For k3_2 (3_1), k5_2 (4_1), k5_4 (5_1), k7_2 (5_2), k7_6 (7_1) I rebuilt the doubled 1-3 tangle word myself from the knot word
  (cap on the left, every strand doubled, writhe full twists on (b2,b3)); kht++ on my word reproduces the stored cxBNr-c2-d
  byte for byte (after the header line).  Tracing T_K.u0: two components, each with the Jones polynomial and the bigraded Kh~
  (kht++) of K; linking number 0.
- Result for these five: dim N(T_K) = (rk Kh~ K)^2 (9, 25, 25, 49, 49); the unique admissible shift is c = 0 = -2 lk; R = 0;
  the l-distribution of N equals that of Kh~(K) (x) Kh~(K) exactly.
- All 21 doubles with stored data (k3_2 ... k17_8; the other 12 records are timeouts): N read from the stored chain file by my
  parser agrees with gtilde jset; Kh~(K) from my own kht++ run of the knot word; dim N = (rk Kh~ K)^2, c = 0, R = 0 in 21/21.
  No violation.  (All 21 are two-bridge, so this is the collapse case only.)

## 5. The "= max(...)" claim and the identification of the components  [RUN, except the HFK ranks]
- det K (from kht++'s Kh~ of the knot itself, run by me on the half-diagram words without -q) = det(o) det(c) for all 138
  inversions (also the 6 without N data).  This is twobridge 1.4, first line, and is at the same time a strong check that my
  separation of the two components is right.
- My own Alexander polynomials (alexander.py: Wirtinger arcs, exact determinant) of the two components agree, as an unordered
  pair, with the constituent knots (K_u, K_l) listed in twobridge/table_const.txt in 132/132; in fact open component = K_u and
  closed component = K_l in all 131 cases where the two differ.  The lens computed K_u, K_l from the half-diagram (theta-curve),
  I computed them from the tangle word, so "components of T(0) = constituents of the theta-curve other than the axis" is
  confirmed at the level of Alexander polynomials (chirality is not tested by this).
- Named cases (from my Jones/Alexander polynomials and kht++ ranks over F_2):
      8_19:    (U, 3_1)         ranks 1, 3    dim N = 5
      9_42:    (5_2, U)         ranks 7, 1    dim N = 9
      9_46-1:  (3_1, mirror 3_1) ranks 3, 3   dim N = 9      (Jones polynomials t^-1+t^-3-t^-4 and t+t^3-t^4: a mirror pair, as the report says)
      9_46-2:  (T(3,4), 3_1)    ranks 5, 3    dim N = 15     (Jones q^6+q^10-q^16; Kh~ over F_2 of rank 5 with an H^2-torsion piece)
      7_4-2:   (5_1, 3_1)       ranks 5, 3    dim N = 15
      7_7-2:   (3_1, 5_2)       ranks 3, 7    dim N = 21
      9_23-2:  (6_1, 4_1)       ranks 9, 5    dim N = 45
  All agree with twobridge 1.4 / 6.4.  Both components are knotted in 31 of the 138 inversions (25 of the 132 with data).
- max formula: with rank HFK^(K) = det K except 8_19 (5) and 9_42 (9)  [RECALLED, standard; NOT recomputed: no HFK program here],
  dim N = max(rank HFK^(K), rk Kh~(K_u) rk Kh~(K_l)) in 132/132.  Split: 129 cases where dim N = rank HFK^ = product (= det K);
  2 cases dim N = rank HFK^ > product (8_19, 9_42); 1 case dim N = product > rank HFK^ (9_46-2).
  REMARKS for the reader of the claim:
  (a) the content of "= max" rests on three data points; in the other 129 everything is thin and all three numbers are det K.
  (b) rk Kh~(K; F_2) = rank HFK^(K) for every knot of the table (5 for 8_19, 9 for 9_42, det otherwise), so the table cannot
      distinguish "max(rank HFK^(K), ...)" from "max(rk Kh~(K), ...)".
  (c) the task says "table of 138"; there are 132 data points (6 timeouts).

## 6. The double of 8_19 = T(3,4) (the non-collapse example of colored section 2, Remark (c))  [RUN]
Recomputed from scratch with my own diagram (T(3,4) as the closure of (s1 s2)^4, word r1.r2.(y0.y1)^4.u2.u1; doubled with my own
doubling code, 48 crossings; kht++ 219 s; examples/dbl819/).
- Kh~(T(3,4); F_2) = {(0,6), (2,10), (3,12), (4,12), (5,16)}, rank 5; both components of T_K(0) have exactly this bigraded Kh~; lk = 0.
- dim N(T_K) = 41 = one arc with 9 b-generators + 8 compact components with 4 each.     (report: "41 = arc(9) + 8 squares": CONFIRMED)
- l-distribution from the lowest l (l = -22..-12):  N: 2 3 4 6 5 8 5 3 4 0 1;  Kh~(x)Kh~: 1 0 2 4 1 6 4 2 4 0 1.   (CONFIRMED, identical)
- unique admissible shift c = 0 = -2 lk;  R = x^-22 (1 + 2x + 2x^3 + 2x^4 + x^6) >= 0, eight cancelling pairs.   (CONFIRMED)
- CONSEQUENCE for the "= max" claim: T_K is the quotient tangle of the swap inversion on K # K (BRIEF2 2(a)), rank HFK^(K # K) = 25
  (Kunneth, [RECALLED]) and rk Kh~(K_u) rk Kh~(K_l) = 25, but dim N = 41.  So "dim N = max(rank HFK^(K), product)" is FALSE as a general
  statement; it is a property of the 132 table entries (and of the 21 two-bridge doubles) only.  The reports do present it as data on
  the table, and colored 2(c) itself notes the strict inequality; twobridge 6.4's last sentence should carry the same warning.
