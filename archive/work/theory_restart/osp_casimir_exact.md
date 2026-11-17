# Exact osp(1|2) comparison for the minus-one crossing symbol

Codex subagent `osp_casimir_exact`, 16 November 2026. Referee of Claude212613 item2. This is a fixed finite-dimensional calculation, not a scan and not an appeal to a generic quantum-group correspondence.

## Verdict

**The proposed comparison is correct, with the crossing-versus-chord distinction made explicit.** In the conventions of `ft_local.py`, let P be the root super permutation and let K be contraction followed by coevaluation. For the invariant form `B(X,Y)=str_V(XY)/2` on osp(1|2), its natural-module tensor Casimir is

    Omega=P-K.

The exact local crossing-difference symbol is

    C22=2K-2I=-2 Omega+2P-2I.

After transporting the crossing's endpoints back by the root permutation, the straight chord insertion is therefore

    P C22=C22 P=-2 Omega.

Thus Claude's request “Casimir modulo identity and root super flip” holds exactly. More naturally, the endpoint-transported symbol is exactly a multiple of the Casimir, with no corrections. All statements below are verified by 21 exact assertions in `referee_checks/osp_casimir.py`; the output is `osp_casimir.json`.

## 1. The actual root duality is orthosymplectic

Use the ordered basis `(w0,w1,w2)` with parities `(1,0,1)`. At `q=i` the cup and cap from the FT construction are

    z=coev(1)=-w0⊗w2+w1⊗w1+w2⊗w0,
    ev(w0⊗w2)=1, ev(w1⊗w1)=1, ev(w2⊗w0)=-1.

The cap's matrix is

    G = [[0,0,1], [0,1,0], [-1,0,0]].

It is symmetric on the even line and skew-symmetric on the odd plane, with no mixed term: this is a nondegenerate even supersymmetric form. There is no mismatch in the odd signs. In particular the root cup is **not** `w0w2+w1w1+w2w0`.

Let `Pi=diag(-1,1,-1)` be parity and `K=z ev`. Directly,

    ev(z)=-1, K²=-K, P K=K P=K,

where `P(v⊗w)=(-1)^(|v||w|)w⊗v`. These relations encode superdimension `1-2=-1`.

## 2. Define osp from this form and compute its metric

The homogeneous endomorphisms preserving G satisfy

    X^T G+Pi^p G X=0,

where p is the parity of X. The even solution space has basis

    H=diag(1,0,-1), E=E02, F=E20,

and the odd solution space has basis

    Qplus=E01-E12, Qminus=E10+E21.

Here Eij sends wj to wi. The two matrix equations for the even and odd blocks give these dimensions3 and2 directly, so this is the full orthosymplectic Lie superalgebra, not merely a subalgebra of it. The bracket is the supercommutator. For example,

    Qplus Qminus+Qminus Qplus=H,
    Qplus²=-E, Qminus²=F.

For `str(M)=tr(Pi M)`, use the invariant bilinear form

    B(X,Y)=str(XY)/2.

Its invariance follows from the supertrace cyclic rule; nondegeneracy is visible in the dual basis below. For the ordered basis `(H,E,F,Qplus,Qminus)`, its right-dual basis, satisfying `B(X_i,X^j)=delta_i^j`, is

    (-H,-2F,-2E,-Qminus,Qplus).

Thus all normalizations are fixed explicitly. Rescaling B rescales the Casimir inversely; no claim about a different author's preferred Killing-form factor is needed.

## 3. Compute the tensor Casimir

For homogeneous A,B, use the super tensor convention

    (A tensor_s B)(v⊗w)=(-1)^(|B||v|)Av⊗Bw.

In ordinary matrices this is `(A Pi^|B|) tensor B`. The invariant canonical tensor is

    Omega=sum_i (-1)^|X_i| X_i tensor_s X^i
         =-H⊗H-2E⊗F-2F⊗E
           +Qplus tensor_s Qminus-Qminus tensor_s Qplus.

Substituting the five matrices gives **Omega=P-K**. The certificate independently checks that this operator commutes with the super diagonal action

    Delta_s(X)=X⊗I+Pi^|X|⊗X

for all five generators. It is therefore the natural-module tensor Casimir of the orthosymplectic algebra defined above, with the stated invariant form.

For calibration, V tensor V has the familiar invariant sectors of ordinary dimensions1,3,5 in this representation. The Casimir eigenvalues are2,1,-1. This follows here without a decomposition theorem: K has one-dimensional image with eigenvalue-1; P has +1 multiplicity4 and -1 multiplicity5; K vanishes on the other eigenspaces. Thus Omega=P-K has multiplicities1,3,5 for2,1,-1 respectively.

## 4. Compare with the FT symbol

The FT certificate defines

    C22=((B22-B22^-1)/h)|h=0,
    q=i exp(h/2), t=q²=-exp(h).

Direct differentiation gives

    C22=2K-2I.

For example on the middle input,

    C22(w1⊗w1)=-2w0⊗w2+2w2⊗w0.

Because `P K=K`,

    P C22=2K-2P=-2 Omega.

This has eigenvalues-4,-2,+2 on the dimensions1,3,5. The **raw crossing** symbol instead has eigenvalues-4,-2,-2: it has not yet removed the root endpoint permutation. Confusing these two operators would produce an incorrect apparent mismatch with the Casimir.

The exact answer in Claude's requested form is

    C22=-2 Omega+2P-2I.

It is important that these I,P terms are not evidence of a new Lie algebra: they arise because C22 is still a crossing morphism. Preferred framing can add a multiple of P to the raw principal insertion, equivalently a scalar identity to the straight chord insertion. The core Casimir comparison survives that usual framing adjustment.

## 5. Scope of the identification

This proves the **off-axis principal-symbol** identification. Root cups/caps are precisely the orthosymplectic duality, and straight off-axis chords carry `-2 Omega`, up to the convention reversal already noted in FT. A simultaneous mirror/parameter inversion changes the sign of the first-order symbol.

The rest of the root model supplies additional marked data:

* root mixed monodromy is `Id_(axis) tensor Pi`;
* the normalized on-axis symbol is `3(T0-I)=-6 Id tensor Qodd`;
* the two root vertices select w1 and its dual, with cancelling signs.

Parity implements the grading automorphism of osp: it commutes with even generators and conjugates odd generators to their negatives. This is a concrete reason to describe the axis as a parity defect. It is nevertheless additional data to the ordinary closed-link osp weight system: the endpoints are selected vectors, and a rank-two axis with nontrivial mixed monodromy has not been identified with an ordinary module in the symmetric classical category.

The calculation therefore supports the precise statement “the off-axis chords use the fundamental osp(1|2) Casimir, with the explicitly given parity insertions and pointed boundary conditions.” It does **not** prove a full ribbon-category equivalence, identify the integral third-order iota invariant, or establish nonvanishing of the resulting series. Those require further arguments.
