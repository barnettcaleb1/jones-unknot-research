# REFEREE (lens ALGEBRA) -- finite_index_pattern_rigidity.md

15 November 2026. Adversarial read of the exact-algebra content of
`work/theory_restart/finite_index_pattern_rigidity.md` (Theorems A, B and the element E),
with `pattern_symmetry_dichotomy.md` and `global_design/two_box_signed_square.md` as inputs.
Everything below was re-derived (by hand and by exact sympy / exact Z[zeta_8] arithmetic);
scripts and outputs are in this folder (`check1..5_*.py`, `*.out`).

## Verdict

**CONFIRMED WITH CORRECTIONS (all corrections cosmetic or strengthening; nothing in this lens breaks).**

Out of scope of this lens and NOT refereed here: Section 4 of the text (Gamma_n = Delta(2,3,n),
Comm^+ of the nonarithmetic triangle group, the Jorgensen--Klein step) and the written proof of
the signed-square theorem itself (I only probed its sign rule by brute force, item 6). Theorem A
therefore stands or falls with the kleinian lens; Theorem B additionally with the signed-square lens.

## 1. The element E  (check1)

Exact, over Q(A), with delta = -A^2 - A^-2:

- E^2 = (delta^2-1) I;  E* G E = (delta^2-1) G;  E J E^-1 = -J;  E M E^-1 = -A^-2 J M^-1 J.  All four TRUE.
- Also G E = (delta^2-1) diag(1,-1), det E = 1-delta^2, E (JM) E^-1 = A^-2 (JM)^-1, and the background
  facts M* G M = G, J* G J = G, bar(M) = M^-1, J^2 = I, (A J M)^3 = -I, det M = -A^-2.
- Hence [E] Gamma [E]^-1 = Gamma (generators go to scalar multiples of elements of Gamma; [E]^2 = 1).

**[E] is not in Gamma.** Three independent proofs, all checked:
1. (Text's proof.) [E] centralizes [J]; E is proportional to neither I nor J; the centralizer of the
   order-2 generator is <[J]>. I verified the centralizer claim directly in the zeta_8 gauge instead of
   citing free-product theory: g S0 = +S0 g forces g = [[e,-c],[c,e]], det = c^2+e^2 = 1, so g = +-I, +-S0;
   g S0 = -S0 g forces det = -(c^2+e^2) < 0. (check4)
2. (Text's "equivalently".) Conjugation by E fixes [J] and inverts [JM]; an inner automorphism acts
   trivially on the abelianization C_2 x C_3, inversion on C_3 does not.
3. (New, shortest.) det E = -(A^2-A+1)(A^2+A+1)(A^4-A^2+1)/A^4 has nontrivial squarefree part, while every
   bare word has determinant +-A^(2k). So E is not a K-scalar multiple of any bare word:
   the class of det in K*/K*^2 separates the two cosets. (check3)

**The induced automorphism.** At A_0 = exp(pi i/4), with D = diag(1,i):
D^-1 M D = A_0 [[1,0],[-1,1]],  D^-1 J D = i [[0,1],[-1,0]],  D^-1 E D = i [[0,1],[1,0]]  (exact; check1).
So E-conjugation is conjugation by X = [[0,1],[1,0]] in PGL_2(Z), det X = -1: S0 -> -S0, T' -> X T' X = [[1,-1],[0,1]]
= S0 T'^-1 S0^-1, matching E M E^-1 ~ J M^-1 J. It is the nontrivial class of Out(PSL_2(Z)) = C_2
(reflection of the upper half-plane in the unit circle, fixing i). Answer to the lens question: YES.
"Determinant -1" is meaningful: two nonzero real matrices that are complex-proportional are real-proportional,
so the sign of the determinant of the real normal form is an invariant of the projective class. Equivalently, in the
gauge D* G_0 D = i [[0,1],[-1,0]], so every real L is a similitude with multiplier det L: the sign of the multiplier
at zeta_8 is the sign of det L (E: multiplier delta^2-1 = -1 there).

Triangle data: delta(A_n) = -2 sin(pi/n) exactly; eigenvalue ratio of M(A_n) is exp(-2 pi i/n) (principal). (check1)

## 2. "S then normalizes Gamma, so there are no intermediate finite-index intersections"

Given Theorem A this is immediate ([S] in Gamma^ext and Gamma^ext normalizes Gamma, so the intersection is Gamma).
Independent of Theorem A, I checked the index-one case outright:

**Proposition (unconditional).** N_{PGL_2(K)}(Gamma) = Gamma^ext = Gamma x| <[E]>, with no similitude hypothesis.
Proof. If [X] centralizes Gamma projectively then X J X^-1 = s1 J, X M X^-1 = s2 M with s1^2 = 1 (square) and
s2^2 = 1 (determinant). Solving the four linear systems exactly: (+,+) gives X scalar; the other three give X = 0
(tr M = A - A^-3 != 0 kills s2 = -1). So the normalizer injects into Aut(PSL_2(Z)) = PGL_2(Z), in which
Inn = PSL_2(Z) has index 2; E realizes the outer class. (check3; Aut(PSL_2(Z)) = PGL_2(Z) is classical, see Sources.)
This is consistent with Theorem A and shows Gamma^ext cannot be enlarged or shrunk.

## 3. Specialization and normal forms at zeta_8  (check2: 60 random words, 3 placements, exact in Q(zeta_8))

- Every bare word W: D^-1 W(zeta) D = scalar x L, L in SL_2(Z).  TRUE in all cases.
- W E and E W: scalar x integral matrix of determinant -1.  TRUE in all cases.
- With D^-1 S_0 D = v L, L = [[a,b],[c,d]]:  C(zeta) = G_0 S_0 = v [[i c, d],[a, -i b]].  TRUE (G_0 = [[0,1],[1,0]]).
- det C(zeta) = v^2 (bc - ad) = -det(L) v^2. Hence, for every nonzero entry,

      det C / C_ij^2 = det(L) (-1)^(i+j) / x^2,    x = c, d, a, b for (i,j) = 00, 01, 10, 11  (0/1 corner labels).

  Inner coset (det L = +1): sign (-1)^(i+j) -- exactly the signed-square rule.
  Outer coset (det L = -1): sign -(-1)^(i+j) at EVERY nonzero anchor. 540 anchor evaluations, no exception.
- For the text's anchor: corner11 in the 0/1 labelling is the lower-right entry -i b v, so b != 0 and the ratio is
  -1/b^2 < 0.  CONFIRMED.

**Correction C1 (notation).** The same section writes f = (C W^-1)_12, which is 1-based matrix indexing; under
1-based indexing "C_11" would be the upper-left entry i c v, and the correct statement would be "c != 0,
ratio -1/c^2". The text's "b" is right only with the 0/1 corner labels of two_box_signed_square.md. The conclusion
is unaffected (negative either way; both diagonal anchors carry the same sign), but the text should say explicitly
that corner11 = lower-right entry, or write (C W^-1)_01.

**The scalar v.** C = f G W E^eps with G W E^eps in GL_2(O) (determinants -1, unit, 1 at zeta), so f = entry of
C (G W E)^-1 lies in O, and f(zeta) != 0 iff C(zeta) != 0. CONFIRMED as argued in the text.

**Remark R1 (strengthening).** Because the outer coset has the wrong sign at every nonzero anchor, moving the seed to
corner11 is needed only if one insists on the |C_11| = 1 form of the signed-square theorem. With the "nonzero anchor
of arbitrary determinant" form, the outer coset is excluded as soon as C(zeta_8) != 0, i.e. as soon as SOME rational
closure has nonzero determinant; the unit seed is used only for f = +-A^m. (rigidity_algebra_read.md Section 4 already
says this; the main text does not.)

**Remark R2.** Since E = (delta^2-1) G^-1 diag(1,-1), the outer coset of tensors is exactly {f diag(1,-1) W}: the
rational-gluing tensors with the Gram form G replaced by diag(1,-1).

Transport: G^-1 P^T C Q = bar(P)^-1 S Q identically (check4), bar(Gamma) = Gamma, E Gamma = Gamma E, bar(E) = E, so
boundary operations and the bar in the dichotomy's first projection preserve both cosets and the similitude property.
M is the exact raw-bracket matrix of adding one crossing (e_1 -> A e_1 + A^-1 e_2, e_2 -> (A + A^-1 delta) e_2 = -A^-3 e_2),
so P^T C Q is again the tensor of an actual two-box diagram: the transported tensor is a legitimate input to the
signed-square theorem.

## 4. The DVR argument at Phi_8 = A^4+1

Re-derived; CONFIRMED.
- bar preserves the prime: Phi_8(A^-1) = A^-4 Phi_8(A). Residue field Q(zeta_8).
- h S = alpha S k with bare h,k: alpha^2 = det h / det k. **Strengthening:** bare determinants are +-A^(2j) and neither
  -1 nor A is a square in Q(A), so alpha = +-A^j is a Laurent unit, not merely a Phi_8-unit. The relations therefore
  specialize at every A where S is regular and invertible, which is what Section 4 of the text uses at A_n.
- If S_0 had rank one, l = im S_0 satisfies h_0 l = S_0 k_0 (K^2) = l (k_0 invertible). Specialization is faithful on
  Gamma_proj (C_2*C_3 -> Gamma_proj -> PSL_2(Z) is an isomorphism), so H_0 has finite index and contains
  T'^N = [[1,0],[-N,1]] and S0 T'^N S0^-1 = [[1,N],[0,1]], whose unique invariant lines are e_2 and e_1 (check4).
  No common line over any field of characteristic 0. Contradiction; S_0 is invertible.
- c_0 != 0: c^2 = det(S) bar(det S) with both factors units of O.
- The similitude hypothesis is not used in this step.
- Limitation worth recording: this step gives good reduction only. At zeta_8 alone the hypotheses put S_0 in the
  commensurator of PSL_2(Z), which is PGL_2(Q) (Hecke elements), far larger than PGL_2(Z). The algebra at zeta_8
  does NOT prove Theorem A; the whole weight is on the discreteness input from the triangle specializations and the
  algebraic-limit step (kleinian lens).

## 5. The integrality step

CONFIRMED. W bare, det W = +-A^(2k), so W^-1 in Mat_2(R); C W^-1 = f G and G has off-diagonal entry 1, so
f = (C W^-1)_offdiag in R. With integral seed vectors, u = f (v^T G W w), both factors in R, u a unit of
R = Z[A,A^-1], hence f = +-A^m. Undoing the seed move: C = P^-T C' Q^-1 = f G bar(P) W' Q^-1, again f times G times a
bare word, same f. Tested with f = -A^5, A^2+1, A^2-A+1: the off-diagonal entry recovers f and every rational seed
bracket is divisible by f (check3). The reduced (not absolute) bracket is required, as the text says.

## 6. Brute-force probe of the signed-square sign rule  (check5; supplementary, outside this lens' brief)

228 random braid closures (3-5 strands, 6-11 crossings) with two crossings used as the two boxes
(generally non-rational patterns); exact tensors in Z[zeta_8] by state sum. For all 674 nonzero anchors,
det C(zeta)/C_ij(zeta)^2 is rational, a rational square in absolute value, of sign (-1)^(i+j) or zero; for the 295
unit-modulus anchors it is an integer. No violation. Together with item 3 (the full inner coset, which consists of
actual diagrams, obeys the same rule) this corroborates the sign that excludes the outer coset. It is evidence,
not a proof; the written proof belongs to the signed-square lens.

## 7. Dichotomy inputs used by Theorem B

Re-derived: P^-T = G bar(P) G^-1; Q = u S^-1 bar(P) S; a finite-index subgroup of PSL_2(Z) is not cyclic, so Z_C is
scalar and S* G S = cG with bar(c) = c (H_C and G are Hermitian). The first projection is
Gamma cap [bar S] Gamma [bar S]^-1; bar is an automorphism of Gamma fixing E, so Theorem A applies. Index-one sanity:
for C = diag(1,-1), J^T C J = -C and M^T C (J M J) = -A^-2 C (check4).

## What would settle the parts not decided here

- Theorem A: exact hypotheses of the commensurator statement for Delta(2,3,n) (n > 30, nonarithmetic, maximal) and of
  Jorgensen--Klein for the 4-generator groups <J_n, M_n, E_n, S_n> in PGL_2(C).
- Theorem B: the signed-square proof for the transported diagram (connectivity of the completed projection, common
  framing). The algebraic interface to it (item 3) is exact.

## Sources

- Aut(PSL_2(Z)) = PGL_2(Z), Out = C_2 (used only in my Proposition of item 2, not in the text under review):
  stated in https://arxiv.org/pdf/1605.03717 and https://arxiv.org/pdf/1711.09209 . Not traced to a primary proof in
  this pass. (Hua--Reiner 1952 concerns PGL_n(Z); their n = 2 claim about Aut(PGL_2(Z)) was corrected by Dyer 1978 and is
  not what is used here.)
- All other facts used in this lens were proved directly above; no published theorem is relied on.
