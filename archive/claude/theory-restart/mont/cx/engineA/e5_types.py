"""Second-order 'end types' of rational boxes and the exact combinatorics of two-ended ties.
type(u) = (top: d, lc, s1) , (bot: d, lc, s1) of the slope q = b/a (series datum, K=1).  Additive data: d, s1; multiplicative: lc.
A closure F = w1 A + w t^-3N B ties to order 2 at both ends iff for both ends: sum d - 3N = d*, prod lc = lc*, sum s1 = s1*."""
import sys, itertools, collections
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineA')
import vc, eng, lib, ser
from fractions import Fraction as Fr
def types(pool,K=1):
    T=collections.Counter(); ex={}
    for b in pool:
        tp=ser.slope(b[1],'top',K); bt=ser.slope(b[1],'bot',K)
        key=(tp[0],tp[1],tp[2],bt[0],bt[1],bt[2])
        T[key]+=1; ex.setdefault(key,b)
    return T,ex
def target(w1,w,K=1):
    out=[]
    for end in ('top','bot'):
        T=ser.divD(ser.pdata(w1,end,K),ser.pdata(w,end,K)); out.append((T[0],-T[1],T[2]))
    return out
def solve(keys,n,tt,tb,maxn=None):
    """multisets of n types meeting both targets at order K (N free, same N both ends)"""
    sols=[]
    for ms in itertools.combinations_with_replacement(range(len(keys)),n):
        dt=sum(keys[i][0] for i in ms); db=sum(keys[i][3] for i in ms)
        if (dt-tt[0])%3 or (dt-tt[0])!=(db-tb[0]): continue
        lt=1; lb=1
        for i in ms: lt*=keys[i][1]; lb*=keys[i][4]
        if lt!=tt[1] or lb!=tb[1]: continue
        st=[sum(keys[i][2][k] for i in ms) for k in range(len(tt[2]))]   # K=1: additive
        sb=[sum(keys[i][5][k] for i in ms) for k in range(len(tb[2]))]
        if st!=list(tt[2]) or sb!=list(tb[2]): continue
        sols.append(ms)
    return sols
if __name__=='__main__':
    L=int(sys.argv[1]) if len(sys.argv)>1 else 8
    pool=lib.rational(L)
    T,ex=types(pool)
    keys=list(T)
    print('rational R(%d): %d boxes, %d second-order end types'%(L,len(pool),len(keys)))
    for k in keys: print('  type top(d=%d,lc=%d,s1=%s) bot(d=%d,lc=%d,s1=%s) x%d'%(k[0],k[1],k[2][0],k[3],k[4],k[5][0],T[k]), ex[k][2])
    for a in (3,5,7,9,11,-3,-5,-7,-9,-11):
        a1,aV=eng.WV(a); tt,tb=target(a1,aV)
        n=abs(a)+1
        sols=solve(keys,n,tt,tb)
        print('vertical a=%d (n=%d): targets top %s bot %s : %d second-order two-ended type-multisets'%(a,n,(tt[0],tt[1],[str(x) for x in tt[2]]),(tb[0],tb[1],[str(x) for x in tb[2]]),len(sols)))
        for s in sols[:3]: print('     ',[ (keys[i][0],keys[i][1],str(keys[i][2][0]),keys[i][3],keys[i][4],str(keys[i][5][0])) for i in s])
    for mu in (1,-1,2,-2,3,-3,5):
        a1,a3=eng.W(mu); tt,tb=target(a1,a3)
        for n in (1,2,3,4,5):
            sols=solve(keys,n,tt,tb)
            if sols: print('horizontal mu=%d n=%d: %d multisets'%(mu,n,len(sols)))
