# Typeset notes

## Nine symmetry classes of extremal cube colorings

[Read the paper](cube_classification.pdf) · [LaTeX source](cube_classification.tex)
· [Web report and diagram atlas](../results/cube_classification.md)

A four-page report gives an elementary proof of the seven-color maximum,
a necessary equality condition, and all nine computed canonical representatives,
orbit sizes, stabilizers, and labeled diagrams. The full dataset saves every
one of the 174 fixed-edge partitions. No novelty is claimed.

```sh
python -m experiments.render_cube_atlas
tectonic --outdir papers papers/cube_classification.tex
```

The renderer deterministically regenerates the SVG and LaTeX from the checked
dataset. Mathematical verification belongs to the classification and its tests,
not to the renderer.

## Expansion and random walks: exact examples

[Read the paper](expansion_walks.pdf) · [LaTeX source](expansion_walks.tex)

A three-page expository note proves complete-graph and cycle expansion formulas,
exact ordinary/lazy walk formulas on K(d,d), and a disconnection obstruction on
unions of cliques. No novelty is claimed. Formula checks and a scoped
[self-review record](../results/walk_paper_verification.md) accompany the proofs.

```sh
tectonic --outdir papers papers/expansion_walks.tex
python -m unittest discover -s tests -p test_walk_formulas.py -v
```

## Rainbow perfect matchings

- [Rainbow perfect matchings on even cycles and two disjoint squares](cycle_extremizers.pdf)
- [Editable LaTeX source](cycle_extremizers.tex)
- [Markdown reading copy](../notes/cycle_extremizers.md)

The three-page paper contains the complete elementary proofs, a diagram of an
avoiding six-coloring, and the small-case table. No novelty or publication is
claimed.

The PDF is compiled directly from the self-contained LaTeX source. It uses
Latin Modern text and mathematics, theorem and proof environments, booktabs
tables, and a vector diagram drawn in TikZ.

Build from the repository root with Tectonic:

```sh
tectonic --outdir papers papers/cycle_extremizers.tex
```

Alternatively, upload `cycle_extremizers.tex` to a LaTeX editor such as Overleaf
and compile it with pdfLaTeX. No external images, bibliography file, or local
font files are required. The LaTeX file is the typesetting source; keep the
Markdown reading copy mathematically consistent when editing.

The computational experiments remain standard-library-only. LaTeX dependencies
are needed only to rebuild the paper. Inspect the compilation log and all
rendered pages before publishing.

The checked PDF was built with Tectonic 0.17.0 using the official
`tlextras-2022.0r0` bundle. The mathematical results and proof arguments are
unchanged by the typesetting conversion.
