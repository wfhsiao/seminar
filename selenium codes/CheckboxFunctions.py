# Selenium WebDriver Python coding
from selenium.webdriver.common.by import By
# The following two import statements are for webdriverwait Python (explicit wait).
from selenium.webdriver.support.ui import WebDriverWait as W
from selenium.webdriver.support import expected_conditions as E
import time
wait_time_out = 15

def answered(d, question_number):
    # function documentation on the next line
    """Locate the answer element. Return True or False based on the value attribute."""
    wait_variable = W(d, wait_time_out)
    answer_element = wait_variable.until(E.presence_of_element_located((By.NAME, "answer" + str(question_number))))
    time.sleep(0.25)
    if "Correct." in answer_element.get_attribute("value"):
        return True
    else:
        return False
