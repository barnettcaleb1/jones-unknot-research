# REPORT: lens TWOBRIDGE (induction on rational and arborescent pieces)

STATUS (16 Nov 2026): COMPLETE for this session. Sections 1-8 + SUMMARY at the end. Appended as work proceeded; main results: Theorems A, B, D (proved), junction formula 8.2 (data, 145 tangles).
Marks: PROVED / CITED (source, statement number, read-now or recalled) / DATA / CONJECTURED.

## 1. Topology of the quotient tangle: correction of the premise, and the right structure

Notation: (K,h) strongly invertible, theta-graph Theta = A u k in S^3/h = S^3 (A = image of the axis, an unknot; k = image
of K, an arc with its ends on A). The ends of k cut A into two half-axes A_u, A_l. T = (S^3 - N(k), A - N(k)).
CONSTITUENT KNOTS: K_u := k u A_u, K_l := k u A_l (the third cycle A is the unknot).

1.1 [PROVED] T is a 2-string STRING LINK. Its two strands are A_u and A_l; each runs from the disc D_1 (boundary of N(k) near
one end of k) to the disc D_2 (near the other end). The boundary sphere is D_1 u (annulus around k) u D_2, the core of the
annulus has slope infinity (unknot filling), and b = Q_0 is the filling by a band along k. Equivariant connected sum =
composition of string links. Consequently
      T(0) = K_u u K_l   (the two edges of the band along k; a 2-component link with lk fixed by the Seifert framing),
and N(T) = top-weight annular Khovanov homology of K_u u K_l with respect to the meridian circle B of the band.
(Proof: the 0-filling replaces N(k) by two parallel copies of k; each strand of T closes up with one copy.)

1.2 [PROVED] The task statement "the quotient tangle of a two-bridge knot is a sum of two rational tangles" is true only for
torus knots T(2,n). Reason: a disc in the tangle ball meeting T in two points lifts to an annulus in the knot exterior; a sum
of two non-integral rational tangles has Seifert fibred double cover (base a disc, two cone points) = a torus knot exterior.
Two-bridge knots other than T(2,n) are hyperbolic, so their quotient tangles are not sums, and not arborescent either
(arborescent tangle => graph manifold cover). What IS true:

1.3 [PROVED] (structure of two-bridge quotients). Write K = K(p/q) as the 4-plat sigma_2^{a_1} sigma_1^{2 b_1} sigma_2^{a_2}
... (Conway C(a_1, 2b_1, a_2, 2b_2, ...); every p/q with q even has such an expansion; kht++ half-diagram
s.l1.y0^{a_1}.x1^{b_1}.y0^{a_2}.x1^{b_2}...u2, signs by y0<->x0, x1<->y1). The three involutions of the four-punctured
sphere extend over both rational tangles of the 2-bridge decomposition; exactly one of them meets K inside the first ball
(inversion 1), one inside the second ball (inversion 2), the third is the cyclic period. For an inversion:
   (a) Theta = "H-tangle" (axis with two legs) u rational tangle (axis arc alpha', quotient arc kappa'); after pushing
       kappa' into the splitting sphere, k = an arc of slope r on the sphere punctured at c_1, c_2 (axis) and m_1, m_2 (legs).
   (b) T = the rational 3-braid picture on (A, k_1, k_2) with the two k-strands DOUBLED into bands and capped by nested caps:
       6 boundary points (c_1, m_1^-, m_1^+, m_2^-, m_2^+, c_2), inside a trivial 3-string tangle (alpha', kappa'_1,
       kappa'_2) twisted by the braid  w = prod_i  Y^{a_i} X^{b_i},
           Y = full twist of the axis strand around the band (m_1^-, m_1^+)   [kht++ y0.y1.y1.y0],
           X = half twist of the two bands                                     [kht++ x2.x1.x3.x2],
       and one closing arc (c_1, m_1^-). Free ends: m_1^+, m_2^-, m_2^+, c_2.  (This is exactly Tangle::quotient in kht++.)
   (c) Constituents: K_l = unknot;  K_u = plat closure of the 3-braid sigma_1^{2a_1} sigma_2^{b_1} sigma_1^{2a_2} ... =
       the two-bridge knot C(2a_1, b_1, 2a_2, b_2, ...) = K(p/(q/2))   (numerator p unchanged: [2c_1, c_2/2, 2c_3, ...] = 2 [c_1, c_2, ...]).
   So the strand A_l of the string link is unknotted and "straight", and T = one strand (A_u) wound around it;
   T(0) = K(p/(q/2)) u (unknot).

1.4 [DATA, 132 inversions of the table; script scripts/table_const.py, output table_const.txt]
   det K = det K_u * det K_l in all 132 cases (classical for Z/2 x Z/2 covers of a theta-graph; I did not look up a source).
   dim N(T) = det K_u * det K_l in all cases where everything is thin; the three exceptions are exactly
        8_19:    dim N = 5,  rank HFK^(K) = 5,  (K_u, K_l) = (U, 3_1):        rank HFK^(K_u) rank HFK^(K_l) = 3
        9_42:    dim N = 9,  rank HFK^(K) = 9,  (K_u, K_l) = (5_2, U):        7
        9_46-2:  dim N = 15, rank HFK^(K) = 9,  (K_u, K_l) = (T(3,4), 3_1):   15      <-- explains the 15
   So in the data  dim N(T) = max( rank HFK^(K), rank HFK^(K_u) rank HFK^(K_l) ).  The first bound is Theorem S.
   CONJECTURED (S'): dim N(T) >= rank HFK^(K_u # K_l) in general (sharpened to reduced Khovanov ranks, with a proof route, in 6.4).
   (Ranks of the constituents were taken as determinants, except for the rows listed, where Kh~ was computed.)
   Length of the zigzag (thin cases checked by hand on ~15 entries): 2l + 1 = |sigma(K_u) + sigma(K_l)| + 1.
   The naive guess "N = CFK(K_u # K_l) with Alexander grading b - a" is FALSE (script scripts/table_alex.py): the shapes
   (staircase length, number of squares) agree in thin cases, the positions of the squares do not.

## 2. Closed formula for N(T) of two-bridge quotients, positive words

Lattice coordinates as in BRIEF2 section 4: generator = rho + a D + b P; P_T(x,y) := sum over N(T) of x^a y^b (positive
integer coefficients; J(T) = P_T(-t, -t^4)). Put u := x/y (the step D - P = (1,-1)).
Word w = Y^{a_1} X^{b_1} ... Y^{a_n} X^{b_n} (Y = axis crossing y0, X = off-axis crossing x1; knot C(a_1, 2b_1, ..., a_n, 2b_n)).

2.1 [DATA, 24 words (19 with one or two blocks, 5 with three), exact agreement of the whole multiset including rho at the origin; scripts/matrix_formula.py]
      P_w(x,y) = (1 0) M_X^{b_n} M_Y^{a_n} ... M_X^{b_1} M_Y^{a_1} (1 0)^T,
      M_Y = [[1, 0], [u, u]],      M_X = [[1, 1+y], [0, x]]          (all a_i, b_i > 0).
   One block:  P_{Y^a X^b} = 1 + u [a]_u (1+y) [b]_x   ([n]_z = 1 + z + ... + z^{n-1}), uniformly in the parity of b.
   Checked: Y^aX^b for a,b <= 4 (11 cases) and 13 two-block words up to determinant 33.
   CONJECTURED for all positive words. (Proof route in section 4.)

2.2 [PROVED] Why a 2 x 2 matrix formula must exist for J. T is an endomorphism of V (x) V and uJ is its eigenvalue on V_2.
   Insert the Jones-Wenzl projector on the band along k: uJ * Delta_2 = Kauffman-Lins evaluation of the theta-graph
   Theta = A u k with A_u, A_l coloured 1 and k coloured 2:
        J(T) = <Theta; (A_u, A_l, k) = (V_1, V_1, V_2)> / (same for the trivial theta-graph).
   So LEMMA Q <=> the (1,1,2)-coloured sl_2 invariant detects the trivial theta-curve among theta-curves with an unknotted
   cycle (the cycle of the two edges coloured 1). (Special case k = long knot, A straight: 3-dimensional coloured Jones.)
   For a two-bridge theta-curve this is a matrix element of the braid group B_3 acting on Hom(V_1, V_1 (x) V_2 (x) V_2), which
   has dimension 2 (intermediate colours 0, 2 for the pair of k-strands). Twist eigenvalue ratios: half twist of (2,2): -A^{-4}
   = -t; full twist of (1,2): A^{-12} = t^{+-3}. These are exactly x -> -t and u = x/y -> t^{-3} at (x,y) = (-t,-t^4).
   So M_X, M_Y are a positive two-variable lift of that representation (the entries 1+y and u lift the 6j-coefficients),
   and N(T_w) categorifies the matrix element.

## 3. THEOREM A and THEOREM B: J for all two-bridge inversions, and non-flatness (Lemma Q for this class)

Words: w = L_1 L_2 ... L_m in the letters Y, X and their inverses y, x (L_1 nearest the cap). Every strong inversion of a
two-bridge knot that preserves the two sides of a bridge sphere is T_w for some w (1.3). SCOPE (correction found while
writing): these are ALL strong inversions unless q^2 = 1 mod p, q != +-1 (Sakuma Prop. 3.6 Case (2), as quoted in the kht++
source; not read in the original): then the two side-preserving inversions are conjugate and the second class exchanges
the two sides; it has a 4-strand half-diagram and two knotted constituents (7_4-2: (5_1, 3_1); 7_7-2: (3_1, 5_2); 9_23-2:
(6_1, 4_1)) and is NOT covered below. "Two-bridge inversion" means side-preserving from here on. T_w (Seifert framed) depends only on w modulo the centre of B_3 (the full twist
Delta^2 slides to the cap and only changes the framing of the band), modulo X on the left (a band half twist under the band
cap is a framing change) and Y on the right (twisting the end of k around the axis next to its end point is trivial).

THEOREM A [PROVED; conventions fixed by the kht++ trefoil; checked against kht++ on 130 tangles: 24 positive and 16 mixed own
   runs (scripts/jcheck.py) and all 90 table entries with a two-letter half-diagram, 80 of them mixed (scripts/table_thmA.py)].
   J(T_w) = unit * (1 0) rho(L_m) ... rho(L_1) (1 0)^T,     rho(Y) = [[1,0],[t^-3, t^-3]],   rho(X) = [[1, 1-t^4],[0, -t]],
   rho(y) = rho(Y)^-1, rho(x) = rho(X)^-1.   (This is 2.1 at (x,y) = (-t,-t^4).)
 Proof. By 2.2, uJ = phi(w . E_1), where w acts on H = Hom(V_1, V_1 (x) V_2 (x) V_2) (projectors on the two bands), E_1 = (axis
 straight) (x) (band cap), and phi = (close axis with the first band strand, take the coefficient of b).
 (a) dim H = 2: of the five crossingless matchings of {top,0,1,2,3,4} exactly (top 0)(1 4)(2 3) = E_1 and (top 4)(0 1)(2 3)
     survive the projectors on (1,2) and (3,4).
 (b) Removing the projectors does not change the coefficient of b: the correction terms contain a turn-back on a band,
     which passes through every crossing and closes to c. phi(E_1) = 1.
 (c) E_1 is an eigenvector of X (a band half twist under the band cap is a kink in the band), and phi is a left
     eigenvector of Y (the full twist of the axis around the band, followed by joining the axis to a band strand, untwists).
     So in the basis (E_1, F) with phi = (1 0): rho(X) = [[1, xi],[0, lam]], rho(Y) = [[1,0],[eta, mu]] after normalising
     the eigenvalues on E_1 and on phi to 1.
 (d) lam = ratio of the half-twist eigenvalues on the channels V_2, V_0 of V_2 (x) V_2 = -A^{-4} =: -t; mu = ratio of the
     full-twist eigenvalues on the channels V_3, V_1 of V_1 (x) V_2 = A^{+-12} = t^{-+3}  (CITED, recalled: Kauffman-Lins
     twist eigenvalue (-1)^{(a+b-c)/2} A^{[a(a+2)+b(b+2)-c(c+2)]/2}; the relative handedness of X and Y is the alternating one
     and gives mu = t^{-3} in the normalisation where the trefoil s.l1.y0.x1.u2 has J = t^-3 + 1 - t, as kht++ confirms).
 (e) (sigma_1^2 sigma_2)^2 = Delta^2 is central and acts on H by a scalar; with Y = sigma_1^2, x = sigma_2 this says
     rho(Y) rho(X)^-1 has scalar square, i.e. trace 0 (it is not scalar):  1 + xi eta / t - t^-4 = 0, xi eta = t^-3 (1 - t^4).
     Rescaling F gives xi = 1 - t^4, eta = t^-3.                                                                    QED
 Consequences: J = 1 mod (1 - t^4) (the first coordinate changes only through xi); J(T_{Y^a X^b}) = 1 + t^-3 [a]_{t^-3}
 (1 - t^4) [b]_{-t};  mirror: J_{w^-}(t) = J_w(t^-1) (conjugation by diag(1, -t^-3)).

Normal form. Put E := rho(Y)^-1 rho(X) = [[1, 1-t^4],[-1,-1]], E^2 = t^4. The group generated by Y, X modulo the centre is
Z/2 * Z = <e> * <Y>, and every w gives  J_w = unit * F(n_0,...,n_{k-1}),
      F(n_0,...,n_{k-1}) := (1 0) E rho(Y)^{n_{k-1}} E ... E rho(Y)^{n_0} (1 0)^T,     n_1,...,n_{k-1} != 0.
(n_i all positive <=> w is a positive word in X, Y <=> alternating-type transvergent diagram; e.g. the second inversion of
5_2 is Y e Y^-1 e, genuinely mixed.)  T_w is trivial (K = unknot) iff w lies in <X><Y>, iff the sequence is a
"degenerate prefix" (n_0 in {0,-1} followed by the forced continuation), see below.

THEOREM B [PROVED given Theorem A; the automaton checked against direct expansion on 12440 normal forms, the statement
"J monomial <=> determinant 1" on 47988 words; scripts/span_check.py, scripts/jmatrix.py].
   For every side-preserving strong inversion of every non-trivial two-bridge knot (all strong inversions when
   q^2 != 1 mod p, and the unique one of T(2,n)), J(T) is not a unit: T is not flat. More precisely the
   two extreme coefficients of J are +-1 and
        span_t J = sum over the generic E-steps i of c_i,   c_i = 3|n_i| - 2 + 2 [sign(n_i) != sign(n_{i-1})]  (i >= 1),
        c_0 = 3 n_0 + 1 (n_0 >= 1),  3|n_0| - 2 (n_0 <= -2);     every c_i >= 1.
   Positive words: span J = 3A + B, top term (-1)^B t^B, bottom term t^{-3A}  (A = sum a_i, B = sum b_i).
 Proof. Follow v = (v_1, v_2) through the product and put r = v_2/v_1, expanded at t = infinity; deg = degree of the leading
 term, lc = its coefficient.  Y^n: r -> r_n + t^{-3n} r with r_n = t^-3 [n]_{t^-3} (n > 0), -[m]_{t^3} (n = -m < 0); v_1 fixed.
 E: v_1 -> v_1 (1 + (1 - t^4) r),  r -> -(1 + r)/(1 + (1 - t^4) r).
 States of r before an E-step and the effect of the E-step (gain = increase of deg v_1; the lc of v_1 is multiplied by +-1):
    P   = (deg -3, lc 1)        [after Y^n, n > 0]                      gain 1,      then r = (deg -1, lc 1) =: R
    Q_m = (deg 3m-3, lc -1)     [after Y^-m from S_j or from the start] gain 3m+1,   then r = (deg -4, lc 1) =: S_0
                                 (m = 1 from S_j: gain 4, then S_{j+1} = (deg -5-j, lc (-1)^{j+1}))
    U_m = (deg 3m-1, lc 1)      [after Y^-m from R]                     gain 3m+3,   then S_0
    degenerate (exact) states: r = 0 (gain 0, then r = -1), r = -1 (gain 4, then r = 0); they occur only in a prefix
    (X^n or x^n at the start of w) and contribute nothing to the span.
 From R: Y^n (n>0) gives P, Y^-m gives U_m. From S_j: Y^n gives P, Y^-m gives Q_m. In every case the two competing terms
 have different degrees (-3 against -1-3n or -4-j-3n; 3m-3 against 3m-1 or 3m-4-j; 4+deg r against 0 with deg r > -4),
 so NO CANCELLATION occurs, and deg v_1 = sum of gains with leading coefficient +-1.
 Lowest degree: F(n_0, n_1, ..., n_{k-1})(t^-1) = t^{-4k} F(-n_0 - 1, -n_1, ..., -n_{k-1})(t)  (from the mirror conjugation),
 so mindeg F = 4k - (sum of gains of the mirrored sequence). Adding: each generic step contributes
 gain + mirror gain - 4 = c_i >= 1, each degenerate step 0. Hence span >= number of generic steps, which is 0 only for the
 trivial knot.                                                                                                        QED
 Remarks. (1) This proves END at the level of J for the class: the extreme coefficients of J are +-1.
 (2) Lemma Q for two-bridge K concerns the closures T(1/n), which are NOT two-bridge; I do not know this statement in the
     literature (not searched).  (3) The proof uses only that J is a matrix coefficient of a 2-dimensional representation
     of Z/2 * Z with these two explicit matrices: a ping-pong on the leading exponents.

## 4. The categorified statement: where the proof of the closed formula and of NP stops

4.1 [PROVED, algebra] Structure behind the matrices. <Y, X> = Artin group of type B_2 (Y X^-1 Y X^-1 central), realised
   both as <sigma_1^2, sigma_2> in B_3 (quotient picture: axis, k_1, k_2) and as the symmetric 4-braids <sigma_2, sigma_1 sigma_3>
   in B_4 (the transvergent diagram of K: Y = crossing on the axis, X = mirror pair of crossings). rho is the 2-dimensional
   representation of the B_2 Hecke algebra with UNEQUAL parameters (-t for X, t^-3 for Y). M_X = [[1,1+y],[0,x]] and
   M_Y = [[1,0],[u,u]] are graded versions of the twist matrices of the folded A_3 zigzag category: the non-symmetric Cartan
   entries 2 and 1 of B_2 appear as (1+y) and 1 (the object "pair of bands" is the folded pair P_1 + P_3, and (1+y) = its two
   lifts = the two edges of the band = one P-pair = one special component).

4.2 [CONJECTURED (CAT); DATA: 47 words, scripts/hybrid_vs_data.py] Positive lifts of the inverse letters and of e:
       Mt_y = [[1,0],[y/x^4, y/x]],   Mt_x = [[1, x^3(1+y)/y],[0, 1/x]],   EE = [[x^4/y, x^4(1+y)/y],[1,1]]  (lift of -E),
   all specialising correctly at (x,y) = (-t,-t^4). For a word w let P^E_w be the corresponding product of positive matrices
   (row (1 0), column (1 0)^T). Then
       P^E_w = (monomial) * P_{N(T_w)} + (1 + x^4/y) R_w,     R_w >= 0,
   i.e. N(T_w) is the homology of a complex with Poincare polynomial P^E_w and a differential of lattice degree (4,-1) =
   (h,q)-degree (1,0). For positive words in X, Y: R_w = 0 (formula 2.1; now 24 words incl. 3-block ones). The relations
   (M_e)^2 = monomial, M_Y M_e = monomial * M_X hold exactly after cancelling (4,-1)-pairs.
   (CAT) is the statement that the B_2 braid group acts on a 2-object dg category by functors with these Poincare matrices
   and that N(T_w) = Hom(cap object, w . cup object). I did not construct the functors.

4.3 [PROVED from 2.1] Positive words: the Newton polygon and the shape.
   Expanding the product: P_w = sum over sets of "excursions" i_1 <= j_1 < i_2 <= j_2 < ... of products of
       W_{ij} = u [a_i]_u * u^{a_{i+1}+...+a_j} * x^{b_i+...+b_{j-1}} * (1+y) [b_j]_x          (a quantum continuant).
   From this (A = sum a_i, B = sum b_i):
   - Newton polygon of N(T_w) = the pentagon with vertices (0,0), (B,0), (A+B-1, 1-A), (A+B-1, -A), (A,-A);
     edges B*(1,0), (A-1)*(1,-1), 1*(0,1), (B-1)*(1,0), A*(1,-1): only the directions D, P, D-P. All five vertex
     coefficients are 1. (Checked by machine on all words with <= 3 blocks and exponents <= 4, scripts/hull_formula.py.)
   - top of J at the vertex (B,0), bottom at (A,-A): NP holds; span J = 3A + B (agrees with Theorem B).
   - P_w(x,-1) = 1 and P_w(-1,y) = +-y^{-l} with l = sum_i a_i [b_i + ... + b_n odd]: the Euler characteristics of
     H(d_P) = H(d_D) = F, so P_w = Z_l + (1+x)(1+y) Pi_w with Z_l = [l+1]_u + x [l]_u the staircase from rho = (0,0) to
     x_0 = (l,-l). (Pi_w >= 0 in all computed cases; not proved in general.)
   - [DATA, 24 words] slope of the rational component in Seifert framing: k = -4 sum_i b_i [a_1 + ... + a_i odd].
   So, granting 2.1 and the shape law, BN~(T_w) for a positive word is: an arc = staircase with 2l+1 bullet generators and
   a tail of |k| circle generators, plus one square for every monomial of Pi_w = (P_w - Z_l)/((1+x)(1+y)).
   One block: Pi = u [a]_u [b/2]_{x^2} (b even), x u [a]_u [(b-1)/2]_{x^2} (b odd).

4.4 [PROVED given (CAT); the combinatorial part checked on 7775 normal forms, scripts/hybrid.py] THEOREM C (conditional NP).
   In the calculus with letters Y^n, y^m, EE and x (for interior exponents n_i = -1), no two terms tie in t-degree at any
   step of the leading-exponent automaton of Theorem B, and now all coefficients are positive. Hence the top t-degree part
   of the positive polynomial is ONE monomial with coefficient 1 (same at the bottom, by the mirror). If (CAT) holds, N(T)
   has exactly one generator in its top and one in its bottom quantum degree: NP for all two-bridge inversions.
   WHERE THE PROOF STOPS: (CAT). Everything else is proved. Route for positive words: (CAT) gives dim N <= det K, Theorem S
   (Grigsby-Wehrli + Ozsvath-Szabo for alternating knots) gives dim N >= det K, so the complex has zero differential and
   2.1 follows.

4.5 [PROVED] Mixed words really differ. The hull direction (2,-1) = 2D - P occurs exactly for mixed normal forms (8 of the 47
   computed words; never for one-signed ones). Example: Y^a x^b has P = 1 + (1+y)([a]_u [b]_{1/x} - 1): a thickened
   parallelogram with one corner (the generator y) removed by the cancellation of the pair {1, x^4/y}; the cut corner
   between a D-edge and a (D-P)-edge is the edge 2D - P. So "P - 2D" in the polygon law = a corner cut by one cancellation.

   Addendum to 4.3 [machine check of the formula, 4368 positive words with <= 3 blocks and exponents <= 4, scripts/check43.py]:
   hull = pentagon with all vertex coefficients 1; P_w(x,-1) = 1; P_w(-1,y) = (-1)^l y^{-l} with the stated l;
   Pi_w = (P_w - Z_l)/((1+x)(1+y)) has non-negative coefficients. k-formula: 33 kht++ words, no mismatch.

## 5. Geometric picture behind the formula (interpretation; PROVED where marked)

5.1 [PROVED] T as a wall curve. For a two-bridge inversion the string link T in D x I is: A_l = the core 0 x I; A_u =
   (radial segment at the bottom) u (an embedded arc eta on the wall dD x I, of slope r in the sphere with the four marked
   points c_1, c_2 = ends of eta, and the two lids) u (radial segment at the top). Closing up, K_u = k u A_u is presented
   as a (1,1)-knot on the torus dN(B), and A_l-closed and B (the meridian of the band) are the two cores of that genus one
   splitting. So  T(0) u B = (1,1)-knot K_u together with the two core circles of its Heegaard torus,
   and N(T) = annular Khovanov homology of (K_u u core) with respect to the other core, top weight.
5.2 [PROVED] N(T) does not depend on the framing of T (up to an overall shift): the twist that changes the framing is
   supported away from A_b (this is BRIEF2 2(b): N(T) = AKh(T sigma^n; 2) for every n). So any convenient framing may be used.
5.3 [CONJECTURED, consistent with all data] Arc model. On the sphere with marked points c_1, c_2 (axis, order two) and
   m_1, m_2 (ends of k): N(T_w) has a basis  {rho} u {z, y z : z an interior intersection point of the leg [c_1, m_1] with
   w(kappa)}, kappa = the arc joining m_1 and m_2 (the core of the band cap); equivalently N(T_w) = CF(leg arc, boundary of a
   neighbourhood of w(kappa)), the same intersection points that compute reduced Khovanov homology of K_u = K(p/(q/2)) in
   the Kotelskiy-Watson-Zibrowius picture, with a two-parameter grading: winding around m_1, m_2 is weighted by x,
   winding around c_1, c_2 by u, and the two intersection points next to each crossing of the arcs differ by y (they are
   the two edges of the band: one P-pair, one special component). Count: 1 + 2 (p-1)/2 = p. In state-sum form: P_w is the
   Kauffman-state sum of the alternating diagram C(2a_1, b_1, 2a_2, b_2, ...) of K_u in which a crossing of k with k has
   weight step x and the crossings of k with the axis have weight steps y and u/y alternately (k over A, A over k).

## 6. Montesinos quotients: torus knots, the gluing formula, 9_46, and counterexamples to the shape law

6.1 [PROVED] Vertical sum as a cone. Let T = T_1 * T_2 be the sum transverse to the horizontal sum (T_1 on top, carrying the
   reduction point). Composition of resolutions: b*b = b + circle, b*c = c*b = b, c*c = c (verified). Hence
        F_b C(T_1 * T_2) = [ C_b(T_1) (x) C_b(T_2) (x) <1, X> ]  +  [ C_b(T_1) (x) C_c(T_2) ]  +  [ C_c(T_1) (x) C_b(T_2) ],
   where C_o(T_i) are the generators of type o, X is the dot on the new circle, and the differential is induced as follows:
     saddle b -> c of T_1:  (b,b) a -> (c,b) eps(a), eps(1) = 1, eps(X) = 0;      saddle c -> b of T_1:  (c,b) -> (b,b) X;
     saddle b -> c of T_2:  (b,b) a -> (b,c) eps(a);                               saddle c -> b of T_2:  (b,c) -> (b,b) X;
     D and S^2 between b-generators of T_1, and the dot on the UPPER strand of T_2 between its b-generators: multiplication by X;
     every arrow between c-generators of either summand, and the dot on the lower strand of T_2: zero.
   IMPORTANT: for T_2 one needs the complex over the unreduced Bar-Natan category: the dot on its second strand does not
   die (it becomes X on the circle), and D S = 0 fails there. BN~(T_2) alone is not enough. This is the "second strand
   survives" phenomenon of BRIEF2 section 3 in its simplest form.
   Twists: a framing twist of T changes nothing (5.2). A twist inside a summand lengthens its twist-region complex by one.

6.2 [PROVED from 6.1; checked with kht++ for (p,q) = (2,3), (3,4), (4,5), (5,6), (6,7), (3,5)] Integer summands.
   T = Q_{-p} * Q_q (kht++ word l0.y1^p.l0.x1^q.u2). Then N(T) has the basis (c_{1,j}, b_2), 2 <= j <= p, and
   (b_1, c_{2,j}), 1 <= j <= q-1: two D-ladders on adjacent delta-levels,
        N = { -m D : 0 <= m <= q-2 }  u  { (P - D) + m D : 0 <= m <= p-2 },      dim N = p + q - 2,
   in lattice coordinates rows b = 0: a in [-(q-2), 0];  b = 1: a in [-1, p-3].
   For q = p+1 this is the quotient tangle of the torus knot T(p,p+1) in the fibre framing (T(infinity) = unknot, T(0) =
   T(2,p) # T(2,p+1)); adding p(p+1) twists gives the Seifert framing and literally the table entry for 8_19 (p = 3).
   THEOREM D [PROVED]. For the strong inversion of T(p,p+1), p >= 2: dim N = 2p - 1 (= rank HFK^, the number of terms of the
   Alexander polynomial of this L-space knot; recalled, Ozsvath-Szabo);
        J = unit * ( [p]_{-1/t} + t^3 [p-1]_{-t} ),   extreme coefficients +-1, span 2p;   NP holds;
   Newton polygon = trapezoid with edges p-1 and p-2 times (1,0) and the two directions (p-3, 1) and (p-2, 1).
   So the hull directions n D + P occur for every n >= 0: (1,1) for 8_19 (the exception noted in BRIEF2), (1,1),(2,1) for
   T(4,5), (2,1),(3,1) for T(5,6). The list D, P, P-D, P-2D of the polygon law is only the low-crossing part of the truth;
   what survives in all examples is NP (no direction (4,-1)).
   [For general torus knots T(p,q) the summands are Q_{-p/b_1} * Q_{q/b_2} with b_1 q + b_2 p = +-1; 6.1 applies, not worked out.]

6.3 [DATA, kht++; files work/examples/vsum/] The shape law of BRIEF2 section 3 is FALSE beyond the table:
   T(4,5): Kh~ = r + 2 s4(inf) + s8(inf); the arc of BN~ has the move P_4 (lattice vector 4D + P); one square.
   T(5,6): 2 s4 + 2 s8; a compact component which is the rectangle  x -P_4-> . -D-> . <-P_4- . <-D- x ; one square.
   T(6,7): 2 s4 + 2 s8 + s12; arc with P_6, rectangle with P_4, square.
   So longer specials s_{4n}(inf) and the moves P_{2n} do occur (first at 15 crossings), compact components need not be
   squares, and N need not be "staircase + unit squares". What survives there: N is a union of D-ladders; H(d_D) = H(d_P) = F.
   In lattice terms P_n = (2n-4) D + P and D^a = D + (a-1)(5,-1).

6.4 [DATA + PROVED topology] 9_46 = P(3,3,-3).
   First inversion: constituents (K_u, K_l) = (3_1, 3_1) (mirror pair); N = point + 2 squares, 9 = rank HFK^.
   Second inversion: (K_u, K_l) = (T(3,4), 3_1) (Alexander polynomials t^6 - t^5 + t^3 - t + 1 and t^2 - t + 1).
   dim N = 15 = rank Kh~(8_19) * rank Kh~(3_1) = 5 * 3 > 9 = rank HFK^(9_46).
   What is special: this is the only table entry where the product of the constituent ranks exceeds rank HFK^(K), i.e.
   where the bound (S') below is stronger than Theorem S. The arc of BN~ is  rho -D- . -P- . -D^2- . -P- . -D- . -P- x_0
   with the D^2 step (lattice jump (6,-1)) in the middle, and the hull has the directions (7,-3) and (3,-2); the long step
   mirrors the length-two steps of the staircase of the non-thin constituent T(3,4).
   (S') [CONJECTURED; holds in all 132 table cases, with equality in 130]  dim N(T) >= rank Kh~(K_u) * rank Kh~(K_l).
   Proof route: N(T) = AKh(K_u u K_l; top weight) and each constituent winds once around the band meridian B, with top-weight
   annular homology Kh~(K_u), Kh~(K_l); a Batson-Seed link-splitting spectral sequence that respects the annular filtration
   would give the inequality (their deformation uses only edge maps, which never raise the annular degree; the invariance
   of the deformed homology under crossing changes has to be re-proved for the associated graded complex: not done).
   Together with Theorem S:  dim N(T) >= max( rank HFK^(K), rank Kh~(K_u) rank Kh~(K_l) ), an equality in all 132 cases.

## 7. Task (4): the edge directions, the operation that creates (4,-1), and why B0 is not a tangle

7.1 [PROVED given 2.1/4.2] Origin of the directions. In the two-bridge class every generator is a monomial x^i u^j y^e:
     D = x      comes from band crossings (X-blocks contribute [b]_x; eigenvalue ratio -t of the half twist of the bands),
     D - P = u  comes from axis crossings (Y-blocks contribute u [a]_u; eigenvalue ratio t^-3 of the axis going round a band),
     P = y      is the factor (1+y) = the two edges of the band = the two bullet generators of one special component,
     2D - P = x u is a corner between a D-edge and a (D-P)-edge cut off by one cancellation (4.5); larger cuts give the rarer
               directions (3,-2) = x u^2 etc.;  n D + P come from long twist regions transverse to the axis (6.2).
   In the (q/2, delta) plane these move q/2 by 1 (D, same level), 4 (P), 3 (D-P), 2 (2D-P), n+4 (nD+P) per level.
7.2 [PROVED] The direction (4,-1) = x^4/y = (h,q) (1,0) is the degree of the differential that implements the relations of
   the braid group: Mt_x M_X = [[1, (1+y)(1 + x^4/y)],[0,1]] and Mt_y M_Y = [[1,0],[(y/x^4)(1 + x^4/y),1]] instead of the
   identity. In particular  Mt_x^2 M_X^2 = [[1, (1+x)(1+y)(1 + x^4/y)],[0,1]], so for the word w = Y X^2 x^2 (a diagram of the
   TRIVIAL tangle: two band crossings followed by their inverses)
        P^E_w = 1 + u (1+x)(1+y) + (x^4/y) u (1+x)(1+y)  =  a(0) + S + hS  =  B0.
   B0 IS the unreduced complex of a Reidemeister-II pair of band crossings with its differential set to zero.
   The operation that creates the forbidden edge is therefore "compose a twist with its inverse and forget the map that
   makes them cancel". In an actual tangle that map is an isomorphism because twist functors are invertible (Reidemeister
   II invariance), and S, hS cancel.
7.3 [PROVED for J; conditional on (CAT) for N] Why no tangle of the class has it. A (4,-1) edge at the top of the polygon
   is a tie in the leading exponent at an E-step: deg(v_2/v_1) = -4. Theorem B: for a reduced word the exponent before an
   E-step always lies in {-3} u [0, infinity); the value -4 is the state immediately AFTER an E-step, so a tie needs two
   consecutive E's, i.e. an unreduced word E E = t^4 (equivalently X x or Y y). So in the two-bridge class the offset
   (4,-1) is extremal only for unreduced words, where it is killed by the differential. This is the precise statement
   that B0 violates (its two top generators tie and nothing cancels them) and that actual tangles of the class satisfy
   (ping-pong of the leading exponent).  For general tangles the corresponding statement is open; see the summary.

## 8. THE JUNCTION FORMULA: closed form of N(T) for all side-preserving two-bridge inversions (added last; supersedes 4.2 as the main statement)

8.1 Reduction of words (PROVED at the level of rho; these are the relations of Z/2 * Z and the trivial end moves):
       Yy, yY, Xx, xX -> empty;   YxY -> X,  xYx -> y,  XyX -> Y,  yXy -> x;   leading X, x dropped;  leading Yx -> y,
       leading yX -> Y;   trailing Y, y dropped.
   In a reduced word the sign changes (a positive letter next to a negative one) are disjoint pairs "Yx", "Xy" (type +-) and
   "xY", "yX" (type -+).

8.2 JUNCTION FORMULA [DATA: exact equality of multisets up to translation for 145 tangles = 90 table entries (80 with mixed
   signs) + 55 own kht++ runs; scripts/junction.py. CONJECTURED in general.]
       P_{N(T_w)}(x,y) = monomial * (1 0) * prod of matrices * (1 0)^T,      one matrix per letter of the reduced word,
       except that each sign-change pair is replaced by ONE junction matrix:
         M_Y = [[1,0],[u,u]]            M_X = [[1,1+y],[0,x]]                 (u = x/y)
         M_y = [[1,0],[y/x^4, y/x]]     M_x = [[1, x^3(1+y)/y],[0, 1/x]]
         J+- = [[1, 1+y],[y/x^4, y/x^4]]            J-+ = [[1, x^3(1+y)/y],[x/y, x^4/y]].
   J+- and J-+ are M_x M_Y (= M_y M_X up to a monomial) and M_Y M_x (= M_X M_y) with exactly one pair of monomials at
   offset (4,-1) removed. All matrices are positive; at (x,y) = (-t,-t^4) the formula is Theorem A.
   Example: Y^a x^b -> Y^{a-1} J+- x^{b-1}:  P = 1 + (1+y)([a]_u [b]_{1/x} - 1).

8.3 [machine consequence of 8.2, 30482 reduced words with <= 3 blocks and |exponents| <= 3; scripts/junction_hull.py]
   (i)   the number of generators is |p| = det K (the formula is a minimal model: no further cancellation is possible by rank);
   (ii)  NP in the strong form: exactly one generator in the top and one in the bottom quantum degree;
   (iii) POLYGON LAW: the Newton polygon has edges in the directions D, P, D-P, 2D-P and no others; 2D-P occurs iff the
         reduced word has a sign change (28012 of 30482), never for one-signed words (pentagon of 4.3).
   Table check [DATA, scripts/table_cat.py]: the 90 two-letter table entries have these four directions only and
   multiplicity (1,1) in the extreme quantum degrees.
   So for this class the polygon law of BRIEF2 holds with exactly its four directions, and the exceptional directions of
   the table ((3,-2), (1,1), (7,-3)) all come from other classes (6.2, 6.4, exchange-type inversions).

8.4 What a proof of 8.2 needs [route]. (CAT') (a) the Artin group of type B_2 acts on a 2-object dg category C with
   N(T_w) = H Hom(cap, w . cup) (functoriality of F_b C(.) under the two elementary 6-ended pieces "band crossing" and
   "axis round a band", each a 4-crossing tangle: a finite computation in Bar-Natan's category, not done here);
   (b) the Poincare matrices of the minimal complexes of X, Y, x, y are M_X, M_Y, M_x, M_y, and that of the composite at a
   sign change is J+-/J-+ (one Reidemeister-II cancellation, local). Then the tensor product complex of a reduced word has
   |p| generators, and Theorem S (dim N >= rank HFK^(K) = det K, K alternating) forces its differential to vanish: 8.2.
   Without Theorem S one would need the differential to vanish for degree reasons, which is false in general (offsets
   (4,-1) occur inside N), so the Floer lower bound is a genuine input.

   Addendum to 8.3 [machine, same 30482 words, scripts/junction_shape.py]: the junction polynomial satisfies P(x,-1) = +-monomial,
   P(-1,y) = +-monomial and P = (staircase from rho to x_0) + (1+x)(1+y) Pi with Pi >= 0, for every reduced word: the
   multiset version of the shape law holds in the whole class.
   Addendum to 6.4 [DATA, kht++ on the constituent knots, work/examples/const/]: for 9_46-2, Kh~(K_u) = tower + H + H^2 torsion
   (rank 5, the reduced Khovanov homology of T(3,4)) and Kh~(K_l) of rank 3; for 9_42: ranks (7,1); 8_19: (1,3);
   9_46-1: (3,3), a left-handed and a right-handed trefoil.
   Clarification of 6.1: "multiplication by X" refers to the summand (b,b); on (b,c) the D- and S^2-arrows of T_1 act by 0,
   and powers D^k, k >= 2, act by 0 everywhere (X^2 = H X and H -> 0).

## FILES
scripts/chain.py (parser of kht++ chain files), run.py (cached kht++ runner, lattice picture; cache in work/cache.json),
constituents.py + table_const.py (constituent knots K_u, K_l; table_const.txt), table_alex.py, matrix_formula.py (2.1),
mixed.py, hybrid.py, hybrid_vs_data.py (4.2, 4.4), jmatrix.py, span_check.py, jcheck.py, table_thmA.py (Theorems A, B),
hull_formula.py, check43.py (4.3), junction.py, junction_hull.py, junction_shape.py, table_cat.py (section 8),
gridfile.py; kht++ working folder work/ (examples/words, examples/vsum = vertical sums / torus knots, examples/const).
Coefficients F_2 throughout. Nothing here proves Lemma Q or the Jones unknot conjecture.

## SUMMARY

MECHANISM PROPOSED BY THIS LENS (PP = ping-pong). J(T) is the coefficient "band cap -> band cup" of a braid-type
representation (Theorem A for two bands), and N(T) is the homology of the corresponding product of twist complexes, whose
differential has lattice degree (4,-1). STATEMENT: for a REDUCED word the leading exponent of the state vector never ties
(Theorem B: before every E-step deg(v_2/v_1) lies in {-3} u [0,infinity), never -4), so the extreme coefficient is +-1 and,
granting (CAT'), the extreme quantum degree of N has one generator (NP). B0 violates it: B0 is the product for the
UNREDUCED word Y X^2 x^2 with the cancelling differential removed, and its two top generators tie. Actual tangles satisfy it
because the twist functors are invertible, so every tie comes from a cancelling pair and is removed by the differential.
First lemma proved: Theorems A, B (all side-preserving two-bridge inversions) and D (torus knots T(p,p+1)). Gap: more
than two band strands (general theta-curves), and the categorified statement (CAT').
NEGATIVE FINDINGS: two-bridge quotients are not sums of rational tangles (premise of task (1)); the shape law and the list
of directions in the polygon law are false in general (T(4,5), T(5,6), T(6,7)); NP is the statement that survives.

PROVED
 1. Topology (section 1). The quotient tangle of a strong inversion is a 2-string string link with strands A_u, A_l, and
    T(0) = K_u u K_l (constituent knots of the theta-graph). Two-bridge quotients are NOT sums of two rational tangles
    unless K = T(2,n); they are "axis + a band wound by a 3-braid" (word in Y = axis crossing, X = off-axis crossing), with
    K_l = unknot and K_u = K(p/(q/2)); T(0) u (band meridian) = a (1,1)-knot with the two cores of its Heegaard torus.
 2. J(T) = the (V_1, V_1, V_2)-coloured sl_2 invariant of the theta-graph; Lemma Q <=> this invariant detects the trivial
    theta-curve among theta-curves with an unknotted cycle.
 3. THEOREM A: for side-preserving two-bridge inversions J(T_w) is the (1,1)-coefficient of a product of the matrices
    rho(Y) = [[1,0],[t^-3,t^-3]], rho(X) = [[1,1-t^4],[0,-t]] (a 2-dimensional representation of Z/2 * Z, the B_2 Hecke
    algebra with unequal parameters). Confirmed on 130 kht++ tangles.
 4. THEOREM B: for every side-preserving strong inversion of a non-trivial two-bridge knot T is not flat; the extreme
    coefficients of J are +-1 and span J is given by an explicit sum of positive terms. Proof: ping-pong on the leading
    exponent of v_2/v_1 (no ties for reduced words). This is Lemma Q, and END at the level of J, for that class.
 5. Vertical (Montesinos) sum as a cone (6.1), with the unreduced complex of the second summand; THEOREM D: for T(p,p+1),
    N = two D-ladders of lengths p and p-1, J = [p]_{-1/t} + t^3 [p-1]_{-t}, NP holds, hull directions (p-3)D+P, (p-2)D+P.
 6. B0 = a(0) + S + hS is exactly the unreduced complex of the trivial tangle written as Y X^2 x^2 (two band crossings and
    their inverses) with the Reidemeister-II differential deleted; the forbidden direction (4,-1) is the degree of that
    differential (7.2).
DATA (new)
 7. Closed formula for N(T): positive words 2.1 (24 words), all words by the JUNCTION FORMULA 8.2 (145 tangles, exact).
    From the formula (machine, 30482 words): dim N = det K, NP, polygon law with exactly the directions D, P, D-P, 2D-P,
    staircase + squares. Slope k and staircase length l in closed form (4.3).
 8. det K = det K_u det K_l; dim N = max(rank HFK^(K), rank Kh~(K_u) rank Kh~(K_l)) in all 132 table cases; this explains
    15 for 9_46 second inversion (constituents T(3,4) and 3_1).
 9. The shape law of BRIEF2 is false beyond the table: T(4,5), T(5,6), T(6,7) have specials s8, s12, moves P_4, P_6 and
    non-square compact components. The polygon law's list of directions is not complete (nD + P occur). NP survives everywhere.
CONJECTURED
 10. (CAT') the type B_2 braid group action on a 2-object category with Poincare matrices M_X, M_Y, M_x, M_y and junction
     matrices J+-, J-+, computing N(T_w). (CAT') => NP for the class (Theorem C); (CAT') + Theorem S => junction formula
     => polygon law (proved for positive words, machine-checked for mixed ones).
 11. (S') dim N(T) >= rank Kh~(K_u) rank Kh~(K_l) (annular Batson-Seed).
 12. Arc model 5.3 (N = intersection points of two arcs on the orbifold sphere with a two-parameter grading).

THE NAMED GAP
 For the two-bridge class: (CAT'), i.e. that the tensor product of the elementary twist complexes computes N(T_w) with the
 stated Poincare matrices (a finite computation with two 4-crossing 6-ended tangles in Bar-Natan's category, plus one
 local cancellation at a sign change). Given (CAT'), NP for the class is proved (Theorem C: the no-tie argument holds for
 every normal form), and with Theorem S the junction formula follows. The polygon law with exactly four directions is then
 proved for positive words (4.3); for mixed words it is machine-checked from the formula on 30482 words, and the induction
 on the word that would prove it has not been written. Outside the class: exchange-type two-bridge inversions (q^2 = 1 mod p; a 4-dimensional
 representation), general Montesinos and arborescent quotients (6.1 applies but is not worked out), and the general
 statement behind Lemma Q: "for a reduced presentation the leading exponent never ties", which is what B0 violates.

THE SINGLE MOST PROMISING NEXT STEP
 Generalise the ping-pong of Theorem B from 2 to n band strands: every theta-curve with unknotted cycle A is "axis + plat
 of doubled strands", so J(T) is a matrix coefficient (band caps to band cups) of the mixed braid group B_{1,n} acting on
 Hom(V_1, V_1 (x) V_2^{(x) n}); Lemma Q says this coefficient is a unit only for the trivial theta-curve. The proof for n = 2
 used only a leading-exponent (tropical) automaton with no ties on reduced words, the same mechanism as in the
 Krammer-Bigelow proofs of faithfulness. First test case: the exchange-type inversions (7_4-2, 7_7-2, 9_23-2; n = 3,
 dimension 4), where the answer can be checked against kht++. In parallel, (CAT') should be verified by the finite local
 computation, which would turn the junction formula and NP for two-bridge inversions into theorems (and the polygon law,
 once the induction on the word is written for mixed words).
