from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import numpy as np
import csv



driver = webdriver.Firefox()
driver.get("http://www.delta.com")
assert "Delta" in driver.title

#elem = driver.find_element_by_name("Book a Trip")
#elem.send_keys(Keys.CLICK)
#kuky = driver.find_element_by_xpath("//*[@id='ck-banner-close']").click()
#elem2 = driver.find_element_by_name("destinationCity")
elem2 = driver.find_element_by_xpath("//*[@id='destinationCity']")
elem2.clear()
elem2.send_keys("BCN")
elem2.send_keys(Keys.DOWN)
elem2.send_keys(Keys.RETURN)

elem3 = driver.find_element_by_xpath("//*[@id='departureDate']")
elem3.clear()
elem3.send_keys("02112018")
elem3.send_keys(Keys.RETURN)

elem3 = driver.find_element_by_xpath("//*[@id='returnDate']")
elem3.clear()
elem3.send_keys("02172018")
elem3.send_keys(Keys.RETURN)
elem4 = driver.find_element_by_xpath("//*[@id='milesBtn']").click()

elem5 = driver.find_element_by_xpath("//*[@id='findFlightsSubmit']").click()
# wait for the shit to load

elem6 = WebDriverWait(driver, 300).until(EC.presence_of_element_located((By.XPATH, "//*[@id='selector_3_3']/a")))

#print(elem6.text)
elem7 = driver.find_element_by_xpath("//*[@id='selector_3_3']/a/span[1]")
#print(elem7.text)
#np.save('file_something.npy',elem6.text)

rawstr = str(elem6.text)

for char in rawstr:
    if char in ",?.!/;:":
        rawstr = rawstr.replace(char,'')

compons = rawstr.split(" ")

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


print("You can fly for " + str(miles) + " miles plus $" + str(dolla) + "." + str(cents))

driver.close()

