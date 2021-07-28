# -*- coding: utf-8 -*-
# @Author: Ram Krishna Sharma
# @Author Email: ram.krishna.sharma@cern.ch
# @Date:   2021-07-21
# @Last Modified by:   Ram Krishna Sharma
# @Last Modified time: 2021-07-28
import os
import sys
import glob
from os import walk
import re

import json


json_file = open("config.json")
variables = json.load(json_file)
json_file.close()

AuthorNames                 = variables["AuthorNames"]
InstituteName               = variables["InstituteName"]
InstituteLogoWithRelativePath = variables["InstituteLogoWithRelativePath"]
SlideTitle                  = variables["SlideTitle"]
SubTitleOfSlide             = variables["SubTitleOfSlide"]
InputDirPath                = variables["InputDirPath"]
OutPutTexFileName           = variables["OutPutTexFileName"]
DirListShouldStartsWith     = variables["DirListShouldStartsWith"]
DirNameShouldContain        = variables["DirNameShouldContain"]
ListRemoveStringFromDirName = variables["ListRemoveStringFromDirName"]
DictReplaceString           = variables["DictReplaceString"]

cwd = os.getcwd()
sys.path.insert(0, os.path.join(cwd,"templates"))
from header_footer import LatexHeader, LatexFooter
from frames import frame_DNN_LeftEpoch_CenterROC_RightRanking, frame_OneImageRotate90Deg

from utils import GetTitle, GetDirList

texFileIn = open(OutPutTexFileName,'w')
texFileInVarRanking = open(OutPutTexFileName.replace('.tex','_varRanking.tex'),'w')

# Step-1: Write latex header
texFileIn.write(
    LatexHeader.format(
        SlideTitle=SlideTitle,
        SlideSubTitle=SubTitleOfSlide,
        author=AuthorNames,
        institute=InstituteName,
        instLogo=InstituteLogoWithRelativePath
        )
    )

texFileInVarRanking.write(
    LatexHeader.format(
        SlideTitle=SlideTitle,
        SlideSubTitle=SubTitleOfSlide,
        author=AuthorNames,
        institute=InstituteName,
        instLogo=InstituteLogoWithRelativePath
        )
    )

# Step-2: How to grab appropriate image
# count=0
# GetAllDirNames = []
# for (dirpath, dirnames, filenames) in walk(InputDirPath):
#     for name in dirnames:
#         for DirListStartsWith in DirListShouldStartsWith:
#             # if name.startswith(DirListStartsWith) and (DirNameShouldContain in DirListStartsWith):
#             if name.startswith(DirListStartsWith):
#                 if DirNameShouldContain in name:
#                     count += 1
#                     # if count>10: break
#                     GetAllDirNames.append(dirpath+name)

# GetAllDirNames.sort()

GetAllDirNames = GetDirList(InputDirPath,DirListShouldStartsWith,DirNameShouldContain)

texFileIn.write("%================================================\n\n")
GotAnyImages = False
for dirr in GetAllDirNames:
    img1=dirr+"/plots/history_loss.png"
    img2=dirr+"/plots/history_acc.png"
    img3=dirr+"/plots/MultiClass_ROC_dataset_test.png"
    img4=dirr+"/plots/MultiClass_ROC_dataset_train.png"
    img5=dirr+"/plots/DeepExplainer_Bar_sigmoid_y0.png"
    if os.path.exists(img3):
        texFileIn.write((frame_DNN_LeftEpoch_CenterROC_RightRanking).format(title=str(GetTitle(dirr, InputDirPath,ListRemoveStringFromDirName,DictReplaceString)),img1=str(img1),img2=str(img2),img3=str(img3),img4=str(img4),img5=str(img5)))
        texFileIn.write("\n")
        texFileIn.write("%========")
        GotAnyImages = True

for dirr in GetAllDirNames:
    # img1=dirr+"/plots/DeepExplainer_Bar_sigmoid_y0.png"
    img1=dirr+"/plots/DeepExplainer_Bar_sigmoid_y0_all.png"
    if os.path.exists(img3):
        texFileInVarRanking.write((frame_OneImageRotate90Deg).format(title=str(GetTitle(dirr, InputDirPath,ListRemoveStringFromDirName,DictReplaceString)),img1=str(img1)))
        texFileInVarRanking.write("\n")
        texFileInVarRanking.write("%========")

if GotAnyImages == False:
    print("No image found. Existing...")
    exit()

# Step-3: Write latex footer
texFileIn.write(LatexFooter)
texFileIn.close()

texFileInVarRanking.write(LatexFooter)
texFileInVarRanking.close()

LatexCommand1 = 'pdflatex '+OutPutTexFileName
LatexCommand2 = 'pdflatex '+OutPutTexFileName.replace('.tex','_varRanking.tex')
MoveTexFile1 = 'mv  '+OutPutTexFileName+ " pdffile/"
MovePdfFile1 = 'mv  '+OutPutTexFileName.replace('.tex','.pdf')+ " pdffile/"
MovePdfFile2 = 'mv  '+OutPutTexFileName.replace('.tex','_varRanking.pdf')+ " pdffile/"
MoveTexFile2 = 'mv  '+OutPutTexFileName.replace('.tex','_varRanking.tex')+ " pdffile/"

print(LatexCommand1)
os.system(LatexCommand1)
os.system(LatexCommand1)
print(MoveTexFile1)
os.system(MoveTexFile1)
print(MovePdfFile1)
os.system(MovePdfFile1)

# os.system(LatexCommand2)
# os.system(LatexCommand2)
os.system(MoveTexFile2)
# os.system(MovePdfFile2)

print('make clean')
os.system('make clean')

