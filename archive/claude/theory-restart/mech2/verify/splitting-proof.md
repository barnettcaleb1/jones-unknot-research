# Referee notes: THEOREM A and THEOREM B of colored/REPORT.md (sections 0.1, 2, 3)

Referee: independent proof referee (Claude), 16 November 2026.  Notes are appended as I go; the VERDICT section is at the end of the file.
Target: /Users/calebbarnett/jones-lanes/theory-restart/mech2/colored/REPORT.md, sections 0.1, 2, 3.
Scripts and kht++ working folders: /Users/calebbarnett/jones-lanes/theory-restart/mech2/verify/splitting-proof/ .
Marks used below: OK = I verified the step myself; CORR = true after a correction (stated); GAP = I could not verify; WRONG = false as stated.

## 0. What I read
- BRIEF2.md (whole), notes/2026-11-15b-sutured-side.md (whole), REPORT.md sections 0.1, 0.4, 2, 3 (whole).
- Batson-Seed, arXiv:1303.6240v1 (25 Mar 2013): read sections 1, 2, 3, 4, 5 (through Theorem 1.2) and 6 completely, from the text copy
  saved by the report's author at colored/lit/bs/bs.txt (pdftotext of the arXiv PDF; I did not re-download; I will spot-check the copy
  against arXiv if a statement is in doubt).  Figures are not in the text copy; where a figure matters I say so.

## 1. Which statements of Batson-Seed (BS) are used, and whether BS state them with marked points
(Statement numbers as in arXiv v1.)
| used in | BS statement | content | stated with marked points in BS? |
|---|---|---|---|
| A(1) | section 2.2, displayed formula for d_1 (two components, F_2) and items (1),(2) | d = d_0 + d_1, d_1 = sum of backward edge maps over mixed edges; d raises l by 1, d_1 lowers g = (q-m)/2 by 1; g-filtration, E_1 = H(C,d_0) | no marked points needed |
| A(1) | Prop. 2.2 | d^2 = 0 (proof: Case 2 uses A(J_i,I)A(I,J_i) = X_{p_i} + X_{q_i} and the sign assignment; over F_2 with two components no signs) | marked points appear only as a device in the proof |
| A(2) | section 2.1 (last paragraph) and Prop. 6.3 | X_p is defined on C(D) for a point p away from the double points; "dX_p = X_p d" for the total differential | YES, stated exactly for marked points |
| A(3) | section 2.2 item (3) and the sentence "d is manifestly unchanged if we swap a mixed crossing"; Prop. 2.3 | crossing change between components gives an isomorphism of relatively l-graded complexes | Prop. 2.3: NO.  The compatibility with X_p is only asserted inside the proof of Prop. 6.5 ("C(D,w) and C(D',w) differ only by rescaling generators ... The action of X_c^p commutes with rescaling generators") |
| A(5) | Lemma 3.1, Prop. 3.2 | cancellation lemma; R1, R2, R3 give l-graded, q-filtered chain homotopy equivalences | NO.  Prop. 3.2 has no marked points.  The only marked-point statement is one unproved sentence in the proof of Prop. 6.5: "The total homology and A_m action are also invariant under Reidemeister and marked point moves" - a statement about the MODULE structure on homology, not about the subcomplex X_1X_2 C |
| A(6) | Thm. 3.3, Cor. 3.4 | total homology = Kh of the split union; l-shift t = sum 2 lk | no marked points |
So: the pointed statements that Theorem A needs beyond BS are (a) X-equivariance of the crossing-change identification (trivial over F_2),
and (b) chain-level X_p-equivariance of the maps f, g, h in BS's proof of Prop. 3.2 for p outside the disc of the move.  (b) is NOT in BS;
the report proves it itself in step (5).  It must be checked here, not cited.  (Checked in section 3 below.)
Note also: the homology of the subcomplex X_1X_2 C is not a function of the A_m-module H(C), so BS Prop. 6.5 could not be used as a
substitute; the report does not try to, which is correct.

## 2. Section 0.1 (N(T) = H(X_1X_2 CKh(D), d_Kh))   -- OK
Checked by hand:
(a) Let gamma be the arc crossing the two closing arcs at p_1, p_2 (the cut of the annulus).  A circle of a resolution through exactly one of
    p_1, p_2 meets gamma once, so it is essential; a circle through both meets gamma twice, so it is inessential.  Hence
    "p_1, p_2 on different circles" <=> "two essential circles", and "p_1, p_2 on the same circle" <=> "no essential circle".
(b) On a state of the first kind X_1X_2 = multiplication by x_{c1} x_{c2}: image = span of the monomials divisible by x_{c1} x_{c2}.
    On a state of the second kind X_1X_2 = x_c^2 = 0.  So X_1X_2 C is spanned by labelled states (it is a homogeneous subspace), namely
    exactly the generators of annular weight -2.  States with both points on one circle contribute NOTHING to X_1X_2 C, and the components
    of d_Kh from X_1X_2 C into such states vanish (the only such edge merges the two marked circles: x.x = 0).
(c) Every merge/split map is non-increasing in the annular weight k (checked case by case: e.g. v_+ (x) v_+ -> w_+ lowers k by 2, w_- -> v_- (x) v_-
    lowers k by 2, v_+ -> v_- (x) w_+ lowers k by 2, the others preserve k).  So weight -2 is a subcomplex of (CKh, d_Kh) on which d_Kh equals
    the annular differential (there is nothing below weight -2 to drop into).  The same holds for BACKWARD saddles, so it is also a
    subcomplex for the Batson-Seed differential (used in section 2).
(d) weight -2 = weight +2 up to a q-shift by 4: the annular differential is symmetric under v_+ <-> v_- on essential circles (all six
    annular edge maps are), over any ring.
(e) weight (-2) = N(T): in the reduced Bar-Natan type D structure over B a generator of idempotent b contributes End_B(b) = F[H]<1, D> to
    the complex of T(0), the generator "D" is the labelled state with both essential circles labelled x, and post-composition with an arrow
    label a in End(b) or Hom(b,c) kills it unless a = id (D.D = HD -> 0 at H = 0, S^2 D = 0, S D = 0).  So the subcomplex spanned by the "D"
    generators is F_b C(T), with bigrading shifted by deg D = (0,-2).  (This is BRIEF2 (b); it is a premise of the report, I re-derived it.)
Checked by machine (my own program khsplit.py, written from scratch: Morse word -> cube of resolutions -> the subcomplex X_1X_2 C over F_2):
   t_kht_compare.py: for 15 tangles (quotient tangles of 3_1, 4_1 inversions 1 and 2 in kht++'s explicit form, and 12 random 1-3 tangle
   words with two-component closure, dim N = 1, 3, 5) the bigraded multiset of b-generators of kht++'s BN~ equals
   H(X_1X_2 CKh(T(0)), d_0) up to one overall shift ((0,-2) or (2,4) according to the orientation kht++ picks): 15 of 15.
Remarks on 0.1:
 - "weight -2 (isomorphic to weight +2)" is right; "N(T sigma^n) = N(T) up to shift" is right (a state with sigma resolved the other way
   has no essential circle).
 - CORR (wording): the statement needs D to be an ANNULAR diagram: there must be an arc on the sphere from p_1 to p_2 meeting D only at its
   endpoints (then put the axis points on its two extensions).  For the 2-cable of "ANY diagram of K" with p_1, p_2 two parallel points
   this holds.  It is exactly this adjacency that is used again in step (4) of Theorem A.
