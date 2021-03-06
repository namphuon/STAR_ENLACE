import os
import CiclesReader
from CiclesReader import *

import GeneListSorter
from GeneListSorter import *


turner = {}


with open("Data\Turner2017_sample_list.csv","r") as file: #parsing Gene ID file and creating geneDict dictionary
    for skipLine in file:
        line = skipLine.split(",")
        name = line[0]
        idxs = line[2:]
        turner[name] = idxs

def Intersegments(x,y,x1,y1): 
    return((x>=x1 and x<=y1) or (x1>=x and x1<=y))

class FF:
    """docstring for FF"""
    def __init__(self, intervals, cycles, segments):
        self.intervals = intervals
        self.segments = segments
        self.cycles = cycles


#MAIN 
#geneList

#for i in geneList:
    #print(i)
#print("------------")
#print (turner)
#print("------------")
#print(a[2])


def writer(f,a,FfName):
    with open("prueba.txt","a") as file2:
        file2.write(FfName + "\n")
        writeStuff= ""
        #print("The writer enter the scene!!!")
        aux = set()
        aux2 = set()
        countBools = 0
        for nc in f.cycles:
            for i in geneList:
                if f.cycles[nc][1:2]!= "" and f.cycles[nc][2:3]!= "" and i[1:2][0]!= "" and i[2:3][0]!= "":
                    if Intersegments(int(f.cycles[nc][1:2][0]),int(f.cycles[nc][2:3][0]),int(i[1:2][0]),int(i[2:3][0])):
                        if nc in a[2].keys():
                            b = a[2][nc][3]
                        for x in turner:
                            if b:
                                countBools += 1
                                aux2.add(str(i[4:5]) + ",")
                            for j in turner[x]:
                                if len(j)>1:
                                    aux.add(j)
        if countBools>= 1:
            writeStuff+=("\t Turner info: "+ str(aux) + "\t All genes:" + str(i[4:5])+ "\t Cycle Genes:" + str(aux2) + "\t Has a cycle -> YES \n\n" )
        else:
            writeStuff+=("\t Turner info: "+ str(aux) + "\t All genes:" + str(i[4:5])+ "\t Cycle Genes:" + str(aux2) + "\t Has a cycle -> NO\n\n" )
        aux2.clear()
        file2.write(writeStuff)

    #print(os.getcwd()+"\Data\Cycles")
for file in os.listdir(os.getcwd()+"\Data\Cycles"):
    file2 = os.getcwd()+"\Data\Cycles\\" + file
    a = cicleReader(file2)
    f = FF(a[0],a[1],a[2])
    FFName = file[0:5]
    #print("writer de " +file +" " + str(FFName))
    writer(f,a,FFName)