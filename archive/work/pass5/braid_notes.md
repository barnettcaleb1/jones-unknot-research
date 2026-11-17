# Fifth-pass braid and ribbon results

No counterexample and no general unknot-detection proof were found. The useful results are exact exclusions, plus a simplification of the satellite reduction. None is claimed to be new to the literature.

## 1. All twists and all colors in the Kinoshita--Terasaka symmetric-union family

Write H_N(K;q) for the normalized N-dimensional colored Jones polynomial, with H_N(U)=1 and H_2=V. Eisermann--Lamm, [A refined Jones polynomial for symmetric unions](https://arxiv.org/html/0802.2283), Example 6.7 and Table 2, specify a ribbon twist family D_k for which D_0=U, D_1=10_153, D_2 is Kinoshita--Terasaka, and

    V(D_k;q)-1 = ((-q)^k-1) f(q),
    f(q) = q^-4(q^2+1)(q-1)^2(q^2+q+1)(q^2-q+1).

The twist recurrence extends this identity to every integer k. Mirror conventions reverse exponents and do not affect the nonvanishing conclusions.

[Habiro's cyclotomic expansion](https://msp.org/gtm/2002/04/gtm-2002-04-005p.pdf), using its a_i normalization, gives

    H_N(K;q) = 1 + a_1(K;q)(q^N+q^-N-q-q^-1) + terms of order (q-1)^4.

Every higher term has at least two factors that each vanish to order two at q=1. Setting q=exp(h), the displayed factor is (N^2-1)h^2+O(h^4). Consequently a first nonzero h^2 or h^3 coefficient of H_2-1 is multiplied by (N^2-1)/3 in H_N-1.

Here f(exp(h))=6h^2+O(h^4). Therefore, for every N>=2,

    k odd:          H_N(D_k;exp(h))-1 = -4(N^2-1)h^2 + O(h^3),
    k even, k!=0:   H_N(D_k;exp(h))-1 =  2k(N^2-1)h^3 + O(h^4).

Both coefficients are nonzero. Thus H_N(D_k)=1 holds in this family exactly when k=0, which is geometrically the unknot. In particular the Alexander-trivial even-twist examples do not pass the color-three necessary condition that V-1 vanish to order at least four. The same argument excludes any mutant with the same ordinary Jones polynomial, without requiring a claim about higher-color mutation invariance.

The exact certificate `braid_ribbon_filter.py` checks f and its Taylor coefficients, then independently reproduces the k=2 polynomial with a 4-strand Temperley--Lieb braid calculation. The all-parameter proof above does not depend on bounded testing. The independent braid word is recorded in its JSON, so that its identification as a named knot is not needed to reproduce the algebraic check. This argument was independently checked by the homology agent.

Connected sums do not rescue this construction. Reduced colored Jones polynomials multiply under connected sum. Their values at q=1 are 1 and their first derivatives there vanish. If a product equals 1 in Z[q^+/-1], each factor must be a Laurent unit, hence q^r; the derivative condition then forces r=0. Thus any connected sum with one of the nonzero-k factors above also fails H_N=1, even if some low Taylor coefficients cancel.

## 2. The ordinary (2,1)-cable already converts H_3=1 into V=1

Use the skein convention delta=-A^2-A^-2, an empty diagram equal to 1, and a trivial framed circle equal to delta. Let J_2(C) denote the zero-framed Jones--Wenzl degree-two evaluation, so

    Delta_2 = J_2(U) = A^4+1+A^-4,
    H_3(C) = J_2(C)/Delta_2.

In TL_2, let P_2=1-e/delta and P_0=e/delta. The positive crossing is

    A*P_2 - A^-3*P_0.

Embedding this in the zero-framed tubular neighborhood of C and closing gives A J_2(C)-A^-3. The resulting (2,1)-cable has one positive framing crossing; multiplying by -A^-3 and dividing by delta to set V_U=1 yields

    V(C_(2,1)) = (-A^-2 J_2(C)+A^-6)/delta,
    V(C_(2,1))-1 = -A^-2 (J_2(C)-Delta_2)/delta.

The unknot normalization is verified directly: -A^-2 Delta_2+A^-6=delta. Thus, as a polynomial identity,

    V(C_(2,1))=1  iff  H_3(C)=1.

Here (2,1) means winding two and one positive longitudinal braid crossing relative to the companion's zero framing; some papers reverse the two slope indices. A nontrivial companion has nontrivial (2,1)-cable, for example by the classical cable genus formula g(C_(2,1))=2g(C)>0. This familiar cable is a simpler converter than the Ren wrapping-four pattern. It does not supply a companion satisfying H_3=1 and is not a proof of either detection statement.

## 3. Why the faithful LKB representation is not an automatic solution

Jackson--Kerler, [The Lawrence--Krammer--Bigelow representations via U_q(sl_2)](https://arxiv.org/html/0912.2114), Theorem 2 and equation (3), identify their generic highest-weight construction with LKB after

    q_LKB=s^2,  t_LKB=-q^-2

and a braid inversion automorphism. Their finite-dimensional specialization, equations (46)--(49), uses s=q^ell. Color three has ell=2 and therefore lies on the curve

    q_LKB=q^4,  t_LKB=-q^-2,  q_LKB*t_LKB^2=1.

Faithfulness with two independent parameters does not imply faithfulness on this curve. No claim of faithfulness or nonfaithfulness of the full color-three braid representation is justified by that identification alone. Also, faithfulness of a representation would not by itself settle unknot detection by its Markov trace.

## 4. A concrete all-powers obstruction for the prior Bigelow braid

`braid_color3_kernel.py` applies Jackson--Kerler equation (23), with s=q^2 and q=2, to the total-lowering-two sector of (C^3)^tensor5. This is an invariant 15-dimensional sector. The script checks inverse matrices and braid relations with exact rational arithmetic, then evaluates the previously specified Bigelow B5 Burau-kernel braid K.

Its trace is the exact positive rational number recorded in `braid_color3_kernel.json`; its absolute value is greater than 15. Hence at least one eigenvalue has modulus greater than 1. For every nonzero integer m, rho(K)^m cannot equal the identity; conjugation does not change this conclusion. Thus no nonzero power or conjugate of this specific K is in the generic color-three representation kernel. Writhe is zero, so changing the scalar normalization of each braid generator does not alter this statement.

This excludes a representation-kernel construction only. It does not exclude a coincidence of colored Jones traces for particular knot closures. No non-Bigelow color-three kernel construction emerged during the bounded pass.

## 5. Exact obstruction to the proposed finite-image shortcut for arbitrary top braids

Let T be the Ren capped four-strand core from `tangle_four_strand.json`, and let rho_2 be the three-dimensional two-through TL4 module. Its standard link-state basis has caps at (1,2), (2,3), or (3,4). The annular coefficient of z^2 in the closure of T beta is exactly

    a(T beta) = tr(M rho_2(beta)),  M=rho_2(T),

because T's four-through component is zero. This is a scalar trace equation; M need not vanish when the scalar does.

The exact Laurent matrix is recorded in `braid_core_matrix.json`. Put y=A^4 and write Phi_j for the j-th cyclotomic polynomial in y. Its three eigenvalues are

    lambda_0 = A^-10 Phi_1^2 Phi_2 Phi_4,
    lambda_+ = A^-18 Phi_1^2 Phi_2 Phi_4^2 Phi_6,
    lambda_- = -A^-6 Phi_2 Phi_6 = -A^6-A^-6.

The verifier checks the corresponding cubic matrix identity and their product

    det(M) = -A^-34 Phi_1^4 Phi_2^3 Phi_4^3 Phi_6^2.

Thus M is generically invertible, not a rank-one operator. This prevents a direct identification of the target as one elementary Burau arc-intersection pairing. The rank degeneracies occur precisely at the small cyclotomic parameters already known to annihilate the degree-two coefficient of the genuine-unknot seed beta=sigma_1^-1 sigma_3.

More specifically, at a primitive 24th root A (y primitive sixth), exact reduction modulo A^8-A^4+1 proves M=e_2. Modulo97 with A=4, the normalized generators A^-1 rho_2(sigma_i) have order3. Complete enumeration gives an image of648 matrices,108 of which have tr(Mg)=0. One such class is sigma_1^2 sigma_3, the same image as sigma_1^-1 sigma_3. The known geometric unknot seed therefore already passes this proposed finite-image zero test. No all-braid exclusion follows from this root. The enumeration is explicitly over F97; it is not being used as a proof of the characteristic-zero image order.

At Ising parameter y primitive fourth, the generic three-dimensional standard module has a radical; finiteness of its two-dimensional semisimple quotient does not imply finiteness of the original three-dimensional image. This finite-image idea did not produce an exclusion. The first-jet argument below subsequently did, at a different parameter.

## 6. All-B4 theorem: no top braid can remove the remaining annular degree two

The tangle agent found the following first-jet proof. I independently reconstructed its matrices and checked the integral quotient argument; this is an all-word theorem, not evidence from a search.

Set x=-A^-4, S=diag(1,A^2,A^4), and define

    M(x)=A^-2 S^-1 rho_2(T) S,
    U_i(x)=A^-1 S^-1 rho_2(sigma_i) S.

Each U_i is the identity except in row i, where its diagonal is x, its predecessor entry is -x if present, and its successor entry is1 if present. Its determinant is x; its inverse has entries in Z[x^+/-1]. For a braid beta of writhe w, put U=U_beta. Then

    a(T beta)=A^(w+2) F(x),  F(x)=tr(M(x)U(x)).

The exact matrix calculation gives

    M(1) = [[-15,0,15],[-25,0,25],[-15,0,15]],
    M'(1)= [[-33,0,0],[-40,-8,-15],[-15,0,-18]].

Let u=(1,0,1)^t, v=(0,1,0)^t, and r=(1,0,-1). Every U_i(1) fixes u and has determinant1. Also

    M(1)=(-15u-25v)r,
    M(1)=0 modulo5,  M'(1)=2I modulo5.

Suppose F(1)=0. Since r u=0 and U(1)u=u, taking the trace gives

    0=F(1)=-25 r U(1)v.

The quotient lattice Z^3/<u> is free of rank2: the basis change with columns (u,e1,e2) is unimodular. In its quotient basis ([e1],[e2]), rU(1)v is precisely the upper-right entry of the induced integral matrix B, and det B=1. Its vanishing forces B to be triangular, with diagonal entries both1 or both-1. Therefore

    tr U(1)=1+tr B is either3 or-1.

Differentiate F and reduce modulo5. The term involving U'(1) drops out because M(1)=0 modulo5, so

    F'(1)=2 tr U(1) modulo5, which is either1 or3.

In either case the derivative is nonzero. Thus F cannot vanish identically: either its value at1 is nonzero, or it has a simple zero there. Consequently a(T beta) is nonzero for every beta in B4, without any assumption on the permutation or number of closure components. Since its annular z^4 coefficient is always zero, every such closure has annular skein degree exactly2.

The trace-to-annular identification was checked on all13 nonidentity TL4 basis diagrams. The identity diagram is the only four-through basis diagram; its coefficient is zero in T and remains zero after multiplication by every braid generator and inverse. This accounts for the otherwise relevant S4(z)=z^4-3z^2+1 correction and prevents a normalization gap.

This theorem blocks the entire strategy of appending an arbitrary four-strand top braid to this fixed Ren core in order to obtain annular degree zero. It does not prove ordinary Jones unknot detection: an ordinary closure may still be the unknot, as the known seed illustrates, and the corresponding satellites still retain the color-three condition.

## Reproduction

Run `python3 work/pass5/braid_ribbon_filter.py` and `python3 work/pass5/braid_color3_kernel.py`. Both use exact arithmetic; the former imports the existing TL engine from `work/attack_search/search.py`, and the latter imports the explicit Bigelow word from `work/pass2/braid_kernel.py`.

Run `python3 work/pass5/braid_core_matrix.py` and `python3 work/pass5/braid_finite_image.py` for the final exact matrix and finite-image audit. These use only the four-strand core JSON and Python's standard library.

Run `python3 work/pass5/braid_first_jet_audit.py` for the independent all-B4 proof certificate; it imports the independently reconstructed core matrix and compares the first jets with the tangle agent's certificate.
