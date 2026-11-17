"""VERTICAL closures at ORDER 3 for ONE dangerous box B (each order-3 subclass) + n >= 1 rational boxes, every odd |a| >= 3.
 (1) offset cases at the weak end (C1 rows, order 2, single box, n >= 1);  (2) 'd=0 r=1' (m = sigma(B) + 1 != 0): order-2 rows +
 the ORDER-3 EQUALITY d3 = -m [1/2 - Y2 + (1-X1)^2/2 - m^2/6], X1-sliced (|1-X1| < 6) + exact linear relaxation, n by the
 delta-law (= delta+4 or >= delta+off as in lpg);  (3) tie (sigma(B) = -1): per weak end, sign of a, |a| = 3 (n = delta + 4
 pinned, D2 fixed: lpgen tie rows) or |a| >= 5 (n >= delta + 6 free; tau*_V = 1/2 constant; X1-sliced so that D3 = D2 (1 - X1)
 with D2 = tau* - tau(B) + n is LINEAR in n; relaxation |D3| >= 6 |D2| beyond the window; T3 = tau-law checked exactly).
 Closure data (computed, eng.w1/eng.wV): typ '+' end: w1 (0,1,0), wV (1,1/2,1/3) for all |a| >= 3; typ '-' end: |a| = 3:
 w1 (0,-1,0), wV (0,0,0); |a| >= 5: (0,0,0), (0,0,0); tau*_V = -1/2 (|a| = 3), +1/2 (|a| >= 5)."""
import sys, pickle, collections, time
from fractions import Fraction as Fr
LPG='/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundD/lpgen'
sys.path.insert(0,LPG); sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineA')
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundE/arb')
import lpg, f1o3, eng, runner
from o3h import comb, rowsL
from multiprocessing import Pool
T=6
def wdat(a,end):
    return f1o3.lj(eng.w1(a),end),f1o3.lj(eng.wV(a),end)
def dec(L): return runner.decide(L)[0]
def mkcl(end,a):
    (p1,p2,p3),(q1,q2,q3)=wdat(a,end)
    return dict(kind='V',name='V',end=end,p=(p1,p2),q=(q1,q2),sigstar=Fr(-1)),p3,q3
def single(key,cl,nmin,npin=None,nge=None,extra_rows=()):
    b=lpg.Cls(key,1,'B'); L=lpg.build([b],cl,[],nmin,kmin=0,fixk={0:1})
    if npin is not None: L.add_eq({L.iN:Fr(1)},Fr(npin))
    if nge is not None: L.add_ub({L.iN:Fr(-1)},-Fr(nge))
    return L
def addcase(L,rows,Bend,m):
    ra,la,rb,lb=Bend
    for coef,a in rows: L.add_eq(L.zrow(coef),lpg.evalaff(a,ra,la,rb,lb,m))
def o3slices(key,d3,cl,p3,q3,rows,m,npin,nge,end):
    ra,la,rb,lb=key[0] if end=='top' else key[1]
    l3a,l3b=(d3[0],d3[1]) if end=='top' else (d3[2],d3[3])
    (p1,p2),(q1,q2)=cl['p'],cl['q']
    opn=[]
    for x in list(range(-T+1,T))+['big+','big-']:
        L=single(key,cl,1,npin,nge); addcase(L,rows,(ra,la,rb,lb),m)
        RA,RQ=rowsL(L)
        X1=comb((1,RA(1))); Y2=comb((1,RA(2)),(1,RQ(2))); d3f=comb((-1,RQ(3)))
        cX1=p1+ra; cY2=q2+lb; cd3=p3-q3+l3a-l3b
        Qf=comb((-1/m,d3f),(1,Y2)); cQ=-cd3/m-Fr(1,2)+cY2+m*m/6
        if isinstance(x,int):
            L.add_eq(X1,(1-x)-cX1); L.add_eq(Qf,Fr(x*x,2)-cQ)
        else:
            s=1 if x=='big+' else -1
            L.add_ub({i:s*v for i,v in X1.items()},s*(1-cX1)-T)
            L.add_ub(comb((-1,Qf),(-Fr(T,2)*s,X1)),cQ-Fr(T,2)*s*(1-cX1))
        if dec(L)!='closed': opn.append(x)
    return opn
def tie(key,d3,end,a):
    """weak end 'end', vertical closure with this a (sign + class); returns verdict string"""
    cl,p3,q3=mkcl(end,a); (p1,p2),(q1,q2)=cl['p'],cl['q']
    ra,la,rb,lb=key[0] if end=='top' else key[1]
    l3a,l3b=(d3[0],d3[1]) if end=='top' else (d3[2],d3[3])
    tau=sum((k[3]-k[1]) for k in (key[0],key[1])); dl=Fr(key[3])
    taus=Fr(-1,2) if abs(a)==3 else Fr(1,2)
    if abs(a)==3:
        n=dl+4
        if n<1: return 'n<1'
        T3=(n==tau-taus); D2=taus-tau+n
        if D2==0: return 'T3 possible'
        L=single(key,cl,1,npin=n)
        L.add_eq(L.zrow((0,1,0,0)),p1-q1-rb+ra)
        L.add_eq(L.zrow((0,0,0,1)),p2-q2-(lb-la)-D2)
        RA,RQ=rowsL(L)
        L.add_eq(comb((-1,RQ(3)),(D2,RA(1))),D2*(1-p1-ra)-p3+q3+(l3b-l3a))
        return 'T2 '+dec(L)+(' T3 possible' if T3 else '')
    # |a| >= 5: n = delta + |a| + 1 >= delta + 6, n free in the LP (parity relaxed)
    n0=max(dl+6,1)
    nT3=tau-taus                         # T3 needs n = tau - tau*
    T3=(nT3>=dl+6 and nT3.denominator==1 and (nT3-dl-1)%2==1)
    opn=[]
    for x in list(range(-T+1,T))+['big+','big-']:
        for sD in (1,-1):                # sign of D2 (T2: D2 != 0)
            L=single(key,cl,1,nge=n0)
            L.add_eq(L.zrow((0,1,0,0)),p1-q1-rb+ra)
            # Lam = p2 - q2 - (lb-la) - D2,  D2 = taus - tau + n   ->  Lam + n = p2 - q2 - (lb-la) - taus + tau
            L.add_eq(comb((1,L.zrow((0,0,0,1))),(1,{L.iN:Fr(1)})),p2-q2-(lb-la)-taus+tau)
            # D2 sign:  sD*(taus - tau + n) >= 1/2
            L.add_ub({L.iN:Fr(-sD)},sD*(taus-tau)-Fr(1,2))
            RA,RQ=rowsL(L)
            X1=comb((1,RA(1))); cX1=p1+ra
            D3f=comb((-1,RQ(3))); cD3=p3-q3+l3a-l3b      # D3 = l3(s1) - l3(s2)
            c0=taus-tau                                   # D2 = c0 + n
            if isinstance(x,int):
                L.add_eq(X1,(1-x)-cX1)
                # D3 = D2 * x  ->  D3f - x n = x c0 - cD3
                L.add_eq(comb((1,D3f),(-x,{L.iN:Fr(1)})),x*c0-cD3)
            else:
                s=1 if x=='big+' else -1                 # s(1 - X1) >= T
                L.add_ub({i:s*v for i,v in X1.items()},s*(1-cX1)-T)
                # D3 = D2 (1-X1): sign(D3) = sD*s and |D3| >= T |D2|:  sD*s*D3 >= T * sD * D2
                #   -> -sD*s*D3f + T*sD*n <= sD*s*cD3 - T*sD*c0
                L.add_ub(comb((-sD*s,D3f),(T*sD,{L.iN:Fr(1)})),sD*s*cD3-T*sD*c0)
            if dec(L)!='closed': opn.append((x,sD))
    return ('T2 closed' if not opn else 'T2 open %s'%opn[:3])+(' T3 possible' if T3 else '')
def one(job):
    key,d3=job; out={}
    sig=Fr(key[2]); m=sig+1; dl=Fr(key[3])
    for cl in lpg.closure_classes():
        if cl['kind']!='V': continue
        end=cl['end']; Bend=key[0] if end=='top' else key[1]
        # (1) offset cases, order 2
        for nm,rows in lpg.case_rows(cl['p'],cl['q']):
            L=single(key,cl,1); addcase(L,rows,Bend,m)
            v=dec(L)
            if v!='closed': out[(cl['name'],nm)]='open@2'
        # (2) d=0 r=1
        if m!=0:
            kind,off=cl['d0n']
            rows=dict(lpg.case_rows(cl['p'],cl['q'],m=m)).get('d=0 r=1')
            npin=dl+off if kind=='eq' else None; nge=None if kind=='eq' else max(dl+off,1)
            if npin is not None and npin<1: continue
            L=single(key,cl,1,npin,nge); addcase(L,rows,Bend,m)
            if dec(L)!='closed':
                a=3 if cl['a3'] else 5
                if cl['typ']=='+': a=3
                asg=cl['asg']; aa=asg*a
                cl3,p3,q3=mkcl(end,aa)
                # typ '+' (a3 class covers all |a| >= 3; order <= 3 data constant): fine
                opn=o3slices(key,d3,cl,p3,q3,rows,m,npin,nge,end)
                if opn: out[(cl['name'],'d=0 r=1')]='open@3 %s'%opn
    if m==0:
        for end in ('top','bot'):
            for a in (3,-3,5,-5):
                v=tie(key,d3,end,a)
                if not (v in ('n<1','T2 closed')): out[('tie',end,a)]=v
    return (key,d3,out)
if __name__=='__main__':
    t0=time.time()
    K3=pickle.load(open('gen1k3_R5_n2.pkl','rb'))
    O=pickle.load(open('o3h.pkl','rb'))
    keys=sorted(set(r[0][0] for r in O['res']),key=str)
    jobs=[(k,d3) for k in keys for d3 in K3.get(k,{})]
    print('dangerous classes',len(keys),'order-3 subclasses',len(jobs),flush=True)
    with Pool(3) as P: res=P.map(one,jobs,chunksize=4)
    per=collections.defaultdict(list)
    for key,d3,out in res: per[key].append(out)
    vclosed=[k for k,outs in per.items() if all(not o for o in outs)]
    why=collections.Counter()
    for key,d3,out in res:
        for k,v in out.items(): why[(k[0] if k[0]!='tie' else 'tie',k[1] if k[0]!='tie' else '', v.split(' [')[0][:30])]+=1
    H=pickle.load(open('hb_o3.pkl','rb')); Hc=set(H['closed'])
    print('V-closed at order 3 (B + any n >= 1 rational, every odd |a| >= 3):',len(vclosed),'of',len(per))
    print('H3 and V3 both closed:',len([k for k in vclosed if k in Hc]))
    for k,v in why.most_common(15): print('   open:',k,v)
    pickle.dump(dict(res=res,vclosed=vclosed),open('o3v.pkl','wb'))
    print('time',round(time.time()-t0,1))
