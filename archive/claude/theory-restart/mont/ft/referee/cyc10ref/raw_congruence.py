# Referee (lens B) test of the RAW congruence of Section 5, with the claimed framing T_fold = theta_U^-1 B.
# F_raw = reduced theta value with straight 0-framed axis and blackboard band = y (Q_0-coefficient of bracket_vector),
#   as a function of Q = -t^-1, t = A^4 (lp.J convention: exponent e of A -> e/4 of t).
# G_raw = <K, lifted framing>/<O> = theta_U^(n_y0-n_x0) * kauffman.bracket(word) at A_c, A_c^2 = Q, theta_U = -A_c^3.
# Claims under test: (i) all exponents of y are = 0 mod 4 (F_raw in Q(Q)); (ii) exponents of G_raw are even (G_raw in Q(Q));
# (iii) F_raw(zeta) = G_raw(zeta) at primitive 5th roots (exact, mod Phi_5) -- no sign or unit adjustment allowed.
import sys, random
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont')
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/tools')
import lp, flat_search as fs, kauffman, alex
from collections import Counter

def polymod_phi5(p):
    # p: {exp: coeff} Laurent in Q; reduce mod Phi_5 = Q^4+Q^3+Q^2+Q+1 (use Q^5=1 then Q^4 = -(1+Q+Q^2+Q^3))
    r=[0]*5
    for e,c in p.items(): r[e%5]+=c
    # now r represents sum r_k Q^k, k=0..4 modulo Q^5-1; reduce mod Phi_5: subtract r_4*Phi_5
    r4=r[4]
    return tuple(r[k]-r4 for k in range(4))

def F_raw(y):
    # y in A; A^4 = t = -Q^-1  => A^e = (-1)^(e/4) Q^(-e/4)
    out={}
    for e,c in y.items():
        if e%4: return None
        k=e//4
        out[-k]=out.get(-k,0)+c*(-1)**(k%2)
    return {e:c for e,c in out.items() if c}

def G_raw(kb,nx,ny):
    # theta_U^(ny-nx) * kb(A_c) ; theta_U=-A_c^3; A_c^2 = Q
    m=ny-nx
    out={}
    for e,c in kb.items():
        E=e+3*m
        if E%2: return None
        out[E//2]=out.get(E//2,0)+c*(-1)**(m%2)
    return {e:c for e,c in out.items() if c}

rnd=random.Random(int(sys.argv[1])); N=int(sys.argv[2])
n=0; stats=Counter(); bad=[]
while n<N:
    w=fs.gen(rnd,rnd.randint(6,18))
    if not w: continue
    half=alex.parse(w)
    full=alex.symmetrize(half)
    if full is None or alex.diagram(full) is None: continue
    bv=fs.bracket_vector(half)
    if bv is None: continue
    y,x=bv
    y={e:c for e,c in y.items() if c}
    u={}; fs.padd(u,y); fs.padd(u,fs.pdelta(x)); u={e:c for e,c in u.items() if c}
    if len(u)!=1: continue
    kb=kauffman.bracket(w)
    if not kb: continue
    kb={e:c for e,c in kb.items() if c}
    n+=1
    nx=sum(1 for c,s in half if c=='x' and s==0); ny=sum(1 for c,s in half if c=='y' and s==0)
    (eu,cu),=u.items()
    stats['eu mod4=%d'%(eu%4)]+=1
    F=F_raw(y); G=G_raw(kb,nx,ny)
    if F is None: stats['y exps not 0 mod 4']+=1; continue
    if G is None: stats['G odd exps']+=1; continue
    d={}; 
    for e,c in F.items(): d[e]=d.get(e,0)+c
    for e,c in G.items(): d[e]=d.get(e,0)-c
    if all(v==0 for v in polymod_phi5(d)): stats['raw F==G mod Phi5']+=1
    else:
        # diagnose: does it hold up to sign / unit?
        stats['raw FAIL']+=1
        if len(bad)<5: bad.append((w,nx,ny))
print('samples',n); [print(' ',k,v) for k,v in sorted(stats.items())]
for b in bad: print('fail example',b)
