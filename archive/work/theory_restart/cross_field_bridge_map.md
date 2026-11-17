# Cross-field theory: first ranked map and concrete tests

17 November 2026. Caleb's pivot pauses the arborescent and width-two programmes and stops the counterexample lane. This note proposes theory, not a new search. Companion reports contain the primary sources and written proofs. New elementary deductions are TRUSTED pending Claude's read; no novelty or external review is claimed.

Archive check: the 3 November notes `work/global_design/crossfield_category.md`, `colored_propagation.md`, and `projection_prior.md` already recorded the central-charge gap, a stronger formal color-propagation obstruction, and the signed-Tutte/graphic-code dictionary. Those are retained barriers, not new discoveries or reasons to restart those routes. The new emphasis below is the exact-gadget restrictions and a specific deformation-extension falsifier.

## 1. First choice: exact gadget theory, joining complexity and planar tensor networks

**Precise translation.** Let JT be the language of explicit knot diagrams with V=1. JC is the equality JT=UNKNOT. JT is unconditionally in C_=P: each Jones coefficient is a GapP state sum, and the sum of the squares of its differences from 1 is a single GapP function vanishing exactly on JT. Unknot recognition is unconditionally in NP intersect coNP. Therefore a deterministic polynomial-time many-one coNP-hardness theorem for JT would imply JC => NP=coNP. This is a genuine conditional connection to an independent problem, not an equivalence between JC and a complexity separation. [Details and primary sources](bridge_complexity.md).

**Why it could help.** Exact tensor-signature and gadget classification from Holant/counting complexity studies which algebraic operations topology can realize. The target is the exact Laurent-polynomial fibre, not approximate evaluation at a root. A symbolic zero-test construction, or a structural obstruction to one, would explain something our quantum-topological calculations do not.

**What already survives as a first result.** Two independently useful restrictions are proved in the reports:

- Bounded-order Jones jets are polynomial-time computable; a family whose nontriviality is always visible in a fixed number of jets has its unit test in P. Fixed-prefactor encodings V_K-1=D(t)#SAT(C) with polynomial-size output are impossible by polynomial growth of finite-type invariants.
- With a supplied sweep of width w, the full polynomial is computable in poly(N) exp(O(w)); uniformly logarithmic-width gadgets cannot prove hardness without P=NP.

The proposed construction must therefore have genuinely unbounded depth and width, and must preserve its zero predicate exactly. Existing root-evaluation hardness does not meet that specification. Computational hardness of evaluation already occurs in families whose special trivial fibre is easy.

**My additional geometric restriction.** Full relative bracket equality up to a Laurent unit preserves the endpoint matching and the number of closed components. The two-closure proof is in [the network note](bridge_network_geometry.md). A fixed external fusion cannot convert a link mechanism to a knot while preserving a full signature and changing its connectivity. Cutting inside the gadget is a different, higher-boundary problem. Also, V_L=1 already forces L to be a knot by V_L(1)=(-2)^(c-1); equality to the c-component unlink polynomial is a different decision language.

**First open statement.** Determine whether exact classical tangle signatures can implement a zero-test-preserving encoding of equality of two counting circuits, with polynomial-size connected closures. Before any proposed construction is pursued, it must display its symbolic operations, its connectivity, and how it avoids the two restrictions above. This is a hard theory target, not a plan to enumerate gadgets. Existing Holant dichotomies do not answer it because their hypotheses concern fixed numerical signatures and a different output problem.

## 2. Second choice: derived realization obstructions, rather than another detector

**Precise translation.** In the unknot-filling fibre, Lemma Q asks whether a rational bracket class forces an actual tangle object to be rational. Passing from Bar–Natan complexes to immersed curves/Fukaya categories is already established theory. Its value lies in separating formal objects from ones realized by a tangle with the specified filling, not in renaming the Euler characteristic. [Source audit](bridge_categories.md).

**Why it could help.** Higher operations and coherent filling/cobordism maps retain data discarded by the Grothendieck group. KWZ's B*[U] extension is a concrete precedent: actual tangle structures extend, and uncancellable higher-product terms prove a geography restriction. A relative obstruction to an enhancement could rule out a formal Jones-flat object without assuming positivity of its Euler polynomial.

**What does not work.** A new homology theory that detects rational tangles is not enough; existing categorifications already detect them. Every additive central charge still kills Q+Q[1]. A stability mass sees those summands, but equal bracket class provides no bound on that mass. The archived tangle data contain adjacent-shift pairs, ruling out universal semistability/common-heart positivity under their recorded realization identification; that diagram identification was not independently reconstructed in this pass. Formal ladder examples survive the separately available closure and spectral-sequence constraints.

**First statement and test.** Extension over any fixed A-infinity algebra deformation is closed under finite direct sums and shifts, by block-diagonal structure maps. Hence if the rational arc A and a single compact ladder block Q each extend, then all the formal ladders extend. The first finite task is the extension problem for this one Q over the *exact* KWZ deformation. If Q extends, mere extension existence cannot exclude the ladders. If it does not, the whole ladder must still be checked: deformed summands can interact. A stronger candidate must specify additional coherent maps and an actual relation they cannot satisfy; we have not identified one yet.

This is a proposed source of a real reduction, not a completed reduction. Do not invent a new invariant before locating the extra relation. Functorial and stable-homotopy refinements also already exist, so adding “coherence” without an explicit new constraint is insufficient.

## 3. Third choice: arithmetic zero witnesses from geometry

**Precise translation, proved algebraically.** For P in Z[t,t^-1], the following are equivalent: P is a Laurent unit; P has no zero in the multiplicative group of any finite field; P(zeta_n) is an algebraic-integer unit for every n. A nonconstant shifted polynomial acquires a nonzero root over some finite extension of F_p; the root's multiplicative order supplies a nonunit cyclotomic specialization. For normalized knot polynomials, V(1)=1 and V'(1)=0 force a Laurent unit to be 1. Thus JC is exactly:

> Every nontrivial knot has a finite field F and alpha in F* with V_K(alpha)=0.

[Proof and arithmetic audit](bridge_arithmetic.md).

**Why it might help.** It replaces simultaneous coefficient cancellation by existence of one arithmetic zero. The missing leverage would be a geometric construction of that zero, independently of computing V. Merely passing to a maximal ideal after assuming V is nonunit is circular as a topological argument. At present this is a useful exact reformulation, not a genuine reduction to a known theorem.

**First theorem supplied and first open step.** The equivalence above is a complete elementary theorem. The next useful statement must relate an actual geometric structure to such a zero. No universal nonabelian character-variety-to-Jones-zero map is asserted. Verification of a proposed root still requires Jones evaluation; the algebraic formulation alone does not give an efficient certificate from a diagram.

**Why generic Habiro rigidity is not the missing step.** The formal integral cyclotomic sequence H_0=H_r=1, all other H_k=0, is q-holonomic and has J_2=...=J_r=1 but J_(r+1)!=1. Thus integrality, root/Taylor compatibility and q-holonomicity alone do not propagate triviality between colors. A proposed propagation theorem needs an actual-knot realization constraint and must fail on this explicit model. The all-colored detection endpoint is itself still listed as open; it cannot be assumed after propagation. Mahler measure alone fails already for the figure-eight.

## 4. What the ranking means

The first bridge presently gives the sharpest new constraints and connects to an independently meaningful complexity problem. The second has the most plausible route to information genuinely missing from J, but its first task is an inexpensive obstruction test, not wholesale construction of a homology theory. The third is an exact alternative language with a clearly located geometric gap.

The signed-graph translation is an enabling bridge for the first item, not a fourth solved approach: knot connectivity is mod-2 Laplacian nullity one, while the partition function retains signed interference. Matchgate/positivity theorems have hypotheses and do not automatically cover this fibre.

Nothing here proves JC, Lemma Q, a complexity hardness theorem, or a new realizability constraint. The advance is a set of precise targets and falsifiers that separates useful imported structure from a reformulation which leaves the same gap untouched. My recommendation is to build the exact-gadget theory first and perform the single-block deformation test before committing to a new categorical construction. No old scan or class ladder is resumed.
