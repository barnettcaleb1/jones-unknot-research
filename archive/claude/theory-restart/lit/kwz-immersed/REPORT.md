# Digest: Kotelskiy, Watson, Zibrowius, "Immersed curves in Khovanov homology" (arXiv:1910.14584)

**Version read.** arXiv v2, 17 Dec 2019 (latest version on the arXiv listing; v1 is 31 Oct 2019; the listing shows no journal reference, publication status not verified). 95 pp. Read from the TeX source (`src/tex/sections/*.tex`) with page numbers from `src/paper.pdf` (pdftotext) and figures checked by rendering pages (`src/png/`). Theorem/page numbers below are those of v2.

**Marking.** Statements with a cited location (theorem, example, figure, page) are from the paper. "[mine]" = my own inference or computation from statements in the paper; not in the source.

---

## 0. Bottom line

1. The paper proves, over any field k, a classification of bigraded complexes over an explicit quiver algebra B by bigraded immersed multicurves with local systems on the four-punctured sphere S^2_{4,*} (Thm 1.5 = Thms 5.14, 5.22, 5.27), and a pairing theorem (Thm 7.2) computing BN~(L), Kh~(L), Kh(L) of L = L(T_1,T_2) as wrapped Lagrangian Floer homology of m(curve of T_1) with curve of T_2, bigraded, and F[H]-linear for BN~.
2. It does **not** contain: the planar cover R^2 - Z^2 with "special lattice points", the notion of slope of a component, linearity of components, the curves r_n(p/q), s_2n(p/q), or any statement about Jones polynomial / Euler characteristic / decategorification of multicurves. The only cover that appears is the torus double cover of the pillowcase (Prop 8.3, pp. 77-78), used to match BN~ of rational tangles with straight lines. Items (e) and (g) of the brief are therefore mostly "not in this source"; the geography results are in the later KWZ papers ("Thin links and Conway spheres" arXiv:2105.06308, "Khovanov multicurves are linear" arXiv:2202.01460; strong inversions are treated in "Khovanov homology and strong inversions" arXiv:2104.13592), which I did not digest.
3. Naturality under the mapping class group (adding twists = Dehn twists on curves) is proved **only over F = F_2** (Thm 8.1); for other fields it is "expected". Hence BN~ and Kh~ of a general rational tangle Q_{p/q} are identified with the embedded arc / figure-eight only over F_2 in this paper; over other fields only the twist tangles T_{±n} are computed.
4. For the F[H]-module structure of BN~(T_1 ∪ T_2) the paper gives: towers come from ends of non-compact curves meeting at a common puncture ("each tower comes from the wrapping behavior of non-compact curves", proof of Prop 6.15, p. 61), H = moving to the next intersection point along the wrapping ray (Remark 5.23), and cone formulas (P5). It gives **no** general rule reading H-torsion orders off the curves. In its own main example (closures of the (2,-3)-pretzel tangle) the curve BN~(T_{2,-3}) has no compact component, and all torsion, including F[H]/(H^2) for T(3,4), comes from the arc-arc pair [mine, from the gradings in Ex 7.7].

---

## (a) Setting

### Tangles
- Def 1.11 (p. 6): an unparameterized pointed 4-ended tangle is an embedding of two arcs and finitely many circles in D^3 up to isotopy with a distinguished end *; parameterized = plus an oriented circle on ∂D^3 through the four ends (equivalent to diagrams up to Reidemeister moves). Closed components are allowed.
- The Bar-Natan bracket [[T]]_{/l} depends on an orientation of T for its absolute bigrading only: reversing a component t multiplies by h^{-2 lk_T(t)} q^{-6 lk_T(t)} δ^{-lk_T(t)} (Prop 4.8, p. 27), lk_T(t) = (n_+(t) - n_-(t))/2 counting crossings of t with other components.
- Crossing conventions (checked in the PSTricks sources): for the crossing whose over-strand runs NW-SE, the 0-resolution is ≍ (ends NW-NE and SW-SE joined) and the 1-resolution is )( (p. 18, p. 26). h(D(v)) = |v| - n_-, q(D(v)) = |v| + n_+ - 2 n_-, δ(D(v)) = (n_+ - |v|)/2.

### Gradings (Section 2.1, p. 11; Remark 2.3, p. 12)
- Two integer gradings: homological h and quantum q. **δ = q/2 - h** ∈ (1/2)Z.
- Differentials have bidegree (h,q) = (+1, 0), hence δ-degree -1.
- Shift notation: h^n q^m X is X shifted into homological grading n and quantum grading m (Bar-Natan's X[n]{m}). Grading of an arrow x --a--> y: gr(y) - gr(x) + gr(a).
- Link conventions (Section 3.1, p. 18): q(x_+) = +1, q(x_-) = -1; generator in V_{D(v)} with k plus and l minus: h = |v| - n_-, q = k - l + |v| + n_+ - 2n_-. Kh~(unknot) is supported in q^0 h^0 (p. 20). Right-handed trefoil: Kh~ in (h,q) = (0,2), (2,6), (3,8) (Fig. 37c), all δ = 1.

### The cobordism variable H and the algebra B
- Def 4.10 (p. 27): after fixing a distinguished end, every cobordism has a special component. H, **gr(H) = q^{-2} h^0** (δ(H) = -1), is defined by H·C := -(C with a 1-handle added to the special component). A dot on a component := (tube joining it to the special component) + H·(the cobordism); a dot on the special component is 0. q(H^i·C) = χ(C) - 2i - 2#dots - |B|/2 (B = set of tangle ends).
- Def 4.19 (p. 29): **B** = path algebra over R (any commutative unital ring) of the quiver with two vertices ●, ○, loops D_● at ●, D_○ at ○, arrows S_●: ● → ○ and S_○: ○ → ●, modulo D_○S_● = 0 = S_●D_●, D_●S_○ = 0 = S_○D_○ (composition right to left); written DS = 0 = SD. **gr(D) = q^{-2}h^0, gr(S) = q^{-1}h^0** (δ(D) = -1, δ(S) = -1/2). Idempotents: ι_●, ι_○.
- Thm 4.21 (p. 30) = Thm 1.1: for each choice i ∈ {1,2,3,4} of distinguished end there is an isomorphism ω_i: B → End_{/l}(≍ ⊕ )( ) with ● ↦ ≍, ○ ↦ )(, S ↦ saddle cobordisms, D ↦ identity cobordism with one dot on the non-special component. In the proof: **ω_i^{-1}(H) = D - SS**, i.e. H = D_● + D_○ - S_○S_● - S_●S_○.
- The ω_i agree on powers of S and on even powers of D; ω_i(D) = ±ω_j(D), with minus iff ends i, j lie on different components of the cobordism (Obs 4.24, p. 31).
- **Centre.** The paper never states the centre of B. It only uses that H = D - S^2 acts on everything (B is treated as an R[H]-algebra, generated over R[H] by idempotents, D, S; proof of Thm 4.21). [mine] H·D^k = D^{k+1}, H·S^k = -S^{k+2}, so H is central; but the centre is strictly larger than R[H]: D_●, D_○ and S^2 := S_○S_● + S_●S_○ are each central (all mixed products vanish), so Z(B) = R⟨1, D_●^k, D_○^k, (S^2)^k : k ≥ 1⟩. In the general language of Section 5 these are the loops U_f around the three non-special punctures separately, and H = U = Σ_f U_f with signs U_f := -(-p_f)^{n_f} (p. 52). A claim "Z(B) = F[H]" would be false.

### Type D structures and the invariant Д
- Type D structures over B = complexes over Mat(B) (Def 2.12, Prop 2.13, pp. 14-15); in practice: a bigraded set of generators, each in idempotent ● or ○, with a differential of bidegree (h,q) = (1,0) whose components are elements of B.
- Def 4.23 (p. 30) = Def 1.2: **Д(T) := Ω_i^{-1}([[T]]_{/l})**, a bigraded complex over B, invariant of the pointed (oriented) tangle up to homotopy; defined over Z.
- Trivial tangles (Ex 1.3): Д(≍) = [●], Д()( ) = [○], both with * at the NW end, in bigrading 0.

### Curves (Def 1.4 p. 3; Def 5.12 p. 43)
- S^2_{4,*}: sphere with four punctures, one special (*), with two parameterizing arcs. Drawn as a square: * at top-left (TL), non-special punctures BL, BR, TR. Equivalent picture: 3-punctured disc Σ (Fig. 12a, p. 37) with arc system A = {b, c}, outer boundary = *, three inner punctures. b ↔ ●, c ↔ ○. Faces: around BL (one side, loop D_●), around BR (two sides, the 2-cycle S_○S_●), around TR (one side, loop D_○). [Fig. 1 p. 2, Ex 5.5, 5.6.]
- A curve is (γ, X): either γ an immersed oriented circle representing a non-trivial primitive class and X ∈ GL_n(k) (compact), or γ an immersed interval with both ends on **non-special** punctures and X = id (non-compact). Multicurve = finite set, underlying curves pairwise non-homotopic; up to homotopy and similarity of local systems.
- Dictionary curve ↔ complex (Ex 1.6, Section 5.3): generators = intersection points of γ with the arcs b, c (idempotents ●, ○); each segment of γ in a face retracts to a path in the quiver, i.e. a power of D or of S, giving the differential; a 1-dimensional local system multiplies one differential by the scalar.
- **How a curve carries gradings**: a bigraded curve is a curve with a consistent bigrading (q,h) on its intersection points with the arcs (Def 5.12). Consistent means: for a segment x --a--> y, h(y) = h(x) + 1, q(y) = q(x) - q(a). So along a segment labelled D^k: q rises by 2k, δ changes by k - 1; along S^k: q rises by k, δ changes by k/2 - 1. In particular δ is constant along D and S^2 segments and drops by 1/2 along S.
- General grading rule (Def 5.4, p. 38): an elementary algebra element of a face with n_f sides has q = -2/n_f, δ = q/2.
- **Role of the special puncture**: (i) the distinguished end fixes ω_i, i.e. which component is special and what D means (signs of odd powers of D depend on it; this is what drives mutation, Section 9); (ii) it is the reduction point of BN~(L), Kh~(L) after gluing (the two * are identified, p. 5); (iii) H is "genus on the special component"; (iv) on the surface it is the outer boundary: no curve ends there, and S^2_{4,*} retracts onto the quiver away from it; (v) only mapping classes fixing * act (Thm 8.1).

### Classification theorem
- Thm 1.5 (p. 3), proved as Thm 5.14 (p. 44: every bigraded type D structure over A(Σ,A) is homotopic to one coming from a multicurve), Thm 5.27 (p. 51: uniqueness up to homotopy of curves and similarity of local systems), Thm 5.22 (p. 46: HF(C,C') ≅ H_*(Mor(C,C'))). Over any field k (Section 5.6 handles signs). Not available over Z: Remark 5.29 (p. 55) explains why a classification over Z "seems to be considerably harder".
- Def 6.1 (p. 56): **BN~(T;k) := L[Д(T;k)]**, the "arc type invariant".
- Def 6.5 (p. 58): Д_1(T) := cone [ q^{-1}h^{-1}δ^{1/2} Д(T) --H·id--> q^{+1}h^0δ^{1/2} Д(T) ], **Kh~(T) := L[Д_1(T)]**, the "figure-8 type invariant".
- Def 6.12 (p. 60): Д_n(T) := cone [ q^{-n}h^{-1}δ^{1-n/2} Д(T) --H^n--> q^{+n}h^0δ^{n/2} Д(T) ], L_n(T) its curve. Kh~ = L_1; Kh(T;K) = L_2(T;K) for char K ≠ 2; Kh(T;F) = q^{-1}L_1 ⊕ q^{+1}L_1 (Remark 6.13).
- The curves depend on the field (Section 9.1, Ex 9.1: T(4,5) over F versus Q).

### Structural facts about the curves
- Prop 6.15 (p. 60): if T has exactly l closed components, BN~(T) has exactly 2^l non-compact components, and exactly 2^l ends at each of the two non-special punctures joined by T (none at the third). So a tangle without closed components has exactly one arc component, and its two ends are at the two non-special punctures joined by the strand of T that does not contain *. The proof counts towers of rational closures: a closure by a rational tangle joining punctures i, j has n_i + n_j towers, n_i = number of ends of BN~(T) at i.
- Prop 6.17: L_n(T) is compact for n > 0. Prop 6.18 (p. 61): no component of BN~(T), Kh~(T), Kh(T), L_n(T) is compact and embedded (no compact embedded curve admits a quantum grading).
- Thm 1.14 = Thm 9.9: Conway mutation preserves the underlying curves of BN~(T;k) and the local systems up to sign. Thm 9.17: s^k is mutation invariant.

---

## (b) Pairing theorems

### Gluing convention (Def 4.30, p. 32; Fig. 10, p. 34)
L(T_1,T_2): put T_1 on the left and T_2 on the right; Fig. 10b: rotate T_1 by π about the vertical axis in the plane of the diagram, join its (now right-hand) ends to the left-hand ends of T_2 (the two * are joined by a short arc), and join the outer ends over the top and under the bottom. L(T_1,T_2) = L(T_2,T_1). Reduction point = the joined *.

Checked instances (figures):
- L()( , ≍) = unknot (Ex 7.3, Fig. 35a). L(≍, ≍) = two-component unlink (Ex 7.4).
- L()( , T_3) = right-handed trefoil, T_3 = three vertical crossings (Ex 7.5, Fig. 37a).
- L(≍, T_{2,-3}) = unknot; L(T_{-n}, T_{2,-3}) = P(-n,2,-3) = mT(2,5), mT(3,4), mT(3,5) for n = 1, 3, 5 (Fig. 40).
- [mine] In Conway terms with ≍ the 0-tangle: L(T_1,T_2) = N(rot(T_1) + T_2); L(≍, T) is the closure joining NW-NE and SW-SE of T, L()( , T) the closure joining NW-SW and NE-SE.

### Mirror
- Def 4.25 (p. 31): mT = all crossings switched. m(C) for a type D structure: reverse all arrows, exchange S_● and S_○, negate all gradings. Prop 4.26: Д(mT) = m(Д(T)).
- On curves (p. 61): m(L) is the image of L under the involution that reflects Fig. 12a in its horizontal middle line (fixes every puncture, preserves b and c), with reversed bigrading and inverse-transposed local systems. Prop 7.1 (p. 61): m(BN~(T)) = BN~(mT), **m(L_i(T)) = h^1 L_i(mT)** (so m(Kh~(T)) = h^1 Kh~(mT)).
- [mine] In the pillowcase coordinates of Prop 8.3 this involution is (x,y) ↦ (x,-y), i.e. slope s ↦ -s; the arcs of ≍ and )( are fixed.

### Algebraic pairing
Prop 4.31 (p. 32), over any commutative unital ring R: for L = L(T_1,T_2),

  h^0 q^{-1} δ^{-1/2} CBN~(L) ≅ Mor( m(Д(T_1)), Д(T_2) )  as chain complexes of R[H]-modules.

### Geometric pairing: Theorem 7.2 (p. 62), over any field k (intro version: Thm 1.9, p. 5)
- (P1) BN~(L) ≅ q^1 h^0 HF( m(BN~(T_1)), BN~(T_2) )
- (P2) Kh~(L) ≅ HF( m(BN~(T_1)), Kh~(T_2) ) ≅ HF( m(Kh~(T_1)), BN~(T_2) )
- (P3) Kh(L) ≅ HF( m(BN~(T_1)), Kh(T_2) ) ≅ HF( m(Kh(T_1)), BN~(T_2) )
- (P4) q^{-1}h^{-1} Kh~(L) ⊕ q^{+1}h^0 Kh~(L) ≅ HF( m(Kh~(T_1)), Kh~(T_2) )
- (P5) for i ≥ 1, coker H^i := H_*[ q^{-i-1}h^{-1} CBN~(L) --H^i--> q^{i-1}h^0 CBN~(L) ] ≅ HF( m(BN~(T_1)), L_i(T_2) ) ≅ HF( m(L_i(T_1)), BN~(T_2) )
- (P6) HF( m(L_i(T_1)), L_j(T_2) ) ≅ q^{-M}h^{-1} coker H^m ⊕ q^{M}h^0 coker H^m, M = max(i,j), m = min(i,j).

All bigraded. Thm 1.9 adds: the first is an isomorphism of k[H]-modules, the others of vector spaces. Note "coker H^i" is the homology of the cone, not the module-theoretic cokernel.

### What HF means here (Section 5.4)
- Def 5.15 (p. 44): pairing position. The **first** curve is wrapped: each end of a non-compact curve spirals infinitely often around its puncture (ray t ↦ φ_f(s+ε+t, t)); the second curve runs straight into the puncture. Intro, Ex 1.7: "wrapping the first curve infinitely many times around the punctures at their ends".
- Def 5.16 (p. 45): CF(C,C') is generated by intersection points, split into upper (in arc neighbourhoods) and lower (in faces); the differential counts embedded bigons from upper to lower generators.
- Defs 5.17-5.20 (p. 46): the bigrading of an intersection point x is the bigrading of its resolution φ(x) ∈ Mor(C,C') (paths from a generator of C through x, turning right, to a generator of C'; labelled by an idempotent or by the algebra element of the face path, anticlockwise only). Concretely gr(x) = gr(y') - gr(y) + gr(a). Lemma 5.21: d on CF has δ-degree -1, q-degree 0.
- Thm 5.25 (p. 51): for curves in minimal position, HF(L,L') ≅ V^0_0(n n') ⊗ k⟨γ ∩ γ'⟩ (n, n' = ranks of the local systems) unless γ, γ' are parallel, in which case one adds (V^0_0(1) ⊕ V^0_1(1)) ⊗ V^{q(γ,γ')}_{δ(γ,γ')}(dim ker((X^{-1})^t ⊗ X' - id)). Stated for compact curves; "the other cases are treated similarly" (non-compact first curve wrapped).

### The F[H]-module structure read from curves
- Remark 5.23 (p. 50): the canonical isomorphism HF ≅ H_*(Mor) transports the k[U]-action (U = H); on lower intersection points, x·U is the **next intersection point on the same straight segment** running into the puncture, or 0 if there is none. Extension to upper generators is "not canonical" without more work.
- Intro Ex 1.10 (p. 5): "the H-action on the generators corresponds to wrapping around the non-special puncture".
- Unknot, Ex 7.3 (p. 63, Fig. 35b): m(BN~()( )) ∩ BN~(≍) = {w_i}, i ≥ 0, w_i ↔ S^{1+2i}: ○ → ●, gr(w_i) = q^{-(1+2i)} h^0; so q^1 HF = q^0 h^0 k[H]. The w_i spiral into the common puncture BR.
- Unlink, Ex 7.4 (p. 67): intersection points ↔ basis ..., D^2, D, id, S^2, S^4, ... of ι_●Bι_●; H w_0 = w_1 + w'_1; q^{-1}BN~ = q^0 F[H] ⊕ q^{-2} F[H].
- Trefoil, Ex 7.5 (p. 67, Fig. 37b): BN~(T(2,3)) = tower from w_0 at (h,q) = (0,2) plus one isolated point v_2 at (3,8); i.e. q^2h^0 k[H] ⊕ q^8h^3 k. The text describes Kh~(T(2,3))^{k[H]} as carrying one arrow v_1 --H--> v_2.
- Towers: proof of Prop 6.15 uses "each tower comes from the wrapping behavior of non-compact curves"; number of towers of BN~(L) is 2^{|L|-1} (Prop 3.6, p. 22); for a knot the tower generator sits at h = 0, q = s^k(K) (Prop 3.8, p. 23): BN~(K) = q^{s}h^0 k[H] ⊕ ⊕_i k[H]/(H^{l_i}).
- Torsion orders: the only tools given are (P5) and the bookkeeping of Prop 9.3's proof (p. 81): a tower contributes 1 to rk Kh~ and 2 to rk Kh (char ≠ 2); k[H]/(H) contributes 2 and 2; k[H]/(H^m), m ≥ 2, contributes 2 and 4. More generally dim coker H^i = i·#towers + Σ_j 2 min(i, l_j). **No statement in the paper reads l_j directly from the geometry of the curves.**
- Thm 4.34 (p. 36): BN~(L,p) as a bigraded R-module is independent of the basepoint, and carries an R[H_1,...,H_l]-module structure (l = number of components); as R[H]-modules different basepoints can differ (trefoil ∪ unknot: Q[H]^2 ⊕ (Q[H]/H)^2 versus Q[H]^2 ⊕ Q[H]/(H^2)).

---

## (c) BN~ versus Kh~

- Links: Prop 3.9 (p. 24): 0 → q^{-2}h^0 CBN~(L) --H--> CBN~(L) → CKh~(L) → 0, so CKh~(L) ≃ [q^{-2}h^{-1}CBN~(L) --H--> CBN~(L)]; over char ≠ 2 also 0 → q^{-4}CBN~ --H^2--> CBN~ → q^{-1}CKh → 0. Cor 3.10: CKh(L;k) ≃ total complex of H, H, 2 (formula (9)).
- Tangles: Kh~(T) is by definition the curve of the cone of H·id on Д(T) (Def 6.5).
- Embedded arc: the cone of H on the arc of )( is the figure-8 curve around the arc (Fig. 2c, Fig. 30), L[○ --(D - S^2)--> ○], with local system (-1) in the paper's sign convention (Ex 1.6). Ex 6.6 (p. 58): Kh~()( ) is obtained by replacing the arc by the figure-8; over F the same holds for every rational tangle by Thm 8.1.
- One teardrop (p. 59-60, unnumbered paragraph before Question 6.10): if a curve has at most one teardrop and no closed components, the cone of H is obtained by resolving the teardrop and replacing each resulting non-compact component by a figure-8. Question 6.10: the general rule is open in this paper.
- Obs 5.26 (p. 51), for N large (γ wraps around each inner puncture strictly fewer than N times): on a compact curve U^N·id is null-homotopic, so the cone is two grading-shifted copies of the curve; on a non-compact curve the cone is the compact curve made of two copies of γ joined at the ends by paths wrapping N times around the two end punctures, with trivial local system.
- Ex 6.7, n = 5 (p. 59): on the compact component of BN~(T_{2,-5}) the cone of H "simply splits into two copies of itself".
- [mine] H acts null-homotopically on any cone of H, hence HF(a, Kh~(T)) always has H = 0; and cone(H) on L_2(arc) is two copies of L_1(arc), not of L_2.

---

## (d) Rational tangles and worked examples

### Trivial tangles
- BN~(≍) = arc through ● joining BL and BR (horizontal bottom edge); BN~()( ) = arc through ○ joining TR and BR (vertical right edge) (Fig. 2a). Each is the non-special strand pushed to the boundary (Ex 6.2). Bigrading 0.
- Kh~()( ): generators ○ at (q,h,δ) = (-1,-1,1/2) and (+1,0,1/2), differential D - S^2; figure-8 with lobes around TR and BR. Same with ● for ≍. Mirror: (q,h) = (+1,+1) and (-1,0), both δ = -1/2 (Fig. 35c).

### Twist tangles (Ex 4.27 p. 31, Ex 6.2 p. 56), valid over Z
Horizontal n positive crossings (0-resolution ≍), n ≥ 1:
  Д = [ ●(h=0,q=n,δ=n/2) --S--> ○(1,n+1) --D--> ○(2,n+3) --SS--> ○(3,n+5) --D--> ... --> ○(n,3n-1) ], all ○ at δ = (n-1)/2.
Vertical n positive crossings T_n (0-resolution )( ):
  Д(T_n) = [ ○(h=0,q=n) --S--> ●(1,n+1) --D--> ●(2,n+3) --SS--> ●(3,n+5) --D--> ... --> ●(n,3n-1) ], δ = n/2 then (n-1)/2.
T_{-n} = mirror: Д(T_{-n}) = [ ●(-n,-3n+1) --> ... --D--> ●(-3,-n-5) --SS--> ●(-2,-n-3) --D--> ●(-1,-n-1) --S--> ○(0,-n) ]. (The displayed formula in Ex 6.2 has typos in the idempotents: an ○ printed at q = -n-5; the mirror rule and Ex 4.27 fix it.)
Example: Д(T_3) = [○(0,3) --S--> ●(1,4) --D--> ●(2,6) --SS--> ●(3,8)], δ = 3/2, 1, 1, 1 (Fig. 37).
BN~(T_n) is an embedded arc obtained from the ○-arc by Dehn twists; it joins TR to BR for n even and TR to BL for n odd (Fig. 28).
Kh~(T_n): double each generator (q,h) to (q-1,h-1) and (q+1,h), cone of H; curve = figure-8 around the arc.

### General rational tangles
- Ex 6.2: "the arc type invariant BN~(T;F) of any rational tangle is obtained by pushing the tangle component without the reduction point * to the boundary of D^3"; expected over any field, proved over F only (via Thm 8.1). Ex 6.6: same for Kh~(T;F) = figure-8 around that arc.
- No formula for the absolute bigrading of BN~(Q_{p/q}) is given; it is determined by iterating the bimodule of Prop 8.2. The paper cites Thompson (rational tangles over H = 0: zig-zag complexes, bigradings governed by a B_3-action) as explained by the curve picture (p. 56).
- The paper does not name tangles by slope p/q anywhere except the informal T_{p/q} in the introduction (p. 10).

### (2,-n)-pretzel tangles (Ex 4.28, 6.3, 6.7; Figs. 9, 29, 31, 32)
T_{2,-n}: two vertical twist regions side by side, * at NW; orientation as in Fig. 9a unless said otherwise.

**n = 2** (one closed component, so two arcs; Ex 6.3):
 Д(T_{2,-2}) = [○(δ=-1/2,q=-9,h=-4) --S--> ●(-1,-8,-3) --D--> ●(-1,-6,-2)] ⊕ [●(-1,-6,-2) --D--> ●(-1,-4,-1) --S--> ○(-3/2,-3,0)].
 Two embedded arcs = arcs of the two 2-twist rational tangles (Fig. 29a). No compact component. Kh~ = the two figure-8s.

**n = 3** (Fig. 9c, p. 33). Д(T_{2,-3}) has 9 generators forming one path:
 ●(δ=-3/2,q=-7,h=-2) <--D-- ●(-3/2,-9,-3) <--S-- ○(-1,-10,-4) <--D-- ○(-1,-12,-5) --S--> ●(-3/2,-11,-4) --D--> ●(-3/2,-9,-3) --SS--> ●(-3/2,-7,-2) --D--> ●(-3/2,-5,-1) --S--> ○(-2,-4,0).
 **BN~(T_{2,-3}) is a single non-compact immersed arc from TR to BR with one teardrop around TR; it has no compact component** (Fig. 29b, Fig. 32a). With the orientation compatible with the unknot closure L(≍,T) (multiply everything by h^2 q^6 δ^1, Ex 7.6) the two end generators are ●(q=-1,h=0) and ○(q=2,h=2); Figs. 41, 42 use the gradings of Fig. 9c.
 Kh~(T_{2,-3}) has two compact components (Ex 6.7, Fig. 31a): (1) the figure-8 of a 2-twist rational tangle, equal to δ^{-2}q^{-12} Kh~(T_2) in the bigrading of Ex 7.7; (2) the figure-8 built on the arc that "starts and ends at the top right puncture and winds around the top two punctures twice" (it encircles * and TR). Individual generator gradings of (2) are not tabulated; its pairing with m(BN~(T_{-n})) gives the four classes ϰ_1,...,ϰ_4 in δ = -3/2, q = -3, -7, -9, -13 (after the shift of Ex 7.7), independent of n.

**n = 5**: BN~(T_{2,-5}) = arc with the same underlying curve as for n = 3 (Fig. 29b) ∪ **one compact component** (Fig. 29c): a closed curve with 2 ○- and 4 ●-generators and one self-intersection, looping around TR and around the bottom punctures. No gradings are given. By Ex 6.7 and Remark 6.8 this compact component is the figure-8 of the same 2-twist rational tangle: Kh~(T_{2,-5}) = component (2) above plus three copies of that rational figure-8. This is the paper's only example of a compact component in BN~.

**Closures** (Ex 7.6, 7.7; Figs. 41, 42):
- L(≍, T_{2,-3}) = unknot: HF(m(BN~(≍)), BN~(T_{2,-3})) is a single tower starting at h^0 q^{-1}; BN~(T_{2,-3}) ∩ m(Kh~(≍)) is one point at δ^0 q^0.
- P(-n,2,-3) = L(T_{-n}, T_{2,-3}), n = 1, 3, 5: HF(h^0 q^{-n} m(BN~(T_{-n})), BN~(T_{2,-3})) ≅ h^0 q^{n-1} BN~(P(-n,2,-3)). Generators (δ, q, h): tower from w_0 at (-2,-4,0); ϰ_1 (-2,-12,-4), ϰ_2 (-2,-8,-2) for all n; v_1 (-1,-10,-4) for n ≥ 3; v_2 (-1,-14,-6) for n ≥ 5; each further full twist adds a generator shifted by δ^{-1}q^{-4}.
- δ^{n/2}q^{n} Kh~(L(T_{-n},T_{2,-3})) ≅ ⟨ϰ_1,...,ϰ_4⟩ ⊕ δ^{(n-4)/2}q^{n-12} Kh~(T(2,2-n)) (p. 70), with ϰ_i in δ = -3/2, q = -3, -7, -9, -13; ⟨ϰ⟩ agrees with Watson's ϰ for the (2,-3)-pretzel tangle (his q is half of this q and his δ has the opposite sign).
- [mine] For n = 3 (mT(3,4)): rk Kh~ = 5 gives two torsion summands; the torsion part ⟨ϰ_1,ϰ_2,v_1⟩ has dimension 3, and H (q-degree -2, h-degree 0) can only send v_1 to ϰ_1. Hence BN~(mT(3,4)) = tower ⊕ k[H]/(H) ⊕ k[H]/(H^2) with the H^2-torsion ⟨v_1, ϰ_1⟩ produced by the pairing of two arcs. Check: removing the shift q^{2}, the classes are w_0 (q,h) = (-6,0), ϰ_2 (-10,-2), v_1 (-12,-4), ϰ_1 (-14,-4); the cone of H then has generators at (-6,0), (-10,-2), (-12,-3), (-12,-4), (-16,-5), which is the mirror of Kh~(T(3,4)). The paper lists only the bigradings, not the module structure.

### Other examples
- Ex 6.4: Д((L,p) # )( ) ≃ emb(CKh~(L,p)^{R[H]}), emb: R[H] → B, 1 ↦ ι_○, H ↦ D_○ - S_●S_○. So connected sums with a trivial strand give curves built from H-arrows between ○-generators.
- Ex 9.1 (p. 79): Kh~(T(4,5))^{R[H]} over F and Q with H and H^2 arrows; the two curves differ.

---

## (e) The planar cover

**Not in this paper.** There is no cover R^2 - Z^2, no "special lattice points", no lifts of curves, and no notion of slope of a curve. What the paper has is Section 8.2, Prop 8.3 (p. 77) with Fig. 49 (p. 78):

- Pillowcase P = [-1,1]^2/(±1) = quotient of the torus R^2/(2Z)^2 by the hyperelliptic involution, identified with the traceless SU(2) character variety of the 4-punctured sphere by (x,y) ↦ ρ_{x,y}: a ↦ i e^{kπy}, b ↦ i, c ↦ i e^{kπx}.
- Marked points: p_0 = (0,0) ↔ special puncture *, p_1 = (0,1) ↔ puncture 1 = BL, p_2 = (1,1) ↔ puncture 2 = BR, p_3 = (1,0) ↔ puncture 3 = TR.
- R(B^3, ≍) = the straight line y = 1 joining p_1, p_2; R(B^3, )( ) = the line x = 1 joining p_2, p_3; for the crossing tangle with over-strand SW-NE (the paper's \CrossingLDot) the line y = x - 1 joining p_3 and p_1.
- Prop 8.3: up to homotopy there is a unique identification of P minus marked points with the tangle boundary such that R(B^3,T) agrees with BN~(T;F) for all pointed rational tangles, compatible with Dehn twists. τ_12 (exchanging punctures 1, 2) acts as the linear map (1 1; 0 1), i.e. (x,y) ↦ (x+y, y); τ_23 as (x,y) ↦ (x, x+y) (the second only in a commented-out line of the source; the text says "the same argument works").

[mine] Translation into the planar picture: lifting to R^2, the marked points are Z^2; lifts of * are (2Z)^2; BL ↔ (even, odd), BR ↔ (odd, odd), TR ↔ (odd, even). BN~(Q;F) of a rational tangle lifts to straight segments between adjacent non-special lattice points, with slope dy/dx = 0 for ≍, ∞ for )(, 1 for the SW-NE-over crossing, 1/n for T_n (n crossings of that type stacked vertically, obtained from x = 1 by τ_12^n). The mirror acts by slope ↦ -slope. The mathematician's labelling Q_s must be matched to this by hand; the paper does not fix a slope convention.

---

## (f) Mapping class group action (Section 8, all in characteristic 2)

- Thm 8.1 (p. 72) = Thm 1.13: for a pointed 4-ended tangle T and ρ in the mapping class group of the 4-punctured sphere fixing the reduction basepoint, BN~(ρ(T)) = ρ(BN~(T)) and L_n(ρ(T)) = ρ(L_n(T)) for all n ≥ 1 (hence also Kh~, Kh), **over F**. First sentence of Section 8: "In this section, we will only work in characteristic 2. However, we expect the main result to hold over any field."
- τ (Fig. 43, p. 71) adds one crossing between the two right-hand ends (NE, SE) of T. Prop 8.2 (p. 72): Д(τT) ≃ Д(T) ⊠ τ, with τ the type AD bimodule of Fig. 44 on generators ●● (δ = n_+/2, h = -n_-), ●○ (δ = (n_+ - 1)/2, h = -1 - n_-), ○○ (δ = n_+/2, h = 1 - n_-), where (n_+, n_-) = (1,0) or (0,1) is the sign of the added crossing; actions (H^k|H^k), (D H^k|D H^k), (-|S), (S H^k|H^k), (S H^k|D H^k), (H^k|H^k) + (D H^k|SS H^k), and two higher actions (S H^k, S H^n | S H^{n+k}), (S H^k, D H^n | S H^{k+n}).
- Proof: keep T fixed and change the arc system by the half twist; check on elementary segments (Figs. 46-48). The twist on the other pair of ends follows by the rotation exchanging idempotents; the two twists generate the stabilizer of *.
- **Grading shifts**: the paper states that after forgetting the parameterization one loses "the absolute bigradings" (p. 56); the only grading information for twisting is in the bimodule of Fig. 44 (and Prop 4.8 for orientation changes). No closed formula for the shift of a curve under a Dehn twist is given.
- Which geometric twist: adding a crossing at the two right ends is the half twist exchanging TR and BR (punctures 3 and 2), acting on the pillowcase by the unipotent matrix fixing the line x = 1; adding a crossing at the bottom ends exchanges BL and BR and fixes y = 1 [mine, from Prop 8.3's proof].

---

## (g) Jones polynomial, Euler characteristic, decategorification

**Nothing substantive in the paper.** Occurrences:
- Section 1.7 (p. 9): one sentence that the Jones polynomial via Kauffman's state sum is computable locally through the skein module of a tangle and that Bar-Natan's framework does the same for Khovanov homology.
- Section 1.9 (p. 11): figure-8 curves also appear in Bigelow's homological definition of the Jones polynomial and in Manolescu's and Droz-Wagner's work; for 2-bridge knots the intersection picture (e.g. Fig. 37c) "coincides with the Bigelow generators for reduced Khovanov homology" [Manolescu, Section 7.5].
- p. 56: Thompson's B_3-action governing bigradings of rational tangle invariants.
No Burau representation, no module of decategorified curves, no Euler characteristic statement.

[mine] What follows formally from Prop 4.31 and (P1), (P2), and is the calculus the mathematician wants; checked on the trefoil:
- Define [T] := Σ over generators x of Д(T) of (-1)^{h(x)} q^{q(x)} [idempotent of x] ∈ Z[q^{±1}]{●,○}. This is the Kauffman bracket vector in the basis ≍ = ●, )( = ○ in the paper's normalization (it depends on orientation through n_±).
- Poincaré series: ι_●Bι_● and ι_○Bι_○ have series (1+q^{-2})/(1-q^{-2}) (basis 1, D^k, S^{2k}), ι_○Bι_● and ι_●Bι_○ have q^{-1}/(1-q^{-2}) (basis S^{2k+1}). Since the mirror negates gradings, χ of Mor(mД(T_1), Д(T_2)) is the bilinear form G([T_1],[T_2])/(q - q^{-1}) with Gram matrix G = ((q+q^{-1}, 1),(1, q+q^{-1})).
- Hence χ(BN~(L)) = G([T_1],[T_2])/(1 - q^{-2}) as a power series in q^{-1}, and **χ(Kh~(L)) = Σ (-1)^h q^q dim = G([T_1],[T_2])**, the Jones polynomial normalized to 1 on the unknot, q + q^{-1} on the 2-component unlink. Trefoil: [)( ] = ○, [T_3] = q^3 ○ - q^4 ● + q^6 ● - q^8 ●, G = q^3(q + q^{-1}) - q^4 + q^6 - q^8 = q^2 + q^6 - q^8, matching Fig. 37c.
- The same formula holds componentwise for any bigraded curve γ with [γ] := Σ over its intersection points with b, c. χ(Kh~(T)) = (q - q^{-1})[T]. For a compact γ the series G([a],[γ])/(1 - q^{-2}) must be a Laurent polynomial for both trivial arcs a, and G is invertible at q = ±1, so [γ] is divisible by q - q^{-1}: compact components of BN~(T) contribute to the bracket vector only multiples of (q - q^{-1}).
- The classes D_●, D_○, S^2 and H are invisible at this level except through these series.

---

## Claim checks

**C1** (Kh~(Q_s) is a figure-eight obtained from a(s) = BN~(Q_s), along the same lattice line of slope s). Confirmed in substance, with restrictions. Figure-8 obtained from the arc: Ex 6.6 (p. 58), for )( over any field and for all rational tangles over F_2 via Thm 8.1; for T_{±n} over any field by Ex 4.27/6.2 plus the teardrop paragraph (pp. 59-60). Straight line: Prop 8.3 (p. 77) says BN~(Q;F) is a straight line in the pillowcase joining two non-special marked points. The planar cover R^2 - Z^2 and the phrase "lattice line of slope s" are not in this paper, and the paper fixes no slope convention; the figure-8 lies in a neighbourhood of the arc, so its lift follows the same line [mine]. In char ≠ 2 the figure-8 carries the local system -1 in the paper's sign convention (Ex 1.6).

**C2** (dim HF(a(s), Kh~(Q_s')) = |pq' - p'q|). Not stated in the paper; modified. By (P2) (Thm 7.2) HF(m(BN~(Q_{s''})), Kh~(Q_{s'})) = Kh~(L(Q_{s''},Q_{s'})), and by Thm 5.25 its dimension is the minimal intersection number when the curves are not parallel. So the count is between the mirrored arc a(s) = m(a(s'')) (slope s = -s'' in the coordinates of Prop 8.3) and the figure-8 of slope s'. [mine] Lifting to the torus R^2/(2Z)^2 gives intersection number Δ = |pq' - p'q| for Δ ≥ 1; for Δ = 0 the dimension is 2, not 0 (Ex 7.4: Kh~ of the unlink in q = ±1). Instances in the paper: 1 (Ex 7.3), 2 (Ex 7.4), 3 (Ex 7.5). That rk Kh~ = det for two-bridge links is not in the paper.

**C3** (for a knot, BN~(K) = HF(BN~(T_1), BN~(T_2)) = one tower from the arc pair plus torsion from compact components). Modified. Correct parts: the formula needs the mirror and a shift, BN~(K) ≅ q^1 HF(m(BN~(T_1)), BN~(T_2)) (Thm 7.2 (P1)); exactly one arc in each BN~(T_i) (Prop 6.15); exactly one tower (Prop 3.6), which comes from the arc-arc pair (proof of Prop 6.15). Incorrect part: torsion is not confined to compact components. The arc-arc pair itself contributes torsion: trefoil = k[H] ⊕ k with two rational tangles and no compact components (Ex 7.5, Fig. 37b); P(-3,2,-3) = mT(3,4) with BN~(T_{2,-3}) a single arc and three torsion classes ϰ_1, ϰ_2, v_1 (Ex 7.7, Fig. 41), including H^2-torsion [mine].

**C4** (a compact component away from the arc's endpoints and not winding around them contributes only F[H]/(H); long torsion only when it winds around an endpoint). Not addressed in the paper: there is no statement about torsion orders of arc-compact pairs. Consistent with Remark 5.23 (H moves along the ray into the puncture) and Obs 5.26. [mine] A rank count supports a sharper form: for an embedded arc a and a compact γ not parallel to the figure-8 e(a), the number of torsion summands is i(e(a),γ)/2 and their total length is i(a,γ) (Thm 5.25 plus the cone argument of (P5)); group the crossings of γ with a into maximal runs of consecutive crossings made while γ winds around an endpoint of a; then #summands = #runs and Σ lengths = Σ run lengths. So all summands are F[H]/(H) iff γ never winds twice in a row around an endpoint of a; winding once (as a figure-8 of another slope does at a shared puncture) still gives only F[H]/(H). Example: L_2(a') winds twice around the shared puncture and gives F[H]/(H^2) (coker H^2 of the tower). Caveat: as a statement about all long torsion in BN~(T_1 ∪ Q_s) the claim is false, since arc-arc pairs produce it (see C3).

**C5** (two curves homotopic to straight lines of different slopes: all intersection points have the same δ). Not stated in the paper; modified. It fails literally for the wrapped pairing of two arcs: in Ex 7.3 the points w_i have δ = -1/2 - i, and in Fig. 37b the tower w_i has q = 2 - 2i at h = 0 (H has δ = -1). It holds in the paper's examples for the non-tower points and for arc versus figure-8: Fig. 37c has all three generators at δ = 1; Fig. 37b has w_0 and v_2 at δ = 1. A general statement of this kind is not in this paper (it belongs to the later "thin links"/"linear" papers).

---

## What the paper proves and does not prove

Proves: B ≅ End_{/l}(≍ ⊕ )( ) for each pointing (over any commutative unital ring); classification of bigraded complexes over B and their morphism spaces by multicurves and wrapped HF (over fields); the pairing theorem (P1)-(P6) with bigradings and the k[H]-structure on (P1); number of non-compact components; no embedded compact components; mapping class group naturality over F_2; mutation invariance of BN~ over F_2 and of s over any field; module structures for infinitely twisted knots (Section 10, over F_2).

Does not prove or address: naturality under twisting over fields other than F_2 (stated as expected); any geography of components (linearity, slopes, rational versus special); behaviour of the cone of H on general curves (Question 6.10); a geometric rule for H-torsion orders; anything about Euler characteristics. Question 6.9 (does Kh~(T) always contain a rational component for T without closed components?) and Question 6.16 (do non-compact components end on distinct punctures?) are posed, not answered.

Relevant to Lemma Q (Section 10.2, pp. 88-89): for a strongly invertible knot (K,h) with quotient tangle T_{K,h}, "in our conventions, the L(≍,T)-closure of the tangle is the unknot"; the x-torsion submodule ker(x^N) ⊂ Kh~(K_∞), K_∞ = L(T_{-∞}, mT_{K,h}), corresponds to Watson's ϰ(K,h) as a vector space, and the paper states that this module vanishes if and only if the strongly invertible knot is trivial (citing Watson, Thm 1). This is a statement about homology, not about its Euler characteristic. In the worked example the twisting family T_{-n} is at distance 1 from the unknot-closure slope [mine: mirrored arc slopes 1/n against slope 0 in the coordinates of Prop 8.3], i.e. it is the integer-surgery family on the trefoil (mT(2,5), mT(3,4), mT(3,5) for n = 1, 3, 5, with double covers the 5-, 3-, 1-surgeries up to orientation), not a family at distance n from the unknot slope. The closures K_n of the brief are a different one-parameter family of slopes.

Also relevant: Prop 9.3 (p. 81): if BN~(L)_{Q[H]} contains Q[H]/(H) then Kh(L;Z) has 2-torsion. Question 9.4: does BN~(K)_{Q[H]} contain Q[H]/(H) for every non-trivial knot? (all examples known to the authors do). Knight-move in this language: only towers, Q[H]/(H), Q[H]/(H^2); disproved by Manolescu-Marengon.

---

## Open questions for the mathematician

1. Slope dictionary: the paper's pillowcase coordinates give ≍ ↦ 0, )( ↦ ∞, SW-NE-over crossing ↦ +1, mirror ↦ negation, and L(Q_{s''}, Q_{s'}) has determinant Δ(-s'', s'). Does this match the convention behind "Q_s" and "τ(∞), τ(0)"? It has to be fixed against the later KWZ papers.
2. Torsion from arc-arc pairs: the T(3,4) example shows F[H]/(H^2) arising from one immersed arc (with a teardrop) paired with an embedded arc. Is there a run-length rule for immersed arcs analogous to the one in C4?
3. The cone of H on a general immersed arc (Question 6.10) controls how Kh~(T) splits into rational and special components; is this resolved in the later papers in the generality needed?
4. Coefficients: with naturality proved only over F_2 here, which field is intended for the Jones calculus? (Euler characteristics are field-independent, but the curves are not.)
