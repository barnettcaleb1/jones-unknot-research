# Referee: symbol(v3) per labelled order-3 type from the upstairs lift (sum over one lift per site of the v3 weight
# system: P3 -> 1, K3 -> 2, else 0); compare with exact Delta^3 v3 on random words and with builder's iota_table.txt.
import sys, itertools, json, random, re
from fractions import Fraction as Fr
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/ft/referee/proofref')
import ss
from abstract_ref import shapes, realize
from rel_ref import lift, cross
def v3w(chords):
    e=sum(1 for i in range(3) for j in range(i+1,3) if cross(chords[i],chords[j]))
    if e==3: return 2
    if e==2: return 1
    return 0
def v3_symbol(slots):
    ch,pairs=lift(slots)
    tot=0
    for pick in itertools.product(*[list(pr) for pr in pairs]):
        tot+=v3w([ch[i] for i in pick])
    return tot
def type_key(slots):
    axis=set(p for p,tk in enumerate(slots) if tk in ('o','g')); pos={}
    for p,tk in enumerate(slots):
        if tk.startswith('c'): pos.setdefault(tk,[]).append(p)
    seq=[tk for tk in slots if tk!='g']
    labs=''.join(str(sum(1 for p in axis if pos[c][0]<p<pos[c][1])%2) for c in sorted(pos))
    return '%s | %s'%(' '.join(seq),labs)
W3=json.load(open('table_m3.json'))
mine={}
for nc in range(3,-1,-1):
    for seq in shapes(nc,3-nc):
        for gpat in itertools.product([0,1],repeat=len(seq)-1):
            sl=realize(seq,gpat); k=type_key(sl); v=v3_symbol(sl)
            if k in mine and mine[k]!=v: print('v3 symbol not label-determined!',k)
            mine[k]=v
# builder table
b={}
for line in open('/Users/calebbarnett/jones-lanes/theory-restart/mont/ft/proof/iota_table.txt'):
    m=re.match(r'\s+((?:c\d|o)(?: (?:c\d|o))*)\s+(\d*)\s+W3=\s*(-?\d+)\s+Delta3 v3=\s*(-?\d+)\s+Delta3 iota=\s*(-?\d+)',line)
    if m: b['%s | %s'%(m.group(1),m.group(2))]=(int(m.group(3)),int(m.group(4)),int(m.group(5)))
print('builder rows parsed:',len(b),'  my types:',len(mine))
diffs=[(k,b[k],W3[k],mine[k]) for k in b if (W3[k]!=[b[k][0]] or mine[k]!=b[k][1])]
print('rows where my W3 or my v3-symbol differ from builder:',len(diffs),diffs[:5])
# rows not listed by builder: are they all W3=0 and v3=0?
unl=[k for k in mine if k not in b]; print('types not in builder iota table:',len(unl),' nonzero among them:',[ (k,W3[k],mine[k]) for k in unl if W3[k]!=[0] or mine[k]!=0][:5])
ints=0; supp={}
for k in mine:
    w=W3[k][0]; v=mine[k]; io=(Fr(w,6)-7*v)/5
    ints+=(io.denominator!=1)
    d=(Fr(w)-72*v)/30
    if d!=0: supp.setdefault(d,[]).append(k)
print('non-integral iota symbols:',ints)
for d,ks in sorted(supp.items()): print('iota - v3 =',d,':',len(ks),'types:',sorted(set(re.sub(r'\| .*','',x) for x in ks)))
json.dump(mine,open('v3sym_m3.json','w'),indent=0)
