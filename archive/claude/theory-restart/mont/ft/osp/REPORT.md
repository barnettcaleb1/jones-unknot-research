# REPORT (lane OSP): conceptual mechanism behind THEOREM FT (BRIEF F2)
Lane folder: ~/jones-lanes/theory-restart/mont/ft/osp/   (16 Nov 2026, Claude, OSP lane)
Marks: PROVED / CHECKED(n) / CONJECTURE / GAP / KNOWN.  No novelty claims (LIT lane decides).
Status: COMPLETE for this round (16 Nov 2026). Headline: THEOREM FT PROVED (section 2.2); mechanism = classical osp(1|2) with a parity defect.

## 0. Conventions
Kauffman-Lins (KL): loop delta = -A^2-A^-2, t = A^-4, colour n = n parallel strands with Jones-Wenzl f_n, Delta_n = (-1)^n [n+1]
([m] = (A^{2m}-A^{-2m})/(A^2-A^{-2})), twist theta_n = (-1)^n A^{n(n+2)}, half-twist eigenvalue of colours a,b on channel c:
lambda^{ab}_c = (-1)^{(a+b-c)/2} A^{(c(c+2)-a(a+2)-b(b+2))/2}; full twist of a around b on channel c: theta_c/(theta_a theta_b).
Expansion point: t = -e^h, A = e^{i pi/4} e^{-h/4} (so A^4 = t^-1, A_0 := e^{i pi/4} at h = 0). Crossing letters: kauffman.py 'x' = A.1 + A^-1.e
= the KL positive braiding R (eigenvalues A, -A^-3); colour-2 crossing x_i (i>=1) in the quotient = 2-cable of R = R_22; x0 = positive
full twist Yhat of the arc around the axis, y0 = Yhat^-1 (flat_search.quotient_word). "Raw" J = the plain-bracket y-coefficient of the
fixed diagram (regular-isotopy invariant, no unit normalisation); normalised J as in the BRIEF.
CONVENTION WARNING: lp.J_raw maps A^e -> t^{e/4}, i.e. lp uses t = A^{+4} (mirror of the KL t = A^-4 used in sections 1-2 and in
ident3.VK). So lp's moments M_k are (-1)^k times the KL-convention moments of the same diagram. Numbers quoted "in the F3
convention" (M_k from lp, v_3 from ident3.VK) follow BRIEF F3; in one common convention the sign of every odd-k relation flips.

## 1. Part (1): sl_2 colour 2 at t = -1 versus osp(1|2) / so(3)
1.1 Colour-2 data at t = -e^h (PROVED: direct from the KL formulas in section 0).
 R_22 eigenvalues on channels c = 0,2,4:  A^-8 = t^2 = e^{2h},  -A^-4 = -t = e^{h},  A^4 = t^-1 = -e^{-h}   (at h=0: +1,+1,-1).
 Twist theta_2 = A^8 = t^-2 = e^{-2h}.  Delta_2 = t^-1+1+t = 1-2cosh h = -1 - h^2 - ...;  Delta_1 = delta = 2i sinh(h/2) (zero at h=0).
 Channel quantum dims at h=0: Delta_0, Delta_2, Delta_4 = 1, -1, +1 (generally Delta_{2m}(-1) = [2m+1]_{q=i} = (-1)^m).
 LEMMA 1.1 (colour-2 skein = Dubrovnik; PROVED by checking the three channels):
     R_22 - R_22^{-1} = z (1 - E),   z = A^4 - A^-4 = t^-1 - t = (1-t)(1+t)/t,   kink = a = A^8 = t^-2,   loop = Delta_2,
 where 1 = vertical smoothing and E = horizontal (cup-cap) smoothing of the two colour-2 strands (E = Delta_2 P_0).
 Check: channel 0: z(1 - Delta_2) = A^-8 - A^8; channels 2, 4: z = A^4 - A^-4 = (-A^-4) - (-A^-4)^{-1} = A^4 - A^-4.
 So colour 2 obeys the Dubrovnik (unoriented Kauffman) skein with (a, z) = (q3^2, q3 - q3^-1), q3 := t^-1: the SO(3) specialisation.

1.2 The variable change (PROVED at the level of skein parameters; the osp side is KNOWN-MEMORY, see refs below).
 Dubrovnik specialisations (KNOWN-MEMORY: Turaev/Reshetikhin; for supergroups the invariant depends only on N = m - 2n):
     SO(N) / OSp(m|2n) with N = m-2n, fundamental rep at q:  (a, z) = (q^{N-1}, q - q^{-1}),  loop = 1 + [N-1]_q -> N at q = 1.
 OSp(1|2) is N = -1: (a, z) = (q^-2, q - q^-1), loop 1 - q - q^-1 (= -1 = sdim C^{1|2} at q = 1).
 Matching with 1.1:  t^-2 = q^-2,  t^-1 - t = q - q^-1,  t+1+t^-1 = 1-q-q^-1   <=>   t = -q   (no extra sign, no framing factor).
 Equivalently SO(3) at q3 = -q^-1 equals SO(-1) = OSp(1|2) at q (the N <-> 2-N symmetry for odd N: (-q^-1)^{N-1} = q^{(2-N)-1}).
 DICTIONARY:  sl_2 colour 2 at t  =  SO(3) at q3 = t^-1  =  OSp(1|2) fundamental at q = -t.   With t = -e^h:  q = e^h.
 So t = -1 is the CLASSICAL point q = 1 of OSp(1|2): (a, z) = (1, 0), the colour-2 braiding is symmetric (R = R^-1), kinks are free,
 and the loop is -1 = sdim(1|2). At t = -1 the colour-2 skein category is the Brauer category Br(-1) (classical osp(1|2), V = C^{1|2}).
 Further matches (PROVED, elementary): (i) R_22 = P_s exp(-h T), P_s = diag(+1,+1,-1) = the SUPER flip of C^{1|2} (+1 on
 S^2_super V = R_0 + R_{1/2}, dim 4 = 1+3; -1 on Lambda^2_super V = R_1, dim 5), T = diag(-2,-1,1) = 2(C(R_j) - 2C(V)) with the osp(1|2)
 Casimir C(R_j) = j(j+1/2) (R_0, R_{1/2}, R_1: 0, 1/2, 3/2). (The ORDINARY flip of C^3 would be +1 on dims 1+5 and -1 on dim 3:
 the colour-2 R-matrix at t = -1 is the super flip, not the flip.) (ii) Twists for all integer spins: sl_2 colour 2m at t = -q has
 theta_{2m} = A^{4m(m+1)} = t^{-m(m+1)} = q^{-m(m+1)} = q^{-4 C(R_{m/2})}, the osp(1|2) twist of R_{m/2} in the same normalisation.
 (iii) Quantum dims: Delta_{2m}(t) = sum_{k=-m..m} t^k = sum_k (-1)^k q^k -> (-1)^m = sdim R_{m/2} (top sl_2-summand of parity m).
 Literature for the correspondence osp(1|2)_q <-> so(3)_{-q} (MEMORY, not re-read here): Saleur; Ennes-Ramadevi-Ramallo-Sarkar;
 Blumen; Clark-Wang (covering quantum groups). Convention caveat: many papers write the osp parameter as q^{1/2} of ours; the
 Dubrovnik parameters above fix our normalisation unambiguously.
1.3 Knots: the colour-2 coloured Jones J_3(K) at t = -1.
 PROPOSITION 1.3 (PROVED). For every knot K, J_3(K)(-1) = 1, and J_3(K)(-e^h) = sum_n c_n(K) h^n with c_n a Vassiliev invariant of
 order <= n. (J_3 normalised by the unknot and by the writhe: J_3 = (A^8)^{-w} (<K^(2)> - 1)/Delta_2, KL <O> = delta.)
 Proof. (a) Value: by Lemma 1.1 a crossing change of the colour-2 knot costs z(1 - E) with z = 2 sinh h, and every colour-2 diagram
 evaluates to a Laurent polynomial in A (a colour-2 component with one f_2 equals its 2-cable minus the diagram without it: the
 e-closure of a 2-cable bounds an embedded disc, is a split 0-framed unknot and contributes delta, cancelling delta^-1 in f_2;
 this is the Chebyshev identity S_2(x) = x^2 - 1). So at h = 0 crossings are free and kinks cost A_0^8 = 1: K evaluates as the
 unknot. (b) Finite type: m crossing changes give z^m times a sum of values of colour-2 links, all regular at h = 0, so the
 alternating sum is O(h^m). Independent confirmation (KNOWN): Habiro's cyclotomic expansion J_3 = sum_k C_k(K;q)(q^4;q)_k(q^-2;q)_k
 at q = -1: every k >= 1 term vanishes (factor 1 - q^4). QED
 Remark. This is special to even colours: for colour 1 (the Jones polynomial) R - R^-1 = (A - A^-1)(1 - e) and A_0 - A_0^-1 = i sqrt2
 != 0, so V_K(-1) = +-det(K) and the Jones polynomial has no finite-type expansion at t = -1.
 CHECKED(7 knots, 8 diagrams; j3knots.py, 2-cable sweeps of braid closures):
     J_3(K)(-e^h) = 1 + 0.h - 24 a_2(K) h^2 - 144 v_3(K) h^3 + O(h^4)      (v_3 := -(V'''(1)+3V''(1))/36 as in BRIEF F3)
 on 3_1 (also a stabilised braid), 3_1 mirror, 4_1, 5_1, 5_2, 6_1, 3_1#3_1. h^4-coefficients: 3_1: -508, 4_1: 124, 5_1: -4308,
 5_2: -2264, 6_1: 728, 3_1#3_1: -440 (= 576 - 2.508, multiplicativity). Given Prop 1.3 the h^2 and h^3 identities are PROVED:
 order-2 (order-3) knot invariants are spanned by 1, a_2 (and v_3) [KNOWN], and the coefficients are fixed by 3_1, 4_1.
 COMPARISON with the equivariant J: [h^2] J(K,h)(-e^h) = M_2/2 = -12 a_2(K) = (1/2) [h^2] J_3(K). (Heuristic: the quotient arc is
 "half of K".) At order 3: J^2 = J_3(K) + O(h^4) would force M_3/36 = 12 v_3(K) in the F3 convention, i.e. iota = v_3(K). This holds
 EXACTLY on local-knot inversions (3.2: there J = J_3(L) and J_3(K) = J_3(L)^2), but BRIEF F3 has iota != v_3(K) in general (e.g. iota = 1
 with v_3 = 0). So J is not a square root of J_3(K) beyond order 2; the defect iota - v_3(K) is the equivariant part of M_3.

## 2. Part (2): the axis, and a PROOF of THEOREM FT

2.1 LEMMA (on-axis relation; PROVED). Yhat := x0 = positive full twist of the colour-2 arc around the colour-1 axis acts on
 End(V_1 (x) V_2) = C P_1 + C P_3 by t^2 P_1 + t^-1 P_3 (theta_c/(theta_1 theta_2)). Hence
     Yhat - Yhat^-1 = z [ -(A^4+A^-4) P_1 + P_3 ],          z = A^4 - A^-4,
     Yhat - t^4 Yhat^-1 = (1 + t^3)(Yhat - t^2)     (integral; check on both channels),
 and in TH-2BR normalisation rho(Y) = Yhat/t^2 (eigenvalues 1, t^-3): rho(Y) - rho(Y)^-1 = (1 + t^3)(rho(Y) - 1).
 At h = 0: Yhat = P_1 - P_3 =: sigma, an involution, and Yhat - Yhat^-1 = z (3 + sigma)/2 + O(h^2).
 Exact form: Yhat = e^{h/2} sigma exp((3h/2) sigma) (on P_1: e^{2h}; on P_3: -e^{-h}).

2.2 THEOREM FT (BRIEF F2) -- PROVED here (integral skein argument; numerically re-confirmed in 2.4).
 Statement: for m independent flips (any mix of symmetric off-axis pairs x_i<->y_i, i>=1, and on-axis x0<->y0), the alternating sum
 Delta^m J = sum_S (-1)^|S| J_S of the NORMALISED J is divisible by (t+1)^m in Z[t,1/t]. Equivalently M_k has order <= k.
 Proof. Let D be the quotient diagram (axis = vertical line, arc = colour-2 band) and E(D) := <Theta_D; 1,1,2>/Delta_2, the
 blackboard evaluation; E(D) = (unit) * J and E(D) lies in Z[A,1/A] (BRIEF 0 / proof REPORT 0.2: <Theta> = mu^f Delta_2 y).
 (i) Multilinearity. The m sites are disjoint discs; E(D_S) is multilinear in the local skein elements at the sites.
 (ii) Local relations, each = (1+t) x (integral element):
   off-axis (one colour-2 crossing c of the quotient):  R_22 - R_22^-1 = z (1 - E)  (Lemma 1.1), z = (1-t)(1+t)/t;
   on-axis (one full twist):  Yhat - t^4 Yhat^-1 = (1 + t^3)(Yhat - t^2)  (Lemma 2.1; the unit t^4 is absorbed in (iv)).
 (iii) Integrality of the resulting networks. Expanding all sites gives networks W = (a theta-curve with colour-2 arc) u (closed
   colour-2 loops), possibly with some full twists removed. Each colour-2 loop (one f_2 after merging; f_2 slides along bands and
   through crossings) expands as (its 2-cable) - (W without it): the e-term of f_2 = 1 - delta^-1 e closes the 2-cable into the
   boundary of the cut framing annulus, an unknot bounding an embedded disc disjoint from everything, 0-framed (the four crossings at
   each band self-crossing have total writhe 0), so it contributes delta. The remaining theta-curve with plain closed curves has
   <.> = mu Delta_2 y' with y' its y-coefficient in Z[A,1/A]. Hence E(W) is in Z[A,1/A].
   So Delta^m Etilde := sum_S (-1)^|S| (t^4)^{#on-axis flips in S} E(D_S) = z^p (1+t^3)^r (integral) is in (1+t)^m Z[A,1/A].
 (iv) Normalisation. Put A = e^{i pi/4 - h/4}. From (iii) for every sub-family of sites: Delta^T Etilde = O(h^|T|). So
   c_0 := Etilde_S(0) is independent of S, and Etilde'_S(0) is affine in S. The normalised J_S = u_S A^{n_S} Etilde_S (u_S = +-1)
   with J_S(0) = 1, J_S'(0) = 0 forces n_S = 4 Etilde'_S(0)/c_0 (affine in S) and J_S(h) = e^{-n_S h/4} Etilde_S(h)/c_0.
   A product of a multiplicative-affine factor prod_i f_i^{S_i} (f_i = 1 + O(h)) with an order-filtered family keeps Delta^m = O(h^m)
   (Leibniz: each difference either hits Etilde or produces a factor 1 - f_i = O(h)). So Delta^m J = O(h^m).
 (v) Delta^m J is in Z[t,1/t] and vanishes to order m at t = -1; since 1+t is monic, (1+t)^m divides it in Z[t,1/t] (Gauss). QED
 COROLLARY 2.2a (PROVED; explains BRIEF's on-axis-only observation). If all m flips are on-axis, Delta^m J = O(h^{m+1}), i.e.
   Delta^m M_m = 0. Reason: with no off-axis site there are no smoothings, so at h = 0 every on-axis difference z(3+sigma)/2 acts on
   the ARC, where sigma acts as 1 (2.3(d)); each site's leading term is the scalar 2z, the leading part of Delta^T Etilde is
   multiplicative, c_0 prod_{i in T} l_i, and (iv) gives leading coefficient c_0^{-1} sum_T prod_{i in T}(-l_i) prod_{i notin T} l_i
   = prod_i (l_i - l_i) = 0 (the normalisation exponents are d_i = 4 l_i). This is the "isolated chord" (1T) mechanism.
 Scope remark. This is the standard Birman-Lin argument transplanted to t = -1; the only inputs are Lemma 1.1, Lemma 2.1 and the
 integrality (iii). The caveat in BRIEF F2 (f_2 and theta-values singular at delta = 0) is avoided because f_2 never appears
 unmerged: every network in (iii) has exactly one f_2 per colour-2 component, and those are integral.

2.3 The axis at h = 0 is a PARITY DEFECT for the classical osp(1|2) arc (all items PROVED, elementary; (e) CHECKED).
 Dictionary: V = C^{1|2} on the arc; P_1 <-> projection onto the even line V_0 (the unique sl_2-invariant vector e_0, sl_2 =
 osp(1|2)_even = fixed algebra of the parity automorphism), P_3 <-> projection onto the odd plane V_1; sigma = Yhat|_{h=0} = P_1 - P_3
 <-> (-1)^F. Evidence that this is forced, not a choice:
 (a) Box ring at t = -1: R = {(a,b): a = b mod (1 - t^3)} becomes {(a,b): a = b mod 2} = Z[Z/2] (basis 1 = (1,1), sigma = (1,-1));
     the Y-box (1, t^-3) becomes (1,-1) = sigma. The box state space is End_{sl_2}(V) = C e_+ + C e_- (2-dim, as required).
 (b) Channel dimensions: Delta_1 = delta and Delta_3 = -[4] both vanish at h = 0, but Delta_3/Delta_1 = t + t^-1 -> -2. So after
     dividing by the vanishing axis dimension, (P_1, P_3) have dimensions (1, -2) = (sdim V_0, sdim V_1); sum -1 = sdim V = Delta_2(-1).
 (c) Loops: a colour-2m loop around the axis, normalised by the axis, is the Hopf ratio [2(2m+1)]/[2] -> 2m+1 at q = A^2 = i, which
     is str_{R_{m/2}}((-1)^F) = ordinary dim R_{m/2}; an unlinked colour-2m loop gives Delta_{2m} -> (-1)^m = str(1) = sdim R_{m/2}.
     (m = 1: 3 versus -1.)
 (d) Junctions: the vertex fuses axis+arc into colour 1, i.e. sees only P_1: the arc ends in e_0 (even), so sigma acts as +1 on the
     arc: e_1^T sigma = e_1^T (TH-2BR: at t = -1, X = I and Y = [[1,0],[-1,-1]] with e_1^T Y = e_1^T).
 (e) PROPOSITION 2.3 (h = 0 evaluation; PROVED). At A_0 every network W of 2.2(iii) evaluates to c_0 prod_{loops} w(loop), where
     w = -1 for even winding around the axis and w = 3 for odd winding, and c_0 = E(D)(A_0). Proof: at A_0 colour-2 crossings and
     kinks are free (z = 0, a = 1) and Yhat^2 = 1, so components move by homotopy in the solid torus S^3 - axis modulo even windings;
     a loop is homotopic to an unlinked loop or a meridian of the axis (values Delta_2 = -1, Hopf ratio 3); a winding of the arc slides
     along the arc (pi_1 of the solid torus is abelian) to a vertex, where it acts as +1 by (d). QED
     COROLLARY (top-order formula). For m flipped sites, [h^m] Delta^m E = 2^m c_0 Sigma, where Sigma is the state sum: off-axis site
     -> eps (vertical - horizontal), on-axis site -> eps ((3/2) unwound + (1/2) wound), unflipped crossings -> swap, unflipped x0/y0
     -> wound; loops weighted -1 / 3 as above; eps = +1 if the site's letter is x, -1 if y. (z = 2 sinh h; on-axis: (Yhat - Yhat^-1)/z ->
     2P_1 + P_3 = (3 + sigma)/2.) This is the classical osp(1|2) (Brauer(-1)) evaluation with a Z/2 branch line.

2.4 Numerical confirmation (ftraw.py, ftraw_sens.py; raw plain-bracket y-coefficients of flat_search, no normalisation at all).
 For random half-words and m = 1..4 random flip sites: D := sum_S (-1)^|S| y_S is divisible by (1+A^4)^m (in fact by z^m), and
 D/(1+A^4)^m at A_0 equals 2^m y_0(A_0) Sigma exactly in Z[zeta_8]:
   CHECKED(40 off-axis + 40 on-axis + 40 mixed = 120): 120/120 divisible, 120/120 state-sum match.
 Sensitivity (40 further mixed samples, m = 2..4, Sigma ranging over -32..16, never 0): replacing the odd-winding loop weight 3 by -1 or
 by 1 fails in 24/40; replacing the on-axis weights (3/2, 1/2) by (1, 1) fails in 19/40. So the values str((-1)^F) = 3 and
 (3 + sigma)/2 are detected, not fitted.

2.5 Perturbative osp(1|2) series: what holds and the precise obstruction.
 Exact (non-perturbative) presentation, PROVED: J(t) is the evaluation of Theta in the skein theory where the arc obeys the OSp(1|2)
 Dubrovnik relations at q = -t (Lemma 1.1 + 1.2), the arc's full twist around the axis obeys (rho(Y) - 1)(rho(Y) + q^-3) = 0
 (eigenvalues 1, t^-3 = -q^-3), and the vertices project onto the rho(Y) = 1 channel. At q = 1: Brauer(-1) + sigma^2 = 1 + even junctions.
 Expansion data, PROVED: R_22 = P_s exp(-h T) (T = 4 t_osp on V (x) V, Casimir C(R_j) = j(j+1/2)); Yhat = e^{h/2} sigma exp((3h/2) sigma).
 So arc-arc chords carry the osp(1|2) Casimir tensor and on-axis chords carry the PARITY operator sigma (mod framing scalars).
 CONJECTURE (Lie-theoretic reading of the on-axis chord). sigma-part of the on-axis chord = -2 x (pi-twisted Casimir mu(1 (x) pi) t_osp =
 C_0 - C_1 on V), pi = parity automorphism: with C_0 = s(s+1) on sl_2-spin s, C_0 - C_1 = 1/4 - (3/4) sigma on V, and -2(-3/4) = 3/2
 matches the TL value; i.e. an on-axis chord {p, h(p)} upstairs is a "twisted chord" whose two ends coincide in the quotient.
 (Normalisation of the sl_2 part of the osp Casimir assumed from memory: C(R_j) = j(j+1/2) = C_0 - j/2 on the top sl_2-summand.)
 OBSTRUCTION to a naive osp(1|2) Vassiliev series of Theta (precise): the axis is not an osp(1|2)-module line. It is the
 half-integer-spin ("twisted sector") line of sl_2 = (integer spins = Rep OSp(1|2) at q = -t) + (half-integer spins); (i) its quantum
 dimension vanishes at h = 0 (all odd colours have [even]_{q=i} = 0), so it can only appear with the vertex normalisation
 theta(1,1,2) = Delta_2; (ii) at h != 0 it is not a symmetry defect: the double-braiding eigenvalue ratio is -q^-3, not -1; the
 correction exp((3h/2) sigma) has to be carried by sigma-insertions (on-axis chords). A full formula J(-e^h) = W(Z(Theta)) needs a
 Kontsevich integral of theta-curves with a Z/2 branch line (equivalently a Z/2-equivariant Kontsevich integral upstairs): GAP. What is
 proved instead is the order-by-order statement (Theorem FT + the top-order formula 2.3(e)), which is all the weight system needs.

## 3. Part (3): weight system of the J-tower; abelian diagonal question

3.1 The weight system (PROVED, from 2.2 + 2.3(e)). For an equivariant chord diagram D of order m (m flip sites: symmetric off-axis
 pairs and on-axis chords), the raw top-order weight is W_raw(D) = 2^m Sigma(D) (classical osp(1|2) = Brauer(-1) state sum with the
 axis as a Z/2 branch line: loops -1 / 3, on-axis sites (3 + sigma)/2). The weight system of the normalised J is its framing-
 independent (1T) projection, obtained from step (iv) of 2.2 by expanding e^{-b_S h} (b_S affine, b_i = -2 Sigma_i): each site either
 contributes its state-sum term or the framing factor -Sigma_i. Single sites have Sigma_i = +-2 (off-axis: one smoothing makes a loop
 of weight -1 or 3, the other none; on-axis: (3+1)/2 = 2), so every single flip shifts the normalising power of t.
 Explicitly (lp convention): [h^m] Delta^m J = (-2)^m sum_{T subset sites} prod_{i in T} (-Sigma_i) Sigma(sites minus T), Sigma_i := Sigma({i}).
 CHECKED(120; wjnorm.py, seeds 3 and 11, m = 2..4, normalised J from lp.J, top-order term nonzero in 49 of them): 120/120 exact.
 On-axis chords alone give 0 (Cor 2.2a); an on-axis chord interacts with off-axis chords only through loops created by their
 smoothings that pass the on-axis site (sigma acts as -1 on odd-winding loops). So: the J-tower weight system is the osp(1|2)
 fundamental weight system on the quotient arc, twisted by the parity automorphism along the axis (equivalently: Kauffman/so(N)
 weight system at N = -1 with a Z/2 holonomy). It is NOT the sl_2 (colour-1) weight system: colour 1 has no expansion at t = -1.
 Comparison numbers (knots, J_3; CHECKED on 3_1): at t = +1 (so(3) = sl_2 adjoint): J_3(e^h) = 1 - 8 a_2 h^2 - 16 v_3 h^3 + ...;
 at t = -1 (osp(1|2)): J_3(-e^h) = 1 - 24 a_2 h^2 - 144 v_3 h^3 + ... (section 1.3). Different weight systems, both non-abelian.

3.2 LOCAL KNOTS (PROPOSITION; PROVED by Schur's lemma, CHECKED 3/3 exact). Let L be any knot and (K,h) = (L # rL, swap): tie L in a
 small ball B on the trivial strongly invertible unknot away from the axis and h(L) in h(B) (h reverses the orientation of K, so the
 second summand is rL). In the quotient, the arc carries the local knot L. The skein space of a ball meeting Theta in one colour-2
 arc is End(V_2) = C, so the local knot is the scalar J_3(L) (normalised). Hence
       J(L # rL, swap) = J_3(L)   (exactly, in one common convention; lp.J returns J_3(L)(1/t) because lp uses t = A^{+4}).
 CHECKED (localknot.py): s.l1.x2^3.u1, s.l1.y2^3.u1, s.l1.x2^5.u1 give exactly J_3(3_1)(1/t), J_3(3_1*)(1/t), J_3(5_1)(1/t).
 Consequences:
 (a) The J-tower contains the full osp(1|2) Vassiliev series of EVERY knot L (J_3 at t = -1). In particular [h^2]: -12 a_2(K) with
     a_2(K) = 2 a_2(L) (consistent with M_2 = -24 a_2(K)), and M_3/36 = 12 v_3(K) on these inversions (F3 convention; v_3(K) = 2 v_3(L)), i.e. in the
     notation of BRIEF F3, iota = v_3(K) on local-knot inversions. Rewriting F3: M_3/36 = 12 v_3(K) + 5 (iota - v_3(K)), where the
     equivariant defect iota - v_3(K) vanishes on local-knot inversions. (Not a combination of v_3(K), v_3(K_1), v_3(K_2) for the
     constituent knots K_i = arc u axis-edge_i: best small-integer fit matches only 81/150 rows of ident3_rows.json; constit.py.)
 (b) GENUINELY NON-ABELIAN (answers the dichotomy). Take L = Wh(3_1), the untwisted Whitehead double of the trefoil (whdouble.py:
     a_2(L) = 0 as computed, Delta_L = 1 KNOWN for untwisted doubles). Then K = L # rL has Delta_K = 1 (so a_2(K) = 0: the a_2 = 0 core),
     both constituent knots are L (Delta = 1), so every invariant determined by the Alexander modules / Seifert forms of K and of its
     constituents is that of the unknot; but
        J(K,h) = J_3(Wh(3_1)) != 1,   J_3(Wh(3_1))(-e^h) = 1 + 0 h - 0 h^2 - 288 h^3 - 864 h^4 + 13536 h^5 + ...   (= -144 v_3(L) h^3, v_3(L) = 2).
     So J is not a function of Alexander-type invariants of K and its constituents. Sakuma's eta: CONJECTURE (not verified here) that
     eta vanishes on local-knot inversions (local knots do not change linking numbers of lifts in the Kojima-Yamasaki construction);
     if so, this (K,h) has ALL standard abelian invariants trivial while J != 1, detected at order 3 (M_3 = +-1728).
 (c) REDUCTION (PROVED): Lemma Q restricted to local-knot inversions is EQUIVALENT to "J_3 detects the unknot" (J_3(L) = 1 => L = O),
     since J = J_3(L) is a unit iff J_3(L) = 1 (J_3 = 1 mod (t+1)^2 by Prop 1.3) and L # rL = O iff L = O. So the a_2 = 0 core of
     Lemma Q contains the spin-1 coloured-Jones unknot problem for all knots with a_2 = 0 (e.g. all Delta = 1 knots). Combined with
     BRIEF's JC => Lemma Q, this gives JC => (J_3 detects the unknot) via the branch sets of L # rL. Whether this is known / open is for
     the LIT lane (MEMORY: I know of no proof that J_3 detects the unknot).

3.3 Abelian diagonal (MMR-type question).
 - Order 2 is abelian: [h^2] J(-e^h) = -12 a_2(K) = (1/2)[h^2] J_3(K)(-e^h) (Conway coefficient; KNOWN/PROVED in BRIEF).
 - From order 3 on the tower is non-abelian by 3.2(b): it contains v_3 of local knots, a 2-loop invariant (odd wheels vanish by AS, so
   the degree-3 primitive part for knots is 2-loop; Alexander-type = 1-loop/wheels data cannot produce it).
 - A genuine MMR "diagonal" needs a colour parameter, which a single J lacks. The natural family is the arc colour 2m (osp(1|2) R_{m/2}),
   J^(m)(K,h) = <Theta; 1,1,2m>/<Theta_0>; FT should extend (all even colours are classical at t = -1). Question (OPEN, not computed):
   is sum_k a_kk (m h)^k an Alexander-type invariant of (K,h) (of K, the constituents, or eta)? Even if yes, 3.2(b) shows the off-diagonal
   terms carry non-abelian information, so the dichotomy in the task resolves on the non-abelian side.


## 4. Scripts and checks (all in this folder; run with tools/venv/bin/python; each runs in seconds to ~2 minutes)
- j3knots.py: J_3 of braid closures by 2-cable sweeps (KL, t = A^-4); expansions at t = -1 (section 1.3).
- ftraw.py SEED N {off|axis|mixed}: raw y alternating sums, divisibility by (1+A^4)^m and z^m, h = 0 state sum (2.3(e), 2.4).
- ftraw_sens.py SEED N: sensitivity of the state-sum model to wrong loop / on-axis weights (2.4).
- wjnorm.py SEED N: normalised top-order weight system versus lp.J moments (3.1).
- localknot.py: J(L # rL, swap) = J_3(L) for L = 3_1, 3_1*, 5_1 (3.2).
- whdouble.py: untwisted Whitehead double of 3_1: V, a_2 = 0, J_3 and its expansion (3.2(b)).
- constit.py: constituent knots K_1, K_2 of the quotient theta-curve; test of iota against their v_3 (3.2(a)).

## 5. Summary of claims
- Dictionary sl_2 colour 2 at t = SO(3) at q3 = t^-1 = OSp(1|2) fundamental (1|2) at q = -t (Dubrovnik parameters match exactly;
  R_22 = P_super exp(-hT), theta_2 = q^-2, Delta_2 -> -1 = sdim). PROVED (osp side KNOWN-MEMORY).
- J_3(K)(-1) = 1 for all knots, finite-type expansion at t = -1; J_3(-e^h) = 1 - 24 a_2 h^2 - 144 v_3 h^3 + O(h^4). PROVED (+CHECKED 7 knots).
- THEOREM FT (BRIEF F2): Delta^m J divisible by (t+1)^m for any m equivariant flips. PROVED (integral skein argument, 2.2);
  raw-level confirmation CHECKED(120); on-axis-only sums vanish one order further (Cor 2.2a) PROVED.
- Axis at h = 0 = Z/2 parity defect: full twist = sigma = (-1)^F up to the scalar e^{h/2} and exp((3h/2) sigma); box ring -> Z[Z/2];
  loops around the axis -> str((-1)^F) = 3 (generally 2m+1); junction = even line. PROVED; state-sum model CHECKED(120 + 40 sensitivity).
- Top-order weight system = twisted classical osp(1|2) (Brauer(-1)) state sum, with explicit 1T-projection formula. PROVED; CHECKED(120).
- Full perturbative formula via a Kontsevich integral with a Z/2 branch line: GAP. Obstruction: axis = twisted-sector line
  (zero quantum dimension; double braiding ratio -q^-3, not -1). On-axis chord = pi-twisted Casimir: CONJECTURE (normalisation from memory).
- Local knots: J(L # rL, swap) = J_3(L). PROVED (Schur) + CHECKED(3). Hence: tower contains the osp(1|2) series of every knot;
  iota = v_3(K) on these (F3 convention); Lemma Q on this class <=> J_3 detects the unknot (reduction PROVED).
- Non-abelian: (Wh(3_1) # r Wh(3_1), swap) has Delta_K = 1, constituents with Delta = 1, but J = J_3(Wh(3_1)) != 1 (order 3). CHECKED.
  Sakuma's eta vanishing on local-knot inversions: CONJECTURE (not verified).
- iota - v_3(K) is not a small-integer combination of v_3(K), v_3(K_1), v_3(K_2): CHECKED (best fit 81/150).
- MMR diagonal for the arc-colour family 2m: OPEN (not computed).
