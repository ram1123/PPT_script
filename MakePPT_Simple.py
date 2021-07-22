import os
import sys
import glob
from os import walk
import re

###############################################################
##      Variables to be updated by user                      ##
###############################################################
InputDirPath = '/hpcfs/bes/mlgpu/sharma/ML_GPU/MultiClassifier/MultiClassifier/'
# OutPutTexFile = 'DNNDistributions_05May2021.tex'
OutPutTexFile = 'MultiClass_RawAllVar_MultiClass_NodeLayerScan_RawVarV2Redu30_20July2021.tex'
# OutPutTexFile = 'DNNDistributions_05May2021_Best.tex'

ListRemoveString = [
                # "HHWWyyDNN_binary_May01_",
                # "HHWWyyDNN_binary_May02_",
                # "HHWWyyDNN_binary_May04_",
                # "HHWWyyDNN_binary_May05_",
                # "HHWWyyDNN_binary_",
                "HHWWyyDNN_MultiClassifier_Model",
                "BalanceNonWeighted",
                "BalanceYields"
                ]
ListDirListStartsWith = [
                # All
                # "HHWWyyDNN_MultiClassifier_Model",
                "HHWWyyDNN_MultiClass_ModelVarLayerV1_E",
                # "HHWWyyDNN_binary_May05",

                # Best only
                # "HHWWyyDNN_binary_May05_NewModel5_E700_LR10em5_B100_ELU_DR0p1_Nadam_DefaultVar_CW_BalanceNonWeighted",
                # "HHWWyyDNN_binary_May05_NewModel5_E700_LR10em5_B100_ELU_DR0p1_Adam_DefaultVar_BalanceNonWeighted",
                ]

DirNameShouldContain = "RawVarV2Redu30"
# DirNameShouldContain = [
            # "RawVar_CWFix_Trial"
        # ]

DictReplaceString = {
                # Some general replacement
                # "_": ", ",
                # path removal
                # InputDirPath: "", # FIXME: variable not picking in the for loop used below.

                # General parameters name upadate removal
                # "_E": "_Epoch=",
                # "_LR0p": ", LR=0.",
                "LR10em1": ", LR$10^{-1}$",
                "LR10em2": ", LR$10^{-2}$",
                "LR10em3": ", LR$10^{-3}$",
                "LR10em4": ", LR$10^{-4}$",
                "LR10em5": ", LR$10^{-5}$",
                "LR10em6": ", LR$10^{-6}$",
                "LR10em7": ", LR$10^{-7}$",
                # "1_B": "1, Batch=",
                # "BalanceYields": "Weighted",
                # "BalanceYields": "",
                # "BalanceNonWeighted": "No Wgt",

                # Update model name removal
                # "NewModel5_": "Model5 ",
                # "NewModel4_": "Model4 ",
                # "NewModel3_": "Model3 ",
                # "NewModel2_": "Model2 ",
                # "NewModel_" : "Model1 ",

                # "AllLOSignalWhileTrain": "All Sig"
}

###############################################################

# os.system('cp ram.tex '+OutPutTexFile)

texFileIn = open(OutPutTexFile,'w')

from LatexHeader import LatexHeader, frame, frameThreeImageInLine, frameThreeImageInLine2, frame_section, TableHeader, TableFooter

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
            # if name.startswith(DirListStartsWith) and (DirNameShouldContain in DirListStartsWith):
            if name.startswith(DirListStartsWith):
                if DirNameShouldContain in name:
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
    img1=dirr+"/plots/history_loss.png"
    img2=dirr+"/plots/history_acc.png"
    img3=dirr+"/plots/MultiClass_ROC_dataset_test.png"
    img4=dirr+"/plots/MultiClass_ROC_dataset_train.png"
    img5=dirr+"/plots/DeepExplainer_Bar_sigmoid_y0.png"
    if os.path.exists(img3):
        # print (frameThreeImageInLine)%(str(GetTitle(dirr)),str(img1),str(img2),str(img3))
        # texFileIn.write((frame)%(str(GetTitle(dirr)),str(img1),str(img2),str(img3)))
        texFileIn.write((frameThreeImageInLine2).format(title=str(GetTitle(dirr)),img1=str(img1),img2=str(img2),img3=str(img3),img4=str(img4),img5=str(img5)))
        texFileIn.write("\n")
        texFileIn.write("%========")
        # print dirr
        # files = glob.glob(dirr+"/*.out")
        # print files[0]
        # tempValues = []
        # for line in open(files[0]).readlines():
            # if re.search("     ROC AUC", line):
                # tempValues.append(line)
        dirName = str(GetTitle(dirr).replace(","," "))
        # ROCTestArea = str(tempValues[0].split()[-1])
        # ROCTrainArea = str(tempValues[1].split()[-1])
        # print("{0:56},{1:6},{2:6}\n".format(dirName,ROCTestArea,ROCTrainArea))
        # TableCSVFile.write("{0:56},{1:6},{2:6},{3:80}\n".format(dirName,ROCTestArea,ROCTrainArea,dirr))
        # TableMDFile.write("|{0:56}|{1:6}|{2:6}|{3:80}|\n".format(dirName,ROCTestArea,ROCTrainArea,dirr))
        # TabelContent.append("  %s & %s & %s \\\\ \n\\hline\n"%(str(GetTitle(dirr)),str(tempValues[0].split()[-1]),str(tempValues[1].split()[-1])))
        # TabelContent.append("  {0:56} & {1:6} & {2:6} \\\\ \n\\hline\n".format(dirName,ROCTestArea,ROCTrainArea))

# texFileIn.write(TableHeader)
# for lines in TabelContent:
    # texFileIn.write(lines)
    # TableCSVFile.write(lines.replace("%s",","))
    # TableMDFile.write(lines.replace("%s","|"))
# texFileIn.write(TableFooter)
# TableFile.write(TableFooter)
# TableCSVFile.close()
# TableMDFile.close()

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


