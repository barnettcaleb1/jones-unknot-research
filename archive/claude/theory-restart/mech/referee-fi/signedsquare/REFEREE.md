# REFEREE report -- lens SIGNED SQUARE

Referee of: finite_index_pattern_rigidity.md, Section 5 (exclusion of the outer coset in TH-PATTERN-FI, Theorem B),
and its input two_box_signed_square.md (CX-BOX-SQUARE).  15 November 2026.

**Verdict: CONFIRMED.**  I could not break the signed-square identity, the identification of the tensor, or the
outer-coset contradiction.  Everything below was re-derived independently; exact computation found no violation
in about 10,000 actual two-box diagrams.  I add two remarks that strengthen the step (Section 3.3, 3.4) and four
cosmetic corrections (Section 5).  Nothing here referees Theorem A, TH-SYM, or the step "finite index implies
non-cyclic implies similitude"; those belong to other lenses.

Notation: z = zeta_8 = exp(pi i/4); corners are indexed 0/1 (index 0 = first basis tangle [Q_0], index 1 = [Q_inf]);
"reduced raw bracket" = Kauffman bracket with <O> = 1, no writhe factor, the same normalisation at all four corners.

---------------------------------------------------------------------------------------------------------------

## 1. The identity: exact statement, hypotheses, independent derivation

### 1.1 What is actually proved in two_box_signed_square.md

Hypotheses (all used):
- ONE link diagram on the sphere, with TWO disjoint marked disks ("boxes"), each meeting the diagram in exactly four
  boundary points and containing nothing else.  A box is "crossing-type" only in the sense that an auxiliary crossing
  can be drawn in it; equivalently it is an arbitrary four-end disk slot.  There are exactly two crossingless fillings
  of such a disk, so the corner basis is canonical up to swapping the two labels of a box.
- The four corners C_ij are the reduced raw brackets of the four diagrams obtained by the crossingless fillings;
  outside crossings and framing are the same in all four.
- Evaluation at A = z, where delta = 0.

Statement proved (in the general form that the proof gives, and which I re-derived):

  (SQ)  For every corner (i,j) with C_ij(z) != 0,
            (-1)^(i+j) det C(z) / C_ij(z)^2  =  m^2 / t^2  >= 0,
        with integers m, t;  t = +-1 (so the value is the integer square m^2) when |C_ij(z)| = 1.
        The statement does not depend on which filling of a box is called 0 and which 1.

The file states the case (i,j) = (1,1), |C_11(z)| = 1, and mentions the general anchor sign (-1)^(i+j) "for
reference".  Both are correct.  So is the label independence: swapping the labels of one box multiplies det C by -1
and moves a diagonal anchor to an off-diagonal position, and the two signs cancel.

It is NOT a statement about abstract 2x2 Laurent matrices, nor about slots that are not disjoint disks of one planar
diagram.  (The ratio in (SQ) is invariant under rescaling C, so a common scalar is harmless.)  Any two disjoint
Conway balls of a link in S^3 can be isotoped to disjoint disks of one diagram, at the price of a change of boundary
marking, which is an outside braiding of the four ends and hence an element of Gamma acting on that slot; so the
identity applies to any two disjoint Conway-tangle slots once such a diagram is fixed.  Theorem B assumes exactly
"one actual planar diagram with two disjoint marked rational-tangle slots", i.e. two disjoint boxes into which
rational tangles are inserted.  The hypotheses match.

### 1.2 Independent derivation

Complete each box by an auxiliary crossing.  If the completed projection is disconnected, every state of every corner
has at least two circles and all four corners vanish at z; (SQ) is then vacuous.  Otherwise checkerboard-colour and
let T be the black Tait graph, v vertices.

Circle count.  A state is a set F of edges of T ("IN" = the smoothing that merges the two black regions at the
crossing).  The state circles are the boundary of a regular neighbourhood of (V,F) in S^2, and an Euler characteristic
count gives  #circles = |F| - |V| + 2k(F).  Since |F| >= |V| - k(F), one circle iff k = 1 and |F| = |V| - 1, i.e. F is
a spanning tree.  The reduced bracket is sum A^(a-b) delta^(c-1), so at delta = 0 exactly the spanning trees survive.

Weights.  At an outside crossing e let the IN smoothing have weight A^(s_e), s_e = +-1; OUT has A^(-s_e).  A tree F
with marked-edge membership bits b = (b_1,b_2) has weight
    prod_e z^(-s_e) * prod_{e in F outside} z^(2 s_e) = z^(-sum s_e) * i^(v-1-b_1-b_2) * prod_{e in F outside} s_e,
because z^(2s) = i s for s = +-1 and F has v-1-b_1-b_2 outside edges.  Hence
    C_b(z) = q i^(-b_1-b_2) tau_b,     q = z^(-sum s_e) i^(v-1),
with tau_b the signed count of spanning trees with marked membership b.

Matrix-tree.  With M the reduced signed Laplacian of the outside edges (weights s_e; loops contribute nothing) and
p, r the reduced incidence vectors of the marked edges, the weighted matrix-tree theorem (a polynomial identity in
the edge weights, valid for any signs) gives T(x,y) = det(M + x pp^T + y rr^T) = tau_00 + tau_10 x + tau_01 y +
tau_11 xy.  For invertible M, det(M + x pp^T + y rr^T) = det M * det(I_2 + diag(x,y) [p r]^T M^-1 [p r]), so
    tau_00 = det M,  tau_10 = det M * alpha,  tau_01 = det M * beta,  tau_11 = det M * (alpha beta - gamma^2),
alpha = p^T M^-1 p, beta = r^T M^-1 r, gamma = p^T M^-1 r, and
    tau_10 tau_01 - tau_00 tau_11 = (det M * gamma)^2 = (p^T adj(M) r)^2 = m^2.
Both sides are polynomials in the entries of M, p, r, so this holds for singular M too.

Phases.  In black-IN coordinates the corner matrix is q [[tau_00, -i tau_01], [-i tau_10, -tau_11]], determinant
q^2 (tau_10 tau_01 - tau_00 tau_11) = q^2 m^2.  If the supplied labels (l_1,l_2) differ from the black-IN bits on k
axes, det C = (-1)^k q^2 m^2, and the supplied corner (l_1,l_2) has b_1 + b_2 = l_1 + l_2 + k (mod 2), so
C_l^2 = q^2 (-1)^(l_1+l_2+k) tau^2.  The ratio is (-1)^(l_1+l_2) m^2 / tau^2.  This is (SQ).  For l = (1,1) and
tau = +-1 it is the banked statement det C / u^2 = m^2.

I agree with the file on every point of the proof: tree-state model, phase q i^(-b_1-b_2), rank-two identity,
singular case, label reversals, common reduced normalisation.

### 1.3 Machine checks of the derivation (all exact)

- matrix_tree_check.py: the rank-two identity as a symbolic polynomial identity for generic symmetric M, sizes 1..4;
  and 400 random signed multigraphs with two marked edges (loops, bridges, parallel edges allowed; 210 of them with
  singular reduced outside Laplacian): brute-force signed tree counts equal the determinant coefficients, and
  tau_10 tau_01 - tau_00 tau_11 is a perfect square, 0 failures.
- tait_check.py: for 1238 random connected two-box diagrams (closed braids on 2..4 strands and plats on 2..6 strands,
  up to 9 outside crossings; label reversals k = 0, 1, 2 occurring 229, 499, 510 times) I built the black Tait graph
  from the diagram, computed tau_b and m from the Laplacian, and compared the PREDICTED values
  z^(-sum s_e) i^(v-1) i^(-b_1-b_2) tau_b with the actual brackets from a state sum that knows nothing about Tait
  graphs.  All four corners agree exactly in all 1238 diagrams, and tau_10 tau_01 - tau_00 tau_11 = m^2 in all.
  The 262 disconnected diagrams all have C(z) = 0.

---------------------------------------------------------------------------------------------------------------

## 2. The tensor of Theorem B is the corner matrix of the identity

For a two-slot pattern, B_C(v,w) = v^T C w with v, w the bracket vectors of the inputs in the basis ([Q_0],[Q_inf]).
Taking v, w basis vectors, C_ij is the reduced raw bracket of the diagram with the crossingless tangle Q_i in slot 1
and Q_j in slot 2: these are the four corners of (SQ).  Linearity in each slot is the skein expansion of the input
inside its box, with <O> = 1 at the end, so one common normalisation is used; that is "common reduced raw tensor".

Convention check on actual diagrams (explicit_patterns.py; brackets from cx-tools/bracket.py, cross-checked by two
independent state sums):
- two-strand pattern N(T1+T2): C = G = [[delta,1],[1,delta]] exactly;
- stacking a twists on box 1 and b twists on box 2 changes C to (M^a)^T C M^b with M = [[A,0],[A^-1,-A^-3]] exactly
  (checked for N(T1+T2) with a = 2, b = -3 and for the seed moves below).  Index 0 is the filling on which a twist acts
  as "the crossing itself", index 1 the filling that becomes a kink (eigenvalue -A^-3).  J is the label swap.
So the tensor, the group Gamma and the form G of the theorem are literally the ones realised by diagrams, in the
basis in which (SQ) is stated.

---------------------------------------------------------------------------------------------------------------

## 3. The contradiction with the outer coset

### 3.1 Normal form and ratio (algebra_check.py, sympy, exact)

All of (E) re-verified: E^2 = (delta^2-1) I, E*GE = (delta^2-1) G, EJE^-1 = -J, EME^-1 = -A^-2 J M^-1 J; also
M*GM = G, J*GJ = G, bar(M) = M^-1, bar(E) = E, GE = (delta^2-1) diag(1,-1).
At z with D = diag(1,i):  D^-1 M D = z [[1,0],[-1,1]],  D^-1 J D = i [[0,1],[-1,0]],  D^-1 E D = i [[0,1],[1,0]],
G(z) = [[0,1],[1,0]].  So bare Gamma words become scalar * SL_2(Z) and E * (Gamma word) becomes scalar * (integral,
det -1).  The sign of the determinant of the real matrix is well defined projectively (a complex scalar relating two
nonzero real matrices is real).

If S(z) = v D L D^-1 with L = [[a,b],[c,d]] real, then C(z) = G(z) S(z) = v [[i c, d],[a, -i b]] (as in the text) and
    det C = -v^2 det L,
    det C / C_ij^2 = det L / x^2 at the two diagonal corners (x = c at 00, x = b at 11),
    det C / C_ij^2 = -det L / x^2 at the two off-diagonal corners (x = d at 01, x = a at 10).
Inner coset (det L = +1): sign (-1)^(i+j), in agreement with (SQ).  Outer coset (det L = -1): sign -(-1)^(i+j) at
EVERY nonzero corner; at corner 11 the value is -1/b^2, as claimed.  The ratio is independent of v, so no assumption
on the scalar beyond 0 < |v| < infinity is used.  Confirmed also on 60 random words W in M, M^-1, J (length <= 9):
354 nonzero anchors of G W and G E W, all with the predicted sign and |ratio| a rational square.

v finite and nonzero: C = f X with X = G E W, entries of X in R and X(z) nonsingular.  C in Mat_2(R) forces
ord_{Phi_8}(f) >= 0, and one nonzero entry of C(z) forces ord_{Phi_8}(f) = 0.  The unit seed gives this (3.2).

### 3.2 Unit seed, denominator, coset preservation

- A unit u = +-A^k has |u(z)| = 1, so after the move the denominator C'_11(z)^2 is nonzero and the banked form of the
  identity (integer square) applies verbatim.
- The move: a rational tangle is isotopic rel boundary to a twist-form diagram, whose bracket vector is W e_j with W
  a bare word in M^+-1, J (vertical twist = M^+-1 by the diagram check above; horizontal twist = J M^-+1 J by rotating
  the picture a quarter turn; J = relabelling).  Replacing the seed diagrams by twist forms changes the seed bracket
  by a unit only.  Pushing the twist crossings out of the boxes gives a new ACTUAL two-box diagram with tensor
  C' = P^T C Q, P, Q in Gamma, and C'_11 = the seed bracket.  (SQ) applies to this new diagram.
- G^-1 P^T G = bar(P)^-1 for P in Gamma (checked on random words), so S' = bar(P)^-1 S Q.  bar(Gamma) = Gamma and
  E^-1 Gamma E = Gamma with unit scalars, so Gamma E Gamma = E Gamma: the coset is preserved.
- Diagram test of the move (explicit_patterns.py): for patterns P4 and P5 below and every unit seed among integer-
  twist fillings |a|,|b| <= 3 (2 and 7 seeds), the tensor computed from the twisted diagram equals
  (M^a J)^T C (M^b J) exactly, and det C'/C'_11^2 at z is 9 resp. 36: nonnegative integer squares.

So the step is correct: outer coset would give -1/b^2 < 0 at a corner where the identity gives m^2 >= 0.

### 3.3 Remark: the seed move is not needed for the contradiction

By 3.1 the outer coset has the wrong sign at every nonzero corner, diagonal or not, and (SQ) holds at every nonzero
corner.  So the contradiction needs only C(z) != 0, i.e. ord_{Phi_8}(f) = 0.  The unit seed gives that directly
(u = v^T C w is nonzero at z, so C(z) != 0) without moving anything.  The move in the text is correct but can be
deleted; this removes the only place where twist-form diagrams of the seed are used.

### 3.4 Remark: an independent exclusion at A = 1 (no seed, no zeta_8)

At A = 1: delta = -2, M(1) = [[1,0],[1,-1]], J; they generate a group of order 12 (projectively S_3), and EVERY
element has a zero entry (algebra_check.py (d), by enumeration).  Since GE = (delta^2-1) diag(1,-1), an outer-coset
tensor is C = g diag(1,-1) W with g in K, W a bare word.  Pick an entry with W(1)_ij != 0: g = +-C_ij / W_ij is
regular at A = 1.  Then at an entry with W(1)_kl = 0 we get C_kl(1) = 0.  But a corner is the reduced bracket of a
link diagram, and <D>(1) = +-(-2)^(c-1) != 0 (c = number of components).  Contradiction.

Hence no tensor whose four corners are brackets of actual link diagrams lies projectively in the outer coset.  This
confirms the conclusion of Section 5 by a route that shares nothing with the signed-square identity and needs neither
the unit seed nor planarity of the boxes.  (It also gives a one-line proof that [E] is not in Gamma: E(1) =
[[-2,1],[-1,2]] has no zero entry.)  The inner coset passes the same test: G(1)W(1) has no zero entry for all 12 W.
In the random scans no corner ever vanished at A = 1.

The unit seed is still needed for the last step of Theorem B (f is a unit).  Example (hopf_sum_example.py):
N(T1+T2) # Hopf has C = (-A^4 - A^-4) G exactly, S scalar, full Gamma symmetry, C(z) = -2 G(z) != 0, no unit seed,
and f = -A^4 - A^-4 is not a unit.  This is consistent with Theorem B as stated.

---------------------------------------------------------------------------------------------------------------

## 4. Attempts to refute on explicit patterns

Tools.  twobox.py describes a two-box pattern as a closed braid-like word (or plat) with two box letters; fillings
0 = two through strands, 1 = cup-cap.  Three evaluations of each corner: (i) cx-tools/bracket.py on a PD code made
with twist.Builder after smoothing the boxes by reconnection; (ii) my own state sum on the port graph; (iii) a direct
Temperley-Lieb state sum on the word that uses no PD code.  Evaluation at z is exact in Z[zeta_8] (integer
4-vectors), ratios in Q(zeta_8) by Galois norm.  bracket.py conventions as in VALIDATION.md; calibration: closure of
s1^3 gives A^-7 - A^-3 - A^5 by (i) and (iii).

Explicit patterns (explicit_patterns.log); (i) = (ii) = (iii) in every case:

| pattern | tensor at z (z = zeta_8) | ratios det/C_ij^2 at nonzero anchors | law (SQ) |
|---|---|---|---|
| P1 N(T1+T2), C = G | [[0,1],[1,0]] | (01): -1, (10): -1 | pass |
| P1' N(T1+T2) with twists, C = (M^2)^T G M^-3 | [[z,-z^3],[-z^3,0]] | (00): 1, (01): -1, (10): -1 | pass |
| P2 EKT Hopf shell = 2-cable of Hopf, one box per ribbon; C = [[h,delta^2],[delta^2,delta]] exactly as in the dichotomy file | 0 | none (C(z) = 0, m = 0) | vacuous |
| P3 closed 3-braid B1 s2^2 B2 s2^-2 | [[0,0],[0,4]] | (11): 0 | pass |
| P4 closed 3-braid B1@1 s2 s1^-1 B2@2 s1 s2^2 | [[0,3z],[3z,-2z^3]] | (01): -1, (10): -1, (11): 9/4 | pass |
| P5 4-plat s2^2 (B1@1 B2@3) s2^-3 | [[z,-6z^3],[-6z^3,0]] | (00): 36, (01): -1, (10): -1 | pass |
| P6 4-braid B1@1 s2^2 B2@3 s2^-2 s1 s3^-1 | [[0,4],[0,4i]] | (01): 0, (11): 0 | pass |

The EKT tensor has C(z) = 0 identically (h is divisible by delta), so EKT has no unit rational seed and neither
Theorem B nor the identity says anything about it; consistent with the dichotomy file, where EKT is in the cyclic
(non-similitude) case.  P5 has a unit corner with m^2 = 36, so it is an actual pattern with unknot seeds whose tensor
is not +-A^m G W (those have m^2 = 1 at a unit diagonal anchor); it is not a similitude, so no conflict with
Theorem B.

Random scans (random_scan.py, seeds 1115 and 777; closed braids on 2..5 strands, plats on 2..6 strands, up to 9
outside crossings, boxes at random positions):
- 9000 patterns, 900 of them cross-checked against bracket.py: 0 tool mismatches;
- 6574 with C(z) != 0; 15,611 nonzero anchors tested, of which 9969 unit anchors; (SQ) FAILURES: 0;
- 7072 diagonal anchors: 0 with negative ratio (the outer-coset signature never occurs);
- unit diagonal anchors: m^2 in {0, 1, 4, 9, 16, 25, 36, 49}, always an integer square;
- no corner vanishes at A = 1.

Similitude scan (similitude_scan.py, 4000 patterns): 1489 have S = G^-1 C a G-similitude; 994 with multiplier 1, the
rest with multipliers such as delta^2 (split circle), (delta^2-2)^2 (Hopf summand), i.e. consistent with f G W, f a
non-unit.  None shows an outer signature (no negative diagonal ratio, no zero at A = 1).  This is a search, not a
proof that every actual similitude pattern is f G W.

---------------------------------------------------------------------------------------------------------------

## 5. Corrections (all cosmetic; none affects the theorem)

1. Index convention.  In Section 5 of finite_index_pattern_rigidity.md "corner11" is the lower-right entry
   -i b v of C(z) (0/1 labels: both slots filled by the second basis tangle), not the (1,1) entry of the matrix in
   1-based indexing.  Harmless: the upper-left entry gives -1/c^2, also negative, and (SQ) is positive at both
   diagonal corners.  Worth one sentence in the text.
2. two_box_signed_square.md, "It is connected: a disconnected completed projection would make ...".  This should read
   "we may assume it is connected; otherwise all four corners vanish at z and the hypothesis |C_11(z)| = 1 fails".
3. Section 5 writes the Laplacian as M_0 and an incidence vector as r while M is the twist generator; the source file
   uses q for both the phase and (as q_0) an incidence vector.  Rename.
4. The sentence "Move the actual rational unknot seed to corner11 by rational boundary operations" should say that
   the seed tangles are first put in twist form (unit change of the seed bracket) so that the moved pattern is again
   an actual two-box diagram; or, better, drop the move altogether (3.3).

Optional strengthening for the write-up: add the A = 1 argument (3.4) as a second, independent proof of the
outer-coset exclusion.  It shows that the unit seed is not needed to exclude the outer coset, only to make f a unit.

## 6. Not refereed here / what would settle open points

- Theorem A, TH-SYM and the non-cyclic step: other lenses.  The sign step uses only the OUTPUT "[S] in Gamma or
  E Gamma projectively".
- The consequence in two_box_signed_square.md for the opposite-Omega tensor (a^2 - m^2 = 8) is not used by Theorem B
  and was not re-checked, apart from the identity h = delta^3(delta^2-3)^2 - delta(delta^2-2)(delta^2-4) (true).
- External sources: this step uses no published theorem beyond the weighted matrix-tree theorem and <D>(A=1) =
  +-(-2)^(c-1); both were verified here by brute force (matrix_tree_check.py; A = 1 column of the scans), so no
  literature lookup was needed.  The Chung--Lin reference in two_box_signed_square.md is explicitly not relied on.

## 7. Files (all in this folder)

- algebra_check.py / .log        sympy: (E), D-gauge, coset normal forms and ratios, seed-move identity, A = 1, EKT h
- matrix_tree_check.py / .log    rank-two determinant identity, signed spanning trees by brute force
- twobox.py                      two-box pattern tool (three bracket evaluations, exact Q(zeta_8) arithmetic)
- explicit_patterns.py / .log    P1..P6 incl. EKT Hopf shell, convention tests, seed moves on diagrams
- random_scan.py, random_scan.log (seed 1115, 3000), random_scan_seed777.log (6000)
- tait_check.py / .log           phase formula C_b(z) = q i^(-b1-b2) tau_b checked corner by corner on 1238 diagrams
- similitude_scan.py / .log      which actual patterns are similitudes; outer signatures: none
- hopf_sum_example.py / .log     C = <Hopf> G: unit seed needed for "f unit", not for the sign step
Nothing outside this folder was modified; cx-tools was imported read-only with bytecode writing disabled.
