#!/usr/bin/env python3
"""Run kht++ -c2 -q -s on half-diagram words and test the statement of Theorem 2.4 on the output.
usage: runcheck.py WORKDIR OUT.jsonl TIMEOUT NWORKERS < words   (one word per line, optional tab-separated tag)
Every record: own diagram data (signs, genus bounds), own cube data, kht++ generators, verdict fields."""
import sys, os, json, hashlib, collections
from concurrent.futures import ThreadPoolExecutor
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/tools')
import sidiag as S, khtio, light, khtorient
import gtilde, alex, kauffman

def diagram_data(word):
    hs = S.half_signs(word)
    if hs is None:
        return None
    K = hs['K']
    half = S.parse(word)
    ap = K.alexander_poly()
    b, cc = light.typeb(S.band_word(half, 0))
    P, (M, Et), (m, Eb) = b
    uc = S.unit_of(P)
    c, wr = hs['c'], hs['wr']
    d0 = 2 * c - 4 * wr
    s = K.seifert_circles()
    rec = dict(word=word, c=c, wr=wr, c_axis=hs['c_axis'], c_off=hs['c_off'], one_sign=hs['one_sign'], n_full=K.n,
               seifert=s, gD=K.diagram_genus(), alex=ap, galex=(len(ap) - 1) // 2,
               M=M, Etop=Et, m=m, Ebot=Eb, unit_cube=uc, d0=d0,
               Jcube={e - uc[1]: v * uc[0] for e, v in P.items()} if uc else None)
    # tools/alex.py and tools/kauffman.py (as the task prescribes) for knot / non-triviality
    rec['alexpy_det'] = alex.alex_eval(word, -1); rec['alexpy_2'] = alex.alex_eval(word, 2); rec['alexpy_3'] = alex.alex_eval(word, 3)
    br = kauffman.bracket(word)
    rec['kauffman_terms'] = None if br is None else len(br)
    rec['kauffman_key'] = None if br is None else list(kauffman.key(br))
    return rec

def kht_data(workdir, word, timeout, sub='examples/words'):
    name = 'w' + hashlib.md5(word.encode()).hexdigest()[:12]
    r = khtio.run_kht(workdir, name, word, timeout=timeout, sub=sub)
    out = dict(name=name, time=r['time'], rc=r['rc'])
    if not r['bn_file']:
        out['error'] = 'no output'; out['tail'] = r.get('tail', '')
        return out
    gens = khtio.b_generators(r['bn_file'])
    out['gens'] = gens
    out['dimBN'] = sum(len(ch['gens']) for ch in khtio.read_bn(r['bn_file']))
    khr = khtio.read_khr(r['kh_file']) if r['kh_file'] else []
    out['khr'] = khr
    # the quotient word kht++ actually used (before simplification)
    svg = os.path.join(workdir, sub, name, name + '-q.svg')
    out['svg_word'] = khtio.svg_levels(svg) if os.path.exists(svg) else None
    return out

def verdict(d, k):
    """d: diagram data, k: kht data. returns dict of checks"""
    v = {}
    if 'gens' not in k:
        v['status'] = 'no kht++ output'; return v
    gens = [tuple(g) for g in k['gens']]
    P = {}
    for (h, q) in gens:
        S.padd(P, {q: (-1) ** (h % 2)})
    u = S.unit_of(P)
    v['unit_kht'] = u
    if u is None:
        v['status'] = 'chi(N) not a unit mod (q^2+1)^2'; return v
    dq = u[1]
    js = gtilde.jset(k['khr']) if (k['khr'] and gtilde.valid(k['khr'])) else None
    v['jset_ok'] = None
    if js is not None:
        kk, j, pts = js
        g2 = sorted(((q - 2 * dd) // 2, q) for q, dd in pts)
        v['jset_ok'] = (g2 == sorted(gens)); v['k'] = kk; v['j'] = j
        v['unit_is_24j'] = (u == (1, 24 * j))
    J = {e - dq: c * u[0] for e, c in P.items()}
    v['J_equal_cube'] = (d['Jcube'] is not None and J == {int(a): b for a, b in d['Jcube'].items()})
    v['J_is_unit'] = (len(J) == 1)
    v['gens_in_unit_degree'] = [g for g in gens if g[1] == dq]
    v['coef_at_unit'] = P.get(dq, 0)
    qs = [q for h, q in gens]
    v['qmin'] = min(qs); v['qmax'] = max(qs); v['dimN'] = len(gens); v['d'] = dq
    half = S.parse(d['word'])
    v['svg_ok'] = (k['svg_word'] == S.band_word(half, d['wr'])) if k.get('svg_word') is not None else None
    if d['one_sign']:
        g = d['gD']
        if d['wr'] < 0:
            dist = dq - v['qmax']; side = v['qmax'] < dq; E = d['Etop']; ext = [x for x in gens if x[1] == v['qmax']]
            cube_edge = d['d0'] - d['M']
        else:
            dist = v['qmin'] - dq; side = v['qmin'] > dq; E = d['Ebot']; ext = [x for x in gens if x[1] == v['qmin']]
            cube_edge = d['m'] - d['d0']
        v['dist'] = dist; v['E'] = E; v['cube_edge'] = cube_edge
        v['ext_rel_unit'] = [(x[0] - (8 * v['j'] if js else 0), x[1] - dq) for x in ext] if js else None
        if g >= 1:
            ok = (side and not v['gens_in_unit_degree'] and v['coef_at_unit'] == 0 and dist >= 2 * g and cube_edge == 2 * g
                  and ((dist == 2 * g) == (E == 1)) and not v['J_is_unit'])
            if E == 1 and js:
                ok = ok and v['ext_rel_unit'] == [(0, -2 * g if d['wr'] < 0 else 2 * g)]
        else:
            ok = (v['dimN'] == 1 and v['J_is_unit'] and (not js or gens == [(8 * v['j'], 24 * v['j'])]))
        v['theorem_ok'] = bool(ok and v['J_equal_cube'] and (v['jset_ok'] in (True, None)) and v.get('unit_is_24j', True))
    v['status'] = 'done'
    return v

def process(args):
    workdir, word, tag, timeout = args
    d = diagram_data(word)
    if d is None:
        return dict(word=word, tag=tag, error='not a knot')
    k = kht_data(workdir, word, timeout)
    v = verdict(d, k)
    d2 = dict(d); d2['Jcube'] = {str(a): b for a, b in d['Jcube'].items()} if d['Jcube'] else None
    return dict(word=word, tag=tag, diagram=d2, kht=k, verdict=v)

if __name__ == '__main__':
    workdir, outp, timeout, nw = sys.argv[1], sys.argv[2], int(sys.argv[3]), int(sys.argv[4])
    os.makedirs(workdir, exist_ok=True)
    items = []
    for l in sys.stdin:
        l = l.rstrip('\n')
        if not l.strip():
            continue
        parts = l.split('\t')
        items.append((workdir, parts[0].strip(), parts[1] if len(parts) > 1 else '', timeout))
    done = set()
    if os.path.exists(outp):
        for l in open(outp):
            try:
                done.add(json.loads(l)['word'])
            except Exception:
                pass
    items = [it for it in items if it[1] not in done]
    fo = open(outp, 'a')
    with ThreadPoolExecutor(max_workers=nw) as ex:
        for rec in ex.map(process, items):
            fo.write(json.dumps(rec, ensure_ascii=False) + '\n'); fo.flush()
            v = rec.get('verdict', {}); d = rec.get('diagram', {})
            print(rec['word'], rec.get('tag', ''), 'c=%s wr=%s gD=%s' % (d.get('c'), d.get('wr'), d.get('gD')),
                  v.get('status'), 'time', rec.get('kht', {}).get('time'), 'dimN', v.get('dimN'), 'dist', v.get('dist'), 'E', v.get('E'),
                  'theorem_ok', v.get('theorem_ok'), flush=True)
