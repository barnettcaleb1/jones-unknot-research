# REPORT (lens STATES: the cube, extreme degrees)

STATUS (final, 2026-11-16): sections 0-7 written as found; the report ends with SUMMARY. Outcome: theorems for classes
(adequate ends, positive/negative half-diagrams), a proved limitation of the extreme-state method, and two data laws
(channel directions = twist eigen-bidegrees; nesting under twisting). Lemma Q is NOT proved.
Marks used below: PROVED / CITED (source, statement number, read-now or recalled) / DATA / CONJECTURED.

## 0. Set-up and conventions actually used (all checked against the kht++ source and output)

- [PROVED, read now in lit/kht/src/khtpp/sources/modules/Tangles.cpp lines 690-712] Smoothing convention of kht++:
  x<i>: 0-smoothing = e (turnback, cup over cap), 1-smoothing = id (two vertical arcs); y<i>: 0 = id, 1 = e.
- [PROVED, read now, Tangles.cpp 967-1040 (Tangle::quotient) and 32-120 (symmetric parser)] The half-diagram has a virtual
  strand 0 (the axis); the quotient diagram D(T) has: strand 0 = the axis image A (top end = special end); every other
  strand of the half-diagram is a BAND (two parallel strands, positions 2i-1, 2i); the word starts with a doubled cap
  r1.r2, so there is an extra band on the far right which ends at b2, b3; the final u0 joins A to the left edge of the band.
  Hence the two strands of T are  alpha = top - A - u0 - left band edge - outer cap - b3  and  beta = b1 - right band edge -
  inner cap - b2: connectivity type b. Crossings: 4 per off-axis crossing (2-cable of the crossing: sigma_2i sigma_2i-1
  sigma_2i+1 sigma_2i), 4 per axis crossing ("hook" sigma_0 sigma_1 sigma_1 sigma_0: A runs once around the band),
  2|w| framing twists on (b2,b3), w = writhe of the half-diagram (kht++ Tangle::writhe; x-twists if w > 0, y-twists if w < 0).
- THE b-CUBE. C_b(D) = span of (s, labels): s a state of type b (top-b3, b1-b2), labels v_+/v_- on the closed circles,
  no label on the two strands. Differential = Khovanov differential between type-b states with: circle+strand merge
  v_+ -> 1, v_- -> 0; strand -> strand + circle: the circle gets v_-; strand-strand saddles (they lead to type c) dropped.
  h = |s| + const, q = |s| + #v_+ - #v_- + const.
- [PROVED] Lemma 0.1 (twists are frozen). In every type-b state all framing-twist crossings carry the smoothing id.
  Proof: the twists are the last letters of the word and act on (b2,b3); a turnback there joins b2 to b3 below it. QED.
  So the framing twists only shift gradings: from now on D = D(T) without the twists (4c crossings, c = number of
  crossings of the half-diagram).
- [DATA, script py/fullcube.py] Brute force over the 2^12 states of the trefoil quotient (2824 of type b, 17165 generators):
  H(C_b) has rank 3 at (|s|, q_cube) = (4,4), (8,10), (9,12). kht++: bullet generators of BN~ at (h,q) = (0,10), (4,16), (5,18).
  Same up to the shift (h,q) -> (h-4, q+6), so C_b is the right complex. The complex lives in q_cube from 0 to 16:
  the top of N is 4 below the top of the complex and the bottom of N is 4 above its bottom.
- [DATA, py/bcube.py b_bracket] chi_q(C_b) computed by a transfer matrix over planar matchings agrees with chi_q of the
  bullet generators of the kht++ output up to a unit for every half-diagram tested (this fixes all grading shifts).

## 1. The extreme part of the type-b cube of a band diagram (task 1)

Notation: D = twist-free band diagram, n = 4c crossings, grouped in blocks of four: BAND CROSSINGS (2-cable of an off-axis
crossing) and HOOKS (axis crossings). s_1 = all-one state, s_0 = all-zero state. For a state s: k(s) = number of closed
circles. Top quantum degree of the complex: M = max over type-b states of |s| + k(s); E = set of maximisers ("extreme
states"); the top-degree part of C_b is the complex with basis E (all labels v_+) and d(s) = sum of the s' in E covering s.

- [PROVED] Lemma 1.1 (monotonicity). Along a 1 -> 0 flip the quantity |s| + k(s) changes by -2 (merge of two components,
  one of them a circle), 0 (a chord with both feet on one component: a circle is split off), or -1 (the chord joins the two
  strands: type changes b <-> c). Hence |s| + k(s) <= n + k(s_1) for all type-b s, E is convex in the cube, and every state
  of E is obtained from a maximal element by flips that split off a circle.
- [PROVED] Lemma 1.2 (s_1 and s_0 are of type b). In s_1 every band crossing is a band smoothing and every hook is either
  id (A does not meet the band) or e_0 e_1 e_1 e_0 = (A joined to the adjacent band edge above and below, the other band
  edge passes, one small circle). No arc of s_1 crosses a band, so the inside of the extra band is connected, along the
  band, to the region to the left of A (it opens into it either under u0 or through the channel of a cut hook). In a
  type-c state the inside of the extra band (between b2 and b3) is closed off. QED. So M = n + k(s_1), s_1 is the unique
  maximal element of E, and likewise s_0 at the bottom. [DATA: confirmed in all 128 analysed cases.]
- HALF-PLANE PICTURE [PROVED]. Let Pi be the closed half-plane of the half-diagram, bounded by the axis A. Smooth the
  half-diagram by the 1-smoothing of every crossing, where an axis crossing of type y (1 = e) is CUT (the strand ends on A
  from above and from below) and an axis crossing of type x (1 = id) PASSES BY (the strand stays in Pi). This gives a
  system Gamma_1 of disjoint arcs with ends on A, loops, and one arc gamma_0 running from the top end (the "b-end") to A.
  The components of s_1 other than the small hook circles are exactly the boundary curves of the regions of
  Pi minus (ribbon neighbourhoods of Gamma_1), the axis counted as part of the boundary. alpha is the curve through the
  top of A, beta the curve through b1.
- CHORDS. Each crossing of D is a chord between two components of s_1. In a band crossing two of the four chords join the
  two edges of one ribbon and two (twins, parallel) join the facing edges of the two ribbons across the smoothed crossing.
  In a pass-by hook two chords join the two edges of the ribbon and two (twins) join A to the adjacent ribbon edge. In a
  cut hook all four chords join distinct curves (U, Z, W and the small circle; U and Z, Z and W border different regions).
  The two edges of a ribbon always border different regions, so those chords are never loops.
  A block is BAD (at the 1-end) if its twin chords have both feet on one component of s_1, i.e.
    (i) off-axis crossing: the two arcs of the smoothed crossing lie on the same boundary component of the region of
        Pi - Gamma_1 that contains the crossing;
    (ii) pass-by axis crossing: the strand and the axis lie on the same boundary component of the region between them.
  A chord with one foot on alpha and the other on beta is NOT bad (its flip leaves type b; it is simply absent from C_b).
- [PROVED] Proposition 1.3 (the Lando graph of a band diagram has no edges). All bad chords attached to one component of
  s_1 lie in one planar region (the complementary region of the ribbons which that curve bounds; the other side of the
  curve is the inside of a ribbon and carries no bad chord). Disjoint chords in a planar region attached to one boundary
  curve are pairwise non-interleaved. Hence flipping any set of bad chords splits off that many circles:
      E = { s_1 with an arbitrary subset of the bad chords flipped },  |E| = 4^(number of bad blocks),
  and the top-degree part of C_b is the cochain complex of a full simplex (a Boolean cube).
- [PROVED] Corollary 1.4. H^{*, top}(C_b) = F if D has no bad block at the 1-end ("b-adequate"), and 0 otherwise. The
  independence complex in the sense of Gonzalez-Meneses-Manchon-Silvero is either empty or a simplex; its reduced Euler
  characteristic is 1 or 0. The same holds at the bottom with s_0 and the 0-smoothing (x and y exchanged).
  [CITED, recalled not re-read: Gonzalez-Meneses, Manchon, Silvero, "A geometric description of the extreme Khovanov
  cohomology", Proc. Roy. Soc. Edinburgh A 148 (2018), Thm 1: extreme Khovanov cohomology = reduced cohomology of the
  independence complex of the Lando graph; Przytycki-Silvero, "Homotopy type of circle graph complexes motivated by extreme
  Khovanov homology", J. Algebraic Combin. 48 (2018).]
  [DATA, py/survey.py over the 138 half-diagrams, 128 with a chain file and a feasible enumeration (6 have no chain file, for 4 the
  enumeration of 4^(bad blocks) extreme states was cut off): |E| is a power of 4 in
  every case, the extreme complex is acyclic whenever |E| > 1, s_1 (s_0) is the unique maximal (minimal) element.]
  For comparison [DATA]: for the kht++-simplified diagrams (not band diagrams) this fails: 6_2-1, bottom, has 125 extreme
  states and a non-trivial extreme complex of rank one.

## 2. An adequacy condition on the half-diagram, and what it proves (task 2)

DEFINITION (b-adequate at the 1-end; at the 0-end exchange x and y, 1 and 0). A half-diagram H is b-adequate at the 1-end
if in the half-plane picture of section 1 (all crossings 1-smoothed; y-axis crossings cut, x-axis crossings pass by)
  (i)  for every off-axis crossing, the two arcs of the smoothed crossing lie on DIFFERENT boundary curves of the region
       of Pi - Gamma_1 containing the crossing (boundary curves run along arcs of Gamma_1 AND along segments of the axis);
  (ii) for every pass-by axis crossing, the strand and the axis lie on different boundary curves of the region between them.
Without axis crossings this is ordinary adequacy of the long-knot diagram; the new feature is that the axis joins state
arcs. Example: the standard half-diagram l1.y0.y0.y1.u2 of the trefoil is adequate upstairs (Seifert state of a negative
diagram) but NOT b-adequate at the 1-end: the two arcs at y1 are joined along the axis.

- [PROVED] Theorem 2.1. If H is b-adequate at the 1-end, the top quantum degree of C_b(D) is spanned by the single
  generator (s_1, all v_+). Hence N(T) is one-dimensional in its top quantum degree, in the maximal homological degree
  h = n = 4c: NP and END hold at the top. Same at the bottom for the 0-end, with (s_0, all v_-), h = 0.
  Proof: Lemma 1.1 and Proposition 1.3 with no bad chord: every other type-b state has |s| + k <= M - 2. The generator is
  a cycle (no state above it) and not a boundary (nothing else in its quantum degree). QED
- [PROVED] Corollary 2.2. If H is b-adequate at both ends, then J has extreme coefficients +-1 in degrees M and m with
  M - m = 4c + k(s_1) + k(s_0) > 0, so T is not flat; moreover the homological width of N(T) is exactly 4c.
  (Doubles T_K of adequate diagrams of K are of this kind: for a half-diagram without axis crossings b-adequacy is adequacy
  of the diagram of K. This is the classical statement that the 3-dimensional coloured Jones polynomial of an adequate
  knot has extreme coefficients +-1.)
- THE UNIT POSITION [PROVED; signs calibrated on 3_1, s.y0, 4_1-1, 4_1-2]. Use cube coordinates (h,q) = (|s|, |s| + #v_+ - #v_-)
  of the twist-free diagram D. Let c = number of crossings of H, wr = its writhe (kht++ Tangle::writhe). Then
      T is flat  <=>  chi_q(C_b(D)) = +- q^(d_0),   U := (h_0, d_0) = (2c - 2 wr, 2c - 4 wr).
  Derivation: J = (eigenvalue of T on V_2)/(eigenvalue on V_0). The V_0-eigenvalue of the twist-free tangle is the bracket
  of the unknot diagram D(infinity); in D(infinity) the two edges of a band are antiparallel, so every block has two
  positive and two negative crossings, n_+ = n_- = 2c, and reduced Khovanov homology of that unknot diagram sits at cube
  position (n_-, 2n_- - n_+) = (2c, 2c). Each framing twist pair multiplies J by the ratio of the half-twist eigenvalues
  squared, i.e. moves the unit by (2,4) (y-twists, wr < 0) or (-2,-4) (x-twists).
  Checks [DATA]: trefoil U = (12,18) = kht++'s unknot-normalised origin (the brief's h^8 q^24 discrepancy); 4_1-1: U = (8,10)
  and 4_1-2: U = (4,2) are generators of N (the end rho of the arc); s.y0: N = F at (4,6) = U.
- [PROVED] Theorem 2.3 (one adequate end suffices). If H is b-adequate at the 1-end and 4c + k(s_1) != 2c - 4wr, or
  b-adequate at the 0-end and -k(s_0) != 2c - 4wr, then T is not flat (J has coefficient +-1 in a degree different from
  that of the unit).
- [PROVED] Theorem 2.4 (positivity). Suppose all crossings of H have the same sign, wr = -c (resp. +c). Let c_o be the
  number of off-axis crossings and l the number of closed loops of the Seifert smoothing of H in the half-plane. Then
  k(s_1) = 2 c_axis + 2 l and the whole complex C_b(D) lies in quantum degrees
        <= d_0 - 2 (c_o - l)      (resp. >= d_0 + 2 (c_o - l)),
  and c_o - l is the genus of the Seifert surface of the symmetric diagram (= g(K): [CITED, recalled] Cromwell, Homogeneous
  links, J. London Math. Soc. 39 (1989), Cor. 4.1: Seifert's algorithm on a homogeneous diagram gives minimal genus).
  So T is flat only if K is the unknot: Lemma Q holds for strongly invertible knots with a positive or negative
  half-diagram, by a count. If moreover H is b-adequate at that end, N is exactly F in bidegree (h,q) = U -+ (0, 2g(K)):
  the tangle analogue of "Kh^{0,*} of a positive knot starts at 2g - 1".
  Proof of the count: every axis crossing is cut (one small circle each); Gamma_1 has c_axis + 1 arcs and l loops, hence
  c_axis + l + 2 regions and c_axis + 2l + 2 boundary curves, two of which are the strands; M = 4c + 2c_axis + 2l and
  d_0 = 6c, so d_0 - M = 2(c - c_axis - l) = 2(c_o - l). QED
- [DATA, py/census.py, py/criteria.py, py/negcheck.py; all 138 half-diagrams in lit/kht/out/k138/examples/si]
    b-adequate at both ends: 7   (8_5-2, 8_15-2, 8_18-1, 8_18-2, 9_34, 9_35-1, 9_37-1)
    at the 1-end only: 23;  at the 0-end only: 13;  at neither end: 95.
    In all 128 cases with kht++ output: adequate end <=> the top (bottom) of N is at the cube corner, one-dimensional;
    |E| = 4^(bad blocks) always.
    Theorem 2.3 applies to all 43 half-diagrams with at least one adequate end (the unit is never at an adequate corner).
    Theorem 2.4 applies to 39 half-diagrams (all those with |wr| = c); d_0 - M = 2 g(K) in each (genera from the table, recalled).
    Together: 72 of the 138 are non-flat by a diagram count (no homology computed). 66 remain, e.g. 6_2, 6_3, 7_6, 7_7.
- [DATA] Much more is true than the theorem gives: the top quantum degree of N is ONE-DIMENSIONAL in 127 of 128 cases
  (exception 9_37-2: dimension 2, both in the same homological degree), and likewise the bottom (exception 9_40-2).
  So "N^top = F" is the rule, but it is invisible in the extreme part of the cube, which is acyclic in 98 (top) and 108
  (bottom) of the 128 cases.

## 3. Why N has slopes in [5/4, 2] although the cube is flat (task 3)

3.1 What the cube itself offers.
- [PROVED] The only filtration by "number of circles" that the differential respects is by the number of v_- labels
  (equivalently by |s| + k(s) at fixed q: merges preserve it, splits raise it by 2). Its level-zero part in the top quantum
  degree is the extreme complex of section 1, a full simplex: acyclic unless the diagram is b-adequate. So this filtration
  does NOT make the top of N visible; it only says "not here". delta = q/2 - h is a grading which the differential lowers
  by exactly one, so it carries no filtration information either.
- [PROVED, with the kht++ data for N] A limitation that no choice of half-diagram can remove: at a b-adequate 1-end the top
  generator of N sits in absolute homological degree 2(c + wr) (even, >= 0; absolute = normalised by the unknot closure,
  i.e. relative to the unit U of section 2), at a b-adequate 0-end the bottom generator sits in degree -2(c - wr) (even,
  <= 0). In the table the top generator of N has odd or negative absolute homological degree for 54 of 128 tangles and
  the bottom generator odd or positive degree for 50; for 16 tangles (8_19, 7_3-2, 9_46-1, 9_37-2, ...) both happen.
  For those no band diagram whatsoever is adequate at that end: the extreme-state method cannot reach the top of N.
- [DATA, py/onebad.py] The distance ("defect") from the cube corner to the true extreme generator of N is not a sum of
  local contributions of the bad blocks. One bad band crossing on a strand: defect (3,4) in 32 of 34 ends, but (4,6) for
  8_16 and (5,6) for 9_42; one bad band crossing on a circle: (8,10) in 5 of 6; a run of 2, 4 or 6 bad hooks plus one bad
  crossing: (4,4) regardless of the number of hooks; a lone bad hook next to the vertex (half-diagram s.y0): (4,6).

3.2 The local minimal complexes (hand computation by delooping and Gaussian elimination; Euler characteristics checked).
Write objects as Temperley-Lieb diagrams, (h,q) = bidegree in the y-convention (0-smoothing = id).
- [PROVED] HOOK sigma_0 sigma_1 sigma_1 sigma_0 on (A; band): 16 states reduce to 9 objects
      1 (0,0);  e0, e1 (1,1);  e0e1, e1e0 (2,2), e1 (2,3);  e0e1, e1e0 (3,4);  e0 (4,5).
  Objects without a turnback of the band: 1 at (0,0) and e0 at (1,1) and at (4,5).
- [PROVED] BAND CROSSING sigma_2 sigma_1 sigma_3 sigma_2: 16 states reduce to 13 objects
      1 (0,0);  e1, e3, e2 (1,1);  e2e1, e2e3, e1e2, e3e2, e1e3 (2,2);  e2e1e3, e1e3e2, e2 (3,3);  E = e2e1e3e2 (4,4).
  Objects without a band turnback: 1 (vertical band smoothing), the fused object e2 at (1,1) and at (3,3), and E
  (horizontal band smoothing). Turnback objects cannot be dropped: in the half-diagram s.y0 (trivial tangle) the type-b
  objects are 1 (0,0), e0 with a circle (1,2),(1,0), e0e1 (2,2), e0e1 (3,4), e0 with a circle (4,6),(4,4); the homology F at
  (4,6) arises after cancelling 1 against e0(v_-), e0(v_+) against e0e1(2,2), and e0e1(3,4) against e0(4,5)(v_-).
  (The final answer F at (4,6) is confirmed by brute force, py/small.py.)
- [DATA + count] N is not the homology of a plain cube of "webs" with one homological step per channel step (two per band
  crossing, two per hook): such a cube has homological width <= 2c, but N(4_1 quotient, c = 3) has width 9. So the pieces
  of any channel filtration have internal homological structure (as e2 at (1,1) and (3,3) above).

3.3 Twist eigenvalues give exactly the lattice of the brief.
- [PROVED, direct computation in the Temperley-Lieb algebra with the y-convention sigma = 1 - q e, e^2 = (q + 1/q) e]
  On the band (two strands with the projector p_2, i.e. modulo band turnbacks):
     band crossing R = 1 - (q + q^3) e2 + q^4 E:   eigenvalue 1 on V_4,  -q^4 on V_2,  +q^6 on V_0;
     hook        H = 1 + (q^5 - q) e0:            eigenvalue 1 on V_3,  +q^6 on V_1;
     single crossing: 1 on V_2, -q^2 on V_0.
  With the sign read as (-1)^h these are the bidegrees
     (1,2) = D,   (3,4) = P - 2D,   (4,6) = P - D        (D = (1,2), P = (5,8)),
  and they are realised in the minimal complexes: (4,6) = E(4,4) with its two circles = e0(4,5) with its circle,
  (3,4) = e2(3,3) with its circle. In general the channel V_(a+b-2j) of V_a (x) V_b has bidegree
  (j(a+b-j), j(a+b-j+1)) per half twist: quantum shift minus homological shift = j = number of turnbacks.
  CONSEQUENCE: the lattice Z D + Z P in which N lives (brief, section 4) is the lattice of twist eigen-bidegrees, and
  J = sum (-t)^a (-t^4)^b is the corresponding expansion in eigenvalues (-t = -q^2 for D, -t^4 = (-q^2)(q^6) for P).
  The directions of the polygon law are differences of channels of ONE block:
     D = V_0 - V_2 (band crossing),  P - D = V_0 - V_4 (band crossing) = V_1 - V_3 (hook),  P - 2D = V_2 - V_4.
  The excluded direction (h,q) = (1,0) is P - 4D = (P - 2D) - 2D: not a channel difference of a single block; it needs
  three simultaneous channel changes pulling the quantum degree in opposite directions (+4, -2, -2).
- [DATA, kht++ runs in states/kht, script py/famrel.py; gradings relative to the unit U] Twisting translates part of N by
  an eigen-bidegree and fixes the rest; each step adds four generators (a Z-block, see section 7):
     A  l1.y0.y0.y1^b.u2 (b=1..5):  fixed hull vertices (0,-2), (-3,-6), (-8,-14); moving (-8,-14)-(b-1)D, (-4,-8)-(b-1)D,
        (-1,-4)-(b-3)D.
     C  l1.y0.y0.x1^b.u2 (b=1..4):  fixed (-8,-12), (0,0); moving bD, (-4,-6)+bD, (-9,-14)+bD.
     B  l1.y0^(2a).y1.u2 (a=1..4):  fixed (-4,-8), (-3,-6); moving (-8,-14)-(a-1)(8,12), (-3,-6)-(a-1)(8,12).
     D  l1.x0^(2a).y1.u2 (a=1..3):  fixed (-1,-2), (0,0); moving (8,12)a, (3,4)+(a-1)(8,12).
  So a twist region moves a sub-configuration by +-D per crossing (channels V_2 against V_0; V_4 cannot occur there by the fusion rules:
  A (x) band (x) band must fuse to V_1, and V_1 (x) V_4 = V_5 + V_3 does not contain V_1, so the space of intertwiners is
  two-dimensional and J(T_b) = A + B lambda^b, lambda = -t^(+-1), in unit normalisation [PROVED, recoupling]), a hook run by +-(P - D) = +-(4,6) per hook (V_3 against V_1). The fixed and the
  moving vertices differ by multiples of the translation vector plus a bounded part, and the new blocks fill the gap
  along the translation direction; this is why the long edges of the Newton polygon have directions D and P - D and why
  no tie between a fixed and a moving top vertex produces a flat edge in these families.
- ANSWER TO (3). The complex is flat because its extreme generators are states related by flipping bad chords, which is
  the bidegree (1,0) of the differential. The homology is organised not by states but by the fusion channels of the twist
  regions and hook runs of the band; every channel has quantum shift strictly larger than its homological shift
  (difference = number of turnbacks j >= 1), all channel differences have slope q/h in {2, 3/2, 4/3}, and P = D + (P - D)
  has slope 8/5. The filtration that makes the top visible is therefore the one by fusion channel (band structure), not
  by circles and not by delta.
- [CONJECTURED] CHANNEL FILTRATION. For a band diagram with twist regions R_i (b_i band crossings) and hook runs H_j (m_j
  hooks) there is a filtration of C_b by channel states phi with graded pieces N_phi supported, in unit-normalised
  gradings, at  sum_i b_i e(phi_i) + sum_j m_j f(phi_j) + (a set depending only on the combinatorial type of phi, not on
  b_i, m_j),  e in {0, D, P - D} up to sign, f in {0, P - D}. Established: the local eigen-bidegrees (3.3), the minimal local
  complexes (3.2), the translation behaviour in four families. Not established: the filtration itself (the eigen-filtration
  of powers of the hook and of the band crossing in the Bar-Natan category, compatible with the type-b quotient).
  NP would follow from the channel filtration together with: the quantum-maximal channel state is unique, or all
  quantum-maximal channel states lie on one delta-level. The only way to violate NP is a tie between channel states
  whose bidegrees differ by (m,0), e.g. (V_4,V_0,V_0) against (V_2,V_2,V_2) on three band crossings.

- [PROVED; DATA: confirmed at all 50 adequate ends of the table, py/almost.py] Proposition 2.5 (almost-extreme degree at an
  adequate end). Let G' be the reduced state graph of s_1: vertices = circles of s_1 and ONE vertex for the two strands,
  one edge for each pair of distinct vertices joined by at least one crossing (crossings joining the two strands are
  ignored). If H is b-adequate at the 1-end then
        dim N in bidegree (top corner) - D  =  b_1(G') = |E(G')| - |V(G')| + 1,
  i.e. J = +-( q^M - b_1(G') q^(M-2) + ... ).  Proof: in quantum degree M - 2 the complex is, in homological degrees
  n-2, n-1, n: (pairs of parallel chords) -> (single chords, all v_+) -> (s_1 with one v_-); the second map is the
  incidence map of the state graph with the strands as base point (strand label = 0), the first sends a parallel pair
  {c,c'} to e_c + e_c'. The kernel modulo the image is the cycle space of the reduced graph. QED
  (This is the type-b version of the "second coefficient = cyclomatic number of the reduced graph" for adequate links.)

## 4. What a diagram needs for the top quantum Euler characteristic to vanish; role of T(infinity) = unknot (task 4)

- [PROVED] PARITY RULE. On C_b all quantum degrees have one parity, and for a generator (s, labels):
  h = |s| = q + k(s) (mod 2) (cube coordinates). So the sign of a generator in J is fixed by the parity of the number of
  circles of its state: the coefficient of q^d in J is +-( #generators with k(s) even - #generators with k(s) odd ).
  In lattice coordinates this parity is the parity of the delta-level b.
- AT THE TOP OF THE DIAGRAM (degree M = 4c + k(s_1)) [PROVED]: the Euler characteristic is the sum over subsets of bad
  chords of (-1)^|I|, which is 0 exactly when there is at least one bad block, i.e. when some crossing of the half-diagram
  has, after 1-smoothing, its two arcs joined around one complementary region by state arcs and segments of the axis
  (or, for a pass-by axis crossing, when the strand is joined to the axis in this way). In that case the homology in
  degree M vanishes as well. So for a band diagram "Euler characteristic zero with non-zero homology" never happens in
  the diagrammatic top degree: the extreme part is F or 0.
- AT THE TOP OF N [reformulation, PROVED]: END fails at the top iff the classes of N in its top quantum degree q* are
  carried equally often by states with an even and with an odd number of circles; NP fails iff two such classes sit in
  different homological degrees. In channel language (section 3, conjectural) this needs two quantum-maximal channel
  states whose total bidegrees differ by (m,0), m odd for END.
- WHAT T(infinity) = UNKNOT DOES:
  (a) [PROVED] It is exactly the condition for T to have a band diagram (T is the tangle of a finger of the unknot A
      pushed along an arc k with ends on A; conversely such a tangle has unknot closure). For band diagrams the Lando
      graph is edgeless (Proposition 1.3). For other diagrams of the same tangle the extreme part can be richer
      [DATA: kht++-simplified diagram of 6_2-1, bottom: 125 extreme states, homology of rank 1].
  (b) [PROVED] It pins the unit position U = (2c - 2wr, 2c - 4wr): flat means chi = +- q^(d_0). This turns every one-sided
      degree bound into non-flatness (Theorems 2.3, 2.4).
  (c) [PROVED, by example] It does NOT prevent bad blocks; the axis, which is the unknot closure itself, creates them: in
      the trefoil half-diagram the two state arcs at the crossing y1 lie on different Seifert circles upstairs but on one
      boundary curve downstairs, joined along the axis. And for tangles whose N has its top in odd or negative absolute
      homological degree bad blocks are unavoidable in every band diagram (section 3.1).
  (d) [CONJECTURED, DATA] The true statement behind END seems to be much stronger than what the extreme part of the cube
      shows: dim N^top = 1 in 127 of 128 cases, dim N^top = 2 in one homological degree once (9_37-2, whose 1-end has the
      two bad blocks "horizontal band crossing on alpha" and "pass-by hook on alpha"). Without the unknot hypothesis the
      corresponding statement is false for formal objects (B0) and I expect it to be false for actual tangles with a
      knotted closure (N of a strand with a local knot K is a reduced Khovanov homology of K; not checked here).
- B0 IN THIS LANGUAGE. N(B0) has two generators in its top quantum degree, in homological degrees differing by one. By
  Theorem 2.1 a tangle with a b-adequate end cannot look like this at that end; by Theorem 2.4 a tangle with a
  homogeneous half-diagram cannot have its unit where B0 has it. So the realisation input that B0 violates, in the cases
  where the cube lens proves something, is: "the extreme state of a band diagram is a single state, of type b, and all
  its chords are honest merges". For non-adequate ends the cube lens does not at present exclude a B0-like top.

## 5. Nesting under twisting (new DATA; a second route to NP for families)

- [DATA, kht++ runs, py/famrel.py; gradings relative to the unit U] In the four families of 3.3 the invariant is NESTED:
        N(T_b)  is a sub-multiset of  N(T_(b+1)),
  with nothing lost and exactly four new generators at each step, and the four new generators at step b+1 are the four new
  generators of step b translated by the eigen-vector v of the family:
     A  l1.y0.y0.y1^b.u2 :  new at b -> b+1:  {(-9,-16), (-5,-10), (-4,-8), (0,-2)} - (b-1) D          (v = -D)
     C  l1.y0.y0.x1^b.u2 :  new:  {(-7,-10), (-3,-4), (-2,-2), (2,4)} + (b-1) D                      (v = +D)
     B  l1.y0^(2a).y1.u2 :  new at a -> a+1:  {(-16,-26), (-12,-20), (-11,-18), (-7,-12)} - (a-1)(8,12)  (v = -2(P-D))
  The four new points are  w, w + (P - D), w + P, w + 2P - D:  two D-pairs and two P-pairs, completed to squares / longer
  staircases by generators already present.
  So in the normalisation by the unknot closure N(T_b) = (fixed core) + (a ladder of translates of one four-element set
  along an eigen-direction). In cube coordinates the same statement reads: the old generators move with the V_0-channel
  eigen-bidegree (4,6) per added crossing, the new ones with (3,4).
- [CONJECTURED; refined in section 7: for a twist region between PARALLEL strands the normalisation must be changed]
  NESTING. For every twist region and every hook run of a half-diagram, adding one crossing of the same sign
  (resp. two hooks of the same type) embeds N, in unit-normalised gradings, into the new N, with a complement of four
  generators that is translated by +-D (resp. +-2(P - D)) at each further step. Expected source: the eigenmap of the
  lowest channel, lambda_0 . [[twist^b]] -> [[twist^(b+1)]], whose cone is supported on the other channels (this is the
  mechanism behind stable Khovanov homology of torus links); the content of the conjecture is that the long exact
  sequence splits.
- [PROVED from the conjecture] If NESTING holds for a family T_b with translation vector v, then NP for all b >= b_0 follows
  from NP for the core and the first ladder step unless the top of the core and the top of the ladder tie at different
  homological degrees for one value of b: the top of the ladder moves monotonically in q (every eigen-vector has q != 0),
  so it meets the top of the core at most once. In families A, B, C, D the core top and the ladder top lie on one line of
  direction v (e.g. (0,-2) and (-1,-4) - tD in family A), so they never tie at different h.

- [DATA, strongest form; N_rel_unit.json, 128 tangles of the table with kht++ output] NESTING holds for EVERY pair in the
  table: among the 138 half-diagrams there are 42 pairs (H, H') where H' is H with one more copy of an off-axis crossing
  letter in a twist region, or two more copies of an axis crossing letter in a hook run (3_1 -> 5_2-1, 3_1 -> 5_2-2,
  4_1 -> 6_1, 5_1 -> 7_5, 6_2 -> 8_4, 8_6, 8_11, 6_3 -> 8_8, 8_13, 7_1 -> 9_6, 9_9, 7_3 -> 9_10, 9_13, 7_4 -> 9_5, 7_5 -> 9_7,
  9_18, 9_23, 7_6 -> 9_8, 9_12, ...). In all 42, N(T_H) is a sub-multiset of N(T_H') in unit-normalised bigradings. The
  number of new generators is 4, 8, 12, 16, 20 or 24. Nesting starts with the first crossing of a region (b = 1 -> 2), but
  NOT when a region is created (b = 0 -> 1): the unknot's N = {U} is not contained in N(3_1).
  Consequences if true in general: (i) dim N, the Newton polygon and the quantum span are monotone under twisting;
  (ii) decategorified, J(T_b) = A + B lambda^b with lambda = +-t^(+-1) (twist) or t^(+-6) (hook pair), the usual two-channel
  twisting formula, so at most one member of a twist family with B != 0 can be flat; (iii) every statement about the
  outline of N (NP, END, polygon law) reduces to "cores" (all twist regions of length <= 2, all hook runs of length <= 2)
  plus the position of the first new block, because later blocks are translates.

- [DATA, py/grid2.py, 30 kht++ runs] Two-parameter two-bridge grids, a = 1..3, b = 1..5, unit-normalised gradings:
     l1.y0^(2a).y1^b.u2 :  dim N = 4ab - 1;  top = (-3,-6) for b = 1 and (0,-2) for b >= 2 (independent of a);
                           bottom = (-8a, -12a - 2) - (b-1) D   (the two regions add their shifts).
     l1.y0^(2a).x1^b.u2 :  dim N = 4ab + 1;  top = b D (independent of a);  bottom = (-8a, -12a) (independent of b).
  In all 30 tangles the top and the bottom quantum degree of N are one-dimensional. The extreme vertices are SUMS of the
  shifts of the two regions (Minkowski behaviour), so the two regions never compete and no tie occurs. A tie needs regions
  that exclude each other's extreme channel; two-bridge families do not have this.
- PROOF ROUTE FOR NESTING [CONJECTURED]. For a single strand, sigma^b = (1 -> e{1} -> e{3} -> ... -> e{2b-1}); in gradings
  normalised by the lowest channel (subtract b(1,2)) the objects e sit at (-m, -2m-1), m = 0..b-1, independently of b, a
  new one is appended at the far end when b grows, and only the object "1" moves, by -D. The band data have exactly this
  shape (old generators fixed, four new ones at the far end of a ladder in direction -D). So the statement to prove is:
  in the type-b quotient the complex of a band twist region of length b is a ladder of b rungs whose rungs are fixed in
  V_0-normalised gradings, and the long exact sequence of "append one rung" splits on N for degree reasons.

- [DATA] WHAT HAPPENS WHEN A REGION IS CREATED. Extrapolating the ladders of families A and B back by one step gives, for
  both, the same four-element block  S = {(-8,-14), (-4,-8), (-3,-6), (1,0)} = w, w + (P-D), w + P, w + 2P - D  (w = (-8,-14)),
  and  N(unknot) + S = {(0,0)} + S = N(trefoil) + {(0,0), (1,0)}.
  So at the creation step the new block is attached with ONE cancellation, between the unit generator (0,0) and the top
  element (1,0) of the block: a pair at the offset (1,0) of the differential (the offset of Codex's B0). After that
  (b >= 1) blocks are appended without cancellation. In the other twisting direction (family C, 4_1, 6_1, 8_1, ...) there is
  no cancellation even at creation: (0,0) stays in N.
  READING [CONJECTURED]: there is a spectral sequence with E_1 = (unit) + (one block for each rung of each twist region /
  hook run, positioned by the channel shifts) and differentials of bidegree (1,0), abutting to N; NESTING says the
  differential vanishes on all rungs after the first. Lemma Q would follow from: the unit can be cancelled only by the top
  element of a first rung, and then the rest of that rung (three generators with Euler characteristic of the shape
  +-t^w (1 + t^3 - t^4), as for the trefoil: J = t^-7 + t^-4 - t^-3) survives.

## 6. Files

py/bcube.py (quotient word as in kht++, transfer matrix for chi_q(C_b), extreme states), py/fullcube.py and py/reps.py (brute
force C_b and N for small diagrams), py/survey.py -> survey.jsonl (138 half-diagrams: extreme part versus kht++), py/badblocks.py,
py/census.py, py/criteria.py, py/negcheck.py (adequacy, unit position, positivity), py/almost.py (Proposition 2.5),
py/family.py, py/famrel.py, py/grid2.py, py/grid3.py (kht++ runs in kht/, cache kht/cache.jsonl), py/unitpos.py, py/cone.py
-> N_rel_unit.json (N of the 128 table tangles relative to the unit), py/onebad.py, py/showN.py.
Checked and REJECTED along the way (do not redo): (i) the kht++-simplified diagrams are not more often adequate than the
band diagrams; (ii) a "cone law" N - U inside {h <= q <= 2h} fails (445 generators violate it); (iii) defects are not
additive over bad blocks; (iv) no class of N has a single-generator cycle representative in the trefoil cube.

## 7. Addendum to section 5: the new generators are Z-blocks; scope of the nesting data

- [DATA] In all 42 nested pairs of the table the new generators are a disjoint union of translates of ONE four-element set
        B(w) = { w, w + (P - D), w + P, w + 2P - D } = w + {(0,0), (4,6), (5,8), (9,14)}
  (1 to 7 blocks per step). In lattice coordinates (a,b) this is the Z-tetromino (0,0), (0,1), (-1,1), (-1,2): a staircase
  segment P, -D, P, i.e. two P-pairs (two special components of Kh~) at relative shift P - D. Its Euler characteristic is
  +-t^w (1 + t^3)(1 - t^4). (A square of BN~ is the O-tetromino {x, x+D, x+P, x+D+P}, two P-pairs at relative shift D.)
- SCOPE (honesty). All 42 pairs, and families A-D, are two-bridge knots, whose N is a single staircase. Whether nesting and
  the block shape persist for half-diagrams with compact components (squares) is tested below on a few non-two-bridge
  half-diagrams (results appended when the runs finish; if no line follows, the runs did not finish in time).

- [DATA, check of the unit formula of section 2 against the brief's independent normalisation] In kht++'s own gradings the unit
  sits at (h,q) = (8j, 24j), j = lk(T(0))/4 read off from the rational component of Kh~ (brief, [T] = q^(24j)[Q_0] + ...).
  Converted to cube coordinates this equals (2c - 2wr, 2c - 4wr) in all 128 tangles of the table with kht++ output
  (0 disagreements). So the unit formula, and with it Theorems 2.3 and 2.4, do not depend on my sign calibration.

- [DATA, kht++ runs, py/nest_dbl.py] BEYOND TWO-BRIDGE: doubled tangles of the torus knots T(2,b), half-diagram l2.y1^b.u2
  (no axis crossings; N has squares; dim N = b^2 = 9, 25, 49 for b = 3, 5, 7). Here the twist region is braid-like (its two
  strands are parallel, the oriented smoothing is the VERTICAL band smoothing). Result:
    * In unit-normalised gradings N is NOT nested (bottom generator at (0, 2g(K#K)) = (0,4), (0,8), (0,12), as Theorem 2.4
      predicts for these positive, bottom-adequate diagrams).
    * In cube coordinates, i.e. normalised by the vertical channel V_4, N IS nested: N(3) in N(5) in N(7).
    * The new generators move with BOTH other channels: new(5 -> 7) contains new(3 -> 5) + 2(4,6) and new(3 -> 5) + 2(3,4)
      (two crossings times the V_0 - V_4 and the V_2 - V_4 eigen-differences). The new sets are not unions of Z-blocks.
  REFINED NESTING CONJECTURE: nesting holds in the gradings normalised by the channel of the ORIENTED smoothing of the
  region: the horizontal channel V_0 (= unit normalisation) for a twist region between antiparallel strands and for hook
  runs (an axis crossing is always antiparallel: the strand meets its reversed image), the vertical channel V_4 (unit
  shifted by -+(P - D) per crossing) for a twist region between parallel strands. This is the tangle form of "Khovanov
  homology is concentrated near the oriented resolution and stabilises under twisting".
- NOT DONE: nesting for half-diagrams with both axis crossings and compact components (pretzel-type words with a letter at
  position 2). Two test pairs turned out to be links and the others (8_15-2, 8_18-1, 9_46-1 with one more crossing) were
  stopped because each kht++ run exceeded four minutes.

## SUMMARY

PROVED
1. Extreme part of the cube (Lemmas 1.1, 1.2, Proposition 1.3, Corollary 1.4). For the twist-free band diagram of any
   half-diagram: framing twists are frozen in type-b states; the all-one and all-zero states are of type b and are the
   unique extreme vertices; the bad chords come in twin pairs (one pair per bad band crossing or bad pass-by hook) and are
   pairwise non-interleaved, so the Lando graph has no edges and the set of extreme states is a Boolean cube with
   4^(bad blocks) elements. The top (bottom) quantum degree of the complex has homology F if the half-diagram is b-adequate
   at that end and 0 otherwise; its Euler characteristic is 1 or 0. Bad blocks are read off the half-plane picture: a
   crossing is bad iff its two smoothing arcs are joined around one region by state arcs and segments of the axis.
2. Adequate ends (Theorem 2.1, Corollary 2.2, Proposition 2.5). At a b-adequate end N is one-dimensional in its extreme
   quantum degree, at the cube corner (NP and END at that end); in the next degree its dimension is the cyclomatic number
   of the reduced state graph; b-adequate at both ends implies non-flat.
3. Unit position (section 2; checked against the brief's (k,j) normalisation on all 128 tangles): in cube coordinates
   flat <=> chi_q(C_b) = +- q^(2c - 4wr), the unit sitting at (2c - 2wr, 2c - 4wr). Hence Theorem 2.3 (one adequate end not at
   the unit => non-flat) and Theorem 2.4 (positivity): if all crossings of the half-diagram have one sign, the whole cube
   lies at least 2 g(K) beyond the unit, so Lemma Q holds for strongly invertible knots with a positive or negative
   half-diagram. On the 138 half-diagrams: 7 adequate at both ends, 43 at one end at least, 39 homogeneous; 72 are non-flat
   by these counts alone.
4. Local structure (3.2, 3.3): minimal complexes of the hook (9 objects) and of the band crossing (13 objects); the twist
   eigenvalues on the fusion channels are 1, -q^4, q^6 (band crossing), 1, q^6 (hook), i.e. the bidegrees (3,4) = P - 2D and
   (4,6) = P - D, and (1,2) = D for a single crossing. So the lattice Z D + Z P of the brief is the lattice of twist
   eigen-bidegrees and the edge directions of the polygon law are the differences of channels of one block; the direction
   (1,0) is not such a difference. In two-bridge-type regions the fusion rules allow only two channels (J = A + B lambda^b).
5. Negative results. (a) The only filtration of the cube by circles (number of v_-) sees a simplex at the top, and delta is
   a grading, so neither makes the top of N visible. (b) At an adequate end the extreme generator of N has even absolute
   homological degree of a fixed sign; for 54 of 128 tangles the top (50 the bottom, 16 both) violates this, so NO band
   diagram of those tangles is adequate there: extreme states cannot prove NP or END in general. (c) The distance from the
   cube corner to the true top of N is not additive over bad blocks.

CONJECTURED / DATA
- dim N^top = dim N^bottom = 1 in 127 of 128 table tangles (2 in one homological degree for 9_37-2 top, 9_40-2 bottom).
- CHANNEL FILTRATION (3.3): N is filtered by fusion-channel states of the twist regions and hook runs, with shifts
  b e(phi) and m f(phi), e in {0, +-D, +-(P - D)}, f in {0, +-(P - D)} in unit-normalised gradings.
- NESTING (sections 5, 7): in the gradings normalised by the channel of the oriented smoothing of the region (unit
  normalisation for antiparallel twist regions and for hook runs; vertical-channel normalisation for parallel regions)
  N(T_H) is contained in N(T_H') whenever H' has one more crossing in a twist region or two more hooks in a hook run.
  Data: 42 of 42 pairs of the table, four one-parameter families and a 30-point two-parameter grid (all two-bridge; new
  generators are Z-blocks w + {0, P - D, P, 2P - D}, translated by +-D per crossing or +-2(P - D) per hook pair), and the
  doubles of T(2,3), T(2,5), T(2,7) (with squares; all three channels move). At the creation of a region there is one
  cancellation, between the unit generator and the top of the first block, at the offset (1,0). Not tested: half-diagrams
  with axis crossings and compact components together.

NAMED GAP
The top of N at a non-adequate end. There the extreme degree of the cube is acyclic and nothing in this lens excludes two
classes of N in the top quantum degree at an offset (m,0) (the B0 pattern). What is missing is the channel filtration, i.e.
the splitting of the exact triangle "append one rung to a twist region" (NESTING), and a rule for ties between channel
states of different regions.

MOST PROMISING NEXT STEP
Prove NESTING for a single twist region: show that in the type-b quotient the Bar-Natan complex of a band twist region of
length b is a ladder whose rungs are fixed in V_0-normalised gradings (the analogue of sigma^b = 1 -> e{1} -> ... -> e{2b-1}),
and that the connecting map of "append one rung" vanishes on N for b >= 1 for degree reasons. First computation: the minimal
complexes of (band crossing)^2 and hook^2 from the 13- and 9-object complexes of section 3.2; then test nesting and the block
shape on a family with compact components (pretzel-type half-diagrams with a letter at position 2).
