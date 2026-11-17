"""Analyze kht++ quotient-tangle outputs (JSONL from tilt_2bridge.py or doubles.jsonl) for the TILT law."""
import json, sys, collections
def valid(khr):
    r=[c for c in khr if c['type']=='r']; s=[c for c in khr if c['type']=='s']
    if len(r)!=1: return False
    try: int(r[0]['slope'])
    except Exception: return False
    return all(c.get('slope')=='∞' for c in s)

def analyze(path):
    n=0; err=0; tilt_fail=[]; trivial=0; steps_min=collections.Counter(); steps_max=collections.Counter(); types=collections.Counter(); kvals=collections.Counter()
    nspec=collections.Counter(); width=collections.Counter(); cancel=0; gaps=collections.Counter(); notop=[]
    for l in open(path):
        try: r=json.loads(l)
        except Exception: continue
        if r.get('error') or 'khr' not in r: err+=1; continue
        if not valid(r['khr']): invalid=globals().get('invalid',0)+1; globals()['invalid']=invalid; continue
        n+=1
        sp=[(c['delta'],c['q']) for c in r['khr'] if c['type']=='s']
        for c in r['khr']:
            types[c['type']+c['len']+('(inf)' if c['slope']=='∞' else '(other)') if c['type']=='s' else 'r'+c['len']]+=1
            if c['type']=='r': kvals[c['slope']]+=1
        if not sp: trivial+=1; continue
        lev=collections.defaultdict(list)
        for d,q in sp: lev[d].append(q)
        ds=sorted(lev); nspec[len(sp)]+=1; width[len(ds)]+=1
        ok=True
        for i in range(len(ds)-1):
            gaps[ds[i+1]-ds[i]]+=1
            dmin=min(lev[ds[i+1]])-min(lev[ds[i]]); dmax=max(lev[ds[i+1]])-max(lev[ds[i]])
            steps_min[dmin]+=1; steps_max[dmax]+=1
            if not (dmin<0 and dmax<0): ok=False
        if not ok: tilt_fail.append((r.get('file') or r.get('knot'), [(d,min(lev[d]),max(lev[d]),len(lev[d])) for d in ds]))
        # cancelling pairs: same q-offset in levels of different parity
        byq=collections.defaultdict(set)
        for d,q in sp: byq[q].add(int(round(d))%2)
        if any(len(v)>1 for v in byq.values()): cancel+=1
    print(path)
    print("  tangles computed:",n," errors/timeouts:",err," with no special component:",trivial," invalid (unknot closure fails):",globals().get("invalid",0))
    print("  component types:",dict(types))
    print("  rational slopes k:",dict(sorted(kvals.items(), key=lambda kv: kv[0])))
    print("  number of delta-levels:",dict(sorted(width.items()))," max specials:",max(nspec) if nspec else 0)
    print("  delta gaps:",dict(gaps))
    print("  shift of window min per +1 delta:",sorted(steps_min.items()))
    print("  shift of window max per +1 delta:",sorted(steps_max.items()))
    print("  tangles with a cancelling pair (same q-offset, opposite parity):",cancel)
    print("  TILT failures:",len(tilt_fail))
    for t in tilt_fail[:10]: print("    ",t)
if __name__=='__main__':
    for p in sys.argv[1:]: analyze(p)
