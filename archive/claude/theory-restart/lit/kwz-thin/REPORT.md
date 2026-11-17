# Literature digest: kwz-thin

STATUS: complete (both sources read in TeX source; page numbers from the arXiv PDFs)

## 0. Sources and versions

- **[Thin]** Kotelskiy, Watson, Zibrowius, "Thin links and Conway spheres", arXiv:2105.06308**v3** (4 Feb 2022), 50 pp.; Compositio Math. 160 (2024) 1467-1524. All numbers below are v3 numbers. Warning: v1/v2 contained the geography proofs, which were moved to [Linear]; papers citing "KWZ thin, Theorem 6.5 / 6.41 / Corollary 6.42" (as [Cosm] does) refer to the v2 numbering.
- **[Cosm]** Kotelskiy, Lidman, Moore, Watson, Zibrowius, "Cosmetic operations and Khovanov multicurves", arXiv:**2109.14049v1** (28 Sep 2021; only one arXiv version), 20 pp.; Math. Ann. 389 (2023) 2903-2930.
- **[Linear]** (consulted only for three cited statements) Kotelskiy, Watson, Zibrowius, "Khovanov multicurves are linear", arXiv:2202.01460v1.
- Raw files: `src/thin`, `src/cosmetic`, `src/linear` (TeX under `tex/`, text dumps `*.txt`).

Everything is over F = F_2 unless said otherwise. Items marked **[inference]** are my own deductions from the cited statements, not statements of the papers.

## 1. Conventions (both papers agree)

- **Gradings.** h homological, q quantum, delta = q/2 - h ([Thin] p.2; [Cosm] p.12 "q = 2(h+delta)"). chi_gr Kh~(L) = sum (-1)^h t^{q/2} dim Kh~^{h,q}(L) = V_L(t) ([Thin] p.2). Algebra B: gr(D) = q^{-2} delta^{-1}, gr(S) = q^{-1} delta^{-1/2}, h(D)=h(S)=0; differentials preserve q and lower delta by 1 (equivalently raise h by 1). H = D + S^2. D_1(T) = [q^{-1} delta^{1/2} D(T) --H--> q^{1} delta^{1/2} D(T)] ([Thin] Sec. 5.1; [Cosm] Sec. 2.1, 2.3).
  - Consequence for the mathematician's parity statement: in this normalization a delta-thin summand in delta = d contributes (-1)^d * sum_q dim_q (-t)^{q/2} to V. Cancellation in V is only possible between summands whose delta-gradings differ by an ODD integer. (This is "2 mod 4" in a doubled convention delta' = q - 2h.) "A-link" = no such cancellation at all at t = -1.
- **Rational filling.** T(p/q) := Q_{-p/q} cup T ([Thin] p.4; [Cosm] Fig. 1e and p.2). Q_s^* = Q_{-s}. Gluing ([Thin] Thm 5.8 = [KWZ, Thm 1.9]; [Cosm] Thm 2.3): Kh~(T1 cup T2) (x) V = HF(Kh~(T1^*), Kh~(T2)) and Kh~(T1 cup T2) = HF(Kh~(T1^*), BN~(T2)) = HF(m(BN~(T1)), Kh~(T2)), relatively bigraded, V = delta^{1/2} q^{1} F + delta^{1/2} q^{-1} F. Kh~(T^*) = m(Kh~(T)) up to shift ([Thin] Lemma 5.9). Hence T(s) is computed by pairing Kh~(T) with the slope-s curve r_1(s) = Kh~(Q_s), or with the arc a(s) = BN~(Q_s).
- **Double covers.** If T is the quotient tangle of (K,h), framed so that slope infinity lifts to the meridian and slope 0 to the Seifert longitude, then Sigma(T(p/q)) = S^3_{p/q}(K) ([Cosm] p.2 and p.11). Distance Delta(p/q,p'/q') = |qp' - pq'| ([Cosm] Def 2.9). So Delta(1/n, infinity) = n.
- **Cyclic order of slopes.** QP^1 in RP^1 = S^1 with the counter-clockwise order; (s1,s2) = {s : (s1,s,s2) increasing} ([Thin] Sec. 2.1 p.6). Check: Theta(P_{2,-3}) = (-2, infinity] contains 0, so "increasing" is the usual order of R wrapped through infinity. X^m = {-s : s in X} (Def 1.11).
- **Curves.** r_n(p/q) rational of length n, s_{2n}(p/q) special of length 2n, images of r_n(0), s_{2n}(0) under [[q,r],[p,s]] in PSL(2,Z) = Mod(S^2_{4,*}) ([Thin] Def 5.11 p.30; [Cosm] Def 2.4). Kh~(Q_{p/q}) = r_1(p/q). Planar cover R^2 minus Z^2; special puncture drawn as marked squares.
- **Sign differences Kh vs HF** ([Thin] Sec. 6.1 p.31): the Khovanov and Heegaard Floer conventions are opposite; see Section 4 below.

## 2. Thin fillings: definitions and theorems

### 2.1 Definitions ([Thin] Sec. 1, 2, 6.3)

- Thin: a delta-graded vector space supported in at most one delta-grading (Def 1.1). Z/2-thin: supported in one delta-grading mod 2 (Def 4.25). A-link: dim H(L) = |chi_delta H(L)|, i.e. Z/2-thin (Def 1.3). Full support (Def 1.4): no gaps in the delta-support; for Kh~ this is a folklore conjecture; if it holds, thin = A-link (Prop 1.5).
- Theta(T) = {s : T(s) thin}, A(T) = {s : T(s) A-link} (p.4). Def 6.14 (p.34): Theta_G(Gamma) = {s : HF(r_1(s), Gamma) is G-thin}; Theta_Kh(T) = Theta_Z(Kh~(T)), A_Kh(T) = Theta_{Z/2}(Kh~(T)). Note the test object is the compact curve r_1(s), not the arc.
- Line sets (Sec. 2.1, p.6-8). A line is c = (s(c), gr(c), eps(c)) in QP^1 x G x {0,1}, G = Z or Z/2, eps = 0 rational, 1 special. gr: lines x lines -> G satisfies
  - symmetry: gr(c,c') + gr(c',c) = 0 if s(c) = s(c'), = -1 otherwise;
  - transitivity: gr(c,c') + gr(c',c'') = gr(c,c'') if (s(c),s(c'),s(c'')) is increasing;
  - linearity: gr(n.c, n'.c') = gr(c,c') + n' - n.
- **Remark 2.1 (p.7), the cleanest description of the delta-grading.** Rational lines over G = Z are identified with the pull-back of the universal cover p: R -> RP^1 to QP^1, i.e. each line is a lift eta(c) in R of its slope, the Z-action being deck translation (+1 = one counter-clockwise loop), and gr(c,c') = floor(eta(c') - eta(c)). The authors say they do not use this further.
- Def 2.2: C is s-consistent if gr(c,c') = 0 for all c,c' in C of slope s.
- Def 2.3: (C,D) is G-thin if there is n in G with, for all (c,d): (eps(c),eps(d)) in {(0,1),(1,0)} if s(c) = s(d), and gr(c,d) = n otherwise. Theta_G(C) = {s : ((s,0,0), C) thin}.
- Def 2.12: C exceptional if S_C = {s,s'}, C is s- and s'-consistent, and some c,c' of slopes s,s' have gr(c,c') != 0 != gr(c',c). (Impossible for G = Z/2.) Def 6.11: T is Khovanov exceptional if Kh~(T) is.

### 2.2 Combinatorial theorems ([Thin] Sec. 2, pp.8-12)

- Lemma 2.4: s(c) not in Theta(C) for rational c in C.
- **Lemma 2.5: if s_0 in Theta(C) then C is s-consistent for every s != s_0.**
- Lemma 2.6 (single supporting slope s): Theta(C) = {s} if C is not s-consistent and s-special; QP^1 if s-consistent and s-special; empty if not s-consistent and not s-special; QP^1 minus {s} if s-consistent and not s-special.
- **Lemma 2.7:** C = {c_1,...,c_n}, slopes (s_1,...,s_n) increasing, s_1 != s_n. Equivalent: (1) some s in Theta(C) lies in (s_n,s_1); (2) gr(c_i,c_j) = 0 for all i<j; (3) (s_n,s_1) subset Theta(C) subset [s_n,s_1]; (4) (s_n,s_1) subset Theta(C).
- Theorem 2.9: for a non-trivial line set, Theta(C) is empty, a point, two points, or an interval; two points cannot occur for G = Z/2. Observation 2.10: boundary of Theta(C) lies in S_C. Prop 2.11: if Theta_Z(C) is an interval then Theta_Z = Theta_{Z/2}.
- **Theorem 2.14 (G-thin gluing):** C, D non-trivial, not both exceptional. (C,D) is thin iff (1) Theta(C) cup Theta(D) = QP^1 and (2) for all s in bdry Theta(C) cap bdry Theta(D), at least one of C, D is s-rational. Corollary 2.16: int Theta(C) cup int Theta(D) = QP^1 implies thin. Example 2.17 shows the exceptionality hypothesis is needed.

### 2.3 Khovanov theorems ([Thin] Sec. 6, pp.31-35)

- **Theorem 6.16 (reduction, p.34):** there are Phi: {Kh~(T)} -> line sets and gr with the three properties such that (i) same supporting slopes, (ii) Theta_G(Gamma) = Theta_G(Phi(Gamma)), (iii) Phi(Gamma) non-trivial, (iv) Gamma exceptional implies Phi(Gamma) exceptional, (v) s-rational iff s-rational, (vi) HF(Gamma,Gamma') G-thin iff (Phi(Gamma),Phi(Gamma')) G-thin. Construction: gr(c,c') := delta(gamma(c),gamma(c')); the line of a component gamma has gr = delta_H(gamma) if slope != 0 and delta_V(gamma) - 1/2 if slope 0. The proof normalizes absolute gradings so that **delta_H in Z and delta_V in Z + 1/2 for every component of every Kh~(T)**.
- Theorem 6.17 (= 1.8, 1.9): A_Kh(T) is empty, a point or an interval; Theta_Kh(T) is empty, a point, two points or an interval. Prop 6.18 (= 1.10): if Theta_Kh(T) is an interval, Theta_Kh = A_Kh.
- **Theorem 6.19 (A-link gluing):** T1 cup T2 is a Khovanov A-link iff (1) A_Kh(T1)^m cup A_Kh(T2) = QP^1 and (2) for every s in bdry A_Kh(T1)^m cap bdry A_Kh(T2), at least one of m(Kh~(T1)), Kh~(T2) has only rational components of slope s (condition R).
- **Theorem 6.20 (thin gluing):** same with Theta_Kh in place of A_Kh, under the hypothesis that at least one of T1, T2 is not Khovanov exceptional. Corollary 6.21: int Theta_Kh(T1)^m cup int Theta_Kh(T2) = QP^1 implies thin (same for A).
- Conjecture 6.12: no link has Kh~ supported in exactly two non-adjacent delta-gradings. Prop 6.13 (= 1.14): a Khovanov exceptional tangle would refute it. No Khovanov exceptional tangle is known; Heegaard Floer exceptional tangles exist (Example 7.15). Conjecture 7.13: Theta never consists of two points.

### 2.4 Exact criterion for a rational filling (answer to C2)

Combining Def 2.3, Def/Lemma 6.7, Lemma 6.10 and Theorem 6.16(ii): **T(s) is Khovanov thin iff**
(a) Kh~(T) has no rational component of slope s (special components of slope s are allowed; they pair to zero with r_1(s)), and
(b) delta(r_1(s), gamma) takes the same value on all components gamma of slope != s.
Equivalent form of (b) via Lemma 2.7: list the components of slope != s as gamma_1,...,gamma_n with slopes increasing counter-clockwise starting after s; then delta(gamma_i, gamma_j) = 0 for all i < j. In particular all components of a common slope != s have equal delta (Lemma 2.5), and components of consecutive slopes have delta(gamma_i,gamma_j) = 0 in the increasing direction (hence -1 in the other). T(s) is an A-link iff the same holds mod 2. No theorem of the paper expresses this through the Jones polynomial; delta only.

## 3. Statements about delta-gradings of components

All in [Thin] Sec. 6.1-6.2 (pp.31-34); "linear curve" is Def 4.14 (p.19): a closed immersed curve whose lift can be homotoped to have all tangent slopes in any neighbourhood of one slope p/q.

- Lemma 6.1: for a connecting domain phi from x to x' on one curve, delta(x') - delta(x) = -2 e(phi) (e = Euler measure). Lemma 6.2: an intersection point of gamma, gamma' with connecting domain phi from x in gamma to y in gamma' has delta = delta(y) - delta(x) - 1/2 + 2 e(phi). Prop 6.3, Cor 6.4 (delta(y) - delta(x) = -2e(phi) for a domain between two generators of HF(gamma,gamma')); Example 6.5 (bigon: difference -1). These do not assume linearity.
- **Def/Lemma 6.6:** for a linear curve of slope s, all intersections with horizontal lines of the parametrization have one delta-grading delta_H (if s != 0), all with vertical lines one grading delta_V (if s != infinity), and delta_V = delta_H - 1/2 for 0 < s < infinity, delta_V = delta_H + 1/2 for infinity < s < 0.
- Def 4.16 (used also for Kh): for two linear curves of the same slope, delta(gamma,gamma') := delta_H(gamma') - delta_H(gamma) (or with delta_V); "same delta-grading" means this is 0.
- **Def/Lemma 6.7 (p.32):** for linear curves gamma, gamma' of different slopes s, s', HF(gamma,gamma') is supported in the single grading
  delta(gamma,gamma') = delta_H(gamma') - delta_V(gamma) - 1/2 if s in (infinity, s') with s' in (0,infinity], or s in (s', infinity) with s' in [infinity,0);
  delta(gamma,gamma') = delta_V(gamma') - delta_H(gamma) - 1/2 if s in (s',0) with s' in [0,infinity), or s in (0,s') with s' in (infinity,0].
- Corollary 6.8: delta(gamma,gamma') + delta(gamma',gamma) = 0 for equal slopes, -1 for different slopes.
- **Theorem 6.9 (transitivity):** delta(gamma,gamma') + delta(gamma',gamma'') = delta(gamma,gamma'') for increasing triples.
- **Lemma 6.10:** for linear curves of the same slope, HF(gamma,gamma') = 0 if one is rational and the other special; otherwise it is non-zero and supported in the two consecutive gradings delta(gamma,gamma') and delta(gamma,gamma') - 1.
- Dependence on the test slope **[inference from 6.8, 6.9, Remark 2.1]**: each component gamma has a lifted slope eta(gamma) in R with delta(gamma,gamma') = floor(eta(gamma') - eta(gamma)). For two components of the SAME slope, delta(r_1(s),gamma') - delta(r_1(s),gamma) = delta(gamma,gamma') =: k for every test slope s != that slope: the offset k in Z is a constant of the pair. For components of different slopes the offset takes two consecutive values, switching when s crosses one of the two slopes.
- p.38 (after Prop 7.3): a special component of slope 0 contains two pairs of generators in gradings d - 1/2 and d + 1/2 (d its vertical grading), and a special component of slope infinity four generators in gradings d' - 1/2 and d' + 1/2 (d' its horizontal grading); so neither can occur in a multicurve all of whose vertical generators share one grading and all of whose horizontal generators share one grading. Used to show that for a connected alternating tangle diagram Kh~(T) has no components of slope 0 or infinity. Bar-Natan-Burgos-Soto: for such tangles all vertical generators share one delta_V, all horizontal one delta_H, differing by 1/2. So for alternating tangles all components are mutually consistent (Prop 7.3, Cor 7.4: Theta_Kh contains an open interval containing 0 and infinity).

## 4. Comparison with HFT ([Thin] Sec. 3, 4, 7)

- Geography: every component of HFT(T) is rational (lift a straight line, embedded, possibly with a local system; whether non-trivial ones occur is unknown) or special s_n(p/q; i,j) with trivial local system (Thm 3.9, from [Zibrowius]). Every component of Kh~(T) is r_n(p/q) or s_{2n}(p/q) with trivial local system (Thm 5.13, proved in [Linear] Thms 1.2, 5.1, 5.4); no component of Kh~(T) is embedded (Prop 5.6); Kh~ detects rational tangles (Thm 5.7).
- **Conjugation symmetry (Thm 3.10, HFT only):** the numbers of components s_n(p/q; i,j) and s_n(p/q; k,l) in any given delta-grading agree. This is the only theorem in the paper relating the delta-gradings of two distinct components of one slope. No Khovanov analogue is stated; in the tables one Khovanov s_4 corresponds to one conjugate pair of HFT specials.
- Lemma 3.11: rational components of HFT separate the punctures according to the connectivity of T (Khovanov analogue: [Linear] Thm 5.6 = [Cosm] Thm 2.7, for odd-length rational components only).
- Signs: HFT has delta(x') - delta(x) = +2e(phi) (Lemma 4.5), symmetry constant +1 (Cor 4.18), transitivity for decreasing triples (Thm 4.19), same-slope support in delta(gamma,gamma') and delta(gamma,gamma')+1 (Lemma 4.20); gr(c,c') := -delta(gamma(c'),gamma(c)).
- HFT thin theorems (4.27-4.34) are the same statements with an extra local-system condition R_* ("inhibited"/"complementary" local systems, Def 4.21); Thm 4.31 needs non-exceptionality and Example 7.15 shows it is necessary.
- Examples (Table 1, p.45): Theta_HF = Theta_Kh for Q_0, P_{2,-3}, P_{2,-2}, T_{4_1}; HFT(P_{2,-2}) has an extra special pair not present in Kh~. Example 7.14 (p.46-47): for a tangle with 5/3-filling 16n197566, Kh~ over F_2 is {16 s_4(infinity), s_8(infinity), r_1(4/3)} and over F_3 is {16 s_4(infinity), s_6(infinity), r_1(2), r_2(2)}, Theta = [infinity,4/3) resp. [infinity,2); HFT gives [infinity,2). Example 7.15: a tangle with HFT = {r(-5/2), 2 s_4(infinity)}, A_HF = (-5/2, infinity], Theta_HF = {infinity} (exceptional, offset 2); its Kh~ is {r_1(3/2), 8 s_4(infinity)} over F_2 and {r_1(-1/2), 2 s_4(infinity), 6 s_2(infinity)} over Q, F_3, F_5, F_7, F_11, with special components in three consecutive delta-gradings.
- Theorem 7.10 / Cor 7.11: a Khovanov A-link has L-space double cover; A_Kh(T) subset L(Sigma_T). For the quotient tangle T_n of the torus knot T(2,2n+1) in Seifert framing: A_Kh(T_n) = (4n, infinity] inside [2n-1, infinity] = L (p.43).

## 5. [Cosm]: split detection, cosmetic statements, unknot/unlink closures

- **Theorem 1.1 (p.1):** (K,h) non-trivial strongly invertible, f: S^3_r(K) -> S^3_{r'}(K) orientation-preserving with h_{r'} f = f h_r implies r = r'.
- **Theorem 1.2 (p.2):** T a Conway tangle with an unknot closure; if T(r) and T(r') are isotopic links then r = r' or T is rational. Proof input: Hanselman's theorem (cosmetic slopes are {+-2} or {+-1/n}), then Kh~ distinguishes.
- **Structure of Kh~(T) for T(infinity) = unknot (proof of Thm 1.2, p.11-12).** In the Seifert framing T has no closed component and connectivity of the type for which T(0) is a 2-component link. Because Kh~(T) meets the arc a_infinity in one point: **Kh~(T) = gamma_1 cup ... cup gamma_m cup rho, with gamma_i special of slope infinity and rho = r_1(s), s an even integer; m > 0 iff T is non-rational.** (s in Z from the single intersection; s even from Thm 2.7.) The special components are disjoint from a_infinity, so the unknot closure gives no information on their gradings; it pins the bigrading of rho only.
- Lemma 2.10 (p.8): for s != r and gamma rational or special of length l and slope r, dim HF(a(s), gamma) = l * Delta(s,r); an arc and a figure-eight r_1 of the same slope meet in 2 points; specials of slope s are disjoint from a(s).
  - **[inference]** dim Kh~(T(p/q)) = |q| * sum_i l_i + |p - s q| for p/q not in {infinity, s}; for the mathematician's K_n = T(1/n): n * sum_i l_i + |1 - s n|.
- Case 2 of the proof (p.13-14), slopes +-1/n: the arcs a_+ = BN~ of the mirror of the filling tangle are
  a_+ = [o^{-2n} -S-> b^{1-2n} -D-> b^{3-2n} ..S^2.. b^{4j-3-2n} -D-> b^{4j-1-2n} ..S^2.. b^{-1}], a_- its mirror image with gradings negated (superscripts are q-gradings; o, b the two idempotents; j = 1..floor(n/2)). dim HF(a_+-, rho) = |1 -+ s n|, equal only if s = 0. After pulling tight, all generators of HF(a_+-, gamma_i) sit near the vertical line through the special puncture, at the D-segments of the arc; there is a bijection x_+ <-> x_- with q(x_-) - q(x_+) = 8j - 4 - 4n < 0 (plus, for n odd, extra generators with shift -2), while HF(a_+-, rho) agree. Hence Kh~(T(1/n)) and Kh~(T(-1/n)) differ as bigraded groups. Case 1 (slopes +-2): HF(a_-, gamma_i) = q^{+2} HF(a_+, gamma_i).
  - **[inference]** the generators of HF(a(1/n), gamma_i) fall into floor(n/2) (+1 if n odd) blocks attached to successive D-segments, whose q-gradings step by 4; by Def/Lemma 6.7 the whole summand is delta-thin, so h steps by 2. The proof does not state this block structure as a lemma.
- **Theorem 3.1 = 1.6 (split tangle detection, p.9):** equivalent: T horizontally split; every component of BN~(T) is the horizontal arc or a generalized figure-eight [b -H^k-> b]; every component of Kh~(T) is r_1(0) up to shift; BN~(T) resp. Kh~(T) lies in a neighbourhood of the slope-0 arc; D(T) resp. D_1(T) has no generator in the idempotent o. The hard direction uses Xie's annular instanton detection theorem.
- Section 5 (K_n := T(1/2n), T with fixed connectivity and no closed components, so K_n are band surgeries on T(0); note this K_n is not the mathematician's K_n):
  - Lemma 5.4: if Kh~(T) = Sigma cup P has only slope-0 components with Sigma (specials) non-empty, then HF(a_{1/2n}, P) is independent of n as a graded group and HF(a_{1/2n}, Sigma) = q^{4n} HF(a_infinity, Sigma); so the K_n are pairwise distinct.
  - Lemma 5.5 and Theorem 5.3 = 1.4: if T is not horizontally split, the K_n with |n| >= N are pairwise distinct (dimension growth l_i |q_i - 2n p_i| and unbounded q-gradings).
  - **Theorem 5.6 (split closure property, p.17):** if T(0) is a split link K cup K' then Kh~(T) only contains components of slope 0. Proof: over F_2 the basepoint action of F[x]/(x^2) on Kh~(K cup K') is free, and a component of non-zero slope produces torsion. In particular this applies when T(0) is the 2-component unlink.
  - Theorem 5.7 (= Wang): T not horizontally split and T(0) split implies all K_n distinct.
  - Conjecture 5.8: T(0) split iff Kh~(T) has only slope-0 components. Theorem 5.9: true if in addition no rational component has length > 1. Conjecture 5.10: every rational component of Kh~(T; F_2) has length 1 (false away from characteristic 2).
- [Cosm] p.8 quoting [Linear]: a tangle without closed components has at least one rational component ([Linear] Cor 5.7: the number of odd-length rational components is odd); Thm 2.7: for the connectivity type of Section 4, an odd-length rational component has slope p/q with p even.

## 6. Geography restrictions (complete list found)

1. Every component of Kh~(T) is r_n(p/q) or s_{2n}(p/q), trivial local system ([Thin] 5.13; [Cosm] 2.5); none embedded ([Thin] 5.6). BN~(T) may be non-linear but cannot wrap around the special puncture ([Thin] p.30, citing [Linear]).
2. H.id is null-homotopic on every component of Kh~(T) ([Linear] Lemma 5.2).
3. T rational iff Kh~(T) = single r_1 ([Thin] 5.7); T split iff all components are r_1 of one slope ([Cosm] 3.1).
4. Odd number of odd-length rational components when T has no closed component; their slopes detect connectivity ([Linear] 5.6, 5.7). No rational component of length >= 3 is known ([Linear] p. after Thm 5.6); length 1 conjectured over F_2 ([Cosm] Conj 5.10).
5. HF(Gamma_1,Gamma_2) != 0 for any two tangle invariants ([Thin] Sec. 6.3, p.33-34).
6. T(infinity) unknot: Kh~(T) = specials of slope infinity plus one r_1(s), s in Z (Section 5 above). T(0) split: all slopes 0 ([Cosm] 5.6).
7. If T has a thin (A-link) filling s_0, components of any slope != s_0 have equal delta (equal mod 2), and consecutive slopes are aligned as in Lemma 2.7. Connected alternating diagrams: no components of slope 0 or infinity, everything consistent ([Thin] 7.3, 7.4).
8. Normalization: delta_H in Z, delta_V in Z + 1/2 for all components, so same-slope offsets are integers ([Thin] proof of 6.16).
9. HFT only: conjugate special pairs in identical delta-gradings ([Thin] 3.10).
10. Dependence on the field: slopes and lengths of components can change with the characteristic ([Thin] Ex. 7.14, 7.15).

## 7. Answer to the mathematician's question

**Is there a theorem or mechanism restricting the delta- or q-gradings of two components of the same slope relative to each other?**

Known:
- (a) Integrality only: the offset k = delta(gamma,gamma') of two same-slope components is an integer, and it is independent of the test slope (Section 3). Nothing constrains its parity in general.
- (b) Conditional constraint: if T has a thin filling at s_0, then k = 0 for every pair of components of a common slope s != s_0; if T has an A-link filling at s_0, k is even (Lemma 2.5 with G = Z or Z/2, plus Thm 6.16). Contrapositive: two components of slope s with odd offset force A_Kh(T) subset {s}. Nothing is forced at slope s_0 itself when the components there are special.
- (c) For the quotient tangle of a strong inversion the only thin filling one knows a priori is s_0 = infinity, and all components except the single rational one live at slope infinity. So (b) is vacuous exactly where it is needed: **neither paper restricts the relative delta- or q-gradings of the special components of slope infinity.** The unknot filling does not see them (they are disjoint from a_infinity).
- (d) Counterexample to any parity rule: Kh~(T_{4_1}) (quotient of the figure-eight knot) = s_4(infinity) in delta_H = 3, s_4(infinity) in delta_H = 4, r_1(4) in delta_H = 3; the text says the two specials lie "in adjacent delta-gradings" and Theta = A = {infinity} ([Thin] Table 1 p.45, p.44). Also T_b (Table 2): s_4(infinity) with multiplicities 4, 12, 8 in delta_H = 11/2, 9/2, 7/2 and s_4(4) in delta_V = 3 and 4; Example 7.15: three consecutive gradings.
- (e) Quantum gradings: [Thin] contains no statement about q-gradings of components. [Cosm] uses q only through the arcs: it computes how the q-grading of HF(a, gamma) shifts with the arc, for a fixed component; it proves nothing relating the q-gradings of two components.
- (f) All examples in the papers have same-slope special components in consecutive delta-gradings (no gaps); "no gaps" for links is Conjecture 6.12 / full support, open.

**[inference] Two consequences that the papers do not state** (sanity-checked on the trefoil and figure-eight data):
- Determinant constraint. For T cap-trivial in Seifert framing, Kh~(T) = {gamma_i} cup {r_1(s)}, each HF(a(p/q), gamma) is delta-thin, and |chi_delta| = det T(p/q) = |p|. With e_i = +-1 the parity of the offset of gamma_i relative to rho (constant for p/q on one side of s), this gives |q| sum_i e_i l_i +- |p - s q| = +-p for all p/q, hence **sum_i e_i l_i = -+ s**: the signed total length of the special components equals the slope of the rational component up to a global sign. Trefoil ([Thin] p.42-43, Seifert framing): one s_4(infinity), rational slope 4. Figure-eight: two s_4(infinity) of opposite parity, so the identity predicts s = 0 in Seifert framing; Table 1 lists r_1(4), which is consistent only if the framing of Table 1 differs from the Seifert framing by 4 (not verified).
- A-link filling space of such T is {infinity}, (s, infinity] or [infinity, s) (Lemmas 2.4-2.7), and a non-trivial Jones-trivial filling can never lie in A_Kh(T), since dim Kh~ > 1 = det.

Open (stated in the papers): existence of Khovanov exceptional tangles and of two-point Theta (Conj 7.13); full support / Conj 6.12; Question 7.2 (do Kh and HF thinness agree over Q); Conj 5.8 and 5.10 of [Cosm]; whether rational components of HFT carry non-trivial local systems. Not addressed anywhere: any rule for the delta- or q-offsets among special components of one slope; any statement about the Jones polynomial of fillings.

## 8. Claim checks

- **C1 (confirmed, with a caveat on the test object).** [Thin] Def/Lemma 6.7 (p.32): for linear curves of different slopes HF(gamma,gamma') is supported in one delta-grading, with the formula in Section 3. The statement is for closed linear curves, i.e. for r_1(s) = Kh~(Q_s), not literally for the arc a(s). For the arc it follows because HF(r_1(s),gamma) = HF(a(s),gamma) (x) V with V in one delta-grading (gluing theorem form; H null-homotopic on components, [Linear] Lemma 5.2), or by the same rectangle argument. For s equal to the slope of gamma the claim fails: Lemma 6.10 gives two consecutive gradings (rational gamma against r_1(s)) or zero (special gamma).
- **C2 (confirmed; exact statement in Section 2.4).** T(s) thin iff no rational component of slope s and delta(r_1(s), gamma) is constant over components of slope != s; equivalently delta(gamma_i,gamma_j) = 0 for i<j in the increasing order starting after s (Def 2.3, Lemma 2.7, Thm 6.16(ii)). Gluing version: Thm 6.20, with the non-exceptionality hypothesis.
- **C3 (confirmed).** Nothing forces a common parity. Example: Kh~(T_{4_1}) has two s_4(infinity) in delta_H = 3 and 4 ([Thin] Table 1 p.45, text p.44); also T_b (Table 2) and Example 7.15.

## 9. Open questions for the mathematician

1. Is the block structure of HF(a(1/n), gamma_i) (Section 5, inference) exact, giving special contribution to V(T(1/n)) of the form (geometric sum in t^2) times an n-independent polynomial? It would need the h-gradings of the arc generators, which [Cosm] does not print.
2. What determines the slope s of the rational component in Seifert framing (the determinant identity suggests a signed count of special lengths)? Likely treated in KWZ "Khovanov homology and strong inversions" (arXiv:2104.13592), not read here.
3. Is there a Khovanov analogue of conjugation symmetry or any duality pairing special components of one slope?
4. Are same-slope special components always in consecutive delta-gradings for cap-trivial tangles?
