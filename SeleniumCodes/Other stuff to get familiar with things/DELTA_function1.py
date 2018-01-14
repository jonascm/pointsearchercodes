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
def find5by5delta(oriloc, oridat, desloc, desdat):
    driver = webdriver.Firefox()
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
        
        elem5 = driver.find_element_by_xpath("//*[@id='findFlightsSubmit']").click()
    # wait for the shit to load
    
    except NoSuchElementException:
        print('Error loading page')
        return(-1)

    elem6 = WebDriverWait(driver, 300).until(EC.presence_of_element_located((By.XPATH, "//*[@id='selector_3_3']/a")))
    
    for vari in range(1,6):
        for varj in range(1,6):
            strini = 'el' + str(vari) + str(varj) + ' = str(driver.find_element_by_xpath("'
            strmid = "//*[@id='selector_" + str(vari) + "_" + str(varj) + "']/a/span[1]"
            strend = '").text)'
            strall = strini + strmid + strend
            exec(strall) # this makes the texts in the vars named el11, el12,...
    
    #el33 = str(driver.find_element_by_xpath("//*[@id='selector_3_3']/a/span[1]").text)   
    
    for vari in range(1,6):
        for varj in range(1,6):
            strg1 = 'data' + str(vari) + str(varj) + ' = extractvalsdelta(el' + str(vari) + str(varj) + ')'
            exec(strg1) # this extracts values and give an array with [miles, money]
    
    # now I just need to make the numpy matrix miles and the money one
    deltamiles = np.matrix([[data11[0], data12[0], data13[0], data14[0], data15[0]],[data21[0], data22[0], data23[0], data24[0], data25[0]],[data31[0], data32[0], data33[0], data34[0], data35[0]],[data41[0], data42[0], data43[0], data44[0], data45[0]],[data51[0], data52[0], data53[0], data54[0], data55[0]]])

    deltamoney = np.matrix([[data11[1], data12[1], data13[1], data14[1], data15[1]],[data21[1], data22[1], data23[1], data24[1], data25[1]],[data31[1], data32[1], data33[1], data34[1], data35[1]],[data41[1], data42[1], data43[1], data44[1], data45[1]],[data51[1], data52[1], data53[1], data54[1], data55[1]]])

    driver.close()
    
    return([deltamiles, deltamoney])


# main function here

print('This CODE runs a search on Delta and finds a 5-by-5 matrix with miles and money cost... The function defined opens and closes the navigator each time')
result = find5by5delta("ATL", "02112018", "AMS", "02192018")
print('Mile prices')
print(result[0])
print('Money prices')
print(result[1])



