print(
    """\\documentclass[beamer,crop,tikz]{standalone}

\\usepackage{formation}

\\begin{document}
  \\begin{tikzpicture}[transparent/.style={text opacity=1, text=black}]"""
)
words = ["<GO>", "How", "are", "you", "<STOP>"]
for i, (previous_word, word) in enumerate(zip(words, words[1:])):
    i_opacity = 1 if not i else 0
    h_opacity = 0.5 - i * 0.4 / (len(words) - 2)
    o_opacity = 0.45 - i * 0.4 / (len(words) - 2)
    print(
        f"""
    \\node[hencoder, transparent, fill opacity={h_opacity}] (H{i}) at ({i * 1.5}, 1) {{$h_{i}$}};
    \\node[output, transparent, fill opacity={o_opacity}] (O{i}) at ({i * 1.5}, 2) {{$y_{i}$}};
    \\node[input, transparent, fill opacity={i_opacity}] (WE{i}) at ({i * 1.5}, 0) {{$x_{i}$}};
    \\node[anchor=mid] (TI{i}) at ({i * 1.5}, -1) {{{previous_word}}};
    \\node[anchor=mid] (TO{i}) at ({i * 1.5}, 3) {{{word}}};
    \\draw[->] (WE{i}) -- (H{i});
    \\draw[->] (H{i}) -- (O{i});
    \\draw[densely dotted] (TI{i}) -- (WE{i});
    \\draw[densely dotted] (O{i}) -- (TO{i});
    \\draw[color=gray] ({i * 1.5 - 0.5}, -1.4)
      -- ({i * 1.5 - 0.5}, -1.5)
      -- ({i* 1.5 + 0.5}, -1.5) node [below, midway] {{$t_{i}$}}
      -- ({i* 1.5 + 0.5}, -1.4);
"""
    )
for i in range(len(words) - 2):
    print(f"    \\draw[->] (H{i}) -- (H{i + 1});")
print(
    """
  \end{tikzpicture}
\end{document}
"""
)
