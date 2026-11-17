"""Check: number of generators of BN~(T) in the idempotent W (= slope-0 idempotent, the 'through' resolution for the product
structure whose sutures lift to meridians) equals 2N+1; compare with rank HFK^(kappa).
Also record their (h,q) and delta for the grading comparison."""
import json, sys, collections
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mech/floer/scripts')
from knots import DET_SIG, floer
d=json.load(open('/Users/calebbarnett/jones-lanes/theory-restart/lit/kwz-inversions/data.json'))
c=collections.Counter(); exc=[]
def rkHFK(kn):
    if kn=='8_19': return 5
    if kn=='9_42': return 9
    return DET_SIG[kn][0]
rows=[]
for inv in d['inversions']:
    name=inv['name']; kn=inv['knot']; N=inv['n_special']; k=inv['rational_component']['slope_k']
    W=B=0; Wg=[]
    for comp in inv['khtpp']['BNr_components']:
        for (idem,h,q) in comp['generators_idem_h_q']:
            if idem=='W': W+=1; Wg.append((h,q))
            else: B+=1
    c['W == 2N+1'] += (W==2*N+1)
    c['B == 4N+|k|'] += (B==4*N+abs(k))
    c['W == rk HFK'] += (W==rkHFK(kn))
    c['W >= rk HFK'] += (W>=rkHFK(kn))
    if W!=rkHFK(kn): exc.append((name,W,rkHFK(kn)))
    rows.append((name,kn,W,Wg))
print(dict(c),'of',len(d['inversions']))
print('exceptions to equality:',exc)
# delta-distribution of the W generators for a few knots
for name,kn,W,Wg in rows[:12]:
    dist=collections.Counter(q/2-h for h,q in Wg)
    print(name,'W gens by delta=q/2-h:',dict(sorted(dist.items())),' q-range',min(q for h,q in Wg),max(q for h,q in Wg))
json.dump({n:Wg for n,kn,W,Wg in rows}, open('/Users/calebbarnett/jones-lanes/theory-restart/mech/floer/Wgens.json','w'))
