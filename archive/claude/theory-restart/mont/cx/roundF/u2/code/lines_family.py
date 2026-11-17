"""lines_family.py -- certify engineB's unit-valued twist LINES as whole infinite families (all k, not only the 5 sampled
points), and Codex's fixed regression family for ALL m.
A line at junction (V, U) with offset (m0, n0) and direction d: K_k = closure of V.(x1x1)^m.(x3x3)^n.U, (m,n) = (m0,n0)+k d.
x1 and x3 commute, so the varying block (x1x1 for d = (1,0), x3x3 for d = (0,1), x1x1.y3y3 for Codex's d = (1,-1)) can be
placed right after V, right after V + the fixed block, right before U, or right before the fixed block + U.  If the varying
block is a STABILISER of one of these top tangles (from the bottom side) or bottom tangles (from the top side) -- tested
exactly with Lemma K (tangle_kernel.py) -- then every K_k is isotopic to every other one, so a single CERTIFIED point
certifies the whole line.  usage: lines_family.py OUT.json"""
import sys, os, json
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import tangle_kernel as TK
def blk(letter, k):
    inv = {'x1': 'y1', 'x3': 'y3', 'y1': 'x1', 'y3': 'x3'}
    return [letter] * (2 * k) if k >= 0 else [inv[letter]] * (-2 * k)
def line_ok(V, U, d, off):
    m0, n0 = off
    if d == (0, 1): var = ['x3', 'x3']; fixed = blk('x1', m0)
    elif d == (1, 0): var = ['x1', 'x1']; fixed = blk('x3', n0)
    elif d == (1, -1): var = ['x1', 'x1', 'y3', 'y3']; fixed = blk('x1', m0) + blk('x3', n0)
    else: return None
    reasons = []
    for top in (V, V + fixed):
        if TK.same_top(top, top + var): reasons.append('top stabiliser after %s' % ('V' if top is V else 'V+fixed'))
    for bot in (U, fixed + U):
        if TK.same_bottom(bot, var + bot): reasons.append('bottom stabiliser before %s' % ('U' if bot is U else 'fixed+U'))
    return reasons
if __name__ == '__main__':
    d = json.load(open('/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/cert/extract/data/s3b_items.json'))['items']
    lines = {}
    for W, p in d:
        key = (p['V'], p['U'], tuple(p['direction']), tuple(p['offset']))
        lines.setdefault(key, []).append(p['k'])
    from collections import Counter
    res = []; c = Counter()
    for (V, U, dd, off), ks in lines.items():
        Vl = [x for x in V.split('.') if x]; Ul = [x for x in U.split('.') if x]
        r = line_ok(Vl, Ul, dd, off)
        c['geometric' if r else 'NOT_PROVED'] += 1
        res.append({'V': V, 'U': U, 'direction': dd, 'offset': off, 'reasons': r})
    codex = line_ok(['x2', 'x1'], ['x1'], (1, -1), (0, 0))
    summ = {'unit_lines': len(lines), 'whole_line_isotopy_PROVED': c['geometric'], 'NOT_PROVED': c['NOT_PROVED'],
            'codex_family_V=x2.x1_U=x1_dir(1,-1)': codex,
            'reason_counts': dict(Counter(tuple(r['reasons'])[:1] and r['reasons'][0] for r in res if r['reasons']))}
    print(json.dumps(summ, default=str))
    json.dump({'summary': summ, 'lines': res}, open(sys.argv[1], 'w'), default=str)
