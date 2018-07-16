import Project1
from Project1 import *

ensemble_data = []
#ensemble_map = {}
count =0
listID = []

def Intersegments(x,y,x1,y1): 
	return((x>=x1 and x<=y1)or(x1>=x and x1<=y))

with open("Data\gene.annotation.gff.filtered", "r") as file:
#with open("Data\AuxiliarGene.txt", "r") as file:
	for line in file:
		if line[0] == '#':
			continue
		res = line.split('\t')
		info = dict([r.strip().replace('"', '').split(' ') for r in res[-1].split('; ') if len(r.split(' ')) == 2])
		temp = [res[0], int(res[3]), int(res[4]), {'data': info}]
		ensemble_data.append(temp)
		chrName = temp[0]
		ID = info['gene_name']
		for x in CS:
			if chrName == CS[x][0]:
				if Intersegments(int(CS[x][1]),int(CS[x][2]),int(temp[1]),int(temp[2])):
					if ID not in CS[x]:
						CS[x].append(ID)
	
	for x in CS:
		print(CS[x])

	#for i in range(0, len(ensemble_data)):
		#print(ensemble_data[i])
