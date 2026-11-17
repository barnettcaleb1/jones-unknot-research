#!/usr/bin/env python3
"""Is Kh~ of a knot Szabo-matchable down to its determinant?  (pairs (h,q) -> (h+k, q+2k-2), k>=2.)
usage: matchable.py torus P Q ... | matchable.py word NAME MORSEWORD"""
import sys,os,subprocess
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/tools')
import surgery_collapse as sc
def torus_word(p,q,letter='x'):
    w=['r%d'%i for i in range(1,p)]
    for _ in range(q):
        w+=['%s%d'%(letter,i) for i in range(p-1)]
    w+=['u%d'%i for i in range(p-1,0,-1)]
    return '.'.join(w)
def report(name,word):
    gens=sc.closure_gens(name,word)
    if gens is None: print(name,'timeout/failed'); return
    det=abs(sum((-1)**((q//2-h)%2) for h,q in gens))
    mm=sc.max_matching(gens)
    levels={}
    for h,q in gens: levels.setdefault(q//2-h,[]).append(q)
    print('%s: rank %d, det %d, max Szabo matching %d, minimal rank %d  %s'%(name,len(gens),det,mm,len(gens)-2*mm,'MATCHABLE to det' if len(gens)-2*mm==det else 'NOT matchable to det'))
    print('     '+' | '.join('d=%d:%s'%(d,sorted(levels[d])) for d in sorted(levels)))
if __name__=='__main__':
    if sys.argv[1]=='torus':
        args=sys.argv[2:]
        for i in range(0,len(args),2):
            p,q=int(args[i]),int(args[i+1]); report('torus_%d_%d'%(p,q),torus_word(p,q))
    else:
        report(sys.argv[2],sys.argv[3])
