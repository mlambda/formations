print(
    r"""\documentclass[beamer,crop,tikz]{standalone}
\usepackage{formation}
\begin{document}
  \begin{tikzpicture}[transparent/.style={text opacity=1, text=black}]"""
)

words = ["J", "ai", "vraiment", "adoré", "ce", "film", "il", "est", "super"]

for i, word in enumerate(words):
    i_o = i / (len(words) + 1)
    h_o = (i + 1) / (len(words) + 1)
    print(
        f"""
    \\node[hencoder, transparent, fill opacity={h_o}] (H{i}) at ({i * 1.5}, 1) {{$h_{i}$}};
    \\node[input, transparent, fill opacity={i_o}] (WE{i}) at ({i * 1.5}, 0) {{$x_{i}$}};
    \\node[anchor=mid] (TI{i}) at ({i * 1.5}, -1) {{{word}}};
    \\draw[->] (WE{i}) -- (H{i});
    \\draw[densely dotted] (TI{i}) -- (WE{i});
    \\draw[color=gray] ({i* 1.5 - 0.5}, -1.4)
      -- ({i * 1.5 - 0.5}, -1.5)
      -- ({i* 1.5 + 0.5}, -1.5) node [below, midway] {{$t_{i}$}}
      -- ({i* 1.5 + 0.5}, -1.4);"""
    )
for i in range(len(words) - 1):
    print(
        f"""
    \\draw[->] (H{i}) -- (H{i + 1});"""
    )

print(
    f"""
    \\node[output] (O) at ({(len(words) - 1) * 1.5}, 2) {{$y$}};
    \\node[anchor=mid] (TO) at ({(len(words) - 1) * 1.5}, 3) {{Positif}};
    \\draw[->] (H{len(words) - 1}) -- (O);
    \\draw[densely dotted] (O) -- (TO);
  \\end{{tikzpicture}}
\\end{{document}}
"""
)
