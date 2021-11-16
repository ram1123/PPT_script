# -*- coding: utf-8 -*-
# @Author: Ram Krishna Sharma
# @Author Email: ram.krishna.sharma@cern.ch
# @Date:   2021-07-21
# @Last Modified by:   Ram Krishna Sharma
# @Last Modified time: 2021-08-06
import os
import time
import datetime
import sys
import glob
from os import walk
import re
import time
import json

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-c", "--config", type=str, default="config.json", help = "configuration file name")
args = parser.parse_args()

# json_file = open("config.json")
# json_file = open("config_binaryDNN.json")
json_file = open(args.config)
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
DirNameShouldContain2       = variables["DirNameShouldContain2"]
ListRemoveStringFromDirName = variables["ListRemoveStringFromDirName"]
DictReplaceString           = variables["DictReplaceString"]
GetPlots                    = variables["GetPlots"]
GetROCAreaSummary           = variables["GetROCAreaSummary"]
GetVarRankingPlots          = variables["GetVarRankingPlots"]
ifMultiClass                = variables["ifMultiClass"]

cwd = os.getcwd()
sys.path.insert(0, os.path.join(cwd,"templates"))
from header_footer import LatexHeader, LatexFooter
from frames import frame_DNN_LeftEpoch_CenterROC_RightRanking
from frames import frame_OneImageRotate90Deg
from frames import frame_TwoColumns_BinaryDNN

from utils import GetTitle, GetDirList, ExecuteCommand

texFileIn = open(OutPutTexFileName,'w')
if (GetVarRankingPlots): texFileInVarRanking = open(OutPutTexFileName.replace('.tex','_varRanking.tex'),'w')

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

if (GetVarRankingPlots):
    texFileInVarRanking.write(
        LatexHeader.format(
            SlideTitle=SlideTitle,
            SlideSubTitle=SubTitleOfSlide,
            author=AuthorNames,
            institute=InstituteName,
            instLogo=InstituteLogoWithRelativePath
            )
        )


GetAllDirNames = GetDirList(InputDirPath,DirListShouldStartsWith,DirNameShouldContain,DirNameShouldContain2)

texFileIn.write("%================================================\n\n")
GotAnyImages = False

if ifMultiClass == 0:
    for dirr in GetAllDirNames:
        img1=dirr+"/plots/all_metrics.png"
        img2=dirr+"/plots/overfitting_plot_BinaryClassifier_Binary.png"
        img3=dirr+"/plots/ROC.png"
        if os.path.exists(img3):
            texFileIn.write((frame_TwoColumns_BinaryDNN).format(title=str(GetTitle(dirr, InputDirPath,ListRemoveStringFromDirName,DictReplaceString)),img1=str(img1),img2=str(img2),img3=str(img3)))
            texFileIn.write("\n")
            texFileIn.write("%========")
            GotAnyImages = True

if ifMultiClass == 1:
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

if (GetVarRankingPlots):
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

if (GetVarRankingPlots): texFileInVarRanking.write(LatexFooter)
if (GetVarRankingPlots): texFileInVarRanking.close()

LatexCommand1 = 'pdflatex '+OutPutTexFileName
LatexCommand2 = 'pdflatex '+OutPutTexFileName.replace('.tex','_varRanking.tex')
MoveTexFile1 = 'mv  '+OutPutTexFileName+ " pdffile/"
MovePdfFile1 = 'mv  '+OutPutTexFileName.replace('.tex','.pdf')+ " pdffile/"
MovePdfFile2 = 'mv  '+OutPutTexFileName.replace('.tex','_varRanking.pdf')+ " pdffile/"
MoveTexFile2 = 'mv  '+OutPutTexFileName.replace('.tex','_varRanking.tex')+ " pdffile/"

if GetPlots == 1:
    ExecuteCommand(LatexCommand1)
    time.sleep(2)
    ExecuteCommand(LatexCommand1)
    ExecuteCommand(MoveTexFile1)
    ExecuteCommand(MovePdfFile1)

    if (GetVarRankingPlots): ExecuteCommand(LatexCommand2)
    if (GetVarRankingPlots):
        time.sleep(2)
        ExecuteCommand(LatexCommand2)
    if (GetVarRankingPlots): ExecuteCommand(MoveTexFile2)
    if (GetVarRankingPlots): ExecuteCommand(MovePdfFile2)


print('make clean')
os.system('make clean')


if GetROCAreaSummary == 1 and ifMultiClass == 1:
    print("{0:55},{1:5},{2:5},{3:5}".format("DirName","WWgg","bbgg","bkg"))
    for dirr in GetAllDirNames:
        files = glob.glob(dirr+"/*.out")
        tempValues = []
        for line in open(files[0]).readlines():
            if re.search("     ROC AUC \(Test", line):
                # print(line)
                tempValues.append(line)
        dirName = str(GetTitle(dirr, InputDirPath,ListRemoveStringFromDirName,DictReplaceString).replace(","," "))
        print("tempValues: {}".format(tempValues))
        ROCTestArea_WW = str(tempValues[0].split()[-1])
        ROCTestArea_bb = str(tempValues[1].split()[-1])
        ROCTestArea_bkg = str(tempValues[2].split()[-1])
        dirName_ = ((dirr.split('/')[-1]).replace("_BalanceYields","")).replace("HHWWyyDNN_","")
        print("{0:55},{1:5},{2:5},{3:5}".format(dirName_,ROCTestArea_WW,ROCTestArea_bb,ROCTestArea_bkg))

if GetROCAreaSummary == 1 and ifMultiClass == 0:
    print("{0:121},{1:7},{2:5},{3},{4}".format("DirName","Test","Train","Dir Full path","Creation Time Stamp"))
    for dirr in GetAllDirNames:
        files = glob.glob(dirr+"/*.out")
        tempValues = []
        # print("length of files: {}".format(len(files)))
        if len(files) == 0: continue
        for line in open(files[0]).readlines():
            if re.search("     ROC AUC \(Test", line):
                # print(line)
                tempValues.append(line)
            if re.search("     ROC AUC \(Train", line):
                # print(line)
                tempValues.append(line)
        dirName = str(GetTitle(dirr, InputDirPath,ListRemoveStringFromDirName,DictReplaceString).replace(","," "))
        # print("tempValues: {}".format(tempValues))
        # print("len(tempValues): {}".format(len(tempValues)))
        if len(tempValues) == 0: continue
        ROCTestArea_WW = str(tempValues[0].split()[-1])
        ROCTrainArea_WW = str(tempValues[1].split()[-1])
        # dirName_ = ((dirr.split('/')[-1]).replace("_BalanceYields","")).replace("HHWWyyDNN_","")
        dirName_ = (dirr.split('/')[-1])
        modelCreationTimeStamp = str(time.ctime(os.path.getmtime(dirr+"/model.pb")))
        # print(modelCreationTimeStamp)
        print("{0:121},{1:7},{2:5},{3},{4}".format(dirName_,ROCTestArea_WW,ROCTrainArea_WW,dirr+"/model.pb",modelCreationTimeStamp))
