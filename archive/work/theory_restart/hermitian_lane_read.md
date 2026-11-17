# Hermitian tangle pairing and reflective doubles

Read of the 15 November letters. The Gram identity gives an equivalence between rationality of a two-string tangle with an actual unknot filling and unlink detection for its reflective double, in the precise senses below. The topology does not require its doubled components to be unknotted.

## Normalizations and the Gram identity

Use `R = Z[A, A^-1]`, `delta = -A^2-A^-2`, `t = A^-4`, and the absolute bracket with empty diagram 1 and circle `delta`. Write `v_X = (x,y)^T` in the through and turnback basis `(I,e)`, where `e^2=delta e`. In this note a tangle consists of exactly two arcs. Glue diagrams along the marked sphere, reflecting the second diagram. The off-diagonal closures are one circle and the diagonal closures are two circles. Therefore

```
B(X,Y) = bracket(X union reflect(Y)) = v_X^T G bar(v_Y)
G = [[delta^2,delta],[delta,delta^2]],       bar(A)=A^-1.
```

Taking the determinant of the two-vector Gram matrix gives

```
B(X,X) B(Y,Y) - B(X,Y) B(Y,X)
    = delta^2 (delta^2-1) (x_X y_Y-y_X x_Y) bar(x_X y_Y-y_X x_Y).
```

The two adjacent half twists have matrices

```
M = [[A,0],[A^-1,-A^-3]],       N = [[-A^-3,A^-1],[0,A]].
```

They are conjugated by the basis swap and each satisfies `M^T G bar(M)=G` or its counterpart for `N`. This follows by multiplying matrices and using `delta=-A^2-A^-2`. Changing tangle framing multiplies its vector by `(-A^3)^w`, whose norm is one. These statements use the ordinary four-end bracket action. [Sikora, §§4–7](https://arxiv.org/html/2005.08162)

## Exact elimination using the unknot filling

Choose a marking in which the actual unknot filling is `I`. In absolute normalization its bracket is `delta u`, with `u=(-A^3)^w`, so

```
delta x+y = u,
B(X,X) = (delta x+y) bar(delta x+y) + (delta^2-1)y bar(y)
       = 1 + (delta^2-1)y bar(y).
```

In particular `B(X,X)=delta^2` exactly when `y bar(y)=1`. For a nonzero Laurent polynomial the coefficient of its norm at the difference of its highest and lowest exponents is the product of the two extreme coefficients. Norm one therefore means `y=±A^r`, including the necessity that its coefficient be a unit. Since `delta | u-y` and `delta=-A^-2(A^4+1)`, evaluation at `A_0=exp(pi i/4)` forces `y/u=(-A^4)^k` for an integer `k`.

This conclusion identifies an actual rational tangle vector. The horizontal boundary half twist `N` multiplies the row `(delta,1)` by `-A^-3` and multiplies the second coordinate by `A`. Starting from `e`, it follows that `N^k e` has ratio `y/u=(-A^4)^k`. The relation `delta x+y=u` then determines the full normalized vector. Thus the double has unlink bracket exactly when `X` has the projective bracket of a rational tangle, and the twin can be taken from the explicit `N^k e` family. Conversely a rational tangle vector has norm `delta^2` since it is in the orbit of `e` and the two generators preserve the form.

The preferred marking gives a simpler exact form. Let `M_X` be the branched cover of `X`. Its `I` filling is `S^3`, so `M_X` is the exterior of the filling core knot. Choose the `e` filling at the homological longitude. The reduced bracket of that closure is `x+delta y`, and the closure has determinant zero because its branched cover has positive first Betti number. At `A_0` this gives `x(A_0)=0`. The minimal polynomial of `A_0` is `A^4+1`, so `delta | x` in `R`. It follows that `y/u congruent 1 mod delta^2`. A Laurent monomial congruent to 1 modulo `delta^2` equals 1 because its derivative at the nonzero simple root `A_0` has to vanish. Thus in the preferred marking

```
B(X,X)=delta^2    iff    y=u    iff    x=0.
```

The determinant specialization is used here only for the marked longitude filling. An unmarked rational tangle can have `x` nonzero and still have unlink double. For instance `N e=(A^-1,A)^T` is a rational tangle, has `I` closure an unknot, and has double bracket `delta^2`. [Sikora, §§3, 5, 10](https://arxiv.org/html/2005.08162)

## Topology of the reflective double

Let `DX` be the mirror double with the same endpoints glued. Each arc is glued to its own reflected arc, so there are exactly two components. Orient each doubled component along one arc and back along the reflected arc. Crossings come in opposite-sign pairs where the diagrams are joined without further crossings. The writhe and linking number vanish. In these conventions, `B(X,X)=delta V_DX`.

Its branched cover is the ordinary topological double `M_X union_boundary (-M_X)` of the exterior of the filling core `kappa`. It is also the zero surgery on `kappa # (-mirror(kappa))`, with the second knot oriented as the concordance inverse. One sees this by cutting the connected-sum exterior along its decomposing meridional annulus and capping that annulus by the annulus in the surgery solid torus. The meridian of each piece runs along the resulting torus, and zero surgery identifies the two preferred longitudes oppositely because the sum longitude bounds a meridian disk of the filling. In oriented meridian-longitude coordinates the full gluing is `(mu,lambda) -> (mu,-lambda)`, which is the double gluing written in the mirror exterior with its core orientation reversed.

For nontrivial `kappa`, the seam torus has injective fundamental group in the double. The torus is incompressible in each knot exterior and the amalgamated product preserves its injection. Hence the cover cannot be `S^1 x S^2`, which is the branched cover of `U_2`. For rational `X`, double a homeomorphism of the ball-tangle pair to the trivial pair to obtain an actual unlink. The solid-torus criterion for rational tangles identifies the unknot core case with rationality. [Hanselman–Rasmussen–Watson, “Solid tori and rational tangles”](https://doi.org/10.1112/plms.12473)

The doubled components need not be unknots. Let `a` be a knotted proper arc, for example a trefoil cut at one short unknotted subarc. Take the two long sides of an embedded strip along `a`, with both short sides in the boundary sphere as the `I` caps. The cap closure bounds the strip and is an actual unknot. Each component of the mirror double instead intersects the equatorial sphere twice and is the connected sum of the arc's knot with its mirror. Both components in this example are square knots. Each doubled component generally has this connected-sum description with its own capped arc. A *local* knot tied into one strand in a ball disjoint from the other strand would instead be a connected-sum factor of the cap closure, so an actual unknot closure excludes local knot factors. The strip example meets the unknot condition because the two knotted arcs need not be separately isolated by local knot spheres.

Consequently the rational-twin assertion for tangles with an actual unknot filling is equivalent to Jones detection of the unlink on the class of their marked reflective doubles. In the preferred marking this says `V_DX=delta` forces `x=0` and then calls for rationality of `X`. The component-unknotted restriction proposed in the letter would omit examples from the actual class.

## Exact symmetry reformulation

Consider a nonzero power of a Dehn twist about an essential separating curve on the four-punctured boundary. Its bracket action is conjugate to a nonzero (even) power of `M`, up to an invertible framing scalar. Over `Q(A)` the two eigenlines of `M`, and of all its nonzero powers, are `(0,1)` and `(delta,-1)`. The first is the rational line. An integral vector on the second line has the form `c(delta,-1)` with `c` Laurent. Its reduced bracket pairing against any rational filling `R` with vector `(x_R,y_R)` is

```
delta^-1 B(c(delta,-1),R) = (delta^2-1)c bar(x_R).
```

This is zero or divisible by the nonunit `delta^2-1`. Since simultaneous boundary reparametrization carries the actual unknot filling to another rational filling, this second eigenline is excluded for every tangle in the cap-trivial class. On the first eigenline the bracket vector equals `c(0,1)` after conjugation, where the actual cap unit forces `c` to be a Laurent unit. Conjugating back gives a rational bracket twin. The same cap on the rational twin is itself an unknot. Its reduced bracket is a unit, so evaluation at `t=1` forces one component and evaluation at `t=-1` forces determinant one. A two-bridge knot of determinant one is the unknot. The quotient of the two cap brackets is therefore an ordinary framing unit. A rational bracket twin has the algebraic twist stabilizer of the twin's rational disk slope, so the equivalence is two-way.

If such a nontrivial boundary Dehn twist is realized by a homeomorphism of the tangle pair, it lifts to a nontrivial torus twist on the exterior of `kappa`. The lift preserves the primitive kernel of the boundary homology map, so its twist slope is the longitude. The meridian is carried to the distinct slope `mu+k lambda` for some nonzero `k`. This would give another `S^3` filling of a nontrivial knot exterior, which is excluded by Gordon–Luecke. The rational tangle has a separating disk and a homeomorphism inducing its boundary Dehn twist. Thus for the cap-trivial class the rational-twin assertion is exactly the claim that a nontrivial algebraic boundary-twist stabilizer can be realized geometrically. A local knot tied into one strand of a trivial tangle illustrates the role of the cap hypothesis: the separating disk twist still exists and its bracket line is still rational, although that tangle is not rational. [Gordon–Luecke, Theorem 2](https://doi.org/10.1090/S0894-0347-1989-0965210-7)

## Unit-circle check

For `|A|=1`, the eigenvalues of `G` are `delta^2+delta` and `delta^2-delta`. The matrix is positive definite for `|delta|>1` and has signature `(1,1)` for `0<|delta|<1`. Here `delta^2=2+t+t^-1`, so the latter arc passes through the degeneration at `t=-1` between the primitive cube roots. The double satisfies `B(X,X)>=1` on the definite arc and `B(X,X)<=1` on the indefinite arc when the cap bracket has unit norm. Both inequalities are immediate from the cap identity. A general `X` on the indefinite arc need not have positive norm by this argument.

For positive lines in the indefinite form the standard complex hyperbolic disk relation is `cosh^2(d/2)=|B(X,Y)|^2/(B(X,X)B(Y,Y))`. On rational tangles `B(Y,Y)=delta^2`, giving the claimed formula `|B(X,Y)|=delta^2 cosh(d/2)` for two rational inputs. For an actual or Jones-unit knot filling by a rational `Y`, `|B(X,Y)|^2=delta^2`, so `B(X,X) cosh^2(d/2)=1` if `X` is in the positive disk.

The half twist normalized by `A` has eigenvalue ratio `-A^-4=-t`. The generators are the two Burau matrices after conjugation by `diag(1,A^2)` and division by `A`. This explains the root parameter in the triangle group description. The metric relates projective specialization values. Distinct rational slopes can specialize to the same line because the nth power of a half twist is projectively trivial at `-t=exp(2 pi i/n)`. The loss of knot detection can also be seen without the triangle-group theorem. For odd `r` the two-strand trace gives

```
V_T(2,r) = (-A^3)^(-r) [A^r(delta^2-1)+(-A^-3)^r]/delta.
```

If `t^m=1` and `t != -1`, set `r=2m-1`. The numerator after multiplying by the writhe correction becomes `-A^2(delta^2-1)+A^6=delta`, hence the value is 1. For the root of order `m>1` this produces a nontrivial two-bridge knot. [Funar–Kohno, §3](https://arxiv.org/html/0907.0568)
