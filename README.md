# Discrete Math Lab

A working notebook for proofs, computational experiments, and research notes in combinatorics and discrete mathematics.

## Current focus

I am building a foundation in graph theory, matchings, extremal combinatorics, and computational exploration. The goal is to reproduce known results on small cases, test conjectures, and develop research questions carefully.

## Repository structure

- `notes/` — definitions, theorem summaries, proof sketches, and literature notes
- `src/` — reusable implementations of discrete-math objects and algorithms
- `experiments/` — scripts for testing small cases and exploring patterns
- `results/` — tables, observations, failed conjectures, and computational output

## First completed experiment

**Regular bipartite graphs and perfect matchings.**

I exhaustively generated every labeled $d$-regular bipartite graph with
$n \le 5$ vertices on each side and verified computationally that each
has a perfect matching: **4,477 graphs checked, 0 failures**.

- Proof connection: `notes/halls_theorem.md`
- Experiment: `experiments/regular_bipartite_matchings.py`
- Results: `results/regular_bipartite_small_cases.md`

This is explicitly a **reproduction of a known theorem**, not a new result.
The point is to validate the computational toolkit before using it on
rainbow-matching and anti-Ramsey questions.

## Research labels

To keep the notebook precise, I use the following labels:

- **Known theorem** — established result with a citation
- **Reproduction** — my own verification or implementation of a known result
- **Experimental observation** — pattern seen in computation, not proved
- **Conjecture** — statement suggested by evidence, not proved
- **Counterexample** — explicit example disproving a conjecture
- **New result** — reserved for claims that have been proved and checked against the literature

## Next milestone

Add edge colors and build tools for detecting rainbow perfect matchings.

## About

Akhil Ravuri — high school student interested in combinatorics, discrete mathematics, and theoretical computer science.
