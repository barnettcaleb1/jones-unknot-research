# Eight-route theory batch: seven route builds, seven hostile referees, synthesis

- Workflow: wf_2f8f87e8-37a (jones-eight-routes-wf_2f8f87e8-37a.js)
- Session: bridge session (Claude-Codex integrator)
- Launched (script written): 2026-11-03 11:52 local; journal last written: 2026-11-03 13:21 local
- Agents started: build:circle-graphs, build:symplectic, build:habiro, build:arithmetic, build:statmech, build:representations, build:gauge, build:minimal, ref:gauge, ref:circle-graphs, ref:arithmetic, ref:statmech, ref:representations, ref:minimal, ref:symplectic, synthesize
- Results extracted here: build:gauge, build:circle-graphs, build:arithmetic, build:statmech, build:representations, build:minimal, build:symplectic, ref:gauge, ref:circle-graphs, ref:arithmetic, ref:representations, ref:symplectic, ref:minimal, ref:statmech, synthesize
- Started but returned no result: build:habiro
- Context: Launched 3 Nov 11:52 after the 10:30/10:41 redirects (novel cross-field routes). Board summary: SCAFFOLD.md 13:31 entry ('EIGHT-ROUTE BATCH CLOSED: seven routes built, all seven killed by their referees') and STATUS.md 13:31. The Habiro builder died on the output cap and returned nothing. Full route statements, mechanisms, referee kills and the synthesis exist only in the journal.
- Provenance: contemporaneous agent outputs recorded in the workflow journal (runtime state, not copied). Text below is verbatim except formatting (JSON fields rendered as markdown), em dashes replaced by ' - ', email addresses redacted, and home-directory paths shortened to ~ (session scratchpad roots to <scratch>). These are internal AI agent outputs, not external review; statuses are as the agent stated them at the time and may be superseded by later board entries.


## Agent: build:gauge


### route_title

SU(2)/pillowcase route: Jones as a graded Casson-Lin count

### candidate_statement

Setup. Every knot is K = T ∪ T_0 with T_0 the trivial 2-tangle (cut out a ball around an arc) and T = K minus that ball. Let P be the pillowcase (traceless SU(2) character variety of the 4-punctured sphere), R(T_0) ⊂ P the arc of the trivial tangle, and BN~(T) the Kotelskiy-Watson-Zibrowius immersed multicurve in S^2_{4,*}, which realizes Hedden-Herald-Hogancamp-Kirk's twisted complex of traceless character varieties of the elementary tangles of T; conjecturally (Cazassus-Herald-Kirk-Kotelskiy, Herald-Kirk) it is the earring-correspondence image of the honest variety R(T).

Bridge (J), a theorem (HHHK + KWZ gluing, universal coefficients): V_K(t) = Σ_{x ∈ BN~(T) ⋔ R(T_0)} (−1)^{h(x)} t^{q(x)/2}, a sum over earring-perturbed traceless SU(2) representations of K bigraded by Floer data. By KWZ linearity every component c is rational (embedded, slope p_c/q_c, local system rank n_c) or special s_n(p/q), so V_K(t) = Σ_c ε_c n_c t^{a_c} Φ_c(t), with Φ_c = V_{S(p_c,q_c)} (2-bridge Jones polynomial: alternating signs, no gaps) for rational c and an explicit special polynomial Ψ_{p/q} for special c.

Candidate C (two-sided extreme sign coherence). For every knot K, the representations x of minimal q-grading all have the same sign (−1)^{h(x)}, and likewise those of maximal q-grading. Equivalently: span V_K equals the q-span of Khr(K;Q) (t = q^2 convention) and the extreme coefficients of V are ± the extreme ranks.

C ⟹ T: V_K = 1 forces q-span of Khr(K;Q) = 0, so Khr lives in one column, which is then sign-coherent; hence rank Khr = |V_K(1)| = 1 and K = U by Kronheimer-Mrowka. Class version: for tangles whose multicurve has no special components, every summand is δ-thin and C reduces to an ordering statement on the shifts a_c of rational components.

### mechanism

(i) V reaches SU(2) geometry exactly once: as the graded Euler characteristic of Lagrangian Floer theory in P whose Lagrangians are built from traceless character varieties (HHHK). KM's irreducible traceless representation of a nontrivial knot is what makes rank Khr ≥ 2 (via I^♮), and in the earring picture the extra generators are literally irreducible traceless representations. (ii) Linearity kills intra-component cancellation: a component lifts to a straight line in the planar cover, R(T_0) lifts to a periodic family of parallel segments, so intersection gradings along a component form an arithmetic progression (constant δ = q − 2h for rational c; two adjacent diagonals for special c). Cancellation in χ_q can therefore only occur between distinct components, and the extreme degrees are governed by the component(s) with extremal shift, a finite geography problem (KWZ geography restrictions). (iii) Evidence: for A- or B-adequate diagrams the extreme column is Z (Khovanov, Patterns I), so one side of C holds on exactly the adequate/alternating/semi-adequate classes where T is known; thin knots satisfy both sides. (iv) C uses the whole Laurent polynomial (each coefficient as a signed count, exponent range as grading range), as the global-only principle demands.

### why_not_excluded

Not a sieve: C involves no evaluation at a root of unity and no congruence; it is a statement about exponent range (span V versus q-span of Khr), the global data licensed by (1)-(2). Not a reformulation: C is logically independent of T (it can fail for knots with V ≠ 1, and T could hold while C fails); its proof would give T as a corollary of KM, not restate it. Not (4): no Temperley-Lieb width ladder, no strongly invertible or Sakuma frame, no finite computation. It overlaps (5) only in the target column; here that column is organized by pillowcase geometry (components, slopes, shifts, local systems) rather than by Lando graphs, giving a different handle (slope ordering ⟹ shift ordering) on sign coherence. The degree bounds (3) are consistent: Jones's braid bounds are the N = 2 shadow of the same filtration.

### obstacle

(a) Gauge theory supplies existence, never signs. Every signed count of SU(2) representations vanishes on Alexander-trivial knots: Casson-Lin (traceless meridian) = σ/2; Herald and Heusener-Kroll (tr m = 2cos α) = Tristram-Levine σ_ω; so no count detects the unknot, KM's theorem is a rank statement, and V is a count. The three channels by which SU(2) data reach V are exhausted: (α) evaluations with 2 + t + t^{-1} ∈ {0,1,2,3,4} (Potts/Beraha; Lickorish-Millett; Jones) give |H_1(Σ_2;Z_2)|, the Z_3-rank, Arf: dihedral/metabelian data, sieves by (1); (β) Witten's Wilson loop at level k → ∞ with color N = 2 localizes on the unique flat connection of S^3 (Rozansky; Melvin-Morton; Bar-Natan-Garoufalidis), i.e. finite type; the KM representations sit at color N ≈ k/2 (Gukov's generalized volume conjecture), inside the colored Jones, not V. Indeed KM ⟹ A-polynomial nontrivial (Dunfield-Garoufalidis; Boyer-Zhang) ⟹ via AJ (Garoufalidis; Le; Le-Tran) the colored Jones function detects the unknot, using all colors. Astra's D_G: at A = −1 the skein module of the exterior surjects onto C[X(E_K)] (Bullock; Przytycki-Sikora), but V is a pairing in K(S^3) = Z[A^{±}], where X(E_K) acts only through the core; D_G enters only through the peripheral ideal, i.e. the colored Jones. Dead at N = 2. SL_2(F_q): Kuperberg derives small-p nonabelian SL_2(F_p) representations from KM, but their counts (quandle colorings by the traceless class; p = 2 gives Fox 3-colorings) have no Jones expression beyond (α). (γ) Only categorification carries the full polynomial, and there the whole difficulty is the sign problem C.
(b) C is probably false in general: at a diagram's all-A degree the extreme Kh column is H̃_*(Ind(Lando circle graph)) (GMS), and circle-graph independence complexes are expected to be wedges of spheres of mixed dimensions (Przytycki-Silvero); a knot diagram with χ̃ = 0 but H̃ ≠ 0 at the knot's extreme degree gives a Khr column outside the span of V, refuting C for that knot.
(c) Known gap, stated sharply: KM plus Lee's (1,4)-pairing give q-span of Khr(K;Q) ≥ 4 for K ≠ U, while T is equivalent to span V ≥ 3 (item 2). The route reduces T to closing exactly this Euler-characteristic gap, which is Khovanov-combinatorial, not gauge-theoretic. The CHKK identification of BN~(T) with the earring image of R(T) is unproved beyond small tangles, but (J) holds unconditionally, so that is not what blocks the route.

### first_lemma

Lemma A (component thinness and locality of cancellation). For any 4-ended tangle T and the trivial arc R(T_0): each rational component r_n(p/q) of BN~(T) contributes to Khr(T ∪ T_0; F_2) a summand isomorphic, up to bigrading shift and n-fold multiplicity, to Khr(S(p,q)), hence δ-thin; each special component contributes a summand supported on exactly two adjacent δ-diagonals. Consequently V_K(t) − 1 = Σ_{c ≠ c_0} ε_c n_c t^{a_c} Φ_c(t), c_0 the component carrying the Lee survivor, and any cancellation in V_K is between distinct components.
Sketch: KWZ linearity gives a lift of c homotopic to a straight line L in the planar (peg-board) cover of S^2_{4,*}, punctures lifted to a lattice; R(T_0) lifts to a periodic family of parallel segments; in minimal position L meets them at equally spaced points, and KWZ's grading recipe (bigrading from winding of the lift against the two lattice generators) assigns consecutive points bidegree steps (±1, ±2), i.e. constant δ. The rational case is the HHK/KWZ 2-bridge computation. For a special curve the singular representative passes the special puncture, so the lift consists of two parallel strands joined at the puncture, producing two diagonals.
Lemma B (the decisive test of C). For the two-component example BN~(P(2,−3)) = r(1/2) ⊔ s(0) (KWZ) closed by arcs of all slopes n, show that the extreme-q intersection points of the two components never share a q-grading with opposite sign, and identify the structural reason (slope ordering of components forces ordering of extreme shifts a_c + mindeg Φ_c); if instead opposite-sign extreme points occur for some n, C is refuted and the route collapses into route (5).

### literature

  - Kronheimer-Mrowka, Dehn surgery, the fundamental group and SU(2), Math. Res. Lett. 11 (2004), arXiv:math/0312322; Witten's conjecture and Property P, Geom. Topol. 8 (2004), arXiv:math/0311489
  - Kronheimer-Mrowka, Khovanov homology is an unknot-detector, Publ. IHES 113 (2011), arXiv:1005.4346
  - Lin, A knot invariant via representation spaces, J. Diff. Geom. 35 (1992); Herald, Flat connections, the Alexander invariant, and Casson's invariant, Comm. Anal. Geom. 5 (1997); Heusener-Kroll, Deforming abelian SU(2)-representations of knot groups, Comment. Math. Helv. 73 (1998)
  - Hedden-Herald-Kirk, The pillowcase and perturbations of traceless representations of knot groups, Geom. Topol. 18 (2014), arXiv:1301.0164
  - Hedden-Herald-Hogancamp-Kirk, The Fukaya category of the pillowcase, traceless character varieties, and Khovanov cohomology, Trans. AMS 373 (2020), arXiv:1808.06957
  - Kotelskiy-Watson-Zibrowius, Immersed curves in Khovanov homology, arXiv:1910.14584; Thin links and Conway spheres, arXiv:2105.06308; Khovanov multicurves are linear, arXiv:2202.01460
  - Cazassus-Herald-Kirk-Kotelskiy, The correspondence induced on the pillowcase by the earring tangle, J. Topol. 15 (2022), arXiv:2010.04320; Herald-Kirk, An endomorphism on immersed curves in the pillowcase, arXiv:2407.11247
  - Gukov, Three-dimensional quantum gravity, Chern-Simons theory, and the A-polynomial, Comm. Math. Phys. 255 (2005), arXiv:hep-th/0306165; Rozansky, A contribution of the trivial connection to the Jones polynomial, arXiv:hep-th/9401061
  - Dunfield-Garoufalidis, Non-triviality of the A-polynomial for knots in S^3, Algebr. Geom. Topol. 4 (2004), arXiv:math/0405353; Boyer-Zhang, Every nontrivial knot in S^3 has nontrivial A-polynomial, Proc. AMS 133 (2005); Le, The colored Jones polynomial and the A-polynomial of knots, Adv. Math. 207 (2006), arXiv:math/0407521; Le-Tran, On the AJ conjecture for knots, Indiana Univ. Math. J. 64 (2015), arXiv:1111.5258
  - Kuperberg, Knottedness is in NP, modulo GRH, Adv. Math. 256 (2014), arXiv:1112.0845
  - Bullock, Rings of SL_2(C)-characters and the Kauffman bracket skein module, Comment. Math. Helv. 72 (1997); Przytycki-Sikora, On skein algebras and SL_2(C)-character varieties, Topology 39 (2000)
  - Lickorish-Millett, Some evaluations of link polynomials, Comment. Math. Helv. 61 (1986); Jones, Hecke algebra representations of braid groups and link polynomials, Ann. Math. 126 (1987)
  - Przytycki-Silvero, Homotopy type of circle graph complexes motivated by extreme Khovanov homology, J. Algebraic Combin. 48 (2018), arXiv:1608.03002; Khovanov, Patterns in knot cohomology I, Experiment. Math. 12 (2003); Lee, An endomorphism of the Khovanov invariant, Adv. Math. 197 (2005)

### verdict

doubtful

### confidence

Medium. Bridge (J) and Lemma A are essentially theorems (HHHK, KWZ) and sharply localize T to inter-component cancellation; but candidate C likely fails in general (mixed-dimension circle-graph complexes), and gauge theory itself supplies no sign mechanism: every SU(2) channel into V other than categorification is a sieve (Beraha evaluations) or finite type (trivial-connection expansion), and the KM representations live in the colored Jones at N ≈ k/2, not in V.


## Agent: build:circle-graphs


### route_title

Extreme coefficients via Lando-graph independence complexes: diagrammatic realization of the Jones extreme degree

### candidate_statement

Notation (convention: the A-smoothing of a positive crossing is its oriented smoothing; otherwise swap A/B). For a knot diagram D: c_± = numbers of positive/negative crossings, s_A, s_B = circles of the all-A/all-B states, G_A(D), G_B(D) the Lando graphs (self-chords of the state circles, adjacent iff interlaced; circle graphs), I(G) the independence complex, I(G;-1) = sum over independent sets S of (-1)^|S| = -reduced Euler characteristic of I(G). Potential extreme degrees in t: p_A(D) = (c_+ - 2c_- - s_A + 1)/2, p_B(D) = (2c_+ - c_- + s_B - 1)/2; p_B - p_A = c(D) - g_T(D) >= c(D)/2.

Facts. (Bae-Morton 2003) min deg V_K >= p_A(D), with equality iff I(G_A(D);-1) != 0, the extreme coefficient then being ±I(G_A(D);-1); dually at B. (Gonzalez-Meneses-Manchon-Silvero 2018, Thm 4.4) Kh^{*, j_min(D)}(K) = reduced homology of I(G_A(D)) up to shift; so by invariance every Lando complex of every diagram is either acyclic or computes the extreme Khovanov group of K.

Conjecture R (one-ended realization). Every nontrivial knot K has a diagram D and an end E in {A,B} with I(G_E(D);-1) != 0 and p_E(D) != 0. Equivalently: max_D p_A(D) = min deg V_K != 0, or min_D p_B(D) = max deg V_K != 0.

R implies T: V_K = 1 forces both extreme degrees to be 0, so any sharp end has p_E(D) = 0.

Class theorem (immediate): T holds on the class of knots satisfying R, which contains positive knots (the Seifert state has no self-chord, so G_A is empty and p_A = g(K) >= 1), semiadequate knots with p_E != 0 at the adequate end, and the negative-forest diagrams of the first lemma with g_c(D) != c_-(D).

Two caveats fix the form. The two-ended version "some diagram has span V_K = c(D) - g_T(D)" is false: T(5,6) has span 9 < 12 <= c/2 <= c(D) - g_T(D) for every diagram. And the clause p_E != 0 cannot be dropped: p_E = 0 with coefficient ±1 is consistent with V = 1, so for p_E = 0 one needs R': the almost-extreme coefficient is nonzero (Stoimenow's Theorem 4.1 does exactly this for adequate ends).

### mechanism

(i) R is a statement about the exponent range of V, precisely the global information principle (1) demands; it packages Jones's degree bound with an exact sharpness criterion.

(ii) GMS rigidity makes sharpness a homological dichotomy rather than a coincidence of cancellations: a diagram's Lando complex is acyclic unless the diagram realizes j_min(Kh(K)). Under the Przytycki-Silvero conjecture (proved for bipartite circle graphs, arXiv:2302.02527; for 4-braid Lando graphs, arXiv:2305.18648; for permutation graphs and non-nested families, arXiv:1608.03002) realizing complexes are wedges of spheres and I(G;-1) = ±(#even-dimensional - #odd-dimensional spheres), so Jones-sharpness fails only by exact parity cancellation.

(iii) Non-adequate ends can be sharp, which is what separates n = 1 from the colored case. First lemma: the all-A Lando graph of an almost positive diagram whose negative crossing has k >= 1 parallel positive crossings is the star K_{1,k}; I(K_{1,k}) is S^0, I(G;-1) = -1, so min deg V = g_c(D) - 1 with coefficient ±1 (Stoimenow's almost-positive theorem recovered by chord combinatorics). Interlacing single chords (K_2, stars, joins of stars) have nonzero I(G;-1); cabled chords do not (n parallel copies of a self-chord are mutually non-interlaced and cone off the complex), which is exactly why Lee 2018 and Kalfagianni-Lee 2023 get "sharp iff adequate" for colored Jones while the uncolored route has room.

(iv) A Jones-trivial K would need I(G_A(D);-1) = 0 for every diagram with p_A(D) < 0 and I(G_A(D);-1) = ±1 for every diagram with p_A(D) = 0, a rigid pattern across all diagrams that explicit families (lemma, part 3) can be played against.

### why_not_excluded

No congruence, no finite set of evaluations, no finite-type coefficient: a degree-plus-leading-coefficient statement is blind to the Eliahou-Fromentin (V = 1 mod 2^r) and Aiello-Baader-Ferretti examples, all of which have nonzero span. It is not (3): Jones's braid bound (e-n+1)/2 is a Temperley-Lieb estimate with no sharpness criterion, whereas p_E(D) is a state-sum bound with one (I(G_E;-1) != 0), and it applies to every diagram, not only closed braids. It is not a reformulation of T: R is strictly stronger (R implies T; T implies R is unknown, since a knot with V != 1 whose extreme degree is realized by no diagram would refute R without touching T), so R is independently falsifiable, and the degree gap gamma_A(K) = min deg V_K - max_D p_A(D) >= 0 is a diagram-free invariant not on the board. Nothing here uses the parked Lemma-Q frame, width ladders, single-level TQFT pairings, or finite-case computation.

### obstacle

No monotonicity. Under Reidemeister moves p_A never increases (positive R1: unchanged; negative R1: drops by 1 and adds an isolated vertex, so I(G_A) becomes a cone; R2: unchanged or drops by 1), so max_D p_A(D) is attained, but no canonical diagram (minimal crossing, Turaev-genus-minimizing, c_- -minimizing) is known to be sharp, and the lemma shows sharpness depends on cyclic orders of crossings around Seifert circles, which is why no "move that increases I(G;-1)" is in sight. The colored analogue is a warning: for n >= 2 the potential extreme coefficient of J_K(n) vanishes for every non-A-adequate diagram (Lee, arXiv:1611.00686; Kalfagianni-Lee: Jones diameter = 2c(K) iff adequate, arXiv:2108.12391), so beyond semi-adequacy sharpness at n = 1 is an exception a proof must manufacture. The two-ended version is false (torus knots), so R gives no span bound; when the realized end has p_E = 0 one needs the almost-extreme coefficient, whose Lando-type description (Przytycki-Silvero, Geom. Dedicata 2020) exists only for adequate ends. Even Khovanov-level realization ("some diagram realizes j_min(Kh K)") is open, and a Jones-trivial K would by GMS have every realizing Lando complex non-acyclic with zero Euler characteristic, a mixed-parity wedge; Przytycki-Silvero show such Lando graphs exist (I(G) = S^n v S^{2n-1}), so no parity argument on circle graphs alone excludes them. Net: the route proves T on an explicit, extendable class and produces a new invariant, but offers no mechanism for an arbitrary knot.

### first_lemma

Lemma (negative-forest Lando structure). Let D be a knot diagram with Seifert graph Gamma (vertices = the s Seifert circles, edges = crossings, signed), N = negative crossings, P = positive crossings parallel to some edge of N (joining the same two circles). Assume (a) N is a forest in Gamma; (b) every positive crossing joining two circles of the same component of (V(Gamma), N) lies in P. Then:
(1) s_A = s - |N| and p_A(D) = g_c(D) - |N|, where g_c = (c - s + 1)/2 is the canonical genus.
(2) G_A(D) has vertex set N u P; each x in N is adjacent exactly to its parallels; the parallels of x are pairwise non-interlaced (nested); chords of distinct x, x' in N never interlace; and y parallel to x, z parallel to x' interlace iff x, x' share a Seifert circle C and the four sites occur on C in cyclic order (x, x', y, z) up to rotation and reversal.
(3) Hence: if some x in N has no parallel, I(G_A) is a cone (D not A-sharp). If every x has a parallel and no cross-interlacing occurs, I(G_A) = join of |N| copies of S^0 = S^{|N|-1}, I(G_A;-1) = ±1, so min deg V_K = g_c(D) - c_-(D) with extreme coefficient ±1 (|N| = 1 is Stoimenow 2005). A fully cross-interlaced chain gives a tree with a pendant N-vertex whose fold isolates the next N-vertex, so I(G_A) is contractible: sharpness is governed by cyclic order, which flypes can change.
Sketch. The all-A state is the Seifert state resmoothed non-orientedly at N; the Seifert state has no self-chord (two co-oriented parallel arcs of one oriented Jordan curve would have the region between them both interior and exterior), and (a) makes each resmoothing a merge, giving (1). Traverse the merged circle of a tree component: C_1-part, x_1-site, C_2-segment, x_2-site, ...; parallels of x have one endpoint on each side of x, in reverse order on the two sides (nested); chords of x' != x lie on one side of x; reading the cyclic word on a shared circle yields the four-site criterion. Sanity check on the braid word s_1^3 s_1^{-1}: G_A = K_{1,3}, p_A = 1/2 = min deg V(positive Hopf). Homotopy types from Engstrom's fold lemma, the pendant-vertex suspension I(G) = Sigma I(G - N[w]), and I(G u H) = I(G) * I(H).
Next use: compute gamma_A, gamma_B on the first non-A-adequate knots (Lee cites 12n706) by looking for diagrams satisfying (3); a knot with both gaps positive refutes R and closes the route, otherwise relax (b) to allow long positive chords (cycles in G_A; Kozlov's I(C_n)) and look for a flype that removes cross-interlacing.

### literature

  - Y. Bae, H. R. Morton, The spread and extreme terms of Jones polynomials, J. Knot Theory Ramif. 12 (2003), arXiv:math/0012089
  - P. M. G. Manchon, Extreme coefficients of Jones polynomials and graph theory, J. Knot Theory Ramif. 13 (2004)
  - J. Gonzalez-Meneses, P. M. G. Manchon, M. Silvero, A geometric description of the extreme Khovanov cohomology, Proc. Roy. Soc. Edinburgh A 148 (2018), arXiv:1511.05845
  - J. H. Przytycki, M. Silvero, Homotopy type of circle graph complexes motivated by extreme Khovanov homology, J. Algebraic Combin. 48 (2018), arXiv:1608.03002
  - J. H. Przytycki, M. Silvero, Geometric realization of the almost-extreme Khovanov homology of semiadequate links, Geom. Dedicata (2020)
  - J. H. Przytycki, M. Silvero, Khovanov homology, wedges of spheres and complexity, arXiv:2305.18648 (2023)
  - On bipartite circle graphs and Khovanov homology, arXiv:2302.02527 (2023); Independence complexes of circle graphs, arXiv:2412.01125 (2024)
  - A. Engstrom, Complexes of directed trees and independence complexes, Discrete Math. 309 (2009); R. Ehrenborg, G. Hetyei, The topology of the independence complex, European J. Combin. 27 (2006); D. Kozlov, Complexes of directed trees, J. Combin. Theory A 88 (1999); J. Barmak, Star clusters in independence complexes of graphs, Adv. Math. 241 (2013), arXiv:1007.0418
  - A. Stoimenow, On polynomials and surfaces of variously positive links, J. Eur. Math. Soc. 7 (2005), arXiv:math/0202226
  - A. Stoimenow, Non-triviality of the Jones polynomial and the crossing numbers of amphicheiral knots, arXiv:math/0606255 (Thm 4.1, semiadequate links)
  - C. R. S. Lee, A trivial tail homology for non A-adequate links, Algebr. Geom. Topol. 18 (2018), arXiv:1611.00686
  - E. Kalfagianni, C. R. S. Lee, Jones diameter and crossing number of knots, Adv. Math. 417 (2023), arXiv:2108.12391
  - O. Dasbach, D. Futer, E. Kalfagianni, X.-S. Lin, N. Stoltzfus, The Jones polynomial and graphs on surfaces, J. Combin. Theory B 98 (2008), arXiv:math/0605571

### verdict

doubtful

### confidence

Medium. About 0.9 that R implies T, that the two-ended version fails (torus knots), and that lemma parts (1)-(3) hold as stated (the four-site interlacing criterion was derived by hand on the cyclic word, not machine-checked). About 0.15 that R is provable for all knots by any mechanism visible from here. The salvageable output is the class theorem, the degree-gap invariant gamma_A, gamma_B, and the lemma.


## Agent: build:arithmetic


### route_title

Arithmetic rigidity: dead for V alone; survives only as Burau_4 trace rigidity for closed 4-braids

### candidate_statement

Negative part (precise): no theorem of the form "V_K congruent to 1 in a global arithmetic sense implies V_K = 1" can prove T (two-invariant principle, see mechanism). Surviving candidate (C4), equivalent to T for braid index <= 4: let rho_n be the reduced Burau representation, pi: B_4 -> B_3 the homomorphism sigma_1, sigma_2, sigma_3 -> sigma_1, sigma_2, sigma_1, and for beta in B_4 with exponent sum e set D'_beta(t) := (1 + (-t)^e - tr rho_3(pi beta))/(1+t+t^2) in Z[t^{+-1}] (Burau-normalized Alexander polynomial of the auxiliary 3-braid link closure(pi beta)). If beta has 4-cycle permutation and tr rho_4(beta) = c_e(t) + t*D'_beta(t), with c_3 = t^2 - 2t and c_1 = 1 - t - t^{-1} (mirror images for e = -1, -3), then closure(beta) is the unknot. By Lemma A this hypothesis is exactly V = 1 for closure(beta) (Jones's bound (3) forces e in {+-1, +-3}), so (C4) is equivalent to "V detects the unknot among closed 4-braids", which is open (Korzun-Lanina-Sleptsov 2025) and is the first braid index where (Delta, V)-non-injectivity is not governed by Datta's quadratic class numbers.

### mechanism

Why V-alone arithmetic is dead. (i) Two-invariant principle: any property P of integer Laurent polynomials with P(V_K) for all knots satisfies P(1); so heights, Mahler measure, Res(V-1, Phi_r), Galois norms and Habiro-ring integrality of V alone are sieves, never proofs. (ii) No gap: V - 1 = H_1 t^{-2}(t-1)^2(t^2+t+1) with H_1(4_1) = 1 and H_1(3_1) = -t^{-+2}; the target "H_1 nonzero" sits next to realized unit-height values, and for primes p >= 5, |Res(V-1, Phi_p)| = p^2 |N_{Q(zeta_p)/Q}(H_1(zeta_p))| is merely a norm of H_1. (iii) Per level, Freedman-Larsen-Wang density (r = 5, r >= 7) plus Galois closure make each level's value set as large as integrality permits, and "V(zeta_r) = 1 for infinitely many r" is literally V = 1 (phi(r) > span). Arithmetic can bite only through a relation R(V_K, X_K) with a second invariant X that determines K. Faithfulness of rho_4 (Bharathram-Birman-Brendle 2026) makes X = rho_4(beta) such an invariant for braid index 4 and closes Bigelow's (2002) only known source of 4-braid counterexamples. Lemma A: generic TL_4 has irreps W_4, W_2, W_0 (dims 1, 3, 2) with Markov weights [5], [3], 1; W_2 = A^e (x) rho_4 and W_0 = A^e (x) pi^* rho_3 (T_3 -> T_1 is an algebra map H_4 -> H_3 killing the TL ideal, and the pulled-back 2-dimensional module is irreducible). So V = 1 for closure(beta) is a single identity in Z[t^{+-1}]: [3] tr rho_4(beta) + tr rho_3(pi beta) = R_e(t), span R_e <= 4. Rigidity: Datta (arXiv:2209.10826) reads the entries of rho_4(g), hence the extreme-degree terms of tr rho_4(g), off the Garside normal form, with cancellation only in an explicit exceptional family; the rho_3 image is explicit. The identity forces total cancellation of [3] tr rho_4(beta) + tr rho_3(pi beta) outside a degree window of width 4, which should bound inf and sup of the normal form of beta by those of pi beta, leaving only exchange-move orbits of unknotted braids (infinite by Morton 1983; consistent, since tr rho_4 is not exchange-move invariant, only the combination is). Squier unitarity (s_2 = (-t)^e tr rho_4(beta)(t^{-1})) adds, for V = 1 and e = 3: Delta_closure(beta) = 1 - (t D' + t^2 D'(t^{-1}))/((1+t)(1+t^2)), hence D'(i) in (1-i)Z, a Datta-type arithmetic fingerprint of the auxiliary 3-braid link.

### why_not_excluded

(C4) is an identity in Z[t^{+-1}] whose content is the exponent range and every coefficient of two Burau traces: not a congruence, not a finite set of root-of-unity evaluations, not finitely many Vassiliev coefficients; the degree bound (3) is used only to restrict e. Braid index 4 is strictly beyond Stoimenow's 3-braid theorem and is open (KLS 2025); Bigelow's counterexample mechanism needed an unfaithful rho_4, now excluded. It is not the parked Lemma Q frame, not the TL width ladder (it uses matrix entries of rho_4, not module widths), not single-level TQFT pairing, not Carmi-Cohen degree growth, and not a finite-case computation. (2) is not re-derived: H_1 = 0 is rewritten as trace data.

### obstacle

(a) Korzun-Lanina-Sleptsov (AIHPD 2025, arXiv:2402.02553) show that character-level data for 4-braids, even all five H_4 characters (full HOMFLY-PT), leave a writhe-indexed one-parameter family of hypothetical polynomials compatible with V = 1. So Lemma A alone cannot close (C4); the required input is entry-level control of rho_4(beta), which Datta supplies only "almost everywhere", and the exceptional braids where entry cancellation occurs are exactly where a counterexample could hide. (b) tr rho_3(pi beta) is not an arithmetic function of the matrix rho_4(beta): pi is a homomorphism of B_4 invisible in GL_3(Z[t^{+-1}]), and the image of rho_4 is not cut out by unitarity (Lee 2024 answers Salter's question negatively). Hence no Latimer-MacDuffee-Taussky/class-number statement about conjugacy classes of rho_4(beta) with fixed characteristic polynomial decides (C4); Datta's philosophy transfers only as a count of (Delta, V)-collisions. (c) The solution set is infinite (exchange-move orbits of unknotted 4-braids, Morton's irreducible examples), so the rigidity must be orbit-wise and needs Birman-Menasco MTWS for 4-braids: a "4-braid Stoimenow" of real length, yielding only the braid-index-4 case of T with no visible induction on n (pi has no TL-compatible analogue for n >= 5). (d) Conventions in Lemma A (t = A^{-4}, Burau normalization of D') were checked on three braids by hand only and must be matched against Jones 1987 Section 8 and KLS.

### first_lemma

Lemma A (prove and cross-check first). For beta in B_4 with exponent sum e, t = A^{-4}, [k] = (t^{k/2} - t^{-k/2})/(t^{1/2} - t^{-1/2}): (-1)^{e+1} t^{-e/2} [2] V_closure(beta)(t) = [5] + [3] tr rho_4(beta)(t) + tr rho_3(pi beta)(t). Consequently, for 4-cycle beta with V = 1: e in {+-1, +-3}; e = 3 gives tr rho_4(beta) = t^2 - 2t + t D'_beta; e = 1 gives tr rho_4(beta) = 1 - t - t^{-1} + t D'_beta; and for e = 3, Delta_closure(beta) = 1 - (t D'(t) + t^2 D'(t^{-1}))/((1+t)(1+t^2)). Sketch: generic TL_4 = End W_4 + End W_2 + End W_0; the bracket of a closure is the Markov trace sum_k Delta_k(delta) tr_{W_k} with Chebyshev Delta_k and delta = -[2], giving weights [5], [3], 1. On each W_k, sigma_i -> A + A^{-1} e_i with e_i of rank <= 1, so sigma_i has eigenvalues A and -A^{-3} = A(-t); uniqueness of the generic 3- and 2-dimensional irreps gives W_2 = A^e (x) rho_4 and W_0 = A^e (x) pi^* rho_3. Normalize V = (-A^3)^{-e} <closure(beta)>/delta. Hand checks: beta = sigma_1 gives A^9 + 3A^5 + 3A + A^{-3} = A^3 [2]^3 (3-component unlink); beta = sigma_1 sigma_2 sigma_3: rho_4-eigenvalues t{i, -1, -i} (from (sigma_1 sigma_2 sigma_3)^4 = full twist -> t^4 I, det = -t^3, Burau's formula det(I - rho_4) = (1+t)(1+t^2)), trace -t, and tr rho_3(sigma_1 sigma_2 sigma_1) = 0 (rho_3(Delta_3)^2 = t^3 I, det -t^3), so V = 1 holds; beta = sigma_1 sigma_2 sigma_3^{-1}: the formula forces tr rho_4 = 1 - t - t^{-1}, and Burau's formula then returns Delta = t^{-1}. The Alexander relation uses Squier unitarity. Lemma B (first genuinely new target): if V = 1 then the maximal and minimal degrees of [3] tr rho_4(beta) and of tr rho_3(pi beta) coincide, with opposite extreme coefficients, whenever they lie outside [-2, 2]; combine with Datta's normal-form description of the extreme-degree entries of rho_4 (2209.10826) and the explicit rho_3 image to bound inf and sup of the Garside normal form of beta by those of pi beta plus a constant. Test on Morton's irreducible unknotted 4-braids and on the exchange-move orbit of sigma_1 sigma_2 sigma_3 before attempting the general case.

### literature

  - Jones, Hecke algebra representations of braid groups and link polynomials, Ann. Math. 126 (1987): degree bounds; 3- and 4-braid trace formulas
  - Birman, On the Jones polynomial of closed 3-braids, Invent. Math. 81 (1985)
  - Stoimenow, Coefficients and non-triviality of the Jones polynomial, J. reine angew. Math. 657 (2011), arXiv:math/0606255
  - Datta, A novel connection between integral binary quadratic forms and knot polynomials, arXiv:2204.13660 (2022)
  - Datta, A strong characterization of the entries of the Burau matrices of 4-braids: the Burau representation of B_4 is faithful almost everywhere, arXiv:2209.10826 (2022)
  - Bharathram-Birman-Brendle, The Burau representation of the braid group is faithful for n = 4, arXiv:2607.05283 (2026)
  - Bigelow, Does the Jones polynomial detect the unknot?, J. Knot Theory Ramif. 11 (2002), arXiv:math/0012086
  - Ito, A kernel of a braid group representation yields a knot with trivial knot polynomials, Math. Z. 280 (2015), arXiv:1402.2028
  - Korzun-Lanina-Sleptsov, Closed 4-braids and the Jones unknot conjecture, Ann. Inst. H. Poincare D (2025), arXiv:2402.02553
  - Freedman-Larsen-Wang, The two-eigenvalue problem and density of Jones representation of braid groups, Comm. Math. Phys. 228 (2002)
  - Squier, The Burau representation is unitary, Proc. AMS 90 (1984)
  - Habiro, A unified Witten-Reshetikhin-Turaev invariant for integral homology spheres, Invent. Math. 171 (2008), arXiv:math/0605314
  - Morton, An irreducible 4-string braid with unknotted closure, Math. Proc. Camb. Phil. Soc. 93 (1983)
  - Birman-Menasco, Stabilization in the braid groups I: MTWS, Geom. Topol. 10 (2006)
  - Lee, Salter's question on the image of the Burau representation of B_4, arXiv:2412.11853 (2024)

### verdict

doubtful

### confidence

High that the pure-arithmetic sub-route (heights, Mahler measure, resultants, Galois norms, Habiro integrality of V alone) is dead: the two-invariant principle is a proof, and the unit-height values H_1(4_1) = 1, H_1(3_1) = -t^{-+2} were checked. Medium that Lemma A is correct as stated (three hand checks; conventions not yet matched against Jones 1987 or KLS). Low-to-medium that Lemma B closes (C4): KLS's hypothetical HOMFLY-PT family shows only entry-level control of rho_4 can work, and that is the hard, long part; even success gives braid index 4 only, not T.


## Agent: build:statmech


### route_title

Potts/Tutte positivity, Jones zeros, and the Boyle-Spyropoulos projective (myopic Tutte) breadth strategy

### candidate_statement

Projective (myopic) adequacy theorem. Let K ⊂ S^3 be a knot, viewed as a local (hence nullhomologous, checkerboard-colourable) knot in RP^3, and D ⊂ RP^2 a connected checkerboard diagram with signed ℜ-Tait graph G (vertices = shaded faces, edges = crossings); α_ℜ(D) = projective rank of G (fewest edges whose deletion puts G in a disc). Let J^ℜ_D be the myopic state sum: Kauffman states S ⊆ E(G) with (V,S) nullhomologous in RP^2 (for local K it equals V_K up to normalisation; the non-local states cancel identically). Myopic Lando graph Λ_A(D): vertices = A-chords with both ends on one all-A state circle whose switching keeps the state nullhomologous; edges = interlacing. Λ_B(S_0): the same at each maximal nullhomologous state E − S_0, S_0 a minimum hitting set of one-sided cycles (|S_0| = α_ℜ). Call D myopically adequate if Λ_A(D) = ∅ and Σ_{S_0} I(Λ_B(S_0); −1) = ±1 (e.g. S_0 unique, Λ_B empty). STATEMENT: for myopically adequate D, breadth V_K = c(D) − α_ℜ(D). Hence Boyle-Spyropoulos Conjecture 1.1(2), and T, hold for every knot admitting a myopically adequate RP^2 diagram (a class containing adequate knots, possibly strictly), and a Jones-trivial knot admits no such diagram except the crossingless one.

### mechanism

Bracket = Potts/FK sum Σ_S q^{k(S)} Π v_e on the Tait graph, q = t+2+1/t, v_± = −(1+t^{±1}) (Jones 1989; Wu 1992; Kauffman 1989; Thistlethwaite 1987). State circles are the boundary components of N(V,S); on RP^2 their number is k(S)+n(S) for nullhomologous S and one less when (V,S) contains a one-sided cycle (N(S) acquires a crosscap, χ = 1 − b; at most one component can). That shift is exactly the integer/half-integer exponent split J = J^ℜ + J^ℑ, so the myopic Tutte polynomial is the FK sum over nullhomologous S. For alternating D the extreme nullhomologous states are ∅ and E − S_0, which gives Theorem 1.4 (breadth J^± = c − α^±) and Drobotukhina's c − 1/2 (Euler on RP^2: |s_A|+|s_B| = c+1). For general D the states at the potential extreme degrees are E_− Δ I with I independent in Λ_A, and (E − S_0) Δ I: a chord on a two-sided state circle C splits C iff it runs on the disc side of RP^2 − C or boundary-parallel on the Möbius side (nullhomology kept); a chord crossing the Möbius core once leaves one circle (degree drops by 2) and creates a one-sided cycle, invisible to J^ℜ. So the extreme coefficients are independence polynomials at −1 (Bae-Morton 2003; categorified by González-Meneses-Manchón-Silvero 2018), equal to ±1 under adequacy. New leverage over S^3: crossings of a projective twist region are absorbed into α while V is unchanged, and essential loop-edges all sit at one vertex (two one-sided curves in RP^2 meet), so breadth 0 forces the bouquet family Υ_n, inside which J determines the link. Precisely, the Boyle-Spyropoulos strategy needs breadth V_K ≥ c(D) − α_ℜ(D) for ONE RP^2 diagram of each knot K; the candidate gives it exactly for myopically adequate diagrams.

### why_not_excluded

It uses the exponent range of V, not a congruence, a root-of-unity value or finitely many finite-type coefficients, so (1) is silent; it is a Lickorish-Thistlethwaite-type class theorem with diagrammatically checkable hypotheses, not T rephrased. Consistent with Kanenobu knots (their diagrams are non-adequate in any sense) and with the Eliahou-Kauffman-Thistlethwaite local 2-component links (not knots; by the lemma they have no myopically adequate diagram). Nothing in (4) is reopened. In S^3 a diagram realising breadth 0 has no characterisation; the projective rank supplies one, which is the genuinely new ingredient.

### obstacle

(a) Reduction gap: Conjecture 1.1(2) at breadth 0 reads "V_K = 1 ⟹ some diagram has every crossing an essential loop ⟹ K ∈ {Υ_n} ∩ {local} = {unknot}", i.e. T restated. (2) is a strengthening of T whose uniform proof needs span lower bounds for non-adequate diagrams, the same wall as in S^3: extreme coefficients are Euler characteristics of independence complexes and vanish exactly off adequacy (one loop chord: 1 − 1 = 0), whereas Kronheimer-Mrowka's nonvanishing lives in homology, not in χ. (b) Falsification test. Structural lemma: α(G) = ℓ + α(G'), ℓ = number of essential loop-edges, and α(G') ≤ |E(G')|/2 (hitting sets = representatives of the embedding class φ + δC^0(G;Z/2); a random cut averages half the non-loop edges). Hence c − ℓ ≤ 2(c − α): bounded local crossing number forces D = Υ_ℓ plus ≤ 2β_ℜ further crossings. So (2) predicts that every Kanenobu knot K(p,−p) (V = V_{4_1}^2, breadth 8, crossing number unbounded, Khovanov homology p-independent by Watson) has, for every p, an RP^2 diagram that is a projective bouquet plus ≤ 16 crossings. This is enumerable by the authors' Theorem 5.3 method; failure refutes (2) and ends the strategy quantitatively (T unaffected). (c) Statistical-mechanics positivity is dead on this route: along the Jones curve the Potts model is never physical  -  q > 0 forces t > 0 where v = −(1+t) < −1 (e^K < 0); v ≥ −1 forces t ∈ [−1,0], q ≤ 0; v > 0 forces t < −1, q < 0  -  touching the physical closure only at t = −1 (q = v = 0, spanning trees = determinant). FKG, Griffiths and Lee-Yang never apply; the only positivity is Tutte-coefficient positivity of unsigned (alternating) Tait graphs, giving V_K(−s) ≠ 0 for s > 0, i.e. KMT. V > 0 on (0,∞) fails for both trefoils (V(1/2) = −6 for −t^{−4}+t^{−3}+t^{−1}). Zeros of V and of V − 1 are dense in ℂ (Jin-Zhang-Dong-Tay 2010; Jabłonowski 2026; Beraha-Kahane-Weiss as in Sokal 2004): no zero-free region exists, and no zero-location theorem separates V − 1 ≢ 0 from ≡ 0; |t| = 1 is |v| = √q, q ∈ [0,4], the Beraha accumulation regime, and Beraha-point identities (Fendley-Krushkal 2009) are root-of-unity sieves. (d) Whether myopically adequate knots strictly extend adequate knots is open; if not, the lemma adds no knots.

### first_lemma

Lemma (myopic Bae-Morton). For a connected checkerboard diagram D ⊂ RP^2 of a nullhomologous link, the coefficient of J^ℜ_D at the potential top A-degree c + 2|s_A| − 2 is ±I(Λ_A(D); −1), and at the potential bottom degree (from the maximal nullhomologous states E − S_0) it is ±Σ_{S_0} I(Λ_B(S_0); −1); all other nullhomologous states lie strictly inside. Sketch: S contributes A^{c−2|S|}(−A^2−A^{−2})^{b(S)−1}, b = #∂N(V,S). Starting from E_− (all-A), toggling an edge changes |S| by one and b by at most one, so the degree is kept only when b rises, i.e. the chord has both ends on one circle C and surgery splits C. Lift to the orientation double cover S^2 → RP^2 (deck map σ antipodal): C is two-sided, so it lifts to two disjoint circles swapped by σ; a disc-side or boundary-parallel chord lifts to σ-paired chords on the two lifts, interlacing is planar, and Bae-Morton's inclusion-exclusion over independent sets runs verbatim; a core-crossing chord lifts to one arc joining the two lifts, surgery gives one circle, and the subgraph gains a one-sided cycle, so it exits the myopic sum. At the bottom, nullhomologous subgraphs of maximal size are exactly E − S_0 with S_0 minimum-weight in φ + δC^0, and the same count runs from each. Corollary: myopically adequate ⟹ breadth V_K = c − α_ℜ (bookkeeping as in Theorem 1.4). Immediately afterwards run the Kanenobu test (b), before investing in non-adequate diagrams.

### literature

  - Boyle, Spyropoulos, Myopic Tutte polynomials and Khovanov homology in RP^3, 2026, arXiv:2609.40122 (Conj. 1.1, Thm 1.4, Thm 5.3)
  - Drobotukhina, An analogue of the Jones polynomial for links in RP^3 and a generalization of the Kauffman-Murasugi theorem, Leningrad Math. J. 2 (1991)
  - Hoste, Przytycki, The (2,∞)-skein module of lens spaces, J. Knot Theory Ramif. 2 (1993)
  - Jones, On knot invariants related to some statistical mechanical models, Pacific J. Math. 137 (1989)
  - Wu, Knot theory and statistical mechanics, Rev. Mod. Phys. 64 (1992)
  - Kauffman, A Tutte polynomial for signed graphs, Discrete Appl. Math. 25 (1989)
  - Thistlethwaite, A spanning tree expansion of the Jones polynomial, Topology 26 (1987)
  - Lickorish, Thistlethwaite, Some links with non-trivial polynomials and their crossing-numbers, Comment. Math. Helv. 63 (1988)
  - Sokal, Bounds on the complex zeros of (di)chromatic polynomials and Potts-model partition functions, CPC 10 (2001), arXiv:cond-mat/9904146
  - Sokal, Chromatic roots are dense in the whole complex plane, CPC 13 (2004), arXiv:cond-mat/0012369
  - Sokal, The multivariate Tutte polynomial (alias Potts model), 2005, arXiv:math/0503607
  - Jin, Zhang, Dong, Tay, Zeros of the Jones polynomial are dense in the complex plane, Electron. J. Combin. 17 (2010) R94
  - Jabłonowski, density of zeros of J_L(t) − 1, 2026, arXiv:2603.14585
  - Chang, Shrock, Zeros of Jones polynomials for families of knots and links, Physica A 301 (2001), arXiv:math-ph/0103043
  - Bae, Morton, The spread and extreme terms of Jones polynomials, JKTR 12 (2003), arXiv:math/0012089
  - González-Meneses, Manchón, Silvero, A geometric description of the extreme Khovanov cohomology, Proc. Roy. Soc. Edinburgh A 148 (2018), arXiv:1511.05845
  - Fendley, Krushkal, Tutte chromatic identities from the Temperley-Lieb algebra, Geom. Topol. 13 (2009), arXiv:0711.0016
  - Kanenobu, Infinitely many knots with the same polynomial invariant, Proc. AMS 97 (1986)
  - Watson, Knots with identical Khovanov homology, AGT 7 (2007), arXiv:math/0606631
  - Yang, Khovanov homology detects the unknot and the projective unknot in RP^3, 2024, arXiv:2402.15716

### verdict

doubtful

### confidence

0.9 that Lee-Yang / Potts-positivity / zero-free arguments are dead on this route (the Jones curve never enters the physical Potts region; zeros of V and V−1 are dense); 0.75 that the myopic adequacy lemma is provable as stated; 0.5 that Boyle-Spyropoulos Conj. 1.1(2) survives the Kanenobu test; below 0.1 that the route reaches T itself rather than a class theorem.


## Agent: build:representations


### route_title

Closed 4-braids: three-character decomposition of V, Burau_4 traces on the F_2-coset, and unitary extremality

### candidate_statement

(S) T holds for closed 4-braids, in the following sharpened form. Let β ∈ B_4 have 4-cycle permutation and exponent sum e (necessarily odd; by Jones' bound e ∈ {±1,±3} if V=1), K = closure(β), π: B_4→B_3 the surjection σ_1,σ_2,σ_3 ↦ σ_1,σ_2,σ_1, and L' = closure(π(β)), a 2-component 3-braid link. Put B(t) = Tr Bur_4^red(β)(t). Then V_K = 1 iff
(J4)  B(t) = t·[t^{-(e+1)/2}(1+t) + t^{-e/2} V_{L'}(t) − t^{-2} − 1 − t^2] / (1+t+t^2),
and (S) asserts that (J4) together with the Alexander coupling (1+t)(1+t^2)Δ_K ≐ 1 + t^e − B(t) − t^e B(t^{-1}) forces K to be unknotted. Calibration theorem (provable now, Lemma A): if β ∈ B_n and V(closure β) = V(n-component unlink) then β = 1.

### mechanism

For n=4 the Kauffman bracket of a closed braid is a sum of exactly three characters: ⟨closure β⟩ = Δ_4 A^e + Δ_2 χ_2(β) + Δ_0 χ_0(β), Δ_p the quantum dimensions (Δ_0=1, Δ_2=t^{-1}+1+t, Δ_4=t^{-2}Φ_5(t), t=A^{-4}). Here W(4,2) is reduced Burau: ρ(σ_i) has eigenvalues A,A,−A^{-3}, so χ_2 = A^e Tr Bur_4(β)|_{t=A^{-4}}; and W(4,0) (two cup diagrams (12)(34),(14)(23)) has σ_1 and σ_3 acting identically, so it factors through π and χ_0 = A^e Tr Bur_3(πβ). Since ⟨L'⟩ = A^e(Δ_3 + Δ_1 Tr Bur_3(πβ)), one gets Tr Bur_3(πβ) = −t^{-e/2}V_{L'} − t^{-1} − t, and V_K=1 ⇔ Δ_4 + Δ_2 B + Tr Bur_3(πβ) = t^{-(e+1)/2}(1+t) (e odd), which rearranges to (J4). Check: β=σ_1σ_2σ_3, B=−t, L'=positive Hopf link, V_{L'}=−t^{1/2}−t^{5/2}: numerator = −(1+t+t^2), B=−t. Alexander coupling: det(I−Bur_4(β)) = (1+t)(1+t^2)Δ_K, det Bur_4(β) = (−t)^e, and by Squier unitarity Tr ∧²Bur_4(β) = (−t)^e B(t^{-1}); so when V_K=1 the Jones polynomial of the 3-braid link L' and e determine B and hence Δ_K: all classical invariants of the pair (K,L') are locked together. Coset form: B_4 = F_2 ⋊ B_3 with F_2 = ker π = ⟨σ_1σ_3^{-1}, σ_2σ_1σ_3^{-1}σ_2^{-1}⟩ (Long's reduction subgroup used by BBB); writing β = fγ̃, γ̃ ∈ B_3 ⊂ B_4, closure(γ̃) = L' ⊔ O and f is trivial on W(4,4), W(4,0), so (†) ⟨closure β⟩ = ⟨L' ⊔ O⟩ + Δ_2 A^e [Tr Bur_4(fγ̃) − Tr Bur_4(γ̃)]. Jones-triviality of a 4-braid knot is thus exactly a statement about the Burau_4 trace function on the coset F_2·γ̃, where Bur_4 is a deformation of a unipotent (Torelli-type point-pushing) action at t=−1  -  the same place faithfulness was proved. Unitary mechanism (for Lemma A): at A = i e^{iπ/2r}, δ = 2cos(π/r) > 0, Δ_p = sin((p+1)π/r)/sin(π/r) > 0 for p ≤ r−2 and the W(n,p) are unitary, so |⟨closure β⟩| ≤ Σ_p Δ_p dim W(n,p) = δ^n with equality iff every ρ_p(β) is one common scalar; asymptotic faithfulness (Freedman-Walker-Wang, Andersen) then pins β to the center.

### why_not_excluded

(J4), (†) and the Alexander coupling are identities in Z[t^{±1}]; they use V globally (degree range, integrality of B, divisibility of the numerator by Φ_3, symmetrization about e/2), not evaluations or congruences, so principle (1) does not apply. Closed 4-braids are not in the parked/known list (4); Korzun-Lanina-Sleptsov (AIHPD 2025) state the 4-strand case is open. Bigelow (2002) and Ito (2014) only give 'Burau_4 unfaithful ⇒ counterexample'; BBB's faithfulness (Cor. 1.1: Jones rep of B_4 faithful) closes that door and is used here structurally (trace function on F_2·γ̃), not as a sieve. Datta's 3-braid detection (binary quadratic forms attached to the 2×2 Burau_3 characteristic polynomial, class numbers) is precisely the n=3 instance of this trace strategy, and he announces only 'generic' 4-braid closures, so the n=4 statement is open and not a reformulation.

### obstacle

Non-extremality. The unitary/asymptotic-faithfulness mechanism detects only closures of central braids (unlinks, torus links T(n,nk)): V is the single functional tr(ρ(β)) of the operator ρ(β) ∈ TL_4, while identifying ρ(β) with ρ(σ_1σ_2σ_3) needs tr(ρ(β)h) for all h ∈ TL_4, i.e. brackets of other closures that V_K does not see. Concretely the unknot braid has tiny traces (Tr Bur_4(σ_1σ_2σ_3) = −t) and |⟨unknot⟩| = δ ≪ δ^4, so no inequality is saturated. Second, a 3×3 matrix over Z[t^{±1}] is not determined by its trace: Datta's n=3 trick (trace + det ⇒ conjugacy class ⇒ ideal class) has no 3×3 analogue, and f ↦ Tr Bur_4(fγ̃) on F_2 is far from injective (3×3 trace identities, conjugation by the centralizer of γ̃). Third, no lower bound on the degree spread of Burau traces of pseudo-Anosov 4-braids is available (Alexander-trivial pA 4-braid knots exist, so the symmetric part of B can be a monomial-plus). The power sub-route is a side road: ⟨closure β^m⟩ is a generalized power sum in m over Q(A), so by Skolem-Mahler-Lech {m : V(closure β^m)=1} is a finite union of arithmetic progressions plus a finite set, and an infinite set forces an eigenvalue of some ρ_p(β) to be a root of unity times (−A^3)^e; but T is the m=1 statement and periodic links only yield Murasugi congruences (sieves), so this gives at best 'finitely many Jones-trivial powers per non-periodic β', not T.

### first_lemma

Lemma A (do first; essentially proved above). For β ∈ B_n, V(closure β) = V(unlink_n) ⇒ β = 1. Sketch: V = V(unlink_n) gives ⟨closure β⟩ = (−A^3)^e δ^n; at A = i e^{iπ/2r}, r ≥ n+2, the bound |⟨closure β⟩| ≤ δ^n is saturated, so ρ_p(β) = λ_r I on every W(n,p); hence β ∈ ∩_r ker(Pρ_r) = Z(B_n) (FWW 2002, Thm 1.1; Andersen 2006), so β = Δ^{2k}, closure = T(n,nk), and span V(T(n,nk)) > 0 for k ≠ 0. This calibrates the route: the representation-theoretic input detects exactly the extremal point.
Lemma B (the new step). Prove (J4) and the coupling Δ_K ≐ [1 + t^e − B − t^e B(t^{-1})]/((1+t)(1+t^2)) with B from (J4): (a) W(4,0) factorization through π; (b) ⟨L'⟩ in terms of Tr Bur_3(πβ); (c) ∧²Bur_4 ≅ det ⊗ Bur_4^{*} via Squier's form, so the characteristic polynomial of Bur_4(β) is x^3 − Bx^2 + (−t)^e B(t^{-1})x − (−t)^e. Corollary to extract: for a Jones-trivial 4-braid knot, Δ_K is an explicit function of V_{L'} and e ∈ {±1,±3}, the numerator in (J4) is divisible by Φ_3, and B(1) = −1, B(−1) = 1 + Tr(M_β), M_β ∈ SL_2(Z) the image of β. Then Lemma C (the real target, Datta-style): describe the fibers of f ↦ Tr Bur_4(fγ̃) on F_2 using that Bur_4|_{F_2} is unipotent at t = −1 and that the symmetric part of B is fixed by Δ_K; show the fiber through the unknotted braids σ_1^{±1}σ_2^{±1}σ_3^{±1} (and their Markov/exchange-move relatives) contains no knotted closure. A proof of Lemma C for γ̃ with L' hyperbolic (V_{L'} of full span) would already give T for a large class of 4-braids, the 'generic' class Datta announces.

### literature

  - V. F. R. Jones, Hecke algebra representations of braid groups and link polynomials, Ann. Math. 126 (1987): V of closed braids as weighted sum of traces of W(n,p); degree bounds.
  - S. Bigelow, Does the Jones polynomial detect the unknot?, J. Knot Theory Ramif. 11 (2002), arXiv:math/0012086: Burau_4/TL_4/Jones-rep faithfulness equivalent; kernel element would give a Jones-trivial knot.
  - T. Ito, A kernel of a braid group representation yields a knot with trivial knot polynomials, Math. Z. (2015), arXiv:1402.2028: Burau_4 unfaithful ⇒ V fails to detect the unknot (proves Bigelow's conjecture).
  - V. Bharathram, J. Birman, T. Brendle, The Burau representation of the braid group is faithful for n = 4, 2026, arXiv:2607.05283: Thm (faithfulness via Long's reduction to the Brunnian subgroup), Cor. 1.1 (Jones representation of B_4 faithful).
  - A. Datta, A novel connection between integral binary quadratic forms and knot polynomials, 2022, arXiv:2204.13660 (class numbers of discriminant t^2−4 forms count 3-braid links with given V, Δ; seminar abstracts: V detects the unknot for 3-braid links, 'generic 4-braid closures' announced); A. Datta, Burau representation of B_4 faithful almost everywhere, arXiv:2209.10826.
  - E. Korzun, E. Lanina, A. Sleptsov, Closed 4-braids and the Jones unknot conjecture, Ann. Inst. H. Poincaré D (2025), arXiv:2402.02553: 4-strand case open; trivial-V vs nontrivial-HOMFLY on 4-braids.
  - M. Freedman, K. Walker, Z. Wang, Quantum SU(2) faithfully detects mapping class groups modulo center, Geom. Topol. 6 (2002); J. E. Andersen, Asymptotic faithfulness of the quantum SU(n) representations of the mapping class groups, Ann. Math. 163 (2006).
  - C. Squier, The Burau representation is unitary, Proc. AMS 90 (1984): Hermitian form giving Tr Bur(β^{-1})(t) = Tr Bur(β)(t^{-1}).
  - A. Stoimenow, Coefficients and non-triviality of the Jones polynomial, J. reine angew. Math. 657 (2011), arXiv:math/0606255: semiadequate links and closed 3-braids.
  - J. Birman, On the Jones polynomial of closed 3-braids, Invent. Math. 81 (1985): V of 3-braids ↔ Burau_3 trace.
  - N. Fullarton, R. Shadrach, Observed periodicity related to the four-strand Burau representation, arXiv:1610.04648: computer evidence any Burau_4 kernel element is very complicated.
  - A. Champanerkar, I. Kofman, On the Mahler measure of Jones polynomials under twisting, Algebr. Geom. Topol. 5 (2005): V under twisting satisfies linear recurrences (the power/recurrence sub-route is known technology).

### verdict

viable

### confidence

medium-low. Lemmas A and B are essentially proved here (A is a clean theorem; B is a checked identity). The route credibly yields T for a large 'generic' class of closed 4-braids (where V_{L'} pins B rigidly), but all of B_4 almost certainly needs an input beyond traces (3×3 trace non-rigidity), e.g. adequacy for the residual words; faithfulness of Burau_4 contributes structure, not a sieve.


## Agent: build:minimal


### route_title

Structure of a minimal Jones-trivial knot (geometric topology)

### candidate_statement

Theorem S (all provable now). Let K be nontrivial with V_K = 1, WLOG prime (V is multiplicative; the only unit of Z[t^±1] with V(1)=1, V'(1)=0 is 1, so every prime factor is Jones-trivial) and of least crossing number among prime Jones-trivial knots. Then, for K and its mirror K* (V_{K*}(t)=V_K(t^{-1})=1):
(a) c(K) ≥ 25; every n-braid representative has |e| ≤ n−1; braid index ≥ 4 (2-braids alternating, 3-braids Stoimenow); sl_max ≤ −1 and TB ≤ −1 for K and K*.
(b) K is neither quasipositive nor quasinegative: the closure of a quasipositive n-braid with k bands bounds Rudolph's embedded braided surface, connected with χ = n−k; Jones's bound gives k = e ≤ n−1, so χ ≥ 1, a disk. Hence K is not positive/negative, not strongly quasipositive/negative, not a positive/negative braid closure.
(c) det K = |V(−1)| = 1, a_2(K) = −V''(1)/6 = 0 (so Arf = 0, ∇_K = 1 + a_4 z^4 + …); Σ_2(K) is an irreducible integral homology sphere (Kim-Tollefson, K prime).
(d) No diagram of K is semiadequate (Stoimenow 2011): not alternating, adequate, Montesinos, almost alternating; Turaev genus g_T(K) ≥ 2 (g_T=0 iff alternating; g_T=1 links have nontrivial V, Lowrance-Spyropoulos via Kim / Armond-Lowrance).
(e) K is Khovanov-thick over Q: on one diagonal j−2i=s the ranks of reduced Kh would be |coefficients of V|, so Kh̃ = Q, contradicting Kronheimer-Mrowka. So K is not quasi-alternating (Manolescu-Ozsváth), and Kh̃(K;Q) has odd rank ≥ 3: Q in (0,0) plus ≥ 1 cancelling pair.
(f) For every diagram D of K, ⟨D⟩ = (−A^3)^{w(D)} is a monomial: at least one of the two extreme Lando independence complexes (all-A / all-B states, GMMS) has Euler characteristic 0, and both do unless 3w(D) ∈ {c+2s_A−2, −(c+2s_B−2)}, in which case the whole bracket sits at that potential extreme and that extreme Khovanov group of D has nonzero Euler characteristic. (DFKLS's span V ≤ c − g_T is vacuous.)
(g) K is not a torus knot, so K is hyperbolic or a satellite. If K = P(C), C ≠ U, winding λ, wrapping ω ≥ 2, then V_K = Σ_{n≤ω, n≡λ(2)} b_n(A) J̃_{n+1}(C), b_n the Chebyshev coefficients of P in the bracket skein module of the solid torus, J̃ the unnormalised coloured Jones with P's framing. For untwisted Whitehead doubles ⟨Wh⟩ = a_0 + a_2 z^2, a_2 ≠ 0, Wh_±(U) = U, so V_{Wh_+(C)} = 1 ⟺ V_{Wh_−(C)} = 1 ⟺ the 0-framed 2-parallel link C ∪ C' has the Jones polynomial of the 2-unlink ⟺ J_3(C) = J_3(U).
Candidate C (the push): no satellite knot is Jones-trivial, i.e. a minimal Jones-trivial knot is hyperbolic with (a)-(f). By (g) this is a finite-colour rigidity statement about companions; its smallest case is "no nontrivial C has J_3(C) = J_3(U)".

### mechanism

(b) is pure exponent range: Jones's degree bound compares the whole Laurent polynomial with braid data, exactly the global use principle (1) allows. For Candidate C: V_{P(C)} is a Z[A^±]-combination of finitely many coloured Jones polynomials of C, whose degrees separate quadratically in the colour (Garoufalidis: deg J_n is a quadratic quasi-polynomial; Jones slopes are boundary slopes in every verified case), while the pattern coefficients b_n have degrees fixed by P. For winding ≥ 1 torus-knot patterns the top coefficient is a unit monomial (Morton; Rosso-Jones), so the top colour dominates both ends of V_{P(C)} unless the cabling slope pq coincides with a Jones slope of C, the degeneracy Kalfagianni-Tran isolate; then span V_{P(C)} ≥ span J̃_{ω+1}(C) − O(1) > 0. For winding 0 the requirement is triviality of a single colour, and that colour is categorically rigid: Khovanov homology of the 2-cable (Hedden) and of every colour n ≥ 2 (Grigsby-Wehrli) detects the unknot. Lemma B below settles the smallest case when TB(C) ≥ 0 or TB(C*) ≥ 0 by feeding Rudolph's quasipositive plumbing into (b).

### why_not_excluded

Nothing is a congruence or finite evaluation: (a), (b), (f), (g) use the exponent range of V and of coloured Jones polynomials globally; (c)-(e) are sieves used only to sharpen the structure, never as the engine. The satellite reduction uses the full Laurent polynomial across several colours at once. The route does not touch Lemma Q, strong invertibility, the Temperley-Lieb width ladder, or fixed-root satellite amplification; EKT enters only as a warning that any proof of Candidate C must use the annulus cobounded by C and C', since Hopf satellites with trivial V exist. No finite computations.

### obstacle

1. Minimality is nearly inert: V = 1 is not inherited by companions, smoothings or crossing changes, and crossing number does not descend to companions (Lackenby: c(P(C)) ≥ c(C)/10^13 is the best known), so Theorem S is a list of necessary conditions, not an induction. 2. Winding-zero satellites: by (g), T for untwisted Whitehead doubles is equivalent to "the 0-framed 2-cable link detects the unknot", a case of "J_3 detects the unknot", which is open; only categorified versions are known, and Andersen's announced coloured-Jones detection never appeared. 3. Cables: degree domination needs deg J̃_n(C) at the small colours n ≤ ω+1 for arbitrary non-adequate C, but quasi-polynomiality is only asymptotic, the slope conjecture is open, and the degenerate case pq = Jones slope permits cancellation. 4. Hyperbolic case: every Jones-to-geometry bound (Dasbach-Lin, Futer-Kalfagianni-Purcell) needs semiadequacy, precisely what (d) excludes, and (f) is per-diagram and does not propagate to the knot. So the route yields a sharp structure theorem and new partial results, but no mechanism reaching a contradiction for hyperbolic K.

### first_lemma

Lemma B (prove first; sketch complete). If C is nontrivial with TB(C) ≥ 0 or TB(C*) ≥ 0, then V_{C∪C'} ≠ V_{unlink_2} for the 0-framed 2-parallel; hence J_3(C) ≠ J_3(U) and neither untwisted Whitehead double of C is Jones-trivial. Sketch: for TB(C) ≥ 0 the 0-framed annulus A(C,0) is quasipositive (Rudolph, quasipositive annuli) and its plumbing with a positive Hopf band is quasipositive (Rudolph 1998; Hedden 2010 proves the converse), so Wh_+(C,0) is strongly quasipositive, hence not Jones-trivial by S(b). By (g), V_{Wh_+(C)} − 1 = unit·a_2·(⟨C^{(2)}_0⟩ − ⟨U^{(2)}_0⟩) with a_2 ≠ 0, so ⟨C^{(2)}_0⟩ ≠ ⟨U^{(2)}_0⟩, which also kills Wh_−(C) and gives V_{C∪C'} ≠ V_{unlink_2}. Mirror for TB(C*) ≥ 0. To check: a_2 of the clasp is an explicit nonzero two-term polynomial; writhe bookkeeping with a writhe-zero companion diagram.
Lemma C (next). For K = C_{p,q}, Morton's expansion ⟨T_{p,q}⟩ = Σ_k ε_k A^{e_k} S_{p−2k}(z) gives V_K = Σ_k ε_k A^{e_k} J̃_{p+1−2k}(C); V_K = 1 forces max and min degrees of J̃_{p+1}(C) to match those of J̃_{p−1}(C) up to the fixed offsets e_1 − e_0 at both ends simultaneously. Target: show via the Kalfagianni-Tran cabling formula that both equalities at a fixed colour force C = U. If quadratic separation cannot be made effective at a fixed colour, Candidate C is dead for cables and the route stalls at Lemma B.

### literature

  - Jones, Hecke algebra representations of braid groups and link polynomials, Ann. Math. 126 (1987): degree bounds vs braid exponent sum
  - Stoimenow, Coefficients and non-triviality of the Jones polynomial, J. reine angew. Math. 657 (2011), arXiv:math/0606255
  - Tuzun-Sikora, Verification of the Jones unknot conjecture up to 24 crossings, JKTR 30 (2021), arXiv:2003.06724
  - Kronheimer-Mrowka, Khovanov homology is an unknot-detector, Publ. IHES 113 (2011), arXiv:1005.4346
  - Hedden, Khovanov homology of the 2-cable detects the unknot, Math. Res. Lett. 16 (2009), arXiv:0805.4418
  - Grigsby-Wehrli, On the colored Jones polynomial, sutured Floer homology, and knot Floer homology, Adv. Math. 223 (2010), arXiv:0807.1432
  - Rudolph, Braided surfaces and Seifert ribbons for closed braids, Comment. Math. Helv. 58 (1983); Rudolph, Quasipositive plumbing (Constructions of quasipositive knots and links V), Proc. AMS 126 (1998); Hedden, Notions of positivity and the Ozsváth-Szabó concordance invariant, JKTR 19 (2010), arXiv:math/0509499
  - Lowrance-Spyropoulos, The Jones polynomial of an almost alternating link, New York J. Math. 23 (2017); Dasbach-Lowrance, Extremal Khovanov homology of Turaev genus one links, Fund. Math. 250 (2020); Kim, Link diagrams with low Turaev genus, Proc. AMS 146 (2018); Armond-Lowrance, Turaev genus and alternating decompositions, AGT 17 (2017)
  - Dasbach-Futer-Kalfagianni-Lin-Stoltzfus, The Jones polynomial and graphs on surfaces, JCTB 98 (2008), arXiv:math/0605571
  - Manolescu-Ozsváth, On the Khovanov and knot Floer homologies of quasi-alternating links, Gökova 2007, arXiv:0708.3249
  - González-Meneses-Manchón-Silvero, A geometric description of the extreme Khovanov cohomology, Proc. Roy. Soc. Edinburgh A 148 (2018), arXiv:1511.05845
  - Kim-Tollefson, Splitting the PL involutions of nonprime 3-manifolds, Michigan Math. J. 27 (1980): Σ_2(K) reducible iff K composite
  - Eliahou-Kauffman-Thistlethwaite, Infinite families of links with trivial Jones polynomial, Topology 42 (2003)
  - Stoimenow-Tanaka, Mutation and the colored Jones polynomial, J. Topol. 2 (2009), arXiv:math/0607794
  - Garoufalidis, The Jones slopes of a knot, Quantum Topol. 2 (2011), arXiv:0911.3627; Kalfagianni-Tran, Knot cabling and the degree of the colored Jones polynomial, New York J. Math. 21 (2015), arXiv:1501.01574; Kalfagianni-Lee, Jones diameter and crossing number of knots, Adv. Math. (2023)
  - Lackenby, The crossing number of satellite knots, AGT 14 (2014)
  - Dasbach-Lin, A volumish theorem for the Jones polynomial of alternating knots, Pacific J. Math. 231 (2007); Futer-Kalfagianni-Purcell, Guts of surfaces and the colored Jones polynomial, LNM 2069 (2013), arXiv:1108.3370

### verdict

doubtful

### confidence

High (about 0.85) that Theorem S(a)-(g) and Lemma B are correct, and that S(b), the Whitehead-double/2-cable equivalence in S(g), and Lemma B are not stated in the literature in this form (one targeted search found only the categorified detection results). Low (about 0.15) that the route reaches T: the satellite half reduces to open single-colour coloured-Jones detection, and the hyperbolic half has no Jones-to-geometry mechanism once semiadequacy is excluded.


## Agent: build:symplectic


### route_title

Categorified chi-rigidity: extreme-column non-cancellation (ECN) as the only Floer-compatible bridge from V to Khovanov rank

### candidate_statement

ECN (for every knot K): the two extreme quantum degrees of Kh(K;Q) carry nonzero Euler characteristic, i.e. min/max q-degree of Kh(K;Q) equal min/max degree of the unnormalized Jones polynomial V~_K (equivalently: neither extreme column of Kh contains two generators of opposite homological parity). ECN implies T: if V~_K = q + q^{-1}, ECN forces Kh(K;Q) to be supported in q in {-1, 1}; Lee's spectral sequence has d_r of bidegree (1, 4r), so every differential vanishes, Kh = E_infinity = Q^2 (Lee), and rank 2 forces K = U (Kronheimer-Mrowka). The argument uses exactly the gap 2 < 4 between the unknot's Jones span and Lee's q-shift; for a 2-component link the unlink's span is 4, d_1 can act, so the Thistlethwaite / Eliahou-Kauffman-Thistlethwaite links with unlink Jones polynomial are NOT contradicted, which is the right sanity check for any knot-only mechanism. Weaker provable byproduct (Lemma 0): a nontrivial Jones-trivial knot is not Kh-thin, and at least one of its extreme Kh columns is a cancelling column (same proof run backwards).

### mechanism

Extreme columns are the rigid, combinatorial part of Kh. For any diagram D, Kh^{*, q_min(D)}(D) is the reduced homology of the independence complex Ind(G_D) of the Lando graph (a bipartite circle graph) of the all-A state (Gonzalez-Meneses-Manchon-Silvero), with Bae-Morton's extreme coefficient as Euler characteristic; the extreme Khovanov spectrum is a suspension of Ind(G_D) (Cantero Moran-Silvero); the next columns are chromatic graph homology (Lowrance-Sazdanovic). Przytycki-Silvero conjecture Ind(circle graph) is always a wedge of spheres and prove it for cactus, outerplanar, permutation, non-nested graphs and for 4-braid extreme degrees (contractible, a sphere, or a wedge of two spheres). So 'can the extreme column cancel?' is a finite combinatorial question about chord interlacement, not about the whole of Kh. Empirical pattern behind ECN: interior cancellation can be total while extremes survive. Using only the alternating-sign structure of V one gets V~(4_1) = q^5 + q^{-5} and V~(9_42) = q^7 + q^{-7}; more generally V~ = q^a + q^{-a} passes the (1-t)^2(1+t+t^2) test iff a = +-1 mod 6 and then det = a, so T is the a = 1 member of a family whose known members (a = 5, 7) have nonzero extreme columns and total interior cancellation. On the Floer side the same structure appears as: HF(L_0, beta L_0) in Seidel-Smith's slice Y_n, weight-graded via Abouzaid-Smith, has an extreme weight piece computed by the lowest-order terms of the iterated fibered-Dehn-twist exact triangles, i.e. by the same cube corner; no additional symplectic input is needed or available.

### why_not_excluded

ECN uses the exponent range of V globally (both extreme degrees), which (1) explicitly lists as admissible; it is not a congruence, not finitely many evaluations, not finite-type. It is strictly stronger than T and falsifiable on a single knot, so it is not T dressed up: it holds for adequate/alternating knots (extreme columns have rank 1), at the minimal end for positive knots (q_min = s-1 = 2g-1 in h = 0), and for 4-braid extreme degrees of the sphere/contractible type. It does not touch (3)-(4). It avoids the (1)-type obstruction because the Eliahou-Fromentin knots with V = 1 mod 2^r have V not equal to 1 and hence honest extreme degrees; nothing is said about V modulo anything.

### obstacle

(a) ECN is probably false in general. Przytycki-Silvero give a construction of a permutation (hence circle) graph whose independence complex is any prescribed finite wedge of spheres, and report Lando graphs with Ind homotopy equivalent to S^n v S^{2n-1}; for n even the reduced Euler characteristic is 0 while the homology is nonzero, so that diagram's extreme column is a genuine cancelling column of Kh of the link, i.e. q-span(Kh) > span(V). GMS also give knots with arbitrarily many nontrivial extreme modules and P-S give H-thick knots with arbitrarily many gaps in the extreme column, so mixed parity for a KNOT diagram is likely; I could not confirm from abstracts whether the S^n v S^{2n-1} example is a knot. (b) Even if ECN survives at diagram level, the minimal nonzero column of Kh(K) need not be the extreme potential column of any diagram, so GMS control can fail exactly where it is needed. (c) The Floer half of the route is dead: the geometric (Maslov) Euler characteristic of HF(L_0, beta L_0) is the algebraic intersection number [L_0].[beta L_0] = +-det(K) (Seidel-Smith's single grading), a sieve by (1); the Jones grading of Abouzaid-Smith is algebraic, induced from the graded arc algebra H^n through formality of the symplectic arc algebra, not an intersection-theoretic or equivariant quantity (Y_n is a fibre over a point of Conf_{2n}(C), so it carries no C^* action), so no Lagrangian rigidity statement in Y_n can see V rather than det. (d) ECN still needs KM at the end: it lifts V to a rank statement, it does not avoid decategorification. Every known detection theorem (KM, Baldwin-Sivek trefoils, Baldwin-Dowlin-Levine-Lidman-Sazdanovic figure-eight, Dowlin's Khr to HFK-hat) runs through a theory with chi = Delta or through sutured genus detection, and the common invariant of the q-grading and the Alexander grading is det. (e) Lee-structure refinements are blocked: the knight move decomposition fails in general (Manolescu-Marengon), and V = q^{s-1}+q^{s+1} mod (1-q^4) holds automatically for every even s, so s is unconstrained by V = 1.

### first_lemma

Lemma A (diagram-level ECN, necessary for ECN): if D is a KNOT diagram whose all-A Lando graph G_D has H~_*(Ind(G_D)) nonzero, then chi~(Ind(G_D)) is nonzero. Attack: a one-component condition constrains interlacement. For a single state circle with self-chord interlacement matrix A over F_2, the number of components of the diagram is 1 + dim ker(A + I), so knot diagrams have A + I nonsingular (with several circles, the analogous nonsingularity of the full chord-interlacement matrix after eliminating inter-circle chords). Run the cofibration sequence Ind(G - N[v]) -> Ind(G - v) -> Ind(G) (so Ind(G) = Ind(G-v) v Suspension Ind(G - N[v]) when the inclusion is null) together with the fold lemma, and test whether the nonsingularity of A + I forbids wedges S^a v S^b with a and b of different parity; the P-S cases (permutation and non-nested graphs) are the first place to look since the realization theorem lives there. Expected outcome: a P-S style mixed wedge S^n v S^{2n-1}, n even, on a Lando graph with A + I nonsingular exists; then Lemma A, ECN, and this whole route are dead, and only Lemma 0 (Jones-trivial nontrivial knots are thick with a cancelling extreme column) remains as a usable filter for other routes. If instead the parity constraint kills every mixed wedge, ECN becomes a serious conjecture and the second lemma is realizability: for the minimal nonzero q-degree of Kh(K) find a diagram realizing it as q_min(D) with nonzero extreme homology (true for A-adequate diagrams, open otherwise).

### literature

  - Seidel, Smith, A link invariant from the symplectic geometry of nilpotent slices, Duke 2006, arXiv:math/0405089
  - Abouzaid, Smith, The symplectic arc algebra is formal, Duke 2016, arXiv:1311.5535
  - Abouzaid, Smith, Khovanov homology from Floer cohomology, JAMS 2019, arXiv:1504.01230
  - Manolescu, Nilpotent slices, Hilbert schemes, and the Jones polynomial, Duke 2006, arXiv:math/0411015
  - Seidel, Smith, Localization for involutions in Floer cohomology, GAFA 2010, arXiv:1002.2648
  - Kronheimer, Mrowka, Khovanov homology is an unknot-detector, Publ. IHES 2011, arXiv:1005.4346
  - Lee, An endomorphism of the Khovanov invariant, Adv. Math. 2005, arXiv:math/0210213
  - Rasmussen, Khovanov homology and the slice genus, Invent. Math. 2010, arXiv:math/0402131
  - Manolescu, Marengon, The knight move conjecture is false, Proc. AMS 2020, arXiv:1809.09769
  - Gonzalez-Meneses, Manchon, Silvero, A geometric description of the extreme Khovanov cohomology, Proc. Roy. Soc. Edinburgh 2018, arXiv:1511.05845
  - Przytycki, Silvero, Homotopy type of circle graph complexes motivated by extreme Khovanov homology, J. Algebraic Combin. 2018, arXiv:1608.03002
  - Przytycki, Silvero, Khovanov homology, wedges of spheres and complexity, RACSAM 2024, arXiv:2305.18648
  - Cantero Moran, Silvero, Extreme Khovanov spectra, Rev. Mat. Iberoam. 2020
  - Bae, Morton, The spread and extreme terms of Jones polynomials, JKTR 2003, arXiv:math/0012089
  - Lowrance, Sazdanovic, Chromatic homology, Khovanov homology, and torsion, Topology Appl. 2017, arXiv:1609.05008
  - Dowlin, A spectral sequence from Khovanov homology to knot Floer homology, 2018, arXiv:1811.07848
  - Baldwin, Sivek, Khovanov homology detects the trefoils, Duke 2022, arXiv:1801.07634
  - Baldwin, Dowlin, Levine, Lidman, Sazdanovic, Khovanov homology detects the figure-eight knot, Bull. LMS 2021, arXiv:2007.01269
  - Hedden, Ni, Khovanov module and the detection of unlinks, Geom. Topol. 2013, arXiv:1204.0960
  - Batson, Seed, A link-splitting spectral sequence in Khovanov homology, Duke 2015, arXiv:1303.6240

### verdict

doubtful

### confidence

High (about 0.9) that the Lagrangian-Floer half is dead: the geometric Euler characteristic in the slices is det, and the Jones grading is algebraic. Low-to-medium (about 0.25) that ECN is true; I expect Lemma A to fail on a knot diagram built from a Przytycki-Silvero mixed-parity wedge, which would close the route except for Lemma 0.


## Agent: ref:gauge


### route_title

SU(2)/pillowcase route: Jones as a graded Casson-Lin count

### main_flaw

Candidate C is false for explicit knots, and the pillowcase supplies no structure beyond the bigrading of Khr itself. (i) González-Meneses-Manchón-Silvero (Proc. Roy. Soc. Edinburgh 148, 2018, arXiv:1511.05845), Thm 10: an 11-crossing diagram whose Lando graph is two hexagons sharing a vertex has Kh^{i,j_min} ≅ Z for i = 0, 1 and nothing else. Remark 14 / Thm 13: adding crossings whose A-chords join distinct state circles merges components without changing the Lando graph, so a 15-crossing KNOT has extreme group Z ⊕ Z in consecutive homological degrees (shifted). A nonzero group at j_min is the knot's true extreme column; its Euler characteristic is 0, so the Jones coefficient there vanishes: q-span Khr(K;Q) > span V and the extreme column is not sign-coherent. The reduced column agrees with the unreduced one at the extreme degree (reduced/unreduced LES). Mirror kills the other side; K # mirror(K) kills both. (ii) The "class version" (no special components) is vacuous: a finger move gives K = T ∪ Q_0 with T = Q_∞ carrying K as a local knot, BN~(T) = ⊕_{g ∈ Khr(K)} r(∞)[bideg g], rational only; the "ordering of shifts" is the bigrading of Khr(K), i.e. C verbatim. Every knot is in the class. (iii) Lemma A's consequence "cancellation only between components" does not follow: two adjacent reduced δ-diagonals (δ, δ+2) place opposite-parity generators in one q-degree; Khr(T(3,4);Q), the n = 3 closure of the Lemma B tangle up to mirror, lives on δ = 4, 6 with cancelling pairs at q = 12 and q = 14.

### counterexample_or_reason

GMS knot: Thm 10 diagram (Fig. 10, c = 11, 3 negative crossings, j_min = 1, H^{0,1} ≅ H^{1,1} ≅ Z) made one-component by Thm 13's four extra crossings. Extreme column rank 2, χ = 0, torsion-free, so C fails over Q (and every field). Infinite supply: Przytycki-Silvero (J. Algebraic Combin. 48, 2018, arXiv:1608.03002) Thm 7.9(1): diagrams D_n with extreme Kh = Z in degrees 3n+1 and 4n (independence complex S^n ∨ S^{2n-1}); for even n the degrees have opposite parity, χ = 0; Remark 14 of GMS makes them knots. Przytycki-Silvero (arXiv:2305.18648) Cor 1.6: 4-braid closures have extreme Kh ∈ {0, Z, Z[k]⊕Z[i], Z[k]⊕Z^2[i], Z[k]⊕Z^3[i]}, so even 4-braids escape only when k ≡ i mod 2. Babson's bipartite circle graph (S^4 ∨ S^5) shows mixed parity is generic, not accidental. Note V = 1 for a knot forces V to be a monomial only via V'(1) = 0, so T ⟺ "at least two q-columns of Khr have χ ≠ 0"; C attacked the extreme columns, exactly the ones that can vanish in χ.

### principle_check

C itself is global (exponent range, extreme coefficients), not a sieve, and C ⟹ T is valid. But the only bridge from SU(2) to V is χ(Khr) = V: HHHK (arXiv:1808.06957) is a chain-level repackaging of the reduced Khovanov complex (hom into the trivial-tangle Lagrangian is naturally the reduced Khovanov complex, unconditional, no earring needed); no SU(2) quantity touches signs, as the builder concedes in obstacle (a). So the route is route (5) relabeled, and the counterexample is the one the builder's obstacle (b) predicted. Lemma B is a finite-family computation (barred by the brief). Lemma A is stated over F_2 while C and Kronheimer-Mrowka are over Q; harmless for the implication (F_2-rank ≥ Q-rank), but the F_2 form of C is strictly stronger, and the counterexample is torsion-free, so C dies in every characteristic.

### literature_check

Checked (abstracts/texts): HHHK 1808.06957: twisted complex of compact Lagrangians in the pillowcase Fukaya category, hom into the trivial-tangle Lagrangian ≅ reduced Khovanov chain complex (confirmed, chain-level, unconditional). KWZ "Khovanov multicurves are linear" 2202.01460: every component lifts to a straight line (confirmed); the coefficient field and rational/special pairing statements were not verifiable from abstracts, and Lemma A's "two adjacent diagonals ⟹ no intra-component cancellation" is wrong regardless. GMS 1511.05845: Thm 4 (extreme Kh = cohomology of Ind(Lando)), Thm 10, Remark 14, Thm 13 (knots with n+1 nontrivial extreme groups) confirmed. Przytycki-Silvero 1608.03002 (Example 2.7: wedge of hexagons gives S^2 ∨ S^3; Thm 7.9 families; Conjecture 2.10) and 2305.18648 (Thm 1.5, Cor 1.6, Def. 9.1 "Khovanov adequate") confirmed. KWZ "Thin links and Conway spheres" (Compositio 160, 2024) abstract confirmed; details on special components not checked.

### salvage

Nothing proof-shaped. Recordable negatives: (1) the extreme Khovanov column of a knot can have zero Euler characteristic (GMS knot), so any Khovanov route to T must use a non-extreme column or the full χ; the forced residual statement is "if V_K = 1 then s(K) = 0 and Khr^{*,0}(K;Q) has odd rank ≥ 3 with χ = 1, all other columns having χ = 0", a parity count on the Lee column with no pillowcase content. (2) Rational-only decompositions exist for every knot, so KWZ geography constrains nothing about V unless the Conway sphere is essential; the only non-vacuous KWZ output is the thinness criterion, and thin knots already satisfy T via KM. (3) "Khovanov adequate" diagrams (PS Def. 9.1) with sign-coherent extreme columns give V ≠ 1 trivially; this is Bae-Morton/Lickorish-Thistlethwaite, not progress. Recommend closing the route and folding item (1) into route (5)'s board as a constraint.

### verdict

killed


## Agent: ref:circle-graphs


### route_title

Extreme coefficients via Lando-graph independence complexes (Conjecture R, one-ended realization)

### main_flaw

R is a Khovanov statement in disguise, and the clause p_E != 0 makes it unstable under connected sum. For any diagram D, 2p_A(D)-1 is the minimal quantum degree of the Khovanov chain complex of D, so p_A(D) <= (j_min Kh(K)+1)/2 for every D; when equality holds, Bae-Morton's coefficient I(G_A(D);-1) is +-chi(Kh^{*,j_min}(K)), a knot invariant (GMS). Hence "some diagram is A-sharp" iff [no Euler-characteristic cancellation at j_min Kh(K)] and [some diagram attains j_min Kh(K)]. The first bracket is a global non-cancellation property that R silently assumes for all knots at both ends: suppose one knot K2 has Kh(K2;Q) nonzero in a quantum degree strictly outside [2 min deg V-1, 2 max deg V+1]. Choose T a sum of 3_1, 3_1*, 4_1 (adequate; max degrees 4, -1, 2 generate Z) with max deg V_T = -max deg V_{K2}. K = T # K2 is nontrivial, max deg V_K = 0, and by multiplicativity of V plus the Kunneth formula for Khr(.;Q) (Khovanov, Patterns in knot cohomology I, 2003) the cancellation persists: j_min Kh(K) < 2 min deg V_K - 1, so no diagram of K is A-sharp, while every B-sharp diagram has p_B = 0. R fails. So R implies "for every knot the Jones extreme degrees equal the Khovanov extreme quantum degrees at both ends", a conjecture the builder never states, which already fails at the graph level (Przytycki-Silvero arXiv:2305.18648, Ex. 3.8: I(theta_{3k1,3k2,3k3}) = S^{m-1} v S^{m-2}, reduced Euler characteristic 0) and which GMS's H-thick constructions (extreme Kh in arbitrarily many homological degrees) make implausible. Even if no knot cancels, what remains is the open Khovanov realization problem with no mechanism, as the builder admits; and the class theorem is subsumed by Stoimenow math/0606255 (V != 1 for all semiadequate links, including adequate end at degree 0) except for the negative-forest family.

### counterexample_or_reason

Decisive cheap test (no computation done): T(4,5). Its positive 4-braid diagram has p_B = 15 while max deg V = 13 (for T(3,q) the two always agree, matching Przytycki-Silvero's T(3,q) extreme-Kh computation in arXiv:1608.03002; for T(4,m), m >= 5, the gap is (m-1)/2). If Kh(T(4,5)) is nonzero in q-degree 29 or 31 (a table lookup; the Knot Atlas page was unreachable), then K = T(4,5) # 4_1 # 3_1* has min deg V_K = 6-2-4 = 0 with an uncancellable B end, refuting R. The suggested knots do not bite: Kanenobu K(p,q) share V and Kh (Watson 2007) with Khovanov-sharp ends; 4_1 is alternating; 11n118's +-2 extreme coefficients only force |chi~| = 2 at any sharp diagram, and Manchon (2004) realizes every integer; EKT examples are links; Whitehead doubles have nonzero extreme coefficients and no known cancellation.

### principle_check

Formally passes (1): R uses exponent range and extreme coefficients, no evaluations, congruences or finite-type truncations. But its entire content is the Euler characteristic of one quantum level of Kh (one extreme Lando complex), the weakest admissible global datum and exactly where mixed-parity wedges occur. Side flag for the board: item (3) is misstated. 4_1 = closure of s1 s2^{-1} s1 s2^{-1} (n = 3, e = 0) has min deg V = -2 < (e-n+1)/2 = -1, and 3_1 = closure of s1^3 has max deg 4 > (e+n-1)/2 = 2; the correct diagrammatic bounds are p_A(D) <= min deg V <= max deg V <= p_B(D), and the tb <= -1 consequence should be re-derived from a correct source.

### literature_check

Four lookups. GMS arXiv:1511.05845: confirmed (extreme Khovanov cohomology = cohomology of the independence complex of the Lando graph; independence number = its Euler characteristic; H-thick knots with many extreme modules). Przytycki-Silvero arXiv:2305.18648: confirmed (4-braid I(w) is contractible, a sphere, a wedge of two spheres, or S^k v S^i v S^i (v S^i), k >= i; positive 4-braids: contractible, sphere or wedge of two; theta-graph example with spheres of adjacent dimensions; no explicit knot with vanishing extreme Jones coefficient). arXiv:1608.03002 computes extreme Kh of T(3,q). Stoimenow math/0606255 covers all semiadequate links. Kalfagianni-Lee 2108.12391 and Lee 1611.00686 not re-verified (consistent with memory). The builder's nesting claim in the lemma checks out: the non-oriented resmoothing at a negative crossing traverses the second Seifert circle backwards, so parallels of one negative crossing nest.

### salvage

(i) Theorem, no new input: gamma_A(K) := min deg V_K - max_D p_A(D) satisfies gamma_A(K) >= kappa_A(K) := min deg V_K - (j_min Kh(K)+1)/2 >= 0, with gamma_A = kappa_A = 0 iff some diagram attains j_min Kh(K) and chi there is nonzero; so the proposed invariant is sandwiched between the Khovanov cancellation gap and the Khovanov realization gap. A remark, not a route. (ii) The negative-forest lemma is a correct-looking small theorem (cyclic-order criterion for A-sharpness, extending Stoimenow JEMS 2005 beyond one negative crossing), publishable in a paper on Jones degree realization. (iii) The only version still implying T and immune to cancellation is R': every nontrivial knot has a diagram with nonzero extreme coefficient at an end with p_E != 0, or nonzero almost-extreme coefficient at an end with p_E = 0; this needs an almost-extreme Lando theory for non-adequate ends (Przytycki-Silvero 2020 covers adequate ends only) and is Stoimenow's semiadequate argument generalized, with no mechanism in sight.

### verdict

killed


## Agent: ref:arithmetic


### route_title

Burau_4 trace rigidity for closed 4-braids (C4) / arithmetic rigidity

### main_flaw

Three defects. (i) Reformulation: Lemma A is Jones's four-braid formula (Jones, Ann. Math. 126 (1987) §8, the [2,2]-rep of H_4 factoring through B_4→B_3; eq. (1) of Bigelow 2002, math/0012086; basis of KLS 2025), so (C4) is T_4 rewritten. (ii) False premise: "V=1 ⇒ e∈{±1,±3}" invokes board item (3), which is false: 4_1 = closure((σ_1σ_2^{-1})^2) ∈ B_3 has e=0 but min deg V=−2 < (e−n+1)/2=−1; 5_1 = closure(σ_1^5σ_2σ_3) ∈ B_4 has e=7 but max deg V=7 > (e+n−1)/2=5. True versions: min deg V=(e−n+1)/2 for positive braids (mirror for negative), and Franks-Williams-Morton e−n+1 ≤ deg_v P ≤ e+n−1 for HOMFLY. So |e|≤n−1 (and tb≤−1) follows from P=1, not from V=1; for 4-braids V=1 fixes only [3]tr ρ_4 + tr ρ_3∘π, not P, leaving e free, which is exactly why KLS obtain a family indexed by writhe. (C4) thus omits all |e|≥5; the claimed equivalence with T_4 is false; the "width-4 window" has width ~|e|/2. (iii) Value-blind mechanism: Datta's normal-form control, Squier unitarity and the t=i fingerprint apply verbatim to any target R, yet for general R the (V,e)-fibre on 4-braid knots contains several knot types (non-conjugate 3-braids with equal Burau trace, Birman 1985, counted by Datta's class numbers, stabilized to B_4; closures generically non-isotopic by the Birman-Menasco 3-braid classification). For R_e the solution set is the infinite union of exchange-move orbits (Morton 1983; Birman-Menasco unlink theorem), so the required rigidity is Birman-Menasco's topological argument re-run with V=1 replacing unknottedness: circular. Lemma B restates span R_e ≤ 4 (vacuous), and the trace's extreme term sums three diagonal entries, which Datta's "at least one row" theorem does not control.

### counterexample_or_reason

No counterexample to (C4) proper exists in the literature (T verified to 24 crossings; Kanenobu K(p,q), Whitehead doubles and EKT satellites are not 4-braid knots), so the kill is structural plus the explicit refutation of the e-restriction. Corrected identity (checked by hand): for odd e set N_e := (−1)^{e+1} t^{−e/2}[2] − [5] − 1 + t^e; with m=(1−e)/2, N_e(ω) = ω^m + ω^{m−1} + ω^{1−2m} = −ω^{m+1} + ω^{m+1} = 0 at primitive cube roots ω, so c_e := tN_e/(1+t+t^2) ∈ Z[t^{±1}] for every odd e (c_3 = t^2−2t, c_1 = 1−t−t^{−1} recovered). T_4 is then: no nontrivial 4-cycle β ∈ B_4 satisfies tr ρ_4(β) = c_e + tΔ_{closure(πβ)} for its own odd e.

### principle_check

Lemma A is global (fine). Lemma B uses only extreme degrees: permitted as "exponent range", but it holds on the whole infinite unknotted solution set, so it is a degree sieve of Jones-bound strength, not a separator. The fingerprint D'(i) ∈ (1−i)Z is a congruence at one root of unity (sieve by (1)) and vacuous: it is integrality of Δ_{β̂} via Burau's determinant formula, automatic for every knot closure. The "two-invariant principle" is a triviality (the unknot has V=1), not a theorem.

### literature_check

Bharathram-Birman-Brendle arXiv:2607.05283 exists (version Sept 2026; Columbia announcement Aug 2026) but is an unrefereed claimed proof, cited by the builder as settled; not load-bearing, since faithfulness only removes the Bigelow/Ito source. Korzun-Lanina-Sleptsov arXiv:2402.02553 (AIHPD 2025) confirmed: "a whole 1-parameter family, parameterised by the writhe number" of hypothetical HOMFLY-PT polynomials, no writhe bound, contradicting e∈{±1,±3}. Datta arXiv:2209.10826 confirmed, but its theorem is: for a generic positive 4-braid and prime p≠2, the leading coefficients of at least one row are nonzero mod p; "almost everywhere" is density; exceptional set unspecified in the abstract; nothing on traces. "Explicit exceptional family" overstates it.

### salvage

S1 (board correction): replace item (3) by the positive-braid equality, FWM for HOMFLY, and the bracket bounds min deg V ≥ (c_+ − 2c_− − s_A + 1)/2, max deg V ≤ (2c_+ − c_− + s_B − 1)/2 (s_A, s_B = all-A/all-B circle counts); the tb ≤ −1 claim needs P=1. S2 (the one honest non-reformulation target): Conjecture W4: every closed 4-braid knot with V=1 has |e| ≤ 3. True for the unknot (Birman-Menasco unlink theorem); implied by no degree bound; would cut KLS's family to four polynomials; it is what the builder silently assumed. Cheap first lemma from the bracket bounds: a Jones-trivial 4-braid has c_− ≥ (e−1)/2 and c_+ ≥ (−e−1)/2. S3: the all-odd-e identity above as the correct trace form of T_4.

### verdict

killed


## Agent: ref:representations


### route_title

Closed 4-braids: three-character decomposition of V, Burau_4 traces on the F_2-coset, unitary extremality

### main_flaw

The route has no mechanism beyond restating T for 4-braids, and its one "new step" is already published. Lemma B (three-character expansion; W(4,0) factoring through π: B_4→B_3 with σ_3↦σ_1 so χ_0 is the Jones polynomial of a 2-component 3-braid link L'; locking of the remaining Hecke characters, hence HOMFLY and Δ_K, to (V_{L'}, e)) is in the paper the builder cites only for "4-strand case open": Korzun-Lanina-Sleptsov, arXiv:2402.02553 (AIHPD 2025), Sec. 2.3 eq. 2.22 (R_1^{[2,2]}=R_3^{[2,2]}=R_1^{[2,1]}, a_{[2,2]} parametrized by 3-strand 2-component links) and Thm 3.2 (a Jones-trivial 4-braid knot has HOMFLY 1+(A²−q²)(A²−q⁴)(A²−q⁻²)(A²−q⁻⁴)F with writhe fixed and a_{[3,1]}, a_{[2,1,1]} expressed through the free a_{[2,2]}). KLS also already impose the Squier-unitarity/eigenvalue constraints on L' and prove (Thm 3.1) no nontrivial 4-braid knot has V=1 and Δ=1. So (J4), (†) and the "Alexander coupling" are KLS's equations in Temperley-Lieb notation, and the residue, Lemma C ("the fiber of f↦Tr Bur_4(fγ̃) through unknotted braids contains no knotted closure"), is T for 4-braids verbatim with no proposed mechanism; the builder concedes 3×3 trace non-rigidity. Lemma A never touches knots.

### counterexample_or_reason

No counterexample is possible: (S) is T restricted to closed 4-braids (verified through 24 crossings). The route is dead structurally. V_K=1 ⟺ Tr Bur_4(β)=B_{γ,e}(t), explicit from γ=π(β) and e, is an identity valid for every 4-braid, so it carries exactly the information of V_K; the coupling is the general fact that for any 4-braid, HOMFLY (hence Δ) is determined by (V_K, V_{L'}, e). The "corollaries" are empty: divisibility of the (J4) numerator by Φ_3 is V_K(ω)=1, automatic for every knot (Δ_2 vanishes at ω); B(1)=−1 is the S_4 standard character of a 4-cycle; neither constrains f. Unitary extremality: for a knot |⟨closure β⟩|=δ at the chosen roots against the bound δ⁴, nothing is near saturation; the mechanism detects only ρ(β) scalar, i.e. central braids. Lemma A's hypothesis forces n components and, by Jones's bound, e=0: it is a statement about links disjoint from T.

### principle_check

(J4), (†), the coupling: global identities, principle (1) not violated. Lemma A uses evaluations at all roots of unity simultaneously (permitted), but its honest content is: V=V(unlink_n) forces ρ(β)=λ_r·1 in the semisimple TL_n(δ_r) for every r≥n+2 (common scalar across p from the equality case), hence by Zariski density ρ(β)=±A^k·1 in TL_n(Z[A^{±1}]). Concluding β=1 needs the projective Jones/TL representation of B_n to have kernel equal to the center: for n=4 this is BBB Cor. 1.1 (a 2026 preprint, not yet refereed); for n≥5 it is open at generic A, and the asymptotic-faithfulness theorems cited (FWW 2002, Andersen 2006) are stated for closed surfaces; the punctured-sphere/braid-group version needs its own citation. So Lemma A is conditional, not "essentially proved". No finite-type or fixed-level leakage elsewhere.

### literature_check

(1) Bharathram-Birman-Brendle, "The Burau representation of the braid group is faithful for n=4", arXiv:2607.05283: exists, claims faithfulness with corollary that the Jones representation of B_4 is faithful; preprint status (Wikipedia lists it as a claim). (2) KLS arXiv:2402.02553 exists and, contrary to the builder's use, already contains the [2,2]-through-B_3 factorization, the L'-parametrization, the HOMFLY/Alexander locking (Thm 3.2), unitarity constraints on L', and Thm 3.1 (V=1 with Δ=1 impossible for 4-braids). (3) Datta arXiv:2204.13660 exists: class numbers of discriminant t²−4 forms equal counts of links of braid index ≤3 with prescribed invariants; it does not provide 3-braid unknot detection (that is Birman-Murasugi/Stoimenow 2011), and "generic 4-braids" is only an announcement, not usable input.

### salvage

Two precise statements, neither a route to T. (A′, link theorem, apparently new): if β∈B_n and V(closure β)=V(unlink_n), then β is pure with e=0 and ρ(β)=±A^k·1 in TL_n(Z[A^{±1}]); hence β=1 for n≤3, for n=4 given BBB, and for n≥5 given asymptotic faithfulness of the Jones representations of B_n (reference needed). Proof: at A=ie^{iπ/2r}, r≥n+2, all Δ_p>0 and ρ_p unitary, so |Σ_pΔ_pTrρ_p(β)|≤δ^n saturates only if ρ_p(β)=λ_rI with one λ_r, i.e. ρ(β)=λ_r·1 in semisimple TL_n(δ_r); Zariski density. (B′, reduction): by KLS Thm 3.1 plus the coupling, a Jones-trivial 4-braid knot would have Δ_K≠1 given explicitly by (V_{L'}, e), e∈{±1,±3}; since 3-braid links are classified (Murasugi; Birman 1985; Stoimenow 2011 computes their V), one can list the admissible L' for which Δ_{γ,e} is a symmetric integral polynomial compatible with Squier's signature on the unit circle. This constrains γ only (KLS already ran its unitarity part), never f, so it is a sieve on the base of the coset, not a proof.

### verdict

killed


## Agent: ref:symplectic


### route_title

ECN (extreme-column non-cancellation) as a Floer-compatible bridge from V to Khovanov rank

### main_flaw

ECN is false exactly where the route needs it: nothing ties Lee's generators at bidegrees (0, s±1) to the Jones span. ECN implies 2·mindeg V ≤ s ≤ 2·maxdeg V for every knot. Positive diagrams are A-adequate, so for a positive knot K' of genus g' the lower Lee generator (q = 2g'−1) is the extreme column; any K with V_K = V_{K'} (up to mirror) and |s(K)| < 2g' has a Lee generator outside the Jones span, so an extreme column of Kh(K) cancels. The smallest instance, 10_132 versus 5_1, sits in Bar-Natan's 2002 table. Lemma A is also refuted in the paper the builder cites: GMS Theorem 13 gives knot diagrams whose Lando independence complex has nonzero homology in n+1 consecutive degrees with binomial ranks, so reduced Euler characteristic 0; a nonzero potential extreme column is the true q_min of Kh(K), so ECN fails at the diagram-controlled end as well.

### counterexample_or_reason

10_132 (Knot Atlas): V = q^{-2}+q^{-4}−q^{-5}+q^{-6}−q^{-7}, i.e. V(5_1) up to mirror, so the unnormalized V~ is supported in [−15,−3]; σ = 0, g_4 = 1, u = 1, |s| = 2 (5_1: σ = −4, |s| = 4). Its rational Khovanov table has rows j = −1,−3,…,−15, and row j = −1 carries two generators with χ = 0. Hence maxdeg_q Kh = −1 > −3 = maxdeg V~, and the top column cancels (Lee pair at q = −3, −1 in the table's convention, the latter killed by a neighbour of opposite homological parity). GMS Theorem 13, n = 1: a knot diagram whose Lando graph is two hexagons sharing a vertex has extreme Khovanov groups Z in two adjacent homological degrees, χ = 0, so Lemma A fails and that knot's q_min column cancels. The ECN ⇒ T deduction itself (d_r of bidegree (1,4r) vanish, rank 2, Kronheimer-Mrowka) is correct; its hypothesis fails precisely for thick knots whose s is not read off V, which is the regime any Jones-trivial knot would occupy.

### principle_check

ECN passes (1): it uses V only through its exponent range, a global quantity; it dies empirically, not by principle. The proof mechanism, though, is a sieve: GMS controls only a diagram's potential extreme column, a non-invariant that becomes a knot invariant only when nonzero. For a Jones-trivial knot every diagram has Bae-Morton extreme coefficient 0, so Lemma A would reduce to acyclicity diagram by diagram, while the true extreme column of Kh(K) is invisible to every Lando graph. The Floer half is dead by the builder's own account (its Euler characteristic is det).

### literature_check

(i) Knot Atlas 10_132 page: s = 2 (sign convention mirrors the printed table), σ = 0, 4-genus 1, unknotting number 1, Jones polynomial and Khovanov table as quoted above. (ii) GMS, arXiv:1511.05845: Theorem 4 concerns the hypothetical degree j_min(D) of a diagram, H^{i,j_min}(D) ≅ H^{i−1+n}(X_D); 'any Lando graph is bipartite', but realizability of every bipartite circle graph is not claimed (Remark 11 gives a non-realizable bipartite graph), so the builder's transfer of Przytycki-Silvero's arbitrary wedges to knot diagrams is unavailable; Theorem 10 (link, extreme Z in degrees 0 and 1) and Theorem 13 (knots with n+1 nontrivial extreme groups, ranks C(n, i−n+1)) are as used above. (iii) Lee's d_r bidegree (1,4r) (Rasmussen, arXiv:math/0402131) and rank-2 detection (Kronheimer-Mrowka, arXiv:1005.4346) are correct and not load-bearing. The S^n ∨ S^{2n−1} attribution to P-S went unchecked; it is unnecessary.

### salvage

Nothing categorified survives. (a) Lemma 0, strengthened for free: a nontrivial Jones-trivial knot is thick, every Kh column with |q| ≥ 3 cancels, its Lee columns s±1 cancel if s ≠ 0, and each of its diagrams has Bae-Morton extreme coefficients 0, so every Lando complex is Q-acyclic or of GMS mixed type. (b) The only provable class statement: T holds for knots with a diagram D such that χ~(Ind(G_D^A)) ≠ 0 or χ~(Ind(G_D^B)) ≠ 0 (Bae-Morton 2003, arXiv:math/0012089; Manchón 2004); it contains semiadequate knots and grows with Przytycki-Silvero's wedge computations (cactus, outerplanar, permutation, non-nested Lando graphs, arXiv:1608.03002), but it is a diagrammatic sieve using no Khovanov homology. (c) Honest open question: realizability, whether q_min(Kh(K)) is always a potential degree of some diagram with non-acyclic Lando complex; 10_132's j = −1 column is the first test. None of this bears on T.

### verdict

killed


## Agent: ref:minimal


### route_title

Structure of a minimal Jones-trivial knot (geometric topology)

### main_flaw

No engine. Theorem S is a list of non-interacting necessary conditions; minimality enters only as primality. (a),(c),(d) are quotations; (f) is the tautology that a monomial misses one of two distinct potential extremes; (b) is the two-line corollary of Jones's bound and Rudolph's slice-Bennequin equality (quasipositive K: sl = 2g_4-1, so mindeg V >= g_4), folklore. Candidate C splits by winding number. Winding 0: one skein relation at the clasp gives V_{Wh±(C,0)} - 1 = unit·(t^{1/2}-t^{-1/2})(V_{∂A(C,0)} - V_{O_2}), so "T for untwisted doubles" is literally "J_3 detects the unknot", the n=3 instance of the open coloured-Jones detection problem, not easier than the n=2 instance T (only categorified versions exist: Hedden; Grigsby-Wehrli). Winding >= 1: degree domination is Kalfagianni-Tran's cabling analysis, valid only under hypotheses on deg J_n(C) at every colour (adequate, torus, iterated companions) and with a genuine degenerate slope. Hyperbolic K: nothing. Lemma B collapses into S(b): by Rudolph (quoted in Hedden, arXiv:math/0509499) D_+(C,t) is strongly quasipositive iff t <= TB(C), so Lemma B is "T for strongly quasipositive doubles". Its complement, TB(C) <= -1 and TB(C*) <= -1, contains every slice companion and is exactly the class S(a) puts Jones-trivial knots in: the sieve is blind precisely where it would matter.

### counterexample_or_reason

A counterexample to Candidate C would refute T, so none is known; the mechanism, however, has known failures. Eliahou-Kauffman-Thistlethwaite's Hopf-link satellites have V = V_unlink with nontrivial patterns: cross-colour cancellation is total because the Hopf link's coloured Jones degrees grow linearly, and linear growth at small colours is exactly what is unexcluded for non-adequate companions. Wh(U) = U shows the winding-0 expansion can cancel completely. Jones's braid bound cannot exclude cables: if C closes an m-braid of exponent sum e, C_{p,q} closes a pm-braid of exponent sum pe+(p-1)q, so V = 1 forces only |pe+(p-1)q| <= pm-1, a finite window of q for each (C,p). Minor error: (e)'s "Q in (0,0)" is unjustified; the Lee survivor sits at (0,s(K)) and s need not vanish.

### principle_check

The engines (Jones degree bounds, extreme degrees of unnormalised J_n) are exponent-range statements, so (1) is respected, and (c)-(e) are correctly labelled sieves. But the winding-0 reduction trades one single-colour Laurent polynomial (J_2) for another (J_3): a lateral move, the fixed-level trap in the colour direction, since no step uses several colours jointly. (f) uses one extreme coefficient per diagram (Bae-Morton, GMMS) and is vacuous: every diagram of a monomial-bracket knot satisfies it.

### literature_check

(i) Rudolph's criterion confirmed: Hedden (arXiv:math/0509499) quotes "D_+(K,n) is SQP iff n <= TB(K)"; Stoimenow's NYUAD slides (Oct 2025) restate it (A(K,t), W_+(K,t) SQP iff t >= -TB(K); W_- never SQP) in a talk on doubles and polynomial invariants, so Lemma B may be prior art. (ii) S(d) confirmed: Lowrance-Spyropoulos proved no Turaev genus one link has trivial V (cited in arXiv:2211.10009); Dasbach-Lowrance (arXiv:1812.11387) give Kh = Z in an extremal grading. (iii) Kalfagianni-Tran (arXiv:1501.01574, 1501.04614): cable degree formulas hold under hypotheses on the companion's degree and fail when the cabling slope is a Jones slope; obstacle 3 confirmed. (iv) mindeg V = g for positive knots (Fiedler; Stoimenow, JEMS 2005); the quasipositive bound mindeg V >= g_4 is its immediate slice-Bennequin analogue, not new.

### salvage

(S1) Proposition (folklore): K quasipositive with k bands on n strands implies mindeg V_K >= (k-n+1)/2 = g_4(K); so V_K = 1 forces K = U. (S2) Identity (skein relation at one clasp crossing: the crossing change unclasps to U, the smoothing is ∂A(C,t) with antiparallel orientation): V_{Wh+(C,t)} - V_{Wh+(U,t)} = t(t^{1/2}-t^{-1/2})(V_{∂A(C,t)} - V_{∂A(U,t)}) up to the clasp's sign; at t = 0, V_{Wh±(C,0)} = 1 iff V_{∂A(C,0)} = V_{O_2} iff J_3(C) = J_3(U). Bookkeeping, not a theorem. (S3) Theorem: t <= TB(C) implies mindeg V_{D_+(C,t)} >= 1; hence TB(C) >= 0 or TB(C*) >= 0 implies J_3(C) != J_3(U). Check Stoimenow 2025 for priority. (S4) The one lever: a Jones-trivial cable must satisfy, at each extreme, either the degeneracy pq = Jones slope or an explicit degree equation; with Kalfagianni-Tran's formulas for adequate, torus or iterated-cable companions these finitely many conditions on (p,q) should be inconsistent, giving "no cable of such a companion is Jones-trivial" (possibly implicit in their n = 2 formula).

### verdict

killed


## Agent: ref:statmech


### route_title

Myopic (projective) adequacy via Boyle-Spyropoulos; Potts positivity and Jones zeros

### main_flaw

The first lemma rests on "J^R_D = V_K for local K, one-sided states cancel", which is shading-dependent and false for one of the two checkerboard shadings of every non-disc diagram. Two-sided states have A-exponent class |E_-|-|E_+|-2|V|-2 (mod 4); the dual shading flips edge signs and swaps |V| for |F|, and Euler (|V|+|F|-|E|=1 for cellular D) shifts the class by 2. So for a local knot exactly one shading has J^R = V_K; the other has J^R identically 0 and J^I = V_K. The projective rank, Lambda_A and Lambda_B all change with the shading. Second: the bottom-degree formula c-2|V|+2-4n(S), used to identify the extreme states E-S_0 and to insert alpha_R(G), is the unsigned (alternating) formula; for a signed Tait graph the exponent is a(S)-b(S) = 2|S_+|-2|S_-|+|E_-|-|E_+|, so bottom states cluster around the all-B subgraph S_B, hitting sets must lie inside S_B, and alpha_R(G) is the wrong parameter. Third: Sum_{S_0} I(Lambda_B(S_0);-1) double counts states reachable from several minimum hitting sets (one-sided triangle: formula 0, true coefficient +-1). Fourth: once repaired, the top half is classical Bae-Morton on D, equivalently A-adequacy of the lifted planar diagram D~ of the split link K u K (bracket of D~ equals d times bracket(K)^2 up to a unit); and D~ is never adequate, since breadth V(K u K) = 2 breadth V_K + 1 is odd while adequacy forces 2c(D). The "projective leverage" (Upsilon_n, twist regions absorbed into alpha) concerns non-local knots only.

### counterexample_or_reason

Local unknot: take the 0-crossing circle meeting the line at infinity twice, push an arc across infinity and dip it over a far arc (R2 bigon): c = 2, Tait signs opposite. Shading bigon+exterior: G = one-sided digon, alpha = 1; two-sided states empty,{x1},{x2} contribute d + A^2 + A^-2 = 0, so J^R is identically 0 while the bracket 1 comes entirely from the one-sided state. Other shading: G = bouquet of two one-sided loops, alpha = 2, J^R = 1 = V. The candidate's conclusion breadth = c - alpha = 1 is escaped only because the bridge x1 of S_A lies in the Lando graph, which the builder's definition (chords with both ends on one circle) does not state. Kanenobu knots, Whitehead doubles and EKT links do not refute a sufficient condition; they threaten Conj. 1.1(2), as the builder concedes.

### principle_check

Breadth is global, so (1) is not violated. But the mechanism is chi(independence complex) = +-1 forced by a combinatorial emptiness hypothesis, exactly the S^3 wall: Kronheimer-Mrowka nonvanishing lives in homology (GMMS 2018 gives these complexes as extreme Khovanov), not in chi. For a local knot the lift is the split link K u K, so every RP^2-diagrammatic statement is a statement about the planar V_K; nothing new enters at the top, and the bottom side is a Drobotukhina-type count valid for alternating-type diagrams. Potts/Lee-Yang/zero-free arguments: the builder's own kill stands (Jin-Zhang-Dong-Tay 2010 confirmed; Jablonowski 2603.14585 confirmed).

### literature_check

Boyle-Spyropoulos: no arXiv record found; an Aug 2026 Sydney seminar listing describes it as forthcoming joint work (myopic Tutte polynomial, thin Khovanov homology for alternating links in RP^3, a "local crossing number"). The id arXiv:2609.40122 is unverifiable and numerically suspicious; Conj. 1.1, Thm 1.4 and Thm 5.3 must be treated as unconfirmed. Yang, Instantons and Khovanov homology in RP^3, arXiv:2402.15716: confirmed (reduced Kh mod 2 has dimension 1 iff unknot in class 0 or projective unknot in class 1). Jin-Zhang-Dong-Tay, EJC 17 (2010) R94: confirmed. Bae-Morton (arXiv:math/0012089) and GMMS (arXiv:1511.05845) as in context.

### salvage

Repaired statement: let D in RP^2 be a connected checkerboard diagram of a local knot K, with the shading in which the all-A subgraph S_A is two-sided (equivalently J^R_D = V_K). Then the coefficient of V_K at A-degree c + 2|s_A| - 2 is +-I(Lambda_A(D); -1), where Lambda_A consists of the bridges of S_A and the non-core loop chords, interlacing as edges; this is the Lando graph of D~ modulo the deck involution. If moreover S_B = E (B-alternating type), the bottom coefficient is +-Sum over two-sided S with n(S) = n(G) - alpha of (-1)^{k(S)}, alpha the projective rank in that shading. This hybrid of Bae-Morton and Drobotukhina is provable and worth one page, but it yields a knot beyond the semi-adequate/adequate ones only if such diagrams exist for non-adequate K, which nothing indicates; the only live question is that existence question, to be put to Boyle-Spyropoulos once the paper appears.

### verdict

killed


## Agent: synthesize

Seven reports arrived, not eight; all seven referees returned "killed". What follows ranks what survives repair; no route to T itself is on the table.

**Survivors with repair, ranked**

First, the extreme-coefficient route, which circle-graphs, symplectic and gauge built three times as R, ECN and C. The only form still implying T is the circle-graph referee's R′: every nontrivial knot has a diagram D and an end E with either p_E(D) ≠ 0 and nonzero extreme coefficient, or p_E(D) = 0 and nonzero almost-extreme coefficient. Mechanism: the extreme coefficient is ±χ of the independence complex of the Lando graph (Bae-Morton 2003), which González-Meneses-Manchón-Silvero (arXiv:1511.05845) identify with the extreme Khovanov column, so sharpness is a parity question about wedges of spheres. First lemma: the negative-forest Lando lemma, a cyclic-order criterion for A-sharpness when the negative crossings form a forest in the Seifert graph, extending Stoimenow (JEMS 2005) past one negative crossing. Strongest objection: the almost-extreme Lando description exists for adequate ends only (Przytycki-Silvero, Geom. Dedicata 2020), so R′ is Stoimenow's semiadequate argument with no non-adequate mechanism, and R itself is now explicitly refuted (below).

Second, the satellite half of the minimal route in the referee's S4 form: no cable C_{p,q} of an adequate, torus or iterated-cable companion is Jones-trivial. Mechanism: V of a cable is a Z[A^±]-combination of coloured Jones polynomials of C at colours up to p+1 (Morton; Rosso-Jones), whose degrees Kalfagianni-Tran (arXiv:1501.01574) give exactly for those companions, so the top colour dominates both ends unless pq is a Jones slope. First lemma: the builder's Lemma C, the two extreme-degree equations at colours p±1 are inconsistent for adequate C, with the degenerate slope handled rather than excluded. Objection: the degree hypotheses are exactly what a Jones-trivial knot's companion escapes; winding zero is "J_3 detects the unknot", a lateral move in the colour direction; hyperbolic K is untouched.

Third, the 4-braid route (arithmetic and representations are one route). Candidate: W4, every closed 4-braid knot with V = 1 has |e| ≤ 3; with the arithmetic referee's all-odd-e identity, T_4 reads: no nontrivial 4-cycle β ∈ B_4 satisfies tr ρ_4(β) = c_e + tΔ_{closure(πβ)}. Mechanism: the three-character decomposition of the bracket (Jones 1987 §8; Korzun-Lanina-Sleptsov arXiv:2402.02553), with Burau_4 faithfulness (Bharathram-Birman-Brendle arXiv:2607.05283, unrefereed) closing the Bigelow-Ito source. First lemma: B′, list the 3-braid links L′ whose (V_{L′}, e) yield a symmetric integral Δ compatible with Squier's signature, using KLS Thm 3.1. Objection: the mechanism is value-blind, the V = 1 fibre is an infinite union of exchange-move orbits (Morton 1983), so any rigidity re-runs Birman-Menasco with V = 1 in place of unknottedness, and 3×3 traces are not rigid.

**Killed**

Circle-graphs R: refuted (below). Symplectic/ECN: false; 10_132 (V = V(5_1) up to mirror, |s| = 2) has a cancelling top Khovanov column, GMS Thm 13 gives knots whose extreme column has χ = 0, and the Floer half's Euler characteristic is det. Gauge/C: the same conjecture; HHHK is the reduced Khovanov complex at chain level, the pillowcase adds nothing. Statmech: the myopic lemma's premise J^R = V_K holds for only one of the two shadings, its bottom-degree formula is the unsigned one, the Potts curve never enters the physical region, and the source paper ("arXiv:2609.40122") cannot be located. Arithmetic of V alone: any property shared by all V_K holds for 1. Unitary extremality: saturation forces ρ(β) scalar, so only central braids are detected. Minimal's Theorem S: necessary conditions with no engine, several of them wrong (below).

**Two first lemmas for this week**

The negative-forest Lando lemma. The referee verified the nesting claim and called the lemma correct-looking; its three parts need only Engström's fold lemma, the pendant-vertex suspension and the join formula; and it is the shortest path to a class theorem beyond semiadequate knots (negative-forest diagrams with g_c ≠ c_−). It also yields explicit families for the realizability question symplectic and gauge both ended on. Machine-check the four-site criterion, then run Przytycki-Silvero's wedge computations on the first cross-interlaced cases.

Lemma C for cables of adequate companions. Everything needed is in print (Morton's expansion, Kalfagianni-Tran's degree formulas, Kalfagianni-Lee), it is the only place a genuinely multi-colour mechanism bites, and the expected output, T for every cable of an adequate or torus knot, would be the broadest new class theorem of the round. Check first whether Kalfagianni-Tran's n = 2 formula already states it.

The representations referee's A′ (V(closure β) = V(unlink_n) forces β = 1 for n ≤ 4) is a cheap third but never touches knots.

**Cross-fertilization the builders missed**

R is refuted by combining two referees. The circle-graph referee's connected-sum argument waited on a Khovanov table for T(4,5); the symplectic referee's 10_132 supplies the cancelling end. Take K = 3_1^{#7} # 10_132, right-handed trefoils and the chirality of 10_132 with mindeg V = −7: mindeg V_K = 0, and by Künneth over Q the top column of Khr(K) has rank 2 and χ = 0, so no diagram is B-sharp and every A-sharp diagram has p_A = 0.

Board item (3) is false (4_1: e = 0, n = 3, mindeg V = −2; 3_1: maxdeg 4 > 2), as two referees found independently; the correct statements are the bracket bounds p_A(D) ≤ mindeg V ≤ maxdeg V ≤ p_B(D), equality mindeg V = (e−n+1)/2 for positive braids, and Franks-Williams-Morton for HOMFLY. Nobody carried this to the minimal route, whose S(a) (|e| ≤ n−1, sl ≤ −1, TB ≤ −1), S(b), Lemma B and the referee's "folklore" S1 all rest on it. I checked S1: it is false. 8_20 is quasipositive (up to mirror it closes σ_1^{−3}σ_2σ_1^{3}σ_2, two conjugates of σ_2 on three strands, so g_4 = 0), and V(8_20) = −t^{−5}+t^{−4}−t^{−3}+2t^{−2}−t^{−1}+2−t (det 9) has mindeg −5 or −1 by chirality, never ≥ 0. And a disk braided surface is a slice disk, not an unknotting, so S(b) could at most give slice. Both 4-braid builders and the representations referee also used "V = 1 forces e ∈ {±1, ±3}"; B′ must run over all odd e.

The gauge referee's residual "V_K = 1 forces s(K) = 0" is wrong (10_132 and 5_1 share V with |s| = 2 and 4); the minimal referee caught the same slip in S(e). The correct residual, from the symplectic referee: the Lee survivor sits at (0, s), every column of Khr(K;Q) has χ = 0 except q = 0 with χ = 1, and if s ≠ 0 the Lee column itself cancels.

Przytycki-Silvero's 4-braid classification (arXiv:2305.18648, Cor 1.6: the extreme group of a 4-braid closure is 0, Z, or Z[k] ⊕ Z^m[i], m ≤ 3) feeds the 4-braid route: for a Jones-trivial 4-braid knot, every braid diagram has, at each end not carrying the bracket's monomial, extreme group 0 or Z[k] ⊕ Z[i] with k, i of opposite parity, a word-level condition complementary to the trace identity.

**Assessment**

Nothing on the table has a mechanism for an arbitrary knot, and the project should say so. Three walls recur. Kronheimer-Mrowka gives rank and V gives Euler characteristic, and the one column where they were hoped to meet, the extreme column, can cancel (GMS Thm 13, 10_132), so the χ-to-rank gap is intrinsic, not a missing lemma. For 4-braids the character data is T_4 itself (KLS) and the solution set is infinite. Every satellite reduction trades J_2 for J_3. The round's honest output is a corrected board, an explicit refutation of R, two small theorems within reach and a sharper negative map; three errors passed referees, so run a cross-referee pass before any next round. A genuine mechanism would have to control the Euler characteristic of a non-extreme Khovanov column, or use several colours at once, which leaves V. Freeze route generation and spend the week on the two lemmas.
