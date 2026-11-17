# A nonaxis unit line in the canonical width-two module

17 November 2026. Exact referee certificate, no search.

## Verdict

The proposed statement that a unit full-twist line forces one of the two
sites to act scalarly on the input vector or output covector is false in
the literal canonical nine-dimensional module. The parallel-circle
cancellation already has a short marked realization there. Every member
of this particular line is an unknot; it is not a counterexample to
Jones detection. It also disproves the reported finite-screen conclusion
that only axis-parallel unit lines occur, if that conclusion concerns all
the stated junctions.

## Marked word and exact identities

Use `collab/data/engineB/rho2_matrices.json`, its integral basis `f0,...,f8`,
and its chronological word convention. Write `X_i=M[x_i]`, let `v=f0`,
and let

    phi = t^2 PHIT[u2.u2]/(1+t)^4.

The canonical prefix is `s.l1.l1` (equivalently `s.l1.l3`) and the suffix
is `u2.u2`. Set `w=f2`, the nested cups `(14),(23)`. The exact identities
are

    X1 X2 v = t^4 w,
    X1 w = X3 w = t f0 + (t^2+t^3) f1 + t^3 f2,
    phi X1 w = t^4.

Since `X1` and `X3` commute and are invertible,

    X1^(2m) X3^(-2m) w = w                 (m in Z).

Thus the chronological family

    s.l1.l1.x2.x1.(x1)^(2m).(x3)^(2n).x1.u2.u2

has raw coefficient `t^8` on the entire line `n=-m`. Negative exponents
mean inverse letters `y_i`. The preferred `J` is therefore identically1
on that line. Full twists preserve the permutation, and the base word
`x2.x1.x1` is a connected-arc plat, so every parameter on the line is a
knot quotient.

Neither site acts scalarly on the input `t^4 w`: the displayed image has
nonzero `f0` and `f1` coordinates. Nor is the output covector `phi X1`
an eigenvector for either `X1` or `X3`. The script checks nonzero two-by-two
minors of each pair of rows. Because the generic eigenvalues of `X_i`
are `1,-t,t^3`, while those of `X_i^2` are the distinct `1,t^2,t^6`, the
same non-eigenvector assertions hold for the full twists.

## The seven-sector certificate

Take the outside prefix `V=x2.x1` and outside suffix `U=x1`, in the
notation `c_ab=phi rho(U) E_ab rho(V)v`. The only nonzero coefficients are

    c00 = t^5/(t^2+t+1),
    c22 = -t^5,
    c44 = t^6(t^4+t^3+t^2+t+1)/(t^2+t+1).

All of `c02,c20,c24,c42` vanish. Hence, for all integer `m,n`,

    F(m,n)=c00+c22 t^(2(m+n))+c44 t^(6(m+n)).

The single surviving slope group on `(m,n)=(m,-m)` has sum `t^8`.
The three sector coefficients do not vanish individually. This is
precisely the allowed central-triple case of WIDTH2-FLAT-LINES, not an
exception to that theorem.

Both individual sites are nonflat. For example,

    F(1,0)=F(0,1)
      =t^14+t^11-t^9+t^8-t^7-t^6+t^5,

which has span9 and is not a unit. Consequently neither site can be
nugatory in the base marked theta graph: a nugatory twist would preserve
the preferred invariant. The two sites cancel each other along the
diagonal rather than separately sliding off the chosen boundary.

## Geometry

The prefix `x2.x1` is the standard cap-slide taking the two unnested cups
to the nested cups, up to a ribbon framing unit. In the nested pairing,
crossings on legs1,2 can slide along the cups to crossings on legs3,4.
Equal and opposite full twists therefore cancel by ribbon isotopy. This
is the usual annulus between parallel twisting circles, now with its
literal four-leg marking. It proves that all diagonal members are
isotopic to the zero-parameter closure, independently of the polynomial.

After that cap-slide, the base halfword is

    s.l1.l2.x1.u2.u2.

Its arc is connected (the input matching becomes `(13),(24)`, while the
output cap is `(23)`), and its covering knot has just the two crossings
lifting the one off-axis crossing. A connected knot diagram with at most
two crossings is an unknot. This supplies the non-spectral topological
certificate for the entire diagonal.

## What can still be asked

This refutes only the proposed *literal boundary-scalar* conclusion.
A repaired geometric conjecture could allow an annulus relating the
two sites, or first quotient templates by cap slides and parallel-circle
cancellation. Neither repair follows from the seven-sector algebra;
they require a topological classification of its realizable vanishing
patterns. A useful target is therefore: do all unit lines arise from
one-site nugatory twists **or** such cancellation surfaces? No claim of
that broader classification is made here.

The finite screen should retain this short template as a regression
certificate before its absence-of-diagonal-lines conclusion is used.

## Reproduction

`width2_unit_line_certificate.py` reads only the workspace JSON module,
uses exact rational functions, checks the identities, all nine joint
coefficients (including the structurally zero sectors), both boundary
non-eigenvector tests, and connectedness. Run with a Python that has
SymPy, for example the existing research environment:

    /Users/calebbarnett/jones-lanes/theory-restart/tools/venv/bin/python work/theory_restart/width2_unit_line_certificate.py

