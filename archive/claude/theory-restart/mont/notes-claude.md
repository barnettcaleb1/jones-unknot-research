# Claude's notes, 16 Nov evening (while workflow wf_262f952b-d86 runs)

## TYPE LAW (CHECKED: all 11,606 reduced non-integral words of length <= 8 in X, Y and inverses; types.py)
For a rational box v = rho(w)e_1 write a = a(v), b = b(v), D+ = top(a) - top(b), D- = bot(a) - bot(b),
s+ = lc(a) lc(b), s- = tc(a) tc(b) (leading / trailing coefficients are +-1). Then either
  - a(v) is a unit, and then b(v) is a monomial too (integral box: acts like Y^k up to a unit; 0 exceptions), or
  - v is of type P_k: (D+, D-, s+, s-) = (1+3k, 3k, -1, +1), or of type N_k: (3k, 3k-1, +1, -1), k in Z.
  N_k is the mirror of P_-k. Y^k shifts b by t^(-3k), i.e. P_0 -> P_k. So span(a) = span(b) + 1 for every non-integral box.
  Example: twist rows r >= 3 are P_0 (a: top j, b: top j-1, common bottom -3 with coefficient 1); r <= -3 are N_0.

## BOTH ENDS NEVER CANCEL (PROVED from the type law; CHECKED 40,000 random necklaces, oneend.py: 0 double cancellations)
J_raw Phi_3 = w_1 A + w_3 B, A = prod a_i, B = prod b_i. With n_P boxes of type P, n_N of type N and total integral shift K:
  top(A) - top(B) = n_P + 3K, bot(A) - bot(B) = -n_N + 3K, lc ratio (-1)^n_P, tc ratio (-1)^n_N.
Table of the twist weights (d+ = top w_3 - top w_1, r+ = lc w_1 / lc w_3; d-, r- at the bottom):
  mu >= 2:  d+ = 0, r+ = -1;  d- = -1, r- = +1
  mu = 1:   d+ = 0, r+ = -1;  d- = -3, r- = -1
  mu = -1:  d+ = 3, r+ = -1;  d- = 0,  r- = -1
  mu <= -2: d+ = 1, r+ = +1;  d- = 0,  r- = -1
Top cancels iff n_P + 3K = d+ and r+ (-1)^n_P = -1; bottom cancels iff -n_N + 3K = d- and r- (-1)^n_N = -1.
Solving both at once: mu >= 2 forces K = 0, n_P = 0, n_N = 1; mu <= -2 forces K = 0, n_P = 1, n_N = 0; mu = +-1 has no solution
(parity fails). So for n = n_P + n_N >= 2 at least one end of J_raw Phi_3 is exact (no cancellation).

## What is still missing for Lemma Q (Montesinos, horizontal inversion)
- One-end + unit-position criterion (J_raw = +-t^k0 would put the exact end at k0 or k0+2): fails in 48 of 40,000 cases
  (the exact end happens to sit at the unit position), so a second ingredient is needed.
- Cancellation depth at the cancelling end (depth.py, 60,000 cases): 0 in ~97.6%, then 1:~1.8%, 2:0.4%, 3:0.2%, 4:0.1%, 5:0.05%, one 7.
  Minimum span of J_raw Phi_3 over the run: 8 (so span J >= 6). Depth is not bounded by a tiny constant.
- Two-channel form: J(mu) = P + Q (-t)^mu with P = (tA + (1+t^2)B)/Phi_3, Q = (1+t^2)(A-B)/Phi_3 = (1+t^2)(1-t) (A-B)/(1-t^3).
  The bottom of J (mu > 0 large) comes from P alone; the top from Q (-t)^mu. Cancellation at an end is internal to P or to Q.
- Natural lower bound if neither end cancels: span(J Phi_3) >= span(w_1) + sum span(a_i) >= 8.

## Pretzel case by hand (twist rows only, K = 0): explicit germs
Twist row r = 2j+1 >= 3: with c = t^-3 (1 - t + t^2) and u_j = (-1)^(j+1) t^(j-3):
   a_r = c + u_j (1 - t)(1 + t^2),    b_r = c - u_j t (1 - t).
So A - B = c^(n-1) (1 - t) Phi_3 sum_i u_i + (terms of order >= 2 in the u's), bot(A - B) = j_min - 3n exactly
(equal j's have equal signs, so no cancellation inside sum u_i; coefficient +-multiplicity).
Cancellation pattern for pure pretzels (all |r_i| >= 3): mu >= 2: top cancels iff all rows negative, bottom iff exactly one negative row;
mu = 1: top iff all rows negative, bottom never; mu = -1: bottom iff all rows positive, top never; mu <= -2: top iff exactly one
positive row, bottom iff all rows positive. Mirror symmetry pairs these, so two essential cases.
Case mu = -M <= -2, all rows positive (P(-2M, r_1..r_n), e.g. P(-4,3,7)): top(S) = 1 + sum j (exact); near the bottom
S = (-1)^M t^-M (1+t^2)(A - B) + tA + (1+t^2)B, and tA + (1+t^2)B = Phi_3 c^n + ... has bottom -3n with coefficient 1.
If j_min > M: bot(S) = -3n; if j_min < M: bot(S) = -M + j_min - 3n; if j_min = M: the -3n terms cancel iff mult(j_min) = 1, and the
next coefficients decide. In all cases bot(S) <= -3n + O(1) while top(S) = 1 + sum j, so span(S) >> 2. Writing this as a proof needs
only the first few bottom coefficients of c^n, sum u_i, and the second-order term: a finite germ computation.

## Nesting breaks the type law (nested_types.py, 40 necklace bodies used as boxes, 38 pinned)
Necklace bodies r2.(y1)^m.ROW...ROW.u1 used as boxes have many channel shapes: (1,0,-1,1) and (0,-1,1,-1) (the rational types) in
10 of 38, and 16 other shapes, e.g. (1,-1,-2,-1), (0,0,1,-1), (2,0,1,1), with extreme coefficients up to 6 in absolute value.
Random non-rational half-diagram bodies (general_boxes.json): 31 of 50 have rational types (allowing Y-shifts), 19 do not.
So the two-type law is special to rational boxes; Lemma Q for iterated necklaces needs a different no-tie mechanism.

## a_2 shortcut (J''(-1) = -24 a_2): J = 1 forces a_2(K) = 0, so Lemma Q only has content when a_2 = 0 (a2zero.py)
- Pure pretzels P(-2m; r_1..r_n), |r_i| in {3..9}, n = 2, 3, mu in [-6,6]\0: a_2 = 0 in 18 of 1872, e.g. mu = 1, rows (3,5) (an
  alternating pretzel, det 31); spans of J in those cases 10..19.
- Random Montesinos necklaces: a_2 = 0 in 2553 of 60000; smallest span of J among them 10. So the a_2 = 0 cases are far from flat.

## CALIBRATION (16 Nov, evening, after LIT report and Caleb's question)
- Logical position: JC => Lemma Q (Gordon-Luecke); converse unknown. Full Lemma Q <=> Jones detects the unknot among knots with
  tangle unknotting number one (det 1 forces the slope 1/n; crossing change = n = +-2, so this includes all unknotting-number-one
  knots). Khovanov version: Hedden-Watson 2010; Jones version left open there. Sikora 2024 Thm 9.2: JC <=> bracket detects rational
  tangles among ALL tangles; his reduction uses locally knotted tangles, so no bootstrap from Lemma Q.
- Lemma Q is AUTOMATIC when a_2(K) != 0 (unit J with J = 1 mod (t+1)^2 forces J = 1, then J''(-1) = -24 a_2 = 0). Covers ~96% of the
  survey and all headline examples (P(-2,3,7), T(3,4), T(3,5)). Branch-set statement for a_2 != 0 is near-classical (LIT 3.4(b):
  Mullins + Casson + signature). Content lives only in a_2(K) = 0.
- Theorem N: true (PROOF lane skein proof, referee pending) but the mechanism is standard recoupling (V_1 x V_2 = V_1 + V_3). Present
  as a tool, not as a new theorem. Useful new packaging: the box ring R = {(a,b): a = b mod 1 - t^3}.
- Type law: enumeration only (11,606 words). Survey, depth stats, n = 11 Kh run: evidence, no theory.
- Real items: TH-2BR (Astra, proved); two-channel mechanism for the TWIST-2CH family; NOTIE lane's potential-function argument
  (Q-MONT, second-order automaton) if the referee passes it.
- Next theory target proposed to Caleb: expansion of J at t = -1 when a_2 = 0 (J = 1 mod (t+1)^3); identify the next coefficients as
  invariants of (K,h) and look for a class-free obstruction.

## NECKLACE WORKFLOW REFEREE OUTCOMES (wf_262f952b-d86, finished 16 Nov ~21:30)
- PROOF (Theorem N): STANDS_WITH_REPAIRS (bookkeeping only): scope must say special region C_m; Prop 3.9 (two raw closures fix v)
  is CHECKED not PROVED (243/243 exact); unit fixes in Prop 2.2, (U1) (kink gives a power of A), (U5). ~2,300 independent lp checks.
- NOTIE (Q-MONT): STANDS_WITH_REPAIRS: algebraic theorem holds (50k boxes, 12,740 necklaces, 0 units, 0 two-ended ties);
  repairs: cascade evidence wrong (conclusion survives with 2-parameter family), "n = 4 minimum 13" only searched, needs the lemma
  non-unit a <=> non-integral box (Gamma_0(2) orbit of 0), state mu = 0 and n <= 1, headline depends on Theorem N.
- NEST: STANDS_WITH_REPAIRS with one FALSE class claim: "both strong inversions of 2-bridge knots are one-box necklaces" is
  false (7_4 = P(3,1,3) vertical swap inversion, J span 12, matches no one-box class). Results N, O, V and Corollary S hold
  modulo GAP 1 (identifying lp.J with the coloured theta evaluation for general boxes; now covered by the PROOF lane's 0.2 and
  Astra's FT model). Corollary S (swap inversion of K#K^r: J = J_3(K)) CHECKED 715/715 against an independent 2-cable J_3.
- Consequence with FT: J_3(K)(-e^h) has Vassiliev coefficients (order <= k) for ordinary knots (via Corollary S).

## MOMENT-CYC10 (Astra 221023): J_(K,h)(t) = V_K(t^2) mod Phi_10 (K = covering knot)
- CHECKED by Claude: 300/300 random (K,h) (ft/claude/check_cyc10.py); the mirrored form V_K(t^-2) fails 173/300.
- Scan m <= 36 (ft/claude/cyc_scan.py): only m = 10 carries a nontrivial J-V relation; m = 1, 2, 4, 6 are the classical values.
- New class-free gate: J = 1 => V_K(omega) = 1 for every primitive 5th root omega. In 400 random nontrivial-V samples:
  a_2 = 0 in 18, V_K(zeta_5) = 1 in 8, both in 0 (ft/claude/z5_gate.py).
- Consequence (Astra): Phi_10 = (t+1)^4 mod 5 gives M_3/36 = 7 v_3(K) mod 5, so iota is an integer.
- Exclusions (Astra): no linear combination of v_3(K), v_3(constituents) gives M_3/36; the two 9_9 inversions share K, j and
  Sakuma eta but have iota = -4, +4. So iota is not a function of (K, eta, j).
- Proof under adversarial referee: workflow wf_3a347bde-78b (annular lens, projector/normalisation lens).

## a2 = 0 ROUND RESULTS (workflow wf_3ae3e846-831, finished ~23:00; all referees STANDS_WITH_REPAIRS)
- PROOF lane: independent proof of FT (TL model with f_2 sandwiches; R - R^-1 = (A^4 - A^-4)(Id - E'); mixed full twist
  F - F^-1 = (1+t)[t^-1 F - t^-2(1-t+t^2)]; integrality lemma <G> in Delta_2 Z[A^+-1]; units multiplicative, n_i = 4 eps_i).
  Symbol W_m = deframed osp(1|2) Brauer(-1) state sum with parity defect; 1T relations (a)-(c) proved; 4T proved modulo the
  Brauer -> Rep OSp(1|2) dictionary; W_2 = -12 Delta^2 a_2; W_3 tabulated on 193 types (78 nonzero, multiples of 48).
- OSP lane: sl_2 colour 2 at t = SO(3) at t^-1 = OSp(1|2) fundamental at q = -t, Dubrovnik parameters match exactly.
  J_3(K)(-e^h) = 1 - 24 a_2 h^2 - 144 v_3 h^3 + ... for every knot. Axis = parity defect at h = 0, but not a pure symmetry
  defect (quantum dim 0, double-braiding ratio -q^-3): a full perturbative series with the axis is still a GAP.
  Local knots: J(L # rL, swap) = J_3(L); Lemma Q on local-knot inversions <=> J_3 detects the unknot. Non-abelian:
  Wh(3_1) # r Wh(3_1) has Delta = 1 (and constituents Delta = 1) but J = J_3(Wh(3_1)) = 1 - 288 h^3 + ... .
- CORE lane: J'(1) = 8Q(1) = sigma(T(1/odd)); span theorem: J != 1 => span J >= 4, equality only for the trefoil values
  J = 1 + D_7 and its mirror; in the a_2 = 0 core span J >= 7. Second-order Mullins impossible (Lin-Wang lambda_2 has an
  n^2 a_4 term; 6_2's two inversions give det-1 branch sets with equal Sigma_2 and sigma, c_2 = 108 vs 228).
  Conjecture D = Astra's MOMENT-CYC10 found independently (J(-t) = V_K(t^2) mod (t^2-1)(t^3-1)(t^5-1)); referee: 0 failures in
  ~30,000 new cases; two-bridge mechanism: at primitive 10th roots TH-2BR is projectively conjugate to the TL 4-plat rep of K.
  Swap sums with C_{N+1}-trivial K' give nontrivial inversions with M_1..M_N = 0 (independent of Astra's FT-DEEP).
  SERIOUS referee issue: CORE's claim "Birman-Lin fails at R-matrix level" holds only in the divided-power lattice; in Astra's
  s-lattice the braiding is the super flip at q = i. Superseded.
- IDENT lane: M_3 = 432 v_3(K) + 180 D, iota = v_3 + D; M_4 = -1440 a_2^2 - 1440 a_4 + 864 j_4 - 120 a_2 + 1440 F_4.
  D, F_4 integral on 1,912 + words, vanish on local configurations, not combinations of ~60 classical/constituent/butterfly
  candidates (exact certificates). J = 1 => 5 | v_3(K), 5 | j_4(K). P(2k,4k-1,4k+1): congruence test excludes J = 1 iff 5 does
  not divide k (Q-MONT covers all k anyway). Example s.r1.x2.y1.y0.x1.x2.x1.x2.y0.y1.x2.y1.u1: a_2 = v_3 = a_4 = j_4 = 0,
  M_2 = M_3 = M_4 = 0, M_5 = 69120. J at t = +1 is also equivariant finite type (N_1 = J'(1) order 1; N_2 - N_1^2 =
  -8(a_2(K_in) + a_2(K_out))).
- LIT lane: no prior equivariant finite-type theory found; F1 new but routine; F2 new as stated (standard BMW mechanism; Huh-Jin
  Yamada argument extends to A = -e^x); osp colour-2 correspondence implicit in Zhang/Blumen/Clark; axis parity defect not
  found; J_3(K)(-e^h) Vassiliev not found stated; Habiro: J_K(3) - 1 in (t^2-1)(t^4-1)Z[t^+-1]; J^2 = J_3(K) mod (t+1)^3.
