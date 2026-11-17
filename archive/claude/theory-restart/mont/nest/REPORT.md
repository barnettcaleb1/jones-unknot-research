# Lane NEST: report (16 Nov 2026)
Folder: ~/jones-lanes/theory-restart/mont/nest/   Scripts: nest/*.py (run with tools/venv/bin/python from mont/)
Status legend: PROVED / CHECKED(n) / CONJECTURE / GAP.

## 0. Status summary (final, 16 Nov 2026)
- (1) OUTER MAP: DONE (and this proves Theorem N modulo the TH-2BR dictionary). v_N = t^(2m(1-eps)) X^(-m) p, eps = (-1)^(#axis letters) = b(p)(-1). CHECKED 60 single + 25 depth-2 + 40 depth-3 exact; skein proof sketch (nested-cap slide) + unit forced by normalisation.
- (2) CLASS: DONE. Lift dictionary (rational boxes = odd rational tangles, * = tangle sum, F_m = symmetric even twist, closure = D); depth 1 = Montesinos N(T_1+..+T_n+1/2m), rho_h; iterated = arborescent D(T), T in C; every Montesinos knot with exactly one even tangle (rho_h) is reached; dihedral inversions (e.g. vertical P(p,q,p)) are not. 2-bridge: both inversions reached. Converse characterisation CONJECTURE.
- (3) TWIST-2CH: DONE. T_n ~ s.r2.(y1)^(n+1).B.u1, B = y0.r2.y0.y1.y0.y1.x2.u1 (non-rational box, s.B = trefoil, eps=-1); J(T_n) = t^(4n+4)P_B + (-1)^(n+1)t^(3n+3)Q_B, P_B = t^-15(t^2-t+1), Q_B = J(3_1)-P_B. CHECKED n=-3..5.
- (4) VERTICAL: DONE (formula DERIVED: 3 channels + prism admissibility + a=+-1 necklace values + a=0 partial trace + Corollary S force it, units included). J(s.l1.B.(x2)^a.u1) Phi_3 =. tA + (-t)^a((1+t^2)A + tB) + t^(3a-1)Phi_5 B (3 arc-pair channels, 4 terms; zeros = prism admissibility). CHECKED 350 pinned + 220 direct. Bonus (Corollary S): the swap inversion of K#K has J = coloured Jones J_3(K) (PROVED; CHECKED 3_1, 4_1), so Lemma Q contains 'J_3 detects the unknot'.

## 1. Outer map F_m
Notation: for a body B (word without 's.', one half-strand in, one out, s.B a knot) v_B = pinned vector (v_1 = J(s.B), v_2 fixed by
the twisted closures m = 1, 2, -1 as in test_general2.py). n_0(B) = number of axis letters (x0, y0) in B.
eps(v) := b(v)(-1) = v_1(-1) + 2 v_2(-1).

THEOREM O (outer map). Let N = r2.(y1)^m.B_1...B_n.u1 and p = v_1 * ... * v_n. Then
      v_N = t^(2m(1 - eps(p))) X^(-m) p,
i.e. F_m = X^(-m) on boxes with eps = +1 and F_m = t^(4m) X^(-m) on boxes with eps = -1. First row e_1^T X^(-m) (unit 1 or t^(4m)),
second row (0, (-t)^(-m)) times the same unit. eps is multiplicative (eps(v*w) = eps(v) eps(w)) and eps(v_N) = eps(p).
Status: CHECKED. (a) single boxes: 60/60 exact (12 random non-rational boxes x m in {1,-1,2,-2,3}; the pinned vector of N computed
from scratch and compared with X^(-m) v_B: ratio is exactly t^(4m) when n_0(B) odd and exactly 1 when n_0(B) even).
(a') exact units for several boxes (pinned vectors from scratch, nest/p1_units.py): v_{B1.B2} = v_B1 * v_B2 EXACTLY (no unit) 10/10, and
the 2-box body r2.(y1)^m.B1.B2.u1 has pinned vector exactly t^(2m(1-eps(p))) X^-m (v_B1 * v_B2) with eps(p) = eps(v_B1) eps(v_B2) 10/10.
(b) nested necklaces, prediction = normalize(first entry of the recursively computed vector), compared with direct J of the full word:
depth 2: 25/25 exact; depth 3: 40/40 exact (random mixtures of twist rows +-1, +-3, +-5 and random non-rational flat_search bodies,
twists m in {+-1, +-2}, up to 3 children per node; widths up to 9 half-strands). Logs: nest/p1_nest.log, nest/p1_nest3.log.
(c) parity: eps(v_B) = (-1)^(n_0(B)) for all 50 boxes of general_boxes.json. CHECKED(50).
(d) realisation of arbitrary 2-bridge words by nesting (section 2): 728/728 exact. Unit-J cases met in the nesting tests
(s.r2.x1.r2.y1.y1.r1.y0.y2.u1.u1.u1 and one depth-3 word) reduce by the calculus to 2-bridge words (F_{-2} F_2 = id, inner box
rational, e.g. inner body r1.y1.y0.y0.x1.x2.u2 has vector X Y^2 e_1) with J = 1, hence unknots by TH-2BR; Alexander/det trivial.

Why (skein picture). Identify a box state beta in End(V_1 (x) V_2) with the vector v = beta e_1 in H = Hom(V_1, V_1 (x) V_2 (x) V_2),
where e_1 = id_{V_1} (x) coev_{V_2} is the identity box with its west arc end w bent down to a fourth point w* (so H has the points
W | E, e, w*). In N^# = N e_1 the arc runs  w* -> (cap) -> strand 0 -> [twist with strand 1] -> beta -> (cup u1) -> strand 1 -> (cap r2)
-> strand 2 -> e.  Strand 0 sits under the outer cap (w*, strand 0) and strand 1 under the inner cap r2 (strand 1, strand 2): the two
caps are NESTED. A crossing y of the two left legs of a pair of nested caps slides through the caps to a crossing of the two right
legs with the SAME letter (check: the vertical smoothings correspond, s0<->w*, s1<->s2, and the horizontal ones correspond, so the
A/A^-1 weights agree only for the same letter). The right legs are strand 2 and w*, which then run straight down to the output points
(e, w*) of H. Hence N^# = sigma^m (beta e_1) with sigma the y-type half twist of the two ARC points of H, and after the twist is moved
away the remaining picture is the zig-zag r2 ... u1 = identity. By the TH-2BR dictionary sigma = X^-1 (this is the same twist that the
necklace closure dictionary 'y1 <-> X^-1' records). So v_N = X^-m v_B up to a unit. PROVED at the bracket level modulo the
identification of (H, X, e_1) with TH-2BR (which the brief takes as checked).
The unit. Normalisation is J = 1 mod (t+1)^2. X = I mod (t+1) and e_1^T X^(-m) e_2 = (1-t)(1+t^2)(1-(-t)^(-m)) has value 0 and
derivative -4m at t = -1, so e_1^T X^(-m) p = 1 - 4m p_2(-1) (t+1) mod (t+1)^2. With p_2(-1) = (eps - 1)/2 the normalising unit is
t^(2m(1-eps)) with sign +1. So once v_N is proportional to X^(-m) p (skein argument) the unit is FORCED: PROVED given the dichotomy
v_2(-1) in {0, -1} (i.e. eps = +-1), which is CHECKED(50) and holds for all rational boxes (X = I, Y = [[1,0],[-1,-1]] mod t+1).
Orientation meaning: upstairs the strand entering a box at the top right leaves at the bottom right iff n_0 is even. If n_0(B) is even,
strand 0 (down) and strand 1 (up) are antiparallel in the twist region; if odd they are parallel. So the 2m twist crossings change
writhe sign with eps; the jump t^(4m) is the writhe correction. At the level of unnormalised (bracket) states the outer map is
honestly linear: [N] = c^m X^(-m) [B] for a fixed framing constant c.
Corollary (Theorem N itself). The brief's necklace formula follows: the closure s.B evaluates the trivial special region, i.e. the
functional e_1^T (left Y-eigenvector, e_1^T e_1 = 1), so J(s.B) = a(v_B); stacking boxes composes endomorphisms in the commutative
algebra End(V_1 (x) V_2) = span(1, Y) acting on H through the (axis, arc) pair, which is the product * on vectors beta e_1; and
J(s.r2.(y1)^m.B_1...B_n.u1) = a(v_N) = e_1^T sigma^m (v_1 * ... * v_n) = e_1^T X^-m p by the nested-cap slide. So Theorem N is PROVED
modulo the TH-2BR dictionary (H, X, Y, e_1) and the identification of J with the coloured theta evaluation (the brief's set-up).
Corollary (nesting closes up). The class of vectors of iterated necklace bodies is the smallest subset of R e_1 containing the given box
vectors and closed under * and p -> F_m p; every J of an iterated necklace closure is normalize(first entry of the recursively computed
vector). In particular Theorem N for necklace closures is the m = 0 closure of the box N: J(s.N) = (v_N)_1.

## 2. Class of iterated necklaces ("equivariantly arborescent")
Setting. pi: S^3 -> S^3/h = S^3 is the double cover branched along the axis a; K = pi^-1(k). A box B (downstairs) meets a in one string
W->E and k in one string w->e and contains no vertex.

LEMMA L (lift dictionary). Let B be a rational box. Then B~ = pi^-1(B) is a ball, K n B~ is a rational tangle T_B, h swaps its two
strings and acts on dB~ as a rotation fixing the two axis points (not on K) and swapping the punctures in pairs (w' w'')(e' e'').
Put the axis horizontal, w' = NW, w'' = SW, e' = NE, e'' = SE. Then:
  identity box e_1  <->  the 0-tangle (horizontal arcs, axis between them);
  box product *     <->  tangle sum + (east face of B_1 glued to west face of B_2);
  Y (full twist of W,w)   <-> half twist of the west pair NW,SW:  slope s -> s + 1   (a disc around W,w contains one branch point,
                              its preimage is one disc around NW,SW and the full turn lifts to a half turn);
  X (half twist of w,e)   <-> the pair of half twists (NW NE)(SW SE), swapped by h:  1/s -> 1/s + 2  (the disc around w,e has no
                              branch point and lifts to two discs);
  closure s.B (vertices at W and E) <-> D-closure (NW-SW and NE-SE joined, each joining arc through one fixed point);
  necklace body N = F_m(product)    <-> sigma^m(T_1 + ... + T_n): m crossings added above and m below, swapped by h
                                         (equivalently, after a flype, vertical composition with the twist 1/(-2m));
  twisted necklace closure          <-> N(T_1 + ... + T_n + 1/(-2m)): a Montesinos knot whose special tangle 1/(-2m) contains
                                         both fixed points.
Consequently rational boxes <-> rational tangles of slope p/q with q ODD: the generated group is Gamma_0(2) (s->s+1, s->s/(2s+1))
and its orbit of 0 = (0,1)^T is exactly {(b,d): gcd = 1, d odd}. The box rho(w) e_1 has slope (word in these Moebius maps)(0).
Status: PROVED for the topology (branched-cover argument above; sign conventions fixed by the next check). CHECKED: (i) it reproduces
the brief's identification mont(m,[r_i]) = P(-2m, r_1,...,r_n) (row r = 2j+1 = X^j Y e_1 lifts to the vertical twist 1/r);
(ii) determinants: for 235 random iterated necklaces of rational boxes (twist rows r in {-5..7}, boxes y0, x0, depth 1-3, up to 3
children per node, twists |m| <= 3) det(K) = |Delta_K(-1)| (alex.py) equals |q| computed by the arborescent fraction calculus
(sum: (p1 q2 + p2 q1, q1 q2); F_m: (p,q) -> (p, q - 2mp); closure det = |q|): 235/235 (nest/p2_det.py).
Fixed points: for a rational tangle in symmetric position, rho_h (horizontal axis) fixes one point on each string that joins NW to
SW; hence 2 fixed points on K in a tangle of EVEN denominator and none in an ODD one; the arcs joining consecutive tangles and the
closing arcs are swapped. So on N(T_1+...+T_r) rho_h is a strong inversion iff exactly one T_i has even denominator.

THEOREM C1 (depth 1). The necklace closures of rational boxes are exactly the pairs (M, rho_h) with M = N(T_1 + ... + T_n + 1/(2m'))
a Montesinos knot, T_i of odd denominator, special tangle 1/(2m') (m' = -m). PROVED (Lemma L; converse: put any such M in the
standard symmetric position and read off boxes and twist).
THEOREM C2 (iterated). Let C be the smallest class of rho_h-symmetric tangles containing the odd rational tangles and closed under
(a) T_1 + T_2 and (b) T -> sigma^m(T). Iterated necklaces of rational boxes give exactly the pairs (D(T), rho_h), T in C. Every such
knot is arborescent (Conway-algebraic). PROVED (induction on depth with Lemma L; Theorem O is the J-shadow of (b)).
THEOREM C3 (every Montesinos knot with one even tangle). If M = N(T_1 + ... + T_r + R) with exactly one even-denominator tangle R,
then (M, rho_h) is an iterated necklace of rational boxes, and
      J = e_1^T X^(a_1) ( Y^(b_1) e_1 * X^(a_2) ( Y^(b_2) e_1 * ... X^(a_k) (v_1 * ... * v_r) ) )
where R = phi(infinity) and phi = X^(a_1) Y^(b_1) ... X^(a_k) in Gamma_0(2) (transitive on even slopes, orbit of (1,0)^T). The integral
boxes Y^b e_1 are realised by (y0)^b, and each X-block is one nesting level. Proof: the special region of R is phi applied to the
trivial one; move phi^-1 onto the boundary of the box chain (both lifts are h-equivariant, and an integral tangle commutes past a
rho_h-symmetric sum by a flype). PROVED modulo Lemma L. CHECKED: the realisation body(w) (nest/p2_twobridge.py: Y -> y0 box,
y -> x0 box, X -> r2.x1.(.).u1, x -> r2.y1.(.).u1) gives J(s.body(w)) = normalize(e_1^T rho(w) e_1) for ALL 728 reduced words
w of length <= 6 tested (exact).
So depth-1 necklaces = Montesinos knots whose even tangle is 1/(2m); general even tangles cost extra nesting levels (depth = number
of X-blocks of phi), and genuinely deeper trees (a nested body with >= 2 non-integral summands) give non-Montesinos arborescent knots.

WHICH INVERSIONS ARE REACHED.
(i) 2-bridge knots (single rational box; J = e_1^T rho(w) e_1, the TH-2BR words). BOTH strong inversions are reached (a hyperbolic
knot has at most two inequivalent strong inversions: KNOWN, Sakuma / Kodama-Sakuma, as recalled): grouping the J's
of the 728 words by Alexander polynomial and identifying J(t) with J(1/t) (mirror), the non-torus non-amphichiral knots
5_2, 6_1, 6_2, 7_2, 7_3, 7_4 (Alexander (2,-3,2), (2,-5,2), (1,-3,3,-3,1), (3,-5,3), (2,-3,3,-3,2), (4,-7,4)) and several larger
ones each show exactly 2 distinct J classes (2-bridge knots with these determinants are determined by Delta, so these are 2 inequivalent
inversions of one knot, distinguished by J); T(2,n) show 1 class (unique inversion). CHECKED (words <= 6; some knots show 1 class only,
attributed to the length cut-off or amphichirality: 4_1, 6_3).
(ii) Montesinos knots with r >= 3 genuine tangles (all |q_i| >= 2), non-elliptic. Literature used (KNOWN, as recalled, not re-checked
here): [BZ] Boileau-Zimmermann (Math. Ann. 1987): every symmetry is conjugate to one preserving the standard Montesinos presentation
(rho_h and the dihedral symmetries permuting tangles that the cyclic sequence admits); [MU] uniqueness of the Montesinos presentation
(Bonahon / Boileau-Siebenmann); [O] Oertel: the essential Conway spheres of a Montesinos knot are the obvious ones (both sides sums of
consecutive rational tangles). Claim (PROVED modulo [BZ], [MU], [O]; sketch): (K,h) is an iterated necklace of rational boxes iff
exactly one q_i is even and h is conjugate to rho_h. Sketch: a necklace presentation of a Montesinos K cannot contain a nested body
sigma^m(U_1 + U_2) (m != 0, U_i non-integral) inside a sum with further non-integral summands, because its sphere would be an essential
Conway sphere whose inner side is not a sum of rational tangles [O]; so the presentation is of the Theorem C3 shape, i.e. a Montesinos
presentation with one even tangle and h = its rho_h; by [MU] it is the standard one. Consequences: dihedral-type inversions (which swap
at least two tangles when r >= 3, since a reflection of an r-cycle fixes at most 2 positions) are NOT reached unless conjugate to rho_h;
if all q_i are odd, rho_h is a free period-2 symmetry and K is not reached with ANY inversion. Example: the vertical inversion of
P(p,q,p), |p|,|q| >= 3 (section 4), swaps the outer columns; for q odd it is the only kind of inversion and is not a necklace; for
q even P(p,q,p) carries both, and J separates them (18/20 checked) except T(3,4) and its mirror, where they are equivalent.
Independent of the literature: the vertical family has a genuinely 3-channel twist dependence (Theorem V), while any twist region
that sits in a necklace special region has 2 channels (eigenvalues of X).
(iii) Arborescent knots in general. CONJECTURE (characterisation): (K,h) is an iterated necklace of rational boxes iff K is arborescent
and h preserves every sphere of the Bonahon-Siebenmann characteristic Conway-sphere system (sides preserved, h free on the four
punctures), i.e. h acts trivially on the canonical tree and is 'horizontal' at every node. The forward direction is Theorem C2 (box
and body spheres are invariant). GAP for the converse: one needs the canonical splitting to be h-equivariant (expected from
uniqueness of the characteristic splitting plus the equivariant torus decomposition of the double branched cover) and then to show
that an invariant Montesinos piece with >= 3 invariant holes carries the horizontal action (true: a rotation fixing every position of
an r-cycle, r >= 3, is rho_h) and that the fixed points sit in one even leaf (true: in a symmetric Montesinos piece rho_h has no fixed
points on the connecting arcs; two arc points on an invariant sphere never separate the two vertices, by parity of arc crossings).
Plumbing picture (remark): each necklace body with >= 2 summands is a node of valence >= 3; the twist m of a body is an EVEN weight 2m
on the edge towards the root; the root is the even leaf containing the fixed points; rational boxes are chains of odd-denominator type.

## 3. The family T_n = s.r1.x2.(y1)^n.y0.r2.y0.y1.y0.y1.x2.u3.u1
ANSWER: yes. T_n is, up to an explicit equivariant isotopy of the half-diagram, the twisted necklace closure of ONE box:
      T_n  ~  s.r2.(y1)^(n+1).B.u1,      B = y0.r2.y0.y1.y0.y1.x2.u1   (= y0.y0.r2.y1.y0.y1.x2.u1, the second y0 commutes past r2).
Moves (both equivariant, mirrored on the left half): (i) r1.x2 -> r2.y1: in r1.x2 the right leg of the new cap passes OVER the strand A
from the top fixed point (x2 = left-to-right strand over); slide the whole cap (it lies above A) to the right of A; its left leg now
crosses A from right to left, over it: letter y1. So the x2 is one more twist crossing and m = n + 1. (ii) u3.u1 -> u1.u1: the two cups
occupy disjoint positions (2,3) and (0,1); exchange heights. After (i)+(ii) the letters between the twist and the final u1 form a body
B acting only on position 0 and its own strands (the external strands 1, 2 are untouched until the final u1).
CHECKED: J(T_n) = J(s.r2.(y1)^(n+1).B.u1) = J(s.r2.(y1)^(n+1).y0.r2.y0.y1.y0.y1.x2.u3.u1) for n = -3..5 (9/9 exact).
The box. s.B is the trefoil (Alexander t^2 - t + 1; J(s.B) = t^-7 + t^-4 - t^-3); n_0(B) = 3 so eps = -1. Pinned vector (unique):
      v_B = ( t^-7 + t^-4 - t^-3 ,  t^-15 + t^-12 + t^-11 + t^-8 - t^-6 ),
      a(v_B) = J(3_1),   b(v_B) = t^-15 + t^-11 - t^-9 + t^-7 - t^-6 - t^-5 + t^-4.
B is NOT a rational box. PROVED (given the slope classification of rational boxes in section 2): a rational box with s.B = right
trefoil has slope +-1/3 mod 1 for one fixed sign, so its vector is Y^k v_0 for one fixed v_0 and b(Y^k v_0) = t^(-3k) b(v_0) has
3 terms; b(v_B) has 7. (Brute force: the 11 distinct normalised rational vectors from words of length <= 7 with a = J(3_1) all have
3-term b.) Also v_B is not t^c X^(-m) (p_1 * p_2) for rational p_i from words of length <= 5 and |m| <= 4 (CHECKED; this does not
prove that B is outside the iterated-necklace class).
Formula. By Theorem N/O with m = n+1:
      J(T_n) = t^(4(n+1)) e_1^T X^-(n+1) v_B = t^(4n+4) P_B + (-1)^(n+1) t^(3n+3) Q_B,
      P_B = a + (1-t)(1+t^2) v_2 = (t a + (1+t^2) b)/Phi_3 = t^-15 (t^2 - t + 1)        [X-eigenvalue 1 channel],
      Q_B = -(1-t)(1+t^2) v_2 = (1+t^2)(a - b)/Phi_3 = J(3_1) - P_B                    [X-eigenvalue -t channel].
With alpha = t^10 P_B = t^-5 (t^2 - t + 1) and beta = -t^9 Q_B this is exactly J(T_n) = t^(2n-6) (alpha t^(2n) + beta (-t)^n), the stated
formula (unit t^(2n-6)). CHECKED n = -3..5 exact (nest/p3_twist.py, p3_channels.py).
Which sphere. The boundary of the ball around B: it meets the axis twice and the arc twice, its state space is H (dim 2), and the n+1
twist crossings act on H as X^-1 with eigenvalues 1 and (-t)^-1. The two channels are the V_0 and V_2 fusion channels of the two arc
points of that sphere; V_4 cannot occur because it must pair with V_1 (x) V_1 = V_0 + V_2 of the two axis points.
Endpoint behaviour (formula, n = -6..13): P-part occupies degrees [4n-11, 4n-9], Q-part [3n-12, 3n]. For 0 <= n <= 8 the P-part lies
inside the Q-part, so both extremes of J(T_n) come from Q_B alone: span 12 for n = 0..8 (constant, although the knots grow), lc's
(-1)^n at both ends; n = 9: the tops collide and cancel, span 10; n >= 10: channels separate, span n + 3. n = -1 is the trefoil.
So the endpoint behaviour of T_1 (and of all T_n, 0 <= n <= 8) is inherited from the Q-channel of the non-rational box B
(Q_B = J(3_1) - t^-15 Phi_6 has span 12 while J(s.B) has span 4); the twist region only shifts the two channels against each other.

## 4. Vertical inversion of P(a,b,a)
Words. For a body B and odd a let V_a(B) = s.l1.B.(x2)^a.u1 ((y2)^|a| if a < 0). The pretzel family is
VP(p,q) = s.l1.(x0)^q.(x2)^p.u1 (y0 for q < 0, y2 for p < 0) = P(p,q,p) with the rotation about the vertical axis of the standard
picture: the middle column (q crossings) sits ON the axis, the two outer columns (p crossings each) are swapped by h.
Sign check: VP(3,-2) = s.l1.y0.y0.x2.x2.x2.u1 has the same J as mont(1,[3,3]) = P(-2,3,3) = T(3,4) (the table word
s.l1.x0.x0.y2.y2.y2.u1 is its mirror: J(t) -> J(1/t)). The body x0 has pinned vector (1,-1) = Y^-1 e_1, y0 has (1,t^-3) = Y e_1.
Downstairs: the outer columns become ONE column of a crossings between two arc strands (c' and A). A sphere S_a around it meets
the arc 4 times; its state space is End(V_2 (x) V_2) = C Pi_0 + C Pi_2 + C Pi_4 (dim 3), and the crossing acts with eigenvalues
lambda_0 : lambda_2 : lambda_4 = 1 : -t : t^3 (Kauffman-Lins: (-1)^((4-c)/2) A^((c(c+2)-16)/2) with t = A^4).
The middle part is a box (axis + arc) with state beta = A P_1 + B P_3, A = a(v), B = b(v).

THEOREM V (vertical closure formula). For every body B and odd a, with A = a(v_B), B = b(v_B):
      J(V_a(B)) * Phi_3  =.  t A + (-t)^a [ (1+t^2) A + t B ] + t^(3a-1) Phi_5 B,          Phi_5 = 1+t+t^2+t^3+t^4,
where =. means equality after normalisation (exact equality if the left side is multiplied by t^(4a) and J is replaced by the
functional normalised on the identity box). Equivalently the three channel functionals are
      K_0 = t A / Phi_3   (only P_1),   K_2 = ((1+t^2) A + t B) / Phi_3,   K_4 = t^-1 Phi_5 B / Phi_3   (only P_3),
      J =. sum_c lambda_c^a K_c,   lambda = (1, -t, t^3).
For the pretzels (A = 1, B = t^(3q) both for x0^q and y0^|q|):
      J(P(p,q,p), vertical) * Phi_3 =. t + (-t)^p (1 + t^2 + t^(3q+1)) + t^(3p+3q-1) Phi_5.
Example: p = 3, q = -2 gives t^6 - t^5 + t^4 + t - 1 =. J(T(3,4)).
Status: CHECKED. (a) For each a in {1,-1,3,-3,5,-5,7} the closure functional l_a (row vector with J(V_a(B)) = normalize(l_a v_B))
was pinned from the boxes empty and y0 plus 6 random boxes (unique candidate in every case) and then holds for ALL 50 random
non-rational boxes of general_boxes.json: 350/350 exact. (b) The closed form was fitted from a = 1, 3 only and reproduces l_a for
a = -1, -3, 5, -5, 7 exactly (unit t^(-4a) relative to the identity-box normalisation). (c) Fresh direct tests of the closed form:
P(p,q,p) for p in +-{1,3,5,7,9}, q in [-7,7]: 150/150; random boxes at a = 9, -7, -9, 11: 40/40; twist-row boxes and products of
rows (Montesinos boxes) at a in {-3,-1,1,3,5}: 30/30. Scripts nest/p4_fit.py, p4_channels.py, p4_test.py.

Why (derivation; PROVED modulo the same skein dictionary as Theorem N).
(i) Three channels: sigma^a = sum_c lambda_c^a Pi_c in the commutative algebra End(V_2 (x) V_2); so J(V_a) = sum_c lambda_c^a K_c(beta)
with K_c linear in the box state. (ii) Admissibility zeros. Fuse with Pi_c = (dim_c/theta(2,2,c)) [fusion through c] and
P_k = (dim_k/theta(1,2,k)) [fusion through k]. What remains is a planar trivalent network with 6 vertices: the two vertices of the
theta curve, two c-vertices, two k-vertices. It is the triangular PRISM: triangles (v_top, b_top, a_top) and (v_bot, b_bot, a_bot)
with edges (axis 1, arc 2, arc 2), rungs coloured (1 [axis through infinity], k, c). Each triangle reduces to Tet/theta(1,k,c) times
a vertex (1,k,c), so K_c(P_k) is proportional to Tet^2/theta(1,k,c) and VANISHES unless (1,k,c) is admissible:
(k,c) in {(1,0),(1,2),(3,2),(3,4)}. Hence K_0 sees only A and K_4 only B: exactly the zeros found in the fit (4 channel terms, not 6).
(iii) Three values fix the rest: a = +-1: V_{+-1}(B) is a necklace closure and indeed l_1 = e_1^T X^-1, l_{-1} = e_1^T X exactly
(found by the pinning, no unit); formal a = 0: the closure becomes the theta curve plus a separate V_2 loop through the box, i.e. the
partial trace tr_{V_2}(beta) = A + ([4]/[2]) B = A + t^-1 (1+t^2) B; the closed form at a = 0 gives
(Phi_3 A + (t + t^-1 Phi_5) B)/Phi_3 = A + t^-1 (1+t^2) B because t^2 + Phi_5 = (1+t^2) Phi_3. So the formula is the unique
3-channel interpolation of the necklace values at a = +-1 and the partial trace at a = 0 (Vandermonde in lambda_c, distinct).
The relative units between a = 1, 0, -1 are NOT an extra input: write J_1 = u_+ e_1^T X^-1 v, J_0 = tr_{V_2}(beta), J_-1 = u_- e_1^T X v with
unknown units u_+-, solve the Vandermonde system for K_0, K_2, K_4 and impose the two admissibility zeros [K_0]_B = 0, [K_4]_A = 0.
Both reduce to the single relation u_+ = t^5 u_- + t^4 - t (nest/p4_derive.py), whose only unit solutions are (u_+, u_-) = (t^4, t^-4)
and (-t, -t^-1). The second gives identity-box weights K_c(id) proportional to (1+t^2) : t^-1 (1+t^2) Phi_3 : t, not to the
q-dimensions [1] : [3] : [5] demanded by Corollary S below (bubble argument); the first gives exactly Theorem V. So Theorem V is
DERIVED from: 3-channel structure + prism admissibility + Theorem N at a = +-1 + partial trace at a = 0 + Corollary S.
(The units t^(-+4) are the writhe correction of the outer crossings, which join PARALLEL strands; cf. t^(4m) in Theorem O.)
Status of Theorem V: PROVED modulo the skein dictionary (the same inputs as Theorem N), and CHECKED as listed.
Comparison with Theorem N: necklace  J Phi_3 = [t + (1+t^2)(-t)^mu] A + (1+t^2)[1 - (-t)^mu] B  (channels 0, 2 of the arc pair
only, 2x2 coefficient matrix [[t, 1+t^2],[1+t^2, -(1+t^2)]]); vertical: channels 0, 2, 4 with coefficient matrix
rows c=0: (t, 0), c=2: (1+t^2, t), c=4: (0, t^-1 Phi_5).  The A-coefficient t + (1+t^2)(-t)^a is the SAME in both.
Two inversions of the same knot. For q even P(p,q,p) carries both the horizontal inversion (necklace mont(-q/2,[p,p])) and the
vertical one. J differs in 18/20 cases checked (p in {3,5,-3,7}, q in {+-2,+-4,-6}); it agrees exactly for P(3,-2,3) = T(3,4) and its
mirror, where the two inversions are equivalent (torus knots have a unique strong inversion). a_2 agrees in all 20 (as it must).
The vertical J is usually wider (e.g. P(3,4,3): span 10 horizontal vs 21 vertical).

COROLLARY S (swap inversions of K # K; the identity box). For B = identity, V_a(empty) = s.l1.(x2)^a.u1 = T(2,a) # T(2,a) with the
inversion that SWAPS the summands, and Theorem V gives K_0 : K_2 : K_4 = t : Phi_3 : t^-1 Phi_5 = [1] : [3] : [5] (q-dimensions,
t = q^2 up to units), i.e. J = sum_c lambda_c^a [c+1]/[3] = the colored Jones polynomial of T(2,a) with the 3-dim colour.
General statement, PROVED: for ANY knot K, the swap inversion of K # K has J = J_{V_2}(K) (normalised colored Jones, colour = spin 1,
"N = 3"). Reason: the connected-sum sphere is h-invariant with h swapping its sides, so h reflects it and the axis lies IN it;
downstairs the axis bounds a disc D (= sphere/h) whose interior misses the arc k, and k u (axis edge) = K. The two V_1 axis edges
bound D, so they form a bubble on the V_2 strand: bubble = theta(1,1,2)/[3] x (V_2 strand), and the theta curve evaluates to
theta(1,1,2)/[3] <K>_{V_2}. CHECKED: J(s.l1.x2.x2.x2.u1) = q^-2 + q^-5 - q^-7 + q^-8 - q^-9 - q^-10 + q^-11 (t = q) exactly equals the
Habiro/Masbaum N = 3 colored Jones of the trefoil (and the y2 word gives the mirror).
Second check, figure-eight: among random swap words s.l1.tau.u1 (tau on positions >= 1) with det 25, three different words have J
exactly equal to Habiro's J_3(4_1) = t^-6 - t^-5 - t^-4 + 2t^-3 - t^-2 - t^-1 + 3 - t - t^2 + 2t^3 - t^4 - t^5 + t^6 (and Delta(2) = Delta(3) = 1
= Delta_{4_1}(2)^2 = Delta_{4_1}(3)^2): e.g. s.l1.x2.r3.y2.x3.y2.x3.u2.x2.y2.u1 (nest/p4_swapcheck.py). CHECKED (3_1, 4_1).
CONSEQUENCE FOR THE PROGRAM (important): Lemma Q restricted to swap inversions of K # K is EQUIVALENT to "the 3-colored Jones polynomial
J_3 detects the unknot" (K # K is non-trivial iff K is). As far as I know that statement is open (it is of the same type as the Jones
unknot conjecture; J_3(K) = Jones polynomial of the 0-framed 2-parallel of K minus the trivial summand). So Lemma Q in full contains
the J_3-unknot problem; any proof strategy for Lemma Q must either handle swap inversions separately or prove J_3-detection.

SURVEY (formula only, cheap; nest/p4_survey.py): 30,000 vertical closures V_a(B) with |a| in {3,5,7,9}, B a product of 1-3 random
rational boxes (words of length <= 7), optionally wrapped in a necklace body: NO unit J; minimum span 4 (|a| = 3, the trefoil
P(3,+-1,3)), 10 (|a| = 5), 13 (|a| = 7), 10 (|a| = 9). CHECKED(30000).

## 5. Open problems / handoff
1. GAP (used everywhere): a written identification of the quotient-tangle bracket J with the coloured theta-curve evaluation
   (axis V_1, arc V_2) and of (H, X, Y, e_1) with the TH-2BR matrices for boxes that are not part of a 2-bridge picture. With it,
   Theorems N, O, V and Corollary S are proofs; without it they are proofs of the skein-level statements plus exact computer checks.
2. eps-dichotomy: prove v_2(-1) in {0,-1} (equivalently b(v)(-1) = (-1)^(n_0)) for every box. It is the only input for the unit
   t^(2m(1-eps)) in Theorem O. CHECKED(50) + all rational boxes.
3. CONJECTURE C4 (section 2 (iii)): iterated necklaces of rational boxes = arborescent (K,h) with h acting trivially and horizontally
   on the Bonahon-Siebenmann canonical tree. Needs the equivariant canonical splitting.
4. PROGRAM-LEVEL: by Corollary S, Lemma Q for swap inversions of K # K is equivalent to "the 3-coloured Jones polynomial J_3 detects
   the unknot" (open as far as I know). Decide whether Lemma Q should be restricted (e.g. to inversions whose quotient has no
   'swap' sphere) or whether the program accepts this as a sub-problem.
5. Is the T_n box B = y0.r2.y0.y1.y0.y1.x2.u1 an iterated necklace body (arborescent lift)? It is non-rational and not a short
   2-box Montesinos body. If its lift is non-arborescent, T_n is a clean family of non-arborescent (K,h) where the single-box
   formula still applies.
6. Vertical/dihedral inversions of Montesinos knots with r >= 4 (fixing 2 tangles, or none): the same 3-channel calculus (spheres
   meeting the arc 4 times; channels 0, 2, 4 with admissibility zeros) should give closed formulas; not done here.
Scripts (all in nest/): nlib.py (helpers: vec, F, tree_vec, ...), p1_probe.py, p1_nest.py, p1_nest3.py, p1_units.py,
p2_det.py, p2_twobridge.py, p3_twist.py, p3_channels.py, p3_structure.py, p4_probe.py, p4_fit.py, p4_channels.py, p4_test.py,
p4_derive.py, p4_survey.py, p4_swapcheck.py; data nest/p4_functionals.json; logs nest/p1_nest.log, nest/p1_nest3.log.
