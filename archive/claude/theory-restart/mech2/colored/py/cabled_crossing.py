#!/usr/bin/env python3
"""The 16 smoothings of a 2-cabled crossing (over band y=+-1, under band x=+-1).
A-smoothing at a crossing joins W<->N and E<->S ends; B joins W<->S and N<->E.
Classify the resulting crossingless (4,4)-tangle: A2 (cable of A), B2 (cable of B), M (no turnback, mixed), or turnback; count closed circles."""
import itertools,collections
X=[(-1,1),(1,1),(-1,-1),(1,-1)]   # crossings; (-1,1),(1,-1) are self-crossings of copies 1,2; (1,1),(-1,-1) are mixed
strand=[  # connections along strands
 ('w1',((-1,1),'W')),(((-1,1),'E'),((1,1),'W')),(((1,1),'E'),'e1'),
 ('w2',((-1,-1),'W')),(((-1,-1),'E'),((1,-1),'W')),(((1,-1),'E'),'e2'),
 ('n1',((-1,1),'N')),(((-1,1),'S'),((-1,-1),'N')),(((-1,-1),'S'),'s1'),
 ('n2',((1,1),'N')),(((1,1),'S'),((1,-1),'N')),(((1,-1),'S'),'s2')]
ends=['w1','w2','e1','e2','n1','n2','s1','s2']
side={e:e[0] for e in ends}
res=collections.defaultdict(list)
for bits in itertools.product([0,1],repeat=4):
    adj=collections.defaultdict(list)
    for a,b in strand: adj[a].append(b); adj[b].append(a)
    for x,bit in zip(X,bits):
        pairs=[('W','N'),('E','S')] if bit==0 else [('W','S'),('N','E')]
        for p,q in pairs: adj[(x,p)].append((x,q)); adj[(x,q)].append((x,p))
    seen=set(); match=[]; loops=0
    for e in ends:
        if e in seen: continue
        prev=None; cur=e; seen.add(e)
        while True:
            nxt=[z for z in adj[cur] if z!=prev]
            if cur in ends and prev is not None: break
            prev,cur=cur,nxt[0]
            seen.add(cur)
        match.append(tuple(sorted((e,cur))))
    nodes=set(adj)
    comp_nodes=set(seen)
    for n in nodes:
        if n in comp_nodes: continue
        loops+=1
        stack=[n]
        while stack:
            z=stack.pop()
            if z in comp_nodes: continue
            comp_nodes.add(z); stack+=adj[z]
    m=tuple(sorted(match))
    turn=any(side[a]==side[b] for a,b in m)
    sides=tuple(sorted(tuple(sorted((side[a],side[b]))) for a,b in m))
    if turn: typ='turnback'
    elif sides==(('n','w'),('n','w'),('e','s'),('e','s')): typ='A2'
    elif sides==(('e','n'),('e','n'),('s','w'),('s','w')): typ='B2'
    else: typ='M'
    res[typ].append((sum(bits),bits,loops,m if typ in('M',) else ''))
for typ in ['A2','M','B2','turnback']:
    print(typ)
    for r,bits,loops,m in sorted(res[typ]):
        print('   r=%d  smoothing at [(-1,1),(1,1),(-1,-1),(1,-1)] = %s  closed circles: %d  %s'%(r,bits,loops,m))
print('M Poincare polynomial sum h^r q^r (q+1/q)^loops:')
import sympy as sp
h,q=sp.symbols('h q')
P=sum(h**r*q**r*(q+1/q)**loops for r,bits,loops,m in res['M'])
print('  ',sp.expand(P),'  at h=-1:',sp.factor(P.subs(h,-1)))
