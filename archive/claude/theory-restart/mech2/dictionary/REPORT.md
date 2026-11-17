# REPORT: lens DICTIONARY (N(K,h) versus the knot Floer complex of K)

STATUS (2026-11-15, start): reading the brief and derivation notes. Nothing established yet.
Marks: PROVED / CITED (source, statement number, read-now or recalled) / DATA / CONJECTURED.

## 0. Working notes (appended as I go)

- [setup] Parser for kht++ chain files: `dictionary/chains.py` (b-generators, D- and P-arrows, lattice coordinates).
  Checked on 3_1, 4_1^1, 5_2^2, 8_19, 9_42, 9_46^2 against tools/grid.py.
- Normalisation used below (from the brief + grid.py): in kht++'s absolute bigrading (tangle oriented braid-like, both strands
  left to right) the end rho of the arc has (h,q) = (8j + k, 24j + 2k), delta(rho) = 4j. Lattice coordinates (a,b) are relative to rho.
  With P(x,y) := sum over N of x^a y^b one has  J(t) = t^k P(-t,-t^4)  (k is divisible by 4 in all data).

## 1. Table (task 1) and first formulas (task 2)

Files: `dictionary/table.json` (132 parsed inversions of the 138: lattice positions, arc path, squares, plus knot data),
`dictionary/alex.json` (Alexander polynomials from the same diagrams), scripts `chains.py`, `table.py`, `show.py`, `jtest.py`,
`alexall.py`; knot-mode kht++ runs (s-invariant, Kh~ of the knot itself, same diagram hence same chirality) in `dictionary/work/examples/kn/`.
Signature convention: positive knots have negative signature; sigma read off as -2 x (delta of the majority diagonal of Kh~(K)),
which is correct for all knots up to 9 crossings (thin ones, and 8_19, 9_42 checked by hand).

DATA (132 inversions; "exceptional" = 9_46 second inversion, the one case with dim N > rank HFK^):
- D1. The start x_0 of the arc (the generator of H(d_D)) has homological degree h = 0 in kht++'s absolute grading, in all 132.
      Its quantum degree is q(x_0) = 12j + k/2 in 131 (exceptional case: 24 instead of 22).
- D2. The zigzag is a pure staircase in 131: either type "+" rho=(0,0),(1,0),(1,-1),...,(l,-l) or type "-" (0,0),(-1,0),(-1,1),...,(-l,l).
      The first arrow at rho is always a D-arrow. Signed length l_s := +-l equals 2j + k/4.
- D3. dim N = rank HFK^(K) in 131 (= det K for the thin knots, 5 for 8_19, 9 for 9_42).
- D4. k = 2 s(K) = -2 sigma(K) for every thin knot in the table (129 inversions); 8_19: k = 8, s = 6; 9_42: k = 0, s = 0, sigma = -2;
      exceptional case: k = -4, s = 0.  k is the same for the two inversions of a knot (except 9_46).
- D5. j = Arf(K) mod 2 in all 132 (Arf from the Alexander polynomial at -1).
- D6. For the two inversions of one knot, j_1 - j_2 is even and takes values in {0, +-2, +-4}; j is NOT a function of K.

Consequences in the lattice (PROVED from the double domino structure, i.e. from Kh~(T) = r_1(k) + specials s4(infinity) and the square/staircase shape):
- P1. Signed column sums: P(x,-1) = 1, i.e. sum over column a of (-1)^b = delta_{a,0}.  Signed row sums: P(-1,y) = (-1)^{a_0} y^{b_0}
      (only the row of x_0 survives).
- P2. k/4 = sum over specials (vertical dominoes) of (-1)^{b_bot} = -sum_N b (-1)^b = d/dy P(1,y) at y = -1   [determinant relation, = J'(-1) = 0].
- P3. 2j + k/4 = sum over specials of (-1)^{a+b_bot} = d/dy P(-1,y) at y=-1   [from dJ/dt(1) = -8j with J = t^k P(-t,-t^4)].
- P4. A unit square with lower left corner (a,b) contributes 0 to P3 and 2(-1)^b to P2. Hence, writing s_sq := sum over squares of (-1)^b:
          l_s = 2j + k/4 (staircase only),   k/4 = k_stair/4 + 2 s_sq,   j = j_stair - s_sq,
      where a pure staircase of signed length l_s has k_stair/4 = -(l_s mod 2) for type "+", +(l_s mod 2) for type "-", j_stair = (l_s - k_stair/4)/2.
  So the pair (j,k) is equivalent to the pair (l_s, s_sq): signed staircase length and delta-signed number of squares.

## 2. Classical shadow of N (task 4): what is PROVED, with proofs or proof routes

Notation: P(x,y) = sum over N of x^a y^b (rho at the origin), J(t) = t^k P(-t,-t^4); Q_1(x,y) = generating function of the bottoms
(a_i,b_i) of the vertical dominoes (= special components), so P = 1 + (1+y) Q_1.  [T] = y.1 + x.e in TL_2 (horizontal direction),
y = uJ, y + delta x = u.

- S1 [PROVED, elementary TL_2 computation; checked on T(3,5) and P(-2,3,7) for the trefoil]. Jones polynomials of the closures
  K_n = T(1/n) (branch sets of S^3_{1/n}(K)):
        V_{K_n}(t) = t^{-12 j [n odd]} { 1 + (1 - (-t)^n) (1 + t + t^2)/(1+t)^2 (J(t) - 1) }      (up to t <-> 1/t and the sign of n).
  The monomial t^{-12j} for odd n is the writhe change between the two orientations of T (the two strands have "linking number" 4j).
- S2 [PROVED from S1 + CITED Mullins (Topology 32 (1993), formula lambda(Sigma_2(L)) = -(1/12) d/dt log V_L(-1) + sigma(L)/8, recalled) +
  CITED Casson surgery formula lambda(S^3_{1/n}(K)) = n a_2(K) (recalled)]:
        (a)  J''(-1) = -24 a_2(K)        (a_2 = Conway coefficient of the knot upstairs; Arf(K) = a_2 mod 2),
        (b)  sigma(K_n) = -8j for n odd,  sigma(K_n) = 0 for n even   (sign convention of the table).
  Reason: write J - 1 = (1-t^4)(1+t^3) R(t). Then V'_{K_n}(-1) = -12 n R(-1) plus, for n odd, the contribution -12j(-1) of the
  monomial; Mullins + Casson for one even n give R(-1) = -a_2(K), i.e. (a); then Mullins + Casson for odd n force the signature term to
  cancel the monomial term, i.e. (b).  DATA: (a) holds exactly in all 132 table cases (script mullins.py; zero residual).
  A second, independent route to (b) is Gordon-Litherland applied to the surface (disc of the unknot T(infinity)) + (band along the arc
  alpha) in B^4, whose double branched cover is the surgery trace; it gives sigma(T(n)) = sigma(U(n)) - 8j for every integer n with the
  braid-like orientation (U = trivial tangle), not written out in full here.
- S3 [PROVED, consequence of S2b + Rokhlin]: j = Arf(K) mod 2 (Rokhlin invariant of S^3_1(K) is Arf(K) and equals sigma(K_1)/8 mod 2).
  DATA: all 132.  So j is an integer lift of the Arf invariant depending on the inversion: j = -sigma(K_1)/8, the mu-bar type invariant
  of (S^3_{+1}(K), induced involution). For the Montesinos involution on a Seifert homology sphere it is the Neumann-Siebenmann invariant.
  Example: S^3_{+1}(4_1) = Sigma(2,3,7) with its two involutions (branch sets T(3,7) and P(-2,3,7), signatures of opposite sign) <-> j = +1, -1.
- S4 [PROVED from P = 1 + (1+y)Q_1]. In the lattice:
        J'(-1) = 0      <=>   k/4 = sum_i (-1)^{b_i},
        J'(1) = -8j     <=>   2j + k/4 = sum_i (-1)^{a_i+b_i},
        J''(-1) = -24a_2 <=>  3 a_2(K) = k(k+4)/8 + sum_i (-1)^{b_i} (a_i + 4 b_i).
  The last identity pins the delta-signed first q-moment of the special components relative to rho by the classical invariant a_2(K).
  Checked by hand on 3_1, 4_1, T(2,2g+1), T(3,4), T(3,5), P(-2,3,7).
- S5 [PROVED]. Flat (J = 1) forces j = 0 AND a_2(K) = 0 (the second is new relative to the brief; it is Mullins + Casson).
- S6 [route, first step PROVED]. x_0 (generator of H(d_D)) has h = 0: the complex (N (x) F[D], d_D) is C(T) (x)_B B/(c) = the complex of
  b-resolutions with the dot of the non-special strand kept; inverting D it is Lee/Bar-Natan homology of T with the two strands coloured
  differently, which is one-dimensional and generated by the canonical generator of the orientation in which the strands are parallel
  (adjacent parallel arcs carry different colours); this generator sits in homological degree 0 for that orientation, which is kht++'s.
  rho is the generator of Kh~(T(infinity)) = F shifted by k D: (h,q) = (8j + k, 24j + 2k); the shift (8j,24j) is the usual
  (2 lk, 6 lk) shift between the two orientations of T with lk = 4j.

CORRECTION to S1 (sign conventions, fixed after checking against the published Jones polynomials of T(3,5) and P(-2,3,7)):
in kht++'s variable t = q^2 (positive knots have positive exponents), with J = t^k P(-t,-t^4),
        V_{K_n}(t) = t^{12 j [n odd]} { 1 + (1 - (-t)^{-n}) (1 + t + t^2)/(1+t)^2 (J(t) - 1) },   n = +-1, +-2, ...
(for the table's 3_1, j = 1, J - 1 = t^{-7}(1-t^4)(1+t^3): n = 1 gives t^4 + t^6 - t^10 = V(T(3,5)), n = -1 gives V(P(-2,3,7)).)
S2(b) stands as written: sigma(K_n) = -8j for n odd, in the convention "positive knots have negative signature".

## 3. The dictionary (tasks 1-2): what N(K,h) is in knot Floer / classical terms

### 3.1 Statement
Let mu_1(K) := sum over x in HFK^(K) of (-1)^{M(x)} M(x) = signed number of vertical arrows of CFK(K), signed by the Maslov parity of
the source (PROVED equal: a vertical pair x -> y has M(y) = M(x) - 1). For thin knots mu_1 = tau = -sigma/2; for L-space knots
mu_1 = (rank HFK^ - 1)/2 = number of vertical steps of the staircase (NOT the genus); mu_1 is additive under connected sum.

  DICTIONARY (DATA unless marked; "collapse" = dim N = rank HFK^(K), true in 131 of 132 table cases, all doubles, all torus/pretzel cases below)
  (a) dim N(K,h) >= rank HFK^(K)   [Theorem S of the brief], with equality in the collapse case.
  (b) k = 4 mu_1(K).   Independent of the inversion.  [H3; CONJECTURED in the collapse case.]
      Evidence: 129 thin table cases (k = -2 sigma = 2s), 8_19 (k = 8 = 4*2, while 2s = 12: so k is not 2s in general),
      9_42 (k = 0), 21 doubled tangles (k = -4 sigma(K) = 4 mu_1(K # K)), 101 two-bridge quotients with denominators up to 45
      (|k| = 2|sigma|, signature from Murasugi's formula), T(2,2g+1) for g <= 7 (k = 4g), T(3,5), P(-2,3,7), P(-2,3,9)
      (k = -12, -16, -20 = -4 x number of vertical steps; computed here, files torus.jsonl, pretzel.jsonl). No exception except
      9_46 second inversion, where dim N = 15 > 9 and k = -4 instead of 0.
      PROVED for T(2,2g+1), T(3,4), T(3,5): Theorem S gives 1 + 2m >= rank HFK^, Watson's bound dim kappa = 4m <= pq - 1
      (CITED [W, Theorem 18], from the digest lit/kwz-inversions, not reread) gives the reverse, and the lens space surgery pq + 1
      (T(pq+1) two-bridge, thin of rank pq + 1 = 4m + |pq + 1 - k|) gives k = 4m.
  (c) j = -sigma(K_n)/8 for every odd n (K_n = T(1/n) = branch set of S^3_{1/n}(K))   [PROVED, S2].  Depends on the inversion.
      j = Arf(K) mod 2 [PROVED].  For L-space knots with some quasi-alternating closure T(n) (all torus knots): j = -V_0(K)
      [PROVED from CITED Manolescu-Owens/Lisca-Owens d = -sigma/4 for the spin structure of a quasi-alternating link and the
      Ni-Wu d-invariant surgery formula, both recalled]; DATA: T(2,2g+1): |j| = ceil(g/2) = V_0; T(3,4): 1; T(3,5): 2; P(-2,3,7): 2; P(-2,3,9): 3.
      So j is the signature-type ("mu-bar type") counterpart of the equivariant V_0 / d-invariants of (S^3_{+1}(K), h) studied by
      Dai-Mallick-Stoffregen (arXiv:2201.01875, not reread): equal to -V_0 when everything is thin, different in general
      (4_1: j = +-1 for the two inversions, V_0 = 0).
      NEGATIVE: j is not the g-signature sigma-tilde of Alfieri-Boyle (CITED arXiv:2109.09915v1, read now: Example 7.4 gives
      sigma-tilde(T(2,2n+1)) = -2n for the direction of their Figure 8, Example 7.1 gives -6 and -10 for the two directions of one
      inversion of 7_4; their invariant depends on a direction, j does not).  Sakuma's eta: no relation found; eta vanishes for
      amphicheiral knots with a unique inversion while j = +-1 for 4_1's two inversions.
  (d) Shape:  N = (staircase of signed length l_s) + (dim N - 2|l_s| - 1)/4 unit squares,   l_s = 2j + k/4 = mu_1(K) + 2 j(K,h).
      The staircase of CFK(K) (thin K) has signed length tau = mu_1. So N has the CFK shape exactly when j = 0
      (5_2 second inversion, 6_1 second, 8_3, 8_20, 9_42, 9_46 first, all doubles), and the discrepancy is the signature 2j = -sigma(K_n)/4
      (4_1: 0 + 2 = 2, five-staircase; T(2,5): -2 + 2 = 0, point + square; 5_2 first: -1 + 4 = 3, seven-staircase).
      This answers "the shape depends on the inversion".
  (e) Parity: the delta-parity (-1)^b of a special (vertical domino) corresponds to the Maslov parity of the source of a vertical arrow:
      the numbers of specials on even and on odd levels are (m + k/4)/2 and (m - k/4)/2, and (b) says these are the numbers of
      vertical arrows with even and odd source. A square of N carries two dominoes of the SAME parity (it contributes +-2 to k/4), a box
      of CFK two arrows of OPPOSITE parity: squares are not boxes. Two squares at offset (-1,+1) (a "(1+y/x)-pair") count like two boxes;
      one square alone counts like two staircase arrows (torus knots).
  (f) First moment: sum over specials of (-1)^{b_i}(a_i + 4 b_i) = 3 a_2(K) - k(k+4)/8   [PROVED, S4].
      Compare CFK: a_2 = tau^2/2 + sum over vertical arrows of (+-1) l (A_source - l/2). So on signed average the quantum position
      a + 4b = q/2 of a special plays the role of 3 x (Alexander grading of the source): the step 6 in q of the brief is the step 1 in A.
  (g) Rows: N lies on two adjacent delta-levels in all L-space examples (torus knots, P(-2,3,7), P(-2,3,9)) [Watson's Conjecture 30 is
      the general statement]. For thin knots the number of levels depends on the inversion (twist knots: (det+1)/2 for one inversion,
      3 for the other); no formula found.  NEGATIVE: no linear function of (a,b) reproduces the Alexander grading, even for 4_1
      (proof: the five values on the 5-staircase would have to be {1,0,0,0,-1}; impossible for an affine function).
  (h) The Alexander-side analogue of N is not HFK^(K) but the sutured Floer homology of the quotient theta-curve:
      (D x I minus T, sutures) = (S^3 minus nu(theta), one meridional suture per edge) [PROVED identification of manifolds]; its Euler
      characteristic is the Alexander polynomial of the theta-curve (Litherland), and the one-variable analogue of J is the Conway
      polynomial of the two-component link T(0) (linear coefficient = linking number = -+4j). Three objects, three expected maps:
      N => HFK^(K) (Theorem S), HFK^(K) => SFH(theta) (Smith-type localisation for the double cover, expected),
      N => SFH(theta) (Dowlin-type, expected).  Not used further.

### 3.2 Families computed here (L-space knots; all on two levels, so N is given by the multiset {a_i} of the specials, rows b = -1, 0)
  knot (negative chirality)   k    j   specials' a_i          staircase of CFK (step lengths)
  T(2,2g+1), g = 1..7        -4g  ceil(g/2)  1,2,...,g       1,1,...,1
  T(3,4) (two diagrams)       -8   1   -2,-1                 1,2,2,1
  T(3,5)                     -12   2   -1,0,1                1,2,1,1,2,1
  P(-2,3,7)                  -16   2   0,1,1,2               1,2,1,1,1,1,2,1
  P(-2,3,9)                  -20   3   1,1,2,2,3             1,2,1,1,1,1,1,1,2,1
  T(2,7) and T(3,5) have the same (k,j) and dim but different N: the positions of the specials see the lengths of the CFK arrows.
  The identity (f) holds in each line (a_2 = g(g+1)/2, 5, 8, 12, ...).
  J for T(2,2g+1) has exactly 7 monomials for g >= 4 (the two rows cancel almost completely; the extremes come from one row each).

(Full table: `dictionary/table.tsv`, 132 rows + doubles; columns N-shape, CFK-shape, s, sigma, det, a_2, mu_1, checks of (b) and of j = Arf mod 2.)

Proof of S1 (for the record). In TL_2 = <1, e>, e^2 = delta e, delta = -A^2 - A^-2, write [T] = y 1 + x e, y = uJ, y + delta x = u.
sigma^n = A^n 1 + beta_n e with A^n + delta beta_n = (-A^-3)^n. The tangle of n vertical half twists is the rotation A^n e + beta_n 1.
With the pairing G(1,1) = G(e,e) = delta^2, G(1,e) = delta:  <K_n> = A^n(y delta + x delta^2) + beta_n (y delta^2 + x delta)
= delta u [ (-A^-3)^n + beta_n (delta - 1/delta)(J - 1) ].  Divide by the value for J = 1 and use delta^2 = (1+t)^2/t, -A^4 = -t^{-+1}:
<K_n>/<unknot_n> = 1 + (1 - (-t)^{+-n}) (1+t+t^2)/(1+t)^2 (J-1). The remaining monomial is the writhe difference between the
orientation of T used for the unknot closure (strands antiparallel) and the one of K_n for n odd (parallel): 16j crossings-signs, i.e. t^{12j}.
Checked against four published polynomials: 3_1 gives V(T(3,5)) and V(P(-2,3,7)); 4_1 (first inversion) gives V(P(-2,3,7)) and V(T(3,7)).
(So S^3_{+-1}(4_1) = +-Sigma(2,3,7) is the double cover of P(-2,3,7) and of T(3,7), both positive, both of signature -8 = -8j.)

## 4. NP on the Floer side (task 3)

### 4.1 Translation and verdict
- In the lattice q/2 = a + 4b + const, delta = -b. NP: the generators of maximal (minimal) a + 4b lie in one row. In a fixed q-degree the
  h-parity equals the delta-parity up to a global sign, so END says: the top q-degree part of N has non-zero delta-Euler characteristic.
- Under the dictionary the delta-parity is the Maslov parity [3.1(e)]. Hence, IF the top q-degree of N corresponded to a sum of full
  Alexander gradings of HFK^(K), END would read "the corresponding coefficients of Delta_K do not cancel", e.g. for the top Alexander
  grading: deg Delta_K = g(K).  This Floer statement is FALSE (every knot with Delta = 1; Whitehead doubles, Kinoshita-Terasaka).
  On the Floer side the top group HFK^(K,g) is always non-zero (genus detection) but its Euler characteristic can vanish;
  NP/END assert the opposite pattern for N: the Euler characteristic of the extreme q-degree never vanishes.
- VERDICT (negative, with reason): NP has no valid Floer-side counterpart, and no grading-compatible dictionary N <-> HFK^ can exist that
  sends extreme q to extreme Alexander degree; a mechanism for NP cannot be imported from knot Floer homology through gradings.
  What the Floer side does supply is a REALIZATION input (section 5.2): N is the E_2 page of a spectral sequence to HFK^ of an actual knot.
- The only grading statement available: Theorem S's differentials should have Szabo-type bidegrees (r, 2r-2), r >= 2, i.e. lattice
  degree (r-5, 1): they raise q, so the top q-degree of N consists of permanent cycles and the bottom q-degree is never hit.
  [CONJECTURED; supported by the one non-collapsing case: in 9_46 second inversion cancelling the three pairs of arc generators at
  offset (-1,1), bidegree (4,6), r = 4, leaves point + 2 squares = the mirror of N(9_46 first inversion); no other choice of three
  pairs with offsets (r-5,1) leaves a point + (1+y/x)-pair of squares.]

### 4.2 The natural counterexample family: Alexander polynomial one (files lit/kht/out/alex1/runs.jsonl, runs2b.jsonl, runsB.jsonl; analysed with rec.py)
Three classes are computed (runs2a timed out). In all three j = 0, NP and END hold, and a_2 = 0 is confirmed by S2.
  class A  (word s.r1.y0.x2.r3.y0.y2.u1.x2.x2.y0.y1.x0.u1): k = +-4, dim N = 31 = 3-staircase + 7 squares at
           (-2,0),(-1,-1)^2,(-1,0),(0,-2),(0,-1),(1,-2); Pi = t^-8 - t^-7 + 2t^-5 - t^-4 + t^-2 - t^-1.
           Knot itself: Kh~ of rank 31, s = 2 (knot-mode kht++, here). So tau is probably +-1 = k/4, consistent with (b).
  class 2b (word s.l1.y0.y2.r3.x2.y1.x0.y2.y2.u1.x0.x2.x0.u1): k = 0, dim N = 17 = point + 4 squares at (-1,1),(0,0),(0,0),(1,-1):
           N - rho = x y^-1 (1+x)(1+y)(1+y/x)^2,   Pi = t^-3 (1+t^3)^2  (all four squares have the SAME sign in J).
           Knot itself: Kh~ of rank 33, s = 0; so dim N < dim Kh~(K): N is not bounded below by Kh~ of the knot.
  class B  (word s.l1.x0.y1.x0.y1.l1.y4.y4.x1.y0.y3.u2.y2.y0.u1): k = 0, dim N = 65 = point + 16 squares:
           N - rho = x^-1 y^-1 (1+x)^3 (1+y)(1+y/x)^2,   Pi = t^-5 (1-t)^2 (1+t^3)^2.   Knot itself: Kh~ of rank 65, s = 0.
Reading.
- For 2b and B the generating function of N - rho is a PRODUCT of dominoes in the three directions D = (1,0), P = (0,1), P - D = (-1,1)
  [(h,q) = (1,2), (5,8), (4,6)]; the Newton polygon is the zonotope they span, so the extreme q-degrees are single generators.
- The Floer cancellation is visible but displaced: k = 0 forces as many squares on even as on odd levels (P4), which is the shadow of
  "boxes cancel in Delta". The squares of opposite delta-parity are paired by the factor (1 + y/x), offset (-1,+1), bidegree (4,6);
  a cancellation in J needs offset (-4,+1), bidegree (1,0). In the 132 table tangles NO two squares sit at offset (-4,+1)
  (offsets between squares on adjacent levels: -3: 26, -2: 364, -1: 808, 0: 154); in the doubled tangles the offset -4 occurs 327 times,
  always inside a larger cloud.
- Ranks are those of Whitehead doubles by Hedden's formula (recalled, not reread): 17 = point + 4 boxes is the rank of the untwisted
  double of a genus-one knot with tau <= 0 (e.g. of 4_1 or of the left trefoil), 15 that of the double of the right trefoil; 31 and 65
  fit doubles of T(2,5) and of a genus-one knot of determinant 17. The three knots are NOT identified; this is a guess to be checked.
- So the test "where the Floer side cancels" is passed with room to spare, and it suggests a sharper statement to prove:
  for a symmetric satellite, N - rho is a product of dominoes in directions D, P, P - D (CONJECTURED from two examples).

### 4.3 Flatness is inherited by satellites [PROVED, skein functoriality]
If (K,h) is flat, then for every tangle R in the complementary ball the link T_K u R has the Kauffman bracket of Q_0 u R (the skein
module of the ball with four marked points is TL_2, and gluing R is linear). Two consequences:
 (i) for every pattern P in the solid torus that is invariant under the standard involution, J(P(K), h) = J(P(U), h)
     (cables: J(K_{p,q}) = J(T(p,q)); patterns with P(U) = U, e.g. Whitehead doubling: the satellite is flat again);
 (ii) for every strongly invertible (K',h'), the knot T_K u (T_K' rotated by a quarter turn) has Jones polynomial 1 and its double
     branched cover is a splice of the exteriors of K and K'.
Applying S2 to (i) gives nothing beyond a_2(K) = 0 (a_2 of a satellite is a_2(P(U)) + w^2 a_2(K)); signatures give nothing beyond j.

## 5. Results for classes, and the realization input

### 5.1 THEOREM T2 (two levels)  [PROVED from (V) and (H) below]
(V) N = {rho} + vertical dominoes {(a_i,b_i),(a_i,b_i+1)} (special components; structure theorem of the brief).
(H) H(N (x) F[D], d_D) has rank one over F[D]; hence N minus one generator is a union of pairs at lattice offset (5e-4, 1-e), e >= 1
    (a D^e-arrow has bidegree (1,2e)).  [S6; e = 1 in all data except one e = 2.]
THEOREM. If all special components lie on one delta-level (N on two adjacent levels, kappa(K,h) in a single delta-grading), then J != 1
unless T is rational.  In particular Lemma Q holds for strongly invertible torus knots (Watson: kappa in one grading, CITED via the digest)
and for every L-space knot for which Watson's Conjecture 30 holds; DATA: P(-2,3,7), P(-2,3,9), P(-2,3,11), P(-2,3,13) have two levels.
Proof. Let b_0 be the level and R_1(x) = sum x^{a_i}. J = 1 means 1 + (1-t^4)(-t^4)^{b_0} R_1(-t) = t^{-k}. For k = 0 this gives R_1 = 0.
For k != 0, (t^{-k} - 1)/(1-t^4) is +-(t^{4c} + t^{4c+4} + ...), a sum of |k|/4 distinct monomials of one sign, so (R_1 has non-negative
coefficients) R_1(x) is a sum of distinct monomials x^{4c}: the special components sit at pairwise distinct a = 0 mod 4 on one level.
Then no two generators of N differ by (5e-4, 1-e) with e >= 1: within a row the offset would be (1,0); between the two rows of the
dominoes it would be (6,-1); between rho and a domino generator a short case check (e = 0 mod 4 forces the wrong position) excludes it.
So d_D = 0 and (H) gives dim N = 1.  QED
Remarks. (1) Sharp: the formal flat object B1 below has special components on two levels. (2) END itself can fail formally on two levels
(rho + one square at (4,-1): J = t^-7 + t^-4 - t^-3, bottom degree cancelled); that object would need a knot with rank HFK^ <= 5 and
a_2 = 1, i.e. the trefoil, whose N has dimension 3; so it is excluded by 5.2, not by algebra.

### 5.2 The realization input that B0 violates (partial mechanism)
INPUT (all PROVED or CITED): a formal N determines k, j (S4) and a_2 := (k(k+4)/8 + sum (-1)^{b_i}(a_i+4b_i))/3. If N = N(K,h) then
  (R1) rank HFK^(K) <= dim N and g(K) <= m = (dim N - 1)/2   [Theorem S];
  (R2) a_2(K) = a_2(N), Arf(K) = j mod 2                      [S2, S3];
  (R3) K is non-trivial as soon as N != {rho}.
Formal flat objects: B0 = rho + squares at (0,0) and (-4,1) (dim 9, k = j = 0), and the smaller
  B1 = 3-staircase (0,0),(1,0),(1,-1) + one square at (-4,0)   (dim 7, k = 4, j = 0;  t^4 [1 - t + t^-3 + (1-t)(1-t^4) t^-4] = 1).
Both satisfy (V), (H), the shape law, and a_2(N) = 0.
CONSEQUENCE [PROVED given the input]. A knot realizing B0 (resp. B1) has a_2 = 0, genus <= 4 (resp. 3) and sum of |coefficients of
Delta_K| <= 9 (resp. 7); a short enumeration (a_1 + 4a_2 + 9a_3 + 16a_4 = 0 with the size bound) leaves only Delta_K = 1.
So B0/B1 require a NON-TRIVIAL knot with Delta = 1 and rank HFK^ <= 9 (resp. <= 7).
 - B1 (rank <= 7): in genus one the ranks would be (2,1,2) or (2,3,2), a nearly fibered genus-one knot with Delta = 1; these are
   classified and all have Delta != 1 [CITED: Baldwin-Sivek, Floer homology and non-fibered knot detection, arXiv:2208.03307,
   recalled, statement number not checked]. In genus 2 or 3 the knot would have HFK^ supported in Alexander gradings +-g and 0 only,
   with ranks (2, 0,.., r_0 <= 3, ..,0, 2): no such knot is known and I know no theorem excluding it.
 - B0 (rank <= 9): genus one would need ranks (2,r_0,2) (excluded as above) or (4,1,4); genus >= 2 ranks (2,a,..,r_0,..,a,2), a in {0,2}.
   None is known: the smallest known rank of a non-trivial knot with Delta = 1 is 15 (untwisted Whitehead double of the trefoil).
So B0 and B1 are excluded as N of an actual knot unless there is an exotic knot with Delta = 1 and rank HFK^ <= 9; this is a genuine
realization input (a statement about the knot upstairs) and it uses nothing that B0 satisfies formally. It is NOT a proof that B0, B1
do not occur: that would need the classification of knots with Delta = 1 and rank HFK^ <= 9.
LIMIT (proved negative for this lens): the input bounds flat objects from below (any flat (K,h) has a_2(K) = 0 = Arf(K) and
dim N >= rank HFK^(K) >= 5) but cannot exclude large ones: for every knot K_0 with a_2 = 0 the object "N-shape of rank HFK^(K_0)
plus extra J-cancelling squares" passes (R1)-(R3). A complete mechanism needs more than ranks, parities and the Casson invariant.


### 5.3 Two-level arithmetic and a sharp test on torus knots [PROVED relation; test running]
For N on two adjacent levels with unit D-arrows (all data), (V) + (H) + J'(1) = -8j give  sum_i (-1)^{a_i} in {0,-1} and hence
        |j| = ceil(m/2),     m = number of special components, dim N = 1 + 2m.
Checked: T(2,2g+1) (m = g), T(3,4) (2;1), T(3,5) (3;2), P(-2,3,7) (4;2), P(-2,3,9) (5;3), P(-2,3,11) (6;3), P(-2,3,13) (7;4).
With j = -V_0(K) (3.1(c)) this reads  dim N = 4 V_0 + 1 or 4 V_0 - 1  for L-space knots.  Comparison with (b)/(a):
collapse (dim N = rank HFK^) requires the number n_v of vertical steps of the staircase to be 2V_0 or 2V_0 - 1.
True for T(2,n), T(3,n) (n <= 11 checked by hand from the semigroups), P(-2,3,q).  FALSE for T(4,5): n_v = 3, V_0 = 3, and Watson's bound
gives m <= 4, Theorem S gives m >= 3. So for T(4,5) at least one of {collapse, unit D-arrows, j = -V_0} must fail (an elementary
case check shows m = 3, j = -3 is impossible on two levels even with D^2-arrows). T(4,5) is therefore the smallest sharp test of the
dictionary; a symmetric diagram in kht++ form is s.l1.x0.l1.x0.y4.y4.y3.y2.y3.y4.x0.u1.x0.u1 (5-braid form
s2 s4 . g . s4 s2 . rev(g), g = s1 s1 s2 s3 s2 s1, Alexander polynomial of T(4,5) checked; file torusw.py). Result: see section 6.


## 6. What d_D is on the Floer side: the Smith differential of the inversion (CONJECTURED; the hypothesis of task 2 about Dai-Mallick-Stoffregen)

Convention fix for 3.1: mu_1 is the signed number of vertical arrows of CFK(K) with sign (-1)^{M(target)}, so that mu_1 = tau for thin
knots (with honest Maslov gradings sum (-1)^M M equals -mu_1). The sign in "k = 4 mu_1" is then the one of the table.

- FACT [PROVED]. On N the two differentials have different parity behaviour: d_P is odd for the delta-parity, d_D is EVEN for it
  (D preserves delta). The Grigsby-Wehrli spectral sequence respects the delta-parity = Maslov parity. So under N = HFK^(K), d_D can
  only correspond to an even operator of square zero with one-dimensional homology. It is therefore NOT the horizontal differential
  (odd), and (N (x) F[D], d_D) is not HFK^-: e.g. T(3,4) has a horizontal arrow of length 2 while N has only unit D-arrows.
- CANDIDATE. Over F_2 the operator 1 + tau_K, tau_K = action of the strong inversion on HFK^(K) = SFH(S^3 - nu K) (Dai-Mallick-Stoffregen),
  is even, squares to zero, and its homology is the Tate homology of the involution, which the localisation theorem for the branched
  double cover Sigma(D x I, T) = S^3 - nu K (Hendricks / Lipshitz-Treumann / Large type, recalled) should identify with SFH(D x I) = F.
  On the Khovanov side the Lee/Bar-Natan spectral sequence N (x) F[D] => F[D] plays the same role (D <-> the Tate variable theta;
  unit D-arrows <-> collapse at 1 + tau; a D^2-arrow <-> a higher localisation differential; the Lee generator x_0 <-> the tau-fixed class,
  which lies in Alexander grading 0).  This is the knot-level version of "Lee spectral sequence = localisation for the covering involution".
- CONSEQUENCE IF TRUE: the shape of N is the graph of two matchings on a basis of HFK^(K): P-dominoes = pairs of a tau-invariant
  differential with homology F, D-dominoes = tau-orbits; the zigzag is the path from the survivor of the first to the tau-fixed class,
  squares are 4-cycles. In particular the dependence of N on the inversion is the dependence of tau_K on the inversion.
- CHECKS (by hand).
  3_1: CFK = a <- b -> c, tau swaps a,c: d = (b -> a + c), 1 + tau = (a -> a + c): path b, a+c, a: the 3-staircase. OK.
  4_1 (CFK = isolated p + box x -> y, x -> z, y -> w, z -> w): vertical pairs (x,z), (y,w), survivor p. tau swaps y and z; on Alexander
       grading 0 it must pair p with a corner of the box (this is what DMS find for the two inversions, recalled: the isolated
       generator is moved by a box corner, differently for the two inversions). Path p - w - y - z - x: the 5-staircase, for both
       inversions (mirror images). If tau fixed p the shape would be point + square, the CFK shape. OK.
  T(2,5): tau is forced (x_i <-> x_{4-i}). With the vertical differential the graph is a 5-path, but N is point + square. With the
       differential of A_0 = C{max(i,j) = 0} (the large surgery complex of the spin structure, which IS tau-invariant):
       pairs (x_1,x_0), (x_3,x_4), survivor x_2 = the tau-fixed class, and the tau-orbits (x_0,x_4), (x_1,x_3) close a 4-cycle: point + square. OK.
  So the first differential must be taken tau-invariant (N is a module over the commutative ring Lambda; the vertical differential
  does not commute with tau). For L-space knots the natural candidate is (A_0, tau) with H(A_0) = F; for 4_1, H(A_0) has rank 3 and the
  vertical complex was used. A uniform statement is NOT found: "N = associated graded of (a tau-invariant model of CF^(S^3) filtered
  by K; 1 + tau)" is the working form.  This is the most concrete entry of the dictionary and is checkable against DMS's tables.
- If this holds, j (the mismatch between the staircase of N and that of CFK, l_s = mu_1 + 2j) measures how far the tau-fixed class is
  from the survivor of the knot filtration: an equivariant correction, in line with j = -sigma(K_n)/8.

