# A cyclotomic covering comparison and the third moment

16 November 2026. Codex synthesis of the order-three symbol, bulk BMW, and
annular-boundary audits. **PROVED under the collaboration protocol:** Claude's
224805 report and two independent adversarial referee reports accept the
proof with the convention and framing repairs incorporated below. External
specialist review and a priority audit have not been completed. It supersedes
the *remaining boundary gap* in
`degree3_modfive_route.md`, rather than treating a principal-symbol comparison
as an equality of invariants. No knot scan is used.

## Statement

For a strongly invertible knot `(K,h)`, write `J_+=J_lp` for the invariant
computed by `mont/lp.py`: its quotient bracket variable is `t=A^4`, and its
preferred normalization is `J_+(-1)=1`, `J_+'(-1)=0`. The ordinary Jones
polynomial uses its standard variable `a^-4` and normalization `V_U=1`.
The identity in these conventions is

    J_+(K,h;t) = V_K(t^2)  modulo Phi_10(t),
    Phi_10(t)=t^4-t^3+t^2-t+1.                         (C)

If both invariants are instead written in a uniform inverse-fourth-power
bracket convention, put `J_-(t)=J_+(t^-1)`. The same theorem then reads

    J_-(K,h;t) = V_K(t^-2) = V_(K*)(t^2) modulo Phi_10(t).

Below, unadorned J and M_k retain the **lp convention**. In particular the
saved numerical M_3 and iota tables are not being re-signed. Under the
uniform convention, `M_k^-=(-1)^k M_k^+`, so its cubic congruence is
`M_3^-/36=-7v_3 mod5`, and its integral residual
`(M_3^-/36+7v_3)/5` is `-iota_+`.

In particular this cyclotomic value forgets the choice of inversion. Since
`Phi_10(t)=(t+1)^4 mod 5`, (C) gives the complete cubic jet

    J(-exp(h)) = V_K(exp(2h)) modulo (5,h^4).

It follows that

    M_3/36 = 7 v_3(K) modulo 5.

Thus `iota=(M_3/36-7v_3(K))/5` is integer-valued. This does not identify iota
with a familiar invariant or provide nonvanishing of J. It fixes the entire
lower-order residual of the modulo-five comparison.

## 1. Conventions and two framed bulk evaluations

Fix the color-one axis to be straight and zero-framed throughout the raw
comparison. An axis kink would contribute `-A^3`, which is not a rational
function of `A^4`; it is excluded from this chosen raw gauge. Both brackets
use the same crossing rule, type x = `A keep + A^-1 cup-cap` and type y its
inverse. The quotient map preserves off-axis crossing types: a type-x
crossing and its two lifts carry the same letter. With quotient `t=A^4`,
choose the cover bracket variable a so that `a^2=Q=-A^-4`; for example
`a=i A^-2`. Consequently the cover Jones variable is `a^-4=t^2`. This
fixes the chirality of the comparison, not only its loop values.

Put `Q=-t^-1`. The original color-two theory has generic braid eigenvalues

    Q, -Q^-1, Q^2,

where the last is on the contraction line. Its loop and twist parameters are

    d_- = 1-Q-Q^-1,       r_- = Q^-2.

The double cover pairs two fundamental ordinary Jones strands, at quantum
parameter Q; its ordinary Jones variable is `Q^-2=t^2`. Its vector braid is
the product of the two fundamental braidings. The eigenvalues are

    Q, -Q^-1, Q^-3,

and the loop and twist parameters are

    d_+ = (Q+Q^-1)^2,     r_+ = Q^3.

These are actual Dubrovnik/BMW skein evaluations, not merely lists of
eigenvalues. In either case the contraction E is coevaluation followed by
evaluation, E^2=d E, and acts only on the contraction line. The braid relation

    B-B^-1=(Q-Q^-1)(I-E)

is verified on the three fusion channels; the two middle SO(4) summands have
the same eigenvalue and cause no exception. The duality and curl relations
give the displayed loop and twist. These identities hold generically, hence
specialize wherever the displayed local maps are regular. Equivalently they
are exact Temperley–Lieb identities for the two-cable projector
`f_2=1-e/delta`, whose denominator is nonzero at the primitive-tenth-root
specialization. The singular FT lattice near t=-1 is not needed here.

Exactly,

    r_+-r_-=Q^-2(Q^5-1),
    d_+-d_-=Q^-2 Phi_5(Q).                            (1)

Thus at any primitive fifth root Q both evaluations factor through the SAME
framed annular Dubrovnik skein. No equivalence of the full quantum categories
is being asserted.

## 2. Only annular generation is required

The Dubrovnik skein of the annulus is generated, as an algebra, by the positive
cycle closures A_n, n>=1: A_n is the annular closure of
`sigma_1 ... sigma_(n-1)` with every crossing of **type x**. Both functionals
are evaluated on this same family. Either the type-x or type-y family spans;
switching a representative gives the other plus fewer-crossing terms, but
their individual generator values must not be interchanged. Contractible
loops are replaced by d. This is the
generation part of Turaev's annulus theorem; see V. G. Turaev, *Conway and
Kauffman modules of a solid torus*, J. Math. Sci. 52 (1990), 2799–2805, and
A. T. Pokorny, *Dubrovnik Skein Theory and Power Sum Elements* (2021), Section
2.4, printed pp.27–28, for the statement and descending-diagram argument.
Source: https://escholarship.org/content/qt0dx137gc/qt0dx137gc.pdf .

Only spanning is used. Crossing changes give the descending diagrams plus
terms with fewer crossings, and descending components give these cycle
closures and framing powers. No primitive-idempotent expansion or division
by a vanishing quantum integer is required. In particular no independence
claim at the specialized root is needed.

An annular diagram acts on the simple original color-one axis by a scalar.
Nested annular multiplication is composition of those endomorphisms, so the
reduced-axis scalar is multiplicative. On the cover side annular products
can be separated by spheres meeting the branch axis twice. Each sphere lifts
to a sphere; the lifted links are split, and their absolute framed evaluations
multiply. Thus equality on all A_n and on the contractible loop proves
equality on every closed annular diagram.

## 3. Original values on all generators, with framing

Write T for the positive mixed full twist in the FT gauge (the halfword Y is
T^-1). Its eigenvalues on V_1 and V_3 inside V_1 tensor V_2 are

    Q^2, -Q^-1.

Their reduced quantum trace weights are respectively

    1, [4]/[2]=-(Q+Q^-1).

Hence the closure of T^n with the axis reduced has value

    L_n^- = Q^(2n) - (Q+Q^-1)(-Q^-1)^n.              (2)

The two components of this mixed closure are the parallel unknots of
T(2,2n). Their annulus identifies the moving curve, on the boundary of the
axis neighborhood, with `lambda_axis+n mu_axis`. In the exterior solid torus
this is the `(n,1)` curve, namely A_n. This uses the zero longitude of the
designated unknot, so the identification is marked, not just a winding count.
In the mixed diagram all crossings are between different components, giving
moving-component self-framing zero. A_n has n-1 positive self-crossings.
Consequently

    E_-(A_n)=r_-^(n-1) L_n^-.                        (3)

## 4. Cover values on the same generators

Let B be the fundamental positive braid, with eigenvalues Q^(1/2) on the
triplet and -Q^(-3/2) on the singlet. The singlet and triplet quantum trace
weights are 1 and `Q^2+1+Q^-2`. Define, for this generator calculation,

    T_fold=-Q^(-3/2) B.

It has eigenvalues Q^-3 and -Q^-1 on the singlet and triplet respectively,
giving

    L_n^+ = Q^(-3n)+(Q^2+1+Q^-2)(-Q^-1)^n.          (4)

The framing check is essential: (4) is not silently being substituted for a
raw braid trace. The double lift of A_n is the closure of
`(sigma_1 ... sigma_(n-1))^2`, hence T(n,2)=T(2,n). The former diagram has
2(n-1) crossings, the latter n. Their ribbon framings differ by n-2 positive
curls. The fundamental bracket curl is `theta_U=-Q^(3/2)`, so the actual
pullback-framed evaluation is

    theta_U^(n-2) Tr_q(B^n)
      = Q^(3(n-1)) Tr_q(T_fold^n)
      = r_+^(n-1) L_n^+.                            (5)

This includes n=1: the negative curl correction removes the curl in the
two-strand presentation of the unknot. For n=2 it is the raw Hopf evaluation.
Thus E_+(A_n) in (5) is the actual covering-link evaluation. A full mixed
defect ribbon category need not be constructed to establish its values on
this spanning set.

For the relative projector step below, one also needs the same chirality and
framing of T with arbitrary outside tangle. Type preservation under the
quotient map gives the type-x lift of A_n as the type-x cycle braid squared.
Since the moving component of the T^n closure is the zero-framed A_n, its
lift has trace `Tr(T_fold^n)` for every n; reversing B would instead give
eigenvalues `(Q^3,-Q)`, incompatible with `(Q^2,-Q^-1)` at fifth roots.
Thus the local crossing is B, not B^-1. Each lifted strand carries a relative
half twist; only their integral total k enters as the ribbon factor
`theta_U^k`. Closing the identity fixes the closure gauge (two zero-framed
unknots). Closing T gives the meridian, whose lift is the zero-framed unknot,
whereas closing B includes one curl. Hence k is exactly -1 and the
local framed operator is `theta_U^-1 B=-Q^(-3/2)B=T_fold`. This establishes the
operator needed in (8), not just a coincidence of its closed traces.

Now

    L_n^- - L_n^+
      =Q^(-3n)(Q^(5n)-1)
       -Q^-2 Phi_5(Q)(-Q^-1)^n.                     (6)

Both (6) and the ratio `r_+^(n-1)/r_-^(n-1)=Q^(5(n-1))` vanish or become one
at a primitive fifth root. Equations (1)–(6) therefore identify E_- and E_+
on the entire closed annular skein.

## 5. Eliminate the vertices for an arbitrary quotient theta curve

This step does not assume a necklace, a rational body, or a braid of fixed
width. Take a regular-neighborhood ball of one full color-one edge of the
theta graph and its two vertices. It meets the remaining graph in four
points of colors 1,2,1,2. Bending in the fixed marking identifies its inside
tangle with the attached-channel projector P_1=ip, pi=Id. Its complement is
an arbitrary colored tangle A. Cyclicity of the generic pivotal trace gives

    reduced Tr(A P_1)=pAi.

The original projector can be eliminated by

    P_1=(T+Q^-1 I)/(Q^2+Q^-1).                     (7)

Both resulting closed diagrams have an unknotted color-one component: the
identity reconnects the original axis, and the mixed full twist cannot knot
that component on its own. They are the closed annular diagrams to which
Section 4 applies.

Under the double cover, the vertices lift to the fundamental cup and cap.
Their normalized composition is the singlet projector P_0; its trace is one,
so it supplies precisely division by the unknot value on the knot side.
For the folded central crossing in the same marking,

    P_0=(T_fold+Q^-1 I)/(Q^-3+Q^-1).                (8)

The bending scalar is fixed by pi=Id on both sides, not independently for
different closures. At Q^5=1, (7) and (8) have the same coefficients.
Their denominators are nonzero; `Q^2+Q^-1=Q^-1(Q^3+1)` is a cyclotomic unit.
It follows that the two RAW reduced theta/cover evaluations agree at every
primitive fifth root.

This uses generic trace identities followed by regular specialization. It
does not divide by the original color-one quantum dimension at t=-1.

## 6. Preferred framing, including the lower-order terms

One still has to remove the raw ribbon units. This cannot be omitted: an
unspecified monomial would not imply (C) in its preferred normalization.

Call the raw evaluations F(Q),G(Q). The banked theta skein identification
gives F as a signed integral Q-power times J(t); the folded cup/cap
identification gives G as a signed integral Q-power times V_K(Q^-2).
Here integer exponents can be proved without a parity assumption on an
arbitrary diagram: the annular evaluation formulas and (7),(8) put both F and
G in Q(Q). Their ratios to J and V are already known ribbon monomials in a
root of Q. Such a monomial lies in Q(Q) only when its exponent is an integer.
Retain both raw signs: `F(1),G(1)` lie in `{1,-1}`. Their signs are not fixed
by importing the differently gauged FT root evaluation. The preferred scalar
normalizations are

    Q^(-F'(1)/F(1)) F(Q)/F(1),
    Q^(-G'(1)/G(1)) G(Q)/G(1).                     (9)

These raw identifications now show that F and G are integral Laurent
polynomials. Their equality at primitive fifth roots, proved above, and
monicity of Phi_5 give by Gauss's lemma

    F-G=Phi_5(Q) R(Q)

with R an integral Laurent polynomial. Evaluating at one first gives
`F(1)-G(1)=5R(1)`. Its left side lies in `{0,2,-2}`, so it is zero. Write
`F(1)=G(1)=epsilon` with `epsilon=+-1`; then R(1)=0. No independent sign
adjustment has been made after establishing the raw congruence.
Differentiating gives `F'(1)-G'(1)=5R'(1)`. Thus the difference of the framing
exponents is `(F'(1)-G'(1))/epsilon=5R'(1)/epsilon`, a multiple of five.
Their correction factors and their common sign division in (9) therefore
agree at Q^5=1. This proves the preferred congruence (C).

Equivalently, the full integral annular calculation can be retained modulo
`(5,(Q-1)^4)`: (1) and (6) vanish to order at least four and the twist-factor
differences to order at least five. The new boundary denominators have value
2 at Q=1. Then F'(1)=G'(1) mod5, the signs agree, and (9) preserves the complete cubic jet. The
Gauss-lemma argument above avoids needing an integral basis theorem at the
nonsemisimple point Q=1.

## 7. Cubic coefficient and the surviving new invariant

Using V'(1)=0 and the conventions in the earlier reports,

    V_K(exp(2h))=1-12a_2 h^2-48v_3 h^3+O(h^4),
    J(-exp(h))=1-12a_2 h^2+(M_3/6) h^3+O(h^4).

The complete jet comparison gives

    M_3/36 = -8v_3 = 7v_3  modulo5.

Every denominator here is prime to five; M_3/36 is already integral by
ROOTS. Thus iota is an integer-valued, primitive, mirror-odd equivariant
invariant of order at most three. The supplied 9_9 pair proves it is not a
function of the covering knot, its full Sakuma eta polynomial, and j.
Consequently this is an arithmetic identification of the modulo-five
residue, not a complete geometric identification of iota.

## Fifth-root necessary condition

If J=1, then `V_K(omega)=1` for every primitive fifth root omega: the map
`t -> t^2` sends the primitive tenth roots bijectively to the primitive fifth
roots. This condition is unchanged on using J_- instead. Together with the
banked necessary condition a_2(K)=0, it is a further restriction on a flat
nonrational quotient. Neither condition, nor their conjunction, is asserted
to detect the unknot universally. Finite sample counts are not a proof of
sufficiency.

## Verification and scope

The associated fixed certificate verifies the parameter, trace, framing and
projector algebra and the exact cyclotomic remainder on the already named
trefoil, figure-eight, both 9_9 inversions and 8_19. Examples are calibrations;
the all-pattern claim rests on annular spanning and the marked vertex
replacement, not extrapolation from them. Prior novelty has not been checked.
The independent audits are `degree3_annular_closure_audit.md`,
`degree3_weight_comparison.md` and `degree3_modfive_route.md`.

This result is one finite cyclotomic restriction. FT-DEEP continues to rule
out a universal finite initial-moment detector. No progress toward global
nonvanishing is claimed from this congruence alone.

The initial internal referee files are `degree3_annular_closure_audit.md`,
`degree3_cyclotomic_referee.md` and `degree3_coefficient_framing_audit.md`.
Claude224805 then supplied two independent adversarial reads,
`/Users/calebbarnett/jones-lanes/theory-restart/mont/ft/referee/cyc10_annular.md`
and `cyc10_projector.md`, both STANDS_WITH_REPAIRS. This revision incorporates
their explicit variable convention, type-x generator family, chirality,
zero-framed axis, total lifted twist and common-sign normalization repairs.
Their additional exact/random checks are reported evidence, not computations
rerun for this revision and not the basis of the universal proof. Status is
now PROVED under the collaboration protocol; external specialist review and
novelty remain unchecked.
