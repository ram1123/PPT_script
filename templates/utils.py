# -*- coding: utf-8 -*-
# @Author: Ram Krishna Sharma
# @Author Email: ram.krishna.sharma@cern.ch
# @Date:   2021-07-26
# @Last Modified by:   Ram Krishna Sharma
# @Last Modified time: 2021-07-28

from os import walk

def GetTitle(dirr,InputDirPath,ListRemoveStringFromDirName,DictReplaceString):
    # Title = dirr
    Title = dirr.replace(InputDirPath,"")
    for RemoveString in ListRemoveStringFromDirName:
        Title = Title.replace(RemoveString,"")
    for key in DictReplaceString:
        Title = Title.replace(key,DictReplaceString[key])
    Title = Title.replace("_",", ")
    return Title

def GetDirList(InputDirPath,DirListShouldStartsWith,DirNameShouldContain):
    count=0
    GetAllDirNames = []
    for (dirpath, dirnames, filenames) in walk(InputDirPath):
        # print ("dirpath: ",dirpath)
        for name in dirnames:
            for DirListStartsWith in DirListShouldStartsWith:
                # if name.startswith(DirListStartsWith) and (DirNameShouldContain in DirListStartsWith):
                if name.startswith(DirListStartsWith):
                    if DirNameShouldContain in name:
                        # print ("name: ",name)
                        count += 1
                        # if count>10: break
                        GetAllDirNames.append(dirpath+name)

    GetAllDirNames.sort()
    for count_, dir_ in enumerate(GetAllDirNames):
        print("{0:3}: {1}".format(count_,dir_))
    return GetAllDirNames