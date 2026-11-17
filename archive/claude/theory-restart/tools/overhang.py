"""OVERHANG test. For Khr(T) = r_1(k) + specials s4(inf) at printed labels (c = q, d = delta):
 j = (q_r - k(|k|+2)/(|k|+1))/24; virtual string offsets 24j+4+8i (k>0, i<k/4) or 24j+4-8i (k<0, 1<=i<=|k|/4).
 k > 0: overhang = max actual offset - max virtual offset;  k < 0: overhang = min virtual offset - min actual offset.
 Also: is the extreme actual offset attained in a single delta-level (TILT consequence), and is P_tot nonzero."""
import json, sys, collections
def valid(khr):
    r=[c for c in khr if c['type']=='r']; s=[c for c in khr if c['type']=='s']
    if len(r)!=1: return False
    try: int(r[0]['slope'])
    except Exception: return False
    return all(c.get('slope')=='∞' for c in s)

def recs(path):
    for l in open(path):
        try: r=json.loads(l)
        except Exception: continue
        if r.get('error') or not r.get('khr'): continue
        if not valid(r['khr']): continue
        yield (r.get('file') or r.get('knot')), r['khr']
for path in sys.argv[1:]:
    over=collections.Counter(); n=0; bad=[]; single=0; multi=[]; k0=0; triv=0
    for name,khr in recs(path):
        r=[c for c in khr if c['type']=='r']; s=[c for c in khr if c['type']=='s']
        if len(r)!=1: continue
        k=int(r[0]['slope']); j=round((r[0]['q']-k*(abs(k)+2)/(abs(k)+1))/24.0)
        if not s:
            triv+=1; continue
        cs=[int(round(c['q'])) for c in s]
        lev=collections.defaultdict(list)
        for c in s: lev[int(round(c['delta']))].append(int(round(c['q'])))
        n+=1
        if k>0:
            vmax=24*j+4+8*(k//4-1); om=max(cs)-vmax; ext=max(cs)
        elif k<0:
            vmin=24*j+4-8*(abs(k)//4); om=vmin-min(cs); ext=min(cs)
        else:
            k0+=1; om=None; ext=max(cs)
        levels_with_ext=[d for d,v in lev.items() if ext in v]
        if len(levels_with_ext)==1: single+=1
        else: multi.append(name)
        if om is not None:
            over[om]+=1
            if om<=0: bad.append((name,k,j,om))
    print(path); print("  nontrivial tangles:",n," (k=0:",k0,") rational-only outputs skipped:",triv)
    print("  overhang distribution (k != 0):",sorted(over.items()))
    print("  overhang <= 0:",bad[:10])
    print("  extreme actual offset attained in one delta-level:",single,"of",n,"; exceptions:",multi[:5])
