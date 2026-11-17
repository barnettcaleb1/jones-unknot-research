"""Referee necklace-level tests: N1-N5, N3, N4, main theorem, M4, S3 on random + forced-tie necklaces (independent code)."""
import random, time, sys
from rcore import *
from t_box import auto, exact_state
from fractions import Fraction
SEED=int(sys.argv[1]) if len(sys.argv)>1 else 1
NT=int(sys.argv[2]) if len(sys.argv)>2 else 500
KMAX=int(sys.argv[3]) if len(sys.argv)>3 else 10
MMAX=int(sys.argv[4]) if len(sys.argv)>4 else 7
NMAX=int(sys.argv[5]) if len(sys.argv)>5 else 9
rnd=random.Random(SEED)
cache={}
def boxdata(s):
    if s not in cache:
        u=ubox(s); a=ach(u); b=bch(u)
        st,rho_auto,rq=auto(s)
        cache[s]=(a,b,st,rho_auto,rq,xs(a,2)[1],xs(b,2)[1])
    return cache[s]
def gseq():
    mode=rnd.choice(['unif','neg1','pos1','alt','small','altneg','one'])
    if mode=='one': 
        s=(rnd.choice([-2,-3,1,2]),)
        return s
    k=rnd.randint(1,KMAX); s=[]
    for i in range(k):
        if mode=='unif': m=rnd.choice([x for x in range(-MMAX,MMAX+1) if x])
        elif mode=='neg1': m=-1 if rnd.random()<0.7 else rnd.choice([x for x in range(-MMAX,MMAX+1) if x])
        elif mode=='pos1': m=1 if rnd.random()<0.7 else rnd.choice([x for x in range(-MMAX,MMAX+1) if x])
        elif mode in ('alt','altneg'): m=(1 if i%2==0 else -1)*rnd.randint(1,MMAX)
        else: m=rnd.choice([-2,-1,1,2])
        s.append(m)
    if mode=='altneg' and s[-1]>0: s=[-x for x in s]
    if s[0] in (0,-1): s[0]=rnd.choice([-2,-3]) if mode=='altneg' else rnd.choice([-2,-3,1,2])
    if mode=='altneg' and s[0]>0 and len(s)%2==0: pass
    return tuple(s)
def wx(mu):
    W1=w1(mu); W3=w3(mu)
    return (tp(W1),W1[tp(W1)],xs(W1,2)[1]),(tp(W3),W3[tp(W3)],xs(W3,2)[1])
def predict_top(mu,N,seqs):
    """theory prediction at the TOP: ('tie',type,s1,s3,c1w1A-sign info) or ('gen',ratio, Delta)"""
    (t1,c1,r1),(t3,c3,r3)=wx(mu)
    bd=[boxdata(s) for s in seqs]
    rho=sum(1 for x in bd if x[2][0]=='R')
    d=2*rho-3*N
    Delta=t3-t1+d
    eps=c3*c1*(-1)**rho
    s1=r1+sum(x[3] for x in bd)
    s3=r3+sum(x[3]+x[4] for x in bd)
    if Delta==0 and eps==-1: return ('tie',s1,s3,rho,d)
    if Delta<=-2: return ('gen',Fraction(s1),Delta)
    if Delta==-1: return ('gen',Fraction(s1+eps),Delta)
    if Delta==0: return ('gen',Fraction(s1+s3,2),Delta)
    if Delta==1: return ('gen',Fraction(s3+eps),Delta)
    return ('gen',Fraction(s3),Delta)
def mirror(s): return (-s[0]-1,)+tuple(-m for m in s[1:])
def tie_type_top(mu,rho,d):
    if mu>=1 and d==0 and rho%2==0: return 'T1'
    if mu<=-2 and d==-1 and rho%2==1: return 'T2'
    if mu==-1 and d==-3 and rho%2==0: return 'T3'
    return None
def tie_type_bot(mu,rho,d,n):
    if mu<=-1 and d==-n and (rho-n)%2==0: return 'B1'
    if mu>=2 and d==1-n and (rho-n)%2==1: return 'B2'
    if mu==1 and d==3-n and (rho-n)%2==0: return 'B3'
    return None
def forced_params(seqs):
    n=len(seqs); rho=sum(1 for s in seqs if boxdata(s)[2][0]=='R')
    c=[]
    for mu in [m for m in range(-9,10) if m]:
        for N in range(-15,20):
            d=2*rho-3*N
            if tie_type_top(mu,rho,d) or tie_type_bot(mu,rho,d,n): c.append((mu,N))
    return c
if __name__=="__main__":
    stats=dict(neck=0,forced=0,unit=0,M4bad=0,N12bad=0,twoend=0,N5bad=0,c2zero_nonP1=0,P1=0,P1bad=0,notie_spanbad=0,
               S3n=0,S3bad=0,S3formula_bad=0,matrix_checked=0,matrix_bad=0,minspan_minus_4n=10**9)
    types={}
    t0=time.time()
    for it in range(NT):
        n=rnd.randint(2,NMAX)
        seqs=[gseq() for _ in range(n)]
        if rnd.random()<0.6:
            fp=forced_params(seqs)
            if not fp: continue
            mu,N=rnd.choice(fp); stats['forced']+=1
        else:
            mu=rnd.choice([m for m in range(-9,10) if m]); N=rnd.randint(-12,15)
        bd=[boxdata(s) for s in seqs]
        A=fprod([x[0] for x in bd]); B=fprod([x[1] for x in bd]); Bp=sh(B,-3*N)
        P1_=ml(w1(mu),A); P3_=ml(w3(mu),Bp); G=ad(P1_,P3_)
        J=pdiv_exact(G,PHI3)
        stats['neck']+=1
        if rnd.random()<0.03 and sum(len(s) for s in seqs)<40:
            Jm=neck_matrix(mu,N,[ubox(s) for s in seqs]); stats['matrix_checked']+=1
            if Jm!=J: stats['matrix_bad']+=1; print('MATRIX MISMATCH',mu,N,seqs)
        if len(J)<2: stats['unit']+=1; print('UNIT!',mu,N,seqs,J)
        # M4: J = 1 mod t^4-1
        res=[0,0,0,0]
        for e,c in J.items(): res[e%4]+=c
        if res!=[1,0,0,0]: stats['M4bad']+=1
        rho=sum(1 for x in bd if x[2][0]=='R'); d=2*rho-3*N
        ttop=tie_type_top(mu,rho,d); tbot=tie_type_bot(mu,rho,d,n)
        act_top = tp(P1_)==tp(P3_) and P1_[tp(P1_)]==-P3_[tp(P3_)]
        act_bot = bt(P1_)==bt(P3_) and P1_[bt(P1_)]==-P3_[bt(P3_)]
        if act_top!=(ttop is not None) or act_bot!=(tbot is not None): stats['N12bad']+=1; print('N1/N2 MISMATCH',mu,N,seqs)
        if act_top and act_bot: stats['twoend']+=1; print('TWO-ENDED TIE',mu,N,seqs)
        key=(ttop or '-')+'/'+(tbot or '-'); types[key]=types.get(key,0)+1
        sA=sum(sp(x[0]) for x in bd)
        stats['minspan_minus_4n']=min(stats['minspan_minus_4n'],sp(J)-4*n)
        if not act_top and not act_bot:
            if sp(J)<sA-2: stats['notie_spanbad']+=1; print('NO-TIE SPAN FAIL',mu,N,seqs,sp(J),sA)
        # clean-end predictions
        for end in ('top','bot'):
            if end=='top':
                pr=predict_top(mu,N,seqs); cJ=xs(J,3,'top'); tied=act_top
            else:
                pr=predict_top(-mu,n-N,[mirror(s) for s in seqs]); cJ=xs(J,3,'bot'); tied=act_bot
            if pr[0]=='tie':
                if not tied: stats['N5bad']+=1
                continue
            ratio=pr[1]
            if cJ[1]+1!=ratio: stats['N5bad']+=1; print('N5 MISMATCH',end,mu,N,seqs,cJ,ratio)
            if cJ[1]==0:
                # must be P1 (or its mirror)
                isP1 = (end=='top' and mu==-2 and n%6==0 and 3*N==n and all(x[2][0]=='S' and x[5]==0 for x in bd))
                isP1m= (end=='bot' and mu==2 and n%6==0 and 3*(n-N)==n and all(boxdata(mirror(s))[2][0]=='S' and boxdata(mirror(s))[5]==0 for s in seqs))
                if not (isP1 or isP1m):
                    stats['c2zero_nonP1']+=1
                    if act_top or act_bot: stats['c2zero_in_tiecase']=stats.get('c2zero_in_tiecase',0)+1; print('c2=0 outside P1 IN TIE CASE',end,mu,N,seqs,ttop,tbot)
                else:
                    stats['P1']+=1
                    ss=seqs if end=='top' else [mirror(s) for s in seqs]
                    Yv=sum(xs(boxdata(s)[0],3)[2] for s in ss)
                    if cJ[2]!=Yv-1 or cJ[2]==0: stats['P1bad']+=1; print('P1 FAIL',seqs,cJ,Yv)
        # S3 at a top tie
        if act_top:
            stats['S3n']+=1
            pr=predict_top(mu,N,seqs); s1,s3=pr[1],pr[2]
            D=tp(P1_); c1=P1_[D]
            if G.get(D-1,0)!=c1*(s1-s3): stats['S3bad']+=1; print('S3 FAIL',mu,N,seqs)
            nS0=sum(1 for x in bd if x[2]==('S',0)); sR=sum(x[2][1] for x in bd if x[2][0]=='R')
            form=(1 if mu==-2 else 0)-(1 if mu in (1,-1) else 0)+nS0-sR
            if form!=s1-s3: stats['S3formula_bad']+=1
    print(stats); print('tie types',types); print('time',round(time.time()-t0,1))
