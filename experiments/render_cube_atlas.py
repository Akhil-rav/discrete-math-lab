"""Render the checked cube-classification data as a labeled SVG and LaTeX atlas.

Run: python -m experiments.render_cube_atlas
This renderer does not establish the classification; see classify_cube and tests.
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PALETTE = ['B4472D', '2765A1', '29835A', '86519B', 'B27B18', '566779', '007E87']
LEFT = [(0, 0, 0), (0, 1, 1), (1, 0, 1), (1, 1, 0)]
BITS = LEFT + [tuple(1-b for b in p) for p in LEFT]


def coordinates(bits):
    x, y, z = bits
    # Nested-square planar drawing: all twelve cube edges remain uncrossed.
    return (0.55+0.9*x, 0.55+0.9*y) if z else (2*x, 2*y)


def render(data):
    classes = data['classes']
    edges = data['edges']
    svg = ['<svg xmlns="http://www.w3.org/2000/svg" width="1050" height="1060" viewBox="0 0 1050 1060">',
           '<rect width="1050" height="1060" fill="white"/>',
           '<g font-family="Arial,sans-serif" fill="#19354A">',
           '<text x="35" y="45" font-size="27" font-weight="bold">Nine symmetry classes of cube colorings</text>',
           '<text x="35" y="76" font-size="16">174 fixed-edge partitions · 7 colors · all 48 cube automorphisms · color names ignored</text>']
    tikz = []
    for c in classes:
        cid = c['class_id']
        col, row = (cid-1)%3, (cid-1)//3
        ox, oy = 35+col*340, 105+row*310
        svg += [f'<g transform="translate({ox},{oy})">',
                '<rect width="320" height="290" rx="8" fill="#F8FAFC" stroke="#D8E1E7"/>',
                f'<text x="15" y="28" font-size="18" font-weight="bold">Class {cid}</text>',
                f'<text x="15" y="50" font-size="13">Orbit {c["orbit_size"]} · Stabilizer {c["stabilizer_size"]}</text>']
        positions = [(65+78*x, 238-78*y) for x,y in map(coordinates, BITS)]
        # All edges first, labels afterwards: vertex labels remain readable.
        for i,(u,v) in enumerate(edges):
            a,b = positions[u],positions[4+v]
            color=PALETTE[c['representative'][i]]
            svg.append(f'<line x1="{a[0]}" y1="{a[1]}" x2="{b[0]}" y2="{b[1]}" stroke="#{color}" stroke-width="3.5"/>')
        for i,(u,v) in enumerate(edges):
            a,b=positions[u],positions[4+v]
            x,y=(a[0]+b[0])/2,(a[1]+b[1])/2
            color=c['representative'][i]
            svg += [f'<circle cx="{x}" cy="{y}" r="9" fill="white"/>',
                    f'<text x="{x}" y="{y+4}" text-anchor="middle" font-size="13" font-weight="bold" fill="#{PALETTE[color]}">{color}</text>']
        for v,(x,y) in enumerate(positions):
            label=('L' if v<4 else 'R')+str(v%4)
            svg += [f'<circle cx="{x}" cy="{y}" r="4" fill="#19354A"/>',
                    f'<rect x="{x-27}" y="{y-20}" width="21" height="12" fill="#F8FAFC"/>',
                    f'<text x="{x-7}" y="{y-9}" text-anchor="end" font-size="11">{label}</text>']
        sizes=','.join(map(str,c['color_class_sizes']))
        svg += [f'<text x="15" y="275" font-size="13">Class sizes: {sizes}</text>', '</g>']
        tikz.append(r'\begin{minipage}[t]{0.32\linewidth}\centering')
        tikz.append(r'\textbf{Class '+str(cid)+r'}\quad {\small $|O|='+str(c['orbit_size'])+r'$, $|S|='+str(c['stabilizer_size'])+r'$}\par\smallskip')
        tikz.append(r'\begin{tikzpicture}[scale=1.4,every node/.style={font=\scriptsize}]')
        for v,bits in enumerate(BITS):
            x,y=coordinates(bits)
            tikz.append(f'\\coordinate (v{v}) at ({x},{y});')
        for i,(u,v) in enumerate(edges):
            color=c['representative'][i]
            tikz.append(f'\\draw[line width=1.2pt,draw=c{color}] (v{u}) -- node[fill=white,inner sep=1pt,text=c{color}] {{{color}}} (v{4+v});')
        for v in range(8):
            name=('L' if v<4 else 'R')+str(v%4)
            tikz.append(f'\\fill[ink] (v{v}) circle (1.7pt);')
            tikz.append(f'\\node[above left,fill=white,inner sep=0.6pt,text=ink] at (v{v}) {{{name}}};')
        tikz.append(r'\end{tikzpicture}\par{\scriptsize Sizes: $'+sizes+r'$}\end{minipage}')
        tikz.append(r'\par\vspace{1.1em}' if cid%3==0 else r'\hfill')
    svg += ['<text x="35" y="1042" font-size="14">Edge numerals specify color equality; palette choices are only for display. Vertex labels are fixed.</text>', '</g></svg>']
    figures=ROOT/'results/figures'
    figures.mkdir(exist_ok=True)
    (figures/'cube_classes.svg').write_text('\n'.join(svg)+'\n', encoding='utf-8', newline='\n')
    table=[]
    for c in classes:
        table.append(f'{c["class_id"]} & \\texttt{{'+''.join(map(str,c['representative']))+'} & $'+','.join(map(str,c['color_class_sizes']))+f'$ & {c["orbit_size"]} & {c["stabilizer_size"]}'+r' \\')
    preamble=r'''\documentclass[11pt,letterpaper]{article}
\usepackage[margin=1in,headheight=14pt]{geometry}
\usepackage[T1]{fontenc}\usepackage{lmodern}
\usepackage{amsmath,amssymb,microtype,booktabs,tikz,xcolor,fancyhdr}
\definecolor{ink}{HTML}{19354A}
\usepackage[colorlinks=true,urlcolor=ink,linkcolor=ink]{hyperref}
\hypersetup{pdftitle={Nine symmetry classes of extremal cube colorings},pdfauthor={Akhil Ravuri}}
\pagestyle{fancy}\fancyhf{}\fancyhead[L]{\small\textsc{Extremal cube colorings}}
\fancyhead[R]{\small Akhil Ravuri}\fancyfoot[C]{\thepage}
\renewcommand{\headrulewidth}{0.3pt}\setlength{\parskip}{0.25em}\setlength{\emergencystretch}{1em}
'''
    preamble+='\n'.join(f'\\definecolor{{c{i}}}{{HTML}}{{{p}}}' for i,p in enumerate(PALETTE))
    body=r'''
\title{\vspace{-1.5em}\LARGE\bfseries Nine symmetry classes\\of extremal cube colorings}
\author{Akhil Ravuri}\date{}
\begin{document}\maketitle\vspace{-1.5em}
\begin{abstract}
An exact search partitions the 174 seven-color edge partitions of the cube
that avoid rainbow perfect matchings into nine classes under graph
automorphisms and color renaming. We list canonical representatives, orbit
sizes, stabilizers, and labeled diagrams. A separate vertex-permutation
oracle checks the symmetry group. This is a finite computational study;
no novelty is claimed.
\end{abstract}
\section{Host, equivalence, and result}
Write the cube $Q_3$ as $K_{4,4}$ with the diagonal matching deleted.
The two parts are $\{L_0,\ldots,L_3\}$ and $\{R_0,\ldots,R_3\}$.
An edge $L_iR_j$ exists exactly when $i\ne j$.
Edges are ordered lexicographically by $(i,j)$.
Thus a representative below is a string of twelve colors in row-major order,
omitting diagonal positions. Color names are normalized by first appearance.
Colorings need not be proper. A perfect matching is rainbow if its four
edges have distinct colors.

The existing full partition search establishes a maximum avoiding count of
seven, attained by 174 fixed-edge partitions. Here we independently enumerate
all $S(12,7)=627{,}396$ partitions into exactly seven classes and recover the
same 174 avoiding partitions. Quotienting by cube symmetry gives:
\begin{center}\small
\begin{tabular}{clcrr}\toprule
Class & Representative & Color-class sizes & Orbit & Stabilizer\\\midrule
'''
    body+='\n'.join(table)
    body+=r'''
\bottomrule\end{tabular}\end{center}
The orbit sizes sum to $174$; each orbit size times its stabilizer is $48$.
\section{Why the group has order 48}
The cube is connected and bipartite, so an automorphism preserves its two
parts or exchanges them. If it preserves them, write its relabelings as
$i\mapsto\sigma(i)$ on the left and $j\mapsto\tau(j)$ on the right.
The missing diagonal edges must remain missing, forcing $\sigma(i)=\tau(i)$.
Conversely every simultaneous permutation preserves adjacency. There are
$4!$ such maps. Exchanging the parts gives the other $4!$, for $48$ in total.

\newpage
\section{A labeled representative of every class}
In these drawings the left vertices correspond to binary strings
$000,011,101,110$; $R_i$ corresponds to the bitwise complement of $L_i$.
Edges therefore join strings differing in one coordinate. Numerals on edges
are color labels, not weights. Each panel uses its own palette.
Here $O$ denotes the orbit and $S$ its partition stabilizer.
\begin{center}
'''
    body+='\n'.join(tikz)
    body+=r'''
\end{center}
The displayed labels determine the partitions exactly, including when two
edge colors are visually similar. Vertices are identified across panels by
their labels; equivalence in the table permits all 48 cube automorphisms.

\newpage
\section{Structure and verification}
The first three classes all have color-class sizes $(6,1,1,1,1,1,1)$.
They are nevertheless inequivalent: the sorted vertex-degree sequences of
their six-edge color classes are respectively
\[
 (3,3,2,2,1,1,0,0),\quad
 (3,3,1,1,1,1,1,1),\quad
 (2,2,2,2,2,2,0,0).
\]
The second consists of two disjoint three-edge stars; the third is a
six-cycle. All vertex degrees above are in the monochromatic subgraph,
with isolated vertices retained. Degree sequences are graph invariants, so
these three classes cannot be identified by a cube automorphism.

Other repeated size profiles also conceal differences. Among the nine perfect
matchings, class 4 always has color multiplicities $(2,1,1)$, whereas class 5
has one matching with multiplicities $(3,1)$. Classes 6, 7, and 8 have the
same block sizes, but their exceptional matching profiles are respectively
none, $(2,2)$, and $(4)$. Thus class 8 contains a monochromatic perfect
matching. These are properties of the recorded finite classes, not general
classification theorems for larger graphs.

\subsection*{Coverage and checks}
Restricted-growth strings with exactly seven blocks are enumerated without
rainbow-prefix pruning. Their total is checked against the independent
recurrence, starting from $S(0,0)=1$ and zero outside the admissible range:
\[
 S(n,k)=kS(n-1,k)+S(n-1,k-1).
\]
Each candidate is tested against all
nine perfect matchings. Each orbit is formed explicitly, normalized by color
renaming, and removed from the remaining population. The computation checks
disjointness, closure in the avoiding population, and orbit--stabilizer counts.

Tests separately enumerate all $8!$ vertex bijections and retain exactly
the adjacency-preserving maps. Their edge actions equal the 48 constructed
actions. All four-edge subsets independently reconstruct the perfect
matchings. A direct equal-color-pair test validates every saved orbit member;
the earlier full search independently supplies the maximum and population
count. These are implementation checks, not external refereeing.

\subsection*{Reproduction and interpretation}
From the repository root, with Python 3.11 or later:
\begin{quote}\small\ttfamily
python -m experiments.classify\_cube\par
python -m unittest discover -s tests -v
\end{quote}
The full dataset in \texttt{results/data/cube\_classification.json} includes
all 174 members, the edge order, and the nine matching constraints. The SVG
atlas and this source are regenerated by
\texttt{python -m experiments.render\_cube\_atlas}.
The detailed project report records provenance and the limited literature
search. No assertion of originality or currently open status follows from
this computation. The diagrams illustrate the classification; they do not
replace its enumerative coverage argument.
\end{document}
'''
    (ROOT/'papers/cube_classification.tex').write_text(preamble+body, encoding='utf-8', newline='\n')


if __name__ == '__main__':
    render(json.loads((ROOT/'results/data/cube_classification.json').read_text(encoding='utf-8')))
    print('Rendered SVG atlas and LaTeX source from cube_classification.json.')
