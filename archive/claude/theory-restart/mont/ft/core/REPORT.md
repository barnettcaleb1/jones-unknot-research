# REPORT: lane CORE (class-free structure of the a_2 = 0 core)
(16 Nov 2026, Claude, lane CORE. Builds on ../BRIEF.md (F1, F2, F3, 1.3). Status tags: PROVED / CHECKED(n) / CONJECTURE / GAP / KNOWN / MEMORY.)

## 0. Summary
(a) SHAPE. F1 is D_7 = (t^4-1)(t^3+1) | J - 1 (core: (t+1) D_7). New: J'(1) = 8 Q(1) = sigma(T(1/n)) for odd n (PROVED from 1.3 +
    V'(1) = 0), so (t-1)^2 | J-1 iff sigma(L_odd) = 0; this FAILS in the core in general (examples with J'(1) = +-16). Rokhlin's
    congruence is automatic from F1. Moment formula M_k = -sum C(k,i)(7^i-4^i-3^i) q_{k-i} (q = moments of Q = (J-1)/D_7) PROVES
    M_3 = 0 mod 36 (F3's integrality), M_3/36 = a_2 mod 2, core M_3 = 0 mod 72, M_4 = 16 M_3 mod 288. No further cyclotomic factor
    is forced by classical evaluations. SPAN THEOREM (PROVED from F1): J != 1 => span J >= 4 (equality only for 1 + D_7 = J(LHT)
    and its mirror = J(RHT): attained); in the core span J >= 7 (sharp at the level of congruences). "span >= 7 always" is false
    (P(-2,3,7): 6, trefoil: 4); span(J-1) >= 7 / >= 8 hold trivially.
(b) NO second-order Mullins (PROVED mod 1.3 + Mullins/Casson/Montesinos): K = 6_2 has two inversions with equal j and M_3 = -612,
    +108; their branch sets T(1) both double cover S^3_{+1}(6_2) (same orientation), both have sigma = -8, but c_2 = 108 vs 228.
    Exact formula c_2(L_n) = 72 j^2 - 144 n j a_2 + n M_3/6 + 6 n^2 a_2: the involution enters through M_3. The suggested pair:
    Y = S^3_{+1}(4_1) = S^3_{-1}(RHT) is covered by P(-2,3,7) (sigma -8, c_2 180) and T(3,7)* (sigma +8, c_2 -48): opposite sigma,
    so that pair alone is not decisive. Pattern: for the two inversions of a 2-bridge knot, Delta M_3 in 360 Z with
    Delta M_3/360 = Delta j/2 mod 2 (CHECKED 76 pairs).
(c) Casson at order 2. From order 3 on the J-tower is not a function of {S^3_{1/n}(K)} (6_2 pair). With Lin-Wang's lambda_2 surgery
    formula (Geom. Topol. Monogr. 2 (1999) Thm 4.3, converted to our conventions and checked on 39/63/69) there is an EXACT identity
    c_2(L) = -lambda_2(Y) + 60 lambda^2 + 18 sigma lambda - 3 lambda + (9/8) sigma^2 + n(M_3/6 - 12 v_3) - 60 n^2 a_4; the n^2 a_4 term
    rules out any formula P(lambda, lambda_2, sigma) + (linear in n); the defect is 30 n (v_3 + iota) - 60 n^2 a_4, so F3's
    mod-5 integrality of iota is EQUIVALENT to a mod-30 "second-order Mullins congruence" on branch sets (CONJECTURE for all
    det-1 knots). The mod-5 congruence M_3/36 = 7 v_3(K) mod 5 is reduced to the Phi_5 part of Conjecture D below (c').
(c') DOUBLING CONGRUENCE (CONJECTURE D, CHECKED 4196, 0 failures): J(-t) = V_K(t^2) mod (t^2-1)(t^3-1)(t^5-1). All parts except Phi_5
    are PROVED (F1, M_2 = -24 a_2); the Phi_5 part J(xi) = V_K(xi^2) at primitive 10th roots is new. For two-bridge words it is PROVED
    up to a root of unity: at primitive 10th roots the TH-2BR representation is projectively conjugate to the Temperley-Lieb 4-plat
    representation of K at A^-4 = xi^2 (the eigenvalue match is exactly xi^5 = -1). It explains F3 exactly
    (iota = g(1) - 3 v_3, CHECKED 282) and gives a NEW necessary condition for a Lemma Q counterexample: V_K(e^{2 pi i/5}) = 1.
(d) Swap sums K' # rho K' (no axis letters) have J = normalised colour-2 coloured Jones of K' (PROVED; CHECKED on the trefoil).
    Hence Lemma Q contains "the colour-2 coloured Jones polynomial detects the unknot". With F2 on this family (CHECKED 40; proof via
    the so(3)/osp(1|2) correspondence, MEMORY; the direct integral R-matrix argument FAILS: Jordan block at q = i, computed), nontrivial
    C_{N+1}-trivial K' give nontrivial core (K,h) with M_1..M_N = 0: the tower vanishes to any finite order, so no finite-order,
    positivity (M_3, M_4 take both signs) or bounded-first-moment mechanism exists. J = 1 iff M_k = 0 for k <= span(J-1); C_n-claspers
    give (t+1)^n | J-1 but no leverage beyond that tautology. Mechanisms must be global (span/extreme coefficients), i.e. class-based.

## 1. (a) Divisibility and shape of J - 1

Notation. Lambda = Z[t,1/t]. Q := (J - 1)/D_7 where D_7 := (t+1)^2 (t-1)(t^2+1)(t^2-t+1) = (t^4 - 1)(t^3 + 1) (F1: Q in Lambda).
G := (J-1)/(1+t)^2 = (t-1)(t^2+1)(t^2-t+1) Q. q_m := sum_e Q_e (-1)^e e^m (moments of Q at t = -1), M_k as in BRIEF 1.2.
j := the exponent in 1.3 (V(L_n) = t^{12 j [n odd]} {...}); BRIEF/letter 63: j = -sigma(L_n)/8 for odd n.

1.1 PROPOSITION (t = 1 data; PROVED from 1.3 + V'(1) = 0 for knots). G'(1) = -2j, hence
      J'(1) = 4 G'(1) = -8 j = sigma(L_odd)   (BRIEF sign convention),   and   J'(1) = D_7'(1) Q(1) = 8 Q(1).
  So Q(1) = -j = sigma(L_odd)/8, and (t-1)^2 | J - 1  <=>  J'(1) = 0  <=>  sigma(T(1/n)) = 0 for odd n.
  Proof. For odd n, put t = e^u in 1.3: 1 - (-t)^{-n} = 2 - n u + ..., Phi_3 = 3 + 3u + ..., G(1) = 0 (F1), so
  V(L_n)(e^u) = (1 + 12 j u + ...)(1 + 6 G'(1) u + O(u^2)); V'(1) = 0 gives 12 j + 6 G'(1) = 0. J - 1 = (1+t)^2 G gives
  J'(1) = 4 G(1) + 4 G'(1) = 4 G'(1). D_7'(1) = 2^2 * 2 * 1 = 8. QED
  CHECKED(400): J'(1) = 8 Q(1) and Q(-1) = a_2(K) in all 400 random words (script a1_checks.py).
  Remarks. (i) sigma(L_n) is constant on each parity class (det L_n = 1 forces sigma in 8Z, a crossing change moves it by <= 2,
  and L_n -> L_{n-2} is one crossing change), and sigma(L_even) = sigma(L_0) = 0; this is consistent with 1.3 having one j.
  (ii) Q(1) = Q(-1) mod 2 holds for EVERY integer Laurent polynomial, so the Rokhlin congruence sigma(L_odd)/8 = mu(S^3_{1/n}(K))
  = a_2(K) mod 2 (KNOWN: Rokhlin of a det-1 branch set is sigma/8 mod 2, and mu(S^3_{1/n}(K)) = n Arf(K)) is AUTOMATIC from F1;
  it gives no new constraint (consistency check only).
  (iii) The (t-1)^2 question has a NEGATIVE answer, even in the core: CHECKED, core samples with J'(1) = +-16 (Q(1) = +-2):
  s.l1.x0.y2.y2.y1.y2.x0.x1.y2.y0.y0.x1.x0.u1 (Q(1) = 2), s.l1.x2.x0.x2.x2.x0.x0.x1.y2.x0.x1.x0.u2 (2),
  s.l1.y2.x1.y2.y1.y0.y2.x1.y0.y0.x1.u2 (-2); 3 of 13 core samples in a 400-word run. In the core Q(1) is EVEN (Q = (t+1)Q').
  So the best general statement is: (t-1)^2 | J-1 iff sigma(L_odd) = 0; a unit J (= 1) of course has sigma(L_odd) = 0.

1.2 PROPOSITION (moment formula; PROVED from F1 by an exponential generating function computation).
  D_7(-e^h) = (e^{4h}-1)(1-e^{3h}) = - sum_{k>=2} (7^k - 4^k - 3^k) h^k/k!, hence for every k
      M_k = - sum_{i=2}^{k} C(k,i) (7^i - 4^i - 3^i) q_{k-i}          (q_m = moments of Q, integers; q_0 = Q(-1) = a_2).
  M_2 = -24 q_0, M_3 = -72 q_1 - 252 q_0, M_4 = -(144 q_2 + 1008 q_1 + 2064 q_0).
  Consequences (PROVED): M_3 = 0 mod 36 and M_3/36 = -2 q_1 - 7 a_2 = a_2 mod 2 (this PROVES the integrality observed in F3;
  combined with F3's fit M_3/36 = 7 v_3 + 5 iota it forces iota = a_2 + v_3 mod 2); M_4 = -48 a_2 mod 144.
  Core (D_8 := (t+1) D_7 | J - 1, Q = (t+1)Q', q'_m moments of Q'): D_8(-e^h) = sum_{k>=3} (8^k - 7^k - 5^k + 3^k + 1) h^k/k!, so
      M_k = sum_{i=3}^{k} C(k,i)(8^i - 7^i - 5^i + 3^i + 1) q'_{k-i};  M_3 = 72 q'_0,  M_4 = 288 q'_1 + 1152 q'_0 = 288 q'_1 + 16 M_3.
  CHECKED(400): M_3 = 0 mod 36 in all 400; core M_3 = 0 mod 72 in all 13 core samples.
  Interpretation: F1 is EQUIVALENT to the statement that the moment vector (M_k) lies in the image of Q -> 1 + D_7 Q; all
  congruences among moments implied by classical evaluations are of this form.

1.3 Other classical evaluations (status of each).
  - V'(1) = 0: used in 1.1 (gives J'(1) = sigma(L_odd), a RELATION with a non-K invariant, not a constraint on J).
  - V''(1) = -6 a_2(L_n): gives a formula, not a constraint. For even n: a_2(L_n) = 2 n j = -n sigma(L_odd)/4 (PROVED from 1.3:
    V(L_n)(e^u) = 1 + 3 n G'(1) u^2 + O(u^3)); for odd n: a_2(L_n) = 24 j^2 + 6 j - 2 n j - G''(1). Arf(L_n) = 0 (det 1) is
    automatic (G''(1) is even for every integer Laurent G).
  - v_3(L_n) in Z: automatic from V(L_n)(i) = 1 (for any knot polynomial V - 1 = (1-t)(1-t^3) W, and v_3 in Z <=> W'(1) even,
    which follows from V(i) real).  - V'(-1) (Mullins): gives back M_2 = -24 a_2 (the sigma terms cancel identically, so
    Mullins at first order says nothing about j).  - V(e^{2 pi i/3}) = 1: automatic (Phi_3 divides the correction term).
  - By Jaeger-Vertigan-Welsh (KNOWN) the classically computable points are t in {+-1, +-i, e^{+-2 pi i/3}, e^{+-pi i/3}};
    all are used. CONCLUSION: no further cyclotomic factor of J - 1 is forced by classical evaluations; D_7 (resp. D_8 in the core)
    is the full classical divisibility, and (t-1)^2 is NOT forced (examples above).
1.4 SPAN BOUNDS (PROVED from F1 alone; scripts a2_span.py, a3_span_proof.py).
  Trivial part: J != 1 => span(J - 1) >= deg D, i.e. >= 7 always, >= 8 in the core, >= 9 in the core with sigma(L_odd) = 0.
  For span(J) itself (the meaningful quantity; note P(-2,3,7) has span J = 6 < 7, so "span J >= 7 always" is FALSE):
  Lemma. If J = 1 mod D and span(J) < deg D, then J = t^{-c} R_c where R_c is the remainder of t^c mod D (deg R_c < deg D).
    Proof: write J = t^{-c} P, P a polynomial with P(0) != 0, deg P = span J < deg D; then P = t^c mod D. QED
  On each residue class c = r mod 12 the coefficients of R_c are polynomials in c of degree < a (D = (t+1)^a (t-1)^b (t^2+1)(t^2-t+1)),
  by CRT (t^c mod Phi_1^b Phi_4 Phi_6 depends on c mod 12 polynomially of degree < b; t^c mod (t+1)^a = (-1)^c sum_{i<a} C(c,i)(-(t+1))^i).
  The c-leading term is +-(t+1)^{a-1}(t-1)^b(t^2+1)(t^2-t+1)/const, of degree deg D - 1 with nonzero constant term, so
  span(R_c) = deg D - 1 except where the top or the constant coefficient (a polynomial in c, interpolated exactly) vanishes.
  All such c were found exactly (sympy roots of the interpolants) and evaluated:
    THEOREM (span). Let J satisfy F1 (D_7 | J - 1) and J != 1. Then span(J) >= 4, with equality only for J = t^7 + t^4 - t^3
      (= 1 + D_7) and its mirror t^-7 + t^-4 - t^-3; span 5 occurs for exactly 4 more J (c in {-6,-5,11,12}); all others >= 6.
    In the CORE (D_8 | J - 1), J != 1  =>  span(J) >= 7, and EVERY J = t^{-c} R_c with c not in [0,7] has span exactly 7
      (an infinite family, so 7 is sharp at the level of congruences).
    Core with sigma(L_odd) = 0 (D_9 := (t+1)^3 (t-1)^2 (t^2+1)(t^2-t+1) | J-1): span(J) >= 7 (4 values of c), generically 8.
    sigma(L_odd) = 0 without a_2 = 0 ((t+1)^2(t-1)^2(..)): span >= 6, equality only at J = t^4 + t^6 - t^10 and its mirror.
  Data: observed minimum spans are larger (core Montesinos necklaces: 10; integrator survey), so these bounds are not tight on
  realised J's. They are what the classical evaluations alone give.

## 2. (b) Second-order Mullins: is [h^2] V_L(-e^h) determined by Sigma_2(L), sigma(L)?

Notation. For a det-1 knot L write V_L(-e^h) = 1 + c_1(L) h + c_2(L) h^2 + ... (V_L(-1) = 1 for det-1 knots, since V(-1) = Delta(-1)
= 1 mod 4). c_1 = -V'(-1), c_2 = V''(-1) - V'(-1). Mirror: c_1 -> -c_1, c_2 -> c_2.
Mullins (Topology 32 (1993); KNOWN, normalisation fixed internally below): lambda(Sigma_2 L) = (1/12) V_L'(-1)/V_L(-1) - sigma(L)/8.

2.1 PROPOSITION (branch-set expansion; PROVED from 1.3 by expanding at t = -e^h).
      V(L_n)(-e^h) = e^{12 j h} [ 1 + (n M_2/2) h + (n M_3/6 - n^2 M_2/4) h^2 + O(h^3) ]   (j := j [n odd]), i.e.
      c_1(L_n) = 12 j - 12 n a_2,        c_2(L_n) = 72 j^2 - 144 n j a_2 + n M_3/6 + 6 n^2 a_2.
  Proof: 1 - (-t)^{-n} = 1 - e^{-nh} = nh - n^2h^2/2 + ..., Phi_3(-e^h) = 1 + h + ..., G(-e^h) = (J(-e^h) - 1)/(e^h - 1)^2
  = (M_2/2 + M_3 h/6 + ...)/(1 + h + ...). Multiply out. QED
  CHECKED(24): exact agreement for L_n, n in {+-1,+-2,+-3}, of RHT, LHT and both inversions of 4_1 (b3_branch.py).
  Consequence: Mullins at order 1 reproduces lambda(S^3_{1/n}(K)) = n a_2 for every n, j (sigma terms cancel); this pins the
  internal normalisation: with sigma = sigma_B (BRIEF, = KnotInfo sign: sigma(T(3,5)) = -8 below) and Sigma_2(L_n) = S^3_{1/n}(K),
  lambda(Sigma_2 L) = (1/12)V'(-1) - sigma/8 = -c_1/12 - sigma/8.

2.2 THE SIGMA(2,3,7) / POINCARE SPHERE DATA (CHECKED, exact; b2_small.py, b3_branch.py).
  Half-words: RHT = s.l1.y0.x1.u2 (J = t^-7 + t^-4 - t^-3, j = 1); 4_1 has two inversions, h1 = s.l1.y0.y0.x1.u2 (j = 1, M_3 = -180)
  and h2 = s.l1.x0.x0.y1.u2 = mirror of h1 (J(t) -> J(1/t); j = -1, M_3 = +180).
  Branch sets identified by V (and Sigma_2 by Casson; T(3,5) and P(-2,3,7) V's match the knots, P(-2,3,7) also by Alexander/det):
     RHT:    L_1 = T(3,5) (Sigma_2 = S^3_{+1}(RHT), lambda = +1),   L_{-1} = P(-2,3,7) (S^3_{-1}(RHT), lambda = -1)
     4_1 h1: L_1 = P(-2,3,7) (S^3_{+1}(4_1), lambda = -1),          L_{-1} = T(3,7)   (S^3_{-1}(4_1), lambda = +1)
     4_1 h2: L_1 = T(3,7)*   (S^3_{+1}(4_1), lambda = -1),          L_{-1} = P(-2,3,7)* (lambda = +1)
  So the oriented manifold Y := S^3_{+1}(4_1) = S^3_{-1}(RHT) (= Sigma(2,3,7) up to orientation; lambda(Y) = -1) is the double
  branched cover of BOTH P(-2,3,7) (sigma = -8, c_1 = 24, c_2 = 180) and T(3,7)* (sigma = +8, c_1 = 0, c_2 = -48).
  (V(P(-2,3,7)) = t^5 + t^7 - t^11 + t^12 - t^13 from kauffman.bracket(mont(1,[3,7])); V(T(3,7)) = t^6 + t^8 - t^14.)
  Observation: the two branch sets of the same oriented Y have OPPOSITE signatures, so this pair alone cannot decide whether c_2 is
  a function of (Sigma_2, sigma): c_2(P) - c_2(T*) = 228 could be a sigma-effect. A decisive test needs equal sigma (2.3).
2.3 THEOREM (b), NEGATIVE ANSWER (PROVED modulo BRIEF 1.3 and the KNOWN inputs Mullins/Casson/Montesinos trick):
  the h^2 coefficient c_2 of V_L(-e^h) is NOT determined by (Sigma_2(L), sigma(L)) for det-1 knots L.
  Witness. K = 6_2 (the chirality with V_K = t^-1 - 1 + 2t - 2t^2 + 2t^3 - 2t^4 + t^5), two strong inversions
     h  = s.l1.y0.x1.y0.x1.u2      J = t^-10 - t^-9 + 2t^-7 - 2t^-6 + t^-5 + t^-4 - 2t^-3 + t^-2,   j = 1, a_2 = -1, M_3 = -612
     h' = s.l1.x0.x0.x0.x1.x1.u2   J = t^-7 - t^-5 + 2t^-4 - t^-3 - t^-2 + 2t^-1 - 1 + t^2 - t^3,    j = 1, a_2 = -1, M_3 = +108
  L := T_h(1),  V_L  = t - t^2 + t^3 + t^6 - t^7 + t^8 - t^9 (det 1):                     c_1 = 24, c_2 = 108
  L':= T_h'(1), V_L' = t^4 + t^7 - t^8 + t^9 - t^10 + t^12 - t^13 + t^14 - t^15 (det 1): c_1 = 24, c_2 = 228.
  Both double cover Y = S^3_{+1}(6_2) with the same orientation (Montesinos trick; the slope 1/1 and the orientation are confirmed by
  Mullins = Casson: lambda = -1 for both, and Y is chiral since lambda != 0), and sigma(L) = sigma(L') = -8 j = -8 (2.1/1.1).
  Proof that both words give the same knot: a word s.l1.W.u2 with W over {y0,x0,x1,y1} is a 4-plat (push the top arc through
  infinity: caps (m1,m0),(0,1), middle twists y0/x0, outer twists x1/y1 paired, cups (m0,0),(m1,1)), hence a two-bridge knot,
  hence alternating, so span V_K = crossing number = 6 (Kauffman-Murasugi-Thistlethwaite); det = |V_K(-1)| = 11; the two-bridge
  knots of det 11 are T(2,11), 7_2, 6_2 (up to mirror), so K = 6_2, with chirality fixed by V_K. The J's differ, so h, h' are
  inequivalent (the two strong inversions of a two-bridge knot). n = -1 and n = 2 give further such pairs (c_2 = 24 vs -96 and
  -228 vs 12). QED
  What enters (PROVED, from 2.1): with lambda = n a_2(K) (Casson) and sigma = -8j,
      c_2(L_n) = (9/8) sigma^2 + 18 sigma lambda + 6 n lambda + n M_3/6,     M_3 = 36 (7 v_3(K) + 5 iota)  (F3 fit).
  The only datum not determined by (K, n, sigma) is M_3(K,h), an equivariant order-3 invariant: the covering involution enters
  exactly through M_3 at second order (through iota, if F3's fit is exact). (Note 6 n lambda = 6 n^2 a_2 is not a function of
  (Y, sigma) either unless a 3-manifold invariant of S^3_{1/n}(K) supplies an n^2 a_2 term; the 6_2 pair has the same K, n, so
  this ambiguity does not affect the counterexample; 3.5 gives the exact comparison with lambda_2.)
2.4 PATTERN (CHECKED: all 64 two-bridge knots with two inversions in the length <= 7 enumeration, 76 pairs; b5_verify.py).
  For the two inversions h, h' of one two-bridge knot: Delta M_3 is a multiple of 360 and Delta M_3/360 = Delta j/2 mod 2
  (Delta j in {0, 2, 4}). Equivalently (with M_3/36 = 7 v_3 + 5 iota): Delta iota in 2Z and Delta iota = Delta j mod 4.
  CONJECTURE: iota - j mod 4 depends only on K (two-bridge case at least).

## 3. (c) J-tower vs 3-manifold invariants of S^3_{1/n}(K)

3.1 Order 2 (PROVED; BRIEF 1.2 + Casson): M_2 = -24 a_2(K) = -(24/n) lambda(S^3_{1/n}(K)) for every n != 0 (Casson's surgery formula
  lambda(S^3_{1/n}(K)) = n a_2(K), KNOWN). Equivalently M_2 = 4 V_K''(1). Branch-set form: c_1(L_n) = -12 lambda(Sigma_2 L_n) - (3/2) sigma(L_n).

3.2 Dictionary between the J-tower and the branch-set tower (PROVED from 1.3). Put Psi(h) := Phi_3(-e^h) G(-e^h) = sum_i psi_i h^i;
  psi_i is a Q-linear combination of M_2, ..., M_{i+2} (G(-e^h) = sum_{i>=0} M_{i+2} h^i/(i+2)! divided by ((e^h-1)/h)^2). Then
      V(L_n)(-e^h) = e^{12 j [n odd] h} [ 1 + (1 - e^{-nh}) Psi(h) ]      EXACTLY (for even n there is no unit at all),
  so [h^k] e^{-12jh} V(L_n)(-e^h) = sum_{m=1}^{k} (-1)^{m+1} (n^m/m!) psi_{k-m}: a polynomial of degree k in n whose n^m coefficient
  involves only M_2..M_{k-m+2}. The J-tower is the n-linear part of the branch-set tower: M_{k+1} = (k+1)! [n^1][h^k](...) + lower.
  Degree comparison with an Ohtsuki-order-D invariant Lambda of S^3_{1/n}(K) (Aarhus/LMO heuristics, MEMORY): there the n^l coefficient
  comes from Kontsevich-integral diagrams of degree D + l with 2l legs, i.e. has knot order D + l. For D = 1 this is Casson
  (n^1 a_2), matching c_1. For c_2: the n^1 coefficient has (equivariant) order 3 (M_3/6 + 18 sigma a_2), compatible with the n^1 part
  of lambda_2 (order 3, v_3-type); but the n^2 coefficient of c_2 is 6 a_2 (order 2), while the n^2 coefficient of lambda_2 has
  order 4 (wheel w_4 / Alexander a_4 and a_2^2 parts; MEMORY). So a "second-order Mullins" c_2 = alpha lambda_2(Sigma_2) + f(lambda, sigma)
  is impossible with alpha != 0 unless the a_4-part of the n^2 coefficient of lambda_2 vanishes. RESOLVED in 3.5 against the source
  (Lin-Wang Thm 4.3: the n^2 coefficient contains -60 c_4): no such formula exists (3.5 Corollary 1).

3.3 Order 3: the J-tower is NOT a function of the 3-manifolds (PROVED, from 2.3). The 6_2 pair has the same K (hence the same
  S^3_{1/n}(K) for all n) and the same sigma(L_n) for all n (same j), but M_3 = -612 vs +108. So no formula
  M_3 = F({S^3_{1/n}(K)}_n, {sigma(L_n)}_n) exists; any relation with lambda_2 must be "K-part + equivariant part".
  Where the K-part sits: (CHECKED 300 + F3's 150) M_3 = -7 (V_K'''(1) + 3 V_K''(1)) mod 180, i.e. M_3/36 = 7 v_3(K) mod 5 (this is
  exactly F3's "iota is an integer"). Using 1.2 (M_3/36 = -2 q_1 - 7 a_2) it reads   q_1 + q_0 + v_3(K) = 0 mod 5   (q_m = moments of
  Q = (J-1)/D_7). Source: it is the h^3-shadow of the doubling congruence 3.6 (Conjecture D), which gives iota = g(1) - 3 v_3 and
  M_3 = -288 v_3 (mod 180); mod 180 the order-3 moment is a knot invariant of K, and only this residue can be matched with the
  v_3-term of the lambda_2 surgery formula (3.5).
  Also CHECKED(300): M_1 = N_1, M_3 = N_3 mod 4 and M_2 = N_2, M_4 = N_4 mod 2, where N_k := sum_e V_{K,e} (-1)^e e^k (c3_mod5.py).
3.4 Constituent knots do not explain the equivariant part (CHECKED, negative): with K_in = k u A_in and K_out = k u A_out (the two
  constituent knots of the quotient theta-curve containing the arc; c1_constituents.py builds them from the half-word), M_3 is NOT
  a rational linear combination of {1, a_2, v_3} of K, K_in, K_out and j (exact least squares on 150 random words: no exact fit;
  c2_fit3.py). Two-bridge words have K_out = unknot; e.g. RHT gives K_in = LHT, 4_1 h1 gives K_in = T(2,5) (one chirality),
  6_2 h gives K_in = mirror 6_2, 6_2 h' gives K_in = a det-11 7-crossing knot (7_2 by V).

3.5 THE lambda_2 COMPARISON (PROVED modulo BRIEF 1.3 and Lin-Wang's surgery formula; CHECKED 36/36, c4_lambda2.py).
  Source: X.-S. Lin, Z. Wang, "Fermat limit and congruence of Ohtsuki invariants", Geom. Topol. Monogr. 2 (1999) 321-332, Thm 4.3
  (read from the paper): lambda_1(S^3_{K,1/n}) = -n v_2(K), lambda_2(S^3_{K,1/n}) = (n/2) v_2 - (n/3) v_3 + n^2 [v_2 + (5/3) v_2^2 - 60 c_4],
  v_i = i-th derivative of V(K; e^h) at h = 0 in THEIR convention, c_4 = z^4 Conway coefficient; Example 4.4: lambda_2 = 39 for
  +1 surgery on the right-handed trefoil (Poincare sphere), 63 for +1 on the left-handed trefoil (Sigma(2,3,7)).
  Convention match: their V(K;t) is our V_K(1/t) (they assign t + t^3 - t^4 to the left-handed trefoil; ours, standard skein, to the
  right-handed one; independent check: our K with V = t + t^3 - t^4 has S^3_{+1}(K) = Sigma_2(T(3,5)) = Poincare sphere, so it is the
  RH trefoil). Hence in OUR notation (v_3 = -(V'''(1)+3V''(1))/36, lambda = Casson = lambda_1/6):
      lambda_2(S^3_{1/n}K) = -3 n a_2 - 12 n v_3 + n^2 (-6 a_2 + 60 a_2^2 - 60 a_4).
  Consistency: reproduces 39 (S^3_{+1}RHT) and 63 (S^3_{+1}LHT); S^3_{-1}(RHT) and S^3_{+1}(4_1) both give 69 = 63 + 6, matching
  lambda_2(-M) = lambda_2(M) + lambda_1(M) and our 2.2 finding that both are the same oriented Y (covered by P(-2,3,7)).
  THEOREM (exact second-order branch-set identity). For every strongly invertible (K,h), n != 0, Y = S^3_{1/n}(K), L = T(1/n),
  lambda = lambda(Y), sigma = sigma(L):
      c_2(L) = -lambda_2(Y) + 60 lambda^2 + 18 sigma lambda - 3 lambda + (9/8) sigma^2  +  n (M_3/6 - 12 v_3(K)) - 60 n^2 a_4(K).
  Proof: 2.1 + the displayed lambda_2 formula, with lambda = n a_2, sigma = -8j [n odd]. QED (verified exactly on 36 branch sets:
  RHT, LHT, 4_1 x2, 6_2 x2, n = +-1, +-2, +-3).
  COROLLARY 1 (no exact second-order Mullins; PROVED mod Lin-Wang). There is no polynomial P(lambda_1, lambda_2, sigma) (Ohtsuki order
  <= 2 in the manifold, any degree in sigma) with c_2(L_n) = P(Y_n, sigma) + n E_1(K,h) + E_0(K,h) for invariants E_i of (K,h):
  comparing n^2-coefficients on odd n (sigma constant) gives alpha(-6 a_2 + 60 a_2^2 - 60 a_4) + 36 beta a_2^2 = 6 a_2 for all strongly
  invertible K (alpha = coefficient of lambda_2, beta of lambda_1^2); RHT (a_2,a_4) = (1,0) and 4_1 (-1,0) force alpha = -1,
  beta = 5/3, and then T(2,5) (3,1) fails (78 != 18). The obstruction is the n^2 a_4 term (wheel/Alexander part of lambda_2).
  COROLLARY 2 (mod-30 second-order Mullins congruence on branch sets). The defect n(M_3/6 - 12 v_3) - 60 n^2 a_4 = 30 n (v_3 + iota)
  - 60 n^2 a_4 (iota := (M_3/36 - 7 v_3)/5). Hence
      c_2(L) = -lambda_2(Sigma_2 L) + 60 lambda^2 + 18 sigma lambda - 3 lambda + (9/8) sigma^2   (mod 30)   for all branch sets L = T(1/n)
  <=> iota in Z for all (K,h) <=> M_3/36 = 7 v_3 (mod 5): EQUIVALENT to F3's integrality (CHECKED 450 random + all 36 above).
  CONJECTURE (second-order Mullins congruence): the displayed mod-30 congruence holds for EVERY knot L with det L = 1. The exact
  defect is the involution datum. Example: Y = S^3_{+1}(4_1): T(3,7)* has defect +30, P(-2,3,7) has defect -30 (iota = +-1).

3.6 THE DOUBLING CONGRUENCE (CONJECTURE D; partly PROVED; CHECKED 4196 nontrivial cases; c5_doubling.py, c6_factor.py, c7_phi5.py,
  c8_iota.py, c9_swap_doubling.py). For every strongly invertible (K,h):
      J(K,h)(-t) = V_K(t^2)   mod   (t^2 - 1)(t^3 - 1)(t^5 - 1) = Phi_1^3 Phi_2 Phi_3 Phi_5      (in Lambda).
  Equivalently: J(xi) = V_K(xi^2) for xi = 1, for xi a primitive 6th root and for xi a primitive 10th root of unity, and
  J(-e^h) = V_K(e^{2h}) + O(h^3).
  Status of the parts. Phi_1^3: M_0 = 1, M_1 = 0, M_2 = 4 V_K''(1) (BRIEF 1.2) - PROVED. Phi_2: J(1) = 1 = V_K(1) (F1) - PROVED.
  Phi_3: J(e^{-+ i pi/3}) = 1 (F1 and complex conjugation) = V_K(e^{+-2 pi i/3}) (Jones) - PROVED. Phi_5: J(xi) = V_K(xi^2) for primitive
  10th roots xi - NEW, CHECKED: all 3668 nontrivial two-bridge words of length <= 7, 528 nontrivial random words (lengths 6-20),
  60 swap sums; 0 failures. Exact equality J(-t) = V_K(t^2) occurred only for unknots (118/118). Phi_7 does NOT divide in general
  (0/60 swap sums), so the pattern stops at r = 5 (V at the Fibonacci root).
  Discovery route: D_k := M_k - 2^k sum_e V_{K,e} e^k is 0 for k <= 2 and has gcd 180, 720, 300, 5400, 420, 10080 for k = 3..8 over 300
  random words; exactly the divisibility forced by f = (t^2-1)(t^3-1)(t^5-1) g, since f(e^h) = 30 h^3 (1 + 5h + ...) g(e^h).
  CONSEQUENCES (conditional on the Phi_5 part; all CHECKED where stated):
  (1) F3 EXPLAINED: with g := (J(-t) - V_K(t^2))/((t^2-1)(t^3-1)(t^5-1)) in Lambda, iota = g(1) - 3 v_3(K) (CHECKED 282/282), so iota
      is an integer and M_3 = -288 v_3 (mod 180), i.e. M_3/36 = 2 v_3 (mod 5). So F3's "genuinely equivariant part" is g(1).
  (2) NEW NECESSARY CONDITION FOR COUNTEREXAMPLES: if J(K,h) = 1 then V_K(zeta) = 1 for every primitive 5th root of unity zeta
      (Phi_5 | V_K - 1), besides a_2(K) = 0. (A counterexample to Lemma Q must have trivial Jones polynomial at the Fibonacci root.)
  (3) The mod-30 second-order Mullins congruence of 3.5 (Corollary 2) follows (it is equivalent to iota in Z).
  (4) Swap family (4.2): I(K')(-t) = V_{K'}(t^2)^2 mod (t^2-1)(t^3-1)(t^5-1) for every knot K' (CHECKED 60/60), i.e. the colour-2
      coloured Jones polynomial at a primitive 10th root xi equals V_{K'}(xi^2)^2. A pure statement about coloured Jones polynomials
      (may be KNOWN; LIT lane).
  TWO-BRIDGE MECHANISM (PROVED up to a root of unity; c10_2br_mechanism.py, c11_exact_char.py). For s.l1.W.u2 (W over y0,x0,x1,y1)
  the Kauffman bracket of K is <K> = (1, delta) M(W) (1,0)^T in the 2-dim matching space {a = (12)(34), b = (14)(23)} of the 4-plat,
  with y0 -> Y_V = A^-1 + A U_2, x1 -> X_V = (A + A^-1 U_1)^2, U_1 = [[delta,1],[0,0]], U_2 = [[0,0],[1,delta]] (CHECKED 40/40 against
  kauffman.bracket). Claim: if xi is a primitive 10th root of unity and A^-4 = xi^2, then rho_J(g)(xi) = chi(g) P M(g) P^-1 for a
  fixed P and a character chi of F_2 = <X,Y>. Proof: tr^2/det agree on X, Y, XY, XY^-1 identically modulo A^10 = -s (xi = s A^-2),
  computed exactly; tr[X,Y] - 2 = +-(A-1)^2(A+1)^2(A^2+1)^2(A^4+1)/A^6 != 0 at these A, so both representations are irreducible and
  (Fricke characters) projectively conjugate. The generators' eigenvalue ratios match ( -xi <-> xi^-4 for X, xi^-3 <-> -xi^2 for Y)
  EXACTLY BECAUSE xi^5 = -1, and the matching sends the right eigenvector e_1 of X (eigenvalue 1) to a (eigenvalue A^-6) and the left
  eigenvector e_1^T of Y to (1, delta) (eigenvalue -A^3); the empty word fixes the constant. Hence
      e_1^T rho_J(W)(xi) e_1 = (-A^-3)^{n_Y - n_Y^-1} A^{6 (n_X - n_X^-1)} <K_W>(A)     (TH-2BR matrix element; y0 <-> Y, x1 <-> X,
                                                                                   x0, y1 <-> inverses; on the V side X_2 = Y_2^-1 exactly),
  so J(xi) = u(W) V_K(xi^2) with u(W) a root of unity (normalisation units and writhe), and |J(xi)| = |V_K(xi^2)| is PROVED for this
  class. u(W) = 1 is CHECKED on all 3668 nontrivial words of length <= 7 (not proved: needs the unit bookkeeping of TH-2BR's span
  formula against the writhe). Reading: at primitive 10th roots the J-automaton IS the Jones automaton of K at the squared parameter.
  PROOF ROUTE in general (GAP): the Phi_3 part is F1, proved through the branch sets and Lickorish-Millett (Z/3 homology of Sigma_2). The Phi_5
  part should be its level-3 analogue: by 1.3 it is equivalent to an expression of V(T(1/n)) at primitive 10th roots in terms of
  V_K at 5th roots, i.e. of the SO(3)_3 = Fibonacci invariant of S^3_{1/n}(K) (whose surgery formula only involves V_K(zeta_5),
  since at level 3 colour 2 = colour 1 (x) simple current). Candidate inputs: Jones' theorem on the Kauffman polynomial at
  2cos(2 pi/5) (Z/5 homology of the double branched cover; Comm. Math. Phys. 125 (1989), MEMORY) and the so(3)/osp(1|2) correspondence.

## 4. (d) The reduction question (equivariant claspers, mechanisms)

4.0 Exact reformulations (PROVED). For any (K,h): J = 1 <=> M_k = 0 for all k <=> M_k = 0 for 1 <= k <= s, s := span(J - 1)
  (support including 0): a Laurent polynomial t^a P(t), deg P = s, P != 0, has a zero of order <= s at t = -1.
  <=> V(T(1/n)) = 1 for one (every) n != 0 in the core (BRIEF 1.3) <=> Q' = (J-1)/D_8 = 0 (core).
  First nonzero moment k_0 := min{k : M_k != 0}. In the core k_0 >= 3, and if J != 1 then k_0 <= span(J - 1) (the only "degree
  bound", and it is tautological). By 1.2, M_{k_0} = 72 C(k_0,3) q'_{m_0}, m_0 = k_0 - 3 = first nonzero moment index of Q'.
  Data (d2_core_tower.py, 60 random core words, all with V_K != 1): k_0 = 3 in 59, k_0 = 4 in 1
  (s.l1.x1.y0.x1.x0.y1.y1.y1.y0.x2.y0.y1.x2.y0.y0.u1, M_4 = -15552, span J = 16).

4.1 Positivity: NEGATIVE (CHECKED). With mu_J := sum_e (-1)^e J_e delta_e (a signed measure of mass 1, mean 0), M_k are its moments and
  M_2 = variance. If mu_J >= 0 (sign-alternating J) then M_2 = 0 forces J = 1, so Lemma Q would be trivial for such (K,h) (and a_2 < 0
  unless J = 1); but J is not sign-alternating even for two-bridge knots (trefoil: mu = -delta_-7 + delta_-4 + delta_-3). In the core
  the first two candidate orders have no sign: M_3 is chirality-odd (30 positive / 29 negative in the sample) and M_4 (= the 4th
  cumulant kappa_4 = M_4 - 3 M_2^2 in the core) takes both signs (37 negative / 23 positive). No positivity at orders <= 4.

4.2 THE SWAP SUB-FAMILY (PROVED; this is the main structural point of section 4).
  Setting: K' any knot, rho a rotation by pi about an axis disjoint from K', K = K' # rho(K') joined by two bands crossing the axis;
  h = the rotation (swapping the summands). Half-words with no axis letters x0, y0 realise exactly these (CHECKED: V_K = V_{K'}^2 in
  40/40 random such words, K' = K_out = K_in from c1_constituents.py).
  (i) J(K' # rho K', swap) = I(K') := the normalised colour-2 (3-dimensional) coloured Jones polynomial of K'.
     Proof: the quotient theta-curve is the trivial theta-curve with K' tied locally into the colour-2 edge; a local knot in a
     coloured edge contributes the scalar <K';2>/<U;2> (Schur), and the normalisation J = 1 mod (t+1)^2 removes the framing unit.
     CHECKED(1): K' = RH trefoil (word s.l2.x1.x1.y2.u1): J = t^-11 - t^-10 - t^-9 + t^-8 - t^-7 + t^-5 + t^-2 = the known
     N = 3 coloured Jones of the trefoil q^2 + q^5 - q^7 + q^8 - q^9 - q^10 + q^11 (MEMORY) under q <-> 1/q.
  (ii) F2 on this family = the Vassiliev property of the t = -1 Taylor series of the colour-2 coloured Jones polynomial I(K').
     CHECKED(40): Delta^m M_k = 0 for m > k on 40 swap words (m = 3..5 random arc flips, 0 violations; order attained at m = k in
     13 of 40; d5_swap_ft.py). Status of a proof:
     - The naive Birman-Lin argument FAILS in the integral Weyl-module model (GAP located; d4_Rmatrix.py): the integral R-matrix of
       U_q(sl_2) on V(2) (x) V(2) (divided-power basis, entries in Z[q^+-1]) has characteristic polynomial
       (x - q^2)^5 (q^2 x + 1)^3 (q^4 x - 1) (eigenvalues 1, 1, -1 on channels 0, 2, 4 at q = i, as in BRIEF F2), but at q = i
       (t = -1) it is NOT an involution: (R - 1)^2 (R + 1) = 0 while (R - 1)(R + 1) != 0 (a Jordan block between channels 0 and 2;
       V(2) is not semisimple at q = i: E v_1 = [2] v_0 = 0). So "R = R^-1 at t = -1" is false at the level of R-matrices.
     - A valid route (PROVED modulo a KNOWN correspondence, MEMORY: Blumen; Clark-Wang; the uncoloured osp(1|2) link invariant equals
       the so(3) (= sl_2 colour 2) invariant at -q): on the osp(1|2) side the (1|2) representation is semisimple near the classical
       point q = 1 and R(1) is the super flip, an involution, so R - theta^2 R^-1 = O(q - 1) and m-fold alternating sums are
       O((q-1)^m); the equality of invariants transfers this to O((t+1)^m) for I. (Only invariants, not R-matrices, need to agree,
       which is consistent with the Jordan block above.) Taking m = 1, 2 then gives I = 1 mod (t+1)^2, so J = I with no extra unit.
     So M_k(K' # rho K') is a Vassiliev invariant of K' of order <= k (modulo that correspondence). It is NOT the t = 1 series:
     J(-t) != unit * J(t) in 40/40 swap words (d1_swap.py).
  (iii) Lemma Q restricted to the family <=> "the colour-2 coloured Jones polynomial detects the unknot" (J unit <=> J = 1 <=> I(K') = 1;
     K' # rho K' trivial <=> K' trivial). In the core: a_2(K) = 2 a_2(K'), so the core part is detection among knots K' with a_2 = 0.
     (Combined with JC => Lemma Q (BRIEF): JC implies that I detects the unknot. The literature status of "I detects the unknot" is
     for the LIT lane; I believe it is open.)
  (iv) COROLLARY (the tower can vanish to any finite order; PROVED modulo (ii) and the KNOWN existence of nontrivial knots all of
     whose Vassiliev invariants of order <= N are those of the unknot, for every N: Ohyama (Proc. AMS 1995), Habiro (Geom. Topol. 4
     (2000), C_{N+1}-trivial knots); it does NOT need the full F2, only its swap-family case (ii)):
     for every N there is a NONTRIVIAL core strongly invertible knot (K' # rho K', swap) with M_1 = ... = M_N = 0, i.e.
     J = 1 mod (t+1)^{N+1}. So: no argument using finitely many moments, and no bound "k_0 <= absolute constant", can prove Lemma Q;
     any mechanism must use global information about the Laurent polynomial (span / extreme coefficients versus complexity).

4.3 Equivariant C_k language (statements; PROVED modulo F2 except where marked).
  An ARC CLASPER is a tree clasper (Habiro) in the complement of the quotient theta-curve Theta, all of whose leaves are small
  meridional discs of the arc k (upstairs: a pair of claspers exchanged by h). Its leaves realise arc-arc crossing changes, i.e. the
  off-axis flips of F2. The standard argument (an order-<= k invariant w.r.t. crossing changes is invariant under C_{k+1}-moves)
  uses only that leaves sit on strands where the crossing changes are allowed, so under F2: M_k is invariant under arc C_{k+1}-moves.
  (A clasper with at least one leaf on the arc and some on the axis keeps the axis unknotted, since deleting the arc trivialises it;
  whether F2's on-axis order bound covers such mixed claspers is a GAP.)
  What a counterexample needs: a nontrivial (K,h) with all M_k = 0. Being arc C_n-equivalent to the trivial inversion gives
  (t+1)^n | J - 1 (under F2), hence span(J - 1) >= n or J = 1; so a C_n-trivial (K,h) is a counterexample iff n > span(J(K,h) - 1),
  which is impossible unless J = 1 already: FT gives no leverage beyond 4.0. The swap family shows the "race" explicitly: C_n-trivial
  K' make J - 1 divisible by (t+1)^{n} while span(J - 1) >= n grows with them, exactly as for V and JC (Stanford/Ohyama).
  Degree bounds: k_0 <= span(J - 1) <= (const) * crossing number is automatic for J != 1 and prevents nothing. A bound of k_0 in terms
  of genus alone is not available: it would fail if there are nontrivial C_n-trivial knots of bounded genus for all n (MEMORY/
  CONJECTURE: untwisted Whitehead doubles of C_m-trivial knots; not verified here).
4.4 What a counterexample (K,h) to Lemma Q must satisfy (collected). J = 1 and K nontrivial forces:
  a_2(K) = 0 (BRIEF); V(T(1/n)) = 1 and sigma(T(1/n)) = 0 for all n (1.3, 1.1); all M_k = 0, all q'_m = 0;
  and, CONDITIONAL ON CONJECTURE D (3.6):   (t - 1)(t^3 - 1)(t^5 - 1)  divides  V_K(t) - 1.
  Proof of the last: J = 1 gives V_K(t^2) = 1 mod (t^2-1)(t^3-1)(t^5-1); t -> t^2 maps primitive 10th roots onto primitive 5th roots,
  primitive 6th roots onto primitive cube roots, and is a local diffeomorphism at t = 1 (so the zero of order 3 at t = 1 survives).
  Every knot has (t-1)(t^3-1) | V_K - 1 (Jones); a_2 = 0 adds a factor (t-1); Conjecture D adds Phi_5. So the new constraint is
  V_K(e^{2 pi i/5}) = 1 (trivial Fibonacci-root value). Through the swap family (4.2) this also says: a nontrivial K' with I(K') = 1
  would need V_{K'}(zeta_5)^2 = 1.
4.5 Leading coefficients. For swap sums J = I(K') and the extreme coefficients are those of the coloured Jones polynomial: +-1 with
  predictable degrees for adequate K' (KNOWN for adequate knots), which proves Lemma Q on that sub-class but is class-dependent.
  For general words the extreme coefficients of J need not be +-1 (integrator's EXT records), so no class-free leading-coefficient law.
## 5. Scripts and data in this folder (run with tools/venv/bin/python from this folder)
- clib.py: helpers (moments, V_K, a_2/v_3, exact Laurent division, D(a,b), V_branch(J,n) from 1.3, h-expansions).
- a1_checks.py: F1/Q(1)/Q(-1)/moment congruences on random words (400, seed 1).   a2_span.py, a3_span_proof.py: span theorem.
- b1_pretzel.py: V(P(-2,3,7)) and expansions.   b2_small.py: words for RHT, LHT, 4_1 (two inversions).
- b3_branch.py: branch sets L_n via 1.3, identification with T(3,5), T(3,7), P(-2,3,7), Mullins = Casson check.
- b4_pairs.py, b5_verify.py: two-bridge enumeration (length <= 7), same-K pairs, the 6_2 witness, Delta M_3 pattern; b4_hits.json.
- c1_constituents.py: constituent knots K_in, K_out of the quotient theta-curve.   c2_fit3.py: M_3 regression (negative).
- c3_mod5.py: mod-5 congruence and J vs V_K moment congruences.   c4_lambda2.py: Lin-Wang conversion and exact c_2 identity (36 cases).
- d1_swap.py: swap sums (V_K = V_K'^2, no t -> -t symmetry).   d2_core_tower.py: first nonzero moments, signs.
- d3_trefoil_c2.py: J of the trefoil swap sum = N=3 coloured Jones.   d4_Rmatrix.py: integral R-matrix at q = i (Jordan block).
- d5_swap_ft.py: F2 on swap words.
- c5_doubling.py (D_k gcds), c6_factor.py (cyclotomic factorisation of J(-t) - V_K(t^2)), c7_phi5.py (stress test: 2br / random),
  c8_iota.py (iota = g(1) - 3 v_3), c9_swap_doubling.py (swap family, Phi_7 absent), c10_2br_mechanism.py (4-plat TL model, numeric
  projective characters), c11_exact_char.py (exact character identity mod A^10 = -s, irreducibility).
