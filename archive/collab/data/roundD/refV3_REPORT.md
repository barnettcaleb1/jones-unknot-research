# REFEREE refV3: THEOREM V3 (engine C1 REPORT section 2)
17 Nov 2026, Claude (referee refV3, round D). Folder ~/jones-lanes/theory-restart/mont/cx/roundD/refV3/ (scripts in src/, logs and
pickles here, running log NOTES.md).  Marks: PROVED / CHECKED(n) / CONJECTURE / GAP / FALSE.   STATUS: FINAL (04:40).  All runs complete.

## 0. VERDICT (short)
THEOREM V3 is CORRECT as an algebraic statement about Theorem V's closure formula, for n >= 2 (every odd a) and for n >= 1 when
|a| >= 3.  Every step of C1's proof checks out; the case analysis was re-derived independently (log-jet algebra) and matches both
the hand proof and the generator's encoded cases.  Two lemmas C1 calls 'PROVED by automaton' have SHORT HAND PROOFS (T2) or a
correct hand proof already in the REPORT (BX4').  The n = 1 extension (|a| >= 3) is NOT covered by the hand proof of section 2
(the delta = -1, a >= 3 sub-case forces n = 2 only when n >= 2); C1 closes it with an automaton Farkas certificate.  This referee
supplies a hand proof (new Lemma BX5 below), so the n = 1 extension is PROVED by hand too.
No counterexample: exhaustive search of the requested region (1,062,393,500 closures) finds units ONLY at n = 1, a = +-1 (2-bridge
unknots, excluded by the statement).  Caveats (GAPs, none inside V3's algebra):
 (G1) V3 is about the formula of Theorem V, which is PROVED only modulo the skein dictionary (nest REPORT, open item 1); here CHECKED
      against lp.J on 682 explicit half-words of the tested family (622 random + all units/survivors, 60 deepest cancellations;
      0 mismatches).
 (G2) C1's 'WHAT IT IMPLIES' overstates the branch-knot consequence: J != 1 gives V(L_m) != 1 for every EVEN m, but for ODD m
      V(L_m) = 1 <=> J = J_*(m,j) := 1 + (1+t)^2 (t^-12j - 1)/((1+t^-m) Phi_3) with j = -J'(1)/8 = m a_2(K) != 0, 3 not dividing m
      (ft BRIEF 1.3, 'Astra's formal counterexample').  V3 does not exclude J = J_*.  (CHECKED: no J_* among all n <= 2 closures
      and 100,000 random n = 3, 4 closures.)  See also R1: J_* would be a genuine Jones counterexample the BRIEF's pruning misses.
 (G3) C1's section-5 sentence 'every depth-one arborescent quotient has J != 1' omits the vertical n = 0 bodies (integral middle:
      the pretzels P(a, q, a) with their vertical inversion); V3 needs n >= 1.  (See section 6.)

## 1. What exactly is claimed and what is proved
 Notation (C1/engineA): u_i = u(m_0..m_{k-1}) non-integral rational boxes (normal forms, k >= 1), A = prod a(u_i), B = prod b(u_i),
 Q = t^-3N B/A, w_1(a) = t + (1+t^2)(-t)^a, wV(a) = (-t)^a t + t^(3a-1) Phi_5, q* = -w_1/wV, and by Theorem V
     J(s.l1.(Y^N u_1...u_n).(x2)^a.u1) Phi_3  =.  F := w_1(a) A + wV(a) t^-3N B.
 THEOREM V3 (as refereed).  For odd a and any N, F is not +-t^e Phi_3 (so J is not a unit, the closure is not flat) when
   (i) n >= 2 and |a| >= 3            [C1 section 2, hand proof]                              PROVED (re-derived);
   (ii) n >= 1 and |a| >= 3            [C1: automaton certificate of section 2b]             PROVED (C1: computer-assisted;
                                                                                           this referee: by hand, Lemma BX5);
   (iii) n >= 2 and a = +-1            [wV(+-1) = t^(+-3) w_3(+-1): a mu = +-1 necklace; Q-MONT] PROVED modulo Q-MONT (notie).
 n = 1, a = +-1 is genuinely excluded (2-bridge unknots occur; 20 found in R(6), all J = 1, det = |D(2)| = |D(3)| = 1).

## 2. Step-by-step audit of the proof (every step re-derived by hand; all CHECKED as noted)
 S0 Theorem V (the 3-channel formula) .......... upstream; PROVED modulo the skein dictionary (nest open item 1) => GAP (G1) for the
    topological reading only.  CHECKED here: formula = lp.J on 622 explicit half-words of this very family (all n = 1..4, odd |a|
    <= 9, |N| <= 12, incl. all units/survivors), 0 mismatches.
 S1 Mirror reduction to a weak TOP .............. PROVED.  Re-derived for VERTICAL closures: bar w_1(a) = t^-2 w_1(-a),
    bar wV(a) = t^-2 wV(-a), so with notie R2  bar F(a,N;u) = t^(-2-4K) F(-a, n-N; u''); the hypothesis class is mirror-closed.
 S2 Lemma W (some end coincides; leading terms cancel at a lone coincident end) ... PROVED (elementary; needs span S_i >= 3: span S1 >=
    span w_1 >= |a|+1 >= 4 for |a|>=3 [>= 2 for a = +-1 handled by Q-MONT], span S2 >= span wV = 2|a|+2).
    The a/N WINDOWS of engineA's corollary are NOT used by V3.  (Re-derived anyway: with an end tie, for a >= 3 the block P1 = tA
    (top tie) or P2 = -t^a(1+t^2)A (bottom tie) is isolated once a > max(span A, span B) + 3; engineA's '+8' is safe.)
 S3 r_top + r_bot = Tot := span(w_1 A) - 2 at a unit, r >= Tot at a lone coincident end ... PROVED (F = -w_1 A (Q/q* - 1)).
 S4 Theorem V2 (no two-ended order-2 tie) ....... PROVED: sigma is additive, sigma(u) = 0 for every rational box (Lemma S),
    sigma*_V(a) = -1 for all odd |a| >= 3 (re-derived: a >= 3: top -1, bottom 0; a <= -3: top 0, bottom -1).  CHECKED: 20,000
    random closures (R(8), n = 1..5, odd 3 <= |a| <= 15, 90% with forced end coincidence): no closure with r >= 2 at both ends.
 S5 Weak-end mismatch = +1 ........................ PROVED: s1_w(Q) - s1_w(q*) = [sigma(Q) - sigma*] - [s1_s(Q) - s1_s(q*)] = 1 - 0
    whenever the strong end has r >= 2 (true: r >= Tot - 1 >= 5 in every unit configuration, n >= 1, |a| >= 3).
    CHECKED: 1,037 / 1,037 strong ends in the random sample (mismatch exactly +1; P = s1(q*) + 1 exactly).
 S6 P pinned: P = sum rho_q = 0 (a >= 3) / 1 (a <= -3) at the weak top ... PROVED.
 S7 Top data of w_1, wV ......................... PROVED; CHECKED exactly for all odd 3 <= |a| <= 41 at both ends against the
    REPORT text AND against the generator's hard-coded wdata (v3b.wdata): 0 discrepancies.
 S8 Offset / tie cases (normalised expansion of F must be 1 + u + u^2 + 0u^3): re-derived from x2 = l2 + l1^2/2:
    delta >= 2: x1(F) = alpha <= 0 (BX3).                                                           PROVED (any n)
    delta = 1: needs alpha = 0, eps = 1 => all boxes alternating S_0-top => P = -n, contradicting P in {0,1}. (C1's x2-argument
      needs n >= 2 for a >= 3; the P-argument works for every n >= 1.)                                PROVED (any n)
    delta = 0, eps = +1 (r = 0): x1(F) = (x1(s1)+x1(s2))/2 <= 1/2.                                     PROVED (any n)
    delta = 0, r = 1: x2(s1) - x2(s2) = -1 <=> sum(lambda_q + rho_a) = 1 (a >= 3), 1/2 - [|a|=3] (a <= -3); T2 kills a >= 3 and
      a <= -5; a = -3: P = 1 => #R_1 = #S_0 + 1 >= 1 => sum <= -3/2.                                 PROVED (any n)
    delta = -1, a <= -3: beta = 0 => all R_1-alternating => P = n => n = 1, then x2(F) = sum l2(b) - n <= -2.   PROVED (any n)
    delta = -1, a >= 3: eps = 1, beta = alpha = -1.  n >= 2: forces n = 2, {alternating S_0-box, alternating R_1-box},
      needs sum l2(b) = 3/2 but BX4 + lambda_q(S_0) = -1/2 and BX4' give <= -3/2.                    PROVED (n >= 2)
      n = 1: ONE box with rho_a = -1, rho_q = 0 (top class R_0 or S_{>=1}) needing l2(b) = 3/2.  NOT in C1's hand proof;
      C1 closes it by the certificate 'sup over boxes of 200 rho_a + 101 rho_q + 100 l2(a) + 100 lambda_q = -150' (automaton).
      Hand proof here: Lemma BX5 (section 3) gives l2(b) <= 1/2.                                     PROVED (n = 1)
    delta = -2: a <= -3: x1 = beta <= 0; a >= 3: beta = 0 => P = n != 0.                             PROVED (any n)
    delta <= -3: as delta = -2.                                                                      PROVED (any n)
    All cases also agree with the generator's encoded equations (v3b.cases), which I re-derived line by line.

## 3. The lemmas: proved for ALL rational boxes, or only checked?
 (Exact checks: boxlemmas.py = exact Laurent arithmetic on ALL normal forms u(m_0..m_{k-1}) with sum|m_i| <= 12, i.e. 354,293 boxes,
  exponents up to 12 > the automaton's clipping bound 6; boxlemmas_R.py = the word library R(10), 3,362 boxes, both ends.  0 failures.)
 Lemma S (delta = -1, sigma = 0, lc_top lc_bot = -1) ... PROVED (BX2 + R2; I re-checked the R_1 <-> S_0, R_0 <-> S_{>=1} pairing
    under u -> u'' including k = 1, 2).  CHECKED(354,293 + 3,362), and S3 (tau = -1) CHECKED on the same sets.
 BX3 (Psi = rho_a + phi non-increasing; rho_a <= -1 on R-top, <= 0 on S-top, rho_b <= 0; equality characterisations) ... PROVED
    (notie; every BX2 row re-derived by hand); CHECKED(354,293) including both equality characterisations.
 BX4 (alternating S-boxes: l2(a) = -(k - [m_0<=-2])/2) ... PROVED (notie); CHECKED exactly.
 BX4' ... PROVED BY AN ARGUMENT for all boxes (C1's hand proof is correct: Psi-preserving path ending in R_1 = alternating ending
    positive; every entry into R_1 has r_pre = t^-3(1+O(u^3)), so r = t^-1(1+u+u^2+..), q = -t^2(1+u+0u^2+..), l2(q) = -1/2;
    l2(a) from BX4).  CHECKED: the EXACT formula l2(b) = -(k - [m_0<=-2] + 1)/2 on all 354,293 boxes; converse (alternating
    ending positive => rho_a = -1) too.
 T2 (lambda_q + rho_a <= 0; <= -3/2 R_1, -2 R_0, -1/2 S_0, 0 S_1, -1 S_2, S_{>=3}) ... C1: PROVED by automaton longest paths
    (computer-assisted).  It ALSO has a short hand proof (this referee), so it does not depend on the automaton:
      (a) lambda_q is a function of the top class.  R state r = t^-1(1 + c1 u + c2 u^2 ..) gives q = -t^2(1 + c1 u + (c2-1)u^2 ..).
          Entry into R_1 (from init / S_j by n >= 1, from R by n >= 2): r_pre = t^-3(1+O(u^3)), D = -t(1-u+O(u^3)),
          r = t^-1(1+u+u^2+O(u^3)) => lambda_q = -1/2.  Entry into R_0 (from R_c by +1): r_pre = t^-3(1+u+cu^2..),
          D = -t(1+0u+cu^2..), r = t^-1(1+0u-cu^2..) => lambda_q = -1-c in {-1,-2}.  S_0 (all three entries): r = t^-4(1+0u+..)
          => q = 1-u+0u^2.. => lambda_q = -1/2.  S_1 (only from S_0 by -1): D = t^4(1-u..), r = -t^-5(1+u..) => q = 1+u^2+..
          => +1.  S_2: q = 1-u^3.. => 0.  S_{>=3}: q = 1+O(u^4) => 0.
      (b) BX3: rho_a <= -1 except on S_0 (rho_a <= 0), because S_{j>=1} is entered only through S_0 -(-1)-> S_1, a Psi-drop.
      (c) Combine.  []   CHECKED(354,293 + R(10)); every class bound is attained.
 BX5 (NEW, needed only for n = 1): if rho_a = -1 and rho_q = 0 (top class R_0 or S_{j>=1}) then l2(b) <= 1/2.  PROVED:
      R_0: Psi(R_0) = rho_a + 1 = 0, so the path is Psi-preserving: alternating up to R_1 (k_alt steps), then +1, then (+1)^j'
          (R_0 is entered only by +1 from R and left Psi-preservingly only by +1).  D-jets: R_1 -(+1)-> R_0: -t(1+0u+u^2..), l2 = +1;
          R_0 -(+1)-> R_0: -t(1+0u+0u^2..), l2 = 0.  So l2(b) = -(k_alt - [m_0<=-2])/2 + 1 + lambda_q, lambda_q = -2 (j'=0) or -1,
          hence l2(b) <= -1/2.
      S_{j>=1}: Psi = -1, one Psi-drop, necessarily the final S_0 -(-1)-> S_1; so: alternating up to S_0 (k_alt steps), then
          (-1)^j.  D-jets: S_0->S_1: t^4(1-u+0u^2), l2 = -1/2;  S_1->S_2: t^4(1+0u+u^2), l2 = +1;  S_i->S_{i+1} (i>=2): l2 = 0.
          lambda_q = 1, 0, 0 for S_1, S_2, S_{>=3}.  So l2(b) = 1/2 - (k_alt - [m_0<=-2])/2 <= 1/2 for every j >= 1.  []
      CHECKED: both exact formulas on all 354,293 boxes; max l2(b) = 1/2 (S), -1/2 (R_0), attained by u(m_0,-1,..,-1), m_0 <= -2.
      With BX5 the single n = 1 case missing from C1's hand proof (delta = -1, a >= 3: one box with rho_a = rho_b = -1 needs
      l2(b) = 3/2) is impossible.  C1's automaton certificate (sup = -150) is also CHECKED exactly on the 354,293 boxes (max -150).
 The jet automaton itself (jauto.py, K = 3, 19 states / 227 edges): soundness argument (absolute-precision tracking, assertions,
    exponent clipping M = 6) audited and found correct; CHECKED against exact computation on all 39,365 normal forms with
    sum|m_i| <= 10 (final key = exact r-jet to relative order 3, and log-jet of a): 0 mismatches.  So the computer-assisted parts
    of C1 are sound as far as I can see -- but V3 no longer depends on them.

## 4. Independent tests
 (i) BRUTE FORCE, requested region (brute.py; NO Lemma W in the search).  All multisets {u_1..u_n} of R(6) (98 canonical boxes),
   n = 1..4, every odd a in [-9,9], every N in [-12,12]: 1,062,393,500 closures (n = 4: 1,020,731,250).  Test = exact necessary
   condition for J = +-t^e: F(2) = +-2^e Phi_3(2) modulo 2^31-1 and modulo 2^19-1 (ord 2 = 31, 19); the 24 survivors were re-tested
   with exact Laurent arithmetic.  RESULT: units ONLY at n = 1, a = +-1 (20; all 2-bridge unknots: lp.J = 1, det = |D(2)| = |D(3)| = 1).
   No unit with n >= 2, none with |a| >= 3.  V3 CHECKED on the whole region (at the level of Theorem V's formula).
   Why not literally lp.J on each word: lp.J costs 0.03 - 8 s per word here (state sums on 18-52 letter words), ~10^9 words is out of
   reach.  Instead the formula was validated against lp.J on explicit half-words:
     lpcheck.py: 622 words (all 20 units, the 2 non-unit survivors, 600 random: 150 per n = 1..4, odd |a| <= 9, |N| <= 12): 622/622 equal.
     lpdeep.py: the 60 closures with the DEEPEST one-ended cancellation (|a| >= 3, n = 1..4, up to 5 orders): 60/60 equal.
   Exact J for EVERY closure with n <= 2 (jstar.py, 1,237,250 closures): no unit except the 20; minimal span for |a| >= 3 is 8
   (n = 1) and 11 (n = 2); deepest one-ended cancellation 5 orders; 26,094 non-unit closures with a_2 = 0 (min span 9).
   100,000 random exact n = 3, 4 closures (jstar34.py): no unit, min span 17.
   Lemma-W CROSS-CHECK (wcheck.py, engineA's eng.vclosures with its FULL a-window): all multisets n <= 3 + 20,000 random n = 4:
   2,495,784 candidates, units = exactly the same 20, none outside |a| <= 9, |N| <= 12.  Consistent.
   EXTENSION (brute2.py, R(5) = 40 boxes, n = 4, 5, 6 -- n = |a|+1 = 6 is where two-ended first-order ties occur for |a| = 5 --
   odd |a| <= 11, |N| <= 15): n = 4: 45,908,520, n = 5: 403,994,976, n = 6: 3,029,962,320 closures: 0 survivors, 0 units.
   Total closures tested exhaustively (i + extension): 4,542,259,316; units only the 20 excluded ones.
   n = 0 (integral body = vertical pretzels P(a,q,a), not in V3): exact scan odd |a| <= 101, |N| <= 150: units only at a = +-1.
 (ii) BOX LEMMAS EXACTLY (boxlemmas.py, no automaton): all normal forms with sum|m_i| <= 10 (39,365) and <= 12 (354,293), plus the
   word library R(10) (3,362 boxes) at both ends: BX1, BX3 (+ equality cases), BX4, BX4' (exact formula), T2 (+ all class bounds,
   each attained), BX5, Lemma S, S3, R2 (bottom = top of the mirror), span a >= 4, C1's n = 1 certificate sup: 0 failures.
 (iii) PROOF-CHAIN test (chain.py): w-jets for odd 3 <= |a| <= 41 (top and bottom) = REPORT text = generator's wdata; sigma*_V = -1,
   delta*_V = -|a|-1.  20,000 random closures (R(8), n = 1..5, odd 3 <= |a| <= 15, 90% with a forced Lemma-W coincidence):
   1,037 ends with r >= 2: weak-end mismatch exactly +1 and P = s1(q*) + 1 in 1,037/1,037; no two-ended r >= 2; no unit.
 (iv) AUTOMATON (autocheck.py): jauto K = 3 vs exact on 39,365 normal forms: 0 mismatches; v3lemmas.py reproduces P1-P6.

## 5. What V3 implies, precisely
 (a) CLOSURES.  Every half-word  s.l1.(y0)^N.B(w_1).B(w_2)...B(w_n).(x2)^a.u1   ((x0)^|N| if N < 0, (y2)^|a| if a < 0), B(w) the TH-2BR
     realisation of a rational box rho(w)e_1 with a(rho(w)e_1) not a unit (B(Yw) = y0.B(w), B(yw) = x0.B(w), B(Xw) = r2.x1.B(w).u1,
     B(xw) = r2.y1.B(w).u1), boxes repeatable, any order, any N, odd a, has J != unit, provided n >= 1 when |a| >= 3 and n >= 2 when
     a = +-1.  (By R0 every rational box is unit * Y^k * u(m_0..m_{k-1}), so this is ALL products of non-integral rational boxes
     with any integral part.)  NOT covered: n = 0 (vertical pretzels P(a,q,a); CHECKED here |a| <= 101, |N| <= 150, see G3);
     n = 1 with a = +-1 (2-bridge, TH-2BR; units = unknots occur); bodies with a non-rational factor (that is V3(B), C1 2b).
 (b) STRONGLY INVERTIBLE KNOTS.  For the (K,h) encoded by these half-words, J(K,h) != 1: none is a Lemma-Q counterexample.
     Topologically (nest REPORT sec. 2 Lemma L and sec. 4; NOT re-derived by this referee): K is the knot of the pretzel picture
     P(a, q, a) with the middle column (on the axis) replaced by the lift of the body, i.e. by the Montesinos tangle
     N + T_1 + ... + T_n of odd-denominator non-integral rational tangles T_i, and h is the rotation about the vertical axis
     exchanging the two outer columns of |a| crossings (a vertical / dihedral-type inversion).  n = 1: three-tangle Montesinos knots
     with two equal tangles of type 1/a and h exchanging them; n >= 2, |a| >= 3: arborescent non-Montesinos knots (the body's lift
     and the pair of 1/a columns are separated by a Conway sphere); a = +-1: Q-MONT's Montesinos knots with rho_h (as C1 says).
 (c) BRANCH KNOTS L_m = T(1/m) (m != 0) of these (K,h), by BRIEF/ft 1.3, V(L_m) = t^(12j[m odd]) {1 + (1-(-t)^-m) Phi_3 G},
     G = (J-1)/(1+t)^2, j = -J'(1)/8:
       every EVEN m: V(L_m) != 1 (PROVED from J != 1);
       ODD m: V(L_m) = 1  <=>  J = J_*(m,j) := 1 + (1+t)^2 (t^(-12j) - 1)/((1 + t^-m) Phi_3), j != 0.  I computed
       a_2(J_*) = j/m and J_*'(1) = -8j identically, so j = m a_2(K) != 0, and F1 (D_7 | J - 1) forces 3 not dividing m; at most one
       odd m per (K,h).  V3 does NOT exclude J = J_*, so C1's 'V(L_n) != 1 for every n != 0' is OVERSTATED (GAP G2; ft BRIEF 1.3 itself
       says 'the inference needs more').  CHECKED: no closure with J = J_* among all 1,237,250 closures with n <= 2 (exact) and
       100,000 random n = 3, 4 closures.  So: V(L_m) != 1 for all even m, and for odd m whenever a_2(K) = 0 or m does not divide
       j = -J'(1)/8 or J differs from J_*(m,j) (a one-line test per (K,h)).

## 6. Remarks for the program (outside V3, found while refereeing)
 R1 (J_* hits).  A nontrivial (K,h) with J = J_*(m,j) (odd m, 3 not dividing m, j = m a_2 != 0) would make L_m a NONTRIVIAL knot
    with V(L_m) = 1 (Gordon-Luecke), i.e. a counterexample to the Jones unknot conjecture.  Example target:
    J_*(1,1) = t^-11 - t^-9 + t^-8 - t^-6 + t^-5 - t^-3 + t^-2 (a_2 = 1, passes F1/D_7).  The cx BRIEF only counts J = 1 as a hit and
    lists 'a_2(K) != 0' as PROVEN-EMPTY; that pruning is valid for J = 1 only, and J_* hits live exactly in the pruned region.
    Note: Mullins-type constraints do not exclude J_*: V(L_m) = 1 forces c_1(L_m) = 12j - 12 m a_2 = 0 (ft/core), i.e. j = m a_2,
    and J_* satisfies exactly this (a_2(J_*) = j/m).  J_* also passes F1 for 3 not dividing m.  So either find a genuinely new
    exclusion (e.g. via the level-5 MOMENT-CYC10 link with V_K) or add 'J = J_*(m, -J'(1)/8) for some odd m' to the hit test
    (cheap: the degree count fixes m; detector jstar_hit in src/jstar.py, self-tested on J_*(1,1) and J_*(-3,-1)).
 R2 (scope of 'depth one').  C1 sec. 5 says every depth-one arborescent quotient is closed by theorem; the vertical n = 0 bodies are
    not covered by V3 (nor Q-MONT, TH-2BR).  They are CHECKED non-flat for odd |a| <= 101, |N| <= 150 (units only at a = +-1).
 R3 (the a-window of engineA's Lemma-W corollary, not used by V3): re-derived by block separation: with an end tie, for a >= 3 the
    block tA (top tie) or -t^a(1+t^2)A (bottom tie) is isolated once a > max(span A, span B) + 3, so |a| <= max(span A, span B) + 8
    is a valid window.

## 7. Verdict table
 V3, n >= 2, odd |a| >= 3 ............................................... PROVED (re-derived; hand proof of C1 sec. 2 is correct)
 V3, n = 1, odd |a| >= 3 ................................................ PROVED (C1: automaton certificate; here: by hand via BX5)
 V3, n >= 2, a = +-1 ..................................................... PROVED modulo Q-MONT (identity wV(+-1) = t^(+-3) w_3(+-1) checked)
 Lemma W ................................................................ PROVED;  a/N windows: not used by V3 (window re-derived, R3)
 Lemma S (sigma-law), Theorem V2, weak-end mismatch +1, P pinned .......... PROVED; CHECKED (354,293 boxes; 1,037 strong ends)
 BX3, BX4 ............................................................... PROVED (notie); CHECKED exactly
 BX4' ................................................................... PROVED for ALL rational boxes by argument; CHECKED (exact formula)
 T2 ..................................................................... PROVED for ALL rational boxes (automaton AND hand proof); CHECKED
 offset cases delta >= 2, 1, -1, -2, <= -3; tie cases delta = 0 (r = 0, 1) .. PROVED (all re-derived; match generator's equations)
 Theorem V (input formula) .............................................. GAP upstream (skein dictionary); CHECKED 682 lp.J words, 0 mismatch
 'V(L_n) != 1 for every n != 0' (C1 'WHAT IT IMPLIES') ..................... GAP: proved for even n; odd n needs J != J_*(n, j)
 'every depth-one arborescent quotient closed by theorem' (C1 sec. 5) ...... GAP: vertical n = 0 missing (CHECKED |a|<=101, |N|<=150)
 Counterexample search (i) ............................................... none: 1,062,393,500 closures (+3,479,865,816 extension)

## 8. Files (this folder)
 NOTES.md (running log), REPORT.md (this file).  src/: copies of C1/engineA code (jauto.py, v3lemmas.py, v3check.py, v3b.py,
 v3b3.py, vc.py, eng.py, lib.py; lib/eng/v3b re-pointed to src/), and the referee scripts:
   boxlemmas.py (exact lemma checks on normal forms), boxlemmas_R.py (same on R(L)), autocheck.py (automaton vs exact),
   run_gen.py (C1 generator certificates for rational-only V3, n_min = 2 and 1; output run_gen.log),
   brute.py / brute2.py (exhaustive mod-p + exact unit search), lpcheck.py / lpdeep.py (formula vs lp.J), wcheck.py (Lemma-W
   cross-check), chain.py (proof-chain test), jstar.py / jstar34.py (exact J, spans, J_* branch-knot loophole), t_speed*.py.
 Logs/pickles: boxlemmas_{10,12}.log/.pkl, boxlemmas_R10.log, brute_n4.log/.pkl (+ brute_n2.pkl), brute2_L5_n4-6.log/.pkl
   (+ brute2_L5_n1-3_a11_N15.pkl), lpcheck_s7.log/.pkl, lpdeep.log/.pkl, wcheck.log/.pkl, chain.log, jstar.log/.pkl,
   jstar34.log/.pkl, n0scan.log.
