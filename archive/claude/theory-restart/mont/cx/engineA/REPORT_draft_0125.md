# ENGINE A REPORT (cx lane; T1 arborescent horizontal outside Q-MONT, T2 vertical/dihedral) -- 17 Nov 2026
Folder: ~/jones-lanes/theory-restart/mont/cx/engineA/   Python: tools/venv/bin/python   Marks: PROVED / CHECKED(n) / CONJECTURE / GAP
STATUS: IN PROGRESS (skeleton written 00:13). No hit so far.

## 0. Plan
 (1) vc.py: exact 2-dim calculus in channel coordinates (a,b); validated against lp.J.
 (2) canonical tree enumeration outside proven-empty regions (depth >= 2 nests, general bodies, general special regions).
 (3) two-box closures by meet-in-the-middle (hash at a root of w_1 mod p), exact verification.
 (4) vertical closures (Theorem V) over exact windows.
 (5) near misses + mechanisms; exhausted regions.

## 1. Calculus and validation
 vc.py works in CHANNEL coordinates v = (a,b) (a = v_1, b = v_1 + (1-t^3) v_2): star = componentwise product, Y^k: b -> t^-3k b,
 X^mu = Moebius on the slope q = b/a:  a(X^mu v) = a(v) lambda_mu(q),  lambda_mu(q) = (w_1(mu) + w_3(mu) q)/Phi_3,
   w_1 = t + (1+t^2)(-t)^mu,  w_3 = (1+t^2)(1-(-t)^mu)   (eigenvectors (1,1) [eigenvalue 1] and (1+t^2,-t) [eigenvalue -t]).
 So for ANY tree, J = prod over internal nodes of lambda_{mu_N}(Q_N), Q_N = t^-3(int part) prod(child slopes)  (exact, PROVED
 from Theorem N/O: products multiply channels, X^mu is linear).  A HIT at a node with product (A,B) and twist mu needs
 w_1 A + w_3 B = u Phi_3, i.e. the product slope Q must equal the pole q*_mu = -w_1/w_3 of the closure functional up to
 u Phi_3/(A w_3): agreement orders r_inf + r_0 = span A + span w_1 - 2 at the two ends (PROVED, elementary).
 Dictionary tree -> halfword: rational word w -> B(w) (Y->y0, y->x0, X->r2.x1.().u1, x->r2.y1.().u1); node (m,children) ->
 r2.(y1)^m.B_1...B_n.u1; vertical closure s.l1.N.(x2)^a.u1.  Vectors normalised (a = 1 mod (t+1)^2) so the unit of Theorem O
 is asserted in every node evaluation.
 VALIDATION (validate.py, exact equality with lp.J of the explicit halfword): random trees depth 1-3, mixing rational leaves and
 the 50 general bodies, twists m in {+-1,+-2,+-3}, up to 3 children per node: CHECKED 38/38; vertical closures of the same bodies,
 a in {+-1,+-3}: CHECKED 38/38 (Theorem V); Theorem O unit t^(2m(1-eps)) asserted in every node: no failure.

## 2. Exact closure windows, library, enumerations
 LEMMA W (two-summand end coincidence; PROVED). If F = S1 + S2, span S1, span S2 >= 3, and F = u Phi_3 (u a unit), then
   top S1 = top S2 or bot S1 = bot S2 (if both differ, span F >= max span S_i >= 3).  Moreover the leading coefficients must cancel
   at a coincident end unless both ends coincide.
 COROLLARY (exact windows; PROVED). Horizontal closure of a product p=(A,B) with integral part N and twist mu:
   J Phi_3 = w_1(mu) A + w_3(mu) t^-3N B. For fixed mu, N in {N_top, N_bot} (2 values; they depend only on the class of mu:
   mu>=2, 1, -1, <=-2, since top/bot of w_1 - w_3 are constant on classes). For fixed N, J_mu = P_N + (-t)^mu Q_N with
   Q_N = (1+t^2)(A - B_N)/Phi_3 of span >= 2 (or 0: scalar state, J independent of mu), hence mu in {top P - top Q, bot P - bot Q}
   unless P_N is a monomial (brute force |mu| <= 40). So every two-parameter twist family (mu,N) has at most ~16 candidate
   members, computed from degrees.  This is much sharper than the BRIEF's N5 window and it is what eng.hclosures uses.
   Vertical closures: J Phi_3 = w_1(a) A + wV(a) t^-3N B, wV(a) = (-t)^a t + t^(3a-1) Phi_5: N in {N_top(a), N_bot(a)} for each odd a,
   and |a| <= max(span A, span B) + 8 (for larger |a| the low blocks t A and -t^(a+1-3N) B of the two summands separate from each
   other and from the high blocks, so F has >= 2 separated nonzero pieces: block-separation argument, PROVED sketch).
   CHECKED: candidate sets recover every unit found by brute force over |mu| <= 30, |N| <= 14 (80/80 random rational products,
   167 units, all recovered) and over odd |a| <= 31, |N| <= 14 for vertical closures (110/110 products, 308 units recovered).
 DATA CORRECTION (CHECKED): of the 50 bodies in general_boxes.json only 35 are distinct modulo Y, and 18 of those 35 are
   RATIONAL vectors (equal to rho(w) e_1 for a word of length <= 10; e.g. body 0 = l1.y0.y2.r3.y1.x2.u1.u1 has vector X Y e_1,
   the trefoil row). The remaining 17 (indices 3,4,6,9,12,26,27,30,33,35,39,41,43,44,45,47,48) are not reduced to an integral
   vector by greedy X/Y descent (which reduces 600/600 rational boxes): treated as the non-rational bodies.
   (A first pair test that still used the disguised rational bodies produced 27 unit J's; all 27 have det = Delta(2) = Delta(3) = 1
   and are unknot closures of rational configurations: sanity check of the pipeline, not hits.)
 Library (lib.py, all vectors normalised and canonical mod Y, i.e. d_top(q) = top b - top a in {0,1,2}):
   R(L)  rational boxes from words of length <= L (L=5: 40, 6: 98, 7: 238, 8: 576 distinct mod Y; integral ones dropped);
   L1    Montesinos boxes F_m(Y^N u_i * u_j), u in R(6), |m| <= 3, |N| <= 3: 174,620 distinct;
   G     17 non-rational general bodies; G-lib = G u F_m(Y^N g) u F_m(Y^N g * u), u in R(6), |m|,|N| <= 3: 58,068 distinct.
 E1 (single-child root = twisted closure X^mu Y^N of one box = general special region; and vertical closure of one box):
   R(8) sanity: 576 boxes, 1,728 horizontal + 9,578 vertical candidates, 142 units, all det = Delta(2) = Delta(3) = 1 (2-bridge
   unknots, as TH-2BR requires).
   L1 (174,620 Montesinos boxes F_m(Y^N u_i*u_j), u in R(6), |m|,|N| <= 3): 515,426 horizontal + 2,245,902 vertical candidate
   closures: 0 UNITS. CHECKED (complete for these boxes: every (mu,N) and every (a,N), by Lemma W).  Region: Montesinos knots
   with two odd rational tangles from R(6) and ONE GENERAL even tangle phi(infinity), phi = X^mu Y^N X^-m (general special
   region, outside Q-MONT), plus the vertical closures of the same boxes.
   G-lib (58,068 boxes; built with all 17 bodies incl. the 3 scalar ones, see below): 161,967 horizontal + 840,786 vertical: 0 UNITS.
 SCALAR BODIES (PROVED by inspection of the vectors): bodies 6, 35, 44 have b = +-t^k a (gcd(a,b) = a): their box state is a
   scalar times an integral state, i.e. a LOCAL KNOT on the arc (upstairs a swapped pair of summands). Every closure containing
   one factorises as (that scalar) x (closure with an integral box): this is Corollary S / T4 territory, not T1. They produced all
   of the deepest 'two-ended' near misses in the first runs (span J = 9, 15, 18 = their own spans): artefacts. Excluded from now on.
   The other 14 non-rational bodies have gcd(a,b) = 1.

## 2b. THE SLOPE-SPREAD (delta) LAW: a first-order obstruction to two-ended cancellation
 DEFINITION. delta(v) := span b(v) - span a(v) = d_top(q) - d_bot(q) (q = b/a). It is ADDITIVE under * and unchanged by Y^k.
 LEMMA D1 (PROVED). If the closure J Phi_3 = w_1 A + w t^-3N B ties at BOTH ends at first order (top degrees equal and bottom
   degrees equal), then delta(product) = delta* := span w_1 - span w. Horizontal: delta*(mu) = -1 (|mu| >= 2), -3 (mu = +-1).
   Vertical: delta*_V(a) = -a-1 (a >= 3), a-1 (a <= -3), -3 (a = +-1).  [spans of w_1, w_3, wV read off directly]
 LEMMA D2 (PROVED from BX1 + R2 of notie). Every non-integral rational box has delta = -1 (top-R <=> bottom-S); integral boxes
   have delta = 0. CHECKED 576/576 (R(8)).
 COROLLARIES (PROVED). (i) Horizontal necklace of n rational boxes ties at both ends only if -n in {-1,-3}: n = 1 (2-bridge) or
   n = 3 with mu = +-1 (Q-MONT's T3/B3 configuration; there the leading signs fail, Lemma N3).  This is a one-line reason for
   Q-MONT's 'ties are one-ended' (N3).  (ii) Vertical closure of n rational boxes with |a| >= 3 ties at both ends only if
   n = |a| + 1.  The earlier survey (nest p4_survey: products of 1-3 rational boxes, |a| >= 3) never satisfies this, which is why
   it found nothing; the RIGHT vertical knots are V_a(B_1 ... B_{|a|+1}).  (iii) In a two-child necklace a two-ended tie needs
   delta_1 + delta_2 in {-1,-3}: one child must have EVEN delta.
 Nested boxes break D2: F_m(p) has delta = -1 generically (X^-m contracts the slope to the two X-eigenslopes 1 and -t/(1+t^2),
   one at each end), but when p is close to the 'wrong' eigenslope at an end to more than |m| orders the end flips and delta
   moves by +-1. Distribution over L1 (R(5) pairs, |m|,|N| <= 3, 34k boxes): delta = -1: 30,700; -2: 2,022; -3: 332; 0: 190;
   +1: 554; +2: 258; ... (range -8..4). General bodies: delta in {-4,-3,-2,-1,1,4,7,8,9}.
 E2 (pairs at the root, MITM on slope series, library 50,138 non-rational boxes x (same + 576 rational)): the two-ended stage
   (4 orders of agreement at each end) produced 0 CANDIDATES (CHECKED). Deep one-ended stages and small-pair brute force: running.

## 2c. END-JET INVARIANTS: the second-order (sigma) law
 For a box with slope q = b/a write the end expansions q = lc t^d (1 + s1 t^-1 + ...) at t = inf and q = lc' t^d' (1 + s1' t + ...)
 at t = 0. Under * the degrees and s1 ADD, lc MULTIPLY; Y^k changes only d, d' (by -3k). A closure F = w_1 A + w t^-3N B ties at
 BOTH ends to order 2 iff (degrees) delta-law, (signs) prod lc = lc*, prod lc' = lc'*, and (second order) sum s1 = s1*, sum s1' = s1'*.
 LEMMA S (PROVED; CHECKED on all 576 boxes of R(8)): a non-integral rational box has one of exactly FOUR end types:  R_1/S_0: top (d=2,lc=-1,s1=+1) bot (d=3,lc=+1,s1=-1);  S_0/R_1: (0,+1,-1) / (1,-1,+1);
               R_0/S_j: (2,-1,0) / (3,+1,0);  S_j/R_0: (0,+1,0) / (1,-1,0).
   In particular sigma(u) := s1 + s1' = 0 for every rational box (and for integral boxes), and d' = d + 1, lc' = -lc.
   PROOF. Top data from notie BX1/BX2: R_c has r = t^-1(1 + c t^-1 + ...), so q = 1 + (1-t^3) r = -t^2 (1 + c t^-1 + ...);
   S_j has q = 1 - (-1)^j t^(-1-j) + ..., so (d,lc,s1) = (0,1,-[j=0]). Bottom data: by R2, q(u)(1/t) = t^-3 q(u'')(t) with
   u'' = u(-m_0-1, -m_1, ..., -m_{k-1}), so (d',lc',s1')(u) = (3 - d, lc, s1)(top of u''). The last exponent of u'' is -m_{k-1}
   and its previous state is R iff that of u is S (signs flipped; for k = 1 use init). From the BX2 table: u ends R_0 iff
   m_{k-1} = 1 after an R state, and then u'' ends S_j+1 (j+1 >= 1); u ends R_1 iff m_{k-1} >= 2 or (m_{k-1} = 1 after S/init),
   and then u'' ends S_0 (-m <= -2, or -1 after R). Symmetrically for S-tops. QED  (So delta = -1 and sigma = 0 are PROVED.)
 TARGETS: sigma* := s1* + s1'* of the closure pole: vertical |a| >= 3: sigma* = -1 (top s1* = -1, bottom 0, all a);
   horizontal: mu = +-1: -2; mu = +-2: +1; |mu| >= 3: 0.
 THEOREM V2 (PROVED, given Lemma S): no vertical closure V_a(B_1...B_n) of rational bodies with |a| >= 3 (any n, any integral
   part) ties at second order at both ends: sum sigma = 0 != -1. Consequently a unit would need one-ended agreement r >= Tot - 1
   (Tot = span A + span w_1(a) - 2 >= 4n + |a| - 1): DEEP one-ended cancellation through essentially all of J.
   Likewise a horizontal necklace of rational boxes with mu = +-1 or +-2 never ties to second order at both ends; with |mu| >= 3
   the sigma-obstruction vanishes but the delta-law forces n = 1 (2-bridge).  CHECKED by the type enumeration (e5_types.py):
   0 admissible type-multisets for a = +-3..+-11 (n = |a|+1), horizontal only n = 1 at |mu| >= 3.
 DATA: vertical closures of products of 4 boxes of R(6), a = +-3: 541,450 configurations tie at first order at both ends and ALL
   stop at exactly (r_top, r_bot) = (1,1) (CHECKED(541,450), e4_R6k0.pkl); for products of up to 6 boxes of R(5) at a = +-5 no
   configuration ties to second order at both ends (CHECKED). Both as predicted by Theorem V2.
 DESIGN RULE (the point of all this): a two-ended tie to order k needs the children's end-jets to sum to the target's at both
   ends. Rational boxes span only 4 jets at order 2 (sigma = 0); nested boxes (F_m) and general bodies carry sigma != 0 and
   delta != -1, and are the ONLY way to meet the targets. The searches below are organised by these jets.

## 3. Two-child roots (pairs) by meet-in-the-middle on slope series (e2b.py)
 Design (COMPLETE for units): a hit has r_top + r_bot = Tot = span A + span w_1 - 2. Stage S1 hashes two-ended keys (degree
 difference delta, top d mod 3, lc and Kt normalised coefficients at both ends, solving the integral part N from the top degree);
 stages S2/S3 hash one end with Kd terms; stage S4 brute-forces pairs with span a_1 + span a_2 <= Kt+Kd+1. Every candidate is
 evaluated exactly at all end-coincidence twists mu (Lemma W). Targets for |mu| > K+1 are the two X-eigenslopes 1 and
 -t/(1+t^2), so finitely many hash passes cover every mu.
 Library A: 50,138 non-rational boxes (Montesinos boxes F_m(Y^N u_i*u_j), u in R(5), |m|,|N| <= 3; the 14 general bodies;
 F_m(Y^N g); F_m(Y^N g*u)) against themselves and the 576 boxes of R(8). Pairs of two rational boxes are excluded (Q-MONT).
   S1, Kt = 3 (agreement >= 4 orders at BOTH ends): 0 candidates (CHECKED).
   S1, Kt = 1 (>= 2 orders at both ends): 234,351 candidate pairs; EVERY ONE has min(r_top, r_bot) = 2 exactly (CHECKED(234,351)):
     two-ended cancellation in two-child necklaces of this class reaches second order and never third. 0 units.
   S2 (deep top, 11 orders): 5.7 million candidates, almost all pairs of Montesinos boxes whose top slopes agree with the
     large-|mu| target -t/(1+t^2) (the -t eigenslope) to 11 orders. This is the X^-m contraction toward the eigenslopes, a
     structural ONE-ENDED effect, and an exact check of all of them (about 1 h) was not run. A complete run on a moderate library
     follows in 3b.
 MECHANISM (horizontal pairs): order 1 (degree + sign) at both ends needs delta_1 + delta_2 = delta* (odd) and is impossible
   for two generic boxes (delta = -1 each); it needs a nested box whose slope has FLIPPED to the other eigenslope at one end.
   Order 2 needs sigma_1 + sigma_2 = sigma* and occurs 234k times; order 3 never occurs.

## 3b. Complete pair runs, depth 2, triples, and the third-order wall
 COMPLETE pair run, library B (e2b_B.pkl + e2b_s4.py): A-side = 5,968 non-rational boxes [Montesinos F_m(Y^N u_i*u_j), u in
   R(4), |m|,|N| <= 2; the 14 general bodies; F_m(Y^N g); F_m(Y^N g*u)], partners = A-side + R(7) (238). All four stages:
   S1 (Kt=3) 0 cand; S2 deep top (Kd=10) 3,260; S3 deep bottom 85,544; S4 all pairs with span a1 + span a2 <= 15 (2,042 checks).
   0 UNITS. By the r_top + r_bot = Tot argument this is EXHAUSTIVE: every two-child necklace with one child in A and the other in
   A u R(7), every twist mu and every integral part N. (NOTE: the first S4 bound was 14; the correct bound is
   Kt + Kd + 2 = 15 (mu = +-1 has span w_1 = 0); S4 was rerun with 15 for both libraries: 0 units.)
 Big library A (50,138): S1 (Kt=3) 0 cand, S4 (bound 15, 2,991 checks) 0 units; deep stages in 6 parallel chunks (running).
 DEPTH 2 (e6_depth2.py): 129,966 depth-2 boxes F_m(Y^N c*u) and F_m(Y^N c) built on the 486 depth-1 boxes with non-generic jet
   (delta != -1 or sigma != 0) and the general bodies, u in R(4), |m|,|N| <= 2; pairs against (depth-2 u depth-1 u G u R(6)):
   second order at both ends: 143,704 configurations, ALL with two-ended depth exactly 2; third order at both ends: 0. 0 UNITS.
 TRIPLES (e7_triples.py): three-child roots with >= 1 non-generic child (L1 from R(4), |m|,|N| <= 2; G; R(6)): pair table of
   992,310 sub-products; second order at both ends: only 8 triples, all depth exactly 2. 0 UNITS. (Larger run running.)
 THIRD-ORDER WALL (e8_third.py / e8b.py): at a second-order two-ended tie of a pair let Delta_t = l2_top(Q) - l2_top(q*),
   Delta_b = l2_bot(Q) - l2_bot(q*) (third log-jet coefficients). Library A, |mu| <= 12: 255,834 second-order two-ended pairs,
   and Delta_t = Delta_b = 0 NEVER occurs (CHECKED(255,834)); one end matches at third order in 67,986 of them.
   mu = +-1 (231,910 ties) and mu = +-2 (54): Delta_t + Delta_b >= 2 always (a POSITIVITY law, the order-3 analogue of notie BX3;
   CONJECTURE for all depth-1 Montesinos boxes). |mu| >= 3 (about 23k ties): the sum ranges over [-4, 11] and is 0 in a few dozen
   cases, always as Delta_t = -Delta_b != 0: no positivity, but the two ends still never match together. Library B: 7,526 ties,
   all at mu = +-1, sums 2..7.
   So, organised by order, horizontal two-ended cancellation is blocked by: delta parity (order 1, PROVED for rational),
   sigma = 0 (order 2, PROVED for rational), third-order mismatch (order 3, CHECKED for depth <= 2 nested).

## 4. Vertical (dihedral) closures, Theorem V (e1_single.py, e4_vert.py)
 Single bodies: every library box (R(8), 174,620 L1 boxes, 58,068 G-lib boxes) under every candidate (a,N) of Lemma W:
   9,578 + 2,245,902 + 840,786 vertical candidates, 0 UNITS (CHECKED; complete for these bodies).
 Designed products (delta-law: two-ended ties need sum delta = -|a|-1; sigma-law: rational products can never tie to order 2):
   4 boxes of R(6), a = +-3: 541,450 first-order two-ended ties, ALL stop at (1,1) (CHECKED). [Theorem V2 explains it.]
   up to 6 boxes of R(5), a = +-5, order 2 at both ends: 0 (CHECKED). [Theorem V2]
   up to 4 factors from R(5) + 410 non-generic Montesinos boxes (delta != -1 or sigma != 0, from R(4) pairs, |m|,|N| <= 3) + the 14
   general bodies, a in {+-3,+-5,+-7,+-9}, order 2 at both ends: 1,452,019 configurations; 1,452,013 stop at two-ended depth 2,
   6 reach depth 3 (all contain general body g43 = l1.x1.y2.y0.y0.y0.y2.y2.y0.u1 and two Montesinos boxes, a = -5; span J about 60).
   0 UNITS (CHECKED).
 So for vertical inversions the sigma-law kills rational products at order 2, and non-rational factors buy at most ONE more order.
 COMPLETE SEARCH FOR VERTICAL CLOSURES OF RATIONAL PRODUCTS (e11_vdeep.py). By Theorem V2, min(r_top, r_bot) <= 1, so a unit has
   r >= Tot - 1 at the other end, with Tot = span A + span w_1(a) - 2 >= 4n + 2 (span a(u) >= 4 for non-integral rational u,
   span w_1(a) = |a| + 1 >= 4). A one-ended key with Kd = 4 (agreement >= 5 orders) at top or bottom therefore catches EVERY unit.
   Every odd |a| >= 3 inside the block-separation window (|a| <= 81 covers all products below), every integral part N:
     products of <= 4 boxes of R(7) (238 boxes): 354 candidates, 0 UNITS;  <= 6 boxes of R(5): 19,442 candidates, 0 UNITS;
     <= 8 boxes of R(4): 3,986 candidates, 0 UNITS;  <= 4 boxes of R(5): 0 candidates.   (CHECKED; complete given V2 + Lemma W)
   Sanity of the hash: with Kd = 1, 2, 3 the R(5)/n <= 4 run returns 415,648 / 7,862 / 2,416 candidates (agreement >= 2, 3, 4),
   so the single-end cancellation depth of vertical closures of rational products is at most 4 there (max 6 in the larger runs),
   against the >= 4n + 1 a unit would need.
 CONJECTURE V3 (vertical Lemma Q for rational boxes): V_a(Y^N u_1...u_n) with |a| >= 3 and non-integral rational u_i never has
   unit J. Proof route: V2 (PROVED) + a CLEAN-END lemma at the end with r <= 1. At a clean top dominated by S1 = w_1 A the first
   normalised coefficient would have to be sum l1(a_i) = 1, impossible since l1(a) = rho_a <= 0 (notie BX3); dominated by
   S2 = wV B it needs all l1(b_i) = 0 and sum l2(b_i) = 0, impossible since l1(b) = 0 forces l2(b) <= -1 (CHECKED on R(9), 1,392
   boxes; GAP: prove from the automaton). The mixed offsets 1 <= |top S1 - top S2| <= 4 and the r = 1 end leave a few small
   residual cases (n <= 2) needing third/fourth-order jets: GAP, but the complete searches above cover them for these pools.

## 5. Near misses, mechanisms, exhausted regions
 (pending)
