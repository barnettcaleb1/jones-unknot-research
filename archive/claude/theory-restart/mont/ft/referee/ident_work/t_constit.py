# Claim 1 validation + agreement of the builder's stored candidate values with my independent ones.
import sys, json, random
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/ft/referee/ident_work')
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont')
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/tools')
import refinv as R, constit as C, lp, flat_search as fs
from fractions import Fraction as Fr
rows=json.load(open('/Users/calebbarnett/jones-lanes/theory-restart/mont/ft/ident/inv_rows5.json'))
mism={}; n=0
for r in rows:
    w=r['w']; v=R.all_vals(w,True); cs=C.constituents(w)
    if v is None or cs['in'] is None or cs['out'] is None: mism['fail']=mism.get('fail',0)+1; continue
    n+=1
    mine={'M2':v['M2'],'M3':v['M3'],'M4':v['M4'],'N1':v['N1'],'N2':v['N2'],'N3':v['N3'],'D':v['D'],'E4':v['M4']-R.M4loc(v['a2'],v['a4'],v['j4'])}
    for key,X in (('K',v),('Kin',cs['in']),('Kout',cs['out'])):
        for f in ('a2','v3','j4','a4'): mine[key+'.'+f]=X[f]
    for k,val in mine.items():
        if Fr(str(r[k]))!=Fr(val): mism[k]=mism.get(k,0)+1
print('builder rows checked',n,'mismatches by field:',mism if mism else 'none')
# det identity on NEW words, with the correct and the reversed winding handedness
rnd=random.Random(9401); tot=0; ok=0; okrev=0; both=0; nontriv=0
while tot<150:
    w=fs.gen(rnd,rnd.randint(8,20)) if rnd.random()<0.5 else R.gen2(rnd,rnd.randint(8,18),maxw=5,pw=0.35)
    if not w: continue
    K=R.Kinv(w,True)
    if K is None: continue
    cs=C.constituents(w); cr=C.constituents(w,hand=-1)
    if None in (cs['in'],cs['out'],cr['in'],cr['out']): continue
    detK=abs(sum(c*(-1)**e for e,c in K['Delta'].items()))
    tot+=1; nontriv+= (cs['in']['det']>1 and cs['out']['det']>1)
    ok+= detK==cs['in']['det']*cs['out']['det']; okrev+= detK==cr['in']['det']*cr['out']['det']
print('det(K) = det(K_in) det(K_out): correct handedness %d/%d (both factors >1 in %d); reversed handedness %d/%d'%(ok,tot,nontriv,okrev,tot))
