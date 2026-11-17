# Derivations of 15 November 2026 (Claude). Status: derived and spot-checked; conventions of the multicurve calculus pending the literature digests in ../lit/.

## 1. Defect identity
BN~(K;F) = F[H]{0,s} + Tors, bars F[H]/(H^k) generated at (h,q), deg H = (0,-2). Cone of H: each bar gives Kh~ generators at (h,q) and (h-1, q-2k). Hence
    V~_K(q) = q^s + (1 - q^-2) chi_q(Tors),   chi_1(Tors) = -s/2   (V'(1) = 0).
Checks by hand: 3_1, 4_1, T(3,4) (bars k = 1 at h = 3 and k = 2 at h = 5: -3 = -s/2), T(3,5) (bars k = 1, 2, 1 at h = 3, 5, 7: -4 = -s/2).
T: a nonzero Tors never has chi_q = (1 - q^s)/(1 - q^-2). Knot Floer control: the same algebra holds for HFK^- and the analogue of T fails there.

## 2. Bracket-vector frames
Board frame: [X] = x id + y e. id = tangle of the unknot-closing slope (X cup id* = U), e = longitude prototype (flat X has [X] = u e). Unknot closure: <X cup id*> = x delta^2 + y delta = delta u, so y = u - delta x and
    [X] = u e + x (id - delta e).
v := id - delta e spans the G-orthogonal complement of id (G = [[d^2,d],[d,d^2]] in basis (id,e), d = delta): G(id,v) = 0, G(v,v) = d^2(d^2-1), G(e,v) = -d(d^2-1).
Multicurve reading (KWZ coordinates: unknot slope infinity, longitude slope 0): compact components of BN~(T_(kappa,h)) are disjoint from a(infinity), so their classes are G-orthogonal to [Q_infinity] = id: they lie in Z[q,q^-1] v. With arc component a(0): x = C (the class of the compact part), exactly; the unknot-closure relation y = u - delta x IS the orthogonality statement. At BN level the pairing B = chi_q HF( , ) is skew-Hermitian on compact classes (Poincare duality in dimension one), G = (1 - q^-2) B up to units, and chi_q HF(Gamma_c, Gamma_c) = |C_BN|^2 B(v,v): the H^*(S^1) summands cancel and what remains is the self-intersection character sum over pairs of eps (q^a - q^-a). C vanishes at A = 1 (so C = (1 - q^-2) C_BN) and delta | C (preferred framing).

## 3. Gram identity, doubles
<DX><DY> - <X cup Y*><Y cup X*> = d^2 (d^2 - 1) W conj(W), W = x_X y_Y - y_X x_Y.  With an unknot id-closure: <DX> = 1 + (d^2 - 1) y conj(y) = d^2 + d(d^2-1)[d x' conj(x') - x' - conj(x')], x' = x/u.
DX = X cup X* has unlink bracket iff y is a monomial iff X is Jones-rational. Sigma_2(DX) = S^3_0(kappa # -kappa).

## 4. The invariant J of a strong inversion
J_(kappa,h) := y/u = 1 - delta x/u in Z[A,A^-1]. Properties:
 - J = 1 iff flat (all K_n Jones-trivial); J a monomial iff Jones-rational; Lemma Q iff (J = 1 only for the trivial inversion).
 - J(A = 1) = 1; J = 1 at delta = 0 (t = -1).
 - MULTIPLICATIVE under equivariant connected sum along the axis: J is the character TL_2 -> Z[A,A^-1], e -> 0, of the quotient tangle in the direction in which the unknot closure is the trace (vertical composition); checked: J(3_1 # 3_1) = J(3_1)^2 and the composite has unknot closure.
 - Annular form: with P(z) = x z^2 + y delta the annular bracket of the branch-set knot, J = P(0)/P(delta); P(0) is the supertrace of w = i on annular Khovanov homology (z = w + 1/w).
 - |J|^2 = (<DX> - 1)/(delta^2 - 1) on the unit circle.
 - Trefoil (quotient tangle 1/2 + (-1/3), prototype 1/6, script ../tools/jq_tangle.py): J = t^7 + t^4 - t^3 = 1 - (1 + t^3)(1 - t^4), t = A^-4; x = unit (A^16 - 1)(A^8 - A^4 + 1), a product of cyclotomic polynomials (Montesinos product structure: the [0]-coefficient is multiplicative under pretzel sum and equals ((-A^-3)^a - A^a)/delta on 1/a). Closures reproduce V(T(3,5)) and V(P(-2,3,7)).
 - J'(1) is an additive integer invariant of strong inversions (8 for the trefoil with this chirality).
 - Chord form: (kappa,h) <-> an arc alpha attached to an unknot O (theta-curve quotient); K_n = n-half-twisted band surgery of O along alpha; J = through-strand bracket of S^3 - N(alpha) divided by the unknot value. Lemma Q = "J detects the trivial chord of the unknot".
Novelty of J as a named invariant: unchecked (compare Sakuma's eta, Snape's annular Jones polynomial, Lobb-Watson's refinement, Yamada polynomial of the quotient theta curve).

## 5. Period picture
det G = d^2(d^2-1): definite for |d| > 1, signature (1,1) for |d| < 1. At t = -e^{2 pi i/n}, n >= 7: |d| = 2 sin(pi/n); image of B_3 in PU(1,1) = triangle group (2,3,n); rational tangles = order-n vertices; |<Q cup Q'*>| = d^2 cosh(dist/2); unknot closures = adjacent vertices (cosh(dist/2) = 1/|d| = cos(pi/3)/sin(pi/n), the leg of the (2,3,n) triangle). Numerical check: |V(T(2,k))| = |d| cosh(d_k/2), cosh d_k = cosh^2(2a) - sinh^2(2a) cos(2 pi k/n), for k = 1,2,3,5, n = 7,8,9,12,30 (six digits). A general tangle: P_n(X) in CP^1, in the disk iff <DX> > 0; [X] = u(e + x' v) parametrizes CP^1 - {[v]} by x', with [v] the polar point of the vertex [id] (outside the disk in the indefinite range). Jones-unit knot X cup Q: <DX> cosh^2(d(P_n(X), v_Q)/2) = 1.

## 6. Consistency checks of the multicurve picture
 - Parity: a(1/n) has an endpoint on the special line of slope infinity iff n is odd; so compact curves can wind around an endpoint, and long H-bars can occur, only for odd n (K_1 = T(3,5) of the trefoil has an H^2 bar; even n gives proper rational replacements and unit bars).
 - r_1(s) must lie along the same (non-special) lattice line as a(s): otherwise HF(a(0), r_1(0)) would vanish instead of having rank 2 (two-component unlink).
 - Bigradable closed curves have rotation number zero for the flat line field, so they are never embedded circles; their self-Floer homology has the q-graded Euler characteristic of the self-intersection points only.

## 7. Geography reduction (evening; see board THEORY X.9 for the statement)
- Universal arc contribution A(k,j) = (arc specials) - (virtual string of r_1(k)), extracted from 106 two-bridge quotients: one value per (k,j); for k = 0: sign(j) q^{12j+4}[2|j|]_{q^6} (j > 0), e.g. (0,1): q^16 + q^22; (-4,1): q^14 + q^20; (-8,1): q^12 + q^20; (-16,2): q^20 + q^28 + q^36 + q^44; always 2|j| terms of one sign when sign(2j + k/4) = sign(-k) or k = 0. (k,j) = (-4,0): A = -q^-6 + q^-4 = -(1 - q^2) q^-6.
- P_tot = A(k,j) + (1 - q^2) Pi(q); P_tot(1) = 2j; flat iff j = 0 and Pi = -A(k,0)/(1 - q^2).
- Composite check: s.l1.y0.y0.y1.u2.l1.y0.y0.y1.u2 is 3_1 # 3_1 (tower + 4 bars); quotient Kh~ = r(-8) + specials (30,9),(30,9),(32,9),(24,10); k and j add (k = -8, j = 2); the formula gives J(3_1#3_1) = J(3_1)^2 exactly, J(3_1, left-handed) = -(q^8 - q^6 - 1)/q^14.
- Bar bookkeeping for integer closures: a special contributes V_kappa = {t^0,t^2,t^3,t^5} (t = q^2 h) on one diagonal; BN-bars go (h,q) -> (h+1,q+2l), i.e. from level d to level d+l-1 with q up by 2l; Szabo-type differentials go (h,q) -> (h+r,q+2r-2), i.e. down one level with q up by 2r-2. Bottom-to-top H^2 bar between blocks at relative shift (Delta a, Delta c) = (4,6) is the generic twist-knot step.
- In 9_2 (second inversion) the seven specials have consecutive homological shifts a = -8.5..-2.5 with (Delta a, Delta c) = (1,2) inside a level and (1,0) across the level change (the cancelling pair).

## 8. State at the pause (20:05). See the board, THEORY-width-ladder.md X.13.
- Tallies: k138 132 tangles / 366 level pairs; two-bridge to 45: 182 / 513; doubles 21 / 132; sums 82 / 201; random 34 / 47. Total 451 / 1259, 0 TILT failures, OVERHANG >= 6, all specials s4(inf).
- Corrections of the day: no single-root detection; reflective double components need not be unknotted; finite-index lemma false (E); arc character not a function of (k,j) (9_46 second inversion: q^28 + q^34 + q^38 + q^44 against q^26 + q^32 + q^38 + q^44); sign coherence false; all-s4 is an observation.
- Unrefereed: mech/sum/REPORT.md (J-TILT; J as signed count of bullet-generators of BN~(T); sum rule), mech/maps/REPORT.md (BLINDNESS).
- Observation not yet used: the twist-knot step (Delta h, Delta q) = (4,6) between consecutive specials is the period of reduced Khovanov homology of three-strand torus links (Kh~(T(3,3n+1)) is a sum of V_kappa blocks shifted by (4,6)); the special part lies in a band of slope 3/2 in the (h,q) plane, while delta-levels have slope 2.
- Theta-curve reading: T(0) is the two-component link of the two non-unknotted constituents of the quotient theta-curve, banded with the Seifert framing; lk = 4j; the specials are the non-torus part of its reduced Khovanov homology.
