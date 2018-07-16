x = []
longList = []



#with open("Data\gene.annotation.gff.filtered","r") as file: #parsing Gene ID file and creating x (pre-sorted geneList)
with open("Data\AuxiliarGene.txt","r") as file: #parsing Gene ID file and creating x (pre-sorted geneList)
    for skipLine in file:
        #print("Running...")
        line = skipLine.split("\t")
        if(line[0][0] == "c"):
            chrom = line[0]
            spliceOne = int(line[3])
            spliceTwo = int(line[4])
            x = line[8].split(";")
            geneID = x[0]
            xx = x[4].split(" ")
            geneName = xx[2]
            longList.append([chrom,spliceOne,spliceTwo,geneID,geneName])
          #  x = remove_duplicates(longList)


geneList = sorted(longList, key=lambda longList: longList[1])
#this is the sorter 

#print (geneList)


