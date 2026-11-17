# G1-PLANAR: prior art and the signed-Tutte identification

Targeted theory/novelty read, 2026-11-03. No enumeration. Main conclusion: the projection equation is genuine classical input, but the proposed weighted-nullity enumerator is the existing signed planar-Tutte state sum in another coordinate system. It is not a new constraint on classical Jones polynomials. A geometric cancellation theorem could still be new; none was supplied by this read.

## 1. What the published projection theorem actually says

[Shtylla–Traldi–Zulli, 0709.2933, Theorem 2](https://arxiv.org/pdf/0709.2933) proves that a double-occurrence word with interlacement matrix B is planar-realizable exactly when B admits a diagonal completion P with P²=P over F2. Its final remark already constructs the projection from the checkerboard splitting of a sphere with one crosscap inserted at every crossing. Thus the topology-to-projection dictionary is in the original source.

The circle-graph hypothesis is indispensable. Their first remark gives a 9-by-9 symmetric idempotent whose off-diagonal graph is not a circle graph. Arbitrary LCD codes or arbitrary symmetric idempotents are strictly more general than planar Gauss diagrams.

[Traldi–Zulli, Topological realizations of ortho-projection graphs](https://sites.lafayette.edu/traldil/files/2010/06/topreals.pdf), Section 3, makes the relation to Jones especially explicit. Its Remark 3.1 recalls that Zulli's trip matrix computes the Jones polynomial and that the trip matrix of an alternating classical diagram is an orthogonal projection (Zulli 2002, with the observation attributed to Stong). The paper distinguishes these knot projections from general surface splittings realizing arbitrary orthoprojections. Shtylla–Zulli's 2006 paper, *An extension of the Jones polynomial of classical knots*, is already devoted to the Jones polynomials of these matrices; see that paper's citation in STZ and Traldi–Zulli.

## 2. Tait cycle and cut spaces explain the projector

For the natural checkerboard choice, one summand is the binary cycle space C(G) of a Tait graph G, and the other is its orthogonal cut space. Indeed, the two checkerboard pieces in the crosscap construction retract onto the black and white Tait graphs; their mod-two edge coordinates give the corresponding cycle spaces. Planar duality identifies one with the other's cut space. Choosing the other color exchanges P and I+P.

For a connected plane graph G, the number of components of its medial link is one plus the dimension of its bicycle space C(G)∩C(G)⊥. This is the standard link-component/bicycle theorem; a primary modern account is [Dasbach–Russell, Equivalence of edge bicolored graphs on surfaces, Sections 3–4](https://www.combinatorics.org/ojs/index.php/eljc/article/download/v25i1p59/pdf/). Thus the knot condition is precisely the LCD condition for this graphic code.

Let H be a reduced binary vertex-edge incidence matrix. The cut projector is

    Q=H^T(HH^T)^(-1)H,

and the cycle projector is P=I+Q. Invertibility of HH^T is equivalent to zero bicycle space. By the matrix-tree theorem it is also equivalent to an odd number of spanning trees. This parity is a condition on the knot SHADOW, before over/under choices.

There is also a useful matrix-class observation, whose following argument is a deduction rather than a separately identified published theorem. If P0 and P are two idempotent completions of the same B, their diagonal difference d satisfies (d_i+d_j)B_ij=0. Hence d is constant on each connected component of the off-diagonal graph. P0 is block diagonal on these components; replacing P0 by P complements the code on selected blocks. Starting from a planar graphic cycle code, this is blockwise matroid duality, which remains planar graphic. Thus the completion choices do not produce an exotic additional LCD class. This observation concerns a matrix realization by some planar graph; it does not identify an isotopy of a fixed marked diagram.

## 3. Exact reduction to the signed planar state sum

Write E for the edge set, S⊆E, and D_S for its diagonal indicator. Suppose im(P)=C(G). The elementary projector identity is

    ker(P+D_S) ≅ C(G)_S ⊕ C(G)⊥_(E\S),

where the subscript denotes vectors supported on the indicated set. To verify it, write a vector uniquely as u+w with u∈im(P), w∈ker(P). The equation P(u+w)=D_S(u+w) says exactly that u is supported on S and w on E\S.

If r is the graphic matroid rank function, then

    dim C(G)_S = |S|-r(S),
    dim C(G)⊥_(E\S) = r(E)-r(S).

Consequently

    nullity(P+D_S)=|S|+r(E)-2r(S).

For connected planar G, this is b(S)-1, where b(S) is the number of boundary circles of a regular neighborhood of the spanning subgraph G[S]. Indeed b(S)=2k(S)-|V(G)|+|S| and r(S)=|V(G)|-k(S).

Therefore the proposed enumerator is exactly

    N_(P,c)(u,v)=sum_(S⊆E) u^|S Δ c| v^(|S|+r(E)-2r(S)).

At u=A^-2, v=delta=-A²-A^-2, multiplying by A^|E| gives

    sum_(S⊆E) A^(|E|-2|S Δ c|) delta^(b(S)-1),

the signed checkerboard Kauffman state sum. The choice of which checkerboard smoothing is called S changes only the corresponding c convention. This is the content of the signed-Tutte formulation, introduced in [Kauffman, A Tutte polynomial for signed graphs (1989)](https://homepages.math.uic.edu/~kauffman/TuttePolySignGraphs.pdf).

In particular, the new code terminology does not strengthen the available polynomial data. Its potential benefit would have to be a new theorem about graphic LCD codes with their planar realizations, not an inference from the idempotent equation alone.

## 4. Cancellation and the first-page decision

For an alternating assignment (uniform checkerboard sign), the familiar Tutte extremal-term argument already gives Jones detection for reduced alternating diagrams. With arbitrary c, the state weights are changed and the signed cancellations are exactly those of the usual nonalternating problem. Positivity of the pre-specialization enumerator does not persist on the Jones curve.

I found no published all-sign cancellation-to-isotopy theorem that settles the monomial case; asserting such a theorem would settle T in its standard signed-Tutte form. Local loop/bridge and signed parallel/series reductions correspond to the established Reidemeister calculus. A new useful statement must identify additional hypotheses forcing one of these actual geometric reductions, and must handle hard unknot diagrams requiring temporary complexity increases.

Recommendation: retain the exact rank/support identity as a convenient lemma, but do not claim the dictionary as a new route advantage. A single genuinely new cancellation block and its geometric lift is still an appropriate bounded target. If the proposed block is only standard signed-Tutte deletion/contraction, the pass has produced no new detection mechanism.
