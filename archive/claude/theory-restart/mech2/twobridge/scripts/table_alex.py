#!/usr/bin/env python3
"""Test: sum over N(T) of T^(5h-3q) [= T^(b-a)]  versus |Delta_{K_u} Delta_{K_l}| and |Delta_K| (absolute values of coefficients)."""
import sys,os,glob,collections,re
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import chain, constituents as cs
import sympy as sp
t=cs.t
base='/Users/calebbarnett/jones-lanes/theory-restart/lit/kht/out/k138/examples/si/'
def nat(s): return [int(x) if x.isdigit() else x for x in re.split(r'(\d+)',s)]
def abscoeffs(p):
    P=sp.Poly(sp.expand(p),t); c=[abs(int(x)) for x in P.all_coeffs()]
    return tuple(c)
def Nprofile(comps):
    cnt=collections.Counter()
    for c in comps:
        for g in c['gens']:
            if g[0]=='b': cnt[5*g[1]-3*g[2]]+=1
    lo,hi=min(cnt),max(cnt)
    return tuple(cnt.get(i,0) for i in range(lo,hi+1))
if __name__=='__main__':
    names=sorted([os.path.basename(f)[:-4] for f in glob.glob(base+'*.kht')],key=nat)
    stats=collections.Counter()
    for nm in names:
        word=open(base+nm+'.kht').read().split('\n')[1].strip()
        fn=base+nm+'/cxBNr-c2-qs'
        if not os.path.exists(fn): continue
        comps=chain.parse_file(fn)
        prof=Nprofile(comps)
        K,u,l=cs.consts(word)
        ul=abscoeffs(sp.expand(u*l)); kk=abscoeffs(K)
        m_ul=(prof==ul or prof==ul[::-1]); m_k=(prof==kk or prof==kk[::-1])
        stats[(m_ul,m_k)]+=1
        if not m_ul or (len(sys.argv)>1 and sys.argv[1]=='-v'):
            print('%-8s N-profile(b-a)=%s  |Ku*Kl|=%s  |K|=%s  match_ul=%s match_K=%s'%(nm,prof,ul,kk,m_ul,m_k))
    print('counts (match K_u*K_l, match K):',dict(stats))
