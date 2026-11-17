#include <array>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <vector>
#include <chrono>
#include "tables.h"
using namespace std;
constexpr int P=1000003,A=2;
int power(int a,int e){if(e<0)e=(P-1)+e%(P-1);long long r=1,b=a;while(e){if(e&1)r=r*b%P;b=b*b%P;e>>=1;}return r;}
const int AI=power(A,-1),D=(2*P-1LL*A*A-1LL*AI*AI%P)%P;
using Vec=array<int,14>;
Vec gen(Vec v,int s){Vec u={};int g=abs(s)-1,a=s>0?A:AI,b=s>0?AI:A;
 for(int j=0;j<14;j++){u[j]=(u[j]+1LL*a*v[j])%P;long long z=1LL*b*v[j]%P;if(lp[g][j])z=z*D%P;u[dest[g][j]]=(u[dest[g][j]]+z)%P;}return u;}
Vec applyword(Vec v,const vector<int>&w){for(int s:w)v=gen(v,s);return v;}
int closev(Vec v){long long r=0;for(int j=0;j<14;j++)r=(r+1LL*v[j]*power(D,loops[j]-1))%P;return r;}
vector<int> inv(vector<int>w){vector<int>r;for(auto i=w.rbegin();i!=w.rend();++i)r.push_back(-*i);return r;}
array<vector<int>,4> blocks;
array<vector<int>,6> seeds;
array<Vec,6> functionals;
array<array<int,4>,6> seedperm;
vector<int> path;
ofstream hits,checks;
long long nodes=0,knotcases=0,candidates=0;
int depthmax,target;
void outword(ostream&out,const vector<int>&w){for(int s:w)out<<s<<' ';out<<'\n';}
void dfs(const Vec&v,array<int,4>perm,int depth,int last){
 nodes++;
 for(int j=0;j<6;j++){
  array<int,4>p;for(int i=0;i<4;i++)p[i]=perm[seedperm[j][i]];
  int q=p[0],cyc=1;while(q!=0){q=p[q];cyc++;}if(cyc!=4)continue;
  knotcases++;long long z=0;for(int i=0;i<14;i++)z=(z+1LL*v[i]*functionals[j][i])%P;
  if(nodes<15 || nodes%1000003==0 || z==target){vector<int>w;for(int b:path)w.insert(w.end(),blocks[b].begin(),blocks[b].end());w.insert(w.end(),seeds[j].begin(),seeds[j].end());
   if(nodes<15 || nodes%1000003==0){checks<<z<<' ';outword(checks,w);}
   if(z==target){candidates++;hits<<j<<' '<<depth<<' ';for(int b:path)hits<<b<<' ';hits<<"| ";outword(hits,w);}
  }
 }
 if(depth==depthmax)return;
 for(int b=0;b<4;b++)if(last<0||b!=(last^2)){
  auto p=perm;for(int s:blocks[b])swap(p[abs(s)-1],p[abs(s)]);
  path.push_back(b);dfs(applyword(v,blocks[b]),p,depth+1,b);path.pop_back();
 }
}
int main(int argc,char**argv){
 depthmax=argc>1?stoi(argv[1]):12;blocks[0]={1,-3};blocks[1]={2,1,-3,-2};blocks[2]=inv(blocks[0]);blocks[3]=inv(blocks[1]);
 int pars[6][4]={{-5,2,6,2},{-2,-1,1,7},{-2,-1,3,5},{-2,2,3,2},{-1,1,2,3},{-2,2,1,4}};
 for(int j=0;j<6;j++){
  for(int k=0;k<4;k++)for(int i=0;i<abs(pars[j][k]);i++)seeds[j].push_back((k%2+1)*(pars[j][k]>0?1:-1));
  seedperm[j]={0,1,2,3};for(int s:seeds[j])swap(seedperm[j][abs(s)-1],seedperm[j][abs(s)]);
  for(int i=0;i<14;i++){Vec v={};v[i]=1;functionals[j][i]=closev(applyword(v,seeds[j]));}
 }
 target=power(P-A,15);hits.open("coset_modular_hits.txt");checks.open("coset_modular_checks.txt");
 Vec initial={};initial[identity]=1;auto start=chrono::steady_clock::now();dfs(initial,{0,1,2,3},0,-1);
 double sec=chrono::duration<double>(chrono::steady_clock::now()-start).count();
 ofstream report("coset_counts.json");report<<"{\"depth\":"<<depthmax<<",\"kernel_words\":"<<nodes<<",\"knot_closures\":"<<knotcases<<",\"modular_candidates\":"<<candidates<<",\"prime\":"<<P<<",\"A\":"<<A<<",\"seconds\":"<<sec<<"}\n";
 cout<<"Kernel words="<<nodes<<" knot closures="<<knotcases<<" modular candidates="<<candidates<<" seconds="<<sec<<endl;
}
