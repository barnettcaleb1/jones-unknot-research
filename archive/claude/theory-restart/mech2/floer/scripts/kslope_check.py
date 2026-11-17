#!/usr/bin/env python3
"""Test: slope k of the rational component of Kh~(T) versus M1(K) := sum over HFK^ of (-1)^M M, tau, and the first delta-moment of N."""
import sys,json,os,signal,collections
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mech2/floer/scripts')
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/tools')
from hfk_word import pd_of_word
from gtilde import valid,jset
import spherogram
OUT='/Users/calebbarnett/jones-lanes/theory-restart/lit/kht/out/'
def word_of_kht(path):
    try: return open(path).read().split('\n')[1].strip()
    except Exception: return None
def hfk(word):
    pd=pd_of_word(word)
    if pd is None: return None
    K=spherogram.Link(pd)
    if len(K.link_components)!=1: return None
    K.simplify('basic')
    if len(K.crossings)==0: return dict(total_rank=1,seifert_genus=0,tau=0,ranks={(0,0):1})
    return K.knot_floer_homology()
class TO(Exception): pass
def handler(s,f): raise TO()
signal.signal(signal.SIGALRM,handler)
jobs=[]
for l in open(OUT+'k138/k138.jsonl'):
    r=json.loads(l); nm=r['file']; jobs.append(('k138:'+nm,word_of_kht(OUT+'k138/examples/si/'+nm.replace('^','-')+'.kht'),r))
for l in open(OUT+'tilt/run_3_45.jsonl'):
    r=json.loads(l); jobs.append(('tilt:'+os.path.basename(r['file']),word_of_kht(OUT+'tilt/'+r['file']),r))
for fn in ['comp/comp4.jsonl','comp/comp5.jsonl']:
    for l in open(OUT+fn):
        r=json.loads(l); jobs.append(('comp:'+r['file'],word_of_kht(OUT+'comp/examples/comp/'+r['file']+'.kht'),r))
for fn in ['rand/probe.jsonl','rand/rand2.jsonl','alex1/runs.jsonl','alex1/runsB.jsonl','alex1/runs2b.jsonl']:
    for l in open(OUT+fn):
        try: r=json.loads(l)
        except: continue
        jobs.append((fn.split('/')[0]+':'+r.get('file',''),r.get('word'),r))
rows=[]; seen=set()
for name,word,r in jobs:
    khr=r.get('khr') or []
    if not khr or word is None or not word.startswith('s.') or not valid(khr): continue
    if word in seen: continue
    seen.add(word)
    js=jset(khr)
    if js is None: continue
    k,j,pts=js
    q0,d0=pts[0]
    mom=sum((-1)**((d-d0)%2)*(d-d0) for q,d in pts)   # first delta-moment of N relative to rho
    try:
        signal.alarm(60); h=hfk(word); signal.alarm(0)
    except Exception as e:
        signal.alarm(0); continue
    if h is None: continue
    M1=sum((-1)**(M%2)*M*rk for (A,M),rk in h['ranks'].items())
    thin=len(set(A-M for (A,M) in h['ranks']))==1
    rows.append(dict(name=name,k=k,j=j,dimN=len(pts),rk=h['total_rank'],tau=h['tau'],g=h['seifert_genus'],M1=M1,mom=mom,thin=thin))
json.dump(rows,open('/Users/calebbarnett/jones-lanes/theory-restart/mech2/floer/scripts/kslope_check.json','w'))
c=collections.Counter()
for x in rows:
    a=(x['k']==4*x['M1'], x['k']==-4*x['M1'], x['k']==4*x['tau'], x['k']==-4*x['tau'], x['k']==4*x['mom'], x['k']==-4*x['mom'])
    c['n']+=1
    for i,nm in enumerate(['k=4M1','k=-4M1','k=4tau','k=-4tau','k=4mom','k=-4mom']):
        if a[i]: c[nm]+=1
    if x['M1']==0 and x['k']==0: c['both0']+=1
print(dict(c))
print('thick knots:',[(x['name'],x['k'],x['M1'],x['tau'],x['dimN'],x['rk']) for x in rows if not x['thin']][:40])
print('failures of |k|=4|M1|:',[(x['name'],x['k'],x['M1'],x['tau'],x['dimN'],x['rk']) for x in rows if abs(x['k'])!=4*abs(x['M1'])])
print('sign pattern k vs M1 (nonzero):',collections.Counter((1 if x['k']*x['M1']>0 else -1) for x in rows if x['k']*x['M1']!=0))
print('M1 != +-tau cases:',[(x['name'],x['k'],x['M1'],x['tau']) for x in rows if abs(x['M1'])!=abs(x['tau'])][:30])
