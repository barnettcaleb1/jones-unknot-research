# Claims 4, 5: exact non-membership certificates.  (a) builder's 150 rows (K, K_in, K_out, N, D, E4 columns verified
# against my code; U_in, U_out, SL columns taken from the builder unverified); (b) fresh words, my own candidates only.
import sys, json, random, itertools
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/ft/referee/ident_work')
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont')
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/tools')
import refinv as R, constit as C, lp, flat_search as fs
from fractions import Fraction as Fr
def cert(A,b):
    """exact: returns (y dict, y.b) with sum_i y_i A_i = 0, y.b != 0; or None if b in span of columns."""
    m=len(A[0]); basis=[]; piv=[]
    for i,(row,bi) in enumerate(zip(A,b)):
        v=[Fr(x) for x in row]+[Fr(bi)]; prov={i:Fr(1)}
        for (bv,bp),pc in zip(basis,piv):
            if v[pc]!=0:
                f=v[pc]/bv[pc]; v=[x-f*y for x,y in zip(v,bv)]
                for k,c in bp.items(): prov[k]=prov.get(k,Fr(0))-f*c
        nz=next((c for c in range(m) if v[c]!=0),None)
        if nz is None:
            if v[m]!=0: return {k:c for k,c in prov.items() if c!=0}, v[m]
            continue
        basis.append((v,prov)); piv.append(nz)
    return None
def verify(A,b,y):
    for j in range(len(A[0])):
        assert sum(c*Fr(A[i][j]) for i,c in y.items())==0
    return sum(c*Fr(b[i]) for i,c in y.items())
def val(r,f):
    out=Fr(1)
    for g in f.split('*'): out*=Fr(str(r[g]))
    return out
rows=json.load(open('/Users/calebbarnett/jones-lanes/theory-restart/mont/ft/ident/inv_rows5.json'))
for r in rows:
    J=lp.J(r['w']); r['N4']=R.nmom(J,4); r['F4']=str(Fr(r['E4'])/1440)
KEYS=['K','Kin','Kout','Uin','Uout']
featsD=['K.v3','Kin.v3','Kout.v3','Uin.v3','Uout.v3','SLin','SLout','SLax','N1','N3','N1*N2','N1*N1*N1']+['N1*'+k+'.a2' for k in KEYS]
A=[[val(r,f) for f in featsD] for r in rows]; b=[val(r,'D') for r in rows]
c=cert(A,b)
print('(a) D vs 17 builder candidates on builder rows:', 'IN SPAN' if c is None else 'certificate on %d words, y.D = %s (verified %s)'%(len(c[0]),c[1],verify(A,b,c[0])))
feats=[k+'.a2' for k in KEYS]+['N2','N1*N1']+[a+'.a2*'+bb+'.a2' for a,bb in itertools.combinations_with_replacement(KEYS,2)]
feats+=[k+'.a4' for k in KEYS]+[k+'.j4' for k in KEYS]+['N4','N1*N3','N2*N2','N1*N1*N2','N1*N1*N1*N1']
feats+=['N1*N1*'+k+'.a2' for k in KEYS]+['N2*'+k+'.a2' for k in KEYS]+['N1*'+k+'.v3' for k in KEYS]+['N1*D','N1*SLin','N1*SLout','N1*SLax']
A=[[val(r,f) for f in feats] for r in rows]; b=[val(r,'F4') for r in rows]
c=cert(A,b)
print('(a) F4 vs %d builder candidates on builder rows:'%len(feats), 'IN SPAN' if c is None else 'certificate on %d words, y.F4 = %s (verified %s)'%(len(c[0]),c[1],verify(A,b,c[0])))
# rank deficiency of the candidate matrix itself (how many candidates are effectively independent)
def rank(A):
    M=[[Fr(x) for x in row] for row in A]; rk=0; cols=len(M[0])
    for c_ in range(cols):
        p=next((i for i in range(rk,len(M)) if M[i][c_]!=0),None)
        if p is None: continue
        M[rk],M[p]=M[p],M[rk]
        for i in range(len(M)):
            if i!=rk and M[i][c_]!=0:
                f=M[i][c_]/M[rk][c_]; M[i]=[x-f*y for x,y in zip(M[i],M[rk])]
        rk+=1
    return rk
print('    rank of the 56-candidate matrix on 150 rows:',rank(A),' with F4:',rank([row+[bb] for row,bb in zip(A,b)]))
# (b) fresh words, my own candidates only (K, K_in, K_out, N's)
rnd=random.Random(9501); fresh=[]; seen=set()
while len(fresh)<160:
    w=fs.gen(rnd,rnd.randint(8,22)) if rnd.random()<0.5 else R.gen2(rnd,rnd.randint(8,20),maxw=5,pw=0.35)
    if not w or w in seen: continue
    seen.add(w); v=R.all_vals(w,True)
    if v is None: continue
    cs=C.constituents(w)
    if cs['in'] is None or cs['out'] is None: continue
    r={'N1':v['N1'],'N2':v['N2'],'N3':v['N3'],'N4':R.nmom(v['J'],4),'D':v['D'],'F4':v['F4']}
    for key,X in (('K',v),('Kin',cs['in']),('Kout',cs['out'])):
        for f in ('a2','v3','j4','a4'): r[key+'.'+f]=X[f]
    fresh.append(r)
K3=['K','Kin','Kout']
fD=[k+'.v3' for k in K3]+['N1','N3','N1*N2','N1*N1*N1']+['N1*'+k+'.a2' for k in K3]
A=[[val(r,f) for f in fD] for r in fresh]; b=[val(r,'D') for r in fresh]; c=cert(A,b)
print('(b) D vs %d own candidates on 160 fresh words:'%len(fD), 'IN SPAN' if c is None else 'certificate on %d words, y.D = %s (verified %s)'%(len(c[0]),c[1],verify(A,b,c[0])))
fF=[k+'.a2' for k in K3]+['N2','N1*N1']+[a+'.a2*'+bb+'.a2' for a,bb in itertools.combinations_with_replacement(K3,2)]
fF+=[k+'.a4' for k in K3]+[k+'.j4' for k in K3]+['N4','N1*N3','N2*N2','N1*N1*N2','N1*N1*N1*N1']
fF+=['N1*N1*'+k+'.a2' for k in K3]+['N2*'+k+'.a2' for k in K3]+['N1*'+k+'.v3' for k in K3]+['N1*D']
A=[[val(r,f) for f in fF] for r in fresh]; b=[val(r,'F4') for r in fresh]; c=cert(A,b)
print('(b) F4 vs %d own candidates on 160 fresh words:'%len(fF), 'IN SPAN' if c is None else 'certificate on %d words, y.F4 = %s (verified %s)'%(len(c[0]),c[1],verify(A,b,c[0])))
print('    rank own F4 candidates:',rank(A))
