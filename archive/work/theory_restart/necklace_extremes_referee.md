# Necklace channels: a controlled-cancellation theorem

16 November 2026. Referee of Claude192557 and the subsequently completed
`/Users/calebbarnett/jones-lanes/theory-restart/mont/notie/REPORT.md`, Sections
1–4. No scan was run. The finite proof below was checked independently by
expanding its transitions and its six endpoint cases. One specific
third-order exceptional example was evaluated exactly as a normalization
check; it is not evidence substituted for the proof.

## Verdict and precise theorem

The new report contains a sound **algebraic nonunit theorem**, substantially
stronger than the leading-degree observation in the letter. Its mechanism
is controlled cancellation, not a literal no-tie theorem. It avoids the
potentially unbounded cascade at the tied end by examining two coefficients
at the other end. In one explicit case it examines three coefficients.

Put

```
Y = [[1,0],[t^-3,t^-3]],
X = [[1,1-t^4],[0,-t]],
E = Y^-1 X = [[1,1-t^4],[-1,-1]], E^2=t^4 I,
a(v)=v1, b(v)=v1+(1-t^3)v2.
```

Let `v_1,...,v_n` belong to the rational orbit `rho(w)e1`, with every
`a(v_i)` nonunit and `n>=2`. Define star product by multiplication of a
and b. For every integer `N` and every nonzero integer `mu`,

```
J = e1^T X^mu Y^N (v_1 * ... * v_n)
```

is a nonunit Laurent polynomial. This includes all signs of the box words,
the special twist, and the collected integral part. The proof is over
`Z[t,t^-1]`; no root specialization or generic-coefficient assumption is
used. Nonunit means more than one nonzero Laurent coefficient, so an
overall ribbon-framing monomial does not affect the conclusion.

Applying this to a geometric class remains conditional on the marked
necklace formula and the identification of each intended piece with this
rational orbit. In particular a **pure `X^mu` special region** is part of
the hypothesis. A general rational special tangle has not been handled by
this proof. The letter uses inconsistent signs when matching mu to an
even pretzel column; state the theorem using the marked matrix exponent
until that convention is fixed geometrically.

## 1. Normalized boxes and first-order channel data

The repaired TH-2BR normal form gives, up to a monomial,

```
v_i = Y^Ni u_i,
u_i = E Y^m_(k-1) ... E Y^m0 e1,
m0 not in {0,-1}, m_j!=0 for j>=1, k>=1.
```

All `Ni` can be absorbed into the outside N because Y multiplies channel
b by `t^-3` and fixes channel a. Thus it suffices to work with the u_i.
Write `r=v2/v1` and `q=b/a=1+(1-t^3)r`.

The post-E ratio states from TH-2BR are

```
R:   r=t^-1(1+...),
S_j: r=(-1)^j t^(-4-j)(1+...), j>=0.
```

For R, `top(b)-top(a)=2` and their leading signs are opposite. For S_j,
their top degrees and leading signs agree. R occurs exactly when the last
normal-form exponent is positive. The reciprocal box has last sign
reversed, including the one-exponent boundary case, so top-R and
bottom-S are exchanged.

The old automaton already gives `span(a_i)>=4`, with leading and trailing
coefficients +/-1.

## 2. The two-term state extension and its potential

For a nonzero Laurent function write its expansion at infinity as

```
f=c t^D (1+rho(f)t^-1+x2(f)t^-2+...).
```

The quantity rho is additive under products. Refine R to R_c with
`r=t^-1(1+c t^-1+...)`, where `c=0` or `1`. Each E step multiplies a by
`D=1+(1-t^4)r_pre`. The complete transition table is:

| Incoming state | Next exponent | Outgoing state | rho(D) |
|---|---:|---|---:|
| initial | positive | R_1 | -1 |
| initial | -m, m>=2 | S_0 | 0 |
| R_c | 1 | R_0 | 0 |
| R_c | n>=2 | R_1 | -1 |
| S_j | positive | R_1 | -1 |
| R_c | -m, m>=1 | S_0 | c |
| S_j | -m, m>=2 | S_0 | -[j=0] |
| S_j | -1 | S_(j+1) | -[j=0] |

For example, a positive step has
`r_pre=t^-3(1+epsilon t^-1+...)`, with epsilon=1 only when the incoming
state is R and the exponent is one. Hence
`D=-t+(1-epsilon)+...`, and the new R coefficient is `1-epsilon`.
For a negative step from R_c, its shifted term dominates the geometric
sum and gives `rho(D)=c`. From S_j the geometric sum dominates; its first
correction comes from the shifted ratio only for j=0. At exponent -1 the
identity `r_pre=-1+t^3 r_old` controls the numerator cancellation exactly.
These calculations require no unrecorded second coefficient of S_j.

The channel correction has

```
rho(q)=c       in R_c,
rho(q)=-1      in S_0,
rho(q)=0       in S_j, j>=1.
```

Define phi=1 on both R states and phi=0 on initial/S states. Along every
transition the quantity `rho(a)+phi` is nonincreasing, starting at zero.
Indeed the eight changes in the table order are

```
0,0,0,-1,0,c-1,-[j=0],-[j=0].
```

Consequently

```
rho(a)<=-1 on an R-top box,
rho(a)<=0 on an S-top box,
rho(b)<=0 on every box.
```

Moreover an S-top box has `rho(a)=0` exactly when its exponent signs
alternate and end negative. A same-sign run either loses the potential
immediately or enters R_0, from which return to an ending S state loses
it. Thus equality has the stated exact characterization.

One further coefficient is needed only in this equality case. In an
alternating S-top box with k E steps, every D factor has x2(D)=0. Its
rho(D) values alternate +/-1, with an initial zero if m0<=-2. Since their
sum is zero, additivity of `x2-rho^2/2` gives

```
x2(a)=-(k-[m0<=-2])/2 <=0.
```

The local expansion behind this is `r(R_1)=t^-1(1+t^-1+t^-2+...)` along
an alternating path. A negative step subtracts the geometric-sum term
at relative order two, so its D factor has normalized coefficients
`(1,1,0)`, while the positive step has `(1,-1,0)`. An initial negative
step has `(1,0,0)`. This checks the third-order equality claim directly.

## 3. Ties can occur at only one end

Set

```
Phi=1+t+t^2,
w1=t+(1+t^2)(-t)^mu,
w3=(1+t^2)(1-(-t)^mu),
A=product a_i,
B'=t^(-3N) product b_i,
J Phi=w1 A+w3 B'.
```

Let Rcount be the number of R-top boxes and put
`d=2 Rcount-3N`. Then d is `top(B')-top(A)`, and the leading sign ratio
of B' to A is `(-1)^Rcount`.

The first-order cancelling top ties are exactly

| Type | Twist | d | Rcount parity |
|---|---|---:|---|
| T1 | mu>=1 | 0 | even |
| T2 | mu<=-2 | -1 | odd |
| T3 | mu=-1 | -3 | even |

The exact reciprocal-box identities are

```
bar a(u)=t^(-4k) a(u''),
bar b(u)=t^(-4k-3) b(u''),
u''=u(-m0-1,-m1,...),
bar J(mu,N;u)=t^(-4 sum k_i) J(-mu,n-N;u'').
```

Thus the mirrored values are `Rcount''=n-Rcount` and `d''=-n-d`.
The cancelling bottom ties are exactly

| Type | Twist | d | Rcount parity |
|---|---|---:|---|
| B1 | mu<=-1 | -n | n mod2 |
| B2 | mu>=2 | 1-n | different from n mod2 |
| B3 | mu=1 | 3-n | n mod2 |

No top row and bottom row can hold together when n>=2. The only degree
coincidences require n=1, or n=3 with incompatible parity. Hence there
is always at least one clean endpoint of the *two-channel expression*.
This is unrelated to the retired unsigned-homology endpoint conjecture.

If neither end ties, put `T=top(w1+w3 B'/A)` and let T'' be its mirror
value. The reciprocal identity yields

```
span(J)=span(A)-4+T+T''.
```

For mu>=2, T+T''>=5; for mu=1 it is >=2. The other signs follow by
mirroring. Thus `span(J)>=4n-2>0` whenever neither end cancels.

## 4. A clean endpoint has a second term, with one exception

By mirror symmetry, suppose the bottom ties and the top does not. Put

```
Delta=top(w3 B')-top(w1 A),
epsilon=leading(w3 B')/leading(w1 A) in {+1,-1},
s1=rho(w1)+sum rho(a_i),
s3=rho(w3)+sum rho(b_i).
```

The normalized second coefficient R of `J Phi` is respectively

```
s1           if Delta<=-2,
s1+epsilon   if Delta=-1,
(s1+s3)/2    if Delta=0 and epsilon=+1,
s3+epsilon   if Delta=1,
s3           if Delta>=2.
```

Since Phi has normalized top coefficients `(1,1,1)`, the normalized
second coefficient of J is R-1. Thus R!=1 proves that J has two terms.
The only positive rho values of the weights are

```
rho(w1)=1 exactly for mu=-2,
rho(w3)=1 exactly for mu=1 or mu=-1.
```

The other weight rho values are zero. Combining these with Section 2
settles all cases as follows.

* **B1, mu<=-2.** Delta=1-n. If n=2, R=s1+1. Equality R=1 would force
  either all boxes S with rho(a)=0, or (at mu=-2) total rho(a)=-1 and
  Rcount even. In either event Rcount=0, inconsistent with d=-2 being
  a multiple of three. For n>=3, R=s1; equality R=1 requires mu=-2
  and every box to be alternating S-top. Then Rcount=0, N=n/3 and n
  is even: exactly the exceptional case P1 below.
* **B1, mu=-1.** For n=2,3,4,>=5 the respective values/bounds are
  `R=sum rho(b_i)<=0`, `R<=1/2`,
  `R=sum rho(a_i)-1<=-1`, and `R=sum rho(a_i)<=0`.
* **B2, mu>=2.** For n=2, R=sum rho(a_i)+1; equality R=1 forces all
  boxes S, but the B2 parity requires Rcount odd. For n>=3, R<=0.
* **B3, mu=1.** The same four bounds as the mu=-1 B1 case apply.

The remaining P1 case is

```
n divisible by6, mu=-2, N=n/3,
every box alternating S-top with rho(a_i)=0.
```

Here Delta=1-n<=-5, so the first three coefficients of `J Phi` come
only from w1 A. Write `Y2=sum x2(a_i)<=0`. Then

```
w1=t(1+t^-1+0*t^-2+t^-3),
A=c t^D (1+0*t^-1+Y2*t^-2+...),
J=c t^(D-1)(1+0*t^-1+(Y2-1)t^-2+...).
```

Since Y2-1<0, the third coefficient survives. This completes the proof
for every pure-twist necklace in the algebraic class.

As a fixed sanity check, six copies of `u(-2)` with N=2, mu=-2 have
`a(u(-2))=t^7+t^4-t^3`. Direct integer Laurent multiplication gives J
top degree41 and first four coefficients `(1,0,-1,8)`, of span24. This
checks the exceptional normalization without a search.

## 5. What the result gives, and what it does not

1. Subject to the marked skein identification, this gives a real class
   theorem beyond merely a finite check of a list of Montesinos examples.
   The proof admits rational boxes of arbitrary word length and arbitrary
   collected integral twist. It covers every sign pattern in that class.
2. The report's stronger span speculations are unnecessary for nonflatness.
   First-order ties can cascade to high depth at the tied end. Nothing
   in this audit gives a uniform bound on that depth, or proves the
   conjectural span>=3n. Do not add either claim to the theorem.
3. No integral or homological END/NP statement follows. The two nonzero
   coefficients are coefficients of J. They need not occur at the
   extreme quantum support of N.
4. A general rational special region, arbitrarily nested frames, and
   arbitrary strong inversions of Montesinos knots require their own
   marked-frame theorem. Calling the result “all Montesinos inversions”
   would overstate its present hypotheses.
5. None of the large verification counts in the shared reports is used
   in the proof above. They corroborate the normalization but do not
   replace the finite transition and endpoint analysis.

The appropriate name is a **two-channel controlled-cancellation theorem**:
ties are allowed, one endpoint stays clean, and its next one or two
coefficients prevent a Laurent unit.

## 6. A separate closure-corollary caution

The parent found, and I checked, a counterexample to the *algebraic
divisibility argument* in Claude120708 for all nonzero surgery-closure
parameters. In the stated odd-closure formula take j=1,n=1 and set

```
J*=1+t(t+1)(t^-12-1)/(1+t+t^2).
```

This is a Laurent polynomial: `1+t+t^2` divides `t^12-1`. It is not one,
and `(t+1)^2` divides `t(J*-1)`. Nevertheless

```
t^12 [1+(1+t^-1)(1+t+t^2)/(1+t)^2 (J*-1)] = 1.
```

Indeed the coefficient of J*-1 simplifies to
`(1+t+t^2)/(t(t+1))`, so the bracket is exactly t^-12. This is not an
actual tangle construction and does not refute the topological corollary.
It shows that its proposed divisibility inference is insufficient. The
nonflatness theorem above should therefore not be advertised as detection
of every odd closure without an additional realizability constraint.
