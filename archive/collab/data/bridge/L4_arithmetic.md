# L4 — Arithmetic / number theory lens (Claude agent, started 2026-11-17 ~11:30)

Status: IN PROGRESS. Written continuously; later sections may be incomplete if the agent was cut off.

## 0. What is already in the project (read before proposing; do not duplicate)
- Codex `work/theory_restart/bridge_arithmetic.md` (17 Nov): (i) finite-field-zero translation of JC
  (V nonunit <=> V has a zero at a nonzero element of some finite field <=> some V(zeta_n) is a nonunit);
  (ii) Mahler measure alone defeated by 4_1 (V = t^-2 Phi_10, measure 1); (iii) Habiro integrality does not
  propagate J_2 = 1 to J_3 (formal H_0 = H_r = 1 model). I agree with all three and do not repeat them.
- SCAFFOLD U4 / letter 76: Mullins' formula (Casson invariant of Sigma_2 = log-derivative of V at t = -1 plus
  sigma/8) is ALREADY used: a_2 != 0 branch knots are covered for even n and all but one odd n. My first idea
  (Mullins + Casson surgery formula + signature constancy in antiparallel twist families) reproduces exactly this,
  so it is not new here. Recorded only as a calibration (section 1).
- SCAFFOLD U5-FROB5: fifth-root Sakuma identity V_S(q)^2 = 1 + d V_kappa(q) in F_16 (char-2 Frobenius arithmetic).

## 1. Calibration: the t = -1 jet is 3-manifold arithmetic (known)
For a knot L with det L = 1 (Sigma_2(L) a Z-homology sphere), with Casson normalisation lambda(Sigma(2,3,5)) = -1:
    lambda(Sigma_2(L)) = sigma(L)/8 - V_L'(-1) / (12 V_L(-1))        (Mullins 1993)
Checked by hand: T(3,5) has V = t^4 + t^6 - t^10, V(-1) = 1, V'(-1) = 0, sigma = -8, Sigma_2 = Poincare sphere,
lambda = -1. Right trefoil gives Walker's -1/18 for L(3,1) (lambda_W = 2 lambda).
Consequences for a JC counterexample K: Sigma_2(K) is a ZHS with lambda = sigma(K)/8, Rokhlin = sigma/8 mod 2,
Arf(K) = 0 (det = 1 => det = +-1 mod 8). For branch knots L_n with Sigma_2 = S^3_{1/n}(K): lambda = n a_2(K), and
in an antiparallel twist family sigma is constant on each parity class (rank-one Seifert change + sigma in 8Z),
so V(L_n) = 1 forces n a_2(K) = sigma(L_n)/8: even n => a_2 = 0; odd n => at most one n. (Project already has this.)

## 2. Cheap probe (done, ~5 min CPU): which cyclotomic values of J are "classical" or determined by V_K?
Script: scratchpad l4/cong.py, test.py, clif.py (random kht++ words via flat_search.gen; J normalised J = 1 mod (t+1)^2,
V normalised V(1)=1, V'(1)=0). 300 + 1500 nontrivial samples, 472 distinct J.
- For n = 3..48: regress J(zeta_n) on {1, V_K(zeta_n^k) : all k}. EXACT relations only at n = 4, 6 (J = 1) and n = 10
  (J(z) = V_K(z^2), calibrates conventions). Nothing else up to n = 48. So the Phi_10 identity is isolated.
- J at the remaining "Clifford-type" orders 3, 8, 12 (where t^2 has order 3, 4, 6) is NOT classical: norms
  N(J(zeta)) take dozens of values (n=3: 7, 13, 19, 31, ...), not functions of (det, Arf).
- Cube root, elementary and proved: J(w) = 1 + 2(w-1) g(w) (w = e^{2 pi i/3}, J-1 = (t^4-1)(t^3+1) g). Writing
  g(w) = a + b w:  N(J(w)) = 1 - 6a + 12(a^2 - ab + b^2) == 1 mod 6, and N(J(w)) = 1 iff g(w) = 0 iff J(w) = 1.
  Why J(w) is rich although V_L(w) = +-1 for EVERY link: at t = w, delta = +-1 and the Gram matrix [[delta,1],[1,delta]]
  of the 4-ended tangle module is singular, so every closure functional is proportional to one functional; J(w) is the
  coordinate on the radical that no closure sees (a decategorified non-semisimple phenomenon). Astra's w-gate lives here.
- Cube-root detection is FALSE: T(4,5) from X = 1/4 + 1/(-5), lam = 20 gives J = t^15(t^8 - t^7 + t^6 + t^3 - t^2 + t - 1),
  J(w) = 1 exactly. (T(2,3) and T(3,4) give norm 7.)

## 3. BEST BRIDGE: Lemma Q as a Lehmer problem (Mahler measure of J, Smyth, Lawton)
### 3.1 Data that motivates it
Over 1800 nontrivial samples: M(V_K) = 1 in 128 samples (cyclotomic Jones polynomials, figure-eight type; Champanerkar-
Kofman's "cyclotomic links"), but min M(J) = 1.349716 (J = t^6(1 - t + t^2 - t^4 + t^5)). Among the 128 cyclotomic-V
samples, min M(J) = 1.47995. Reciprocal J occur (32 samples) with M(J) = 1.50746. Ten smallest distinct M(J):
1.34972, 1.38028, 1.39568, 1.41877, 1.46509, 1.47144, 1.47995, 1.49167, 1.49843, 1.50746.
So the obstruction that kills a Mahler-measure route for V (Codex note section 2: 4_1 has M(V) = 1) does NOT appear for J.

### 3.2 Definitions
M(P) = |lead| prod max(1,|root|) for P in Z[t^{+-1}] (monomials have M = 1). P is reciprocal if P(1/t) = +-t^k P(t).
(K,h) is J-amphichiral if J(Kbar,hbar) = J(K,h). theta_0 = 1.324717... (real root of x^3 - x - 1).

### 3.3 Proposition A (mirror). J(Kbar,hbar)(t) = J(K,h)(1/t) for the normalised J.
Proof: mirroring the symmetric diagram swaps A <-> A^{-1} in every bracket, hence in y, x and u = y + delta x, so the
raw J goes to J(1/t) up to a unit; the normalisation "J = 1 mod (t+1)^2" is preserved by t -> 1/t (value 1 and zero
derivative at -1 are preserved: d/dt J(1/t) = -t^-2 J'(1/t)), and the normalised representative is unique. Checked
exactly on 120/120 random words (x <-> y swap).
Corollary: J reciprocal <=> (K,h) J-amphichiral, and then J(1/t) = J(t) on the nose (a reciprocal normalised J must
satisfy +-t^k = 1 mod (t+1)^2, so k = 0, sign +).

### 3.4 Proposition B (Smyth gap). If (K,h) is not J-amphichiral then M(J(K,h)) >= theta_0 = 1.3247.
Proof: J is non-reciprocal, so some irreducible factor f of t^m J in Z[t] is non-reciprocal (a product of reciprocal
polynomials is reciprocal up to sign). If f is not monic, M(f) >= 2. If monic, its roots are non-reciprocal algebraic
integers and Smyth (1971) gives M(f) >= theta_0. M is multiplicative.  []
Meaning: the strong inversion BREAKS mirror symmetry (the figure-eight's two inversions are swapped by the mirror), and
a chirally broken J is automatically far from every cyclotomic polynomial. A Lemma Q counterexample must be
J-amphichiral, and there the question is exactly Lehmer's (reciprocal) problem.
Caveat (honest): qualitatively "non-reciprocal => J != 1" is trivial. Prop B's value is QUANTITATIVE: a uniform gap that
survives limits (3.6).

### 3.5 Proposition C (arithmetic shape of a cyclotomic J). If M(J) = 1 then J = +-t^k prod Phi_{n_i}(t) with no
n_i of the form p^a, 2p^a, 4p^a, 6p^a (p prime, a >= 0; includes n = 1,2,3,4,6,8,...). Allowed n start 15, 21, 33, 35,
39, 40, 45, 51, 55, 56, 57, 60, ...; every factor has degree >= 8.
Proof: J(1) = J(-1) = J(i) = J(e^{i pi/3}) = 1 are units, and Phi_n(zeta_m) is a nonunit iff m/n or n/m is a prime
power (classical resultant formula Res(Phi_n,Phi_m) = p^{phi(min)} in that case, else +-1). Phi_n(1) = p for n = p^a,
Phi_n(-1) is p or 2 or 0 for n = 2p^a, 2^a, 2; Phi_n(i) nonunit for n = 4p^a and n = 1,2; Phi_n(zeta_6) nonunit for
n = 6p^a and n = 1,2,3.  []
So "cyclotomic J" is arithmetically possible but rigidly constrained (no small cyclotomic factors at all, unlike
V_{4_1} = t^-2 Phi_10). Conjecture LJ below says it never happens geometrically.

### 3.6 Proposition D (families: Lawton + Boyd). Let J_m = P(t, t^{m_1}, ..., t^{m_r}) for a Laurent polynomial P
(true for J along any multi-parameter family of FULL twists in r twist regions, after the m-dependent unit: each
twist region contributes eigenvalues that are monomials in t; transfer-matrix form already in the project).
(i) Lawton (1983) + Brunault-Guilloux-Mehrabdollahei-Pengo (2024, explicit error): M(J_m) -> M(P) as
q(m) := min{|v| : 0 != v in Z^{r+1}, v.(1,m) = 0} -> infinity.
(ii) Boyd / Smyth (1981): M(P) = 1 iff P is +- a monomial times a product of cyclotomic polynomials in monomials.
(iii) Hence if P is not generalised-cyclotomic, then M(J_m) >= (1+M(P))/2 > 1 for all m outside a finite union of
"resonant" sublattices {v.(1,m) = 0, |v| <= C}; on each resonant sublattice J_m is again a family of the same form with
fewer parameters, so one recurses. At the bottom: finitely many sporadic m, plus resonant subfamilies whose polynomial
is generalised-cyclotomic.  []  (i),(ii) are theorems; (iii) is a direct consequence.
Translation: the project's "resonance budget" and "resonant mirror-type products" are exactly the sublattices where
Lawton's convergence fails, and generalised-cyclotomic restrictions are the only way an infinite family can approach
M = 1. This is a GLOBAL mechanism for interactions between pieces (all twist parameters simultaneously), which is what
CONTEXT says is missing. It is checkable: generalised-cyclotomicity of a multivariable P is decidable (torsion points
on varieties: Beukers-Smyth / Aliev-Smyth style algorithms).

### 3.7 Conjecture LJ (Lehmer gap for J). There is c > 1 (data suggest c = 1.3497...) with M(J(K,h)) >= c for every
strongly invertible (K,h) with K != U. LJ => Lemma Q => (with the project's reduction) JC for branch knots.
LJ is strictly STRONGER than Lemma Q (it also forbids non-unit cyclotomic J), so it is not a restatement; its advantage
is robustness: it is stable under twisting limits (3.6), multiplicative, and has entropy meaning (Lind-Schmidt-Ward:
log M(J) = entropy of the principal algebraic Z-action on the dual of Z[t^{+-1}]/(J)).
Two halves: (a) chiral (K,h): Prop B already gives c = theta_0 = 1.3247. (b) J-amphichiral (K,h): reciprocal Lehmer
problem; this is where all the difficulty sits.

### 3.8 Obstructions / why the naive versions fail
- For V the analogous gap is FALSE (4_1, and Champanerkar-Kofman found 17 cyclotomic prime knots up to 16 crossings).
  The gain for J comes from the inversion breaking symmetry plus the strong universal congruences; nothing like this is
  proved for amphichiral (K,h).
- Lawton only gives limits; finitely many members per level are uncontrolled unless the BGMP explicit error term is
  made uniform in the family. Exact J = 1 is better handled by exponent-collision (semilinear) analysis.
- Arithmetic alone cannot rule out cyclotomic J (Prop C leaves infinitely many n); the gap must be geometric.

### 3.9 First concrete steps (cheap, for whoever continues)
1. Take the project's two-node / Montesinos transfer matrices (X, Y in mont/jtools.py) and write J for a 2- or
   3-parameter twist family as an explicit P(t, x1, x2). Certify P is not generalised-cyclotomic, compute M(P)
   (Lawton limit), list resonant sublattices v.(1,m) = 0 with |v| <= C. Compare with the project's resonance budget.
2. Find the smallest-M J-amphichiral (K,h) (reciprocal J): data minimum so far 1.50746. If some J-amphichiral J has
   M close to Lehmer's 1.17628, LJ with c = 1.3497 is false but LJ with c > 1 may survive.
3. Identify the minimiser J = t^6(1 - t + t^2 - t^4 + t^5), M = 1.349716 (word s.l1.x0.x0.x1.x0.y1.u2).

## 4. Other arithmetic bridges (short, with honest status)
- B2 Finite-field zeros (Codex): RESTATEMENT. My addition: the only "classical" zeros of V are at t = -1 (and e^{i pi/3}
  at p = 3), i.e. primes dividing det, which come from dihedral (Fox) representations. A JC counterexample has det 1, so
  every finite-field zero of V_K must come from NON-dihedral data. The natural geometric source to try: traceless
  SL(2,F_q) representations (reductions of the traceless SU(2) representations Kronheimer-Mrowka guarantee). UNCLEAR.
- B3 Cube-root radical (section 2): J(w) is the radical coordinate at the degenerate-Gram point; PARTLY_KNOWN in
  spirit (non-semisimple TQFT: Costantino-Geer-Patureau-Mirand / Blanchet-Costantino-Geer-Patureau-Mirand recover
  torsion-type invariants at such points). New here: norm formula, N(J(w)) = 1 mod 6, and T(4,5) shows no cube-root
  detection. Partial check only: for T(2,3), N(J(w)) = 7 is not |Res(Delta, Phi_m)| for any m (Delta = Phi_6); a
  sample-wide comparison with norms of V_K and Delta_K at m <= 30 was started but NOT finished (agent time).
- B4 Whang descent: integral points of SL_2 character varieties of surfaces form finitely many Mod-orbits outside a
  degenerate locus (Whang, arXiv:1710.01848). Rational tangles = one Mod(S_{0,4})-orbit; Sikora's equivalent of JC is
  "bracket detects rational tangles". A q-deformed descent (Euclid on q-rationals, Morier-Genoud-Ovsienko
  arXiv:1812.00170) with the Bonahon-Wong Chebyshev-Frobenius shadow at roots of unity (arXiv:1206.1638) might transport
  Whang's height-descent to tangle vectors. NEW/UNCLEAR; first step: compute the Frobenius shadow of [T] at A of odd
  order N and ask whether it is an integral point of the S_{0,4} cubic in the orbit of the rational ones.
- B5 Habiro / quantum modularity / Kashaev: need all colours; Codex's formal H_0 = H_r = 1 obstruction applies.
  No leverage for V alone. KNOWN limits.
- B6 Iwasawa / p-adic: V(1) = 1 makes the Iwasawa lambda and mu of V trivial at every p; p-adic residue disks around
  roots of unity of order 1,2,3,4 (and 6 when 3 does not divide det) contain no zeros of V for det-1 knots. Restatement.
- B7 t = -1 jet = Casson invariant of Sigma_2 (Mullins): KNOWN and already used by the project (section 1).

## 5. Verdict
Strongest arithmetic bridge: Lemma Q as a Lehmer-type gap for J (section 3). It is genuinely more than a
restatement (strictly stronger, limit-stable), it imports real tools absent from quantum topology (Smyth's
non-reciprocal bound, Lawton/Boyd limits with explicit error terms, Boyd-Smyth classification of measure-one
polynomials, Lind-Schmidt-Ward entropy), it immediately handles the chiral half quantitatively (Prop B), and it
turns multi-parameter twist families into finitely many algebraic checks plus generalised-cyclotomic resonant
subfamilies (Prop D). The amphichiral half is honestly a Lehmer problem and is where it could fail.
Novelty check: Champanerkar-Kofman studied Mahler measure of V (math/0404236, math/0605631); nothing found on Mahler
measure of strongly-invertible / theta-curve invariants. Not checked by outside experts.
