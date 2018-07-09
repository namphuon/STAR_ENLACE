import GeneMatcher
from GeneMatcher import *

CSOnco ={}
lineNum = 1

for x in CS:
    CSOnco[x] = [CS[x][0],CS[x][1],CS[x][2]]

with open("Data\AllOncoAux.tsv", "r") as file:
    for line in file:
        if line[0] == '#':
            continue
        #print(lineNum)
        lineNum += 1
        res = line.split('\t')
        symbol = res[1]
        prevSymbols = res[2]
        synonyms = res[3]
        name = res[4]
        listaNombres= symbol + prevSymbols + synonyms + name
        listaNombres=listaNombres.split('"')
        print(listaNombres)
        for x in range(1,len(CS)):
           for y in listaNombres:
                print(y)
                print(CS[x])
                if y in CS[x]:
                    print("entre al if")
                    CSOnco[x]+y
            print("this is X" +str(x))

for x in CSOnco:
    print(CSOnco[x])
