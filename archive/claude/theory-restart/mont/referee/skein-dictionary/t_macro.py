import sys, json
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/referee/skein-dictionary')
from refskein import *
gb=[B for B,_ in json.load(open('/Users/calebbarnett/jones-lanes/theory-restart/mont/general_boxes.json'))]
import random
rnd=random.Random(5)
ok=0;tot=0
for it in range(12):
    bs=rnd.sample(gb[:20],rnd.choice([1,2]))
    m=rnd.choice([-2,-1,1,2])
    word='r2.'+('y1.' if m>0 else 'x1.')*abs(m)+'.'.join(bs)+'.u1'
    direct=body_TL3(word)
    macro=tl3_necklace(m,tl3_product(*[body_TL3(b) for b in bs]))
    tot+=1; ok+= all(pclean(direct[k])==pclean(macro[k]) for k in TL3)
print('macro==direct',ok,'/',tot)
