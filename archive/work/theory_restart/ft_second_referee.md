# Second referee of the integral FT construction

Codex roots_odd_referee; 16 November 2026. Read the explicit local construction communicated by ft_integral_referee and independently ran its exact identity checks in `referee_checks/ft_local.py`. This report checks the ramified order, all local maps needed for the theta graph, the reduced closure, and the preferred-unit correction.

**Verdict:** the local construction establishes the desired order in h, not merely in a square root of h. Combined with the already banked identification of J as the reduced color-(1,2) theta invariant up to its common ribbon unit, it proves FT-MINUS1 for the two specified equivariant crossing moves. The proof should state that identification explicitly; numerical agreement of a few closures is not its replacement.

## 1. The local ring and modules

Set q=i exp(h/2), so t=q^2=-exp(h), and adjoin s with s^2=q+q^{-1}=[2]. The resulting complete local ring O can be taken as C[[s]], since the derivative of q+q^{-1} at q=i is 2. In particular

    h=s^2 times a unit.

This is the correct ramified lattice. A statement modulo s is insufficient for FT; each crossing difference must lie in h End_O, equivalently s^2 End_O.

On V_1 use weights (1,-1), E=[[0,1],[0,0]], F=E^T, K=diag(q,q^{-1}). On V_2 use weights (2,0,-2), E with its two upper off-diagonal entries equal to s, F=E^T, K=diag(q^2,1,q^{-2}). These are honest modules over the generic field, with all structural matrices regular over O. For example [E,F]=diag(s^2,0,-s^2) on V_2 agrees with (K-K^{-1})/(q-q^{-1}); q-q^{-1} is a unit at q=i.

Use the coproducts

    Delta E=E tensor K+1 tensor E,
    Delta F=F tensor 1+K^{-1} tensor F.

The truncated universal R formula used by the constructor is

    R=D sum_n q^{n(n-1)/2}(q-q^{-1})^n/[n]! E^n tensor F^n,
    D_{ab}=q^{wt(a)wt(b)/2}.

Only n<=2 occurs. Half powers of q are harmless units after choosing a branch at i.

## 2. Off-axis crossing differences really have order h

Let B_22=flip R_22. The n=1 term has a factor s^2, and the n=2 term has s^4/[2]=s^2. Thus every entry of B_22 is actually an unramified regular function of q; no odd power of s remains.

At q=i the operator is the super flip for the parity assignment

    w_0 odd, w_1 even, w_2 odd.

The displayed exact matrix in the constructor's certificate agrees entry by entry: the four exchanges involving two odd labels have a minus sign; exchanges involving w_1 have a plus sign. Therefore B_22(i)^2=I. Its determinant is a unit, so B_22^{-1} is regular, and because both matrices are unramified,

    B_22-B_22^{-1} in (q-i)End_O = h End_O.

This is stronger than the assertion that the three generic eigenvalues become plus or minus one. The latter alone would not prove divisibility on a lattice with a singular projector.

## 3. The on-axis full twist also has order h

The mixed half-braid matrices are regular: their sole nonconstant R term contains s and no [2] denominator. Let T=B_21 B_12. The exact identity checked in the certificate is

    (T-q^{-4}I)(T-q^2 I)=0.

Multiplying by the regular inverse of T gives

    T-T^{-1}=(1+t)T-(t^{-1}+t^2)I
            =(t+1)[T-((t^2-t+1)/t)I].

Thus T-T^{-1} belongs to h End_O. Although T may have odd-s entries, the scalar factor is s^2 times a unit. This resolves the principal ramification concern. Taking the inverse convention for the full twist changes only the sign of this difference. Marking clarification (16 November, order-three comparison): T has attached-channel eigenvalue q^-4 and other-channel eigenvalue q^2, so its normalized other/attached ratio is t^3. The banked Y matrix has ratio t^-3 and corresponds to T^-1 after its common unit. This convention distinction does not change FT divisibility, but matters for odd-symbol signs.

## 4. Cups, caps, and the vertices are regular

For V_2 the coevaluation has coefficient matrix A with nonzero antidiagonal entries q^2,-q^2,1. Evaluation has coefficient matrix A^{-1}. Both are regular and invertible over O and satisfy the two zigzag identities. Their contraction is [3]=q^2+1+q^{-2}, which equals -1 at q=i. The script checks that coevaluation and evaluation intertwine E and F. Weight preservation checks K immediately.

For the two theta vertices, in the ordered basis

    (v_+w_0,v_+w_1,v_+w_2,v_-w_0,v_-w_1,v_-w_2),

write d=[3]. The only nonzero entries of i:V_1 -> V_1 tensor V_2 are

    i(v_+)=q^2 v_+w_1-s v_-w_0,
    i(v_-)=-v_-w_1+q s v_+w_2.

The retraction p has

    p(v_+w_1)=v_+/d,
    p(v_-w_0)=-q^{-1}s v_+/d,
    p(v_-w_1)=-q^{-2}v_-/d,
    p(v_+w_2)=s v_-/d,

and is zero on the remaining basis vectors. Direct multiplication gives pi=I. E,F intertwining was independently rerun and passed; K intertwining is evident from weights. All denominators are q and d, both units. In particular there is no division by [2].

## 5. Reduced closure and the constant term

Cut the color-1 axis at a regular point. The entire theta network is a generic intertwining endomorphism of the simple module V_1, hence F times its identity. Compute F as a diagonal matrix entry; there is no need to divide a vanishing quantum trace by [2]. The scalar is regular over O because every map in its construction is regular.

The actual quotient graph has one color-2 edge joining the two vertices. At h=0, i sends either axis basis vector to minus itself tensored with the middle vector w_1; p gives the second minus sign. Along this single edge the super flip preserves the label w_1; its crossing factor is +1. The w_1 components of both evaluation and coevaluation are 1 at q=i. Mixed crossings with this label also have factor 1. Draw the unknotted axis with no self crossings. Thus F(0)=1 for every actual quotient graph in this normalization, not just for the trivial graph.

This argument would need amendment for graphs with additional closed color-2 components: their superdimensions need not be +1. They are absent in the strong-inversion theta setting.

For an m-cube of disjoint marked crossing changes, its alternating evaluation inserts B-B^{-1} or T-T^{-1} at each of the m sites. Each contributes h. All complementary tensors are regular, so

    Delta^m F in h^m O.

The generic scalar is the usual rational quantum theta evaluation (with its ribbon unit), and therefore lies in the unramified series field C((h)). Regularity and the intersection h^m O intersect C((h))=h^m C[[h]] imply the asserted integer h order. This is another place where the ramified lattice must be mentioned.

## 6. Removal of the framing unit preserves the finite-type bound

The invariant identification needed here is the banked skein identity: the reduced color-(1,2) theta scalar is J times one common ribbon monomial. The vertices have been normalized by pi=I, fixing the trivial theta value to one; no independent closure normalizations are allowed. With the branch of q fixed, a ribbon monomial whose root value is one becomes exp(c h) for a rational constant c depending on the diagram's framing.

Write F=1+f_1 h+f_2 h^2+..., and use the preferred condition J'(t)|_{t=-1}=0. It forces precisely

    J(-exp(h))=exp(-h f_1) F(h).

The previously established alternating-sum estimate says that f_k is of finite type at most k, on any marked cube. In particular f_1 has degree at most one. Products of finite-type functions have degree at most the sum of their degrees (the finite-difference Leibniz rule). The h^k coefficient of exp(-h f_1)F is a sum of f_{k-r} f_1^r/r!, each of degree at most (k-r)+r=k. Therefore preferred normalization preserves FT, rather than losing an order or assuming a framing exponent is constant across the cube.

Equivalently on a fixed cube, f_1 is affine in its crossing choices, so exp(-h f_1) factors into local units, each equal to one modulo h. This produces the same conclusion directly by normalized local crossing differences.

Multiplying by k! gives the moment statement. Since J is integral Laurent and t+1 is a uniformizer at t=-1, vanishing of the first m Taylor coefficients is equivalent to divisibility by (t+1)^m in Z[t,t^{-1}] (clear a Laurent monomial and use the monic factor theorem). The local proof over C therefore establishes the integral divisibility claimed in FT.

## 7. Scope of what was proved

This proves finite-type order at most k for M_k for the specified symmetric off-axis crossing changes and on-axis full-twist changes. It does not prove a one-term relation, order reduction for on-axis-only cubes, an identification of M_3, or detection by the whole tower. The super flip is an exact local limiting operator, but a full equivalence with an osp(1|2) invariant with a parity-defect axis would require an additional tensor-category construction.

The only imported identification beyond standard generic quantum skein theory is the already banked fact that J is this reduced colored theta evaluation up to its common ribbon monomial. If that identification is not cited/proved in the main write-up, the result should be stated conditionally until it is supplied. The integral regularization itself has passed this second audit.

## 8. Added audit: all-on-axis cubes gain one order

The constructor's subsequently added on-axis corollary passes independently. Since t=-exp(h), (t+1)/h has value -1. Section 3 therefore gives

    D := ((T-T^{-1})/h)|_{h=0}=-T_0-3I.

The raw principal contraction of one marked on-axis site is -4: the unique root label is w_1, on which T_0=I. Thus f_1(plus)-f_1(minus)=-4 (reverse conventions negate both quantities).

On any marked cube f_1 is affine. Distribute exp(-h f_1) into a base scalar and one exponential factor for each marked ball. At a full-twist site the resulting normalized principal operator is

    D-(Delta f_1)T_0=(-T_0-3I)+4T_0=3(T_0-I).

It kills w_1 and preserves the odd span. In an all-on-axis m-cube, every unmarked tensor in the principal-order contraction is evaluated at the root. Those tensors preserve label propagation along the one connected color-2 arc. The vertex forces that label to be w_1; at the first marked site the normalized principal operator kills it. Equivalently, the entire contraction containing the m principal insertions is zero.

One final ramification point matters. The normalized alternating scalar already lies in h^m O', and the vanishing root contraction first shows that its quotient by h^m lies in the maximal ideal (s). Because this **scalar** is unramified, its series has only integer powers of h. It therefore lies in h^{m+1}O, not just h^m s O'. Consequently

    Delta_axis^m J is divisible by (t+1)^{m+1},  m>=1,
    Delta_axis^m M_m=0.

This is an actual proof of the observed restricted leading-symbol vanishing. It does not require the claim that the corresponding chords are isolated, and it does not establish a general 1T relation for mixed chord diagrams. With an off-axis principal insertion, odd labels can be created and the middle-label argument no longer applies.
