# What the binary conflict count measures

The forward transform in the [single-probe note](single-probe.pdf) is a specialization of finite Fourier duality. Its inverse problem has a different input: only the distribution on the augmented graph is supplied, without the original signed paths or a generator matrix.

| Setting | Given | Obtained |
|---|---|---|
| Two-terminal Potts calculation | Path lengths, weights, terminal spins | Restricted partition functions, then the unrestricted partition function by summing over terminal spins |
| Binary coset transform | A binary linear code and coset shift, or their signed dual weight sums | The coset weight distribution; conversely the distribution specifies the signed dual sums **by weight**, not individual dual words |
| Single-probe reconstruction | Original total length, positive probe length, and one normalized conflict-count law | For probe length m-2, the original multiset of signed path lengths under the simple parallel-path hypotheses |

**Exact dictionary.** On the augmented graph of N edges, encode a negative edge by 1 in a vector b. Write u for the independent fair vertex bits and C for the image of the map sending u to its edge differences over the binary field. Every element of this cut space has equally many preimages. Thus w=b+du is uniform on b+C. An edge is counted when its coordinate in w is **zero**, so the probability generating function G is the coset zero-coordinate enumerator divided by |C|. Using the ordinary Hamming weight without reversing it would count the opposite events.

For x an indeterminate, averaging the product of the factors 1+x(-1)^(w_e) gives

    (1-x)^N G((1+x)/(1-x)) = sum over y in C-perp of (-1)^(b dot y) x^weight(y).

Indeed the character associated to y averages to zero on C unless it is trivial there. The dual consists of even edge sets: orthogonality to the cut of each vertex says its selected degree is even. On the augmented path system these sets take whole paths and use evenly many in total. Splitting on the positive probe gives exactly E+x^p O in the note. This derivation uses normalized probabilities; the observer need not be told |C|.

**What is covered by earlier work?** Andrew Goodall, [Fourier analysis on finite Abelian groups: some graphical applications](https://iuuk.mff.cuni.cz/~andrew/dwajgApr06.pdf), equation (8) and the Hamming enumerator specialization following (13), supplies precisely the coset transform, including the shift character and the zero-coordinate convention. Alan D. Sokal, [Chromatic roots are dense in the whole complex plane](https://arxiv.org/abs/cond-mat/0012369), section 2.3, equations (2.31)-(2.32), gives a forward terminal calculation on generalized theta graphs. Neither cited calculation, taken alone, shows how to separate overlapping coefficients in E+x^p O. In fact the same identities hold on the two different original types in every shorter-probe counterexample; invertibility of the transform cannot by itself distinguish those types.

**Scope of this check.** English-language searches combined generalized theta graphs and inverse path lengths with Ising polynomials, signed graphs, cut spaces and coset weight enumerators. The direct overlap verified here is the forward transform. The family-specific separation argument and the sharp threshold still need a prior-art check under other formulations, particularly identification of binary codes with repeated coordinates from weight distributions. No conclusion about priority or independent refereeing follows.
