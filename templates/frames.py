# -*- coding: utf-8 -*-
# @Author: Ram Krishna Sharma
# @Author Email: ram.krishna.sharma@cern.ch
# @Date:   2021-07-21
# @Last Modified by:   Ram Krishna Sharma
# @Last Modified time: 2021-08-03


frame_Thanks = """
\\begin{{frame}}[c]
    \\begin{{center}}
    \\Huge {message}
    \\end{{center}}
\\end{{frame}}
"""

frame_OneImageRotate90Deg = """
\\begin{{frame}} [fragile]{{\\small{{ {title} }}}}
    \\includegraphics[width=\\textwidth,height=\\textheight,angle=90]{{{img1}}}
\\end{{frame}}
"""

frame_ThreeImageInLine = """
\\begin{{frame}} [fragile]{{\\small{{ {var1} }}}}
    \\includegraphics[width=0.33\\textwidth]{{{var2}}} %
    \\includegraphics[width=0.33\\textwidth]{{{var3}}} %
    \\includegraphics[width=0.33\\textwidth]{{{var4}}}
\\end{{frame}}
"""

# trim={<left> <lower> <right> <upper>}
frame_TwoColumns_BinaryDNN = """
\\begin{{frame}}[fragile]{{\\small{{{title}}}}}
\\vspace{{-28.0pt}}
\\begin{{center}}
\\begin{{columns}}
    \\begin{{column}}{{0.6\\textwidth}}
    \\begin{{center}}
    \\includegraphics[scale=0.3]{{{img1}}}
    \\end{{center}}
    \\end{{column}}
    \\begin{{column}}{{0.4\\textwidth}}
    \\begin{{center}}
    \\includegraphics[width=\\textwidth,height=3.5cm,trim={{1cm 1cm 1cm 1.9cm}},clip]{{{img2}}}\\\\
    \\includegraphics[width=\\textwidth,height=4cm,trim={{0 0 0 1cm}},clip]{{{img3}}}
    \\end{{center}}
    \\end{{column}}
\\end{{columns}}
\\end{{center}}
\\end{{frame}}
"""


# trim={<left> <lower> <right> <upper>}
frame_DNN_LeftEpoch_CenterROC_RightRanking = """
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
