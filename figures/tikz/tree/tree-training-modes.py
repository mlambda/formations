import numpy as np
NB_DOTS=30


print(r"""\documentclass[beamer,crop,tikz]{standalone}
\usepackage{formation}
\newcommand{\tree}{\includegraphics[scale=0.15]{tikz/sub-img/empty-tree.pdf}}
\tikzset{boxD/.style={
  dashed,
  very thick,
  DeepSpaceSparkle,
  }}
\tikzset{point/.style={
  circle,fill,inner sep=0.1
  }}
\tikzset{pointW/.style={
  point,draw=DeepSpaceSparkle,
  fill=DeepSpaceSparkle
  }}
\tikzset{pointG/.style={
  point,draw=Rosewood,
  fill=Rosewood
  }}
\tikzset{arrowZ/.style={
  ->,>=stealth,
  very thick,
  Rosewood
  }}  
\tikzset{circleZ/.style={
  draw=Rosewood,
  very thick,
  }} 
\tikzset{textZ/.style={
  DeepSpaceSparkle,
  }}  
  

\begin{document}
  \begin{tikzpicture}""")

# SINGLE
print(r"""
\node[textZ] at (1.35,4.5) {\LARGE \textbf{single}};
\node[textZ] at (1.35,-5.5) {\large 1 interation};
\draw[boxD] (-1.5,4.2) rectangle (4.2,-6);
\draw[circleZ] (0,0) circle (1);
""")
pos=np.random.uniform(-1,1,size=(100,2))
pos=pos[np.hypot(pos[:,0],pos[:,1])<=1][:NB_DOTS]
pos=pos*0.9
for coord in pos:
  print(f"\\node[pointG] at ($(0,0)+({coord[0]:.2f},{coord[1]:.2f})$){{}};") 


print(r"""
\node at (3,0) {\tree};
\draw[arrowZ] (1,0) -- (2,0);
""")

# BAGGING
print(r"""
\node[textZ] at (8.05,4.5) {\LARGE \textbf{bagging}};
\node[textZ] at (8.05,-5.5) {\large parallel};
\draw[boxD] (4.6,4.2) rectangle (11.5,-6);
      """)
for x in [3,0,-4]:
  print(f"""
  \\draw[circleZ] (7,{x}) circle (1);
  """)
  for i,coord in enumerate(pos):
    if np.random.randint(2):
      print(f"\\node[pointG] at ($(7,{x})+({coord[0]:.2f},{coord[1]:.2f})$){{}};") 
    else:
      print(f"\\node[pointW] at ($(7,{x})+({coord[0]:.2f},{coord[1]:.2f})$){{}};") 
  print(f"""
    \\node at (10,{x}) {{\\tree}};\n
    \\draw[arrowZ] (8,{x}) -- (9,{x});
    \\draw[arrowZ] (5.5,0) |- (6,{x});
  """)
print(r"""
\node[textZ] at (8.5,-2) {...};
""")

# BOOSTING
print(r"""
\node[textZ] at (15.2,4.5) {\LARGE \textbf{boosting}};
\node[textZ] at (15.2,-5.5) {\large sequential};
\draw[boxD] (11.9,4.2) rectangle (18.5,-6);
      """)
dot_sizes=np.random.uniform(0.1,1.2,size=NB_DOTS)
for i,x in enumerate([3,0,-4]):
  print(f"""
  \\draw[circleZ] (14,{x}) circle (1);
  \\node at ($(14,{x})+(0,1)$) (topC{i}) {{}};
  """)
  for coord,ds in zip(pos,dot_sizes):
    if np.random.randint(2):
      print(f"\\node[pointG,inner sep={ds:.2f}pt] at ($(14,{x})+({coord[0]:.2f},{coord[1]:.2f})$) {{}};") 
    else:
      print(f"\\node[pointW,inner sep={ds:.2f}pt] at ($(14,{x})+({coord[0]:.2f},{coord[1]:.2f})$) {{}};") 
  print(f"""
  \\node at (17,{x}) (boost{i}) {{\\tree}};\n
  \\draw[arrowZ] (15,{x}) -- (16,{x});
  """)
print(r"""
\node[textZ] at (15.2,-2) (dots) {...};
\draw[arrowZ] (12.5,3) -- (13,3);

\draw[arrowZ] (boost0) -- (topC1);
\draw[arrowZ] (boost1) -- (dots);
\draw[arrowZ] (dots) -- (topC2);
""")


print(r"""
\end{tikzpicture}
\end{document}
  """)
