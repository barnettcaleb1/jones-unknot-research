"""Parser for kht++ chain files (current build symbols: ⬮ = Q_0 = unit of the horizontal sum = '•', ⬯ = Q_inf = 'o').
Degree rule: arrow x --a--> y: h(y)=h(x)+1, q(y)=q(x)+deg(a), deg(S^k)=k, deg(D^k)=2k."""
import re, os, glob
from fractions import Fraction as Fr
from collections import Counter
def parse_chain(line):
    m=re.match(r'\s*\d+\)\s*h\^\s*(-?\d+)\s*q\^\s*(-?\d+)\s*δ\^\s*(-?[\d/]+)\s*(\S+)(.*)$',line)
    if not m: return None
    h,q,chain,rest=int(m.group(1)),int(m.group(2)),m.group(4),m.group(5).strip()
    toks=re.findall(r'[⬮⬯]|[^⬮⬯]+',chain)
    gens=[t for t in toks if t in '⬮⬯']; arrows=[t for t in toks if t not in '⬮⬯']
    n=len(gens); cyclic=(len(arrows)==n)
    info=[]
    for i,a in enumerate(arrows):
        left=gens[i]; right=gens[(i+1)%n]
        direction=+1 if a.endswith('>') else -1
        assert a.endswith('>')!=a.startswith('<'),a
        mm=re.search(r'([SD])(?:\^(\d+))?',a)
        if mm: kind=mm.group(1); power=int(mm.group(2) or 1)
        else:
            kind='S' if '~' in a else 'D'; power=1
            if kind=='S' and left==right: power=2
        info.append((direction,kind,power))
    G=[(gens[0],h,q)]
    for i in range(n-1):
        d,kind,p=info[i]; deg=p if kind=='S' else 2*p
        _,hh,qq=G[-1]; G.append((gens[i+1],hh+d,qq+d*deg))
    if cyclic:
        d,kind,p=info[n-1]; deg=p if kind=='S' else 2*p
        assert (G[-1][1]+d,G[-1][2]+d*deg)==(G[0][1],G[0][2]),line
    return dict(gens=G,arrows=info,cyclic=cyclic,label=rest)
def read_file(path):
    out=[]
    for line in open(path,encoding='utf-8'):
        c=parse_chain(line)
        if c: out.append(c)
    return out
def dots(chains):
    """multiset of (h,q) of the • generators"""
    C=Counter()
    for c in chains:
        for idem,h,q in c['gens']:
            if idem=='⬮': C[(h,q)]+=1
    return C
