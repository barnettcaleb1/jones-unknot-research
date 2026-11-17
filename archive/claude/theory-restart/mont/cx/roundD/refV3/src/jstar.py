"""refV3: exact J for EVERY vertical closure with n <= 2 boxes of R(6), odd a in [-9,9], |N| <= 12 (1,237,250 closures):
 (a) span statistics / near misses (min span, a_2, J(zeta_10) gate);
 (b) the branch-knot implication: for each J != 1 and every odd m with |m| <= 99, test whether V(L_m) = 1 is still possible,
     i.e. t^(12j) {1 + (1 + t^-m) Phi_3 G} = 1 with G = (J-1)/(1+t)^2, j = -J'(1)/8 (BRIEF 1.3; Astra's J_* loophole)."""
import sys, time, pickle, itertools, multiprocessing as mp, cmath
sys.dont_write_bytecode=True
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundD/refV3/src')
import vc, lib
R6=lib.rational(6)
OUT='/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundD/refV3/'
AS=list(range(-9,10,2)); NS=list(range(-12,13))
T1P2={0:1,1:2,2:1}
def jstar_hit(J):
    """True if some odd m (|m|<=99) gives V(L_m) = 1 by formula 1.3 although J != 1"""
    d1=sum(e*c for e,c in J.items())        # J'(1)
    if d1%8: return ('j not integral',d1)
    j=-d1//8
    if j==0: return None                     # then V(L_m) = 1 <=> J = 1
    G=vc.divexact(vc.add(J,{0:-1}),T1P2)
    if G is None: return ('G not Laurent',)
    PG=vc.mul(vc.PHI3,G)
    # (1 + t^-m) PG = t^(-12j) - 1 forces (top/bottom degree count) m = top(PG) - max(0,-12j) [m<0] or bot(PG) - min(0,-12j) [m>0]
    cands=set()
    m1=max(PG)-max(0,-12*j)
    if m1<0: cands.add(m1)
    m2=min(PG)-min(0,-12*j)
    if m2>0: cands.add(m2)
    for m in cands:
        if m%2==0: continue
        H=vc.add({0:1}, vc.add(PG, vc.shift(PG,-m)))
        if H=={-12*j:1}: return ('LOOPHOLE',m,j)
    return None
def zeta10(J):
    z=cmath.exp(2j*cmath.pi/10)
    return abs(sum(c*z**e for e,c in J.items())-1)<1e-9
def work(cmb):
    p0=vc.starall([R6[i][1] for i in cmb])
    res=[]
    for a in AS:
        for N in NS:
            J=vc.J_vert(a,vc.Ypow(N,p0))
            if J is None: res.append((cmb,a,N,'NONE')); continue
            sp=vc.span(J)
            h=jstar_hit(J) if J!={0:1} else None
            # one-ended cancellation depths of F = w_1 A + wV t^-3N B relative to S1 = w_1 A (only where degrees coincide)
            A,B=vc.Ypow(N,p0); W1=vc.add({1:1}, vc.mul(vc.tmono(a),vc.T2P1)); WV=vc.add(vc.shift(vc.tmono(a),1), vc.shift(vc.PHI5,3*a-1))
            S1=vc.mul(W1,A); S2=vc.mul(WV,B); F=vc.add(S1,S2)
            rt=(max(S1)-max(F)) if max(S1)==max(S2) else 0
            rb=(min(F)-min(S1)) if min(S1)==min(S2) else 0
            res.append((cmb,a,N,sp,vc.a2(J),h,rt,rb))
    return res
if __name__=='__main__':
    jobs=[(i,) for i in range(len(R6))]+list(itertools.combinations_with_replacement(range(len(R6)),2))
    t0=time.time(); allr=[]
    with mp.Pool(6) as pool:
        for r in pool.imap_unordered(work,jobs,chunksize=8): allr+=r
    print('closures',len(allr),round(time.time()-t0),flush=True)
    nones=[r for r in allr if r[3]=='NONE']; print('J None:',len(nones))
    hits=[r for r in allr if r[3]!='NONE' and r[5] is not None]
    print('branch-knot loophole / anomalies:',len(hits),hits[:10])
    ones=[r for r in allr if r[3]!='NONE' and r[3]==0]
    print('span-0 (unit) J:',len(ones),'by (n,a):',{(len(r[0]),r[1]) for r in ones})
    import collections
    for n in (1,2):
        for absa in (1,3,5,7,9):
            spans=[r[3] for r in allr if r[3]!='NONE' and len(r[0])==n and abs(r[1])==absa and r[3]>0]
            print('n=%d |a|=%d: min span(J != unit) = %s'%(n,absa,min(spans)))
    nm=sorted([r for r in allr if r[3]!='NONE' and r[3]>0 and abs(r[1])>=3],key=lambda r:r[3])[:15]
    print('smallest-span non-unit closures with |a|>=3:',[(tuple(R6[i][2] for i in r[0]),r[1],r[2],r[3],r[4]) for r in nm[:8]])
    a20=[r for r in allr if r[3]!='NONE' and r[3]>0 and r[4]==0]
    print('a_2 = 0 non-unit closures:',len(a20),' min span among them:',min([r[3] for r in a20]) if a20 else None)
    deep=sorted([r for r in allr if r[3]!='NONE' and abs(r[1])>=3],key=lambda r:-max(r[6],r[7]))
    print('deepest one-ended cancellations (|a|>=3):',[(r[0],r[1],r[2],r[6],r[7],r[3]) for r in deep[:12]])
    print('max min(rt,rb) over |a|>=3:',max(min(r[6],r[7]) for r in allr if r[3]!='NONE' and abs(r[1])>=3))
    pickle.dump(allr,open(OUT+'jstar.pkl','wb'))
