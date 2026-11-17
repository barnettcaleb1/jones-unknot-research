# REPORT — LENS COLORED (doubled tangles and coloured Khovanov homology)

STATUS (2026-11-16): complete for this session.  Sections 0 (working log), 1 (literature), 2 (Theorem A), 3 (Theorem B), 4 (hexagon law),
5 (Habiro lift, closed formulas), 6 (edge directions), 7 (B0 for doubles), 8 (hidden involution), SUMMARY at the end.  Scripts in py/, kht++ runs in kht/, papers in lit/.
Marks: PROVED / CITED (source, statement no., read-now or recalled) / DATA / CONJECTURED.

## 0. Working log (appended as I go)

### 0.1 Reformulation used throughout  [PROVED, elementary]
Let T be a 2-string tangle, D a diagram of the closure T(n) in the direction of the horizontal sum (the closure that turns b into two
circles), p_1, p_2 one point on each closing arc, X_i the basepoint maps (multiply by x on the circle through p_i) on CKh(D; F_2).
    N(T) = H( X_1 X_2 CKh(D), d_Kh )     (up to a bigrading shift, for every n).
Reason: X_1X_2 CKh(D) is spanned by the labelled states in which p_1 and p_2 lie on two different circles, both labelled x.
It is a subcomplex (the X_i commute with merges and splits), a merge of the two marked circles is x(x)x -> 0, and these are exactly the
rules of the annular differential in annular weight -2 (isomorphic to weight +2); this is description (b) of BRIEF2.  For T = T_K
(doubled strand) D can be taken to be the 2-cable of ANY diagram of K with ANY framing (N(T sigma^n) = N(T) up to shift, since the
b-resolutions of T sigma are the b-resolutions of T with sigma resolved to b).  This is Khovanov's reduced 2-coloured homology in
the Grigsby-Wehrli form.

### 0.2 First structural finding: N(T_K) is an l-graded tensor square  [DATA, 21/21 doubles; mechanism in section 2]
Let l = h - q.  In lattice coordinates l = -(a+3b).  For every one of the 21 two-bridge doubles in lit/kht/out/dbl:
    multiset { a+3b : (a,b) in N(T_K) }  =  multiset { h_1 + h_2 : h_i in supp Kh~(K) }  + const        (py/lgrade.py)
i.e. N(T_K) = Kh~(K) (x) Kh~(K) as spaces graded by l = h - q.  The second grading is NOT the tensor grading: each tensor
generator is moved along the l-level line by a multiple of (h,q) = (2,2)  (lattice (-3,1)).
E.g. T(2,2n+1): N = staircase(4n+1) + n^2 squares; the squares are the squares of staircase(2n+1) (x) staircase(2n+1)
(Minkowski positions (m,-m), multiplicity mult(m) = min(m,2n-m), m = 1..2n-1) moved by s(-3,1), s = 1..mult(m).
Checked on n = 1..6 (k3_2, k5_4, k7_6, k9_8, k11_10, k13_12).

### 0.3 POLYGON FORMULA for doubles of two-bridge knots  [DATA, 21/21, exact; py/ranges.py]
Let Kh~(K) (thin) have homological support [h_min, h_max] and surviving generator at q = s (Rasmussen s; h = 0).  Put
    B = s - h_min,   G = h_max - s,   B + G = c(K) (crossing number).
For a reduced alternating diagram {B, G} = {|s_A| - 1, |s_B| - 1}.  Then in lattice coordinates (a,b) relative to rho the convex
hull of N(T_K) is EXACTLY
    P(B,G) = { -B <= b <= G,   -B <= a+b <= G,   -B <= a+2b <= G,   |a| <= c-1 },
and in addition a+3b ranges over [-2B, 2G] and a+4b over [-3B, 3G]  (all 21 doubles; every bound is attained).
In (h,q):  b = h - q/2 = -delta,  a+b = 2q - 3h,  a+2b = (3q - 4h)/2,  a = (5q - 8h)/2,  a+3b = q - h = -l.
In the coordinates u = b, v = a+b this is the hexagon { u, v, u+v in [-B,G] } with its two acute corners (G,-B), (-B,G) cut off
by |v-u| <= c-1.  The unique top-q generator is g_B = (a,b) = (-G, G), the unique bottom-q generator is g_A = (B, -B);
the row b = 0 of rho runs from a = -B to a = G.
Examples: 3_1: (B,G) = (2,1); 4_1: (2,2); 5_1: (4,1); 5_2: (2,3); 6_1: (2,4); 6_3: (3,3); T(2,2n+1): (2n,1).

### 0.4 Mechanism behind 0.2: a pointed Batson-Seed spectral sequence  (details and proof in section 2)
N(T) = H(X_1X_2 CKh(L)) for the two-component link L = T(n) (0.1).  Batson-Seed's deformation d = d_0 + d_1 (backward saddle maps at the
crossings between the two components; arXiv:1303.6240, section 2.2, read now) commutes with X_1, X_2 (their Prop. 6.3), is literally
unchanged by a crossing change between the components over F_2 (their Prop. 2.3), and their Reidemeister equivalences (Prop. 3.2)
commute with X_p for p away from the move.  Hence a spectral sequence
        E_1 = N(T)  ==>  Kh~(t_1^) (x) Kh~(t_2^)        (t_i^ = the knot obtained by closing the i-th strand of T alone),
d_k of (h,q)-bidegree (1-2k, -2k), i.e. lattice (3k-4, 1-k); it preserves nothing but raises l = h-q by one, so the abutment is
l-graded.  For T_K both strands are K:  N(T_K) ==> Kh~(K) (x) Kh~(K),  dim N(T_K) >= (dim Kh~ K)^2, and the 21 data points say the
sequence collapses for two-bridge K (dim N = det^2), which is exactly 0.2.


---------------------------------------------------------------------------------------------------------------------------
## 1. Literature (task 1)

Conventions: t = q^2 (kht q). J_3 = reduced Jones polynomial coloured by the 3-dimensional representation (unknot = 1); N(T_K) = Kh~_2(K),
Khovanov's reduced 2-coloured homology in Grigsby-Wehrli's sutured form.  "read now" = I opened the text during this session
(sources saved under colored/lit/); "recalled" = from memory, not re-read.

1.1 Is "J_3 detects the unknot" open?  YES, as far as I can find; and it is exactly Lemma Q on the swap inversions.
 - [PROVED, classical bracket argument; also used in Stoimenow's proof below] T_K flat  <=>  J_3(K) = 1  <=>  V(Wh_+(K)) = 1  <=>  V(Wh_-(K)) = 1
   <=> the w-framed 2-cable of K has the Jones polynomial of the torus link T(2,2w)  (untwisted Whitehead doubles = T_K(+-1/2); the bracket
   vector of T_K is determined by J_3 and the framing).
 - [CITED, read now] A. Stoimenow, "Coefficients and non-triviality of the Jones polynomial", arXiv:math/0606255 (J. reine angew. Math. 657
   (2011)), Proposition 4.3: "Let K be a semiadequate non-trivial knot. Then the untwisted Whitehead doubles Wh_+-(K) of K (with either clasp)
   have non-trivial Jones polynomial."  The text after it: this generalises Lickorish-Thistlethwaite (adequate) and Stoimenow (positive);
   Remark 4.2: among Whitehead doubles only untwisted ones may have trivial Jones polynomial; and "no non-trivial knot of <= 16 crossings has
   untwisted Whitehead doubles with trivial Jones polynomial".  He calls untwisted doubles "one suggestive class of knots to look for trivial
   Jones polynomial".   ==> J_3(K) != 1, i.e. LEMMA Q HOLDS FOR THE SWAP INVERSION ON K # K^r, for every semiadequate K and for all K
   with at most 16 crossings.  No statement for general K was found.
 - [CITED, read now, abstract] J. E. Andersen, arXiv:1206.2785: "if a knot has the same colored Jones polynomials as the unknot, it must be
   the unknot" (ALL colours together; via asymptotics of WRT invariants of 1-surgery and Kronheimer-Mrowka's SU(2) representations).
   Dunfield-Garoufalidis (arXiv:math/0405353, recalled): the same conclusion is implied by the AJ conjecture.  Nothing for one fixed colour.
 - [CITED, read now] Grigsby-Wehrli, arXiv:0807.1432 (Adv. Math. 223 (2010)), Theorem 1.2: for each n a spectral sequence with E^2 = Kh~_n(mirror K)
   and E^infinity = HF^(Sigma(K)) (n = 1), HFK^(Sigma(K), K~) (n odd > 1), HFK^(S^3, K # K^r) (n even); Corollary 1.3: Kh~_n detects the unknot for
   all n > 1.  This is THEOREM S of BRIEF2 for T_K.  (Their Theorem 5.19 + 6.1; the identification of Kh~_n with the Khovanov functor of the
   n-cabled balanced tangle is their section 5.2.)
 - [CITED, read now, abstracts] Hedden, arXiv:0805.4418: Khovanov homology of the 2-cable detects the unknot (hence Khovanov's unreduced
   2-coloured homology does).  Hedden-Watson, arXiv:0805.4423: Khovanov homology detects the unknot among unknotting-number-one knots, Whitehead
   doubles, (2,1)-cables (these are the closures T(1/n) of our tangles).  Kronheimer-Mrowka (Kh detects the unknot) and Baldwin-Sivek
   (arXiv:1801.07634, Kh detects the trefoils): recalled, both quoted in Robinson's introduction which I read.
 - [CITED, read now, whole note] G. Robinson, arXiv:1809.00055, Theorem 2.1: K is a trefoil iff rk Kh~_2(K) = 9.  Its last paragraph: rk Kh~_2 = 9
   for the trefoil and 25 for the figure-eight "suggests that perhaps the spectral sequence always collapses by the E^2 page for alternating
   knots, however this is not true for links since the 2-4 torus link has rk Kh~_2 = 18".   Our data: collapse for all 21 two-bridge doubles.
 So: the categorified statement (Kh~_2 detects the unknot and the trefoil) is known; the polynomial statement is open beyond semiadequate knots.

1.2 Extreme degrees of coloured Khovanov homology versus the coloured Jones polynomial.
 - [recalled] Polynomial side: for an A- (resp. B-) adequate diagram the lowest (resp. highest) coefficient of every coloured Jones polynomial
   is +-1 and the extreme degree is the one of the all-A (all-B) state of the cable (Lickorish's book ch. 5 and 14; Le; Dasbach-Lin, Compositio
   2006, for the head and tail of V and of J_N; Armond, arXiv:1112.3995 and Garoufalidis-Le, arXiv:1112.3905: the tail of J_N stabilises as
   N -> infinity for adequate links).  For non-adequate diagrams the all-A contribution cancels (C. Lee, "A trivial tail homology for non
   A-adequate links", arXiv:1611.00686) and the true degree is governed by Jones slopes (Garoufalidis' slope conjecture; the degree of J_N is
   a quadratic quasi-polynomial in N for N large); there is no general theory of the degree or of the extreme coefficient of J_N for a FIXED
   small colour of a non-semiadequate knot.
 - [CITED, read now, abstract] L. Rozansky, "Khovanov homology of a unicolored B-adequate link has a tail", arXiv:1203.5741: the coloured Khovanov
   homology (projector model) of a B-adequate link has a stable tail whose Euler characteristic is the tail of the coloured Jones polynomial.
   This is in the Cooper-Krushkal / Rozansky model (categorified Jones-Wenzl projectors, arXiv:1005.5117, unbounded complexes; recalled), not in
   Khovanov's finite cabling model.  Hogancamp (arXiv:1405.2574, recalled): End(P_n) contains a polynomial ring with generators u_k of bidegree
   q^{2k} t^{2-2k}; Beliakova-Wehrli (arXiv:math/0510382, recalled): cabling categorifications and Rasmussen invariants for links.
   I found no published statement that the extreme q-degrees of Khovanov's REDUCED cabling homology Kh~_n are one-dimensional for adequate
   knots; section 3 below proves it (the argument is the standard extreme-state argument and is surely known to experts).
 - [recalled] Grigsby-Licata-Wehrli, arXiv:1505.04386: the sutured annular Khovanov homology of an n-cable carries commuting actions of sl_2 and
   of S_n ("knotted Schur-Weyl"); N(T_K) is the top weight space for n = 2 and so carries an involution (trivial information over F_2).
 - [CITED, read now, abstract; body recalled] P. Wedrich, "Exponential growth of colored HOMFLY-PT homology", arXiv:1602.02769: reduced coloured
   sl(N) and HOMFLY-PT homologies and deformation spectral sequences; proves the Gorsky-Gukov-Stosic conjecture that Lambda^k-coloured reduced
   HOMFLY-PT homology is at least as large as the k-th tensor power of the uncoloured one (Gukov-Stosic arXiv:1112.0030, GGS arXiv:1304.3481:
   "refined exponential growth", recalled).  Section 2 below is the Sym^2 / sl_2 / cabling-model counterpart, obtained from Batson-Seed.
 - [CITED, read now, sections 1-3 and 6.1] J. Batson, C. Seed, "A link splitting spectral sequence in Khovanov homology", arXiv:1303.6240 (Duke
   Math. J. 164 (2015)): Theorem 1.1 (spectral sequence Kh(L) => Kh of the split link, for weights with invertible differences), Prop. 2.2
   (d^2 = 0), Prop. 2.3 (a crossing change between components gives an isomorphic complex), Prop. 3.2 (Reidemeister invariance, l-graded and
   q-filtered), Cor. 3.4 (rank^l Kh(L) >= rank^{l+t} of the tensor product, t = sum 2 lk), Prop. 6.3 (X_p commutes with the total differential).

1.3 Habiro.  [recalled; the integrality is confirmed numerically below] K. Habiro (Invent. Math. 171 (2008)): J_N(K) = sum_{n>=0} a_n(K) prod_{k=1}^n
 {N+k}{N-k}, {m} = t^{m/2} - t^{-m/2}, a_n in Z[t^{+-1}] independent of N.  Masbaum (2003) for twist knots.  For N = 3:
 J_3 = 1 + a_1 X_1 + a_2 X_1 X_2,  X_1 = {4}{2} = t^{-3}(1-t^2)(1-t^4),  X_2 = {5}{1} = t^{-3}(1-t)(1-t^5),  a_1 = (V-1)/({3}{1}).
 [DATA] For all 21 doubles a_2 computed from N(T_K) and Kh~(K) is a Laurent polynomial (py/habiro.py).


---------------------------------------------------------------------------------------------------------------------------
## 2. THEOREM A: a pointed link-splitting spectral sequence for N(T)   [PROVED, given Batson-Seed sections 2-3 as read]

Setting. T a 2-string tangle with strands t_1, t_2 joining left ends to right ends (connectivity b; if the connectivity is crossed, replace
T by T sigma, which does not change N).  L = T(n) = L_1 u L_2 the closure in the direction of the sum, L_i containing t_i, p_i a point on the
closing arc of L_i, D a diagram of L.  t_i^ := the knot type of L_i (the strand t_i closed up alone).  F = F_2.  C = CKh(D), d_0 = Khovanov
differential, l = h - q (Batson-Seed's internal grading: l = deg(monomial) - #circles - writhe; it does not see the cube coordinate),
g = q/2 up to a constant.

    THEOREM A.  There is a spectral sequence with
        E_1 = N(T) = H(X_1X_2 C, d_0)      and      E_infinity = gr H(X_1X_2 C, d_0 + d_1)  with  H(X_1X_2 C, d_0+d_1) = Kh~(t_1^) (x) Kh~(t_2^)
    as l-graded spaces (l shifted by 2 lk(L_1,L_2)).  The differential d_k has (h,q)-bidegree (1-2k, -2k); in lattice coordinates it
    sends (a,b) to (a+3k-4, b+1-k):  k=1: (-1,0) = -D,  k=2: (2,-1),  k=3: (5,-2), ...
    Consequences:  (i)  dim N(T) >= dim Kh~(t_1^) dim Kh~(t_2^);
                   (ii) with P_N(x) = sum over N of x^l and W_i(x) = sum over Kh~(t_i^) of x^(h-q):
                              P_N(x) - x^c W_1(x) W_2(x) = (1 + x) R(x),   R with non-negative coefficients;
                   (iii) equality in (i) iff the sequence collapses at E_1, and then N(T) = Kh~(t_1^)(x)Kh~(t_2^) as l-graded spaces.
    For the doubled tangle T_K:  N(T_K) ==> Kh~(K) (x) Kh~(K),  dim Kh~_2(K) >= (dim Kh~(K))^2.

Proof.
 (1) Deformation.  d_1 := sum of the backward saddle maps over the edges of the cube at crossings between L_1 and L_2 (Batson-Seed 2.2 for two
     components over F_2).  d = d_0 + d_1 squares to zero (BS Prop. 2.2; over F_2 the term of d^2 at a state is sum over mixed crossings of
     X_p + X_q for the two arcs at the crossing, which telescopes to zero along L_1 because every self-crossing of L_1 is visited twice).  d raises l by
     1; d_0 preserves q, d_1 lowers q by 2.  Filtering by q gives the spectral sequence; E_0 = (C, d_0).  [CITED BS 2.2, read now]
 (2) Basepoints.  X_p commutes with every saddle map, hence with d_0 and d_1 (BS Prop. 6.3).  So X_1X_2 C is a filtered subcomplex of (C, d);
     its E_1 page is H(X_1X_2 C, d_0) = N(T) by 0.1.
 (3) Crossing changes.  If D' differs from D by changing crossings between L_1 and L_2, then (C(D), d) and (C(D'), d') are the SAME complex on
     the same labelled states (the 0- and 1-smoothings of the changed crossings are interchanged, forward and backward saddles are
     interchanged, and d contains both); BS Prop. 2.3.  The identification is the identity on labelled states, so it commutes with X_1, X_2 and
     carries X_1X_2 C(D) onto X_1X_2 C(D').  Only the q-filtration changes.
 (4) Splitting.  Change crossings until L_1 lies entirely above L_2.  Shrink L_1 by a homothety centred at p_1 (in the closure diagram p_2 lies on
     the outermost arc and p_1 on the next one, so the ray from p_1 through p_2 does not meet the diagram again and no strand ever passes over or
     under a marked point): this is a sequence of Reidemeister II and III moves between L_1 (over) and L_2 (under), all away from p_1, p_2, ending
     in a split diagram D_1 u D_2 with p_i on D_i.
 (5) Reidemeister invariance.  BS Prop. 3.2 proves that each move gives an l-graded, q-filtered chain homotopy equivalence, by the cancellation
     lemma (their Lemma 3.1): the maps f, g, h are built from components of d between the summands indexed by the local resolutions, and from
     the splitting of one summand according to whether the monomial contains the small circle created by the move.  For p outside the disc of
     the move, X_p preserves these summands and commutes with all components of d, hence with f, g, h.  So f, g, h restrict to X_1X_2 C and
     give a filtered homotopy equivalence of the pointed subcomplexes.  [BS use the same compatibility for their Proposition 6.5:
     "The total homology and A_m action are also invariant under Reidemeister and marked point moves"; read now.]
 (6) For the split diagram d_1 = 0 and X_1X_2 C(D_1 u D_2) = X_1 C(D_1) (x) X_2 C(D_2), whose homology is Kh~(t_1^) (x) Kh~(t_2^) (Kunneth over
     F).  The l-shift is as in BS Cor. 3.4.  (i)-(iii) are the standard consequences for a spectral sequence whose differentials raise l by 1.  QED

Remarks.
 (a) Theorem A is the Sym^2, sl_2, cabling-model counterpart of the "exponential growth" of coloured homology (Gukov-Stosic, GGS; Wedrich for
     Lambda^k-coloured HOMFLY-PT).  I did not find it stated for Khovanov's reduced coloured homology.  It needs no Floer theory.
 (b) Compared with THEOREM S (dim N(T_K) >= (rk HFK^(K))^2): Theorem A gives (dim Kh~(K))^2 >= (rk HFK^(K))^2 (Dowlin's spectral sequence,
     recalled), keeps a grading (l), and applies to every tangle whose strands are knotted.  For a general strong inversion the strands of the
     quotient tangle are the two half-axis arcs; t_1^, t_2^ are the two constituent knots (other than the unknot U = axis image) of the quotient
     theta-curve.  If both are unknots (the generic case for Lemma Q, e.g. all two-bridge quotients) Theorem A only says N(T) ==> F: a third
     cancelling structure on N besides d_D (bidegree (1,2)) and d_P ((5,8)), with first differential of bidegree (1,2) again.
     B0 = pt + S + hS is compatible with it (each square cancels in itself by two d_1's).  So Theorem A does not exclude B0 for unknotted strands.
 (c) [DATA] Collapse: all 21 two-bridge doubles (dim N = det^2; l-graded identity of 0.2 checked, py/lgrade.py).
     NON-collapse: the double of 8_19 = T(3,4), computed now (kht/examples/dbl/k819, 195 s): dim N(T_K) = 41 = arc(9) + 8 squares, while
     (dim Kh~)^2 = (rk HFK^)^2 = 25.  The l-distributions (from the lowest l) are
          N:        2 3 4 6 5 8 5 3 4 0 1          Kh~(x)Kh~:   1 0 2 4 1 6 4 2 4 0 1,
     and the difference is (1+x)(1 + 2x + 2x^3 + 2x^4 + x^6): (ii) holds with R >= 0, eight cancelling pairs.  So neither Theorem A's nor
     Theorem S's sequence collapses for the double of 8_19 (first example with 1 + 2m > rk HFK^ among doubles).
 (d) PROPOSITION (delta-strip) [PROVED].  Suppose Kh~(K) is thin and the sequence for T_K collapses (e.g. the 21 data knots).  Let D be any
     diagram of K with c crossings.  Then N(T_K) is supported in at most c+1 consecutive delta-gradings.
     Proof: the complex (X_1X_2 C(D^2), d) carries the filtration F of D^2 and the filtration F' of the diagram D' in which copy 1 lies over
     copy 2; D' differs from D^2 at exactly one crossing over each crossing of D, so on every labelled state the two q-degrees differ by
     c - 2u + const, u in [0,c] the number of changed crossings that are 1-smoothed.  F' is the filtration of the split link, whose sequence
     collapses at E_1, so on H^l it has a single jump, at q = -2l + const (thinness).  Comparing the two filtrations on H^l, gr_F H^l can be
     non-zero only for q in a window of c+1 consecutive even values around -2l + const, i.e. b = h - q/2 = l + q/2 takes at most c+1 values.  QED
     For a reduced alternating D the two extreme generators of section 3 lie exactly c delta-levels apart, so the width is exactly c: this is
     the pair of horizontal edges b = -B, b = G of the polygon formula 0.3.


---------------------------------------------------------------------------------------------------------------------------
## 3. THEOREM B: END and NP for doubles of adequate knots (and for "b-adequate" tangle diagrams)   [PROVED]

    THEOREM B.  Let D be a diagram of the closure T(n) (n arbitrary) with the marked points p_1, p_2 on the two closing arcs, with c crossings,
    n_+ positive ones, all-A state s_A and all-B state s_B.
    (A) If D is A-adequate and p_1, p_2 lie on different circles of s_A, then N(T) is ONE-dimensional in its lowest q-degree, spanned by
        g_A = (s_A, every circle labelled x), in the lowest homological degree of the cube.
    (B) If D is B-adequate and p_1, p_2 lie on different circles of s_B, then N(T) is ONE-dimensional in its highest q-degree, spanned by
        g_B = (s_B; x on the two marked circles, 1 on all others), in the highest homological degree of the cube.
    In particular, if both hold, T satisfies END and NP (hence T is not flat unless N = F), with extreme coefficients +-1.
    COROLLARY.  If K has an adequate diagram D (for instance K alternating), then both hold for T_K with the blackboard 2-cable D^2:
    Kh~_2(K) is one-dimensional in its top and in its bottom quantum degree, the two generators lie in homological degrees 4c apart and
    quantum degrees 2(|s_A(D)| + |s_B(D)|) + 4c - 4 apart ( = 6c, i.e. the lattice vector c(P - D), when D is reduced alternating).
    If K is only A- (or B-) adequate, one extreme degree is one-dimensional.  The same proof gives one-dimensional extreme degrees of
    Kh~_n(K) for every colour n (n marked points on the n parallel strands).

Proof.  By 0.1, N(T) = H(X_1X_2 C(D), d_0); a generator is a labelled state with the two marked circles distinct and labelled x, and
q = (#1 - #x) + r + n_+ - 2n_-, r = number of 1-smoothings.
 (A) Every state s != s_A is reached from s_A by r(s) switches, the first of which merges two circles (A-adequacy), so |s| <= |s_A| + r(s) - 2
     and min_q on s is -|s| + r(s) >= -|s_A| + 2.  Hence g_A is the unique generator of the whole Khovanov complex in the lowest q-degree;
     it lies in X_1X_2 C because the marked circles are distinct; d_0 g_A = 0 (every edge out of s_A merges two x's); it is not a boundary
     (lowest homological degree).
 (B) Every generator of X_1X_2 C has at least two x's, so max_q on s is |s| - 4 + r(s).  For s != s_B, B-adequacy gives |s| + r(s) <= |s_B| + c - 2.
     So g_B is the unique generator of X_1X_2 C in the top q-degree; it is a cycle (top homological degree) and not a boundary (nothing else
     in its q-degree).
 Corollary: the all-A state of the 2-cable is the 2-cable of the all-A state.  (Explicitly, at a crossing of D with bands O = {y = +-1} over
     U = {x = +-1}, the four A-smoothed arcs are two parallel copies of each A-arc; the self-crossings (-1,1), (1,-1) are chords between the
     two copies of one circle of s_A(D), the mixed crossings (1,1), (-1,-1) are two parallel chords between the near copies of the two
     circles of s_A(D) meeting at the crossing.)  So D^2 is A-adequate iff D is, and the marked points lie on the two copies of one circle.
     Same for B.  The framing of D^2 is irrelevant because N(T sigma^n) = N(T).  Degrees: r(g_B) - r(g_A) = 4c, q(g_B) - q(g_A) =
     (2|s_B| - 4 + 4c) + 2|s_A|.  QED

Comments.
 - Theorem B is the categorification, in Khovanov's reduced cabling model, of the classical fact that coloured Jones polynomials of adequate
   knots have extreme coefficients +-1.  It proves NP (in the strong form "the extreme q-degree is a single generator") for the doubles of
   all adequate knots, and one half of it for semiadequate knots.  For the latter Lemma Q itself is known (Stoimenow Prop. 4.3, section 1.1).
 - It is a statement about a DIAGRAM of the closure, so it applies to any strong inversion whose quotient tangle has a diagram D_T with
   s_A(D_T), s_B(D_T) of connectivity b and D_T(0) adequate ("b-adequate tangle diagram").  [not surveyed here which table inversions have one]
 - B0 violates (A) or (B) trivially (its extreme degrees have Euler characteristic 0); the input B0 lacks is a diagram.
 - What it does not give: non-semiadequate K, where the extreme state is killed (cf. C. Lee) and the true extreme degree is not at a corner
   of the cube.  Example computed now: 8_19 = T(3,4) is a positive braid knot, adequate on one side only; its double still has
   one-dimensional top and bottom q-degrees (41 generators), so END/NP hold there, but the hull has new edge directions (section 4.4).
 - [DATA, py/endplus.py] Over all 279 distinct tangles in the data files the top and the bottom q-degree of N are one-dimensional except
   9_37 second inversion (top: 2) and 9_40 second inversion (bottom: 2); in both the two generators have the same delta (END still holds).


---------------------------------------------------------------------------------------------------------------------------
## 4. The outline of N(T_K): hexagon law, what is proved, where the proof stops (task 2, second half)

4.1 HEXAGON LAW [DATA, exact for the 21 two-bridge doubles; restated from 0.3].  With B = s - h_min, G = h_max - s (data of Kh~(K); for a reduced
alternating diagram {B,G} = {|s_A|-1, |s_B|-1}, B + G = c), and g_A = rho + B(D - P) the bottom generator:
        hull N(T_K)  =  g_A + G Delta_1 + B Delta_2,  minus one unit at two corners,
        Delta_1 = conv{0, D, P-D},   Delta_2 = conv{0, P-2D, P-D}          (Minkowski sum of two triangles; plane geometry from 0.3).
Equivalently: writing a generator as g_A + alpha D + beta (P-2D), one has 0 <= alpha <= c, 0 <= beta <= c, -B <= alpha - beta <= G
(beta = delta-level above g_A, alpha = (a+2b) above g_A), and the two corners g_A + G D and g_B - B D are cut off (|a| <= c-1).
The six vertices are g_A, g_B = g_A + c(P-D), W_1 = rho + G D, W_2 = rho - B D (the two ends of the delta-level of rho), and the two cut corners.
So for these knots all edges have directions D = (1,2), P-2D = (3,4), P-D = (4,6) (in (h,q)), plus P at the two unit cuts: the polygon law of
BRIEF2, in an exact form.  NP is immediate from it: q is positive on D, P-2D and P-D, so q is maximal only at g_B and minimal only at g_A.

4.2 Meaning of the three vectors [PROVED, local computation py/cabled_crossing.py].  A 2-cabled crossing has 16 smoothings: one is the cable A^2 of the
A-smoothing (r = 0), one the cable B^2 of the B-smoothing (r = 4), nine contain a turnback (a cap joining the two strands of one band end), and
five give the same turnback-free pattern M (outer arcs turn as in A, inner arcs as in B): two with r = 1 (one mixed crossing switched), one with
r = 2 and an extra circle (both mixed crossings), two with r = 3 (both mixed and one self-crossing).  After cancelling the circle the M-part is
M{h q} + M{h^3 q^3}.  Relative to the all-x generator over A^2 (and when the change merges circles, as from an adequate all-A state) the all-x
generators over M_1, M_3, B^2 sit at
        M_1: (1,2) = D,     M_3: (3,4) = P-2D,     B^2: (4,6) = P-D,       M_3 - M_1 = (2,2) = P-3D  (the l-preserving vector).
So Delta_1 = {A^2, M_1, B^2} and Delta_2 = {A^2, M_3, B^2}: the hexagon is what one gets if G crossings (a spanning tree of the Tait graph) use
the low copy of M and the other B crossings (the dual tree) use the high copy.  This is task 3's answer for (1,0), (1,-1), (2,-1).

4.3 What is proved towards the hexagon for alternating K.
 (i)  [PROVED, Theorem B] g_A and g_B are generators of N, alone in their q-degrees, and g_B - g_A = c(P-D).  (All adequate K, with 6c -> 6c - 4g_T.)
 (ii) [PROVED under collapse of Theorem A, Prop. 2(d)] the strip 0 <= beta <= c (the edges parallel to D), with g_A, g_B on its two sides.
 (iii)[PROVED under collapse] the l-projection: #{generators with alpha + beta = k} = #{pairs in Kh~(K)^2 with total height k}; in particular the
      extreme l-degrees are one-dimensional (g_A, g_B).
 (iv) THREE-STATE REDUCTION  [corrected: my first version claimed that every turnback state of a cabled crossing has N = 0; that is false].
      [PROVED] If the band is cut at ONE POINT and both sides are capped (a turnback e inserted in the doubled strand), both pieces are fingers,
      they retract along the band, the tangle is c and N = 0.  So N(T_K) does not change if categorified Jones-Wenzl projectors P_2
      (Cooper-Krushkal: P_2 = identity + an infinite tail of turnback terms; recalled) are inserted on the band [PROVED modulo the standard
      convergence of the tail], and between projectors a cabled crossing has only the states A^2, M{hq}, M{h^3q^3}, B^2{h^4q^4} of 4.2.  This is
      the form of the cabling cone in the reduced theory: the empty-cable terms are the turnback terms and they are killed by the top-weight
      condition, but only after projecting.
      [PROVED] Without projectors, the 16-state cube at a crossing x of D gives a spectral sequence converging to N(T_K) from
      N(A^2_x) + N(M_x){hq} + N(M_x){h^3q^3} + N(B^2_x){h^4q^4} + (turnback states).  The 9 turnback states are: four caps (1 state, r = 2),
      two caps at a corner with the doubled arc at the opposite corner (4 states, r = 1,1,3,3), one cap and a Y-pattern (4 states, r = 2)
      (py/cabled_crossing2.py).  Write K = alpha.lambda.omega (lambda = the loop of the long knot between its two passages through x).  A turnback
      state has N = 0 as soon as one of its caps sits on the end of alpha or of omega (finger).  The survivors are the states that cap only the
      loop: the corner state at the loop corner, with N = N(T_K') (x) V, and two one-cap states, with N = N(T_K') each, where K' = alpha.omega is
      K with the loop removed.  They sit in cube degrees 1 (or 3), 2, 2 and are connected by d_1 to each other and to the M-terms (I did not
      compute the E_2 page).  So a cabled crossing
      has, without projectors, FOUR kinds of terms: A^2, M (twice), B^2 and the loop-removal terms; the latter are the trace of the empty cable.
      (A^2_x, B^2_x = doubles of the two resolutions of D at x; M_x = the diagram with the pattern M at x.)
 WHERE IT STOPS.  The coloured-state complex is far bigger than the hexagon (for instance (s_A, labels 1) lies outside), exactly as the
 Kauffman-state complex of an alternating knot is wider than one diagonal.  What is missing is the analogue of Lee's thinness theorem:
     CONJECTURE H (coloured thinness).  For K alternating, N(T_K) is supported in g_A + G Delta_1 + B Delta_2, i.e. the functionals
     a+b = 2q - 3h and a+2b = (3q - 4h)/2 take values in [-B, G] on N(T_K), as h - q/2 does.
 Expected proof: a spanning-tree (activity) retraction of the coloured-state complex in which tree edges carry {A^2, M_1, B^2} and cotree edges
 {A^2, M_3, B^2}; or an induction over crossings with the three-state sequence (iv), in the way quasi-alternating thinness is proved, with
 the invariants (B,G) playing the role of the signature.  Neither is done.
 Observation for that proof [DATA, 3_1 and 4_1]: on each l-line the tensor positions (alpha,beta) = (k_y,k_x) (k = height in Kh~(K)) that fall
 outside the hexagon appear reflected in its walls alpha - beta = G and alpha - beta = -B (e.g. 4_1, total height 4: (4,0),(0,4) -> (2,2)).
 I could not make this into a rule valid for T(2,5).

4.4 Beyond alternating knots: the double of 8_19 = T(3,4)  [DATA, new, kht/examples/dbl/k819; Kh~(8_19) = (0,6),(2,10),(3,12),(4,12),(5,16)]
      b= 1   . 1 2 1 . . . . . . . . . . .
      b= 0   1*1 2 2 1 1 1 . . . . . . . .
      b=-1   . . . 1 2 2 3 1 . . . . . . .
      b=-2   . . . . 1 1 2 2 . 1 1 . . . .
      b=-3   . . . . . . . 1 . 1 2 1 . . .
      b=-4   . . . . . . . . . . 1 1 . 1 .
      b=-5   . . . . . . . . . . . . . 1 1
      b=-6   . . . . . . . . . . . . . . 1          (a from 0 to 14; * = rho)
 41 generators = arc of 9 + 8 squares.  The arc is rho -D^2-> . <-P- . -D-> . <-P- . -D^2-> . <-P- . -D-> . <-P- . : a staircase with D^2 steps
 (Kh~(8_19) has an H^2-torsion summand); slope of the rational component k = 16.  Top and bottom q-degree are one-dimensional (END, NP hold).
 Hull vertices (0,0),(4,-2),(14,-6),(14,-5),(13,-4),(10,-2),(6,0),(3,1),(1,1); edge directions (1,0),(0,1),(1,-1),(2,-1) and ALSO
 (3,-2), (1,1), (3,-1) and (5,-2).   (3,-1) is the l-preserving direction (2,2): the two generators (3,1), (6,0) share the extreme l-degree,
 where Kh~(x)Kh~ has only one; (5,-2) is the direction of the third Batson-Seed differential.  So the strict polygon law (four directions)
 is a property of thin K (collapse of Theorem A); for non-thin K the hull acquires the directions of the higher splitting differentials, but
 none of them is the cancelling direction (4,-1).   [The double of 8_20 did not finish in 590 s.]
 Validation of the run [PROVED by hand]: chi(N) = t^-10 + t^-7 + t^-4 - t^-3 - 1 - t^3 + t^4 - t^6 + t^7, which is a unit times
 (t^21 - t^14 - t^12 + t^7 + t^2 - t)/(t^3 - 1) = t^18 + t^15 + t^12 - t^11 - t^8 - t^5 + t^4 - t^2 + t, the 3-dimensional coloured Jones polynomial of
 T(3,4) from Morton's torus-knot formula (recalled).


---------------------------------------------------------------------------------------------------------------------------
## 5. Habiro's expansion lifted to N(T_K); closed formulas (task 2, first half)

Notation: [v] := 1 + h^i q^j for a bidegree v = (i,j) ("domino of type v"); a product of dominoes is centred when stated so.  y := the l-grading
variable; D, P have l-degree y, y^3; Lambda := (2,2) = P - 3D has l-degree 1.

5.1 The 1-coloured picture [classical; DATA on the 21 knots].  For thin K, Kh~(K) = F g_0 + D-dominoes (BN~(K) = F[H] + H-torsion).  If sigma = 0,
    Kh~(K) = 1 + A_1 C,   C = h^-2 q^-4 [(1,2)][(3,6)],   A_1 a positive Laurent polynomial in (h,q) with Euler characteristic a_1(K)
    (this is V - 1 = a_1 {3}{1}: the two "cancelling" directions (1,2), (3,6) of reduced Khovanov homology).
5.2 The 2-coloured blocks.  B_1 := h^-4 q^-6 [(1,2)][(5,8)][(2,2)]  (two squares, offset Lambda; 8 generators; Euler characteristic X_1 = {4}{2}, four terms cancel);
    B_2 := h^-8 q^-12 [(1,2)][(3,4)][(5,8)][(7,10)]  (four squares at 0, P-2D, 2P-3D, 3P-5D; 16 generators; Euler characteristic X_1 X_2 = {1}{2}{4}{5}:
    the exponents 1,2,4,5 of t carry homological degrees 1,3,5,7).
    In the l-grading  B_1 = 2C  and  B_2 = C^2.  So Habiro's three terms 1, a_1 X_1, a_2 X_1 X_2 are the Euler characteristics of the three parts
        F (x) F,      F (x) A_1C + A_1C (x) F,      A_1C (x) A_1C
    of the tensor square Kh~(K) (x) Kh~(K) of Theorem A, with the q-grading deformed: the second copy of C is moved by Lambda, the square D x (3,6)
    becomes the square D x P (P = (3,6) + Lambda), C (x) C becomes B_2, and A_1 (x) A_1 becomes a deformed A_2 with chi(A_2) = a_2.
    THE LIFT [DATA: exact for twist knots; l-graded for all 21; CONJECTURED as a filtration in general]:
        P(N(T_K)) = 1 + A_1 B_1 + A_2 B_2      (sigma = 0),
    A_1 from Kh~(K), A_2 positive with dim A_2 = (dim A_1)^2 = ((det-1)/4)^2, so that det^2 = 1 + 8 dim A_1 + 16 dim A_2.
    It holds on the nose for 4_1, 6_1, 8_1, 10_1 and mirrors (py/habiro_lift.py).  For 6_3 (k13_8) it holds only l-graded: after removing A_1 B_1 the
    remaining 36 squares still pair up by (7,10) but not by (3,4) (the quotient is 18 terms with l-polynomial (1+y)(1+y+y^2)^2).  For sigma != 0
    (torus knots) Habiro's a_1, a_2 have many more terms than N has squares (|a_1| = n(n+1)/2, |a_2| = 5 C(n+2,4) + C(n+1,2) against n^2 squares for
    T(2,2n+1)), so the lift is a spectral sequence, not a decomposition, and the staircase replaces the summand F.
5.3 CLOSED FORMULAS [DATA, checked by py/families.py against all available cases].
    (T) K = T(2,2n+1), n = 1..6:   N(T_K) = staircase { (i,-i), (i+1,-i) : 0 <= i < 2n } u { (2n,-2n) }  (rho = (0,0), bottom generator g_A = (2n,-2n))
        together with the n^2 squares with lower left corners (m - 3s, -m + s),   1 <= m <= 2n-1,  1 <= s <= min(m, 2n-m).
        In words: the tensor square of the staircase of length 2n+1, with the square on the m-th antidiagonal number s moved by s Lambda.
    (W) K = twist knot K_p = two-bridge (4p+1)/2  (4_1, 6_1, 8_1, 10_1), p = 1..4:   N(T_K) = { rho } u squares with lower left corners
            (2s+1, -1), (2s-2, 0)                                              0 <= s < p                       [A_1 B_1]
            (2(s+s') - 3c + 2, c - 2) + { (0,0), (-2,1), (-3,2), (-5,3) }      0 <= s,s' < p,  c = 2 min(s,s') + [s > s']      [A_2 B_2]
        i.e. A_1 = sum_s (h^2q^4)^s,  A_2 = sum_{s,s'} (h^2q^4)^(s+s') (h^2q^2)^(2 min(s,s') + [s>s']).  Mirror images: (a,b) -> (-a,-b).
        Euler characteristic: a_1 = sum t^{2s}, a_2 = sum t^{2(s+s') + 2min(s,s') + [s>s']} (agrees with the a_2 extracted from the data).
    For a general two-bridge knot I have no closed formula for the multiset; what holds for all 21 is: (a) the l-marginal (tensor square), (b) the
    hull (hexagon 0.3/4.1), (c) the Euler characteristic (Habiro).  N(T_K) cannot be a function of Kh~(K) alone, since J_3 is not a function of V.
5.4 [DATA, py/pi_coh.py] Cancelling pairs of squares (same q, adjacent h: the B0 offset) are everywhere inside doubles: 4 pairs in 6_1, 13 in 8_1, 25 in
    10_1; they occur inside A_2 B_2 (e.g. the squares (h^2q^4)(h^7q^10) and (h^10 q^14)).  Only torus knots T(2,2n+1), 4_1 and 3_1 have none.

---------------------------------------------------------------------------------------------------------------------------
## 6. The edge directions (task 3)

All vectors in (h,q), with lattice coordinates in brackets.  [PROVED] = the stated identification; the hull statement itself is DATA (4.1).
   D = (1,2) [(1,0)]         the thin direction of Kh~(K); Lee/Bar-Natan arrow d_D; bidegree of the first splitting differential (Thm A, k = 1);
                             step A^2 -> M_1 (and M_3 -> B^2) of a cabled crossing.  Edges: the two extreme delta-levels (Prop. 2(d)).
   Lambda = (2,2) [(-3,1)]   = P - 3D.  The only primitive lattice direction preserving l = h - q; step M_1 -> M_3; offset of the two squares in the
                             Habiro block B_1; the "level" shift between N(T_K) and the tensor square.  Not a hull edge when Theorem A collapses and
                             the extreme l-degrees of Kh~ (x) Kh~ are one-dimensional (the 21 data knots); it IS a hull edge for the double of 8_19.
   P - 2D = (3,4) [(-2,1)]   step A^2 -> M_3 (and M_1 -> B^2); second splitting differential (k = 2); Szabo-type k = 3.  Edges g_A W_2 and W_1 g_B.
   P - D = (4,6) [(-1,1)]    step A^2 -> B^2 of a cabled crossing (four smoothing changes, two circles lost); g_B - g_A = c (4,6) for alternating K
                             [PROVED, Thm B].  Edges from the two cut corners to W_1 and W_2; also the staircase direction.
   P = (5,8) [(0,1)]         = (3,6) + Lambda: the second cancelling direction (3,6) of Kh~(K) moved up one level.  Hull edges only at the two cut corners.
   (2k-1, 2k) [(4-3k, k-1)]  splitting differentials of Theorem A; k = 3, (5,6), is a hull edge of the double of 8_19 (non-collapse).
   (1,0) [(-4,1)]            the Khovanov differential (k = 0 of the same family, k = 1 of Szabo's (k,2k-2)); the direction a cancellation in J at an
                             extreme needs.  It is excluded as a hull edge as soon as the hull is generated from g_A by vectors on which q is positive.
 Summary of the explanation.  For a double the hull is (for thin K, data) g_A + G conv{0, D, P-D} + B conv{0, P-2D, P-D}: the Minkowski sum over the
 crossings of K of the triangles of bidegrees of the three projected states A^2, M, B^2 of a cabled crossing, with M in its low copy on G crossings
 and in its high copy on B crossings.  The bidegrees of the maps in the cabling picture are therefore: A^2 -> M: (1,2) or (3,4); M -> B^2: (3,4) or
 (1,2); A^2 -> B^2: (4,6); M_1 -> M_3: (2,2); and the empty cable enters only through turnback states, which vanish after projecting (4.3 (iv)).
 Reformulation of TILT [PROVED, arithmetic]: with M_b the largest a on level b, "M_b >= M_{b-1} - 3" says that a + 3b = -l at the q-extreme generator
 of each delta-level is monotone in the level, and NP only needs "> -4".  So the step bound 3 of TILT is the l-preserving direction Lambda and the
 forbidden step 4 is the Khovanov differential.
 DOUBLE EXTREMALITY [DATA: 278 of 278 distinct tangles in all data files, py/corner.py, and the double of 8_19]: every generator of top q-degree has
 minimal delta and minimal l = h - q among all generators of N(T); every generator of bottom q-degree has maximal delta and maximal l.
 It implies NP [PROVED: at fixed q, minimal delta means maximal h and minimal l means minimal h] and is implied by TILT.  For doubles of
 alternating knots for which Theorem A collapses it is PROVED: g_A, g_B exist and are unique in their q-degrees (Thm B), they are c delta-levels
 apart and N has at most c+1 levels (Prop. 2(d)), and they are 2c apart in l, which is the whole l-range of Kh~ (x) Kh~.  It is stated in the two gradings that the two known structures respect: delta (the Lee direction) and l (the
 internal grading of the splitting deformation, l = #x - #1 up to a constant: it does not see the cube).

---------------------------------------------------------------------------------------------------------------------------
## 7. The formal object B0 for a double (task 4)

7.1 [PROVED from Habiro's expansion (recalled) by algebra]  T_K flat  <=>  J_3(K) = 1  <=>  a_1 = -a_2 X_2  <=>
        V_K = 1 - a_2 t^-5 (1-t)^2 (1-t^3)(1-t^5),      a_2 = a_2(K) in Z[t, 1/t].
    So a flat double comes in two flavours: (alpha) V_K = 1 and a_2 = 0 (a counterexample to T whose double is flat too);
    (beta) V_K != 1 of this special form.  In case (beta): V_K(i) = 1 + 4 a_2(i), and V_K(i) = (-1)^Arf (Murakami, recalled) forces a_2(i) = 0, so
    (1 + t^2) | a_2 and Arf(K) = 0; det(K) = |1 + 16 a_2(-1)|.  In particular a_2 cannot be a monomial: the simplest algebraic solution of
    J_3 = 1 with V != 1 is already excluded by the Arf invariant.
7.2 What N(T_K) would be: F + squares in cancelling pairs (Pi = 0), with dim N >= (dim Kh~ K)^2 >= 9 (Theorem A and Kronheimer-Mrowka).
    The literal B0 = a(0) + S + hS has 9 generators; rk Kh~_2 = 9 only for the trefoil (Robinson, Thm 2.1, read now), whose J_3 != 1.  So
    [PROVED by citation] B0 itself is not the invariant of any doubled tangle; the first candidates have at least 25 generators (six squares
    in three cancelling pairs) and would need dim Kh~(K) <= 5.  By Theorem A, (ii), such an N must also satisfy
    P_N(x) - x^c W_K(x)^2 = (1+x) R(x), R >= 0, where P_N(x) - 1 is divisible by (1+x)^3 (each cancelling pair contributes
    x^l (1+1/x)(1+1/x^3)(1 + x^m), m odd).
7.3 Which property of actual coloured homology excludes it.  The one that is proved: Theorem B.  If K is adequate, Kh~_2(K) has a single
    generator in its top and in its bottom q-degree, so J_3 has extreme coefficients +-1 and span 3c - 2g_T > 0.  If K is semiadequate one
    extreme is a single generator, and J_3 != 1 by Stoimenow.  So a formal flat double must come from a knot that is not semiadequate.
    The property that would exclude it in general:
        (NP for doubles)  the top q-degree of Kh~_2(K) is supported in one homological degree (equivalently: the generator(s) of top q-degree
        have minimal delta and minimal l = h - q among all generators), and the same at the bottom.
    For thin K this follows from Conjecture H; for K = 8_19 it holds by computation although the hexagon fails.  What a proof must control is
    the extreme degree when the all-B state is not adequate, i.e. the first non-vanishing layer of the coloured-state complex; this is the
    homological form of the question "what is the leading coefficient of J_3 of a non-adequate knot", for which no theory exists (1.2).
    Theorem A does not help here: it constrains the l-grading, and cancellation at an extreme happens inside one q-degree across l.

## 8. A hidden involution of N(T_K)   [DATA, found last; exact on all 21 two-bridge doubles; py/iota.py]

    iota(a,b) = (-a, a+b)   (about rho):   fixes P = (5,8), exchanges D = (1,2) with P - D = (4,6), negates P - 2D = (3,4), sends Lambda = (2,2) to -(7,10).
    In (h,q):  iota(h,q) = (-11h + 15q/2, -16h + 11q).   In the hexagon coordinates u = b, v = a+b it is the transposition u <-> v.
    Equivalently: the generating function P_N(x,y) = sum over N of x^a y^b satisfies P_N(x,y) = P_N(y/x, y)  (hq^2 <-> h^4q^6 with h^5q^8 fixed).
 [DATA] iota(N(T_K)) = N(T_K) as multisets for every one of the 21 doubles (it is not the mirror symmetry: it holds for each chirality separately).
 It is NOT a general property of N(T): among the other data it holds (up to translation) for 4 of 132 table inversions, 0 of 112 two-bridge
 quotients, the Alexander-polynomial-one example, and a few sums; and it FAILS for the double of 8_19.  So it is a property of doubles of thin knots.
 Consequences [PROVED from the symmetry, for the 21 knots]:
  - iota exchanges the vertices g_B <-> W_1, g_A <-> W_2 and the two cut corners; it exchanges the delta-strip (b in [-B,G]) with the strip for
    a + b = 2q - 3h, and fixes a + 2b = (3q - 4h)/2.  So, GIVEN iota, Conjecture H reduces to the single strip -B <= (3q - 4h)/2 <= G.
  - a second tensor-square grading: the multiset { 2a + 3b } = { (7q - 10h)/2 } on N(T_K) is again the multiset of total heights of Kh~(K) (x) Kh~(K)
    (image of the l-grading); the image of the splitting differentials would have bidegrees (4,6), (3,4), (10,14), ... (step (7,10)).
  - a third cancelling domino structure: N(T_K) minus the point iota(x_0) is a union of pairs differing by P - D = (4,6) (image of the D-dominoes),
    besides the D-dominoes (N minus x_0) and the P-dominoes (N minus rho, preserved by iota).  For the trefoil: (2,-2)-(1,-1), (2,-1)-(1,0),
    (0,0)-(-1,1), (-1,0)-(-2,1), leftover (-2,0) = W_2.
  - Euler characteristic form: J_3(t) = sum over N of (-1)^b t^{3a+4b}   (a "delta-signed" count), besides J_3 = sum (-1)^{a+b} t^{a+4b}.
  - iota does not preserve squares, nor the Habiro blocks B_1, B_2 (it mixes them): so it is not visible in the arrow structure of BN~(T_K).
 Origin [CONJECTURED]: the sl_2 shadow of the self-symmetry of symmetric-coloured HOMFLY-PT homology (the coloured generalisation of the q <-> 1/q
 symmetry; Gorsky-Gukov-Stosic, recalled).  For thin K the Sym^2-coloured HOMFLY-PT homology should specialise to Kh~_2(K) without cancellation,
 and the two-dimensional lattice of N(T_K) has room for the symmetry to act, whereas on the one-dimensional thin Kh~(K) it is invisible.  This fits
 the failure for 8_19 (not thin).  I did not verify it against a published superpolynomial.

## SUMMARY

PROVED
 1. N(T) = H(X_1X_2 CKh(T(n)), d_Kh) for every n (two basepoints on the closing arcs); for T_K this is the doubly pointed homology of the 2-cable
    with any framing (0.1).
 2. THEOREM A (pointed link-splitting spectral sequence, from Batson-Seed).  N(T) ==> Kh~(t_1^) (x) Kh~(t_2^), t_i^ the closures of the two strands;
    differentials of bidegree (1-2k, -2k), abutment graded by l = h - q.  For doubles: N(T_K) ==> Kh~(K) (x) Kh~(K), dim Kh~_2(K) >= (dim Kh~ K)^2,
    l-graded Morse inequalities.  (Sym^2 / sl_2 counterpart of "exponential growth"; needs no Floer theory.)
 3. THEOREM B.  If the closure diagram is A- (B-) adequate with the marked circles distinct in the extreme state, the bottom (top) q-degree of N(T) is
    a single generator.  Hence END and NP for the doubles of all adequate (in particular alternating) knots, one side for semiadequate knots; the two
    extreme generators of an alternating double differ by c(P - D) = c(4,6).  Same for all colours n.
 4. Under collapse of Theorem A and thinness of K: N(T_K) has at most c+1 delta-levels and its l-projection is the tensor square.  If moreover K is
    alternating: exactly c+1 levels, and DOUBLE EXTREMALITY holds (the top generator has minimal delta and minimal l), which implies NP.
 5. Local structure of a cabled crossing: states A^2, M{hq}, M{h^3q^3}, B^2{h^4q^4} and turnback states; bidegree steps A^2->M_1 = D, A^2->M_3 = P-2D,
    A^2->B^2 = P-D, M_1->M_3 = Lambda = (2,2); a turnback inserted at a point of the band gives N = 0; without projectors the surviving turnback states
    are loop-removal terms N(T_K').
 6. Flat double <=> J_3 = 1 <=> V = 1 - a_2 t^-5 (1-t)^2(1-t^3)(1-t^5); then (1+t^2) | a_2 and Arf = 0.  B0 itself is not the homology of any double
    (Theorem A + Kronheimer-Mrowka + Robinson/Baldwin-Sivek).  TILT's step bound 3 is the l-preserving direction.
CITED (read now unless marked)
 Stoimenow Prop. 4.3: untwisted Whitehead doubles of semiadequate knots have non-trivial Jones polynomial; verified for all knots up to 16 crossings.
 So Lemma Q holds for the swap inversion on K # K^r with K semiadequate.  "J_3 detects the unknot" is otherwise OPEN (only all colours together:
 Andersen).  Grigsby-Wehrli Thm 1.2, Cor. 1.3; Robinson Thm 2.1; Hedden; Hedden-Watson; Batson-Seed Thm 1.1, Props 2.2, 2.3, 3.2, 6.3, Cor. 3.4;
 Rozansky (tail homology, abstract); Wedrich (abstract).  Recalled only: Habiro, Masbaum, Armond, Garoufalidis-Le, Dasbach-Lin, C. Lee, Cooper-Krushkal,
 Hogancamp, Beliakova-Wehrli, Grigsby-Licata-Wehrli, Gukov-Stosic, GGS, Dowlin, Murakami.
DATA (no proof)
 - Theorem A collapses for all 21 two-bridge doubles (N(T_K) = Kh~(K)^{(x)2} as l-graded spaces); it does NOT collapse for the double of 8_19
   (41 generators against 25; new computation; this is also the first double with 1 + 2m > rk HFK^).
 - HEXAGON LAW (21/21, exact): hull N(T_K) = g_A + G conv{0,D,P-D} + B conv{0,P-2D,P-D} minus two unit corners, B = s - h_min, G = h_max - s.
   It fails for the double of 8_19, whose hull has the extra directions (3,-1) (l-preserving), (5,-2) (third splitting differential), (3,-2), (1,1);
   END and NP still hold there.
 - Closed formulas for N(T_K): T(2,2n+1), n <= 6, and twist knots K_p, p <= 4 (5.3).  Habiro lift P(N) = 1 + A_1B_1 + A_2B_2 exact for twist knots.
 - DOUBLE EXTREMALITY in 278/278 tangles of all data files; one-dimensional extreme q-degrees in 277/279.
 - HIDDEN INVOLUTION iota(a,b) = (-a, a+b) about rho (D <-> P-D, P fixed): exact symmetry of N(T_K) for all 21 two-bridge doubles, false for the
   double of 8_19 and for generic quotient tangles (section 8).
CONJECTURED
 - CONJECTURE H (coloured thinness): for alternating K, N(T_K) lies in the hexagon, i.e. 2q - 3h and (3q - 4h)/2 are confined to [-B, G] like h - q/2.
 - Theorem A collapses for all alternating K (rk Kh~_2(K) = det(K)^2; cf. Robinson's remark).
 - DOUBLE EXTREMALITY for every strong inversion (stronger than NP, weaker than TILT).
 - The Habiro lift as a filtration of N(T_K) with graded pieces F, A_1 (x) B_1, a deformation of A_1 (x) A_1 (x) B_2.
 - The involution iota for doubles of all thin knots, as the sl_2 shadow of the self-symmetry of Sym^2-coloured HOMFLY-PT homology.
THE NAMED GAP
 Coloured thinness.  Between the proved facts (the two extreme generators, the delta-strip, the l-projection) and the hexagon stand the two oblique
 strips: a bound for 2q - 3h and 3q - 4h on N(T_K).  (If the involution of section 8 were proved, the first would follow from the delta-strip and
 only the strip for 3q - 4h would remain.)  At chain level the coloured-state complex violates them, exactly as Kauffman states violate
 thinness; a spanning-tree retraction (tree edges {A^2, M_1, B^2}, cotree edges {A^2, M_3, B^2}) or an induction over crossings is missing.
 Beyond thin K nothing is proved: for a non-semiadequate K the extreme degree of Kh~_2 is not at a corner of the cube, and no statement about it exists.
 For a general strong inversion (unknotted strands) Theorem A gives only a third cancelling structure and does not exclude B0.
MOST PROMISING NEXT STEP
 Prove DOUBLE EXTREMALITY, in its two halves, each inside the structure that respects the grading involved:
   (l)     the top q-degree of N(T) has minimal l = h - q.   l is the internal grading of the splitting complex (X_1X_2 C, d_0 + d_1) of Theorem A,
           whose l-graded homology is known (Kh~(t_1^) (x) Kh~(t_2^)); the statement is that the classes of extreme l sit in extreme filtration.
   (delta) the top q-degree of N(T) has minimal delta.   delta is the internal grading of the Lee / Bar-Natan deformation (the D-arrows), whose
           homology is one-dimensional.
 Together they give NP, hence END and Lemma Q, and they are the form of the outline law that survives outside thin knots (it holds for the double
 of 8_19, where the hexagon and the four-direction polygon law fail).  For doubles of alternating knots with collapse both halves are proved here.  The
 first concrete task is the double of 8_19: Theorem A does not collapse there (eight cancelling pairs, R = 1 + 2x + 2x^3 + 2x^4 + x^6), yet both
 halves hold; determine which splitting differentials occur and why none reaches the extreme q-degrees.  That is the smallest laboratory for a proof.
 Second: identify the involution iota of section 8 (expected: self-symmetry of Sym^2-coloured HOMFLY-PT homology); with it, coloured thinness
 (Conjecture H) reduces to the single strip for 3q - 4h, to be attacked by a spanning-tree retraction of the coloured-state complex.
 Cheap data wanted: doubles of 8_20, 8_21 (thin, not alternating) and of an alternating non-two-bridge knot (8_5, 8_16) with a longer time limit,
 to see whether collapse, the hexagon and iota follow thinness or alternation; and the list of table inversions that have a b-adequate tangle
 diagram, to which Theorem B applies verbatim.
