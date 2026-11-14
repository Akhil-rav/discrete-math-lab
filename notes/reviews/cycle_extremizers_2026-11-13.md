# Review of the cycle and disjoint-square note

**LaTeX conversion, November 13, 2026:** replaced the earlier PDF renderer with
the self-contained source `papers/cycle_extremizers.tex`. The PDF now uses native
Latin Modern mathematics, AMS theorem/proof environments, booktabs tables, and
a TikZ construction diagram. The maximum and extremal-count statements and
their proof dependencies are unchanged. The definition of A explicitly requires
an avoiding coloring, so its maximum is defined; all hosts in the note satisfy
this requirement. The native binomial expression replaces the equivalent
expanded expression used by the earlier PDF.

Validated with Tectonic 0.17.0 and the official `tlextras-2022.0r0` bundle. The
final compile log contains no overfull/underfull boxes, undefined-reference
warnings, or missing-character warnings. All three final pages were rendered
and visually inspected. The earlier Python rendering script has been removed;
it remains available in Git history.

**Presentation review, November 13, 2026:** standardized mathematical subscripts,
set notation, theorem numbering, and the squared binomial coefficient; added
an abstract and typeset PDF. These are notation and presentation changes, not
changes to the theorem conclusions or proof dependencies. The PDF uses an
equivalent expanded expression for the squared binomial coefficient. The C10
table entry is explicitly a proof consequence, not an unrecorded computation.
All three final PDF pages were rendered and visually inspected, including the
six-color diagram and the two tables. No unresolved mathematical error was found
in the three elementary proofs. This is a review finding, not a guarantee of
error-free mathematics or external refereeing.

**Review, November 13, 2026:** the submitted logical arguments were checked for
the n=2 boundary case, upper and lower bounds, equality conditions, uniqueness
of partitions, and the different-component alternative in the two-pair case.
Verdict: proved under the stated fixed-edge, color-renaming convention. This
records a logical review, not external refereeing. Only the repository's
documented computations are used as computational evidence. No literature
novelty determination was made.
