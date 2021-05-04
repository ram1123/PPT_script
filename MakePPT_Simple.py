import os
import sys
import glob
from os import walk
import re

###############################################################
##      Variables to be updated by user                      ##
###############################################################
InputDirPath = '/hpcfs/bes/mlgpu/sharma/ML_GPU/HHWWyy/'
OutPutTexFile = 'DNNDistributions_05May2021.tex'

ListRemoveString = [
                "HHWWyyDNN_binary_May01_",
                "HHWWyyDNN_binary_May02_",
                "HHWWyyDNN_binary_May04_",
                "BalanceNonWeighted"
                ]
ListDirListStartsWith = [
                "HHWWyyDNN_binary_May05"
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
                "NewModel5_": "Model5",
                "NewModel4_": "Model4",
                "NewModel3_": "Model3",
                "NewModel2_": "Model2",
                "NewModel_": "Model1",

                "AllLOSignalWhileTrain": "All Sig"
}

###############################################################

# os.system('cp ram.tex '+OutPutTexFile)

texFileIn = open(OutPutTexFile,'w')

from LatexHeader import LatexHeader, frame, frame_section, TableHeader, TableFooter

texFileIn.write(LatexHeader)
TableCSVFile = open(OutPutTexFile.replace(".tex",".csv"),'w')
TableMDFile = open(OutPutTexFile.replace(".tex",".md"),'w')

TableCSVFile.write("{0:56},{1:6},{2:6},{3:80}\n".format("Training Vars","AUC (Test area )","AUC (Train area)","Full Dirc Name"))
TableMDFile.write("|{0:56}|{1:6}|{2:6}|{3:80}\n".format("Training Vars","AUC (Test area )","AUC (Train area)","Full Dirc Name"))
TableMDFile.write("|{0:56}|{1:6}|{2:6}|{3:80}\n".format("---","---","---","---"))

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

GetAllDirNames.sort()

def GetTitle(dirr):
    # Title = dirr
    Title = dirr.replace(InputDirPath,"")
    for RemoveString in ListRemoveString:
        Title = Title.replace(RemoveString,"")
    for key in DictReplaceString:
        Title = Title.replace(key,DictReplaceString[key])
    Title = Title.replace("_",", ")
    # Title = Title.rstrip()
    # if Title[-1] == ",":
        # Title[-1] = ""
    return Title

# texFileIn.write("\n\n%================================================\n")
# texFileIn.write("\\section{No Weight (Adam)}\n")
# texFileIn.write((frame_section)%("No Weight (Adam)"))
texFileIn.write("%================================================\n\n")
TabelContent = []
for dirr in GetAllDirNames:
    img1=dirr+"/plots/all_metrics.png"
    img2=dirr+"/plots/overfitting_plot_BinaryClassifier_Binary.png"
    img3=dirr+"/plots/ROC.png"
    if os.path.exists(img3):
        texFileIn.write((frame)%(str(GetTitle(dirr)),str(img1),str(img2),str(img3)))
        texFileIn.write("\n")
        texFileIn.write("%========")
        # print dirr
        files = glob.glob(dirr+"/*.out")
        # print files[0]
        tempValues = []
        for line in open(files[0]).readlines():
            if re.search("     ROC AUC", line):
                tempValues.append(line)
        dirName = str(GetTitle(dirr).replace(","," "))
        ROCTestArea = str(tempValues[0].split()[-1])
        ROCTrainArea = str(tempValues[1].split()[-1])
        # print("{0:56},{1:6},{2:6}\n".format(dirName,ROCTestArea,ROCTrainArea))
        TableCSVFile.write("{0:56},{1:6},{2:6},{3:80}\n".format(dirName,ROCTestArea,ROCTrainArea,dirr))
        TableMDFile.write("|{0:56}|{1:6}|{2:6}|{3:80}|\n".format(dirName,ROCTestArea,ROCTrainArea,dirr))
        # TabelContent.append("  %s & %s & %s \\\\ \n\\hline\n"%(str(GetTitle(dirr)),str(tempValues[0].split()[-1]),str(tempValues[1].split()[-1])))
        TabelContent.append("  {0:56} & {1:6} & {2:6} \\\\ \n\\hline\n".format(dirName,ROCTestArea,ROCTrainArea))

texFileIn.write(TableHeader)
for lines in TabelContent:
    texFileIn.write(lines)
    # TableCSVFile.write(lines.replace("%s",","))
    # TableMDFile.write(lines.replace("%s","|"))
texFileIn.write(TableFooter)
# TableFile.write(TableFooter)
TableCSVFile.close()
TableMDFile.close()

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
% \\section{Summary}
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

% \\begin{frame}[c]
   % \\begin{center}
   % \\Huge Backup Slides
   % \\end{center}
% \\end{frame}
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

print('make clean')
os.system('make clean')
# print('rm '+OutPutTexFile.replace('.tex','')+'.toc '+ OutPutTexFile.replace('.tex','')+'.snm '+ OutPutTexFile.replace('.tex','')+'.out '+ OutPutTexFile.replace('.tex','')+'.nav '+ OutPutTexFile.replace('.tex','')+'.aux '+ OutPutTexFile.replace('.tex','')+'.log')
# os.system('rm '+OutPutTexFile.replace('.tex','')+'.toc '+ OutPutTexFile.replace('.tex','')+'.snm '+ OutPutTexFile.replace('.tex','')+'.out '+ OutPutTexFile.replace('.tex','')+'.nav '+ OutPutTexFile.replace('.tex','')+'.aux '+ OutPutTexFile.replace('.tex','')+'.log')


