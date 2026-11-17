"""Exact evaluation of class-level triple hits (fr_triples_*.pkl): closures of the representative products."""
import sys, pickle, collections
sys.path.insert(0,'.')
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineA')
import vc, eng, ser, front, lp
fn=sys.argv[1]; tags=sys.argv[2:]
R=pickle.load(open(fn,'rb'))
L=pickle.load(open('libA_jets.pkl','rb'))
vecs=list(L['vecs']); names=[(b[1],b[2]) for b in L['boxes']]
for tag in tags:
    F=pickle.load(open('fr_%s.pkl'%tag,'rb')); vecs+=F['vecs']; names+=[(b[1],b[2]) for b in F['boxes']]
T={Tg[0]:Tg for Tg in front.targets()}
out=[]
for tk,lst in R['ex'].items():
    Tg=T[tk]
    for (x,y,z) in lst:
        p=vc.star(vc.star(vecs[x],vecs[y]),vecs[z]); A,B=p
        kind,par=tk
        a1,w=eng.W(par) if kind=='h' else eng.WV(par)
        tq=ser.slope(p,'top',1); N=(tq[0]-Tg[1][0])//3
        S1=vc.mul(a1,A); S2=vc.mul(w,vc.shift(B,-3*N)); F_=vc.add(S1,S2)
        rt=max(max(S1),max(S2))-max(F_); rb=min(F_)-min(min(S1),min(S2))
        J=vc.divexact(F_,vc.PHI3)
        Jn=vc.norm(J) if J else None
        rec=(min(rt,rb),rt,rb,vc.span(J),vc.span(A),tk,N,lp.a2(Jn) if Jn else None,names[x][1],names[y][1],names[z][1])
        out.append(rec)
        if J and len(J)==1: print('UNIT!!',rec,names[x],names[y],names[z])
out.sort(key=lambda r:(-r[0],r[3]))
for r in out[:40]: print(r)
print('depth histogram',collections.Counter(r[0] for r in out))
# gates on all evaluated
PHI10={0:1,1:-1,2:1,3:-1,4:1}
g=[]
for r in out:
    pass
