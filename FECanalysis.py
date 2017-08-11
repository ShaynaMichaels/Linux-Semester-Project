#!/usr/bin/env python3
import gzip
import jellyfish
import re

presidents = [("Obama", "10", "12", "14"), ("Obama", "06", "08", "22"), ("Bush2", "02", "04", "06"), ("Bush2", "98", "00", "22"), ("Clinton", "94", "96", "98"), ("Clinton", "90", "92", "22"), ("Bush", "86", "88", "90"), ("Reagan", "82", "84", "86")]
#22 is a placeholder.  Anytime a file is accessed that is 22, it is a blank file so each tuple could be the same length and there wouldn't be repeated data analysis

path = "/home/shayna/SemesterProject/"

def changeNames(inputFile):
   global fields
   print("Trying to process file", inputFile)
   first = True
   l = None
   while first or l: #change name to be first name last name
      first = False
      try:
        l = inputFile.readline()
        flds = l.split("|")
        eighth = flds[7]
        new8 = eighth.strip()
        n = new8.split(",") #split into a list of last name, first name
        if (len(n)>1): #to not include empty fields so index isn't out of range
           line = (n[1]).strip()+" "+ n[0]
           fields= flds
           yield line
      except:
        pass
   print("Done with file", inputFile)

for p in range(len(presidents)):
  Afile = "Anames_"+presidents[p][0] #open the Ambassador name file
  AmbassFile = open("/home/shayna/SemesterProject/"+Afile)
   
  if (p == 0):
     outFile = open("/home/shayna/SemesterProject/matches_"+presidents[p][0], "w")
  elif (p != 0):
     if (presidents[p][0] != presidents[p-1][0]):
        outFile = open("/home/shayna/SemesterProject/matches_"+presidents[p][0], "w") #if it's not the first president and it's not the same as the one before it, open the file
 

  for i in range(1,4): #going through each president's tuple and opening up the indiv file for the three years recorded
    if (int(presidents[p][i]) >= 4 and int(presidents[p][i])< 17): #if it's a .gz, open .gz
      inputFile = "indiv"+presidents[p][i]+".gz"
      if i == 1: #whatever i equals, that should be the end number of the file name
        inputFile1 = gzip.open(path+inputFile, "rt")
      if i == 2:
        inputFile2 = gzip.open(path+inputFile, "rt")
      else:
        inputFile3 = gzip.open(path+inputFile, "rt")
    else:
      inputFile = "indiv"+presidents[p][i]+".zip.txt" #if it's a .txt, open
      if i == 1:
        inputFile1 = open(path+inputFile)
      if i ==2:
        inputFile2 = open(path+inputFile)
      else:
        inputFile3 = open(path+inputFile)
  
   
        
  for line in changeNames(inputFile1):
     for name in AmbassFile: 
        if (jellyfish.jaro_distance(name, line)>=.91):
           info = fields[7]+"|"+fields[8]+","+fields[9]+","+fields[10]+"|"+fields[14]+"|"+fields[0]+"\n" #output name, address, amount, committee contributed to
           #print(info)
           outFile.writelines(info)
     AmbassFile.close()
     AmbassFile = open("/home/shayna/SemesterProject/"+ Afile)
        #have to reopen this so it starts at the beginning again
     
  inputFile1.close()

  for line in changeNames(inputFile2):
     for name in AmbassFile: 
        if (jellyfish.jaro_distance(name, line)>=.91):
           info = fields[7]+"|"+fields[8]+","+fields[9]+","+fields[10]+"|"+fields[14]+"|"+fields[0]+"\n" #output name, address, amount, committee contributed to
           #print(info)
           outFile.writelines(info)
     AmbassFile.close()
     AmbassFile = open("/home/shayna/SemesterProject/"+ Afile)

  inputFile2.close()

  for line in changeNames(inputFile3):
     for name in AmbassFile: 
        if (jellyfish.jaro_distance(name, line)>=.91):
           info = fields[7]+"|"+fields[8]+","+fields[9]+","+fields[10]+"|"+fields[14]+"|"+fields[0]+"\n" #output name, address, amount, committee contributed to
           #print(info)
           outFile.writelines(info)
     AmbassFile.close()
     AmbassFile = open("/home/shayna/SemesterProject/"+ Afile)
  inputFile3.close()
  AmbassFile.close()
  
  if(p != len(presidents)-1):
     if (presidents[p][0] != presidents[p+1][0]):
        outFile.close()
        #if it's not the last one and the one after it is not the same, close it
  elif (p == len(presidents)-1):
     outFile.close()




