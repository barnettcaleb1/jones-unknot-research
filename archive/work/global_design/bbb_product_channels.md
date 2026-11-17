# Products of return axes: a two-axis theorem and a three-axis cancellation

2026-11-03. Supporting BBB-MULTISET. Written proof with an independent internal read and Claude165614's independent read of the two-axis theorem. Claude checked the three-axis degree count; the exact channel identities retain their internal read. Novelty unchecked. No enumeration was used.

The result detects arbitrary words on two axes, extending the single-return calculation. The explicit three-axis word below refutes strict highest-eigenchannel dominance for general products. It does not refute faithfulness or BBB-MULTISET, and it is not a Brunnian example.

## 1. Setup and theorem

Use unreduced Burau on columns over Q(t), with generator block [[1-t,t],[1,0]], and bar(t)=t^-1. Put

    R=rho_4(sigma_3^2)=I+(t^2-1)P,
    P=v ell,  v=(0,0,-t,1)^T,  ell=(0,0,-1,1)/(1+t).

For u_i in the old B_3 on strands 1,2,3, let U_i=rho_4(u_i), v_i=U_i v, ell_i=ell U_i^-1, P_i=v_i ell_i and R_i=U_i R U_i^-1.

**Theorem.** If P_i != P_j, the matrices R_i,R_j freely generate a rank-two group, and every nontrivial word has nonscalar image on span(v_i,v_j). Axis equality is equivalent to u_i^-1 u_j belonging to <sigma_1>.

Distinct conjugating braids need not define distinct axes. The theorem concerns two axes at a time, not a free group on their entire orbit.

## 2. Overlap and degree bounds

The invariant Hermitian form H_4 has diagonal 1 and entries

    (H_4)_(ij)=-t^(j-i-1) for i<j,
    (H_4)_(ji)=bar((H_4)_(ij)).

Each v_i has norm t+2+t^-1 and lies in the reduced invariant summand E=ker(1,t,t^2,t^3). H_4 restricted to E is positive definite for unit-circle t sufficiently close to 1. This follows at t=1 from H_4=2I-J, whose restriction to sum-zero vectors is 2I, and by continuity nearby.

With U=rho_3(u_i^-1 u_j), define

    eta=ell_i(v_j)=(1+t U_33)/(1+t),
    r=tr(P_i P_j)=eta bar(eta).

At t=1, U is a permutation matrix, so eta(1) is 1 or 1/2. Thus r is nonzero. If r were identically 1, equality in Cauchy-Schwarz on that definite arc would make the two lines equal at every nearby regular parameter and therefore over Q(t). Distinct axes consequently have r!=1. Their two-plane is nondegenerate.

All v_i have fourth coordinate 1, so equal lines mean equal vectors. Hence axis equality is equivalent to Ue_3=e_3, and BBB-RETURN's column-stabilizer lemma gives u_i^-1u_j in <sigma_1>.

Write N=1+t U_33, a Laurent polynomial. Both r and 1-r have nonzero reciprocal Laurent numerators over the common denominator

    D=(1+t)(1+t^-1)=t+2+t^-1.

A nonzero reciprocal Laurent polynomial has degree at infinity at least zero. Therefore

    d=deg_inf(r)>=-1,  e=deg_inf(1-r)>=-1.

Since r+(1-r)=1, either d=e>0, or both lie in [-1,0]. In particular |d-e|<=1.

## 3. Freeness for arbitrary two-axis words

On the two-plane set X=t^-1 R_i and Y=t^-1 R_j. Their eigenvalues are t,t^-1 and their determinants are 1. For a cyclically reduced alternating word

    X^(a_1)Y^(b_1)...X^(a_k)Y^(b_k),  all a_i,b_i nonzero,

expand the trace using each factor's two spectral projectors. The two-dimensional projector lemma proved in g2_two_twist_freeness.md gives each coefficient as

    +/- r^p (1-r)^(k-p),  0<=p<=k.

Changing one spectral choice changes p by at most one. For completeness, diagonalize P_i and write P_j=[[r,b],[c,1-r]], bc=r(1-r). A cyclic matrix-entry product pairs every off-diagonal b with a c; changing a choice toggles two adjacent binary agreements, which changes p by at most one.

Choose the larger-degree eigenvalue in every block. Its eigenvalue degree is sum(|a_i|+|b_i|)>=2k, and its coefficient degree is at least -k. Its total degree is therefore at least k>0. Changing s choices loses at least 2s eigenvalue degrees and gains at most s coefficient degrees. The chosen term is uniquely highest and cannot cancel.

The trace is nonconstant. Pure powers have trace t^a+t^-a, also nonconstant. Every nontrivial free word is conjugate to one of these cases; hence no such word is scalar in SL_2(Q(t)). Restoring the scalar factors t does not change nonscalarity. This proves the theorem.

## 4. A canonical three-axis word cancels at the predicted top degree

Use the standard free generators A_14,A_24,A_34 of the kernel of forgetting strand 4, and write R_i=rho_4(A_i4). They are the above conjugates for

    u_1=sigma_1^-1 sigma_2^-1,  u_2=sigma_2^-1,  u_3=1.

Their vectors and covectors are

    v_1=(-t,1-t,1-t,1)^T,
    v_2=(0,-t,1-t,1)^T,
    v_3=(0,0,-t,1)^T,
    ell_i=(-e_i^*+e_4^*)/(1+t).

The vectors are independent. Set a=1/(1+t), b=t/(1+t), so a+b=1. Then

    ell_i(v_j)=1 if i=j,  a if i<j,  b if i>j.

Consider the actual freely reduced word

    W=R_1 R_2^-1 R_1^-1 R_3.

The total exponent sum is zero, so W=X_1 X_2^-1 X_1^-1 X_3 with X_i=t^-1 R_i. On the three-dimensional reduced summand X_i=t P_i+t^-1 Q_i, where Q_i=I-P_i.

The maximal-eigenvalue channel has coefficient

    C_top=tr(P_1 Q_2 Q_1 P_3)=-a^3 b,

of degree -3. Changing only the third choice gives

    C_flip=tr(P_1 Q_2 P_1 P_3)=ab(1-ab),

of degree -1. Their weighted contributions obey the exact identity

    t^4(-a^3 b)+t^2 ab(1-ab)=t^2 a^2 b.

The two summands separately have degree 1, with opposite leading coefficients; their sum has degree 0. Thus the coefficient gain exactly cancels the eigenvalue loss. Strict dominance of the maximal-eigenvalue channel is false already in the canonical free basis, without a hidden relation among the axes.

Nevertheless W!=I. Otherwise R_3=R_1 R_2 R_1^-1, so their distinct nontrivial eigenlines would coincide. But

    R_1 v_2=v_2+(t-1)v_1

cannot be proportional to v_3, by independence. This also verifies that the example is a failure of a proof mechanism rather than a kernel example.

## 5. Scope and the remaining task

The example is not Brunnian: its individual A_i4 exponent sums do not all vanish. It neither refutes a suitably Brunnian-specific dominance statement nor supplies a Jones counterexample. It prevents extending the two-axis proof to arbitrary products solely from pairwise overlap bounds.

Regrouping factors as conjugated rank-one operators resolves this particular word, but an arbitrary prefix need not keep its eigenline in the old-B_3 orbit. No terminating regrouping argument or column-stabilizer theorem for that larger orbit has been proved here. That missing step cannot be hidden under the two-axis result.

BBB-MULTISET remains OPEN, held by Codex. Claude owns the actual unmodified push construction; no duplicate construction or search was performed in this pass.
