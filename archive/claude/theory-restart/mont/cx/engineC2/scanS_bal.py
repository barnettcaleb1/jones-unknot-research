"""E3: S-necklace, balanced regime: products of n = 3,4 rational boxes (R(5)), m in {2,4,6,8}; and engineA depth-2 boxes
(292 positive-potential) alone and times R(5).  Exact; every N with a top tie."""
import sys, pickle, time, itertools
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineC2')
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineA')
import fastS, lp, vc, lib, scanS
tab=pickle.load(open('Gtab_Sneck.pkl','rb'))
which=sys.argv[1]; chunk=int(sys.argv[2]); nch=int(sys.argv[3])
R5=lib.rational(5)
items=[]
if which=='P3': items=list(itertools.combinations_with_replacement(range(len(R5)),3))
elif which=='P4': items=list(itertools.combinations_with_replacement(range(len(R5)),4))
elif which=='D2':
    D2=pickle.load(open('/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineA/d2pos_boxes.pkl','rb'))
    items=[(i,None) for i in range(len(D2))]+[(i,j) for i in range(len(D2)) for j in range(len(R5))]
items=items[chunk::nch]
stats={'cand':0}; best={}; units=[]; t0=time.time(); seen=set()
for it in items:
    if which in ('P3','P4'):
        v=vc.starall([R5[i][1] for i in it]); tag='P:'+'*'.join(str(R5[i][2][1]) for i in it)
    else:
        i,j=it; v=D2[i][1] if j is None else vc.starall([D2[i][1],R5[j][1]]); tag='D2:%d*%s'%(i,'' if j is None else R5[j][2][1])
    v,_=lib.canonY(v,None); k=lib.vkey(v)
    if k in seen: continue
    seen.add(k)
    scanS.scan_box(k,v,tag,[2,4,6,8],stats,best,units)
out=(stats,best,units)
pickle.dump(out,open('scanbal_%s_%d.pkl'%(which,chunk),'wb'))
print(which,chunk,'items',len(items),'cand',stats['cand'],'units',len(units),'best rho',best.get('rho',(None,))[:6],'best depth',best.get('depth',(None,))[:6],'gated',len(best.get('gated',[])),'time %.0f'%(time.time()-t0))
