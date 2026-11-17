import sys, pickle, collections
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundD/lpgen')
tag=sys.argv[1]
U=pickle.load(open('uni_%s.pkl'%tag,'rb'))
S=U['S']; lab=[s[2] for s in S]
isD=[l.startswith('d2') for l in lab]
opn=[(k,info) for k,v,info in U['res'] if v=='open']
print(tag,'open cases',len(opn))
badD=collections.Counter(); 
for k,info in sorted(opn,key=str):
    pD=[lab[j] for j in info['part'] if isD[j]]; pT=sum(1 for j in info['part'] if not isD[j])
    uD=[lab[j] for j in info['unb'] if isD[j]]; uT=sum(1 for j in info['unb'] if not isD[j])
    for j in info['part']:
        if isD[j]: badD[lab[j]]+=1
    iso=None if info['isol'] is None else ({lab[j]:v for j,v in enumerate(info['isol'][0]) if v},info['isol'][1])
    print(k,'| partD',len(pD),pD[:6],'| partT',pT,'| unbD',uD[:6],'| unbT',uT,'| isol',iso)
print('d2 classes participating in some open case:',len(badD))
