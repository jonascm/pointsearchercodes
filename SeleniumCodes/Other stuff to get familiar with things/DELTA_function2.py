# here I want to copy function1 but keep the navigator open...
# I may need to pass the driver (?)
# dale

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

import numpy as np
import csv

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
        return(-1)
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
        return(-1)

    try:
        kuky = driver.find_element_by_xpath("//*[@id='ck-banner-close']").click()
    except NoSuchElementException:
        pass
    
    try:
        elem5 = driver.find_element_by_xpath("//*[@id='findFlightsSubmit']").click()
    # wait for the shit to load
    
    except NoSuchElementException:
        print('Error loading page')
        return(-1)

    elem6 = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//*[@id='selector_3_3']/a")))
    
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


# main function here

print('This CODE runs a search on Delta and finds miles and money cost... it is an awesome Jonasito cretaion #majo')

drover = webdriver.Firefox()
result = findDELTA(drover,"ATL", "12252017", "AMS", "12312017")

print('Mile prices')
print(result[0])
print('Money prices')
print(result[1])
# next goes on too soon!!! gosh -.-
#result2 = findDELTAnext(drover,"ATL", "12/25/2017", "AMS", "12/31/2017")

#print('Mile prices')
#print(result2[0])
#print('Money prices')
#print(result2[1])

drover.close()



