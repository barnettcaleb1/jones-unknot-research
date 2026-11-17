# Referee report on lane IDENT (adversarial)
(16 Nov 2026, Claude referee. Target: mont/ft/ident/REPORT.md. My scripts: mont/ft/referee/ident_work/.)
Tags: PROVED / CHECKED(n) / CONJECTURE / GAP / KNOWN. No novelty judgements.

## 0. Verdict: STANDS_WITH_REPAIRS
Nothing in the ten claims is broken. Every number I recomputed with my own code agrees exactly with the builder's
(150/150 stored rows, all family rows, both claim-10 examples). The repairs are about scope and conventions, not about
mathematics: (a) J and V_K are computed in OPPOSITE chirality conventions (lp.J: t = A^{+4}; V_K: t = A^{-4} on the same
bracket), so 'J = colour-2 Jones of K_1' and 'v_3(K_1)' do not refer to the same chirality; in one uniform convention the
odd formulas read M_3^loc = -864 v_3(K_1), M_3 = -432 v_3(K) + 180 D (divisibility statements unaffected); (b) claim 4's
phrase 'products of N_1 with order-2 invariants' must be restricted to the listed ones (which span only 6 dimensions,
because N_2 - N_1^2 = -8(a_2(K_in) + a_2(K_out)), a relation I found, CHECKED 400); (c) claim 7's family values for
k >= 3 depend on Theorem N (CHECKED, not proved); the 'exactly when 5 does not divide k' clause was supported only by
k = 5, 10 on the 5 | k side, and is now justified by the closed form j_4 = 18k^2(8k^2 - 1) (5 | j_4 iff 5 | k);
(d) the U_in/U_out/Sato-Levine columns of the certificates come from the builder's constructions (U_in passed my
discriminating symmetry test; SL not independently verified).
One builder GAP is CLOSED here: the 'unrealised' type T0^T1^T2^ is realised by s.r1.c2.w0.u1.r1.c2.w0.u1.r1.c2.w0.u1
(all 64 letter choices are knots of that type by the builder's own classifier), with D-, M_3- and v_3-symbols all 0. The
conditional integrality proof of D therefore rests only on FT (proved, BRIEF update) and the classification conjecture,
which survived 4800 new configurations at levels 2, 3, 4 with 0 inconsistencies.

## 1. Claim-by-claim
1. [CHECKED] Constituent knots.  STANDS.  Geometry re-derived (sec. 3.1): the quotient map (x+iz) -> (x+iz)^2 is
   orientation preserving; near an on-axis crossing the image arc crosses the axis line first UNDER, then OVER, both as
   'x'-type crossings in the code's picture ('x' = TL-BR over), i.e. x0 -> (x,0),(x,0); A_out is disjoint from the
   diagram strip.  Independent implementation (constit.py): det(K) = det(K_in) det(K_out) 150/150 (42 with both
   factors > 1) with this handedness, but only 49/150 with the windings reversed, so the det identity really validates
   the construction.  The builder's stored a_2, v_3, j_4, a_4 of K, K_in, K_out agree with mine on all 150 rows.
2. [PROVED] Local formulas.  STANDS (proof sound given FT; KNOWN: rational Vassiliev knot invariants of order <= 4 form a
   6-dim space with basis 1, a_2, v_3, a_2^2, a_4, j_4; parity removes v_3 from M_4 and constants vanish at the trivial
   knot; the exact fit is overdetermined).  My check: 200 new local words, 29 distinct K_1 tuples, 0 failures in K-form
   and K_1-form (R3).  K_1 -> K conversion re-derived by hand.  CAVEAT (convention, R4): J(local) is the colour-2 Jones
   of K_1 computed with t = A^{+4}, V_K uses t = A^{-4}; with one convention J(local) = col2(mirror K_1), so the sign of
   every v_3-term flips (M_2, M_4 formulas are mirror-even and unaffected).  Repair: say so explicitly.
3. [CHECKED] D integral; local-trivial; symbols.  STANDS.  D in Z on 1912 new words (R2, R13), 0 failures;
   local vanishing = claim 2; level-3 symbols in 8Z on 400 new configurations, '2 chords + T' rule 280/280 (R7);
   level-4 sums of D vanish (79/79 checked explicitly; type-constant on 343 repeated level-4 types).  GAP closed (R11).
4. [PROVED] D not a combination.  STANDS with a scope repair.  Certificate re-derived exactly on the builder's rows
   (16 words, y.D = -464/5; R10); independent certificate on 160 fresh words against my own 10 candidates (v_3 of K,
   K_in, K_out; N_1, N_3, N_1N_2, N_1^3, N_1 a_2(K/K_in/K_out)): 8 words, y.D = -64/3.  The proof is valid as a
   statement about the computed functions; for U_in, U_out, SL it inherits the correctness of the builder's
   constructions (U_in: symmetric K_+/K_- test 60/60 vs 46/60 for a deliberately wrong resolution; SL: unverified).
   Wording: 'order-2 invariants' must mean the listed ones; completeness of that list is not shown.
5. [PROVED] F4.  STANDS.  Integrality CHECKED on 1912 new words (via G4 = M_4 + 1440a_2^2 - 864j_4 + 120a_2, so a_4
   drops out); local vanishing = claim 2; certificate re-derived exactly (46 words; candidate matrix rank 47 of 56 on
   150 rows, so at least 9 relations among the candidates, partly explained by the N_2 identity); independent
   certificate on fresh words against 32 own candidates (27 words).
6. [CONJECTURE] Corollary.  Logic correct: J = 1 => M_k = N_k = 0 for k >= 1; M_4 = 0 with a_2 = 0 gives
   3j_4 = 5(a_4 - F4) after dividing by 288; j_4 = sum V_e binom(e,4) - 9v_3 + 11a_2/4 (re-derived), integral when
   a_2 = 0.  Correctly labelled conditional on D, F4 in Z.
7. [CHECKED] Family.  STANDS, strengthened (R8): rows k = 1..4 reproduced exactly; k = 1, 2 straight from the half-words;
   closed forms hold for k <= 10; NEW j_4 = 18k^2(8k^2-1), a_4 = -2k^2(8k^2+1)/3, F4 = -8k^2(11k^2-2)/3.  Repairs:
   name the Theorem-N dependence for k >= 3; justify the 5 | k half by the j_4 closed form.
8. [CONJECTURE] Classification.  Strongly supported (R12): 0 inconsistencies; delta-independence of the M_2, M_3, M_4
   and D symbols and delta-dependence of N_2, N_3, N_4, a_2(K_in), v_3(K_in) confirmed (U_in not tested).
9. [CHECKED] t = +1 expansion.  STANDS (R6), strengthened: N_1 = 4(sum_{T^} sigma - sum_{C-} sigma) exactly (300/300);
   N_1 in 8Z is immediate from F1.  New: N_2 - N_1^2 = -8(a_2(K_in) + a_2(K_out)) (CHECKED 150 + 250).
10. [CHECKED] Examples.  STANDS (R1), strengthened: for s.r1.x2.y1.y0.x1.x2.x1.x2.y0.y1.x2.y1.u1 also N_1 = ... = N_4 = 0
   (N_5 = -7680, M_5 = 69120), so even the t = +1 moments of order <= 4 do not see it.

## 2. Independent recomputations (log)
Code: ident_work/refinv.py (my own; imports only the shared lp.J, kauffman.bracket, alex.parse/symmetrize/diagram/
alex_matrix; nothing from ident/). V_K normalised V(1)=1, V'(1)=0 with t = A^-4 on kauffman's bracket (same convention
as BRIEF F3 / ident3.py); a_2, v_3, j_4 from power sums m_k = sum V_e e^k (a_2 = -m_2/6, v_3 = -m_3/36, j_4 = m_4/24);
Alexander polynomial by modular evaluation + Newton interpolation + CRT (3 primes ~2^61), a_4 = mu_4/24 - a_2/12
(mu_k = sum Delta_e e^k), cross-checked a_2(Delta) = a_2(V).
R1 (examples, claim 10) CHECKED by my code: s.r1.x2.y1.y0.x1.x2.x1.x2.y0.y1.x2.y1.u1: a_2 = v_3 = a_4 = j_4 = 0,
   M_2 = M_3 = M_4 = 0, M_5 = 69120 (exact).  s.l1.x2.x2.x0.x1.x1.y0.x1.x1.l2.y0.y2.y1.x4.x1.x4.x3.u1.y2.u1:
   a_2 = v_3 = a_4 = j_4 = 0, M_3 = 1080 (D = 6), M_4 = -25920 (F4 = -18), N_1 = -16.  Figure-eight inversions
   s.l1.y0.y0.x1.u2 / s.l1.x0.x0.y1.u2: M_3 = -180 / +180, v_3 = 0, D = -1 / +1 (= BRIEF calibration iota = -1/+1).
R2 (integrality of D and F4, claims 3 and 5) CHECKED on 1500 NEW words, 0 failures (412 more in R13: 1912 in all).  F4 integrality is tested through
   G4 := M_4 + 1440 a_2^2 - 864 j_4 + 120 a_2 = 1440 (F4 + a_4) mod 1440 (a_4 in Z drops out), D through M_3 - 432 v_3 mod 180.
   Samples (t_integrality.py; integ_*.json): flat_search.gen seeds 7101, 7105 with length 16-30 (longer than the builder's
   6-22): 500 words, 73 with a_2 = 0; my own generator gen2 (width up to 7 half-strands, winding density up to 50%,
   trivial-V words discarded in seed 7104): 500 words, mean 6.6 windings; words.mont(m, rows) with random m in [-3,3],
   1-3 rows in {+-1,+-3,+-5,+-7}, random x/y conventions: 250 words; necklaces s.r2.(x1|y1)^m.B_1.B_2.u1 with random
   generic bodies B_i: 250 words.  D != 0 on about 85% of the nontrivial samples, so the test is not vacuous.

R3 (local formulas, claim 2) CHECKED on 200 NEW local words (fs.gen seed 8101 words with x0/y0 deleted, and my gen2
   with no windings; 29 distinct K_1 tuples; t_local.py): M_2 = -24 a_2(K), M_3 = 432 v_3(K), M_4 = M_4^loc(K) exactly, and
   in K_1 form (K_1 = k u A_out from my own Morse-word bracket + Alexander): M_2 = -48 a_2(K_1), M_3 = 864 v_3(K_1),
   M_4 = 576 a_2^2 - 2880 a_4 + 1728 j_4 - 240 a_2, together with a_2(K) = 2a_2(K_1), v_3(K) = 2v_3(K_1),
   a_4(K) = 2a_4(K_1) + a_2(K_1)^2, j_4(K) = 2j_4(K_1) + 9a_2(K_1)^2: 0 failures.  The algebra converting K_1-form to
   K-form re-derived by hand (coefficient of a_2^2: 144 + 360 - 1944 = -1440): correct.
R4 (premise of claim 2: J(local) = normalised colour-2 Jones of K_1) CHECKED 40/40 by an independent computation: the
   Jones-Wenzl 2-cable <K_1^(2)> - <K_1^(2) with e>/delta, divided by [3], computed with the SAME bracket code, equals lp.J
   after normalisation when converted with t = A^{+4} (40/40), but only 23/40 with t = A^{-4}; those 23 are exactly the
   words with V(K_1)(t) = V(K_1)(1/t), and all 17 chiral K_1 match only at t = A^{+4} (rechecked).  CONVENTION FINDING (see sec. 3): lp.J uses t = A^{+4} (lp.J_raw: A^e -> t^{(e-eu)/4}), V_K uses t = A^{-4}
   (ident3.py, diag.jones_from_bracket) on the same bracket.  So 'J = colour-2 Jones of K_1' and 'v_3(K_1)' are taken in
   OPPOSITE chirality conventions.  Also alex.writhe('s.r2.r1.y0.y2.u1.u1') = -3 while its V_K = t + t^3 - t^4 is the
   standard V of the right-handed trefoil: kauffman.py's smoothing weights are the mirror of the standard rule for the
   alex.py picture ('x' = TL-BR over).
R5 (family, claim 7) k = 1, 2 recomputed DIRECTLY from the half-words words.mont(-k,[4k-1,4k+1]) (lp.J of the half-word,
   V_K and Delta_K of its symmetric diagram; no necklace formula, no auxiliary pretzel diagram): (v_3, a_4, j_4, M_3, M_4,
   D, F4) = (-4, -6, 126, -2088, 82944, -2, -24) and (-36, -88, 2232, -17712, 1410048, -12, -448): exactly the builder's rows.
R6 (claim 9) CHECKED with my own traversal of k (mytrav.py; conventions stated there, chosen equal to the builder's
   stated ones): N_1 in 8Z on 300/300 words (also immediate from F1: J - 1 divisible by (t+1)^2(t^2+1)(t^2-t+1)(t-1)
   gives J'(1) = 8 Q(1)); level-1 symbol sigma*(N_1(w) - N_1(w')) = 8 on T^ (114/114), 0 on Tv (208/208), 0 on C+
   (364/364), -8 on C- (213/213); Delta^m N_k = 0 for all m > k (80 configurations, m = 2,3,4, k <= 3).
   EXTRA (CHECKED 300/300, not in the report): N_1 = 4 (sum_{T^ windings} sigma - sum_{odd-label crossings} sigma),
   an explicit diagram formula; so lambda_- alone is not invariant but lambda_- - w_^ is (= -N_1/4).
R7 (claim 3 symbols) CHECKED on 400 NEW level-3 configurations (t_sym3.py, seed 9301; 280 of type '2 chords + 1 T'):
   D-symbol in 8Z always (values 0 x346, 8 x38, -8 x15, 16 x1); the rule 8(-1)^{#odd chords}[T inside both chords]
   holds 280/280; level-4 alternating sums of D vanish 79/79.

R8 (family, claim 7, k <= 10) t_family2.py: J from the necklace closure in matrix form e_1^T X^k (X^{2k-1}Y e_1 * X^{2k}Y e_1)
   with lp.apply/lp.star/lp.close (my own assembly from the BRIEF statement of Theorem N, not the builder's closed-form rows),
   asserted equal to lp.J of the half-word for k = 1, 2 (lp.J itself is infeasible for k >= 3: the twist rows make the
   quotient state space explode).  K-invariants from a width-6 pretzel Morse diagram whose V is asserted equal to the
   half-word's V_K for k <= 3 (pins knot type and chirality).  Results: all four builder rows (k = 1..4) reproduced exactly
   (v_3, a_4, j_4, M_3, M_4, D, F4); closed forms v_3 = -2k(7k^2-1)/3, D = -2k(2k^2+1)/3, M_3 = -2256k^3 + 168k hold for
   k = 1..10; M_2 = 0 for all k.  NEW closed forms (degree-4 interpolation on k = 1..5, confirmed on k = 6..10):
       j_4 = 18 k^2 (8k^2 - 1),   a_4 = -2k^2(8k^2 + 1)/3,   F4 = -8k^2(11k^2 - 2)/3.
   Justification of polynomiality (KNOWN-type argument): k -> k+1 inserts equivariant full-twist units (one symmetric pair
   of full twists per unit), each removable by one equivariant flip, so an order-n (equivariant) invariant is a polynomial
   of degree <= n in k; v_3, j_4 (classical, order 3, 4) are therefore determined by the 10 values.  CONSEQUENCE: 5 | j_4
   iff 5 | k (8k^2 = 1 mod 5 is impossible), and 5 | v_3 iff 5 | k; so 'the test fires exactly when 5 does not divide k'
   is now PROVED (modulo the pretzel identification), whereas the report supported the 5 | k half only by k = 5, 10.
   Remark: in this family M_3 = -24k(94k^2 - 7) != 0 for every k >= 1, so J != 1 already follows from M_3 (the family is
   in any case covered by Q-MONT); the congruence test is weaker than M_3 != 0 by design (it uses K only).
R9 (claim 1 + data layer) t_constit.py: builder rows 150/150 agree with my values for M_2, M_3, M_4, N_1, N_2, N_3, D,
   E4 and a_2, v_3, j_4, a_4 of K, K_in, K_out.  det identity: 150/150 correct handedness, 49/150 reversed handedness.
R10 (certificates, claims 4, 5) t_cert.py: my own exact elimination (Fractions), each certificate verified by direct
   substitution.  Builder rows: D vs 17 candidates -> 16-word certificate, y.D = -464/5; F4 vs 56 -> 46-word certificate.
   Fresh words (seed 9501), own candidates only: D vs 10 -> 8 words, y.D = -64/3; F4 vs 32 (rank 26) -> 27 words.
   Symbol-level certificate (certificate.py/bigfit.py): products are formed from values at each of the 8 words before
   alternating, so, as claimed, no FT assumption enters.
R11 (GAP closed) the type T0^T1^T2^ (three tangencies met in A-order, all against A_in) is realised by the word
   s.r1.c2.w0.u1.r1.c2.w0.u1.r1.c2.w0.u1 (c2 in {x2,y2}, w0 in {x0,y0}; derived from a planar arc that leaves the axis,
   comes back from below to touch it, and repeats three times).  All 64 variants are knots, classified 'T0^T1^T2^' by
   ident/chord.py, delta = ^ for all three by my traversal; level-3 symbols of M_3, v_3, D are 0 and the G4 level-3
   sums are 0 mod 1440 on all 64.
R12 (classification, claim 8) t_class.py / t_class2.py (builder's classifier read-only, my values and signs):
   level 2: 1572 configurations in 23 repeated types, symbols of M_2, a_2(K), N_2, a_2(K_in) constant per type;
   level 3: 1524 configurations in 146 repeated types, M_3, v_3(K), D, N_3, v_3(K_in) constant;
   level 4: 1725 configurations in 343 repeated types (711 types met), M_4, G4, N_4 and D sums constant per type.
   delta-flip pairs: M_2 16/16, M_3 122/122, D 122/122, M_4 364/364 independent of delta; N_2, N_3, N_4, a_2(K_in),
   v_3(K_in) depend on delta.  (Lower-level sums of higher-order invariants are of course NOT type invariants; seen.)
R13 (structured stress) t_struct.py: 412 more words (long x0/y0 runs, width up to 9, necklaces with 3-4 boxes):
   D, F4 integral.  Concatenation s.B1.B2 (equivariant connected sum along the axis): J multiplicative 60/60, D and F4
   additive 60/60 (additivity of F4 re-derived: cross term 6 M_2 M_2' = 3456 a_2 a_2' on both sides).
R14 (relations among candidates) on the builder rows the 7 order-2 candidates have rank 6, the relation being
   N_2 - N_1^2 = -8(a_2(K_in) + a_2(K_out)); CHECKED on 250 fresh words with my constituent code (rhs != 0 in 161).
   Equivalently [h^2] log J(e^h) = -4(a_2(K_in) + a_2(K_out)), the t = +1 companion of M_2 = -24 a_2(K).  (Not in the
   report; possibly KNOWN-type via Casson-Walker of the double branched covers, which I do not claim.)

## 3. Hidden assumptions examined
3.1 Quotient geometry.  h(x,y,z) = (-x,y,-z); on x > 0 the quotient map (x,y,z) -> (x^2-z^2, y, 2xz) preserves orientation
   (dX^dY^dZ = |f'|^2 dx^dy^dz) and the sign of the depth, so crossing letters are unchanged.  On-axis crossing: the
   piece of R with x > 0 maps to X = s^2 - eps^2, Z = -2 s eps (< 0): k crosses the axis line BEHIND it moving left, then
   (piece of L) in FRONT moving right: two 'x' crossings at (0,1) for x0.  Matches diag.quotient_constituent_tokens.
3.2 Chirality and t-conventions (finding).  kauffman.py gives the identity smoothing of an 'x' crossing the weight A,
   which is the mirror of the standard rule for the alex.py picture ('x' = TL-BR over): alex.writhe('s.r2.r1.y0.y2.u1.u1')
   = -3 but its V_K = t + t^3 - t^4 (standard right-handed trefoil).  lp.J then uses t = A^{+4}, so J is standard for
   the alex picture while V_K is standard for its mirror.  Internal identities are unaffected (everything is computed
   with the same code), but every statement that pairs J with V_K-derived odd invariants (v_3, j_odd) carries this sign,
   including the BRIEF's F3 and the site-sign conventions (x0 -> +1 is the alex-picture sign).
3.3 Normalisation/framing units: J = 1 mod (t+1)^2 fixes M_0 = 1, M_1 = 0; a unit J is then 1, so J = 1 <=> 'unit';
   all M_k, N_k (k >= 1) vanish at J = 1.  The FT proof (BRIEF update) handles the unit; no claim uses f_2 at t = -1.
3.4 delta = 0 at t = -1: the builder's arguments use only exact Laurent arithmetic of the plain-bracket y-coefficient
   (lp.J) and FT; no singular theta-values are evaluated.  Fine.
3.5 Moves and connectivity (spanning argument).  Flips = equivariant crossing changes; I re-derived that h preserves
   'descending from the top fixed point' (h reverses both the parameter along K and the depth), on-axis crossings are
   made descending by x0 <-> y0, the unknot has a unique strong inversion (KNOWN) with J = 1, v_3 = 0.  The level-2 type
   count 24 re-derived by hand (TT 6, TC 8, CC 10); the 228 level-3 types come from a brute-force canonical enumeration,
   complete by construction.  The induction itself is correct; its only open input is the classification conjecture.
3.6 Half-word language: l_i and r_i are identical in every tool (only caps); all windings lie on A_in because the fixed
   points are the extreme points of the diagram strip.  lp.J is infeasible on wide twist rows (state explosion), hence
   the Theorem-N dependence for the family at k >= 3.

## 4. Repairs (all minor)
R-a State the conventions: lp.J uses t = A^{+4}, V_K uses t = A^{-4} on kauffman's bracket; equivalently v_3 here is v_3
    of the mirror relative to J.  In a uniform convention: M_3^loc = -864 v_3(K_1), M_3 = -432 v_3(K) + 180 D,
    iota = -v_3 + D (F3 likewise).  'J = colour-2 Jones of K_1' holds with the colour-2 Jones taken at t = A^{+4}.
R-b Claim 4: replace 'products of N_1 with order-2 invariants' by the explicit list, note the relation
    N_2 - N_1^2 = -8(a_2(K_in) + a_2(K_out)), and mark the U_in/U_out/SL part as conditional on those constructions.
R-c Claim 7: name the Theorem-N dependence (k >= 3) and add j_4 = 18k^2(8k^2-1) (and a_4, F4 closed forms), which proves
    the 'exactly when 5 does not divide k' clause given the pretzel identification.
R-d Claim 3 / sec. 3 of the report: the unrealised type is realised (word above); remove that GAP.  Integrality of D
    becomes: PROVED modulo FT and the classification CONJECTURE; CHECKED on 450 + 1912 words.
R-e Claim 10 may be strengthened: N_1..N_4 also vanish on the first example.
