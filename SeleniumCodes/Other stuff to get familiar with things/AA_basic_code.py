from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.action_chains import ActionChains
import numpy as np
import csv
import time
import random

driver = webdriver.Firefox()
driver.get("https://www.aa.com/booking/find-flights")
assert "American" in driver.title

#kuky = driver.find_element_by_xpath("//*[@id='ck-banner-close']").click()
elem4 = driver.find_element_by_xpath("//*[@id='flightSearchView']/div/div[1]/div[2]/label/span[1]").click()

elem1 = driver.find_element_by_xpath("//*[@id='segments0.origin']")
elem1.clear()
elem1.send_keys("ATL")
elem1.send_keys(Keys.DOWN)

elem2 = driver.find_element_by_xpath("//*[@id='segments0.destination']")
elem2.clear()
elem2.send_keys("JFK")
elem2.send_keys(Keys.DOWN)
#elem2.send_keys(Keys.RETURN)

elem3 = driver.find_element_by_xpath("//*[@id='segments0.travelDate']")
elem3.clear()
elem3.send_keys("02/11/2018")
#elem3.send_keys(Keys.RETURN)


elem3 = driver.find_element_by_xpath("//*[@id='segments1.travelDate']")
elem3.clear()
elem3.send_keys("02/17/2018")
#elem3.send_keys(Keys.RETURN)

#this works nicely :-P
elem5 = driver.find_element_by_xpath("//*[@id='flightSearchSubmitBtn']")
driver.execute_script("return arguments[0].scrollIntoView();", elem5)
scawl = ActionChains(driver).move_to_element(elem5).perform()
time.sleep(4.7)
elem5 = driver.find_element_by_xpath("//*[@id='flightSearchSubmitBtn']").click()

# THIS WORKED:
#elem5 = driver.find_element_by_xpath("//*[@id='flightSearchSubmitBtn']").click()
# #raises error
#time.sleep(5.0)
#driver.back()
#elem5 = driver.find_element_by_xpath("//*[@id='flightSearchSubmitBtn']")
#hoverover =ActionChains(driver).move_to_element(elem5).perform()
#time.sleep(0.7)
#elem5 = driver.find_element_by_xpath("//*[@id='flightSearchSubmitBtn']").click()

# wait for the shit to load 
elem6 = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//*[@id='calContainer_0']/ul[2]/li")))
elem7 = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//*[@id='calContainer_1']/ul[2]/li")))

# lemme try to open the whole month and get all the data

monthdatumup = driver.find_element_by_xpath("//*[@id='calTabLink_0']/span").click()
elem8 = driver.find_element_by_xpath("//*[@id='calContainer_0']")
monthdatumdown = driver.find_element_by_xpath("//*[@id='calTabLink_1']/span").click()
elem9 = driver.find_element_by_xpath("//*[@id='calContainer_1']")

idainfo = elem8.text
vueltainfo = elem9.text

print('\n\n IDAS')
print(idainfo)
print('\n\n VUELTAS')
print(vueltainfo)
print('\n\n')


idaspl = idainfo.split("\n")
for ix in range(0,len(idaspl)):
    if 'K' in idaspl[ix]:
        milesi = int(1000.0*float(idaspl[ix].replace('K','')))
        infi = idaspl[ix-4]+' '+idaspl[ix-3]+' '+idaspl[ix-2]+' '+str(milesi)+' miles'
        print(infi)

vueltaspl = vueltainfo.split("\n")
for ix in range(0,len(vueltaspl)):
    if 'K' in vueltaspl[ix]:
        milesv = int(1000.0*float(vueltaspl[ix].replace('K','')))
        infv = vueltaspl[ix-4]+' '+vueltaspl[ix-3]+' '+vueltaspl[ix-2]+' '+str(milesv)+' miles'
        print(infv)
