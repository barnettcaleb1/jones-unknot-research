# REFEREE NOTES: Theorem A (shape law for unit arrows), annular/REPORT.md section 2

Referee: independent check, started 2026-11-16. Target: /Users/calebbarnett/jones-lanes/theory-restart/mech2/annular/REPORT.md, sections 2.1-2.7.
Scripts and kht++ working folders: /Users/calebbarnett/jones-lanes/theory-restart/mech2/verify/shape-proof/ (my own code; nothing imported from annular/scripts).
Marks: [OK] verified by me, [CORR] correction needed, [GAP] step not justified as written, [NOTE] remark, [UNCHECKED] not verified.
This file is written as I go; the VERDICT section at the end is the summary.

## 1. Citation check against the source (arXiv:2202.01460v1, TeX at lit/kwz-linear/src/tex/sections/WrappingSpecial.tex, read in full for 4.1 and the proof of 4.4)

1.1 [OK] Numbering. Section 4 of v1: Theorem 4.1 (no wrapping around the special puncture), Definition 4.2 (B^infty), Definition 4.3
    (B^*[U], B^*[U,U^-1]), Theorem 4.4 (extension property), Assumptions 4.6 (on the diagram). Confirmed in the PDF text (kwz-linear.txt
    lines 642-747) and the TeX counters (one shared counter per section).

1.2 [OK] Definition 4.2. mu_2 as in B. Disk sequences: E_4 = the four cyclic rotations of (oS., .D., .So, oDo); E_(2m+2) from E_2m by the four
    interposition rules (..., D^k, S^l, ...) -> (..., D^(k+1), S, D, S^(l+1), ...) and (..., S^k, D^l, ...) -> (..., S^(k+1), D, S, D^(l+1), ...)
    (two idempotent versions each). Products: mu_2m(a_1,...,a_2m b) = b and mu_2m(b a_1,...,a_2m) = b for b in {id, S^n, D^n} with
    a_2m b != 0 resp. b a_1 != 0. (The source prints "n > 1"; the displayed examples "for any k >= 1" show that n >= 1 is meant.)
    The four mu_4 families quoted in the report are exactly the four displayed in the source, and they are ALL the non-zero mu_4 on basis
    elements: this follows from the definition (E_4 has only the rotations of (S,D,S,D)), and is stated verbatim in the later version
    arXiv:2602.23442 Remark 10.3 ("there are no other sequences of basic algebra elements for which mu_4 is non-vanishing").
    The report's remark "mu_2m (m >= 3) needs an argument D^j with j >= 2" is correct (every interposition raises one D-power and one
    S-power), and it also needs an argument S^j with j >= 2. Neither is used in the proof (only the order U^2 equation is used).

1.3 [OK] Definition 4.3. B^*[U] = B^infty (x) F_2[U], mu_k carries U^(k-2); gr(U) = q^-3 h^-1, gr(S) = q^-1, gr(D) = q^-2, gr(mu_k) = q^0 h^(2-k).
    So an arrow x -> y with label U^i a has h(y) - h(x) = 1 + i, q(y) - q(x) = 3i + |a| (|S^k| = k, |D^k| = 2k). A U^2.1 arrow has (h,q)-shift (3,6).

1.4 [OK] Theorem 4.4, as printed: "Given a diagram D_T of an oriented pointed Conway tangle, there exist type D structures D(D_T)^{B^*[U]} and
    D^c(T)^{B^*[U]} such that D(D_T)^{B^*[U]}|_{U=0} = D(D_T)^B and D^c(T)^{B^*[U]}|_{U=0} = D^c(T)^B. The same ... for D_1(D_T)^B and D_1^c(T)^B."
    D^c(T) is "a type D structure from which BN~(T) can be read off directly" (Section 2.1 of the source). Coefficients F_2 throughout.
    The extension is bigraded (differential of degree q^0 h^1 for the grading of 1.3): this is how the source uses it in the proof of Thm 4.1
    and it is what the construction gives (Section 4.3 of the source: "bigraded type D structure ... with a positive differential").

1.5 [OK] Order convention. In the source an element with left idempotent X and right idempotent Y (written XaY) is an arrow from Y to X
    (quiver (2.1) of the source is drawn with reversed arrows; S^3_. = oS. .So oS.), so for a path x -a_1-> . -a_2-> . ... -a_k-> y of the
    type D structure the structure equation uses mu_k(a_k, ..., a_1) ("we read the higher multiplications from right to left", comment in
    the TeX, and the use mu_4(S,D,S,D) for the path D,S,D,S in the proof of Thm 4.1). The report writes the labels in path order and
    quotes "mu_4(D,S,D,S^k)" for a path with labels (D,S,D,S^2); in the source's convention the relevant product is mu_4(S^2,D,S,D) = S.
    Both families exist, so the VALUE used is right. More precisely the set of non-zero mu_4 is invariant under reversing the order of the
    arguments (with the induced swap of the two S's): reversal exchanges family 1 with family 4 and family 2 with family 3. So the order
    convention cannot affect any first-order statement. (Checked by machine for E_4, E_6, E_8 in section 3 below.)

1.6 [OK] The equation (*) of the report. With delta = delta_0 + U delta_1 + U^2 delta_2 + ..., the type D structure equation
    sum_k mu_k(delta,...,delta) = 0 in B^*[U] (mu_1 = 0, mu_odd = 0) reads in degree U^2:
        mu_2(delta_0,delta_2) + mu_2(delta_2,delta_0) + mu_2(delta_1,delta_1) + mu_4(delta_0,delta_0,delta_0,delta_0) = 0.
    delta_1 = 0: the source proves this in the proof of Thm 4.1 by q-parity. I re-derived the parity statement in the form needed
    (the source only says "same parity in the same idempotent"): in the cube of resolutions a saddle either changes the number of closed
    circles by one and keeps the connectivity type (b or c) of the arcs, or keeps the number of circles and changes the type; in both cases
    q + (type) is preserved mod 2. So q mod 2 is a function of the idempotent on the whole complex, and the two idempotents have opposite
    parity. A label U.a needs q-shift 3 + |a|, which has the wrong parity for every a (|a| is even iff a preserves the idempotent).
    Confirmed on data in section 4 below (all b-generators of a chain file have one q-parity, all c-generators the other).
    Also strict unitality: mu_2m vanishes when an argument is an idempotent (immediate from Def. 4.2), so U^2.1 arrows never enter mu_4.

1.7 [NOTE] Hypotheses of Theorem 4.4 that the report does not mention.
    (a) Coefficients F_2 only in 2202.01460. Over F_2 a one-dimensional local system is trivial, so the clause "trivial local system" in
        Theorem A(i) and the parenthesis "(With a local system X ... A = X, B = A, B = 1)" have no content there. Over other fields the
        statement must be taken from arXiv:2602.23442 Thm 10.4 (text at lit/kwz-linear/src/mut2026/mut.txt lines 3905-3960), where
        mu_2m carries the sign (-1)^(m-1) (their U is the square of the old U). With that sign the cancellation in Step 3 gives
        holonomy -1 in the sign conventions of that paper (compare its proof of Thm 7.10: "can only be cancelled if c = -1"), not +1.
        Whether "-1" is the trivial local system is a matter of the sign convention for curve-form type D structures; the report's
        parenthesis was not derived with signs and should be deleted or redone. [CORR, minor]
    (b) Theorem 4.4 is proved for diagrams satisfying Assumptions 4.6 (both top ends oriented outwards, connected diagram, the region x_3
        adjacent to a single crossing), which the source says can always be achieved "by changing the orientation on components and rotating
        D_T by 90 degrees" and by Reidemeister moves. For a pointed tangle whose special strand joins the two top ends (the connectivity of
        Q_0) the orientation condition cannot be met without the rotation, and the rotation moves the special end to the other strand.
        The source treats this as harmless and states the theorem for every oriented pointed Conway tangle; I did not re-prove that
        reduction. Theorem A inherits exactly the generality of KWZ's Theorem 4.4 as stated. [UNCHECKED, belongs to the cited paper]
    (c) 2202.01460 is described by its authors (2602.23442, introduction) as "an earlier, unpublished version"; the extension property is
        restated there as Theorem 10.4 for every field. Neither is, to my knowledge, published in a journal. [NOTE]
    (d) Which representative. Theorem 4.4 gives an extension of "D^c(T)", the output of the arrow sliding algorithm. Theorem A is applied
        to any curve-form representative (e.g. kht++ output). This is fine: two reduced representatives are isomorphic over B, an
        isomorphism is a product of elementary base changes x -> x + a.y of bidegree 0 (triangular in q for a in B_+, and GL over F_2
        for a = 1), and the proof of Lemma 4.27 of the source ("Case 1: Clean-up") lifts every such elementary base change to the
        extension. The report should say this in one line. [NOTE]

## 2. Line-by-line check of the proof (report 2.3)

Notation of the report: composable junction w -D-> x -P-> y with run x -S-> c_1 -D-> c_2 -S^2-> c_3 -D-> c_4 -S-> y.
I checked every step by listing ALL terms of (*) in the relevant matrix entry (x0 -> x1, coefficient of one basis element of B).
A term of (*) from x0 to x1 is one of: (m4) a delta_0-path of length 4 from x0 to x1 on which mu_4 is non-zero; (L) a delta_0-arrow out
of x0 followed by a delta_2-arrow; (R) a delta_2-arrow out of x0 followed by a delta_0-arrow into x1. In curve form with a one-dimensional
local system the delta_0-arrows at a generator are its (at most one) D-power arrow and its (at most one) S-power arrow, so the lists
below are complete. delta_2-arrows may a priori join ANY two generators of the whole complex D^c(T) (other components included); they
only enter through (L) and (R), where one end is a delta_0-neighbour of x0 or x1, so other components never contribute to the entries
used. By the bigrading (1.3) a delta_2-arrow between two c-generators at (h,q)-distance (3,6) can only carry the label 1.

Step 1, entry (w -> c_3), coefficient of S.  [OK]
  (m4) the only path of length 4 into c_3 is w,x,c_1,c_2,c_3 (each of c_2, c_1, x has exactly one incoming arrow); labels (D,S,D,S^2);
       mu_4(S^2,D,S,D) = S.  Contribution 1.
  (R)  only arrow into c_3 is c_2 -S^2->; S^2.a never has an S-term.  0.
  (L)  w -D-> x followed by a: a.D has no S-term. 0.  The S-side arrow of w, if it LEAVES w with label S^k to z: a.S^k = S iff k = 1 and
       a = 1.  So: w has an outgoing arrow w -S-> z, z a c-generator, and delta_2(z -> c_3) = 1.
  [GAP, fixable] The report concludes "Hence: w starts a run w -S-> c_1' -D-> c_2' -S^2-> c_3' -D-> c_4' -S-> y'". This does not follow:
  (U2) only constrains chains of c-generators BETWEEN TWO b-generators; the chain starting at z may be the TAIL of the arc (ending at a
  puncture), about which the hypotheses say nothing. The case must be treated; it is treated in "Tail cases" below and is obstructed.

Step 2, entry (z -> c_4), coefficient of D (z = c_1').  [OK]
  (R) only arrow into c_4 is c_3 -D->; D.delta_2(z -> c_3) = D. Contribution 1.
  (m4) the only 4-path into c_4 starts at x, which is not z. 0.  (The report's remark about the 4-path FROM c_1' is beside the point
       but harmless.)
  (L) z has S incoming (from w), so its only possible outgoing arrow is its D-side arrow z -D^j-> z_2: a.D^j = D iff j = 1, a = 1.
  So z -D-> z_2 =: c_2' and delta_2(c_2' -> c_4) = 1.

Step 3, entry (c_2' -> y), coefficient of S.  [OK, uses (U2) twice]
  (R) arrows into y: c_4 -S-> y gives S.1 = S, contribution 1; the D-side arrow of y, if incoming, gives D.a, no S-term.
  (L) the S-side arrow of c_2' if outgoing, c_2' -S^k-> z_3: a.S^k = S iff k = 1 and a = 1; then z_3 is a b-generator and (c_1', c_2')
      is a maximal c-chain between the b-generators w and z_3 that is not a run: excluded by (U2). [This is the "R = L-1" situation of
      report 2.6; it is exactly where (U2) is needed.]
  (m4) a 4-path c_2' -> y. Last arrow c_4 -S-> y: the path would be c_1,c_2,c_3,c_4,y and start at c_1; c_1 != c_2' (c_1 has no incoming
      D-arrow), and its labels (D,S^2,D,S) give mu_4 = 0 anyway. Last arrow y* -D-> y (y* a b-generator): the path is
      c_2' -S^l-> u_1 -D^j-> u_2 -S^k-> y* -D-> y with u_1, u_2 c-generators; then (c_1', c_2', u_1, u_2) is a c-chain between the
      b-generators w and y*, hence a run by (U2): l = 2, j = 1, k = 1, and mu_4(D,S,D,S^2) = S. Contribution 1.
  So the entry vanishes iff w -P-> y' and y' -D-> y. Then w, x, y, y' each have both sides occupied by arrows among these twelve
  generators: the component is the unit square. (Coincidences such as y' = x are impossible: x would need two S-side arrows.)

Mirror case "P then D" (w -P-> y' -D-> y, run through c_1'..c_4').  [OK; the report only says "mirror argument"; written out:]
  Entry (c_2' -> y), coefficient of S: (m4) the unique forward 4-path from c_2' is c_2',c_3',c_4',y',y, labels (S^2,D,S,D), value S;
  (L) c_2' -S^2-> then a: no S-term; (R) y' -D-> y: no S-term; the S-side arrow of y if incoming, z -S^k-> y: S^k.a = S iff k = 1, a = 1.
  So y has an incoming arrow z -S-> y from a c-generator z with delta_2(c_2' -> z) = 1.
  Entry (c_1' -> z), coefficient of D: (L) c_1' -D-> c_2' -1-> z gives D; (m4) none (the forward 4-path from c_1' ends at y');
  (R) the D-side arrow of z if incoming, z_3 -D^j-> z: j = 1 and delta_2(c_1' -> z_3) = 1. So z_3 -D-> z.
  Entry (w -> z_3), coefficient of S: (L) w -S-> c_1' -1-> z_3 gives S; the D-arrow of w gives no S-term; (R) an arrow u -S-> z_3 from a
  b-generator u would make (z_3, z) a two-element c-chain between b-generators: excluded by (U2); (m4) a 4-path
  w -D-> u_1 -S^l-> u_2 -D^j-> u_3 -S^k-> z_3 (the first arrow must be the D-arrow of w, since c_1' has no outgoing S-arrow); then
  (u_2, u_3, z_3, z) is a c-chain between b-generators u_1 and y, a run by (U2), and mu_4(S^2,D,S,D) = S.
  So the entry vanishes iff w -D-> x and x -P-> y through z_3 = c_3, z = c_4: the unit square again.

Tail cases (missing in the report).  [GAP closed here]
  (a) "D then P" with the S-arrow of w starting a tail w -S-> z ...: Step 2 still forces z -D-> z_2 with delta_2(z_2 -> c_4) = 1 (or
      there is an obstruction). In Step 3 the term S from z_2 to y (through c_4 -S-> y) cannot be cancelled: (L) would need
      z_2 -S-> (b-generator), making the chain a non-run between two b-generators; (m4) would need a 4-path from z_2 to y* -D-> y, making
      the chain starting at z a chain between the b-generators w and y*, i.e. not a tail. Obstructed.
  (b) "P then D" with the S-arrow into y coming from a tail ... -> z_3 -D-> z -S-> y: in the last entry (w -> z_3) both (R) and (m4)
      would again force a b-generator at the far end of the chain. Obstructed.
  So a composable D/P junction forces the unit square also when the neighbouring S-arrow belongs to a tail. Machine check: section 3, T1.

End of the proof.  [OK with one correction]
  "A component without composable junctions has all its b-generators sources or sinks; if it were compact with 2r b-generators its
  homological grading would change by 4r around the cycle": correct for r >= 1 (every c-chain of a compact component with a b-generator
  lies between two b-generators, so it is a run; (U1) excludes S^(2k)-arrows between b-generators; travelling along the curve the moves
  alternate +P, -D and h changes by 5 - 1 per pair).
  [CORR] r = 0 is not covered: a compact component WITHOUT b-generators satisfies (U1) and (U2) vacuously and is neither (i) nor (ii).
  Such components pass every extension test trivially (no path of length 4), e.g. [c -D-> c, c -S^2-> c] = cone of H on a c-generator,
  which occurs in BN~ of Q_infty with a knot of H-torsion order 1 tied into a strand (checked with kht++ in section 5). Theorem A must
  assume that gamma contains a b-generator (or add the case "gamma has no b-generator"). The Corollary is not affected (such components
  contribute nothing to N).

Statement (ii), wording.  [NOTE] "every b-generator is a source or a sink" is proved for b-generators that carry both a D-arrow and a run.
  For the b-generator next to the tail the theorem says nothing: "D then tail" can be composable. It is obstructed at first order only when
  the tail at the head of the D-arrow has at least 3 more c-generators than the S-side chain at its tail end (section 3, T1b); e.g. the
  rational arc b -D-> b -S-> c (kht++: r(-1/2)) is a composable "D then tail". The sentence in report 2.4 'an arc containing ... "D then
  tail": NOT solvable' is true for the standard tail S (D S^2)^j D with j >= 1 when w has no S-arrow, not in general. [CORR, wording]

Corollary (report 2.2).  [NOTE] Beyond Theorem A it uses: (1) exactly one non-compact component (true iff T has no closed component;
  the source says BN~(T) has 2^|T| arcs); (2) the arc has an odd number of b-generators, equivalently exactly one end of the arc at the
  puncture of the D_b-face; this is the standing assumption of the project (dim N odd, T(infty) = unknot), not a consequence of unit
  arrows (for Q_infty: N = 0). With (1), (2) the statement N = Z_l + Lambda^r and H(N,d_D) = H(N,d_P) = F follows. The Corollary should
  state these two inputs.

## 3. Independent computations (my code: binf.py, ainf_check.py, tdu.py, test_basic.py, test_enum.py, test_adversarial.py)

3.0 Implementation. binf.py builds E_4, E_6, ... literally from Definition 4.2 (4, 12, 48, 220 sequences; each E_n is automatically closed
    under rotation and under order reversal combined with the anti-automorphism of B). ainf_check.py: the A-infinity relations hold on
    all composable basis sequences of length 3 (powers <= 4; 1458), 5 (powers <= 4; 118098), 7 (powers <= 3; 1647086): 0 violations
    (this exercises mu_2, mu_4, mu_6). Non-zero mu_4 on basis elements: exactly the four families of the report (36 tuples with powers <= 5).
    tdu.py: curve-form type D structures from words; (*) solved for delta_2 by Gaussian elimination over F_2 with unknowns all arrows
    x -> y, label any basis element (idempotents included) of bidegree (3, 6 + |a|).

3.1 test_basic.py  [all in agreement with report 2.3/2.4]
    unit square: mu_4 term = {w -S-> c_3, c_2' -S-> y}; solvable; solution delta_2 = {c_1' -1-> c_3, c_2' -1-> c_4}, UNIQUE (solution space of
       dimension 0 among the 4 graded candidates).
    zigzags (3_1 type with tail, 4_1 type, a 7-generator zigzag with tail k = 6, the oppositely oriented zigzag): mu_4 term 0, delta_2 = 0.
    composable junction: "D then P", "P then D", "P,D,P", a zigzag with one composable junction, three sides of the square, "D then tail
       S D S^2 D": all NOT solvable.  "D then tail S D" (k = 2): solvable (no path of length 4).
    square with D^2 sides and P_2 legs: mu_4 term 0, solvable (3-dimensional solution space); same for D^3 sides.
    square with D sides and P_1 legs: the two mu_4 terms (1.U^2 from w to y along the two sides) cancel each other; solvable with delta_2 = 0.
    square with D sides and P_3 legs: solvable, delta_2 = 4 identity arrows (unique).

3.2 test_enum.py  [reproduces the counts of report 2.4]
    +-D, +-P_2, up to 10 moves: 5 classes of gradable primitive cyclic words (1 with 4 moves, 4 with 8 moves); only the unit square passes.
    +-D, +-P_1 only / +-D, +-P_3 only: 5 classes each; only the square with those legs passes.
    +-D, +-P_1, +-P_2, +-P_3 mixed, up to 8 moves: 199 classes; 9 pass = the three squares + 6 words of 8 moves.
    +-D, +-D^2, +-P_2, up to 8 moves: 28 classes; 7 pass = the unit square + 6 others (among them the D^2-square).

3.3 test_adversarial.py  [beyond the report]
    T1. All arcs with moves +-D, +-P_2 (1 to 4 moves, all sign patterns) and ARBITRARY tails on the free S-sides of the end generators
        (tails with up to 4 c-generators, labels S^1/S^3, D/D^2, S^2/S^4, all directions; up to 3 when both ends carry a tail):
        85900 arcs, 30504 pass the first-order test, NONE of these contains a composable D/P junction. (Confirms the tail cases.)
    T1b. w -D-> x with standard tails of n_w and n_x c-generators leaving w and x: obstructed iff n_x >= n_w + 3.
    T2. Each of three obstructed pieces together with a second component (point b, point c, unit square, 3_1 arc, a second obstructed
        piece, the c-loop, a rational arc, a tail-like c-arc) placed at every relative bigrading dh in [-12,12], dq in [-24,24]:
        never solvable (27 x 1225 cases). So no arrow between components can cancel the obstruction, as the term count predicts.
    T3. Compact components with c-generators only ([c -D-> c, c -S^2-> c] and two others): mu_4 term zero, trivially extendable.
