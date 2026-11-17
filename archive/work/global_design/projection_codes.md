# Projection nullity, Tutte rank, and the complete two-coordinate cancellation

G1-PLANAR theory page, 2026-11-03. Exact algebra below was derived without enumeration. No novelty claim: the resulting invariant is the familiar signed Tutte rank sum. The useful output is the precise scope of the proposed local mechanism and its wheel obstruction.

## 1. A support decomposition of every kernel

Let P be a symmetric idempotent n-by-n matrix over F2, C=im(P), C-perp=ker(P), and k=dim(C). For S contained in E={1,...,n}, let D_S be the coordinate projection onto F2^S. Then there is a canonical direct-sum identity

    ker(P+D_S) = (C intersect F2^S) direct-sum (C-perp intersect F2^(E-S)).       (1)

Proof. If (P+D_S)v=0, put u=Pv=D_Sv and w=(I+P)v=D_(E-S)v. Then u belongs to C and is supported in S; w belongs to C-perp and is supported in E-S; v=u+w. Conversely any such u,w satisfies P(u+w)=u=D_S(u+w). The supports are disjoint, so the sum is direct.

Let G be a full-row-rank generator matrix of C and let M be its column matroid. Put T=E-S. The two summands have dimensions k-r_M(T) and |T|-r_M(T), respectively. Hence

    nullity(P+D_S) = k+|T|-2*r_M(T).                                          (2)

In particular the exponent is exactly matroid corank plus nullity, not an additional invariant of the projection matrix. The entire function S -> nullity(P+D_S) recovers r_M(T), but nothing beyond that rank function.

Because C is nondegenerate for the dot product, GG^t is invertible and

    P = G^t (GG^t)^(-1) G.                                                     (3)

Conversely (3) is the unique orthogonal projection onto any nondegenerate binary code. Cauchy-Binet over F2 gives

    det(GG^t) = sum_(|B|=k) det(G_B)^2 = number_of_bases(M) mod 2.

Thus a binary code admits this projection precisely when its matroid has an odd number of bases. This equivalence is also recorded in [Connections between Linear Complementary Dual Codes, Permanents and Geometry](https://www.mdpi.com/2227-7390/11/12/2774). In the graphic case it is the odd spanning-tree condition. This does not say that an arbitrary LCD code is graphic or planar.

## 2. Jones specialization becomes the signed Tutte rank sum

With c from the G1-PLANAR note, set epsilon_e=1-2c_e, so epsilon_e is +1 or -1. Complementing S to T in the projection enumerator gives the exact bracket expression

    F(M,epsilon) = sum_(T subset E)
        product_(e in T) A^(epsilon_e)
        product_(e notin T) A^(-epsilon_e)
        delta^(k+|T|-2*r_M(T)),     delta=-A^2-A^-2.                            (4)

For a plane Tait graph this is the usual signed-graph state sum; see [Kauffman, A Tutte polynomial for signed graphs](https://homepages.math.uic.edu/~kauffman/TuttePolySignGraphs.pdf). Equation (2) explains why the new projection language collapses exactly to this old object.

Consequences for strategy: P^2=P does organize the local rank changes, but one must not claim that the scalar identity in (4) has acquired extra positive information. The remaining geometric data are the graphic/planar realization and crossing signs, and the Jones specialization is still signed.

## 3. Exact cancellation of an oppositely signed parallel pair

Suppose e,f are a nonloop parallel pair in M and epsilon_e=+1, epsilon_f=-1. Fix any T contained in E-{e,f}; put d=r(T+e)-r(T), either 0 or 1. Parallelism makes the rank increment for e, f, and {e,f} the same d. Relative to the term with neither edge present, the four choices contribute

    1 + (A^2+A^-2)*delta^(1-2d) + delta^(2-2d) = 1.                           (5)

The two middle terms combine with the last because A^2+A^-2=-delta. Apparent negative exponents when d=1 cancel against the outside term's positive delta exponent; the identity is an identity of the original Laurent polynomials.

Deleting e,f does not lower rank when M has an odd number of bases. Otherwise every basis would contain exactly one of e,f, and exchange e<->f would pair all bases, making their number even. Therefore

    F(M,epsilon) = F(M delete {e,f}, epsilon restricted).                     (6)

The same argument works when both columns are zero (two loops). The dual identity removes an oppositely signed series pair by contraction. Equation (4) is unchanged under M -> M* together with epsilon -> -epsilon and T -> E-T, so this dualization is exact.

In matrix terms parallel columns of G are equivalent to equal columns (and rows) of P. Deleting their coordinates leaves a symmetric idempotent matrix: the two equal outer-product contributions to P^2 cancel in characteristic two. Equation (3) gives the same result because deleting two equal columns leaves GG^t unchanged. Series pairs are equal rows of I+P and obey the dual deletion statement on the projector.

If the common diagonal entry on e,f is p, their oriented crossing signs are L_e=c_e+p and L_f=c_f+p. Opposite c implies opposite L, so the writhe normalization also cancels for this pair.

For a plane graph an actually adjacent parallel pair bounds the Reidemeister-II bigon. A nonadjacent parallel pair requires an additional geometric argument (e.g. Whitney flips/Conway mutation to make the bigon empty). The algebra above alone is not that geometric argument.

## 4. Why this is all of the universal two-edge deletion cancellation

At T empty, the pair has one of the following rank patterns: both loops; parallel nonloops; one loop and one nonloop; or two independent nonloops. For opposite edge signs, requiring the sum of the three nonempty choices to vanish identically in A leaves only the first two patterns.

For example, for independent nonloops their sum is

    (A^2+A^-2)*delta^-1 + delta^-2 = -1 + delta^-2,

which is not identically zero. For one nonloop e and one loop f it is

    A^2*delta^-1 + A^-2*delta + 1,

also nonzero; multiplying by delta gives A^2+A^-2+A^-6. The other sign ordering is its A-inverse. Thus outside-state-by-outside-state cancellation down to deletion of both edges is precisely parallel/loop cancellation. Its dual is series/coloop cancellation. This classification does NOT exclude cancellations between different outside states.

There is a related consequence directly from idempotence. If rows e,f of P agree outside {e,f}, with nonzero common outside vector v, write their internal block as [[a,b],[b,d]]. The two equations for the outside part of P^2=P imply (a+d)v=0, hence a=d. Then either a=b (equal full rows: parallel) or a=b+1 (equal rows of I+P: series). If v=0, the diagonal equations of the two-by-two idempotent block force b=0, so both coordinates are isolated loop/coloop coordinates of Reidemeister-I type. Thus a two-coordinate twin block supplies no third kind of projector cancellation.

## 5. Infinite obstruction to forcing these blocks (root's construction, algebra checked)

Let W_m be the wheel with m rim vertices and one hub, m>=4 and 3 not dividing m. Its reduced Laplacian over F2, deleting the hub, is

    I + adjacency(C_m).

Its kernel satisfies x_(i+1)=x_i+x_(i-1). Every nonzero solution has period three, so the cyclic system has only the zero solution when 3 does not divide m. Thus W_m has an odd number of spanning trees and its cut code has an orthogonal projector P.

The graph is simple and 3-edge-connected. Consequently its graphic matroid has no loops, coloops, parallel pairs, or series pairs. Accordingly P has no zero or coordinate-unit row, no pair of equal rows, and I+P has no pair of equal rows. The preceding twin-block lemma then also rules out any non-isolated twin rows of its off-diagonal graph.

The plane medial shadow has one component in these cases (equivalently, the familiar three-strand weaving shadow has component count gcd(3,m)). Give this shadow a descending crossing assignment: it is an actual unknot diagram. It therefore has Jones polynomial 1 while none of the one- or two-coordinate blocks above exists. Whitney flips preserve the cycle matroid and cannot create loops, coloops, parallel pairs, or series pairs.

This refutes the proposed implication “Jones unit forces one of these local projection blocks,” even allowing Whitney flips first. It does NOT refute a mechanism with higher-coordinate moves, Reidemeister III, temporary stabilization, or another genuinely geometric transformation. Those would need separate forcing and termination arguments.

## Verdict

The support decomposition and the complete local cancellation are useful exact results, but the cancellation is the standard signed series/parallel move, and wheels show that it cannot be forced by V=1. The proposed low-block version of G1-PLANAR should therefore be stopped, not escalated to a claim of new noncancellation. A revived version must name a larger geometric move that acts on the wheel unknot diagrams and a reason Jones equality forces such a move.
