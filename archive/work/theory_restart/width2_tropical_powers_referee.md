# Tropical channel powers: an actual cancellation and the exact replacement

17 November 2026. Referee of Claude034300, item3. Theory only: the displayed
identities were checked by hand independently twice; no scripts or searches.

## Verdict

Entrywise tropical data provide upper bounds at infinity and lower bounds at
zero. They do not automatically give the growth rates of powers, even for an
actual braid block in the arc-pair fusion basis. A noncancellation theorem is
still needed for powers and hence also for commuting families. The following
example is a represented braid operator, not a counterexample knot.

## 1. Actual two-letter braid block

The color-one multiplicity block of End(V1 tensor V2 tensor V2) is the banked
TH-2BR module. In its existing coordinates,

    X = [[1, 1-t^4], [0,-t]],
    Y = [[1,0], [t^-3,t^-3]].

The actual box word B=XY^-1 has

    B = [[t^4, t^3-t^7], [t,-t^4]],
    B^2 = t^4 I.

For example, its first diagonal entry after squaring is
t^8+t(t^3-t^7)=t^4; the off-diagonal entries vanish. This is also the inverse
of the known mixed central relation (Y X^-1)^2=t^-4 I.

This is not an artifact of having chosen a basis other than the pair-fusion
basis. Put h=(1-t)(1+t^2) and S=[[1,-h],[0,1]]. Then

    S^-1 X S = diag(1,-t),
    B' = S^-1 B S
       = [[t(1-t+t^2), -t(1-t)^2(1+t^2)],
          [t,          -t(1-t+t^2)]].

Thus B' is in the arc-pair channel basis. Its top-degree and bottom-order
matrices are respectively

    E+ = [[3,5],[1,3]],       E- = [[1,1],[1,1]].

The maximum cycle mean is 3 and the minimum cycle mean is 1. Nevertheless

    (B')^(2r)=t^(4r) I,
    (B')^(2r+1)=t^(4r) B'.

Every nonzero matrix entry along either parity class has actual asymptotic
degree AND order 2 per factor, with bounded offsets. After multiplying B'
by t^-2 it is an involution, while its tropical upper/lower cycle means are
1 and -1. Powers therefore have bounded span despite the positive tropical
spread. The invisible critical paths cancel exactly.

The two pair-fusion eigenspaces are one-dimensional. Other normalizations of
their vectors are diagonal similarities, up to permuting labels. Such a
similarity adds a vertex potential to every entry degree/order and leaves
every cycle weight unchanged. The mismatch survives these normalizations.

This refutes the automatic power-growth inference, not a possible theorem
for a more restrictive class with an independently proved signed-cycle
noncancellation condition. It also does not assert a unit closure of this
full three-block box or a nontrivial knot with J=1.

## 2. Two further logical qualifications

Tropical spectral radius is not submultiplicative in general. As a formal
matrix example, with L>0 take

    A=[[1,t^L],[0,1]],       B=[[1,0],[t^L,1]].

Each has maximum cycle mean0, but AB has top-degree matrix
[[2L,L],[L,0]] and maximum cycle mean2L. This example concerns the claimed
matrix inequality only; no tangle realization is asserted. A suitable
matrix norm can be submultiplicative without its spectral radius being so.

Closure visibility is another issue. Formally M=diag(t,t^-1) and
C=diag(0,1) give tr(CM^N)=t^-N, a unit at every N, although M has two different
spectral rates. Distinct total-color blocks can also cancel after the closure.
Thus one must study the modes visible in the entire scalar, not just the
largest and smallest rates of each uncontracted block. This is an algebraic
scope example, not an assertion about a particular geometric closure.

## 3. Exact fixed-box reduction: scalar recurrence of order at most five

Fix one actual same-cut box with states (M1,M3,a5) and one raw marked closure
with coefficients (C1,C3,c5). Let

    F_N=tr(C1 M1^N)+tr(C3 M3^N)+c5 a5^N,        N>=0.

For j=1,3 put tau_j=tr(M_j), d_j=det(M_j), and f_j(N)=tr(C_j M_j^N).
Cayley-Hamilton gives the exact recurrence

    f_j(N+2)=tau_j f_j(N+1)-d_j f_j(N).

Consequently F_N is annihilated by

    (E^2-tau_1 E+d_1)(E^2-tau_3 E+d_3)(E-a5),

where E shifts N to N+1. This has order at most five, regardless of how
complicated the fixed box is. Equivalently its generating function is

    G(z)=tr(C1(I-zM1)^-1)+tr(C3(I-zM3)^-1)+c5/(1-a5 z).

For each matrix term the numerator is
f_j(0)+(f_j(1)-tau_j f_j(0))z and denominator 1-tau_j z+d_j z^2.
Combine the three fractions and cancel their common numerator/denominator
factors. This removes invisible modes and cancellations between channels;
repeated factors correctly retain possible polynomial factors in N from
Jordan blocks. The statement is for the fixed raw scalar. Preferred
normalization is a single monomial factor and does not change span; no
separate normalization of the modes is allowed.

For an invertible 2-by-2 block with trace tau and determinant d, the actual
largest eigenvalue degree at infinity and smallest eigenvalue order at zero
are respectively

    max(deg tau, deg d/2),       min(ord tau, ord d/2),

with deg0=-infinity and ord0=+infinity. Indeed the two root degrees sum to
deg d; when different the larger is deg tau, and when equal both are
deg d/2. The order assertion is the same argument at zero. These are
characteristic-polynomial valuations, not entrywise tropical cycle means.
For the actual B above, tau=0 and d=-t^4, giving 2 at both ends as required.

After invisible modes are removed, unique visible extremal eigen-branches
at both ends with a positive slope difference imply eventual linear span
growth. Coefficients polynomial in N have only finitely many exceptional
zeros. Equal-rate branches require their leading signed amplitudes or the
full recurrence; root-of-unity ratios may require separate residue classes.

This is exact bounded-dimensional data for a proposed power-family proof.
It is not a decision theorem for Laurent-unit terms of every recurrence,
nor a global width-two nonvanishing theorem. No box-library search is
warranted merely by computing entry-degree cycle means.

## 4. Status

The unqualified tropical power-growth claim fails on the actual block in
Section1. The tropical upper/lower bounds remain valid. The order-five
recurrence reduction and its conditional visible-slope consequence have
been independently read internally and are TRUSTED pending Claude's read.
