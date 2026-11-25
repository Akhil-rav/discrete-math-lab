using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Numerics;

public static class LadderScan {
    static int k,n,depth;
    static long nodes;
    static Stopwatch clock;
    static double budget;
    static Dictionary<long,long> counts;
    static ulong Bit(int i) => 1UL<<i;
    static int Take(ref ulong x) { int j=BitOperations.TrailingZeroCount(x); x&=x-1; return j; }
    static void Edge(ulong[] g,int u,int v) { g[u]|=Bit(v); g[v]|=Bit(u); }
    static void Add(long key,long weight) {
        counts.TryGetValue(key,out long a);
        counts[key]=checked(a+weight);
    }
    static void Walk(ulong[] g,ulong[] o,int rem,long key,long weight) {
        if (((++nodes)&8191)==0 && clock.Elapsed.TotalSeconds>budget) throw new TimeoutException();
        Span<int> bin=stackalloc int[32]; bin.Clear();
        bool terminal=true;
        for(int i=0;i<n;i++) {
            ulong options=o[i] & ~( (2UL<<i)-1);
            while(options!=0) {
                int j=Take(ref options); terminal=false;
                ulong left=o[i]&g[j],right=o[j]&g[i];
                int loss=1+BitOperations.PopCount(left)+BitOperations.PopCount(right);
                if(rem==1) { bin[loss]++; continue; }
                // Delete the chosen pair and every pair through a new two-edge path.
                Edge(g,i,j);
                o[i]^=Bit(j)|left; o[j]^=Bit(i)|right;
                ulong x=left,y=right;
                while(x!=0) o[Take(ref x)]^=Bit(i);
                while(y!=0) o[Take(ref y)]^=Bit(j);
                Walk(g,o,rem-1,(key<<5)+loss,weight);
                x=left; y=right;
                while(x!=0) o[Take(ref x)]^=Bit(i);
                while(y!=0) o[Take(ref y)]^=Bit(j);
                o[i]^=Bit(j)|left; o[j]^=Bit(i)|right;
                g[i]^=Bit(j); g[j]^=Bit(i);
            }
        }
        if(terminal) Add(key,weight);
        else if(rem==1) for(int i=1;i<32;i++) if(bin[i]!=0) Add((key<<5)+i,checked(weight*bin[i]));
    }
    static long Half(int twist,int sign) {
        ulong[] g=new ulong[n],o=new ulong[n];
        for(int i=0;i<k;i++) {
            Edge(g,2*i,2*i+1);
            for(int r=0;r<2;r++) Edge(g,2*i+r,2*((i+1)%k)+(r^((i==k-1)?twist:0)));
        }
        for(int i=0;i<n;i++) {
            ulong blocked=Bit(i)|g[i], x=g[i];
            while(x!=0) blocked|=g[Take(ref x)];
            o[i]=((1UL<<n)-1)&~blocked;
        }
        var reps=new Dictionary<int,(int,int,int)>();
        int q=0;
        for(int i=0;i<n;i++) for(int j=i+1;j<n;j++) if((o[i]&Bit(j))!=0) {
            q++;
            int d=j/2-i/2,par=(i^j)&1,code=Math.Min(2*d+par,2*(k-d)+(par^twist));
            reps.TryGetValue(code,out var prev); reps[code]=(i,j,prev.Item3+1);
        }
        if(q==0) { Add(1,sign); return q; }
        foreach(var v in reps.Values) {
            var (i,j,w)=v; var gg=(ulong[])g.Clone(); var oo=(ulong[])o.Clone();
            ulong l=oo[i]&gg[j],r=oo[j]&gg[i]; int loss=1+BitOperations.PopCount(l)+BitOperations.PopCount(r);
            Edge(gg,i,j); oo[i]^=Bit(j)|l; oo[j]^=Bit(i)|r;
            while(l!=0) oo[Take(ref l)]^=Bit(i);
            while(r!=0) oo[Take(ref r)]^=Bit(j);
            long key=32+loss;
            if(depth==1) Add(key,sign*w); else Walk(gg,oo,depth-1,key,sign*w);
        }
        return q;
    }
    public static string Compare(int cols,int t,double seconds) {
        if(cols<4 || cols>30 || t<1 || t>7) throw new ArgumentException();
        k=cols;n=2*k;depth=t;nodes=0;budget=seconds;clock=Stopwatch.StartNew();counts=new Dictionary<long,long>();
        try {
            long a=Half(0,1), b=Half(1,-1); int different=0; long example=0, delta=0;
            foreach(var entry in counts) if(entry.Value!=0){different++;if(example==0 || entry.Key>example){example=entry.Key;delta=entry.Value;}}
            var loss=new List<int>(); long v=example;
            while(v>1){loss.Add((int)(v&31));v>>=5;} loss.Reverse();
            return $"{k} {t} complete Q={a}/{b} differing-loss-words={different} last=[{string.Join(",",loss)}] count-difference={delta} nodes={nodes} seconds={clock.Elapsed.TotalSeconds:F1}";
        } catch(TimeoutException) {return $"{k} {t} INCOMPLETE nodes={nodes} seconds={clock.Elapsed.TotalSeconds:F1}";}
    }
}
