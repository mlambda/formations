print(
    """\\documentclass[beamer,crop,tikz]{standalone}

\\usepackage{formation}

\\begin{document}
  \\begin{tikzpicture}[transparent/.style={text opacity=1, text=black}]"""
)
words = ["<GO>", "Que", "fais", "tu", "<STOP>"]
i_opacities = [1, 0, 0, 0]
h_opacities = [1, 1, 1, 1]
o_opacities = [0, 1, 0, 1]
for i, (previous_word, word, i_o, h_o, o_o) in enumerate(
    zip(words, words[1:], i_opacities, h_opacities, o_opacities)
):
    i2h = r"$\circ$" if i_o + h_o == 2 else "---"
    h2o = r"$\circ$" if h_o + o_o == 2 else "---"
    print(
        f"""
    \\node[hencoder, transparent, fill opacity={h_o}] (H{i}) at ({i * 1.5}, 1) {{$h_{i}$}};
    \\node[output, transparent, fill opacity={o_o}] (O{i}) at ({i * 1.5}, 2) {{$y_{i}$}};
    \\node[input, transparent, fill opacity={i_o}] (WE{i}) at ({i * 1.5}, 0) {{$x_{i}$}};
    \\node[anchor=mid] (TI{i}) at ({i * 1.5}, -1) {{{previous_word}}};
    \\node[anchor=mid] (TO{i}) at ({i * 1.5}, 3) {{{word}}};
    \\path (WE{i}) -- (H{i}) node [midway] {{{i2h}}};
    \\path (H{i}) -- (O{i}) node [midway] {{{h2o}}};
    \\draw[densely dotted] (TI{i}) -- (WE{i});
    \\draw[densely dotted] (O{i}) -- (TO{i});
    \\draw[color=gray] ({i * 1.5 - 0.5}, -1.4)
      -- ({i * 1.5 - 0.5}, -1.5)
      -- ({i* 1.5 + 0.5}, -1.5) node [below, midway] {{$t_{i}$}}
      -- ({i* 1.5 + 0.5}, -1.4);
"""
    )
for i, (i_o, j_o) in enumerate(zip(h_opacities, h_opacities[1:])):
    i2i = r"$\circ$" if i_o + j_o == 2 else "---"
    print(f"    \\path (H{i}) -- (H{i + 1}) node [midway] {{{i2i}}};")
print(
    """
  \end{tikzpicture}
\end{document}
"""
)
