# -*- coding: utf-8 -*-
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait as W
from selenium.webdriver.support import expected_conditions as E
from selenium.webdriver.support.ui import Select

service = ChromeService(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.get(r"https://inderpsingh.blogspot.com/2014/08/demowebapp_24.html")

#distance_id_locator = "distance"

#time_id_locator = "hours"
#calculate_css_locator = ".post-body > div:nth-child(1) > div:nth-child(1) > form:nth-child(1) > button:nth-child(20)"

calculate_css_locator = "#calculate"
#result_id_locator = "result"

wait_time_out = 5
wait_variable = W(driver, wait_time_out)

test_page=wait_variable.until(E.presence_of_element_located((By.LINK_TEXT, "Useful Links")))
test_page.click()
time.sleep(1)
driver.back()

driver.execute_script("window.scrollBy(0,240)", "")


distance_element = wait_variable.until(E.presence_of_element_located((By.ID, "distance")))
speed_element = wait_variable.until(E.presence_of_element_located((By.ID, "speed")))
time_element = Select(wait_variable.until(E.presence_of_element_located((By.ID, "hours"))))
result_element = wait_variable.until(E.presence_of_element_located((By.ID, "result")))
calculate_element = wait_variable.until(E.presence_of_element_located((By.CSS_SELECTOR, calculate_css_locator)))

distance = 0         
speed = 45            
for option in time_element.options:
    distance_element.clear()
    distance += 100 
    distance_element.send_keys(distance)
    speed_element.clear()
    speed += 1 
    speed_element.send_keys(speed)
    time_element.select_by_visible_text(option.text) 
    calculate_element.click()
    time.sleep(1)
    expected_result = round(float(distance)/float(speed)/float(option.get_attribute("value")),4)
    if expected_result == int(expected_result): expected_result = int(expected_result)
    if str(expected_result) in result_element.text:
        print ("Passed", str(expected_result), result_element.text)
    else:
        print ("Failed", str(expected_result), result_element.text)
        
       

