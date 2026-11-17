// Minimal rainbow-survivor sets for deficit D on L_k, written one per line as lists of matching indices.
#include <bits/stdc++.h>
using namespace std;
const int W=2048; typedef bitset<W> B;
int k,m,D,nm; vector<B> inc; struct H{size_t operator()(const B&b)const{return hash<B>()(b);}};
unordered_set<B,H> masks; unsigned long long nodes=0, bad=0, full=0; B fam;
void rec(int e,int def,const B&alive,vector<B>&bm){
  if(alive.none()) return; nodes++;
  if(e==m){ if(def==D){ full++; if((alive&fam).none()) bad++; } return; }
  bm.push_back(inc[e]); rec(e+1,def,alive,bm); bm.pop_back();
  if(def<D) for(size_t b=0;b<bm.size();b++){ B old=bm[b]; B na=alive&~(old&inc[e]); if(na.none()) continue; bm[b]=old|inc[e]; rec(e+1,def+1,na,bm); bm[b]=old; }
}
int main(int argc,char**argv){ k=atoi(argv[1]); D=atoi(argv[2]); m=3*k-2;
  vector<vector<int>> M; for(int s=0;s<(1<<(k-1));s++){ if(s&(s>>1)) continue; vector<int> es; for(int i=0;i<k;i++){ bool cov=((s>>i)&1)||(i>0&&((s>>(i-1))&1)); if(!cov) es.push_back(i);} for(int i=0;i<k-1;i++) if((s>>i)&1){es.push_back(k+i);es.push_back(2*k-1+i);} M.push_back(es);} 
  nm=M.size(); if(nm>W){puts("too many matchings");return 1;} inc.assign(m,B()); for(int j=0;j<nm;j++) for(int e:M[j]) inc[e][j]=1;
  B all; for(int j=0;j<nm;j++) all[j]=1; for(int a=3;a<argc;a++){ fam[atoi(argv[a])]=1; printf("gaps:"); for(int e:M[atoi(argv[a])]) if(e>=k&&e<2*k-1) printf(" %d",e-k); puts(""); } vector<B> bm; rec(0,0,all,bm);
  printf("k=%d d=%d colourings_with_rainbow=%llu defeated=%llu\n",k,D,full,bad);
}
