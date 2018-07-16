Intervals = {}
Segments = {}
Cycles = {}
ImportantCycles ={}
CS = {} #Dictionary with Important cycle info and segments info
dontCare = []

##I want to make this an ??object?? (function?) that reads files ... necessary?
with open("Data\Cycles\FF-3_amplicon1_cycles.txt","r") as file:
    for skipLine in file:
        line = skipLine[:len(skipLine) -1].split("\t")
        if(line[0] == "Interval"):
                num = line[1]#single and double digit values
                chrom = line[2]
                spliceOne = line[3]
                spliceTwo = line[4]
                Intervals[int(num)] = [chrom,spliceOne,spliceTwo]
        elif(line[0] == "Segment"):
            num = line[1]
            chrom = line[2]
            spliceOne = int(line[3])
            spliceTwo = int(line[4])
            segLen = spliceTwo-spliceOne
            #print(segLen)
            Segments[int(num)] = [chrom,spliceOne,spliceTwo,segLen]
            segLen =0 
        elif (line[0].split("=")[0] == "Cycle"):
            lineAux = line[0].split(";")
            #print(lineAux)
            numAux = lineAux[0].split("=")
            num = numAux[1]
            countAux = lineAux[1]
            cAux = lineAux[2].split("=")
            cycleAux1 = cAux[1].split(",")
            #print(cycleAux1)
            #print("--------")
            listSegments = []
            for foo in cycleAux1:
                foo = foo.split("-")
                foo = foo[0].split("+")
                listSegments.append(int(foo[0]))
            #print(listSegments)
            length = 0
            for segmentNum in listSegments:
                if segmentNum != 0:
                    #print(segmentNum)
                    #print(Segments[segmentNum][3])
                    length += Segments[int(segmentNum)][3]

            #print(length)
            Cycles[int(num)] = [listSegments,length]

for x in range(1,len(Cycles)+1):
    if 0 not in Cycles[x][0]:
        if Cycles[x][1]>10000:
            ImportantCycles[x] = Cycles[x]

#print(ImportantCycles)
#print("-----------------------------------------------------------------------------")
y =0
for i in range (1,len(ImportantCycles)+1):
    #print(i)
    if i in ImportantCycles.keys():
        for x in ImportantCycles[i][0]:
            #print(x)
            #print(str(Segments[x][1]) + "---"+ str(Segments[x][2]))
            #print(str(Segments[x][0])+"---"+str(Segments[x][1])+"---"+str(Segments[x][2]))
            if x in CS.keys():
                y += i + .1
                CS[y]= [Segments[x][0],Segments[x][1],Segments[x][2]]
                continue
            CS[i]= [Segments[x][0],Segments[x][1],Segments[x][2]]
            #a= {Segments[x][0],Segments[x][1],Segments[x][2]}
    y=0


#print(CS)