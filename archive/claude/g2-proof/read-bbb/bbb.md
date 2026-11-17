# Bharathram, Birman, Brendle, arXiv:2607.05283: proof architecture

Lane g2-proof, task read-bbb, 2026-11-03.

**Source.** V. Bharathram, J. S. Birman, T. E. Brendle, "The Burau representation is faithful for n = 4". v1 is dated 6 Jul 2026. v2 (the current version, 14 Sep 2026) has 28 pp. and 32 figures and is unrefereed. I read the arXiv HTML of v2 through WebFetch. To pin down the exact wording of the key statements, I also extracted text from the v2 PDF that WebFetch had already saved. Everything below is paraphrase unless it is in quotation marks. Remarks that are mine and not the paper's are marked **[mine]**.

**One-line summary.** The proof runs on Moody's arc-pairing criterion in Bigelow's planar form. It shows that every nontrivial Brunnian 4-braid stays out of the kernel after it is stabilized into B_5. The proof uses a "parity condition" on disk sequences, and parity forces the Moody polynomial to have no cancellation. One point-push in B_5 repairs the single parity-violating disk type that occurs in B_4. The proof uses no forks, no train tracks, no orderings, no Lawrence-Krammer, and not the free group ker(B_4 -> B_3) ≅ F_2. The paper explicitly avoids that last approach ("we do not consider elements in the image of ρ4 that potentially generate a free group", citing Birman's book, Thm 3.19). The free group it does use is the point-pushing group K_4 = π_1(D_3, p_4) ≅ F_3.

---

## 0. Conventions (Section 2)

- B_n = Mod(D_n), with marked points p_1..p_n and a basepoint p* on the boundary. Braids act **on the right**, (β)Φ, and products are read left to right.
- ρ_n is the **unreduced** Burau representation. It is the action on H_1(D̃_n, {p̃*}), a free Z[t^{±1}]-module of rank n, where D̃_n is the Z-cover given by the exponent sum π_1(D_n, p*) -> Z (following Long-Paton).
- α is the horizontal arc from p_1 to p_2, oriented left to right. β*_3 is a fixed arc from p* to p_3. For a braid Φ, set β = (β*_3)Φ.
- **Moody polynomial.** M(α,β) = Σ_ℓ (t^ℓ α̃, β̃) t^ℓ, the algebraic intersection in the cover, defined up to a power of t. In planar form, M(α,β) = Σ_{i=1..m} ε_i t^{k_i}, where q_1..q_m are the points of α∩β in order along β. The sign is ε_i = +1 when β points down at q_i. Set M_Φ = M(α, (β*_3)Φ). M_Φ depends only on the homology class [(β*_3)Φ] in H_1(D̃_n, {p̃*}).

## 1. The reduction (Section 1): confirmed, with the exact reference

The board says "Long's reduction to Brunnian braids". **This is correct.** The citation is [Lon86, Theorem 2.2]: D. D. Long, "A note on the normal subgroups of mapping class groups", Math. Proc. Cambridge Philos. Soc. 99 (1986) 79-87. The paper paraphrases it as follows: ρ_n is faithful on B_n if it is faithful on any nontrivial noncentral normal subgroup of B_n.

- K_i is the point-pushing subgroup. It is the kernel of the Birman exact sequence that forgets p_i, so K_i ≅ π_1(D_{n-1}, p_i).
- Brun_n = ∩_i K_i is normal in B_n.
- **Proposition 1.2.** If ρ_4 is faithful on Brun_4, then ρ_4 is faithful on B_4.
- The noncentrality of Brun_4 is not checked in the text. **[mine]** It is immediate. Brun_4 ≠ 1 (Fig. 1.1 gives an example), and Brun_4 ⊂ K_4 is free, while the centre ⟨Δ²⟩ maps nontrivially under "forget p_4". The other half is also immediate: Burau sends Δ² to a nontrivial scalar, so ker ρ_4 ∩ Z = 1, and a nontrivial kernel is therefore noncentral.
- **Pseudo-Anosov input.** Whittlesey (Geom. Topol. 4, 2000) proves that every nontrivial Brunnian braid is pseudo-Anosov. The transfer from the punctured sphere to B_n is via Lee-Song (Pacific J. Math. 219, 2005, §1). This is used only to get ι(α, (β*_3)Φ) > 0 for every nontrivial Φ ∈ Brun_n.
- **[mine] For the lane.** The board's (F2) "normal-intersection lemma" is the content of Long 1986, the same theorem that BBB use here and that Kasahara uses as "Long's theorem on direct sums" (§8). It is a citation, not a new lemma.

## 2. Moody's criterion (Section 2)

- **Observation 2.1.** Let f: B_n -> B_{n+1} come from D_n ⊂ D_{n+1}. If Φ ∈ ker ρ_n, then f(Φ) ∈ ker ρ_{n+1}. The paper calls this "crucial". **[mine]** For unreduced Burau, ρ_{n+1}(f(Φ)) = ρ_n(Φ) ⊕ 1 as a block matrix, so the observation is in fact an equivalence. Passing to B_5 therefore loses nothing. It only supplies an extra puncture p_5 that can be pushed.
- **Theorem 2.2 (Moody, one direction).** Let n ≥ 3. Suppose M(α,β) ≠ 0 for every oriented arc β from p* to p_3 with ι(α,β) > 0. Then ρ_n is faithful. The paper notes that Moody's full result is an equivalence.
- **Theorem 2.3 (Moody, form used).** Let Φ ∈ B_n with n ≥ 3. If M_{Φ·Γ} ≠ M_Γ for some Γ ∈ B_n, then Φ ∉ ker ρ_n. The proof is two lines. If Φ ∈ ker, then Γ^{-1}ΦΓ ∈ ker, so the classes [(β*_3)ΦΓ] and [(β*_3)Γ] are equal, and M depends only on the class.
- **Corollary 2.4.** This is the case Γ = 1: if M_Φ ≠ 0, then Φ ∉ ker ρ_n.

## 3. Disk sequences and winding numbers (Section 3, Bigelow's tools)

Take consecutive points q_i, q_{i+1} along β. Let β_i be the β-subarc between them, which has no interior intersections, and α_i the α-subarc between them. Then α_i ∪ β_i bounds a disk Δ_i. Its winding number is W_i = ±|P(Δ_i)|, where P(Δ) is the set of marked points in the interior of Δ, and the sign is + when β_i runs clockwise. The sequence Δ_1..Δ_{m-1} is the **disk sequence** of Φ. Two disks are equivalent when they agree up to isotopy of β in D_n.

- **Lemma 3.1 (Bigelow).** W_i = k_{i+1} - k_i.
- **Corollary 3.2.** k_i = k_j if and only if Σ_{ℓ=i}^{j-1} W_ℓ = 0.

## 4. The parity condition and n = 3 (Section 4)

- **Definition.** A disk Δ with boundary points q_i, q_{i+1} is *sign-changing* if ε_i = -ε_{i+1}, and *sign-preserving* otherwise. A braid Φ satisfies the **parity condition** if every disk of its disk sequence is sign-changing exactly when |P(Δ)| is odd. This is a property of the whole disk sequence of (β*_3)Φ.
- **Lemma 4.2.** Let φ ∈ B_n, any n. If φ satisfies the parity condition, its Moody polynomial has no cancellation. Proof: if k_i = k_j, Corollary 3.2 makes the winding sum over the window zero. Then an even number of disks in the window have odd count. Under parity, these are exactly the sign flips, so ε_i = ε_j.
- **Consequence used later.** Suppose parity holds and the arcs are in minimal position. Then Σ|coefficients| of M_Φ equals ι(α, (β*_3)Φ). In particular M_Φ ≠ 0 when ι > 0.
- **Theorem 4.1 (Magnus-Peluso, new proof).** Every 3-braid satisfies parity, so ρ_3 is faithful by Theorem 2.2. A disk contains 1, 2 or 3 points, and the count 2 is exactly the sign-preserving type (Fig. 4.1).
- The paper adds that n-braids with n ≥ 4 "do not in general" satisfy parity.
- **[mine] A clean reformulation.** The proof of Lemma 6.1 shows two things for any n. First, P(Δ) is never contained in {p_1, p_2}, because β is simple and in minimal position. Second, Δ is sign-preserving if and only if it contains exactly one endpoint of α. Combining these, a disk satisfies parity if and only if **|P(Δ) ∩ {p_3,...,p_n}| is odd**. For n = 3 this always holds. For n = 4 it fails exactly for disks that contain both p_3 and p_4. This matches Lemma 6.1's lists.

## 5. Push-maps and proper products (Section 5, general n ≥ 4)

- Point-pushing comes from the Birman exact sequence 1 -> π_1(D_{n-1},p) -> Mod(D_n,p) -> Mod(D_{n-1}) -> 1. Γ ∈ K_n is the push of p_n around a loop. The loop is generic but need not be simple; simplicity is needed only for Theorem 6.9.
- **Piecewise Γ-arcs.** These are chains of subarcs of Γ, ordered along Γ, that switch at self-intersections and contain no loop.
- **Bigon-forming polygons.** There are four configurations. (i) Generalized bigons: a piecewise Γ-arc with both ends on α that bounds an empty polygon. (ii) β-to-α (generalized) trigons, where the Γ-side is oriented from β to α. (iii) β-to-α rectangles: two parallel Γ-subarcs bounding an empty rectangle, with two adjacent same-sign crossings of Γ with α. (iv) Versions of (i)-(iii) "with basepoint" through p_n. The paper says that only these configurations make bigons between (β)Γ and α.
- **Definition (proper product).** Let Φ ∈ K_n and β = (β*_3)Φ. Let Γ_I be the part of Γ from p_n to its first crossing with α, and Γ_F the part from its last crossing with α back to p_n. Let β' be the β-side of the innermost p_n-only disk of Φ, or ∅ if there is none. Then Φ·Γ is **proper** if some representative of Γ is in minimal position with α and β and satisfies two conditions. (1) There are no bigon-forming polygons among α, β and Γ. (2) Either (a) Γ_I ∩ β' ≠ ∅, or (b) Γ_I ∩ β' = ∅ and Γ_F ∩ β' = ∅. Condition 2 prevents Γ from undoing the p_n-only disk. Longer proper products are defined iteratively.
- **Proposition 5.1.** Let Φ ∈ K_n and β = (β*_3)Φ, and let Γ be based at p_n with Φ·Γ proper. Then (β)Γ and α are in minimal position. The proof sorts the intersections of (β)Γ with α into "original" and "new" ones and runs a case analysis on the vertices of a putative bigon. Each case contradicts properness.
- The paper states that up to this point **nothing uses n = 4**.

## 6. The 4-strand argument (Section 6)

The paper says n = 4 is used "particularly in Lemmas 6.1 and 6.3".

- **Lemma 6.1 (B_4).** Sign-preserving disks are exactly those with P(Δ) one of {p1,p3}, {p1,p4}, {p2,p3}, {p2,p4}, {p1,p3,p4}, {p2,p3,p4}. Sign-changing disks are exactly those with P(Δ) one of {p3}, {p4}, {p3,p4}, {p1,p2,p3}, {p1,p2,p4}, {p1,p2,p3,p4}. Four of these types violate parity: {p3,p4}, {p1,p3,p4}, {p2,p3,p4} and {p1,p2,p3,p4}.
- **Lemma 6.2.** Let Φ, Γ ∈ K_4, with Γ a push along a simple loop and Φ = Ψ·Γ proper. Then each single disk Δ_i of Φ either is a 1-disk containing only p_4, or has its β-side isotopable off Γ. The paper stresses that the isotopy is one disk at a time, not simultaneous.
- **The loop Γ_1.** Γ_1 is one specific simple loop based at p_4, given only as a picture (Fig. 6.3). In the free basis y_1, y_2, y_3 of K_4 (Fig. 6.13), its reduced word begins with y_2^{-1}.
- **Lemma 6.3.** Let Φ = Ψ·Γ_1 be a proper product in K_4. Then Δ is sign-preserving if and only if P(Δ) = {p2,p3}, and sign-changing if and only if P(Δ) is one of {p3}, {p4}, {p1,p2,p3}, {p1,p2,p3,p4}. The proof uses Lemma 6.2 and then a finite list of α-β disks disjoint from Γ_1 (Figs. 6.4-6.5, types δ_1..δ_5). **Consequence:** the only parity violator left is the **4-disk**, the disk containing all four points, and 4-disks are nested. Their β-sides form a "band".
- **Passage to B_5.** Add p_5 inside D_4, so that f: B_4 -> B_5. Call Γ ∈ K_5 *disjoint from β modulo 4-disks* if Γ_F crosses the band of 4-disk β-sides transversally, once per 4-disk, and Γ misses β otherwise. Call it *simple modulo 4-disks* if every self-crossing of Γ lies where Γ_F meets the boundary of an α-Γ 4-disk. Call it *properly simple modulo 4-disks* if it is simple modulo 4-disks and satisfies three more conditions: (1) every α-Γ disk is one of the five types of Fig. 6.5; (2) some α-Γ disk is the 3-disk containing p1, p2 and p3; (3) Γ_I does not meet β*_3.
- **Lemma 6.4.** Let Φ ∈ B_4, and let Γ ∈ K_5 be based at p_5 and disjoint from β modulo 4-disks. Then the disk sequence of f(Φ)·Γ is the disk sequence of Φ with each 4-disk replaced by a 5-disk, and every such 5-disk is sign-changing. A 5-disk has odd count, so parity is repaired.
- **Lemma 6.5.** If Γ is properly simple modulo 4-disks, then the signs of its crossings with β*_3 alternate, except between two consecutive 4-disks.
- **Lemma 6.6.** If Γ is properly simple modulo 4-disks, then Γ itself satisfies parity. The proof is a case analysis showing that the only disks are a 1-disk containing p_4, a 3-disk containing p1, p2 and p3, a sign-changing 5-disk, and a sign-preserving 2-disk.
- **Proposition 6.7.** Let Φ ∈ B_4 be a proper product Φ = Φ'·Γ_1. Then some Γ ∈ K_5 has three properties: f(Φ)·Γ is a proper product; f(Φ)·Γ and Γ both satisfy parity; and ι((β*_3)(f(Φ)Γ), α) ≠ ι((β*_3)Γ, α). The construction takes a point q in the innermost 4-disk. γ_1 runs from p_5 to q without meeting β. γ_2 runs from q back to p_5, crossing each 4-disk's β-side once. Set Γ = γ_2γ_1. For the inequality, γ_2 is modified in two cases (Figs. 6.9-6.12), using a nontrivial loop in the complement.
- **The paper's own remark on generalization (end of §6.3).** The construction iterates: for any n and any Φ ∈ B_n, one can find Γ_1..Γ_k with f(Φ)Γ_1⋯Γ_k satisfying parity, by correcting the innermost disk of each violating type. However, the product Γ_1⋯Γ_k itself cannot be guaranteed to satisfy parity. The authors write that needing to correct only one disk type, and so needing only one push-map, "is crucial". For k > 1 they cannot simultaneously arrange that Γ_2 misses both β and (β)Γ_1.
- **Corollary 6.8.** Let Φ ∈ K_4 be a proper product Φ'·Γ_1 with ι(α, (β*_3)Φ) > 0. Then some Γ ∈ K_5 has M_{f(Φ)·Γ} ≠ M_Γ. Proof: both polynomials have no cancellation (Lemma 4.2), and the arcs are in minimal position (Prop. 5.1). So the sum of the absolute values of the coefficients of each polynomial equals its ι, and the two ι differ by Prop. 6.7.
- **Theorem 6.9.** ρ_4 is faithful on Brun_4. The argument runs in four steps.
  1. Kernel membership is invariant under conjugation by B_4.
  2. Nontrivial Brunnian braids are pseudo-Anosov, so ι > 0.
  3. For a simple loop like Γ_1, the only possible bigon-forming polygons are trigons and rectangles. Trigons are removed by isotopy. Rectangles cannot occur because the crossings of α with Γ_1 alternate in sign.
  4. If the juxtaposition of reduced words is reduced in y_1, y_2, y_3, then condition 2 of properness holds. Since Γ_1 starts with y_2^{-1}, one conjugates so that the word does not end in y_2, "so that it can be written as a proper product Φ = Φ'·Γ_1".

  Then Corollary 6.8 gives Γ with M_{f(Φ)Γ} ≠ M_Γ. Theorem 2.3 gives f(Φ) ∉ ker ρ_5, and hence Φ ∉ ker ρ_4, implicitly by Observation 2.1.
- **Section 7.** This is an illustrative arc, not one that comes from K_4. Its Moody polynomial has cancelling ±t terms and violates parity. After the push Γ there is no cancellation.

## 7. Where n = 4 is used, and why the argument cannot give n = 5

**Uses of n = 4.**
1. Lemma 6.1, the finite disk-type lists.
2. Lemma 6.3. This is the essential use. The specific loop Γ_1 in D_4, together with the case analysis of Figs. 6.4-6.5, reduces the parity violators to the single type "contains all punctures".
3. Nestedness of 4-disks. A disk containing every puncture is nested with every other such disk, so a single push of one new point p_5 enters exactly those disks.
4. Lemma 6.6 and Prop. 6.7, the D_4-specific α-Γ disk types and the 3-disk containing p1, p2 and p3.
5. The free basis of K_4 ≅ F_3 and the first letter of Γ_1, in the conjugation step.

Sections 2-5 are valid for all n.

**Why not n = 5.** First, a necessary obstruction, which is **[mine]** but immediate. Burau_5 is unfaithful (Bigelow 1999). By Long's theorem, ker ρ_5 ∩ Brun_5 contains some Φ ≠ 1. For that Φ, Observation 2.1 and Theorem 2.3 force M_{f(Φ)Γ} = M_Γ for **every** Γ ∈ B_6. So the analogue of Corollary 6.8 must fail somewhere in B_5.

Where it fails, in the paper's words: more than one violating disk type needs correcting, so k > 1 pushes are needed, and then parity of Γ_1⋯Γ_k cannot be secured. In the reformulation of §4 above, the n = 5 violators are the disks with exactly two of {p3, p4, p5}. These come in three types and need not be nested, so no single extra point can flip exactly them. No analogue of Γ_1 and Lemma 6.3 is offered for D_5.

## 8. Remarks on Jones, W(5,1), genus two and knots

**What BBB say about the Jones representation.**
- **Corollary 1.1:** "The Jones representation of B_n is faithful for n = 4". The justification is that, "as Jones points out", the Jones representation of [Jon87] (Ann. of Math. 126) contains reduced Burau as a summand, so Burau faithful implies Jones faithful. The paper gives no definition, so this presumably means the full Hecke algebra representation.
- BBB also point to [Kas08, Remark 5.6] for the "equivalence" between Burau faithfulness and Jones faithfulness at n = 4.
- BBB never mention Temperley-Lieb, W(5,1), genus two, the Jones polynomial or the unknot. The only knot mentioned is the Borromean rings, as an example of a Brunnian braid.

**What Kasahara proves, read through the arXiv HTML.** The paper is Y. Kasahara, "Remarks on the faithfulness of the Jones representations", Adv. Stud. Pure Math. 52 (2008) 369-381, arXiv:0803.0304.
- **Thm 3.1.** For a rectangular Young diagram Y with n ≥ 6 boxes, Y ≠ [n], [1^n], Jones's representation of Mod(S_{0,n}) is faithful if and only if π_{Y_0} of B_{n-1} is faithful. Here Y_0 is Y with its one removable box deleted.
- **Genus two, §5, with Y = [2^3].** Thm 5.1: Ker ρ = Z/2 (the hyperelliptic involution) ⊕ (Ker ρ ∩ I_2), where I_2 is the Torelli group. Moreover ρ is faithful on I_2 if and only if π_{[2^2,1]} is faithful on B_5.
- **Remark 5.5.** Mess's theorem makes I_2 free, so any kernel is free.
- **Remark 5.6.** π_{[2^2,1]} restricted to B_4 splits as π_{[2,1^2]} ⊕ π_{[2,2]}. The summand π_{[2,2]} factors through B_4 -> B_3. By Long's direct-sum theorem, faithfulness of the restriction reduces to π_{[2,1^2]}, which is sgn ⊗ reduced Burau_4.
- Kasahara's introduction also notes that a nontrivial kernel element might produce a nontrivial knot with the unknot's Jones polynomial.

**[mine] Consequences for the lane.**
- (F3) is essentially Kasahara 2008 (Thm 3.1 at n = 6, Thm 5.1 and Rem. 5.6), written in transposed diagrams: [2^2,1] corresponds to the board's shape (3,2), and [2^3] to (3,3). This should be cited, not re-derived. The convention bridge (transpose versus a sgn twist) should be checked once, but Kasahara himself treats it as harmless.
- If BBB is correct, then W(5,1) is faithful on B_4 ⊂ B_5. The open rung is exactly W(5,1) on B_5, which is equivalent to the genus-two Jones representation on I_2.
- **Transfer caveat.** BBB's engine needs Burau's model as H_1 of a Z-cover of D_n, where M_Φ is a pairing of planar arcs. W(5,1) is a 2-point (Lawrence-type) homological representation, so the disk-sequence and winding-number combinatorics does not carry over as it stands.

## 9. Assessment (cheap checks only)

- **Gap or slip in Theorem 6.9.** The text establishes that the product **Φ·Γ_1** is reduced, and so proper, with Φ the Brunnian braid. It then asserts **Φ = Φ'·Γ_1**. Corollary 6.8 needs the latter: the Brunnian element itself must end in Γ_1. As written, the argument only shows ΦΓ_1 ∉ ker, which is vacuous.
- **[mine] Repair.** This looks like an expository slip. Any 1 ≠ g ∈ K_4 ≅ F_3 has a K_4-conjugate x g x^{-1} whose reduced word ends with the word of Γ_1 without cancellation. The conjugate stays in Brun_4 ∩ ker, since both are normal in B_4. The introduction's "final step" sentence confirms that this is the intent. What still deserves scrutiny is the briefly asserted claim that a reduced juxtaposition gives conditions 1 and 2 of properness.
- **Scope inconsistencies.** §6 opens with "faithful on ... K_4". Thm 6.9 is stated for Brun_4, and the outline calls Brun_4 "the point-pushing group". Prop. 6.7 takes Φ ∈ B_4, while Cor. 6.8 takes Φ ∈ K_4. All of this is harmless.
- **Where a referee should look.** The real weight lies in two figure-driven case analyses: Lemma 6.3 (Figs. 6.4-6.5) and Proposition 6.7 (Figs. 6.9-6.12).
