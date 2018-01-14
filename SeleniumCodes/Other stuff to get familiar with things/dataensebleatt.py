import numpy as np
import random
import datetime

def datetostr(var):
    styr = str(var.year).zfill(4)
    stmt = str(var.month).zfill(2)
    stdy = str(var.day).zfill(2)
    dateheader = styr + stmt + stdy
    return(dateheader)

def mkrandmatn(n, *therest):
    print("INPUT data: %s" % list(therest))
    return np.random.randint(10000, size=(n, n))

# mainfunction here

ORIDES_m = np.zeros((61,60),dtype=np.int)
ORIDES_d = np.zeros((61,60),dtype=np.int)

currdate = datetime.date.today() + datetime.timedelta(days=3) # dont do anything before today

# 60 / 5 = 12 so I go from 0 to 11 and multiply by 5 to get what we want
for ii in range(0,12):
    iipos = ii * 5
    for addedval in range(0,5):
        ORIDES_m[0][iipos+addedval] = int(datetostr(currdate))
        ORIDES_d[0][iipos+addedval] = ORIDES_m[0][iipos+addedval]
        if addedval == 2:
            datestocallini = currdate
        if addedval == 3:
            datestocallfin = currdate
        currdate += datetime.timedelta(days=1)

    for jj in range(ii,12):
        jjpos = jj * 5
        
        block = mkrandmatn(5, datetostr(datestocallini), datetostr(datestocallfin +  datetime.timedelta(days=jjpos)))
        ORIDES_m[iipos+1:iipos+1+block.shape[0],jjpos:jjpos+block.shape[1]] = block
        block = block.transpose() #just for shits and giggles bhroahhj
        ORIDES_d[iipos+1:iipos+1+block.shape[0],jjpos:jjpos+block.shape[1]] = block

np.savetxt('ORIDES_m.csv',ORIDES_m)
np.savetxt('ORIDES_d.csv',ORIDES_d)
print(ORIDES_m)

