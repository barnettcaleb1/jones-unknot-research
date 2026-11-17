# Bare B: one exact closure and the monotone-matching obstruction

15 November 2026. Codex definition-level referee check for Claude234649. Coefficients F_2 for the finite algebra. MATCH is pinned in surgery_collapse_sources_referee.md: Daemi's geometric sequence is over a characteristic-two Novikov field, with E2 the scalar extension of reduced Kh(mirror;F_2). It therefore imposes exactly the matching constraint on F_2 graded dimensions used here. No geometric descent to F_2 is required. The root checked this input and the finite certificate before banking the exclusion.

## 1. The decisive closure really has the claimed support

Let Q be the 12-generator compact Bar–Natan component used in the earlier B model, normalized so its bullet square has generators

    (h,q)=(0,0),(1,2),(5,8),(6,10).

The full idempotent list is

    b,c,c,c,c,b,b,c,c,c,c,b,

and its differential arrows, using 1-based indices, are

    1--S->2--D->3--S²->4--D->5--S->6--D->7,
    1--D->12--S->11--D->10--S²->9--D->8--S->7.

Take the slope-one filling arc

    X = [c(-1,-2) --S-> b(0,-1)],

and the standard H-cone

    C_1(Q)=Cone(H:h^-1 q^-1 Q -> q Q).

The morphism complex uses the algebra DS=SD=0, deg D=-2, deg S=-1. Direct exact F_2 linear algebra gives

    H Mor(X,C_1(Q)):

    (h,q)       multiplicity
    (0,0)             1
    (1,2)             1
    (2,4)             1
    (3,6)             2
    (4,8)             1
    (5,10)            1
    (6,12)            1.

All eight generators have delta=q/2-h=0. The rational a(0) summand contributes exactly the pawn (0,0). Thus the closure of

    B=a(0) direct-sum Q direct-sum hQ

has the pawn, the eight-point row above on delta0, and its identical-quantum copy on delta-1. Its total rank is 17 and its Jones Euler polynomial is 1.

This calculation does not infer the closure support from N's four-generator square. It pairs the entire 12-generator Q and its H-cone with the actual two-generator filling arc.

The independent script is `referee_checks/bare_b_slope_one.py`. It imports neither Claude's typeD code nor his matching code. It constructs homogeneous morphism bases and computes kernel/image ranks directly over F_2. The homological range is finite from the generator differences. Below the quantum differences only positive-length paths occur and the matrices stabilize under q->q-2 in each parity; two zero tail computations certify that the displayed table is exhaustive. The script also checks the matching certificate below.

## 2. Exactly three generators must survive

Write p=q/2. Both compact rows have multiset

    M={0,1,2,3,3,4,5,6}.

A differential of degree (r,2r-2), r>=2, goes from the upper row at p to the lower row at p'>p. Consider the five upper generators at positions >=3. Their only possible lower targets are the three generators at positions >3, namely4,5,6. At least two of these upper generators survive. The lower generator at position0 has no incoming arrow from the upper row or the pawn at position0, and survives as well.

This lower bound is attained. Label the upper compact generators by their ordered positions, and use the pawn as a second upper position0. Match

    upper0 -> lower1,
    pawn0 -> lower2,
    upper1 -> first lower3,
    upper2 -> second lower3,
    first upper3 -> lower4,
    second upper3 -> lower5,
    upper4 -> lower6.

These seven disjoint pairs all have the allowed degrees. The survivors are the upper5, upper6 and lower0 generators. Hence the minimum possible rank is exactly3, not1.

The same lower bound holds even if the pawn is allowed an arbitrary position and delta level: adding a single vertex to a matching graph raises the matching number by at most one. The compact graph has maximum matching6, so adding the pawn permits at most7 pairs out of17 generators.

Therefore **MATCH excludes bare B as an actual tangle with its specified unknot cap**: its slope-one closure is a determinant-one knot by the decategorified closure identity, yet its bigraded Khovanov support cannot collapse to rank1 by the required degrees. This is a realization obstruction, not a proof of NP. It supersedes the earlier statement that bare B satisfies every then-known formal constraint.

## 3. Exact Hall formula and the larger-n correction

For any finite multiset M of ordered positions, put N=|M| and w=max multiplicity of a position. Between two identical copies of M, with edges x->y exactly when y>x, the maximum matching is

    N-w.

Proof: a tail beginning at a position p has deficiency exactly the multiplicity at p. Conversely a subset whose minimum is p has at most as many elements as that tail and has the same neighbor set, so no larger deficiency occurs. Hall's deficiency formula gives the claim.

Consequently the residual rank of two such rows is2w, and adding one arbitrarily placed pawn leaves at least2w-1 generators. This lower bound is attainable by putting the pawn strictly below every position on the upper row, so the best residual rank is exactly2w-1.

Under the block formula used in `daemi_match.py`, the compact-Q row for slope1/n has generating polynomial

    M_n(z)=(1+z)(1+z²)(1+z³)(1+z+...+z^{n-1}).

Its maximum coefficient is

    w_n=min(n+1,8),

because the first factor product has coefficient list (1,1,1,2,1,1,1), and multiplication by the length-n interval takes consecutive-window sums of that list. Thus, **assuming that asserted closure block formula**, the arbitrary-pawn best residual rank is

    2 min(n+1,8)-1.

It equals2n+1 only for n<=7 and then remains15. It cannot grow indefinitely, because each row has at most eight generators at one quantum position. The n=1 exclusion above is independently certified and does not depend on extending the block formula to every n.

## 4. A genuine strip restriction

The same argument excludes more than one bare pair. Suppose a formal unknot-cap tangle has the form

    a(0) direct-sum sum_i(Q_i direct-sum hQ_i),

where every Q_i is a shift of Q and all Q_i contribute to the **same** delta row in the slope-one closure. Their quantum positions can be arbitrary. The two compact rows are identical multisets M; each translated compact Q row has a position of multiplicity2, so w(M)>=2. With one pawn, at least3 generators remain. MATCH therefore excludes every such single-strip configuration.

This is an explicit, non-tautological restriction on realizable graded configurations. Its scope is the two identical adjacent compact rows, not all configurations with cancelling Euler characteristics.

## 5. The two-rung ladder survives this stronger test

The already-audited model

    L_2=a(0) direct-sum Q direct-sum hQ
                   direct-sum h^-8q^-14Q direct-sum h^-7q^-14Q

occupies three compact delta levels rather than two. Its degree(8,14) identity maps pair the shifted Q copies to the unshifted copies under every additive closure functor. It therefore passes the determinant-one matching test at slope1/n and leaves the correct rational closure at every other slope. Its N still fails END at both quantum extremes.

The new MATCH obstruction thus has genuine force: it excludes bare B and the entire two-row strip class. It does not yet exclude the coherent ladder. A mechanism intended to prove NP or END must use a further geometric restriction, or strengthen the matching constraints in a way the explicit ladder fails.

No knot search or family sweep was performed. The only invariant calculation here is the named slope-one pairing of the fixed formal Q.
