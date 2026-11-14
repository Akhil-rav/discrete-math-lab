# Typeset notes

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
