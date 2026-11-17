"""Referee test of box laws BX1-BX4, TH-2BR facts, R2 on long random normal forms (independent code)."""
import random, time, sys
from rcore import *
from fractions import Fraction
rnd=random.Random(int(sys.argv[1]) if len(sys.argv)>1 else 1)
def gen_seq(kmax=30,M=12,mode=None):
    mode=mode or rnd.choice(['unif','neg1','pos1','alt','mixsmall','big'])
    k=rnd.randint(1,kmax)
    s=[]
    for i in range(k):
        if mode=='unif': m=rnd.choice([x for x in range(-M,M+1) if x])
        elif mode=='neg1': m=-1 if rnd.random()<0.7 else rnd.choice([x for x in range(-M,M+1) if x])
        elif mode=='pos1': m=1 if rnd.random()<0.7 else rnd.choice([x for x in range(-M,M+1) if x])
        elif mode=='alt': m=(1 if i%2==0 else -1)*rnd.randint(1,M)
        elif mode=='mixsmall': m=rnd.choice([-2,-1,1,2])
        else: m=rnd.choice([x for x in range(-M,M+1) if x])*rnd.choice([1,1,2])
        s.append(m)
    if mode=='alt' and rnd.random()<0.5: s=[-x for x in s]
    if s[0] in (0,-1): s[0]=rnd.choice([-2,-3,1,2])
    return tuple(s)
# report's automaton (BX2), coded independently from the REPORT text
def auto(seq):
    st=('init',); rho=0
    for m in seq:
        if st[0]=='init':
            st,r=(('R',1),-1) if m>=1 else (('S',0),0)
        elif m>=1:
            if st[0]=='R': st,r=(('R',0),0) if m==1 else (('R',1),-1)
            else: st,r=('R',1),-1
        else:
            if st[0]=='R': st,r=('S',0),st[1]
            else:
                j=st[1]
                if m<=-2: st,r=('S',0),-(1 if j==0 else 0)
                else: st,r=('S',j+1),-(1 if j==0 else 0)
        rho+=r
    rq = st[1] if st[0]=='R' else (-1 if st[1]==0 else 0)
    return st,rho,rq
def exact_state(v):
    d,c=ser_ratio(v[1],v[0],3)
    if d==-1 and c[0]==1: return ('R',c[1])
    if d<=-4 and c[0]==(-1)**((-4-d)%2): return ('S',-4-d)
    return ('?',d,c[:2])
if __name__=="__main__":
    stats=dict(n=0,auto_bad=0,ineq_bad=0,lc_bad=0,span_bad=0,degb_bad=0,eq_bad=0,mirror_bad=0,bx4_n=0,bx4_bad=0,maxk=0,maxspan=0)
    t0=time.time()
    NT=int(sys.argv[2]) if len(sys.argv)>2 else 1500
    for it in range(NT):
        s=gen_seq()
        u=ubox(s); a=ach(u); b=bch(u)
        stats['n']+=1; stats['maxk']=max(stats['maxk'],len(s))
        st,rho,rq=auto(s)
        est=exact_state(u)
        xa=xs(a,3); xb=xs(b,2)
        ra=xa[1]; rb=xb[1]
        if est!=st or ra!=rho or rb!=rho+rq:
            stats['auto_bad']+=1
            if stats['auto_bad']<6: print('AUTO MISMATCH',s,est,st,ra,rho,rb,rho+rq)
        R = est[0]=='R'
        if (R and ra>-1) or ((not R) and ra>0) or rb>0: 
            stats['ineq_bad']+=1; print('INEQ FAIL',s,est,ra,rb)
        # equality characterisation: S-top and rho_a==0 iff alternating & ends negative
        signs=[1 if m>0 else -1 for m in s]
        altneg = all(signs[i]!=signs[i+1] for i in range(len(s)-1)) and signs[-1]<0
        if ((not R) and ra==0) != altneg:
            stats['eq_bad']+=1; print('EQ FAIL',s,est,ra)
        # TH-2BR facts: lc a = +-1, span a >= 4, top-R iff last exponent >0, deg b-deg a, lc relation
        if abs(a[tp(a)])!=1 or abs(a[bt(a)])!=1: stats['lc_bad']+=1
        if sp(a)<4: stats['span_bad']+=1; print('SPAN<4',s,a)
        stats['maxspan']=max(stats['maxspan'],sp(a))
        if R != (s[-1]>0): stats['degb_bad']+=1
        if R and not (tp(b)-tp(a)==2 and b[tp(b)]==-a[tp(a)]): stats['degb_bad']+=1
        if (not R) and not (tp(b)==tp(a) and b[tp(b)]==a[tp(a)]): stats['degb_bad']+=1
        # BX4 on alternating S-boxes
        if altneg:
            stats['bx4_n']+=1
            pred=-Fraction(len(s)-(1 if s[0]<=-2 else 0),2)
            if xa[2]!=pred: stats['bx4_bad']+=1; print('BX4 FAIL',s,xa,pred)
        # R2 mirror
        s2=(-s[0]-1,)+tuple(-m for m in s[1:])
        u2=ubox(s2); k=len(s)
        if bar(a)!=sh(ach(u2),-4*k) or bar(b)!=sh(bch(u2),-4*k-3): stats['mirror_bad']+=1; print('MIRROR FAIL',s)
    print(stats,'time',round(time.time()-t0,1))
