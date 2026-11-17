# Exact Boolean gates in generic Temperley–Lieb networks: scope and obstructions

17 November 2026. Bounded algebraic contribution to JT2. No gate search, diagram enumeration, or hardness theorem. The statements distinguish ordinary tangles, linear combinations in their skein module, braids preserving a code, and postselected maps between codes.

## 1. A fundamental strand is not a Boolean copying wire

Work over K=Q(A) at generic parameter. Let V1 be the fundamental two-dimensional quantum sl2 object. The fusion rule is

    V1 tensor V1 = V0 direct-sum V2.

Thus Hom(V1,V1 tensor V1)=0. Equivalently, an ordinary unoriented tangle cannot have three boundary endpoints: every component pairs its boundary endpoints. Consequently a literal COPY map sending the two spin basis vectors to their repeated tensor squares cannot be a one-input/two-output fundamental-strand TL morphism. A trivalent Boolean equality signature on three such ports is not an allowed TL tensor.

This is a local obstruction to a naive Holant translation, not to encoded computation. Fusion multiplicity spaces supply logical degrees of freedom. For example

    H4=Hom(V0,V1^4),        dim H4=2.

A logical bit can be a choice of basis in H4. Two logical bits occupy the four-dimensional tensor-product code H4 tensor H4 inside Hom(V0,V1^8), whose full dimension is Catalan_4=14. That distinction creates leakage conditions. A COPY between these codes is a map with four physical input and eight physical output ends, not a three-ended tangle. With b logical bits this simple disjoint-block encoding uses 4b fundamental boundary strands; no claim that it is optimal is needed.

Generic TL spans the intertwiners algebraically. This means a desired encoded map may be a rational linear combination of crossingless diagrams. It does not mean one actual tangle realizes it, or that a polynomial-size actual-tangle compiler exists. In particular, Jones–Wenzl projectors are supplied linear combinations with denominators unless a separate physical realization is given. Applying them formally to a calculation is not an exact gate construction.

## 2. An arithmetic obstruction to a standard exact mixing gate

Let Lambda=Z[A,A^-1]. Any usual diagram/cell TL braid module has an integral lattice on which every braid and its inverse act by Lambda-matrices: a crossing is A I+A^-1 e_i and its inverse is A^-1 I+A e_i. The statements below apply to any representation with this integral-lattice property.

**Lemma (no projective rational Hadamard on an invariant code).** Let rho(beta) lie in GL_D(Lambda), so its inverse also has entries in Lambda, and let W be a rho(beta)-invariant K-subspace. There is no K-basis of W in which its restriction equals lambda(A) H, with nonzero lambda in K and

    H = [[1,1],[1,-1]].

The same conclusion holds for H tensor I_d on a larger invariant code.

**Proof.** Localize Lambda at its height-one prime (2). This is a DVR with uniformizer 2, residue field F2(A), and valuation taking integer values on K*. Both rho(beta) and its inverse preserve the resulting lattice. All eigenvalues in an algebraic extension therefore have valuation zero: integrality gives nonnegative valuation, and integrality of the inverse gives nonpositive valuation.

But the eigenvalues of lambda H are plus or minus lambda sqrt(2), of valuation v_2(lambda)+1/2. This cannot be zero because v_2(lambda) is an integer. The eigenvalues of a restriction to an invariant subspace are among the ambient eigenvalues, giving a contradiction. No regularity of a chosen code basis at any complex value of A is required. QED.

For the elementary four-strand code there is an even shorter check. Each braid generator has eigenvalues A and -A^-3, so

    det rho(beta)=(-A^-2)^(exponent(beta)).

Equality rho(beta)=lambda H would require -2lambda^2 to equal that Laurent unit. Equivalently, plus or minus 1/2 would be a square in Q(A), which it is not.

**Scope.** This forbids a particular familiar exact mixing gate in a rational invariant-code braid compiler. It does not forbid every counting gate set. It does not cover caps/cups with postselection, leakage followed by projection, noninvertible actual tangles, or arbitrary field extensions in the encoding. If a logical basis is defined using independent algebraic normalization factors rather than K-rational state vectors, the hypothesis must be checked anew. Specialized root-of-unity representations and approximate synthesis are different problems. Clearing a global scalar does not evade the lemma within K: the valuation argument already allows every nonzero rational-function scalar.

## 3. Root's constant-gate lemma: generic braid compilers have finite constant image

The following is the root agent's proposed lemma, independently checked here.

Let rho be a fixed finite-dimensional generic TL braid representation on N physical strands. Assume its standard matrices are regular at A=1. Let Gamma be a subgroup of B_N preserving a generic code W over C(A). Suppose in one common basis of W each specified generator acts as

    rho_W(beta_i)=u_i(A) C_i,

where u_i is nonzero and C_i is a constant invertible complex matrix. Then the projective group generated by the C_i factors through the permutation image of Gamma in S_N. In particular it is finite and has order at most N!.

**Proof.** At A=1 the braid generator squares to the identity: with delta=-2 and e_i^2=-2e_i,

    (I+e_i)^2=I.

Hence every pure braid acts as the identity on the full specialized module. Let beta be in Gamma intersect P_N. Its generic restriction is u_beta(A) C_beta. Its characteristic polynomial divides that of the full rho(beta), so each u_beta(A)lambda_j, where lambda_j is an eigenvalue of C_beta, is an eigenvalue of the full matrix. As A approaches 1 all full eigenvalues approach 1. Therefore u_beta has a finite nonzero limit and every lambda_j is equal.

To eliminate a possible constant Jordan block, use the positive-definite unitary arc for each fixed finite TL module. One direct justification is to replace e by -e, so the loop parameter becomes delta'=A^2+A^-2. At delta'=2 the ordinary finite TL Markov form is positive definite: the classical spin-one-half tensor representation is faithful and its normalized matrix trace is the Markov trace. Its Gram matrix remains positive definite for real delta' sufficiently close to 2. Thus along a small unit-circle arc about A=1 the operators A I-A^-1 e' are unitary. Directly, their product with their adjoints is I because e'^2=(A^2+A^-2)e'. This argument concerns fixed finite N, not an infinite-depth C*-planar algebra at arbitrary delta'<2.

Choose a point on that arc where the code basis and all needed scalars are regular. The restricted braid is unitary on its invariant code, so C_beta is diagonalizable. Since all its eigenvalues agree, it is scalar. Therefore Gamma intersect P_N lies in the projective kernel, and Gamma/(Gamma intersect P_N) is the finite permutation image. QED.

For a fully sourced alternative, the diagonalizability step needs only one sufficiently high-order unitary root, not a whole arc. Jones–Reznikoff, *Hilbert space representations of the annular Temperley–Lieb algebra*, Pacific J. Math. 228 (2006), §2, Theorem 2.1 and the paragraph before it, identify the positive TL quotient at delta'=2cos(pi/r); for N<r-1 no Jones–Wenzl ideal is removed, so the finite algebra has the generic dimensions. Choose A=exp(pi i/(2r)), so delta'=A²+A^-2. The finite path-model matrices are self-adjoint projectors, and the associated Jones braid matrices are unitary; see Freedman–Larsen–Wang, *A modular functor which is universal for quantum computation*, Commun. Math. Phys. 227 (2002), 605–622, equations (14)–(15). Arbitrarily large r avoid the finitely many poles and rank degeneracies of the code basis. Thus one such specialization makes C_beta diagonalizable and completes the proof even without the continuity argument. Primary sources: https://msp.org/pjm/2006/228-2/pjm-v228-n2-p02-p.pdf and https://www.microsoft.com/en-us/research/wp-content/uploads/2017/09/universality-02.pdf . No density theorem is imported.

**Consequences and limits.**

- No single invariant-code generic braid compiler can realize a constant gate library generating an infinite projective group, up to scalar functions, in one fixed code basis.
- If a proposed m-bit constant reversible library has projective image containing the alternating group on 2^m states, then N! >= (2^m)!/2. For m>=2 this forces N>=2^m. This is a conditional group-order deduction; the compiler must actually realize that entire gate group on the code, not merely one accepting amplitude.
- This does not rule out A-dependent gates, noninvertible operators, postselection, changing code spaces, or a direct scalar zero-test construction without a common invariant code. It does not prove that generic TL tensor networks cannot encode counting.
- A single constant finite-order gate is not excluded by this finite-image lemma. The rational Hadamard obstruction above uses an additional arithmetic lattice condition and gives a different restriction.

## 4. One surviving exact gate obligation

Fix rational embeddings E:H4 coordinates -> V1^4 and E2:H4 tensor H4 -> V1^8, together with the fixed dual extraction maps and all common denominators. An actual twelve-ended tangle D would be an exact encoded copier only if

    rho(D) E = lambda(A) E2 C,
    C(0)=00, C(1)=11,

as equality in the full output tensor space, for a specified nonzero common scalar lambda. Writing only the projected 4-by-2 matrix is insufficient: the equation also requires zero leakage into the ten complementary invariant directions. The corresponding clause gate needs its own exact truth-table matrix, normalizations and leakage equations. End connectivity and the final two-component closure remain additional geometric obligations.

This is a concrete algebraic test of one proposed diagram; it is not permission to enumerate diagrams. If only a rational linear combination of tangles solves the equation, the missing task is a compilation of that sum into one actual tangle. If a braid preserves the code and is proposed to supply constant universal mixing, the preceding lemmas provide inexpensive structural checks before such a search.

The current findings are TRUSTED internal deductions pending the root/Claude read. No claim of novelty or external specialist review is made.

## 5. Formal matrix multiplication is available; its physical compilation is not

For m independent inputs, in Mat_(m+1)(K) put

    M_i = I + z_i E_(i,i+1),      i=1,...,m,
    ell(M)=M_(1,1)+M_(1,m+1).

The ordered product has

    ell(M_1 ... M_m)=1+z_1 ... z_m.

Indeed the (1,m+1) entry requires the unique complete consecutive path,
while the (1,1) entry remains one. This elementary control explains why
the serial TL2 obstruction is a dimension/architecture statement, not an
obstruction in all matrix algebras. Generic TL algebras have matrix blocks
of growing size, so their linear skein category has room for such formal
calculations after choosing a sufficiently large block and rational matrix
units. This does not realize the matrices or the output functional by
actual tangles, and it supplies no efficient clause or counting compiler.

Every nonidentity M_i is unipotent. Such a matrix cannot itself be the
restriction of a generic braid to an invariant code: a sufficiently high
unitary specialization would make it both unitary and nontrivially
unipotent. Hence any actual implementation of this formal accumulator
would require something beyond a braid on that invariant code, such as
noninvertible operations or a different encoding with leakage and
postselection. Realizability and a two-component output remain open.

The root independently checked the proofs above, including the
constant-code finite-image lemma, the DVR obstruction, and this formal
path identity. Claude's referee read is pending.
