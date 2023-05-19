# Selenium WebDriver Python coding
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as W
from selenium.webdriver.support import expected_conditions as E
import CheckboxFunctions as C
# Import Utilities in order to call the log function.
import Utilities as U
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

URL = "https://inderpsingh.blogspot.com/2013/01/HTMLCSSQuiz1.html"
wait_time_out = 15
check_name_locator = "option"
# Specify the log file file path and file name with your computer's folder. Escape the backslashes.
# The following is an example only.
log_file = "LogCheckBoxQuiz.txt"
# Specify the log message for pass and fail.
pass_message = "Answered correctly - Question Number"
fail_message = "Answered incorrectly - Question Number"

service = ChromeService(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
wait = W(driver, wait_time_out)
driver.get(URL)
i = 0
while i<10:
    i += 1
    driver.execute_script("window.scrollBy(0,120)","")
    check_element_1 = wait.until(E.presence_of_element_located((By.NAME, check_name_locator + str(i) + "1")))
    check_element_2 = wait.until(E.presence_of_element_located((By.NAME, check_name_locator + str(i) + "2")))
    check_element_3 = wait.until(E.presence_of_element_located((By.NAME, check_name_locator + str(i) + "3")))
    check_element_1.click()
    check_element_2.click()
    check_element_3.click() # checkboxes 1, 2 & 3 are selected
    if C.answered(driver, i):
        # Python Selenium logging if the question is answered successfully
        U.log("INFO", pass_message + str(i), log_file)
        continue
    check_element_1.click() # checkboxes 2 & 3 are selected
    if C.answered(driver, i):
        # Python Selenium logging if the question is answered successfully
        U.log("INFO", pass_message + str(i), log_file)
        continue
    check_element_1.click()
    check_element_2.click() # checkboxes 1 & 3 are selected
    if C.answered(driver, i):
        # Python Selenium logging if the question is answered successfully
        U.log("INFO", pass_message + str(i), log_file)
        continue
    check_element_2.click()
    check_element_3.click() # checkboxes 1 & 2 are selected
    if C.answered(driver, i):
        # Python Selenium logging if the question is answered successfully
        U.log("INFO", pass_message + str(i), log_file)
        continue
    check_element_2.click() # only checkbox 1 is selected
    if C.answered(driver, i):
        # Python Selenium logging if the question is answered successfully
        U.log("INFO", pass_message + str(i), log_file)
        continue
    check_element_1.click()
    check_element_2.click() # only checkbox 2 is selected
    if C.answered(driver, i):
        # Python Selenium logging if the question is answered successfully
        U.log("INFO", pass_message + str(i), log_file)
        continue
    check_element_2.click()
    check_element_3.click()# only checkbox 3 is selected
    if C.answered(driver, i):
        # Python Selenium logging if the question is answered successfully
        U.log("INFO", pass_message + str(i), log_file)
        continue
    # Selenium Python logging if the question is still unanswered.
    U.log("ERROR", fail_message + str(i), log_file)
