# Lemma Q literature sweep: EKT, Sakuma, pattern, bridge and band-move readings

- Workflow: wf_81ef8d26-c51 (lemma-q-literature-sweep-wf_81ef8d26-c51.js)
- Session: bridge session (Claude-Codex integrator)
- Launched (script written): 2026-11-03 08:58 local; journal last written: 2026-11-03 09:30 local
- Agents started: read:ekt, read:sakuma, read:pattern, read:bridge, read:band, synthesize
- Results extracted here: read:bridge, read:band, read:pattern, read:ekt, read:sakuma
- Started but returned no result: synthesize
- Context: Launched 3 Nov 08:58 (the bounded literature workflow on EKT, Sakuma, the encircling identity, 3-bridge Jones detection and band moves). The synthesizer did not return. THEORY-width-ladder.md cites the workflow; the readers' fact lists exist only in the journal.
- Provenance: contemporaneous agent outputs recorded in the workflow journal (runtime state, not copied). Text below is verbatim except formatting (JSON fields rendered as markdown), em dashes replaced by ' - ', email addresses redacted, and home-directory paths shortened to ~ (session scratchpad roots to <scratch>). These are internal AI agent outputs, not external review; statuses are as the agent stated them at the time and may be superseded by later board entries.


## Agent: read:bridge


### facts

  -
    - claim: No theorem and no explicit counterexample found for 'Jones polynomial detects the unknot among 3-bridge knots' or 'detects the 2-component unlink among 3-bridge links'.
    - source: Web/arXiv/seminar search, Nov 2026
    - kind: not_found
  -
    - claim: Thm 4.1: 'There is no non-trivial semiadequate link L with trivial Jones polynomial ... even up to units.' Cor 4.1: 'No Montesinos link has trivial Jones polynomial up to units.' Cor 6.3: '3-braid links are semiadequate, and so have non-trivial Jones polynomials up to units.'
    - source: Stoimenow, arXiv:math/0606255v2 (J. reine angew. Math. 657, 2011)
    - kind: theorem_in_source
  -
    - claim: Closed 3-braids have bridge number <=3; Montesinos knots with n>=3 non-integer rational tangles have bridge number n (Boileau-Zieschang, Comment. Math. Helv. 60 (1985), as quoted in arXiv:1510.08469). So the previous fact settles the 3-bridge question for these two subclasses only.
    - source: inference from Stoimenow Cor 4.1/6.3 + Boileau-Zieschang
    - kind: inference
  -
    - claim: Birman 2022: 'To this day it is not known whether the Jones polynomial is a complete invariant' for the unknot among braid-index-3 links. Datta's seminar abstract (7 Nov 2022): 'the Jones polynomial detects the unknot for 3-braid links' via class numbers; the abstract of his arXiv:2204.13660 does not state this and no paper was found. Stoimenow Sec. 6 records Birman's unreferenced claim (Invent. Math. 81, 1985) and Takahashi 1989's claimed long calculation (knots only).
    - source: Birman, The work of Jones, arXiv:2210.01920; GaTech seminar page; Stoimenow Sec. 6
    - kind: theorem_in_source
  -
    - claim: 'The links in these families are all satellites of the Hopf link, and all conform to the pattern H(T,U)' (clasped numerators of tangles T,U; 8 clasp crossings). If T^N, U^N are geometrically essential, the solid-torus boundaries are incompressible with a companion Hopf link (so non-hyperbolic: inference); Prop 2.3 gives non-split, Prop 2.4 prime.
    - source: Eliahou-Kauffman-Thistlethwaite, Topology 42 (2003) 155-169, Secs. 1-2
    - kind: theorem_in_source
  -
    - claim: Thistlethwaite's original links are LL1(0,-2), LL1(0,-1), LL1(0,0), LL1(0,1), LLL(0), found by computer enumeration; LL1(m,n)=H((T_{m,n})^omega,-3) with T rational; 'their sublinks are all alternating'; LL2(n)=H(T_n,-T_n) has components that are 'pairwise distinct 2-bridged knots'; LL2(n), n even, are boundary links with zero Alexander polynomial (hence lk=0).
    - source: EKT 2003, Secs. 3-5
    - kind: theorem_in_source
  -
    - claim: Bridge number of Thistlethwaite's link / EKT families: no source states it. Since b(L) >= sum of component bridge numbers, LL2(n) has b>=4. By my tangle arithmetic (Conway conventions, unverified) the 15-crossing LL1(0,0)=H(5/2,-3) has components 4_1 and a trefoil, giving b>=4. Every Jones-trivial nontrivial link has b>=3, because 2-bridge links are alternating.
    - source: inference from EKT + Kauffman/Murasugi/Thistlethwaite
    - kind: inference
  -
    - claim: Alternating: span of V equals the reduced alternating crossing number, so V detects the unknot/unlink (hence also among 2-bridge links: inference); adequate links likewise; 'the Jones polynomial of an almost alternating link is nontrivial'.
    - source: Kauffman, Murasugi, Thistlethwaite, Topology 26 (1987); Lickorish-Thistlethwaite, Comment. Math. Helv. 63 (1988); Lowrance-Spyropoulos arXiv:1707.05443
    - kind: theorem_in_source
  -
    - claim: Arborescent: no detection theorem found. Stoimenow Example 4.1: extending Cor 4.1 'to arborescent links' met difficulties (non-semiadequate arborescent knots exist). Yamada verified algebraic knots to 21 crossings; Tuzun-Sikora arXiv:1809.02285 covers algebraic knots at 24.
    - source: Stoimenow Sec. 4.2; Tuzun-Sikora arXiv:1606.06671 intro
    - kind: not_found
  -
    - claim: Crossing-number verifications: Dasbach-Hougardy 17 (Exp. Math. 1997); Yamada 18; Thistlethwaite 21 (private comm.); Tuzun-Sikora 22 (JKTR 27 (2018) 1840009, arXiv:1606.06671), 23 (arXiv:1809.02285), 24 (arXiv:2003.06724, JKTR 2021). Inference: a Jones-trivial knot needs >=25 crossings.
    - source: Tuzun-Sikora papers
    - kind: theorem_in_source
  -
    - claim: Thistlethwaite 'found examples of 15-crossing two-component links with the Jones polynomial of the unlink of 2 components' (JKTR 10 (2001) 641-643). Whether all links with <15 crossings were excluded: not found (Kauffman's abstract page unreachable).
    - source: Tuzun-Sikora arXiv:1606.06671 intro
    - kind: theorem_in_source
  -
    - claim: No theorem bounding bridge number of a Jones-trivial link found. The results above imply such links are not alternating, adequate, semiadequate, almost alternating, Montesinos, or 3-braid closures, so braid index >=4 (cf. Bigelow arXiv:math/0012086: a nontrivial 4-braid in the Burau kernel would yield one).
    - source: inference
    - kind: inference
  -
    - claim: (5) No result found where V decides splitness for 2-component links with an unknotted component and lk=0. A split K u U has V = u*V_K (standard); EKT 2-component families have knotted alternating components, so they neither confirm nor refute such a statement. Khovanov analogue: Hedden-Ni (unlink, 2013); Lipshitz-Sarkar: 'the module structure on Khovanov homology detects split links', Amer. J. Math. 144 (2022), arXiv:1910.04246.
    - source: search; Lipshitz-Sarkar abstract
    - kind: not_found

### relevance

For a 3-bridge program: the question is open, with only the Montesinos and closed-3-braid subclasses settled (semiadequacy, Stoimenow 2011). Known Jones-trivial links are Hopf-link satellites whose components are 2-bridge knots, so by the component-sum bound they are not 3-bridge; no 3-bridge counterexample is on record.


## Agent: read:band


### facts

  -
    - claim: Setting F=Z/2Z, Bar-Natan complex over F[h]. Def 1.1: u(K):=max order of h-torsion in H_BN(K). Thm 1.2: 'u(K) is a lower bound for the unknotting number of K', proved via crossing-change chain maps f_c^±: C_BN(K_±)→C_BN(K_∓) whose two composites act on homology as multiplication by h.
    - source: Alishahi, The Bar-Natan homology and unknotting number, arXiv:1710.07874 (2017); Pacific J. Math. 301 (2019)
    - kind: theorem_in_source
  -
    - claim: u_X(K):=maximal order of X-torsion in H_Lee(K) (lift of Lee's complex, X^2=t, Q-coefficients). Thm 1.2: u_X(K)≤u(K) (crossing-change maps with composites ±2X). Lee spectral sequence collapses at page 1+(max order of t-torsion), ⌈u_X/2⌉=u_t. Thm 1.3: u(K)≤2, K nontrivial ⇒ collapse at E_2 (Knight Move Conjecture for u≤2).
    - source: Alishahi-Dowlin, The Lee spectral sequence, unknotting number, and the knight move conjecture, arXiv:1710.07875 (2017)
    - kind: theorem_in_source
  -
    - claim: Lemma 2.2: if L is obtained from K by an oriented saddle with attaching points q,q′, and f:C_BN(K)→C_BN(L), f̄:C_BN(L)→C_BN(K) are the cobordism maps for the saddle and its inverse, then f̄∘f(a)=ha+x_q(a)+x_{q′}(a) (x_p = basepoint action, x_p∘x_p=hx_p). Lemma 2.1: p,q on opposite sides of one crossing ⇒ x_p+x_q≃h.
    - source: Alishahi, arXiv:1710.07874, Section 2
    - kind: theorem_in_source
  -
    - claim: Lemma 4.3: a saddle followed by its reverse acts on Lee's perturbation Kh_L as (dot on strand 1)+(dot on strand 2), up to sign; Lemma 4.1: dot position within a component is immaterial. Thm 1.1: ribbon distance d ⇒ (2X)^d Kh_L(K)≅(2X)^d Kh_L(K′). Cor 1.2: extortion order xo(K)≤ ribbon distance from the unknot (any field with 2≠0).
    - source: Sarkar, Ribbon distance and Khovanov homology, arXiv:1903.11095; Algebr. Geom. Topol. 20 (2020)
    - kind: theorem_in_source
  -
    - claim: Cor 2: xo(K)≤u_b(K), the minimum number of oriented band moves taking K to an unlink (field with 2 invertible). Cor 1: a cobordism F:K_1→K_0 with M deaths gives xo(K_0)≤max{M,xo(K_1)}+2g(F).
    - source: Zhuang, Knot cobordism and Lee's perturbation of Khovanov homology, arXiv:2201.01910 (2022)
    - kind: theorem_in_source
  -
    - claim: An explicit statement of how rank or torsion order changes under one knot→two-component band move: not found (the three items above are the nearest).
    - source: arXiv/web searches
    - kind: not_found
  -
    - claim: Thm 1.1: weights w_c∈R on components give a spectral sequence E_k(L,w), E_1≅Kh(L;R), converging to Kh(⊔_r L(r);R) when w_c−w_d is invertible for distinct weights. Thm 1.2: b(L,w):=largest k with E_k≠E_∞ satisfies b(L,w)≤sp(L). Thm 1.3: rank Kh^{i,j}(L;F_2)=rank Kh^{i,j}(U^m;F_2) for all i,j ⇒ L is the unlink. Cor 1.6: rank Kh(L;F)≥rank ⊗_c Kh(K_c;F) over any field.
    - source: Batson-Seed, A link splitting spectral sequence in Khovanov homology, Duke Math. J. 164 (2015), arXiv:1303.6240
    - kind: theorem_in_source
  -
    - claim: Thm 1: for 2-component L with basepoints p,q on the two components, reduced Kh~(L;F_2) (w.r.t. p), as an F_2[X]/(X^2)-module via q, is free iff L is split; generally a 2-sphere in S^3∖L separating p,q exists iff Kh~(L;F_2) is free. Cor 1.3: unreduced version, freeness over F_2[W,X]/(W^2,X^2). Split⇒free is due to Shumakovitch.
    - source: Lipshitz-Sarkar, Khovanov homology detects split links, Amer. J. Math. 144 (2022), arXiv:1910.04246
    - kind: theorem_in_source
  -
    - claim: n-component L: rank Kh(L)≥2^n; equality with Z/2 coefficients iff L is an iterated connected sum/disjoint union of Hopf links and unknots.
    - source: Xie-Zhang, Classification of links with Khovanov homology of minimal rank, arXiv:1909.10032 (2019)
    - kind: theorem_in_source
  -
    - claim: Inference: V_L=V_{U_2} forces det L=|V_L(−1)|=0; the 2-component minimal-rank links are U_2 and the Hopf link (det 2), so rank Kh(L;F_2)=4 ⇒ L=U_2, otherwise rank≥6 (Euler-characteristic parity). Jones data alone never gives the module structure needed above.
    - source: derived from the Xie-Zhang and Batson-Seed items
    - kind: inference
  -
    - claim: Khovanov-homology statements specific to links obtained from the unknot by one band move: not found. Band-surgery literature calls these band-trivializable and settles prime links ≤9 crossings using signature, Jones and Q evaluations, Arf (wording seen only through an abstract listing).
    - source: Kanenobu, Band surgery on knots and links, II, J. Knot Theory Ramifications 21 (2012)
    - kind: not_found
  -
    - claim: A statement 'band move on the unknot + Jones polynomial of the unlink ⇒ split': not found.
    - source: arXiv/web searches
    - kind: not_found
  -
    - claim: Inference: replacing the band by a crossing gives knots K_+, K_−=U with common oriented smoothing L; the skein relation yields V_{K_+}=1 ⟺ V_L=V_{U_2}, and the Montesinos trick gives Σ(K_+)=S^3_{±1/2}(J), Σ(L)=S^3_0(J). So (5) is the unknotting-number-one case of the Jones unknot problem.
    - source: elementary skein/Montesinos argument
    - kind: inference
  -
    - claim: Nontrivial k-component links with V=V_{U_k} exist for every k≥2, so any (5)-type theorem must use the band hypothesis; whether any such 2-component example is band-trivializable: not found.
    - source: Eliahou-Kauffman-Thistlethwaite, Infinite families of links with trivial Jones polynomial, Topology 42 (2003)
    - kind: theorem_in_source
  -
    - claim: Preprint claims 'a knot whose Jones polynomial is equal to that of the unknot must itself be the unknot' (finite-type coefficients up to order 3c(K)); unrefereed, no independent verification found.
    - source: Carmi-Cohen, On trivial Jones-Vassiliev polynomials, arXiv:2606.22410 (June 2026)
    - kind: theorem_in_source

### relevance

For the unknotting-number-one route to the Jones unknot problem: u=1 forces h-torsion order ≤1 (Alishahi) and E_2 collapse of the Lee sequence (Alishahi-Dowlin); the saddle-composite formulas (Alishahi 2.2, Sarkar 4.3) are the only algebraic bridge between Kh(K) and Kh(L); split detection needs the F_2[X]/(X^2) module structure (Lipshitz-Sarkar), invisible to the Jones polynomial; no source reaches (5), and the June-2026 preprint claiming the full conjecture is unverified.


## Agent: read:pattern


### facts

  -
    - claim: Encircling lemma: a 0-framed unknot around a strand carrying the Jones-Wenzl idempotent f_k equals λ_k·f_k, λ_k = −(A^{2k+2}+A^{−2k−2}); coloured Hopf link ⟨e_i,e_j⟩ = (−1)^{i+j}[(i+1)(j+1)]. arXiv:1912.11779 (p.36) cites it as 'By Lemma 14.2 in [14], |J_{M1,M2}(W,t)| = |[M1 M2]/[M1]·J_{M1}(U,t)|'.
    - source: Lickorish, An Introduction to Knot Theory, GTM 175 (1997), Lemma 14.2; Kirby-Melvin, Invent. Math. 105 (1991) 473-546 (coloured Hopf-link matrix)
    - kind: theorem_in_source
  -
    - claim: KBSM(S^1×D^2) = Z[A^±][z], free on z^n (z = core); the annular closure of f_n is the Chebyshev polynomial S_n(z); the standard embedding sends e_n to Δ_n = (−1)^n[n+1].
    - source: Turaev, Zap. Nauchn. Sem. LOMI 167 (1988) 79-89; Przytycki, Bull. Polish Acad. Sci. 39 (1991) 91-100 and arXiv:math/9809113 Thm 3.1; Bonahon-Wong arXiv:1206.1638 Lemma 26 (proof credited to Lickorish Ch. 13)
    - kind: theorem_in_source
  -
    - claim: (1) If P = Σ c_k e_k then ⟨U∪P⟩ = Σ c_k λ_k Δ_k (normalisation ⟨∅⟩ = 1). (2) The identity holds: z^n is n meridians of U, each removed at cost λ_1, so ⟨U∪P⟩ = δ·f_P(−A^4−A^{−4}) with f_P the annular class; check: δ·S_i(λ_1) = (−1)^{i+1}[2i+2] = ⟨e_i,e_1⟩. Wrapping 2, winding 0: f_P = f(T)z^2 + g(T)δ where ⟨T⟩ = f(T)·0 + g(T)·∞ (EKT bracket vector), so ⟨U∪P⟩/δ = f(T)(A^4+A^{−4})^2 + g(T)δ.
    - source: my derivation from the two facts above
    - kind: inference
  -
    - claim: Identity (2) stated as 'δ times the annular bracket at z = −(A^4+A^{−4})': not found. Closest published form: EKT Prop. 2.1', ⟨H(T,U)⟩ = br(T)^t·H·br(U), h00 = −a^{−14}−a^{−6}−2a^{−2}−2a^2−a^6−a^{14}, h01 = δ^2, h11 = δ (⟨O⟩ = 1), where both Hopf components carry 2-strand tangles.
    - source: Eliahou-Kauffman-Thistlethwaite, Topology 42 (2003) 155-169, §2
    - kind: not_found
  -
    - claim: All published Jones-trivial 2-component links are H(T,U) (numerators of tangles T, U clasped together): 'The sublinks T^N, U^N of H(T,U) lie in solid tori V_T, V_U, respectively, whose cores form a Hopf link', each meeting a cross-sectional disk in two points, so BOTH components are wrapping-number-2 patterns. Families: LL2(n) = H(T_n,−T_n), T_n = 5·(1·4)^{2(n−1)}·1·2; LL1(m,n) = H((T_{m,n})^ω, −3); ω: T ↦ (T+2)·1·2 preserves the bracket (Thm 3.2).
    - source: EKT 2003 §§2-4; Thistlethwaite, J. Knot Theory Ramif. 10 (2001) 641-643
    - kind: theorem_in_source
  -
    - claim: Component types: in EKT's convention D(n) is the unknot (proof of Prop. 4.2), hence N(−3) = T(2,−3): every LL1(m,n) has a trefoil component; EKT prove the numerators of the T_n are pairwise distinct 2-bridge knots. Thistlethwaite's 15-crossing link is LL1(0,0) = H(2·2,−3) (survey arXiv:1407.2196 §5.2: T = −1, U = ∞+2, then ω): sublinks figure-eight and trefoil, 4+3+8 crossings. So no published example has an unknotted component.
    - source: inference from EKT 2003 definitions
    - kind: inference
  -
    - claim: Jones-trivial U∪P with U unknotted and P of wrapping number 2 in S^3∖U: no example and no non-existence theorem found. Encyclopedia of Mathematics ('Jones unknotting conjecture'): 'this and similar examples constructed since are 2-satellites on a Hopf link'. Related only: Whitehead doubles of semiadequate knots have non-trivial Jones polynomial (knots, not U∪P).
    - source: encyclopediaofmath.org/wiki/Jones_unknotting_conjecture; Stoimenow arXiv:math/0606255
    - kind: not_found
  -
    - claim: Criterion (EKT's test ⟨D⟩ = δ^{k−1}(−a^3)^{wr(D)}, k = 2, clasp writhe 0 since lk = 0): U∪T^N is Jones-trivial iff f(T)(A^4+A^{−4})^2 + g(T)δ = δ(−A^3)^{wr(T)}. A^4+1 is prime in Z[A^±] and coprime to A^8+1, so (A^4+1) | f(T) is necessary.
    - source: my inference
    - kind: inference
  -
    - claim: Four-point annular modules. All 2n points on the outer circle: the relative KBSM 'is a free R[α] module with (2n choose n) free generators, where α is represented by a longitude of the annulus' (Cor. 3.12(b)); rank 6 for four points. n points on each boundary: ATL_n = R[α]⟨t,e_1,…,e_{n−1}⟩/I(n) (Thm 3.13, after Jones 1994 and tom Dieck); infinite rank over R[α] since t has infinite order (inference). Graham-Lehrer's affine TL category (Enseign. Math. 44 (1998) 173-218) is equivalent to the skein category of the annulus.
    - source: Przytycki arXiv:math/9809113; Al Qasimi-Stokman arXiv:1710.04058; Queffelec-Wedrich arXiv:1701.02316
    - kind: theorem_in_source

### relevance

For the one-patterned Hopf satellite U∪P the bracket is δ times the evaluation homomorphism z ↦ −A^4−A^{−4} on the annular skein class, so Jones-triviality is one polynomial condition on the TL_2 coefficients (f(T), g(T)) of the defining tangle, with (A^4+1) | f(T) forced. The EKT/Thistlethwaite examples do not settle this case: they pattern both Hopf components and have no unknotted component. Existence of a Jones-trivial U∪P with unknotted U and wrapping number 2 appears open in the literature searched.


## Agent: read:ekt


### facts

  -
    - claim: Template: every EKT example is H(T,U) (Fig. 1), the 2-strand parallel of the Hopf link with tangle boxes T, U spliced in; EKT describe it as clasping together the numerator closures T^N, U^N, which lie in solid tori V_T, V_U whose cores form a Hopf link. Both components are patterned; the clasp has 8 crossings.
    - source: Eliahou-Kauffman-Thistlethwaite (EKT), Infinite families of links with trivial Jones polynomial, Topology 42 (2003) 155-169, pp.156-159; homepages.math.uic.edu/~kauffman/ekt.pdf
    - kind: theorem_in_source
  -
    - claim: Thistlethwaite's note: the examples are all satellites of the Hopf link; two 2-component links (15 and 17 crossings) have V = u, two more (14, 17 crossings) have t^{±6}u, a 16-crossing 3-component link has V = u²; the links 'may be distinguished from one another (and from the unlink) by the knot types of their components'.
    - source: Thistlethwaite, Links with trivial Jones polynomial, JKTR 10(4) (2001) 641-643; preprint homepages.math.uic.edu/~kauffman/tj.pdf
    - kind: theorem_in_source
  -
    - claim: The 15-crossing link is EKT's LL1(0,0) = H(2·2, −3): T_{0,0}^ω = 0·1·1·1·2 has fraction 5/2, so T^N = N(5/2) = figure-eight, U^N = N(−3) = trefoil; 4+3+8 = 15 crossings. EKT §5 attributes LL1(0,−2), LL1(0,−1), LL1(0,0), LL1(0,1), LLL(0) to the enumeration; crossing counts 17, 14, 15, 17, 16 match the note. Neither component is unknotted.
    - source: EKT §§4.2, 5; Wikipedia 'Jones polynomial' ('a trefoil knot linked to a figure-eight knot'); Amankwah, The Jones polynomial and its limitations, arXiv:1407.2196 (seed T=−1, U=∞+2)
    - kind: inference
  -
    - claim: Linking number of the 15-crossing link is 0: 5/2 (odd/even) joins NW-SW and NE-SE, so the figure-eight's two clasp arcs are antiparallel and the 8 clasp crossings cancel; consistent with its writhe −3. Generally lk(H(T,U)) ∈ {0, ±4}, and the V = t^{±6}u members are exactly the lk = ±4 ones.
    - source: Inference from EKT Fig. 1, §§3-5 (Remark 3 treats lk ±4); writhe −3 from Amankwah arXiv:1407.2196
    - kind: inference
  -
    - claim: EKT p.160: 'since there exists a cross-sectional disk of V_T meeting T^N transversely in two points, every cross-sectional disk of V_T which is transverse to T^N must meet T^N in an even number of points'; T^N is geometrically essential in V_T iff T admits no NS-separating disk, and the only rational tangle admitting one is ∞.
    - source: EKT pp.159-160
    - kind: theorem_in_source
  -
    - claim: Hence each component of every rational-tangle example, including both components of the 15-crossing link, has wrapping number exactly 2 about its own Hopf core. One component's intersection with a spanning disk of the other is not discussed anywhere; the 15-crossing link has no unknotted component.
    - source: EKT pp.159-160
    - kind: inference
  -
    - claim: Bridge numbers: not found in any source; trivially ≥ 4 for the 15-crossing link (two 2-bridge components).
    - source: EKT 2003; Thistlethwaite 2001; web/arXiv searches
    - kind: not_found
  -
    - claim: ⟨T⟩ = f(T)⟨0⟩ + g(T)⟨∞⟩, br(T) = (f(T), g(T)). Prop 2.1′: ⟨H(T,U)⟩ = br(T)^t·ℋ·br(U), with h00 = ⟨H(0,0)⟩ = −a^{−14} − a^{−6} − 2a^{−2} − 2a² − a⁶ − a^{14}, h01 = h10 = ⟨H(0,∞)⟩ = δ², h11 = ⟨H(∞,∞)⟩ = δ, δ = −a^{−2} − a². V is trivial iff ⟨D⟩ = δ^{k−1}(−a³)^{wr(D)}.
    - source: EKT §2, pp.156,158-159
    - kind: theorem_in_source
  -
    - claim: EKT solve no linear condition on one tangle; they apply a bracket-preserving operator to unlink seeds: T^ω = (T+2)·1·2, T^ω̄ = (T−2)·(−1)·(−2), with T·U := T^ρ + U (ρ: NW-SE reflection). Prop 3.1: br(T^ω) = Ω·br(T), br(T^ω̄) = Ω^{−1}·br(T), Ω = M_+²M_*M_+² (entries p.163). Thm 3.2: ⟨H(T,U)⟩ = ⟨H(T^ω,U^ω̄)⟩ because Ω^tℋΩ^{−1} = ℋ. Seeds: H(∞−2, ∞+2) gives LL2(n) = H(T_n, −T_n), T_n = ω^n(∞−2); H(T_{m,n}, ∞+2), T_{m,n} = n·1·(1·1/2)^m·(−1) with N(T_{m,n}) unknotted, gives LL1(m,n) = H(T_{m,n}^ω, −3). Thms 4.1/4.3: V = u except (LL2(n), n odd) and (LL1(0,n), n odd), where V = t^{±6}u.
    - source: EKT §§3-4, pp.162-166
    - kind: theorem_in_source
  -
    - claim: All displayed 2-component EKT examples have two nontrivial 2-bridge components: LL1(0,n) = N((8n+5)/(3n+2)) ∪ trefoil; LL2(n) components are distinct 2-bridge knots (proof of Thm 3.3). No Jones-trivial example with an unknotted component appears in EKT.
    - source: EKT §§3.3, 4; fraction computed with EKT's product convention
    - kind: inference
  -
    - claim: Later papers: Eliahou-Fromentin, A remarkable 20-crossing tangle (arXiv:1610.05560): knots with V ≡ 1 mod 2^r, no links. Ganzell, Local moves and restrictions on the Jones polynomial, JKTR 23 (2014): knot divisibility results only. Ganzell-Huffman-Mavrakis-Tademy-Walker, Unoriented links and the Jones polynomial, Involve 12 (2019): no Jones-trivial links. Encyclopedia of Mathematics, Jones unknotting conjecture: known examples are '2-satellites on a Hopf link'. No source gives a Jones-trivial 2-component link with an unknotted component and wrapping number exactly 2.
    - source: As cited; Drube-Pongtanapaisan arXiv:1903.04033 summarizes Ganzell 2014
    - kind: not_found

### relevance

Thistlethwaite's link and all EKT 2-component examples are Hopf-link satellites with both components knotted, each of wrapping number 2 in its own solid torus; no Jones-trivial link with an unknotted wrapping-2 component was found.


## Agent: read:sakuma


### facts

  -
    - claim: Sakuma's link, restated from [Sak86]: take a preferred longitude l of K with τ(l)∩l=∅; with p:S^3→S^3/τ≅S^3 set O=p(Fix τ), L=p(l); then "L(K,τ)=O∪L is a two-component link in S^3 and lk(O,L)=0". Boyle-Issa §1 phrase it as the axis of symmetry plus "the quotient of two parallel push-offs" of K.
    - source: Mukohara, Strong corks derived from the Akbulut cork, arXiv:2601.02230 §4; Borodzik-Dai-Mallick-Stoffregen, Khovanov homology and equivariant surfaces, arXiv:2507.13642 Def. A.1; Boyle-Issa, Equivariant 4-genera of strongly invertible and periodic knots, arXiv:2101.05413 §1
    - kind: theorem_in_source
  -
    - claim: Both components of a Sakuma link are unknotted (L is l∪h(l) "glued together near the points of intersection of K with Fix(h)"); lk=0 is Prop. 3.1.1. Sakuma's algorithm starts from a projection of the quotient θ-curve θ(K,h)=O∪p(K): L runs as two parallel strands along the arc p(K), except where the strands twist about each other, clasp around O, or coil around O.
    - source: Framba, Equivariant concordance and 2-bridge knots, MSc thesis Pisa 2022 (etd-10122022-153438) §3.1-3.2; Snape, PhD thesis Glasgow 2018 §2.1.4
    - kind: theorem_in_source
  -
    - claim: So Sakuma's link is neither a pair of cycles of c∪α nor the band move of c along α: it keeps the axis c=O, and its second component is ∂ of the quotient of the invariant 0-framed annulus, i.e. a thin band around α closed by clasps around O at the two vertices (slope-0 curve on ∂N(α)). The band move of O along α (both non-axis constituent knots pushed apart) is instead the family of two-component rational closures of the quotient tangle.
    - source: derived from the definitions in facts 1-2 and Watson §2.2
    - kind: inference
  -
    - claim: Quotient tangle arcs are "the image of the fixed point set in the quotient"; for the unknot "T(1) is the two-component trivial link and T(2) and T(0) are both trivial knots". ϰ(K,h) is the inverse limit of Kh over closures T(n); Theorem 1: ϰ(K,h)=0 iff K trivial. η is called "Alexander-like" and vanishes for the trivial knot.
    - source: Watson, Khovanov homology and the symmetry group of a knot, Adv. Math. 313 (2017), arXiv:1311.1085 §2.2, §3.3
    - kind: theorem_in_source
  -
    - claim: η_{(K,τ)}(t)=Σ_i lk(L̃′,t^i L̃)t^i ∈ Z[t^{±1}], L̃ the lift of L to the infinite cyclic cover of S^3∖O, L̃′ the lift of a preferred longitude of L; an invariant of Sakuma equivalence; "equivalently the Z[t,t^{-1}] equivariant self-linking of λ_τ in S^3∖O_τ".
    - source: Mukohara arXiv:2601.02230 §4; BDMS arXiv:2507.13642 Def. A.1
    - kind: theorem_in_source
  -
    - claim: Properties: η(t)=η(t^{-1}), η(1)=0, unlink↦0, topological concordance invariant of lk-0 links (KY79, Thm 7 in Boyle-Issa). For strongly invertible knots η is an equivariant concordance invariant, additive under equivariant connected sum (Sakuma Thm III), hence a homomorphism C̃→Z[t,t^{-1}] vanishing on equivariantly slice knots; it ignores the direction ("Unlike Sakuma's polynomial, our concordance invariants are sensitive to the choice of direction"). BDMS Thm A.4: invariant under locally flat equivariant concordance.
    - source: Boyle-Issa Thm 7, §4; Framba Thm 3.3.1, Rem. 3.3.2; BDMS App. A
    - kind: theorem_in_source
  -
    - claim: Detection limits: η=0 whenever K is amphicheiral with a unique strong inversion [Sak86 Prop 3.4(1)]; η(9_9,h_1)=η(9_9,h_2)=−2t^{-2}+4−2t^2; η(10_155,h_1)=0, η(10_155,h_2)=2t^{-2}−4+2t^2; η(8_20)=0; both inversions on 8_9 have η=0 yet are not equivariantly slice; η(T(−m,2))=η(T(−m−2,2)) for m=4k−1 while the annular Jones polynomial separates them.
    - source: Watson 2017 Prop 21, Figs 6-8, Rem 27; Boyle-Issa §1, §4; Snape thesis Prop 3.4.1
    - kind: theorem_in_source
  -
    - claim: Snape: J_{(K,h)}(q):=J(L) for the Sakuma link (Def 3.2.3), used only for ε-amphicheirality, then dropped "in favour of its annular counterpart" (annular Sakuma knot L⊂A×I=E(O)). Thm 0.1.1: (K,h)≅(U,h_0) ⟺ dim_F Kh(L)=4. Thm 0.1.2: annular Kh of either component detects the unlink. §3.5 bounds intrinsic symmetry groups (Cor 3.5.1; Prop 3.5.3: (U,h_0,0) gives the unlink, (U,h_0,−2) gives 5^2_1). Lemma 2.1.9: "Sakuma links are prime. Sakuma links are clearly non-trivial and non-split" (no proof; tacitly excludes the trivial knot).
    - source: Snape, Homological invariants of strongly invertible knots, PhD thesis Glasgow 2018, theses.gla.ac.uk/39015
    - kind: theorem_in_source
  -
    - claim: Lobb-Watson: Sakuma's invariant is Kojima-Yamasaki "applied to a 2-component link obtained through a quotient of the symmetry"; their triply graded refinement (axis filtration) is an involutive-link invariant detecting mutation and separating the inversions on 4_1 and 6_3; Couture's, Snape's and Watson's invariants "also arise by first passing to some auxiliary object via a quotient". Couture: Khovanov homology for signed divides categorifies his polynomial of strongly invertible links; relation to ϰ "not clear" (Watson Rem 17).
    - source: Lobb-Watson, A refinement of Khovanov homology, Geom. Topol. 25 (2021), arXiv:1908.00082 §1; Couture, Algebr. Geom. Topol. 9 (2009) 1987-2026
    - kind: theorem_in_source
  -
    - claim: Boyle-Issa: butterfly link L_b(K)=band move on K along a band containing the chosen half-axis, lk 0 (Def 4.1); quotient butterfly link L_qb(K)=quotient of L_b(K) plus the axis, lk=2·lk̃(K) (Def 4.7); η(L_qb) is a homomorphism on ker lk̃ (Prop 10). Di Prisa: θ(K)=K∪half-axis gives θ:C̃→Θ and "one of the parallel link of θ(K) is ... exactly the butterfly link". Lipshitz-Sarkar: quotient knot = arc ∪ part of the axis ("two equally natural choices"); spectral sequence Kh(K)⊗F_2[θ^±] ⇒ annular Kh of the pair; K_0 is the butterfly link; Jones congruence J_K≡J_K̄ is "vacuous" (Rem 4.7).
    - source: Boyle-Issa arXiv:2101.05413 §4; Di Prisa, arXiv:2207.04985 §3.2; Lipshitz-Sarkar, arXiv:2203.13895 (PSPUM 109, 2024) §1, §4
    - kind: theorem_in_source
  -
    - claim: KWZ: bijection between nontrivial (K,h) and 4-ended tangles with τ(∞) unknotted, τ(0) ↔ Seifert-longitude surgery; Khovanov multicurves of quotient tangles for ≤9 crossings. KLMWZ: "Kh and BN detect if a Conway tangle is split"; equivariant cosmetic surgery for strongly invertible knots.
    - source: Kotelskiy-Watson-Zibrowius, Khovanov homology and strong inversions, arXiv:2104.13592; Kotelskiy-Lidman-Moore-Watson-Zibrowius, Math. Ann. 389 (2023), arXiv:2109.14049
    - kind: theorem_in_source
  -
    - claim: Not found: no statement "the quotient link of a nontrivial strong inversion is nonsplit" beyond Snape's unproved Lemma 2.1.9, and no theorem on the Jones polynomial of Sakuma links beyond Snape Def 3.2.3/§3.2.2. Sakuma's 1986 text itself is not online.
    - source: searches of arXiv, Glasgow/Pisa theses, msp
    - kind: not_found
  -
    - claim: Nonsplitness argument: a splitting ball for O∪L lifts under the double cover branched along O to two disjoint balls containing l and τ(l), so the 0-framed 2-cable l∪τ(l) would be split, forcing K trivial (knot exterior ∪ cable space is irreducible); (U,h_0) gives the unlink. For the band-move closures: a split τ(0) would make Σ(τ(0))=S^3_0(K) reducible with an S^1×S^2 summand, impossible for nontrivial K (Gabai, Property R); Σ(τ(2n))=S^3_{2n}(K), n≠0, has finite H_1.
    - source: my inference from facts 1-4, Montesinos trick, Gabai 1987
    - kind: inference

### relevance

(1) Sakuma's link is the quotient axis O together with the quotient of a preferred longitude l disjoint from τ(l); on the quotient θ-curve it is two parallel strands along α closed by clasps around O, not a pair of cycles. (2) It is not the band move of the axis along α; that band-move family is Watson's two-component closures of the quotient tangle, while the butterfly link is the band move upstairs along a half-axis. (3) η = Kojima-Yamasaki self-linking of L in the infinite cyclic cover of S^3∖O; equivariant (also topological) concordance homomorphism, direction-blind, vanishing for amphicheiral/unique-inversion knots and some non-slice examples. (4) Watson, Snape, Lobb-Watson, Couture, KWZ, Lipshitz-Sarkar, Boyle-Issa, Di Prisa, BDMS. (5) Only Snape's one-line Lemma 2.1.9 asserts nonsplitness; a proof is given as inference.
