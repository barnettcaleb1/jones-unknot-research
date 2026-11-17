# REFEREE NOTES: MOMENT-CYC10, LENS B (theta reduction, projector, framing, normalisation)
Referee: Claude (adversarial, quantum topology), 16 Nov 2026.
Theorem under review (Codex/Astra): preferred J_(K,h)(t) = V_K(t^2) mod Phi_10(t); consequences M_3/36 = 7 v_3 mod 5, iota integral.
Source read completely: Codex work/theory_restart/degree3_cyclotomic_comparison.md; also degree3_weight_comparison.md,
degree3_geometric_identity.md, the 3 internal audits (annular_closure, cyclotomic_referee, coefficient_framing), certificates
degree3_cyclotomic.py/.json and degree3_brauer_mod5.py/.json (read, not rerun: my own code below replaces them).
Own scripts: ~/jones-lanes/theory-restart/mont/ft/referee/cyc10ref/ (independent code; shared tools only imported, run with -B).
Marks: PROVED / CHECKED(n) / GAP / FALSE. Severity: FATAL / SERIOUS / MINOR.

STATUS: COMPLETE.

## 0. Verdict
LENS B STANDS. Items (1)-(5) re-derived step by step; no fatal or serious gap. The decisive new evidence is a RAW test:
the un-normalised quotient theta value F_raw and the framed-lift cover value G_raw (with exactly the claimed local operator
T_fold = theta_U^-1 B) agree modulo Phi_5 with NO sign or unit adjustment on 600/600 random theta graphs, and the test is
sensitive (wrong framing rules fail). Six MINOR wording repairs (M1-M6 below), none affecting the conclusion.
Conventions in which the theorem is true (and in which the proof's parameters are stated): J = lp.J, which reads the
quotient bracket with t = A^(+4); V_K from kauffman.bracket with t = A_c^(-4); both brackets use the same crossing rule
x = A*vertical + A^-1*cupcap. (The task text's "t = A^-4 conventions of lp.py" is right for V_K, not for J; see M3.)

## 1. Item (1): vertex elimination, P_1 vs P_0 as a relative identity  -- PROVED, CHECKED
1.1 Quotient. B = regular nbhd of the tree e_1 u {v_1,v_2} u stubs (a ball). Inside = Y = i_KL p_KL with
    p_KL i_KL = (theta(1,1,2)/Delta_1) Id, theta(1,1,2) = Delta_2 = <Theta_0>. P_1 := (Delta_1/Delta_2) Y is the idempotent onto
    V_1 in V_1 (x) V_2. The relative skein module of (B; colours 1,2,1,2) is End(V_1 (x) V_2), 2-dimensional generically,
    and <Theta> = Tr_q(A o Y) is a LINEAR functional of the inside for the fixed outside A. Hence (7) may be substituted for
    an ARBITRARY outside (1,2)-tangle A. PROVED.
    Explicit TL_3 check (identities.py, f_2 on strands 2,3, crossing rule of kauffman.py): T = X12 X23 X23 X12 (the quotient_word
    image of x0) commutes with f_2, T i = A^-8 i, T = A^4 on V_3, P_1 idempotent, p i = (Delta_2/Delta_1) Id, and
    P_1 = (T + Q^-1)/(Q^2 + Q^-1) with Q = -A^-4. CHECKED (exact sympy).
1.2 Normalisation. Tr_q(A P_1)/Delta_1 = pAi = <Theta>/<Theta_0>. With bracket_vector's picture (axis = straight strand at
    position 0, band = doubled half-strands) the f_2 closure of REPORT 0.2 is planar (b2 closes via b1 and the v_bot cup, b3 via
    T and infinity, nested), so F_raw = y exactly (no mu_2^f factor).
1.3 Cover. Coordinates (w,s) -> (w^2,s) on D^2 x [0,1], branch line w = 0: the k-stub {(lambda p, 1-eps+lambda eps)} lifts to
    an arc through the branch point joining (+-sqrt p, 1) (cap), likewise at the bottom (cup): lift(Y) = E. lift(I) = I
    (radial = blackboard for the strands at +-sqrt p). lift(T) = one crossing. All three in ONE marking (the lift of the
    quotient marking). (8) is the Kauffman relation E = A_c B - A_c^2 I rewritten with A_c^2 = Q, so it holds for any outside.
    PROVED; CHECKED (identities.py: P_0 = (T_fold+Q^-1)/(Q^-3+Q^-1), eigenvalues Q^-3 singlet, -Q^-1 triplet).
1.4 Coefficients/denominators. At Q^5 = 1, Q^2 = Q^-3, so (7),(8) have identical coefficients. Q^2+Q^-1 = Q^-1(Q^3+1),
    Q^-3+Q^-1 = Q^-3(Q^2+1): resultants with Phi_5 are +-1 (cyclotomic units), value 2 at Q = 1. Moreover at Q = zeta_5
    (t a primitive 10th root) [n] = 0 iff 10 | n, so delta, Delta_1, Delta_2, Delta_3 are all nonzero: the generic identities
    specialise with no regularity issue at all (the t = -1 singularities never enter the Gauss-lemma route). PROVED.
1.5 Both resolved closures contain the ORIGINAL unknotted axis (the colour-1 strand of T and of I is a straight arc in B),
    so C_T, C_I are closed annular colour-2 diagrams in V = S^3 - N(axis). F_raw = (E_-(C_T)+Q^-1 E_-(C_I))/(Q^2+Q^-1),
    G_raw = (E_+(C_T)+Q^-1 E_+(C_I))/(Q^-3+Q^-1), identities of rational functions; at zeta: F_raw = G_raw given
    E_- = E_+ at zeta on annular diagrams (Sections 1-4) and item (2).
1.6 Spot checks of the Sections 1-4 inputs that lens B relies on (not a full lens-A referee):
    quotient type-x colour-2 crossing (2-cable + f_2): B - B^-1 = (Q-Q^-1)(I-E), contraction eigenvalue Q^2 (r_- = Q^-2),
    E^2 = Delta_2 E, d_- = Delta_2 = 1-Q-Q^-1, with Q = -A^-4. Cover paired type-x crossing at A_c^2 = Q: same z,
    contraction eigenvalue Q^-3 (r_+ = Q^3), d_+ = (Q+Q^-1)^2. CHECKED (exact). The z's agree ONLY with Q = -A^-4 (lp's J
    convention); this is what makes the type-preserving geometric lift compatible with V_K(t^2).
    Generators: E_-(A_n) = reduced bracket of braid axis u closure of type-x sigma_1...sigma_(n-1) equals r_-^(n-1) L_n^-
    for n = 1,2,3 (annular_gen_check.py, numeric, errors ~1e-12); the type-y closure matches the MIRROR formula and not the
    claimed one (test distinguishes chirality). n = 2 also by hand: Q^2 - Q^-3 - Q^-5 both ways. CHECKED.
    Framed generator values agree mod Phi_5 for n = 1..8 and the cover framing identity theta_U^(n-2) Tr(B^n) =
    Q^(3(n-1)) Tr(T_fold^n) for n = 1..6 (u = Q^(1/2) avoids fractional powers). CHECKED.

## 2. Item (2): local framing factor theta_U^-1, T vs T_fold  -- PROVED (with M4), CHECKED
2.1 The framed lift of the 2-strand tangle T, with the boundary bands fixed (they lift to the blackboard bands, as for I),
    is B with some twist on each strand. Direct coordinates (small pitch): quotient blackboard band angle 0, lifted band at
    w~ = +-sqrt(p) e^(i pi s) has angle -pi s, cover blackboard 0: each strand carries a HALF twist (-1/2), total -1.
    Since theta_U is a scalar on the simple U, the operator is theta_U^(-1/2-1/2) B = theta_U^-1 B. The doc's wording
    "the only possible discrepancy is a curl power" is right for the operator but each strand individually has a half
    twist (M5, cosmetic).
2.2 Closure argument re-derived: lift of the trivial outside = standard trace closure (identity -> two 0-framed unknots,
    d_c^2, CHECKED). Closure of T = colour-2 meridian, blackboard framing 0 (no self-crossings); framings of a curve in V
    are classified by lk in S^3, so it is isotopic to the concentric (radial) 0-framing, whose lift is concentric: the lift
    is the 0-framed unknot, d_c. Trace closure of B = theta_U d_c (CHECKED). So k = -1. PROVED.
2.3 Chirality (lift(T) = theta_U^-1 B, not theta_U B^-1): the doc only cites "the fixed halfword marking". It is in fact
    forced: the quotient map (x,y,z) -> (x^2-z^2, y, 2xz) preserves off-axis crossing types (orientation-preserving on the
    right half-plane, heights keep sign), so lift(type-x A_n) = closure of type-x (sigma_1...sigma_(n-1))^2; with 1.6,
    C_(T^n) = A_n^(0), hence Tr(lift(T)^n) = Tr(T_fold^n) for all n, which pins lift(T) = theta_U^-1 B (B^-1 would give
    Q^(3n) + [3](-Q)^n). With B^-1 the projector coefficients would be (Q^3,-Q) vs (Q^2,-Q^-1) and never agree: the
    chirality is load-bearing, so the one-line justification should be written into Section 4 (M4, MINOR).
2.4 RAW TEST (cyc10ref/raw_congruence.py, raw_controls.py): G_raw = theta_U^(n_y0-n_x0) kauffman.bracket(w) at A_c^2 = Q
    against F_raw = y at A^4 = -Q^-1: equal mod Phi_5 in 600/600, no adjustment. Controls on 300 words with n_x0 != n_y0:
    no correction -> 195 odd-exponent + 105 fail; reversed theta_U^(n_x0-n_y0) -> 294 fail (6 pass, exactly 5 | n_x0-n_y0);
    doubled -> fail. CHECKED(600).

## 3. Item (3): integrality / integer ribbon exponents  -- PROVED, CHECKED
3.1 F_raw in Q(Q): E_-(C) in Z[Q^+-1] for every framed annular C (descending reduction with coefficients in Z[z,r^+-1,d],
    generators r_-^(n-1)L_n^- in Z[Q^+-1]) PROVIDED the axis is 0-framed; a kink on the axis would bring theta_1 = -A^3, not in
    Q(A^4) (M2: state the 0-framed straight axis; harmless since the axis framing does not affect the lift). Since also
    F_raw = +-A^m J(A^4) in Z[A^+-1] and A has degree 4 over Q(A^4), 4 | m: F_raw = eps Q^a J(-Q^-1), a in Z, eps = +-1.
    CHECKED: y exponents = 0 mod 4 in 600/600.
3.2 G_raw = +-theta_U^f V_K(Q^-2) with theta_U = -Q^(3/2); G_raw in Q(Q) (E_+(C) in Z[Q^+-1]) forces f even:
    G_raw = eta Q^b V_K(Q^-2). CHECKED 600/600. Independent of the square root: A_c -> -A_c multiplies by
    (-1)^(c(D) + n_y0 - n_x0) = (-1)^(2 n_y0) = 1 (c(D) = n_x0 + n_y0 mod 2). PROVED.
3.3 The doc's alternative "ratio is a ribbon monomial in a root of Q, rational only for integer exponent" is the same
    argument; fine.

## 4. Item (4): preferred-unit argument  -- PROVED (with M1, M6), CHECKED
4.1 F, G in Z[Q^+-1]; F(zeta) = G(zeta) at the 4 primitive roots; Phi_5 monic => F - G = Phi_5 R, R in Z[Q^+-1].
    F(1) = eps J(-1) = eps, G(1) = eta V_K(1) = eta, both +-1; F(1)-G(1) = 5R(1) in {0,+-2} => eps = eta, R(1) = 0.
    F'(1)-G'(1) = Phi_5'(1)R(1) + 5R'(1) = 5R'(1); F'(1) = eps a (J'(-1) = 0, d/dQ J(-Q^-1) = Q^-2 J'), G'(1) = eta b
    (V'(1) = 0). So a = b mod 5, J(-zeta^-1) = V_K(zeta^-2); t = -zeta^-1 runs over the primitive 10th roots and t^2 = Q^-2;
    Gauss again: Phi_10 | J(t) - V_K(t^2) in Z[t^+-1]. PROVED.
4.2 M1 (MINOR): "F(1) = 1 by the FT root evaluation" cross-references the FT integral model, which uses another gauge
    (q = i e^(h/2), lattice units); as written it is not justified, and it is not needed (only F(1),G(1) in {+-1} and 5 not | 2).
    M6 (MINOR): normalisation (9) Q^(-F'(1)) F is correct only when F(1) = 1; write Q^(-F'(1)/F(1)) F/F(1).
    Numerically F_raw(1) = G_raw(1) = 1 and a = b mod 5 in 300/300 (raw_controls.py), so (9) is right as used.

## 5. Item (5): cubic consequence mod 5  -- PROVED, CHECKED
5.1 Phi_10(t) = Phi_5(-t) = (t+1)^4 mod 5; Phi_10(-e^h) = Phi_5(e^h) = (e^h-1)^4 + 5 e^h(e^(2h)-e^h+1). Hence for
    S in Z[t^+-1], [h^k] Phi_10(-e^h) S(-e^h) = 5 sum_j s_j (-1)^j ((j+3)^k-(j+2)^k+(j+1)^k)/k! in 5 Z_(5) for k <= 3
    (denominators 1,1,2,6). So [h^k] J(-e^h) = [h^k] V_K(e^(2h)) mod 5 Z_(5), k = 0..3. (Interpretation of "mod (5,h^4)".)
5.2 sympy: [h^3] V(e^(2h)) = -48 v_3 + (4/3) V'(1), [h^2] = -12 a_2 + 2 V'(1); with V'(1) = 0: -48 v_3, -12 a_2. [h^3] J(-e^h)
    = M_3/6. So M_3/6 = -48 v_3, M_3/36 = -8 v_3 = 7 v_3 mod 5 (6 a unit). With 36 | M_3 (MOMENT-3) and v_3 in Z: iota in Z.
    PROVED. CHECKED: 200 random words (cubic_check.py): iota integral 200/200, jets k <= 3 agree mod 5 200/200; iota takes
    many values (0 in 93/200).

## 6. Issues (severity, repair)
 M1 MINOR  F(1) = 1 "by the FT root evaluation" unjustified cross-normalisation; drop it (sign argument needs only +-1).
 M2 MINOR  Q(Q)-rationality of F needs the colour-1 axis 0-framed (straight); say so.
 M3 MINOR  Conventions: lp.J reads the quotient bracket with t = A^(+4) (J_raw: A^e -> t^(e/4)) while V_K uses t = A_c^(-4),
           same crossing rule in both. The proof's parameters (Q = -t^-1, quotient eigenvalues Q^2,Q,-Q^-1) are exactly lp's
           convention (checked), so the theorem is J_lp(t) = V_K(t^2); in one uniform t = A^-4 convention it reads
           J(t) = V_K(t^-2) = V_(K*)(t^2). State the convention in the theorem.
 M4 MINOR  The chirality lift(T) = theta_U^-1 B (not theta_U B^-1) is load-bearing but only asserted ("fixed halfword
           marking"); add the type-preservation + Tr(lift(T)^n) = Tr(T_fold^n) argument of 2.3.
 M5 MINOR  Each lifted strand carries a half twist; only the total (an integer) enters the operator. Wording only.
 M6 MINOR  (9) should be Q^(-F'(1)/F(1)) F/F(1) unless F(1) = 1 is proved.
 No FATAL or SERIOUS issue in lens B.

## 7. Independent computations (scripts in cyc10ref/, all run with tools/venv/bin/python -B)
7.1 raw_congruence.py (seeds 1, 7; 300+300 words from flat_search.gen): F_raw := y read in Q = -A^-4; G_raw :=
    theta_U^(n_y0-n_x0) kauffman.bracket at A_c^2 = Q. y exponents = 0 mod 4: 600/600; G_raw exponents even: 600/600;
    F_raw = G_raw mod Phi_5 exactly: 600/600.
7.2 raw_controls.py (seed 7, 300 words with n_x0 != n_y0): claimed rule 300/300 pass; none 195 odd + 105 fail; reversed
    294 fail / 6 pass (5 | n_x0-n_y0); doubled fails. F_raw(1) = 1, G_raw(1) = 1, a = b mod 5: 300/300.
7.3 identities.py: 51 exact sympy checks (TL_3 projector identity (7) with f_2, vertex normalisation, T eigenvalues,
    quotient and cover Dubrovnik relations and parameters, closures d_c^2 / theta_U d_c / d_c, (8), (1), unit resultants,
    framed generator congruence n <= 8, cover framing identity n <= 6, cubic coefficients, Phi_10 = (t+1)^4 mod 5,
    jet denominators). ALL PASS.
7.4 annular_gen_check.py: E_-(A_n) = r_-^(n-1) L_n^- for n = 1,2,3 at two random complex A (type x); type-y closure matches
    the mirror formula only.
7.5 cubic_check.py (seed 11, 200 words): iota integral 200/200; cubic jet congruence mod 5 200/200.
7.6 cert_copy/degree3_cyclotomic.py (copy of the Codex certificate, with degree3_eta_gate.json): ALL 30 CHECKS PASSED.
    It checks only fixed algebra + 5 named calibrations; the universal content is carried by 7.1-7.4 and the proof.
