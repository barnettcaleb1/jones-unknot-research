"""NORMALISATION, refined: by rule R3 the residual at an end, R = (l1,l2 of a' minus a_P; deg, lc, l1, l2 of q'), depends only on
q_P at that end and m.  Pieces: (m, deg q_P, lc q_P) at the end.  Test, per piece, whether R is a FUNCTION of (L1, L2) = (l1, l2)(q_P)
and whether it is AFFINE in (L1, L2).  Data: depth-one boxes with n = 2, 3 (R(5), 3,000 multisets for n = 3) and n = 4 (R(4))."""
import sys, itertools, random, collections, pickle
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundE/arb')
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineA')
import jbox, lib
from jauto import logs
from fractions import Fraction as Fr
MS=[m for m in range(-7,8) if m]; NS=list(range(-4,5))
def ld(s,K=2):
    d,c,ser=jbox.endjet(s,K); return d,Fr(c),logs(ser)
pieces=collections.defaultdict(dict)   # (end, m, degq, lcq) -> {(L1,L2): R}
conflict=collections.Counter()
random.seed(4)
for L,n,samp in ((5,2,None),(5,3,3000),(4,4,None)):
    R=lib.rational(L); P=[jbox.from_vec(r[1]) for r in R]
    idxs=list(itertools.combinations_with_replacement(range(len(R)),n))
    if samp and len(idxs)>samp: idxs=random.sample(idxs,samp)
    for idx in idxs:
        x=P[idx[0]]
        for i in idx[1:]: x=jbox.star(x,P[i])
        for N in NS:
            y=jbox.ypow(N,x)
            pre={}
            ok=True
            for e in ('top','bot'):
                try:
                    da,ca,la=ld(y[e][0]); db,cb,lb=ld(y[e][1])
                except (AssertionError,KeyError,TypeError): ok=False; break
                pre[e]=(db-da,cb/ca,lb[0]-la[0],lb[1]-la[1],la)
            if not ok: continue
            for m in MS:
                try: z=jbox.nest(m,y)
                except Exception: continue
                for e in ('top','bot'):
                    try:
                        da,ca,la=ld(z[e][0]); db,cb,lb=ld(z[e][1])
                    except (AssertionError,KeyError,TypeError): continue
                    dq,cq,L1,L2,laP=pre[e]
                    Rv=(la[0]-laP[0],la[1]-laP[1],db-da,cb/ca,lb[0]-la[0],lb[1]-la[1])
                    key=(e,m,dq,cq)
                    d=pieces[key]
                    if (L1,L2) in d and d[(L1,L2)]!=Rv: conflict[key]+=1
                    d[(L1,L2)]=Rv
    print('after R(%d) n=%d: pieces %d'%(L,n,len(pieces)),flush=True)
# affine test per piece: R = c0 + c1 L1 + c2 L2 (componentwise), exact rational solve on 3 points, check all
def affine(d):
    pts=list(d.items())
    if len(pts)<=3: return 'few'
    import itertools as it
    for a,b,c in it.combinations(pts[:12],3):
        (x1,y1),(x2,y2),(x3,y3)=a[0],b[0],c[0]
        det=(x2-x1)*(y3-y1)-(x3-x1)*(y2-y1)
        if det==0: continue
        coef=[]
        for comp in range(6):
            r1,r2,r3=a[1][comp],b[1][comp],c[1][comp]
            if comp==3:   # lc: multiplicative; test constancy instead
                coef.append(None); continue
            c1=((r2-r1)*(y3-y1)-(r3-r1)*(y2-y1))/det; c2=((x2-x1)*(r3-r1)-(x3-x1)*(r2-r1))/det; c0=r1-c1*x1-c2*y1
            coef.append((c0,c1,c2))
        good=all(all((coef[k][0]+coef[k][1]*X+coef[k][2]*Y)==Rv[k] for k in range(6) if k!=3) for (X,Y),Rv in pts)
        lcs=set(Rv[3] for _,Rv in pts)
        return 'affine' if good and len(lcs)==1 else ('affine(lc varies)' if good else 'NOT affine')
    # collinear data: check functional dependence on L1 only
    return 'degenerate'
stat=collections.Counter(); bad=[]
for key,d in pieces.items():
    gen=not ((key[2]==0 and key[3]==1) or (key[2]==-1 and key[3]==-1))
    v=affine(d)
    stat[('generic' if gen else 'special',v)]+=1
    if v=='NOT affine' and gen and len(bad)<8: bad.append((key,len(d)))
print('conflicts (R not a function of (L1,L2) within a piece):',sum(conflict.values()),'pieces with conflicts',len(conflict))
print('  conflict pieces (generic):',sum(1 for k in conflict if not ((k[2]==0 and k[3]==1) or (k[2]==-1 and k[3]==-1))))
for k,v in sorted(stat.items()): print('  ',k,v)
print('examples of non-affine generic pieces:',bad)
pickle.dump(dict(stat=stat,conflict=dict(conflict)),open('affine.pkl','wb'))
