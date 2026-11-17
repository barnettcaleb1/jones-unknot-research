# LIT lane REPORT: literature and novelty check (necklace calculus, Lemma Q, branch sets)
Lane: ~/jones-lanes/theory-restart/mont/lit/   Started 16 Nov 2026.   Status: COMPLETE (16 Nov 2026, evening)

Conventions: every source is tagged READ (opened the paper/abstract page myself), SNIPPET (search-result text only) or MEMORY
(standard reference not opened this session).
Every claim tagged PROVED / CHECKED(n) / CONJECTURE / GAP / KNOWN (= stated in a cited source).
Quotes are kept under 15 words.

## 0. Summary of verdicts
Answers in one line each: (1) NO prior Jones/bracket invariant of theta(K,h) with colours (axis 1, arc 2), and no necklace formula,
was found; neighbours are Sakuma's eta (abelian), Watson/KWZ/Lobb-Watson/Lipshitz-Sarkar (Khovanov), Collari-Lisca (equivariant
HOMFLY on symmetric diagrams), knotoid quantum invariants (endpoints not coloured), Yamada (all edges spin 1).  (2) The two-channel
collapse is an instance of standard Temperley-Lieb recoupling (V_1 (x) V_2 = V_1 (+) V_3); the published Montesinos/pretzel
colored-Jones fusion formulas (Lee-van der Veen; Garoufalidis-Lee-van der Veen; Elhamdadi-Hajij) always have EQUAL colours on the
two strands and are not single-channel products, so they do not contain our formula.  (3) Jones polynomials of these branch sets are
not studied anywhere I found; the Khovanov analogue is known (Hedden-Watson 2010; now KM + Gordon-Luecke); for torus knots the
branch sets are Montesinos (Lickorish-Thistlethwaite => V != 1).  (4) Jones-level "quotient tangle detects the unknot" is NOT known
for any class beyond what this program proved; Sikora (Canad. J. Math. 2024) shows the unrestricted version ("bracket detects
rational tangles") is EQUIVALENT to the Jones conjecture, and Lemma Q is its restriction to tangles with an unknot closure.

NOVELTY VERDICTS
- THEOREM N: NEW AS STATED (no trace found), KNOWN MECHANISM. A referee will see it as a routine recoupling computation:
  End(V_1 (x) V_2) = C P_1 (+) C P_3 commutative => necklace = channel-wise product; closure = fixed 6j weights (the Phi_3 = [3]
  denominator is the quantum dimension of V_2). Recommend proving it that way (1-2 pages) and presenting it as a tool, with the
  integral "box ring" R = {(a,b): a = b mod 1 - t^3} as the genuinely useful new packaging. Precedents to cite for flavour:
  multiplicativity of the Yamada polynomial under theta-curve connected sum; Eisermann-Lamm W_D(-1,t) = V(K+)V(K-) for symmetric unions.
- LEMMA Q for Montesinos horizontal inversions: NEW (not found). Position it as: special case of Sikora's Thm 9.2(c) restricted to
  quotient tangles; implied by the Jones conjecture (via Gordon-Luecke); Khovanov analogue known for ALL (K,h) (Watson Thm 1;
  KWZ rational-tangle detection). CAVEAT (PROVED here, 3.4(a)): Lemma Q is AUTOMATIC when a_2(K) != 0, since the normalised J is a
  unit only if J = 1, forcing a_2 = 0. All BRIEF headline examples (P(-2,3,7): a_2 = 12; T(3,5): 8; T(3,4): 5) are of this trivial
  kind. The substantive content is the a_2(K) = 0 Montesinos family; 789 such necklaces in the survey generator, none flat (4.0c).
- V(T(1/n)) != 1 for those branch sets: NOT IN THE LITERATURE for Montesinos/pretzel inversions (P(-2,3,7) branch sets are hyperbolic,
  not Montesinos, not arborescent -- assuming the standard exceptional-slope list, MEMORY, not re-checked). BUT (PROVED here modulo standard normalisations, 3.4(b)): if a_2(K) != 0 then V(T(1/n)) != 1
  for every even n != 0 and for all but at most one odd n, by Mullins' formula + Casson's surgery formula + the crossing-change
  signature bound. So for P(-2,3,7) the claim is classical except possibly one odd n; the new content is again the a_2 = 0 cases.

## 1. Q1: Jones-type invariants of theta-curves / quotient tangles of strongly invertible knots

### 1.1 Watson, "Khovanov homology and the symmetry group of a knot", arXiv:1311.1085, Adv. Math. 313 (2017) 915-946 [READ: full text extracted]
- Defines the quotient tangle exactly as we use it: restrict h to the exterior M_K, quotient is a ball, arcs = image of Fix(h);
  with equivariant meridional sutures this is a SUTURED tangle T_{K,h} with T(1/0) = trivial knot; one-to-one correspondence
  (K,h) <-> sutured tangles T with T(1/0) trivial. Adding half-twists does not change the sutured tangle (framing ambiguity).
- Invariant: inverse limit of reduced Khovanov homologies of the INTEGER closures T(i) (branch sets of S^3_i(K)), maps f_i from the
  crossing long exact sequence; kappa(K,h) = finite-dimensional quotient of that limit.
- Theorem 1 (KNOWN): kappa(K,h) = 0 iff K is trivial. Proof of the hard direction is NOT internal to Khovanov theory: stability
  Kh(T(n+1)) = Kh(T(n)) + F (n >> 0), then kappa = 0 forces dim Kh(T(n)) = det = n, Ozsvath-Szabo spectral sequence => S^3_n(K)
  L-space for all |n| >> 0 => g(K) = tau(K) = -tau(K) = 0.
- Mentions Sakuma's eta(K,h) as "an Alexander-like polynomial invariant" vanishing for the unknot but ALSO for some nontrivial (K,h)
  (amphicheiral with unique h, Sakuma Prop 3.4).
- Theorem 18: kappa of torus knots is thin, via lens-space surgery branch sets (two-bridge, Hodgson-Rubinstein).
- Conj 28 (dim kappa = 0 mod 4), Conj 29 (dim kappa independent of the inversion), Conj 30 (L-space knot iff kappa thin).
- NO Jones polynomial / Euler characteristic of the quotient tangle is studied; the Jones polynomial is mentioned only as
  the Euler characteristic of Kh and as an amphicheirality test (Sec 5).
- RELEVANCE: Theorem 1 is the KHOVANOV analogue of LEMMA Q (unknot detection by an invariant of the sutured quotient tangle), but:
  (a) it uses integer closures and an inverse limit, (b) its proof goes through Heegaard Floer / L-spaces, which has no
  Euler-characteristic shadow. Observation (CHECKED by hand on the trefoil, 1 case): chi(kappa(trefoil)) is NOT our J
  (kappa(3_1) is 6-dim thin, so |chi(-1)| = 6, while J(-1) = 1 by normalisation). So kappa does not decategorify to J in any
  naive way; "J unit" is rather the Jones-level analogue of "T is indistinguishable from the trivial sutured tangle".

### 1.2 Kotelskiy-Watson-Zibrowius, "Khovanov homology and strong inversions", arXiv:2104.13592, Open Book Series 5 (2022) 223-244 [READ: full text, see 1.9]
- One-to-one correspondence: strong inversions <-> special class of four-ended tangles; reduced Khovanov (immersed-curve) invariants
  of these tangles computed for all strong inversions of knots up to 9 crossings; counterexample to Watson Conj 29; evidence for Conj 28.
  Abstract does not mention Jones polynomials, unknot detection, Montesinos or pretzel knots.

### 1.4 Lipshitz-Sarkar, "Khovanov homology of strongly invertible knots and their quotients", arXiv:2203.13895, Proc. Sympos. Pure Math. 109 (2024) 157-182 [READ: full text grep]
- "Quotient knots" = arc K/h glued to one of the two halves of the axis (the two constituent knots e_0 u e_+ and e_0 u e_- of the
  theta-curve), viewed as annular knots around the axis. Spectral sequence (Smith theory on the Khovanov homotopy type) from Kh(K)
  to annular Kh of the pair (K^1, K^0). No Jones-polynomial statement in the paper (grep "Jones": no hits). Different object from J
  (J sees the whole theta-curve with the axis coloured, not a constituent knot).

### 1.5 Collari-Lisca, "A polynomial invariant of strongly involutive links", arXiv:2606.21471 (June 2026) [READ: intro + refs]
- Two-variable equivariant HOMFLY-PT analogue P^e via equivariant skein relations on TRANSVERGENT symmetric diagrams; its Jones-type
  specialisation = graded Euler characteristic J^e of page E_3 of the Lobb-Watson G-filtration spectral sequence = Couture's
  polynomial W of signed divides (Couture, Topology 47 (2008); AGT 9 (2009)). Uses an "equivariant Kauffman bracket" defined on
  unoriented involutive DIAGRAMS (closer to Khovanov's modified bracket). Thm 1.3: P^e = z^(l-1) P mod 2. Thm 1.2: distinguishes
  pretzel mutants K(5,3,3,2n,5), K(5,3,2n,3,5).
- No theta-curve / quotient-tangle bracket, no Jones-Wenzl colouring, no unknot-detection statement. Its J^e is a different
  invariant from our J (J^e = Jones mod 2; our J satisfies J(-1) = 1 and J''(-1) = -24 a_2(K), i.e. it is a quotient invariant).
- Useful reference list for the equivariant-invariant literature: Couture; Dai-Mallick-Stoffregen (J. Topol. 2023); Di Prisa;
  Di Prisa-Framba (AGT 2025); Miller-Powell (JLMS 2023); Boyle-Issa (J. Topol. 2022); Lamm arXiv:2210.13198 (symmetric diagrams
  of all strongly invertible knots up to 10 crossings).

### 1.6 Lobb-Watson, "A refinement of Khovanov homology", arXiv:1908.00082, Geom. Topol. 25 (2021) 1861-1917 [SNIPPET]
- (Note: the arXiv number 1610.04253 in the task is wrong; correct is 1908.00082.) Triply graded refinement of Kh for links with an
  involution, from a pair of filtrations; detects mutation for strongly invertible knots. Works on the symmetric diagram.

### 1.7 Knotoid side: Turaev; Barbensi-Buck-Harrington-Lackenby; Moltmaker; Gugumcu-Kauffman; Moltmaker-van der Veen
- DICTIONARY (KNOWN): Turaev (Knotoids, Osaka J. Math. 49 (2012)): spherical knotoids <-> SIMPLE theta-curves (e_- u e_+ unknotted),
  knotoid arc = e_0. Barbensi-Buck-Harrington-Lackenby, "Double branched covers of knotoids", arXiv:1811.09121, Comm. Anal. Geom.
  30 (2022) 1007-1057 [SNIPPET]: double branched cover along e_- u e_+ gives a bijection
  {knotoids in S^2 up to reversal/rotation} <-> {strongly invertible knots up to conjugacy}; hyperbolic (K,h) has exactly 4 oriented
  knotoids. CONSEQUENCE for us: our theta-curve theta(K,h) (axis = e_- u e_+, colour 1; arc = e_0, colour 2) IS the knotoid's theta
  curve, so J is a (1,1,2)-coloured quantum invariant of spherical knotoids. Barbensi-Goundaroulis arXiv:1909.08556: forbidden
  moves on knotoids = equivariant band moves on (K,h) = crossing changes of the theta-curve [SNIPPET].
- Moltmaker, "Framed knotoids and their quantum invariants", arXiv:2108.10246 (Commun. Math. Phys., DOI 10.1007/s00220-022-04382-1
  per arXiv page) [READ: full text grep, Sec 3.3]: RT invariants of BIFRAMED knotoids; the endpoints are represented by LINEAR MAPS
  THAT ARE NOT MODULE MAPS (Option 1) or via braided groups (Option 2); the shortcut edges e_+-, e_- are NOT coloured; example
  U_q(sl2) with V = fundamental rep on the knotoid strand. So this is NOT the honest coloured theta-graph evaluation; our J is not
  a special case of his construction as written.
- Gugumcu-Kauffman, "Quantum invariants of knotoids", Commun. Math. Phys. (2021) [SNIPPET]: Morse knotoids in the plane, state
  sums (bracket partition function, binary bracket). Planar setting; not the coloured theta-curve.
- Moltmaker-van der Veen, "New quantum invariants of planar knotoids", arXiv:2207.04894, Commun. Math. Phys. 402 (2023) [SNIPPET]:
  planar knotoids <-> simple H-curves; polynomial-time invariants; not the coloured theta evaluation.
- GAP (not found in the time available): any paper evaluating the Kauffman-Lins / RT invariant of theta(K,h) with colours
  (axis 1, arc 2), or equivalently the f_2-projected doubled-arc bracket of the quotient tangle.

### 1.8 Sakuma's eta-polynomial (Sakuma, "On strongly invertible knots", Algebraic and Topological Theories (Kinosaki 1984), Kinokuniya 1986, 176-196) [definition READ in Mukohara arXiv:2601.02230 Sec 4; original not accessible]
- Take a preferred longitude l of K with h(l) disjoint from l; in the quotient, O = image of Fix(h), L = image of l; then
  O u L is a 2-component link with lk(O,L) = 0 and eta(K,h)(t) = sum_i lk(L~', t^i L~) t^i in the infinite cyclic cover of S^3 - O
  (the Kojima-Yamasaki eta-function of O u L; Kojima-Yamasaki, Invent. Math. 54 (1979)).
- So eta is an ABELIAN (Alexander-type) invariant of exactly the quotient data our J uses (axis O plus the doubled arc). Watson
  (1311.1085) notes eta vanishes for the unknot but also for some nontrivial (K,h) (amphicheiral with unique h, Sakuma Prop 3.4),
  so eta does NOT detect the unknot. J is a QUANTUM analogue on the same data; no paper relating the two was found.
- Kodama-Sakuma, "Symmetry groups of prime knots up to 10 crossings", Knots 90 (Osaka 1990), de Gruyter 1992, 323-340 [SNIPPET via
  Watson's bibliography]: tables of symmetry groups / strong inversions, eta used to separate inversions.
- Hirasawa-Hiura-Sakuma, arXiv:2206.02097 (Essays in Geometry, EMS 2023, 325-349) [READ: ar5iv] and arXiv:2312.06156 ("The
  equivariant genera of marked strongly invertible knots associated with 2-bridge knots", v2 May 2024) [SNIPPET]: use theta(K,h) =
  O u k and its constituent knots, but only for invariant Seifert surfaces / equivariant genus (band, crosscap numbers). The Jones
  polynomial appears once (crosscap numbers of alternating links); no Kauffman bracket; no Montesinos results.
- Marumoto, Math. Sem. Notes Kobe Univ. 5 (1977) 377-388 [SNIPPET via Watson]: (K,h) is trivial iff K is trivial (unknot has a unique
  strong inversion). Calcut-Metcalf-Burton, "Double branched covers of theta-curves", arXiv:1509.07788, JKTR 2016 [SNIPPET]:
  primeness of theta-curves with an unknotted constituent via the double branched cover (a folklore theorem attributed to Thurston).

### 1.9 KWZ structure theorem for quotient-tangle multicurves (arXiv:2104.13592, Sec 3) [READ: full text]
- Theorem 3.1 (computer, all strong inversions of knots <= 9 crossings): Kh~(T_{K,h}) = r_1(k) u s_2(inf) u ... u s_2(inf), one
  rational component of integer slope k in 4Z plus n >= 1 special components of slope inf. kappa(K,h) = HF(a(0), special part);
  dim Kh~(tau(n)) = dim kappa + dim Kh~(T(2, n-k)). Counterexample 3.5 to Watson's Conj 29 (9_46: dim kappa 16 vs 28). Conj 3.6
  (= Watson Conj 28) and Conj 3.7 (special components are s_{2n}(inf)).
- For T(2,q) they record S^3_{+-1/n}(T_{2,q}) = Sigma(T*_{q,2qn-+1}) = Sigma(tau(+-1/n)) with tau(+-1/n) "an explicit Montesinos
  link" (the Montesinos involution) versus the torus knot (the Seifert involution); e.g. dim Kh~ 57 vs 15 for q = 5, n = 1.
- REMARK (this lane, CONJECTURE-level strategy, not a result): since chi of the Kh tangle invariant is the bracket vector, a flat T
  (J = 1) with K nontrivial would need the Euler characteristics of the special components (each s_2(inf) contributes the 4-dim
  V_kappa in one delta-grading to kappa) to cancel against each other and against the rational part. A grading argument showing such
  cancellation impossible would prove Lemma Q in general; this is the decategorification gap.

### 1.3 Elpers-Ibrahim-Moore, "Determinants of simple theta curves and symmetric graphs", arXiv:2211.00626 [READ: abstract page]
- det of a theta curve from H_1 of its Klein (Z/2 x Z/2) cover; for SIMPLE theta curves (a constituent unknot = our case) det =
  product of determinants of constituent knots. Determinant-level only (our J has J(-1) = 1 always, so invisible to J).


### 1.10 Answer to Q1
- No source found that evaluates a Kauffman-bracket / Jones-type invariant of the quotient theta-curve theta(K,h) with the axis
  coloured V_1 and the arc coloured V_2 (equivalently the coefficient [T]_0 of the bracket of the quotient tangle, i.e. our J), for
  Montesinos/pretzel knots or any other class; and no necklace / two-channel product formula or equivalent. GAP-free statement:
  "not found in: Watson 2017, KWZ 2022/2026, Lobb-Watson, Lipshitz-Sarkar, Collari-Lisca 2026, Sakuma/Kodama-Sakuma (via
  secondary sources), Hirasawa-Hiura-Sakuma, BBHL, Moltmaker, Moltmaker-van der Veen, Huh, Oshmarina-Vesnin, Sikora 2024".
- Nearest relatives: (i) Sakuma's eta = Kojima-Yamasaki eta-function of (axis image) u (longitude image) in the quotient: same
  quotient data, abelian; does not detect the unknot. (ii) Watson's kappa / KWZ multicurve of the quotient tangle: categorified,
  detects the unknot. (iii) Sikora's bracket ratio {T}_q of 2-tangles (general tangles; q-rationals). (iv) Yamada polynomial of
  theta-curves (all edges spin 1). (v) Knotoid quantum invariants (Moltmaker; Gugumcu-Kauffman), which do NOT colour the shortcut
  edges. Via Turaev + BBHL, J can be described as a (1,1,2)-coloured RT invariant of spherical knotoids; I found no such invariant.

## 2. Q2: Colored Jones of Montesinos knots via 6j / fusion

### 2.1 Lee-van der Veen, "Slopes for pretzel knots", arXiv:1602.04546, New York J. Math. 22 (2016) [READ: ar5iv text, Lemma 2.4]
- Colored Jones (all strands colour n) of 3-tangle pretzel P(r,s,t) from the THETA graph via knotted-trivalent-graph moves
  (triangle expansions, framing changes, unzips). Each twisted band is fused into its OWN channel a, b, c (even, in [0,2n],
  triangle inequalities); summand = prod of twist eigenvalues f(a)^r f(b)^s f(c)^t times theta evaluation times a squared
  normalised 6j-symbol Delta(a,b,c,n,n,n)^2. So channels are coupled by 6j-symbols; there is NO single shared channel.
### 2.2 Garoufalidis-Lee-van der Veen, "The slope conjecture for Montesinos knots", arXiv:1807.00957, Internat. J. Math. 31 (2020) [READ: full text grep, Sec 3]
- Fusion formula applied to the (n-cabled) NEGATIVE twist region only (one channel k_0, coefficient G_{k_0}(v) with theta factors),
  then a Kauffman state sum over the remaining crossings, organised by numbers of through strands. Again not a channel-product formula.
### 2.3 Other fusion-based pretzel work [SNIPPET]
- Garoufalidis-van der Veen, "Quadratic integer programming and the slope conjecture", arXiv:1405.5088 (2-fusion knots, contains
  pretzels as a 2-parameter family). Elhamdadi-Hajij, "Pretzel knots and q-series", Osaka J. Math. 54 (2017) (tails via
  false theta identities). Elhamdadi-Hajij-Saito (twist regions and coefficient stability). Beirne arXiv:1902.07061 (2-head of
  pretzel colored Jones).
- Hajij [SNIPPET]: "The bubble skein element and applications" arXiv:1212.2224 (JKTR 2014) and "The colored Kauffman skein relation and
  the head and tail of the colored Jones polynomial" arXiv:1401.4537 (JKTR 2017): skein expansions with n-coloured Jones-Wenzl
  idempotents for heads/tails; no mixed-colour box calculus visible in abstracts.
### 2.4 Assessment of the "two-channel collapse"
- In ALL of these the two strands of a twist region carry the SAME colour n (they are pieces of one knot), so channels run over
  {0,2,...,2n}. None treats a 2-string box with strands of DIFFERENT colours (1 and 2), which is what the quotient theta-curve forces.
- The mechanism behind THEOREM N is nevertheless standard Temperley-Lieb recoupling (Kauffman-Lins, "Temperley-Lieb recoupling
  theory and invariants of 3-manifolds", Ann. Math. Stud. 134 (1994); Masbaum-Vogel, "3-valent graphs and the Kauffman bracket",
  Pacific J. Math. 164 (1994)): V_1 (x) V_2 = V_1 (+) V_3 is multiplicity free => End(V_1 (x) V_2) is commutative with idempotents
  P_1, P_3 => boxes composed W->E act by scalars per channel => a necklace is a channel-wise product; the closure through the two
  trivalent vertices and the mu half-twists is a fixed 2x2 recoupling (6j) computation. KNOWN-mechanism, NEW-instance (not found).
  The pretzel formulas above are the same principle in a different direction of fusion (vertical bands vs our W->E necklace).


## 3. Q3: Branch sets of 1/n surgeries via Montesinos trick

### 3.1 Hedden-Watson, "Does Khovanov homology detect the unknot?", arXiv:0805.4423 (Amer. J. Math. 132 (2010) [journal ref SNIPPET]) [READ: ar5iv text]
- Theorem 1 (KNOWN): if K has TANGLE UNKNOTTING NUMBER ONE (equivalently Sigma_2(K) is Dehn surgery on a knot K', which is then
  strongly invertible, their Lemma 4), then rank Kh~(K; Z/2) = 1 iff K is the unknot. Includes all unknotting-number-one knots and
  ALL our branch sets T(1/n) (they are T(p/q) closures of a quotient tangle with T(1/0) = unknot).
- Proof: Ozsvath-Szabo spectral sequence |H_1| <= rk HF^(Sigma) <= rk Kh~; the hard case is 1/q surgery giving a Z-homology-sphere
  L-space, forcing K' = trefoil (genus bound + fiberedness: Kronheimer-Mrowka-Ozsvath-Szabo, Ghiggini, Ni); then K = P(-2,3,5) = 10_124
  by Schreier/strong inversions of torus knots, and rank Kh~(10_124) = 7 by computer.
- The Jones-polynomial version is explicitly left OPEN ("While the question remains open..." in their intro).
- COMMENT: post-2011 the Kh statement is subsumed by Kronheimer-Mrowka (Kh detects the unknot) + Gordon-Luecke (T(1/n) unknot =>
  S^3_{1/n}(K') = S^3 => K' trivial). So "Kh(T(1/n)) nontrivial for all n != 0 and nontrivial K'" is KNOWN; the Jones statement
  V(T(1/n)) != 1 is NOT implied by any of this (Euler characteristic can cancel).

### 3.2 Watson, "Surgery obstructions from Khovanov homology", arXiv:0807.1341, Selecta Math. 18 (2012) [READ: abstract page]
- Khovanov homological WIDTH of branch sets of fillings of strongly invertible knot exteriors obstructs lens-space and
  finite-pi_1 surgeries; computes width for a family of Montesinos links. No Jones-polynomial statement in the abstract.

### 3.3 Miyazawa, Osaka J. Math. 32 (1995) 193-206 [SNIPPET]
- For an unknotting-number-one knot K and a "surgical knot" C (strongly invertible, Sigma_2(K) = surgery on C): Arf(C) = a_2(K) mod 2
  (quoted in a snippet as "Arf(C) = a_2(K) (mod 2)"). Classical precedent for relating Conway coefficients of the branch set and
  of the strongly invertible surgical knot. Our identity J''(-1) = -24 a_2(K) is the same flavour; it should follow from Mullins'
  formula (Topology 32 (1993), Casson-Walker of Sigma_2(L) via V_L'(-1) and signature) plus Casson's surgery formula
  lambda(S^3_{1/n}(K)) = n a_2(K) (Mullins: SNIPPET only, exact constants not checked here).


### 3.3b Torus knots: branch sets are Montesinos links (KNOWN)
- For K = T(2,q) (and generally torus knots, whose strong inversion is unique), S^3_{1/n}(K) is a Seifert fibred homology sphere and
  the strong-inversion branch set T(1/n) is a Montesinos knot (KWZ 2104.13592 intro, READ; Watson 1311.1085 Sec 4 uses the same
  Seifert/Montesinos dichotomy). Lickorish-Thistlethwaite, Comment. Math. Helv. 63 (1988) 527-539 [SNIPPET]: reduced Montesinos
  diagrams are semi-adequate, hence nontrivial Jones polynomial. So V(T(1/n)) != 1 for torus knots is KNOWN (and Lemma Q for torus
  knots also follows from 3.4(a) since a_2(T(p,q)) = (p^2-1)(q^2-1)/24 > 0).
- For P(-2,3,7) the slopes 1/n (n != 0) are not exceptional (exceptional slopes are 16, 17, 18, 37/2, 19, 20 -- standard, from
  memory, not re-checked here), so S^3_{1/n} is hyperbolic and T(1/n) is a hyperbolic knot (orbifold theorem), NOT Montesinos and
  NOT arborescent (Bonahon-Siebenmann: arborescent => graph-manifold double cover). No general theorem covers its Jones polynomial.
- Watson, "A surgical perspective on quasi-alternating links", arXiv:0910.0449, Proc. Sympos. Pure Math. 82 (2011) 39-51 [READ: grep]
  draws and simplifies the quotient tangle of P(-2,3,q) (Figs 5-7) and shows certain INTEGER-surgery branch sets are quasi-alternating;
  nothing on 1/n branch sets or Jones polynomials.

### 3.4 OBSERVATION (this lane): a classical shortcut for V(T(1/n)) != 1 when a_2(K) != 0
Setting: K strongly invertible, T its quotient tangle, T(1/0) = unknot, L_n := T(1/n) (det 1, Sigma_2(L_n) = +-S^3_{1/n}(K)).
- (a) PROVED (from the BRIEF identity J''(-1) = -24 a_2(K)): the normalised J is a unit iff J = 1 (a unit +-t^k with
  J = 1 mod (t+1)^2 forces k = 0, sign +), and then J''(-1) = 0, so a_2(K) = 0. Hence LEMMA Q IS AUTOMATIC WHENEVER a_2(K) != 0.
  CHECKED(7) with lp.py: a_2 read off J equals 12 for P(-2,3,7) (Alexander = Lehmer L(-t)), 8 for T(3,5), 5 for T(3,4) = 8_19,
  2 for mont(-1,[3,7]), mont(1,[3,-3]), mont(2,[3,-3]), 6 for mont(1,[5,-5]). So all BRIEF headline examples are covered by a_2 alone.
- (b) PROVED modulo the normalisations of two standard formulas (checked in absolute value on T(3,5), T(3,7)):
  if V(L_n) = 1 then V'(-1) = 0, so Mullins (Topology 32 (1993)) gives lambda_Casson(Sigma_2(L_n)) = sigma(L_n)/8 (the V'(-1) term
  drops out, so its coefficient is irrelevant); Casson's surgery formula gives lambda(S^3_{1/n}(K)) = n a_2(K). Hence
  sigma(L_n) = eps * 8 n a_2(K) with eps = +-1 independent of n. Now L_n and L_{n-2} differ by ONE crossing change (one crossing of the
  n-crossing twist region of the 1/n rational tangle), so |sigma(L_n) - sigma(L_m)| <= |n - m| for n = m mod 2. Therefore:
  if V(L_n) = V(L_m) = 1 with n != m, n = m mod 2, then 8|a_2(K)| |n-m| <= |n-m|, i.e. a_2(K) = 0.
  Taking m = 0 (L_0 = unknot): IF a_2(K) != 0 THEN V(T(1/n)) != 1 FOR EVERY EVEN n != 0, AND FOR ALL BUT AT MOST ONE ODD n.
  (Uses only: Mullins' formula at V = 1, Casson's surgery formula, signature change <= 2 under a crossing change.)
  Consequence for the novelty question: for P(-2,3,7) (a_2 = 12) and torus knots, "V(T(1/n)) != 1" is classical except for at most
  one odd n; the genuinely Jones-level content of the program is in the a_2(K) = 0 cases. Status of (b): PROVED here; I did not find
  it stated in the literature, but it is the kind of argument that is folklore (cf. Ichihara-Wu arXiv:1606.03372 using V''(1) and
  surgery formulas for cosmetic surgery; Miyazawa 1995 for Arf/a_2). Recommend the proof lane re-derive the sign/normalisation once.

## 4. Q4: Quotient-tangle / J detects unknot beyond two-bridge?

### 4.0 Logical position of LEMMA Q (PROVED, elementary)
- Lemma Q is a CONSEQUENCE of the Jones unknot conjecture: if J = 1 then every T(1/n) has V = 1 (flat_search docstring /
  BRIEF), so V-detection would make every T(1/n) an unknot, so S^3_{1/n}(K) = S^3, so K is trivial by Gordon-Luecke (one n != 0
  suffices). Conversely Lemma Q does NOT imply the conjecture. So Lemma Q is a "family" special case: a counterexample to Lemma Q
  would give infinitely many nontrivial knots T(1/n) (n != 0) with V = 1 at once.
- Every tangle T with T(1/0) = unknot is the quotient tangle of some strongly invertible knot (Montesinos trick; Watson 1311.1085 states
  the bijection with sutured tangles). So Lemma Q <=> "no non-rational 4-ended tangle T with T(1/0) = unknot has the Kauffman bracket
  vector of a rational tangle (up to unit)".

### 4.0b KEY SOURCE: Sikora, "Tangle equations, the Jones conjecture, slopes of surfaces in tangle complements, and q-deformed
rationals", arXiv:2005.08162, Canad. J. Math. 76 (2024) 707-727, DOI 10.4153/S0008414X23000755 [READ: published PDF, Secs 1, 7-9]
- Bracket of a framed 2-tangle [T] = ([T]_0, [T]_inf) in Z[A^+-1]^2; KB ratio {T}_q = A^-2 [T]_inf/[T]_0 (framing independent);
  Thm 1.7: for rational tangles {<x>}_q = Morier-Genoud-Ovsienko q-rational [x]_q. Cor 7.2: the bracket distinguishes framed
  RATIONAL tangles from each other (classical-type statement, NOT detection of rationality).
- Thm 9.2 (KNOWN): the Jones unknot conjecture is EQUIVALENT to each of
  (a) [T] = (1,0) => T = <0> (framed);  (b) [T] = (r A^n, 0) => T = <0> unframed;
  (c) if [T'] = [T] with T rational then T' = T as framed tangles  ("the bracket detects rational tangles among ALL tangles").
  The proof of (a) => JC uses LOCALLY KNOTTED tangles K # <0>, whose closures contain K as a connected summand.
  Prop. after 9.2: JC up to N crossings => (c) whenever c(T) + c(T') < N; with Tuzun-Sikora (24 crossings) => tangles up to 11 crossings.
- Intro: Sikora announces he will "connect it with the theory of strongly invertible knots in an upcoming work" (re: the unframed
  Conjecture 1.4 that every solution of a system with a rational solution is rational). Prop 1.5: if L1 = L2 is a nontrivial rational
  or torus knot, the tangle system has no ALGEBRAIC tangle solutions (uses double branched covers / cosmetic surgery).
- POSITIONING OF LEMMA Q (PROVED, elementary): flat (J unit) <=> [T] equals the bracket of a framed integral tangle <n> up to framing
  (y monomial and u = y + delta x monomial pin the pair to the orbit of the twist operator P). So
      LEMMA Q  =  Sikora's statement (c) RESTRICTED to tangles T with an unknotted rational closure T(1/0)
               =  "the Kauffman bracket detects rational tangles among quotient tangles of strongly invertible knots".
  Sikora's equivalence (c) <=> JC does NOT restrict to this class (his reduction needs local knots, which never have an unknotted
  closure unless trivial). So Lemma Q is strictly a special case: JC => Lemma Q (via Gordon-Luecke, 4.0), converse unknown.
  For the two-bridge and Montesinos classes the program's results are therefore partial cases of Sikora's (c); I found no paper
  proving (c) for any infinite class of non-rational tangles with an unknot closure.

### 4.0c CHECK (this lane): does the BRIEF's survey reach the non-automatic regime a_2(K) = 0?  [script: lit/a2zero_survey.py]
- Same generator and seed as mont/survey_formula.py, first 20,000 necklaces (THEOREM-N formula level, not diagram level):
  789 have a_2 = 0 (3.9%); units among them: 0; minimum span of J among the a_2 = 0 cases: 10 (n=2), 15 (n=3), 21 (n=4).
  CHECKED(789). So the survey's "no unit J" evidence does include the cases where Lemma Q is not automatic; there J is far from a
  unit. (Runtime 4 s.)

### 4.1 Categorified versions are KNOWN (all via Kronheimer-Mrowka or Heegaard Floer)
- Watson (Adv. Math. 2017, arXiv:1311.1085) Thm 1: kappa(K,h) = 0 iff K trivial (proof via Ozsvath-Szabo spectral sequence, L-spaces,
  tau). [READ]
- Hedden-Watson (arXiv:0805.4423): Kh~ detects the unknot among tangle-unknotting-number-one knots (all T(p/q)). [READ]
- Kotelskiy-Watson-Zibrowius, "On mutation invariance in Khovanov homology", arXiv:2602.23442 (Feb 2026) [READ: full text grep]:
  states that both multicurve invariants HFT(T) and Kh~(T) "detect rational tangles" (more generally split tangles), citing
  Lidman-Moore-Zibrowius, "L-space knots have no essential Conway spheres", Geom. Topol. 26 (2022) 2065-2102, and Kotelskiy-Lidman-
  Moore-Watson-Zibrowius, "Cosmetic operations and Khovanov multicurves", arXiv:2109.14049 (Math. Ann. 2024, DOI 10.1007/s00208-023-
  02697-5 per search). Their Thm 3.17-type statement: the multicurve of T equals that of Q_{p/q} iff T = Q_{p/q}; the proof for
  general coefficients reduces to Kronheimer-Mrowka unknot detection via the closure rho(T) u T, plus Lemma 3.18 (two 4-ended tangles
  gluing to the unknot => one is rational). Applied to quotient tangles: Kh~(T_{K,h}) is rational iff K is the unknot.
  THIS IS EXACTLY THE KHOVANOV-HOMOLOGY ANALOGUE OF LEMMA Q, for ALL strongly invertible knots. Its decategorification fails to give
  Lemma Q only because a non-rational multicurve can have rational Euler characteristic (cancellation), the usual obstruction.


### 4.2 Answer to Q4
- Jones/bracket level: NOT KNOWN beyond rational/two-bridge-type statements. Known only: Sikora Cor 7.2 (bracket separates rational
  tangles from each other), Sikora Thm 9.2 (general detection <=> JC), Sikora Prop: JC up to 24 crossings => detection for tangles up
  to 11 crossings. The project's TH-2BR (two-bridge) and any Montesinos result would be the first infinite non-rational classes
  for the unknot-closure version, as far as this search shows.
- Knotoid side: Barbensi-Buck-Harrington-Lackenby detect the trivial knotoid via the double branched cover (topological, not Jones).
- Spatial-graph side: whether the Yamada polynomial detects trivial embeddings is reported OPEN (Fleming-Mellor, Kobe J. Math. 24
  (2007), SNIPPET); our J is a different colouring (1,1,2) of the same kind of question for simple theta-curves.

## 5. Source list (READ = I opened the paper or its abstract page; SNIPPET = search result only; MEMORY = standard reference, not opened)
READ (full text or substantial grep):
- Watson, arXiv:1311.1085, Adv. Math. 313 (2017) 915-946.
- Kotelskiy-Watson-Zibrowius, arXiv:2104.13592, Open Book Ser. 5 (2022) 223-244.
- Kotelskiy-Watson-Zibrowius, "On mutation invariance in Khovanov homology", arXiv:2602.23442 (2026).
- Lipshitz-Sarkar, arXiv:2203.13895, Proc. Sympos. Pure Math. 109 (2024) 157-182.
- Collari-Lisca, arXiv:2606.21471 (2026).
- Moltmaker, arXiv:2108.10246 (Commun. Math. Phys.).
- Lee-van der Veen, arXiv:1602.04546, New York J. Math. 22 (2016).
- Garoufalidis-Lee-van der Veen, arXiv:1807.00957, Internat. J. Math. (2020).
- Hedden-Watson, arXiv:0805.4423 (ar5iv text).
- Sikora, arXiv:2005.08162, Canad. J. Math. 76 (2024) 707-727.
- Eliahou-Kauffman-Thistlethwaite, Topology 42 (2003) 155-169 (intro).
- Mukohara, arXiv:2601.02230 (for the definition of Sakuma's eta).
- Watson, arXiv:0910.0449, Proc. Sympos. Pure Math. 82 (2011) (grep).
- Hirasawa-Hiura-Sakuma, arXiv:2206.02097 (ar5iv).
READ (abstract page only):
- Elpers-Ibrahim-Moore arXiv:2211.00626; Watson arXiv:0807.1341 (Selecta 18 (2012)); Watson arXiv:1010.3051 (Quantum Topol. 4 (2013));
  Barbensi-Buck-Harrington-Lackenby arXiv:1811.09121; Huh arXiv:2206.11450; Oshmarina-Vesnin arXiv:2404.12264; Costantino
  arXiv:0908.0542; Kotelskiy-Lidman-Moore-Watson-Zibrowius arXiv:2109.14049 (Math. Ann. 389 (2023) 2903-2930); Fleming-Mellor
  math/0510158 (abstract page did not show the Yamada remark).
SNIPPET:
- Sakuma 1986 (original); Kodama-Sakuma 1992; Marumoto 1977; Hirasawa-Hiura-Sakuma arXiv:2312.06156; Lobb-Watson arXiv:1908.00082
  (Geom. Topol. 25 (2021)); Boyle-Issa arXiv:2101.05413; Di Prisa-Framba arXiv:2303.08794; Calcut-Metcalf-Burton arXiv:1509.07788;
  Barbensi-Goundaroulis arXiv:1909.08556; Gugumcu-Kauffman (CMP 2021); Moltmaker-van der Veen arXiv:2207.04894; Elhamdadi-Hajij
  (Osaka J. Math. 54 (2017)); Hajij arXiv:1212.2224, arXiv:1401.4537; Garoufalidis-van der Veen arXiv:1405.5088; Beirne
  arXiv:1902.07061; Miyazawa (Osaka J. Math. 32 (1995)); Mullins (Topology 32 (1993)); Lickorish-Thistlethwaite (CMH 63 (1988));
  Eisermann-Lamm (Osaka J. Math. 48 (2011), arXiv:0802.2283); Tuzun-Sikora arXiv:2003.06724; Ichihara-Wu arXiv:1606.03372;
  Yamada (J. Graph Theory 13 (1989)); Lidman-Moore-Zibrowius (Geom. Topol. 26 (2022)); Huh-Jin math/0104179; Lamm arXiv:2210.13198.
MEMORY (not opened this session): Kauffman-Lins (Ann. Math. Stud. 134, 1994); Masbaum-Vogel (Pacific J. Math. 164, 1994);
  Kauffman-Vogel (JKTR 1, 1992); Turaev, Knotoids (Osaka J. Math. 49, 2012); Casson's surgery formula; Bonahon-Siebenmann;
  exceptional slopes of P(-2,3,7).
Correction to the task text: Lobb-Watson "A refinement of Khovanov homology" is arXiv:1908.00082, not 1610.04253.
