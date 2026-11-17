# check the rule  D-symbol(2 chords + T) = 8 (-1)^{#odd labels} [T inside both chords]  on all observed such types
import json, re
from fractions import Fraction as F
tab=json.load(open('dtable3.json'))      # type -> [n, M3/36, v3, D8]
wit=json.load(open('witness_D.json'))     # (type, D', v3)
Dp={t:F(v[3])/40 for t,v in tab.items()}
for t,d,v in wit: Dp[t]=F(d)
def parse(t):
    toks=re.findall(r'T\d[v^]|[a-h][+-]',t); return toks
ok=bad=0; badlist=[]
for t,d in Dp.items():
    toks=parse(t)
    Ts=[i for i,x in enumerate(toks) if x[0]=='T']; Cs=[x for x in toks if x[0]!='T']
    if len(Ts)!=1 or len(Cs)!=4: continue
    ti=Ts[0]; chords={}
    for i,x in enumerate(toks):
        if x[0]!='T': chords.setdefault(x[0],[]).append((i,x[1]))
    inside_both=all(ps[0][0]<ti<ps[1][0] for ps in chords.values())
    nodd=sum(1 for ps in chords.values() if ps[0][1]=='-')
    pred=(-1)**nodd if inside_both else 0
    if pred==d: ok+=1
    else: bad+=1; badlist.append((t,d,pred))
print('2 chords + T types: rule holds on',ok,'fails on',bad,badlist[:10])
