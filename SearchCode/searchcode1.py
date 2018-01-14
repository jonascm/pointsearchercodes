import numpy as np
import csv
import os

#maxmiles = raw_input('max num of miles you wanna spend:')
depdate = raw_input('departure date (mmddyyyy):')
retdate = raw_input('return date (mmddyyyy):')
maxmiles = raw_input('max num of miles you wanna spend:')



onbudget = []
onbudgetmls = []
onbudgetdls = []
overbudget = []

depdatecol = -1
retdatecol = -1

for root, dirs, files in os.walk('datasets', topdown=False):
    for name in files:
        #print(name)
        if name[7] == 'm':
            # it's a miles!
            rawdata = np.loadtxt(open('datasets/'+name, "rb"), delimiter=" ", skiprows=0)
            for col in range(0,np.shape(rawdata)[1]):
                currposdate = str(int(rawdata[0][col])).zfill(8)
                if currposdate == depdate:
                    depdatecol = col-1
                if currposdate == retdate:
                    retdatecol = col
            if ((depdatecol < 0) or (retdatecol < 0)):
                print("Sorry mate, dates out of range. Try lookin at february perhaps")
            else:
                milesfordat = rawdata[depdatecol][retdatecol]
                namedoll = name[0:7]+'d'+name[8:]
                rawdatausd = np.loadtxt(open('datasets/'+namedoll, "rb"), delimiter=" ", skiprows=0)
                dollafordat = rawdatausd[depdatecol][retdatecol]
                strng = 'Checking ' + name[0:6] + ': miles = ' + str(milesfordat) + ' + ' + str(dollafordat) + '$'
                print(strng)
                if ((milesfordat > float(maxmiles)) or (milesfordat < 0)):
                    overbudget.append(name[0:6])
                else:
                    onbudget.append(name[0:6])
                    onbudgetmls.append(milesfordat)
                    onbudgetdls.append(dollafordat)

            #donext = raw_input('press key for next:')

# allegedly now I've gone over ALL the files and found, for those dates, if I'm in budget or not... print info!
print("\nOVER THE BUDGET DESTINATIONS:")
print(overbudget)

print("\n\nPOSSIBLE DESTINATIONS:")
for j in range(0,len(onbudget)):
    strng2 = 'Fly ' + onbudget[j][0:3] + ' to ' + onbudget[j][3:] + ' for ' + str(int(onbudgetmls[j])) + ' miles + ' + str(onbudgetdls[j]) + '$'
    print(strng2)




