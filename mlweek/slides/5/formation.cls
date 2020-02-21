
\NeedsTeXFormat{LaTeX2e}

\ProvidesClass{formation}[2017/12/01 LaTeX class for my formations]

\PassOptionsToPackage{dvipsnames,hyperref,usenames,table}{xcolor}

\LoadClass[10pt,handout]{beamer}


\RequirePackage{xcolor}
\RequirePackage{comment}
\RequirePackage{amsmath}
\RequirePackage{amssymb}
\RequirePackage{booktabs}
\RequirePackage{subfigure}
\RequirePackage{hyperref}
\RequirePackage{multicol}
\RequirePackage{minted}
\RequirePackage{graphicx}
\RequirePackage[numbers]{natbib}
\RequirePackage{forest}
\RequirePackage{bm}
\RequirePackage{stmaryrd}
\RequirePackage[francais]{babel}
\RequirePackage[export]{adjustbox}
\RequirePackage{array}
\RequirePackage{adjustbox}
%\RequirePackage{listings}
%\RequirePackage[utf8]{inputenc}
%\RequirePackage{relsize}
\RequirePackage{amsmath,mathtools}
\RequirePackage{mathabx}         
%\RequirePackage[T1]{fontenc}
%\RequirePackage{physics}
\RequirePackage{url}
%\RequirePackage{times}

%\RequirePackage{enumitem}



\DeclareGraphicsExtensions{.pdf,.png,.jpg,.jpeg,.PNG,.JPG,.JPEG}
\graphicspath{{./img/}}

\usetheme{metropolis}
\setbeamercolor{normal text}{bg=white}
\setbeamertemplate{bibliography item}{\insertbiblabel}
\setbeamertemplate{frame footer}{%
  \includegraphics[height=0.8cm]{logo_mlweek}%
  \hspace{.1cm}%
  \url{https://www.ml-week.com/}
  \hspace{.1cm}%
  À l'usage exclusif des participants aux formations
}



\bibliographystyle{abbrv}

\newcommand{\partiald}[2]{\frac{\partial #1}{\partial #2}}
\DeclareMathOperator*{\argmin}{arg\,min}
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

\newcommand{\vect}[1]{\bm{\mathbf{#1}}}

\newcommand{\imgtw}[2][1]{%
  \begin{figure}%
    \centering%
    \includegraphics[width=#1\textwidth]{#2}%
  \end{figure}%
}
\newcommand{\imgtwl}[2][1]{%
  \begin{figure}%
    \includegraphics[width=#1\textwidth,left]{#2}%
  \end{figure}%
}
\newcommand{\imgth}[2][1]{%
  \begin{figure}%
    \centering%
    \includegraphics[height=#1\textheight]{#2}%
  \end{figure}%
}
\newcommand{\imgthl}[2][1]{%
  \begin{figure}%
    \includegraphics[height=#1\textheight,right]{#2}%
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

\newcommand{\tw}{\textwidth}

\newcommand{\green}[1]{\textcolor{OliveGreen}{#1}}
\newcommand{\red}[1]{\textcolor{BrickRed}{#1}}
\newcommand{\blue}[1]{\textcolor{NavyBlue}{#1}}
\newcommand\gray[1]{\textcolor{gray}{#1}}
\newcommand\purple[1]{\textcolor{purple}{#1}}
\newcommand\smallgray[1]{\textcolor{gray}{\footnotesize\it #1}}


\date{}
