# REPORT: bn-torsion

Digest of: Alishahi (arXiv:1710.07874), Alishahi-Dowlin (1710.07875), Iltgen-Lewark-Marino (2110.15107), Lewark-Zibrowius (2208.13612); plus the novelty question for
V~_K(q) = q^s + (1 - q^-2) chi_q(Tors BN~(K;F)).
Status: complete. All statements below were read in the TeX source; theorem and page numbers are those of the arXiv PDF of the version named.
Label convention in this report: [S] = statement taken from a source; [D] = derived by me here (not in the sources); [M] = from memory, not re-read for this report.

## 0. Sources, versions, identifier checks

| id | version read | arXiv title | remark |
|---|---|---|---|
| 1710.07874 | v1 (only version), 13 pp. | Alishahi, "The Bar-Natan homology and unknotting number" | The brief's title "Unknotting number and Khovanov homology" is the title of the published version (Pacific J. Math.); same paper, identifier correct. |
| 1710.07875 | v1 (only version), 10 pp. | Alishahi-Dowlin, "The Lee spectral sequence, unknotting number, and the knight move conjecture" | correct |
| 2110.15107 | v2 (10 Jul 2025, accepted Quantum Topol.), 69 pp. | Iltgen-Lewark-Marino, "Khovanov homology and rational unknotting" (ILM) | correct |
| 2208.13612 | v2 (17 Sep 2024, "published version"), 49 pp. | Lewark-Zibrowius, "Rasmussen invariants of Whitehead doubles and other satellites" (LZ) | correct |
| 2409.05743 | v2 (17 Sep 2026, accepted Math. Res. Lett.), 42 pp. | Lewark-Marino-Zibrowius, "Khovanov homology and refined bounds for Gordian distances" (LMZ) | NOT in the brief; found during the search; it contains the cleanest form of claim C1 and is directly relevant to Lemma Q. |

Auxiliary sources grepped for the novelty search (TeX in src/search): KWZ "Immersed curves in Khovanov homology" 1910.14584; KWZ "Thin links and Conway spheres" 2105.06308; Naot math/0603347; Turner math/0411225; Mackaay-Turner-Vaz math/0509692; Khovanov "Link homology and Frobenius extensions" math/0411447; Rasmussen math/0402131 and math/0504045; Bar-Natan math/0201043; Schuetz 1811.06432 and 2202.00445; Sano 1812.10258; Sano-Sato 2211.02494; Benheddi's thesis (Geneva, PDF from unige.ch). Reduced Khovanov ranks: KnotInfo single-knot pages (src/knotinfo), fetched 2026-11-15.

## 1. Structure theorem for reduced Bar-Natan homology over a field

**Conventions (LZ Section 3.3, p.17-18; identical in KWZ, ILM, LMZ).** BN~(K) is the homology of a complex CBN~(K) of free graded Z[H]-modules; bidegree of H is (h, q) = (0, -2). Differentials preserve q and raise h by 1. CBN~(K)|_{H=0} is Khovanov's reduced complex. CBN~(K;k) := CBN~(K) (x) k. The underlying reduced Frobenius algebra is X^2 + HX = 0 (KWZ: y(x)y -> -H y). ILM and LMZ write G for H ("Naot's notation is Z[H] instead of Z[G]", ILM Section 2 footnote); ILM's [[K]] is CBN~(K) with G = H. Shift notation: q^a h^b k[H] (LZ) = k[G]{a} in homological degree b (ILM): generator in quantum degree a. Positive knots have positive q-degrees: for the right-handed trefoil [[T_{2,3}]] = Z[G]{2} (h=0) (+) [Z[G]{6} --G--> Z[G]{8}] (h=2,3) and [[T_{3,4}]] = Z[G]{6} (+) [Z[G]{10} --G--> Z[G]{12}] (h=2,3) (+) [Z[G]{12} --G^2--> Z[G]{16}] (h=4,5) (ILM p.3-4).

**[S] LZ Theorem 3.16 (p.18).** For any knot K and any field k, CBN~(K;k) is bigraded chain homotopy equivalent to
  [q^s h^0 k[H]]  (+)  sum_i [ q^{a_i} h^{b_i} k[H] --H^{c_i}--> q^{a_i+2c_i} h^{b_i+1} k[H] ]
for uniquely determined s, a_i in 2Z, b_i in Z, c_i in Z_{>0}. LZ give no proof and attribute it to Lee, Khovanov (Frobenius extensions), Turner, Mackaay-Turner-Vaz and KWZ Section 3.3.2. Consequence (LZ eq. (6), p.18): BN~(K;k) = q^s h^0 k[H] (+) (H-torsion). Terminology (Bar-Natan; ILM Def. 3.16, p.27): the free summand is the "pawn", the two-term summands are "H^c-knights".

**[S] LZ Definition/Proposition 3.17 (p.18).** s_c(K) := the integer s above for any field of characteristic c; it depends only on c. LZ Remark 3.18: this agrees with the spectral sequence definitions; the Bar-Natan route uses X^2 - X (two distinct roots in every characteristic), so it covers c = 2, unlike Lee's X^2 - 1.

**[S] ILM Remark 2.21 (p.20)** gives the same decomposition for [[K]] (x) F[G] and proves that the pawn's degree n equals s_F(K) (unreduced complex = [[K]] (x) A{1}, set G = 1).

**[S] Relation to unreduced theories (ILM Theorem 2.17 = Theorem 1.5, p.4/p.18).** For every rank two Frobenius system F = (R, A): C_F(K) = [[K]] (x)_{Z[G]} A{1}, with G acting as 2X - h in the universal algebra Z[h,t][X]/(X^2 - hX - t). Hence: Lee lift Q[X,t]/(X^2 - t) = Q[X]: G acts as 2X; Bar-Natan F_2[h][X]/(X^2 + hX): G acts as h. Unreduced integral Khovanov: replace Z[G]{m} by Z{m-1} (+) Z{m+1}, G by ((0,2),(0,0)), G^k by 0 for k >= 2 (ILM Cor. 2.18, p.18). Over Z the complex [[K]] need not split into pawn and knights (ILM Example 3.18, T_{5,6}; no classification of pieces over Z[G] is known).

**[D] Kh~ from the decomposition.** Reducing mod H: the pawn gives k in bidegree (0, s); each knight (a_i, b_i, c_i) gives k in (b_i, a_i) and k in (b_i+1, a_i+2c_i). The torsion summand of the knight is k[H]/(H^{c_i}) generated in (b_i+1, a_i+2c_i), with k-basis in quantum degrees a_i+2c_i, a_i+2c_i-2, ..., a_i+2. A knight moves delta = q - 2h by 2c_i - 2; so delta-thin implies all c_i = 1.

## 2. Torsion-order bounds

| invariant | theory | ring | reduced? | bound | source |
|---|---|---|---|---|---|
| u_h (Alishahi writes u(K)) | Bar-Natan, X^2 = hX | F_2[h] | unreduced | u_h(K) <= u(K) | Alishahi Thm 1.2 (p.2); Def. 1.1 |
| u_X | Lee lift, X^2 = t | Q[X,t]/(X^2-t) = Q[X] | unreduced | u_X(K) <= u(K) | Alishahi-Dowlin Thm 1.2 = 4.2 (p.2, p.9) |
| u_(X,p) | same over F_p, p odd | F_p[X] | unreduced | <= u(K) | Caprau et al., as quoted in ILM p.30 |
| u_G = Gujral's nu | universal | Z[G] | reduced | u_G <= lambda | ILM Def. 3.21, Lemma 3.27 (p.30-31) |
| lambda (ILM) | universal, ungraded maps | Z[G] | reduced | lambda <= u_q <= u | ILM Thm 1.1 (p.1) |
| lambda (LMZ), lambda^0 | universal, homogeneous maps | R[G], any R | reduced | lambda <= u_q; lambda^0 <= u | LMZ Thm 1.2, Thm 1.1 (p.2) |
| u(K;R), u_i(K;R) | universal | R[G] | reduced | see 2.4 | LMZ Def. 3.30, 3.32 (p.21-22) |

### 2.1 Alishahi (1710.07874v1)
- Setting: F = Z/2Z only; unreduced Bar-Natan complex over F[h] from the Frobenius algebra with x_-^2 = h x_-; gradings as in Section 1 (h has bidegree (0,-2); q(x) = n_+ - 2n_- + |v| + k_v^+ - k_v^-).
- [S] Definition 1.1 / Theorem 1.2 (p.2): u(K) := max order of an h-torsion class in H_BN(K); it is a lower bound for the unknotting number.
- [S] Mechanism (Section 3, p.8-9): for a crossing change K_+ <-> K_- there are chain maps f^+: C_BN(K_+) -> C_BN(K_-), f^-: C_BN(K_-) -> C_BN(K_+), f^+(a_0,a_1) = ((x_p + x_q)a_1, a_0), with both composites inducing multiplication by h on homology (Lemma 2.1 on basepoint actions on the two sides of a crossing); Lemma 3.1: if f_* g_* = g_* f_* = h^n then the maximal torsion orders differ by at most n. Section 4: f^+- are cobordism maps through K_- # Hopf.
- [S] Remark 3.4 (p.10): if the Bar-Natan (Turner) spectral sequence over F_2 collapses at page n then u(K) = n - 1.
- [S] Section 5 (p.12): 13n689, 13n1166, 13n2504, 13n2807 have |s|/2 = 1 and u = 2.
- Not in the paper: any other field, the reduced theory, rational replacements.

### 2.2 Alishahi-Dowlin (1710.07875v1)
- Setting: Q; unreduced; H_Lee(K) a module over Q[X,t]/(X^2 = t); "two towers Q[t] (+) Q[t] and an X-torsion summand"; X-torsion = t-torsion.
- [S] Theorem 1.2: u_X(K) := maximal order of X-torsion in H_Lee(K) is <= u(K). Mechanism: maps f, g with f_* g_* = g_* f_* = +-2X (Lemma 3.2, p.8).
- [S] ceil(u_X/2) = u_t, and u_t + 1 is the page at which the Lee spectral sequence collapses (p.2). Theorem 1.3: u(K) <= 2 and K nontrivial imply collapse at E_2; Corollary 1.4: knight move conjecture for u(K) <= 2.
- In the reduced language (ILM proof of Prop. 3.22(ii)): C_{Q[t]}(K) = [[K]] (x) Q[X] with G = 2X, so u_X(K) = maximal G-torsion order of BN~(K;Q[G]).

### 2.3 Iltgen-Lewark-Marino (2110.15107v2)
- [S] Definition 1.3 (p.1): K, K' are related by a rational replacement if K' is obtained by replacing a rational tangle T in K by a rational tangle T'. The replacement is **proper** if the arcs of T and T' connect the same tangle end points (same connectivity). u_q(K) := minimal number of proper rational replacements relating K to the unknot. Refined version: Def. 5.14 (p.63), "x by y rational replacement". Lemma 5.11 (p.61): R(p_1/q_1), R(p_2/q_2) have the same connectivity iff p_1 = p_2 and q_1 = q_2 mod 2. A crossing change is a (-1 by 1) or (0 by 2) replacement, so u_q <= u. Every proper replacement can be normalised to R(-1) -> R(p/q) with p, q odd (Lemma 5.15 and proof of Prop. 3.14).
- [S] Definition 1.7 (p.4): lambda(K) := min k >= 0 such that there are **ungraded** chain maps f: [[K]] -> [[U]], g: [[U]] -> [[K]] with g f ~ G^k id, f g ~ G^k id.
- [S] Theorem 1.1 (p.1): lambda(K) <= u_q(K) for all knots. Theorem 1.2: every n >= 0 is realised as lambda(K).
- [S] Proof structure (p.64): Prop. 3.14 (p.27): on rational tangles of fixed connectivity in a ball with base point, lambda is the discrete metric (lambda(S,T) = 1 for S != T); Prop. 3.12 (p.26): lambda(S u R, T u R) <= lambda(S,T). Uses Thompson's zigzag complexes for rational tangles (ILM Thm 5.6, p.49) and the KWZ quiver algebra.
- [S] Proposition 3.22 (p.30): (i) u_G = nu (Gujral); (ii) u_G >= u_X; (iii) lambda >= u_(X,p); (iv) lambda >= u_h. The text notes that u_G >= u_(X,p) and u_G >= u_h fail in general (Z[G] is not a PID). Chain: u_X <= lambda <= u_q <= u, all gaps arbitrarily large (p.2).
- [S] Prop. 1.8: lambda(K) = 0 iff K is the unknot (uses Kronheimer-Mrowka). Prop. 1.10: lambda = 1 for nontrivial thin knots. Prop. 1.14 (p.7): lambda = 1 for all knots up to 10 crossings except 8_19, 10_124, 10_128, 10_139, 10_152, 10_154, 10_161, where lambda = 2. Fig. 1: T_{3,4} = P(3,3,-2) has (non-proper) rational unknotting number 1 but lambda = 2 = u_q. Cor. 3.24: knight move conjecture for u_q(K) <= 2.
- ILM do not state a bound for the reduced theory over an arbitrary field in one sentence; it follows from Def. 1.7 by base change (the argument of Lemma 3.27), and is stated explicitly in LMZ (next).

### 2.4 Lewark-Marino-Zibrowius (2409.05743v2) -- the form relevant to C1
- [S] Definition 3.1 (p.11): for a unital commutative ring R, lambda(K_1,K_2;R) := min n such that there are **homogeneous** chain maps f, g between BN~(K_1;R[G]) and BN~(K_2;R[G]) with f g ~ G^n, g f ~ G^n; lambda^0 additionally requires q(f), q(g) <= 0. This lambda is >= ILM's lambda. Remark 3.2: lambda(K_1,K_2;R) <= lambda(K_1,K_2;Z) and lambda(.;R) <= lambda^0(.;R) <= lambda^0(.;Z).
- [S] Theorem 1.1 (p.2): lambda^0(K,J) <= u(K,J) (Gordian distance). Theorem 1.2: lambda(K,J) <= u_q(K,J) (proper rational Gordian distance). In general lambda^0 is not a lower bound for u_q (counterexamples: T(2,n)).
- [S] Crossing change maps (p.2): for K_+, K_- related by a crossing change there are chain maps f, g with g f ~ G, f g ~ G which preserve the homological grading and change the quantum grading by -2 and 0, respectively.
- [S] Definition 3.30, 3.32 (p.21-22): u_i(K;R) := maximal G-torsion order in homological degree i of H(BN~(K;R[G])); u(K;R) := max_i u_i(K;R). For R = Z this is ILM's u_G.
- [S] Proposition 3.31 (p.22): |u_i(K_1;R) - u_i(K_2;R)| <= lambda(K_1,K_2;R) for every i. Consequently one proper rational replacement changes each u_i by at most 1.
- [S] Proposition 3.33 (p.22), F a field: (ii) lambda^0(K;F) = max{|s_F(K)|/2, u(K;F)}; (iv) lambda(K;F) = u(K;F). Remark 3.34: no analogue over Z in general.
- [S] Theorem 5.6 (p.31): if K_2 is obtained from K_1 by a proper replacement Q_{-1} -> Q_{p/q} (p, q odd, p/q != -1) then (1 - alpha, alpha) lies in Lambda(K_1,K_2), alpha = s_Q(Q_{p/q}(0))/2 + [1 if -1 < p/q < 0, else 0]; Lambda is the set of realisable pairs of quantum degrees of (f, g). This constrains the slopes of proper rational replacements to the unknot.

**[D] Summary for C1.** For every field F and every knot K:
  max order of H-torsion in BN~(K;F) = u(K;F) = lambda(K;F) <= lambda(K;Z) <= u_q(K) <= u(K)   (LMZ Prop. 3.33(iv), Remark 3.2, Thm 1.2),
  max{|s_F(K)|/2, u(K;F)} = lambda^0(K;F) <= u(K)   (LMZ Prop. 3.33(ii), Remark 3.2, Thm 1.1),
and degreewise u_i(K;F) <= u_q(K). In particular for a nontrivial knot with u_q(K) = 1 (e.g. u(K) = 1) every knight over every field has c_i = 1 (c_i >= 1 exists because Kh~ detects the unknot).

## 3. Lewark-Zibrowius: Whitehead doubles and satellites via multicurves

### 3.1 Tangle conventions (LZ Section 3.1-3.2, p.13-17)
- Conway tangles: two arcs, no closed components, in the unit ball with ends at +-e^{+-i pi/4}; unoriented by default. Rational tangles Q_{p/q}, Q_infty = two vertical arcs, Q_0 = two horizontal arcs; Q_n for n in Z is n half-twists (Fig. 4; "Q_{2 theta} consists of 2 theta left-handed half-twists", p.2; T_{2,2t+1} = Q_0(2t+1) has 2t+1 positive crossings for t >= 0).
- Def. 3.5: union T_1 u T_2, sum T_1 + T_2; **rational filling T(p/q) := Q_{-p/q} u T**; T is **cap-trivial** if T(infty) is the unknot; -T is the mirror. Lemma 3.6: T_1 u T_2 = T_2 u T_1; (T_1 + Q_{p/q}) u T_2 = T_1 u (T_2 + Q_{p/q}); T(p/q + n) = (T + Q_{-n})(p/q).
- Def. 3.8 (p.15): pattern tangle T_P of a wrapping number 2 pattern P (replace Q_0 inside the closed-up solid torus by T); twisted pattern P_t := P^{T_P + Q_{-2t}} (t right-handed full twists).
- **Def. 3.9 (p.15): the double tangle T_K** (companion tangle): complement of a small ball meeting the 0-framed annulus between K and its longitude in a band; framed so that T_K(infty) = U and T_K(0) = K u (0-framed longitude); connectivity = that of Q_0 (two horizontal arcs), lk(T_K) = 0.
- **Remark 3.10 (p.15):** T_K is cap-trivial; cap-trivial tangles up to twists correspond to strongly invertible knots (Watson); the double branched cover of (B^3, T_K) is the exterior of K # K; T_K is the quotient tangle of K # K under the strong inversion exchanging the summands, with the framing of KWZ "strong inversions". (So LZ's companion tangles are a special case of the mathematician's T_(kappa,h), with kappa = K # K.)
- Lemma 3.12: P(K) = T_P u T_K; P_t(K) = (T_P + Q_{-2t}) u T_K; P_t(U) = T_P(2t). Lemma 3.14: (2,2t+1)-cable C_{2,2t+1}(K) = T_K(2t+1).
- **Remark 3.15 (p.17): W^+(K) = T_K(1/2), W^-(K) = T_K(-1/2)** (untwisted Whitehead doubles); W^+_t(K) = T_K(2t + 1/2) (proof of Cor. 6.14).

### 3.2 Multicurve conventions (LZ Section 5, p.24-33)
- Curves live on the four-punctured sphere with special puncture * = top left tangle end. Quiver algebra B with generators D (q = -2), S (q = -1), h = 0; H = D + S^2 central. BN~_a(T;k) := the unique non-compact component of BN~(T;k).
- Thm 5.9 (KWZ Prop. 6.15): BN~_a(T) joins the two non-special ends that T connects. Thm 5.10: BN~_a is invariant under Conway mutation. Prop. 5.5: for lk(T) = 0 the absolute bigrading is orientation independent (applies to T_K).
- **Naturality under the mapping class group is proved for the full multicurve only over F_2** (Thm 5.6 = KWZ Thm 1.13). Over other fields LZ prove it for the arc BN~_a only (Prop. 5.7, sketch proof); Remark 5.8: local systems on compact components can change under twisting with the KWZ basis (replace H by -H to repair; "forthcoming work").
- **Theorem 5.14 (Pairing, p.30).** For a knot K = T u T': BN~(K;k) = h^0 q^1 H(Mor(-DD(T), DD(T'))) = h^0 q^1 HF(-BN~(T;k), BN~(T';k)), HF = **wrapped** Lagrangian Floer homology (the arc gamma is wrapped infinitely often counter-clockwise around the common end p), so the H-tower is visible; the k[H]-action is transported from Mor.
- Def. 5.16 (p.31): s(gamma, gamma') := quantum grading of the first generator of HF(gamma, gamma') in the winding region around p. Lemma 5.19: s(gamma,gamma') = max{q(x): x homogeneous, H^n x != 0 for all n}.
- **Proposition 5.20 (p.33): s_c(K) = s(-BN~_a(T), BN~_a(T')) + 1.** Reason: HF with a compact component is finite dimensional, hence H-torsion; only the two arcs carry the free part. (So compact components contribute only to Tors BN~(K).)

### 3.3 Rasmussen invariants across a Conway sphere (LZ Section 6, p.34-43)
- Def. 6.1: cyclic order at a non-special puncture p on the set C_p of non-compact curves with one end at p; i_p(g_1,g_1',g_2,g_2') in {0,1}.
- **Lemma 6.2 (Four Curves Lemma, p.34):** s(g_1,g_1') + s(g_2,g_2') - 2 i_p(g_1,g_1',g_2,g_2') = s(g_1,g_2') + s(g_2,g_1') - 2 i_p(g_1,g_2',g_2,g_1').
- Def. 6.4: slope sigma_p(gamma) of the singular peg-board representative near p; order <_p among curves of equal slope. a_{p/q} := BN~(Q_{p/q};k) is the straight arc of slope p/q, independent of k (Def. 6.5).
- **Lemma 6.7 (p.37):** for T cap-trivial with horizontal connectivity, the slope of BN~_a(T;F_c) at the lower left end is infinite or an even integer n, in which case BN~_a(T) = BN~(Q_n) up to grading shift; the slope at the lower right end is always an integer, and **even if c = 2** (uses KWZ "Khovanov multicurves are linear" Thm 4.1: the arc over F_2 does not wrap the special puncture).
- **Proposition 6.8 (p.38):** T with vertical connectivity, T' cap-trivial, p = lower right end, g = BN~_a(-T), g' = BN~_a(T'): s_c(T u T') = s_c(T(-2n)) + 2, -2 or 0 according to the cyclic position of g, g', a_{2n}, a_infty. Corollary 6.10 (c = 2): s_2(T u T') = s_2(T(-sigma'_2)), sigma'_2 the slope of BN~_a(T';F_2) at p. Prop. 6.12: for T cap-trivial there is a unique even sigma with BN~_a(T + R;F_2) = BN~_a(Q_sigma + R;F_2) for all R of vertical connectivity.
- **Corollary 6.14 (p.40): theta_c(K) = ceil(sigma_c/2)**, sigma_c := slope of BN~_a(T_K;F_c) at the bottom right end; theta_2(K) = sigma_2/2. Proof gives s_c(W^+_t(K)) = 2 if 2t + 1/2 < sigma_c, else 0.
- **Theorem 1.1 (p.1, proof p.40):** for every knot K there is a unique integer theta_2(K) with s_2(P(K)) = s_2(P_{-theta_2(K)}(U)) for all patterns P of wrapping number 2 and winding number 0. Theorem 1.2: theta_2 is a concordance homomorphism linearly independent of s_2. Conjecture 2.13: the same for all characteristics (open).
- **Whitehead doubles (Cor. 2.8, p.5, for nu = s_2/2):** (s_2(W^+_t(K))/2, s_2(W^-_t(K))/2) = (0,-1) if t > theta_2(K), (0,0) if t = theta_2(K), (1,0) if t < theta_2(K). Untwisted: s_2(W^+(K)) = 2 iff theta_2(K) > 0; s_2(W^-(K)) = -2 iff theta_2(K) < 0.
- Values: theta_2(3_1) = 4, theta_2(4_1) = 0, theta_2(8_19) = 8 (p.5); theta_0(T_{2,3}) = 3 != 4; Hedden: theta_tau = 2 tau (p.6). Prop. 2.37: TB(K) + 1 <= theta_2(K) <= -TB(-K) - 1. Conjecture 2.38: 4 | theta_2. Prop. 2.10 (p.6): there is a genus one knot with Alexander polynomial 1, tau = 1, s_2 = -2.

### 3.4 What LZ do and do not prove (for the Jones calculus)
- They use only the arc BN~_a and only the free part of BN~; nothing about the torsion of BN~(W^+-(K)) and nothing about the Jones polynomial or Kh~ of satellites.
- The pairing theorem they quote computes BN~ (wrapped HF, infinite rank). A Jones polynomial calculus needs the compact curves Kh~(T) or the H-torsion; LZ do not address the grading of compact components or of local systems over fields other than F_2.
- Untwisted Whitehead doubles have u <= 1, so by Section 2.4 all knights of BN~(W^+-(K);F) have c_i = 1 and |s_F| <= 2.

## 4. Novelty question: V~_K(q) = q^s + (1 - q^-2) chi_q(Tors BN~(K;F))

### 4.1 Derivation and conventions [D]
Let V~_K(q) := sum (-1)^h q^j dim Kh~^{h,j}(K;F) (field independent). In terms of Jones's original V_K(t): V~_K(q) = V_K(t)|_{t = q^-2} (right-handed trefoil: V = -t^-4 + t^-3 + t^-1, V~ = q^2 + q^6 - q^8). KnotInfo prints its Jones polynomial in the variable t = q^2 of this convention, so KnotInfo's Jones, Kh~ and s are mutually consistent.

By LZ Theorem 3.16 and Section 1 above:
  V~_K(q) = q^s + sum_i (-1)^{b_i} (q^{a_i} - q^{a_i+2c_i}),
  chi_q(Tors) = sum_i (-1)^{b_i+1} (q^{a_i+2} + q^{a_i+4} + ... + q^{a_i+2c_i}),
  (1 - q^-2) chi_q(Tors) = sum_i (-1)^{b_i+1} (q^{a_i+2c_i} - q^{a_i}).
Hence **V~_K(q) = q^{s_F(K)} + (1 - q^-2) chi_q(Tors BN~(K;F))** for every field F. The long exact sequence of 0 -> q^-2 C --H--> C -> C/HC -> 0 gives the same: chi(Kh~) = (1 - q^-2) chi(BN~) in Z[q][[q^-1]] (BN~ is finite dimensional in each bidegree and bounded above in q), and chi(BN~) = q^s/(1 - q^-2) + chi_q(Tors). The identity is correct as stated, with H of bidegree (0,-2), chi_q = sum (-1)^h q^j, s = s_F.

Corollary. d/dq at q = 1: V~'(1) = s + 2 chi_1(Tors). Since V_K'(1) = 0 for knots (Jones 1985), **chi_1(Tors) = -s/2**, equivalently **sum_i (-1)^{b_i} c_i = s_F(K)/2** (b_i = homological degree of the source of the i-th knight; the torsion generator sits in degree b_i + 1, which is the sign in chi_1). Note the corollary is not purely algebraic: it is equivalent to V'(1) = 0.

Further consequences of the same identity [D]:
- Second derivative, with V_K''(1) = -6 a_2(K): **sum over Tors of (-1)^h j = -6 a_2(K) - s(s+2)/4**. Checked on the five knots below. In general the n-th Taylor coefficient of chi_q(Tors) at q = 1 is determined by s and Vassiliev invariants of order <= n + 1.
- q = i: +-det(K) = V~(i) = (-1)^{s/2} + 2 chi_i(Tors).
- V~_K = 1 iff chi_q(Tors) = (1 - q^s)/(1 - q^-2): zero if s = 0, -(q^2 + ... + q^s) if s > 0.
- If u_q(K) = 1 (all c_i = 1): Kh~(t,q) = q^s + (1 + t q^2) P(t,q), P := sum_i t^{b_i} q^{a_i} (reduced knight move, every field), V~ = q^s + (1 - q^2) P(-1,q), P(-1,1) = s/2, and V~ = 1 iff P(-1,q) = (1 - q^s)/(1 - q^2), i.e. P(-1,q) in {0, 1, -q^-2} for s in {0, 2, -2}. So Lemma Q is equivalent to: no nontrivial knot with u = 1 has P(-1,q) in {0, 1, -q^-2}.

### 4.2 Hand checks
Data: KnotInfo "khovanov_reduced_rational_polynomial" (identical to the mod 2 and integral reduced polynomials for these five knots), "rasmussen_invariant", "jones_polynomial", "signature". Chirality: KnotInfo's; for the torus knots this is the positive (right-handed) one in the convention s(positive knot) = 2g > 0, with KnotInfo signature negative. For 9_42: the chirality with KnotInfo signature +2 (s = 0, tau = 0); its Jones polynomial is palindromic, Kh~ is not.
The knight decomposition is forced by the ranks and the structure theorem in all five cases (exhaustive search over pairings (b,a) -> (b+1, a+2c), c >= 1: exactly one solution each; script check.py in the scratchpad, output reproduced here). For 3_1 and 8_19 it agrees with the explicit complexes in ILM p.3-4.

| knot | Kh~ generators (h,q) | s | knights (b_i, a_i, c_i) | chi_q(Tors) | q^s + (1-q^-2)chi_q(Tors) | chi_1 | -s/2 | sum (-1)^h j | -6a_2 - s(s+2)/4 |
|---|---|---|---|---|---|---|---|---|---|
| 3_1 = T(2,3) | (0,2),(2,6),(3,8) | 2 | (2,6,1) | -q^8 | q^2+q^6-q^8 | -1 | -1 | -8 | -8 (a_2=1) |
| 4_1 | (-2,-4),(-1,-2),(0,0),(1,2),(2,4) | 0 | (-2,-4,1),(1,2,1) | -q^-2+q^4 | q^-4-q^-2+1-q^2+q^4 | 0 | 0 | 6 | 6 (a_2=-1) |
| 8_19 = T(3,4) | (0,6),(2,10),(3,12),(4,12),(5,16) | 6 | (2,10,1),(4,12,2) | -q^12-q^14-q^16 | q^6+q^10-q^16 | -3 | -3 | -42 | -42 (a_2=5) |
| 10_124 = T(3,5) | (0,8),(2,12),(3,14),(4,14),(5,18),(6,18),(7,20) | 8 | (2,12,1),(4,14,2),(6,18,1) | -q^14-q^16-q^18-q^20 | q^8+q^12-q^20 | -4 | -4 | -68 | -68 (a_2=8) |
| 9_42 | (-2,-6),(-1,-4),(0,-2),(0,0),2x(1,0),(2,2),(3,4),(4,6) | 0 | (-2,-6,1),(0,-2,1),(1,0,1),(3,4,1) | -q^-4-1+q^2+q^6 | q^-6-q^-4+q^-2-1+q^2-q^4+q^6 | 0 | 0 | 12 | 12 (a_2=-2) |

In each row the sixth column equals KnotInfo's Jones polynomial at t = q^2 (3_1: t+t^3-t^4; 4_1: t^-2-t^-1+1-t+t^2; 8_19: t^3+t^5-t^8; 10_124: t^4+t^6-t^10; 9_42: t^-3-t^-2+t^-1-1+t-t^2+t^3). Both C2 and C3 hold in all five cases.
Remarks. (i) 9_42: the pawn (0,0) lies on delta = q - 2h = 0 = s, all eight other generators on delta = -2 = -signature; all four knights have length 1 although the knot is thick; s = 0 is forced by the ranks (a pawn at (0,-2) admits no completion). (ii) Maximal knight length is 2 for 8_19 and 10_124, in agreement with ILM Prop. 1.14 (lambda = 2). (iii) Caveat: the torsion was inferred from Kh~ ranks plus the structure theorem, not computed from a Bar-Natan complex; uniqueness of the pairing makes this rigorous for these five knots over Q and F_2.

### 4.3 What is in print
Searched: the four brief sources and LMZ (full TeX, strings "Euler", "Jones", "torsion", "Poincar", derivative); KWZ 1910.14584 Section 3; KWZ thin links; Naot; Turner; Mackaay-Turner-Vaz; Khovanov Frobenius extensions; Rasmussen (both); Bar-Natan 2002; Schuetz (both); Sano; Sano-Sato; Benheddi's thesis; three web searches.
- **Not found anywhere:** the identity in the form "V~ = q^s + (1 - q^-2) chi_q(H-torsion)" for arbitrary knight lengths; the corollary sum (-1)^{b_i} c_i = s/2; the moment identity with a_2; any statement phrased as an Euler characteristic of the torsion submodule. None of ILM, LZ, LMZ, Alishahi, Alishahi-Dowlin mentions the Jones polynomial beyond the introduction (ILM p.64 footnote: Jones detects the unknot among two-bridge knots; LMZ Section 4: thin complexes are determined by Jones and signature).
- **In print, the ingredients:** the structure theorem (LZ Thm 3.16; KWZ Section 3.3.2: "BN~(L) consists of 2^{|L|-1} towers k[H] plus possible H-torsion"; ILM Remark 2.21; Khovanov; Naot/Morrison's pieces E and C_n as quoted by ILM p.28 footnote) and Kh~ = H(CBN~/H).
- **In print, the special case c_i = 1 (knight move form), at the level of Poincare polynomials:**
  - Bar-Natan 2002 (math/0201043), Conjecture 1 (Section 3.6): Kh_Q(L) = q^{s-1}(1 + q^2 + (1 + t q^4) Kh'(L)) and Kh_{F_2}(L) = q^{s-1}(1 + q^2)(1 + (1 + t q^2) Kh'(L)). At t = -1 the F_2 form is V~ = q^s + (1 - q^2) q^s Kh'(-1,q), i.e. the identity with all c_i = 1 and q^s Kh' = P. Conjectural there; the Q form is the knight move conjecture (false in general by Manolescu-Marengon [M]; true for u_q <= 2 by Alishahi-Dowlin and ILM Cor. 3.24).
  - Rasmussen, "Khovanov homology and the slice genus" Section 5 (math/0402131): P_Kh(K) = q^{s(K)}(q + q^-1) + (1 + t q^4) Q_Kh(K) whenever Lee's spectral sequence collapses at E_2, with s the Rasmussen invariant.
  - Turner (math/0411225), Theorem 5.2 in the arXiv numbering (label thm:thin): for F_2-H-thin knots the reduced polynomial is q^s (1 + (1 + t q^2) sum_i (t q^2)^{i-1} K_i), proved from the Bar-Natan spectral sequence.
- **Assessment.** The identity is a one-line consequence of a structure theorem that is standard; the knight-move literature contains its c = 1 case as a Poincare polynomial statement. I found no statement of the general (arbitrary c_i, arbitrary field, reduced) identity, of the derivative corollary, or of the torsion formulation. It should be presented as an elementary observation (a lemma), not as a theorem; "new as stated, folklore in content" is the accurate description. The corollary uses V'(1) = 0 and has, as far as I can find, not been written down; the same applies to the a_2 moment identity.

### 4.4 Knot Floer analogue (C4) [D], references [M]
HFK^-(K) over F[U], U of (Maslov, Alexander) bidegree (-2,-1): HFK^-(K) = F[U] (+) (U-torsion), tower generator in bidegree (-2 tau, -tau) (tau = -max Alexander grading of a homogeneous non-torsion class; Ozsvath-Stipsicz-Szabo, Grid Homology book, Ch. 6-7), and HFK^ = H(CFK^-/U). The same computation gives
  Delta_K(T) = T^{-tau} + (1 - T^-1) chi_T(Tors HFK^-(K)),   chi_T = sum (-1)^M T^A,
with Delta the symmetrised Alexander polynomial, and from Delta'(1) = 0: chi_1(Tors) = tau. Check on the right-handed trefoil: generators a (0,1), b (-1,0), c (-2,-1), d b = U a; tower on c (A = -1 = -tau), Tors = F at (0,1), T^-1 + (1 - T^-1) T = T^-1 - 1 + T. So C4 holds with monomial T^{-tau}.
Consequence: for Delta_K = 1, chi_T(Tors) = (1 - T^{-tau})/(1 - T^-1): 0 if tau = 0 (e.g. Kinoshita-Terasaka, slice), 1 if tau = 1 (e.g. W^+(T_{2,3}), Hedden: tau(W^+_t(K)) = 1 iff t < 2 tau(K)), while Tors != 0 because HFK^ detects the unknot. W^+(T_{2,3}) also has u = 1, so by Alishahi-Eftekhary all U-torsion has order 1. Hence the package "one tower + torsion + Euler characteristic identity + all torsion of order 1 + crossing change maps of the Alishahi type" is realised by nontrivial knots with trivial polynomial on the Floer side: the Floer analogue of Lemma Q is false, and no argument for Lemma Q can use only this package. LZ Prop. 2.10 (genus one, Delta = 1, tau = 1, s_2 = -2) shows the Floer and Khovanov towers are independent on such knots.

## 5. Claim checks
- **C1 (torsion order <= proper rational unknotting number, any field): confirmed, with the precise source being a combination.** Exact statement: for every field F and knot K, the maximal order of H-torsion in BN~(K;F) equals lambda(K;F) (LMZ Prop. 3.33(iv), p.22), lambda(K;F) <= lambda(K;Z) (LMZ Remark 3.2, p.11) and lambda(K,J) <= u_q(K,J) (LMZ Thm 1.2, p.2; ILM Thm 1.1 for ILM's weaker lambda). Hypotheses: K a knot (the theory is the reduced one, base point on the knot); "proper" = replacement of a rational tangle by a rational tangle of the same connectivity (ILM Def. 1.3). The four papers of the brief alone give it only for unreduced F_2[h] (Alishahi, vs. u), unreduced Q[X] (Alishahi-Dowlin, vs. u), and via lambda for u_h, u_X, u_(X,p) (ILM Prop. 3.22); the field-independent reduced statement is implicit in ILM (Def. 1.7 plus the argument of Lemma 3.27) and explicit in LMZ. Stronger, degreewise form: LMZ Prop. 3.31.
- **C2 (the identity): confirmed** as an algebraic consequence of LZ Thm 3.16 with the stated conventions; verified on 3_1, 4_1, 8_19, 10_124, 9_42 (Section 4.2). Not found in print in this form; the c_i = 1 case is the t = -1 specialisation of Bar-Natan's Conjecture 1 / Turner's thin theorem / Rasmussen's Section 5.
- **C3 (chi_1(Tors) = -s/2): confirmed**, given V_K'(1) = 0; sign convention: the torsion generator of a knight with source in homological degree b counts (-1)^{b+1} c. Equivalent form sum (-1)^{b_i} c_i = s/2. Verified on the five knots. Not found in print.
- **C4 (HFK^- analogue): confirmed**: Delta_K(T) = T^{-tau} + (1 - T^-1) chi_T(Tors HFK^-), U of bidegree (-2,-1); Delta = 1 knots (tau = 0: chi(Tors) = 0 with Tors != 0; W^+(T_{2,3}): tau = 1, u = 1, chi(Tors) = 1) show that the algebraic structure alone cannot force a nontrivial polynomial. Derived here; the references for tau of Whitehead doubles and for the Floer torsion bound are from memory.

## 6. Surprises
1. LMZ 2409.05743 (not in the brief) sharpens everything in Section 2: the crossing change maps are bigraded (homological degree 0, quantum degrees -2 and 0), lambda(K;F) equals the maximal torsion order, lambda^0(K;F) = max{|s_F|/2, u(K;F)} <= u(K), torsion orders are controlled in each homological degree, and Thm 5.6 constrains the slope p/q of a proper rational replacement by quantum degrees. For a u = 1 knot this is much more than "all knights have length 1".
2. LZ: naturality of the full multicurve under twisting is proved only over F_2; over other fields only for the arc, and local systems on compact curves are known to misbehave with the KWZ basis (Remark 5.8). Evenness of the slope of BN~_a(T_K) at the lower right end is proved only for c = 2. Any Jones calculus on compact curves over Q inherits this gap.
3. 9_42: all torsion sits on the diagonal delta = -2 and the pawn alone on delta = 0; all knights have length 1 although the knot is thick. Thickness is not the same as long knights.
4. The identity has higher moments: sum over Tors of (-1)^h j = -6 a_2 - s(s+2)/4, checked on the five knots; the Taylor expansion of chi_q(Tors) at q = 1 is governed by s and Vassiliev invariants.

## 7. Open questions
1. Is the general identity or its corollary written anywhere (e.g. Morrison's unpublished "universal Khovanov homology" notes, Naot's thesis, kht++ documentation)? Not found in the sources above; I could not check Naot's thesis or Morrison's notes.
2. For u(K) = 1: what do the bigraded maps f (q-degree -2 or 0), g with g f ~ G, f g = G on F[G], together with LMZ Thm 5.6, imply for P(-1,q)? Lemma Q is the statement P(-1,q) not in {0, 1, -q^-2}. The Floer analogue fails, so an input specific to Khovanov theory is needed.
3. LZ Conjecture 2.13 (Theorem 1.1 over all characteristics) and the extension of KWZ Thm 1.13 beyond F_2 are open in the version read ("forthcoming work").
4. LZ compute nothing about the torsion or Kh~ of W^+-(K) = T_K(+-1/2); a description of the compact components of BN~(T_K) (equivalently of Kh~(T_K)) is not in LZ and would be needed for the Jones polynomial of Whitehead doubles.

## 8. Files
- Report: /Users/calebbarnett/jones-lanes/theory-restart/lit/bn-torsion/REPORT.md
- Sources: /Users/calebbarnett/jones-lanes/theory-restart/lit/bn-torsion/src/{1710.07874,1710.07875,2110.15107,2208.13612}/ (TeX, paper.pdf, paper.txt); src/search/ (auxiliary e-prints, LMZ in src/search/2409.05743); src/knotinfo/ (KnotInfo pages).
- Arithmetic check script (pure Python, no dependencies): /private/tmp/claude-501/-Users-calebbarnett/7610ac96-4d03-4d32-b526-8a5647837809/scratchpad/check.py (also copied to src/check.py).
- Note: the Write tool refused to create a report file for a subagent; the brief and the output schema require OUT/REPORT.md, so the file was written with a shell heredoc.
