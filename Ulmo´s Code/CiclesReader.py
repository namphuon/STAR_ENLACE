Intervals = {}
Segments = {}
Cycles = {}
ImportantCycles ={}
CS = {} #Dictionary with Important cycle info and segments info
dontCare = []


##I want to make this an ??object?? (function?) that reads files ... necessary?
def cicleReader(nameFile):
    Segments[0] = ""
    with open(nameFile) as file:
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
                boolean = True
                for segmentNum in listSegments:
                    # ------------------------------------------------------- segment 0 
                    if segmentNum != 0:
                        length += Segments[int(segmentNum)][3]
                        #print(segmentNum)
                        #print(segmentNum)
                        #print(Segments[segmentNum][3])
                    else:
                        boolean = False
                Cycles[int(num)] = [listSegments,length,boolean]
                #print(length)
    #print(Cycles)
    for x in range(1,len(Cycles)+1):
        if Cycles[x][1]>10000:
            #print(Cycles[x][0])
            if 0 not in Cycles[x][0]:
                ImportantCycles[x] = Cycles[x]
            else:
                ImportantCycles[x] = ""
    #print("-----------------------------------------------------------------------------")            
    #print(Cycles)
    #print(Cycles[1][0])
    y =0

    for i in range (1,len(Cycles)+1): #Para cada ciclo
        if i in Cycles.keys():        #Si i esta en las llaves del ciclo
            #if 0 not in Cycles[i][0]:
            for x in Cycles[i][0]: #Para cada elemento de la lista de segmentos
                if x !=0:
                    #print(Cycles[i][0])
                    #print(x)
                    #print(i)
                    #print("---")
                    if i in CS.keys():
                        y += i + .1
                        #print(Cycles[i][2])
                        CS[y]= [Segments[x][0],Segments[x][1],Segments[x][2],Cycles[i][2]]
                    else:
                        #print(Cycles[i][2])
                        CS[i]= [Segments[x][0],Segments[x][1],Segments[x][2],Cycles[i][2]]
            #else:
                #ELIMINA LOS CEROS DE LA LISTA Y HAS LO DE ARRIBA
                
                

                #print("Hay ceros")
    y=0
    #print (CS)
    return [Intervals,Segments,CS]