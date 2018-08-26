import os.path
from os import path

dateA = []
dateB = []
desc = []
amount = []
newLine = []
p=0
payload = ""
filename = ""
filenameOut = ""
temppayloadA = ""
temppayloadB = ""

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
        payload = i
        if len(i) >= 2 and len(i) <= 7 :
            if temppayloadA == '' :
                temppayloadA = payload + '  '
            else:
                temppayloadB = payload + '  '
        else :
            if temppayloadA != '' and temppayloadB != '':
                payload = temppayloadA  + temppayloadB  + payload
            if temppayloadA != '' and temppayloadB == '':
                payload = temppayloadA  + payload
            #if payload != '':
            newLine.insert(p,payload)
            p = p+1
            temppayloadA = ''
            temppayloadB = ''

    p = 0
    print newLine
    for i in newLine:
        if i[3:4] == " ":
            a = i.find('$')
            dateA.append(i[:6])
            dateB.append(i[7:13])
            desc.append(i[14:a-1])
            amount.append(i[a:])
            #Build Output Format
            if i[a-1:a] == "-": #check for negative numbers
                payload = dateA[p] + " 2017," + desc[p] + "," + "," + amount[p] 
            else:
                payload = dateA[p] + " 2017," + desc[p] + "," + amount[p]

            p = p+1
        
        else :
            payload = "," + i     

        #Save to disk
        #if i != '':
        filesave(payload,filenameOut)

print 'Done ! - Put down your drink....'

    
   
