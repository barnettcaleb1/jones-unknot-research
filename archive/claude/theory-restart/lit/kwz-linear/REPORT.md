# Digest: Kotelskiy–Watson–Zibrowius, "Khovanov multicurves are linear" (arXiv:2202.01460)

Status: COMPLETE (2026-11-15).

Sources read
- [KWZ-lin] arXiv:2202.01460v1 (3 Feb 2022; the only arXiv version; 41 pp.; arXiv comment: "The contents of this paper used to be part of arXiv:2105.06308"). No journal version found. TeX in `src/tex/`, PDF `src/kwz-linear.pdf`. Page numbers = PDF pages of v1.
- [KWZ-mut] arXiv:2602.23442v1 (26 Feb 2026; 85 pp.), same authors, "On mutation invariance in Khovanov homology". Its introduction (p. 1) calls [KWZ-lin] "an earlier, unpublished version" of its multicurve part, valid over F_2, and redoes everything over arbitrary fields. Consulted only for status, field of definition, and conventions. TeX in `src/mut2026/tex/`.
- My own computations (F_2, exact linear algebra): `calc/hf.py`, `calc/run1..5.py`, outputs `calc/out_*.txt`. Everything in Sections 9 and 12, and the formulas under C3 in Section 10, are DERIVED by me unless a location is given.

## 0. Bottom line

1. [KWZ-lin] is about Kh~(T) only and works over F = F_2 throughout (p. 2). Thm 2.14 (p. 7): every component of Kh~(T) is linear. Thm 2.15 (p. 7): every component is r_n(p/q) or s_2n(p/q), n >= 1, with trivial local system. [KWZ-mut] Thm 3.19 = Theorem B (p. 19) gives the same classification over any field (local system (-1) in GL_1 by their sign convention), up to an overall bigrading shift.
2. For BN~(T) the only geography statement is Thm 4.1 (p. 10): no component of BN~(T) or Kh~(T) wraps around the special puncture. Compact components of BN~ are NOT classified: they may wrap around non-special punctures (Remark 5.3 and Fig. 15, pp. 32-33, tangle T_CKMC) and may carry non-trivial local systems ([KWZ-mut] Remark 3.20, p. 19: a 2-dimensional indecomposable local system over Z/7). Claim C1 is false for BN~.
3. The paper contains no statement about Euler characteristics, the Jones polynomial, or K_0 classes, and no constraint on relative bigradings between different components. The only grading facts are a q-parity statement and the mirror statement (Section 5 below).
4. Derived: the linear curves disjoint from a(infty) are exactly those carried by the special line of slope infty; among components of Kh~ these are the s_2n(infty). For m, n >= 1, HF(a(1/n), s_2m(infty)) has dimension 2mn, sits in one delta-grading (computed for m <= 5, n <= 10), and has Euler characteristic +-q^c (1 - q^6)(1 + q^4 + ... + q^{4m-4})(1 - q^2 + ... + (-q^2)^{n-1}), never identically zero; nothing qualitative depends on the parity of n. Each r_n and s_2n has non-zero K_0 class, but cancellation between different special components is not excluded by anything in the source.

## 1. Conventions of the paper

- Pointed Conway tangle T: one distinguished ("special") end *, drawn top-left. S^2_{4,*} = boundary sphere minus the four ends (p. 2).
- Algebra B (eq. (1), p. 3): quiver with vertices bullet, circ; arrows D_bullet, D_circ (loops), S (both ways); relations DS = 0 = SD. bullet <-> crossingless tangle with the two top ends joined (special end joined to top-right; this is Q_0), circ <-> the one with the two left ends joined (Q_infty) (p. 3). H = D + S^2 is central.
- Bigrading: gr(D) = q^{-2} delta^{-1}, gr(S) = q^{-1} delta^{-1/2}; differentials preserve q and lower delta by 1 (p. 3). h = q/2 - delta (Def. 4.3, p. 11). So D, S have h = 0 and the differential has h-degree +1.
- DD(T) = Bar-Natan's delooped complex as a type D structure over B; DD_1(T) = [q^{-1} delta^{1/2} DD(T) --H.id--> q^{1} delta^{1/2} DD(T)] (p. 3). BN~(T), Kh~(T) = multicurves of DD(T), DD_1(T) under the classification [KWZ19, Thm 1.5]; DD^c, DD^c_1 denote representatives in "curve form".
- Compact curve = immersed circle, primitive in pi_1, with a local system in GL_n(F) up to conjugacy; non-compact curve = immersed interval with both ends on non-special punctures, trivial local system (p. 2). Kh~(T) has only compact components; BN~(T) has exactly 2^{|T|} non-compact ones, |T| = number of closed components (p. 4).
- Field: F_2 "exclusively" (p. 2). The construction needs a field (Remark 2.1, p. 4).
- Naturality (Thm 2.2, p. 4): Kh~(tau(T)) = tau(Kh~(T)), BN~(tau(T)) = tau(BN~(T)) for tau in Mod(S^2_4); "This assumes that we work over F [KWZ19, Thm 1.13], but we expect the same to hold over arbitrary fields" (p. 4). Now [KWZ-mut] Thm 3.6 / Cor. 3.7 (pp. 15-16) over any field.
- Gluing (Thm 2.8, p. 5, = [KWZ19, Thm 1.9]): for L = T_1 u T_2, Kh~(L) (x) V = HF(Kh~(T_1^*), Kh~(T_2)) and Kh~(L) = HF(Kh~(T_1^*), BN~(T_2)) as relatively bigraded spaces, V = delta^{1/2} q F + delta^{1/2} q^{-1} F, T^* = mirror with reversed orientation. [KWZ-mut] Thm 2.40 (p. 12) states this absolutely bigraded: Kh~(L) = HF(-Kh~(T_1), BN~(T_2)) = HF(-BN~(T_1), Kh~(T_2)).
- HF(gamma, gamma') = H_*(Mor(C(gamma), C(gamma'))) ([KWZ-mut] Thm 2.38, p. 12); a morphism x -> y (x) b has grading gr(y) + gr(b) - gr(x).
- Slopes. Planar cover R^2 \ Z^2 -> T^2 \ 4pt -> S^2 \ 4pt (p. 1). Mod(S^2_{4,*}) = PSL(2,Z); the curve of slope p/q is the image of the slope-0 curve under [[q, r],[p, s]], qs - pr = 1, which sends lines of slope 0 to lines of slope p/q (p. 7). In the figures slope is the usual visual slope (Fig. 2e: the "rational curve of slope 1/2" rises to the right). [KWZ-mut] Lemma 3.2 (p. 14): psi(tau_bullet) = [[1,0],[-1,1]], psi(tau_circ) = [[1,1],[0,1]]; Def. 3.15: Q_{p/q} = tau_{p/q}(Q_0).
- Coordinates I use for the cover (consistent with Figs. 2, 4, 15): lifts of * = (2Z)^2; lifts of the top-right end = (odd, even); bottom-left end = (even, odd); bottom-right end = (odd, odd). Deck group = 2Z^2 semidirect {+-1}. Lines of slope p/q through lattice points come in two kinds: "special lines" (through lifts of * and of the end = (q,p) mod 2) and "non-special lines" (through lifts of the other two ends, alternating).
- Reading a type D structure from a curve (Fig. 1, p. 3; Fig. 15 inset, p. 33): generators in idempotent circ are the intersections with the parametrising arc enclosing the top-right end (in the cover: the boundary of the horizontal grey bands along special rows); idempotent bullet: the arc enclosing the bottom-left end (vertical bands). A curve segment crossing a face gives an arrow in the direction that runs counterclockwise around the puncture of that face; D_circ winds around the top-right end, D_bullet around the bottom-left end, S^2 around the bottom-right end, and nothing winds around *.
- Arcs (Example 2.5, p. 5): BN~(Q_s) = a(s) is the single arc obtained by pushing the strand not ending at * onto the sphere; Kh~(Q_s) is a figure-eight curve in a neighbourhood of it (this is r_1(s)). a(0) = [bullet], a(infty) = [circ]. a(p/q) joins: bottom-left and bottom-right if p even; top-right and bottom-left if p, q odd; top-right and bottom-right if q even (table on p. 35, stated there for r_d(p/q)).
- DERIVED from the Fig. 15 rule and checked against the twisting table of [KWZ-mut] (Table 1, p. 15, with the recipe on p. 14: cases (a), (d) and the rule for bullet --S--> circ): a(1) = [circ --S--> bullet]; a(1/n) = [circ --S--> bullet --D--> bullet --S^2--> bullet --D--> ...] (n bullets), which for n = 3 is the complex of Fig. 1a; a(-n) = [bullet --S--> circ --D--> circ --S^2--> ...] (n circs); a(-1/n), a(n): all arrows reversed. Rotation rho by 90 degrees (slope s -> -1/s) swaps bullet and circ ([KWZ-mut] Prop. 3.10, p. 16).

## 2. Definitions: linear curves, r_n(p/q), s_2n(p/q)

Peg-board representatives (Def. 2.11, p. 6). With the flat metric induced from R^2 \ Z^2 and 0 < eps < 1/2, an eps-peg-board representative of a closed curve gamma is a shortest representative of its homotopy class staying at distance eps from all four punctures. The limit eps -> 0 of a connected infinite lift is the singular peg-board representative, a piecewise linear curve, unique up to deck transformations (p. 6). Only curves with no embedded representative are considered (justified by Prop. 2.7).

Wrapping and linearity (p. 6, unnumbered, between Def. 2.11 and Def. 2.12). gamma wraps around a puncture if there are alpha > 0 and delta_0 > 0 such that for all 0 < eps < delta_0 the eps-peg-board representative of the lift changes direction at a lift of that puncture by an angle >= alpha. gamma is linear if it wraps around no puncture. A linear curve has its singular peg-board representative in a single line; the converse fails because of k*pi-turns around punctures.

Rational versus special (Def. 2.12, p. 7). A linear curve is special if its singular peg-board representative contains the lift of *, and rational otherwise. ([KWZ-mut] Def. 7.3, p. 36, renames these classes "almost special" / "almost rational" and reserves "special" / "rational" for the families s_2n, r_n.)

Equivalent concrete picture (derived from the definitions). A linear curve of slope p/q is a closed curve whose lift runs in a thin neighbourhood of one lattice line of slope p/q and passes each puncture on that line on one side or the other, in a periodic pattern; it is special or rational according to whether that line is a special or a non-special line. The pattern with no side change is the embedded curve and is excluded.

The families (p. 7, Fig. 4d; TeX source of the figure confirms the counts). Lengths: n for r_n, 2n for s_2n.
- s~_2n(0): runs along a horizontal special line (punctures alternate *, top-right end, *, ...). It passes below 2n consecutive punctures, crosses the line, passes above the next 2n consecutive punctures, and crosses back; the lift is invariant under translation by 4n. Closed, immersed, not embedded. s_2(0) is the figure-eight around * and the top-right end (Fig. 4a).
- r~_n(0): runs along a horizontal non-special line (punctures alternate bottom-left end, bottom-right end). It passes below n consecutive punctures, then above the next n; invariant under translation by 2n. r_1(0) is the figure-eight around the two bottom ends, r_1(0) = Kh~(Q_0).
- r_n(p/q), s_2n(p/q): images under [[q, r],[p, s]]. So s_2n(p/q) is carried by the special line of slope p/q, and r_n(p/q) by the non-special line of slope p/q (whose punctures are the two ends that a(p/q) joins).
- Local systems: "defined to be trivial" (p. 7). In [KWZ-mut] Def. 3.11 (p. 16) they are (-1) in GL_1(R), a sign convention.
- Both curves are invariant under the reflection in their line (the two patterns differ by a deck translation), so as ungraded curves m(r_n(p/q)) = r_n(-p/q), m(s_2n(p/q)) = s_2n(-p/q) (derived).

Type D structures (slope 0).
- r_n(0) (Lemma 5.5, p. 33): 2n generators, all in bullet; one source, one sink, joined by two directed chains of n arrows each, labelled alternately D, S^2, ... and S^2, D, .... r_1(0) = [bullet ==> bullet] with labels D and S^2, i.e. the cone of H on [bullet].
- s_2n(0) (proof of Thm 5.1, p. 30): 4n generators in bullet and 4 in circ. Two rows circ --S--> bullet --D--> bullet --S^2--> ... --D--> bullet --S--> circ (2n bullets each), plus arrows D from the first circ of row 1 to the first circ of row 2 and from the last circ of row 1 to the last circ of row 2. (The first display on p. 30 labels the last arrow of row 2 by D; this is a misprint for S, cf. the second display and [KWZ-mut] Def. 3.12.)
- Absolute gradings fixed in [KWZ-mut] Def. 3.12 (p. 17), written q^s h^t: C(a(0)) = [bullet at q^0 h^0]; C(r_n(0)): source at q^{-n} h^{-n}, sink at q^{n} h^{0}; C(s_2n(0)): the four circ generators at q^{-2n-1} h^{-n-1}, q^{1-2n} h^{-n}, q^{2n-1} h^{n}, q^{2n+1} h^{n+1}. Every arrow raises h by 1 and raises q by 2 (D, S^2) or 1 (S).
- [KWZ-mut] Lemma 4.6 (p. 21): C(s_2n(p/q)) has max(2, 2n|q|) arrows D_bullet and max(2, 2n|p|) arrows D_circ; C(r_n(p/q)) has n|q| arrows D_bullet and n|p| arrows D_circ.

## 3. Main theorems of [KWZ-lin]

- Thm 1.2 (p. 2): every component of Kh~(T) is either rational or special.
- Thm 2.14 (p. 7): for any pointed Conway tangle T, every component of Kh~(T) is linear.
- Thm 2.15 (p. 7): every component of Kh~(T) equals r_n(p/q) or s_2n(p/q) for some n >= 1, p/q in QP^1. Sentence after it: the local system on any component of Kh~(T) is trivial.
- Thm 3.1 (p. 8): a curve that wraps around a non-special puncture cannot be a component of Kh~(T). (False for BN~, Example 2.13.) Proof uses Thm 2.2 "in an essential way" (p. 8).
- Prop. 3.2 (p. 8): the differential of DD^c_1(T) only contains linear combinations of D, S, S^2.
- Thm 4.1 (p. 10): a curve that wraps around the special puncture cannot be a component of BN~(T) or of Kh~(T).
- Thm 4.4, extension property (p. 11): DD(D_T), DD^c(T), DD_1(D_T), DD^c_1(T) extend to type D structures over the A_infty algebra B^*[U] (Defs. 4.2, 4.3; gr(U) = q^{-3} h^{-1}; mu_k picks up U^{k-2}), recovering the original at U = 0. Interpretation given (p. 11): the curves are unobstructed in the three-punctured sphere obtained by filling in *.
- Thm 5.1 (p. 30): every special component of Kh~(T) is s_2n(p/q) with trivial local system. Thm 5.4 (p. 32): every rational component is r_n(p/q) with trivial local system. Lemma 5.2 (p. 30): H.id is null-homotopic on every direct summand of DD^c_1(T) corresponding to a component.
- Over arbitrary fields: [KWZ-mut] Theorem B / Thm 3.19 (p. 19), Thm 7.5 (no wrapping around *, for BN~ and Kh~, p. 36), Thm 7.6 (linearity of Kh~), Prop. 7.9, Thms 7.10, 7.11.

## 4. Which types occur where; how Kh~ arises from BN~

- Kh~(T): only r_n(p/q) and s_2n(p/q); no arcs. Known examples in the paper: Kh~(Q_s) = r_1(s); Kh~(P_{2,-3}) = one rational curve of slope 1/2 and one special curve of slope 0 (Example 2.13, p. 7); from Fig. 2e these are r_1(1/2) and s_4(0) (my reading of the figure). "At the time of writing, no tangle is known whose invariant Kh~ contains a rational component of length >= 3" (p. 35; repeated in [KWZ-mut], p. 35).
- BN~(T): 2^{|T|} arcs plus possibly compact curves. Arcs need not be straight: BN~(P_{2,-3}) is one arc whose singular peg-board representative has two segments, of slopes 1/2 and 0, turning at a lift of the top-right end (Example 2.13). Compact components need not be linear and need not be of type r or s: Remark 5.3 (p. 32) and Fig. 15 (p. 33) exhibit a compact component of BN~(T_CKMC) which extends over B^*[U] and whose complex contains an S^3 arrow; in Fig. 15 (my reading) its singular peg-board representative has two segments, of slopes 3 and -1, both on special lines, meeting at a lift of the bottom-right end, so the curve wraps around a non-special puncture. Rational curves of odd length may occur in BN~ with non-trivial local systems ([KWZ-mut] Thm 3.22 allows for this; Remark 3.20 gives an actual non-trivial local system in BN~).
- Relation: algebraic only. Kh~(T) is the multicurve of Cone(H.id on DD(T)); hence it is determined by BN~(T) with its H-action, summand by summand: Kh~(T) = union over components gamma of BN~(T) of the multicurve of Cone(H.id_{C(gamma)}). The paper gives no general geometric recipe. Stated instances: an arc a(s) gives r_1(s) (Example 2.5; [KWZ-mut] Remark 3.13: C(r_1(0)) = Cone(G.1_{C(a(0))})); the single arc BN~(P_{2,-3}) gives two components, one for each linear segment. Derived remark: on a compact summand with H.id null-homotopic the cone splits as two shifted copies of the summand.

## 5. Constraints on bigradings stated in the source

- q-parity: the quantum gradings of generators of DD^c(T) have the same parity if they lie in the same idempotent (p. 12, proof of Thm 4.1), and different parity in different idempotents (p. 32, proof of Thm 5.1); [KWZ-mut] p. 66 states "if and only if". Justified by the cube of resolutions.
- Mirror: Kh~(T^*) = m(Kh~(T)) up to a bigrading shift (Lemma 2.9, p. 6). [KWZ-mut] Prop. 2.36 (p. 12): -DD(T) = DD(-T), -DD_1(T) = h^1 DD_1(-T).
- Gluing is only relatively bigraded in [KWZ-lin] (Thm 2.8); absolutely bigraded in [KWZ-mut] Thm 2.40.
- Shape of a single component: fixed by Thm 2.15 (all internal relative gradings are those of Section 2).
- NOT in the source: any relation between the bigrading shifts of different components, any conjugation-type symmetry of Kh~(T), any constraint on the parity of h. [KWZ-mut] only adds that a component is determined by type, slope, length and bigrading shift (after Thm 3.19) and that Kh~ is unchanged by the component-preserving mutation (Thm 4.4, p. 20).
- Derived from the q-parity statement and Def. 3.12 of [KWZ-mut]: there is one class e in Z/2 for the whole of Kh~(T) such that a slope-0 component q^a h^b r_n(0) has a + n = e and a slope-0 component q^a h^b s_2n(0) has a = e (mod 2).

## 6. Corollaries and detection results

- Thm 2.6 (p. 5): T is rational iff Kh~(T) is a single figure-eight curve with the one-dimensional local system. Proof by the gluing theorem and Hedden–Ni two-component unlink detection (not by linearity). [KWZ-mut] Thm 3.17 (p. 18): over any coefficients, DD_1(T) = C(r_1(p/q)) up to shift iff T = Q_{p/q}; same for DD(T) and a(p/q).
- Prop. 2.7 (p. 5, from [KWZ19, Prop. 6.18]): no component of Kh~(T), over any field, is embedded.
- Thm 5.6 (p. 35): if Kh~(T) contains r_d(p/q) with d odd, then the two ends on which it is based are joined by T (connectivity detection). Prop. 5.8, 5.9 (p. 36): algebraic form via the actions of D_bullet, D_circ, S^2; Lemma 5.11 (p. 39): Bar-Natan's basepoint moving lemma D_p.id = (H - D_{p'}).id up to homotopy.
- Cor. 5.7 (p. 35): for T without closed components, the number of odd-length rational components of Kh~(T) is odd (proof uses only V_K(1) = 1 through the parity of dim Kh~ of a knot).
- Dimension formula used in [KWZ-mut] (proof of Lemma 6.4, p. 35, citing [KLMWZ, Lemma 2.10]): for a component gamma of length l and slope p/q != 0, dim HF(a(0), gamma) = l|p|; for slope 0 it is 0 if gamma is special and 2 if rational.
- Applications cited (p. 1): equivariant cosmetic surgery and cosmetic crossing for split links [KLMWZ], thin gluing criteria [KWZ-thin], strong inversions [KWZ-strong].

## 7. Proof idea

1. Kh~ corresponds to Cone(H.id) on DD^c(T). In the cone, an arrow D^n (n > 1) or S^m (m > 2) is removed by the Clean-Up Lemma using the H-arrows; so DD^c_1(T) has only D, S, S^2 (Prop. 3.2).
2. A curve wrapping around a non-special puncture can be twisted (Thm 2.2) until it turns by more than 135 degrees; its complex then contains D^n, n > 1, or S^m, m > 2. Contradiction (Thm 3.1). This step is why BN~ is not covered.
3. Wrapping around * is excluded by the extension property. B^infty is the endomorphism A_infty algebra of the two parametrising arcs in the wrapped Fukaya category of the three-punctured sphere (fill in *); it has mu_2 as in B and higher products from discs covering *, e.g. mu_4(S,D,S,D) = 1, deformed to U^2 in B^*[U]. A curve wrapping * contains bullet -D-> bullet -S-> circ -D-> circ -S-> bullet -D-> bullet; the resulting U^2 term in the structure relation cannot be cancelled, because arrows labelled U are excluded by q-parity (q(U) = -3).
4. The extension comes from Khovanov–Rozansky matrix factorizations in Ballinger's multifactorization form (the tangle version of Rasmussen's d_{-1}). The cube of resolutions gives a type D structure over the dg endomorphism algebra A of two elementary matrix factorizations; H_*(A) = B (Lemma 4.12, Cor. 4.21); mirror symmetry for the pair of pants (AAEKO, Orlov) gives A quasi-isomorphic to B^infty (Thm 4.23), bigraded version Thm 4.25; positivity in U and Lemma 4.27 transport the extension through the cancellations and clean-ups that lead to curve form.
5. Lemma 5.2: H.id is null-homotopic on each component of Kh~. For a special component, mu_4 forces a chain of U^2 arrows; these close up only if the two legs have equal length, and the unequal case is excluded by H.id = 0; the same computation forces the local system X X^{-1} = id (Thm 5.1). For a rational component, a complex over F[D,S^2]/(DS^2) with only D, S^2 arrows and H.id = 0 must be r_n, with trivial local system (Lemma 5.5).
6. Remark 5.3: unlike for HFT, extendability alone does not give the special classification; H.id = 0 is needed (T_CKMC).

## 8. Open questions and expectations stated

- [KWZ-lin] states no conjecture about which lengths, slopes or gradings occur. The only geography remark: no known tangle has a rational component of length >= 3 in Kh~ (p. 35).
- Expectations in [KWZ-lin], all settled in [KWZ-mut]: naturality over arbitrary fields (p. 4); Thm 3.1 over arbitrary fields (p. 8); Kh~(Q_s) over arbitrary fields is the same curve with local system (-1) (Example 2.5, p. 5).
- Remark 4.13 / 4.26 (pp. 16, 29): invariance of the multifactorization of a tangle diagram up to 1-homotopy is left open ([KWZ-mut] refers to separate work for it).
- [KWZ-mut] Remark 3.23 (p. 19): "A reasonable question is whether Kh~(T) contains an odd-length rational curve for any tangle T"; if so Kh~ detects connectivity for all tangles.
- [KWZ-mut] p. 62: the quasi-isomorphism from mirror symmetry is only established over fields; extension to rings expected.

## 9. Answers to Q1–Q4 (DERIVED; curves at slope infty)

Method. The rotation rho swaps slopes s <-> -1/s and bullet <-> circ and preserves relative bigradings, so HF(a(1/n), gamma(infty)) = HF(a(-n), gamma(0)), HF(a(0), gamma(infty)) = HF(a(infty), gamma(0)), HF(a(infty), gamma(infty)) = HF(a(0), gamma(0)). I computed H_*(Mor(C(a), C(gamma))) over F_2 with all gradings from the explicit complexes of Sections 1-2. Checks: d^2 = 0 and grading consistency of all complexes; HF(a(0), Cone_H(a(-n))) reproduces the reduced Khovanov homology of T(2,n) (unknot, Hopf link, trefoil (0,0),(4,2),(6,3), ...) and a(+n) gives the mirrors; dimensions agree with the [KLMWZ] formula of Section 6; Euler characteristics agree with the K_0 formula of Section 10. Ranges: special, length parameter m <= 5 and n <= 10; rational, m <= 7 and n <= 9. Status of the formulas below: the Euler characteristics hold for all m, n (exact K_0 computation, Section 10, given the complexes of Sections 1-2); the dimensions hold for all m, n by the [KLMWZ] formula; these two facts imply for all m, n that in each q-degree all generators have the same h-parity. The single delta-grading and the polynomials P(t) are verified only in the stated ranges. Notation: t = q^2 h; [k]_x = 1 + x + ... + x^{k-1}.

Q1. A curve can be made disjoint from a(infty) iff HF(a(infty), .) = 0. The lifts of a(infty) are the unit segments on the non-special lines of slope infty (x odd). (i) Every linear curve carried by the special line of slope infty (x even: through * and the bottom-left end) lies in a neighbourhood of that line which contains no lift of a(infty) and neither of its endpoints; so it is disjoint. Among components of Kh~ these are exactly the s_2n(infty). Yes: it is the line through the special puncture. (ii) r_n(infty) is carried by the line through the two endpoints of a(infty) and meets a(infty) in exactly 2 points (one per side change). (iii) A component of slope p/q != infty and length l meets a(infty) in l|q| points (l = n for r_n, 2n for s_2n).

Q2 and Q3. Relative gradings (q, h, delta) with base generator (0,0,0); "thin" = one delta-grading, and then every generator is at (2k, k, 0), recorded by the polynomial P(t) = sum of t^k. The first argument is the arc; for HF(gamma, a) replace t by t^{-1}.

Special curve s_2m(infty):

| arc | points | P(t), thin | Euler characteristic (up to +-q^c) |
|---|---|---|---|
| a(infty) | 0 | HF = 0 | 0 |
| a(0), a(1), any integer slope | 2m | (1 + t^3)[m]_{t^2} | (1 - q^6)[m]_{q^4} |
| a(1/2) | 4m | (1 + t^3)[m]_{t^2}(1 + t) | (1 - q^6)[m]_{q^4}(1 - q^2) |
| a(1/n), a(-1/n) | 2mn | (1 + t^3)[m]_{t^2}[n]_t | (1 - q^6)[m]_{q^4}[n]_{-q^2} |

Examples: m = 1, a(0): (0,0,0), (6,3,0). m = 2, a(0): (0,0,0), (4,2,0), (6,3,0), (10,5,0). m = 1, a(1/2): (0,0,0), (2,1,0), (6,3,0), (8,4,0). m = 1, a(1/3): (2k, k, 0), k = 0..5. Absolute, with [KWZ-mut] Def. 3.12 gradings and the arc generator at q^0h^0, in the rotated frame: HF([circ], s_2(0)) = q^{-3}h^{-1} + q^{3}h^{2}; HF([circ], s_4(0)) = q^{-5}h^{-2} + q^{-1}h^{0} + q^{1}h^{1} + q^{5}h^{3}.

Rational curve r_m(infty) (it does not lie near the special line; included for comparison):

| arc | points | gradings | Euler characteristic (up to +-q^c) |
|---|---|---|---|
| a(infty) | 2 | (0,0,0), (2m, m-1, 1): two delta-gradings | 1 - (-q^2)^m |
| a(0), a(1), any integer slope | m | thin, P = [m]_t | [m]_{-q^2} |
| a(1/2) | 2m | thin, P = [m]_t (1 + t^2) | [m]_{-q^2}(1 + q^4) |
| a(1/n), n >= 2 | mn | thin, P = [m]_t (1 + t + ... + t^{n-2} + t^n) | [m]_{-q^2}(1 - q^2 + ... + (-q^2)^{n-2} + (-q^2)^n) |
| a(-1/n), n >= 2 | mn | thin, P = [m]_t (1 + t^2 + t^3 + ... + t^n) | mirror of the previous line |

The second factor in the last two lines is the reduced Khovanov homology of the torus link T(2,n) or its mirror.

Vanishing. In a thin pairing the sign of a generator is determined by its q-grading (sign (-1)^k at q = 2k), so there is no cancellation: the sum of the absolute values of the coefficients of the Euler characteristic equals the number of intersection points. Hence the Euler characteristic of HF(a(s), gamma) vanishes identically only when HF = 0, i.e. only for gamma = s_2m(infty) and s = infty. At q = 1 every Euler characteristic of a special pairing vanishes (factor 1 - q^6), and at q^2 = -1 its absolute value is the dimension.

Q3. Yes for every pairing listed with a(0), a(1), a(1/2), a(1/n), for both types. The only pairing with two delta-gradings is the parallel one HF(a(infty), r_m(infty)). Arcs of other slopes were not computed.

Q4. No qualitative dependence on the parity of n: the count 2mn, thinness and the product formula are uniform. What changes: (i) for n odd, a(1/n) joins the top-right and bottom-left ends, so exactly one endpoint (the bottom-left one) lies on the special line of slope infty; then 2m of the 2mn intersection points come from the 2m endpoint-lifts on that line per period (the curve separates the two lifts of a(1/n) ending there) and 2m(n-1) are transverse crossings of the line; for n even both endpoints are on the non-special line and all 2mn points are transverse crossings. (ii) the factor [n]_{-q^2} equals 1 at q = 1 for n odd and 0 for n even, so for n even the Euler characteristic of a special pairing has a double zero at q^2 = 1.

## 10. Claim checks

- C1. Kh~: confirmed. Over F_2 by [KWZ-lin] Thm 2.15 (p. 7); over any field by [KWZ-mut] Thm 3.19 (p. 19), up to bigrading shift. Kh~ has no arc components. BN~: refuted. Only Thm 4.1 holds for BN~; non-linear compact components exist (Remark 5.3, Fig. 15, pp. 32-33) and BN~(P_{2,-3}) is a non-straight arc (Example 2.13).
- C2. Kh~: confirmed, trivial over F_2 (sentence after Thm 2.15; Thms 5.1, 5.4); over other fields the one-dimensional local system (-1), which is the same convention that makes Kh~(Q_s) = r_1(s). BN~: not proved and false in general ([KWZ-mut] Remark 3.20, p. 19).
- C3. Not addressed in either paper. Derived and verified numerically: with the gradings of [KWZ-mut] Def. 3.12, in K_0 = Z[q, q^{-1}]<[bullet], [circ]> (class = sum of (-1)^h q^j over generators),
  [r_n(0)] = (q - q^{-1}) (q^n - (-1)^n q^{-n})/(q + q^{-1}) [bullet],
  [s_2n(0)] = (-1)^{n+1} (q - q^{-1})^2 (q^{2n} - q^{-2n})/(q^2 - q^{-2}) ( -[bullet] + (q + q^{-1})[circ] ).
  Both are non-zero. The pairing is chi(Mor(X,Y)) = [ (q + q^{-1})(X_b^bar Y_b + X_c^bar Y_c) + X_b^bar Y_c + X_c^bar Y_b ] / (q - q^{-1}), bar = (q -> q^{-1}). Hence for any arc or curve a with class a_b[bullet] + a_c[circ]:
  chi HF(a, r_n(0)) = ((q + q^{-1}) a_b^bar + a_c^bar) (q^n - (-1)^n q^{-n})/(q + q^{-1}),
  chi HF(a, s_2n(0)) = (-1)^{n+1} a_c^bar (q^3 - q^{-3}) (q^{2n} - q^{-2n})/(q^2 - q^{-2}).
  The class of s_2n(0) spans, up to a scalar, the kernel of pairing with a(0). For slope infty swap the roles of bullet and circ. So C3 holds for each single component. It does not follow that the sum over components is non-zero.

## 11. Points where the mathematician's statements need adjusting

1. C1 as stated for BN~ is false (see above).
2. "The endpoints of a(1/n) lie on the special line of slope infty exactly when n is odd": only one endpoint does (the bottom-left end); the other endpoint is the top-right end, on the non-special line. For n even neither endpoint is on the special line (p. 35 table).
3. r_n(infty) does not lie near the special line of slope infty; it lies on the line through the endpoints of a(infty) and meets a(infty) twice.
4. Terminology: in [KWZ-lin] "rational/special" (Def. 2.12) are classes of linear curves and r_n, s_2n are named families; Thm 2.15 is the statement that only these families occur.

## 12. Derived remarks for the Lemma Q programme (not in the source)

- If T u Q_infty is the unknot, then by Section 9 and dim Kh~(unknot) = 1: Kh~(T) consists of exactly one rational component r_1(k) with k an integer, and special components s_{2m_i}(infty). Example consistent with this: Kh~(P_{2,-3}) = r_1(1/2) u s_4(0) pairs with a(0) to dimension 1 + 0.
- For such T and any rational filling Q, with a = -BN~(Q) of class a_b[bullet] + a_c[circ] and the special components carrying shifts q^{a_i}h^{b_i}:
  V(Q u T) = (term of r_1(k)) + a_b^bar (q^3 - q^{-3}) P_T(q) up to a unit, where P_T(q) = sum over i of (-1)^{b_i + m_i + 1} q^{a_i} (q^{2m_i} - q^{-2m_i})/(q^2 - q^{-2}).
  For the fillings at distance n, a_b^bar is a unit times [n]_{-q^{-2}}. All special components enter the Jones polynomial of every filling through the single Laurent polynomial P_T. The papers contain no statement preventing P_T = 0 (two special components with equal q-shift and opposite h-parity cancel).
- The slope k of the rational component need not be 0. At q^2 = -1 a thin summand in delta-grading d contributes (-1)^d times its dimension, so det(K_n) = 1 reads | e_0 |1 - nk| + n sum_i e_i 2m_i | = 1 with signs e in {+1, -1}; if the signs do not depend on n this gives k = 2 sum_i e_i m_i up to sign. In the P_{2,-3} example (unknot slope 0, components r_1(1/2) and s_4(0)), the determinant-1 fillings at distance n are n/(6n +- 1) or n/(-2n +- 1); normalising the unknot slope to infty and these fillings to 1/n turns the components into r_1(4) or r_1(-4), and s_4(infty).
- These three items rest on Sections 9 and 10 and on the gluing theorem; the absolute shifts of s_2m(infty; e) in [KWZ-mut] Def. 3.14 depend on an orientation datum e that I did not track, hence "up to a unit".
- Possible misprint in [KWZ-mut], display before Thm 2.40 (p. 12): the shift is written q^{a_i - a'_j} h^{b_i - b'_j}; with gr(Mor) = gr(target) - gr(source) one expects the opposite sign. Not checked further.

## 13. Files

- Report: /Users/calebbarnett/jones-lanes/theory-restart/lit/kwz-linear/REPORT.md
- Sources: /Users/calebbarnett/jones-lanes/theory-restart/lit/kwz-linear/src/tex/ (2202.01460v1), /Users/calebbarnett/jones-lanes/theory-restart/lit/kwz-linear/src/mut2026/tex/ (2602.23442v1), PDFs and text alongside, figure crops in src/png/.
- Computations: /Users/calebbarnett/jones-lanes/theory-restart/lit/kwz-linear/calc/hf.py (algebra, complexes, HF), run1.py (special), run2.py (rational), run3.py (closed formulas, mirrors, reversed order), run4.py (absolute gradings, classes), run5.py (K_0 pairing); outputs out_*.txt.
