import sys; sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mech/sum/scripts')
from load import *
k138=load_jsonl(R+'lit/kht/out/k138/k138.jsonl')
F={}
for r in k138:
    p=parse(r)
    if p is None: print('bad',r['file']); continue
    F[r['file'].replace('^','i')]=p
print(len(F), list(F)[:12])
# check dr = 4j+1/2
bad=[n for n,p in F.items() if p['dr']!=4*p['j']+Fr(1,2)]
print('dr != 4j+1/2:',bad)
print('lens',Counter(tuple(sorted(p['lens'])) for p in F.values()))
print('j nonint',[n for n,p in F.items() if p['j'].denominator!=1])
comps=load_jsonl(R+'lit/kht/out/comp/comp4.jsonl')+load_jsonl(R+'lit/kht/out/comp/comp5.jsonl')
print(len(comps))
names=sorted(F,key=len,reverse=True)
def split(name):
    # name = n1 + '_' + n2 with optional m suffixes
    res=[]
    for a in names:
        for am in ('m',''):
            pre=a+am+'_'
            if name.startswith(pre):
                rest=name[len(pre):]
                for bm in ('m',''):
                    if rest.endswith(bm) and (rest[:len(rest)-len(bm)] if bm else rest) in F:
                        b=rest[:len(rest)-len(bm)] if bm else rest
                        res.append((a,am,b,bm))
    return res
for r in comps:
    s=split(r['file'])
    print(r['file'], s, 'ERR' if 'error' in r else '', r.get('time'))
