"""GLOBAL disc criterion for a twist site (exact, rigorous via Dehn's lemma on the sphere S' around the closure's H-tree).
theta = T' u H:  H = the closure's H-tree {a - v_bot - p, E - v_top - q, A_seg} in a ball B_H; T' = everything else
(axis strand + caps + braid + cup) in B' = S^3 - B_H, partial B' = S' with punctures a, E, p = closure leg 0, q = closure leg 3.
A site twist tau_c at the junction equals tau_{c''} at the closure level, c'' = U_*(c).  If c'' is isotopic off the cup disc
(D_12, boundary h = g2 g3) it lives on S'.  Then:
  'T-disc'   : c'' null-homotopic in pi_1(B' - T') = F_3/<<psi_V(U_*^-1(h))>>  => bounds a disc in B' - T' (Dehn) => tau fixes T';
  'H-vertex' : c'' = curve around {a, p} (= around {E, q}) on S' => tau rotates a vertex of H => fixes H.
Either way every knot of the twist family is isotopic to the base knot.
Word problem in F_3/<<r>>: whitehead.trivial_in_quotient (exact when r is primitive, i.e. when pi_1(B'-T') is free)."""
import sys
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/regress')
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/regress/orig')
import geo, whitehead, fgroup
INV = geo.INV
def cyc5(w):
    w = list(fgroup.red(w))
    while len(w) >= 2 and w[0] == -w[-1]: w = w[1:-1]
    return tuple(w)
def to_h_basis(w):
    """F_5 symbols 1..5 (g0..g4); rewrite with g2 = h g3^-1 (h = symbol 6) -> cyclically reduced word in {1,2,6,4,5}"""
    out = []
    for a in w:
        if abs(a) == 3: out.extend([6, -4] if a > 0 else [4, -6])
        else: out.append(a)
    return cyc5(out)
def is_cyc_conj(w, target):
    w = cyc5(w); t = cyc5(target)
    if len(w) != len(t): return False
    for tt in (t, tuple(-a for a in reversed(t))):
        for k in range(len(w)):
            if w[k:] + w[:k] == tt: return True
    return False
def site_disc(V, U, curve):
    """V: words above the site, U: below (lists of letters); curve: (2,3) [X1] or (4,5) [X3]"""
    cpp = geo.push_down(U, curve)
    hb = to_h_basis(cpp)
    if any(abs(a) == 4 for a in hb): return 'not-cup-avoiding'
    sprime = cyc5(tuple(a for a in hb if abs(a) != 6))
    if not sprime: return 'S-trivial'                      # c'' bounds a disc on S' itself (cup curve)
    if is_cyc_conj(sprime, (1, 2)): return 'H-vertex'
    w = geo.subst(geo.psi_top(V), curve)
    cupc = (3, 4)
    for L in reversed(U): cupc = fgroup.act(INV[L], cupc)  # U_*^-1(g2 g3)
    r = geo.subst(geo.psi_top(V), cupc)
    t = whitehead.trivial_in_quotient(w, r)
    if t is None: return 'r-not-primitive'
    return 'T-disc' if t else 'cup-avoid-no-disc'
if __name__ == '__main__':
    print('plane V=x2 U=x2.x3, X1 site:', site_disc(['x2'], ['x2', 'x3'], (2, 3)))
    print('plane V=x2 U=x2.x3, X3 site:', site_disc(['x2'], ['x2', 'x3'], (4, 5)))
    print('offset V=x0.x2.x1.x3 U=x2.x0.x1, X3 site:', site_disc('x0.x2.x1.x3'.split('.'), 'x2.x0.x1'.split('.'), (4, 5)))
    print('offset V=x0.y2 U=x2.y0.x1, X3 site:', site_disc('x0.y2'.split('.'), 'x2.y0.x1'.split('.'), (4, 5)))
    print('caps V= U=, X1:', site_disc([], [], (2, 3)), ' X3:', site_disc([], [], (4, 5)))
    print('codex V=x2.x1 U=x1, X1:', site_disc(['x2', 'x1'], ['x1'], (2, 3)), ' X3:', site_disc(['x2', 'x1'], ['x1'], (4, 5)))
    print('closure x0 absorbed? V=x2 U=x0, axis curve (1,2):', site_disc(['x2'], ['x0'], (1, 2)))
