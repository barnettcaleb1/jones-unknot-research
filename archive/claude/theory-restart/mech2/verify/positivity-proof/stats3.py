import json
rows = json.load(open('sweep.json'))
A=set();B=set();C=set();P=set()
for r in rows:
    M, m, d0 = r['M'], r['m'], r['d0']
    nb1, nb0 = len(r['bad1']), len(r['bad0'])
    if d0 > M or d0 < m: A.add(r['name'])
    Mt = M - (2 if nb1 else 0); mt = m + (2 if nb0 else 0)
    if d0 > Mt or d0 < mt: B.add(r['name'])
    if (nb1 == 0 and d0 != M) or (nb0 == 0 and d0 != m): C.add(r['name'])
    if abs(r['wr']) == r['c']: P.add(r['name'])
print('A', len(A), 'B', len(B), 'C', len(C), 'P(|wr|=c)', len(P))
print('A|B|C', len(A|B|C), 'C|P', len(C|P), 'A - P', sorted(A-P), 'P - A', sorted(P-A))
print('(A|B|C) - (C|P):', sorted((A|B|C) - (C|P)))
for r in rows:
    if r['name'] in (A|B|C) - (C|P):
        print(r['name'], r['word'], 'c', r['c'], 'wr', r['wr'], 'M', r['M'], 'm', r['m'], 'd0', r['d0'], 'bad1', r['bad1'], 'bad0', r['bad0'], sorted(int(e) for e in r['alpha']))
