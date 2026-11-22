"""First differing coefficient of the rooted leaf-set polynomials."""
from cycle_histories import cycle_count, path_count


def multiply(a, b):
    result = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            result[i+j] += x*y
    return result


def rooted(parts):
    whole, marked = [1], [0]
    for k in parts:
        cycle = [cycle_count(k, j) for j in range(k//3+1)]
        m = max(0, k-7)
        at_root = [k*path_count(m, j) for j in range((m+2)//3+1)]
        old, new = multiply(marked, cycle), multiply(whole, at_root)
        marked = [0]*max(len(old), len(new))
        for term in (old, new):
            for i, x in enumerate(term):
                marked[i] += x
        whole = multiply(whole, cycle)
    return marked


if __name__ == "__main__":
    from itertools import zip_longest
    for a,b in [([7]*8+[112], [8]*21), ([9]*5+[135], [10]*18)]:
        h, g = rooted(a), rooted(b)
        i, diff = next((i,x-y) for i,(x,y) in
                       enumerate(zip_longest(h,g,fillvalue=0)) if x != y)
        print(sum(a), i, diff)

    # Check the two-experiment identity without using the marked-product rule.
    from cycle_histories import direct_polynomial
    for parts in [(4,), (7,), (8,), (4,5), (7,8)]:
        f = [1]
        for k in parts:
            f = multiply(f, [cycle_count(k,j) for j in range(k//3+1)])
        h = direct_polynomial(parts)
        observed = direct_polynomial(parts+(4,))
        for j in range(sum(parts)+5):
            expected = h[j]+4*h[j-1]+4*(f[j] if j < len(f) else 0)
            assert observed[j] == expected
    print("Square identity agrees with direct enumeration on five examples.")
