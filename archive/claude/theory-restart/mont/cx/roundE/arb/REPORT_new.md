# ENGINE ARB REPORT (round E): Lemma Q for arborescent quotients via end-jet closure
17 Nov 2026, Claude (engine ARB). Folder ~/jones-lanes/theory-restart/mont/cx/roundE/arb/ .  Python: /opt/homebrew/bin/python3
(scipy HiGHS for LPs; every certificate re-verified exactly in Fractions by lpgen's lpg.farkas).  Marks: PROVED / CHECKED(n) /
CONJECTURE / GAP / FALSE.   STATUS: FINAL (06:2x).  NO HIT (0 units in 118,609 exact products / 1,961,438 Lemma-W candidates).

## HEADLINE
 * THE CLOSURE IS NOT FINITE (PROVED, explicit family).  Arborescent boxes do NOT have a finite end-jet automaton (unlike rational
   boxes, refGen).  Mechanism M-LEAD: when the children's slopes cancel in degree and sign at an end (q_P ~ 1 or q_P ~ e2), the
   eigen-coordinate z_P = (q_P-1)/(q_P-e2) acquires an ADDITIVE log-jet sum as its leading coefficient, and the nest F_m moves it
   into the slope's leading coefficient or into any jet order: F_-1(Y^(-k/3) B(XY)^k) has top slope lc 1/(k+1) (k = 0 mod 6), and
   F_+1 of the same product is ELIGIBLE with l2(q) = -k.  Rules R1-R5 (star / Y^N / F_m in the eigen-coordinate, two clipping
   lemmas) are PROVED; the clipping threshold for F_m is |m| >= max z-order + K + 2 (= K+3 for generic products) and grows on
   special products.  Normalisation: the class of F_m(P) = (additive data of P) + G(slope state of P, m); G is NOT finite either
   (it depends on the slope's log-jet sums), see section 2 for the affine test.
 * POSITIVE END POTENTIAL ALREADY AT DEPTH ONE (CHECKED exactly, 28 classes): e.g. F_-5(B(XY) B(xy)) has rho_a = +1 at the bottom,
   F_+-6(B(XXY)B(xxy)), F_+-7(B(XXXY)B(xxxy)) likewise; b-potential at |m| = 3, 4.  engineA's potential law (checked only for
   |m| <= 3) is FALSE at depth one.  Mechanism: RESONANCE -- mirror-type pairs have q ~ e2 to 3-5 orders at both ends and the
   twist |m| = z-order makes w = (-t)^-m z of order 0.
 * THEOREM ARB-2 (PROVED by exact uniform Farkas certificates, modulo the C1 framework as refereed by refGen, Theorem N/V and the
   halfword dictionary): a CERTIFIED FAMILY S** of 10,877 order-2 classes -- top-300 + D36 + 10,541 eligible signatures of
   depth-one boxes F_m(Y^N u_1..u_n) (n = 2: R(5); n = 3: R(5); n = 4: R(4); 1 <= |m| <= 7, |N| <= 4) -- such that EVERY product of
   >= 2 factors whose non-rational factors have signatures in S** (ANY multiplicities, span a >= 3 each), with any number of
   non-integral rational boxes and any integral part, has NO flat horizontal (any mu != 0) and NO flat vertical (any odd a) closure.
 * THE RESIDUAL FRONTIER IS TWO-ENDED AND RESONANT (CHECKED): the uncertified depth-one classes (666 of n=2 after re-admission,
   3,460 of n=3/4, + 260 with sigma in Z/3, Z/4) are dominated by sigma = -1 (= sigma*_V: order-2 tie at both ends of a vertical
   closure) and delta >= 0 classes; 84% of the n=2 dangerous classes are (near-)resonant nests (gap <= 1) vs 30% of the certified
   ones; the certificates they violate are 'd=0 r=1' slices and ties (two-ended), only 68 violate offset cases alone.
 * CLOSED (PROVED): (4a) vertical n = 0 pretzels P(a,q,a), |a| >= 3, short hand proof; (4b) lpgen's F1' tail (mB <= -31) by an exact
   linear bound with the right asymptotic slope (A* = 5, 5.5 < 6), and (4b') lpgen's two remaining F1' survivors B^3 u_1 u_2 at
   ORDER 4 (K = 4 automaton, exact) -- F1' is now EMPTY for all top-300 + d2pos multisets; (4c) two D36 boxes x any top-300
   multiset; (4c') THEOREM D36*: ANY multiset of top-300 + D36 boxes (any number of D36 boxes), >= 2 factors.
 * EXACT SEARCHES of every residual family (dangerous classes alone / squared / cubed / paired, LP-open points rounded, V-tie
   configurations, aligned positive potential up to B^7, ineligible boxes): 118,609 products, 1,961,438 Lemma-W candidates,
   0 UNITS, 0 double-gate passers (a_2 = 0 and J(zeta_10) = 1); min span J 6 (single-child closure).

## 0. Log
- 05:21 read BRIEF, C1 REPORT, refGen NOTES, refV3 REPORT, lpgen REPORT + integrator note, engineA REPORT; code jauto, gen2, lpg.
- 05:25-05:35 item 4a (hand proof + exact check), 4c (uniform LP, integrator's suggestion), 4c' (D36*), 4b (F1' tail).
- 05:35-06:00 rules + jet arithmetic (jbox.py, validated), non-finiteness family (mech.py), depth-one closure (gen1.py), LP over
  the new classes (arblp.py, run_arblp.py), greedy certified family (greedy.py), certificate column test (certtest2.py).
- 06:00-06:15 exact searches E-D1..E-D6, resonance anatomy, F1' survivors at order 4 (f1b_o4.py), normalisation tests.

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
  (R4) CLIPPING LEMMA for F_m (PROVED).  Let delta_t = deg_top z_P, o_b = ord_bot z_P (lowest exponent).  If
       m >= max(delta_t, -o_b) + K + 2 then at the top w = O(u^(K+2)) (so a', b' have the K-jets of alpha_P) and at the bottom
       1/w = O(t^(K+2)) (so a' = -alpha_P w (1 - 1/w), b' = -alpha_P e2 w (1 - 1/(e2 w)), K-jets = those of alpha_P w, alpha_P e2 w,
       whose RELATIVE jets do not depend on m); symmetrically for m <= -(max(-delta_t, o_b) + K + 2).  Hence the order-K signature
       of F_m(P) is independent of m beyond these thresholds (only the overall degree of a' moves = a unit).  For a GENERIC product
       (z of order one at both ends: delta_t in {0,1}, o_b in {-1,0}) the threshold is |m| >= K+3 = refGen's M for rational boxes;
       it GROWS with the z-order of special products (CHECKED: gen1, m = +-7 vs +-6 differ on 302/14,694 depth-1 instances, all
       special).
  (R5) CLIPPING LEMMA for Y^N (PROVED).  If deg_top(t^-3N q_P) >= K+2 then z = 1 + O(u^(K+2)); if <= -(K+3) then z = (1/e2)(1+O(u^(K+2)));
       likewise at the bottom; so for |3N| >= |deg q_P| + K + 3 (both ends) the order-K signature of F_m(Y^N P) is N-independent.
 Implementation: jbox.py (precision-tracked truncated series at both ends, 8 orders kept per leaf, low precision FLAGGED, never
 guessed).  VALIDATION: signatures of 1,496 random depth-1/depth-2 boxes (R(5) children, |m| <= 6, |N| <= 3) equal the exact
 vector computation (C1's bdata) in 1,496/1,496; 4 flagged low-precision (jbox_val.py).  CHECKED(1,496).

## 2. Is the closure finite?  NO (PROVED) -- mechanism M-LEAD; normalisation
 THEOREM N-INF (PROVED, exact, mech.py).  Let u = rational box XY (R_1-type: top slope q = -t^-1(1 + u - u^2/2 ..) ~ e2).  For k = 0 mod 6
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
 NORMALISATION: by (R3) the class of F_m(Y^N P) = (additive data of P) + G(z_P-state, m); the clipping lemmas make G depend on
 finitely many (shape, m, N) away from the special shapes; at the special shapes G depends on L_j (rational functions such as
 1/(1+L_1)), and eligibility pins L_j to finitely many values (lc q' = +-1), the infinite eligible families being AFFINE in the
 additive sums (F_+1(P_k): l2 = -k).  CONJECTURE (CHECKED below on depth one): the eligible order-2 signatures of depth-one boxes form
 finitely many families that are affine images of the children's additive data; the LP (multiplicity cone) is the right tool, not
 a finite class list.

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
 (1/2)Z), exact LINEAR relaxations of the quadratic d=0 rows for |m| >= 15 (both signs, H and V; as in 4c'), ties; constraint
 >= 1 non-rational box and >= 2 factors.  'd=0 r=0' is VACUOUS and skipped (PROVED, refGen remark (a)): offset 0 without
 cancellation means eps = +1, so lc F = 2 lc S1 is an even non-zero integer, never +-1.
 Sanity: on top-300 + D36 it reproduces D36* (511 sampled jobs, all closed).
 RUN 1 (arblp_n2): S = top-300 + D36 + 1,881 new eligible depth-one signatures (R(5), n = 2): 2,237/2,935 case-LPs OPEN; every
   open support contains new classes (130 distinct; positive-potential and delta >= 0 / sigma <= -1 classes dominate).
 GREEDY CERTIFIED FAMILY (greedy.py; remove every new class occurring in an open LP support, re-test, iterate; 16 rounds):
   THEOREM ARB-1 (PROVED; exact certificates; modulo the C1 framework as refereed by refGen, Theorem N/V and the halfword
   dictionary).  Let S* = the top-300 classes + the 36 D36 classes + 1,107 further ELIGIBLE order-2 signatures of depth-one boxes
   F_m(Y^N u_1 u_2) (u_i in R(5), 1 <= |m| <= 7, |N| <= 4; list = gen1_R5_n2.pkl minus greedy_n2.pkl['D']).  For every product
   Y^N (B_1 ... B_k u_1 ... u_n) with k >= 1 boxes whose signatures lie in S* (ANY multiplicities), n >= 0 non-integral rational
   boxes and k + n >= 2, every N: no horizontal closure (any mu != 0) and no vertical closure (any odd a) is flat.
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
   an end.  Off resonance (g >= 2) nests behave like rational boxes (Lemma Z) and are certified.

### 4.2 Extension to 3 and 4 rational children: certificate column test (certtest2.py)
 For every one of the 1,593 case-LPs, an exact Farkas certificate y over S* (ARB-1) is recomputed; a candidate class with column c
 is compatible iff c.y >= 0 (the extended LP stays infeasible with the SAME certificate).  A class compatible with ALL 1,593
 certificates can be added to S* with any multiplicity, and all such classes simultaneously.  Candidates: D (774) + every new
 eligible signature with sigma in Z/2 from R(5) n=3 and R(4) n=4 (12,786): 13,560.  Every job had a certificate over S*.
 RESULT: SAFE 9,434 (108 of D re-admitted, 5,960 of n=3, 3,366 of n=4); UNSAFE 4,126 (666 of D, 1,974 n=3, 1,486 n=4).
 THEOREM ARB-2 (PROVED, same hypotheses as ARB-1): ARB-1 holds with S* replaced by S** = S* + the 9,434 safe signatures
 (10,877 order-2 classes in all: top-300, D36 and 10,541 eligible depth-one signatures with 2-4 rational children, |m| <= 7,
 |N| <= 4).  Certified = any multiset of boxes with these signatures, any rational part, >= 2 factors, every mu, every odd a.
 (Classes with sigma in Z/3 or Z/4 (260 of n=3/4) were not tested: uncertified.)
 Anatomy of the 4,126 unsafe classes: sigma = -1: 2,073; sigma < 0: 2,866; delta >= 0: 972; positive potential: 20.  Violated
 certificate families: d=0 r=1 slices (426,544 violations), ties (25,740), big r1 (12,492), offsets (~11,000).  Per class:
 (d0, tie) 2,722; (big, d0, tie) 485; d0 only 344; (big, d0, off, tie) 318; offsets only 68.  => The uncertified frontier is
 TWO-ENDED (offset-0 weak end with exactly one cancelled order, or a second-order tie at both ends), as for lpgen's GAP-A.

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
   mirror box 50139 at mu = -2, exactly n = 2 rational boxes), searched exactly by lpgen for u_i in R(5)/R(6) (0 units): RESIDUAL
   (needs order 4 for ALL rational u_1, u_2; see section 7).

### 5b'. lpgen's two F1' SURVIVORS closed at ORDER 4 (PROVED, exact; f1b_o4.py)
 Configurations (lpgen 5.9): B^3 u_1..u_n with B = box 50216 at H mu = +2 (weak top) and the mirror B = box 50139 at mu = -2
 (weak bottom); offset +1, eps = -1, mB = -7 (3 x sigma -2 against sigma* = +1).  The Phi_3 pattern f = s1 - u s2 = 1 + u + u^2
 + 0u^3 + 0u^4 gives, with log-jets (X, Y, Z, W) of orders 1-4 and series coefficients s_k:
   [u^1] X1 = 2;  sigma-law X2 = X1 + mB;  [u^2] Y1 = X2 - 1;  [u^3] Z1 - Y2 = mB^2/2 - 4/3 (lpgen);
   [u^4] (NEW) W1 - Z2 + (X1 - X2) Y2 = X2^3/6 - X1 (mB^2/2 - 4/3) - Y1^2/2 - X1^2 Y1/2 - X1^4/24.
 Rational part EXACT on the K = 4 jet automaton (35 states; 174 distinct edge log-jets; terminal q log-jets; refGen: the automaton
 is PROVED for all rational boxes at every fixed K, bottom data = top data of mirrors), n >= 0 FREE.
 CONTROL: orders 1-3 alone are FEASIBLE with n = 2 (reproduces lpgen's survivor exactly).  With [u^4] added: INFEASIBLE, exact
 Farkas certificate, for BOTH configurations.  => Together with section 4b (tail) and lpgen 5.9 (slices |mB| <= 30, whose only
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
 and 4c, and closes all multisets built from the 36 b-potential depth-2 classes.

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
 TOTAL (this lane): 118,609 products, 1,961,438 Lemma-W candidates (every mu, every odd a, N in the windows): 0 UNITS,
   0 candidates with a_2 = 0 and J(zeta_10) = 1.  NEAR MISSES: span J 6 (single-child closure of a dangerous class, E-D1),
   10 (LP-open rounding, E-D2), 17 (V tie, E-D3); none passes both gates.  No HIT file written.

## 7. What can be stated, and the exact residual frontier
 THEOREM (combined; PROVED modulo the C1 framework -- Lemma W, BX1-BX4/BX4', T2, the jet automaton (refGen: PROVED), R0/R2 --
 Theorem N (horizontal), Theorem V (vertical; skein dictionary GAP upstream) and the halfword dictionary).
 Let K be strongly invertible with quotient a ROOT CLOSURE (horizontal X^mu, any mu != 0, or vertical, any odd a) of
 Y^N (B_1 ... B_k u_1 ... u_n), u_i non-integral rational tangles (n >= 0), B_j non-rational boxes, k + n >= 2.  Then J(K,h) != 1 if
   (i) k = 0 (Q-MONT, V3, and 5a for n = 0 vertical), or
   (ii) every B_j is eligible with span a >= 3 and order-2 signature in S** (10,877 classes; ARB-2; contains M300, D36*, D2x2), or
   (iii) the non-rational part is any multiset of top-300 + d2pos boxes and the weak end is in the offset-+1 configuration F1'
        (empty, 5b/5b'), or in F1 (lpgen 5.5'), at every multiplicity.
 THE RESIDUAL FRONTIER (where an arborescent counterexample would have to live; every item searched exactly, 0 units):
  F-A (two-ended, resonant): a factor whose signature is UNCERTIFIED -- in the lists: 666 dangerous n=2 classes, 3,460 unsafe
      n=3/4 classes, 260 classes with sigma in Z/3, Z/4; structurally: sigma(B) = sigma*-type classes (sigma = -1: vertical
      two-ended order-2 tie), delta(B) >= 0 classes (the delta-law no longer caps the number of factors in d=0 configurations) and
      positive-potential classes; 84% of the n=2 ones are near-resonant nests (twist within one of the product's z-order).  The
      certificates they break are 'd=0 r=1' slices and second-order ties, i.e. lpgen's GAP-A: the next step is the order-3 analysis
      of two-ended configurations (tau-law + the T2 condition d3 = d2 (1 - X1), and for 'd=0 r=1' the order-3 equality
         d3 = -m [1/2 - Y2 + (1 - X1)^2/2 - m^2/6]   (DERIVED here, d_k = l_k(s1) - l_k(s2), m = mB, X1 = l1(s1), Y2 = l2(s2)),
      quadratic in X1: slice X1 + linear relaxation for large |1 - X1|; not run).
  F-B (ineligible boxes, GAP-ELIG): |lc b/lc a| != 1 at an end.  Generated in infinite families by M-LEAD (lc 1/(k+1)); excluded
      by every certificate theorem so far (C1, lpgen, ARB).  At a unit closure the non-coincident end forces |lc a_i| = 1 for all
      children (S1-dominated) or |lc b_i| = 1 (S2-dominated), but eps = lc S2/lc S1 may be ANY integer there: the casework must be
      extended to integer eps (offset +-1, +-2 rows become eps-dependent; slice eps).  E-D6: 0 units.
  F-C (single-child closures, k = 1, n = 0): engineA E1 territory (computational only); every open LP case of D36* lives there.
  F-D (depth >= 2 and larger parameters): nests of nests, |m| > 7 or |N| > 4 on special products (the clipping thresholds grow
      there), children outside R(5)/R(4): not enumerated; by N-INF no finite list can cover them -- they must be handled by the
      affine-family structure (section 2) or by the order-3 two-ended lemma.

## 8. GAPs and next steps
 GAP-1 (main): order-3 (and 4) two-ended lemmas for multisets (ties: tau-law + T2; 'd=0 r=1': the equality above), uniform over
   multiplicities.  This is what blocks 4,126 + 666 classes; implementing it on the dangerous classes is the next concrete step
   (the order-4 run of 5b' shows the automaton machinery works at K = 4 with exact certificates).
 GAP-2 (GAP-ELIG): integer eps in the casework (F-B).
 GAP-3: no finite class list can prove Lemma Q for all arborescent quotients (N-INF); a proof must use the structure
   (class of F_m(P) = additive part + G(slope state, m), G piecewise polynomial in the slope's log-jet sums) as an LP over
   PARAMETRISED families, or an inductive potential invariant.
 GAP-4: classes with sigma in Z/3, Z/4 (260) not run; |m| > 7 / |N| > 4 near resonance not enumerated.
 CAVEAT: all certificate theorems are about the order-2 casework with C1's weak-end rows; they inherit C1's framework (refereed
   SOUND by refGen) and Theorem V's skein-dictionary GAP for vertical closures; 'd=0 r=0' was skipped as vacuous (PROVED: eps = +1
   forces |lc F| = 2 |lc S1| >= 2).

## 9. Files (this folder)
 jbox.py (two-end precision-tracked jet arithmetic, signatures), jbox_val.py (validation 1,496/1,496), mech.py (N-INF family),
 gen1.py + gen1_R5_n2.pkl / gen1_R5_n3.pkl / gen1_R4_n4.pkl (depth-one closure; signature -> [count, eligible, representative
 (multiset of lib.rational(L) indices, N, m)]), gen1k3.py + gen1k3_R5_n2.pkl (order-3 subclasses), anasig.py, pos1.py (exact
 check of positive potential), resonance.py, residual.py / affine.py (+ .log/.pkl; normalisation tests), spanchk.py,
 arblp.py (general uniform LP driver incl. big-|m| relaxations, r=0 skip), run_arblp.py + arblp_n2.pkl/.log, greedy.py +
 greedy_n2.pkl (certified family ARB-1, dangerous set D), certtest2.py + certtest2.pkl (ARB-2 safe/unsafe lists),
 ARB1_family.pkl (S* new classes with representatives, D), d2two.py / d2two_phi.py / d2two_ctl.py (4c), d36star.py / d36star2.py
 (D36*), f1b_tail.py / f1b_tail2.py (+ logs; F1' tail), f1b_o4.py / f1b_o4_prep.py (+ log; F1' survivors at order 4),
 pretzel_n0.py (5a), exact_arb.py + ex_d1..ex_d6.py (+ .pkl/.log; exact searches), waitfor.sh.  REPORT_draft_0612.md = earlier draft.
 Representative boxes: exact_arb.tree_of(rep, lib.rational(L)) gives the engineA tree; vc.hw(tree) the explicit half-word.
