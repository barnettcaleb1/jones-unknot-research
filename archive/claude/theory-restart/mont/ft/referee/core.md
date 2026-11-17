# REFEREE: lane CORE (adversarial)
(16 Nov 2026, Claude referee. Reads ../BRIEF.md and ../core/REPORT.md. My own scripts: ./coreref/ (rlib.py = own helpers,
independent of core/clib.py; lp.J and kauffman.bracket are the shared DEFINITIONS and are used as such). Status tags as in BRIEF.)

## 0. Verdict: STANDS_WITH_REPAIRS
No fatal error. Every PROVED derivation was redone line by line; every CHECKED/computational claim was recomputed with my own code
on new data (other seeds, longer words, four other generators, exhaustive length-8 two-bridge words). 0 computational failures.
BRIEF 1.3 (on which (b), (c) rest) was confirmed DIRECTLY by building the branch sets T(1/n) from the quotient tangle (40 random +
6 two-bridge words). Conjecture D survived ~30,000 new nontrivial cases (incl. 80 core samples, 8748 exhaustive length-8 two-bridge
words, 19,784 axis-only / nested-cap words). Repairs needed:
  R1 (SERIOUS, claim 11): the conclusion "any proof must work with invariants, not R-matrices" is FALSE: in Astra's s-lattice the
     braiding is integral and equals the super flip at q = i (r7_rmat.py); FT is proved that way (BRIEF 21:25). Restrict the
     Jordan-block statement to the divided-power lattice.
  R2 (MINOR but must be fixed before LIT sees it, claim 9 / core 3.6 (4)): J(K' # rho K', swap)(t) = J_3(K'; 1/t) (checked exactly
     on 9 swap words), i.e. I(K'*) in standard conventions; the "pure coloured Jones statement" must read J_3(K'; xi) =
     V_K'(xi^-2)^2 (the stated V_K'(xi^2)^2 is false for both trefoils).
  R3 (MINOR, claim 3): span 5 is attained by exactly TWO J (t^6-t^7+t^8-t^10+t^11 and mirror; c = -6,-5 and 11,12 give the same J),
     not four. (The pair is realised: it is J of the T(2,5) inversion s.l1.y0.x1.x1.u2 and its mirror.)
  R4 (MINOR, claim 2): it proves 36 | M_3 (already BRIEF MOMENT-3), NOT the integrality of iota (that needs Conjecture D);
     reword "proves F3's integrality".
  R5 (MINOR, claim 6): Corollary 1 needs the three test inversions to share sigma (they do: j = 1 for RHT, 4_1 h1, T(2,5)) or,
     cleaner, use even n (sigma = 0 always). The whole corollary hinges on the -60 n^2 a_4 coefficient of Lin-Wang, which I could
     not check independently (the trefoil-level part of the conversion IS confirmed by Le's Poincare-sphere series: 45 / 39).
  R6 (MINOR, claim 10): cite THEOREM FT (Astra) instead of the osp/so(3) "MEMORY" route.
  R7 (MINOR, conventions C1): 1.3's V(L_n) is in the J-variable t = A^4, opposite to V_K (t = A^-4); named branch sets (T(3,5),
     P(-2,3,7), T(3,7)*) and the sign in "J'(1) = sigma(L_odd)", "j = -sigma/8" refer to that variable. In a uniform standard
     convention sigma_std(L_odd) = +8j and e.g. L_1(4_1 h2) = T(3,7)_+ (consistent with Sigma_2(T(3,7)_+) = S^3_{+1}(4_1)).
  R8 (MINOR, claim 1): "no further cyclotomic factor from classical evaluations" is a heuristic (JVW list of easy points), not a
     theorem; label it so.

## 1. Claim-by-claim (running)
1. J'(1) = 8Q(1) = sigma(L_odd); (t-1)^2 not forced in core.
   Derivation re-done line by line: correct (t = e^u in 1.3; G(1) = 0; V'(1) = 0 gives G'(1) = -2j; D_7'(1) = 8).
   CHECKED independently: J'(1) = 8Q(1), Q(-1) = a_2(K) on 708 new random words (seeds 1001/2002/3003, lengths 4-36);
   core samples with Q(1) = +-2 found in all three seeds (16 of 41 core samples). Sign of "= sigma" is convention (BRIEF j = -sigma/8).
2. Moment formula etc. Re-derived: D_7(-e^h) = -(e^{7h}-e^{4h}-e^{3h}+1); D_8(-e^h) = e^{8h}-e^{7h}-e^{5h}+e^{3h}+e^h-1;
   M_3 = -36(2q_1+7q_0), M_4 = -(144q_2+1008q_1+2064q_0), core M_3 = 72q'_0, M_4 = 288q'_1 + 16 M_3. All correct.
   CHECKED: the full formula for k <= 8 and all stated congruences on the same 708 words (41 core). 0 failures.
7. Conjecture D: CHECKED on new data, 0 failures: 708 random flat_search words (lengths 4-36), 150 own random Morse words
   (<= 7 half-strands), 120 Montesinos words (words.mont, random signs/rows/twists), 150 two-bridge words of length 8-16
   (builder only did <= 7), 80 own swap words (several caps/cups). iota = g(1) - 3v_3 and iota in Z: 708/708.
   Further: all 8748 reduced two-bridge words of length 8 (r5_2br.py); 19,784 nontrivial axis-only words (s.(x0|y0)^L, L <= 9)
   and nested-cap words s.l1.l1.W.u1.u1 / s.l2.l1.W.u3.u1 (W over x0..y2, length <= 6); 80 CORE samples (r10_core.py; also
   V_K(zeta_5) != 1 in all 80, as it must be since J != 1); the a_2 = 0 Montesinos family P(2,3,5), P(4,7,9) and sign variants.
   0 failures anywhere. Derivation of iota = g(1) - 3v_3 from D (h^3 coefficient, f(e^h) = 30h^3(1+5h+...)) redone: correct.
   VERDICT: a well-supported CONJECTURE; the "PROVED parts" (Phi_1^3, Phi_2, Phi_3) are correctly reduced to F1 and M_2 = -24a_2.

3. Span theorem. Lemma re-proved (P = t^c mod D when span < deg D). Own exact code r3_span.py (R_c for |c| <= 400 plus a rigorous
   tail: per residue class mod 12 the coefficients of R_c are polynomials in c of degree <= max(a,b)-1, interpolated exactly,
   integer zeros listed; none outside the window, no identically-zero class). CONFIRMED: D_7: min span 4 only at t^7+t^4-t^3 and
   its mirror; D_8 (core): span exactly 7 for every c outside [0,7]; D_8b: min 6 only at t^4+t^6-t^10 and mirror; D_9: min 7.
   ERROR (MINOR): "span 5 occurs for exactly 4 more J (c in {-6,-5,11,12})" double counts: R_{-5} = t R_{-6} and R_{12} = t R_{11},
   so c = -6,-5 give the SAME J = t^6-t^7+t^8-t^10+t^11 and c = 11,12 its mirror: exactly TWO more J of span 5. (Same
   phenomenon behind "D_9: 4 values of c": they give 2 distinct J.) Repair: count J's, not c's.
4. 6_2 pair. INDEPENDENT DIRECT CHECK (r4_closure.py): I built T(1/n) directly from the quotient tangle (flat_search state machine,
   then k framing half-twists on (b2,b3), n half-twists on (b1,b2), close). For each word there is a UNIQUE k in [-40,40] making all
   closures det 1 (the 0-framing); with it the closures reproduce BRIEF 1.3 EXACTLY, in the J-variable t = A^4, with my twist
   sign n <-> 1.3's -n: 6 two-bridge words x 6 values of n, and 40 random words x n in {1,-1,2,3}: 0 mismatches. For the 6_2 pair:
   T(1) of h: det 1, c_1 = 24, c_2 = 108; of h': det 1, c_1 = 24, c_2 = 228 (also n=-1: 24 vs -96; n=2: -228 vs 12). Words: same
   V_K = t^-1-1+2t-2t^2+2t^3-2t^4+t^5 (6_2), a_2 = -1, M_3 = -612 / +108: CONFIRMED. Robustness: sigma(L) = sigma(L') also follows
   from Mullins alone (equal c_1, equal lambda of the common Sigma_2), and c_2 is mirror-invariant, so (b) does not depend on the
   global sign conventions. 4-plat / two-bridge / det 11 / alternating identification of 6_2 re-derived: correct.
   VERDICT claim 4: STANDS (modulo 1.3, now independently confirmed on these words).

5. Y = S^3_{+1}(4_1) pair. Direct closures (r4_closure.py): L_{-1}(RHT) and L_1(4_1 h1) both have J-variable V =
   V_std(mont(1,[3,7])) = t^5+t^7-t^11+t^12-t^13, c_1 = 24, c_2 = 180; L_1(4_1 h2) has J-variable V = V(T(3,7)*), c_1 = 0,
   c_2 = -48. Numbers CONFIRMED. Names are identifications by V only (as the REPORT says, CHECKED level) and are in the J-variable
   (see C1): in the convention of V_K, L_1(4_1 h2) is the POSITIVE T(3,7), which is consistent with the classical fact
   Sigma_2(T(3,7)_+) = Sigma(2,3,7) = S^3_{+1}(4_1) (lambda = -1). Conclusion ("opposite signatures, not decisive") correct. STANDS.
6. Lin-Wang lambda_2 identity. Algebra re-derived by hand from 2.1 and the quoted Thm 4.3 (conversion v_2^LW = -6a_2,
   v_3^LW = 36 v_3 under V_LW(t) = V(1/t)): correct. INDEPENDENT DATA POINT for the conversion: Le's Ohtsuki series of the
   Poincare sphere, (1/(1-q)) sum_n q^n (q^{n+1};q)_{n+1} = 1 - 6x + 45x^2 - 464x^3 + 6224x^4 - ... (x = q-1; I expanded it
   exactly; the numbers agree with the series as I remember it from the literature). lambda_1 = -6 fixes the orientation
   Sigma(2,3,5) = S^3_{-1}(LHT); the converted formula gives exactly 45 there, and 45 + (-6) = 39 for S^3_{+1}(RHT) (LW's example).
   NOT independently checked: the -60 n^2 a_4 coefficient (trefoils have a_4 = 0). Corollary 1 rests entirely on it being nonzero.
   Corollary 1 logic: with alpha, beta allowed to depend on sigma, the three test inversions must share sigma. CHECKED: the RHT
   word, 4_1 h1 and the T(2,5) word s.l1.y0.x1.x1.u2 all have j = 1 (J(T(2,5)) = t^-11 - t^-10 + t^-8 - t^-7 + t^-6, which is
   exactly the span-5 congruence solution of claim 3). So the argument is complete as written, but the REPORT does not say so;
   cleaner repair: compare n^2-coefficients over EVEN n, where sigma = 0 for every (K,h). The exact identity itself re-checked on
   30 DIRECT closures (6 words incl. T(2,5) with a_4 = 1 and a random word with a_4 = 3, j = -2; n in {1,-1,2,-2,3}): 30/30.
   VERDICT: STANDS modulo the source's a_4 term.
8. Two-bridge mechanism. r5_2br.py (mpmath, 40 digits): tr^2/det agree on X, Y, XY, XY^-1 and a length-7 word for all 4 primitive
   10th roots xi and all 4 roots A of A^-4 = xi^2 (max deviation 4e-37); |tr[X,Y]-2| = sqrt5 (irreducible). The displayed
   matrix-element identity e1^T rho_J(W)(xi) e1 = (-A^-3)^{#y0-#x0} A^{6(#x1-#y1)} <K_W>(A) (xi = s A^-2) holds on 60/60 random
   words (lengths 1-12) with rho_J(W) = rho(W_last)...rho(W_first). Exact J(xi) = V_K(xi^2): all 8748 reduced length-8 words
   (builder: <= 7) + 150 random lengths 8-16. Argument (Fricke characters + eigen-matching + empty word) is sound. STANDS.
9. Swap sums. r6_swap.py: own Habiro-formula colour-2 coloured Jones J_3 (standard variable, J_2 = V, V(RHT) = t+t^3-t^4).
   For 9 swap words found by search (K' = 4_1 x3, RHT x3, LHT x3; V_K = V_K'^2 in all): J(swap)(t) = J_3(K'; 1/t) EXACTLY
   (no extra unit), and J != J_3(K'; t) for the trefoils. So, in standard conventions, J(K' # rho K', swap) = I(K'*) (mirror),
   not I(K'); harmless for detection. BUT the "pure statement about coloured Jones polynomials" in core 3.6 (4)
   ("the colour-2 coloured Jones polynomial at a primitive 10th root xi equals V_K'(xi^2)^2") is FALSE in standard conventions
   (fails for both trefoils at all four xi); the correct form is J_3(K'; xi) = V_K'(xi^-2)^2 (true for both trefoils at all xi).
   MINOR as a convention slip, but it must be fixed before it goes to the LIT lane. Conditional constraint (t-1)(t^3-1)(t^5-1) |
   V_K - 1: derivation correct (t -> t^2 maps primitive 10th roots onto primitive 5th roots; local diffeo at 1). STANDS with repair.
10. Tower vanishes to any finite order. Logic re-derived: FT restricted to swap words (off-axis flips only) makes M_k(K' # rho K')
   an order-<= k Vassiliev invariant of K' (any singular long knot can be drawn in the half-plane, and J depends only on the
   knot type of K' since the quotient is the trivial theta-curve with K' tied in the arc); C_{N+1}-trivial nontrivial K' exist for
   all N (KNOWN: Ohyama, Habiro). Correct. But the REPORT's stated proof route (osp(1|2)/so(3) correspondence, "MEMORY") is not a
   proof; the claim is PROVED because THEOREM FT is proved (Astra, BRIEF 21:25 update). Repair: cite that. CONCRETE INSTANCE
   (r9_tower.py, via J(swap) = J_3(K';1/t) and multiplicativity): K' = RHT # LHT # 4_1 # 4_1 (a_2 = v_3 = 0, C_4-trivial):
   M_1 = M_2 = M_3 = 0, M_4 = -46080, J != 1. "No finite-order / positivity / bounded-first-moment mechanism" is a correct
   meta-statement about MOMENT-based arguments only (informal; not a theorem about all mechanisms). STANDS with citation repair.
11. R-matrix. r7_rmat.py: in the divided-power (Lusztig) lattice, at q = i: (B-1)(B+1) != 0, (B-1)^2(B+1) = 0: computation
   CONFIRMED. In Astra's s-lattice (E w1 = s w0, ..., s^2 = [2]) the braiding has entries in Z[q,1/q] and at q = i, s = 0 it is
   EXACTLY the super flip (w1 even, w0, w2 odd), an involution. So the conclusion "any proof must work with invariants
   (super correspondence, semisimplification), not R-matrices" is FALSE (and was already refuted by the BRIEF 21:25 update:
   THEOREM FT proved by Astra with this lattice). SERIOUS overstatement; no downstream damage. Repair: restrict to the
   divided-power lattice and cite the s-lattice proof.
12. r8_claim12.py: (a) own constituent builder; 200 new random words (78 with K_out nontrivial): rank(features) = 8,
   rank([features | M_3]) = 9, so M_3 is not in the Q-span of {1, a2, v3 of K, K_in, K_out, j}: CONFIRMED. (b) Delta M_3 pattern on
   ALL two-bridge words of length <= 8 grouped by (V_K, Delta(2), Delta(3), Delta(5)): 155 pairs (builder 76), 0 violations.

## 2. Independent computations (scripts in ./coreref)
- r1_basic.py SEED N Lmin Lmax : claims 1, 2, 7 on flat_search.gen words.
- r2_gens.py {morse,mont,2br,swap} ... : F1, M_2, M_3 congruences, Conjecture D on other generators.
- r3_span.py : span theorem, exact.
- r4_closure.py : direct branch-set closures T(1/n) with framing correction; compare13(word) tests BRIEF 1.3.
- r5_2br.py : two-bridge Phi_5 mechanism (characters, matrix element identity, exhaustive length 8).
- r6_swap.py : swap sums vs Habiro coloured Jones; 10th-root statement in standard conventions.
- r7_rmat.py : braiding at q = i in the divided-power lattice and in Astra's s-lattice.
- r8_claim12.py fit|pairs : M_3 regression (rank test), two-bridge Delta M_3 pattern.
- r9_tower.py : C_4-trivial instance of claim 10 (K' = RHT # LHT # 4_1 # 4_1).
- r10_core.py : core-targeted Conjecture D test, k_0 = 4 example (confirmed: a_2 = 0, M_1..M_3 = 0, M_4 = -15552, span 16),
  M_4 signs in the core (37 -, 42 +, 1 zero of 80: both signs, as claimed in core 4.1).

## 3. Hidden assumptions / conventions (running)
- C1 (variable of 1.3): BRIEF 1.3's V(T(1/n)) is in the J-VARIABLE t = A^4 (lp.J_raw divides A-exponents by +4), while V_K
  (clib.VK, rlib.VK) uses t = A^-4. So the branch-set polynomials, c_1, sigma_B and the NAMED branch sets in core 2.2
  (T(3,5), P(-2,3,7), T(3,7)*) are those of the mirror images of the branch sets drawn in the same conventions as K. Internally
  consistent (BRIEF's j = -sigma/8 and the -sigma/8 sign in the builder's Mullins formula absorb it), and harmless for c_2 (mirror-
  invariant) and for all relative statements; but a reader using the standard convention (V(RHT) = t+t^3-t^4, Sigma_2(T(3,5)_+) =
  Sigma(2,3,5) = S^3_{-1}(LHT), lambda = -1) must mirror every named branch set (e.g. L_1(RHT) is T(3,5)* in that convention,
  which indeed double covers S^3_{+1}(RHT) = -Sigma(2,3,5)).
- C2 (units): J = 1 mod (t+1)^2 and V(1) = 1, V'(1) = 0 fix all units, so Conjecture D is a unit-free statement (good). For swap
  sums the 0-framed J_3 already satisfies J_3 = 1 mod (t+1)^2 in the 3 knots tested, so "J = I" needs no extra unit there.
- C3 (delta = 0 at t = -1): claim 9's Schur step is a Laurent-polynomial identity valid generically, hence identically
  (<U; 2> = delta^2 - 1 = -1 at t = -1, no pole); claim 8 works at A with A^4 a primitive 5th root, where delta != 0. No issue.
- C4 (framing of T(1/n)): the raw quotient tangle of flat_search is NOT 0-framed (offset k = -4 for s.l1.y0.x1.u2, -2 for 4_1 h1,
  +14 for a random word); 1.3 refers to the 0-framed tangle, singled out by det(T(1/n)) = 1 for all n (unique k). Anyone
  recomputing branch sets from bracket_vector must insert these twists. The builder never built T(1/n) directly (all branch-set
  data come from 1.3); this referee report supplies the missing direct check.
- C5 (scope of moves): claim 10 needs FT only for off-axis symmetric flips (swap words have no axis letters). Covered by FT.
- C6 (mirrors): (K,h) -> (K*,h) sends J(t) -> J(1/t), V_K(t) -> V_K(1/t) and the modulus to a unit multiple of itself, so
  Conjecture D is mirror-compatible; the pairing J(xi) <-> V_K(xi^2) (not xi^-2) is forced by the mixed variables (C1).
