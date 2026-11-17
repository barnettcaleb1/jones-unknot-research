# Positive fractions and Perron eigenlines in the four-strand Burau representation

2026-11-03. Supporting BBB-MULTISET. Status: TRUSTED, written proof with independent internal reads of the cone/Perron argument and the Brunnian specialization corollary, and Claude171218's independent read. Novelty unchecked.

This controls certain products involving all three canonical point-pushing generators. It uses nonnegative dynamics at every real t>2, not a claim that a highest trace channel survives.

## 1. Statement

Let K=ker(P_4 -> P_3) be free on x=A_14, y=A_24, z=A_34. Use the unreduced Burau convention sigma_i=[[1-t,t],[1,0]] on columns. A positive word below uses x,y,z without inverses; the empty word is permitted for P,Q. Let H be nonempty and positive, and H_0 its primitive positive root, so H=H_0^r with r>=1 and H_0 not a proper positive power.

**Theorem (BBB-PERRON).** Fix any real t>2 and any nonzero integer m. If g has either form P Q^-1 or Q^-1 P with P,Q positive, then

    [rho_t(g),rho_t(H)^m]=I  iff  g belongs to <H_0>

as an actual word in K.

In particular every nontrivial braid commutator [g,H^m] of this form has nonidentity Burau image at every real t>2, and hence over Q(t). No faithfulness assumption on Burau_4 is made. The restriction on g is essential to the proof; it is not a normal form for every word of K.

## 2. Two cones, one for vectors and one for covectors

Put R_i=rho(A_i4)=I+(t^2-1)v_i ell_i, using

    v_1=(-t,1-t,1-t,1)^T,
    v_2=(0,-t,1-t,1)^T,
    v_3=(0,0,-t,1)^T,
    ell_i=(-e_i^*+e_4^*)/(1+t).

The v_i form a basis of the reduced invariant summand E=ker(1,t,t^2,t^3). The restrictions of the ell_i form a basis of E^*. These assertions hold at every real t>2. Set a=1/(1+t), b=t/(1+t); then

    eta_ij=ell_i(v_j)=1 (i=j), a (i<j), b (i>j).

In the vector basis, R_i changes only coordinate i:

    c_i' = t^2 c_i + t(t-1) sum_(j<i) c_j + (t-1) sum_(j>i) c_j.

In the covector basis, right multiplication by R_i also changes only coordinate i, with the off-diagonal coefficients reversed:

    c_i' = t^2 c_i + (t-1) sum_(j<i) c_j + t(t-1) sum_(j>i) c_j.

All other coordinates remain fixed. Thus both closed nonnegative cones, with the origin removed, are invariant under positive words. Each update makes coordinate i strictly larger than the sum of the other coordinates, because t-1>1. The three output regions are disjoint.

**Decoding lemma.** Starting from any nonzero vector in the vector cone, projectively equal positive-word images have the same first letter whenever both words are nonempty. In the covector cone they have the same last letter. The common letter can be cancelled and the argument repeated. In particular two words of equal length giving projectively equal images of the same nonnegative vector or covector are literally the same word.

The lemma includes vectors on boundary faces. Scalar proportionality is positive, since the coordinate vectors are nonzero and nonnegative. No contraction or limit of infinite words is needed.

## 3. A positive word has a simple nonnegative eigenline

Consider right multiplication by H in covector coordinates. Let I be the set of its letters. Coordinates outside I never change. On the coordinate face supported on I, the action has a strictly positive matrix A: each coordinate in I is updated at least once, and that update draws a strictly positive multiple of every coordinate in I. Subsequent updates preserve strict positivity of the updated rows.

Every diagonal entry of A is at least t^2. Its Perron eigenvalue lambda is therefore >1, simple, and strictly larger in modulus than its other eigenvalues. The full coordinate action has block form [[A,B],[0,I]] after ordering I first. Its other additional eigenvalues are 1. It consequently has a nonnegative eigenvector supported on I, giving a covector ell_H with

    ell_H rho_t(H)=lambda ell_H.

For m!=0 the eigenvalue lambda^m remains simple in rho_t(H)^m: no other eigenvalue has the same modulus as lambda before powering. For negative m it need not be the largest eigenvalue; simplicity is all that is used.

The identical argument for the vector cone gives a nonnegative right eigenvector v_H with the same simplicity property.

## 4. Centralizer proof

Suppose first g=P Q^-1. Commutation with rho_t(H)^m preserves its simple dual eigenline, so

    ell_H rho_t(P) is proportional to ell_H rho_t(Q).

Last-letter decoding makes P and Q suffix-comparable. Cancelling their common suffix leaves either P=TQ or Q=TP for a positive T, and

    ell_H rho_t(T) is proportional to ell_H.

Thus g=T or T^-1 as an actual free word. Since ell_H is also an eigenvector of H,

    ell_H rho_t(HT) is proportional to ell_H rho_t(TH).

The words HT and TH have equal lengths. The decoding lemma gives HT=TH literally. The elementary commuting-words lemma now gives T=H_0^s for some s>=0. One proof repeatedly cancels the shorter initial word from HT=TH, reducing total length until a common primitive root remains. Hence g is a power of H_0.

For g=Q^-1 P use the right Perron vector. Commutation gives rho_t(P)v_H proportional to rho_t(Q)v_H. First-letter decoding makes P,Q prefix-comparable, leaving g=T or T^-1, and the same equal-length argument proves HT=TH.

The converse follows from actual commutation of powers of H_0. This completes the proof at each real t>2. The invariant unreduced trivial summand causes no issue there: E has an invariant complement because 1+t+t^2+t^3 is nonzero.

## 5. An explicit family in Brun_4 intersect ker rho_4(-1)

Write delta=xyz. The standard pure-braid factorization of the full twist is

    Delta_4^2=Delta_3^2 A_14 A_24 A_34,
    delta=Delta_4^2 Delta_3^-2.

This is an identity of braids, not an inference from Burau matrices. For k>=1 set

    P_k=(xyz)^(2k) yx,
    Q_k=yx(zxy)^(2k),
    g_k=P_k Q_k^-1,
    W_(k,m)=[g_k,z^m],  m!=0.

Since zxy=(xy)^-1 delta(xy),

    g_k=[delta^(2k),h],  h=yx(xy)^-1=[y,x].

**Corollary.** Every W_(k,m) is Brunnian, its unreduced Burau matrix is I at t=-1, and its Burau matrix is nonidentity for every real t>2.

Proof of Brunnianness: deleting strand 4 kills x,y,z. Deleting strand 1 kills x, and the two positive words become equal by (yz)^(2k)y=y(zy)^(2k). Deleting strand 2 similarly uses (xz)^(2k)x=x(zx)^(2k). Deleting strand 3 kills the outer z^m. The remaining generators under each deletion are the standard renamed point-pushing generators.

For the specialization, rho_4(Delta_3^4)(-1)=I on the old three-strand block. This follows from its eigenvalues t^3 and 1 and the regular splitting at t=-1 (1+t+t^2=1 there). Consequently

    rho_4(delta^(2k))(-1)=rho_4(Delta_4^(4k))(-1),

a CENTRAL matrix in the braid image. It need not be scalar in the unreduced representation. Therefore rho_4(g_k)(-1)=I and likewise rho_4(W_(k,m))(-1)=I.

Finally P_k and Q_k begin with different letters, so g_k is a nontrivial actual free word. Its exponent sum in z is zero; it cannot be a nonzero power of z. The theorem with H=z proves nonidentity at every t>2.

For k=m=1, the braid identities, g(-1)=W(-1)=I in unreduced 4x4 matrices, and W(3)!=I received one exact rational calibration. The all-k, all-m conclusions follow from the proofs above, not that check. This is a different placement of nested commutators from both BBB-RETURN and the original Phi_0; no identification with Phi_0 or its chosen Gamma is asserted.

## 6. Where the argument stops

A general four-run word P Q^-1 R S^-1 does not preserve a known simple nonnegative eigenline. When it is cyclically freely reduced, Q and R have different first letters, so Q^-1 R sends the entire vector cone outside that cone. The other middle branch does so too. Prefix decoding alone cannot compare those mixed-sign images.

The theorem instead succeeds because commutation with a positive H supplies a simple Perron eigenline, turning the comparison back into two positive words. No theorem makes an arbitrary Brunnian kernel candidate admit that form. No finite-index or normal-generation argument promotes the detected family to the whole group.

BBB-MULTISET stays OPEN: this does not evaluate the prescribed Moody probe or extract the simultaneous localization of BBB-LOCAL. Its contribution is an exact mechanism for a family inside the actual Brunnian BI_4 slice, beyond the two-axis restriction, without trace-channel noncancellation.

Related dynamical prior art: Witzel–Zaremsky, [A free subgroup in the image of the 4-strand Burau representation](https://arxiv.org/abs/1304.7923), prove freeness for certain powers using Euclidean-building geometry. Their distinguished pair differs from the canonical point-pushing generators here. No novelty claim is made for this cone/centralizer statement.
