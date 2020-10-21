\NeedsTeXFormat{LaTeX2e}

\ProvidesClass{formation}[2017/12/01 LaTeX class for my formations]

\PassOptionsToPackage{dvipsnames,hyperref,usenames,table}{xcolor}

\PassOptionsToPackage{hidelinks}{hyperref}

\DeclareOption*{\PassOptionsToClass{\CurrentOption}{beamer}}

\ProcessOptions\relax

\LoadClass{beamer}


\RequirePackage{xcolor}
\RequirePackage[export]{adjustbox}
\RequirePackage{amsmath}
\RequirePackage{amssymb}
\RequirePackage{tabularx}
\RequirePackage{booktabs}
\RequirePackage{etoolbox}
\RequirePackage{hyperref}
\RequirePackage{multicol}
\RequirePackage{minted}
\RequirePackage{graphicx}
\RequirePackage[numbers]{natbib}
\RequirePackage{forest}
\RequirePackage{bm}
\RequirePackage{soul}
\RequirePackage{stmaryrd}
\RequirePackage[french]{babel}

\DeclareGraphicsExtensions{.pdf,.png,.jpg,.jpeg}
\graphicspath{{./img/}}

\usetheme[block=fill,sectionpage=progressbar,subsectionpage=progressbar,progressbar=frametitle]{metropolis}
\setlength{\metropolis@progressinheadfoot@linewidth}{1pt}
\setbeamercolor{normal text}{bg=white}
\setbeamertemplate{bibliography item}{\insertbiblabel}
\setbeamertemplate{blocks}[rounded]

\makeatletter
\setlength{\metropolis@frametitle@padding}{1.9ex}% <- default 2.2 ex
\renewcommand{\metropolis@frametitlestrut@start}{%
  \rule{0pt}{\metropolis@frametitle@padding}%
}
\renewcommand{\metropolis@frametitlestrut@end}{%
  \rule[-\metropolis@frametitle@padding]{0pt}{\metropolis@frametitle@padding}%
}
\setbeamertemplate{frametitle}{%
    \nointerlineskip%
    \begin{beamercolorbox}[%
        wd=\paperwidth,%
        sep=0pt,%
        leftskip=\metropolis@frametitle@padding,%
        rightskip=\metropolis@frametitle@padding,%
        ]{frametitle}%
        \metropolis@frametitlestrut@start%
        \ifdefempty{\insertsectionhead}{}{%
          {%
            \scriptsize%
            \insertsectionhead%
            \ifdefempty{\insertsubsectionhead}{}{ > \insertsubsectionhead}%
            \newline%
          }%
        }%
        \insertframetitle%
        \nolinebreak%
        \metropolis@frametitlestrut@end%
    \end{beamercolorbox}
    \usebeamertemplate*{progress bar in head/foot}
}

\bibliographystyle{abbrv}

\newcommand{\partiald}[2]{\frac{\partial #1}{\partial #2}}
\DeclareMathOperator*{\argmin}{arg\,min}
\DeclareMathOperator*{\argmax}{arg\,max}
\DeclareMathOperator{\ReLU}{ReLU}
\DeclareMathOperator{\softmax}{softmax}
\DeclareMathOperator{\cov}{cov}
\DeclareMathOperator{\corr}{corr}
\DeclareMathOperator{\asym}{asym}
\DeclareMathOperator{\kurt}{kurt}
\DeclareMathOperator{\RNN}{RNN}
\DeclareMathOperator{\EC}{EC}
\DeclareMathOperator{\ECB}{ECB}
\DeclareMathOperator{\BCE}{BCE}
\DeclareMathOperator{\l1}{L1}
\DeclareMathOperator{\L2}{L2}
\DeclareMathOperator{\similarity}{sim}

\makeatletter
\let\UL\ul
\renewcommand\ul{%
  \let\set@color\beamerorig@set@color
  \let\reset@color\beamerorig@reset@color
  \UL}
\makeatother

\newcommand{\newlinebar}{%
  \noindent\makebox[\linewidth]{\rule{\paperwidth}{0.4pt}}\\%
}

\newcommand{\bluelink}[2]{%
  \href{%
    #1%
  }{%
    \color{blue}%
    \setulcolor{blue}%
    \ul{#2}%
  }%
}

\newcommand{\vect}[1]{\bm{\mathbf{#1}}}

\newcommand{\imgtw}[2][1]{%
  \begin{figure}%
    \centering%
    \includegraphics[width=#1\textwidth]{#2}%
  \end{figure}%
}
\newcommand{\imgth}[2][1]{%
  \begin{figure}%
    \centering%
    \includegraphics[height=#1\textheight]{#2}%
  \end{figure}%
}
\newcommand{\imgcmw}[2]{
  \begin{figure}%
    \centering%
    \includegraphics[width=#1cm]{#2}%
  \end{figure}%
}
\newcommand{\imgcmh}[2]{
  \begin{figure}%
    \centering%
    \includegraphics[height=#1cm]{#2}%
  \end{figure}%
}
\newcommand{\img}[1]{
  \begin{figure}%
    \centering%
    \includegraphics{#1}%
  \end{figure}%
}
\newcommand{\imgtwl}[2][1]{%
  \begin{figure}%
    \includegraphics[width=#1\textwidth,left]{#2}%
  \end{figure}%
}
\newcommand{\mintedpy}[1]{%
  \inputminted[fontsize=\footnotesize,bgcolor=pythonbg,framesep=1mm]{python}{code/#1.py}%
  \vspace{-1cm}%
  \inputminted[fontsize=\footnotesize,bgcolor=returnbg,framesep=1mm]{python}{code/#1.output}%
}

\newcommand{\mintedpycode}[1]{%
  \inputminted[fontsize=\footnotesize,bgcolor=pythonbg,framesep=1mm]{python}{code/#1.py}%
}

\definecolor{pythonbg}{rgb}{0.63,0.84,0.71}
\definecolor{returnbg}{rgb}{0.88,0.88,0.88}

\newcommand{\tw}{\textwidth}

\newcommand{\green}[1]{\textcolor{OliveGreen}{#1}}
\newcommand{\red}[1]{\textcolor{BrickRed}{#1}}
\newcommand{\blue}[1]{\textcolor{NavyBlue}{#1}}
\newcommand\gray[1]{\textcolor{gray}{#1}}
\newcommand\purple[1]{\textcolor{purple}{#1}}
\newcommand\smallgray[1]{\textcolor{gray}{\footnotesize\it #1}}
