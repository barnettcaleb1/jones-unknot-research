# Two-slot pattern symmetries: a Hermitian dichotomy

15 November 2026. Holder: Codex. Direct algebraic theorem with an independent internal derivation; novelty unassessed. This extends the earlier EKT-specific centralizer calculation. It does not assert tangle rationality or Jones detection.

## 1. The group and the form

Put R=Z[A,A^{-1}], K=Q(A), bar(A)=A^{-1}, and δ=−A²−A^{-2}. Work with the reduced closure form

    G = [[δ,1],[1,δ]].

Multiplying G by δ gives the absolute closure Gram matrix; none of the conclusions changes. For a matrix B, write B*=bar(B)^T. The two rational-tangle operations

    M = [[A,0],[A^{-1},−A^{-3}]],    J = [[0,1],[1,0]]

preserve G: B*GB=G. Let Γ be their matrix group, allowing harmless bracket-framing scalars of norm one, and let Γ_proj denote its projective image. Also bar(Γ)=Γ, since bar(M)=M^{-1} and bar(J)=J.

The projective group is PSL(2,Z). Indeed J²=I and (A J M)³=−I give a homomorphism from C₂*C₃ onto Γ_proj. At A₀=exp(πi/4), conjugation by diag(1,i), with scalar normalizations, takes J and M to the standard modular involution and the lower unipotent generator. Thus specialization recovers the faithful standard C₂*C₃ action and proves that the generic representation has no extra relations. All matrices used here are Laurent and invertible at A₀.

Every abelian subgroup of Γ_proj is cyclic. One proof uses its standard discrete action on the hyperbolic plane: the centralizer of a nonidentity elliptic is a rotation group, and the centralizer of a hyperbolic or parabolic is a one-parameter group. Its intersection with a discrete group is cyclic (finite in the elliptic case).

## 2. A universal pattern symmetry

A two-slot planar pattern has a bilinear bracket

    B_C(v,w)=v^T Cw,       C∈Mat₂(R).

The following result needs only this tensor, not planar realization. Assume det C≠0 in K. A universal symmetry is a pair P,Q∈Γ and a norm-one scalar u for which

    P^T C Q = u C.                                      (1)

It acts on every pair of input bracket vectors. It is much stronger than equality on one chosen pair of tangles.

Set

    S=G^{-1}C,
    H_C=(S^{-1})* G S^{-1},
    Z_C=G^{-1}H_C.                                      (2)

These are explicit 2-by-2 rational-function matrices. Rescaling C changes Z_C by a scalar, so whether Z_C is scalar is independent of a global pattern framing or nonzero scalar normalization.

### Theorem

If Z_C is not scalar, the projective group of universal symmetries (1) is cyclic.

If Z_C is scalar, S is a Hermitian similitude. The universal symmetry group is instead the intersection of two conjugate projective rational-tangle groups, specified below. In particular, a pattern with two noncommuting universal symmetries must satisfy the exact identity

    S* G S = cG                                         (3)

for some c∈K with bar(c)=c.

### Proof

G is real symmetric for the coefficient involution. From P*GP=G and its conjugate,

    P^{-T}=G bar(P) G^{-1}.

Equation (1) therefore forces

    Q=u S^{-1}bar(P)S.                                  (4)

The norm-one scalar disappears from Q*GQ. Thus Q is unitary exactly when

    bar(P)* H_C bar(P)=H_C.

But bar(P) also preserves G. Dividing these two invariance relations gives

    bar(P)^{-1} Z_C bar(P)=Z_C.                          (5)

The centralizer of any nonscalar 2-by-2 matrix over a field is the commutative algebra K[Z_C]. To see this, choose a vector v for which v,Z_Cv is a basis; a commuting map is determined by its image of v and is a polynomial of degree at most one in Z_C. Consequently all allowed P commute, and their projective image is an abelian subgroup of PSL(2,Z), hence cyclic.

Equation (4) determines [Q] from [P]. The first projection on the projective symmetry group is therefore injective, establishing the statement for the full pair group rather than only its projection.

If Z_C=c₀I, then H_C=c₀G and multiplying by S* and S gives S*GS=c₀^{-1}G. Conversely this similarity identity makes (5) automatic. What remains is actual membership of the forced Q in Γ. After conjugating coefficients, the first projection is exactly

    Γ_proj ∩ [bar(S)] Γ_proj [bar(S)]^{-1},              (6)

or, equivalently before conjugating coefficients,

    Γ_proj ∩ [S] Γ_proj [S]^{-1}

in the variable [bar(P)]. Membership suffices: choose a unitary Γ representative Q of the forced projective class. Its scalar ratio to S^{-1}bar(P)S has norm one because both matrices are unitary. This is an intersection, not automatically a finite-index intersection. Calling every S in (3) a commensurator would require an additional argument. ∎

## 3. Degenerate tensors

For rank-one C=a b^T, universal preservation forces P^T[a]=[a] and Q^T[b]=[b]. The projective stabilizer of either line in Γ is cyclic, so the pair group is a product of two cyclic groups under the present definition allowing any norm-one scalar u. Indeed P^T and Q^T preserve the dual form G^{-1}; the eigenvalue of a nondegenerate invariant line has norm one, so the product of the two eigenvalues supplies u. If one restricts u further, for example to u=1, an additional relation between these eigenvalues remains.

For completeness, line stabilizers are abelian without any assumption about a real specialization. Every K-line has nonzero Hermitian norm for G (and for the dual form G^{-1}): specialize at a generic unit-circle point on an open arc with |δ|>1, where the form is definite. A nonzero rational-function vector cannot vanish or have a pole throughout that arc. A unitary map stabilizing this nondegenerate line also preserves its orthogonal complement; such maps are simultaneously diagonal and commute. The cyclic conclusion follows from the projective modular group.

The zero tensor is a separate algebraic case with unrestricted stabilizer; no claim about its realization by a planar tangle pattern is needed.

## 4. Exact calibrations

1. Rational gluing: C=G gives S=I and Z_C=I. More generally C=GR with R∈Γ gives Z_C=I. These are examples of the exceptional similarity case, not a classification of it.

2. EKT: in the archived Hopf-shell conventions,

       C = [[h,δ²],[δ²,δ]],
       h=−A¹⁴−A⁶−2A²−2A^{-2}−A^{-6}−A^{-14}.

   C is symmetric and fixed by bar, hence S=G^{-1}C is G-self-adjoint and Z_C=S^{-2}. The previous calculation gives

       S = [[δ²(δ²−3)², δ],
            [−δ(δ²−2)(δ²−4), 0]].

   S is nonscalar with nonzero trace. Cayley–Hamilton shows that S², and therefore S^{-2}, is nonscalar. Every universal EKT symmetry thus lies in one cyclic group. This explains the architecture of the opposite-Ω orbit; it neither trivializes that orbit nor proves that its known generator is primitive.

Both calibrations are symbolic deductions; no word scan or root-of-unity experiment is involved.

## 5. What this reduces, and what it leaves

For a fixed two-slot tensor, the first exact classification step is now finite: compute Z_C and decide whether it is scalar. In the ordinary case, all universal coupled moves are powers of one projective move; in the exceptional case, there is a genuine conjugate-group intersection to study.

This separates two problems that the proposed commensurator approach had combined. Nonarithmetic triangle-group specializations are unnecessary for the ordinary case. They may still provide information about the exceptional intersection, with the finite-root kernel carefully retained.

The geometric problem remains: which actual patterns realize exceptional S, and how do their unknotted seed closures restrict the intersection? There is no assertion here that every similitude is a rational tangle operation, that polynomial symmetry is isotopy, or that a cyclic symmetry cannot yield a counterexample.

Proposed next lemma, not a theorem: classify the Hermitian similitudes realized by the specified two-slot patterns with an actual unknot seed, up to a scalar and rational boundary operations. A positive result would reduce that class of pattern symmetries to explicit rational operations; a negative result would identify a genuinely new pattern symmetry.

Cheap falsifier of the algebraic theorem: one exact pattern tensor with nonscalar Z_C and two explicitly noncommuting universal braid-pair symmetries satisfying (1). Neither numerical agreement at roots nor a single input-pair equality would meet this test.

Relation to the earlier work: this theorem is a general rank-two Hermitian argument; the EKT-specific version was banked in CX-EKT-PAIR on 3 November. No priority claim is made.
