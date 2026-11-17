# ENGINE A REPORT (cx lane): T1 arborescent horizontal inversions outside Q-MONT, T2 vertical (dihedral) inversions
17 Nov 2026, Claude (engine A). Folder ~/jones-lanes/theory-restart/mont/cx/engineA/ . Python: tools/venv/bin/python (pure Python).
Marks: PROVED / CHECKED(n) / CONJECTURE / GAP.   STATUS: FINAL (01:45). NO HIT. (E11 vertical rational R(6) n <= 6 was
stopped unfinished: about 3M candidates at about 2 ms each; not claimed.)

## HEADLINE
No unit J in any region searched. More useful than the count: two-ended cancellation, which a unit needs, is blocked order by
order by end-jet invariants of the box slopes, and this tells you exactly which knots are worth building.
 * order 1: the slope spread delta = span b - span a is additive; a two-ended tie needs sum delta = delta* (odd: -1 or -3
   horizontal, -|a|-1 vertical). Every non-integral rational box has delta = -1 (PROVED).
 * order 2: sigma = s1_top + s1_bot (normalised second slope coefficients) is additive; EVERY rational box has sigma = 0
   (Lemma S, PROVED from notie BX2 + R2), while the vertical closure needs sigma* = -1: no vertical closure of rational bodies
   ties to order 2 at both ends (Theorem V2, PROVED). Same for horizontal mu = +-1, +-2.
 * order 3: among 255,834 second-order two-ended ties of two-child necklaces (depth-1 nested children) NONE ties at order 3
   (CHECKED); at mu = +-1, +-2 by a positivity law Delta_t + Delta_b >= 2. Depth-2 children and triples: same wall.
 * one-ended: deep one-ended agreement is STRUCTURAL (X^-m contracts slopes to the X-eigenslopes 1 and -t/(1+t^2)); for
   vertical closures of rational products the single-end cancellation never exceeds 6 orders, while a unit needs >= 4n+1.
 COMPLETE (exhaustive) new empty regions are listed in section 5. The strongest: every vertical closure V_a(Y^N u_1...u_n),
 |a| >= 3, of rational boxes from R(8) with n <= 4, R(5) with n <= 6, R(4) with n <= 8 (all a, all N); vertical closures of
 <= 4 factors mixing rational, non-generic Montesinos and general bodies; all two-child necklaces of library B; and all
 two-child necklaces built on the 100 + 292 'positive-potential' boxes (the only boxes that can beat the clean-end argument).
 WHERE TO LOOK NEXT (T1/T2): a unit needs either >= 3 orders of two-ended cancellation (never seen except 6 vertical cases with
 general body 43) or a clean end showing the Phi_3 pattern, which needs POSITIVE end potentials; those first appear at depth 2
 (4 + 39 boxes in 107k). Deeper nesting around such boxes is the only arborescent direction the jets leave open.

## 1. Calculus (vc.py) and validation
 Channel coordinates v = (a,b), a = v_1, b = v_1 + (1-t^3) v_2. Star = componentwise product; Y^k: b -> t^-3k b;
 X^mu (A,B) = alpha (1,1) + (-t)^mu beta (1+t^2,-t), alpha = (tA + (1+t^2)B)/Phi_3, beta = (A-B)/Phi_3.  On slopes q = b/a,
 X^mu is a Moebius map and a(X^mu v) = a(v) (w_1(mu) + w_3(mu) q)/Phi_3, w_1 = t + (1+t^2)(-t)^mu, w_3 = (1+t^2)(1-(-t)^mu).
 Hence for any tree J = prod over nodes of (w_1 + w_3 Q_node)/Phi_3 (Q_node = t^-3(int part) prod of child slopes), and a hit
 at the root needs w_1 A + w_3 t^-3N B = u Phi_3: the product slope must equal the pole q* = -w_1/w_3 up to u Phi_3/(A w_3),
 i.e. agreement orders r_top + r_bot = Tot := span A + span w_1 - 2 at the two ends (PROVED, elementary).
 Vertical (Theorem V): J Phi_3 = w_1(a) A + wV(a) t^-3N B, wV(a) = (-t)^a t + t^(3a-1) Phi_5 (same structure).
 Tree -> halfword dictionary: rational word w -> B(w) (Y->y0, y->x0, X->r2.x1.().u1, x->r2.y1.().u1); necklace node ->
 r2.(y1)^m.B_1...B_n.u1 (x1 if m<0); vertical closure s.l1.N.(x2)^a.u1. Vectors normalised (a = 1 mod (t+1)^2); the Theorem O
 unit t^(2m(1-eps)) is ASSERTED in every node evaluation (never failed).
 VALIDATION (validate.py): exact equality with lp.J of the explicit halfword, random trees of depth 1-3 mixing rational leaves and
 general bodies, |m| <= 3, <= 3 children: CHECKED 38/38; vertical closures of the same bodies, a in {+-1,+-3}: CHECKED 38/38.

## 2. Exact windows (eng.py)
 LEMMA W (PROVED). F = S1 + S2 with span S_i >= 3 and F = u Phi_3 forces top S1 = top S2 or bot S1 = bot S2, with cancelling
 leading coefficients at a coincident end unless both ends coincide.
 COROLLARY (PROVED). Horizontal closure with integral part N and twist mu: N in {N_top, N_bot} (depending only on the class of
 mu: >= 2, 1, -1, <= -2) and, for fixed N, J_mu = P_N + (-t)^mu Q_N with Q_N of span >= 2, so mu in {top P - top Q, bot P - bot Q}
 (brute force |mu| <= 40 if P_N is a monomial). So each (mu,N) twist family has <= ~16 candidates, computed from degrees (much
 sharper than the BRIEF's N5 window). Vertical: N in {N_top(a), N_bot(a)} for each odd a, |a| <= max(span A, span B) + 8
 (block separation). CHECKED against brute force: 80/80 horizontal products (167 units recovered), 110/110 vertical (308).

## 3. The obstruction hierarchy (end-jets)
 Notation: at t = inf, q = lc t^d (1 + s1 t^-1 + ...), log-jet (l1, l2, ...) of the normalised series; at t = 0 likewise.
 Degrees d, d' and log-jets ADD under *, lc multiply; Y^k only shifts d, d'.
 D1 (PROVED). A first-order tie at both ends forces delta(product) = delta* := span w_1 - span w (Lemma W at both ends).
    delta*(mu) = -1 (|mu| >= 2), -3 (mu = +-1); vertical delta*_V(a) = -|a|-1 (|a| >= 3).
 LEMMA S (PROVED; CHECKED 576/576). A non-integral rational box has one of FOUR end types:
    R_1/S_0: top (d,lc,s1) = (2,-1,+1), bottom (3,+1,-1);   S_0/R_1: (0,+1,-1) / (1,-1,+1);
    R_0/S_j: (2,-1,0) / (3,+1,0);                           S_j/R_0: (0,+1,0) / (1,-1,0).
    Proof: top data from BX1/BX2 (R_c: q = -t^2(1 + c t^-1 + ...), S_j: q = 1 - (-1)^j t^(-1-j) + ...); bottom data of u = top data
    of the mirror u'' = u(-m_0-1, -m_1, ..., -m_{k-1}) with d -> 3 - d (R2: q(u)(1/t) = t^-3 q(u'')(t)); u'' flips the signs of
    the trailing exponents, so by the BX2 table R_1 <-> S_0 and R_0 <-> S_{j>=1}. QED.
    Consequences: delta = -1 (D2) and sigma := s1 + s1' = 0 for every rational box.
 TARGET JETS: sigma*: vertical |a| >= 3: -1;  horizontal mu = +-1: -2, mu = +-2: +1, |mu| >= 3: 0.
 THEOREM V2 (PROVED). No vertical closure V_a(Y^N u_1...u_n), |a| >= 3, of non-integral rational bodies ties to order 2 at both
    ends (sum sigma = 0 != -1). Likewise for horizontal rational necklaces at mu = +-1, +-2 (and |mu| >= 3 forces n = 1 by D1).
    So in these classes a unit needs single-end agreement >= Tot - 1. This also gives a one-line reason for Q-MONT's N3
    (n rational boxes tie at both ends only if n in {1,3}; n = 3 needs mu = +-1 where sigma* = -2 != 0).
 DESIGN CONSEQUENCE. Rational boxes span only 4 second-order jets; nested boxes F_m(p) have delta = -1, sigma = 0 GENERICALLY
    (X^-m contracts the slope to the eigenslope 1 at one end and -t/(1+t^2) at the other) and become non-generic only when p is
    close to the 'wrong' eigenslope at an end. Distribution over 34,440 depth-1 boxes: 154 (delta, sigma, l2t+l2b) classes,
    delta in [-8,4], sigma in {-3,...,3} incl. halves/thirds (leading coefficients +-2, +-3). General bodies: delta in
    {-4,-3,-2,-1,1,4,7,8,9}. These non-generic boxes are the ONLY way to meet the targets, and every search below is organised
    by them.
 ORDER 3 (CHECKED). At second-order two-ended ties of pairs (library A, |mu| <= 12): 255,834 ties, Delta_t = Delta_b = 0 never
    (Delta = third log-jet mismatch); one end matches in 67,986. At mu = +-1 (231,910) and +-2 (54): Delta_t + Delta_b >= 2
    (POSITIVITY, CONJECTURE in general: order-3 analogue of notie BX3); at |mu| >= 3 the sum takes values in [-4, 11] and is 0 only
    as Delta_t = -Delta_b != 0.
 POTENTIAL LAW (CHECKED at depth <= 1; FAILS rarely at depth 2, section 7). l1 of the a-channel (= normalised second coefficient of J(s.B) at an extreme) is <= 0 at BOTH ends for
    all 1,392 rational boxes of R(9), all 14 general bodies and all 34,440 depth-1 nested boxes; l1 of the b-channel is <= 0 except
    for 100 boxes of library A (14 Montesinos, 86 built on general bodies). In the rational case a box with l1(b) = 0 has
    l2(b) <= -1. Clean-end consequence: a clean end dominated by S1 = w_1 A needs sum l1(a_i) = l1(Phi_3-pattern) - l1(w_1) > 0 when
    l1(w_1) = 0 (all mu except +-2 at one end): impossible.

## 4. Searches and results (all exact; every unit is verified by halfword, det and Delta(2), Delta(3))
 Library: R(L) rational boxes from words of length <= L, canonical mod Y (R(5) 40, R(6) 98, R(7) 238, R(8) 576, R(9) 1,392);
 Montesinos boxes F_m(Y^N u_i*u_j); the 14 genuine general bodies; F_m(Y^N g), F_m(Y^N g*u); depth-2 F_m(Y^N c*u), F_m(Y^N c).
 DATA CORRECTION: general_boxes.json has 35 distinct bodies mod Y, of which 18 have RATIONAL vectors (e.g. body 0 =
 l1.y0.y2.r3.y1.x2.u1.u1 has vector X Y e_1) and 3 (bodies 6, 35, 44) have SCALAR states b = +-t^k a (a local knot tied in the arc:
 Corollary S / T4 territory; every closure factorises). Only 14 are genuinely non-rational and non-scalar:
 3, 4, 9, 12, 26, 27, 30, 33, 39, 41, 43, 45, 47, 48 (gcd(a,b) = 1; greedy X/Y descent fails; it succeeds on 600/600 rational).
 The scalar bodies produced every deep 'two-ended' near miss of the first runs (span J = their own span): artefacts, excluded.
 E1 single-child roots (general special regions X^mu Y^N acting on one box; vertical closures of one box), all Lemma-W candidates:
   R(8): 576 boxes, 142 units, all det = Delta(2) = Delta(3) = 1 (2-bridge unknots: sanity).
   174,620 Montesinos boxes (u in R(6), |m|,|N| <= 3): 515,426 horizontal + 2,245,902 vertical candidates, 0 units.
   58,068 G-lib boxes: 161,967 horizontal + 840,786 vertical candidates, 0 units.
 E2 two-child roots (MITM on slope series: S1 two-ended key, S2/S3 deep one-ended keys, S4 small-pair brute force; complete by
   r_top + r_bot = Tot; S4 bound corrected from 14 to 15 = Kt + Kd + 2 and rerun):
   library B (5,968 non-rational boxes x (B u R(7))): S1 0, S2 3,260, S3 85,544, S4 2,042 checks: 0 units. COMPLETE.
   the 100 positive-potential boxes x (library A u R(8)): S1 0, S2 60, S3 20, S4 62: 0 units. COMPLETE.
   library A (50,138 non-rational x (A u R(8))): S1 (>= 4 orders both ends) 0; S1 at Kt = 2 (3 orders) 0; S1 at Kt = 1:
   234,351 ties, all depth exactly 2; S4 2,991 checks 0 units. Deep stages NOT finished (5.7M structural candidates; see M4).
 E6 depth-2 children (129,966 depth-2 boxes): second order both ends 143,704 ties, all depth 2; third order 0. 0 units.
 E7 triples with >= 1 non-generic child (pair tables of 0.99M and 3.29M sub-products): only 8 second-order two-ended ties, all
   depth 2. 0 units.
 E4/E9 vertical products: 4 boxes of R(6), a = +-3: 541,450 first-order two-ended ties, ALL stop at (1,1) (V2); mixed products
   (R(5) + 410 non-generic nested + general, <= 4 factors, |a| <= 9): 1,452,019 second-order two-ended ties, 1,452,013 at depth
   2 and 6 at depth 3; pool with 30,492 non-generic depth-2 boxes (<= 2 factors, |a| <= 11): 11,474 ties, all depth 2. 0 units.
 E11 COMPLETE vertical search for rational products (V2 => r >= Tot - 1 >= 4n + 1 at one end => one-ended key Kd = 4 is
   complete; all odd |a| >= 3 in the window, all N): R(7) n <= 4: 354 candidates; R(5) n <= 6: 19,442; R(4) n <= 8: 3,986;
   0 UNITS. Hash sanity: R(5) n <= 4 gives 415,648 / 7,862 / 2,416 / 0 candidates for agreement >= 2 / 3 / 4 / 5 orders.

## 5. Exhausted regions (new computationally empty regions; complete within the stated bounds)
 (a) Montesinos knots with two odd rational tangles from R(6) and ONE GENERAL even tangle phi(inf), phi = X^mu Y^N X^-m,
     |m|,|N| <= 3, any mu (horizontal inversion), and the vertical closures V_a of the same boxes, any a, N.
 (b) single-child twisted closures X^mu Y^N and vertical closures of: the 14 general bodies, F_m(Y^N g), F_m(Y^N g*u)
     (u in R(6), |m|,|N| <= 3): any mu, a, N.
 (c) two-child necklaces with one child in library B (Montesinos boxes from R(4), |m|,|N| <= 2; general bodies; F_m(Y^N g);
     F_m(Y^N g*u)) and the other in B u R(7): any mu, any N.
 (d) two-child necklaces with one child among the 100 positive-potential boxes and the other in library A u R(8): any mu, N.
 (e) vertical closures V_a(Y^N u_1...u_n), |a| >= 3, of rational boxes: R(8) n <= 4, R(7) n <= 4, R(5) n <= 6, R(4) n <= 8
     any a, any N.
 (e') vertical closures of products of <= 4 factors from R(5) + 410 non-generic Montesinos boxes + 14 general bodies (section 7).
 (d') two-child necklaces with one child among the 292 depth-2 positive-potential boxes, the other in library A u R(8).
 Two-ended-depth statements (not unit-completeness): (f) library A pairs, depth-2 pairs, triples: no third-order two-ended tie.

## 6. Near misses and mechanisms
 Gates on all stored near misses (several hundred per run): none has a_2 = 0 AND J(zeta_10) = 1. 26 of 800 pair near misses
 have a_2 = 0 but J(zeta_10) != 1; single-closure near misses of span 6 (e.g. s.r2.x1.x1.x1.r1.y2.y0.l2.y0.x3.x1.x1.x0.u3.u2.y0.u1.x0,
 span J 6 from span A 18, end depths (8,7)) pass J(zeta_10) = 1 but have a_2 = 5.
 Deepest two-ended cancellation found: (r_top, r_bot) = (4,3), vertical a = -5, product of two Montesinos boxes and general body
 43 = l1.x1.y2.y0.y0.y0.y2.y2.y0.u1 (jet delta = -4, sigma = -1), span J 56-65 (a_2 = 9, 39, -19, 14; J(zeta_10) != 1).
 MECHANISMS:
  M1 delta parity (order 1) and M2 sigma = 0 (order 2) for rational boxes: PROVED (section 3).
  M3 third-order wall for nested children: CHECKED (255,834 + 143,704 + 1.45M vertical); positivity at mu = +-1, +-2.
  M4 eigenslope contraction: F_m pushes slopes to the X-eigenslopes, so products of nested boxes agree with the large-|mu| poles
     to many orders at ONE end (5.7M pairs to 11 orders): cancellation is deep but one-ended; the other end is clean.
  M5 clean-end potential: l1(a) <= 0 at both ends in every class tested, so an S1-dominated clean end can never show the Phi_3
     pattern; S2-dominated clean ends need positive b-potential (only 100 boxes; searched completely in (d)).
  M6 local-knot (scalar) boxes give fake near misses; they belong to T4 (J_3 detection).
  Why the old vertical survey (nest p4_survey, products of 1-3 rational boxes) found nothing: D1 needs n = |a| + 1 boxes.

## 7. Open items / GAPs and late runs
 GAP 1: CONJECTURE V3 (vertical Lemma Q for rational boxes): V_a, |a| >= 3, of non-integral rational products is never flat.
   Route: V2 (PROVED) gives an end with r <= 1; a unit forces F's normalised expansion there to be the Phi_3 pattern (1,1,1,0,..).
   Clean end (r = 0) dominated by ONE summand (offset >= 5); the four (end, sign a) cases:
     top, a <= -3: l1(w_1) = l1(wV) = 0, so either domination needs a first-order sum = 1 > 0: impossible (rho_a, rho_b <= 0, BX3).
     top, a >= 3, S1 = w_1 A dominant: l1(w_1) = 0, needs sum rho_a = 1: impossible (BX3).
     top, a >= 3, S2 = wV B dominant: l(wV) = (1, 1/2, 1/3, 1/4), needs sum l1(b_i) = 0 and sum l2(b_i) = 0. By BX3 equality
       analysis l1(b) = rho_b = 0 only for R_1-top boxes with rho_a = -1 (Psi-preserving paths), and on those
       l2(b) <= -1 (CHECKED R(9): values -1, -2): impossible once 'R_1 & rho_a = -1 => l2(b) <= -1' is proved (a BX4-type lemma).
     bottom ends: the mirror (R2) exchanges a <-> -a and top <-> bottom, so they reduce to the top cases.
   Remaining: offsets 1 <= |top S1 - top S2| <= 4 and the r = 1 end (third/fourth-order jets, small n): covered computationally
   by E11 for the pools there, unproved in general.
 GAP 2: third-order positivity (M3) unproved; library A deep one-ended stage unfinished (structural, see M4).
 GAP 3: the 'potential law' l1(a) <= 0 at both ends for all boxes (CHECKED 35,846) is unexplained beyond rational boxes.
 LATE RUNS (01:25-):
  E11 vertical rational, R(8) n <= 4: 6,780 candidates, max single-end depth 7, 0 UNITS (COMPLETE, added to 5(e)).
  Lemma S re-CHECKED on R(10): 3,362 boxes, exactly the four types (985/985/696/696).
  POTENTIAL LAW FAILS AT DEPTH 2 (CHECKED): among 107,136 depth-2 boxes F_m(Y^N c*u) (c depth-1 or general, u in R(4)),
    l1(a) > 0 occurs for 4 boxes at the top and 4 at the bottom, l1(b) > 0 for 39 (top) and 10 (bottom). These boxes are exactly the
    ones that can evade the clean-end argument (M5); searched completely next.
  ORBIT DESCENT (descent.py; HEURISTIC, beam search over W = words in X^{+-1} Y^k, i.e. general special regions of arbitrary
    length): for the 14 general bodies, all body x body products and body x R(6) products (1,491 items), the smallest span of a
    closure J = a(W v) reached is 4 (single bodies 3, 4, 12, 41: trefoil-span closures), 6, 8, ...; products never go below 8.
    No unit. (On 30/30 rational boxes the same descent reaches the unknot, so it is not blind.)
  DEPTH-2 POSITIVE-POTENTIAL BOXES (292 boxes with l1(a) > 0 or l1(b) > 0 at an end): single closures 620 horizontal + 1,932
    vertical candidates, 0 units, no two-ended depth >= 3; pairs with every box of library A u R(8), all four stages: 0
    candidates at every stage, 0 UNITS (COMPLETE).
  MIXED VERTICAL PRODUCTS, COMPLETE (e11_mix): products of <= 4 factors from R(5) + the 410 non-generic Montesinos boxes (from
    R(4), |m|,|N| <= 3) + the 14 general bodies, every odd |a| >= 3, every N, one-ended key Kd = 6: 125,724 candidates, single-end
    depth <= 9, 0 UNITS. Completeness: a unit with two nontrivial factors has Tot >= 10; if Tot >= 13 one end has r >= 7 (caught);
    Tot <= 12 forces |a| <= 9 and then both ends would have r >= 4, excluded by the E4/E9 second-order runs (two-ended depth <= 3
    for this pool and |a| <= 9). Single factors: E1.

## 8. Files (this folder)
 vc.py (calculus, tree -> halfword), validate.py, eng.py (Lemma W candidate sets), lib.py (library; NONRAT list), scan.py (depths,
 gates), ser.py / jets.py (end series and log-jets), units.py / units2.py (unit verification), ratred.py (rationality descent),
 e1_single.py (E1), e2_pairs.py / e2b.py / e2b_s4.py / e2c_count.py (pairs), e4_vert.py (vertical MITM), e5_types.py (Lemma S
 types), e6_depth2.py, e7_triples.py, e8_third.py / e8b.py (third-order mismatch), e9_vert_d2.py, e10_cleanend.py (channel
 jets), e11_vdeep.py (complete vertical search), descent.py (orbit descent). Results: *.pkl with matching *.log.
 REPORT_draft_0125.md is an earlier draft (superseded by this file).
