# -*- coding: utf-8 -*-
"""
Created on Sun Apr 30 03:42:39 2023

@author: 123
"""
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import StaleElementReferenceException

service = ChromeService(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.get("https://orteil.dashnet.org/cookieclicker/")

driver.implicitly_wait(20)
select=driver.find_element(By.ID,"langSelect-ZH-CN")
select.click()

time.sleep(3)

cookie=driver.find_element(By.ID, 'bigCookie')
cookie_count=driver.find_element(By.ID, 'cookies')
items=[driver.find_element(By.ID, "productPrice"+str(i)) for i in range(1,-1,-1)]

action=ActionChains(driver)

for i in range(10000):
    action.click(cookie).perform()
    count=int(cookie_count.text.split(" ")[0])
    for item in items:
        value=int(item.text)
        if value<=count:
            upgrade_actions=ActionChains(driver)
            upgrade_actions.move_to_element(item)
            upgrade_actions.click().perform()

