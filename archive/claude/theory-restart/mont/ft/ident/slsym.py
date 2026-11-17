# level-3 symbols of the butterfly Sato-Levine invariants on one configuration per type (two per type when available)
import sys, json, itertools
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/ft/ident')
import butterfly as bf, chord
from fractions import Fraction as F
def flip(tokens, idxs):
    t=list(tokens)
    for i in idxs: a=t[i]; t[i]=('y' if a[0]=='x' else 'x')+a[1:]
    return '.'.join(t)
rs=json.load(open('symtab_m3_s3.json'))
by={}
for r in rs: by.setdefault(r['type'],[]).append(r)
out=[]
for ty,rr in sorted(by.items()):
    for r in rr[:2]:
        w=r['w']; sites=r['sites']; toks=w.split('.')
        alt={'SLin':0,'SLout':0}; ok=True
        for S in itertools.product([0,1],repeat=3):
            ww=flip(toks,[s+1 for s,b in zip(sites,S) if b]); sg=(-1)**sum(S)
            for ax in ('in','out'):
                s=bf.sato_levine(ww,ax)
                if not isinstance(s,dict): ok=False; break
                alt['SL'+ax]+=sg*s['a3']
            if not ok: break
        if not ok: print('fail',ty,w); continue
        sg=chord.site_signs(w,sites); pr=sg[sites[0]]*sg[sites[1]]*sg[sites[2]]
        rec=dict(type=ty,w=w,sites=sites,SLin=pr*alt['SLin'],SLout=pr*alt['SLout'])
        rec.update({k:r['sym'][k] for k in ('M3','K.v3','Kin.v3','Kout.v3','Uin.v3','Uout.v3')})
        out.append(rec)
json.dump(out,open('slsym3.json','w'))
# consistency
cons={}
for o in out: cons.setdefault(o['type'],set()).add((o['SLin'],o['SLout']))
print('types',len(cons),'inconsistent',[t for t,v in cons.items() if len(v)>1])
