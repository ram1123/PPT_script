import os
import sys
import glob

InputDirPath = '/Users/ramkrishna/cernbox/www/cppf/may18'

OutPutTexFile = 'ram_test.tex'

os.system('cp ram.tex '+OutPutTexFile)

texFileIn = open(OutPutTexFile,'a')

NumberOfSlidesInOnePage=6
count = 0
for files in os.listdir(InputDirPath):
    if files.endswith('.pdf'):
        if files.find("ID") != -1 and files.find("h1") != -1:
            # print(files)
            pdfFileNames = InputDirPath+os.sep+files
            fileNames = files.replace('.pdf','')
            # print(count,count%NumberOfSlidesInOnePage)
            filetitle = fileNames.replace('_',' ')
            figTemplate = ''
            if (count % NumberOfSlidesInOnePage == 0):
                figTemplate = "\\begin{frame}\\frametitle{%s}\n"%(filetitle)
            if (count % NumberOfSlidesInOnePage == 0):
                figTemplate += "\n\t\\includegraphics[scale=0.25]{%s}"%(pdfFileNames)
                figTemplate += repr("%").replace("'",'')
            elif (count % NumberOfSlidesInOnePage == 2):
                figTemplate += "\n\t\\includegraphics[scale=0.25]{%s}\\\\"%(pdfFileNames)
                # figTemplate += repr("%").replace("'",'')
            else:
                # pass
                figTemplate += "\n\t\\includegraphics[scale=0.25]{%s}"%(pdfFileNames)
                figTemplate += repr("%").replace("'",'')
            if (count % NumberOfSlidesInOnePage == 5):
                # figTemplate += "\t\\includegraphics[scale=0.25]{%s.pdf}"%(pdfFileNames)
                figTemplate += "\n\\end{frame}\n"
            # print(figTemplate)
            texFileIn.write(figTemplate)
            count +=1
texFileIn.close()

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


