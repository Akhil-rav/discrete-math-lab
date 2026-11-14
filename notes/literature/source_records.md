# Source records

All checks below occurred on **2026-11-13**. “Verified” concerns the named
statement and its stated application, not an audit of the entire paper's proof.
PDFs were read through web text extraction; full texts were not retained in Git.
Local cache hashes: not recorded. No paper is represented as exhaustively read.

## LTJ09 — exact bipartite matching thresholds

- **Record:** Xueliang Li, Jianhua Tu, Zemin Jin, *Bipartite rainbow numbers of
  matchings*, Discrete Mathematics 309(8) (2009), 2575–2578.
  [DOI](https://doi.org/10.1016/j.disc.2008.05.011).
- **Version checked:** [arXiv:math/0610910v1](https://arxiv.org/pdf/math/0610910v1),
  submitted October 30, 2006; full-text extraction available.
- **Extracted:** §1 definition of maximum avoiding count f and rb=f+1;
  Theorem 2.3: rb(K22,2K2)=3; Theorem 2.5:
  rb(K_{m,n},kK2)=m(k−2)+2 for m≥n≥k≥3.
- **Translation:** local A(Knn)=f(Knn,nK2)=rb(Knn,nK2)−1. Thus A(K33)=4,
  and the exceptional k=2 theorem gives A(K22)=2.
- **Checks:** author/title authentication, exact statement/hypotheses, application.
  **Verdict: verified; overlap: known after translation of notation.**
  The two sides may be interchanged before imposing m≥n. No properness assumption.
  No full classification of extremal colorings is attributed to this theorem.

## HY12 — Young and complete-graph perfect matchings

- **Record:** Ruth Haas, Michael Young, *The anti-Ramsey number of perfect
  matching*, Discrete Mathematics 312(5) (2012), 933–937.
  [Publisher](https://www.sciencedirect.com/science/article/pii/S0012365X11004663),
  [DOI](https://doi.org/10.1016/j.disc.2011.10.017).
- **Version/access:** publisher record and abstract. Mathematical expressions
  were not reliably available in the extracted abstract. Full theorem extraction
  **unavailable**; no theorem number or exact formula is asserted here.
- **Verified metadata/context:** complete graph host; minimum forcing number of
  colors in an exact coloring; perfect matching target. Independently cited in
  OY13, reference [9].
- **Verdict:** exact formula **unverified** here; application as a bipartite
  threshold **inapplicable**. Overlap: partial or adjacent result only.

## OY13 — hypergraph matching lower-bound mechanism

- **Record/version:** Lale Özkahya and Michael Young, *Anti-Ramsey number of
  matchings in hypergraphs*, [author manuscript dated June 13, 2013](https://web.cs.hacettepe.edu.tr/~ozkahya/pub/AR-hyperg.pdf).
  Introduction and Proposition 1, printed pp. 1–2; extraction available.
- **Extracted:** for the complete s-uniform host, ar(n,s,k) is a minimum exact
  forcing threshold. Proposition 1 gives ar(n,s,k)≥ex(n,s,k−1)+2 in its feasible
  matching range. Take k≥2 and n≥sk for our use.
- **Translation/application:** color every edge in a (k−1)-matching-free
  extremal hypergraph distinctly, and all remaining edges with one new color.
  A rainbow k-matching could use at most one outside edge and would leave a
  forbidden (k−1)-matching inside. This explains the +2 threshold.
- **Checks:** source authentication, statement extraction, construction inspected.
  **Verdict: verified** for this lower-bound explanation; overlap: known after
  translation of notation. No general hypergraph solver or reproduction claimed.
  Conjectures in the 2013 paper have **no current-open-status check** here.

## BE+16 — intervals and cyclic arithmetic progressions

- **Record:** Steve Butler, Craig Erickson, Leslie Hogben, Kirsten Hogenson,
  Lucas Kramer, Richard L. Kramer, Jephian Chin-Hung Lin, Ryan R. Martin,
  Derrick Stolee, Nathan Warnberg, Michael Young, *Rainbow arithmetic progressions*.
- **Version:** [arXiv:1404.7232v2](https://arxiv.org/abs/1404.7232v2), metadata
  revision January 11, 2016; [PDF](https://arxiv.org/pdf/1404.7232v2) returned by
  the web tool has an internal January 8, 2018 date. This discrepancy is retained;
  theorem locators refer to the returned PDF, not an assumed journal version.
- **Extracted:** §1 distinct-term AP and exact coloring definitions; Theorem 1.1
  small values for 3≤n≤8; Remark 1.4 interval/cyclic comparison. Cyclic power-of-two
  fact is attributed there to Jungić et al., not invented here.
- **Translation:** [n] is shifted to indices 0..n−1, preserving APs. Zn uses modular
  addition; all terms must be distinct. Code computes the maximum avoiding count
  then adds one. This yields the same exact-color threshold because merging colors
  cannot create a rainbow AP.
- **Checks:** authentication, selected statement extraction, finite application.
  **Verdict: verified** for these conventions and benchmark values; overlap: known
  after translation of notation. Finite searches do not prove asymptotic theorems.

## Y16 — finite abelian groups

- **Record/version:** Michael Young, *Rainbow Arithmetic Progressions in Finite
  Abelian Groups*, [arXiv:1603.08153v1](https://arxiv.org/abs/1603.08153v1), submitted
  March 26, 2016. The [returned PDF](https://arxiv.org/pdf/1603.08153v1) has an internal
  September 16, 2021 date; treat it as the specifically accessed copy, not a
  certified reproduction of the original uploaded bytes.
- **Extracted:** §1 nondegenerate k-AP definition and exact-color convention;
  Theorem 3 states aw(G×Zn,3)=aw(G,3)+aw(Zn,3)−2 for finite abelian G and odd n.
- **Application:** product coordinates in the implementation use componentwise
  modular addition. General product formulas and unitary colorings are **not**
  implemented or asserted from extraction; the selected groups are enumerated.
- **Checks:** source authentication, definitions and Theorem 3 statement extraction,
  translation of definitions. **Verdict: verified** for definition alignment;
  general theorem implementation **not attempted**. Overlap: partial or adjacent
  result only for the broader group classification.

## DS+18 — multiplicity is a different optimization

- **Record:** Jessica De Silva, Xiang Si, Michael Tait, Yunus Tunçbilek, Ruifan
  Yang, Michael Young, *Anti-Ramsey Multiplicities*.
- **Versions:** [arXiv:1801.00474v2](https://arxiv.org/abs/1801.00474v2), revised
  March 28, 2018 (abstract checked); [author-hosted v1](https://www.math.cmu.edu/~mtait/antiramseyREU.pdf),
  internal January 3, 2018 date (introduction checked). These are separate versions.
- **Extracted/context:** fixed-palette extremization of the proportion of rainbow
  copies, rather than the maximum number of colors avoiding one copy.
- **Verdict:** verified topic/definition context; individual results and proof
  dependencies **unverified** here. Overlap: partial or adjacent result only.
  No multiplicity theorem is used in the computations.

## AYZ95 — vertex color-coding

- **Record/version:** Noga Alon, Raphael Yuster, Uri Zwick, *Color-coding*,
  [author manuscript revised March 9, 1995](https://www.math.tau.ac.il/~nogaa/PDFS/col5.pdf).
- **Extracted:** §3, Lemma 3.1, printed pp. 4–5: subset DP for colorful paths;
  a fixed k-vertex simple path becomes colorful with probability k!/k^k when
  vertices receive independent uniform colors from a palette of size k.
- **Translation:** k counts **vertices** in our functions, so path length is k−1;
  masks encode color sets. This concerns vertex colors, unlike the edge-colored
  anti-Ramsey experiments. No independence assumptions are inferred from arbitrary
  graph colorings: all k^n assignments are enumerated for the finite probability check.
- **Checks:** source authentication, extraction, DP recurrence and probability
  application. **Verdict: verified; overlap: known after translation of notation.**
  Perfect-hash derandomization and cycle algorithms are not implemented.

## HLW06 — edge expansion

- **Record/version:** Shlomo Hoory, Nathan Linial, Avi Wigderson, *Expander graphs
  and their applications*, Bulletin of the AMS 43(4) (2006), 439–561.
  [Published author-hosted PDF](https://www.math.ias.edu/~avi/PUBLICATIONS/MYPAPERS/HLW06/hlw06.pdf),
  [DOI](https://doi.org/10.1090/S0273-0979-06-01126-8).
- **Extracted:** Definition 2.1, printed p. 452, counts cut edges once and minimizes
  boundary size / |S| for nonempty |S|≤|V|/2. Definition 2.2 concerns an increasing
  family of bounded-degree regular graphs with uniform positive expansion.
- **Translation:** `edge_expansion` returns this unnormalized edge quantity, not
  conductance or vertex expansion. Exact Fraction arithmetic is used.
- **Checks:** authentication, definition extraction, normalization/application.
  **Verdict: verified; overlap: known after translation of notation.** Walk examples
  use the explicitly derived transition rule in our note; no spectral estimate or
  construction theorem is claimed reproduced. Finite examples do not establish
  an expander family.

## W19 and MSS14 — advanced orientation

- **W19:** Avi Wigderson, *Mathematics and Computation*, [IAS-hosted draft dated
  March 25, 2019](https://www.math.ias.edu/files/Website03-25-19.pdf). Contents and
  chapter scope inspected: Chapters 7–8 connect randomness, pseudorandomness, and
  expansion. The draft subtitle differs from the final publisher title; BibTeX
  cites the draft without importing final-edition pagination.
- **MSS14:** Adam W. Marcus, Daniel A. Spielman, Nikhil Srivastava, *Interlacing
  Families I: Bipartite Ramanujan Graphs of All Degrees*,
  [arXiv:1304.4132v2](https://arxiv.org/abs/1304.4132v2), March 3, 2014 revision;
  abstract in [v2 PDF](https://arxiv.org/pdf/1304.4132v2) checked. It establishes
  existence of infinite families of d-regular bipartite Ramanujan graphs for d>2.
- **Verdict:** authenticated orientation references; no proof audit, theorem
  implementation, or project implication beyond context. Overlap: partial or
  adjacent result only. Existence is not a claim that our finite examples implement
  their method.
