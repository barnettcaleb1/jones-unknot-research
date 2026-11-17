# Physics/analytic design pass: no qualified new route found

Design only, no computation. My strongest attempted candidate was reflection positivity: turn Jones equality into an equality case of a Hilbert-space norm inequality, then use rigidity of the equality case. The exact normalization kills the naive version. I recommend reporting this honestly rather than promoting it as another route.

## Candidate and exact obstruction

For a 2m-strand plat and q=exp(2 pi i/r), write d=2 cos(pi/r). With a normalized cup vector v and a unitary Jones representation rho,

    |V_(plat beta)(q)| = d^(m-1) |<v,rho(beta)v>|.

This is [Wocjan–Yard, equation (5.39)](https://arxiv.org/pdf/quant-ph/0603069). Therefore V=1 imposes the overlap magnitude d^(1-m), not 1. For m>1 and d>1 this is an interior amplitude. Cauchy–Schwarz rigidity cannot apply: the unknot's high-bridge presentations already have precisely that interior overlap. The identity braid gives the m-component unlink and the SATURATING overlap 1. Thus the normalization error exchanges the knot of interest with the unlink.

The Thompson-group positive-type interpretation does not fix this. [Aiello–Conti, section 2](https://arxiv.org/pdf/1603.03946) normalizes an n-leaf tree pair by the unlink factor to power 1-n. Jones-triviality again does not make the positive-type function attain its identity value. Their positive-type construction is genuine; interpreting its unknot value as an extremal point is not.

Asymptotic faithfulness, quantum universality and the density of braid images do not repair this. Prescribing one interior matrix coefficient, even throughout an analytic parameter family, does not determine the operator. Example at the operator level: direct sums R(q) direct-sum U(q) retain a prescribed coefficient of R for arbitrarily nontrivial U. This example is not a braid/knot counterexample; it identifies the additional geometric theorem a braid-specific argument must supply.

## What would revive the candidate

A new **geometric saturation certificate** would have to construct, from a classical one-component knot diagram and using only its ordinary Jones polynomial, a positive operator Q_K whose trace is an explicitly nonnegative function of V_K, and whose zero space detects a compressing disk or an actual unknot isotopy. A possible global scalar is

    E(K) = (1/2pi) integral |V_K(exp(i theta))-1|^2 dtheta
         = sum_j (coefficient_j(V_K)-[j=0])^2.

This is an exact nonnegative INTEGER and uses all coefficients. However, taking Q_K to be the scalar E(K) is just a reformulation. What is missing is a local geometric positive decomposition whose equality case forces a disk. Doubling a signed state sum produces cross-terms and does not give that decomposition. No construction of Q_K with the requisite geometry emerged in this pass.

This candidate currently passes neither B1 nor B2: Hilbert-space positivity alone has no reason to distinguish one-component classical diagrams from links or virtual diagrams. Any future certificate must use the component condition and actual planar/three-dimensional disk geometry before applying positivity. Merely introducing the energy E or a doubled tensor network is not progress on the missing bridge.

## Judgment

There is no fresh physics mechanism here strong enough to put on the scaffold. The useful conclusion is a precise normalization check that rules out a family of attractive but invalid arguments. The existing planar-projection route is more substantive because it has an actual additional classical equation P^2=P; the proposed positive-operator route does not yet have comparable input.
