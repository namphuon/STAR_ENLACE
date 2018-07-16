Intervals = {}
Segments= {}
Cycles = {}
#I have all the Examples in a folder called Data inside the Project folder where my python file is, if needed I can send you a SS,
#This line Opens FF-5... file so we can work with it...
with open("Data\FF-5_amplicon1_cycles.txt", "r") as file:
    #This for reads line by line the file and save the line as "line"
    for line in file:
        #lineAux just erase last character, which is an skipline :)
        lineAux =(line[:len(line)-1])
        if(lineAux[:1]== "I"):
            print("hello")
            #DO INTERVAL STUFF ----------------------------------------------------------------------------
            #print ("its an I")
            num = lineAux[9:10]
            chrom = lineAux[11:15]
            x = lineAux[16:25]
            y = lineAux[26:]
            #I´ve saved all info in a Dictionary called Intervals, we have to do the same on Segments and cicles :)
            Intervals[num] = [chrom,x,y]
        elif(lineAux[:1]== "S"):
            #DO SEGMENTS STUFF------------------------------------------------------------------------
            #YOU HAVE TO COMMENT THE PRINT LINE WITH A # WHEN YOU WRITE YOUR CODE
            print("its S")
        elif(lineAux[:1]== "C"):
            #DO CICLES STUFF--------------------------------------------------------------------
            # YOU HAVE TO COMMENT THE PRINT LINE WITH A # WHEN YOU WRITE YOUR CODE
            print("Its C")
        else:
            print("")