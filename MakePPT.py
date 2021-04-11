import os
import sys
import glob
from os import walk
InputDirPath = '/Users/ramkrishna/cernbox/www/cppf/may18'

OutPutTexFile = 'ram_test.tex'

os.system('cp ram.tex '+OutPutTexFile)

texFileIn = open(OutPutTexFile,'a')

frame = """
\\begin{frame}[fragile]{%s}
\\vspace{-8.0pt}
\\begin{center}
\\begin{columns}
    \\begin{column}{0.6\\textwidth}
    \\begin{center}
    \\includegraphics[scale=0.3]{%s}
    \\end{center}
    \\end{column}
    \\begin{column}{0.4\\textwidth}
    \\begin{center}
    \\includegraphics[width=\\textwidth,height=4cm,trim={1cm 1cm 1cm 1.6cm},clip]{%s}\\\\
    \\includegraphics[width=\\textwidth,height=4cm,trim={0 0 0 1cm},clip]{%s}
    \\end{center}
    \\end{column}
\\end{columns}
\\end{center}
\\end{frame}
"""

# frame = "test_%s"

# print(frame)


count = 0
count1 = 0
for (dirpath, dirnames, filenames) in walk("/Users/ramkrishna/Documents/remote_works/ihep/DNN/HHWWyy/"):
    # for name in filenames:
    #     if name.endswith(".out"):
    #         count += 1
    #         print("%i,%s"%(count,dirpath))
    #     if name.endswith(".sh"):
    #         count += 1
    #         print("%i,%s"%(count,dirpath))
    for name in dirnames:
        if name.startswith("HHWWyyDNN_binary_TEST"):
            count += 1
            print("%i,%s"%(count,dirpath+name))
            img1=dirpath+name+"/plots/all_metrics.png"
            img2=dirpath+name+"/plots/overfitting_plot_BinaryClassifier_Binary.png"
            img3=dirpath+name+"/plots/ROC.png"
            print("\t==> %s"%img1)
            print("\t==> %s"%img2)
            print("\t==> %s"%img3)
            print(type(img1))
            print(type(img2))
            print(type(img3))
            # frame = (frame)%(str(name),str(img1),str(img2),str(img3))
            # frame = (frame)%(str("img3"))
            texFileIn.write((frame)%(str(name),str(img1),str(img2),str(img3)))
            texFileIn.write("\n")
            texFileIn.write("%========")
texFileIn.close()

# NumberOfSlidesInOnePage=6
# count = 0
# for files in os.listdir(InputDirPath):
#     if files.endswith('.pdf'):
#         if files.find("ID") != -1 and files.find("h1") != -1:
#             # print(files)
#             pdfFileNames = InputDirPath+os.sep+files
#             fileNames = files.replace('.pdf','')
#             # print(count,count%NumberOfSlidesInOnePage)
#             filetitle = fileNames.replace('_',' ')
#             figTemplate = ''
#             if (count % NumberOfSlidesInOnePage == 0):
#                 figTemplate = "\\begin{frame}\\frametitle{%s}\n"%(filetitle)
#             if (count % NumberOfSlidesInOnePage == 0):
#                 figTemplate += "\n\t\\includegraphics[scale=0.25]{%s}"%(pdfFileNames)
#                 figTemplate += repr("%").replace("'",'')
#             elif (count % NumberOfSlidesInOnePage == 2):
#                 figTemplate += "\n\t\\includegraphics[scale=0.25]{%s}\\\\"%(pdfFileNames)
#                 # figTemplate += repr("%").replace("'",'')
#             else:
#                 # pass
#                 figTemplate += "\n\t\\includegraphics[scale=0.25]{%s}"%(pdfFileNames)
#                 figTemplate += repr("%").replace("'",'')
#             if (count % NumberOfSlidesInOnePage == 5):
#                 # figTemplate += "\t\\includegraphics[scale=0.25]{%s.pdf}"%(pdfFileNames)
#                 figTemplate += "\n\\end{frame}\n"
#             # print(figTemplate)
#             texFileIn.write(figTemplate)
#             count +=1
# texFileIn.close()

last_line = ''
with open(OutPutTexFile, 'r') as f:
    lines = f.read().splitlines()
    last_line = lines[-1]

texFileIn = open(OutPutTexFile,'a')
# print(last_line)
if last_line.find("end") == -1:
    print(last_line)
    texFileIn.write('\n\\end{frame}\n')
texFileIn.write("""
\\section{Summary}
\\begin{frame}\\frametitle{Summary \\& Conclusion}
  \\begin{itemize}
    \\item Test
  \\end{itemize}
\\end{frame}



\\begin{frame}[c]
    \\begin{center}
    \\Huge Thanks
    \\end{center}
\\end{frame}

\\section{Backup}
\\begin{frame}[c]
   \\begin{center}
   \\Huge Backup Slides
   \\end{center}
\\end{frame}



\\end{document}
""")

texFileIn.close()



os.system('pdflatex '+OutPutTexFile)
os.system('pdflatex '+OutPutTexFile)

print('rm fig_*.tex  '+OutPutTexFile.replace('.tex','')+'.toc '+ OutPutTexFile.replace('.tex','')+'.snm '+ OutPutTexFile.replace('.tex','')+'.out '+ OutPutTexFile.replace('.tex','')+'.nav '+ OutPutTexFile.replace('.tex','')+'.aux '+ OutPutTexFile.replace('.tex','')+'.log')


