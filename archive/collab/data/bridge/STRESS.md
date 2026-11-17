# STRESS.md: skeptic pass on the four THEORY-MAP programs

17 Nov 2026. Skeptic: Claude (subagent). Mandate: for each program try to show it is (a) a trivial restatement importing no tool, (b) already known, or (c) false; default to the harsher verdict; record the strongest surviving form.
Status: working notes, written continuously. Nothing here has outside review.

## Log
- start: read CONTEXT.md and THEORY-MAP.md.
- read L2. Two immediate attacks found (details in the program sections below):
  * P1: Theorem S does not need Brownawell-Masser. All "S-units" are monomials in ONE variable A, so the unit locus is decided by exponent coincidences (a linear arrangement in n). Elementary 10-line proof written below. The function-field import is decorative.
  * P4: S6 (growth obstruction via Bar-Natan) is subsumed by L2 4.1(i): if ord_{t=1} g_phi <= r0 then the zero test is decided by the r0-jet of V at t=1, which is polynomial-time (GPV Gauss-diagram formulas). So the gadget's zero set is in P, for ANY N, not just N = #SAT.
- PRIOR ART HIT (P1): Champanerkar-Kofman, "On links with cyclotomic Jones polynomials", Algebr. Geom. Topol. 6 (2006) 1655-1668, arXiv:math/0605631 (text extracted to scratchpad stress/ck06/ck06.txt). Contains:
  * Def 1 + Prop 2.1: twist-bracket P(A,x_1..x_k) = sum_s prod_i (x_i - 1)^{s_i} delta^{1-s_i} <L~_s>, and delta^k <L_n> = A^{sigma(n)} P(A, (-A^-4)^{n_1}, ..., (-A^-4)^{n_k}). This IS Program 1's expansion y(n) = A^{|n|} sum_eps c_eps (-A^-4)^{<eps,n>}.
  * Example 4: Kanenobu K(p,q) has P(A,x,y) = delta^2(<8_9> - 1 + xy): the Kanenobu invisible direction (1,-1) is "P depends on x,y only through xy". Example 5: K(n_1..n_k), P depends only on prod x_i.
  * Prop 2.2: one site, P(A,x) = x f(A) => V(L_n) = V(L) for all n; proof by evaluating at A = 1 (<L> = (-1)^c (-2)^{mu-1}) forces the component count to jump and the strands at the site to be antiparallel. (This A = 1 argument is also the content of "Astra's connectivity lemma".)
  * Lemma 3.1 (Boyd: M(F) = 1 iff monomial times cyclotomics in monomials), Lemma 3.2-3.3 (Boyd-Lawton with signs), Lemma 3.4 (bounded nu => pass to a subsequence on a fixed hyperplane a.x = 0: this is the "resonant sublattice" step), Example 6 (limit in one fewer variable on the resonant hyperplane).
  * Prop 4.1: one site: distinct V(L_m) are cyclotomic for only finitely many m. Thm 1.1: cyclotomic Jones polynomials of growing span force unbounded twist number.
  So R3, the multilinear set-up, the Kanenobu caveat and the resonant-hyperplane mechanism are all in print since 2005-06. Also CK05 (Algebr. Geom. Topol. 5 (2005) 1-22, arXiv:math/0404236): Mahler measure of Jones and coloured Jones converges under twisting; coefficient vectors split into fixed blocks after many twists (= the generic-partition statement, i.e. R1/R2 generic case).
- P2 literature (KWZ, "Khovanov multicurves are linear", arXiv:2202.01460; text in scratchpad stress/kwz22/kwz22.txt):
  * Thm 1.2: every component of Khr(T) is rational or special. Thm 5.1: every special component is s_{2n}(p/q), n >= 1, TRIVIAL local system. Thm 5.4: every rational component is r_n(p/q), trivial local system. Thm 5.6: odd-length rational components are based on the ends that T connects.
  * So L1's hypothesis H ("KWZ Conj 3.6/3.7 geography") is now essentially a THEOREM. Remaining gap: rational components r_{2m}(inf) of even length and slope inf are not excluded by Thms 5.4/5.6 (KWZ remark before Cor 5.7: no tangle known with a rational component of length >= 3; length 2 not addressed). THEORY-MAP's "conditional on KWZ Conjectures 3.6/3.7" is out of date.
  * Thm 4.4 (extension property): the whole type D structure extends over B*[U] = B^infty (x) F[U], with mu_k weighted by U^{k-2}. The only obstruction used (Thm 4.1) is a local configuration inside one component (wrapping the special puncture); its U^2-times-idempotent term can be cancelled only by pure-U arrows, which KWZ exclude by a parity fact (generators in one idempotent have equal q-parity). Lemma 5.2 (H.id null-homotopic) is proved summand by summand.
  * Remark 5.3: for Khr, extendability alone does NOT force s_{2n} (their Fig. 15 gives an extendable non-s_{2n} curve). So extension is a weak constraint even on single components.
- SANITY RUN (scratchpad stress/code/coincidence.py, 95 s): exponent-coincidence linear algebra in v = (n1,n2,m) (unknown target exponent m as an extra variable) on L2's twist2 family. Output: positive-rank families only along the axes n1 = 0, n2 = 0; isolated unit points exactly {(1,-2),(-1,2),(2,-1),(-2,1)}; brute force on |n_i| <= 40 agrees. This is L2's grid answer, now GLOBAL, with no Brownawell-Masser window. Confirms the BM import is decorative.
- P4 prior art: Hass-Lagarias-Pippenger (J. ACM 46 (1999), arXiv:math/9807016, Sec. 1) quote Welsh (Complexity: Knots, Colourings and Counting, CUP 1993): an affirmative answer to JC "would yield an algorithm in P^#P for recognizing trivial knots". So the sandwich is a 1993 observation; C=P and NP cap coNP are routine refinements.
- P3 prior art: Eliahou-Fromentin, "A remarkable 20-crossing tangle", arXiv:1610.05560 (JKTR 2017): a 20-crossing tangle invisible to the bracket pair mod 2 gives prime knots K_r with V == 1 mod 2^r. This is the published state of the art for "tangle mechanisms toward J/V = 1 for knots".

---------------------------------------------------------------------------------------------------
# VERDICTS (summary table; details follow)

| Program | Verdict | One-line reason |
|---|---|---|
| P1 Two-place Diophantine geometry of twist families | ALREADY_KNOWN (and its new part is TRIVIAL) | Twist-bracket expansion, Boyd/Lawton Mahler limits, resonant hyperplanes and the Kanenobu invisible direction are all in Champanerkar-Kofman (AGT 2005, 2006). Theorem S needs no Brownawell-Masser: it is exponent-coincidence linear algebra (checked globally on L2's family). |
| P2 Positional rigidity of Watson's kappa | FALSE (Conjecture P as stated) | Every congruence on special positions that J can see contains the flat position, because J = 1 obeys every law of J. B*[U]-extension is checked component by component in KWZ, so by the block-extension lemma it cannot see relative shifts. Positive side: L1's hypothesis H is now essentially a theorem (KWZ arXiv:2202.01460). |
| P3 Link/knot boundary (band distance one, doubles, EKT) | TRIVIAL | (B) and (D) are equivalent to Lemma Q (the program says so). The categorified version is Hedden-Ni / Batson-Seed. The "connectivity lemma" is V_L(1) = (-2)^{mu-1} (Jones 1985; used the same way in CK06 Prop 2.2). Survives only as a falsification screen. |
| P4 Exact counting gadgets / complexity | TRIVIAL (for JC) | The sandwich is Welsh 1993 (via HLP 1999) plus routine refinements. "JC is equivalent to non-existence of gadgets" is false as an equivalence. S6 is a weak corollary of the bounded-jet observation already in L2 4.1(i). The only surviving content is an open complexity question that does not bear on JC. |

---------------------------------------------------------------------------------------------------
## P1. Two-place Diophantine geometry of twist families

### Attack (b): already known. CONFIRMED.
Champanerkar-Kofman, AGT 6 (2006) 1655-1668 (arXiv:math/0605631) and AGT 5 (2005) 1-22 (arXiv:math/0404236). Item by item (details in the log above):
- The multilinear expansion is CK06 Def 1 + Prop 2.1: delta^k <L_n> = A^{sigma(n)} P(A, (-A^-4)^{n_1}, ..., (-A^-4)^{n_k}). Program 1's c_eps are the coefficients of P in the eigen-basis.
- R3 (Mahler measure converges off resonant sublattices) is CK05 (for V and all coloured V), proved with Boyd-Lawton (CK06 Lemmas 3.2-3.3, signs included).
- The resonance mechanism is CK06 Lemma 3.4 plus Example 6: bounded nu means passing to a subsequence on a fixed hyperplane, where the limit polynomial loses a variable.
- The Kanenobu caveat is CK06 Example 4: P(A,x,y) = delta^2(<8_9> - 1 + xy). An invisible direction is exactly "P depends on the slot variables only through a monomial".
- The one-slot invisible case is CK06 Prop 2.2: P = x f(A) gives constant V. Their A = 1 argument forces the component count to jump and the strands to be antiparallel.
- The "generic coefficient blocks" of R1/R2 are CK05: after many twists the coefficient vector splits into fixed blocks.
- So the claim "searches found no prior use for knot polynomials" (THEORY-MAP section 4, L2 section 3) is wrong. L2 cited CK05 but called it "different". It is the same object.

### Attack (a): the new part is trivial. CONFIRMED.
**Coset Lemma (elementary; replaces Theorem S).** Let y(n) = sum_eps c_eps (-1)^{<eps,n>} A^{<l_eps,n>}, with c_eps in Z[A^+-1] and l_eps affine-integral. Fix g != 0, the target up to monomials. Then U = {n : y(n) in +-g A^Z} is a finite union of affine lattices (rank 0 allowed). It is computable by linear algebra on the coincidence arrangement.

*Proof.*
1. Put v = (n,m). Write y(n) - s g A^m as a sum of signed monomials kappa_mu chi_mu(v) A^{e_mu(v)}, with e_mu affine in v and chi_mu a parity character.
2. Let Pi(v) be the partition of the monomials by the value of e_mu(v). The sum vanishes iff every block sums to 0. That condition depends only on (Pi(v), v mod 2).
3. Admissibility is preserved under coarsening: zero blocks merge to zero blocks.
4. Hence the zero set is the union, over admissible (Pi, rho), of L_Pi intersected with (rho + 2Z^{k+1}), where L_Pi = {v : e_mu(v) = e_nu(v) for mu ~ nu} is an affine lattice.
5. Project to n. QED.

*Consequences.*
- Sporadic points are vertices of the arrangement. Positive-rank cosets are flats whose generic block sums vanish. L2's "vanishing subsums", with exact windows.
- No function-field abc is used. The reason everything is easy is that all exponentials are monomials in the single variable A. So L2's comparison with Skolem's problem over Z (S2) is misleading: there is no Skolem difficulty here at all.
- CHECKED (stress/code/coincidence.py). On L2's twist2 family the method returns, globally: the axes, plus exactly {(1,-2),(-1,2),(2,-1),(-2,1)}. This matches brute force on |n_i| <= 40.

*k = 1 corollary.* A positive-rank coset forces one TL_2 channel of the slot to vanish identically (c_0 = 0 or c_1 = 0) and the other to be a unit times g. This is CK06 Prop 2.2's hypothesis.

*k >= 2.* A coset in direction w forces every class {eps : <eps,w> = j}, except the target class, to have identically vanishing signed sum. Kanenobu is the case w = (1,-1), c_10 = c_01 = 0.

### Attack (c): false?
- **C1, "the three resonances coincide": FALSE as stated, though harmlessly.** Lawton's exceptional set (bounded nu) is the union of ALL hyperplanes with small normal. The R2 resonances are the finitely many hyperplanes along which monomials actually coincide. So R3's set strictly contains R2's.
- **Conjecture R: not refuted.** But it is JC restricted to the coset families, and algebra cannot touch it (Kanenobu; CK06 Ex. 4-5). The topological input it needs is twist rigidity for families with constant unit J.
  - Single-slot cosets lift to annulus twists upstairs, because the crossing disk meets the branch set twice. Annulus twists are exactly the operation that produces infinitely many distinct knots with the same 0-surgery (Osoinach 2006). So "invisible direction implies trivial direction" has no general reason to hold.
  - Kouno-Motegi-Shibuya-type results need infinitely many unknots in the family as a hypothesis. That hypothesis is what Conjecture R is trying to prove, so using them here would be circular.

### Strongest surviving form
For each fixed body, the J-unit locus is an explicitly computable finite union of affine lattices. The proof is elementary, and the points are vertices of the coincidence arrangement. So Lemma Q on the body reduces to two pieces:
- (i) finitely many vertex points, which can be certified by the existing pipeline;
- (ii) finitely many positive-rank cosets. On each of these the slot polynomial factors through a monomial in the slot variables, in the sense of CK06 Prop 2.2 / Ex. 4.

On (ii), Lemma Q is equivalent to rationality of the whole coset family, an open twist-rigidity statement.

This is a useful certification engine for the arborescent programme (it upgrades finite searches to whole twist lattices up to explicit cosets). It is not a bridge: no outside tool does any work. Write it up citing CK05/CK06, not as a Diophantine import.

---------------------------------------------------------------------------------------------------
## P2. Positional rigidity of Watson's kappa

### Literature (positive correction first)
KWZ, arXiv:2202.01460:
- Thm 1.2: every component of Khr(T) is rational or special.
- Thm 5.1: specials are s_{2n}(p/q) with trivial local system.
- Thm 5.4: rational components are r_n(p/q) with trivial local system.

So L1's hypothesis H, and with it J = t^k + (t^4-1)P, is no longer conditional on KWZ Conj 3.6/3.7. One residual gap: even-length rational components r_{2m}(inf) of slope inf are not excluded by Thms 5.4/5.6, though none has ever been observed. THEORY-MAP sections 4.2 and 5 (W5) should drop "conditional on KWZ geography" and cite 2202.01460 instead.

### Attack (a): restatement
"No nontrivial quotient tangle realises P_flat(k)" is Lemma Q verbatim, now via a theorem rather than a conjecture. So the program is a restatement until a structure is found that constrains positions.

### Attack (c): Conjecture P (Lambda(k,n) is a proper coset missing the flat position) is FALSE as stated
**(c1) Arithmetic cannot separate.** Take a single special, n = 1, and J = t^k + eps (t^4-1) t^m.
- J'(-1) = 0 forces eps = (-1)^m for k = -4, and eps = (-1)^{m+1} for k = 4.
- J(e^{i pi/3}) = 1 forces m == 2 mod 3 for k = -4, and m == 0 mod 3 for k = 4. (Computed by hand above; it matches L1 B3(c).)
- The flat positions satisfy both: (k,m,eps) = (-4,-4,+) and (4,0,-). So does the trefoil, (-4,-7,-).
- In general, any congruence on positions that is a consequence of J's arithmetic is satisfied by J = 1, hence by the flat profile. A coset that misses the flat point would have to be a new, purely categorified congruence. S1 and S2 already found such congruences false for general profiles.

**(c2) The B*[U]-extension does not see positions.**
- KWZ's extension obstruction (Thm 4.1) lives inside one component. Its U^2 x idempotent term can be cancelled only by pure-U arrows, and those are excluded globally by the idempotent q-parity fact (2202.01460, p. 12).
- Lemma 5.2 is applied summand by summand. Remark 5.3 shows that extendability is weaker than being s_{2n}, even for a single curve.
- The s_{2n} curves are exactly the special curves that survive (in the HFT analogue, extension alone singles them out), so s_{2n}(inf) should extend on its own.
- Then Astra's block-extension lemma makes A + Q[a,b] extend for EVERY shift. The only constraint left is q-parity within an idempotent, which is a mod-2 condition already visible in J.
- So Lambda(k,n) is everything, and step zero comes out "yes, extends". I did not machine-check this; it is a finite computation over B*[U].

**(c3) Structure (b) is position-blind for the same reason.**
- Watson's inverse system and the Rozansky projector limit are computed by pairing Khr(T) with the arcs a(n) and the triangle maps between them.
- Maps natural in the second argument are block-diagonal on Khr = A + Q[a,b], so their limits split.
- Caveat: naturality of KWZ's gluing isomorphism with respect to cobordism maps is expected, but I did not find it proved in print.

**(c4) Structure (c) is not available as stated.** Extreme Khovanov homology (C6) is a property of diagrams, not of the invariant, except for adequate diagrams. So it cannot by itself constrain positions of components of an invariant.

### Strongest surviving form
Lemma Q is equivalent (now unconditionally, modulo even-length slope-inf rational components) to a bigraded realization problem: which multicurves r1(k) + sum_i s_{2n_i}(inf)[a_i,b_i] arise from tangles with tau(inf) = U?

Any positional obstruction must come from structure that is NOT additive over the direct-sum decomposition of Khr. Examples:
- the relation between Khr(T) and the upstairs Kh(K) (Lipshitz-Sarkar, arXiv:2203.13895);
- the symmetry data of (K,h);
- the global topology of T.

It cannot come from B*[U]-extension, the H-action, or the a(n)-inverse systems. Concrete next test (cheap, Astra): verify by hand or machine that s_2(inf) alone extends over B*[U]. If it does, retire Conjecture P.

---------------------------------------------------------------------------------------------------
## P3. Link/knot boundary

### Attack (a): restatement. CONFIRMED (the program concedes it).
- Conjecture B is equivalent to Lemma Q.
  - Given a non-rational quotient tangle T with J = 1, L = tau(0) is a 2-component link one band from tau(inf) = U, with V(L) = V(O u O). It is not the unlink, because Sigma_2(L) = S^3_0(K) is not S^1 x S^2 for K != U (Gabai, Property R).
  - Conversely, L5 Prop 1 gives the other direction.
- The reflection-double form: <D(T)> = 1 + [3] J J(1/t) is the unlink value iff J is a unit. This is Lemma Q verbatim.
- The categorified Lemma Q via unlink detection is Hedden-Ni (G&T 17 (2013)) plus Batson-Seed (Duke 164 (2015)) plus KWZ gluing. It is a correct observation, not a new tool.

### Attack (b): known
- **"Astra's connectivity lemma"** is the classical V_L(1) = (-2)^{mu(L)-1} (Jones 1985). It is used exactly this way (component count forced by A = 1) in CK06 Prop 2.2, eq. (3).
- **Infinite families of Jones-trivial links:** EKT (Topology 42 (2003)), and Thistlethwaite (JKTR 10 (2001)) for the first examples.
- **Tangle mechanisms that approach V = 1 for KNOTS:** Eliahou-Fromentin, arXiv:1610.05560. A 20-crossing tangle invisible to the bracket pair mod 2 gives knots with V == 1 mod 2^r. This is the published frontier for counterexample design and should be cited and reproduced before any new "nilpotent channel" design is built.
- **The nilpotent element.** x = e1 - delta e1e2 in TL_3 has x^2 = 0 and tr x = 0 (re-derived here). A (3,3)-tangle with <T> = 1 + f x would only give Jones-trivial 3-component links, which EKT already produce for every component count. At A = 1 the bracket of a tangle is +-(-2)^j times its connectivity diagram, so f(+-1) = 0 is forced, and f vanishes at A^4 = 1. That is consistent, not an obstruction.

### Attack (c): false?
Nothing false found. The band-surgery Jones criteria (Kanenobu, Kanenobu-Miyazawa) are vacuous here, because the 2-component unlink passes them. Only non-Jones obstructions screen anything:
- H_1(Sigma_2 L) = Z;
- the linking form;
- d-invariants of 0-surgery;
- |sigma(L)| <= 1 for one coherent band from U.

### Strongest surviving form
A falsification screen with a definite output. For each known Jones-trivial 2-component link, record which of the following first kills band distance one:
1. H_1(Sigma_2) = Z;
2. |sigma| <= 1;
3. d-invariant bounds for 0-surgery.

A survivor of all three would be a serious JC candidate: T(1/n) of modest size, partly beyond the 24-crossing verification. Expected outcome: all are killed at step 1 or 2. No proof leverage.

---------------------------------------------------------------------------------------------------
## P4. Exact counting gadgets / complexity

### Attack (b): known
- The sandwich (JC puts unknot recognition into a counting class) is Welsh 1993 (P^#P), quoted by Hass-Lagarias-Pippenger (J. ACM 46 (1999), Sec. 1).
- C=P membership (GapP, sum of squares) and NP cap coNP (HLP + Lackenby) are routine refinements.
- Prop 2.3(a)-(c) are one-line consequences.

### Attack (c): false claims found
**(c1) "JC is equivalent to a non-existence theorem for knot gadgets" (THEORY-MAP section 4, P4 bridge) is FALSE as an equivalence.**
- What holds is the implication: JC plus NP != coNP rules out hardness reductions to KJT.
- The converse fails. Non-existence of gadgets does not imply JC: a counterexample need not come from any reduction.
- L2 itself wrote only "can be read as"; the THEORY-MAP strengthened it.

**(c2) Prop 2.3(d), "infinitely many counterexamples".** The proof gives infinitely many counterexample DIAGRAMS R(phi). It does not give infinitely many knot TYPES: they could all be one knot, unless recognising a fixed knot type is in NP. The THEORY-MAP wording should say "diagrams".

### Attack (a): S6 is a weak corollary
**(a1) Knots.** Suppose V(D_phi) - 1 = N(phi) g_phi with ord_{t=1} g_phi <= r0. Then V(D_phi) = 1 iff the r0-jet of V(D_phi) at t = 1 vanishes. That jet consists of finite-type invariants of order <= r0, so it is polynomial-time by the Goussarov-Polyak-Viro Gauss-diagram formulas (Topology 39 (2000)), as already used in L2 4.1(i). So the gadget's zero set is in P for EVERY N, not just N = #SAT. Bar-Natan's growth bound is not needed.

**(a2) Links, without assuming polynomial-time jets for links.**
- S6 gives |N| <= p(|phi|).
- Then G(phi) = prod_{j=1}^{p} (j^2 - N(phi)^2) is in GapP (closed under polynomial-length products). It equals (p!)^2 times the indicator [N(phi) = 0].
- So the zero set is in LWPP (Fenner-Fortnow-Kurtz 1994).
- A coNP-hard zero set would therefore put coNP inside LWPP, making NP low for PP. (With polynomial-time jets for 2-component links, which I expect via GPV for string links but have not checked, the zero set is even in P.)
- So fixed-direction or bounded-order gadgets are dead for every N, not only for #SAT. This strictly strengthens S6, and it is also routine.

### Strongest surviving form
An open complexity question independent of JC: is JT_2 (2-component Jones-triviality) coNP-hard, or C=P-complete? No hardness result is in print. Kuperberg (Theory of Computing 11 (2015)) is approximate only.

Any many-one reduction must have ord_{t=1}(V(L_phi) - V(O u O)) unbounded on the NO side. Otherwise the zero set lies in P (knots) or LWPP (links).

For JC, the program yields only conditional statements: a hardness reduction to KJT plus NP != coNP gives infinitely many counterexample diagrams. It cannot prove JC.

---------------------------------------------------------------------------------------------------
## Net effect on the THEORY-MAP (recommended edits)
1. P1: retitle it as a certification engine. Cite CK05/CK06 as the source of the expansion and the Mahler/Lawton layer. Replace Theorem S's BM proof with the Coset Lemma. Keep Conjecture R as the open core.
2. P2: drop "conditional on KWZ Conj 3.6/3.7" and cite arXiv:2202.01460 Thms 1.2, 5.1, 5.4. Retire Conjecture P unless the step-zero computation shows that s_2(inf) does NOT extend alone. State the "non-additive structure" requirement.
3. P3: credit Jones 1985 / CK06 for the connectivity lemma. Add Eliahou-Fromentin arXiv:1610.05560 to the counterexample-design toolkit.
4. P4: change "equivalent" to "implies (under NP != coNP)" and "counterexamples" to "counterexample diagrams". Replace S6 by the bounded-jet (P) and LWPP statements. Credit Welsh 1993.

## Final checks (end of session)
- Numerically re-verified P2 (c1): single special, k = -4 passes J(-1)=1, J'(-1)=0, J(i)=1, J(e^{i pi/3})=1 exactly at m == 2 mod 3 with eps = (-1)^m (includes flat m = -4 and trefoil m = -7); k = 4 exactly at m == 0 mod 3 with eps = (-1)^{m+1} (includes flat m = 0).
- Files: this note; scratchpad (session-local, copy out if needed): /private/tmp/claude-501/-Users-calebbarnett/7610ac96-4d03-4d32-b526-8a5647837809/scratchpad/stress/{code/coincidence.py, ck06/ck06.txt, kwz22/kwz22.txt, hlp/hlp.txt}.
- coincidence.py copied to bridge/STRESS_code/ (durable).
