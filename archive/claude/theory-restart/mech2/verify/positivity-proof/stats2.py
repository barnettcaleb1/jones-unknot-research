import json
rows = json.load(open('sweep.json'))
A = set(); B = set()
for r in rows:
    if (not r['bad1'] and r['M'] != r['d0']) or (not r['bad0'] and r['m'] != r['d0']): A.add(r['name'])
    if abs(r['wr']) == r['c']: B.add(r['name'])
print(len(A), len(B), len(A & B), len(A | B))
print('intersection', sorted(A & B))
print('2.4 only', sorted(B - A))
# for positive ones: which are b-adequate at the relevant end
for r in rows:
    if abs(r['wr']) == r['c']:
        rel = r['bad1'] if r['wr'] < 0 else r['bad0']
        oth = r['bad0'] if r['wr'] < 0 else r['bad1']
        print(r['name'], 'wr', r['wr'], 'bad blocks at Seifert end', len(rel), 'at other end', len(oth), 'c_o', r['c_o'])
