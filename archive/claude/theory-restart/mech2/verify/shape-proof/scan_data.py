#!/usr/bin/env python3
"""Referee's own parser of kht++ chain files (cxBNr-*), and a check of Theorem A and of the first-order extension
equation (*) on the actual data.  Read-only on the data; writes nothing outside stdout."""
import sys, re, os, collections
from tdu import *

ROOT = '/Users/calebbarnett/jones-lanes/theory-restart'
SYM = {'⬮': B, '⬯': C}

def parse_arrow(tok, left_idem, right_idem):
    fwd = '>' in tok
    bwd = '<' in tok
    assert fwd != bwd, tok
    kind = 'S' if '~' in tok else 'D'
    assert ('—' in tok) != ('~' in tok), tok
    m = re.search(r'([SD])(?:\^(\d+))?', tok)
    neg = '(-' in tok
    if m:
        assert m.group(1) == kind, tok
        k = int(m.group(2)) if m.group(2) else 1
    else:
        k = 1 if kind == 'D' else (1 if left_idem != right_idem else 2)
    # consistency of idempotents
    if kind == 'D':
        assert left_idem == right_idem, (tok, left_idem, right_idem)
    else:
        assert (left_idem == right_idem) == (k % 2 == 0), (tok, left_idem, right_idem)
    return kind, k, (1 if fwd else -1), neg

def parse_file(path):
    """returns list of components: dict(gens=[(idem,h,q)], arrows=[(i,j,(kind,k,src,tgt))], compact=bool, line=str)"""
    comps = []
    signs = False
    for line in open(path, encoding='utf-8'):
        line = line.rstrip('\n')
        if not line.strip() or line.startswith('%'):
            continue
        m = re.match(r'^\s*(\d+)\)\s*h\^\s*(-?\d+)\s*q\^\s*(-?\d+)\s*δ\^\s*(-?\d+(?:/\d+)?)\s*([⬮⬯].*)$', line)
        if not m:
            raise ValueError('unparsed line in %s: %r' % (path, line))
        h0, q0 = int(m.group(2)), int(m.group(3))
        body = m.group(5)
        syms = re.findall('[⬮⬯]', body)
        toks = re.split('[⬮⬯]', body)
        assert toks[0] == '', body
        idems = [SYM[s] for s in syms]
        arrows_tok = toks[1:]            # token after each symbol; last one empty unless cyclic
        compact = arrows_tok[-1] != ''
        n = len(idems)
        gens = [[idems[0], h0, q0]] + [[idems[i], None, None] for i in range(1, n)]
        arrows = []
        for i, tok in enumerate(arrows_tok):
            if tok == '':
                assert i == n - 1
                continue
            j = (i + 1) % n
            kind, k, sgn, neg = parse_arrow(tok, idems[i], idems[j])
            signs = signs or neg
            dq = 2 * k if kind == 'D' else k
            if sgn > 0:
                hj, qj = gens[i][1] + 1, gens[i][2] + dq
                arrows.append((i, j, (kind, k, idems[i], idems[j])))
            else:
                hj, qj = gens[i][1] - 1, gens[i][2] - dq
                arrows.append((j, i, (kind, k, idems[j], idems[i])))
            if gens[j][1] is None:
                gens[j][1], gens[j][2] = hj, qj
            else:
                assert (gens[j][1], gens[j][2]) == (hj, qj), 'cyclic chain does not close up in %s: %s' % (path, line)
        comps.append({'gens': [tuple(g) for g in gens], 'arrows': arrows, 'compact': compact, 'line': line})
    return comps, signs

def analyse_component(c):
    """returns dict: nb, unit (U1 and U2), reasons, composable (number of composable D/P junctions), kind."""
    gens, arrows = c['gens'], c['arrows']
    n = len(gens)
    nb = sum(1 for g in gens if g[0] == B)
    reasons = []
    # (U1)
    for (i, j, e) in arrows:
        if gens[i][0] == B and gens[j][0] == B and not (e[0] == 'D' and e[1] == 1):
            reasons.append('U1: b-b arrow %s' % name(e))
    # neighbours along the curve: arrows are stored in order of the chain: arrow t joins position t and t+1 (mod n)
    # rebuild adjacency by position
    adj = collections.defaultdict(list)    # gen -> list of (other gen, arrow index)
    for t, (i, j, e) in enumerate(arrows):
        adj[i].append((j, t)); adj[j].append((i, t))
    # maximal chains of c-generators: walk along the curve
    runs = []        # (b_start, b_end, direction, ok)
    order = list(range(n))
    # the chain order is the position order 0..n-1 (cyclic if compact)
    pos_arrow = {}
    for t, (i, j, e) in enumerate(arrows):
        pos_arrow[t] = (i, j, e)
    # arrows[t] joins positions t and (t+1) % n by construction of the parser
    def step(t):
        i, j, e = arrows[t]
        a, b = t, (t + 1) % n
        fwd = (i == a and j == b)
        return a, b, e, (1 if fwd else -1)
    junction = collections.defaultdict(dict)   # b-gen -> {'D': +1 (enters) / -1 (leaves), 'P': ...}
    T = len(arrows)
    t = 0
    # D-arrows between b generators
    for t in range(T):
        a, b, e, sgn = step(t)
        if gens[a][0] == B and gens[b][0] == B and e[0] == 'D':
            junction[a]['D'] = -1 if sgn > 0 else 1     # leaves a if forward
            junction[b]['D'] = 1 if sgn > 0 else -1
    # c-chains
    visited = set()
    for t in range(T):
        a, b, e, sgn = step(t)
        if gens[a][0] == B and gens[b][0] == C:
            # walk forward from a through c-generators
            chain = [(e, sgn)]
            tt = t
            end = None
            while True:
                tt2 = tt + 1
                if tt2 >= T:
                    if c['compact']:
                        tt2 = 0
                    else:
                        break
                if not c['compact'] and tt2 >= T:
                    break
                a2, b2, e2, s2 = step(tt2)
                chain.append((e2, s2))
                tt = tt2
                if gens[b2][0] == B:
                    end = b2
                    break
            if end is None:
                continue     # a tail (going forward to the end of the arc)
            labels = [(x[0][0], x[0][1]) for x in chain]
            sgns = set(x[1] for x in chain)
            ok = labels == [('S', 1), ('D', 1), ('S', 2), ('D', 1), ('S', 1)] and len(sgns) == 1
            if not ok:
                reasons.append('U2: chain %s signs %s' % (' '.join(name((k, p, 0, 0)) for (k, p) in labels), ''.join('+' if x[1] > 0 else '-' for x in chain)))
            else:
                s = chain[0][1]
                junction[a]['P'] = -1 if s > 0 else 1
                junction[end]['P'] = 1 if s > 0 else -1
    ncomp = sum(1 for g, d in junction.items() if 'D' in d and 'P' in d and d['D'] != d['P'])
    nnon = sum(1 for g, d in junction.items() if 'D' in d and 'P' in d and d['D'] == d['P'])
    unit = not reasons
    is_square = False
    if c['compact'] and unit and nb == 4 and n == 12:
        is_square = True
    return {'nb': nb, 'n': n, 'unit': unit, 'reasons': reasons, 'composable': ncomp, 'noncomposable': nnon, 'compact': c['compact'], 'square': is_square}

def to_td(comps):
    td = TD()
    for ci, c in enumerate(comps):
        off = len(td.gens)
        for gi, (idem, h, q) in enumerate(c['gens']):
            td.add_gen(idem, h, q, '%d.%s%d' % (ci + 1, idem, gi))
        for (i, j, e) in c['arrows']:
            td.add_arrow(i + off, j + off, e)
    return td

def all_files():
    files = []
    for dp, dn, fn in os.walk(ROOT):
        if '/verify/shape-proof' in dp:
            continue
        for f in fn:
            if f.startswith('cxBNr-'):
                files.append(os.path.join(dp, f))
    return sorted(files)

if __name__ == '__main__':
    do_first_order = '--first-order' in sys.argv
    maxgens = 100000
    for a in sys.argv:
        if a.startswith('--maxgens='):
            maxgens = int(a.split('=')[1])
    files = all_files()
    stats = collections.Counter()
    violations = []
    nonunit = []
    parity_bad = []
    fo_fail = []
    fo_done = 0
    for f in files:
        try:
            comps, signs = parse_file(f)
        except Exception as ex:
            stats['unparsed files'] += 1
            print('PARSE ERROR', f, ex)
            continue
        stats['files'] += 1
        # q-parity by idempotent over the whole file
        par = {B: set(), C: set()}
        for c in comps:
            for (idem, h, q) in c['gens']:
                par[idem].add(q % 2)
        if len(par[B]) > 1 or len(par[C]) > 1 or (par[B] and par[C] and par[B] == par[C]):
            parity_bad.append(f)
        for ci, c in enumerate(comps):
            a = analyse_component(c)
            stats['components'] += 1
            if a['nb'] == 0:
                stats['components without b-generator (%s)' % ('compact' if a['compact'] else 'arc')] += 1
                continue
            if not a['unit']:
                stats['non-unit components (%s)' % ('compact' if a['compact'] else 'arc')] += 1
                nonunit.append((f, ci + 1, a['compact'], a['reasons'][:3], a['composable']))
                continue
            if a['compact']:
                stats['unit compact components'] += 1
                if a['square'] and a['composable'] == 2 and a['noncomposable'] == 2:
                    stats['unit compact = unit square'] += 1
                else:
                    violations.append((f, ci + 1, 'compact unit-arrow component that is not the unit square', c['line']))
            else:
                stats['unit arcs'] += 1
                if a['composable'] == 0:
                    stats['unit arcs without composable junction'] += 1
                else:
                    violations.append((f, ci + 1, 'arc with unit arrows and %d composable junction(s)' % a['composable'], c['line']))
        if do_first_order and not signs and '-c2' in os.path.basename(f) or (do_first_order and not signs and re.search(r'cxBNr-(q|qs|s|d)?$', os.path.basename(f))):
            td = to_td(comps)
            if len(td.gens) <= maxgens:
                assert td.check_d2() and td.check_curve_form()
                res = first_order(td)
                fo_done += 1
                if not res['solvable']:
                    fo_fail.append(f)
    for k, v in sorted(stats.items()):
        print('%-55s %d' % (k, v))
    print('q-parity by idempotent violated in %d files' % len(parity_bad))
    for f in parity_bad[:10]:
        print('   ', f)
    print('VIOLATIONS of Theorem A among unit-arrow components with a b-generator: %d' % len(violations))
    for v in violations[:40]:
        print('   ', v)
    print('non-unit components (with a b-generator): %d' % len(nonunit))
    seen = set()
    for (f, ci, compact, reasons, ncomp) in nonunit:
        key = (os.path.basename(os.path.dirname(f)), ci)
        print('    %s comp %d %s: %s; composable D/P junctions among the unit parts: %d' % (f.replace(ROOT + '/', ''), ci, 'COMPACT' if compact else 'arc', '; '.join(reasons), ncomp))
    if do_first_order:
        print('first-order equation (*) solved on %d whole F_2 complexes; NOT solvable for %d' % (fo_done, len(fo_fail)))
        for f in fo_fail[:20]:
            print('   ', f)
