longList = []
geneList = []
count =0

with open("Data\AuxiliarGene.txt","r") as file: #parsing Gene ID file and creating x (pre-sorted geneList)
    for skipLine in file:
        line = skipLine.split("\t")
        if(line[0][0] == "c"):
            count+=1
            print("entre al if"+ str(count))
            chrom = line[0]
            spliceOne = int(line[3])
            spliceTwo = int(line[4])
            x = line[8].split(";")
            geneID = x[0]
            xx = x[4].split(" ")
            geneName = xx[2]
            longList.append([chrom,spliceOne,spliceTwo,geneID,geneName])



geneList = sorted(longList, key=lambda longList: longList[1])
#this is the sorter


for i in geneList:
    print(i)