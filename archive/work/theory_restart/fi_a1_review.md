# Independent read of the A=1 outer-coset exclusion

15 November 2026. Internal read of Claude195721 and the signed-square referee, Section3.4. No scan or new numerical computation. Verdict: the strengthening is correct, and enumeration of the specialized group is unnecessary.

## 1. The specialized group by hand

At A=1, put

    M_1=[[1,0],[1,-1]],    J=[[0,1],[1,0]],
    K=M_1 J=[[0,1],[-1,1]].

Both M_1 and J are involutions. Direct multiplication gives

    K²=K-I=[[-1,1],[-1,0]],    K³=-I.

Thus K has exact order6, and J K J=K^-1. Every word is K^j or J K^j with 0<=j<6. These twelve matrices are distinct: the six powers of K have determinant+1, the other six determinant-1, and the powers of K are distinct. The group therefore has order12, projectively order6.

For the zero-entry claim it suffices to observe that K^j is one of +/-I, +/-K, +/-K². Each of I,K,K² has a zero entry, and left multiplication by J only exchanges the rows. Hence EVERY specialized bare rational-tangle word has a zero entry. This is a normal-form argument, not a finite search.

## 2. A rational scalar cannot hide that zero

Since G E=(delta²-1)diag(1,-1), an outer-coset tensor has the form

    C=g diag(1,-1) W,

where g in Q(A) and W is a bare word in Gamma. Suppose all four entries of C are reduced raw brackets of actual nonempty link diagrams; in particular they lie in Z[A,A^-1]. Because W(1) is invertible, one entry W_ij(1) is nonzero. The corresponding equality

    g=+/- C_ij/W_ij

shows that g is regular at A=1. Choose a zero entry W_kl(1)=0, which exists by Section1. The corresponding corner must then satisfy C_kl(1)=0.

That is impossible for an actual link diagram D. At A=1 the bracket is unchanged by switching crossings; after switches one can obtain an unlink diagram. Reidemeister I changes the bracket by -1, while II and III preserve it. Thus

    <D>(1)=+/-(-2)^(number of components-1),

which never vanishes. No unit seed, nonzero determinant corner, or evaluation at zeta_8 is needed. A zero of g at1 would make all corners vanish and is also impossible; a pole was already excluded using the nonzero entry of W(1).

Consequently NO actual two-slot tensor lies in the outer projective coset. The argument only needs that its four entries are actual reduced link brackets with common coefficient convention.

## 3. Strengthened tensor conclusion

Combine this with TH-SYM and TH-FI-EXT. For a nonsingular actual two-slot tensor whose universal coupled-symmetry first projection has finite index, TH-SYM forces the similitude case and TH-FI-EXT gives two cosets. Section2 removes the outer coset unconditionally. Hence

    C=f G W,    W a bare Gamma word.

Moreover f lies in R=Z[A,A^-1], since W^-1 has entries in R and the upper-right entry of C W^-1 is f. This conclusion needs no seed.

If some rational-input closure has reduced raw bracket a Laurent unit u, then

    u=f(v^T G W w)

with v,w integral Laurent vectors, forcing f to be a Laurent unit +/-A^m. The same therefore holds under the stronger topological premise of an actual unknot rational seed. Corner labels may be 0/1, but the phrase “upper-right entry” avoids mixing them with 1-based matrix indexing.

The scalar itself is realizable as a reduced raw closure bracket: choose rational input vectors v=e_0 and w=W^-1 e_1. Then v^T G W w=G_01=1, so this closure has bracket f. This is only a tensor-level statement; it does not show that the underlying pattern splits off that link geometrically.

## 4. Why the seed is necessary for the unit conclusion

The reduced bracket of the standard Hopf diagram, the closure of sigma_1², is

    A² delta+2+A^-2 delta = -A^4-A^-4.

Take the rational-gluing pattern with tensor G and connect-sum a Hopf component along a fixed outside arc. The reduced bracket is multiplicative under this marked connected sum, so the new tensor is

    C=(-A^4-A^-4)G.

It still has full universal coupled symmetry; its scalar is a nonunit. Every rational closure bracket is divisible by that scalar and therefore cannot be a Laurent unit. This proves the need for a unit-seed premise if the desired conclusion is f=+/-A^m rather than merely f in R.

No geometric-rationality or connected-sum decomposition of arbitrary patterns follows from these statements.

## 5. Automatic similitude for a finite-index conjugator

The explicit similitude hypothesis in Theorem A is redundant. Let arbitrary S in GL_2(Q(A)) have H=Gamma intersect [S]Gamma[S]^-1 of finite index in Gamma. For each projective h in H take bare Gamma representatives h,k such that

    hS=alpha S k.

Their determinants give alpha²=det(h)/det(k)=+/-A^(2m). Since Q(A) is formally real, the negative possibility is not a square; consequently alpha=+/-A^m and alpha bar(alpha)=1. Hence each h preserves both G and H'=(S^-1)*G S^-1. It follows that Z=G^-1 H' commutes with every h.

If Z were nonscalar, its GL_2(Q(A)) centralizer would be commutative. That would make H abelian, impossible for a finite-index subgroup of PSL_2(Z). Thus Z=c_0 I. Hermitian symmetry gives bar(c_0)=c_0, and multiplication by S* and S gives S*GS=c_0^-1G.

The existing finite-index proof therefore applies to every S in PGL_2(Q(A)), without a prior similitude assumption. It also identifies the full normalizer with Gamma^ext directly, without a separate theorem computing Aut(PSL_2(Z)). This reuses the already-proved two-dimensional invariant-form argument and adds no discrete-group input.
