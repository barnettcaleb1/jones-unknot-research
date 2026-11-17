# Two-ended theory: what extends, and an effective fixed-template reduction

17 November 2026. Bounded referee of the engineA end-jet proposal.
No knot words were enumerated. This note does not establish global
width-two positivity.

## 1. The rational-box laws use a commutative operation

Read: `collab/data/engineA/REPORT.md`, section 3, and the proofs of R2,
BX1--BX3 in
`~/jones-lanes/theory-restart/mont/notie/REPORT.md`, sections 1--2.

For a box let q=b/a. With its two ends expanded as

    q(t)=c_infty t^d (1+s_infty/t+...),
    q(t)=c_0 t^e (1+s_0 t+...),

write delta(q)=d-e and sigma(q)=s_infty+s_0. Both are additive under
multiplication of nonzero rational functions. Thus they are additive under
the necklace star product, whose channel amplitudes multiply. This
additivity does not hold under arbitrary braid composition: X acts on q by
a fractional-linear transformation and can cancel its leading terms.

The four rational end types in engineA follow from the last-letter states
R_1/S_0, S_0/R_1, R_0/S_j, S_j/R_0 and R2. They give delta=-1 and sigma=0.
In particular the proof of the sigma-law requires the rational normal form;
it is not a two-dimensional representation identity. EngineA's actual
nested-body examples already have sigma != 0, and actual depth-two boxes
have positive second coefficients. Neither assertion may be promoted to a
universal state constraint.

A general potential that is nondecreasing under every generator AND its
inverse is constant on the orbit: apply the two inequalities successively.
A useful width-two potential must therefore specify a reduced geometric
normal form or an operation other than unrestricted letter multiplication.
The width-one automaton has exactly such a normal-form hypothesis.

## 2. A mirror-pair obstruction to the proposed construction mechanism

Suppose a marked mirror pair of bodies has channel ratios q(t) and
epsilon t^ell q(t^-1). (This is the channel-wise reflection relation; any
relative framing monomial does not affect the statements below.) Their
star product has ratio

    Q(t)=epsilon t^ell q(t)q(t^-1).

Then, exactly,

    delta(Q)=2 delta(q),       sigma(Q)=2 sigma(q).

Indeed the normalized expansion of q(t)q(t^-1) at either end starts
`1+(s_infty+s_0)/t+...` at infinity and
`1+(s_infty+s_0)t+...` at zero. A product of any number of mirror pairs
still has EVEN delta, including nonrational boxes and arbitrary integral
Y-shifts.

For the nonzero horizontal special twist mu the closure pole is
`-w_1(mu)/w_3(mu)`. Its delta is -3 for mu=+-1 and -1 for |mu|>=2.
Consequently a mirror-paired body cannot tie the two closure channels at
BOTH ends, even to first order. This follows just from degree parity and
does not require rationality or the sigma-law.

Scope: this rejects the specific strategy of making a star-product body a
mirror norm and expecting one-ended pole agreement to reproduce itself at
the other end of the same twisted closure. It does NOT exclude arbitrary
prime amphicheiral theta-curves. It does NOT by itself rule out a unit
closure through a clean-end alternative. The reflection relation must use
the same channel labels and marking; an arbitrary diagram called
"symmetric" is not automatically a channel-wise mirror pair. Scalar
equivariant mirror sums are separately covered by TH-J-FACTORS.

## 3. Effective two-ended exclusion for a fixed seven-sector template

There is a rigorous replacement for global positivity when the two twist
sites and their outsides are fixed. It strengthens the existing
infinite-line classification into a finite, explicit decision procedure.

Use the seven-sector expansion of `width2_tropical_crux.md`:

    F(m,n)=sum c_ij(t) t^(2im+2jn),
    (i,j) in S={(0,0),(0,1),(1,0),(1,1),(1,3),(3,1),(3,3)}.

Assume the SIX BOUNDARY coefficients c00,c02,c20,c24,c42,c44 are nonzero;
the interior coefficient c22 may vanish. Let D be any common nonzero
Laurent denominator, p_ij=D c_ij, and choose [L,U] containing the support of
every nonzero p_ij. Put W=U-L, S_D=span D, and

    B=max(1,W,S_D),       C=3B.

**Finite-window theorem.** If F(m,n) is a Laurent unit, then

    |m| <= C  OR  |n| <= C.

Thus every unit lies in finitely many horizontal or vertical integer
lines. On each line there is either a whole unit-valued line, no units, or
an explicitly bounded finite list of parameters. This is a fixed-template
result, not a uniform complexity bound on all outside braids.

### Proof of the window

If m,n have the same nonzero sign, the 00 and 33 sectors give unique
opposite endpoints as soon as 2 min(|m|,|n|)>W. The resulting numerator
span is at least 6(|m|+|n|)-W, exceeding S_D outside the claimed window.

For opposite signs it suffices, after replacing t by t^-1 and changing
both parameter signs if needed, to write m>0, n<0. Put M=2m, N=-2n.
The seven exponent translations are

    0, -N, M, M-N, M-3N, 3M-N, 3M-3N.

Since M,N>3B, only 20 and 42 can give the top endpoint, and only 02 and 24
the bottom endpoint (color labels are used in this sentence). The upper
endpoint can cancel only on

    N-2M=deg p42-deg p20,                 (U)

and the lower only on

    M-2N=minexp p02-minexp p24.           (L)

Both right sides lie in [-W,W]. The two equations cannot hold together
when M,N>W: their sum after elimination gives M,N<=W. If neither holds,
the actual span is at least M+N-W>S_D.

If (U) holds, write N=2M+d, |d|<=W. The sector 02 sits at -2M-d and is
isolated from all other translated support intervals: the smallest
possible separation from another translation is at least M-2W>W.
The sector 24 at -5M-3d is likewise the unique bottom sector. Both survive,
whether or not the top pair cancels. Their surviving endpoint separation
is at least

    3M+2d-W >= 3M-3W > S_D.

If (L) holds, interchange the argument: write M=2N+d. Sector 20 at 2N+d
is isolated from every other support interval, while 42 at 5N+3d is the
unique top. Their separation is at least 3N-3W>S_D. In every case the
numerator cannot be a shifted signed copy of D. This proves the theorem.
The stated C is deliberately conservative; the proof uses smaller
constants in several regions.

### The finite one-variable finish

Fix any integer n0 in [-C,C] and aggregate in m:

    D F(m,n0)=g_0(t)+g_1(t)t^(2m)+g_3(t)t^(6m).

Discard identically zero g_i. If no group survives, there are no units.
If one group survives, its ratio to D is either a Laurent unit, giving
the entire line, or is not, giving no units.

If at least two groups survive, let W_n0 be the width of an interval
containing all their supports. For 2|m|>W_n0 the translated group supports
are disjoint, so the extreme groups survive and

    span(D F(m,n0)) >= 2|m|-W_n0.

Hence every unit parameter satisfies

    |m| <= floor((W_n0+S_D)/2).

All remaining tests are exact Laurent polynomial equalities to a signed
shift of D. Repeat with fixed m0 in [-C,C] for the vertical lines. Duplicate
points can be ignored. This gives a complete finite decision procedure,
plus the explicitly identified whole axis-parallel unit lines.

Since W_n0 <= W+6|n0|, every finite remainder lies in

    |m|,|n| <= floor((W+18B+S_D)/2) <= 10B.

The output is therefore a finite set inside this explicit square, together
with the whole unit-valued axis lines found by the aggregation test. At
least one coordinate of every point in the finite set is bounded by3B.
No claim of an optimal constant is made.

The proof of the window never used c22 != 0. The two same-sign corners
require c00,c44; the opposite-sign argument requires the four off-diagonal
boundary coefficients. This explains the six-coefficient hypothesis.

This calculation is applicable to the two engineB templates in the latest
letter because every individual sector there is nonzero. A relation such
as c42=-c44 at n=0 merely removes an aggregated row on that one horizontal
line; the procedure explicitly allows this. No implication that the
boundary vector itself is a twist eigenvector has been used.

### Two supplied templates: exact application, no parameter scan

Clearing the supplied rational coefficients gives:

| chronological V | chronological U | D | support interval of p | W | span D | strip bound C | finite square bound |
|---|---|---|---|---:|---:|---:|---:|
| x0.y2.y2.x1.x1 | x1.x1.y0.x1 | t^8(t^2+1)(t^2+t+1) | [0,28] | 28 | 4 | 84 | 268 |
| y0.y2.y1.x0.x3.y2 | y3.x2.x2.y3.x0.x1 | t^11(t^2+1)(t^2+t+1) | [0,21] | 21 | 4 | 63 | 201 |

Neither template has an axis-parallel unit line, at ANY offset. For a
horizontal line the outer aggregated groups are
g0=c00+c02 t^(2n) and g3=c42 t^(2n)+c44 t^(6n). Their vanishing requires
-c00/c02 to be t^(2n), or -c42/c44 to be t^(4n), respectively. For the
second template neither ratio is a monomial of coefficient1. For the
first, only the latter ratio is such a monomial, namely1; at n=0, g0 and
g1 are both nonzero. For vertical lines replace c02,c42 by c20,c24:
neither ratio is a monomial of coefficient1 in either template. Thus at
least two slope groups survive on every axis line. These are exact
rational-function tests, not finite-offset samples.

Consequently their entire unit fibers, if nonempty, lie in the finite
regions just displayed. The regions have not been enumerated by this
proof. A stronger gate may reduce the subsequent exact work.

## 4. What this contributes to the global question

The finite-window theorem uses two-ended incompatibility of the Newton
support's opposite faces, rather than a sign inequality for coefficients.
It is independent of the braid-word presentation of the two FIXED outside
tangles, once their seven rational coefficients are identified. Enlarging
the outsides can enlarge W without bound. Thus it makes the two-site
construction problem finite after the outsides are supplied, but it does
not settle the unrestricted width-two unit fiber.

For a global extension, the missing assertion would have to control how
the outside coefficient support and its identically zero sectors change
under recoupling or under a geometric normal form. The rational-box
delta/sigma proof does not provide that assertion. The banked failures of
NP/END also rule out identifying it with a positivity law for the
categorified outline.

## 5. Independent referee closure (Claude030114)

R1's proof report and R2's source/diagram log were read in full:
`~/jones-lanes/theory-restart/mont/referee/width2-window/R1_NOTES.md`
and `r2_all.log`. Both return SOUND. WIDTH2-WINDOW and AMPHI-PAIR are
PROVED under the collaboration protocol; no general width-two detection
theorem is claimed.

The proof allows the sharper strip radius C=floor(3B/2), since
M=2m,N=-2n>3B suffices. The finite remainder then has radius
floor((W+6C+spanD)/2), at most floor(11B/2). Whole unit-valued axis lines
remain separate, possibly unbounded outputs. The original3B/10B bounds
and conservative template constants remain correct.

R1 supplies the abstract table W=2,D=1:
p00=3t^2,p02=-4,p20=4+t+4t^2,p22=-3,p24=4t^2,p42=1,p44=-p20.
At(m,n)=(3,-2) its value is t^14. The optimal universal strip constant
for arbitrary coefficient tables is thus at least1; no marked tangle
realization of this table is asserted. No optimization task was opened.

AMPHI-PAIR applies only to horizontal nonzero special-twist closures of
a top-level star product consisting entirely of channel-wise mirror
pairs. It does not cover vertical closures with odd vertical parameter
(their pole spread is even), an unpaired odd-spread factor, or a clean-end
unit alternative. The channel correspondence requires the common marking.
