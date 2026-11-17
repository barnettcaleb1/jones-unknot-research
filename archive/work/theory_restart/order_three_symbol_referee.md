# Principal symbols and the actual commutator-depth family

Codex `order_three_symbol`; 16 November 2026. Bounded independent read for Claude212613. No scan. The fixed W3 check below supplements, rather than supplies, the all-r proof.

## 1. Crossing and chord operators must be distinguished

Let P=B22(0) be the root super flip and C=((B22-B22^-1)/h)|0. The local certificate gives

    PC=CP,
    char(C)=(lambda+2)^8(lambda+4),
    char(PC)=(lambda-2)^5(lambda+2)^3(lambda+4),
    C=PC-2I+2P.

A singular crossing replacement has the strand permutation of a crossing. A straight chord insertion is therefore PC (or CP, the same here). The osp comparison should either use this straight operator or explicitly retain the correction by I and P. This distinction is not an obstruction: the exact identity above shows that the two comparisons modulo I,P are equivalent. The separate osp referee supplies the explicit Casimir comparison.

Preferred framing also matters at the symbol level. On a fixed marked cube the first raw coefficient f1 is affine; distributing exp(-h f1) among marked balls subtracts the appropriate scalar multiple of the root crossing at each site. Thus a raw C matrix is not automatically the preferred principal tensor. Its off-diagonal terms, including C(w1w1)=-2w0w2+2w2w0, survive this scalar correction. The all-on-axis correction has already been computed exactly as3(T0-I).

## 2. What an order-three comparison could establish

M3 is primitive under compatible equivariant connected sum, because J multiplies and M1=0. Its order is at most3 by FT. The same holds for ordinary v3 restricted to equivariant crossing moves: expanding a paired crossing difference gives terms with at least one ordinary difference at that marked site, so four equivariant differences kill an ordinary order3 invariant. Hence

    I3=(M3/36-7v3)/5

is a rational-valued primitive invariant of equivariant order at most3.

A match of principal order3 weights with a proposed geometric invariant proves only that their difference has order at most2. It does not identify the invariant without controlling that lower-order residual. Likewise, proving the mod5 relation on order3 symbols alone does not establish the integral congruence on all knots; lower-order data and base components still have to be fixed. The published figure-eight pair supplies useful value calibrations but not a spanning theorem for the equivariant degree<=3 quotient.

The current Claude identification report is a skeleton. No independent constituent-knot or eta identification is yet available, and none is asserted here.

## 3. Independent referee of an actual unbounded-depth construction

The nonvanishing referee proposes

    X=[[1,1-t^4],[0,-t]],
    Y=[[1,0],[t^-3,t^-3]],
    W0=Y^2,  Wr=[X,W_(r-1)] for r>=1,
    F_r=e1^T rho(Wr)e1.

This construction passes the following independent checks.

### 3.1 Leading term for every r

Set t=-exp(h). Then

    X=I+hA+O(h^2),      A=[[0,-4],[0,1]],
    Y^2=I+hB+O(h^2),    B=[[0,0],[-3,-6]].

For a group commutator [g,k]=gkg^-1k^-1, the standard multiplication identity gives

    [I+hA+O(h^2), I+h^r C+O(h^(r+1))]
       =I+h^(r+1)[A,C]+O(h^(r+2)).

Induction therefore gives

    rho(Wr)=I+h^(r+1) ad_A^r(B)+O(h^(r+2)).

The two exact matrices are

    C1=[A,B]=[[12,24],[-3,-12]],
    C2=[A,C1]=[[12,72],[-3,-12]],
    [A,C2]=C1.

Consequently the (1,1) coefficient of ad_A^r(B) is12 for every r>=1. Thus

    F_r=1+12h^(r+1)+O(h^(r+2)).

There is no vanishing-leading-term loophole in the commutator induction.

### 3.2 Preferred framing is already correct

The banked TH-2BR all-word skein theorem identifies the preferred J with F_r up to a signed Laurent monomial. Since F_r(0)=1 and its linear coefficient is0 for r>=1, the unique monomial enforcing J(-1)=1 and J'(-1)=0 is1. Therefore J_r=F_r exactly in this marking, not merely to leading order.

It follows that

    M_k(K_r,h_r)=0 for1<=k<=r,
    M_(r+1)(K_r,h_r)=12(r+1)! !=0.

For r>=2, the second-moment identity gives a2(K_r)=0.

### 3.3 These are actual strong inversions

TH-2BR is an all-word theorem for the mixed braid on one distinguished axis strand and the two legs of a single arc. The axis is straight (closed at infinity to an unknot); the lower cup joins the two arc legs; the upper ends attach to the two theta vertices. X exchanges only the two arc legs, while Y is a full mixed twist and preserves strand type. Arbitrary words and inverses therefore preserve the one-axis/one-arc topology. There is no added closed colored component.

The double cover branched over the axis is S3. The preimage of the connected arc joining two distinct points of the axis is a knot, invariant under the deck involution with two fixed points. Thus every Wr gives an actual strongly invertible knot. In half-diagram notation one reverses matrix-composition order and substitutes X->x1, X^-1->y1, Y->y0, Y^-1->x0 between s.l1 and u2.

Nonconstant J_r proves K_r is nontrivial using the easy direction of the quotient-tangle theorem: an unknot strong inversion has a rational quotient and preferred J=1. No use of Lemma Q's difficult converse is made. Equivalently this is the already banked standard two-bridge realization of mixed words.

### 3.4 Fixed calibration

I independently evaluated only r=3, as a marked construction/calibration. Its30-letter matrix word gives the actual halfword

    s.l1.y1.y1.x0.x0.x1.y0.y0.x1.x0.x0.y1.y0.y0.x1.y1.y1.x0.x0.x1.y0.y0.y1.x0.x0.y1.y0.y0.x1.x1.x1.u2.

The direct quotient bracket gives moments [M0,...,M4]=[1,0,0,0,288], as required by12*4!. The ordinary bracket of the full symmetric covering-knot diagram gives determinant217345, a2=0 and v3=0. This fixed test is consistent with the proposed mod5 relation but proves no general congruence. The all-r theorem above rests on the written matrix expansion and marked topology, not this check.

## 4. Consequence for the nonvanishing discussion

There is now an actual equivariant statement stronger and more relevant than an appeal to ordinary finite-type invisibility. For every N, choose r>=max(2,N). The resulting nontrivial strongly invertible knot lies in the a2=0 core and has M1=...=MN=0, although M_(r+1) is nonzero. Thus there can be no universal finite moment cutoff for this particular J tower, even inside the already detected two-bridge class.

This does not prevent a bound depending on diagram or word complexity, and it does not produce a flat tangle. It does show that increasing a fixed finite list of moment gates cannot solve Lemma Q. A nonvanishing argument must see the complete series, or relate its first nonzero term to complexity/topology by an additional theorem.
