"""refV3 (ii'): the same exact lemma checks on the word library R(L) (engineA convention: reduced words of length <= L in X,x,Y,y,
first letter X/x, non-integral, canonical mod Y), using only the vector (a,b) (no normal form): T2 + class bounds, BX3, BX4' in the
form 'R_1-top & rho_a=-1 => rho_b=0, l2(b)<=-1', BX5 bound, C1 certificate sup, Lemma S (delta, sigma, lc), S3 (tau), at both ends
(bottom class read from the bottom data)."""
import sys, time
sys.dont_write_bytecode=True
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundD/refV3/src')
from fractions import Fraction as Fr
import lib
from boxlemmas import enddata, topclass
L=int(sys.argv[1]) if len(sys.argv)>1 else 10
t0=time.time()
R=lib.rational(L); print('R(%d): %d boxes (%.1fs)'%(L,len(R),time.time()-t0),flush=True)
bounds={'R1':Fr(-3,2),'S0':Fr(-1,2),'R0':Fr(-2),'S1':Fr(0),'S2':Fr(-1),'S3+':Fr(-1)}
def mirror(p): return {-e:c for e,c in p.items()}
fails={}; cnt={}; mx={}
def F(name,info): fails.setdefault(name,[]).append(info)
for key,v,T,tag in R:
    a,b=v
    for end in ('t','b'):
        if end=='t': A,B=a,b
        else: A,B=mirror(a),mirror(b)      # bottom of (a,b) = top of (a(1/t), b(1/t)) up to units: classes read the same way
        cls=topclass(A,B) if end=='t' else None
        D=enddata(a,b,end)
        ra=D['la'][0]; rb=D['lb'][0]; rq=D['lq'][0]; l2a=D['la'][1]; l2b=D['lb'][1]; lq2=D['lq'][1]
        # class from data at this end: R if |deg b - deg a| = 2 ... at bottom deg difference is in terms of t-expansion
        dd=D['db']-D['da']
        if end=='t': c2 = cls
        else:
            # bottom: by R2 the bottom of u is the top of u'' with q(u)(1/t) = t^-3 q(u''); so deg diff at bottom = -(dd'') + 3
            ddm=3-dd   # = top class deg diff of mirror box
            if ddm==2: c2='R1' if rq==1 else ('R0' if rq==0 else '?')
            elif ddm==0:
                if rq==-1: c2='S0'
                else:
                    # j from first nonzero of q-1 at this end
                    bs={e-3:c for e,c in b.items()}     # bottom: q ~ t^3 (1 - (-1)^j t^(1+j) ..)
                    diff={e:c for e,c in ((e,bs.get(e,0)-a.get(e,0)) for e in set(a)|set(bs)) if c}
                    j=min(diff)-D['da']-1
                    c2='S%d'%j if j<=2 else 'S3+'
            else: c2='?'
        cnt[(end,c2)]=cnt.get((end,c2),0)+1
        if c2 not in bounds: F('class',(T,end,c2)); continue
        if c2.startswith('R') and ra>-1: F('BX3 R',(T,end))
        if c2.startswith('S') and ra>0: F('BX3 S',(T,end))
        if rb>0: F('BX3 rho_b',(T,end))
        v2=lq2+ra
        if v2>bounds[c2]: F('T2',(T,end,c2,v2))
        if c2=='R1' and ra==-1 and (rb!=0 or l2b>-1): F("BX4'",(T,end,rb,l2b))
        if ra==-1 and rq==0:
            k_=('BX5',c2); mx[k_]=max(mx.get(k_,l2b),l2b)
            if l2b>Fr(1,2): F('BX5',(T,end,l2b))
        g=200*ra+101*rq+100*l2a+100*lq2
        mx['cert']=max(mx.get('cert',g),g)
        if g>-150: F('cert',(T,end,g))
    Dt=enddata(a,b,'t'); Db=enddata(a,b,'b')
    if (max(b)-min(b))-(max(a)-min(a))!=-1: F('delta',T)
    if Dt['lq'][0]+Db['lq'][0]!=0: F('sigma',T)
    if Dt['lq'][1]+Db['lq'][1]!=-1: F('tau',T)
    if Fr(Dt['cb'],Dt['ca'])*Fr(Db['cb'],Db['ca'])!=-1: F('lc',T)
print('class counts',cnt)
print('max',mx)
print('FAILURES',{k:len(v) for k,v in fails.items()})
for k,v in fails.items(): print(' ',k,v[:3])
print('time %.1f'%(time.time()-t0))
