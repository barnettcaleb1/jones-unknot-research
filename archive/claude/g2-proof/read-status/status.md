# Literature status: Jones genus-two representation, W(5,1), Ito 2015, Kasahara, Heegaard and handlebody angle

Lane g2-proof / read-status, 2026-11-03. Verification tags:
- [READ]: I read the relevant pages this session.
- [ABS]: I checked only the abstract or listing.
- [MEM]: cited from memory and not re-checked this session. Treat these as pointers only.

Notation follows the lane: W(n,k) is the TL standard module and sigma_i -> A + A^{-1} e_i. In Bigelow's 2002 notation the TL representation of B_n is the sum of the V_lambda with at most two rows. So W(5,5), W(5,3), W(5,1) = V(5), V(4,1) (Burau), V(3,2).

## 0. Bottom line

1. **Status.** Faithfulness of Jones's genus-two representation is open. I found no proof and no counterexample through Nov 2026, and nobody claims one. Two published sources treat it as a live possibility:
   - Jones 1987, p. 362: "entirely possible" that the M(0,m) representations are faithful.
   - Kasahara 2001: calls it a "candidate for the faithful linear representation" of M_2.
   
   No source names W(5,1) as an open problem. It falls under the general open question of whether TL/Jones is faithful for n >= 5 (Jones's "Ten problems" no. 3 as cited by Bigelow 2002; FWW 2002 say "not known to be faithful"). BBB 2026 claims only n = 4.
2. **Normalization fact.** In Jones's linear normalization rho(iota) = I for the hyperelliptic involution iota. I proved this and checked it exactly; see 1.1. So "faithful" can only mean ker rho = <iota>, that is, the projective W(6,0) representation of Mod(S_{0,6}) is faithful.
3. **Observation (not in the literature as far as I found).** W(5,1) is faithful if and only if Jones's genus-two representation is faithful modulo iota. F3 gives one direction. The other follows from Long 1986 plus capping (proof sketch in 1.3). So the genus-two formulation is equivalent to the W(5,1) formulation, not stronger.
4. **Ito 2015.** The statements are pinned down in section 2. The theorem is about any non-trivial, non-central normal subgroup H of B_n. To apply it to the Jones polynomial, the kernel must be the kernel of the full TL representation, not of one summand. Long's Lemma 2.1, which Ito quotes, converts "every summand has a nontrivial kernel" into "the full representation has one". For B_5, Bigelow's Burau_5 result plus Long gives: TL_5 is unfaithful iff W(5,1) is unfaithful. F1 and F2 are therefore confirmed, and **F2 for B_n is a known lemma (Long 1986, Lemma 2.1), not new.**
5. **Kasahara.** The addendum corrects no error. It adds an overlooked restriction: det rho = +-1, so no graded quotient contains the trivial summand. **Kasahara's Problem 6.2 is the only published route to UNfaithfulness I found.** If the cyclic group Z_rho = rho(I_2)/rho([M_2, I_2]) is finite, then rho is not faithful on I_2. Its order is known to be at least 10, the computed truncations give Z/10, and Kasahara says order exactly 10 "remains possible".
6. **Heegaard angle.** F5 is Jones 1987, Note 13.19 (p. 376). There Jones computes V of a 3-bridge plat from the 5x5 (3,3) matrix using the projection p_2 = e1 e3 e5, which is the cup or handlebody vector. That makes F5 a restatement of a known formula. Jones also remarks (p. 363) that the representation might "settle most questions about genus 2 Heegaard splittings rather mechanically" by reducing q into a finite field. I found no follow-up that develops this. I found no theorem identifying the stabilizer of the handlebody vector with the handlebody (Hilden) group, either for the generic-q Jones representation or asymptotically for quantum representations.

## 1. Faithfulness status

### 1.1 Jones's genus-two representation: definition and normalization

**Jones's construction.** Jones 1987, Section 10, pp. 361-363 [READ]:
- Theorem 10.2: the adjusted Hecke representation pi'_Y of B_m defines a representation of M(0,m) iff Y is rectangular.
- In genus two the theta_i generate the whole mapping class group M(2,0). There is "really only one representation" (Y = (3,3) up to symmetry), given by explicit 5x5 matrices over Z[q^{+-1}] multiplied by q^{-2/5}.
- p. 363: the separating Dehn twist is q^6 I plus a rank-one matrix whose only nonzero off-diagonal row is row 4. Jones calls the representation "highly non-trivial on the Torelli group" and notes that this matrix is the identity at q = -1.

**Kasahara's normalization.** Kasahara 2001, Section 2.3 [READ]: rho: M_2 -> GL(5, Z[t^{+-1}]) with t = q^{1/5}. He gives explicit rho(zeta_1) and rho(xi), where xi = zeta_1...zeta_5 has order 6 and zeta_{i+1} = xi zeta_i xi^{-1}. Formula (2.2) gives rho(psi_0) = rho((zeta_1 zeta_2 zeta_1)^4) = t^6 Id + ((t^15+1)/t^24) x (row-4 matrix). The image is trivial on I_2 at t = +-1.

**Fact: rho(iota) = I.**
- Proof: rho is absolutely irreducible, so rho(iota) = cI. Each rho(zeta_i) has determinant -1, with eigenvalues -t^{-2} three times and t^3 twice. iota = zeta_1...zeta_5 zeta_5...zeta_1 is a word of length 10, so c^5 = 1. Units of Z[t^{+-1}] are +-t^k, so c = 1.
- Exact check with Kasahara's matrices at t = 3/2: scratch/iota_check.py confirms rho(iota) = I, rho(xi)^6 = I, and that the separating twist is t^6 I plus a single nonzero row.
- Funar 2021, Section 2.6.3, also notes that the hyperelliptic involution maps trivially.
- Consequence: "faithful" must mean ker rho = <iota>, i.e. faithfulness of the projective representation of Mod(S_{0,6}) = M_2/<iota>.

### 1.2 Status statements found

- **Jones 1987, p. 362 [READ].** On the M(0,m) representations with parameter q, he says it is "entirely possible" that they are faithful, and that this is "closely linked to the question of faithfulness of the Burau representation". This is the original posing.
- **Kasahara 2001, Introduction [READ].** rho "has been given attention as a candidate for the faithful linear representation of M_2", citing J. Birman, *Mapping class groups of surfaces*, Contemp. Math. 78 (1988). He notes there are "few results" on rho beyond Humphries 1992 and his own root-of-unity preprint.
- **Kasahara 2001, Section 6 [READ].** Proposition 6.1, Problem 6.2 (determine the order of Z_rho) and Remark 6.3: finite order implies rho is not faithful on I_2. The order is at least 10. Computer calculations give Z/10 for the first- and second-order truncations ("it remains possible that the order of Z_rho is exactly 10"). For context: Ker d_1 = [M_2, I_2], and I_2/[M_2, I_2] = Z is the Casson core d_1 (Morita).
- **Freedman-Walker-Wang, G&T 6 (2002) 523-539, abstract [ABS].** Jones' original braid group representation "is not known to be faithful".
- **Bigelow, "Does the Jones polynomial detect the unknot?", JKTR 11 (2002) 493-505, arXiv math/0012086 [READ, pp. 1-7].**
  - Question 1.2: is the TL representation faithful? This is Problem 3 in Bigelow's ref. [8], presumably Jones's "Ten problems" (2000) [MEM for the identification].
  - Conjecture 1.3: a TL kernel implies a nontrivial knot with V = 1.
  - Conjecture 1.4: a Hecke ("Jones" in his usage) kernel implies a knot with HOMFLY = 1.
  - Proposition 1.5: for B_4, the Jones, TL and Burau representations are all faithful or all unfaithful.
  - Section 3 identifies V(2,2) = Burau_3 composed with B_4 -> B_3, and shows the kernel of V(2,1,1) equals that of V(3,1). This matches F3's description of W(5,1)|B_4.
- **BBB, arXiv:2607.05283 [ABS].** v1 6 Jul 2026, v2 14 Sep 2026 ("Minor corrections and improved exposition"). Claims Burau of B_4 is faithful, with the corollary that the Jones representation of B_4 is faithful. The abstract says nothing about n >= 5, TL or genus two. A Columbia news item dated Aug 2026 exists. A Nov 2026 web search found no paper citing BBB that discusses n = 5 or genus two.
- **Birman-Brendle, "Braids: a survey" (Handbook of Knot Theory 2005, arXiv math/0409205) [READ, about 200k of 234k characters].** Open Problem 5 (Section 4.4) is Burau_4. The parts scanned make no faithfulness claim for the Jones, Hecke or TL representations and do not mention genus two or Kasahara.
- **Not checked.**
  - Bigelow, ICM 2002 survey (math/0304212) [ABS]: the abstract mentions LK faithful, Burau unfaithful, Hecke as a future direction.
  - Bigelow, "Braid groups and Iwahori-Hecke algebras" (Farb's problem book, Proc. Symp. Pure Math. 74, 2006; math/0505064): the text could not be extracted. This is the most likely place for an explicit genus-two question. A later lane could read it.

### 1.3 W(5,1)

**No source names it.** No source I found names W(5,1) (shape (3,2)) as an open problem. It is covered by the general TL/Jones faithfulness question for n >= 5.

**Reduction (implicit in the literature, not stated anywhere I saw).**
- TL_5 = V(5) + V(4,1) + V(3,2).
- ker V(4,1) = ker Burau_5 is nontrivial (Bigelow 1999).
- ker V(5) = [B_5, B_5].
- Long 1986, Lemma 2.1 (as quoted in Ito 2015, Cor. 2): two non-central nontrivial normal subgroups of B_n intersect nontrivially.
- Hence TL_5 is unfaithful iff W(5,1) is unfaithful.
- One technical point (my computation): Delta^2 acts on W(n,k) by the scalar +-A^{k(k+2)-3n}. For example, on W(2,0) it is A^{-6} and on W(5,1) it is A^{-12}. At generic A each kernel therefore meets the centre trivially, so "nontrivial" already implies "non-central".

**Observation: W(5,1) is faithful iff Jones's genus-two representation is faithful mod iota.**
- The direction "genus two faithful implies W(5,1) faithful" is F3.
- For the converse, let N be a nontrivial kernel of projective W(6,0) on Mod(S_{0,6}). This group is centreless. N is normal, so it contains a pseudo-Anosov (Long 1986) and is infinite.
- Stab(p6) has index 6, so N meets it nontrivially.
- Capping gives a surjection B_5 -> Stab(p6) with kernel <Delta^2>.
- W(6,0) restricted to B_5 is W(5,1), by the branching rule (3,3) -> (3,2) only.
- So the preimage of N in B_5 is a non-central normal subgroup acting by scalars on W(5,1). Commutators [beta, gamma] are nontrivial when beta is non-central, and they lie in the genuine kernel.

### 1.4 Partial results (none settles faithfulness)

- **Kasahara 2001.** Expansion t = -e^h; filtration F_k of I_2 (see Section 3). ker rho intersected with I_2 equals the intersection of the F_k, because substituting t = -e^h is injective on Laurent polynomials. So faithfulness on I_2 is equivalent to the F_k intersecting trivially, which is not addressed.
- **Kasahara 2004 (JKTR 13, no. 2, 297-306, "II").** Expansion t = e^h; the graded quotients are S_6-modules; the Lie subalgebra generated by degree 1 is determined [content via the addendum's summary].
- **Kasahara addendum.** No trivial summand in any graded quotient (Section 3).
- **Humphries 1992 (Glasgow Math. J. 34, 313-317)** and Kasahara's 4th-root-of-unity preprint: specializations at roots of unity, used for normal closures of powers of twists [MEM for content].
- **Specializations are never faithful**, since twists have finite order there. They give image and density results:
  - Funar 2021 (arXiv:2009.05961, Turaev volume, EMS): Prop. 2.11 shows the projectivized Jones representation at a primitive 10th root of unity is the genus-2 Fibonacci TQFT representation; this gives Gamma_2(5) -> PU(1,4) with non-virtually-solvable image [READ via ar5iv summary].
  - Freedman-Larsen-Wang 2002 and Kuperberg 2011 on density [MEM].
- **Asymptotic faithfulness** of level-k quantum representations is not the generic-q Jones representation and says nothing about it:
  - Andersen, Ann. of Math. 163 (2006): in genus 2 the intersection of kernels is {1, iota}.
  - FWW 2002: faithful modulo centre.
  [ABS/MEM]

## 2. Ito 2015 (arXiv:1402.2028 v1, 10 Feb 2014; Math. Z. 280 (2015) 347-353) [READ, all 5 pages of v1; published version not compared]

### Exact statements

- **Theorem 1** (proves Bigelow's Conjecture 3.2 in a stronger form). Let H be a non-trivial, non-central normal subgroup of B_n and alpha an n-braid whose closure is the unknot. Then for every N > 0 there is beta in H such that the closure of alpha beta is a hyperbolic knot of genus >= N and braid index n. (v1 has a typo, "beta in K".)
- **Corollary 1.** Let rho_V: B_n -> GL(V^{tensor n}) be the quantum representation for a finite-dimensional U_q(g)-module V. If rho_V is not faithful for some n, then every knot K has infinitely many distinct hyperbolic knots K_i with the same quantum V-invariant.
- **Corollary 2.** The same holds for a finite family rho_{V_j} that are all non-faithful on B_n. The proof uses Long 1986, Lemma 2.1: the intersection of two non-central nontrivial normal subgroups of B_n is nontrivial.
- **Corollary 3.** If Burau_4 is unfaithful, the Jones polynomial fails to detect the unknot (Bigelow 2002).

### Hypotheses pinned down

- **Which representation.** It must be the one whose quantum trace computes the invariant. For the Jones polynomial that is rho_V with V = C^2 for U_q(sl_2), isomorphic to the sum over k of W(n,k) tensor C^{k+1}. Its kernel is the kernel of the full TL representation, which is Jones's pi_0 at generic t.
  - A kernel element of one summand is not enough on its own.
  - Long's lemma makes the kernels' intersection nontrivial iff each W(n,k), k < n, has a nontrivial kernel. W(n,n) is automatic, with kernel [B_n, B_n].
- **Centre.** The theorem needs H non-central.
  - For TL at generic A this is automatic, by the scalar computation in 1.3.
  - A projective kernel (elements acting as scalars) yields a genuine kernel by taking commutators.
- **n.** Any n >= 3. Nothing is special about n = 5.
- **Which polynomials.** For the TL representation, the Jones polynomial. For the Hecke representation, HOMFLY (Bigelow's Conjecture 1.4). For other V, the corresponding colored invariants.

### Construction and why the knot is nontrivial

- **The knot.** It is the closure of alpha beta, for example with alpha = sigma_1...sigma_{n-1}.
- **Why it is a knot.** beta is chosen pure, so alpha beta has the n-cycle permutation of alpha.
- **Why V = 1.** rho(alpha beta) = rho(alpha), so the traces agree.
- **Why it is nontrivial.** Ito's Dehornoy-floor theorems:
  - beta' >_D Delta^{2N} implies g >= N (Ito, JKTR 20 (2011), Cor. 1.3).
  - beta' >_D Delta^{2r(n)} implies braid index n (Ito, G&T 15 (2011), Thm 2.8).
  - beta' >_D Delta^4 and pseudo-Anosov implies hyperbolic (G&T 15, Thm 1.3).
- **Key new step (Theorem 3).** A nontrivial normal subgroup is unbounded in the Dehornoy order (proof via the alternating decomposition). If it is non-central, one can take a pseudo-Anosov element (Long 1986, Lemma 2.5). Papadopoulos 1982 makes alpha beta pseudo-Anosov after taking powers. Choose a pseudo-Anosov pure beta with beta >_D alpha^{-1} Delta^{2N}.

### Plat or genus-two analogue

- Neither Ito nor Bigelow 2002 has a plat or genus-two version.
- None is needed: by the equivalence in 1.3, a genus-two kernel element mod iota gives a W(5,1) kernel element in B_5. Then Burau_5, Long and Ito give a nontrivial knot with V = 1 that is a closed 5-braid.
- A direct plat version (plat-close alpha beta, with beta in the kernel and alpha a 3-bridge unknot) also gives V = 1 by F5. Nontriviality would then need plat analogues of Ito's Dehornoy floors, which I did not find.

### Related: Jones 1987, Cor. 14.5 [READ]

- Statement: alpha is in ker pi_0 (generic t) iff V of the closure of alpha equals (-(t+1)/sqrt t)^{n-1}, the value for the n-component unlink. The proof uses C*-positivity at t = e^{2 pi i/k}.
- With Birman-Menasco's unlink theorem (a closed n-braid representing the n-unlink is trivial) [MEM]: TL_n is faithful iff the Jones polynomial detects the n-component unlink among closed n-braids.
- The Eliahou-Kauffman-Thistlethwaite 2003 links with the Jones polynomial of the unlink [MEM] matter here only when the braid index equals the number of components.

## 3. Kasahara 2001 (AGT 1, 39-55; arXiv math/0012216) and the addendum (arXiv 1004.1068) [READ]

### The 2001 paper

**Setup.** rho as in 1.1. phi is the expansion t = -e^h, with powers of e^h expanded as Taylor series. F_k = I_2 intersected with {f : phi(f) = Id mod degree > k}.
- F_1 = I_2.
- The filtration is central and coarser than the lower central series.
- The graded quotients G_k F are free abelian of finite rank, and G_k F tensor Q are rational Sp(4,Q)-modules.

**Results.**
- **Theorem 1.1.** G_1 F_Q = Gamma_{0,2}.
- **Corollary 1.2.** ker tau_2(2) = F_2. In particular the second Johnson homomorphism factors through rho.
- **Theorem 1.3.** For k >= 2, G_k F_Q contains Gamma_{2,0} if k is even and Gamma_{0,2} if k is odd.
- **Section 6.** Proposition 6.1: Morita's core d_1 of the Casson invariant factors through rho iff Z_rho = Z. Problem 6.2 asks for the order of Z_rho. Remark 6.3 is quoted in 1.2.

Kasahara explains that the expansion t = e^h gives Sp(4, Z/2) structures instead. That is the reason for -e^h in 2001, and the 2004 sequel uses e^h with S_6-modules.

### The addendum

The addendum is dated 19 Apr 2010 (v2). A web search listing places it in JKTR 20 (2011), no. 6; I did not verify this.
- Fact: det rho is in {+-1}; this holds for all of Jones's rectangular representations.
- The image of I_2 in H_1(M_2) = Z/10 is Z/5, so det = 1 on I_2.
- Lemma: det phi^(k)(x) = 1 + h^k trace Delta_k(x) mod h^{k+1}.
- Therefore trace Delta_k = 0, and **no G_k^Q F (k >= 1), in either expansion, contains the trivial 1-dimensional summand**. M(5,Q) decomposes as Gamma_{0,2} + Gamma_{2,0} + Gamma_{0,0}, or [6] + [4,2] + [2^3] + [3,1^3]. The trivial summand is the centre, which has nonzero trace.
- The author describes this as "a little restriction" that "we had overlooked previously". It corrects no error. The structure beyond the Lie subalgebra generated by degree 1 is stated to remain unknown for both expansions.

**My remark.** By an elementary argument, the addendum implies that d_1, if nonzero, is nonzero on every F_k, so no finite truncation detects it. This is consistent with Z_{phi^(1)} = Z_{phi^(2)} = Z/10 but does not decide Problem 6.2. Faithfulness is untouched, which confirms F4.

## 4. Jones polynomial of 3-bridge knots, Heegaard splittings, handlebody group

### Jones 1987

- **Note 13.19, p. 376 [READ].** The plat of alpha in B_{2m} is an m-bridge link. V is computed from the Catalan-dimension (m,m) matrix of alpha together with the projection p_m.
  - For 3-bridge links Jones uses the (3,3) representation of Section 10, with p_2 = e1 e3 e5 = (1+t)^{-3}(1+g1)(1+g3)(1+g5).
  - V is, up to a power of t, the third row of the 5x5 matrix summed with weights t, 1+t, (1+t)^2, 1+t, 1+t.
  - This is F5 in a fixed basis. The cup vector corresponds to p_2.
- **Section 10, p. 363 [READ].** "Presumably one may use the above representation to settle most questions about genus 2 Heegaard splittings rather mechanically" by taking q in a finite field. This is the only place I found that ties Jones's genus-two representation to genus-two Heegaard splittings. I found no follow-up.
- **Section 15 [READ].**
  - Prop. 15.6: |V_L(e^{2 pi i/k})| <= (2cos(pi/k))^{n-1} for plats on 2n strings.
  - Cor. 15.7: if alpha in B_{2n} lies in ker pi_0 at t = e^{2 pi i/k}, the plat of alpha has bridge number n.
  - Jones on p. 378: "Positivity might be useful in questions of faithfulness".

### Observation for the Heegaard lane (from Jones's positivity; I did not find it stated)

- Hilden is contained in Stab([c]).
- At unitary specializations, Cauchy-Schwarz gives: |<c, rho(beta) c>| = <c, c> iff rho(beta) c is proportional to c.
- Hence Stab([c]) in W(6,0) = {beta : V(plat beta) = monomial x V(3-component unlink)}.
- So "Stab([c]) = Hilden" is equivalent to the Jones polynomial detecting the 3-component unlink among 3-bridge plats. This uses uniqueness of the genus-2 splitting of #2 S^1 x S^2 (Waldhausen) [MEM].
- Care is needed over which roots of unity keep W(6,0) nondegenerate and unitary, and over the monomial ambiguity.

### Background

- **Genus-two splittings and 3-bridge links.**
  - Birman-Hilden, Trans. AMS 213 (1975): manifolds of Heegaard genus <= 2 are 2-fold branched covers of 3-bridge links, and genus-2 splittings correspond to 3-bridge plats via the hyperelliptic involution.
  - Birman-Gonzalez-Acuna-Montesinos, Michigan Math. J. 23 (1976): inequivalent genus-2 splittings arise from distinct 3-bridge links with the same double cover.
  
  So V of the link is an invariant of the splitting, not of the manifold. [MEM]
- **TQFT and Heegaard splittings.** Z(H) is fixed projectively by the handlebody group, and Z(M) = <Z(H), rho(phi) Z(H')> (BHMV, Topology 34 (1995)). Lickorish, Math. Ann. 290 (1991), builds the TL-algebra Heegaard construction of the WRT invariants; Kohno, Topology 31 (1992), does the same with mapping class group representations. [MEM]
- **Quantum representations.**
  - Funar, PJM 188 (1999): infinite image [found by search].
  - Masbaum 1999: an element of infinite order.
  - Roberts 2001: irreducibility; the vacuum vector is cyclic.
  - Gilmer-Masbaum, Ann. Sci. ENS (2007): integral lattices spanned by handlebody skein vectors.
  - FWW 2002 and Andersen 2006: asymptotic faithfulness.
  - Funar 2021, as above.
  [MEM except where marked]
- **Homological plat formulas.** Bigelow, "A homological definition of the Jones polynomial", G&T Monographs 4 (2002), math/0201221, uses plats and bridge position, as does Lawrence 1993. [ABS/MEM]
- **Handlebody-group representation theory** exists but does not address the stabilizer: Bader, Prym representations of the handlebody group, arXiv:2308.14095; Mueller-Woike on handlebody group representations from modular functors. [search hits]
- **Not found:** any theorem that the stabilizer of the handlebody vector equals the handlebody group, whether for Jones's generic-q representation or asymptotically for quantum representations.

## 5. Check of the lane's facts F1-F6

| Fact | Status |
|---|---|
| F1 | Confirmed; hypotheses pinned down in Section 2. |
| F2 | For B_n this is Long 1986, Lemma 2.1, quoted by Ito, so it is known. Long's paper treats mapping class groups generally; I did not verify the exact Mod(S_{0,6}) statement. |
| F3 | Confirmed by branching, and it matches Bigelow 2002 Section 3. **The converse also holds (1.3), so the two problems are equivalent.** |
| F4 | Confirmed, and sharpened by Problem 6.2, Remark 6.3 and the addendum. |
| F5 | **Restatement of Jones 1987 Note 13.19.** The Heegaard reading is anticipated by Jones's Section 10 remark. |
| F6 | The rank-one shape of the separating twist is known (Jones p. 363; Kasahara (2.2); exact check). I did not find the injectivity criterion or the [T_c, T_c'] kernel element in the literature. Context: I_2 is free on separating twists (Mess 1992) [MEM], so F6 is a ping-pong-type question. |

## 6. Other 2026 items

- **Carmi-Cohen, "On trivial Jones-Vassiliev polynomials", arXiv:2606.22410 (21 Jun 2026, math.GM) [ABS].** Claims that every nontrivial knot has a nonzero finite-type coefficient of order <= 3 x crossing number, so V detects the unknot. It is unrefereed, filed under math.GM, and I found no evaluation of it. Not relied on.
- **BBB status.** Unrefereed preprint (v2, Sep 2026). A web search found press coverage but no independent verification.

## Sources

- V.F.R. Jones, Hecke algebra representations of braid groups and link polynomials, Ann. of Math. 126 (1987) 335-388. Sections 10, 13.19, 14, 15 [READ, via a JSTOR copy fetched by WebFetch].
- T. Ito, arXiv:1402.2028; Math. Z. 280 (2015) 347-353 [READ v1].
- S. Bigelow, Does the Jones polynomial detect the unknot?, JKTR 11 (2002) 493-505; arXiv math/0012086 [READ pp. 1-7].
- Y. Kasahara, AGT 1 (2001) 39-55; arXiv math/0012216 [READ pp. 39-44, 53-55].
- Y. Kasahara, Addendum, arXiv:1004.1068 [READ].
- Y. Kasahara, JKTR 13 (2004) 297-306 [via the addendum and the author's faculty page].
- V. Bharathram, J. Birman, T. Brendle, arXiv:2607.05283 [ABS].
- J. Birman, T. Brendle, Braids: a survey, arXiv math/0409205 [READ partially].
- M. Freedman, K. Walker, Z. Wang, G&T 6 (2002) 523-539; math/0209150 [ABS].
- L. Funar, arXiv:2009.05961 (Turaev volume, EMS 2021) [READ via ar5iv summary].
- S. Bigelow, Representations of braid groups (ICM 2002), math/0304212 [ABS].
- S. Bigelow, Braid groups and Iwahori-Hecke algebras, math/0505064 [NOT READ].
- J.E. Andersen, Ann. of Math. 163 (2006) [search snippet/MEM].
- D. Long, A note on the normal subgroups of mapping class groups, Math. Proc. Camb. Phil. Soc. 99 (1986) 79-87 [via Ito].
- A. Carmi, E. Cohen, arXiv:2606.22410 [ABS].
- [MEM]: Birman-Hilden 1975; Birman-Gonzalez-Acuna-Montesinos 1976; BHMV 1995; Lickorish 1991; Kohno 1992; Roberts 2001; Gilmer-Masbaum 2007; Mess 1992; Birman-Menasco 1992; Eliahou-Kauffman-Thistlethwaite 2003; Humphries 1992.

Scratch: /Users/calebbarnett/jones-lanes/g2-proof/read-status/scratch/iota_check.py (single-identity sanity check, under 1 second).
