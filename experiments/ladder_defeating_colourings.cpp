// Given k and a family of gap sets (one per line on stdin, gaps separated by spaces, empty line allowed),
// list deficit<=3 colourings (as classes of edges) that have a rainbow perfect matching but defeat the family.
// Edges: rung c -> c ; upper rail g -> k+g ; lower rail g -> 2k-1+g.   Requires 3k-2 <= 64.
#include <bits/stdc++.h>
using namespace std; typedef unsigned long long u64;
int k,m; vector<u64> allM; vector<u64> T; int nt; unsigned FULL;
u64 mk(const vector<int>&J){ u64 x=0; vector<char> cov(k,0); for(int g:J){cov[g]=cov[g+1]=1; x|=1ULL<<(k+g); x|=1ULL<<(2*k-1+g);} for(int c=0;c<k;c++) if(!cov[c]) x|=1ULL<<c; return x; }
bool witness(const vector<u64>&cls){ for(u64 M:allM){ bool ok=true; for(u64 c:cls) if(__builtin_popcountll(M&c)>1){ok=false;break;} if(ok) return true;} return false; }
long long found=0, limit; unsigned long long seen=0; int stride;
void emit(const vector<u64>&cls){ if(!witness(cls)) return; seen++; if(seen%stride) return; if(found>=limit) return; found++; for(u64 c:cls){ for(int e=0;e<m;e++) if(c>>e&1) printf("%d ",e); printf("| "); } puts(""); }
int main(int argc,char**argv){ k=atoi(argv[1]); limit=atoll(argv[2]); stride=argc>3?atoi(argv[3]):1; m=3*k-2;
  for(int s=0;s<(1<<(k-1));s++){ if(s&(s>>1)) continue; vector<int> J; for(int g=0;g<k-1;g++) if(s>>g&1) J.push_back(g); allM.push_back(mk(J)); }
  string line; while(getline(cin,line)){ istringstream is(line); vector<int> J; int g; while(is>>g) J.push_back(g); T.push_back(mk(J)); }
  nt=T.size(); FULL=(1u<<nt)-1;
  // useful pairs
  vector<array<int,2>> P; vector<unsigned> pd; vector<u64> pm;
  vector<vector<unsigned>> PD(m, vector<unsigned>(m,0));
  for(int a=0;a<m;a++) for(int b=a+1;b<m;b++){ unsigned d=0; for(int t=0;t<nt;t++) if((T[t]>>a&1)&&(T[t]>>b&1)) d|=1u<<t; PD[a][b]=PD[b][a]=d; if(d){ P.push_back({a,b}); pd.push_back(d); pm.push_back((1ULL<<a)|(1ULL<<b)); } }
  int np=P.size(); unsigned long long total=0;
  for(int i=0;i<np;i++) if(pd[i]==FULL){ total++; emit({pm[i]}); }
  // shape: up to three disjoint pairs
  for(int i=0;i<np;i++) for(int j=i+1;j<np;j++){ if(pm[i]&pm[j]) continue; unsigned d2=pd[i]|pd[j]; if(d2==FULL){ total++; emit({pm[i],pm[j]}); continue; }
    for(int l=j+1;l<np;l++){ if((pd[l]|d2)!=FULL) continue; if(pm[l]&(pm[i]|pm[j])) continue; total++; emit({pm[i],pm[j],pm[l]}); } }
  // shape: triple class (+ optional disjoint pair)
  for(int a=0;a<m;a++) for(int b=a+1;b<m;b++) for(int c=b+1;c<m;c++){ unsigned d3=PD[a][b]|PD[a][c]|PD[b][c]; u64 cm=(1ULL<<a)|(1ULL<<b)|(1ULL<<c);
    if(d3==FULL){ total++; emit({cm}); continue; }
    if(d3) for(int l=0;l<np;l++){ if((pd[l]|d3)!=FULL) continue; if(pm[l]&cm) continue; total++; emit({cm,pm[l]}); }
    for(int e=c+1;e<m;e++){ unsigned d4=d3|PD[a][e]|PD[b][e]|PD[c][e]; if(d4==FULL){ total++; emit({cm|(1ULL<<e)}); } } }
  fprintf(stderr,"k=%d tests=%d killing_colourings=%llu with_witness=%llu emitted=%lld\n",k,nt,total,seen,found);
}
