"""critic: are regress's type-R lines (and the R directions of planes) AXIS-FREE families?
A family word V . B . U (B = the varying twist block, a token) is reduced by moves that are isotopies for EVERY member:
  free cancellation; far commutation of x0/y0 with x2,y2,x3,y3 (and with B when B = (x3 x3)^k; never with x1/y1 or B = (x1 x1)^k);
  deletion of an axis letter that reaches the BOTTOM end (R1 at the bottom vertex: engineB/extract BOT rule x0^{+-1}).
If no x0/y0 survives, every member is an axis-free width-two theta-curve, hence (SWAP-SUM LEMMA) K_k = K'_k # rK'_k with
K'_k the 4-plat closure of the arc along the axis.  Output: per line, axis-free or not, and the reduced family word."""
import sys, pickle, json
from collections import Counter
sys.dont_write_bytecode = True
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/regress')
from certify_summary import typ
OUT = '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/regress/out/'
INV = {'x0': 'y0', 'y0': 'x0', 'x1': 'y1', 'y1': 'x1', 'x2': 'y2', 'y2': 'x2', 'x3': 'y3', 'y3': 'x3'}
AX = {'x0', 'y0'}
def comm_ax(L, btype):
    if L in ('x2', 'y2', 'x3', 'y3', 'x0', 'y0'): return True
    if L == 'B3': return True
    return False
def reduce(W):
    W = list(W); changed = True
    while changed:
        changed = False
        # free reduction
        out = []
        for L in W:
            if out and L in INV and out[-1] == INV[L]: out.pop(); changed = True
            else: out.append(L)
        W = out
        # move each axis letter right; cancel with inverse or delete at the bottom end
        for i, L in enumerate(W):
            if L not in AX: continue
            j = i + 1
            while j < len(W) and W[j] != INV[L] and comm_ax(W[j], None): j += 1
            if j == len(W):                       # reached the bottom end: R1 at the bottom vertex
                W = W[:i] + W[i + 1:]; changed = True; break
            if W[j] == INV[L]:
                W = W[:i] + W[i + 1:j] + W[j + 1:]; changed = True; break
            # try moving left to an inverse
            j = i - 1
            while j >= 0 and W[j] != INV[L] and comm_ax(W[j], None): j -= 1
            if j >= 0 and W[j] == INV[L]:
                W = W[:j] + W[j + 1:i] + W[i + 1:]; changed = True; break
    return W
def twist_fixed(m, n, vary):
    """offset twists with the varying site replaced by a token: vary = 'X3' -> B3 token for x3 part; 'X1' -> B1 token"""
    a = (['x1', 'x1'] * m if m > 0 else ['y1', 'y1'] * (-m))
    b = (['x3', 'x3'] * n if n > 0 else ['y3', 'y3'] * (-n))
    if vary == 'X3': return a + ['B3']
    if vary == 'X1': return ['B1'] + b
    return a + b
res = {}
for D in (5, 6):
    d2 = pickle.load(open(OUT + 'classify2_%d_%d.pkl' % (D, D), 'rb')); r3 = pickle.load(open(OUT + 'classify3_%d_%d.pkl' % (D, D), 'rb'))
    lines = d2['lines']; tab = Counter(); keep = []
    for (i, c, ex, nc, pt, Wb, cert) in d2['res']:
        t = typ(c, r3.get(i))
        if t not in ('R-residual', 'PLANE-with-R'): continue
        kind, wt, wb, d, m0, n0 = lines[i][:6]
        V = [a for a in wt.split('.') if a]; U = [a for a in wb.split('.') if a]
        if t == 'R-residual':
            vary = 'X3' if d == (0, 1) else 'X1'
            fam = V + twist_fixed(m0, n0, vary) + U
            red = reduce(fam); free = not any(a in AX for a in red)
            tab[(t, vary, free)] += 1
            keep.append({'type': t, 'vary': vary, 'V': wt, 'U': wb, 'd': list(d), 'm0': m0, 'n0': n0, 'axis_free': free, 'reduced': '.'.join(red)})
        else:
            r = r3.get(i)
            for site, v in r.items():
                if not v.startswith('NONE'): continue
                fam = V + (['B3'] if site == 'X3' else ['B1']) + U   # plane offset (0,0); other site's twist = 0
                red = reduce(fam); free = not any(a in AX for a in red)
                tab[(t, site, free)] += 1
                keep.append({'type': t, 'vary': site, 'V': wt, 'U': wb, 'axis_free': free, 'reduced': '.'.join(red)})
    res[D] = keep
    print('ENUM', D, dict(tab))
    nf = [k for k in keep if not k['axis_free']]
    for k in nf[:8]: print('   NOT axis-free:', k['type'], k['vary'], k['V'], '|', k['U'], '->', k['reduced'])
json.dump(res, open('/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/critic/rlines/rlines_axisfree.json', 'w'))
