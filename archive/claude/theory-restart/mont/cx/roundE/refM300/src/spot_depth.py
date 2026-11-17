"""post-processing of the spot-check: agreement depths (r_top, r_bot) of S1 = w1 A and -S2 = -w2 t^-3N B at the chosen
closure (number of cancelled leading terms at each end), and totals."""
import sys, glob, pickle, collections
EA='/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineA'
sys.path.insert(0,EA); sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundE/refM300/src')
import vc, eng, spot_lib
items,pool=spot_lib.load()
R=[pickle.load(open(f,'rb')) for f in glob.glob('/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundE/refM300/spot_res/*.pkl')]
def depth(S1,S2,end):
    F=vc.add(S1,S2)
    if end=='top':
        t1,t2,tf=max(S1),max(S2),max(F)
        return (max(t1,t2)-tf) if t1==t2 else 0
    b1,b2,bf=min(S1),min(S2),min(F)
    return (bf-min(b1,b2)) if b1==b2 else 0
dist=collections.Counter(); two=collections.Counter(); mx=0
for r in R:
    vecs=[items[x][2] for x in r['xs']]+[vc.rat(w) for w in r['rats']]
    A,B=vc.starall(vecs); x,N=r['x'],r['N']
    w1,w2=(eng.W(x) if r['kind']=='H' else eng.WV(x))
    S1=vc.mul(w1,A); S2=vc.shift(vc.mul(w2,B),-3*N)
    dt,db=depth(S1,S2,'top'),depth(S1,S2,'bot')
    dist[max(dt,db)]+=1; two[min(dt,db)]+=1; mx=max(mx,max(dt,db))
print('closures',len(R),' one-ended depth max(r_t,r_b) distribution',sorted(dist.items()),' two-ended min(r_t,r_b)',sorted(two.items()))
