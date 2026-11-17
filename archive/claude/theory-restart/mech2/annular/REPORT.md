# REPORT: lens ANNULAR (sl_2 and the exterior current algebra)

STATUS (started 2026-11-15): in progress. Reading the brief, the derivation notes and the Grigsby-Licata-Wehrli papers. Nothing established yet.
Marking convention: PROVED / CITED (source, statement number, read-now or recalled) / DATA / CONJECTURED.


## 0. Sources actually read (pinned)

- [GLW1] Grigsby-Licata-Wehrli, "Annular Khovanov homology and knotted Schur-Weyl representations", arXiv:1505.04386.
  READ NOW from the TeX source (copy at ~/jones-lanes/theory-restart/mech/annular/src/1505.04386/x/annular_draft_v8.tex). The arXiv
  source numbers theorems, lemmas and propositions with separate counters; my numbers below are counted in that file.
  * Lemma 1: (CKh, d_0, d_-) is a bicomplex; spectral sequence AKh => Kh.  Remark 2: gradings (i, j', k) with j' = j - k:
    d_0 has degree (1,0,0), d_- has degree (1,2,-2)  [so (h,q,k) = (1,0,-2)].
  * Lee deformation dLee = dLee_0 + dLee_+, degrees (i,j',k) = (1,4,0) and (1,2,2).  Lemma 3 (lem:partials): the ten relations among
    d_0, d_-, dLee_0, dLee_+ and the involution Theta.
  * Section 3.2 + Lemma 4: the annular TQFT F: essential circle -> V (or V*), trivial circle -> W = <w_+, w_-> (trivial sl_2 module,
    j' = +-1); merge/split maps are sl_2-maps.  Prop. 1: (CKh, d_0) = F([P(L)]).  Prop. 3: AKh is a bigraded sl_2-representation,
    factoring through the Schur algebra S(2, wrapping number).
  * Prop. 5 (marked points): f = +- sum_i (-1)^i x_i  (alternating sum of the dot operators at the points where an arc from the axis
    to infinity meets the diagram), e = Theta f Theta.
  * Section 5.2: the dg Lie superalgebra sl_2(wedge)_dg with odd generators v_2, v_-2, d, D; Prop. 6: it acts on CKh by
    v_2 -> dLee_+, v_-2 -> d_-, d -> d_0, D -> dLee_0.  Lemma 7 + Prop. 7 (= Theorem 1): sl_2(wedge) = sl_2 (x) Lambda[theta] acts on AKh,
    functorially for annular cobordisms.  The weight-preserving odd element is v_0 = [e, v_-2] = -[f, v_2].
  * Lemma 8: on Kh only f and (v_2 + D) survive; Lemma 9: on Lee homology only [e+f] (diagonal on canonical generators).
  * Prop. 12 (quiver): finite-dimensional graded sl_2(wedge)-modules = representations of the quiver with vertices i >= 0
    (E_i = highest weight vectors of weight i), arrows alpha_i: E_i -> E_{i+2} (from v_2), beta_i: E_{i+2} -> E_i (from v_-2),
    eps_i: E_i -> E_i (from v_0), with the relations listed there.
- [KWZ-lin] Kotelskiy-Watson-Zibrowius, "Khovanov multicurves are linear", arXiv:2202.01460v1.  READ NOW (text of the PDF at
  ~/jones-lanes/theory-restart/lit/kwz-linear/src/kwz-linear.txt, Section 4.1): Definition 4.2 (the A_infinity algebra B^infty: mu_2 as in B,
  higher products from disk sequences, e.g. mu_4(D,S,D,S^k) = S^(k-1), mu_4(D^k,S,D,S) = D^(k-1), mu_4(S,D,S,D^k) = D^(k-1),
  mu_4(S^k,D,S,D) = S^(k-1), mu_6(S,D,S^2,D,S,D^(k+1)) = D^(k-1)); Definition 4.3 (B^*[U] = B^infty (x) F[U], mu_k picks up U^(k-2),
  gr(U) = q^-3 h^-1); Theorem 4.4 (EXTENSION PROPERTY: the curve-form type D structure of any pointed Conway tangle extends to a type D
  structure over B^*[U], recovering the original at U = 0); proof of Theorem 4.1 (no odd power of U occurs, by q-parity).
  Field F_2 there; arXiv:2602.23442 (same authors) redoes it over any field (digest only, not re-read by me).
- Digests written earlier by this project (read now): lit/kwz-linear/REPORT.md, lit/kwz-immersed/REPORT.md, lit/kht/REPORT.md.

- [GLW2] Grigsby-Licata-Wehrli, "Annular Khovanov-Lee homology, braids, and cobordisms", arXiv:1612.05953v1. READ NOW (TeX source
  downloaded to mech2/annular/src/1612.05953/x/SKhTwoVariable_v2.tex): Lemma lem:Leediffgr (dLee = (d_0 + d_-) + (Phi_0 + Phi_+) with
  (i,j,k)-degrees (1,0,0), (1,0,-2), (1,4,0), (1,4,2)); Definition defn:annularRas (d_t(L,o) = filtration grading of the Lee class s_o
  for j_t = j - t k, t in [0,2]); Theorem thm:main (invariance, d_{1-t} = d_{1+t}, d_0 = d_2 = s - 1, piecewise linear with slopes in
  {-w,...,w}, and the cobordism bound |d_t(L,o) - d_t(L',o')| <= (a_1 - a_0) - b_0 (1-t)).

Conventions used below (as in BRIEF2): b = Q_0 = ⬮, c = Q_infty = ⬯; a type D arrow x -> y with label a has h(y) = h(x)+1,
q(y) = q(x) + |q(a)|, q(D) = 2, q(S) = 1.  T(n) = annular closure of T sigma^n in the horizontal direction.  j = quantum grading of the
closure, k = annular weight, j' = j - k.

## 1. TASK 1: the annular dictionary (AKh(T(n)), sl_2, the odd operators) in terms of the type D structure

### 1.0 Topology of the annular link T(n)  [PROVED, elementary]
T = exterior of an arc tau attached to the unknot U = T(infty) (theta-curve U + tau; K = lift of tau to the double cover of U).
T(n) is the result of the band move on U along a band with core tau and n half twists.  The axis of the annulus is isotopic to the
curve of slope infty on the Conway sphere (it bounds a disc in the filling ball that separates the two strands of Q_infty), i.e. to the
meridian circle of the band: it bounds a disc meeting T(n) in the two parallel strands of the band (a crossing circle).  Cutting the band
is an annular saddle cobordism T(n) -> U, and U is inessential.  For n even T(n) = kappa_1 + kappa_2, the two constituent knots of the
theta-curve other than U, each winding once; for n odd T(n) is a knot winding twice.  The axis lifts to two parallel copies of the
meridian of K, i.e. of the core of the surgery solid torus in S^3_n(K) (this is the picture behind Theorem S).

### 1.1 The unreduced algebra  [PROVED; agrees with Codex TH-UNRED-LIFT, independent derivation]
Over F_2, dotted cobordisms with x^2 = Hx: x_* = dot on the special sheet (central), x_2 = dot on the other sheet of b.
  D_b = x_2 + x_*,  S_c S_b = tube = x_* + x_2 + H,  so D S = S D = 0 and D + S^2 = H persist, and the unreduced two-object algebra is
  A = B (x)_{F[H]} F[H][x_*]/(x_*^2 + H x_*).
LEMMA U (F_2). The unreduced complex of T is the induced one, C(T) = BN~(T) (x)_B A (same generators, arrows with labels in B).
Proof. sigma: x -> x + H on every dot is an automorphism of the dotted cobordism category over F_2 fixing B and the saddles;
nu := (sigma - 1)/H is a sigma-derivation with nu^2 = 0, nu(d) = 0 and nu x_* + x_* nu = sigma.  On M = Hom(b + c, [[T]]) this gives
M = nu M (+) (x_* + H) nu M as complexes of right B-modules (graded Nakayama for the second summand), i.e. M = nu(M) (x)_{F[H]} A_H. QED
(For H = 0 this is Shumakovitch's argument.)  CONSEQUENCE: over F_2 the "dot on the second strand" carries no information beyond
BN~(T); the mechanism proposed in BRIEF2 section 3 for the shape law cannot work in this form.  The correct enlargement is in section 2.
Characteristic 0 (signs as in KWZ: H~ := D - S^2 = -(handle on the special sheet) = H - 2 x_*, D = x_2 - x_*): the subalgebra
generated by D, S is B with central element H~, x_*^2 = -H~ x_*, and setting H = 0 gives x_* = -H~/2, H~^2 = 0.  So unreduced Khovanov
homology over Q is the reduced Bar-Natan type D structure with H~^2 set to zero (this is "Kh = L_2" in KWZ, arXiv:1910.14584
Remark 6.13, CITED from the project digest lit/kwz-immersed/REPORT.md, not re-read).

### 1.2 The annular module  [PROVED]
Let X = BN~(T sigma^n), a reduced type D structure over B (no identity arrows), X_b, X_c its generators.  The Khovanov complex of the
annular closure is X [x] M with
   M(b) = V (x) V  (two essential circles; basis 11, 1x, x1, xx; k = 2, 0, 0, -2; j-shift 2, 0, 0, -2; first factor = special circle),
   M(c) = W        (one trivial circle; basis 1, x; k = 0; j-shift 1, -1),
   D_b = 1(x)X - X(x)1  (= X(x)1 + 1(x)X over F_2),   S_b = merge,   S_c = split,   D_c = 0,
   hence S_c S_b = split.merge = X(x)1 + 1(x)X on M(b),  S_b S_c = merge.split = 2X on M(c)  (0 over F_2),  H~ = -2 x_*.
Splitting by weight (Roberts' lemma, [GLW1] Lemma 1): d_0 = { S: b->c on 1x, x1 -> x;  S: c->b on 1 -> 1x + x1;  S^2: c->c on 1 -> 2x },
d_- = { D on b;  S: b->c on 11 -> 1;  S: c->b on x -> xx }.
PROPOSITION 1.  (a) AKh(T(n); k = +-2) = X_b (x) 11 resp. X_b (x) xx with zero differential: this is N(T), at j = q +- 2.
(b) AKh(T(n); 0) is the homology of the complex on X_c(x)<1,x> (+) X_b(x)<1x,x1> with differential
        c(x)1 -> y(x)(1x + x1)  for every S-arrow c -> y,      c(x)1 -> 2 c'(x)x  for every S^2-arrow c -> c',
        x(x)1x, x(x)x1 -> z(x)x  for every S-arrow x -> z.
    Over F_2 it is the direct sum  [X_c(x)1 -> X_b(x)(1x+x1)] (+) [X_b(x)1x -> X_c(x)x].
(c) f = D_b (the sl_2 lowering operator is the action of the algebra element D on the b-generators; [GLW1] Prop. 5), e = Theta f Theta,
    both zero on W.  e, f commute with d_0 and f commutes with d_-.
(d) v_-2 = d_- acts on N by   x (x) 11  |->  f.(d_D x) (x) 11  +  [z (x) 1],   z = the c-generator at the end of the S-arrow leaving x
    (first generator of a P-run or of the tail starting at x), zero if there is none.
(e) v_0 = [e, d_-] acts on N as  2 d_D,  d_D = sum of the D-arrows between b-generators (characteristic 0; chain level identity).
    Its bidegree is (h,q) = (1,2).  In characteristic 2 this operator vanishes and d_D is its divided form.
(f) The saddle S enters only through the two maps  beta: N -> M_0 (x -> [first c-generator of the run leaving x] (x) w_+)  and
    alpha: M_0 -> N ([last c-generator of a run] (x) w_- -> endpoint of the run), M_0 = multiplicity space of V_0.
    beta is injective on the span of the P-sources (and of rho if the tail leaves rho); im(alpha) = span of the P-targets.
(g) The run P = S D S^2 D S is NOT an operator of the current algebra: its three inner arrows act by zero on W (D_c = 0; S_c^2 = 2X
    only matches w_+ to w_- inside one run in characteristic 0).  d_P relates beta(x), which lies in delta' = delta(x), to the
    alpha-preimage of Px, which lies in delta' = delta(x) - 1, by a correspondence [c_1 (x) w_+] ~> [c_4 (x) w_-] of bidegree (3,4).
    This is a secondary operation.  In the A_infinity language of section 2: mu_6(S,D,S^2,D,S,D^2) = U^4, "P is inverse to D^2 after
    filling the special puncture".
(h) Every operator of sl_2(wedge) preserves delta' := j'/2 - h = (j-k)/2 - h (degrees (0,0,+-2), (1,2,0), (1,2,+-2) in (i,j',k)).
    So AKh(T(n)) is the direct sum over delta' of sl_2(wedge)-modules; the rows b = -delta of N are the highest weight spaces of the
    summands, and the current algebra never connects two rows.  ([GLW1] does not state this; it is immediate from Remark 2 there.)
Proofs: (a),(b) by inspection of M; (c) [GLW1] Prop. 5 and Lemma 5; (d),(f) read off d_-; (e): for a D-arrow x -> y,
d_-(x(x)11) contains y(x)(1x - x1) and e(1x - x1) = 2.11 with the signs of [GLW1] (V (x) V^*); e kills W and weight 2; (h) degrees.
CHECK (scripts/annq2.py, exact arithmetic over Q, on the unit square with either local system, the zigzags of length 3 and 5 and the
point): all relations of sl_2(wedge) hold on homology; v_0|_N = 2 d_D on the nose; dim H(AKh, v_-2) = dim Kh(.;Q) in every case.
CHECK over F_2 (scripts/annh.py on the saved chain file of 9_42, k = j = 0, m = 4): dim AKh = 9 + 34 + 9 = 52 = 12m + 4,
dim Kh(T(0)) = 36 = 8m + 4, the spectral sequence degenerates at E^2.

### 1.3 Shape of the module for wrapping number two  [PROVED from [GLW1] Prop. 12]
E_2 = N, E_0 = M_0(n), E_i = 0 otherwise.  The quiver relations reduce to: eps_2^2 = 0, eps_0^2 = 0, alpha beta = 0 = beta alpha,
eps alpha + alpha eps = 0, eps beta + beta eps = 0 (eps_2 = v_0/2 = d_D on N).  So an sl_2(wedge)-module with weights in {2,0,-2} is
a pair (N, M_0) with three anticommuting square-zero maps eps, alpha: M_0 -> N, beta: N -> M_0.  The complex (AKh, v_-2) is
        N --(2 beta, eps)--> M_0 (+) N --(-alpha/6, eps)--> N           (weights 2, 0, -2; bidegree (1,0) in (h,j)),
and Kh(T(n)) = its homology whenever the annular spectral sequence degenerates at E^2 (true in all the checks above).
Standard pieces (characteristic 0): unit square: N = 4, M_0 = 8, Kh = 8; point: N = 1, M_0 = 1 (AKh = V (x) V), Kh = 4.
In characteristic 0, E^infty in weight 2 = sinks of N (b-generators with no outgoing D and no outgoing S), weight -2 = sources.
Over F_2 (where f.[z (x) 11] can die): weight 2 = top rows of the squares, weight -2 = bottom rows (each square: 2 + 12 + 2 of its 16).

### 1.4 Lee theory inside each weight; why H(N, d_D) = F  [PROVED over Q given [GLW1] Section 5.2; the eigenvalue statement RECALLED]
In sl_2(wedge)_dg one has (d + D + xi.theta)^2 = (Q(xi) - 1) x for xi in sl_2, Q = -det, x = [v_2, v_-2] = -[d, D].  Lee's differential is
xi = e + f.  Conjugating by exp(-f/2) exp(e) (e, f are locally nilpotent and commute with d, D) turns it into
        d_h := d_0 + dLee_0 + [e, d_-]            (xi = h),
which PRESERVES THE ANNULAR WEIGHT, and turns e + f into h.  Hence H(CKh, d_h) = Lee homology, split by weight, and the weight of the
class of an orientation o is the eigenvalue of e + f on s_o, which is the winding number of (L, o) around the axis ([GLW1] Lemma 9
says e + f is diagonal on the s_o; the value is the signed number of essential circles of the oriented resolution; RECALLED form).
For T(n): exactly one orientation class (up to reversal) winds twice.  So there is a spectral sequence
        N(T) = AKh(T(n); 2)  ==>  F  (one generator),   first differential v_0 = 2 d_D (bidegree (1,2)), later ones raise q by 4, 6, ...
Under the shape law it degenerates after d_D: H(N, d_D) = F x_0.  Independent explanation of the same fact: H(X (x)_B F[D, D^-1]) counts
the ends of the arc of BN~(T) at the puncture p1 = BL, and the arc of BN~(T) joins BL and BR (KWZ arXiv:1910.14584 Prop. 6.15, CITED
via digest), so exactly one end: x_0 is "the Lee generator of T(n) that winds twice".


## 2. TASK 2: the SHAPE LAW is a theorem for unit arrows (proof via the extension property of KWZ)

Status in one line: the mechanism proposed in the brief (dots on both strands) is REFUTED (Lemma U, 1.1), but the conclusion is
PROVED from a different enlargement of the reduced theory that is already in the literature: the U-deformation B^*[U] of
Kotelskiy-Watson-Zibrowius (Rasmussen's d_{-1} / filling in the special puncture).  There a composable pair "D then P" does have a
non-zero composite: a mu_4 product equal to S U^2.

### 2.1 Input  [CITED, read now: KWZ arXiv:2202.01460 Def. 4.2, Def. 4.3, Thm 4.4, proof of Thm 4.1]
B^infty: the A_infinity algebra with the multiplication of B and higher products from disk sequences; the ones needed are
    mu_4(D,S,D,S^k) = S^(k-1),  mu_4(S^k,D,S,D) = S^(k-1),  mu_4(D^k,S,D,S) = D^(k-1),  mu_4(S,D,S,D^k) = D^(k-1)     (k >= 1),
and mu_4 vanishes on every other 4-tuple of basis elements; mu_2m (m >= 3) needs an argument D^j with j >= 2 (each interposition raises a
D-power).  B^*[U] = B^infty[U] with mu_k weighted by U^(k-2), gr(U) = q^-3 h^-1.
EXTENSION PROPERTY (Thm 4.4): for every pointed Conway tangle the curve-form type D structure of BN~(T) is the U = 0 reduction of a
type D structure over B^*[U] on the same generators: delta = delta_0 + U^2 delta_2 + U^4 delta_4 + ... (odd powers are excluded by the
parity of q; proof of Thm 4.1).  The structure equation in degree U^2 reads
    (*)   mu_2(delta_0, delta_2) + mu_2(delta_2, delta_0) + mu_4(delta_0, delta_0, delta_0, delta_0) = 0.
Proved over F_2 in that paper; arXiv:2602.23442 states the same over every field (digest only).

### 2.2 Statement
Curve form: every generator is incident to at most one arrow labelled by a power of D and at most one labelled by a power of S (the two
sides of the parametrising arc).  A component gamma has UNIT ARROWS if (U1) every arrow between two b-generators is labelled D, and
(U2) every maximal chain of c-generators between two b-generators x, y is a run  x -S-> c_1 -D-> c_2 -S^2-> c_3 -D-> c_4 -S-> y
with all five arrows in the same direction (write x -P-> y).  A junction (a b-generator with its D-arrow and its run) is COMPOSABLE if
one of them enters and the other leaves.

THEOREM A (PROVED given Thm 4.4 of KWZ).  Let T be a pointed Conway tangle and gamma a component of BN~(T), in curve form with a
one-dimensional local system, having unit arrows.  Then gamma is
  (i) the unit square: four b-generators x, x+D, x+P, x+D+P with arrows x -D-> x+D, x -P-> x+P, x+D -P-> x+D+P, x+P -D-> x+D+P
      (12 generators), trivial local system; or
 (ii) non-compact with no composable junction: along gamma the moves alternate P, D, P, D, ... and every b-generator is a source or a
      sink, so all P point one way and all D the other way (a zigzag / staircase).
COROLLARY (shape law).  If all components of BN~(T) have unit arrows (apart from the tail of the arc, which contains no b-generator),
then N(T) = Z_l (+) Lambda^r over Lambda = F[d_D, d_P]/(d_D^2, d_P^2), with exactly one zigzag (KWZ Prop. 6.15: one arc) and r squares,
H(N, d_D) = H(N, d_P) = F.  This is the b-part statement asked for in BRIEF2 section 3.

### 2.3 Proof
Let w -D-> x -P-> y be a composable junction "D then P", with x -S-> c_1 -D-> c_2 -S^2-> c_3 -D-> c_4 -S-> y.
Step 1. The path w, x, c_1, c_2, c_3 has labels (D,S,D,S^2), so mu_4 contributes S U^2 from w to c_3 in (*).  The other terms of (*)
from w to c_3 are products a.b = S of one delta_0-arrow and one U^2-arrow.  Arrows of delta_0 into c_3: only c_2 -S^2-> c_3 (a.S^2 = S
is impossible).  Arrows of delta_0 out of w: D (D.b = S impossible) and, if it exists, the S-arrow w -S-> c_1' (then b = 1).  No other
path of length four leads from w to c_3.  Hence: w starts a run  w -S-> c_1' -D-> c_2' -S^2-> c_3' -D-> c_4' -S-> y',  and delta_2
contains c_1' -U^2-> c_3.
Step 2. c_1' -U^2-> c_3 -D-> c_4 gives D U^2 from c_1' to c_4; the only cancelling term is c_1' -D-> c_2' -U^2-> c_4 (c_4 has no other
incoming arrow, and the 4-path from c_1' has labels (D,S^2,D,S), not a disk sequence).  So delta_2 contains c_2' -U^2-> c_4.
Step 3. c_2' -U^2-> c_4 -S-> y gives U^2 S from c_2' to y.  Products: c_2' -S^2-> c_3' followed by a U^2-arrow would need S^2.b = S;
a U^2-arrow from c_2' followed by an arrow into y would need the arrow c_4 -S-> y again or a.D = S.  So the term must be cancelled by
mu_4 along c_2' -S^2-> c_3' -D-> c_4' -S-> y' -?-> : this is S U^2 exactly when y' -D-> y.  Then w, x, y', y are joined cyclically, each
with both of its neighbours: gamma is the unit square.  (With a local system X on one arrow the three steps give A = X, B = A, B = 1.)
"P then D" (-P-> y' -D-> y): the mirror argument (start from the term c_2' -> y of Step 3 and run the steps backwards) forces the same
square.  So a component with a composable junction is a unit square.  A component without composable junctions has all its
b-generators sources or sinks; if it were compact with 2r b-generators its homological grading would change by r(5 - 1) = 4r around the
cycle, impossible.  QED
The unit square does extend: delta_2 = {c_1' -> c_3, c_2' -> c_4} (U^2 times the identity), and nothing else is needed.

### 2.4 Computational check of the mechanism  [DATA; scripts/uext.py, uenum.py]
uext.py implements mu_2, mu_4, mu_6 of B^*[U] and solves (*) for delta_2 by linear algebra over F_2.
 - unit square: solvable, the solution is exactly the two arrows of 2.3, and the extended structure satisfies the full structure
   equation through order U^4;  zigzags (with or without tail): solvable with delta_2 = 0;
 - an arc containing "D then P", "P then D" or "D then tail": NOT solvable (first-order obstruction);
 - all gradable primitive cyclic words in +-D, +-P_2 with up to 10 moves: 5 classes, only the square passes;
   the same with P_1 only or P_3 only: only the square with those legs passes.
So the theorem's mechanism is confirmed, and the hypothesis is needed:
 - with runs of different lengths (P_1, P_2, P_3 mixed) 6 further cyclic words of 8 moves pass the first-order test (they turn around
   p1; this is the "L > R" situation of KWZ's proof of their Thm 5.1, which for Kh~ is excluded by H.id ~ 0 but for BN~ is not);
 - with D^2 allowed, 6 further words pass (e.g. the square with D^2 sides).
What the general first-order analysis gives without (U2): at a junction w -D-> x -P_L-> the generator w must start a run P_R with
R <= L, and R = L forces the square with legs L (same three steps; this is KWZ's "L <= R" case).

### 2.5 Scope and remarks
 - Theorem A needs only the extension property; it does not use T(infty) = U, the strip, or H.id ~ 0.
 - It explains the two exceptions in the data as failures of (U1): the arc of 9_46 second inversion has a D^2, and so does the arc of
   the double of 8_19 = T(3,4) computed here (kht/examples/dbl/t34, 203 s): BN~ = 8 unit squares + an arc with 9 b-generators and
   two D^2 arrows; dim N = 41 (20 specials + r(16)), while rank HFK^(8_19 # 8_19) = 25 = rank Kh~(8_19)^2.  [DATA, new: first double of
   a thick knot; the Theorem S sequence does not collapse here (defect 8), and N is not Kh~ (x) Kh~.]  NP and END hold for it
   (top q at one generator (24,46), bottom at (0,12)).
 - In these examples all COMPACT components are still unit squares.  Not proved in general: a compact component could have a D^2 side or
   unequal legs as far as the first-order obstruction is concerned.
 - The zigzag arc is not linear in the sense of KWZ: travelling along it the moves read +P, -D, +P, -D, i.e. the peg-board
   representative turns at a lift of p1 at every step (a spiral around five punctures of the special line, l turns).  Wrapping around
   p1 is allowed for BN~; wrapping around * (+P,+D,+P) is exactly the composable pattern excluded above (KWZ Thm 4.1).
 - Group-theoretic picture (PROVED, elementary): the strip covers a disc U around the arc [*, p1]; with beta = loop around p1 inside
   A_b and gamma = loop around A_b, D^a = beta^(+-a), P_n = gamma^(+-n), a compact component is a cyclic word in these, the unit square is
   the commutator [beta, gamma^2], and the special curve called s_2n by kht++ is [beta, gamma^n].

## 3. TASK 3 (main question): the annular package does NOT constrain the bigradings of N beyond B0  [PROVED NEGATIVE]

### 3.1 The formal computation for B0 = a(0) + S + hS and its twists
BN~(B0 sigma^n) = a(n) (+) S (+) hS (twisting fixes the compact components of slope infty and only changes the arc).  By section 1 the
whole package is computed generator by generator from the type D structure, so
   AKh(B0(n)) = AKh(closure of sigma^n) (+) AKh(S) (+) AKh(S)[h-shift 1]      as trigraded sl_2(wedge)-modules,
with (characteristic 0) AKh(S) = Lambda (x) V_2 (+) M_0(S) (x) V_0, dim N(S) = 4, dim M_0(S) = 8, H(AKh(S), v_-2) = 8 = the two
special blocks of four, and (F_2) 4 + 16 + 4 -> 16.  N(B0) has dimension 9, J = 1; M_0(B0(n)) = M_0(sigma^n) + 16.  The d_- homology
is Kh(T(2,n)) plus two copies of the block of a square, i.e. exactly the "reduced form HF(a(n), Kh~) of rank 4m + |n - k|" with
m = 4, k = 0.  Lee homology, the weightwise Lee sequence of 1.4 and the annular Rasmussen invariants d_t are those of the two-braid
closure (compact summands are acyclic for every Lee-type differential).  The exact triangles AKh(T(n)) -> AKh(T(n+1)) -> W are the cones
of S and split in the same way.  Every summand is the module of an actual component of an actual tangle (squares at relative offset
(1,0) occur inside actual tangles, 333 times in the data), so no property of sl_2(wedge)-modules can be violated.

### 3.2 Why this is forced: ADDITIVITY LEMMA  [PROVED]
Every ingredient of the package is the value of an additive, shift-equivariant functor on the type D structure X = BN~(T sigma^n):
the complex X [x] M, its weight splitting, d_0, d_-, e, f, the Lee pieces, hence AKh, the current algebra action (quiver data
(N, M_0; eps, alpha, beta)), all pages of AKh => Kh, the weightwise Lee sequence, Lee generators and their filtration levels, the
triangles in n.  If X = X' (+) X'' then everything is the direct sum.  Consequently any statement that (i) holds for every actual
tangle, (ii) is inherited by direct summands of X or is a numerical identity additive in X, and (iii) is invariant under shifting a
compact summand, holds for B0, for Codex's ladder L2, and more generally for
        a(0) (+) C (x) (F (+) F[h-shift 1])
for every compact part C of an actual tangle with k = j = 0 (e.g. C = the two squares of 9_42: point + squares at (1,0), (0,1),
(-3,1), (-4,2) is flat).  The same holds for the U-extension of section 2 (each square extends by itself, and the split extension of a
direct sum is an extension) and for Rasmussen's E(-1) sequence that it induces on closures (differentials of bidegree (2i+1, 6i)).
So: "AKh(T(n)) is a module over the current algebra for every n, its d_- homology is Kh(T(n)), with the stated ranks" is strictly
weaker than what is needed.  What excludes bare B0 (Daemi's plane Floer sequence, board X.17) is not additive in X: its higher
differentials join different components of BN~(T).  Flatness with arc a(0) is equivalent to: the Poincare polynomial of the positions
of the squares is divisible by (1 + h); no additive structure sees divisibility by (1 + h).

### 3.3 What the representation theory does say (all PROVED, none excludes B0)
 - Rows: AKh(T(n)) = sum over delta' of modules; N_b is the highest weight space of the row-b module; beta is injective on the
   P-sources of the row and alpha is onto the P-targets of the row (1.2 (f),(h)).  A P-run from row b to row b+1 contributes two
   classes [c_1 w_+], [c_3 w_+] to M_0 in row b and two classes [c_2 w_-], [c_4 w_-] in row b+1; the only maps that join them are the
   Lee deformation Phi_0 ([c_2 w_-] -> 2 [c_3 w_+], bidegree (1,4)) and the vanishing actions D_c: [c_1 w_+] -> [c_2 w_-],
   [c_3 w_+] -> [c_4 w_-] of bidegree (1,0) (zero because the two dots lie on the same circle).  So the excluded offset (1,0) is the
   bidegree of the two "missing" arrows inside every P-run; the current algebra does not see them.
 - chi(M_0(n)) is a unit for every n (it equals chi(X_b) + (q + 1/q) chi(X_c), the bracket of the unknot closure), while
   dim M_0 = 4m + 1 over Q (6m + 1 over F_2) for k = n = 0: the weight-zero
   multiplicity space is itself a bigraded space with trivial Euler characteristic and large rank.  The package therefore contains an
   honest "trivial Jones, non-trivial homology" object next to N; it gives no reason why N should behave differently.
 - Trapezoid/Schur algebra ([GLW1] Cor. 1, Prop. 2), Weyl-module type structure: N (x) V_2 is generated by the sources of N and the
   classes not in im(alpha); its socle in weight 2 is spanned by the sinks.  No constraint between different rows.
 - Annular Rasmussen invariants ([GLW2] Thm (main)(6)): for n even and the orientation with antiparallel band strands, the band-cutting
   saddle gives |d_t(T(n)) - d_t(U)| <= 1; this bounds the position of the weight-zero Lee generators only.  For the orientation winding
   twice, d_t reads off the bigrading of x_0; cobordisms to the two-braid closure have unbounded genus.  No constraint on squares.

## 4. TASK 4: NP and the pair (d_0, d_-)

### 4.1 What the pair gives  [PROVED]
PROPOSITION 4.  (a) A b-generator of N with no outgoing arrow (a sink) gives a cycle x (x) 11 of the full Khovanov complex of T(n), for
every n; in characteristic 0 the weight-2 part of E^infty is exactly the span of the sinks, the weight -2 part the span of the
sources (F_2: top rows / bottom rows of squares).  (b) A generator of maximal q in N is a sink (an outgoing D raises q by 2, an outgoing
run by 8), unless it is rho with the tail leaving it.  Hence N_top embeds in Kh(T(n)) at j = q_max + 2 with the same homological
degrees, as the top annular filtration quotient, and dually N_bot embeds at j = q_min - 2 as the bottom filtration piece.
(c) NP at the top  <=>  gr_2 Kh(T(n)) in quantum degree q_max + 2 is supported in one homological degree (any n).
(d) d_- preserves delta', d_0 lowers it by one, and E^1 = AKh splits by delta' as a module; so (d_0, d_-) computes Kh(T(n)) row by row:
   Kh(T(n)) = sum over rows b of H( N_b -> M_0,b (+) N_b -> N_b ).  Two generators of N in the same q on different rows lie in different
   summands.  The pair (d_0, d_-) therefore carries no relation between rows, and NP (a statement about two rows) cannot follow from a
   weight or purity argument for this pair alone.  The relation between rows is d_P, a secondary operation (1.2 (g)).
So the answer to task 4 is negative in this precise sense.  The coincidence "(1,0) = bidegree of d_-" has the following content only:
(1,0) is the bidegree of every first-page differential of Khovanov type, and inside a P-run it is the bidegree of the two arrows D_c
that act by zero on a single circle.

### 4.2 A caution for any purity argument at the level of closures  [DATA, new]
Purity of the extreme quantum degree is FALSE for reduced Khovanov homology of knots, already for an unknotting number one knot that
is a closure of the simplest quotient tangle:  10_132 (4-braid 1,1,1,-2,-1,-1,-2,-3,2,-3,-3; kht/examples/knots/k10_132) has
Kh~ of rank 11 with top quantum degree q = -2 carried by (h,q) = (0,-2) and (-1,-2): the Euler characteristic of the top degree is 0
and the offset between the two generators is exactly (1,0).  This knot is the closure T(-5/2) of the quotient tangle of the trefoil
(kht/examples/clos/cx1x1y0y0: identical reduced Bar-Natan homology; Sigma(10_132) = S^3_{-5/2}(trefoil) up to mirror, distance 2 from
the unknot closure).  The cancellation is between the pairing of the arc with the rational component and with the special component.
So a mechanism for Lemma Q through extreme coefficients has to be formulated for N (tangle level), not for the closures K_n or T(p/q),
and "purity at the top of Kh~ of a closure" is not available as a lemma.  A random search of 11,500 width-5 plats with 10, 12, 14
crossings found no other knot type with an impure extreme (only 10_132 and its mirror).

### 3.4 Explicit check of 3.1  [DATA; scripts/b0check.py, exact arithmetic over Q]
                          dim N   chi_q(N)                 dim AKh (weights 2,0,-2)   dim M_0   dim H(AKh,v_-2) = dim Kh(Q)   dim H(AKh,v_0)
 point a(0)                 1     1                         4  (1, 2, 1)                 1         4                            4
 B0 = a(0) + S + hS         9     1  (J = 1)                44 (9, 26, 9)                17        20                           12
 9_42 (actual tangle)       9     8 non-zero coefficients   44 (9, 26, 9)                17        20                           12
All sl_2(wedge) relations hold on homology in each case.  B0 and the actual tangle 9_42 give modules that differ only by regrading
one summand: nothing in the module theory, the d_- homology or the weightwise Lee sequence distinguishes them.

### 2.6 Addendum: unequal legs and D^2 at first order  [DATA; scripts/uext.py]
 - junction w -D-> x -P_L->, with w -P_R->: R > L and "R = L without the closing D" are obstructed at order U^2; R < L is not
   (R = L-1: a U^2 arrow between the two run ends; R = L-2: a U^2 S arrow).  So without (U2) the first-order statement is exactly
   "the run at the tail of a D is not longer than the run at its head, with equality only in a square".
 - "D^2 then P_2" and "P_2 then D^2" pass the order U^2 test; their obstruction sits at order U^4 (mu_6(D^2,S,D,S^2,D,S) = U^4), which
   I did not analyse beyond noting that the D^2-square [beta^2, gamma^2] cancels it.  In both examples with a D^2 (9_46 second
   inversion, double of 8_19) the D^2 arrows sit at non-composable junctions: the arc is still a zigzag, with some D replaced by D^2.

### 3.5 A second small formal flat object, and its fate  [DATA; scripts/b1match.py]
For (k,j) = (-4,0) flatness needs exactly one (net) square at the "virtual" position.  The actual tangle 5_2 second inversion is
3-zigzag + one square; shifting its square by (h,q) = (3,6) (three D-steps, the bidegree of a U^2 arrow) gives a formal object
B1 with dim N = 7 and J a unit: three corners of the shifted square are (1,0)-shifts of the three zigzag generators.  B1 has the same
ranks and delta-levels on all closures as the actual tangle and trivial Jones polynomial on K_n, but the largest matching by pairs of
bidegree (r, 2r-2), r >= 2 leaves 3, 5, 5, 7, 9, 9 generators on the closures of slope +1, -1, +1/2, -1/2, +1/3, -1/3 (the actual
tangle: 1 each time).  So B1, like bare B0, is excluded by Daemi's MATCH and by nothing in the annular package.  (The pairing engine
is the project's lit/kwz-linear/calc/hf.py; the check reproduces rank 16n +- 1 and the matching to 1 for the actual tangle.)

### 2.7 The double of 8_19 in lattice coordinates  [DATA; scripts/gridbn.py on kht/examples/dbl/t34/cxBNr-c2-d]
dim N = 41, 8 unit squares + arc with 9 b-generators (two D^2 arrows, each D^2 = 6D - P in lattice terms).  Rows b = 1 ... -6:
   [. 1 2 1], [1* 1 2 2 1 1 1], [. . . 1 2 2 3 1], [4: 1 1 2 2 . 1 1], [7: 1 . 1 2 1], [10: 1 1 . 1], [13: 1 1], [14: 1]   (a from 0 to 14).
J has 9 non-zero coefficients (q = -20, -14, -8, -6, 0, 6, 8, 12, 14 relative to rho), and N is non-zero with vanishing Euler
characteristic in seven interior q-degrees: heavy cancellation, none at the ends.  NP and END hold (one generator at each extreme).
The left ends of the rows give one step outside the range seen before (rows 0 -> 1: min q rises by 10), a hull edge of direction (1,1)
as for 8_19 itself.

## 5. Where a mechanism could come from, seen from this lens

5.1 What is now settled.  The linear algebra of N is under control: for unit arrows N = Z_l + Lambda^r is a theorem (section 2), the
two collapses H(N,d_D) = H(N,d_P) = F have explanations (Lee theory in weight two; the arc has one end at p1), and every structure
that is a functor of the type D structure is exhausted (section 3).  What is missing is information BETWEEN components.

5.2 The only tangle-level place where such information can live algebraically is the non-split part of the U-extension: the true
invariant over B^*[U] (KWZ construct it from Khovanov-Rozansky matrix factorizations) may contain U^2-arrows between different
components; its class lives in the sum of HF(gamma_i, gamma_j) in the bidegree of U^2, i.e. between b-generators at lattice offset 3D
(and (3,6)+(0,|q(a)|) for labels U^2 a).  This is the exact analogue of passing from the immersed curve / UV = 0 complex of a knot to
the full complex over F[U,V].  For the split objects B0, B1, ladders this class is zero by definition.  CONJECTURED (no evidence yet):
for an actual tangle, squares that cancel in J are linked through this class.  It is computable in principle (KWZ Section 4.2), not
with kht++.

5.3 Geometric spectral sequences are the proven source of non-additive constraints (Daemi's MATCH kills B0 and B1).  In annular form:
Roberts' argument (the lift of the axis filters the Floer complex) should refine Daemi's sequence to each annular weight.  In weight
two it would be a sequence N => (rank one) with degrees (r, 2r-2); d_P has bidegree (5,8) = (r, 2r-2) for r = 5 and H(N, d_P) = F,
so the natural guess is that d_P IS the plane Floer differential of the sutured tangle (CONJECTURED).  This gives nothing new on N
itself, but the weight-zero part M_0(n) would then carry the inter-square matching, n by n, with a fixed target; the family in n
(exact triangles with W) is a rigid package that the ladders have not been tested against.

5.4 Cautions that any mechanism must respect.
 (i) Extreme-degree purity is false for closures (10_132, section 4.2).
 (ii) N is not Kh~ (x) Kh~ for doubles of thick knots, and the Theorem S sequence need not collapse (8_19: 41 against 25).
 (iii) The analogue of END for the weight-zero multiplicity space is false by construction (chi(M_0) is a unit, 3.3).
 (iv) A decisive stress test of END/NP for N that is still missing: the double of 10_132 (the smallest knot whose own Kh~ has a
      cancelling extreme degree).  Diagram (width 5, 12 crossings, same reduced Bar-Natan homology as 10_132):
      r1.r3.y0.x2.x2.y1.y2.y0.y0.x2.y1.x2.x3.x1.u0.u0   (kht/examples/dbl2/k132p.kht; command: kht++ -c2 -d FILE).
      It was started here with a three hour limit; the result, if it finished, is in kht/examples/dbl2/k132p/cxBNr-c2-d and can be
      read with scripts/gridbn.py.  (At slice 42 of 65 it had 5946 generators.)

## 6. A theorem for a class, obtained by combining Theorem A with MATCH: flat => at least 7 specials (unit arrows)

### 6.1 The flatness equation for zigzag + squares  [PROVED for l <= 7 by exact division, scripts/flatpi.py; elementary]
With unit arrows N = Z_l + squares and (lattice coordinates, one of the two mirror orientations)
   chi(N) = sum_{i=0..l} t^{3i} - sum_{i=0..l-1} t^{3i+4} + (1-t)(1-t^4) Pi(t),   Pi = sum over squares of (-1)^{a+b} t^{a+4b}.
T is flat iff chi(N) is a unit (project fact: J unit iff J = 1).  For each l there is exactly one solution: unit t^{-l} and
   Pi_0 = 0,  Pi_1 = t^-1,  Pi_2 = t^2 + t^-1 + t^-2,  Pi_3 = t^5 + t^2 + t + t^-1 + t^-2 + t^-3,  ...
with non-negative coefficients summing to l(l+1)/2.  So a flat tangle with zigzag Z_l has r >= l(l+1)/2 squares, r = l(l+1)/2 mod 2, and
   dim N >= 2 l^2 + 4 l + 1  (1, 7, 17, 31, ...),  and for l = 0: r even, dim N in {1, 9, 17, ...}.
Formal flat configurations with dim N <= 15 are therefore exactly:
   dim 7:  B1_{s'}: Z_1 + one square at lattice position (3 - 4s', -1 + s'), s' even (relative to the zigzag {(-1,1),(-1,0),(0,0)});
   dim 9:  B0_s: point + two squares at lattice offset s(-4,1), s odd  ((h,q)-offset (s,0));
   dim 15: Z_1 + three squares (one B1-type square and one cancelling pair),
and their mirrors.

### 6.2 The matching test  [DATA; scripts/b1match.py, smallflat.py, c3match.py; Daemi's degree rule as in board X.17]
Closures of slope +-1/n computed by the pairing theorem (engine lit/kwz-linear/calc/hf.py), then the largest matching by pairs of
bidegree (r, 2r-2), r >= 2; an actual knot of determinant 1 must leave exactly 1.
   B1_{s'}, s' = 0, 2: 3 to 7 generators left (n = 1, 2, both signs);  s' = -2, +-4: nothing can be matched (non-adjacent levels);
   B0_s, s = +-1: 3 to 7 left;  s = +-3: 15 to 33 left.
   (Other s, s' : the two blocks are at least two delta-levels from everything else, nothing can be matched.)
   C3 := arc of 5_2 second inversion + squares Y (its actual square), Y shifted by (h,q) = (-1,0), Y shifted by (3,6):
        dim N = 15, Jones polynomial of every K_n trivial, and the matching leaves exactly 1 on all six closures tested.
        In lattice coordinates: zigzag {(-1,1),(-1,0),(0,0)}, squares at (0,-1), (4,-2), (3,-1).  It is the actual tangle plus one
        "Daemi cube" (two squares at offset P - D = (4,6)) whose lower square is the (1,0)-shift of the actual square.

### 6.3 Statement
PROPOSITION B (PROVED given: KWZ Thm 4.4 [Theorem A], the pairing theorem for Kh~ of closures, Daemi's theorem as used in board
X.17, and the project fact "flat iff chi(N) is a unit").  Let T be the Seifert-framed quotient tangle of a strongly invertible knot,
and suppose BN~(T; F_2) has unit arrows.  If T is flat and not rational then dim N(T) >= 15, i.e. Kh~(T) has at least 7 special
components.  Equivalently: Lemma Q holds for every strong inversion whose quotient tangle has unit arrows and at most 6 specials.
Proof: by Theorem A, N = Z_l + r squares; by 6.1 a flat configuration with dim N <= 13 is a B1_{s'} or a B0_s (or mirror); for these
the arc with its tail and all bigradings are determined up to an overall shift, so Kh~(K_n) is determined, and by 6.2 it violates
Daemi's matching.  QED
The bound cannot be improved by MATCH alone: C3 (dim 15, l = 1) and the ladder (dim 17, l = 0) pass.  This improves the board's
"dim N >= 5" under the unit-arrow hypothesis; it is not a proof of Lemma Q.
REMARK (structure of the formal survivors).  A pair of squares at offset (a'-a, 1) with a'-a >= -3, matched by Daemi, changes Pi by
+- t^e (1 - (-t)^k), k = a'-a+4 in {1,...}; all of these vanish at t = -1, and the forbidden k = 0 is the (1,0)-shift.  So modulo
formal matched pairs only Pi(-1) = sum over squares of (-1)^b is determined (the determinant condition), and formal flat objects that
pass MATCH are "actual tangle + matched pairs whose total contribution to Pi is minus the actual defect".  For 5_2 second inversion
the defect is J - t^4 = -(1-t)(1-t^4) t^-4 (1 + t^3): exactly one cube.

### 2.8 Theorem A against the saved data  [DATA; scripts/shapecheck.py on lit/kht/out/{k138,dbl,comp,tilt,alex1}]
348 arcs: 347 have unit arrows and every one of them is a zigzag (no composable junction); the remaining one is 9_46 second inversion
(one D^2, still no composable junction).  2287 compact components: all have unit arrows and all are the unit square.  No violation.
(The folder rand/ contains invalid random words with components carrying S^2 arrows between b-generators; excluded.)

### 6.4 Addendum to 6.1: proof for all l  [PROVED]
Write c_l(t) = sum_{i=0..l} t^{3i} - sum_{i=0..l-1} t^{3i+4}.  If c_l + (1-t)(1-t^4) Pi = e t^m then at t = 1: c_l(1) = 1, so e = +1;
first derivative at t = 1: c_l'(1) = 3l(l+1)/2 - 3l(l-1)/2 - 4l = -l, so m = -l.  The unit is forced.  Divisibility of t^-l - c_l by
(1-t)^2, 1+t and 1+t^2 holds (c_l(-1) = (-1)^l, c_l(i) = i^-l), so Pi_l exists and is unique, and by the second derivative
Pi_l(1) = (l(l+1) + 3l(l+1))/8 = l(l+1)/2.  Hence r >= |Pi_l(1)| = l(l+1)/2 and r = l(l+1)/2 mod 2 for every flat configuration,
dim N >= 2l + 1 + 2l(l+1), with no use of the explicit form of Pi_l.  (The explicit Pi_l for l <= 7 have non-negative coefficients.)

## 7. Tests on 10_132 as a strongly invertible knot  [DATA, new; kht/find132.py, kht/examples/siq/, scripts/gridbn.py]
Random half-diagram words filtered by the Alexander polynomial of 5_1 = that of 10_132 (values at -1, 2, 3) and then by reduced
Khovanov rank 11 gave seven diagrams of a strongly invertible knot with the reduced Bar-Natan homology of 10_132 or of its mirror
(pawn at (0,-2), top quantum degree carried by h = -1 and h = 0):
    s.l1.y2.y2.x0.y1.y0.y2.x1.x0.u1            (shortest; 48 s for the quotient tangle)
    s.r1.x2.y0.y2.y0.l1.x2.y3.u3.y2.y2.y1.y2.y0.u1,   s.r1.x2.x0.r1.x1.y0.x1.y2.u3.x0.x0.y2.u1
    s.l1.y2.y1.x2.y1.x2.y0.x1.x0.x0.x2.u1  (mirror),  s.l1.y0.y0.x2.x2.y1.y2.x0.x2.x0.x1.x2.x0.u2  (mirror, not run)
Two further short diagrams found later: s.r1.x0.x0.x2.x1.x2.y0.y1.u2 (mirror) and s.r1.x0.x2.x1.x0.y2.y1.y0.y0.u1.
All seven quotient tangles computed are the same up to mirror (so only one strong inversion was found):
    BN~ = arc with three b-generators and tail (k = -4, the arc of the trefoil quotient) + two unit squares at (h,q) = (5,18), (1,12);
    Kh~ = r_1(-4) + 5 specials;   dim N = 11;   rows b = 1, 0, -1:  [. 1 1 .], [1* 2 2 1], [. 1 1 1]   (a from 0 to 3);
    J has 9 non-zero coefficients with absolute sum 11: NO cancellation anywhere; NP and END hold; hull directions (1,0), (0,1), (1,-1).
So for this knot the reduced Khovanov homology of K itself (rank 11) has a cancelling extreme degree, while N of its quotient tangle
(also rank 11) has no cancellation at all: N is not a regrading of Kh~(K), and the failure of extreme purity for knots does not
propagate to N in this example.  This is evidence for END at tangle level; the double of 10_132 remains the harder test.
STATUS of the double of 10_132 (kht/examples/dbl2/k132p): after 34 minutes of CPU it had finished slice 44 of 65 with 10030
generators (slices 41-44: 2.7, 2.4, 6.9, 14.6 minutes); it runs under a three hour limit and will probably be cut off.  An overnight
run, or one of the 11-crossing diagrams r1.r3.x0.y1.x2.x2.x1.y0.y3.x1.y3.y3.y0.u0.u0 / r1.r3.x3.y0.y2.y2.y1.x3.x2.x3.x2.x3.y1.u0.u0,
is needed.

## SUMMARY

STATUS: complete for tasks 1-4; one long computation (double of 10_132) was still running when this was written, see section 7.

What is PROVED (given the cited theorems, each read in source during this session unless said otherwise)
 1. Dictionary (section 1).  AKh(T(n)) = H(BN~(T sigma^n) [x] M, d_0) with M(b) = V (x) V, M(c) = W; weight +-2 is N; f is the action of D;
    v_-2 = d_-; the weight-preserving odd element v_0 = [e, d_-] acts on N as 2 d_D (characteristic 0), bidegree (1,2); the saddle gives
    beta: N -> M_0 and alpha: M_0 -> N; the run P is not in the current algebra (secondary operation; P D^2 = U^4 in B^*[U]);
    sl_2(wedge) preserves delta' = (j-k)/2 - h, so the module splits by rows of N.  Lemma U: over F_2 the unreduced complex is induced
    from the reduced one (so "dots on both strands" add nothing).  Weightwise Lee differential d_0 + dLee_0 + [e,d_-]: N => F with first
    differential d_D.  [GLW1 Lemma 1, Lemma 3, Prop. 5, Section 5.2, Prop. 6, 7, 12; GLW2 Lemma on degrees.]
 2. THEOREM A (section 2): for a component of BN~(T) with unit arrows (D and P_2 only) the extension property of
    Kotelskiy-Watson-Zibrowius (arXiv:2202.01460 Thm 4.4, with mu_4(D,S,D,S^2) = S U^2) forces: unit square with trivial local system,
    or a zigzag arc.  So the SHAPE LAW N = Z_l + Lambda^r holds for every tangle with unit arrows.  Checked against the 2634 unit-arrow components of the saved data (347 arcs, 2287 squares).
 3. PROVED NEGATIVE (sections 3, 4): every ingredient of the annular package (current algebra module for all n, d_- homology = Kh,
    ranks, weightwise Lee theory, annular Rasmussen invariants, triangles in n, also the U-extension) is additive in the type D structure,
    and the pair (d_0, d_-) never relates two delta-rows of N.  Hence it cannot exclude B0, B1, ladders, or any
    a(0) + C (x) (F + hF), and NP does not follow from a weight or purity argument for (d_0, d_-).  Explicit: B0 and the actual tangle 9_42
    have the same module up to regrading a summand (9 | 17 | 44 | 20 | 12).
 4. PROPOSITION B (section 6): with unit arrows, a flat non-rational quotient tangle has dim N >= 15 (at least 7 specials); uses
    Theorem A, the flatness equation (unique unit t^-l, at least l(l+1)/2 squares), and Daemi's matching (board X.17) on the two
    families of formal candidates of dimension 7 and 9.
What is DATA (new)
 - double of 8_19: 8 unit squares + arc with two D^2, dim N = 41 (HFK^ rank of 8_19 # 8_19 is 25: no collapse; N is not Kh~ (x) Kh~);
   NP and END hold.
 - 10_132 = closure of slope -5/2 of the trefoil quotient tangle has reduced Khovanov homology whose top quantum degree is carried by
   two generators at offset (1,0): purity of extremes is false for closures, even for unknotting number one.
 - 10_132 as a strongly invertible knot (one inversion found): dim N = 11 = ||J||_1, no cancellation at all, NP and END hold (section 7).
 - Formal flat objects: B1 (dim 7) fails Daemi's matching; C3 (dim 15: 5_2 second inversion + one "Daemi cube") passes it at slopes
   +-1, +-1/2, +-1/3.  C3 is smaller than the ladder (dim 17).
What is CONJECTURED
 - d_P is the plane Floer differential of the sutured tangle (annular refinement of Daemi's sequence in weight two).
 - Compact components of BN~(T) for T(infty) = U are always squares [beta^a, gamma^n] (no proof beyond unit arrows; first-order
   obstruction theory allows other curves when runs of different lengths or D^2 occur).
The named GAP
 A non-additive input stronger than MATCH.  Formal flat objects that survive everything proved or cited so far are exactly of the form
 "actual tangle + Daemi-matched pairs of squares (cubes) whose contribution to Pi is minus the actual defect"; the smallest are C3
 (dim N = 15) and the ladder (dim N = 17).  Nothing in the annular lens distinguishes them from actual tangles.
The single most promising next step
 Settle END/NP on the double of 10_132 (diagram and command in 5.4 (iv); kht++ -d, several hours): it is the smallest tangle whose
 closures are governed by a knot with a cancelling extreme degree, and the outcome decides whether END is the right target at all.
 If END survives there, the structural next step from this lens is the non-split part of the U-extension over B^*[U] (5.2): it is the
 only tangle-level structure that is not a functor of the multicurve, and Theorem A shows that it has force.
