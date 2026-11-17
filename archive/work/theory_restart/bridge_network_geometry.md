# Exact counting gadgets with boundary connectivity retained

17 November 2026. Cross-field theory pivot; no enumeration. Written elementary deductions, independently read internally, awaiting Claude's referee. These are restrictions on a possible bridge, not a Jones detection theorem or a hardness proof.

## 1. The translation and the imported machinery

A classical link diagram is a signed plane-graph partition function: Kauffman's signed Tutte polynomial specializes to its bracket. This is an established bridge to statistical mechanics, not a new translation. [Kauffman, *A Tutte polynomial for signed graphs*, Discrete Applied Mathematics 25 (1989), §§3–5](https://homepages.math.uic.edu/~kauffman/TuttePolySignGraphs.pdf).

The knot condition also has an exact graph formulation. For the connected plane graph G underlying a checkerboard diagram, the number of medial-link components is the nullity of its mod-2 Laplacian. Thus a one-component output requires nullity one, equivalently an invertible reduced Laplacian over F_2. This is independent of the crossing signs. [Silver–Williams, *On the Component Number of Links from Plane Graphs*, arXiv:1408.6815](https://arxiv.org/abs/1408.6815).

Consequently JC can be expressed as rigidity of the normalized signed partition-function fibre 1 on these nullity-one plane graphs, modulo diagram moves. This formulation alone is a restatement. The possible leverage is **exact gadget realizability**: classify which polynomial signatures can be built by actual diagrams, while retaining their endpoint matching and their closed components as part of the type.

Holant/holographic reductions provide a model for this kind of classification: they study exact tensor signatures and their composition, rather than just numerical evaluations. Their existing dichotomies concern specified fixed numerical signature classes, not our Laurent-polynomial identity fibre with a knot-output requirement. They cannot be imported as a hardness theorem here. [Cai–Fu–Guo–Williams, *A Holant Dichotomy: Is the FKT Algorithm Universal?*, arXiv:1505.02993](https://arxiv.org/abs/1505.02993).

The precise ambitious target would be a polynomial-time construction from two Boolean circuits C_0,C_1 to a knot diagram D such that

    V_D = 1  iff  #SAT(C_0) = #SAT(C_1).

That would give counting-class hardness of the exact fibre, and, conditional on JC, a collapse NP=coNP. No such construction is supplied. Approximate gate universality at one root does not supply the equality in this display.

## 2. Boundary-connectivity rigidity of a full skein signature

**Lemma.** Let T and S be classical tangles in the same marked ball with 2n boundary points, n>=1. If their complete relative Kauffman bracket classes obey

    [T] = epsilon A^k [S],  epsilon in {+1,-1},

then T and S have the same endpoint matching and the same number of closed components.

**Proof.** Write pi and sigma for their endpoint matchings, and r_T,r_S for their closed-component counts. Let ell(pi,sigma) be the number of cycles in the union of the two matchings (coincident edges counted as a two-edge cycle). It is at most n, with equality exactly when pi=sigma.

Any matching can be realized by n arcs in a second ball, with no closed components; the closing tangle may have crossings. Close both T and S first by a tangle realizing pi and then by one realizing sigma. Their component counts are respectively

    r_T+n, r_S+ell;    r_T+ell, r_S+n.

For any nonempty c-component link diagram, the absolute value of its reduced bracket at A=1 is 2^(c-1). This follows also by changing crossings: the two crossing types have equal bracket at A=1, curls change only its sign, and the unlink evaluates to (-2)^(c-1). The assumed monomial unit evaluates to +/-1. The two closures therefore give

    r_T+n = r_S+ell,
    r_T+ell = r_S+n.

Subtracting yields ell=n; then pi=sigma and r_T=r_S. This proves the lemma without requiring a noncrossing closing matching.

**Consequence.** An exact full-signature substitution up to a Laurent unit cannot change the component count in any fixed outside context. It cannot turn a link construction into a knot by changing connectivity while preserving that signature. The statement permits nontrivial substitutions with the *same* connectivity. It does not address a seam that cuts inside the old gadget, equality of only one closed evaluation, nonunit scalar factors, or a different outside context.

This gives a general version of the earlier warning about fusing EKT content: after cutting a seam, the required equality is in the larger boundary module. The old scalar equality is insufficient. The lemma is elementary; no novelty is asserted.

## 3. A width obstruction independent of topology

**Lemma.** Given a planar sweep of a diagram with N elementary events and at most w boundary endpoints at any step, its full Jones polynomial is computable in poly(N) exp(O(w)) bit operations.

**Proof.** Resolve each partial diagram in the noncrossing-matching basis of its frontier. There are at most Catalan(w/2)=exp(O(w)) entries. A local cup, cap or crossing updates these entries by a fixed finite set of Laurent-monomial operations. A completed circle multiplies by -A^2-A^-2. Across N events, degrees and coefficient bit lengths are O(N): the state expansion has at most exponentially many signed contributions, each of bounded exponential magnitude. The final writhe normalization is a monomial. The polynomial arithmetic overhead is therefore polynomial in N.

The decomposition is supplied; no algorithm for finding optimal width is being asserted. This elementary form is consistent with the more general singly exponential width algorithms for quantum invariants. [Maria, *Parameterized complexity of quantum invariants*, arXiv:1910.00477](https://arxiv.org/abs/1910.00477).

Hence a polynomial-time hardness construction that always supplies a sweep of width O(log N) would put its exact identity test in P. A coNP-hard construction of this kind would force P=NP. This excludes uniformly logarithmic-width gadgets under the usual separation assumption; it does not say that each individual hard instance has a large minimum width.

## 4. Two independent limits on the intended gadget theorem

The companion complexity note proves a second restriction: if every nontrivial output is visible in a uniformly bounded Taylor order at t=1, its exact unit test is also in P. Moreover, a fixed-prefactor encoding V_K-1=D(t)#SAT(C), with D fixed and nonzero, cannot have polynomial-size knot outputs: the first nonzero jet would grow exponentially on tautologies, whereas a fixed finite-type invariant grows polynomially with crossing count.

Thus a genuine exact counting reduction must handle unbounded perturbative depth and cannot remain uniformly logarithmic in supplied contraction width. It must also respect the connectivity lemma. These restrictions are useful before designing any gadgets. They are not evidence that hardness is impossible, and they do not turn our old width-one or width-two calculations into a new research assignment.

The open problem is now specific: which exact zero predicates can be realized by the classical tangle tensor calculus under these constraints? This is a candidate bridge to complexity theory, with genuine external machinery and independently checkable failure conditions. Establishing its universality or a structural obstruction would be new work; evaluation hardness by itself does neither.
