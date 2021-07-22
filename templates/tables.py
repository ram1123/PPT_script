# -*- coding: utf-8 -*-
# @Author: Ram Krishna Sharma
# @Author Email: ram.krishna.sharma@cern.ch
# @Date:   2021-07-21
# @Last Modified by:   Ram Krishna Sharma
# @Last Modified time: 2021-07-21

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