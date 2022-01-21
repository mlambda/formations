print(
    r"""\documentclass[beamer,crop,tikz]{standalone}
\usepackage{formation}
\begin{document}
  \begin{tikzpicture}[x=2cm,transparent/.style={text opacity=1, text=black}]"""
)

for y in range(1,5):
    print(rf"""\node[input] (I{y}) at (0, {3 - y}) {{$X_{y}$}};""")

for h in range(1,7):
    for y in range(1,5):
        op = h/6
        print(rf"""\node[hencoder, transparent, fill opacity={op}] (H{h}{y}) at ({h}, {3 - y}) {{}};""")    

for y in range(1,5):
    print(rf"""\node[output] (O{y}) at (7, {3 - y}) {{$O_{y}$}};""")

for i in range(1,5):
    for j in range(1,5):
        print(rf"""\draw[->,>=stealth] (I{i}.east) to (H1{j}.west);""")

for h in range(1,6):
    for i in range(1,5):
        for j in range(1,5):
            print(rf"""\draw[->,>=stealth] (H{h}{i}.east) to (H{h+1}{j}.west);""")
    

for i in range(1,5):
    for j in range(1,5):
        print(rf"""\draw[->,>=stealth] (H6{i}.east) to (O{j}.west);""")

print(
    rf"""
  \end{{tikzpicture}}
\end{{document}}
"""
)
