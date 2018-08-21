import os.path
from os import path

dateA = []
dateB = []
desc = []
Amount = []
p=0
payload = ""
filename = ""
filenameOut = ""

#Define Write to disk Routine
def filesave(payload,filenameOut):
    f = open(filenameOut,"a")
    f.write ('\r\n')
    f.write (payload)
    f.close()

#Build Output Filename from Source filename
filename = raw_input ('Please enter file name for parsing: ')
filenameOut = filename.split(".")
filenameOut = filenameOut[0] + "-output.csv"

#Check for Output Filename, If exists ask user to override or quit
if path.exists(filenameOut):
    doWhat = raw_input("File Already exists Type O to override or anykey to quit ")
    if doWhat != "O" :
        exit()
    w = open(filenameOut, "w")
    w.close()

#Parsing Engine  
with open(filename, "r") as f:
    line = f.readline()
    line = line.split("\r")
    for i in line:
        if i[3:4] == " ":
            a = i.find('$')
            dateA.append(i[:6])
            dateB.append(i[7:13])
            desc.append(i[14:a-1])
            Amount.append(i[a:])
            #Build Output Format
            payload = dateA[p] + "," + dateB[p] + "," + Amount[p] + "," + desc[p]

            p = p+1

        else :
            payload = i     

        #Save to disk    
        filesave(payload,filenameOut)

print 'Done ! - Put down your drink....'

    
   
