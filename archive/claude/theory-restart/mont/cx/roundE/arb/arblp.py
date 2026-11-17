"""Uniform multi-box LP (lpgen machinery, read-only import) over an ARBITRARY class list S (signatures may have any sigma,
delta, fractional values).  Cases: all offset cases; d=0 slices for |m| < M0 on the lattice of attainable mB; for |m| >= M0 an exact
LINEAR relaxation of the quadratic d=0 rows (both closure kinds, both signs of m):
   r=1: sum phi - c0 = X/m  (X = p2 - q2 - LAM)   r=0: sum phi = c0 and (La+Lb)_all + p2 + q2 = 1 - m^2/4 <= 1 - M0|m|/4;
ties (mB = 0 + delta-law).  Every product has >= 1 non-rational box and >= 2 factors (sum k + n >= 2)."""
import sys, math, collections
LPG='/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundD/lpgen'
sys.path.insert(0,LPG)
import lpg, runner
from fractions import Fraction as Fr
def lcm(a,b): return a*b//math.gcd(a,b)
def jobs_for(S,M0=15,skip_r0=True):
    """skip_r0: 'd=0 r=0' (eps = +1, no cancellation at an offset-0 end) is VACUOUS for units: lc F = 2 lc S1 is an even
    nonzero integer (refGen remark (a)); its LPs are not needed."""
    den=1
    for c in S: den=lcm(den,Fr(c.sig).denominator)
    jobs=[]
    for cl in lpg.closure_classes():
        for nm,rows in lpg.case_rows(cl['p'],cl['q']): jobs.append(('case',cl['name'],nm,None))
        ss=cl['sigstar']
        for x in range(-M0*den+1,M0*den):
            m=Fr(x,den)
            for nm,rows in lpg.case_rows(cl['p'],cl['q'],m=m):
                if skip_r0 and nm=='d=0 r=0': continue
                jobs.append(('case',cl['name'],nm,m))
        for sg in (1,-1):
            for kind in (('r1+','r1-') if skip_r0 else ('r1+','r1-','r0')): jobs.append(('big',cl['name'],kind,sg))
    for tc in lpg.tie_classes(): jobs.append(('tie',tc['name'],'tie',0))
    return jobs
CL={cl['name']:cl for cl in lpg.closure_classes()}; TC={tc['name']:tc for tc in lpg.tie_classes()}
def twofactor(L): L.add_ub({**{j:Fr(-1) for j in range(L.nk)},L.iN:Fr(-1)},-2)
def lin(L,coef4,kcoef):
    r=L.zrow(coef4)
    for j,v in kcoef.items():
        if v: r[j]=r.get(j,0)+v
    return r
def neg(r): return {i:-v for i,v in r.items()}
def comb(*pairs):
    out={}
    for s,r in pairs:
        for i,v in r.items(): out[i]=out.get(i,0)+s*v
    return out
def big(S,cl,kind,sg,M0):
    end=cl['end']; (p1,p2),(q1,q2)=cl['p'],cl['q']; c0=1-(p1+q1)/2; ss=cl['sigstar']
    L=lpg.build(S,cl,[],0,kmin=1,nrule=cl['d0n']); twofactor(L)
    ra={j:c.end(end)[0] for j,c in enumerate(S)}; la={j:c.end(end)[1] for j,c in enumerate(S)}
    rb={j:c.end(end)[2] for j,c in enumerate(S)}; lb={j:c.end(end)[3] for j,c in enumerate(S)}
    sig={j:c.sig for j,c in enumerate(S)}
    RA=lin(L,(1,0,0,0),ra); RQ=lin(L,(0,1,0,0),{j:rb[j]-ra[j] for j in ra})
    LAM=lin(L,(0,0,0,1),{j:lb[j]-la[j] for j in ra}); LALB=lin(L,(0,0,2,1),{j:la[j]+lb[j] for j in ra})
    SPHI=comb((1,RA),(Fr(1,2),RQ))
    L.add_eq(comb((1,RQ),(-1,sig)),p1-q1-ss)                       # P0 row (mB = sigma.k - ss)
    # sg*mB >= M0
    L.add_ub({j:-sg*v for j,v in sig.items() if v},-(M0+sg*ss))
    Xc=p2-q2
    if kind=='r0':
        L.add_eq(SPHI,c0)
        # (La+Lb)_all + p2 + q2 <= 1 - (M0/4) sg mB
        L.add_ub(comb((1,LALB),(Fr(M0,4)*sg,sig)),1-p2-q2+Fr(M0,4)*sg*ss)
        return L
    # Y := SPHI - c0 = X/m, X = Xc - LAM; sg*m >= M0
    if (kind=='r1+')==(sg>0):
        # X >= 0 and Y in [0, X/M0]  (sg=+1)   or   X <= 0 and Y in [0, -X/M0] (sg=-1, kind r1-) ... handled uniformly below
        pass
    if sg>0:
        if kind=='r1+':   # X >= 0: 0 <= Y <= X/M0
            L.add_ub(LAM,Xc); L.add_ub(neg(SPHI),-c0); L.add_ub(comb((M0,SPHI),(1,LAM)),Xc+M0*c0)
        else:             # X <= 0: X/M0 <= Y <= 0
            L.add_ub(neg(LAM),-Xc); L.add_ub(SPHI,c0); L.add_ub(neg(comb((M0,SPHI),(1,LAM))),-(Xc+M0*c0))
    else:
        if kind=='r1+':   # X >= 0, m <= -M0: -X/M0 <= Y <= 0
            L.add_ub(LAM,Xc); L.add_ub(SPHI,c0); L.add_ub(comb((-M0,SPHI),(1,LAM)),Xc-M0*c0)
        else:             # X <= 0: 0 <= Y <= -X/M0
            L.add_ub(neg(LAM),-Xc); L.add_ub(neg(SPHI),-c0); L.add_ub(neg(comb((-M0,SPHI),(1,LAM))),-(Xc-M0*c0))
    return L
def build_job(S,job,M0=15):
    typ,cn,nm,m=job
    if typ=='tie':
        tc=TC[cn]; L=lpg.build(S,dict(tc,end='top'),[],0,kmin=1,slice_m=0,nrule=tc['n'])
    elif typ=='big': return big(S,CL[cn],nm,m,M0)
    else:
        cl=CL[cn]
        if m is None: L=lpg.build(S,cl,dict(lpg.case_rows(cl['p'],cl['q']))[nm],0,kmin=1)
        else:
            rows=dict(lpg.case_rows(cl['p'],cl['q'],m=m)).get(nm)
            L=lpg.build(S,cl,rows,0,kmin=1,slice_m=m,nrule=cl['d0n'])
    twofactor(L)
    return L
def decide_job(S,job,M0=15):
    L=build_job(S,job,M0)
    d=runner.decide(L)
    if d[0]=='open':
        k,n=d[1]; return (job,'open',({S[j].label:v for j,v in enumerate(k) if v>1e-9},n))
    return (job,d[0],str(d[1][2]) if d[0]=='closed' else None)
