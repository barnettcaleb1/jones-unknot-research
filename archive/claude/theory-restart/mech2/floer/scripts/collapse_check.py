#!/usr/bin/env python3
"""Compare dim N(T) = 1 + 2*(number of specials) with rank HFK^(K), K computed from the half-diagram word (spherogram + knot_floer_homology).
Reads .kht words; matches with jsonl records. Cheap check of collapse of the spectral sequence of THEOREM S."""
import sys,json,os,glob,signal,collections
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mech2/floer/scripts')
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/tools')
from hfk_word import pd_of_word
from gtilde import valid
import spherogram
OUT='/Users/calebbarnett/jones-lanes/theory-restart/lit/kht/out/'
def word_of_kht(path):
    try:
        L=open(path).read().split('\n')
        return L[1].strip()
    except Exception: return None
def hfk(word):
    pd=pd_of_word(word)
    if pd is None: return None
    K=spherogram.Link(pd)
    if len(K.link_components)!=1: return None
    K.simplify('basic')
    if len(K.crossings)==0: return dict(total_rank=1,seifert_genus=0,tau=0,ranks={(0,0):1})
    h=K.knot_floer_homology()
    return h
class TO(Exception): pass
def handler(s,f): raise TO()
signal.signal(signal.SIGALRM,handler)
jobs=[]
# k138: file names like 4_1^1 -> examples/si/4_1-1.kht
for l in open(OUT+'k138/k138.jsonl'):
    r=json.loads(l); nm=r['file']; p=OUT+'k138/examples/si/'+nm.replace('^','-')+'.kht'
    jobs.append(('k138:'+nm,word_of_kht(p),r))
for l in open(OUT+'tilt/run_3_45.jsonl'):
    r=json.loads(l); p=OUT+'tilt/'+r['file']
    jobs.append(('tilt:'+os.path.basename(r['file']),word_of_kht(p),r))
for fn in ['comp/comp4.jsonl','comp/comp5.jsonl']:
    for l in open(OUT+fn):
        r=json.loads(l); p=OUT+'comp/examples/comp/'+r['file']+'.kht'
        jobs.append(('comp:'+r['file'],word_of_kht(p),r))
for fn in ['rand/probe.jsonl','rand/rand2.jsonl','alex1/runs.jsonl','alex1/runsB.jsonl','alex1/runs2b.jsonl']:
    for l in open(OUT+fn):
        try: r=json.loads(l)
        except: continue
        jobs.append((fn.split('/')[0]+':'+r.get('file',''),r.get('word'),r))
res=[]; seen=set()
for name,word,r in jobs:
    khr=r.get('khr') or []
    if not khr or word is None: continue
    if not word.startswith('s.'): continue
    if (name.split(':')[0],word) in seen: continue
    seen.add((name.split(':')[0],word))
    ok=valid(khr)
    m=sum(1 for c in khr if c['type']=='s')
    lens=set(c['len'] for c in khr if c['type']=='s')
    dimN=1+2*m if lens<= {'4'} else None
    try:
        signal.alarm(60)
        h=hfk(word)
        signal.alarm(0)
    except TO:
        res.append((name,word,dimN,'timeout',None,None,ok)); continue
    except Exception as e:
        signal.alarm(0)
        res.append((name,word,dimN,'err:'+str(e)[:40],None,None,ok)); continue
    if h is None:
        res.append((name,word,dimN,'notknot',None,None,ok)); continue
    res.append((name,word,dimN,h['total_rank'],h['seifert_genus'],h['tau'],ok))
with open('/Users/calebbarnett/jones-lanes/theory-restart/mech2/floer/scripts/collapse_check.tsv','w') as f:
    for x in res: f.write('\t'.join(str(y) for y in x)+'\n')
cnt=collections.Counter()
for name,word,dimN,rk,g,tau,ok in res:
    if not isinstance(rk,int): cnt['nocomp:'+str(rk)[:12]]+=1; continue
    if dimN is None: cnt['nonstandard']+=1; continue
    cnt['equal' if dimN==rk else ('N>HFK' if dimN>rk else 'N<HFK !!')]+=1
print(dict(cnt))
for name,word,dimN,rk,g,tau,ok in res:
    if isinstance(rk,int) and dimN is not None and dimN!=rk: print('DIFF',name,word,'dimN',dimN,'HFK',rk,'g',g,'tau',tau,'valid',ok)
