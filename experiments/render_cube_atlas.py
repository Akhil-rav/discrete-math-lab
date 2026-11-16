"""Render the checked cube-classification data as a labeled SVG and LaTeX atlas.

Run: python -m experiments.render_cube_atlas
The paper text is in papers/templates/cube_classification.tex.in.
"""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PALETTE = ["B4472D", "2765A1", "29835A", "86519B", "B27B18", "566779", "007E87"]
LEFT = [(0, 0, 0), (0, 1, 1), (1, 0, 1), (1, 1, 0)]
BITS = LEFT + [tuple(1 - b for b in p) for p in LEFT]


def coordinates(bits):
    x, y, z = bits
    # Nested-square planar drawing: all twelve cube edges remain uncrossed.
    return (0.55 + 0.9 * x, 0.55 + 0.9 * y) if z else (2 * x, 2 * y)


def render(data):
    classes = data["classes"]
    edges = data["edges"]
    svg = [
        '<svg xmlns="http://www.w3.org/2000/svg" width="1050" height="1060" viewBox="0 0 1050 1060">',
        '<rect width="1050" height="1060" fill="white"/>',
        '<g font-family="Arial,sans-serif" fill="#19354A">',
        '<text x="35" y="45" font-size="27" font-weight="bold">Nine symmetry classes of cube colorings</text>',
        '<text x="35" y="76" font-size="16">174 fixed-edge partitions · 7 colors · all 48 cube automorphisms · color names ignored</text>',
    ]
    tikz = []
    for c in classes:
        cid = c["class_id"]
        col, row = (cid - 1) % 3, (cid - 1) // 3
        ox, oy = 35 + col * 340, 105 + row * 310
        svg += [
            f'<g transform="translate({ox},{oy})">',
            '<rect width="320" height="290" rx="8" fill="#F8FAFC" stroke="#D8E1E7"/>',
            f'<text x="15" y="28" font-size="18" font-weight="bold">Class {cid}</text>',
            f'<text x="15" y="50" font-size="13">Orbit {c["orbit_size"]} · Stabilizer {c["stabilizer_size"]}</text>',
        ]
        positions = [(65 + 78 * x, 238 - 78 * y) for x, y in map(coordinates, BITS)]
        # All edges first, labels afterwards: vertex labels remain readable.
        for i, (u, v) in enumerate(edges):
            a, b = positions[u], positions[4 + v]
            color = PALETTE[c["representative"][i]]
            svg.append(
                f'<line x1="{a[0]}" y1="{a[1]}" x2="{b[0]}" y2="{b[1]}" stroke="#{color}" stroke-width="3.5"/>'
            )
        for i, (u, v) in enumerate(edges):
            a, b = positions[u], positions[4 + v]
            x, y = (a[0] + b[0]) / 2, (a[1] + b[1]) / 2
            color = c["representative"][i]
            svg += [
                f'<circle cx="{x}" cy="{y}" r="9" fill="white"/>',
                f'<text x="{x}" y="{y+4}" text-anchor="middle" font-size="13" font-weight="bold" fill="#{PALETTE[color]}">{color}</text>',
            ]
        for v, (x, y) in enumerate(positions):
            label = ("L" if v < 4 else "R") + str(v % 4)
            svg += [
                f'<circle cx="{x}" cy="{y}" r="4" fill="#19354A"/>',
                f'<rect x="{x-27}" y="{y-20}" width="21" height="12" fill="#F8FAFC"/>',
                f'<text x="{x-7}" y="{y-9}" text-anchor="end" font-size="11">{label}</text>',
            ]
        sizes = ",".join(map(str, c["color_class_sizes"]))
        svg += [
            f'<text x="15" y="275" font-size="13">Class sizes: {sizes}</text>',
            "</g>",
        ]
        tikz.append(r"\begin{minipage}[t]{0.32\linewidth}\centering")
        tikz.append(
            r"\textbf{Class "
            + str(cid)
            + r"}\quad {\small $|O|="
            + str(c["orbit_size"])
            + r"$, $|S|="
            + str(c["stabilizer_size"])
            + r"$}\par\smallskip"
        )
        tikz.append(
            r"\begin{tikzpicture}[scale=1.4,every node/.style={font=\scriptsize}]"
        )
        for v, bits in enumerate(BITS):
            x, y = coordinates(bits)
            tikz.append(f"\\coordinate (v{v}) at ({x:g},{y:g});")
        for i, (u, v) in enumerate(edges):
            color = c["representative"][i]
            tikz.append(
                f"\\draw[line width=1.2pt,draw=c{color}] (v{u}) -- node[fill=white,inner sep=1pt,text=c{color}] {{{color}}} (v{4+v});"
            )
        for v in range(8):
            name = ("L" if v < 4 else "R") + str(v % 4)
            tikz.append(f"\\fill[ink] (v{v}) circle (1.7pt);")
            tikz.append(
                f"\\node[above left,fill=white,inner sep=0.6pt,text=ink] at (v{v}) {{{name}}};"
            )
        tikz.append(
            r"\end{tikzpicture}\par{\scriptsize Sizes: $" + sizes + r"$}\end{minipage}"
        )
        tikz.append(r"\par\vspace{1.1em}" if cid % 3 == 0 else r"\hfill")
    svg += [
        '<text x="35" y="1042" font-size="14">Edge numerals specify color equality; palette choices are only for display. Vertex labels are fixed.</text>',
        "</g></svg>",
    ]
    figures = ROOT / "results/figures"
    figures.mkdir(exist_ok=True)
    (figures / "cube_classes.svg").write_text(
        "\n".join(svg) + "\n", encoding="utf-8", newline="\n"
    )
    table = []
    for c in classes:
        table.append(
            f'{c["class_id"]} & \\texttt{{'
            + "".join(map(str, c["representative"]))
            + "} & $"
            + ",".join(map(str, c["color_class_sizes"]))
            + f'$ & {c["orbit_size"]} & {c["stabilizer_size"]}'
            + r" \\"
        )
    template = (ROOT / "papers/templates/cube_classification.tex.in").read_text(
        encoding="utf-8"
    )
    colors = "\n".join(
        f"\\definecolor{{c{i}}}{{HTML}}{{{color}}}" for i, color in enumerate(PALETTE)
    )
    paper = template.replace("@@COLORS@@", colors)
    paper = paper.replace("@@TABLE@@", "\n".join(table))
    paper = paper.replace("@@DIAGRAMS@@", "\n".join(tikz))
    (ROOT / "papers/cube_classification.tex").write_text(
        paper, encoding="utf-8", newline="\n"
    )


if __name__ == "__main__":
    render(
        json.loads(
            (ROOT / "results/data/cube_classification.json").read_text(encoding="utf-8")
        )
    )
    print("Rendered SVG atlas and LaTeX source from cube_classification.json.")
