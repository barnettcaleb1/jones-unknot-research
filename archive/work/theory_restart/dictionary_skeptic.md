# Upstream skein dictionary: independent scope and normalization audit

17 November 2026. Read-only audit for Claude050833. No numerical checks,
scripts, or scans were run. This note identifies the step the completed
proof must supply; it does not promote the engine's downstream topology or
novelty assertions.

## 1. Exact definitions in the implementations

`tools/flat_search.py` constructs the quotient tangle, before the preferred
framing twists, in the boundary basis

    b=(03)(12),  c=(01)(23),  [T]=y b+x c.

Its unknot cap evaluates to `u=y+delta x`. `mont/lp.py::J_raw` checks that u
is a signed Laurent monomial and returns y/u, using t=A^4. `lp.J` then applies
`normalize`, the unique signed t-power making the value at -1 equal1 and the
derivative there equal0. Thus neither a fitted normalized closure nor a raw
theta evaluation may silently be substituted for the preferred J.

`engineC2/theta.py` uses the color-(1,1,2) theta graph, with ONE f2 on the
connected color-two edge. Its raw evaluator computes

    delta <Theta> = delta <D> - <D_e>,

and divides by the same quantity for the planar theta. It then performs the
same preferred normalization. The factor and marking must be proved before
using the reported sample agreement as a theorem.

## 2. Noncircular local extraction

The sufficient diagram statement is exact: in the fixed boundary marking,
the plain theta cable closes T with b and the single f2 turnback closes it
with c. The two closure functionals are

    L_b(T)=delta^2 y+delta x,
    L_c(T)=delta y+delta^2 x.

Consequently

    <Theta>=L_b(T)-delta^-1 L_c(T)=(delta^2-1)y,
    <Theta_0>=delta^2-1,
    <Theta>/<Theta_0>=y.

This is independent of the contents of T. Rotating b to the TL2 identity
and c to e gives the equivalent formula tr(f2 T)=Delta2*y. The missing
geometric sentence is to identify the band-boundary construction of T with
these two closures. It can be proved before any state expansion using a
regular neighborhood of the distinguished arc; it is not a hypothesis about
where an arbitrary turnback travels through an arbitrary diagram.

The existing `twobridge_geometry_referee.md` Section2.1 states the projector
extraction and then calls it the quotient invariant. The new proof should
make this marking explicit instead of using that abbreviated identification
as an independent premise. Once it is written, the contents can be an
arbitrary nonrational box: no two-bridge property enters the local identity.

The elementary Morse replacements are independently visible in source:
`flat_search.quotient_word` replaces an off-axis crossing with its four-strand
cable and an axis letter with the four crossings of the mixed full twist.
`theta.from_halfword` does the same before cable expansion. This is a useful
marking check, not a numerical proof. Their initial/final cup patterns are
the planar closure comparison above.

## 3. What must be kept separate

1. The coefficient extraction gives raw y. Divide by the actual cap unit u
   and account for the preferred longitude marking to get J. All closures
   used to reconstruct a state require ONE common raw framing. Independently
   normalized scalar closures do not determine relative state phases.
2. Color2 means V2, the three-dimensional/spin-one object. Do not use
   “spin2” if it could be read as the five-dimensional object V4.
3. A generic colored box has state aP1+bP3 because End(V1 tensor V2) has
   two multiplicity-one summands. Bending then identifies its state with H.
   This is independent of whether the body lies in a two-bridge presentation.
   Rational words merely generate a special orbit in that same space.
4. Integrality of normalized v2 is stronger than generic recoupling. The
   projected TL3 proof in `necklace_skein_referee.md` Section2 uses raw a
   being Laurent, then delta divisibility of the e1 coefficient, then the
   extra factor1-t from the crossing-change evaluation at A=1. It is sound
   only after the raw-a/J dictionary has been supplied, so do not present it
   as a premise proving that same dictionary.
5. At t=-1 use the regular s-lattice, not specialization of f2=1-e/delta.
   The latter is singular. The generic identity proved first can be
   transported to the regular model and only then specialized.
6. The body hypotheses matter: one straight axis strand, one connected arc
   strand, the fixed through-through marking, and no extra closed component.
   A disjoint color-two loop could change the root scalar and invalidates
   the claimed epsilon dichotomy as stated.

## 4. Root-sign proof requirement

The regular root model identifies the color-one fusion summand with
V1 tensor the even state w1; the complementary color-three summand is the
four-dimensional odd sector. A credible all-body sign argument must show
that after the common scalar normalization the even sector has value1 and
the odd sector has value(-1)^(axis winding). Merely checking rational words
does not prove that statement for arbitrary bodies.

A possible topological route is available: the straight-axis complement
in the box is a solid torus, and a single through arc is classified up to
relative homotopy by winding. A generic such homotopy is isotopy plus
self-crossing changes. The regular root crossing equals its inverse, and
the color-two curl has value1, so these changes do not alter the root box
operator. A standard winding contributes the mixed root monodromy, +1 on
w1 and -1 on the odd sector. The halfword axis letter counts that winding
modulo2. This is a reduction by crossing changes for a root evaluation,
not a claim that a scalar skein state has local topology.

The parent and the dedicated root-sign agent are checking this argument.

## 5. Carmi-Cohen scope

FT-DEEP does not refute a bound depending on crossing number: it only rules
out a universal fixed-order cutoff independent of complexity. The explicit
residual-twist obstruction is already recorded in
`work/paper/carmi-cohen-obstruction/`, with the trefoil host, L=23 and
b_51=-1 against the asserted residual cap22. That attacks the claimed
uniform-control proof step, not the truth of the main detection statement.
No renewed literature or obstruction search is necessary here.

## 6. Vertical shortcut: independent read

The parent's replacement for the a=+-1 interpolation is sound, with the
following explicit common normalization. Use the single normalized color-two
crossing X=A^8 times the raw x-crossing, with eigenvalues 1,-t,t^3, t=A^4,
and the same standard theta divisor Delta2 at every a. Call the resulting
raw linear scalar F_a, rather than preferred J.

Accepting the marked prism isotopy of `mont/nest/REPORT.md` Section4,
admissibility gives K0(P3)=K4(P1)=0. The two needed diagrams are then:

* At a=0, the marked vertical closure is the partial trace over V2 of the
  box endomorphism A P1+B P3, hence F0=A+([4]/[2])B=A+(t+t^-1)B.
* For the identity box, the axis bounds the bubble disk. Removing that
  bubble converts F_a into the quantum trace of X^a on V2 tensor V2 divided
  by Delta2. Thus K_c(id)=Delta_c/Delta2, exactly in the same normalization.

Since Delta0=1, Delta2=Phi3/t, Delta4=Phi5/t², the zeros and the second
diagram force K0=t A/Phi3 and K4=t^-1 Phi5 B/Phi3. Subtracting these from
F0 gives K2=((1+t²)A+tB)/Phi3. All three coefficients are thereby determined
without fitted relative units for a=1 and a=-1.

The physical unscaled theta scalar differs by the one crossing factor
A^(-8a); body and preferred framing are then common scalar factors. This
must be stated rather than identifying F_a literally with preferred J.
The shortcut does not itself replace the proof that the marked network is
the stated prism and that the two closures have these isotopies; once those
are supplied, no remaining scalar interpolation gap is present.
