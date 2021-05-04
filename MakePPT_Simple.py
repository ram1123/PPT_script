import os
import sys
import glob
from os import walk

###############################################################
##      Variables to be updated by user                      ##
###############################################################
InputDirPath = '/hpcfs/bes/mlgpu/sharma/ML_GPU/HHWWyy/'
OutPutTexFile = 'DNNDistributions_04May2021.tex'

ListRemoveString = [
                "HHWWyyDNN_binary_May01_",
                "HHWWyyDNN_binary_May02_",
                "HHWWyyDNN_binary_May04_",
                "BalanceNonWeighted"
                ]
ListDirListStartsWith = [
                "HHWWyyDNN_binary_May04"
                ]

DictReplaceString = {
                # Some general replacement
                # "_": ", ",
                # path removal
                # InputDirPath: "", # FIXME: variable not picking in the for loop used below.

                # General parameters name upadate removal
                # "_E": "_Epoch=",
                "_LR0p": ", LR=0.",
                "1_B": "1, Batch=",
                "BalanceYields": "Weighted",
                "BalanceYields": "",
                "BalanceNonWeighted": "No Wgt",

                # Update model name removal
                "NewModel4_": "Model4",
                "NewModel3_": "Model3",
                "NewModel2_": "Model2",
                "NewModel_": "Model1",

                "AllLOSignalWhileTrain": "All Sig"
}

###############################################################

os.system('cp ram.tex '+OutPutTexFile)

texFileIn = open(OutPutTexFile,'a')

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

count=0
GetAllDirNames = []
for (dirpath, dirnames, filenames) in walk(InputDirPath):
    for name in dirnames:
        for DirListStartsWith in ListDirListStartsWith:
            if name.startswith(DirListStartsWith):
                count += 1
                # if count>10: break
                GetAllDirNames.append(dirpath+name)



DirList = {"Adam_BalanceYields", "Nadam_BalanceYields", "Adam_CW_BalanceYields", "Nadam_CW_BalanceYields", "Adam_SW_BalanceYields", "Nadam_SW_BalanceYields"}

# print("DirList: ",DirList)
# DirList_set = set(DirList)

# print("DirList_set: ",DirList_set)
# adam, nadam, sw_adam, sw_adam_NonWgt, sw_nadam, sw_nadam_NonWgt, cw_adam, cw_nadam = [], [], [], [], [], [], [], []
GetAllDirNames.sort()
# for item in GetAllDirNames:
#     if "Adam_BalanceYields" in item:
#         adam.append(item)
#     elif "Nadam_BalanceYields" in item:
#         nadam.append(item)
#     elif "Adam_CW_BalanceYields" in item:
#         cw_adam.append(item)
#     elif "Nadam_CW_BalanceYields" in item:
#         cw_nadam.append(item)
#     elif "Adam_SW_BalanceYields" in item:
#         sw_adam.append(item)
#     elif "Nadam_SW_BalanceYields" in item:
#         sw_nadam.append(item)
#     elif "Adam_SW_BalanceNonWeighted" in item:
#         sw_adam_NonWgt.append(item)
#     elif "Nadam_SW_BalanceNonWeighted" in item:
#         sw_nadam_NonWgt.append(item)


def GetTitle(dirr):
    # Title = dirr
    Title = dirr.replace(InputDirPath,"")
    # Title = Title.replace("_E","_Epoch=")
    for RemoveString in ListRemoveString:
        Title = Title.replace(RemoveString,"")
    for key in DictReplaceString:
        Title = Title.replace(key,DictReplaceString[key])
    # Title = Title.replace("_LR0p",", LR=0.")
    # Title = Title.replace("1_B","1, Batch=")
    # if "_SW_" in Title:
        # Title = Title.replace("BalanceYields","Weighted")
        # Title = Title.replace("BalanceNonWeighted","No Wgt")
    # else:
        # Title = Title.replace("BalanceYields","")
    Title = Title.replace("_",", ")
    # Title = Title.rstrip()
    # if Title[-1] == ",":
        # Title[-1] = ""
    return Title

# texFileIn.write("\n\n%================================================\n")
# texFileIn.write("\\section{No Weight (Adam)}\n")
# texFileIn.write((frame_section)%("No Weight (Adam)"))
texFileIn.write("%================================================\n\n")
for dirr in GetAllDirNames:
    img1=dirr+"/plots/all_metrics.png"
    img2=dirr+"/plots/overfitting_plot_BinaryClassifier_Binary.png"
    img3=dirr+"/plots/ROC.png"
    # Title = dirr.replace(InputDirPath,"").replace(RemoveString,"")
    # Title = Title.replace("_E","_Epoch = ")
    # Title = Title.replace("_LR0p","_LR = 0.")
    # Title = Title.replace("_B","_Batch Size = ")
    # Title = Title.replace("_"," ")
    if os.path.exists(img3):
        texFileIn.write((frame)%(str(GetTitle(dirr)),str(img1),str(img2),str(img3)))
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

\\begin{frame}[c]
   \\begin{center}
   \\Huge Backup Slides
   \\end{center}
\\end{frame}



\\end{document}
""")

texFileIn.close()


LatexCommand = 'pdflatex '+OutPutTexFile
MoveTexFile = 'mv  '+OutPutTexFile+ " pdffile/"
MovePdfFile = 'mv  '+OutPutTexFile.replace('.tex','.pdf')+ " pdffile/"

print(LatexCommand)
os.system(LatexCommand)
os.system(LatexCommand)
print(MoveTexFile)
os.system(MoveTexFile)
print(MovePdfFile)
os.system(MovePdfFile)
# os.system('pdflatex '+OutPutTexFile)
# os.system('pdflatex '+OutPutTexFile)
# os.system('mv  '+OutPutTexFile+ " pdffile/")
# os.system('mv  '+OutPutTexFile.replace('.tex','.pdf')+ " pdffile/")

print('rm '+OutPutTexFile.replace('.tex','')+'.toc '+ OutPutTexFile.replace('.tex','')+'.snm '+ OutPutTexFile.replace('.tex','')+'.out '+ OutPutTexFile.replace('.tex','')+'.nav '+ OutPutTexFile.replace('.tex','')+'.aux '+ OutPutTexFile.replace('.tex','')+'.log')
os.system('rm '+OutPutTexFile.replace('.tex','')+'.toc '+ OutPutTexFile.replace('.tex','')+'.snm '+ OutPutTexFile.replace('.tex','')+'.out '+ OutPutTexFile.replace('.tex','')+'.nav '+ OutPutTexFile.replace('.tex','')+'.aux '+ OutPutTexFile.replace('.tex','')+'.log')


