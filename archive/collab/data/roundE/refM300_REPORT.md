# REFEREE refM300 (round E): THEOREM M300 of lpgen and its supporting lemmas
17 Nov 2026, Claude (referee refM300). Folder ~/jones-lanes/theory-restart/mont/cx/roundE/refM300/ (own code in src/,
logs and pickles here).  Marks: PROVED / CHECKED(n) / CONJECTURE / GAP / FALSE.  Default GAP when a step is only checked.
STATUS: FINAL (07:05).  All runs complete.  NO HIT (no unit anywhere; no HIT file written).

## 0. VERDICT (short)
THEOREM M300 is CORRECT (PROVED, computer-assisted) as an algebraic statement about the closure formulas of Theorem N
(horizontal) and Theorem V (vertical).  Every one of the 955 stored certificates was re-verified by an INDEPENDENT exact
semantic check (lpgen's code is used only to name the rows the multipliers refer to and, for regenerated certificates,
to FIND them; never to validate): own symbolic derivation of the weak-end case
conditions, own closure data, own class data recomputed from the box vectors, own jet automaton written from scratch
(validated exactly on 354,293 normal forms at both ends), own exact minimisation of each certificate's functional over
ALL rational boxes, own Farkas inequality.  955/955 valid; strong negative controls are rejected.  The same certificates
also prove the |k| = 1, n >= 1 clause.  The phi-lemma and its vertical d = 0 use are PROVED.  THEOREM D36 is TRUE but
lpgen's run (d2fix.py) had NO exact certificates (HiGHS status only): re-done here with 56,556 exact certificates, now
PROVED.  The ORDER-3 LEMMA is PROVED (sympy), and the F1 closure at order 3 for every multiset of listed top-300 + d2pos
boxes is now fully PROVED: lpgen's 798 'closed at order 2' slices were float verdicts and the 4 'MILP slices' were
HiGHS-MILP verdicts; here every slice has a verified exact certificate and the 4 MILP slices are proved integer-
infeasible by an exact branch and bound (19-20 certified leaves each).  The order-3 tie result (160 instances)
reproduces exactly (T3 impossible 160/160; T2 closed at the generic end, open at the a-positive end).
In all, about 60,900 exact Farkas certificates were verified by the own checker (955 M300 + 56,556 D36 + 1,382 F1 +
78 F1 B&B leaves + 1,583 F1' + 191 F1' B&B/enumeration + 160 tie leaves), 0 rejected where a proof was claimed.
No FALSE statement in M300, D36, the phi-lemma or the order-3 lemma.  ONE FALSE frontier statement (lpgen 5.9: 'F1'
closes all but ONE integer configuration'): the order-3 F1' survivors are whole families, incl. one lpgen missed (4.5).  GAPs are documentation/scope items and inherited
items (section 6/7): the branch-knot sentence 'all its branch knots L_n have V != 1' is OVERSTATED (odd n need
J != J_*(n, j), refV3 G2); the topological reading inherits Theorem N / V and the skein dictionary.

## 1. Claim (1): affine casework, additivity, LP formulation, the 955 certificates
 1.1 CASEWORK (PROVED).  Unit <=> F = S1 + S2 = c t^e Phi_3, S1 = w1 A, S2 = w2 t^-3N B (w2 = w3 for H, wV for V)
   <=> the normalised expansion of F at each end is 1 + u + u^2 + 0u^3 + ...  Own sympy derivation (derive_cases*.py) with
   s1 = exp(A1 u + A2 u^2 + A3 u^3), s2 likewise, offset d = deg S1 - deg S2 toward the expansion, e = lc S2/lc S1:
     d > 0: F_norm = s1 + e u^d s2;  d < 0: s2 + e u^|d| s1;  d = 0, e = +1: (s1 + s2)/2;  d = 0, e = -1, r = 1: c2 = c1.
   After the first condition pins A1 (or B1, or A1+B1 on a slice) every second condition is LINEAR in the LP variables.
   lpgen's rows (lpg.case_rows) have the same solution set as the derived system at 40 random rational points
   (p1,p2,q1,q2,m) in all 12 cases: 560/560 (cmp_cases.py); at the exact closure data every single lpgen row lies in the
   span of the derived rows (checked inside every certificate verification).  Rows for |d| = 3, 4, 5 coincide for both e
   (so 'd>=3', 'd<=-3' are exact merges).  Exhaustiveness: Lemma W gives a coincident end; Tot >= 3 gives an end with
   r >= 2 (strong); the other end is (i) also r >= 2 (TIE: sigma-law forces mB = 0, delta-law pins n), or (ii) offset
   d != 0 (10 offset cases, e = +-1 since |eps| = 1), or (iii) d = 0 with r = 0 (e = +1) or r = 1 (e = -1, mB != 0); in
   (ii)/(iii) the strong end has zero first-order mismatch, so the weak-end mismatch is mB (row P0), and in (iii) both ends
   coincide, so the delta-law n = delta.k - delta* holds.  The quadratic/bilinear terms (mB^2, mB*alpha) occur only in
   (iii) and are removed by slicing on mB.  So 'AFFINE in the end data' is right after slicing.
 1.2 ADDITIVITY (PROVED; CHECKED(300)).  The star product multiplies channels (a, b) componentwise (BRIEF: b = v1 +
   (1-t^3) v2 turns the TH-2BR product into a componentwise one), so at each end degrees ADD, leading coefficients
   MULTIPLY, log-jets (l1, l2, l3, ...) ADD; sigma = sum_ends (l1 b - l1 a) and delta = span b - span a ADD; Y^N changes
   only degrees.  CHECKED directly on 300 random products of 2-5 listed boxes (classdata.py): log-jets to order 3 at both
   ends of both channels, sigma, delta, span a of the product == sums: 0 failures.
   What does NOT add: the normalised coefficients x_k (only their logs add -- harmless: the rows are written in logs with
   X1/X2 pinned); leading coefficients (multiplicative; the eligibility |lc b/lc a| = 1 is therefore PRESERVED by products,
   which keeps eps = +-1); the agreement orders r_top, r_bot (closure-dependent, not data).  What only SUB-adds: the
   rational part (n boxes enter through n x conv(per-box vectors) = the automaton flow polyhedron, a valid relaxation),
   and the per-box bounds used by the phi-lemma (sum of bounds).  Nothing sub-additive is treated as additive.
 1.3 LP FORMULATION (PROVED sound).  Variables k >= 0 (real), n >= nmin, automaton flows: any actual configuration gives
   a feasible point (boxes = walks from init; R0 normal form + clipping lemma (refGen, PROVED) + own validation), so
   infeasibility <=> one Farkas vector valid for every multiplicity vector and every n.  Bottom data of rational boxes
   range over the same set as top data (R2; own check: bottom data == top data of the mirror on 354,293 normal forms).
   Slices sigma.k in [-8, 8] (top-300 sigma_j in {0,1}, so den = 1; 33 slice-LPs per closure class) + phi-lemma cover
   every mB (section 2).  Job list: 22 closure classes x 10 offsets = 220, 726 slices, 9 ties = 955.
 1.4 THE 955 CERTIFICATES (PROVED: all valid).  certcheck.py, own semantic verification of every stored (u, w):
   for each case LP the certificate's combination of case rows is a combination of OWN derived conditions; the induced
   functional G on rational boxes has exact minimum g0 over ALL non-integral rational boxes computed on the OWN K=3
   automaton (Bellman-Ford; finite in all 955); class columns computed from OWN class data are >= 0; g0 + cn >= 0;
   (g0 + cn) nmin - y.b > 0.  RESULT: 955/955 VALID (220 offset, 726 slice, 9 tie; the ties are trivially impossible:
   sigma.k = sigma* has no solution or forces n = delta.k - delta* < 0); max denominator 59; the stored set
   equals the job list.  Same certificates with kmin = 1, nmin = 1: 955/955 valid (=> the '|k| = 1 with n >= 1' clause).
   NEGATIVE CONTROLS (certcheck_neg.py): S + 60 d2pos classes -> 913 rejected; kmin = 1, nmin = 0 -> exactly the 12
   single-child cases lpgen reports open are rejected; planted rational-like class -> 293 rejected; planted b-potential
   class -> 302 rejected; one random multiplier perturbed -> 582 rejected.  The checker is discriminating.
 1.5 INPUT DATA (CHECKED / PROVED).  Own closure data (cmp_wdata.py) = lpgen's 22 classes + 9 ties exactly; class
   stability is PROVED by inspection (variable terms of w1, w3, wV sit at relative order >= 3 in every merged class) and
   CHECKED for |mu| <= 40, odd |a| <= 41; |lc w2/lc w1| = 1; wV(+-1) = t^(+-3) w3(+-1).  Own class data: all 27,585 listed
   top-300 boxes (and 256 d2pos boxes) reproduce C1's keys from the stored exact vectors, all eligible, min span a = 10.
   Vectors vs knot diagrams: see 5.2.
 1.6 SCOPE 'any box with such a signature' (PROVED here).  The proof needs Tot >= 3, i.e. span A >= 5 at mu = +-1.  No
   top-300 signature is realised by an eligible channel pair with span a <= 2 (smallspan3.py: jets fix the coefficient
   ratios; |lc| conditions and (1 - t^3) | (b - a) fail for every class), so every such box has span a >= 3 and |k| >= 2
   gives span A >= 6.  lpgen's wording is correct.

## 2. Claim (2): the phi-lemma  [PROVED]
 phi := rho_a + rho_q/2 = (rho_a + rho_b)/2 at the weak end.  Own data: sup over all non-integral rational boxes = -1/2
 exactly (own automaton K = 2, 3, 4); rational lambda_q in [-2, 1]; top-300 classes: phi <= -1/2 at both ends, |lambda_q|
 <= 2.  Vertical d = 0 (rows P0 and r=1 re-derived): sum_all boxes phi = 1 - (p1+q1)/2 - (LQ - p2 + q2)/mB, LQ = total
 lambda_q.  r = 0: sum phi = 1/2 (typ +) or 1 (typ -) > 0 > -N/2: impossible for every mB (and r = 0 is vacuous for units
 anyway: |lc F| = 2|lc S1| >= 2).  r = 1: N(1/2 - 2/|mB|) <= -1 + (p1+q1)/2 + |q2 - p2|/|mB| < 0 for |mB| >= 4 in all six
 V classes (typ +: -1/2 + 1/(2|mB|); typ -: <= -3/4): impossible.  Horizontal d = 0: delta_j <= -1 for all top-300
 classes, so n = delta.k - delta* >= 0 forces |k| <= 3 (mu = +-1) / |k| <= 1 (|mu| >= 2) and sigma.k in [0, 3], inside
 the slices.  Hence slices |sigma.k| <= 8 + phi-lemma cover every mB.

## 3. Claim (3): THEOREM D36  [TRUE; lpgen's run was only CHECKED; now PROVED here]
 lpgen's d2fix.py decides each case by `solve_primal(L).status == 0` (open) and counts every other HiGHS status as
 'closed' -- no Farkas certificate is extracted or verified, so D36 was CHECKED, not PROVED.  Re-done (d36.py): for each
 of the 60 d2pos classes D, S = top-300 + [D], k_D = 1 fixed, top multiplicities free, n >= 0, all 22 closure classes x
 (10 offsets + d = 0 slices sigma.k in [-15, 15]) + 9 ties = 1,571 case-LPs; certificates generated with lpgen's LP code,
 VERIFIED by the own checker.  The 36 D36 classes: 1,571/1,571 verified each (56,556 certificates); the other 24 stay open
 in 3-7 cases each (= lpgen's open list).  Generalised phi-lemma constants (own data): phi_D <= 0 (lpgen: <= 1/2),
 |lambda_q,D| <= 12, sigma_D in {2,3,4}, delta_D in [-5,-1]: vertical d = 0 with |mB| >= 15 forces N <= 3 boxes, hence
 |mB| <= 7: impossible; vertical slices cover mB in [-14, 16]; horizontal d = 0 has |k_top| <= 2, sigma.k in [2, 6].
 => D36 PROVED (for the 90 listed boxes; for an unlisted box with such a signature the single-box n = 0, mu = +-1 closure
 needs span a_D >= 5, which the signature does not imply).
 Corollary (lpgen 5.4, now PROVED): for the 6 b-potential classes d2_457, 459, 895, 902, 1232, 1247 the only cases left
 open in this run are F1 ('d=-1 e=-1'), and F1 is closed at order 3 for every multiset of listed top-300 + d2pos boxes
 (4.2); so ONE listed box of these 6 classes x ANY top-300 multiset x ANY rational part is never flat (box-level).

## 4. Claim (4): the ORDER-3 LEMMA, the F1 closure, the MILP slices, the tie result
 4.1 ORDER-3 LEMMA (PROVED, sympy).  F1 = 'd=-1 e=-1': F_norm = s2 - u s1; [u] gives l1(s2) = 2, [u^2] gives
   l2(s2) = X1 - 1, and with the mismatch l1(s2) - l1(s1) = mB (P0) X1 = 2 - mB is PINNED; [u^3] then reads
   l3(s2) - l2(s1) = (X1 - 2)^2/2 - 4/3 = mB^2/2 - 4/3, an equality affine in the end data for fixed mB.  Mirror F1':
   l3(s1) - l2(s2) = mB^2/2 - 4/3 (X2 = 2 + mB pinned).  Tie at r = 2: D3 = D2 (1 - X1).  All three re-derived symbolically.
   Third-order inputs (own): l3 of D per automaton edge and l3(q) per state from the own K = 3 automaton (validated exactly:
   log-jets of a and q to order 3 on 354,293 normal forms); closure q3 = l3(w2): V typ+ 1/3, typ- 0, H mu=+-1 1/3, +-2 0,
   +-3 1, |mu| >= 4 0 (mu = +-4 and |mu| >= 5 differ only in p3 = l3(w1), which F1 does not use and F1' does); box l3 data
   recomputed for every listed box (3,735 subclasses, = lpgen).
 4.2 F1 CLOSED AT ORDER 3 for every multiset of the LISTED top-300 + d2pos boxes, any rational part (f1redo.py): PROVED.
   mB <= -31: 22/22 order-2 exact certificates (own-verified).  mB >= 31: 22/22 exact certificates for LHS - 4 mB < b'
   (b' in [-37,-26]) own-verified; with c0 = 4/3 + q3 - p2 the quadratic mB^2/2 - 4 mB - (b' + c0) < 0 has negative
   discriminant in all 22: impossible.  |mB| <= 30: 1,342 slice-LPs, 798 closed at order 2 + 540 by the order-3 equality,
   every one with an own-verified exact certificate (lpgen had counted its 798 order-2 closures from HiGHS status only).
   The 4 LP-feasible slices (V typ+ |a|=3, mB = 4, top and bottom; H mu = +-1 bottom, mB = 5) are INTEGER-INFEASIBLE:
   exact depth-first branch and bound on integer k (3,735 subclasses) and n, 37/37/39/39 nodes, every leaf (19/19/20/20)
   closed by an own-verified exact certificate (milp_exact.py).  lpgen: 'PROVED except 4 MILP slices (CHECKED)'; now PROVED.
   SCOPE: order-3 data are box-level, so this is a statement about the listed boxes (lpgen says so).
 4.3 F1' (mirror, frontier): own re-run (f1pre.py): 1,586 slice-LPs |mB| <= 30 (mu = +-4 run with both p3 values):
   1,534 + 49 closed with own-verified certificates (lpgen's 'closed@2' were float verdicts), 3 open = lpgen's 3 (4.5).
   The tail mB <= -31 at mu = +-2 is unbounded in lpgen's LP (GAP, lpgen's own statement; not re-examined).
 4.4 ORDER-3 TIE RESULT (CHECKED(160), PROVED per instance).  tie3own.py with own data: 160 instances (H mu = +-1, one box
   from the 8 open a-potential classes with sigma = -2, n = delta_D + 3 pinned): T3 impossible in 160/160 (tau-law n =
   tau(B) - tau* contradicts the delta-law); T2 closed by own-verified certificates at the generic end, OPEN at the
   a-positive end in 80 + 80.  As lpgen states, this localises the tie frontier; it does not close it.
 4.5 F1' INTEGER STATUS (exact B&B milp_f1p.py + complete enumeration f1p_enum.py, all exclusions own-certified):
   mu=+2 top, mB=-7: the integer survivors are ANY 3 boxes of class d2_497 (4 order-3 subclasses, 18 boxes) with n = 2;
   mu=-2 bottom, mB=-7: ANY 3 boxes of d2_460 with n = 2, AND one box of top197 (40 boxes) + ANY 3 boxes of d2_460 with
   n = 1; mu=-2 bottom, mB=-8: integer-infeasible (sigma.k = -7 with sigma in {-2, 0}: parity; B&B 55 certified leaves).
   lpgen's 'closes all but ONE integer configuration: B^3 u_1 u_2 with B = box 50216 (resp. 50139)' is FALSE as stated
   (frontier description only; no effect on M300/D36): the survivor set is two whole families plus the T B B B u_1 family
   at mu = -2, and lpgen's exact search (5.10) covered only the cube of one box.  Sampled exact J search of the three
   families (f1p_sample.py; vector calculus, every Lemma-W candidate, all mu and all odd a): 10,000 products (2,500 +
   2,500 + 5,000), 364,561 candidates, 0 UNITS, 0 double-gate passers, min span J 58 / 58 / 68.  CHECKED(10,000).

## 5. Claim (5): lp.J spot-check  [CHECKED(1,004): 0 units]
 Design (spot_lib2.py, spot_run.py): seeds 0..999; each closure = a random multiset of 2-5 boxes of the top-300 classes
 (random classes, 30% forced repeated class, 15% literally repeated box) + 0-2 random non-integral rational companions
 (random reduced words of length 2-5); H or V with probability 1/2; (mu, N) resp. (a, N) drawn from the product's Lemma-W
 candidate set (engineA eng.hclosures / eng.vclosures: forced end coincidence, for V with leading cancellation or a
 two-ended coincidence; if V has no candidate, a forced degree coincidence N = N_top(a) or N_bot(a), 3 <= |a| <= 9).
 The explicit half-word is built with the BRIEF dictionary and J is computed EXACTLY by lp.J (subprocess, 300 s cap) and
 compared with the vector-calculus J; in addition EVERY Lemma-W candidate of every sampled product is scanned for units
 with the vector calculus.  Restriction (stated bias): boxes whose half-word nesting depth is <= 3 (13,353 of the 27,585
 listed boxes, in 263 of the 300 classes; depth-4/5 boxes make lp.J on products intractable -- one calibration product
 reached 3.5 GB).  The remaining boxes/classes are covered by the vector-calculus scans (vcscan.py, all depths).
 5.1 RESULT (spot_summary.py, spot_depth.py): seeds 0..999 all run: 998 lp.J results + 2 lp.J timeouts (two H closures,
 152-letter words of nesting depth 5); 6 replacement seeds (1000-1005) -> 1,004 closures with EXACT lp.J:
   H 439 / V 565; multisets of 2 / 3 / 4 / 5 boxes: 364 / 331 / 173 / 136; rational companions n = 0 / 1 / 2: 262 / 505 /
   237; 263 classes, 2,302 distinct listed boxes; 973 Lemma-W candidates + 31 forced degree coincidences;
   lp.J == vector-calculus J in 1,004 / 1,004; UNITS 0; min span J 31 (median 104); a_2 = 0 in 13, J(zeta_10) = 1 in 0;
   one-ended cancellation depth at the chosen closure 0..8 (0: 256, 1: 511, 2: 196, 3: 33, 4: 6, 5-8: 1 each), one closure
   with a two-ended depth (1,1).  In addition all 20,367 Lemma-W candidates of the 1,006 sampled products were scanned
   with the vector calculus: 0 units.  With vcscan.py (4,000 products of 2-6 boxes of ANY depth, 170,324 candidates,
   0 units; sigma-law/P0 identities hold on every actual closure) and d36scan.py (64,707 D36 candidates, 0 units).
   No unit: M300 is not refuted.  CHECKED(1,004 lp.J closures; 255,398 vector-calculus candidates).

 5.2 VECTORS vs KNOT DIAGRAMS (vec_lpj.py): for 80 listed boxes (one per class, 80 random top-300 classes) the box vector
 rebuilt from two raw lp.J closures (BRIEF sec. 4 formula) equals the stored vector up to a unit, and its own signature
 equals the class key: 80/80.  CHECKED(80) (refGen: 200 more).  So the class data feeding the certificates are the data
 of the actual knot diagrams on this sample.

## 6. What M300 implies, and what it inherits
 PROVED (algebraic): let B_1..B_K be eligible boxes whose order-2 signatures lie in the 300 listed classes (in particular
 any of the 27,585 listed boxes), K >= 2, or K = 1 and n >= 1; u_1..u_n non-integral rational boxes (n >= 0); N in Z;
 A = prod a(B_i) prod a(u_j), B = prod b(B_i) prod b(u_j).  Then for every mu != 0, w1(mu) A + w3(mu) t^-3N B is not
 +-t^e Phi_3, and for every odd a, w1(a) A + wV(a) t^-3N B is not +-t^e Phi_3 (|a| = 1 is the horizontal mu = +-1 case).
 INHERITED for the knot-theoretic reading: (i) Theorem N (necklace formula, mont/proof: PROVED; referee/nest: modulo GAP 1,
 the identification of lp.J / bracket_vector with the coloured theta evaluation and of (H, X, Y, e_1) with TH-2BR
 coordinates) for horizontal closures s.r2.(y1)^m.Y^N(B_1..B_K u_1..u_n).u1 (mu = -m); (ii) Theorem V (vertical formula,
 nest: PROVED modulo the same skein dictionary) for s.l1.(...).(x2)^a.u1; (iii) Theorem O / the tree -> half-word
 dictionary (the box vectors of nested boxes; refGen and this referee: vectors vs lp.J raw closures); (iv) C1's framework:
 Lemma W, Lemma S (sigma-law), D1/D2 (delta-law), R0, R2, the K = 3 automaton and clipping lemma (refGen PROVED; re-done and
 validated here), BX lemmas (only through the automaton facts).  Then: every strongly invertible (K, h) whose quotient
 half-word is such a closure has J(K, h) != 1, so it is NOT a Lemma-Q counterexample.
 BRANCH KNOTS: lpgen's 'all its branch knots L_n have V != 1' is OVERSTATED (inherits refV3's G2): J != 1 gives
 V(L_n) != 1 for every EVEN n; for odd n, V(L_n) = 1 <=> J = J_*(n, j) (j = -J'(1)/8 = n a_2(K) != 0, 3 not dividing n),
 which M300 does not exclude.  GAP (inherited, not specific to M300).

## 7. GAPs and remarks
 G1 (documentation, CLOSED here) D36 and the F1 order-2 slices were float verdicts in lpgen's runs; exact certificates
    now exist and verify.  The 4 F1 MILP slices: exact branch and bound here.
 G2 (inherited) Theorem N / V and the skein dictionary for the topological reading (section 6).
 G3 (inherited) branch-knot consequence for odd n (J_* loophole).
 G4 (scope) D36 for unlisted boxes needs span a_D >= 5 (single box, n = 0, mu = +-1); M300 has no such gap (1.6).
 G5 (lpgen frontier, not re-examined) F1' tail mB <= -31 at mu = +-2; two-ended families with a-potential factors.
 F1 (FALSE as stated, frontier only) lpgen 5.9 / HEADLINE 'F1' closes all but ONE integer configuration (B^3 u_1 u_2 with
    B = box 50216 / 50139)': the integer survivors are the families of 4.5 (any 3 boxes of d2_497 resp. d2_460 with n = 2,
    and T B B B u_1 with T in top197 at mu = -2).  Sampled exact search of the families: 0 units (log).
 D1 (documentation) lpgen sec. 3 says '24 closure families x 11 offset cases' and 'd=0 slices |mB| <= 8': the run has 22
    closure classes x 10 offset cases (+ 726 slices with |sigma.k| <= 8, i.e. mB in [-8-sigma*, 8-sigma*], + 9 ties).
    Harmless (the job list is complete, 1.3).
 D2 (documentation) lpgen's 'exact certificates' for D36, for the 798 F1 order-2 slices and the 1,412 F1' order-2 slices
    were HiGHS status verdicts; the 4 F1 'MILP slices' were HiGHS MILP verdicts.  All re-done exactly here (sections 3, 4).
## Log (chronological; clock times approximate)
- read BRIEF, engineC1/REPORT, refGen/NOTES (+ integrator note), refV3/REPORT, lpgen/REPORT (+ integrator note), engineA/REPORT.
- 05:25 OWN code (src/): rlaurent.py (exact Laurent/end-series/log-jets, w1 w3 wV), rauto.py (own precision-tracked jet
  automaton, written from scratch): K=2: 9 states/89 transitions, K=3: 19/227 (89 dedup edges), K=4: 35/489; clipping
  asserted for |m| = M..M+8 from every state; NO edge into init.
- v_auto.py: own automaton vs EXACT Laurent computation on ALL normal forms u(m) with sum|m_i| <= 12 (354,293 boxes):
  top log-jets of a (order K), q (deg, lc, log-jet order K) and BOTTOM data == top data of the mirror u'' at K=3:
  0 mismatches at K=3 AND at K=4 (v_auto12.log).  CHECKED(354,293 x 2 ends x 2 K).
- derive_cases*.py (sympy, independent derivation from 'normalised F = 1 + u + u^2 + 0u^3'): every lpgen case row
  (lpg.case_rows) has the same solution set as the derived system at 40 random rational (p1,p2,q1,q2,m): 560/560
  case systems identical.  Order-3 identities re-derived: F1 l3(s2) - l2(s1) = (X1-2)^2/2 - 4/3 (= mB^2/2 - 4/3 with
  X1 = 2 - mB); F1' l3(s1) - l2(s2) = mB^2/2 - 4/3; tie r=2: D3 = D2 (1 - X1).  PROVED (symbolic).
- cmp_wdata.py: own closure data from w1, w3, wV: lpgen's 22 closure classes (p, q, sigma*, delta-law offset) and 9 tie
  classes agree exactly; classes are stable (order 2) for |mu| <= 40, odd 3 <= |a| <= 41; |lc w2/lc w1| = 1;
  wV(+-1) = t^(+-3) w3(+-1).  At order 3 the H class |mu|>=4 splits (mu=+-4 vs |mu|>=5, only in p3 = l3(w1)).
- classdata.py: signatures of ALL 27,585 listed top-300 boxes and 256 d2pos boxes recomputed from the exact vectors with
  own code: 0 mismatches with C1's keys, all eligible (|lc b/lc a| = 1, span a >= 1); min span a = 10 (top-300), 12 (d2pos);
  order-3 subclasses 3,598 + 137 = 3,735 (= lpgen).  top-300: sigma in {0 (296 classes), 1 (4)}, delta in {-1 (294), -2 (6)}.
  ADDITIVITY: 300 random products of 2-5 listed boxes: product end data computed directly == sum of factor data
  (log-jets to order 3 at both ends for a and b, sigma, delta, span a): 0 failures.
- certcheck.py: ALL 955 certificates of certs_M300.pkl VALID under an independent semantic check (own rows, own closure
  data, own class data, own automaton min of the certificate's functional on rational boxes, own Farkas inequality;
  lpgen's flow potentials not used).  Max denominator 59.  Stored set == the 955 jobs of the M300 run.
  NEGATIVE CONTROLS (certcheck_neg.py): + 60 d2pos classes: 913 rejected; kmin=1 & nmin=0: exactly 12 rejected (= the 12
  single-child cases lpgen reports open); planted rational-like class: 293 rejected; planted b-potential class: 302 rejected;
  random single-multiplier perturbations: 582 rejected.  The SAME 955 certificates are also valid with kmin=1, nmin=1
  (955/955), i.e. they also certify M300's '|k| = 1 with n >= 1' clause.
- 05:40 philemma.py (own data): sup over ALL non-integral rational boxes of phi = rho_a + rho_q/2 is exactly -1/2 (own
  automaton, K = 2, 3, 4); rational lambda_q in [-2, 1], rho_q in {-1,0,1}; top-300 classes: max phi (both ends) = -1/2,
  max |lambda_q| = 2, delta in {-1,-2}, sigma in {0,1}.  Vertical d=0: r=0 needs sum phi = 1/2 or 1 (> 0): impossible
  for every mB; r=1 impossible for every |mB| >= 4 in all six V classes (inequality re-derived and evaluated).  PROVED.
  Horizontal d=0: n = delta.k - delta* >= 0 with delta_j <= -1 forces |k| <= 3 (mu=+-1), |k| <= 1 (|mu|>=2), so
  sigma.k in [0,3]: inside the LP slices sigma.k in [-8,8].  PROVED.
- 05:55 d36.py: THEOREM D36 RE-DONE WITH EXACT CERTIFICATES.  lpgen's d2fix.py had only HiGHS float verdicts (status != 0
  counted as closed; no Farkas certificate extracted) -> its 'PROVED' was only CHECKED.  Here: for each of the 60 d2pos
  classes D, S = top-300 + [D] with k_D = 1 fixed, n >= 0, every closure class x 10 offsets, d=0 slices sigma.k in
  [-15,15] (V: mB in [-14,16]), 9 ties = 1,571 case-LPs per class; certificates generated with lpg (HiGHS) and VERIFIED by
  the own checker (certcheck2.py): the 36 D36 classes: 1,571/1,571 verified each (56,556 certificates); the 24 lpgen-open
  classes stay open in exactly 3-7 cases each (control).  Generalised phi-lemma constants (own data): D36 classes have
  phi <= 0 (claimed <= 1/2) and |lambda_q| <= 12 at both ends, sigma in {2,3,4}, delta in [-5,-1]: |mB| >= 15 vertical d=0
  impossible (N <= 3 boxes => |mB| <= 7).  Horizontal d=0: |k_top| <= 2, sigma.k in [2,6] (covered).  => D36 PROVED.
- spot-check launched (spot_run.py, 5 parallel lp.J subprocesses, timeout 300 s, per-seed result files spot_res/).
  lp.J cost: 2-70 s per closure with boxes of half-word nesting depth <= 3 (depth 4-5 boxes make products intractable
  for lp.J: one 5-closure calibration run reached 3.5 GB and was killed by me).  So the sample uses the 13,353 listed
  top-300 boxes whose half-word nesting depth is <= 3 (selection bias stated).
- 06:05 ratlaws.py: own exact check on all 118,097 normal forms with sum|m_i| <= 11: delta = -1, sigma = 0, tau = -1,
  |lc q| = 1 at both ends, rho_b <= 0 at both ends, span a >= 4: 0 violations (re-check of the PROVED Lemma S / S3 / BX3
  inputs of the sigma-law, delta-law and tau-law).
- f1redo.py bound: F1 order-2 LP with mB <= -31 over all top-300 + d2pos classes: 22/22 exact certificates VERIFIED by the
  own checker (mB >= 31 side open at order 2, as lpgen says).
- tie3own.py: the 160 order-3 tie instances (H mu=+-1, one a-potential d2 box from the 8 open classes with sigma = -2,
  n = delta_D + 3 pinned): own data reproduce lpgen exactly: T3 (both ends r >= 3) impossible in 160/160 (tau-law n =
  tau(B) - tau* contradicts the delta-law); T2 closed with an own-verified exact certificate at the box's generic end and
  OPEN at its a-positive end in 80 + 80.  So the tie result LOCALISES, it does not close, these ties (as lpgen states).
- 06:15 f1redo.py large: mB >= 31: 22/22 exact certificates (LHS - 4 mB < b', b' in [-37,-26]) VERIFIED by the own
  checker; with c0 = 4/3 + q3 - p2 (own closure data) the discriminant 16 + 2(b' + c0) is negative in all 22 (values
  -172/3 .. -98/3): the order-3 equality is impossible for every mB >= 31.  PROVED.
- f1redo.py slices |mB| <= 30 (S = all 3,735 order-3 subclasses of top-300 + d2pos, any multiplicities, n >= 0):
  1,342 slice-LPs: 798 closed at order 2 + 540 closed by the order-3 equality, EVERY one with an exact certificate
  VERIFIED by the own checker (lpgen's f1uni counted its 798 order-2 closures from HiGHS status only, without a
  certificate: now certified); 4 LP-feasible slices = exactly lpgen's 4 MILP slices.
- milp_exact.py: the 4 MILP slices (V typ+ |a|=3 mB=4 top & bottom; H mu=+-1 bottom mB=5) are INTEGER-INFEASIBLE, proved
  exactly by depth-first branch and bound on integer k (3,735 subclasses) and n: 37/37/39/39 nodes, 19/19/20/20 leaves,
  every leaf closed by an exact Farkas certificate verified by the own checker (branching bounds as extra rows).
  => F1 at order 3 is EMPTY for every multiset of the LISTED boxes of top-300 + d2pos: PROVED (was: PROVED except 4 MILP).
- 06:05 smallspan*.py: SCOPE of 'any box with such a signature'.  The proof needs Tot = span S1 - 2 >= 3 (H mu=+-1:
  span A >= 5).  Exact test: no top-300 or d2pos signature is realised by an eligible channel pair (a, b) with span a <= 2
  (jets fix the coefficient ratios of span-1/2 channels; |lc b/lc a| = 1 at both ends and (1 - t^3) | (b - a) checked
  for every residue shift): NONE.  So every eligible box with a top-300 signature has span a >= 3, hence |k| >= 2 gives
  span A >= 6: M300 holds for ANY eligible box with these signatures (as lpgen states).  [For D36 the single box with
  n = 0 at mu = +-1 needs span a_D >= 5: true for the 90 listed boxes (span a >= 12); not implied by the signature.]
- 06:10 vec_lpj.py: 80 listed top-300 boxes (one per class, 80 random classes, half-word depth <= 3): box vector
  rebuilt from the KNOT DIAGRAMS (two raw lp.J closures, BRIEF sec. 4 formula) == stored vector up to a unit, and the
  own signature of the lp.J vector == class key: 80/80.  CHECKED(80) (refGen: 200 more).
- f1pre.py (F1' = 'd=1 e=-1', order-3 equality l3(s1) - l2(s2) = mB^2/2 - 4/3): 1,586 slice-LPs |mB| <= 30 (mu = +-4 with
  both p3 values): 1,534 closed at order 2 + 49 at order 3, all with own-verified certificates; 3 open = lpgen's 3.
- milp_f1p.py (exact B&B on the 3 open F1' slices): mu=+2 top mB=-7: integer point k = 3 x d2_497, n = 2 (= lpgen);
  mu=-2 bottom mB=-8: INTEGER-INFEASIBLE (109 nodes, 55 own-certified leaves; lpgen: 'fractional only', now PROVED);
  mu=-2 bottom mB=-7: integer points k = 3 x d2_460, n = 2 (= lpgen) AND k = {1 x top197, 3 x d2_460}, n = 1, which
  lpgen's report does NOT list ('ONE integer configuration').  Complete enumeration running (f1p_enum.py).
- 06:10 spot-check interim: 215 closures done, lp.J == vector calculus 215/215, 0 units (also 0 units among all 3,971
  Lemma-W candidates of the sampled products, vector calculus), min span J 38.
- 06:15 f1p_enum.py (COMPLETE integer enumeration of the 3 LP-open F1' slices; participating variables found by
  iterated LP screening, every other pattern closed by an own-verified certificate):
    H mu=+2 top, mB=-7: 20 integer configurations = ANY 3 boxes of class d2_497 (all 4 order-3 subclasses, 18 boxes), n=2.
    H mu=-2 bottom, mB=-7: 40 = ANY 3 boxes of d2_460, n = 2 (20) AND one top197 box (40 boxes) + ANY 3 boxes of d2_460,
      n = 1 (20).
    H mu=-2 bottom, mB=-8: none (sigma parity; B&B proof above).
  => lpgen 5.9/HEADLINE 'closes all but ONE integer configuration: B^3 u_1 u_2 with B = box 50216 (resp. 50139)' is FALSE
  as stated (frontier description, not M300): the survivors are whole families (any 3 boxes of the class, and at mu=-2 an
  extra family T B B B u_1 with T in top197), and lpgen's exact search 5.10 covered only the cube of one box.
- gtest.py: the 946 non-tie certificate functionals G evaluated on 3,000 random ACTUAL rational boxes (exact Laurent data
  at the weak end, bottom computed directly at t = 0, no automaton): G(box) >= g0 always (0 violations); the automaton
  minimum g0 is attained by an actual sampled box in 771/946 (the bound is tight, not loose).
- f1p_sample.py: sampled exact J search (vector calculus, every Lemma-W candidate, all mu and all odd a) of the complete
  F1' survivor families: A = 3 random d2_497 boxes + 2 from R(6) (2,500), B = mirror with d2_460 (2,500), C = top197 box +
  3 d2_460 boxes + 1 from R(7) (5,000): 10,000 products, 364,561 candidates, 0 UNITS, 0 double-gate (a_2 = 0 and
  J(zeta_10) = 1), min span J 58 / 58 / 68.  CHECKED(10,000 products).
- spot_depth.py (interim, 259 closures): chosen closures have one-ended cancellation depth 0..8 (0: 72, 1: 120, 2: 55,
  3: 9, 4: 1, 6: 1, 8: 1); no two-ended cancellation.

- d36scan.py: one listed D36 box (90 boxes) + 0-4 listed top-300 boxes + 0-2 rational boxes (R(6)), 2,000 random
  products, EVERY Lemma-W candidate (H all mu, V all odd a): 64,707 candidates, 0 UNITS (vector calculus).
- k4check.py: the exact minima of the 946 non-tie certificate functionals are identical on the own K = 2, 3 and 4
  automata (946/946) -- consistency of the automaton refinement.
- certshow.py (what a certificate says): e.g. F1 at V top a>=3 ('d=-1 e=-1'): G = -(7 rho_a + 4 rho_q + 2 l2a + 2 lambda_q)/9
  has exact minimum 5/9 > 0 on every rational box (a negative-potential functional; rho_a, rho_b <= 0), every top-300 class
  column is >= 0 and the constant is 8/3 > 0; H mu=+1 top F1: G = -(5 rho_a + 4 rho_q + 2 l2a + 2 lambda_q)/7 >= 3/7.  The
  d=0 r=1 slices use the delta-law row (cn = -g0) to absorb n.  This is lpgen's M-ADD mechanism made explicit.
- d2pos anatomy (lpgen sec. 4) CHECKED with own data: each of the 60 classes has exactly one positive end; 42 b-potential
  (rho_b = +1, sigma in {2 (12), 3 (28), 4 (2)}), 18 a-potential (rho_a = +1, rho_b in {-1,0}, sigma in {-2 (8), -1 (10)});
  the other end has rho_a, rho_b <= -2.  No deviation.
- vcscan.py (vector calculus, ANY nesting depth): 4,000 random products of 2-6 listed top-300 boxes + 0-2 rational boxes
  (R(6)), EVERY Lemma-W candidate (H all mu, V all odd a): 170,324 candidates, 0 UNITS.  On the same actual closures the
  sigma-law identity X_top + X_bot = mB (X = l1(s2) - l1(s1)) holds in all of them (0 failures), and at all 40,141 ends
  with r >= 2 the opposite end's mismatch is exactly mB (the P0 row).  CHECKED(170,324).
- spot-check runners: ascending (pid 1196, 5 workers) and descending (pid 3115, 3 workers), one result file per seed;
  a third runner (pid 4256) was started and then stopped by me after ~1 min because free memory was low (load 68); its
  two orphaned lp.J workers (pids 4311, 4319) were killed by PID; their seeds are recomputed by the other runners.
  Only PIDs I started were killed.
- 07:05 FINAL spot-check: seeds 0..999 complete (998 lp.J + 2 timeouts) + 6 replacement seeds = 1,004 exact lp.J
  closures, lp.J == vector calculus 1,004/1,004, 0 units, min span 31; 20,367 Lemma-W candidates of the sampled products
  scanned with the vector calculus, 0 units.  All my background processes have finished.

## 8. Files (this folder; own code in src/, run with tools/venv/bin/python, or /opt/homebrew/bin/python3 where scipy/lpg
## is imported)
 src/rlaurent.py (own Laurent/end-series/log-jets; w1, w3, wV), src/rauto.py (own jet automaton + exact Bellman-Ford),
 src/nf_exact.py + v_auto.py (exact normal forms; automaton validation; log v_auto12.log), src/ratlaws.py (rational laws),
 src/derive_cases.py, derive_cases2.py, derive_cases3.py, derive_poly.py (sympy derivation of the casework and order-3
 identities; derived_*.pkl), src/cmp_cases.py, cmp_wdata.py (comparison with lpgen; wdata.pkl), src/classdata.py
 (classdata.pkl; additivity), src/certcheck.py (THE 955-certificate verification), certcheck_neg.py (negative controls),
 certcheck2.py, semcheck.py (general semantic Farkas checker), gtest.py (functionals vs actual boxes), philemma.py,
 smallspan.py/smallspan2.py/smallspan3.py (scope), d36.py (d36.log, d36_res.pkl), f1redo.py (f1redo_*.log/pkl),
 milp_exact.py (milp_exact.log), f1pre.py (f1pre.log/pkl), milp_f1p.py, f1p_enum.py, f1p_search.py, f1p_sample.py
 (milp_f1p.log, f1p_enum.log, f1p_sample.log), tie3own.py (tie3own.pkl), spot_lib.py, spot_lib2.py, spot_worker.py,
 spot_run.py, spot_run_desc.py, spot_summary.py, spot_depth.py (spot_res/<seed>.pkl, spot_run*.log), vec_lpj.py
 (vec_lpj.log), spot_fg.py (foreground helper), spot_profile.py / spot_cal*.py / spot_time.py (lp.J cost calibration),
 vcscan.py (vcscan.log), d36scan.py (d36scan.log), k4check.py, certshow.py, t_auto.py, peek.py.
