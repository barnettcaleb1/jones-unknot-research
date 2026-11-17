# The unique unit point of fixed template1 is an unknot

17 November 2026. Single-object geometric certificate; no search and no
inference from Jones polynomial1.

The parameter `(-2,-1)` of the marked template

    V=x0.y2.y2.x1.x1,    U=x1.x1.y0.x1

reduces by inverse cancellation and distant commutation to the halfword

    s.l1.l1.y2.y2.y3.y3.x1.u2.u2.

Indeed the complete chronological braid word before reduction is

    x0.y2.y2.x1.x1.y1.y1.y1.y1.y3.y3.x1.x1.y0.x1.

Cancel two `x1` against two `y1`, commute the remaining `y1.y1` past
`y3.y3` and cancel against `x1.x1`. The remaining `x0` commutes past
indices2 and3 and cancels `y0`.

There are now no axis crossings. The quotient arc lies on one side of
the axis, and the covering knot is the local swap sum `L # rL`, where
`r` reverses the half by the strong inversion (whether the convention
also mirrors it is immaterial here). The local knot `L` is the ordinary
four-plat with top matching `(12),(34)`, bottom matching `(14),(23)`, and
chronological braid

    sigma2^-2 sigma3^-2 sigma1.

This is a two-bridge knot. Its determinant is1, so its rational numerator
is `+1` or `-1`, and the rational-knot classification makes it an unknot.
Consequently the covering knot `L # rL` is an unknot as well.

Here is the determinant certificate, computed directly from the five
crossings of `L`. A cyclic PD code (starting on the incoming under-edge)
is

    [[0,3,4,2], [3,5,6,4], [6,7,8,2], [10,8,7,9], [5,0,10,9]].

A Wirtinger Alexander minor at `t=-1` is

    [[ 2,-1,-1, 0],
     [-1, 0, 2,-1],
     [-2, 1, 0, 1],
     [ 1,-2, 0, 0]],

whose determinant is `-1`. Its absolute value is the knot determinant.
The five-crossing trace is connected; the code can also be reconstructed
by the existing `tools/alex.py` diagram reader from

    [('l',2), ('y',1), ('y',1), ('y',2), ('y',2), ('x',0), ('u',1), ('u',0)].

That reader begins with one top cap; `l2` adds the other, and the final
`u1,u0` give the nested bottom matching. This uses the unbranched local
four-plat directly, rather than guessing its type from polynomial data.

An independent check on the symmetrized ten-crossing covering diagram
gives Alexander determinant1 as expected. This check is redundant; the
local rational-knot argument supplies the topological conclusion.
