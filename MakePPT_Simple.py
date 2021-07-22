# -*- coding: utf-8 -*-
# @Author: Ram Krishna Sharma
# @Author Email: ram.krishna.sharma@cern.ch
# @Date:   2021-07-21
# @Last Modified by:   Ram Krishna Sharma
# @Last Modified time: 2021-07-22
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
from frames import frameThreeImageInLine2

texFileIn = open(OutPutTexFileName,'w')

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


# Step-2: How to grab appropriate image
count=0
GetAllDirNames = []
for (dirpath, dirnames, filenames) in walk(InputDirPath):
    for name in dirnames:
        for DirListStartsWith in DirListShouldStartsWith:
            # if name.startswith(DirListStartsWith) and (DirNameShouldContain in DirListStartsWith):
            if name.startswith(DirListStartsWith):
                if DirNameShouldContain in name:
                    count += 1
                    # if count>10: break
                    GetAllDirNames.append(dirpath+name)


GetAllDirNames.sort()

def GetTitle(dirr):
    # Title = dirr
    Title = dirr.replace(InputDirPath,"")
    for RemoveString in ListRemoveStringFromDirName:
        Title = Title.replace(RemoveString,"")
    for key in DictReplaceString:
        Title = Title.replace(key,DictReplaceString[key])
    Title = Title.replace("_",", ")
    return Title

texFileIn.write("%================================================\n\n")
for dirr in GetAllDirNames:
    img1=dirr+"/plots/history_loss.png"
    img2=dirr+"/plots/history_acc.png"
    img3=dirr+"/plots/MultiClass_ROC_dataset_test.png"
    img4=dirr+"/plots/MultiClass_ROC_dataset_train.png"
    img5=dirr+"/plots/DeepExplainer_Bar_sigmoid_y0.png"
    if os.path.exists(img3):
        texFileIn.write((frameThreeImageInLine2).format(title=str(GetTitle(dirr)),img1=str(img1),img2=str(img2),img3=str(img3),img4=str(img4),img5=str(img5)))
        texFileIn.write("\n")
        texFileIn.write("%========")
        dirName = str(GetTitle(dirr).replace(","," "))


# Step-3: Write latex footer
texFileIn.write(LatexFooter)
texFileIn.close()

LatexCommand = 'pdflatex '+OutPutTexFileName
MoveTexFile = 'mv  '+OutPutTexFileName+ " pdffile/"
MovePdfFile = 'mv  '+OutPutTexFileName.replace('.tex','.pdf')+ " pdffile/"

print(LatexCommand)
os.system(LatexCommand)
os.system(LatexCommand)
print(MoveTexFile)
os.system(MoveTexFile)
print(MovePdfFile)
os.system(MovePdfFile)

print('make clean')
os.system('make clean')

