# ENGINE ARB REPORT (round E): Lemma Q for arborescent quotients via end-jet closure
17 Nov 2026, Claude (engine ARB). Folder ~/jones-lanes/theory-restart/mont/cx/roundE/arb/ .  Python: /opt/homebrew/bin/python3
(scipy HiGHS for LPs; every certificate re-verified exactly in Fractions by lpgen's lpg.farkas).  Marks: PROVED / CHECKED(n) /
CONJECTURE / GAP / FALSE.   STATUS: FINAL (07:30).  NO HIT (0 units in 222,397 exact frontier products / 3,716,659 Lemma-W candidates).

## HEADLINE
 * THE CLOSURE IS NOT FINITE (PROVED, explicit family).  Arborescent boxes do NOT have a finite end-jet automaton (unlike rational
   boxes, refGen).  Mechanism M-LEAD: when the children's slopes cancel in degree and sign at an end (q_P ~ 1 or q_P ~ e2), the
   eigen-coordinate z_P = (q_P-1)/(q_P-e2) acquires an ADDITIVE log-jet sum as its leading coefficient, and the nest F_m moves it
   into the slope's leading coefficient or into any jet order: F_-1(Y^(-k/3) B(XY)^k) has top slope lc 1/(k+1) (k = 0 mod 6), and
   F_+1 of the same product is ELIGIBLE with l2(q) = -k.  Rules R1-R5 (star / Y^N / F_m in the eigen-coordinate, two clipping
   lemmas) are PROVED; the clipping threshold for F_m is |m| >= max z-order + K + 2 (= K+3 for generic products) and grows on
   special products.  Normalisation: class of F_m(P) = (additive data of P) + R(slope state of P, m); R is not finite either, but
   on each of finitely many generic pieces (end, m, deg q_P, lc q_P) it is a low-degree polynomial in the slope's log-jet sums
   (1,266 of 1,302 generic pieces affine, CHECKED); the special (cancellation) pieces have unbounded depth.  So the closure
   stabilises only as PARAMETRISED polynomial families: the LP over the multiplicity cone, not a finite class list, is the tool.
 * POSITIVE END POTENTIAL ALREADY AT DEPTH ONE (CHECKED exactly, 28 classes): e.g. F_-5(B(XY) B(xy)) has rho_a = +1 at the bottom,
   F_+-6(B(XXY)B(xxy)), F_+-7(B(XXXY)B(xxxy)) likewise; b-potential at |m| = 3, 4.  engineA's potential law (checked only for
   |m| <= 3) is FALSE at depth one.  Mechanism: RESONANCE -- mirror-type pairs have q ~ e2 to 3-5 orders at both ends and the
   twist |m| = z-order makes w = (-t)^-m z of order 0.
 * THEOREM ARB-2 (PROVED by exact uniform Farkas certificates, modulo the C1 framework as refereed by refGen, Theorem N/V and the
   halfword dictionary; certificates re-checked by independent code on the full family, 120/120): a CERTIFIED FAMILY S** of 10,877 order-2 classes -- top-300 + D36 + 10,541 eligible signatures of
   depth-one boxes F_m(Y^N u_1..u_n) (n = 2: R(5); n = 3: R(5); n = 4: R(4); 1 <= |m| <= 7, |N| <= 4) -- such that EVERY product of
   >= 2 factors whose non-rational factors have signatures in S** (ANY multiplicities, span a >= 3 each), with any number of
   non-integral rational boxes and any integral part, has NO flat horizontal (any mu != 0) and NO flat vertical (any odd a) closure.
 * THE RESIDUAL FRONTIER IS TWO-ENDED AND RESONANT (CHECKED): the uncertified depth-one classes (666 of n=2 after re-admission,
   3,460 of n=3/4, + 260 with sigma in Z/3, Z/4) are dominated by sigma = -1 (= sigma*_V: order-2 tie at both ends of a vertical
   closure) and delta >= 0 classes; 84% of the n=2 dangerous classes are (near-)resonant nests (gap <= 1) vs 30% of the certified
   ones; the certificates they violate are 'd=0 r=1' slices and ties (two-ended), only 68 violate offset cases alone.
 * RAISING K ON THE FRONTIER (PROVED per class, exact; negative control: the 16 genuine two-bridge units at mu = +-2 stay open,
   16/16): the 'd=0 r=1' case has the ORDER-3 EQUALITY d3 = -m [1/2 - Y2 + (1-X1)^2/2 - m^2/6] (derived here); with it and lpgen's
   tie rows (vertical ties with |a| >= 5 handled by slicing X1, cross-checked 1,200/1,200), 578 of the 636 dangerous classes B
   satisfy H3(B) ('B + any rational part' has no flat horizontal closure, any mu) and 622 satisfy V3(B) (no flat vertical
   closure, any odd |a| >= 3); 566 are closed for EVERY closure; for the 3,460 unsafe n=3/4 classes H3(B) holds for 3,424
   (1,940/1,974 and 1,484/1,486).  What survives order 3 is two-ended: ties where the tau-law holds
   (T3 possible: horizontal 392 subclass instances at |mu| = 2, 3, >= 4; vertical 24, all at |a| = 3; need order 4), T2-open ties
   (26 H, 12 V), 'd=0 r=1' open at the slice 1 - X1 = 1 (6, mu = +-2), and 20 offset 'd=-2 e=1' cases at mu = +-1 / |a| = 3.  (Uniform multiset version at order 3: not run.)
 * CLOSED (PROVED): (5a) vertical n = 0 pretzels P(a,q,a), |a| >= 3, short hand proof; (5b) lpgen's F1' tail (mB <= -31) by an exact
   linear bound with the right asymptotic slope (A* = 5, 5.5 < 6), and (5b') lpgen's two remaining F1' survivors B^3 u_1 u_2 at
   ORDER 4 (K = 4 automaton, exact) -- F1' is now EMPTY for all top-300 + d2pos multisets; (5c) two D36 boxes x any top-300
   multiset; (5d) THEOREM D36*: ANY multiset of top-300 + D36 boxes (any number of D36 boxes), >= 2 factors.
 * EXACT SEARCHES of every residual family (dangerous classes alone / squared / cubed / paired, LP-open points rounded, V-tie
   configurations, aligned positive potential up to B^7, ineligible boxes, the order-3 survivors): 222,397 products, 3,716,659
   Lemma-W candidates, 0 UNITS, 0 double-gate passers (a_2 = 0 and J(zeta_10) = 1); min span J 6 (single-child closure).

## 0. Log
- 05:21 read BRIEF, C1 REPORT, refGen NOTES, refV3 REPORT, lpgen REPORT + integrator note, engineA REPORT; code jauto, gen2, lpg.
- 05:25-05:35 items 5a (hand proof + exact check), 5c (uniform LP, integrator's suggestion), 5d (D36*), 5b (F1' tail).
- 05:35-06:00 rules + jet arithmetic (jbox.py, validated), non-finiteness family (mech.py), depth-one closure (gen1.py), LP over
  the new classes (arblp.py, run_arblp.py), greedy certified family (greedy.py), certificate column test (certtest2.py).
- 06:00-06:15 exact searches E-D1..E-D6, resonance anatomy, F1' survivors at order 4 (5b', f1b_o4.py), normalisation tests.
- 06:15-06:40 order 3 on the frontier (o3h, o3v + controls), independent re-check of ARB-2 certificates, report.
- 06:40-07:30 order 3 for the unsafe n=3/4 classes (H complete; V n=4 partial), exact searches E-O3, E-O3b.  At 07:30 the
  run o3_uv.py (PID 8578, mine) is still finishing V for n=4; it writes only o3_uv_n4.pkl/.log in this folder (final line
  'V3(B) closed: ...').

## 1. End-jet classes and their transformation rules (step 1)
 Box v = (a, b) in channel coordinates (a = J(s.B) channel, b = a q), defined up to units.  At an end (top: t -> oo; bottom = top of the
 mirror f(1/t)) write f = lc t^d (1 + s_1 u + s_2 u^2 + ..), log-jet (l_1, l_2, ..).  ORDER-K END CLASS: E_K(v) = (deg, lc, l_1..l_K) of
 a and of b at both ends.  The casework (C1/lpgen) uses exactly the order-2 SIGNATURE (top (l1a,l2a,l1b,l2b), bottom (same),
 sigma = s1_top(q) + s1_bot(q), delta = deg_top q - ord_bot q) plus eligibility (|lc b/lc a| = 1 at both ends, span a >= 1).
 Eigen-coordinate (C1 3.2): e2 = -t/(1+t^2), alpha = a (1+t^2)(q - e2)/Phi3, z = (q-1)/(q-e2); then a = alpha(1-z), b = alpha(1-e2 z).
 RULES (all PROVED: exact identities in Lambda^2):
  (R1) star product: E_K adds (degrees add, lc multiply, log-jets add) at each end; q multiplies.
  (R2) Y^N: b -> t^-3N b (deg_top q and ord_bot q drop by 3N); nothing else changes.
  (R3) nesting F_m = X^-m: alpha is X-invariant, z -> w := (-t)^-m z, so
         F_m(P) =. ( alpha_P (1 - w), alpha_P (1 - e2 w) ),   l(a') = l(a_P) + l(q_P - e2) + l((1+t^2)/Phi3) + l(1 - w),
         l(b') = l(a') + l(1 - e2 w) - l(1 - w),  q' = (1 - e2 w)/(1 - w).
       I.e. the class of a nested box = (ADDITIVE a-data of the product) + G(slope state of the product, m), where the slope state
       enters only through z_P (equivalently q_P) at each end.
  (R4) CLIPPING LEMMA for F_m (PROVED).  Let delta_t = deg_top z_P (highest exponent), o_b = ord_bot z_P (lowest exponent).  If
       m >= max(delta_t, o_b) + K + 2 then at the top w = O(u^(K+2)) (so a', b' have the K-jets of alpha_P) and at the bottom
       1/w = O(t^(K+2)) (so a' = -alpha_P w (1 - 1/w), b' = -alpha_P e2 w (1 - 1/(e2 w)), K-jets = those of alpha_P w, alpha_P e2 w,
       whose RELATIVE jets do not depend on m); symmetrically for m <= -(max(-delta_t, -o_b) + K + 2).  Hence the order-K signature
       of F_m(P) is independent of m beyond these thresholds (only the overall degree of a' moves = a unit).  For a GENERIC product
       (z of order one at both ends: delta_t in {0,1}, o_b in {-1,0}) the threshold is |m| >= K+3 = refGen's M for rational boxes;
       it GROWS with the z-order of special products.  CHECKED (r4chk.py, all R(5) n=2 products, |N| <= 4): m = +-7 vs +-6 differ on
       302/14,694 instances, and in every one of them R4's threshold exceeds 6 (0 violations).
  (R5) CLIPPING LEMMA for Y^N (PROVED).  If deg_top(t^-3N q_P) >= K+2 then z = 1 + O(u^(K+2)); if <= -(K+3) then z = (1/e2)(1+O(u^(K+2)));
       likewise at the bottom; so for |3N| >= |deg q_P| + K + 3 (both ends) the order-K signature of F_m(Y^N P) is N-independent.
 Implementation: jbox.py (precision-tracked truncated series at both ends, 8 orders kept per leaf, low precision FLAGGED, never
 guessed).  VALIDATION: signatures of 1,496 random depth-1/depth-2 boxes (R(5) children, |m| <= 6, |N| <= 3) equal the exact
 vector computation (C1's bdata) in 1,496/1,496; 4 flagged low-precision (jbox_val.py).  CHECKED(1,496).

## 2. Is the closure finite?  NO (PROVED) -- mechanism M-LEAD; normalisation
 THEOREM N-INF (PROVED, exact, mech.py).  Let u = rational box XY (R_1-type: top slope q = -t^-1 exp(u - u^2/2 + ..) ~ e2 = -t^-1(1 - u^2 + ..)).  For k = 0 mod 6
 the product P_k = Y^(-k/3) u^k has top slope q = 1 + k u + .. (degree and sign cancel), so z_P = k t^-1 + .., and
     F_-1(P_k): top slope leading coefficient 1/(k+1), lc a = k+1   (k = 6, 12, 18: 1/7, 1/13, 1/19 exactly);
     F_+1(P_k): top slope 1 + 0u - k u^2 + ..  (ELIGIBLE, l2(q) = -k);   F_+2(P_k): l3(q) = k.
 So already at depth ONE the set of order-0 classes (slope leading coefficients) and of ELIGIBLE order-2 signatures is infinite.
 MECHANISM M-LEAD: when the children's slope degrees and signs cancel at an end (q_P ~ 1: z small; or q_P ~ e2: z large), the
 leading coefficient of z_P is the first non-vanishing ADDITIVE log-jet sum L_j = sum_i l_j(q_i) (unbounded), and F_m moves it to
 any order (F_{+m}: into l_{j+m}(q')) or into the leading coefficient (F_{-j}: lc q' = 1/(1+L_j)).  For rational children (vc
 convention: R-ends q ~ e2 ~ -t^-1, S-ends q ~ 1) the cancellation at the top happens exactly when n_R = 0 mod 6 (q_P ~ 1, N = -n_R/3)
 or n_R = 1 mod 6 (q_P ~ e2, N = (1-n_R)/3); L_1 = #R_1 - #S_0, and deeper L_j when L_1 = 0 (S_j contribute at order j+1).
 Consequences: (i) no finite automaton of order-K end classes exists for arborescent boxes (unlike rational boxes, refGen);
 (ii) ineligible boxes (|lc b/lc a| != 1, e.g. lc 1/(k+1)) are generated in infinite families; C1/lpgen EXCLUDE them by hypothesis
 (eps = +-1).  For a unit closure, at the non-coincident (weak) end all children must have |lc a_i| = 1 (S1-dominated) or |lc b_i| = 1
 (S2-dominated), but eps = lc S2/lc S1 can then be any integer: GAP-ELIG (the casework must be extended to integer eps; section 7).
 NORMALISATION (what does stabilise).  By (R3) the class of F_m(Y^N P) at an end = (additive a-data of P) + R, where the RESIDUAL R
 (l1, l2 of a' minus those of a_P; deg, lc, l1, l2 of q') depends only on the slope state of P at that end and on m.
  (a) R itself is NOT finite (residual.py): R(5) n = 2: 720 generic + 1,248 special distinct residuals; n = 3 (2,500 multisets)
      adds 975 generic + 1,651 special -- because R depends on the log-jet sums (L1, L2) = (l1, l2)(q_P), which grow with n.
  (b) Pieces (end, m, deg q_P, lc q_P) are finitely many for eligible children (lc q_P = +-1, deg and m clipped by R4/R5), and on
      each piece R is a low-degree POLYNOMIAL in (L1, L2) (affine.py, R(5) n = 2, 3 and R(4) n = 4; 1,358 pieces):
        generic pieces: 1,266 AFFINE in (L1, L2), 36 not affine (quadratic terms in L1 from the expansion of log(q_P -+ 1) or
        log(q_P - e2) at deg q_P in {0, 2, -3}: polynomial of degree <= K), 4 with R not a function of (L1, L2);
        special pieces (q_P ~ 1 or ~ e2): 28 affine, 28 not, 28 not determined by (L1, L2) (they need L3, ...: the M-LEAD depth).
  So the closure 'stabilises after normalisation' only in the PARAMETRISED sense: finitely many generic pieces, each a polynomial
  family in the additive sums (CHECKED), plus the special (cancellation) pieces whose depth is unbounded (PROVED, N-INF).
  CONSEQUENCE for the method: the right object is an LP over parametrised families (multiplicity cone + piecewise polynomial
  nest maps, sliced where non-linear), not a finite class list; this is what sections 4-4.3 implement on enumerated families.

## 3. Closure computation at depth one (gen1.py; jet arithmetic of section 1)
 All F_m(Y^N u_1..u_n), multisets of n rational boxes, |N| <= 4, 1 <= |m| <= 7 (beyond C1's NRR library: n = 2, |m|,|N| <= 3).
  R(5), n = 2: 820 multisets, 103,320 boxes: 2,575 distinct order-2 signatures (2,127 eligible), 104 flagged low precision;
  clipping test m = +-7 vs +-6: 302/14,694 differ (special products, as predicted by R4).
 NEW (CHECKED exactly, pos1.py: jet signature == exact signature for all 28): POSITIVE END POTENTIAL ALREADY AT DEPTH ONE.
  28 eligible depth-one signatures have rho_a = +1 (8) or rho_b = +1 (20) at an end, e.g.
    F_-5(B(XY) B(xy)):  top (ra,la,rb,lb) = (-1,-1/2,-1,-3/2), bottom (1,-3/2,0,-1), sigma -1, delta -1   (a-potential at the bottom)
    F_+5(B(XY) B(xy)):  the mirror (a-potential at the top);   F_-4: bottom (0,-1,1,-3/2), sigma 1, delta 0 (b-potential)
    F_+-6(B(XXY) B(xxy)), F_+-7(B(XXXY) B(xxxy)): rho_a = +1, sigma -1.
  Mechanism: the product of a rational tangle with its mirror-type partner has q ~ e2 to 3-5 orders at BOTH ends (z of order
  -4..-6 in C1's ztypes convention), and F_m RESONATES when |m| equals that z-order (w = (-t)^-m z of order 0, 1 - w cancels):
  this is M-LEAD at both ends.  engineA's 'potential law l1(a) <= 0 at depth <= 1' was checked only for |m| <= 3; it is FALSE at
  depth one for |m| = 5..7 (a-potential) and |m| = 3,4 (b-potential).  So the positive-potential frontier (lpgen M-POT) is NOT a
  depth-2 phenomenon: it is reached at depth one by resonant twists on mirror-type products.
 Growth (eligible signatures): R(5) n=2: 2,127; R(5) n=3: 8,741 (8,078 new); R(4) n=4: 7,717 (4,971 new vs n<=3).  First-order
 skeletons (sigma, delta, rho_a, rho_b at both ends): 320 / 594 / 540, union 1,112 -- still growing.  NOT FINITE, as predicted by
 section 2 (the additive part grows with n).  Positive potential becomes RARER with more children: 28 (n=2), 2 (n=3), 0 (n=4, R(4))
 (resonance needs a mirror-type pair whose slopes agree with e2 to many orders at both ends; extra children spoil it).
 R(5) n=3: 1,446,480 boxes, 28 low-precision; clipping m=+-7 vs +-6 differs 1,056/206,626.  R(4) n=4: 488,376 boxes, 0 low precision,
 62/69,768 differ.

## 4. Farkas/LP closure over the reachable classes (step 3): THEOREMS ARB-1, ARB-2
 Driver arblp.py (lpgen's lpg/runner imported read-only): ANY class list (sigma, delta arbitrary), every closure family (V: 6 types
 = every odd |a| >= 3; H: 8 mu-classes = every mu != 0), every offset case, d=0 slices |m| < 15 on the attainable lattice (here
 (1/2)Z), exact LINEAR relaxations of the quadratic d=0 rows for |m| >= 15 (both signs, H and V; as in 5d), ties; constraint
 >= 1 non-rational box and >= 2 factors.  'd=0 r=0' is VACUOUS and skipped (PROVED, refGen remark (a)): offset 0 without
 cancellation means eps = +1, so lc F = 2 lc S1 is an even non-zero integer, never +-1.
 Sanity: on top-300 + D36 it reproduces D36* (511 sampled jobs, all closed).
 RUN 1 (arblp_n2): S = top-300 + D36 + 1,881 new eligible depth-one signatures (R(5), n = 2): 2,237/2,935 case-LPs OPEN; every
   open support contains new classes (130 distinct; positive-potential and delta >= 0 / sigma <= -1 classes dominate).
 GREEDY CERTIFIED FAMILY (greedy.py; remove every new class occurring in an open LP support, re-test, iterate; 16 rounds):
   THEOREM ARB-1 (PROVED; exact certificates; modulo the C1 framework as refereed by refGen, Theorem N/V and the halfword
   dictionary).  Let S* = the top-300 classes + the 36 D36 classes + 1,107 further ELIGIBLE order-2 signatures of depth-one boxes
   F_m(Y^N u_1 u_2) (u_i in R(5), 1 <= |m| <= 7, |N| <= 4; list = gen1_R5_n2.pkl minus greedy_n2.pkl['D']).  For every product
   Y^N (B_1 ... B_k u_1 ... u_n) with k >= 1 eligible boxes whose signatures lie in S* (ANY multiplicities; span a(B_j) >= 3, used
   only when n = 0 so that Lemma W and Tot >= 3 apply at mu = +-1), n >= 0 non-integral rational boxes and k + n >= 2, every N:
   no horizontal closure (any mu != 0) and no vertical closure (any odd a) is flat.
   (All 1,593 case-LPs closed over S*: 1,443 classes.)
 DANGEROUS SET D (774 of the 1,881 new n=2 signatures; greedy_n2.pkl): it contains ALL 191 eligible signatures with sigma = -1
   (= sigma*_V: a single such box ties to order 2 at BOTH ends of a vertical closure -- C1's known open type), 310 with delta >= 0
   (the delta-law no longer caps the number of factors in two-ended (d=0) configurations), 263 with sigma < 0, 19 of the 28
   positive-potential ones.  |m| of representatives: D 1:219 2:174 3:156 4:80 5:87 6:42 7:16.
   Open case types before greedy: 'd=0 r=1' slices 1,276, ties 9, 'big' r1 88, offsets d=+-1, +-2, <=-3 (e=+-1) 108 -- i.e. the
   frontier is TWO-ENDED (d=0, ties) exactly as lpgen's GAP-A, now reached at depth one.
 ANATOMY OF D = RESONANCE (resonance.py, CHECKED on all 2,127 eligible n=2 classes).  For F_m(P), P = Y^N u_1 u_2, let
   w = (-t)^-m z_P; resonance gap g = min(|deg_top w|, |ord_bot w|) (g = 0: the twist brings z_P exactly to order 0 at an end,
   so 1 - w can cancel = the inner closure of P at twist -m is near a unit).
     D (774):      g = 0: 343 (44%), g = 1: 304, g = 2: 108, g >= 3: 19;   special product (z_P not of order one at an end): 657 (85%)
     S* (1,353):   g = 0: 119 (9%),  g = 1: 287, g = 2: 483, g >= 3: 464;   special: 752 (56%)
   So the order-2 frontier at depth one is made of (near-)RESONANT nests: twists |m| within one of the z-order of the product at
   an end.  Off resonance (g >= 2) 947 of 1,074 classes (88%) are certified, near resonance (g <= 1) only 406 of 1,053 (39%).

### 4.2 Extension to 3 and 4 rational children: certificate column test (certtest2.py)
 For every one of the 1,593 case-LPs, an exact Farkas certificate y over S* (ARB-1) is recomputed; a candidate class with column c
 is compatible iff c.y >= 0 (the extended LP stays infeasible with the SAME certificate).  A class compatible with ALL 1,593
 certificates can be added to S* with any multiplicity, and all such classes simultaneously.  Candidates: D (774) + every new
 eligible signature with sigma in Z/2 from R(5) n=3 and R(4) n=4 (12,786): 13,560.  Every job had a certificate over S*.
 RESULT: SAFE 9,434 (108 of D re-admitted, 5,960 of n=3, 3,366 of n=4); UNSAFE 4,126 (666 of D, 1,974 n=3, 1,486 n=4).
 INDEPENDENT RE-CHECK (verify_arb2.py): 120 random case-LPs rebuilt over the FULL S** (10,877 classes); the exact Farkas vector
 found over S* satisfies A^T y >= 0 on EVERY column and b'.y < 0, checked by separate code: 120/120 OK.
 THEOREM ARB-2 (PROVED, same hypotheses as ARB-1): ARB-1 holds with S* replaced by S** = S* + the 9,434 safe signatures
 (10,877 order-2 classes in all: top-300, D36 and 10,541 eligible depth-one signatures with 2-4 rational children, |m| <= 7,
 |N| <= 4).  Certified = any multiset of boxes with these signatures, any rational part, >= 2 factors, every mu, every odd a.
 (Classes with sigma in Z/3 or Z/4 (260 of n=3/4) were not tested: uncertified.)
 Anatomy of the 4,126 unsafe classes: sigma = -1: 2,073; sigma < 0: 2,866; delta >= 0: 972; positive potential: 20.  Violated
 certificate families: d=0 r=1 slices (426,544 violations), ties (25,740), big r1 (12,492), offsets (~11,000).  Per class:
 (d0, tie) 2,722; (big, d0, tie) 485; d0 only 344; (big, d0, off, tie) 318; offsets only 68.  => The uncertified frontier is
 TWO-ENDED (offset-0 weak end with exactly one cancelled order, or a second-order tie at both ends), as for lpgen's GAP-A.

### 4.3 Raising K for the residual classes: ORDER 3 for the two-ended cases (o3h.py)  [single dangerous box + rational part]
 'd=0 r=1' (weak end: offset 0, exactly one cancelled order, m = mB != 0).  DERIVATION (PROVED): F = c t^D s2 (e^Delta - 1),
 Delta = log s1 - log s2 = sum d_k u^k, d1 = X1 - X2 = -m.  The Phi_3 pattern 1 + u + u^2 + 0u^3 for F/(c d1 t^(D-1)) gives
   order 1: X2 + d2/d1 + d1/2 = 1   (= C1's 'd=0 r=1' row, re-derived),
   order 2: Y2 + e2 - e1^2/2 = 1/2,  e1 = 1 - X2,  e2 = d3/d1 + d2 + d1^2/6,   i.e.
            d3 = -m [ 1/2 - Y2 + (1 - X1)^2/2 - m^2/6 ]        (d3 = l3(s1) - l3(s2), Y2 = l2(s2), X1 = l1(s1)),
 an EQUALITY that is affine in the rational sums once X1 is fixed: sliced for |1 - X1| < 6, exact linear relaxation
 (1-X1)^2/2 >= 3|1-X1| beyond.  Ties (mB = 0): lpgen's T3 (tau-law vs delta-law) / T2 (D3 = D2 (1 - X1)) rows, every mu.
 NEGATIVE CONTROL (o3h_ctl.py): the 16 genuine two-bridge-unknot boxes of R(6) at mu = +-2 (refGen: they live in 'd=0 r=1') are
 left OPEN at order 3 at exactly one end, at the slice 1 - X1 = 1, and closed at the other end: the equality is satisfied by the
 true units (CHECKED 16/16) -- the cut is not vacuous and not wrong in sign.

 RESULTS (o3h.py, 22,260 jobs = 636 dangerous n=2 classes with order-3 data x their order-3 subclasses x 8 mu-classes (+ mu = +-5 at
 order 3) x weak end; ONE dangerous box B + n rational boxes, n pinned by the delta-law):
   'd=0 r=1': closed at order 2 (single box) 14,460; closed by the ORDER-3 EQUALITY 462; open 6 (all at the slice 1 - X1 = 1).
   ties: T3 impossible and T2 closed 2,130; T3 POSSIBLE (tau-law holds: two-ended order-3 tie, needs order 4) 392; T2 open 26.
 Combined with C1's per-box generator gen2.proveH at order 2 for the one-ended cases (hb_o3.py): THEOREM H3(B) (PROVED, exact):
   for 578 of the 636 dangerous classes, B + ANY n >= 1 non-integral rational boxes, any N: NO horizontal closure (any mu) is flat.
   Still open for 58: offset 'd=-2 e=1' at mu = +-1 (18; one-ended, the case where two-bridge units live for rational B),
   two-ended ties with T3 possible (at |mu| = 2, 3, >= 4), F1 'd=-1 e=-1' at mu = +-1 (2; lpgen's F1 order-3 cut applies).
 Vertical (vb_o2.py, gen2.proveV at order 2): 401 of the 636 are V-closed at order 2; open: sigma(B) = sigma*_V (207, the V tie),
   'd=0 r=1' (78), 'd=-2 e=1' (2).  => 361 dangerous classes are now closed for EVERY closure of 'B + any rational part'
   (H at order 3, V at order 2).  Vertical order 3 (o3v.py): offsets at order 2, 'd=0 r=1' with the order-3 equality (n by the
   vertical delta-law), and the V tie per weak end, sign of a and |a| = 3 (n = delta + 4 pinned, lpgen rows) or |a| >= 5 (n >=
   delta + 6 free: X1 is sliced instead of D2, so D3 = D2 (1 - X1) with D2 = tau*_V - tau(B) + n is LINEAR in n; relaxation
   |D3| >= 6|D2| beyond the window; tau*_V = -1/2 (|a| = 3), +1/2 (|a| >= 5), closure jets computed from eng.w1/eng.wV).
   CROSS-CHECK (o3v_xchk.py): the sliced formulation with |a| = 3 data and n pinned agrees with the pinned rows in 1,200/1,200
   instances (1,142 closed/closed, 2 open/open, 24 T3-possible, 32 n < 1).
   RESULT (o3v.py, 1,113 order-3 subclasses of the 636 classes): THEOREM V3(B) (PROVED, exact): for 622 of the 636 dangerous
   classes, B + ANY n >= 1 non-integral rational boxes, any N: NO vertical closure (any odd |a| >= 3) is flat.  Open: ties with
   T3 possible (24 subclass instances), T2-open ties (12), offset 'd=-2 e=1' at |a| = 3 (2).  With H3(B): 566 of the 636
   dangerous classes are closed for EVERY closure of 'B + any rational part' (k = 1).
   EXTENSION to the UNSAFE n=3/4 classes (gen1k3u.py: order-3 subclasses of the unsafe classes; o3_u.py = o3h + gen2.proveH;
   o3_uv.py = o3v):  n = 4 (R(4)): 1,486 unsafe classes, 5,049 order-3 subclasses: H3(B) holds for 1,484 of 1,486;
   n = 3 (R(5)): 1,974 unsafe classes, 8,470 order-3 subclasses: H3(B) holds for 1,940 of 1,974.
   VERTICAL for these (o3_uv.py, n = 4 only; still running at the deadline, partial result from o3_uv_n4.pkl via uv_partial.py):
   2,500 of 5,049 subclasses processed, 517 of 1,486 classes complete: V3(B) holds for 512 of them (all 512 also H3).  n = 3
   vertical not run.
   Not done: the uniform multiset version (dangerous boxes together with S** multisets) at order 3.

## 5. The specific open items (step 4)
### 5a. Vertical n = 0 closures (pretzels P(a,q,a), vertical inversion): PROVED (short hand proof)
 Body = integral part only, v = Y^N e_1, so A = 1, B = t^-3N and (Theorem V) J Phi_3 =. F := w_1(a) + t^-3N wV(a),
   w_1(a) = t + (1+t^2)(-t)^a = t - t^a - t^(a+2),   wV(a) = (-t)^a t + t^(3a-1) Phi_5 = -t^(a+1) + t^(3a-1) + ... + t^(3a+3)   (a odd).
 CLAIM: for odd |a| >= 3 and every N, F is not +-t^e Phi_3 (so J is not a unit).
 PROOF. Put M = -3N.  F is a signed sum of 9 monomials with coefficients +-1: POSITIVE t^1 and the block t^(3a-1+M) .. t^(3a+3+M)
 (5 consecutive degrees), NEGATIVE t^a, t^(a+2), t^(a+1+M).  F(1) = 6 - 3 = 3, so F = -t^e Phi_3 is impossible and F = t^e Phi_3
 needs every coefficient of F in {0, 1}: each of the three negative monomials must sit at a degree carrying a positive one.
 (i) t^(a+1+M) cannot sit in the block: a+1+M in [3a-1+M, 3a+3+M] <=> -1 <= a <= 1.  So a+1+M = 1, i.e. M = -a, and the block is
     t^(2a-1) .. t^(2a+3), while degree 1 is now used up by t^(a+1+M) (if the block also covers degree 1 it can absorb one more, but
     see (ii), which only uses the block's position).
 (ii) a >= 3: a < 2a-1, so t^a is below the block and must sit at degree 1: a = 1, contradiction.
      a <= -3: a+2 > 2a+3, so t^(a+2) is above the block and must sit at degree 1: a = -1, contradiction.  []
 CHECKED exactly (pretzel_n0.py): odd |a| <= 201, |N| <= 300 (121,402 closures): units only (a,N) = (1,0), (1,1), (-1,0), (-1,-1)
 (two-bridge unknots; excluded).  Together with refV3's V3 (n >= 1, |a| >= 3) this closes refV3's GAP G3 / R2: every
 vertical closure of a Montesinos-type body (any n >= 0 non-integral rational tangles, any integral part, odd |a| >= 3) is
 non-flat (modulo Theorem V's skein dictionary, as for all vertical results).

### 5b. lpgen's F1' tail (>= 15 aligned a-potential boxes at mu = +-2, mB <= -31): CLOSED (PROVED, exact)
 (f1b_tail.py, f1b_tail2.py; class set = lpgen's 3,735 order-3 subclasses of top-300 + d2pos; F1' = 'd=1 e=-1' at H mu=+2 top and
 its mirror H mu=-2 bottom; order-3 EQUALITY (lpgen 5.9, PROVED): LHS' := l3(s1) - l2(s2) - (p3 - q2) = mB^2/2 - 4/3 - p3 + q2.)
 * Why lpgen's tail stayed open: f1b_large maximised LHS' + A|mB| (a sign slip, harmless where bounded) with A = 4, below the
   true asymptotic slope.  Recession-cone LP (f1b_tail.py): sup dLHS'/d|mB| over rays of the order-2 F1' region = A* = 5 (mu=+2
   top; ray = d2_497 boxes + rational flow) and 5.5 (mu=-2 bottom; ray = top198 + d2_460); NO ray with d|mB| = 0 raises LHS'.
 * With A = 6 > A*: max(LHS' - 6|mB|) on the order-2 region with |mB| >= 31 is certified EXACTLY (Farkas) below b' = -42 (mu=+2 top)
   and b' = -29 (mu=-2 bottom).  The equality needs mB^2/2 - 7/3 = LHS' < 6|mB| + b', i.e. |mB|^2 - 12|mB| - 2(b' + 7/3) < 0, whose
   reduced discriminant A^2 + 2(b' + 7/3) is NEGATIVE (-130/3 and -52/3): no |mB| at all.
   => F1' is EMPTY for every multiset of top-300 + d2pos boxes with |mB| >= 31.  Together with lpgen 5.9 (|mB| <= 30 by slices),
   the only F1' survivors are lpgen's two integer configurations B^3 u_1 u_2 (B in the order-3 subclass of box 50216 at mu = +2,
   mirror box 50139 at mu = -2, exactly n = 2 rational boxes), searched exactly by lpgen for u_i in R(5)/R(6) (0 units); they are
   closed for ALL rational u_1, u_2 at order 4 in 5b'.

### 5b'. lpgen's two F1' SURVIVORS closed at ORDER 4 (PROVED, exact; f1b_o4.py)
 Configurations (lpgen 5.9): B^3 u_1..u_n with B = box 50216 at H mu = +2 (weak top) and the mirror B = box 50139 at mu = -2
 (weak bottom); offset +1, eps = -1, mB = -7 (3 x sigma -2 against sigma* = +1).  The Phi_3 pattern f = s1 - u s2 = 1 + u + u^2
 + 0u^3 + 0u^4 gives, with log-jets (X, Y, Z, W) of orders 1-4 and series coefficients s_k:
   [u^1] X1 = 2;  sigma-law X2 = X1 + mB;  [u^2] Y1 = X2 - 1;  [u^3] Z1 - Y2 = mB^2/2 - 4/3 (lpgen);
   [u^4] (NEW) W1 - Z2 + (X1 - X2) Y2 = X2^3/6 - X1 (mB^2/2 - 4/3) - Y1^2/2 - X1^2 Y1/2 - X1^4/24.
 Rational part EXACT on the K = 4 jet automaton (35 states; 174 distinct edge log-jets; terminal q log-jets; refGen: the automaton
 is PROVED for all rational boxes at every fixed K, bottom data = top data of mirrors), n >= 0 FREE.
 CONTROL: orders 1-3 alone are FEASIBLE with n = 2 (reproduces lpgen's survivor exactly).  With [u^4] added: INFEASIBLE, exact
 Farkas certificate, for BOTH configurations.  => Together with section 5b (tail) and lpgen 5.9 (slices |mB| <= 30, whose only
 integer survivors were these two): F1' ('d=1 e=-1') is EMPTY for every multiset of top-300 + d2pos boxes and any rational part.
 (So lpgen's frontier item (ii) is closed; what remains of lpgen's frontier is the two-ended family GAP-A, item (i).)

### 5c. Two depth-2 positive-potential boxes from the D36 classes x ANY top-300 multiset x ANY rational part: PROVED
 (d2two.py; the integrator's suggested uniform LP; replaces the killed d2fix2.)  S = top-300 classes + the 36 D36 classes (the
 d2pos classes closed singly), D36 multiplicities are LP variables with sum EXACTLY 2 (any two boxes, equal or different classes),
 top-300 multiplicities and n >= 0 free.  Cases already closed in lpgen's uniform top-300+d2pos run stay closed (sub-family);
 re-run: the 125 cases open there + all d=0 slices 9 <= |m| <= 14 (V) and 9 <= |m| <= 12 (H): 525 case-LPs, ALL CLOSED with exact
 verified Farkas certificates (6 s).  Slice completeness:  H: the delta-law n = delta.k + off >= 0 with every delta_j <= -1 caps
 the box count (2 D36 + <= 1 top at mu = +-1, impossible at |mu| >= 2), so |mB| <= 11;  V: mB = sigma.k + 1 >= 5 (all sigma >= 0)
 and for mB >= 15 the two-exceptional phi bound (d2two_phi.py): ordinary boxes (rational, top-300) have phi = rho_a + rho_q/2 <=
 -1/2 and |lam| <= 2, D36 boxes phi <= 0, |lam| <= 12; mB <= N_top + 9 gives N_o >= mB - 9, and
   r=1:  N_o (1/2 - 2/mB) >= 11/5 > max over V classes of [2 phi_max - c0 + (|p2-q2| + 2 lam_max)/15] = 17/15;   r=0: sum phi <= 0 < c0.
 NEGATIVE CONTROL (d2two_ctl.py): with all 60 d2pos classes (sum 2) 43 cases are OPEN (the machinery is not vacuous); with three
 D36 boxes (sum 3): 525/525 closed.
 THEOREM D2x2 (PROVED, modulo the C1 framework as refereed by refGen): for any two boxes B1, B2 whose order-2 signatures lie in the
 36 D36 classes, any multiset of boxes with top-300 signatures and any n >= 0 non-integral rational boxes, any N: no horizontal
 (any mu) and no vertical (any odd a) closure of Y^N (B1 B2 ...) is flat.

### 5d. THEOREM D36* (PROVED; d36star.py, d36star2.py): ANY multiset of top-300 u D36 boxes (any number of D36 boxes)
 All C1/lpgen case-LPs over S = top-300 + D36 with free multiplicities (kmin = 1), d=0 slices |m| <= 14 (H: the delta-law caps the
 box count at 3, all delta_j <= -1, so |mB| <= 14), and for the vertical d=0 cases with mB >= 15 (mB <= -15 is impossible: every
 sigma_j >= 0, sigma*_V = -1) an exact LINEAR relaxation of the quadratic rows:
   r=1:  sum phi - c0 = X/mB, X := p2 - q2 - LAM, mB >= 15   =>  (X >= 0, 0 <= sum phi - c0 <= X/15)  or  (X <= 0, X/15 <= sum phi - c0 <= 0);
   r=0:  sum phi = c0  and  (La+Lb)_all + p2 + q2 = 1 - mB^2/4 <= 1 - 15 mB/4
 (phi = rho_a + rho_q/2, LAM = sum l2(q) over ALL boxes, c0 = 1 - (p1+q1)/2; derivation: m RA + LAM = m - m^2/2 + p2 - q2 - m p1 and
 RQ = p1 - q1 + m from C1's rows).  1,501 case-LPs: 1,487 closed with exact certificates; the 14 open ones all have total mass
 sum k + n = 1 (single-child closures, engineA E1, known open in M300); with the constraint sum k + n >= 2 all 14 close (d36star2).
 THEOREM D36*: every product of >= 2 factors (non-rational factors with signatures in top-300 u D36, ANY multiplicities, plus any
 n >= 0 non-integral rational boxes), any N: no flat horizontal (any mu) or vertical (any odd a) closure.  This contains M300, D36
 and 5c, and closes all multisets built from the 36 b-potential depth-2 classes.

## 6. Exact searches (Lemma W windows via engineA eng.hclosures/vclosures, every mu and odd a; gates a_2 = 0, J(zeta_10) = 1)
 E-D1 (ex_d1.py): the 130 depth-one classes occurring in LP-open supports of the first uniform run (section 4): B^j u_1..u_n
   (j = 1: n = 0, 1, 2 over R(4); j = 2: n = 0, 1; j = 3: n = 0) and pairs B B' (30 most frequent) with n = 0, 1:
   29,625 products, 426,107 Lemma-W candidates: 0 UNITS, 0 double-gate passers, min span J 6 (a single-child closure).
 E-D2 (ex_d2.py): integer roundings of the LP-OPEN points of run 1 ('d=0 r=0' excluded): support multiplicities floor/ceil
   (<= 8 non-rational boxes; representatives: gen1 trees / library boxes), n in {round(n), +-1} rational boxes from R(4)
   (all for n <= 1, 40 random for n = 2): 20,000 products, 479,510 candidates: 0 UNITS, 0 double-gate passers, min span J 10.
 E-D3 (ex_d3.py): the V-TIE configurations of the 40 most frequent dangerous sigma = -1 classes (n pinned by the delta-law,
   n = delta(B) + |a| + 1, |a| = 3, 5; all multisets of R(4) for n <= 3, 150 random otherwise): 29,800 products, 532,179
   candidates: 0 UNITS, 0 double-gate passers, min span J 17.
 E-D4 (ex_d4.py): the 80 most frequent UNSAFE n=3/n=4 classes: B u, B u u' (R(4)), B^2, B^2 u, and V-tie configurations
   (sigma = -1: n = delta + 4, 120 random): 16,640 products, 301,023 candidates: 0 UNITS, 0 double-gate passers, min span J 21.
 E-D5 (ex_d5.py): ALIGNED POSITIVE POTENTIAL at high multiplicity (LP-open points use 4-7 copies): all 28 positive-potential n=2
   classes, B^j (j = 4..7) with n = 0, 1 (R(4)), and B^j B'^j' (j + j' = 4..6) for the 10 most frequent pairs: 2,024 products,
   67,299 candidates: 0 UNITS, 0 double-gate passers, min span J 32.
 E-D6 (ex_d6.py, GAP-ELIG): the 120 most frequent INELIGIBLE n=2 signatures (448 such signatures, 1,329 of 103,216 boxes):
   B, B u, B u u', B^2, B^2 u, B^3: 20,520 products, 155,320 candidates: 0 UNITS, 0 double-gate passers, min span J 8.
 E-O3 (ex_o3.py): the ORDER-3 SURVIVORS of 4.3 (118 (subclass, n) configurations: H ties with T3 possible / T2 open, 'd=0 r=1'
   open, all open vertical items with |a| = 3, 5, 7), explicit box = the gen1k3 representative, n = the delta-law value, rational
   parts all multisets of R(5) (n <= 2) / R(4) (n = 3), 200 random (n >= 4): 45,200 products, 717,163 candidates: 0 UNITS,
   0 double-gate passers, min span J 13.
 E-O3b (ex_o3b.py): the n=3/4 unsafe classes NOT closed by H3(B) (34 + 2), every order-3 subclass representative + n rational
   boxes for n = 1, 2 and every delta-law value <= 6 (all R(4) multisets for n <= 2, 150 random otherwise): 58,588 products,
   1,038,058 candidates: 0 UNITS, 0 double-gate passers, min span J 17.
 E-S (ex_s2.py, sanity of ARB-2): 3,000 random products of CERTIFIED depth-one classes (1-3 boxes from the 10,541 S** depth-one
   representatives, 0-2 rational boxes from R(4)): 75,579 candidates: 0 UNITS (as the theorem predicts), min span J 18.
 TOTAL (this lane, frontier searches E-D1..E-D6 + E-O3 + E-O3b): 222,397 products, 3,716,659 Lemma-W candidates (every mu, every odd a,
   N in the windows): 0 UNITS,
   0 candidates with a_2 = 0 and J(zeta_10) = 1.  NEAR MISSES: span J 6 (single-child closure of a dangerous class, E-D1),
   10 (LP-open rounding, E-D2), 17 (V tie, E-D3); none passes both gates.  No HIT file written.

## 7. What can be stated, and the exact residual frontier
 THEOREM ARB (combined; PROVED modulo the C1 framework -- Lemma W, BX1-BX4/BX4', T2, the jet automaton (refGen: PROVED), R0/R2 --
 Theorem N (horizontal), Theorem V (vertical; skein-dictionary GAP upstream) and the halfword dictionary).
 Let (K,h) be strongly invertible with quotient the ROOT CLOSURE (horizontal X^mu, any mu != 0, or vertical, any odd a) of
 Y^N (B_1 ... B_k u_1 ... u_n), u_i non-integral rational tangles (n >= 0), B_j non-rational boxes, k + n >= 2.  Then J(K,h) != 1 if
   (i)   k = 0  (Q-MONT, V3, and 5a for the vertical n = 0 pretzels);
   (ii)  every B_j is eligible (|lc b/lc a| = 1 at both ends), has span a >= 3 and an order-2 signature in S** (10,877 classes:
         top-300, D36, 10,541 depth-one signatures; lists in gen1_*.pkl minus greedy_n2.pkl['D'], plus certtest2.pkl['safe'])
         -- ARB-2, containing M300, D36* and D2x2 (5c, 5d) -- any multiplicities;
   (iii) k = 1, n >= 1 and B in the per-class lists (order-2 signature in the list AND order-3 end data among that class's
         subclasses in gen1k3_R5_n2.pkl / gen1k3u_*.pkl -- e.g. every box of the enumerated depth-one families with that
         signature): horizontal closures for the 578 n=2 classes of hb_o3.pkl['closed'] and the 3,424 n=3/4 classes of
         o3_u_n3.pkl / o3_u_n4.pkl ['Hc'] (H3(B)), vertical closures for the 622 n=2 classes of o3v.pkl['vclosed'] (V3(B)),
         both for 566 n=2 classes;
   (iv)  (partial, by configuration) for ANY multiset of top-300 + d2pos boxes and any rational part, no unit closure has its weak
         end in configuration F1 ('d=-1 e=-1', lpgen 5.5') or F1' ('d=1 e=-1', 5b + 5b'): both are empty at every multiplicity.
 THE RESIDUAL FRONTIER (an arborescent counterexample must have a factor of type F-A, F-B or F-D, or be of type F-C; every listed
 family was searched exactly, 0 units):
  F-A TWO-ENDED, RESONANT factors: an eligible factor whose signature is outside S** -- in the computed lists: 666 dangerous n=2
      classes (per-class closures above remove most of them for k = 1 only), 3,460 unsafe n=3/4 classes, 260 classes with sigma in
      Z/3, Z/4.  Structure (CHECKED): sigma(B) = sigma*-type classes (sigma = -1: vertical second-order tie), delta(B) >= 0 classes
      (the delta-law no longer caps the number of factors in offset-0 configurations), positive-potential classes; 84% of the n=2
      ones are near-resonant nests; the certificates they break are 'd=0 r=1' slices and second-order ties (two-ended), only 68
      of 4,126 break offset cases alone.  After order 3 (single box): ties with the tau-law satisfied (T3 possible; need order 4)
      and a few offset 'd=-2 e=1' at mu = +-1.
  F-B INELIGIBLE factors (GAP-ELIG): |lc b/lc a| != 1 at an end.  Generated in infinite families by M-LEAD (lc 1/(k+1)); excluded
      by every certificate theorem (C1, lpgen, ARB).  At a unit closure the non-coincident end forces |lc a_i| = 1 (S1-dominated) or
      |lc b_i| = 1 (S2-dominated) for all children, but eps = lc S2/lc S1 may be ANY integer: the casework must be extended to
      integer eps (offset +-1, +-2 rows become eps-dependent; slice eps).  E-D6: 0 units.
  F-C SINGLE-CHILD closures (k = 1, n = 0): engineA E1 territory, computational only; every open LP case of D36* lives there.
  F-D NOT ENUMERATED: depth >= 2 nests beyond lpgen's lists, |m| > 7 or |N| > 4 on special products (clipping thresholds grow there),
      children outside R(5)/R(4).  By N-INF no finite list covers them: they need the parametrised-family LP (section 2) or a
      uniform order-3 two-ended lemma.

## 8. GAPs and next steps
 GAP-1 (main): the UNIFORM order-3 two-ended lemma for MULTISETS (dangerous boxes together with S** multisets and rational parts).
   Done here only per class (k = 1): H3(B) 578, V3(B) 622, both 566 of 636.  The ingredients are in place and tested: the 'd=0 r=1'
   order-3 equality (negative control 16/16), lpgen's T3/T2 tie rows, the X1-slicing that makes T2 linear in n (cross-check
   1,200/1,200).  For multisets, D2 and m vary with the multiplicities: slice (m or D2, X1) on the lattice + the big-|.|
   relaxations of section 4; then re-run the greedy/column test of section 4 with order-3 rows.  After that: order 4 for the
   ties where the tau-law holds (T3 possible), exactly as 5b' did for F1'.
 GAP-2 (GAP-ELIG): integer eps in the casework (F-B): ineligible boxes are excluded from every certificate theorem so far.
 GAP-3: no finite class list can prove Lemma Q for all arborescent quotients (N-INF).  A proof must use the structure of section 2
   (class of F_m(P) = additive part + residual, residual piecewise polynomial in the slope's log-jet sums) as an LP over
   PARAMETRISED families, or an inductive potential invariant -- and the potential law is false already at depth one (section 3).
 GAP-4: classes with sigma in Z/3, Z/4 (260) not run; |m| > 7 / |N| > 4 near resonance not enumerated; depth >= 2 only via
   lpgen's lists (top-300, d2pos).
 CAVEATS: all certificate theorems are about C1's order-2 weak-end casework (refereed SOUND by refGen) and inherit Theorem V's
   skein-dictionary GAP for vertical closures; 'd=0 r=0' was skipped as vacuous (PROVED: eps = +1 forces |lc F| = 2 |lc S1| >= 2);
   ARB-1/2 need span a >= 3 per non-rational factor for the n = 0 products (true for every listed box: depth-one min span a = 6,
   top-300 >= 10 (refGen)).  'Theorem' statements about signature classes apply to ANY eligible box with that signature.

## 9. Files (this folder)
 jbox.py (two-end precision-tracked jet arithmetic, signatures), jbox_val.py (validation 1,496/1,496), mech.py (N-INF family),
 gen1.py + gen1_R5_n2.pkl / gen1_R5_n3.pkl / gen1_R4_n4.pkl (depth-one closure; signature -> [count, eligible, representative
 (multiset of lib.rational(L) indices, N, m)]), gen1k3.py + gen1k3_R5_n2.pkl (order-3 subclasses), anasig.py, pos1.py (exact
 check of positive potential), resonance.py, residual.py / affine.py (+ .log/.pkl; normalisation), spanchk.py,
 arblp.py (general uniform LP driver: big-|m| relaxations, r=0 skip), run_arblp.py + arblp_n2.pkl/.log, greedy.py + greedy_n2.pkl
 (ARB-1 family, dangerous set D), ARB1_family.pkl, certtest2.py + certtest2.pkl (ARB-2 safe/unsafe), verify_arb2.py (+ .pkl/.log;
 independent certificate re-check), o3h.py / o3h_ctl.py / hb_o3.py / vb_o2.py / o3v.py / o3v_xchk.py, gen1k3u.py / o3_u.py / o3_uv.py (+ .pkl/.log; order 3
 on the frontier), d2two.py / d2two_phi.py / d2two_ctl.py (5c), d36star.py / d36star2.py (5d), f1b_tail.py / f1b_tail2.py (5b),
 f1b_o4_prep.py / f1b_o4.py (5b'), pretzel_n0.py (5a), exact_arb.py + ex_d1..ex_d6.py + ex_o3.py + ex_o3b.py + ex_s2.py (+ .pkl/.log; exact searches), r4chk.py (R4 check),
 waitfor.sh.  REPORT_draft_0612.md / REPORT_new.md = earlier drafts.
 Representative boxes: exact_arb.tree_of(rep, lib.rational(L)) gives the engineA tree; vc.hw(tree) the explicit half-word.
