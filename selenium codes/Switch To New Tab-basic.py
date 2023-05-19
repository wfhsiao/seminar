# -*- coding: utf-8 -*-

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

service = ChromeService(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)


languages = ["en", "zh", "ja"]
driver.get("https://www.wikipedia.org/")#維基百科
for i in range(len(languages)):
    driver.execute_script("window.open()")
    driver.switch_to.window(driver.window_handles[i+1])
    language_URL="http://"+languages[i]+".wikipedia.org/"
    driver.get(language_URL)

'''
#測試打開學校網站
new_tab = ["404-1000-60341", "412-1000-3309"]
driver.get("https://www.nptu.edu.tw/")
for i in range(len(new_tab)):
    driver.execute_script("window.open()")
    driver.switch_to.window(driver.window_handles[i+1])
    language_URL="https://www.nptu.edu.tw/p/"+new_tab[i]+".php?"
    driver.get(language_URL)

'''

#print("Window handle of the current window is", driver.current_window_handle)
#print(language_URL,driver.window_handles[i+1],driver.title,driver.current_url)
