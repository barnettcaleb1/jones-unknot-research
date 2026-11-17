# ENGINE lpgen REPORT (round D): multi-box Farkas/LP generator over jet classes
17 Nov 2026, Claude (engine lpgen). Folder ~/jones-lanes/theory-restart/mont/cx/roundD/lpgen/ .  Python: /opt/homebrew/bin/python3
(numpy/scipy HiGHS for the LPs; every certificate re-verified in exact Fractions).  Marks: PROVED / CHECKED(n) / CONJECTURE / GAP / FALSE.
STATUS: FINAL (04:55).  NO HIT.  (d2fix2 and the first J4/probe runs were killed externally at 04:38 under machine load ~400;
J4 and the R(6) probe were rerun and completed; d2fix2 is NOT claimed.)

## HEADLINE
 * GENERATOR.  C1's weak-end casework is AFFINE in the end-jet data, and those data are ADDITIVE under the star product, so
   'no flat closure for products of ANY number of boxes from a class set S' is ONE linear program per case over the multiplicity
   cone (rational part = n x the flow polyhedron of the K=3 jet automaton; the quadratic d=0 cases sliced by mB).  Infeasible
   <=> one Farkas certificate valid for EVERY multiplicity vector and every n.  Validated: re-derives Q-MONT (every mu) and V3
   exactly, reproduces C1's single-box verdicts on 360 classes (0 disagreements), and leaves open exactly C1's n = 1 negative
   control (mu = +-1 offset -2, mu = +-2 d=0 r=1, |mu| >= 3 tie at n = 1).
 * THEOREM M300 (PROVED; 955 exact certificates + PHI-LEMMA): any multiset of >= 2 boxes from the 300 most frequent jet classes
   (any box with such a signature; 27,585 library boxes), times ANY number n >= 0 of rational boxes, any integral part: NO horizontal (any mu) and NO vertical (any odd a)
   closure is flat; also for one such box with n >= 1.  (C1 had singles and pairs; this is all multiplicities at once.)
 * THEOREM D36 (PROVED): one box from 36 of the 60 depth-2 positive-potential classes x ANY top-300 multiset x ANY rational part:
   never flat.
 * FRONTIER (exact, order 2): every uncertified combination contains a positive-potential (depth-2) factor.  Anatomy: each d2pos
   class has ONE positive end (b-potential rho_b = +1, sigma = 2..4, or a-potential rho_a = +1, sigma = -1/-2).  Universal open
   case F1 (offset -1, eps = -1: needs b-potential 2 - q1 at one end), unbounded in the multiplicities; plus two-ended families
   (d=0 r=1, ties) for a-potential classes.  Small combos: 24/60 single classes, 73/1830 d2 x d2 pairs, 18 x 50 d2 x top pairs open.
 * ORDER 3 (PROVED lemma): in F1, X1 = 2 - mB is pinned and the u^3 coefficient gives the EQUALITY l3(s2) - l2(s1) = mB^2/2 - 4/3.
   It closes F1 COMPLETELY for every multiset of the listed library boxes of the top-300 + d2pos classes (3,735 order-3 subclasses; exact
   certificates: mB <= -31 at order 2, mB >= 31 by an exact linear bound vs the quadratic, |mB| <= 30 by slices; 4 slices MILP).  6 of the 24 open
   single classes (all b-potential) are thereby closed.  At the H mu = +-1 ties the tau-law contradicts the delta-law (T3
   impossible) and the first order-3 condition closes the weak end except at the box's a-POSITIVE end.
 * EXACT SEARCH of the frontier (Lemma W windows, gates a_2 = 0 and J(zeta_10) = 1): d2 x d2 open pairs with n <= 2 (256,150
   products), open d2 singles with n = 1..3 (215,016), open d2 x top-50 pairs with n <= 1 (147,900), d2 triples with n <= 1
   (193,069) and the order-3 survivors (34,382): 846,517 products, 17.8M candidates, 0 UNITS, 0 double-gate passers, min span 15.
 * MIRROR CASE F1' ('d=1 e=-1', the H mu = +-2 order-2 frontier, needs a-potential X1 = 2): same order-3 equality
   l3(s1) - l2(s2) = mB^2/2 - 4/3 closes all but ONE integer configuration on |mB| <= 30: B^3 u_1 u_2 with B = box 50216
   (class d2_497) at mu = +2 (weak top), mirror B = box 50139 (d2_460) at mu = -2; of n = 0..7 only n = 2 rational boxes fit.  Exact search of
   it (R(5), n = 1..3, and R(6) at n = 2: 34,382 products, 875,094 candidates): 0 units, min span J 40.  Tail mB <= -31 (>= 15 aligned a-potential
   boxes at mu = +-2) is not bounded by the linear argument: GAP.
 * WHAT IS LEFT (sharp), for products from the top-300 + d2pos classes: (i) TWO-ENDED configurations (H mu = +-1 ties and
   'd=0 r=1', V 'd=0 r=1' and V tie) containing a-potential factors (sigma < 0); at order 3 only the single-box H mu = +-1 tie was
   treated, and there the survivor is pinned to the box's a-POSITIVE end (order-4 test next: K = 4 automaton, X1 sliced);
   (ii) the F1' survivors above and the >= 15-box tail at mu = +-2; (iii) single-child closures (|k| = 1, n = 0; engineA E1, exact).
   Every ONE-ended (offset != 0) configuration is closed at order 2 or 3 apart from (ii).

## 0. Log
- 03:45 read BRIEF, C1/A REPORTs and C1 code (gen2.py, v3b.py, v3b3.py, h3b.py, jauto.py).  Copied C1 modules to c1copy/ (only
  sys.path lines changed).  Built lpg.py (LP generator) + runner.py.  Python: /opt/homebrew/bin/python3 (has numpy/scipy; pure-Python
  C1/engineA code runs unchanged there).
- VALIDATION 1 (val1.py): transcription of C1's casework into affine-in-B-data rows: 78,738 case systems compared at random B-data,
  0 mismatches (CHECKED).  Rational-only (k = 0): n >= 2: ALL 265 case-LPs infeasible with exactly verified Farkas certificates
  (re-derives Q-MONT for every mu and V3); n >= 1: V all closed (V3 for one rational box, |a| >= 3), H open EXACTLY at
  mu = +-1 'd=-2 e=1', mu = +-2 'd=0 r=1', |mu| >= 3 two-ended tie at n = 1 (= the n = 1 negative control of C1; units exist there:
  two-bridge unknots).  CHECKED.
- VALIDATION 2 (val2.py, 148 s): single non-rational box (k = e_j), n >= 1, for the 360 classes top-300 + 60 depth-2
  positive-potential (d2pos) classes (27,841 boxes): per class and per closure family (V; H for each mu) the lpgen verdict equals
  C1's gen2 verdict EXACTLY: C1-closed => lpgen-closed (0 violations) and lpgen closes nothing more here (C1's multiplier grid
  was already complete for these classes).  0 unverified certificates.  Open (box-weighted): V 'd=0 r=1' 320, H mu=+-1 tie 80+80,
  H mu=+-1 'd=-1 e=-1' 66+66, H mu=+-1 'd=0 r=1' 20+20, V tie 20.  CHECKED(360 classes).
- UNIFORM RUNS (run_uni.py; nmin = min number of rational boxes, kmin = min number of non-rational boxes; every case LP is over ALL
  real k >= 0, so 'closed' = one exact Farkas certificate for every multiplicity vector at once):
    top-50,  kmin=1, n>=0: 951/955 closed; open only H |mu|>=3 two-ended tie at |k| = 1, n = 0 (single-child closures, engineA E1).
    top-50,  kmin=2, n>=0: 955/955 closed.
    top-300, kmin=1, n>=0: 943/955 closed; the 12 open cases all sit at |k| = 1, n = 0 (single-child closures).
    top-300, kmin=2, n>=0: 955/955 CLOSED.        top-300, kmin=1, n>=1: 955/955 CLOSED.
    top-50 + 60 d2pos classes, kmin=1, n>=0: 836/955 closed, 119 open (all involve d2pos classes; see section 4).
- PHI-LEMMA (PROVED; closes the d=0 slices for ALL values of mB): phi := rho_a + rho_q/2 at the weak end.  Rational boxes:
  sup phi = -1/2 (exact automaton longest path), lambda_q in [-2,1].  Top-300 classes: phi_j <= -1/2 at both ends, |lambda_q,j| <= 2.
  If every box has phi <= -1/2 then (vertical, d=0): r=0 reads sum phi = 1 - (p1+q1)/2 > 0: IMPOSSIBLE for every mB; r=1 reads
  sum phi = 1 - (p1+q1)/2 - (LQ - p2 + q2)/mB, hence N(1/2 - Lmax/|mB|) <= -1 + (p1+q1)/2 + |q2-p2|/|mB| < 0: IMPOSSIBLE for
  |mB| >= 2 Lmax = 4.  Horizontal d=0 cases have n = delta.k - delta* >= 0, so |k| <= 3 and |mB| <= 5 (top classes: delta <= -1).
  So the LP slices |mB| <= 8 plus the phi-lemma cover every mB.  (30 of the 60 d2pos classes violate phi <= -1/2: positive potential.)
- PER-COMBO VERDICTS with d2pos classes (pairs_d2.py, S = top-50 + 60 d2pos, exact m-slices): single d2pos box with n >= 0 or
  n >= 1 rational: 24/60 classes LP-open (36 closed for every n, N, mu, a); d2 x d2 pairs (n >= 0): 73/1830 class pairs open;
  d2 x top-50 pairs: 900/3000 open = exactly 18 open d2 classes x all 50 top classes (generic boxes are absorbed like rational
  boxes).  Open cases are dominated by V 'd=0 r=1' and the mu = +-1 ties / 'd=-1 e=-1'.
- 04:01 THEOREM M300 certificates stored (certs_M300.pkl): 955 exact uniform Farkas certificates (one per case LP / mB-slice / tie),
  re-verified from scratch by an independent dual check (certs300.py), max denominator 59.  Exact frontier search launched
  (exact_run.py, families J1-J4).

## 1. Formulation (lpg.py)  [PROVED: soundness of the relaxation; CHECKED: transcription]
 Product Y^N (B_1^{k_1} ... B_S^{k_S}) u_1 ... u_n, B_j in a jet class j of S (key = top (rho_a, l2 a, rho_b, l2 b), bottom (same),
 sigma, delta), u_i non-integral rational.  The star product multiplies channels, so every end datum used by C1's weak-end
 casework is a SUM over factors: with d_j the class data, B-data(k) = sum_j k_j d_j, mB(k) = sigma.k - sigma*, deltaB(k) = delta.k.
 Every C1 case system (V: weak end x type x |a|=3/|a|>=5; H: weak end x mu-class; offsets d>=3, 2, 1, -1, -2, <=-3 with eps = +-1;
 d=0 r=0; d=0 r=1; the mB = 0 two-ended tie with the delta-law) is E z = r0 + R k with z = (alpha, P, L_a, Lambda) the rational sums,
 EXCEPT the d=0 cases, which carry mB^2 and mB*alpha: these are SLICED by the value m of mB (on a slice everything is affine) and
 have n pinned/bounded by the delta-law.  The rational sums are relaxed EXACTLY to the flow polyhedron of the K=3 jet automaton
 (n unit flows from init; flow polyhedron = n * conv(per-box vectors) since every cycle lies on an init->state path).
 Case LP: k >= 0, sum k >= kmin, n >= nmin, flows >= 0, E z = r0 + R k (+ slice + delta-law).  Infeasible <=> a Farkas vector
 (u, w) with A^T (u,w) >= 0 and b.(u,w) < 0: ONE certificate valid for EVERY multiplicity vector and every n at once (integer
 points are a subset).  Feasible <=> some real (k, n) admits no certificate; for a fixed integer k the same LP with k fixed decides
 exactly whether C1-type certificates exist for that combination (so 'open' = no certificate in this framework, not a unit).
 HiGHS solves the float LPs; every certificate is rationalised and checked EXACTLY (0 unverified in all runs).
 New vs C1: (a) any number of non-rational factors, multiplicities as LP variables; (b) complete multiplier search (C1: grid);
 (c) the mB = 0 situation split into 'two-ended tie' (delta-law + slice) and the remaining weak-end cases (C1-V gave up there).

## 2. Validation  [CHECKED]
 (i) transcription: 78,738 case systems vs v3b.cases / h3b.cases_pq at random B-data: 0 mismatches.
 (ii) k = 0: n >= 2 all 265 case-LPs closed = Q-MONT (every mu) + V3 re-derived; n >= 1: V closed (V3 at n = 1), H open EXACTLY at
      mu = +-1 'd=-2 e=1', mu = +-2 'd=0 r=1', |mu| >= 3 tie at n = 1 = C1's negative control (two-bridge unknots live there).
 (iii) single box (k = e_j, n >= 1), 360 classes (top-300 + 60 d2pos): identical verdicts to C1 gen2 per class and closure family.
 (iv) pairs: C1 proved all 45,150 top-300 signature pairs (n >= 1 and n >= 0); THEOREM M300 below contains all of them (and every
      larger multiset) in one certificate per case.

## 3. THEOREM M300 (PROVED: exact uniform certificates + PHI-LEMMA)
 Let S be any subset of the 300 most frequent jet classes of library A (C1's eligibility: |lc b/lc a| = 1 at both ends,
 span a >= 1).  The statement concerns ANY eligible box whose order-2 jet signature lies in S (only the signature enters the
 certificates), in particular the 27,585 listed library boxes.  For EVERY multiplicity vector k with |k| >= 2, every n >= 0 non-integral rational boxes and every N, the
 necklace X^mu Y^N (prod B_j^{k_j} u_1..u_n) is non-flat for every mu != 0, and the vertical closure is non-flat for every odd a.
 The same holds for |k| = 1 with n >= 1.  (|k| = 1, n = 0 = single-child closures: open only at H ties/offset cases, engineA E1.)
 Proof: 955 case-LPs (24 closure families x 11 offset cases, d=0 slices |mB| <= 8, ties) infeasible with exact certificates
 (certs_M300.pkl); d=0 slices with |mB| > 8: horizontal impossible (n = delta.k - delta* >= 0 and delta_j <= -1 force |k| <= 3,
 |mB| <= 5); vertical by the PHI-LEMMA (section 0 log): phi = rho_a + rho_q/2 <= -1/2 for every rational box (exact sup) and every
 top-300 class at both ends, |lambda_q| <= 2, so r=0 is impossible for all mB and r=1 for |mB| >= 4.  []
 Consequence (with Lemma Q / BRIEF section 0): Lemma Q holds for every strongly invertible knot whose quotient is such a closure;
 all its branch knots L_n have V != 1.  This replaces C1's 'pairs from the top-300 classes' by 'ANY number of factors'.
 Also top-50 (kmin=2) and top-300 with n >= 1 (kmin=1): all 955 closed.
 SANITY (j0.py, CHECKED 4,000): random products of 2-4 library boxes from the top-300 classes x 0-2 rational boxes (R(5)), exact
 closures in the Lemma-W windows: 123,941 candidates, 0 units, min span J 29 (consistent with the theorem).

## 4. The frontier: where NO certificate exists (S = top-300 + the 60 depth-2 positive-potential classes)  [CHECKED, exact LPs]
 Uniform run (uni_t300d2_n0.pkl): 830/955 case-LPs closed for EVERY multiplicity vector; 125 open.  Since top-300 alone is closed
 (THEOREM M300), every open combination contains >= 1 d2pos box.  Jet anatomy of the 60 d2pos classes (classes.d2pos()): each has
 exactly ONE positive end, with either rho_b = +1 (b-potential; 'sigma = 2,3,4' classes) or rho_a = +1 (a-potential, rho_b in
 {-1,0}; 'sigma = -1,-2' classes); the other end is generic-like (rho_a, rho_b <= -2).
 Open families (part = classes that can occur, unb = classes that can occur with multiplicity >= 50):
  (F1) offset d = -1, eps = -1 at the weak end, EVERY closure family (H all mu both ends, V all six types): part = unb = all 60 d2
       + all 300 top classes.  The case needs l1(s2) = 2 at the weak end, i.e. b-potential q1 + sum rho_b = 2; rational and top
       boxes have rho_b <= 0, so it needs (2 - q1) d2 boxes with rho_b = +1 at the SAME end (or a-potential boxes feeding P);
       after that, any number of generic and rational boxes can be added.  UNBOUNDED: the order-2 casework is exhausted here.
  (F2) V 'd=0 r=1' (64 of 70 mB-slices unbounded) and the V tie (mB = 0 needs sigma.k = -1: an a-potential box (sigma = -1) alone,
       or sigma = -2 plus sigma = +1 etc.).
  (F1') H mu = +-2 offset d = +1, eps = -1 (mirror of F1, needs a-potential l1(s1) = 2): ONE d2 class each (d2_497 at mu = +2,
       d2_460 at mu = -2; sigma = -2), unbounded in that class and in 10-20 top classes (see 5.9).
  (F3) bounded families: H mu = +-1 'd=0 r=1' slices and ties (<= 18 d2 classes, n pinned by the delta-law), H mu = +-2 'd=0 r=1'
       / tie and H mu = +-1 'd=-2 e=1' (top classes, |k| = 1, n = 0 only).
 Small combinations, per combination (pairs_d2.py; S = top-50 + d2pos; every mB slice exact):
   single d2 box, n >= 0 (or n >= 1): 24/60 classes OPEN:  d2_457 459 460 497 536 565 895 902 1232 1238 1247 1494 2557 2780
     3075 3076 3077 3933 4277 4643 5150 5152 5153 5154 (box weight 178 incl. pair classes); the other 36 classes CLOSED (any n, N, mu, a).
   d2 x d2 (n >= 0): 73/1830 class pairs OPEN (22 classes involved, 18 of them open singles); 1757 CLOSED.
   d2 x top-50 (n >= 0): 900/3000 OPEN = exactly the 18 'absorbing' open singles x all 50 top classes.
 THEOREM D36 (PROVED; d2fix.py, exact LPs + generalised phi-lemma): for each of the 36 d2pos classes NOT in the open-single list
 (90 depth-2 positive-potential boxes, e.g. d2_1588 ... d2_4710), the product of ONE such box with ANY multiset of top-300 boxes and
 ANY n >= 0 rational boxes, any N, has no flat horizontal (any mu) or vertical (any odd a) closure.  [d=0 slices: LP for
 |mB| <= 14; for |mB| >= 15 the phi-lemma with one exceptional box (phi_e <= 1/2, |lambda_e| <= 12) forces N <= 3 boxes, hence
 |mB| <= 7: contradiction; r=0 impossible for N >= 2.]  The 24 open single classes stay open with any top multiset added.

## 5. Exact search of the frontier and the order-3 closure of F1
 5.1 J1 (exact_run.py): d2 x d2 box pairs from the 73 LP-open class pairs (<= 10 boxes per class), with n = 0, n = 1 (R(6)) and
     n = 2 (R(4)) rational boxes: 256,150 products, 5,812,516 Lemma-W candidates (every mu, every odd a, every N in the windows),
     0 UNITS, 0 candidates passing both gates (a_2 = 0 and J(zeta_10) = 1), minimal span J = 22.  COMPLETE for these products.
 5.2 ORDER-3 LEMMA FOR F1 (PROVED).  In case F1 (offset -1, eps = -1) the order-1/2 rows pin alpha + P = 2 - K2 and P = P0, so
     X1 = l1(s1) = 2 - mB is DETERMINED; the u^3-coefficient of the Phi_3 pattern (0) then reads
         l3(s2) - l2(s1) = (X1 - 2)^2/2 - 4/3 = mB^2/2 - 4/3        (an EQUALITY, affine in the end data for fixed mB).
     Rational third-order data are exact on the K=3 automaton (l3 of D per edge is a function of the edge; l3(q) = FIN[s][2]).
     Third-order closure jets (computed, eng.W/WV): V '+': w1 (0,1,0), wV (1,1/2,1/3) for all a >= 3; '-': (0,-1|0,0), (0,0,0);
     H: mu = +-1: w3 (1,1/2,1/3); the |mu| >= 4 class SPLITS at order 3 (mu = +-4 differs from |mu| >= 5): both checked.
     RESULT (f1o3.py): all 198 (box, closure) instances of F1 left open by the order-2 generator among the 24 open d2pos classes
     are CLOSED by the order-3 equality (exact certificates).  So F1 is not a genuine frontier for single positive-potential boxes.
 5.3 UNIFORM ORDER-3 TEST OF F1 (f1uni.py): S = all 1,200 order-3 subclasses of top-50 (1,063) and the 60 d2pos classes (137),
     ANY multiplicity vector, n >= 0, every closure family (H |mu| >= 4 split into mu = +-4 and |mu| >= 5 at order 3), every slice
     |mB| <= 8: 374 slice-LPs: 314 already infeasible at order 2 on the slice, 58 closed by the order-3 equality (exact certificates),
     2 real-feasible (V typ '+' |a| = 3, mB = 4, top and mirror bottom: fractional mixtures 0.87 d2_457 + ...); the integer programs
     for these two slices are INFEASIBLE (HiGHS MILP, integer k and n): CHECKED (not an exact certificate).
     => At jet order 3 the universal order-2 frontier F1 is EMPTY for every multiset of these classes with |mB| <= 8 (CHECKED);
        all |mB|: see 5.5 / 5.5'.
 5.4 WHAT REMAINS AFTER ORDER 3 (single d2 box, d2fix1.pkl): 6 of the 24 open single classes (d2_457, 459, 895, 902, 1232, 1247:
     all b-potential, sigma = 3) had F1 as their ONLY open case and are now CLOSED (box level, order-3 certificates).  The other 18
     open classes are exactly the A-POTENTIAL classes (rho_a = +1 at one end; sigma = -1 or -2) and their open cases are all
     TWO-ENDED: H mu = +-1 tie (n = 2 pinned by the delta-law) or H mu = +-1 'd=0 r=1' (mB = 1), V 'd=0 r=1' (mB = -1 or 1), V tie
     (mB = 0).  Example d2_460: tau = lambda_q,top + lambda_q,bot = 0, so at the mu = +-1 tie the tau-law would need n = tau + 1 = 1
     but the delta-law pins n = 2: one end stops at r = 2 exactly and its Phi_3 pattern needs order-3/4 data (next lemma).
 5.5 F1 IS CLOSED AT ORDER 3 FOR EVERY MULTISET (top-50 + d2pos, 1,200 order-3 subclasses):
     (a) mB <= -31: the ORDER-2 F1 LP is already infeasible (f1bound.py, exact certificates, all 22 families);
     (b) |mB| <= 30: 1,342 slice-LPs: 798 closed at order 2, 542 closed by the order-3 equality (exact), 2 real-feasible slices
         (V typ '+' |a| = 3, mB = 4, top/bottom mirror) with NO integer multiset (MILP): CHECKED;
     (c) mB >= 31 (f1large.py): on the order-2 F1 region, LHS := l3(s2) - l2(s1) - (q3 - p2) satisfies LHS - 4 mB < b' with
         b' in [-37, -26] per family (EXACT Farkas certificates); the order-3 equality LHS = mB^2/2 - 4/3 - q3 + p2 then needs
         m^2/2 - 4m < b' + 4/3 + q3 - p2 < 0 with negative discriminant: IMPOSSIBLE.   [PROVED for (a),(c); (b) exact except 2 MILP]
     So the universal order-2 frontier F1 disappears completely at order 3 for these classes.
 5.5' SAME FOR top-300 + d2pos (3,735 order-3 subclasses = every box of those 360 classes): mB <= -31 closed at order 2
     (f1bound_t300.log, 22/22 exact); |mB| <= 30: 1,342 slice-LPs, 798 closed at order 2, 540 at order 3 (exact), 4 real-feasible
     slices (V typ '+' |a| = 3 mB = 4 top/bottom; H mu = +-1 bottom mB = 5, fractional mixtures of top207, d2_459, d2_4710) with NO
     integer multiset (MILP, f1milp2.py); mB >= 31: LHS - 4 mB < b' (26 exact certificates, f1large_t300.log) => impossible.
     => F1 is EMPTY at order 3 for every multiset of boxes from the top-300 and d2pos classes, any rational part (PROVED except
     4 MILP slices: CHECKED).
 5.6 J2 (exact_run.py): one box from each of the 24 open d2 classes (<= 10 boxes per class) x n = 1 (R(6)), n = 2 (R(5)),
     n = 3 (R(4)) rational boxes: 215,016 products, 3,651,354 Lemma-W candidates, 0 UNITS, 0 double-gate passers, min span J 15.
 5.7 ORDER-3 AT THE TWO-ENDED TIES (tie3.py; H mu = +-1 tie, ONE a-potential d2 box, n = delta + 3 = 2 pinned): 160 box-level
     instances.  T3 (both ends r >= 3) needs the tau-law n = tau(B) - tau* (tau* = -1): it contradicts the delta-law in ALL 160
     (PROVED per box).  T2 (one end stops at r = 2 with D2 = tau* - tau(B) + n != 0): the first Phi_3 condition at that end,
     D3 = D2 (1 - X1) (linear for fixed k, n), CLOSES the case when the weak end is the box's generic end and leaves it open exactly
     when the weak end is the box's a-POSITIVE end (80 + 80).  So the surviving frontier is pinned to ONE end of ONE box: the
     a-positive end must carry an r = 2 weak end whose u^2-coefficient (order-4 data, K = 4 automaton, X1 sliced) is the next test.
 5.8 J3 (exact_run.py): the 900 open d2 x top-50 class pairs (<= 6 d2 boxes x 3 top boxes per pair) with n = 0 and n = 1 (R(4)):
     147,900 products, 2,845,364 candidates, 0 UNITS, 0 double-gate passers, min span J 23.
 5.9 THE MIRROR CASE F1' = 'd=1 e=-1' (offset +1, eps = -1; needs a-potential X1 = 2; the order-2 frontier of H mu = +-2).
     Same mechanism: X2 = 2 + mB is pinned and the u^3 coefficient gives l3(s1) - l2(s2) = mB^2/2 - 4/3 (PROVED).  Uniform over
     the 3,735 order-3 subclasses of top-300 + d2pos (f1b.py), |mB| <= 30: 1,464 slice-LPs, 1,412 closed at order 2, 49 by the
     order-3 equality, 3 OPEN:
       H mu = +2, weak TOP, mB = -7:  k = 3 x box 50216 (class d2_497, a-potential at the top; tree
            ('n',2,[('p',[('n',-2,[xy,xy]),y]),xy,Y]) ), INTEGER, and among n = 0..7 only n = 2 rational boxes is feasible;
       H mu = -2, weak BOTTOM, mB = -7: the mirror, 3 x box 50139 (class d2_460), n = 2;
       H mu = -2, bottom, mB = -8: fractional only.
     |mB| >= 31 (f1b_large.py): 42/44 (family, sign) cases closed EXACTLY; OPEN (LP unbounded): H mu = +2 top and mu = -2 bottom
     with mB <= -31, i.e. >= 15 aligned a-potential boxes (sigma = -2 each).  GAP.
     => SURVIVORS OF ORDER 3 (sharpest frontier found): B^3 u_1 u_2 with B = box 50216 (resp. 50139), closure X^{+2} (resp.
        X^{-2}), and the long tail of >= 15 aligned a-potential factors at mu = +-2.
 5.10 EXACT SEARCH OF THE F1' SURVIVORS (probe_exact.py): B^3 u_1..u_n with B = box 50216 and B = box 50139, u_i in R(5),
     n = 1, 2, 3: 24,680 products, 637,788 Lemma-W candidates (all mu, N), 0 UNITS, 0 double-gate passers, min span J = 40
     (mu = 1); with u_1, u_2 in R(6) (n = 2, the only LP-feasible n): 9,702 products, 237,306 candidates, 0 UNITS, min span 44.
     The jet-level survival is not accompanied by any global cancellation in these samples.
 5.11 J4 (triples of d2 boxes from the 22 classes of the open d2 x d2 pairs, 2 boxes per class): n = 0: 11,357 products,
     200,572 candidates, 0 UNITS, 0 double-gate passers, min span J 34; n = 1 (R(4)): 181,712 products, 4,410,173 candidates,
     0 UNITS, 0 double-gate passers, min span J 37.
 TOTAL EXACT FRONTIER SEARCH: 846,517 products, 17,795,073 Lemma-W candidates (every mu, odd a, N in the windows): 0 UNITS,
     0 candidates with a_2 = 0 and J(zeta_10) = 1; smallest span J anywhere 15 (J2).  NO HIT.

## 6. Mechanisms (what the LP says, in words)
 M-ADD (PROVED): every quantity the order-2 weak-end casework uses is additive over factors, so non-flatness for a class set is
   one LP over the multiplicity cone; the Farkas vector is a 'potential' (a linear functional on per-box end data) that is
   nonnegative on every class in S and on the rational automaton.  For the top-300 classes such a potential exists for all 24 x 11
   weak-end cases at once: adding factors never helps, because generic classes behave like rational boxes (Lemma Z) and the
   delta-law bounds the number of factors in the d=0 cases.
 M-PHI (PROVED): phi = rho_a + rho_q/2 <= -1/2 per box for rational boxes and top classes; this single functional kills the vertical
   d=0 cases for every slope mismatch mB (no slicing needed beyond |mB| <= 3).
 M-POT (CHECKED): the only way to defeat the order-2 casework is POSITIVE end potential (rho_b = +1 or rho_a = +1), available only
   at depth 2 (the 60 d2pos classes, one positive end each).  The universal open case is offset -1 at the weak end with l1(s2) = 2:
   it needs (2 - q1) units of b-potential at ONE end, i.e. >= 1-2 positive-potential boxes on the same side; after that the order-2
   data cannot exclude adding any number of generic/rational factors (unbounded open region).  Second unbounded family: vertical
   d=0 r=1 with a-potential boxes (sigma = -1, -2).
 So the arborescent frontier at jet order 2 is exactly: products with positive-potential factors aligned at one end (F1/F2 above);
 everything built from generic/top-300 factors is closed by theorem.
 M-ORDER3 (PROVED lemma; CHECKED runs): in the one-ended offset cases F1 / F1' the order-1/2 conditions PIN X1 (resp. X2) to
   2 -+ mB, so the u^3 coefficient of the Phi_3 pattern becomes an affine EQUALITY l3 - l2 = mB^2/2 - 4/3; its right side grows
   quadratically in mB while the left side grows at most linearly on the order-2 region, so it kills F1 for all multisets and F1'
   except two 3-box configurations.  What survives is TWO-ENDED (ties, d=0 r=1) and pinned to the a-positive end of a factor.


## 7. GAPs and next targets
 GAP-A (two-ended families, the real frontier after order 3): a-potential d2 classes (rho_a = +1 at one end, sigma = -1/-2) in
   d=0 / tie configurations: H mu = +-1 tie (n pinned = delta.k + 3) and 'd=0 r=1', V 'd=0 r=1' (mB = +-1) and the V tie (mB = 0),
   plus their multisets.  Next lemma (derived, not yet in the generator): at a two-ended tie with the tau-law violated
   (sum tau_j - n != tau*), one end stops at r = 2 exactly; with d_i = l_i(s1) - l_i(s2) at that end (d_1 = 0, d_2 != 0 known from
   tau) the Phi_3 pattern needs  d_3/d_2 + X1 = 1  (linear in the rational l3(q) sums and alpha for fixed k) and
   (d_4 - d_2^2/2)/d_2 + X1 d_3/d_2 + x_2(s1) = 1 (needs the K = 4 automaton, quadratic in X1: slice X1).  Same mechanism as 5.2.
 GAP-B: horizontal/vertical d=0 slices are exact only for the class sets tested; THEOREM M300 uses the phi-lemma (top-300 only).
 GAP-C: the order-3 closure of F1 (5.5/5.5') uses the K = 3 automaton and box-level l3 data (claims are for the listed library
   boxes); 2 (top-50) resp. 4 (top-300) slices rest on MILP verdicts.  F1' (5.9): two integer survivors and the tail mB <= -31.
 GAP-D: 'open' verdicts are LP-feasibility in the relaxation (n * conv of automaton paths): they mean 'no certificate of this
   order', not that a unit exists; the exact searches (5.1, 5.6, 5.8, 5.10, 5.11) found none.
 NOT CLAIMED: d2fix2 (two d2 boxes + any top-300 multiset) and the first J4/probe runs were killed externally at 04:38.
 CAVEAT (inherited): every theorem here is conditional on C1's framework being sound (Lemma W, BX1-BX4/BX4', T2, the K = 3 jet
   automaton, R2 mirror for bottom data); refGen (round D) is refereeing that framework.

## 8. Files (all in this folder)
 lpg.py (case rows affine in end data, LP assembly with automaton flows, exact Farkas extraction/verification), runner.py,
 classes.py (jet classes from C1's gen2_res.pkl), val1.py / val2.py (validation), run_uni.py (uniform runs; uni_*.pkl, uni_*.log),
 certs300.py + certs_M300.pkl (THEOREM M300 certificates), pairs_d2.py + pairs_d2.pkl, d2fix.py (+ d2fix1.pkl/.log), d2fix2.py (killed),
 f1o3.py (order-3 lemma for F1), f1uni.py (+ f1uni_30_*.pkl), f1bound.py, f1large.py, f1milp.py / f1milp2.py (+ logs), f1b.py,
 f1b_large.py, f1b_probe.py (mirror case F1'), tie3.py (order-3 at ties), exact.py / exact_run.py (+ exact_J*.pkl, exact_run*.log),
 probe_exact.py (+ probe_exact*.pkl/log), verify_unit.py (HIT protocol helper), ana.py, tail_sections.md (report fragment),
 c1copy/ (unchanged copies of C1 modules; only sys.path lines changed).
