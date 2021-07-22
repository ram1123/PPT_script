# -*- coding: utf-8 -*-
# @Author: Ram Krishna Sharma
# @Author Email: ram.krishna.sharma@cern.ch
# @Date:   2021-07-21
# @Last Modified by:   Ram Krishna Sharma
# @Last Modified time: 2021-07-21


# trim={<left> <lower> <right> <upper>}
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


# trim={<left> <lower> <right> <upper>}
frameThreeImageInLine2 = """
\\begin{{frame}} [fragile]{{\\small{{ {title} }}}}
    \\vspace{{-29.0pt}}
    \\begin{{center}}
        \\begin{{columns}}
            \\begin{{column}}{{0.30\\textwidth}}
                \\begin{{center}}
                \\includegraphics[width=\\textwidth,height=0.43\\textheight]{{{img1}}}\\
                \\includegraphics[width=\\textwidth,height=0.43\\textheight]{{{img2}}}
                \\end{{center}}
            \\end{{column}}
            \\begin{{column}}{{0.30\\textwidth}}
                \\begin{{center}}
                \\includegraphics[width=\\textwidth,height=0.43\\textheight]{{{img3}}} \\
                \\includegraphics[width=\\textwidth,height=0.43\\textheight]{{{img4}}}
                \\end{{center}}
            \\end{{column}}
            \\begin{{column}}{{0.40\\textwidth}}
                \\begin{{center}}
                \\includegraphics[width=\\textwidth,height=0.8\\textheight,trim={{32cm 0 0 0}},clip]{{{img5}}}
                \\end{{center}}
            \\end{{column}}
        \\end{{columns}}
    \\end{{center}}
\\end{{frame}}
"""

frameThreeImageInLine = """
\\begin{{frame}} [fragile]{{\\small{{ {var1} }}}}
    \\includegraphics[width=0.33\\textwidth]{{{var2}}} %
    \\includegraphics[width=0.33\\textwidth]{{{var3}}} %
    \\includegraphics[width=0.33\\textwidth]{{{var4}}}
\\end{{frame}}
"""

frame_section = """
\\begin{frame}[c]
    \\begin{center}
    \\Huge %s
    \\end{center}
\\end{frame}
"""