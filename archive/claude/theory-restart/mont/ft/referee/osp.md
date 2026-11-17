# REFEREE NOTES: lane OSP (adversarial), 16 Nov 2026
Referee: Claude (adversarial referee subagent). Target: ../osp/REPORT.md (237 lines, read in full).
Own scripts: ./ospref/ (referee's own code; builder scripts only read, never edited).
Marks: PROVED / CHECKED(n) / CONJECTURE / GAP / KNOWN. Verdict at the end.

## Status: COMPLETE (16 Nov 2026). Verdict: STANDS_WITH_REPAIRS (all repairs expository; no claim broken).

## 0. Claims under review (builder numbering)
1 Dictionary (PROVED)            2 J_3(-1)=1 + expansion (PROVED)     3 THEOREM FT (PROVED)
4 on-axis O(h^{m+1}) (PROVED)    5 parity defect (PROVED)             6 top-order formula (CHECKED)
7 GAP (perturbative series)      8 CONJECTURE (twisted Casimir)       9 local knots J = J_3(L) (PROVED)
10 Lemma Q on local <=> J_3 detects unknot (PROVED)                   11 non-abelian Wh(3_1) (CHECKED)
12 iota - v_3 not small-int combination (CHECKED)

## 0b. First pass (reading only; 16 Nov ~22:10)
- Read BRIEF, ../../BRIEF.md, osp/REPORT.md (full), builder scripts ftraw.py, wjnorm.py, localknot.py, whdouble.py, j3knots.py,
  constit.py, ftraw_sens.py; tools lp.py, flat_search.py, kauffman.py, alex.py.
- Cross-lane: CORE lane independently states claim 9 (swap sums = colour-2 coloured Jones, its 4.2) and claim 12's negative
  (its 3.4); CORE also proposes iota = g(1) - 3 v_3(K) with g = (J(-t) - V_K(t^2))/((t^2-1)(t^3-1)(t^5-1)). No conflict seen.
- Convention map (verified by reading code): kauffman/flat_search letter 'x' = A*(vertical) + A^-1*(cup-cap); lp.J_raw maps
  A^e -> t^(e/4) (t = A^+4); ident3.VK, j3knots, whdouble.to_t use t = A^-4 (KL). So lp.J = J_KL(1/t), as the builder says.
  FT (divisibility by (1+t)^m) is invariant under t -> 1/t, so FT is convention-free; only odd-order statements need care.

## 1. Claim 1 (dictionary)
- Re-derived: R_22 eigenvalues (KL lambda^{22}_c) A^-8, -A^-4, A^4 = t^2, -t, t^-1 = e^{2h}, e^h, -e^{-h}; Lemma 1.1 per channel;
  kink theta_2 = A^8 = t^-2; loop Delta_2 = t^-1 + 1 + t = 1 + (a - a^-1)/z (consistent Dubrovnik loop).
  SO(N) Dubrovnik (q^{N-1}, q - q^-1, loop 1 + [N-1]): N = 3 at q3 = t^-1 matches; N = -1 at q matches iff t = -q (t = +q fails
  on z). N <-> 2-N for odd N: (-q^-1)^{N-1} = q^{(2-N)-1} and (-q^-1) - (-q^-1)^-1 = q - q^-1. All correct.
- R_22 = P_s exp(-hT), T = diag(-2,-1,1) = 2(C(R_j) - 1) with C(R_j) = j(j+1/2) (0, 1/2, 3/2): exact (all diagonal). Super flip on
  C^{1|2}: S^2_super = (2|2) = R_0 + R_{1/2} (dim 4), Lambda^2_super = (3|2) = R_1 (dim 5): matches channels 0+2 / 4. Twists
  theta_{2m} = A^{4m(m+1)} = q^{-m(m+1)} = q^{-4C(R_{m/2})} (m(m+1) even); Delta_{2m} = sum_{|k|<=m} (-1)^k q^k -> (-1)^m. Correct.
- Caveat (MINOR, already flagged by the builder as KNOWN-MEMORY): what is PROVED is the skein-parameter statement (colour 2 obeys
  the N = -1 Dubrovnik specialisation at q = -t; at q = 1 this is Brauer(-1) with the super flip, classical osp(1|2) invariant
  theory). The identification with the module category of the quantum supergroup U_q(osp(1|2)) in these exact parameters needs a
  checked reference (signs of a and z are convention-dependent in that literature); no later claim of the report uses it.
VERDICT claim 1: STANDS (with that labelling caveat).

## 2. Claim 2 (J_3 at t = -1)
- Proof re-derived: Lemma 1.1 (checked channel by channel: c=0: z(1-Delta_2) = A^-8 - A^8; c=2,4: z = A^4 - A^-4) makes a
  colour-2 crossing change cost z(1 - E), z = A^4 - A^-4 = 2 sinh h; kink a = A^8 -> 1; integrality of f_2-coloured links by
  <K_f2> = <K^(2)> - 1 (e-closure of the 2-cable = boundary of the cut band: unknot, writhe 0, split => delta). Writhe factor
  t^(2w) is multiplicative-affine. So J_3(-1) = 1 and finite type: PROVED (standard Birman-Lin at a root of unity).
- Calibration logic: c_1 = 0 (order 1 => constant); c_2 = beta a_2; c_3 = gamma a_2 + delta v_3 with gamma = 0 forced by
  J_3(K*)(t) = J_3(K)(1/t) (c_n(K*) = (-1)^n c_n(K)). So one knot (3_1) fixes both coefficients. Correct.
- CHECKED(13 diagrams, own code ospref/rlib.py + c2_j3.py, independent bracket/writhe/2-cable implementation): 3_1 (two
  diagrams), 3_1*, 4_1 (two diagrams), 5_1, 5_2, 6_1, 6_2, 6_3, 7_1, 3_1#4_1, T(3,4): J_3(-1) = 1, [h^1] = 0, [h^2] = -24 a_2,
  [h^3] = -144 v_3 in every case; the builder's h^4 values (3_1 -508, 4_1 124, 5_1 -4308, 5_2 -2264, 6_1 728) reproduced.
- Convention: both J_3 and V in KL t = A^-4 with the same letter convention, so c_3 = -144 v_3 is mirror-consistent.
VERDICT claim 2: STANDS.

## 3. Claim 3 (THEOREM FT proof, line by line)
- (i) multilinearity: fine (sites are disjoint balls; <Theta> is linear in each local tangle).
- (ii) local relations: off-axis R_22 - R_22^-1 = z(1-E) (re-derived per channel); on-axis Yhat - t^4 Yhat^-1 = (1+t^3)(Yhat-t^2)
  (re-derived: P_1: t^2 - t^4 t^-2 = 0; P_3: t^-1 - t^5 = t^-1(1-t^6) = (1+t^3)(t^-1-t^2)). Both are identities between honest
  diagrams (twist / no twist; crossing / two smoothings), so they hold in every closure. Also checked: the UNtwisted difference is
  integral too: Yhat - Yhat^-1 = (1+t) t^-1 [Yhat - (t - 1 + t^-1)] (own computation; matches Astra's T - T^-1 formula).
  Quotient dictionary checked in flat_search.quotient_word: x0 -> sigma_0 sigma_1^2 sigma_0 = c_{V2,V1} c_{V1,V2} (axis strand 0
  around the band (1,2); the middle sigma_1's involve the axis, not the two band edges), y0 = its inverse (palindromic word).
- (iii) integrality: the key identity is <Theta;1,1,2> = <T(1)> - delta^-1 <T(e)> = delta(delta y + x) - (y + delta x) =
  (delta^2 - 1) y = Delta_2 y for ANY quotient tangle T = y Q_0 + x Q_inf, including tangles containing extra closed curves
  (own derivation; it does not use T(1/0) = unknot). With the loop expansion (e-term = split 0-framed unknot, value delta, so
  -delta^-1 * delta = -1) every expanded network has E = <.>/Delta_2 in Z[A,1/A]. Correct.
- (iv) normalisation: re-derived. c_0 = Etilde_S(0) independent of S (|T|=1), Etilde'_S(0) affine (|T|=2), n_S = 4 Etilde'_S(0)/c_0,
  J_S(h) = e^{-n_S h/4} Etilde_S(h)/c_0 EXACTLY (u_S e^{i pi n_S/4} = 1/c_0), Leibniz for finite differences
  (Delta_i(f^S g) = (g_S - g_{S+i}) + (1 - f_i) g_{S+i}). Correct. (v) Gauss: correct ((1+t) monic).
- Statement equivalence (Delta^m J in (1+t)^m <=> Delta^m M_k = 0 for k < m <=> M_k of order <= k): correct.
- CHECKED (own driver ospref/ft_check.py, seed 101, lp.J as the definition of J, own exact division by (1+t)):
  225 samples = 3 generators (own random half-word walk; flat_search.gen long words L = 14..24; words.mont Montesinos with random
  rows/twists/letters) x 3 modes (mixed / off-axis / on-axis), m = 1..6: 0 failures. Non-vacuous: Delta^m J has order EXACTLY m in
  8/25 long-mixed, 7/25 long-off, 16/25 mont-mixed, 14/25 mont-off (bound sharp); on-axis order exactly m+1 in 17/25 long and
  25/25 mont (Cor 2.2a sharp). (Own walk generator is weak: 66/75 sums identically 0; reported, not counted as evidence.)
- Extra probe (ospref/ft_bigm.py, seed 707, stopped early to stay cheap): m = 7, 8 mixed flips on Montesinos words, 5/5 with
  order EXACTLY m (includes the non-automatic (8,7) case).
VERDICT claim 3: STANDS. (Independent of, and consistent with, Astra's integral proof recorded in BRIEF UPDATE 21:25.)

## 4. Claim 4 (on-axis corollary)
- Statement true; the builder's write-up mixes E (untwisted) and Etilde (twisted) and the 'scalar 2z / l_i' bookkeeping is
  muddled. Clean proof (referee): with only on-axis sites there are no loops, so by 2.3(e) every network evaluates at h = 0 to
  c_0 regardless of windings; the twisted site difference is (1+t^3)(Yhat - t^2) and (Yhat - t^2)|_{h=0} = sigma - 1 evaluates to
  c_0 - c_0 = 0. Hence Delta^T Etilde = O(h^{|T|+1}) for every sub-family T, so Etilde'_S(0) is CONSTANT, n_S is constant, and
  Delta^m J = e^{-nh/4} Delta^m Etilde / c_0 = O(h^{m+1}). (Equivalently: an on-axis flip shifts the UNtwisted normalising power by
  exactly the t^4 that Etilde absorbs.)
- CHECKED: on-axis order >= m+1 in 75/75 (above), exactly m+1 in 45/75.
VERDICT claim 4: STANDS (MINOR: rewrite the proof as above).

## 5. Claim 5 (parity defect)
- (a) R tensor Z at t=-1 = Z[s]/(s^2 - 2s) = Z[Z/2] via sigma = 1 - s (sigma^2 = 1 - 2s + s^2 = 1); Y-box (1,t^-3) -> (1,-1). OK.
- (b) Delta_3/Delta_1 = [4]/[2] = A^4 + A^-4 = t + t^-1 -> -2; (1,-2) sums to -1 = Delta_2(-1). OK.
- (c) Hopf ratio (KL) (-1)^b [(a+1)(b+1)]/[a+1] with a=1, b=2m: [2(2m+1)]/[2] = sum of 2m+1 powers of A^8 -> 2m+1. It is an
  honest polynomial (encircling loop acts on V_1 by a scalar), so no 0/0 at delta = 0. Unlinked: Delta_2m(-1) = (-1)^m. OK.
- (d) e_1^T Y = e_1^T at t=-1 (Y = [[1,0],[-1,-1]]); X = I. Equivalently a winding slid to a vertex acts by theta_1/(theta_1
  theta_2) = t^2 -> 1. OK.
- (e) Prop 2.3: re-derived. At h=0: z = 0 (colour-2 crossings free), a = 1 (kinks free), Yhat^2 = 1; homotopy of colour-2 curves in
  S^3 - axis = isotopy + crossing changes among colour-2 strands; free loop classes = winding in Z, Yhat changes winding by 1 and
  Yhat -> Yhat^-1 by 2, so parity is the invariant; odd loops -> meridian (3), even -> unlinked (-1); arc windings slide to a
  vertex (+1). Correct. Numerically implied by claim 6 checks below.
- Wording: 'parity defect' / '(-1)^F' is an interpretation; the PROVED content is (a)-(e). Fine as marked.
VERDICT claim 5: STANDS.

## 6. Claim 6 (top-order formula, independent recomputation)
- Derivation re-done: per site [h^1] of (R - R^-1) = 2(1 - E) (z = 2 sinh h), of (Yhat - Yhat^-1) = 2(2P_1 + P_3) = 2(3+sigma)/2;
  then Prop 2.3. Normalised version: n_S affine with d_i = -8 Sigma_i, f_i = e^{2 Sigma_i h}; Leibniz gives
  [h^m] Delta^m J = 2^m sum_T prod_{i in T}(-Sigma_i) Sigma(rest) (KL), times (-1)^m in lp's t = A^+4. Uses that Sigma(U) does
  not depend on the state of the other sites (true: at h=0 flipping is invisible). Single-site Sigma_i = +-2: correct.
- CHECKED (own code: ospref/statesum_ref.py = explicit state enumeration + curve tracing, written independently of the builder's
  matching/parity bookkeeping; ospref/c6_topm.py with own Z[zeta_8] arithmetic; seed 202; generators long/mont/walk, m = 1..5):
  raw identity [h^m] D = 2^m y_0(A_0) Sigma: 90/90; normalised formula vs lp.J moments: 90/90 (top coefficient nonzero in 24).
  Sigma nonzero in 90/90 (values -32..32, incl. 20, 26).
VERDICT claim 6: STANDS (as CHECKED; it is in fact PROVED given Prop 2.3, the builder's 3.1 says so).

## 7-8. GAP / CONJECTURE (status only)
- 7: the stated obstruction data are right: Delta_1(-1) = delta(-1) = 0; Yhat eigenvalue ratio t^-1/t^2 = t^-3 = -q^-3 (-> -1 only
  at q = 1). Correctly marked GAP. 2.5's phrase 'exact presentation ... PROVED' should read 'the coloured TL skein satisfies these
  relations' (no completeness of the relations is shown) (MINOR).
- 8: arithmetic checked: C_1 = 1/2 - C_0 on V gives C_0 - C_1 = -1/2 (even), 1 (odd) = 1/4 - (3/4) sigma; -2 x (-3/4) = 3/2 = the
  sigma-coefficient of Yhat = e^{h/2} sigma exp((3h/2) sigma). Correctly marked CONJECTURE (normalisation from memory).

## 9-10. Local knots and the reduction
- Proof of 9 (Schur: a ball meeting Theta in one colour-2 arc has skein space End(V_2) = C) is correct generically and hence as an
  identity of Laurent polynomials; both sides are = 1 mod (t+1)^2, so the units agree exactly. J_3(rL) = J_3(L) (colour 2 self-dual).
- CHECKED (own construction ospref/c9_local.py: long-knot half-words built from closed braid diagrams by the referee, NOT the
  builder's words; both kink letters x1 and y1): lp.J = J_3(L)(1/t) (own 2-cable J_3, KL) for 3_1, 3_1*, 4_1, 5_2, 6_1, 6_2, 6_3,
  T(3,4): 16/16; Delta_K = Delta_L^2 (3_1, 4_1).
- STRONGER product form CHECKED 24/24: L tied into the arc of a random (K0,h) (fs.gen long and Montesinos backgrounds, L in
  {3_1, 4_1, 5_2}): J = normalize(J(K0) * J_3(L)(1/t)). (This tests Schur in a nontrivial background.)
- iota = v_3(K) on local-knot inversions (F3 convention, ident3.VK): CHECKED 10/10 (incl. both Whitehead doubles, M_3 = +-1728).
- 10 (reduction): logic re-checked: J_3 = 1 mod (t+1)^2 => unit iff = 1 (t^k = (-1)^k(1 - k(t+1)) mod (t+1)^2); L # rL = O iff L = O
  (genus); every L occurs ((L # rL, swap) is strongly invertible). JC => Lemma Q (BRIEF, via 1.3 with even n and Gordon-Luecke)
  then gives JC => J_3 detects the unknot. Correct as stated; novelty/known status is for LIT.
VERDICT claims 9, 10: STAND.

## 11. Non-abelian example
- Independent route (ospref/c11_wh.py): own untwisted Whitehead double of the braid-closure trefoil (framing twists -3 and clasp
  on the OTHER band than whdouble.py), converted to a long-knot half-word, and lp.J computed DIRECTLY on (L # rL, swap) (2 s; no
  Schur, no 2-cable). Result (clasp x, the builder's L): V_L has a_2 = 0, v_3 = 2; |Delta_K(t)| stripped = 1 at t = 2, 3, 5, -1;
  J (KL) at t = -e^h: 1 + 0h + 0h^2 - 288 h^3 - 864 h^4 + 13536 h^5 + ... = the builder's J_3(Wh(3_1)) expansion EXACTLY.
  (Clasp y gives the other double: v_3 = -2, J = 1 + 288 h^3 + 2592 h^4 - 3168 h^5 + ...)
- Constituents of a local-knot inversion are arc u edge_i = L (both Delta = 1). Conclusion 'J is not a function of Alexander-type
  data of K and its constituents' follows. 'Non-abelian' is an interpretation (KNOWN: v_3 is not Alexander-determined).
VERDICT claim 11: STANDS.

## 12. iota fit
- Own constituents (ospref/c12_constit.py): K2 by a RIGHT-side closure (different diagram from constit.py's left closure; V agrees
  150/150), K1 by left closure with x0/y0 -> two crossings of the same letter with the inner axis edge. Handedness of that twist
  re-derived geometrically (doubling map w -> w^2/|w| on the (x,z)-plane is orientation preserving and keeps over/under away from
  the axis; x0 gives dtheta/dy < 0, same as sigma_0^2 with x letters) - consistent with flat_search.quotient_word.
- EXACT rational rank test on the 150 rows: iota - v_3(K) is NOT in span_Q{1, v3K, v3K1, v3K2} (rank 4 -> 5), nor in
  span_Q{1, v3K, v3K1, v3K2, a2K1, a2K2, a2K} (rank 7 -> 8); same with the K1 twist handedness flipped (robustness).
  So the builder's 'not a small-integer combination' is TRUE and in fact holds over Q. (A global mirror of the v3(K_i) cannot
  matter: the span is sign-symmetric.)
VERDICT claim 12: STANDS (can be upgraded to 'not a Q-linear combination, CHECKED 150').

## Verdict: STANDS_WITH_REPAIRS
Every PROVED claim (1, 2, 3, 4, 5, 9, 10) was re-derived line by line and survives; every CHECKED claim (6, 11, 12) was recomputed
with the referee's own code on independent samples/constructions and survives (12 in a stronger form). GAP 7 and CONJECTURE 8 are
correctly marked. No fatal or serious error found. Repairs (all MINOR, expository):
 R1 (claim 4) Cor 2.2a mixes E and Etilde: read literally, 'the leading part of Delta^T Etilde is c_0 prod l_i' with l_i from the
    scalar 2z is false (the TWISTED site difference has leading term 0). Replace by the clean proof in section 4 above (or use E
    throughout: then l_i = 4 and the normalisation shifts cancel, prod(l_i - l_i) = 0).
 R2 (claim 1) Say exactly what is PROVED: the N = -1 Dubrovnik specialisation at q = -t (and Brauer(-1) + super flip at q = 1).
    The match with the module category of U_q(osp(1|2)) in these parameters is KNOWN-with-reference-needed (sign conventions vary).
 R3 (claim 2) Proof (b) omits the writhe factor (A^8)^-w: add 'each crossing change moves w by +-2, so t^{2w} is multiplicative-
    affine and the Leibniz step of 2.2(iv) applies'.
 R4 (claim 3) Make (iii) self-contained with the one-line identity <Theta;1,1,2> = <T(1)> - delta^-1 <T(e)> = (delta^2-1) y =
    Delta_2 y, valid for any quotient tangle INCLUDING extra closed curves (it does not need T(1/0) = unknot); this covers the
    networks with loops directly, rather than citing proof/REPORT 0.2.
 R5 (2.5) 'Exact (non-perturbative) presentation, PROVED' overstates: only 'the coloured TL skein satisfies these relations' is
    shown (no completeness).
 R6 (3.1 remark, not in the claim list) 'NOT the sl_2 (colour-1) weight system: colour 1 has no expansion at t = -1' is not an
    argument that two weight systems differ; drop or support with a chord diagram where they differ.
 R7 (claim 12) Upgrade: not in span_Q{1, v3(K), v3(K1), v3(K2), a2(K), a2(K1), a2(K2)} (exact rank test, 150 rows, robust to the K1
    twist handedness).

## Referee scripts (ospref/, run with tools/venv/bin/python)
rlib.py (own bracket/writhe/2-cable/Jones/J_3), c2_j3.py (claim 2), gens.py (own sample generators), ft_check.py (claims 3/4),
ft_bigm.py (m = 7, 8), statesum_ref.py + c6_topm.py (claim 6), c6_sens.py (sensitivity), c9_local.py + c9_iota.py (claims 9/10),
c11_wh.py (claim 11), c12_constit.py + c12_robust.py (claim 12).
