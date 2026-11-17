#include <array>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <random>
#include <string>
#include <vector>
#include "tables.h"
using namespace std;
constexpr int P=1000003, A=2;
int power(int a,int e){ if(e<0) e=(P-1)+e%(P-1); long long r=1,b=a; while(e){if(e&1)r=r*b%P;b=b*b%P;e>>=1;}return r; }
const int Ai=power(A,-1),d=(2*P-1LL*A*A-1LL*Ai*Ai%P)%P;
bool knot(const vector<int>&w){array<int,4> p={0,1,2,3}; for(int s:w)swap(p[abs(s)-1],p[abs(s)]); int q=p[0],c=1;while(q!=0){++c;q=p[q];}return c==4;}
int bracket(const vector<int>&w){
 array<int,14> v={};v[identity]=1;
 for(int s:w){array<int,14> u={};int g=abs(s)-1,a=s>0?A:Ai,b=s>0?Ai:A;
  for(int j=0;j<14;++j){u[j]=(u[j]+1LL*a*v[j])%P;long long z=1LL*b*v[j]%P;if(lp[g][j])z=z*d%P;u[dest[g][j]]=(u[dest[g][j]]+z)%P;}v=u;
 }
 long long r=0;for(int j=0;j<14;++j)r=(r+1LL*v[j]*power(d,loops[j]-1))%P;return r;
}
int target(const vector<int>&w){int wr=0;for(int s:w)wr+=s>0?1:-1;return power(P-A,3*wr);}
void wordout(ostream&out,const vector<int>&w){for(int s:w)out<<s<<' ';out<<'\n';}
int main(int argc,char**argv){
 int per=argc>1?stoi(argv[1]):10000;uint64_t seed=20261031;mt19937_64 rng(seed);
 ofstream hits("modular_hits.txt"),checks("modular_checks.txt"),report("search_counts.json");
 report<<"{\"seed\":"<<seed<<",\"prime\":"<<P<<",\"A\":"<<A<<",\"freely_reduced\":true,\"lengths\":[\n";
 int idx=0;for(int length:{27,31,35,39}){long long knots=0,passes=0;
  for(int z=0;z<per;++z){vector<int>w;for(int k=0;k<length;++k){int s;do{s=int(rng()%6);s=s<3?s+1:2-s;}while(k>0&&s==-w.back());w.push_back(s);}
   if(!knot(w))continue;++knots;int b=bracket(w);
   if(z<50){checks<<b<<' ';wordout(checks,w);}
   if(b==target(w)){++passes;wordout(hits,w);}
  }
  if(idx++)report<<",\n";report<<"{\"length\":"<<length<<",\"generated\":"<<per<<",\"knots\":"<<knots<<",\"modular_hits\":"<<passes<<"}";
  cout<<length<<" generated="<<per<<" knots="<<knots<<" modular_hits="<<passes<<'\n';
 }report<<"\n]}\n";
}
