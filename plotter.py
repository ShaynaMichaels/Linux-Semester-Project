#!/usr/bin/env python3

import matplotlib.pyplot as plt


names = ["OBAMA, BARACK", "BUSH, GEORGE W", "CLINTON, WILLIAM JEFFERSON", "BUSH, GEORGE", "REAGAN, RONALD"]
lastNames = ['B.OBAMA', 'GW.BUSH', 'WJ.CLINTON', 'G.BUSH', 'R.REAGAN']
ans = []
for i in range(len(names)):
    money = 0
    mTotal = 0
    fin = open("/home/shayna/SemesterProject/finalFile")
    for line in fin:
        fields = line.split("|")
        if fields[3].strip() == names[i].strip(): #if the candName is the same
            times = fields[0].strip().split(" ") #split the first field because the beginning has the number of entries that were the same
            contAmount = int(fields[2])
            if contAmount < 0:
                contAmount *= -1
            money = contAmount*int(times[0])
            mTotal +=money
    ans.append(mTotal)
    fin.close()



f = plt.figure()

plt.xticks([1,2,3,4,5],lastNames)
plt.xlabel("President")
plt.ylabel("Money contributed by later-appointed ambassadors")
plt.scatter([1,2,3,4,5],ans)

plt.show()
f.savefig("scatterPlot.pdf")
