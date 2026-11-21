"""Exact binary-color collision search, batched by the sum of path lengths."""
def partitions(total,slots,lo=1):
    if slots==1:
        if total>=lo: yield (total,)
        return
    for v in range(lo,total//slots+1):
        for tail in partitions(total-v,slots-1,max(2,v)):
            yield (v,)+tail

def packed(ls):
    # Base 2^(r+1): coefficients cannot carry even for equal lengths.
    width=len(ls)+1
    even,odd=1,0
    for v in ls:
        even,odd=even+(odd<<(width*v)),odd+(even<<(width*v))
    return even

def search(r,limit):
    tested=0
    for s in range(2*r-1,limit+1):
        seen={}
        for ls in partitions(s,r):
            tested+=1; key=packed(ls)
            if key in seen:
                return tested,(seen[key],ls)
            seen[key]=ls
    return tested,None

if __name__=='__main__':
    import sys
    print(search(int(sys.argv[1]),int(sys.argv[2])))
