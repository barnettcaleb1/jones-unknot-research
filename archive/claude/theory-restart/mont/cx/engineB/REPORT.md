# ENGINE B REPORT (width two: the 9-dim module rho_2; Bigelow-style coincidence searches; guided extreme-term search)
Lane: ~/jones-lanes/theory-restart/mont/cx/engineB/  (Claude, started 17 Nov 2026 00:17 CST)
Marks: PROVED / CHECKED(n) / CONJECTURE / GAP.

## STATUS (01:48; final; NO HIT)
- HEADLINE: no counterexample in T3.  rho_2 (dim 9) and rho_3 (dim 51) built exactly and validated against lp.J.
  Exhaustive screen of ALL width-two theta-curves s.l1.l1.W.u2.u2 with |W| <= 14 (207,002,083 knots): every J = 1
  configuration is an unknot (|W| <= 12, rigorous via the 24-crossing JUC verification) or a presumed unknot (V = Delta = 1).
  Bigelow-type coincidence searches: rho_2 is INJECTIVE on 700,000 trivial tangles (cap side; rho_3 likewise on 250,000
  width-three tangles) and on 106,041 bottom classes (covector side), every commuting pair among 300,000 arc/curve twists is geometric, and on 400,000 group elements the only
  projective kernel is the centre.  No non-faithfulness seen.
- Near misses: doubly-gated (a_2 = 0, J(zeta_10) = 1) J's reach span 12 (two-bridge) / 13 (width two, J - 1 =
  (t-1)(t+1)^3(t^2+1)(t^2-t+1)^2 Phi_10 exactly); a_2 = 0 span floor 9 = a two-bridge knot (widths 2 and 3 never beat it);
  relatively flattest J's (span J / span V_K ~ 0.65-0.7) belong to Alexander-trivial knots, none passing zeta_10.
- Files: rho2.py (+ rho2_matrices.json), fastJ.py, fastJ3.py (width 3), fgroup.py, orbit_search.py, bottom_orbit.py,
  commute_search.py, kernel_search.py, mitm.py, mitm_gated.py, sectors.py, exact_sectors.py, template_screen.py,
  template_window.py, e3_search.py, e3w3.py, e3d_alex.py, analyse_nm.py, kcert.py, vspan.py, find_short.py; logs/json in out/.
- Log: 00:17 skeleton; 00:30 rho_2 validated; 00:55 coincidence searches; 01:10 guided searches + near-miss analysis;
  01:29 MITM (7,7) complete; 01:41 doubly-gated (7,7); 01:46 seven-sector (6,6) + window (4,4); 01:48 width-three orbit.
  out/HIT_CANDIDATES.txt was never created (no candidate at any stage).

## 1. The module rho_2 (basis, literal halfwords, normalisation)  [DONE 00:28; file rho2.py, data rho2_matrices.json]
Construction (exact, no hand normalisation): the plain Kauffman-bracket state space of the kht++ quotient picture used by
tools/flat_search.py (axis = position 0, half-strand j = band at quotient positions 2j+1, 2j+2; index 0 of a state = top end E).
The BALL = axis + half-strands 0..3 (quotient positions 0..8); the passing strand c (from v_top, half position 4) and
flat_search's auxiliary band stay outside and joined. Plain module: the 42 crossingless matchings of the 10 ball points.
f_2^{(x)4} kills exactly the span of matchings with a band matched to itself; that span is invariant (CHECKED: every letter
maps it into itself), so rho_2 := the quotient, dim 9 (= Hom(V_1, V_1 x V_2^{x4}) = 3 + 6). BASIS (pairs of the matching;
bXa,bXb = the two strands of leg X, a nearer the axis; E = axis above the ball):
   e0: E-ax  b0a-b1b b0b-b1a  b2a-b3b b2b-b3a      [= the cap vector of s.l1.l1 : caps on legs (0,1),(2,3)]
   e1: E-ax  b0a-b3b b0b-b1a  b1b-b2a b2b-b3a
   e2: E-ax  b0a-b3b b0b-b3a  b1a-b2b b1b-b2a      [= the cap vector of s.l1.l2 : nested caps (0,3),(1,2)]
   e3: E-b0b ax-b0a  b1a-b3b  b1b-b2a b2b-b3a
   e4: E-b1b ax-b0a  b0b-b1a  b2a-b3b b2b-b3a
   e5: E-b3b ax-b0a  b0b-b1a  b1b-b2a b2b-b3a
   e6: E-b3b ax-b0a  b0b-b3a  b1a-b2b b1b-b2a
   e7: E-b3b ax-b2a  b0a-b1b  b0b-b1a b2b-b3a
   e8: E-b3b ax-b3a  b0a-b2b  b0b-b1a b1b-b2a
 e0..e2: the axis passes straight (component Hom(V_0, V_2^{x4}) side); e3..e8: the axis strand turns into a leg strand.
LITERAL HALFWORDS. For W in {x0,y0,x1,y1,x2,y2,x3,y3}* (x_i/y_i, i>=1: crossing of legs i-1,i; x0/y0: axis crossing =
quotient full twist of the axis with leg 0):
   prefix P in {s.l1.l1 (caps (0,1),(2,3); s.l1.l3 gives the same state), s.l1.l2 (nested caps (0,3),(1,2))},
   suffix S in {u1.u2 (v_bot on leg 2, legs 0-1 cupped, leg 3 to c), u2.u2 (v_bot on leg 0, 1-2 cupped, 3 to c),
               u3.u2 (v_bot on leg 0, 2-3 cupped, 1 to c)};   halfword = s.P.W.S, e.g. s.l1.l1.y0.x2.y1.u2.u2.
 ORDER: the state after W = L_1...L_n is M[L_n]...M[L_1] V[P] (first letter acts first).
 Knot test: rho2.is_knot(P,W,S) (leg permutation; agrees with lp.J's knot test 1500/1500). Trivial closures (unknot, J=1):
 (l1.l1,-,u2.u2), (l1.l2,-,u1.u2), (l1.l2,-,u3.u2); (l1.l1,u1.u2), (l1.l1,u3.u2), (l1.l2,u2.u2) are links for W = empty.
NORMALISATION (t = A^4, the SAME t as lp.J; no mirror). Integral gauge f_j = A^(-2c_j) e_j, c = (0,1,0,1,1,0,1,1,1):
   Y := t^-2 M[y0]  (eigenvalues 1 (x4, axis+leg0 fuse to V_1), t^-3 (x5, V_3))       = TH-2BR Y on the width-one slice
   X_i := t^2 M[x_i] (eigenvalues 1 (x2, legs fuse to V_0), -t (x4, V_2), t^3 (x3, V_4)) = TH-2BR X
   y0 <-> Y, x0 <-> Y^-1, x_i <-> X_i, y_i <-> X_i^-1 (the BRIEF's width-one sign dictionary).  All entries in Z[t,1/t].
   V[s.l1.l1] = f0, V[s.l1.l2] = f2 (basis vectors).
   CLOSING FUNCTIONAL: PHI_S(m) := phi_y(P m), P = prod_j (1 - delta^-1 e_j) = f_2 on every leg (the naive y-functional is
   NOT zero on the self-matched span: CHECKED, 14-16 of the 33 self-matched matchings have nonzero naive y; it agrees with
   PHI only on physical states). Stored integrally:  J_raw(s.P.W.S) =. t^2 PHIT_S . rho(W) V[P] / (1+t)^4,
   and every entry of PHIT_S has the factor (1+t)^2, e.g. PHIT_{u2.u2}(f0) = (1+t)^4/t^2 (so J(trivial) = 1).
   (1+t)^4 = t^2 delta^4 is the f_2 denominator; division is exact on every physical vector (CHECKED on all samples).
 Then J = lp.normalize(J_raw) (J = 1 mod (t+1)^2).
VALIDATION: CHECKED(1007 + 269): exact equality with lp.J on random width-two knots (both prefixes, all three suffixes,
 |W| = 1..16), in the A-form (rho2.J_split) and in the integral t-form (rho2.J_t).
COMPARISON WITH CODEX'S MARKING (msgs 002116, 002550): engineB implements exactly Codex's canonical connected-arc plat
 s.l1.l3.W.u2.u2 (our s.l1.l1 gives the identical state: caps on legs (0,1),(2,3) = Codex's input cups (12),(34); our suffix
 u2.u2 = Codex's output cap (23) followed by the width-one vertex functional), W on indices 0..3, the fifth half-strand c is the
 spectator.  General two-cup words with x4/y4 (21-dim state, 9 + 12) are NOT covered by rho_2 (scope as Codex states).
 Seven-sector ranks CHECKED here: joint (X1,X3) colour ranks [[1,1,0],[1,2,1],[0,1,2]], E04 = E40 = 0 (sectors.py).
RELATIONS: CHECKED exactly: x_i y_i = 1 (i=0..3), sigma_1 sigma_2 sigma_1 = sigma_2 sigma_1 sigma_2, sigma_2 sigma_3 sigma_2 = ...,
 sigma_1 sigma_3 = sigma_3 sigma_1, tau sigma_j = sigma_j tau (j=2,3), tau sigma_1 tau sigma_1 = sigma_1 tau sigma_1 tau (type B_4).

## 2. Coincidence searches (kernel / commuting images / line stabilisers)  [00:55]
Tools: fgroup.py (exact Artin action of the type-B_4 group on F_5, puncture 0 = axis; all defining relations CHECKED as
automorphisms), orbit_search.py, commute_search.py, mitm.py, kcert.py.  Screening mod p = 2^61-1 (or p = 1 mod 2520) at random t.

2(ii) LINE STABILISERS of the cap vector v = V[s.l1.l1] (orbit_search.py).  BFS over the projective orbit [rho_2(G) v],
 deduplicated by the projective point.  Every re-hit g2 of a point first reached by g1 is decided EXACTLY:
 the trivial tangle T_g = (axis + two caps) after g has complement group F_5/<<g(c1), g(c2)>> = F_3 (c1 = g1 g2, c2 = g3 g4);
 with psi_g := psi_0 o g_*^-1 (psi_0: g0->a, g1->b, g2->b^-1, g3->c, g4->c^-1), T_g1 = T_g2 iff psi_g2(g1_*(c1)) = psi_g2(g1_*(c2)) = 1
 (one inclusion of kernels suffices since F_3 is Hopfian; equal kernels = same trivial tangle, Hilden-type coset:
 standard handlebody-extension argument, GAP: not written out here; empirically consistent, see sanity check).
 Sanity: 5000 random pairs of distinct points are never judged the same tangle; every point vs itself is (CHECKED).
 (A first version keyed cosets by the 2-D arc pair; that is WRONG: e.g. sigma_2 sigma_1^2 sigma_2 moves the shadow arc but slides
 over the cap in 3-D (Hilden).  The kernel test is the right 3-D notion.)
 RESULT: CHECKED(700,000 distinct projective points = distinct trivial tangles, all of BFS depth <= 9 and 515,556 of depth 10):
 522,942 re-hits, ALL geometric (same 3-D tangle).  NO non-geometric line stabiliser of [v] among words of length <= 10
 (each new tangle compared against all earlier ones).  Growth of the orbit: 1,4,13,44,160,598,2274,8808,34650,137892 (ratio ~3.95).
 So: the map {trivial tangles of depth <= 9} -> P^8, T -> [state of T], is INJECTIVE (CHECKED at one random t mod p; a collision
 at a random point would be required for a generic coincidence, so this is a genuine generic statement up to hash error ~1e-12).
 CONJECTURE (Bigelow-type key lemma for rho_2, offered to the theory lane): T -> [rho_2-state of T] is injective on ALL trivial
 tangles (axis + two caps); equivalently the cap vector has no non-geometric line stabiliser.  CHECKED(700,000).
 WIDTH THREE (orbit3.py; rho_3, dim 51; exact test via F_7 -> F_4, caps g1g2, g3g4, g5g6; Artin relations CHECKED):
 250,000 distinct trivial tangles (axis + three caps; depth <= 8 complete: 1,6,26,106,433,1782,7461,31822,138120; + 70,243 of
 depth 9), 377,525 re-hits, ALL geometric.  The same injectivity holds at width three (CHECKED(250,000)).

2(i) COMMUTING IMAGES (commute_search.py).  g0 in {sigma_1 = x1, tau = x0}; all conjugates C_u = rho(u) rho(g0) rho(u)^-1 up to
 BFS depth 8 (+ part of 9), deduplicated by the exact matrix (hash); tested [C_u, rho(s)] = 0 for s in {x0,x1,x2,x3}, then group
 commutation decided exactly by the Artin action.  Every pair of conjugates (a g0 a^-1, b s b^-1) is conjugate to such a pair,
 so this covers all pairs (half twist along an arc / axis twist along a curve, vs. a generator) up to the depth.
 RESULT: sigma_1-conjugates: CHECKED(150,000 distinct arcs; depth <= 8 complete): 4,998 commuting pairs, ALL geometric (disjoint
 arcs/curves); tau-conjugates: CHECKED(150,000 distinct curves; depth <= 8 complete): 6,360 commuting, ALL geometric.
 NO kernel commutator [g,h] of this type.

2(i') DIRECT PROJECTIVE-KERNEL SCREEN (kernel_search.py).  BFS over the group with EXACT element keys (Artin images of all five
 free generators), hash [rho_2(g) r] for a random r.  400,000 distinct group elements (all of length <= 8: 1,8,44,212,952,4116,
 17420,72816,302112; + 2,319 of length 9).  46 hash collisions, ALL of the form g1^-1 g2 of length 16, scalar at an independent
 second t and CENTRAL in the group (the type-B Garside element, which must act as a scalar on an irreducible module).
 RESULT: rho_2 is projectively faithful on these 400,000 elements modulo the centre.  No non-faithfulness seen anywhere.

2(iii) EXHAUSTIVE WIDTH-TWO SCREEN (meet in the middle; mitm.py).  Every width-two theta-curve s.l1.l1.G1.G2.u2.u2 with
 |G1| <= D1, |G2| <= D2 (so EVERY width-two braid word of length <= D1 + D2; other prefixes/suffixes are braid-equivalent),
 deduplicated on the top by the trivial tangle (projective vector) and on the bottom by the projective covector phi rho(G2)
 (two bottoms with proportional covectors give the same J for every top, so one representative suffices).
 Filter: J = 1 forces J_raw(zeta) = +-zeta^k; tested at zeta_7 and zeta_10 (p = 1 mod 2520).  Survivors: K certified by
 kcert.py (modular V_K: CHECKED 449/449 against the exact normalised V_K; then det, |Delta(2)|, |Delta(3)| exactly), exact lp.J
 whenever K is nontrivial.  (Bug found and fixed on the way: alex.writhe has the opposite sign convention to the bracket.)
 RESULT (D1,D2) = (5,5): 820 tops x 1,589 bottoms -> 868,361 KNOTS (leg-permutation knot test); 30,635 pass zeta_7;
   30,385 have V_K = 1, det = |Delta(2)| = |Delta(3)| = 1 (presumed unknots; 610 sampled: exact J = 1, consistent);
   250 have K nontrivial and J(zeta_7), J(zeta_10) units but J != 1 (all a_2 != 0: torus/twist-type J with sparse cofactor,
   e.g. J - 1 = (t-1)(t+1)^2(t^2+1)(t^2-t+1) Phi_9 Phi_18 / t, a_2 = -3);  HITS: 0.
 RESULT (D1,D2) = (6,6): 3,094 tops x 6,431 bottoms -> 13,263,181 KNOTS (every width-two braid word of length <= 12);
   151,707 pass zeta_7; 148,161 presumed unknots (V_K = 1, det = |Delta(2)| = |Delta(3)| = 1; 2,967 sampled: exact J = 1);
   3,546 K nontrivial with J(zeta_7) unit but J != 1;  HITS: 0.   [CHECKED(13.3M) modulo hash error ~1e-15 per knot]
   RIGOUR NOTE: a half letter x_i (i >= 1) is 2 crossings of K, x0 is 1, so |W| <= 12 gives diagrams with <= 24 crossings;
   the Jones unknot conjecture is verified up to 24 crossings (Tuzun-Sikora 2018), hence every V_K = 1 configuration of the
   (6,6) screen IS the unknot.  The zeta_7 filter has no false negatives (J = 1 exactly forces J_raw(zeta_7) in +-zeta_7^Z).
   So: NO counterexample among width-two theta-curves s.l1.l1.W.u2.u2 with |W| <= 12 (modulo random-prime hashing in the
   deduplication; tops exact, bottoms validated in bottom_orbit.py).
 RESULT (D1,D2) = (7,7): 11,902 tops x 26,089 bottoms -> 207,002,083 KNOTS (every width-two braid word of length <= 14);
   722,637 pass zeta_7; 685,033 presumed unknots (V_K = 1, det = |Delta(2)| = |Delta(3)| = 1; 13,675 sampled: exact J = 1);
   37,604 K nontrivial with J(zeta_7) unit, J != 1;  HITS: 0.  (Words of length 13-14 can have 25-28 crossings, beyond the
   24-crossing verification: there "presumed unknot" means V_K = 1 & Delta = 1; any nontrivial one would itself be a Jones
   unknot counterexample.)  Knot-class test CHECKED 20,000/20,000 against the leg-permutation test.
 SOUNDNESS OF THE DEDUPLICATION.  Tops: exact (2(ii): every merged pair is the same 3-D tangle, depth <= 10).  Bottoms
 (bottom_orbit.py): a re-hit U2 of the class of U1 means phi rho(U2) = lambda phi rho(U1), hence J(s.l1.l1.U1^-1.U2.u2.u2) =
 lambda is a UNIT by construction: a non-geometric bottom collision would itself be a candidate.  CHECKED to depth 7
 (26,089 classes): 18,930 re-hits, every U1^-1 U2 closes to a presumed unknot (V_K = 1, det = |Delta(2)| = |Delta(3)| = 1),
 and in 5,404 tests V_K(V.U1) = V_K(V.U2) for random tops V (bottoms behave as geometrically equal).
 Depth 8: 106,041 covector classes (1,4,18,74,296,1196,4842,19658,79952), 76,584 re-hits: ALL U1^-1 U2 close to presumed
 unknots (no candidate), 21,910 V_K comparisons all equal.  So no non-geometric line stabiliser on the COVECTOR side either
 (CHECKED to depth 8), and the bottom deduplication of mitm.py is validated to depth 8 >= D2 = 7.
 Width-one contamination: words in {x0,y0,x1,y1}* with prefix l1.l1 / suffix u2.u2 are width one (the cap (2,3) zigzags into
 the cup (1,2)), i.e. two-bridge (TH-2BR, proven empty); they are included in the screen (cheap) but flagged in near-miss lists.
 WIDTH THREE: the same construction gives rho_3 on Hom(V_1, V_1 x V_2^{x6}), dim 51 (429 matchings, 378 self-matched;
 invariance CHECKED); s.l1.l1.l1.W.u2.u2.u2 with W over x0..y5: CHECKED 214/214 = lp.J.  Saved: rho3_k3.pkl (A-form matrices,
 prefix vector, delta^6-scaled functional; J = normalise(NPHI.rho(W).V / delta^6)).

## 3. Guided extreme-term search  [01:10]
E3 (e3_search.py; simulated annealing over s.l1.l1.W.u2.u2, |W| = n fixed, moves = substitute / swap / delete+insert, objective
f = span(J) + 3 min(|a_2|,10); J = 1 with K unknot rejected, J = 1 with K nontrivial = HIT; exact J by fastJ.py = lp.J
(CHECKED 215/215)).  Six runs x 8 min, n = 12,16,20,24,30,40: 2.40M exact evaluations; HITS 0.
 - Minimum span(J) with a_2 = 0: 9 in EVERY run (never 7 or 8; N6 allows 7).  Best J's (all K nontrivial, ord_{t+1}(J-1) = 3,
   none passes the zeta_10 gate):  span 9: J = t^-14 - t^-13 + t^-12 + 2t^-11 - 3t^-10 + 2t^-9 - 2t^-7 + 2t^-6 - t^-5 (K: det 17,
   |Delta(2)| = 1, |Delta(3)| = 181) and its mirror; span 9, det 15 (|Delta(2)| = 165); span 10, det 15 (|Delta(2)| = 3) ...
 - TROPICAL (max-plus) ANALYSIS of 120 such near misses (fastJ.tropical / analyse_nm.py): naive extreme-degree prediction of
   PHI.rho(W).v has span median 39 (max 77) against actual ~10: deficit median 25.5 (max 62).  The loss happens INSIDE the
   state vector (local cancellation events at almost every step, ~2 per leg crossing, ~1 per axis twist, spread over all
   nine basis states), while the closing pairing loses only ~2-3 degrees.  Interpretation: the annealer finds long,
   highly NON-MINIMAL presentations of small knots (Reidemeister/braid-relation redundancy); span(J) against word length is
   therefore NOT evidence of exotic flatness.  Proper normaliser: the size of K.
 - CONFIRMATION (find_short.py): all 10 best E3 J's (span 9-10, a_2 = 0; found as words of length 16-40) occur in the
   exhaustive (6,6) enumeration as words of length 5-9; the span-9 floor is attained by s.l1.l1.y0.x1.x1.y0.x1.u2.u2 =
   WIDTH ONE (two-bridge, TH-2BR class): K = 8_2 (det 17, |Delta(2)| = 1, V_K span 8; Conway 1 - 3z^4 - z^6, a_2 = 0).
   So width two (and three, E3c) never beat the two-bridge a_2 = 0 floor (span 9),
   and the huge tropical deficits are pure presentation redundancy.  (Algebraic floor: J = 1 + (t-1)(t+1)^3(t^2+1)(t^2-t+1)
   = t^8 + t^7 + t^5 - t^3 - t has a_2 = 0 and span 7; never realised.)
 - RELATIVE FLATNESS rho := span(J)/span(V_K).  300 random a_2 = 0 width-two knots (|W| = 14): rho in [1.0, 2.1], median 1.6.
   E3 near misses reach rho = 9/11 = 0.82 (span J 9, span V_K 11).
 E3b (objective span(J) - span(V_K), a_2 penalty; 6 runs x 7 min, n = 12..40, 0.78M evaluations; HITS 0): best rho
   0.647 (span J 11, span V_K 17, n = 30), 0.682 (15/22), 0.688 (11/16), 0.70 (14/20), 0.714 (10/14 and 25/35) ...
   FINDING: most of the relatively flattest J's belong to ALEXANDER-TRIVIAL knots: |Delta_K(t)| = 1 at t = -1, 2, 3, 5, 7
   (presumed Delta_K = 1), with sparse V_K, e.g.
     s.l1.l1.x2.y1.x0.x1.x0.y1.x0.y3.y3.x1.y2.y2.x0.x2.y3.y1.x3.y1.x3.y2.u2.u2:
       V_K = 1 - t^4 + t^5 + t^8 - t^9 + t^10 - t^11 - t^14 + t^15,
       J   = t^-9 - t^-8 + 2t^-6 - 3t^-5 + t^-4 + t^-3 - 3t^-2 + 2t^-1 + 1 - t + t^2   (span 11, a_2 = 0, J(zeta_10) != 1).
   Delta = 1 forces a_2 = 0, so this is a natural targeted region (all Alexander-type necessary conditions hold);
   E3d (e3d_alex.py; reward Delta = 1 and the zeta_10 gate; n = 20, 30, 40, 8 min each, 0.15M evaluations; HITS 0):
   24 distinct J with presumed Delta_K = 1 (|Delta| = 1 at -1, 2, 3); min span J = 11 (span V_K 10..15); NONE passes the
   zeta_10 gate (V_K(zeta_5) != 1 for every Alexander-trivial knot found).
 E3c WIDTH THREE (e3w3.py with fastJ3.py = rho_3 integral t-form, dim 51, CHECKED 183/183 = lp.J; s.l1.l1.l1.W.u2.u2.u2,
   n = 14, 18, 24, 30, 8 min each, 0.50M evaluations; HITS 0): minimum a_2 = 0 span = 9 again (the same floor as width two);
   doubly-gated (a_2 = 0 and zeta_10) minimum spans 12, 13 (again the width-two values).

## 4. Near misses and cancellation mechanisms  [01:10]
(a) DOUBLY GATED (a_2 = 0 AND J(zeta_10) = 1, i.e. N1 and N2 both passed), exhaustive over all width-two words of length <= 12
 (mitm_gated.py, (D1,D2) = (6,6)): 13,263,181 knots -> 242,085 pass zeta_10 (148,161 unknots, 90,590 a_2 != 0) -> 3,334 with
 a_2 = 0, only 64 distinct J.  span histogram: 12:2, 13:6, 15:8, 16:8, 17:6, 18:10, 19:10, 20:8, 21:4, 23:2.
 * span 12: J = t^-22 - 2t^-21 + 2t^-20 - 2t^-18 + 4t^-17 - 4t^-16 + 2t^-15 - 2t^-13 + 3t^-12 - 2t^-11 + t^-10, from
   s.l1.l1.y0.x1^4.y0.x1^2.u2.u2 = WIDTH ONE (two-bridge, TH-2BR: excluded); its support misses t^0, so J - 1 has span 22.
 * span 13 (genuinely width-two words, e.g. s.l1.l1.x0.y1.y1.y1.x0.y2.x1.x1.u2.u2, 661 junctions):
       J - 1 = (t-1)(t+1)^3(t^2+1)(t^2-t+1)^2 Phi_10    exactly,
   i.e. the FORCED divisor of a doubly-gated J (D_7 (t+1) Phi_10, degree 12) times the cofactor H = Phi_6 (span 2).
   This is the closest-to-1 structure seen anywhere in the width-two class: J - 1 is the gate polynomial times Phi_6.
   K here: det 33, V_K alternating of span 12 (an alternating 12-crossing knot), so span J / span V_K = 13/12: flat only in
   the gate sense, not relatively.  (The span-12 two-bridge one: det 49, V_K span 14, ratio 0.86.)
 EXTENDED to all words of length <= 14 ((D1,D2) = (7,7)): 207,002,083 knots -> 1,305,063 pass zeta_10 (685,033 J = 1,
 590,446 a_2 != 0) -> 29,584 doubly gated, 304 distinct J; span histogram 12:2, 13:6, 14:2, 15:16, 16:24, 17:22, 18:32, ...
 The minimum does NOT drop with complexity: still 12 (the same two-bridge knot) and 13 (the same width-two J, now also
 from s.l1.l1.y0.x1.x1.x1.y0.x2.x2.x1.x1.u2.u2, 4,369 junctions).  CHECKED: doubly-gated width-two J's have span >= 12
 for every word of length <= 14.
(b) zeta_7 "false positives" (J(zeta_7) a unit root but J != 1): 250 at (5,5), 3,546 at (6,6); every one inspected has
 a_2 != 0 and J - 1 = D_7 x (sparse cofactor), e.g. D_7 Phi_9 Phi_18 / t (a_2 = -3): torus/twist-type families
 (x0^6 . y1 etc.), i.e. N1-excluded.  Not near misses.
(c) SEVEN-SECTOR TEMPLATES (Codex WIDTH2-SECTORS; template_screen.py, sectors.py, exact_sectors.py).
 CHECKED in engineB's module: joint ranks of (X1, X3) colour sectors = [[1,1,0],[1,2,1],[0,1,2]], E04 = E40 = 0.
 Screen: every junction (V top, U bottom) of the (5,5) enumeration with the double full-twist site X1^{2m} X3^{2n} inserted:
 868,361 two-parameter families; |NZ| (number of nonzero c_ab) histogram {1: 3105, 2: 124454, 3: 75044, 4: 36928,
 5: 21084, 6: 3760, 7: 603986}.  Lines on which all but one equal-slope group vanishes identically (16 directions, 49 transverse
 offsets each): 1,840; of these 480 have a non-unit surviving group (no flat line) and 1,360 are unit-valued lines
 whose knots are unknots (all in directions (0,1), (1,0): one-site twists acting on unknot configurations; 300 lines x 7
 points checked: J unit and V_K = 1, det = Delta(2) = Delta(3) = 1 at every point).  NO non-trivial flat line.
 (6,6): 13,263,181 families; |NZ| histogram {1: 14297, 2: 1183390, 3: 634096, 4: 516320, 5: 366712, 6: 103018,
 7: 10445348}; 11,870 single-group lines: 4,504 with non-unit surviving group, 7,366 unit-valued lines, and on EVERY one of
 these the knots at 5 points of the line are unknots (V_K = 1, det = |Delta(2)| = |Delta(3)| = 1).  NO non-trivial flat line.
 WINDOW SCREEN (template_window.py): every junction of the (4,4) enumeration with |m|, |n| <= 6 (58,173 families, 9,831,237
 theta-curves, words up to 32 letters with two long twist rows): 254,389 zeta_7 survivors = 154,869 J = 1 presumed unknots +
 99,520 J != 1 with J(zeta_7) a unit root (examples: a_2 = 91, +-14, torus-type); HITS 0.
 Exact c_ab of two gated near-miss templates (out/exact_sectors.json): (V,U) = (x0.y2.y2.x1.x1, x1.x1.y0.x1): no sector vanishes;
 exact relation c42 = -c44 (so the a = 4 group vanishes on the whole line n = 0: the X1-twist family has only colours 0, 2);
 (V,U) = (y0.y2.y1.x0.x3.y2, y3.x2.x2.y3.x0.x1): no sector vanishes; c02 = c20 and c24 = c42 exactly (site-exchange symmetry).
 Neither admits a unit line (>= 2 singleton groups survive in every direction).
(d) MECHANISMS seen.  (i) Width one / two-bridge: no cancellation at all (tropical deficit 0: the TH-2BR automaton is exact);
 (ii) all width-two near misses: large tropical deficit from non-minimal presentations, absorbed inside the state vector;
 (iii) gate-passing near misses come from twist families (rows of x1^k between axis twists), consistent with Codex's
 torus-row certificate (J_m = 1 at all primitive 10th roots for m = 5k, span 5k+3): the zeta_10 gate is cheap for families;
 (iv) unit lines exist only where one site acts by a scalar on one side (geometric: the twist slides off a cap/cup).

## 5. What was searched, to what bound (all exact algebra or exhaustive structured enumeration; no blind sampling)
 * rho_2 (dim 9) and rho_3 (dim 51) built exactly from the quotient bracket; CHECKED against lp.J (1,276 + 183 knots).
 * Line stabilisers of the cap vector: ALL trivial tangles (axis + 2 caps) reachable by words of length <= 9 (184,444) and
   515,556 of length 10: the tangle -> projective-state map is injective (exact geometric test on every coincidence).
 * Width three: 250,000 trivial tangles (axis + three caps), depth <= 8 complete: rho_3-state map injective.
 * Line stabilisers of the closing covector: ALL bottom classes to depth 8 (106,041): every coincidence closes to an unknot.
 * Commuting images: all conjugates of sigma_1 (arcs) and of tau (axis curves) to depth 8 (+ part of 9), 2 x 150,000: every
   commuting pair is geometric.
 * Projective kernel: 400,000 group elements (complete to length 8): only the centre acts by scalars.
 * Exhaustive J = 1 screen of width-two theta-curves s.l1.l1.W.u2.u2: ALL W of length <= 12 (13.3M knots; rigorous via
   the 24-crossing verification) and ALL W of length <= 14 (207M knots): no hit; every J = 1 configuration is an unknot
   (length <= 12) or a presumed unknot (V_K = 1, Delta = 1).
 * Seven-sector two-parameter twist families X1^{2m} X3^{2n} at every junction of the (6,6) enumeration (13.3M families):
   no non-trivial flat line (every unit-valued line is an unknot family); window |m|,|n| <= 6 at every (4,4) junction
   (9.8M theta-curves): no hit.
 * Guided searches: E3 (2.40M evals, width two), E3b (0.78M, relative flatness), E3c (0.50M, width three), E3d (0.15M,
   Delta = 1 class): no hit; floors FOUND (heuristic minima, not bounds): span(J) = 9 when a_2 = 0 (both widths; attained by a
   two-bridge knot); Delta = 1: 11.  Doubly gated (a_2 = 0 & zeta_10): exhaustive minimum 12 (two-bridge) / 13 (width two)
   over ALL words of length <= 14 (207M knots).
 NON-FAITHFULNESS: none observed for rho_2 on any tested element (beyond the centre, which acts by scalars by Schur).
