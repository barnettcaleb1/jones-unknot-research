# refV3 NOTES (referee of THEOREM V3, engine C1 REPORT section 2)
17 Nov 2026, Claude (referee refV3). Folder ~/jones-lanes/theory-restart/mont/cx/roundD/refV3/ .
Marks: PROVED / CHECKED(n) / CONJECTURE / GAP / FALSE.  Running log; final verdicts go to REPORT.md.

## 0. Read so far (03:30)
- BRIEF, engineC1 REPORT (sec 1,2), engineA REPORT (Lemma W, D1, Lemma S, V2, GAP1), notie REPORT (R0-R2, BX1-BX4, N1-N5),
  nest REPORT sec 4 (Theorem V).

## 1. Proof-structure audit of V3 (by hand, 03:45)
Setup re-derived: Theorem V gives F := J Phi_3 (=.) = w_1(a) A + wV(a) t^-3N B, w_1 = t + (1+t^2)(-t)^a, wV = (-t)^a t + t^(3a-1) Phi_5.
 - Top data re-derived by hand: a>=3: w_1 = -t^(a+2)(1+0u+u^2+0u^3..), wV = t^(3a+3)(1+u+u^2+u^3+u^4+0..);
   a<=-3: w_1 = t(1+0u-[|a|=3]u^2 ..), wV = -t^(a+1)(1+O(u^4)).  OK.
 - Mirror for VERTICAL closures re-derived: bar w_1(a) = t^-2 w_1(-a), bar wV(a) = t^-2 wV(-a); with notie R2 for boxes
   bar F(a,N;u) = t^(-2-4K) F(-a, n-N; u'').  So the class is mirror-closed and 'weak top' WLOG is legitimate.  OK.
 - sigma* (vertical, |a|>=3) = -1 re-derived at both signs of a (a>=3: top -1, bottom 0; a<=-3: top 0, bottom -1). OK.
 - Lemma W: elementary, correct (needs span S_i >= 3; span A >= 4n, span B = span A - n). OK.
 - Weak-end mismatch: s1_w(Q)-s1_w(q*) = [sigma(Q)-sigma(q*)] - [s1_s(Q)-s1_s(q*)] = (0-(-1)) - 0 = +1, valid whenever the
   strong end has r >= 2.  Strong end has r >= Tot-1 (both ends coincide; V2) or r >= Tot (one end).  Tot >= 4n+4-2.  OK.
 - Weak top pins P = sum rho_q = 0 (a>=3) / 1 (a<=-3).  OK.
 - Case table re-derived independently (log-jet algebra x2 = l2 + l1^2/2):
   delta>=2 OK; delta=1 OK (simpler: alpha=0 => all alternating S_0-top => P=-n, contradiction for every n>=1);
   delta=0,eps=+1 OK; delta=0,r=1: condition M2-L2 = 1/2 - L1 re-derived => sum(lambda_q+rho_a) = 1 (a>=3), 1/2-[|a|=3] (a<=-3). OK;
   delta=-1 a<=-3 OK (also P=n forces n=1, then x2 <= -2); delta=-1 a>=3: forces n=2 (if n>=2) and sum l2(b)=3/2 vs <= -3/2. OK;
   delta=-2, <=-3 OK (also P=n != 0).
 - NOTE: the hand proof's delta=-1, a>=3 subcase uses n>=2.  For n=1 the configuration is ONE box with rho_a=rho_b=-1
   (R_0- or S_{>=1}-top) and needs l2(b)=3/2: NOT treated in sec 2 (only via the certificate generator with n_min=1). See below.

## 2. Lemma status by hand (03:55)
 - T2 has a SHORT HAND PROOF (no automaton needed): lambda_q depends only on the top class (all R_1 states have
   r = t^-1(1+u+u^2+..) since every entry into R_1 has r_pre = t^-3(1+O(u^3)); R_0 has r = t^-1(1+0u-c_prev u^2..)
   => lambda_q = -1-c_prev in {-1,-2}; S_0 always has r = t^-4(1+0u+..) => lambda_q = -1/2; S_1: q = 1+u^2+..
   => +1; S_2: q = 1-u^3 => 0; S_{>=3}: 0) and BX3 gives rho_a <= -1 for every class except S_0 (rho_a <= 0;
   S_{>=1} is entered only by the Psi-decreasing step S_0 -(-1)-> S_1).  Hence lambda_q + rho_a <= 0 with the
   per-class bounds of the REPORT.  PROVED (by hand) + automaton.
 - BX4' hand proof in the REPORT is correct (re-derived: Psi-preserving path ending in R_1 = alternating ending positive;
   q = -t^2(1+u+0u^2..) => l2(q) = -1/2; l2(a) from BX4).  PROVED.
 - n = 1 (|a|>=3): the hand proof of sec. 2 does NOT cover delta=-1, a>=3 at n=1 (needs one box with rho_a=rho_b=-1,
   l2(b)=3/2).  C1 closes it only with the automaton certificate y=(100,100,1): sup over boxes of
   200 rho_a + 101 rho_q + 100 l2(a) + 100 lambda_q = -150.  NEW HAND LEMMA BX5 (this referee):
     rho_a = -1 and top class R_0  => path = alternating..R_1, then (+1)(+1)^j'  => l2(b) = -(k_alt-[m0<=-2])/2 - 1 (j'=0),
                                      -(k_alt-[m0<=-2])/2 (j'>=1)  <= -1/2;
     rho_a = -1 and top class S_{j>=1} => path = alternating..S_0, then (-1)^j  => l2(b) = 1/2 - (k_alt-[m0<=-2])/2 <= 1/2
   (D-jets: S_0->S_1: t^4(1-u+0u^2), l2 = -1/2; S_1->S_2: t^4(1+0u+u^2), l2 = +1; S_2->S_3: l2 = 0; R_1-(+1)->R_0:
   -t(1+0u+u^2), l2 = +1; R_0-(+1)->R_0: l2 = 0).  So l2(b) <= 1/2 < 3/2: the n=1 case closes BY HAND.  To be CHECKED exactly.

## 3. Exact checks (04:10)
 - boxlemmas.py (exact Laurent arithmetic on normal forms, NO automaton): sum|m_i| <= 10: 39,365 boxes; <= 12: 354,293 boxes.
   BX1 (lc, classes), BX3 (+ both equality characterisations), BX4 (exact formula), BX4' (exact formula -(k-[m0<=-2]+1)/2),
   T2 + per-class bounds (attained: R1 -3/2, R0 -2, S0 -1/2, S1 0, S2 -1, S3+ -1), BX5 (exact formulas, max l2(b) = 1/2),
   C1 n=1 certificate sup (= -150 exactly), Lemma S (delta, lc, sigma), S3 tau = -1, R2 (bottom = top of mirror), span a >= 4:
   0 FAILURES at both sizes.  CHECKED(39,365) and CHECKED(354,293).
 - boxlemmas_R.py on the word library: R(8) 576 boxes, R(10) 3,362 boxes, both ends: 0 FAILURES.  CHECKED.
 - brute.py (no Lemma W; mod-(2^31-1) and mod-(2^19-1) evaluation at t=2 = exact necessary condition, survivors re-tested
   exactly): n=1: 24,500; n=2: 1,212,750; n=3: 40,425,000 (multiset,a,N): exact units ONLY at n=1, a=+-1 (20; all 2-bridge
   unknots: lp.J = 1, det = |D(2)| = |D(3)| = 1).  n=4 running.
 - lpcheck.py (formula vs lp.J on explicit half-words, parallel): 250/622 done, 0 mismatches so far.
 - brute.py n=4 DONE: total n=1..4: 1,062,393,500 (multiset, a, N) cases [n=4: 1,020,731,250], 24 mod-p survivors, exact units
   ONLY the 20 at n=1, a=+-1 (2-bridge unknots).  => test (i): V3 CHECKED on the full requested region (formula level).
 - chain.py: w-jets of w_1, wV (top+bottom, odd 3<=|a|<=41) agree with the REPORT's top data AND with the generator's hardcoded
   wdata; sigma*_V = -1, delta*_V = -|a|-1 for all.  20,000 random closures (R(8), n=1..5, odd 3<=|a|<=15, N forced into a
   Lemma-W coincidence 90%): 1,037 strong ends (r>=2): weak-end mismatch = +1 in 1037/1037, P = s1(q*)+1 in 1037/1037,
   two-ended r>=2: 0 (V2), units 0.  CHECKED.
 - lpcheck.py seed 7: 622 explicit half-words (all 20 units, 2 non-unit survivors, 600 random: 150 each n=1..4, odd |a|<=9,
   |N|<=12): lp.J == formula in 622/622; the 20 units have lp.J = 1 and det = |D(2)| = |D(3)| = 1 (2-bridge => unknot).
 - wcheck.py (Lemma-W windows as CROSS-CHECK only): all multisets n<=3 + 20,000 random n=4, FULL a-window, N in {N_top,N_bot}:
   2,495,784 candidates, units = the same 20 (n=1, a=+-1), none outside |a|<=9, |N|<=12.  Consistent with brute.py.
 - autocheck.py: C1's K=3 automaton (copy) vs exact Laurent computation on 39,365 normal forms (sum|m|<=10, exponents up to 10
   exercise the clipping m -> +-6): final key (r-jet, rel. order 3) and log-jet of a: 0 mismatches.
 - v3lemmas.py (copy) output reproduces the REPORT's P1-P6 numbers (19 states/227 edges; T2 class maxima; Psi-preserving maxima).
 - n=0 (integral body, vertical pretzels P(a,q,a)): exact scan odd |a|<=101, |N|<=150: units only at a=+-1 (N in {0,1}/{-1,0},
   unknots); none for |a|>=3 (min span 4 at |a|=3).  Not part of V3 (needs n>=1); C1's 'every depth-one quotient' claim omits it.
 - Lemma W a-window re-derived by block separation: with an end coincidence (Lemma W), for a >= 3 the blocks P1 = tA,
   P2 = -t^a(1+t^2)A, P3 = -t^(a+1)B_N, P4 = t^(3a-1)Phi_5 B_N leave P1 (top tie) or P2 (bottom tie) isolated once
   a > max(span A, span B) + 3, so units need |a| <= max(span A, span B) + 3 (engineA's +8 is safe).  NOT used by V3.
 - load average ~93 (other agents); my parallel runs slowed.

## 4. Branch-knot implication (04:20) -- IMPORTANT side finding
 1.3: V(L_m) = t^(12 j [m odd]) {1 + (1-(-t)^-m) Phi_3 G}, G = (J-1)/(1+t)^2, j = -J'(1)/8.
 Even m: V(L_m) = 1 <=> J = 1.  Odd m: V(L_m) = 1 <=> J = J_*(m,j) := 1 + (1+t)^2 (t^(-12j)-1)/((1+t^-m) Phi_3), j != 0.
 Computed: a_2(J_*) = -J''(-1)/24 = j/m (h(-1) = -12j/m), and J_*'(1) = -8j automatically; c_1(L_m) = 12j - 12 m a_2 = 0 is
 then automatic, and Mullins (as an identity in ft/core's conventions) adds nothing.  Example: J_*(1,1) = t^-2 - t^-3 + t^-5 - t^-6
 + t^-8 - t^-9 + t^-11 (a_2 = 1), D_7 | J_* - 1, J_*(1) = 1.  So:
  - V3 => V(L_m) != 1 for every EVEN m and for odd m unless J = J_*(m, j) with j = m a_2(K) != 0 (at most one odd m).
    C1's 'every n != 0' is OVERSTATED (ft BRIEF 1.3 itself flags this).  GAP (G2).
  - PROGRAM FLAG: a nontrivial (K,h) with J = J_*(m,j) would give a nontrivial L_m with V = 1 (a Jones counterexample) and has
    a_2 = j/m != 0.  The cx BRIEF's hit criterion is only J = 1 and its pruning 'a_2(K) != 0 is PROVEN-EMPTY' is valid only
    for that criterion; J_* hits live exactly in the pruned region.
 Detector jstar_hit (degree count fixes m: m = top(PG) - max(0,-12j) if < 0, or bot(PG) - min(0,-12j) if > 0, PG = Phi_3 G),
 self-tested on synthetic J_*(1,1) and J_*(-3,-1): detected.  Running on all n <= 2 closures (exact) + 100k random n = 3,4.
 - jstar.py DONE (n <= 2 exhaustive, EXACT J for all 1,237,250 closures, odd |a| <= 9, |N| <= 12): normalisation never fails;
   units = the 20 (n=1, a=+-1); J_* loophole hits: 0; min span (|a|>=3): n=1: 8 (|a|=3), 13, 15, 20; n=2: 11, 15, 18, 23;
   26,094 non-unit closures with a_2 = 0 (min span 9); deepest one-ended cancellation 5 orders; two-ended: none (n <= 2 < |a|+1).
 - jstar34.py: 100,000 random n=3,4 exact closures: 0 units, 0 J_* hits, min span 17.
 - brute2 (R(5), n=4,5,6, odd |a|<=11, |N|<=15): n=4 45.9M and n=5 404.0M tested, 0 survivors; n=6 running.
 - lpdeep.py DONE: 60 deepest one-ended-cancellation closures (|a|>=3, n=1..4, depth up to 5): lp.J == formula 60/60.
 - brute2 DONE: R(5), n=4,5,6, odd |a|<=11, |N|<=15: 3,479,865,816 closures, 0 survivors, 0 units.
 - REPORT.md FINAL written 04:40.
