#!/usr/bin/env python3
"""Chain-level test of the UNIT POSITION formula and of the count in Theorem 2.4 on a list of all-negative words
(one per line) and on their mirror images (all-positive). No kht++ here: own state sum on the twist-free band diagram.
usage: exh3.py WORDS.txt OUT.jsonl"""
import sys, os, json, collections, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import sidiag as S, light
from gen3 import mirror

def analyse(w):
    hs = S.half_signs(w)
    if hs is None:
        return None
    K = hs['K']
    c, wr, ca, co = hs['c'], hs['wr'], hs['c_axis'], hs['c_off']
    s = K.seifert_circles()
    gD = K.diagram_genus()
    ap = K.alexander_poly()
    galex = (len(ap) - 1) // 2
    half = S.parse(w)
    b, cc = light.typeb(S.band_word(half, 0))
    P, (M, Et), (m, Eb) = b
    u = S.unit_of(P)
    d0 = 2 * c - 4 * wr
    rec = dict(w=w, c=c, wr=wr, ca=ca, co=co, s=s, gD=gD, galex=galex, det=abs(sum(ap[i] * (-1) ** i for i in range(len(ap)))),
               M=M, Et=Et, m=m, Eb=Eb, unit=u, d0=d0, coef=P.get(d0, 0), nterms=len(P), mono=(len(P) == 1), one=hs['one_sign'],
               ap=ap)
    return rec

if __name__ == '__main__':
    words = [l.strip() for l in open(sys.argv[1]) if l.strip()]
    out = open(sys.argv[2], 'w')
    st = collections.Counter(); fails = collections.defaultdict(list)
    t0 = time.time()
    for n, w0 in enumerate(words):
        for sign, w in ((-1, w0), (1, mirror(w0))):
            r = analyse(w)
            if r is None:
                fails['not a knot'].append(w); continue
            st['words'] += 1
            c = r['c']
            if not r['one'] or r['wr'] != sign * c:
                fails['not one-sign as constructed'].append(w)
            if r['unit'] != (1, r['d0']):
                fails['unit != (+, 2c-4wr)'].append((w, r['unit'], r['d0']))
            l2 = r['s'] - r['ca'] - 1
            if l2 % 2 or r['gD'] != r['co'] - l2 // 2:
                fails['Seifert circle count != c_axis + 1 + 2l / genus != c_off - l'].append(w)
            l = l2 // 2
            if sign < 0:
                edge = r['d0'] - r['M']; ks = r['M'] - 4 * c; E = r['Et']
            else:
                edge = r['m'] - r['d0']; ks = -r['m']; E = r['Eb']
            if ks != 2 * r['ca'] + 2 * l:
                fails['k(s_extreme) != 2 c_axis + 2 l'].append((w, ks, r['ca'], l))
            if edge != 2 * r['gD']:
                fails['cube edge != 2 * diagram genus'].append((w, edge, r['gD']))
            if r['galex'] != r['gD']:
                fails['half span of Alexander != diagram genus'].append((w, r['galex'], r['gD'], r['ap']))
            if r['gD'] >= 1:
                st['genus>=1'] += 1
                if r['coef'] != 0:
                    fails['non-zero coefficient of chi in the unit degree, genus >= 1'].append(w)
                if r['mono']:
                    fails['chi is a monomial (FLAT) with genus >= 1'].append(w)
            else:
                st['genus 0'] += 1
                if not (r['mono'] and r['coef'] == 1):
                    fails['genus 0 but chi is not +q^d0'].append(w)
            st[('g', r['gD'])] += 1
            st[('adequate end' if E == 1 else 'non-adequate end')] += 1
            st[('c', c)] += 1
            r['E'] = E; r['l'] = l; r['sign'] = sign
            del r['one']
            out.write(json.dumps(r) + '\n')
        if n % 5000 == 0:
            print(n, len(words), round(time.time() - t0), 's', flush=True)
    print('STATS', dict((str(k), v) for k, v in sorted(st.items(), key=lambda kv: str(kv[0]))))
    print('FAILURES:')
    for k, v in fails.items():
        print('  ', k, ':', len(v), v[:8])
    if not fails:
        print('   none')
