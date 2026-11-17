"""Per dangerous class: V(B) at order 2 (C1 gen2.proveV, n >= 1) -- which vertical cases stay open; combined with hb_o3 (H at order 3)."""
import sys, pickle, collections
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineC1')
import gen2
H=pickle.load(open('hb_o3.pkl','rb')); Hc=set(H['closed'])
O=pickle.load(open('o3h.pkl','rb'))
keys=sorted(set(r[0][0] for r in O['res']),key=str)
st=collections.Counter(); why=collections.Counter(); both=0
for key in keys:
    ok,opn=gen2.proveV({'top':key[0],'bot':key[1]},key[2],key[3],1)
    st['V-closed@2' if ok else 'V-open@2']+=1
    if ok and key in Hc: both+=1
    for o in opn: why[o if isinstance(o,str) else o[3]]+=1
print('dangerous classes',len(keys),dict(st),'| H-closed@3 AND V-closed@2:',both)
for k,v in why.most_common(8): print('   V open case:',k,v)
