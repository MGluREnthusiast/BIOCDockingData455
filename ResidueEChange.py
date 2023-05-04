import pandas as pd

NumMutations = 55

data = pd.read_csv(r'SP23 Protein-Protein Docking Data - Sheet1 (1).csv')

MutationFrame =  pd.DataFrame(data, columns=['Variant'])
LZRDFrame =  pd.DataFrame(data, columns=['LZerD MM/GBSA via HawkDock'])
GRAMMFrame =  pd.DataFrame(data, columns=['GRAMM Model 1 MM/GBSA via HawkDock'])
ClusProFrame =  pd.DataFrame(data, columns=['ClusPro Cluster 0 MM/GBSA via HawkDock'])
HDockFrame = pd.DataFrame(data, columns=['HDOCK Model 1 MM/GBSA'])


LZRDList = []
GrammList = []
ClusProList =[]
HDockList = []

for i in range(0, NumMutations):
    LZRDList.append(abs(LZRDFrame.iat[i, 0]-LZRDFrame.iat[0, 0]))
    GrammList.append(abs(GRAMMFrame.iat[i, 0]-GRAMMFrame.iat[0, 0]))
    ClusProList.append(abs(ClusProFrame.iat[i, 0]-ClusProFrame.iat[0, 0]))
    HDockList.append(abs(HDockFrame.iat[i, 0]-HDockFrame.iat[0, 0]))

valueStoreDictLZ = {}
valueStoreDictGr = {}
valueStoreDictCL = {}
valueStoreDictHD = {}

for i in range(0, NumMutations):
    valueStoreDictLZ[LZRDList[i]] = MutationFrame.iat[i, 0]
    valueStoreDictGr[GrammList[i]] = MutationFrame.iat[i, 0]
    valueStoreDictCL[ClusProList[i]]= MutationFrame.iat[i, 0]
    valueStoreDictHD[HDockList[i]]= MutationFrame.iat[i, 0]

def Nmaxelements(list1, N, ListNam):
    newerList = pd.Series(list1).dropna()
    workaround = newerList.tolist()
    here = sorted(workaround)
    outputList = []
    #print(here)
    newList =[]
    for i in range(N):
        newList.append(here[-(i+1)])

    for i in range(N):
        if ListNam == 0:
            outputList.append([newList[i], valueStoreDictLZ[newList[i]]])
        elif ListNam == 1:
            outputList.append([newList[i], valueStoreDictGr[newList[i]]])
        elif ListNam == 2:
            outputList.append([newList[i], valueStoreDictCL[newList[i]]])
        else:
            outputList.append([newList[i], valueStoreDictHD[newList[i]]])

    return outputList



print(Nmaxelements(LZRDList, 3, 0))
print(Nmaxelements(GrammList, 3, 1))
print(Nmaxelements(ClusProList, 3, 2))
print(Nmaxelements(HDockList, 3, 3))






