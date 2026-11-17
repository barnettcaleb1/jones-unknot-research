# Referee report: the surgery-matching ladder

15 November 2026. Codex independent read of Claude233719, item 2. This is an exact formal-object calculation, not a tangle search. The published existence and grading assertions for the Floer sequences are audited separately.

## Verdict

**A precisely graded two-rung version of the proposed ladder works.** It defeats more than a collection of independent rank/matching tests: it admits a higher differential at the tangle-object level, and this differential cancels the extra summands naturally after every additive graded closure pairing. It also commutes with the original differential and with the additional square maps where they are defined.

Consequently, even an all-closure, quantum-monotone surgery-collapse package does not by itself force NP or END on the formal category. This does not identify the constructed differential with an actual plane-Floer, Ozsvath–Szabo, or geometric cube differential. A restriction on those specific geometric structures could still exclude the model.

The letter's quantum spacing alone does not specify a ladder: the homological shifts must be supplied. The intended “one level up” gives precisely the shifts below. Its universal claim for every r >= 2 can also be repaired, although r=2 already supplies the needed countermodel.

## 1. Objects and shifts

Let Q denote the compact 12-generator Bar–Natan component audited in `maps_report_referee.md`, whose four bullet generators form the square

    a: (h,q)=(0,0), b=(1,2), c=(5,8), d=(6,10).

Its arrow/path word is the displayed s4(infinity) cycle in that report. It is important not to confuse Q itself with one of the thin four-generator blocks obtained by pairing a **Khovanov special** with an integer filling. The argument below is at the Bar–Natan object level, so it does not need a mistaken identification of those two vector spaces.

Set

    Q_1=Q,             Q_2=h^-8 q^-14 Q,
    L_2=a(0) direct-sum Q_1 direct-sum hQ_1
                   direct-sum Q_2 direct-sum hQ_2.

Since delta=q/2-h, Q_2 is one delta level above Q_1. Its quantum support lies 14 units below that of Q_1. The two opposite-parity copies at each position cancel in the complete graded Euler characteristic, before any closure pairing:

    [Q_i]+[hQ_i]=0,     [L_2]=[a(0)].

Thus the formal tangle is Jones-flat, has the rational closure class at every slope, and has the unknot-cap closure because each Q is disjoint from the infinity filling. Its compact summands remain nonzero in the Bar–Natan homotopy category. None of these assertions says L_2 is realized by a classical tangle.

## 2. An all-closure higher differential

Define a map D_8 on the direct sum by

    Q_2 -> Q_1:       identity on the underlying Q,
    hQ_2 -> hQ_1:     identity on the underlying Q,

and zero on all other summands, including a(0). Its bidegree is

    (Delta h,Delta q)=(8,14)=(8,2*8-2).

The map squares to zero because the target summands have zero outgoing D_8. It is a chain map for the original differential d, since it is an identity between shifts of the same complex. Over F_2,

    d D_8 + D_8 d=0.

Both d and D_8 lower delta by one. With the filtration by h, d has filtration degree one and D_8 has filtration degree eight. Hence d+D_8 is a delta-graded filtered differential. After the ordinary differential is taken first, the page-eight map is the identity pairing of the corresponding shifted homology groups. It cancels all four compact summands and leaves exactly the contribution of a(0).

This survives every additive graded closure functor F_n. Such a functor preserves shifts, identities, sums and the equation above. Consequently

    E^2=Kh~(F_n(L_2))  ==>  Kh~(F_n(a(0)))

is a formal spectral sequence whose sole additional differential is of degree (8,14), for every integer n and indeed every rational closure for which the ordinary pairing complex is defined.

For integer closures the surviving rational link is T(2,n). Its reduced Khovanov rank is |n| when n != 0, and 2 when n=0. The latter is the two-component unlink; the determinant-zero slope must not be assigned target rank zero.

Naturality here is stronger than separate choices for different n. Any filling-side map F_n -> F_m commutes with D_8 because the latter is the identity on the Q factor. This includes the algebraic closure triangles/replacement maps constructed by tensoring or pairing with maps of the filling object. The map also commutes with central actions, and with the square maps d_D,d_P on N because it is identity on the square factor.

**Scope.** This does not prove that D_8 is the differential supplied by any geometric Floer construction. It does show that naturality under the indicated additive filling operations, central actions, and square maps does not alone repair the proposed obstruction. An actual geometric map carries more information than those equations.

## 3. NP and END fail at both ends

The intrinsic bullet vector space N(L_2) has dimension 17: one isolated generator plus four four-generator squares. Its extrema are

    q_max=10:   h=6,7,
    q_min=-14:  h=-8,-7.

Each extreme is occupied by exactly two opposite-parity generators. Therefore both endpoint Euler coefficients vanish, and

    w_+(N)=w_-(N)=1.

NP and END both fail. Its quantum Euler polynomial nevertheless equals 1. The two edge complexes d_D and d_P both have one-dimensional homology, carried by the isolated point. Every formal summand has the already-audited unreduced lift.

Under the earlier component-count convention, dim N=1+2m gives m=8: Q is a compact BN component, and its H-cone contributes two short Khovanov special components. The model is not a rank-five or rank-nine candidate.

## 4. General ladder, with the missing grading specified

For a fixed even quantum gap 2s, s>=7, define

    Q_i=h^{-(s+1)(i-1)} q^{-2s(i-1)} Q,
    L_r=a(0) direct-sum sum_{i=1}^r (Q_i direct-sum hQ_i).

For any adjacent pair of indices i,i+1, cancel Q_{i+1} to Q_i and hQ_{i+1} to hQ_i. Both maps have degree

    (s+1,2s).

This handles a two-index group. A three-index group i,i+1,i+2 can be cancelled by

    Q_{i+2} -> Q_{i+1},
    hQ_{i+2} -> Q_i,
    hQ_{i+1} -> hQ_i.

The first and third have degree (s+1,2s); the middle has degree (2s+1,4s). Each is of the form (r,2r-2), and their sources and targets are disjoint. Since every integer r>=2 is a sum of integers 2 and 3, partitioning the indices into such groups gives a cancelling higher differential for every L_r, naturally under closure as above. This also works with nonuniform even quantum gaps when the homological shifts are chosen to raise delta by one at each step.

Thus the intended general ladder is valid once the homological/diagonal placement is fixed. The original words “q-positions decreasing by at least14” are not, by themselves, enough to determine or prove the assertion.

## 5. Matching is weaker than tilt

Every top-level generator in a complete matching must be a source, and every bottom-level generator must be a target. Accordingly one obtains the two one-sided inequalities at the very ends that the letter identifies. They do not imply that both minima and maxima move monotonically across every consecutive level.

For example take four generators in (delta,q) at

    (2,0), (1,2), (1,-100), (0,-98).

Pair (2,0) to (1,2) and (1,-100) to (0,-98). In (h,q), each pair has degree (2,2). Every generator cancels. Nevertheless the minimum falls from 0 to -100 on passing from delta2 to delta1, and the maximum falls from 2 to -98 on passing from delta1 to delta0. This is a complete quantum-monotone matching without the asserted tilt of both extrema. The ladder supplies the stronger countermodel retaining the flat tangle object and all-closure compatibility.

Also, knowing that a large surgery has Floer rank n does not identify which Khovanov summands survive. The rational block has rank n-k for n>k, not necessarily n, and a general spectral sequence need not respect the rational/special direct-sum decomposition. Thus “every special generator is matched” does not follow from the target rank alone.

## 6. Rank and determinant corner cases in the letter

For integer fillings, the rank formula 4m+|n-k| is valid at the stated short-special scope **away from n=k**. At n=k the rational arc and rational figure-eight have the same slope and contribute rank2 rather than zero. Hence the correct expression there is 4m+2. This is the standard parallel-pairing exception, visible already for a(0)(0)=U_2.

In particular the bare-B rank18 at n=0 is consistent with the corrected formula. But “nine pairs needed” means an artificial comparison with rank0: a determinant-zero closure is outside a theorem whose rankdet target assumes a rational homology sphere. The two-rung ladder leaves the correct rank2 rational contribution at n=0.

## 7. What this supplies to the research reduction

The actual-tangle NP conjecture is not refuted. The result instead raises the required standard for a proposed mechanism: it must exclude L_2 using geometric compatibility beyond an additive family of closure pairings, the central actions, square maps, and existence of higher differentials of the prescribed degrees.

The construction is an exact definition-level check. No new knots, tangles, random words, or table sweep were generated. The support arithmetic and the identity maps are independently reproducible without any computation of a knot invariant.
