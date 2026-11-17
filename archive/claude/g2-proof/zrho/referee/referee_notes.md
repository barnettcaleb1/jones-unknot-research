# Referee notes on build-identity, build-infinite, build-finite (zrho), 2026-11-03

Scratch notes for the referee lane. Check script: `check/const_check.py` (exact rationals, runs in about 1 s).

## 0. Verdicts

| Build | Verdict | One line |
|---|---|---|
| identity | survives | Correct reformulation. The constant -1/10 is independently confirmed. The new content is thin: the signature value and the knot reading. |
| infinite | survives | Theorem A and Lemma B look correct, modulo Deligne (confirmed for g >= 2) and c = +-lambda_1. The named crux is a tautology. The sketches are unverified. |
| finite | damaged | Its analysis of the Z/10 is right. Its leading proposal is refuted by Lemma B. Its verdict leaning toward Z_rho = Z is unsupported. |

No fatal error was found in any load-bearing step.

## 1. Identity build

### 1.1 Checked and correct
- **Birman-Hilden: M_phi = Sigma_2(K_phi).** The two lifts differ by iota, and iota extends over H. K_phi depends only on phibar, since Delta^2 is trivial in Mod(S_{0,6}). The determinant is 1, so K_phi is a knot.
- **d^ (exponent sum in Mess's basis).**
  - d^ is invariant.
  - It spans Hom(I_2, Q)^{M_2}.
  - Ker d^ = [M_2, I_2].
  - Reason: separating curves with the same splitting are I_2-conjugate, because Stab(c) surjects onto Stab(splitting). So H_1(I_2) = Z[splittings], and Sp acts transitively on splittings.
- **The constant.** lambda(M_{T_c}) = -a_2(K_c), and a_2(K_c) = det theta|_{V_1} = (1/4) B(u_c, u_c), where u_c = omega_1 - omega_2 and B(omega, .) = 0.
  - Decomposition: u (x) u = pi_22(u (x) u) + (Q(u,u)/5) Q^{-1}, with Q(u,u) = -2.
  - So the invariant part of a_2 is (1/4)(-2/5) tr_Q(B).
  - The referee's script computes tr_Q(B) = -1 exactly, so the invariant part is 1/10.
  - It also checks a_2 = (1/4) B(u,u) on 300 random splittings, with both sides of each splitting agreeing.
  - Hence lambda = -d^/10 + q o tau_2 on I_2, with q(Gamma) contained in (1/10)Z.
  - The Stab(c)-invariants in [22] are 1-dimensional, so tau_2(T_c) is a fixed multiple of pi_22(u_c (x) u_c), and q is well defined.
- **tau_2 factors through rho.** Kasahara 2001, Cor 1.2, read in k2001.txt: Ker tau_2(2) = F_2. So N is contained in Ker tau_2.
- **Mullins's sigma/8 term.** Pinned by T(3,5): sigma = -8 and lambda(Sigma(2,3,5)) = -1.
- **Mullins's L/12 term.** Pinned only through the Casson-Walker value of L(3,1), which is not a homology sphere. T(3, 6n +- 1) has L = 0. No homology-sphere example with L != 0 was checked. This is harmless on N, where L = 0.
- **Lemma 4.** V of the plat is a normalised matrix coefficient. Units cancel, including when Kasahara's t and A are fractional powers of each other: work over Z[s^{+-1}] with A = s^5 and t = s^{-4}.
- **Logic of (a) to (d).** Correct.

### 1.2 Objections
- **Attribution.**
  - The lambda-form of (c) is a sentence in Kasahara section 6: "rho contains the full information of lambda ... iff rho contains the information of d_1."
  - Kasahara's statement there that "q_f factors through tau_g(2)" in the closed genus-2 case is true only with d_1 = (12/5) d^. That is, it presupposes the -1/10 constant. The identity lane supplies this missing normalisation.
- **Mullins is not needed for (b) or (d).**
  - Take kappa in N. Then V(K_kappa) = 1 and tau_2(kappa) = 0. So lambda(Sigma_2 K_kappa) = -d^(kappa)/10.
  - So T implies d^(N) = 0, and finiteness of Z_rho gives a nontrivial Jones-trivial knot.
  - This uses Morita, Kasahara Cor 1.2, Birman-Hilden and the plat formula.
  - Mullins adds only the numerical value sigma = -(4/5) d^ on N.
- **"Every 3-bridge knot of determinant 1 is K_phi [STD]."** Unproved. It is not used.
- **The "next lead" in section 9 is vacuous for Problem 6.2.** On Ker phi(2), the right-hand side is a homomorphism through the t = +1 first-order term, and it vanishes identically on N.
- **Plats from kernel elements are known.** That Jones-trivial plats arise from kernel elements is in Jones 1987, in Kasahara 2008's introduction, and in Ito 2015. What is new is only the certificate by Casson invariant or signature, available when d^(kappa) != 0.

## 2. Infinite build

### 2.1 Checked and correct
- **E is a central Z-extension of Sp(4,Z).**
- **Its class.** eps = d_2(d^) = +-5 c (mod torsion), by two consistent routes:
  - Meyer: phi|_{I_2} = +-(4/5) d^, and [tau] = +-4c. The factor 4 is checked on SL(2,Z), where [tau] = 4e has order 3 in Z/12.
  - Cokernel: H^2(Sp(4,Z); Z) = Z + Z/2, with the torsion being Ext(H_1 = Z/2). The cokernel is H^2(M_2; Z) = Z/10. Then |a|·|T| = 10 with |T| = 2 gives a = +-5.
  - Here c is Deligne's class, the Euler class of det on U(2), which is the Hodge class lambda_1.
- **Deligne.** Funar-Pitsch (ar5iv 2004.04129) state Deligne's result "for any g >= 2": twice the central generator dies in every finite quotient.
- **Lemma 2.2, Theorem A(a) and (b), Lemma B.** The steps hold:
  - the pushout argument;
  - the modular law;
  - Chevalley's unipotent congruence subgroup property;
  - finite generation of P_k (it is a subgroup of a finitely generated nilpotent group);
  - Bass-Milnor-Serre for transvection powers.
- **Uncovered q.** Lemma B also covers q = e^{2 pi i/3}, which the finite lane left unanalysed. There, nonseparating twists still have finite order. The separating-twist transvections are irrelevant to the argument.
- **Propositions 1 and 2.** Correct. Proposition 2 is a restatement of Kasahara's Prop 6.1.
- **Hodge-winding formula** d^ = w/2 + 5 wind(det A). Consistent:
  - chi_5 vanishes to order 1 on each D_s, so d^ is the winding of chi_5.
  - Thomae gives chi_10 proportional to (det A)^10 Disc.
  - The full twist gives 15 - 15 = 0.
  - This is probably known in the Atiyah-Iida line (Meyer function via chi_10).

### 2.2 Objections
- **The named crux is a tautology.** "wind(det A) = -w/10 on N" is d^|_N = 0 rewritten through the formula. There is no mechanism, so the build is neither circular nor wrong; it proves nothing on the infinite side, which it says itself.
- **The normalisation caveat in section 6 is stated backwards.**
  - If lambda_1 = 2c, the bound becomes 20.
  - If c = 2lambda_1, the bound would be 5, which contradicts Kasahara's q = i lower bound.
- **Theorem A is a statement about M_2 alone.** For the faithful representation id, Z_id = Z, while every finite shadow is at most Z/10. So the "non-commuting limit" is the normal situation, and it is no evidence for |Z_rho| = 10. This neutralises Kasahara's "remains possible".
- **Sharp falsification test of Theorem A.**
  - Take phi with tau_2(phi) in 20 Gamma. Then q_f(tau_2 phi) is in 2Z for every Heegaard embedding f. So every BC_q(phi) = lambda mod 2 = d^(phi)/10 mod 2.
  - If the ten BC homomorphisms were profinitely continuous on I_2, then together with tau_2 mod 20 (which is continuous, through Out of pi/Gamma_4) they would give a finite quotient with 20 dividing |Z_pi|.
  - So Theorem A forces: in genus 2, no BC_q is induced from a finite quotient of M_2.
  - **Consistency check.** Wright (thesis 1992, JKTR 1994): the r = 4 RT representation restricted to Torelli is the sum of the BC homomorphisms. That representation is projective. For an M_2-equivariant linear lift W^:
    - W^|_{I_2} = omega^{d^} diag((-1)^{BC_q});
    - det forces omega^10 = -xi^2;
    - kernel elements with d^ = 10 must have all BC_q = 1.
    This is exactly consistent with Casson, so no contradiction is found.
  - **Remaining checks.** The Ising anomalies (Theorem A predicts det W^ = 1 on I_2, i.e. xi^2 = 1). Also any genus-2 result extending BC homomorphisms to a finite-index subgroup. Sato's level-2 abelianization is for g >= 3.
- **Sketches with unchecked assumptions.** The Toledo lift and "sigma(K_.) is a homomorphism on I_2" remain sketches.

## 3. Finite build

### 3.1 Checked and correct
- **The two parts of the 10.**
  - Z/5 = the image of I_2 in H_1(M_2) (as the addendum already notes), seen as the q = 1 scalar.
  - Z/2 from the parity lemma, verified: B(x,x) = 2Pf(x), B(u,u) = -2 and B(x, u_c) = -2 x_{e1f1}.
  - d^ mod 2 = sum over even q of BC_q, verified: exactly one even q has BC_q(T_c) = 1.
- **Centre form, bounded defect, prime-by-prime.** Correct.
- **C1 to C3.** Correct. tr = B(u,u')^2/4 = (2n-1)^2.
- **Casson reading.** |Z_{phi(k)}| = 10 [Z : lambda(F_{k+1})]. Correct.

### 3.2 Objections
- **The leading proposal is dead.** The proposal is d^ mod 25 at t = zeta_25, or a 5-adic tower over Z_5[[t-1]]. By Lemma B and Theorem A, every root-of-unity specialisation with q != -1, and every finite or pro-p quotient, has |Z| dividing 10. So the 5-part can never exceed 5 residually, and the test answer is known in advance.
- **The verdict "every reason points to Z_rho = Z" is unsupported.**
  - Reason 1 assumes T.
  - Reason 2 excludes only pairwise relations, while centres of pseudo-reflection groups come from global relations.
  - Reason 3, that all the evidence is classical, cuts both ways. Theorem A shows residual evidence cannot exist either way.
- **"Far stronger than not-T" is overstated.** One Jones-trivial knot with sigma != 0 already gives an unbounded-signature family by connected sum. Only 3-bridge-ness is extra.
- **The only finite-side route is a search for (F).** The user has ruled out such sweeps.
- **The q = i reading of the 2.** Probably in Kasahara 2002 (Rochlin, per its abstract). Not read.

## 4. Literature
- Kasahara 2001 section 6:
  - the lambda-equivalence, Prop 6.1 and Problem 6.2;
  - Remark 6.3: finite implies unfaithful; at least 10 via the q = i paper; computer value Z/10 for k = 1, 2.
- Kasahara addendum: I_2 maps to Z/5 in H_1(M_2).
- Not found: (*), the signature forms, Theorem A, Lemma B, the parity lemma. Two searches here, plus the siblings'.
