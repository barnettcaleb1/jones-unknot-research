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
def uD(J): return Counter({((C+8*D)//2,D):m for (C,D),m in J.items()})
def show(U):
    us=[u for u,D in U]; Ds=[D for u,D in U]
    for D in range(max(Ds),min(Ds)-1,-1):
        print('   D=%3d '%D+''.join((str(U[(u,D)]) if U[(u,D)] else '.') for u in range(min(us),max(us)+1)), ' u from',min(us))
def translate_eq(A,B):
    a=sorted(A.elements()); b=sorted(B.elements())
    if len(a)!=len(b): return False
    t=(b[0][0]-a[0][0],b[0][1]-a[0][1])
    return Counter({(u+t[0],D+t[1]):m for (u,D),m in A.items()})==B
sym=Counter()
for tag,name,p in allp:
    U=uD(Jset(p))
    T=Counter({(-D,-u):m for (u,D),m in U.items()})   # anti-transpose
    T2=Counter({(D,u):m for (u,D),m in U.items()})     # transpose
    sym[(tag,'anti',translate_eq(U,T))]+=1; sym[(tag,'transpose',translate_eq(U,T2))]+=1
for k in sorted(sym): print(k,sym[k])
for tag,name,p in allp[:14]+[x for x in allp if x[1] in ('9_46^1','9_46^2','8_20','8_19','9_42','9_44^1')]:
    print(tag,name,'k',p['k'],'j',p['j']); show(uD(Jset(p)))
