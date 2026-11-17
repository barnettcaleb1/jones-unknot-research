import abstract as ab, json
out={}
for (no,nn) in [(3,0),(2,1),(1,2),(0,3)]:
    res=ab.all_diagrams(no,nn)
    for sh,vals in sorted(res.items()):
        assert len(vals)==1, (sh,vals)
        out['%s | %s'%(sh[0],''.join(map(str,sh[1])))]=vals.pop()
json.dump(out,open('w3_table.json','w'),indent=0)
nz={k:v for k,v in out.items() if v}
print('order-3 types:',len(out),' nonzero:',len(nz))
for k,v in sorted(nz.items(),key=lambda kv:(kv[0].count('o'),kv[0])): print('  ',k,'->',v)
