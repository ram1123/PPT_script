# -*- coding: utf-8 -*-
# @Author: Ram Krishna Sharma
# @Author Email: ram.krishna.sharma@cern.ch
# @Date:   2021-07-21
# @Last Modified by:   Ram Krishna Sharma
# @Last Modified time: 2021-07-22

LatexHeader = """\\documentclass[slidestop,compress,mathserif,aspectratio=169]{{beamer}}
\\usepackage[latin1]{{inputenc}}
\\usepackage{{verbatim}}
\\usepackage{{graphicx}}
\\usetheme{{Boadilla}}
\\usecolortheme{{beaver}} %{{beetle}}%{{crane}}
\\usepackage{{textpos}}
\\usepackage{{tikz}}


\\title[Priliminary Plots]{{{SlideTitle}}}
\\subtitle{{{SlideSubTitle}}}
\\date[\\today]{{\\today}}

\\author[Ram krishna Sharma]{{
        \\emph{{{author}}}\\inst{{1}}
        }}

\\institute[Beijing,China]{{
            \\inst{{1}}{institute}
        }}


\\setbeamertemplate{{footline}}[slide number]
\\setbeamertemplate{{frametitle}}[default][center]         % For centering the Heading

\\titlegraphic{{
    \\includegraphics[width=1.5cm,keepaspectratio]{{logo/cern.jpg}}\\hspace*{{3.35cm}}~%
    \\includegraphics[width=4cm,keepaspectratio]{{{instLogo}}}\\hspace*{{2.75cm}}~%
    \\includegraphics[width=1.5cm,keepaspectratio]{{logo/cmsLogo.jpeg}}
}}

\\begin{{document}}
% \\renewcommand{{\\inserttotalframenumber}}{{\\pageref{{lastslide}}}}

%%%%%%
%
%  if you need footer in title slide then comment line \\setbeamertemplate{{footline}}{{}}
% Ref: https://tex.stackexchange.com/questions/18828/how-to-remove-footline-on-the-title-page-of-beamer-slides
%
%%%%%%
{{
\\setbeamertemplate{{footline}}{{}}
\\begin{{frame}}
\\titlepage
\\end{{frame}}
}}

% \\begin{{frame}}\\frametitle{{Table of contents}}\\tableofcontents
% \\end{{frame}}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% \\section{{Introduction}}

% \\section{{Plots}}
"""


LatexFooter = """% \\section{Summary}
% \\begin{frame}\\frametitle{Summary \\& Conclusion}
  % \\begin{itemize}
    % \\item Test
  % \\end{itemize}
% \\end{frame}

\\begin{frame}[c]
    \\begin{center}
    \\Huge Thanks
    \\end{center}
\\end{frame}

\\end{document}
"""