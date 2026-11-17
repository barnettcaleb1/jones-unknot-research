# Band obstructions for EKT Jones-trivial links

Research continuation, 2026-10-31. These calculations concern the explicit EKT construction, not all possible links with the unlink Jones polynomial. No general solution of Jones unknot detection is claimed.

## 1. Published stronger obstruction for boundary links

Let L be a two-component boundary link. Feller–Park–Powell, *The Z-genus of boundary links*, Revista Matemática Complutense 36 (2023), Corollary 1.9, proves that any internal band fusion K satisfies g_Z(L) <= g_Z(K). Corollary 1.3 proves g_Z(L)=0 exactly when the single-variable Alexander module H_1(X_L; Z[t,t^-1]) has no Laurent-polynomial torsion submodule. Thus a band fusion to the unknot requires this entire torsion submodule to vanish.

This is stronger than the requirement H_1(Sigma_2(L);Z)=Z. The ordinary one-variable Alexander polynomial of a boundary link vanishes because the module has positive rank; that does not imply the torsion submodule vanishes.

Primary source: https://link.springer.com/article/10.1007/s13163-022-00424-3 (Corollaries 1.3 and 1.9).

No full Alexander-module computation is necessary for the explicit LL1 and LL2 examples below: their double-cover homology already obstructs every band to the unknot.

## 2. Exact construction of LL1(m,n)

EKT uses T dot U = reciprocal-reflection(T) + U. A repeated parenthesized word (1 dot 1/2)^m means insert the list of factors 1,1/2 a total of m times into the left-associated product. It must NOT be implemented as repeated multiplication by the single compound tangle (1 dot 1/2). The latter changes the examples and fails EKT Proposition 4.2.

Our implementation constructs

    seed S_mn = n dot 1 dot [1 dot 1/2]^m dot (-1),
    T_mn      = n dot 1 dot [1 dot 1/2]^m dot 1 dot 1 dot 2,
    LL1(m,n)  = H(T_mn, -3).

Here T_mn is the transformed tangle used in the LL1 definition, not EKT's untransformed tangle with the same letter. The seed numerator is the unknot (EKT Prop.4.2); the transformed tangle is omega(seed).

Validated implementation: work/ekt_model/ll1_scan.py. For m=0,1,2,3 and n=-3,...,3, every seed numerator simplifies to the unknot. Every m>=1 diagram has Jones polynomial exactly -x-x^-1. At m=0 the Jones polynomial matches the EKT parity distinction. Full diagram codes and integer Smith results are in ll1_scan.json.

## 3. Fraction data are valid even for the nonrational tangles

A tangle whose numerator is the unknot has double branched cover X with a Dehn filling equal to S^3. Therefore X is the exterior of the core knot of the attached solid torus in S^3. In particular H_1(X;Z)=Z, and the map from boundary homology onto H_1(X) is surjective. The universal Fox-coloring module of the tangle is the direct sum of a global constant-color Z and H_1(X); it is therefore free of rank two. Its integral boundary data are described by a primitive pair (p,q), not merely a rational relation valid over Q. The omega operation only reparametrizes the boundary, so it preserves this property.

Consequently the same exact two-generator Fox calculation used for rational tangles applies to these tangles. For H(T,U), with primitive data (p_T,q_T),(p_U,q_U), it yields

    H_1(Sigma_2(H(T,U))) = Z direct-sum coker [[p_U, -2q_T],[-2q_U, p_T]].

This presentation was independently derived in the ekt_homology agent's work and checked against full diagrams. For U=-3, the matrix contains the coprime entries -3 and -2, so its finite cokernel is cyclic of order | -3p_T -4q_T |.

## 4. Closed formula for all LL1(m,n)

Set A = 4^m (3n+2). Immediately after n dot 1 and the m repeated pairs, the tangle's fraction pair is

    (p,q) = ((A+1)/3, (A-2)/3).

This follows because n dot 1 has pair (n+1,n) and one repeated pair sends

    (p,q) -> (3p+q, 2p+2q),

whose eigenvalues are 4 and 1. In particular p-q=1 throughout, consistent with the unknot numerator after the final dot(-1).

Appending dot1 dot1 dot2 gives

    p_T=(8A-1)/3,  q_T=A.

Hence

    H_1(Sigma_2(LL1(m,n))) = Z direct-sum Z / |12*4^m*(3n+2)-1|.

The order is never 0 or 1 for m>=0,n integer: A is an integer congruent to 2 mod3 and hence nonzero; |12A-1|>=11, with the actual allowed minimum 13. Thus no member of the LL1 family can band to the unknot. This includes every Jones-trivial member (m>=1, or m=0 with n even).

Sample exact orders:

| m \\ n | -3 | -2 | -1 | 0 | 1 | 2 | 3 |
|---|---:|---:|---:|---:|---:|---:|---:|
|0|85|49|13|23|59|95|131|
|1|337|193|49|95|239|383|527|
|2|1345|769|193|383|959|1535|2111|
|3|5377|3073|769|1535|3839|6143|8447|

## 5. All additional omega iterates of LL1 are also blocked, except the actual unlink seed

Let k be any integer, counted from LL1(m,n) itself, so that k=-1 is the pre-omega seed H(S_mn,infinity+2), the two-component unlink.

Write

    Omega^k = [[a,8b],[b,a]],  a>0, a^2-8b^2=1,
    Omega   = [[3,8],[1,3]].

The pair for T is multiplied by Omega^k, and U by Omega^-k. The finite homology order is |D|, where

    D = (a+2b)^2 - 4A(3a+8b)(a+3b),
    D-1 = 4(a+3b)[b-A(3a+8b)].

Because A=2 mod3, D=1 mod12. Thus D cannot be 0 or -1. To get |D|=1 one must have D=1.

If a+3b=0, Pell's equation gives (a,b)=(3,-1), exactly k=-1. Otherwise D=1 forces b=A(3a+8b). If b=0 then k=0 and A=0, impossible. Squaring this equality and using Pell gives

    (1-16A-8A^2)b^2 = 9A^2.

Positivity confines the integer A to {-2,-1,0}. Since A=2 mod3, only A=-1 survives. But then b=-3a-8b, hence a=-3b, contradicting a+3b!=0. Therefore D=1 occurs exactly at k=-1.

The homology cokernel is still cyclic: p_U'=-3a-8b is odd, and gcd(p_U',q_U')=1 for q_U'=a+3b. Thus gcd(p_U',2q_U')=1, forcing the first Smith factor of the 2x2 matrix to be 1.

Conclusion: every member of the full LL1 omega orbit other than the known unlink seed has nontrivial finite torsion in the double branched cover. None can be banded to the unknot.

Independent full-diagram verification: work/ekt_model/ll1_orbit.py constructs omega and inverse omega as actual tangle operations. For five pairs (m,n) and k=-3,...,3, all 35 exact integer Smith forms agree with D. Data include full PD codes in ll1_orbit.json. The tested examples have up to 53 crossings; this is a finite verification of the construction and formula, not a substitute for the all-integer argument above.

## 6. Scope and source

EKT: https://homepages.math.uic.edu/~kauffman/ekt.pdf, Sections 3 and 4.2. The omega actions and numerator-unknot claim are theirs. The homology calculation and the obstruction application above are this investigation's derivation; no novelty claim is made and no exhaustive literature search for an existing version is asserted.

This closes the band-to-unknot route for these explicit known families. It does not rule out other Jones-trivial links, other constructions of knots with Jones polynomial 1, or arbitrary Jones-trivial knots.

## 7. Stronger universal statement for the EKT unknot-seed construction

The LL1 orbit argument above simplifies and extends to every tangle S whose numerator is the unknot.

**Proposition (derived in this investigation).** Let S be any 2-tangle with numerator closure the unknot. Form L_j = H(S, infinity+2)^(omega^j), for j any integer. Then L_0 is the two-component unlink, while for j != 0 the double branched cover of L_j has nonzero finite homology torsion. Consequently no L_j with j != 0 admits a band surgery to the unknot.

**Proof.** The double cover X of S is a knot exterior in S^3 because its numerator Dehn filling is S^3. Thus H_1(X)=Z, and the primitive boundary pair for its Fox module may be normalized to (p,q)=(1,d) for some integer d. The pair for infinity+2 is (1,0). Let

    Omega^j = [[a,8b],[b,a]],   a>0, a^2-8b^2=1.

The omega operation acts by Omega on the first tangle and Omega^-1 on the second. Their new pairs are

    (p_T,q_T) = (a+8bd, b+ad),
    (p_U,q_U) = (a,-b).

The two-offset/two-difference Fox presentation gives

    H_1(Sigma_2(L_j)) = Z direct-sum coker
        [[a, -2(b+ad)], [2b, a+8bd]].

Because a is odd and gcd(a,b)=1, this 2x2 matrix has first Smith factor 1. Its determinant is

    D = a^2+4b^2+12abd = 1+12b(b+ad).

Thus the group is Z direct-sum Z/|D|. In particular D=1 mod12, so D cannot vanish or equal -1. If D=1, then b=0 or b=-ad. In the second case a divides b, whereas gcd(a,b)=1, forcing a=1 and then b=0 by Pell's equation. Therefore D=1 exactly when b=0, namely j=0. This proves |D|>1 for every j!=0.

The actual unlink nature of L_0 is EKT's geometric observation that H(S,infinity+2) is a split union of S^N with an unknot. QED.

Consistency checks: LL2 has d=0, giving |D|=1+12b^2. For LL1, write the original seed pair as (-1,e), e=(4^m(3n+2)+1)/3; normalizing yields d=-e. The first omega move gives D=13-36e=1-12*4^m(3n+2), exactly the independently computed formula. An LL1 additional iterate k corresponds to j=k+1.

This is stronger than the family-specific statements: it rules out the band-to-unknot route for all the two-component links produced by the EKT unknot-seed omega construction, regardless of whether the initial tangle is rational. It still does not rule out other constructions of Jones-trivial two-component links.
