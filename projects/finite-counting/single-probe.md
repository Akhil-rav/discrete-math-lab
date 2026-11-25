# The shortest universal single path probe

Fix the original total length m>=6. There are at least three positive-length paths, at most one of length one, and signs may be arbitrary. Only the modified-host law is observed. Among positive probes of length p>=2 (so adding one always preserves simplicity), the shortest which determines every signed type is **p=m-2**. This concerns a choice made knowing m, and an exact full distribution, not the number of samples needed.

Use E,O from [the two-observation decoder](calibrated-paths.md); the observed transform is C=E+x^p O. Write sigma for the product of the original signs. Complementing a subset multiplies its sign by sigma and sends its length j to m-j. In even path count this gives E_(m-j)=sigma E_j and O_(m-j)=sigma O_j. In odd path count it gives E_(m-j)=sigma O_j. Here subscripts denote coefficients. Always E_0=1, O_0=E_1=0 and |O_1|<=1.

Suppose two signed types have the same C with p=m-2. The top coefficient at p+m is O_m, zero for even path count and sigma for odd path count. Thus parity agrees and in the odd case sigma agrees. Taking differences (first type minus second), the only potentially hidden terms are

    delta O = a x + b x^2,      delta E = -a x^(m-1) - b x^m.

In odd parity E_m=0, so b=0. The value B(1) of B=E-O is a product of factors 1-s_i: it is either zero or a power of two at least eight. The difference of the two B(1) values is -2a, of absolute value at most four. Since both values are multiples of eight, a=0.

In even parity E_(m-1)=sigma E_1=0, so a=0. If the sign products agree, so do the two E_m and b=0. If they differ, b is 2 or -2. Now the B(1) difference is -2b, impossible by the same divisibility. Thus E and O both agree, and [length and sign peeling](calibrated-paths.md) gives identical signed types.

For any 2<=p<=m-3 take three original paths of lengths p,1,m-p-1. Give the length-p path a negative sign. Assign the other two signs both positive in one host and both negative in the other. The hosts differ even if two lengths coincide. After adding a positive length-p path, swapping the positive and negative length-p copies and negating all signs identifies the two augmented sign multisets. Their laws agree because only even subsets enter. This counterexample works throughout the lower range and uses simple graphs. It proves minimality; it does not assume sufficiency is monotone in probe length.

The finite collision search in [single_probe_search.py](single_probe_search.py) motivated the question. The proof, not the search, gives the unrestricted result within these hypotheses. Priority has not been verified.


[Independent enumeration](check_single_probe.py) constructs distributions by conditioning on terminal colors instead of comparing even-subset polynomials. It distinguishes all 4,164 signed types across fixed totals m=6 through 16 and verifies the exhibited counterexamples for every shorter admissible probe in that range. For the forward calculation, see Alan D. Sokal, [Chromatic Roots are Dense in the Whole Complex Plane](https://arxiv.org/abs/cond-mat/0012369), section 2.3, equations (2.31)-(2.32), on terminal-restricted Potts partition functions of generalized theta graphs. That calculation is established background; it does not by itself state this inverse cutoff.


[Comparison with binary coset weight enumerators and the two-terminal Potts formula](probe-literature.md).
