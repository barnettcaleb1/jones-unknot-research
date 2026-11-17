import json,sys,os,collections,glob
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/tools')
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mech2/dictionary')
import rec
from gtilde import jset,valid
O='/Users/calebbarnett/jones-lanes/theory-restart/lit/kht/out'
def chainfile(folder):
    c=glob.glob(os.path.join(folder,'cxBNr-c2-*'))
    return c[0] if c else None
def run(jsonl,folderfn,label):
    offs=collections.Counter(); n=0; seen=set(); res=[]
    for line in open(jsonl):
        try: r=json.loads(line)
        except: continue
        khr=r.get('khr') or []
        if not khr or not valid(khr): continue
        f=chainfile(folderfn(r))
        if not f: continue
        lines=[l.rstrip('\n') for l in open(f) if not l.startswith('%')]
        try: a=rec.analyse_chains(lines,khr)
        except Exception as e:
            print('ERR',r.get('knot') or r.get('file'),repr(e)[:80]); continue
        key=(a['k'],a['j'],tuple(sorted(a['L'])))
        if key in seen: continue
        seen.add(key); n+=1
        sq=a['squares']
        for (x,b) in sq:
            for (x2,b2) in sq:
                if b2==b+1: offs[x2-x]+=1
        res.append(dict(name=r.get('knot') or r.get('file'),k=a['k'],j=a['j'],path=a['path'],squares=sq,odd=a['odd'],dim=len(a['L']),L=a['L']))
    print(label,'distinct tangles',n,'square a-offsets on adjacent levels:',sorted(offs.items()))
    return res
if __name__=='__main__':
    R1=run(O+'/dbl/doubles.jsonl',lambda r:O+'/dbl/examples/knots/2-bridge_knots/'+r['knot'],'doubles')
    R2=run(O+'/tilt/run_3_45.jsonl',lambda r:O+'/tilt/'+r['file'][:-4],'two-bridge')
    json.dump(dict(doubles=R1,twobridge=R2),open('more.json','w'))
