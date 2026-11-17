"""size_and_facts.py -- exact partial facts within the stop rule:
 (1) numpy exact Burau (deck convention phi(x)=t^-1) coefficient sums = size proxy for iota(alpha,(beta*_3)X);
 (2) Burau at t=-1, 2 for Phi_0, Phi, Gamma_1, y_i;  (3) ranking of small Brunnian cap BI_4 candidates;
 (4) (beta*_3)Phi_0 : disk-type census, M_{Phi_0}(t), parity statistics  (iota = 976672, feasible, linear time)."""
import sys, time, json
import numpy as np
HERE='/private/tmp/claude-501/-Users-calebbarnett/7610ac96-4d03-4d32-b526-8a5647837809/scratchpad/bbb-attack'
sys.path.insert(0, HERE+'/scripts')
from braidarc import *
from fractions import Fraction
out = {}
def log(*a):
    print(*a, flush=True)

def burau_np(braid, n):
    L = len(braid) + 2; D = 2*L+1; off = L
    M = np.zeros((n, n, D), dtype=object)
    for r in range(n): M[r, r, off] = 1
    def sh(v, k):  # multiply by t^k
        w = np.zeros_like(v)
        if k >= 0: w[k:] = v[:D-k]
        else: w[:D+k] = v[-k:]
        return w
    for s in braid:
        i = abs(s)
        c0, c1 = M[:, i-1, :].copy(), M[:, i, :].copy()
        for r in range(n):
            if s > 0:
                M[r, i-1, :] = sh(c1[r], -1)
                M[r, i, :] = c0[r] + c1[r] - sh(c1[r], -1)
            else:
                M[r, i-1, :] = c0[r] - sh(c0[r], 1) + c1[r]
                M[r, i, :] = sh(c0[r], 1)
    return M, off
def coeffsum(M): return int(sum(abs(int(x)) for x in M.flatten()))
def eval_np(M, off, t):
    n = M.shape[0]; t = Fraction(t)
    return [[sum(Fraction(int(M[r,c,k])) * t**(k-off) for k in range(M.shape[2]) if M[r,c,k] != 0) for c in range(n)] for r in range(n)]
def is_id(E): return all(E[r][c] == (1 if r == c else 0) for r in range(len(E)) for c in range(len(E)))
def row3_moody_size(M, off):
    # unsimplified-size proxy: sum |coeff| of (-row3[0] + t^-1 row3[1]) / (1-t^-1) ... just report sum|row 3|
    return int(sum(abs(int(x)) for x in M[2].flatten()))

A14=[3,2,1,1,-2,-3]; A24=[3,2,2,-3]; A34=[3,3]
a=[1,2]*6; b=comm(comm(A14,A24),A34); phi0=comm(a,b)
G1_seq=[1,3,2,1,3,1,0,3,1,2,3,1]; G1y=xprime_to_nested(loop_seq_to_xprime_word(G1_seq,'L',4),4); G1=push_braid_nested(G1y,4)
y={k:push_braid_nested([k],4) for k in (1,2,3)}
w0y=[-2, -1, 2, 2, -3, -2, 1, 2]  # placeholder replaced below
T4=arc_of_braid(phi0,4); w0y=xprime_to_nested(loop_seq_to_xprime_word(T4,'L',4),4)
m=len(w0y)+1
Phi_y=reduce_word(inv_word(G1y)+[1]*m+w0y+[-1]*m+G1y); Phi=push_braid_nested(Phi_y,4)
log("Gamma_1 y-word", G1y, "; Phi_0 y-word", w0y, "len", len(w0y), "; m", m, "; Phi braid len", len(Phi))
out['Gamma1_y']=G1y; out['Gamma1_braid']=G1; out['Phi0_y']=w0y; out['m']=m; out['Phi_y']=Phi_y; out['Phi_braid']=Phi; out['y_braids']=y
# (2) exact Burau facts
facts={}
for name, br in [('Phi_0',phi0),('Phi',Phi),('Gamma_1',G1),('y1',y[1]),('y2',y[2]),('y3',y[3]),('b=[[A14,A24],A34]',b),('(s1s2)^6',a)]:
    for n in (4,5):
        M,off=burau_np(br,n)
        f={'coeffsum':coeffsum(M),'I_at_-1':is_id(eval_np(M,off,-1)),'I_at_2':is_id(eval_np(M,off,2)),'row3_coeffsum':row3_moody_size(M,off)}
        facts[f"{name}|B_{n}"]=f
        log(f"{name:22s} B_{n}: coeffsum={f['coeffsum']:>12d} row3={f['row3_coeffsum']:>12d} I(t=-1)={f['I_at_-1']} I(t=2)={f['I_at_2']}")
out['burau_facts']=facts
# (3) candidates ranking
def delete_strand(braid, n, s):
    outw=[]; pos=s
    for g in braid:
        i=abs(g)
        if i==pos: pos=i+1; continue
        if i+1==pos: pos=i; continue
        outw.append((i if i<pos else i-1)*(1 if g>0 else -1))
    return outw
def artin_sig(braid,n): return tuple(tuple(apply_braid_to_word([j],braid)) for j in range(1,n+1))
def brunnian(br): return all(artin_sig(delete_strand(br,4,s),3)==artin_sig([],3) for s in range(1,5))
cands={}
a2=[2,3]*6
bs={'[[A14,A24],A34]':b,'[[A14,A34],A24]':comm(comm(A14,A34),A24),'[[A24,A34],A14]':comm(comm(A24,A34),A14),'[A14,[A24,A34]]':comm(A14,comm(A24,A34))}
xs={'(s1s2)^6':a,'(s2s3)^6':a2,'s3(s1s2)^6s3^-1':[3]+a+[-3],'s1(s2s3)^6s1^-1':[1]+a2+[-1],'s2(s1s2)^6s2^-1':[2]+a+[-2]}
for xn,x in xs.items():
    for bn,bb in bs.items():
        cands[f"[{xn},{bn}]"]=comm(x,bb)
for g in ([1],[-1],[2],[-2],[3],[-3],[1,2],[2,3],[3,3],[1,1],[2,2]):
    cands[f"conj({g})Phi_0"]=g+phi0+braid_inverse(g)
rank=[]
t0=time.time()
for name,br in cands.items():
    M,off=burau_np(br,4)
    cs=coeffsum(M); r3=row3_moody_size(M,off)
    triv=is_id(eval_np(M,off,2)); tm1=is_id(eval_np(M,off,-1))
    rank.append((cs,r3,name,len(br),tm1,triv))
rank.sort()
log("candidate ranking by exact-Burau coefficient sum (B_4): [coeffsum, row3sum, name, len, I(t=-1), I(t=2)]")
for r in rank: log("   ",r)
out['ranking']=rank
best=[r for r in rank if r[4] and not r[5]]
log("smallest nontrivial-at-t=2, trivial-at-t=-1 candidate:", best[0] if best else None, " Brunnian?", brunnian(cands[best[0][2]]) if best else None)
out['best']=best[0] if best else None
# (4) arc of Phi_0 (iota = 976672): linear-time census
t0=time.time(); T0=arc_of_braid(phi0,3); log("(beta*_3)Phi_0 computed: len T", len(T0), "iota", T0.count(1), "%.0fs"%(time.time()-t0))
var4={j:0 for j in range(1,5)}
# streaming disk census (avoid storing cumulative arrays): walk and accumulate
deck=0; wind=[0]*5; last_alpha=None; terms=[]; census={}; viol={}; nd=0
import collections
census=collections.Counter(); viol=collections.Counter()
prev_eps=None; prev_wind=None
for idx,aa in enumerate(T0):
    j=idx+1; up=(j%2==1)
    if aa==1:
        eps=-1 if up else 1
        terms.append((eps,deck))
        if prev_wind is not None:
            wv=[wind[p]-prev_wind[p] for p in range(5)]
            P=tuple(p for p in range(1,5) if wv[p]!=0); chg=(eps!=prev_eps)
            key=(P,'chg' if chg else 'prs'); census[key]+=1
            if chg != (len(P)%2==1): viol[key]+=1
        prev_eps=eps; prev_wind=list(wind)
    if up:
        bb=T0[idx+1] if idx+1<len(T0) else None
        if bb is None: rng,sg=(range(aa+1,3),1) if aa<3 else (range(4,aa+1),-1)
        elif bb>aa: rng,sg=range(aa+1,bb+1),1
        else: rng,sg=range(bb+1,aa+1),-1
        for p in rng: deck+=sg; wind[p]+=sg
poly=collections.Counter()
for e,k in terms: poly[k]+=e
log("M_{Phi_0}(t) simplified (exponent: coeff):", dict(sorted(poly.items())))
sp=[e*(-1 if k%2 else 1) for e,k in terms]
log("M_{Phi_0}(-t) sign pattern: #+=%d #-=%d ; |M(-1)| = %d vs iota = %d" % (sp.count(1),sp.count(-1),abs(sum(e*(-1)**(k%2) for e,k in terms)),len(terms)))
log("disk census (P, changing/preserving): count  [* = parity violator]")
for k,v in sorted(census.items(), key=lambda kv:-kv[1]): log("   ",k,v,"*" if k in viol else "")
log("total disks", sum(census.values()), "violators", sum(viol.values()), "4-disks", sum(v for k,v in census.items() if len(k[0])==4))
out['Phi0_arc']={'lenT':len(T0),'iota':len(terms),'M_simplified':{str(k):v for k,v in sorted(poly.items())},'signpat_plus':sp.count(1),'signpat_minus':sp.count(-1),
                 'census':{str(k):v for k,v in census.items()},'violators':{str(k):v for k,v in viol.items()}}
json.dump(out,open(HERE+'/results/size_and_facts.json','w'),default=str)
log("done")
