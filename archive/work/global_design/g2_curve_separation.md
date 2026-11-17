# Separating curves can be distinguished by trivial tangles

2026-11-03. Response to Q1 in the consolidated genus-two lane letter. Status: TRUSTED, complete written proof checked by an independent internal reader; main collaborator read and novelty check pending. This completes the tangle-invariant version of that letter's Lemma C. It does not establish the Jones vanishing criterion.

## Statement

Let c be an essential 3|3 curve on the six-punctured sphere. Let c_1,...,c_m be finitely many essential 3|3 curves, none isotopic to c. There is a trivial three-strand tangle S, with this marked boundary sphere, such that:

- c bounds a disk in the ball meeting S transversely once;
- no c_j bounds such a disk.

Thus c is reducing for S and all c_j are nonreducing. The curves may have identical homological splittings in the genus-two branched cover. No condition on their splittings is needed.

The stronger statement upstairs is that a marked genus-two handlebody can make a specified separating curve compressible and any finite list of other separating curves incompressible. Here incompressible means that the individual curve does not bound a disk; the whole boundary is of course compressible.

## Proof upstairs: retain a reduced free-product word

Take the double cover of the sphere branched at its six marked points. It is a closed genus-two surface Sigma. The lift gamma of c is separating and cuts Sigma into once-punctured tori Q_1,Q_2. Write gamma_j for the separating lift of c_j. Distinct 3|3 classes have distinct lift classes: one can use an invariant hyperbolic metric and the unique geodesic in each class to see injectivity here.

Put each gamma_j in minimal position with gamma. Two nonisotopic separating curves on a genus-two surface cannot be disjoint: an essential separating curve disjoint from gamma would lie in one once-punctured torus and be parallel to its boundary. Hence every gamma_j meets gamma.

Every segment of gamma_j in a Q_i is an essential properly embedded arc. A boundary-parallel segment would, by choosing an innermost such segment, give a bigon with gamma and contradict minimality. After capping the boundary of Q_i by a disk, each essential arc closes to a nontrivial primitive loop on the torus. Equivalently, cutting a once-punctured torus along an essential arc gives an annulus, and the closed loop has a dual curve meeting it once.

Compress the inner boundary of Sigma times [0,1] along gamma. The resulting compression body C has positive boundary Sigma and negative boundary two tori. Its fundamental group is

    pi_1(C) = Z^2 * Z^2.

One can see this either by cutting its single connecting one-handle or from

    pi_1(Sigma) / <<gamma>>
      = <a,b,u,v | [a,b]=1, [u,v]=1>.

The successive segments of gamma_j give a reduced alternating word in the two Z^2 factors, with every syllable nonzero. Paths joining their endpoints to a basepoint along gamma cause no extra syllables: gamma is killed in C. The word is cyclically reduced as well, but ordinary reducedness is enough.

There are finitely many nonzero syllables across the entire list. For each i choose a primitive homomorphism ell_i:Z^2 -> Z that is nonzero on all syllables in the i-th factor. Explicitly, after choosing coordinates,

    ell_i(a,b) = a + N_i b.

Each nonzero syllable forbids at most one integer N_i. Thus an admissible N_i exists; if there are M_i syllables on that side, at least one integer in {0,...,M_i} works.

Fill the i-th negative-boundary torus of C by a solid torus whose meridian generates ker ell_i. The result H is a genus-two handlebody, the boundary connected sum of the two filling solid tori. The original separating disk with boundary gamma remains present. On fundamental groups the filling is

    Z^2 * Z^2 -> Z * Z,

with factor maps ell_1 and ell_2. Every syllable of every gamma_j survives. Therefore every image word remains nonempty and reduced, so gamma_j is nontrivial in pi_1(H). In particular, gamma_j does not bound a disk in H.

This proves the asserted separation upstairs. It uses no disk-set limit theorem, disk-complex rigidity, or uniqueness assertion about compression disks.

## Direct realization as a trivial tangle

The two sides of c downstairs are disks with three branch points. Each has once-punctured-torus double cover Q_i. A chosen primitive meridian slope on the capped torus is the lift of a suitable arc joining two of the three branch points. To see all slopes occur, the two standard half-twists downstairs lift to Dehn twists about curves intersecting once upstairs; their action generates SL(2,Z), which is transitive on primitive slopes.

Choose the corresponding arc alpha_i in each side of c. Join the two remaining branch points by a third arc alpha_0 that crosses c once and is disjoint from alpha_1 and alpha_2. Such an arc exists: each disk minus its interior endpoint-to-endpoint arc is connected. Push the interiors of these three disjoint arcs slightly into a ball. Their disjoint bridge disks make the resulting three-strand tangle S trivial.

The obvious disk bounded by c meets only alpha_0, and meets it once. Its lift is the separating disk with boundary gamma. Cutting the tangle cover along this disk gives precisely the two solid tori whose meridian slopes were selected above. Thus the cover is the marked handlebody H, not merely an abstract homeomorphic handlebody.

If a c_j bounded a disk meeting S once, the double cover of that disk branched at its single intersection would be a disk in H with boundary gamma_j. This contradicts the nontrivial free-group word. Hence all c_j are nonreducing for S. QED.

## What this removes from the Jones route

Let v_c be the spin-3/2 line vector, and H the generic invariant Hermitian form on W(6,0). The easy skein implication is established:

    c reducing for S  =>  H(v_c,S)=0.

The unresolved twisted-unlink rigidity statement is the converse, for all trivial tangles S. If that converse holds and distinct curves c,c' have the same spin line, use the theorem to choose S reducing for c and nonreducing for c'. Their proportional vectors have the same zero pairings; this contradicts the proposed converse. Therefore the converse makes the curve-to-line map injective.

The coordinated lane's rank-one twist argument then gives genus-two faithfulness modulo the hyperelliptic involution, and the published braid comparison gives faithfulness of W(5,1). For the published comparison see [Kasahara, Remarks on the faithfulness of the Jones representations, Corollary 4.1 and Theorem 5.1](https://arxiv.org/abs/0803.0304). We have removed Lemma C as a separate gap; we have not proved the converse vanishing implication.

Faithfulness by itself would not prove Jones unknot detection. The proposed additional Haken-curve statement for Jones-unit three-bridge knots also remains OPEN. No claim about the general Jones conjecture or literature novelty follows from this lemma.
