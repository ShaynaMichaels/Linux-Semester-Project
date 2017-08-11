#!/usr/bin/env python3
import gzip

presidents = [("Obama", "10", "12", "14"), ("Obama", "06", "08", "22"), ("Bush2", "02", "04", "06"), ("Bush2", "98", "00", "22"), ("Clinton", "94", "96", "98"), ("Clinton", "90", "92", "22"), ("Bush", "86", "88", "90"), ("Reagan", "82", "84", "86")]

path = "/home/shayna/SemesterProject/"
outFile = open("/home/shayna/SemesterProject/finalFile", "w")


print("beginning")
#open the files:
for p in range (len(presidents)):
    matchesFile = open(path+"sortedMatches_"+presidents[p][0])
    for line in matchesFile:
        found = False
        fields = line.split("|")
        commID = fields[3]
        for i in range(1,4):
            commFile = open(path+"cm"+presidents[p][i]+".zip.txt")
            candFile = open(path+"new_cn"+presidents[p][i]+".zip.txt")
            if found == False:
                    for line in commFile:
                            commFields = line.split("|")
                            if commID.strip() == (commFields[0]).strip(): #if the commID in the matchesFile matches the commID in the cm file
                                    candID = commFields[14]
                                    for line in candFile:
                                            candFields = line.split("|")
                                            if candID.strip() == (candFields[0]).strip():
                                                    info = fields[0]+"|"+fields[1]+"|"+fields[2]+"|"+(candFields[1]).strip()+"\n"
                                                    outFile.writelines(info)
                                                    found = True
            commFile.close()
            candFile.close()
    matchesFile.close()
        
outFile.close()

