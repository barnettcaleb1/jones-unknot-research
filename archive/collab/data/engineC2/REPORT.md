# ENGINE C2 REPORT: mirror-symmetric (amphicheiral) theta-curves
Lane: ~/jones-lanes/theory-restart/mont/cx/engineC2/ (Claude, started 17 Nov 2026 ~02:05 CST). Marks: PROVED / CHECKED(n) / CONJECTURE / GAP.
STATUS: FINAL (03:05). NO HIT. Main output: Theorem M2 (mirror pairing kills contraction) + far-field closure F, F'; S1 decided for all library boxes.

## 1. Mirror rule (lp.J conventions)
 MIRROR = swap x_i <-> y_i in every letter (caps/cups unchanged): J(mirror w)(t) = J(w)(1/t) exactly (normalised J).
 CHECKED(300) random half-words (mirror_check.py). So an amphicheiral theta-curve has J(1/t) = J(t) (centred, no unit).

## 2. Which theta-curves are isotopic to their mirrors (geometry; PROVED, elementary)
 Let f be an orientation-reversing self-map of (S^3, Theta) with f(k) = k (finite order, as for hyperbolic theta-curves).
 (a) If f fixes the vertices, f|k fixes both endpoints and has finite order, so f|k = id and k lies in Fix(f): impossible
     for a point reflection; for a plane reflection k lies in the mirror plane P, P - N(k) is a disc splitting the exterior
     of k into two half-balls each holding one boundary-parallel axis arc, so the tangle is rational and K is the UNKNOT.
     So f swaps v_top, v_bot and reverses k. If f is then a PLANE reflection, P meets Theta in 3 points (one per edge):
     a vertex-sum sphere, so K = K' # K'* (composite; excluded by N3). The useful case is the POINT
     REFLECTION (2 isolated fixed points): one fixed point is the midpoint of k, the other is off Theta, and f acts on the
     axis circle A as a free rotation, so f SWAPS THE TWO AXIS EDGES A_1 <-> A_2 (A_in <-> A_out).
     (Order-4 rotoreflections whose square is a strong inversion of K descend to order 2 on the quotient: same case.)
 (b) CONSEQUENCE (PROVED for the two closed-form grammars): the standard grammars of the previous round put all boxes
     on ONE axis edge (A_in; A_out = the axis line through infinity is bare). A point reflection must move them to A_out, so
     they are symmetric only through a non-manifest isotopy, and for the closed forms this is excluded:
     standard necklace s.r2.(y1)^m.B_1..B_n.u1 has mirror s.r2.(x1)^m.B_1*..B_n*.u1 (twist mu -> -mu, boxes mirrored; the
     special-region covector e_1^T X^mu is not mirror-invariant for mu != 0: w_1(1/t) != unit*w_1(t)); vertical closure
     a -> -a likewise (a odd, so never). With mu = 0 the necklace is J = prod a(v_i): an equivariant connected sum (N3).
     So "mirror-closed necklaces" are NOT amphicheiral theta-curves; the brief's suggestion must be replaced by grammars in
     which BOTH axis edges carry boxes, exchanged by f.
     WARNING (CHECKED): K amphicheiral does NOT make (K,h) amphicheiral. Every strong inversion of the amphicheiral
     two-bridge knots 4_1, 6_3, 8_3, 8_9, 8_12 (TH-2BR words, fig8.py) has NON-palindromic J (e.g. 4_1: s.l1.y0.y0.x1.u2,
     span J 7): the mirror symmetry of K EXCHANGES its two inversions. The symmetry must be a symmetry of the theta-curve.
 (c) DIAGRAM MODEL (circle model): A = left line A_l + right line A_r closed by a top cap and a bottom cup; v_top on A_l,
     v_bot on A_r; k in between. f = rotation by pi of the plane about the centre + switch of every crossing.
     A Morse word W_top (from the top down to the middle level) and its image f(W_top) (reverse order, positions mirrored,
     cap <-> cup, split <-> merge, X <-> Y) glue to an f-INVARIANT DIAGRAM: Theta(W_top) := W_top . f(W_top) (sym.py).
     Connectivity rule (PROVED): with middle level (A_l, k_1..k_{2j+1}, A_r) the glued arc is ONE arc iff the strand from
     v_top is not the middle strand at the middle level (otherwise k = straight middle arc + a closed loop).
 (d) STRUCTURE (PROVED): cut at the middle level; the top half has state v in the skein space S of (1,2^{2j+1},1)
     (dim 4 for j = 1, 21 for j = 2) and J =. v^T G v~ with v~(t) = v(1/t) and a fixed gluing form G. Hence:
     THE TOP END OF J IS DECIDED BY THE TOP JETS AND THE BOTTOM JETS OF v TOGETHER (top(v_i v~_j) = top(v_i) - bot(v_j)).
     Point symmetry makes J palindromic (one-ended in J) but turns the unit condition into a JOINT condition on both ends
     of the half-state. This is the precise sense in which the symmetric trick converts, but does not remove, the two-ended
     obstruction.

## 3. Tools (this folder)
 theta.py   direct exact evaluator of <Theta;1,1,2> for two-colour Morse words (axis colour 1, k = doubled band + one f_2),
            J = normalise(<Theta>/<Theta_0>), t = A^4.  CALIBRATED: equals lp.J on 150/150 random half-words (calib.py).
 sym.py     f-image of Morse words, symmetric gluing, body words on (A_l, k) slots, S-necklace generator.
 gform.py / gtable.py   2-slot bilinear forms: R = (a,b) G (a~,b~)^T exactly for normalised box vectors (box units cancel
            against the mirror box units: u(A) u(1/A) = 1).  Gtab_Sneck.pkl = Ghat(m) = Phi_3^2 G(m), m even in [-12,12].
 fastS.py   fast exact J for 2-slot closures from box vectors (engineA vc/lib conventions).

## 4. Class S1: the S-NECKLACE (first symmetric grammar)
 W_top = capA, v_top on A_l, cap(M,R), (L-M twists)^m, body B on (A_l, L).  Glued: B* = f(B) sits on (R, A_r) = A_out, and
 the M-R twists (mirror) sit near v_bot.  Symmetry: f (explicit, by construction).  m must be EVEN (connectivity rule);
 m = 0 is the vertex sum J = J_B(t) J_B(1/t) (CHECKED exactly on 'r2.x1.y0.u1').
 J palindromic: CHECKED on every even case computed.
 G(m) (gtable.py, exact): Hermitian, G(m)^T(1/t) = G(m), G(-m) = G(m)^T, RANK 2 for m != 0 (not X^T G(0) X~: the closure is
   a genuinely new two-slot special region; the L-M twist has THREE channels d = 0,2,4 here, top degrees grow like t^{m-1},
   t^{-2}, t^{3m}, t^{2m-1} for G_11, G_13, G_31, G_33).  Bilinearity CHECKED(4 extra boxes per m, m = +-2,+-4).
   det Ghat(2) = -(t^2-1)^2 (t^2+1) Phi_6 Phi_3^3 / t^3.
 DEGREE IDENTITY (CHECKED all m): top(G_11) + top(G_33) = top(G_13) + top(G_31), so the four top degrees of
   R = sum G_cc' chan_c chan~_c' satisfy T1 + T4 = T2 + T3 for every box; a tie at the maximum forces
   E = +-D with D = m + delta, i.e. 3N = m + 1 + delta_b or 3N = 2m + 1 + delta_t: the integral part N is fixed by ONE end's
   degree, and the first m + delta orders of cancellation test ONLY the bottom jet of the slope q against the pole
   pi = -G_13/G_33 (t -> 0); after that the a-terms enter and the top jet couples in.
 POLE vs EIGENSLOPES: m = 2: pi = t^-3 (1 + t^4 + t^6 - t^7 + ...): agrees with the Y-shifted X-eigenslope 1 for only 4 orders;
   m = 4: pi = t^-5 (1 + t^2 - ...), m = 6: t^-7 (...): degree -(m+1) is not -3N or 1-3N for m >= 4 (unreachable by
   eigenslope contraction).  So the cheap one-ended mechanism (M4 of engineA) does not align with this closure.
 E1 SCAN (scanS.py; every N with a top tie, every even m in [-12,12]):
   R(7) 238 boxes: 1,904 candidates, 0 units, best rho = depth/half-span = 2/7 = 0.29, max depth 3 orders.
   14 general bodies: 110 candidates, 0 units, best rho 0.17.
   820 products of two R(5) boxes: 6,140 candidates, 0 units, best rho 0.21 (5 of 24 orders).
   1,499 depth-1 nested boxes F_k(Y^N u) (u in R(5) + general, |k| <= 4, |N| <= 2): 11,987 candidates, 2 "units" = the
   identity box vector (sanity: theta-curve = special region + full twist, unknot), best rho 0.29, max depth 6 of 39.
   Doubly gated (a_2 = 0 and J(zeta_10) = 1): 3 (spans 70, 70, 74).  Class S1 is SHALLOW: rho <= 0.29.
   BALANCED REGIME (n rational boxes ~ m, all four top terms tie): products of 3 boxes of R(5), m in {2,4,6,8}: 30,240
   candidates, 0 units, max depth 4, best rho 0.13; products of 4 boxes of R(5): 290,920 candidates, 0 units, max depth 4
   (naive half-spans 30-78), best rho 0.11.  engineA's 292 depth-2 positive-potential boxes, alone and times R(5): 28,140
   candidates, 0 units, max depth 3.  DEPTH DOES NOT GROW WITH COMPLEXITY: it stays <= 6 while the needed depth grows.
   NOTE: m < 0 is redundant: Theta(m,B)* = Theta(-m,B*) and Theta(m,B) is amphicheiral, so J(m,B) = J(-m,B*).
 CONTRACTION IS NEUTRALISED (CHECKED): slot box F_k(p) (nested necklace body, the engine-A contraction): span J = 2|k| + c
   for |k| >= 3, both signs, p in {XY, XXY, XYY}, m in {2,4} (neutral.py).  See mechanism M2 below.

## 5. Class S2: two-pole symmetric plats (plat2.py, enum2b.py)
 Top half = v_top, cap(M,R), then a word in s1 = L-M crossing ('a'), s2 = M-R crossing ('b' = f(s1)), tl = full twist of A_l
 with L ('c'), tr = f(tl) ('d') (capitals = inverses); Theta(W) = W . f(W).  Exact state in the 14 plain matchings of the 8
 doubled middle points, J = <s_P, mirror(s_D)>; CHECKED(14) against the direct evaluator.  Inverting every letter gives the
 mirror theta-curve, hence the same J (redundancy halved).  First letter c is a framing change (excluded), first letter b
 is a kink on the new cap (kept as sanity).
 EXHAUSTIVE to |W| <= 7 (reduced, commuting pairs normalised; first letters a, B, d; the other three are mirror copies):
   58,887 words, 1,274 distinct non-unit J, 11,481 J = 1 words.
   CERTIFICATION of every J = 1 word: constituent knot A_1 u k unknotted (constit.py) AND the SISTER invariant (edge A_1
   coloured 2, A_2 and k coloured 1; relabel.py; a unit on every trivial theta-curve) is a unit: 11,481/11,481, i.e. all
   presumed trivial theta-curves (not hits; a Brunnian theta-curve would have shown a non-unit sister).
   Doubly gated: 0.  a_2 = 0: 130 distinct J, min span 14 (W = BCABBdb).  Smallest span 8 (BDDB, a_2 = 2).
   Best tropical rho (1 - halfspan/predicted) 0.59 (DbAAbbd: half-span 6 vs predicted 14.5; a_2 = 18).

## 6. E4: generalised 2-slot symmetric closures (e4_gen.py)
 Special part = any S2 word W_s of length <= 4, slot box on (A_l, k) at the middle; 2x2 form G(W_s) fitted exactly;
 boxes R(6) + 279 nested F_k(Y^N u) (u in R(4)); every tie-N.  69 distinct forms G.  Deepest cancellation 7 of 19
 orders (abba, nested box); best rho 0.56 (abCa, 5 of 9).  65 (box, N) unit pairs: each rebuilt as an explicit diagram,
 J = 1 recomputed directly, constituent unknotted, sister invariant a unit (cert_e4.py): presumed trivial, NOT hits.

## 7. THE OBSTRUCTION (main theoretical output)
 THEOREM M2 (mirror pairing kills contraction; PROVED). Let Theta be point-symmetric, J = v^T G v~ (section 2(d)); the gluing
 is f-invariant, so G~^T = G (CHECKED exactly for every S1 form). Let a twist site with channel eigenvalues
 eps_d t^{e_d} (d in D; D = {0,2} for an X-type site / nested necklace body, {0,2,4} for an L-M site with eigenvalues
 1, -t, t^3, {1,3} for an axis twist Y) be repeated k times in the top half (so, by symmetry, its mirror k times in the bottom
 half). Write v = sum_d (eps_d t^{e_d})^k v_d (spectral decomposition). Then
     J(k) = sum_{d,d'} C_{dd'} (eps_d eps_d' t^{e_d - e_d'})^k,   C_{dd'} = v_d^T G v~_{d'},   C_{d'd}(t) = C_{dd'}(1/t).
 Proof of the last identity: C~_{dd'} = v~_d^T G~ v_{d'} = v_{d'}^T G~^T v~_d = v_{d'}^T G v~_d = C_{d'd}.  QED
 CONSEQUENCES. (i) Every contracting frequency -(e_d - e_d') at the top is paired with the expanding frequency +(e_d - e_d')
 whose coefficient is its mirror: they vanish together. Hence J(k) is either INDEPENDENT of k, or top J(k) >= c|k| - c'
 (c = max e_d - e_d' over nonzero C) for both signs of k: large twists never make the top of J converge, so the cheap
 one-ended mechanism of engine A (M4, eigenslope contraction of nested boxes) has NO analogue in a symmetric closure.
 (ii) For nested boxes in a slot, also inside products (v = F_k(p) * u): J(k) = A_0 + (-t)^k A_+ + (-t)^{-k} A_+~:
 contraction of the box at one end is exactly compensated by the expansion of its mirror image at the same end of J.
 (iii) Units only in an explicit finite window of k (Lemma-W type), as for non-symmetric closures, but now with no
 one-ended convergence to help: a unit must come from a finite-window coincidence.
 CHECKED: S1 slot box F_k(p): span J = 2|k| + c (section 4); S2 families (families.py): a^k span 6k exactly
 (k = 2..14), d a^k 6k + c, (ab)^n 12/period, (aD)^n 12/period, (aBd)^n growing; the only bounded family (aB)^n is
 identically J = 1 (certified-trivial words).
 GENERAL OPERATORS (irrational eigenvalues, e.g. pseudo-Anosov plats; CONJECTURE, partial proof): for a unit-determinant
 2x2 operator with Puiseux degrees p, d-p at infinity and q, d-q at 0, the four pair rates at the top are
 {+-(p-q), +-(p+q-d)}: again symmetric; if no rate vanishes, palindromicity forces a nonzero positive-rate coefficient
 (otherwise top J_n -> -infinity, impossible for J_n(-1) = 1), so J_n is a unit only in a finite window.

 MECHANISM M1 (PROVED, section 2(d)): the top of J reads top(v) - bot(v): point symmetry converts "both ends of J" into
 "both ends of the half-state". The two-ended problem is relocated, not removed.
 MECHANISM M3 (S1 poles; CHECKED): in the S-necklace the slot box must match one of four poles at one of its ends for
 |m + delta| orders (phase 1: the integral part N is forced by one end's degree), then a coupled phase follows
 (q~ - pi) q ~ kappa := -det G / G_33^2 with deg kappa = -(2m-1) (CHECKED m = 2,4,6) and deg det/Ghat_33 = 4.
 The limiting pole series (normalised, m >= 8) is 1 + u^2 + u^3 + ... (u = 1/t at the top, degree -(m+1) at the bottom
 of the box); the X-eigenslopes have normalised series 1 and 1 - u^2 + ...: they miss the pole at order 2, and for
 m >= 4 the degree -(m+1) is reachable only when m = 2 mod 3. So contraction cannot even start phase 1.
 Observed: depth <= 6 in every S1 run (single, products of 2-4, nested, general, depth-2 boxes), while the depth a unit
 needs is about span(a) + 2m - 1 + delta.

## 8. E5: S1 COMPLETE in (m, N) (s1window.py, s1complete.py, kfit.py)
 FREQUENCY FORM (CHECKED 24/24 entries at m = +-8, +-10, +-12): (1+t^2) Ghat(m) = sum_{f=-3..3} t^{f m} K_f (L-M eigenvalues
 1, -t, t^3).  Hence (1+t^2) Phat(m,N) = sum over 13 terms t^{f m + 3 g N} c_{f,g}(box), g = -1 (b a~), 0, +1 (a b~); the
 exponent set {(f,g)} is the CENTRALLY SYMMETRIC hexagon (3,-1),(2,0),(0,1),(-3,1),(-2,0),(0,-1) (central symmetry = the
 mirror), so top and bottom tie-rays coincide (normals +-(1,1), +-(1,2), +-(0,1)): tropical arguments alone cannot exclude
 far units; along each m-ray the top is t^{2m} E_c with a fixed edge polynomial E_c, so each ray carries at most one
 candidate, |m| <= (3 Dmax + 6)/2 (Dmax = largest |exponent| of the c_{f,g}); fixed-m rays are exact 3-term families in t^{3N}.
 ALGORITHM: for every even m with |m| <= 3 Dmax + 12 and every N (exact Lemma-W candidates of the 3-term family), test
 P == +-(1+t^2) Phi_3^2 exactly; check every edge polynomial is nonzero.
 RESULT (all boxes; max m bound 132): R(7) 238 boxes 15,205 candidates; general 14: 779; products of two R(5) 820: 55,739;
 depth-1 nested 1,499: 113,768; depth-2 positive-potential 292: 24,560.  0 UNITS except the identity-vector box
 (trivial sanity at (m,N) = (+-2,+-1)); 0 edge polynomials vanish identically.
 => REGION CLOSED (CHECKED, completeness by the ray argument): every S-necklace with slot box from these libraries,
    ANY m, ANY integral part N, has J != 1.

## 9. THEOREM F (S1 far field closed for EVERY box; PROVED modulo the CHECKED frequency fit)
 Exact frequency components (kfit.py, exactpoles.py): K_3^{31} = (1+t^2) Phi_5,  K_2^{33} = -t Phi_5,  K_0^{13} = -t^2 (1+t^2).
 Along the m-rays of the hexagon (edges (3,-1)-(2,0) and (2,0)-(0,1), and their central mirrors) the top of P is
 t^{2m} E_c with E_c a FIXED polynomial; a unit far out on a ray needs E_c == 0 identically, i.e. the box slope q = b/a
 (or its mirror) equals EXACTLY
      q~ = t^c (1+t^2)/t = -t^c / eps      (eps = -t/(1+t^2) the X-eigenslope: the pole is its reciprocal), or
      q  = -t^c t (1+t^2)/Phi_5.
 Both have |q(-1)| = 2. Every box has a(-1) = 1, b(-1) = +-1 (Theorem O of mont/proof; CHECKED on 1,170 boxes), so
 |q(-1)| = 1. Hence NO box realises a resonant ray: for every box the unit set {(m,N)} of the S-necklace is finite,
 inside |m| <= (3 Dmax + 6)/2, and each fixed m is an exact 3-term family in t^{3N} (Ghat_13(m), Ghat_31(m) != 0).
 With section 8 this decides S1 completely for every box of the libraries; for an arbitrary box it is a finite check.
 (The mismatch is a t = -1 phenomenon: at t = -1 the L-M eigenvalues 1, -t, t^3 become 1, 1, -1, and the edge pole
 doubles the box slope.)

## 10. Periodic families (rate test of Theorem M2 beyond twists; periodic.py, per2.py)
 172 periodic S2 families (W0)^n, period <= 4, n <= 8: every family is either identically J = 1 ((AAbd)^n, (Ab)^n,
 (BB)^n: trivial) or grows linearly (3 per period after separating parities; e.g. (AbAd)^n spans 0,0,8,8,14,14,20,20;
 the span-8 value is J_B(t) J_B(1/t) for the trefoil box, a composite). No family with bounded non-unit J and no
 contracting family: CHECKED(172).

## 11. THEOREM F' (far field of symmetric L-M twist families; famres.py, famres2.py, famres3.py)
 Family = top half PREFIX . W1 . (L-M twist)^{2k} . W2 . slot box, glued to its mirror; frequencies f in {-3..3} (fitted on
 k in {0,+-1,+-2,+-3}, VERIFIED on k = +-4, every entry), integral part N of the box gives g in {-1,0,1}.
 Necessary conditions for a box slope q = b/a (PROVED): q(-1) = +-1 (a(-1) = 1, b(-1) = eps); q(omega) = 1 at the primitive
 cube roots of unity (a = b mod 1 - t^3).  Outcomes for the m-rays (edges of the Newton polygon not parallel to the f-axis):
  * HEXAGON families (box right after the twist: W2 = '' or 'd'; W1 in {'', d, ab, db}): every m-ray edge relation fails
    at t = -1 and/or at t = omega for every eps and every monomial shift: NO box realises a far-field resonance.
  * RECTANGLE families (M-R letters between twist and slot: W2 in {bD, ab, Db}, A.a^2k.B): the f = +-3 edge form K_3 has
    RANK 1 (det = 0 exactly; it pairs the 1-dimensional V_4 and V_0 channel lines), and both kernel slopes are MONOMIALS
    (t^-6, t^3, t^-3): resonance needs a SCALAR box b = +-t^j a, i.e. the trivial box or a local knot tied in k
    (an equivariant connected summand: excluded by N3).
  * b^{2k} right after the cap: the twist is a kink, J independent of k (Theorem M2, case (i)).
 So, for every slot box and every family tested (9 families), units occur only in a bounded window of the twist
 parameter, and inside each window every fixed m is an exact 3-term family in t^{3N} (Lemma W).  CHECKED(9 families),
 GAP: a uniform proof for all special words (the rank-1/monomial-kernel phenomenon suggests one).

## 12. SUMMARY (02:00-03:05)
 HIT: none.  Every J = 1 found is a presumed-trivial theta-curve (constituent unknotted AND sister invariant a unit).
 THEOREMS / PROVED:
  P1 Mirror rule: x <-> y gives J(1/t) (CHECKED 300).  An amphicheiral theta-curve has a centred palindromic J.
  P2 Geometry: point reflection is the only prime case; it swaps the axis edges, so boxes come in pairs B on A_in,
     B* on A_out (standard one-edge closures are symmetric only with zero special twist = composite).  K amphicheiral
     does NOT imply (K,h) amphicheiral (4_1, 6_3, 8_3, 8_9, 8_12: mirror exchanges the two inversions; CHECKED).
  P3 Structure: J = v^T G v~ with G~^T = G: the top of J reads both ends of the half-state.
  P4 (M2) Mirror pairing kills contraction: for any twist site with monomial eigenvalues, J(k) = sum C_dd' (eps t^{e_d-e_d'})^k
     with C_d'd = C_dd'~; contracting and expanding frequencies vanish together, so J(k) is constant or grows at both ends.
     Engine A's one-ended mechanism has no symmetric analogue.
  P5 (F, F') Far field closed: the resonant rays of the S-necklace and of 8 further L-M families need slopes with
     |q(-1)| = 2, q(omega) != 1, or scalar boxes: none realisable by a prime configuration.
 EXHAUSTED (no unit): S1 complete in (m,N) for 2,878 boxes (R(7), 14 general, 820 products of two R(5), 1,499 nested,
   292 depth-2); balanced products of 3-4 R(5) boxes for m in {2,4,6,8}; S2 two-pole plats, all words |W| <= 7
   (58,887 words); 69 generalised 2-slot forms (special words |W| <= 4) x (R(6) + 279 nested boxes).
 DEPTH / HALF-SPAN: S1 <= 0.29 (max depth 6 of 39; balanced regime 0.11-0.13); E4 forms <= 0.56 (7 of 19 orders);
   S2 tropical <= 0.59 (tropical prediction inflated). Depth does not grow with complexity; needed depth does.
 NEAR MISSES: S1 doubly gated (a_2 = 0 & J(zeta_10) = 1): 3, spans 70-74 (nested boxes, m = +-10). S2: no doubly gated;
   a_2 = 0 minimum span 14 (W = BCABBdb); smallest span 8 (BDDB, a_2 = 2). The span-8 J = J_B J_B~ recurs (composite).
 WHERE A UNIT COULD STILL HIDE IN SYMMETRIC CLASSES: only in finite windows (finite-window coincidences, with no
   structural mechanism); the symmetric trick halves the conditions per order of depth (one end is free) but removes
   contraction, the only known way to get depth.  Untested: the j = 2 middle level (21-dim), non-twist (pseudo-Anosov)
   operators beyond period 4, uniform proof of F' for all special words.

## 13. Cross-check with NOTE-from-integrator.md (read 03:06; treated as data)
 * Points 1-3 (marked inversion must be mirror-equivalent; reciprocal a_2 = 0 & Phi_10-gated J has span >= 14; mirror
   pairs give J * J~) agree with sections 2 and 5: the S2 a_2 = 0 minimum span is exactly 14 (W = BCABBdb, but not Phi_10-gated).
 * NOTE 03:02 (vertical closures with mirror-paired bodies escape the AMPHI-PAIR parity block): these closures are NOT
   amphicheiral theta-curves (a -> -a under the mirror; J not palindromic), so they sit outside this lane's symmetric
   classes; for RATIONAL bodies they are blocked at order 2 anyway by engine A's Theorem V2 (sigma = 0 per box, mirror
   pairs included) and exhausted in engine A 5(e)/(e') (libraries are mirror-closed).
   OBSERVATION (PROVED from the eigen-decomposition): a mirror pair of NESTED boxes F_k(p) * F_k(p)~ has slope -> eps at
   BOTH ends (F_k: (1, eps); its mirror: (eps, 1)); so does any F_k(p) * F_{-k}(p'). The vertical pole has degree -2a-1
   at the top and -a at the bottom, so Y-shifted eps matches both ends only for |a| = 1.
   CHECKED (vertpair.py): V_a(Y^N (F_k(p) * F_k(p)~)), p in R(5), 1 <= |k| <= 6, odd 3 <= |a| <= 9, |N| <= 25:
   187,272 exact evaluations, 0 units, minimum span J = 12 (a_2 = 7).
