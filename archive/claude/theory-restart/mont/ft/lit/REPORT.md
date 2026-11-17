# LIT lane REPORT (ft round): finite-type theory of J at t = -1, roots-of-unity divisibility F1, osp(1|2) mechanism
(16 Nov 2026, lane ~/jones-lanes/theory-restart/mont/ft/lit/. Status: COMPLETE for this round. Read together with the prior
LIT report ../../lit/REPORT.md, which already covers: J of theta(K,h) not in the literature; Watson/KWZ/Lobb-Watson/Lipshitz-Sarkar/
Collari-Lisca; Sakuma's eta definition; knotoid dictionary (Turaev; Barbensi-Buck-Harrington-Lackenby = BBHL).)

Source tags: READ = full text or abstract page fetched and read this session; SNIPPET = search-engine text only; MEMORY = background
knowledge, not re-verified this session. Claim tags: PROVED / CHECKED(n) / CONJECTURE / GAP / KNOWN (= stated in a cited source).
Quotes kept under 15 words. Scripts in this folder: col2_torus.py, sqrt_check.py (sympy + lp.py, seconds each).
NOTE: the BRIEF was updated at 21:25 (Astra): THEOREM FT (= F2) is now PROVED, with FT-AXIS and MOMENT-3. Verdicts below account for that.

## 0. Summary and novelty verdicts
F1 (J - 1 in (t^4-1)(t^3+1) Lambda, i.e. J(1) = J(i) = J(e^{i pi/3}) = 1):  NOT FOUND (no paper studies J). NEW AS STATED, LOW
   NOVELTY: a routine corollary of classical evaluations (Jones 1985; Lickorish-Millett 1986; Murakami 1986; Lipson 1986, now
   Jost-Lewark arXiv:2601.16588 Thm 1.1 for the sign at e^{i pi/3}) plus the closure formula 1.3. Natural analogues, all KNOWN:
   Jones's V_K - 1 in (1-t)(1-t^3); Habiro's colour-N divisibility J_K(N) - 1 in (1-q^{N-1})(1-q^{N+1}) (colour 2: (1-t^2)(1-t^4));
   det-1 knots: V - 1 divisible by Phi_1^2 Phi_2 Phi_3 Phi_4 Phi_6 (packaged here from known evaluations; not found stated).
   Cleaner proof input: det(L_1) = 1 gives V_{L_1}(e^{i pi/3}) = +1 exactly (Jost-Lewark Thm 1.1), no algebraic-integer case split.
F2 (THEOREM FT: M_k equivariant finite type of order <= k; Delta^m J divisible by (t+1)^m):  NOT FOUND. NEW AS STATED, MODERATE
   NOVELTY. No theory of finite-type invariants of strongly invertible knots for on-axis + off-axis equivariant crossing changes was
   found, and no paper states that any knot, knotoid or theta-curve invariant is finite type when expanded at t = -1 (q = i).
   But every MECHANISM ingredient is standard, and nearby statements are routine:
   (a) knot level: the spin-1 coloured Jones J3(K; -e^h) is a Vassiliev series (= 1 - 24 a_2 h^2 + ...): corollary of the BMW/Kauffman
       relation R - R^-1 = (s - s^-1)(1 - E), s = q_so(3) = t^-1 (eigenvalue match exact), which vanishes at t = -1 as well as at t = 1 (Turaev's so(N) identification
       + Birman-Lin). PROVED here modulo those standard facts, CHECKED(6 knots: T(2,n), n = 3,5,7,9,-3, and 4_1). Not found stated.
   (b) all-spin-1 theta-curves: Huh-Jin (arXiv:math/0104179) prove Yamada-polynomial coefficients at A = e^x are finite type; every
       factor in their proof is divisible by 1 - A^2, so the SAME proof gives A = -e^x (the osp(1|2) point, loop value -1). They do
       not state it (PROVED by reading their proof).
   (c) off-axis-only equivariant theory exists implicitly: finite-type invariants of spherical knotoids (Manouras-Lambropoulou-
       Kauffman, arXiv:2010.01692, Eur. J. Combin.) transfer via BBHL to symmetric off-axis crossing changes (translation
       CONJECTURE-level, BBHL conventions not re-checked); they expand at t = 1,
       and spherical knotoids already have NONTRIVIAL type-1 invariants.
   (d) abelian precedent: Sakuma's eta = Kojima-Yamasaki eta of the quotient link, whose Cochran coefficients are Vassiliev (Melikhov);
       hence equivariantly finite type by telescoping (deduction here, not stated anywhere).
   What is genuinely new in F2: the mixed colouring (axis 1, arc 2) with the RESTRICTED filtration (single arc-axis crossing changes
   are NOT allowed; on-axis moves are double arc-axis changes), the integral model at the ramified point (Astra: s^2 = [2] ~ ih), the
   FT-AXIS (t+1)^{m+1} improvement, and the explicit local symbols (C_22 creates odd pairs; axis insertions detect parity).
osp(1|2) MECHANISM:  colour-2 part KNOWN (implicit): "sl_2 colour 2 at t = -1 = osp(1|2) fundamental at its classical point" is exactly
   what the Zhang/Blumen/Clark correspondence says once written in Jones variables (Clark, AGT 17 (2017): osp J^lambda_K(q) =
   t^{*(K,lambda)} so J^lambda_K(t^-1 q), t^2 = -1, for EVERY weight lambda; in Jones variables t_J -> -t_J). Super-flip at the root:
   consistent with the classical limit of osp(1|2) (Astra's lattice computation confirms it). The Vassiliev conclusion at t = -1 is
   not stated in any source found, but follows from Blumen's Kauffman-polynomial form or from Clark + Geer (AGT 5 (2005), Le-Murakami
   for Lie superalgebras of type A-G). The AXIS-AS-PARITY-DEFECT part: NOT FOUND; in Clark's framework the axis colour is the lambda = 1
   covering module, which is not a classical osp(1|2) module at q = 1 (Clark Ex. 3.10: quasi-R-matrix entry q^-1 - pi q = 2 there), so
   Geer/Le-Murakami do not cover it. NEW (heuristic) interpretation; present it as a remark, citing Zhang, Blumen, Clark, CFLW, Geer.

## 1. Question (1): finite-type theory for symmetric knots, theta-curves, spatial graphs; anything finite type at q = i / t = -1?
1.1 Equivariant / symmetric knots. Direct searches ("finite type"/"Vassiliev" + strongly invertible / periodic / equivariant /
    symmetric chord diagrams) found NO theory of equivariant finite-type invariants of strongly invertible or periodic knots.
    Garoufalidis's survey "Periodicity of Goussarov-Vassiliev knot invariants" (GT Monographs 4, 2002) is about periodic GENERATING
    FUNCTIONS, not periodic knots [SNIPPET]. Invertibility detection by Vassiliev invariants is open (8_17) [SNIPPET].
1.2 Knotoids (the BBHL dictionary makes these the closest relatives). Manouras-Lambropoulou-Kauffman, arXiv:2010.01692 [READ: Secs
    5, 7, 8]: finite type w.r.t. knotoid crossing changes; spherical knotoids have nontrivial type-1 invariants (classified by linear
    chord diagrams of order one; affine index polynomial; a universal type-1 invariant); bracket/Jones at t = e^x and Turaev's
    extended bracket at A = e^x give type-k coefficients. No t = -1, no colour 2, no theta-curves or strongly invertible knots.
    Translation (elementary, this lane; BBHL conventions not re-checked, so CONJECTURE-level): a knotoid crossing change lifts to a
    symmetric off-axis pair of crossing changes of (K,h); on-axis changes are not knotoid moves. So knotoid FT = off-axis equivariant FT.
    Also: Ding-Jin-Lei-Li-Vesnin arXiv:2511.20269 (virtual knotoids, order one) [SNIPPET]; enhanced Jones of knotoids (Proc. R. Soc. A
    2021) [SNIPPET].
1.3 Theta-curves and spatial graphs (ALL crossing changes allowed). Stanford (Topology 35 (1996); JKTR 3 (1994)); Kanenobu (JKTR 6
    (1997), types <= 3 via the associated 3-component link); Koike (Yokohama Math. J. 47 (1999), types <= 4); Yasuhara (C_k-moves,
    arXiv:math/0104177); Taniyama (arXiv:math/0106173) [SNIPPET/MEMORY]. Huh-Jin arXiv:math/0104179 [READ]: Yamada (and Yokota)
    polynomial at A = e^x has finite-type coefficients; the polynomial's own coefficients do not. OBSERVATION (PROVED by reading
    their proof): their factors -(1 - A^4), -(1 - A^-2), +-(A - A^-1) are all divisible by 1 - A^2, and sigma - sigma^2 = -2 at A = -1,
    so A = -e^x also gives finite-type coefficients. This is the all-spin-1 analogue of F2 at the osp(1|2) point; unstated by them.
    Kontsevich integral of knotted trivalent graphs: Murakami-Ohtsuki (CMP 188 (1997)), Cheptea-Le, Dancso (arXiv:0811.4615, AGT 10
    (2010)), Bar-Natan-Dancso (arXiv:1103.1896), Kassel-Turaev (Duke 92 (1998)) [SNIPPET/MEMORY]. Composed with Lie (super)algebra
    weight systems these give Vassiliev invariants of coloured graphs; no source restricts crossing changes by edge, and the axis
    colour (lambda = 1 covering module at pi = -1) has no classical weight system, so F2 is not an instance of this machinery as is.
1.4 Quantum invariants finite type at q = i or t = -1: NOT FOUND stated anywhere (searched: Birman-Lin-type literature, Bar-Natan's
    VasBib hit only by title, Habiro-ring expansions, osp(1|2) papers, Huh-Jin, MLK). For the Jones polynomial itself it is false
    (V(-1) = +-det is not finite type). Implicit instances: (a) and (b) of Section 0. The Habiro-ring framework gives expansions at all
    roots of unity for 3-manifold invariants (determined by the Ohtsuki series), not finite-type statements for knots at zeta != 1
    [SNIPPET]. Branched-cover genre (relevant background): Kricker arXiv:math/0003035 (moves on knots corresponding to Goussarov-Habiro
    equivalence of branched covers), Garoufalidis-Kricker arXiv:math/0107220 (Topology 43 (2004): LMO of cyclic branched covers via
    the rational Kontsevich integral and signatures) [SNIPPET]; these concern invariants of Sigma_p, which J is not (F3: iota is not a
    function of K).

## 2. Question (2): the sl_2 / so(3) / osp(1|2) correspondence
2.1 Precise statements found.
    - R.B. Zhang, Lett. Math. Phys. (1992): U_q(osp(1|2n)) and U_{-q}(so(2n+1)) have matching finite-dimensional representation theory
      [MEMORY; cited by Blumen and Clark].
    - Blumen arXiv:0901.3232 [READ]: Phi^{osp(1|2n)}_L(q) = F_L(-q^{2n}, q) and Phi^{so(2n+1)}_L(-q) = F_L(q^{2n}, -q) (vector reps; F the
      BMW/Kauffman invariant); equal for closures of sigma_1^m; "equal up to a substitution of variables" for all links.
    - Clark arXiv:1509.03533, AGT 17 (2017) 2961-3005 [READ]: covering quantum group U_{q,pi}, twistor pi -> -pi, q -> t^-1 q (t^2 = -1;
      from Clark-Fan-Li-Wang, CMP 2014 [MEMORY]); THEOREM: osp J^lambda_K(q) = t^{*(K,lambda)} so J^lambda_K(t^-1 q) for every knot and
      every dominant lambda (n = 1: lambda = 1 is the Jones polynomial, lambda = 2 is colour 2). From his Ex. 3.10 skein relation, the
      Jones variable is t_J = q^2 at pi = 1 and t_J = -q^2 at pi = -1: the correspondence is t_J -> -t_J in Jones variables.
    - Ebert arXiv:2210.09583 [READ abstract]: uncoloured U_q(osp(1|2)) invariant = U_{t^-1 q}(sl_2) invariant; Kauffman-bracket-like skein;
      Khovanov-type categorification with an extra Z_4 grading.
    - Ennes-Ramadevi-Ramallo-Sanchez de Santos hep-th/9709068, IJMPA 13 (1998) [READ abstract]; Chauhan-Ramadevi arXiv:2209.00095
      (AHP 2023) [READ abstract], arXiv:2412.10885 [SNIPPET]: physics side, same change of variables.
    - Geer arXiv:math/0411053, AGT 5 (2005) 1111-1139 [SNIPPET]: quantum-group invariant = Kontsevich integral + weight system for Lie
      superalgebras of type A-G (osp(1|2) = B(0,1) included).
2.2 Consequence (this lane). With q_so(3) = t^{+-1} (matching the spin-1 eigenvalues t^2, -t, t^-1 with the BMW eigenvalues), the
    osp(1|2) classical point q_osp = 1 corresponds to q_so(3) = -1, i.e. t = -1 (BRIEF's guess is the right reading). The colour-2
    R-matrix obeys R - R^-1 = (t^-1 - t)(1 - E) integrally (E = cap o cup); at t = -1 it is an involution with +1 on channels 0, 2
    (dims 1 + 3) and -1 on channel 4 (dim 5): the super flip of C^{1|2} (+1-space S^2 = 1 + 1 + 2 = 4, -1-space = 3 + 2 = 5). PROVED
    (eigenvalue bookkeeping); Astra's lattice result in the updated BRIEF agrees.
2.3 Have t = -1 expansions of colour-2 invariants been noted as finite type? NOT FOUND (grep of Blumen, Clark, Ebert for Vassiliev /
    finite type / Kontsevich / weight system: no hits; ERRS, Chauhan-Ramadevi, Geer abstracts silent on t = -1).

## 3. Question (3): coloured Jones, colour 2 (spin 1), at q = i for knots
3.1 KNOWN (corollary of Habiro's cyclotomic expansion; Masbaum AGT 3 (2003) Thm 5.1, Rem 5.2 [READ] in the twist-knot case, Habiro
    Invent. Math. 171 (2008) in general [MEMORY]): J'_K(N) = sum_n f~_{K,n} (q^{1-N})_n (q^{1+N})_n with q = A^4, so J_K(N) - 1 is
    divisible by (1 - q^{N-1})(1 - q^{N+1}). For colour 2 (N = 3): J_K(3; t) - 1 in (t^2-1)(t^4-1) Z[t^+-1]; hence J_K(3) = 1 at
    t = +-1 and t = +-i, and J_K(3) = 1 mod (t+1)^2. The evaluation corollary is not stated as such in what I found (folklore level).
    CHECKED(5) (T(2,n), n = 3, 5, 7, 9, -3).
3.2 Expansion at t = -1 (PROVED modulo the standard BMW identification; CHECKED(6): five T(2,n) by script and, by hand from
    Habiro's coefficients, 4_1 (3_1 by hand as a cross-check of T(2,3))): J3(K; -e^h) = 1 - 24 a_2(K) h^2 + c_3 h^3 + ..., with c_3 = -6n(n^2-1) on T(2,n) (cubic in n, as an
    order-3 invariant must be) and c_3 = 0 on 4_1 (amphichiral). Reason: R - R^-1 = (s - s^-1)(1 - E) with s - s^-1 = 0 and kink factor
    s^2 = 1 at t = -1, so the Birman-Lin skein argument applies; weight system = osp(1|2) = "so(-1)" (Blumen's F_L(-q^2, q)).
3.3 Comparison with J (PROVED from BRIEF's M_1 = 0, M_2 = -24 a_2 and 3.2): J(K,h)^2 = J3(K) mod (t+1)^3 for every (K,h). The same
    constant -24 appears in both. Beyond order 2 there is no such identity (figure-eight inversions: J1 J2 = J3(4_1) mod (t+1)^4 only
    because J2(t) = J1(1/t); in general M_3 contains the equivariant part iota).

## 4. Question (4): invariants of strongly invertible knots; finite type? relation to a Jones-type invariant of the quotient?
4.1 Sakuma's eta (Kinosaki 1986) = Kojima-Yamasaki eta of the quotient link O u L (prior LIT, READ via Mukohara). Cochran's derived
    invariants of a lk-0 two-component link give the Kojima-Yamasaki eta under z = 2 - t - t^-1; Melikhov (arXiv:2011.01409 [READ],
    arXiv:math/0312007 [SNIPPET]) extends each beta^i to a Vassiliev invariant of order 2i+1 and shows -z C_L(-z^2) is a quotient of
    Conway polynomials. DEDUCTION (this lane, not stated in any source): an equivariant crossing change of (K,h) is 4 crossing changes of
    O u L preserving lk = 0, so the Cochran coefficients of Sakuma's eta are equivariant finite-type invariants (order <= 2i+1).
    CONJECTURE-level until the 4-crossing dictionary is written out. Abelian, at t = 1; not related to J in any source.
4.2 Boyle-Issa (arXiv:2101.05413) butterfly links (lk-0 two-component links from an equivariant band move along a half-axis) and their
    Kojima-Yamasaki eta; Di Prisa-Framba (arXiv:2303.08794, AGT 25 (2025)): Conway polynomial of the butterfly link obstructs equivariant
    sliceness; moth links (arXiv:2412.09322): eta gives a homomorphism to Q(t); Di Prisa (arXiv:2207.04985): equivariant concordance
    group not abelian [SNIPPET; Boyle-Issa abstract READ]. Concordance-type; no source claims finite type. Their Conway/eta coefficients
    are finite type AS LINK INVARIANTS, hence plausibly equivariantly finite type by 4.1's telescoping; not stated.
4.3 Equivariant signatures (Alfieri-Boyle arXiv:2109.09915, g-signature), Miller-Powell, Dai-Mallick-Stoffregen [SNIPPET/MEMORY]:
    signature-type, not finite type.
4.4 Khovanov-type: Watson kappa (2017), KWZ multicurves of the quotient tangle (2022, 2026), Lobb-Watson (GT 25 (2021)), Lipshitz-Sarkar
    (2024), Borodzik-Dai-Mallick-Stoffregen (arXiv:2507.13642) [prior LIT READ; abstracts]: not finite type; no t = -1 statements.
    RELATION TO A JONES-TYPE INVARIANT OF THE QUOTIENT: the Euler characteristic of Bar-Natan/KWZ's invariant of the quotient tangle is its
    bracket vector (y, x), so J = y is (up to reduction and grading conventions) the decategorification of KWZ's invariant in the Q_0
    coordinate. This is the only such relation in the literature, and it is implicit. Collari-Lisca's J^e (= Euler characteristic of the
    Lobb-Watson E_3 page = Couture's polynomial) lives on symmetric diagrams, not the quotient; grep: no finite type.
4.5 Other skein-type symmetric invariants (precedents, none stated as finite type): Boyle-Chen half-Conway polynomial for strongly
    negative amphichiral knots, with an EQUIVARIANT SKEIN RELATION (arXiv:2206.03598, Rev. Mat. Iberoam. 40 (2024)) [SNIPPET];
    Eisermann-Lamm W_D(s,t) for symmetric unions, s for on-axis crossings, t for off-axis pairs, W_D(-1,t) = V_{K-} V_{K+}
    (arXiv:0802.2283) [READ abstract]; Politarczyk's equivariant Jones of periodic links (JKTR 26 (2017)) [READ abstract].

## 5. Question (5): the roots-of-unity divisibility F1 and analogues
5.1 Classical evaluations (Jost-Lewark arXiv:2601.16588 (1.2) and Thm 1.1 [READ]): V_K(1) = V_K(e^{2 pi i/3}) = 1;
    V_K(-1) = (-1)^{(det-1)/2} det; V_K(i) = (-1)^{Arf}; V_K(e^{i pi/3}) = eps_K (i sqrt3)^{dim H_1(D_K;F_3)} with eps_K determined by the
    linking pairing (Lipson's singular determinant delta_3). For det K = 1: all five values equal 1 (with V'(1) = 0): V - 1 is divisible
    by Phi_1^2 Phi_2 Phi_3 Phi_4 Phi_6 (PROVED from these KNOWN facts; packaged statement not found).
5.2 Analogues: Jones's (1-t)(1-t^3) for knots [MEMORY]; Habiro's (1-q^{N-1})(1-q^{N+1}) for colour N (3.1); periodic-link congruences
    (Murasugi 1988; Traczyk 1990; Przytycki 1989; Chen-Le arXiv:math/0408358; Politarczyk 2017) [SNIPPET/abstract]; Mullins (V'(-1) and
    Casson-Walker of the double branched cover) and Garoufalidis's Casson-Walker-Lescop extension [SNIPPET via Eisermann arXiv:0802.2287].
5.3 Branch sets: no paper studies Jones polynomials of the branch sets T(1/n) (prior LIT). F1 transfers the det-1 evaluations of L_1, L_2
    through 1.3. Remark (this lane): in the osp variable u = -t, F1 reads J(-u) - 1 in (1-u^3)(1-u^4) Z[u^+-1], to be compared with
    Habiro's colour-2 factor (1-q^2)(1-q^4). No cyclotomic (Habiro-type) expansion for coloured theta-curve or knotoid invariants was
    found (one search); an intrinsic cyclotomic expansion of J would explain F1 and is a natural GAP to look at.

## 6. Pointers for the theory lanes (from the literature)
- Integral relation for arc-arc crossings: BMW/Kauffman relation of the so(3) vector R-matrix, R - R^-1 = (s - s^-1)(1 - E), exact over
  Z[s^+-1] (Turaev, Invent. Math. 92 (1988) [MEMORY]); gives the colour-2 part of F2 without Jones-Wenzl denominators. (Astra's lattice
  proof is now in the BRIEF; this is the standard citation for the same fact.)
- Huh-Jin's multilinear expansion (E1)-(E4) is a ready template for writing Delta^m as a product of local factors.
- Clark's twistor constant t^{*(K,lambda)} is a 4th root of unity depending on K and lambda: any osp(1|2) restatement of J must track it
  (it plays the role of the BRIEF's "coherent framing units").
- For F1 use Jost-Lewark Thm 1.1 (det 1 => V(e^{i pi/3}) = +1) instead of the algebraic-integer argument.

## 7. Source list
MEMORY (bibliographic data verified in Jost-Lewark's bibliography, papers not opened): Jones, Bull. AMS 12 (1985) 103-111; Lickorish-Millett,
  Comment. Math. Helv. 61 (1986) 349-359; Murakami, J. Math. Soc. Japan 38 (1986) 335-338 (Arf); Lipson, Math. Proc. Camb. Philos. Soc.
  100 (1986) 361-364 (sign at e^{i pi/3}); Rong, Indiana Univ. Math. J. 40 (1991) (Kauffman polynomial and the two-fold cover).
READ (full text or substantial grep): Manouras-Lambropoulou-Kauffman arXiv:2010.01692; Clark arXiv:1509.03533 (AGT 17 (2017));
  Blumen arXiv:0901.3232; Huh-Jin arXiv:math/0104179; Melikhov arXiv:2011.01409; Jost-Lewark arXiv:2601.16588; Masbaum
  arXiv:math/0306345 (AGT 3 (2003)); Collari-Lisca arXiv:2606.21471 (grep only).
READ (abstract page): Ebert arXiv:2210.09583; Ennes-Ramadevi-Ramallo-Sanchez de Santos hep-th/9709068; Chauhan-Ramadevi arXiv:2209.00095;
  Boyle-Issa arXiv:2101.05413; Borodzik-Dai-Mallick-Stoffregen arXiv:2507.13642; Eisermann-Lamm arXiv:0802.2283; Chen-Le
  arXiv:math/0408358; Politarczyk arXiv:1504.03462.
SNIPPET: Geer arXiv:math/0411053 (AGT 5 (2005)); Geer arXiv:0904.0408; Yasuhara arXiv:math/0104177; Taniyama arXiv:math/0106173; Koike
  (Yokohama Math. J. 47 (1999)); Dancso arXiv:0811.4615; Bar-Natan-Dancso arXiv:1103.1896; Ding-Jin-Lei-Li-Vesnin arXiv:2511.20269;
  Kricker arXiv:math/0003035; Garoufalidis-Kricker arXiv:math/0107220; Garoufalidis GT Monographs 4 (2002); Di Prisa-Framba
  arXiv:2303.08794; moth links arXiv:2412.09322; Di Prisa arXiv:2207.04985; Alfieri-Boyle arXiv:2109.09915; Boyle-Chen arXiv:2206.03598;
  Conant-Manathunga arXiv:1608.04453; arXiv:2607.18655; Murasugi PJM 131 (1988); Chbili arXiv:math/0702359; Kirk-Livingston Topology 36
  (1997); Melikhov arXiv:math/0312007; Chauhan-Ramadevi arXiv:2412.10885; Garoufalidis-Wheeler (2026, Habiro-type lift, title only).
MEMORY: Zhang (Lett. Math. Phys. 1992); Clark-Fan-Li-Wang (CMP 2014); Kulish-Reshetikhin (Lett. Math. Phys. 18 (1989)); Habiro (Invent.
  Math. 171 (2008)); Birman-Lin (Invent. Math. 111 (1993)); Turaev (Invent. Math. 92 (1988)); Stanford (Topology 35 (1996)); Kanenobu
  (JKTR 6 (1997)); Kassel-Turaev (Duke 92 (1998)); Murakami-Ohtsuki (CMP 188 (1997)); Jones (Bull. AMS 1985); Vaintrob (Math. Res. Lett. 1 (1994)); Yamada (J. Graph Theory 13 (1989)).

---- WORKING LOG (appended as I go; sections above are rewritten at the end) ----
[L1] Prior LIT lane report (../../lit/REPORT.md) already covers: J of theta(K,h) not in literature; Sakuma eta (definition);
     Watson/KWZ/Lobb-Watson/Lipshitz-Sarkar/Collari-Lisca; knotoid dictionary (Turaev; Barbensi-Buck-Harrington-Lackenby (BBHL)
     arXiv:1811.09121: knotoids in S^2 <-> strongly invertible knots via double branched cover along e_- u e_+). Not redone here.
[L2] Manouras-Lambropoulou-Kauffman, "Finite type invariants for knotoids", arXiv:2010.01692 (Eur. J. Combin., to appear per
     arXiv v2, 2021) [READ: full text grep, Secs 5, 7, 8]. Vassiliev theory of knotoids w.r.t. knotoid crossing changes.
     Spherical knotoids have NONTRIVIAL type-1 invariants (complete classification via linear chord diagrams of order one;
     examples: affine index polynomial, a universal type-1 invariant v-bar). Sec 8: Jones/bracket of a knotoid at t = e^x and
     Turaev's extended bracket T_K(A,u) at A = e^x give type-k coefficients (standard skein argument at the CLASSICAL point
     t = 1). No mention of strongly invertible knots, theta-curves or double branched covers; nothing at t = -1; no colour 2.
     TRANSLATION (this lane, elementary, CHECK-level reasoning only): via BBHL, a crossing change of a spherical knotoid
     diagram lifts to a symmetric off-axis PAIR of crossing changes of (K,h); so knotoid finite-type theory = equivariant
     finite-type theory of strongly invertible knots for OFF-AXIS moves only. On-axis crossing changes (arc twisting around the
     axis) are not knotoid crossing changes (they involve the shortcut), so F2's mixed filtration is a variant not covered.
[L3] osp(1|2) <-> sl_2 / so(3) correspondence, precise sources:
     - Clark, "Quantum osp(1|2n) knot invariants are the same as quantum so(2n+1) knot invariants", arXiv:1509.03533,
       Algebr. Geom. Topol. 17 (2017) 2961-3005 [READ: intro, Sec 2.2, Example 3.10]. Covering quantum group U_{q,pi}
       (pi^2 = 1; pi = 1: U_q(so(2n+1)) (rank 1: U_q(sl_2)); pi = -1: U_q(osp(1|2n))). Twistor (CFLW) sends pi -> -pi,
       q -> t^-1 q with t^2 = -1. THEOREM (Thms 3.8 + 4.24): for every knot K and dominant weight lambda,
       osp J^lambda_K(q) = t^{*(K,lambda)} so J^lambda_K(t^-1 q), *(K,lambda) in Z.  Ex. 3.10 (n = 1, lambda = 1, the 2-dim
       module): J^1 is the Jones polynomial in the variable tau^-1 q, i.e. (from his skein relation) Jones variable
       t_J = q^2 at pi = 1 and t_J = -q^2 at pi = -1. So in Jones variables the twistor is t_J -> -t_J, for ALL colours.
       lambda = 2 is the 3-dim (1|2) module (classical osp(1|2) fundamental) <-> sl_2 colour 2.
       Ex. 3.10 also shows the pi = -1 quasi-R-matrix on V(1) x V(1) has entry q^-1 - pi q, which is 2 (not 0) at q = 1.
     - Blumen, "On the U_q(osp(1|2n)) and U_{-q}(so(2n+1)) uncoloured quantum link invariants", arXiv:0901.3232
       [READ: abstract + intro]. Thm 1.1: Phi^{osp(1|2n)}_L(q) = F_L(-q^{2n}, q) and Phi^{so(2n+1)}_L(-q) = F_L(q^{2n}, -q),
       F_L(r,s) the BMW/Kauffman invariant; equality of the two for closures of sigma_1^m (Thm 1.2), and "up to a
       substitution of variables" for all links (Thm 1.3). Background: R.B. Zhang (Lett. Math. Phys. 1992) U_q(osp(1|2n))
       vs U_{-q}(so(2n+1)) [MEMORY]. No Vassiliev / finite-type statement (grep).
     - Ebert, "A new presentation of the osp(1|2)-polynomial link invariant and categorification", arXiv:2210.09583
       [READ: abstract page]: uncoloured U_q(osp(1|2)) invariant = U_{t^-1 q}(sl_2) invariant (t^2 = -1); Kauffman-bracket-
       like skein; categorified by a Khovanov variant with an extra Z_4-grading.
     - Ennes-Ramadevi-Ramallo-Sanchez de Santos, hep-th/9709068, Int. J. Mod. Phys. A 13 (1998) 2931-2978 [READ: abstract]:
       osp(1|2) vs su(2) polynomials related by an identification of parameters (CFT/Chern-Simons derivation).
     - Chauhan-Ramadevi, arXiv:2209.00095, Ann. Henri Poincare (2023) [READ: abstract] and arXiv:2412.10885 [SNIPPET]:
       Z-hat for SO(3) and OSp(1|2) using the same change of variables (q -> -q type).
     - Geer, "The Kontsevich integral and quantized Lie superalgebras", arXiv:math/0411053, Algebr. Geom. Topol. 5 (2005)
       1111-1139 [SNIPPET: abstract via search]: Le-Murakami equivalence (quantum group invariant = Kontsevich integral
       composed with the weight system) holds for Lie superalgebras of type A-G (osp(1|2) = B(0,1) included).
     None of these mention finite type at t = -1, theta-curves, or strongly invertible knots.
[L4] KNOT-LEVEL ANALOGUE of F2, checked (script col2_torus.py, sympy, seconds): colour-2 (spin-1) Jones J3 of T(2,n) via
     2-strand recoupling (half-twist eigenvalues t^2, -t, t^-1 on channels 0,2,4; colour-2 twist t^-2; dims [1],[3],[5]):
     J3(K; -e^h) = 1 - 24 a_2(K) h^2 + c_3 h^3 + ..., with c_3 = -6 n (n^2 - 1) = -144 (n^3 - n)/24 (degree-3 polynomial in n,
     consistent with an order-3 invariant); n = 3, 5, 7, 9, -3. CHECKED(5). By hand from Habiro's cyclotomic expansion
     (J_N(K) = sum_k C_k(K;q) prod_{j=1}^k {N+j}{N-j}, {m} = q^{m/2} - q^{-m/2}, q = t; C_k(3_1) = (-1)^k q^{k(k+3)/2},
     C_k(4_1) = 1 [MEMORY]): J3(3_1; -e^h) = 1 - 24 h^2 + ..., J3(4_1; -e^h) = 1 + 24 h^2 + ... (a_2 = 1, -1). CHECKED(2).
     Also J3 - 1 divisible by (t^2-1)(t^4-1) in all 5 torus cases (this is the k >= 1 factor {4}{2} of Habiro's expansion:
     KNOWN consequence of Habiro). Observation: [h^2] J3(K;-e^h) = -24 a_2 = 2 [h^2] J(K,h;-e^h) (since M_2 = -24 a_2).
     WHY (PROVED modulo standard identifications): the spin-1 R-matrix is the so(3) vector R-matrix (Turaev, Invent. Math.
     92 (1988); Reshetikhin) and satisfies the BMW/Kauffman relation R - R^-1 = (s - s^-1)(1 - E) as integral matrices with
     s = q_so(3) = t^{+-1} (E = cap o cup, integral). s - s^-1 vanishes at t = 1 AND at t = -1, and the kink factor
     s^{N-1} = s^2 = 1 at both. Hence the usual skein argument makes BOTH J3(K; e^h) and J3(K; -e^h) Vassiliev power
     series: at t = 1 with the so(3) weight system, at t = -1 with the osp(1|2) = so(-1) weight system (Blumen's
     F_L(-q^2, q) vs F_L(q^2, -q); Clark's twistor). I have NOT found this t = -1 statement written anywhere (see [L7]).
[L5] Sakuma's eta and Kojima-Yamasaki eta: finite-type status.
     - Melikhov, "Topological isotopy and Cochran's derived invariants", arXiv:2011.01409 [READ: intro, Thm 3, refs]:
       Cochran's derived invariants beta^i of 2-component links with lk = 0 form a rational series C_L(z) = sum beta^i z^i
       which equals the Kojima-Yamasaki eta-function under z = 2 - t - t^-1 (Cochran); his [26] = Melikhov,
       arXiv:math/0312007, extends each beta^i to a Q-valued VASSILIEV invariant of order 2i+1 of all 2-component links.
       Thm 3: -z C_L(-z^2) = Nabla_Lambda(z)/Nabla_{K_1}(z) (quotient of one-variable Conway polynomials; via
       Tsukamoto-Yasuhara). Also cites Kirk-Livingston, Topology 36 (1997) 1333-1353 (finite type for 2-component links,
       weaker sense) [SNIPPET only].
     - Sakuma's eta(K,h) is the Kojima-Yamasaki eta of the quotient link O u L (axis image, longitude image; lk = 0)
       [prior LIT report, definition READ in Mukohara arXiv:2601.02230].
     DEDUCTION (this lane; elementary, not found stated): an equivariant crossing change of (K,h) is 4 crossing changes of
     O u L (arc-arc: 4 self-crossings of L, which runs twice along the arc; on-axis: 4 crossings of L with O, in
     cancelling pairs so lk(O,L) = 0 is kept). A link invariant of order n is therefore an equivariant invariant of order
     <= n (telescoping each 4-fold change into single changes). Hence the Cochran-variable coefficients of Sakuma's eta
     are EQUIVARIANT FINITE-TYPE invariants (order <= 2i+1). Status: CONJECTURE-level until the 4-crossing dictionary
     is written carefully; it is the natural precedent for "equivariant finite type" in the literature's own invariants.
     It lives at t = 1 (Alexander-type), not at t = -1, and is abelian.
[L6] Finite-type invariants of theta-curves (all crossing changes), the closest classical relatives of F2:
     - Huh-Jin, "theta-curve polynomials and finite-type invariants", arXiv:math/0104179 (2001) [READ: full text]. Normalised
       Yamada polynomial R~_A of theta-curves (Yamada, J. Graph Theory 13 (1989); all edges effectively spin 1, loop value
       sigma = A + 1 + A^-1, skein R(+) - R(-) = (A - A^-1)(R(0) - R(inf))). THEOREM: coefficients of R~ at A = e^x are
       finite type (w.r.t. ALL crossing changes); coefficients of R~_A itself are not. Same for Yokota's polynomial.
       Their proof: R~(D|C) (sigma - sigma^2) = (-A)^m sum_delta prod_i G_i(delta) R(D_delta), with every factor G_i in
       {-(1 - A^4), -(1 - A^-2), +-(A - A^-1)}.
       OBSERVATION (this lane, PROVED by reading their proof): every such factor is divisible by (1 - A^2) = (1-A)(1+A), not
       only by (1 - A); (-A)^m and sigma - sigma^2 = -2 are harmless at A = -1. Hence the SAME proof shows that R~ at
       A = -e^x also has finite-type coefficients. Huh-Jin state only A = e^x. At A = -1 the loop value is sigma = -1 =
       sdim C^{1|2}: this is the osp(1|2) classical point for the all-spin-1 theta-curve invariant.
     - Background refs (from Huh-Jin's bibliography, MEMORY/SNIPPET): Stanford, Topology 35 (1996) 1027-1050 and JKTR 3
       (1994) 247-262 (finite type for graphs; invariants of the associated links are finite type); Kanenobu, "Vassiliev-type
       invariants of a theta-curve", JKTR 6 (1997) 455-477 (basis of type <= 3 via the associated 3-component link);
       Kauffman-Simon-Wolcott-Zhao, Topology Appl. 49 (1993) 193-216; Koike, Yokohama Math. J. 47 (1999) 245-252 (types <= 4);
       Yasuhara, "C_k-moves on spatial theta-curves and Vassiliev invariants", arXiv:math/0104177 [SNIPPET]; Taniyama,
       arXiv:math/0106173 [SNIPPET]; Kontsevich integral of trivalent graphs: Murakami-Ohtsuki (CMP 188 (1997)), Cheptea-Le,
       Dancso arXiv:0811.4615 (AGT 10 (2010) 1317-1365), Bar-Natan-Dancso arXiv:1103.1896 [SNIPPET].
     None of these restrict the crossing changes (all edges may cross), none has mixed colours (1 on two edges, 2 on one),
     none expands at t = -1, none mentions strongly invertible knots.
[L7] Roots-of-unity evaluations (inputs of F1), sharpened:
     - Jost-Lewark, "Signs of knot polynomial evaluations from a topological perspective", arXiv:2601.16588 (Jan 2026)
       [READ: intro, Thm 1.1]. Recalls (1.2): V_K(1) = V_K(e^{2 pi i/3}) = 1; V_K(-1) = (-1)^{(det-1)/2} det K;
       V_K(i) = (-1)^{Arf K}; V_K(e^{2 pi i/6}) = eps_K (i sqrt3)^{dim H_1(D_K;F_3)} [Jones 1985, Lickorish-Millett 1986].
       THM 1.1: with det K = 3^alpha q (3 not dividing q): V_K(e^{2 pi i/6}) = nu(q) (-1)^{alpha + dim H_1(D_K;F_3) +
       sum_k r_{3,k}(K)} (i sqrt3)^{dim H_1(D_K;F_3)}, nu(q) = +1 iff q = +-1 mod 12. Based on Lipson (1986) singular
       determinant delta_3(K) = eps_K. CONSEQUENCE (immediate): det K = 1 => V_K(e^{i pi/3}) = +1 exactly, and V_K(-1) = +1,
       V_K(i) = +1 (det = 1 = +-1 mod 8 => Arf = 0). So for every det-1 knot V_K - 1 is divisible by
       Phi_1^2 Phi_2 Phi_3 Phi_4 Phi_6 (degree 9). [KNOWN ingredients; the packaged divisibility I did not find stated.]
     - For F1 this REMOVES the sign case analysis ("the other option is not an algebraic integer"): V(L_1)(e^{i pi/3}) = +1
       directly (L_1 has det 1). F1's proof = classical evaluations (Jones; Lickorish-Millett; Murakami; Lipson /
       Jost-Lewark) + closure formula 1.3.
[L8] Colour 2 at q = i for knots (question (3)):
     - Habiro's cyclotomic expansion (Habiro, Invent. Math. 171 (2008) [MEMORY]; stated for twist knots in Masbaum,
       "Skein-theoretical derivation of some formulas of Habiro", arXiv:math/0306345, AGT 3 (2003) 537-556, Thm 5.1 and
       Rem 5.2 [READ]): J'_K(N) = sum_n f~_{K,n} (q^{1-N})_n (q^{1+N})_n, q = A^4, f~ in Z[q^+-1]. Every n >= 1 term contains
       (1 - q^{1-N})(1 - q^{1+N}). Hence J_K(N; q) = 1 whenever q^{N-1} = 1 or q^{N+1} = 1 (N = 2: Jones's V(1) = V(omega) = 1).
       For N = 3 (colour 2): J_K(3) - 1 is divisible by (q^2-1)(q^4-1), so J_K(3; +-1) = J_K(3; +-i) = 1 for every knot,
       and J_K(3; t) = 1 mod (t+1)^2. (KNOWN as a corollary of Habiro; I did not find the evaluation stated as such; the
       general "J_N(zeta) = 1 for zeta^{N+-1} = 1" is folklore-level.) CHECKED(5) on T(2,n) [L4].
     - Expansion at t = -1: see [L4]: J3(K; -e^h) = 1 - 24 a_2 h^2 + ..., Vassiliev (osp(1|2) weight system). Not found
       stated. Birman-Lin (Invent. Math. 111 (1993)) give Vassiliev coefficients of the Kauffman polynomial along
       a = e^{Nx}-type paths with z = e^x - e^-x [MEMORY]; with the so(3) identification and the knot parity symmetry
       F_K(-a,-z) = F_K(a,z), J3(K; -e^h) is the N = -1 ("so(-1)" = osp(1|2)) path, so the statement is a corollary of
       Birman-Lin + Turaev's so(N) identification. Experts would regard it as routine once asked.
[L9] Other symmetric-knot invariants with skein relations (precedents for equivariant finite type, none stated as such):
     - Boyle-Chen, "Negative amphichiral knots and the half-Conway polynomial", arXiv:2206.03598, Rev. Mat. Iberoam. 40
       (2024) 581-622 [SNIPPET]: Hartley-Kawauchi factor f(z) of Nabla = f(z)f(-z) normalised; EQUIVARIANT SKEIN RELATION;
       half-linking number bounds equivariant unknotting number. (Strongly negative amphichiral, not strongly invertible.)
     - Conant-Manathunga arXiv:1608.04453 and arXiv:2607.18655 (mod 4 Kawauchi conjecture) [SNIPPET]: Vassiliev invariants
       built from Conway coefficients vanishing on amphicheiral knots.
     - Collari-Lisca arXiv:2606.21471 [prior LIT READ; grep this round]: no "Vassiliev", "finite type", "quotient", "theta".
[L10] Further neighbours (question (4)/(5)):
     - Eisermann-Lamm, "A refined Jones polynomial for symmetric unions", arXiv:0802.2283 (Osaka J. Math. 48 (2011) per
       prior LIT) [READ: abstract page]: W_D(s,t), variables s for crossings ON the symmetry axis and t for symmetric pairs
       OFF the axis; W_D(t,t) = V_K, W_D(-1,t) = V_{K-}(t) V_{K+}(t). Precedent for the on-/off-axis split; no finite type.
     - Periodic links: Murasugi, Pacific J. Math. 131 (1988) (Jones of periodic link vs quotient, congruence); Traczyk
       (1990); Przytycki (1989) [SNIPPET]; Chen-Le, "Quantum invariants of periodic links and periodic 3-manifolds",
       arXiv:math/0408358 [READ: abstract; congruence modulo an ideal at roots of unity relating the link to a power of the
       quotient, per snippet]; Politarczyk, "Equivariant Jones polynomials of periodic links", arXiv:1504.03462, JKTR 26
       (2017) [READ: abstract: from equivariant Kh; skein relation; reproves Murasugi's congruence]. Chbili,
       arXiv:math/0702359 (equivariant Khovanov homology of symmetric links) [SNIPPET]. These are the "roots-of-unity
       congruences for symmetric objects" genre; none concerns strongly invertible knots' quotient theta-curves.
     - Couture / Collari-Lisca / Lobb-Watson: equivariant Jones J^e = graded Euler characteristic of the Lobb-Watson E_3
       page = Couture's polynomial [prior LIT READ]; no finite-type statement found; Khovanov-type invariants (Watson's kappa,
       KWZ, Lobb-Watson, Lipshitz-Sarkar, Borodzik-Dai-Mallick-Stoffregen arXiv:2507.13642) are not finite type and carry no
       t = -1 statements. NOTE (prior LIT): the Euler characteristic of Bar-Natan/KWZ's quotient-tangle invariant is the
       bracket vector (y, x), so J = y is (up to reduction/grading conventions) the decategorification of KWZ's invariant in
       the Q_0 coordinate; this is the only "Jones-type invariant of the quotient" in the strongly-invertible literature.
     - Equivariant signatures / concordance (Alfieri-Boyle arXiv:2109.09915; Boyle-Issa arXiv:2101.05413 butterfly links +
       Kojima-Yamasaki eta; Di Prisa-Framba arXiv:2303.08794, AGT 25 (2025) (Conway polynomial of butterfly links; moth link
       arXiv:2412.09322); Miller-Powell; Dai-Mallick-Stoffregen) [SNIPPET/abstract]: concordance-type, not finite type
       (no source claims finite type). Butterfly/moth link Conway coefficients and Kojima eta are finite-type invariants OF
       THOSE LINKS, hence plausibly equivariant finite type of (K,h) by the [L5] telescoping argument; not stated anywhere.
[L11] Low-order cross-check (sqrt_check.py, seconds): figure-eight, two inversions s.l1.y0.y0.x1.u2 and s.l1.x0.x0.y1.u2:
     J1 J2 - J3(4_1) = -(t-1)^2 (t+1)^4 (t^2+1)(t^2-t+1) Phi_10 / t^7, i.e. J1 J2 = J3(4_1) mod (t+1)^4
     (J1(-e^h) = 1 + 12h^2 - 30h^3 + ..., J3(4_1)(-e^h) = 1 + 24h^2 + 0h^3 + ...). General statement (PROVED from
     M_1 = 0, M_2 = -24 a_2 (BRIEF) and [L4]): J(K,h)^2 = J3(K) mod (t+1)^3 for every (K,h). No identity beyond order 2
     is expected (order-3 terms: M_3 = 36(7 v_3 + 5 iota) vs a multiple of v_3 for J3).
