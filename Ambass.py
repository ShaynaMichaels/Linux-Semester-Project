#!/usr/bin/env python3
import re
import urllib.request

presidents = ["Obama", "Bush2", "Clinton", "Bush", "Reagan"]
urls = ["http://www.afsa.org/list-ambassadorial-appointments","http://www.afsa.org/ambassadorial-appointments-george-w-bush","http://www.afsa.org/ambassadorial-appointments-william-j-clinton", "http://www.afsa.org/ambassadorial-appointments-george-h-w-bush", "http://www.afsa.org/ambassadorial-appointments-ronald-reagan"]

pat = [r'">(.*)</a></td>', r'<td>(.*)</td>\n<td>[Career|Political]']


#open outputFiles for each president for writing the HTML into
for p in range (len(presidents)):
    name = presidents[p]
    htmlFile = open(name+"_html", "w")

    #open outputFiles for writing that will contain a list of names of ambassadors for each president
    outputFile = open("Anames_"+name, "w")

    f = urllib.request.urlopen(urls[p])
    data = f.read().decode()
    htmlFile.write(data) #write data from the webpages into a separate file for each president
    
    if p == 0: #if it's Obama
        Nowpat = re.compile(pat[0])
    else:
        Nowpat = re.compile(pat[1])

    if data: #if it successfully got the HTML, find the names using the regex
        found = re.findall(Nowpat, data)
    
    for f in range (len(found)): #for each element in the resulting list of ambassador names
        element = found[f]+"\n"
        element = element.upper().strip()
        found[f] = re.sub(r'[^\w\s]',"", element) #take  out all punctuation by substituting any nonalpha or nonspace char with an empty string
        ans = found[f]+"\n"
        outputFile.writelines(ans) #add \n after each element before writing and use .strip when read back in
        

    htmlFile.close()
    outputFile.close()
