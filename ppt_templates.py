# -*- coding: utf-8 -*-
# @Author: Ram Krishna Sharma
# @Date:   2021-04-12 10:24:47
# @Last Modified by:   ramkrishna
# @Last Modified time: 2021-04-12 10:27:14
header="""
\\documentclass[slidestop,compress,mathserif,aspectratio=169]{beamer}
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

\\title[Priliminary Plots]{Some Priliminary Plots}
\\subtitle{Test Plots}
\\date[\\today]{\\today}

\\author[Ram krishna Sharma]{
        \\emph{Ramkrishna Sharma}\\inst{1}
        % Test1\\inst{2},
        % Test2\\inst{3},
        % test4\\inst{1}
        }

\\institute[Beijing, China]{
            \\inst{1}Institute of High Energy Physics
            % \\inst{2}National Taiwan University,
            % \\inst{3}Brazilian Center for Physics Research
        }


\\setbeamertemplate{footline}[slide number]
\\setbeamertemplate{frametitle}[default][center]         % For centering the Heading

\\titlegraphic{
    \\includegraphics[width=1.5cm,keepaspectratio]{cern.jpg}\\hspace*{3.35cm}~%
    \\includegraphics[width=2cm,keepaspectratio]{IHEP_logo.png}\\hspace*{2.75cm}~%
    \\includegraphics[width=1.5cm,keepaspectratio]{cmsLogo.jpeg}
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

%\\begin{frame}\\frametitle{Table of contents}\\tableofcontents
%\\end{frame}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\\section{Introduction}

\\section{Plots}
%Pointer-rk
\\documentclass[slidestop,compress,mathserif,aspectratio=169]{beamer}
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

\\title[Priliminary Plots]{Some Priliminary Plots}
\\subtitle{Test Plots}
\\date[\\today]{\\today}

\\author[Ram krishna Sharma]{
        \\emph{Ramkrishna Sharma}\\inst{1}
        % Test1\\inst{2},
        % Test2\\inst{3},
        % test4\\inst{1}
        }

\\institute[Beijing, China]{
            \\inst{1}Institute of High Energy Physics
            % \\inst{2}National Taiwan University,
            % \\inst{3}Brazilian Center for Physics Research
        }


\\setbeamertemplate{footline}[slide number]
\\setbeamertemplate{frametitle}[default][center]         % For centering the Heading

\\titlegraphic{
    \\includegraphics[width=1.5cm,keepaspectratio]{cern.jpg}\\hspace*{3.35cm}~%
    \\includegraphics[width=2cm,keepaspectratio]{IHEP_logo.png}\\hspace*{2.75cm}~%
    \\includegraphics[width=1.5cm,keepaspectratio]{cmsLogo.jpeg}
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

%\\begin{frame}\\frametitle{Table of contents}\\tableofcontents
%\\end{frame}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\\section{Introduction}

\\section{Plots}
"""