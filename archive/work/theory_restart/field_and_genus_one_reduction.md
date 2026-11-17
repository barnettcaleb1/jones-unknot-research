# Genus-one and coefficient-field reductions for the endpoint programme

16 November 2026. Root synthesis of three independent referee reports:

- `genus_one_rank_five_referee.md`;
- `characteristic_zero_ladder_referee.md`;
- `instanton_sutured_referee.md`.

The first result restricts actual covering knots. The second chooses the weakest coefficient-field version of the endpoint conjectures. Neither proves END or NP. The characteristic-zero ladder and the instanton target correction prevent two false shortcuts.

## 1. Actual genus-one covering knots require rank at least nine

Let T be a quotient tangle with an actual unknot filling, with covering knot kappa in S^3. Suppose T is Jones-flat and nonrational. The banked TH-S and U4 inputs give

    dim_F2 N(T) >= rank_F2 HFKhat(kappa),    a_2(kappa)=0.

If g(kappa)=1, then Delta_kappa=1. Indeed its normalized symmetric polynomial is a_0+a_1(t+t^-1), and a_2=a_1.

For any genus-one knot with Delta=1 the rational top Alexander group is nonzero and has Euler characteristic zero. Its dimension is therefore a positive even integer. Dimension two would make the knot genus-one nearly fibered over Q. Baldwin–Sivek, *Floer homology and non-fibered knot detection*, Forum Math. Pi 13 (2025), e1, Theorem 1.2 and Table 1, classify this case; every listed knot has determinant seven or nine. Thus the top dimension is at least four. Conjugation gives four at the bottom, and the central Alexander coefficient one gives at least one in the middle. Hence

    rank_Q HFKhat(kappa) >= 9.

Integral universal coefficients give rank_F2 >= rank_Q, without a torsion-freeness assumption. Consequently

    g(kappa)=1 and T flat nonrational  =>  dim_F2 N(T)>=9, m(T)>=4.

This excludes genus one from both dimN=5 and dimN=7. It does not exclude the higher-genus rank-five residual. The exact source and full coefficient argument are in the first referee report; [published source](https://doi.org/10.1017/fmp.2024.28).

### The rank-five residual has a specified sutured core

The previous low-rank theorem gives Delta=1, total F2 HFK rank five, Alexander ranks (2,1,2) at (-g,0,g), and |tau|=g. We now know g>=2. Its rational top rank is also exactly two: it is positive even and at most the F2 rank two.

Li–Ye, *The guts of nearly fibered knots*, AGT 26 (2026), 1385–1393, Theorem 1.4, Corollary 1.5 and Remark 2.1(1), then force guts model M1: a solid torus with four longitudinal sutures. The other two models have nonzero top Alexander coefficient. This is an additional actual-topology restriction, not a choice of formal chain complex. [Source](https://arxiv.org/html/2208.05382v3).

The residual would also violate next-to-top HFK nonvanishing, since HFK(g-1)=0. Existing results checked here do not rule it out: Ni's Theorem 1.1 requires a single top Maslov parity, whereas this top group has both; Binns–Wan's Theorem 1.3 requires a particular two-annulus decomposition. The four-suture guts description supplies neither hypothesis. Their Remark 4.13 expressly leaves general annular/disc decompositions open. [Ni](https://www.its.caltech.edu/~yini/Published/SecondTerm.pdf), [Binns–Wan](https://arxiv.org/html/2608.03900v1).

## 2. Coefficient-field reduction for END and NP

Let C_b(T) be the finite free integral complex obtained by the bullet augmentation of the integral Bar–Natan complex. Put N_F=H(C_b tensor F). Work with cochain differential of degree +1 in h. Let b_(h,q) be the free rank of integral homology and t_p(h,q) its number of p-primary cyclic summands. Universal coefficients give

    dim_Fp N_Fp^(h,q) = b_(h,q) + t_p(h,q) + t_p(h+1,q).

Thus rational bigraded support is contained in every mod-p support. All fields have the same *integer* graded Euler polynomial: the two contributions from each torsion summand cancel in adjacent h. This does not assert field-independent curve types or local systems.

Recall END means nonzero Euler coefficient at both unsigned quantum endpoints of N. NP means that each unsigned quantum endpoint is concentrated in one h-degree, equivalently one delta-level there. Assume N_Q is nonzero.

**Field lemma.** For either P=END or P=NP,

    P(N_Q) <=> P(N_Fp) for some prime p
           <=> P(N_Fp) for all but finitely many primes p.

Moreover P(N_Fp) implies P(N_Q) for every individual prime p.

Proof: under END_Fp, both mod-p endpoints are present in the common Euler polynomial, hence in rational support. Support inclusion forces the two endpoint degrees to agree, and the Euler coefficients are identical. Under NP_Fp, endpoint concentration first implies END_Fp, and rational endpoint support is a nonempty subset of one h-degree. Finally the integral homology has torsion at only finitely many primes, and all other primes have exactly the rational bigraded dimensions. This proves every implication.

The finite exceptional set depends on T. END_Q does not imply END_F2. A failed mod-two endpoint test can be a torsion effect; a failed rational test cannot disappear at any prime. The lemma chooses a weaker endpoint problem but does not itself establish noncancellation or the positive-breadth input needed in a detection argument over a different field.

## 3. Adjacent-degree pairs need not be torsion shadows

A Z/p^e cohomology summand in degree (k,q) produces mod-p copies in degrees (k,q) and (k-1,q). The converse is false: two free classes do the same and survive over Q.

The fixed twelve-generator compact object Q has an integral lift Q^- obtained by changing its D_b edge 1->12 to coefficient -1. Every differential square vanishes termwise by DS=SD=0. Its bullet augmentation is free of rank four in degrees

    (0,0), (1,2), (5,8), (6,10).

The signed H-cone pairs acyclically with the unknot-filling arc using only integral unit pivots. D_b, D_c, S^2 and H=D-S^2 have explicit integral null-homotopies. Signs matter: the all-plus integral lift does not have the same central null-homotopies over Q.

For tau=h^-3 q^-4 define

    L = a(0) + Q^- + hQ^- + tau Q^- + h tau Q^-.

The identities tau Q^- -> Q^- and h tau Q^- -> hQ^- have degree (3,4). The odd shifts reverse the internal differentials, so dD_3+D_3d=0 integrally, and D_3^2=0. Standard Koszul signs preserve this formal identity-cone collapse under additive closure pairings. N(L) is free of rank seventeen, has Euler polynomial one, and has cancelling quantum endpoints at q=-4 and q=10. Thus it violates NP and END over Q, C and every prime field.

This is a formal countermodel, not an actual tangle or an assertion about geometric Floer maps. It does not extend the earlier characteristic-two unreduced-dot formula to characteristic zero. The reproducible finite certificate `referee_checks/integral_ladder.py` was independently rerun by root and passed all checks. No knot scan was performed.

## 4. The characteristic-zero instanton sequence has a different target

Xie, *Instantons and annular Khovanov homology*, Adv. Math. 388 (2021), 107864, Corollary 1.2/Theorem 6.1, gives

    N_C(mirror T) => THI(T),

via the top annular weight, with no additional two-dimensional factor. THI is the singular instanton invariant of (I x D, gamma, T), the original sutured cylinder retaining T. It is not KHI(kappa) for the double branched cover. [Source](https://arxiv.org/abs/1809.01568); see also Xie–Zhang, [Definition 7.6 and Proposition 7.7](https://arxiv.org/abs/1907.00547).

This distinction is testable. For the doubled cut-open trefoil T_K, the covering knot is K#K, whereas Xie's Theorem 6.3 identifies THI(T_K) with I^natural(K), of rank at most three. Alexander categorification gives rank KHI(K#K)>=||Delta_K^2||_1=9. The proposed target identification is therefore false.

The sequence retains useful rank and braid detection: Xie's Corollary 4.11 detects braids by rank one for the indicated tangles. It does not supply the missing quantum endpoint restriction or a covering-knot KHI rank bound. Additional information about its *specified geometric maps* could matter; replacing those maps by arbitrary formal collapse maps would not distinguish the ladder.

## Disposition

Bank the genus-one rank-nine bound, the M1 restriction in the rank-five case, and the field lemma as genuine restricted reductions. Keep universal END/NP and the higher-genus rank-five realization problem OPEN. The new source checks give no justification for a renewed scan or for another unqualified scalar/rank mechanism.
