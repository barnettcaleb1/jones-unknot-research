# Characteristic zero, universal coefficients, and the signed ladder

16 November 2026. Referee of Claude235059, item4. This report concerns
formal Bar–Natan complexes and the integral augmentation. It does not
identify an actual tangle with a formal ladder or identify any invented
higher differential with an instanton differential.

## 1. What the universal-coefficient pair means

The homological convention here is cohomological: the differential raises
h by1. For a finite complex C of free bigraded abelian groups, universal
coefficients gives

    0 -> H^{h,q}(C;Z) tensor F_p
      -> H^{h,q}(C tensor F_p)
      -> Tor_1(H^{h+1,q}(C;Z),F_p) -> 0.

Thus a Z/p^e summand in integral cohomology at(h,q) creates one mod-p
copy at(h,q) and another at(h-1,q). Its contribution is
h^{h-1}q^q(1+h). The exponent e does not change the number of copies.
This follows equally from the elementary free two-term complex with
differential p^e; it needs no knot-specific theorem.

The converse is false. Two independent integral free summands in adjacent
homological gradings have the same mod-p dimension profile and persist
over Q. Therefore a factor(1+h), by itself, does not diagnose torsion.
If the same equal-quantum adjacent-h classes actually persist over Q,
they cannot be explained solely by 2-primary torsion. This agrees with
the scope of Claude's stated9_2 field comparison; that dataset has not
been recomputed in this pass.

## 2. A field reduction for NP and END

This is the root agent's additional observation, checked here. Apply the
integral augmentation to the integral Bar–Natan tangle complex and call
the resulting finite free complex C_b(T). This definition commutes with
coefficient extension; it does not assume the immersed-curve decomposition
is independent of the field. Put N_k=H(C_b tensor k).

Let b_{h,q}=dim_Q N_Q^{h,q}, and let t_p(h,q) count the p-primary cyclic
summands of H^{h,q}(C_b;Z). Then

    dim_Fp N_Fp^{h,q}=b_{h,q}+t_p(h,q)+t_p(h+1,q).

In particular the rational bigraded support is contained in every
positive-characteristic support. Their integer Euler polynomials are
identical: the two torsion contributions have opposite h-parity.

Assume N_Q is nonzero, as it is in the intended unknot-cap setting.
If END holds over F_p, the two quantum endpoints are nonzero coefficients
of the common Euler polynomial. They therefore lie in rational support.
Since rational support is contained in F_p support, both endpoint degrees
coincide between the two fields. The endpoint Euler coefficients are the
same, so END holds over Q.

If NP holds over F_p, each endpoint is concentrated in one homological
degree, so its Euler coefficient is nonzero. The preceding argument makes
the endpoint degrees agree, and the rational endpoint support is a subset
of a single homological degree. Hence NP holds over Q as well.

Only finitely many primes divide integral torsion. Away from those primes,
N_Fp and N_Q have exactly the same bigraded dimensions. Consequently, for
either property P in {END,NP},

    P over Q  <=>  P over some prime field
              <=>  P over every sufficiently large prime field.

In particular failure over Q forces failure over every F_p. Failure at
one exceptional prime, such as2, need not force rational failure. This is
a genuine field reduction, but supplies no noncancellation mechanism by
itself. No analogous field-independence of individual curves, their types,
or local systems is being asserted.

## 3. The compact component exists integrally; signs matter

Use the quiver algebra B_Z with two idempotents, arrows S, loops D, and
relations DS=SD=0. This is defined over a commutative unital ring in
Kotelskiy–Watson–Zibrowius, *Immersed curves in Khovanov homology*,
[arXiv:1910.14584v2](https://arxiv.org/abs/1910.14584v2), Definition4.19 and
Theorem4.21. Their §2.1 gives the cohomological and Koszul-sign conventions;
§4 identifies the algebra with the formal universal cobordism category.
The characteristic-zero central parameter is H=D-S², not D+S².
The primary TeX of those sections was inspected.

Take the banked12-generator Q with idempotents

    b,c,c,c,c,b,b,c,c,c,c,b

and the same graded arrows as in bare_b_closure_referee.md. Lift all arrow
coefficients to+1 **except** the D arrow1->12, whose coefficient is-1.
Every length-two composable arrow product contains DS or SD, so d_Q²=0
term by term over Z, without any characteristic-two cancellation.

The augmentation N_Z(Q) is free of rank4 at

    (h,q)=0,(1,2),(5,8),(6,10).

It is therefore not a source of purely mod-two universal-coefficient
classes. Q and hQ remain nonzero formal objects over Q and C.

The local sign is substantive. With all coefficients+1, rational D_b and
H actions are not null-homotopic, although they are in characteristic2.
With the single minus sign just specified, exact integral linear algebra
gives homogeneous null-homotopies for D_b,D_c,S² and H, with respectively
6,4,6 and16 nonzero terms. Thus a correctly signed characteristic-zero
lift retains the relevant central-annihilation property.

The signed H-cone has source differential-d_Q, target differential+d_Q,
and off-diagonal map H=D-S². Pairing with the infinity arc c gives an
acyclic complex. The independent finite calculation uses only integral
unit pivots and verifies the stable zero tails, so this acyclicity is
integral, not merely rational. In particular the compact additions do not
change the formal unknot cap.

All these assertions have the reproducible exact certificate
`referee_checks/integral_ladder.py`. It checks the fixed object only; no
knot enumeration or parameter sweep is involved.

## 4. One signed characteristic-zero ladder is enough

To avoid any unnecessary even-page sign discussion, choose the gap-two
ladder and use the standard cochain shifts:

    tau=h^-3 q^-4,
    L=a(0) + Q + hQ + tau Q + h tau Q.

The differential on tau Q is-d_Q and that on Q is+d_Q. The underlying
identity tau Q->Q has degree(3,4). Likewise h tau Q->hQ has degree(3,4),
with the two internal signs reversed. Let D3 be these two identities and
zero elsewhere. Then

    D3²=0,       dD3+D3d=0

over Z: the off-diagonal cancellation is d_Q-d_Q, not2d_Q. Thus d+D3
squares to zero. Both summands have delta-degree-1, and D3 has filtration
degree3, giving a formal page-three collapse of the extra summands.

Because3 is odd, the ordinary cochain Koszul rule also supplies the needed
anticommutation with the differential of any filling factor. Additive
graded closure pairings preserve the signed identity-cone construction.
On homology the extra copies cancel to the rational closure. Filling-side
maps obey the usual graded naturality; no characteristic-two sign
suppression is needed for this example.

N(L) has rank17 over Z, Q and every prime field. Its quantum extrema are
q=-4 at h=-3,-2 and q=10 at h=6,7. Both endpoint Euler coefficients
vanish, and its full Euler polynomial is1. NP and END therefore fail in
characteristic zero just as they do mod2. The adjacent-h summands here
are independent free classes, not universal-coefficient torsion shadows.

This does not establish a signed integral classification of all curves,
mapping-class naturality over every field, or the characteristic-zero
version of the earlier unreduced-dot algebra section. Those separate
claims are unnecessary. It does establish that simply changing the
coefficient field does not remove every formal ladder, even with the
unknot-cap and central-annihilation calibration retained.

## 5. What the instanton route would have to add

Characteristic-zero instanton theory may impose a genuinely new target,
grading, or geometric-map constraint. That is being audited separately.
Its usefulness cannot rest solely on interpreting(1+h) as2-torsion or on
the availability of characteristic-zero coefficients: the signed formal
ladder already has rational free classes and compatible formal collapse.
An instanton argument must distinguish its specified geometric structure
from that example.
