print(r"""
\documentclass[beamer,crop,tikz]{standalone}

\usepackage{formation}
\tikzset{ylayer/.style={
  hencoder,
  minimum width=0.5cm,
  fill=MediumChampagne!50!black,
  circle,
  text=white,
  draw=MediumChampagne!75!black}}
\tikzset{vlayer/.style={
  hencoder,
  minimum width=0.5cm,
  circle,
  fill=DeepSpaceSparkle,
  text=white,
  draw=DeepSpaceSparkle!50}}
\tikzset{wlayer/.style={
  hencoder,
  minimum width=0.5cm,
  circle,
  fill=IndianYellow,
  text=white,
  draw=IndianYellow!50}}
\tikzset{zlayer/.style={
  hencoder,
  minimum width=0.5cm,
  circle,
  text=white,}}


\begin{document}
  \begin{tikzpicture}[x=1.5cm]
  """)
# FIRST ENCODER
# Nodes
for i in range(8):
    print(fr"""\node[ylayer] (Yinput{i}) at (0, 4.5 - {i}) {{}};""")
for i in range(6):
    print(fr"""\node[vlayer] (V{i}) at (1, 3.5 - {i}) {{}};""")
for i in range(8):
    print(fr"""\node[ylayer] (Yhat{i}) at (2, 4.5 - {i}) {{}};""")

# Arrows
for i in range(8):
    for j in range(6):
        print(fr"""\draw[MediumChampagne!75!black] (Yinput{i}.east) to (V{j}.west);""")
for i in range(6):
    for j in range(8):
        print(fr"""\draw[DeepSpaceSparkle!50] (V{i}.east) to (Yhat{j}.west);""")

print(r"""
\node at (Yinput0) [above=0.75,text=MediumChampagne!50!black] {{$Y$}};
\node at (V0) [above=.75,text=Rosewood] {{$V$}};
\node at (Yhat0) [above=0.75,text=MediumChampagne!50!black] {{$\widehat{{Y}}$}};
""")

print(r"""\node at (2.5,1)  {{$\Rightarrow$}};""")

# SECOND ENCODER
# Nodes
for i in range(6):
    print(fr"""\node[vlayer] (Vinput{i}) at (3, 3.5 - {i}) {{}};""")
for i in range(4):
    print(fr"""\node[wlayer] (W{i}) at (4, 2.5 - {i}) {{}};""")
for i in range(6):
    print(fr"""\node[vlayer] (Vhat{i}) at (5, 3.5 - {i}) {{}};""")

# Arrows
for i in range(6):
    for j in range(4):
        print(fr"""\draw[DeepSpaceSparkle!50] (Vinput{i}.east) to (W{j}.west);""")
for i in range(4):
    for j in range(6):
        print(fr"""\draw[IndianYellow!50] (W{i}.east) to (Vhat{j}.west);""")

print(r"""
    \node at (Vinput0) [above=0.75,text=DeepSpaceSparkle] {{$V$}};
    \node at (W0) [above=0.75,text=IndianYellow] {{$W$}};
    \node at (Vhat0) [above=0.75,text=DeepSpaceSparkle] {{$\widehat{{V}}$}};
""")

print(r"""\node at (6,1)  {{$\dots$}};""")
# FINAL ENCODER
# Nodes
for i in range(8):
    print(fr"""\node[ylayer] (YinputF{i}) at (7, 4.5 - {i}) {{}};""")
for i in range(6):
    print(fr"""\node[vlayer] (VinputF{i}) at (8, 3.5 - {i}) {{}};""")
for i in range(4):
    print(fr"""\node[wlayer] (WinputF{i}) at (9, 2.5 - {i}) {{}};""")
for i in range(2):
    print(fr"""\node[zlayer] (Z{i}) at (10, 1.5 - {i}) {{}};""")
for i in range(4):
    print(fr"""\node[wlayer] (WhatF{i}) at (11, 2.5 - {i}) {{}};""")
for i in range(6):
    print(fr"""\node[vlayer] (VhatF{i}) at (12, 3.5 - {i}) {{}};""")
for i in range(8):
    print(fr"""\node[ylayer] (YhatF{i}) at (13, 4.5 - {i}) {{}};""")

# Arrows
for i in range(8):
    for j in range(6):
        print(fr"""\draw[MediumChampagne!75!black] (YinputF{i}.east) to (VinputF{j}.west);""")
for i in range(6):
    for j in range(4):
        print(fr"""\draw[DeepSpaceSparkle!50] (VinputF{i}.east) to (WinputF{j}.west);""")
for i in range(4):
    for j in range(2):
        print(fr"""\draw[IndianYellow!50] (WinputF{i}.east) to (Z{j}.west);""")
for i in range(2):
    for j in range(4):
        print(fr"""\draw[Rosewood!50] (Z{i}.east) to (WhatF{j}.west);""")
for i in range(4):
    for j in range(6):
        print(fr"""\draw[IndianYellow!50] (WhatF{i}.east) to (VhatF{j}.west);""")
for i in range(6):
    for j in range(8):
        print(fr"""\draw[DeepSpaceSparkle!50] (VhatF{i}.east) to (YhatF{j}.west);""")

print(r"""
    \node at (YinputF0) [above=0.75,text=DeepSpaceSparkle] {{$Y$}};
    \node at (VinputF0) [above=0.75,text=DeepSpaceSparkle] {{$V$}};
    \node at (WinputF0) [above=0.75,text=IndianYellow] {{$W$}};
    \node at (Z0) [above=0.75,text=Rosewood] {{$Z$}};
    \node at (WhatF0) [above=0.75,text=IndianYellow] {{$\widehat{{W}}$}};
    \node at (VhatF0) [above=0.75,text=DeepSpaceSparkle] {{$\widehat{{V}}$}};
    \node at (YhatF0) [above=0.75,text=MediumChampagne!75!black] {{$\widehat{{Y}}$}};
""")


print(r"""
  \end{tikzpicture}
\end{document}
""")
