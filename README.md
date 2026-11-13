# Discrete Math Lab

A working notebook for proofs, computational experiments, and research notes in combinatorics and discrete mathematics.

## Current focus

I am building a foundation in graph theory, matchings, extremal combinatorics, and computational exploration. The current direction is **rainbow perfect matchings and anti-Ramsey-style questions in bipartite graphs**.

## Repository structure

- `notes/` — definitions, theorem summaries, proof sketches, and literature notes
- `src/` — reusable implementations of discrete-math objects and algorithms
- `experiments/` — scripts for testing small cases and exploring patterns
- `results/` — tables, observations, failed conjectures, and computational output

## Experiment 1: regular bipartite graphs

I exhaustively generated every labeled $d$-regular bipartite graph with
$n \le 5$ vertices on each side and verified computationally that each
has a perfect matching: **4,477 graphs checked, 0 failures**.

- Proof connection: `notes/halls_theorem.md`
- Experiment: `experiments/regular_bipartite_matchings.py`
- Results: `results/regular_bipartite_small_cases.md`

This is a **reproduction of a known theorem**.

## Experiment 2: rainbow perfect matchings

I added edge-coloring tools and exhaustively searched color patterns of
small complete bipartite graphs, up to color relabeling.

- $K_{2,2}$: 15 patterns checked; maximum of 2 colors while avoiding a rainbow perfect matching
- $K_{3,3}$: 21,147 patterns checked; maximum of 4 colors while avoiding a rainbow perfect matching

- Definitions: `notes/rainbow_matchings.md`
- Experiment: `experiments/rainbow_complete_bipartite.py`
- Results: `results/rainbow_knn_small_cases.md`

These are recorded as **exhaustive computational small cases**, with no novelty claim.

## Research labels

To keep the notebook precise, I use the following labels:

- **Known theorem** — established result with a citation
- **Reproduction** — my own verification or implementation of a known result
- **Experimental observation** — pattern seen in computation, not proved
- **Conjecture** — statement suggested by evidence, not proved
- **Counterexample** — explicit example disproving a conjecture
- **New result** — reserved for claims that have been proved and checked against the literature

## Next milestone

Classify the extremal four-color patterns of $K_{3,3}$ and then move from
complete bipartite graphs to broader regular bipartite graph families.

## About

Akhil Ravuri — high school student interested in combinatorics, discrete mathematics, and theoretical computer science.
