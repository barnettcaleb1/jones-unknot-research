#include <array>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <vector>
#include <chrono>
#include <sstream>
#include "top_braid_tables.h"
using namespace std;
constexpr int MOD=1000000007;
using Vec=array<int,14>;
int crossing_coeff[6][14];
const int letters[6]={1,2,3,-1,-2,-3};
Vec apply_generator(const Vec& v,int letter){
 Vec u={};int g=abs(letters[letter])-1;
 int a=letter<3?2:500000004;
 for(int j=0;j<14;j++){
  u[j]=(u[j]+1LL*a*v[j])%MOD;
  int k=dest[g][j];u[k]=(u[k]+1LL*crossing_coeff[letter][j]*v[j])%MOD;
 }
 return u;
}
long long nodes=0,knots=0,hits_count=0;
int max_depth;
vector<int> path;
ofstream hits;
void dfs(const Vec& v,array<int,4> perm,int last,int depth){
 nodes++;
 int ix=perm[0]+4*perm[1]+16*perm[2]+64*perm[3];
 if(knot_permutation[ix]){
  knots++;long long a=0;
  for(int j=0;j<14;j++)a=(a+1LL*v[j]*close2[j])%MOD;
  if(a==0){
   hits_count++;hits<<depth<<" |";
   for(int s:path)hits<<' '<<s;
   hits<<'\n';
  }
 }
 if(depth==max_depth)return;
 for(int s=0;s<6;s++)if(last<0||letters[s]!=-letters[last]){
  int g=abs(letters[s])-1;auto np=perm;swap(np[g],np[g+1]);
  path.push_back(letters[s]);dfs(apply_generator(v,s),np,s,depth+1);path.pop_back();
 }
}
int main(int argc,char**argv){
 bool checking=argc>1 && string(argv[1])=="check";
 max_depth=argc>1&&!checking?stoi(argv[1]):10;
 for(int s=0;s<6;s++)for(int j=0;j<14;j++){
  long long b=s<3?500000004:2;
  if(loops[abs(letters[s])-1][j])b=b*delta%MOD;
  crossing_coeff[s][j]=b;
 }
 if(checking){
  string line;
  while(getline(cin,line)){
   Vec v;for(int j=0;j<14;j++)v[j]=initial[j];
   array<int,4> perm={0,1,2,3};istringstream in(line);int s;
   while(in>>s){int ix=s>0?s-1:2-s;v=apply_generator(v,ix);swap(perm[abs(s)-1],perm[abs(s)]);}
   long long a=0;for(int j=0;j<14;j++)a=(a+1LL*v[j]*close2[j])%MOD;
   int ix=perm[0]+4*perm[1]+16*perm[2]+64*perm[3];
   cout<<a<<' '<<knot_permutation[ix]<<'\n';
  }
  return 0;
 }
 hits.open("top_braid_hits.txt");auto start=chrono::steady_clock::now();
 Vec v;for(int j=0;j<14;j++)v[j]=initial[j];
 dfs(v,{0,1,2,3},-1,0);
 double sec=chrono::duration<double>(chrono::steady_clock::now()-start).count();
 ofstream stats("top_braid_counts.json");
 stats<<"{\"max_length\":"<<max_depth<<",\"freely_reduced_words\":"<<nodes
      <<",\"knot_closure_instances\":"<<knots<<",\"modular_zero_hits\":"<<hits_count
      <<",\"prime\":"<<MOD<<",\"A\":2,\"seconds\":"<<sec<<"}\n";
 cout<<"words "<<nodes<<" knot closures "<<knots<<" modular zeros "<<hits_count<<" seconds "<<sec<<endl;
}
