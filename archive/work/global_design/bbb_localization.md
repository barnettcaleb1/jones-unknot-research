# A Brunnian localization lemma for the actual comparison arcs

2026-11-03. Node: BBB-MULTISET. Holder: Codex.

Status: the disjoint-disk localization lemma below is TRUSTED, with a written proof, independent internal read, and Claude162836 sketch-level read. It is elementary planar topology and free-product normal form; no novelty claim. The proposed implication FROM polynomial equality TO localization is OPEN.

## 1. Comparison arcs and the deletion property

Let Phi be a pure Brunnian braid on the old punctures p1,p2,p3,p4. Add an auxiliary puncture p5 and let Gamma be any pure braid on the resulting five-punctured disk. Let b be a fixed arc from the boundary basepoint to p3, and put

  b0 = b Gamma,       b1 = b f(Phi) Gamma.

Products act on the right. The particular BBB push is an instance, but the localization lemma does not need its disk assertions.

For every j in {1,2,4}, the arcs b0 and b1 become isotopic after filling in pj: deletion is a homomorphism on pure braids, deletion of Phi is the identity, and the same deleted Gamma remains on both sides. The endpoint p3 is retained.

This is considerably stronger than equality of their winding numbers. The proof below uses these actual isotopies.

## 2. Disjoint-disk localization

**Lemma.** Suppose b0 and b1 have representatives which coincide outside finitely many pairwise disjoint embedded disks E1,...,Ek in the interior of D5. Require:

1. The disk boundaries avoid all punctures.
2. Each arc visits each Ei exactly once, in a proper subarc with the same boundary endpoints on the two representatives.
3. The disks avoid p3.
4. For each Ei, at least one of p1,p2,p4 lies outside Ei.

Then b0 and b1 are isotopic in D5. Consequently Phi is the identity.

**Proof.** Use b0 as a reference arc. Collapsing each disk to a vertex, its common exterior portions form an embedded chain: the once-per-disk condition prevents a repeated vertex. A thin neighborhood N of this chain, the disks, and the common terminal path to p3 is a disk containing exactly the disk punctures and p3.

Use the reference chain as a tree of access paths. Van Kampen gives

  pi1(N minus punctures) = G1 * ... * Gk * <z3>,

where Gi is the fundamental group of the punctured Ei transported along the reference tree and z3 is the peripheral generator at p3. Empty Gi are allowed. The inclusion of this group into the punctured ambient disk is injective. The comparison loop, with the common endpoint truncated just before p3, has the form

  w1 w2 ... wk,       wi in Gi,

with at most one syllable in each disk factor. The access-path conjugations have been absorbed into this tree-based free-product decomposition; they have not been discarded. The formula follows by inserting and cancelling the reference prefixes between consecutive replacement subarcs.

Fix i and choose an old puncture pj outside Ei, with j different from 3. After deleting pj, Gi is unchanged and injective. Other disk factors either stay unchanged or lose one puncture; they cannot merge with Gi. If wi is nonidentity, it remains the sole syllable in that factor and cannot cancel in the reduced word.

On the other hand, the deletion property makes the puncture-ending arcs isotopic. For based arcs ending at p3, this says their comparison loop lies in the peripheral subgroup <z3>; this formulation allows endpoint rotation and does not assume a fixed tangent at the puncture. A word with a nonidentity Gi syllable cannot be in the separate <z3> factor. Thus wi=1.

Repeat for every i. All replacement subarcs are homotopic relative endpoints in their punctured disks, hence isotopic. These isotopies can be performed in disjoint disks, so b0 and b1 are isotopic simultaneously.

Undo Gamma. Phi fixes the isotopy class of b. The forget-p3 map is injective on the stabilizer of a boundary-to-p3 arc: cut along that fixed arc to obtain the disk with the other three punctures. Since Phi is Brunnian, its image under forget-p3 is the identity. Therefore Phi=1. QED.

**Terminal-disk variant.** One of the disks may instead be the terminal disk containing p3, provided it contains one boundary-to-p3 segment of each arc and still omits at least one of p1,p2,p4. In the free product its group replaces the separate <z3> factor and contains that peripheral subgroup. Deleting a puncture outside it first forces every other disk syllable to vanish; it then forces the terminal comparison element to lie in <z3>, which is exactly isotopy of the two terminal arcs within that disk. Alternatively, first eliminate the other factors using their respective outside punctures, then apply the same argument to the terminal factor. This variant uses no new mechanism.

Both versions have an independent internal read. The terminal variant is written out separately because its comparison need only be peripheral, rather than the identity, before interpreting it as an arc isotopy.

## 3. What this changes in the geometric target

The previous matched-ribbon proposal sought an embedded EMPTY bigon-forming polygon. That is sufficient but unnecessarily restrictive for a Brunnian comparison.

A different sufficient endpoint is a simultaneous localization of the WHOLE comparison into the disks of the lemma. The regions may contain punctures, and the matching loops inside them may initially self-intersect. Actual deletion isotopies, together with free-product normal form, eliminate that ambiguity.

The revised proof obligation is:

  equality of anchored colored occupation polynomials
     => simultaneous one-visit localization in proper punctured regions
     => Phi=1.

Only the second implication is proved. No implication from equal polynomials to localization is asserted. This remains a proposed mechanism under the same held target, not a new faithfulness theorem.

A nontrivial Brunnian comparison admitting a once-per-disk decomposition must have at least one disk containing ALL of p1,p2,p4. Otherwise the lemma applies. Repeated visits to a disk also invalidate the single-syllable argument: they can form commutators after other factors are deleted. These are precise geometric possibilities that a localization proof must address, not formal counterexamples to the BBB configuration.

## 4. Calibration: ordering alone is insufficient

Let c bound a disk containing p3 and p4, disjoint from alpha (the p1-to-p2 arc) and from p5. Choose a simple boundary-to-p3 arc b which crosses c and has essential intersections with alpha before entering c. A nonzero twist about c changes the isotopy class of b.

Nevertheless c is disjoint from alpha, and the twist has a lift fixing the chosen based lift of alpha. It preserves every signed colored intersection with every translate of that lift. Thus b and T_c(b) have identical colored Moody polynomials; indeed their crossings with alpha have the same order and the same individual labels.

This is an actual planar arc pair, not a formal occupation measure. It does NOT satisfy the required Brunnian comparison hypothesis: a twist enclosing only p3,p4 survives deletion of p1 or p2. It therefore calibrates the need for Brunnian input without refuting BBB-MULTISET.

The example also warns against treating equal height data as information about an unobserved terminal excursion.

## 5. The annular part is already rigid

For a puncture-free annular corridor whose core surrounds the old four punctures, the coloring on its fundamental group is n -> (4n,0). If it also surrounds the auxiliary puncture, it is n -> (4n,n). Both are injective.

Consequently two embedded corridor arcs with the same fixed endpoints and the same deck displacement are homotopic, hence isotopic, in that annulus. In its universal strip, the lift endpoints determine the relative homotopy class.

Thus hidden ambiguity cannot live wholly in such a corridor. It must leave the corridor, or fail the simultaneous matching/confinement requirement. This is the place to use the actual nested-push geometry.

## 6. Do not infer simultaneous isotopies from the disk list

BBB explicitly states immediately after Lemma 6.2 that individual disk components can be moved off Gamma1, but that this cannot in general be done for all components simultaneously. The finite disk-type list therefore does not itself give the localization in section 3.

Primary source: [BBB, section 6.2, page 16](https://arxiv.org/pdf/2607.05283v2#page=16), with figures 6.5–6.6 inspected on page 18. No claim is made here about the validity of the pending explicit proper-product construction.

## 7. Next action

Claude's explicit Gamma test remains the next external object. There is no duplicate computation. The mathematical question for its actual arc arrangement is whether a same-height matching yields a simultaneous local comparison, rather than merely whether each individual disk can be normalized.

BBB-MULTISET, Burau_4 faithfulness, G2-TWIST and Jones unknot detection remain OPEN.
