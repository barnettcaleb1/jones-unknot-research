# REFEREE NOTES: NO-TIE lane (mont/notie/REPORT.md)
Referee: Claude subagent (adversarial), 16 Nov 2026. Status: COMPLETE. Verdict: STANDS WITH REPAIRS (main theorem stands; repairs are to side claims and presentation).

Legend: OK = step checked and holds; ISSUE(sev) = problem found; NE = not established (asserted, not proved).

## 0. Scope of review
- Sec 1 reductions R0-R2; Sec 2 box laws BX1-BX4; Sec 3 N1-N5; Sec 4 main theorem; Sec 6 span (M4,S1,S3, counterexamples);
  Sec 9 pretzel closed form, T1, T2.
- Independent recomputation with my own code (referee/rcore.py and referee/t_*.py; the other files in referee/ belong to other
  referees), on words longer than the builder used.

## 1. Logic check (by hand)
1.1 J*Phi_3 = w_1 A + w_3 B is an ALGEBRAIC identity once J := e_1^T X^mu (v_1*...*v_n): e_1^T X^mu = (1, f'), f' = (1-t^4)(1-(-t)^mu)/(1+t),
    v_2 = (b-a)/(1-t^3), so J = a + (1+t^2)(1-(-t)^mu)(b-a)/Phi_3. OK. (Theorem N, that this is the knot's J, is NOT proved: acknowledged.)
1.2 w-data table (tops, c1, rho of w_1, w_3): recomputed by hand for mu >= 2, mu = 1 (w_1 = -t^3), mu = -1 (w_1 = -1/t), mu = -2, mu <= -3. OK.
1.3 R0 normal form: E e_1 = Y^-1 e_1 and E Y^-1 e_1 = t^4 e_1 (checked), E Y^0 E = t^4: reduction terminates. OK.
    Box well-definedness: X, Y act on slopes by T -> T/(2T+1), T -> T+1, generating Gamma_0(2); orbit of 0/1 = all p/q with q odd,
    i.e. exactly the W-to-E rational tangles; E^2 = t^4 so rho is a projective rep of PGamma_0(2) = Z * Z_2 and X fixes e_1.
    So each rational box has a well-defined vector up to unit, and k = #E in the reduced coset word is an invariant. OK.
1.4 N1/N2 tie tables, N3 (one-endedness, all 9 pairs), N4 arithmetic, span J = span A - 4 + T + T'' (top/bottom bookkeeping via
    bar(J Phi_3) = t^-2 bar J Phi_3): all redone by hand. OK.
1.5 BX2 derivations: redone each expansion (positive step from R_c/S_j/init, R_c with Y^-m, S_j with Y^-m (m>=2), S_j with Y^-1,
    init with Y^-m). All OK, including rho(q) = c, -1, 0. BX3 potential: all 8 increments recomputed: 0,0,0,-1,0,c-1,-[j=0],-[j=0]. OK.
    Equality case: any visit to R_0 or S_{j>=1}, or two consecutive same-sign exponents, forces a strict decrease. OK.
1.6 BX4 expansions (third order on alternating paths): positive step D = -t + 1 + 0/t + ..., R_1 -> S_0 D = -t^{3m+3}(1 + 1/t + 0/t^2),
    init -> S_0 D = t^{3m+1}(1 + 0 + 0). Additivity of l_2 = x_2 - x_1^2/2. OK.
1.7 Main theorem case table (B1 mu<=-2 n=2 / n>=3 -> P1; B1 mu=-1 n=2,3,4,>=5; B2 n=2, n>=3; B3 n=2,3,4,>=5): every ratio
    recomputed from N5 with the w-data; all as stated. P1: w_1(-2) = t + 1 + t^-2, Delta = 1-n <= -5, J = c t^{D-1}(1 + 0/t + (Y-1)/t^2).
    OK.

## 2. Independent computations
Code: referee/rcore.py (own Laurent arithmetic, matrices typed from the BRIEF, own box/necklace builders; imports nothing
from notie/). All checks exact.
2.1 Box laws (t_box.py, t_box_exh.py). For each normal form u(m_0..m_{k-1}) compute a, b exactly; read the state from the
    expansion of r = v_2/v_1 at t = infinity; compare with an independently re-coded BX2 automaton.
    - 3,300 random normal forms, k up to 30, |m| up to 24, six sign-biased generators (uniform, mostly -1 [long S_j chains],
      mostly +1 [R_0 chains], alternating, small {+-1,+-2}, doubled magnitudes); spans of a(u) up to 943:
      BX2 state + rho_a + rho_b: 0 mismatches. BX3 inequalities: 0 failures. Equality characterisation (S-top & rho_a = 0 iff
      signs alternate and end negative): 0 failures. TH-2BR facts (lc a = +-1 both ends, span a >= 4, R-top iff m_{k-1} > 0,
      deg b - deg a in {2,0} with the stated lc relation): 0 failures. R2 mirror identities for a and b: 0 failures.
      BX4 (x_2(a) = -(k - [m_0 <= -2])/2 on alternating S-boxes): 374 boxes, 0 failures.
    - Exhaustive k <= 6, |m| <= 3 (46,655 normal forms): BX2 + span >= 4: 0 mismatches.
    VERDICT on Sec 2: BX1-BX4 hold on everything I tried; the hand derivations in Sec 2 also check line by line (Sec 1 above).
2.2 Necklaces (t_neck.py; J computed as (w_1 A + w_3 t^{-3N} B)/Phi_3 by exact division, cross-checked against the star-product/
    matrix route e_1^T X^mu Y^N (u_1*...*u_n) on 221 random cases: 0 mismatches). Runs: seeds 1,2,3,7:
    11,240 necklaces in all, 5,083 with (mu,N) forced into a first-order tie; n = 2..22; boxes up to k = 14, |m| <= 9 (|m| <= 30 in the stress run 2.11);
    |mu| <= 9, N in [-15,19]. Tie types seen: T1 965, T2 1689, T3 106, B1 889, B2 1415, B3 81, none 6095.
    - unit J: 0.  M4 (raw J = 1 mod t^4-1): 0 violations.  N1/N2 (predicted vs actual first-order cancellation, both ends): 0 mismatches.
    - two-ended first-order tie: 0.  N5 clean-end second coefficient (predicted from the automaton, not from the polynomial): 0 mismatches.
    - S3 (coefficient below a cancelled top tie = c1(w_1A)(s_1-s_3), and the closed form of s_1-s_3): 2,760 ties, 0 mismatches.
    - no-tie span >= span A - 2: 0 violations.
    - c2(J) = 0 at a clean end happened 12 times, ALL in necklaces with no tie at either end (case (i)), where the theorem claims
      nothing about c2. In tie cases (case (ii)) c2 = 0 never occurred outside P1. Consistent with the statement as written.
2.3 P1 (t_p1.py): 90 instances, n = 6, 12, 18, random alternating S-boxes up to k = 14, |m| <= 8: c2 = 0 and c3 = c1(Y-1) != 0 in all.
2.4 Quoted examples (t_examples.py): n=13 example span 48 (both versions) REPRODUCED; P1 example top 1,0,-1,8 / bottom -6,28 / span 24
    REPRODUCED; minimal families u(-2)^n (mu=-1,N=1) and u(1)^n (mu=-1,N=n) spans 6,9,13,17,21 REPRODUCED (also n=7: 25).
2.5 CASCADE CLAIM (Sec 6 'OBSTRUCTION'): the quoted (m,j) data mostly reproduce, but
    - m = 3, j = 14 gives span J = 20, not 16 (report: '14, 14, 16, 16'; I get 14, 14, 16, 20).
    - The claim 'along this family span J does not grow with j' is FALSE beyond j ~ 3m: for m = 5, j = 18, 22, 30, 40, 60 give
      span J = 24, 28, 36, 46, 66 (T saturates at -10; span A - span J saturates at 13-14). For m = 8, span A - span J saturates at 22.
      So for FIXED m the deficit is bounded and the j-family does NOT refute 'span J >= span A - C'.
    - The conclusion survives with a 2-parameter family: max_j (span A - span J) = 8, 10, 14, 16, 22, 32, 40, 58 for
      m = 3, 4, 5, 6, 8, 11, 14, 20 (attained near j = 3m) (t_cascade2.py). So 'no bound span J >= span A - C' is CHECKED
      (unbounded along m), but the report's stated mechanism/evidence is wrong and must be replaced.
2.6 Minimal span searches over ALL first-order tie configurations (t_minspan.py; only ties can go below 4n-2):
    n=3: boxes k<=2,|m|<=3 (43,068 tie necklaces) and k<=3,|m|<=2 (241,280): min 9 = 3n (u(-2)^3, mu=-1, N=1).
    n=4: boxes k<=2,|m|<=3, |mu|<=6 (259,920 tie necklaces): min 13. n=5: (k<=1,|m|<=6) and (k<=2,|m|<=2): min 17.
    No span < 3n found. Consistent with S4 and with 'n=4 minimum 13', but the latter is only searched, not proved.
2.7 Pretzel section (t_pretzel.py, t_pretzel2.py, t_t2b.py):
    - closed form G = w_1 prod(Phi_6 + z alpha) + w_3 t^{-3k} prod(Phi_6 - z beta) vs necklace of row vectors X^j Y e_1 / X^-l Y^-1 e_1:
      400 random (n <= 6, |r| <= 21, |mu| <= 8, extra twist k in [-4,4] sometimes): 0 failures (unit t^{sum u_r} as stated).
    - span J = 2n + top H + top H'' - 4 (H = G/Phi_6^n is a RATIONAL function; top H := top G - 2n): 0 failures.
    - gamma_0 = Phi_3, gamma_1 formula, degeneration identity, pair identity: exact (sympy cancel), mu in [-6,6]\{0}.
      g_m formula: exact for m <= 10; I also PROVED it for all m by hand: w_1(t^2+1)^m + w_3(-t)^m
      = (t^2+1)Phi_3 (t[m-1] + (-t)^mu [m]) using t(t^2+1)^m + (t^2+1)(-t)^m = (t^2+1) t((t^2+1)^{m-1} - (-t)^{m-1}). OK.
    - T1 top-H formula: 1500 fresh cases (n <= 7, l <= 15, mu <= 12, 40% forced into the degenerate l_min = mu branch): 0 failures;
      no T1 pretzel with span < 3n.  Clean-top formula: 1500 fresh, 0 failures.
    - T2: 4000 fresh (m <= 16, j <= 16, up to 6 negative rows, l <= 18): reduction span = 3n + L + m - 3 + top H exact;
      min top H = -1; min span - 3n = 1.
    - OPEN subcase T2(b) exhaustively (m in [3,16], j = l_1 in [1,m-2], up to 4 further rows from l_1+1..l_1+7, l_1+12):
      51,975 configurations; top H in {-1,0,1}; the x_1 / x_2 predictions agree whenever decisive; third-order region
      (x_1 = x_2 = 0): 9,282 cases, top H = -1 in ALL of them. So the open claim holds well beyond the builder's range (CHECKED only).
    - Genuine-pretzel minima, exhaustive over row multisets |r| in [3,11], |mu| <= 6 (t_pretzmin.py): n = 2..5 give 6, 9, 13, 17, all at
      P(-2,3,...,3) (mu = -1). REPRODUCED.
2.8 S3 span consequences (t_s3span.py): 1,736 forced first-order-only top ties (s_1 != s_3): actual span equals the stated value
    (T1/T2/T3 formulas) in all; 332 second-order ties (s_1 = s_3) go up to 5 below span A - 3, consistent with 'deficit >= 2 possible'.
2.9 Zero-excess scan (t_zeroexcess.py, u(-2)^p u(1)^{n-p}, all tie (mu,N), |mu| <= 8, n <= 45): min span = 4n - 3 except n = 13, 25, 37
    (= 1 mod 12) where 4n - 4; min span - 3n = 0 only at n = 2, 3. REPRODUCED and extended (builder: n <= 28, |mu| <= 4).
2.10 Theorem N spot check (t_thmN.py, t_thmN2.py): bracket state sum lp.J vs necklace formula on 8 chosen + 92 random NEW pretzel words
    (n <= 4, rows in {+-1,...,+-9}, m in [-4,4]\{0}): all equal. Unit J occurred only for P(2m,1,-1)-type words with NO non-integral
    row (unknot), consistent with the n >= 2 hypothesis.
2.11 Extra checks: necklace-level mirror identity bar J(mu,N;u) = t^{-4K} J(-mu,n-N;u'') on 400 random necklaces: 0 failures
    (t_mirror_neck.py). Stress run (t_stress.py): 1,500 necklaces with |m| <= 30, |mu| <= 30, |N| <= 40, mostly forced ties:
    0 prediction failures, 0 units, 0 two-ended ties. T2(a) formula top H = 1/0/-1 exhaustive (m <= 14, up to 4 rows): 1,625, 0 failures.
2.12 c2 can vanish at an end of a NO-TIE necklace (examples, both span >= 4n-2): mu=-1, N=8, u(-2),u(-3): bottom 1,0,-2,3 (span 31);
    mu=-1, N=-1, u(2),u(1,-2,3,-1,1): top 1,0,-4,7 (span 40). Not a counterexample (the theorem claims c2 != 0 only at the clean end
    of a TIE necklace), but the Sec 0 sentence 'so the clean end's second coefficient cannot vanish' is true only in case (ii).

## 3. Issues list (claim / problem / severity / fix)
I1 (minor) CLAIM Sec 6 'OBSTRUCTION': along u_1 = u(-m,-1,-1), u_2 = u(-2,-1^j), mu = 3, N = 0, 'span J does not grow with j while span A
   grows by 1 per unit of j, so no bound span J >= span A - C exists'; data 'm = 3 gives 14, 14, 16, 16'.
   PROBLEM: false for fixed m. The deficit saturates near j ~ 3m: m = 5, j = 18, 22, 30, 40, 60 give span J = 24, 28, 36, 46, 66
   (T stuck at -10, span A - span J stuck at 13); m = 8 saturates at 22. m = 3, j = 14 gives 20, not 16. The summary's REFUTED status
   for 'no bound span J >= span A - C' rests on this family.
   FIX: use the two-parameter family: max_j (span A - span J) = 8, 10, 14, 16, 22, 32, 40, 58 at m = 3, 4, 5, 6, 8, 11, 14, 20
   (j ~ 3m), which does grow without bound in the data (CHECKED, not PROVED). Restate the mechanism: the depth is set by the
   matching box u(-m,-1,-1) (about 3m), not by the near-trivial box, which only needs j >~ 3m. Change the status from REFUTED to CHECKED.
I2 (minor) CLAIM (summary): 'The BRIEF's n=4 minimum of 14 is not the true minimum, which is 13.' PROBLEM: no lower bound 13 is proved
   (S3 gives span >= 13 only when s_1 != s_3; S4 is a conjecture). FIX: 'min <= 13; = 13 in exhaustive searches' (mine: all tie
   necklaces with boxes k <= 2, |m| <= 3, |mu| <= 6: min 13).
I3 (minor) HYPOTHESIS 'a(v_i) non-unit' vs 'tangle non-integral'. The equivalence holds but is not written down. Needed facts: X, Y act on
   slopes as generators of Gamma_0(2) (T -> T/(2T+1), T -> T+1); the orbit of 0 is exactly the odd-denominator (W-to-E) tangles;
   E^2 = t^4 so rho is projective on PGamma_0(2) = Z * Z_2 with Stab(e_1) = <X>; the R0 normal form is a coset normal form;
   slope -> line is injective because k >= 1 forces span a >= 4 (TH-2BR). So k = 0 <=> integral <=> a unit. FIX: add this as a lemma.
   Note that 'every rational body has vector rho(w)e_1' for bodies that are not twist rows is part of the unproved Theorem N realisation.
I4 (minor) COMPLETENESS of the reductions. The report proves n >= 2, mu != 0. The rest of the X^mu necklace class is easy but not stated:
   mu = 0 gives J = A, a product of non-units; n <= 1 is a TH-2BR word. FIX: one line in the Corollary, so Lemma Q covers the whole
   class (rational boxes, special twist X^mu).
I5 (minor) WORDING. Headline 'Lemma Q holds for Montesinos necklaces' should say 'for the algebraic necklace coefficient'; the knot
   statement is conditional on Theorem N (the body of the report says this correctly). The Sec 0 sentence 'the clean end's second
   coefficient cannot vanish' holds only in case (ii) (see 2.12).
I6 (minor) NOTATION. rho means three things: the representation, the normalised 2nd coefficient, and the number of R-top boxes. Y means
   the matrix and also sum x_2 in P1. H = G/Phi_6^n is a rational function and top H means top G - 2n. FIX: rename.
I7 (info, not a defect) Dependencies: Theorem N (BRIEF, unproved) and the TH-2BR span formula/automaton (board). I re-checked the TH-2BR
   facts that are used (lc +-1, span a >= 4, R/S degree/lc laws) on 50k normal forms.
I8 (info) OPEN pretzel subcase T2(b) (third order): top H = -1 in all 9,282 third-order configurations of my exhaustive run, and
   top H >= -1 in all 51,975 (b)-configurations, well beyond the builder's 14,742. Status stays CHECKED.

## 4. Verdict
STANDS WITH REPAIRS.
- THEOREM Q-MONT (algebraic: n >= 2, mu != 0, any k, boxes with a(v_i) non-unit => J not a unit, >= 2 nonzero coefficients):
  every step re-derived by hand (R0-R2, BX1-BX4, N1-N5, the full case table, P1). Independently recomputed on 11,240 + 1,500
  necklaces (5,083 forced ties) and 50k boxes, k up to 30, n up to 22. No gap, no counterexample. PROVED as an algebraic statement,
  given TH-2BR. Topological reading conditional on Theorem N, as the report says.
- M4/S1 (span >= 4), N4/S2 (no tie: span >= span A - 2 >= 4n-2), S3 (first-order tie: span >= span A - 3) all hold; S3's span
  table matches exactly on 1,736 ties.
- Counterexample to 4n-3 (n = 13, span 48) REPRODUCED. Pretzel closed form, identities, T1, clean tops REPRODUCED; g_m proved for all m.
- Repairs needed: I1 (wrong evidence for the cascade claim; the conclusion survives with a corrected family), I2 (overclaim),
  I3-I6 (missing lemma, completeness line, wording, notation).
- Conjecture S4 (span >= 3n): consistent with everything I ran (zero-excess to n = 45; exhaustive n = 3,4,5 small boxes; pretzels).
