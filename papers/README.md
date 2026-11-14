# Typeset notes

- [Rainbow perfect matchings on even cycles and two disjoint squares](cycle_extremizers.pdf)
- [Editable mathematical text](../notes/cycle_extremizers.md)
- [Review scope](../notes/reviews/cycle_extremizers_2026-11-13.md)

The three-page paper contains the complete elementary proofs, a diagram of an
avoiding six-coloring, and the small-case table. No novelty or publication is
claimed.

The optional PDF build uses ReportLab and Cambria font files:

```sh
python papers/build_cycle_note.py --font-dir C:/Windows/Fonts
```

The computational experiments remain standard-library-only. PDF dependencies
are needed only to rebuild the typeset note. When editing, compare the PDF text
with the Markdown source and inspect all rendered pages before publishing.
