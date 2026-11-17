# Symmetry construction gate

2026-11-03. Bounded theory/literature pass; no enumeration. Parent task: can a global construction force useful symmetry while retaining only the ordinary Jones polynomial?

**Conclusion.** The elementary strong-inversion double works, but it does not enter Lemma Q. Two natural ways to improve it are obstructed: Conway mutation cannot make the composite double prime, and an amphichiral symmetric union with one twist region is necessarily the original connected sum. The color-3 appearance in the flipping quotient is structural, not a normalization accident. I found no new complete positive reduction.

## 1. The exact reduction and its wrong target

For any oriented knot J, let J^r denote orientation reversal, not mirror image. The knot D(J)=J#J^r admits the factor-exchanging strong inversion. This appears in the **published** Miller–Powell paper, Example 2.5(ii); the archive's Example 2.5(iii) is apparently a preprint numbering. Since Jones is orientation-insensitive and multiplicative,

    V_D(J) = V_J^2.

Thus ordinary Jones detection among strongly invertible knots implies ordinary Jones detection for all knots. Nontriviality is retained by prime decomposition. This reduction is correct, but is not a reduction to Lemma Q, whose polynomial belongs to a marked quotient tangle/inversion.

The archive `work/defect-calculus/sums.txt`, section 5, records

    H_(flipping J#J^r) = J_3(J),

where J_3 is reduced color-3 Jones, whereas ordinary Jones is J_2. The present pass did not redo that double-tangle calculation. Its scope is exactly the missing color-propagation gate; J_2=1 supplies no established J_3=1 implication.

Primary source: [Miller–Powell, Strongly invertible knots, equivariant slice genera, and an equivariant algebraic concordance group, JLMS 2023](https://londmathsoc.onlinelibrary.wiley.com/doi/full/10.1112/jlms.12732), Example 2.5(ii).

## 2. Why wrapping two produces color three

Work in the zero-framed Kauffman bracket skein of the solid torus over R=Z[A,A^-1], with core z and Chebyshev basis e_0=1, e_1=z, e_2=z^2-1. A pattern admitting a diagram cut into two strands has annular class

    P = a z^2 + b = a e_2 + (a+b)e_0.

After insertion around a companion J this evaluates to

    <P(J)> = a Delta_2 J_3(J) + (a+b),

up to the explicitly fixed framing normalization. This is the representation identity V_2 tensor V_2 = V_1 direct-sum V_3.

Consequently a universal *annular skein identity* for a two-strand operation cannot retain nonconstant ordinary-color-2 dependence: e_1 is in the odd parity summand, while the whole two-strand pattern lies in the even summand. Erasing e_2 erases all companion dependence in this setting. This is a rigorous skein-module obstruction; it is **not** a theorem that special relations between actual knots' colored Jones polynomials cannot exist.

A wrapping-three construction is the first parity-compatible alternative: its skein lies in span{e_1,e_3}. It would have to remove the e_3 sector while retaining e_1. The sibling satellite investigation covers that gate and its topological obstructions. A double formed from two independent connected-sum factors is not a single-companion two-parallel, so V_J^2 causes no contradiction with the parity statement.

## 3. Conway mutation cannot primeify the double

Conway mutation preserves the branched double cover. The cover of a composite nontrivial knot is reducible; conversely reducibility of a knot's branched double cover detects a connected-sum decomposition (equivariant sphere theorem). Therefore a Conway mutant of J#J^r, or J#mirror(J), remains composite whenever J is nontrivial.

This kills the proposed sequence “double to force symmetry, then Conway-mutate to become prime without changing Jones.” It does not exclude broader Jones-preserving operations. Paoluzzi's primary paper explicitly recalls both facts together in its introduction: [Cyclic branched covers of alternating knots (2020), p. 2](https://www.i2m.univ-amu.fr/perso/luisa.paoluzzi/alternating.pdf).

Genus-two mutation is a broader operation preserving colored Jones: [Dunfield–Garoufalidis–Shumakovitch–Thistlethwaite, Behavior of knot invariants under genus 2 mutation, NYJM 2010](https://nyjm.albany.edu/j/2010/16-7.html). The preceding branched-cover argument was not established for that operation in this pass. Equally, no theorem was found saying it universally forces primeness or strong inversion. It is an unproved construction gate, not a proposed proof route.

## 4. Symmetric unions: exact information loss, and a published no-go

The refined symmetric-union polynomial satisfies

    W_D(t,t)=V_K(t),
    W_D(-1,t)=V_J(t)V_J(t^-1),

where J is the partial knot. Thus knowing V_J=1 fixes one specialization of a two-variable polynomial and does not fix the Jones specialization. Algebraically, the missing information is the quotient in

    W_D(s,t)-1 = (s+1) Q_D(s,t)

when V_J=1 (in the Laurent ring appropriate to knot symmetric unions). Substituting s=t leaves (t+1)Q_D(t,t). Symmetry has introduced an extra quantity rather than eliminated one. Source: [Eisermann–Lamm, A refined Jones polynomial for symmetric unions](https://arxiv.org/abs/0802.2283), Propositions 5.9–5.10.

There was a genuine candidate here: impose amphichirality on a one-twist-region symmetric union, making Tanaka's functional equation force V_K=V_J(t)V_J(t^-1). It would preserve flatness and potentially produce a prime ribbon knot. But Köse proves that **every amphichiral one-twist-region symmetric union of J is J#mirror(J)**. So this exact mechanism provably gives no prime upgrade. [Köse, On amphichirality of symmetric unions](https://arxiv.org/abs/2111.08765), abstract and main theorem. This is stronger than merely observing that some examples fail.

Do not replace amphichirality by palindromicity of Jones without notice: palindromicity is a much weaker polynomial hypothesis, and arranging it while retaining nontrivial topology is another unknown gate. Nor does a symmetric-union diagram automatically give the orientation-preserving strong inversion required by Lemma Q.

## 5. Recommendation

Bank the two precise no-go statements as pruning facts. Do not spend a new cycle on the factor-exchanging double or on one-region amphichiral symmetric unions. A genuinely new symmetry route must specify a Jones-preserving operation beyond Conway mutation and the one-region construction, and explain **both** how it changes the topology and why it avoids additional color/sector data. No such operation was constructed here.

Statuses: literature assertions above are published; the wrapping-two parity argument is an explicit elementary proof; the archived H=J_3 identity remains at its prior project status. No scaffold status changed in this child task.
