# Typeset reports

All seven completed mathematical reports have editable LaTeX sources and
compiled PDFs. The web reports, code, and evidence records remain linked below.
The reports contain mathematical exposition, exact computations, and references
to the published results used.

| Report | PDF | LaTeX | Web report / evidence |
|---|---|---|---|
| Nine symmetry classes of extremal cube colorings | [Read](cube_classification.pdf) | [Source](cube_classification.tex) | [Classification and atlas](../results/cube_classification.md) |
| Exact probabilities of rainbow perfect matchings | [Read](random_rainbow.pdf) | [Source](random_rainbow.tex) | [Study and plot](../projects/random-colorings/report.md), [verification](../results/random_rainbow_verification.md) |
| Expansion and random walks: exact examples | [Read](expansion_walks.pdf) | [Source](expansion_walks.tex) | [Project](../projects/expansion-and-walks/report.md), [verification](../results/walk_paper_verification.md) |
| Disjoint unions of even cycles | [Read](cycle_extremizers.pdf) | [Source](cycle_extremizers.tex) | [General proof and equality cases](../notes/cycle_extremizers.md), [verification](../results/cycle_union_verification.md) |
| Matching foundations and exact small-host studies | [Read](matching_foundations.pdf) | [Source](matching_foundations.tex) | [Hall corollary](../notes/halls_theorem.md), [K33 classes](../results/k33_classification.md), [sparse hosts](../projects/rainbow-matchings/report.md) |
| Rainbow progressions in small intervals and groups | [Read](rainbow_progressions.pdf) | [Source](rainbow_progressions.tex) | [Definitions](../notes/rainbow_progressions.md), [finite results](../results/rainbow_progressions.md) |
| Vertex color-coding for simple paths | [Read](color_coding.pdf) | [Source](color_coding.tex) | [Method](../notes/color_coding.md), [22,955 comparisons](../results/algorithm_demos.md) |

The cube report combines its elementary seven-color bound with the complete
nine-class atlas. The probability report combines the counting proofs, the
six-host comparison, the figure, and the large-palette limit. The matching
foundations report collects the Hall corollary, 4,477 graph checks, known
complete-bipartite thresholds, four K33 classes, and sparse-host coverage.
The cycle paper proves A(G)=|E(G)|-2 for every nonempty union of even cycles
and counts all fixed-edge extremizers as the sum of binomial(n_i,2)^2 over
its components. It retains the cycle and two-square proofs as introductory cases.
The progression and color-coding reports typeset their existing definitions,
arguments, finite tables, references, and reproduction instructions.

## Build

Reading the committed PDFs requires no dependencies. To rebuild, install
Tectonic and run the relevant command from the repository root:

```sh
tectonic --outdir papers papers/cube_classification.tex
tectonic --outdir papers papers/random_rainbow.tex
tectonic --outdir papers papers/expansion_walks.tex
tectonic --outdir papers papers/cycle_extremizers.tex
tectonic --outdir papers papers/matching_foundations.tex
tectonic --outdir papers papers/rainbow_progressions.tex
tectonic --outdir papers papers/color_coding.tex
```

The reports use Latin Modern text and mathematics, theorem/proof environments,
booktabs tables, and linked references. All sources are self-contained except
for the probability report's committed image,
[random_rainbow.png](../results/figures/random_rainbow.png). Keep the repository
layout when building it. The other six sources can also be uploaded individually
to a LaTeX editor and compiled with pdfLaTeX.

The cube source and SVG are generated from the checked classification data:

```sh
python -m experiments.render_cube_atlas
```

The cube paper text is in [its LaTeX template](templates/cube_classification.tex.in);
the renderer fills in the data table, colors, and diagrams. The other six
`.tex` files are edited directly. Keep their corresponding Markdown
arguments and saved-data summaries consistent. Figure regeneration has its own
optional [Matplotlib dependency](../requirements-figures.txt); the mathematical
checks remain standard-library-only.

## Verification

The checked PDFs were built with Tectonic 0.17.0 and the official
`tlextras-2022.0r0` bundle. Inspect the compilation log and every rendered page
after an edit; typesetting checks do not replace mathematical verification.
The [verification index](../results/verification_index.md) records the scopes of
proof reviews, finite searches, source checks, and execution records.

Run the current mathematical and evidence checks from the repository root:

```sh
python -m tools.verify_repository
```
