import pandas as pd
import numpy as np

NumMutations = 56

data = pd.read_csv(r'SP23 Protein-Protein Docking Data - Sheet1 (1).csv')

colorFrame =  pd.DataFrame(data, columns=['Blue or Yellow from Procko Paper?'])
clusProFrame =  pd.DataFrame(data, columns=['ClusPro Cluster 0 Member Count',	'ClusPro Cluster 0 Center Energy',	'ClusPro Cluster 0 Lowest Energy'])

colorlist = []

for i in range(0, NumMutations):
    colorlist.append(colorFrame.iat[i, 0])
BinaryColors = []

for j in colorlist:
    if j == "blue" or j == "Blue":
        BinaryColors.append(1)
    elif j == "n/A":
        BinaryColors.append(2)
    else:
        BinaryColors.append(0)

HigherAffinity = {"Member Count" : [], "Center Energy": [], "Lowest Energy" : []}
LowerAffinity = {"Member Count" : [], "Center Energy": [], "Lowest Energy" : []}
for i in range(1, NumMutations):
    if BinaryColors[i] == 1:
        HigherAffinity["Member Count"].append(clusProFrame.iat[i, 0])
        HigherAffinity["Center Energy"].append(clusProFrame.iat[i, 1])
        HigherAffinity["Lowest Energy"].append(clusProFrame.iat[i, 2])
    else:
        LowerAffinity["Member Count"].append(clusProFrame.iat[i, 0])
        LowerAffinity["Center Energy"].append(clusProFrame.iat[i, 1])
        LowerAffinity["Lowest Energy"].append(clusProFrame.iat[i, 2])

HMEM = pd.Series(HigherAffinity["Member Count"]).dropna()
HCEN = pd.Series(HigherAffinity["Center Energy"]).dropna()
HLOW = pd.Series(HigherAffinity["Lowest Energy"]).dropna()
LMEM = pd.Series(LowerAffinity["Member Count"]).dropna()
LCEN = pd.Series(LowerAffinity["Center Energy"]).dropna()
LLOW = pd.Series(LowerAffinity["Lowest Energy"]).dropna()

print("Predicted Higher Affinity Results ", sum(HMEM)/len(HMEM), sum(HCEN)/len(HCEN), sum(HLOW)/len(HLOW))
print("Stdev of Higher Affinity ", np.std(HMEM), np.std(HCEN), np.std(HLOW))
print()
print("Predicted Lower Affinity Results ", sum(LMEM)/len(LMEM), sum(LCEN)/len(LCEN), sum(LLOW)/len(LLOW))
print("Stdev of Lower Affinity ", np.std(LMEM), np.std(LCEN), np.std(LLOW))

