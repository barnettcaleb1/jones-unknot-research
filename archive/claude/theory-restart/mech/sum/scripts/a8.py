import sys, pickle; sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mech/sum/scripts')
from load import *
allp=pickle.load(open('/Users/calebbarnett/jones-lanes/theory-restart/mech/sum/scripts/allp.pkl','rb'))
def cen(p):
    j=int(p['j']); S=Counter()
    for (c,d),m in p['S'].items(): S[(c-24*j, Fr(d)-4*j-Fr(1,2))]+=m
    return S
def Jset(p):
    S=cen(p); J=Counter(); J[(2*p['k'],0)]+=1
    for (c,d),m in S.items():
        J[(c+4,int(d-Fr(1,2)))]+=m; J[(c-4,int(d+Fr(1,2)))]+=m
    return J
def wD(J): return Counter({(C//2+3*D,D):m for (C,D),m in J.items()})
width=Counter(); incmax=Counter(); incmin=Counter(); kpos=Counter(); nlev=Counter(); perlev=Counter()
big=[]
for tag,name,p in allp:
    W=wD(Jset(p)); ws=[w for w,D in W]; Ds=sorted(set(D for w,D in W))
    wd=max(ws)-min(ws); width[(tag,wd)]+=1
    if wd>=6: big.append((tag,name,p['k'],int(p['j']),wd,len(Ds),sum(W.values())))
    k=p['k']; kpos[(k-min(ws),max(ws)-k)]+=1
    for D in Ds:
        l=[w for w,DD in W if DD==D]; perlev[max(l)-min(l)]+=1
    for a,b in zip(Ds,Ds[1:]):
        la=[w for w,D in W if D==a]; lb=[w for w,D in W if D==b]
        incmax[max(lb)-max(la)]+=1; incmin[min(lb)-min(la)]+=1
print('overall w-width by dataset:',sorted(width.items()))
print('w_max(D+1)-w_max(D):',sorted(incmax.items()))
print('w_min(D+1)-w_min(D):',sorted(incmin.items()))
print('per-level w-width:',sorted(perlev.items()))
print('(k-wmin, wmax-k):',sorted(kpos.items()))
for b in big[:20]: print(b)
