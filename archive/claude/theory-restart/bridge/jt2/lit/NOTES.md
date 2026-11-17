# JT_2 complexity: LIT role notes (prior art)
17 Nov 2026. Role: LIT (literature). Written continuously; newest log entries at bottom of the LOG section.
Status marks: PROVED / CHECKED(n) / CONJECTURE / GAP / FALSE. "VERIFIED-SOURCE" = I read the statement in the source
(abstract or full text); "RECALLED" = from memory, not re-checked in this session.

TARGET: JT_2 = {2-component link diagrams L : V_L = -(t^{1/2}+t^{-1/2})}. In C=P (L2_complexity Prop 2.1).
Questions (from task): (1) hardness of Jones-triviality / polynomial identity for knot & graph polynomials;
(2) planar Holant / #CSP dichotomies and exact zero-testing; (3) Kuperberg 2015, Kuperberg-Samperton, JVW,
Vertigan gadgets under SYMBOLIC identity; (4) all constructions of Jones-trivial links + mechanisms;
(5) TL realisability of tangle brackets.

## LOG
- 13:15 read CONTEXT, L2_complexity, STRESS (P4), bridge_complexity, depth_uniform_audit. Created this folder.
- 13:20 web searches (1): "trivial Jones" + C=P/coNP; Tutte-equivalence complexity; Lackenby sublink. NOTHING found on
  hardness of Jones-triviality or of polynomial-identity (equivalence) testing for Jones/Tutte/chromatic polynomials.
- 13:25 Kuperberg ToC 11 (2015) read in full text (scratchpad dl/kup15.txt). VERIFIED-SOURCE:
  * Thm 1.2: promise |V(L,t)|<a vs >b, t principal non-lattice root: #P-hard under COOK-TURING reductions; still
    #P-hard for knots. Proof = Solovay-Kitaev (FPTEAS precision) + FLW density + Aaronson PostBQP = PP.
  * Thm 1.3: planar Tutte, q=(x-1)(y-1)>4, x,y<0: #P-hard to approximate within any c>1.
  * Sec 5.2 OPEN QUESTIONS (verbatim gist): "Is the degree of the Jones polynomial intractable? Is it intractable to
    determine when some value of the Jones polynomial vanishes? What if the Jones polynomial is reduced mod p?"
    => as of 2015 even ZERO-TESTING AT ONE POINT was listed as open by Kuperberg. (symbolic identity not discussed)
  * Sec 5.3: integer gates generate discrete groups yet Hadamard+Toffoli (proportional to integer gates) are
    universal; "We do not know the right criteria on linear gates to establish #P-hardness results."
- 13:30 Goldberg-Guo-style / Galanis-Goldberg-Herrera-Poyatos (arXiv 2005.01076, complex Potts, planar #P-hardness of
  approximation): the problem definitions EXPLICITLY allow arbitrary output when Z = 0 (they avoid zero-testing);
  only uses the algebraic separation bound "Z = 0 or |Z| >= C^{-n}". No zero-test hardness. VERIFIED-SOURCE (grep).
- 13:32 Annan, DAM 57 (1995) 93-103: some Tutte coefficients #P-complete, others in P; for a hard coefficient,
  "is it < k" for fixed k is in P. (abstract-level VERIFIED-SOURCE). Relevance: coefficientwise hardness exists but
  is Turing; small-threshold questions are easy (cf. DEPTH-type phenomena).
- 13:35 Kuperberg-Samperton AGT 21 (2021) [arXiv 1907.05981] VERIFIED-SOURCE (intro): G fixed nonabelian simple,
  C nontrivial conj. class: #Q(K;G,C) (surjective C-colourings / Aut) is PARSIMONIOUSLY #P-complete for KNOT
  diagrams; Cor 1.2: deciding Q nonempty (equivalently #H(K;G,C) > #C, i.e. colouring invariant != unknot value) is
  NP-complete (Post-Karp). => "G-colouring invariant equals the unknot value" is coNP-complete, and
  "#Q(K1) = #Q(K2)" is C=P-complete (parsimony). THE ONLY EXACT-IDENTITY HARDNESS FOR A (finite-gauge-group,
  Dijkgraaf-Witten type) QUANTUM INVARIANT OF KNOTS that I know. Mechanism: braid group acts by PERMUTATIONS on
  G-colourings of the punctured disk (classical reversible computation), "zombie" symbols, Valiant-Vazirani.
  Kuperberg-Samperton G&T 22 (2018) [1707.03811]: same for homology 3-spheres (mapping class groups, Heegaard).
- 13:40 EKT Topology 42 (2003) full text (Kauffman's homepage, scratchpad dl/ekt.txt). VERIFIED-SOURCE:
  * Prop 2.1: <H(T,U)> = delta*{ g <(T+U)^N> + <T^N><U^N> - g <T^D><U^D> }, g = a^-8 - 2a^-4 + 2 - 2a^4 + a^8.
    MY CHECK: with t = a^-4, g = t^-2 (t-1)^2 (t^2+1). So the "difference term" carries a DOUBLE zero at t = 1
    built in (and zeros at t = +-i). [CHECKED by hand: t^4-2t^3+2t^2-2t+1 = (t-1)^2(t^2+1).]
  * Prop 2.1': <H(T,U)> = br(T)^t H br(U), H = [[h00, delta^2],[delta^2, delta]],
    h00 = <H(0,0)> = -a^-14 - a^-6 - 2a^-2 - 2a^2 - a^6 - a^14 (2-parallel of Hopf).
  * Sec 3: T^w = (T+2).1.2 (a fixed 5-crossing boundary homeomorphism, interchanges SW/SE ends);
    br(T^w) = W br(T), W = M+^2 M* M+ (explicit 2x2 over Z[a^+-1]); Thm 3.2: W^t H W^-1 = H, so
    <H(T,U)> = <H(T^w, U^w')>; w^2 preserves writhe => Jones equal (Thm 3.2').
  * Thm 3.3: for ANY non-split k-component L there are infinitely many inequivalent PRIME (k+1)-component links
    with V = u V_L (u = -t^-1/2 - t^1/2). Cor 3.3.1: infinitely many prime Jones-trivial k-component links, k>=2.
  * Sec 4: LL2(n) = H(T_n, -T_n), T_n = w^n(inf - 2) rational; V = u for n even; for n even these are BOUNDARY
    links, so Alexander polynomial = 0 as well. LL1(m,n) two-parameter family; LLL(n) 3-component family.
  * Remark 5.2: all these links are effectively classifiable (sublinks alternating, Hopf satellites).
    Remark 5.4: 2-clasp pattern generalisation gives 4- and 5-component examples.
  * MECHANISM in one line: an ISOMETRY W of the bilinear "pairing form" H on bracket vectors that is realised by a
    tangle-boundary homeomorphism; W acts as a 2x2 matrix in GL_2(Z[a^+-1]) on TL_2 coordinates.
- 13:45 Eliahou-Fromentin JKTR 26 (2017) [1610.05560] full text VERIFIED-SOURCE: T10 = T8,21 * 2, T20 = T10 + (-T10),
  br(T20) == (1,0) mod 2; M_r = M_{r-1} + M_{r-1} (horizontal sum = multiplication in TL_2 = R[e]/(e^2 - delta e));
  (1 + 2^{r-1}P)^2 = 1 + 2^r(...) => br(M_r) == (1,0) mod 2^r; K_r = den(1 * M_r) knot, V(K_r) == 1 mod 2^r,
  20*2^{r-1}+1 crossings (EXPONENTIAL in r). Open questions they pose: tangle with bracket pair trivial mod m for odd
  m? trivial over Z? (=> nontrivial knot with V = 1). NOTE the 2-adic deepening works because squaring raises
  2-adic order (Frobenius); the (t-1)-adic analogue FAILS in the commutative TL_2 (squaring keeps order), so depth
  in t-1 must come from NON-commutativity (commutators in TL_n, n >= 3) -- see analysis section.
- 13:47 Watson MSc thesis (UBC 2004?) ch.6 re-derives EKT via braid actions on S2 x S2 (tangle pairs), Fix(w).
  Thistlethwaite's original 2001 links = LL1(0,-2), LL1(0,-1), LL1(0,0), LL1(0,1) (2-comp) and LLL(0) (3-comp)
  per EKT Remark 5.1.
- 13:55 Kuperberg 2015 Sec 3.5 (knot clause of Thm 1.2) VERIFIED-SOURCE: link -> knot via DENSITY of the PURE braid
  group image ("switch two strands, then approximately cancel its effect with a pure braid"). All three
  ingredients (Solovay-Kitaev at precision exp(-poly), FLW density, approximate cancellation) are ANALYTIC at a
  fixed non-lattice root; none has meaning for identity in Z[A^+-1] (image of B_n there is a discrete group, no
  topology to approximate in, except possibly the (A-1)-adic one -- see analysis).
- 14:00 Cai-Maran-Young, "Planar graph homomorphisms: a dichotomy and a barrier from quantum groups",
  arXiv 2601.23198 (Jan 2026) VERIFIED-SOURCE (intro + Sec on Qut): Thm 36: for M in Sym_q(R>=0),
  K(M)_ii = K(M)_jj for every PLANAR edge gadget K iff i,j in the same orbit of the quantum automorphism group
  Qut(M) (via Mancinska-Roberson / Lupini-Mancinska-Roberson); Thm 39: deciding whether a planar edge gadget can
  separate i,j is UNDECIDABLE (from undecidability of quantum isomorphism, Atserias et al. JCTB 2019 + Slofstra).
  Remark 40: quantum-isomorphic non-isomorphic pairs can be separated only by NONPLANAR gadgets.
  LESSON FOR JT_2: planar gadget expressivity = intertwiners of a quantum group. For the Kauffman bracket at
  generic A the planar gadgets realise exactly (a subset of) Temperley-Lieb = U_q(sl2)-intertwiners; this is the
  formal content of "no classical spins" (L2 4.2). It is a barrier to porting NONPLANAR gadget techniques.
- 14:02 Mancinska-Roberson FOCS 2020 (arXiv 1910.06958): quantum isomorphic iff equal hom counts from all planar
  graphs; hence "equality of planar partition functions over ALL planar instances" is UNDECIDABLE. The only
  'identity over a family' hardness for planar partition functions I found; different quantifier structure
  (all instances) from JT_2 (one instance, identity in the parameter t).
- 14:05 Graph-polynomial equivalence (identity) testing: OPEN in the literature. Bukovac-Farr-Morgan, JGAA 23 (2019)
  227-269 "Short certificates for chromatic equivalence": certificates = sequences of algebraic rewriting steps;
  chromatic equivalence in NP IF shortest certificates are poly-bounded (open); lower bound Omega(n^2/log n) for
  some pairs (counting argument); trees linear. No hardness claimed. Farr-Morgan arXiv 2406.15746 (2024) open
  questions; Makowsky school studies "distinguishing power" (semantic), not decision complexity.
  => The analogous "short certificate of Jones-equality" (sequences of mutation / rotor / EKT-omega / Kanenobu
  moves + skein rewriting) is the NP-side mirror of the JT_2 hardness question.
- 14:07 Sikora, Canad. J. Math 76 (2024) 707-727 [arXiv 2005.08162] VERIFIED-SOURCE (Secs 5-9): realisability
  constraints on 2-tangle bracket pairs ([T]_0,[T]_inf): Prop 16 (gcd divides [L] for any L containing T, and
  [L] in ideal <[T]_0,[T]_inf>; generalises Krebes 1999 (A = e^{pi i/4}) and Ruberman 2000); Prop 17 (exponents of
  [T]_tau congruent to 3w + 2|T| + 2eta(T) + delta_tau mod 4: parity/type constraint); [T]_0,[T]_inf never both 0
  (A = +-1 evaluation); Thm 7 (rational tangles <-> q-rationals of Morier-Genoud-Ovsienko); Cor 20 bracket
  distinguishes framed rational tangles among rational ones; Thm 3: JC => systems of tangle equations with a
  rational solution have it unique among all 2-tangles.
- 14:08 Aiello-Baader-Ferretti, Glasgow Math J 65 (2023) 730-734 [arXiv 2204.12259]: density of knot Jones
  polynomials mod p in large degree range <= 4/p^7; mod-2 classification for span <= 8. (abstract-level)
  Realisation of Jones polynomials of knots ("characterise V_K in Z[t^+-1]") is an OPEN problem (Kirby-list
  style problem list math/0406190).
- 14:10 Ito, Math Z 280 (2015) 347-353 [arXiv 1402.2028] (abstract): any non-trivial non-central normal subgroup of
  B_n contains a braid whose closure is a hyperbolic knot of arbitrarily large genus; so an unfaithful quantum
  braid representation => the quantum invariant fails to detect the unknot. Bigelow JKTR 2002 [math/0012086]:
  a nontrivial 4-braid in ker(Burau) "almost certainly" suffices for a nontrivial knot with V = 1.
- 14:12 UNVERIFIED CLAIM, do not rely on: Carmi-Cohen arXiv 2606.22410 (21 Jun 2026) "On trivial Jones-Vassiliev
  polynomials" claims a proof of JC (nonzero Jones finite-type coefficient at order <= 3c(K)). Since span V <= c,
  that statement is EQUIVALENT to JC, so the claim is a full proof claim; v1, not refereed. Flag only.
- 14:20 Nikkuni, JKTR 26 (2017) 1750029 [arXiv 1602.02584] (abstract VERIFIED-SOURCE): for n >= 3, if oriented
  links L, M are C_n-equivalent (Habiro clasper / C_n-move) then V_L - V_M is divisible by
  (t-1)^n (t^2+t+1)(t^2+1), and this divisor is ATTAINED by a pair of C_n-equivalent knots. (Search snippet of
  full text: V_L^{(l)}(1) = V_M^{(l)}(1) for l <= n-1 iff V_L - V_M divisible by (t-1)^n (t^2+t+1); not checked.)
  RELEVANCE: this is the published "difference term with prescribed depth" tool. Note the forced factors are
  Phi_1^n Phi_3 Phi_4 only: NOT Phi_2 (t=-1, determinant) and NOT Phi_6 (t=e^{i pi/3}, Z/3-homology of Sigma_2).
  Habiro (G&T 4, 2000): knots share all finite-type invariants of degree <= n-1 iff C_n-equivalent.
- 14:22 HLP J. ACM 46 (1999) [math/9807016] VERIFIED-SOURCE (scratchpad stress/hlp/hlp.txt): Thm 1.1 UNKNOTTING in NP;
  Thm 1.2 SPLITTING in NP. => UNLINK_2 (is a 2-component diagram the trivial link?) is in NP (certificate:
  splitting sphere + unknotting disks for each component sub-diagram). PROVED (combination).
- 14:24 Lackenby (Adv. Math 2021, arXiv 1604.00290): knottedness in NP (knots only; Thurston norm in NP).
  Lackenby DCG 58 (2017) [1602.08427]: sublink problem NP-hard; Thurston-norm bound for links NP-complete.
  de Mesmay-Rieck-Sedgwick-Tancer, Adv. Math (2021) [1810.03502]: NP-hard: unknot diagram untangling with <= k
  Reidemeister moves; trivial sublink with n components; unlinking number; several 4-dim invariants. Gadgets:
  Borromean rings / Brunnian links. Koenig-Tsvietkova, Trans AMS Ser B (2021) [1809.10334]: NP-hard sublink-is-unlink,
  Brunnian clause gadgets, Karp reduction from 3-SAT. ALL are EXISTENTIAL (choose components); none concerns a
  polynomial identity. They show Brunnian links are the standard "clause" device in link complexity.
- 14:26 Stoimenow, Crelle 657 (2011) [math/0606255] (as restated in Lowrance-Spyropoulos 1707.05443): L semiadequate
  and V_L = t^k (-t^1/2 - t^-1/2)^{l-1} => k = 0 and L is the l-component unlink. Lowrance-Spyropoulos 2017: same
  for almost alternating and Turaev genus one links. Thistlethwaite (1987/88): adequate links nontrivial V.
  => JT_2 restricted to (semi)adequate / almost-alternating / Turaev-genus-1 DIAGRAMS reduces to UNLINK_2 on them.
- 14:28 Kuperberg G&T 15 (2011) 11-39 [0911.2188] (abstract): Jones braid reps are Zariski dense when q is not a
  root of unity (and at non-lattice roots except one order-10 case). Kuperberg-Ming: transcendental A, image Zariski
  dense in SL of TQFT spaces. => at generic A there is NO algebraic obstruction (Zariski closure is everything);
  obstructions for exact symbolic identities must be ARITHMETIC (integrality over Z[A^+-1]) or TOPOLOGICAL.
