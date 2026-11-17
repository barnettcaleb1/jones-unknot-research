"""Finite-field rank witnesses for exact generic rank-six commutator defects."""
import json,pathlib
HERE=pathlib.Path(__file__).resolve().parent
PRIME=1000003

def rank_certificate(a):
    a=[x[:] for x in a];labels=list(range(len(a)));pivrows=[];pivcols=[];rank=0
    for col in range(len(a[0])):
        pivot=next((i for i in range(rank,len(a)) if a[i][col]),None)
        if pivot is None:continue
        a[rank],a[pivot]=a[pivot],a[rank];labels[rank],labels[pivot]=labels[pivot],labels[rank]
        pivrows.append(labels[rank]);pivcols.append(col)
        scale=pow(a[rank][col],-1,PRIME);a[rank]=[x*scale%PRIME for x in a[rank]]
        for i in range(rank+1,len(a)):
            f=a[i][col];a[i]=[(x-f*y)%PRIME for x,y in zip(a[i],a[rank])]
        rank+=1
    return rank,pivrows,pivcols

def determinant(a):
    a=[x[:] for x in a];det=1
    for col in range(len(a)):
        pivot=next((i for i in range(col,len(a)) if a[i][col]),None)
        if pivot is None:return 0
        if pivot!=col:a[pivot],a[col]=a[col],a[pivot];det=-det
        f=a[col][col];det=det*f%PRIME
        a[col]=[x*pow(f,-1,PRIME)%PRIME for x in a[col]]
        for i in range(col+1,len(a)):
            f=a[i][col];a[i]=[(x-f*y)%PRIME for x,y in zip(a[i],a[col])]
    return det%PRIME

def main():
    source=json.loads((HERE/'kernel_results.json').read_text());result=[]
    for item in source['results']:
        if item['n']!=6 or item['k']!=2:continue
        m=[[sum(c*pow(2,int(e),PRIME) for e,c in p.items())%PRIME for p in row] for row in item['matrix']]
        d=[[(m[i][j]-(i==j))%PRIME for j in range(9)] for i in range(9)]
        r,rows,cols=rank_certificate(d);assert r==6
        det=determinant([[d[i][j] for j in cols] for i in rows]);assert det
        result.append({'label':item['label'],'specialization_A':2,'prime':PRIME,'rank':r,'minor_rows_zero_based':rows,'minor_columns_zero_based':cols,'minor_determinant':det})
    (HERE/'kernel_structure.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))
if __name__=='__main__':main()
