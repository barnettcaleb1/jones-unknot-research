#!/usr/bin/env python3
"""Independent integer Kauffman-bracket contraction from the unsimplified PD.
No Regina, Spherogram, or Reidemeister simplification is used here.
"""
import json
from collections import defaultdict, Counter
from pathlib import Path

ROOT=Path(__file__).resolve().parent
def divide(p,d):
    p=dict(p);out={};m=max(d);lead=d[m]
    while p and max(p)>=m:
        k=max(p)-m;c=p[k+m]
        assert c%lead==0
        c//=lead;out[k]=c
        for e,v in d.items():
            p[e+k]=p.get(e+k,0)-c*v
            if not p[e+k]:del p[e+k]
    return out,p

def delta(p):
    out=defaultdict(int)
    for e,c in p.items():out[e+2]-=c;out[e-2]-=c
    return {e:c for e,c in out.items() if c}

def join(old,new,outer):
    parent={x:x for pair in old+new for x in pair}
    def find(x):
        while parent[x]!=x:parent[x]=parent[parent[x]];x=parent[x]
        return x
    for a,b in old+new:parent[find(a)]=find(b)
    groups=defaultdict(list)
    for x in parent:groups[find(x)]
    for x in outer:groups[find(x)].append(x)
    assert all(len(g) in (0,2) for g in groups.values())
    return tuple(sorted(tuple(sorted(g)) for g in groups.values() if g)),sum(not g for g in groups.values())

def writhe(pd):
    ports=defaultdict(list)
    for i,c in enumerate(pd):
        for j,x in enumerate(c):ports[x].append((i,j))
    assert all(len(p)==2 for p in ports.values())
    incoming=set();visited=set();components=0
    for start in ((i,j) for i in range(len(pd)) for j in range(4)):
        if start in visited:continue
        components+=1;p=start
        while p not in visited:
            i,j=p;incoming.add(p);visited.add(p)
            q=(i,(j+2)%4);visited.add(q)
            a,b=ports[pd[q[0]][q[1]]];p=b if a==q else a
    w=0
    for i in range(len(pd)):
        u=next(j for j in (0,2) if (i,j) in incoming)
        o=next(j for j in (1,3) if (i,j) in incoming)
        w += 1 if (o-u)%4==1 else -1
    # Standard PD Jones convention with our A-smoothing at (0,1),(2,3).
    return -w,components

def bracket(pd):
    states={():{0:1}};seen=Counter();maxstates=0;maxfront=0
    remaining=list(range(len(pd)));front=set()
    while remaining:
        # Fixed diagram data only: choose a small frontier, independent of states.
        i=min(remaining,key=lambda k:len(front.symmetric_difference(x for x,n in Counter(pd[k]).items() if n%2)))
        remaining.remove(i);c=pd[i];seen.update(c)
        front={x for x,n in seen.items() if n==1}
        maxfront=max(maxfront,len(front));out={}
        for old,p in states.items():
            for smoothing,shift in ((((c[0],c[1]),(c[2],c[3])),1),(((c[0],c[3]),(c[1],c[2])),-1)):
                key,nloops=join(old,smoothing,front);q=p
                for _ in range(nloops):q=delta(q)
                z=out.setdefault(key,defaultdict(int))
                for e,v in q.items():z[e+shift]+=v
        states={k:{e:v for e,v in p.items() if v} for k,p in out.items()}
        maxstates=max(maxstates,len(states))
    assert set(states)=={()}
    # This contraction gives delta for every circle; divide once.
    raw=states[()];low=min(raw)
    quotient,remainder=divide({e-low:c for e,c in raw.items()},{0:1,4:1})
    assert not remainder
    ans={e+low+2:-c for e,c in quotient.items()}
    return ans,maxstates,maxfront

def main():
    rows=json.loads((ROOT/'stoimenow_k3.json').read_text());report=[]
    for row in rows:
        pd=row['initial_PD'];w,n=writhe(pd)
        b,states,front=bracket(pd)
        v={e-3*w:c*(-1 if w%2 else 1) for e,c in b.items()}
        expected={-2*int(e):c for e,c in row['coefficients'].items() if c}
        direct=v==expected
        mirror={-e:c for e,c in v.items()}==expected
        assert direct or mirror,(row['flips'],w,row['writhe'],v)
        report.append({'flips':row['flips'],'independent_writhe':w,'components':n,'max_states':states,'max_frontier':front,'matches_direct':direct,'matches_mirror':mirror})
        print(report[-1],flush=True)
    V={int(e)//2:c for e,c in rows[0]['coefficients'].items() if c};V[0]-=1
    low=min(V);factor={e-low:c for e,c in V.items()};factors={}
    for name,p in [('t-1',{0:-1,1:1}),('t+1',{0:1,1:1}),('t²+t+1',{0:1,1:1,2:1}),('t²-t+1',{0:1,1:-1,2:1})]:
        n=0
        while True:
            q,r=divide(factor,p)
            if r:break
            factor=q;n+=1
        if n:factors[name]=n
    moments=[sum(c*(int(e)//2)**k for e,c in rows[0]['coefficients'].items())-(1 if k==0 else 0) for k in range(8)]
    out={'PD_checks':report,'V_minus_1_t_power':low,'V_minus_1_known_factors':factors,'remaining_factor':factor,'log_derivatives_at_1':moments}
    (ROOT/'homology_k3_bracket_audit.json').write_text(json.dumps(out,indent=2))
    print(json.dumps({k:v for k,v in out.items() if k!='PD_checks'},indent=2))

if __name__=='__main__':main()
