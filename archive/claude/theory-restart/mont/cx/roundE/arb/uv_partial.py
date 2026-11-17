"""analyse the (possibly partial) o3_uv_n4.pkl: classes whose subclasses are ALL processed -> V3(B) closed or open."""
import pickle, collections
K=pickle.load(open('gen1k3u_R4_n4.pkl','rb'))
r=pickle.load(open('o3_uv_n4.pkl','rb'))
res=r['res'] if isinstance(r,dict) else r
done=collections.defaultdict(list)
for key,d3,o in res: done[key].append(o)
full=[k for k in done if len(done[k])==len(K[k])]
closed=[k for k in full if all(not o for o in done[k])]
H=pickle.load(open('o3_u_n4.pkl','rb')); Hc=set(H['Hc'])
print('subclasses processed',len(res),'of',sum(len(v) for v in K.values()),'| classes fully processed',len(full),'of',len(K),
      '| V3(B) closed',len(closed),'| H3 and V3 both',len([k for k in closed if k in Hc]))
