# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

def obtainFundayTitles(driver, rowId):
    gridL0 = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.ID, rowId)))
    #elements = gridL0.find_elements(By.XPATH, '//*[starts-with(@id, "DV-")]')
    elements = gridL0.find_elements(By.CSS_SELECTOR, '[id^="DV-"]')
    res = {}
    for element in elements:
        try:
            newsSlogan=element.find_element(By.CSS_SELECTOR, '[id^="newsSlogan_"]')
            newsTitle=element.find_element(By.CSS_SELECTOR, '[id^="newsTitle_"]')
            res[newsSlogan.text]=newsTitle.text
        except:
            pass
    return res
    
if __name__=='__main__':
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    
    start = time.time()
    driver.get("https://tts-nptu.funday.asia/")
    email = driver.find_element(By.NAME, 'email')
    email.send_keys('BBF110008')
    passwd = driver.find_element(By.NAME, 'password')
    passwd.send_keys('BBF110008')
    #passwd.send_keys(Keys.RETURN)
    passwd.submit()
    res = obtainFundayTitles(driver, "gridL0")
    print(res)
    driver.quit()
    end = time.time()
    print(f'duration: {end-start}')
