#include <algorithm>
#include <chrono>
#include <fstream>
#include <iostream>
#include <vector>
#include <cstring>
using namespace std;
#include "config.h"
int main(){
 auto start=chrono::steady_clock::now();
 long long count=0, row=0, jet3=0,jet4=0,jet5=0,full=0;
 int s[7]={1,1,1,1,-1,-1,-1};
 long long fall[40][6];
 for(int e=0;e<40;e++){fall[e][0]=1;for(int k=1;k<6;k++)fall[e][k]=fall[e][k-1]*(e-k+1);}
 ofstream hits("work/try8/quiver/hits.txt");
 ofstream finalists("work/try8/quiver/finalists.txt");
 for(int a=0;a<NR;a++){
  int C[7][7]={0},zbase[7]={0};
  for(int i=4;i<7;i++)C[i][i]=1;
  for(int k=0;k<9;k++){int i=se[k][0],j=se[k][1],v=reps[a][k];C[i][j]=C[j][i]=v;zbase[i]+=s[j]*v;zbase[j]+=s[i]*v;}
  int op[12]={0,0,0,0,0,0,1,1,4,7,10,10};
  do{
   count++;
   int z[7];copy(zbase,zbase+7,z);
   for(int k=0;k<12;k++){int i=oe[k][0],j=oe[k][1],v=op[k];C[i][j]=C[j][i]=v;z[i]-=v;z[j]+=v;}
   int score=0;for(int i=0;i<7;i++)score+=s[i]*z[i]*z[i];
   if(score)continue;row++;
   long long P[40]={0};
   for(int i=0;i<7;i++)P[3*C[i][i]]+=s[i];
   for(int i=0;i<7;i++)for(int j=0;j<7;j++)if(i!=j){int e=C[i][i]+2*C[i][j];for(int k=0;k<3;k++)P[e+k]+=s[j];}
   for(int i=0;i<7;i++)for(int j=i+1;j<7;j++)for(int k=j+1;k<7;k++){
    int e=C[i][j]+C[i][k]+C[j][k],v=s[i]*s[j]*s[k];P[e]+=v;P[e+1]+=2*v;P[e+2]+=2*v;P[e+3]+=v;
   }
   long long d3=0;for(int e=0;e<40;e++)d3+=P[e]*fall[e][3];if(d3)continue;jet3++;
   long long d4=0;for(int e=0;e<40;e++)d4+=P[e]*fall[e][4];if(d4!=4320)continue;jet4++;
   long long d5=0;for(int e=0;e<40;e++)d5+=P[e]*fall[e][5];finalists<<"FINALIST "<<jet4<<" D5 "<<d5<<"\n";for(int i=0;i<7;i++){for(int j=0;j<7;j++)finalists<<C[i][j]<<' ';finalists<<'\n';}
   if(d5!=86400)continue;jet5++;
   long long R[42]={0};for(int e=0;e<40;e++){R[e]-=expect[e];R[e+2]+=P[e];}
   for(int e=41;e>=24;e--){long long v=R[e];for(int j=0;j<=24;j++)R[e-24+j]-=v*divisor[j];}
   bool good=true;for(int e=0;e<24;e++)if(R[e])good=false;
   if(!good)continue;full++;
   hits<<"CANDIDATE "<<full<<"\n";for(int i=0;i<7;i++){for(int j=0;j<7;j++)hits<<C[i][j]<<' ';hits<<'\n';}hits.flush();
  }while(next_permutation(op,op+12));
  if(chrono::duration<double>(chrono::steady_clock::now()-start).count()>110){cerr<<"TIME LIMIT at rep "<<a<<"\n";break;}
 }
 double sec=chrono::duration<double>(chrono::steady_clock::now()-start).count();
 ofstream out("work/try8/quiver/search_result.json");
 out<<"{\"assignments\":"<<count<<",\"total\":"<<NR*166320LL<<",\"row_square_zero\":"<<row<<",\"third_derivative_zero\":"<<jet3<<",\"fourth_derivative_correct\":"<<jet4<<",\"fifth_derivative_correct\":"<<jet5<<",\"full_H4_Habiro\":"<<full<<",\"seconds\":"<<sec<<"}\n";
 cout<<"assignments "<<count<<" row "<<row<<" third "<<jet3<<" fourth "<<jet4<<" fifth "<<jet5<<" full "<<full<<" seconds "<<sec<<'\n';
}
