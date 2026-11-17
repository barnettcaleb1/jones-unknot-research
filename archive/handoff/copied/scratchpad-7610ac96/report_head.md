# Lane IDENT: identifying the moments M_3, M_4 (a_2 = 0 core of Lemma Q)
(16 Nov 2026, Claude, lane folder mont/ft/ident/. Tags: PROVED / CHECKED(n) / CONJECTURE / GAP / KNOWN. No novelty claims.)
Notation: M_k = sum_e J_e (-1)^e e^k; a_2, a_4 = Conway coefficients; v_3 = -(V'''(1)+3V''(1))/36 (BRIEF F3);
j_4 := [h^4] V_K(e^h) = (V''''+6V'''+7V''+V')(1)/24 (in the a_2 = 0 core j_4 = sum_e V_e binom(e,4) - 9 v_3, an integer).
K_in = k u A_in, K_out = k u A_out (quotient constituent knots; A_in = axis segment between the fixed points, carrying all
windings in the half-word normal form); U_in = K_+ u O_in, U_out = K_+ u O_out (upstairs constituents).

## 0. Summary
1. Constituent knots built from half-words and validated (sec. 1): det(K) = det(K_in) det(K_out) on 150/150 words (forced by the
   Z/2 x Z/2 cover; fails for the upstairs pair), local knots behave correctly, trefoil inversion -> {3_1*, unknot},
   figure-eight inversions -> {4_1, unknot} and {5_1, unknot}.
2. M_3 = 432 v_3(K) + 180 D,  i.e. iota = v_3(K) + D  (F3: M_3/36 = 7 v_3 + 5 iota = 12 v_3 + 5 D).
   D is an order-<=3 equivariant invariant, vanishing on local configurations (K_1 # rK_1), integer-valued (CHECKED 450
   words; PROVED modulo FT + the classification CONJECTURE + one unrealised diagram type), and NOT a linear combination of
   v_3(K), v_3(K_in), v_3(K_out), v_3(U_in), v_3(U_out), the Sato-Levine invariants of both butterfly links, of K u O',
   N_3, or products of the order-1 invariant N_1 := J'(1) (or of any order-1 invariant) with order-2 invariants
   (PROVED by exact certificates, sec. 2).  So the 'genuinely equivariant part' of M_3 is a NEW order-3 invariant relative to
   all classical candidates (i)-(iv) that I could build; its weight system is tabulated (227 types) and e.g. equals
   8 (-1)^{#odd chords} [T inside both chords] on every '2 chords + 1 tangency' type (CHECKED 67/67 types).
3. M_4 = -1440 a_2^2 - 1440 a_4 + 864 j_4 - 120 a_2 + 1440 F4 (a_2,a_4,j_4 of K), F4 integer (CHECKED 450 words), F4 = 0 on
   local configurations, F4 NOT a combination of 56 candidate order-<=4 invariants (PROVED, exact certificate, sec. 4).
   The first four terms are exactly the 'local' (colour-2 Jones) formula; PROVED modulo a cited osp(1|2) fact.
4. Corollary (sec. 5): J = 1  =>  a_2 = 0,  12 v_3 + 5 D = 0,  3 j_4 + 5 (F4 - a_4) = 0.  Classical consequence
   (conditional on D, F4 in Z):  J = 1  =>  a_2(K) = 0,  v_3(K) = 0 mod 5,  j_4(K) = 0 mod 5.
   On P(2k,4k-1,4k+1): v_3 = -2k(7k^2-1)/3, D = -2k(2k^2+1)/3, M_3 = -2256k^3+168k (CHECKED k <= 10); the congruence
   test excludes J = 1 exactly when 5 does not divide k (k = 1..4 all excluded).
5. Side results: (a) the singular configurations are classified (CONJECTURE, consistent in all data) by quotient chord diagrams
   with LABELS (parity of windings inside a chord), tangency DIRECTIONS delta and the A_in-ORDER of tangencies; without delta
   the a_2(K) symbol is inconsistent.  (b) The symbols of M_2, M_3, M_4 never depend on delta (CHECKED levels 2,3,4), unlike
   those of v_3(K_in), v_3(U_in), N_2, N_3.  (c) The expansion of J at t = +1 is ALSO equivariant finite type (N_k order <= k,
   CHECKED 60); N_1 = J'(1) in 8Z is an order-1 invariant with symbol T^ -> 8, C- -> -8 (so order-1 invariants exist; the
   naive count lambda_- of odd crossings is NOT invariant).  (d) D's weight system is not a sum over upstairs lifts of ANY
   weight on 2-pointed 3-chord diagrams (PROVED, 4-type certificate): D 'sees' the inner axis, not just K with its fixed points.

## 1. Constituent knots: construction and validation
- Construction (PROVED geometric facts): the quotient map of the rotation (x,y,z) -> (-x,y,-z) is (x+iz) -> (x+iz)^2, holomorphic,
  so on X > 0 the quotient diagram of k is the half-diagram with the same crossing types; x0 (resp. y0) is a full twist of k
  around the axis line, two crossings (x,0),(x,0) (resp. (y,0),(y,0)) with the axis at position 0.  All windings lie on A_in.
  K_in: cap(0,1), letters shifted by +1, windings as above, cup(0,1).  K_out: the same with x0/y0 deleted.  (diag.py)
- Validation (CHECKED): generic bracket = kauffman.bracket on 60/60; Jones-a_2 = Conway-a_2 for all five knots 60/60;
  det(K) = det(K_in) det(K_out) 150/150 (42 with both factors > 1) [the Z/2 x Z/2-cover/transfer argument forces this
  identity]; local trefoil s.r1.y2.y2.y2.u1: K = 3_1#3_1, K_in = K_out = U_in = U_out = 3_1; trefoil inversion
  (s.r2.r1.y0.y2.u1.u1 or s.l1.y0.x1.u2): K_in = mirror trefoil, K_out = unknot; figure-eight: three J's found (one is the
  mirror of another), quotient constituents {4_1, unknot} (e.g. s.l1.y2.y0.y2.y0.r3.y1.y2.y1.x4.x3.u1.x2.x1.x1.x1.y0.u1) and
  {5_1, unknot} (s.r1.y0.y0.y2.u1) -- the two det-5 two-bridge knots, as the det identity requires.

## 2. M_3
- Local part (PROVED mod citation, CHECKED 250 local words): if k is a local knot K_1 (no windings) then J is the normalised
  colour-2 Jones polynomial of K_1 and M_3 = 864 v_3(K_1) = 432 v_3(K).
- Definition D := (M_3 - 432 v_3(K))/180.  Level-3 symbol of D in 8Z on all 227 realised 3-element types (CHECKED);
  nonzero on 30 types; full table dtable3.json + witness_D.json.  Rule on '2 chords + T': D-symbol = 8(-1)^{#odd}[T inside
  both chords] (67/67 types, crossing or nested, either delta).  A short odd chord acts like -2 T in all observed cases.
- Obstructions (PROVED by exact computation; constructions validated as in sec. 1):
  (a) symbol level, 12-type certificate (certificate.py) against v_3 of K, K_in, K_out, U_in, U_out, a_3(butterfly in/out),
      N_3, N_1*a_2(X), N_1*N_2, N_1^3; robust under adding products with hypothetical order-1 invariants supported on T^ or
      C- (certificate2.py; uses that order-1 symbols vanish on Tv and C+, argued in L4);
  (b) value level, 16-word certificate (cert4.py) against 17 candidates including the Sato-Levine invariant of K u O'.
  Literature candidate (iii): if Sakuma's eta-polynomial is the Kojima-Yamasaki eta-function of the butterfly link (my
  recollection; LIT lane to confirm), its first coefficient is the Sato-Levine invariant (+-a_3), already excluded; its
  higher coefficients have order >= 5.
- Status: 'M_3 = 432 v_3(K) + 180 D' is a definition; the content is: D integral (sec. 3), D local-trivial, D new.

## 3. Spanning argument (order <= 3) and its gap
- Principle: if g is an invariant of order <= m (FT) with values in an abelian group and top-level sums depend only on the
  diagram type (classification CONJECTURE), then g = 0 follows from: level-j sums vanish on one configuration of each
  j-element type, j = m, m-1, ..., 1, and g(trivial) = 0 (induction on the order; every half-word is connected to the
  trivial (K,h) by flips: make the symmetric diagram descending from the top fixed point -- h preserves 'descending' --
  and the unknot has a unique strong inversion, KNOWN).
- Types: 4 / 24 / 228 combinatorial types with 1 / 2 / 3 elements (enumtypes.py); realised: 4 / 24 / 227 (missing only
  T0^T1^T2^).  Used configurations: random words (fastsym.py) + targeted search (hunt.py), stored in fast_m3_*.json,
  hunt_*.json.
- Application: g = M_3 - 432 v_3 mod 180 vanishes at all levels on all realised types => D in Z, modulo FT, the
  classification, and the one unrealised type (GAP).  The same method would prove an identity 'M_3 = known combination' --
  but no such identity exists (sec. 2), so the spanning family here serves integrality only.

## 4. M_4
- Local part (PROVED mod citation; CHECKED 250 local words, 31 distinct (a_2,v_3,a_4,j_4) tuples, exact fit):
  M_4 = 576 a_2(K_1)^2 - 2880 a_4(K_1) + 1728 j_4(K_1) - 240 a_2(K_1) = M_4^loc(K) := -1440 a_2^2 - 1440 a_4 + 864 j_4 - 120 a_2.
- F4 := (M_4 - M_4^loc(K))/1440 is an integer (CHECKED 450 words; spanning check: levels 1-3 complete on realised types,
  level 4 only sampled: 150 configurations/120 types, so integrality stays CHECKED).  M_4 symbols consistent per type at
  level 4 (500 configurations, 334 types, 88 repeated) and delta-independent.
- Obstruction (PROVED, 46-word exact certificate cert_F4.json): F4 is not a linear combination of the 56 order-<=4 even
  candidates a_2(X), a_2(X)a_2(Y), a_4(X), j_4(X) (X,Y in {K,K_in,K_out,U_in,U_out}), N_2, N_1^2, N_4, N_1 N_3, N_2^2,
  N_1^2 N_2, N_1^4, N_1^2 a_2(X), N_2 a_2(X), N_1 v_3(X), N_1 D, N_1 a_3(butterflies), N_1 a_3(K u O').

## 5. Corollary and values on a_2 = 0 examples
- J = 1 => a_2(K) = 0 (KNOWN, BRIEF) and M_3 = M_4 = 0, i.e.  12 v_3(K) + 5 D = 0  and  3 j_4(K) = 5 (a_4(K) - F4).
  With D, F4 in Z:  v_3(K) = 0 mod 5 and j_4(K) = 0 mod 5 (then D = -12 v_3/5 and F4 = a_4 - 3 j_4/5).  [CONJECTURE-level
  only through the integrality of D (sec. 3 gap) and F4 (CHECKED).]
- P(2k,4k-1,4k+1) = mont(-k,[4k-1,4k+1]) (J from the necklace formula, equal to lp.J for k = 1,2; K-invariants from a
  standard pretzel diagram of the same chirality as the half-word):
      k   v_3     a_4     j_4      M_3       M_4         D      F4     v_3,j_4 mod 5
      1   -4      -6      126     -2088      82944       -2     -24      1, 1
      2   -36     -88     2232    -17712     1410048     -12    -448     4, 2
      3   -124    -438    11502   -60408     7216128     -38    -2328    1, 2
      4   -296    -1376   36576   -143712    22892544    -88    -7424    4, 1
  (a_2 = 0 = M_2 in all rows.)  Closed forms (CHECKED k = 1..10): v_3 = -2k(7k^2-1)/3, D = -2k(2k^2+1)/3,
  M_3 = -2256 k^3 + 168 k; 5 | v_3 iff 5 | k (k^2 = 3 mod 5 is impossible), and k = 5, 10 indeed give v_3 = j_4 = 0 mod 5.
- Other a_2 = 0 examples met: 48 of the 150 words of ident3_rows have a_2 = 0; all nontrivial ones have M_3 != 0
  (e.g. s.r1.y0.y0.x2.x1.x0.x0.x2.u1: v_3 = -1, D = 0, F4 = 7; s.r1.y0.y2.x1.y2.y2.x0.u1: v_3 = 1, D = -4, F4 = -16).

## 6. Scripts (all in this folder; run with tools/venv/bin/python)
diag.py (diagrams, K_in/K_out/U_in/U_out, generic bracket, Alexander/Conway), chord.py (traversal, labels, delta, types, signs),
symtab.py / fastsym.py (symbol tables), butterfly.py, axislink.py, ltheta.py (derived links), nmom.py, n1sym.py (t=+1 moments),
local_fit.py (local formulas), congr.py, integrality.py, integrality2.py (integrality checks), enumtypes.py, hunt.py (type
coverage), certificate.py, certificate2.py, cert4.py, modrank.py, upfit.py (obstructions), family3.py (family values),
fig8.py, test_*.py (validation).  Data: inv_rows*.json, dtable3.json, witness_D.json, family_values.json, cert_F4.json.
