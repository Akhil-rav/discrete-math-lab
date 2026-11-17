// Exact minimum test-family size h_d(k) for the ladder L_k, by brute force.
// Edges: rungs 0..k-1, upper rails k..2k-2, lower rails 2k-1..3k-3.
#include <bits/stdc++.h>
using namespace std;
typedef unsigned long long u64;
int k,m,D,nm; vector<u64> inc; // inc[e] = mask of matchings containing e
vector<int> blockOf; vector<u64> blockMask; // per block: matchings containing an edge of block (if rainbow so far)
unordered_set<u64> masks; u64 nodes=0;
// state: alive = matchings still rainbow. Block b has for each matching at most one edge.
void rec(int e,int def,u64 alive,vector<u64>&bm){
  if(!alive) return; nodes++;
  if(m-e < D-def && false) return;
  if(e==m){ if(def==D) masks.insert(alive); return; }
  // new block
  bm.push_back(inc[e]); rec(e+1,def,alive,bm); bm.pop_back();
  if(def<D) for(size_t b=0;b<bm.size();b++){ u64 old=bm[b]; u64 na=alive&~(old&inc[e]); if(!na) continue; bm[b]=old|inc[e]; rec(e+1,def+1,na,bm); bm[b]=old; }
}
int main(int argc,char**argv){ k=atoi(argv[1]); D=atoi(argv[2]); m=3*k-2;
  vector<vector<int>> M; for(int s=0;s<(1<<(k-1));s++){ if(s&(s>>1)) continue; vector<int> es; for(int i=0;i<k;i++){ bool cov=((s>>i)&1)||(i>0&&((s>>(i-1))&1)); if(!cov) es.push_back(i);} for(int i=0;i<k-1;i++) if((s>>i)&1){es.push_back(k+i);es.push_back(2*k-1+i);} M.push_back(es);} 
  nm=M.size(); if(nm>64){puts("needs k<=9 (at most 64 matchings)");return 1;} inc.assign(m,0); for(int j=0;j<nm;j++) for(int e:M[j]) inc[e]|=1ULL<<j;
  vector<u64> bm; rec(0,0,(nm==64?~0ULL:((1ULL<<nm)-1)),bm);
  // minimal masks
  vector<u64> v(masks.begin(),masks.end()); sort(v.begin(),v.end(),[](u64 a,u64 b){return __builtin_popcountll(a)<__builtin_popcountll(b);});
  vector<u64> mn; for(u64 x:v){ bool ok=true; for(u64 y:mn) if((y&x)==y){ok=false;break;} if(ok) mn.push_back(x);} 
  int best=-1; u64 bestCount=0;
  function<bool(int,u64)> go=[&](int left,u64 T){ const u64* pick=nullptr; int pc=99; for(const u64&y:mn) if(!(y&T)){ int c=__builtin_popcountll(y); if(c<pc){pc=c;pick=&y;} } if(!pick) return true; if(left==0) return false; u64 y=*pick; while(y){ u64 bit=y&-y; y^=bit; if(go(left-1,T|bit)) return true;} return false; };
  for(int t=0;t<=nm;t++){ if(go(t,0)){best=t;break;} }
  int singles=0; for(u64 y:mn) if(__builtin_popcountll(y)==1) singles++;
  printf("k=%d d=%d matchings=%d nodes=%llu minimalsets=%zu forced=%d h=%d\n",k,D,nm,nodes,mn.size(),singles,best);
}
