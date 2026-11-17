> PRECEDENCE NOTE (integrator, 13:20): STRESS.md and Codex's corrections (msgs 124730, 131440) take precedence over this map. Known errors here: (i) the Brownawell-Masser promotion of Theorem S (its affine-fibre part is the project's D-MULTITWIST and Champanerkar-Kofman 2006; only FIXED-TWIST-P is new); (ii) the gauge-lens barrier statements (the quoted chi(I^natural) formula is false; barrier withdrawn); (iii) any phrasing that JC is EQUIVALENT to the non-existence of gadgets (it is an implication under NP != coNP only); (iv) the P2 positional conjecture (refuted by STRESS).

# THEORY-MAP: bridges into the Jones unknot problem

17 November 2026. Synthesis of the seven lens reports (bridge/L1 to L7) and of Astra's cross-field map (bridge/astra/). Synthesizer: Claude.
Status: internal working document. Nothing here has outside review. Results marked PROVED were checked by the lens that produced them and re-read here; results marked CHECKED are machine checks run today.
Notation as in CONTEXT.md: (K,h) is a strongly invertible knot, T its quotient tangle, J = J(K,h) the preferred-normalised invariant (J = 1 mod (t+1)^2). LEMMA Q: J a unit implies K = U.

---

## 0. The map in one page

**Where detection lives.** Every detection theorem near this problem is of one of two kinds.
- Categorified: Kronheimer-Mrowka; KWZ detection of rational tangles; Watson's kappa(K,h), which vanishes iff K = U.
- Positive counts: traceless SL(2,C) characters of the branch knots T(1/n) grow linearly for nontrivial hyperbolic K (L5 Prop 4); BHMV curve operators on doubles (L3 Theorem E).

J is a signed Euler characteristic at one fixed colour, not the order of a module (for an order, "unit" would mean "module vanishes"; see C4 for why no small module can have J or V as its order). So the problem is a cancellation problem. A homology theory that detects and has Euler characteristic built from J already exists: J = t^k + (t^4-1) P, where P is the Euler characteristic of kappa written in blocks (L1). **What is missing is not a new homology theory. It is a structure that forbids one specific cancellation.**

**What the lenses established about that cancellation.**
- **Categorification (L1).** J = 1 iff P = P_flat(k) := (1 - t^k)/(t^4 - 1). For k != 0, a flat profile needs no cancellation among the specials: one special at the right bigrading is enough. Any proof therefore needs positional (bigraded) realization input.
- **Gauge theory, physics, arithmetic (L5, L7, L4).** Every shadow that depends on K alone is used up:
  - SU(2) and instanton Euler characteristics are classical (sigma, det, n a_2).
  - The root-of-unity congruences of J are exactly the genon levels k in {0, 2, 4, 8} (L7).
  - With the certified pair of inversions of the figure-eight, J mod Phi_n depends only on K for finitely many n.
  - What remains of Lemma Q depends on h.
- **Quantum representations (L3).** Lemma Q is unlink detection among doubles. Positivity proves detection only in doubled (diagonal) geometry, and the Jones conjecture is an off-diagonal statement.
- **Complexity (L2).**
  - In any fixed body, the twist parameters with unit J form an S-unit equation over the function field C(A). It has effective structure: a finite set plus finitely many lattice cosets (Theorem S).
  - Knot Jones-triviality is in C=P. The Jones conjecture would place it in NP intersect coNP.
- **Combinatorics (L6).** On signed chord diagrams the virtual obstruction to detection is parity (odd chords), not genus (the Even Jones Conjecture).
- **Astra.**
  - Block-extension lemma: deformation-extension existence cannot see direct sums.
  - Connectivity lemma.
  - Growth obstruction to counting gadgets.
  - JC as the existence of a finite-field zero.
  - A formal model blocking colour propagation.

**The four programs (Section 4), in order:**
1. **Two-place Diophantine geometry of twist families.** S-units, tropical end invariants and Mahler measure as three resolutions of one object. Owner: both, Claude leading.
2. **Realization constraints for the strong-inversion multicurve.** The categorified route with the highest ceiling. Owner: Astra.
3. **The link/knot boundary.** Band distance one, doubles and EKT. A cheap falsification test plus the mechanism of nilpotent units. Owner: Claude.
4. **Exact counting gadgets.** The complexity bridge, corrected by a growth obstruction found today. Owner: both.

**Answers to the two examples in the directive.**
- *"Build a new homology theory."* Detection at the categorified level is already available (kappa, KWZ, KM). A new theory is worth building only if it carries a structure that pins down where the specials sit; Program 2 names candidates.
- *"Adjacent or equivalent to complexity theory."* JC is not equivalent to a complexity statement. There is a precise conditional link (the sandwich, Program 4), and a clean independent question: is Jones-triviality of 2-component links coNP-hard? Today's growth obstruction shows what any reduction must look like.

---

## 1. Lens verdicts

| Lens | Best bridge | Proved or checked | Kind | Leverage on Lemma Q |
|---|---|---|---|---|
| L1 categorification | J = t^k + (t^4-1)P, P = chi(kappa) in [n]-blocks; reverse laws for kappa | Prop A1 (J is the Jones-Wenzl channel); Theorem B3 (a)-(d) conditional on KWZ geography; obstructions O1-O3 | new dictionary plus new laws for kappa | Locates the gap exactly (positions of specials); no direct leverage |
| L2 complexity | Theorem S: twist families as S-unit equations over C(A) | Theorem S (modulo Brownawell-Masser); C=P sandwich; Prop 4.2 (corrected below) | genuine import (function-field abc) | Upgrades searches to infinite-family theorems body by body |
| L3 quantum reps | JC = conservativity; doubles; Theorem E | Units of TL_2 are braids; doubling identity; Theorem E; exotic nilpotent units in TL_3 | reformulation plus an off-path theorem | Explains why TQFT positivity stops at the diagonal |
| L4 arithmetic | Lehmer gap for J (Conjecture LJ) | Prop A (mirror); Prop B (Smyth bound for non-reciprocal J); Prop C; Prop D (Lawton descent) | quantitative strengthening | Chiral half is trivial qualitatively; amphichiral half is a reciprocal Lehmer problem |
| L5 gauge/geometry | Band criterion; SL(2,C) positivity | Prop 1 (band), Prop 2 (classical vacuity), Prop 3 (equivariant KM), Prop 4 (SL(2,C) count) | restatement plus negative results plus a true counting analogue | Says the missing ingredient is q-graded positivity |
| L6 combinatorics | Even Jones Conjecture on signed chord diagrams | Parity lemma; Z-faithfulness at the unknot; EJC holds up to 6 chords | new conjecture in a wider setting | Indirect: EJC implies JC |
| L7 physics | Genon identity: Jones at e^{i pi/5} is the Fibonacci TQFT of the double branched cover | Exact numerics (2-bridge, 336 pretzels, 173 links); classification k in {0,2,4,8}; finiteness | strong explanatory import | Explains all arithmetic of J; proves no further K-only congruences exist |
| Astra | Exact gadget theory; derived realization; arithmetic zeros | Block-extension lemma; connectivity lemma; bounded-jet and width obstructions; finite-field-zero form; H_0 = H_r = 1 model | precise filters | Filters that kill weak proposals |

---

## 2. Checks run by the synthesizer (17 Nov; under 10 minutes of CPU in total)

Scripts are in bridge/SYNTH_code/.

**S1. Residue-mod-4 law: DEAD.**
- *Observation.* In the five normalised J's quoted in the notes (trefoil, 4_1, l_bXXYa, T(4,5), the L4 minimiser), the exponents divisible by 4 carry exactly one monomial, t^k.
- *Why it would have mattered.* If specials always avoided the residue class 0 mod 4, then P_flat(k), which lives entirely in that class, could never be matched for k != 0. Lemma Q would reduce to the case k = 0.
- *Test.* Random strongly invertible words, run through tools/flat_search.py (bracket_vector) and normalised; 473 nontrivial samples (seeds 1, 2, 3).
- *Result.* 160 violations. Example: s.r1.x0.y2.y2.x0.x2.y1.x2.y0.y0.u1 has residue-0 part -t^-4 + 2.
- Script: residue_test.py.

**S2. delta-window law: DEAD.**
- *Claim tested.* Every special sits at delta_r +- 1/2, where delta_r is the delta-grading of the rational component.
- *Data.* 171 kht++ records with one rational component.
- *Result.* The offsets of specials range over +-1/2, ..., +-5.5. 101 records have a special beyond +-1/2.
- Script: geography_checks.py.

**S3. Inequality |k| <= dim_F2 kappa (new here; novelty checked only against L1's reading of KWZ arXiv:2104.13592).** Conditional on KWZ Conjectures 3.6/3.7 and on L1 Cor B2.
- *Statement.* |k| <= 4 sum_s n_s = dim kappa, with equality iff every special has the same sign (-1)^{h_s + m_s}.
- *Proof.* L1's law (b) gives P(-1) = -k/4, and [n]_{t^2} evaluated at t = -1 equals n.
- *Data.* 0 violations in 171 records; equality in 41 records with specials (for example every T(2,2m+1)).
- *What it gives.* Nothing for Lemma Q, since J = 1 satisfies it. It is a clean reverse-bridge inequality: the arithmetic of J bounds the slope of the rational component by the size of Watson's invariant.

**S4. Slope versus signature: NO.**
- *Hope.* k = -2 sigma would turn P(-1) = -k/4 into a Khovanov shadow of Lin's count sigma/2 (L5).
- *Result.* False. T(3,4) has |k| = 8 with sigma = -6; T(3,5) has |k| = 12 with sigma = -8. (Records in mech2/dictionary, knots identified by their Alexander polynomials.)

**S5. Kanenobu caveat for Theorem S.**
- *Fact.* Kanenobu's knots K(p,q) have HOMFLY (hence Jones) polynomial depending only on p + q. For even p, q they are pairwise distinct (Kanenobu, Proc. AMS 97 (1986); Lobb, arXiv:1105.3985).
- *Consequence.* Twist directions invisible to the bracket, along which the knot type changes, do exist. L2's TWIST-INVISIBILITY in the form "invisible directions are topologically trivial" is false.
- *What survives.* Only the version restricted to unit cosets survives, and that version is exactly JC on the family.

**S6. Growth obstruction against L2 Prop 4.2.** The fixed-direction "affine counting tangle" cannot exist with N = #SAT. The proof is in Program 4. It extends Astra's knot-level obstruction to links.

**S7. Astra's connectivity lemma.** The proof was re-read and is correct.
- At A = 1 the normalised bracket of any c-component diagram equals +-(-2)^{c-1}.
- Closing T and S by tangles realizing their matchings pi and sigma gives r_T + n = r_S + l and r_T + l = r_S + n.
- Hence l = n, so pi = sigma and r_T = r_S.

---

## 3. Cross-connections between lenses

**C1. One object at three resolutions.** Along twist parameters, J is an exponential polynomial
J(C(n)) = sum_eps c_eps (-1)^<eps,n> A^<l_eps,n>.
- The project's end invariants analyse it to first order at the two places infinity and 0 of C(A). This is the tropical layer, and L2's Bruhat-Tits pointer is its matrix form.
- Theorem S (Brownawell-Masser, L2) analyses it exactly.
- Lawton and Boyd-Smyth (L4 Prop D) analyse it in measure.

In all three, "resonance" means a vanishing subsum. So the resonance budget, the resonant mirror-type products and Lawton's bad sublattices should be one object.

**C2. Detection is positive; J is signed.**
- SU(2) counts are classical (sigma/2) and do not detect (L5).
- Traceless SL(2,C) counts are positive and detect (L5 Prop 4).
- Kh and kappa detect (L1). BHMV on doubles detects (L3 Theorem E).
- The doubling identity <D(T)> = 1 + [3] J J(1/t), together with Kh(D(T)) = H(End Kh(T)) and unlink detection (Hedden-Ni; Batson-Seed), gives a categorified Lemma Q for free.

L1's O1-O3 and today's S1-S2 show that the missing positivity must be positional (bigraded) and global, not a local congruence.

**C3. The arithmetic is exactly the genon levels.**
- L7's levels k in {0,2,4,8} produce exactly the board's congruences: Phi_1, Phi_2^2, Phi_4, Phi_6 and Phi_10.
- L4's independent probe found no other exact relation up to n = 48.
- L1's new mod-3 and Phi_10 laws for kappa are the categorified images of the levels k = 4 and k = 8.

What remains is dependent on h: L4's reciprocal Lehmer problem, and L7's reading of J as an h-twisted SO(3) Wilson loop. **Stop hunting congruences.**

**C4. Complexity meets finite type.** Astra's growth bound for knots, L2's jet filters (4.1(i)) and the project's FT-DEEP all say the same thing: hardness and cancellation must live in Taylor coefficients of unbounded order at t = 1. Applying Bar-Natan's polynomial growth to L2's link gadget kills the fixed-direction version (S6). A further consequence: no polynomial-size determinantal formula (module order computable from a diagram) can present V, unless FP = #P. Such a presentation would make V, which is #P-hard to evaluate at generic t (Jaeger-Vertigan-Welsh), computable in polynomial time. The same is expected for J. So any "J as an order" bridge, where a unit would force a module to vanish, must be exponential, the size of Khovanov theory.

**C5. Lemma Q is EKT on the reflection diagonal.**
- EKT's Jones-trivial links come from the indefinite pairing <H(T,U)> = br(T)^T H br(U) of two different tangles.
- L3's double D(T) pairs T with its own mirror: <D(T)> = 1 + [3] J J(1/t), which equals the unlink's value iff J J(1/t) = 1, iff J is a unit.
- L5's band criterion is the same statement at band distance one from the unknot.

So the EKT cancellation is available only off the diagonal. There are two known ways link mechanisms escape: an indefinite pairing (EKT), and nilpotent units in TL_3 (L3). Astra's connectivity lemma blocks fusing either into a knot by substituting a full skein signature.

**C6. End laws as extreme Khovanov homology of circle graphs.**
- The extreme coefficient of a diagram's bracket is the reduced Euler characteristic of the independence complex of its Lando graph, which is a circle graph (Gonzalez-Meneses, Manchon, Silvero, arXiv:1511.05845).
- These complexes are wedges of spheres in known cases: bipartite circle graphs (arXiv:2302.02527); 4-braids (Przytycki-Silvero, arXiv:2305.18648, conjecture in arXiv:1608.03002).
- L6's interlace graphs, and its split decomposition (canonical Conway circles), supply the same combinatorics.
- The project's "one end easy, both ends blocked" becomes a statement about simultaneous non-contractibility of the extreme complexes at the all-A and all-B ends. This is a possible homotopy-theoretic reason for end non-cancellation that does not depend on the arborescent tree.

---

## 4. Top programs

### Program 1. Two-place Diophantine geometry of twist families
**Owner:** both. Claude leads (computation, Diophantine literature); Astra identifies cosets with skein moves.

**Bridge.**
- *Set-up.* Fix a body C: a quotient-tangle diagram with k twist slots holding n_i half twists. In TL_2 a horizontal box is [n] = A^n (1-p) + (-A^{-3})^n p, with p = e/delta; vertical boxes have eigenvalues A^{-1} and -A^{3}.
- *Expansion.* Multilinearity gives y(n) = sum over eps in {0,1}^k of c_eps (-1)^<eps,n> A^<l_eps,n>. Here c_eps is the body evaluated with an idempotent in each slot, and l_eps is in {1,-3}^k.
- *The equation.* J(C(n)) is a unit iff y(n) = +-A^m, which is an S-unit equation in C(A).
- *Three resolutions.* (R1) Tropical: first order at the places infinity and 0, i.e. the project's end invariants. (R2) Exact: Theorem S, a finite set plus lattice cosets inside resonance subspaces W_P where block sums of the c_eps vanish identically. (R3) Measure: Lawton plus Boyd-Smyth give M(J(C(n))) -> M(P_C) off finitely many resonant sublattices.

**Why it could work.**
- It turns the finite certified searches (about 500k configurations with J = 1, all unknots) into statements about all twist parameters of a body at once. The existing finite-window theorem and the "two candidate twist values" theorem handle one slot.
- It gives resonance an exact meaning.
- The tools are effective and are not available inside quantum topology: Mason-Stothers, Brownawell-Masser, Zannier, Lawton, Boyd-Smyth. No previous use for knot polynomials was found by search.
- It locates exactly where any infinite family of counterexamples must live: on a unit coset of positive rank.
- It fits the project's machinery: transfer matrices (mont/jtools.py), end invariants, resonance budget.

**First theorem (write and machine-check now). Theorem S_J for the E6/V3 two-node bodies, k = 2..4.**
- The J-unit locus equals F u (b_1 + L_1) u ... u (b_r + L_r), listed explicitly, each coset with its resonance partition.
- F lies in the box cut out by the tropical layer (R1).
- For k <= 2, give a sharp version from Mason-Stothers. It should recover the one-slot finite-window theorem as the three-term case.

**Conjecture to attack next (Conjecture R).** For every body C in the E6/V3 class and every positive-rank J-unit coset b + L, every tangle C(b + w) with w in L is rational. Equivalently, the coset directions are generated by Reidemeister I, nugatory and flype directions. Conjecture R plus Theorem S_J gives Lemma Q for all twist parameters of these bodies.

**Obstructions to check first.**
- *Kanenobu-type invisible directions (S5).* A constant bracket along a direction with changing knot type does occur. So no coset can be certified by algebra alone, and each positive-rank unit coset needs a topological argument. The needed input is twist-family rigidity: infinitely many unknots in a twist family force the twist to be trivial. Results of Kouno-Motegi-Shibuya type exist, but the exact statement for lifted crossing circles must be located. *Check first:* do the E6/V3 bodies have any positive-rank J-unit coset that is not an evident move? This is finite linear algebra on the c_eps.
- *Not uniform across bodies.* The Brownawell-Masser windows grow with |S|, so this is a theorem per body, not a global proof. Use the cheap tropical layer to prune before applying BM: L2 found the BM window to be about 100 against 12 observed.

**First-week tasks.**
1. Compute the c_eps for the k = 2..4 bodies from the existing transfer matrices.
2. Enumerate the partitions P with W_P != 0 and test for identical vanishing.
3. Compute the tropical box for F and compare it with the resonance budget.
4. Compute M(P_C) (L4) for the same bodies and list Lawton's resonant sublattices.
5. Compare the three lists. If they coincide, that is C1 made concrete.

### Program 2. Realization constraints for the strong-inversion multicurve
**Owner:** Astra. Claude supplies data dumps and literature.

**Bridge.**
- Work over F_2 under KWZ geography: Khr(T) = r1(k) u specials s_{2n}(inf), as in KWZ Conjectures 3.6/3.7; this holds in every project run.
- L1 Cor B2 gives J = t^k + (t^4 - 1) P, with P = sum_s (-1)^{h_s} t^{m_s} [n_s]_{t^2}, which is chi(kappa(K,h))/chi(V_kappa).
- Since kappa = 0 iff K = U, Lemma Q says: no nontrivial quotient tangle realises P = P_flat(k).
- Formal multicurves realising P_flat(k) exist for every k. For k = -4n, a single special s_{2n}(inf) with h even at m = -2n-2 does it. For k = 4n, take h odd and m = 2n-2.
- So Lemma Q is precisely a statement about which bigraded positions of specials, relative to r1(k), actual quotient tangles can realise. Example: the trefoil has k = -4 and P = -t^-7; its special sits at m = -7 with h odd, while the flat position is m = -4 with h even.

**Why it could work.**
- Detection is already proved at this level, and L1's O1-O3 isolate the one missing datum (position).
- Actual tangles carry three structures that formal direct sums need not have, and each can tie the position of a special to that of r1(k):
  - (a) KWZ's B*[U] deformation: actual type D structures extend ("Khovanov multicurves are linear", arXiv:2202.01460, Thm 4.4), and uncancellable higher products already exclude some curves there.
  - (b) Watson's inverse system Kh(tau(n+1)) -> Kh(tau(n)) and Rozansky's projector limit, with Hogancamp's polynomial action. This should make the coloured-unknot part free and kappa torsion (L1 bridge A).
  - (c) Extreme Khovanov homology (C6), which governs the extreme special levels.

**First conjecture (precise). Conjecture P (positional rigidity).**
- Let A = r1(k) and Q = s_{2n}(inf), with trivial local system.
- Let Lambda(k,n) be the set of relative bigrading shifts (a,b) for which A + Q[a,b] extends over B*[U] compatibly with rank-one pairing against a(inf).
- Claim: Lambda(k,n) is a proper lattice coset that misses the flat position.

The case n = 1, k = +-4 is the single-special flat model, the first case Lemma Q must exclude.

**Step zero (decisive and cheap; Astra's test).** Decide whether the compact ladder block Q of TH-LADDER extends over B*[U] on its own.
- If it does, the block-extension lemma shows that mere extension cannot see positions. Conjecture P is then false as stated, and the program moves to structure (b), with maps between different closures.
- If it does not, compute the obstruction class for A + Q[a,b] as a function of (a,b). This is the first place a positional constraint could appear.

**Obstructions to check first.**
- Astra's block-extension lemma: direct sums and shifts of extendable objects extend.
- Today's S1 and S2: no local congruence (residue mod 4, or a delta window) protects the flat positions. Any positional law must be global.
- L1's O2: specials of opposite h-parity occur in actual tangles, as in l_bXXYa.

**Free consistency laws for every kht++ record.**
- L1 Theorem B3 (c), the mod-3 law.
- L1 Theorem B3 (d), the Phi_10 law, after fixing the mirror convention between the board and KWZ.
- S3, the inequality |k| <= dim kappa.

**Claude's first task.** Dump the full bigraded special lists (h_s, q_s, delta_s, n_s) from every kht++ run, and tabulate how far each record's P is from P_flat(k).

### Program 3. The link/knot boundary: band distance one, doubles, and EKT
**Owner:** Claude.

**Bridge.** Three equivalent forms of Lemma Q as statements about links.
- **(B) Band form (L5 Prop 1).** Let L be a 2-component link one coherent band away from the unknot. Then V(L) = V(O u O) iff J(T) = 1. By the Montesinos trick, Sigma_2(L) = S^3_0(K) with K strongly invertible. If such an L is not the unlink, every T(1/n) is a nontrivial knot with V = 1.
- **(D) Doubles (L3).** <D(T)> = 1 + [3] J J(1/t), and T is rational iff D(T) is the unlink.
- **(E) EKT.** Known Jones-trivial links come from indefinite pairings of two different tangles. Lemma Q says the cancellation fails on the reflection diagonal (C5).

**Why it could work.**
- Prop 1 turns the known Jones-trivial 2-component links (Thistlethwaite, JKTR 10 (2001); Eliahou-Kauffman-Thistlethwaite, Topology 42 (2003)) into concrete test objects. Any one of them at band distance one from the unknot gives explicit JC counterexamples T(1/n).
- It imports band-surgery theory and Heegaard Floer obstructions to being a 0-surgery.
- L3's exotic units supply a second, nilpotent mechanism for Jones-trivial links. In TL_3 the element x = e1 - delta e1 e2 satisfies x^2 = 0 and tr x = 0, so 1 + f x is a unit outside the braid image. This mechanism is the natural model for a "J = 1 without rationality" defect in the width-two channels End(V1 x V2 x V2) = Mat2 + Mat2 + K.

**First conjecture (precise). Conjecture B.** No nontrivial 2-component link L with V(L) = V(O u O) has a coherent band to the unknot. Equivalently, no such L has a band presentation with Sigma_2(L) = S^3_0(K).

Test on the explicit list of known examples, in order (lk = 0 and det = 0 are automatic from V):
1. H_1(Sigma_2(L)) = Z exactly. This is a Goeritz computation; any torsion kills the candidate.
2. The d-invariant inequalities satisfied by every 0-surgery on a knot (Ozsvath-Szabo, Adv. Math. 173 (2003)).
3. If a candidate survives, recognise the manifold with SnapPy and search for the band.

**Second, independent question.** Is there a non-braid (3,3)-tangle T with <T> = 1 + f x? Run a bounded search over cap_i beta cup_j with beta in B_5 of length <= 8 (L3 section 8). A hit gives a new family of Jones-trivial 3-component links and a design for width-two nilpotent defects.

**Obstructions to check first.**
- (B) and (D) are restatements, so this program can falsify but cannot prove.
- Any EKT tangle with [T] proportional to [0], b-connectivity and D(T) = unknot would already disprove JC. So expect the band test to fail, and record which obstruction blocks it, since that is information.
- Astra's connectivity lemma forbids turning a link mechanism into a knot by substituting a full skein signature; a fusion must cut inside the gadget.

### Program 4. Exact counting gadgets and the complexity of Jones-triviality
**Owner:** both. Astra: classification of TL tensor signatures. Claude: complexity literature and obstructions.

**Bridge.**
- Knot Jones-triviality (KJT) is in C=P unconditionally (L2 Prop 2.1; Astra).
- JC implies KJT = UNKNOT, which lies in NP intersect coNP (Hass-Lagarias-Pippenger; Lackenby).
- A coNP- or NP-hardness many-one reduction to KJT would give: JC implies NP = coNP. Assuming NP != coNP, such a reduction would yield infinitely many counterexamples (L2 Prop 2.3).
- So JC is equivalent to a non-existence theorem for knot gadgets with the following necessary features:
  - (i) unbounded Taylor depth at t = 1 (L2 4.1; Astra; extended to links below);
  - (ii) unbounded width (Makowsky; Astra's sweep lemma);
  - (iii) not parametric in a fixed body (Theorem S);
  - (iv) compatible with Astra's connectivity lemma.

**New today (S6): the growth obstruction for links.**
- *Set-up.* Suppose phi -> T_phi is computable in polynomial time with br(T_phi) = mu_phi ((0,1) + N(phi) v), where v is fixed. This is L2's affine counting tangle. Let w = v_1 delta + v_2, and let r be its vanishing order at t = 1.
- *Key identity.* The coefficient of h^r in V(H(T_phi, inf))(e^h) equals +-2 w_r N(phi) + poly(|phi|).
- *Contradiction.* That coefficient is a Vassiliev invariant of order r, so it is polynomially bounded in crossing number (Bar-Natan, Math. Res. Lett. 2 (1995); his crossing-change argument works for links). Hence |N(phi)| <= poly(|phi|), which is impossible for N = #SAT on tautologies.
- *General version.* Any construction with V(D_phi) - V(U_c) = N(phi) g_phi, where g_phi is integral with bounded vanishing order at t = 1, forces N to be polynomially bounded.
- *Conclusion.* Exact gadgets, for knots or for links, need instance-dependent directions whose order of vanishing at t = 1 grows with the instance.

**First open question (precise).** Is JT_2 = {2-component link diagrams L : V(L) = V(O u O)} coNP-hard under polynomial-time many-one reductions?
- A yes would be a new complexity theorem: Jones-triviality is hard for links, while JC predicts it is easy for knots.
- A structural no, meaning a classification showing that planar TL tensor networks at generic A cannot realise exact zero tests under (i)-(iv), would be a first explanation of why evaluation hardness misses the trivial fibre.

**Obstructions to check first.**
- The growth obstruction above.
- No exact universality is known for TL at generic A. Kuperberg's #P-hardness is approximate (Solovay-Kitaev). Kuperberg-Samperton's exact encodings are for finite-group colourings, which act by permutations.

**Honest leverage.** This program cannot prove JC. It gives an independent meaning to JC and a disproof strategy that is conditional on NP != coNP. It is ranked fourth for that reason, and kept because it is the cleanest complexity-theoretic question in the area.

---

## 5. Results worth writing up now (not programs)

- **W1. Genon identity (L7).** |V_L(e^{i pi/5})| = |Z_Fib(Sigma_2 L)| / |Z_Fib(S^3)|. Also the tangle form [T](zeta_10) = Z_Fib(E(K)), the classification of levels k in {0,2,4,8}, and finiteness of the root-of-unity congruences that depend on K only. Exact on the 2-bridge family, 336 pretzels and 173 links. *Before claiming novelty,* check Y. Rong, "The Kauffman polynomial and the two-fold cover of a link" (Indiana Univ. Math. J. 40 (1991)), which relates special values of the Kauffman polynomial to the double branched cover, plus the Kirby-Melvin evaluations and the literature on permutation orbifolds and HQFTs.
- **W2. Theorem S (L2),** with the Kanenobu caveat (S5) and the 2-bridge and pretzel sanity checks.
- **W3. Theorem E and Corollary E1 (L3).** BHMV invariants detect the unknot among curves on the standard Heegaard surface of #^g(S^1xS^2), and the equality case of Garoufalidis' bound characterises #^g(S^1xS^2). Clean and off the main path.
- **W4. Parity lemma, Z-faithfulness at the unknot, and the Even Jones Conjecture (L6),** with the exhaustive check up to 6 chords. Next cheap step: n = 7, 8 for even words only.
- **W5. Reverse laws for Watson's kappa (L1 Theorem B3 (c),(d)) and S3 (|k| <= dim kappa).** Conditional on KWZ geography; the mirror convention must be fixed first.
- **W6. Equivariant Kronheimer-Mrowka (L5 Prop 3) and the linear SL(2,C) traceless count for branch knots (L5 Prop 4).** A version of Lemma Q that counts and is true.

---

## 6. Discarded or parked, with reasons

1. **Residue-mod-4 geography law.** Dead: 160 violations in 473 samples (S1).
2. **delta-window law** (specials only at delta_r +- 1/2). Dead: 101 of 171 records violate it (S2).
3. **k = -2 sigma** (P(-1) as a Khovanov shadow of Lin's count). Dead: T(3,4) and T(3,5) contradict it (S4).
4. **TWIST-INVISIBILITY as "invisible directions are trivial".** False by Kanenobu's knots (S5). Only the unit-coset version survives, and it is JC on the family.
5. **L2 Prop 4.2 with a fixed direction and N = #SAT.** Impossible by Bar-Natan's growth bound (S6). Replaced by the requirement of unbounded vanishing order.
6. **Euler-characteristic routes that are blind by construction:**
   - J as the Lefschetz trace of h on Kh(K) (refuted on the trefoil by L1 and L7);
   - Heegaard Floer and immersed-curve Euler characteristics (Alexander-type; their version of Lemma Q is false);
   - SU(2) and instanton Euler characteristics (classical).
7. **Further cyclotomic congruences for J.** Exhausted: genon classification plus the figure-eight pair, and the probe up to n = 48. Cube-root detection fails (T(4,5) has J(omega) = 1). Mahler measure of V fails (4_1).
8. **Faithfulness routes:**
   - faithfulness and asymptotic faithfulness at fixed colour (downstream of JC; Faith_1 is vacuous);
   - the positive-definite function on Thompson's group F (the unknot is interior);
   - colour propagation through Habiro integrality (Astra's H_0 = H_r = 1 model);
   - positivity from stability conditions (central charges kill Q + Q[1]).
9. **"Build a homology theory that detects."** Already exists (kappa, KWZ, KM). Worth doing only together with a structure that forbids positional cancellation (Program 2).
10. **Parked, not refuted:**
    - Whang descent with Bonahon-Wong shadows;
    - Fibonacci and Tutte golden identity;
    - Z-hat at a single root;
    - Potts and SPQR (a restatement);
    - finite-field zeros without a geometric source;
    - quantitative JC via jets of order log c(K) (untested);
    - Lehmer gap LJ in full (its amphichiral half is a reciprocal Lehmer problem; its family version lives inside Program 1).

---

## 7. Comparison with Astra's map, and answers to her asks

**Agreement.**
- Her second choice, derived realization, is Program 2 here.
- Her block-extension lemma is the first obstruction there.
- Her one-block test is step zero there.

**Divergence.** She ranks exact-gadget theory first; here it is fourth, for two reasons:
- It can only yield conditional or strategic statements about JC.
- Today's growth obstruction (S6) removes the most natural gadget shape.

Her proofs of the bounded-jet and width restrictions and of the connectivity lemma are correct (S7). The growth bound extends from her fixed-prefactor knot gadgets to L2's link gadgets.

**Ask: "name the exact extra structure beyond the block-extension no-go."** The structure must make an obstruction depend on the relative bigrading shift (a,b) between the rational arc A and a compact block Q, because positions are the only datum a flat formal profile needs (L1 O3; S1-S2). Concretely, either of the following would do:
- a nonzero obstruction class for A + Q[a,b] over B*[U] that varies with (a,b) (this needs Q not to extend on its own);
- maps between different closures that actual tangles carry and direct sums need not respect: Watson's inverse system tau(n+1) -> tau(n), or the Rozansky-Hogancamp projector limit (Program 2, structures (a) and (b)).

**Arithmetic.** Her finite-field-zero form of JC is correct and remains a restatement until a geometric source of the zero is found. L4 notes that classical zeros of V sit at primes dividing det, which come from dihedral representations, so for det-1 knots any zero must come from non-dihedral data. L5's traceless representations, reduced to finite fields, are the natural candidate (parked).

---

## 8. Key sources

**Function-field arithmetic and Mahler measure.**
- Brownawell-Masser, Math. Proc. Camb. Phil. Soc. 100 (1986) 427-434.
- Mason, LMS Lecture Notes 96 (1984).
- Zannier, Acta Arith. 64 (1993).
- Lawton, J. Number Theory 16 (1983).
- Boyd, J. Number Theory 13 (1981).
- Smyth, Bull. LMS 3 (1971).

**Twist families and links with trivial Jones polynomial.**
- Kanenobu, Proc. AMS 97 (1986).
- Lobb, arXiv:1105.3985.
- Thistlethwaite, JKTR 10 (2001).
- Eliahou-Kauffman-Thistlethwaite, Topology 42 (2003).

**Khovanov multicurves, strong inversions and projectors.**
- Kotelskiy-Watson-Zibrowius: arXiv:1910.14584, arXiv:2104.13592, arXiv:2202.01460, arXiv:2105.06308, arXiv:2602.23442.
- Watson, Adv. Math. 313 (2017).
- Rozansky, arXiv:1005.3266.
- Cooper-Krushkal, arXiv:1005.5117.
- Hogancamp, arXiv:1405.2574.
- Hedden-Ni, G&T 17 (2013).
- Batson-Seed, Duke 164 (2015).
- Kronheimer-Mrowka, Publ. IHES 113 (2011).

**Extreme Khovanov homology and circle graphs.**
- Gonzalez-Meneses, Manchon, Silvero, arXiv:1511.05845.
- Przytycki-Silvero, arXiv:1608.03002 and arXiv:2305.18648.
- Bipartite circle graphs, arXiv:2302.02527.

**Complexity.**
- Bar-Natan, Math. Res. Lett. 2 (1995).
- Hass-Lagarias-Pippenger, J. ACM 46 (1999).
- Lackenby, Adv. Math. 387 (2021).
- Kuperberg, Theory of Computing 11 (2015).
- Kuperberg-Samperton, AGT 21 (2021).
- Jaeger-Vertigan-Welsh (1990).

**Gauge theory and TQFT.**
- Ozsvath-Szabo, Adv. Math. 173 (2003).
- Cui-Galindo-Plavnik-Wang, CMP 348 (2016).
- Rong, Indiana Univ. Math. J. 40 (1991) (prior-art check for W1).

**Equivalence of JC with rational-tangle detection.**
- Sikora, Canad. J. Math. 76 (2024).

The full citation lists are in L1-L7 and astra/*.md.
