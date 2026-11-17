"""Independent Kauffman-bracket evaluation of the two annular functionals of MOMENT-CYC10 (Lens A).
Conventions copied from kauffman.py: letter x at position i = A*(keep) + A^-1*(cup_i then cap_i); y = reverse.
E_minus(D): colour-1 axis (belt around the cut level) + colour-2 annular diagram D (2-cables, f2 on every cable pair at the cut),
            divided by Delta_1 = delta;  variable t = A^4, Q = -t^-1.
E_plus(D):  bracket of the double-branched lift (two copies of the fundamental domain), variable a with a^2 = Q.
Annular diagrams are given as words over n colour-2 'strands' (the fundamental domain of the annulus):
   ('s',j,+1/-1): crossing between strands j,j+1 of type x (+1) or y (-1); ('e',j): colour-2 cup-cap between j,j+1."""
import sympy as S
def padd(p, q, c=1):
    for e, v in q.items():
        nv = p.get(e, 0) + c*v
        if nv: p[e] = nv
        elif e in p: del p[e]
def pshift(p, k, c=1): return {e+k: c*v for e, v in p.items()}
def pmul(p, q):
    r = {}
    for e, v in p.items():
        for f, w in q.items(): r[e+f] = r.get(e+f, 0) + v*w
    return {e: v for e, v in r.items() if v}
DELTA = {2: -1, -2: -1}
def cap(m, i):
    m2 = [(x+2 if x >= i else x) for x in m]; m2[i:i] = [i+1, i]; return tuple(m2)
def cup(m, i):
    p, q = m[i], m[i+1]; m = list(m); loop = False
    if p == i+1: loop = True
    else: m[p] = q; m[q] = p
    del m[i:i+2]; m = [(x-2 if x > i+1 else x) for x in m]; return tuple(m), loop
def run(word):
    """word: list of (op, i): ('cap',i),('cup',i),('x',i),('y',i),('F',i)= delta*f2 = delta*keep - e at i. Closed diagram -> poly in A."""
    state = {(): {0: 1}}
    for c, i in word:
        new = {}
        for m, p in state.items():
            if c == 'cap':
                padd(new.setdefault(cap(m, i), {}), p)
            elif c == 'cup':
                m2, loop = cup(m, i); padd(new.setdefault(m2, {}), pmul(p, DELTA) if loop else p)
            else:
                if c == 'x': ka, kb = (1, {1: 1}), {-1: 1}
                elif c == 'y': ka, kb = (1, {-1: 1}), {1: 1}
                elif c == 'F': ka, kb = (1, DELTA), {0: -1}
                padd(new.setdefault(m, {}), pmul(p, ka[1]))
                m2, loop = cup(m, i); q = pmul(p, DELTA) if loop else p
                padd(new.setdefault(cap(m2, i), {}), pmul(q, kb))
        state = {m: p for m, p in new.items() if p}
    assert set(state) <= {()}, state.keys()
    return state.get((), {})

def cover_word(D, n):
    """lift of the annular closure of D (n strands): closure of D.D, fundamental strands, braid closure on n strands."""
    w = [('cap', i) for i in range(n)]            # nested: positions 0..n-1 down strands, n..2n-1 closure arcs
    for _ in range(2):
        for g in D:
            if g[0] == 's': w.append(('x' if g[2] > 0 else 'y', g[1]))
            else: w += [('cup', g[1]), ('cap', g[1])]
    w += [('cup', n-1-k) for k in range(n)]
    return w
def orig_word(D, n, belt='x'):
    """axis at position 0 (closing at far right), 2-cabled strands at positions 1..2n, closure arcs 2n+1..4n.
    belt = full twist of the axis around the 2n down-strands at the cut level; f2 (delta-scaled) on every cable pair."""
    w = [('cap', 0)] + [('cap', 1+i) for i in range(2*n)]
    w += [(belt, i) for i in range(2*n)] + [(belt, i) for i in reversed(range(2*n))]
    w += [('F', 1+2*j) for j in range(n)]
    nF = n
    for g in D:
        p = 1 + 2*g[1]
        if g[0] == 's':
            c = 'x' if g[2] > 0 else 'y'
            w += [(c, p+1), (c, p), (c, p+2), (c, p+1)]
        else:  # colour-2 cup-cap between cables at p,p+1 and p+2,p+3: nested cup then nested cap, plus f2 on the new cap arc
            w += [('cup', p+1), ('cup', p), ('cap', p), ('cap', p+1), ('F', p)]
            nF += 1
    w += [('cup', 2*n - k) for k in range(2*n)] + [('cup', 0)]
    return w, nF

A, a, Q = S.symbols('A a Q', nonzero=True)
phi5 = Q**4 + Q**3 + Q**2 + Q + 1
def tolaurent(p, var): return sum(S.Integer(v)*var**e for e, v in p.items())
def E_plus(D, n):
    p = run(cover_word(D, n))
    assert all(e % 2 == 0 for e in p), 'odd a-power in cover'
    return S.expand(sum(S.Integer(v)*Q**(e//2) for e, v in p.items()))
def E_minus(D, n, belt='x'):
    w, nF = orig_word(D, n, belt)
    p = run(w)
    num = tolaurent(p, A); den = (-A**2 - A**-2)**(nF+1)     # delta^nF from scaled f2's, times Delta_1 = delta
    val = S.cancel(num/den)
    nn, dd = S.fraction(val)
    # express in t = A^4: require val to be a Laurent polynomial in A^4
    P = S.Poly(S.expand(nn), A); Dd = S.Poly(S.expand(dd), A)
    assert Dd.is_monomial, ('non-Laurent E_minus', dd)
    (dexp,), dco = Dd.terms()[0]
    out = 0
    for (e,), c in P.terms():
        k = e - dexp
        assert k % 4 == 0, ('A-exponent not mult of 4', k)
        out += S.Rational(c, dco) * (-1/Q)**(k//4)    # t = -Q^-1
    return S.expand(out)
def mod_phi5(expr):
    num, den = S.fraction(S.cancel(S.together(expr)))
    return S.rem(S.Poly(num, Q), S.Poly(phi5, Q)).as_expr()

if __name__ == '__main__':
    import sys
    Lm = lambda n: Q**(2*n) - (Q + 1/Q)*(-1/Q)**n
    Lp = lambda n: Q**(-3*n) + (Q**2 + 1 + Q**-2)*(-1/Q)**n
    allok = True
    for n in range(1, 6):
        D = [('s', j, +1) for j in range(n-1)]          # A_n = closure of sigma_1...sigma_{n-1}, type x
        em = E_minus(D, n); ep = E_plus(D, n)
        okm = S.simplify(em - (Q**-2)**(n-1)*Lm(n)) == 0
        okp = S.simplify(ep - (Q**3)**(n-1)*Lp(n)) == 0
        okz = mod_phi5(em - ep) == 0
        allok &= okm and okp and okz
        print(f'n={n}: E_-(A_n) == r_-^(n-1) L_n^- : {okm} | E_+(A_n) == r_+^(n-1) L_n^+ : {okp} | equal mod Phi5: {okz}')
        if n <= 3: print('   E_- =', S.factor(em), '\n   E_+ =', S.factor(ep))
    # belt type must not matter (mirror-symmetric belt)
    for n in (2, 3):
        D = [('s', j, +1) for j in range(n-1)]
        print(f'belt x vs y, n={n}:', S.simplify(E_minus(D, n, 'x') - E_minus(D, n, 'y')) == 0)
    # the other family A_n^y: E_- must NOT equal r_-^(n-1)L_n^- (handedness is detected)
    D = [('s', 0, -1), ('s', 1, -1)]
    print('A_3^y gives a different value (handedness detected):', S.simplify(E_minus(D, 3) - (Q**-2)**2*Lm(3)) != 0)
    # contractible loop and empty diagram
    print('empty: E_-', E_minus([], 1) if False else 'n/a', )
    print('GENERATORS ALL OK' if allok else 'GENERATOR FAILURE')
