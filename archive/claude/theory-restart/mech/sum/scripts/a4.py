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
def prof(S):
    lv=sorted(set(d for c,d in S))
    return [(d,min(c for c,dd in S if dd==d),max(c for c,dd in S if dd==d)) for d in lv]
def tilt(S):
    pr=prof(S); ok_cons=all(pr[i+1][0]-pr[i][0]==1 for i in range(len(pr)-1))
    ok_min=all(pr[i+1][1]<pr[i][1] for i in range(len(pr)-1)); ok_max=all(pr[i+1][2]<pr[i][2] for i in range(len(pr)-1))
    return ok_cons,ok_min,ok_max
def overhang(p):
    S=cen(p); k=p['k']
    if not S: return True
    if k>0: return max(c for c,d in S)>=2*k+2
    if k<0: return min(c for c,d in S)<=2*k-2
    return True
cnt=Counter(); fails=[]
for tag,name,p in allp:
    t=tilt(cen(p)); o=overhang(p); jt=tilt(Jset(p))
    cnt[(tag,'tilt',all(t))]+=1; cnt[(tag,'over',o)]+=1; cnt[(tag,'Jtilt',all(jt))]+=1
    if not all(jt): fails.append((tag,name,p['k'],int(p['j']),jt,prof(Jset(p)),prof(cen(p))))
for k in sorted(cnt): print(k,cnt[k])
for f in fails[:60]:
    print(f[0],f[1],'k',f[2],'j',f[3],f[4]); print('   J:',' '.join('%d:[%d,%d]'%x for x in f[5])); print('   S:',' '.join('%s:[%d,%d]'%x for x in f[6]))
print(len(fails))
