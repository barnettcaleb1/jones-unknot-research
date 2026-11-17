# REPORT (lane PROOF, ft/): THEOREM FT and the symbol W_m
Lane: ~/jones-lanes/theory-restart/mont/ft/proof/   (16 Nov 2026, Claude, PROOF lane)
Marks: PROVED / CHECKED(n) / CONJECTURE / GAP / KNOWN.  x := 1 + t.  zeta := primitive 8th root of unity (A^4 = -1, t = -1).

STATUS: COMPLETE (sections 0-6). THEOREM FT PROVED; symbol W_m: state sum PROVED, W_2/W_3 tables; osp(1|2) CHECKED; F3 symbol.

## 0. Summary
 1. THEOREM FT is PROVED (section 2): for any m independent equivariant moves (any mixture of off-axis pair flips x_i <-> y_i and
    on-axis flips x0 <-> y0), Delta^m J is divisible by (1+t)^m; every moment M_k has equivariant order <= k. No class
    restriction, no use of a_2/Mullins/Casson. The integral local model is the coloured theta-curve itself with two exact
    relations (proved by eigenvalues, and checked exactly in the Temperley-Lieb algebra):
      (L1) colour-2 crossing:  R - R^-1 = (A^4 - A^-4)(Id - E'),  A^4 - A^-4 = t^-1 (1-t)(1+t)   [SO(3)/Dubrovnik relation]
      (L2) colour-1/colour-2 full twist:  F - F^-1 = (1+t)[t^-1 F - t^-2 (1-t+t^2) Id]   (t = A^-4; mirror form for F^-1).
    The right sides are honest coloured graphs of the class G (axis + colour-2 arc + colour-2 loops), and the INTEGRALITY LEMMA
    gives <G> in Delta_2 Z[A^+-1] for all G in G (the delta^-1 of a loop's projector cancels because its e-term is a split
    unknot). Units: the normalising units are forced to be multiplicative over sites, u_S = u_empty prod (-t)^{-n_i}, and such
    units cannot spoil the order. Observed: n_i = 4 eps_i (eps_i = upstairs crossing sign), = lp's normalisation increment.
 2. The symbol W_m := [Delta^m J/(1+t)^m](-1) is an explicit state sum on the equivariant chord diagram (3.2): at t = -1 a
    colour-2 loop with even/odd winding around the axis counts -1/3 (= sdim C^{1|2}, str (-1)^F), chords insert
    -2 eps^q (or - un), on-axis sites insert -kappa (F + 3 Id), followed by deframing. Checked against exact alternating sums
    for m = 2, 3, 4 (116/116). W_m = prod eps_i * w(D), w depending only on the labelled chord diagram.
 3. Relations: 1T in three proved forms (even empty chord; empty unenclosed chord; on-axis point outside all chords), the
    general equivariant 1T as a CONJECTURE checked on all order <= 3 types; 4T [t12, t13 + t23] = 0 PROVED in quotient-sign
    normalisation. On-axis-only configurations have W_m = 0 for all m >= 1 (PROVED; explains the brief's observation).
 4. W_2 reproduces M_2 = -24 a_2 on every order-2 type; W_3 is tabulated on all 193 order-3 types (78 nonzero, multiples of 48).
 5. osp(1|2): colour 2 at t = -1 is the delta = -1 Brauer category (Rep OSp(1|2)), the axis is a (-1)^F defect, and the
    symbol equals the deframed osp(1|2) weight system with that defect (CHECKED 214/214 types with explicit (3|2) matrices).
 6. Brief F3 at symbol level: symbol(iota) is integral on all order-3 types; symbol(iota - v_3) takes only the values 0, -8, -16.

## 1. Setting and the integral local model

1.1 Conventions. Kauffman bracket <.> at generic A (tools/kauffman.py convention: crossing 'x' = A (vertical) + A^-1 (cup-cap)),
 delta = -A^2 - A^-2, Delta_2 = delta^2 - 1 = A^4 + 1 + A^-4, t := A^-4 (TH-2BR convention; lp.py's variable is t' = A^4 = 1/t,
 which changes nothing below since 1 + t' = (1+t)/t), x := 1 + t. Note delta = -A^2 (1+t): the ideal (x) of Z[A^+-1] is (delta),
 and Z[A^+-1]/(x) = Z[zeta], zeta = e^{i pi/4} (A^4 + 1 is the 8th cyclotomic polynomial). Colour 2 = 2-cable with the
 Jones-Wenzl projector f_2 = 1 - delta^-1 e (one copy per colour-2 edge suffices: idempotent, slides along the edge).
 J(K,h) =. <Theta;1,1,2>/<Theta_0;1,1,2> (TH-2BR 2.2, ../../proof/REPORT.md 0.2; "=." = up to +-A^k), normalised by J = 1 mod x^2.
 Half-word W with m distinguished crossing letters (SITES) i = 1..m. For S subset [m], W_S = W with the letters in S flipped
 (x <-> y), Theta_S its quotient theta-curve, drawn by the kht++ quotient picture (letter-local, TH-2BR 1.3(b)), blackboard
 framed. Sites in the quotient (checked letter by letter against flat_search.quotient_word):
   off-axis letter c_j (j >= 1): quotient letters (c,2j)(c,2j-1)(c,2j+1)(c,2j) = the 2-cable of one crossing of k with itself;
     with f_2 on both bands this is the colour-2 crossing R^{+-1} in End(V_2 (x) V_2); flipping c gives its inverse (palindromic word).
   on-axis letter c_0: quotient letters (c,0)(c,1)(c,1)(c,0) = the 2-cable (on the band) of the full twist sigma^2 of the axis
     (colour 1) with k (colour 2), an element F^{+-1} of End(V_1 (x) V_2); flipping gives the inverse.
 Exact (unnormalised) values:  Ĵ_S := <Theta_S;1,1,2> / <Theta_0;1,1,2>   (blackboard framing of the fixed diagram).
 Then J_S = u_S Ĵ_S for a unit u_S = +-A^{k_S} of Z[A^+-1].

1.2 LOCAL RELATIONS (PROVED; and CHECKED exactly in the Temperley-Lieb algebra by tl_local.py, sympy, all True).
 (L1) In (f_2 x f_2) TL_4 (f_2 x f_2) = End(V_2 (x) V_2), with R = (f_2 x f_2) C (f_2 x f_2), C = s_1 s_0 s_2 s_1 (all 'x'),
      Id = f_2 x f_2 (the smoothing through which the bands pass), E' = (f_2 x f_2) e_1 e_0 e_2 e_1 (f_2 x f_2) (the colour-2
      cup-cap = the 2-cable of the other smoothing):
         R - R^-1 = (A^4 - A^-4)(Id - E'),      and in fact R = A^4 Id + (A^2 + A^-2) E + A^-4 E',  E = (f_2 x f_2) e_1 (f_2 x f_2).
      Proof. End(V_2 (x) V_2) = C P_0 + C P_2 + C P_4 (commutative, generic A); R has eigenvalues lambda_c = A^-8, -A^-4, A^4
      (Kauffman-Lins lambda^{22}_c), E' = Delta_2 P_0. On channels 2, 4: lambda - lambda^-1 = A^4 - A^-4 and Id - E' acts by 1;
      on channel 0: A^-8 - A^8 = (A^4 - A^-4)(1 - Delta_2). QED (This is the Dubrovnik/SO(3) Kauffman relation, z = q - q^-1,
      q = A^4, kink factor a = A^8, loop value Delta_2 = 1 + q + q^-1: colour 2 = vector representation of SO(3).)
 (L2) In (1 x f_2) TL_3 (1 x f_2) = End(V_1 (x) V_2) = C P_1 + C P_3, with F = (1 x f_2) s_0 s_1 s_1 s_0 (1 x f_2) ('x' letters):
         F - F^-1 = (1+t) [ t^-1 F - t^-2 (1 - t + t^2) Id ];  for the 'y' twist F_y = F^-1:  F_y - F_y^-1 = (1+t)[ F_y - t^-1 (t^2-t+1) Id ].
      Proof. F has eigenvalues t^2 (P_1), t^-1 (P_3) (squares of lambda^{12}_c = -A^-4, A^2), so F^2 = (t^2 + t^-1)F - t, hence
      F^-1 = t + t^-2 - t^-1 F, and F - F^-1 = (1 + t^-1)F - (t + t^-2) = (1+t)[t^-1 F - t^-2 (t^2 - t + 1)]. QED
 Since A^4 - A^-4 = t^-1 - t = t^-1 (1 - t)(1 + t), BOTH moves are "identity + x * (integral combination of honest coloured
 tangles)": the right-hand sides contain only Id, E' (colour-2 smoothings) and Id, F (twist kept or removed).

1.3 The class G and the INTEGRALITY LEMMA.
 DEFINITION. G = the set of framed coloured graphs G in S^3 consisting of the axis A (an unknot with two trivalent vertices,
 both edges colour 1), an arc k of colour 2 joining the two vertices, and finitely many disjoint framed closed curves of
 colour 2 (embedded arbitrarily). G is closed under: replacing a colour-2 crossing by either smoothing (the colour-2 part is a
 1-manifold with boundary = the two vertices, and stays one), and removing or inserting a full twist of k (or a loop) around A.
 INTEGRALITY LEMMA (PROVED). For every G in G, <G> lies in Delta_2 Z[A^+-1]; and <Theta_0> = (unit) Delta_2.
 Hence Ĵ(G) := <G>/<Theta_0> lies in Z[A^+-1].
 Proof. Step 1 (loops). Let l be a colour-2 loop. Expanding its projector, <G> = <G^{l,1}> - delta^-1 <G^{l,e}>, where G^{l,1}
 has l replaced by its plain blackboard 2-cable and G^{l,e} has the 2-cable with e inserted. The blackboard 2-cable bounds
 the thin blackboard band N_l (an embedded annulus; every other strand crosses over or under it, hence misses it). With e
 inserted, the curve is the boundary of N_l cut along one arc: an embedded disc D disjoint from G - l. So it is a split
 unknot, <G^{l,e}> = (-A^3)^f delta <G - l> (f = its framing), and
          <G> = <G^{l,1}> - (-A^3)^f <G - l>.
 Both graphs have one projector fewer; by induction <G> is a Z[A^+-1]-combination of evaluations of graphs G' in which the only
 projector is the f_2 on the arc k, all other strands being plain (colour 1).
 Step 2 (the arc; the argument of ../../proof/REPORT.md 0.2, which never used that A is the only other component). Let
 N = N(k), a ball meeting A in two short arcs at the vertices; B = S^3 - int N is a ball, and T := (G' - k) n B is a framed
 tangle in B with 4 endpoints (plus closed components). The relative skein module of (B, 4 points) is free over Z[A^+-1] on
 the two crossingless matchings, so [T] = y Q_0 + x' Q_inf with y, x' in Z[A^+-1] (Q_0 = matching parallel to k, Q_inf = the two
 short arcs at the vertices). Inside N the coloured arc with its two (1,1,2)-vertices is the band along k with f_2 joining the
 v_top points to the v_bot points. Q_inf caps the f_2-band at one end: 0. Q_0 closes it into an f_2-annulus whose core is an
 unknot (union of a boundary-parallel arc in B and one in N): A^{8f'} Delta_2. So <G'> = A^{8f'} Delta_2 y. For Theta_0, T is
 the trivial tangle with [T] = Q_0. QED
 Remark. Step 1 is where colour 2 matters: the e-term of a closed colour-2 loop always splits off an unknot, so the
 apparent delta^-1 pole cancels exactly. (For the arc, the cancellation is the vanishing of the Q_inf term.)
 CHECK: J_raw(-1) = 1 in 952/952 evaluations (check_units.py), i.e. y = 1 mod delta (Step 2 with u = y + delta x' = 1).

## 2. THEOREM FT

Notation. For f : {0,1}^m -> M (M a module), a base point S_0 and T subset [m], the alternating sum on the face through S_0 is
 Delta^T_{S_0} f := sum_{U subset T} (-1)^{|U|} f(S_0 xor U).  "f has x-order <= 0 on all faces" means Delta^T_{S_0} f in x^{|T|} M
 for all S_0, T.

THEOREM 2.1 (unnormalised FT; PROVED). For every S_0 and T, Delta^T_{S_0} Ĵ lies in x^{|T|} Z[A^+-1]. More precisely
 Delta^T_{S_0} Ĵ = x^{|T|} * (a Z[A^+-1]-combination of Ĵ(G), G in G).
 Proof. The coloured evaluation is multilinear in the contents of disjoint balls (relative skein modules), so
 Delta^T_{S_0} Ĵ = <Theta_{S_0} with the piece X_i at each site i in T replaced by X_i - X_i^-1> / <Theta_0>, X_i in {R^{+-1}, F^{+-1}}.
 By (L1)/(L2), X_i - X_i^-1 = x * Y_i with Y_i = +-t^-1 (1-t)(Id - E') (off-axis) or +-[t^-1 F - t^-2(1-t+t^2) Id] (on-axis, resp.
 its mirror form); expanding, the right side is x^{|T|} times a Z[t^+-1]-combination of <G>/<Theta_0> with G obtained from Theta_{S_0}
 by smoothing colour-2 crossings and removing full twists: G is in the class G. Integrality Lemma. QED
 CHECKED: Delta^m J_raw divisible by (1+t)^m with NO normalisation, 60/60 random configurations, m = 2..5, mixed sites
 (check_units.py). (J_raw = lp's y-coefficient divided by the monomial u = y + delta x', which is identically 1, so J_raw is a
 fixed unit times Ĵ.)

LEMMA 2.2 (units congruent to 1; PROVED). (a) A unit +-A^k of Z[A^+-1] is = 1 mod x iff it equals (-t)^n for some n in Z
 (i.e. A^{8j} or -A^{8j+4}). (b) (-t)^n = 1 - n x mod x^2 for every n in Z. (c) For n in Z, n x in x^2 Z[A^+-1] implies n = 0.
 Proof. (a) Z[A^+-1]/(x) = Z[zeta] by A -> zeta; +-zeta^k = 1 iff (k = 0 mod 8, +) or (k = 4 mod 8, -); A^8 = t^-2, -A^4 = (-t)^-1.
 (b) -t = 1 - x. (c) evaluate n = x q at A = zeta. QED

PROPOSITION 2.3 (coherence of the normalising units; PROVED). There are integers n_1, ..., n_m with
        u_S = u_empty * prod_{i in S} (-t)^{-n_i}    for all S.
 Proof. J_S = 1 mod x^2 gives Ĵ_S = u_S^-1 mod x^2. Put v_S := u_empty / u_S (a unit). (i) |T| = 1 in Theorem 2.1: Ĵ_{S+i} = Ĵ_S
 mod x for all S, i, so v_S = v_empty = 1 mod x, and v_S = (-t)^{n_S} by Lemma 2.2(a). (ii) |T| = 2: all second differences of
 S -> Ĵ_S vanish mod x^2, so S -> Ĵ_S is affine mod x^2: Ĵ_S = Ĵ_empty + sum_{i in S} (Ĵ_{i} - Ĵ_empty) mod x^2. Multiply by u_empty and
 use (b): 1 - n_S x = 1 - (sum_{i in S} n_i) x mod x^2, with n_i := n_{i}. By (c), n_S = sum_{i in S} n_i. QED
 CHECKED: for 60/60 configurations the lp normalisation J = sgn t'^k J_raw has constant sgn and k_S additive over sites,
 with every increment = +-4 (on-axis: flipping x0 -> y0 always -4, y0 -> x0 always +4; off-axis: both signs for both letters,
 according to the upstairs crossing sign, see 3.2). (check_units.py)

LEMMA 2.4 (multiplicative units do not spoil the order; PROVED). Let f : {0,1}^m -> M have x-order <= 0 on all faces and
 w_i in 1 + x Z[A^+-1]. Then g_S := prod_{i in S} w_i * f_S also has: Delta^{[m]}_{empty} g in x^m M.
 Proof. g_S = sum_{U subset S} prod_{i in U} (w_i - 1) f_S, so Delta^{[m]} g = sum_U prod_{i in U}(w_i - 1) (-1)^{|U|} Delta^{[m]-U}_U f,
 and each term lies in x^{|U|} x^{m-|U|} M. QED

THEOREM 2.5 (THEOREM FT; PROVED). For m independent equivariant moves (any mixture of off-axis pair flips x_i <-> y_i, i >= 1,
 and on-axis flips x0 <-> y0) on any half-word,
        Delta^m J := sum_{S subset [m]} (-1)^{|S|} J_S   is divisible by (1+t)^m in Lambda = Z[t^+-1].
 Equivalently Delta^m M_k = 0 for k < m, i.e. each moment M_k = k! [h^k] J(-e^h) has equivariant order <= k.
 Proof. J_S = u_empty prod_{i in S} (-t)^{-n_i} Ĵ_S (Prop. 2.3); apply Lemma 2.4 with f = Ĵ (Theorem 2.1) and w_i = (-t)^{-n_i}:
 Delta^m J in x^m Z[A^+-1]. Since Z[A^+-1] = sum_{r mod 4} A^r Lambda (direct) and x is in Lambda, x^m Z[A^+-1] n Lambda = x^m Lambda.
 Equivalence: Delta^m J = (1 - e^h)^m Q(-e^h) after t = -e^h, which is O(h^m). QED
 REMARKS. (1) The proof applies verbatim to any family of theta-curves differing by colour-2 crossing changes and full twists
 of the arc about the axis; half-words are only one way to present them. (2) It does not use a_2, Mullins, Casson or any
 class restriction. (3) It gives the explicit derivative formula Delta^m J = x^m * (Lambda-combination of Ĵ(G), G in G), used in 3.

## 3. The symbol W_m

DEFINITION. For an m-site configuration, W_m := [ Delta^m J / x^m ](t = -1) (an integer, by Theorem 2.5); likewise W_m(Ĵ) for the
 exact values (an element of Z[zeta], in fact of Z, see 3.2). With t = -e^h: [h^m] Delta^m J(-e^h) = (-1)^m W_m and
 Delta^m M_m = m! (-1)^m W_m. (lp's variable t' = 1/t gives [Delta^m J/(1+t')^m](t'=-1) = (-1)^m W_m.)

3.1 Evaluation at t = -1 of graphs in G.
 Say G in G is in QUOTIENT FORM if it is drawn like a kht++ quotient picture: the axis is a vertical line, the colour-2 part lies
 to its right except at full twists F^{+-1} around the axis (this holds for Theta_S and for every graph produced from it by
 smoothing sites or removing twists). For a colour-2 loop l let w(l) = number of full twists traversed by l (= lk(l, A)).
 LEMMA 3.1 (PROVED). For G in G in quotient form,   Ĵ(G) = prod_{loops l} c(w(l) mod 2)  mod x,   c(0) = -1, c(1) = 3.
 Proof. (i) By (L1) and the Integrality Lemma, changing a colour-2 crossing changes Ĵ(G) by an element of x Z[A^+-1]; by (L2),
 so does replacing a full twist F by F^-1; a colour-2 kink costs A^{+-8} = t^{-+2} = 1 mod x. (ii) Let l be a loop. Free homotopy
 classes of loops in the solid torus S^3 - A are classified by w(l); a homotopy in S^3 - A is an isotopy plus crossing changes of l
 with itself and with the other colour-2 strands. So mod x we may move l into a small ball meeting A in an unknotted arc and
 disjoint from everything else, as a coil winding w(l) times around that arc, i.e. w(l) consecutive full twists; by (i) these
 may be flipped, F F^-1 cancels, leaving w(l) mod 2 twists. A split colour-2 unknot multiplies by Delta_2 = -1 mod x; a colour-2
 meridian of a colour-1 edge acts by the scalar [6]/[2] = A^8 + 1 + A^-8 = 3 mod x (Kauffman-Lins encircling lemma). (iii) After
 removing all loops, Theta' (a theta-curve in quotient form, same diagram minus the loops) has Ĵ(Theta') = A^{8f'} y = y = u mod x
 (Integrality Lemma, Step 2; u = y + delta x'), and u = (-A^3)^{writhe} = 1 because the closure T'(1/0) is the axis with two
 "fingers" (antiparallel band pairs): band-band crossings come in quadruples of total writhe 0, axis-band crossings occur only in
 the twists s0 s1 s1 s0 with total writhe 0 (the referee's argument for u = 1). QED  CHECKED: J_raw(-1) = 1 (952/952).
 Interpretation: c(0) = -1 = sdim C^{1|2}, c(1) = 3 = str_{C^{1|2}}((-1)^F) (section 4).

3.2 STATE-SUM FORMULA (PROVED; CHECKED against exact alternating sums: m = 2: 26/26, m = 3: 40/40, m = 4: 50/50, symbol.py).
 Data of a configuration, read along the quotient arc k (oriented v_top -> v_bot; symbol.py: trace()):
  off-axis site i: k passes the crossing twice, at a_i < b_i; kappa_i = +1 for an x-letter, -1 for a y-letter; pi_i = +1 if the
   two passages run in the same vertical direction, -1 otherwise; tau_i = number of on-axis letters (x0/y0, sites or not)
   passed between a_i and b_i, mod 2 (the SHEET LABEL: tau_i = 0 iff the upstairs pair is {a,b},{h(a),h(b)}).
  on-axis site j: k passes it once, at c_j; kappa_j = +1 (x0) or -1 (y0).
 Smoothings (w.r.t. the orientation of k): "or" = in(a)-out(b), in(b)-out(a) (splits off a loop), "un" = in(a)-in(b), out(a)-out(b).
 (a) W_m(Ĵ) = sum over choices (or/un at each off-axis site, F/Id at each on-axis site) of
        prod_off [ -2 kappa_i pi_i (+1 or, -1 un) ] * prod_on [ -kappa_j (1 for F, 3 for Id) ] * prod_{loops l} c(w(l) mod 2),
     where the winding of a loop counts the on-axis letters it passes (an on-axis SITE counts only with choice F).
     Proof. Theorem 2.1's expansion with Y_i(-1): (A^4 - A^-4)/x = t^-1 (1-t) -> -2, the vertical smoothing Id being "or" iff
     pi_i = +1; [t^-1 F - t^-2(1-t+t^2)] -> -(F + 3) for x0 and [F_y - t^-1(t^2-t+1)] -> F_y + 3 for y0; then Lemma 3.1. QED
 (b) n_i = W_1 of site i alone: n_i = 4 kappa_i pi_i (-1)^{tau_i} (off-axis; c(tau) - 1 = -2(-1)^tau), n_j = -4 kappa_j (on-axis).
     Define eps_i by n_i = 4 eps_i. CHECKED 721/721: eps_i is the upstairs crossing sign of the site's crossing(s) (bracket
     convention = minus alex.writhe's convention), and n_i is exactly lp's normalisation increment (check_signs.py).
     So: flipping any site changes the normalising power by t'^{4 eps_i}; the quotient sign of an off-axis site is
     eps^q_i = kappa_i pi_i = eps_i (-1)^{tau_i} (orientation reverses on the other sheet).
 (c) DEFRAMING (PROVED): W_m(J) = sum_{T subset [m]} prod_{i in T} (-n_i) * W_{[m]-T}(Ĵ), where in W_{[m]-T}(Ĵ) the sites of T are
     ordinary crossings (off-axis: not smoothed; on-axis: twists, winding 1).
     Proof. Lemma 2.4's expansion: w_i - 1 = (-t)^{-n_i} - 1 = n_i x mod x^2, u_empty = 1 mod x (Lemma 3.1), and the order-(m-|T|)
     symbol at base T equals that at base empty (they differ by a Delta of order m-|T|+1). QED
 So W_m(J) = prod_i eps_i * w(D), with w(D) depending only on the EQUIVARIANT CHORD DIAGRAM D: the interval k with the chords
 (a_i, b_i) labelled by tau_i in Z/2 and the on-axis points c_j (equivalently, upstairs: K with the involution, off-axis chord
 pairs {c, h(c)} and on-axis chords {p, h(p)}). Reason: a loop is, as a mod-2 chain on k, a sum of chord intervals [a_i,b_i]
 (its boundary consists of chord endpoints only), so its winding parity is the sum of the corresponding tau_i (taken with the
 F/Id choices at on-axis sites inside), and nothing else enters.

3.3 RELATIONS.
 Notation: a SITE POINT is a chord endpoint or an on-axis site; twists that are not sites only enter through the labels.
 (1T-a) (PROVED) If no site point lies inside (a_i, b_i) and tau_i = 0, then W(D) = 0.
 (1T-b) (PROVED) If no site point lies inside (a_i, b_i) and no chord interval contains (a_i, b_i), then W(D) = 0 (any tau_i).
 (1T-c) (PROVED) If an on-axis site c_j lies in no chord interval, then W(D) = 0.
   Proof. Every segment of k lies on exactly one component, traversed once, so a loop is (as a set) the mod-2 sum of the chord
   intervals it jumps across. In (a)/(b): for every choice at the other sites, "or" at i splits off the loop [a_i,b_i] (factor
   c(tau_i)) and removes that segment from the component that contained it; this does not change that component's parity if
   tau_i = 0, or if the component is the arc (case b: no chord encloses the segment, so it is always on the arc); "un" at i has
   the same components and parities as passing straight through. So site i contributes -2 kappa_i pi_i (c(tau_i) - 1) V = n_i V,
   V = the state sum with i passed through. In (c), c_j is on the arc in every state, so its F/Id choice changes no loop:
   factor -kappa_j (1 + 3) = n_j. In all cases W_S(Ĵ) = n_i W_{S-i}(Ĵ) for every site set S containing i, and the deframing sum
   of 3.2(c) cancels in pairs (T with and without i). QED
   WARNING (corrects a tempting shortcut): an "empty" chord with ODD label inside another chord does NOT vanish
   (W_2(nested, inner label 1) = -48): its split-off loop changes the parity of the enclosing loop.
 (1T-equivariant) (CONJECTURE; CHECKED on all 215 equivariant chord diagram types of order <= 3, check_1t.py) W(D) = 0 whenever
   the upstairs lift of D has an isolated chord or a pair {c, h(c)} that crosses only itself. (a), (b), (c) are the cases: an
   even empty chord (two isolated lifts), an empty unenclosed chord (lifts isolated or crossing only each other), an on-axis
   chord {p, h(p)} crossed by nothing. At order <= 3 the converse also holds: W(D) = 0 ONLY in these cases (0 exceptions).
 ON-AXIS-ONLY CONFIGURATIONS (PROVED): if all m >= 1 sites are on-axis, every on-axis point lies in no chord interval (there are
   none), so W_m = 0 by (1T-c). Upstairs: on-axis chords {p, h(p)} are mutually parallel, so each is isolated. This explains the
   brief's observation that on-axis-only alternating sums vanish already at m = k.
 (4T) (PROVED; CHECKED 150/150 random backgrounds, check_4t.py) Weight off-axis chords by
   their QUOTIENT signs eps^q_i (= kappa_i pi_i). For three small segments I_1, I_2, I_3 of k with sheets s_1, s_2, s_3 and chords
   t_ab between I_a, I_b with label s_a + s_b:  [t_12, t_13 + t_23] = 0, i.e. D1 - D2 + D3 - D4 = 0 with D1 = (on I_1: e13 before
   e12), D2 = (e12 before e13), D3 = (on I_2: e23 before e12), D4 = (e12 before e23); every other part of D is arbitrary.
   Proof. In the operator form of section 4 a chord is 2 Omega = P - K inserted at its two points (Koszul signs), conjugated by
   g = (-1)^F on the sheet-1 points; t_ij = P_ij - K_ij satisfies [t_12, t_13 + t_23] = 0 in the Brauer algebra B_3(delta) for
   every delta (verified exactly with delta symbolic, check_deframed.py (b); it is the so(N) Casimir identity interpolated in N),
   and conjugation by g x g x g preserves it.
   Deframing adds scalar multiples of the identity to chords, which commute. QED (In upstairs-sign normalisation the relation
   fails, 38/150: the natural signs for 4T are the quotient signs.)

3.4 W_2 (PROVED: state sum; CHECKED 26/26 exact; abstract.py). Upstairs signs +1 (in general multiply by eps_1 eps_2):
        two chords crossed (c0 c1 c0 c1), any labels ......................... -24
        two chords nested (c0 c1 c1 c0), inner label 1 ........................ -48     (inner label 0: 0)
        two chords disjoint ........................................................ 0
        chord containing an on-axis point (c0 o c0), any label ................ -24     (point outside: 0)
        two on-axis points ......................................................... 0
 Agreement with M_2 = -24 a_2 (KNOWN/PROVED via Mullins + Casson): Delta^2 M_2 = 2 W_2, and Delta^2 a_2 = sum over pairs of upstairs
 crossings (one from each site) of eps eps' [chords cross]. Counting upstairs crossings: crossed: 2; nested: 4 if the inner label
 is 1, else 0; disjoint: 0; on-axis point inside a chord: 2, outside: 0; two on-axis: 0 (parallel). So W_2 = -12 Delta^2 a_2 in
 every case: the symbol calculus reproduces M_2 = -24 a_2 at the level of weight systems (a consistency check, not a new proof).

3.5 W_3 ON ALL ORDER-3 TYPES (PROVED: state sum; table CHECKED against 40 exact m = 3 sums; w3_table.py, w3_table.json).
 193 labelled types (3 chords: 15 matchings x 8 labels; 2 chords + 1 point: 60; 1 chord + 2 points: 12; 3 points: 1); 78 nonzero.
 Upstairs signs +1 (general: multiply by eps_1 eps_2 eps_3). Labels listed for c0 c1 c2 (chords named by first endpoint),
 counting on-axis sites as twists; * = either value. All values are multiples of 48.
   c0 c1 c0 c2 c1 c2   ***  144
   c0 c1 c0 c2 c2 c1   **1  288                    (**0: 0)
   c0 c1 c1 c2 c0 c2   *1*  288                    (*0*: 0)
   c0 c1 c1 c2 c2 c0   *11  576                    (otherwise 0)
   c0 c1 c2 c0 c1 c2   *0*  288    *1*  192        (all three mutually crossing)
   c0 c1 c2 c0 c2 c1   **0  144    **1  336
   c0 c1 c2 c1 c0 c2   *0*  144    *1*  336
   c0 c1 c2 c1 c2 c0   *01, *10  288    *11  384    *00  0
   c0 c1 c2 c2 c0 c1   **1  384                    (**0: 0)
   c0 c1 c2 c2 c1 c0   *01  96     *11  672        (**0: 0)
   c0 c1 c0 o c1       **   144
   c0 c1 c1 o c0       *1   288                    (*0: 0)
   c0 c1 o c0 c1       **   192
   c0 c1 o c1 c0       *0   48     *1   336
   c0 o c1 c0 c1       **   144
   c0 o c1 c1 c0       *1   288                    (*0: 0)
   c0 o o c0           *    144
   every other type (in particular every type with an isolated upstairs chord or pair, and o o o): 0.
 Observations: the label of the chord with the earliest endpoint never matters in this table; in the t-variable
 Delta^3 M_3 = -6 W_3 (in lp's variable t' = 1/t: Delta^3 M_3^lp = +6 W_3, see 3.6), so Delta^3 M_3/36 = -+W_3/6 is a multiple of 8,
 consistent with M_3/36 in Z (brief F3).

3.6 The brief's F3 at the symbol level: v_3(K) and iota (iota.py, check_iota.py, iota_table.txt).
 Sign conventions: the brief's moments use lp's variable t' = 1/t, so M_k^lp = (-1)^k M_k^(t) and Delta^3 M_3^lp/36 = + W_3/6
 (CHECKED: Delta^3 M_3^lp = 6 W_3, 40/40 exact m = 3 sums).
 Symbol of v_3 = -(V'''(1) + 3V''(1))/36 on an equivariant configuration (PROVED by the classical argument below; CHECKED 40/40
 against exact third differences of v_3 computed from kauffman.bracket, 8 of them nonzero): for an order-3 knot invariant,
 Delta^3 over three equivariant sites = sum over choices of one upstairs crossing per site of the ordinary third difference
 (terms with >= 4 single differences vanish), and the ordinary symbol of [h^n] V(e^h) is
     W^V_m(D) = prod eps * sum_{U subset chords} (3/2)^{|U|} (1/2)^{m-|U|} sum_{or/un on the others} (+-1) (-2)^{c-1}
 (D a chord diagram on the circle K, c = number of circles after smoothing; same argument as 3.2 for the plain bracket:
 sigma_+ - sigma_- = (A - A^-1)(or - un), A - A^-1 = -h/2 + O(h^3), <L>(A=1) = (-1)^{#crossings} (-2)^{c-1}, and the writhe
 normalisation (-A^3)^{-w} deframes with factor A^{6 eps} = 1 - (3/2) eps h). Values: crossed pair -3 (= -3 Delta^2 a_2, since
 [h^2] V(e^h) = -3 a_2), path diagram P3 -6, triangle K3 -12; and [h^3] V(e^h) = -6 v_3.
 RESULT (PROVED from 3.5 and the above; table in iota_table.txt): with iota := (M_3^lp/36 - 7 v_3)/5 (brief F3),
   symbol(iota) = (W_3/6 - 7 symbol(v_3))/5 is an INTEGER on all 192 order-3 types (values 0, +-2, +-4, +-8), and
   symbol(iota - v_3) = (W_3 - 72 symbol(v_3))/30 takes only the values 0, -8, -16 (upstairs signs +1):
     -8 on: c0 c1 c2 c0 c1 c2 (*1*); c0 c1 c2 c0 c2 c1 (**1); c0 c1 c2 c1 c0 c2 (*1*); c0 c1 o c0 c1 (**); c0 c1 o c1 c0 (**);
     -16 on: c0 c1 c2 c1 c2 c0 (*11); c0 c1 c2 c2 c0 c1 (**1); c0 c1 c2 c2 c1 c0 (**1);
     0 on every other type (in particular wherever W_3 = 72 symbol(v_3), e.g. c0 c1 c0 c2 c1 c2, c0 o o c0).
   So at the symbol level M_3^lp/36 = 12 v_3 + 5 (iota - v_3), and the correction iota - v_3 has symbol -8 x (a weight system
   with values 0, 1, 2), supported where an odd label or an on-axis point sits inside an overlap or a nesting.
 CAVEATS. (i) Data (150 rows of ident3_rows.json): iota - v_3 is an integer (150/150) but NOT divisible by 8 as an invariant
 (57/150): its lower-order part is not. (ii) A symbol not proportional to symbol(v_3) does not by itself prove that iota is
 not an invariant of K: an order-4 invariant of K can have a nonzero equivariant order-3 symbol (choosing both crossings of a
 pair). The brief's direct example (iota = 1 with v_3 = 0) remains the evidence that iota is not determined by K.

## 4. osp(1|2) interpretation (brief F2, last paragraph)

4.1 Colour 2 at t = -1 (PROVED). Mod x, (L1) reads R = R^-1 (z = A^4 - A^-4 -> 0), the colour-2 kink factor is A^8 -> 1 and the
 colour-2 loop is Delta_2 -> -1. So, inside evaluations of graphs in G (which are integral, Integrality Lemma), the colour-2
 theory at t = -1 is the Brauer category with symmetric crossing and loop value delta = -1. It is realised (KNOWN: Brauer category
 at delta = m - 2n -> Rep(OSp(m|2n))) by V = C^{1|2} with an even supersymmetric form: P = super flip, K = cup-cap, sdim V = -1.
 Channel check: V_2 x V_2 = V_0 + V_2 + V_4 has, at t = -1, quantum dimensions (1, -1, 1) and R-eigenvalues (1, 1, -1); V x V =
 C + V + osp(1|2) has superdimensions (1, -1, 1) and super-flip eigenvalues (+1, +1, -1). This is the brief's guess, now a statement.
4.2 The axis is a parity defect (PROVED, Lemma 3.1): a colour-2 loop with winding w around the axis evaluates to str_V(g^w),
 g = (-1)^F = diag(1, -1, -1), an even element of OSp(1|2) acting on osp(1|2) by the parity automorphism (str 1 = -1, str g = 3).
4.3 The symbol is the deframed osp(1|2) weight system with the parity defect (CHECKED 214/214 types of order <= 3, osp12.py;
 the general identity is the KNOWN fact that Brauer-diagram evaluations equal OSp(1|2) evaluations, plus 2 Omega = P - K, which
 osp12.py verifies: Omega = sum_a x^a (x) x_a (str(x^a x_b) = delta) equals (P - K)/2 on V (x) V).
   W_m(Ĵ)(D) = prod_off (-2 eps^q_i) prod_on eps_j * < v0 | WORD | v0 >,
   WORD = the U(osp(1|2))-word read along k (first position leftmost, Koszul signs for the chord tensors): each off-axis chord
   inserts 2 Omega = 2 sum_a x^a (x) x_a at its endpoints, each on-axis SITE inserts g + 3, every other on-axis letter inserts g;
   v0 = the even basis vector (the vertices are the g-even boundary condition: <v0|g^w|v0> = 1, matching Ĵ(theta) = 1 mod x).
 Deframing (3.2(c)) is multilinear in the site insertions, so W_m(J) has the same form with the DEFRAMED insertions
   off-axis chord:  -2 eps^q_i (2 Omega + 2 (-1)^{tau_i})      on-axis site:  eps_j ((g + 3) - 4 g) = 6 eps_j P_odd,
 P_odd = (1 - g)/2 (the dropped on-axis site keeps its twist g; the dropped chord is the identity). On-axis sites thus project the
 strand onto the odd part of V; since the vertices see v0, an on-axis site outside all chords gives 0 (= 1T-c). The label tau of
 a chord is invisible in the word (it is the parity of the g's between its endpoints): Omega^(1) = (g x 1) Omega (g x 1) =
 Omega_even - Omega_odd.
 So F2's conceptual guess holds in this precise sense: J(-e^h) is a Vassiliev series whose symbols are those of osp(1|2) at its
 classical point on the quotient chord diagram, with the axis acting as (-1)^F, followed by deframing. (Whether this extends
 beyond symbols to a full osp(1|2)/U_q(osp(1|2)) description of J near t = -1 is not addressed here.)

## 5. Checks (scripts in this folder; exact arithmetic; each run seconds to a few minutes)
 tl_local.py   (L1), (L2) and R = A^4 Id + (A^2+A^-2) E + A^-4 E' in the Temperley-Lieb algebra (sympy, exact) ......... all True
 check_units.py J_raw(-1) = 1 ......................................................................... 952/952
                Delta^m J_raw divisible by (1+t)^m, no normalisation, m = 2..5 mixed ...................... 60/60
                normalisation sign constant, exponent additive over sites, increments +-4 ............... 60/60
 check_signs.py n_i (= W_1 of the exact value, state sum) = lp normalisation increment ...................... 721/721
                n_i/4 = upstairs crossing sign (bracket convention = -alex.writhe convention), both site types .. 721/721
 symbol.py      state-sum W_m (3.2) = exact [Delta^m J/x^m](-1):  m = 2: 26/26, m = 3: 40/40, m = 4: 50/50
                (mixed sites and off-axis only; nonzero values occur, e.g. 144, 288, -24, -48)
 abstract.py    W_2 table; depends only on labels (one value per labelled type) ................................. 12+6+1 types
 w3_table.py    W_3 on all 193 order-3 labelled types (78 nonzero), single value per type .................... w3_table.json
 check_4t.py    4T in quotient-sign normalisation, for W(J) and W(Ĵ) ........................................ 150/150 each
 check_1t.py    equivariant 1T (isolated upstairs chord or pair => W = 0) ........................ 129/129, converse 0 exc.
 osp12.py       osp(1|2) (dim 3|2), Omega = (P - K)/2, Lie-superalgebra weight system = Brauer state sum ........ 214/214
 check_deframed.py (a) deframed insertions (4.3) give W(J) .................................................... 214/214
                   (b) [t12, t13 + t23] = 0 in B_3(delta), delta symbolic ...................................... True
 check_iota.py  v_3 symbol (upstairs Jones state sum) = exact Delta^3 v_3; Delta^3 M_3^lp = 6 W_3 ................ 40/40 each
 iota.py        symbols of v_3 and iota on all 192 order-3 types; iota symbol integral ...................... 192/192
 check_ft.py, check_ft2.py: copies of the brief's scripts (not modified; Theorem 2.5 makes their PRED ZERO lines theorems).

## 6. Status of every claim
 PROVED  (L1) R - R^-1 = (A^4 - A^-4)(Id - E') and (L2) F - F^-1 = (1+t)[t^-1 F - t^-2(1-t+t^2) Id] (and mirror); also CHECKED exactly.
 PROVED  INTEGRALITY LEMMA: <G> in Delta_2 Z[A^+-1] for every G in G (theta + colour-2 loops).
 PROVED  Theorem 2.1 (unnormalised FT, all faces), Lemma 2.2, Proposition 2.3 (normalising units are multiplicative over sites,
         u_S = u_empty prod (-t)^{-n_i}), Lemma 2.4, THEOREM 2.5 = THEOREM FT: Delta^m J divisible by (1+t)^m for any m independent
         equivariant moves, any mixture of off-axis and on-axis; each M_k has equivariant order <= k.
 PROVED  Lemma 3.1 (t = -1 values: prod over loops of c(w mod 2), c(0) = -1, c(1) = 3), the state-sum formula 3.2(a), n_i formula
         3.2(b), deframing 3.2(c); hence W_m depends only on the equivariant chord diagram (W_m(J) = prod eps_i * w(D)).
 CHECKED n_i = 4 eps_i with eps_i the upstairs crossing sign (721), = lp's normalisation increment (721).
 PROVED  1T-a, 1T-b, 1T-c; on-axis-only configurations have W_m = 0 for every m >= 1.
 CONJ.   Equivariant 1T in general (isolated upstairs chord or isolated pair => W = 0); CHECKED on all 215 types of order <= 3.
 PROVED  4T (quotient-sign normalisation, labels = sheet differences); the Brauer identity [t12, t13+t23] = 0 in B_3(delta) is
         verified exactly (symbolic delta); CHECKED 150/150 on the symbol.
 PROVED  W_2 table (3.4); it agrees with M_2 = -24 a_2 on every order-2 type (consistency, not a new proof of M_2 = -24 a_2).
 PROVED  W_3 table (3.5) (computed from the proved state sum; CHECKED against 40 exact sums).
 PROVED  4.1-4.2 (colour 2 at t = -1 is the delta = -1 Brauer category; the axis acts as (-1)^F on loops).
 CHECKED 4.3: symbol = deframed osp(1|2) weight system with the parity defect, 214/214 types of order <= 3, both for W(Ĵ)
         (osp12.py) and, with the deframed insertions, for W(J) (check_deframed.py (a)); the general identity rests on the
         KNOWN Brauer -> Rep(OSp(1|2)) correspondence.
 PROVED  3.6: symbol of v_3 (classical upstairs Jones state sum; CHECKED 40/40), hence the symbol of iota (brief F3): integral
         on all 192 order-3 types; symbol(iota - v_3) in {0, -8, -16} with explicit support. CHECKED: iota - v_3 itself is not
         divisible by 8 (57/150). Whether iota is an invariant of K is NOT settled by the symbol (caveat ii).
 Not claimed: anything about Lemma Q itself, an identification of iota beyond its symbol, or novelty.
