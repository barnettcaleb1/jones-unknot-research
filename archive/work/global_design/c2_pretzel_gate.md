# C2 candidate P(−5,9,11): arithmetic passes, strong inversion impossible

Date: 2026-11-03. Bounded theory/primary-source check; no Jones calculation or search over knots.

**Verdict:** the family κ_p=P(−p,2p−1,2p+1), odd p≥3, consists of noninvertible genus-one knots. In particular P(−5,9,11) has no strong inversion and cannot be an input to the Sakuma-link construction.

## Exact primary obstruction

[H. F. Trotter, Non-invertible knots exist, Topology 2 (1964), 275–280](https://ymsc.tsinghua.edu.cn/__local/F/9A/83/59C11C305D0DAC09D78FF073977_B742DA6C_53731.pdf), theorem on printed page 276: odd pretzel parameters whose absolute values are distinct and greater than one give a noninvertible knot. The PDF theorem itself was opened and read; this is not an inference from a search summary. Signed parameters are explicitly included. Trotter's proof also explains why changing a parameter's sign does not remove its obstruction.

For (−p,2p−1,2p+1), the three absolute values are p,2p−1,2p+1, distinct and greater than one. Strong inversion implies invertibility, so it is excluded. The obvious half-turn about the horizontal line through the centers of the standard odd twist boxes has no fixed points on the knot. It is a period, not a strong inversion. Trotter's Remark (2) contrasts this with the one-even-parameter case, where that horizontal rotation is an inversion.

## The proposed algebraic checks are correct

For odd a,b,c, the standard orientable two-disk/three-band pretzel surface has genus one. A Seifert matrix, up to the usual basis and global mirror conventions, is

    [(a+b)/2, (b+1)/2]
    [(b−1)/2, (b+c)/2].

Its determinant is (ab+ac+bc+1)/4, giving

    ∇_(P(a,b,c))(z) = 1 + [(ab+ac+bc+1)/4] z².

For a=−p,b=2p−1,c=2p+1, the pairwise-product sum is −1. Hence ∇=1, Δ=1, and a₂=0. Noninvertibility proves nontriviality; the exhibited genus-one surface therefore realizes the minimal genus. P(−5,9,11) has a standard 25-crossing diagram; no assertion about minimal crossing number is needed.

At A=q in F₁₆ with q⁵=1 and q≠1, the two-strand TL braid generator has distinct eigenvalues q and q⁻³=q². Thus σ⁵=I, and in particular σ¹⁰=I. Replacing 9 by −1 and 11 by 1 preserves the bracket at this specialization. Each replacement changes oriented writhe by ±10, so the Jones normalization also stays unchanged. The rational summands −1 and +1 cancel in P(−5,−1,1), leaving the numerator closure of the rational tangle −1/5, which is an unknot. Therefore

    V_(P(−5,9,11))(q)=1 in F₁₆.

This is a genuine example of a nontrivial knot satisfying the proposed a₂/FROB5 sieve. It fails the required geometric hypothesis for C2.

## No parameter repair within this class

**Corollary.** Every nontrivial odd three-strand pretzel knot with Δ=1 is noninvertible.

If two entries have equal absolute value, they are either a,a or a,−a. In the first case a₂=0 would require a(a+2b)=−1, forcing |a|=1. In the second case a₂=(1−a²)/4, again forcing |a|=1. If any parameter is ±1, the Montesinos presentation has an integer rational summand and only two remaining rational tangles, so it is a two-bridge link. For a knot, Δ=1 gives determinant one, and a two-bridge knot of determinant one is the unknot. Thus every nontrivial Δ=1 case has distinct parameter absolute values greater than one, and Trotter applies. ∎

Consequently imposing a visible repeated-parameter symmetry cannot repair this proposed genus-one odd-pretzel construction while retaining Δ=1. A new Sakuma seed must come from a different class.
