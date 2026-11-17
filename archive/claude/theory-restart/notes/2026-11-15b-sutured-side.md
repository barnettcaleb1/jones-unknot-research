# N(T) is the Khovanov side of knot Floer homology (Claude, 15 November 2026, evening)

Status markers: [PROVED] = argument complete given the cited theorem; [CITED] = quoted from memory, source to be pinned;
[DATA] = derived from the saved kht++ outputs; [CONJ] = conjecture. Coefficients F_2. Nothing here proves Lemma Q.

Notation. (K,h) strongly invertible, T its quotient tangle, Seifert framed, T(inf) = U. b = Q_0 = kht++ ⬮ (unit of the
horizontal sum), c = Q_inf. N(T) = H(F_b C(T)) = bullet-generators of BN~(T) (Codex TH-BULLET-SUM/RANK), dim N = 1 + 2m,
m = number of special components of Kh~(T); chi_q N = u J.

## 1. Three descriptions of N(T)

(1a) [PROVED] Representation theory. In the direction of the horizontal sum T is an endomorphism of V (x) V = V_2 + V_0.
Its eigenvalue on V_0 is the unit u (this is the statement that T capped off on one side is a trivial arc, i.e. T(inf) = U)
and its eigenvalue on V_2 is y = uJ. So J = (eigenvalue on the 3-dimensional summand)/(eigenvalue on the trivial summand),
and N(T) categorifies the action of T on the highest weight vector v_+ (x) v_+.
Special case: for the swap inversion on K # K the tangle is the doubled strand tangle T_K and J = reduced Jones polynomial
of K coloured by the 3-dimensional representation. So Lemma Q contains "the 3-dimensional coloured Jones polynomial detects
the unknot" as the special case of swap inversions.

(1b) [PROVED] Annular. Close T (or T sigma^n) around an annulus in the horizontal direction. Resolutions of type b give two
essential circles, type c one inessential circle. The complex F_b C(T) (keep b-resolutions, kill dots on the two strands,
kill saddles to c) is term by term the annular Khovanov complex in annular weight k = 2. So
    N(T) = AKh(T(n) in A x I; k = 2)   for every integer n (up to shift),
and by the sl_2 action AKh(T(n)) = N (x) V_2 + (weight-zero multiplicity space).

(1c) [PROVED given CITED] Sutured. The same complex is Grigsby-Wehrli's Khovanov complex of the balanced tangle T in D x I
(non-backtracking resolutions). Grigsby-Wehrli (arXiv:0807.1432, the balanced-tangle theorem behind their coloured Jones
result; and arXiv:0907.4375): a spectral sequence from Kh(mirror T in D x I) to SFH(Sigma(D x I, T)).
Here Sigma(D x I, T) = S^3 - nu(K), and the suture dD x {1/2} separates the two left ends from the two right ends, so it
bounds a disc disjoint from the closing arcs of T(inf); its lift is two meridians of K. Hence SFH = HFK^(K) (Juhasz) and

    THEOREM S. There is a spectral sequence with E_2 = N(mirror T) converging to HFK^(K; F_2).
    In particular  1 + 2 m(T) = dim N(T) >= rank HFK^(K) >= 2 g(K) + 1,  so m(T) >= g(K),
    and m(T) = 0 iff K is the unknot (a second proof of rational detection on this locus).

For T_K this is exactly Grigsby-Wehrli's theorem for n = 2: reduced 2-coloured Khovanov homology => HFK^(K # K).

(1d) [PROVED] Curves. With parametrising arcs A_bullet (loop at the special puncture * around p1) and A_circ (loop at *
around p3), N(T) = HF(BN~(T), A_bullet). The arc [*, p1] has the slope of the unknot filling, so A_bullet lifts to the
meridian arc through the basepoint on the boundary torus of the knot exterior. Hanselman-Rasmussen-Watson compute HFK^(K)
as HF(curve of the exterior, meridian arc through z). So N(T) is, word for word, the Khovanov-multicurve analogue of
the immersed-curve formula for HFK^.

## 2. Data check of Theorem S [DATA]
- Table of 138 (132 parsed): 1 + 2m = rank HFK^(K) in 131 cases, including the thick knots 8_19 (5, not det = 3) and
  9_42 (9, not det = 7). Exception: 9_46 second inversion, 15 > 9 (allowed by a spectral sequence). That tangle is also the
  only one with a D^2 arrow in its arc.
- Doubled tangles T_K, K two-bridge of determinant p: 1 + 2m = p^2 = rank HFK^(K # K) in all 21.
- Two-bridge quotients: 1 + 2m = p whenever the generated file is the labelled knot (101 files; the others are diagrams of
  smaller two-bridge knots produced by the generator, to be relabelled, not counterexamples).
So the count of specials is a knot Floer rank, and the sequence collapses in almost every computed case.

## 3. The strip picture and the standard form [DATA + elementary geometry]
Cover R^2 - Z^2 -> pillowcase: * = (even, even), p1 = (0,1), p3 = (1,0), p2 = (1,1) mod 2. Lifts of A_bullet are the two
sides of vertical lenses L_n on the special line x = 0 (from (0,2n) to (0,2n+2), around the p1-lift (0,2n+1)).
Moves between consecutive bullet-generators along a curve:
    D^a   (cross a lens, a half-turns about a p1-lift):            (h,q) = (1, 2a),      delta-change 0
    P_n = S (D S^2)^{n-1} D S  (run past n lenses on one side):     (h,q) = (2n+1, 4n),   delta-change -1
Every multicurve component lies in the strip |x| < 1 around the special line. In ALL saved chain files the only moves are
D (a = 1) and P_2, except: one D^2 (9_46 second inversion), and the arc's tail S (D S^2)^{|k|/2 - 1} D ending at p2
(which carries the slope k of the rational component). The arc starts at a p1-lift. Field independent on the cases
rerun over F_3 and Q.
Compact components seen: only the square  x -P-> . -D-> . <-P- . <-D- x  (four bullet-generators).

## 4. Lattice coordinates [PROVED from 3]
Write a bullet-generator as rho + a D + b P (D = (1,2), P = (5,8) in (h,q)). Then
    h = a + 5b,  q = 2a + 8b,  delta = -b,  2q - 3h = a + b,
N = finite multiset S in Z^2,  J = sum over S of (-t)^a (-t^4)^b   (t = q^2; positive polynomial P(x,y) at x = -t, y = -t^4).
Double domino structure: S minus x_0 (start of the arc) is a union of horizontal dominoes (D-pairs); S minus rho (end of
the arc) is a union of vertical dominoes (P-pairs = the two generators of a special). So N looks like the reduced
Khovanov homology of a knot twice over: pawn + (1,2)-pairs, and pawn + (5,8)-pairs.
Cancellation in J: (a,b) against (a - 4m, b + m), m odd. Codex's B = two squares offset by (-4, +1), i.e. by
(h,q) = (1,0), the bidegree of the Khovanov differential itself.
TILT in these coordinates: with M_b, m_b the largest and smallest a on level b,
    M_b >= M_{b-1} - 3  and  m_b >= m_{b-1} - 3   (observed: differences in {0,-1,-2,-3}).
Equivalent form: every generator not on the extreme level has a generator above it and one below it at relative bidegree
(k, 2k-2) with k >= 2, the bidegrees of the higher differentials d_k of a Szabo-type spectral sequence; the excluded offset
is k = 1.

## 5. Reading
Lemma Q is the Jones-type question for the sutured (tangle) theory: the Euler characteristic of the Khovanov side of
HFK^ detects the unknot, while the Euler characteristic of HFK^ itself (the Alexander polynomial) does not. On the
Floer side the configuration B really occurs: for Alexander polynomial one knots CFK is a point plus boxes of both
parities. So the sharpest test of END / J-TILT is a strong inversion on a knot with Delta = 1 (section 6).

## 6. Test on Alexander polynomial one knots
Tools: tools/alex.py (Alexander polynomial from a half-diagram word), tools/kauffman.py (bracket of the completed diagram),
tools/alex_search.py, tools/run_words.py. Random search of ~320,000 half-diagram words found two classes with Delta = 1
(numerically at t = -1, 2, 3, 5) and non-trivial Jones polynomial:
  A: s.r1.y0.x2.r3.y0.y2.u1.x2.x2.y0.y1.x0.u1  (Jones span 10, 15 = sum of |coefficients|; 12 words)
  B: s.l1.x0.y1.x0.y1.l1.y4.y4.x1.y0.y3.u2.y2.y0.u1  (Jones span 12, sum 31)
Results (class A, four different words, all the same tangle up to mirror; 90 to 290 s each): Kh~ = r_1(+-4) + 15 specials s4(inf),
k = +-4, j = 0, dim N = 31; BN~ = arc (three bullet-generators, a 3-staircase with tail) + 7 squares.
    b= 1:  1 2 1 . .
    b= 0:  1 4 5* 2 .
    b=-1:  . 2 4 4 1
    b=-2:  . . 1 2 1          (a from -2 to 2; * = rho)
END holds at both ends (extreme coefficients +-1); hull edges only (1,0), (0,1), (1,-1); one interior cancellation.
The squares have signs + - + + - + - at seven q-positions with no two cancelling: the q-grading separates the boxes
that the Alexander grading identifies. (The knot is not identified; dim N = 31 would force rank HFK^ <= 31, so it is not
the Conway or Kinoshita-Terasaka knot if their rank is 33.) Class B: running.

## 7. Shape law and polygon law [DATA]
SHAPE LAW. In 548 of 551 saved arcs (the three others are invalid random words) the arc is a pure staircase: P_2 runs all
in one direction alternating with D arrows all in the other direction (one D^2, in 9_46 second inversion), plus the tail.
All 1420 compact components in the table and the doubles are the square. So with d_D, d_P the two arrow maps,
N = Z_l + Lambda^r as a module over Lambda = F[d_D, d_P]/(d_D^2, d_P^2):  one zigzag of length 2l+1 = 2|2j + k/4| + 1 and r
free modules (squares). This is exactly the structure theorem for knot Floer complexes of thin knots (staircase + boxes).
Expected proof: lift to the unreduced theory, where the dot on the second strand does not kill the saddle, so that
d_D d_P != 0 unless compensated; a composable pair D then P must then be completed to a square.  [CONJ, first lemma for Codex]
Examples of shapes: 4_1 (both inversions) 5-staircase; 5_2 first inversion 7-staircase, second inversion 3-staircase + 1
square; 9_42 and 9_46 first inversion point + 2 squares; double of 3_1: 5-staircase + 1 square; double of 4_1: point + 6
squares (the shapes of CFK(3_1 # 3_1) and CFK(4_1 # 4_1)).
J = chi(zigzag) + (1 - t)(1 - t^4) Pi(t),   Pi(t) = sum over squares of (-1)^{a+b} t^{a+4b} = sum over squares of
(-1)^{delta} (-t)^{q/2}: squares on even delta-levels minus squares on odd delta-levels, graded by q.
The B-offset (two squares differing by (h,q) = (1,0)) DOES occur inside actual tangles (333 adjacent-level pairs of squares
in the data); only the bare object a(0) + S + hS is excluded. So the missing law is global, about the outline.

POLYGON LAW. Newton polygon of N in the (a,b) plane, 283 distinct tangles: edge directions
    (1,0) [D] 468,  (0,1) [P] 424,  (1,-1) [P-D = (4,6)] 511,  (2,-1) [P-2D = (3,4)] 177,
    (3,-2) 7,  (1,1) 1 (8_19),  (7,-3) 1 (9_46 second inversion).
In the (q/2, delta) plane: every non-horizontal edge moves q/2 by 2, 3 or 4 per delta-level (rare: 5/2, 5, 5/3).
A cancellation at an extreme of J needs an edge that moves q by 0 per delta-level. Lemma Q follows from:
    (NP)  the maximum and the minimum of q on N(T) are each attained on a single delta-level.
Newton polygons add under the tangle sum, so the set of edge directions is closed under sums.
In the (h,q) plane all edges have slope between 5/4 and 2; the cube complex itself has a flat top and bottom (slope 0).

## 8. Check of (1a): the doubled figure-eight
From the grid of the doubled 4_1 tangle: J = t^6 - t^5 - t^4 + 2t^3 - t^2 - t + 3 - t^-1 - t^-2 + 2t^-3 - t^-4 - t^-5 + t^-6,
which is Habiro's formula 1 + {2}{1} + {2}{1}{5/2}{1/2} for the 3-dimensional coloured Jones polynomial of 4_1 (q = t). [PROVED by expansion]

## 9. Surgery collapse and MATCH (late evening)
See THEORY X.16, X.17 on the board for the statements. Tools: tools/surgery_collapse.py (closures T(n) via kht++, largest pairing of Szabo type,
comparison with the Ozsvath-Szabo surgery rank for a staircase+boxes model), tools/matchable.py (torus knots), tools/daemi_match.py (formal
configurations at K_n). Results file: lit/kht/out/surg/results.txt.
Key points: (1) Daemi's plane Floer sequence gives MATCH for every link with nonzero determinant, with the degree rule (r, 2r-2) forced by his
gradings. (2) Bare B fails MATCH at every K_n (2n+1 generators left). (3) Ladders pass. (4) The steps 2,4,6,8 of TILT are the q-shifts of
r = 2..5; step 0 would be r = 1. (5) Withdrawn: m >= g (8_19), "rank HFK^ = 5 is classified" (T(3,4) has rank 5); the corollary is
dim N >= 5 for a flat non-rational tangle.
Correction of a slip in section 6: it is the delta (row) parity that corresponds to the Maslov parity, since differentials have h-degree r.

## 10. Two further observations (midnight)
(a) THETA-CURVE FORM [PROVED, elementary]. (K,h) corresponds to the theta-curve Theta = U + kappa (U the image of the axis, kappa the image of K; Sakuma).
The two strands of T are the two edges e_1, e_2 of Theta other than kappa. Projecting V (x) V onto V_2 at both ends of T fuses e_1, e_2 into the chord, so
uJ is the sl_2 evaluation of Theta with colours (V_1, V_1, V_2), V_2 on kappa, normalised by the planar theta; u is the evaluation with kappa deleted (the unknot).
So Lemma Q says: this (1,1,2)-coloured invariant detects the planar theta-curve among theta-curves with unknotted cycle e_1 + e_2. (The Yamada polynomial is the
(2,2,2) colouring.) N(T) is the corresponding coloured Khovanov homology (2-coloured edge = 2-cable in top annular weight), and Theorem S sends it to HFK^ of the lift of kappa.
(b) FACTORS [DATA]. For tangles with trivial arc (k = j = 0), N = point + squares, write the squares as a polynomial in the lattice monomials x^a y^b.
    9_42: x(1 + u^-1);  9_46 first inversion: x^-3 (1 + u^-1);  class C (Alexander polynomial 1): (1 + u)(1 + u^-1);
    double of 4_1: x^-3 y (1 + u)(1 + w + w^2);      u = x/y (offset (1,-1), (h,q) = (-4,-6)),  w = x^2/y (offset (2,-1), (h,q) = (-3,-4)).
  Under x -> -t, y -> -t^4: u -> t^-3, w -> -t^-2, so (1 + u) -> 1 + t^-3 and 1 + w + w^2 -> 1 - t^-2 + t^-4: cyclotomic factors Phi_2 Phi_6 and Phi_12.
  Classical reason for one factor [PROVED]: with trivial arc J - 1 = (1-t)(1-t^4) Pi and J - 1 = 0 mod (1-t^4)(1+t^3), hence Pi = 0 mod (1 + t^3). At t = -1 this
  says: the number of squares on even delta-levels equals the number on odd delta-levels. In the examples the factor is visible on the nose: the squares pair up at
  offset u (bidegree (4,6), the r = 4 differential of MATCH).
  A ladder is  point + (1 + h)(1 + tau_g) Q,  h = offset (-4,1) = (h,q) (1,0), which goes to 1 - 1 = 0. So flatness for trivial arc means: the polynomial of squares
  has a factor that specialises to zero; the actual examples have only factors that specialise to cyclotomic polynomials.

## 11. The EKT link as a control (00:05)
LL2(1) = closure of sigma_3^3 (sigma_2^-1 sigma_3^-1 sigma_1^-1 sigma_2^-1)^2 sigma_1^-3 (Morse word r1.r2.r3.x2.x2.x2.y1.y2.y0.y1.y1.y2.y0.y1.y0.y0.y0.u3.u2.u1):
Kh~ over F_2 has rank 26: delta = 1.5: (1,5),(2,7),(3,9)^2,(4,11)^3,(5,13)^2,(6,15)^2,(7,17),(8,19); delta = 2.5: (0,5),(1,7),(2,9)^2,(3,11)^2,(4,13)^3,(5,15)^2,(6,17),(7,19).
Jones: q^11 + q^13 only. So Kh~ = unlink + X + hX, rank X = 12. Largest Daemi-type matching: 10 pairs; but the plane Floer limit has rank 2 |Z/13| = 26, so no
differential is nonzero. Bare-B structure exists for links when the double cover has torsion; it cannot exist for closures of quotient tangles (cyclic H_1 of order |p|).

## 12. The delta-rows of N are not a Maslov grading (00:20) [DATA + elementary; to be refereed]
Grigsby-Wehrli arXiv:0807.1432, Conjecture 7.1 (as read by the Floer lens): there is a lift M of the relative Maslov grading of SFH with E^infinity_{delta = d} = SFH_{M = d}.
Test on their own case n = 2, K = 4_1: the doubled tangle has dim N = 25 = rank HFK^(4_1 # 4_1), so E^2 = E^infinity. Its delta-levels have dimensions (2, 6, 9, 6, 2).
HFK^(4_1 # 4_1) is thin with ranks (1, 6, 11, 6, 1) in Alexander gradings 2..-2, each Alexander summand in a single Maslov grading; a lift of the relative Maslov grading
assigns one integer to each Alexander summand, so its graded dimensions are sums of whole numbers from {1,6,11,6,1}: some degree has dimension >= 11. But no delta-level
exceeds 9. Same contradiction for the two inversions of 4_1 (levels (1,2,2) against three generators in one Maslov grading at A = 0) and for 5_2 first inversion
(levels (2,2,2,1) against three generators at A = 0). The Z/2 version holds in all cases (delta parity = Maslov parity).
So when the sequence collapses, N = gr of a filtration on HFK^(K), but the Alexander summands sit skew to the (h,q) bigrading: there is no Alexander grading on N,
and the rows of N are not Maslov gradings. (Class C is NOT P(-3,5,7): different Jones polynomials; P(-3,5,7) has rank Kh~ = 15.)
