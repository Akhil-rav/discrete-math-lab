# First session: take ownership of one result

Allow 60–90 minutes. Work on paper first; use the code to check afterward.

1. Draw C6. Label the left vertices 0,1,2 and the right vertices 0,1,2.
   Its edges are (i,i) and (i,i+1 mod 3). List both perfect matchings.
2. Color those six edges with four colors so neither matching is rainbow.
   Explain why five colors cannot work. Compare with the cycle argument in
   [the flagship report](rainbow-matchings/report.md) after making your attempt.
3. Run `python -m experiments.sparse_rainbow --check results/data/sparse_rainbow.json`.
   Locate the C6 entry. Explain what its 203 partitions and 9 extremal partitions
   count. They do not count colorings with fixed named colors.
4. Trace a three-position prefix with two colors. Count its one-position
   extensions. Then derive the two-position count without listing all full arrays.
5. Write six sentences: the question, the answer, an upper-bound argument, a
   lower-bound example, what the program checked, and what is not claimed new.

Save your own work in a dated journal entry when you have actually done it.
There is no pre-filled entry implying these exercises have been completed.
