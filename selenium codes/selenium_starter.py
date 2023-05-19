# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
#from time import sleep

service = ChromeService(executable_path=ChromeDriverManager().install())

driver = webdriver.Chrome(service=service)

start = time.time()
driver.get("https://tw.dictionary.yahoo.com")
search = driver.find_element(By.NAME, 'p')
search.send_keys('selenium')
search.send_keys(Keys.RETURN)
#sleep(3)
#elements = WebDriverWait(driver, 20).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "div.compList.d-ib")))
elements = WebDriverWait(driver, 20).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div.compList.d-ib')))
#elements = driver.find_elements(By.CSS_SELECTOR, "div.compList.d-ib")
print(len(elements))
for element in elements:
    print(element.text)
driver.quit()
end = time.time()
print(f'duration: {end-start}')
