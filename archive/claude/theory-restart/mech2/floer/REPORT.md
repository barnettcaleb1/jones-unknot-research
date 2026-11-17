# REPORT — LENS FLOER (sutured spectral sequence and its gradings)

STATUS (2026-11-16): complete draft; SUMMARY at the end.  Marks: PROVED / CITED (source, number, read-now or recalled) / DATA / CONJECTURED.
HEADLINE (section 7): a strongly invertible knot (word s.r1.x2.y1.y0.r2.y0.y1.y0.y1.x2.u3.u1, 13 crossings, rank HFK^ = 17) whose quotient tangle VIOLATES END, NP, TILT and the
polygon law (two generators of N in the top quantum degree, in adjacent homological degrees; the same over F_2, F_3 and Q).  Lemma Q is not contradicted (J != 1).
The offending squares belong to a J-neutral (v,w)-quadruple of four squares whose 16 generators account exactly for dim N - rank HFK^(K) = 33 - 17 (section 8).

## 1. THEOREM S pinned in the literature

### 1.1 Grigsby-Wehrli, arXiv:0807.1432 ("On the colored Jones polynomial, sutured Floer homology, and knot Floer homology")
READ NOW (TeX source SFHExact9.tex dated 13 Oct 2008, local copy lit/recent/src/0807.1432/; numbering = arXiv version, counted from the source).

- [CITED, read now] Def 5.1/5.2: an ADMISSIBLE tangle in D x I (I = [-1,4]) is an unoriented properly embedded 1-manifold with boundary in Int(D_+) u Int(D_-),
  up to isotopy acting trivially on (dD) x I; BALANCED means #(T n D_+) = #(T n D_-).  [So twisting the two ends in D_+ is an equivalence: this is why N(T) = N(T sigma^n).]
- [CITED, read now] Def 5.7-5.12 (Khovanov functor): for a resolved tangle T, V(T) = 0 if T backtracks (some arc has both ends on D_+ or both on D_-), and otherwise
  V(T) = Lambda^* Z(T), Z(T) = span of the closed circles (arc components are set to 0).  Merge = quotient map, split = wedge with [T_i]+[T_j], zero map across a "zero saddle"
  (one side backtracks).  CV(P(T)) = cube complex over {0,1}^l.  This is, term by term, our F_b C(T): through-resolutions = b, backtracking = c -> 0, dots on the two through
  strands -> 0.  Remark 5.9: V(T) = Z_2 (x) (_eZ (x)_{H^n} F(T)), _eZ the 1-dimensional H^n-module of Khovanov's coloured construction.
- [CITED, read now] Def 5.13/5.14: gradings on CV: i(a) = -n_+ + sum m_i ;  j(a) = dim Z - 2d + n_- - 2n_+ + sum m_i  (a in Lambda^d Z).  The differential has bidegree (1,0).
- [CITED, read now] PROPOSITION 5.20: "Let T in D x I be an admissible, balanced tangle. Then there is a spectral sequence whose E^2 term is V(T) and whose E^infinity
  term is SFH(Sigma(D x I, T))."  (Theorem 5.19 = Theorem 1.2/"Theorem A" is the special case of cables T^n of a long knot.)  Hypotheses: admissible + balanced; Z_2 coefficients
  throughout ("all Khovanov and Heegaard Floer homology theories will be considered with Z_2 coefficients", Introduction).  Proof: sutured link surgeries spectral sequence
  (Prop 4.1, filtered complex X^(0,1) = sum over {0,1}^l of CFH(Y(I)), D = D_0 + D_1 + ... + D_l, D_k counts holomorphic (k+2)-gons) + Prop 5.17 (the Khovanov functor and
  the sutured Floer functor agree on resolved tangles and saddles, analogue of Ozsvath-Szabo Prop 6.1).
- [CITED, read now] MIRROR: Remark 5.15: "Kh~_n(mirror K) := V(T^n) ... mirror K appears, as in [OS], because Khovanov and Ozsvath-Szabo use opposite conventions for the 0 and 1
  resolutions."  So with Khovanov's (= Bar-Natan's = kht++'s) resolution convention the E^2 page is the Khovanov homology of the MIRROR tangle: E^2 = N(mirror T), as in THEOREM S.
  (For rank statements the mirror is irrelevant: N(mirror T) is the dual of N(T).)
- [CITED, read now] Def 2.11: the sutured branched double cover Sigma((Y,Gamma),B) has sutures pi^{-1}(s(Gamma)).  Example 2.6: (Y - N(K), two oppositely oriented meridional
  sutures) has SFH = HFK^(Y,K) (Juhasz, Holomorphic discs and sutured manifolds, Prop 9.2; quoted there).  Theorem 6.1: SFH(Sigma(D x I, T^n)) = HF^(Sigma(K)) (n=1),
  HFK^(S^3, K # K^r) (n even), HFK^(Sigma(K), K~) (n > 1 odd).
- [CITED, read now] GRADINGS, Section 7: with D_0 = 0, X^(0,1) = CV(P(T)) as a vector space, and "it is easy to see that D_k raises the i grading by k, raises the j grading
  by 2(k-1), and thus lowers delta := j/2 - i by 1" (asserted, no proof given).  CONJECTURE 7.1: there is a lift M of the relative Maslov grading M_SF with
  E^infinity_{delta = d} = SFH(Sigma(D x I,T))_{M = d}.  Corollary 7.3 (of the conjecture): liminf hw(Kh~_n(K))/2(n-1) >= g(K).
  => In the source of THEOREM S the bidegree (k, 2k-2) of the higher differentials is an ASSERTION WITHOUT PROOF, and the comparison delta <-> Maslov is a CONJECTURE.
     (See section 2 below for what is actually proved elsewhere.)

### 1.2 Our identification (PROVED, elementary; checked against GW's definitions)
Let (K,h) be strongly invertible, A = Fix(h), q: S^3 -> S^3/h = S^3.  q(K) is an arc with ends on the unknot q(A); a ball neighbourhood B of q(K) meets q(A) in a trivial
2-string tangle and q^{-1}(B) = N(K).  B' = S^3 - B, T = q(A) n B' is the quotient tangle and q^{-1}(B') = S^3 - N(K) is the double cover of B' branched along T.
Parametrise B' = D x I so that the suture dD x {pt} bounds a disc in B separating the two arcs of q(A) n B (equivalently: the closure T(infinity) = q(A) = unknot joins the two
D_+ ends to each other and the two D_- ends to each other).  The disc lifts to two meridian discs of N(K), so pi^{-1}(suture) = two parallel meridians, oppositely oriented as
boundary of R_+.  By GW Def 2.11 and Example 2.6:  Sigma(D x I, T) = (S^3 - N(K), Gamma_mu),  SFH = HFK^(K; F_2).
The through-resolution (two arcs from D_- to D_+) closes up under T(infinity) to ONE circle, so it is b = Q_0, and the backtracking resolution is c = Q_infinity.  Hence
GW's V = H(F_b C) = N, and Prop 5.20 gives

    THEOREM S [PROVED given GW Prop 5.20].  For every strongly invertible (K,h) with quotient tangle T there is a spectral sequence with E^2 = N(mirror T) and
    E^infinity = HFK^(K; F_2).  Hence 1 + 2m(T) = dim N(T) >= rank HFK^(K) >= 2g(K) + 1.

In the curve picture: * and p1 lie in D_+ (say), p2 and p3 in D_-; the suture is the curve separating {*,p1} from {p2,p3}, of slope infinity, and A_b (the loop at * around
p1) is that curve cut open at *.  Its lift to the boundary torus is the pair of meridional sutures.

### 1.3 Roberts and the annular version (text of the arXiv PDFs read now; extracted copies in floer/lit/)
- [CITED, read now] Roberts, arXiv:0706.0741v2, Proposition 1.1: L a link in A x I meeting the spanning disc of the axis B in an ODD number of points, L' = L plus two split
  core circles; spectral sequence with E^2 = reduced Khovanov skein homology of the mirror of L' in A x I (F_2) converging to sum_i HFK^(Sigma(L) #^2 S^1xS^2, B~ # B(0,0), i; F_2).
  Theorem 1.3 (= 9.1): for L non-split ALTERNATING in A x I (odd wrapping) the sequence collapses, each skein-grading k is the Alexander grading k, and tau(B~) = 0.
- [CITED, read now] Grigsby-Wehrli, arXiv:0907.4375v2 (AGT 10 (2010); v2 corrects Thm 3.1 of v1):
  Theorem 2.1: for ANY link L in A x I (no parity restriction) a spectral sequence Kh^*(mirror L) => SFH(Sigma(A x I, L)), F_2.
  Theorem 1.1 there = "[GW1, Prop. 5.20]" (confirms the number of the tangle statement).
  Lemma 2.21/Def 2.22: the annular (k = f) grading is a filtration on the Khovanov complex; Kh^* is the homology of the associated graded.
  Proposition 2.24: SFH(Sigma(A x I, L)) = HFK^(Sigma(S^3,L), B~) (x Theta if lk(L,B) is odd); proof of Prop 2.29: A(Psi(x)) = (f(x) - p(L))/2, i.e. the annular grading IS
  the Alexander grading of the lifted axis, and the edge maps correspond grading by grading.
  Theorem 3.1: cutting A x I along a meridional disc lambda x I gives a balanced tangle T in D x I, and the spectral sequence Kh^*(T) => SFH(Sigma(D x I,T)) is a DIRECT
  SUMMAND of the one for L (proof: [GW naturality, IMRN 2010, Thm 4.5], a filtered version of Juhasz's surface decomposition theorem).
  => (b) of BRIEF2 is literally in the literature: N(T) = Kh^*(T(n)) in top annular degree, and Theorem S is the top-degree summand of Roberts' sequence for T(n).
- [CITED, read now] Grigsby-Wehrli, arXiv:1010.3727v1 ("On gradings in Khovanov homology and sutured Floer homology"), Theorem 5.1: for the standard multi-diagram of
  Construction 3.1, every generator x of the filtered cube complex satisfies k(x) = -2 A_S(x), S = lift of the meridional disc; and "[GW naturality, Lem. 3.12] implies that
  the filtered chain complex splits according to these gradings".  This is the ONLY grading comparison that is a theorem on the Heegaard Floer side.
- [PROVED, elementary] Why the Alexander grading of HFK^(K) is NOT of this type.  A grading A_S on the cube complex needs a surface S in S^3 - N(K) disjoint from the surgery
  link, i.e. the preimage of a surface in D x I transverse to T.  Such S is h-invariant.  But h reverses the meridian, so h_* = -1 on H_2(M, dM) = Z, and an h-invariant
  surface whose orientation is preserved by h (it is a branched double cover of an oriented surface) has class 0.  So no A_S sees the Alexander grading; the strong inversion
  exchanges HFK^(K,A) and HFK^(K,-A) (Dai-Mallick-Stoffregen: tau_K is skew-graded), while the E^2 page N has no such symmetry.  Consequence: the filtration that the cube
  induces on HFK^(K) cannot be expected to be compatible with the Alexander decomposition.  (Confirmed by the grading counts in section 2.3.)

## 2. What can carry the quantum grading on the Floer side (task 2)

### 2.1 Status of the bidegree (k, 2k-2) of higher differentials
- [CITED, read now] Szabo, arXiv:1010.4252v2, Section 7 (after Fig. 20, from the grading rule Lemma 2.12): in his COMBINATORIAL geometric spectral sequence "the map d_k shifts
  the (q,h) gradings by (2k-2, k), and decreases the delta grading by 2" (his delta = q - 2h).  Theorem 1.1: invariance.  That it equals the Ozsvath-Szabo sequence is a
  conjecture (Introduction; Question 8.1 for the reduced theory).
- [CITED, read now via ar5iv] Baldwin, arXiv:0809.3293, CONJECTURE 1.1: each page E^k(L), k >= 2, of the Ozsvath-Szabo sequence has a well defined quantum grading (resp. delta
  grading) and D^k raises q by 2k-2 (resp. lowers delta by 1).  Stated as a conjecture; true for k = 0,1 by definition; verified for almost alternating links (attributed to
  J. Greene).  Section 6 there: not clear that a quantum grading exists on E^k, k > 2.
- [CITED, read now] Lobb-Zentner, arXiv:1310.7909v1: still a conjecture in 2013; they prove that for all pretzel knots the higher differentials of both the Ozsvath-Szabo and the
  Kronheimer-Mrowka sequences strictly lower the delta grading (abstract, Section 2.1).
- [PROVED remark] GW's sentence in 0807.1432 Section 7 ("it is easy to see that D_k raises j by 2(k-1)") contains Baldwin's Conjecture 1.1 as the special case n = 1 (T = a knot
  minus a point).  The standard argument gives it only when every Spin^c structure on the 2-handle cobordisms W_{I,J} that contributes has c_1^2 = 0 = sigma(W); the cobordisms
  between resolutions can have indefinite intersection form (e.g. a ladybug face: branched double cover of a twice punctured torus, form H), so this needs proof.
  => For the Heegaard Floer sequence of THEOREM S the bidegree (k,2k-2) is CONJECTURED, not proved.
- [CITED, read now] Kronheimer-Mrowka, arXiv:1110.1290v2 (instantons): Theorem 1.1: a differential d# on the Khovanov cube complex C(D†) with H(C,d#) = I#(K), d# and d_Kh of
  order >= (1,0) and d# - d_Kh of order >= (1,2) for the (h,q) bifiltration.  Theorem 1.2/Cor 1.3/1.4: the filtered homotopy type, all pages, and the induced h- and q-filtrations
  on I#(K) are invariants of K.  Prop 1.5: a cobordism S induces a map of order >= (S.S/2, chi(S) + 3 S.S/2).  The same for the reduced I-natural (Remark).  Section 11: the
  mod 4 grading is j - i - 1, all differentials have degree -1 mod 4 and satisfy Delta j - Delta i >= -1; for T(4,5) the one non-zero differential goes from row j-i = 13 to
  row 16, so it has j-i shift 3 (bidegree (5,8) if it is of Szabo type: it is not known on which page).  So in instanton theory q survives as a FILTRATION (a theorem), not
  as a grading, and only q - h mod 4 is a grading.
- [CITED, read now] Xie, arXiv:1809.01568v2: Theorem 1.1: AKh(mirror L; C) => AHI(L; C); Theorem 5.16: the sequence preserves the annular grading; Corollary 1.2: for a balanced
  admissible tangle T in I x D, TKh(mirror T; C) => THI(T) (Street's tangle instanton homology = the top annular summand); THI(T) = C iff T is a braid (Street), giving
  Theorem 1.3 (TKh detects braids; Grigsby-Ni over Z/2); Theorem 1.4: Khr_n(mirror K; C) => I-natural(K; C) for every colour n.
  For us: N(T; C) => THI(T), with THI(T) = sutured instanton homology of the tangle exterior (no branched cover).  For the doubled tangle T_K this gives only
  dim N >= dim KHI(K), much weaker than GW's rank HFK^(K)^2; for a general quotient tangle it gives dim N(T;C) >= dim THI(T) >= 2 unless K is trivial, in characteristic 0.
  No q-filtration statement is proved in the annular instanton setting (not found in the paper).

### 2.2 Summary: gradings available on the Floer side of THEOREM S
    annular k            <->  Alexander grading of the lifted axis          PROVED (GW 0907.4375 Prop 2.29; GW 1010.3727 Thm 5.1; Xie Thm 5.16 for instantons)
    delta = q/2 - h      <->  a Maslov-type Z-grading                       CONJECTURED (Baldwin Conj 1.1; GW Conj 7.1 -- the latter is FALSE as stated, see 2.3)
    q (or h) alone       <->  only a filtration, and only proved for instantons in S^3 (KM Thm 1.1); nothing in the sutured/annular setting
    Alexander grading of K  <->  nothing on the Khovanov side (section 1.3, last item)
So the Floer side sees ranks, the mod 2 grading, conjecturally the rows b = -delta of the lattice picture, and never the column coordinate a.

### 2.3 Grigsby-Wehrli's grading Conjecture 7.1 is false as stated (DATA + CITED => refutation)
Conjecture 7.1 of 0807.1432 asks for a lift M of the relative Maslov gradings (one free constant per relative Spin^c structure = per Alexander grading) with
dim E^infinity_{delta=d} = dim SFH_{M=d} for all d.
- [CITED, recalled: Ozsvath-Szabo, "Heegaard Floer homology and alternating knots", Thm 1.3] HFK^(4_1) = F_(A=1,M=1) + F^3_(A=0,M=0) + F_(A=-1,M=-1).  So for every lift M some
  M-level has rank >= 3 (the three generators in Alexander grading 0 have the same Maslov grading).
- [DATA, chain file k138/examples/si/4_1-1/cxBNr-c2-qs read now] N(T) for the first inversion of 4_1 has five generators at (h,q) = (0,12),(5,20),(4,18),(9,26),(8,24), i.e.
  delta = 6,5,5,4,4: delta-levels of rank (2,2,1) (mirror: (1,2,2)).  dim N = 5 = rank HFK^(4_1), so E^2 = E^infinity.  No level has rank 3.  Contradiction.
- The same in GW's own setting (2-cable, n = 2): N(T_K) for K = 4_1 has 25 generators in delta-levels (2,6,9,6,2) (dbl/doubles.jsonl, record k5_2), E^2 = E^infinity because
  rank HFK^(4_1 # 4_1) = 25, but HFK^(4_1 # 4_1) has rank 11 in the single bigrading (A,M) = (0,0).  9 < 11.
So: the delta-grading that the cube induces on HFK^(K) is NOT compatible with the Alexander decomposition (as predicted in 1.3).  The conjecture has to be weakened to a
statement about the mod 2 grading plus one more number, see section 3.3.  (Caveat: this uses kht++'s delta-gradings and THEOREM S; no independent recomputation of Kh~_2(4_1).)

### 1.4 The other sutures, the bypass triangle, and "delta x + y = u"  (task 1, second half)
Notation: for a slope s on the pillowcase let c_s be the curve of slope s (separating the four ends two by two), D_s x I the corresponding product structure on the ball,
V_s(T) the Khovanov homology of T in D_s x I in the sense of GW (non-backtracking resolutions, both arcs reduced), and Gamma_s the lift of c_s to the boundary torus.
Conventions of the brief: Sigma(T(p/q)) = S^3_{p/q}(K), so Gamma_{p/q} = two parallel copies of p mu + q lambda.
(a) [PROVED given GW Prop 5.20] For EVERY slope s there is a spectral sequence V_s(mirror T) => SFH(S^3 - N(K), Gamma_s) (the tangle is balanced for every c_s).
    SFH(M, Gamma_{p/q}) = HFK^(S^3_{p/q}(K), core of the filling) (Juhasz, sutured manifold of a knot complement; the meridian of the core is p mu + q lambda).
    s = infinity: V = N = H(F_b C), target HFK^(K).   s = 0: V_0 = N_c := H(F_c C) (the c-generators), target HFK^(S^3_0(K), mu_K) (Eftekhary's longitude Floer homology).
    s = +-1: target HFK^(S^3_{+-1}(K), core).  In curves: V_s(T) = HF(BN~(T), A_s), A_s = loop at * around the far end of the arc of slope s from * (naturality of BN~ under twists).
(b) [CITED, recalled: Friedl-Juhasz-Rasmussen, decategorification of SFH] chi(SFH(M, Gamma_{p/q})) = +-T^? Delta_K(T)(1 - T^p)/(1 - T) in Z[H_1(M)] = Z[T^+-1].  So for s = 0 the
    Euler characteristic vanishes in every relative Spin^c structure ("longitudinal sutures"), while chi_q(N_c) = x is not zero: the c-side cannot collapse.
    Example [DATA + CITED recalled]: trefoil.  N_c has 8 generators (count the symbols ⬯ in the chain file of 3_1) and chi_q = x has 6 terms; rank SFH(M,Gamma_lambda) <= rank
    HFK^(K) + rank SFH(M,Gamma_1) = 3 + 1 = 4 by the bypass exact triangle (Honda; Etnyre-Vela-Vick-Zarev) and the fact that the core of +1 surgery on the right-handed trefoil
    is Floer simple.  So 8 -> at most 4 on the c-side, against 3 -> 3 on the b-side.  In general dim N_c = 4m + |k| = dim Kh~(T(0)) (count of c's: 4 per P-arrow, |k| in the tail).
(c) [PROVED] Khovanov analogue of the bypass exact triangle.  Let chi be one crossing added at the side of T (a half twist exchanging one D_+ end with one D_- end).  Then
    V_infinity(T chi) = V_{+-1}(T), and resolving chi gives V_infinity(T chi) = H(F_X (x) C(T)), where F_X is the 2-dimensional B-module {1_b -S-> 1_c} (S_b an isomorphism, all else 0;
    for the other crossing S_c).  Proof: the resolutions of T chi are b.id = b (F), c.id = c (backtracks, 0), b.E = b + circle (V = <1,x>), c.E = b (F); the edge b.id -> b.E is the
    split 1 -> x, which cancels x, and the remaining saddle b.E -> c.E is the merge 1_b -> 1_c.  The short exact sequence 0 -> F_c -> F_X -> F_b -> 0 gives
            ... -> N_c(T) -> V_{+1}(T) -> N(T) -S-> N_c(T)[1] -> ...
    with connecting map the action of S in Ext^1_B(F_b,F_c).  In the Fukaya picture: A_{+-1} is the boundary connected sum of A_b and A_c along one of the two boundary segments
    at *.  This is the exact analogue of the bypass triangle for (Gamma_mu, Gamma_lambda, Gamma_{lambda+-mu}).  Its Euler characteristic is the Kauffman skein relation
    (bracket of T chi), not "delta x + y = u".
    Remark [PROVED]: there are two different triangles for V_{+-1}(T).  (i) The skein triangle of the crossing chi itself: N(T) -> V_infinity(T E) -> V_{+-1}(T), whose middle
    term is H(M_E (x) C(T)) = Kh~(T(0)) (M_E = the 3-dimensional module 1_b -> 1_c -> x_b); its Floer counterpart is the SURGERY triangle
    HFK^(K), HF^(S^3_0(K)), HFK^(S^3_{+-1}(K), core)  (Sigma(D_infinity x I, T E) = S^3_0(K) minus a ball: decompose along the product disc that cuts off the trivial strand).
    (ii) The triangle above with middle term N_c, whose Floer counterpart is the BYPASS triangle HFK^(K), HFK^(S^3_0(K), mu), HFK^(S^3_{+-1}(K), core).
    The two middle terms have the same dimension 4m + |k| but different Euler characteristics (x + (q+1/q)-multiple of y versus x).
(d) [PROVED] "delta x + y = u" is categorified by the closure, not by the triangle: Kh~(T(infinity)) = H(M_inf (x) C(T)) = F, where M_inf is the 3-dimensional B-module
    1_c -S_c-> 1_b -S_b-> x_c (D_c: 1_c -> x_c), uniserial with composition factors F_c{+1}, F_b, F_c{-1}.  So F is the homology of a 3-step filtered complex with graded pieces
    N_c{1}, N, N_c{-1}; in particular dim N <= 2 dim N_c + 1.  Floer counterpart: delta = q + 1/q becomes 0 (gl(1|1)), the two copies of N_c cancel (chi(SFH(Gamma_lambda)) = 0)
    and the relation degenerates to chi(HFK^(K)) = 1, categorified by HFK^(K) => HF^(S^3).

## 3. Consequences (task 3)

### 3.1 The collapse, checked directly against knot Floer homology (DATA, new today)
Tool: floer/scripts/hfk_word.py turns a half-diagram word into a PD code and calls Szabo's knot Floer program (python package knot_floer_homology 1.2.2 through spherogram; read-only
use of the copy already installed in the Codex workspace).  Sanity: trefoil word gives rank 3, genus 1; table knots give the known ranks.
floer/scripts/collapse_check.py compares dim N = 1 + 2m with rank HFK^(K), K computed FROM THE WORD (so the mislabelled two-bridge files do not matter):
    384 tangles with a word (k138, two-bridge run_3_45, sums comp4/comp5, random, alex1):  dim N = rank HFK^(K) in 383,  dim N > rank HFK^(K) in 1  (9_46 second inversion, 15 > 9),
    dim N < rank HFK^(K) never (as THEOREM S demands).  Output: floer/scripts/collapse_check.tsv.
In this set the one exception is exactly the one tangle whose arc has a D^2 arrow.  [DATA]  (More exceptions, of two kinds, were found by targeted runs: 3.6.)

### 3.2 A theorem that follows: a lower bound for Watson's invariant, and why Watson's rank conjecture is "almost" true
kappa(K,h) = HF(a(0), specials) is Watson's invariant (Kotelskiy-Watson-Zibrowius arXiv:2104.13592, Def 3.4, read now); dim kappa = 4m when all specials are s_4(infinity).
    THEOREM F1 [PROVED given GW Prop 5.20 and BRIEF2 section 1; specials of type s_4].  For every strong inversion h on K:
          dim kappa(K,h) = 2(dim N(T) - 1) >= 2(rank HFK^(K; F_2) - 1) >= 4 g(K).
    (Watson and KWZ only had kappa != 0 for K non-trivial, through L-space surgeries.)
[CITED, read now] Watson, "Khovanov homology and the symmetry group of a knot" (TeX source in lit/kwz-inversions/src/watson), conjecture labelled con:rank (= [Wat17, Conjecture 29] in
KWZ): dim kappa(K,h_1) = dim kappa(K,h_2) for two strong inversions on the same knot.  KWZ Counterexample 3.5: for 9_46, 16 < 28.  KWZ Remark 3.2: among the 57 knots up to nine
crossings with two inversions this is the only failure.
    EXPLANATION [PROVED + DATA]: when the sequence of THEOREM S collapses, dim kappa(K,h) = 2(rank HFK^(K) - 1) does not depend on h.  Watson's conjecture holds exactly as far as
    the Grigsby-Wehrli sequence collapses, and 9_46 (second inversion: 28 = 2(15-1) > 2(9-1) = 16) is the one non-collapsing tangle in the data.

### 3.3 What the Floer side determines in N: two numbers (PROVED parts and one new empirical identity)
(i) [PROVED modulo standard facts] The Floer Z/2-grading of the cube complex is delta mod 2 (inside a vertex delta = Maslov + const mod 2; an edge map preserves q and raises h by
    one; every polygon map has a well defined parity because c_1^2 = sigma mod 8 for characteristic classes).  It is NOT the homological parity (-1)^h that J uses:
    (-1)^h = (-1)^(a+b), (-1)^delta = (-1)^b.  Check: sum over N of (-1)^b = 1 = sum (-1)^M rank HFK^_M  (= J(-1) = 1, known).
(ii) [PROVED: KWZ determinant constraint, digest lit/kwz-thin section on determinants; DATA 374/374]  k = 4 sum over specials of (-1)^(d_i - delta(rho)) = 4 sum over N of
    (-1)^(delta - delta_rho) (delta - delta_rho).  In lattice coordinates k/4 = sum_N (-1)^b (-b): the slope of the rational component is the first delta-moment of N, equivalently
    the signed count of P-arrows (d_P lowers delta by one and H(N,d_P) = F rho).
(iii) [DATA, 373 of 374 distinct tangles; the exception is again 9_46 second inversion; floer/scripts/kslope_check.py]
            k(T) = -4 M_1(K),      M_1(K) := sum over a basis of HFK^(K) of (-1)^M M  =  signed count of the vertical arrows of a reduced CFK(K) by the Maslov parity of the source.
    For thin knots M_1 = -+tau and k = 4 tau = -2 sigma (kht++ sign conventions); for L-space knots |M_1| = (number of terms of Delta - 1)/2, NOT tau: 8_19 = T(3,4) has k = 8,
    tau = 3, M_1 = -2.  Further discriminating knots run today (words from a random search, HFK^ computed first; floer/scripts/cand_runs.jsonl): see 3.6.
    Meaning: under the collapse, (N, d_P) and (HFK^(K), vertical differential) are isomorphic as Z/2-graded complexes: same total rank, same numbers (e,o) of arrows with even /
    odd source.  So the Floer side knows how many specials sit on even and on odd delta-levels relative to rho:  e - o = -M_1(K), e + o = (rank HFK^(K) - 1)/2.
    This answers conjecturally KWZ's Questions 3.3 (meaning of the slope; divisibility by 4).  CONJECTURE F2: k = -4 M_1(K) (at least whenever the GW sequence collapses;
    by 3.6 it also holds in 4 of the 5 known non-collapsing tangles; the one known failure is 9_46 second inversion).
    Expected reason: d_P is "allow paths through the special puncture" = fill one of the two sutures; on the Floer side this is the differential of HFK^(K) => HF^(S^3).
    A refinement of THEOREM S compatible with these two differentials would give (iii) for free.  NOT proved.
(iv) Nothing else is Floer-visible: the delta-levels themselves are not ((2,2,1) against (1,3,1) for 4_1; two specials on one level for 5_1 against Maslov gradings -1,-3
    of the two vertical arrows of T(2,5)); they depend on the inversion (5_2: levels (1,1,1) for the first inversion, (1,2) for the second) while (e,o) do not.
    The parameter j = lk(T(0))/4 and all column coordinates a are invisible.

### 3.4 What END / NP would say on the Floer side: nothing, and the Floer analogue is false
- [PROVED] If the higher differentials have bidegree (k,2k-2), k >= 2 (conjectural for HF), they are the lattice vectors (k-5, 1) = P-3D, P-2D, P-D, P, P+D,...; they never have
  the J-cancelling offset (-4,1) = (h,q) = (1,0).  So a J-cancelling pair is never removed by the spectral sequence: the Floer side cannot "explain away" a cancellation, and
  conversely it does not forbid one.  E^infinity = N minus pairs at offsets (k-5,1); chi_q is not preserved (each removed pair changes it by +-t^(q/2)(1 - (-t)^(k-1))).
- [PROVED, formal] B0 = a(0) + S + hS passes every Floer-side test listed in 3.3: dim N = 9, sum (-1)^delta = 1, k = 0 = first moment (the two P-arrows of S and of hS have
  opposite delta-parity), (e,o) = (2,2).  These are the numbers of an honest knot, e.g. 6_1 or 9_46 (rank 9, tau = 0, M_1 = 0, two boxes: (e,o) = (2,2)).  Hence no statement that
  uses only [ranks, delta-rows mod 2, first moment, bidegrees (k,2k-2)] can exclude B0.
- [CITED + DATA] The Floer analogue of END is false: knots with Delta = 1 have chi = 0 in the top Alexander grading.  For the knot of BRIEF2 section 5 (computed in section 5 below)
  HFK^ in Alexander grading +-2 is F_(M) + F_(M-1), Euler characteristic 0, while N has a single generator in each extreme q-degree.  So the Floer side contains exactly the
  cancellations that NP forbids on the Khovanov side, in the same vector space (dim N = rank HFK^ = 31).
- [DATA, floer/scripts/extremes.py; OLD data only -- section 7 has a violation found later] In 278 distinct tangles the extreme quantum degrees of N are one-dimensional in 554 of 556 cases (2-dimensional on one delta-level for
  9_37 second inversion (top) and 9_40 second inversion (bottom)).  So END holds in the data in the strong form "N in its top/bottom q-degree is F or F^2 in ONE homological degree".
  Equivalent form of NP: N^{*,q_max} and N^{*,q_min} are each supported in a single homological degree (delta = q/2 - h).

### 3.5 A proved theorem for a class (the "one parity" class; conjecturally the L-space knots)
Normalisation used here (checked on the trefoil against the notes: J(3_1) = t^7 + t^4 - t^3 up to mirror):  with rho at the lattice origin and L(t) := sum over N of
(-t)^a (-t^4)^b,  the invariant is  J = t^k L,  so  T is flat  iff  L = t^(-k).   [The formula "J = sum over N" of BRIEF2 section 4 is off by the unit t^k; it does not matter for
END/NP, but it matters here.  Check: J = 1 mod (1+t)^2 forces L'(-1) = k, and indeed L'(-1) = k is identity 3.3(ii).]
Every generator other than rho lies in exactly one P-pair {(alpha_i, beta_i), (alpha_i, beta_i + 1)} (one pair per special; [PROVED] from the J-set formula), hence
        L = 1 + (1 - t^4) S,     S := sum_i (-1)^(beta_i) (-t)^(e_i),     e_i := alpha_i + 4 beta_i,
and flat  iff  S = (t^(-k) - 1)/(1 - t^4) = "virtual string": |k|/4 monomials of ONE sign with exponents in 4Z (k < 0: -(1 + t^4 + ... + t^(|k|-4)); k > 0: t^-4 + ... + t^-|k|).
Two specials cancel in S only if they have the same e and levels beta of OPPOSITE parity.  Every b-generator except one (the one next to the end of the arc at p1) lies in exactly
one D-pair, and an arrow D^a' changes e = q/2 by a' ([PROVED]: a curve segment inside the lens region joins two points of A_b or runs to p1; the arc has exactly one end at p1).

    THEOREM F3 [PROVED].  Let T be the quotient tangle of (K,h), m >= 1 its number of specials (type s_4).  Suppose
      (1) all specials lie on delta-levels of the same parity  (equivalently |k| = 4m; equivalently Kh~(T(n)) has rank n = det for all n >= k, or for all n <= k), and
      (2) some D-arrow of BN~(T) has exponent not divisible by 4 (e.g. a unit arrow; true in every computed example).
    Then T is not flat.  More precisely S has no cancellation at all, and J - t^k = t^k (1 - t^4) S with S = +- sum_e n_e (-t)^e, n_e >= 0.
    Proof.  By (1) S = (-1)^beta sum_e n_e (-t)^e without cancellation.  If T were flat, S would be the virtual string, so every e_i would lie in 4Z.  Then every generator of N
    has q/2 in 4Z relative to rho (lower generator e_i, upper generator e_i + 4, rho 0).  There are m >= 1 D-pairs, each joining two generators whose q/2 differ by the exponent
    a' of the arrow; so every a' is divisible by 4, contradicting (2).  QED
    Scope.  [CITED, read now: Watson, Theorem labelled thm:torus] kappa of every torus knot is supported in one delta-grading, so (1) holds for all torus knots.  [CITED, read now:
    Watson, discussion of conjecture con:L-space] the same for knots with a lens space surgery and for the (-2,3,q) pretzel knots, and for sufficiently positive cables.
    [DATA + Conjecture F2] (1) <=> |M_1(K)| = (rank HFK^(K) - 1)/2 <=> all vertical arrows of CFK(K) have sources of one Maslov parity; this holds for L-space knots and their
    mirrors (staircases), and fails as soon as there is a box.  So the class of F3 is, conjecturally, exactly Watson's conjectural class "strongly invertible L-space knots".
    Remark on (2).  It is a hypothesis.  Heuristically the Lewark-Marino-Zibrowius order-one statement for the knots T(1/2n) (proper rational replacements of the unknot)
    controls, in the limit n -> infinity, the D-arrows at p3 (c-side; and indeed every c-c arrow in every saved chain file is a unit D), not the D-arrows at p1, whose
    exponents are the H-torsion orders of N^BN(T) := H(F_b[H] (x) C(T)) (b -> F[H], D -> H, S -> 0) = F[H] x_D + sum over D-arrows of F[H]/(H^a').  The one non-unit arrow in
    the data is the D^2 of 9_46 second inversion, so (2) holds in all 384 computed cases.  NOT proved in general.
    What F3 does not give: as soon as specials of both level-parities occur (any box on the Floer side), cancellations in S are possible and F3 says nothing.  Then flatness is
    S = virtual string after cancellation, and one needs the outline law (NP).

### 3.6 Extra runs made today for 3.1 and 3.3(iii) (cheap check; words chosen because HFK^ separates tau, M_1 and the thin case; kht++ under a 150 s limit)
Selection: random half-diagram words (generator of tools/alex_search.py), HFK^ computed first; kept (a) knots with |M_1| != |tau| ("discriminating": L-space knots with long
steps and thick knots), (b) thick knots with |M_1| = |tau|, (c) variants of the 9_46 second-inversion word, (d) a further batch of thick knots (floer/scripts/end_search.py).
kht++ quotient mode under a time limit of 60-150 s (19 words timed out and are not counted).  Records: floer/scripts/cand_runs.jsonl, variants.jsonl, end_search.jsonl.
    33 new tangles with a result:   collapse 28, no collapse 5;    k = -4 M_1 holds in 32 (the failure is 9_46 second inversion again);    END holds in 32, fails in 1.
(a) eight discriminating knots, all collapse and all have k = -4 M_1, never 4 tau:  rank 5 (tau = 3, k = 8; 8_19 again), rank 7 (tau = 4, k = 12; twice, T(3,5)-like),
    rank 9 (tau = 5, k = 16; L-space knot of genus 5), rank 11 (tau = 4, M_1 = -3, k = 12; not an L-space knot), rank 13 (tau = 5, M_1 = -4, k = 16).
(b)-(d) the five tangles with dim N > rank HFK^:
      word                                              dim N  rank  tau  g   k   -4M_1   arrows        END
      s.l1.y0.y2.r1.y2.y2.y2.u3.x0.u1 (9_46, 2nd inv.)    15     9    0   1   -4    0     one D^2       ok
      s.l1.y0.y0.y0.y2.r1.y2.y2.y2.u3.x0.u1               27    19   -1   2   -4   -4     one D^2       ok
      s.l1.y0.r2.x2.y0.y3.y3.x0.y1.u2.y0.y0.x2.y0.u1      21    13   -2   2   -8   -8     one D^2       ok
      s.r1.x2.y1.y0.r2.y0.y1.y0.y1.x2.u3.u1               33    17    0   2    0    0     unit only     FAILS (section 7)
      s.r1.y2.x1.x0.r3.x0.y2.x0.x1.y2.y1.u1.x0.u1         45    29    2   2    8    8     unit only     ok
    Two kinds of non-collapse.  "Hinge" kind: the arc is a staircase with one D^2 arrow and the staircase is too long (7, 11, 9 generators against 2|tau|+1 = 1, 3, 5 on the Floer
    side; the squares match the boxes: 2, 4, 3); the drop is 6, 8, 4 = 2 min(#generators beyond the D^2, #generators before it) in the first two.
    "Square" kind: all arrows unit, N = arc + squares, and four squares' worth (16 generators) dies in both examples (33 -> 17, 45 -> 29).
    Every tangle with a non-unit D-arrow fails to collapse (3 of 3); unit arrows do not imply collapse (2 counterexamples).
So: the collapse is the rule for knots with thin knot Floer homology and for all L-space-like examples tried, and it fails for some thick knots.  The moment identity
k = -4 M_1(K) is more robust than the collapse: it holds in 4 of the 5 non-collapsing tangles.  Totals over old and new data: 406 distinct tangles, k = -4 M_1 in 405.

## 4. Results on strongly invertible knots that constrain the quotient (task 4)
None of them gives an inequality or a grading statement involving N(T), the specials or J, except THEOREM S itself.  What exists:
- [CITED, read now] Lipshitz-Sarkar, arXiv:2203.13895v1.  Theorem 1.1: for a strongly invertible K with an intravergent diagram and annular quotient knots K-bar^0, K-bar^1
  (quotients of the 0- and 1-resolution of the crossing on the axis) there is a spectral sequence with E^1 = Kh(K; F_2) (x) F_2[theta, 1/theta], d_1 = theta(1 + tau_*), converging
  to AKh(K-bar^1, K-bar^0; F_2) (x) F_2[theta,1/theta] (cone of the axis-moving map f^+), preserving the quantum grading (formula (1.1)).  Corollary 1.2: rank inequality in each
  quantum grading.  Theorem 1.5: rank HF^(Sigma(K)) >= rank HF^(Sigma(K-bar)) for a quotient knot K-bar = q(K u A_1).  Theorem 6.2 (from Large): the same for the knot Floer
  homology of the preimage of the other half axis.  The quotient objects are the CONSTITUENT KNOTS of the quotient theta-curve (the two components of T(0)), viewed in the
  complement of the axis; the Khovanov side is Kh of K itself, not of T.  So this is a second, independent "quotient" relation: Kh(K) => annular Kh of constituents.
  It does not bound dim N from above: rank Kh~(9_46) = 9 < 15 = dim N for the second inversion.
- [CITED, read now] Dai-Mallick-Stoffregen, arXiv:2201.01875v3.  Theorem 1.7: a strong inversion induces a skew-graded, F[U,V]-skew-equivariant homotopy involution tau_K of
  CFK(K), with tau_K iota_K = sigma iota_K tau_K.  Theorems 1.1/1.2: equivariant concordance invariants V_0^tau etc., bounds on the equivariant slice genus.  No statement about
  the quotient tangle.  For us: tau_K exchanges Alexander gradings A and -A, which is why the Alexander grading cannot be seen on the E^2 page (1.3, 2.3).
- [CITED, read now] Hendricks-Lidman-Lipshitz, arXiv:2007.03023v2.  Theorem 1.1: rank HF^(Sigma(Y,L)) >= rank HF^(Y) for nullhomologous L.  Proposition 1.11: the sutured
  version, for a link L in the INTERIOR of a balanced sutured manifold: dim SFH(Sigma(M,L)) >= dim SFH(M).  Our branch set T is a tangle meeting R_+-, so 1.11 does not apply as
  stated; the expected analogue (base D x I, SFH = F) would only say: the Tate homology of (HFK^(K), tau_h) has rank one.
- [CITED, abstract only] Boyle-Issa, arXiv:2101.05413: equivariant 4-genus bounds from invariants of the strongly invertible concordance group, Donaldson's theorem and the
  g-signature.  KWZ (read now, p. 3): 9_46 is slice with non-zero equivariant 4-genus [BI21, Fig. 14].  No statement about N or J.
- [CITED, read now] Watson (TeX source local): kappa(K,h) = 0 iff K trivial (via L-space surgeries); thm:torus (torus knots: kappa delta-thin, dim <= |pq| - 1);
  conjectures con:structure (kappa = sum of V's; now KWZ's Conjecture 3.6), con:rank (false: 9_46, KWZ Counterexample 3.5), con:L-space (L-space knot iff kappa delta-thin).
  Watson explicitly aligns his sutured tangle invariant with Grigsby-Wehrli ("perhaps best aligned with the work of Grigsby and Wehrli") but states no inequality with HFK^.
- NEW here: THEOREM F1 (dim kappa >= 2(rank HFK^(K) - 1)), the explanation of con:rank, Conjecture F2 (k = -4 M_1(K)), and the heuristic derivation of con:L-space from
  collapse + F2 (section 3.5, Scope).

## 5. The Alexander-polynomial-one knot of BRIEF2 section 5 (task 5)
- [DATA] Word s.r1.y0.x2.r3.y0.y2.u1.x2.x2.y0.y1.x0.u1: symmetric diagram with 14 crossings, writhe -4, bracket <D>/delta = A^-16 - A^-12 + 2A^-8 - 2A^-4 + 1 - A^8 + 2A^12
  - 2A^16 + 2A^20 - A^24 (tools/kauffman.py), i.e. Jones coefficients (-1, 2, -2, 2, -1, 0, 1, -2, 2, -1, 1) in consecutive powers of t (V(1) = 1, V'(1) = V''(1) = 0 checked).
- [CITED, read now from KnotInfo single-knot pages] Jones polynomials of the knots with Delta = 1 up to 12 crossings: 11n34 = 11n42: (1,-2,2,-2,1,0,0,2,-2,2,-1);
  12n313: (-1,2,-2,2,-1,1,1,-2,2,-2,1); 12n430: (-1,2,-2,2,-1,0,1,-1,2,-2,1).  Ours is none of these (it differs from 12n430 only in the last four coefficients).  All four of
  those knots have rank HFK^ = 33 (KnotInfo HFK polynomials for 11n42, 12n313, 12n430: 2 + 8 + 13 + 8 + 2).  So the knot has crossing number 13 or 14; not named.
- [DATA, knot Floer program] HFK^ of the knot, as (Alexander, Maslov): rank:  (2,2):1 (2,1):1 | (1,1):4 (1,0):4 | (0,0):6 (0,-1):5 | (-1,-1):4 (-1,-2):4 | (-2,-2):1 (-2,-3):1.
  Total rank 31, genus 2, tau = 1, epsilon = 1, not fibered, Delta = 1 (Euler characteristic 0,0,1,0,0).  So the knot is topologically slice and not smoothly slice.
  TEST PASSED WITH EQUALITY: dim N = 31 = rank HFK^(K).  The cancellation that is absent in N is present here: Alexander grading 2 is F + F in adjacent Maslov gradings.
  Shape: N = 3-staircase + 7 squares, and tau = 1 with rank 31 = 3 + 28 is the count for a 3-staircase plus 7 boxes.  k = 4 = -4 M_1 (M_1 = -1).
- [DATA] Second class (word s.l1.x0.y1.x0.y1.l1.y4.y4.x1.y0.y3.u2.y2.y0.u1, 16 crossings after simplification): HFK^ rank 65, genus 3, tau = 0, epsilon = 0, Delta = 1;
  dim N = 65 (alex1/runsB.jsonl).  Equality again; k = 0 = M_1.

## 6. Why the collapse and the moment identity should hold: the two deformation variables (heuristic, with the degree computations PROVED)
- [PROVED] Degrees.  A D-arrow D^a' has (h,q) = (1,2a'), so the deformation variable at p1 is H with (h,q) = (0,-2) and delta-degree -1; N^BN(T) = H(F_b[H] (x) C(T)) =
  F[H] x_D + sum over D-arrows F[H]/(H^a').  A P-arrow P_n has (h,q) = (2n+1,4n), so the deformation variable at the special puncture has (h,q) = (-2,-4) and delta-degree 0;
  the corresponding module is F[U] rho + sum over P-arrows F[U]/(U^n).  In lattice coordinates D^a' = (5a'-4, 1-a') and P_n = (2n-4, 1).
- [PROVED, elementary geometry of the cover] The pillowcase has cone angle pi at each end of T.  One full turn around * downstairs is HALF a turn around its lift upstairs.
  P_n passes n lifts of * = n full turns downstairs = n/2 turns upstairs; D^a' = a' turns downstairs = a'/2 upstairs.  So P_2 is exactly one turn around the lift z of *, D^2 exactly
  one turn around the lift w of p1, and a unit D-segment is not a loop upstairs at all: it is a transverse crossing of the meridian through z and w.
  The two meridional sutures are the two sides of the lens; R_+ is the thin annulus around w, and * sits on the suture.
- Reading: on the Floer side the basepoint variable that keeps the Maslov grading (V in the gr_U convention: arrows x -> V^n y have M(y) = M(x) - 1 for every n) behaves exactly
  like the *-variable (P_n lowers delta by 1 for every n, the variable has delta-degree 0).  The p1-variable H has delta-degree -1 = "half of U": it is the square root that a
  branched double cover produces, and it has no Floer counterpart of the same parity.  This is the asymmetry behind 3.3: (N, d_P) matches (HFK^, one basepoint differential) as a
  Z/2-graded complex, while d_D is EVEN for the Floer Z/2-grading and matches nothing.
- CONJECTURE F4 (refined THEOREM S).  The GW filtered complex carries a second filtration (bigons through the lift of *), and its E^2 page is (N, d_P)-compatible: there is a
  spectral sequence of Z/2-graded complexes from (N(mirror T), d_P) to (HFK^(K), d_v), d_v the differential of HFK^(K) => HF^(S^3) = "attach a 2-handle along the suture" =
  "cap T on the side of * and p1" (the capped tangle is the trivial arc, PROVED in 1.4(d)).  F4 + collapse => F2.
- HEURISTIC for the non-collapse of 9_46 type.  If there is also a minus version N^BN(T) => (an F[U]-module refinement of HFK^(K)) in which H^2 acts as the Floer variable,
  then an H^2-torsion class (a D^2 arrow) is an honest Floer arrow of length one around w, and generators near it can cancel on the Floer side.  9_46 is thin, its second
  inversion has one D^2 arrow, and there dim N drops (15 -> 9); the same in a 12-crossing relative (27 -> 19), see 3.6.
  REFUTED GUESS (kept for the record): "the sequence collapses whenever all D-arrows are unit" (true in the 384 old cases) is FALSE: 3.6 has a tangle with unit arrows only,
  N = point + 8 squares, dim N = 33 > 17 = rank HFK^.  What survives of the guess: non-unit D-arrow => no collapse (2 examples, no counterexample).
  REFUTED MODEL (kept for the record): "lift BN~(T) to the torus, fill in the three branch points other than z, pull tight; HFK^ = intersection number with the meridian through z".
  It predicts a drop of exactly 2 per D^2 arrow (the loop around w contracts, the two P_2 runs merge into a P_4 run); the observed drops are 6 and 8.
- [DATA, scan of 482 chain files] D-arrows at p3 (between c-generators): 10220, all unit.  D-arrows at p1 (between b-generators): 2685 unit, one D^2 (9_46 second inversion;
  the other two D^2 are a duplicate file and an invalid random word).

## 7. COUNTEREXAMPLE TO END / NP / TILT / the polygon law (DATA; found by the Floer-guided search for non-collapsing tangles)
Half-diagram word      s.r1.x2.y1.y0.r2.y0.y1.y0.y1.x2.u3.u1      (files: floer/work/examples/words/wef4c96470e*, floer/work/examples/check/ce1*).
- The knot: 13 crossings after simplification, one component.  HFK^ (knot Floer program): (A,M): (2,1):2, (1,0):4, (0,0):1, (0,-1):4, (-1,-2):4, (-2,-3):2; rank 17, genus 2,
  tau = 0, epsilon = 0, Delta = -2T^2 + 4T - 3 + 4/T - 2/T^2, det 15; point + 4 boxes; thick.  Bracket of the knot: 9 terms, coefficients (-1,1,-2,3,-2,2,-2,1,-1).
- kht++ -c2 -q -s (20 s): Kh~(T) = r(0) + 16 specials s4(infinity) at (q,delta) = (2,0),(4,0) | (-4,1),(-2,1),(0,1),(2,1),(2,1),(4,1) | (-6,2),(-4,2),(-4,2),(-2,2) | (-8,3),(-6,3) |
  (-14,4),(-12,4).   k = 0, j = 0.   BN~(T) = the trivial arc (one generator rho at (h,q) = (0,0)) + 8 squares with first corners
  (-1,-2), (-5,-8), (-3,-4), (-2,-2), (-7,-10), (-6,-8), (-9,-12), (-13,-18).  All arrows unit (D and P_2 only).  dim N = 33.
  Lattice picture (rows b = 1..-4, a from -1 to 8):  [1 1 . . . . . . . .] [1 3* 1 1 2 1 . . . .] [. 1 1 1 3 3 1 . . .] [. . . . 1 2 1 1 1 .] [. . . . . . . 1 2 1] [. . . . . . . . 1 1];
  squares at A=(-1,0), B=(0,-1), C=(2,-1), D=(3,-1), E=(3,-2), F=(4,-2), G=(6,-3), H=(7,-4).
- THE VIOLATION.  The maximal quantum degree of N is q = 8.  It contains exactly two generators: (h,q) = (5,8) (top corner of the square at (-1,-2)) and (h,q) = (4,8) (top corner
  of the square at (-2,-2)).  The second square is the first one shifted by (h,q) = (-1,0): this is the B0 offset, sitting on the outline.  Hence
        chi(N^{*, q_max}) = 0      (END fails at the top),      q_max is attained on two delta-levels (NP fails),
        the specials (4,0) and (4,1) have the same maximal offset on adjacent levels (TILT fails),  the Newton polygon has an edge of direction (4,-1) (polygon law fails).
  The bottom is fine (one generator at (h,q) = (-13,-18)).
- FIELD INDEPENDENT.  kht++ -c3 and -c0 (rationals) give a different multicurve (three compact components with P_1 arrows, three squares, an arc with 9 generators containing a
  P_3 and a P_1; Kh~ has components s2, s4, s6) but THE SAME bigraded N: 33 generators with the same multiset of (h,q), in particular (4,8) and (5,8) at the top.
  So the integral invariant is Z in both bidegrees; it is not a 2-torsion effect.
- LEMMA Q IS NOT CONTRADICTED.  J = L = -t^-9 + t^-8 - t^-6 + t^-5 + t^-1 + t^2 - t^3 = 1 - t^-9 (1-t)(1-t^4)(1+t^4)(1+t^3)  (checked: J(1) = J(-1) = 1, J'(-1) = 0).
  The two top generators cancel, and the top coefficient of J comes from the next degree.  In the old language: P has specials (4,0) and (4,1) with opposite signs at the top
  offset, and the next offset 2 has coefficient -1 + 2 = +1.
- STRUCTURE OF THE VIOLATION.  Pi(t) = sum over squares of (-1)^(a+b) t^(a+4b) = -t^-1 [A] - t^-4 [B] - t^-2 [C] + t^-1 [D] - t^-5 [E] + t^-4 [F] - t^-6 [G] - t^-9 [H].
  A cancels D and B cancels F.  The four squares form a parallelogram  {S, S+v, S+w, S+v+w},  v = (1,-1) (the bidegree (4,6) = P - D, a Szabo bidegree, k = 4),  w = (4,-1)
  (the J-cancelling offset, (h,q) = (1,0)).  Such a quadruple is J-neutral, and it is acyclic for a differential along v.
  Floer side: rank HFK^ = 17 = point + 4 boxes, so exactly four squares' worth of N dies in the GW sequence.  If the dying squares are A,B,D,F (d_4 : B -> A and F -> D), the
  survivors are rho, C, E, G, H: rows (3,4,4,4,2), the Maslov distribution of HFK^ is (2,5,4,4,2) (same up to the usual displacement of rho by one level), the surviving part
  satisfies END/NP/TILT, and chi_q of the surviving part is J.  NOT verified (E^infinity is not computed), but it is the only choice of two Szabo pairs of squares whose
  survivors span five consecutive levels.
- CONSEQUENCES.  (1) END, NP, TILT and the polygon law are false as universal laws; "END => Lemma Q" cannot be the route.  (2) The earlier statistics (no exception in 283 / 451
  tangles) came from families with thin or nearly thin knot Floer homology, where the GW sequence collapses.  (3) A possible replacement: the outline law holds for the part of N
  that survives to HFK^(K), and the part that dies is J-neutral in this example (but not for 9_46 second inversion, where N satisfies END and the dying part is not J-neutral).
- INDEPENDENT CHECK OF J (no homology).  floer/scripts/tangle_bracket.py computes the Kauffman bracket vector of the quotient tangle from the Morse word that kht++ prints
  ("Simplifies with options '-qs' to ..."), by a state sum.  Validation: trefoil gives J = t^-7 + t^-4 - t^-3 and 4_1 gives t^-6 + t^-3 - t^-2 + 1 - t, both equal to t^k L.
  For the counterexample: u = -A^9 (a unit: the closure is an unknot) and J = -t^-9 + t^-8 - t^-6 + t^-5 + t^-1 + t^2 - t^3 (t = A^4), identical to L from the lattice.
  So the Euler characteristic of N vanishes in the degree q/2 = 4 where kht++ (three fields) has its two top generators.
- PD code of the knot (after simplification, from spherogram): [(13,1,14,0),(1,15,2,14),(25,13,0,12),(15,3,16,2),(16,11,17,12),(10,17,11,18),(9,7,10,6),(21,19,22,18),(22,5,23,6),
  (23,8,24,9),(19,4,20,5),(7,24,8,25),(3,20,4,21)].  Quotient tangle word: l0.x1.l1.x2.l3.y2.y2.y1.l2.x3.y2.x4.y3.x4.y1.y2.y0.y1.y1.x3.u2.y5.y4.x3.x2.x1.u0.y1.x0.x2.x3.y1.y2.u3.y0.y1.y0.y0.y1.y0.y1.y1
  (one top end).  The knot is not identified by name.

## 8. The quadruple law (DATA; floer/scripts/quad_scan.py) and the corrected picture
Definition.  A (v,w)-QUADRUPLE is a set of four square components of BN~(T) whose first corners are X, X + (1,0), X + (4,6), X + (5,6) in (h,q)
(in lattice coordinates: S, S + w, S + v, S + v + w with w = (4,-1) the J-cancelling offset and v = (1,-1) = D - P, the Szabo bidegree k = 4).
- [PROVED] A quadruple is J-neutral: its contribution to L is sigma t^e (1-t)(1-t^4)(1 + t^-3)(1 - 1) = 0.  It is acyclic for any differential that maps S + v isomorphically
  to S (bidegree (4,6)), so it can die in a spectral sequence with Szabo bidegrees without changing J.
- [DATA] Old data (282 distinct chain files, 1388 squares): 4 w-pairs of squares (two-bridge b35_32, b35_26, b29_26 and one random word), 0 quadruples; all these tangles collapse.
  New data: the two non-collapsing tangles with unit arrows have exactly ONE quadruple each (first corners at X = (-6,-8) resp. (-1,-10)), and in both dim N - rank HFK^(K) = 16
  = the 16 generators of one quadruple.  All 28 new collapsing tangles have no quadruple.
      QUADRUPLE LAW (conjecture, 2 + 310 cases):  for a tangle with unit arrows,   dim N(T) - rank HFK^(K) = 16 x (number of (v,w)-quadruples),
      the GW sequence kills exactly the quadruples, and therefore   J = chi_q(N minus its quadruples)   with   dim(N minus quadruples) = rank HFK^(K).
- In the counterexample of section 7 the quadruple is {A, B, D, F}; N minus the quadruple is rho + C, E, G, H, which satisfies END, NP and TILT.  The violation of the outline law
  is entirely inside the J-neutral, Floer-acyclic part.  In the second example (45 -> 29) the quadruple is in the interior and N itself satisfies END.
- [REFUTED IN SECTION 9 -- kept for the record] CORRECTED OUTLINE LAW (was a conjecture): END / NP hold for N^red := N minus its (v,w)-quadruples (equivalently, conjecturally, for the E^infinity page = HFK^(K) with the bigrading
  induced by the inversion), for tangles with unit arrows.  Then, for unit arrows, Lemma Q would follow as before, because J = chi_q(N^red).
  For tangles with a non-unit D-arrow ("hinge" kind) N satisfied END in all three examples, but the part that dies is not J-neutral (9_46: it contributes
  t^-8 + t^-5 - t^-4 - t^-1 + t^-3 + 1 if the dying pairs are the (P-D)-pairs of the staircase), so there J is not chi_q(E^infinity).
- [THE REDUCED FORM OF (W) IS REFUTED IN SECTION 9] What B0 violates, in this language: B0 = a(0) + S + hS is a bare w-pair.  Bare w-pairs of squares do occur inside actual tangles (4 cases, all in the interior, all in tangles
  that collapse); a w-pair ON THE OUTLINE has been seen once, and there it comes with its v-partners, i.e. as a J-neutral quadruple.  So the candidate realization input is:
      (W)  a w-pair of compact components that is extreme for q is always half of a (v,w)-quadruple.
  B0 violates (W); (W) + "N^red satisfies NP" gives Lemma Q for unit arrows.  Neither half is proved.

## 9. A second violation: the cancellation at the top is deeper than one layer, and it survives the removal of the quadruples (DATA)
Variants of the word of section 7 (floer/scripts/ce_variants.py, run_one.py; kht++ under a time limit; HFK^ from the knot Floer program):
      word                                               crossings  dim N  rank HFK^  drop  quadruples   k   END     e-range of N    support of L    top gap
      s.r1.x2.y1.y0.r2.y0.y1.y0.y1.x2.u3.u1                   13       33      17      16       1        0   FAILS     -9 .. 4         -9 .. 3          1
      s.r1.x2.y1.y1.y1.y0.r2.y0.y1.y0.y1.x2.u3.u1             17       69      37      32       2        8   FAILS    -11 .. 4        -11 .. 1          3
      s.r1.x2.y1.y1.y1.y1.y1.y0.r2.y0.y1.y0.y1.x2.u3.u1       21      105      57      48       3       16   FAILS    -13 .. 4        -13 .. -1         5
      s.r1.x2.y1.y0.y0.y0.r2.y0.y1.y0.y1.x2.u3.u1             15       57      41      16       1        0   ok
(e = q/2 relative to rho; "top gap" = number of top quantum degrees of N in which the Euler characteristic vanishes.)
- QUADRUPLE LAW again: drops 16, 32, 48, 16 with 1, 2, 3, 1 quadruples.  Together with 3.6: five unit-arrow tangles with dim N > rank HFK^, and in all five the drop is 16 x #quadruples;
  about 340 unit-arrow tangles without quadruple, all collapsing.  k = -4 M_1 holds in all of them.
- In the 17-crossing example the three top quantum degrees of N (dimensions 2, 4, 4) all have Euler characteristic 0:
      L = -t^-11 + t^-10 - t^-9 + t^-7 - t^-6 + t^-5 + t^-3 + 1 - t      (J = t^8 L),   while N has generators up to e = 4.
  The top pair (lattice (0,1) and (4,0), i.e. (h,q) = (5,0) and (4,0)) belongs to the quadruple with base X = (-6,-16).  After removing BOTH quadruples (37 generators remain,
  = rank HFK^) the new top degree again consists of two cancelling generators: the top corners of the squares at (h,q) = (-3,-12) and (-2,-12), a w-pair that is NOT part of a
  quadruple (its would-be partners (-7,-18), (-6,-18): the second is missing).
  => The "corrected outline law" of section 8 (END for N minus quadruples) and statement (W) in its reduced form are FALSE if "N minus quadruples" is the Floer-surviving part.
     Bare w-pairs can be extreme.  The cancellation at the top of J can be at least three layers deep, and the family (y1 repeated 1, 3, 5, ... times) suggests it is unbounded.
- THE FAMILY.  T_j := the tangle of s.r1.x2.(y1)^(2j+1).y0.r2.y0.y1.y0.y1.x2.u3.u1, j = 0, 1, 2:   dim N = 33, 69, 105;   rank HFK^ = 17, 37, 57 (genus 2, 4, 6; tau = 0, 2, 4);
  quadruples 1, 2, 3 (drop 16, 32, 48);   k = 0, 8, 16 = -4 M_1;   TOP GAP = 1, 3, 5.   For j = 2:  L = -t^-13 + t^-12 - t^-11 + t^-7 - t^-6 + 2t^-5 + t^-2 - t^-1, while N reaches e = 4.
  So in this family the top 2j+1 quantum degrees of N have vanishing Euler characteristic: the depth of the cancellation is unbounded, while J keeps 7 to 9 terms.
  Checks: J of the j = 1 member recomputed from the bracket of the quotient tangle (u = 1, J = t^8 L exactly); N of the j = 1 member recomputed over Q (69 generators;
  top degrees: h = {4,5}, {3,3,4,4}, {2,2,3,3}, then {0,1,1,1,2} with Euler characteristic -1).  The j = 2 member was run over F_2 only (60 s).
- So there is no outline law of bounded depth: neither N nor its Floer-surviving part has, in general, a non-cancelling extreme quantum degree.  Lemma Q is still true in
  these examples (J has 7 resp. 9 non-zero coefficients), but the non-vanishing of J - 1 has to come from the interior of the lattice picture.

## 10. Files (all inside mech2/floer/)
- lit/*.txt: text of the arXiv PDFs read for sections 1, 2, 4 (GW 0907.4375v2, GW 1010.3727, Roberts 0706.0741v2, Lobb-Zentner 1310.7909, KM 1110.1290v2, Szabo 1010.4252v2,
  Xie 1809.01568v2, Dai-Mallick-Stoffregen 2201.01875v3, Hendricks-Lidman-Lipshitz 2007.03023v2, Lipshitz-Sarkar 2203.13895).  GW 0807.1432 and Watson, KWZ: local sources under lit/ of the project.
- scripts/hfk_word.py, hfk_word2.py: half-diagram word -> PD code -> HFK^ (spherogram + knot_floer_homology from the Codex workspace, read-only; set PYTHONPATH to
  .../work/braid_classification/packages).   scripts/collapse_check.py (+ .tsv), kslope_check.py (+ .json): dim N and k against HFK^ on the old data.
- scripts/find_candidates.py, run_candidates.py, variants.py, end_search.py, ce_variants.py, run_one.py and the .jsonl/.log files of the same names: the new kht++ runs (3.6, 9).
- scripts/extremes.py (multiplicity of the extreme quantum degrees), quad_scan.py (w-pairs and (v,w)-quadruples of squares), tangle_bracket.py (bracket vector and J of the
  quotient tangle from kht++'s simplified word; independent of Khovanov homology).
- work/: kht++ working folder (examples/words/*.kht and outputs; examples/check/ce1*, ce2*: the two violating tangles over F_3 and Q).

## SUMMARY

### What is proved (given the cited theorems)
1. THEOREM S is Grigsby-Wehrli, arXiv:0807.1432, Proposition 5.20 (any admissible balanced tangle in D x I, F_2 coefficients, E^2 = their V of the tangle = Khovanov
   homology of the MIRROR in Khovanov's resolution convention), applied to the quotient tangle with the suture separating {*,p1} from {p2,p3}; the branched double cover is the
   knot exterior with two meridional sutures (their Def 2.11, Example 2.6).  Same for every slope s: V_s(mirror T) => SFH(exterior, two sutures of slope s)
   = HFK^ of the core of the s-filling.  The annular version (Roberts 0706.0741 Prop 1.1; GW 0907.4375 Thm 2.1, Thm 3.1, Prop 2.24) says N is the top annular summand.
2. Gradings: only "annular k = Alexander grading of the lifted axis" is a theorem (GW 0907.4375 Prop 2.29; GW 1010.3727 Thm 5.1).  The bidegree (k,2k-2) is a theorem for
   Szabo's combinatorial sequence and a CONJECTURE for Heegaard Floer (Baldwin 0809.3293 Conj 1.1; GW's remark in 0807.1432 Section 7 is an unproved assertion).  For instantons
   q is only a filtration (Kronheimer-Mrowka 1110.1290 Thm 1.1); Xie 1809.01568 gives N(T;C) => THI(T) preserving the annular grading.
   The Alexander grading of K is invisible on the cube (the inversion acts by -1 on H_2).  The Floer Z/2-grading is delta mod 2, not (-1)^h.
3. Khovanov bypass triangle N_c -> V_{+-1} -> N -> N_c[1] (connecting map S); "delta x + y = u" is categorified by the 3-step filtration of the closure module (N_c, N, N_c)
   with total homology F, not by the triangle; dim N <= 2 dim N_c + 1.  The c-side does not collapse (trefoil: 8 against at most 4).
4. THEOREM F1: dim kappa(K,h) = 2(dim N - 1) >= 2(rank HFK^(K) - 1) >= 4g(K) for Watson's invariant.  Watson's rank conjecture (false for 9_46, KWZ) holds exactly as far as
   the GW sequence collapses.
5. k/4 = signed count of specials by delta-parity = first delta-moment of N (KWZ determinant constraint); J = t^k L with L the lattice sum (BRIEF2's formula is off by t^k).
6. THEOREM F3: if all specials lie on delta-levels of one parity (|k| = 4m >= 4; e.g. all torus knots by Watson; conjecturally exactly the strongly invertible L-space knots
   and mirrors) and some D-arrow has exponent not divisible by 4, then T is not flat; J - t^k has no cancellation at all.  (Also: m <= 2 and no D^(4l) arrow => not flat.)
7. Formal negative: B0 passes every Floer-side test (rank, delta-parity, first moment, (e,o), Szabo bidegrees in closures).  The Floer analogue of END is false (Delta = 1).

### What is data
8. GW's grading Conjecture 7.1 is false as stated: N of the 4_1 tangle has delta-levels (2,2,1) and E^2 = E^infinity, but HFK^(4_1) has three generators in one (A,M);
   the same for their own 2-cable case of 4_1 ((2,6,9,6,2) against rank 11 in bidegree (0,0)).
9. dim N = rank HFK^(K), HFK^ computed from the words with Szabo's program: 383 of 384 old tangles; 28 of 33 new ones chosen among thick and L-space-like knots.
   Non-collapsing tangles found (8 in all, sections 3.6 and 9), of two kinds: three with a D^2 arrow in the arc ("hinge"), five with unit arrows and 1, 1, 2, 1, 3
   (v,w)-quadruples of squares (drop 16 per quadruple).
10. k = -4 M_1(K), M_1 = sum (-1)^M M over HFK^(K): 405 of 406 tangles (failure: 9_46 second inversion).  For thin knots this is 4 tau, for L-space knots it is not.
11. The Alexander-polynomial-one knot of BRIEF2: not one of 11n34, 11n42, 12n313, 12n430; HFK^ rank 31 (genus 2, tau = 1), so dim N = rank HFK^ = 31.  Second class: 65 = 65.
12. COUNTEREXAMPLE to END / NP / TILT / polygon law: word s.r1.x2.y1.y0.r2.y0.y1.y0.y1.x2.u3.u1 (13 crossings, rank HFK^ 17).  N = point + 8 squares; the top quantum degree
    contains two generators in homological degrees 4 and 5 (over F_2, F_3, Q); J = -t^-9 + t^-8 - t^-6 + t^-5 + t^-1 + t^2 - t^3, confirmed by an independent bracket computation.
    Lemma Q holds for it.  The offending pair of squares is a B0-pair on the outline, and it is half of a J-neutral (v,w)-quadruple; N minus the quadruple satisfies END.
13. Second violation (17 crossings, dim N = 69, rank HFK^ = 37, two quadruples): the three top quantum degrees of N have zero Euler characteristic, and END still fails after
    removing both quadruples (a bare B0-pair becomes extreme).  In the family T_j (block y1 repeated 2j+1 times; j = 0,1,2) the top 2j+1 quantum degrees of N have zero
    Euler characteristic (top gap 1, 3, 5), dim N = 33, 69, 105, rank HFK^ = 17, 37, 57, and the drop is 16(j+1) = 16 x #quadruples.

### What is conjectured
F2: k = -4 M_1(K).   F4: a refinement of THEOREM S compatible with d_P and the differential of HFK^ => HF^(S^3) (would give F2 under collapse).
QUADRUPLE LAW: for unit arrows, dim N - rank HFK^ = 16 x #(v,w)-quadruples (5 tangles with 1, 1, 2, 1, 3 quadruples; about 340 without), and the quadruples are what dies.
Refuted here: GW Conjecture 7.1; "unit arrows => collapse"; the naive lifted-curve model; END / NP / TILT / polygon law as universal laws (sections 7, 9);
the "corrected outline law" (END for N minus its quadruples) and (W), by the 17-crossing example of section 9.

### The named gap
COLUMN GAP.  The Floer side determines (at best) the rank of N, the two numbers (e,o) of specials on even and odd delta-levels, and (conjecturally) which part of N survives;
it never sees the column coordinate a (the quantum grading inside a delta-level).  Cancellation in J happens only between specials on levels of opposite parity lying on
different components, at lattice offset (4,-1).  Such pairs DO occur at the extremes of N (sections 7, 9), in the first example as half of a J-neutral quadruple, in the second
also as a bare pair one layer further in; in the family T_j the top of J is 1, 3, 5 quantum degrees below the top of N.  So no statement about the outline of N (END, NP, TILT), nor
about the outline of its Floer-surviving part, can be the mechanism.  What is missing is a reason why the cancellation cannot go all the way, i.e. why J - 1 != 0, when specials
of both parities are present.  The one-parity case is closed (F3); every case with a box on the Floer side is open.  Nothing here proves Lemma Q.

### The single most promising next step
Stop looking for an outline law.  The three violating tangles belong to a one-parameter family (the block y1 repeated 1, 3, 5, ... times in s.r1.x2.[y1...].y0.r2.y0.y1.y0.y1.x2.u3.u1)
in which the depth of the cancellation at the top of J grows (1, 3, 5 for the first three members).  Work out this family in closed form: N as a function of the twist parameter (the squares form a ladder
of w-pairs and (v,w)-quadruples), J as a function of the twist parameter, and the reason J - 1 does not vanish (it is t^-9(1-t)(1-t^4)(1+t^4)(1+t^3) times a unit for the first
member).  Any mechanism for Lemma Q has to survive this family, whose outline consists of B0-pairs; this is the smallest place where "what do actual tangles have that B0 lacks"
can be read off.  On the Floer side the parallel computation is the E^infinity page for the same family (is the dying part exactly the quadruples, via d_4 along v?), which
would settle the QUADRUPLE LAW and tell whether J is the q-graded Euler characteristic of the surviving part.
