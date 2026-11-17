# targeted search for configurations realizing the missing types (type computation only; cheap)
import sys, json, glob, itertools, random
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/ft/ident')
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont')
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/tools')
import chord, lp, flat_search as fs, enumtypes
want={m:{chord.dstr(t) for t in enumtypes.all_types(m)} for m in (1,2,3)}
have={1:set(),2:set(),3:set()}
for f in glob.glob('fast_m3_s*.json')+glob.glob('symtab_m3_*.json'):
    for r in json.load(open(f)): have[3].add(r['type'])
for f in glob.glob('symtab_m2_*.json'):
    for r in json.load(open(f)): have[2].add(r['type'])
missing={m:want[m]-have[m] for m in (2,3)}
missing[1]=set()
print('missing counts',{m:len(v) for m,v in missing.items()})
rnd=random.Random(int(sys.argv[1])); found={}
def gen2(rnd):
    # words with many windings: letters biased to x0/y0 and caps near the axis
    L=rnd.randint(6,18)
    a=[rnd.choice(['x0','y0','x1','y1','x2','y2']) for _ in range(rnd.randint(1,L//2))]
    b=[rnd.choice(['x0','y0','x1','y1','x2','y2','x3','y3','x4','y4']) for _ in range(rnd.randint(2,L//2+2))]
    c=[rnd.choice(['x0','y0','x1','y1','x2','y2']) for _ in range(rnd.randint(0,L//2))]
    return 's.'+rnd.choice(['l1','r1'])+'.'+'.'.join(a)+'.'+rnd.choice(['l1','r1','l2','r2','l3','r3'])+'.'+'.'.join(b)+'.'+rnd.choice(['u1','u2','u3'])+('.'+'.'.join(c) if c else '')+'.'+rnd.choice(['u1','u2'])
for it in range(int(sys.argv[2])):
    w=gen2(rnd) if it%2 else fs.gen(rnd,rnd.randint(8,20))
    if not w or lp.J(w) is None: continue
    toks=w.split('.')[1:]
    fl=[i for i,a in enumerate(toks) if a[0] in 'xy']
    for m in (2,3):
        if len(fl)<m: continue
        for _ in range(12):
            sites=sorted(rnd.sample(fl,m))
            d=chord.diagram(w,sites)
            if d is None: continue
            ty=chord.dstr(d)
            if ty in missing[m] and ty not in found: found[ty]=(w,sites)
print('found',len(found),'of',sum(len(v) for v in missing.values()))
json.dump(found,open('hunt_%s.json'%sys.argv[1],'w'))
still={m:sorted(missing[m]-set(found)) for m in (2,3)}
print('still missing:',still)
