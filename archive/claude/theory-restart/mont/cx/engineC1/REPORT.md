# ENGINE C1 REPORT (cx lane): closing the arborescent frontier
17 Nov 2026, Claude (engine C1). Folder ~/jones-lanes/theory-restart/mont/cx/engineC1/ . Python: tools/venv/bin/python (pure Python).
Marks: PROVED / CHECKED(n) / CONJECTURE / GAP.   STATUS: FINAL (03:26).  NO HIT.

## HEADLINE
 * THEOREM V3 (PROVED): no vertical (dihedral) closure V_a, any odd a, of a product of n >= 2 non-integral rational boxes with any
   integral part is flat (for |a| >= 3 even n = 1, by the certificate generator of Section 2b).  With Q-MONT this closes BOTH arborescent root types over Montesinos bodies (depth one) by theorem.
   Ingredients: a rigorous FINITE jet automaton for rational boxes (19 states at order 3, 35 at order 4), the BX4-type lemma (BX4'),
   a per-box second-order bound (T2), and the sigma-law, which fixes the slope mismatch at the weak end to be exactly +1.
 * THEOREM V3(B) / H(B) (PROVED per box by exact Farkas certificates on the automaton; the generator re-derives Q-MONT and V3
   by itself): for 46,771 listed non-rational boxes B (97% of the eligible depth-1 Montesinos boxes F_m(Y^N u u'), 96% of the
   general-body-based boxes, 90 of the positive-potential depth-2 boxes), B x (ANY n >= 1 rational tangles) x Y^N is never flat,
   under EVERY horizontal twist mu and EVERY vertical closure a.  This extends engineA's bounded regions 5(c), 5(d) (rational
   partner from R(7)/R(8)) and 5(e') (rational factors from R(5)) to ALL rational parts, for the covered B.
 * TWO non-rational children (depth-two step): for every pair B1, B2 from the 300 most frequent jet classes (27,585 boxes;
   380M pairs) and ANY n >= 0 rational boxes, all horizontal and vertical closures are non-flat (PROVED by the same
   certificates; no open case at all).  In particular every two-child necklace of such boxes is non-flat (engineA's unfinished
   library-A pair search, closed by theorem for these classes).
 * LEMMA S3 (PROVED): every rational box has tau := l2_top(q) + l2_bot(q) = -1 (third-order Lemma S), and generic nested boxes
   inherit (delta, sigma, tau) = (-1, 0, -1) (LEMMA Z, via the X-eigen-coordinate z = (q-1)/(q-e2), in which F_m is z -> (-t)^-m z
   and the closure pole is the MONOMIAL (-t)^-mu).
 * engineA's third-order POSITIVITY is FALSE at mu = -2 (17 counterexample pairs, Delta_t + Delta_b in {-2,-1}); the wall there is
   ONE-ENDED (Delta >= 2 at the e2-like end, CHECKED 54/54).  At mu = +-1 positivity holds on all 231,910 ties.
 * FRONTIER (exact hashing of jets, no sampling): depth-3 nesting around the 292 positive-potential boxes and around body 43
   (581k boxes) never pushes the two-ended tie depth past 4: pairs reach 3 (vertical) / 4 (one accidental class around body 43),
   triples reach 4; nesting one level deeper around the depth-4 configuration DROPS it back to 3.  The depth grows with the number
   of factors, not with nesting, and far below the requirement r_top + r_bot = span A + span w - 2 (~ 30-70 here).  0 units.

## 1. A rigorous finite jet automaton for rational boxes (jauto.py)  [PROVED + CHECKED]
 State r = v_2/v_1 (TH-2BR); combined step m: r_pre = Y^m r, D = 1 + (1-t^4) r_pre, r' = -(1+r_pre)/D, a -> a D; b = a q,
 q = 1 + (1-t^3) r.  Implemented with ABSOLUTE-PRECISION-TRACKED truncated series at t = infinity; a state key is (deg r, relative
 jet of r to order K), 'tiny' (r = O(t^(-4-K)), i.e. S_j with j >= K) or 'init'.  Each transition is computed from the key alone and
 the code ASSERTS that D and r' are known to relative order K (soundness: the key determines the next key and the log-jet of D for
 every exact r with that key).  Exponent clipping: all states have deg r <= -1, so for m >= M = K+3 (resp. <= -M) the extra terms of
 Y^m r lie beyond relative order K (argument in jauto.py; m = M, M+1, M+2 agree from every state: CHECKED).
 RESULT: the automaton is FINITE: K = 2: 9 states; K = 3: 19 states / 227 transitions; K = 4: 35 states.
 VALIDATION: log-jets of a and b to order 2, 3, 4 and (deg, lc) of q agree EXACTLY with exact Laurent computation on all 79,422
 normal-form boxes with k <= 5, |m| <= 4 and k <= 6, |m| <= 3 (CHECKED 79,422 x 3, 0 mismatches; jval.py).
 Top classes (BX2 names) and q-data (rho_q, lambda_q) = (l1, l2) of the normalised top series of q (v3lemmas.py, PROVED):
     R_1: (1, -1/2);  R_0: (0, -1) or (0, -2);  S_0: (-1, -1/2);  S_1: (0, +1);  S_2: (0, 0);  S_{>=3}: (0, 0).
 Psi = rho_a + phi (phi(R) = 1, else 0) is non-increasing on all 227 edges (= BX3); longest paths: max rho_a = -1 for R-top and
 for S_{>=1}-top boxes, 0 for S_0-top (PROVED).
 LEMMA BX4' (engineA GAP 1; PROVED by hand and by the automaton).  If u is R_1-top with rho_a(u) = -1 (equivalently a Psi-preserving
   path: alternating signs ending POSITIVE), then l1(b) = 0 and l2(b(u)) = -(k - [m_0 <= -2] + 1)/2 <= -1.
   Proof: along an alternating path each step has x1(D) = +-1 (init -> S_0: 0) and x2(D) = 0 (BX4 expansions), so
   l2(a) = -(k - [m_0<=-2])/2; the final R_1 state has r = t^-1(1 + u + u^2 + O(u^3)) (from S_j/init by a positive power:
   r_pre = t^-3(1 + O(u^3)), D = -t(1 - u + 0u^2 + ..)), so q = -t^2(1 + u + 0u^2 + ..), l2(q) = -1/2.  []
 LEMMA T2 (PROVED, automaton longest paths): lambda_q + rho_a <= 0 for EVERY rational box; <= -3/2 (R_1-top), <= -1/2 (S_0),
   <= -2 (R_0), <= 0 (S_1), <= -1 (S_2, S_{>=3}).

## 2. THEOREM V3 (vertical Lemma Q for rational bodies)  [PROVED]
 STATEMENT.  n >= 2, u_1..u_n non-integral rational boxes, N in Z, a odd, |a| >= 3: the vertical closure J(s.l1.B.(x2)^a.u1),
 B = Y^N u_1...u_n (J Phi_3 =. w_1(a) A + wV(a) t^-3N B, Theorem V) is NOT a unit.  For a = +-1, wV(+-1) = t^(+-3) w_3(+-1), so the
 vertical closure is a horizontal necklace with mu = +-1 (Q-MONT).  Hence NO vertical closure of >= 2 non-integral rational boxes
 (any odd a, any integral part) is flat.
 PROOF.  F = S1 + S2, S1 = w_1 A, S2 = wV t^-3N B; a unit means F = c t^e Phi_3.  At an end write s1, s2 for the normalised
 expansions (x_k their coefficients), delta := top S1 - top S2, eps := lc S2 / lc S1, alpha = sum rho_a, beta = sum rho_b (<= 0,
 BX3), P = beta - alpha = sum rho_q.  Lemma W: some end coincides.  If only one end coincides, the other ('weak') end has delta != 0
 and the coincident end cancels r = Tot >= 8 orders; if both coincide, r_top + r_bot = Tot and by Theorem V2 one end ('weak') has
 r <= 1 and the other r >= Tot - 1 >= 2.  Since F = -A w_1 (Q/q* - 1) (Q = t^-3N prod q_i, q* = -w_1/wV), r >= 2 at the strong end
 means s1(Q) = s1(q*) there, and the sigma-law (sum over boxes of s1_top + s1_bot is 0, while it is -1 for q*) gives at the WEAK
 end the exact mismatch s1(Q) - s1(q*) = +1.  By the mirror R2 (a <-> -a, top <-> bottom) it suffices to treat a weak TOP.
 Top data: a >= 3: w_1 = -t^(a+2)(1 + 0u + u^2 + ..), wV = t^(3a+3)(1 + u + u^2 + u^3 + u^4 + ..);
           a <= -3: w_1 = t(1 + 0u - [|a|=3] u^2 + ..), wV = -t^(a+1)(1 + O(u^4)).
 The weak-top mismatch +1 reads P = 0 (a >= 3) and P = 1 (a <= -3).  The Phi_3 pattern needs F's normalised top expansion
 1 + u + u^2 + 0u^3 + .. :
  delta >= 2: needs x1(s1) = 1, but x1(s1) = alpha <= 0.                                                       IMPOSSIBLE
  delta = 1: needs alpha = 0, eps = 1 (all boxes alternating S-boxes, rho_b = -1 each) and x2(s1) + x1(s2) = 1; but by BX4
     x2(s1) <= 1 (a >= 3) or <= 0 (a <= -3), and x1(s2) = 1 - n or -n.                                          IMPOSSIBLE (n >= 2)
  delta = 0, no cancellation: needs x1(s1) + x1(s2) = 2 but it is <= 1.                                        IMPOSSIBLE
  delta = 0, r = 1: needs x2(s1) - x2(s2) = x1(s1) - x1(s2) (= -1): a >= 3: sum_i (lambda_q,i + rho_a,i) = 1;
     a <= -3: sum_i (lambda_q,i + rho_a,i) = 1/2 - [|a| = 3].  T2 gives sum <= 0, killing a >= 3 and |a| >= 5; for a = -3,
     P = 1 means #R_1 = #S_0 + 1, so sum <= -3/2 #R_1 - 1/2 #S_0 <= -3/2 < -1/2.                                 IMPOSSIBLE
  delta = -1: needs x1(s2) + eps = 1.  a <= -3: beta = 0 (all R_1-alternating) and then x2(s2) + x1(s1) <= -2n.
     a >= 3: eps = 1, beta = -1, P = 0 so alpha = -1; with n >= 2 this forces n = 2 (one alternating S-box, one alternating
     R_1-box) and the second-order condition sum l2(b_i) = 1/2 - alpha = 3/2, but sum l2(b_i) <= -1/2 - 1 (BX4, BX4').  IMPOSSIBLE
  delta = -2: needs x1(s2) = 1: a <= -3 impossible; a >= 3 forces all boxes R_1-alternating and x2(s2) = 1 + sum l2(b_i) <= 1 - n,
     but it must be 0 or 2.                                                                                         IMPOSSIBLE
  delta <= -3: needs x1(s2) = 1 and x2(s2) = 1: as for delta = -2.                                              IMPOSSIBLE  []
 Ingredients: Lemma W, Lemma S / Theorem V2 (engineA), BX1-BX4 (notie), BX4' and T2 (here).  Independent check (v3check.py,
 4,000 random closures with forced coincidences): whenever one end had r >= 2 (162 cases) the weak-end mismatch was exactly +1;
 no two-ended r >= 2; no unit.  Consistent with engineA E11/e11_mix (complete searches, 0 units).
 WHAT IT IMPLIES.  Lemma Q holds for every strongly invertible (K, h) whose quotient is the vertical closure s.l1.B.(x2)^a.u1 of a
 Montesinos-type body B = Y^N B(w_1)...B(w_n) (n >= 2 non-integral rational tangles, any integral twist, any odd a).  So for each
 such (K, h) and every n != 0 the branch knot L_n = T(1/n) has V(L_n) != 1: the Jones polynomial detects the unknot on all their
 branch knots.  With Q-MONT (horizontal) and TH-2BR, every depth-one arborescent quotient (root closure over a product of rational
 tangles, horizontal or vertical) is now closed by theorem.

## 2b. THEOREM V3(B): vertical closures of ONE arbitrary box B with ANY rational boxes  [PROVED per B, exact certificates]
 v3b.py / v3b3.py turn the Section-2 casework into a THEOREM GENERATOR.  For a box B put rho_a^B, l2(a_B), rho_b^B, l2(b_B) = the
 first two log-coefficients of its channels at each end and sigma(B) = s1_top + s1_bot of its slope.  If sigma(B) != -1 (= sigma*_V)
 the weak end exists and its mismatch is m_B = sigma(B) + 1 (rational boxes contribute 0 by Lemma S); each weak-end case
 (offsets delta >= 3, 2, 1, -1, -2, <= -3; delta = 0 with r = 0 or r = 1; eps = +-1; both ends; a >= 3, a <= -3, |a| = 3) becomes
 linear equations in the rational sums (alpha, P, L_a, Lambda) = sum (rho_a, rho_q, l2(a), lambda_q) with P pinned by m_B, and is
 closed by a FARKAS CERTIFICATE: multipliers y with sup over ALL rational boxes of y.(per-box vector) <= 0 (sup computed EXACTLY
 as a longest path on the K = 3 jet automaton; float screening, Fraction verification of every certificate used) and
 right-hand side > n_min * sup.  Sanity: with B empty and n_min = 2 it re-derives Theorem V3 automatically, every case closed;
 with n_min = 1 also every case closes (V3 holds for a SINGLE rational box at |a| >= 3; CHECKED: the 28 vertical units among the
 576 boxes of R(8) are all at |a| = 1).
 RESULT (v3b_run.py, 50,430 boxes, 5,794 jet signatures, 45 s): V3(B) PROVED, with B's channel leading-coefficient ratio of modulus 1
 at both ends (so eps = +-1; boxes violating this are excluded), for
     28,318 / 29,520 depth-1 Montesinos boxes F_m(Y^N u u')  (u in R(5), |m| <= 3, |N| <= 3),
     18,598 / 20,160 boxes F_m(Y^N g u) and 419 / 445 boxes F_m(Y^N g) on the 14 general bodies, 6 of the general bodies
     themselves, and 156 / 292 of the depth-2 positive-potential boxes:
   for each such B, every n >= 1 non-integral rational boxes u_i, every N and every odd |a| >= 3, the vertical closure
   s.l1.(Y^N B u_1...u_n).(x2)^a.u1 is NOT flat.  Open: 1,282 boxes with sigma(B) = -1 (two-ended second-order ties possible),
   ~5,400 where the delta = 0, r = 1 case needs third-order data, 4 with delta = -2.  Brute-force sanity (random companions from
   R(6), all Lemma-W candidates): 4,620 + 3,017 candidates, 0 units.
 WHAT IT IMPLIES: Lemma Q (hence Jones detection for all branch knots L_n) for the vertical inversions whose quotient body is
 'one depth-1 (or general / listed depth-2) tangle plus ANY number (>= 1) of rational tangles' - extending engineA's bounded
 searches 5(c), 5(d), 5(e') (rational parts from R(5)-R(8)) to ALL rational parts, for the listed B.  (Single-child closures of B
 alone, engineA 5(a), 5(b), are a different class and stay computational.)

 HORIZONTAL ANALOGUE H(B) (h3b.py; same casework with (w_1, w_3)(mu); the order-2 jets of w_1, w_3 at both ends and sigma*, delta*
 are constant for mu >= 4 and for mu <= -4 (asserted for |mu| <= 10, clear from the formulas), so the mu-classes {+-1, +-2, +-3,
 >= 4, <= -4} are exhaustive).
 VERSION 2 (gen2.py, gen2_run.py): in the cases where the weak end coincides in degree (delta = 0, r = 0 or 1) BOTH ends coincide,
 so the delta-law pins n exactly: n = delta(B) - delta*(mu) (horizontal), n = delta(B) + |a| + 1 (vertical); with n pinned a
 certificate only needs rhs > n * sup.  If sigma(B) = sigma*(mu) the same law leaves at most one exceptional n (reported open).
 SANITY: with B empty the generator now re-derives Q-MONT for EVERY mu (n >= 2) and Theorem V3 (n >= 1, |a| >= 3) automatically.
 FINAL RESULT (gen2_run.py, 105 s; boxes with |lc(b)/lc(a)| = 1 at both ends and span a >= 1, i.e. 48,683 of 50,430):
   V3(B) (every odd |a| >= 3):      28,318 NRR, 18,598 NGR, 419 NG, 6 G, 156 d2pos               (47,497 boxes)
   H(B) (EVERY mu != 0):            28,228 NRR, 18,994 NGR, 425 NG, 6 G, 90 d2pos                 (47,743 boxes)
   BOTH (every closure, any odd a): 27,844 NRR, 18,417 NGR, 416 NG, 4 G, 90 d2pos                 (46,771 boxes)
   (NRR = depth-1 Montesinos boxes F_m(Y^N u u'), u in R(5), |m|,|N| <= 3: 28,714 eligible; NGR = F_m(Y^N g u): 19,272;
    NG = F_m(Y^N g): 431; G = general bodies: 10; d2pos = depth-2 positive-potential boxes: 256.)
 i.e. for each such B, every n >= 1 non-integral rational boxes and every N, NO horizontal necklace X^mu Y^N (B u_1..u_n) (any
 mu != 0) and NO vertical closure (any odd a) is flat.  Open (box-weighted): V: delta = 0, r = 1 needing third order (1,519),
 sigma(B) = -1 (806), delta = -2 (4); H: exceptional n = 2, 3 at mu = +-2, +-1 (~600) and a few hundred delta = 0, r = 1 cases.
 NEGATIVE CONTROL (soundness): rational-only with n >= 1 horizontal (where genuine units, the two-bridge unknots, exist at n = 1)
 the generator does NOT conclude: it leaves open exactly mu = +-1 (offset -2), mu = +-2 (delta = 0, r = 1), |mu| >= 3 (two-ended
 tie at n = 1).
 TWO NON-RATIONAL BOXES (gen2_pairs.py; depth-two step): B1 * B2 is one box whose end data are the SUMS of the two signatures,
 so the generator applies verbatim.  For all 7,260 unordered pairs of the 120 most frequent signatures (19,754 boxes, i.e.
 195,120,135 box pairs), EVERY case closes: for every such pair B1, B2, every n >= 1 rational boxes, every N, every mu and every
 odd a, the necklace X^mu Y^N (B1 B2 u_1..u_n) and the vertical closure are NOT flat (PROVED by certificates; brute-force sanity:
 5,688 vertical + 347 horizontal Lemma-W candidates with random companions, 0 units).  The same holds with n = 0 (n_min = 0;
 the preconditions span A >= 5 hold since every non-rational library box has span a >= 4): every TWO-CHILD necklace and vertical
 closure B1 B2 with both children in these 120 classes is non-flat - a theorem-level closure of the bulk of engineA's library-A
 pair search, whose deep stages were never finished (sanity: 1,299 horizontal + 12,056 vertical candidates, 0 units).
 EXTENDED: the 300 most frequent classes (27,585 boxes): all 45,150 signature pairs (380,479,905 box pairs) proved, no open case,
 both with n >= 1 rational boxes (gen2_pairs300.log) and with n >= 0 (gen2_pairs300_n0.log).
 Brute-force sanity on the 46,771 'BOTH' boxes with random companions from R(6), all Lemma-W candidates: 681 horizontal +
 7,004 vertical candidates, 0 units (and 4,620 + 3,017 vertical candidates in the first run).

## 3. Third-order end laws and the third-order wall (GAP 2)
 3.1 LEMMA S3 (PROVED, taulaw.py).  For every non-integral rational box: (delta, lc_top lc_bot, sigma, tau) = (-1, -1, 0, -1), where
     tau := l2_top(q) + l2_bot(q).  Proof: bottom data of u = top data of u'' = u(-m_0-1, -m_1, ..) (R2); run the K = 3 automaton on
     u and u'' simultaneously (independent clipping is sound): 28 reachable product states, the four quantities are constant.
     (R_0 with lambda_q = -2 pairs only with S_1 (+1), R_0 with -1 only with S_{>=2} (0).)  For rational products the order-3
     mismatch is additive: Delta_t + Delta_b = -n - tau*.
 3.2 EIGEN-COORDINATE (PROVED; two-child formula CHECKED 300/300 exact).  z := (q-1)/(q-e2) = -(1+t^2) beta/alpha, e2 = -t/(1+t^2),
     alpha = (ta + (1+t^2)b)/Phi_3, beta = (a-b)/Phi_3 (so a = alpha(1-z), b = alpha(1-e2 z)).  X^mu: z -> (-t)^mu z; nested box
     F_m(p): z = (-t)^-m z(p), alpha unchanged up to a unit; product: alpha_p = prod alpha_i [t prod(1-z_i) + (1+t^2) prod(1-e2 z_i)]/Phi_3;
     horizontal closure J = prod alpha_i [w_1 prod(1-z_i) + w_3 prod(1-e2 z_i)]/Phi_3, e.g. for two children
         J = alpha_1 alpha_2 [ 1 - (-t)^mu (z_1 + z_2) + ((t + (-t)^mu Phi_6)/(1+t^2)) z_1 z_2 ],
     and the pole q* = -w_1/w_3 is z* = (-t)^-mu, a monomial.  (w_1 + w_3 = Phi_3.)
     LEMMA Z (PROVED): if ord_top z >= 3 and ord_bot z <= -4 (or ord_top z <= -4 and ord_bot z >= 3) then the slope end data are
     (d, lc, l1, l2) = (0, 1, 0, 0) at the z-small end and (-+1, -1, 0, -1) (= jet of e2) at the z-large end, hence
     (delta, lc lc', sigma, tau) = (-1, -1, 0, -1) exactly as for rational boxes.  F_m shifts ord z by +m at the top, -m at the
     bottom, so large twists make boxes rational-like ('eigenslope contraction').  Only boxes with a small z-order at some end can
     move delta, sigma, tau (ztypes.py: the 50k library-A boxes by (ord_top z, ord_bot z); e.g. class (3, <=-4): 5,123 boxes, all
     (-1, 0, -1); class (2, <=-4): tau = 0; class (0, -1): 253 different (delta, sigma, tau)).  Further classes: z small at BOTH
     ends = near-scalar box (q ~ 1 at both ends: delta = sigma = tau = 0; exactly scalar = local knot, T4), z large at both ends:
     (-2, 0, -2).
 3.3 POSITIVITY IS FALSE AT mu = -2 (CHECKED, tau2.py, tau3.py).  Census of second-order two-ended ties of pairs (library A x
     (A u R(8)), engineA spec): mu = +-1: 115,955 + 115,955, min(Delta_t + Delta_b) = 2 (positivity holds); mu = 2: 8 ties,
     Delta_t in {-1,0}, Delta_b in {3,4}; mu = -2: 46 ties, 17 with Delta_t + Delta_b in {-2,-1}, e.g.
       F_3(Y^2 (B(XXY) B(y)) (B(XXXXY) B(y))) x F_1(Y^3 (g43 B(yy)) (B(XXXyy) B(y))), mu = -2, N = 1: depths (2,2),
       (Delta_t, Delta_b) = (2,-4), span J 34.
     Surviving statement (CONJECTURE W3, CHECKED 231,964): at a second-order two-ended tie of depth-<=2 boxes,
     (Delta_t, Delta_b) != (0,0); mu = +-1: Delta_t + Delta_b >= 2; |mu| = 2: Delta >= 2 at the end where q* has the jet
     (1, -1/2, 4/3) (top for mu = -2).  So at |mu| = 2 the wall is one-ended, not an additive law.  GAP: a proof needs the joint
     (top, bottom) z-jet bookkeeping of depth-1 child products at small z-order; with S3 the rational inputs are finitely many
     classes, but the casework was not completed.
     Targets (tau* = l2_top + l2_bot of q*): mu = +-1: -1; +-2: +1/2; +-3: -2; |mu| >= 4: -1.

## 4. Frontier search (all exact; jets hashed exactly at both ends; every tie of order >= 3 evaluated exactly with Lemma W's N)
 4.1 Depth 3 around the 292 depth-2 positive-potential boxes: F_m(Y^N s u), u in {1} u R(4), |m| <= 3, |N| <= 2: 128,264 boxes
     (73% generic).  Pairs with library A u R(8) u themselves (fr_pairs.py d2pos): horizontal |mu| <= 12: 502,960 second-order
     two-ended ties, NO third-order; vertical 3 <= |a| <= 13: 70,554 second-order, 26 of depth exactly (3,3) (all a = +-7, span J
     38-50).  0 units.
 4.2 Around general body 43: depth 1 (442), depth 2 (192,017), depth 3 around 600 non-generic depth-2 boxes (260,802): 453,261
     boxes (fr_pairs.py g43): horizontal 50.4M second-order ties, 675,528 of depth 3, 160 of depth exactly (4,4); vertical 1.28M
     second-order, 89 of depth 3.  0 units.  All 160 depth-4 ties use ONE depth-2 box
       X = Y^-1 F_-2(Y^2 F_-2(Y^2 (g43 B(yy)) B(xyy)) B(XXXY) B(y))
     against 20 library boxes F_2(Y g30 u ..), at every mu = -5..-12 (span J 57-73).  MECHANISM: the bottom jets are exact negatives
     to order 3, (-1, 1/2, -4/3) + (1, -1/2, 4/3) = 0, and the top jets add to (0, -1, 0) = jet of e2: the pair IMITATES a single
     generic nested box, whose jets are the pole jets for |mu| >= 5.
     CHASE (chase.py, fr_pairs2.py): one more nesting level around X, its jet-class mates and the 20 partners (9,282 boxes) against
     the whole 513k pool: 627,309 + 6,745 second-order ties, 14,091 of depth 3, NONE of depth 4.  The coincidence does not propagate.
 4.3 THREE factors, class-level exact census (fr_triples.py, fr_eval3.py; pool = library A u R(8) u 4.1, 753 second-order classes):
     third-order two-ended ties exist (horizontal all |mu| except 2; vertical all |a|); exact evaluation of the 794 class
     representatives: 781 of depth 3, 13 of depth (4,4) (e.g. mu = 3: F(Y^N u u') x g x F(g'), span J 30 from span A 36, a_2 = -1;
     vertical a = 5, three depth-1 Montesinos boxes, span J 36); none of depth 5; 0 units; min span J 29; 2 with a_2 = 0 (span 38),
     none passes J(zeta_10) = 1.
 SUMMARY (CHECKED): two-ended depth <= 4 everywhere; it grows with the number of factors (pairs 2-4, triples 4), not with nesting
 depth, while a unit needs r_top + r_bot = Tot = span A + span w - 2 (30-70 in these pools).

## 5. Closed regions and the lemma list for 'Lemma Q for every arborescent quotient'
 CLOSED BY THEOREM: (i) TH-2BR (width one); (ii) Q-MONT: horizontal necklaces over >= 2 rational boxes, special twist X^mu, any
 integral part; (iii) THEOREM V3 (here): vertical closures over >= 1 rational boxes (|a| >= 3; >= 2 boxes for a = +-1), any integral
 part.  Together: every depth-one arborescent quotient (root closure over a Montesinos body of rational tangles) has J != 1.
 (iv) THEOREM V3(B) / H(B) (here, per-box certificates): one listed box B (46,771 boxes: depth-1 Montesinos, general-body-based,
 depth-2 positive-potential) plus ANY number (>= 1) of rational tangles: every horizontal twist and every vertical closure (47,497
 boxes for vertical alone, 47,743 for horizontal alone).  This turns engineA's bounded regions 5(c), 5(d), 5(e') into theorems for
 all rational parts.
 CLOSED IN THE TWO-ENDED SENSE (CHECKED, Section 4; not unit-complete): pairs/triples above have min(r_top, r_bot) <= 4, and every
 tie of order >= 3 was evaluated exactly (no unit).
 LEMMA LIST.  Lemma Q for every arborescent quotient (horizontal or vertical root, any depth) follows from:
  L1 [PROVED] eigen-coordinate calculus: J = prod_leaves alpha_leaf x prod_nodes H-factors (3.2); Lemma W.
  L2 [PROVED] rational end laws: Lemma S (delta, sigma), S3 (tau), BX1-BX4, BX4', T2; finite jet automaton (any fixed order).
  L3 [PROVED] Lemma Z: generic nested boxes have the rational end data.
  L4 [OPEN; CHECKED with R = 4] TWO-ENDED BOUND: for >= 2 non-scalar top-level factors, min(r_top, r_bot) <= R (an absolute R).
     Known exact cases: R = 1 for rational products (V2 vertical; horizontal mu = +-1, +-2).
  L5 [OPEN] WEAK-END EXCLUSION: at an end with r <= R (or offset != 0) the normalised expansion of F is not 1 + u + u^2 + 0u^3 + ..
     For rational bodies this is exactly what Section 2 proves (R = 1, orders <= 3); in general it needs channel potentials of
     nested boxes to order R + 2.  Caution: the per-box potential law l1(a) <= 0 FAILS for 4 + 39 depth-2 boxes (engineA), so L5
     must be a joint statement (box + partners), e.g. via the z-jets of 3.2.
  L6 [OPEN, alternative to L5] ONE-ENDED BOUND: max(r_top, r_bot) <= span A/2 + C for >= 2 non-scalar factors (eigen-contraction
     gives depth ~ min |m_i| at one end at a span cost ~ |m_i|).  L4 + L6 bound span A by 2(R + C), reducing Lemma Q to a finite check.
 Minimal next targets: (a) the delta = 0, r = 1 cases left open (V3(B): ~1,500 boxes) need third-order channel data: extend the
 per-box vector by l3 (the automaton already exists at K = 4) and add the lc-parity / degree-mod-3 constraints on the R-class count;
 (b) the sigma(B) = sigma* boxes and the exceptional n of H(B) need the tau-law (S3) at the two-ended level; (c) L4 at R = 2 for
 depth-1 children.
 The certificate generator (v3b3.py / h3b.py) applies verbatim to TWO or more non-rational boxes (sum their jets) - the natural route
 to 'Lemma Q for all depth-two arborescent quotients'.

## 6. Near misses and mechanisms
 Near misses (no gate passes both a_2 = 0 and J(zeta_10) = 1): triples span J 29 (depth 3, mu = +-4, a_2 = 87), 30 (depth (4,4),
 mu = 3, a_2 = -1); a_2 = 0 triples span 38; vertical depth-3 pairs span 38; depth-4 body-43 pairs span 57.
 MECHANISMS: M-V3 (sigma-law fixes the weak-end mismatch; second-order potentials BX4'/T2 forbid the Phi_3 pattern);
 M-S3 (tau = -1 for rational boxes, inherited by generic nested boxes: third-order two-ended ties need small z-order);
 M-imitation (deeper two-ended ties = a pair imitating one generic box's jets; accidental, does not propagate);
 M-count (two-ended depth grows ~ with the number of factors, the requirement grows ~ span A >= 4n).
 Reformulation worth keeping: J = 1 iff the product slope Q equals the pole q* up to c t^e Phi_3/(A w): a two-point Pade condition
 of defect zero, i.e. (A, t^-3N B) on the line (c t^e)(1,1) + Lambda (w_3, -w_1)/g of solutions of w_1 A + w_3 B' = c t^e Phi_3.

## Files
 jauto.py (rigorous jet automaton), jdata.py + jdata_*.pkl, jval.py (validation), v3lemmas.py (P1-P6, BX4', T2), taulaw.py (S3),
 v3b.py / v3b3.py / v3b_run.py + v3b_res.pkl (V3(B) generator v1), h3b.py / h3b_run.py + h3b_res.pkl (H(B) v1),
 gen2.py / gen2_run.py + gen2_res.pkl (FINAL generators with the delta-law; per-signature results), gen2_pairs.py,
 gen2_pairs_n.py (two non-rational boxes; logs gen2_pairs*.log),
 v3check.py (V3 skeleton check), libjets.py + libA_jets.pkl, tau1-5.py (positivity census), zjet.py + ztypes.py (eigen-coordinate),
 front.py, fr_build.py, fr_pairs.py, fr_pairs2.py, fr_triples.py, fr_eval3.py, chase.py; logs *.log, results fr_*.pkl.
 (fr_g43.pkl / fr_d2pos.pkl hold the frontier boxes with trees; vc.hw(tree) gives the explicit half-word.)
