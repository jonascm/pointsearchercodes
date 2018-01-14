# ISSUES: goes too fast, DELTA blocks me after a while, for some time...
# bypasses: check here: https://www.scrapehero.com/how-to-prevent-getting-blacklisted-while-scraping/


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
import numpy as np
import random
import datetime
import csv

def datetostr(var):
    styr = str(var.year).zfill(4)
    stmt = str(var.month).zfill(2)
    stdy = str(var.day).zfill(2)
    dateheader = stmt + stdy + styr
    return(dateheader)


# Extract data from DELTA string withdrawn
def extractvalsdelta(datstr):
    
    if datstr == 'NOT AVAILABLE':
         # or similar I guess... -.-
         return([-1,-1])
    
    for char in datstr:
        if char in ",?.!/;:":
            datstr = datstr.replace(char,'')
    compons = datstr.split(" ")
    counter = 0
    for els in compons[9:]:
        if els.isdigit():
            if counter == 2:
                cents = int(els)
                counter += 1
            if counter == 1:
                dolla = int(els)
                counter += 1
            if counter == 0:
                miles = int(els)
                counter += 1
    return([miles,float(dolla)+0.01*float(cents)])
# cool I guess


# DELTA function
def findDELTA(driver,oriloc, oridat, desloc, desdat):
    
    try:
        driver.get("http://www.delta.com")
        assert "Delta" in driver.title
    except AssertionError:
        print('Error loading page')
        return([np.matrix([-1],dtype=np.int),np.matrix([-1],dtype=np.int)])
    try:
        elem1 = driver.find_element_by_xpath("//*[@id='originCity']")
        elem1.clear()
        elem1.send_keys(oriloc)
        elem1.send_keys(Keys.DOWN)
        elem1.send_keys(Keys.RETURN)

        elem2 = driver.find_element_by_xpath("//*[@id='destinationCity']")
        elem2.clear()
        elem2.send_keys(desloc)
        elem2.send_keys(Keys.DOWN)
        elem2.send_keys(Keys.RETURN)
        
        elem3 = driver.find_element_by_xpath("//*[@id='departureDate']")
        elem3.clear()
        elem3.send_keys(oridat)
        elem3.send_keys(Keys.RETURN)
        
        elem3 = driver.find_element_by_xpath("//*[@id='returnDate']")
        elem3.clear()
        elem3.send_keys(desdat)
        elem3.send_keys(Keys.RETURN)
        elem4 = driver.find_element_by_xpath("//*[@id='milesBtn']").click()
    except NoSuchElementException:
        print('Error loading page')
        return([np.matrix([-1],dtype=np.int),np.matrix([-1],dtype=np.int)])

    try:
        kuky = driver.find_element_by_xpath("//*[@id='ck-banner-close']").click()
    except NoSuchElementException:
        pass
    
    try:
        elem5 = driver.find_element_by_xpath("//*[@id='findFlightsSubmit']").click()
    # wait for the shit to load
    
    except NoSuchElementException:
        print('Error loading page')
        return(np.matrix([-1],dtype=np.int))
    try:
        elem6 = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//*[@id='selector_3_3']")))
    except TimeoutException:
        print('Error loading page')
        return([np.matrix([-1],dtype=np.int),np.matrix([-1],dtype=np.int)])

    for vari in range(0,7):
        for varj in range(0,7):
            try:
                strini = 'el' + str(vari) + str(varj) + ' = str(driver.find_element_by_xpath("'
                strmid = "//*[@id='selector_" + str(vari) + "_" + str(varj) + "']/a/span[1]"
                strend = '").text)'
                strall = strini + strmid + strend
                exec(strall) # this makes the texts in the vars named el11, el12,...
            except NoSuchElementException:
                strexc = 'el' + str(vari) + str(varj) + " = 'NOT AVAILABLE'"
                exec(strexc)
                pass
    #el33 = str(driver.find_element_by_xpath("//*[@id='selector_3_3']/a/span[1]").text)   
    
    for vari in range(0,7):
        for varj in range(0,7):
            strg1 = 'data' + str(vari) + str(varj) + ' = extractvalsdelta(el' + str(vari) + str(varj) + ')'
            exec(strg1) # this extracts values and give an array with [miles, money]
    
    # now I just need to make the numpy matrix miles and the money one
    deltamiles = np.matrix([[data00[0], data01[0], data02[0], data03[0], data04[0], data05[0], data06[0]],[data10[0], data11[0], data12[0], data13[0], data14[0], data15[0], data16[0]],[data20[0],data21[0], data22[0], data23[0], data24[0], data25[0], data26[0]],[data30[0],data31[0], data32[0], data33[0], data34[0], data35[0], data36[0]],[data40[0],data41[0], data42[0], data43[0], data44[0], data45[0], data46[0]],[data50[0],data51[0], data52[0], data53[0], data54[0], data55[0], data56[0]],[data60[0],data61[0], data62[0], data63[0], data64[0], data65[0], data66[0]]])

    deltamoney = np.matrix([[data00[1], data01[1], data02[1], data03[1], data04[1], data05[1], data06[1]],[data10[1], data11[1], data12[1], data13[1], data14[1], data15[1], data16[1]],[data20[1],data21[1], data22[1], data23[1], data24[1], data25[1], data26[1]],[data30[1],data31[1], data32[1], data33[1], data34[1], data35[1], data36[1]],[data40[1],data41[1], data42[1], data43[1], data44[1], data45[1], data46[1]],[data50[1],data51[1], data52[1], data53[1], data54[1], data55[1], data56[1]],[data60[1],data61[1], data62[1], data63[1], data64[1], data65[1], data66[1]]])
    return([deltamiles, deltamoney])



# mainfunction here
cities_usa = ["ATL","JFK","LGA","SFO","LAX","MIA","FLL","MSY","BOS","ORD","HOU","SLC","CLT","SEA","MSP"]
cities_caribbean = ["MEX","CUN","PTY","SJO","NAS","PUJ","MBJ","SJU","SLU","AUA"]
cities_latam = ["EZE","RIO","BOG","CTG","LIM","SCL","UIO","MAO"]
cities_europe = ["BCN","MAD","CDG","HTR","DUS","ATH","FCO","OSL","MOW","DUB","PRG","WAW","BER","AMS","IST"]
cities_africa = ["JNB","LOS","CAI","NBO","CAS"]
cities_asia = ["NRT","JKT","TLV","SYD","SHA","DXB","BOM"]

citini = "ATL"
numofdates = 70
sizeretmat = 7
numofsearches = numofdates/sizeretmat

drover = webdriver.Firefox()

for citifin in cities_africa:
    currdate = datetime.date.today() + datetime.timedelta(days=3) # dont do anything before today
    # need to update the date to present otherwise I just move onto foreva
    if citini != citifin:
        oridesM_strg = citini + citifin + "_m.csv"
        oridesD_strg = citini + citifin + "_d.csv"

        ORIDES_m = (-1)*np.ones((numofdates+1,numofdates),dtype=np.int)
        ORIDES_d = (-1)*np.ones((numofdates+1,numofdates),dtype=np.int)

        for ii in range(0,numofsearches):
            iipos = ii * sizeretmat
            for addedval in range(0,sizeretmat):
                ORIDES_m[0][iipos+addedval] = int(datetostr(currdate + datetime.timedelta(days=1)))
                ORIDES_d[0][iipos+addedval] = ORIDES_m[0][iipos+addedval]
                if addedval == 3:
                    datestocallini = currdate
                if addedval == 4:
                    datestocallfin = currdate
                currdate += datetime.timedelta(days=1)
        
            for jj in range(ii,numofsearches):
                jjpos = jj * sizeretmat
                
                #block = mkrandmatn(sizeretmat, datetostr(datestocallini), datetostr(datestocallfin +  datetime.timedelta(days=jjpos)))
                block = findDELTA(drover,citini, datetostr(datestocallini), citifin, datetostr(datestocallfin +  datetime.timedelta(days=jjpos))) #block[0] are miles, block[1] are dollars
                ORIDES_m[iipos+1:iipos+1+block[0].shape[0],jjpos:jjpos+block[0].shape[1]] = block[0]
                ORIDES_d[iipos+1:iipos+1+block[1].shape[0],jjpos:jjpos+block[1].shape[1]] = block[1]

        np.savetxt(oridesM_strg,ORIDES_m)
        np.savetxt(oridesD_strg,ORIDES_d)
    print('StepDone')

drover.close()

