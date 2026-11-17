"""Check candidate absorption rules against the rho_2 scalars (exact, integral t-form of engineB/rho2.py).
TOP: h at the START of W (acts first): need rho(h) f0 = c f0  (f0 = V['l1.l1']).
BOT: h at the END of W (adjacent to u2.u2): need PHI rho(h) = c PHI  (PHI = PHIT['u2.u2']).
rho(W) = M[L_n]...M[L_1] (first letter acts first)."""
import sys, itertools, json, random
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineB')
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mont')
import rho2
MT, VT, PHIT = rho2.normalised()
def tmul(p, q): return rho2._tmul(p, q)
def tadd(p, q): return rho2._tadd(p, q)
def apply_vec(W, v):
    for L in W:
        M = MT[L]; v = [rho2._rowdot_t(M[i], v) for i in range(9)]
    return v
def apply_covec(W, w):
    # w . M[L_n] ... M[L_1] : apply letters from the END of the word first
    for L in reversed(W):
        M = MT[L]
        w = [ {e: c for e, c in sum_cols(w, M, j).items() if c} for j in range(9)]
    return w
def sum_cols(w, M, j):
    r = {}
    for i in range(9):
        if w[i] and M[i][j]:
            for e, a in w[i].items():
                for f, b in M[i][j].items(): r[e + f] = r.get(e + f, 0) + a * b
    return r
def proportional(u, v):
    """exact: is u = c v with c a Laurent polynomial (we report c if it is a monomial or polynomial ratio)? test via cross products"""
    # u_i v_j - u_j v_i = 0 for all i, j
    for i in range(9):
        for j in range(i + 1, 9):
            a = tadd(tmul(u[i], v[j]), {e: -c for e, c in tmul(u[j], v[i]).items()})
            if a: return False
    return True
def ratio(u, v):
    for i in range(9):
        if v[i]:
            return (u[i], v[i])
f0 = VT['l1.l1']; PH = PHIT['u2.u2']
TOP = {'x1': ['x1'], 'y1': ['y1'], 'x3': ['x3'], 'y3': ['y3'],
       'exch+ x2.x1.x3.x2': ['x2', 'x1', 'x3', 'x2'], 'exch- y2.y1.y3.y2': ['y2', 'y1', 'y3', 'y2'],
       'loopB_around_A x2.x1.x1.x2': ['x2', 'x1', 'x1', 'x2'], 'loopA_around_B x2.x3.x3.x2': ['x2', 'x3', 'x3', 'x2'],
       'axloop_A x0.x1.x0.y1': ['x0', 'x1', 'x0', 'y1'], 'Delta2(ax,A) x0.x1.x0.x1': ['x0', 'x1', 'x0', 'x1'],
       'NEG x0': ['x0'], 'NEG x2': ['x2'], 'NEG x2.x2': ['x2', 'x2']}
BOT = {'x0': ['x0'], 'y0': ['y0'], 'x2': ['x2'], 'y2': ['y2'],
       'leg0_loop_C x1.x2.x2.x1': ['x1', 'x2', 'x2', 'x1'], 'leg3_loop_C x3.x2.x2.x3': ['x3', 'x2', 'x2', 'x3'],
       'NEG x1': ['x1'], 'NEG x3': ['x3'], 'NEG leg1_loop_axleg0 x1.x0.x1': ['x1', 'x0', 'x1'], 'NEG x3.x3': ['x3', 'x3']}
out = {}
for name, W in TOP.items():
    v = apply_vec(W, f0); ok = proportional(v, f0); out['TOP ' + name] = ok
    print('TOP', name, 'eigen:', ok, ('ratio ' + str(ratio(v, f0))) if ok else '')
for name, W in BOT.items():
    w = apply_covec(W, PH); ok = proportional(w, PH); out['BOT ' + name] = ok
    print('BOT', name, 'eigen:', ok, ('ratio ' + str(ratio(w, PH))) if ok else '')
json.dump(out, open('/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/cert/extract/scalars_check.json', 'w'), indent=1)
