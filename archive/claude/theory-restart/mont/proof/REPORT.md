# REPORT (lane PROOF): a skein proof of THEOREM N (the necklace formula)
Lane: ~/jones-lanes/theory-restart/mont/proof/   (16 Nov 2026, Claude, PROOF lane)
Marks: PROVED / CHECKED(n) / CONJECTURE / GAP.  "=." means equality up to a unit (a signed power of A).
Scripts (this folder): check_moves.py, check_vector.py, check_nested.py, check_special.py (spot checks of every word
identity used and of the corollaries; results in section 6). Run with tools/venv/bin/python from mont/.

STATUS: COMPLETE (sections 0-7 final). Theorem N PROVED (skein proof, sections 1-3); one GAP and one CONJECTURE, both peripheral (section 7).

## 0. Setting, conventions, and what is taken from TH-2BR

0.1 Skein conventions. Kauffman bracket at generic A, delta = -A^2 - A^-2, t := A^-4 (so the half twist of two V_2
strands has eigenvalue ratio -t and the full twist of V_1 with V_2 has ratio t^-3, as in TH-2BR). V_n = colour n
(n parallel strands with the Jones-Wenzl projector f_n), Delta_n = quantum dimension, f_2 = 1 - delta^-1 e.
Trivalent vertices and theta(a,b,c) as in Kauffman-Lins. UNIT = a signed power of A. Lambda := Z[t, 1/t].
All diagrams are blackboard framed; isotopies used below are regular isotopies (R2, R3, planar), unless a kink is
named, and a kink only costs a unit (-A^{+-3} on a colour-1 strand, A^{+-8} on a colour-2 strand).

0.2 J as a theta-curve evaluation (TH-2BR 2.2; PROVED there; two-line proof recalled because it fixes the units).
Theta = A u k is the quotient theta-curve (axis A, both edges coloured 1; arc k coloured 2). T = (S^3 - N(k), A - N(k))
with bracket [T] = y[Q_0] + x[Q_inf] (Q_0 = the matching parallel to k, Q_inf = the two short arcs). Colouring k by 2 =
replacing k by a band with f_2 inserted. The x-term dies (Q_inf closes the two band strands at one end: a cap on f_2);
the y-term is the closure of f_2 with f framing twists. Hence <Theta;1,1,2> = mu_2^f Delta_2 y, and
      J(T) =. <Theta; 1,1,2> / <Theta_0; 1,1,2>,      Theta_0 = trivial (planar) theta-curve,
with J normalised by J = 1 mod (t+1)^2 (unique signed power of t). Everything below computes <Theta>/<Theta_0>.

0.3 Half-diagrams -> quotient pictures. In the quotient of a symmetric diagram s.W the axis is a vertical line (closed
through infinity) and half-strand i becomes a colour-2 strand at position i to the right of the axis (TH-2BR 1.3(b):
kht++ Tangle::quotient doubles every half-strand into a band; f_2 on the single edge k slides along it). Letters:
y0/x0 = full twist of the axis with the strand at position 0 (kht++ y0.y1.y1.y0 on axis+band); x_i, y_i (i >= 1) =
colour-2 crossing of positions i-1, i; r_i/l_i = cap creating positions i-1, i; u_i = cup joining them. The start
(one half-strand) is the vertex v_top (k meets A), the implicit final u0 is the vertex v_bot.
Crossing types: x = over strand from top-left to bottom-right, y = over strand from top-right to bottom-left
(alex.py, diagram()). Rotation by 90 degrees in the plane exchanges x and y; rotation by pi in the plane, and the
3-dimensional rotation R by pi about a horizontal line of the projection plane ((x,y,z) -> (x,-y,-z)), preserve them.

0.4 What is used from TH-2BR-A (PROVED by both agents; board X.21-X.22; Codex 20261116-112801 section 2).
 H := Hom(V_1, V_1 (x) V_2 (x) V_2) (axis in at the top; axis and two legs out at the bottom); dim H = 2.
 E_1 = the band cap (letter l1 in s.l1.W.u2): axis straight, the two legs joined by a cap (colour-0 fusion).
 phi : V_1 (x) V_2 (x) V_2 -> V_1 = fuse (axis, leg 1) to colour 1, then fuse with leg 2 (the closing functional).
 X^ = the actual colour-2 crossing x1 of the two legs; Y^ = the actual full twist y0 of the axis with leg 1.
 Basis (E_1, F), F in ker(phi); rho(X) = X^/lambda_X, rho(Y) = Y^/theta_1 (eigenvalues normalised to 1 on E_1, phi):
      rho(Y) = [[1,0],[t^-3,t^-3]],   rho(X) = [[1,1-t^4],[0,-t]];   phi = e_1^T,  E_1 = e_1.
 For a word: [l1.L_1...L_m] =. rho(L_m)...rho(L_1) e_1, with y0 <-> Y, x1 <-> X (inverse letters <-> inverses).
LEMMA 0.1 (closure; PROVED). Let W be any half-diagram word which, run after l1 on the strand configuration
 (leg a, leg b, passing strand c from v_top), only uses positions occupied by a, b and strands it creates itself,
 and ends with two legs at positions 0, 1 (c at 2). Then [l1.W] in H is defined, and the quotient theta-curve of
 the knot s.l1.W.u2 is cl([l1.W]) := the closure of [l1.W] by phi; hence J(s.l1.W.u2) =. phi([l1.W]) = e_1^T [l1.W].
 Proof. Cut the quotient picture by a ball D containing the axis segment from just above the l1 cap to just above u2
 and every strand of [l1.W], but not c (c runs at the outer position and W never touches it). D meets Theta in the
 axis twice (colour 1) and the two legs (colour 2), so its skein lies in H. Outside D: v_top (above D, where c starts),
 c running down outside D to u2, u2 joining leg 2 to c, leg 1 running to v_bot on the axis below D, and the axis edge
 A_out from v_bot through infinity to v_top. Slide v_top along A_out through infinity to a point just below v_bot.
 This is an isotopy of Theta in S^3 (in the projection sphere it is a planar isotopy: c is dragged along the right
 side of A_out, inside the empty outer region), and afterwards c is a short arc. The outside is then exactly:
 leg 1 fused to the axis (v_bot), then leg 2 fused to the axis just below (old v_top): this is phi. QED
 (This is the statement TH-2BR uses for words in y0, x1; the proof never looks inside W.)

## 1. Boxes, their states, and the star product

DEFINITION 1.0 (box). A BOX is a closed ball B in S^3 with B n Theta = alpha u kappa, alpha a sub-arc of the axis
(colour 1) and kappa a sub-arc of k (colour 2), both properly embedded and both running from the WEST disc D_W to the
EAST disc D_E of dB, together with a product parametrisation (B, D_W, D_E) = (D^2 x I, D^2 x 0, D^2 x 1), fixed up to
isotopy. W, w := alpha n D_W, kappa n D_W; E, e := alpha n D_E, kappa n D_E. Equivalently: a framed 2-string tangle in
D^2 x I, one string coloured 1 and one coloured 2, each from the west disc to the east disc. Boxes STACK: B o B' is B'
followed by B (east disc of B' glued to the west disc of B). Its STATE [B] is its class in the relative skein module of
(D^2 x I; (W,w) coloured (1,2), (E,e) coloured (1,2)), which is End(V_1 (x) V_2) (the skein module of a ball with
coloured boundary points is the corresponding Hom space of the Temperley-Lieb category; stacking = composition).
The parametrisation matters only through full twists of D_E relative to D_W (a half twist would exchange E and e,
which carry different colours); one full twist multiplies the state by the full twist Y^ of (E, e) (see 1.6).

LEMMA 1.1 (PROVED). End(V_1 (x) V_2) = C P_1 (+) C P_3 with P_c = (Delta_c / theta(1,2,c)) split_c o fuse_c (c = 1, 3)
orthogonal idempotents, P_1 + P_3 = id (= 1 (x) f_2). In particular this algebra is COMMUTATIVE.
 Proof. Kauffman-Lins fusion: id_{V_1 (x) V_2} = sum over admissible c of (Delta_c/theta(1,2,c)) split_c o fuse_c,
 and (1,2,c) is admissible exactly for c = 1, 3. Bubble identity: fuse_c o split_c' = delta_{cc'} (theta(1,2,c)/Delta_c)
 id_{V_c}; hence P_c P_c' = delta_{cc'} P_c. For any B, P_c B P_c' factors through fuse_c o B o split_c' in
 Hom(V_c', V_c), which is 0 for c != c' and C id for c = c' (V_1, V_3 simple and distinct at generic A). So
 B = sum_c beta_c P_c. Both P_c are nonzero (quantum trace Delta_c != 0). QED
DEFINITION (channel amplitudes). [B] = a(B) P_1 + b(B) P_3. Identity box: a = b = 1. Under stacking,
 a(B o B') = a(B) a(B'), b(B o B') = b(B) b(B') (orthogonal idempotents). These are the P_1- and P_3-channels.

LEMMA 1.2 (R-symmetry; PROVED). Let R be the rotation by pi of D^2 x I about a horizontal line of the projection
plane through the middle level (it exchanges the two discs, keeps the axis string on the left, preserves crossing types,
0.3). Then [R(B)] = [B] for every box B. Proof. R acts linearly, and R(P_c) = P_c: split_c o fuse_c is a crossingless
planar H-shaped graph (axis edge on the left, arc edge on the right, c-edge in the middle), and R maps it to its
reflection in a horizontal line, which is the same graph (Jones-Wenzl vertices are reflection symmetric). Hence
R([B]) = a(B) P_1 + b(B) P_3 = [B]. QED  (Equivalently: a(R(B)) is the evaluation of the R-image of a closed graph, and
R is an orientation-preserving isometry of S^3.)

DEFINITION 1.3 (box vector). v : End(V_1 (x) V_2) -> H,  v(B) := (B (x) id_{V_2}) o E_1: hang the box on leg 1 of the
band cap (TH-2BR orientation: E_1 = the l1 cap at the top, the box below it on its left leg, leg 2 passing by;
west = top, east = bottom). Put h_1 := v(P_1), h_3 := v(P_3).
LEMMA 1.3 (PROVED). v is a linear isomorphism, v(B o B') = (B (x) id) v(B'), and E_1 = h_1 + h_3,
v(B) = a(B) h_1 + b(B) h_3, H = C h_1 (+) C h_3.
 Proof. Injective: from v(B) recover B by adding a strand s on the right and cupping leg 2 with s at the bottom; the
 zigzag (leg 2 - cup - s) straightens (exact Temperley-Lieb relation; f_2 idempotent), giving back B. dim H = 2 =
 dim End(V_1 (x) V_2), so v is an isomorphism. The rest is linearity, id = P_1 + P_3 and (B o B') (x) id =
 (B (x) id)(B' (x) id). QED
LEMMA 1.4 (eigen-data; PROVED). (i) Y^ = theta_1 P_1 + theta_3 P_3 in End(V_1 (x) V_2) (a full twist acts on each
 irreducible summand by a scalar, the ratio of ribbon twists), so Y^ h_c = theta_c h_c: h_1, h_3 are the eigenvectors
 of Y^ (Y^ acts on H through the first two factors, i.e. exactly as a box). (ii) phi(h_3) = 0, because phi factors
 through fuse_1 (x) id and fuse_1 o P_3 = 0. (iii) phi o Y^ = theta_1 phi, so rho(Y) = Y^/theta_1 has eigenvalue 1 on
 h_1 and theta_3/theta_1 on h_3; since rho(Y) = [[1,0],[t^-3,t^-3]] has eigenvalues 1, t^-3, theta_3/theta_1 = t^-3.
 (iv) In TH-2BR coordinates: by (ii) h_3 = (0, kappa); h_1 = E_1 - h_3 = (1, -kappa); rho(Y) h_1 = h_1 reads
 t^-3 (1 - kappa) = -kappa, so kappa = 1/(1 - t^3):
        h_1 = (1, 1/(t^3 - 1)),        h_3 = (0, 1/(1 - t^3)).                                          QED

THEOREM 1.5 (coordinates and the star product; PROVED). A box with state a P_1 + b P_3 has vector
        v = a h_1 + b h_3 = ( a , (b - a)/(1 - t^3) ),   i.e.   a(v) = v_1,   b(v) = v_1 + (1 - t^3) v_2,
and stacking is the commutative product v(B o B') = v(B) * v(B') with h_c * h_c' = delta_{cc'} h_c, unit e_1:
        v * w = ( v_1 w_1 ,  v_1 w_2 + v_2 w_1 + (1 - t^3) v_2 w_2 ).
 Proof. First line: Lemma 1.3 and 1.4(iv). Second: a(v*w) = v_1 w_1 and b(v*w) = b(v) b(w) =
 (v_1 + s v_2)(w_1 + s w_2) with s = 1 - t^3; subtract and divide by s. QED
 Checks. (a) identity box: v = E_1 = e_1, (a,b) = (1,1). (b) rho(Y) is diagonal in the (a,b) basis: for
 rho(Y)v = (v_1, t^-3 (v_1 + v_2)) one gets a = v_1 and b = t^-3 (v_1 + (1 - t^3) v_2), i.e. (a,b) -> (a, t^-3 b);
 the Y-box itself has (a,b) = (1, t^-3) = (theta_1, theta_3)/theta_1. (c) rho(X) is NOT diagonal in this basis
 (X moves the two legs, not the box): X is not a box operator, it lives in the special region (section 2).
 Box ring: (Lambda^2, *) = Lambda[s]/(s^2 - (1 - t^3) s) (s = (0,1)), embedded in Lambda x Lambda by v -> (a(v), b(v)) with
 image {(a,b) : a = b mod (1 - t^3)}. That box vectors are integral (in Lambda^2 after a unit) is Proposition 4.2.

1.6 Integral parts. Re-parametrising a box by k full twists of its east disc multiplies its state by Y^^k, i.e.
v -> rho(Y)^k v (up to the unit theta_1^k): a -> a, b -> t^-3k b. This is the box incarnation of "integral parts act
as Y^k" (5.3); it is the only re-parametrisation ambiguity of a box, and R (Lemma 1.2) acts trivially.

## 2. The necklace closure: a trace pairing, the special region = e_1^T X^mu, and the closed form

DEFINITION 2.0 (necklace). A NECKLACE is the theta-curve Theta together with boxes B_1, ..., B_n stacked along the axis
(east disc of B_i = west disc of B_{i+1}), forming the composite box N = B_n o ... o B_1, such that the complementary
ball C := closure(S^3 - N), the SPECIAL REGION, contains both vertices. C meets Theta in a graph with the two vertices
and four ends W, w, E, e on dC = dN.

PROPOSITION 2.1 (the closed necklace is a trace pairing; PROVED).
 (i) <Theta> = <C, N>, where <C, .> : End(V_1 (x) V_2) -> Q(A) is the (bilinear) skein pairing of the two balls.
     Hence <Theta> = gamma_1(C) a(N) + gamma_3(C) b(N), gamma_c(C) := <C, P_c>.
 (ii) a(N) = prod_i a(B_i), b(N) = prod_i b(B_i)  (Lemma 1.1: stacking multiplies channels).
 (iii) The quantum trace form (U,V) -> Tr_q(UV) on End(V_1 (x) V_2) is nondegenerate (Tr_q(P_c P_c') = delta Delta_c),
     so C defines a unique bead C^ = sum_c (gamma_c(C)/Delta_c) P_c with <C, N> = Tr_q(C^ [B_n] ... [B_1]): the closed
     necklace is the quantum trace of the product of its n + 1 beads, diagonal in (P_1, P_3):
          <Theta> = Delta_1 (gamma^_1 prod_i a_i) + Delta_3 (gamma^_3 prod_i b_i).
 Proof. Gluing two balls along their boundary sphere is the skein pairing; linearity in N and Lemma 1.1. QED

2.2 The standard special region C_m. C_m denotes the special region of the necklace realised by the half-diagram
s.r2.(y1)^m.<N>.u1 (section 3 shows the bodies form N). Explicitly, in the quotient picture (0.3): axis vertical
(x = 0); v_top at the top, where the strand at x = 1 starts; the r2 cap joins x = 2 and x = 3; m y-crossings of
x = 1 with x = 2; then the composite box N on (axis, x = 1); the u1 cup joins x = 1 and x = 2 below N; x = 3 runs
down outside everything to v_bot (below the cup). C_m contains v_top, v_bot, the m crossings, the cap, the cup, x = 3
and the axis edge A_out from v_bot through infinity to v_top.

PROPOSITION 2.2 (identification of the special region; PROVED). For every N in End(V_1 (x) V_2),
        <C_m, N> = u_m . phi( X^^-m (N (x) id) E_1 ) = u_m' . e_1^T rho(X)^mu v(N),     mu := -m,
with units u_m, u_m' that do not depend on N (u_m' = u_m lambda_X^-m, lambda_X the eigenvalue of X^ on E_1).
 Proof. Step 1 (slide). Slide v_bot along A_out (downwards, through infinity, and down from the top) to a point v_bot'
 just above v_top, dragging x = 3 along the right side of A_out. As in Lemma 0.1 this is an isotopy of Theta in S^3 (a
 planar isotopy in the projection sphere, through the empty outer region), and afterwards x = 3 is a short arc from
 the r2 cap to v_bot'. Step 2 (read upwards). Read the new picture from the bottom up: the u1 cup is a band cap E_1
 with legs x = 1 (leg 1, next to the axis) and x = 2 (leg 2); N acts on (axis, leg 1); then the m crossings act on
 the two legs; at the top leg 1 meets the axis at v_top and leg 2 (through the r2 cap and the short arc) meets the
 axis at v_bot' just above it: this is phi. Step 3 (rotate). Apply R (0.3, Lemma 1.2), an orientation-preserving
 isometry of S^3 that preserves brackets and crossing types, keeps the axis on the left and the legs at x = 1, 2, and
 turns the bottom-up reading into the top-down TH-2BR reading (E_1 = l1 cap at the top, phi at the bottom). It maps
 N to R(N) and the m crossings to m y-crossings of positions 0 and 1, i.e. the TH-2BR letters (y1)^m, and y1 is the
 inverse crossing of x1 <-> X^. All moves are regular isotopies. Hence <Theta> = <C_m, N> =. phi(X^^-m (R(N) (x) id) E_1),
 and [R(N)] = [N] by Lemma 1.2. The units come only from normalising phi(E_1), E_1, X^ (u_m, u_m'), not from N. QED
COROLLARY (sign dictionary; PROVED). A y1 twist of the special region is rho(X)^-1 (mu = -m); an x1 twist is rho(X).

THEOREM 2.3 (THEOREM N; PROVED). For a necklace with boxes B_1, ..., B_n and special region C_m, mu = -m:
        J =. e_1^T X^mu (v_1 * v_2 * ... * v_n),     v_i = v(B_i),
        (1 + t + t^2) J =. w_1 A + w_3 B,   w_1 = t + (1 + t^2)(-t)^mu,   w_3 = (1 + t^2)(1 - (-t)^mu),
        A = prod_i a(v_i),  B = prod_i b(v_i),  a(v) = v_1,  b(v) = v_1 + (1 - t^3) v_2.
 Proof. 0.2, Proposition 2.2 and Theorem 1.5 (v(N) = v_1 * ... * v_n, commutative). Closed form: rho(X) is upper
 triangular with diagonal (1, -t), so for every integer mu, (X^mu)_12 = (1 - t^4)(1 - (-t)^mu)/(1 + t) and
        e_1^T X^mu = ( 1 , (1 - t)(1 + t^2)(1 - (-t)^mu) ).
 With h_1 = (1, 1/(t^3-1)), h_3 = (0, 1/(1-t^3)) (Lemma 1.4) and (1-t)/(1-t^3) = 1/Phi_3:
        e_1^T X^mu h_1 = 1 - (1+t^2)(1-(-t)^mu)/Phi_3 = w_1/Phi_3,    e_1^T X^mu h_3 = (1+t^2)(1-(-t)^mu)/Phi_3 = w_3/Phi_3.
 Since v(N) = A h_1 + B h_3, e_1^T X^mu v(N) = (w_1 A + w_3 B)/Phi_3. QED
 So gamma_c(C_m) =. e_1^T X^mu h_c: the special region is the row vector (w_1, w_3)/Phi_3 in the channel basis.
REMARKS. (1) mu = 0: w_1 = Phi_3, w_3 = 0, so J = A: the untwisted special region kills the P_3 channel. Independent
 check: with m = 0 the closure graph with N := P_3 (fuse to colour 3) is planar and contains the empty bigon formed by
 the axis piece and the arc piece from v_top to the box, whose outer legs are A_out (colour 1) and the colour-3 edge;
 a bigon with distinct outer colours is 0. (2) Two channels in the twist site, independently of TH-2BR's matrices:
 fuse the two strands of the twist site, V_2 (x) V_2 = V_0 + V_2 + V_4; the m crossings act by lambda_d^m. After
 fusing the box to colour c too, the closure graph is a planar prism; its face bounded by A_out and the two arc edges
 at v_top, v_bot is a triangle with outer colours (1, d, 1), which vanishes unless d in {0, 2}. Hence
 gamma_c(C_m) = alpha_c + beta_c (lambda_2/lambda_0)^m, ratio (-t)^-m = (-t)^mu, as in w_1, w_3. (3) Phi_3 divides
 w_1 A + w_3 B automatically for integral v (w_1 A + w_3 B = Phi_3 e_1^T X^mu v).

## 3. Half-diagram realisation; vectors of bodies; twist rows

DEFINITION 3.0 (body). A BODY is a half-diagram word B (no 's.') which, run on one half-strand at position 0, only
uses positions it occupies or creates (crossings x_i/y_i with both positions present, cups/caps likewise), ends with one
half-strand, and closes no component. In a context with further strands outside (larger positions), the same letters
act on the same strands, and the outer strands are shifted by the body's caps and cups but never crossed.

LEMMA 3.1 (bodies are boxes; sphere argument; PROVED). Let B be a body inside any symmetric half-diagram. Upstairs, the
slab between the horizontal lines just above and just below B, cut off just outside B's strands (and capped far away
in depth), is a ball B~ with h(B~) = B~, meeting Fix(h) in an unknotted segment and K in the strands of B and their
mirrors (outer strands never enter: no letter of B touches them). K n B~ has no closed component and no fixed point of
K (the two fixed points are the start and the final u0, outside every body), so it is two arcs exchanged by h, each
from the top of B~ to its bottom (an arc joining the two top points would be h-invariant, hence contain a fixed point).
So dB~ is an h-invariant Conway sphere meeting Fix(h) twice, and Q_B := B~/h is a ball meeting Theta in the axis
segment and ONE arc of k from top to bottom: a box (Definition 1.0), parametrised by the height (west = top). QED

PROPOSITION 3.2 (half-diagram realisation; PROVED). For bodies B_1, ..., B_n and m in Z, the quotient theta-curve of
        s.r2.(y1)^m.B_1.B_2...B_n.u1
is a necklace whose boxes are Q_{B_1}, ..., Q_{B_n} (stacked top to bottom) and whose special region is C_m. Hence
        J( s.r2.(y1)^m.B_1...B_n.u1 ) =. e_1^T X^{-m} ( v(B_1) * ... * v(B_n) ),    v(B) := v([Q_B]).
 Proof. While the bodies act, the two strands created by r2 are outer strands (pushed outwards, never crossed), so
 Lemma 3.1 applies to every B_i; consecutive boxes share their horizontal discs, and their union N (the region next to
 the axis between the twist region and the u1 cup) is a box whose state is [Q_{B_n}] o ... o [Q_{B_1}]. Its complement
 is the special region C_m of 2.2 by construction. Apply Theorem 2.3. QED
 The order of the boxes is irrelevant (commutativity), and so is the choice of which side the composite box is read
 from (Lemma 1.2).

DEFINITION/PROPOSITION 3.3 (the vector of an arbitrary body is well defined; PROVED). For a body B, v(B) = [l1.B] in
H: the fragment l1.B (B hung on leg 1 of the band cap, leg 2 passing outside) is literally the picture of Definition
1.3 with west = top. It depends only on the box Q_B up to isotopy rel boundary (hence on B only up to moves inside
the body), and not on the necklace in which B sits, on the other boxes, on m, or on B's place in the stack: the
necklace enters only through the functional <C_m, .>, which is the same for all boxes (Proposition 2.1/2.2). Also
v(R(B)) = v(B) for R(B) = the reversed word with caps and cups exchanged (Lemma 1.2).
COROLLARY 3.4 (PROVED). J(s.r2.(y1)^m.N.u1) = J(s.l1.N.(y1)^m.u2) for every product N of bodies: both are
 e_1^T X^{-m} v(N) up to units (Proposition 3.2; Lemma 0.1 and Lemma 1.3). CHECKED 180/180 (check_moves.py).

3.5 Local moves. Letters acting on disjoint sets of positions commute, with the evident index shift by 2 when a cap
or cup at smaller positions is moved past (e.g. r1.y_i = y_{i-2}.r1 for i >= 3): planar isotopy.
LEMMA 3.5 (cap slide; PROVED). For a strand s at position k-1 (before the cap):
        r_k.y_{k+1} ~ r_{k+1}.x_k,     r_k.x_{k+1} ~ r_{k+1}.y_k,     and dually   y_{k+1}.u_k ~ x_k.u_{k+1},  x_{k+1}.u_k ~ y_k.u_{k+1}.
 Proof. In r_k.y_{k+1} the cap is born just left of s and s passes OVER its right leg into the cap (y: over strand
 top-right to bottom-left); in r_{k+1}.x_k the cap is born just right of s and s passes OVER its left leg into the cap
 (x: over strand top-left to bottom-right). As s passes over the cap in both, the cap's maximum slides under s from one
 side to the other (an R2 move of the cap top against s); the final configurations agree. The x-version is the same
 with s under; the cup versions follow by applying R (reverses words, exchanges caps and cups, keeps crossing types).
 QED  CHECKED in context 40/40.
LEMMA 3.6 (folding lemma; PROVED). For every body B and every m in Z, r2.(x1)^m.B.u1 is a body and
        v( r2.(x1)^m.B.u1 ) = X^^m v(B)     (exactly: [l1.r2.(x1)^m.B.u1] = [l1.B.(x1)^m]);   similarly with y1 and X^^-m.
 Proof. (a) l1.r2 creates nested caps, outer (a,b) and inner (L,R): positions [a, L, R, b]. A crossing x1 of the two
 LEFT legs (a, L) just below them equals a crossing x3 of the two RIGHT legs (R, b): Lemma 3.5 (k = 1, s = a) gives
 l1.r2.x1 ~ l1.r1.y2 (inner cap moved out to the left of a); the two caps are now side by side, so l1.r1 = r1.l3;
 Lemma 3.5 (k = 2, s = R') gives l3.y2 ~ l2.x3 (cap (a,b) moved inside); the result r1.l2.x3 is, as an unlabelled
 diagram, l1.r2.x3. (Geometrically: the half twist slides around the U-turn of the doubled cap, a planar rotation by pi,
 which preserves crossing types.) Iterate (and use y for negative m): l1.r2.(x1)^m ~ l1.r2.(x3)^m.
 (b) R and b are outer strands for B and for the u1 cup, so (x3)^m commutes down past B and u1, where R, b sit at
 positions 0, 1: l1.r2.(x3)^m.B.u1 ~ l1.r2.B.u1.(x1)^m.
 (c) In l1.r2.B.u1, B acts on a and u1 joins B's output to L, which runs up into the inner cap and down as R: a snake,
 which straightens (exact Temperley-Lieb relation). So l1.r2.B.u1 ~ l1.B, and [l1.r2.(x1)^m.B.u1] = X^^m [l1.B].
 All moves are regular isotopies, so the identity is exact. QED  CHECKED 840/840 (random bodies, m = +-1, +-2, seven
 different continuations W, comparing J(s.l1.r2.(x1)^m.B.u1.W.u2) with J(s.l1.B.(x1)^m.W.u2)).

PROPOSITION 3.7 (twist rows; PROVED). ROW_j := (r1)^j.y0.y2.y4...y_(2j).(u1)^j (r = 2j+1 crossings) has
        v(ROW_j) =. X^j Y e_1,   and its mirror ROW_j^- := (r1)^j.x0.x2...x_(2j).(u1)^j has v =. X^-j Y^-1 e_1.
 Proof. ROW_0 = y0 and [l1.y0] = Y^ E_1 =. rho(Y) e_1 (TH-2BR). Recursion ROW_{j+1} ~ r2.x1.ROW_j.u1:
 (i) y_(2j+2) commutes with y0, ..., y_(2j) (disjoint positions) and moves past the last j caps with index shift 2
 each, so ROW_{j+1} = r1.y2.(r1)^j.y0.y2...y_(2j).(u1)^{j+1}; (ii) Lemma 3.5 (k = 1): r1.y2 ~ r2.x1, after which the
 positions are [L, s, R] (L = left leg of the new cap, s = incoming strand); the j inner caps, y0, ..., y_(2j) and the
 first j cups act on L exactly as ROW_j (s and R are outer), and the last u1 joins ROW_j's output with s. So
 ROW_{j+1} ~ r2.x1.ROW_j.u1 and Lemma 3.6 gives v(ROW_{j+1}) = X^ v(ROW_j). Mirror: the same with r1.x2 ~ r2.y1,
 X^^-1 and Y^^-1. QED  CHECKED: recursion 56/56 and [l1.ROW_j] = [l1.y0.(x1)^j] 56/56 (j <= 4, both chiralities).
 Closed forms (BRIEF 1, re-derived from the vector): a_r = e_1^T X^j Y e_1 = 1 + t^-3 (1-t)(1+t^2)(1-(-t)^j) and
 b_r = a_r + (1 - t^3)(-t)^j t^-3 [second coordinate of X^j Y e_1 is (-t)^j t^-3].
COROLLARY 3.8 (nested rational bodies; PROVED). For every word w = Y^{a_1} X^{b_1} Y^{a_2} X^{b_2} ... (exponents in Z)
 the body B(w) defined by B(Y^a w') = (y0)^a.B(w') ((x0)^{-a} if a < 0), B(X^b w') = r2.(x1)^b.B(w').u1, B(empty) =
 empty, has v(B(w)) =. rho(w) e_1. Proof: a box stacked on B acts on v(B) through the first two factors and commutes
 with [Q_B] (Lemma 1.3, Lemma 1.1), so v((y0)^a.B) = Y^^a v(B); and Lemma 3.6. QED
 Thus every element of rho(<X,Y>) e_1 is the vector of an explicit body (rational boxes), and twist rows are B(X^j Y).

PROPOSITION 3.9 (computing v(B) from twisted closures; PROVED, CHECKED 50/50). Write alpha_m(B) for the raw bracket
 value of the twisted closure s.r2.(y1)^m.B.u1, i.e. lp.J_raw (the y-coefficient of the drawn quotient tangle divided
 by its infinity-closure monomial, re-indexed in t). Then alpha_m(B) = U_m c(B) e_1^T X^-m v(B) with U_m depending only
 on m (the special region and the twist crossings) and c(B) a unit depending only on B (the blackboard framing of the
 body and its contribution to the monomial of the infinity closure, the same for all m). Since e_1^T X = (1, 1 - t^4):
        v(B) =. ( alpha_0(B)/alpha_0(empty) ,  [ alpha_{-1}(B)/alpha_{-1}(empty) - alpha_0(B)/alpha_0(empty) ] / (1 - t^4) ),
 with alpha_0(empty) = 1, alpha_{-1}(empty) = t^-2. CHECKED: on the 50 random bodies of general_boxes.json this
 two-closure recipe returns an integral vector equal (up to +-t^k) to the brief's vector in 50/50 cases
 (check_vector.py). With NORMALISED J's only, the relative unit between two closures is lost; one closure then pins v
 only up to a finite set of candidates (+-t^k making the division exact), and a third closure is used to select one
 (the brief's test_general2.py: m in {1, 2, -1}, unique in 50/50 cases). That a third closure always suffices is not
 proved here (GAP, irrelevant once raw brackets are used).

## 4. Units and framing

4.1 Inventory of every unit ambiguity (PROVED; this is the complete list for the statements above).
 (U1) Framing of Theta. <Theta>/<Theta_0> depends on the framing of the theta-curve: a full twist of the arc edge
      multiplies it by A^{+-8} = t^{-+2}, of an axis edge by -A^{+-3}. J is DEFINED as the unique signed power of t times
      <Theta>/<Theta_0> with J = 1 mod (t+1)^2 (0.2), which removes (U1).
 (U2) Framing inside a box. A kink on the arc string of a box multiplies [B] by A^{+-8}, on its axis string by
      -A^{+-3}. So [B] and v(B) are defined up to a unit for an unframed box; for a body (blackboard framing) they are
      exact. Bilinearity of * makes the product of the boxes' units one unit in front of J.
 (U3) TH-2BR normalisations: rho(X) = X^/lambda_X, rho(Y) = Y^/theta_1, phi(E_1) = 1 after rescaling, the scale of F.
      These are fixed once; they contribute lambda_X^m and theta_1^k (units) and the universal units u_m, U_m (2.2, 3.9).
 (U4) NOT a unit: the parametrisation of a box (1.6). k full twists of the east disc multiply the state by Y^^k, i.e.
      v -> rho(Y)^k v (a -> a, b -> t^-3k b). In a half-diagram the parametrisation is the height function (Lemma 3.1),
      so (U4) does not arise there; in a Montesinos presentation it is the bookkeeping of integral parts (5.3).
 (U5) The isotopies used (slide through infinity, R, cap slides, folding, zigzags) are regular isotopies: they change
      nothing. (Kinks occur only in the TH-2BR facts "X at the band cap" / "Y at phi", which are not used here.)
 There is no other source of scalars: every identity above is an equality in a 2-dimensional skein space.
THEOREM 4.1 (exact form of Theorem N; PROVED). Let v_i in Lambda^2 be ANY representatives of the normalised body
 vectors (Proposition 4.2: each is determined up to +-t^k_i). For s.r2.(y1)^m.B_1...B_n.u1,
        J = norm( e_1^T X^-m (v_1 * ... * v_n) ),    norm(p) := the unique +-t^k p that is 1 mod (t+1)^2,
 as an identity of Laurent polynomials; changing the representatives multiplies the argument of norm by +-t^{sum k_i}.
 Equivalently Phi_3 J = +-t^k (w_1 A + w_3 B) for one sign and one shift. Proof: (U1)-(U5) and Theorem 2.3.
 Since the exact value is a unit times J and J = 1 mod (t+1)^2, the argument of norm is automatically a unit times a
 polynomial that is +-t^k mod (t+1)^2, so norm is defined. QED
 What normalisation can NOT absorb: the relative scale of v_1 and v_2 inside one vector (it is fixed, Proposition 3.9;
 rescaling v_2 alone changes J in general), and (U4).

PROPOSITION 4.2 (integrality of box vectors; PROVED). For every body B, a unit multiple of v(B) lies in Lambda^2, with
 v_1 = J(s.B). In particular the normalised vector of a body is well defined up to +-t^k, and v(B) lies in the box ring
 R = {(a,b) in Lambda^2 : a = b mod (1 - t^3)}.
 Proof. (a) Expansion. Cable the arc string by two strands with ONE f_2 (it slides along the single edge and is
 idempotent; put it at the ends). The Kauffman expansion of the cabled diagram is sum_M c_M M over crossingless
 (3,3)-matchings M in TL_3, c_M in Z[A,1/A] (closed loops give delta). Sandwiching with 1 (x) f_2 kills e_2, e_1 e_2,
 e_2 e_1 (each has a cap or cup on the cable pair), so [B] = c_1 (1 (x) f_2) + c_e U, U := (1 (x) f_2) e_1 (1 (x) f_2),
 c_1, c_e in Z[A,1/A]. (b) U factors through one strand, so U P_3 = 0, and Tr_q U = Delta_2 (zigzag); hence
 U = (Delta_2/Delta_1) P_1 and a = c_1 + c_e (delta^2 - 1)/delta, b = c_1 (actual amplitudes). (c) Parity: for a fixed
 matching all contributing states have exponents in one class mod 4 (close by a fixed planar closure and use the
 closed-diagram fact); the matchings 1 and e_1 differ by one saddle, so c_1 in A^r Z[A^+-4], c_e in A^(r+2) Z[A^+-4].
 (d) a is a unit times J(s.B) in Lambda (Proposition 2.2 with m = 0: <C_0, N> = u_0' v_1(N) = u_0' a(N); and
 s.r2.B.u1 ~ s.B, 5.2). Since delta = -A^-2 (1 + A^4) is coprime to delta^2 - 1 = A^-4 (1 + A^4 + A^8), delta divides
 c_e; put c_e' := c_e/delta in A^r Z[A^+-4]. Then b - a = -c_e' (delta^2 - 1) = -c_e' t^-1 Phi_3(t).
 (e) Classical limit. At A = 1, delta = -2 and the Kauffman crossing s = 1 + e satisfies s^2 = 1 + 2e + delta e = 1:
 crossing changes and full twists act trivially, R1 gives a sign. Crossing changes unknot and unlink the arc string of
 the box (a 2-string tangle with both strings running bottom to top is homotopic rel boundary to the trivial braid), so
 [B](A=1) = +-(1 (x) f_2)(A=1). As U(1) = -(3/2) P_1(1) and 1 (x) f_2 = P_1 + P_3 are independent, c_e(1) = 0, so c_e'(1) = 0.
 (f) Let u = +-A^(-r-4k) be the unit with u a in Lambda. Then u c_e' in Lambda vanishes at t = 1, so (1 - t) divides it in
 Lambda (monic divisor), and v_2 = u (b - a)/(1 - t^3) = -t^-1 (u c_e')/(1 - t) is in Lambda, v_1 = u a in Lambda. QED
 (Agrees with the data: all 50 bodies of general_boxes.json have integral vectors, and so do all rho(w) e_1.)

## 5. Corollaries

COROLLARY 5.1 (two-channel twisted closures; PROVED). Let N be any product of bodies with vector v = v(N), A = a(v),
B = b(v), and J_mu := J(s.r2.(y1)^{-mu}.N.u1). Then, with one unit for each mu,
        J_mu =. P + Q (-t)^mu,   P = v_1 + (1-t)(1+t^2) v_2 = (t A + (1+t^2) B)/Phi_3,   Q = -(1-t)(1+t^2) v_2 = (1+t^2)(A - B)/Phi_3.
 The two channels are the eigenlines of the band crossing (ratio -t). Consequences:
 (i) Q = 0 iff v_2 = 0 iff A = B iff [N] is a scalar: then J_mu =. J_0 for all mu (one-channel family).
 (ii) P = 0: then J_mu =. Q for all mu (again one channel).
 (iii) If P != 0 and Q != 0, J_mu is a unit for at most finitely many mu: P, Q are in Lambda (Proposition 4.2), and once
     |mu| > span P + span Q + |deg_min P - deg_min Q| + |deg_max P - deg_max Q| the supports of P and Q(-t)^mu are
     disjoint, so span J_mu >= |mu| - (span P + span Q) - const -> infinity.
 Proof. Theorem 2.3 with e_1^T X^mu = (1, (1-t)(1+t^2)(1 - (-t)^mu)); regroup. QED
 (This is the necklace case of the "TWIST-2CH" proposal on the board: a twist family has one channel or finitely many
 flat members.)

COROLLARY 5.2 (equivariant connected sum is multiplicative; PROVED). For bodies B_1, ..., B_n,
        J(s.B_1.B_2...B_n) = prod_i J(s.B_i).
 Proof. (a) s.r2.N.u1 ~ s.N for every product N of bodies: with m = 0 the strands created by r2 (x = 2, 3) run side by
 side from the cap to the u1 level with nothing between them, so the cap slides down to the cup and the resulting
 zigzag straightens (equivariant planar isotopy). (b) Theorem 2.3 with mu = 0: J(s.r2.N.u1) = A = prod_i a(v_i), and
 the case n = 1 gives a(v_i) = J(s.B_i). QED
 Topology: the horizontal plane between B_i and B_{i+1}, closed at infinity, is an h-invariant sphere meeting K in two
 points and Fix(h) in two points (one at infinity); cutting there and closing each side by the h-invariant arc through
 the fixed point gives s.B_1...B_i and s.B_{i+1}...B_n. So s.B_1.B_2 is the equivariant connected sum (at fixed points)
 of s.B_1 and s.B_2, and Corollary 5.2 is a skein proof of the multiplicativity of J recorded on the board (TH-BULLET-SUM).

COROLLARY 5.3 (Montesinos formula; parts as marked). Let K = M(e; R_0, R_1, ..., R_n) be a Montesinos knot drawn with
its rational tangles side by side along a horizontal axis line, each R_i DRAWN in R_x-symmetric position, and h = R_x
(R_x = rotation by pi about the horizontal axis through the middles). Twist columns and nested bodies are drawn so; that
every rational tangle admits an R_x-equivariant diagram is the flip symmetry of rational tangles (standard, recalled,
not re-proved here), and (a)-(b) are stated for such diagrams.
 (a) [PROVED] R_x maps NW <-> SW and NE <-> SE. If R_i has infinity-parity (strings NW-SW, NE-SE) each of its strings is
     R_x-invariant and contains exactly one fixed point; otherwise (parity 0 or 1) the two strings are exchanged and
     contain none. The joining arcs between consecutive tangles are exchanged. Hence h is a STRONG inversion iff exactly
     one tangle, say R_0, has infinity-parity, and then both fixed points lie in R_0.
 (b) [PROVED] In that case the balls of R_1, ..., R_n, enlarged to contain the joining arcs (whose quotients are identity
     boxes), are h-invariant Conway spheres meeting Fix(h) twice; their quotients are boxes Q_{R_i} (Lemma 3.1's argument),
     stacked along the axis, and the complement of their union is the special region C_{R_0} (it contains both vertices).
     The integral part e consists of e crossings centred on the axis; each is a box with state Y^^{+-1} (letter y0/x0), so
     it contributes Y^e: "integral parts act as Y^k", diagonal in the channel basis (a -> a, b -> t^-3e b); absorbing e
     into a neighbouring tangle is re-parametrising its box (1.6). By Proposition 2.1:
            J =. < C_{R_0} , Y^^e o [Q_{R_1}] o ... o [Q_{R_n}] > =. gamma_1(C_{R_0}) A + gamma_3(C_{R_0}) t^-3e B.
 (c) [PROVED for the half-diagram family] If R_0 is the special region C_m of s.r2.(y1)^m. ... .u1 and each R_i is realised by
     a nested body B(w_i) (Corollary 3.8; every odd twist column r = 2j+1 is B(X^j Y), r = -(2j+1) is B(X^-j Y^-1)), then
            J = norm( e_1^T X^-m Y^e ( rho(w_1) e_1 * ... * rho(w_n) e_1 ) )      (Y^e e_1 * v = rho(Y)^e v).
     For pretzel columns this is the brief's formula. CHECKED 109/109 with randomly built nested bodies, random m, e
     (check_nested.py), besides the brief's 4000 + 270 cases.
 (d) [CHECKED by the brief, not re-proved here] mont(m, [r_1..r_n]) is the horizontal-axis inversion of the pretzel
     P(-+2m, r_1, ..., r_n) (Alexander polynomials; mont(1,[3,3]) has the k138 table J of 8_19). The m = 0 case is PROVED:
     by Corollary 5.2 the knot is the equivariant connected sum of the s.ROW_{j_i}, and the symmetric diagram of s.ROW_j
     is one twist region of 2j+1 crossings closed up, i.e. T(2, 2j+1); so J = prod_i a_{r_i} with a_r = J(T(2,r)).
 (e) [CONJECTURE] Every R_x-symmetric rational tangle of parity 0 or 1 is the quotient-box of a nested body B(w), with w read
     off a continued fraction as in TH-2BR 1.3 for two-bridge knots (C(a_1, 2b_1, a_2, ...) <-> Y^a_1 X^b_1 Y^a_2 ...), and a
     general infinity-parity R_0 gives a special region whose functional is e_1^T rho(W_0) for a word W_0 (5.4).

COROLLARY 5.4 (two-bridge special regions; PROVED). For every word W in y0^{+-1}, x1^{+-1} and every product N of bodies,
        J(s.l1.N.W.u2) =. e_1^T rho(W) v(N).
 Proof. Lemma 0.1 and [l1.N.W] = rho^(W) [l1.N] = rho^(W) v(N) (TH-2BR for the letters of W). QED
 So the special region "band cap + W + phi" acts on box vectors by the functional e_1^T rho(W); C_m is the case
 W = (y1)^m (Corollary 3.4). The general two-bridge special region interacts with boxes through all of rho(W), not only
 through X-powers.

## 6. Spot checks (exact, pure Python lp.py; each run < 2 minutes; scripts in this folder)

These only test identities that are PROVED above; they guard against sign/handedness slips in the written proofs.
 check_moves.py  (25 random flat_search.gen bodies + rows ROW_1..3, ROW_1^-, ROW_2^-; continuations W in
                 {'', y1, x1.x1, y0, y0.x1, x0.y1.y1, y1.y0.x1.x0}):
     Corollary 3.4  J(s.r2.(y1)^m.B.u1) = J(s.l1.B.(y1)^m.u2), m in [-2,3] ............................ 180/180
     Lemma 1.2      J(s.l1.B.W.u2) = J(s.l1.R(B).W.u2)  (R = reverse, caps <-> cups) ................. 210/210
     Lemma 3.6      J(s.l1.r2.(x1)^m.B.u1.W.u2) = J(s.l1.B.(x1)^m.W.u2), m = +-1, +-2 ................. 840/840
     Prop. 3.7      ROW_{j+1} ~ r2.x1.ROW_j.u1 (both chiralities, j <= 3, in context) ..................... 56/56
     Prop. 3.7      [l1.ROW_j] = [l1.y0.(x1)^j] (resp. x0, y1) in context .................................. 56/56
     Lemma 3.5      l1.r1.y2.u1.B... = l1.r2.x1.u1.B... ........................................................ 40/40
 check_vector.py Proposition 3.9: two raw closures (m = 0, -1) reproduce the brief's three-closure vectors of all 50
                 bodies in general_boxes.json, up to +-t^k, and are integral (Prop. 4.2) ........................ 50/50
                 (raw units of the empty body: alpha_0 = 1, alpha_{-1} = t^-2).
 check_nested.py Corollaries 3.8 / 5.3(c): necklaces of 1-3 nested bodies B(w), w random of length <= 5, random
                 m in [-3,3] and integral part e in [-2,2], against norm(e_1^T X^-m Y^e (*_i rho(w_i) e_1)) .......... 109/109
 check_special.py Corollary 5.4: J(s.l1.B.W.u2) = norm(e_1^T rho(W) v(B)) for 30 bodies, random W of length <= 5 ... 120/120
 Together with the brief's evidence (4000 + 270 pretzel cases, 150 + 120 random-body cases), no mismatch is known.

## 7. Status of every claim

 PROVED  Lemma 0.1 (TH-2BR closure of any fragment), given TH-2BR-A and the theta-curve formula for J (TH-2BR 2.2).
 PROVED  Lemma 1.1: End(V_1 (x) V_2) = C P_1 (+) C P_3, commutative; channel amplitudes multiply under stacking.
 PROVED  Lemma 1.2: box states are invariant under the pi-rotation R.
 PROVED  Lemmas 1.3-1.4, Theorem 1.5: v : End -> H is an isomorphism of modules; h_1 = (1, 1/(t^3-1)), h_3 = (0, 1/(1-t^3));
         a(v) = v_1, b(v) = v_1 + (1-t^3) v_2; the star product formula; rho(Y) diagonal (a, b) -> (a, t^-3 b); identity box (1,1).
 PROVED  Proposition 2.1 (trace pairing), Proposition 2.2 (special region C_m = e_1^T X^-m, sign dictionary y1 <-> X^-1),
         Theorem 2.3 = THEOREM N with the closed form Phi_3 J = w_1 A + w_3 B.
 PROVED  Lemma 3.1 (bodies are boxes), Proposition 3.2 (s.r2.(y1)^m.B_1...B_n.u1 is a necklace with boxes B_i),
         Proposition 3.3 (vectors of arbitrary bodies are well defined), Corollary 3.4, Lemma 3.5 (cap slide),
         Lemma 3.6 (folding lemma), Proposition 3.7 (twist rows X^j Y e_1, mirror X^-j Y^-1 e_1), Corollary 3.8 (nested
         rational bodies realise every rho(w) e_1), Proposition 3.9 (two raw closures determine v(B)).
 PROVED  Theorem 4.1 (exact form up to normalisation; complete list of unit ambiguities, (U4) is not a unit),
         Proposition 4.2 (box vectors are integral: they lie in the box ring R).
 PROVED  Corollary 5.1 (two channels; finitely many flat members unless one channel), Corollary 5.2 (multiplicativity under
         equivariant connected sum), Corollary 5.3(a)(b)(c) (strong inversion iff one infinity-parity tangle; Montesinos
         formula for the half-diagram family, integral parts act as Y^k), Corollary 5.4 (two-bridge special regions).
 CHECKED Corollary 5.3(d): the half-diagram mont(m, rows) is the pretzel P(-+2m, rows) (brief: Alexander polynomials, 8_19);
         the m = 0 case is proved.
 GAP     With normalised J's only, that three twisted closures always single out one vector (unique in 50/50; moot,
         since two raw closures determine v exactly, Proposition 3.9).
 CONJ.   Corollary 5.3(e): every R_x-symmetric rational tangle of parity 0/1 is a nested body B(w) with w from a continued
         fraction, and every infinity-parity rational R_0 gives a special region e_1^T rho(W_0).
 Inputs taken as proved elsewhere: TH-2BR-A (matrices rho(X), rho(Y) on H with basis (E_1, F), phi = e_1^T, letters
 y0 <-> Y, x1 <-> X) and the theta-curve formula J =. <Theta;1,1,2>/<Theta_0;1,1,2> (TH-2BR 2.2); standard Kauffman-Lins
 recoupling (fusion, bubble, twist eigenvalues) and the Kauffman bracket parity fact.
 Not claimed: anything about N(T)/homology, the no-tie lemma for necklaces (open, BRIEF 1), Lemma Q.
