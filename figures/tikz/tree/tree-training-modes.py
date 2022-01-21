import numpy as np

print(r"""\documentclass[beamer,crop,tikz]{standalone}
\usepackage{formation}
\newcommand{\tree}{\includegraphics[scale=0.15]{tikz/sub-img/empty-tree.pdf}}
\tikzset{point/.style={
  circle,fill,inner sep=0.1
  }}
\tikzset{pointW/.style={
  point,draw=black,
  fill=black
  }}
\tikzset{pointG/.style={
  point,draw=red,
  fill=red
  }}
\begin{document}
  \begin{tikzpicture}""")

# SINGLE
print(r"""
\draw (0,0) circle (1);
""")
pos=np.random.uniform(-1,1,size=(100,2))
pos=pos[np.hypot(pos[:,0],pos[:,1])<=1][:50]
pos=pos*1
for coord in pos:
  print(f"\\node[pointG] at ($(0,0)+({coord[0]:.2f},{coord[1]:.2f})$){{}};") 


print(r"""
\node at (3,0) {\tree};
\draw[->,>=stealth] (1,0) -- (2,0);
""")

# BAGGING
for x in [3,0,-4]:
  print(f"""
  \\draw (7,{x}) circle (1);
  """)
  for i,coord in enumerate(pos):
    if np.random.randint(2):
      print(f"\\node[pointG] at ($(7,{x})+({coord[0]:.2f},{coord[1]:.2f})$){{}};") 
    else:
      print(f"\\node[pointW] at ($(7,{x})+({coord[0]:.2f},{coord[1]:.2f})$){{}};") 
  print(f"""
    \\node at (10,{x}) {{\\tree}};\n
    \\draw[->,>=stealth] (8,{x}) -- (9,{x});
    \\draw[->,>=stealth] (5,0) |- (6,{x});
  """)
print(r"""
\node at (8.5,-2) {...};
""")

# BOOSTING

for x in [3,0,-4]:
  print(f"""
  \\draw (14,{x}) circle (1);
  """)
  for i,coord in enumerate(pos):
    if np.random.randint(2):
      print(f"\\node[pointG] at ($(14,{x})+({coord[0]:.2f},{coord[1]:.2f})$){{}};") 
    else:
      print(f"\\node[pointW] at ($(14,{x})+({coord[0]:.2f},{coord[1]:.2f})$){{}};") 
  print(f"""
    \\node at (17,{x}) {{\\tree}};\n
    \\draw[->,>=stealth] (15,{x}) -- (16,{x});
  """)
print(r"""
\node at (8.5,-2) {...};
\draw[->,>=stealth] (12.5,3) -- (13,3);
""")


print(r"""  \end{tikzpicture}
\end{document}""")
