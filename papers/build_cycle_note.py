"""Typeset the self-contained cycle note (optional PDF build).

Requires reportlab and Cambria fonts. Run from repository root:
python papers/build_cycle_note.py --font-dir C:/Windows/Fonts
The computational experiments require neither these fonts nor reportlab.
"""
import argparse
from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle, Flowable,
)

ROOT = Path(__file__).resolve().parents[1]
NAVY = colors.HexColor('#19354a')
GRAY = colors.HexColor('#53616a')


class Coloring(Flowable):
    def __init__(self):
        super().__init__()
        self.width, self.height = 480, 126

    def draw(self):
        c = self.canv
        palettes = [('#19354a', '#ba603f', '#19354a', '#ba603f'),
                    ('#28786e', '#87619e', '#bd8b28', '#647f9b')]
        for x, palette, labels in [(115, palettes[0], 'ABAB'), (350, palettes[1], 'CDEF')]:
            pts = [(x-35, 91), (x+35, 91), (x+35, 21), (x-35, 21)]
            offsets = [(0, 7), (12, -3), (0, -15), (-12, -3)]
            for i, (color, label) in enumerate(zip(palette, labels)):
                a, b = pts[i], pts[(i+1) % 4]
                c.setStrokeColor(colors.HexColor(color))
                c.setLineWidth(2.4)
                c.line(*a, *b)
                dx, dy = offsets[i]
                c.setFillColor(colors.HexColor(color))
                c.setFont('Paper', 11)
                c.drawCentredString((a[0]+b[0])/2+dx, (a[1]+b[1])/2+dy, label)
            c.setFillColor(NAVY)
            for px, py in pts:
                c.circle(px, py, 2.7, fill=1, stroke=0)
        c.setFillColor(GRAY)
        c.setFont('Paper', 9)
        c.drawCentredString(115, 112, 'First component')
        c.drawCentredString(350, 112, 'Second component')


def build(font_dir, destination):
    pdfmetrics.registerFont(TTFont('Paper', str(font_dir/'cambria.ttc'), subfontIndex=0))
    pdfmetrics.registerFont(TTFont('Paper-Bold', str(font_dir/'cambriab.ttf')))
    pdfmetrics.registerFont(TTFont('Paper-Italic', str(font_dir/'cambriai.ttf')))
    pdfmetrics.registerFontFamily('Paper', normal='Paper', bold='Paper-Bold', italic='Paper-Italic')
    body = ParagraphStyle('body', fontName='Paper', fontSize=10.5, leading=14.4,
                          alignment=TA_JUSTIFY, spaceAfter=7, textColor=colors.HexColor('#20252a'))
    heading = ParagraphStyle('heading', parent=body, fontName='Paper-Bold', fontSize=14,
                             leading=19, spaceBefore=5, spaceAfter=11, textColor=NAVY)
    equation = ParagraphStyle('equation', parent=body, alignment=TA_CENTER,
                              fontSize=13, leading=22, spaceBefore=2, spaceAfter=12)
    caption = ParagraphStyle('caption', parent=body, fontSize=9, leading=12,
                             alignment=TA_CENTER, textColor=GRAY)
    story = []

    def p(text, style=body):
        story.append(Paragraph(text, style))

    def h(text):
        p(text, heading)

    def eq(text):
        p(text, equation)

    def table(rows, widths):
        cells = [[Paragraph(str(v), ParagraphStyle('cell', parent=body, fontSize=10,
                   leading=13, spaceAfter=0)) for v in row] for row in rows]
        t = Table(cells, colWidths=widths, hAlign='CENTER')
        t.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#edf2f5')),
            ('LINEBELOW', (0, 0), (-1, 0), .7, NAVY),
            ('LINEBELOW', (0, -1), (-1, -1), .4, colors.HexColor('#bcc6cc')),
            ('VALIGN', (0, 0), (-1, -1), 'TOP'),
            ('LEFTPADDING', (0, 0), (-1, -1), 9), ('RIGHTPADDING', (0, 0), (-1, -1), 9),
            ('TOPPADDING', (0, 0), (-1, -1), 5), ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
        ]))
        story.extend([t, Spacer(1, 11)])

    title = ParagraphStyle('title', parent=body, fontName='Paper-Bold', fontSize=23,
                           leading=27, alignment=TA_CENTER, spaceAfter=13, textColor=NAVY)
    p('Rainbow perfect matchings<br/>on even cycles and two disjoint squares', title)
    p('Akhil Ravuri', ParagraphStyle('author', parent=body, alignment=TA_CENTER,
                                    fontSize=12, spaceAfter=16))
    p('<b>Abstract.</b> We determine the maximum number of colors in an edge coloring '
      'of an even cycle that avoids a rainbow perfect matching and count all extremal '
      'partitions of its fixed edge set. For two disjoint squares, we prove that the '
      'maximum is six and that exactly two extremal partitions occur. The arguments '
      'are elementary and self-contained; no novelty is claimed.')
    h('1. Definitions and the even-cycle formula')
    p('All graphs are finite and simple. Edge colorings need not be proper. A perfect '
      'matching is <i>rainbow</i> when its edges have pairwise distinct colors. Let '
      '<i>A</i>(<i>G</i>) be the largest number of colors in a coloring avoiding every '
      'rainbow perfect matching. Let <i>N</i><sub>ext</sub>(<i>G</i>) count the extremal '
      'partitions of the fixed edge set into color classes. Color names are ignored; '
      'vertex symmetries are not identified.')
    p('<b>Theorem 1.</b> For every integer <i>n</i> ≥ 2,')
    eq('<i>A</i>(<i>C</i><sub>2n</sub>) = 2<i>n</i> − 2, &nbsp;&nbsp; '
       '<i>N</i><sub>ext</sub>(<i>C</i><sub>2n</sub>) = [<i>n</i>(<i>n</i> − 1)/2]<super>2</super>.')
    p('<b>Proof.</b> The cycle has exactly two perfect matchings, <i>M</i><sub>1</sub> '
      'and <i>M</i><sub>2</sub>: one choice at a vertex forces the alternating edges '
      'around the cycle. These matchings partition its 2<i>n</i> edges. Let '
      '<i>S</i><sub>i</sub> be the palette on <i>M</i><sub>i</sub>. Each palette has '
      'at most <i>n</i> − 1 colors, so')
    eq('|<i>S</i><sub>1</sub> ∪ <i>S</i><sub>2</sub>| ≤ '
       '|<i>S</i><sub>1</sub>| + |<i>S</i><sub>2</sub>| ≤ 2<i>n</i> − 2.')
    p('For equality, merge one pair of edges in each matching into a color class '
      'and give all remaining edges distinct colors, with disjoint palettes '
      'between the matchings. This uses 2<i>n</i> − 2 colors and avoids a rainbow matching.')
    p('Conversely, equality forces both palettes to have size <i>n</i> − 1 and to be '
      'disjoint. A partition of <i>n</i> edges into <i>n</i> − 1 classes has exactly '
      'one doubleton and otherwise singletons. Choosing that pair independently '
      'in each matching gives [<i>n</i>(<i>n</i> − 1)/2]<super>2</super> distinct '
      'partitions, and every extremizer arises uniquely this way. ∎')

    story.append(PageBreak())
    h('2. The maximum for two disjoint squares')
    p('<b>Theorem 2.</b> If <i>G</i> is the disjoint union of two copies '
      '<i>H</i><sub>1</sub>, <i>H</i><sub>2</sub> of <i>C</i><sub>4</sub>, then '
      '<i>A</i>(<i>G</i>) = 6.')
    p('<b>Proof.</b> Color the edges of <i>H</i><sub>1</sub> in cyclic order '
      '<i>A</i>, <i>B</i>, <i>A</i>, <i>B</i>. Give the four edges of '
      '<i>H</i><sub>2</sub> four distinct new colors. Every global perfect matching '
      'contains one of the two monochromatic local matchings in '
      '<i>H</i><sub>1</sub>. Thus six colors are attainable without a rainbow matching.')
    story.append(Coloring())
    p('Figure 1. An avoiding six-coloring; the first square forces a repeated color.', caption)
    story.append(Spacer(1, 10))
    p('For the upper bound, consider a coloring using at least seven colors on the '
      'eight edges. With eight colors, every perfect matching is rainbow. With '
      'seven colors, precisely one pair <i>e</i>, <i>f</i> shares a color and all '
      'other classes are singletons. In the component containing <i>e</i>, choose '
      'the alternating matching omitting <i>e</i>. Combine it with either matching '
      'of the other component. The resulting perfect matching cannot contain the '
      'only repeated pair, so it is rainbow. This proves the upper bound. ∎')
    h('3. Characterizing all extremal partitions')
    p('<b>Theorem 3.</b> With edge positions fixed and color names ignored, '
      '<i>N</i><sub>ext</sub>(<i>G</i>) = 2 for the graph of Theorem 2.')
    p('<b>Proof.</b> Six nonempty color classes on eight edges have total excess '
      'size two over singletons. Their sizes are therefore either '
      '(3, 1, 1, 1, 1, 1) or (2, 2, 1, 1, 1, 1).')
    p('<b>Excluding the triple.</b> There are four global perfect matchings, formed '
      'by independently choosing one of two local matchings in each component. '
      'Every edge belongs to exactly two of them. Three equal-colored edges '
      'therefore have six total appearances across the four matchings. If every '
      'matching were non-rainbow, each would contain at least two of these edges, '
      'requiring at least eight appearances. This contradiction rules out a triple.')

    story.append(PageBreak())
    h('3. Characterizing all extremal partitions (continued)')
    p('<b>Two repeated pairs.</b> Let <i>P</i> and <i>Q</i> be the two doubleton '
      'color classes. A matching is non-rainbow exactly when it contains '
      '<i>P</i> or <i>Q</i> in full. A pair is contained in the following number '
      'of global perfect matchings:')
    table([['Pair position', 'Number of matchings'],
           ['Adjacent edges in one component', '0'],
           ['Opposite edges in one component', '2'],
           ['One edge in each component', '1']], [310, 170])
    p('Adjacent edges cannot occur together. Opposite edges specify one local '
      'matching, leaving two choices in the other component. One edge in each '
      'component specifies both local choices and hence exactly one global matching.')
    p('Together, the two repeated pairs must obstruct all four matchings. Each '
      'obstructs at most two, so both must obstruct exactly two, and the obstructed '
      'sets must be disjoint. Thus each pair consists of opposite edges within '
      'one component. If the pairs belonged to different components, choosing the '
      'other local matching in each component would give a rainbow global matching.')
    p('Both pairs must therefore lie in the same component. Because the color '
      'classes are disjoint, they are precisely its two alternating perfect '
      'matchings. There are exactly two choices for that component; the other '
      'component has four singleton classes. Each choice avoids a rainbow matching, '
      'and the choices define different fixed-edge partitions. Renaming or '
      'interchanging colors adds no further partitions. Thus the count is two. ∎')
    h('4. Small cases and computational checks')
    table([['Host', 'Maximum colors', 'Extremal partitions'],
           ['C<sub>4</sub>', '2', '1'], ['C<sub>6</sub>', '4', '9'],
           ['C<sub>8</sub>', '6', '36'], ['C<sub>10</sub>', '8', '100'],
           ['Two disjoint C<sub>4</sub>s', '6', '2']], [200, 140, 140])
    p('All entries follow from the proofs. The repository’s documented sparse '
      'search also checks the three cycles through eight edges and the disjoint '
      'squares, agreeing with these formulas. The C<sub>10</sub> row is a proof '
      'consequence; no additional computation is claimed here. Computation is '
      'not a premise of any theorem in this note.')
    p('For the edge order, raw partitions, reproduction commands, and execution '
      'limits, see <link href="https://github.com/Akhil-rav/discrete-math-lab/pull/1" '
      'color="#19354a">Discrete Math Lab, PR #1</link> and the files '
      '<i>results/data/sparse_rainbow.json</i> and <i>results/sparse_verification.md</i>. '
      'The counts concern color partitions on fixed edges, not graph isomorphism classes.')

    def page(canvas, doc):
        canvas.saveState()
        w, h = doc.pagesize
        canvas.setStrokeColor(colors.HexColor('#cbd4da'))
        canvas.setLineWidth(.4)
        canvas.line(54, 39, w-54, 39)
        canvas.setFont('Paper', 8)
        canvas.setFillColor(GRAY)
        canvas.drawString(54, 26, 'Discrete Math Lab | Elementary exposition')
        canvas.drawRightString(w-54, 26, str(doc.page))
        canvas.restoreState()

    destination.parent.mkdir(parents=True, exist_ok=True)
    doc = SimpleDocTemplate(str(destination), pagesize=(612, 792),
                            leftMargin=60, rightMargin=60, topMargin=43, bottomMargin=53,
                            title='Rainbow perfect matchings on even cycles and two disjoint squares',
                            author='Akhil Ravuri', subject='Elementary combinatorics exposition')
    doc.build(story, onFirstPage=page, onLaterPages=page)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--font-dir', type=Path, default=Path('C:/Windows/Fonts'))
    parser.add_argument('--output', type=Path, default=ROOT/'papers/cycle_extremizers.pdf')
    args = parser.parse_args()
    build(args.font_dir, args.output)
    print(args.output)
