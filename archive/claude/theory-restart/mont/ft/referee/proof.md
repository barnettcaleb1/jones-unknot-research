# REFEREE NOTES: lane PROOF (ft/proof/REPORT.md), adversarial
Referee: Claude (adversarial referee for lane PROOF), 16 Nov 2026.
Own scripts: ~/jones-lanes/theory-restart/mont/ft/referee/proofref/ (independent code; builder files only read).
Marks: PROVED / CHECKED(n) / CONJECTURE / GAP / KNOWN. Severity: FATAL / SERIOUS / MINOR.

STATUS: COMPLETE. VERDICT: STANDS_WITH_REPAIRS (all repairs minor/presentational; THEOREM FT stands unconditionally).

## 0. Verdict
 STANDS_WITH_REPAIRS. Every PROVED and CHECKED claim survived: proofs re-derived line by line, and every computational claim
 recomputed with independent code (own TL algebra, own half-word generator, own tracer of k, own state sum, own upstairs-lift
 code, own osp(1|2) construction) on new samples (own random walk words, fs.gen new seeds, words.mont Montesinos words).
 NO fatal and NO serious error found. THEOREM FT (claim 1) STANDS as stated, with no repair. The repairs are:
  R1 (minor, claim 8) the written proof of 4T goes through the operator form 4.3, which the report itself only marks CHECKED;
     either upgrade 4.3 to PROVED (standard Brauer -> OSp(1|2) tensor calculus + 2 Omega = P - K + P K = K) or label 4T
     "PROVED modulo 4.3". A clean replacement proof given 4.3 is in section 3 (R1) below.
  R2 (minor, claim 10 / REPORT 4.3 text) the formula "Omega = sum_a x^a (x) x_a with str(x^a x_b) = delta" is, read literally
     with the Koszul action (X(x)Y)(u(x)w) = (-1)^{|Y||u|} Xu (x) Yw, NOT ad-invariant: rank(2 Omega - P) = 5 and the Casimir is
     diag(1,-2,-2), not scalar (proofref/osp_ref.py). The invariant tensor is sum_a (-1)^{|a|} x^a (x) x_a (equivalently the
     builder's code convention: dual defined by str(x_c x^b) = delta with the dual in the FIRST slot). With it: 2 Omega - P is
     a rank-1 idempotent, i.e. 2 Omega = P - K, K^2 = -K, Casimir = -1 on V. The builder's code (osp12.py) is right; only the
     sentence in REPORT 4.3 needs the convention.
  R3 (cosmetic) type counts: "192 order-3 types" (3.6, claim 11) vs 193 (3.5; the extra one is o o o); "214/214" (osp) vs 215
     types of order <= 3; Lemma 3.1(iii) writes A^{8f'} y for the ratio with Theta_0 (harmless: A^8 = 1 mod x).
  Upgrade suggestion (not an error): n_i = 4 eps_i is provable, not only CHECKED (see claim 4).

## 1. Claim-by-claim
 1. THEOREM FT (2.5). Proof re-derived line by line (Thm 2.1 multilinearity; Lemma 2.2 (a)-(c); Prop 2.3; Lemma 2.4; the
    intersection x^m Z[A^+-1] n Lambda = x^m Lambda). No gap found. Every step is sound once (i) lp.J_raw(word_S) = (unit) *
    <Theta_S;1,1,2>/<Theta_0> (the brief's KNOWN equivalence, ../proof/REPORT.md 0.2) and (ii) the quotient pieces at sites are
    exactly R^{+-1} (off-axis: (c,2j)(c,2j-1)(c,2j+1)(c,2j) = s_b s_a s_c s_b, palindromic, so the flip is the inverse) and
    F^{+-1} (on-axis: (c,0)(c,1)(c,1)(c,0), position 0 = axis), which I re-derived from flat_search.quotient_word.
    Numerics with OWN code (proofref/ft_ref.py, own random generator myword() + fs.gen new seed + words.mont Montesinos words,
    longer words, m = 2..6, mixed/off/on): Delta^m J divisible by (1+t)^m in 59/59 tests, 0 failures; order exactly m attained in
    30 of them (incl. m = 5: 9 cases, m = 6: 2 cases). VERDICT: STANDS. (Same theorem as Astra's FT, brief UPDATE 21:25; the
    builder's route is different: Dubrovnik relation + integrality lemma instead of Astra's lattice on V_2.)
 2. Local relations L1, L2: RE-DERIVED by eigenvalues (KL lambda^{22}_c = A^-8, -A^-4, A^4; lambda^{12}_c squared = t^2, t^-1)
    and CHECKED with the referee's OWN Temperley-Lieb code (proofref/tl_ref.py, planar-matching composition, sympy):
    C C^-1 = 1, (L1), minimal polynomial (R-A^-8)(R+A^-4)(R-A^4) = 0, (L2) both forms, (F-t^2)(F-t^-1) = 0: all True.
    Convention check: 'x' = A*vertical + A^-1*cupcap (kauffman.py), so the 2-cable of an x-letter has eigenvalue A^4 on
    channel 4, i.e. x <-> R (kappa = +1), as the builder says. VERDICT: STANDS.
 3. INTEGRALITY LEMMA: re-derived. Step 1: the e-term of the 2-cable of a colour-2 loop l is the boundary of the blackboard
    band N_l cut along one arc, an embedded disc missing G - l (other strands pass over/under the thin band), so it is a split
    unknot even when l links A or k; <G> = <G^{l,1}> - (-A^3)^{+-f} <G - l>, no delta^-1 survives. Several f_2 on one
    colour-2 edge merge (idempotent, slide through crossings). Step 2: S^3 - int N(k) is a ball; KBSM of (B^3, 4 pts) is free on
    two crossingless matchings; Q_inf caps the f_2-band (0), Q_0 closes it to a blackboard f_2-annulus with unknotted core
    (A^{8f'} Delta_2). Class G is closed under 2-cabled smoothings and twist removal. No gap. Consistency checks (own runs):
    lp's unit u = y + delta x equals 1 in 800/800 base+flipped words, J_raw(-1) = 1 in 800/800. VERDICT: STANDS.
 4. Units. Prop 2.3 re-derived: correct (Lemma 2.2(a)-(c) are right: Z[A^+-1]/(x) = Z[zeta_8]; units = +-A^k; (1-x)^n =
    1 - n x mod x^2 also for n < 0 since 1 - x = -t is a unit). The multiplicativity is FORCED, exactly as claimed.
    n_i = 4 eps_i: CHECKED with own code 93/93 (n_i from own state sum = lp increment = -4*(alex.diagram sign)); both crossings of
    an off-axis pair have the same sign 93/93. Referee remark: n_i = 4 eps_i is in fact provable in two lines (not just CHECKED):
    n_i = W_1(Jhat) = 4 kappa pi (-1)^tau (off), -4 kappa (on), and the upstairs sign in the bracket convention is kappa*pi on
    the same sheet, -kappa*pi across sheets (h reverses the orientation of K but the rotation preserves vertical direction),
    and -kappa on the axis (the two strands of an on-axis crossing are antiparallel). Only 'n_i = lp's increment' needs the
    framing unit of lp (S-independence of A^{8f'}), which stays CHECKED. VERDICT: STANDS.
 5. Symbol state sum 3.2: re-derived (Y_i(-1): (A^4-A^-4)/x -> -2, Id = 'or' iff pi = +1; on-axis -(F+3) / +(F_y+3);
    Lemma 3.1 values c(0) = Delta_2(zeta) = -1, c(1) = A^8+1+A^-8 = 3 by the encircling lemma; deframing via Lemma 2.4 with
    (w_i - 1)/x -> n_i and u_empty(-1) = 1). Lemma 3.1 proof checked step by step: (i) mod-x moves are legitimate because the
    smoothed graphs stay in class G (integral); (ii) homotopy in S^3 - A never crosses A, loops are classified by lk; (iii) the
    writhe-0 argument for T'(1/0) (antiparallel finger pairs) holds for every graph obtained from Theta_S by 2-cabled
    smoothings and twist removals. Own implementation (written from the report's text, not from symbol.py) agrees with exact
    alternating sums: m=1..4, 40/40 (seed 7) + 90/90 (seed 2027; 38 nonzero). VERDICT: STANDS.
 6. 1T-a,b,c: proofs re-derived (the "or"/"un" bookkeeping, the mod-2 description of loops as sums of chord intervals,
    and the pairwise cancellation in the deframing sum). Correct. CHECKED with own code on ALL types of order 2, 3, 4
    (proofref/rel_ref.py): 1T-a 8+87+1264, 1T-b 12+94+1000, 1T-c 6+47+500 instances, 0 failures. Corollary (on-axis-only
    configurations have W_m = 0) follows. VERDICT: STANDS.
 7. (CONJECTURE, not a target) Cheap falsification attempt at ORDER 4 with own lift code: all 2721 labelled order-4 types,
    1483 degenerate (isolated upstairs chord or self-crossing-only pair): W = 0 in all 1483; converse also holds at order 4
    (0 exceptions; 1238 nonzero types). Builder's counts reproduced at order <= 3 (215 types, 129 degenerate).
 8. 4T: CHECKED with own code, 200 random backgrounds (0-2 background chords, 0-1 on-axis sites, 0-4 twists, random
    positions/roles of I_1, I_2, I_3): D1 - D2 + D3 - D4 = 0 for W(J) 200/200 and W(Jhat) 200/200 with quotient signs;
    fails 67/200 with upstairs signs (the builder's warning reproduced). PROOF status: see issues (the written proof goes
    through the operator form 4.3, which the builder itself marks CHECKED, not PROVED).
 9. W_2, W_3 tables (W_2 = -12 Delta^2 a_2 additionally CHECKED two independent ways: exact W_2 vs a_2(K) from V_K, 22/22
    (7 nonzero); table vs the a_2 symbol computed from my upstairs lifts, 38/38 order-2 realisations, crossing counts 2, 4, 2
    exactly as in 3.4): recomputed with the referee's OWN state sum (proofref/ss.py + abstract_ref.py; labels realised by
    inserting non-site twists in ALL 2^(P-1) ways): W_2 table identical to 3.4; W_3: 193/193 entries identical to
    w3_table.json, 78 nonzero, all multiples of 48; W depends only on (matching, labels): 0 violations over all twist
    placements (order 2 and 3). Own state sum = exact [Delta^m J/x^m](-1) from lp.J on 40/40 independent words (m = 1..4),
    see section 2.
 10. osp(1|2) (CHECKED claim): INDEPENDENT construction (proofref/osp_ref.py): osp(1|2) solved from the invariance condition
    for the even supersymmetric form on C^{1|2} (dim 3|2), str 1 = -1, str g = 3. With the invariant Omega (see R2):
    2 Omega = P - K. Koszul-signed Wilson-line weight system <v0| word |v0> (chord -> 2 Omega, on-axis site -> g + 3, twist -> g)
    times prod(-2 eps^q) equals the Brauer state sum W(Jhat) on ALL realisations (types x twist placements) of order 1, 2, 3:
    3 + 38 + 772 = 813/813; with the deframed insertions (-2 eps^q (2 Omega + 2(-1)^tau), on-axis 3(1 - g) = 6 P_odd) it equals
    W(J) on 813/813. 4.1-4.2 are restatements of Lemma 3.1 (R mod x is the super flip: eigenvalues (1,1,-1) on channels with
    quantum dims (1,-1,1) = sdims of C + V + osp(1|2)); correct. VERDICT: STANDS (with R2).
 11. F3 at symbol level: INDEPENDENT recomputation. symbol(v_3) per labelled type from the UPSTAIRS LIFT (own code
    proofref/iota_ref.py: chord {a,b} label 0 -> {a,b},{h a,h b}; label 1 -> {a,h b},{h a,b}; on-axis point p -> {p,h p}; sum over
    one lift per site of the v_3 weight system P3 -> 1, K3 -> 2). Agrees with the builder's 'Delta3 v3' column on all 78 listed
    rows (the 115 unlisted types have W_3 = 0 and v_3-symbol 0). Validated against EXACT data: eps*Delta^3 v_3 (V_K from
    kauffman.bracket) = lift symbol of the configuration's type 120/120, and eps*W_3(exact) = table value 120/120 (54 distinct
    types hit, 25 of them with W_3 != 0; proofref/type_test.py). iota symbol integral on all 193 types; support of
    symbol(iota - v_3): -16 on 10 labelled types (shapes c0c1c2c1c2c0, c0c1c2c2c0c1, c0c1c2c2c1c0), -8 on 20 (shapes
    c0c1c2c0c1c2, c0c1c2c0c2c1, c0c1c2c1c0c2, c0c1oc0c1, c0c1oc1c0): IDENTICAL to the builder's list. Exact third differences on
    51 random configurations (vk_test.py): Delta^3 M_3^lp = 6 W_3 (51/51), Delta^3 iota integral 51/51, eps*Delta^3(iota - v_3)
    in {0: 39, -8: 8, -16: 4}. VERDICT: STANDS (minor: the report says 192 types here and 193 in 3.5; the difference is o o o).

## 2. Independent computations
 proofref/common.py   own generator myword() (random walk on half-width, caps/cups/crossings), flips, exact (1+t)-division.
 proofref/tl_ref.py   own TL algebra (planar matchings), (L1), (L2) .......................................... all True
 proofref/ft_ref.py   FT divisibility, seeds 101: 59 tests m = 2..6 (my/fs/mont; mix/off/on) .................. 59/59
 proofref/ss.py       own tracer of k (port graph of the half-diagram) + state sum + deframing (from REPORT 3.2 text)
 proofref/ss_test.py  own W_m vs exact (seed 7): 40/40 agree; n_i = lp increment 93/93; n_i = -4*(alex sign) 93/93;
                      both crossings of an off-axis pair have equal sign 93/93
 proofref/abstract_ref.py  W_2, W_3 tables (see 9)
 proofref/vk_test.py  seed 2027, 90 configs: own W = exact (m=2: 22/22, m=3: 51/51, m=4: 17/17; 38 nonzero); W_2 = -12 Delta^2 a_2(K)
                      22/22; Delta^3 M_3^lp = 6 W_3; Delta^3 iota integral 51/51; eps*Delta^3(iota - v_3) in {0,-8,-16}
 proofref/rel_ref.py  4T 200/200 (quotient signs; upstairs signs fail 67/200); 1T-a,b,c and equivariant-1T at orders 2,3,4
 proofref/iota_ref.py, type_test.py  v_3 symbol from upstairs lifts; exact eps*W_3 = table 120/120, exact eps*Delta^3 v_3 =
                      lift symbol 120/120 (54 types hit); iota support list reproduced exactly
 proofref/osp_ref.py  osp(1|2) from scratch; Omega convention (R2); word = Brauer state sum 813/813 (W(Jhat) and W(J))
 inline checks         u = y + delta x = 1 and J_raw(-1) = 1 (800/800); lp exponent additive over 3-5 sites with increments n_i,
                      constant sign, FT for unnormalised J_raw: 40/40 each

## 3. Issues found (with repairs)
 No FATAL, no SERIOUS issue.
 R1 (MINOR) 4T proof dependency. Replacement proof, given 4.3: push all g's to the left end (<v0| g = <v0|), so the word is
   <v0| prod_p Ad_{g^{s(p)}}(X_p) |v0>, s(p) = sheet of position p (labels = sheet differences). D1 - D2 + D3 - D4 inserts at
   (I_1, I_2, I_3) the element sum_a (Ad_{g^{s1}} (x) Ad_{g^{s2}})( [x^a (x) 1 + 1 (x) x^a, Omega_12] ) (x) Ad_{g^{s3}} x_a, with Koszul
   signs; it vanishes by ad-invariance of Omega because Ad_g is a Lie superalgebra automorphism. Background chords and twists
   are untouched (pointwise identity in the word). Deframing adds scalars to chords. This avoids the implicit 'three
   parallel strands in a box' orientation bookkeeping of the written B_3(delta) argument. CHECKED numerically 200/200 above.
 R2 (MINOR) Omega convention in REPORT 4.3 (details in section 0).
 R3 (COSMETIC) counts 192/193, 214/215; Lemma 3.1(iii) A^{8f'} relative to Theta_0.
 Not issues (checked and fine): mirror form of (L2) for y0; sign conventions t vs t' (Delta^m M_m^lp = m! W_m, e.g.
   Delta^3 M_3^lp = 6 W_3 verified 51/51); bracket-vs-alex sign convention (eps_bracket = -alex sign, 93/93); delta = 0 at
   t = -1 never evaluated (all statements are about integral evaluations of graphs in G); scope of moves (every crossing of a
   symmetric half-word diagram is a site letter; flips keep a knot and the inversion; u stays 1).

