# BRIEF: the a_2 = 0 core of Lemma Q, and finite-type theory of J at t = -1
(16 Nov 2026, Claude integrator. Read completely before working. Earlier background: ../BRIEF.md (necklace calculus).)

## 0. Logical position (what we are and are not attacking)
- (K,h): strongly invertible knot. Quotient theta-curve Theta = A u k (A = image of the axis, an unknot; k = K/h, an arc
  joining the two fixed points). Quotient tangle T = (S^3 - N(k), A - N(k)), with T(1/0) = unknot (Watson's bijection).
- J = J(K,h) in Lambda = Z[t,1/t]: the Q_0-coefficient y of the plain Kauffman bracket [T] = y[Q_0] + x[Q_inf], equivalently
  <Theta; axis colour 1, arc colour 2> / <trivial theta>, normalised by J = 1 mod (t+1)^2 (unique signed power of t).
  (Proof of the equivalence: ../proof/REPORT.md section 0.2.) J is computed exactly by ../lp.py: lp.J(halfword).
- LEMMA Q: J unit => K unknot.  JC (Jones unknot conjecture) => Lemma Q (Gordon-Luecke); the converse is unknown
  (Sikora, Canad. J. Math 2024, Thm 9.2: JC <=> the bracket detects rational tangles among ALL tangles; Lemma Q is the
  restriction to tangles with an unknotted closure). Full Lemma Q gives Jones detection for the branch sets L_n = T(1/n)
  (Sigma_2(L_n) = S^3_{1/n}(K)) for every even n != 0 (this includes all unknotting-number-one knots, n = +-2) and for odd n
  when a_2(K) = 0 (see 1.3).
- Lemma Q is AUTOMATIC when a_2(K) != 0: a unit J with J = 1 mod (t+1)^2 must equal 1, and J''(-1) = -24 a_2(K).
  So the open content is the a_2 = 0 CORE. That is this round's target, and we want CLASS-FREE theory.
- Already proved classes (do not redo): two-bridge (TH-2BR, Astra+Claude); horizontal inversions of Montesinos knots
  N(T_1+...+T_n+1/(2mu)), n >= 2 genuine odd rational tangles (Q-MONT: ../notie/REPORT.md, refereed by Astra). This class
  contains the a_2 = 0 family P(2k,4k-1,4k+1), k >= 1 (a_2(P(2mu,r,s)) = (r^2+s^2-2)/8 - mu(r+s)/2); P(2,3,5) has preferred
  J = t^-12 (t^4-3t^3+3t^2-t-2+5t^-1-4t^-2+t^-3+2t^-4-2t^-5+t^-6).
- Counterexample construction stays PAUSED (Caleb's instruction): no geography scans, no searches for J = 1.

## 1. Conventions and facts
1.1 Half-words (../BRIEF.md, ../words.py, ../../tools/alex.py). Letters: s (start), r_i/l_i caps, u_i cups, x_i/y_i crossings.
    x_i, y_i with i >= 1: a crossing between half-strands i-1, i, mirrored on the other side: flipping x_i <-> y_i is a
    SYMMETRIC PAIR of crossing changes of K off the axis; in the quotient it is ONE arc-arc crossing change (colour 2 x 2).
    x0, y0: a single crossing of K ON the axis; in the quotient a full twist of the arc around the axis; flipping x0 <-> y0 is
    an ON-AXIS crossing change (quotient: full twist of colour 2 around colour 1 replaced by its inverse).
    Flips keep K a knot and keep the inversion; lp.J of the flipped word is J of the new (K,h).
    TH-2BR matrices (2-dim state space at a sphere meeting axis twice and arc twice): Y = [[1,0],[t^-3,t^-3]] (y0-type),
    X = [[1,1-t^4],[0,-t]] (y1-type arc-arc). At t = -1: X = I and Y is an involution.
1.2 MOMENTS. M_k(K,h) := sum_e J_e (-1)^e e^k = k! [h^k] J(-e^h).  M_0 = 1, M_1 = 0 (normalisation),
    M_2 = J''(-1) = -24 a_2(K) (PROVED via Mullins + Casson; CHECKED 150/150 against a_2 of K from its Jones polynomial).
    Mirror (K,h) -> (K*,h): J(t) -> J(1/t), so M_k -> (-1)^k M_k (M_odd are chirality-odd).
1.3 Branch-set closure formula (letter 63; Astra-refereed scope): with G := (J-1)/(1+t)^2 in Lambda,
       V(T(1/n)) = t^{12 j [n odd]} { 1 + (1 - (-t)^{-n}) Phi_3 G },   Phi_3 = 1+t+t^2,  j = -sigma(L_n)/8 for odd n.
    For even n (or j = 0), V(L_n) = 1 <=> J = 1. For odd n with j != 0 the inference needs more (Astra's formal
    counterexample J_*). If V(L_n) = 1 then Mullins gives sigma(L_n) = 8 lambda(S^3_{1/n}(K)) = +-8 n a_2(K); so in the
    a_2 = 0 core j = 0 and V(L_n) = 1 <=> J = 1 for every n != 0.

## 2. New facts this round (status as marked)
F1 ROOTS (PROVED from 1.3 + classical evaluations; CHECKED 80/80): J(1) = J(i) = J(e^{i pi/3}) = 1 for every (K,h).
   Reason: L_1, L_2 are det-1 knots, so V(1) = 1, V(i) = (-1)^Arf, V(e^{i pi/3}) = +-1 (Lickorish-Millett, H_1(Sigma_2;Z/3) = 0);
   insert in 1.3 (the unit t^{12j} is 1 at these points): n = 1 and n = 2 force G(i) = 0; n = 1 forces G(e^{i pi/3}) = 0
   (the other option is not an algebraic integer); V(L_1)(1) = 1 forces G(1) = 0.
   Hence J - 1 is divisible by (t+1)^2 (t-1)(t^2+1)(t^2-t+1) (degree 7), and by (t+1)^3 (t-1)(t^2+1)(t^2-t+1) when a_2 = 0.
F2 THEOREM FT (CONJECTURE, strong evidence): M_k is an equivariant finite-type invariant of order <= k with respect to
   equivariant crossing changes (symmetric off-axis pairs and on-axis crossings). Equivalently: for m independent flips,
   the alternating sum Delta^m J = sum_S (-1)^{|S|} J_S is divisible by (t+1)^m.
   Evidence (scripts check_ft.py, check_ft2.py in this folder): Delta^m M_k = 0 for every m > k in all samples
   (mixed flips: 80 samples, m = 3..6, k = 0..6; off-axis only: 40; on-axis only: 40), 0 failures. The non-automatic cases are
   (m,k) = (4,3), (5,4), (6,5). Order is attained: Delta^m M_m != 0 in about 40% of off-axis samples. On-axis-only sums vanish
   even at m = k (consistent with the one-term relation: on-axis chords {p, h(p)} on K are mutually parallel, hence isolated).
   Heuristic mechanism: at t = -1 (A^4 = -1, delta = 0, [2] = 0) the half twist of two colour-2 strands has eigenvalues
   A^-8, -A^-4, A^4 on channels 0, 2, 4, i.e. 1, 1, -1: self-inverse, so R - R^-1 = O(t+1). The full twist of colour 1 around
   colour 2 has eigenvalues t^2, t^-1 on channels 1, 3, i.e. 1, -1: self-inverse. CAVEAT: at delta = 0 the projector f_2 and
   several theta-values are singular, so a proof needs an integral local model (the plain-bracket y-coefficient picture of
   the quotient tangle, or Astra's projected-TL_3 integrality argument from the necklace referee) and coherent framing units.
   Conceptual guess (CONJECTURE): the colour-2 R-matrix at t = -1 is +1 on channels 0+2 (dim 4) and -1 on channel 4 (dim 5),
   which is the super flip of a (1|2)-dimensional super space. Under the known correspondence between U_q(osp(1|2)) and
   U_{-q}(so(3)) (3-dim reps matched; e.g. Blumen; Clark-Wang; Ennes-Ramadevi-Ramallo-Sarkar), sl_2 colour 2 at t = -1 is
   so(3) at q = -1, hence osp(1|2) at its CLASSICAL point q = 1. The axis (colour 1, quantum dimension 0 at t = -1) would act as
   a parity defect: a full twist around it acts by +-1 = (-1)^F. If right, J(-e^h) is an osp(1|2) Vassiliev series of the
   quotient theta-curve with a parity-twisted weight system. This would explain F2 and give its weight system.
F3 IDENTIFICATION DATA (ident3.py, ident3_rows.json: word, M_2, M_3, M_4, a_2(K), w_3(K) for 150 random (K,h)):
   with v_3 := -(V_K'''(1) + 3 V_K''(1))/36 (an integer, chirality-odd, order 3), M_3/36 is an integer and
   M_3/36 = 7 v_3(K) + 5 iota with iota an INTEGER in every sample, iota not determined by K: e.g. iota = 1 with v_3 = 0
   (s.l1.y0.l3.x4.x2.y1.u3.x0.x1.u1, a_2 = -1), iota = 0 in about 20% of samples. So M_3 has a genuinely equivariant part.
   M_4 not yet analysed.

## 3. Tools
- Python: /Users/calebbarnett/jones-lanes/theory-restart/tools/venv/bin/python. Exact Laurent polys are {exp: coeff} dicts.
- ../lp.py: J(word), J_raw, normalize, a2, poly helpers (add, mul, sub, shift, ev, ...), TH-2BR matrices and star product.
- ../../tools/flat_search.py: gen(rnd, L) random half-words; bracket_vector(half) gives (y, x).
- ../../tools/kauffman.py: bracket(word) = Kauffman bracket (in A) of the FULL symmetric diagram of K; ident3.py shows how to
  turn it into V_K (t = A^-4, normalise V(1) = 1, V'(1) = 0).
- ../../tools/alex.py: parse, symmetrize, diagram, Alexander polynomial machinery.
- ../words.py: mont(m, rows) builds Montesinos words (e.g. mont(1,[3,7]) = P(-2,3,7)).
- This folder: check_ft.py, check_ft2.py (alternating-sum tests), ident3.py (moments vs Vassiliev invariants of K).
- lp.J takes milliseconds; a 2^5 alternating sum takes well under a second.

## 4. Ground rules
- Theory first: definitions, statements WITH reasons, proofs or precise obstructions. Compute only to sanity-check a
  definition or to identify a formula you then try to prove (minutes, not hours). No geography scans, no J = 1 searches.
- Write REPORT.md in your lane folder CONTINUOUSLY (skeleton in the first minutes, update after each step).
- Mark every claim PROVED / CHECKED(n) / CONJECTURE / GAP / KNOWN. Never claim novelty: the LIT lane decides that.
- Do not edit files outside your lane folder (copy shared scripts if you need to change them). No outside contact.

## UPDATE 21:25 (Astra 20261116-212109-codex; Claude read)
- THEOREM FT is PROVED (Astra; local certificate rerun by Claude, all identities True; global argument read step by step).
  Model: t = q^2 = -e^h, s^2 = [2] = ih + O(h^3), lattice on V_2: E w_1 = s w_0, E w_2 = s w_1, F w_0 = s w_1, F w_1 = s w_2.
  B_22 is regular and equals the SUPER FLIP at the root (w_1 even, w_0, w_2 odd), so B_22 - B_22^-1 is in h End.
  Mixed full twist T = B_21 B_12 satisfies (T - q^-4)(T - q^2) = 0, so T - T^-1 = (t+1)[T - (t-1+t^-1)].
  Regular vertices i: V_1 -> V_1 x V_2, p: V_1 x V_2 -> V_1 with p i = Id, denominator [3] (unit), never [2].
  Cut the axis: the theta network is a scalar F Id; F(0) = 1 (the connected arc carries w_1 at the root).
  Multilinearity gives Delta^m F in h^m; s -> -s symmetry makes F unramified; J(-e^h) = exp(-f_1 h) F(h) handles the unit.
  Files: Codex workspace work/theory_restart/ft_integral_referee.md, ft_second_referee.md, referee_checks/ft_local.py.
- FT-AXIS (PROVED): an all-on-axis m-fold difference is divisible by (t+1)^(m+1) (principal insertion 3(T_0 - I) kills w_1).
- The off-axis principal insertion C_22 = ((B_22 - B_22^-1)/h)|_0 maps w_1 x w_1 to -2 w_0 x w_2 + 2 w_2 x w_0 (creates odd pairs);
  axis insertions detect parity. This is an explicit noncommutative local tensor system for the weight symbols.
- ROOTS: confirmed. Signatures: det-1 knots have sigma in 8Z, L_{n+2} and L_n differ by one crossing change, so sigma(L_n) is
  CONSTANT on each parity class (0 on even n, -8j on odd n). An odd Jones-unit closure forces j = n a_2 (fixed convention).
- MOMENT-3 (PROVED): with D = (t^4-1)(t^3+1) and H = (J-1)/D in Lambda: H(-1) = a_2(K) and M_3 = 36[2H'(-1) - 7a_2(K)].
  So 36 | M_3 always, 72 | M_3 when a_2 = 0. The fitted iota = [2H'(-1) - 7a_2 - 7v_3]/5: its integrality (H'(-1) = a_2 + v_3
  mod 5) is OPEN and should be EXPLAINED (identify iota), not inferred from samples.
  Calibration: the two inversions of the figure-eight, s.l1.y0.y0.x1.u2 and s.l1.x0.x0.y1.u2, have J_1 = t^-6+t^-3-t^-2+1-t,
  J_2 = J_1(1/t), M_3 = -180, +180, v_3 = 0, so iota = -1, +1.
- log J(-e^h) is primitive (additive under equivariant connected sum); its coefficients have order <= k.
