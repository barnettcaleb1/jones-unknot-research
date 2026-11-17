# CX-EKT-PAIR: a universal EKT partner cannot compensate a full twist

2026-11-03. Status: TRUSTED, hand derivation and two independent internal reads. Novelty unassessed. This is an obstruction to one proposed C1 construction, not a theorem detecting the unknot.

## Statement and scope

Keep the Eliahou–Kauffman–Thistlethwaite Hopf shell H(T,U) fixed. Let P,Q be boundary operations built from the two rational-tangle twist generators and their inverses. Suppose their simultaneous application preserves the bracket for **every pair** of input tangles, up to one fixed framing unit. If P is a nonzero power of a full twist about any essential rational boundary curve, no such Q exists.

Thus an ordinary twist site cannot acquire a universal compensating rational-boundary operation at the other input of this shell. This includes conjugated sites and arbitrary nonzero twist powers, with no bound on the length of the proposed partner Q. It does not exclude a cancellation on a particular pair of input vectors, operations crossing the fusion band, or a changed outer shell. In particular it does not rule out C1 itself.

## Matrices

Work over F=Q(A), with bar(A)=A^-1 and X*=bar(X)^T. Set

    d = -A^2 - A^-2,
    h = -A^14 - A^6 - 2A^2 - 2A^-2 - A^-6 - A^-14,
    H = [[h,d^2],[d^2,d]],
    G = [[d,1],[1,d]].

EKT Proposition 2.1' gives the Hopf closure as br(T)^T H br(U), in their reduced closed-bracket convention. Multiplying H by the common factor d to use the absolute bracket changes none of the argument. The two boundary generators are

    L = [[A,0],[A^-1,-A^-3]],
    R = [[-A^3,A],[0,A^-1]].

Direct multiplication gives L*GL=G and R*GR=G. Consequently every allowed boundary action is G-unitary. Both H and G are reciprocal and symmetric, and both are invertible over F.

Universal equality is exactly

    P^T H Q = u H,                         (1)

where u is the framing unit. The two crossingless input tangles span the skein module, so this equivalence needs no realization hypothesis for arbitrary vectors. Only u bar(u)=1 is used below; in particular every unit ±A^k is allowed.

## The second invariant form forces a commutant

Put S=G^-1 H. Since P is G-unitary, equation (1) implies

    Q = u S^-1 bar(P) S.

Also S^T G=G S and bar(S)=S. Substituting in Q*GQ=G therefore gives

    bar(P)^-1 S^-2 bar(P) = S^-2.

Taking bars shows [P,S^2]=0. The explicit matrix is

    S = [[d^2(d^2-3)^2, d],
         [-d(d^2-2)(d^2-4), 0]].           (2)

For verification, h=d^7-7d^5+15d^3-8d. Its trace d^2(d^2-3)^2 is nonzero in F. Cayley–Hamilton now gives [P,S]=0, hence [P,S/d]=0.

## Specialization excludes every nontrivial full-twist power

Divide S by d **before** specializing at A0=exp(pi i/4). This division leaves a regular matrix in (2), whereas H itself vanishes at this point. With C=diag(1,i),

    C^-1 (S/d)(A0) C = i J,
    J = [[0,1],[8,0]].

In the same basis the generators, with their scalar phases removed, are

    C^-1 (L/A)(A0) C = [[1,0],[-1,1]],
    C^-1 (A R)(A0) C = [[1,-1],[0,1]].

Thus every allowed word specializes projectively to a real integral matrix. A nonzero power of a conjugated full twist specializes projectively to a nonidentity unipotent matrix: for example L^(2k) becomes the lower shear with entry -2k, and conjugation preserves this property.

But the identity [P,S/d]=0 makes that matrix commute with J. The real matrix J has two distinct real eigenvalues, ±sqrt(8). Every commuting matrix preserves its two eigenlines and is diagonalizable over R. A nonidentity unipotent matrix is not diagonalizable. This contradiction proves the assertion.

The genuine EKT operation Omega=L^2 R L^2 escapes this obstruction for the expected reason: its projective specialization is hyperbolic, conjugate to [[3,1],[8,3]], not a full twist. Its opposite operation satisfies Omega^T H Omega^-1=H, as in EKT Theorem 3.2. No classification of all universal partners is asserted here.

## What this says about the rejected anchor

The earlier anchor has input fractions

    (p_T,q_T)=(3+400n,-2+150n), (p_U,q_U)=(-3,1).

One more opposite Omega operation sends these to

    (-7+2400n,-3+850n), (-17,6).

The Hopf-shell Fox determinant p_T p_U-4q_T q_U becomes 191-61200n, never ±1 for integral n. At n=0 its absolute value changes from 1 to 191, despite unchanged Jones polynomial. Thus Jones-preserving EKT moves can change this homology obstruction, but this particular extra move removes the necessary unknot-band anchor. Undoing Omega gives the split union of J and U, with torsion order25. These are two explicit moves, not a new all-orbit classification.

Together with the universal obstruction, the remaining C1 realization problem is specific: a marked double-turnback link must admit two compatible closure-level EKT descriptions, one for each identity d B10=B11=d B01, while restoring both bands gives an actual unknot. Applying a relative equality outside both marked sites preserves all four corner brackets and cannot repair the known nonzero defect. A move through a band needs a fresh geometric certificate; the closed EKT identity does not supply it. No such marked adapter has been constructed in this pass.

## Sources and review

- Eliahou, Kauffman, Thistlethwaite, *Infinite families of links with trivial Jones polynomial*, Topology42 (2003),155–169, Proposition2.1', matrices preceding Proposition3.1, and Theorem3.2. Author copy: https://homepages.math.uic.edu/~kauffman/ekt.pdf ; local text work/attack/ekt.txt.
- Existing marked anchor and the band-filling torsion obstruction: c1_nonunit_turnback.md, c1_nonunit_turnback_anchor.json, and work/ekt_homology_notes.md.
- Algebra audit: independent derivation of G, S, and the specialization proof by /root/algebra_audit. A separate audit by /root/satellite_gate checked the framing-unit argument and gave an alternative proof using the common commutant of S^2 and Omega. No parameter or word scan was used.

The ongoing user goal was cleared during this pass. Only the result already established has been recorded; no further candidate generation is assigned.
