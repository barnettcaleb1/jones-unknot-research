"""Exact leading-rank-one certificates for words in kernel conjugates."""
from braid_conjugates import *
from fractions import Fraction

def lead(m):
    degree=max(e for row in m for p in row for e in p)
    return degree,[[p.get(degree,0) for p in row] for row in m]
def factor_rank_one(L):
    for i,row in enumerate(L):
        for j,x in enumerate(row):
            if x:
                u=[r[j] for r in L];v=[Fraction(a,x) for a in L[i]]
                if all(Fraction(L[r][s])==u[r]*v[s] for r in range(5) for s in range(5)):
                    return u,v
                return None
def dot(u,v):return sum(a*b for a,b in zip(u,v))
def wrap(v,L,u):return sum(v[i]*L[i][j]*u[j] for i in range(5) for j in range(5))
def run():
    contexts=[[]]+[[s*i] for s in (-1,1) for i in range(1,5)]
    entries=[]
    for sign in [1,-1]:
        for c in contexts:
            w=bk.inv(c)+bk.power(bk.KERNEL,sign)+c
            d,L=lead(tl.rho(w));fact=factor_rank_one(L)
            entries.append(dict(sign=sign,c=c,degree=d,L=L,fact=fact))
    for i,e in enumerate(entries):
        print(i,e['sign'],e['c'],'degree',e['degree'],'rank1',bool(e['fact']))
    edges=[];cliques=[]
    for i,a in enumerate(entries):
        if not a['fact']:continue
        u,v=a['fact']
        for j,b in enumerate(entries):
            if b['fact'] and dot(v,b['fact'][0]):edges.append((i,j))
    alpha=bk.ANCHOR;da,La=lead(tl.rho(alpha))
    for i in range(len(entries)):
        for j in range(i+1,len(entries)):
            pair=[i,j]
            if not all((a,b) in edges for a in pair for b in pair):continue
            if all(wrap(entries[b]['fact'][1],La,entries[a]['fact'][0]) for a in pair for b in pair):
                cliques.append(pair)
    print('complete pairs with C-wrap',cliques)
    print('nonzero wraps',[(i,j) for i,a in enumerate(entries) for j,b in enumerate(entries)
          if a['fact'] and b['fact'] and wrap(b['fact'][1],La,a['fact'][0])])
    (ROOT/'braid_leading_results.json').write_text(json.dumps(dict(entries=[{k:v for k,v in e.items() if k!='fact'} for e in entries],
                         edges=edges,complete_pairs=cliques,anchor=alpha,anchor_degree=da,anchor_leading=La),indent=2))
    return entries

if __name__=='__main__':run()
