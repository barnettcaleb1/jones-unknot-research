import sys; sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mech/sum/scripts')
from load import *
k138=load_jsonl(R+'lit/kht/out/k138/k138.jsonl')
F={}
for r in k138:
    p=parse(r)
    if p is None: continue
    F[r['file'].replace('^','i')]=p
comps=load_jsonl(R+'lit/kht/out/comp/comp4.jsonl')+load_jsonl(R+'lit/kht/out/comp/comp5.jsonl')
names=sorted(F,key=len,reverse=True)
def split(name):
    for a in names:
        for am in ('m',''):
            pre=a+am+'_'
            if name.startswith(pre):
                rest=name[len(pre):]
                for bm in ('m',''):
                    b=rest[:len(rest)-len(bm)] if bm else rest
                    if rest.endswith(bm) and b in F: return (a,am,b,bm)
def fac(a,am):
    p=F[a]
    return mirror(p) if am else p
def predict(p1,p2):
    S1=norm(p1); S2=norm(p2); k1=p1['k']; k2=p2['k']
    S=Counter()
    for (c,d),m in S1.items(): S[(c+2*k2,d)]+=m
    for (c,d),m in S2.items(): S[(c+2*k1,d)]+=m
    for (c1,d1),m1 in S1.items():
        for (c2,d2),m2 in S2.items():
            S[(c1+c2+8,d1+d2-1)]+=m1*m2
            S[(c1+c2,d1+d2)]+=m1*m2
    return S
seen=set(); ok=0; bad=0
for r in comps:
    if r['file'] in seen: continue
    seen.add(r['file'])
    a,am,b,bm=split(r['file'])
    p1=fac(a,am); p2=fac(b,bm); p=parse(r)
    if p is None: print('noparse',r['file']); continue
    kj_ok = (p['k']==p1['k']+p2['k'] and p['j']==p1['j']+p2['j'])
    S=norm(p); Sp=predict(p1,p2)
    if S==Sp and kj_ok: ok+=1
    else:
        bad+=1
        print(r['file'],'k,j',(p1['k'],p1['j']),(p2['k'],p2['j']),'->',(p['k'],p['j']),kj_ok)
        print('   actual-not-pred',sorted((S-Sp).items()))
        print('   pred-not-actual',sorted((Sp-S).items()))
print('ok',ok,'bad',bad,'distinct',len(seen))
