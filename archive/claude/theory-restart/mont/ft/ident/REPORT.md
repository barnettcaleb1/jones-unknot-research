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
   N_3, or products of the order-1 invariant N_1 := J'(1) with order-2 invariants (PROVED by exact certificates, sec. 2;
   also robust against products with ANY order-1 invariant, granting the argued fact that order-1 symbols vanish on
   Tv and C+).  So the 'genuinely equivariant part' of M_3 is a NEW order-3 invariant relative to
   all classical candidates (i)-(iv) that I could build; its weight system is tabulated (227 types) and e.g. equals
   8 (-1)^{#odd chords} [T inside both chords] on every '2 chords + 1 tangency' type (CHECKED 67/67 types).
3. M_4 = -1440 a_2^2 - 1440 a_4 + 864 j_4 - 120 a_2 + 1440 F4 (a_2,a_4,j_4 of K), F4 integer (CHECKED 450 words), F4 = 0 on
   local configurations, F4 NOT a combination of 56 candidate order-<=4 invariants (PROVED, exact certificate, sec. 4).
   The first four terms are exactly the 'local' (colour-2 Jones) formula; PROVED modulo FT restricted to local
   configurations (equivalently the osp(1|2)/so(3) correspondence cited in BRIEF F2) plus an exact fit on 31 spanning knots.
4. Corollary (sec. 5): J = 1  =>  a_2 = 0,  12 v_3 + 5 D = 0,  3 j_4 + 5 (F4 - a_4) = 0.  Classical consequence
   (conditional on D, F4 in Z):  J = 1  =>  a_2(K) = 0,  v_3(K) = 0 mod 5,  j_4(K) = 0 mod 5.
   On P(2k,4k-1,4k+1): v_3 = -2k(7k^2-1)/3, D = -2k(2k^2+1)/3, M_3 = -2256k^3+168k (CHECKED k <= 10); the congruence
   test excludes J = 1 exactly when 5 does not divide k (k = 1..4 all excluded).
   Limits (CHECKED): among 15 random a_2 = 0 examples with V_K != 1 the congruences fire 13 times; one example has
   a_2 = v_3 = a_4 = j_4 = 0 but D = 6, F4 = -18 (J != 1 visible only through D, F4); another has M_2 = M_3 = M_4 = 0 and
   M_5 = 69120 (s.r1.x2.y1.y0.x1.x2.x1.x2.y0.y1.x2.y1.u1), so the order <= 4 moment conditions are NOT sufficient.
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
- Other a_2 = 0 examples met (450 random words): 128 have a_2(K) = 0, of which 15 have V_K != 1.  The congruence test
  (5 does not divide v_3 or j_4) fires on 13/15, e.g. s.r1.y0.y0.x2.x1.x0.x0.x2.u1 (v_3 = -1, j_4 = -9, D = 0, F4 = 7),
  s.r1.y0.y2.x1.y2.y2.x0.u1 (v_3 = 1, j_4 = 21, D = -4, F4 = -16).  The two others have a_2 = v_3 = a_4 = j_4 = 0
  (all Vassiliev invariants of K of order <= 4 vanish; V_K, Delta_K nontrivial):
    s.l1.x2.x2.x0.x1.x1.y0.x1.x1.l2.y0.y2.y1.x4.x1.x4.x3.u1.y2.u1 : M_3 = 1080 (D = 6), M_4 = -25920 (F4 = -18) --
        here J != 1 is seen ONLY through the new equivariant invariants D, F4;
    s.r1.x2.y1.y0.x1.x2.x1.x2.y0.y1.x2.y1.u1 : M_2 = M_3 = M_4 = 0 (D = F4 = 0) but M_5 = 69120 -- so 'J = 1 => a_2 = 0,
        M_3 = 0, M_4 = 0' cannot exclude this (K,h); the order-5 moment is needed.  (Both CHECKED by direct computation.)

## 6. Scripts (all in this folder; run with tools/venv/bin/python)
diag.py (diagrams, K_in/K_out/U_in/U_out, generic bracket, Alexander/Conway), chord.py (traversal, labels, delta, types, signs),
symtab.py / fastsym.py (symbol tables), butterfly.py, axislink.py, ltheta.py (derived links), nmom.py, n1sym.py (t=+1 moments),
local_fit.py (local formulas), congr.py, integrality.py, integrality2.py (integrality checks), enumtypes.py, hunt.py (type
coverage), certificate.py, certificate2.py, cert4.py, modrank.py, upfit.py (obstructions), family3.py (family values),
fig8.py, test_*.py (validation).  Data: inv_rows*.json, dtable3.json, witness_D.json, family_values.json, cert_F4.json.

---------------------------------------------------------------------------------------------------------
## LOG (chronological; the numbered sections above are filled in at the end)

L1 (constituent knots, construction).  Quotient picture of a half-word: the rotation (x,y,z) -> (-x,y,-z) has quotient map
  (x+iz) -> (x+iz)^2 (holomorphic, orientation preserving), so on X > 0 the quotient diagram of the arc k IS the half-diagram
  (same crossing types), and each x0/y0 becomes a full twist of k around the axis line, crossing it twice:
  x0 -> (x,0),(x,0), y0 -> (y,0),(y,0) with the axis at position 0 (same convention as flat_search.quotient_word).
  All windings sit on the axis segment between the two fixed points (A_in); A_out (through infinity) crosses nothing.
  K_in  = k u A_in : Morse word cap(0,1) + letters shifted by +1 + windings as above + cup(0,1).
  K_out = k u A_out: same with the x0/y0 letters deleted.
  Also built (upstairs constituents of the theta-curves K u O_in, K u O_out): U_in = K_+ u O_in, U_out = K_+ u O_out
  (K_+ = half of K between the fixed points), via the symmetric diagram with the axis drawn as a strand (an on-axis crossing
  is the triple point P over axis over Q, resolved into 3 crossings) and deletion of K_-.  Code: diag.py.
  VALIDATION (CHECKED): (a) generic frontier bracket reproduces kauffman.bracket's V_K on 60/60 words; a_2 from Jones = a_2 from
  Conway for all five knots K, K_in, K_out, U_in, U_out on 60/60 words.  (b) det(K) = det(K_in) det(K_out) on 150/150 words
  (42 with both factors > 1); this identity is forced by the Z/2 x Z/2 branched cover of the quotient theta-curve (transfer;
  KNOWN-type argument: H_1(Sigma_2(K);Z[1/2]) = H_1(Sigma_2(K_in);Z[1/2]) + H_1(Sigma_2(K_out);Z[1/2])); the analogous
  identity for (U_in,U_out) fails (55/150), so it discriminates.  (c) local knots: s.r1.y2.y2.y2.u1 (a trefoil tied in k away
  from the axis) gives K = 3_1#3_1, K_in = K_out = U_in = U_out = the same trefoil, as it must.
  (d) the inversion of the trefoil s.r2.r1.y0.y2.u1.u1 (K with V = t+t^3-t^4): K_in = mirror trefoil, K_out = U_in = U_out = unknot.

L2 (equivariant chord diagrams; refined).  Singular configuration = half-word + set S of flip sites; symbol of v :=
  prod_{s in S} eps(s) * sum_{T subset S} (-1)^|T| v(w_T).  Quotient chord diagram (code chord.py):
  - crossing site -> chord on k between its two passes, with LABEL = parity of the number of ALL x0/y0 letters passed between
    the two passes (= lk(loop of k at the double point, A) mod 2; '+' = both strands on the same half K_+, '-' = opposite);
  - winding site -> tangency T (k touches A_in); it carries its rank along A_in (order in the word) AND a direction
    delta = 'v' if k passes it in the direction of A_in (both oriented from the start vertex), '^' otherwise.
  - signs: chords use the quotient crossing sign of the oriented arc k; windings use the upstairs crossing sign (x0:+1, y0:-1,
    orientation independent: the two strands of an on-axis crossing are swapped by h).
  First attempt without delta FAILED (a_2(K) symbol took two values on types 'a+T0a+'); with delta it is consistent:
  CHECKED: level-2 symbols of M_2 and of a_2 of all five knots are constant on each type (260 configurations, 22 types);
  level-3 symbols of M_3 and of v_3 of all five knots constant on each type (300 configurations, 108 types).
  This supports both FT (order <= 3) and the classification of singular configurations by (labels, delta, A_in-order).
  Observed (CHECKED, same data): the M_3 and v_3(K) symbols never depend on delta; v_3(K_in), v_3(U_in) symbols are delta-odd.

L3 (negative results for M_3).  M_3 is NOT a linear combination of v_3(K), v_3(K_in), v_3(K_out), v_3(U_in), v_3(U_out)
  (exact least squares on 150 words: residual nonzero; also fails at symbol level on 60 random 3-site configurations).
  Adding the Sato-Levine invariants a_3 of the two butterfly links (band move along O_in / O_out, lk normalised to 0) does
  not help either (CHECKED, 150 words).  lambda_- := sum of signs of odd-label k-k crossings is NOT an invariant (takes values
  +-1,+-2 on half-words of the unknot), so it gives no order-1 invariant.
  Butterfly construction CHECKED: a_3(L^(n+1)) - a_3(L^(n)) = +-a_2(K) along the band-twist family (40/40), as the skein
  relation predicts (smoothing a band crossing gives back K).

L4 (D = the genuinely equivariant part of M_3; symbol-level obstructions).  Put D := (M_3/36 - 12 v_3(K))/5 (= iota - v_3(K)).
  * Local configurations (a knot tied in k away from the axis, K = K_1 # rK_1): J = normalised colour-2 Jones of K_1, and
    the data give M_3/36 = 24 v_3(K_1) = 12 v_3(K), i.e. D = 0 there (CHECKED: D-symbol vanishes on every all-'+' chord type).
  * Level-3 symbol of D (1200 configurations, 153 types, constant on each type; CHECKED): D-symbol in {0, +-8, +-16}; the 25
    nonzero types are listed in dtable3.json.  Two clean families:
      (2 chords + T)  D-symbol = 8 (-1)^{#odd labels} [T lies inside both chords]   (crossing or nested, either delta);
      (3 chords)      nonzero only if some chord is odd, e.g. a+b+c-c-a+b+ -> -16, a+b-c-a+b-c- -> +8.
    A short odd chord (no marked point inside) behaves like -2 T (consistent on 5 types).
  * OBSTRUCTION (CHECKED, exact linear algebra over 108 types): the D-symbol is NOT in the span of the level-3 symbols of
    v_3(K), v_3(K_in), v_3(K_out), v_3(U_in), v_3(U_out), a_3(butterfly_in), a_3(butterfly_out), N_3, and the products
    N_1*a_2(X) (X = K,K_in,K_out,U_in,U_out), N_1*N_2, N_1^3 (span has rank 14; adding D raises it to 15).
    Here N_k := sum_e J_e e^k = k![h^k] J(e^h) (expansion at t = +1; also equivariant finite type of order <= k, CHECKED
    60 samples, m = 2..4; N_1 is an ORDER-1 invariant, N_1 in 8Z, level-1 symbol: T^ -> 8, Tv -> 0, C+ -> 0, C- -> -8).
    [Correction: an earlier draft claimed a 4-type certificate on a+b+T*a+b+ / a+b+T*b+a+; that was wrong (N_3 and
    N_1-products also have nonzero symbols there).  The valid certificate is the 12-type one below.]
  * Also noted: the M_k symbols (k = 2,3) never depend on the tangency direction delta, while v_3(K_in), v_3(U_in),
    a_3(butterfly_in), N_2, N_3 do.
  * 12-type certificate (certificate.py): a linear functional y on level-3 alternating sums with y(X) = 0 for all 15
    candidate invariants X above but y(5D) = -160.  Since an identity D = sum c_i X_i of invariants would force equality of
    the alternating sums configuration by configuration, this obstruction is PROVED by exact computation (no FT needed),
    given the validated constructions of the candidate invariants.  Robustness (certificate2.py): adding level-3 symbols of
    products lambda*a_2(X), lambda*N_2, lambda*N_1^2, lambda^2*N_1, lambda^3, lambda_T*lambda_C*N_1 for HYPOTHETICAL
    order-1 invariants lambda supported on T^ or on C- still leaves D outside the span (rank 21 -> 22).  [This part uses that
    order-1 symbols vanish on Tv and on C+: C+ isolated is a kink after moves; Tv can be slid to its vertex and unwound by
    spinning the end of k about the axis.  NOTE: the same argument does NOT apply to T^, and indeed N_1 detects T^.]
  * A further candidate, the Sato-Levine invariant a_3 of K u O' (axis pushed off K at the fixed points, lk = 0; the two
    lk=0 pushoffs agree, as h predicts; CHECKED 20/20), also fails to fit D (value fit, 150 words).

L5 (local formulas; PROVED modulo the cited osp(1|2) fact, CHECKED 250 local words, 31 distinct invariant tuples).
  For local configurations (no x0/y0 letters: k is a knotted arc in a half-space bounded by a plane through A, so
  K = K_1 # rK_1 with K_1 = K_in = K_out and J = normalised colour-2 Jones polynomial of K_1):
     M_2 = -48 a_2(K_1),  M_3 = 864 v_3(K_1),  M_4 = 576 a_2(K_1)^2 - 2880 a_4(K_1) + 1728 j_4(K_1) - 240 a_2(K_1),
  where j_4 := [h^4] V(e^h) = (V''''+6V'''+7V''+V')(1)/24, a_4 = Conway z^4 coefficient.  (Proof: the M_k of a local
  configuration are order-<=k Vassiliev invariants of K_1 [colour-2 Jones at t = -e^h is a Vassiliev series: U_q(osp(1|2))
  vs U_{-q}(so(3)), as cited in BRIEF F2]; M_4 is chirality-even; order <= 4 knot invariants are spanned by
  1, a_2, v_3, a_2^2, a_4, j_4; the exact fit over 31 spanning tuples pins the coefficients.)
  Rewritten in K = K_1 # K_1 (a_2, v_3, a_4 + a_2^2/2-type rules: a_4(K) = 2a_4(K_1)+a_2(K_1)^2, j_4(K) = 2j_4(K_1)+9a_2(K_1)^2):
     M_2^loc = -24 a_2(K),  M_3^loc = 432 v_3(K),  M_4^loc = -1440 a_2(K)^2 - 1440 a_4(K) + 864 j_4(K) - 120 a_2(K).
  (M_2 = M_2^loc holds for ALL (K,h): that is the known M_2 = -24 a_2(K).)

L6 (equivariant remainders).  D := (M_3 - 432 v_3(K))/180,  F4 := (M_4 - M_4^loc(K))/1440.
  CHECKED: D and F4 are integers on 150 + 300 random words (lengths 6-22); both vanish on local configurations.
  So   M_3 = 432 v_3(K) + 180 D,    M_4 = -1440 a_2^2 - 1440 a_4 + 864 j_4 - 120 a_2 + 1440 F4   (a_2,v_3,a_4,j_4 of K).
  In the a_2 = 0 core: j_4 = sum_e V_e binom(e,4) - 9 v_3 is an integer (j_4 is in Z + 11 a_2/4 in general), and
     M_3 = 36 (12 v_3 + 5 D),   M_4 = 288 (3 j_4 + 5 (F4 - a_4)).
  COROLLARY (conditional on D, F4 in Z): if a_2(K) = 0 and J = 1 then v_3(K) = 0 mod 5 and j_4(K) = 0 mod 5
  (and D = -12 v_3/5, F4 = a_4 - 3 j_4/5).  Equivalently: a_2 = 0 and (5 does not divide v_3(K) or j_4(K)) => J != 1.

L7 (spanning-family checks; how integrality of D and F4 would be proved).  Method: if an invariant g with values in an abelian
  group A has order <= m (FT), and the top-level alternating sums depend only on the chord-diagram type (classification of
  singular configurations by labels, delta, A_in-order: CONJECTURE, consistent in all data), then: g has order <= m-1 iff
  its level-m sums vanish on one configuration of every m-element type; inducting down to g(trivial) = 0 gives g = 0.
  Types: enumerated combinatorially (enumtypes.py): 4 one-element, 24 two-element, 228 three-element types.  Realised by
  half-word configurations (random + targeted search hunt.py): 4/4, 24/24, 227/228 (missing only T0^T1^T2^, three
  tangencies all traversed against A_in in A-order).
  * f = M_3 - 432 v_3(K) mod 180: level-3 sums = 36*(5*8*D') = 0 mod 1440 on all 227 realised 3-element types; level-2 sums
    = 0 mod 180 on all 24 two-element types; level-1 sums = 0 mod 180 on all 4 types; f(trivial) = 0.  Hence
    D = f/180 is an INTEGER, PROVED modulo FT (order <= 3), the classification CONJECTURE, and the unrealised type T0^T1^T2^.
  * g = M_4 - M_4^loc(K) mod 1440: level-1,2,3 sums = 0 mod 1440 on all realised types; level-4 sums = 0 mod 1440 on 150
    random 4-site configurations (120 types).  The 4-element types were not enumerated/covered, so F4 in Z stays CHECKED
    (450 values) only.
  Family P(2k,4k-1,4k+1) (mont(-k,[4k-1,4k+1]); lp.J of k=1 reproduces the BRIEF's J of P(2,3,5) exactly):
    k=1  P(2,3,5): a_2 = 0, v_3 = -4,  a_4 = -6,  j_4 = 126;  M_3 = -2088, M_4 = 82944;    D = -2,  F4 = -24.
    k=2  P(4,7,9): a_2 = 0, v_3 = -36, a_4 = -88, j_4 = 2232; M_3 = -17712, M_4 = 1410048; D = -12, F4 = -448.
    (v_3 mod 5 = 1, 4: the corollary of L6 already excludes J = 1 for k = 1, 2.)  k = 3, 4: see section 5.
