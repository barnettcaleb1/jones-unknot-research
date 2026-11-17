# Genus-two lane: referee verdicts on the Heegaard and kernel builds

- Workflow: wf_d0b0a3e6-177 (jones-g2-proof-lane-wf_d0b0a3e6-177.js)
- Session: structure chat (genus-two lane, ~/jones-lanes/g2-proof)
- Launched (script written): 2026-11-03 12:55 local; journal last written: 2026-11-03 15:00 local
- Agents started: read:bbb, read:status, read:model, build:heegaard, build:transfer, ref:transfer, build:kernel, ref:heegaard, ref:kernel, synthesis
- Results extracted here: ref:heegaard, ref:kernel
- Context: Launched 3 Nov 12:55 in the structure chat. All other agents of this workflow wrote report files in ~/jones-lanes/g2-proof (read-*, build-*, ref-transfer, REPORT.md). These two referees left only check scripts (ref-heegaard/ref_check.py, ref-kernel/ref_check*.py and scratch_notes.txt); their verdicts are summarized in g2-proof/REPORT.md items 9-11 and exist in full only in the journal.
- Provenance: contemporaneous agent outputs recorded in the workflow journal (runtime state, not copied). Text below is verbatim except formatting (JSON fields rendered as markdown), em dashes replaced by ' - ', email addresses redacted, and home-directory paths shortened to ~ (session scratchpad roots to <scratch>). These are internal AI agent outputs, not external review; statuses are as the agent stated them at the time and may be superseded by later board entries.


## Agent: ref:heegaard


### verdict

survives

### strongest_objection

No fatal error found. Unitarity and positivity check out. At |A| = 1 the bilinear diagram form B is not invariant; the sesquilinear H(x,y) = B(x̄,y) is. Theorem A only pairs against the cup vector c, which is bar-invariant, so <plat β> = B(c,ρc) = H(c,ρc) and Cauchy-Schwarz applies as normalised. W(6,0) is definite exactly for |δ| > √2, there is no radical for r ≥ 5, c survives for r ≥ 3, and the sign of A is harmless.

The one false statement is in §4.6. The equivariance note says B(v_s,x) = 0 ⟺ P_s x = 0, with B bilinear. That fails unless s is mirror-symmetric. P_s is H-orthogonal, so P_s x = 0 ⟺ H(v_s,x) = 0 ⟺ B(v_{r(s)},x) = 0. Here r is the reflection σ_i → σ_i^{-1}, and bar(v_s) is parallel to v_{r(s)}.

Check at A = 1.37 with s = σ3(∂{1,2,3}):
- max|B(v_s, ker P_s)| ≈ 4.7;
- B(v_{r(s)}, ker P_s) ≈ 3e-15.

Script and output: ~/jones-lanes/g2-proof/ref-heegaard/ref_check.py and ref_check.out. The model lane uses H throughout; the builder switched to bilinear B for v_s without saying so.

The status claim is also overstated. "No positivity mechanism reaches the unknot (proved)" is not proved:
- No-go 1 is a tautology: Cauchy-Schwarz equality can only happen at sup|f| ≥ |f(1)| = |δ|^3.
- No-go 2 is stated for an undefined class ("constructions whose V is determined by V_K") and only checks four examples.

Together they rule out Cauchy-Schwarz-equality arguments for functions determined by V_K. They do not rule out positivity in general.

### repair

1. In every statement about v_s (HC, Theorem F, Prop D, the transport in Lemma D.1), either replace B by H or keep B and replace v_s by v_{r(s)}. Nothing breaks:
- Prop D is unchanged, because c is bar-invariant, so B(v_s,c) = 0 ⟺ B(v_{r(s)},c) = 0.
- HC and Theorem F are existential over Haken(c), which r preserves, so they survive with witness r(s).
- In Theorem F(i) the witness on the coset is r(h1 s0), not h1 s0.
- In F(ii) the common reducing curve is r(s).

2. Retitle §4 as obstructions to Cauchy-Schwarz-equality arguments:
- keep No-go 1 as a remark;
- mark No-go 2 [HEURISTIC] and restrict it explicitly to the four listed operations;
- drop "no positivity mechanism" from the summary and the table.

3. Lemma D.1 (c)⟹(a) also needs the equivariant Dehn lemma (Meeks-Yau, Kim-Tollefson) to get an ι-invariant disk. Cite the "a power of a twist extends iff the curve bounds a disk" input precisely.

4. §4.7, two corrections; the conclusion is unaffected:
- Torus knots T(3,q) arise from fibre-orientation-preserving involutions and are not all Montesinos. The conclusion holds anyway, since torus knots have V ≠ 1.
- The non-Seifert case also includes JSJ decompositions with hyperbolic pieces, not only graph manifolds.

5. Add the citations listed under already_known.

### already_known

- Theorem A's inequality is Jones 1987, Prop 15.6 (plats on 2n strings), and F5 is Jones's Note 13.19. Only the equality case is new, and as the builder says it is restatement-level.
- F ⟺ W(5,1) faithful is published: Kasahara, arXiv:0803.0304 (2008), Cor 4.1. He states it for the transposed shape [2²,1], which has the same kernel.
  - His Thm 5.1 gives ker ρ = ⟨ι⟩ ⊕ (ker ρ ∩ Torelli), so any kernel lies in the Torelli group.
  - His Remark 5.6 (via Long) gives W(5,1) faithful on B_4 ⟺ Burau_4 faithful.
  - So F3's chain is a 2008 result, not a claim. Neither heegaard.md nor read-status cites it.
- The closed-braid chain is known: T ⟹ Temperley-Lieb rep of B_4 faithful ⟺ Burau_4 faithful (Bigelow 2002 Prop 1.5, plus Ito 2015).
- The builder's EKT reading is correct (checked pp. 157, 164, 166):
  - LLL(n) = H(T,−3), and U^N = N(−3) is a trefoil, since integer tangles twist west to east.
  - In every Theorem 3.3 family, all but at most one member has a nontrivial 2-bridge-knot component.
  - So no EKT link is a 3-bridge counterexample to U.
- Not found in the literature:
  - U ⟺ Stab[c] = H;
  - U ⟹ F;
  - T_3 ⟹ F via Hempel distance. read-status found no plat version of Ito, and the distance argument fills that gap. It may be folklore.


## Agent: ref:kernel


### verdict

damaged

### strongest_objection

The universal form [T_{c0}, f] = [(s1 s2)^3, f] is not T_gamma T_{f gamma}^-1. The 3|3 twist (s1 s2)^3 lifts to the half-twist h_c, with h_c^2 = T_gamma = (s1 s2)^6, and h_c acts on H as J_c (-1 on P_c). So kappa_f has Mess class (J_c - 1)[f] and tau_2(kappa_f) = (J_c - 1)tau_2(f). Neither vanishes in general.

The claims "kappa_f lies in [I_2,I_2] and F_2 automatically", Remark 2.3(a) and R1 ("same-splitting pairs pass orders 0 and 1 for free") are therefore false for the stated form. Exact check with f = T_d^2, d = s3(c0): ord_zeta(rho - I) is 1 for [(s1s2)^3, f] and 2 for [(s1s2)^6, f]. The order is the same in Kasahara's lattice: both reductions at q = -1 are irreducible, so the lattices are homothetic. For the pair of lines only order 0 is free; order 1 is exactly the tau_2 condition m(f) in Q u_0.

Second defect: the F_4 condition for f = [T_g1, T_g2] can never hold when the splittings differ. With w = (2D_20-1)u_1 - (2D_10-1)u_2, <w,u_0> = 0 identically, so w in Q u_0 forces w = 0 and u_1 = +-u_2. That class is excluded, not just "coplanar"; one instance gives order exactly 3.

Third: candidates whose curves all lie in a 4-punctured disk are exactly the Burau_4 question (excluded if BBB holds). This is not flagged.

What survives: the location in SI, Theorem A (re-checked with D = -2, -1, 2, giving r = 25, 9, 9), the trichotomy, Theorem B, the certificate (Cauchy-Schwarz on the definite arc |theta| < pi/8), and the Ito route. Ito's Thm 1 as printed covers non-trivial non-central normal subgroups and an unknotted alpha. The kernel lies in PB_5, so the closure is a knot, and e(beta) = 0. Details: ~/jones-lanes/g2-proof/ref-kernel/scratch_notes.txt

### already_known

- The location (Kbar in SI, the kernel pure, ker cap I_2 = intersection of the F_k) is Kasahara 2008 (arXiv:0803.0304) Thm 5.1 with Lemma 5.4, plus the setup of K2001. It is miscited as AGT 2001.
- F_2 = ker tau_2 is K2001 Cor 1.2.
- Theorem B is a restatement of read-model Prop A, i.e. injectivity of c -> [v_c].
- Prop C is the standard bound comparing degree span with order of vanishing, and is tautological as a target. "Depth <= C|f|" is equivalent to faithfulness and adds no leverage.
- The certificate is ordinary unitarity plus Cauchy-Schwarz.
- The Ito route is exactly Ito 2015 Cor 2 with Long's Lemma 2.1. Thm 1 is Bigelow's Conjecture 3.2 (JKTR 2002), and Kasahara 2008 anticipated the link to knots.
- The plat route is the classical 3-bridge / genus-two Heegaard picture. Its nontriviality step (Hempel distance) is quoted from memory.
- Theorem A and Prop D were not found in any source the lanes read. They are short consequences of Kasahara's Lemma 2.1 (q = -1 is the SO(3,2) representation on Lambda^2_0) and amount to <u_c,u_c'> = 4D - 2 being congruent to 2 mod 4. Theorem A does make F6 vacuous.
- R2 is not evidence: graded kernels are compatible with faithfulness, since free groups of countable rank embed in SL_2(Z).

### repair

Make kappa_f := [T_{c0}^2, f] = [(s1 s2)^6, f] = T_gamma T_{f gamma}^-1 the universal form throughout (Theorem B, Section 4, the certificate, Ito). The kernel criterion is unchanged: [T_c^k, f] is in the kernel iff rho(f) fixes [v_0], for any k != 0. With this change Remark (a), 2.4 and "F_2 automatic, F_3 iff m(f) in Q u_0" become correct.

If (s1 s2)^3 is kept instead, every depth index drops by one: kappa_f is in F_2 iff m(f) is in Q u_0, and its class in H_1(I_2) is (J_c - 1)[f], not 0. Rewrite R1 to say that for the pair of lines only order 0 is free, and order 1 is the tau_2 condition. Kasahara's Cor 1.2 makes that condition necessary for every candidate.

In 2.4, replace "in particular coplanar" with: <w,u_0> = 0 identically, so the condition forces u_1 = +-u_2. Then add every f = [T_g1, T_g2] with distinct splittings to the excluded list.

In Section 4, require that c_0, d_1, d_2 do not all miss some 2|4 curve. Otherwise the class is the Burau_4 problem and BBB applies.

Restrict Corollary A2's "kills the only known mechanism" to 3|3 twists, because other elements acting as scalar plus rank one in SI are not classified.

Fix the citation to Kasahara 2008 Thm 5.1. Note that the plat route's V = 1 needs no writhe bookkeeping: for a knot, <K> = unit times <U> already forces V = 1.
