# COUNTEREXAMPLE BRIEF (overnight 17 Nov 2026; counterexample construction UNPAUSED by Caleb)
Caleb's instruction: approach counterexample checking very intelligently, using our results to build the right kinds of knots;
never keep checking knots that are, for known reasons, not counterexamples. Solve like a mathematician. Do not get lost.

## 0. What a hit would be, and why it matters
- LEMMA Q counterexample: a strongly invertible (K,h) with K NONTRIVIAL and J(K,h) = 1 (preferred normalisation).
  Then for every n != 0 the branch knot L_n = T(1/n) (double cover S^3_{1/n}(K)) is a NONTRIVIAL knot with V(L_n) = 1
  (J = 1 forces a_2(K) = 0, hence j = 0, hence V(L_n) = 1 <=> J = 1; nontrivial by Gordon-Luecke). That disproves the
  Jones unknot conjecture.
- Swap sums: for any knot K', (K' # rK', swap) has J = J_3(K') (spin-1 coloured Jones; in lp's convention
  J_lp(K'#rK', swap)(t) = J_3(K'; t^-1), a mirror that does not affect unit tests). A nontrivial K' with J_3(K') = 1
  therefore also disproves the conjecture.
- J is computed exactly by /Users/calebbarnett/jones-lanes/theory-restart/mont/lp.py: lp.J(halfword) (milliseconds).

## 1. Necessary conditions for J = 1 (all PROVED; use them to design, rank and prune)
 N1 a_2(K) = 0   (J''(-1) = -24 a_2).                         N2 V_K(omega) = 1 at every primitive 5th root omega
 (MOMENT-CYC10: J_lp(t) = V_K(t^2) mod Phi_10), hence 5 | v_3(K) and 5 | j_4(K).
 N3 J is multiplicative under equivariant connected sum and a compatible sum is flat iff every factor is (TH-J-FACTORS):
    search only equivariantly PRIME configurations.                N4 mirror doubling never manufactures flatness.
 N5 Twist families: at a fixed twist site, J_mu = P + Q(-t)^mu (two channels) or three channels at an arc-pair site;
    only FINITELY many mu can give a unit, with an explicit window (|mu| Delta > 2W, see TWIST-2CH): check the window
    exactly, never sample a family.
 N6 J - 1 is divisible by D_7 = (t^4-1)(t^3+1) always (ROOTS), so J != 1 forces span J >= 4 (= 4 only for trefoils) and
    span J >= 7 when a_2 = 0.
 N7 FT: the t = -1 jet is an osp(1|2) Vassiliev series; FT-DEEP: it can vanish to any finite order on nontrivial
    inversions, so deep vanishing at t = -1 is NOT evidence of global flatness; global (extreme-degree) cancellation is.

## 2. PROVEN-EMPTY regions (never search these)
 - a_2(K) != 0; V_K(zeta_5) != 1.
 - Width one: every halfword s.l1.W.u2 with W in {x0,y0,x1,y1}* (standard two-bridge inversions, TH-2BR).
 - Q-MONT: s.r2.(y1)^m.B_1...B_n.u1 with n >= 2 RATIONAL non-integral boxes B_i, any collected integral part, m != 0
   (and the easy cases m = 0, n <= 1 reduce to products / two-bridge). Torus knots (a_2 > 0). Connected sums of the above.
 - Random half-words of length <= 22 were already scanned (48,665 nontrivial quotients, 0 flat) and 60,000 rational
   necklaces (0 flat): do not repeat blind random scans.

## 3. Where cancellation can still live (targets, in priority order)
 T1 Arborescent inversions OUTSIDE Q-MONT: necklaces whose boxes are themselves necklaces (depth >= 2) or general
    non-rational bodies; general (non-pure-twist) special regions reached by nesting. The nest lane found that nested box
    vectors violate the two-type law (16 other shapes, coefficients up to 6), so the potential-function argument does not
    apply there. All of these are computed EXACTLY by the 2-dim vector calculus (section 4), without diagrams.
 T2 Vertical (dihedral) inversions: three arc-pair channels (Theorem V):
      J(s.l1.B.(x2)^a.u1) Phi_3 =. t A + (-t)^a ((1+t^2) A + t B) + t^(3a-1) Phi_5 B,   A = a(v_B), B = b(v_B).
    More channels give more room for cancellation; finite windows in a per body.
 T3 Width two and higher, non-arborescent quotients: J = phi rho_2(beta) v with rho_2 the 9-dim valenced TL / mixed
    Artin B_4 module Hom(V_1, V_1 x V_2^{x4}) (Flores-Peltola L_(1,2,2,2,2)^(1)). Cancellation needs coincidences of the
    representation: kernel or line-stabiliser elements (Bigelow-style), or tuned extreme-term cancellation.
 T4 Swap sums: J_3(K') = 1 (needs a_2(K') = 0 and V_K'(zeta_5) = +-1). Lowest priority tonight.

## 4. The 2-dim vector calculus (exact; from mont/proof, mont/nest, mont/notie REPORTs; all TRUSTED/PROVED)
 Lambda = Z[t,1/t]. Box vector v = (v_1, v_2) in TH-2BR coordinates; channels a = v_1, b = v_1 + (1-t^3) v_2.
 Y = [[1,0],[t^-3,t^-3]], X = [[1,1-t^4],[0,-t]]; in (a,b): Y = diag(1,t^-3), X = (1/Phi_3)[[-t^3,(1+t)(1+t^2)],[t(1+t),1]].
 Stacking B_1.B_2: v_1 * v_2 = channelwise product (v1w1, v1w2+v2w1+(1-t^3)v2w2).   Twist rows: (r1)^j.y0.y2...y_2j.(u1)^j
 has vector X^j Y e_1 (mirror X^-j Y^-1 e_1). Folding: v(r2.(x1)^m.B.u1) = X^m v(B). Outer map (Theorem O):
 v(r2.(y1)^m.B_1...B_n.u1) = t^(2m(1-eps)) X^(-m) (v_1*...*v_n), eps = (-1)^(#axis letters) = b(p)(-1).
 Closure: J(s.r2.(y1)^m.B_1...B_n.u1) = norm(e_1^T X^(-m) (v_1*...*v_n)); J(s.B_1...B_n) = prod J(s.B_i).
 Any body's vector is fixed exactly by two raw closures: v = (alpha_0, (t^2 alpha_{-1} - alpha_0)/(1-t^4)), alpha_m = lp.J_raw
 of s.r2.(y1)^m.B.u1 (m = 0, -1) (CHECKED 243/243). general_boxes.json has 50 non-rational body vectors.
 Every tree corresponds to an explicit half-word, so every algebraic hit can be checked with lp.J.

## 5. Verification protocol for ANY candidate with J a unit
 (1) build the explicit half-word; recompute J with lp.J (exact) and confirm normalised J = 1;
 (2) certify K nontrivial: V_K != 1 (tools/kauffman.bracket, normalised as in mont/ft/ident3.py) or Delta_K != 1 (tools/alex.py)
     or det != 1; if V_K = 1 and Delta_K = 1 that is itself a Jones-trivial knot candidate: record it and flag it;
 (3) write /Users/calebbarnett/Documents/Codex/2026-10-31/it-is-an-open-problem-whether-4/collab/HIT-<time>.md at once
     (word, J, V_K, Delta_K, method) and STOP searching to double-check; a second independent check follows.
 A candidate whose K is the unknot is NOT a hit (unique inversion of the unknot); record it as a sanity check only.

## 6. Efficiency rules
 - Every search region must be justified by section 3; dedupe by (J, Delta_K) and canonical forms; skip anything in
   section 2 before computing; respect caps (minutes per experiment, hours per lane); no kht++.
 - Log NEAR MISSES, which are the main scientific output if there is no hit: span(J) small relative to complexity
   (crossings, sum of box spans), a "cancellation deficit" (expected no-cancellation span minus actual span), and gates
   passed (a_2 = 0; J(zeta_10) = 1; J = 1 mod (t+1)^k for large k). Explain which mechanism produced each near miss.
 - Write REPORT.md in your lane folder continuously; every claim marked PROVED / CHECKED(n) / CONJECTURE / GAP.

## UPDATE 2026-11-17 01:58 (after engines A and B; NO HIT)
New computationally empty regions and mechanisms: read engineA/REPORT.md sections 3, 5, 6, 7 and engineB/REPORT.md sections 4, 5 before searching. Summary:
- engineA: delta-law (order 1) and sigma-law (order 2, Lemma S) PROVED for rational boxes; Theorem V2 (vertical closures of rational bodies never tie to order 2 at both ends); Lemma W exact twist windows; third-order wall CHECKED (nested boxes reach two-ended order 2, never 3; positivity Delta_t + Delta_b >= 2 at mu = +-1, +-2); eigenslope contraction gives deep ONE-ended cancellation only. Open: depth-3 nesting around positive-potential boxes; general body 43 vertical; GAP 1 (Conjecture V3, BX4-type lemma), GAP 2 (third-order positivity).
- engineB: rho_2 (9-dim) and rho_3 (51-dim) exact; all width-two theta-curves |W| <= 14 empty (rigorous to 12); seven-sector double-twist lines all geometric; doubly gated minimum span 13 with J - 1 = (gate divisor) x Phi_6; no Bigelow-type coincidence. Not covered: x4/y4 words (21-dim general two-cup block).
- Common picture: one-ended cancellation is cheap, two-ended cancellation is blocked by additive (delta, sigma) or positive (order 3) end invariants. New targets must defeat this, not re-test it.
