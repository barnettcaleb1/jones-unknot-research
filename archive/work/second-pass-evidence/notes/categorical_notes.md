# Actual categorical constraints: bounded second pass

Investigated 31 October 2026, approximately 16:57–17:16 UTC. This is an audit and a restricted calculation, not a proof of Jones unknot detection.

## What the geometry genuinely supplies

Work with reduced Khovanov tangle curves over F2, with quantum grading q and homological grading h, and delta = q/2 - h. For a four-ended tangle T with an **actual** unknot filling T(infinity), immersed-curve gluing and rank-one unknot homology force

    Kh_curves(T) = r_1(k) union s_(2n_1)(infinity) union ... union s_(2n_m)(infinity).

There is one rational component and all special components are parallel to the unknot filling. A nonrational tangle has m > 0. This is much stronger than arbitrary nonnegative bigraded vector-space data. It follows because the total minimal intersection number with the infinity filling arc is one; any nonparallel special component would already contribute more than one. Rational tangles are detected by having exactly a single r_1 component.

Sources: [Kotelskiy–Watson–Zibrowius, Theorem 3.1](https://arxiv.org/abs/2104.13592); [Kotelskiy–Lidman–Moore–Watson–Zibrowius, Theorem 2.6, Lemma 2.10 and the proof in Section 4](https://pmc.ncbi.nlm.nih.gov/articles/PMC11139753/). The latter gives dim HF(a_s,gamma) = length(gamma) * slope_distance(s,gamma) for distinct slopes.

This suggests a concrete proof target: show that the special components required by a nonrational tangle cannot supply exactly the graded Euler polynomial needed to imitate the chosen rational tangle. But the word **actual** in the unknot-filling hypothesis cannot be replaced by “has Jones polynomial one.”

## The exact equation, and a useful computable certificate

Pair with a transverse filling arc a_0. Let E_R(q) be the graded Euler polynomial of HF(a_0,r_1(k)), and E_S(q) that of the sum of pairings with the special components. Then

    E_T(q) = E_R(q) + E_S(q).

To imitate a target rational tangle, its consistently graded filling polynomial E_target must therefore satisfy

    E_S(q) = E_target(q) - E_R(q).

**It is not legitimate to set E_S = 0 before proving that the rational component has the target slope and absolute grading.** The unknot filling does not establish that additional fact. In particular k need not be zero.

There is an exact certificate when the special pairings decompose into the four-dimensional blocks V used in the published computations. V has delta grading zero and q gradings -5,-1,1,5. A shifted block h^a delta^b V has

    E_block(q) = (-1)^(a-5/2) q^[2(a+b)-5] (1+q^4)(1-q^6).

Indeed its homological gradings are a-5/2, a-1/2, a+1/2, a+5/2, with signs +,+,-,- relative to the first. Thus for a finite collection of shifted blocks,

    E_S(q) = (1+q^4)(1-q^6) B(q),
    B(q) = sum_i (-1)^(a_i-5/2) q^[2(a_i+b_i)-5].

Since the Laurent polynomial ring is an integral domain, E_S is zero **if and only if** B is zero. Complete cancellation requires an exactly balanced signed count at every block-center quantum grading. This is a stronger and cheaper certificate than examining a large expanded polynomial. A unique extreme center, or same sign at every occurrence of an extreme center, rules out complete cancellation.

This factorization applies to the s_4n special-curve class: Lemma 2.5 of the strong-inversions paper decomposes their pairings into such blocks. The 2022 paper verifies s_4 for its tabulated strong inversions through nine crossings. Divisibility of all special lengths by four is posed there as Conjecture 3.10; it must not be silently assumed for arbitrary tangles. Even in this class, no theorem found here forces B to be nonzero or prevents it from matching the nonzero target difference above.

The finite center criterion is our direct algebraic consequence of the published block description, not a new claimed knot theorem. It can guide a search: compute actual tangle curves, compare B with (E_target-E_R)/[(1+q^4)(1-q^6)], and only retain exact matches. Realizability and the rational component still matter.

## Stress test with an actual tangle: figure-eight strong inversion

The published absolute bigrading for one strong inversion of the figure-eight is

    kappa(4_1,h_1) = h^(5/2) delta^(11/2) V
                    direct_sum h^(13/2) delta^(9/2) V.

See [Kotelskiy–Watson–Zibrowius, p.238](https://msp.org/obs/2022/5-1/obs-v5-n1-p10-s.pdf). Converting from h,delta to q gives the following actual special-pairing data:

| Block | (h,q) gradings | Euler polynomial |
| --- | --- | --- |
| First | (0,11), (2,15), (3,17), (5,21) | q^11 + q^15 - q^17 - q^21 |
| Second | (4,17), (6,21), (7,23), (9,27) | q^17 + q^21 - q^23 - q^27 |

The groups at quantum gradings 17 and 21 are nonzero and cancel exactly in Euler characteristic. Thus actual geometric special curves do exhibit opposite homological parity at a common quantum grading. Positivity, linearity of the underlying curves, and the presence of an unknot filling do not remove the cancellation issue.

Here B(q)=q^11+q^17 is nonzero, so the total special contribution is q^11+q^15-q^23-q^27, not zero. This is a stress test against an overstrong positivity claim, not a counterexample to the needed complete-cancellation assertion and not a Jones-one knot.

## Stress test with actual knots: even the outer quantum grade can cancel

Bar-Natan's original rational Khovanov calculation gives different homologies for 5_1 and 10_132, with the same Jones polynomial. In his convention, the highest quantum grade of Kh_Q(10_132) is q=-1 and consists of a generator at h=0 and another at h=-1. They cancel in the Euler polynomial. Its Khovanov rank is 12, whereas that of 5_1 is 6. The common unreduced Euler polynomial is

    -q^-15 + q^-7 + q^-5 + q^-3.

Source: [Bar-Natan, AGT 2 (2002), p.356, Out[21]–Out[23]](https://arxiv.org/pdf/math/0201043). This explicitly defeats the generic plan “take an extremal nonzero Khovanov group; its Jones coefficient cannot cancel.” The arithmetic in both stress tests is independently checked by `categorical_checks.py` and recorded in `categorical_checks.json`.

## Scope: the rational-tangle reduction does not make the generic problem easier

[Sikora, Theorem 9.2](https://www.cambridge.org/core/journals/canadian-journal-of-mathematics/article/tangle-equations-the-jones-conjecture-slopes-of-surfaces-in-tangle-complements-and-qdeformed-rationals/B90AFE6265D3B2D6AF806F9407B9987F) proves that the full Jones unknot conjecture is equivalent to: a framed tangle with bracket vector (1,0) is the trivial zero tangle. It is also equivalent to bracket detection of every rational tangle. Therefore, asserting that bracket equality forces the above categorical rationality would itself contain the missing theorem.

There is a further genuine restriction in the proposed geometric approach. A hypothetical Jones-one knot K can be tied locally into one strand of the zero tangle; the resulting tangle has vector (1,0). Every knot closure retains K as a connected summand. If K is nontrivial, no such closure is an actual unknot. Thus the useful actual-unknot-filling geometry is not a general reduction of an arbitrary potential Jones-one knot.

## Small universal consequence, independently of the tangle route

Any nontrivial knot with Jones polynomial one must have reduced rational Khovanov rank at least five. Rank one detects the unknot; rank three detects a trefoil; the total rank is odd because its Euler characteristic at q=1 is one. A trefoil does not have Jones polynomial one. Consequently there must be at least two even/odd cancellation pairs, counted with multiplicity, beyond the single net generator.

The rank-three input is [Baldwin–Sivek, Theorem 1.4](https://spiral.imperial.ac.uk/server/api/core/bitstreams/7b5272d0-9002-4fab-a986-d202149ab926/content), where the integral rank is the rational dimension. Over F2 the reduced rank is at least this large, and unreduced Khovanov rank is twice reduced rank, so it is at least ten. This constrains actual candidates but provides no contradiction.

## Assessment

The worthwhile next categorical target is a **realizability theorem controlling the signed block centers and the rational component for actual tangles**. The explicit identity above states what it would have to accomplish. Underlying curve linearity and positive dimensions alone cannot do so, and actual examples invalidate the easiest no-cancellation claims. No result in this pass closes that gap. For a bounded search, this machinery is best applied to tangles already having an actual unknot filling; presenting that special sector as a solution to the arbitrary-knot problem would be circular or incomplete.
