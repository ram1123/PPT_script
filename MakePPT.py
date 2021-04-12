import os
import sys
import glob
from os import walk
InputDirPath = '/hpcfs/bes/mlgpu/sharma/ML_GPU/HHWWyy/'
RemoveString = "HHWWyyDNN_binary_TEST_10Apr_"

OutPutTexFile = 'all_training.tex'

os.system('cp ram.tex '+OutPutTexFile)

texFileIn = open(OutPutTexFile,'a')

frame = """
\\begin{frame}[fragile]{%s}
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

count=0
GetAllDirNames = []
for (dirpath, dirnames, filenames) in walk(InputDirPath):
    for name in dirnames:
        if name.startswith("HHWWyyDNN_binary_TEST"):
            count += 1
            # if count>3: break
            GetAllDirNames.append(dirpath+name)



DirList = {"Adam_BalanceYields", "Nadam_BalanceYields", "Adam_CW_BalanceYields", "Nadam_CW_BalanceYields", "Adam_SW_BalanceYields", "Nadam_SW_BalanceYields"}

# print("DirList: ",DirList)
# DirList_set = set(DirList)

# print("DirList_set: ",DirList_set)
adam, nadam, sw_adam, sw_adam_NonWgt, sw_nadam, sw_nadam_NonWgt, cw_adam, cw_nadam = [], [], [], [], [], [], [], []
GetAllDirNames.sort()
for item in GetAllDirNames:
    if "Adam_BalanceYields" in item:
        adam.append(item)
    elif "Nadam_BalanceYields" in item:
        nadam.append(item)
    elif "Adam_CW_BalanceYields" in item:
        cw_adam.append(item)
    elif "Nadam_CW_BalanceYields" in item:
        cw_nadam.append(item)
    elif "Adam_SW_BalanceYields" in item:
        sw_adam.append(item)
    elif "Nadam_SW_BalanceYields" in item:
        sw_nadam.append(item)
    elif "Adam_SW_BalanceNonWeighted" in item:
        sw_adam_NonWgt.append(item)
    elif "Nadam_SW_BalanceNonWeighted" in item:
        sw_nadam_NonWgt.append(item)

texFileIn.write("\n\n%================================================")
texFileIn.write("\\section{No Weight (Adam)}")
texFileIn.write((frame_section)%("No Weight (Adam)"))
texFileIn.write("%================================================\n\n")
for dirr in adam:
    img1=dirr+"/plots/all_metrics.png"
    img2=dirr+"/plots/overfitting_plot_BinaryClassifier_Binary.png"
    img3=dirr+"/plots/ROC.png"
    texFileIn.write((frame)%(str(dirr.replace(InputDirPath,"").replace(RemoveString,"").replace("_"," ")),str(img1),str(img2),str(img3)))
    texFileIn.write("\n")
    texFileIn.write("%========")

texFileIn.write("\n\n%================================================")
texFileIn.write("\\section{No Weight (Nadam)}")
texFileIn.write((frame_section)%("No Weight (Ndam)"))
texFileIn.write("%================================================\n\n")
for dirr in nadam:
    img1=dirr+"/plots/all_metrics.png"
    img2=dirr+"/plots/overfitting_plot_BinaryClassifier_Binary.png"
    img3=dirr+"/plots/ROC.png"
    texFileIn.write((frame)%(str(dirr.replace(InputDirPath,"").replace(RemoveString,"").replace("_"," ")),str(img1),str(img2),str(img3)))
    texFileIn.write("\n")
    texFileIn.write("%========")

texFileIn.write("\n\n%================================================")
texFileIn.write("\\section{Class Weight (Adam)}")
texFileIn.write((frame_section)%("Class Weight (Adam)"))
texFileIn.write("%================================================\n\n")
for dirr in cw_adam:
    img1=dirr+"/plots/all_metrics.png"
    img2=dirr+"/plots/overfitting_plot_BinaryClassifier_Binary.png"
    img3=dirr+"/plots/ROC.png"
    texFileIn.write((frame)%(str(dirr.replace(InputDirPath,"").replace(RemoveString,"").replace("_"," ")),str(img1),str(img2),str(img3)))
    texFileIn.write("\n")
    texFileIn.write("%========")

texFileIn.write("\n\n%================================================")
texFileIn.write("\\section{Class Weight (Nadam)}")
texFileIn.write((frame_section)%("Class Weight (Nadam)"))
texFileIn.write("%================================================\n\n")
for dirr in cw_nadam:
    img1=dirr+"/plots/all_metrics.png"
    img2=dirr+"/plots/overfitting_plot_BinaryClassifier_Binary.png"
    img3=dirr+"/plots/ROC.png"
    texFileIn.write((frame)%(str(dirr.replace(InputDirPath,"").replace(RemoveString,"").replace("_"," ")),str(img1),str(img2),str(img3)))
    texFileIn.write("\n")
    texFileIn.write("%========")

texFileIn.write("\n\n%================================================")
texFileIn.write("\\section{Sample Weight (Adam)}")
texFileIn.write((frame_section)%("Sample Weight (Adam)"))
texFileIn.write("%================================================\n\n")
for dirr in sw_adam:
    img1=dirr+"/plots/all_metrics.png"
    img2=dirr+"/plots/overfitting_plot_BinaryClassifier_Binary.png"
    img3=dirr+"/plots/ROC.png"
    texFileIn.write((frame)%(str(dirr.replace(InputDirPath,"").replace(RemoveString,"").replace("_"," ")),str(img1),str(img2),str(img3)))
    texFileIn.write("\n")
    texFileIn.write("%========")

texFileIn.write("\n\n%================================================")
texFileIn.write("\\section{Sample Weight (Nadam)}")
texFileIn.write((frame_section)%("Sample Weight (Nadam)"))
texFileIn.write("%================================================\n\n")
for dirr in sw_nadam:
    img1=dirr+"/plots/all_metrics.png"
    img2=dirr+"/plots/overfitting_plot_BinaryClassifier_Binary.png"
    img3=dirr+"/plots/ROC.png"
    texFileIn.write((frame)%(str(dirr.replace(InputDirPath,"").replace(RemoveString,"").replace("_"," ")),str(img1),str(img2),str(img3)))
    texFileIn.write("\n")
    texFileIn.write("%========")

texFileIn.write("\n\n%================================================")
texFileIn.write("\\section{Sample Weight (Adam) - No Weight}")
texFileIn.write((frame_section)%("Sample Weight (Aadam) - No Weight"))
texFileIn.write("%================================================\n\n")
for dirr in sw_adam_NonWgt:
    img1=dirr+"/plots/all_metrics.png"
    img2=dirr+"/plots/overfitting_plot_BinaryClassifier_Binary.png"
    img3=dirr+"/plots/ROC.png"
    texFileIn.write((frame)%(str(dirr.replace(InputDirPath,"").replace(RemoveString,"").replace("_"," ")),str(img1),str(img2),str(img3)))
    texFileIn.write("\n")
    texFileIn.write("%========")

texFileIn.write("\n\n%================================================")
texFileIn.write("\\section{Sample Weight (Nadam) - No Weight}")
texFileIn.write((frame_section)%("Sample Weight (Nadam) - No Weight"))
texFileIn.write("%================================================\n\n")
for dirr in sw_nadam_NonWgt:
    img1=dirr+"/plots/all_metrics.png"
    img2=dirr+"/plots/overfitting_plot_BinaryClassifier_Binary.png"
    img3=dirr+"/plots/ROC.png"
    texFileIn.write((frame)%(str(dirr.replace(InputDirPath,"").replace(RemoveString,"").replace("_"," ")),str(img1),str(img2),str(img3)))
    texFileIn.write("\n")
    texFileIn.write("%========")

last_line = ''
with open(OutPutTexFile, 'r') as f:
    lines = f.read().splitlines()
    last_line = lines[-1]

texFileIn = open(OutPutTexFile,'a')
# print(last_line)
if last_line.find("end") == -1:
    print(last_line)
    # texFileIn.write('\n\\end{frame}\n')
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


