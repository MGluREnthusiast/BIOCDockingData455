import pandas as pd
import numpy as np

data = pd.read_csv(r'SP23 Protein-Protein Docking Data - Sheet1 (1).csv')

colorFrame =  pd.DataFrame(data, columns=['Blue or Yellow from Procko Paper?'])
LZRDFrame =  pd.DataFrame(data, columns=['LZerD MM/GBSA via HawkDock'])
GRAMMFrame =  pd.DataFrame(data, columns=['GRAMM Model 1 MM/GBSA via HawkDock'])
ClusProFrame =  pd.DataFrame(data, columns=['ClusPro Cluster 0 MM/GBSA via HawkDock'])
HDockFrame = pd.DataFrame(data, columns=['HDOCK Model 1 MM/GBSA'])

colorlist = []
updatedColors = []
LZRDList = []
GrammList = []
ClusProList =[]
HDockList = []

NumMutations = 62

for i in range(0, NumMutations):
    colorlist.append(colorFrame.iat[i, 0])
    LZRDList.append(LZRDFrame.iat[i, 0])
    GrammList.append(GRAMMFrame.iat[i, 0])
    ClusProList.append(ClusProFrame.iat[i, 0])
    HDockList.append(HDockFrame.iat[i, 0])

for j in colorlist:
    if j == "blue" or j == "Blue":
        updatedColors.append(1)
    elif j == "n/A":
        updatedColors.append(2)
    else:
        updatedColors.append(0)

ValidEntries = {"Lzrd" : 0, "Gramm" : 0, "Hdock" : 0, "ClussPro": 0}
MissingEntries = {"Lzrd" : 0, "Gramm" : 0, "Hdock" : 0, "ClussPro": 0}


for i in range(1, NumMutations):
    if np.isnan(LZRDList[i]): MissingEntries["Lzrd"] += 1
    if np.isnan(GrammList[i]): MissingEntries["Gramm"] += 1
    if np.isnan(ClusProList[i]): MissingEntries["ClussPro"] += 1
    if np.isnan(HDockList[i]): MissingEntries["Hdock"] += 1
    if updatedColors[i] == 1: ### if the entry is blue
            if LZRDList[i] <= LZRDList[0]:
                ValidEntries["Lzrd"] += 1
            if GrammList[i] <= GrammList[0]:
                ValidEntries["Gramm"] += 1
            if ClusProList[i] <= ClusProList[0]:
                ValidEntries["ClussPro"] += 1
            if HDockList[i] <= HDockList[0]:
                ValidEntries["Hdock"] += 1
    else: ### for the case where the entry is yellow
            if LZRDList[i] >= LZRDList[0]:
                ValidEntries["Lzrd"] += 1
            if GrammList[i] >= GrammList[0]:
                ValidEntries["Gramm"] += 1
            if ClusProList[i] >= ClusProList[0]:
                ValidEntries["ClussPro"] += 1
            if HDockList[i] >= HDockList[0]:
                ValidEntries["Hdock"] += 1


print(np.isnan(ClusProList[21]))
print(ValidEntries)
print(MissingEntries)
print("LZerD average ", ValidEntries["Lzrd"]/(NumMutations-MissingEntries["Lzrd"]))
print("Gramm average ",ValidEntries["Gramm"]/(NumMutations-MissingEntries["Gramm"]))
print("ClussPro average ",ValidEntries["ClussPro"]/(NumMutations-MissingEntries["ClussPro"]))
print("Hdock average ",ValidEntries["Hdock"]/(NumMutations-MissingEntries["Hdock"]))
