import sys, json, collections
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mech/floer/scripts')
from load import load138
LIT='/Users/calebbarnett/jones-lanes/theory-restart/lit/kht/out/'
def specials_of(r):
    return sorted((int(c['q']), int(c['delta'])) for c in r['khr'] if c['type']=='s')
sets = {}
sets['k138'] = [(r['name'], r['specials'], r['k'], r['j']) for r in load138()]
for key, fn in [('2bridge','tilt/run_3_45.jsonl'),('doubles','dbl/doubles.jsonl'),('comp5','comp/comp5.jsonl')]:
    L=[]
    for l in open(LIT+fn):
        r=json.loads(l)
        if 'khr' not in r: continue
        rat=[c for c in r['khr'] if c['type']=='r'][0]
        k=int(rat['slope']); j=round((rat['q']-k*(abs(k)+2)/(abs(k)+1))/24)
        sp=specials_of(r)
        if sp: L.append(((r.get('file') or r.get('knot')).split('/')[-1], sp, k, j))
    sets[key]=L
for key, L in sets.items():
    hist = collections.Counter(); hist_s = collections.defaultdict(collections.Counter)
    worst=[]
    for name, sp, k, j in L:
        for s in (2,4,6,8):
            e=[c+s*d for c,d in sp]
            hist_s[s][max(e)-min(e)] += 1
        e=[c+6*d for c,d in sp]
        w=max(e)-min(e)
        worst.append((w,name,len(sp)))
    print('==',key,len(L),'records')
    for s in (2,4,6,8):
        print('   width of c+%d*d :'%s, dict(sorted(hist_s[s].items())))
    worst.sort(reverse=True)
    print('   widest (c+6d):', worst[:6])
