# Selenium WebDriver Python coding
# Import webdriver library to use the Selenium WebDriver commands.
from selenium import webdriver
# Import the By library to find the links on the web page.
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as W
from selenium.webdriver.support import expected_conditions as E
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

URL = "https://inderpsingh.blogspot.com/"
wait_time_out = 15
service = ChromeService(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
# Navigate to the URL.
driver.get(URL)
wait_variable = W(driver, wait_time_out)
# We need to find the link before Python Selenium click link .
# Define the Python list called links.
links = wait_variable.until(E.visibility_of_any_elements_located((By.TAG_NAME, "a")))
print ("The total number of links is", len(links))
# Use for each loop to python selenium loop through links. It takes time to loop through links.
for link in links:
    print (link.text) # Selenium link text
# Selenium link click on the "Selenium Python Tutorials" link using WebDriverWait Python
wait_variable.until(E.element_to_be_clickable((By.LINK_TEXT, "Selenium Python Tutorials"))).click()
# Go back to the home page.
#driver.back()
# Click the same link but with the partial link text to Selenium link click Python.
#wait_variable.until(E.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "Selenium Python"))).click()

time.sleep(5)
driver.quit()
