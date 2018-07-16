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


#for i in turner: 
#	print(turner[i])





def Intersegments(x,y,x1,y1): 
	return((x>=x1 and x<=y1) or (x1>=x and x1<=y))

class FF:
    """docstring for FF"""
    def __init__(self, intervals, cycles, segments):
        self.intervals = intervals
        self.segments = segments
        self.cycles = cycles


#MAIN 


a = cicleReader("Data\Cycles\FF-5_amplicon1_cycles.txt")
f = FF(a[0],a[1],a[2])


	
#geneList

#for i in geneList:
    #print(i)
#print("------------")
#print (turner)
#print("------------")
#print(a[2])
aux = set()
aux2 = set()
writeStuff= ""
countBools = 0
for nc in f.cycles:
	#print(f.cycles[nc][1:2])
	for i in geneList:
		#print(i[1:2][0])
		if f.cycles[nc][1:2]!= "" and f.cycles[nc][2:3]!= "" and i[1:2][0]!= "" and i[2:3][0]!= "":
			if Intersegments(int(f.cycles[nc][1:2][0]),int(f.cycles[nc][2:3][0]),int(i[1:2][0]),int(i[2:3][0])):
				b = a[2][nc][3]
				#print(b)
				#print("Cycle info " + str(a[2][nc]) + " geneName" + str(i[4:5]) )
				#print("Entre al ultimo if")ssssss
				#c = "Sample "+"FF-4" + "; Cycle info " + str(a[2][nc]) + "; geneName" + str(i[4:5])
				for x in turner:
					for j in turner[x]:
						#print("Entre a los 2 for")
						if len(j)>1:
							aux.add(j)
					if b:
						countBools += 1
						#print(countBools)
						aux2.add(str(i[4:5]) + ",")
					#print (aux)
					if countBools>= 1:
						writeStuff+=("Sample "+"FF-4" + "\t Turner info: "+ str(aux) + "\t All genes:" + str(i[4:5])+ "\t Cycle Genes:" + str(aux2) + "\t Has a cycle -> YES \n\n" )
					else:
						writeStuff+=("Sample "+"FF-4" + "\t Turner info: "+ str(aux) + "\t All genes:" + str(i[4:5])+ "\t Cycle Genes:" + str(aux2) + "\t Has a cycle -> NO\n\n" )
					aux2.clear()
					aux.clear()
				#continue
		#aux = ""


with open("prueba.txt","w") as file2:
	file2.write(writeStuff)
	#file2.write(str(geneList))

