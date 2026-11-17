# R3 (SCOPE) referee of skein_dictionary_arbitrary_boxes.md (Codex 052407). 17 Nov 2026, Claude.
Question: do the bodies quantified by Q-MONT, V3, C1 (46,771 single-box; top-300 pairs), M300/D36 satisfy the note's
hypotheses, and which statements must be restricted? Section 2-8 algebra itself is R1/R2's job; I re-checked only what
scope depends on. Scripts/logs: r3_*.py, r3_*.log in this folder (tools/venv python, lp.py, engineA vc.py).

## Checks run (all exact)
- r3_bodies.py: all 50 general_boxes.json bodies: s.B is a knot (alex.diagram), so one through arc, no closed component;
  eps = b(-1) = (-1)^n0 50/50; two raw closures (m=0,-1) reproduce the stored vector up to one common unit 50/50.
  Scalar states: bodies 6 (b = t^-3 a, n0=1), 25 (b=a), 35 (b=a), 44 (b=a). engineA's "3 scalar bodies" counts
  classes mod Y (6 = 25 mod Y; a = J_3(trefoil)). All four are outside engineA NONRAT; node() also rejects scalar products.
- r3_rawunits.py: lp drawn-tangle unit u = y + delta x is identically 1 (all horizontal/vertical closures tried);
  raw closures alpha_m(B) = t^(2m) c(B) e1^T X^-m v(B), U_m = t^(2m) universal, c(B) m-independent, m = -3..3: 50/50.
  => Prop 3.9 (two raw closures fix v) is now a consequence of (7.2) in one raw marking, not just CHECKED.
- r3_vertical.py: J_raw(s.l1.B.(x2)^a.u1) = t^(-2a) c(B) F_a(a,b), F_a from (8.4), SAME c(B) as horizontal,
  a in {+-1,+-3,+-5}: 50/50 (incl. scalar and eps=-1 bodies). F_1(I)=t^4, F_-1(I)=t^-4 as stated.
- r3_trees.py: 70 random trees (depth <= 2, nested F_m, products, rational leaves, all 50 general bodies; 24 trees contain
  scalar bodies): calculus (Norm, Theorems N/O/V) == lp.J of the explicit halfword, horizontal 70/70, vertical 70/70;
  the Theorem O unit assertion in vc.F never failed.
- r3_rootraw.py: in lp's RAW marking a_raw(-1) = 1 and b_raw(-1) = (-1)^n0 on 177/177 bodies (50 general + 127 random);
  raw v2 always integral. Consistent with (6.2) and Section 5.

## Findings
F1 (SOUND) Every body these theorems quantify over is an actual body in the note's sense: rational B(w), (y0)^N, nested
   r2.(y1)^m.p.u1 (one through arc for both parities of m), products, the 14 NONRAT general bodies, d2pos boxes (halfwords
   via vc.word). Straight axis and the Section 2 marking are those of the doubled half-diagram (flat_search.quotient_word).
F2 (SOUND, scope) Section 6 is OFF the critical path of every non-flatness theorem: all of them are invariant under one
   common unit (jets, delta, sigma, lc ratios, Lemma W windows), and engine vectors are computed by Norm (vc.F asserts the
   t^(2m(1-eps)) exponent only as a check). Without Section 6, Theorem O still reads v_outer = (-t)^(-4m p2(-1)) X^-m p.
   Section 6 is needed only for the displayed exponent of Theorem O and the dichotomy statement itself.
F3 (GAP, repairable) M300's "ANY eligible box whose order-2 jet signature lies in S ... n >= 0" is not covered by the
   signature alone when n = 0: refGen's precondition Tot = span S1 - 2 >= 3 (span A >= 5) is not implied by eligibility
   (span a >= 1). True for the 27,585 listed boxes (span a >= 10) and the d2pos boxes (span a >= 12). Restrict the n = 0 part
   to listed boxes or add sum span a(B_j) >= 5. Same caveat for any signature-level reading of C1's n = 0 pair theorem and D36.
F4 (GAP, known) Branch-knot corollaries in C1 sec.2 / lpgen sec.3 ("V(L_n) != 1 for every n"): odd n needs J != J_*(n, n a2);
   automatic only when a2(K) = 0 (refV3). Note sec.9 states this correctly.
F5 (GAP, wording) C1 "every depth-one arborescent quotient ... closed by theorem" holds only with its parenthetical: pure
   twist X^mu Y^N horizontal (Montesinos with even tangle 1/(2m)) and vertical (x2)^a closures (integral swapped columns),
   n >= 1 (n >= 2 horizontal and a = +-1), vertical n = 0 excluded. Not covered: general even special tangles (single-child
   closures, open in M300/C1), dihedral inversions with non-integral swapped tangles, r >= 4 dihedral patterns (nest 5.6).
F6 (SOUND) Scalar/local-knot bodies and swap sums need no restriction. They satisfy the hypotheses; Theorem V now uses only
   the identity-body bubble (planar left half-disc), not Corollary S. For a local-knot body a = J_3(K'), so the eligibility
   span a >= 1 already means J_3(K') != 1: no J_3-detection claim is imported into signature theorems. Corollary S holds
   for every swap inversion (axis lies in the invariant sphere; fixed points = K n S), exactly, since zero-framed J_3 is
   already = 1 mod (t+1)^2 (Habiro: (q^4;q)_k (q^-2;q)_k has a double zero at q = -1).
F7 Note sec.9: no overstatement found. Minor: sec.1 "precisely the actual bodies used in the halfword grammar" asserts an
   unproved converse (every marked ball is a halfword body); no proof uses it.

## Per-theorem status after the note (modulo R1/R2 on Sections 2-5, 7-8)
- Theorem N: proof for arbitrary actual bodies, pure special region C_m (inputs 2-4, 7). Section 6 not used.
- Theorem O: proportionality v_outer ~ X^-m p is a proof (Section 7); displayed unit t^(2m(1-eps)) needs Section 6.
- Theorem V: proof for every actual body, all odd a, one raw marking (Section 8 + 2-4).
- Corollary S: proof for all swap inversions (Sections 2-3 + bubble); not an input to the theorems below.
- Q-MONT: end-to-end proof. Hyp: s.r2.(y1)^m.Y^N.B_1...B_n.u1, m != 0, n >= 2 actual bodies with non-integral rational
  vectors; knot scope horizontal inversions of N(T_1+...+T_n+1/(2m)), odd q_i (Lemma L). Own status TRUSTED.
- V3: end-to-end proof (refV3 SOUND). Hyp: s.l1.Y^N u_1..u_n.(x2)^a.u1, a odd, u_i non-integral rational, n >= 1
  (|a| >= 3), n >= 2 (a = +-1, via wV(+-1) = t^(+-3) w_3(+-1) and Q-MONT); n = 0 excluded (CHECKED only).
- C1 V3(B)/H(B)/BOTH (46,771) and top-300 pairs: end-to-end proof (refGen SOUND) for the LISTED boxes, n >= 1 (single) /
  n >= 0 (pairs, span a >= 10), every mu != 0, every odd a. General-body vectors certified by (7.2) + exact lp.
- M300 / D36: dictionary input now supplied; still pending their own referee; n = 0 needs F3's span precondition off-library.
- All: conclusion is J != 1; V(L_n) != 1 for all even n, and for odd n only with a2 = 0 or J != J_*.
