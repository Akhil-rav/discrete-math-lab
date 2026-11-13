# Discrete Math Lab

A reproducible notebook for proofs, small exhaustive experiments, and carefully
sourced reading in combinatorics and theoretical computer science.

**Research status:** learning, literature study, and reproduction. No result here
is claimed new. Literature checks are selected and explicitly scoped.

## Start here

Python **3.11+**, standard library only. From the repository root:

```sh
python -m unittest discover -s tests -v
python -m experiments.reproduce --check results/data/small_cases.json
```

See [experiment contracts and individual commands](experiments/README.md),
[raw results](results/data/small_cases.json), and [verification](results/verification.md).

## Current focus

**Project portfolio:** [five connected tracks](projects/README.md), with a
[flagship sparse rainbow-matching report](projects/rainbow-matchings/report.md),
[12-week learning plan](projects/roadmap.md), and [first-session exercises](projects/first-session.md).
The material was developed with AI assistance; these checkpoints distinguish
reproducible repository artifacts from independently demonstrated understanding.

The core direction is **rainbow perfect matchings and anti-Ramsey questions in
bipartite graphs**, with adjacent tracks in rainbow arithmetic progressions,
vertex color-coding, and expansion/random walks.

The [literature map](notes/literature/README.md) connects Michael Young's work
to these topics and records relevant IAS connections for Avi Wigderson, Noga
Alon, and Nikhil Srivastava. It distinguishes faculty from historical visitors.
[Source records](notes/literature/source_records.md) state what was actually
checked, including inaccessible exact statements and version discrepancies.
[BibTeX references](references.bib) accompany the notes.

## Repository structure

- `notes/` — definitions, theorem summaries, proof sketches, and literature notes
- `src/` — reusable implementations of discrete-math objects and algorithms
- `experiments/` — scripts for testing small cases and exploring patterns
- `results/` — tables, observations, failed conjectures, and computational output

## Experiment 1: regular bipartite graphs

The experiment exhaustively generates every labeled $d$-regular bipartite graph with
$n \le 5$ vertices on each side and verified computationally that each
has a perfect matching: **4,477 graphs checked, 0 failures**.

- Proof connection: `notes/halls_theorem.md`
- Experiment: `experiments/regular_bipartite_matchings.py`
- Results: `results/regular_bipartite_small_cases.md`

This is a **reproduction of a known theorem**.

## Experiment 2: rainbow perfect matchings

The experiment exhaustively searches color patterns of small complete bipartite
graphs, up to color relabeling.

- $K_{2,2}$: 15 patterns checked; maximum of 2 colors while avoiding a rainbow perfect matching
- $K_{3,3}$: 21,147 patterns checked; maximum of 4 colors while avoiding a rainbow perfect matching

- Definitions: `notes/rainbow_matchings.md`
- Experiment: `experiments/rainbow_complete_bipartite.py`
- Results: `results/rainbow_knn_small_cases.md`

These reproduce Li–Tu–Jin's known thresholds after translating their convention;
see [the precise comparison](notes/literature/young_and_matchings.md).

## Completed extensions

| Track | Verified finite scope | Result / note |
|---|---|---|
| Extremal K33 classification | All 87 extremizers, full vertex automorphism action plus color renaming | [Four classes, orbit sizes 6,36,36,9](results/k33_classification.md) |
| Rainbow progressions | Intervals/cyclic groups of orders 3..9 and three small product groups | [Exact thresholds and witnesses](results/rainbow_progressions.md) |
| Color-coding | Every graph of order ≤4, each 1≤k≤n, all k-color assignments | [22,955 oracle comparisons](results/algorithm_demos.md) |
| Expansion and walks | K4, C6, K33, and two disjoint triangles | [Exact cuts and rational walk probabilities](notes/expansion_and_walks.md) |

Color-coding uses vertex colors; rainbow matching uses edge colors. Finite
expansion examples do not establish an infinite expander family. The original
experiment modules remain available and are rerun by the full suite.

## Research labels

To keep the notebook precise, I use the following labels:

- **Known theorem** — established result with a citation
- **Reproduction** — my own verification or implementation of a known result
- **Experimental observation** — pattern seen in computation, not proved
- **Conjecture** — statement suggested by evidence, not proved
- **Counterexample** — explicit example disproving a conjecture
- **New result** — reserved for claims that have been proved and checked against the literature

## Next milestone

The sparse-host extension now covers six hosts through 12 edges, including all
4,213,597 cube edge partitions via exact subtree accounting. Its maximum avoiding
color count is 7, attained by 174 normalized partitions. See the
[report and limits](projects/rainbow-matchings/report.md). The next steps are
to understand these witnesses, classify them by cube symmetries, and compare
with published sparse-host results before proposing any general statement.

See [contribution and claim standards](CONTRIBUTING.md). Automated checks rerun
the tests and compare regenerated data on Python 3.11 and 3.13 in CI; local run
details and CI status are reported separately in the verification record.

## About

Akhil Ravuri — high school student interested in combinatorics, discrete mathematics, and theoretical computer science.
