# REFEREE REPORT on the PROOF lane (mont/proof/REPORT.md, Theorem N skein proof)
Referee: Claude (adversarial referee, 16 Nov 2026). Notes written continuously.
Marks: PROVED / CHECKED(n) / CONJECTURE / GAP / NOT ESTABLISHED (= asserted, not proved).
Scripts: referee/pf_*.py (mine; other files in referee/ belong to other referees, untouched).

## Status: FINAL. Verdict: STANDS WITH (MINOR) REPAIRS. Theorem N (special region C_m) and sections 1-5 are correct; no mathematical error found. Issues are labelling/bookkeeping (section 3).

## 0. Plan
 R1  End(V1 x V2) = C P1 + C P3; identification v: End -> H; h_1, h_3 coordinates; b = v1 + (1-t^3) v2.
 R2  Star product.
 R3  Trace pairing; special-region functional e_1^T X^mu (slide through infinity, R-rotation, sign dictionary).
 R4  Half-diagram realisation (Lemma 3.1 / Prop 3.2), well-definedness of body vectors (Prop 3.3).
 R5  Folding lemma / twist rows / nested bodies.
 R6  Units, framing, integrality (Prop 4.2), two-closure recipe (Prop 3.9).
 R7  Corollaries 5.1-5.4.

## 1. Findings (filled in as I go)

### 1.1 Algebra of sections 1-2 recomputed (pf_alg.py, sympy, exact)  -- ALL OK
 CHECKED: rho(Y) h1 = h1, rho(Y) h3 = t^-3 h3, h1 + h3 = e1, e1^T h3 = 0, e1^T rho(Y) = e1^T;
   v = a h1 + b h3 <=> a = v1, b = v1 + (1-t^3) v2; a, b multiplicative under *, e1 the unit;
   rho(Y) diagonal (a,b) -> (a, t^-3 b) and rho(Y) v = (rho(Y)e1) * v (Y is a box operator); rho(X) is NOT (X v != (X e1)*v);
   e1^T X^mu = (1, (1-t)(1+t^2)(1-(-t)^mu)) for mu = -6..6; e1^T X^mu h1 = w1/Phi3, e1^T X^mu h3 = w3/Phi3 (mu = -6..6);
   Cor 5.1 P/Q forms; twist-row closed forms a_r, b_r (j <= 6), second coordinate (-t)^j t^-3; mirror rows = t -> 1/t.
 Verdict: the linear algebra of Lemma 1.4(iv), Thm 1.5, Thm 2.3 closed form, Prop 3.7 closed forms, Cor 5.1 is CORRECT.
 Note: Lemma 1.4(iv) is forced: h3 must be the t^-3-eigenvector of rho(Y) (it is (0,1)) and h1 the 1-eigenvector with
 e1^T h1 = 1 (since e1^T h3 = 0 and h1 + h3 = e1). So the (a,b) dictionary is determined by TH-2BR's rho(Y) and phi = e1^T
 alone; the skein input needed is only (i) Y^ acts on the channels by scalars, (ii) phi kills the P3 channel. Both fine.

### 1.2 Word-level checks on an INDEPENDENT body generator (pf_common.random_body; pf_words.py seed 4242, 27 bodies)
 My generator draws arbitrary letter sequences (x_i/y_i, x0/y0, l_i/r_i, u_i at up to 5 positions) subject only to the
 body rules, so it is not tied to flat_search.gen's shape. Results (exact lp.py), all with 0 failures:
   T3  r2-recipe vector integral 27/27; l1-recipe (TH-2BR side: closures l1.B.u2, l1.B.x1.u2) integral 27/27;
   T3c r2-vector = l1-vector up to a common unit 27/27 (Cor 3.4 at the level of VECTORS, not only J's);
   T3d v1 = J(s.B) up to unit 27/27;  T1 Cor 3.4, m = -4..4: 243/243;  T4 Thm 4.1 single box m = -4..4: 243/243;
   T5 Prop 3.9 EXACT raw factorisation alpha_m(B) = alpha_m(empty) e1^T X^-m v_recipe(B), m = -4..4: 243/243
       (alpha_m(empty) = t^(2m) exactly);
   T2 box order irrelevant 60/60; T4 necklaces of 2-3 boxes 60/60; T7 R-invariance 84/84; T6 folding m = +-1, +-3 336/336;
   T8 multiplicativity J(s.B1.B2) = J(s.B1)J(s.B2) 30/30; s.r2.B.u1 vs s.B 27/27.
 Verdict: no counterexample to any PROVED statement of sections 1-3, 5.2 on bodies outside the builder's test family.

### 1.3 The infinity-closure monomial (pf_u.py)
 lp.J_raw divides the Q_0-coefficient y by the monomial u = y + delta x. CHECKED (45 words: 9 bodies x m = -2..2): u = 1
 identically. Reason (referee, PROVED modulo the kht++ doubling of 0.3): u is the bracket of an unknot diagram, so
 u = (-A^3)^(-writhe); in the doubled picture every band-band crossing is 4 crossings of two antiparallel pairs (signs
 cancel in pairs) and every y0/x0 is the axis passing over/under both band strands and back (two pairs of opposite
 sign), so the writhe is 0. Hence alpha_m(B) = y exactly; this is the missing step of Prop 3.9 (see issue list).

### 1.4 Large twists and GENERAL nesting (pf_nest.py)
 CHECKED: single box with |m| = 5..8: 48/48. A necklace used as a body, NB = r2.(y1)^m.B1(.B2).u1:
 recipe vector of NB = X^-m (v(B1)*v(B2)) up to unit 40/40; NB inside an outer necklace with another body and outer twist
 m' in [-3,3]: J = norm(e1^T X^-m' (X^-m(v1*v2) * v3)) 40/40. So Lemma 3.6 holds for composite B as stated (it is proved for
 any body B, and a product of bodies is a body), giving an arborescent (not only Montesinos) calculus. No failure.

### 1.5 Raw-level exactness of the "regular isotopy" claims (pf_raw.py; 12 new bodies)  -- ALL EXACT
 CHECKED at the level of RAW brackets (no normalisation at all): Lemma 3.6 folding 192/192; Lemma 1.2 R-invariance 48/48;
 Prop 3.7 row recursion 24/24; Cor 5.2(a) hairpin 12/12; and J_raw(s.r2.(y1)^m.N.u1) = J_raw(s.l1.N.(y1)^m.u2) EXACTLY
 (ratio 1) for m = -3..3, 84/84. This confirms (U5): the slide through infinity + pi-rotation of Prop 2.2, the cap slides,
 the folding and the zigzags change nothing, not even by a unit.

### 1.6 Inputs and classical limit (pf_th2br.py, pf_classical.py)
 CHECKED: TH-2BR-A matrices against lp, J(s.l1.W.u2) = norm(e1^T rho(W) e1), W random of length <= 9 in y0,x0,x1,y1: 150/150.
 CHECKED: Cor 5.4 on new bodies (raw-recipe vectors), J(s.l1.B.W.u2) = norm(e1^T rho(W) v(B)): 60/60.
 CHECKED: consequence of Prop 4.2(e): J(s.B)(1) = +-1 and J_mu(1) = +-1 (mu = 2,-1,-3) on 25 new bodies: 25/25.

## 2. Step-by-step audit of REPORT.md (my mark after each item)

0.1-0.2  J =. <Theta;1,1,2>/<Theta_0;1,1,2> (input TH-2BR 2.2). ACCEPTED AS INPUT. Wording issue I3.
0.3      Quotient picture (input TH-2BR 1.3(b), see I5). Crossing-type rules VERIFIED by hand: a 90-degree rotation swaps x/y;
         a planar pi-rotation keeps them; R = (x,y,z) -> (x,-y,-z) = reflection in a horizontal line followed by switching every
         crossing, and both operations swap x/y, so R keeps types. Consequence used silently in Lemma 1.2: R acts on tangle
         skeins as the A-LINEAR anti-involution "flip" (reflect crossingless diagrams, crossings go to crossings of the same
         type), with no A -> 1/A. Correct.
Lemma 0.1  PROVED. Checked the picture after the slide: c reaches the axis BELOW the point where leg 1 meets it, so no new
         crossing; the outside is fuse(axis, leg1) then fuse(leg2) = phi.
Lemma 1.1  PROVED (standard fusion/bubble/Schur).
Lemma 1.2  PROVED (P_c is flip-invariant; R linear by 0.3). The alternative proof in the parenthesis (closure graph of a(B)
         is R-symmetric) is cleaner. CHECKED raw-exact 48/48.
Lemma 1.3  PROVED (partial transpose; inverse = zigzag with an added strand).
Lemma 1.4  PROVED. Remark: (iv) is forced by TH-2BR alone: h3 is the t^-3-eigenvector of rho(Y) (= (0,1) up to scale) and h1
         the 1-eigenvector with e1^T h1 = 1. The only skein inputs are: Y^ acts on each channel by a scalar (true also for the
         kht++ y0, which differs from the honest ribbon twist by a band-framing unit) and phi factors through fuse_1.
Thm 1.5  PROVED; algebra CHECKED (pf_alg.py).
1.6      PROVED (given D_W, D_E as part of the box data, the only freedom is relative full twists; Y is diagonal).
Prop 2.1 PROVED.
Prop 2.2 PROVED. Verified the geometry the proof asserts: (i) x = 3 is the outermost strand at every height (bodies push the
         r2 strands outwards, the twist crossings involve x = 1, 2 only), and the face to the right of A_out (both rays) is the
         outer face, so dragging x = 3 along A_out through infinity is a planar isotopy of S^2 with no new crossings and no
         winding of the arc around the axis (a winding next to the cup would have inserted a NON-unit Y^ into the box slot;
         it does not occur); (ii) bottom-up, leg 1 fuses first (v_top below v_bot'), which is phi; (iii) R keeps crossing
         types and left/right. Bookkeeping issue I2. Simplification I9. CHECKED raw-exact: J_raw(s.r2.(y1)^m.N.u1) =
         J_raw(s.l1.N.(y1)^m.u2), ratio exactly 1, m = -3..3, 84/84.
Sign dictionary  PROVED (y1 is the inverse braid generator of x1 <-> X^). CHECKED (all T1/T4 tests with m of both signs).
Thm 2.3  PROVED; closed form CHECKED (mu = -6..6). Remark (2) VERIFIED: the closure graph with box fused to c and twist site
         fused to d is a prism (6 vertices, 9 edges); the triangle (v_top, v_bot, F_up) has outer edges (1, d, 1), so d in {0,2}.
Lemma 3.1  PROVED. ("Closes no component" is automatic for a knot.) The identification of the state of Q_B = B~/h with the
         local quotient picture of B uses that the kht++ quotient is built letter by letter (I5).
Prop 3.2, Prop 3.3  PROVED (well-definedness is purely local). The word rule for R(B) (reverse, caps <-> cups, crossings
         unchanged) VERIFIED: the upstairs rotation about a horizontal line commutes with h (perpendicular pi-rotations commute)
         and keeps crossing types.
Cor 3.4  PROVED; CHECKED 243/243 normalised and raw-exact (above).
Lemma 3.5  PROVED (it is a planar isotopy, not an R2: the crossing slides along the cap through its maximum; I6). Index
         bookkeeping of both the cap and the cup versions VERIFIED by hand.
Lemma 3.6  PROVED. Each sub-step VERIFIED: (a) r2.x1 ~ r1.y2 (3.5, k=1), l1.r1 = r1.l3, l3.y2 ~ l2.x3 (3.5, k=2), and r1.l2.x3
         is the unlabelled diagram l1.r2.x3; (b) x3 slides down past B and u1 (disjoint strands); (c) zigzag. The proof needs the
         crossings moved off the left legs BEFORE B is applied (for odd m, B would otherwise act on L); the proof does this.
         CHECKED raw-exact 192/192; normalised 336/336; also for COMPOSITE B (necklaces used as bodies) 40/40 + 40/40.
Prop 3.7  PROVED (index shift r1.y_i = y_(i-2).r1 VERIFIED; after r2.x1 the positions are [L, s, R]). CHECKED raw-exact 24/24.
Cor 3.8  PROVED (Y^ commutes with [Q_B] in the commutative box algebra).
Prop 3.9  STATEMENT CHECKED (exact raw factorisation 243/243, mine; 50/50 builder). PROOF NOT ESTABLISHED as written (I1).
4.1      (U1)-(U5): substance correct; wording issues I3, I4.
Thm 4.1  PROVED (the ratio of two nonzero elements of Z[A^+-4] that is +-A^j forces 4 | j, so norm recovers J exactly).
Prop 4.2  PROVED. VERIFIED (a) the sandwich by 1 (x) f2 kills e2, e1e2, e2e1; (b) U factors through one strand, Tr_q U =
         Delta_2, U = (Delta_2/Delta_1) P1; (c) parity classes (closed-diagram fact; 1 and e1 differ by one saddle); (d) a(B) is
         exactly <Theta(s.r2.B.u1)>/<Theta_0> (gamma_1(C_0) = <C_0, id> = <Theta_0>, gamma_3(C_0) = 0), gcd(delta, delta^2-1) = 1,
         delta^2 - 1 = t^-1 Phi3; (e) at A = 1, s^2 = 1 and s = s^-1, crossing changes + isotopy reach the trivial box
         (descending diagram), kinks give +-1, so c_e(1) = 0; (f) (1 - t) | u c_e'. CHECKED integrality 27/27 (new bodies) and
         the consequence J(1) = +-1 (25/25).
Cor 5.1  PROVED (the stated bound makes the supports of P and Q(-t)^mu disjoint; then J_mu has >= 2 terms).
Cor 5.2  PROVED; CHECKED 30/30 and raw-exact hairpin 12/12.
Cor 5.3  (a)(b) PROVED for R_x-symmetric drawings (flip symmetry recalled, not proved: I8); (c) PROVED for the half-diagram
         family; (d) CHECKED (correctly labelled); (e) CONJECTURE (correctly labelled).
Cor 5.4  PROVED; CHECKED 60/60 on new bodies (builder 120/120).
Section 7 labels: consistent with the text, except Prop 3.9 (should read CHECKED, proof sketched) and the input list,
         which omits TH-2BR 1.3(b) (the quotient picture) although 0.3, Lemma 3.1 and Prop 3.2 use it.

## 3. Issues (claim / problem / severity / fix)

I1  [minor; mislabelled PROVED] Prop 3.9: "alpha_m(B) = U_m c(B) e1^T X^-m v(B), U_m depending only on m, c(B) only on B".
    Problem: the factorisation of lp.J_raw's normalisation is asserted with a one-line reason ("the blackboard framing of the
    body and its contribution to the monomial of the infinity closure, the same for all m"); nothing shows that the monomial
    splits into an m-part times a B-part. NOT ESTABLISHED as written. The statement itself is true in all tests: exact raw
    identity alpha_m(B) = alpha_m(empty) e1^T X^-m v_recipe(B), m = -4..4, 243/243 (referee) + 50/50 (builder).
    Fix: (i) u = y + delta x is identically 1 (CHECKED 45/45; reason: the infinity closure is an unknot diagram whose writhe is 0,
    because band-band crossings are quadruples of two antiparallel pairs and each y0/x0 is the axis crossing both band strands
    and back, signs cancelling in pairs), so alpha_m = y; (ii) then Prop 2.2 (raw form: J_raw(s.r2.(y1)^m.N.u1) =
    J_raw(s.l1.N.(y1)^m.u2) exactly, CHECKED 84/84) and TH-2BR 2.2 give the factorisation, provided the band framing f in
    TH-2BR 2.2 is additive over slabs (plausible, not verified by me beyond the 293 exact cases). Or relabel Prop 3.9 CHECKED. Peripheral:
    Theorem N and Thm 4.1 do not use it.

I2  [minor; bookkeeping] Prop 2.2 / 0.4: "<C_m,N> = u_m phi(X^^-m (N x id)E_1) = u_m' e1^T rho(X)^mu v(N) with UNITS u_m, u_m'".
    Problem: with phi the actual closing functional, phi(E_1) and the closure through infinity carry the non-unit factor
    <Theta_0> (= Delta_1 * phi(E_1)); so u_m' = u_m lambda_X^-m is not a unit unless phi is normalised (phi(E_1) = 1), which
    0.4 does only implicitly. Harmless: the factor is independent of m and N and is divided out by J = <Theta>/<Theta_0>.
    Fix: state <C_m,N> = <Theta_0> eps_m e1^T X^-m v(N) with eps_m a unit (eps_m = t^(2m) in lp's raw normalisation).

I3  [minor; wording] (U1)/0.2: "J is DEFINED as the unique signed power of t times <Theta>/<Theta_0>". Axis kinks contribute
    -A^(+-3), which is not a power of t; it should read "signed power of A" (as in 0.1's definition of UNIT). Thm 4.1 is
    unaffected (its argument of norm lies in Lambda, and a ratio +-A^j between nonzero elements of Z[A^+-4] has 4 | j).

I4  [minor; wording] (U5): "(Kinks occur only in the TH-2BR facts 'X at the band cap' / 'Y at phi', which are not used here.)"
    They ARE used: they are exactly the normalisations rho(X) = X^/lambda_X (X^E_1 = lambda_X E_1) and e1^T rho(Y) = e1^T
    (phi Y^ = theta_1 phi) that produce the units lambda_X^m, theta_1^k in Prop 2.2 and Thm 4.1. Only units; delete the clause.

I5  [minor; unlisted input] Lemma 3.1 / Prop 3.2 / 0.3 identify the state of the quotient box Q_B = B~/h with the LOCAL quotient
    picture of the letters of B (axis at x = 0, half-strand i -> colour-2 strand at x = i+1, y0 -> axis-band twist). This is
    TH-2BR 1.3(b) (kht++ Tangle::quotient is letter-local, cf. flat_search.quotient_word), but section 7's list of inputs names
    only TH-2BR-A and TH-2BR 2.2. The PROVED marks of sections 2-3 are relative to all three. Fix: add TH-2BR 1.3(b) to the list.

I6  [minor; wording] Lemma 3.5 calls the cap slide "an R2 move of the cap top against s". It is a planar isotopy (the single
    crossing slides along the cap through its maximum). Conclusion unaffected (still exact; CHECKED raw-exact via 3.6/3.7).

I7  [minor; scope, for downstream readers] Def 2.0 defines necklaces with an ARBITRARY special region, but Thm 2.3 covers only
    C_m (and Cor 5.4 the two-bridge regions C_W = e1^T rho(W)). For a general special region only Prop 2.1 holds:
    J =. gamma_1(C) A + gamma_3(C) B with gamma's NOT determined. The REPORT is careful; the BRIEF's phrase "NECKLACE CLOSURE ...
    J = e1^T X^mu (...)" and the summary's "Theorem N ... PROVED" must always be read with "special region C_m". In particular
    Montesinos knots with a general infinity-parity tangle R_0 are covered only by Cor 5.3(e) (CONJECTURE).

I8  [minor; conditional] Cor 5.3(a)(b) assume every R_i is DRAWN R_x-symmetrically ("flip symmetry", recalled, not proved) and
    5.3(d) (mont(m,rows) = pretzel) is CHECKED only; both are labelled correctly in the REPORT. Cosmetic: "P(-+2m, ...)" should
    be P(-2m, ...) as in the BRIEF (mont(1,[3,3]) = P(-2,3,3) = T(3,4)); words.py's docstring "P(2m, rows...)" is also off.
    Also: Alexander polynomials cannot see mirrors, so the CHIRALITY in 5.3(d) (P(-2m, r_i) versus P(2m, -r_i)) rests on the
    single k138 J comparison for 8_19; for the 'which inversion' question the realised inversion is the rotation about the
    axis through the even column (a pretzel can have several strong inversions; J depends on the choice).

I9  [not an error; simplification] Prop 2.2 has a one-line proof without the slide through infinity: the upstairs pi-rotation
    R~ about a horizontal line commutes with h and maps the half-diagram s.r2.(y1)^m.N.u1 LITERALLY to s.l1.R(N).(y1)^m.u2
    (word reversal: the final u0 becomes the start, the u1 cup becomes the l1 cap, the r2 cap becomes the u2 cup, crossing
    types are kept). So the two strongly invertible knots are equivariantly isotopic and J agrees; then Lemma 0.1 and Lemma 1.2.
    This also explains why the RAW brackets agree exactly (84/84).

## 4. What the REPORT establishes (referee's summary of marks)
 PROVED (relative to TH-2BR-A, TH-2BR 2.2, TH-2BR 1.3(b)): Lemmas 0.1, 1.1-1.4, Thm 1.5, Props 2.1-2.2, Thm 2.3 (THEOREM N for
   special region C_m, sign dictionary y1 <-> X^-1), Lemma 3.1, Props 3.2-3.3, Cor 3.4, Lemmas 3.5-3.6, Prop 3.7, Cor 3.8,
   Thm 4.1, Prop 4.2, Cors 5.1, 5.2, 5.3(a)(b) (for R_x-symmetric drawings), 5.3(c), 5.4.
 CHECKED only: Prop 3.9 (statement true in 293 cases; proof incomplete), Cor 5.3(d).
 CONJECTURE: Cor 5.3(e).  GAP (harmless, as the REPORT says): three normalised closures always pin a vector.
 Bonus (referee, CHECKED 40/40 + 40/40): Lemma 3.6 applied to composite bodies gives an ARBORESCENT calculus,
   v(r2.(y1)^m.B1...Bk.u1) = X^-m (v(B1)*...*v(Bk)). Any depth follows by induction (a nested necklace is again a body, and
   Lemma 3.6 is proved for every body): PROVED from the REPORT as written; CHECKED at depth 2 only (a depth-3 run was too
   expensive for lp's state-sum and was aborted, pf_deep.py).

## 5. Computations (all exact, lp.py; scripts in referee/, each < 1 min except pf_deep.py, aborted after 10 min)
 pf_alg.py (sympy identities), pf_common.py (independent random-body generator), pf_words.py (T1-T8, about 1,430 checks),
 pf_u.py (u = 1), pf_nest.py (|m| <= 8, nesting), pf_raw.py (raw exactness, 360 checks), pf_th2br.py (inputs, 210 checks),
 pf_classical.py (J(1) = +-1), pf_i9.py (word reversal R~ gives raw-equal brackets, 50/50). Total failures: 0.
