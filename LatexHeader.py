# -*- coding: utf-8 -*-
# @Author: Ram Krishna Sharma
# @Date:   2021-05-05
# @Last Modified by:   Ram Krishna Sharma
# @Last Modified time: 2021-05-05

LatexHeader = """\\documentclass[slidestop,compress,mathserif,aspectratio=169]{beamer}
\\usepackage[latin1]{inputenc}
\\usepackage{verbatim}
\\usepackage{graphicx}
\\usetheme{Boadilla}
\\usecolortheme{beaver} %{beetle}%{crane}
\\usepackage{textpos}
\\usepackage{tikz}


% Look for graphics in the `figures/` directory
% I try to have all my figures as PDFs
%\\graphicspath{{figures/}}

\\title[Priliminary Plots]{DNN Training Scan Results}
\\subtitle{Scan w.r.t. class\\_weight, sample\\_weight, and without any weight}
\\date[\\today]{\\today}

\\author[Ram krishna Sharma]{
        \\emph{Ramkrishna Sharma}\\inst{1}
        }

\\institute[Beijing,China]{
            \\inst{1}IHEP, Beijing
        }


\\setbeamertemplate{footline}[slide number]
\\setbeamertemplate{frametitle}[default][center]         % For centering the Heading

\\titlegraphic{
    \\includegraphics[width=1.5cm,keepaspectratio]{logo/cern.jpg}\\hspace*{3.35cm}~%
    \\includegraphics[width=4cm,keepaspectratio]{logo/IHEP_logo.png}\\hspace*{2.75cm}~%
    \\includegraphics[width=1.5cm,keepaspectratio]{logo/cmsLogo.jpeg}
}

\\begin{document}
% \\renewcommand{\\inserttotalframenumber}{\\pageref{lastslide}}

%%%%%%
%
%  if you need footer in title slide then comment line \\setbeamertemplate{footline}{}
% Ref: https://tex.stackexchange.com/questions/18828/how-to-remove-footline-on-the-title-page-of-beamer-slides
%
%%%%%%
{
\\setbeamertemplate{footline}{}
\\begin{frame}
\\titlepage
\\end{frame}
}

\\begin{frame}\\frametitle{Table of contents}\\tableofcontents
\\end{frame}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% \\section{Introduction}

% \\section{Plots}
"""


TableHeader = """
\\begin{frame}[fragile]{\\small{Summary Table}}
\\vspace{-28.0pt}
\\begin{table}[htbp]
% \\resizebox{\\linewidth}{!}
% \\footnotesize
\\tiny
% \\resizebox{\\columnwidth}{!}
{
 \\begin{tabular}{||c c c||}
 \\hline
 Training Vars & AUC (Test area ) & AUC (Train area) \\\\ [0.5ex]
 \\hline\\hline
 """

TableFooter = """
\\end{tabular}
}
\\end{table}
\\end{frame}
"""
# TableFile.write(TableHeader)

frame = """
\\begin{frame}[fragile]{\\small{%s}}
\\vspace{-28.0pt}
\\begin{center}
\\begin{columns}
    \\begin{column}{0.6\\textwidth}
    \\begin{center}
    \\includegraphics[scale=0.3]{%s}
    \\end{center}
    \\end{column}
    \\begin{column}{0.4\\textwidth}
    \\begin{center}
    \\includegraphics[width=\\textwidth,height=3.5cm,trim={1cm 1cm 1cm 1.9cm},clip]{%s}\\\\
    \\includegraphics[width=\\textwidth,height=4cm,trim={0 0 0 1cm},clip]{%s}
    \\end{center}
    \\end{column}
\\end{columns}
\\end{center}
\\end{frame}
"""

frame_section = """
\\begin{frame}[c]
    \\begin{center}
    \\Huge %s
    \\end{center}
\\end{frame}
"""

