# REFEREE REPORT on lane NEST (nest/REPORT.md), 16 Nov 2026
Referee: adversarial (Claude subagent). Scripts: referee/*.py (run with tools/venv/bin/python).
Legend: PROVED / CHECKED(n) / CONJECTURE / GAP. "Not established" = asserted, not shown.

## 0. Verdict: STANDS WITH REPAIRS (core theorems stand; one class statement is false and must be restated)
All numerical claims reproduce on FRESH, independently generated data with independent code: Theorem O (96 exact pinned
comparisons, incl. 2- and 3-box products; pins unique), nesting depth 2/3/4 (40/40), eps parity + dichotomy (24/24 fresh), T_n
(23/23, n = -8..14, all four forms incl. letter 63), Theorem V (96 fresh boxes + 40 new pretzels + 8 identity-box cases vs an
independent J_3), the two P(p,q,p) inversions (42 pairs, same knot by chirality-sensitive Jones, J differs in 40, equal only for
T(3,4)/mirror), Corollary S (715 random axis-free words: lp.J = independent 2-cable J_3(K_R), 0 failures). The nested-cap slide
(Theorems N/O) and the Theorem V unit derivation are correct; both are proofs modulo the flagged GAP 1. The program-level
consequence (Lemma Q contains 'J_3 detects the unknot') stands and is the lane's key result.
Repairs needed: a FALSE class statement (2-bridge 'both inversions reached': counterexample 7_4, whose vertical swap inversion is not a
rational necklace; the report's 7_4 data point came from merging 7_4 with 9_2 by Alexander polynomial, see S1);
status labels must say 'modulo GAP 1' uniformly (S2); one invalid 'literature-independent' argument, one mis-sourced step, one
imprecise uniqueness claim, one rationality-from-vector inference, plus minor precision items (M1-M9). GAP 2 is not needed for
Theorem O (M5).

## Plan / log
- P1 fresh random bodies (own generator, NOT general_boxes.json), own pinning with 6 closures; test Theorem O (single box, 2-box,
  |m| up to 4), eps parity, dichotomy v_2(-1) in {0,-1}, concatenation = product.
- P2 fresh nested trees depth 2-4 vs direct J.
- P3 T_n: direct J for n = -6..13 vs formula; letter-63 form (alpha, beta); span claims; non-rationality of B.
- P4 Theorem V fresh boxes / new a; Corollary S: INDEPENDENT J_3 via 2-cable + f_2 bracket on the right-half knot K_R.
- P5 literature / precision of class statements.
Source of TWIST-2CH statement: letters/letter63.md line 14-16: J(T_n) = alpha t^2n + beta (-t)^n (u = 1 normalisation),
alpha = t^-5(t^2-t+1), beta = t^2(t^4-t^3-1) + t^-6(t^2-t+1). NEST's beta = -t^9 Q_B: algebraically identical (checked by hand).

## 1. Theorem O (outer map) - recomputation  [referee/r1_outer.py, log r1_outer.log, boxes r1_boxes.json]
Independent code: own random body generator (seed 7001; caps l/r at any slot, widths up to 7, axis-letter rate 0.15-0.5), own
pinning (v1 = J(s.B), v2 solved from k = 1 and verified on k = -1, 2, -2, 3; candidate count recorded), own exact division.
24 fresh non-integral boxes (a(v) not a unit), every pin UNIQUE.
- eps(v_B) = (-1)^n0(B): 24/24.  Dichotomy v2(-1) in {0,-1}: 24/24.  CHECKED(24, fresh).
- Single-box outer map, pinned vector of r2.(y1)^m.B.u1 from scratch vs t^(2m(1-eps)) X^-m v_B, m random from +-1..+-4: 64/64 EXACT.
- Concatenation B1.B2 pinned vs v_B1 * v_B2: 12/12 EXACT (no unit).  2-box bodies (m in +-1..+-3): 12/12 EXACT.
- 3-box bodies (m in +-1, +-2): 8/8 EXACT.
VERDICT on the numerics of Theorem O: REPRODUCED on fresh, independently generated data (96 pinned comparisons, all exact).
Remark (logic of the checks): for ONE child the nesting is topologically trivial (see section 2: the nested-cap slide gives
F_k F_m = F_(k+m) as an isotopy of boxes), so the single-box tests mainly test Theorem N on depth-2 words; the real content of
Theorem O is in the >= 2-box products, which also pass.

## 1b. Nesting on fresh trees  [referee/r2_nest.py, r2_nest4.py; logs r2_nest*.log]
Leaves: 5 fresh non-rational boxes of width <= 3, twist rows +-3, +-5, integral y0/x0; twists m in {+-1, +-2, 3}; 1-3 children.
normalize(first entry of the recursive vector) vs direct J: depth 2 15/15, depth 3 15/15, depth 4 (width-1 leaves, 2 children at
levels 1 and 3) 10/10. All exact. NOTE: the nested-J test is blind to the units of Theorem O (dropping every unit t^(2m(1-eps))
gives the same normalised prediction, since * is bilinear and X linear); the exact units are tested only by pinned-vector
comparisons (section 1: 96/96).

## 2. Skein argument / Theorem N proof
Referee re-traced the nested-cap slide on N^# = N e_1: the outer cap (w -> w*) and the inner cap r2 are adjacent nested caps
with nothing between them (r2 is the first letter of N); the twist (y1)^m lies directly below them on their LEFT legs; the RIGHT
legs (strand 2 and w*) are the two rightmost strands, untouched by B (B's strands are inserted left of strand 1) and by u1. So the
slide is a genuine isotopy N^# ~ sigma^m (B^#) in H's ball, for every m (odd m only changes which leg passes through B). The
remaining zig-zag is a snake. CORRECT. Consequences, as the report says: Theorem O and Theorem N are PROVED modulo GAP 1 (the
identification of lp.J / bracket_vector with the coloured theta evaluation and of (H, X, Y, e_1) with TH-2BR coordinates).
By the same slide, single-child nesting is topologically trivial: F_k F_m = F_(k+m) as boxes (isotopy rel boundary).
UNIT (improvement): normalisation forces the unit t^(-4m p_2(-1)) for ANY integer p_2(-1) (my computation: first entry
= 1 - 4m p_2(-1)(t+1) mod (t+1)^2, and t^k = (-1)^k (1 - k(t+1)) mod (t+1)^2, so k = -4m p_2(-1), sign +). Hence the eps-dichotomy
(GAP 2) is NOT needed for Theorem O; it only rewrites t^(-4m p_2(-1)) as t^(2m(1-eps)). The parity eps = (-1)^n0 has a clean
topological reason (the right-hand string of the box lift crosses the axis exactly n0 times, so it ends bottom-right iff n0 even;
referee re-derived), but its link to v_2(-1) is still only CHECKED (50 + 24 fresh).
'Orientation meaning' (parallel vs antiparallel twist strands) re-derived: correct. '[N] = c^m X^-m [B] at bracket level':
asserted, not checked (harmless).

## 3. Class statements (Lemma L, C1, C2, C3, inversions reached, C4)  [referee/r2_twobridge.py, logs r2_*.log]
3.1 Lemma L sign conventions, NEW independent test: one-box J-classes grouped by EXACT knot type from the slope (Schubert:
  D(p/q) = S(q,p) up to mirror, key {+-p, +-p^-1 mod q}), words <= 7 (4372 words, 91 types). With X: s -> s/(2s+1) (= Lemma L's
  1/s -> 1/s+2): NO type has > 2 J-classes, every T(2,q) has exactly 1 (consistent with Sakuma's <= 2). With the opposite sign
  X: s -> s/(1-2s): 48 types with > 2 classes (chaos). So the relative sign convention of Lemma L is CONFIRMED (stronger than the
  det check, which only sees |q|). The absolute chirality (mirror) is still fixed only by convention (see 3.6).
3.2 ERROR in section 2 (i) (2-bridge 'both inversions reached'): the report lists 7_4 among knots that 'each show exactly 2
  distinct J classes' and justifies grouping by Alexander polynomial with '2-bridge knots with these determinants are determined by
  Delta'. FALSE for det 15: S(15,4) = 7_4 and S(15,2) = 9_2 both have Delta = 4t^2-7t+4 (checked with alex.py on realised words;
  Jones span 7 vs 9 confirms the identification). In words <= 6 the (4,-7,4) group contains the 7_4 class (XXyyyy) and ONE 9_2
  class (XXXXyy); 9_2's other class needs length 8 (XYYYYYYY). By slope, 7_4 has ONE J-class even with words <= 8.
  Pattern (words <= 8, q <= 29): EVERY type with p^2 = +-1 mod q shows exactly 1 one-box class (S(5,2), S(13,5), S(17,4), S(25,7),
  S(29,12) with p^2 = -1; S(15,4) = 7_4 and S(21,8) with p^2 = +1); no p^2 = +-1 type shows 2. Other 1-class types are S(q,2),
  S(q,4) with q >= 17 (cut-off). Explanation: the one-box classes of S(q,p) come from the slopes {+-p} and {+-p^-1}; they merge
  exactly when p^2 = +-1.
3.3 COUNTEREXAMPLE to section 2(i) 'For 2-bridge knots, BOTH strong inversions are reached by one-box necklaces'
  [referee/r5_slopes.py, logs r5_slopes.log, r5_74.log, r5_threechan.log]:
  - A one-box rational necklace has J = normalize(e1^T rho(w) e1), which depends only on the slope w(0) mod 1 (e1^T Y = e1^T,
    rho(X) e1 = e1, Stab(0) = <X>); the twisted closures are again of this form (X^-m w). So ALL one-box J's of det-d knots are
    obtained from the finitely many slopes b/d mod 1. Enumerated exactly for d = 15 (8 slopes) and d = 35 (24 slopes).
  - V_5(y0) = s.l1.y0.(x2)^5.u1 = P(5,-1,5) and VP(3,1) = s.l1.x0.(x2)^3.u1 = P(3,1,3) are the SAME knot as the slope-4/15
    one-box closure, namely 7_4 (det 15, Delta 4t^2-7t+4, Jones polynomial equal up to mirror; 9_2 has Jones span 9). Their vertical
    inversions have the same J_V = t - t^2 - t^3 + 2t^4 - 2t^5 + t^7 - t^8 + t^10 + t^13 (span 12), which equals NONE of the 8
    one-box J's for d = 15, nor their mirrors; 7_4's one-box class is J_A (slope 4/15, span 13).
  - Hence 7_4 has two inequivalent strong inversions (J_A != J_V up to mirror), and the vertical one (which swaps the two 1/3
    tangles of P(3,1,3) = N(1/3 + 1 + 1/3), middle crossing on the axis) is NOT a one-box rational necklace; by the report's own
    class theory (an iterated necklace of rational boxes whose closure is 2-bridge collapses to one box, using Montesinos
    uniqueness) it is not an iterated rational necklace either.
  - Same for P(7,-1,7) = S(35,6) (det 35, Delta 9t^2-17t+9): its vertical J matches none of the 24 one-box J's. Mechanism:
    P(p,-1,p) = S(p(p-2), p-1) and (p-1)^2 = 1 mod p(p-2); classically q^2 = +-1 mod p iff the continued fraction is palindromic,
    and a palindromic Conway form carries the end-swapping rotation. So for q^2 = +1 the two Schubert presentations coincide
    (one rho_h-class) and the second inversion is the palindromic SWAP, outside the calculus.
  - My earlier reading ('for p^2 = +1 the two inversions are equivalent') was WRONG and is withdrawn: they are inequivalent, J
    separates them, but only one is reached.
  STATUS of 2(i) after repair: FALSE as stated. Correct form (CONJECTURE, CHECKED): one-box rational necklaces reach exactly the
  rho_h-type inversions; for S(q,p) with p^2 != +-1 mod q these are both inversions (22 types checked with 2 classes); for
  p^2 = +1 mod q (p != +-1) the palindromic swap inversion is NOT reached (7_4, S(35,6) exact). This is the r = 2 instance of the
  report's own (ii) phenomenon (tangle-swapping inversions are not necklaces). The report's '7_4 shows 2 classes' arose from
  merging 7_4 with 9_2 by Alexander polynomial.

## 4. TWIST-2CH (T_n) recomputation  [referee/r3_twist.py, log r3_twist.log]
- Own pinning of B = y0.r2.y0.y1.y0.y1.x2.u1 with 6 closures (k = +-1,+-2,+-3): UNIQUE candidate, equal to the claimed
  v_B = (t^-7+t^-4-t^-3, t^-15+t^-12+t^-11+t^-8-t^-6); n0 = 3, eps = -1; b(v_B) has 7 terms; J(s.B) Alexander t^2-t+1 (trefoil).
- Direct J(T_n), n = -8..14 (23 values, builder had 9): equal to (i) letter-63 formula alpha t^2n + beta(-t)^n (normalised),
  (ii) NEST formula t^(4n+4) P_B + (-1)^(n+1) t^(3n+3) Q_B (exactly, no further normalisation), (iii) J of the necklace word
  s.r2.(y1)^(n+1).B.u1, (iv) normalize(e1^T X^-(n+1) v_B): 23/23 for each. CHECKED(23).
- Move (i) r1.x2 -> r2.y1 re-derived at the bracket level (TL computation, referee by hand): cap(0,1).x2 = A[cap01] + A^-1[cap12]
  = cap(1,2).y1. Move (ii) is far commutativity. So the identification T_n ~ s.r2.(y1)^(n+1).B.u1 is PROVED (isotopy), as claimed.
- Span claims confirmed: span 12 for n = 0..8 (lc (-1)^n both ends), n = 9 span 10, n >= 10 span n+3; n <= -2 span 11-n.
  WORDING SLIP (minor): "n >= 10: channels separate" is false for n = 10, 11 (P-part [29,31] vs Q-part [18,30]; [33,35] vs
  [21,33]); they separate only from n = 12. The span formula n+3 is unaffected (top from P alone, bottom from Q alone).
- Non-rationality brute force reproduced: 11 distinct normalised rational vectors (words <= 7) with a = J(s.B), all with 3-term b.
  The slope argument is sound GIVEN: (a) pinned vector = state vector up to a unit (needs Theorem N + unique pinning),
  (b) "rational box" := box in the X,Y-orbit of e_1 (vector depends only on the slope since Stab(0) in Gamma_0(2) = <X>, X e_1 = e_1),
  (c) D(s+1) = D(s) (Y is a kink under the D-closure). Status as claimed: PROVED modulo Theorem N / dictionary.

## 5. Theorem V (vertical) and Corollary S  [referee/r4_vert.py, r4_corS.py, j3lib.py; logs r4_*.log]
INDEPENDENT J_3 EVALUATOR (j3lib.py): Kauffman-bracket sweep of the 2-cable of the right-half knot K_R (closing strand on the left)
with ONE Jones-Wenzl f_2 = id - e/delta inserted, divided by delta*Delta_2, t = A^4, then normalised. It uses nothing from
flat_search/lp.J. Validation: reproduces Habiro's cyclotomic J_3(4_1) and J_3(3_1) exactly (and the builder's two quoted values).
- COROLLARY S, broad test: random AXIS-FREE words (n0 = 0, so the diagram is a connected-sum diagram K_R # K_R with h swapping
  the halves), incl. necklace words with axis-free boxes: lp.J(word) == J_3(K_R) in 94/94 (seed 424242) and 621/621 (seed 99,
  4000 words, 230 with non-trivial K_R; J_3 with up to 31 terms), always with the SAME variable convention (no mirror needed).
  CHECKED(715 + builder's 4). Together with the bubble argument (re-derived below) I rate Corollary S as PROVED modulo GAP 1 and
  very strongly CHECKED for the program's own J (lp.J), which is what Lemma Q is about.
- Bubble argument re-derived: h swaps the sides of the invariant sum sphere S, so h|S is orientation-reversing with fixed points,
  i.e. a reflection whose fixed circle is the whole axis; K n S = the 2 fixed points; S/h = disc D bounded by the two axis edges, its
  interior misses k; the bubble identity (two V_1 edges bounding D on the V_2 strand) gives theta(1,1,2)/Delta_2 <K>_{V_2}. Correct.
  Lift check: k lifts to k' u h(k'), so the upstairs knot is K # K^r (= K # K unoriented): consistent with the 'granny' word.
- PROGRAM CONSEQUENCE (Lemma Q restricted to swap inversions <=> 'J_3 detects the unknot'): logically correct given Cor. S
  (normalised unit = 1; every K is some K_R since any (1,1)-diagram of K placed right of the axis is an axis-free word).
  'Open as far as I know': agrees with referee's knowledge (only the full coloured Jones family is conditionally known to detect
  the unknot, via AJ + A-polynomial detection; nothing for a single colour). This is the report's most important finding; it stands.
- THEOREM V on the 24 fresh boxes (own pins), random odd a in {+-1,...,+-9, 11}: 96/96 exact.  New pretzels P(p,q,p) vertical,
  p in {11,-11,13,3,-3}, q in {+-1,+-8,+-9,+-10}: 40/40.  Identity box a = 3,5,7,9,11,-3,-5,-7: J(word) = ThmV(A=B=1) = independent
  J_3(T(2,a)), 8/8.
- Two inversions of P(p,q,p), q even (p in {3,5,-3,-5,7,9}, q in {+-2,+-4,+-6,8}): the two words are the SAME knot in 42/42
  (chirality-sensitive Jones of the full diagrams, tools/kauffman.py); J differs in 40/42, equal only for (3,-2), (-3,2) = T(3,4)
  and mirror; a_2 equal 42/42. Reproduces and extends the builder's 18/20.

## 5b. Theorem V derivation, independent redo  [referee/r4_derive_check.py, log r4_derive_check.log]
Own sympy computation (closure forms recomputed from X directly; partial trace A + (t + 1/t)B): K0_B numerator =
(1+t^2)(t^5 u_m + t^4 - t - u_p), K4_A numerator = t (t^5 u_m + t^4 - t - u_p): the two admissibility zeros reduce to the single
relation u_p = t^5 u_m + t^4 - t, as claimed; unit solutions exactly (t^4, t^-4) and (-t, -t^-1); the first gives Theorem V's
K_c with identity-box ratios t : Phi_3 : t^-1 Phi_5 = [1]:[3]:[5]; the second gives (1+t^2)/Phi_3 : (1+t^2)/t : t/Phi_3. CONFIRMED.
Prism admissibility re-traced by referee (triangles (v,b,a) with edges (1,2,2), rungs (1,k,c)): correct; pairs (k,c) in
{(1,0),(1,2),(3,2),(3,4)}. The a = +-1 inputs are only CHECKED in the report ('found by the pinning'); they are easy to PROVE:
in s.l1.B.(x2)^{+-1}.u1 the x2 commutes above B (disjoint positions), then the cap slide l1.x2 -> r2.y1 (the bracket identity
re-derived in section 4 for r1; l and r caps are identical for the bracket) gives the necklace closure s.r2.y1.B.u1.

## 5c. Chirality convention note
lp.J(mont(1,[3,3])) = lp.J(VP(3,-2)) = -t^-14 + t^-13 + t^-10 - t^-9 + t^-8, i.e. the MIRROR (t -> 1/t) of the 'k138 table J of 8_19'
quoted in letter 64 (-t^14 + t^13 + t^10 - t^9 + t^8); the word s.l1.x0.x0.y2.y2.y2.u1 gives the quoted table J. The brief states
'its J equals the k138 table J of 8_19 exactly', which is off by t <-> 1/t relative to the polynomial quoted in letter 64.
NEST's own example ('p = 3, q = -2 gives t^6 - t^5 + t^4 + t - 1 =. J(T(3,4))') is internally consistent with VP(3,-2) = mont(1,[3,3])
[referee/r4_example.log]. Consequence: absolute chirality labels ('P(-2m, r_i)', 'T(3,4)' vs mirror) are convention-dependent
and not independently pinned; harmless for every statement that is mirror-symmetric, but should be stated as a convention.

## 6. Issue list (claim / problem / severity / fix)
S1 [serious] Section 2(i) 'For 2-bridge knots, BOTH strong inversions are reached by one-box necklaces' is FALSE.
   Counterexample 7_4 = P(3,1,3) = P(5,-1,5) = S(15,4): its vertical (tangle-swapping) inversion has J_V (span 12), which differs
   (up to mirror) from all 8 one-box J's of det-15 knots; one-box J depends only on the slope mod 1, so this is exhaustive. Same for
   P(7,-1,7) = S(35,6). Mechanism: q^2 = 1 mod p (palindromic continued fraction) merges the two Schubert presentations into one
   rho_h-class, and the second inversion is the palindromic swap. The report's supporting data point ('7_4 shows exactly 2 J
   classes') is itself wrong: it merged 7_4 and 9_2 (same Delta 4t^2-7t+4; the premise 'determined by Delta' fails at det 15).
   Fix: restate (i) as 'one-box necklaces reach exactly the rho_h-type inversions: both inversions when q^2 != +-1 mod p, only one
   when q^2 = +1'; identify knots by slope (Schubert), not by Delta; note this is the r = 2 case of (ii).
S2 [serious, flagged by builder] GAP 1 is the only thing between 'CHECKED' and 'PROVED' for Theorems N, O, V and Corollary S, yet
   section 0 says 'DONE', and section 4 calls Corollary S 'PROVED' without the 'modulo GAP 1'. Fix: label uniformly 'PROVED modulo
   GAP 1'. Note: for axis-free words the referee's 715/715 agreement lp.J = J_3(K_R) is a computational instance of GAP 1.
M1 [minor] 'Independent of the literature: the vertical family has 3 channels, a necklace special region has 2': invalid as an
   argument for non-reachability of individual knots. Concrete: the family V_p(y0) = P(p,-1,p) has all three channel coefficients
   nonzero (Theorem V with A = 1, B = t^-3), yet its member p = 3 (trefoil) IS a one-box rational necklace (word XY, exact J match);
   members p = 5, 7 are not (section 3.3). A 3-channel family says nothing member-wise unless the necklace presentation is uniform
   in p (inside a rational box an arc-arc twist acts on a 2-dim H, so a UNIFORM family would have 2 channels; uniformity is the
   missing hypothesis). Fix: delete, or state as 'no presentation uniform in p'.
M2 [minor] Sourcing in 2(ii): [O] Oertel 1984 is about closed incompressible surfaces; 'inner side is not a sum of rational
   tangles' is false as stated (abstractly sigma^m(U_1+U_2) is U_1+U_2); for r = 3 there are no essential Conway spheres at all.
   Fix: argue in the double branched cover: sigma^m (m != 0) is a Dehn twist along a non-fibre slope (the fibre is the lift of the
   curve around the east pair, since integer sums preserve the Montesinos structure), so the sphere lifts to a JSJ torus with
   non-matching fibrations, contradicting Seifert-fibredness of a Montesinos double cover; cite Bonahon-Siebenmann for the
   characteristic Conway spheres. [BZ] Math. Ann. 277 (1987) and [MU] (Bonahon; Boileau-Siebenmann) are correctly placed.
M3 [minor] 'For q odd it [the vertical inversion of P(p,q,p)] is the only kind of inversion': for p != q odd the symmetry group is
   {1, rho_h, rho_v, rho_perp} with rho_h free and BOTH rho_v and rho_perp = rho_v rho_h (axis perpendicular to the diagram through
   the central crossing of the middle column) strong inversions (referee's geometric check of fixed points); they are inequivalent
   if Sym = Z/2 x Z/2 as recalled from [BZ] (not re-checked); both swap the outer tangles, so both are non-necklace by the same argument. Fix: say 'two tangle-swapping inversions'.
M4 [minor] Section 1(d): unit-J nested words declared unknots because the inner body 'has vector X Y^2 e_1' hence is 'rational':
   inferring rationality of a box from its vector is exactly a Lemma-Q-type statement and cannot be assumed; 'Alexander/det
   trivial' does not detect the unknot. Fix: give the explicit isotopy (the inner bodies are curls of the arc around the axis, i.e.
   Y-twists; F_k F_m = F_(k+m) is an isotopy), then TH-2BR applies.
M5 [minor] GAP 2 (eps-dichotomy) is not an input of Theorem O: normalisation forces t^(-4m p_2(-1)) unconditionally (section 2
   above). Fix: state Theorem O with that unit; keep the dichotomy as a separate CHECKED(74) parity statement.
M6 [minor] Theorem V 'derivation': the a = +-1 inputs are only CHECKED ('found by the pinning'); they follow from x2 commuting
   above B plus the cap slide l1.x2 -> r2.y1. Also the a = 0 value is formal (V_0 is a link); fine in the coloured skein theory,
   should be said. With these, 'PROVED modulo GAP 1' is fair; referee re-derived the unit relation and both unit solutions exactly.
M7 [minor] Corollary S 4_1 check was selection-biased (random det-25 words were searched for J = J_3(4_1)); replace by an
   unbiased test (referee: 715 random axis-free words, lp.J = independent 2-cable J_3(K_R), 230 non-trivial K_R, 0 failures).
M8 [minor] Precision of class statements: C1 with m' = 0 gives connected sums of 2-bridge knots (not Montesinos); 'even tangle
   1/(2m)' should read 'congruent to 1/(2m) mod 1'; 'genuinely deeper trees give non-Montesinos knots' needs 'a nested body with >= 2
   non-integral summands inside a sum with another non-integral summand' (single-child chains collapse); 'forward direction of C4
   is proved' needs that the Bonahon-Siebenmann canonical spheres are (equivariantly isotopic to) box/body spheres; section 0
   'CLASS: DONE' overstates (C4 conjecture, (ii) modulo recalled literature).
M9 [minor] Wording/conventions: T_n 'n >= 10: channels separate' is false for n = 10, 11 (blocks overlap; span n+3 still right);
   absolute chirality: lp.J(mont(1,[3,3])) is the t -> 1/t image of the letter-64 'table J of 8_19' although the brief says
   'equal exactly' (inherited; NEST's own example is consistent). Fix: state the chirality convention once.
REMARK for the program (referee): J_3(K) = 1 iff the Jones polynomial of the 0-framed 2-parallel of K equals that of the
   2-component unlink (from V_1 (x) V_1 = V_0 + V_2: <K^(2)>_0 = Delta_2 J_3 + 1 and <O O> = Delta_2 + 1). Since the Jones polynomial
   does not detect the 2-component unlink in general (Eliahou-Kauffman-Thistlethwaite, as recalled), the swap sub-problem of
   Lemma Q is a genuine 'Jones-type unknot detection' problem restricted to 2-parallels of knots.

## 7. Files
Notes: referee/nest.md (this file). Scripts: rlib.py, j3lib.py (independent 2-cable J_3), r1_outer.py, r2_nest.py, r2_nest4.py,
r2_twobridge.py, r3_twist.py, r4_corS.py, r4_vert.py, r4_derive_check.py, r5_slopes.py. Logs: r1_outer.log, r2_nest*.log,
r2_twobridge.log, r2_74.log, r2_oneclass.log, r3_twist.log, r4_corS*.log, r4_vert.log, r4_sameknot.log, r4_example.log,
r4_derive_check.log, r5_slopes.log, r5_74.log, r5_threechan.log. Data: r1_boxes.json (24 fresh pinned boxes).
