// Minimal survivor sets for deficit D on an abstract system: m edges, a list of "matchings" (edge sets).
// Input (stdin): m n, then n lines: size e1 e2 ...   Output: n, then minimal survivor sets as index lists.
#include <bits/stdc++.h>
using namespace std;
const int W=2048; typedef bitset<W> B;
int m,D,nm; vector<B> inc; struct H{size_t operator()(const B&b)const{return hash<B>()(b);}};
unordered_set<B,H> masks; unsigned long long nodes=0;
void rec(int e,int def,const B&alive,vector<B>&bm){
  if(alive.none()) return; nodes++;
  if(e==m){ if(def==D) masks.insert(alive); return; }
  bm.push_back(inc[e]); rec(e+1,def,alive,bm); bm.pop_back();
  if(def<D) for(size_t b=0;b<bm.size();b++){ B old=bm[b]; B na=alive&~(old&inc[e]); if(na.none()) continue; bm[b]=old|inc[e]; rec(e+1,def+1,na,bm); bm[b]=old; }
}
int main(int argc,char**argv){ D=atoi(argv[1]); if(scanf("%d %d",&m,&nm)!=2) return 1; inc.assign(m,B());
  for(int j=0;j<nm;j++){ int s; if(scanf("%d",&s)!=1) return 1; while(s--){ int e; if(scanf("%d",&e)!=1) return 1; inc[e][j]=1; } }
  B all; for(int j=0;j<nm;j++) all[j]=1; vector<B> bm; rec(0,0,all,bm);
  vector<B> v(masks.begin(),masks.end()); sort(v.begin(),v.end(),[](const B&a,const B&b){return a.count()<b.count();});
  vector<B> mn; for(auto&x:v){ bool ok=true; for(auto&y:mn) if((y&x)==y){ok=false;break;} if(ok) mn.push_back(x);} 
  fprintf(stderr,"m=%d matchings=%d nodes=%llu distinct=%zu minimal=%zu smallest=%zu\n",m,nm,nodes,v.size(),mn.size(),mn[0].count());
  printf("%d\n",nm); for(auto&x:mn){ for(int j=0;j<nm;j++) if(x[j]) printf("%d ",j); puts(""); }
}
