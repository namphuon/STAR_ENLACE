import Project1
from Project1 import *
Genes = {}
j=0
lineCareAbout = {}

def Intersegments(x,y,x1,y1): 
	return((x>=x1 and x<=y1)or(x1>=x and x1<=y)) #Si HAY ERROR CHECAR QUE LAS Y´s SEAN MAYORES QUE LAS X´s 

print("GeneParseEnters")
with open("Data\Genes_July_2010_hg19.gff","r") as file:
	i = 0 #Just a counter to skip first line
	for skipLine in file:
		num = 1
		if i != 0:
			line = skipLine[:len(skipLine) -1].split("\t")
			#print (line)
			geneName = line[0]
			#print(geneName)
			coordX = line[3]
			coordY = line[4]
			ID = line[8].split(";")[0][3:]
			for x in CS:
				#print(CS[x])
				if geneName==CS[x][0]:
					#print(j)
					#print("I get through the while cause "+ geneName + " == " + CS[x][0])
					#print(CS[num][2])
					if Intersegments(int(CS[x][1]),int(CS[x][2]),int(coordX),int(coordY)):
						#print("Intersectiooon!!!!!")
						#print(Intersegments(int(CS[x][1]),int(CS[x][2]),int(coordX),int(coordY)))
						CS[x].append(ID)
					j+=1	            
			#print(ID)
			#lineCareAbout[geneName] = [ID,coordX,coordY]
			#print(geneName +"---"+ coordX +"---"+ coordY)
		i = 1

for x in CS.keys():
	print(str(x)+ "------------------")
	print (CS[x])
	#CS[1].append("Holisssssssss")

#print(Intersegments(22,33,33,40))
